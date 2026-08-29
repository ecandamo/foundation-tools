I'm starting a new script/tool called [NAME].

Read AGENTS.md and CLAUDE.md for all project rules.
Skills are mirrored in three places for different tools — same content,
different path: .claude/skills/ (Claude Code), .cursor/skills/ (Cursor),
.agents/skills/ (everything else, e.g. Codex). If you're Claude Code, use
your native Skill tool — it already lists what's available from
.claude/skills/, don't read the folder manually. If you're Cursor or another
agent without that native mechanism, read skill files directly from
.cursor/skills/ or .agents/skills/ respectively.

## Code Rules
- Copy scripts/example_script.py as the starting point for a new script
- Keep scripts small and single-purpose
- Add comments explaining what each script does
- Take inputs via argparse (CLI flags) rather than hardcoding values at the top of the file
- Save all outputs to outputs/ — prefix filenames with the script name (or use a subfolder per script) to avoid collisions
- Use a virtual environment for Python (venv/), never commit it
- Add type hints to all Python functions
- No unnecessary dependencies — check utils/ before writing a new helper
- Tests aren't expected by default for one-off scripts — add them only for reusable logic in utils/

## Housekeeping (do this first)
- Update `README.md` if the project's purpose diverges from the template description

## What to Build
[DESCRIPTION]

## Deliverable Before Coding
Generate a Plan covering:
- Folder structure (where new scripts/helpers go under scripts/, notebooks/, and utils/)
- Inputs and outputs (what reads from inputs/, what gets written to outputs/)
- Key functions/modules
- Implementation order
- Which skills are most relevant to this build (e.g. python-error-handling,
  python-anti-patterns, systematic-debugging, bash-defensive-patterns,
  async-python-patterns)

Wait for my approval before writing any code.
