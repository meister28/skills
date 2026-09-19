# team/reviews/ — review and design-pass records

Durable records of review passes that surface candidates or design
decisions: architecture-review HTML reports
(`architecture-review-<YYYYMMDD>-<HHMMSS>.html` — the producing skill
writes to the OS temp directory for immediate viewing; copy the durable
version here in the same session) and markdown companions for other
review skills (`<YYYY-MM-DD>-<skill>-<topic>.md`) recording the brief,
tokens/decisions, and constraints for future passes — the report or
companion, not the chat transcript, is the record.

**Every candidate surfaced by a review becomes a `../TASKS.md` entry in the
same session** — Suggested, with its badge strength (Strong / Worth
exploring / Speculative), its problem/change/acceptance from the report,
the source path under Approval, and any deferral or sequencing constraint
in the Status line (AGENTS.md rule 8). Registration is not approval.
