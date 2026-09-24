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
3. **Build.** An agent in the *Implementor / Software Engineer* role picks up the task in a fresh session. It needs no briefing: the task, the spec, and the project rules are all in the repo. The spec and changelog are updated in the same commit as the code. When verification fails twice on the same approach, the agent stops and re-plans instead of grinding on; before reporting done it asks "knowing everything I know now, is this the elegant solution?" — and flags hacks instead of shipping them under a green test suite.
4. **Review.** Audits and architecture reviews are written to `team/audit/` and `team/reviews/`. Anything worth acting on becomes a new `Suggested` queue entry instead of disappearing when the session ends. Corrections — from you, a review, or a failed verification — become one-line prevention rules in `team/LESSONS.md` that every agent reads at session start.
5. **Record.** Finished work moves to `team/TASK-HISTORY.md` with who did it, when, and the evidence. After owner review, recurring lessons become binding rules in the shared agreement or project extension, according to their scope.

Any agent, at any point, can read the queue and know what is sanctioned, what is done, and why — and the team stops paying for the same mistake twice.

### A task's life, in four file snapshots

**1. The architect proposes** — a new entry lands in `team/TASKS.md`, `Suggested`, with a worker recommendation:

```markdown
### P-007 — CSV export for the orders table

**Trigger:** Architect proposal — users need a filtered export.
**Approval:** Suggested — awaiting the owner's decision.
**Recommended worker:** Implementor / Software Engineer — the spec carries the decisions.
**Type:** feature
**Summary:** Export the currently filtered orders as CSV.
**Implementor:** Unassigned
**Created:** YYYY-MM-DD
**Status:** Suggested — awaiting owner approval.
**Acceptance:** Exports match the active filter; 10k rows complete in under 2s.
**Spec:** team/specs/P-007-CSV-EXPORT-SPEC.md
```

**2. You approve** — the approval and status fields record your decision, and the task becomes buildable. The implementor picks it up in a fresh session with no briefing beyond "work the queue."

**3. The implementor ships** — code, spec, and changelog in one commit, each task provable:

```markdown
### Added
- Orders can be exported to CSV. Exports respect the active filter and stream
  in under two seconds for ten thousand rows. (P-007; Implementor / Software
  Engineer; completed YYYY-MM-DD HH:MM <timezone>)
```

**4. The queue stays clean** — the full record moves to `team/TASK-HISTORY.md`:

```markdown
### P-007 — CSV export for the orders table

**Trigger:** Architect proposal — users need a filtered export.
**Approval:** Owner approved the spec on YYYY-MM-DD.
**Recommended worker:** Implementor / Software Engineer — the spec carries the decisions.
**Type:** feature
**Summary:** Filtered CSV export shipped as specified.
**Implementor:** Implementor / Software Engineer
**Created:** YYYY-MM-DD
**Completed by:** Implementor / Software Engineer
**Completed at:** YYYY-MM-DD HH:MM <timezone>
**Acceptance:** Filter and performance criteria met.
**Design:** Stream the active filtered result into CSV.
**What changed:** Export uses the active filter and streams large results.
**Verification:** Export checks pass; measured 10k rows in under 2s (record the command used).
**Evidence:** Filtered export and CSV quoting checks pass; performance result is recorded.
**Spec:** team/specs/P-007-CSV-EXPORT-SPEC.md
**Changed paths:** Export module, tests, and product spec.
**Remaining uncertainty:** Embedded-newline quoting is covered, but downstream tools may interpret it differently.
```

Nothing above lives in a chat. If the next agent asks "is CSV export done?", "who decided the streaming approach?", or "did anyone worry about newline quoting?" — the answers are in the repo.

### What changes in practice

| Without a shared workflow | With `team-workflow` |
|---|---|
| Switching agents means re-explaining the project | The new agent reads the repo and continues |
| "Is this approved?" is answered from memory of a chat | Approval state is recorded per task (`Suggested` / `Approved`) |
| Whichever model is open does whatever is asked | Each task names its worker: frontier for architecture and hard debugging, cost-efficient for well-specified builds, tests, and docs |
| Intent is pasted between chats | Specs in `team/specs/` are the hand-off between agents |
| Docs go stale within weeks | Changelog and spec are updated in the same commit as the change |
| Good ideas from reviews are lost between sessions | Review candidates become queue entries automatically |
| The same mistake repeats with every new agent | Corrections become one-line rules in `team/LESSONS.md`, read at every session start |
| A cheap model ships a hack and you find out later | The workflow makes it stop and re-plan on repeated failures and flag inelegant fixes before done |
| Each repo drifts into its own conventions | Reusable workflow improvements can be brought back to the skill; each project's own policies stay in its extension files |

### What you get

- **Continuity across agents and sessions.** The task queue, specs, and history persist in the repo. No agent depends on what another agent remembers.
- **Lower cost per feature.** Most coding tasks don't need the most expensive model. Because every task names its recommended worker, routing work to the right tier is the default rather than an afterthought.
- **Control without overhead.** Nothing gets built unless it is approved. Product-specific rules, including any visual design approval policy, live in that project's extension. You decide what gets built, and agents handle the rest.
- **Documentation that stays true.** The binding rules require spec and changelog updates in the same commit as the behavior change. Six months later the docs still match the code, and the next agent's first five minutes are cheap.
- **A workflow that improves over time.** Reusable coordination improvements can be brought back to this skill. Project-specific decisions stay in the project's extension files, so future projects receive a clean template.
- **A team that learns from its mistakes.** Every correction becomes a one-line prevention rule in `team/LESSONS.md`, written while the cause is fresh and read at the next session start. Recurring lessons graduate into binding rules — the workflow compounds in the direction of fewer repeated errors.

### What gets scaffolded

```
TEAM.md                 working agreement and binding rules for every agent
AGENTS.md               entry point for agents
TEAM-PROJECT.md         project role preferences and operating decisions
AGENTS-PROJECT.md       project commands, docs, and additional policies
CONTEXT.md              project context
CHANGELOG.md            updated in the same commit as each change
team/
├── TASKS.md            the queue: approval state, acceptance criteria, recommended worker
├── TASK-HISTORY.md     finished work, with who and when
├── LESSONS.md          corrections become prevention rules, read at session start
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

- **New project.** It detects the stack and existing conventions, scaffolds the shared files, and fills the two project extensions with verified commands and decisions. Any unknown remains explicit.
- **Existing repo.** It compares against what is already there, preserves existing content, and separates shared coordination rules from project-specific policies before adapting the files.

From then on, work the way the files prescribe: get tasks approved before they are built, and let finished work flow into `team/TASK-HISTORY.md`.

---

## License

[MIT](LICENSE)
