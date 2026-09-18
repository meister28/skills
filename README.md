# skills

A collection of [Agent Skills](https://agentskills.io) for AI coding agents —
the portable, per-project workflow I use when several agents (owner, a
CTO/Software Architect role, and Implementor/Software Engineer roles) build
and maintain the same codebase.

Inspired by and following the same shape as [mattpocock/skills](https://github.com/mattpocock/skills).
Skills live in `skills/<skill-name>/`, each with a `SKILL.md` and whatever
supporting files it needs.

## Skills

### [team-workflow](skills/team-workflow/)

Instantiate or upgrade a shared multi-agent working agreement in any project:

- **`TEAM.md`** — roles (owner / CTO-architect / implementor), the approval
  rule (`Suggested` must not be implemented; `Approved` may be), and the
  worker recommendation convention — with the model-cost idea made explicit:
  architect tasks prefer a frontier model, implementor tasks suit a
  cost-efficient one.
- **`AGENTS.md`** — eight binding rules: read the backlog first, changelog in
  the same commit, specs truthful in the same commit, prove it before you
  call it done, leave the tree as you found it, the project's single-door
  rule, no UI changes without approval, audits/reviews in `team/`, review
  candidates become tasks.
- **`team/`** — the task queue (`TASKS.md` with required fields), completed
  archive, and the `specs/`, `audit/`, `reviews/` folder contracts that make
  the file tree the communication channel between agents.

Two modes: **init** (detect the stack, fill the project slots, scaffold) and
**adoption** (diff against existing files, never overwrite without per-file
owner confirmation).

## Install

Copy or clone a skill into your agent's skills directory — for Claude Code
and most skill-compatible agents that is `~/.claude/skills/` (this collection
is developed against `~/.agents/skills/`; adjust to whatever your agent
reads):

```bash
# clone the whole collection
git clone https://github.com/rachidis/skills.git
cp -r skills/skills/team-workflow ~/.claude/skills/

# or, without cloning, just the one skill (sparse checkout)
git clone --depth 1 --filter=blob:none --sparse https://github.com/rachidis/skills.git
cd skills && git sparse-checkout set skills/team-workflow
cp -r skills/team-workflow ~/.claude/skills/
```

Or symlink so updates propagate: clone the repo anywhere and
`ln -s /path/to/skills/skills/team-workflow ~/.claude/skills/team-workflow`.

Then invoke it inside a project with `/team-workflow` (or your agent's
equivalent skill invocation).

## The back-port loop

Every project scaffolded by `team-workflow` carries a "Canonical template"
pointer in its `AGENTS.md`: changes to the working agreement must be
back-ported to the skill's `templates` in the same session. This repo is the
canonical home — improve skills here, and every future project inherits the
improvement.

## License

[MIT](LICENSE)
