# Agent identity and workflow upgrades — 2026-09-30

Owner request: name every agent with model/thinking level, and make updating
an older project workflow easy through the existing skill or a separate updater.

Prepared locally by `Atlas [Codex; model=unknown; thinking=unknown; id=A01]`.
The runtime identifies the GPT-6 family but does not expose an exact model
identifier or this session's selected thinking level. Unknown is deliberate;
reading configured defaults would not verify active-session overrides.

Later owner confirmation for this same instance: “Atlas is fine, currently
GPT-6.1 Sol Medium”. Its current label is therefore
`Atlas [Codex; model=GPT-6.1 Sol; thinking=Medium; id=A01]`, with value source
`owner-confirmed current session`. Earlier labels above remain historical.
The owner also required agents to ask for missing name/model/thinking values;
the templates now keep unresolved values pending rather than silently choosing
a name or leaving metadata unknown without asking.

Base: `c15aa13487e7d37061107edd3aa461eda3a408e2`.
At preparation these changes were local. The owner subsequently requested
commit and push; the Git commit containing this report identifies the approved
release. Installed copies and external project workflows are not updated by
this publication.

## Chosen approach

Use one team-workflow skill. A separate updater would duplicate source/version,
preservation and validation rules and require another installation. The skill
selects setup, update or already-current validation when invoked; it does not
run a background upgrade whenever an ordinary contributor starts work.

The updater reads the existing process, pins the requested target and compares
old upstream/current project/new upstream where the adopted base is available.
When the old version is unknown it merges conservatively, retaining safeguards.
It handles older combined files and split roots without replacing live queues,
task history or project policies. Only unresolved binding policy conflicts need
an owner decision. An incomplete upgrade keeps the previous adopted revision.
Repeated completion should not create duplicate rules or change records.

Agent names combine a memorable name, tool, actual reported model/thinking
values and a unique instance ID. Resumed instances retain IDs; distinct workers
with identical settings remain distinct. Settings changes get a dated label,
with past attribution preserved. Names flow through task ownership, handoffs,
reviews and completion; they do not establish role, approval or Git authorship.

TEAM-PROJECT.md now has a registry and an adoption receipt template. No new
task schema, automatic dispatcher, global config changes or root workflow
adoption is included.

## Evidence and limits

From `C:\codex\skills`:

- `python -B -m unittest discover -s skills/team-workflow/tests -v`: 13 pass,
  including old-record compatibility, CRLF, read-only validation and split roots.
- `python -B proposals/2026-09-30/pilot/check_package.py`: limited scalar
  frontmatter, 14 local package/document links and fresh strict adoption pass;
  expected warning is unconfigured project verification commands.
- `git diff --check`: pass. Use the local safe-directory override where needed.

These checks validate packaging and existing structural behavior, not the
agent's ability to merge every real project. No external project was upgraded,
no blind repeated behavior evaluation or automatic-discovery trial was run,
and the full PyYAML-based skill validator remains unavailable in this runtime.
The earlier pilot RESULTS/CHECK-OUTPUT remain historical evidence for their
own prior source rather than current hashes.

Independent review by `Echo [Codex; model=unknown; thinking=unknown; id=A02]`
confirmed the tests and identified one source-tracking gap: a modified checkout
needs a package digest as well as its base commit. The update guidance and
receipt now require that, so different working-tree revisions are distinguishable.

Current official documentation describes model and reasoning settings and
configuration overrides. This supports recording confirmed active settings
instead of treating a default as the current session:
[configuration precedence](https://learn.chatgpt.com/docs/config-file/config-basic),
[model reasoning settings](https://learn.chatgpt.com/docs/config-file/config-reference).

Publication is now owner-authorized. Installation remains separately scoped.
A real project adoption should verify its own preserved policy and records and
record the selected source in its receipt.
