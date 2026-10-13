import JacobiAsym.Recurrence

open Finset Matrix

namespace JacobiAsym

/-- **H2** (item 11 Lemma H2): `D_n = m₀ⁿ ∏_{j=1}^{n-1} (b_j²)^{n-j}`. -/
theorem hankel_one_det (x w : ℕ → ℝ) : (hankel x w 1).det = mom x w 0 := by
  rw [Matrix.det_fin_one, hankel_eq_mom]; rfl

/-- `h_j := D_{j+1}/D_j = m₀ ∏_{i=1}^{j} b_i²`. -/
theorem hratio_eq {x w : ℕ → ℝ} (h : DMeasure x w) (j : ℕ) :
    (hankel x w (j + 1)).det / (hankel x w j).det = mom x w 0 * ∏ i ∈ Ico 1 (j + 1), jb2 x w i := by
  induction j with
  | zero => rw [zero_add, hankel_one_det, det_isEmpty, div_one]; simp
  | succ j ih =>
    rw [prod_Ico_succ_top (by omega : 1 ≤ j + 1), ← mul_assoc, ← ih]
    have h0 := hankel_det_pos h j
    have h1 := hankel_det_pos h (j + 1)
    unfold jb2
    rw [show j + 1 - 1 = j by omega]
    field_simp

theorem prod_pow_step (b : ℕ → ℝ) (n : ℕ) :
    ∏ i ∈ Ico 1 (n + 1), b i ^ (n + 1 - i) = (∏ i ∈ Ico 1 n, b i ^ (n - i)) * ∏ i ∈ Ico 1 (n + 1), b i := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · rw [prod_Ico_succ_top (by omega : 1 ≤ n), prod_Ico_succ_top (by omega : 1 ≤ n),
      Nat.add_sub_cancel_left, pow_one]
    have e : ∏ i ∈ Ico 1 n, b i ^ (n + 1 - i) = (∏ i ∈ Ico 1 n, b i ^ (n - i)) * ∏ i ∈ Ico 1 n, b i := by
      rw [← prod_mul_distrib]
      apply prod_congr rfl; intro i hi
      have : i < n := (mem_Ico.1 hi).2
      rw [show n + 1 - i = n - i + 1 by omega, pow_succ]
    rw [e]; ring

theorem hankel_det_eq_prod {x w : ℕ → ℝ} (h : DMeasure x w) (n : ℕ) :
    (hankel x w n).det = mom x w 0 ^ n * ∏ j ∈ Ico 1 n, jb2 x w j ^ (n - j) := by
  induction n with
  | zero => simp [det_isEmpty]
  | succ n ih =>
    have hn := hankel_det_pos h n
    have hr := hratio_eq h n
    rw [div_eq_iff hn.ne'] at hr
    rw [hr, ih, prod_pow_step, pow_succ]
    ring

end JacobiAsym
