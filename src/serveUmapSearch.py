from __future__ import annotations

import argparse
import json
import logging
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from typing import Any
from urllib.parse import parse_qs, urlparse

import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

from faissSearch import (
    DEFAULT_RERANK_TOP_K,
    DEFAULT_RERANKER_MODEL,
    extract_top_sentences_for_article,
    load_metadata,
    load_or_build_index,
    rerank_results,
    search_top_k,
)


LOGGER = logging.getLogger("serve_umap_search")


def parse_bool(value: str) -> bool:
    return str(value).strip().casefold() not in {"0", "false", "no", "off"}


def compute_local_coordinates(embeddings: np.ndarray) -> tuple[np.ndarray, str]:
    if embeddings.shape[0] < 3:
        coords = np.zeros((embeddings.shape[0], 2), dtype=np.float32)
        if embeddings.shape[0] == 2:
            coords[1, 0] = 1.0
        return coords, "fallback"

    try:
        import umap

        n_neighbors = min(30, max(2, embeddings.shape[0] - 1))
        reducer = umap.UMAP(
            n_components=2,
            metric="cosine",
            n_neighbors=n_neighbors,
            min_dist=0.05,
            random_state=42,
        )
        return reducer.fit_transform(embeddings).astype(np.float32, copy=False), "umap"
    except Exception:
        LOGGER.exception("Local UMAP failed; falling back to PCA.")

    coords = PCA(n_components=2, random_state=42).fit_transform(embeddings)
    return coords.astype(np.float32, copy=False), "pca"


def build_local_cluster_labels(
    candidates: list[dict[str, Any]],
    cluster_labels: np.ndarray,
    top_k_words: int = 5,
) -> dict[int, str]:
    cluster_ids = sorted(int(cluster_id) for cluster_id in np.unique(cluster_labels))
    grouped_docs: list[str] = []
    dominant_topics: dict[int, str] = {}

    for cluster_id in cluster_ids:
        text_parts: list[str] = []
        topic_counts: dict[str, int] = {}
        row_indices = np.where(cluster_labels == cluster_id)[0]
        for row_index in row_indices:
            candidate = candidates[int(row_index)]
            topic = str(candidate.get("category", "") or "Uncategorized").strip() or "Uncategorized"
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

            article_text = str(candidate.get("text", "") or "").strip()
            if not article_text:
                title = str(candidate.get("title", "") or "").strip()
                keywords = candidate.get("keywords", [])
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
            for cluster_id in cluster_ids
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
            for cluster_id in cluster_ids
        }

    labels: dict[int, str] = {}
    for row_pos, cluster_id in enumerate(cluster_ids):
        row = tfidf_matrix.getrow(row_pos)
        topic_label = dominant_topics.get(cluster_id, "Uncategorized")
        if row.nnz == 0:
            labels[cluster_id] = format_cluster_label(cluster_id, topic_label, [])
            continue

        weights = row.toarray().ravel()
        top_indices = np.argsort(weights)[::-1][:top_k_words]
        top_words = [feature_names[index] for index in top_indices if weights[index] > 0]
        labels[cluster_id] = format_cluster_label(cluster_id, topic_label, top_words)

    return labels


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


class FaissSearchService:
    def __init__(
        self,
        embeddings_path: Path,
        metadata_path: Path,
        config_path: Path,
        index_path: Path,
        rebuild_index: bool,
        local_files_only: bool,
        reranker_model_name: str,
        rerank_top_k: int,
        local_map_size: int,
        local_cluster_count: int,
    ) -> None:
        LOGGER.info("Loading embeddings from %s", embeddings_path)
        self.embeddings = np.load(embeddings_path).astype(np.float32, copy=False)

        LOGGER.info("Loading metadata from %s", metadata_path)
        self.metadata = load_metadata(metadata_path)
        if len(self.metadata) != self.embeddings.shape[0]:
            raise ValueError(
                f"Metadata size ({len(self.metadata)}) does not match embeddings "
                f"rows ({self.embeddings.shape[0]})."
            )

        self.metric = "cosine"
        self.normalized = True
        self.model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        if config_path.exists():
            with config_path.open("r", encoding="utf-8") as cfg_file:
                config = json.load(cfg_file)
            self.metric = str(config.get("metric", self.metric)).lower()
            self.normalized = bool(config.get("normalize_embeddings", self.normalized))
            self.model_name = str(config.get("model_name", self.model_name))

        LOGGER.info("Loading FAISS index from %s", index_path)
        self.index = load_or_build_index(
            embeddings=self.embeddings,
            metric=self.metric,
            normalized=self.normalized,
            index_path=index_path,
            rebuild_index=rebuild_index,
        )

        LOGGER.info("Loading query encoder '%s'", self.model_name)
        self.model = SentenceTransformer(self.model_name, local_files_only=local_files_only)
        self.model_lock = Lock()
        self.local_files_only = local_files_only
        self.reranker_model_name = reranker_model_name
        self.rerank_top_k = rerank_top_k
        self.local_map_size = local_map_size
        self.local_cluster_count = local_cluster_count

        LOGGER.info("Loading cross-encoder reranker '%s'", self.reranker_model_name)
        try:
            self.reranker = CrossEncoder(self.reranker_model_name, local_files_only=local_files_only)
        except OSError as exc:
            if local_files_only:
                raise RuntimeError(
                    "Cross-encoder reranker is not cached locally. Run once with "
                    "`python src\\serveUmapSearch.py --allow-model-download` to download it, "
                    "or pass --reranker with a locally cached cross-encoder model."
                ) from exc
            raise
        self.reranker_lock = Lock()

    def search(self, query: str, top_k: int = 5, use_reranker: bool = True) -> dict[str, Any]:
        query = query.strip()
        if not query:
            return {"results": [], "local_map": None}

        with self.model_lock:
            query_embedding = self.model.encode(
                [f"query: {query}"],
                convert_to_numpy=True,
                normalize_embeddings=self.normalized,
                show_progress_bar=False,
            )

        faiss_k = max(top_k, self.local_map_size, self.rerank_top_k if use_reranker else top_k)
        scores, indices = search_top_k(
            index=self.index,
            query_vector=np.asarray(query_embedding[0], dtype=np.float32),
            top_k=faiss_k,
            metric=self.metric,
            normalized=self.normalized,
        )

        candidates: list[dict[str, Any]] = []
        for rank, (index, score) in enumerate(zip(indices, scores), start=1):
            if int(index) < 0:
                continue

            article_index = int(index)
            article = self.metadata[article_index]
            candidates.append(
                {
                    "rank": rank,
                    "faiss_rank": rank,
                    "score": float(score),
                    "article_index": article_index,
                    "id": article.get("id"),
                    "title": article.get("title"),
                    "url": article.get("url"),
                    "date": article.get("date"),
                    "category": article.get("category"),
                    "keywords": article.get("keywords", []),
                    "text": article.get("text"),
                }
            )

        if use_reranker:
            with self.reranker_lock:
                results = rerank_results(
                    query_text=query,
                    candidates=candidates[: self.rerank_top_k],
                    reranker_model_name=self.reranker_model_name,
                    reranker=self.reranker,
                    local_files_only=self.local_files_only,
                )
        else:
            results = candidates

        results = results[:top_k]
        for rank, result in enumerate(results, start=1):
            result["rank"] = rank
            top_sentences = extract_top_sentences_for_article(
                article_text=str(result.get("text", "") or ""),
                query_vector=np.asarray(query_embedding[0], dtype=np.float32),
                model_name=self.model_name,
                top_k=3,
                min_score=0.12,
                model=self.model,
            )
            result["top_sentences"] = top_sentences
            result.pop("text", None)

        local_map = self.build_local_map(candidates=candidates[: self.local_map_size], results=results)
        return {"results": results, "local_map": local_map}

    def build_local_map(
        self,
        candidates: list[dict[str, Any]],
        results: list[dict[str, Any]],
    ) -> dict[str, Any] | None:
        if len(candidates) < 2:
            return None

        article_indices = np.asarray([int(candidate["article_index"]) for candidate in candidates], dtype=np.int64)
        local_embeddings = self.embeddings[article_indices].astype(np.float32, copy=False)
        n_clusters = min(max(2, self.local_cluster_count), len(candidates))
        cluster_labels = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto").fit_predict(local_embeddings)
        coordinates, projection_method = compute_local_coordinates(local_embeddings)
        cluster_names = build_local_cluster_labels(candidates=candidates, cluster_labels=cluster_labels)
        result_ranks = {int(result["article_index"]): int(result["rank"]) for result in results}

        points: list[dict[str, Any]] = []
        for row, candidate in enumerate(candidates):
            article_index = int(candidate["article_index"])
            points.append(
                {
                    "x": float(coordinates[row, 0]),
                    "y": float(coordinates[row, 1]),
                    "cluster": cluster_names.get(int(cluster_labels[row]), f"C{int(cluster_labels[row]) + 1:02d}"),
                    "article_index": article_index,
                    "faiss_rank": int(candidate["faiss_rank"]),
                    "score": float(candidate["score"]),
                    "result_rank": result_ranks.get(article_index),
                    "title": candidate.get("title"),
                    "url": candidate.get("url"),
                    "date": candidate.get("date"),
                    "category": candidate.get("category"),
                }
            )

        return {
            "size": len(points),
            "projection": projection_method,
            "cluster_count": int(n_clusters),
            "points": points,
        }


class UmapSearchHandler(SimpleHTTPRequestHandler):
    service: FaissSearchService
    default_html: str

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/search":
            self.handle_search(parsed.query)
            return

        if parsed.path == "/":
            self.path = "/" + self.default_html
        super().do_GET()

    def handle_search(self, query_string: str) -> None:
        params = parse_qs(query_string)
        query = (params.get("query") or params.get("q") or [""])[0].strip()
        use_reranker = parse_bool((params.get("reranker") or params.get("use_reranker") or ["true"])[0])
        if not query:
            self.send_json({"error": "Missing query parameter."}, status=400)
            return
        if len(query) > 1000:
            self.send_json({"error": "Query is too long."}, status=400)
            return

        try:
            search_payload = self.service.search(query, top_k=5, use_reranker=use_reranker)
        except Exception as exc:  # pragma: no cover - visible through the browser.
            LOGGER.exception("Search failed")
            self.send_json({"error": str(exc)}, status=500)
            return

        results = search_payload["results"]
        self.send_json(
            {
                "query": query,
                "use_reranker": use_reranker,
                "results": results,
                "result": results[0] if results else None,
                "local_map": search_payload["local_map"],
            }
        )

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Serve the UMAP Plotly HTML with a FAISS + cross-encoder reranked search endpoint."
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind.",
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
        "--html",
        type=Path,
        default=Path("data") / "mmc_embeddings" / "umap_visualization.html",
        help="UMAP visualization HTML to serve at /.",
    )
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="Force rebuilding the FAISS index before serving.",
    )
    parser.add_argument(
        "--allow-model-download",
        action="store_true",
        help="Allow sentence-transformers to download model files if they are not cached locally.",
    )
    parser.add_argument(
        "--reranker",
        type=str,
        default=DEFAULT_RERANKER_MODEL,
        help="Cross-encoder model name used to rerank FAISS candidates.",
    )
    parser.add_argument(
        "--rerank-top-k",
        type=int,
        default=DEFAULT_RERANK_TOP_K,
        help="Number of FAISS candidates to rerank before returning the top results.",
    )
    parser.add_argument(
        "--local-map-size",
        type=int,
        default=1000,
        help="Number of FAISS candidates to project into the query-specific local map.",
    )
    parser.add_argument(
        "--local-cluster-count",
        type=int,
        default=12,
        help="Number of KMeans clusters to compute inside each local map.",
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
    if args.local_map_size <= 1:
        raise ValueError("--local-map-size must be greater than 1.")
    if args.local_cluster_count < 2:
        raise ValueError("--local-cluster-count must be at least 2.")

    repo_root = Path.cwd().resolve()
    default_html_path = args.html.resolve()
    try:
        default_html = default_html_path.relative_to(repo_root).as_posix()
    except ValueError as exc:
        raise ValueError("--html must be inside the current working directory.") from exc

    UmapSearchHandler.service = FaissSearchService(
        embeddings_path=args.embeddings,
        metadata_path=args.metadata,
        config_path=args.config,
        index_path=args.index_path,
        rebuild_index=args.rebuild_index,
        local_files_only=not args.allow_model_download,
        reranker_model_name=args.reranker,
        rerank_top_k=args.rerank_top_k,
        local_map_size=args.local_map_size,
        local_cluster_count=args.local_cluster_count,
    )
    UmapSearchHandler.default_html = default_html

    handler = partial(UmapSearchHandler, directory=str(repo_root))
    server = ThreadingHTTPServer((args.host, args.port), handler)
    url = f"http://{args.host}:{args.port}/"
    LOGGER.info("Serving UMAP FAISS search at %s", url)
    print(f"Open: {url}")
    server.serve_forever()


if __name__ == "__main__":
    main()
