# Active task queue

Read [TEAM.md](../TEAM.md) for approval and handoff rules. This is the
short routine queue; completed work moves to
[TASK-HISTORY.md](./TASK-HISTORY.md). Give every task a unique project ID.
Within each section, order entries by recommended implementation order,
not by ID. Read history only when a past decision bears on the current task.

## Entry schema

Every open task records **Trigger**, **Approval**, **Recommended worker**
with a reason, **Type**, **Summary**, **Implementor**, **Created**,
**Status**, and **Acceptance**. Link a **Spec** if one exists. Use the type
definitions in TASK-HISTORY.md; a project-specific type must be defined in
AGENTS-PROJECT.md. The recommendation helps route work but does not approve
or assign it. Implementor says who is actually doing the task, or
`Unassigned` until someone takes it; Current work names the actual worker
and role. Approval starts `Approved` or `Suggested`, followed by its source
and scope, as defined in TEAM.md.

- **Current work:** an active owner with a base commit, progress, and the
  next concrete step another agent could take. Use Status and linked evidence
  for these details. Blocked/review-ready notes name the responsible role,
  prerequisite, next action and evidence; preserve the `Current` prefix.
- **Ready:** owner-approved tasks, in the order they should be attempted.
- **Suggested:** agent proposals and review candidates awaiting approval.
- **Deferred:** work parked behind a decision or prerequisite; Status names
  the condition that would unpark it.

A direct owner request approves its exact scope even if no card existed yet.
Add the card for a non-trivial task so the next agent sees the decision.
An agent-created idea starts Suggested. Recording a review candidate does
not approve its implementation.

## Current work

No current task.

## Ready

No approved queued task.

## Suggested

No proposals awaiting approval.

## Deferred

No deferred task.

## Task-card template

Copy this block into the right section and fill every required field. When
the task finishes, move it to TASK-HISTORY.md, replace Status with
Completed by / Completed at, and add verification and the detail block for
its Type. Keep the final record truthful even if the recommendation and
actual implementor differ. Archive only after Acceptance is met. Required
checks marked FAIL or NOT RUN leave the task open; an implemented result
can be recorded without calling it accepted.

```markdown
### <ID> — <title: the outcome when done>

**Trigger:** <request, defect, or linked review finding>
**Approval:** <Approved — owner request/approval with date and scope, or Suggested — source>
**Recommended worker:** <role and one-line reason>
**Type:** <bug fix | feature | refactor | instrument | playtest | audit | design | architecture review | plan | consultation | docs | infrastructure>
**Summary:** <one or two sentences: what and why>
**Implementor:** <actual worker or Unassigned>
**Created:** <YYYY-MM-DD>
**Status:** <section prefix; base/progress for Current; responsible role, prerequisite, next action and evidence for blocked/review-ready work>
**Acceptance:** <observable behavior, evidence, and records needed for done>
**Spec:** <relative path when a spec exists>
```

Audits and reviews link their durable report from any Suggested follow-up.
If the owner declines a candidate for a lasting reason, record the reason
in the report so a later review can distinguish it from forgotten work.
