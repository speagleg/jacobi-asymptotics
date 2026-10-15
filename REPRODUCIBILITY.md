# Reproducibility (Plan 59)

Two tools let a reader check that the committed outputs are the ones the committed code produces, and that nothing
has changed since:

* **`MANIFEST.sha256`**: SHA-256 of every tracked file that carries a result, in `sha256sum` format.
* **`scripts/reproduce.sh`**: one command that rebuilds, retests and re-runs the checks, diffing each output against
  its committed `.out`.

## Integrity manifest

```bash
python scripts/manifest.py --check     # or: sha256sum -c MANIFEST.sha256
python scripts/manifest.py             # regenerate after an intended change, and commit MANIFEST.sha256
```

Covered (tracked files only, via `git ls-files`): `certified/*.py`, `certified/*.out`; everything under
`research/**/checks/` (scripts and outputs, including `research/G1/RH/**/checks/`); `papers/*/checks/**` and
`papers/*/main.pdf`; `data/SHA256SUMS`; `tests/data/**`; `lean/**/*.lean`, `lean/lake-manifest.json`,
`lean/lean-toolchain`. `--check` fails (exit 1, listing the files) if a covered file changed, is missing, is not
listed, or the manifest lists a file that is no longer covered.

**The manifest must be regenerated whenever a check output, a check script, a paper PDF, a Lean file or the test data
changes.** CI (`python.yml`, job `integrity`) runs `--check` on every push and pull request and fails with a message
asking the author to run `python scripts/manifest.py`.

## reproduce.sh

```bash
scripts/reproduce.sh              # all stages, ~5 min
scripts/reproduce.sh --quick      # certified suite + manifest, ~20 s (this is what CI runs)
scripts/reproduce.sh --extended   # all stages + 16 slower numerical checks, ~11 min
```

Python is `$PYTHON`, else `.venv/bin/python`, else `python3` (needs numpy, scipy, mpmath, sympy, python-flint 0.9.0,
pytest). `src/` is put first on `PYTHONPATH`, so the code checked is the code in the working tree. Every script runs
from the repository root. Each stage prints PASS/FAIL/SKIP and the script exits nonzero on any FAIL.

| Stage | What it does |
|---|---|
| build C kernel | `make -C csrc` (gcc + libquadmath) |
| fast pytest suite | `python -m pytest` (excludes `-m slow`; data tests skip without `data/raw/`) |
| certified suite | each `certified/c0*.py`, stdout compared **byte-for-byte** with its `.out` |
| numerical checks | 47 curated scripts from `papers/*/checks` and `research/**/checks`, compared **byte-for-byte** (2 with wall-clock stamps normalized, see below); 6 in parallel (`JOBS`), 2 BLAS threads each |
| Lean | `bash lean/check.sh` (build + axiom audit, must print `AUDIT OK`); SKIP if `lake` is not installed or `lean/.lake/packages` is absent (set `LEAN_FETCH=1` to let lake download the pinned Mathlib) |
| manifest | `python scripts/manifest.py --check` |

Reference run (12-core WSL2 laptop, Python 3.12, OpenBLAS 0.3.30, python-flint 0.9.0), all PASS: full 281 s (pytest 69 s, certified 15 s, numerical checks 174 s, Lean 20 s with a warm build cache, manifest 3 s); `--quick` 21 s; `--extended` 633 s (numerical checks 543 s). The slowest single check is `table2.py` (~1.5–2.5 min under parallel load).

The certified scripts are deterministic (Arb ball arithmetic, exact rational inputs) and reproduce byte-for-byte; the
weekly `pytest -m slow tests/test_certified.py` checks the same thing.

## How the numerical checks were selected

All 91 check scripts that have a same-named `.out` were run from the repository root (6 at a time, 2 BLAS threads,
240 s timeout) and diffed against their committed outputs. The listed 47 reproduced byte-for-byte and take under
~2 min each; the 16 `--extended` ones also reproduced byte-for-byte but take 1.5–4 min each. Normalization is used in
exactly two places: `papers/paper2/checks/table2.py` and `research/G1/checks/check_cb.py` print wall-clock stamps
such as `[31s]`; those are replaced by `[Ns]` on both sides (`sed -E 's/\[[0-9]+s\]/[Ns]/g'`) before the diff, and
every other byte must match.

### Excluded, and why

| Script(s) | Reason |
|---|---|
| `research/G1/checks/check_mn_loc.py`, `check_ra.py`, `check_rw.py`; `research/G3prime/rhfree/checks/check_spectral_sg.py` | **Thread-count-dependent rounding.** They reproduce byte-for-byte with the machine's default BLAS threading here, but with 2 OpenBLAS threads the last printed digits of a few round-off-level quantities change (e.g. `head=2.2e-32` vs `2.8e-32`, `cross-window +6.9e-18` vs `+0.0e+00`, one 4th digit of a finite difference). The reported conclusions do not change, but a byte-for-byte check would depend on the CPU count, so they are left out. |
| `research/G3prime/checks/check_merge.py`, `check_pc_numerics.py`, `check_ratio.py`, `check_zeta_energy.py`; `research/G3prime/rhfree/checks/check_weighted_pc.py` | Need the Odlyzko zeta-zero tables in `data/raw/` (not tracked; fetched by `data/fetch.py`, verified by `data/SHA256SUMS`). |
| `research/G1/RH/zeta/checks/check_z_farfield.py` | The `.out` concatenates two runs (`N=20` and `N=40`; the script takes one `N`), and the `N=20` run alone takes ~1.5 min. Its first half reproduced byte-for-byte. |
| `papers/paper2/checks/check_p55_strip.py`, `research/G1/RH/route2/checks/check_p55_strip.py`, `research/G1/RH/checks/check_phase1.py`, `research/G1/RH/plt1/checks/check_plt1_seam_winding.py`, `research/G1/RH/px/checks/check_px_bessel.py`, `research/G1/RH/route2/checks/check_bnd_coeff.py`, `check_r2alpha_christoffel.py`, `check_r2p1_coeff.py`, `check_r2p_coeff.py`, `check_r2p_lw1.py`, `check_x1_coeff.py`, `research/G1/RH/zeta/checks/check_z_cmp.py`, `check_z_e2e_xi.py`, `check_z_edge2.py`, `check_z_kappa.py`, `research/G1/checks/check_ql_numerics.py`, `check_regularity.py`, `check_sv_general.py` | Too slow: over 4 min each (they did not finish within the 240 s survey timeout). Not tested for reproducibility. |
| Parameterized end-to-end drivers `check_plt1_e2e.py`, `check_plt1_seam_e2e.py`, `check_px_e2e.py`, `check_x1_e2e.py`, `check_z_e2e.py` (outputs `*_p…s….out`, `*_pp2.out`, `*_zeta.out`); `check_z_saddle_curve.py` (no `.out`); `check_px_e2e_p2s2_reference.out` (reference copy) | Long multi-parameter runs with outputs named per parameter set; not re-run. They are still covered by the manifest. |

Every excluded file is still in `MANIFEST.sha256`, so it cannot change unnoticed; it is only not re-executed.
