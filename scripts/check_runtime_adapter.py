#!/usr/bin/env python3
"""Check that runtime adapters point to one canonical AGENTS.md context."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _common import iter_files


REQUIRED_DOC_TERMS = (
    "AGENTS.md",
    "CLAUDE.md",
    "@AGENTS.md",
    "not by default",
    "unknown",
    "验证证据",
)


def inspect(root: Path) -> list[str]:
    errors: list[str] = []
    markdown_files = iter_files(root, (".md",))
    docs_files = [path for path in markdown_files if path.name == "runtime-adapters.md"]
    markdown = "\n".join(path.read_text(encoding="utf-8") for path in docs_files)
    if docs_files:
        for term in REQUIRED_DOC_TERMS:
            if term.lower() not in markdown.lower():
                errors.append(f"{root}: runtime adapter documentation is missing required term {term!r}")

    agents_files = [p for p in markdown_files if p.name == "AGENTS.md"]
    claude_files = [p for p in markdown_files if p.name == "CLAUDE.md"]
    for path in claude_files:
        text = path.read_text(encoding="utf-8")
        if "@AGENTS.md" not in text and "symlink" not in text.lower():
            errors.append(f"MIGRATION_REQUIRED: {path}: CLAUDE.md adapter must import @AGENTS.md or explicitly document a symlink")
        if "@AGENTS.md" in text and not (path.parent / "AGENTS.md").exists():
            errors.append(f"{path}: imported @AGENTS.md does not exist beside the adapter")
    if len(agents_files) > 1:
        # Nested AGENTS.md files are allowed only when the nested scope is explicit.
        for path in agents_files:
            text = path.read_text(encoding="utf-8").lower()
            if path.parent != root and "scope" not in text and "subproject" not in text:
                errors.append(f"{path}: nested AGENTS.md needs an explicit scope/subproject note")

    for path in iter_files(root, (".json",)):
        if path.name != "settings.json" or ".gemini" not in path.parts:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON ({exc})")
            continue
        names = data.get("context", {}).get("fileName", [])
        if isinstance(names, str):
            names = [names]
        if "AGENTS.md" not in names:
            errors.append(f"{path}: Gemini context.fileName does not include AGENTS.md")
        elif not (path.parent.parent / "AGENTS.md").exists():
            errors.append(f"{path}: Gemini config names AGENTS.md but no canonical file exists at {path.parent.parent / 'AGENTS.md'}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--expect-fail", action="store_true", help="Return success when an adapter problem is found")
    args = parser.parse_args()
    errors = inspect(args.root)
    if args.expect_fail:
        if not errors:
            print(f"FAIL: expected runtime adapter errors in {args.root}, but none were found")
            return 1
        print(f"PASS: negative runtime fixture detected {len(errors)} issue(s) in {args.root}")
        for error in errors:
            print(f"- {error}")
        return 0
    if errors:
        print("FAIL: runtime adapter validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: runtime adapter validation at {args.root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
