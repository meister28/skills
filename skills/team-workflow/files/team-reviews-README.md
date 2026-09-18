# team/reviews/ — architecture-review reports

The visual HTML reports produced by architecture-review passes are stored
here as `architecture-review-<YYYYMMDD>-<HHMMSS>.html`. The producing skill
writes its report to the OS temp directory for immediate viewing; the
durable copy is copied into this folder in the same session.

**Every candidate surfaced by a review becomes a `../TASKS.md` entry in the
same session** — Suggested, with its badge strength (Strong / Worth
exploring / Speculative), its problem/change/acceptance from the report,
the source path under Approval, and any deferral or sequencing constraint
in the Status line (AGENTS.md rule 8). Registration is not approval.
