# team-workflow

A shared, file-based working agreement for people and coding agents. It
coordinates approval, task handoff, specifications, reviews, lessons, and
change records across sessions and agents. It makes no assumption about a
project's language, framework, storage, UI, or test runner.

The skill lives in [skills/team-workflow](skills/team-workflow/) and follows
the [Agent Skills](https://agentskills.io) format.

## How it works

1. The owner requests work or approves a task. Agent proposals start
   Suggested; only Approved tasks and direct owner requests authorize
   implementation of their stated scope.
2. Contributors record current work and its next step in `team/TASKS.md`.
   A linked specification carries decisions another agent needs to
   implement the task.
3. A contributor verifies the change and updates the changelog and affected
   documents in the same commit.
4. The completed task moves to `team/TASK-HISTORY.md` with its result,
   evidence, contributor, and completion time. Corrections enter
   `team/LESSONS.md`.

The queue and files carry the handoff, so the owner does not need to relay
technical context between agents. Role recommendations help route work but
never approve or assign it.

## Shared rules and project extensions

The reusable agreement is in `AGENTS.md` and `TEAM.md`. Each project also
gets `AGENTS-PROJECT.md` and `TEAM-PROJECT.md`. Those two files start as
stubs and hold that repository's verified commands, document locations,
agent preferences, architectural invariants, and dated decisions.

For example, a storage boundary or clock-fixture rule belongs in a project's
extension if that project actually has it. The public template does not
impose either rule, or any UI or browser gate, on unrelated codebases.
Project policies can change without editing the shared agreement.

```text
AGENTS.md                 shared contributor rules
AGENTS-PROJECT.md         project policies and verification commands
TEAM.md                   shared roles, approval, and handoff
TEAM-PROJECT.md           project staffing and operating decisions
CHANGELOG.md              same-commit change record
CONTEXT.md                project vocabulary
team/
  TASKS.md                active and suggested work
  TASK-HISTORY.md         completed work and evidence
  LESSONS.md              corrections and prevention rules
  specs/README.md         specification folder contract
  audit/README.md         audit folder contract
  reviews/README.md       review folder contract
```

The files under `skills/team-workflow/files/` are source templates. The
skill chooses a workflow root, copies the files there, and fills only
project facts supported by the repository or the owner. Existing projects
are compared file by file; their content is preserved while reusable rules
and project extensions are adopted.

## Install and use

Clone this repository and copy or link `skills/team-workflow/` into the
skills directory your coding agent reads.

```sh
git clone https://github.com/meister28/skills.git
cp -R skills/skills/team-workflow ~/.agents/skills/team-workflow
```

Your agent may use a different skill directory. Invoke `team-workflow`
inside the target repository and ask it to initialize or adapt the workflow.
For an existing repository, tell it which documents and rules already
govern the project.

## Boundaries

The template supplies coordination, not product policy. It does not invent
verification commands, require a particular architecture, or overwrite an
existing workflow. A project's additional rules belong in its extension
files and should state why they apply and how to verify them.

## License

[MIT](LICENSE)
