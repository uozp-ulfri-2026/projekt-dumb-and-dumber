from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Any

import numpy as np
import plotly.colors as plotly_colors
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

import umap


LOGGER = logging.getLogger("visualize_umap")
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"
DEFAULT_GEMINI_CACHE_PATH = Path("data") / "mmc_embeddings" / "gemini_global_label_cache.json"


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
    allow_parallelism: bool = False,
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
        str(allow_parallelism),
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
    allow_parallelism: bool = False,
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
        allow_parallelism=allow_parallelism,
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
    reducer_kwargs = {
        "n_components": 2,
        "metric": "cosine",
        "n_neighbors": effective_neighbors,
        "min_dist": umap_min_dist,
    }
    if allow_parallelism:
        LOGGER.info("UMAP parallelism enabled; omitting random_state so n_jobs can use multiple cores.")
        reducer_kwargs["n_jobs"] = -1
    else:
        reducer_kwargs["random_state"] = seed

    reducer = umap.UMAP(**reducer_kwargs)
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
    cluster_names: dict[int, str] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cluster_names = cluster_names or {}
    for sample_row, original_index in enumerate(sample_indices):
        article = metadata[int(original_index)]
        cluster_id = int(cluster_labels[sample_row])
        cluster_name = cluster_names.get(cluster_id, f"Cluster {cluster_id + 1}")
        rows.append(
            {
                "x": float(coordinates[sample_row, 0]),
                "y": float(coordinates[sample_row, 1]),
                "original_index": int(original_index),
                "cluster": cluster_name,
                "topic": str(article.get("category", "") or "Uncategorized"),
                "title": article.get("title", ""),
                "date": article.get("date", ""),
                "url": article.get("url", ""),
                "keywords": ", ".join(article.get("keywords", [])[:8]),
            }
        )
    return rows


def build_cluster_tfidf_labels(
    metadata: list[dict[str, Any]],
    sample_indices: np.ndarray,
    cluster_labels: np.ndarray,
    top_k_words: int = 5,
) -> dict[int, str]:
    cluster_ids = np.unique(cluster_labels)
    grouped_docs: list[str] = []
    sorted_cluster_ids = sorted(int(cluster_id) for cluster_id in cluster_ids)
    dominant_topics: dict[int, str] = {}

    for cluster_id in sorted_cluster_ids:
        text_parts: list[str] = []
        topic_counts: dict[str, int] = {}
        row_indices = np.where(cluster_labels == cluster_id)[0]
        for row_index in row_indices:
            article = metadata[int(sample_indices[int(row_index)])]
            topic = str(article.get("category", "") or "Uncategorized").strip() or "Uncategorized"
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
            article_text = str(article.get("text", "")).strip()
            if not article_text:
                title = str(article.get("title", "")).strip()
                keywords = article.get("keywords", [])
                keywords_text = " ".join(str(keyword) for keyword in keywords if isinstance(keyword, str))
                article_text = " ".join(part for part in [title, keywords_text] if part).strip()
            if article_text:
                text_parts.append(article_text)
        grouped_docs.append("\n".join(text_parts))
        if topic_counts:
            dominant_topic = sorted(topic_counts.items(), key=lambda item: (-item[1], item[0].casefold()))[0][0]
        else:
            dominant_topic = "Uncategorized"
        dominant_topics[cluster_id] = dominant_topic

    if not grouped_docs or not any(doc.strip() for doc in grouped_docs):
        return {
            cluster_id: format_cluster_label(cluster_id, dominant_topics.get(cluster_id, "Uncategorized"), [])
            for cluster_id in sorted_cluster_ids
        }

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_df=0.9,
        min_df=1,
        token_pattern=r"(?u)\b\w\w+\b",
    )

    try:
        tfidf_matrix = vectorizer.fit_transform(grouped_docs)
        feature_names = vectorizer.get_feature_names_out()
    except ValueError:
        return {
            cluster_id: format_cluster_label(cluster_id, dominant_topics.get(cluster_id, "Uncategorized"), [])
            for cluster_id in sorted_cluster_ids
        }

    labels: dict[int, str] = {}
    for row_pos, cluster_id in enumerate(sorted_cluster_ids):
        row = tfidf_matrix.getrow(row_pos)
        topic_label = dominant_topics.get(cluster_id, "Uncategorized")
        if row.nnz == 0:
            labels[cluster_id] = format_cluster_label(cluster_id, topic_label, [])
            continue

        weights = row.toarray().ravel()
        top_indices = np.argsort(weights)[::-1][:top_k_words]
        top_words = [feature_names[index] for index in top_indices if weights[index] > 0]

        if not top_words:
            labels[cluster_id] = format_cluster_label(cluster_id, topic_label, [])
            continue

        labels[cluster_id] = format_cluster_label(cluster_id, topic_label, top_words)

    return labels


def _split_into_sentences(text: str) -> list[str]:
    text = str(text or "").strip()
    if not text:
        return []
    paragraphs = [part.strip() for part in re.split(r"\n{2,}", text) if part.strip()]
    if not paragraphs:
        paragraphs = [text]
    sentences: list[str] = []
    for paragraph in paragraphs:
        paragraph = paragraph.replace("\n", " ").strip()
        if not paragraph:
            continue
        parts = [part.strip() for part in re.split(r"(?<=[.!?])\s+", paragraph) if part.strip()]
        sentences.extend(parts if parts else [paragraph])
    return sentences


def build_cluster_representative_topics(
    metadata: list[dict[str, Any]],
    sample_indices: np.ndarray,
    cluster_labels: np.ndarray,
    top_k_articles: int = 5,
    sentences_per_article: int = 2,
) -> dict[int, dict[str, Any]]:
    cluster_ids = sorted(int(cluster_id) for cluster_id in np.unique(cluster_labels))
    representatives: dict[int, dict[str, Any]] = {}

    for cluster_id in cluster_ids:
        row_indices = np.where(cluster_labels == cluster_id)[0]
        if row_indices.size == 0:
            continue

        articles: list[dict[str, str]] = []
        for row_index in row_indices[:top_k_articles]:
            article = metadata[int(sample_indices[int(row_index)])]
            title = str(article.get("title", "") or "").strip()
            text = str(article.get("text", "") or "").strip()
            keywords = article.get("keywords", [])
            keyword_text = ", ".join(str(keyword) for keyword in keywords if isinstance(keyword, str))

            if text:
                snippet = " ".join(_split_into_sentences(text)[:sentences_per_article])
            elif keyword_text:
                snippet = keyword_text
            else:
                snippet = title

            articles.append({"title": title, "snippet": snippet})

        representatives[cluster_id] = {"articles": articles}

    return representatives


def _normalize_gemini_topic(value: str, max_words: int = 5) -> str:
    value = " ".join(str(value or "").split()).strip()
    if not value:
        return "Neznano"
    return " ".join(value.split()[:max_words])


def _parse_json_from_text(text: str) -> Any | None:
    if not text:
        return None
    try:
        return json.loads(text)
    except Exception:
        match = re.search(r"(\[\s*\{.+\}\s*\])", text, flags=re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except Exception:
                return None
    return None


def _parse_gemini_topics(parsed: Any) -> dict[int, str]:
    topics: dict[int, str] = {}
    if isinstance(parsed, dict) and "predictions" in parsed:
        parsed = parsed["predictions"]
    if not isinstance(parsed, list):
        return topics
    for item in parsed:
        if not isinstance(item, dict):
            continue
        try:
            cluster_id = int(item.get("cluster_id"))
        except Exception:
            continue
        topic = str(item.get("topic") or item.get("label") or "").strip()
        if topic:
            topics[cluster_id] = _normalize_gemini_topic(topic)
    return topics


def _load_json_cache(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as source_file:
            data = json.load(source_file)
        if isinstance(data, dict):
            return data
    except Exception:
        LOGGER.exception("Failed to load Gemini label cache from %s", path)
    return {}


def _save_json_cache(path: Path, cache: dict[str, Any]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as target_file:
            json.dump(cache, target_file, ensure_ascii=False, indent=2)
    except Exception:
        LOGGER.exception("Failed to save Gemini label cache to %s", path)


def build_gemini_cluster_labels(
    metadata: list[dict[str, Any]],
    sample_indices: np.ndarray,
    cluster_labels: np.ndarray,
    model_name: str,
    cache_path: Path,
    enable_gemini: bool,
) -> dict[int, str] | None:
    if not enable_gemini:
        return None

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        LOGGER.warning("Gemini API key is not set; using TF-IDF labels for the global view.")
        return None

    representatives = build_cluster_representative_topics(metadata, sample_indices, cluster_labels)
    if not representatives:
        return None

    cache_key_payload = json.dumps(
        {
            "model": model_name,
            "clusters": representatives,
            "sample_indices": sample_indices.tolist(),
            "cluster_labels": cluster_labels.tolist(),
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    cache_key = hashlib.sha256(cache_key_payload.encode("utf-8")).hexdigest()[:16]
    cache = _load_json_cache(cache_path)
    cached_entry = cache.get(cache_key)
    if isinstance(cached_entry, list):
        cached_topics = _parse_gemini_topics(cached_entry)
        if cached_topics:
            LOGGER.info("Gemini global label cache hit (%s).", cache_key)
            return cached_topics

    payload_blocks: list[str] = []
    for cluster_id, info in representatives.items():
        articles = info.get("articles", [])
        lines = []
        for article in articles:
            title = str(article.get("title", "") or "").strip()
            snippet = str(article.get("snippet", "") or "").strip()
            if title and snippet:
                lines.append(f"- {title}: {snippet}")
            elif title:
                lines.append(f"- {title}")
        payload_blocks.append(f"Skupina {cluster_id}:\n" + "\n".join(lines))

    prompt = (
        "Imas skupine novicarskih clankov o slovenskih aktualnih dogodkih. "
        "Za vsako skupino vrni ENO temo v SLOVENSCINI, dolgo NAJVEC 5 besed. "
        "Ne vracaj stavkov, razlag ali dveh delov. Vrni samo temo. "
        "Vrni IZKLJUCNO JSON polje objektov s kljuci: cluster_id (integer), topic (string). "
        "Brez dodatnega besedila. Primeri skupin so spodaj.\n\n"
        + "\n\n".join(payload_blocks)
        + "\n\nVrni JSON kot: [{\"cluster_id\": 0, \"topic\": \"vpis v srednje sole\"}, ...]"
    )

    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config={"temperature": 0.2, "response_mime_type": "application/json"},
        )
        parsed = _parse_json_from_text((getattr(response, "text", "") or "").strip())
        topics = _parse_gemini_topics(parsed)
        if not topics:
            LOGGER.warning("Gemini returned unparsable global labels; using TF-IDF labels.")
            return None

        cache[cache_key] = [
            {"cluster_id": int(cluster_id), "topic": topic}
            for cluster_id, topic in sorted(topics.items(), key=lambda item: item[0])
        ]
        _save_json_cache(cache_path, cache)
        return topics
    except Exception as exc:
        message = str(exc)
        if "RESOURCE_EXHAUSTED" in message or "quota" in message.lower() or "429" in message:
            LOGGER.warning("Gemini quota exhausted for the global view; using TF-IDF labels.")
        else:
            LOGGER.exception("Gemini global label request failed")
        return None


def format_cluster_label(
    cluster_id: int,
    topic_label: str,
    top_words: list[str],
    max_length: int = 48,
) -> str:
    topic_label = " ".join(str(topic_label).split()) or "Uncategorized"
    word_part = ", ".join(top_words[:3])
    base = f"C{cluster_id + 1:02d} | {topic_label}"
    if word_part:
        base = f"{base} | {word_part}"

    if len(base) <= max_length:
        return base

    shortened_topic = topic_label
    if len(shortened_topic) > 24:
        shortened_topic = shortened_topic[:21].rstrip() + "..."

    base = f"C{cluster_id + 1:02d} | {shortened_topic}"
    if word_part:
        base = f"{base} | {word_part}"
    if len(base) <= max_length:
        return base

    return base[: max(0, max_length - 3)].rstrip() + "..."


def _color_for_index(index: int) -> str:
    palette = plotly_colors.qualitative.Set3
    return palette[index % len(palette)]


def _natural_sort_key(value: str) -> tuple[tuple[int, int | str], ...]:
    return tuple(
        (0, int(part)) if part.isdigit() else (1, part.casefold())
        for part in re.split(r"(\d+)", value)
    )


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
    sorted_groups = sorted(grouped.items(), key=lambda item: _natural_sort_key(item[0]))
    legend_group_title = "Clusters" if axis_name == "cluster" else "Topics"
    for index, (group_name, group_rows) in enumerate(sorted_groups):
        legend_options: dict[str, Any] = {"legendgrouptitle": {"text": legend_group_title}} if index == 0 else {}
        traces.append(
            go.Scattergl(
                x=[row["x"] for row in group_rows],
                y=[row["y"] for row in group_rows],
                mode="markers",
                name=group_name,
                legendgroup=axis_name,
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
                **legend_options,
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

    for trace in _group_traces(plot_rows, group_key="topic", axis_name="topic", show_legend=True):
        fig.add_trace(trace, row=1, col=2)

    fig.update_layout(
        template="plotly_white",
        width=1800,
        height=900,
        title={"text": f"MMC articles UMAP ({len(plot_rows)} sampled from {total_articles})", "x": 0.5},
        legend={"groupclick": "toggleitem", "tracegroupgap": 10},
        legend_title_text="",
        dragmode="zoom",
    )
    fig.update_xaxes(title_text="UMAP 1")
    fig.update_yaxes(title_text="UMAP 2")
    fig.update_xaxes(matches="x", row=1, col=2)
    fig.update_yaxes(matches="y", row=1, col=2)
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
            grid-template-columns: minmax(220px, 1fr) auto auto auto auto auto;
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
        .faiss-reranker-toggle,
        .faiss-reset-button,
        .faiss-local-reset-button,
        .faiss-clear-button {
            height: 38px;
            padding: 0 13px;
            border: 1px solid #1d4ed8;
            border-radius: 6px;
            background: #2563eb;
            color: #ffffff;
            font-size: 14px;
            cursor: pointer;
        }
        .faiss-reranker-toggle {
            border-color: #15803d;
            background: #16a34a;
        }
        .faiss-reranker-toggle[aria-pressed="false"] {
            border-color: #c9d1db;
            background: #ffffff;
            color: #1f2937;
        }
        .faiss-reset-button,
        .faiss-local-reset-button,
        .faiss-clear-button {
            border-color: #c9d1db;
            background: #ffffff;
            color: #1f2937;
        }
        .faiss-search-button:disabled,
        .faiss-reranker-toggle:disabled,
        .faiss-reset-button:disabled,
        .faiss-local-reset-button:disabled,
        .faiss-clear-button:disabled {
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
        .faiss-results {
            margin: 8px 0 0;
            padding-left: 22px;
        }
        .faiss-results li {
            margin: 3px 0;
        }
        .faiss-result-missing {
            color: #6b7280;
        }
        .faiss-result-snippets {
            margin: 6px 0 0;
            padding-left: 18px;
            color: #374151;
        }
        .faiss-result-snippets li {
            margin: 3px 0;
            line-height: 1.35;
        }
        .faiss-result-snippet-score {
            color: #6b7280;
            font-size: 12px;
        }
        .faiss-local-map-panel {
            box-sizing: border-box;
            width: min(900px, calc(100vw - 32px));
            margin: 8px auto 24px;
            padding: 10px 0 0;
            font-family: Arial, sans-serif;
            color: #1f2937;
            display: none;
        }
        .faiss-local-map-title {
            margin: 0 0 8px;
            font-size: 16px;
            font-weight: 700;
        }
        .faiss-local-map-graph {
            width: 100%;
            height: 520px;
            border: 1px solid #d8dee9;
            border-radius: 8px;
            background: #ffffff;
        }
        @media (max-width: 720px) {
            .faiss-search-form {
                grid-template-columns: 1fr;
            }
            .faiss-local-map-graph {
                height: 460px;
            }
        }
    `;
    document.head.appendChild(style);

    const defaultStatus = "Search uses FAISS candidates followed by cross-encoder reranking. Start with: python src/serveUmapSearch.py";
    const panel = document.createElement("section");
    panel.className = "faiss-search-panel";
    panel.innerHTML = `
        <form class="faiss-search-form">
            <input class="faiss-search-input" name="query" type="search" placeholder="FAISS + reranker search top 5..." autocomplete="off" />
            <button class="faiss-search-button" type="submit">Search</button>
            <button class="faiss-reranker-toggle" type="button" aria-pressed="true">Reranker: on</button>
            <button class="faiss-reset-button" type="button">Reset global view</button>
            <button class="faiss-local-reset-button" type="button">Reset local view</button>
            <button class="faiss-clear-button" type="button">Reset</button>
        </form>
        <div class="faiss-search-status">${defaultStatus}</div>
    `;
    graph.parentNode.insertBefore(panel, graph);
    const localPanel = document.createElement("section");
    localPanel.className = "faiss-local-map-panel";
    localPanel.innerHTML = `
        <div class="faiss-local-map-title">Local map</div>
        <div class="faiss-local-map-graph"></div>
    `;
    graph.parentNode.insertBefore(localPanel, graph.nextSibling);

    const form = panel.querySelector("form");
    const input = panel.querySelector(".faiss-search-input");
    const submitButton = panel.querySelector(".faiss-search-button");
    const rerankerToggle = panel.querySelector(".faiss-reranker-toggle");
    const resetButton = panel.querySelector(".faiss-reset-button");
    const localResetButton = panel.querySelector(".faiss-local-reset-button");
    const clearButton = panel.querySelector(".faiss-clear-button");
    const status = panel.querySelector(".faiss-search-status");
    const localTitle = localPanel.querySelector(".faiss-local-map-title");
    const localGraph = localPanel.querySelector(".faiss-local-map-graph");
    let useReranker = true;

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
                    cluster: custom[1],
                    topic: custom[2],
                    date: custom[3],
                    keywords: custom[4],
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
            return Plotly.deleteTraces(graph, indices.reverse()).then(clearHighlightAnnotations);
        }
        return clearHighlightAnnotations();
    }

    function clearHighlightAnnotations() {
        const annotations = (graph.layout.annotations || []).filter(function (annotation) {
            return annotation.name !== "faissHighlight";
        });
        return Plotly.relayout(graph, {annotations: annotations});
    }

    function axisLayoutName(axisRef) {
        return axisRef === "x" || axisRef === "y" ? axisRef + "axis" : axisRef.replace(/^([xy])/, "$1axis");
    }

    function pairedAxisName(axisName) {
        return {
            xaxis: "xaxis2",
            xaxis2: "xaxis",
            yaxis: "yaxis2",
            yaxis2: "yaxis"
        }[axisName] || "";
    }

    function axisRangeFromEvent(eventData, axisName) {
        if (Array.isArray(eventData[axisName + ".range"])) {
            return eventData[axisName + ".range"];
        }
        const start = eventData[axisName + ".range[0]"];
        const end = eventData[axisName + ".range[1]"];
        if (start !== undefined && end !== undefined) {
            return [start, end];
        }
        return null;
    }

    function buildSyncedRelayout(eventData) {
        const relayout = {};
        for (const axisName of ["xaxis", "xaxis2", "yaxis", "yaxis2"]) {
            const pairedAxis = pairedAxisName(axisName);
            const range = axisRangeFromEvent(eventData, axisName);
            if (pairedAxis && range) {
                relayout[pairedAxis + ".range"] = range;
            }
            if (pairedAxis && eventData[axisName + ".autorange"] !== undefined) {
                relayout[pairedAxis + ".autorange"] = eventData[axisName + ".autorange"];
            }
        }
        return relayout;
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

    function formatScore(score) {
        return Number.isFinite(Number(score)) ? Number(score).toFixed(4) : "";
    }

    function highlightColor(rank) {
        const colors = ["#ef4444", "#f97316", "#eab308", "#22c55e", "#06b6d4"];
        const index = Math.max(0, Math.min(colors.length - 1, Number(rank || 1) - 1));
        return colors[index];
    }

    function highlightAnnotation(match) {
        const isFirst = Number(match.rank) === 1;
        return {
            name: "faissHighlight",
            x: match.x,
            y: match.y,
            xref: match.xaxis || "x",
            yref: match.yaxis || "y",
            text: isFirst ? "★" : "■",
            showarrow: false,
            xanchor: "center",
            yanchor: "middle",
            align: "center",
            font: {
                size: isFirst ? 52 : 38,
                color: highlightColor(match.rank),
                family: "Arial Black, Arial, sans-serif"
            },
            opacity: 1
        };
    }

    async function highlight(matches) {
        await clearHighlights();
        const orderedMatches = matches.slice().sort(function (left, right) {
            return Number(right.rank || 0) - Number(left.rank || 0);
        });
        const traces = orderedMatches.map(function (match) {
            return {
                type: "scatter",
                x: [match.x],
                y: [match.y],
                xaxis: match.xaxis,
                yaxis: match.yaxis,
                mode: "markers",
                name: (match.useReranker ? "Reranked top " : "FAISS top ") + match.rank,
                showlegend: false,
                hovertemplate: (
                    "<b>%{customdata[0]}</b><br>"
                    + "Final rank: %{customdata[6]}<br>"
                    + "Cluster: %{customdata[1]}<br>"
                    + "Topic: %{customdata[2]}<br>"
                    + "Date: %{customdata[3]}<br>"
                    + "Keywords: %{customdata[4]}<br>"
                    + "FAISS score: %{customdata[5]}<br>"
                    + "Reranker score: %{customdata[7]}<br>"
                    + "<extra></extra>"
                ),
                customdata: [[
                    match.title,
                    match.cluster,
                    match.topic,
                    match.date,
                    match.keywords,
                    formatScore(match.score),
                    match.rank,
                    formatScore(match.rerankerScore)
                ]],
                marker: {
                    symbol: Number(match.rank) === 1 ? "star" : "square",
                    size: Number(match.rank) === 1 ? 48 : 40,
                    color: highlightColor(match.rank),
                    opacity: 0.01,
                    line: {color: "#111827", width: 0}
                },
                meta: {faissHighlight: true}
            };
        });
        if (traces.length > 0) {
            await Plotly.addTraces(graph, traces);
        }
        await focusMatches(matches);
        const baseAnnotations = (graph.layout.annotations || []).filter(function (annotation) {
            return annotation.name !== "faissHighlight";
        });
        await Plotly.relayout(graph, {
            annotations: baseAnnotations.concat(orderedMatches.map(highlightAnnotation))
        });
    }

    function resultHtml(result, inSample, useReranker) {
        const title = escapeHtml(result.title || "Brez naslova");
        const score = formatScore(result.score);
        const rerankerScore = useReranker ? formatScore(result.reranker_score) : "";
        const faissRank = result.faiss_rank ? String(result.faiss_rank) : "";
        const url = result.url ? String(result.url) : "";
        const link = url ? `<a href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${title}</a>` : title;
        const scoreParts = [];
        if (rerankerScore) {
            scoreParts.push(`reranker: <strong>${escapeHtml(rerankerScore)}</strong>`);
        }
        if (score) {
            scoreParts.push(`FAISS: <strong>${escapeHtml(score)}</strong>`);
        }
        if (faissRank) {
            scoreParts.push(`FAISS rank: <strong>${escapeHtml(faissRank)}</strong>`);
        }
        const scoreHtml = scoreParts.length > 0 ? ` <span>${scoreParts.join(" | ")}</span>` : "";
        const missingHtml = inSample ? "" : ` <span class="faiss-result-missing">(ni v trenutnem UMAP vzorcu)</span>`;
        const snippets = Array.isArray(result.top_sentences) ? result.top_sentences : [];
        const snippetHtml = snippets.length > 0
            ? `<ol class="faiss-result-snippets">${snippets.map(function (sentence) {
                const sentenceText = escapeHtml(sentence.sentence || "");
                const sentenceScore = formatScore(sentence.score);
                const sentenceScoreHtml = sentenceScore ? ` <span class="faiss-result-snippet-score">(${escapeHtml(sentenceScore)})</span>` : "";
                return `<li><strong>${sentenceText}</strong>${sentenceScoreHtml}</li>`;
            }).join("")}</ol>`
            : "";
        return `${link}${scoreHtml}${missingHtml}${snippetHtml}`;
    }

    function resultsHtml(results, pointLookup, useReranker) {
        const items = results.map(function (result) {
            const inSample = (pointLookup.get(String(result.article_index)) || []).length > 0;
            return `<li>${resultHtml(result, inSample, useReranker)}</li>`;
        });
        const heading = useReranker ? "Top 5 after reranking:" : "Top 5 by FAISS:";
        return `${heading}<ol class="faiss-results">${items.join("")}</ol>`;
    }

    function clearLocalMap() {
        localPanel.style.display = "none";
        if (localGraph && localGraph.data) {
            Plotly.purge(localGraph);
        }
    }

    function renderLocalMap(localMap, useReranker) {
        if (!localMap || !Array.isArray(localMap.points) || localMap.points.length === 0) {
            clearLocalMap();
            return;
        }

        const grouped = new Map();
        for (const point of localMap.points) {
            const cluster = String(point.cluster || "Local cluster");
            if (!grouped.has(cluster)) {
                grouped.set(cluster, []);
            }
            grouped.get(cluster).push(point);
        }

        const traces = [];
        const sortedGroups = Array.from(grouped.entries()).sort(function (left, right) {
            return left[0].localeCompare(right[0], undefined, {numeric: true});
        });
        for (let groupIndex = 0; groupIndex < sortedGroups.length; groupIndex += 1) {
            const groupName = sortedGroups[groupIndex][0];
            const points = sortedGroups[groupIndex][1];
            traces.push({
                type: "scattergl",
                mode: "markers",
                name: groupName,
                x: points.map(function (point) { return point.x; }),
                y: points.map(function (point) { return point.y; }),
                customdata: points.map(function (point) {
                    return [
                        point.title || "Brez naslova",
                        point.category || "",
                        point.date || "",
                        point.url || "",
                        point.faiss_rank,
                        formatScore(point.score)
                    ];
                }),
                hovertemplate: (
                    "<b>%{customdata[0]}</b><br>"
                    + "Topic: %{customdata[1]}<br>"
                    + "Date: %{customdata[2]}<br>"
                    + "FAISS rank: %{customdata[4]}<br>"
                    + "FAISS score: %{customdata[5]}<br>"
                    + "<extra></extra>"
                ),
                marker: {
                    color: highlightColor(groupIndex + 1),
                    size: 6,
                    opacity: 0.62,
                    line: {width: 0}
                }
            });
        }

        const resultPoints = localMap.points
            .filter(function (point) {
                return point.result_rank !== null
                    && point.result_rank !== undefined
                    && Number.isFinite(Number(point.result_rank));
            })
            .sort(function (left, right) { return Number(left.result_rank) - Number(right.result_rank); });
        if (resultPoints.length > 0) {
            traces.push({
                type: "scatter",
                mode: "markers",
                name: useReranker ? "Reranked top 5" : "FAISS top 5",
                x: resultPoints.map(function (point) { return point.x; }),
                y: resultPoints.map(function (point) { return point.y; }),
                customdata: resultPoints.map(function (point) {
                    return [
                        point.title || "Brez naslova",
                        point.category || "",
                        point.date || "",
                        point.url || "",
                        point.faiss_rank,
                        formatScore(point.score),
                        point.result_rank
                    ];
                }),
                hovertemplate: (
                    "<b>%{customdata[0]}</b><br>"
                    + "Final rank: %{customdata[6]}<br>"
                    + "Topic: %{customdata[1]}<br>"
                    + "Date: %{customdata[2]}<br>"
                    + "FAISS rank: %{customdata[4]}<br>"
                    + "FAISS score: %{customdata[5]}<br>"
                    + "<extra></extra>"
                ),
                marker: {
                    symbol: resultPoints.map(function (point) {
                        return Number(point.result_rank) === 1 ? "star" : "square";
                    }),
                    size: resultPoints.map(function (point) {
                        return Number(point.result_rank) === 1 ? 18 : 16;
                    }),
                    color: resultPoints.map(function (point) { return highlightColor(point.result_rank); }),
                    line: {color: "#111827", width: 1}
                }
            });
        }

        localTitle.textContent = `Local map: top ${localMap.size} FAISS candidates (${String(localMap.projection || "projection").toUpperCase()})`;
        localPanel.style.display = "block";
        if (localGraph.data) {
            Plotly.purge(localGraph);
        }
        Plotly.newPlot(
            localGraph,
            traces,
            {
                template: "plotly_white",
                height: 520,
                margin: {l: 42, r: 18, t: 24, b: 42},
                xaxis: {title: "Local 1", zeroline: false},
                yaxis: {title: "Local 2", zeroline: false},
                legend: {orientation: "h"}
            },
            {displayModeBar: false, responsive: true}
        );
        localGraph.on("plotly_click", function (eventData) {
            const point = eventData.points && eventData.points[0];
            const custom = point && point.customdata;
            if (!Array.isArray(custom) || !custom[3]) {
                return;
            }
            const articleWindow = window.open(String(custom[3]), "_blank", "noopener,noreferrer");
            if (articleWindow) {
                articleWindow.opener = null;
            }
        });
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

    let syncingAxes = false;
    graph.on("plotly_relayout", async function (eventData) {
        if (syncingAxes) {
            return;
        }
        const relayout = buildSyncedRelayout(eventData || {});
        if (Object.keys(relayout).length === 0) {
            return;
        }
        syncingAxes = true;
        try {
            await Plotly.relayout(graph, relayout);
        } finally {
            syncingAxes = false;
        }
    });

    rerankerToggle.addEventListener("click", function () {
        useReranker = !useReranker;
        rerankerToggle.setAttribute("aria-pressed", useReranker ? "true" : "false");
        rerankerToggle.textContent = useReranker ? "Reranker: on" : "Reranker: off";
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        const query = input.value.trim();
        if (!query) {
            input.focus();
            return;
        }

        submitButton.disabled = true;
        const searchMode = useReranker ? "Searching FAISS candidates and reranking..." : "Searching FAISS top 5...";
        setStatus(searchMode);
        try {
            const response = await fetch(
                "/api/search?query=" + encodeURIComponent(query) + "&reranker=" + (useReranker ? "1" : "0"),
                {
                headers: {"Accept": "application/json"}
                }
            );
            if (!response.ok) {
                throw new Error("HTTP " + response.status);
            }
            const payload = await response.json();
            const responseUsedReranker = payload.use_reranker !== false;
            const results = payload.results || (payload.result ? [payload.result] : []);
            if (results.length === 0) {
                await clearHighlights();
                clearLocalMap();
                setStatus("Ni zadetka.");
                return;
            }

            const pointLookup = buildPointLookup();
            const scoredMatches = [];
            for (const result of results) {
                const matches = pointLookup.get(String(result.article_index)) || [];
                for (const match of matches) {
                    scoredMatches.push(Object.assign({}, match, {
                        rank: result.rank,
                        score: result.score,
                        rerankerScore: result.reranker_score,
                        useReranker: responseUsedReranker
                    }));
                }
            }

            if (scoredMatches.length > 0) {
                await highlight(scoredMatches);
            } else {
                await clearHighlights();
            }
            renderLocalMap(payload.local_map, responseUsedReranker);
            setStatus(resultsHtml(results, pointLookup, responseUsedReranker), true);
        } catch (error) {
            setStatus("Search endpoint is not reachable. Start: python src/serveUmapSearch.py");
        } finally {
            submitButton.disabled = false;
        }
    });

    resetButton.addEventListener("click", async function () {
        resetButton.disabled = true;
        await Plotly.relayout(graph, {
            "xaxis.autorange": true,
            "yaxis.autorange": true,
            "xaxis2.autorange": true,
            "yaxis2.autorange": true
        });
        resetButton.disabled = false;
    });

    localResetButton.addEventListener("click", async function () {
        localResetButton.disabled = true;
        if (localPanel.style.display !== "none" && localGraph.data) {
            await Plotly.relayout(localGraph, {
                "xaxis.autorange": true,
                "yaxis.autorange": true
            });
        }
        localResetButton.disabled = false;
    });

    clearButton.addEventListener("click", async function () {
        clearButton.disabled = true;
        await clearHighlights();
        await Plotly.relayout(graph, {
            "xaxis.autorange": true,
            "yaxis.autorange": true,
            "xaxis2.autorange": true,
            "yaxis2.autorange": true
        });
        input.value = "";
        setStatus(defaultStatus);
        clearLocalMap();
        clearButton.disabled = false;
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
        default=25,
        help="Maximum number of clusters to color code.",
    )
    parser.add_argument(
        "--allow-parallelism",
        action="store_true",
        help="Allow UMAP to use multiple cores for faster projection (non-deterministic).",
    )
    parser.add_argument(
        "--disable-global-labeling",
        action="store_true",
        help="Disable Gemini-based automatic labeling for the global view and use TF-IDF labels only.",
    )
    parser.add_argument(
        "--gemini-model",
        type=str,
        default=DEFAULT_GEMINI_MODEL,
        help="Gemini model name for global labeling (default: gemini-2.5-flash).",
    )
    parser.add_argument(
        "--gemini-cache-path",
        type=Path,
        default=DEFAULT_GEMINI_CACHE_PATH,
        help="Path to the persistent JSON cache file for global Gemini labels.",
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

    cluster_count = args.cluster_count
    LOGGER.info("Using up to %d clusters for KMeans coloring", cluster_count)

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
        allow_parallelism=bool(args.allow_parallelism),
    )

    cluster_name_map = build_gemini_cluster_labels(
        metadata=metadata,
        sample_indices=projection["sample_indices"],
        cluster_labels=projection["cluster_labels"],
        model_name=args.gemini_model,
        cache_path=args.gemini_cache_path,
        enable_gemini=not args.disable_global_labeling,
    )
    if not cluster_name_map:
        cluster_name_map = build_cluster_tfidf_labels(
            metadata=metadata,
            sample_indices=projection["sample_indices"],
            cluster_labels=projection["cluster_labels"],
            top_k_words=5,
        )
        LOGGER.info("Using TF-IDF labels for the global view.")
    else:
        LOGGER.info("Using Gemini labels for the global view.")

    plot_rows = build_plot_data(
        metadata=metadata,
        sample_indices=projection["sample_indices"],
        coordinates=projection["coordinates"],
        cluster_labels=projection["cluster_labels"],
        cluster_names=cluster_name_map,
    )

    fig = build_figure(plot_rows=plot_rows, total_articles=len(metadata))

    output_html = resolve_output_path(args.output_html, "umap_visualization.html")
    output_html.parent.mkdir(parents=True, exist_ok=True)
    pio.write_html(
        fig,
        file=str(output_html),
        include_plotlyjs="cdn",
        auto_open=False,
        config={"displayModeBar": False, "doubleClick": False, "scrollZoom": False, "showTips": False},
        post_script=build_faiss_search_script(),
    )
    LOGGER.info("Saved Plotly visualization to %s", output_html)

    print(f"Saved visualization to: {output_html}")
    print(f"UMAP cache used: {projection['cache_path']}")


if __name__ == "__main__":
    main()
