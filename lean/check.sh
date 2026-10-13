#!/usr/bin/env bash
# Build the library and audit axioms: fails on any sorryAx or non-standard axiom.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/.elan/bin:$PATH"
lake build 2>&1 | tail -5
out=$(lake env lean Audit.lean 2>&1)
echo "$out"
if echo "$out" | grep -q "sorryAx"; then echo "FAIL: sorryAx present"; exit 1; fi
bad=$(echo "$out" | grep -o "depends on axioms: \[[^]]*\]" | tr -d '[]' | sed 's/depends on axioms: //' \
      | tr ',' '\n' | sed 's/ //g' | grep -v -E '^(propext|Classical.choice|Quot.sound)?$' || true)
if [ -n "$bad" ]; then echo "FAIL: non-standard axioms: $bad"; exit 1; fi
if echo "$out" | grep -qi "error"; then echo "FAIL: errors"; exit 1; fi
echo "AUDIT OK"
