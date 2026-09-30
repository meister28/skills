# Shared working agreement

Read this agreement, [team/TASKS.md](./team/TASKS.md), and
[TEAM-PROJECT.md](./TEAM-PROJECT.md) when starting or continuing work.
The queue contains current work; completed records live in
[team/TASK-HISTORY.md](./team/TASK-HISTORY.md) for relevant lookups.

## Roles

- The owner decides priorities and approves work.
- The default CTO/architect role analyzes the product, investigates difficult
  problems, makes architectural recommendations, writes plans/specifications,
  and may implement when the owner asks.
- The default senior-engineer role implements approved work, verifies it, and
  reports results. The owner may also ask this agent to analyze, plan, or make
  a direct change.
- The task backlog belongs to the project. Write tasks neutrally; do not frame
  them as instructions from one AI agent to another.

These are defaults, not restrictions. The owner's latest direct instruction
determines the work.

## Approval rule

Every backlog item has an `Approval` field:

- `Suggested` — an idea or recommendation. It may be analyzed or discussed,
  but it must not be implemented.
- `Approved` — the owner confirmed it or directly requested it. It may be
  implemented.

For new or updated cards, start Approval with `Suggested` or `Approved`,
then name the source and scope. Ready and Current work require approval;
Suggested belongs in Suggested or Deferred. Older approval wording need
not be rewritten merely to adopt this convention.

A task written by an agent starts as `Suggested`. A direct user request is
approval for that exact scope, even if the task was not already in the
backlog. Add or update the entry so the next agent can see it. Do not expand
approval beyond the user's request.

## Worker recommendation

Every task has a `Recommended worker` field with a short reason:

- `CTO / Software Architect` — use for complex analysis, architecture, product
  or UX decisions, difficult debugging, high-risk changes, and work where
  deep architectural judgment materially improves the result. **Prefer a
  frontier model for this role** — the judgment calls are the reason the
  role exists, and this is where the extra cost pays for itself.
- `Implementor / Software Engineer` — use for routine, well-specified
  implementation, straightforward fixes, tests, documentation
  synchronization, and repetitive work. **A cost-efficient model is usually
  the right choice here** — the task is well-specified and the spec, not
  the model, carries the judgment.

When discussing or proposing a new task, recommend one of these workers to the
owner and record the same recommendation in team/TASKS.md. For work that should be
designed by the CTO/architect and then implemented by the implementor, say so
explicitly. The model preference travels with the role: architect tasks
prefer a frontier model, implementor tasks suit a cost-efficient one. The
recommendation is advice, not approval or assignment. The owner may give the
work to either agent, and the owner's direct instruction always wins.

## Choosing work

1. Follow the owner's latest direct instruction within its scope, even if it
   is not yet in the queue. Record non-trivial work there for the next agent.
2. When asked to work from the queue, continue your assigned Current work
   only if its approval, prerequisites and scope allow the next action.
   Preserve another worker's ownership. Otherwise take the first eligible
   Approved item suited to your established role in recommended order;
   skip held dependencies and record why. The model alone does not establish
   a role. If no role is established and routing changes the choice, clarify it.
3. When asked to review the backlog, present Approved and Suggested items
   with their worker recommendations. An agent proposal remains Suggested
   until the owner approves it.

## Work and handoff

Inspect Git status at session start. Read this agreement, the active queue,
[AGENTS.md](./AGENTS.md), [AGENTS-PROJECT.md](./AGENTS-PROJECT.md), and
[team/LESSONS.md](./team/LESSONS.md); then open only the relevant spec and
source files. Use older changelog and task-history entries when investigating
a related decision. Implementor names the actual worker and role, distinct
from Recommended worker. Keep Current work's base commit, progress and next
action in Status or its linked evidence. For blocked or review-ready work,
name the responsible role, prerequisite (or none), exact next action and
evidence link. A held task leaves independent approved work available. The
owner should not have to relay technical handoffs between agents.

## Working discipline

**Stop and re-plan immediately when something goes sideways.** If
verification fails twice on the same approach, the fix feels hacky, or the
change is growing beyond its approved scope — STOP. Re-diagnose (or hand the
evidence to the other role) before pushing on; grinding through a broken
approach costs more than the re-plan. "Same approach" means the same
diagnosis, not merely the same test name. Record the pivot and evidence in
the task's progress notes so the next agent does not repeat a dead end.
An intentional failing test before its fix is normal test-first development,
not a failed attempt at the same diagnosis.

**The implementor's elegance checkpoint:** before reporting done, ask
"knowing everything I know now, is this the elegant solution?" If the fix
feels hacky, pause and say so — propose the cleaner shape to the owner or
architect instead of shipping a hack under a green test suite. A simple fix
can answer the question quickly; a concern calls for a clearer proposal or
a re-plan. Do not silently add an adjacent improvement. A recurring pattern
also becomes a line in team/LESSONS.md.

**Self-improvement loop:** after any correction from the owner, a review,
or a failed verification, write the pattern and its one-line prevention rule
into team/LESSONS.md in the same session, and read that file at session
start. After repeated hits or one expensive failure, the architect proposes
a lasting rule and the owner decides whether to adopt it. Reusable
coordination rules go in AGENTS.md; stack, product, and tool rules go in
AGENTS-PROJECT.md. The lesson remains as history.

## Before finishing

1. Run the checks specified for the changed surface in AGENTS-PROJECT.md.
   Record PASS / FAIL / NOT RUN, tested source, command and working directory,
   with linked evidence and material limits. Record runtime/fixture details
   where they affect interpretation; trivial doc edits need only relevant checks.
2. Update affected specs and add a user- or maintainer-facing CHANGELOG entry
   in the same commit.
3. Archive only when Acceptance is met: approval, implementation and accepted
   behavior are distinct. A required NOT RUN or failed gate keeps that task
   open with its next action; other approved work can continue. Evidence from
   one source or harness accepts only the boundary it exercised. Preserve old
   acceptance as dated history; if disproved, reopen the affected work under
   a new unique task ID linked to the correction and original record.
   Move a completed task to team/TASK-HISTORY.md with its result, evidence,
   changed paths, remaining uncertainty, Completed by, and Completed at.
   Leave unfinished work in TASKS.md with an honest next step.
4. Commit only your work and restore any local state changed for testing.
