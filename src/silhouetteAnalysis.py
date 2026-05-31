from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score


LOGGER = logging.getLogger("silhouette_analysis")


def load_embeddings(embeddings_path: Path) -> np.ndarray:
    """Load embeddings from .npy file."""
    LOGGER.info("Loading embeddings from %s", embeddings_path)
    embeddings = np.load(embeddings_path).astype(np.float32, copy=False)
    LOGGER.info("Loaded embeddings shape: (%d, %d)", embeddings.shape[0], embeddings.shape[1])
    return embeddings


def load_metadata(metadata_path: Path) -> list[dict[str, Any]]:
    """Load metadata from JSONL file."""
    LOGGER.info("Loading metadata from %s", metadata_path)
    metadata: list[dict[str, Any]] = []
    with metadata_path.open("r", encoding="utf-8") as source_file:
        for line in source_file:
            line = line.strip()
            if not line:
                continue
            metadata.append(json.loads(line))
    LOGGER.info("Loaded %d metadata records", len(metadata))
    return metadata


def extract_topic_labels(metadata: list[dict[str, Any]]) -> tuple[np.ndarray, list[str]]:
    """Extract category/topic labels from metadata."""
    topics = [str(record.get("category", "Uncategorized")) for record in metadata]
    
    # Create numeric labels for topics
    unique_topics = sorted(set(topics))
    topic_to_label = {topic: idx for idx, topic in enumerate(unique_topics)}
    labels = np.array([topic_to_label[topic] for topic in topics], dtype=np.int32)
    
    LOGGER.info("Found %d unique topics: %s", len(unique_topics), unique_topics[:10])
    return labels, unique_topics


def compute_kmeans_clusters(
    embeddings: np.ndarray,
    n_clusters: int,
    seed: int,
) -> tuple[np.ndarray, KMeans]:
    """Compute KMeans clusters."""
    LOGGER.info("Computing KMeans clusters (%d clusters, seed=%d)", n_clusters, seed)
    kmeans = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10, verbose=0)
    labels = kmeans.fit_predict(embeddings)
    LOGGER.info("KMeans completed")
    return labels, kmeans


def run_kmeans_sweep(
    embeddings: np.ndarray,
    cluster_counts: list[int],
    seed: int,
    metric: str,
) -> list[dict[str, Any]]:
    sweep_results: list[dict[str, Any]] = []

    for n_clusters in cluster_counts:
        LOGGER.info("Running KMeans silhouette sweep for %d clusters", n_clusters)
        labels, _ = compute_kmeans_clusters(embeddings, n_clusters=n_clusters, seed=seed)
        overall_score, sample_scores = compute_silhouette_metrics(embeddings, labels, metric=metric)
        cluster_stats = compute_cluster_statistics(labels, sample_scores)
        sweep_results.append(
            {
                "n_clusters": int(n_clusters),
                "overall_score": float(overall_score),
                "per_cluster": cluster_stats,
            }
        )

    return sweep_results


def compute_silhouette_metrics(
    embeddings: np.ndarray,
    labels: np.ndarray,
    metric: str = "cosine",
) -> tuple[float, np.ndarray]:
    """Compute overall and per-sample silhouette scores."""
    LOGGER.info("Computing silhouette scores (metric=%s)", metric)
    overall_score = float(
        silhouette_score(embeddings, labels, metric=metric, sample_size=min(80000, len(embeddings)))
    )
    sample_scores = np.asarray(silhouette_samples(embeddings, labels, metric=metric), dtype=np.float32)
    LOGGER.info("Overall silhouette score: %.4f", overall_score)
    return overall_score, sample_scores


def compute_cluster_statistics(
    labels: np.ndarray,
    sample_scores: np.ndarray,
    label_names: list[str] | None = None,
) -> dict[str, Any]:
    """Compute per-cluster/topic silhouette statistics."""
    unique_labels = np.unique(labels)
    stats: dict[str, Any] = {}
    
    for label in unique_labels:
        mask = labels == label
        cluster_scores = sample_scores[mask]
        
        label_name = f"{label_names[label]}" if label_names else f"Cluster {label}"
        stats[label_name] = {
            "count": int(np.sum(mask)),
            "mean_silhouette": float(np.mean(cluster_scores)),
            "median_silhouette": float(np.median(cluster_scores)),
            "std_silhouette": float(np.std(cluster_scores)),
            "min_silhouette": float(np.min(cluster_scores)),
            "max_silhouette": float(np.max(cluster_scores)),
            "negative_samples": int(np.sum(cluster_scores < 0)),
        }
    
    return stats


def format_statistics(
    overall_score: float,
    stats: dict[str, Any],
    title: str,
) -> str:
    """Format statistics for printing."""
    lines = [
        f"\n{'=' * 80}",
        f"  {title}",
        f"{'=' * 80}",
        f"Overall Silhouette Score: {overall_score:.4f}",
        f"",
    ]
    
    sorted_stats = sorted(
        stats.items(),
        key=lambda x: x[1]["mean_silhouette"],
        reverse=True,
    )
    
    lines.append("Per-Cluster Statistics (sorted by mean silhouette score):")
    lines.append(f"{'Label':<40} {'Count':<8} {'Mean':<8} {'Median':<8} {'Std':<8} {'Negative':<10}")
    lines.append("-" * 80)
    
    for label_name, stat in sorted_stats:
        lines.append(
            f"{label_name:<40} {stat['count']:<8} "
            f"{stat['mean_silhouette']:<8.4f} {stat['median_silhouette']:<8.4f} "
            f"{stat['std_silhouette']:<8.4f} {stat['negative_samples']:<10}"
        )
    
    return "\n".join(lines)


def build_silhouette_bar_chart(
    stats: dict[str, Any],
    title: str,
) -> go.Figure:
    """Build a bar chart showing silhouette scores per cluster/topic."""
    sorted_items = sorted(stats.items(), key=lambda x: x[1]["mean_silhouette"], reverse=True)
    
    labels = [item[0] for item in sorted_items]
    means = [item[1]["mean_silhouette"] for item in sorted_items]
    counts = [item[1]["count"] for item in sorted_items]
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Bar(
            x=labels,
            y=means,
            text=[f"n={c}" for c in counts],
            textposition="outside",
            marker=dict(
                color=means,
                colorscale="RdYlGn",
                cmin=-1,
                cmax=1,
                colorbar=dict(title="Silhouette Score"),
            ),
        )
    )
    
    fig.update_layout(
        title=title,
        xaxis_title="Cluster/Topic",
        yaxis_title="Mean Silhouette Score",
        height=600,
        template="plotly_white",
        xaxis_tickangle=-45,
    )
    
    return fig


def build_silhouette_comparison_figure(
    kmeans_stats: dict[str, Any],
    topic_stats: dict[str, Any],
    kmeans_overall: float,
    topic_overall: float,
) -> go.Figure:
    """Build a side-by-side comparison figure."""
    kmeans_sorted = sorted(kmeans_stats.items(), key=lambda x: x[1]["mean_silhouette"], reverse=True)
    topic_sorted = sorted(topic_stats.items(), key=lambda x: x[1]["mean_silhouette"], reverse=True)
    
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            f"KMeans Clustering (Overall: {kmeans_overall:.4f})",
            f"Article Topics (Overall: {topic_overall:.4f})",
        ),
        specs=[[{"type": "bar"}, {"type": "bar"}]],
    )
    
    # KMeans subplot
    kmeans_labels = [item[0] for item in kmeans_sorted]
    kmeans_means = [item[1]["mean_silhouette"] for item in kmeans_sorted]
    kmeans_counts = [item[1]["count"] for item in kmeans_sorted]
    
    fig.add_trace(
        go.Bar(
            x=kmeans_labels,
            y=kmeans_means,
            text=[f"n={c}" for c in kmeans_counts],
            textposition="outside",
            marker=dict(
                color=kmeans_means,
                colorscale="RdYlGn",
                cmin=-1,
                cmax=1,
            ),
            name="KMeans",
            showlegend=False,
        ),
        row=1,
        col=1,
    )
    
    # Topics subplot
    topic_labels = [item[0][:20] + "..." if len(item[0]) > 20 else item[0] for item in topic_sorted]
    topic_means = [item[1]["mean_silhouette"] for item in topic_sorted]
    topic_counts = [item[1]["count"] for item in topic_sorted]
    
    fig.add_trace(
        go.Bar(
            x=topic_labels,
            y=topic_means,
            text=[f"n={c}" for c in topic_counts],
            textposition="outside",
            marker=dict(
                color=topic_means,
                colorscale="RdYlGn",
                cmin=-1,
                cmax=1,
            ),
            name="Topics",
            showlegend=False,
        ),
        row=1,
        col=2,
    )
    
    fig.update_xaxes(tickangle=-45, row=1, col=1)
    fig.update_xaxes(tickangle=-45, row=1, col=2)
    fig.update_yaxes(title_text="Mean Silhouette Score", row=1, col=1)
    fig.update_yaxes(title_text="Mean Silhouette Score", row=1, col=2)
    
    fig.update_layout(
        title_text="Silhouette Analysis: KMeans Clusters vs Article Topics",
        height=700,
        width=1400,
        template="plotly_white",
    )
    
    return fig


def build_kmeans_sweep_figure(sweep_results: list[dict[str, Any]]) -> go.Figure:
    cluster_counts = [result["n_clusters"] for result in sweep_results]
    scores = [result["overall_score"] for result in sweep_results]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=cluster_counts,
            y=scores,
            mode="lines+markers",
            marker={"size": 9},
            line={"width": 3},
            name="KMeans silhouette",
        )
    )

    fig.update_layout(
        title="KMeans Silhouette Sweep",
        xaxis_title="Number of clusters",
        yaxis_title="Overall silhouette score",
        height=600,
        template="plotly_white",
    )
    return fig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Silhouette analysis for a KMeans cluster sweep."
    )
    parser.add_argument(
        "--embeddings",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "embeddings.npy",
        help="Path to embeddings .npy file.",
    )
    parser.add_argument(
        "--metadata",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "metadata.jsonl",
        help="Path to metadata JSONL file.",
    )
    parser.add_argument(
        "--start-clusters",
        type=int,
        default=5,
        help="Starting number of KMeans clusters for the sweep.",
    )
    parser.add_argument(
        "--end-clusters",
        type=int,
        default=20,
        help="Ending number of KMeans clusters for the sweep.",
    )
    parser.add_argument(
        "--step",
        type=int,
        default=1,
        help="Step between cluster counts in the sweep.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility.",
    )
    parser.add_argument(
        "--metric",
        type=str,
        choices=["cosine", "euclidean"],
        default="cosine",
        help="Distance metric for silhouette computation.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data") / "silhouette_analysis",
        help="Directory to save analysis outputs.",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Skip generating Plotly visualizations.",
    )
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    
    args = build_parser().parse_args()
    
    # Load data
    embeddings = load_embeddings(args.embeddings)
    metadata = load_metadata(args.metadata)
    
    if len(embeddings) != len(metadata):
        raise ValueError(
            f"Embeddings shape[0] ({len(embeddings)}) != metadata records ({len(metadata)})"
        )

    if args.step <= 0:
        raise ValueError("--step must be greater than 0.")
    if args.start_clusters < 2:
        raise ValueError("--start-clusters must be at least 2.")
    if args.end_clusters < args.start_clusters:
        raise ValueError("--end-clusters must be greater than or equal to --start-clusters.")

    cluster_counts = [
        n_clusters
        for n_clusters in range(args.start_clusters, args.end_clusters + 1, args.step)
        if n_clusters < len(embeddings)
    ]
    if not cluster_counts:
        raise ValueError("No valid cluster counts remain after applying the requested range.")

    sweep_results = run_kmeans_sweep(
        embeddings=embeddings,
        cluster_counts=cluster_counts,
        seed=args.seed,
        metric=args.metric,
    )

    print(f"\n{'=' * 80}")
    print("  KMeans Silhouette Sweep")
    print(f"{'=' * 80}")
    print(f"Range: {args.start_clusters}..{args.end_clusters} step {args.step}")
    print(f"Metric: {args.metric}")
    print(f"Seed:   {args.seed}")
    print()

    print(f"{'Clusters':<10} {'Overall':<10}")
    print("-" * 22)
    for result in sweep_results:
        print(f"{result['n_clusters']:<10} {result['overall_score']:<10.4f}")

    best_run = max(sweep_results, key=lambda item: item["overall_score"])
    print()
    print(f"Best cluster count: {best_run['n_clusters']} (silhouette {best_run['overall_score']:.4f})")
    print()
    
    # Save outputs
    if not args.no_plots:
        args.output_dir.mkdir(parents=True, exist_ok=True)

        sweep_fig = build_kmeans_sweep_figure(sweep_results)
        sweep_fig.write_html(args.output_dir / "silhouette_kmeans_sweep.html")
        LOGGER.info("Saved KMeans sweep chart to %s", args.output_dir / "silhouette_kmeans_sweep.html")

        results = {
            "kmeans_sweep": sweep_results,
            "best_run": {
                "n_clusters": int(best_run["n_clusters"]),
                "overall_score": float(best_run["overall_score"]),
            },
            "metadata": {
                "n_articles": len(embeddings),
                "embedding_dim": embeddings.shape[1],
                "metric": args.metric,
                "seed": args.seed,
                "start_clusters": args.start_clusters,
                "end_clusters": args.end_clusters,
                "step": args.step,
            },
        }
        
        results_path = args.output_dir / "silhouette_results.json"
        with results_path.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        LOGGER.info("Saved results JSON to %s", results_path)
    
    print(f"Analysis complete. Outputs saved to: {args.output_dir}")


if __name__ == "__main__":
    main()
