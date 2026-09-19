# ${PROJECT_NAME} — shared working agreement

Read this brief agreement and `${TEAM_TASKS_PATH}` when starting or continuing
work. The owner uses one agent at a time and gives instructions directly.
`${TEAM_TASKS_PATH}` contains only current work; completed records are in
`${TEAM_HISTORY_PATH}` for on-demand lookup.

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
owner and record the same recommendation in TASKS. For work that should be
designed by the CTO/architect and then implemented by the implementor, say so
explicitly. The model preference travels with the role: architect tasks
prefer a frontier model, implementor tasks suit a cost-efficient one. The
recommendation is advice, not approval or assignment. The owner may give the
work to either agent, and the owner's direct instruction always wins.

## Working discipline

**Stop and re-plan immediately when something goes sideways.** If
verification fails twice on the same approach, the fix feels hacky, or the
change is growing beyond its approved scope — STOP. Re-diagnose (or hand the
evidence to the other role) before pushing on; grinding through a broken
approach costs more than the re-plan. Record the pivot in the task's
progress notes so the next agent doesn't repeat the dead end.

**The implementor's elegance checkpoint:** before reporting done, ask
"knowing everything I know now, is this the elegant solution?" If the fix
feels hacky, pause and say so — propose the cleaner shape to the owner or
architect instead of shipping a hack under a green test suite. Skip this for
simple, obvious fixes; don't over-engineer. A recurring hackiness pattern
also becomes a line in `team/LESSONS.md`.

**Self-improvement loop:** after any correction from the owner, a review,
or a failed verification, write the pattern and its one-line prevention rule
into `team/LESSONS.md` in the same session, and read that file at session
start. Lessons that recur graduate into numbered AGENTS.md rules.
