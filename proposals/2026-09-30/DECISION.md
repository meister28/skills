# First batch decision — 2026-09-30

Authority: after the owner asked to read REVIEW.md without implementation,
the next instruction was “ok. go ahead.” This authorizes the recommended
local first batch and separate technical pilot. Publication and installation
remain review boundaries from the intake; neither was performed.

Subsequent owner decision: after reviewing the local outcome, the owner
approved committing and pushing the workflow batch to main. The technical
files publish only as proposal/pilot evidence; promotion and installed-copy
adoption remain outside this release. The Git commit containing this update
identifies the approved batch. Push completion is verified against origin/main
after publication rather than assumed by this decision record.

Base: `13add46a7944eb32bca9084806039cb9c44d5c4a`, checked out from origin/main.
The original eight imported files and REVIEW.md remain unchanged.

## Local implementation

- W01 retained: shared templates remain stack-neutral and project extensions
  retain their own policies. No root workflow was adopted for this hub.
- W02: continuation selects owned, approved, dependency-eligible work for the
  established role, then the first suitable eligible approved task.
- W03: existing Implementor and Status fields carry actual role, prerequisite,
  exact next action and evidence for blocked/review-ready handoffs.
- W04, with minimal W07/W08: archive only after Acceptance is met; record
  source-specific PASS/FAIL/NOT RUN and material limits. Reopened accepted work
  gets a fresh linked ID so historical evidence and unique IDs survive.
- W09 support: two new structural checks plus duplicate/CRLF/read-only tests.
  Approval prefixes are a convention, not proof of real human authorization;
  older natural-language records remain compatible.
- W10 clarification: an intentional test-first red is not a repeated failed
  diagnosis. No measurement system or automatic policy graduation was added.
- W12: source/path and adopted revision belong in TEAM-PROJECT.md; capture,
  hub release and installed-file verification are separate scopes.

W05, universal W06, broader W09, W10 measurement and W11 remain unadopted.
No dispatcher, automatic sync, new state machine or installation tool was added.

## Technical pilot

The original exported candidate is preserved. The refined copy is under
[pilot/web-app-engineering](pilot/web-app-engineering/SKILL.md), with its four
references. Discovery targets state, interaction and integration boundaries;
atomic database enforcement need not mean an application lock; recovery and
identity gates apply to the boundary actually being claimed.

Do not promote the pilot to `skills/web-app-engineering/` on package checks
alone. [Pilot evidence](pilot/RESULTS.md) records its limited decision exercises.
No runnable browser/database/application fixture was exercised, no independent
samples establish reliability, and no cost reduction has been demonstrated.

## Next review

Review the local diff and evaluation limits. A later approved release can
publish the workflow batch. Technical promotion needs runnable fixtures and
observed tool/file behavior for the selected contracts, rather than these
paper decisions. Installation/adoption requires its own requested scope and
comparison of actual copied files.
