# Plan 1: scaffolding and toolkit port (implementation plan)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the `jacobi-asymptotics` repo, with its rules and provenance, and a tested Python toolkit
`jacobi_asym`. The toolkit computes Jacobi coefficients, Hankel determinants and Law-P statistics for discrete
measures accumulating at 0, and reproduces item 11's recorded numbers.

**Architecture:** A `src/`-layout Python package on top of the system numpy, scipy, mpmath and sympy, plus one
compiled C kernel (RKPW in double, long double and binary128) invoked as a subprocess. The core value type is
`DiscreteMeasure`. Coefficient engines, reference families, law statistics, Hankel tools, L-function measure sources
and the Arb certification layer are separate subpackages that depend only on `measures.base`.

**Tech Stack:**
- Python 3.12.3 (system) with numpy 2.3.5, scipy 1.17.1, mpmath 1.3.0, sympy 1.14.0 and pytest 9.0.2.
- python-flint 0.9.0, installed in the project `.venv` only.
- gcc 13.3 with libquadmath.

**Spec:** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` (build steps 1 and 2 of §11).

## Global Constraints

- Source repos are read-only. Copy from `/mnt/c/Users/gspea/source/repos/math-pursuits` (commit `f5f6aef`). Never
  modify it, and record every copy in `PROVENANCE.md`.
- Do not install anything into shared environments. Use `.venv` (created with `--system-site-packages`); the only
  added package is `python-flint==0.9.0`.
- Only `jacobi_asym.certify` may call a result "certified". Float results are "numerical".
- No RH, GRH or Langlands framing anywhere (docstrings, README, comments).
- Commit message prefixes: `toolkit:`, `docs:`. Each commit ends with
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Large data (`*.npy`, `*.npz` runs, `*.gz` zero tables) is not committed. Small test fixtures (under 1 MB) live in
  `tests/data/`.
- Repo root: `/mnt/c/Users/gspea/source/repos/jacobi-asymptotics`. All paths below are relative to it.
- Item-11 conventions: a_n is the diagonal and b_n > 0 the off-diagonal, n ≥ 1. RKPW returns α_k = a_{k+1} and
  β_0 = mass, β_k = b_k² for k ≥ 1.

## Review Focus

1. **Unsorted or duplicate atoms passed by a user.** A reasonable user expects either sorting or a clear `ValueError`,
   never silently wrong coefficients. Pinned in Task 2.
2. **Requesting n ≥ number of atoms.** b_N = 0 there, and later logs produce −inf. Expect a `ValueError` that names
   the limit. Pinned in Task 3 (rkpw and mp) and Task 4 (lanczos).
3. **Missing compiled kernel or missing fetched data.** Expect an actionable error ("run `make -C csrc`",
   "run `python data/fetch.py odlyzko`") rather than a FileNotFoundError deep in a subprocess. Pinned in Tasks 3
   and 8.
4. **The Weyl predictor at small n (n = 1, 2).** The bracket degenerates. Expect a `ValueError` for n < 2, not a
   crash or a meaningless number. Pinned in Task 6.
5. **Long-double and quad outputs parsed back into float64.** This would silently lose the extra precision. Expect
   `prec='ld'`/`'q'` to return `np.longdouble` arrays. Pinned in Task 3.

---

### Task 1: Repo scaffolding, rules and environment

**Files:**
- Create: `.gitignore`, `pyproject.toml`, `scripts/setup_env.sh`, `AGENTS.md`, `VERIFICATION_POLICY.md`, `README.md`,
  `PROVENANCE.md`, `src/jacobi_asym/__init__.py`, `tests/test_smoke.py`

**Interfaces:**
- Produces: an importable package `jacobi_asym` with `__version__ = "0.1.0"`; `.venv/bin/python` with python-flint;
  pytest markers `slow` and `data`.

- [ ] **Step 1: Write `.gitignore`**

```gitignore
.venv/
__pycache__/
*.pyc
*.egg-info/
csrc/build/
data/raw/
*.npy
*.npz
!tests/data/*.npz
*.gz
.pytest_cache/
lean/.lake
tmp/
```

- [ ] **Step 2: Write `pyproject.toml`**

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "jacobi-asym"
version = "0.1.0"
description = "Jacobi-coefficient and Hankel-determinant asymptotics for discrete measures accumulating at 0"
requires-python = ">=3.12"
dependencies = ["numpy>=2.0", "scipy>=1.13", "mpmath>=1.3", "sympy>=1.12"]

[project.optional-dependencies]
certify = ["python-flint==0.9.0"]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-m 'not slow'"
markers = [
  "slow: long-running regression (run with -m slow)",
  "data: needs data fetched by data/fetch.py (skipped if absent)",
]
```

- [ ] **Step 3: Write `scripts/setup_env.sh`**

```bash
#!/usr/bin/env bash
# Project venv on top of the system scientific stack. Adds ONLY python-flint (spec §10).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m venv --system-site-packages .venv
.venv/bin/pip install --no-deps -e .
.venv/bin/pip install python-flint==0.9.0
make -C csrc
.venv/bin/python -c "import jacobi_asym, flint; print('ok', jacobi_asym.__version__, flint.__version__)"
```

Run `chmod +x scripts/setup_env.sh`. The `make -C csrc` line fails until Task 3. For now, run the script's first
three commands by hand.

- [ ] **Step 4: Write the failing smoke test `tests/test_smoke.py`**

```python
import jacobi_asym


def test_version():
    assert jacobi_asym.__version__ == "0.1.0"
```

- [ ] **Step 5: Confirm the test fails**

Run: `cd /mnt/c/Users/gspea/source/repos/jacobi-asymptotics && python3 -m venv --system-site-packages .venv && .venv/bin/pip install --no-deps -e . && .venv/bin/python -m pytest tests/test_smoke.py -v`

Expected: an ERROR during install or collection, because `src/jacobi_asym` does not exist yet.

- [ ] **Step 6: Create the package**

`src/jacobi_asym/__init__.py`:
```python
"""jacobi_asym: Jacobi coefficients, Hankel determinants and Law-P statistics for discrete positive measures
sum_k w_k delta_{x_k} accumulating at 0.  Float results are numerical; only jacobi_asym.certify certifies."""
__version__ = "0.1.0"
```

Then run: `.venv/bin/pip install --no-deps -e . && .venv/bin/pip install python-flint==0.9.0`

- [ ] **Step 7: Confirm the test passes**

Run: `.venv/bin/python -m pytest tests/test_smoke.py -v`
Expected: PASS.

- [ ] **Step 8: Write the governance docs**

1. Copy `VERIFICATION_POLICY.md` from math-pursuits verbatim:
   `cp /mnt/c/Users/gspea/source/repos/math-pursuits/VERIFICATION_POLICY.md .`
2. Prepend this header:
   ```markdown
   > Adapted from math-pursuits VERIFICATION_POLICY.md (commit f5f6aef). Changes for this repo: the label
   > PROVED-mod-input (proved modulo a named Lean/structure input listed in lean/JacobiAsym/Inputs.lean) is added;
   > "item" means a research problem under research/ (G3prime, G2, G1) or a toolkit module.
   ```

Write `AGENTS.md`:
```markdown
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
```

Write `README.md`:
```markdown
# jacobi-asymptotics

Jacobi coefficients (a_n, b_n) and Hankel determinants of discrete positive measures σ = Σ w_k δ_{x_k} with
x_k ↓ 0, and the "Law P" asymptotics b_n/x_n → c(p) = ¼(π/(2I(p)))^p for x_k ~ C k^{-p}
(c(2) = π²/16). Continues math-pursuits item 11.

Status: toolkit under construction (Plan 1). Lean core: Plan 2. Research: research/G3prime, G2, G1.

## Setup
    scripts/setup_env.sh
    .venv/bin/python -m pytest            # fast suite
    .venv/bin/python -m pytest -m slow    # regressions against item 11 (minutes)

Measures built from L-function zeros take the ordinates as real numbers. Nothing here is evidence about RH.
```

Write `PROVENANCE.md`:
```markdown
# Provenance

Material copied from read-only sources. Source: math-pursuits = /mnt/c/Users/gspea/source/repos/math-pursuits,
commit f5f6aef.

| Copied to | From | Notes |
|---|---|---|
| VERIFICATION_POLICY.md | math-pursuits/VERIFICATION_POLICY.md | header added |
```

- [ ] **Step 9: Commit**

```bash
git add .gitignore pyproject.toml scripts/setup_env.sh AGENTS.md VERIFICATION_POLICY.md README.md PROVENANCE.md src tests
git commit -m "toolkit: repo scaffolding, rules, venv setup, smoke test

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: `DiscreteMeasure` and pure powers

**Files:**
- Create: `src/jacobi_asym/measures/__init__.py`, `src/jacobi_asym/measures/base.py`,
  `src/jacobi_asym/measures/powers.py`
- Test: `tests/test_measures_base.py`

**Interfaces:**
- Produces:
  - `DiscreteMeasure(atoms: np.ndarray, weights: np.ndarray, label: str = "")`. A frozen dataclass. Atoms are
    float64, strictly decreasing and > 0; weights are float64 and > 0; arrays are read-only. Properties: `mass`
    (float) and `N` (int).
  - `DiscreteMeasure.from_atoms(x, w, tail=None, label="") -> DiscreteMeasure`. Sorts descending, merges an
    optional `tail=(xt, wt)`, and raises `ValueError` on duplicates, non-positive or non-finite input, or length
    mismatch.
  - `pure_power(p: float, K: int, s: float | None = None, C: float = 1.0) -> DiscreteMeasure`. Atoms C k^{-p},
    k = 1..K; weights k^{-s}, or the atoms themselves if s is None.

- [ ] **Step 1: Write the failing tests `tests/test_measures_base.py`**

```python
import numpy as np
import pytest
from jacobi_asym.measures import DiscreteMeasure, pure_power


def test_from_atoms_sorts_descending_and_keeps_pairs():
    mu = DiscreteMeasure.from_atoms([0.1, 0.5, 0.3], [1.0, 2.0, 3.0])
    assert np.array_equal(mu.atoms, [0.5, 0.3, 0.1])
    assert np.array_equal(mu.weights, [2.0, 3.0, 1.0])
    assert mu.N == 3 and mu.mass == pytest.approx(6.0)


def test_rejects_duplicates_nonpositive_nonfinite_mismatch():
    with pytest.raises(ValueError, match="duplicate"):
        DiscreteMeasure.from_atoms([0.5, 0.5], [1.0, 1.0])
    with pytest.raises(ValueError, match="positive"):
        DiscreteMeasure.from_atoms([0.5, -0.1], [1.0, 1.0])
    with pytest.raises(ValueError, match="positive"):
        DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 0.0])
    with pytest.raises(ValueError, match="finite"):
        DiscreteMeasure.from_atoms([0.5, np.nan], [1.0, 1.0])
    with pytest.raises(ValueError, match="length"):
        DiscreteMeasure.from_atoms([0.5, 0.1], [1.0])


def test_direct_constructor_rejects_unsorted():
    with pytest.raises(ValueError, match="decreasing"):
        DiscreteMeasure(np.array([0.1, 0.5]), np.array([1.0, 1.0]))


def test_arrays_are_read_only():
    mu = DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 1.0])
    with pytest.raises(ValueError):
        mu.atoms[0] = 9.0


def test_tail_is_merged():
    mu = DiscreteMeasure.from_atoms([0.5, 0.25], [1.0, 1.0], tail=([0.01, 0.02], [0.1, 0.1]))
    assert np.array_equal(mu.atoms, [0.5, 0.25, 0.02, 0.01])


def test_pure_power():
    mu = pure_power(2, 4, s=3, C=2.0)
    assert np.allclose(mu.atoms, 2.0 * np.arange(1, 5) ** -2.0)
    assert np.allclose(mu.weights, np.arange(1, 5) ** -3.0)
    mu2 = pure_power(1, 3)
    assert np.array_equal(mu2.weights, mu2.atoms)
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_measures_base.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'jacobi_asym.measures'`.

- [ ] **Step 3: Implement**

`src/jacobi_asym/measures/base.py`:
```python
"""Discrete positive measures sigma = sum_k w_k delta_{x_k} with atoms strictly decreasing to (towards) 0."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


def _arr(v, name):
    a = np.array(v, dtype=np.float64).ravel()
    if not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be finite")
    if not np.all(a > 0):
        raise ValueError(f"{name} must be positive")
    return a


@dataclass(frozen=True)
class DiscreteMeasure:
    atoms: np.ndarray
    weights: np.ndarray
    label: str = ""

    def __post_init__(self):
        x = _arr(self.atoms, "atoms")
        w = _arr(self.weights, "weights")
        if x.shape != w.shape:
            raise ValueError(f"atoms/weights length mismatch: {x.size} vs {w.size}")
        if x.size == 0:
            raise ValueError("measure must have at least one atom")
        if np.any(np.diff(x) >= 0):
            raise ValueError("atoms must be strictly decreasing (use DiscreteMeasure.from_atoms to sort)")
        x.setflags(write=False)
        w.setflags(write=False)
        object.__setattr__(self, "atoms", x)
        object.__setattr__(self, "weights", w)

    @classmethod
    def from_atoms(cls, x, w, tail=None, label: str = "") -> "DiscreteMeasure":
        x = _arr(x, "atoms")
        w = _arr(w, "weights")
        if x.shape != w.shape:
            raise ValueError(f"atoms/weights length mismatch: {x.size} vs {w.size}")
        if tail is not None:
            xt, wt = _arr(tail[0], "tail atoms"), _arr(tail[1], "tail weights")
            if xt.shape != wt.shape:
                raise ValueError("tail atoms/weights length mismatch")
            x, w = np.concatenate([x, xt]), np.concatenate([w, wt])
        o = np.argsort(-x, kind="stable")
        x, w = x[o], w[o]
        if np.any(np.diff(x) == 0):
            raise ValueError("duplicate atoms (merge their weights before constructing)")
        return cls(x, w, label)

    @property
    def mass(self) -> float:
        return float(np.sum(self.weights))

    @property
    def N(self) -> int:
        return int(self.atoms.size)
```

`src/jacobi_asym/measures/powers.py`:
```python
"""Pure-power model measures: atoms C k^{-p}, weights k^{-s} (or the atoms themselves)."""
import numpy as np
from .base import DiscreteMeasure


def pure_power(p: float, K: int, s: float | None = None, C: float = 1.0) -> DiscreteMeasure:
    k = np.arange(1, K + 1, dtype=np.float64)
    x = C * k ** (-float(p))
    w = x.copy() if s is None else k ** (-float(s))
    return DiscreteMeasure(x, w, label=f"pure_power(p={p}, K={K}, s={s}, C={C})")
```

`src/jacobi_asym/measures/__init__.py`:
```python
from .base import DiscreteMeasure
from .powers import pure_power

__all__ = ["DiscreteMeasure", "pure_power"]
```

- [ ] **Step 4: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_measures_base.py -v`
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/measures tests/test_measures_base.py
git commit -m "toolkit: DiscreteMeasure (validated, immutable) and pure_power

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Coefficient engines, part 1: mpmath reference and RKPW kernel

**Files:**
- Create: `csrc/rkpw.c` (copied), `csrc/Makefile`, `src/jacobi_asym/jacobi/__init__.py`,
  `src/jacobi_asym/jacobi/result.py`, `src/jacobi_asym/jacobi/mp.py`, `src/jacobi_asym/jacobi/rkpw.py`
- Modify: `PROVENANCE.md` (add the rkpw.c row)
- Test: `tests/test_jacobi_engines.py`

**Interfaces:**
- Consumes: `DiscreteMeasure` (Task 2).
- Produces:
  - `JacobiCoeffs(a: np.ndarray, b2: np.ndarray, method: str, prec: str)`, a frozen dataclass. `a[i] = a_{i+1}` and
    `b2[i] = b_{i+1}²`, each of length n. Property `b = sqrt(b2)` and attribute `mass: float`.
  - `jacobi_mp(mu, n, dps=50) -> tuple[list[mpf], list[mpf]]`, returning (a_1..a_n, b_1²..b_n²) by the
    discretized Stieltjes procedure in mpmath. Requires n < mu.N.
  - `jacobi_rkpw(mu, n, prec='d') -> JacobiCoeffs`. Requires n < mu.N. Arrays are float64 for 'd' and
    np.longdouble for 'ld' and 'q'.
  - `KernelMissing(RuntimeError)`.

- [ ] **Step 1: Copy the kernel, write the Makefile, record provenance**

```bash
mkdir -p csrc
cp /mnt/c/Users/gspea/source/repos/math-pursuits/items/11-zero-measure-jacobi-asymptotics/work/rkpw.c csrc/rkpw.c
```

`csrc/Makefile`:
```make
CFLAGS = -O3 -march=native
all: build/rkpw_d build/rkpw_ld build/rkpw_q
build:
	mkdir -p build
build/rkpw_d: rkpw.c | build
	gcc $(CFLAGS) -o $@ rkpw.c -lm
build/rkpw_ld: rkpw.c | build
	gcc $(CFLAGS) -DLD -o $@ rkpw.c -lm
build/rkpw_q: rkpw.c | build
	gcc $(CFLAGS) -DQUAD -o $@ rkpw.c -lquadmath -lm
clean:
	rm -rf build
```

Run `make -C csrc`. Expected: three binaries in `csrc/build/`.

Append this row to the `PROVENANCE.md` table:
`| csrc/rkpw.c | math-pursuits/items/11-zero-measure-jacobi-asymptotics/work/rkpw.c | verbatim |`

- [ ] **Step 2: Write the failing tests `tests/test_jacobi_engines.py`**

```python
import numpy as np
import mpmath as mp
import pytest
from jacobi_asym.measures import DiscreteMeasure, pure_power
from jacobi_asym.jacobi import jacobi_mp, jacobi_rkpw, JacobiCoeffs


def test_two_atom_closed_form_mp():
    # mu = w1 d_{x1} + w2 d_{x2}: a_1 = (w1x1+w2x2)/(w1+w2), b_1^2 = w1 w2 (x1-x2)^2/(w1+w2)^2
    mu = DiscreteMeasure.from_atoms([0.75, 0.25], [1.0, 3.0])
    a, b2 = jacobi_mp(mu, 1, dps=40)
    assert abs(a[0] - mp.mpf(0.375)) < mp.mpf(10) ** -35
    assert abs(b2[0] - mp.mpf(3) * mp.mpf(0.25) / 16) < mp.mpf(10) ** -35


def test_rkpw_matches_mp_random_measure():
    rng = np.random.default_rng(7)
    x = np.sort(rng.uniform(0.01, 1.0, 60))[::-1]
    w = rng.uniform(0.1, 2.0, 60)
    mu = DiscreteMeasure.from_atoms(x, w)
    a_ref, b2_ref = jacobi_mp(mu, 30, dps=60)
    r = jacobi_rkpw(mu, 30)
    assert isinstance(r, JacobiCoeffs) and r.a.dtype == np.float64
    assert np.max(np.abs(r.a / np.array([float(v) for v in a_ref]) - 1)) < 1e-11
    assert np.max(np.abs(r.b2 / np.array([float(v) for v in b2_ref]) - 1)) < 1e-11
    assert r.mass == pytest.approx(mu.mass, rel=1e-14)


def test_rkpw_long_double_and_quad_keep_precision_type():
    mu = pure_power(2, 2000)
    rd, rl, rq = (jacobi_rkpw(mu, 100, prec=p) for p in ("d", "ld", "q"))
    assert rl.a.dtype == np.longdouble and rq.b2.dtype == np.longdouble
    assert np.max(np.abs(rd.b2 / rl.b2.astype(np.float64) - 1)) < 1e-11
    assert np.max(np.abs(rl.b2 / rq.b2 - 1)) < 1e-14


@pytest.mark.parametrize("engine", ["rkpw", "mp"])
def test_n_must_be_below_number_of_atoms(engine):
    mu = DiscreteMeasure.from_atoms([0.5, 0.3, 0.1], [1.0, 1.0, 1.0])
    with pytest.raises(ValueError, match="n < N"):
        jacobi_rkpw(mu, 3) if engine == "rkpw" else jacobi_mp(mu, 3)


def test_missing_kernel_message(monkeypatch, tmp_path):
    import jacobi_asym.jacobi.rkpw as R
    monkeypatch.setattr(R, "BIN_DIR", tmp_path)
    with pytest.raises(R.KernelMissing, match="make -C csrc"):
        jacobi_rkpw(pure_power(2, 10), 3)
```

- [ ] **Step 3: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_jacobi_engines.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'jacobi_asym.jacobi'`.

- [ ] **Step 4: Implement**

`src/jacobi_asym/jacobi/result.py`:
```python
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class JacobiCoeffs:
    """a[i] = a_{i+1} (diagonal), b2[i] = b_{i+1}^2 (squared off-diagonal), i = 0..n-1.  Numerical, not certified."""
    a: np.ndarray
    b2: np.ndarray
    method: str
    prec: str
    mass: float

    @property
    def b(self) -> np.ndarray:
        return np.sqrt(self.b2)
```

`src/jacobi_asym/jacobi/mp.py`:
```python
"""High-precision reference: discretized Stieltjes procedure in mpmath (O(N n) mpf operations; use N <~ 2000)."""
import mpmath as mp
from ..measures.base import DiscreteMeasure


def jacobi_mp(mu: DiscreteMeasure, n: int, dps: int = 50):
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    with mp.workdps(dps):
        x = [mp.mpf(float(v)) for v in mu.atoms]
        w = [mp.mpf(float(v)) for v in mu.weights]
        N = len(x)
        p_prev = [mp.mpf(0)] * N
        p = [mp.mpf(1)] * N
        nrm_prev = None
        nrm = mp.fsum(w)
        a, b2 = [], []
        for k in range(n):
            ak = mp.fsum(w[i] * x[i] * p[i] ** 2 for i in range(N)) / nrm
            a.append(ak)
            if nrm_prev is None:
                p_next = [(x[i] - ak) * p[i] for i in range(N)]
            else:
                r = nrm / nrm_prev
                p_next = [(x[i] - ak) * p[i] - r * p_prev[i] for i in range(N)]
            nrm_next = mp.fsum(w[i] * p_next[i] ** 2 for i in range(N))
            b2.append(nrm_next / nrm)
            p_prev, p, nrm_prev, nrm = p, p_next, nrm, nrm_next
        return a, b2
```

`src/jacobi_asym/jacobi/rkpw.py`:
```python
"""RKPW (Gragg-Harrod / Gautschi) via the compiled kernels in csrc/build (double, long double, binary128)."""
import os
import subprocess
import tempfile
from pathlib import Path
import numpy as np
from ..measures.base import DiscreteMeasure
from .result import JacobiCoeffs

BIN_DIR = Path(__file__).resolve().parents[3] / "csrc" / "build"
_EXE = {"d": "rkpw_d", "ld": "rkpw_ld", "q": "rkpw_q"}


class KernelMissing(RuntimeError):
    pass


def jacobi_rkpw(mu: DiscreteMeasure, n: int, prec: str = "d") -> JacobiCoeffs:
    if prec not in _EXE:
        raise ValueError(f"prec must be one of {sorted(_EXE)}")
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    exe = Path(BIN_DIR) / _EXE[prec]
    if not exe.exists():
        raise KernelMissing(f"{exe} not found: run `make -C csrc` in the repo root")
    with tempfile.TemporaryDirectory() as td:
        fin, fout = os.path.join(td, "atoms.bin"), os.path.join(td, "out.txt")
        np.stack([mu.atoms, mu.weights], 1).astype("<f8").tofile(fin)
        subprocess.run([str(exe), fin, str(n + 1), fout], check=True)
        dt = np.float64 if prec == "d" else np.longdouble
        d = np.loadtxt(fout, dtype=dt, ndmin=2)
    alpha, beta = d[:, 1], d[:, 2]
    return JacobiCoeffs(a=alpha[:n].copy(), b2=beta[1:n + 1].copy(), method="rkpw", prec=prec, mass=float(beta[0]))
```

`src/jacobi_asym/jacobi/__init__.py`:
```python
from .result import JacobiCoeffs
from .mp import jacobi_mp
from .rkpw import jacobi_rkpw, KernelMissing

__all__ = ["JacobiCoeffs", "jacobi_mp", "jacobi_rkpw", "KernelMissing"]
```

- [ ] **Step 5: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_jacobi_engines.py -v`
Expected: 6 passed. If `test_rkpw_long_double_and_quad_keep_precision_type` fails on the `rl`/`rq` comparison,
check the parse dtype and not the kernel: the kernel already matched item 11's validations (long double vs binary128
≤ 4.5e−13 at 10⁵ atoms).

- [ ] **Step 6: Commit**

```bash
git add csrc/rkpw.c csrc/Makefile src/jacobi_asym/jacobi tests/test_jacobi_engines.py PROVENANCE.md
git commit -m "toolkit: RKPW kernels (d/ld/q) + wrapper, mpmath Stieltjes reference

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Coefficient engines, part 2: Lanczos cross-check and dispatcher

**Files:**
- Create: `src/jacobi_asym/jacobi/lanczos.py`, `src/jacobi_asym/jacobi/dispatch.py`
- Modify: `src/jacobi_asym/jacobi/__init__.py`
- Test: `tests/test_jacobi_dispatch.py`

**Interfaces:**
- Consumes: `JacobiCoeffs`, `jacobi_rkpw`, `jacobi_mp` (Task 3).
- Produces:
  - `jacobi_lanczos(mu, n) -> JacobiCoeffs` (float64, full double reorthogonalisation; memory (n+1)·N doubles).
  - `jacobi_coeffs(mu, n, method='rkpw', prec='d', dps=50) -> JacobiCoeffs`. Methods are 'rkpw', 'lanczos' and
    'mp'; 'mp' returns float64 arrays rounded from mpf, with prec=f'dps{dps}'.

- [ ] **Step 1: Write the failing tests `tests/test_jacobi_dispatch.py`**

```python
import numpy as np
import pytest
from jacobi_asym.measures import pure_power, DiscreteMeasure
from jacobi_asym.jacobi import jacobi_coeffs, jacobi_lanczos


def test_lanczos_vs_rkpw_on_20k_atoms():
    mu = pure_power(2, 20000)
    r = jacobi_coeffs(mu, 300, method="rkpw")
    l = jacobi_lanczos(mu, 300)
    assert np.max(np.abs(np.sqrt(l.b2 / r.b2) - 1)) < 1e-12
    assert np.max(np.abs(l.a / r.a - 1)) < 1e-12


def test_dispatch_mp_returns_float_arrays():
    mu = pure_power(1, 40, s=2)
    m = jacobi_coeffs(mu, 10, method="mp", dps=40)
    r = jacobi_coeffs(mu, 10)
    assert m.prec == "dps40" and m.a.dtype == np.float64
    assert np.max(np.abs(m.b2 / r.b2 - 1)) < 1e-12


def test_dispatch_rejects_unknown_method():
    with pytest.raises(ValueError, match="method"):
        jacobi_coeffs(pure_power(2, 10), 3, method="qr")


def test_lanczos_n_limit():
    with pytest.raises(ValueError, match="n < N"):
        jacobi_lanczos(DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 1.0]), 2)
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_jacobi_dispatch.py -v`
Expected: FAIL with `ImportError: cannot import name 'jacobi_coeffs'`.

- [ ] **Step 3: Implement**

`src/jacobi_asym/jacobi/lanczos.py`:
```python
"""Float64 Lanczos with full double reorthogonalisation (independent cross-check of RKPW; as in item 11)."""
import numpy as np
from ..measures.base import DiscreteMeasure
from .result import JacobiCoeffs


def jacobi_lanczos(mu: DiscreteMeasure, n: int) -> JacobiCoeffs:
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    x = np.asarray(mu.atoms, float)
    w = np.asarray(mu.weights, float) / mu.mass
    q = np.sqrt(w)
    Q = np.zeros((n + 1, x.size))
    Q[0] = q
    qp = np.zeros_like(q)
    A, B2, bp = [], [], 0.0
    for k in range(n):
        r = x * q
        a = q @ r
        r = r - a * q - bp * qp
        for _ in range(2):
            r -= Q[:k + 1].T @ (Q[:k + 1] @ r)
        bn = np.linalg.norm(r)
        A.append(a)
        B2.append(bn * bn)
        qp, q, bp = q, r / bn, bn
        Q[k + 1] = q
    return JacobiCoeffs(np.array(A), np.array(B2), "lanczos", "d", mu.mass)
```

`src/jacobi_asym/jacobi/dispatch.py`:
```python
import numpy as np
from ..measures.base import DiscreteMeasure
from .result import JacobiCoeffs
from .rkpw import jacobi_rkpw
from .lanczos import jacobi_lanczos
from .mp import jacobi_mp


def jacobi_coeffs(mu: DiscreteMeasure, n: int, method: str = "rkpw", prec: str = "d", dps: int = 50) -> JacobiCoeffs:
    if method == "rkpw":
        return jacobi_rkpw(mu, n, prec)
    if method == "lanczos":
        return jacobi_lanczos(mu, n)
    if method == "mp":
        a, b2 = jacobi_mp(mu, n, dps)
        return JacobiCoeffs(np.array([float(v) for v in a]), np.array([float(v) for v in b2]), "mp", f"dps{dps}", mu.mass)
    raise ValueError(f"unknown method {method!r}; use 'rkpw', 'lanczos' or 'mp'")
```

Add to `src/jacobi_asym/jacobi/__init__.py`:
```python
from .lanczos import jacobi_lanczos
from .dispatch import jacobi_coeffs
```
Also add `"jacobi_lanczos", "jacobi_coeffs"` to `__all__`.

- [ ] **Step 4: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_jacobi_dispatch.py -v`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/jacobi tests/test_jacobi_dispatch.py
git commit -m "toolkit: Lanczos cross-check engine and jacobi_coeffs dispatcher

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Exact reference families (Lommel and Tricomi–Carlitz)

**Files:**
- Create: `src/jacobi_asym/measures/reference.py`
- Modify: `src/jacobi_asym/measures/__init__.py`
- Test: `tests/test_reference_families.py`

**Interfaces:**
- Produces:
  - `lommel_coeffs(nu, n, variant='even') -> tuple[list[Fraction|mpf], list[...]]`. With
    c²(m) = 1/(4(m+ν+1)(m+ν+2)) and c²(−1) = 0:
    - even: a_j = c²(2j−3) + c²(2j−2), b_j² = c²(2j−2)c²(2j−1);
    - odd: a_j = c²(2j−2) + c²(2j−1), b_j² = c²(2j−1)c²(2j).

    The result is exact `Fraction` if `nu` is a Fraction or int, and mpf otherwise.
  - `tc_coeffs(alpha, n, variant='even')`. With λ(m) = m/((m+α)(m+α−1)) and λ(0) = 0:
    - even: a_j = λ(2j−2) + λ(2j−1), b_j² = λ(2j−1)λ(2j);
    - odd: a_j = λ(2j−1) + λ(2j), b_j² = λ(2j)λ(2j+1).

    The same Fraction/mpf rule applies.
  - `lommel_measure(nu, K, dps=30) -> DiscreteMeasure`. Atoms j_{ν,k}^{−2} and weights 4(ν+1)j_{ν,k}^{−2}
    (total mass 1), via `mp.besseljzero`; slow, so keep K ≤ ~300.

  These are the closed forms of math-pursuits item 11, PROOF.md §2 (Theorem A) and §7 (TC fact, α = 1:
  b_j² = 1/(2j(2j+1))). The folding relations were rechecked on 2026-10-13: TC by continued fraction G(x) = xF(x²)
  to 1e−41, odd variants by the Christoffel step J = LLᵀ → LᵀL to 1e−51.

- [ ] **Step 1: Write the failing tests `tests/test_reference_families.py`**

```python
from fractions import Fraction as F
import math
import mpmath as mp
import pytest
from jacobi_asym.measures import lommel_coeffs, tc_coeffs, lommel_measure
from jacobi_asym.jacobi import jacobi_coeffs


def _poch(a, n):
    r = F(1)
    for i in range(n):
        r *= a + i
    return r


def _lommel_moments(nu, R):
    # moments of sigma~ (atoms j^{-2}): m_r = [t^r] A(t)/B(t), A = 0F1(;nu+2;-t/4)-type series, B = 0F1(;nu+1;-t/4)
    A = [F((-1) ** i, 4 ** i * math.factorial(i)) / _poch(nu + 2, i) for i in range(R)]
    B = [F((-1) ** i, 4 ** i * math.factorial(i)) / _poch(nu + 1, i) for i in range(R)]
    q = []
    for r in range(R):
        q.append((A[r] - sum(q[i] * B[r - i] for i in range(r))) / B[0])
    return q


def _stieltjes_exact(m, n):
    def ip(p, q):
        return sum(p[i] * q[j] * m[i + j] for i in range(len(p)) for j in range(len(q)))
    Pm, Pc, nm = None, [F(1)], None
    nc = ip(Pc, Pc)
    a, b2 = [], []
    for _ in range(n):
        al = ip([F(0)] + Pc, Pc) / nc
        Pn = [F(0)] + Pc
        Pn = [Pn[i] - al * (Pc[i] if i < len(Pc) else 0) for i in range(len(Pn))]
        if Pm is not None:
            Pn = [Pn[i] - (nc / nm) * (Pm[i] if i < len(Pm) else 0) for i in range(len(Pn))]
        nn = ip(Pn, Pn)
        a.append(al)
        b2.append(nn / nc)
        Pm, Pc, nm, nc = Pc, Pn, nc, nn
    return a, b2


@pytest.mark.parametrize("nu", [F(1, 2), F(0), F(1), F(-1, 2), F(7, 3)])
def test_lommel_closed_form_equals_exact_moments(nu):
    n = 7
    mom = _lommel_moments(nu, 2 * n + 3)
    a, b2 = _stieltjes_exact(mom, n)
    ae, be = lommel_coeffs(nu, n, "even")
    assert a == ae and b2[: n - 1] == be[: n - 1]
    a, b2 = _stieltjes_exact(mom[1:], n - 1)
    ao, bo = lommel_coeffs(nu, n - 1, "odd")
    assert a == ao and b2[: n - 2] == bo[: n - 2]


def test_tc_alpha1_values():
    a, b2 = tc_coeffs(1, 4)
    assert b2 == [F(1, 2 * j * (2 * j + 1)) for j in range(1, 5)]
    assert a == [F(1, 2), F(1, 3) + F(1, 4), F(1, 5) + F(1, 6), F(1, 7) + F(1, 8)]
    _, bo = tc_coeffs(1, 3, "odd")
    assert bo == [F(1, (2 * j + 1) * (2 * j + 2)) for j in range(1, 4)]


@pytest.mark.parametrize("alpha", [mp.mpf("0.5"), 1, 3])
def test_tc_even_continued_fraction_folding(alpha):
    # symmetric zero-diagonal J-fraction with off-diagonal^2 lambda_m equals x F(x^2) with the folded coefficients
    with mp.workdps(40):
        al = mp.mpf(alpha)
        lam = lambda m: mp.mpf(0) if m == 0 else m / ((m + al) * (m + al - 1))
        Nt = 3000
        a, b2 = tc_coeffs(al, Nt)
        for x in (mp.mpc("0.3", "0.4"), mp.mpc(2, 1)):
            g = mp.mpf(0)
            for m in range(2 * Nt, 0, -1):
                g = lam(m) / (x - g)
            G = 1 / (x - g)
            f = mp.mpf(0)
            for j in range(Nt, 0, -1):
                f = 1 / (x * x - a[j - 1] - (b2[j - 1] if j < Nt else 0) * f)
            assert abs(G - x * f) / abs(G) < mp.mpf(10) ** -30


def test_odd_variants_by_christoffel_step():
    with mp.workdps(50):
        for coeffs, par in ((tc_coeffs, mp.mpf(1)), (lommel_coeffs, mp.mpf("0.5"))):
            n = 12
            a, b2 = coeffs(par, n, "even")
            J = mp.matrix(n, n)
            for j in range(n):
                J[j, j] = a[j]
                if j < n - 1:
                    J[j, j + 1] = J[j + 1, j] = mp.sqrt(b2[j])
            L = mp.cholesky(J)
            Jp = L.T * L
            ao, bo = coeffs(par, n, "odd")
            assert max(abs(Jp[j, j] - ao[j]) for j in range(n - 1)) < mp.mpf(10) ** -40
            assert max(abs(Jp[j, j + 1] ** 2 - bo[j]) for j in range(n - 2)) < mp.mpf(10) ** -40


def test_lommel_measure_converges_to_closed_form():
    # truncating to K atoms drops ~1/K of the mass: measured rel. deviation of b_1..b_5^2 is ~4e-3 at K = 200
    _, b2 = lommel_coeffs(mp.mpf("0.5"), 5)
    dev = {}
    for K in (200, 400):
        r = jacobi_coeffs(lommel_measure(0.5, K), 5, method="mp", dps=40)
        dev[K] = max(abs(r.b2[j] / float(b2[j]) - 1) for j in range(5))
    assert dev[200] < 1e-2
    assert dev[400] < 0.6 * dev[200]
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_reference_families.py -v`
Expected: FAIL with `ImportError: cannot import name 'lommel_coeffs'`.

- [ ] **Step 3: Implement `src/jacobi_asym/measures/reference.py`**

```python
"""Exactly solvable reference families (math-pursuits item 11, PROOF.md Thm A and §7 TC fact).

Lommel (p = 2): K_nu has zero diagonal and off-diagonal c_m = 1/(2 sqrt((m+nu+1)(m+nu+2))); folding its spectral
measure to u = x^2 gives atoms j_{nu,k}^{-2} ('even'); 'odd' is u * that measure.  Tricomi-Carlitz (p = 1):
off-diagonal^2 lambda_m = m/((m+alpha)(m+alpha-1)), atoms 1/(k+alpha), k >= 0.
"""
from fractions import Fraction
import mpmath as mp
import numpy as np
from .base import DiscreteMeasure


def _num(v):
    return Fraction(v) if isinstance(v, (int, Fraction)) else mp.mpf(v)


def _fold(lam, n, variant):
    if variant == "even":
        return [lam(2 * j - 2) + lam(2 * j - 1) for j in range(1, n + 1)], [lam(2 * j - 1) * lam(2 * j) for j in range(1, n + 1)]
    if variant == "odd":
        return [lam(2 * j - 1) + lam(2 * j) for j in range(1, n + 1)], [lam(2 * j) * lam(2 * j + 1) for j in range(1, n + 1)]
    raise ValueError("variant must be 'even' or 'odd'")


def lommel_coeffs(nu, n: int, variant: str = "even"):
    nu = _num(nu)
    # lam(q) := c^2_{q-1} = off-diagonal^2 between rows q-1 and q of K_nu; lam(0) = 0
    lam = lambda q: 0 * nu if q == 0 else 1 / (4 * (q + nu) * (q + nu + 1))
    return _fold(lam, n, variant)


def tc_coeffs(alpha, n: int, variant: str = "even"):
    al = _num(alpha)
    lam = lambda m: 0 * al if m == 0 else m / ((m + al) * (m + al - 1))
    return _fold(lam, n, variant)


def lommel_measure(nu: float, K: int, dps: int = 30) -> DiscreteMeasure:
    with mp.workdps(dps):
        j = [mp.besseljzero(mp.mpf(nu), k) for k in range(1, K + 1)]
        x = np.array([float(1 / t ** 2) for t in j])
    return DiscreteMeasure(x, 4 * (nu + 1) * x, label=f"lommel(nu={nu}, K={K})")
```

Check the index shift: with lam(q) = c²_{q−1}, the even a_j = lam(2j−2) + lam(2j−1) = c²_{2j−3} + c²_{2j−2}, and
b_j² = lam(2j−1)lam(2j) = c²_{2j−2}c²_{2j−1}. Both match the Interfaces block.

Add to `src/jacobi_asym/measures/__init__.py`:
```python
from .reference import lommel_coeffs, tc_coeffs, lommel_measure
```
Also extend `__all__`.

- [ ] **Step 4: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_reference_families.py -v`
Expected: 11 passed (5 parametrized Lommel cases, the TC values test, 3 TC folding cases, Christoffel, and the
measure convergence test).

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/measures tests/test_reference_families.py
git commit -m "toolkit: exact Lommel and Tricomi-Carlitz reference coefficients (even/odd), Lommel measure

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Law-P constants, the Weyl-inversion predictor and averaged statistics

**Files:**
- Create: `src/jacobi_asym/laws/__init__.py`, `src/jacobi_asym/laws/weyl.py`, `src/jacobi_asym/laws/averaged.py`
- Test: `tests/test_laws.py`

**Interfaces:**
- Produces:
  - `I_p(p) -> float`, defined as (√π/2)Γ(1/p+½)/Γ(1/p+1).
  - `c_p(p) -> float`, defined as ¼(π/(2I(p)))^p.
  - `K_weyl(alpha, beta, p) -> float`, defined as (1/π)∫₀^∞ arccos(clip((u^p−α)/(2β))) du.
  - `weyl_count(eps, a, b) -> float`.
  - `predict_b(n: int, f, finv) -> float`. f(ξ) is a decreasing atom function on ξ ≥ ½ and
    finv(B) = f^{−1}(B). The result is b_n^W from (P): n = Σ_{k≤k0}(1−B/f(k))^{−1/2} + ∫_{k0+½}^{ξ_B}(1−B/f(ξ))^{−1/2}dξ
    with k0 = ⌊ξ_B/2⌋ and B = 4b_n. Raises `ValueError` for n < 2.
  - `averaged_law(b, x, p, ns) -> dict[int, float]`, where
    S_n = (2/n²)Σ_{j=1}^{n−1}(n−j) log(b_j/x_j) − log c(p), for each n in `ns`. Requires len(b) ≥ n−1.

- [ ] **Step 1: Write the failing tests `tests/test_laws.py`**

```python
import numpy as np
import pytest
from jacobi_asym.laws import I_p, c_p, K_weyl, predict_b, averaged_law, weyl_count


def test_constants():
    assert c_p(1) == pytest.approx(0.5, rel=1e-14)
    assert c_p(2) == pytest.approx(np.pi ** 2 / 16, rel=1e-14)
    assert I_p(2) == pytest.approx(np.pi / 4, rel=1e-14)
    for p in (1, 1.5, 2, 3):
        assert K_weyl(2 * c_p(p), c_p(p), p) == pytest.approx(1.0, abs=1e-8)
    assert K_weyl(2.0, 1.0, 2) == pytest.approx(4 / np.pi, abs=1e-8)


def test_weyl_count_toeplitz():
    # N x N Toeplitz a=1, b=0.25: eigenvalues 1 + 0.5 cos(pi i/(N+1)); count above 1 is N/2 within 1
    a = np.ones(100); b = 0.25 * np.ones(100)
    assert abs(weyl_count(1.0, a, b) - 50) <= 1


@pytest.mark.parametrize("p", [1, 2, 3])
def test_predict_b_pure_powers(p):
    f = lambda xi: np.asarray(xi, float) ** (-p)
    finv = lambda B: B ** (-1.0 / p)
    r = predict_b(1000, f, finv) / f(1000) / c_p(p)
    assert abs(r - 1) < 2e-3          # observed 1 - p/(2n) + ... (0.999001 for p = 2)
    assert predict_b(100, f, finv) > predict_b(1000, f, finv)


def test_predict_b_small_n_rejected():
    with pytest.raises(ValueError, match="n >= 2"):
        predict_b(1, lambda xi: xi ** -2.0, lambda B: B ** -0.5)


def test_averaged_law_on_exact_ratio():
    # b_j/x_j == c(p) exactly: (2/n^2) sum_{j<n}(n-j) = (n-1)/n, so S_n = -log c(p) / n (item-11 convention)
    j = np.arange(1, 501, dtype=float)
    x = j ** -2.0
    b = c_p(2) * x
    S = averaged_law(b, x, 2, [10, 100, 500])
    for n, v in S.items():
        assert v == pytest.approx(-np.log(c_p(2)) / n, abs=1e-13)
    with pytest.raises(ValueError):
        averaged_law(b, x, 2, [600])
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_laws.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'jacobi_asym.laws'`.

- [ ] **Step 3: Implement**

`src/jacobi_asym/laws/weyl.py`:
```python
"""Law-P constants and the Weyl-law (local arcsine) predictor (item 11 note (W), (P); PROOF.md section 1)."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma

_GL = np.polynomial.legendre.leggauss(200)


def I_p(p: float) -> float:
    return float(np.sqrt(np.pi) / 2 * gamma(1 / p + 0.5) / gamma(1 / p + 1))


def c_p(p: float) -> float:
    return float(0.25 * (np.pi / (2 * I_p(p))) ** p)


def K_weyl(alpha: float, beta: float, p: float) -> float:
    def th(u):
        s = (u ** p - alpha) / (2 * beta)
        return np.arccos(np.clip(s, -1.0, 1.0))
    top = (alpha + 2 * beta) ** (1 / p)
    pts = [(alpha - 2 * beta) ** (1 / p)] if alpha - 2 * beta > 0 else None
    return float(quad(th, 0, top, points=pts, limit=200, epsabs=1e-12, epsrel=1e-12)[0] / np.pi)


def weyl_count(eps: float, a, b) -> float:
    z = np.clip((eps - np.asarray(a, float)) / (2 * np.asarray(b, float)), -1, 1)
    return float(np.sum(np.arccos(z)) / np.pi)


def _n_of_B(B, f, finv):
    t, w = _GL
    xiB = float(finv(B))
    k0 = int(np.floor(xiB / 2))
    s = 0.0
    if k0 >= 1:
        k = np.arange(1, k0 + 1, dtype=float)
        s = float(np.sum(1 / np.sqrt(-np.expm1(np.log(B) - np.log(f(k))))))
    lo = k0 + 0.5 if k0 >= 1 else 0.5
    u = (t + 1) / 2
    xi = xiB - (xiB - lo) * u ** 2                     # removes the (xi_B - xi)^{-1/2} singularity
    integrand = 2 * (xiB - lo) * u / np.sqrt(-np.expm1(np.log(B) - np.log(f(xi))))
    return s + float(np.sum(w / 2 * integrand))


def predict_b(n: int, f, finv) -> float:
    """b_n^W from the smoothed Weyl inversion (P).  f: decreasing atom function on xi >= 1/2, finv its inverse."""
    if n < 2:
        raise ValueError("predict_b needs n >= 2 (the bracket degenerates at n = 1)")
    g = lambda lB: _n_of_B(np.exp(lB), f, finv) - n
    lB = brentq(g, np.log(f(2.0 * n + 2)), np.log(f(1.0)), xtol=1e-14)
    return float(np.exp(lB) / 4)
```

`src/jacobi_asym/laws/averaged.py`:
```python
"""Averaged (doubly-Cesaro, geometric) Law-P statistic of PROOF.md Thm H / H_L."""
import numpy as np
from .weyl import c_p


def averaged_law(b, x, p: float, ns) -> dict:
    b = np.asarray(b, float)
    x = np.asarray(x, float)
    lj = np.log(b / x[: b.size])
    lc = np.log(c_p(p))
    out = {}
    for n in ns:
        if n < 2 or n - 1 > b.size:
            raise ValueError(f"need 2 <= n <= len(b) + 1 = {b.size + 1}; got {n}")
        j = np.arange(1, n)
        out[int(n)] = float(2 / n ** 2 * np.sum((n - j) * lj[: n - 1]) - lc)
    return out
```

`src/jacobi_asym/laws/__init__.py`:
```python
from .weyl import I_p, c_p, K_weyl, weyl_count, predict_b
from .averaged import averaged_law

__all__ = ["I_p", "c_p", "K_weyl", "weyl_count", "predict_b", "averaged_law"]
```

- [ ] **Step 4: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_laws.py -v`
Expected: 7 passed.

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/laws tests/test_laws.py
git commit -m "toolkit: Law-P constants, Weyl-inversion predictor (P), averaged statistic S_n

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Hankel tools: log D_n, Heine sum, difference ratios

**Files:**
- Create: `src/jacobi_asym/hankel/__init__.py`, `src/jacobi_asym/hankel/logdet.py`,
  `src/jacobi_asym/hankel/heine.py`, `src/jacobi_asym/hankel/compare.py`
- Test: `tests/test_hankel.py`

**Interfaces:**
- Consumes: `DiscreteMeasure`, `JacobiCoeffs`.
- Produces:
  - `log_hankel(jc: JacobiCoeffs, n) -> float`, defined as n·log m₀ + Σ_{j<n}(n−j)·log b_j² (H2). Requires
    n−1 ≤ len(jc.b2).
  - `hankel_det_mp(mu, n, dps=50) -> mpf`, defined as det(m_{i+j})_{i,j<n} from exact moments in mpmath.
  - `heine_sum_mp(mu, n, dps=50) -> mpf`, defined as Σ_{|S|=n} Π w Π_{i<j}(x_i−x_j)². It enumerates subsets, so
    it is for N ≤ 14.
  - `difference_ratio(f, g, a, b) -> float`, defined as (f(a)−f(b))/(g(a)−g(b)).

- [ ] **Step 1: Write the failing tests `tests/test_hankel.py`**

```python
import numpy as np
import mpmath as mp
import pytest
from jacobi_asym.measures import DiscreteMeasure, pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.hankel import log_hankel, hankel_det_mp, heine_sum_mp, difference_ratio


def _mu():
    rng = np.random.default_rng(3)
    return DiscreteMeasure.from_atoms(rng.uniform(0.05, 1.0, 9), rng.uniform(0.2, 1.5, 9))


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_heine_equals_hankel_det(n):
    mu = _mu()
    d1, d2 = hankel_det_mp(mu, n, dps=60), heine_sum_mp(mu, n, dps=60)
    assert abs(d1 / d2 - 1) < mp.mpf(10) ** -40


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_h2_identity(n):
    mu = _mu()
    jc = jacobi_coeffs(mu, 7, method="mp", dps=60)
    assert log_hankel(jc, n) == pytest.approx(float(mp.log(hankel_det_mp(mu, n, dps=60))), abs=1e-10)


def test_log_hankel_bounds():
    jc = jacobi_coeffs(pure_power(2, 100), 10)
    with pytest.raises(ValueError):
        log_hankel(jc, 12)


def test_difference_ratio_lemma_H5_pure_power_log():
    # f = xi^-2 L, L = log(e + xi) nondecreasing: ratio vs g = xi^-2 lies in [(1-eps*(a)/2) L(a), L(a)]
    L = lambda t: np.log(np.e + t)
    f = lambda t: t ** -2.0 * L(t)
    g = lambda t: t ** -2.0
    for a, b in [(1.0, 2.0), (3.0, 1e4), (100.0, 101.0)]:
        r = difference_ratio(f, g, a, b)
        assert r <= L(a) * (1 + 1e-12)
        assert r >= (1 - 0.5 / np.log(np.e + a)) * L(a) * (1 - 1e-12)   # eps(t) = t/((e+t) L(t)) <= 1/L(t)
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_hankel.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'jacobi_asym.hankel'`.

- [ ] **Step 3: Implement**

`src/jacobi_asym/hankel/logdet.py`:
```python
"""log D_n via H2: D_n = m_0^n prod_{j<n} b_j^{2(n-j)} (item 11 PROOF.md Lemma H2)."""
import numpy as np
from ..jacobi.result import JacobiCoeffs


def log_hankel(jc: JacobiCoeffs, n: int) -> float:
    b2 = np.asarray(jc.b2, float)
    if n < 1 or n - 1 > b2.size:
        raise ValueError(f"need 1 <= n <= len(b2) + 1 = {b2.size + 1}; got {n}")
    j = np.arange(1, n)
    return float(n * np.log(jc.mass) + np.sum((n - j) * np.log(b2[: n - 1])))
```

`src/jacobi_asym/hankel/heine.py`:
```python
"""Exact (mpmath) Hankel determinant and Heine/Andreief sum for small measures (cross-checks)."""
from itertools import combinations
import mpmath as mp
from ..measures.base import DiscreteMeasure


def hankel_det_mp(mu: DiscreteMeasure, n: int, dps: int = 50):
    with mp.workdps(dps):
        x = [mp.mpf(float(v)) for v in mu.atoms]
        w = [mp.mpf(float(v)) for v in mu.weights]
        m = [mp.fsum(wi * xi ** r for xi, wi in zip(x, w)) for r in range(2 * n - 1)]
        return mp.det(mp.matrix([[m[i + j] for j in range(n)] for i in range(n)]))


def heine_sum_mp(mu: DiscreteMeasure, n: int, dps: int = 50):
    if mu.N > 14:
        raise ValueError("heine_sum_mp enumerates subsets; use N <= 14")
    with mp.workdps(dps):
        x = [mp.mpf(float(v)) for v in mu.atoms]
        w = [mp.mpf(float(v)) for v in mu.weights]
        tot = mp.mpf(0)
        for S in combinations(range(len(x)), n):
            t = mp.fprod(w[i] for i in S)
            for i, j in combinations(S, 2):
                t *= (x[i] - x[j]) ** 2
            tot += t
        return tot
```

`src/jacobi_asym/hankel/compare.py`:
```python
"""Difference-ratio tool for Lemmas H4/H5 (item 11 PROOF.md section 7b)."""


def difference_ratio(f, g, a: float, b: float) -> float:
    if not a < b:
        raise ValueError("need a < b")
    return float((f(a) - f(b)) / (g(a) - g(b)))
```

`src/jacobi_asym/hankel/__init__.py`:
```python
from .logdet import log_hankel
from .heine import hankel_det_mp, heine_sum_mp
from .compare import difference_ratio

__all__ = ["log_hankel", "hankel_det_mp", "heine_sum_mp", "difference_ratio"]
```

- [ ] **Step 4: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_hankel.py -v`
Expected: 12 passed.

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/hankel tests/test_hankel.py
git commit -m "toolkit: Hankel tools (H2 log-det, exact Hankel/Heine cross-check, difference ratios)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 8: L-function measure sources (smooth models, true zeros, synthetic) and data fetching

**Files:**
- Create: `src/jacobi_asym/measures/lfun.py`, `src/jacobi_asym/measures/synthetic.py`, `data/fetch.py`,
  `data/SHA256SUMS`
- Modify: `src/jacobi_asym/measures/__init__.py`, `PROVENANCE.md`
- Test: `tests/test_lfun_sources.py`

**Interfaces:**
- Consumes: `DiscreteMeasure.from_atoms(..., tail=...)`.
- Produces (ported from item 11 `measures.py`):
  - `Nsmooth(T, q=1)`, `Ninv(N, q=1)`, `model_zeros(J, q=1, j0=1)` and `tail_nodes(Tstart, q=1, Tend=1e18,
    ratio=1.05, k=6)`.
  - `zero_measure(gammas, q=1, tail=True) -> DiscreteMeasure`, with x = 1/(γ²+¼) and w = 2x, plus the smooth tail
    beyond the last ordinate.
  - `smooth_zeta(J, q=1, tail=True) -> DiscreteMeasure`.
  - `load_odlyzko(M=None, root=None) -> np.ndarray`.
  - `true_zeta(M=None, tail=True) -> DiscreteMeasure`.
  - `DataMissing(FileNotFoundError)`.
  - `synthetic_unfolded(kind, J, seed, m=1000)`, where kind is 'smooth', 'cue', 'poisson' or 'jitter'.
  - `synthetic_zeta(kind, J, seed) -> DiscreteMeasure`.
  - `data/fetch.py odlyzko`. This uses the local math-pursuits copy if present, otherwise downloads; it verifies the
    sha256 and writes `data/raw/zeta_zeros_odlyzko6.npy`.

- [ ] **Step 1: Write the failing tests `tests/test_lfun_sources.py`**

```python
import hashlib
import numpy as np
import pytest
from jacobi_asym.measures import (Nsmooth, Ninv, model_zeros, smooth_zeta, zero_measure, load_odlyzko,
                                  DataMissing, synthetic_unfolded, synthetic_zeta)


def test_Ninv_inverts_Nsmooth():
    for q in (1, 3, 4):
        T = np.array([20.0, 100.0, 1e4, 1e8])
        assert np.allclose(Ninv(Nsmooth(T, q), q), T, rtol=1e-12)


def test_model_zeros_gram_convention():
    g = model_zeros(1000)
    assert np.all(np.diff(g) > 0)
    assert np.allclose(Nsmooth(g), np.arange(1, 1001) - 0.5, atol=1e-8)


def test_smooth_zeta_measure_structure():
    mu = smooth_zeta(5000)
    assert mu.N > 5000                      # tail nodes appended
    g = model_zeros(5000)
    assert np.allclose(mu.atoms[:5000], 1 / (g ** 2 + 0.25))
    assert np.allclose(mu.weights[:5000], 2 * mu.atoms[:5000])


def test_zero_measure_mass_close_to_zeta_constant():
    # total mass of sum_rho 1/(rho(1-rho)) = 2 + gamma_E - log(4 pi) ~ 0.04619; smooth model is close (~1e-3)
    mu = smooth_zeta(100000)
    assert abs(mu.mass - (2 + np.euler_gamma - np.log(4 * np.pi))) < 5e-3


def test_load_odlyzko_missing_message(tmp_path):
    with pytest.raises(DataMissing, match="fetch.py odlyzko"):
        load_odlyzko(10, root=tmp_path)


def test_synthetic_deterministic_and_mean_spacing():
    u1, u2 = synthetic_unfolded("cue", 2000, seed=1), synthetic_unfolded("cue", 2000, seed=1)
    assert np.array_equal(u1, u2)
    assert abs(np.mean(np.diff(synthetic_unfolded("poisson", 20000, seed=2))) - 1) < 0.03
    mu = synthetic_zeta("jitter", 3000, seed=1)
    assert mu.N > 3000


def test_fetch_sha256_helper(tmp_path):
    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("fetch", pathlib.Path(__file__).parents[1] / "data" / "fetch.py")
    fetch = importlib.util.module_from_spec(spec); spec.loader.exec_module(fetch)
    p = tmp_path / "x.bin"; p.write_bytes(b"abc")
    assert fetch.sha256(p) == hashlib.sha256(b"abc").hexdigest()


@pytest.mark.data
def test_true_zeta_if_data_present():
    try:
        g = load_odlyzko(100)
    except DataMissing:
        pytest.skip("Odlyzko data not fetched")
    assert abs(g[0] - 14.134725141734693) < 1e-8
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_lfun_sources.py -v`
Expected: FAIL with `ImportError: cannot import name 'Nsmooth'`.

- [ ] **Step 3: Implement `src/jacobi_asym/measures/lfun.py`**

```python
"""Measures from L-function zero ordinates gamma (taken as REAL numbers on the critical line: an input, not
evidence; item 11 E1).  sigma = sum_j 2 x_j delta_{x_j}, x_j = 1/(gamma_j^2 + 1/4), plus a smooth
Riemann-von Mangoldt tail beyond the last tabulated ordinate (ported from math-pursuits item 11 measures.py)."""
from pathlib import Path
import numpy as np
from scipy.special import lambertw
from .base import DiscreteMeasure

CONST = {1: 7 / 8, 4: 1 / 8, 3: 1 / 8}
DATA_ROOT = Path(__file__).resolve().parents[3] / "data" / "raw"


class DataMissing(FileNotFoundError):
    pass


def Nsmooth(T, q=1):
    T = np.asarray(T, float)
    return T / (2 * np.pi) * np.log(q * T / (2 * np.pi * np.e)) + CONST[q]


def Ninv(N, q=1):
    y = (np.asarray(N, float) - CONST[q]) * q / np.e
    return 2 * np.pi * np.e / q * np.exp(lambertw(y).real)


def model_zeros(J, q=1, j0=1):
    return Ninv(np.arange(j0, J + 1) - 0.5, q)


def tail_nodes(Tstart, q=1, Tend=1e18, ratio=1.05, k=6):
    u0, u1 = np.log(Tstart), np.log(Tend)
    edges = np.arange(u0, u1 + np.log(ratio), np.log(ratio))
    t, wt = np.polynomial.legendre.leggauss(k)
    U, W = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        U.append((a + b) / 2 + (b - a) / 2 * t)
        W.append((b - a) / 2 * wt)
    U, W = np.concatenate(U), np.concatenate(W)
    T = np.exp(U)
    dens = np.log(q * T / (2 * np.pi)) / (2 * np.pi) * T
    return T, W * dens


def _atoms(g, mult=None):
    x = 1 / (np.asarray(g, float) ** 2 + 0.25)
    return x, (2 * x if mult is None else 2 * x * mult)


def zero_measure(gammas, q=1, tail=True, label="", **tailkw) -> DiscreteMeasure:
    g = np.asarray(gammas, float)
    x, w = _atoms(g)
    t = None
    if tail:
        T, m = tail_nodes(Ninv(len(g) + 0.5, q), q, **tailkw)
        t = _atoms(T, m)
    return DiscreteMeasure.from_atoms(x, w, tail=t, label=label or f"zero_measure(q={q}, M={len(g)}, tail={tail})")


def smooth_zeta(J, q=1, tail=True) -> DiscreteMeasure:
    return zero_measure(model_zeros(J, q), q, tail, label=f"smooth_zeta(J={J}, q={q})")


def load_odlyzko(M=None, root=None) -> np.ndarray:
    f = Path(root or DATA_ROOT) / "zeta_zeros_odlyzko6.npy"
    if not f.exists():
        raise DataMissing(f"{f} not found: run `.venv/bin/python data/fetch.py odlyzko`")
    g = np.load(f)
    return g if M is None else g[:M]


def true_zeta(M=None, tail=True) -> DiscreteMeasure:
    return zero_measure(load_odlyzko(M), 1, tail, label=f"true_zeta(M={M}, tail={tail})")
```

`src/jacobi_asym/measures/synthetic.py`:
```python
"""Synthetic unfolded point processes with the zeta counting function (ported from item 11 synth.py)."""
import numpy as np
from .lfun import Ninv, zero_measure


def synthetic_unfolded(kind: str, J: int, seed: int, m: int = 1000) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if kind == "smooth":
        return np.arange(1, J + 1) - 0.5
    if kind == "poisson":
        return np.cumsum(rng.exponential(1.0, J)) - 0.5
    if kind == "jitter":
        return np.arange(1, J + 1) - 0.5 + rng.uniform(-0.5, 0.5, J)
    if kind == "cue":
        us = []
        for blk in range(-(-J // m)):
            Z = (rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))) / np.sqrt(2)
            Qm, R = np.linalg.qr(Z)
            d = np.diag(R)
            Qm = Qm * (d / np.abs(d))
            th = np.sort(np.mod(np.angle(np.linalg.eigvals(Qm)), 2 * np.pi))
            us.append(blk * m + m * th / (2 * np.pi))
        return np.sort(np.concatenate(us))[:J]
    raise ValueError(f"unknown kind {kind!r}")


def synthetic_zeta(kind: str, J: int, seed: int):
    u = synthetic_unfolded(kind, J, seed)
    u = u[u > 0.05]
    return zero_measure(Ninv(u), 1, True, label=f"synthetic_zeta({kind}, J={J}, seed={seed})")
```

Add to `src/jacobi_asym/measures/__init__.py`:
```python
from .lfun import (Nsmooth, Ninv, model_zeros, tail_nodes, zero_measure, smooth_zeta, load_odlyzko, true_zeta,
                   DataMissing)
from .synthetic import synthetic_unfolded, synthetic_zeta
```
Also extend `__all__`.

`data/fetch.py`:
```python
"""Fetch large data into data/raw (gitignored) and verify sha256.  Usage: python data/fetch.py odlyzko"""
import gzip
import hashlib
import shutil
import sys
import urllib.request
from pathlib import Path
import numpy as np

RAW = Path(__file__).resolve().parent / "raw"
LOCAL = Path("/mnt/c/Users/gspea/source/repos/math-pursuits/items/11-zero-measure-jacobi-asymptotics/work/data/odlyzko/zeros6.gz")
URL = "https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6.gz"
SHA = {"zeros6.gz": "6acacb4707c429bf368f32823a8eef0e0737b6318d3e144c78975a4986d155da"}


def sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def odlyzko():
    RAW.mkdir(parents=True, exist_ok=True)
    gz = RAW / "zeros6.gz"
    if not gz.exists():
        if LOCAL.exists():
            shutil.copyfile(LOCAL, gz)
        else:
            urllib.request.urlretrieve(URL, gz)
    if sha256(gz) != SHA["zeros6.gz"]:
        raise SystemExit(f"sha256 mismatch for {gz}")
    with gzip.open(gz, "rt") as f:
        g = np.array([float(l) for l in f if l.strip()])
    if g.size != 2001052 or not np.all(np.diff(g) > 0):
        raise SystemExit("unexpected zeros6 content")
    np.save(RAW / "zeta_zeros_odlyzko6.npy", g)
    print("ok", g.size, sha256(RAW / "zeta_zeros_odlyzko6.npy"))


if __name__ == "__main__":
    {"odlyzko": odlyzko}[sys.argv[1]]()
```

`data/SHA256SUMS`:
```
6acacb4707c429bf368f32823a8eef0e0737b6318d3e144c78975a4986d155da  raw/zeros6.gz
9062f83edd01af3803e848c3ff894a328e595f46bd2085b6356e3d30acc367be  raw/zeta_zeros_odlyzko6.npy
```

Append these rows to `PROVENANCE.md`:
```
| src/jacobi_asym/measures/lfun.py | math-pursuits/items/11-*/work/measures.py | ported; DiscreteMeasure API |
| src/jacobi_asym/measures/synthetic.py | math-pursuits/items/11-*/work/synth.py | ported; CUE blocks truncated to J |
| data/fetch.py (Odlyzko zeros6) | A. Odlyzko, https://www-users.cse.umn.edu/~odlyzko/zeta_tables/ | sha256 from item 11 data/PROVENANCE.md |
```

- [ ] **Step 4: Confirm the tests pass, then fetch the data and rerun**

1. Run: `.venv/bin/python -m pytest tests/test_lfun_sources.py -v`
   Expected: 7 passed and 1 skipped (`test_true_zeta_if_data_present`).
2. Run: `.venv/bin/python data/fetch.py odlyzko`
   Expected: `ok 2001052 9062f83e...` (the npy sha256 should equal item 11's; if numpy's .npy header differs, record
   the new hash in SHA256SUMS and note it in PROVENANCE.md).
3. Run: `.venv/bin/python -m pytest tests/test_lfun_sources.py -v -m "data or not slow"`
   Expected: 8 passed.

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/measures data/fetch.py data/SHA256SUMS tests/test_lfun_sources.py PROVENANCE.md
git commit -m "toolkit: L-function zero measures (smooth RvM, Odlyzko true zeros, synthetic), data fetch with sha256

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 9: Certification layer (Arb balls)

**Files:**
- Create: `src/jacobi_asym/certify/__init__.py`, `src/jacobi_asym/certify/arb.py`
- Test: `tests/test_certify.py`

**Interfaces:**
- Consumes: `DiscreteMeasure`, `jacobi_mp` (as an independent reference in the tests only).
- Produces:
  - `certified_jacobi(mu, n, prec_bits=256) -> tuple[list[arb], list[arb]]`. These are ball enclosures of
    (a_1..a_n, b_1²..b_n²) for the measure whose atoms and weights are exactly the given float64 values: the
    discretized Stieltjes procedure in Arb arithmetic. Requires n < mu.N, and raises `ArithmeticError` if a norm ball
    contains 0.
  - `certified_cp(p: int) -> arb`, defined as ¼(π/(2I(p)))^p with I(p) = √π/2·Γ(1/p+½)/Γ(1/p+1).

- [ ] **Step 1: Write the failing tests `tests/test_certify.py`**

```python
import numpy as np
import mpmath as mp
import pytest
flint = pytest.importorskip("flint")
from flint import arb
from jacobi_asym.measures import DiscreteMeasure
from jacobi_asym.jacobi import jacobi_mp
from jacobi_asym.certify import certified_jacobi, certified_cp


def test_balls_contain_high_precision_reference():
    rng = np.random.default_rng(11)
    mu = DiscreteMeasure.from_atoms(rng.uniform(0.01, 1, 30), rng.uniform(0.1, 2, 30))
    A, B2 = certified_jacobi(mu, 12, prec_bits=300)
    a, b2 = jacobi_mp(mu, 12, dps=90)
    for ball, ref in zip(A + B2, a + b2):
        assert ball.overlaps(arb(mp.nstr(ref, 85)))
        assert float(ball.rad()) < 1e-40 * max(1.0, abs(float(ball.mid())))


def test_certified_cp():
    assert certified_cp(2).overlaps(arb.pi() ** 2 / 16)
    assert certified_cp(1).overlaps(arb(1) / 2)
    assert float(certified_cp(2).rad()) < 1e-60


def test_n_limit():
    mu = DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 1.0])
    with pytest.raises(ValueError, match="n < N"):
        certified_jacobi(mu, 2)
```

- [ ] **Step 2: Confirm the tests fail**

Run: `.venv/bin/python -m pytest tests/test_certify.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'jacobi_asym.certify'`.

- [ ] **Step 3: Implement**

`src/jacobi_asym/certify/arb.py`:
```python
"""CERTIFIED (ball-arithmetic) computations.  Atoms/weights are taken as the exact binary64 values given; every
operation is an Arb ball operation, so the returned balls contain the exact Jacobi coefficients of that measure."""
from flint import arb, ctx
from ..measures.base import DiscreteMeasure


def certified_jacobi(mu: DiscreteMeasure, n: int, prec_bits: int = 256):
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    old = ctx.prec
    ctx.prec = prec_bits
    try:
        x = [arb(float(v)) for v in mu.atoms]
        w = [arb(float(v)) for v in mu.weights]
        N = len(x)
        p_prev = [arb(0)] * N
        p = [arb(1)] * N
        nrm = sum(w, arb(0))
        nrm_prev = None
        A, B2 = [], []
        for _ in range(n):
            if nrm.contains(0):
                raise ArithmeticError("norm ball contains 0; increase prec_bits")
            ak = sum((w[i] * x[i] * p[i] * p[i] for i in range(N)), arb(0)) / nrm
            A.append(ak)
            if nrm_prev is None:
                p_next = [(x[i] - ak) * p[i] for i in range(N)]
            else:
                r = nrm / nrm_prev
                p_next = [(x[i] - ak) * p[i] - r * p_prev[i] for i in range(N)]
            nrm_next = sum((w[i] * p_next[i] * p_next[i] for i in range(N)), arb(0))
            B2.append(nrm_next / nrm)
            p_prev, p, nrm_prev, nrm = p, p_next, nrm, nrm_next
        return A, B2
    finally:
        ctx.prec = old


def certified_cp(p: int, prec_bits: int = 256):
    old = ctx.prec
    ctx.prec = prec_bits
    try:
        P = arb(p)
        I = arb.pi().sqrt() / 2 * arb.gamma(1 / P + arb(1) / 2) / arb.gamma(1 / P + 1)
        return (arb.pi() / (2 * I)) ** P / 4
    finally:
        ctx.prec = old
```

`src/jacobi_asym/certify/__init__.py`:
```python
from .arb import certified_jacobi, certified_cp

__all__ = ["certified_jacobi", "certified_cp"]
```

- [ ] **Step 4: Confirm the tests pass**

Run: `.venv/bin/python -m pytest tests/test_certify.py -v`
Expected: 3 passed. If `ball.overlaps` fails only on the b² entries, the Stieltjes recursion is losing precision.
Raise `prec_bits` in the test to 400 rather than loosening the 1e−40 radius bound.

- [ ] **Step 5: Commit**

```bash
git add src/jacobi_asym/certify tests/test_certify.py
git commit -m "toolkit: Arb-certified Jacobi coefficients for exact float measures; certified c(p)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 10: Regression against item 11, plus README usage

**Files:**
- Create: `tests/data/zeta_zeros_4000_dps60.txt` (copied), `tests/data/A10_b_zeta_4000atoms_n400.npz` (copied),
  `tests/test_regression_item11.py`
- Modify: `PROVENANCE.md`, `README.md`

**Interfaces:**
- Consumes: `zero_measure`, `smooth_zeta`, `jacobi_coeffs`, `averaged_law`, `pure_power`/`DiscreteMeasure`.
- Produces: none. These are tests only.

Recorded reference values:
- A10, from item 11 `checks/truncation_and_fits.py` [1]: RKPW matches A10's mpmath dps-100 b_n² to 4e−14 for
  4000 atoms and n ≤ 400.
- Smooth ζ model (smooth2M + tail), computed by item-11 code on 2026-10-13: S_100 = −0.12627466819980426,
  S_300 = −0.09699890257227572, S_1000 = −0.07455905815171271. RKPW took 20 s.
- H_L adversarial, from item 11 `proof/check_hankel_L_adv.out`: p=2, L=log(e+k)³, w=x, K=2·10⁶ gives
  S_300 = −0.11818 and S_1000 = −0.09009.

- [ ] **Step 1: Copy the fixtures and record provenance**

```bash
mkdir -p tests/data
cp /mnt/c/Users/gspea/source/repos/math-pursuits/items/11-zero-measure-jacobi-asymptotics/source/data/zeta_zeros_4000_dps60.txt tests/data/
cp /mnt/c/Users/gspea/source/repos/math-pursuits/items/11-zero-measure-jacobi-asymptotics/source/data/A10_b_zeta_4000atoms_n400.npz tests/data/
```

Append to the `PROVENANCE.md` table:
```
| tests/data/zeta_zeros_4000_dps60.txt | math-pursuits/items/11-*/source/data/ (orig. /home/gspea/grh) | first 4000 zeta ordinates, 60 digits |
| tests/data/A10_b_zeta_4000atoms_n400.npz | math-pursuits/items/11-*/source/data/ | A10 mpmath dps-100 b_n^2, n <= 400 (key b_sq) |
```

- [ ] **Step 2: Write the tests `tests/test_regression_item11.py`**

```python
from pathlib import Path
import numpy as np
import pytest
from jacobi_asym.measures import zero_measure, smooth_zeta, DiscreteMeasure
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import averaged_law

D = Path(__file__).parent / "data"


def test_A10_reproduction():
    g = np.array([float(l) for l in open(D / "zeta_zeros_4000_dps60.txt") if l.strip()])
    mu = zero_measure(g, tail=False)
    ref = np.load(D / "A10_b_zeta_4000atoms_n400.npz")["b_sq"]
    r = jacobi_coeffs(mu, 400)
    assert np.max(np.abs(r.b2 / ref - 1)) < 1e-12


@pytest.mark.slow
def test_smooth_zeta_averaged_law_item11():
    mu = smooth_zeta(2001052)
    r = jacobi_coeffs(mu, 1000)
    S = averaged_law(r.b, mu.atoms, 2, [100, 300, 1000])
    assert S[100] == pytest.approx(-0.12627466819980426, abs=1e-9)
    assert S[300] == pytest.approx(-0.09699890257227572, abs=1e-9)
    assert S[1000] == pytest.approx(-0.07455905815171271, abs=1e-9)


@pytest.mark.slow
def test_HL_adversarial_log_cubed():
    k = np.arange(1, 2_000_001, dtype=float)
    x = k ** -2.0 * np.log(np.e + k) ** 3
    mu = DiscreteMeasure(x, x.copy())
    r = jacobi_coeffs(mu, 1000)
    S = averaged_law(r.b, x, 2, [300, 1000])
    assert S[300] == pytest.approx(-0.11818, abs=6e-6)
    assert S[1000] == pytest.approx(-0.09009, abs=6e-6)
```

Note on S_1000 in `test_smooth_zeta_averaged_law_item11`: `averaged_law` needs b_1..b_999, and
`jacobi_coeffs(mu, 1000)` returns b_1..b_1000, so the input is sufficient.

- [ ] **Step 3: Run the fast and slow suites**

1. Run: `.venv/bin/python -m pytest -v`
   Expected: all fast tests pass; slow tests are deselected.
2. Run: `.venv/bin/python -m pytest -m slow -v`
   Expected: 2 passed, in about 1–2 minutes.

If `test_A10_reproduction` fails above 1e−12, compare with item 11's measure: x = 1/(γ²+¼) and w = 2x, with **no**
tail and atoms in descending order. Do not loosen the tolerance; item 11 recorded 4e−14.

- [ ] **Step 4: Add a usage section to `README.md`**

````markdown
## Quick use
```python
from jacobi_asym.measures import smooth_zeta, pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import c_p, averaged_law, predict_b

mu = pure_power(2, 200_000)                 # atoms k^-2, weights = atoms
r = jacobi_coeffs(mu, 2000)                 # RKPW, float64 (numerical)
print(r.b[1999] / mu.atoms[1999], c_p(2))   # b_n/x_n vs pi^2/16
print(averaged_law(r.b, mu.atoms, 2, [2000]))
```
Certified (Arb) coefficients for small exact-float measures: `jacobi_asym.certify.certified_jacobi`.
````

- [ ] **Step 5: Commit**

```bash
git add tests/data tests/test_regression_item11.py PROVENANCE.md README.md
git commit -m "toolkit: regression tests against item 11 (A10, smooth-zeta S_n, H_L adversarial); README usage

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

## Later plans (not in scope here)

- **Plan 2:** Lean core (spec §6).
- **Plan 3:** research G3′.
- **Plan 4:** research G2.
- **Plan 5:** research G1.

Each is written after this plan has been executed and reviewed.
