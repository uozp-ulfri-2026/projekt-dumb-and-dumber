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

    def search(self, query: str, top_k: int = 5, use_reranker: bool = True) -> list[dict[str, Any]]:
        query = query.strip()
        if not query:
            return []

        with self.model_lock:
            query_embedding = self.model.encode(
                [f"query: {query}"],
                convert_to_numpy=True,
                normalize_embeddings=self.normalized,
                show_progress_bar=False,
            )

        faiss_k = max(top_k, self.rerank_top_k) if use_reranker else top_k
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
                    candidates=candidates,
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
        return results


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
            results = self.service.search(query, top_k=5, use_reranker=use_reranker)
        except Exception as exc:  # pragma: no cover - visible through the browser.
            LOGGER.exception("Search failed")
            self.send_json({"error": str(exc)}, status=500)
            return

        self.send_json(
            {
                "query": query,
                "use_reranker": use_reranker,
                "results": results,
                "result": results[0] if results else None,
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
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    args = build_parser().parse_args()
    if args.rerank_top_k <= 0:
        raise ValueError("--rerank-top-k must be greater than 0.")

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
