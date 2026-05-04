from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml


YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

SLOVENE_STOPWORDS = {
	"in", "je", "da", "se", "na", "za", "ki", "z", "so", "ni", "ali", "pa", "kot", "tudi",
	"če", "ta", "po", "o", "bi", "ob", "le", "ter", "jo", "ga", "med", "pri", "vse", "od",
	"lahko", "do", "ko", "iz", "tem", "njen", "njegov", "njihov", "to", "tega", "tej", "teh",
	"oziroma", "v", "s", "k",
}


def fix_mojibake(text: str) -> str:
	try:
		return text.encode("cp1250").decode("utf-8")
	except (UnicodeEncodeError, UnicodeDecodeError):
		return text


def clean_text_value(value: str) -> str:
	value = fix_mojibake(value)
	value = value.lower()
	value = re.sub(r"<[^>]+>", "", value)
	value = re.sub(r"http\S+|www\.\S+", "", value)
	value = re.sub(r"^-\s+", "", value)
	value = re.sub(r"\n-\s+", " ", value)
	value = re.sub(r"[^\w\s\.\,\;\:\-\(\)]", "", value)
	value = unicodedata.normalize("NFKC", value)
	value = value.replace("\u00a0", " ")
	value = re.sub(r"[\t\r\f\v]+", " ", value)
	value = re.sub(r"\n\s*\n+", "\n\n", value)
	value = re.sub(r"[ ]{2,}", " ", value)
	value = value.strip()
	
	words = re.findall(r"\b\w+\b", value.lower())
	filtered = [w for w in words if w not in SLOVENE_STOPWORDS and len(w) > 1]
	return " ".join(filtered)


def clean_value(value: Any, field_name: str | None = None) -> Any:
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


def build_embedding_text(article: dict[str, Any]) -> str:
	sections: list[str] = []
	for field_name in ("title", "lead"):
		field_value = article.get(field_name)
		if isinstance(field_value, str) and field_value:
			sections.append(field_value)

	paragraphs = article.get("paragraphs", [])
	if isinstance(paragraphs, list):
		sections.extend(paragraph for paragraph in paragraphs if isinstance(paragraph, str) and paragraph)

	figures = article.get("figures", [])
	if isinstance(figures, list):
		for figure in figures:
			if isinstance(figure, dict):
				caption = figure.get("caption")
				if isinstance(caption, str) and caption:
					sections.append(caption)

	keywords = article.get("keywords", [])
	if isinstance(keywords, list) and keywords:
		keyword_text = ", ".join(keyword for keyword in keywords if isinstance(keyword, str) and keyword)
		if keyword_text:
			sections.append(f"Ključne besede: {keyword_text}")

	return "\n\n".join(clean_text_value(section) for section in sections if clean_text_value(section))


def extract_yaml_to_json(input_path: Path, output_path: Path) -> None:
	with input_path.open("r", encoding="utf-8") as source_file:
		data = yaml.load(source_file, Loader=YAML_LOADER)

	if not isinstance(data, list):
		raise ValueError("Expected the YAML file to contain a list of article records.")

	cleaned_records = []
	for record in data:
		if not isinstance(record, dict):
			continue
		cleaned_record = clean_value(record)
		cleaned_record["embedding_text"] = build_embedding_text(cleaned_record)
		cleaned_record.pop("gpt_keywords", None)
		cleaned_record.pop("mention", None)
		cleaned_record.pop("n_comments", None)
		cleaned_records.append(cleaned_record)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	with output_path.open("w", encoding="utf-8") as target_file:
		json.dump(cleaned_records, target_file, ensure_ascii=False, indent=2)
		target_file.write("\n")


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		description="Convert the mmc.yaml article dataset into JSON."
	)
	parser.add_argument(
		"input",
		nargs="?",
		type=Path,
		default=Path("data") / "mmc.yaml" / "mmc.yaml",
		help="Path to the source YAML file.",
	)
	parser.add_argument(
		"output",
		nargs="?",
		type=Path,
		default=Path("data") / "mmc.cleaned.json",
		help="Path to the output JSON file.",
	)
	return parser


def main() -> None:
	args = build_parser().parse_args()
	extract_yaml_to_json(args.input, args.output)


if __name__ == "__main__":
	main()
