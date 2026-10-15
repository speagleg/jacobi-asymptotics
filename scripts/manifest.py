#!/usr/bin/env python3
"""Integrity manifest (Plan 59): SHA-256 of every tracked file that carries a result.

    python scripts/manifest.py           # (re)write MANIFEST.sha256 at the repository root
    python scripts/manifest.py --check   # verify the working tree against MANIFEST.sha256

Covered (tracked files only, enumerated with `git ls-files`):
  certified/*.py, certified/*.out           certified (Arb) suite and its outputs
  research/**/checks/**                     numerical check scripts and outputs (incl. research/**/RH/**/checks/**)
  papers/*/checks/**, papers/*/main.pdf     paper checks and the compiled drafts
  data/SHA256SUMS                           checksums of the fetched zeta-zero data
  tests/data/**                             committed test fixtures
  lean/**/*.lean, lean/lake-manifest.json, lean/lean-toolchain

The format is that of `sha256sum` (`<hex>  <path>`, sorted by path), so `sha256sum -c MANIFEST.sha256` also works.
--check additionally fails if a covered tracked file is missing from the manifest, or the manifest lists a file that
is no longer covered/tracked. Whenever a covered file changes, rerun `python scripts/manifest.py` and commit the
updated MANIFEST.sha256 together with the change.
"""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"


def covered(path: str) -> bool:
    parts = path.split("/")
    top = parts[0]
    if top == "certified":
        return len(parts) == 2 and path.endswith((".py", ".out"))
    if top == "research":
        return "checks" in parts[1:-1]
    if top == "papers":
        return len(parts) >= 3 and (parts[2] == "checks" and len(parts) >= 4 or
                                    (len(parts) == 3 and parts[2] == "main.pdf"))
    if path == "data/SHA256SUMS":
        return True
    if top == "tests":
        return len(parts) >= 3 and parts[1] == "data"
    if top == "lean":
        if ".lake" in parts:
            return False
        return path.endswith(".lean") or path in ("lean/lake-manifest.json", "lean/lean-toolchain")
    return False


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
    return sorted(p for p in out.decode("utf-8").split("\0") if p and covered(p))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build() -> list[tuple[str, str]]:
    return [(sha256(ROOT / p), p) for p in tracked_files()]


def write() -> int:
    entries = build()
    MANIFEST.write_text("".join(f"{h}  {p}\n" for h, p in entries), encoding="utf-8")
    print(f"wrote {MANIFEST.name}: {len(entries)} files")
    return 0


def check() -> int:
    hint = "Run `python scripts/manifest.py` and commit MANIFEST.sha256 if these changes are intended."
    if not MANIFEST.exists():
        print(f"FAIL: {MANIFEST.name} not found. {hint}")
        return 1
    listed: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        h, sep, p = line.partition("  ")
        if not sep or len(h) != 64:
            print(f"FAIL: malformed manifest line: {line!r}")
            return 1
        listed[p] = h
    expected = tracked_files()
    problems: list[str] = []
    for p in expected:
        if p not in listed:
            problems.append(f"NOT IN MANIFEST  {p}")
    for p, h in sorted(listed.items()):
        f = ROOT / p
        if p not in expected:
            problems.append(f"NOT COVERED/TRACKED  {p}")
        elif not f.is_file():
            problems.append(f"MISSING  {p}")
        elif sha256(f) != h:
            problems.append(f"CHANGED  {p}")
    if problems:
        print(f"FAIL: {len(problems)} manifest mismatch(es):")
        for x in problems:
            print("  " + x)
        print(hint)
        return 1
    print(f"OK: {len(listed)} files match {MANIFEST.name}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="verify the working tree against MANIFEST.sha256")
    args = ap.parse_args()
    return check() if args.check else write()


if __name__ == "__main__":
    sys.exit(main())
