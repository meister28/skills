# Update an existing workflow

Use when the project already has some or all workflow files, even when it
predates the shared/project split or has no recorded version. This is the
update branch of team-workflow, not a second skill.

## Establish source and local changes

1. Read repository-root instructions, Git status and the existing working
   agreement. Locate the actual queue, archive, project policies and any
   package-root routing; preserve split roots and equivalent documents.
2. Identify the target from the available skill source and the owner's request.
   Pin a commit/version; for an unversioned or modified source record a content
   digest/snapshot identifier for the full skill package and its path. A dirty
   checkout needs both its base commit and that digest so two local revisions
   are distinguishable; HEAD alone does not identify its content. Requesting latest published
   permits resolving upstream; ordinary continuation does not require networking.
3. Read TEAM-PROJECT.md's adoption receipt if available. Compare old upstream,
   current project and target upstream when the old source is accessible. This
   distinguishes upstream changes from project customizations. If the old source
   is unknown/unavailable, inventory current rules and use a conservative merge;
   label the comparison limit. Do not classify an unversioned workflow as empty.

## Merge the workflow, not the project history

4. Apply new shared guidance to the actual AGENTS/TEAM locations. Preserve
   existing project policy and approved exceptions; move local rules into the
   project extensions only with their meaning and links intact. For older
   combined files, separate shared rules from local policy instead of replacing
   the entire file. Keep project safeguards that are stricter than the template.
5. Create missing stubs/folder contracts only where there is no equivalent.
   Update pointers to existing glossary, changelog and specs; use the flattened
   template map only to establish destinations, never to replace live queues.
   Preserve task IDs, approvals, owners, history, lessons, dates and existing
   changelog entries. Add the upgrade's own record in the project's existing
   process. Older records keep their original attribution and schema.
6. Introduce the agent registry for future work. Register the updating agent
   with its confirmed name/settings, asking the owner for any missing values.
   Pending answers remain explicit. An occupied task keeps
   its existing owner; add a mapping only when that identity is established,
   rather than assigning it to the updater. Matching model settings alone do
   not establish that two sessions are the same worker.
7. Resolve routine differences within the owner's update scope. If two binding
   policies conflict and the request does not settle them, prepare the compatible
   changes and document the specific decision needed. Preserve the local policy
   meanwhile; do not silently weaken it or mark the whole upgrade adopted.

## Verify and record adoption

8. Run the read-only workflow validator against the real workflow root, with
   `--agreement-root` for a separate agreement. Check links and inspect the diff
   for lost policy, overwritten records or unrelated edits. Compare pre/post
   archive and existing lesson content; intentional active-card corrections
   must preserve actual authority and ownership. Review legacy warnings rather
   than rewriting history to make them disappear.
9. When the update is complete, record target source, revision/digest, roots,
   file mappings/intentional overrides, date, named updater and evidence in
   TEAM-PROJECT.md. Keep installed-copy verification separate and explicit.
   If verification or a policy decision remains open, retain the old adopted
   revision and record pending work and the exact next action.

Report old baseline (or unknown), target, changes, preserved customizations,
checks and remaining limits. A second invocation with the same source should
validate without duplicate rules, registry entries or redundant change records.
Commit, push or installed-skill updates follow the owner's requested scope.
