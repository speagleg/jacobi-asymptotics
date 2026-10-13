# Plan 5: Lean bridge, part 2 (orthogonal polynomials, three-term recurrence, H2, the b_j law)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Define the monic orthogonal polynomials of a discrete measure Σ w_k δ_{x_k}. Then prove:
- the three-term recurrence X P_k = P_{k+1} + a_k P_k + b_k² P_{k−1}, with b_k² = D_{k+1}D_{k−1}/D_k²;
- H2: D_n = m₀ⁿ Π_{j=1}^{n−1} (b_j²)^{n−j}.

From these, derive **the b_j form of Corollary H_L-ζ**:

  (2/n²) Σ_{j=1}^{n−1} (n−j) log(b_j/x_j) → log(π²/16)

This holds for the smooth ζ measure, still mod the named input Theorem H.

**Architecture:**
- **No orthogonal-polynomial library.** Mathlib has none. P_k is defined by the classical determinant formula: rows of
  moments, and a last row 1, X, …, X^k over ℝ[X], divided by D_k.
- **Orthogonality** comes from Laplace expansion along the last row (`Matrix.det_succ_row`) and linearity of the
  discrete inner product. Pairing with X^j for j < k gives a determinant with two equal rows.
- **Recurrence.** The remainder R := X P_k − P_{k+1} − a_k P_k − b_k² P_{k−1} has degree ≤ k and is orthogonal to
  1, …, X^k. So ⟨R, R⟩ = 0, R vanishes at all (infinitely many, distinct) atoms, and R = 0
  (`Polynomial.eq_zero_of_infinite_isRoot`).
- **H2** is telescoping algebra with D_j > 0.
- **The b_j law** combines three things:
  - H2;
  - the "Σ log L(j)" form of Theorem H_L, obtained from `smoothZeta_HL` via `weighted_cesaro_slow`;
  - a superfactorial asymptotic Σ_{j<n}(n−j) log j = (n²/2) log n − (3/4) n² + o(n²), proved by two sum/integral
    comparisons (`MonotoneOn.sum_le_integral_Ico` and friends).

**Tech Stack:** Lean 4.34.1, Mathlib v4.34.1, and the JacobiAsym library on `master` (`e13216e`).

**Spec:** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` §6 (H2 was in the original list). Math
source: item 11 `PROOF.md` §1 (S2, conventions), §7 (H2), §7b (equivalent b_j form of Theorem H_L).

**Conventions:** atoms k ↔ item-11 atom k+1. `jb2 x w k` is b_k² for k ≥ 1; `ja x w k` is a_k. `P_k = opoly x w k`
is monic of degree k. The b_j law uses x_j = `zetaAtom (j − 1)`, the j-th atom in 1-based indexing, for
j ∈ `Ico 1 n`. This matches the toolkit's `averaged_law`: `b[j−1]`/`x[j−1]` 0-based is b_j/x_j 1-based.

**TDD in Lean** works as before. RED is the statement with `sorry` plus `check.sh` failing. GREEN is `check.sh`
printing `AUDIT OK`. Single-file checks are `lake env lean F; echo $?`. All statements were typechecked on
2026-10-13.

## Global Constraints

- Lean 4.34.1 and Mathlib v4.34.1. Never run `lake update`.
- No `sorry`, `admit` or `axiom`. Axioms are limited to the standard three.
- Update the audit and `need` list per task.
- Commit prefix `lean:`. Each commit ends with the `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` trailer.
- Branch `plan-5-lean-orthopoly` from `master`.

## Review Focus

1. **The determinant formula's last row.** Row index `k` must be the X-row, built with `if (i : ℕ) < k then … else …`
   over `Fin (k+1)`. Check k = 0, where P_0 = 1 and D_0 = det of the empty matrix = 1.
2. **The k = 1 edge of the recurrence.** P_{k−1} = P_0 = 1 and b_1² = D_2 D_0/D_1² = D_2/m₀². Check it numerically
   against the toolkit (`jacobi_mp` on a small measure) in the Task 4 example.
3. **Dependence on positive definiteness.** `DMeasure` must give D_n > 0 for every n. That needs infinitely many
   distinct atoms with w > 0. Strict antitonicity of x gives distinctness.
4. **Index alignment of the b_j law with the toolkit.** It uses `Ico 1 n`, b_j, and x_j = `zetaAtom (j−1)`. A Python
   cross-check in Task 6 compares the Lean statement's finite-n quantity with `averaged_law` on the same measure, to
   the extent floats allow.
5. **The superfactorial asymptotic constant −3/4.** Derive it exactly, not numerically; a wrong constant would shift
   the limit.

---

### Task 1: Discrete inner product, moments, and positivity of D_n

**Files:**
- Create: `lean/JacobiAsym/DiscreteMeasure.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces:
  - `DMeasure x w`, a structure with `w_pos`, `w_sum`, `x_bdd`, `x_anti`.
  - `dip x w p q`, `mom x w r`.
  - Lemmas:
    - `dip_summable`;
    - `dip_add_left`, `dip_smul_left`, `dip_sum_left` (linearity in the first argument; with `dip_comm`, also in the
      second);
    - `dip_comm`, `dip_X_mul` (⟨X·p, q⟩ = ⟨p, X·q⟩);
    - `dip_pow_pow` (⟨X^i, X^j⟩ = m_{i+j});
    - `dip_self_eq_zero` (⟨p, p⟩ = 0 → p = 0);
    - `hankel_eq_mom` (entries);
    - `hankel_det_pos` (D_n > 0).

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.HankelLimit

open Finset Filter Topology Matrix Polynomial

namespace JacobiAsym

/-- Standing hypotheses for a discrete measure `∑ w k δ_{x k}`. -/
structure DMeasure (x w : ℕ → ℝ) : Prop where
  w_pos : ∀ k, 0 < w k
  w_sum : Summable w
  x_bdd : ∃ X, ∀ k, |x k| ≤ X
  x_anti : StrictAnti x

/-- Discrete inner product `⟨p, q⟩ = ∑' k, w k p(x k) q(x k)`. -/
noncomputable def dip (x w : ℕ → ℝ) (p q : ℝ[X]) : ℝ := ∑' k, w k * p.eval (x k) * q.eval (x k)

/-- Moment `m_r = ∑' w x^r`. -/
noncomputable def mom (x w : ℕ → ℝ) (r : ℕ) : ℝ := ∑' k, w k * x k ^ r

theorem dip_summable {x w : ℕ → ℝ} (h : DMeasure x w) (p q : ℝ[X]) :
    Summable (fun k => w k * p.eval (x k) * q.eval (x k)) := by sorry

theorem dip_comm (x w : ℕ → ℝ) (p q : ℝ[X]) : dip x w p q = dip x w q p := by sorry

theorem dip_add_left {x w : ℕ → ℝ} (h : DMeasure x w) (p p' q : ℝ[X]) :
    dip x w (p + p') q = dip x w p q + dip x w p' q := by sorry

theorem dip_smul_left (x w : ℕ → ℝ) (c : ℝ) (p q : ℝ[X]) : dip x w (C c * p) q = c * dip x w p q := by sorry

theorem dip_sum_left {x w : ℕ → ℝ} (h : DMeasure x w) {ι : Type*} (s : Finset ι) (f : ι → ℝ[X]) (q : ℝ[X]) :
    dip x w (∑ i ∈ s, f i) q = ∑ i ∈ s, dip x w (f i) q := by sorry

theorem dip_X_mul (x w : ℕ → ℝ) (p q : ℝ[X]) : dip x w (X * p) q = dip x w p (X * q) := by sorry

theorem dip_pow_pow (x w : ℕ → ℝ) (i j : ℕ) : dip x w (X ^ i) (X ^ j) = mom x w (i + j) := by sorry

theorem dip_self_eq_zero {x w : ℕ → ℝ} (h : DMeasure x w) {p : ℝ[X]} (hp : dip x w p p = 0) : p = 0 := by sorry

theorem hankel_eq_mom (x w : ℕ → ℝ) (n : ℕ) (i j : Fin n) : hankel x w n i j = mom x w ((i : ℕ) + j) := by sorry

theorem hankel_det_pos {x w : ℕ → ℝ} (h : DMeasure x w) (n : ℕ) : 0 < (hankel x w n).det := by sorry

end JacobiAsym
```

Add the import, 10 audit lines, and `dip_self_eq_zero hankel_det_pos` to `need`.

- [ ] **Step 2: Confirm RED**: 10 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  - `dip_summable`: `|p.eval (x k)| ≤ Bp`, because a polynomial is bounded on the compact `Icc (−X) X`
    (`p.continuous.continuousOn`, `IsCompact.exists_bound_of_continuousOn`). So the term is ≤ Bp·Bq·w k
    (`Summable.of_norm_bounded`).
  - `dip_comm`: `mul_right_comm` inside the tsum (`tsum_congr`).
  - `dip_add_left`: `eval_add`, `add_mul`, then `tsum_add` with the two summabilities.
  - `dip_smul_left`: `eval_mul`, `eval_C`, then `tsum_mul_left`.
  - `dip_sum_left`: induction on `s` with `dip_add_left` (`Finset.induction_on`). Base case: the tsum of 0.
  - `dip_X_mul`: `eval_mul`, `eval_X`, `ring_nf` inside `tsum_congr`.
  - `dip_pow_pow`: `eval_pow`, `eval_X`, `pow_add`.
  - `hankel_eq_mom`: `rfl` / `simp [hankel, mom]`.
  - `dip_self_eq_zero`:
    1. ⟨p, p⟩ = Σ' w_k p(x_k)², a sum of nonnegative terms.
    2. Its being 0 forces every term to be 0 (`hasSum_zero_iff_of_nonneg` / `tsum_eq_zero_iff`), so
       p(x_k) = 0 for all k (`w_pos`).
    3. Since x is injective (`x_anti.injective`), {x_k} is infinite, so `p = 0` by `eq_zero_of_infinite_isRoot`
       (`Set.infinite_range_of_injective`).
  - `hankel_det_pos`: `heineD_eq_det` (with X from `x_bdd`) plus `heineD_pos` (`x_anti`, `w_pos`,
    `heineK_bdd_of_summable`).
- [ ] **Step 4: Confirm GREEN**: `lean/check.sh` prints `AUDIT OK`.
- [ ] **Step 5: Commit** `lean: discrete inner product, moments, positive definiteness, D_n > 0`.

---

### Task 2: Monic orthogonal polynomials via the determinant formula

**Files:**
- Create: `lean/JacobiAsym/OrthoPoly.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: Task 1.
- Produces:
  - `opolyMat` and `opoly`.
  - `opoly_eq_sum`: the Laplace expansion along the last row,
    `opoly = C(D_k⁻¹) * Σ_j (−1)^{k+j} cof_j X^j`.
  - `dip_opoly_pow` (j < k gives 0), `dip_opoly_pow_self` (⟨P_k, X^k⟩ = D_{k+1}/D_k).
  - `opoly_monic`, `opoly_natDegree`, `opoly_zero` (P_0 = 1).

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.DiscreteMeasure

open Finset Matrix Polynomial

namespace JacobiAsym

/-- The `(k+1) × (k+1)` matrix: rows `i < k` are moments `m_{i+j}`, the last row is `1, X, …, X^k`. -/
noncomputable def opolyMat (x w : ℕ → ℝ) (k : ℕ) : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ[X] :=
  Matrix.of fun i j => if (i : ℕ) < k then C (mom x w ((i : ℕ) + j)) else (X : ℝ[X]) ^ (j : ℕ)

/-- Monic orthogonal polynomial of degree `k`. -/
noncomputable def opoly (x w : ℕ → ℝ) (k : ℕ) : ℝ[X] := C ((hankel x w k).det)⁻¹ * (opolyMat x w k).det

theorem opoly_zero (x w : ℕ → ℝ) : opoly x w 0 = 1 := by sorry

theorem dip_opoly_pow {x w : ℕ → ℝ} (h : DMeasure x w) {k j : ℕ} (hj : j < k) :
    dip x w (opoly x w k) (X ^ j) = 0 := by sorry

theorem dip_opoly_pow_self {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) :
    dip x w (opoly x w k) (X ^ k) = (hankel x w (k + 1)).det / (hankel x w k).det := by sorry

theorem opoly_monic {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : (opoly x w k).Monic := by sorry

theorem opoly_natDegree {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : (opoly x w k).natDegree = k := by sorry

end JacobiAsym
```

Add the import, 5 audit lines, and `dip_opoly_pow dip_opoly_pow_self opoly_monic` to `need`.

- [ ] **Step 2: Confirm RED**: 5 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  1. **Key lemma (`dip_det_lastRow`).** For any polynomial q,
     `dip x w (opolyMat x w k).det q = (Matrix.of fun i j => if i < k then mom (i+j) else dip x w (X^j) q).det`.
     Expand both determinants along the last row with `det_succ_row … (Fin.last k)`. The cofactor submatrices are
     identical constant matrices, mapped by `Polynomial.C` (`RingHom.map_det`). The resulting
     `Σ_j c_j * X^j` is integrated with `dip_sum_left`/`dip_smul_left`.
  2. **Orthogonality, j < k.** The last row becomes `mom (j' + j)`, the same as row j, so the determinant is 0
     (`det_zero_of_row_eq`).
  3. **Self-pairing, j = k.** The last row becomes `mom (j' + k)`, which is exactly `hankel x w (k+1)`. Use
     `hankel_eq_mom` and `ext` over `Fin (k+1)`, with `Fin.lastCases`.
  4. **Leading coefficient.** In the expansion, the coefficient of X^k is the cofactor at (k, k), which is
     `hankel x w k` (`submatrix (Fin.last k).succAbove (Fin.last k).succAbove` = top-left block). So
     `opoly = X^k + (lower terms)`. Prove `natDegree ≤ k` and `coeff k = 1` via `Polynomial.monic_of_natDegree_le_of_coeff_eq_one`.
     This needs D_k ≠ 0 (`hankel_det_pos`).
  5. **`opoly_zero`.** `Fin 1`: the single entry is `X^0 = 1`, and `hankel x w 0` is the empty matrix with det 1.
     Use `det_unique`/`det_fin_one`, `det_isEmpty`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: monic orthogonal polynomials via the determinant formula; orthogonality and norms`.

---

### Task 3: The three-term recurrence

**Files:**
- Create: `lean/JacobiAsym/Recurrence.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: Tasks 1–2.
- Produces: `jb2`, `ja`, `opoly_recurrence`, `jb2_pos`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.OrthoPoly

open Finset Matrix Polynomial

namespace JacobiAsym

/-- `b_k² = D_{k+1} D_{k-1} / D_k²` (`k ≥ 1`). -/
noncomputable def jb2 (x w : ℕ → ℝ) (k : ℕ) : ℝ :=
  (hankel x w (k + 1)).det * (hankel x w (k - 1)).det / (hankel x w k).det ^ 2

/-- `a_k = ⟨X P_k, P_k⟩ / ⟨P_k, P_k⟩`. -/
noncomputable def ja (x w : ℕ → ℝ) (k : ℕ) : ℝ :=
  dip x w (X * opoly x w k) (opoly x w k) / dip x w (opoly x w k) (opoly x w k)

theorem jb2_pos {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : 0 < jb2 x w k := by sorry

/-- **Three-term recurrence** (item 11 §1 convention: monic `P_k`, `b_k²` the squared off-diagonal). -/
theorem opoly_recurrence {x w : ℕ → ℝ} (h : DMeasure x w) {k : ℕ} (hk : 1 ≤ k) :
    X * opoly x w k = opoly x w (k + 1) + C (ja x w k) * opoly x w k + C (jb2 x w k) * opoly x w (k - 1) := by
  sorry

end JacobiAsym
```

Add the import, 2 audit lines, and `opoly_recurrence` to `need`.

- [ ] **Step 2: Confirm RED**: 2 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  - **Pairings with polynomials of lower degree.** First prove `dip_opoly_lowdeg`: for deg q < k,
    ⟨P_k, q⟩ = 0. Expand q in monomials (`Polynomial.as_sum_range`), then use `dip_sum_left` and `dip_comm` with
    `dip_opoly_pow`. Also ⟨P_k, P_k⟩ = ⟨P_k, X^k⟩ = D_{k+1}/D_k, because P_k − X^k has degree < k (monic).
  - **R has degree ≤ k.** Set R := X·P_k − P_{k+1} − a_k P_k − b_k² P_{k−1}. X·P_k and P_{k+1} are both monic of
    degree k+1, so their difference has degree ≤ k (`Monic.natDegree_sub` or `degree_sub_lt`).
  - **R ⊥ X^j for j ≤ k**, by cases:
    - j ≤ k−2: every term vanishes (`dip_X_mul` moves X across; deg X^{j+1} < k).
    - j = k−1: ⟨XP_k, X^{k−1}⟩ = ⟨P_k, X^k⟩ = D_{k+1}/D_k and b_k²⟨P_{k−1}, X^{k−1}⟩ = b_k²·D_k/D_{k−1}. These are
      equal by the definition of `jb2`; field_simp with D's ≠ 0.
    - j = k: this is the definition of a_k. ⟨XP_k, X^k⟩ − a_k⟨P_k, X^k⟩ − b_k²⟨P_{k−1}, X^k⟩ = 0, using
      ⟨P_k, X^k⟩ = ⟨P_k, P_k⟩ and ⟨XP_k, P_k⟩ = ⟨XP_k, X^k⟩ + ⟨XP_k, P_k − X^k⟩. Write a_k with `dip`s; it is
      easiest to show R ⊥ P_k and R ⊥ P_{k−1} directly, together with R ⊥ X^j for j ≤ k−2.
  - **Conclusion.** R ⊥ every polynomial of degree ≤ k, R included, so ⟨R, R⟩ = 0 and R = 0
    (`dip_self_eq_zero`). Rearrange.
  - `jb2_pos`: `hankel_det_pos` three times; `div_pos`, `mul_pos`, `pow_pos`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: three-term recurrence X P_k = P_{k+1} + a_k P_k + b_k² P_{k-1}, b_k² = D_{k+1}D_{k-1}/D_k²`.

---

### Task 4: H2 and a toolkit cross-check

**Files:**
- Create: `lean/JacobiAsym/H2.lean`, `tests/test_lean_H2_crosscheck.py`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces:
  - `hankel_det_eq_prod`, i.e. H2: `D_n = m₀ⁿ ∏_{j ∈ Ico 1 n} (b_j²)^(n−j)`.
  - A Python test confirming that the toolkit's `b2` equals D_{j+1}D_{j−1}/D_j² from exact Hankel determinants on a
    small measure, which pins the Lean `jb2` convention to the toolkit's.

- [ ] **Step 1: Write the Lean statement and the Python test (RED)**

```lean
import JacobiAsym.Recurrence

open Finset Matrix

namespace JacobiAsym

/-- **H2** (item 11 Lemma H2): `D_n = m₀ⁿ ∏_{j=1}^{n-1} (b_j²)^{n-j}`. -/
theorem hankel_det_eq_prod {x w : ℕ → ℝ} (h : DMeasure x w) (n : ℕ) :
    (hankel x w n).det = mom x w 0 ^ n * ∏ j ∈ Ico 1 n, jb2 x w j ^ (n - j) := by sorry

end JacobiAsym
```

`tests/test_lean_H2_crosscheck.py`:
```python
"""Pins the Lean definition jb2 k = D_{k+1} D_{k-1} / D_k^2 to the toolkit's b2 convention."""
import mpmath as mp
import numpy as np
from jacobi_asym.measures import DiscreteMeasure
from jacobi_asym.jacobi import jacobi_mp
from jacobi_asym.hankel import hankel_det_mp


def test_b2_equals_hankel_ratio():
    rng = np.random.default_rng(4)
    mu = DiscreteMeasure.from_atoms(rng.uniform(0.05, 1.0, 12), rng.uniform(0.2, 1.5, 12))
    a, b2 = jacobi_mp(mu, 6, dps=60)
    with mp.workdps(60):
        D = [mp.mpf(1)] + [hankel_det_mp(mu, n, dps=60) for n in range(1, 8)]
        for k in range(1, 6):
            assert abs(b2[k - 1] / (D[k + 1] * D[k - 1] / D[k] ** 2) - 1) < mp.mpf(10) ** -40
```

Run the Python test. Expected: **PASS** immediately, since the toolkit already exists; it is a characterization test
that pins the convention. Record that in the ledger. For the Lean statement, `lake env lean JacobiAsym/H2.lean` shows
1 `sorry`.

- [ ] **Step 2: Prove H2.** Use induction on n with `prod_Ico_succ_top` and `pow_succ`. Put h_j := D_{j+1}/D_j. Then
  - D_n = Π_{j<n} h_j (telescoping, using D_0 = 1);
  - h_0 = m₀;
  - h_j = h_{j−1}·b_j² by the definition of `jb2`.

  So h_j = m₀ Π_{i=1}^{j} b_i², and D_n = Π_{j<n} m₀ Π_{i≤j} b_i² = m₀ⁿ Π_i (b_i²)^{n−i}. Rearrange the double
  product with `prod_comm`-style counting, or by direct induction on n: D_{n+1} = D_n·h_n, and
  `∏_{Ico 1 (n+1)} b^(n+1−j) = (∏_{Ico 1 n} b^(n−j)) · ∏_{Ico 1 (n+1)} b`.
- [ ] **Step 3: Confirm GREEN** with `lean/check.sh` and `.venv/bin/python -m pytest -q`.
- [ ] **Step 4: Commit** `lean: H2 (Hankel determinant = m0^n prod b_j^{2(n-j)}); toolkit convention cross-check`.

---

### Task 5: The superfactorial asymptotic

**Files:**
- Create: `lean/JacobiAsym/SuperFactorial.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces: `sum_log_weighted_asymp`:
  `(Σ_{j ∈ Ico 1 n} (n−j) log j − (n²/2 · log n − 3n²/4)) / n² → 0`.

- [ ] **Step 1: Write the statement with `sorry`**

```lean
import JacobiAsym.SlowVariation

open Finset Filter Topology

namespace JacobiAsym

/-- `∑_{j=1}^{n-1} (n-j) log j = (n²/2) log n - (3/4) n² + o(n²)`. -/
theorem sum_log_weighted_asymp :
    Tendsto (fun n : ℕ => (∑ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log j -
      ((n : ℝ) ^ 2 / 2 * Real.log n - 3 / 4 * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  sorry

end JacobiAsym
```

Add the import, an audit line, and `sum_log_weighted_asymp` to `need`.

- [ ] **Step 2: Confirm RED**: 1 `sorry` warning, exit 0.
- [ ] **Step 3: Prove**
  1. **Rewrite.** Σ_{j<n}(n−j) log j = Σ_{j ∈ Ico 1 n} ∫_j^n log j dt, or more simply Σ_{m ∈ Ico 1 n} log(m!).
     Prove the second by induction on n (`Finset.sum_Ico_succ_top`).
  2. **Bounds on log m! (m ≥ 1):**
     - Lower: m log m − m + 1 ≤ log m!. Integral comparison of the increasing function log on [1, m]:
       ∫_1^m log = m log m − m + 1 ≤ Σ_{j=2}^{m} log j (`MonotoneOn.integral_le_sum_Ico`).
     - Upper: log m! ≤ (m+1) log(m+1) − m. From Σ_{j=2}^{m} log j ≤ ∫_2^{m+1} log ≤ ∫_1^{m+1} log
       (`MonotoneOn.sum_le_integral_Ico`). Use `integral_log` (Mathlib: ∫ log = x log x − x).
  3. **Bounds on Σ_{m<n} m log m.** Sum/integral comparison for t log t (increasing on [1, ∞)) with ∫ t log t =
     t²/2·log t − t²/4. Upper and lower bounds both differ from n²/2·log n − n²/4 by O(n log n).
  4. **Assemble.** Σ log m! = Σ (m log m − m) + O(n log n) = n²/2 log n − n²/4 − n²/2 + O(n log n). The O(n log n)
     remainder over n² → 0 by `tendsto_log_div_nat`; finish with the squeeze lemma.

  The constant −3/4 = −1/4 − 1/2 is exact (Review Focus #5).
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: superfactorial asymptotic sum (n-j) log j = n²/2 log n - 3n²/4 + o(n²)`.

---

### Task 6: The b_j form of Corollary H_L-ζ

**Files:**
- Create: `lean/JacobiAsym/BLaw.lean`, `tests/test_lean_blaw_index.py`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`, `lean/README.md`, `README.md`, spec §6 note

**Interfaces:**
- Consumes: `smoothZeta_HL_det` (Plan 4), `hankel_det_eq_prod` (Task 4), `sum_log_weighted_asymp` (Task 5),
  `weighted_cesaro_slow` (Plan 2), `zetaL_slowFactor`'s `logL_slow`.
- Produces:
  - `zeta_DMeasure`.
  - `smoothZeta_HL_sumForm`: log D_n = −2n² log n + 2Σ_{j<n}(n−j) log L(j) + κn² + o(n²).
  - `smoothZeta_bLaw`.

- [ ] **Step 1: Write the statements with `sorry`, plus a Python index test**

```lean
import JacobiAsym.SmoothZetaHL
import JacobiAsym.H2
import JacobiAsym.SuperFactorial

open Finset Filter Topology

namespace JacobiAsym

theorem zeta_DMeasure : DMeasure zetaAtom (fun k => 2 * zetaAtom k) := by sorry

/-- **b_j form of Corollary H_L-ζ** (PROVED-mod-input): the doubly-Cesàro geometric mean of `b_j / x_j`
tends to `π²/16`; `x_j = zetaAtom (j-1)` is the `j`-th atom. -/
theorem smoothZeta_bLaw (hH : TheoremHPure 2 (3 + Real.log (Real.pi ^ 2 / 16)) 2) :
    Tendsto (fun n : ℕ => 2 / (n : ℝ) ^ 2 *
      ∑ j ∈ Ico 1 n, ((n : ℝ) - j) *
        Real.log (Real.sqrt (jb2 zetaAtom (fun k => 2 * zetaAtom k) j) / zetaAtom (j - 1)))
      atTop (𝓝 (Real.log (Real.pi ^ 2 / 16))) := by
  sorry

end JacobiAsym
```

`tests/test_lean_blaw_index.py` is a characterization test of the index alignment. The Lean finite-n quantity, with
b_j from Hankel ratios and x_j the j-th atom, must equal the toolkit's `averaged_law` plus log c(2) on the same
finite measure:
```python
import mpmath as mp
import numpy as np
from jacobi_asym.measures import pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import averaged_law, c_p


def test_lean_blaw_quantity_matches_toolkit_averaged_law():
    mu = pure_power(2, 3000)
    r = jacobi_coeffs(mu, 40)
    n = 40
    lean_q = 2 / n ** 2 * sum((n - j) * np.log(np.sqrt(r.b2[j - 1]) / mu.atoms[j - 1]) for j in range(1, n))
    assert abs(lean_q - (averaged_law(r.b, mu.atoms, 2, [n])[n] + np.log(c_p(2)))) < 1e-12
```

- [ ] **Step 2: Confirm RED**: 2 `sorry`s; the Python test passes (characterization).
- [ ] **Step 3: Prove**
  - `zeta_DMeasure`:
    - `w_pos` from `zetaAtom_pos`;
    - `w_sum` from `zetaAtom_summable.mul_left 2`;
    - `x_bdd` with X = 1 (`zetaAtom_le_one`);
    - `x_anti`: γ is strictly increasing (`zetaGamma_strictMonoOn`), so 1/(γ²+¼) is strictly decreasing.
  - `smoothZeta_HL_sumForm` (helper): from `smoothZeta_HL_det` and `weighted_cesaro_slow` applied to ℓ = log ∘ zetaL
    (with `logL_slow`), (2Σ_{j ∈ Ico 1 n}(n−j)(log L j − log L n))/n² → 0. Also 2Σ_{Ico 1 n}(n−j) = n(n−1).
  - `smoothZeta_bLaw`:
    1. By H2, log D_n = n log m₀ + Σ_{Ico 1 n} (n−j) log b_j², with b_j² > 0 (`jb2_pos`), and
       log b_j² = 2 log √(b_j²).
    2. By definition, log L(j) = 2 log j + log x_j, since L(j) = j²/(γ(j)²+¼) = j²·zetaAtom(j−1).
    3. Combine with the sum form, and use `sum_log_weighted_asymp`.

    The result is 2Σ(n−j) log(b_j/x_j) = (κ − 3)n² + o(n²), and κ − 3 = log(π²/16). The terms n log m₀/n² → 0.
    This is pure `Tendsto` arithmetic: `Tendsto.add`, `Tendsto.congr'`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh` and pytest.
- [ ] **Step 5: Docs.** Add `lean/README.md` rows for Tasks 1–6.
  - The headline row: **`smoothZeta_bLaw`**, the b_j form, PROVED-mod-input.
  - Update the "Not here" note: only the Toeplitz count (Plan 6) and G3′ remain.
  - Top-level `README.md` status: add "and its b_j form (2/n²)Σ(n−j)log(b_j/x_j) → log(π²/16)".
  - Spec §6 note: "Plan 5 done".
- [ ] **Step 6: Commit** `lean: b_j form of Corollary H_L-ζ via orthogonal polynomials, H2 and the superfactorial sum`.
