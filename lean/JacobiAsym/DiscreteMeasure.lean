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
    Summable (fun k => w k * p.eval (x k) * q.eval (x k)) := by
  obtain ⟨X, hX⟩ := h.x_bdd
  have hK : IsCompact (Set.Icc (-X) X) := isCompact_Icc
  obtain ⟨Bp, hBp⟩ := hK.exists_bound_of_continuousOn p.continuous.continuousOn
  obtain ⟨Bq, hBq⟩ := hK.exists_bound_of_continuousOn q.continuous.continuousOn
  have hmem : ∀ k, x k ∈ Set.Icc (-X) X := fun k => abs_le.1 (hX k)
  refine Summable.of_norm_bounded (h.w_sum.mul_left (Bp * Bq)) (fun k => ?_)
  have h1 := hBp (x k) (hmem k)
  have h2 := hBq (x k) (hmem k)
  rw [Real.norm_eq_abs] at h1 h2 ⊢
  rw [abs_mul, abs_mul, abs_of_pos (h.w_pos k)]
  have hw := (h.w_pos k).le
  calc w k * |eval (x k) p| * |eval (x k) q| ≤ w k * Bp * Bq := by
        apply mul_le_mul (mul_le_mul_of_nonneg_left h1 hw) h2 (abs_nonneg _)
        exact mul_nonneg hw ((abs_nonneg _).trans h1)
    _ = Bp * Bq * w k := by ring

theorem dip_comm (x w : ℕ → ℝ) (p q : ℝ[X]) : dip x w p q = dip x w q p := by
  unfold dip; congr 1; funext k; ring

theorem dip_add_left {x w : ℕ → ℝ} (h : DMeasure x w) (p p' q : ℝ[X]) :
    dip x w (p + p') q = dip x w p q + dip x w p' q := by
  unfold dip
  rw [← Summable.tsum_add (dip_summable h p q) (dip_summable h p' q)]
  congr 1; funext k; rw [eval_add]; ring

theorem dip_smul_left (x w : ℕ → ℝ) (c : ℝ) (p q : ℝ[X]) : dip x w (C c * p) q = c * dip x w p q := by
  unfold dip
  rw [← tsum_mul_left]
  congr 1; funext k; rw [eval_mul, eval_C]; ring

theorem dip_sum_left {x w : ℕ → ℝ} (h : DMeasure x w) {ι : Type*} (s : Finset ι) (f : ι → ℝ[X]) (q : ℝ[X]) :
    dip x w (∑ i ∈ s, f i) q = ∑ i ∈ s, dip x w (f i) q := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [dip]
  | insert a s ha ih => rw [sum_insert ha, sum_insert ha, dip_add_left h, ih]

theorem dip_X_mul (x w : ℕ → ℝ) (p q : ℝ[X]) : dip x w (X * p) q = dip x w p (X * q) := by
  unfold dip; congr 1; funext k; rw [eval_mul, eval_mul, eval_X]; ring

theorem dip_pow_pow (x w : ℕ → ℝ) (i j : ℕ) : dip x w (X ^ i) (X ^ j) = mom x w (i + j) := by
  unfold dip mom; congr 1; funext k; rw [eval_pow, eval_pow, eval_X, pow_add]; ring

theorem dip_self_eq_zero {x w : ℕ → ℝ} (h : DMeasure x w) {p : ℝ[X]} (hp : dip x w p p = 0) : p = 0 := by
  have hnn : ∀ k, 0 ≤ w k * p.eval (x k) * p.eval (x k) := fun k => by
    rw [mul_assoc]; exact mul_nonneg (h.w_pos k).le (mul_self_nonneg _)
  have hsum : HasSum (fun k => w k * p.eval (x k) * p.eval (x k)) 0 := by
    have := (dip_summable h p p).hasSum; unfold dip at hp; rwa [hp] at this
  have hz := (hasSum_zero_iff_of_nonneg hnn).1 hsum
  have hroot : ∀ k, p.IsRoot (x k) := by
    intro k
    have := congrFun hz k
    simp only [Pi.zero_apply] at this
    have hw := (h.w_pos k).ne'
    rw [mul_assoc] at this
    rcases mul_eq_zero.1 this with h1 | h1
    · exact absurd h1 hw
    · exact mul_self_eq_zero.1 h1
  apply Polynomial.eq_zero_of_infinite_isRoot
  apply Set.Infinite.mono _ (Set.infinite_range_of_injective h.x_anti.injective)
  rintro _ ⟨k, rfl⟩; exact hroot k

theorem hankel_eq_mom (x w : ℕ → ℝ) (n : ℕ) (i j : Fin n) : hankel x w n i j = mom x w ((i : ℕ) + j) := rfl

theorem hankel_det_pos {x w : ℕ → ℝ} (h : DMeasure x w) (n : ℕ) : 0 < (hankel x w n).det := by
  obtain ⟨X, hX⟩ := h.x_bdd
  have hw := fun k => (h.w_pos k).le
  rw [← heineD_eq_det hw h.w_sum hX]
  exact heineD_pos h.x_anti h.w_pos (heineK_bdd_of_summable hw h.w_sum hX n)

end JacobiAsym
