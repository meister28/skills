# team/audit/ — triggered audit results

Every triggered audit (the four-dimension SPEC / DESIGN / CORRECTNESS /
QUALITY grading) is stored here as `YYYY-MM-DD-<topic>.md`. The file
records: the scores per dimension, the two or three highest-value concrete
gaps per dimension, the method (what was actually exercised, not what was
asserted), and the single most valuable next pass.

An audit changes no production code — the audit file is the deliverable.
Recommendations that should become work are registered as `Suggested`
entries in `../TASKS.md` (see AGENTS.md rule 8 for the review-candidate
case).
