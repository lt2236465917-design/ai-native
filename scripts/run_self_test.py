#!/usr/bin/env python3
"""Run the ai-native skill's deterministic self-checks in one command."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import argparse
import os


def run(command: list[str], cwd: Path) -> None:
    print("$ " + " ".join(command))
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(command, cwd=cwd, text=True, env=env)
    if result.returncode:
        raise SystemExit(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validator",
        type=Path,
        help="Optional path to skill-creator quick_validate.py; omit when unavailable",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    python = sys.executable
    validator_verified = bool(args.validator and args.validator.exists())
    if validator_verified:
        run([python, str(args.validator), str(root)], root)
    else:
        print("NOT_VERIFIED: skill-creator quick_validate.py was not supplied; run it separately in an environment that provides the validator")
    run([python, str(root / "scripts/validate_artifact_chain.py"), "--root", str(root / "templates"), "--allow-placeholders"], root)
    run([python, str(root / "scripts/validate_artifact_chain.py"), "--root", str(root / "examples/solo-project")], root)
    run([python, str(root / "scripts/validate_artifact_chain.py"), "--root", str(root / "tests/fixtures/invalid-chain"), "--expect-fail"], root)
    run([python, str(root / "scripts/check_context_conflicts.py"), "--root", str(root / "examples/solo-project")], root)
    run([python, str(root / "scripts/check_context_conflicts.py"), "--root", str(root / "tests/fixtures/invalid-conflict"), "--expect-fail"], root)
    run([python, str(root / "scripts/check_runtime_adapter.py"), "--root", str(root / "references")], root)
    run([python, str(root / "scripts/check_runtime_adapter.py"), "--root", str(root / "examples/solo-project")], root)
    run([python, str(root / "scripts/check_runtime_adapter.py"), "--root", str(root / "examples/team-project")], root)
    run([python, str(root / "scripts/check_runtime_adapter.py"), "--root", str(root / "tests/fixtures/invalid-runtime"), "--expect-fail"], root)
    if validator_verified:
        print("PASS: ai-native self-test (including skill-creator validator)")
    else:
        print("PASS: ai-native self-test (skill-creator validator skipped; status is NOT_VERIFIED)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
