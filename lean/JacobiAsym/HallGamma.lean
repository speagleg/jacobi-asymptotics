import JacobiAsym.HallConst

/-! # Plan 60, stage S6: the Gamma form of the constant (Paper 1 (1.2))

`hallLam_eq_gamma : hallLam p = √π Γ(1/p + 1/2)/Γ(1/p + 1)` (= `2 I(p)`), hence
`hallC_eq : hallC p = ¼ (π/(2 I(p)))^p` and `hallKappa_eq : hallKappa p = 3p/2 + log (¼ (π/(2I(p)))^p)`;
special cases `hallKappa_one = 3/2 − log 2`, `hallKappa_two = 3 + log (π²/16)`.

Proof: `arccos (2y − 1) = ∫_y^1 (x(1−x))^{−1/2} dx` (FTC), Tonelli, and the real Beta integral
`∫₀¹ x^{α−1}(1−x)^{β−1} dx = Γ(α)Γ(β)/Γ(α+β)` (from Mathlib's beta distribution). -/

open Real Set MeasureTheory Filter Topology intervalIntegral
open scoped ENNReal

namespace JacobiAsym

/-- The Beta integrand. -/
noncomputable def betaF (α β x : ℝ) : ℝ := x ^ (α - 1) * (1 - x) ^ (β - 1)

theorem betaF_nonneg {α β x : ℝ} (hx : x ∈ Ioo (0 : ℝ) 1) : 0 ≤ betaF α β x :=
  mul_nonneg (rpow_pos_of_pos hx.1 _).le (rpow_pos_of_pos (by linarith [hx.2]) _).le

theorem measurable_betaF (α β : ℝ) : Measurable (betaF α β) := by unfold betaF; fun_prop

/-- The real Beta integral: integrable on `(0,1)` with value `Γ(α)Γ(β)/Γ(α+β)`. -/
theorem betaF_integral {α β : ℝ} (hα : 0 < α) (hβ : 0 < β) :
    IntegrableOn (betaF α β) (Ioo 0 1) ∧
      ∫ x in Ioo (0 : ℝ) 1, betaF α β x = Real.Gamma α * Real.Gamma β / Real.Gamma (α + β) := by
  have hB := ProbabilityTheory.beta_pos hα hβ
  have h1 := ProbabilityTheory.lintegral_betaPDF_eq_one hα hβ
  rw [ProbabilityTheory.lintegral_betaPDF] at h1
  have hlin : ∫⁻ x in Ioo (0 : ℝ) 1, ENNReal.ofReal (betaF α β x) =
      ENNReal.ofReal (ProbabilityTheory.beta α β) := by
    have e : ∀ x, ENNReal.ofReal (betaF α β x) = ENNReal.ofReal (ProbabilityTheory.beta α β) *
        ENNReal.ofReal (1 / ProbabilityTheory.beta α β * x ^ (α - 1) * (1 - x) ^ (β - 1)) := by
      intro x
      rw [← ENNReal.ofReal_mul hB.le]; congr 1; unfold betaF; field_simp
    simp_rw [e]
    rw [lintegral_const_mul _ (by fun_prop), h1, mul_one]
  have hfin : HasFiniteIntegral (betaF α β) (volume.restrict (Ioo 0 1)) := by
    rw [hasFiniteIntegral_iff_ofReal (ae_restrict_of_forall_mem measurableSet_Ioo fun x hx => betaF_nonneg hx),
      hlin]
    exact ENNReal.ofReal_lt_top
  have hint : IntegrableOn (betaF α β) (Ioo 0 1) := ⟨(measurable_betaF α β).aestronglyMeasurable, hfin⟩
  refine ⟨hint, ?_⟩
  rw [integral_eq_lintegral_of_nonneg_ae (ae_restrict_of_forall_mem measurableSet_Ioo fun x hx => betaF_nonneg hx)
    (measurable_betaF α β).aestronglyMeasurable, hlin, ENNReal.toReal_ofReal hB.le]
  rfl

/-- `g(x) = (x(1−x))^{−1/2}`. -/
noncomputable def arcG (x : ℝ) : ℝ := betaF (1 / 2) (1 / 2) x

/-- `arccos (2y − 1) = ∫_y^1 (x(1−x))^{−1/2} dx` for `0 ≤ y ≤ 1`. -/
theorem arccos_eq_integral {y : ℝ} (hy0 : 0 ≤ y) (hy1 : y ≤ 1) :
    arccos (2 * y - 1) = ∫ x in Ioo y 1, arcG x := by
  have hint := (betaF_integral (α := 1 / 2) (β := 1 / 2) one_half_pos one_half_pos).1
  have hint' : IntervalIntegrable arcG volume y 1 := by
    rw [intervalIntegrable_iff_integrableOn_Ioo_of_le hy1]
    exact hint.mono_set (Ioo_subset_Ioo_left hy0)
  have hcont : ContinuousOn (fun x => -arccos (2 * x - 1)) (Icc y 1) :=
    (continuous_arccos.comp (by fun_prop)).neg.continuousOn
  have hder : ∀ x ∈ Ioo y 1, HasDerivAt (fun x => -arccos (2 * x - 1)) (arcG x) x := by
    intro x hx
    have hx0 : 0 < x := hy0.trans_lt hx.1
    have hx1 : x < 1 := hx.2
    have h1 : 2 * x - 1 ≠ -1 := by intro h; linarith
    have h2 : 2 * x - 1 ≠ 1 := by intro h; linarith
    have hd := ((Real.hasDerivAt_arccos h1 h2).comp x ((hasDerivAt_id x).const_mul 2 |>.sub_const 1)).neg
    convert hd using 1
    · funext z; simp [Function.comp_def]
    have hq : 1 - (2 * x - 1) ^ 2 = 4 * (x * (1 - x)) := by ring
    rw [hq, Real.sqrt_mul (by norm_num), show Real.sqrt 4 = 2 by
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)]
    unfold arcG betaF
    rw [show (1 : ℝ) / 2 - 1 = -(1 / 2) by norm_num, rpow_neg hx0.le, rpow_neg (by linarith),
      ← Real.sqrt_eq_rpow, ← Real.sqrt_eq_rpow, Real.sqrt_mul hx0.le]
    have : 0 < Real.sqrt x := Real.sqrt_pos.2 hx0
    have : 0 < Real.sqrt (1 - x) := Real.sqrt_pos.2 (by linarith)
    field_simp
  rw [← intervalIntegral.integral_of_le hy1 |>.trans (integral_Ioc_eq_integral_Ioo),
    integral_eq_sub_of_hasDerivAt_of_le hy1 hcont hder hint']
  norm_num

theorem arcG_nonneg {x : ℝ} (hx : x ∈ Ioo (0 : ℝ) 1) : 0 ≤ arcG x := betaF_nonneg hx

theorem rpow_lt_iff_lt_rpow_inv {p s x : ℝ} (hp : 0 < p) (hs : 0 ≤ s) (hx : 0 ≤ x) :
    s ^ p < x ↔ s < x ^ (1 / p) := by
  constructor
  · intro h
    have := rpow_lt_rpow (rpow_nonneg hs p) h (by positivity : 0 < 1 / p)
    rwa [← rpow_mul hs, mul_one_div_cancel hp.ne', rpow_one] at this
  · intro h
    have := rpow_lt_rpow hs h hp
    rwa [← rpow_mul hx, one_div_mul_cancel hp.ne', rpow_one] at this

/-- **Stage S6**: `Λ(p) = B(1/p + 1/2, 1/2) = √π Γ(1/p + 1/2)/Γ(1/p + 1)` (`= 2 I(p)` of Paper 1 (1.2)). -/
theorem hallLam_eq_gamma {p : ℝ} (hp : 0 < p) :
    hallLam p = √π * Real.Gamma (1 / p + 1 / 2) / Real.Gamma (1 / p + 1) := by
  have hg := betaF_integral (α := 1 / 2) (β := 1 / 2) one_half_pos one_half_pos
  set H : ℝ × ℝ → ℝ := fun z => if z.1 ^ p < z.2 then arcG z.2 else 0 with hH
  have hHm : Measurable H := by
    apply Measurable.ite (measurableSet_lt (by fun_prop) measurable_snd)
      ((measurable_betaF _ _).comp measurable_snd) measurable_const
  have hHi : Integrable H ((volume.restrict (Ioc (0 : ℝ) 1)).prod (volume.restrict (Ioo (0 : ℝ) 1))) := by
    refine Integrable.mono' (hg.1.comp_snd (volume.restrict (Ioc (0 : ℝ) 1))) hHm.aestronglyMeasurable ?_
    have g2 := (Measure.quasiMeasurePreserving_snd (μ := volume.restrict (Ioc (0 : ℝ) 1))
      (ν := volume.restrict (Ioo (0 : ℝ) 1))).ae (ae_restrict_mem measurableSet_Ioo)
    filter_upwards [g2] with z hz
    simp only [hH]
    split_ifs
    · rw [Real.norm_eq_abs, abs_of_nonneg (arcG_nonneg hz)]; rfl
    · simp only [norm_zero]; exact betaF_nonneg hz
  -- step 1: Λ = ∫_s ∫_x H
  have h1 : hallLam p = ∫ s in Ioc (0 : ℝ) 1, ∫ x in Ioo (0 : ℝ) 1, H (s, x) := by
    rw [hallLam, intervalIntegral.integral_of_le zero_le_one]
    apply setIntegral_congr_fun measurableSet_Ioc
    intro s hs
    have hsp0 : 0 ≤ s ^ p := rpow_nonneg hs.1.le p
    have hsp1 : s ^ p ≤ 1 := rpow_le_one hs.1.le hs.2 hp.le
    show arccos (2 * s ^ p - 1) = ∫ x in Ioo (0 : ℝ) 1, H (s, x)
    rw [arccos_eq_integral hsp0 hsp1]
    have e : (fun x => H (s, x)) = (Ioi (s ^ p)).indicator arcG := by
      funext x; simp only [hH, indicator, mem_Ioi]
    have hset : Ioo (0 : ℝ) 1 ∩ Ioi (s ^ p) = Ioo (s ^ p) 1 := by
      ext x; simp only [Set.mem_inter_iff, Set.mem_Ioo, Set.mem_Ioi]; constructor
      · rintro ⟨⟨_, h2⟩, h1⟩; exact ⟨h1, h2⟩
      · rintro ⟨h1, h2⟩; exact ⟨⟨lt_of_le_of_lt hsp0 h1, h2⟩, h1⟩
    rw [e, setIntegral_indicator measurableSet_Ioi, hset]
  -- step 2: swap
  have h2 := integral_integral_swap (μ := volume.restrict (Ioc (0 : ℝ) 1)) (ν := volume.restrict (Ioo (0 : ℝ) 1))
    (f := fun s x => H (s, x)) hHi
  -- step 3: inner over s
  have h3 : ∀ x ∈ Ioo (0 : ℝ) 1, ∫ s in Ioc (0 : ℝ) 1, H (s, x) = betaF (1 / p + 1 / 2) (1 / 2) x := by
    intro x hx
    have hxp : x ^ (1 / p) ≤ 1 := rpow_le_one hx.1.le hx.2.le (by positivity)
    have hxp0 : 0 < x ^ (1 / p) := rpow_pos_of_pos hx.1 _
    have e : ∀ s ∈ Ioc (0 : ℝ) 1, H (s, x) = (Iio (x ^ (1 / p))).indicator (fun _ => arcG x) s := by
      intro s hs
      simp only [hH, indicator, mem_Iio]
      exact if_congr (rpow_lt_iff_lt_rpow_inv hp hs.1.le hx.1.le) rfl rfl
    rw [setIntegral_congr_fun measurableSet_Ioc e, setIntegral_indicator measurableSet_Iio, setIntegral_const]
    have hset : Ioc (0 : ℝ) 1 ∩ Iio (x ^ (1 / p)) = Ioo 0 (x ^ (1 / p)) := by
      ext s; simp only [mem_inter_iff, Set.mem_Ioc, mem_Iio, Set.mem_Ioo]; constructor
      · rintro ⟨⟨h1, _⟩, h3⟩; exact ⟨h1, h3⟩
      · rintro ⟨h1, h3⟩; exact ⟨⟨h1, by linarith⟩, h3⟩
    rw [hset, Measure.real, Real.volume_Ioo, sub_zero, ENNReal.toReal_ofReal hxp0.le, smul_eq_mul]
    unfold arcG betaF
    rw [← mul_assoc, ← rpow_add hx.1]
    congr 2; ring
  rw [h1, h2, setIntegral_congr_fun measurableSet_Ioo h3,
    (betaF_integral (α := 1 / p + 1 / 2) (β := 1 / 2) (by positivity) one_half_pos).2,
    Real.Gamma_one_half_eq, show 1 / p + 1 / 2 + 1 / 2 = 1 / p + 1 by ring]
  ring

/-- `I(p) = (√π/2) Γ(1/p + 1/2)/Γ(1/p + 1)` (Paper 1 (1.2)). -/
noncomputable def hallI (p : ℝ) : ℝ := √π / 2 * Real.Gamma (1 / p + 1 / 2) / Real.Gamma (1 / p + 1)

/-- `c(p) = ¼ (π/(2 I(p)))^p`: the Lean constant is Paper 1's `c(p)`. -/
theorem hallC_eq {p : ℝ} (hp : 0 < p) : hallC p = (π / (2 * hallI p)) ^ p / 4 := by
  rw [hallC, hallLam_eq_gamma hp, hallI]; congr 2; ring

/-- `κ_p = 3p/2 + log (¼ (π/(2 I(p)))^p)`: the Lean constant is Paper 1's `κ_p`. -/
theorem hallKappa_eq {p : ℝ} (hp : 0 < p) :
    hallKappa p = 3 * p / 2 + Real.log ((π / (2 * hallI p)) ^ p / 4) := by
  rw [hallKappa, hallC_eq hp]

theorem hallLam_one : hallLam 1 = π / 2 := by
  rw [hallLam_eq_gamma one_pos]
  norm_num
  rw [show (3 : ℝ) / 2 = 1 / 2 + 1 by norm_num, Real.Gamma_add_one (by norm_num), Real.Gamma_one_half_eq]
  have h := Real.mul_self_sqrt pi_pos.le
  linear_combination (1 / 2) * h

theorem hallLam_two : hallLam 2 = 2 := by
  rw [hallLam_eq_gamma two_pos]
  norm_num
  rw [show (3 : ℝ) / 2 = 1 / 2 + 1 by norm_num, Real.Gamma_add_one (by norm_num), Real.Gamma_one_half_eq]
  have := Real.sqrt_pos.2 pi_pos
  field_simp

/-- `c(1) = 1/2`, `κ_1 = 3/2 − log 2`. -/
theorem hallKappa_one : hallKappa 1 = 3 / 2 - Real.log 2 := by
  rw [hallKappa, hallC, hallLam_one, show π / (π / 2) = 2 by field_simp, rpow_one,
    show (2 : ℝ) / 4 = 2⁻¹ by norm_num, Real.log_inv]; ring

/-- `c(2) = π²/16`, `κ_2 = 3 + log (π²/16)`. -/
theorem hallKappa_two : hallKappa 2 = 3 + Real.log (π ^ 2 / 16) := by
  rw [hallKappa, hallC, hallLam_two, show (2 : ℝ) = ((2 : ℕ) : ℝ) by norm_num, rpow_natCast]
  norm_num
  congr 1; ring

end JacobiAsym
