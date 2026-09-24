---
name: team-workflow
description: "Set up or adapt a shared, repository-based workflow for people and coding agents: approval, task handoff, specs, lessons, and change records."
disable-model-invocation: true
---

# Team workflow

Use the files in `files/` to give contributors one durable place for decisions,
approved work, and handoff. The shared files are stack-neutral. Project facts
and additional policies belong in `AGENTS-PROJECT.md` and `TEAM-PROJECT.md`.

## Choose the workflow root

Prefer the repository root so every contributor finds `AGENTS.md`. In a
monorepo, choose one shared root or a package root deliberately; if the
workflow lives below the repository root, add a short root `AGENTS.md`
pointer without overwriting an existing one. Keep template links relative to
the chosen workflow root.

## New project

1. Inspect the repository and owner request. Identify existing docs, task
   tracking, verification commands, and contributor instructions. Do not
   infer policies from a technology or example.
2. Copy the shared files to the workflow root and the `team/` folder.
   Copy both project extension stubs. Create the glossary and changelog only
   where there is no established equivalent; otherwise retarget links to the
   existing document. Map flattened template names
   to their destinations: `team-TASKS.md` becomes `team/TASKS.md`, and
   `team-specs-README.md` becomes `team/specs/README.md`, for example.
3. Fill only verified project facts in the extension files: existing doc
   locations, actual verification commands and working directory, role
   preferences, and approved extra rules. Leave unknowns explicit.
4. Enter owner-approved work in `team/TASKS.md`. Agent proposals start
   Suggested; a direct owner request approves only its stated scope.
5. Check that every local link resolves and that the chosen commands work.
   Report what was created, what remains unconfigured, and any existing
   convention that the workflow must respect.

## Existing project

Inventory the current workflow and compare each file with the template.
Preserve existing content and unrelated edits. Merge shared coordination
rules where useful; move project-specific commands, paths, invariants, and
dated decisions to the extension files without losing them. A direct owner
request to adopt or revise the workflow authorizes that scope. Ask for a
decision only when competing existing policies cannot be reconciled from
the request and repository evidence. Verify links and task records after
the change.

## Template map

- `files/AGENTS.md` and `files/TEAM.md`: shared contributor rules and
  coordination.
- `files/AGENTS-PROJECT.md` and `files/TEAM-PROJECT.md`: empty
  customization stubs, maintained by each project.
- `files/team-TASKS.md`, `files/team-TASK-HISTORY.md`, and
  `files/team-LESSONS.md`: active queue, completed records, and lessons.
- `files/team-specs-README.md`, `files/team-audit-README.md`, and
  `files/team-reviews-README.md`: folder contracts.
- `files/CONTEXT.md` and `files/CHANGELOG.md`: project glossary
  and change record stubs.

Do not add a universal persistence module, fixture clock, browser gate,
UI policy, test command, or rule date. If a project needs one, record it in
its project extension with its rationale and how to verify it. Keep the
public template free of any adopting project's decisions.
