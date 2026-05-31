from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import plotly.graph_objects as go
from sklearn.metrics import auc, roc_curve
from sklearn.preprocessing import normalize


LOGGER = logging.getLogger("roc_auc_analysis")


def load_embeddings(path: Path) -> np.ndarray:
    LOGGER.info("Loading embeddings from %s", path)
    embeddings = np.load(path).astype(np.float32, copy=False)
    if embeddings.ndim != 2:
        raise ValueError("Embeddings must be a 2D array.")
    LOGGER.info("Loaded embeddings shape: (%d, %d)", embeddings.shape[0], embeddings.shape[1])
    return embeddings


def load_metadata(path: Path) -> list[dict[str, Any]]:
    LOGGER.info("Loading metadata from %s", path)
    metadata: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as source_file:
        first_non_empty = ""
        for line in source_file:
            line = line.strip()
            if not line:
                continue
            if not metadata:
                first_non_empty = line
            metadata.append(json.loads(line))

    if not metadata:
        raise ValueError("Metadata file is empty.")

    if first_non_empty.startswith("["):
        raise ValueError(
            "Expected JSONL metadata, but the file appears to be a JSON array. "
            "Use the cleaned dataset file or convert it to JSONL."
        )

    LOGGER.info("Loaded %d metadata records", len(metadata))
    return metadata


def extract_categories(metadata: list[dict[str, Any]]) -> np.ndarray:
    categories = [str(record.get("category", "Uncategorized") or "Uncategorized") for record in metadata]
    unique_categories = sorted(set(categories))
    category_to_id = {category: index for index, category in enumerate(unique_categories)}
    labels = np.array([category_to_id[category] for category in categories], dtype=np.int32)
    LOGGER.info("Found %d categories", len(unique_categories))
    return labels


def build_category_buckets(labels: np.ndarray) -> dict[int, np.ndarray]:
    buckets: dict[int, np.ndarray] = {}
    for label in np.unique(labels):
        buckets[int(label)] = np.flatnonzero(labels == label)
    return buckets


def sample_pair_indices(
    labels: np.ndarray,
    positive_pairs: int,
    negative_pairs: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    buckets = build_category_buckets(labels)
    category_ids = np.array(sorted(buckets.keys()), dtype=np.int32)

    pos_i: list[int] = []
    pos_j: list[int] = []
    neg_i: list[int] = []
    neg_j: list[int] = []

    positive_categories = [category_id for category_id, indices in buckets.items() if len(indices) >= 2]
    if not positive_categories:
        raise ValueError("No category has at least two articles, so no positive pairs can be formed.")

    for _ in range(positive_pairs):
        category_id = int(rng.choice(positive_categories))
        indices = buckets[category_id]
        first, second = rng.choice(indices, size=2, replace=False)
        pos_i.append(int(first))
        pos_j.append(int(second))

    if len(category_ids) < 2:
        raise ValueError("Need at least two categories to form negative pairs.")

    for _ in range(negative_pairs):
        first_category, second_category = rng.choice(category_ids, size=2, replace=False)
        first = int(rng.choice(buckets[int(first_category)]))
        second = int(rng.choice(buckets[int(second_category)]))
        neg_i.append(first)
        neg_j.append(second)

    pair_i = np.asarray(pos_i + neg_i, dtype=np.int64)
    pair_j = np.asarray(pos_j + neg_j, dtype=np.int64)
    return pair_i, pair_j


def cosine_similarity_scores(embeddings: np.ndarray, pair_i: np.ndarray, pair_j: np.ndarray) -> np.ndarray:
    normalized_embeddings = normalize(embeddings, norm="l2")
    scores = np.sum(normalized_embeddings[pair_i] * normalized_embeddings[pair_j], axis=1)
    return np.asarray(scores, dtype=np.float32)


def build_roc_figure(fpr: np.ndarray, tpr: np.ndarray, roc_auc: float) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=fpr,
            y=tpr,
            mode="lines",
            line={"width": 3},
            name=f"ROC (AUC = {roc_auc:.4f})",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode="lines",
            line={"width": 2, "dash": "dash"},
            name="Random baseline",
        )
    )
    fig.update_layout(
        title="ROC Curve: Same Category vs Different Category Pairs",
        xaxis_title="False Positive Rate",
        yaxis_title="True Positive Rate",
        template="plotly_white",
        width=900,
        height=700,
    )
    return fig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate ROC/AUC for article pairs where same-category pairs are positive."
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
        "--positive-pairs",
        type=int,
        default=20000,
        help="Number of positive pairs to sample from the same category.",
    )
    parser.add_argument(
        "--negative-pairs",
        type=int,
        default=20000,
        help="Number of negative pairs to sample from different categories.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for sampling pairs.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data") / "roc_auc_analysis",
        help="Directory where outputs will be written.",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Skip writing the ROC curve HTML file.",
    )
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    args = build_parser().parse_args()

    if args.positive_pairs <= 0 or args.negative_pairs <= 0:
        raise ValueError("--positive-pairs and --negative-pairs must be greater than 0.")

    embeddings = load_embeddings(args.embeddings)
    metadata = load_metadata(args.metadata)
    if len(embeddings) != len(metadata):
        raise ValueError(
            f"Embeddings count ({len(embeddings)}) does not match metadata records ({len(metadata)})."
        )

    labels = extract_categories(metadata)
    pair_i, pair_j = sample_pair_indices(
        labels=labels,
        positive_pairs=args.positive_pairs,
        negative_pairs=args.negative_pairs,
        seed=args.seed,
    )

    scores = cosine_similarity_scores(embeddings, pair_i, pair_j)
    y_true = np.concatenate(
        [
            np.ones(args.positive_pairs, dtype=np.int32),
            np.zeros(args.negative_pairs, dtype=np.int32),
        ]
    )

    fpr, tpr, thresholds = roc_curve(y_true, scores)
    roc_auc = float(auc(fpr, tpr))

    positive_scores = scores[: args.positive_pairs]
    negative_scores = scores[args.positive_pairs :]

    print(f"AUC: {roc_auc:.4f}")
    print(f"Positive pairs: {args.positive_pairs}")
    print(f"Negative pairs: {args.negative_pairs}")
    print(f"Mean positive similarity: {float(np.mean(positive_scores)):.4f}")
    print(f"Mean negative similarity: {float(np.mean(negative_scores)):.4f}")
    print(f"Score gap (pos - neg): {float(np.mean(positive_scores) - np.mean(negative_scores)):.4f}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = {
        "auc": roc_auc,
        "positive_pairs": int(args.positive_pairs),
        "negative_pairs": int(args.negative_pairs),
        "seed": int(args.seed),
        "mean_positive_similarity": float(np.mean(positive_scores)),
        "mean_negative_similarity": float(np.mean(negative_scores)),
        "score_gap": float(np.mean(positive_scores) - np.mean(negative_scores)),
        "metadata": {
            "n_articles": int(len(embeddings)),
            "embedding_dim": int(embeddings.shape[1]),
        },
    }

    results_path = args.output_dir / "roc_auc_results.json"
    with results_path.open("w", encoding="utf-8") as target_file:
        json.dump(results, target_file, ensure_ascii=False, indent=2)
    LOGGER.info("Saved results JSON to %s", results_path)

    if not args.no_plot:
        roc_fig = build_roc_figure(fpr, tpr, roc_auc)
        roc_path = args.output_dir / "roc_curve.html"
        roc_fig.write_html(roc_path)
        LOGGER.info("Saved ROC curve to %s", roc_path)

    print(f"Outputs saved to: {args.output_dir}")


if __name__ == "__main__":
    main()
