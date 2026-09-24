# Shared contributor rules

Read [TEAM.md](./TEAM.md), [team/TASKS.md](./team/TASKS.md), and
[AGENTS-PROJECT.md](./AGENTS-PROJECT.md) before changing this repository.
The project extension adds local commands and policies; it does not replace
these shared rules.

## Approval and handoff

The owner sets priorities. An agent proposal enters the queue as Suggested
and is not approved for implementation. An Approved item, or a direct owner
request, authorizes exactly its stated scope. Record current work and a
clear next step in the queue. Move completed work to
[team/TASK-HISTORY.md](./team/TASK-HISTORY.md). Read historical records only
when relevant to the task.

## Documentation

Record every landed change in [CHANGELOG.md](./CHANGELOG.md) in the same
commit. Update affected specifications and status documents in that commit.
Put task specifications in [team/specs](./team/specs/) and link them from
the task record. Keep measured claims tied to a reproducible source.

## Verification and preservation

Run the checks appropriate to the changed surface and report their results.
The project extension names actual commands and any extra gates. Check real
behavior when automated tests alone cannot establish it. Inspect Git status;
commit only work belonging to the task and restore local state changed for
testing.

## Project extensions

Maintain project-specific commands, documents, invariants, and dated
decisions in [AGENTS-PROJECT.md](./AGENTS-PROJECT.md). Change this file only
when the reusable coordination rules change.
