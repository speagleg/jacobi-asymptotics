# Plan 6: Lean bridge, part 3 (the tridiagonal Toeplitz eigenvalue count, item 11 (S4))

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prove item 11's (S4) for the ℓ×ℓ tridiagonal Toeplitz matrix T_ℓ(A, B), with B ≥ 0. Its eigenvalues are
A + 2B cos(πi/(ℓ+1)), i = 1..ℓ, and therefore

  |N(T; μ) − (ℓ/π)·θ| ≤ 1, θ = arccos(clip((μ−A)/(2B))) (θ = π·1{μ<A} when B = 0).

Here N counts eigenvalues > μ with multiplicity.

**Architecture:**
- **The count.** `eigCount M μ` is the number of roots of `M.charpoly` above μ, counted with multiplicity. For a real
  symmetric matrix this is exactly the spectral count, since all its eigenvalues are real and the characteristic
  polynomial splits. Defining it this way avoids Mathlib's Hermitian-spectral API.
- **Eigenvectors.** The sine vectors v_i(j) = sin(πi(j+1)/(ℓ+1)) are eigenvectors, by sin(a·j) + sin(a(j+2)) =
  2cos a·sin(a(j+1)), and they vanish at both boundaries.
- **All the roots.** For B > 0 the ℓ eigenvalues are distinct (cos is injective on (0, π)), and the characteristic
  polynomial is monic of degree ℓ, so its roots are exactly these, each simple.
- **Counting.** For s = (μ−A)/(2B) ∈ [−1, 1), cos(πi/(ℓ+1)) > s ⇔ i < θ(ℓ+1)/π, so the count is within [−1, 1] of
  ℓθ/π. The cases B = 0, s ≥ 1 and s < −1 are handled directly.

**Tech Stack:** Lean 4.34.1, Mathlib v4.34.1, JacobiAsym on `master` (`bb48797`).

**Spec:** §6 (Toeplitz count, moved to the bridge plans). Math source: item 11 `PROOF.md` §1 (S4) and `check_weyl.out` [4].

**TDD in Lean** works as before. Use `lake env lean F; echo $?`; `check.sh` is the gate. The statements were typechecked
on 2026-10-13.

## Global Constraints

- The same Lean, Mathlib and shared-cache rules as Plans 2–5.
- No `sorry`, `admit` or `axiom`, and only the standard axioms.
- Commit prefix `lean:` with the `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` trailer.
- Branch `plan-6-lean-toeplitz` from `master`.

## Review Focus

1. **`eigCount` is a charpoly-root count.** The docstring must say so, and must say it equals the spectral count for
   symmetric matrices. Do not claim more.
2. **ℓ = 0 and ℓ = 1.** For ℓ = 0 the charpoly is 1 and the count is 0. For ℓ = 1 the eigenvalue is
   A + 2B cos(π/2) = A.
3. **B = 0.** T = A·I, the charpoly is (X − A)^ℓ, and all ℓ roots equal A. The bound holds exactly.
4. **θ at the clip boundaries.** s = ±1 gives θ = 0 or π. Make sure strict versus non-strict inequalities match:
   N counts eigenvalues *strictly* above μ.

---

### Task 1: The matrix, its eigenvectors, and the count definition

**Files:**
- Create: `lean/JacobiAsym/Toeplitz.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces: `toeplitzTri`, `toepEig`, `toepVec`, `toeplitz_eigen`, `toepVec_ne_zero` (1 ≤ i ≤ ℓ), `eigCount`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.Basic

open Finset Matrix Polynomial

namespace JacobiAsym

/-- `ℓ × ℓ` tridiagonal Toeplitz matrix: diagonal `A`, off-diagonals `B`. -/
noncomputable def toeplitzTri (ℓ : ℕ) (A B : ℝ) : Matrix (Fin ℓ) (Fin ℓ) ℝ :=
  Matrix.of fun i j => if i = j then A else if (i : ℕ) + 1 = j ∨ (j : ℕ) + 1 = i then B else 0

/-- `λ_i = A + 2B cos(π i/(ℓ+1))`. -/
noncomputable def toepEig (ℓ : ℕ) (A B : ℝ) (i : ℕ) : ℝ := A + 2 * B * Real.cos (Real.pi * i / (ℓ + 1))

/-- Sine eigenvector `v_i(j) = sin(π i (j+1)/(ℓ+1))`. -/
noncomputable def toepVec (ℓ : ℕ) (i : ℕ) : Fin ℓ → ℝ := fun j => Real.sin (Real.pi * i * ((j : ℝ) + 1) / (ℓ + 1))

theorem toeplitz_eigen (ℓ : ℕ) (A B : ℝ) (i : ℕ) :
    toeplitzTri ℓ A B *ᵥ toepVec ℓ i = toepEig ℓ A B i • toepVec ℓ i := by sorry

theorem toepVec_ne_zero {ℓ i : ℕ} (hi1 : 1 ≤ i) (hiℓ : i ≤ ℓ) : toepVec ℓ i ≠ 0 := by sorry

/-- Number of eigenvalues `> μ` **counted as roots of the characteristic polynomial, with multiplicity**.
For real symmetric matrices (all eigenvalues real) this is the spectral count `N(M; μ)` of item 11 (S3). -/
noncomputable def eigCount {ℓ : ℕ} (M : Matrix (Fin ℓ) (Fin ℓ) ℝ) (μ : ℝ) : ℕ :=
  (M.charpoly.roots.filter (fun t => μ < t)).card

end JacobiAsym
```

Add the import, 2 audit lines, and `toeplitz_eigen` to `need`.

- [ ] **Step 2: Confirm RED**: 2 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  - `toeplitz_eigen`: `funext j`; `mulVec`, `dotProduct`. The sum over k has at most three nonzero terms: k = j, and
    k = j±1 when in range. Rewrite it as `A v_j + B v_{j−1} + B v_{j+1}`, with the convention that out-of-range
    terms are absent.
    - Each boundary is handled by the vanishing of the sine there: sin(a·0) = 0 at j = 0, and sin(a(ℓ+1)) = sin(πi) = 0
      at j = ℓ−1 (`Real.sin_nat_mul_pi`).
    - Then use `Real.sin_add`/`Real.sin_sub` to get sin(a j) + sin(a(j+2)) = 2 cos a sin(a(j+1)), with
      a = πi/(ℓ+1).
    - A clean way to evaluate the sum is `Finset.sum_eq_add_sum_diff_singleton` (or splitting by
      `Fin` cases), or via an extended function `u : ℤ → ℝ := sin(a(m+1))`.
  - `toepVec_ne_zero`: the entry at j = 0 is sin(πi/(ℓ+1)) > 0, because 0 < πi/(ℓ+1) < π (`Real.sin_pos_of_pos_of_lt_pi`).
    This needs ℓ ≥ 1, which follows from 1 ≤ i ≤ ℓ.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: tridiagonal Toeplitz matrix, sine eigenvectors, charpoly-root eigenvalue count`.

---

### Task 2: The eigenvalues are exactly the charpoly roots (B > 0); the B = 0 case

**Files:**
- Modify: `lean/JacobiAsym/Toeplitz.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces: `toeplitz_charpoly_roots`, `toeplitz_eigCount`, `toeplitz_eigCount_zero` (B = 0).

- [ ] **Step 1: Append the statements with `sorry`**

```lean
theorem toeplitz_charpoly_roots (ℓ : ℕ) (A B : ℝ) (hB : 0 < B) :
    (toeplitzTri ℓ A B).charpoly.roots = ((Icc 1 ℓ).image (toepEig ℓ A B)).val := by sorry

theorem toeplitz_eigCount (ℓ : ℕ) (A B μ : ℝ) (hB : 0 < B) :
    eigCount (toeplitzTri ℓ A B) μ = ((Icc 1 ℓ).filter (fun i => μ < toepEig ℓ A B i)).card := by sorry

theorem toeplitz_eigCount_zero (ℓ : ℕ) (A μ : ℝ) :
    eigCount (toeplitzTri ℓ A 0) μ = if μ < A then ℓ else 0 := by sorry
```

Add 3 audit lines, and `toeplitz_eigCount` to `need`.

- [ ] **Step 2: Confirm RED.**
- [ ] **Step 3: Prove**
  - **Each λ_i is a root, 1 ≤ i ≤ ℓ.** We have T v = λ v with v ≠ 0, so det(λI − T) = 0, so `IsRoot charpoly λ`.
    Use `Matrix.eval_charpoly`, or `charpoly` evaluated at λ equal to `det (scalar λ - T)`, together with
    `Matrix.exists_mulVec_eq_zero_iff`: `(∃ v ≠ 0, M *ᵥ v = 0) ↔ M.det = 0`.
  - **Injectivity.** i ↦ λ_i is injective on `Icc 1 ℓ`, because cos is strictly decreasing on [0, π]
    (`Real.strictAntiOn_cos`) and B > 0. So the image has card ℓ.
  - **Roots.** charpoly is monic of `natDegree ℓ` (`Matrix.charpoly_monic`, `Matrix.charpoly_natDegree_eq_dim`), so
    `card roots ≤ ℓ` (`Polynomial.card_roots'`). A finset of ℓ distinct roots is contained in `roots.toFinset`, so
    `roots = image.val`. Use `Multiset.eq_of_le_of_card_le` with `Multiset.le_iff_subset` (nodup image).
  - **`toeplitz_eigCount`.** Rewrite with the roots, then `Multiset.filter` on `Finset.val` and `Finset.card_image_of_injOn`
    restricted to the filter.
  - **`toeplitz_eigCount_zero`.** `toeplitzTri ℓ A 0 = scalar ℓ A`, so `charpoly = (X − C A)^ℓ`
    (`Matrix.charpoly_scalar`-style, or `charpoly_diagonal`). Its roots are `Multiset.replicate ℓ A`
    (`roots_X_sub_C_pow` / `roots_pow`). Then `Multiset.filter` on `replicate`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: Toeplitz charpoly roots are exactly A + 2B cos(πi/(ℓ+1)); B = 0 case`.

---

### Task 3: The count bound (S4)

**Files:**
- Modify: `lean/JacobiAsym/Toeplitz.lean`, `lean/Audit.lean`, `lean/check.sh`, `lean/README.md`, `README.md`, spec §6
  note

**Interfaces:**
- Produces: `weylAngle`, `cos_count` (the counting lemma), `toeplitz_count`.

- [ ] **Step 1: Append the statements with `sorry`**

```lean
/-- Weyl angle `θ = arccos(clip((μ - A)/(2B)))`, with `θ = π·1{μ < A}` when `B = 0`. -/
noncomputable def weylAngle (A B μ : ℝ) : ℝ :=
  if B = 0 then (if μ < A then Real.pi else 0) else Real.arccos (max (-1) (min 1 ((μ - A) / (2 * B))))

/-- Counting lemma: `#{i ∈ [1, ℓ] : s < cos(π i/(ℓ+1))}` is within 1 of `ℓ · arccos(clip s)/π`. -/
theorem cos_count (ℓ : ℕ) (s : ℝ) :
    |(((Icc 1 ℓ).filter (fun i : ℕ => s < Real.cos (Real.pi * i / (ℓ + 1)))).card : ℝ) -
      ℓ / Real.pi * Real.arccos (max (-1) (min 1 s))| ≤ 1 := by sorry

/-- **Item 11 (S4)**: `|N(T_ℓ(A,B); μ) - (ℓ/π) θ| ≤ 1`. -/
theorem toeplitz_count (ℓ : ℕ) (A B μ : ℝ) (hB : 0 ≤ B) :
    |(eigCount (toeplitzTri ℓ A B) μ : ℝ) - ℓ / Real.pi * weylAngle A B μ| ≤ 1 := by sorry
```

Add 2 audit lines, and `toeplitz_count` to `need`.

- [ ] **Step 2: Confirm RED.**
- [ ] **Step 3: Prove**
  - `cos_count`: put c := clip s and θ := arccos c ∈ [0, π].
    - **Case s ≥ 1.** cos ≤ 1 ≤ s everywhere, so the count is 0; θ = arccos 1 = 0.
    - **Case s < −1.** cos(πi/(ℓ+1)) > −1 > s, because the angle is strictly inside (0, π). So the count is ℓ;
      θ = π, giving ℓ − ℓ = 0.
    - **Case −1 ≤ s < 1.** c = s. For i ∈ [1, ℓ], s < cos(πi/(ℓ+1)) ⇔ πi/(ℓ+1) < arccos s (`Real.arccos_lt_iff`-style
      via `Real.strictAntiOn_cos` on [0, π]). So the filter is `{i ∈ [1, ℓ] : i < θ(ℓ+1)/π}`, whose card K satisfies
      θ(ℓ+1)/π − 1 ≤ K ≤ θ(ℓ+1)/π (also K ≤ ℓ). Hence K − ℓθ/π ∈ [θ/π − 1, θ/π] ⊆ [−1, 1].
    - For the card of an initial segment `{i ∈ [1, ℓ] : i < y}`, use `Nat.card_Icc`/`Finset.filter_lt` reasoning
      with y real: it is `min ℓ (⌈y⌉₊ − 1)`.
  - `toeplitz_count`:
    - **B = 0:** `toeplitz_eigCount_zero`, then case on μ < A: |ℓ − ℓ| = 0 or |0 − 0| = 0.
    - **B > 0:** `toeplitz_eigCount`. Then
      μ < A + 2B cos(...) ⇔ (μ−A)/(2B) < cos(...) (`div_lt_iff₀`), so the filter matches `cos_count` with
      s = (μ−A)/(2B). Unfold `weylAngle` with `if_neg hB.ne'`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Docs.**
  - `lean/README.md`: add the row `toeplitzTri, toeplitz_eigen, eigCount, toeplitz_count | (S4) | Toeplitz count`,
    and update "Not here" to: "the true-zero measure (G3′) is research; the forward Weyl law (Theorem B) itself is not
    formalized."
  - `README.md`: say the Lean bridge plans are complete.
  - Spec §6 note: "Plan 6 done".
- [ ] **Step 6: Commit** `lean: Toeplitz eigenvalue count (S4): |N(T; μ) − (ℓ/π)θ| ≤ 1`.
