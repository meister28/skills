# Team workflow: cross-project improvement handoff

Prepared by Codex, CTO/architect, 2026-09-30. This is a proposal and extraction deliverable, not a change to the installed workflow or authorization to implement every proposal. The owner requested this document and the new technical skill while application implementation continues elsewhere.

## Start the maintenance project here

The verified local public checkout points to [meister28/skills](https://github.com/meister28/skills), with `skills/team-workflow/` at commit `6c074184eb79f0884d49209e0ccdcee8412938a5`. This is a locally verified baseline, not a claim about today's remote HEAD. The application repository is a different repository, `meister28/morning-todo`.

Use a clean checkout/worktree of the skills repository. Refresh its remote and compare these proposals with its current files before changing anything. Preserve unrelated edits; the inspected public checkout contains an untracked Python cache. This export deliberately lives outside the application's checkout and does not alter its queue, changelog, code, installed skills, or either Git repository.

Suggested opening instruction for the new project:

> Read TEAM-WORKFLOW-IMPROVEMENTS.md and EVALUATION.md. Compare the proposals with the current meister28/skills repository, including skills/team-workflow. Show the small recommended first batch and any conflicts with existing rules. The exported web-app-engineering folder is the candidate new skill. Do not publish or install changes until I request it; leave unapproved proposals as Suggested. Keep project-specific decisions out of shared templates.

Recommended split: architect reviews authority, dispatch, acceptance and skill boundaries; implementation engineer applies agreed wording, links, validators, packaging and test cases. The owner chooses either role. No new application task is implied by this handoff.

## Three distinct baselines

| Baseline | Observed state | Consequence |
|---|---|---|
| Installed `~/.agents/skills/team-workflow` | Older all-in-one templates; per-file confirmation during adoption; instructions to back-port changes in the same session; no bundled validator in its file inventory | Do not use this installed copy as the publication source. Updating a repository does not prove the installed copy updated. |
| Public skills checkout, `6c07418` | Shared/project split; read-only validator; direct owner request authorizes scoped adoption; audits and candidate registration already present | Preserve these advances; several items below are refinements rather than missing features. |
| Morning Todo documentation snapshot, `c48aff48cba24df66f964ff5fdab4d9b7cce0ca7` | More mature dispatch, dependency handoffs, source-specific acceptance, verification tiers, lesson and metric disciplines | Extract mechanisms and tested failure lessons, not its stack, provider choices, exact commands or all accumulated prose. |

Sources were inspected locally on 2026-09-30. Application acceptance findings below belong to their named review source, not whatever an engineer changes afterward.

## Enhancement inventory

Priority means recommended order, not implementation approval. All proposed skill changes here are Suggested. Items marked Retain are already in the public baseline and need preservation, not duplicate rules.

### W01 — Preserve the shared/project split

**Priority:** P0, Retain and strengthen routing. **Worker:** architect defines boundary; engineer updates templates/tests.

Keep shared approval, coordination, task records and evidence principles in TEAM/AGENTS. Put local commands, paths, owner preferences, integration conventions and invariants in the project extensions. A root entry point must reach the applicable package instructions in split-root repositories. Detect existing equivalents before creating duplicate documents. The public skill already does this; the installed copy does not.

**Acceptance:** a new adoption and an existing-project upgrade both preserve local policies; a Python/service project inherits no browser, TypeScript, provider or database requirement. Links work from both roots. Project rules remain reachable after a split.

### W02 — Make “continue” resolve work by role and dependency

**Priority:** P0. **Worker:** architect, then engineer for deterministic checks.

Replace the public template's ambiguous “continue Current work” with: follow the specific owner assignment; otherwise resume this worker's active eligible task or choose the first Approved, dependency-ready item for the established role. Check recorded prerequisites and the configured integration source first. A refresh failure is recorded; it does not turn unseen approval into authority. Follow existing local-only conventions when there is no remote.

Complete and record the task, then continue within the existing authorized scope. Another worker's active task, an owner decision and a blocked prerequisite are not eligible merely because they appear first. Reviewing the backlog does not authorize Suggested work. An explicit instruction to approve/document work for another worker does not mean execute it now.

**Acceptance:** scenarios E01–E04 below dispatch without repeated approval questions, taking somebody else's task, or assuming background execution exists.

### W03 — Make technical handoffs sufficient without chat relay

**Priority:** P0. **Worker:** architect specifies minimal fields; engineer adds examples.

A blocked or review-ready task should identify the responsible role, exact question/next action, prerequisites, source commit/branch, and relevant evidence. Separate owner product decisions from technical prerequisites. A pending technical review blocks its dependents, not every independent Approved task. Recommended worker is advice; Implementor identifies actual ownership.

Prefer the existing task card plus linked evidence over another handoff file. Allow multiple active records only under the project's concurrency convention. No generic model names, fixed worker count, automatic messaging or dispatcher is implied.

**Acceptance:** a third agent can resume or review from repository records without the owner copying chat. Missing user feedback only holds work that actually depends on it.

### W04 — Separate approval, implementation and acceptance

**Priority:** P0. **Worker:** architect.

Approval answers whether work is authorized. Status answers where execution stands. Acceptance answers whether the specified result has been evidenced at a particular source. Use these meanings consistently rather than adding a complicated universal state machine. Permit progress such as “implemented; required identity integration NOT RUN; acceptance held by reviewer” in the existing Status field.

Archive Done only when the task's own acceptance criteria are met. A delivered child may be Done if its contract is implementation-only, while a parent awaiting real integration stays open. If a later review disproves completion, append a dated correction, reopen the relevant active work and link the original evidence; preserve the historical record.

**Acceptance:** an auth-dependent parent cannot become accepted from mocked service tests, a health check or broad green CI. Review of source A cannot accept changed source B without a relevant delta check and evidence.

### W05 — Keep the routine reading path bounded

**Priority:** P1. **Worker:** architect chooses disclosure; engineer reorganizes.

Retain the active queue/archive separation and newest-section changelog reading. Keep a short handoff at the top of the queue; detailed plans and evidence stay behind task links. Read applicable policies once per session and refresh changed sections when evidence or instructions change. On continuation, inspect targeted status/diffs instead of rereading every archive.

The lesson ledger now undermines its own “one screen” startup promise. Propose an active lesson index plus an on-demand historical ledger: promoted/superseded entries move intact with their evidence and rule pointer. Read active lessons and task-relevant history. Prefer replacing duplicate policy with a pointer over indefinitely adding startup rules. Evaluate this as a document migration, not permission to discard history.

**Acceptance:** an unrelated routine task opens neither completed history nor old audits by default; a repeated bug still reaches its relevant historical lesson. E08 checks both sides.

### W06 — Isolate concurrent workers and shared generated resources

**Priority:** P1. **Worker:** architect for convention; engineer for templates.

Project configuration should state sequential-only or concurrent work, integration source, task reservation/ID allocation and landing convention. Concurrent code work uses separate checkouts; ports, generated outputs, databases and mutable dependency caches also need isolation where applicable. A separate worktree alone does not isolate shared caches. Respect another worker's active checkout.

One source-of-truth queue need not mean a single-file concurrent editing race. For a small team, use named reservations and serialized integration. Propose automation only when collisions justify it. Remote refresh does not authorize reset, force push or overwrite; integrate conflicting handoff edits deliberately.

**Acceptance:** two workers cannot silently claim the same task/ID or accept each other's in-progress tree. Temporary verification modifies only invocation-owned resources. Documentation work can remain independent of code under development.

### W07 — Specify what each check actually proves

**Priority:** P1. **Worker:** architect designs tiers; engineer implements configured checks.

The shared rule should require appropriate evidence and honest limits. Project policy maps affected surfaces to fast checks, integration/browser checks and release gates, including invocation working directories and actual target runtime. Do not copy Morning Todo's fixed soak counts or “always build everything” into every project.

Distinguish PASS, product failure, environment failure and NOT RUN. A classifier must establish the environmental precondition before blaming the host; a failed result after valid inputs stays a product failure. Record failure evidence even after a later green. Independent doc-only work should not claim to accept another worker's uncommitted product code. Validate final record edits when those records are machine-checked.

**Acceptance:** E05–E07; a normal docs change runs relevant document checks, while an actual release follows the configured full gate. A test-launcher failure is described as invocation/environment trouble, not a product regression.

### W08 — Keep evidence bound to the tested artifact

**Priority:** P1. **Worker:** architect, then engineer for minimal schema support.

For material acceptance, record source, producer command/working directory, environment/version details that affect interpretation, executed result, artifact location and limits. Cite external review baselines before applying their recommendations. Keep volatile counts/costs/verdicts in one current measured location; other docs link to it. Preserve dated historical numbers.

Do not mandate Morning Todo's count regex grammar, score rubric, task taxonomy or report layout everywhere. Structured evidence metadata may replace prose guards where it measurably reduces maintenance. A validator is an aid, not proof that a review premise is true.

**Acceptance:** another reviewer can reproduce the relevant result, distinguish a dated observation from current state, and avoid counting soak runs as test cases. Broken or unexecuted integrations cannot borrow another artifact's PASS.

### W09 — Extend validators around observable workflow errors

**Priority:** P1 after W02–W04 contract agreement. **Worker:** engineer; architect reviews authority implications.

Retain the public stdlib-only, read-only validator and split-root support. Add focused checks where the chosen fields can express a machine-verifiable invariant: active/completed duplicate IDs, missing blocker/next action for held work, role ownership of Current work, approved-vs-suggested section consistency, and completion attribution/time consistency where a project adopts that schema. Treat nuanced authority and semantic dependency judgments as review findings, not infallible regex verdicts.

Accept LF and CRLF input. Reject malformed records without rewriting them; intentional historical gaps remain warnings by default. Test malformed links, fragment links, split roots and missing inputs. New validators must demonstrate that representative invalid inputs fail, not merely that good templates pass. Avoid forcing optional fields into historical records without a migration decision.

**Acceptance:** both valid layouts pass; meaningful malformed fixtures fail; no files change; intentional old-history warnings remain distinguishable from active errors.

### W10 — Budget governance and prevent rule accumulation

**Priority:** P2. **Worker:** architect recommends; engineer measures.

Retain re-plan and elegance checkpoints. Normal red-to-green development is not two failed attempts at the same diagnosis. Compare verification's demonstrated defect catches with wall time, reruns, token/context use and document churn. Offer a periodic keep/retune/retire review on request or at a suitable checkpoint; no unattended scheduler is implied.

Graduation should be evidence-based: repeated hits or one costly failure makes a candidate for review, not an automatic universal rule. Consolidate or retire redundant guidance while retaining its historical rationale. Keep measured cost thresholds project-configurable.

**Acceptance:** a cheaper equivalent check can be proposed without weakening a contract; retirement carries evidence and follows existing approval. A one-off command typo does not automatically become permanent startup policy.

### W11 — Separate owner Git identity from work attribution

**Priority:** P2. **Worker:** engineer.

Make commit attribution an explicit optional project preference. Honor configured Git identity and owner-approved trailer conventions; record the actual worker in task completion records. Preserve the same worker/time in the final changelog entry when the workflow requires it. Morning Todo's “owner only, no generated trailers” is an owner instruction, not a universal rule for every adopting repository.

**Acceptance:** project preference survives tools with conflicting defaults, without overwriting another project's authorship policy or rewriting published history as part of ordinary adoption.

### W12 — Close the skill source/install drift loop

**Priority:** P0 for maintenance project setup. **Worker:** architect defines release contract; engineer implements.

Document the canonical repository/path and last adopted skill version or commit in project configuration. Installation and repository publication are separate operations with separate verification. When upgrading, compare actual installed files rather than trusting a push result. Reconcile conflicting old template-pointer instructions: projects capture improvements now; the maintenance project generalizes, tests and publishes them during an authorized release.

**Acceptance:** future agents can identify the source and installed baseline, report drift, and update only within the requested scope. They do not edit the global skill or public repository whenever a project changes a local policy.

## Low-effort cross-project improvement loop

Use one candidate inbox in the skills maintenance project, for example `team/skill-improvements.md`, governed by that project's chosen workflow. A project agent captures a short candidate in its local lessons or requested export; the owner can say “capture this for the skill” or “review the skill improvements.” The maintenance agent imports/deduplicates it when the artifact/repository is available. This is file-based reuse, not an implicit cross-project sync service.

Capture only: source project/task/commit; observed failure and cost; prevention candidate; scope (shared workflow / web engineering / project-only); proposed observable evaluation; recommendation and approval state. Similar failures enrich one candidate rather than creating duplicate tasks. Record rejected/local-only decisions so they are not proposed again without new evidence.

After approval: make the smallest template/skill change, run validator and realistic scenario checks, review changed instructions for token and approval overhead, update adoption/release notes and publish when requested. Then verify the installed copy separately. Projects adopt a new version intentionally, preserving their extensions. No owner chat recap should be necessary after the initial artifact transfer.

Suggested first batch: W12 plus W02–W04, retaining W01; then W05 and focused W09 checks. W06–W08 can follow with the technical skill pilot. W10–W11 are targeted refinements, not a reason to delay useful publication. All remain Suggested pending the owner's maintenance-project assignment.

## Technical extraction and coverage boundary

The candidate [web-app-engineering skill](web-app-engineering/SKILL.md) is separately packaged. It supports browser prototypes, personal apps, internal tools and production SaaS; React-specific details are conditional. It contains no universal framework/provider selection and requires neither billing nor multi-tenancy in an app that does not use them.

| Application lesson/policy | Destination | Treatment |
|---|---|---|
| TEAM roles, approval, dispatch, handoffs, re-plan, elegance | W01–W04/W10 | Shared coordination, owner/model preferences configurable |
| Active queue, attribution, truthful records, archives | W04/W05/W08/W11 | Retain baseline; improve source and acceptance distinctions |
| Project rule 5: persistence single door | Technical skill: state/data | Preserve boundary intent; no mandated file path or whole-board server save |
| Project rule 6: owner UI decisions | Project policy; W03 | Respect approved behavior/copy; no universal ban on authorized design work |
| Project rules 7–8: reviews/candidates | Public baseline plus W03/W08 | Already supported; extend technical acceptance rather than duplicate scoring rules |
| Project rule 9: fixture clock | Technical skill: state/data + verification | Date keys, instants, midnight/month/DST; no universal fixture naming |
| Project rule 10: fail-loud, seed once | Technical skill: verification; W07/W09 | Select applicable guarantees; demonstrate meaningful negative paths |
| Project rule 11: claims/metric sync | W08 | Single live evidence location, history retained; regex grammar stays local |
| Project rule 12: Git attribution | W11 | Optional project preference |
| P-030 DragSession and recurring drag repairs | Technical skill: interactions | Pure geometry snapshots, one gesture lifecycle, shell timing, browser authority |
| P-069/P-071/P-109 | Technical skill: state/data | Deterministic commands, honest failures, real legacy decoding, semantic no-ops |
| P-083/P-084/P-085 and P-118 review | Technical skill: cloud + verification | Exact production proof, atomic revisions, immutable replay, real request/auth acceptance |
| Consultancy/business/owner-feedback records | Project policy | Customer and commercial evidence stay separate from technical correctness; no outreach/pricing decision implied |

Primary evidence, at the documentation snapshot unless a review names another source:

- [Shared TEAM](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/TEAM.md), [project configuration](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/TEAM-PROJECT.md), [shared rules](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/AGENTS.md), [project rules](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/AGENTS-PROJECT.md).
- [Lessons](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/LESSONS.md), [verification](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/VERIFICATION.md), [release tiers](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/RELEASE-CHECKLIST.md).
- [P-030 spec](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/specs/P-030-DRAG-SESSION-SPEC.md), [P-069](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/specs/p069-deterministic-transitions.md), [P-071](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/specs/p071-storage-boundary.md), [P-084](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/specs/p084-pending-command-contract.md), [P-085](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/specs/p085-platform-decision-gates.md).
- [P-118 acceptance review](https://github.com/meister28/morning-todo/blob/c48aff48cba24df66f964ff5fdab4d9b7cce0ca7/app/team/audit/2026-09-30-p118-cloud-core-acceptance.md), reviewing implementation `26bcf1b661429fb79858adac47616885d837bd0b`. Counterexample probes assert observed defects; their green execution is not acceptance of the implementation.
- [Public workflow baseline](https://github.com/meister28/skills/tree/6c074184eb79f0884d49209e0ccdcee8412938a5/skills/team-workflow). These links describe inspected local content; online availability was not separately tested.

## Export contents and validation

- This file: workflow improvement inventory and maintenance-project handoff.
- `web-app-engineering/`: portable candidate skill, SKILL.md plus four conditional references; proposed repository destination `skills/web-app-engineering/`.
- [EVALUATION.md](EVALUATION.md): observable regression scenarios for both skills; expected outcomes belong to the evaluator, not a blind test agent's input.
- `VALIDATION.md`: executed package checks and remaining behavior-evaluation limits.

The extraction is ready for maintenance-project review. It has not upgraded the installed workflow, installed the technical skill, created the new project, committed application changes or published a release.
