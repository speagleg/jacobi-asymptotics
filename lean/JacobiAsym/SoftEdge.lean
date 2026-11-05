import Mathlib
import JacobiAsym.HallGamma

/-! # The soft-edge condition (Q) for the lattice constraint

Source: `research/G1/RH/spectral/JZC_M1.md`, condition (Q) and Corollary Q.1; Paper IV,
`papers/paperIV/p3_kernel.tex` (Corollary "a = 4c") and `pA_equilibrium.tex`.

For the lattice constraint density `σ(y) = (1/p) y^{−1/p−1}` on `(0, ∞)` (`Y = ∞`), the soft-edge
functional is `F(a) = ∫_a^∞ σ(y) (1 − a/y)^{−1/2} dy`. Substituting `y = a/u` gives
`F(a) = (1/p) a^{−1/p} B(1/p, 1/2) = (4 c(p)/a)^{1/p}`, so `F(a) = 1` has the unique root
`a = 4 c(p)` and `F` is strictly decreasing on `(0, ∞)`. -/

open Real Set MeasureTheory

namespace JacobiAsym

/-- The soft-edge integrand `σ(y) (1 − a/y)^{−1/2}` with `σ(y) = (1/p) y^{−1/p−1}`
(JZC_M1.md, condition (Q), Corollary Q.1). -/
noncomputable def softIntegrand (p a y : ℝ) : ℝ :=
  (1 / p) * y ^ (-(1 / p) - 1) * (1 - a / y) ^ (-(1 / 2 : ℝ))

/-- The soft-edge functional `F(a) = ∫_a^∞ σ(y) (1 − a/y)^{−1/2} dy` (JZC_M1.md, (Q)). -/
noncomputable def softF (p a : ℝ) : ℝ := ∫ y in Ioi a, softIntegrand p a y

theorem image_div_Ioo {a : ℝ} (ha : 0 < a) : (fun u : ℝ => a / u) '' Ioo 0 1 = Ioi a := by
  ext y; simp only [mem_image, mem_Ioo, mem_Ioi]; constructor
  · rintro ⟨u, ⟨hu0, hu1⟩, rfl⟩
    rw [lt_div_iff₀ hu0]; nlinarith
  · intro hy
    have hy0 : 0 < y := ha.trans hy
    refine ⟨a / y, ⟨div_pos ha hy0, (div_lt_one hy0).2 hy⟩, ?_⟩
    field_simp

theorem hasDerivWithinAt_div_const_left {a u : ℝ} (hu : u ≠ 0) (s : Set ℝ) :
    HasDerivWithinAt (fun u : ℝ => a / u) (-(a / u ^ 2)) s u := by
  have := (hasDerivAt_inv hu).const_mul a
  simp only [div_eq_mul_inv] at this ⊢
  convert this.hasDerivWithinAt using 1; ring

theorem injOn_div_const_left {a : ℝ} (ha : 0 < a) : InjOn (fun u : ℝ => a / u) (Ioo 0 1) := by
  intro x hx y hy h
  simp only at h
  rw [div_eq_div_iff hx.1.ne' hy.1.ne'] at h
  exact (mul_left_cancel₀ ha.ne' h).symm

/-- After `y = a/u`: the Jacobian-weighted integrand is `(1/p) a^{−1/p} u^{1/p−1}(1−u)^{−1/2}`. -/
theorem softIntegrand_subst {p a u : ℝ} (ha : 0 < a) (hu : u ∈ Ioo (0 : ℝ) 1) :
    |-(a / u ^ 2)| • softIntegrand p a (a / u) = (1 / p) * a ^ (-(1 / p)) * betaF (1 / p) (1 / 2) u := by
  have hu0 := hu.1
  rw [abs_neg, abs_of_pos (by positivity), smul_eq_mul, softIntegrand, betaF,
    show a / (a / u) = u by field_simp, div_rpow ha.le hu0.le,
    rpow_sub_one ha.ne', rpow_sub_one hu0.ne', rpow_sub_one hu0.ne', rpow_neg hu0.le,
    show (1 / 2 : ℝ) - 1 = -(1 / 2) by norm_num]
  have h1 : 0 < u ^ (1 / p) := rpow_pos_of_pos hu0 _
  have h2 : 0 < a ^ (-(1 / p)) := rpow_pos_of_pos ha _
  field_simp

/-- `(1/p) B(1/p, 1/2) = √π Γ(1/p + 1)/Γ(1/p + 1/2) = (4 c(p))^{1/p}`. -/
theorem beta_eq_four_hallC_rpow {p : ℝ} (hp : 0 < p) :
    (1 / p) * (Real.Gamma (1 / p) * Real.Gamma (1 / 2) / Real.Gamma (1 / p + 1 / 2)) =
      (4 * hallC p) ^ (1 / p) := by
  rw [four_hallC_rpow hp, hallLam_eq_gamma hp, Real.Gamma_one_half_eq,
    Real.Gamma_add_one (by positivity : (1 / p : ℝ) ≠ 0)]
  have hG1 : 0 < Real.Gamma (1 / p + 1 / 2) := Real.Gamma_pos_of_pos (by positivity)
  have hG2 : 0 < Real.Gamma (1 / p) := Real.Gamma_pos_of_pos (by positivity)
  have hs : 0 < √π := Real.sqrt_pos.2 pi_pos
  field_simp
  rw [Real.sq_sqrt pi_pos.le]

/-- **Corollary Q.1 (integral form).** For `p > 0`, `a > 0`, the soft-edge integrand is integrable on
`(a, ∞)` and `∫_a^∞ (1/p) y^{−1/p−1} (1 − a/y)^{−1/2} dy = (4 c(p)/a)^{1/p}`
(JZC_M1.md, condition (Q) and Corollary Q.1; Paper IV, Corollary "a = 4c"). -/
theorem softF_integral {p a : ℝ} (hp : 0 < p) (ha : 0 < a) :
    IntegrableOn (fun y => (1 / p) * y ^ (-(1 / p) - 1) * (1 - a / y) ^ (-(1 / 2 : ℝ))) (Ioi a) ∧
      ∫ y in Ioi a, (1 / p) * y ^ (-(1 / p) - 1) * (1 - a / y) ^ (-(1 / 2 : ℝ)) =
        (4 * hallC p / a) ^ (1 / p) := by
  have hB := betaF_integral (α := 1 / p) (β := 1 / 2) (by positivity) one_half_pos
  have hd : ∀ u ∈ Ioo (0 : ℝ) 1, HasDerivWithinAt (fun u : ℝ => a / u) (-(a / u ^ 2)) (Ioo 0 1) u :=
    fun u hu => hasDerivWithinAt_div_const_left hu.1.ne' _
  have hcongr : EqOn (fun u => |-(a / u ^ 2)| • softIntegrand p a (a / u))
      (fun u => (1 / p) * a ^ (-(1 / p)) * betaF (1 / p) (1 / 2) u) (Ioo 0 1) :=
    fun u hu => softIntegrand_subst ha hu
  have hI := integrableOn_image_iff_integrableOn_abs_deriv_smul measurableSet_Ioo hd
    (injOn_div_const_left ha) (softIntegrand p a)
  have hE := integral_image_eq_integral_abs_deriv_smul measurableSet_Ioo hd
    (injOn_div_const_left ha) (softIntegrand p a)
  rw [image_div_Ioo ha] at hI hE
  refine ⟨hI.2 ((integrableOn_congr_fun hcongr measurableSet_Ioo).2 (hB.1.const_mul _)), ?_⟩
  change ∫ y in Ioi a, softIntegrand p a y = _
  rw [hE, setIntegral_congr_fun measurableSet_Ioo hcongr, integral_const_mul, hB.2,
    div_rpow (by have := hallC_pos hp; positivity) ha.le, ← beta_eq_four_hallC_rpow hp,
    rpow_neg ha.le]
  ring

theorem softF_eq {p a : ℝ} (hp : 0 < p) (ha : 0 < a) : softF p a = (4 * hallC p / a) ^ (1 / p) :=
  (softF_integral hp ha).2

/-- **Corollary Q.1 (uniqueness).** For `p > 0`, `a > 0`: `F(a) = 1 ↔ a = 4 c(p)`. -/
theorem softF_eq_one_iff {p a : ℝ} (hp : 0 < p) (ha : 0 < a) :
    softF p a = 1 ↔ a = 4 * hallC p := by
  have hc : 0 < 4 * hallC p := by have := hallC_pos hp; positivity
  have hx : 0 ≤ 4 * hallC p / a := (div_pos hc ha).le
  rw [softF_eq hp ha]
  constructor
  · intro h
    have h' := congrArg (· ^ p) h
    rw [← rpow_mul hx, one_div_mul_cancel hp.ne', rpow_one, one_rpow, div_eq_one_iff_eq ha.ne'] at h'
    exact h'.symm
  · rintro rfl; rw [div_self hc.ne', one_rpow]

/-- **Corollary Q.1 (monotonicity).** `F` is strictly decreasing on `(0, ∞)`. -/
theorem softF_strictAntiOn {p : ℝ} (hp : 0 < p) : StrictAntiOn (softF p) (Ioi 0) := by
  intro a ha b hb hab
  have hc : 0 < 4 * hallC p := by have := hallC_pos hp; positivity
  rw [softF_eq hp ha, softF_eq hp hb]
  exact rpow_lt_rpow (div_pos hc hb).le (div_lt_div_of_pos_left hc ha hab) (by positivity)

/-- **Corollary Q.1.** Condition (Q) `F(a) = 1` has exactly one root on `(0, ∞)`, namely `a = 4 c(p)`. -/
theorem softF_existsUnique_root {p : ℝ} (hp : 0 < p) : ∃! a, 0 < a ∧ softF p a = 1 := by
  have hc : 0 < 4 * hallC p := by have := hallC_pos hp; positivity
  exact ⟨4 * hallC p, ⟨hc, (softF_eq_one_iff hp hc).2 rfl⟩,
    fun a ⟨ha, h⟩ => (softF_eq_one_iff hp ha).1 h⟩

end JacobiAsym
