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

## Works with any agent
This template is agent-agnostic. The project rules live once in `AGENTS.md`, the
single source of truth. Each agent just reads it under the name it expects:
- **Claude Code** → `CLAUDE.md` (a symlink to `AGENTS.md`)
- **Codex / other agents** → `AGENTS.md` directly

Skills follow the same idea: the real files live in `.agents/skills/`, and
`.claude/skills/` symlinks to them so Claude Code's native Skill tool picks them
up. Edit rules in `AGENTS.md` only — never maintain parallel copies.

## Folder Structure
- `scripts/` — individual scripts, one job each. `example_script.py` is the reference pattern — copy it for a new script.
- `notebooks/` — Jupyter notebooks for exploratory analysis (see Notebooks below)
- `outputs/` — all generated files, CSVs, JSONs (gitignored except `.gitkeep`)
- `inputs/` — source files, raw data (gitignored except `.gitkeep`)
- `utils/` — shared helper functions

## Formatting & Linting
- `make format` (or `black .`) — format Python files
- `make lint` (or `black --check . && ruff check .`) — lint Python files
- Config lives in `pyproject.toml` (line length, target version, and excluded folders)
- CI runs both checks automatically on every push (see `.github/workflows/ci.yml`)

## Notebooks
Uncomment `jupyter`, `ipykernel`, and `nbstripout` in `requirements.txt` if a
project does analysis work in Jupyter. Put notebooks in `notebooks/`.

Before committing a notebook, clear its outputs — embedded output makes diffs
unreadable and can leak data into git history. Either use `Cell > All Output >
Clear` in Jupyter, or run `make clean-notebooks` (requires `nbstripout`).

## Rules
All coding rules — scripts, Python conventions, outputs, dependencies — plus the
self-improvement and handoff workflows live in `AGENTS.md`, the single source of
truth. Read it before writing code. This README intentionally doesn't restate
them, so the two can't drift.
