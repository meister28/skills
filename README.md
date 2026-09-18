# skills

A collection of [Agent Skills](https://agentskills.io) for AI coding agents.
Skills live in `skills/<skill-name>/`, each with a `SKILL.md` and whatever
supporting files it needs. Shape inspired by
[mattpocock/skills](https://github.com/mattpocock/skills).

## Why this exists

A day of AI-assisted development, and probably yesterday too:

You're deep in a feature with your favorite frontier model. The context is
loaded, the plan is set — and then you hit your usage limit. So you switch
to a cheaper agent to keep the implementation moving. Later your quota
resets, you switch back to the frontier agent — and it discovers three
things that need doing. Two are routine, so you hand them to the cheap
agent as well. Then your usage runs low again, and you swap once more.

That rhythm — the expensive model for thinking, the cheap one for typing —
is the most efficient way to work with AI. It is also how projects fall
apart, because **every switch is a fresh start.** The next agent knows
nothing about what was decided, what was tried, what is approved, or what
the rules are. So you re-explain the project from scratch; the agent
re-litigates settled decisions, implements something you never asked for,
or "fixes" what was already fixed. Multiply by every switch in a day and
the mess compounds: two agents, two different versions of what the project
even is.

`team-workflow` fixes this by moving the project's memory out of chat
scrollback and into the repo, where every agent reads the same files:

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
