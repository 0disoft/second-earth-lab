#!/usr/bin/env python3
"""Validate Markdown docs: internal links, README line counts, CRLF detection,
banned claim phrases, README document-map completeness."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

# Documents that must appear in the README Document Map table.
CORE_DOCS = {
    "SUMMARY.md",
    "framework.md",
    "docs/methodology/lock-in-score.md",
    "case-e7-visa.md",
    "case-platform-suspension.md",
    "case-medical-lock-in.md",
    "case-care-lock-in.md",
    "case-education-lock-in.md",
    "chapter-national-kernel.md",
    "chapter-war-kernel.md",
    "appendix-coercion-paradox.md",
    "case-template.md",
}

# Phrases that overclaim framework universality or proof.
# Case-insensitive match. These should not appear in any .md file
# (except validate_docs.py itself).
BANNED_CLAIM_PHRASES = [
    "universality confirmed",
    "final universality confirmation",
    "framework universality verification",
    "what was validated",
    "is proven",
    "proven across five cases",
    "validated the framework",
    "demonstrates the framework's universality",
]


def markdown_files() -> list[Path]:
    return sorted(
        p
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.is_file()
    )


def slugify_heading(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`*_~\[\]()>#]", "", text)
    text = re.sub(r"[^a-z0-9가-힣\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def collect_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*$", line)
        if not match:
            continue
        base = slugify_heading(match.group(2))
        counts[base] = counts.get(base, 0) + 1
        anchor = base if counts[base] == 1 else f"{base}-{counts[base] - 1}"
        anchors.add(anchor)
    return anchors


def check_crlf(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        data = path.read_bytes()
        if b"\r\n" in data:
            errors.append(f"CRLF detected: {path.relative_to(ROOT)}")
    return errors


def check_internal_links(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    anchors_by_file = {path: collect_anchors(path) for path in paths}

    for path in paths:
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)", text):
            raw_link = match.group(1).split()[0]
            if raw_link.startswith(("http://", "https://", "mailto:")):
                continue

            target_part, _, anchor = raw_link.partition("#")
            if target_part == "":
                target = path
            else:
                target = (path.parent / target_part).resolve()

            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"Link points outside repo: {path.relative_to(ROOT)} -> {raw_link}"
                )
                continue

            if not target.exists():
                errors.append(
                    f"Missing linked file: {path.relative_to(ROOT)} -> {raw_link}"
                )
                continue

            if anchor and target.suffix == ".md":
                target_path = target.relative_to(ROOT)
                actual_path = ROOT / target_path
                if anchor not in anchors_by_file.get(actual_path, set()):
                    errors.append(
                        f"Missing anchor: {path.relative_to(ROOT)} -> {raw_link}"
                    )

    return errors


def check_readme_line_counts() -> list[str]:
    if not README.exists():
        return ["README.md not found"]

    errors: list[str] = []
    text = README.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.startswith("| ["):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 3:
            continue
        link_match = re.search(r"\(([^)]+)\)", parts[0])
        if not link_match:
            continue
        try:
            stated = int(parts[1].replace(",", ""))
        except ValueError:
            continue
        relative_path = link_match.group(1).lstrip("./")
        target = ROOT / relative_path
        if not target.exists():
            continue
        actual = len(target.read_text(encoding="utf-8").splitlines())
        if actual != stated:
            errors.append(
                f"README line count mismatch: {relative_path} states {stated}, actual {actual}"
            )
    return errors


def check_readme_completeness() -> list[str]:
    """Check that all CORE_DOCS appear in the README Document Map."""
    if not README.exists():
        return ["README.md not found"]

    errors: list[str] = []
    text = README.read_text(encoding="utf-8")

    for doc in CORE_DOCS:
        # Verify README contains a markdown link to this doc
        if f"]({doc})" not in text and f"](./{doc})" not in text:
            errors.append(
                f"README completeness: {doc} is missing from the Document Map"
            )
    return errors


def check_banned_phrases(paths: list[Path]) -> list[str]:
    """Check that no banned overclaiming phrases appear in markdown files."""
    errors: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8").lower()
        for phrase in BANNED_CLAIM_PHRASES:
            if phrase.lower() in text:
                # Find line number
                for i, line in enumerate(
                    path.read_text(encoding="utf-8").splitlines(), 1
                ):
                    if phrase.lower() in line.lower():
                        errors.append(
                            f"Banned phrase '{phrase}' in {path.relative_to(ROOT)}:{i}"
                        )
    return errors


def main() -> int:
    paths = markdown_files()
    errors: list[str] = []
    errors.extend(check_crlf(paths))
    errors.extend(check_internal_links(paths))
    errors.extend(check_readme_line_counts())
    errors.extend(check_readme_completeness())
    errors.extend(check_banned_phrases(paths))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
