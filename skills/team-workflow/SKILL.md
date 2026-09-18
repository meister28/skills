---
name: team-workflow
description: Instantiate or upgrade the shared multi-agent workflow (TEAM.md roles and approval rule, AGENTS.md binding rules, team/ task queue with specs/audits/reviews) in any project. Use when starting a new project that several AI agents will work on together, or when importing the workflow into an existing repository.
disable-model-invocation: true
---

# Team workflow — instantiate or upgrade the multi-agent working agreement

One canonical workflow, instantiated per project. The template files in
`files/` next to this SKILL.md are **generalized** from a battle-tested
production setup: role definitions and the approval rule for `TEAM.md`,
eight binding agent rules for `AGENTS.md` (the rule-5 slot is deliberately
left empty — it must be derived from the target codebase), the task-queue
conventions for `team/WORKFLOW.md`, and skeletons for the queue, archive,
glossary, and changelog.

The workflow's value is coordination between agents: a `team/TASKS.md`
queue with approval states, specs as the inter-agent communication channel,
and rules that keep documentation truthful in the same commit as code.
Project-specific detail lives in clearly marked slots, not in the template.

## Mode selection

Start by inspecting the target project root:

- **Empty or no AGENTS.md / TEAM.md / team/** → **Mode A: init** (full scaffold).
- **Some workflow files already exist** → **Mode B: upgrade/adopt** — never
  overwrite. Read each existing file fully, present a per-file decision
  (adopt template / keep project version / merge), and get explicit owner
  confirmation per file before writing anything. Structural merges
  (e.g. adding missing `team/` subfolders, adding missing rule sections)
  are safe to propose; content overwrites are not.
- If the owner asks for a diff review first, produce a per-file report
  (exists? / differs how? / recommendation) before any write.

## Mode A — init

1. **Detect the stack.** Look at package.json / lockfiles / config files
   (tsconfig, vite, pytest, cargo, go.mod, requirements.txt…). Record:
   language, framework, package manager, test runner, typechecker, linter,
   build command, dev command, and the repo layout (monorepo? app root?).
2. **Fill the project slots in the templates** (each is marked `<!-- SLOT -->`
   or `${PROJECT}`):
   - `AGENTS.md` rule 3 (prove-it): substitute the real commands —
     e.g. `npm test`, `npx tsc -b`, `npx eslint src` for a TS/Vite app;
     `pytest` + `mypy` for Python; `cargo test` + `cargo clippy` for Rust.
     If the project has no typechecker or linter, rewrite the rule around
     the test runner and say so honestly.
   - `AGENTS.md` rule 5 slot: write the project's equivalent "single door"
     rule only if the codebase has such a module (a storage/db/api boundary);
     otherwise replace the rule with the strongest true invariant you can
     verify, or delete the rule and renumber only if the owner approves
     (rule numbers are cited by other rules — prefer marking it N/A).
   - Rule 2's doc list: keep only the spec docs that exist or that the
     owner wants (PRODUCT-SPECS / ARCHITECTURE-SPECS / HANDOFF / CONTEXT).
   - TEAM.md / WORKFLOW.md: fill project name, app root path, and any
     stack-specific conventions.
3. **Create the files** (never overwrite — if a target exists, that file
   goes through the Mode B decision even inside an init):
   - Root: `TEAM.md`, `AGENTS.md`, `CONTEXT.md`, `CHANGELOG.md`
   - `team/`: `TASKS.md`, `TASK-HISTORY.md`, `WORKFLOW.md`, `specs/README.md`,
     `audit/README.md`, `reviews/README.md`
   - Where they live depends on repo layout: monorepo with one app → put
     workflow docs at the app root (as this repo does) or repo root, then
     **record the choice in TEAM.md** so agents look in the right place.
4. **Bootstrap the queue** with the owner's current asks, if any, as the
   first entries (fields per WORKFLOW.md: Approval, Status, Recommended
   worker, acceptance).
5. **Verify truthfulness**: every path a doc references must exist at the
   end of init; fix or remove references that don't resolve (rule 2's core
   principle applies to the workflow docs themselves).
6. **Install the canonical-template pointer**: append a short "Canonical
   template" section to the project's `AGENTS.md`, naming this skill's
   location (`~/.agents/skills/team-workflow`) and instructing agents to
   back-port future changes to this agreement into the skill's `files/`
   templates in the same session. This is what makes workflow improvements
   propagate to every project instead of diverging per repo.
7. Report: what was created, the filled slots, and the two decisions the
   owner should validate (rule 5 treatment; doc set for rule 2).

## Mode B — upgrade/adopt

1. Inventory which workflow files exist and read them.
2. Produce a table: file → exists? → differs from template how? →
   recommendation (adopt / keep / merge) with reasoning.
3. No writes until the owner confirms the plan per file.
4. After writing, verify references resolve and report.

## Files

- `files/TEAM.md` — roles, approval rule, worker recommendation
- `files/AGENTS.md` — the binding rules (generalized; project slots marked)
- `files/team-WORKFLOW.md` — the one-page quick reference
- `files/team-TASKS.md`, `files/team-TASK-HISTORY.md` — queue + archive skeletons
- `files/CONTEXT.md`, `files/CHANGELOG.md` — glossary and changelog stubs
- `files/team-specs-README.md`, `files/team-audit-README.md`,
  `files/team-reviews-README.md` — folder READMEs explaining each folder's
  contract (what goes in, naming, when)
- `files/TEMPLATE-POINTER.md` — the "Canonical template" section appended
  to a project's AGENTS.md at init, so workflow changes back-port to this
  skill instead of diverging per repo

## Boundaries

- Never overwrite existing content without an explicit per-file owner
  decision (Mode B).
- Never invent project-specific rules that aren't verifiable in the
  codebase; mark slots honestly when there is nothing to say.
- Rule numbers are load-bearing (rules cite each other); when a rule must
  be dropped, mark it N/A with a reason rather than renumbering, unless
  the owner approves renumbering.
