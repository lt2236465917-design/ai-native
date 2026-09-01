#!/usr/bin/env python3
"""Validate the committed-artifact templates or a concrete artifact chain."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _common import has_placeholder, parse_frontmatter


EXPECTED = {
    "intent.md": {
        "artifact": "intent",
        "id_prefix": "INT-",
        "headings": ["## Problem", "## Proposed outcome", "## Open questions", "## Human decision"],
        "fields": ["id", "status", "author", "owner", "created_at"],
    },
    "spec.md": {
        "artifact": "spec",
        "id_prefix": "SPEC-",
        "headings": ["## Intent reference", "## Requirements", "## Design", "## Verification plan", "## Human decision"],
        "fields": ["id", "status", "intent_id", "owner", "created_at"],
    },
    "plan.md": {
        "artifact": "plan",
        "id_prefix": "PLAN-",
        "headings": ["## Inputs", "## Files and interfaces that change", "## Order of work", "## Risks and alternatives", "## Proof", "## Human decision"],
        "fields": ["id", "status", "intent_id", "spec_id", "owner", "created_at"],
    },
    "review-record.md": {
        "artifact": "review-record",
        "id_prefix": "REVIEW-",
        "headings": ["## Scope and evidence", "## Findings", "## Decision"],
        "fields": ["id", "status", "plan_id", "change_id", "reviewer", "created_at", "decision"],
    },
    "incident-record.md": {
        "artifact": "incident-record",
        "id_prefix": "INC-",
        "headings": ["## Impact and timeline", "## Containment and recovery", "## Root-cause classification", "## Writeback", "## Human decision"],
        "fields": ["id", "status", "owner", "created_at"],
    },
}

VALID_STATUSES = {
    "draft",
    "open",
    "accepted",
    "approved",
    "rejected",
    "deferred",
    "pending",
    "request_changes",
    "resolved",
    "contained",
    "accepted_risk",
}


def validate(root: Path, allow_placeholders: bool) -> list[str]:
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}
    candidates: dict[str, list[Path]] = {}
    for path in root.rglob("*.md"):
        if path.name in EXPECTED:
            candidates.setdefault(path.name, []).append(path)
    found: dict[str, Path] = {}
    for filename, paths in candidates.items():
        if len(paths) > 1:
            errors.append(f"{root}: multiple files named {filename}: {', '.join(map(str, paths))}")
        else:
            found[filename] = paths[0]

    for filename, spec in EXPECTED.items():
        path = found.get(filename)
        if path is None:
            errors.append(f"{root}: missing required artifact template/file {filename}")
            continue
        fields, body, parse_errors = parse_frontmatter(path)
        errors.extend(parse_errors)
        for field in spec["fields"]:
            if field not in fields:
                errors.append(f"{path}: missing frontmatter field {field}")
        if fields.get("artifact") != spec["artifact"]:
            errors.append(f"{path}: artifact must be {spec['artifact']!r}, got {fields.get('artifact')!r}")
        artifact_id = fields.get("id", "")
        if artifact_id in seen_ids and artifact_id:
            errors.append(f"{path}: duplicate artifact id {artifact_id!r}; first seen in {seen_ids[artifact_id]}")
        elif artifact_id:
            seen_ids[artifact_id] = path
        if not artifact_id.startswith(spec["id_prefix"]):
            errors.append(f"{path}: id must start with {spec['id_prefix']!r}")
        elif not allow_placeholders and (has_placeholder(artifact_id) or not re.fullmatch(r"[A-Z]+-\d{8}-\d{3}", artifact_id)):
            errors.append(f"{path}: id must use a concrete PREFIX-YYYYMMDD-### value")
        status = fields.get("status", "")
        if status not in VALID_STATUSES:
            errors.append(f"{path}: unsupported status {status!r}")
        for heading in spec["headings"]:
            if heading not in body:
                errors.append(f"{path}: missing required section {heading}")
        if not allow_placeholders:
            for field in spec["fields"]:
                if not fields.get(field) or has_placeholder(fields[field]):
                    errors.append(f"{path}: field {field} is still empty or a placeholder")
            for date_field in ("created_at", "updated_at"):
                if date_field in fields and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields[date_field]):
                    errors.append(f"{path}: {date_field} must be YYYY-MM-DD when present")
            if "revision" in fields and not fields["revision"].strip():
                errors.append(f"{path}: revision must not be empty when present")

    # Cross-artifact references make the chain auditable rather than merely present.
    refs = {}
    for filename in EXPECTED:
        path = found.get(filename)
        if path:
            fields, _, _ = parse_frontmatter(path)
            refs[filename] = fields
    if "spec.md" in refs and "intent.md" in refs and not allow_placeholders:
        if refs["spec.md"].get("intent_id") != refs["intent.md"].get("id"):
            errors.append("spec.md: intent_id does not match intent.md id")
    if "plan.md" in refs and not allow_placeholders:
        if refs.get("plan.md", {}).get("intent_id") != refs.get("intent.md", {}).get("id"):
            errors.append("plan.md: intent_id does not match intent.md id")
        if refs.get("plan.md", {}).get("spec_id") != refs.get("spec.md", {}).get("id"):
            errors.append("plan.md: spec_id does not match spec.md id")
    if "review-record.md" in refs and not allow_placeholders:
        if refs["review-record.md"].get("plan_id") != refs.get("plan.md", {}).get("id"):
            errors.append("review-record.md: plan_id does not match plan.md id")
    if "incident-record.md" in found and "intent.md" in refs and not allow_placeholders:
        incident_text = found["incident-record.md"].read_text(encoding="utf-8")
        match = re.search(r"new_or_updated_intent_id\s*:\s*([^\s|]+)", incident_text)
        if match and match.group(1).lower() not in {"none", "n/a"}:
            if match.group(1) != refs["intent.md"].get("id"):
                errors.append("incident-record.md: new_or_updated_intent_id does not match intent.md id")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Directory containing the five chain artifacts")
    parser.add_argument("--allow-placeholders", action="store_true", help="Validate templates rather than concrete instances")
    parser.add_argument("--expect-fail", action="store_true", help="Return success when the chain is invalid")
    args = parser.parse_args()
    errors = validate(args.root, args.allow_placeholders)
    if args.expect_fail:
        if not errors:
            print(f"FAIL: expected artifact-chain errors in {args.root}, but none were found")
            return 1
        print(f"PASS: negative artifact fixture detected {len(errors)} issue(s) in {args.root}")
        for error in errors:
            print(f"- {error}")
        return 0
    if errors:
        print("FAIL: artifact chain validation")
        for error in errors:
            print(f"- {error}")
        return 1
    mode = "template" if args.allow_placeholders else "instance"
    print(f"PASS: artifact chain validation ({mode}) at {args.root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
