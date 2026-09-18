# ${PROJECT_NAME} — task queue

The active backlog and handoff. One entry per task, next unused `P-NNN` id.
Entries are grouped into categories and placed within each category by
**recommended implementation order**, not by ID. Completed records move to
[`TASK-HISTORY.md`](./TASK-HISTORY.md) — read it only when investigating a
past task, its decision, or its verification.

## Current work

### P-001 — <task title> *(Category tag)*

- Approval: **Owner request, YYYY-MM-DD** — <the owner's words, or the
  review/decision that produced it>.
- Recommended worker: **<CTO / Software Architect | Implementor / Software Engineer>** —
  <one-line reason; architect tasks prefer a frontier model, implementor
  tasks a cost-efficient one (TEAM.md)>.
- Status: **In progress** — <the exact next step, kept accurate, so any
  agent can resume cold>.
- <Problem / contract / acceptance criteria — what done means, measurably.>

## Ready — approved, in recommended implementation order

*(empty — approved tasks land here in the order they should be implemented)*

## Suggested — awaiting owner approval, in recommended order

*(empty — agent-proposed tasks enter here; rule: Suggested must not be
implemented until the owner approves)*

## Deferred

*(empty — parked tasks with the blocking constraint stated in the Status
line, e.g. "after P-00X lands", so nobody picks them up out of order)*

---

Adding or finishing a task: place new entries **within their category by
recommended order**, not at the end by ID. Required fields: Approval, Status,
Recommended worker (with reason), acceptance criteria. A task missing any
field is incomplete.
