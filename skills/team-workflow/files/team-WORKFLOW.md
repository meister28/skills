# Working agreement (short version)

Full working agreement and conventions live in [`AGENTS.md`](../AGENTS.md).
This file is the quick reference agents and the owner consult day to day.

- **Task queue:** `TASKS.md` is the only routine queue. One entry per task,
  next unused `P-NNN` id. Entries are grouped into categories (Current work /
  Ready / Suggested / Deferred) and placed within their category by
  **recommended implementation order**, not by ID. Completed records move to
  `TASK-HISTORY.md`.
- **Required task fields:** Approval (who asked, when), Status,
  **Recommended worker with a reason** (e.g. the CTO/Software Architect for
  investigations with an evidence package — prefer a frontier model; the
  Implementor/Software Engineer for scoped builds — a cost-efficient model
  is usually right), outcome or acceptance criteria. A task missing any field
  is incomplete.
- **Specs:** implementation-ready specs live in `team/specs/` as
  `P-NNN-<NAME>-SPEC.md`; tasks reference them by path.
- **Audits:** triggered audits are stored as markdown in `team/audit/`
  (see AGENTS.md rule 7).
- **Lessons:** corrections become one-line prevention rules in
  `team/LESSONS.md`, written in the same session as the correction and read
  at session start; recurring lessons graduate into AGENTS.md rules.
- **Stop and re-plan:** when verification fails twice on the same approach or
  the fix feels hacky, stop and re-diagnose before pushing on (see TEAM.md).
- **Architecture reviews:** the visual HTML reports produced by the
  architecture-review pass are stored in `team/reviews/`; the temp file is
  ephemeral and the durable copy lands here. **Every candidate becomes a
  TASKS.md entry in the same session** — Suggested, with its badge strength
  and any deferral/sequencing constraints (AGENTS.md rule 8).
- **CHANGELOG:** every contributor appends an entry in the same commit as
  their change (AGENTS.md rule 1).
- **UI changes:** nothing visual ships without an owner-approved spec
  (AGENTS.md rule 6).
<!-- SLOT: stack conventions. Add one bullet for any stack-specific rule
     agents must know (e.g. "quote the app/ path on Windows", "run gates via
     npm run gate:*"). Keep it to what is true today. -->
