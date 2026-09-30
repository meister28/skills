"""Dependency-free checks for this local batch; not a full YAML validator."""

import hashlib
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "skills/team-workflow/scripts"))
from validate_workflow import validate, visible_lines  # noqa: E402


def main():
    skills = [ROOT / "skills/team-workflow", Path(__file__).parent / "web-app-engineering"]
    for skill in skills:
        text = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
        header = text.split("---", 2)
        assert text.startswith("---\n") and len(header) == 3, skill
        fields = dict(line.split(":", 1) for line in header[1].strip().splitlines())
        name = fields["name"].strip()
        description = fields["description"].strip().strip('"')
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64, name
        assert name == skill.name and 0 < len(description) <= 1024, skill
        print("PASS limited scalar frontmatter:", name)

    docs = [ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "proposals/2026-09-30/DECISION.md", skills[0] / "SKILL.md"]
    docs.extend(Path(__file__).parent.rglob("*.md"))
    links = 0
    for path in docs:
        for line in visible_lines(path.read_text(encoding="utf-8-sig")):
            assert line.rstrip() == line, (path, "trailing whitespace")
            for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)", line):
                parsed = urlsplit(target.strip("<>"))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                local = path.parent / unquote(parsed.path)
                assert local.exists(), (path, target)
                links += 1
    print("PASS local package/document links:", links)

    with tempfile.TemporaryDirectory() as directory:
        adoption = Path(directory)
        for source in (skills[0] / "files").glob("*.md"):
            name = source.name
            if name.startswith("team-"):
                name = "team/" + name[5:]
                for folder in ("specs", "audit", "reviews"):
                    name = name.replace("team/" + folder + "-", "team/" + folder + "/")
            target = adoption / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        before = {p: p.read_bytes() for p in adoption.rglob("*") if p.is_file()}
        issues = validate(adoption, strict_history=True)
        assert not [issue for issue in issues if issue.severity == "error"], issues
        assert before == {p: p.read_bytes() for p in adoption.rglob("*") if p.is_file()}
        print("PASS fresh strict adoption, read-only; warnings:", [issue.message for issue in issues])

    print("Candidate SHA-256 (UTF-8 with normalized LF):")
    for skill in skills:
        paths = [skill / "SKILL.md"]
        paths.extend(sorted((skill / ("files" if skill == skills[0] else "references")).glob("*.md")))
        for path in paths:
            content = path.read_text(encoding="utf-8-sig").encode("utf-8")
            print(hashlib.sha256(content).hexdigest(), path.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
