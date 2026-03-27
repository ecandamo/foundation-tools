# Foundation Tools — Agent Rules

## Purpose
Scripts, scraping, data automation, API integrations, and utilities. No web framework.

## Stack
- Python 3 — scraping, data, automation, analysis
- Node.js / TypeScript — API integrations, Claude API, JSON work
- Bash — file management, simple automation

## Rules
- Keep scripts small and single-purpose
- Use venv for Python dependencies
- Save all outputs to outputs/
- Comment code clearly
- No unnecessary dependencies
- Add type hints to all Python functions

## Python Rules
- Always use type hints
- Always handle errors with try/except
- Use pathlib for file paths, not os.path
- Virtual environment lives in venv/ — never commit it

## Folder Structure
- scripts/ — individual scripts
- outputs/ — generated files
- inputs/ — source data
- utils/ — shared helpers

## Self-Improvement
- Review .learnings/ at session start
- Log corrections to .learnings/LEARNINGS.md
- Log errors to .learnings/ERRORS.md
