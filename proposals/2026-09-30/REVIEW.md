# Skills hub intake review — 2026-09-30

Status: imported and reviewed; enhancement choices await the owner's decision.

## Purpose and provenance

The owner wants this repository to become a hub for personally developed skills,
improved through experience in other projects. This intake preserves the supplied
Morning Todo export, evaluates its portability, and recommends a small first
release. Importing the export does not adopt its instructions.

Eight original files were imported unchanged from `skill-evolution-2026-09-30.zip`
into this directory. The archive's `skill-evolution/` wrapper was removed.
SHA-256: `a50da1a661273e88ae5f58fab673f1dd76e5664abee28376d0df6d34e63648e4`.

The local checkout and read-only remote main check both identify
`6c074184eb79f0884d49209e0ccdcee8412938a5`, matching the proposal's public
baseline. Morning Todo source links and installed-copy claims were supplied by
the exporter; they were not independently checked against that repository or
the owner's installed skills. This review assesses the exported recommendations
against the actual skills-hub files, rather than accepting every source claim.

The `AGENTS.md` inside `skills/team-workflow/files/` is a distributed template,
not repository-root governance. The hub currently has no adopted root workflow.
This intake does not scaffold one or copy application policies into it.

## Recommendation

Adopt W02, W03, W04 and a narrow W12 as the first workflow batch, preserving W01.
Use the current task schema: improve the meaning and contents of existing fields
rather than adding a new state machine. Pair those edits with targeted validator
tests and behavior scenarios before release.

Pilot `web-app-engineering` separately. Its separation from coordination is sound;
the main entry routes readers to four technical references and avoids requiring
React, a provider, billing or tenancy. Keep it here as a candidate until its
selected scenarios demonstrate useful behavior. Publish it under
`skills/web-app-engineering/` only after that decision and verification.

For the hub itself, use this `proposals/` directory as the initial inbox. A dated
intake plus a review/decision record is enough now. A second queue, automatic
cross-project synchronization or release tooling would add maintenance before
the need has been demonstrated. A root workflow adoption can be a separate
choice if the owner wants the hub to use its own team skill.

## Workflow decisions proposed

All rows are recommendations, not approvals.

| Item | Recommendation | Reason and implementation boundary |
| --- | --- | --- |
| W01: shared/project split | Retain | Already implemented in SKILL.md and the templates. Preserve split-root routing and project extensions; do not duplicate the existing policy. |
| W02: continuation | First batch | TEAM.md currently says to continue Current work without explicitly checking ownership or dependencies. Choose the worker's eligible task, then the first approved task suited to its established role. A direct owner assignment takes precedence. Do not infer a role from the model alone. |
| W03: handoffs | First batch | Current work already requires a base commit and next step. Extend blocked/review-ready notes with responsible role, prerequisite, exact next action and linked evidence. Ownership remains distinct from worker recommendation; no dispatcher or extra handoff file is needed. |
| W04: acceptance | First batch | Existing proof rules are good but completion needs an explicit distinction from approval and implementation. Archive only when that task's contract is met. Keep source-specific evidence and reopen disproved acceptance without deleting history. |
| W05: bounded reading | Later, when needed | Queue/archive separation and newest changelog reading already exist. Active/history lesson separation can help mature projects, but adds files and migration work to new ones. Start with an optional pattern triggered by a large ledger, retaining linked historical evidence. |
| W06: concurrency | Project option | Isolation and reservation rules are valuable when concurrent workers actually exist. Define the local convention rather than imposing separate worktrees, a worker count or remote refresh on every task. The cloud environment is already isolated. |
| W07: verification tiers | Merge the essential wording into W04 | Shared rules need honest PASS/FAIL/NOT RUN limits; concrete tiers and commands belong to project policies. Environment-failure classification requires evidence and must not swallow product failures. |
| W08: evidence binding | Merge a minimal version into W03/W04 | Add tested source, command/working directory, outcome and relevant limits where material. Avoid requiring full runtime metadata for every trivial doc edit or duplicating evidence in multiple records. |
| W09: validator | Targeted first-batch support | Active/history duplicate IDs, missing fields, dates, links and split roots already have code support. Add tests for existing cross-file duplicates and CRLF, then close chosen new structural gaps. Do not regex-judge semantic authority or source acceptance. |
| W10: governance cost | Small clarification; defer measurement system | The template already defines repeated failure as the same diagnosis. Explicitly exclude intentional test-first red results. Repeated/costly failures justify considering a rule, not automatically adding permanent policy. |
| W11: Git attribution | Optional project preference | Task attribution already exists. Respect configured Git identity; do not universalize Morning Todo's trailer preference or change global Git configuration. |
| W12: source/install drift | Narrow first batch | Record canonical source and adopted commit where a project uses a copied skill. Separate capture, hub release and project adoption. Repository publication does not verify installed files; installation is separately scoped. No installation automation is required yet. |

## Concrete conflicts and cautions

1. **Status syntax:** the validator requires Current work cards to start Status
   with `Current`, Ready with `Ready`, Suggested with `Suggested`, and Deferred
   with `Deferred`. W04's example beginning `implemented; ...` would fail today.
   Preserve the section prefix, for example `Current — implemented; required
   identity check NOT RUN; reviewer next`, or explicitly design and test a schema
   migration. Do not quietly change the prose contract while leaving checks behind.
2. **Partial authority checking:** `check_records` detects an approval beginning
   `Approved` in Suggested, but not Suggested approval in Ready/Current or natural
   language approval variants. A narrow structural check needs an agreed field
   convention first. It cannot decide whether an owner actually granted authority.
3. **No universal checkout refresh:** W02 should inspect the configured source
   when needed, not add mandatory networking at every continuation. Concurrent
   work also needs mutable-resource isolation beyond Git; this is conditional.
4. **Template growth:** several improvements restate existing rules. Replace or
   clarify those passages rather than append twelve new rule sections. Keep
   technical reference detail outside routine startup documents.
5. **Installed drift is unverified here:** the export reports an older installed
   copy. This hub review does not establish the current installed version or
   authorize changing it. Preserve that distinction in release notes.

## Technical skill assessment

The five-file candidate is coherent and useful for stateful web applications.
Its strongest transferable guidance covers semantic no-ops, actual legacy data,
gesture ownership, genuine persistence failures, atomic revision checks,
immutable retries and evidence from the production request path.

Keep these boundaries:

- `team-workflow` governs ownership, approval, records and handoffs.
- `web-app-engineering` governs applicable technical investigation and proof.
- Project extensions contain framework/provider choices, commands, budgets,
  commercial decisions and owner preferences.

Before promotion, refine these points:

- Narrow the discovery description to the stateful interactions, persistence
  and integration situations where the skill helps. Its broad "design/audit"
  trigger could otherwise attract routine work; the stated exclusion helps but
  should be tested with T11.
- Distinguish database-enforced concurrency from a required application lock.
  Atomic compare-and-write can use conditional updates, constraints or suitable
  isolation; the criterion is the promised concurrent outcome. The current
  transaction/lock phrasing could encourage unnecessary locking.
- Express reload/restart, backup restore and live credential checks as gates
  for the boundary actually being claimed. The reference already conditions
  several of these; pilot whether agents still over-expand prototype work.
- Keep project recordkeeping as a reference to the project's existing process.
  Avoid growing a second coordination skill inside the technical skill.
- A package/link check is not evidence that instructions improve agent behavior.
  Do not call the candidate accepted or cheaper until observed evaluations exist.

## Proposed evaluation scope

For the first workflow batch, use E01–E04 for role/dependency and scoped authority,
E05/E07 for incomplete/source-specific acceptance, and E10 for source/install
scope. Use E06 as an overreach control. Deterministic checks should include the
chosen card syntax, Suggested authority in active sections, cross-file duplicate
IDs, CRLF, valid split roots and unchanged files after validation.

For the technical pilot, start with T01/T11 as overreach controls, T03/T04 for
state/data, T05 for production wiring and T06/T07 for concurrency/replay. Add
T02/T08/T12 when evaluating the interaction guidance with a real browser fixture.
Use T09 if credential-bound acceptance wording changes. Do not provision live
services just to validate prose. Record fixtures, revision, observed behavior,
limitations and cost; keep expected outcomes out of the test agent's input.

These scenarios are selected, not executed. No agent behavior or application
acceptance claim is made by this review.

## Checks executed in this hub

- Compared all eight imported files byte-for-byte with the archive: identical.
- Checked the original eight Markdown files: ten local links resolve, no trailing
  whitespace. External source URLs were not checked.
- Ran `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s skills/team-workflow/tests -v`
  from `/workspace/skills`: all eight tests passed.
- Parsed candidate frontmatter with the available PyYAML using safe loading and
  checked its name and description; local references were checked separately.

The export's VALIDATION.md remains an unchanged historical report from the other
environment. Its missing-PyYAML observation is not a blocker here.

## Decision and release boundary

Suggested next decision: select the first workflow batch above and whether to
pilot the technical candidate as a separate deliverable. Then prepare and verify
the exact skill/template edits for review. Promotion, commit, push and installed
copy updates have not happened. GitHub publication waits for the owner's
satisfaction with the resulting changes, as requested.
