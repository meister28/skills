# Approved skill update — 2026-10-01

The owner approved publication of the shared-skill proposal clarification and
requested reliable time-based test guidance in the existing technical skill.

## Changes

- team-workflow's entry point and distributed lessons template explicitly
  separate portable improvement proposals from approved changes to the shared
  skill and its global installation.
- The maintained web-app-engineering pilot covers controlled/live clocks,
  consistent fixtures and expectations, relevant time-zone/calendar boundaries,
  deliberate rollover checks and conditional guards. Its entry point routes
  time-sensitive test fixtures to the verification reference.
- Clock guidance is confined to technical instructions. The technical package
  remains a pilot and is not promoted into the released skills directory.

## Verification

From the repository root:

- `python -B -m unittest discover -s skills/team-workflow/tests -v`: PASS,
  all 13 existing validator tests.
- `python -B proposals/2026-09-30/pilot/check_package.py`: PASS, limited
  scalar frontmatter, local document links, whitespace and fresh strict
  adoption with no mutations. Expected warning: project commands unconfigured.
- `git diff --check`: PASS. Reviewed the skill diff for separation of technical
  and coordination rules.

Checks establish packaging and structural behavior, not an agent behavior
evaluation or an application's acceptance. No installed skills or consumer
agreements were changed by this update.

Completed by Atlas [Codex; model=GPT-6.1 Sol; thinking=Medium; id=A01] on
2026-10-01 (Asia/Riyadh).
