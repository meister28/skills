"""Behavior checks for the team-workflow adoption validator."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))
from validate_workflow import validate  # noqa: E402


def destination(name):
    if not name.startswith("team-"):
        return Path(name)
    rest = name[len("team-"):]
    for folder in ("specs", "audit", "reviews"):
        if rest.startswith(folder + "-"):
            return Path("team") / folder / rest[len(folder) + 1:]
    return Path("team") / rest


def task_card(task_id="P-001", spec=""):
    return """### {task_id} — Export records

**Trigger:** Owner request on 2026-09-24.
**Approval:** Owner approved on 2026-09-24.
**Recommended worker:** Implementor — bounded feature.
**Type:** feature
**Summary:** Export selected records.
**Implementor:** Unassigned
**Created:** 2026-09-24
**Status:** Ready — implementation next.
**Acceptance:** Selected records appear in the export.
{spec}
""".format(task_id=task_id, spec=spec)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for source in (SKILL / "files").glob("*.md"):
            target = self.root / destination(source.name)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def tearDown(self):
        self.temp.cleanup()

    def messages(self, strict=False):
        return validate(self.root, strict)

    def test_fresh_template_has_no_errors_and_fenced_examples_are_ignored(self):
        issues = self.messages()
        self.assertFalse([item for item in issues if item.severity == "error"], issues)
        self.assertTrue(any("verification commands remain unconfigured" in item.message for item in issues))

    def test_missing_file_and_broken_link_are_errors(self):
        (self.root / "TEAM-PROJECT.md").unlink()
        issues = self.messages()
        self.assertTrue(any("required workflow file is missing" in item.message for item in issues))
        self.assertTrue(any("broken local link" in item.message for item in issues))

    def test_heading_links_are_checked_without_failing_on_heuristic_slug(self):
        agents = self.root / "AGENTS.md"
        agents.write_text(agents.read_text(encoding="utf-8") + "\n[valid](./AGENTS-PROJECT.md#verification) [bad](./AGENTS-PROJECT.md#missing-heading)\n", encoding="utf-8")
        issues = self.messages()
        self.assertTrue(any("heading anchor may be broken" in item.message and "missing-heading" in item.message for item in issues))
        self.assertFalse(any("heading anchor may be broken" in item.message and "#verification" in item.message for item in issues))

    def test_active_task_fields_status_and_spec_are_checked(self):
        queue = self.root / "team/TASKS.md"
        queue.write_text(queue.read_text(encoding="utf-8").replace(
            "No approved queued task.", task_card(spec="**Spec:** team/specs/missing.md").replace("**Acceptance:** Selected records appear in the export.\n", "**Acceptance:** \n").replace("**Status:** Ready", "**Status:** Suggested")
        ), encoding="utf-8")
        issues = self.messages()
        self.assertTrue(any("missing Acceptance" in item.message for item in issues))
        self.assertTrue(any("status disagrees" in item.message for item in issues))
        self.assertTrue(any("spec path does not exist" in item.message for item in issues))

    def test_completed_bug_requires_root_cause_in_strict_mode(self):
        history = self.root / "team/TASK-HISTORY.md"
        history.write_text(history.read_text(encoding="utf-8").replace("No completed tasks yet.", """### P-002 — Fix export

**Trigger:** Owner reported failure.
**Approval:** Owner request on 2026-09-24.
**Recommended worker:** Implementor — bounded fix.
**Type:** bug fix
**Summary:** Export works again.
**Implementor:** Codex
**Created:** 2026-09-24
**Acceptance:** Export succeeds.
**Completed by:** Codex
**Completed at:** 2026-09-24 12:00 UTC
**Verification:** Export check passed.
**Changed paths:** export module.
**Remaining uncertainty:** None.
**Fix:** Corrected export selection.
**Evidence:** Reproduced before and passed after.
**Regression risk:** Low.
"""), encoding="utf-8")
        soft = self.messages()
        hard = self.messages(strict=True)
        self.assertTrue(any("missing Root cause" in item.message and item.severity == "warning" for item in soft))
        self.assertTrue(any("missing Root cause" in item.message and item.severity == "error" for item in hard))

    def test_duplicate_id_is_an_error(self):
        queue = self.root / "team/TASKS.md"
        queue.write_text(queue.read_text(encoding="utf-8").replace("No approved queued task.", task_card() + task_card()), encoding="utf-8")
        self.assertTrue(any("duplicate task ID P-001" in item.message for item in self.messages()))

    def test_duplicate_id_across_queue_and_history_is_always_an_error(self):
        queue = self.root / "team/TASKS.md"
        history = self.root / "team/TASK-HISTORY.md"
        queue.write_text(queue.read_text(encoding="utf-8").replace("No approved queued task.", task_card()), encoding="utf-8")
        history.write_text(history.read_text(encoding="utf-8").replace("No completed tasks yet.", task_card()), encoding="utf-8")
        for strict in (False, True):
            self.assertTrue(any(item.severity == "error" and "duplicate task ID P-001" in item.message for item in self.messages(strict)))

    def test_suggested_authority_cannot_enter_ready_or_current_work(self):
        queue = self.root / "team/TASKS.md"
        original = queue.read_text(encoding="utf-8")
        for section, placeholder, status in (
            ("Ready", "No approved queued task.", "Ready"),
            ("Current work", "No current task.", "Current"),
        ):
            with self.subTest(section=section):
                card = task_card().replace("Owner approved on 2026-09-24.", "Suggested — review candidate.").replace("**Status:** Ready", "**Status:** " + status)
                queue.write_text(original.replace(placeholder, card), encoding="utf-8")
                self.assertTrue(any(item.severity == "error" and "Suggested approval" in item.message for item in self.messages()))

    def test_current_work_requires_an_assigned_implementor(self):
        queue = self.root / "team/TASKS.md"
        queue.write_text(queue.read_text(encoding="utf-8").replace("No current task.", task_card().replace("**Status:** Ready", "**Status:** Current")), encoding="utf-8")
        self.assertTrue(any("Current work requires an assigned Implementor" in item.message for item in self.messages()))

    def test_assigned_current_with_missing_acceptance_gate_is_valid(self):
        queue = self.root / "team/TASKS.md"
        card = task_card().replace("**Implementor:** Unassigned", "**Implementor:** Codex / Architect").replace(
            "**Status:** Ready — implementation next.",
            "**Status:** Current — base abc123; implemented; auth gate NOT RUN; prerequisite: credentials; next: owner supplies private session, architect runs wrapper check; evidence: service checks PASS."
        )
        queue.write_text(queue.read_text(encoding="utf-8").replace("No current task.", card), encoding="utf-8")
        self.assertFalse([item for item in self.messages() if item.severity == "error"])

    def test_crlf_validation_is_read_only_and_matches_lf(self):
        queue = self.root / "team/TASKS.md"
        queue.write_text(queue.read_text(encoding="utf-8").replace("No approved queued task.", task_card()), encoding="utf-8")
        lf_issues = self.messages()
        for path in self.root.rglob("*.md"):
            path.write_bytes(path.read_text(encoding="utf-8").replace("\n", "\r\n").encode("utf-8"))
        before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(lf_issues, self.messages())
        self.assertEqual(before, {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()})

    def test_shared_policy_leak_is_flagged_without_flagging_project_extension(self):
        shared = self.root / "AGENTS.md"
        shared.write_text(shared.read_text(encoding="utf-8") + "\n## 7. Storage rule (2026-09-24)\nRun `npm test` after changing `src/lib/store.ts`.\n", encoding="utf-8")
        extension = self.root / "AGENTS-PROJECT.md"
        extension.write_text(extension.read_text(encoding="utf-8") + "\nRun `npm test` after changing `src/lib/store.ts`.\n", encoding="utf-8")
        issues = self.messages()
        self.assertTrue(any("dated rule" in item.message for item in issues))
        self.assertTrue(any("stack command" in item.message for item in issues))
        self.assertTrue(any("source path" in item.message for item in issues))
        self.assertFalse(any(item.path == "AGENTS-PROJECT.md" and "may belong" in item.message for item in issues))

    def test_agreement_can_live_above_the_app_workflow(self):
        app = self.root / "app"
        app.mkdir()
        for name in ("AGENTS.md", "AGENTS-PROJECT.md", "CONTEXT.md", "CHANGELOG.md"):
            (self.root / name).replace(app / name)
        (self.root / "team").replace(app / "team")
        agents = app / "AGENTS.md"
        agents.write_text(agents.read_text(encoding="utf-8").replace("./TEAM.md", "../TEAM.md"), encoding="utf-8")
        team = self.root / "TEAM.md"
        team.write_text(team.read_text(encoding="utf-8").replace("./team/", "./app/team/").replace("./AGENTS.md", "./app/AGENTS.md").replace("./AGENTS-PROJECT.md", "./app/AGENTS-PROJECT.md"), encoding="utf-8")
        queue = app / "team/TASKS.md"
        queue.write_text(queue.read_text(encoding="utf-8").replace("../TEAM.md", "../../TEAM.md"), encoding="utf-8")
        issues = validate(app, agreement_root=self.root)
        self.assertFalse([item for item in issues if item.severity == "error"], issues)


if __name__ == "__main__":
    unittest.main()
