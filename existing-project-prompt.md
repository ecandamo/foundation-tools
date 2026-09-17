Read AGENTS.md for all project rules. Skills: if you're Claude Code use your
native Skill tool; otherwise read .agents/skills/ directly.

## Task
[DESCRIBE THE CHANGE OR BUG]

## Quality Standard
(AGENTS.md has the base rules; this section is what's specific to changing existing code.)
- Preserve type hints and existing error handling patterns already in the file
- Preserve existing conventions already in the file — argparse CLI args,
  output-filename prefixing to avoid collisions in outputs/ — don't quietly
  drop them while fixing something unrelated
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
