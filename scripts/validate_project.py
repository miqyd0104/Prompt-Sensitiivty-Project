#!/usr/bin/env python3
"""Validate the repository's core research artifacts using the standard library."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / "notebooks/01_collect_llm_responses.ipynb",
    ROOT / "notebooks/02_prepare_and_clean_data_colab.ipynb",
    ROOT / "notebooks/03_comprehensive_dissertation_analysis_colab.ipynb",
    ROOT / "data/raw/pre_data_collection.xlsx",
    ROOT / "data/interim/data_collection_all_responses.xlsx",
    ROOT / "data/processed/analysis_ready_responses.csv",
    ROOT / "results/analysis_summary.json",
    ROOT / "results/tables/data_quality_summary.csv",
]


def require_paths() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_PATHS if not path.is_file()]
    if missing:
        raise SystemExit("Missing required artifacts:\n- " + "\n- ".join(missing))


def count_csv_rows(path: Path) -> int:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return sum(1 for _ in csv.reader(handle)) - 1


def validate_summary() -> None:
    summary = json.loads((ROOT / "results/analysis_summary.json").read_text(encoding="utf-8"))
    expected = {
        "rows": 2984,
        "expected_rows": 3000,
        "missing_responses": 16,
        "base_intents": 100,
        "prompts": 1000,
        "figures_created": 12,
    }
    failures = {
        key: (summary.get(key), value)
        for key, value in expected.items()
        if summary.get(key) != value
    }
    if failures:
        raise SystemExit(f"Unexpected analysis summary values: {failures}")

    figures = sorted((ROOT / "results/figures").glob("figure_*.png"))
    if len(figures) != expected["figures_created"]:
        raise SystemExit(f"Expected 12 figures, found {len(figures)}")


def validate_processed_data() -> None:
    path = ROOT / "data/processed/analysis_ready_responses.csv"
    rows = count_csv_rows(path)
    if rows != 2984:
        raise SystemExit(f"Expected 2,984 processed rows, found {rows:,}")

    with path.open(newline="", encoding="utf-8-sig") as handle:
        header = next(csv.reader(handle))
    required = {"prompt_id", "base_intent_id", "phrasing_type", "model_name", "response_text"}
    missing = sorted(required - set(header))
    if missing:
        raise SystemExit(f"Processed dataset is missing columns: {missing}")


def main() -> None:
    require_paths()
    validate_summary()
    validate_processed_data()
    print("Project validation passed: pipeline inputs, 2,984 rows, summary, and 12 figures verified.")


if __name__ == "__main__":
    main()
