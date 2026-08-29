# Foundation Tools

Esteban's starter template for scripts, scraping, automation, data work, and
anything that isn't app development (that's `foundation-webapp`).

## Stack
- Python 3 — scraping, data processing, automation, analysis (Excel/spreadsheets included)
- Bash — file management, simple automation

## Getting Started
1. Create a new repo from this template
2. Clone it locally
3. Set up a Python virtual environment: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
4. Copy `scripts/example_script.py` as the starting point for your first script
5. Start building

## Folder Structure
- `scripts/` — individual scripts, one job each. `example_script.py` is the reference pattern — copy it for a new script.
- `notebooks/` — Jupyter notebooks for exploratory analysis (see Notebooks below)
- `outputs/` — all generated files, CSVs, JSONs (gitignored except `.gitkeep`)
- `inputs/` — source files, raw data (gitignored except `.gitkeep`)
- `utils/` — shared helper functions

## Formatting & Linting
- `make format` (or `black .`) — format Python files
- `make lint` (or `black --check . && ruff check .`) — lint Python files
- Config lives in `pyproject.toml` (line length, excludes for `venv/`, `outputs/`, `inputs/`)
- CI runs both checks automatically on every push (see `.github/workflows/ci.yml`)

## Notebooks
Uncomment `jupyter`, `ipykernel`, and `nbstripout` in `requirements.txt` if a
project does analysis work in Jupyter. Put notebooks in `notebooks/`.

Before committing a notebook, clear its outputs — embedded output makes diffs
unreadable and can leak data into git history. Either use `Cell > All Output >
Clear` in Jupyter, or run `make clean-notebooks` (requires `nbstripout`).

## Rules
- Copy `scripts/example_script.py` as the starting point for a new script
- Keep scripts small and single-purpose
- Add comments explaining what each script does
- Take inputs via `argparse` (CLI flags) rather than hardcoding values at the top of the file
- Save all outputs to `outputs/` — prefix filenames with the script name (or use a subfolder per script) to avoid collisions
- Use a virtual environment for Python (`venv/`, never committed)
- Add type hints to all Python functions
- No unnecessary dependencies
- Tests aren't expected by default for one-off scripts — add them only for reusable logic in `utils/`
