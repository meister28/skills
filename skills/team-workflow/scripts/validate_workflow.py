#!/usr/bin/env python3
"""Check an adopted team-workflow without inspecting the project's code stack."""

import argparse
from datetime import date
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
from urllib.parse import unquote, urlsplit


REQUIRED_PROJECT_FILES = (
    "AGENTS.md",
    "AGENTS-PROJECT.md",
    "team/TASKS.md",
    "team/TASK-HISTORY.md",
    "team/LESSONS.md",
)
RECOMMENDED_FILES = (
    "team/specs/README.md",
    "team/audit/README.md",
    "team/reviews/README.md",
)
REQUIRED_AGREEMENT_FILES = ("TEAM.md", "TEAM-PROJECT.md")
OPEN_FIELDS = (
    "Trigger", "Approval", "Recommended worker", "Type", "Summary",
    "Implementor", "Created", "Status", "Acceptance",
)
HISTORY_FIELDS = (
    "Trigger", "Approval", "Recommended worker", "Type", "Summary",
    "Implementor", "Created", "Acceptance", "Completed by", "Completed at",
    "Verification", "Changed paths", "Remaining uncertainty",
)
TYPE_FIELDS = {
    "bug fix": ("Root cause", "Fix", "Evidence", "Regression risk"),
    "feature": ("Design", "What changed", "Evidence"),
    "refactor": ("Design", "What changed", "Evidence"),
    "instrument": ("Method", "What landed", "Evidence"),
    "playtest": ("Method", "What landed", "Evidence"),
    "audit": ("Method", "Findings", "Verdict", "Recommendation"),
    "consultation": ("Method", "Findings", "Verdict", "Recommendation"),
    "design": ("Decisions", "Alternatives", "Recommendation"),
    "architecture review": ("Decisions", "Alternatives", "Recommendation"),
    "plan": ("Decisions", "Alternatives", "Recommendation"),
    "docs": ("What changed", "Syncs"),
    "infrastructure": ("Change", "Verification", "Rollback or recovery path"),
}

LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^)]+)\)")
FIELD = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$")
HEADING = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
TASK_ID = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*-\d+)\s*(?:[-–—:]|$)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
DATED_RULE = re.compile(r"^\s*#{2,4}\s+(?:\d+\.\s*)?.*\(20\d\d-\d\d-\d\d\)")
STACK_COMMAND = re.compile(
    r"\b(?:npm|npx|pnpm|yarn|bun|pytest|mypy|cargo|flutter|gradle|"
    r"dotnet|mvn)\s+(?:test|run|build|check|lint|typecheck|verify|assemble)\b"
)
SOURCE_PATH = re.compile(
    r"(?<![\w/])(?:src|lib|scripts|packages)/[\w./-]+"
)


@dataclass(frozen=True)
class Issue:
    severity: str
    path: str
    line: int
    message: str


@dataclass
class Record:
    task_id: str
    section: str
    line: int
    fields: dict


def visible_lines(text: str) -> List[str]:
    """Blank fenced examples while preserving line numbers."""
    result = []
    marker = None
    length = 0
    for line in text.splitlines():
        fence = FENCE.match(line)
        if marker is None and fence:
            marker, length = fence.group(1)[0], len(fence.group(1))
            result.append("")
        elif marker is not None:
            if fence and fence.group(1)[0] == marker and len(fence.group(1)) >= length:
                marker = None
            result.append("")
        else:
            result.append(line)
    return result


def read_lines(path: Path) -> List[str]:
    return visible_lines(path.read_text(encoding="utf-8-sig"))


def display_path(path: Path, root: Path) -> str:
    return Path(os.path.relpath(path, root)).as_posix()


def workflow_docs(root: Path, agreement_root: Path) -> List[Path]:
    files = [
        root / name
        for name in ("AGENTS.md", "AGENTS-PROJECT.md", "CONTEXT.md", "CHANGELOG.md")
    ]
    files.extend(agreement_root / name for name in REQUIRED_AGREEMENT_FILES)
    team = root / "team"
    if team.is_dir():
        files.extend(sorted(team.rglob("*.md")))
    return [path for path in files if path.is_file()]


def parse_records(path: Path) -> List[Record]:
    records = []
    section = ""
    current = None
    for number, line in enumerate(read_lines(path), 1):
        heading = HEADING.match(line)
        if heading and len(heading.group(1)) == 2:
            section = heading.group(2).lower()
            current = None
        elif heading and len(heading.group(1)) == 3:
            task = TASK_ID.match(heading.group(2))
            current = Record(task.group(1), section, number, {}) if task else None
            if current:
                records.append(current)
        elif current:
            field = FIELD.match(line)
            if field:
                current.fields[field.group(1).strip().lower()] = field.group(2).strip()
    return records


def heading_anchors(path: Path) -> set:
    anchors = set()
    counts = {}
    for line in read_lines(path):
        heading = re.match(r"^\s*#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        plain = re.sub(r"<[^>]+>|[`*_~]", "", heading.group(1)).lower()
        slug = re.sub(r"[^\w\s-]", "", plain)
        slug = re.sub(r"\s+", "-", slug.strip())
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug if count == 0 else "{}-{}".format(slug, count))
    return anchors


def check_links(root: Path, agreement_root: Path, issues: List[Issue]) -> None:
    for path in workflow_docs(root, agreement_root):
        relative = display_path(path, root)
        for number, line in enumerate(read_lines(path), 1):
            for match in LINK.finditer(line):
                target = match.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                else:
                    target = target.split(" ", 1)[0]
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not (parsed.path or parsed.fragment):
                    continue
                # A leading slash denotes the repository/agreement root.
                if not parsed.path:
                    local = path
                elif parsed.path.startswith("/"):
                    local = agreement_root / unquote(parsed.path.lstrip("/"))
                else:
                    local = path.parent / unquote(parsed.path)
                if not local.exists():
                    issues.append(Issue("error", relative, number, "broken local link: " + target))
                elif parsed.fragment and local.is_file() and local.suffix.lower() == ".md":
                    anchor = unquote(parsed.fragment).lower()
                    if anchor not in heading_anchors(local):
                        issues.append(Issue("warning", relative, number, "heading anchor may be broken: " + target))


def check_boundaries(root: Path, agreement_root: Path, issues: List[Issue]) -> None:
    for path, pointer in ((root / "AGENTS.md", "AGENTS-PROJECT.md"), (agreement_root / "TEAM.md", "TEAM-PROJECT.md")):
        if not path.is_file():
            continue
        name = display_path(path, root)
        lines = read_lines(path)
        if pointer not in "\n".join(lines):
            issues.append(Issue("error", name, 1, "shared document does not point to " + pointer))
        for number, line in enumerate(lines, 1):
            if DATED_RULE.search(line):
                issues.append(Issue("warning", name, number, "dated rule may belong in the project extension"))
            if STACK_COMMAND.search(line):
                issues.append(Issue("warning", name, number, "stack command may belong in the project extension"))
            if SOURCE_PATH.search(line):
                issues.append(Issue("warning", name, number, "source path may belong in the project extension"))
    project = root / "AGENTS-PROJECT.md"
    if project.is_file() and "No project-specific commands recorded yet" in project.read_text(encoding="utf-8-sig"):
        issues.append(Issue("warning", "AGENTS-PROJECT.md", 1, "verification commands remain unconfigured"))


def check_records(root: Path, issues: List[Issue], strict_history: bool) -> None:
    queue = root / "team/TASKS.md"
    history = root / "team/TASK-HISTORY.md"
    seen = {}
    extension = root / "AGENTS-PROJECT.md"
    extension_text = extension.read_text(encoding="utf-8-sig").lower() if extension.is_file() else ""
    for path, completed in ((queue, False), (history, True)):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        severity = "error" if not completed or strict_history else "warning"
        for record in parse_records(path):
            if record.task_id in seen:
                issues.append(Issue("error", relative, record.line, "duplicate task ID " + record.task_id + " (also in " + seen[record.task_id] + ")"))
            else:
                seen[record.task_id] = relative
            missing = [field for field in (HISTORY_FIELDS if completed else OPEN_FIELDS) if not record.fields.get(field.lower())]
            for field in ("Created", "Completed at") if completed else ("Created",):
                value = record.fields.get(field.lower(), "")
                if value:
                    try:
                        date.fromisoformat(value[:10])
                    except ValueError:
                        issues.append(Issue(severity, relative, record.line, record.task_id + " has invalid " + field + " date"))
            spec = record.fields.get("spec", "").strip("` ")
            if spec and spec.lower() not in ("none", "n/a") and not spec.startswith("["):
                if not (root / spec).exists() and not (path.parent / spec).exists():
                    issues.append(Issue(severity, relative, record.line, record.task_id + " spec path does not exist: " + spec))
            task_type = record.fields.get("type", "").lower()
            if task_type and task_type not in TYPE_FIELDS and task_type not in extension_text:
                issues.append(Issue(severity, relative, record.line, record.task_id + " has undefined type: " + task_type))
            if completed:
                for field in TYPE_FIELDS.get(task_type, ()):
                    if field == "Rollback or recovery path" and any(record.fields.get(key) for key in ("rollback", "recovery", "rollback or recovery path")):
                        continue
                    if field == "Recommendation" and record.fields.get("next step"):
                        continue
                    if not record.fields.get(field.lower()):
                        missing.append(field + " detail")
                if record.fields.get("status"):
                    issues.append(Issue(severity, relative, record.line, record.task_id + " still has an open Status field"))
            else:
                expected = next((key for key in ("current work", "ready", "suggested", "deferred") if record.section.startswith(key)), None)
                status = record.fields.get("status", "").lower()
                if expected and status and not status.startswith("current" if expected == "current work" else expected):
                    issues.append(Issue("error", relative, record.line, record.task_id + " status disagrees with " + expected + " section"))
                if expected == "suggested" and record.fields.get("approval", "").lower().startswith("approved"):
                    issues.append(Issue("error", relative, record.line, record.task_id + " is approved but remains Suggested"))
            if missing:
                issues.append(Issue(severity, relative, record.line, record.task_id + " missing " + ", ".join(missing)))


def validate(root: Path, strict_history: bool = False, agreement_root: Optional[Path] = None) -> List[Issue]:
    root = root.resolve()
    agreement_root = agreement_root.resolve() if agreement_root else root
    issues = []
    for name in REQUIRED_PROJECT_FILES:
        if not (root / name).is_file():
            issues.append(Issue("error", name, 1, "required workflow file is missing"))
    for name in REQUIRED_AGREEMENT_FILES:
        if not (agreement_root / name).is_file():
            issues.append(Issue("error", display_path(agreement_root / name, root), 1, "required workflow file is missing"))
    for name in RECOMMENDED_FILES:
        if not (root / name).is_file():
            issues.append(Issue("warning", name, 1, "recommended folder guide is missing"))
    check_links(root, agreement_root, issues)
    check_boundaries(root, agreement_root, issues)
    check_records(root, issues, strict_history)
    return sorted(issues, key=lambda item: (item.path, item.line, item.severity, item.message))


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path, help="adopted workflow root (default: current directory)")
    parser.add_argument("--agreement-root", type=Path, help="directory holding TEAM.md when separate from AGENTS.md")
    parser.add_argument("--strict-history", action="store_true", help="treat missing fields in older completed records as errors")
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error("workflow root is not a directory: " + str(args.root))
    if args.agreement_root and not args.agreement_root.is_dir():
        parser.error("agreement root is not a directory: " + str(args.agreement_root))
    issues = validate(args.root, args.strict_history, args.agreement_root)
    for item in issues:
        print("{}:{}: {}: {}".format(item.path, item.line, item.severity, item.message))
    errors = sum(item.severity == "error" for item in issues)
    warnings = sum(item.severity == "warning" for item in issues)
    print("team-workflow: {} error(s), {} warning(s)".format(errors, warnings))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
