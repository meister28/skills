# Browser interactions

Use for gesture/state/layout bugs or behavior-preserving interaction refactors. Start with the currently approved interaction contract and upstream component behavior at the installed version. A polished demo is a comparison target; replacing app behavior requires checking the app's ordering, history, filters and undo semantics too.

## Own one gesture lifecycle

Trace start, preview, cancel and settle across handlers, state, refs and vendor components. Identify who owns preview order, original state, engagement samples, commit detection and animation captures. Coupled timing/state spread across modules is a candidate for consolidation behind a small lifecycle interface. Repeated fixes across the same files are evidence for examining that seam, not automatic authority for a rewrite.

Keep pure decisions on plain data: IDs, matrices, pointer coordinates and geometry snapshots. A “pure core” accepting a DOM-method adapter is still coupled to the DOM. Let the UI shell read layout, normalize events and apply effects. Scope queries to the board root; portaled overlays may need a separately identified lookup. Gesture-local mutable samples belong to the session and reset with its lifecycle, rather than module-global state reset by distant handlers.

Keep the drag library's sensor and sortable responsibilities unless the task changes them. A vendored component should expose a narrow integration seam; app-specific persistence, calendar and domain logic should have a clear owner outside generic UI code. Record upstream adaptations so an update can distinguish intentional differences from accidental drift.

## Preserve commit and paint ordering

Separate preview from a committed domain action. No-op and cancel outcomes should produce the approved persistence/undo/notification behavior. Compare domain meaning, not incidental object allocation, to decide whether an action changed anything.

In React, a callback outside its synthetic event system may have different flushing behavior. Measure the real sequence before prescribing a timing fix. Capture pre-write geometry before the controlled-value change; play a layout transition after the matching commit, using the project's established shell mechanism. If write-before-host-notification is an existing invariant, preserve it explicitly. Avoid timers or forced flushing as unexplained patches.

Pure unit tests can establish insertion and settlement decisions. jsdom cannot certify real layout, sensor cadence, rendered frames or visual smoothness; do not pin its stub geometry as a product requirement.

## Build a contract-driven interaction matrix

Select relevant cases, including the dimensions that caused past defects:

- Same/cross container, empty destination, first/last/between positions, grow/shrink and filtered/hidden rows.
- Pointer, touch and keyboard where supported; long press versus scroll/swipe; stationary pointer while layout changes.
- Cancel, dropped outside, rapid successive gestures, undo, reload, calendar rollover and authoritative refresh during interaction where applicable.
- Scroll containers, variable row heights, collapsed/stacked layouts, overlay/portal position and focus/announcements.

Use real browser events for the browser contract. Seed a context once; reload should exercise the app's persistence, not reseed the fixture. Record the input preconditions and changed order/domain result separately. A missed long-press duration on a loaded host is different from a valid drag that commits incorrectly.

For performance, observe preview work and frame behavior on representative board sizes. Diagnose repeated layout reads, unbounded scans and unnecessary renders before introducing caches. Preserve correctness while measuring; a fast no-op that never performs the intended move is not an improvement.
