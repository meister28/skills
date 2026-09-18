# Rules for every agent and developer on this project

<!-- SLOT: intro. Replace with the project's own "why these rules exist"
     story — the concrete incidents that motivated them. Rules with a real
     reason behind them get followed; rules that fell from the sky get
     quietly ignored. -->

These rules are binding for humans, AI agents, and any tooling that edits
this repository.

## 0. Read the working agreement and the backlog first

[`/TEAM.md`](./TEAM.md) holds the roles (the owner decides; the architect
analyzes and recommends; the senior engineer implements and verifies) and the
approval rule: **a backlog item marked `Suggested` must not be implemented**,
while `Approved` may be — and a direct owner request approves exactly its own
scope, nothing wider.
`${TEAM_TASKS_PATH}` is the short active backlog and handoff: take the first
`Approved` item recommended for your role (or the owner's direct
instruction), record `Current work`, and keep its next step accurate. When
done, move the full record to `${TEAM_HISTORY_PATH}` with `Completed by` /
`Completed at`. Read the archive only to investigate a past task. The owner
does not relay technical handoffs — the files do.

`${TEAM_SPECS_PATH}` is where specifications and design documents live
(`P-###-…-SPEC.md`, named for the backlog item they specify) — a task with a
spec references it from its record. Design/audit reports that back a spec
live beside it. This folder is the documentation and communication channel
between agents: write the spec there before implementation, keep it truthful
in the same commit as the change it describes (rule 2), and do not paste
spec content into chat as a substitute.

## 1. Update the change log — every change, no exceptions

**Every change that lands in the repo updates
[`CHANGELOG.md`](./CHANGELOG.md) in the same commit: features, behavior
changes, refactors, doc corrections, and bug fixes — especially bug fixes.**
"Small" is not an exemption; a bug fix that isn't logged is how the next
person reintroduces it.

How:

- Put the entry in the **newest date section** (create `## YYYY-MM-DD` right
  under the intro if today's section doesn't exist yet; dates are ISO 8601,
  newest first).
- Choose the matching subsection: `### Added`, `### Changed`, `### Fixed`.
  Doc-only corrections also go under `### Changed`.
- One bullet per user-visible change, written for a *user or a new
  maintainer*: what behaves differently now, not which functions were
  touched. Plain language over jargon.
- For bug fixes, say **what the user experienced before**, not just the
  mechanism.
- Never rewrite or delete existing entries. Append.
- The commit message does not replace the changelog entry; the changelog is
  the readable history, the commit is the patch.
- For routine work, read only the newest date section before appending. Open
  older entries only when investigating a relevant change.

Task attribution:

- Every code or documentation change still gets a changelog entry in the
  same commit, including work completed as part of a larger task.
- When a task reaches `Done` and moves to `${TEAM_HISTORY_PATH}`, its final
  changelog entry names the task ID, who completed it, and the completion
  date/time with timezone. Use a stable identity such as `Codex`,
  `Claude Code`, `Owner`, or the name the owner supplied. The task entry
  records the same identity and timestamp.
- Every task also records a `Recommended worker` and a short reason,
  following `/TEAM.md`. The recommendation routes deep architectural and
  investigative work to the CTO/Software Architect — where a frontier
  model is preferred — and routine, well-specified work to the
  Implementor/Software Engineer, where a cost-efficient model is usually
  the right choice. The model preference travels with the role; it does
  not approve or assign the task.

## 2. Keep the specs truthful in the same commit

If a change alters behavior described by the docs, update the doc in the
same commit:
<!-- SLOT: doc list. Keep only the spec docs this project actually has, e.g.
     PRODUCT-SPECS.md for product rules, ARCHITECTURE-SPECS.md for module
     responsibilities, HANDOFF.md for status/test counts, CONTEXT.md for
     vocabulary. A spec that lags the code is worse than no spec. -->

## 3. Prove it before you call it done

<!-- SLOT: verification commands. Fill with the project's real checks, e.g.
     `npm test`, `npx tsc -b`, and `npx eslint src` for a TS web app;
     `pytest` and `mypy` for Python; `cargo test` and `cargo clippy` for
     Rust. If a typechecker or linter does not exist, rewrite the rule around
     the test runner and say so honestly. Note any non-obvious trap the
     project has (e.g. a solution tsconfig that makes `tsc --noEmit` a
     no-op). For behavior-bearing changes, exercise the real surface (the
     running app, the CLI, the service) — a change that only passes unit
     tests is unverified. -->

Before reporting a change as done, the project's checks must pass — state
the commands you ran and their results.

## 4. Leave the tree as you found it

Commit only what your change touched; never sweep unrelated edits into your
commit. Restore any demo/local state you mutated while testing.

## 5. <!-- SLOT: the single-door rule -->

<!-- Replace with the project's strongest true invariant about where a
     category of change may land — e.g. "all persistence goes through
     src/lib/storage.ts" (the only module allowed to touch storage APIs,
     the only place a database swap has to land), or "all date logic lives
     in src/lib/dates.ts". Write it as: the category, the one module, why,
     and whether it is enforced by lint or only by agreement. If the project
     has no such invariant yet, either propose one as a Suggested task or
     mark this rule N/A with a one-line reason. Do not renumber the later
     rules — they cite each other by number. -->

## 6. No UI design changes without the owner's approval

Visual design — layout, sizing, spacing, colors, control arrangement,
component dimensions — changes only when the owner explicitly requests or
approves it. A bug report approves restoring the behavior the owner
describes and nothing else; it does not license adjacent "improvements". An
unrequested design change must be PROPOSED first (e.g. as a `Suggested`
item in `${TEAM_TASKS_PATH}`) and wait for approval. This rule exists
because unrequested visual changes break the owner's trust in the record:
when the UI silently differs from what they approved, they can no longer
tell which of their requests actually landed.

## 7. Audits and architecture reviews live in `team/`

Every triggered audit — the four-dimension SPEC / DESIGN / CORRECTNESS /
QUALITY grading — is written as a markdown file into
[`${TEAM_AUDIT_PATH}`](${TEAM_AUDIT_PATH}) (create the folder if missing),
named `YYYY-MM-DD-<topic>.md`. The file records the scores, the concrete
gaps per dimension, the method (what was actually exercised), and the single
most valuable next pass. Do not change production code as part of an audit;
the audit file itself is the deliverable.

Architecture-review HTML reports are kept in
[`${TEAM_REVIEWS_PATH}`](${TEAM_REVIEWS_PATH}): the producing skill writes
its report to the OS temp directory for immediate viewing, and the durable
copy is copied into that folder in the same session. A
`${TEAM_WORKFLOW_PATH}` quick reference summarizes these locations.

## 8. Architecture-review candidates become tasks

Every candidate surfaced by an architecture review is registered in
`${TEAM_TASKS_PATH}` in the same session as the review — including
candidates the review defers, sequences behind other work, or badges
"Speculative"; a recommendation strength is an input to prioritization, not
a reason to lose the record. Each entry carries the candidate's problem,
change, and acceptance criteria from the report, cites the source review
path under Approval, states the badge strength in Status, and records a
Recommended worker per rule 1. Deferral or sequencing constraints (e.g.
"after P-00X's verdict") go in the Status line so no agent picks the task
up out of order. Registration is not approval: candidates enter as
Suggested and the owner approves implementation.
