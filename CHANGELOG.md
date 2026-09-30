# Change log

Repository changes. Publication and installed-copy adoption are separate
actions.

## 2026-10-01

### Changed

- `team-workflow` explicitly separates portable improvement proposals from
  owner-authorized changes to the shared skill or global installation.
- The existing `web-app-engineering` pilot explains how time-sensitive fixtures,
  application clock readers and expectations share a clock, with deliberate
  rollover checks. It remains a technical pilot; no clock policy was added to
  the coordination workflow. Completed by Atlas
  [Codex; model=GPT-6.1 Sol; thinking=Medium; id=A01] on 2026-10-01
  (Asia/Riyadh); see [verification](proposals/2026-10-01/SKILL-UPDATE.md).

## 2026-09-30

### Changed

- Agents have distinct names containing tool, model, thinking level and an
  instance ID, carried through ownership, handoffs and completion records.
  Unavailable settings remain explicit; historical attribution is preserved.
- Agents ask the owner for missing name, exact model or thinking settings,
  keeping unanswered values pending and reusing confirmed session identities.
- The same team-workflow skill detects setup, existing-workflow upgrade or
  already-current validation. Upgrades preserve local policy and live records,
  compare adopted sources where available, and record a verified adoption receipt.

- README explains ownership, dependencies, acceptance and deliberate copied-skill
  updates; it distinguishes structural validation from product proof.

- Queue continuation respects actual ownership, approval, role and prerequisites.
  Blocked and review-ready handoffs identify who acts next and the evidence.
- Completed workflow tasks require their own acceptance evidence; missing gates
  stay open, and older source acceptance remains historical.
- Copied workflow adoptions record their canonical source and adopted revision
  in project configuration. Local lesson capture does not imply publication or
  installation.
- The read-only validator rejects Suggested approval in Ready/Current and
  unassigned Current work. Added coverage for CRLF and cross-file duplicate IDs.

### Added

- A separate [technical pilot](proposals/2026-09-30/pilot/web-app-engineering/SKILL.md)
  with narrower discovery and clearer atomic-write and verification boundaries.
  It remains outside the released skill directory.
- [Decision and evaluation evidence](proposals/2026-09-30/DECISION.md) for the
  local first batch. Original intake documents remain unchanged.
