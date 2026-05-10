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

from faissSearch import load_metadata, load_or_build_index, search_top_k


LOGGER = logging.getLogger("serve_umap_search")


class FaissSearchService:
    def __init__(
        self,
        embeddings_path: Path,
        metadata_path: Path,
        config_path: Path,
        index_path: Path,
        rebuild_index: bool,
        local_files_only: bool,
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

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        query = query.strip()
        if not query:
            return []

        with self.model_lock:
            query_embedding = self.model.encode(
                [query],
                convert_to_numpy=True,
                normalize_embeddings=self.normalized,
                show_progress_bar=False,
            )

        scores, indices = search_top_k(
            index=self.index,
            query_vector=np.asarray(query_embedding[0], dtype=np.float32),
            top_k=top_k,
            metric=self.metric,
            normalized=self.normalized,
        )

        results: list[dict[str, Any]] = []
        for rank, (index, score) in enumerate(zip(indices, scores), start=1):
            if int(index) < 0:
                continue

            article_index = int(index)
            article = self.metadata[article_index]
            results.append(
                {
                    "rank": rank,
                    "score": float(score),
                    "article_index": article_index,
                    "id": article.get("id"),
                    "title": article.get("title"),
                    "url": article.get("url"),
                    "date": article.get("date"),
                    "category": article.get("category"),
                    "keywords": article.get("keywords", []),
                }
            )
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
        if not query:
            self.send_json({"error": "Missing query parameter."}, status=400)
            return
        if len(query) > 1000:
            self.send_json({"error": "Query is too long."}, status=400)
            return

        try:
            results = self.service.search(query, top_k=5)
        except Exception as exc:  # pragma: no cover - visible through the browser.
            LOGGER.exception("Search failed")
            self.send_json({"error": str(exc)}, status=500)
            return

        self.send_json({"query": query, "results": results, "result": results[0] if results else None})

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Serve the UMAP Plotly HTML with a FAISS top-5 search endpoint."
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
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    args = build_parser().parse_args()

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
