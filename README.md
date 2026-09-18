# skills

A collection of [Agent Skills](https://agentskills.io) for AI coding agents.
Skills live in `skills/<skill-name>/`, each with a `SKILL.md` and whatever
supporting files it needs. Shape inspired by
[mattpocock/skills](https://github.com/mattpocock/skills).

## Why this exists

Multi-agent coding has a dirty secret: **the agents aren't the bottleneck —
the coordination is.**

If you run more than one AI agent on the same codebase, you know the
failure modes. Agent B re-litigates a decision Agent A already made —
because nothing records it. A "small fix" ships with an unrequested UI
redesign — because nobody wrote down that UI is approval-gated. A bug gets
"fixed" twice and breaks a third time — because the fix lived in a chat
scrollback, not in a file. Handoffs between agents turn into a fresh
onboarding every time, burning tokens re-discovering what was already
known. And every task routes to your most expensive model by default,
because there's no convention for when a cheaper one will do just fine.

**`team-workflow`** fixes this the boring way: a set of plain markdown
files that live *in your repo* and turn a pile of agents into a team with
a memory.

## The skill: [team-workflow](skills/team-workflow/)

One command sets up a working agreement that any AI agent — Claude Code,
Codex, Cursor, or whatever ships next month — reads before it touches
code:

- **A task queue that outlives the chat.** `team/TASKS.md` holds the
  backlog with approval states (`Suggested` ideas may not be implemented;
  `Approved` ones may), required acceptance criteria, and a recommended
  worker per task. An agent starting cold reads one file and knows
  exactly what's sanctioned, what's done, and why.
- **The right model on the right job.** Every task names its worker:
  *CTO/Software Architect* work (architecture, gnarly debugging,
  high-risk changes) prefers a frontier model; *Implementor/Software
  Engineer* work (well-specified builds, tests, docs sync) suits a
  cost-efficient one. Most coding tasks don't need the expensive brain —
  the workflow makes that routing the default instead of an afterthought.
- **Specs as the inter-agent contract.** Implementation-ready specs live
  in `team/specs/` — written before code, referenced by the task, kept
  truthful in the same commit. Agents stop pasting intent into chat and
  start handing each other documents.
- **Documentation that can't drift.** The binding rules require the
  changelog entry in the same commit as the change, and the spec update in
  the same commit as the behavior. Six months later the docs still tell
  the truth — which is what makes the next agent's first five minutes
  cheap instead of forensic.
- **Trust rails, not bureaucracy.** UI changes are approval-gated. Audits
  and architecture reviews land in `team/audit/` and `team/reviews/`.
  Review candidates automatically become queue entries, so good ideas
  stop evaporating between sessions.
- **Self-upgrading.** Projects scaffolded by the skill carry a
  "canonical template" pointer: improve the workflow while working in any
  project, back-port it to the skill, push. Every future project inherits
  the improvement instead of forking the convention per repo.

## Install

Copy a skill into your agent's skills directory — commonly
`~/.claude/skills/` or `~/.agents/skills/` (this collection is developed
against the latter; use whatever your agent reads):

```bash
git clone https://github.com/meister28/skills.git
cp -r skills/skills/team-workflow ~/.claude/skills/
```

Or symlink so updates propagate: clone the repo anywhere and
`ln -s /path/to/skills/skills/team-workflow ~/.claude/skills/team-workflow`.

## Use

Inside a project, invoke the skill (e.g. `/team-workflow`):

- **Fresh project?** It detects your stack, fills the project-specific
  slots (verification commands, the project's single-door rule), and
  scaffolds `TEAM.md`, `AGENTS.md`, `CONTEXT.md`, `CHANGELOG.md`, and the
  whole `team/` tree.
- **Existing repo?** It diffs against what's already there and proposes
  per-file adopt/keep/merge decisions — it never overwrites without your
  explicit per-file confirmation.

Then work the way the files prescribe: tasks get approved before they get
built, finished work moves to `team/TASK-HISTORY.md` with who/when, and
the next agent — human or AI — starts from a record instead of a guess.

## License

[MIT](LICENSE)
