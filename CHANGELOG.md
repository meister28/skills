# Change log

Repository changes. Publication and installed-copy adoption are separate
actions.

## 2026-09-30

### Changed

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
