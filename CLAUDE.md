# Foundation Tools

## Purpose
Lightweight starter for scripts, scraping, automation, data work, API integrations, and anything non-app-development.

## Stack
- Python 3 — scraping, data processing, automation, analysis
- Node.js / TypeScript — API integrations, JSON work, Claude API calls
- Bash — file management, simple automation

## Code Rules
- Keep scripts small and single-purpose
- Add comments explaining what each script does
- Save all outputs to outputs/ folder
- Use virtual environments for Python (venv)
- Use clear readable code over clever code
- No unnecessary dependencies
- Add type hints to all Python functions

## Python Rules
- Always use type hints
- Always handle errors with try/except
- Use pathlib for file paths, not os.path
- Virtual environment lives in venv/ — never commit it

## Folder Structure
- scripts/ — individual scripts
- outputs/ — all generated files, CSVs, JSONs
- inputs/ — source files, raw data
- utils/ — shared helper functions

## Self-Improvement
- Review .learnings/ at session start
- Log corrections to .learnings/LEARNINGS.md
- Log errors to .learnings/ERRORS.md
