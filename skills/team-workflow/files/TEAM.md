# Shared working agreement

Read [team/TASKS.md](./team/TASKS.md) for active work and
[TEAM-PROJECT.md](./TEAM-PROJECT.md) for this project's role preferences.

## Roles and approval

The owner chooses priorities and approves work. Contributors may analyze,
specify, implement, verify, and review as assigned. Recommend an Architect
for work requiring broad judgment and an Implementation engineer for
well-specified work; the recommendation is advice, not approval or assignment.

An agent-created task starts Suggested. An Approved task may be implemented.
A direct owner request approves only its stated scope and takes priority
over queue order. When asked to work from the queue, continue Current work
or take the first suitable Approved task. Surface Suggested work for the
owner to decide; do not silently implement it.

## Working and handoff

At session start, inspect Git status and read the active queue,
[AGENTS.md](./AGENTS.md), and [AGENTS-PROJECT.md](./AGENTS-PROJECT.md).
Open the relevant spec and source files. Keep Current work and its next step
accurate enough for another contributor to resume. The owner should not
have to relay technical handoffs between agents.

When verification repeatedly fails on the same diagnosis, the fix becomes
fragile, or the work grows beyond its approved scope, stop and reassess.
Record the evidence and the revised next step. Before reporting completion,
ask whether the solution is clear and maintainable; surface a concern rather
than silently adding an unapproved improvement.

Record corrections in [team/LESSONS.md](./team/LESSONS.md) while the cause is
fresh. Promote a recurring lesson to a shared rule only if it is genuinely
reusable; project-specific rules belong in AGENTS-PROJECT.md.

## Completion

Run the relevant checks and update affected docs and CHANGELOG in the same
commit. Move the finished record from TASKS to TASK-HISTORY with its result,
verification, remaining uncertainty, and who completed it and when. Leave
unfinished work in TASKS with an honest next step.
