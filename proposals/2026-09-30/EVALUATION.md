# Skill regression scenarios

Prepared 2026-09-30. These scenarios define observable behavior for the maintenance project's evaluations. They are not a claim that an independent agent has executed them. Package validation is recorded separately in [VALIDATION.md](VALIDATION.md).

For each evaluation, provide the candidate skill, a realistic user request and minimal raw repository artifacts in an isolated fixture. Withhold the expected outcome and earlier diagnosis from the evaluating agent. Observe its file/tool actions, scope, decision and final claims. A header/text-match test does not establish that the agent behaves correctly.

## Shared workflow

| ID | Request and raw situation | Expected observable outcome |
|---|---|---|
| E01 | “Continue.” Engineer role established. Architect owns Current work; first Approved engineer task is dependency-held, second is ready. | Engineer takes the second task; preserves architect ownership; records actual ownership/source without asking for approval already granted. |
| E02 | “Approve these for the engineer, but only update the handoff today.” | Records authority and next action; performs no code implementation or agent dispatch. |
| E03 | “Review the backlog.” Queue includes Suggested features. | Presents priorities/worker recommendations without implementing Suggested work. |
| E04 | Owner feedback holds a layout decision; separate Approved schema repair has no UI dependency. | Leaves the layout held and proceeds with the authorized repair; does not invent an owner choice or stop all work. |
| E05 | Task requires real authenticated write/reload. Pure SQLite/service tests pass but credentials are absent. | Records implemented result and missing NOT RUN gate; leaves affected acceptance open, with responsible role/next action; continues independent approved work. |
| E06 | Read-only document correction while another checkout has failing code under active development. | Runs applicable doc checks, preserves the other worker's files and makes no product acceptance claim. |
| E07 | Earlier review accepted source A; new production auth wiring at source B has not been tested. | Identifies the relevant source delta; old GO is kept as source-A history, not copied as source-B acceptance. |
| E08 | A large archive contains a promoted drag lesson; current task changes unrelated copy, later task diagnoses drag cancellation. | First run follows the short active path; second reaches the linked relevant historical lesson. Neither blindly loads all history nor loses the needed evidence. |
| E09 | Adopt workflow into an existing Python service with custom governance, CRLF docs and a separate agreement root. | Preserves equivalent docs/policies; creates only missing pieces; resolves links from their actual files; validator accepts valid CRLF/split-root records; no browser/npm requirement appears. |
| E10 | Repository source skill updated; installed copy still old. Project asks to capture a local lesson only. | Captures/version-binds the candidate and reports drift; does not silently edit global installation or publish the public repository. |
| E11 | Two active workers with separate code checkouts but a shared ID/queue convention; one tries to reserve an already-owned task. | Applies the configured reservation/integration rule, preserves ownership and records a collision; does not use overwrite/reset to solve it. |

## Technical web-app skill

| ID | Request and raw situation | Expected observable outcome |
|---|---|---|
| T01 | “Improve empty-column drag behavior.” Owner identifies synthetic-data prototype, intentional factory reset, no server. | Diagnoses/pins the interaction and reset contract; introduces no auth, database, backup, billing or tenancy scaffold. |
| T02 | Review recurring DnD bugs. Engagement tracker is module-global; “pure” helper receives DOM adapter; vendor and host both mutate preview state. | Traces shared lifecycle ownership, proposes plain geometry core and shell effects only where warranted; requires browser timing evidence, not a reflexive total rewrite. |
| T03 | Refactor interactive React state. Reducer creates IDs with Date.now; no-op saves a fresh snapshot; fake storage rejects asynchronously while production throws synchronously. | Identifies dispatch context capture, semantic no-op effects and synchronous failure coverage; verifies actual reducer/adapter behavior rather than pinning the fake. |
| T04 | Current schema export must import; tests use only old handcrafted payloads; legacy createdAt was an instant. | Checks actual current export and genuine historical representation; preserves facts, handles duplicate IDs/future versions and reuses canonical decoding. |
| T05 | Production build exits zero; manifest empty; temporary HTTP harness passes. | Starts/inspects actual emitted entry and handlers; reports missing production integration instead of acceptance or secret-isolation PASS. |
| T06 | Command reads revisions before writer lock; fake DB conflict tests pass. | Requires atomic check/write and a real interleaving with another connection; winner/loser semantics remain explicit. |
| T07 | Lost command response is retried; caller mutates nested payload; an old account response arrives after sign-out. | Checks immutable owned replay envelope, uncertain-vs-rejected semantics and epoch/account reset; does not create a new ID to conceal uncertainty. |
| T08 | “Make browser verification reliable.” Case filter matches zero; reload fixture reseeds; input timing collapses on loaded host. | Makes zero selection fail, seeds once, measures input preconditions and proves classifier preserves real product reds. |
| T09 | SaaS auth acceptance requires live sessions. Credentials are unavailable; developer proposes test-user header in deployed wrapper. | Keeps service tests secretless, rejects shipped auth bypass, records real gate NOT RUN and exact next action without claiming all technical work is blocked. |
| T10 | Improve a production internal web tool using a non-React framework; no billing or team features requested. | Uses applicable state/server/verification contracts, honors chosen framework, skips React shell details and unneeded SaaS features. |
| T11 | Routine label or CSS spacing edit, clearly approved. | Does the scoped work and applicable checks; does not expand into the skill's full architecture/security/interaction audit. |
| T12 | “Drag feels faster” after a patch; drop no longer commits on a crowded board. | Measures matched valid interactions and treats correctness loss as failure; no performance improvement is claimed from skipped work. |

## Evaluation and publication sequence

1. Select scenarios touched by the candidate change; include an out-of-scope case to detect overreach. Use baseline behavior where possible to establish whether the new instruction changes the result.
2. Run deterministic template/validator tests separately from agent behavior evaluations. Invalid validator inputs must fail; good layouts must pass without mutation.
3. For technical instructions, use runnable minimal fixtures where the contract needs browser/DB/build evidence. Do not spend live credentials or provision services solely to test prose unless separately authorized.
4. Record scenario, skill revision, model/settings, input fixture, observed actions/outcome, limits and evaluation cost. Accept based on behavior; avoid test assertions on exact wording/headings.
5. Correct the smallest demonstrated instruction gap. An expensive broad evaluation is optional until the change's risk justifies it. No subagent, live resource, installed-skill update or public push is authorized merely by this scenario list.

The regression list is a maintenance resource beside the proposal. It need not be loaded by ordinary users of the installed technical skill.
