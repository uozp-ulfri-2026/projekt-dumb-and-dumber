from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import time
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from typing import Any
from urllib.parse import parse_qs, urlparse

import numpy as np
import requests
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from sklearn.cluster import AgglomerativeClustering
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
MAX_SEARCH_ARTICLES = 100
DEFAULT_LOCAL_MAP_SIZE = 100
LOCAL_CLUSTER_REDUCTION_DIM = 20
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"
DEFAULT_GEMINI_CACHE_PATH = Path("data") / "mmc_embeddings" / "gemini_label_cache.json"


def parse_bool(value: str) -> bool:
    return str(value).strip().casefold() not in {"0", "false", "no", "off"}


def reduce_embeddings_for_clustering(embeddings: np.ndarray, target_dim: int = LOCAL_CLUSTER_REDUCTION_DIM) -> np.ndarray:
    if embeddings.ndim != 2:
        raise ValueError("Embeddings must be a 2D matrix [num_vectors, dim].")

    if embeddings.shape[0] < 2 or embeddings.shape[1] < 2:
        return embeddings.astype(np.float32, copy=False)

    n_components = min(target_dim, embeddings.shape[1], max(1, embeddings.shape[0] - 1))
    if n_components >= embeddings.shape[1]:
        return embeddings.astype(np.float32, copy=False)

    try:
        import umap

        reducer = umap.UMAP(
            n_components=n_components,
            metric="cosine",
            n_neighbors=min(15, max(2, embeddings.shape[0] - 1)),
            min_dist=0.0,
            random_state=42,
        )
        return reducer.fit_transform(embeddings).astype(np.float32, copy=False)
    except Exception:
        LOGGER.exception("UMAP reduction to %d dims failed; falling back to PCA.", n_components)

    reducer = PCA(n_components=n_components, random_state=42, svd_solver="randomized")
    return reducer.fit_transform(embeddings).astype(np.float32, copy=False)


def compute_agglomerative_labels(embeddings: np.ndarray, n_clusters: int) -> np.ndarray:
    if embeddings.shape[0] < 2:
        return np.full(embeddings.shape[0], -1, dtype=np.int32)

    # Keep the local map coarse enough to read at a glance. With the 100-article cap,
    # this yields roughly 2-7 clusters instead of fragmenting the view into many tiny groups.
    effective_n_clusters = min(max(2, n_clusters), max(2, embeddings.shape[0] // 15))
    if effective_n_clusters != n_clusters:
        LOGGER.info(
            "Adjusted local agglomerative cluster count to %d for the sampled dataset size",
            effective_n_clusters,
        )

    cluster_model = AgglomerativeClustering(
        n_clusters=effective_n_clusters,
        linkage="average",
        metric="cosine",
    )
    return cluster_model.fit_predict(embeddings).astype(np.int32, copy=False)


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
            cluster_id: dominant_topics.get(cluster_id, "Uncategorized")
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
            cluster_id: dominant_topics.get(cluster_id, "Uncategorized")
            for cluster_id in cluster_ids
        }

    labels: dict[int, str] = {}
    for row_pos, cluster_id in enumerate(cluster_ids):
        row = tfidf_matrix.getrow(row_pos)
        topic_label = dominant_topics.get(cluster_id, "Uncategorized")
        if row.nnz == 0:
            labels[cluster_id] = topic_label
            continue

        weights = row.toarray().ravel()
        top_indices = np.argsort(weights)[::-1][:top_k_words]
        top_words = [feature_names[index] for index in top_indices if weights[index] > 0]
        labels[cluster_id] = topic_label

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
        enable_auto_labeling: bool,
        gemini_model: str,
        gemini_cache_path: Path,
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
        self.enable_auto_labeling = enable_auto_labeling
        self.gemini_model = gemini_model
        self.gemini_cache_path = gemini_cache_path
        self.gemini_cache_lock = Lock()
        self.gemini_cache = self._load_gemini_cache()
        self.gemini_retry_after_epoch = 0.0

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

        requested_candidates = max(top_k, self.local_map_size, self.rerank_top_k if use_reranker else top_k)
        faiss_k = min(MAX_SEARCH_ARTICLES, requested_candidates)
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
        reduced_embeddings = reduce_embeddings_for_clustering(local_embeddings)
        cluster_labels = compute_agglomerative_labels(reduced_embeddings, n_clusters=self.local_cluster_count)
        coordinates, projection_method = compute_local_coordinates(reduced_embeddings)
        # First produce TF-IDF based labels (fast fallback)
        cluster_names = build_local_cluster_labels(candidates=candidates, cluster_labels=cluster_labels)

        # Attempt to label clusters using a Gemini LLM (batch). If the environment
        # is not configured or the call fails, we silently fall back to TF-IDF labels.
        if self.enable_auto_labeling:
            try:
                gemini_labels = self._label_clusters_with_gemini(
                    candidates=candidates,
                    cluster_labels=cluster_labels,
                    local_embeddings=local_embeddings,
                    reduced_embeddings=reduced_embeddings,
                    top_k=5,
                )
                if gemini_labels:
                    for cid, topic in gemini_labels.items():
                        cluster_names[int(cid)] = topic
            except Exception:
                LOGGER.exception("Gemini labeling failed; using TF-IDF labels.")
        result_ranks = {int(result["article_index"]): int(result["rank"]) for result in results}

        points: list[dict[str, Any]] = []
        for row, candidate in enumerate(candidates):
            article_index = int(candidate["article_index"])
            points.append(
                {
                    "x": float(coordinates[row, 0]),
                    "y": float(coordinates[row, 1]),
                    "cluster": cluster_names.get(int(cluster_labels[row]), "Uncategorized"),
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
            "cluster_count": int(len({int(label) for label in cluster_labels if int(label) >= 0})),
            "cluster_reduction_dim": int(LOCAL_CLUSTER_REDUCTION_DIM),
            "points": points,
        }

    def _label_clusters_with_gemini(
        self,
        candidates: list[dict[str, Any]],
        cluster_labels: np.ndarray,
        local_embeddings: np.ndarray,
        reduced_embeddings: np.ndarray,
        top_k: int = 5,
        timeout: int = 15,
    ) -> dict[int, str] | None:
        """Ask a Gemini-compatible LLM to produce one short Slovenian topic
        label (max 5 words) for each cluster. Returns a mapping cluster_id -> topic
        or None on early exit.

        Configuration (Google AI Studio preferred):
        - GEMINI_API_KEY: API key from Google AI Studio
        - GEMINI_MODEL: optional override (otherwise --gemini-model / default)

        Compatibility mode (optional):
        - GEMINI_API_URL: if set, fallback to raw HTTP POST endpoint with bearer auth
        """
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return None

        if time.time() < self.gemini_retry_after_epoch:
            wait_seconds = int(self.gemini_retry_after_epoch - time.time())
            LOGGER.info("Skipping Gemini labeling due to active backoff (%ds remaining).", max(0, wait_seconds))
            return None

        # Build representative examples per cluster using nearest-to-centroid articles
        cluster_ids = sorted(int(cid) for cid in np.unique(cluster_labels))
        payload_blocks: list[str] = []
        cache_clusters: list[dict[str, Any]] = []

        for cid in cluster_ids:
            rows = np.where(cluster_labels == cid)[0]
            if rows.size == 0:
                continue

            # Centroid in reduced space
            centroid_red = np.mean(reduced_embeddings[rows], axis=0)
            # Compute cosine similarity of members to centroid to pick representatives
            cent_norm = centroid_red / (np.linalg.norm(centroid_red) + 1e-12)
            member_red = reduced_embeddings[rows]
            sims = member_red.dot(cent_norm)
            order = np.argsort(sims)[::-1][: top_k]
            examples: list[str] = []

            # For summarization query vector use mean of original embeddings for cluster
            centroid_full = np.mean(local_embeddings[rows], axis=0)

            for pos in order:
                idx = int(rows[int(pos)])
                cand = candidates[int(idx)]
                title = str(cand.get("title") or "").strip()
                text = str(cand.get("text") or "").strip()
                snippet = ""
                if text:
                    try:
                        sents = extract_top_sentences_for_article(
                            article_text=text,
                            query_vector=centroid_full,
                            model_name=self.model_name,
                            top_k=2,
                            min_score=0.05,
                            model=self.model,
                        )
                        if sents:
                            snippet = " ".join(s.get("sentence", "") for s in sents)
                    except Exception:
                        LOGGER.debug("Failed to extract top sentences for candidate %s", cand.get("id"), exc_info=True)
                if not snippet and text:
                    snippet = " ".join(part.strip() for part in re.split(r"(?<=[.!?])\\s+", text)[:2] if part.strip())
                if not snippet and title:
                    snippet = title

                example_line = f"- {title}: {snippet}" if snippet else f"- {title}"
                examples.append(example_line)

            block = f"Cluster {cid} representative articles:\n" + "\n".join(examples)
            payload_blocks.append(block)
            cache_clusters.append({"cluster_id": cid, "examples": examples})

        if not payload_blocks:
            return None

        model_name = os.environ.get("GEMINI_MODEL", self.gemini_model)
        cache_key = self._build_gemini_cache_key(model_name=model_name, cache_clusters=cache_clusters)
        cached = self._get_cached_gemini_labels(cache_key)
        if cached:
            return cached

        # Build a clear instruction that forces strict JSON output.
        prompt = (
            "Imas skupine novicarskih clankov o slovenskih aktualnih dogodkih. "
            "Za vsako skupino vrni ENO temo v SLOVENSCINI, dolgo NAJVEC 5 besed. "
            "Ne vracaj stavkov, razlag ali dveh delov. Vrni samo temo. "
            "Vrni IZKLJUCNO JSON polje objektov s kljuci: cluster_id (integer), topic (string). "
            "Brez dodatnega besedila. Primeri skupin so spodaj.\n\n"
            + "\n\n".join(payload_blocks)
            + "\n\nVrni JSON kot: [{\"cluster_id\": 0, \"topic\": \"vpis v srednje sole\"}, ...]"
        )

        parsed = self._query_gemini(prompt=prompt, api_key=api_key, model_name=model_name, timeout=timeout)
        if parsed is None:
            return None

        out = self._parse_gemini_cluster_labels(parsed)
        if not out:
            return None
        self._set_cached_gemini_labels(cache_key, out)
        return out

    def _query_gemini(self, prompt: str, api_key: str, model_name: str, timeout: int) -> Any | None:
        api_url = os.environ.get("GEMINI_API_URL", "").strip()

        # Preferred path: Google AI Studio SDK
        if not api_url:
            try:
                # New Google AI Studio SDK path (preferred)
                from google import genai

                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config={
                        "temperature": 0.2,
                        "response_mime_type": "application/json",
                    },
                )
                text = (getattr(response, "text", "") or "").strip()
                if not text:
                    LOGGER.warning("Gemini SDK returned empty text response.")
                    return None
                return self._parse_json_from_text(text)
            except ImportError:
                # Backward-compatible legacy SDK fallback.
                try:
                    import google.generativeai as genai_legacy

                    genai_legacy.configure(api_key=api_key)
                    model = genai_legacy.GenerativeModel(model_name)
                    response = model.generate_content(
                        prompt,
                        generation_config={
                            "temperature": 0.2,
                            "response_mime_type": "application/json",
                        },
                    )
                    text = (getattr(response, "text", "") or "").strip()
                    if not text:
                        LOGGER.warning("Legacy Gemini SDK returned empty text response.")
                        return None
                    return self._parse_json_from_text(text)
                except ImportError:
                    LOGGER.warning(
                        "Neither google.genai nor google-generativeai is installed. "
                        "Install `google-genai` or set GEMINI_API_URL for HTTP mode."
                    )
                    return None
                except Exception as exc:
                    self._handle_gemini_failure(exc)
                    return None
            except Exception:
                self._handle_gemini_failure()
                return None

        # Compatibility path: custom HTTP endpoint with bearer token
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        body = {"prompt": prompt, "max_output_tokens": 256}
        try:
            resp = requests.post(api_url, headers=headers, json=body, timeout=timeout)
            resp.raise_for_status()
            return self._parse_json_from_text(resp.text.strip())
        except Exception:
            self._handle_gemini_failure()
            return None

    def _handle_gemini_failure(self, exc: Exception | None = None) -> None:
        message = ""
        if exc is not None:
            message = str(exc)

        # Detect quota / resource exhausted errors and respect suggested retry delay.
        is_quota_error = "RESOURCE_EXHAUSTED" in message or "quota" in message.lower() or "429" in message
        if is_quota_error:
            retry_seconds = self._extract_retry_seconds(message)
            # Apply a minimum backoff to avoid repeated token burn and noisy logs.
            retry_seconds = max(60, retry_seconds)
            self.gemini_retry_after_epoch = time.time() + retry_seconds
            LOGGER.warning(
                "Gemini quota/backoff triggered; disabling Gemini labeling for %ds. "
                "Use --disable-auto-labeling to suppress all Gemini calls while testing.",
                retry_seconds,
            )
            return

        if exc is not None:
            LOGGER.exception("Gemini SDK/API request failed")
        else:
            LOGGER.exception("Gemini SDK/API request failed")

    def _extract_retry_seconds(self, error_text: str) -> int:
        if not error_text:
            return 60
        # Examples: "Please retry in 45.525465468s." or "retry_delay { seconds: 45 }"
        match = re.search(r"retry in\s+([0-9]+(?:\.[0-9]+)?)s", error_text, flags=re.IGNORECASE)
        if match:
            try:
                return int(float(match.group(1)))
            except Exception:
                pass
        match = re.search(r"seconds:\s*([0-9]+)", error_text)
        if match:
            try:
                return int(match.group(1))
            except Exception:
                pass
        return 60

    def _parse_json_from_text(self, text: str) -> Any | None:
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

    def _parse_gemini_cluster_labels(self, parsed: Any) -> dict[int, str]:
        out: dict[int, str] = {}
        if isinstance(parsed, dict) and "predictions" in parsed:
            parsed = parsed["predictions"]

        if not isinstance(parsed, list):
            LOGGER.warning("Unexpected Gemini response structure: %s", type(parsed))
            return out

        for item in parsed:
            if not isinstance(item, dict):
                continue
            try:
                cid = int(item.get("cluster_id"))
            except Exception:
                continue
            topic = str(item.get("topic") or item.get("label") or "").strip()
            if topic:
                # Keep only first 5 words to enforce UI-compatible compact topics.
                topic = " ".join(topic.split()[:5])
                out[cid] = topic
        return out

    def _build_gemini_cache_key(self, model_name: str, cache_clusters: list[dict[str, Any]]) -> str:
        canonical = json.dumps(
            {
                "model": model_name,
                "clusters": sorted(cache_clusters, key=lambda item: int(item.get("cluster_id", -1))),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        return hashlib.sha1(canonical.encode("utf-8")).hexdigest()

    def _load_gemini_cache(self) -> dict[str, Any]:
        if not self.gemini_cache_path.exists():
            return {}
        try:
            with self.gemini_cache_path.open("r", encoding="utf-8") as source_file:
                data = json.load(source_file)
            if isinstance(data, dict):
                return data
        except Exception:
            LOGGER.exception("Failed to load Gemini label cache from %s", self.gemini_cache_path)
        return {}

    def _save_gemini_cache(self) -> None:
        try:
            self.gemini_cache_path.parent.mkdir(parents=True, exist_ok=True)
            with self.gemini_cache_path.open("w", encoding="utf-8") as target_file:
                json.dump(self.gemini_cache, target_file, ensure_ascii=False, indent=2)
        except Exception:
            LOGGER.exception("Failed to save Gemini label cache to %s", self.gemini_cache_path)

    def _get_cached_gemini_labels(self, cache_key: str) -> dict[int, str] | None:
        with self.gemini_cache_lock:
            entry = self.gemini_cache.get(cache_key)
        if not isinstance(entry, list):
            return None
        out: dict[int, str] = {}
        for item in entry:
            if not isinstance(item, dict):
                continue
            try:
                cid = int(item.get("cluster_id"))
                topic = str(item.get("topic") or item.get("label") or "").strip()
                if topic:
                    out[cid] = " ".join(topic.split()[:5])
            except Exception:
                continue
        if out:
            LOGGER.info("Gemini label cache hit (%s).", cache_key[:10])
            return out
        return None

    def _set_cached_gemini_labels(self, cache_key: str, labels: dict[int, str]) -> None:
        serializable = [
            {"cluster_id": int(cid), "topic": " ".join(str(topic).split()[:5])}
            for cid, topic in sorted(labels.items(), key=lambda item: item[0])
        ]
        with self.gemini_cache_lock:
            self.gemini_cache[cache_key] = serializable
            self._save_gemini_cache()


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
        default=DEFAULT_LOCAL_MAP_SIZE,
        help="Number of FAISS candidates to project into the query-specific local map (max 100).",
    )
    parser.add_argument(
        "--local-cluster-count",
        type=int,
        default=12,
        help="Number of agglomerative clusters for the local map.",
    )
    parser.add_argument(
        "--disable-auto-labeling",
        action="store_true",
        help="Disable Gemini-based automatic cluster labeling (uses TF-IDF labels only).",
    )
    parser.add_argument(
        "--gemini-model",
        type=str,
        default=DEFAULT_GEMINI_MODEL,
        help="Gemini model name used for AI Studio labeling (e.g. gemini-2.0-flash-lite).",
    )
    parser.add_argument(
        "--gemini-cache-path",
        type=Path,
        default=DEFAULT_GEMINI_CACHE_PATH,
        help="Path to JSON cache file for Gemini cluster labels.",
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
    if args.local_map_size > MAX_SEARCH_ARTICLES:
        LOGGER.info("Capping --local-map-size from %d to %d.", args.local_map_size, MAX_SEARCH_ARTICLES)
        args.local_map_size = MAX_SEARCH_ARTICLES
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
        enable_auto_labeling=not args.disable_auto_labeling,
        gemini_model=args.gemini_model,
        gemini_cache_path=args.gemini_cache_path,
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
