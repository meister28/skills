# Verification and acceptance evidence

Use when choosing checks or deciding what a result supports. Honor required project gates; this reference helps interpret them, not bypass them.

## Select evidence by the boundary

Choose gates for the claim being made. Reload/restart proves persistence,
live credentials prove the actual identity integration, and backup restore
proves a required recovery contract. A prototype interaction change does
not inherit all three merely because this reference describes them.

| Boundary being claimed | Useful proof | Insufficient by itself |
|---|---|---|
| Pure domain decision | Literal inputs, expected domain outcomes, negative cases | Render snapshot or mocked service success |
| Persistence/transactions | Production adapter, actual schema/migrations, real failure/interleaving/reload | In-memory fake or old hand-crafted payload only |
| Browser interaction/layout | Actual supported browser/input, measured preconditions, rendered/domain result | jsdom geometry or programmatic reducer invocation |
| Authenticated request | Actual production wrapper, supported identity integration, denial/status cases | Injected identity in service tests |
| Production integration | Emitted entry, registered handler, write/read/restart on target runtime | Build exit zero, dev server, health endpoint or unrelated spike |
| Performance | Relevant production path, stated dataset/runtime, matched before/after metric | Faster check that skips the intended operation |

Inspect repository scripts/configs to confirm commands actually cover the claimed surface. A solution-style TypeScript config may make a familiar invocation check no source files; use the project's verified build/typecheck command. A stale launcher should be repaired or correctly invoked before interpreting a test result.

## Keep time-sensitive fixtures on one clock

Use when behavior or test data depends on time. For a deterministic test,
derive fixtures and expectations from the same controlled clock that the
application code observes. A fixed fixture date is valid when that clock is
also fixed; pairing it with a component that reads the live clock can make
the test expire as the calendar advances.

When a scenario intentionally uses live time, derive relative fixtures from
the same observed reference time and account for the time zone and calendar
boundaries relevant to the behavior. Inspect all clock readers, including
browser/server boundaries where applicable. For a rollover test, advance the
controlled clock explicitly rather than wait for the real calendar to change.
Keep genuinely time-independent literals with a clear reason.

Reuse the project's fixture helpers and exemptions. A repeated date-rot
failure can justify a targeted guard; demonstrate its rejected and permitted
cases before relying on it. This guidance does not require a fixed date,
particular toolchain, new guard, or clock policy for unrelated tests.

## Trust the instrument only after its failure path is credible

Filters selecting zero cases, unknown flags, zero executed cases or malformed verdicts must not produce PASS. Demonstrate a representative failure and a genuine success for a new fragile gate. Machine verdicts should have one unambiguous channel; diagnostics use a distinct prefix. Preserve the relation between selected, executed, failed and skipped cases.

Seed fixtures once per intended context. A reload assertion should reload persisted state, not trigger another seed. Keep test state consistent across earlier/later scenario steps; derive the next probe target from what earlier steps actually left behind. Use isolated databases, caches, ports and outputs for concurrent runs where they are mutable.

For timing-sensitive gestures, measure the input conditions used by the actual sensor. If activation duration or swipe cadence wasn't established, report environment failure with those measurements. Once valid input is established, a failed commit is a product failure. Prove that the classifier cannot swallow a real product-failure case.

When failure may depend on host load, compare the same instrument against the predecessor under matched conditions. Keep both reds/greens and the cause evidence. A quiet-host rerun does not erase a loaded-host failure. Follow the project's re-plan rule when the same diagnosis repeatedly fails.

## Keep checks economical

Map changed surfaces to the smallest meaningful set of unit, integration, browser and document checks, while retaining required gates. Separate ordinary changes from actual release candidates. Repeated soak runs are justified by a flaky/timing contract or the established project gate; no fixed universal repetition count applies.

Measure total wall time, duplication and contention before parallelizing. Separate worktrees may still share optimizer caches or outputs. Record test source and input fixtures so evidence from concurrent runs remains attributable. Documentation-only work should validate its records and links without pretending to accept another worker's changing implementation.

For performance claims, compare the same behavior with representative workloads and deployment conditions. Separate startup/bundle cost, render/interaction latency and backend latency. Preserve input validity and correctness; specify the approved budget when one exists. This skill supplies no universal numerical threshold.

## Issue a source-specific conclusion

For material acceptance record: source commit/build, command and working directory, relevant runtime/dependency/fixture details, executed result, evidence artifact and limits. Keep live changing counts in one measured location and historical observations dated. Correct stale claims without rewriting their original evidence.

Mark mandatory unexecuted checks NOT RUN and keep affected acceptance open. Service tests with fake users, a successful stack spike or a broad green CI run cannot substitute for the actual missing boundary. Reconcile the tested artifact with the candidate artifact before accepting later work; state what the delta check covered.

An independent review requires an actual separate completed evaluation when the contract calls for one. An interrupted helper's partial findings, an implementor's self-review or an old favorable external review is not that sign-off. If only a partial audit was performed, report the inspected scope and concrete findings without claiming complete acceptance.
