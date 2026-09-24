# Active task queue

Read [TEAM.md](../TEAM.md) for approval and handoff rules. Completed work
belongs in [TASK-HISTORY.md](./TASK-HISTORY.md). Use a unique task ID chosen
by this project; order entries by recommended implementation priority.

Each entry records Trigger, Approval, Recommended worker with a reason,
Summary, Acceptance, Created, and Status. A direct owner request is an
approval for its exact scope. An agent proposal starts Suggested.

## Current work

No current task.

## Ready

No approved queued task.

## Suggested

No proposals awaiting approval.

## Deferred

No deferred task.

## Task entry format

Copy this shape into the appropriate section and fill every field:

```markdown
### <ID> - <task title>

**Trigger:** <request or finding>
**Approval:** <owner approval, or Suggested with source>
**Recommended worker:** <role and reason>
**Summary:** <what will change and why>
**Acceptance:** <observable completion criteria>
**Created:** <YYYY-MM-DD>
**Status:** <Current, Ready, Suggested, or Deferred; include next step or blocker>
**Spec:** <relative path if a spec exists>
```
