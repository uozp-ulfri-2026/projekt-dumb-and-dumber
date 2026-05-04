from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml


YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


# ----------------------------
# TEXT CLEANING
# ----------------------------

def fix_mojibake(text: str) -> str:
    try:
        return text.encode("cp1250").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def clean_text_value(value: str) -> str:
    """
    Clean text while preserving natural language structure.
    IMPORTANT: Do NOT remove stopwords or destroy sentence structure.
    """
    value = fix_mojibake(value)

    # Remove HTML tags
    value = re.sub(r"<[^>]+>", "", value)

    # Remove URLs
    value = re.sub(r"http\S+|www\.\S+", "", value)

    # Normalize unicode
    value = unicodedata.normalize("NFKC", value)

    # Replace non-breaking spaces
    value = value.replace("\u00a0", " ")

    # Normalize whitespace
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r"\n\s*\n+", "\n\n", value)

    return value.strip()


def clean_value(value: Any, field_name: str | None = None) -> Any:
    """
    Recursively clean values but preserve structure.
    """
    if isinstance(value, str):
        if field_name == "url":
            return value
        return clean_text_value(value)

    if isinstance(value, list):
        cleaned_items = [clean_value(item, field_name) for item in value]
        return [item for item in cleaned_items if item not in (None, "", [], {})]

    if isinstance(value, dict):
        return {key: clean_value(item, key) for key, item in value.items()}

    return value


# ----------------------------
# EMBEDDING TEXT CREATION
# ----------------------------

def build_embedding_text(article: dict[str, Any]) -> str:
    """
    Build a high-quality text representation for embedding.

    Strategy:
    - title (most important)
    - lead (summary)
    - first few paragraphs (NOT all)
    """

    parts: list[str] = []

    title = article.get("title")
    if isinstance(title, str) and title:
        parts.append(title)

    lead = article.get("lead")
    if isinstance(lead, str) and lead:
        parts.append(lead)

    paragraphs = article.get("paragraphs", [])
    if isinstance(paragraphs, list):
        # Only take first 3 paragraphs (important for performance + quality)
        for paragraph in paragraphs[:3]:
            if isinstance(paragraph, str) and paragraph:
                parts.append(paragraph)

    text = "\n\n".join(parts)
    return clean_text_value(text)


# ----------------------------
# MAIN PROCESSING
# ----------------------------

def extract_yaml_to_json(input_path: Path, output_path: Path) -> None:
    print(f"Loading YAML from: {input_path}")

    with input_path.open("r", encoding="utf-8") as source_file:
        data = yaml.load(source_file, Loader=YAML_LOADER)

    if not isinstance(data, list):
        raise ValueError("Expected YAML file to contain a list of articles.")

    cleaned_records = []

    for i, record in enumerate(data):
        if not isinstance(record, dict):
            continue

        cleaned = clean_value(record)

        embedding_text = build_embedding_text(cleaned)
        if not embedding_text:
            continue  # skip empty articles

        processed = {
            "id": cleaned.get("id", i),
            "title": cleaned.get("title", ""),
            "text": embedding_text,
            "category": cleaned.get("category"),
            "date": cleaned.get("date"),
            "url": cleaned.get("url"),
        }

        cleaned_records.append(processed)

        if (i + 1) % 5000 == 0:
            print(f"Processed {i + 1} articles...")

    print(f"Saving {len(cleaned_records)} cleaned articles to: {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as target_file:
        json.dump(cleaned_records, target_file, ensure_ascii=False)

    print("Done.")


# ----------------------------
# CLI
# ----------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert MMC YAML dataset into cleaned JSON for embedding."
    )

    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("data/mmc.yaml"),
        help="Path to input YAML file",
    )

    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path("data/mmc.cleaned.json"),
        help="Path to output JSON file",
    )

    return parser


def main() -> None:
    args = build_parser().parse_args()
    extract_yaml_to_json(args.input, args.output)


if __name__ == "__main__":
    main()