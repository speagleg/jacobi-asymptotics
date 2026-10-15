import JacobiAsym.GeneralAtoms
import JacobiAsym.BLaw
import JacobiAsym.HallCorollaries
import Mathlib.NumberTheory.LSeries.RiemannZeta

/-! # Plan 61, stages G4–G5: Paper 1 Corollary 1.2 (Jacobi form) and Corollary 1.4 (zeta values)

* `paper1_cor12`: under the hypotheses of Theorem 1.1,
  `(2/n²) Σ_{j=1}^{n−1} (n−j) log(j^p b_j) → log(c(p) C)`, with `b_j = √(jb2 x w j)` the Jacobi off-diagonal
  entries (`opoly_recurrence`: `X P_k = P_{k+1} + a_k P_k + b_k² P_{k−1}`), via `hankel_det_eq_prod` (Lemma 2.4).
* `paper1_cor14`: for real `a > 0`, `b` with `2a + b > 1`,
  `log det_{1≤i,j≤n} ζ(a(i+j)+b) = −a n² log n + (3a/2 + log c(a)) n² + o(n²)`; `ζ` is Mathlib's `riemannZeta`
  (a complex function; at real arguments `> 1` it is real, and the matrix is built from the real parts). -/

open Real Filter Topology Finset

namespace JacobiAsym

/-- **Paper 1 Corollary 1.2 (Jacobi form of Theorem 1.1).** Same hypotheses as `paper1_thm11`; `b_j = √(b_j²)`
with `b_j² = jb2 x w j = D_{j+1} D_{j−1} / D_j²` the squared off-diagonal Jacobi coefficients of
`σ = Σ_k w k δ_{f(k+1)}`. -/
theorem paper1_cor12 {p C s c1 : ℝ} {f f' : ℝ → ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hC : 0 < C)
    (hf : ∀ ξ ∈ Set.Ici (1 : ℝ), HasDerivWithinAt f (f' ξ) (Set.Ici 1) ξ) (hf'c : ContinuousOn f' (Set.Ici 1))
    (hlim : Tendsto (fun ξ => ξ ^ (p + 1) * f' ξ) atTop (𝓝 (-p * C)))
    (hbd : ∃ m M : ℝ, 0 < m ∧ ∀ ξ, 1 ≤ ξ → m ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ M)
    (hw0 : ∀ k, 0 ≤ w k) (hws : Summable w) (hc1 : 0 < c1)
    (hwlo : ∀ k : ℕ, c1 * ((k : ℝ) + 1) ^ (-s) ≤ w k) :
    Tendsto (fun n : ℕ => 2 / (n : ℝ) ^ 2 * ∑ j ∈ Ico 1 n, ((n : ℝ) - j) *
        Real.log ((j : ℝ) ^ p * Real.sqrt (jb2 (fun k : ℕ => f ((k : ℝ) + 1)) w j)))
      atTop (𝓝 (Real.log ((π / (2 * hallI p)) ^ p / 4 * C))) := by
  set x := fun k : ℕ => f ((k : ℝ) + 1) with hx
  obtain ⟨-, hxa, X, hX⟩ := atoms_of_hyp hp hC hf hf'c hlim hbd
  have hwp : ∀ k, 0 < w k := fun k => (mul_pos hc1 (powSeq_pos s k)).trans_le (hwlo k)
  have hD : DMeasure x w := ⟨hwp, hws, ⟨X, hX⟩, hxa⟩
  set c := (π / (2 * hallI p)) ^ p / 4 with hc
  have hcpos : 0 < c := by rw [hc, ← hallC_eq hp]; exact hallC_pos hp
  have hK : 3 * p / 2 + Real.log c + Real.log C - 3 * p / 2 = Real.log (c * C) := by
    rw [Real.log_mul hcpos.ne' hC.ne']; ring
  set m0 := mom x w 0
  have h1 := paper1_thm11 hp hC hf hf'c hlim hbd hw0 hws hc1 hwlo
  have h3 := sum_log_weighted_asymp
  have h4 : Tendsto (fun n : ℕ => Real.log m0 / n) atTop (𝓝 0) := tendsto_const_div_atTop_nhds_zero_nat _
  have hall := ((h1.add (h3.const_mul (2 * p))).sub h4).const_add (Real.log (c * C))
  simp only [mul_zero, add_zero, sub_zero] at hall
  refine hall.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hterm : ∀ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log ((j : ℝ) ^ p * Real.sqrt (jb2 x w j)) =
      p * (((n : ℝ) - j) * Real.log j) + (1 / 2) * (((n : ℝ) - j) * Real.log (jb2 x w j)) := by
    intro j hj
    have hj0 : (0 : ℝ) < j := by exact_mod_cast (mem_Ico.1 hj).1
    have hb := jb2_pos hD j
    rw [Real.log_mul (rpow_pos_of_pos hj0 p).ne' (Real.sqrt_pos.2 hb).ne', Real.log_rpow hj0,
      Real.log_sqrt hb.le]
    ring
  have hSb : ∑ i ∈ Ico 1 n, ((n : ℝ) - i) * Real.log (jb2 x w i) =
      Real.log (hankel x w n).det - n * Real.log m0 := by rw [log_hankel_eq hD n]; ring
  rw [sum_congr rfl hterm, sum_add_distrib, ← mul_sum, ← mul_sum, hSb, ← hK]
  field_simp
  ring

/-- The zeta-value Hankel matrix `(ζ(a(i+j)+b))_{1≤i,j≤n}` (0-based: entry `(i,j)` is `ζ(a(i+1+j+1)+b)`), with
real entries `Re ζ(·)` (`ζ` is real at real arguments `> 1`, see `zeta_re_eq_tsum`). -/
noncomputable def zetaHankel (a b : ℝ) (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun i j => (riemannZeta ((a * (((i : ℕ) : ℝ) + 1 + (((j : ℕ) : ℝ) + 1)) + b : ℝ) : ℂ)).re

/-- For real `t > 1`, `ζ(t)` is real and equals `Σ_{k≥0} (k+1)^{−t}`. -/
theorem zeta_re_eq_tsum {t : ℝ} (ht : 1 < t) :
    riemannZeta (t : ℂ) = ((∑' k : ℕ, ((k : ℝ) + 1) ^ (-t) : ℝ) : ℂ) := by
  rw [zeta_eq_tsum_one_div_nat_add_one_cpow (by simpa using ht), Complex.ofReal_tsum]
  congr 1; ext k
  have hk : (0 : ℝ) < (k : ℝ) + 1 := by positivity
  rw [Real.rpow_neg hk.le, Complex.ofReal_inv, Complex.ofReal_cpow hk.le, one_div]
  push_cast; rfl

theorem zetaHankel_eq {a b : ℝ} (ha : 0 < a) (hab : 1 < 2 * a + b) (n : ℕ) :
    zetaHankel a b n = hankel (powSeq a) (powSeq (2 * a + b)) n := by
  ext i j
  simp only [zetaHankel, Matrix.of_apply, hankel_eq_mom, mom]
  have hi : (0 : ℝ) ≤ ((i : ℕ) : ℝ) := Nat.cast_nonneg _
  have hj : (0 : ℝ) ≤ ((j : ℕ) : ℝ) := Nat.cast_nonneg _
  have ht : 1 < a * (((i : ℕ) : ℝ) + 1 + (((j : ℕ) : ℝ) + 1)) + b := by nlinarith
  rw [zeta_re_eq_tsum ht, Complex.ofReal_re]
  congr 1; ext k
  have hk : (0 : ℝ) < (k : ℝ) + 1 := by positivity
  unfold powSeq
  rw [← Real.rpow_natCast, ← Real.rpow_mul hk.le, ← Real.rpow_add hk]
  congr 1; push_cast; ring

/-- **Paper 1 Corollary 1.4 (Hankel determinants of zeta values).** For real `a > 0` and `b` with `2a + b > 1`,
`log det_{1≤i,j≤n} ζ(a(i+j)+b) = −a n² log n + (3a/2 + log c(a)) n² + o(n²)`, `c(a) = ¼ (π/(2I(a)))^a`. -/
theorem paper1_cor14 {a b : ℝ} (ha : 0 < a) (hab : 1 < 2 * a + b) :
    Tendsto (fun n : ℕ => (Real.log (zetaHankel a b n).det -
        (-a * (n : ℝ) ^ 2 * Real.log n + (3 * a / 2 + Real.log ((π / (2 * hallI a)) ^ a / 4)) * (n : ℝ) ^ 2)) /
        (n : ℝ) ^ 2) atTop (𝓝 0) := by
  have h := (theoremHPure_kappa ha hab).asymp
  refine h.congr fun n => ?_
  unfold hnorm
  rw [zetaHankel_eq ha hab, ← heineD_eq_det (fun k => (powSeq_pos _ k).le) (powSeq_summable hab)
    (powSeq_abs_le_one ha)]
  ring

/-- Special cases of Corollary 1.4: `a = 1` (constant `3/2 − log 2`, every `b > −1`). -/
theorem paper1_cor14_one {b : ℝ} (hb : -1 < b) :
    Tendsto (fun n : ℕ => (Real.log (zetaHankel 1 b n).det -
        (-(n : ℝ) ^ 2 * Real.log n + (3 / 2 - Real.log 2) * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  have h := (theoremHPure_all one_pos (by linarith : (1 : ℝ) < 2 * 1 + b)).asymp
  rw [hallKappa_one] at h
  refine h.congr fun n => ?_
  unfold hnorm
  rw [zetaHankel_eq one_pos (by linarith), ← heineD_eq_det (fun k => (powSeq_pos _ k).le)
    (powSeq_summable (by linarith)) (powSeq_abs_le_one one_pos)]
  ring

/-- Special cases of Corollary 1.4: `a = 2` (constant `3 + log(π²/16)`, every `b > −3`). -/
theorem paper1_cor14_two {b : ℝ} (hb : -3 < b) :
    Tendsto (fun n : ℕ => (Real.log (zetaHankel 2 b n).det -
        (-2 * (n : ℝ) ^ 2 * Real.log n + (3 + Real.log (π ^ 2 / 16)) * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2)
      atTop (𝓝 0) := by
  have h := (theoremHPure_all two_pos (by linarith : (1 : ℝ) < 2 * 2 + b)).asymp
  rw [hallKappa_two] at h
  refine h.congr fun n => ?_
  unfold hnorm
  rw [zetaHankel_eq two_pos (by linarith), ← heineD_eq_det (fun k => (powSeq_pos _ k).le)
    (powSeq_summable (by linarith)) (powSeq_abs_le_one two_pos)]
  ring

end JacobiAsym
