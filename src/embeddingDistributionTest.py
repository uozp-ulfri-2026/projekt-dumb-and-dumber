from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np


LOGGER = logging.getLogger("embedding_distribution_test")


def load_config(config_path: Path) -> dict[str, Any]:
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def iter_chunks(embeddings: np.ndarray, chunk_size: int):
    for start in range(0, embeddings.shape[0], chunk_size):
        end = min(start + chunk_size, embeddings.shape[0])
        yield start, end, embeddings[start:end]


def compute_norm_stats_and_unit_sum(
    embeddings: np.ndarray,
    chunk_size: int,
) -> tuple[dict[str, float], np.ndarray, int]:
    dim = embeddings.shape[1]
    unit_sum = np.zeros(dim, dtype=np.float64)
    zero_vectors = 0

    norm_count = 0
    norm_sum = 0.0
    norm_sq_sum = 0.0
    norm_min = float("inf")
    norm_max = float("-inf")

    for start, end, chunk in iter_chunks(embeddings, chunk_size):
        LOGGER.info("Processing exact chunk rows %d-%d", start, end)
        chunk64 = chunk.astype(np.float64, copy=False)
        norms = np.linalg.norm(chunk64, axis=1)

        norm_count += int(norms.size)
        norm_sum += float(np.sum(norms))
        norm_sq_sum += float(np.sum(norms * norms))
        norm_min = min(norm_min, float(np.min(norms)))
        norm_max = max(norm_max, float(np.max(norms)))

        nonzero = norms > 0
        zero_vectors += int(np.count_nonzero(~nonzero))
        if np.any(nonzero):
            unit_sum += np.sum(chunk64[nonzero] / norms[nonzero, None], axis=0)

    norm_mean = norm_sum / norm_count
    norm_var = max(0.0, norm_sq_sum / norm_count - norm_mean * norm_mean)
    norm_stats = {
        "min": norm_min,
        "max": norm_max,
        "mean": norm_mean,
        "std": float(np.sqrt(norm_var)),
    }
    return norm_stats, unit_sum, zero_vectors


def sample_pair_similarities(
    embeddings: np.ndarray,
    sample_pairs: int,
    sample_batch_size: int,
    seed: int,
) -> np.ndarray:
    if sample_pairs <= 0:
        return np.empty(0, dtype=np.float32)

    rng = np.random.default_rng(seed)
    n_rows = embeddings.shape[0]
    similarities = np.empty(sample_pairs, dtype=np.float32)
    written = 0

    while written < sample_pairs:
        batch_size = min(sample_batch_size, sample_pairs - written)
        left_indices = rng.integers(0, n_rows, size=batch_size)
        right_indices = rng.integers(0, n_rows, size=batch_size)

        same = left_indices == right_indices
        while np.any(same):
            right_indices[same] = rng.integers(0, n_rows, size=int(np.count_nonzero(same)))
            same = left_indices == right_indices

        left = embeddings[left_indices].astype(np.float64, copy=False)
        right = embeddings[right_indices].astype(np.float64, copy=False)

        left_norms = np.linalg.norm(left, axis=1)
        right_norms = np.linalg.norm(right, axis=1)
        denom = left_norms * right_norms
        valid = denom > 0

        batch_sims = np.zeros(batch_size, dtype=np.float64)
        batch_sims[valid] = np.sum(left[valid] * right[valid], axis=1) / denom[valid]
        similarities[written : written + batch_size] = batch_sims.astype(np.float32, copy=False)
        written += batch_size

    return similarities


def summarize_sample(similarities: np.ndarray) -> dict[str, float] | None:
    if similarities.size == 0:
        return None

    quantiles = np.quantile(
        similarities.astype(np.float64, copy=False),
        [0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99],
    )
    return {
        "count": int(similarities.size),
        "mean": float(np.mean(similarities)),
        "std": float(np.std(similarities)),
        "min": float(np.min(similarities)),
        "p01": float(quantiles[0]),
        "p05": float(quantiles[1]),
        "p25": float(quantiles[2]),
        "p50": float(quantiles[3]),
        "p75": float(quantiles[4]),
        "p95": float(quantiles[5]),
        "p99": float(quantiles[6]),
        "max": float(np.max(similarities)),
    }


def interpret_mean(mean_cosine: float) -> str:
    if mean_cosine >= 0.8:
        return "highly_collapsed"
    if mean_cosine >= 0.5:
        return "strongly_anisotropic"
    if mean_cosine >= 0.2:
        return "moderately_anisotropic"
    if mean_cosine >= -0.05:
        return "well_spread"
    return "very_spread_or_centered_negative"


def write_markdown(result: dict[str, Any], output_path: Path) -> None:
    exact = result["exact_all_distinct_pairs"]
    sample = result.get("sample_random_distinct_pairs")
    norm_stats = result["embedding_norms"]

    lines = [
        "# Embedding Distribution Isotropic Test",
        "",
        f"Created: {result['created_at']}",
        f"Embedding file: `{result['embeddings_path']}`",
        f"Model: `{result.get('model_name', 'unknown')}`",
        f"Shape: `{result['shape'][0]} x {result['shape'][1]}`",
        "",
        "## Exact All-Pairs Result",
        "",
        f"- Distinct pair count: {exact['distinct_pair_count']}",
        f"- Exact mean cosine similarity: {exact['mean_cosine_similarity']:.6f}",
        f"- Centroid norm of normalized vectors: {exact['centroid_norm']:.6f}",
        f"- Interpretation: `{exact['interpretation']}`",
        "",
        "The exact mean is computed without materializing all pairs, using the identity based on the norm of the sum of normalized vectors.",
        "",
        "## Embedding Norms",
        "",
        f"- Min: {norm_stats['min']:.6f}",
        f"- Mean: {norm_stats['mean']:.6f}",
        f"- Max: {norm_stats['max']:.6f}",
        f"- Std: {norm_stats['std']:.6f}",
        f"- Zero vectors: {result['zero_vectors']}",
    ]

    if sample is not None:
        lines.extend(
            [
                "",
                "## Random Pair Sample",
                "",
                f"- Sample count: {sample['count']}",
                f"- Mean: {sample['mean']:.6f}",
                f"- Std: {sample['std']:.6f}",
                f"- Min: {sample['min']:.6f}",
                f"- P01: {sample['p01']:.6f}",
                f"- P05: {sample['p05']:.6f}",
                f"- P25: {sample['p25']:.6f}",
                f"- P50: {sample['p50']:.6f}",
                f"- P75: {sample['p75']:.6f}",
                f"- P95: {sample['p95']:.6f}",
                f"- P99: {sample['p99']:.6f}",
                f"- Max: {sample['max']:.6f}",
            ]
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate embedding anisotropy via exact average pairwise cosine similarity."
    )
    parser.add_argument(
        "--embeddings",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "embeddings.npy",
        help="Path to embeddings .npy file.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "index_config.json",
        help="Optional index config JSON.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("data") / "evaluation" / "embedding_distribution_test.json",
        help="Where to write JSON results.",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("data") / "evaluation" / "embedding_distribution_test.md",
        help="Where to write Markdown results.",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=8192,
        help="Rows per chunk for the exact pass.",
    )
    parser.add_argument(
        "--sample-pairs",
        type=int,
        default=200000,
        help="Number of random distinct pairs to sample for distribution quantiles. Use 0 to skip.",
    )
    parser.add_argument(
        "--sample-batch-size",
        type=int,
        default=10000,
        help="Random pair sample batch size.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for sampled pairs.",
    )
    return parser


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
    args = build_parser().parse_args()

    if args.chunk_size <= 0:
        raise ValueError("--chunk-size must be positive.")
    if args.sample_pairs < 0:
        raise ValueError("--sample-pairs cannot be negative.")
    if args.sample_batch_size <= 0:
        raise ValueError("--sample-batch-size must be positive.")

    config = load_config(args.config)
    LOGGER.info("Loading embeddings from %s", args.embeddings)
    embeddings = np.load(args.embeddings, mmap_mode="r")
    if embeddings.ndim != 2:
        raise ValueError("Embeddings must be a 2D matrix [num_vectors, dim].")

    n_rows, dim = embeddings.shape
    if n_rows < 2:
        raise ValueError("Need at least two embeddings.")

    LOGGER.info("Embedding shape: (%d, %d)", n_rows, dim)
    norm_stats, unit_sum, zero_vectors = compute_norm_stats_and_unit_sum(
        embeddings=embeddings,
        chunk_size=args.chunk_size,
    )

    nonzero_count = n_rows - zero_vectors
    if nonzero_count < 2:
        raise ValueError("Need at least two non-zero embeddings.")

    sum_norm_sq = float(np.dot(unit_sum, unit_sum))
    mean_cosine = (sum_norm_sq - nonzero_count) / (nonzero_count * (nonzero_count - 1))
    centroid_norm = float(np.sqrt(sum_norm_sq) / nonzero_count)
    distinct_pair_count = nonzero_count * (nonzero_count - 1) // 2

    LOGGER.info("Exact mean cosine over distinct pairs: %.6f", mean_cosine)

    sample_summary = None
    if args.sample_pairs:
        LOGGER.info("Sampling %d random distinct pairs", args.sample_pairs)
        sampled = sample_pair_similarities(
            embeddings=embeddings,
            sample_pairs=args.sample_pairs,
            sample_batch_size=args.sample_batch_size,
            seed=args.seed,
        )
        sample_summary = summarize_sample(sampled)

    result = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "embeddings_path": str(args.embeddings).replace("\\", "/"),
        "config_path": str(args.config).replace("\\", "/"),
        "model_name": config.get("model_name"),
        "normalize_embeddings_config": config.get("normalize_embeddings"),
        "shape": [int(n_rows), int(dim)],
        "dtype": str(embeddings.dtype),
        "zero_vectors": int(zero_vectors),
        "embedding_norms": norm_stats,
        "exact_all_distinct_pairs": {
            "nonzero_vector_count": int(nonzero_count),
            "distinct_pair_count": int(distinct_pair_count),
            "mean_cosine_similarity": float(mean_cosine),
            "centroid_norm": centroid_norm,
            "interpretation": interpret_mean(mean_cosine),
        },
        "sample_random_distinct_pairs": sample_summary,
        "notes": [
            "Exact mean excludes self-pairs and normalizes rows before computing cosine.",
            "The formula avoids materializing the O(n^2) pair matrix.",
        ],
    }

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.output_md)

    print(json.dumps(result["exact_all_distinct_pairs"], ensure_ascii=False, indent=2))
    if sample_summary is not None:
        print(json.dumps({"sample_random_distinct_pairs": sample_summary}, ensure_ascii=False, indent=2))
    print(f"Wrote {args.output_json}")
    print(f"Wrote {args.output_md}")


if __name__ == "__main__":
    main()
