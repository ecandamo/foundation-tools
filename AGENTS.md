# Foundation Tools

> **This file is the single source of truth for every agent.** Claude Code loads
> it as `CLAUDE.md` (a symlink to this file); Codex and other agents load it as
> `AGENTS.md`. Same content either way — make edits here, in `AGENTS.md`.
> If a checkout drops the symlink, recreate it: `ln -sf AGENTS.md CLAUDE.md`.

## Purpose
Lightweight starter for scripts, scraping, automation, data work, and anything non-app-development.

## Stack
- Python 3 — scraping, data processing, automation, analysis (Excel/spreadsheets included)
- Bash — file management, simple automation

## Code Rules
- Copy scripts/example_script.py as the starting point for a new script — it shows the conventions below in working code
- Keep scripts small and single-purpose
- Add comments explaining what each script does
- Take inputs via argparse (CLI flags) rather than hardcoding values at the top of the file — see example_script.py
- Save all outputs to outputs/ folder — prefix filenames with the script name (or use a subfolder per script) to avoid collisions between scripts
- Use virtual environments for Python (venv)
- Use clear readable code over clever code
- No unnecessary dependencies — check utils/ before writing a new helper
- Tests aren't expected by default for one-off scripts — add them only for reusable logic in utils/

## Python Rules
- Always use type hints
- Always handle errors with try/except
- Use pathlib for file paths, not os.path
- Virtual environment lives in venv/ — never commit it

## Folder Structure
- scripts/ — individual scripts (see example_script.py for the reference pattern)
- notebooks/ — Jupyter notebooks for exploratory analysis (clear all outputs before committing — see README)
- outputs/ — all generated files, CSVs, JSONs
- inputs/ — source files, raw data
- utils/ — shared helper functions

## Self-Improvement
- At the start of each session, review .learnings/ files for relevant context
- After solving non-obvious issues or when I correct you, log the learning to .learnings/LEARNINGS.md
- Log errors and failed commands to .learnings/ERRORS.md
- Log feature requests or missing capabilities to .learnings/FEATURE_REQUESTS.md
- Before major tasks, review recent learnings to avoid repeating past mistakes
- Periodically consolidate learnings — merge duplicates, remove outdated entries, promote broadly applicable ones to AGENTS.md

<!-- BEGIN:handoff-workflow -->
## Handoff Workflow
- Always read `HANDOFF.md` before starting meaningful work in this repository
- Use `HANDOFF.md` to understand:
  - project summary
  - current status
  - last session changes
  - files touched
  - open issues
  - next best step
  - guardrails and known decisions
- Before ending a meaningful work session, update `HANDOFF.md`
- Keep `HANDOFF.md` short, current, and practical
- Update these sections when relevant:
  - Current Status
  - Last Session Changes
  - Files Touched
  - Open Issues
  - Next Best Step
  - Known Decisions
- Do not turn `HANDOFF.md` into a long diary or changelog
- Do not duplicate the README
- Prefer concise bullet points over long paragraphs
- When in doubt:
  - preserve working logic
  - avoid unnecessary rewrites
  - follow the Next Best Step unless a blocker requires otherwise
<!-- END:handoff-workflow -->
