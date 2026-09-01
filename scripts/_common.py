"""Small, dependency-free helpers shared by ai-native validation scripts."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


def iter_files(root: Path, suffixes: Iterable[str] = (".md",)) -> List[Path]:
    """Return deterministic, non-hidden files below *root*."""

    if not root.exists():
        return []
    wanted = set(suffixes)
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and (not wanted or path.suffix in wanted)
    )


def parse_frontmatter(path: Path) -> Tuple[Dict[str, str], str, List[str]]:
    """Parse the deliberately small key/value frontmatter used by templates."""

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, [f"{path}: missing opening YAML frontmatter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, text, [f"{path}: missing closing YAML frontmatter"]

    data: Dict[str, str] = {}
    errors: List[str] = []
    for number, line in enumerate(lines[1:end], 2):
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path}:{number}: frontmatter line has no ':'")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            errors.append(f"{path}:{number}: empty frontmatter key")
        elif key in data:
            errors.append(f"{path}:{number}: duplicate frontmatter key {key!r}")
        else:
            data[key] = value
    body = "\n".join(lines[end + 1 :])
    return data, body, errors


def normalized_lines(text: str) -> List[str]:
    """Normalize prose enough to compare duplicated rules without false whitespace noise."""

    result = []
    for line in text.splitlines():
        compact = re.sub(r"\s+", " ", line).strip().lower()
        if compact and not compact.startswith("<!--"):
            result.append(compact)
    return result


def has_placeholder(value: str) -> bool:
    return bool(re.search(r"(?:YYYY|<[^>]+>|INT-YYYY|SPEC-YYYY|PLAN-YYYY)", value))
