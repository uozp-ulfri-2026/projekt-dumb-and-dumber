from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import re
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder

try:
    import faiss  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "faiss is not installed. Install it with 'pip install faiss-cpu' (or faiss-gpu)."
    ) from exc


LOGGER = logging.getLogger("faiss_search")
DEFAULT_RERANKER_MODEL = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
DEFAULT_RERANK_TOP_K = 50


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
        [f"query: {query_text}"],
        convert_to_numpy=True,
        normalize_embeddings=normalize_embeddings,
        show_progress_bar=False,
    )
    return np.asarray(query[0], dtype=np.float32)


def rerank_results(
    query_text: str,
    candidates: list[dict[str, Any]],
    reranker_model_name: str,
    reranker: CrossEncoder | None = None,
    local_files_only: bool = False,
) -> list[dict[str, Any]]:
    if not candidates or not query_text:
        return candidates

    if reranker is None:
        LOGGER.info("Loading cross-encoder reranker '%s'", reranker_model_name)
        reranker = CrossEncoder(reranker_model_name, local_files_only=local_files_only)

    pairs = [[query_text, build_reranker_document_text(candidate)] for candidate in candidates]
    scores = reranker.predict(pairs)

    for candidate, score in zip(candidates, scores):
        candidate["reranker_score"] = float(score)

    reranked = sorted(candidates, key=lambda x: x.get("reranker_score", 0), reverse=True)

    for rank, result in enumerate(reranked, start=1):
        result["rerank"] = rank

    LOGGER.info("Reranked %d candidates. Top: score=%.4f", len(reranked), reranked[0]["reranker_score"])
    return reranked


def build_reranker_document_text(candidate: dict[str, Any]) -> str:
    title = str(candidate.get("title") or "").strip()
    text = str(candidate.get("text") or "").strip()
    if not title:
        return text
    if not text:
        return title

    normalized_title = " ".join(title.casefold().split())
    normalized_prefix = " ".join(text[: max(len(title) + 32, 128)].casefold().split())
    if normalized_title and normalized_title in normalized_prefix:
        return text

    return f"title: {title}\n\n{text}"


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


def _split_into_sentences(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []

    paragraphs = [part.strip() for part in re.split(r"\n{2,}", text) if part.strip()]
    if not paragraphs:
        paragraphs = [text]

    def split_block(block: str) -> list[str]:
        block = block.strip()
        if not block:
            return []

        keyword_match = re.match(r"^Ključne besede:\s*(.+)$", block, flags=re.IGNORECASE | re.DOTALL)
        if keyword_match:
            # Skip keyword blocks entirely so they are not treated as sentences
            return []

        block = block.replace("\n", " ").strip()

        try:
            import spacy

            nlp = spacy.blank("en")
            if "sentencizer" not in nlp.pipe_names:
                nlp.add_pipe("sentencizer")
            doc = nlp(block)
            sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
            if sentences:
                return sentences
        except Exception:
            pass

        try:
            import nltk
            from nltk.tokenize import sent_tokenize

            try:
                nltk.data.find("tokenizers/punkt")
            except Exception:
                try:
                    nltk.download("punkt", quiet=True)
                except Exception:
                    pass

            sentences = sent_tokenize(block)
            sentences = [s.strip() for s in sentences if s.strip()]
            if sentences:
                return sentences
        except Exception:
            pass

        sentences = re.split(r'(?<=[.!?])\s+', block)
        return [s.strip() for s in sentences if s and not s.isspace()]

    sentences: list[str] = []
    for paragraph in paragraphs:
        sentences.extend(split_block(paragraph))

    return [sentence for sentence in sentences if sentence]


def _is_junk_sentence(s: str, min_chars: int = 30, min_words: int = 5) -> bool:
    s = s.strip()
    if len(s) < min_chars:
        return True
    if len(s.split()) < min_words:
        return True
    if re.match(r'^(figure|fig|table|caption|image|photo)[:\s]', s[:12].lower()):
        return True
    if s.isupper():
        return True
    if len(re.findall(r'[A-Za-z]', s)) < 5:
        return True
    return False


def extract_top_sentences_for_article(
    article_text: str,
    query_vector: np.ndarray,
    model_name: str = "intfloat/multilingual-e5-large",
    top_k: int = 3,
    min_score: float = 0.15,
    model: SentenceTransformer | None = None,
) -> list[dict[str, float]]:
    """Return up to top_k sentences from article_text that best match query_vector.

    Sentences that are too short or look like captions/junk are filtered out.
    """
    if not article_text or not str(article_text).strip():
        return []

    sentences = _split_into_sentences(str(article_text))
    sentences = [s for s in sentences if not _is_junk_sentence(s)]
    if not sentences:
        return []

    if model is None:
        model = SentenceTransformer(model_name)

    sent_emb = model.encode(
        sentences,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    ).astype(np.float32, copy=False)

    q = np.asarray(query_vector, dtype=np.float32).reshape(-1)
    q_norm = q / (np.linalg.norm(q) + 1e-12)

    sims = np.dot(sent_emb, q_norm)
    indices = np.argsort(sims)[::-1]
    out: list[dict[str, float]] = []
    for idx in indices:
        score = float(sims[int(idx)])
        if score < min_score:
            continue
        out.append({"sentence": sentences[int(idx)], "score": score})
        if len(out) >= top_k:
            break

    return out


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
        "--reranker",
        type=str,
        default=DEFAULT_RERANKER_MODEL,
        help="Cross-encoder model name for reranking the initial FAISS candidates.",
    )
    parser.add_argument(
        "--rerank-top-k",
        type=int,
        default=DEFAULT_RERANK_TOP_K,
        help="Number of FAISS candidates to rerank before truncating to --top-k.",
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
    if args.rerank_top_k <= 0:
        raise ValueError("--rerank-top-k must be greater than 0.")
    if args.top_k <= 0:
        raise ValueError("--top-k must be greater than 0.")

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
    model_name = "intfloat/multilingual-e5-large"
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

    rerank_k = max(args.top_k, args.rerank_top_k)
    faiss_k = rerank_k if args.query is not None else args.top_k

    if args.query is not None:
        LOGGER.info(
            "Retrieving top %d results from FAISS (will rerank top %d)",
            faiss_k,
            rerank_k,
        )
    else:
        LOGGER.info("Retrieving top %d results from FAISS", faiss_k)
    scores, indices = search_top_k(
        index=index,
        query_vector=query,
        top_k=faiss_k,
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

    if args.query is not None:
        candidates_to_rerank = results[:rerank_k]
        results = rerank_results(
            query_text=args.query,
            candidates=candidates_to_rerank,
            reranker_model_name=args.reranker,
        )
    elif args.reranker:
        LOGGER.warning("Reranker needs a text query. Skipping reranking for raw query embedding input.")

    results = results[:args.top_k]
    # Add explanatory top sentences for the top result when a text query was provided
    if args.query is not None and results:
        try:
            # load model once and reuse for sentence embeddings
            expl_model = SentenceTransformer(model_name)
            top_article = results[0]
            article_text = top_article.get("text", "") or ""
            top_sents = extract_top_sentences_for_article(
                article_text,
                query_vector=query,
                model_name=model_name,
                top_k=3,
                min_score=0.15,
                model=expl_model,
            )
            if top_sents:
                top_article["top_sentences"] = top_sents
        except Exception:
            LOGGER.exception("Failed to compute explanatory top sentences for result.")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
