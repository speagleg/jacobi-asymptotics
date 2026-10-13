# Agent operating instructions: jacobi-asymptotics

Read this file and VERIFICATION_POLICY.md before doing anything. Spec:
docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md.

## What this repo is
A toolkit (`src/jacobi_asym`), a Lean library (`lean/`) and a research workspace (`research/G3prime`, `G2`, `G1`)
for Jacobi-coefficient / Hankel asymptotics of discrete measures accumulating at 0 ("Law P"). It continues
math-pursuits item 11 (read-only source, commit f5f6aef).

## Hard rules
1. Never modify source repos (math-pursuits and everything it lists). Corrections to them go to math-pursuits
   FIXES.md through a human.
2. No pip installs outside `.venv`. `.venv` adds only python-flint.
3. No claim about RH, GRH, Langlands, Ramanujan or physical constants. Measures built from zeros take the ordinates
   as real numbers (item 11, E1); that is an input, not evidence.
4. Citation gate: every external theorem is quoted with its exact hypotheses from a source someone actually read.
5. "Certified" means Arb/ball arithmetic with explicit tail bounds (`jacobi_asym.certify`). Everything else is
   "numerical".
6. Rule A (adversarial pass) for every lemma; Rule R (an independent second reader) before REVIEWED.
7. Commit prefixes: `toolkit:`, `lean:`, `G3p:`, `G2:`, `G1:`, `docs:`. Never force-push or rewrite history.

## Stop conditions
Stop and write it up in the relevant LOG.md if:
- a step is as hard as an open problem;
- a claimed statement has a counterexample;
- the result is already known (record the reference);
- a needed citation cannot be verified;
- work would require editing a read-only source.

## Environment
- `scripts/setup_env.sh` builds `.venv` and `csrc/build/`. Use `.venv/bin/python -m pytest` (fast suite);
  `-m slow` runs the regressions.
- Lean: `export PATH=$HOME/.elan/bin:$PATH`; Lean 4.34.1 and Mathlib v4.34.1 (Plan 2).
- PARI/gp: /usr/bin/gp 2.15.4.
