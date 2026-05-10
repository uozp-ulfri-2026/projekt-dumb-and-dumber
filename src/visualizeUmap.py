from __future__ import annotations

import argparse
import hashlib
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import plotly.colors as plotly_colors
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans

import umap


LOGGER = logging.getLogger("visualize_umap")


def load_metadata(path: Path) -> list[dict[str, Any]]:
    metadata: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as source_file:
        for line in source_file:
            line = line.strip()
            if not line:
                continue
            metadata.append(json.loads(line))
    return metadata


def sample_indices(total: int, sample_size: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if total <= sample_size:
        return np.arange(total, dtype=np.int64)
    return np.sort(rng.choice(total, size=sample_size, replace=False).astype(np.int64))


def resolve_output_path(path: Path, default_name: str) -> Path:
    if path.suffix:
        return path
    return path / default_name


def build_cache_key(
    embeddings_path: Path,
    metadata_path: Path,
    sample_size: int,
    seed: int,
    umap_neighbors: int,
    umap_min_dist: float,
    n_clusters: int,
) -> str:
    parts = [
        str(embeddings_path.resolve()),
        str(embeddings_path.stat().st_size),
        str(embeddings_path.stat().st_mtime_ns),
        str(metadata_path.resolve()),
        str(metadata_path.stat().st_size),
        str(metadata_path.stat().st_mtime_ns),
        str(sample_size),
        str(seed),
        str(umap_neighbors),
        str(umap_min_dist),
        str(n_clusters),
        "umap-v1",
    ]
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()
    return digest[:16]


def load_or_compute_projection(
    embeddings: np.ndarray,
    embeddings_path: Path,
    metadata: list[dict[str, Any]],
    metadata_path: Path,
    sample_size: int,
    seed: int,
    umap_neighbors: int,
    umap_min_dist: float,
    n_clusters: int,
    cache_dir: Path,
    force_recompute: bool,
) -> dict[str, Any]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_key = build_cache_key(
        embeddings_path=embeddings_path,
        metadata_path=metadata_path,
        sample_size=sample_size,
        seed=seed,
        umap_neighbors=umap_neighbors,
        umap_min_dist=umap_min_dist,
        n_clusters=n_clusters,
    )
    cache_path = cache_dir / f"umap_{cache_key}.npz"

    if cache_path.exists() and not force_recompute:
        LOGGER.info("Loading cached UMAP projection from %s", cache_path)
        cached = np.load(cache_path, allow_pickle=False)
        return {
            "sample_indices": cached["sample_indices"],
            "coordinates": cached["coordinates"],
            "cluster_labels": cached["cluster_labels"],
            "cache_path": cache_path,
        }

    LOGGER.info("Sampling %d articles for visualization", sample_size)
    indices = sample_indices(len(metadata), sample_size, seed)
    sample_embeddings = embeddings[indices]

    effective_clusters = min(n_clusters, len(indices))
    effective_clusters = max(2, effective_clusters)

    LOGGER.info(
        "Computing KMeans clusters (%d) and 2D UMAP (n_neighbors=%d, min_dist=%.3f)",
        effective_clusters,
        umap_neighbors,
        umap_min_dist,
    )
    cluster_model = KMeans(n_clusters=effective_clusters, random_state=seed, n_init="auto")
    cluster_labels = cluster_model.fit_predict(sample_embeddings).astype(np.int32, copy=False)

    effective_neighbors = min(umap_neighbors, max(2, len(indices) - 1))
    if effective_neighbors != umap_neighbors:
        LOGGER.info("Adjusted UMAP n_neighbors to %d for the sampled dataset size", effective_neighbors)

    reducer = umap.UMAP(
        n_components=2,
        metric="cosine",
        n_neighbors=effective_neighbors,
        min_dist=umap_min_dist,
        random_state=seed,
    )
    coordinates = reducer.fit_transform(sample_embeddings).astype(np.float32, copy=False)

    np.savez_compressed(
        cache_path,
        sample_indices=indices,
        coordinates=coordinates,
        cluster_labels=cluster_labels,
    )
    LOGGER.info("Saved UMAP cache to %s", cache_path)

    return {
        "sample_indices": indices,
        "coordinates": coordinates,
        "cluster_labels": cluster_labels,
        "cache_path": cache_path,
    }


def build_plot_data(
    metadata: list[dict[str, Any]],
    sample_indices: np.ndarray,
    coordinates: np.ndarray,
    cluster_labels: np.ndarray,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for sample_row, original_index in enumerate(sample_indices):
        article = metadata[int(original_index)]
        rows.append(
            {
                "x": float(coordinates[sample_row, 0]),
                "y": float(coordinates[sample_row, 1]),
                "original_index": int(original_index),
                "cluster": f"Cluster {int(cluster_labels[sample_row]) + 1}",
                "topic": str(article.get("category", "") or "Uncategorized"),
                "title": article.get("title", ""),
                "date": article.get("date", ""),
                "url": article.get("url", ""),
                "keywords": ", ".join(article.get("keywords", [])[:8]),
            }
        )
    return rows


def _color_for_index(index: int) -> str:
    palette = plotly_colors.qualitative.Set3
    return palette[index % len(palette)]


def _group_traces(
    plot_rows: list[dict[str, Any]],
    group_key: str,
    axis_name: str,
    show_legend: bool = True,
) -> list[go.Scattergl]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in plot_rows:
        grouped.setdefault(str(row[group_key]), []).append(row)

    traces: list[go.Scattergl] = []
    for index, (group_name, group_rows) in enumerate(sorted(grouped.items(), key=lambda item: item[0])):
        traces.append(
            go.Scattergl(
                x=[row["x"] for row in group_rows],
                y=[row["y"] for row in group_rows],
                mode="markers",
                name=group_name,
                legendgroup=f"{axis_name}:{group_name}",
                showlegend=show_legend,
                marker={"color": _color_for_index(index), "size": 6, "opacity": 0.78, "line": {"width": 0}},
                customdata=[
                    [
                        row["title"],
                        row["cluster"],
                        row["topic"],
                        row["date"],
                        row["keywords"],
                        row["url"],
                        row["original_index"],
                    ]
                    for row in group_rows
                ],
                hovertemplate=(
                    "<b>%{customdata[0]}</b><br>"
                    "Cluster: %{customdata[1]}<br>"
                    "Topic: %{customdata[2]}<br>"
                    "Date: %{customdata[3]}<br>"
                    "Keywords: %{customdata[4]}<br>"
                    "<extra></extra>"
                ),
            )
        )
    return traces


def build_figure(plot_rows: list[dict[str, Any]], total_articles: int) -> go.Figure:
    fig = make_subplots(
        rows=1,
        cols=2,
        shared_xaxes=True,
        shared_yaxes=True,
        subplot_titles=("Colored by clustering", "Colored by topics"),
        horizontal_spacing=0.07,
    )

    for trace in _group_traces(plot_rows, group_key="cluster", axis_name="cluster", show_legend=True):
        fig.add_trace(trace, row=1, col=1)

    for trace in _group_traces(plot_rows, group_key="topic", axis_name="topic", show_legend=False):
        fig.add_trace(trace, row=1, col=2)

    fig.update_layout(
        template="plotly_white",
        width=1800,
        height=900,
        title={"text": f"MMC articles UMAP ({len(plot_rows)} sampled from {total_articles})", "x": 0.5},
        legend_title_text="Cluster",
    )
    fig.update_xaxes(title_text="UMAP 1")
    fig.update_yaxes(title_text="UMAP 2")
    return fig


def build_faiss_search_script() -> str:
    return r"""
(function () {
    const graph = document.getElementById("{plot_id}");
    if (!graph || graph.dataset.faissSearchMounted === "true") {
        return;
    }
    graph.dataset.faissSearchMounted = "true";

    const style = document.createElement("style");
    style.textContent = `
        .faiss-search-panel {
            box-sizing: border-box;
            width: min(1800px, calc(100vw - 32px));
            margin: 16px auto 8px;
            padding: 12px 14px;
            border: 1px solid #d8dee9;
            border-radius: 8px;
            background: #ffffff;
            font-family: Arial, sans-serif;
            color: #1f2937;
        }
        .faiss-search-form {
            display: grid;
            grid-template-columns: minmax(220px, 1fr) auto auto;
            gap: 8px;
            align-items: center;
        }
        .faiss-search-input {
            min-width: 0;
            height: 38px;
            padding: 0 11px;
            border: 1px solid #c9d1db;
            border-radius: 6px;
            font-size: 14px;
        }
        .faiss-search-button,
        .faiss-reset-button {
            height: 38px;
            padding: 0 13px;
            border: 1px solid #1d4ed8;
            border-radius: 6px;
            background: #2563eb;
            color: #ffffff;
            font-size: 14px;
            cursor: pointer;
        }
        .faiss-reset-button {
            border-color: #c9d1db;
            background: #ffffff;
            color: #1f2937;
        }
        .faiss-search-button:disabled,
        .faiss-reset-button:disabled {
            cursor: progress;
            opacity: 0.72;
        }
        .faiss-search-status {
            margin-top: 9px;
            min-height: 20px;
            font-size: 13px;
            line-height: 1.4;
        }
        .faiss-search-status a {
            color: #1d4ed8;
            text-decoration: none;
        }
        .faiss-search-status a:hover {
            text-decoration: underline;
        }
        @media (max-width: 720px) {
            .faiss-search-form {
                grid-template-columns: 1fr;
            }
        }
    `;
    document.head.appendChild(style);

    const panel = document.createElement("section");
    panel.className = "faiss-search-panel";
    panel.innerHTML = `
        <form class="faiss-search-form">
            <input class="faiss-search-input" name="query" type="search" placeholder="FAISS search top 1..." autocomplete="off" />
            <button class="faiss-search-button" type="submit">Search</button>
            <button class="faiss-reset-button" type="button">Reset view</button>
        </form>
        <div class="faiss-search-status">Za FAISS search odpri stran prek lokalnega serverja: python src/serveUmapSearch.py</div>
    `;
    graph.parentNode.insertBefore(panel, graph);

    const form = panel.querySelector("form");
    const input = panel.querySelector(".faiss-search-input");
    const submitButton = panel.querySelector(".faiss-search-button");
    const resetButton = panel.querySelector(".faiss-reset-button");
    const status = panel.querySelector(".faiss-search-status");

    function setStatus(message, isHtml) {
        if (isHtml) {
            status.innerHTML = message;
            return;
        }
        status.textContent = message;
    }

    function escapeHtml(value) {
        return String(value || "").replace(/[&<>"']/g, function (char) {
            return {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#39;"
            }[char];
        });
    }

    function buildPointLookup() {
        const lookup = new Map();
        for (const trace of graph.data || []) {
            if (trace.meta && trace.meta.faissHighlight) {
                continue;
            }
            const customRows = trace.customdata || [];
            for (let i = 0; i < customRows.length; i += 1) {
                const custom = customRows[i];
                if (!Array.isArray(custom) || custom.length < 7) {
                    continue;
                }
                const articleIndex = String(custom[6]);
                if (!lookup.has(articleIndex)) {
                    lookup.set(articleIndex, []);
                }
                lookup.get(articleIndex).push({
                    x: trace.x[i],
                    y: trace.y[i],
                    xaxis: trace.xaxis || "x",
                    yaxis: trace.yaxis || "y",
                    title: custom[0],
                    topic: custom[2],
                    date: custom[3],
                    url: custom[5],
                    originalIndex: custom[6]
                });
            }
        }
        return lookup;
    }

    function clearHighlights() {
        const indices = [];
        for (let i = 0; i < (graph.data || []).length; i += 1) {
            const trace = graph.data[i];
            if (trace.meta && trace.meta.faissHighlight) {
                indices.push(i);
            }
        }
        if (indices.length > 0) {
            return Plotly.deleteTraces(graph, indices.reverse());
        }
        return Promise.resolve();
    }

    function axisLayoutName(axisRef) {
        return axisRef === "x" || axisRef === "y" ? axisRef + "axis" : axisRef.replace(/^([xy])/, "$1axis");
    }

    function currentBounds(axisName, coordinateKey) {
        const layoutAxis = graph.layout[axisName] || {};
        if (Array.isArray(layoutAxis.range) && layoutAxis.range.length === 2) {
            return [Number(layoutAxis.range[0]), Number(layoutAxis.range[1])];
        }

        let min = Infinity;
        let max = -Infinity;
        for (const trace of graph.data || []) {
            if (trace.meta && trace.meta.faissHighlight) {
                continue;
            }
            const values = trace[coordinateKey] || [];
            for (const value of values) {
                const numeric = Number(value);
                if (Number.isFinite(numeric)) {
                    min = Math.min(min, numeric);
                    max = Math.max(max, numeric);
                }
            }
        }
        if (!Number.isFinite(min) || !Number.isFinite(max) || min === max) {
            return [-1, 1];
        }
        return [min, max];
    }

    function focusMatches(matches) {
        const relayout = {};
        const seen = new Set();
        for (const match of matches) {
            const xAxis = axisLayoutName(match.xaxis);
            const yAxis = axisLayoutName(match.yaxis);
            const key = xAxis + "|" + yAxis;
            if (seen.has(key)) {
                continue;
            }
            seen.add(key);

            const xBounds = currentBounds(xAxis, "x");
            const yBounds = currentBounds(yAxis, "y");
            const xPad = Math.max(Math.abs(xBounds[1] - xBounds[0]) * 0.08, 0.35);
            const yPad = Math.max(Math.abs(yBounds[1] - yBounds[0]) * 0.08, 0.35);
            relayout[xAxis + ".range"] = [Number(match.x) - xPad, Number(match.x) + xPad];
            relayout[yAxis + ".range"] = [Number(match.y) - yPad, Number(match.y) + yPad];
        }
        return Object.keys(relayout).length > 0 ? Plotly.relayout(graph, relayout) : Promise.resolve();
    }

    async function highlight(matches) {
        await clearHighlights();
        const traces = matches.map(function (match) {
            return {
                x: [match.x],
                y: [match.y],
                xaxis: match.xaxis,
                yaxis: match.yaxis,
                mode: "markers",
                name: "FAISS top 1",
                showlegend: false,
                hovertemplate: "<b>%{customdata[0]}</b><br>FAISS top 1<br><extra></extra>",
                customdata: [[match.title]],
                marker: {
                    symbol: "star",
                    size: 20,
                    color: "#ef4444",
                    line: {color: "#111827", width: 2}
                },
                meta: {faissHighlight: true}
            };
        });
        if (traces.length > 0) {
            await Plotly.addTraces(graph, traces);
        }
        await focusMatches(matches);
    }

    function resultHtml(result, prefix) {
        const title = escapeHtml(result.title || "Brez naslova");
        const score = Number.isFinite(Number(result.score)) ? Number(result.score).toFixed(4) : "";
        const url = result.url ? String(result.url) : "";
        const link = url ? `<a href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${title}</a>` : title;
        const suffix = score ? ` (score ${score})` : "";
        return `${escapeHtml(prefix)} ${link}${suffix}`;
    }

    graph.on("plotly_click", function (eventData) {
        const point = eventData.points && eventData.points[0];
        if (!point || point.data && point.data.meta && point.data.meta.faissHighlight) {
            return;
        }

        const custom = point.customdata;
        if (!Array.isArray(custom) || !custom[5]) {
            return;
        }

        const articleWindow = window.open(String(custom[5]), "_blank", "noopener,noreferrer");
        if (articleWindow) {
            articleWindow.opener = null;
        }
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        const query = input.value.trim();
        if (!query) {
            input.focus();
            return;
        }

        submitButton.disabled = true;
        setStatus("Searching FAISS top 1...");
        try {
            const response = await fetch("/api/search?query=" + encodeURIComponent(query), {
                headers: {"Accept": "application/json"}
            });
            if (!response.ok) {
                throw new Error("HTTP " + response.status);
            }
            const payload = await response.json();
            const result = payload.result;
            if (!result) {
                await clearHighlights();
                setStatus("Ni zadetka.");
                return;
            }

            const matches = buildPointLookup().get(String(result.article_index)) || [];
            if (matches.length === 0) {
                await clearHighlights();
                setStatus(resultHtml(result, "Top 1 ni v trenutnem UMAP vzorcu:"), true);
                return;
            }

            await highlight(matches);
            setStatus(resultHtml(result, "Top 1:"), true);
        } catch (error) {
            setStatus("FAISS endpoint ni dosegljiv. Zaženi: python src/serveUmapSearch.py");
        } finally {
            submitButton.disabled = false;
        }
    });

    resetButton.addEventListener("click", async function () {
        resetButton.disabled = true;
        await clearHighlights();
        await Plotly.relayout(graph, {
            "xaxis.autorange": true,
            "yaxis.autorange": true,
            "xaxis2.autorange": true,
            "yaxis2.autorange": true
        });
        setStatus("Pogled je resetiran.");
        resetButton.disabled = false;
    });
}());
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a cached 2D UMAP visualization for a random sample of MMC articles."
    )
    parser.add_argument(
        "--embeddings",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "embeddings.npy",
        help="Path to article embeddings (.npy).",
    )
    parser.add_argument(
        "--metadata",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "metadata.jsonl",
        help="Path to article metadata (.jsonl).",
    )
    parser.add_argument(
        "--output-html",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "umap_visualization.html",
        help="Where to write the interactive Plotly HTML file.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "umap_cache",
        help="Directory used to store cached UMAP projections.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=73363,
        help="Random number of articles to visualize.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for sampling and clustering.",
    )
    parser.add_argument(
        "--umap-neighbors",
        type=int,
        default=30,
        help="UMAP n_neighbors setting.",
    )
    parser.add_argument(
        "--umap-min-dist",
        type=float,
        default=0.08,
        help="UMAP min_dist setting.",
    )
    parser.add_argument(
        "--cluster-count",
        type=int,
        default=16,
        help="Maximum number of clusters to color code.",
    )
    parser.add_argument(
        "--force-recompute",
        action="store_true",
        help="Recompute the cached UMAP projection even if a cache exists.",
    )
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    args = build_parser().parse_args()

    LOGGER.info("Loading embeddings from %s", args.embeddings)
    embeddings = np.load(args.embeddings).astype(np.float32, copy=False)
    LOGGER.info("Embeddings shape: (%d, %d)", embeddings.shape[0], embeddings.shape[1])

    LOGGER.info("Loading metadata from %s", args.metadata)
    metadata = load_metadata(args.metadata)
    if len(metadata) != embeddings.shape[0]:
        raise ValueError(
            f"Metadata size ({len(metadata)}) does not match number of embeddings ({embeddings.shape[0]})."
        )

    unique_topics = {
        str(article.get("category", "")).strip()
        for article in metadata
        if str(article.get("category", "")).strip()
    }
    cluster_count = min(max(len(unique_topics), 8), args.cluster_count)
    LOGGER.info("Using up to %d clusters based on topic diversity", cluster_count)

    projection = load_or_compute_projection(
        embeddings=embeddings,
        embeddings_path=args.embeddings,
        metadata=metadata,
        metadata_path=args.metadata,
        sample_size=args.sample_size,
        seed=args.seed,
        umap_neighbors=args.umap_neighbors,
        umap_min_dist=args.umap_min_dist,
        n_clusters=cluster_count,
        cache_dir=args.cache_dir,
        force_recompute=args.force_recompute,
    )

    plot_rows = build_plot_data(
        metadata=metadata,
        sample_indices=projection["sample_indices"],
        coordinates=projection["coordinates"],
        cluster_labels=projection["cluster_labels"],
    )

    fig = build_figure(plot_rows=plot_rows, total_articles=len(metadata))

    output_html = resolve_output_path(args.output_html, "umap_visualization.html")
    output_html.parent.mkdir(parents=True, exist_ok=True)
    pio.write_html(
        fig,
        file=str(output_html),
        include_plotlyjs="cdn",
        auto_open=False,
        config={"displayModeBar": False},
        post_script=build_faiss_search_script(),
    )
    LOGGER.info("Saved Plotly visualization to %s", output_html)

    print(f"Saved visualization to: {output_html}")
    print(f"UMAP cache used: {projection['cache_path']}")


if __name__ == "__main__":
    main()
