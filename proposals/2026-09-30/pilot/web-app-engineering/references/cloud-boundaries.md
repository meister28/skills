# Cloud and server boundaries

Use when an app actually gains or changes authenticated server state. These contracts apply to personal apps and internal tools as well as SaaS. Billing, teams, background jobs and offline synchronization are conditional features, not default scaffolding.

## Right-size the transition

Start from the chosen customer/workload envelope, deployment target and existing domain contracts. Preserve useful pure domain code while changing authority. Local storage replaced by a database that saves the whole board does not establish authorization, atomic concurrency or safe server undo.

Separate commands and queries from identity resolution and database adapters. Authoritative ownership, time, revisions and acceptance live server-side. Keep client projections free of database/server-secret imports. Adopt an existing supported framework integration rather than inventing an adapter to evade a failing proof. Reopen a selected stack only on the project's stated evidence/cost threshold, classifying missing credentials and environment failures separately from incompatibility.

## Prove the selected integration, then its actual wiring

For a risky new stack/SDK combination, a bounded walking skeleton should use the exact lockfile and target runtime, supported production build/entry, a protected request, an actual database write/read after restart and relevant client/server bundle checks. A dev server or health endpoint alone leaves the critical path unproven.

The product delivery must then prove its own emitted entry invokes its actual handlers. A successful disposable spike is source/version-specific; it cannot accept a different framework pin or middleware configuration. Inspect generated manifests, registered routes and dependency APIs when wiring is suspect. Await async identity resolvers correctly. Exercise strict input validators and HTTP error/status mappings on the deployed request path, not only as disconnected helpers.

## Atomic authority and replay

Enforce authorization and required revisions atomically with the write. Use the database's conditional updates, constraints or suitable transaction isolation to enforce the promised winner/conflict outcome; add an application lock only when the chosen mechanism needs it. A separate pre-write check can become stale even if the write itself is transactional. Use a consistent snapshot for multi-query reads when the contract requires it. Test with genuine second-connection/device interleavings.

Validate commands at the transport boundary and service contract. Bind replay identity to the agreed actor/scope and payload; the same key with different content must not silently become a new successful command. Once sent, retain an owned immutable envelope for retry. A copied reference to the caller's mutable nested object does not satisfy immutability.

Choose explicit revision/conflict semantics. Two distinct commands against the same required revision should satisfy the agreed winner/loser rule; a conflict is not a saved acknowledgment. Check historical ordering anchors and no-op completion semantics against the same domain contract on both client and server.

## Optimistic state without a second authority

For optimistic behavior, represent confirmed state plus ordered pending intents and explicit acknowledged/rejected/conflicted/uncertain outcomes. Reproject remaining valid intents after a rejection rather than restoring an old whole-board snapshot. Handle late/duplicate acknowledgments, stale refresh, dependent actions, interaction barriers and account changes. Capture an account/session epoch so old responses cannot mutate a new account.

Lost response and rejected command are different outcomes. Retry an uncertain request according to its exact replay contract; changing its ID/payload may duplicate a committed action. Make submission and persistence promises explicit before adding durable offline queues.

Keep domain replay separate from fetching/retries/cache invalidation. If multiple routes need shared server data or a custom cache system is emerging, evaluate the project's established query/cache library before extending a board-local reducer into infrastructure.

## Identity, secrets and real-data recovery

Resolve identity from the supported server integration. Scope data access to the authenticated owner/account/tenant as applicable; even a single-user-first app needs separate-account denial tests once multiple accounts can exist. Exercise anonymous, forged identity, invalid/expired session, sign-out and cross-account access on the real request path. Apply same-origin/CSRF protection appropriate to the actual transport; type safety alone does not authorize a request.

Keep real credentials in approved private mechanisms. Pure/service tests may inject identity; shipped code must verify real identity and must not acquire a test-header/login bypass to make acceptance green. Run credentialed checks only against trusted code in an authorized environment. Missing credentials means the relevant gate is NOT RUN; finish secretless independent work and record the next action.

A bundle isolation check must first prove the secret-bearing server module was included and reachable where intended. An empty manifest with no handlers cannot demonstrate a safe working integration. Use harmless canaries rather than printing secrets.

For real durable data, prove rollback on partial failure and restore a consistent backup into a fresh database when required by the release/data contract. Respect the database's consistency/backup mechanism. Deployment, provider procurement and production-data mutation require their own authorization; design or tests do not imply it.
