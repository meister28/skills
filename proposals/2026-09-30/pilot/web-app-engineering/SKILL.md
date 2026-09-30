---
name: web-app-engineering
description: Investigate or change complex browser interactions, state/data persistence, optimistic server commands, or production integration in stateful web apps. Use when these boundaries need technical proof; routine copy or styling edits follow the project's normal checks.
---

# Web app engineering

Improve the requested behavior or technical boundary with evidence from the actual application. Keep product requirements, architecture choices and acceptance distinct. This skill complements the repository's coordination rules; it does not supply a task queue, authorize adjacent work or choose the owner's UX.

## Establish the applicable contract

Read the relevant repository instructions and approved task/spec. Identify the app's current phase, affected journey, source baseline, deployment target and existing authoritative state. Inspect only the code/configuration and evidence needed for the assignment. Treat a handover or passing suite as a claim to verify where it matters.

For a disposable prototype using synthetic data, prioritize UI/interaction and domain correctness. Apply the owner's reset/data-loss contract; production backup, billing and tenancy work is not implied. For real user data, authenticated server integration or release work, apply the relevant boundary and recovery requirements. If the phase is genuinely unclear and changes the decision, clarify that question while continuing independent analysis.

Follow existing framework and library decisions. Verify version-sensitive APIs against the installed implementation and official documentation when needed. A new abstraction or stack change earns its cost through a demonstrated problem; repeated bugs prompt a lifecycle/state-boundary review before more patches.

## Route to the affected surface

Read only the applicable references:

- Drag/drop, swipe, sortable layouts, animation or UI timing: [browser interactions](references/browser-interactions.md).
- Reducers, dates, undo, local persistence, import/export or domain validation: [state and data](references/state-and-data.md).
- Server commands, optimistic reconciliation, identity/database boundaries or moving a prototype to a backend: [cloud boundaries](references/cloud-boundaries.md).
- Selecting checks, interpreting flakes, acceptance reviews, build/runtime proof or performance claims: [verification](references/verification.md).

For a review, trace the relevant journey across its real boundaries and report concrete gaps with evidence; implementation remains within the owner's requested scope. For a refactor, write the behavior invariants before moving ownership and use separable steps so a regression can be located. For a fix, reproduce the contract violation and verify the affected journey after the change.

Keep existing regression coverage during a behavior-preserving refactor. Revise a test only when the approved contract or measured behavior establishes that it pins the wrong thing; document that reason. Core tests prove decisions, integration tests prove wiring and persistence, browser tests prove browser interactions. Pick the smallest combination that proves the assignment under the project's required gates.

## Report the supported conclusion

Record the source, changed boundary, actual verification and unresolved limits in the project's existing task/review records. Distinguish implementation from acceptance and mandatory NOT RUN checks from successful ones. A temporary harness or mocked identity does not accept a different production path. If a prerequisite is unavailable, preserve the useful result, name the exact blocked gate, and continue independent authorized work.

Propose the smallest next repair when a demonstrated gap remains. Avoid turning one project's toolchain, provider, fixed test count or historical workaround into a requirement for unrelated apps.
