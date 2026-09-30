# Decision-exercise inputs

These are the neutral case inputs used for the 2026-09-30 pilot, not a runnable
application fixture. Each suite was sent to a fresh agent context with only its
assigned guidance files. Agents were instructed to give concrete actions and
record fields, make no edits or dispatches, read no expected outcomes, and claim
no executed application checks. Cases within a suite shared one agent context.

## Workflow suite

Guidance: TEAM.md, AGENTS.md and team-TASKS.md from `skills/team-workflow/files/`.
The baseline used HEAD content; the candidate used local edited content.

| Case | Request and supplied situation |
| --- | --- |
| A | Continue. Established engineer; Architect actively owns Current P-1 at abc. Ready P-2 is approved for engineer but depends on P-1 contract. Ready P-3 is approved independent typo fix. |
| B | Approve P-4 for engineer, but only update handoff today. P-4 is Suggested feature. |
| C | Review backlog. Suggested P-5 has good feature spec. |
| D | Continue available work. Owner holds P-6 layout decision; approved P-7 schema repair is assigned to you and independent. |
| E | Finish and clean queue. Assigned P-8 implemented; SQLite service checks pass; Acceptance requires authenticated wrapper write/reload; credentials unavailable. |
| F | Requested doc correction, doc checks pass; another checkout has failing tests during active refactor. |
| G | Record release acceptance. abc has old GO; def changes production auth wrapper; no wrapper test ran. |
| H | Capture local lesson only. Canonical hub changed; installed copy is older. |

## Technical suite

Baseline guidance: original exported web-app-engineering/SKILL.md and applicable
references. Candidate guidance: corresponding files in this pilot directory.

| Case | Request and supplied situation |
| --- | --- |
| A | Improve empty-column drag. Disposable synthetic prototype; deliberate reset; no server. |
| B | Change Save label to Keep. Approved tiny edit; cloud backend and drag engine exist. |
| C | Review state refactor readiness. Reducer generates IDs with Date.now; no-op saves fresh snapshot; fake storage rejects promise while real storage throws synchronously. |
| D | Review import. Current export v4; only hand-written v2 tests; historical createdAt instant is now date key. |
| E | Accept production wiring. Build exit zero; empty emitted route manifest; separate temporary HTTP auth/write harness passes. |
| F | Fix race. Revision read before BEGIN IMMEDIATE; fake tests pass; DB supports atomic conditional UPDATE, affected-row count and rollback. Contract: one winner and one conflict for same revision. Choose minimal mechanism and proof. |
| G | Review retries. Lost response; caller retains and mutates nested payload; old response arrives after sign-out. |
