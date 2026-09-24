# Shared contributor rules

These rules bind people and agents editing this repository. Read the
[project extension](./AGENTS-PROJECT.md) before changing behavior, tests,
or documentation; it holds local commands and additional policies.

## 0. Read the working agreement and the backlog first

[TEAM.md](./TEAM.md) holds the roles (the owner decides; the architect
analyzes and recommends; the senior engineer implements and verifies) and the
approval rule: **a backlog item marked `Suggested` must not be implemented**,
while `Approved` may be — and a direct owner request approves exactly its own
scope, nothing wider.
[team/TASKS.md](./team/TASKS.md) is the short active backlog and handoff: take the first
`Approved` item recommended for your role (or the owner's direct
instruction), record `Current work`, and keep its next step accurate. When
done, move the full record to [team/TASK-HISTORY.md](./team/TASK-HISTORY.md) with `Completed by` /
`Completed at`. Read the archive only to investigate a past task. The owner
does not relay technical handoffs — the files do.

[team/specs](./team/specs/) is where specifications and design documents live
(named for the task they specify) — a task with a
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
- When a task reaches `Done` and moves to [team/TASK-HISTORY.md](./team/TASK-HISTORY.md), its final
  changelog entry names the task ID, who completed it, and the completion
  date/time with timezone. Use a stable identity such as `Codex`,
  `Claude Code`, `Owner`, or the name the owner supplied. The task entry
  records the same identity and timestamp.
- Every task also records a `Recommended worker` and a short reason,
  following TEAM.md. The recommendation routes deep architectural and
  investigative work to the CTO/Software Architect — where a frontier
  model is preferred — and routine, well-specified work to the
  Implementor/Software Engineer, where a cost-efficient model is usually
  the right choice. The model preference travels with the role; it does
  not approve or assign the task.

## 2. Keep the specs truthful in the same commit

If a change alters behavior described by the docs, update the doc in the
same commit. [AGENTS-PROJECT.md](./AGENTS-PROJECT.md) identifies this
repository's product, architecture, status, and glossary documents.

## 3. Prove it before you call it done

Before reporting a change as done, run the checks listed in
[AGENTS-PROJECT.md](./AGENTS-PROJECT.md) and state the commands and results.
For behavior-bearing changes, exercise the real product surface when unit
tests alone cannot prove the change. Record any unverified behavior honestly.

## 4. Leave the tree as you found it

Commit only what your change touched; never sweep unrelated edits into your
commit. Restore any demo/local state you mutated while testing.

## 5. Keep audits and reviews durable

Put audits in [team/audit](./team/audit/) and design, code, or architecture
reviews in [team/reviews](./team/reviews/). Record the scope, method, evidence,
concrete findings, and next action. Choose criteria appropriate to the
project; no fixed scoring model or report format is universal. When the
review is the deliverable, keep implementation work in a separate approved
task.

## 6. Turn review candidates into visible tasks

Register actionable review recommendations in [team/TASKS.md](./team/TASKS.md)
as Suggested in the same session. Each entry cites its source review,
states the problem and proposed outcome, gives acceptance criteria and a
recommended worker, and records sequencing or deferral constraints in
Status. Registration preserves the candidate; it does not approve
implementation. Record an owner-declined candidate's reason in the review
so a later agent can distinguish a settled decision from a forgotten idea.

## Project-specific policy

Put architectural boundaries, verification commands, UI approval rules,
fixture disciplines, and dated decisions in
[AGENTS-PROJECT.md](./AGENTS-PROJECT.md) only when they apply to this
repository. Keep the shared agreement independent of stack and product.
