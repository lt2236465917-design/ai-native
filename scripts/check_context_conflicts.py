#!/usr/bin/env python3
"""Detect contradictory context/artifact files and obvious secret leakage."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from _common import iter_files, parse_frontmatter


SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"(?i)\b(?:password|passwd|secret|api[_-]?key)\s*[:=]\s*['\"]?[^<\s][^\n]*"),
]


def inspect(root: Path) -> list[str]:
    errors: list[str] = []
    ids: dict[str, list[tuple[Path, str, str]]] = defaultdict(list)
    for path in iter_files(root, (".md", ".json", ".yml", ".yaml")):
        text = path.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path}: possible secret or credential pattern; remove/redact it")
        if "<<<<<<<" in text or "=======" in text or ">>>>>>>" in text:
            errors.append(f"{path}: unresolved merge conflict marker")
        if path.suffix == ".md":
            # Ordinary context prose need not have frontmatter; artifact files do.
            if text.lstrip().startswith("---"):
                fields, _, parse_errors = parse_frontmatter(path)
                errors.extend(parse_errors)
                artifact_id = fields.get("id")
                if artifact_id:
                    ids[artifact_id].append((path, fields.get("status", ""), fields.get("decision", "")))

    for artifact_id, entries in sorted(ids.items()):
        if len(entries) < 2:
            continue
        locations = ", ".join(str(item[0]) for item in entries)
        errors.append(f"duplicate artifact id {artifact_id!r} in {locations}")
        statuses = {item[1] for item in entries if item[1]}
        decisions = {item[2] for item in entries if item[2]}
        if len(statuses) > 1 or len(decisions) > 1:
            errors.append(f"artifact id {artifact_id!r} has contradictory status/decision values")

    # A shared context should have one canonical declaration, not competing ones.
    canonical_declarations: list[Path] = []
    for path in iter_files(root, (".md",)):
        text = path.read_text(encoding="utf-8").lower()
        if "canonical" in text and "agents.md" in text:
            canonical_declarations.append(path)
    if len(canonical_declarations) > 1:
        # Multiple references are fine; multiple *files named as canonical* are not.
        named = [p for p in canonical_declarations if p.name.lower() in {"agents.md", "project_context.md", "ai_context.md"}]
        if len(named) > 1:
            errors.append("multiple files claim to be the canonical engineering context: " + ", ".join(map(str, named)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--expect-fail", action="store_true", help="Return success when at least one conflict is found")
    args = parser.parse_args()
    errors = inspect(args.root)
    if args.expect_fail:
        if not errors:
            print(f"FAIL: expected a conflict in {args.root}, but none was found")
            return 1
        print(f"PASS: negative fixture detected {len(errors)} issue(s) in {args.root}")
        for error in errors:
            print(f"- {error}")
        return 0
    if errors:
        print("FAIL: context/conflict validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: context/conflict validation at {args.root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
