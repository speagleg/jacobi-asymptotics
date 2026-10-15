import JacobiAsym.Basic

/-! # Plan 60, stage S0: the constants of Theorem H_all

`hallLam p = ∫₀¹ arccos (2 s^p − 1) ds` (= `2 I(p)` of Paper 1 (1.2), proved in stage S6),
`hallC p = (π / hallLam p)^p / 4` (= `c(p)`), `hallKappa p = 3p/2 + log c(p)` (= `κ_p`).
With this normalisation `(4 c(p))^{1/p} = π / hallLam p` holds by definition. -/

open Real Set intervalIntegral MeasureTheory

namespace JacobiAsym

/-- `Λ(p) = ∫₀¹ arccos (2 s^p − 1) ds` (Paper 1: `Λ(p) = B(1/p + 1/2, 1/2) = 2 I(p)`). -/
noncomputable def hallLam (p : ℝ) : ℝ := ∫ s in (0 : ℝ)..1, arccos (2 * s ^ p - 1)

/-- `c(p) = (π / Λ(p))^p / 4`. -/
noncomputable def hallC (p : ℝ) : ℝ := (π / hallLam p) ^ p / 4

/-- `κ_p = 3p/2 + log c(p)`. -/
noncomputable def hallKappa (p : ℝ) : ℝ := 3 * p / 2 + Real.log (hallC p)

theorem continuousOn_arccos_rpow {p : ℝ} (hp : 0 < p) :
    ContinuousOn (fun s : ℝ => arccos (2 * s ^ p - 1)) (Ici 0) := by
  apply continuous_arccos.comp_continuousOn
  apply ContinuousOn.sub _ continuousOn_const
  apply ContinuousOn.mul continuousOn_const
  exact fun x _ => (continuousAt_rpow_const x p (Or.inr hp.le)).continuousWithinAt

theorem intervalIntegrable_arccos_rpow {p : ℝ} (hp : 0 < p) :
    IntervalIntegrable (fun s : ℝ => arccos (2 * s ^ p - 1)) volume 0 1 :=
  ((continuousOn_arccos_rpow hp).mono (by
    intro x hx; rw [uIcc_of_le zero_le_one] at hx; exact hx.1)).intervalIntegrable

theorem hallLam_pos {p : ℝ} (hp : 0 < p) : 0 < hallLam p := by
  apply intervalIntegral_pos_of_pos_on (intervalIntegrable_arccos_rpow hp) _ zero_lt_one
  intro s hs
  apply arccos_pos.2
  have : s ^ p < 1 := rpow_lt_one hs.1.le hs.2 hp
  linarith

theorem hallLam_lt_pi {p : ℝ} (hp : 0 < p) : hallLam p < π := by
  have h : 0 < ∫ s in (0 : ℝ)..1, (π - arccos (2 * s ^ p - 1)) := by
    apply intervalIntegral_pos_of_pos_on (intervalIntegrable_const.sub (intervalIntegrable_arccos_rpow hp)) _
      zero_lt_one
    intro s hs
    have h1 : 0 < s ^ p := rpow_pos_of_pos hs.1 p
    have : arccos (2 * s ^ p - 1) < π := arccos_lt_pi.2 (by linarith)
    linarith
  rw [integral_sub intervalIntegrable_const (intervalIntegrable_arccos_rpow hp)] at h
  simp only [intervalIntegral.integral_const, sub_zero, smul_eq_mul, one_mul] at h
  unfold hallLam; linarith

theorem hallC_pos {p : ℝ} (hp : 0 < p) : 0 < hallC p := by
  unfold hallC
  have := hallLam_pos hp
  have : 0 < π / hallLam p := div_pos pi_pos this
  positivity

/-- The defining normalisation: `(4 c(p))^{1/p} = π / Λ(p)`. -/
theorem four_hallC_rpow {p : ℝ} (hp : 0 < p) : (4 * hallC p) ^ (1 / p) = π / hallLam p := by
  have hL := hallLam_pos hp
  have h4 : 4 * hallC p = (π / hallLam p) ^ p := by unfold hallC; ring
  rw [h4, ← rpow_mul (div_pos pi_pos hL).le, mul_one_div_cancel hp.ne', rpow_one]

/-- `u_s = (4c)^{-1/p} = Λ(p)/π`. -/
theorem four_hallC_rpow_neg {p : ℝ} (hp : 0 < p) : (4 * hallC p) ^ (-(1 / p)) = hallLam p / π := by
  rw [rpow_neg (by have := hallC_pos hp; positivity), four_hallC_rpow hp, inv_div]

end JacobiAsym
