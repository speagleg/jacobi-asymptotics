import JacobiAsym.Equilibrium
import JacobiAsym.Energy

/-! # Plan 60, stage S2b (value): `𝒥_p(μ*_u) = κ_p` (Paper 1 Theorem 1.3(iii), "The value")

In the parameter coordinates `a = (s, φ)`, `b = (t, ψ)` the kernel is `log |X a − X b|`. For `s < t` we have
`X b ∈ [0, β_t] ⊆ [0, β_s]`, so the arcsine potential gives `∫ log |X(s, ·) − X b| dφ/π = log (β_s/4)`.
Integrating over `s < t`, then over `b`, and using the symmetry `a ↔ b` (the diagonal `s = t` is null):
`𝒥 = 2 ∫₀¹ ∫₀^t (log c − p log s) ds dt = log c + 3p/2`.
Absolute integrability uses `∫ |log |X(s, ·) − y|| dφ/π ≤ 2 log (1 + β_s) − log (β_s/4)` (Paper 1 (3.1)). -/

open Real Set MeasureTheory Filter Topology intervalIntegral
open scoped ENNReal Interval

namespace JacobiAsym

/-! ### The angular measure -/

theorem integral_angMeas (f : ℝ → ℝ) : ∫ φ, f φ ∂angMeas = π⁻¹ * ∫ φ in (0 : ℝ)..π, f φ := by
  rw [angMeas, MeasureTheory.integral_smul_measure, ENNReal.toReal_ofReal (inv_nonneg.2 pi_pos.le), smul_eq_mul,
    intervalIntegral.integral_of_le pi_pos.le]

theorem integrable_angMeas {f : ℝ → ℝ} (hf : IntervalIntegrable f volume 0 π) : Integrable f angMeas := by
  rw [angMeas]; exact hf.1.smul_measure ENNReal.ofReal_ne_top

/-- Inner potential: `∫ log |arcX β φ − y| dφ/π = log (β/4)` for `0 ≤ y ≤ β`. -/
theorem inner_eq {β y : ℝ} (hβ : 0 < β) (hy0 : 0 ≤ y) (hyβ : y ≤ β) :
    ∫ φ, Real.log (arcX β φ - y) ∂angMeas = Real.log (β / 4) := by
  rw [integral_angMeas, arcsine_pot hβ hy0 hyβ]; field_simp

theorem log_le_log_one_add_abs (x : ℝ) : Real.log x ≤ Real.log (1 + |x|) := by
  rcases eq_or_ne x 0 with rfl | hx
  · simp
  · rw [← Real.log_abs x]; exact Real.log_le_log (abs_pos.2 hx) (by linarith)

/-- `∫ |log |arcX β φ − y|| dφ/π ≤ 2 log (1 + β) − log (β/4)` for `0 ≤ y ≤ β`. -/
theorem inner_abs_le {β y : ℝ} (hβ : 0 < β) (hy0 : 0 ≤ y) (hyβ : y ≤ β) :
    ∫ φ, |Real.log (arcX β φ - y)| ∂angMeas ≤ 2 * Real.log (1 + β) - Real.log (β / 4) := by
  have hint : Integrable (fun φ => Real.log (arcX β φ - y)) angMeas :=
    integrable_angMeas (intervalIntegrable_log_arcX_sub β y 0 π)
  set M := Real.log (1 + β)
  have hM : 0 ≤ M := Real.log_nonneg (by linarith)
  have hpt : ∀ φ, |Real.log (arcX β φ - y)| ≤ 2 * M - Real.log (arcX β φ - y) := by
    intro φ
    have h1 : Real.log (arcX β φ - y) ≤ M := by
      refine (log_le_log_one_add_abs _).trans (Real.log_le_log (by positivity) ?_)
      have := arcX_nonneg hβ.le φ; have := arcX_le hβ.le φ
      have : |arcX β φ - y| ≤ β := abs_le.2 ⟨by linarith, by linarith⟩
      linarith
    rcases le_or_gt 0 (Real.log (arcX β φ - y)) with h | h
    · rw [abs_of_nonneg h]; linarith
    · rw [abs_of_neg h]; linarith
  calc ∫ φ, |Real.log (arcX β φ - y)| ∂angMeas ≤ ∫ φ, (2 * M - Real.log (arcX β φ - y)) ∂angMeas :=
        integral_mono hint.abs ((integrable_const _).sub hint) hpt
    _ = _ := by rw [integral_sub (integrable_const _) hint, MeasureTheory.integral_const, inner_eq hβ hy0 hyβ]; simp

/-! ### The bound `g(s) = 2 log (1 + β_s) − log (β_s/4)` -/

/-- `g(s) = 2 log (1 + β_s) − log (β_s/4)`. -/
noncomputable def gStar (p s : ℝ) : ℝ := 2 * Real.log (1 + hallBeta p s) - Real.log (hallBeta p s / 4)

theorem gStar_nonneg {p s : ℝ} (hp : 0 < p) (hs : 0 < s) : 0 ≤ gStar p s := by
  have hβ := hallBeta_pos hp hs
  have h1 : Real.log (hallBeta p s / 4) ≤ Real.log (1 + hallBeta p s) :=
    Real.log_le_log (by positivity) (by linarith)
  have h2 : 0 ≤ Real.log (1 + hallBeta p s) := Real.log_nonneg (by linarith)
  unfold gStar; linarith

theorem integrableOn_abs_log : IntegrableOn (fun s : ℝ => |Real.log s|) (Ioc 0 1) :=
  (intervalIntegral.intervalIntegrable_log' (a := 0) (b := 1)).1.abs

theorem gStar_integrable {p : ℝ} (hp : 0 < p) : IntegrableOn (gStar p) (Ioc 0 1) := by
  have hc := hallC_pos hp
  have hmeas : Measurable (gStar p) := by
    unfold gStar; have := measurable_hallBeta p; fun_prop
  refine Integrable.mono' ((integrableOn_abs_log.const_mul (3 * p)).add (integrable_const
    (2 * Real.log (1 + 4 * hallC p) + |Real.log (hallC p)|))) hmeas.aestronglyMeasurable ?_
  filter_upwards [ae_restrict_mem measurableSet_Ioc] with s hs
  have hβ := hallBeta_pos hp hs.1
  have hlog : Real.log s ≤ 0 := Real.log_nonpos hs.1.le hs.2
  have hsp : 1 ≤ s ^ (-p) := one_le_rpow_of_pos_of_le_one_of_nonpos hs.1 hs.2 (by linarith)
  have hup : Real.log (1 + hallBeta p s) ≤ Real.log (1 + 4 * hallC p) - p * Real.log s := by
    have : 1 + hallBeta p s ≤ (1 + 4 * hallC p) * s ^ (-p) := by unfold hallBeta; nlinarith
    calc Real.log (1 + hallBeta p s) ≤ Real.log ((1 + 4 * hallC p) * s ^ (-p)) :=
          Real.log_le_log (by linarith) this
      _ = _ := by rw [Real.log_mul (by positivity) (by positivity), Real.log_rpow hs.1]; ring
  have hlo : 0 ≤ Real.log (1 + hallBeta p s) := Real.log_nonneg (by linarith)
  simp only [Pi.add_apply]
  rw [Real.norm_eq_abs, abs_of_nonneg (gStar_nonneg hp hs.1), gStar, log_hallBeta_div_four hp hs.1,
    abs_of_nonpos hlog]
  have := neg_abs_le (Real.log (hallC p))
  nlinarith

/-! ### Inner integral over `a = (s, φ)` for fixed `b` -/

/-- `X b ∈ [0, β_{b.1}]` on the support. -/
theorem starX_mem {p : ℝ} (hp : 0 < p) {b : ℝ × ℝ} (hb : b.1 ∈ Ioc (0 : ℝ) 1) :
    0 ≤ starX p b ∧ starX p b ≤ hallBeta p b.1 :=
  ⟨arcX_nonneg (hallBeta_pos hp hb.1).le _, arcX_le (hallBeta_pos hp hb.1).le _⟩

theorem measurable_logX (p : ℝ) : Measurable (fun z : (ℝ × ℝ) × (ℝ × ℝ) => Real.log (starX p z.1 - starX p z.2)) :=
  ((measurable_starX p).comp measurable_fst |>.sub ((measurable_starX p).comp measurable_snd)).log

/-- The truncated inner integrand `a ↦ 1[a.1 < t] log (X a − y)`. -/
noncomputable def innerF (p t y : ℝ) (a : ℝ × ℝ) : ℝ :=
  {a : ℝ × ℝ | a.1 < t}.indicator (fun a => Real.log (starX p a - y)) a

theorem measurable_innerF (p t y : ℝ) : Measurable (innerF p t y) := by
  unfold innerF
  refine Measurable.indicator ?_ (measurableSet_lt measurable_fst measurable_const)
  exact ((measurable_starX p).sub measurable_const).log

theorem innerF_slice_lt {p t y s φ : ℝ} (hs : s < t) :
    innerF p t y (s, φ) = Real.log (arcX (hallBeta p s) φ - y) :=
  Set.indicator_of_mem (show (s, φ) ∈ {a : ℝ × ℝ | a.1 < t} from hs) _

theorem innerF_slice_ge {p t y s φ : ℝ} (hs : ¬ s < t) : innerF p t y (s, φ) = 0 :=
  Set.indicator_of_notMem (show (s, φ) ∉ {a : ℝ × ℝ | a.1 < t} from hs) _

theorem innerF_slice_integrable {p t y s : ℝ} :
    Integrable (fun φ => innerF p t y (s, φ)) angMeas := by
  by_cases hs : s < t
  · simp_rw [innerF_slice_lt hs]
    exact integrable_angMeas (intervalIntegrable_log_arcX_sub _ _ _ _)
  · simp_rw [innerF_slice_ge hs]; exact integrable_zero _ _ _

theorem innerF_slice_norm_le {p t y s : ℝ} (hp : 0 < p) (hs : s ∈ Ioc (0 : ℝ) 1)
    (hy0 : 0 ≤ y) (hyt : y ≤ hallBeta p t) :
    ∫ φ, ‖innerF p t y (s, φ)‖ ∂angMeas ≤ gStar p s := by
  by_cases hst : s < t
  · simp_rw [innerF_slice_lt hst, Real.norm_eq_abs]
    exact inner_abs_le (hallBeta_pos hp hs.1) hy0 (hyt.trans (hallBeta_anti hp hs.1 hst.le))
  · simp_rw [innerF_slice_ge hst, norm_zero, integral_zero]
    exact gStar_nonneg hp hs.1

theorem innerF_integrable {p t y : ℝ} (hp : 0 < p) (_ht : t ≤ 1) (hy0 : 0 ≤ y) (hyt : y ≤ hallBeta p t) :
    Integrable (innerF p t y) starNu := by
  rw [starNu, integrable_prod_iff (measurable_innerF p t y).aestronglyMeasurable]
  refine ⟨Eventually.of_forall fun s => innerF_slice_integrable, ?_⟩
  refine Integrable.mono' (gStar_integrable hp) ?_ ?_
  · exact ((measurable_innerF p t y).norm.aestronglyMeasurable
      (μ := (volume.restrict (Ioc (0 : ℝ) 1)).prod angMeas)).integral_prod_right'
  · filter_upwards [ae_restrict_mem measurableSet_Ioc] with s hs
    rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]
    exact innerF_slice_norm_le hp hs hy0 hyt

theorem innerF_norm_le {p t y : ℝ} (hp : 0 < p) (ht : t ≤ 1) (hy0 : 0 ≤ y) (hyt : y ≤ hallBeta p t) :
    ∫ a, ‖innerF p t y a‖ ∂starNu ≤ ∫ s in Ioc (0 : ℝ) 1, gStar p s := by
  rw [starNu, integral_prod _ (innerF_integrable hp ht hy0 hyt).norm]
  apply integral_mono_ae _ (gStar_integrable hp)
  · filter_upwards [ae_restrict_mem measurableSet_Ioc] with s hs
    exact innerF_slice_norm_le hp hs hy0 hyt
  · exact (innerF_integrable hp ht hy0 hyt).norm.integral_prod_left

/-- `∫₀^t (log c − p log s) ds = t log c − p (t log t − t)`. -/
theorem integral_log_beta {p t : ℝ} (hp : 0 < p) (ht : 0 < t) :
    ∫ s in (0 : ℝ)..t, Real.log (hallBeta p s / 4) = t * Real.log (hallC p) - p * (t * Real.log t - t) := by
  rw [integral_congr_ae (g := fun s => Real.log (hallC p) - p * Real.log s) (Eventually.of_forall
    fun s hs => by rw [uIoc_of_le ht.le] at hs; exact log_hallBeta_div_four hp hs.1)]
  rw [integral_sub intervalIntegrable_const (intervalIntegral.intervalIntegrable_log'.const_mul p),
    intervalIntegral.integral_const, intervalIntegral.integral_const_mul, integral_log]
  simp

theorem innerF_integral {p t y : ℝ} (hp : 0 < p) (ht0 : 0 < t) (ht : t ≤ 1) (hy0 : 0 ≤ y)
    (hyt : y ≤ hallBeta p t) :
    ∫ a, innerF p t y a ∂starNu = t * Real.log (hallC p) - p * (t * Real.log t - t) := by
  rw [starNu, integral_prod _ (innerF_integrable hp ht hy0 hyt)]
  have hslice : ∀ s ∈ Ioc (0 : ℝ) 1, ∫ φ, innerF p t y (s, φ) ∂angMeas =
      (Iio t).indicator (fun s => Real.log (hallBeta p s / 4)) s := by
    intro s hs
    by_cases hst : s < t
    · simp_rw [innerF_slice_lt hst, Set.indicator_of_mem (show s ∈ Iio t from hst)]
      exact inner_eq (hallBeta_pos hp hs.1) hy0 (hyt.trans (hallBeta_anti hp hs.1 hst.le))
    · simp_rw [innerF_slice_ge hst, Set.indicator_of_notMem (show s ∉ Iio t from hst), integral_zero]
  have hset : Ioc (0 : ℝ) 1 ∩ Iio t = Ioo 0 t := by
    ext s; simp only [mem_inter_iff, mem_Ioc, mem_Iio, mem_Ioo]; constructor
    · rintro ⟨⟨h1, _⟩, h3⟩; exact ⟨h1, h3⟩
    · rintro ⟨h1, h3⟩; exact ⟨⟨h1, by linarith⟩, h3⟩
  rw [setIntegral_congr_fun measurableSet_Ioc hslice, setIntegral_indicator measurableSet_Iio,
    hset, ← integral_Ioc_eq_integral_Ioo, ← intervalIntegral.integral_of_le ht0.le,
    integral_log_beta hp ht0]

/-! ### The double integral -/

/-- The kernel in parameter coordinates. -/
noncomputable def Hstar (p : ℝ) (z : (ℝ × ℝ) × (ℝ × ℝ)) : ℝ := Real.log (starX p z.1 - starX p z.2)

/-- The part `s < t`. -/
noncomputable def HstarLt (p : ℝ) : (ℝ × ℝ) × (ℝ × ℝ) → ℝ :=
  {z : (ℝ × ℝ) × (ℝ × ℝ) | z.1.1 < z.2.1}.indicator (Hstar p)

theorem measurable_Hstar (p : ℝ) : Measurable (Hstar p) := measurable_logX p

theorem measurable_HstarLt (p : ℝ) : Measurable (HstarLt p) :=
  (measurable_Hstar p).indicator (measurableSet_lt (measurable_fst.comp measurable_fst)
    (measurable_fst.comp measurable_snd))

theorem HstarLt_slice (p : ℝ) (a b : ℝ × ℝ) : HstarLt p (a, b) = innerF p b.1 (starX p b) a := by
  simp [HstarLt, innerF, Hstar, indicator]

theorem HstarLt_integrable {p : ℝ} (hp : 0 < p) : Integrable (HstarLt p) (starNu.prod starNu) := by
  rw [integrable_prod_iff' (measurable_HstarLt p).aestronglyMeasurable]
  constructor
  · filter_upwards [starNu_ae_mem] with b hb
    simp_rw [HstarLt_slice]
    exact innerF_integrable hp hb.1.2 (starX_mem hp hb.1).1 (starX_mem hp hb.1).2
  · refine Integrable.mono' (integrable_const (∫ s in Ioc (0 : ℝ) 1, gStar p s)) ?_ ?_
    · exact (measurable_HstarLt p).norm.stronglyMeasurable.integral_prod_left.aestronglyMeasurable
    · filter_upwards [starNu_ae_mem] with b hb
      simp_rw [HstarLt_slice]
      rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]
      exact innerF_norm_le hp hb.1.2 (starX_mem hp hb.1).1 (starX_mem hp hb.1).2

/-- `∫₀¹ t log t dt = −1/4`. -/
theorem integral_mul_log_zero_one : ∫ t in (0 : ℝ)..1, t * Real.log t = -1 / 4 := by
  have hcont : ContinuousOn (fun t : ℝ => t / 2 * (t * Real.log t) - t ^ 2 / 4) (Icc 0 1) :=
    ((continuous_id.div_const 2).mul Real.continuous_mul_log |>.sub (by fun_prop)).continuousOn
  have hder : ∀ t ∈ Ioo (0 : ℝ) 1, HasDerivAt (fun t : ℝ => t / 2 * (t * Real.log t) - t ^ 2 / 4)
      (t * Real.log t) t := by
    intro t ht
    have h1 := ((hasDerivAt_id' t).div_const 2).mul (Real.hasDerivAt_mul_log ht.1.ne')
    have h2 := (hasDerivAt_pow 2 t).div_const 4
    convert h1.sub h2 using 1
    push_cast; ring
  rw [integral_eq_sub_of_hasDerivAt_of_le zero_le_one hcont hder
    (Real.continuous_mul_log.intervalIntegrable 0 1)]
  simp; norm_num

theorem HstarLt_integral {p : ℝ} (hp : 0 < p) :
    ∫ z, HstarLt p z ∂(starNu.prod starNu) = hallKappa p / 2 := by
  rw [integral_prod_symm _ (HstarLt_integrable hp)]
  have hb : ∀ᵐ b ∂starNu, ∫ a, HstarLt p (a, b) ∂starNu =
      b.1 * Real.log (hallC p) - p * (b.1 * Real.log b.1 - b.1) := by
    filter_upwards [starNu_ae_mem] with b hb
    simp_rw [HstarLt_slice]
    exact innerF_integral hp hb.1.1 hb.1.2 (starX_mem hp hb.1).1 (starX_mem hp hb.1).2
  rw [integral_congr_ae hb, starNu, integral_fun_fst (fun t => t * Real.log (hallC p) - p * (t * Real.log t - t))]
  simp only [probReal_univ, one_smul]
  rw [← intervalIntegral.integral_of_le zero_le_one]
  have i1 : IntervalIntegrable (fun t : ℝ => t * Real.log (hallC p)) volume 0 1 := by
    apply Continuous.intervalIntegrable; fun_prop
  have i2 : IntervalIntegrable (fun t : ℝ => p * (t * Real.log t - t)) volume 0 1 :=
    (continuous_const.mul (Real.continuous_mul_log.sub continuous_id')).intervalIntegrable 0 1
  rw [integral_sub i1 i2, intervalIntegral.integral_mul_const, intervalIntegral.integral_const_mul,
    integral_sub (Real.continuous_mul_log.intervalIntegrable 0 1) (continuous_id'.intervalIntegrable 0 1),
    integral_mul_log_zero_one, integral_id, hallKappa]
  ring

/-! ### Symmetry and the full integral -/

theorem Hstar_swap (p : ℝ) (z : (ℝ × ℝ) × (ℝ × ℝ)) : Hstar p z.swap = Hstar p z := by
  simp only [Hstar, Prod.fst_swap, Prod.snd_swap]
  rw [← Real.log_neg_eq_log, neg_sub]

/-- The diagonal `s = t` is null. -/
theorem starNu_diag_null : (starNu.prod starNu) {z | z.1.1 = z.2.1} = 0 := by
  have hm : MeasurableSet {z : (ℝ × ℝ) × (ℝ × ℝ) | z.1.1 = z.2.1} :=
    measurableSet_eq_fun (measurable_fst.comp measurable_fst) (measurable_fst.comp measurable_snd)
  have hs : ∀ a : ℝ × ℝ, starNu (Prod.mk a ⁻¹' {z : (ℝ × ℝ) × (ℝ × ℝ) | z.1.1 = z.2.1}) = 0 := by
    intro a
    have : Prod.mk a ⁻¹' {z : (ℝ × ℝ) × (ℝ × ℝ) | z.1.1 = z.2.1} = {a.1} ×ˢ univ := by
      ext b; simp [eq_comm]
    rw [this, starNu, Measure.prod_prod]
    simp
  rw [Measure.prod_apply hm]
  simp_rw [hs]
  simp

theorem Hstar_ae_eq {p : ℝ} : Hstar p =ᵐ[starNu.prod starNu] fun z => HstarLt p z + HstarLt p z.swap := by
  filter_upwards [measure_eq_zero_iff_ae_notMem.1 starNu_diag_null] with z hz
  replace hz : z.1.1 ≠ z.2.1 := hz
  rcases lt_or_gt_of_ne hz with h | h
  · have h' : ¬ z.2.1 < z.1.1 := not_lt.2 h.le
    simp [HstarLt, indicator, h, h']
  · have h' : ¬ z.1.1 < z.2.1 := not_lt.2 h.le
    simp [HstarLt, indicator, h, h', Hstar_swap]

theorem Hstar_integrable {p : ℝ} (hp : 0 < p) : Integrable (Hstar p) (starNu.prod starNu) := by
  have hi2 : Integrable (fun z => HstarLt p z.swap) (starNu.prod starNu) := (HstarLt_integrable hp).swap
  exact ((HstarLt_integrable hp).add hi2).congr Hstar_ae_eq.symm

theorem Hstar_integral {p : ℝ} (hp : 0 < p) : ∫ z, Hstar p z ∂(starNu.prod starNu) = hallKappa p := by
  have hi2 : Integrable (fun z => HstarLt p z.swap) (starNu.prod starNu) := (HstarLt_integrable hp).swap
  rw [integral_congr_ae Hstar_ae_eq, integral_add (HstarLt_integrable hp) hi2]
  have := integral_prod_swap (μ := starNu) (ν := starNu) (HstarLt p)
  rw [this, HstarLt_integral hp]
  ring

/-! ### Transport to `μ*_u` -/

theorem muStar_prod (p : ℝ) : (muStar p).prod (muStar p) =
    (starNu.prod starNu).map (Prod.map (starU p) (starU p)) :=
  Measure.map_prod_map _ _ (measurable_starU p) (measurable_starU p)

theorem Fp_starU_ae {p : ℝ} (hp : 0 < p) :
    (fun z : (ℝ × ℝ) × (ℝ × ℝ) => Fp p (starU p z.1) (starU p z.2)) =ᵐ[starNu.prod starNu] Hstar p := by
  have g1 := (Measure.quasiMeasurePreserving_fst (μ := starNu) (ν := starNu)).ae (starX_pos_ae hp)
  have g2 := (Measure.quasiMeasurePreserving_snd (μ := starNu) (ν := starNu)).ae (starX_pos_ae hp)
  filter_upwards [g1, g2] with z h1 h2
  have e : ∀ X : ℝ, 0 < X → (X ^ (-(1 / p))) ^ (-p) = X := fun X hX => by
    rw [← rpow_mul hX.le, show -(1 / p) * -p = 1 by field_simp, rpow_one]
  simp only [Fp, starU, Hstar, e _ h1, e _ h2, Real.log_abs]

/-- `F_p` is `μ*_u ⊗ μ*_u`-integrable (Paper 1, proof of Theorem 1.3(iii): `𝓛(μ*)` converges absolutely). -/
theorem muStar_energy_integrable {p : ℝ} (hp : 0 < p) :
    Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) ((muStar p).prod (muStar p)) := by
  rw [muStar_prod, integrable_map_measure (measurable_Fp p).aestronglyMeasurable
    ((measurable_starU p).prodMap (measurable_starU p)).aemeasurable]
  exact (Hstar_integrable hp).congr (Fp_starU_ae hp).symm

/-- **The value** (Paper 1 Theorem 1.3(iii)): `𝒥_p(μ*_u) = κ_p`. -/
theorem muStar_energy {p : ℝ} (hp : 0 < p) : Jp p (muStar p) = hallKappa p := by
  rw [Jp, muStar_prod, integral_map ((measurable_starU p).prodMap (measurable_starU p)).aemeasurable
    (measurable_Fp p).aestronglyMeasurable]
  simp only [Prod.map_fst, Prod.map_snd]
  rw [integral_congr_ae (Fp_starU_ae hp), Hstar_integral hp]

end JacobiAsym
