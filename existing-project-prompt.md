Read AGENTS.md and CLAUDE.md for all project rules.
Skills are mirrored in three places for different tools — same content,
different path: .claude/skills/ (Claude Code), .cursor/skills/ (Cursor),
.agents/skills/ (everything else, e.g. Codex). If you're Claude Code, use
your native Skill tool — it already lists what's available from
.claude/skills/, don't read the folder manually. If you're Cursor or another
agent without that native mechanism, read skill files directly from
.cursor/skills/ or .agents/skills/ respectively.

## Task
[DESCRIBE THE CHANGE OR BUG]

## Quality Standard
- Keep scripts small and single-purpose — split rather than let one script
  grow multiple responsibilities
- Preserve type hints and existing error handling patterns already in the file
- Preserve existing conventions already in the file — argparse CLI args,
  output-filename prefixing to avoid collisions in outputs/ — don't quietly
  drop them while fixing something unrelated
- Use pathlib for file paths, not os.path
- Never widen scope beyond what was asked — no unrelated refactors in the
  same change
- Apply systematic-debugging for anything that isn't an obvious fix:
  reproduce → isolate → fix → verify

## Before Touching Any Code
Generate a short plan covering:
- What's actually broken/needed and why
- Which files/functions are affected
- Which skills are most relevant (e.g. python-error-handling,
  python-anti-patterns, systematic-debugging, bash-defensive-patterns,
  shellcheck-configuration)

Wait for my approval before changing anything.
