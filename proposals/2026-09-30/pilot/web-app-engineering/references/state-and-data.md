# State and data contracts

Use for deterministic domain transitions, dates, undo, local persistence and import/export. Agree the app's actual retention/reset contract and phase before adding recovery machinery.

## Deterministic transitions and meaningful no-ops

Capture time and generated IDs once at dispatch and pass them into pure transitions. In React, a state updater can be invoked more than once; generating an ID or timestamp inside it can turn one intent into multiple identities. Prefer explicit action/context inputs and returned domain/effect facts over reducers that read ambient time, storage or notifications.

Define equivalence per stored meaning: optional absent and undefined may be equivalent; a boolean preference may mean “enabled iff true.” Compare fields under that contract rather than JSON bytes. A semantic no-op should not mint an undo record, revision or misleading success effect unless the product explicitly specifies one. Test through the real reducer/journal/adapter when those effects matter.

Undo belongs to domain intent. Local snapshot restore may be appropriate for an isolated local prototype. With acknowledged server commands and other writers, an old whole-board snapshot can erase newer work; use an authorized compensating action and conflict semantics instead.

## Dates are domain types

Distinguish a calendar date key from a timestamp and define whose timezone/day policy controls each. Syntax-only ISO checks can accept impossible dates; Date.parse may normalize invalid components. Reuse component-aware canonical predicates at the real boundary. Server acceptance and client prediction must state how a day change affects an outstanding action.

Fixed-clock tests derive every fixture value from the injected clock. Live-clock browser tests derive assertion dates at the relevant step and verify the picker's displayed month before targeting a day. Include relevant midnight, month/year, leap-day and DST transitions rather than keeping literals that expire. Freeze the clock when determinism is the contract; advance it deliberately when testing rollover.

## Persistence is a boundary, not distributed convenience calls

Use the established adapter/service as the single door for load, validation, migration and write. For recoverable data, distinguish missing, malformed, unsupported version, read failure and write failure according to the product contract. Silent fallback to an empty successful board can mask data loss. A factory-reset prototype may deliberately clear everything when that is the approved behavior.

Preserve published migrations; append changes when evolving a stored schema. Inspect actual historical payloads and Git history, not just today's TypeScript shape. A field once stored as a full instant can be valid legacy data even when the current type is date-only. Keep tests for actual previous formats and the current export/import format.

At import/export boundaries, validate the whole payload under the agreed rules, reject duplicate identifiers, preserve supported optional facts and refuse unsupported future versions explicitly. Reuse the canonical decoder rather than approximating it with a second regex/schema. Define unknown-field and atomic-import policies deliberately; do not silently drop data as an accidental repair. Preview and actual commit must agree about what will be accepted.

Test real write failures, partial failures and restart/reload behavior where relevant. Include synchronous failure if the production adapter throws synchronously; promise-only fakes can miss a retry state that never passes through loading. Restore invocation-owned demo state after verification.
