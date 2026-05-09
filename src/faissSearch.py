from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

try:
    import faiss  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "faiss is not installed. Install it with 'pip install faiss-cpu' (or faiss-gpu)."
    ) from exc


LOGGER = logging.getLogger("faiss_search")


def load_metadata(path: Path) -> list[dict[str, Any]]:
    metadata: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as source_file:
        for line in source_file:
            line = line.strip()
            if not line:
                continue
            metadata.append(json.loads(line))
    return metadata


def load_query_embedding(args: argparse.Namespace, expected_dim: int) -> np.ndarray:
    if args.query_embedding is None and args.query_embedding_file is None:
        raise ValueError("Provide --query-embedding or --query-embedding-file.")

    if args.query_embedding is not None and args.query_embedding_file is not None:
        raise ValueError("Provide only one of --query-embedding or --query-embedding-file.")

    if args.query_embedding is not None:
        parsed = json.loads(args.query_embedding)
        query = np.asarray(parsed, dtype=np.float32)
    else:
        query_path = args.query_embedding_file
        if query_path.suffix.lower() == ".npy":
            query = np.load(query_path).astype(np.float32, copy=False)
        else:
            with query_path.open("r", encoding="utf-8") as source_file:
                parsed = json.load(source_file)
            query = np.asarray(parsed, dtype=np.float32)

    query = np.asarray(query, dtype=np.float32).reshape(-1)
    if query.shape[0] != expected_dim:
        raise ValueError(
            f"Query embedding dimension {query.shape[0]} does not match index dimension {expected_dim}."
        )

    return query


def choose_index(metric: str, dim: int) -> faiss.Index:
    metric = metric.lower()
    if metric == "cosine":
        # For cosine retrieval we use inner product on L2-normalized vectors.
        return faiss.IndexFlatIP(dim)
    if metric == "l2":
        return faiss.IndexFlatL2(dim)
    raise ValueError(f"Unsupported metric: {metric}")


def build_index(embeddings: np.ndarray, metric: str, normalized: bool) -> faiss.Index:
    if embeddings.ndim != 2:
        raise ValueError("Embeddings must be a 2D matrix [num_vectors, dim].")

    vectors = embeddings.astype(np.float32, copy=False)
    dim = vectors.shape[1]

    index = choose_index(metric, dim)

    if metric.lower() == "cosine" and not normalized:
        LOGGER.info("Database vectors are not normalized. Applying L2 normalization for cosine similarity.")
        vectors = vectors.copy()
        faiss.normalize_L2(vectors)

    index.add(vectors)
    return index


def load_or_build_index(
    embeddings: np.ndarray,
    metric: str,
    normalized: bool,
    index_path: Path,
    rebuild_index: bool,
) -> faiss.Index:
    if index_path.exists() and not rebuild_index:
        LOGGER.info("Loading FAISS index from %s", index_path)
        index = faiss.read_index(str(index_path))

        dim_match = getattr(index, "d", None) == embeddings.shape[1]
        size_match = index.ntotal == embeddings.shape[0]
        if dim_match and size_match:
            LOGGER.info("Loaded existing index (%d vectors).", index.ntotal)
            return index

        LOGGER.warning(
            "Existing index metadata mismatch (dim/size). Rebuilding index from embeddings."
        )

    LOGGER.info("Building new FAISS index.")
    index = build_index(embeddings, metric=metric, normalized=normalized)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(index_path))
    LOGGER.info("Saved FAISS index to %s", index_path)
    return index


def embed_query_text(query_text: str, model_name: str, normalize_embeddings: bool) -> np.ndarray:
    LOGGER.info("Embedding text query with model '%s'", model_name)
    model = SentenceTransformer(model_name)
    query = model.encode(
        [query_text],
        convert_to_numpy=True,
        normalize_embeddings=normalize_embeddings,
        show_progress_bar=False,
    )
    return np.asarray(query[0], dtype=np.float32)


def search_top_k(
    index: faiss.Index,
    query_vector: np.ndarray,
    top_k: int,
    metric: str,
    normalized: bool,
) -> tuple[np.ndarray, np.ndarray]:
    query = query_vector.astype(np.float32, copy=False).reshape(1, -1)

    if metric.lower() == "cosine" and not normalized:
        query = query.copy()
        faiss.normalize_L2(query)

    scores, indices = index.search(query, top_k)
    return scores[0], indices[0]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a FAISS index over article embeddings and return top-k nearest articles."
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
        "--config",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "index_config.json",
        help="Path to index config JSON file.",
    )
    parser.add_argument(
        "--index-path",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "faiss.index",
        help="Path to saved FAISS index file.",
    )
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="Force rebuilding index from embeddings and overwrite saved index.",
    )
    parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="Text query (will be embedded automatically).",
    )
    parser.add_argument(
        "--query-embedding",
        type=str,
        default=None,
        help="Inline JSON array embedding, e.g. '[0.1, 0.2, ...]'.",
    )
    parser.add_argument(
        "--query-embedding-file",
        type=Path,
        default=None,
        help="Path to query embedding file (.npy or JSON array).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of most similar articles to return.",
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

    metric = "cosine"
    normalized = True
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    if args.config.exists():
        with args.config.open("r", encoding="utf-8") as cfg_file:
            cfg = json.load(cfg_file)
        metric = str(cfg.get("metric", metric)).lower()
        normalized = bool(cfg.get("normalize_embeddings", normalized))
        model_name = str(cfg.get("model_name", model_name))

    LOGGER.info("Index metric: %s | normalized_embeddings: %s", metric, normalized)
    index = load_or_build_index(
        embeddings=embeddings,
        metric=metric,
        normalized=normalized,
        index_path=args.index_path,
        rebuild_index=args.rebuild_index,
    )

    if args.query is not None:
        query = embed_query_text(
            query_text=args.query,
            model_name=model_name,
            normalize_embeddings=normalized,
        )
    else:
        query = load_query_embedding(args, expected_dim=embeddings.shape[1])

    scores, indices = search_top_k(
        index=index,
        query_vector=query,
        top_k=args.top_k,
        metric=metric,
        normalized=normalized,
    )

    results: list[dict[str, Any]] = []
    for rank, (idx, score) in enumerate(zip(indices, scores), start=1):
        if idx < 0:
            continue
        article = metadata[int(idx)]
        results.append(
            {
                "rank": rank,
                "score": float(score),
                "id": article.get("id"),
                "title": article.get("title"),
                "url": article.get("url"),
                "date": article.get("date"),
                "category": article.get("category"),
                "keywords": article.get("keywords", []),
                "text": article.get("text"),
            }
        )

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
