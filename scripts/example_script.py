"""Example script — the reference pattern for this template.

Copy this file as a starting point for a new script. It demonstrates the
conventions from AGENTS.md: type hints, try/except error handling, pathlib
for paths, CLI args via argparse, and writing outputs prefixed with the
script's own name so multiple scripts never collide in outputs/.

Usage:
    python scripts/example_script.py --input data.csv
    python scripts/example_script.py --input data.csv --limit 50
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

SCRIPT_NAME = Path(__file__).stem  # "example_script" — used to prefix outputs

INPUTS_DIR = Path(__file__).resolve().parent.parent / "inputs"
OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Example script for foundation-tools.")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Filename inside inputs/ to read (e.g. data.csv).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional: only process the first N rows.",
    )
    return parser.parse_args()


def read_rows(input_path: Path, limit: int | None) -> list[dict[str, str]]:
    """Read rows from a CSV file. Raises FileNotFoundError if missing."""
    if not input_path.exists():
        raise FileNotFoundError(f"Expected input file at {input_path}")

    with input_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    return rows[:limit] if limit else rows


def process_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Placeholder transform — replace with real logic."""
    return rows


def write_output(rows: list[dict[str, str]]) -> Path:
    """Write results to outputs/, prefixed with this script's name to avoid
    collisions with other scripts writing to the same shared folder."""
    OUTPUTS_DIR.mkdir(exist_ok=True)
    output_path = OUTPUTS_DIR / f"{SCRIPT_NAME}_output.csv"

    if not rows:
        output_path.write_text("")
        return output_path

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    return output_path


def main() -> None:
    args = parse_args()
    input_path = INPUTS_DIR / args.input

    try:
        rows = read_rows(input_path, args.limit)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except (OSError, csv.Error) as e:
        print(f"Error reading {input_path}: {e}")
        return

    result = process_rows(rows)
    output_path = write_output(result)
    print(f"Wrote {len(result)} rows to {output_path}")


if __name__ == "__main__":
    main()
