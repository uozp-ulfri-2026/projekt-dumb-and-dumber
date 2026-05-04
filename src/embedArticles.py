from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


LOGGER = logging.getLogger("embed_articles")


def load_articles(input_path: Path, text_field: str) -> list[dict[str, Any]]:
    LOGGER.info("Loading cleaned data from %s", input_path)
    with input_path.open("r", encoding="utf-8") as source_file:
        data = json.load(source_file)

    if not isinstance(data, list):
        raise ValueError("Expected a JSON list of article records.")

    articles: list[dict[str, Any]] = []
    for idx, record in enumerate(data):
        if idx > 0 and idx % 50000 == 0:
            LOGGER.info("Scanned %d records...", idx)

        if not isinstance(record, dict):
            continue

        text_value = record.get(text_field)
        if not isinstance(text_value, str) or not text_value.strip():
            continue

        article = {
            "id": record.get("id", idx),
            "title": record.get("title", ""),
            "url": record.get("url", ""),
            "date": record.get("date", ""),
            "text": text_value.strip(),
        }
        articles.append(article)

    if not articles:
        raise ValueError(f"No valid articles with text field '{text_field}' were found.")

    LOGGER.info("Loaded %d valid articles.", len(articles))
    return articles


def resolve_device(device: str) -> str:
    if device != "auto":
        return device

    if torch is None:
        return "cpu"

    if torch.cuda.is_available():
        return "cuda"

    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"

    return "cpu"


def embed_articles(
    articles: list[dict[str, Any]],
    model_name: str,
    batch_size: int,
    normalize_embeddings: bool,
    device: str,
) -> np.ndarray:
    LOGGER.info("Loading model '%s' on device '%s'", model_name, device)
    model = SentenceTransformer(model_name, device=device)
    texts = [article["text"] for article in articles]

    LOGGER.info(
        "Encoding %d articles (batch_size=%d, normalize=%s)",
        len(texts),
        batch_size,
        normalize_embeddings,
    )
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=normalize_embeddings,
        show_progress_bar=True,
    )

    embeddings = embeddings.astype(np.float32, copy=False)
    LOGGER.info("Embedding finished. Shape: (%d, %d)", embeddings.shape[0], embeddings.shape[1])
    return embeddings


def save_outputs(
    embeddings: np.ndarray,
    articles: list[dict[str, Any]],
    output_dir: Path,
    model_name: str,
    normalize_embeddings: bool,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    LOGGER.info("Saving outputs to %s", output_dir)

    embeddings_path = output_dir / "embeddings.npy"
    metadata_path = output_dir / "metadata.jsonl"
    config_path = output_dir / "index_config.json"

    np.save(embeddings_path, embeddings)
    LOGGER.info("Saved embeddings: %s", embeddings_path)

    with metadata_path.open("w", encoding="utf-8") as meta_file:
        for article in articles:
            metadata = {
                "id": article["id"],
                "title": article["title"],
                "url": article["url"],
                "date": article["date"],
                "text": article["text"],
            }
            meta_file.write(json.dumps(metadata, ensure_ascii=False) + "\n")
    LOGGER.info("Saved metadata: %s", metadata_path)

    config = {
        "model_name": model_name,
        "normalize_embeddings": normalize_embeddings,
        "metric": "cosine",
        "num_vectors": int(embeddings.shape[0]),
        "vector_dim": int(embeddings.shape[1]),
        "embeddings_file": embeddings_path.name,
        "metadata_file": metadata_path.name,
        "notes": "If normalize_embeddings=true, cosine similarity is equivalent to dot product.",
    }
    with config_path.open("w", encoding="utf-8") as cfg_file:
        json.dump(config, cfg_file, ensure_ascii=False, indent=2)
        cfg_file.write("\n")
    LOGGER.info("Saved config: %s", config_path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Embed cleaned MMC articles for cosine similarity search."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("data") / "mmc.cleaned.json",
        help="Path to cleaned article JSON.",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        type=Path,
        default=Path("data") / "mmc_embeddings",
        help="Directory where embeddings and metadata are written.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        help="Sentence-transformers model name.",
    )
    parser.add_argument(
        "--text-field",
        type=str,
        default="text",
        help="Field containing article text to embed.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        help="Encoding batch size.",
    )
    parser.add_argument(
        "--device",
        type=str,
        choices=["auto", "cpu", "cuda", "mps"],
        default="auto",
        help="Device for embedding. 'auto' prefers CUDA, then MPS, then CPU.",
    )
    parser.add_argument(
        "--no-normalize",
        action="store_true",
        help="Disable L2 normalization. Leave off for cosine similarity usage.",
    )
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    args = build_parser().parse_args()

    device = resolve_device(args.device)
    LOGGER.info("Using device: %s", device)

    articles = load_articles(args.input, args.text_field)
    normalize_embeddings = not args.no_normalize

    embeddings = embed_articles(
        articles=articles,
        model_name=args.model,
        batch_size=args.batch_size,
        normalize_embeddings=normalize_embeddings,
        device=device,
    )

    save_outputs(
        embeddings=embeddings,
        articles=articles,
        output_dir=args.output_dir,
        model_name=args.model,
        normalize_embeddings=normalize_embeddings,
    )

    print(f"Embedded {len(articles)} articles.")
    print(f"Saved outputs to: {args.output_dir}")


if __name__ == "__main__":
    main()