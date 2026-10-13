# Plan 4: Lean bridge, part 1 (smooth-ζ instance, Cauchy–Binet/Andreief, K → ∞)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** This plan has three parts:
1. Prove Cauchy–Binet. Then prove that the truncated Heine sum `heineK` equals the Hankel determinant of the
   truncated measure (Andreief/Heine).
2. Prove that `heineD`, the sup over K, equals the Hankel determinant of the infinite measure's moments.
3. Instantiate `SlowFactor` for the smooth ζ model. This makes `theoremHL` yield **Corollary H_L-ζ** for the actual
   smooth-ζ measure. The result is still mod the named input `TheoremHPure 2 κ 2`.

**Architecture:**
- **Part B (Cauchy–Binet).** Cauchy–Binet is proved for `A : Fin n × Fin K` and `B : Fin K × Fin n` over ℝ by the
  standard multilinear expansion, in the style of Mathlib's `det_mul` proof. Andreief follows from
  Hankel = Vᵀ·diag(w)·V together with Mathlib's `det_vandermonde`. The rest is bookkeeping between `Fin K` and
  `range K`.
- **Part C (K → ∞).** It uses three facts:
  - `heineK` is monotone in K;
  - the Hankel entries converge to their tsums;
  - `det` is continuous.

  Together these give that the sup equals the limit, which equals the determinant.
- **Part A (smooth ζ).** Mathlib has no Lambert W, so γ = N₀⁻¹ is defined via `Function.invFunOn` on `[2π, ∞)`:
  - surjectivity from `intermediate_value_Ici`;
  - continuity from strict monotonicity plus surjectivity onto an interval;
  - the derivative from `HasDerivAt.of_local_left_inverse`.

  The antitone majorant E of |ε| is defined generically as `E t := ⨆ u ≥ t, |ε u|`.

**Tech Stack:** Lean 4.34.1, Mathlib v4.34.1, and the JacobiAsym library on `master` (`05595bd`).

**Spec:** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` §6 (scope note: the bridge plans).
Mathematical sources: item 11 `PROOF.md` §7 Lemma H1 (Heine/Andreief) and §7b Corollary H_L-ζ, with its hypothesis
check (monotonicity of L ⇔ γ²/2π + ℓ/8π − 11γ/8 ≥ 0, ε ~ 2/log ξ, ε < 2).

**Decomposition (user-approved "full bridge").**
- Plan 4: this plan.
- Plan 5: orthogonal polynomials, the three-term recurrence, and H2 (D_n = m₀ⁿ Π b_j^{2(n−j)}), so the law is
  stated for b_j.
- Plan 6: the Toeplitz eigenvalue count.

**TDD in Lean** works as in Plans 2–3. RED is the statement with `sorry` plus `check.sh` failing. GREEN is
`lean/check.sh` printing `AUDIT OK`. **Gate rule (Plan 3 lesson):** single-file checks must be run as
`lake env lean F; echo $?`, never piped through `head` or `grep` without the exit status. `check.sh` is the only
completion gate. All statements below were typechecked on 2026-10-13. `zetaGamma` was typechecked as a `sorry`
definition; Task 4 gives its real definition.

## Global Constraints

- Lean 4.34.1 and Mathlib v4.34.1. Never run `lake update`; the shared cache is read-only.
- No `sorry`, `admit` or `axiom`. Axioms are limited to propext, Classical.choice and Quot.sound.
- Audit lines and the `need` list are updated per task.
- Commit prefix `lean:`. Each commit ends with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Branch `plan-4-lean-bridge` from `master`.
- Indexing: atom k ↔ item-11 atom k+1. Hankel entries are indexed `i j : Fin n`, with exponent `i + j`.
- Do not change the Plan 2/3 statements, except as dictated by the Plan 3 final review (applied first, Task 0).

## Review Focus

1. **Cauchy–Binet bookkeeping.** The sum over n-subsets S of `Fin K`, re-indexed by `S.orderEmbOfFin`. Edge cases:
   n = 0 (both sides 1), n > K (empty sum vs. rank-deficient product; both 0).
2. **`Fin K` ↔ `range K`.** `heineK` sums over `Finset ℕ` subsets of `range K`; Cauchy–Binet over `Finset (Fin K)`.
   The bijection (`Finset.map Fin.valEmbedding`) must preserve both the order and the Vandermonde sign. Squaring
   removes the sign, but use the same order on both sides.
3. **K → ∞ hypotheses.** Moments need `Summable` of `w k * x k ^ r`. That comes from `Summable w` and bounded `x`.
   Check that the theorem is not vacuous: for the ζ measure, |x k| ≤ 1/(9² + ¼).
4. **ζ instance at the left end.** All `SlowFactor` fields are on `[1, ∞)`, with γ(1) ≈ 14.52. The choice of a0 must
   make `E a0 < 2` *provable*. Use the limit ε → 0 to pick a0, rather than computing sup |ε| over [1, ∞).
5. **The ζ weights.** U must be monotone on all of ℝ (`Monotone U`), with `U ≥ 1` and `log U(n)/n → 0`. Use
   `U t := max 1 (zetaL (max t 1) / zetaL 1)`. Summability of 2x_k needs an explicit majorant; use the slow-variation
   bound L(t) ≤ L(a)·(t/a)^{1/2} beyond some a.

---

### Task 0: Apply the Plan 3 final-review findings

The review verdict was "ready to merge; no Critical or Important issues". Two Minor findings are documentation
overclaims. Under the repo's no-overclaim rule they are re-graded to Important and fixed here. M3 is folded in
because Tasks 5–6 depend on it. M4 (deprecation warnings) stays deferred.

**Files:** `lean/JacobiAsym/Inputs.lean`, `lean/JacobiAsym/TheoremHL.lean`, `lean/JacobiAsym/SlowFactor.lean`
(docstrings only), `lean/README.md`.

- [ ] **Step 1: Failing check.** Run `grep -n "of the infinite measure" lean/JacobiAsym/Inputs.lean` and
  `grep -n "3p/2 + log c(p)" lean/JacobiAsym/TheoremHL.lean`. Both currently match; the overclaims are present.
- [ ] **Step 2: Fix the docstrings.**
  - **M2, `heineD`.** Replace "`D_n` of the infinite measure" with "Heine-sum surrogate for `D_n`: the supremum of
    the truncated Heine sums. It equals det(m_{i+j}) by Andreief + K → ∞; that is proved in Plan 4
    (`heineD_eq_det`), not here."
  - **M2, `TheoremHPure`.** Add: "This is item 11's Theorem H transported to `heineD` via H1. Item 11 supplies it
    only for p ∈ {1, 2} and s ≥ s0(p), with s0(2) = 2, s0(1) = 3/2, and κ = 3p/2 + log c(p)."
  - **M1, `theoremHL`.** Replace the κ claim with: "`κ` is the constant of the input; item 11 supplies
    `TheoremHPure p κ s` only for p ∈ {1, 2} and s ≥ s0(p), with κ = 3p/2 + log c(p). The theorem is therefore
    *usable* only there."
  - **M3, `SlowFactor`.** Add: "`L_deriv` is two-sided at t = 1. Item 11 needs one-sided C¹ only; extend L past 1
    when instantiating. In `theoremHL`, `hU1`/`Monotone U` lose no generality: replace U by
    t ↦ U(max t 1)/U(1), or use a running max."
  - In the `lean/README.md` `theoremHL` row, add "(input available for p ∈ {1,2}, s ≥ s0(p))".
- [ ] **Step 3: Verify.** Both greps from Step 1 now return nothing, and `lean/check.sh` prints `AUDIT OK`.
- [ ] **Step 4: Commit** `lean: Plan 3 review fixes — docstrings for heineD/TheoremHPure scope, theoremHL p-range,
  SlowFactor notes`.

---

### Task 1: Cauchy–Binet

**Files:**
- Create: `lean/JacobiAsym/CauchyBinet.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces: `det_mul_cauchyBinet`.

- [ ] **Step 1: Write the statement with `sorry`**

```lean
import Mathlib

open Finset Matrix

namespace JacobiAsym

/-- Cauchy–Binet for `A : n × K`, `B : K × n` over ℝ: sum over `n`-subsets `S` of the columns, enumerated
increasingly by `S.orderEmbOfFin`. -/
theorem det_mul_cauchyBinet {n K : ℕ} (A : Matrix (Fin n) (Fin K) ℝ) (B : Matrix (Fin K) (Fin n) ℝ) :
    (A * B).det = ∑ S : {S : Finset (Fin K) // S.card = n},
      (A.submatrix id (S.1.orderEmbOfFin S.2)).det * (B.submatrix (S.1.orderEmbOfFin S.2) id).det := by
  sorry

end JacobiAsym
```

Add the import, the audit line, and `det_mul_cauchyBinet` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/CauchyBinet.lean; echo $?`
Expected: a `sorry` warning and exit code 0.

- [ ] **Step 3: Prove**

The standard proof, mirroring Mathlib's `Matrix.det_mul`:
1. `det (A * B) = ∑_{σ} sign σ ∏_i ∑_k A i k * B k (σ i)`, by `det_apply` and `mul_apply`.
2. Swap the product and sum (`Finset.prod_univ_sum`) to get `∑_{f : Fin n → Fin K} ∏_i A i (f i) · det(B.submatrix f id)`,
   using multilinearity in rows: `det_mul_aux`-style, or prove `∑_σ sign σ ∏_i B (f i) (σ i) = det (B.submatrix f id)`
   directly from `det_apply`.
3. Non-injective f contribute 0, since `det` of a matrix with two equal rows is 0 (`det_zero_of_row_eq`).
4. Injective f correspond bijectively to pairs (S, τ), with S = image f (card n) and τ ∈ Perm (Fin n), via
   f = orderEmb_S ∘ τ.
5. `det(B.submatrix (e ∘ τ) id) = sign τ · det(B.submatrix e id)` (`det_permute`). Summing over τ gives
   `det(A.submatrix id e)` by `det_apply` on the transpose side.

Expect 150–300 lines. Factor out lemmas:
- `sum_det_submatrix_rows`: step 2;
- `injective_fun_equiv_subset_perm`: step 4, an `Equiv` between `{f // Injective f}` and
  `Σ S : {S // card = n}, Perm (Fin n)`;
- `det_submatrix_comp_perm`: step 5.

Each gets its own audit line.

- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`, which must print `AUDIT OK`.
- [ ] **Step 5: Commit** `lean: Cauchy–Binet for rectangular real matrices`.

---

### Task 2: Andreief/Heine: `heineK = det(hankelK)`

**Files:**
- Create: `lean/JacobiAsym/Andreief.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: `det_mul_cauchyBinet` (Task 1); `heineK`, `heineTerm`, `pairs` (Plan 2); Mathlib `det_vandermonde`.
- Produces: `hankelK` and `heineK_eq_det`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.CauchyBinet
import JacobiAsym.Heine

open Finset Matrix

namespace JacobiAsym

/-- Truncated Hankel moment matrix `(∑_{k<K} w k x k^(i+j))_{i,j<n}`. -/
noncomputable def hankelK (x w : ℕ → ℝ) (K n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun i j => ∑ k ∈ range K, w k * x k ^ ((i : ℕ) + j)

/-- Andreief / Heine (item 11 Lemma H1, finite form). -/
theorem heineK_eq_det (x w : ℕ → ℝ) (K n : ℕ) : heineK x w K n = (hankelK x w K n).det := by
  sorry

end JacobiAsym
```

Add the import, an audit line, and `heineK_eq_det` to `need`.

- [ ] **Step 2: Confirm RED** with `lake env lean JacobiAsym/Andreief.lean; echo $?`: one `sorry` warning, exit 0.
- [ ] **Step 3: Prove**
  1. **Factorization.** `hankelK = A * B`, with `A i k = w k * x k ^ i` (`Fin n × Fin K`) and `B k j = x k ^ j`, so
     A = Vᵀ diag(w). Prove it entrywise with `mul_apply` and `Fin.sum_univ_eq_sum_range`.
  2. **Cauchy–Binet** gives `∑_S det(A_S) det(B_S)`.
     - `det(B_S)` is the Vandermonde determinant of `fun i => x (S.orderEmbOfFin i)`. By `det_vandermonde` it equals
       `∏_{i} ∏_{j > i} (x s_j − x s_i)`.
     - `det(A_S) = (∏_{k∈S} w k)·det(B_Sᵀ)`, pulling the column scalings out with `det_mul_column`, or via
       `A_S = (B_S)ᵀ * diagonal w_S` and `det_mul`, `det_diagonal`, `det_transpose`.
     - So each term is `(∏ w)·(det B_S)²`.
  3. **Squared Vandermonde.** `(∏_{i<j}(x s_j − x s_i))² = ∏_{(a,b) ∈ pairs S'} (x a − x b)²`, where S' ⊆ ℕ is the
     image of S under `Fin.val`. Re-index i < j to a < b on S', which is order-preserving. Use `prod_pow`, then
     `sq` of a difference is symmetric.
  4. **Re-index the sum.** Map `{S : Finset (Fin K) // card = n}` to `(range K).powersetCard n` by
     `S ↦ S.map Fin.valEmbedding`, a bijection (`Finset.sum_bij`). Products over S map accordingly (`prod_map`).

  Factor out lemmas: `hankelK_eq_mul`, `vandermonde_sq_eq_pairs`, `sum_subtype_fin_eq_powersetCard`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: Andreief/Heine — truncated Heine sum equals the Hankel determinant`.

---

### Task 3: K → ∞: `heineD = det(hankel)`

**Files:**
- Create: `lean/JacobiAsym/HankelLimit.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: `heineK_eq_det` (Task 2), `heineK_mono_K` (Plan 2), `heineD` (Plan 3).
- Produces: `hankel`, `heineD_eq_det`, and also `heineK_bdd_of_summable` (`BddAbove`, the non-vacuity of `heineD`).

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.Andreief
import JacobiAsym.Inputs

open Finset Filter Topology Matrix

namespace JacobiAsym

/-- Hankel moment matrix of the infinite measure. -/
noncomputable def hankel (x w : ℕ → ℝ) (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun i j => ∑' k, w k * x k ^ ((i : ℕ) + j)

theorem heineK_bdd_of_summable {x w : ℕ → ℝ} {X : ℝ} (hw : ∀ k, 0 ≤ w k) (hws : Summable w)
    (hx : ∀ k, |x k| ≤ X) (n : ℕ) : BddAbove (Set.range fun K => heineK x w K n) := by
  sorry

theorem heineD_eq_det {x w : ℕ → ℝ} {X : ℝ} (hw : ∀ k, 0 ≤ w k) (hws : Summable w) (hx : ∀ k, |x k| ≤ X)
    (n : ℕ) : heineD x w n = (hankel x w n).det := by
  sorry

end JacobiAsym
```

Add the import, 2 audit lines, and both names to `need`.

- [ ] **Step 2: Confirm RED**: two `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  1. **Summability of moments.** `|w k * x k ^ r| ≤ X^r · w k`, by `abs_pow` and `pow_le_pow_left₀` with `X ≥ 0`
     (from `hx 0`). So `Summable (fun k => w k * x k ^ r)` (`Summable.of_norm_bounded`).
  2. **Entrywise convergence.** `hankelK x w K n i j → hankel x w n i j` as K → ∞, from
     `(hsum).hasSum.tendsto_sum_nat`.
  3. **Continuity of det.** `Continuous Matrix.det` (`continuous_det`, or `Continuous.matrix_det continuous_id`).
     Use `tendsto_pi_nhds` twice to pass entrywise convergence to the matrix. This gives
     `heineK x w K n → det(hankel)` (rewrite with `heineK_eq_det`).
  4. **Sup equals limit.** `heineK` is monotone in K (`heineK_mono_K hw`) and convergent, hence bounded
     (`Monotone.ge_of_tendsto` gives `heineK ≤ limit`; this is `heineK_bdd_of_summable`). Also
     `tendsto_atTop_ciSup` gives the limit `⨆ K`. By `tendsto_nhds_unique`, `heineD = ⨆ = det`.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: K → ∞ — heineD equals the Hankel determinant of the infinite measure`.

---

### Task 4: The smooth-ζ ordinate γ = N₀⁻¹ and its calculus

**Files:**
- Create: `lean/JacobiAsym/ZetaSmooth.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces:
  - `N0`, `N0_deriv`, `N0_strictMonoOn`;
  - `zetaGamma`, `zetaGamma_spec`, `zetaGamma_mono`, `zetaGamma_tendsto`, `zetaGamma_hasDerivAt`;
  - `zetaL`, `zetaL_pos`.

- [ ] **Step 1: Write the statements with `sorry`** (the definition of `zetaGamma` is real, not `sorry`)

```lean
import JacobiAsym.Basic

open Filter Topology Set

namespace JacobiAsym

/-- Smooth Riemann–von Mangoldt counting function `N₀(T) = (T/2π) log(T/2πe) + 7/8`. -/
noncomputable def N0 (T : ℝ) : ℝ := T / (2 * Real.pi) * Real.log (T / (2 * Real.pi * Real.exp 1)) + 7 / 8

theorem N0_hasDerivAt {T : ℝ} (hT : 0 < T) :
    HasDerivAt N0 (Real.log (T / (2 * Real.pi)) / (2 * Real.pi)) T := by
  sorry

theorem N0_strictMonoOn : StrictMonoOn N0 (Ici (2 * Real.pi)) := by
  sorry

/-- `γ(ξ) := N₀⁻¹(ξ - 1/2)` on `[2π, ∞)` (via `invFunOn`; meaningful for `ξ ≥ 1`). -/
noncomputable def zetaGamma (ξ : ℝ) : ℝ := Function.invFunOn N0 (Ici (2 * Real.pi)) (ξ - 1 / 2)

theorem zetaGamma_spec {ξ : ℝ} (hξ : 1 ≤ ξ) : N0 (zetaGamma ξ) = ξ - 1 / 2 ∧ 9 ≤ zetaGamma ξ := by
  sorry

theorem zetaGamma_strictMonoOn : StrictMonoOn zetaGamma (Ici 1) := by
  sorry

theorem zetaGamma_tendsto : Tendsto zetaGamma atTop atTop := by
  sorry

theorem zetaGamma_hasDerivAt {ξ : ℝ} (hξ : 1 ≤ ξ) :
    HasDerivAt zetaGamma (2 * Real.pi / Real.log (zetaGamma ξ / (2 * Real.pi))) ξ := by
  sorry

/-- `L(ξ) = ξ² / (γ(ξ)² + 1/4)` (so that `ξ^{-2} L(ξ) = 1/(γ² + 1/4)`). -/
noncomputable def zetaL (ξ : ℝ) : ℝ := ξ ^ 2 / (zetaGamma ξ ^ 2 + 1 / 4)

end JacobiAsym
```

Add the import, 6 audit lines, and `zetaGamma_spec zetaGamma_hasDerivAt` to `need`.

- [ ] **Step 2: Confirm RED**: 6 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  - `N0_hasDerivAt`: `HasDerivAt.mul` and `Real.hasDerivAt_log` composed with a constant scaling. Simplify with
    `log(T/2πe) = log(T/2π) − 1` (`Real.log_div`, `Real.log_exp`), then `field_simp`/`ring`.
  - `N0_strictMonoOn`: `strictMonoOn_of_deriv_pos` on `Ici (2π)` (convex), with continuity from the derivatives. On
    the interior T > 2π, `log(T/2π) > 0`.
  - `zetaGamma_spec`:
    1. Surjectivity: `intermediate_value_Ici` with `N0 (2π) = −1/8 ≤ ξ − 1/2` (compute: `log(1/e) = −1`) and
       `N0 → ∞` (`N0 T ≥ (T/2π)(log(T/2π) − 1) + 7/8` → ∞, via `Real.tendsto_log_atTop` and products). This gives a
       preimage in `Ici (2π)`.
    2. `Function.invFunOn_eq` / `invFunOn_mem` give `N0 (zetaGamma ξ) = ξ − 1/2` and `zetaGamma ξ ≥ 2π`.
    3. `9 ≤ zetaGamma ξ`: if γ < 9, then `N0 γ < N0 9` by strict monotonicity (9 ≥ 2π), and
       `N0 9 = (9/2π)(log(9/2π) − 1) + 7/8 < 1/2`. That last bound needs `log(9/2π) < 1`, i.e. `9/(2π) < e`; use
       `Real.pi_gt_three` and `Real.exp_one_gt_d9`. This contradicts `N0 γ = ξ − 1/2 ≥ 1/2`.
  - `zetaGamma_strictMonoOn`: from `N0_strictMonoOn` and `zetaGamma_spec` (`StrictMonoOn.lt_iff_lt`).
  - `zetaGamma_tendsto`: N0 is bounded on bounded sets, so γ must be unbounded: `tendsto_atTop` with contradiction,
    using N0 continuous on compact `Icc (2π) R`.
  - `zetaGamma_hasDerivAt`: `HasDerivAt.of_local_left_inverse` with g = `zetaGamma ∘ (· + 1/2)` around
    a = ξ − 1/2, or directly with `f = fun T => N0 T + 1/2`.
    - It needs `ContinuousAt zetaGamma ξ`. That follows from strict monotonicity on `Ici 1` plus surjectivity onto an
      interval: `StrictMonoOn.continuousWithinAt_right_of_surjOn` / `_left_` at interior points. For ξ = 1, use the
      one-sided version; but the `SlowFactor` field only needs t ≥ 1, and `HasDerivAt` at t = 1 needs two-sided
      continuity, so extend: γ is defined and monotone on `Ici (5/8)` too, since N0(2π) = −1/8 means ξ ≥ 3/8 is in
      range. Prove continuity on `Ioi (1/2)` and use it at ξ ≥ 1.
    - It needs the eventual identity `N0 (zetaGamma y) + 1/2 = y` near ξ, which holds on `Ioi (3/8)`.
    - `N0' (γ ξ) = log(γ/2π)/2π ≠ 0`, because γ ≥ 9 > 2π.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: smooth-ζ ordinate γ = N0⁻¹ (invFunOn), monotonicity, limit, derivative`.

---

### Task 5: `zetaL` satisfies `SlowFactor 2` (generic majorant lemma included)

**Files:**
- Create: `lean/JacobiAsym/ZetaSlowFactor.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: Task 4; `SlowFactor` (Plan 3).
- Produces:
  - `antitoneMajorant`, a generic lemma: if g is bounded on `Ici 1` and g → 0, then E t := ⨆ u ∈ Ici (max t 1), |g u|
    is ≥ 0, antitone, a majorant on `Ici 1`, and tends to 0.
  - `zetaL_deriv`: an explicit L′.
  - `zetaL_slowFactor`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.ZetaSmooth
import JacobiAsym.SlowFactor

open Filter Topology Set

namespace JacobiAsym

/-- Generic antitone majorant of `|g|` on `[1, ∞)`. -/
theorem antitoneMajorant {g : ℝ → ℝ} {B : ℝ} (hB : ∀ t, 1 ≤ t → |g t| ≤ B)
    (hg : Tendsto g atTop (𝓝 0)) :
    ∃ E : ℝ → ℝ, (∀ t, 0 ≤ E t) ∧ Antitone E ∧ Tendsto E atTop (𝓝 0) ∧ ∀ t, 1 ≤ t → |g t| ≤ E t := by
  sorry

/-- **The smooth-ζ factor is slowly varying in the sense of `SlowFactor 2`** (item 11 Corollary H_L-ζ hypothesis
check, PROVED there; here formal). -/
theorem zetaL_slowFactor : ∃ (L' E : ℝ → ℝ) (a0 : ℕ), SlowFactor 2 zetaL L' E a0 := by
  sorry

end JacobiAsym
```

Add the import, 2 audit lines, and `zetaL_slowFactor` to `need`.

- [ ] **Step 2: Confirm RED**: 2 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  - `antitoneMajorant`:
    - Define `E t := ⨆ u : Ici (max t 1), |g u|`, bounded by B (`ciSup_le`).
    - Nonnegativity: `le_ciSup` at `u = max t 1`.
    - Antitone: `ciSup_le_ciSup_of_subset`-style, since the index sets shrink.
    - Majorant: `le_ciSup` at u = t.
    - Limit: for ε > 0 there is R with |g u| ≤ ε/2 for u ≥ R, so E t ≤ ε/2 for t ≥ R (`ciSup_le`).
  - `zetaL_slowFactor`, with γ = zetaGamma, ℓ = log(γ/2π), N0′(γ) = ℓ/2π:
    - **L′ (explicit).** From `zetaGamma_hasDerivAt`:
      `L'(ξ) = 2ξ/(γ²+¼) − ξ²·2γγ′/(γ²+¼)²`, with γ′ = 2π/ℓ. Prove the `HasDerivAt` by `HasDerivAt.div`,
      `.pow`, `.add_const`.
    - **ε(ξ).** `ε(ξ) = ξL′/L = 2 − 2(γ²/(γ²+¼))·(N0(γ)+½)/(γN0′(γ))`. Use `ξ = N0(γ) + ½` (`zetaGamma_spec`) and
      `field_simp`.
    - **Bounds.** `0 ≤ ε < 2` from the monotonicity reduction `γ²/(2π) + ℓ/(8π) − 11γ/8 ≥ 0` (true for γ ≥ 9; item
      11 §7b, checked symbolically there). Also `ε → 0`: `(N0(γ)+½)/(γN0′(γ)) = 1 − 1/ℓ + 11π/(4γℓ) → 1` and
      `γ²/(γ²+¼) → 1`, as γ → ∞ (`zetaGamma_tendsto`, `Real.tendsto_log_atTop`).
    - **E.** Apply `antitoneMajorant` with B = 2.
    - **a0.** Choose a0 ∈ ℕ with E a0 ≤ 1 < 2, from `E → 0` (`eventually_atTop`), with a0 ≥ 1.
    - **L_mono.** L is monotone on `Ici 1`, because `L′ ≥ 0` there (ε ≥ 0 and L > 0). Use
      `monotoneOn_of_deriv_nonneg` on the convex set `Ici 1`.
    - **f_dec.** `ξL′ < 2L ⇔ ε < 2`.
    - **L'_cont.** L′ is a composition of continuous functions on `Ici 1`, using γ continuous (Task 4).
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Commit** `lean: smooth-ζ factor satisfies SlowFactor 2 (generic antitone majorant)`.

---

### Task 6: Corollary H_L-ζ

**Files:**
- Create: `lean/JacobiAsym/SmoothZetaHL.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`, `lean/README.md`, `README.md`

**Interfaces:**
- Consumes: `zetaL_slowFactor` (Task 5), `theoremHL` (Plan 3), `heineD_eq_det` (Task 3).
- Produces:
  - `smoothZeta_HL`: the corollary in `hnorm` form.
  - `smoothZeta_HL_det`: the same conclusion stated with `(hankel x w n).det` in place of `heineD`, which is
    non-vacuous by Task 3.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.ZetaSlowFactor
import JacobiAsym.TheoremHL
import JacobiAsym.HankelLimit

open Filter Topology

namespace JacobiAsym

/-- Smooth-ζ atoms `x_k = 1/(γ(k+1)² + 1/4)` and weights `2 x_k` (item 11's measure with the smooth model). -/
noncomputable def zetaAtom (k : ℕ) : ℝ := 1 / (zetaGamma ((k : ℝ) + 1) ^ 2 + 1 / 4)

/-- **Corollary H_L-ζ** (PROVED-mod-input `TheoremHPure 2 κ 2`). -/
theorem smoothZeta_HL {κ : ℝ} (hH : TheoremHPure 2 κ 2) :
    Tendsto (hnorm 2 κ (heineD zetaAtom (fun k => 2 * zetaAtom k)) (fun n => Real.log (zetaL n)))
      atTop (𝓝 0) := by
  sorry

/-- The same, stated for the Hankel determinant of the infinite smooth-ζ measure. -/
theorem smoothZeta_HL_det {κ : ℝ} (hH : TheoremHPure 2 κ 2) :
    Tendsto (hnorm 2 κ (fun n => (hankel zetaAtom (fun k => 2 * zetaAtom k) n).det) (fun n => Real.log (zetaL n)))
      atTop (𝓝 0) := by
  sorry

end JacobiAsym
```

Add the import, 2 audit lines, and both names to `need`.

- [ ] **Step 2: Confirm RED**: 2 `sorry` warnings, exit 0.
- [ ] **Step 3: Prove**
  - `smoothZeta_HL`: obtain `⟨L', E, a0, hL⟩ := zetaL_slowFactor`, then apply `theoremHL hL hH hH`.
    - s = s0 = 2; c1 = c2 = 2·zetaL 1; U t := max 1 (zetaL (max t 1) / zetaL 1).
    - `slowAtom 2 zetaL (k+1) = zetaAtom k`: `rpow_neg`/`rpow_natCast`, `field_simp`. Use `funext` to rewrite the
      `heineD` atoms.
    - `hwlo`: `c1 (k+1)^{-2} ≤ 2 x_k = 2 L(k+1) (k+1)^{-2}`, because L(k+1) ≥ L(1) (monotone).
    - `hwhi`: `2 x_k = c2 (k+1)^{-2} (L(k+1)/L(1)) ≤ c2 (k+1)^{-2} U(k+1)`.
    - `hU1`, `hUmono`: from `max` and the monotonicity of L on `Ici 1`.
    - `hUsub`: `log U(n)/n → 0`, because `log L(n) ≤ log L(1) + E(1) log n` (`logL_slow`).
    - `hwsum`: from `hL.logL_slow`, beyond a1 with E(a1) ≤ 1/2 we have `L(t) ≤ L(a1)(t/a1)^{1/2}`. So
      `x_k ≤ C (k+1)^{-3/2}`, which is summable (`Real.summable_nat_rpow_inv` with exponent 3/2 > 1), using
      `Summable.of_nonneg_of_le` plus finitely many initial terms (`summable_nat_add_iff`).
  - `smoothZeta_HL_det`: rewrite with `heineD_eq_det` (Task 3), with X = 1/(81 + 1/4), since |x_k| ≤ that by
    γ ≥ 9 (`zetaGamma_spec`). The weights are summable as above.
- [ ] **Step 4: Confirm GREEN** with `lean/check.sh`.
- [ ] **Step 5: Docs.**
  - Add `lean/README.md` rows for Tasks 1–6.
  - Top-level `README.md` status: "Lean: Theorem H_L and Corollary H_L-ζ (smooth ζ model, stated for the Hankel
    determinant) proved from the named input Theorem H."
  - Spec §6 note: "Plan 4 done: Cauchy–Binet, Andreief, K → ∞, smooth-ζ instance."
- [ ] **Step 6: Commit** `lean: Corollary H_L-ζ for the smooth ζ measure (Hankel-determinant form)`.

---

## After this plan

- **Plan 5.** Orthogonal polynomials of a discrete measure, the three-term recurrence, b_j² = D_{j−1}D_{j+1}/D_j²
  (H2), and the b_j form of the law.
- **Plan 6.** The Toeplitz count.
- **Research plans.**
