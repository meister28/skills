# skills

Agent Skills for AI coding agents. Each skill lives in `skills/<skill-name>/` with a `SKILL.md` and any supporting files it needs. Compatible with any agent that reads the [Agent Skills](https://agentskills.io) format, including Claude Code, Codex, and Cursor. Shape inspired by [mattpocock/skills](https://github.com/mattpocock/skills).

---

## The skill: [team-workflow](skills/team-workflow/)

**Every AI agent on your project shares the same memory, the same rules, and the same task queue. All of it lives in the repo, not in chat.**

**Work seamlessly with different AI agents on one project.**

**One command sets up a working agreement that any AI agent — Claude Code, Codex, Cursor, or whatever ships next month — reads before it touches code.**

**Save tokens and still get top-tier code and architecture: the expensive model only works where it matters.**

**Your AI agents work like a real engineering team, coordinating with each other.**

Switch models mid-feature, run two agents in parallel, or come back after a week: the next agent starts from the project's written record instead of a guess.

### The problem

The most cost-effective way to work with AI is to use a frontier model for thinking and a cheaper one for implementation. In practice that setup breaks down, because **every switch is a cold start.** The new agent doesn't know what was decided, what was tried, what is approved, or what the rules are. So you re-explain the project, and the agent re-opens settled decisions, builds something nobody asked for, or "fixes" what was already fixed.

Chat history is the wrong place for project memory. `team-workflow` moves it into files that every agent reads before touching code.

### How the workflow runs

```
Suggested ──▶ Approved ──▶ Built ──▶ Reviewed ──▶ team/TASK-HISTORY.md
    ▲                                    │
    └── review candidates become ────────┘
        new queue entries
```

1. **Plan.** A frontier agent (in the *CTO / Software Architect* role) writes an implementation-ready spec in `team/specs/` and adds a task to `team/TASKS.md` with acceptance criteria and a recommended worker. The task starts as `Suggested`.
2. **Approve.** You review and mark it `Approved`. `Suggested` items may not be implemented; `Approved` ones may.
3. **Build.** A cost-efficient agent (in the *Implementor / Software Engineer* role) picks up the task in a fresh session. It needs no briefing: the task, the spec, and the project rules are all in the repo. The spec and changelog are updated in the same commit as the code.
4. **Review.** Audits and architecture reviews are written to `team/audit/` and `team/reviews/`. Anything worth acting on becomes a new queue entry instead of disappearing when the session ends.
5. **Record.** Finished work moves to `team/TASK-HISTORY.md` with who did it and when.

Any agent, at any point, can read the queue and know what is sanctioned, what is done, and why.

### What changes in practice

| Without a shared workflow | With `team-workflow` |
|---|---|
| Switching agents means re-explaining the project | The new agent reads the repo and continues |
| "Is this approved?" is answered from memory of a chat | Approval state is recorded per task (`Suggested` / `Approved`) |
| Whichever model is open does whatever is asked | Each task names its worker: frontier for architecture and hard debugging, cost-efficient for well-specified builds, tests, and docs |
| Intent is pasted between chats | Specs in `team/specs/` are the hand-off between agents |
| Docs go stale within weeks | Changelog and spec are updated in the same commit as the change |
| Good ideas from reviews are lost between sessions | Review candidates become queue entries automatically |
| Each repo drifts into its own conventions | Improvements are back-ported to the skill, and every future project inherits them |

### What you get

- **Continuity across agents and sessions.** The task queue, specs, and history persist in the repo. No agent depends on what another agent remembers.
- **Lower cost per feature.** Most coding tasks don't need the most expensive model. Because every task names its recommended worker, routing work to the right tier is the default rather than an afterthought.
- **Control without overhead.** Nothing gets built unless it is approved, and UI changes are approval-gated. The rails are light: you decide what gets built, and agents handle the rest.
- **Documentation that stays true.** The binding rules require spec and changelog updates in the same commit as the behavior change. Six months later the docs still match the code, and the next agent's first five minutes are cheap.
- **A workflow that improves over time.** Scaffolded projects carry a pointer to the canonical template. Improve the workflow while working in any project, back-port it to the skill, and every future project benefits.

### What gets scaffolded

```
TEAM.md                 working agreement and binding rules for every agent
AGENTS.md               entry point for agents
CONTEXT.md              project context
CHANGELOG.md            updated in the same commit as each change
team/
├── TASKS.md            the queue: approval state, acceptance criteria, recommended worker
├── TASK-HISTORY.md     finished work, with who and when
├── specs/              implementation-ready specs, written before code
├── audit/              audit findings
└── reviews/            architecture and code reviews
```

### Install

Copy the skill into your agent's skills directory, commonly `~/.claude/skills/` or `~/.agents/skills/`. Use whichever your agent reads.

```bash
git clone https://github.com/meister28/skills.git
cp -r skills/skills/team-workflow ~/.claude/skills/
```

To pick up updates automatically, symlink instead:

```bash
ln -s /path/to/skills/skills/team-workflow ~/.claude/skills/team-workflow
```

### Use

Inside your project, invoke the skill (for example `/team-workflow`).

- **New project.** It detects your stack, fills in the project-specific settings (verification commands and the project's single-door rule), and scaffolds the files above.
- **Existing repo.** It compares against what is already there and proposes an adopt / keep / merge decision for each file. It never overwrites anything without your explicit per-file confirmation.

From then on, work the way the files prescribe: get tasks approved before they are built, and let finished work flow into `team/TASK-HISTORY.md`.

---

## License

[MIT](LICENSE)
