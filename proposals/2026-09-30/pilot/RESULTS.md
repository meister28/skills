# Local first-batch checks and technical pilot — 2026-09-30

## Method and provenance

Base source: `13add46a7944eb32bca9084806039cb9c44d5c4a`.
Candidate at evaluation: uncommitted local diff recorded in DECISION.md.
The later approved workflow release is identified by the Git commit containing
this report; the technical candidate remains a proposal/pilot.
Expected outcomes from EVALUATION.md were withheld. Exact case situations and
read scope are in [INPUTS.md](INPUTS.md).

Four isolated test agents ran two suites before/after the changes:
`workflow_baseline`, `workflow_candidate`, `technical_baseline`,
`technical_candidate`. Each suite was one paper exercise containing several
cases, not independent repeated trials or real tool/file execution.
They inherited this chat's model/settings; the agent API did not expose the
resolved model identifier, token use or monetary cost. No paid external service
or credentials were used. One additional agent reviewed the local diff.

## Deterministic workflow checks

Command, from `C:\codex\skills`:
`python -B -m unittest discover -s skills/team-workflow/tests -v`.

13 tests pass. Before the validator fix, the new unassigned-Current test and
both Suggested-in-active subcases failed by assertion, demonstrating the
missing checks. Cross-file duplicates already failed validation as intended;
CRLF input already parsed correctly. Those tests preserve existing behavior.

Coverage includes valid assigned Current work with required NOT RUN acceptance,
existing approval wording, invalid active fields/status/spec, history warnings
versus strict errors, duplicates across active/history, CRLF, unchanged bytes
after validation, fenced examples, local links and separate agreement roots.
The validator cannot decide actual authority, dependencies or acceptance.

Package check, from the same working directory:
`python -B proposals/2026-09-30/pilot/check_package.py`.
It passes limited scalar frontmatter inspection for both skills, thirteen local
package/document links, whitespace checks and a fresh strict adoption with
unchanged bytes. The fresh template has one expected warning: project
verification commands are not configured. The check prints normalized-LF
SHA-256 hashes; saved output is in [CHECK-OUTPUT.txt](CHECK-OUTPUT.txt).

The official skill-creator `quick_validate.py` was attempted with both local
Python and the bundled runtime; both lack PyYAML and stopped at import. Its
full validation is NOT RUN. The dependency-free inspection above is narrower
and does not claim full YAML validation. No global dependency was installed.

An intermediate package run rejected the RESULTS link to CHECK-OUTPUT.txt
before that output existed. The output artifact was then saved and the final
run passed; this also exercised the check's missing-link failure path.

An isolated reviewer inspected the templates, validator/tests, pilot and
decision/evaluation documents against HEAD and found no actionable findings.
It independently ran all thirteen tests and confirmed the nine original intake
Markdown documents match HEAD content, accounting for Windows line endings.

## Workflow decision observations

| Cases / selected scenarios | Baseline and candidate observations |
| --- | --- |
| A / E01 | Both select independent P-3, preserving Architect ownership and skipping P-2. Candidate names role/prerequisite in Status. |
| B / E02 | Both record feature approval and handoff only, with no feature implementation or dispatch. |
| C / E03 | Both retain Suggested feature pending owner approval. |
| D / E04 | Both continue unrelated approved schema work and preserve layout hold. |
| E / E05 | Both leave acceptance open. Baseline chooses Deferred; candidate records Current with responsible role, credentials prerequisite and wrapper gate NOT RUN. Both are legal prefixes. |
| F / E06 | Both scope acceptance to docs and preserve the other worker's refactor. |
| G / E07 | Both decline to transfer abc GO to def. Candidate describes source-specific NOT RUN. Final template clarifies fresh linked IDs for reopened work; this last ID clarification was self-reviewed rather than a repeated blind trial. |
| H / E10 | Both capture the local lesson without changing installation. The prompt supplied drift; neither independently inspected installed files. |

Representative actual responses:

- Baseline A: “Take P-3, the independent approved typo fix.”
- Candidate E: “Keep P-8 open.” It records “real wrapper write/reload NOT RUN”.
- Candidate G: “Release acceptance for def is unverified”.

No selected baseline failure occurred in these paper decisions. The edits
clarify the existing contract and close observed deterministic structural gaps;
these runs do not demonstrate improved real agent reliability or lower cost.

## Technical decision observations

| Cases / selected scenarios | Baseline and candidate observations |
| --- | --- |
| A / T01 | Both keep synthetic/reset contract and call for real interaction evidence without server/recovery scaffolding. |
| B / T11 | Both keep copy change scoped and avoid auditing unrelated cloud/drag boundaries. |
| C / T03 | Both identify dispatch-time IDs, semantic no-op effects and production synchronous failure coverage. |
| D / T04 | Both require current v4 round trip and genuine historical representation; candidate explicitly preserves instant meaning pending conversion policy. |
| E / T05 | Both reject build/harness-only acceptance and require actual emitted handlers. |
| F / T06 | Both choose conditional atomic UPDATE rather than an extra application lock, and require real two-connection proof. |
| G / T07 | Both retain immutable retry identity/payload and reject stale session responses. |

Candidate F: “The database's conditional update is sufficient for the stated
winner/conflict rule; an application lock is unnecessary.” Candidate B keeps
“the project's normal checks for this tiny edit.”

All application/browser/database checks are NOT RUN. These are action choices,
not observed application outcomes. The candidate remains a pilot; package
validation and correct hypothetical answers do not meet promotion acceptance.

## Remaining limits

No no-guidance control, repeated fresh-context samples, real browser fixtures,
database interleavings, emitted production app or credentialed identity checks
were run. Discovery was prompted by explicitly supplied skill files, so the
narrower description's automatic-selection behavior is unverified. External
source URLs and copied installed versions were not checked. Historical intake
validation claims remain dated evidence, not new checks in this environment.
