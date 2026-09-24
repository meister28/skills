# Completed task history

This is the durable record of completed work. Active work stays in
[TASKS.md](./TASKS.md). Preserve the evidence and decisions that were true
when a task landed; do not rewrite an old result to match today's code or
test counts.

## Record schema

Copy the task's identity and decision fields from TASKS, then replace its
open Status with completion fields. Every new completed record has:

- **Title and ID** — the heading used in the queue.
- **Trigger** — the request, defect, review finding, or other reason for work.
- **Approval** — who approved which scope and when; cite a direct owner
  request or both the proposal and later approval.
- **Recommended worker** — the proposed role and why it was recommended.
- **Type** — one primary type from the list below.
- **Summary** — one to three sentences describing the result.
- **Implementor** — who actually performed the work; this may differ from
  the recommendation.
- **Created** — when the task entered the queue.
- **Acceptance** — the original done conditions and whether each was met.
- **Completed by** and **Completed at** — the contributor and a dated time
  with timezone when available.
- **Verification** — commands, real-surface checks, or other evidence with
  results, plus what was not exercised.
- **Changed paths** — the code, documents, or configuration changed.
- **Remaining uncertainty** — open risks, follow-up checks, or `None`.

Write fields as bold lines (`**Field:** value`) so readers can scan records.
Use the same identity and completion time in the final changelog entry.
Older records may keep their historical format; do not fabricate missing
fields during a migration.

### Choose a type

| Type | Use when the work primarily... |
| --- | --- |
| `bug fix` | repairs behavior that violated an existing contract. |
| `feature` | adds or changes a user-facing capability or behavior. |
| `refactor` | changes structure while preserving behavior. |
| `instrument` | adds or changes reusable verification tooling. |
| `playtest` | explores the real product to find problems; the probe may be temporary. |
| `audit` | examines existing work and renders findings without implementing them. |
| `design` | decides how a bounded change should work before implementation. |
| `architecture review` | examines system boundaries and structural choices. |
| `plan` | chooses scope, sequence, or priorities before implementation. |
| `consultation` | answers a decision question without making a change. |
| `docs` | changes documentation or process records only. |
| `infrastructure` | changes how the project runs, builds, or deploys. |

A project may define an additional type in AGENTS-PROJECT.md when none of
these fits. Keep its meaning and required evidence explicit. A review that
also implements a fix should normally produce separate records: the review
and the approved change have different acceptance conditions.

### Record details by type

Add the detail block appropriate to the type. State `Unconfirmed` with the
evidence when a cause or verdict is not established; silence would make the
record look more certain than it is.

- **Bug fix:** Root cause, Fix, Evidence, and Regression risk. Describe what
  failed for the user and the test or observation that distinguishes the
  cause from a guess.
- **Feature or refactor:** Design, What changed, and Evidence. For a
  refactor, explain how preserved behavior was checked.
- **Instrument or playtest:** Method, What landed, and Evidence. Distinguish
  a committed repeatable instrument from a one-off exploratory probe.
- **Audit or consultation:** Method, Findings, Verdict, and Recommendation.
  Say what was inspected and what remained outside the review.
- **Design, architecture review, or plan:** Decisions, Alternatives, and
  Recommendation or next step. Link the resulting specification if one exists.
- **Docs:** What changed and Syncs. Name other documents checked for
  consistency.
- **Infrastructure:** Change, Verification, and Rollback or recovery path.

## Completed

No completed tasks yet. Prepend completed records here, newest first. The
shape below is a copyable starting point; add the type-specific detail block
above before calling a record complete.

```markdown
### <ID> — <task title>

**Trigger:** <request or finding>
**Approval:** <who approved which scope and when>
**Recommended worker:** <role and reason>
**Type:** <one primary type>
**Summary:** <what actually happened>
**Implementor:** <actual contributor>
**Created:** <YYYY-MM-DD>
**Acceptance:** <criteria and results>
**Completed by:** <contributor>
**Completed at:** <YYYY-MM-DD HH:MM timezone>
**Verification:** <commands or observations, results, and limits>
**Changed paths:** <files or areas changed>
**Remaining uncertainty:** <open issue or None>
```

For a `bug fix`, for example, add separate **Root cause**, **Fix**,
**Evidence**, and **Regression risk** lines below the core record. Use the
matching detail block above for other types.
