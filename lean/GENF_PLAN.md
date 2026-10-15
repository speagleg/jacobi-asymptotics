# Plan 61 — formalizing Paper 1 Theorem 1.1 (general atoms x_k = f(k)) in Lean

Goal: Paper 1 (papers/paper1/main.tex) Theorem `thm:main`, in full: p > 0, C > 0, f ∈ C¹[1,∞) with
ξ^{p+1} f'(ξ) → −pC and 0 < inf_{ξ≥1} ξ^{p+1}|f'(ξ)| ≤ sup < ∞; weights w_k ≥ 0, Σ w_k < ∞, w_k ≥ c₁ k^{−s}
(c₁ > 0, **any real s**). Then log D_n = −p n² log n + (κ_p + log C) n² + o(n²). Plus Corollary `cor:jacobi`
(Jacobi form) and Corollary `cor:zeta` (zeta-value determinants, real a > 0, 2a + b > 1).

Existing input (Plan 60): `hall_upper`, `hall_lower`, `theoremHPure_all` — pure powers `powSeq p`, weights
`powSeq s`, s > 1 only. Existing definitions and statements are not modified; everything below is in new modules.

## 0. Design decisions

1. **Route.** The paper's route: pure powers with general weights (Theorems 4.3/5.2 use only Σw < ∞, resp.
   w_k ≥ c₁k^{−s}), then scaling by C (Lemma 2.2(iii)), then the regular-spacing comparison (Lemma 2.3). We follow it.
   * Upper bound, general weights: the proof of `hall_upper` uses the weights only through W = Σ w_k, w ≥ 0 and the
     positivity of the head sums, so it is re-run with a general positive summable `w` (`hall_upper_w`). It cannot be
     transferred from `powSeq s` weights (a summable `w` need not be dominated by c·k^{−s}).
   * Lower bound, general weights, any real s: transferred from `hall_lower` by monotonicity in the weights:
     for s' := max s 2 > 1, c₁ k^{−s'} ≤ c₁ k^{−s} ≤ w_k, so heineK x w ≥ c₁ⁿ heineK x (powSeq s'), and
     n log c₁ = o(n²). No re-proof needed (this is how the paper's "any real s" is reached).
2. **Translation invariance is automatic**: `heineTerm` depends only on differences x_a − x_b, so the limit L of f
   never appears; Lemma 2.3 is applied directly to f and h(ξ) = Cξ^{−p}.
3. **Lemma 2.3 in Lean** (no η(m) function): for every ε > 0 there are a₀ and B ≥ 1 such that, for every pair a < b
   of 0-based indices, x_a − x_b ≤ B'·(y_a − y_b) and y_a − y_b ≤ B'·(x_a − x_b), with B' = e^ε if a ≥ a₀ and B' = B·e^ε
   if a < a₀ (Cauchy MVT on [a+1, b+1], `ratio_bounds_of_deriv`). `heineTerm_le_of_pair_le_split` then gives
   heineTerm x ≤ B^{2a₀n} e^{εn(n−1)} heineTerm y and symmetrically; the cost is O(n) + εn², so the hnorm limits agree.
4. **C¹[1,∞)** is stated as `∀ ξ ∈ Ici 1, HasDerivWithinAt f (f' ξ) (Ici 1) ξ` and `ContinuousOn f' (Ici 1)`
   (one-sided derivative at 1, as in the paper). The bounds 0 < inf ≤ sup < ∞ are stated as
   `∃ m M, 0 < m ∧ ∀ ξ ≥ 1, m ≤ ξ^{p+1}|f' ξ| ∧ ξ^{p+1}|f' ξ| ≤ M`. Continuity of f' is used (as in the paper) to
   get f' < 0 on [1,∞) (IVT).
5. **Indexing.** 0-based: atom k ↦ x k = f(k+1), weight w k = w_{k+1}, w_{k+1} ≥ c₁ (k+1)^{−s}. D_n is stated both as
   `heineD x w n` and as `(hankel x w n).det` = det(m_{i+j})_{i,j<n} (via `heineD_eq_det`).

## 1. Stages and exact Lean statements

| Stage | File | Statement | Status |
|---|---|---|---|
| G1 | GenWeights.lean | `hall_upper_w (hp : 0 < p) (hw : ∀ k, 0 < w k) (hws : Summable w) (hη : 0 < η) : ∀ᶠ n in atTop, hnorm p (hallKappa p) (heineD (powSeq p) w) (fun _ => 0) n ≤ η` | done (sorry-free) |
| G1 | GenWeights.lean | `hall_lower_w (hp : 0 < p) (hc1 : 0 < c1) (hw0 : ∀ k, 0 ≤ w k) (hws : Summable w) (hwlo : ∀ k, c1 * powSeq s k ≤ w k) (hη : 0 < η) : ∀ᶠ n in atTop, -η ≤ hnorm …` (s : ℝ arbitrary) | done (sorry-free) |
| G1 | GenWeights.lean | `pure_law_w` : `Tendsto (hnorm p (hallKappa p) (heineD (powSeq p) w) (fun _ => 0)) atTop (𝓝 0)` | done (sorry-free) |
| G2 | Spacing.lean | `PairRatio x y` (Prop: for every ε > 0 there are a₀, B ≥ 1 with the two-sided pair bounds of §0.3) and `hnorm_transfer : PairRatio x y → … → Tendsto (hnorm p κ (heineD y w) ℓ) … → Tendsto (hnorm p κ (heineD x w) ℓ) …` (Lemma 2.3) | done (sorry-free) |
| G2 | Spacing.lean | `scaled_law : … → Tendsto (hnorm p (κ + log C) (heineD (fun k => C * powSeq p k) w) …)` (Lemma 2.2(iii)) | done (sorry-free) |
| G3 | GeneralAtoms.lean | `pairRatio_of_deriv` : the hypotheses of Theorem 1.1 on f give `PairRatio (fun k => f (k+1)) (fun k => C * powSeq p k)`; `f'_neg` | done (sorry-free) |
| G3 | GeneralAtoms.lean | **`paper1_thm11`**, **`paper1_thm11_det`** (Theorem 1.1, Heine and determinant form, constant in Gamma form) | done (sorry-free) |
| G4 | GeneralAtoms.lean | **`paper1_cor12`** (Corollary 1.2 via `hankel_det_eq_prod`) | done (sorry-free) |
| G5 | ZetaHankel.lean | **`paper1_cor14`** (Corollary 1.4: det_{1≤i,j≤n} ζ(a(i+j)+b), real a > 0, 2a + b > 1) | done (sorry-free) |

Every main theorem goes into Audit.lean and the `need` list of check.sh.

## 2. Outcome (Plan 61)

All stages done, sorry-free; `lean/check.sh` prints AUDIT OK (only propext, Classical.choice, Quot.sound). No named
hypothesis remains and no hypothesis of Theorem 1.1 is strengthened (the derivative is given as an explicit `f'` with
`HasDerivWithinAt … (Ici 1)` and `ContinuousOn f' (Ici 1)`, which is f ∈ C¹[1,∞)). Final names: `pure_law_w`,
`hnorm_transfer`, `scaled_law`, `pairRatio_of_hyp`, `paper1_thm11_heine`, `paper1_thm11` (GeneralAtoms.lean),
`paper1_cor12`, `paper1_cor14` (+ `_one`, `_two`) (Paper1Corollaries.lean). In Corollary 1.4 the determinant is of the real
matrix `(Re ζ(a(i+j)+b))`; `zeta_re_eq_tsum` shows ζ is real (= Σ (k+1)^{−t}) there.
