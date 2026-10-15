import JacobiAsym.HallLower
import JacobiAsym.EnergyPos

/-! # Plan 60, stages S2c + S4b: the potential of μ* and optimality (Paper 1 Theorem 1.3(ii), (iii) optimality)

* `le_volume_of_lip`: a probability measure with `μ(a, b] ≤ b − a` satisfies `μ ≤ Leb` (Stieltjes:
  `Leb = F_μ.measure + (id − F_μ).measure`).
* `starPot_eq`, `starPot_ge`: `U*(x) = ∫ log |x − y| dμ*(y) = log c + p` for `0 ≤ x ≤ 4c`, `≥` for `x ≥ 0`.
* **`Jp_le_kappa`**: `𝒥_p(μ) ≤ κ_p` for admissible `μ` with bounded support and `F_p` integrable. -/

open Real Set MeasureTheory Filter Topology
open scoped ENNReal

namespace JacobiAsym

/-! ### Interval bounds give `μ ≤ Leb` -/

theorem le_volume_of_lip {μ : Measure ℝ} [IsProbabilityMeasure μ]
    (hlip : ∀ a b, a ≤ b → μ (Ioc a b) ≤ ENNReal.ofReal (b - a)) : μ ≤ volume := by
  set F := ProbabilityTheory.cdf μ
  have hinc : ∀ a b, a ≤ b → F b - F a ≤ b - a := by
    intro a b hab
    rw [ProbabilityTheory.cdf_eq_real, ProbabilityTheory.cdf_eq_real, measureReal_def, measureReal_def,
      ← Iic_union_Ioc_eq_Iic hab, measure_union (Iic_disjoint_Ioc le_rfl) measurableSet_Ioc,
      ENNReal.toReal_add (measure_ne_top _ _) (measure_ne_top _ _), add_sub_cancel_left]
    exact ENNReal.toReal_le_of_le_ofReal (by linarith) (hlip a b hab)
  let h : StieltjesFunction ℝ :=
    { toFun := fun x => x - F x
      mono' := fun a b hab => by have := hinc a b hab; simp only; linarith
      right_continuous' := fun x => (continuousWithinAt_id).sub (F.right_continuous x) }
  have hid : F + h = StieltjesFunction.id := by
    ext x; simp [h]
  rw [Real.volume_eq_stieltjes_id, ← hid, StieltjesFunction.measure_add, ProbabilityTheory.measure_cdf]
  exact Measure.le_add_right le_rfl

/-! ### Atoms and diagonals for two measures -/

theorem diag_null2 {P Q : Measure ℝ} [SFinite Q] (hQ : ∀ x, Q {x} = 0) :
    (P.prod Q) {z : ℝ × ℝ | z.1 = z.2} = 0 := by
  rw [Measure.prod_apply (measurableSet_eq_fun measurable_fst measurable_snd)]
  have : ∀ x : ℝ, Prod.mk x ⁻¹' {z : ℝ × ℝ | z.1 = z.2} = {x} := fun x => by ext y; simp [eq_comm]
  simp_rw [this, hQ]
  simp

/-! ### The potential `U*` -/

/-- `U*(x) = ∫ log |X b − x| dν*(b)` (= `∫ log |x − y| dμ*(y)`). -/
noncomputable def starPot (p x : ℝ) : ℝ := ∫ b, Real.log (starX p b - x) ∂starNu

/-- `∫ log (arcX β φ − x) dφ/π ≥ log (β/4)` for every `x ≥ 0`. -/
theorem inner_ge {β x : ℝ} (hβ : 0 < β) (hx : 0 ≤ x) :
    Real.log (β / 4) ≤ ∫ φ, Real.log (arcX β φ - x) ∂angMeas := by
  rcases le_or_gt x β with h | h
  · rw [inner_eq hβ hx h]
  · rw [integral_angMeas]
    have := arcsine_pot_ge hβ h.le
    rw [le_inv_mul_iff₀ pi_pos]; linarith

/-- `∫ |log |arcX β φ − x|| dφ/π ≤ 2 log (1 + x + β) − log (β/4)` for every `x ≥ 0`. -/
theorem inner_abs_le' {β x : ℝ} (hβ : 0 < β) (hx : 0 ≤ x) :
    ∫ φ, |Real.log (arcX β φ - x)| ∂angMeas ≤ 2 * Real.log (1 + x + β) - Real.log (β / 4) := by
  have hint : Integrable (fun φ => Real.log (arcX β φ - x)) angMeas :=
    integrable_angMeas (intervalIntegrable_log_arcX_sub β x 0 π)
  set M := Real.log (1 + x + β)
  have hM : 0 ≤ M := Real.log_nonneg (by linarith)
  have hpt : ∀ φ, |Real.log (arcX β φ - x)| ≤ 2 * M - Real.log (arcX β φ - x) := by
    intro φ
    have h1 : Real.log (arcX β φ - x) ≤ M := by
      refine (log_le_log_one_add_abs _).trans (Real.log_le_log (by positivity) ?_)
      have := arcX_nonneg hβ.le φ; have := arcX_le hβ.le φ
      have : |arcX β φ - x| ≤ x + β := abs_le.2 ⟨by linarith, by linarith⟩
      linarith
    rcases le_or_gt 0 (Real.log (arcX β φ - x)) with h | h
    · rw [abs_of_nonneg h]; linarith
    · rw [abs_of_neg h]; linarith
  calc ∫ φ, |Real.log (arcX β φ - x)| ∂angMeas ≤ ∫ φ, (2 * M - Real.log (arcX β φ - x)) ∂angMeas :=
        integral_mono hint.abs ((integrable_const _).sub hint) hpt
    _ = 2 * M - ∫ φ, Real.log (arcX β φ - x) ∂angMeas := by
        rw [integral_sub (integrable_const _) hint, integral_const]; simp
    _ ≤ _ := by have := inner_ge hβ hx; linarith

theorem log_one_add_add_le {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    Real.log (1 + x + y) ≤ Real.log (1 + x) + Real.log (1 + y) := by
  rw [← Real.log_mul (by positivity) (by positivity)]
  exact Real.log_le_log (by positivity) (by nlinarith)

/-- The constant `C_g = ∫₀¹ g`. -/
noncomputable def gConst (p : ℝ) : ℝ := ∫ s in Ioc (0 : ℝ) 1, gStar p s

theorem potF_measurable (p x : ℝ) : Measurable (fun b : ℝ × ℝ => Real.log (starX p b - x)) :=
  ((measurable_starX p).sub measurable_const).log

theorem starX_mk (p s φ : ℝ) : starX p (s, φ) = arcX (hallBeta p s) φ := rfl

theorem potF_slice (p x s : ℝ) : Integrable (fun φ => Real.log (starX p (s, φ) - x)) angMeas := by
  simp only [starX_mk]
  exact integrable_angMeas (intervalIntegrable_log_arcX_sub (hallBeta p s) x 0 π)

theorem potF_integrable {p x : ℝ} (hp : 0 < p) (hx : 0 ≤ x) :
    Integrable (fun b => Real.log (starX p b - x)) starNu ∧
      ∫ b, |Real.log (starX p b - x)| ∂starNu ≤ 2 * Real.log (1 + x) + gConst p := by
  have hbd : ∀ s ∈ Ioc (0 : ℝ) 1, ∫ φ, ‖Real.log (starX p (s, φ) - x)‖ ∂angMeas ≤
      2 * Real.log (1 + x) + gStar p s := by
    intro s hs
    have hβ := hallBeta_pos hp hs.1
    simp_rw [Real.norm_eq_abs]
    refine (inner_abs_le' hβ hx).trans ?_
    have := log_one_add_add_le hx hβ.le
    unfold gStar; linarith
  have hgi : IntegrableOn (fun s => 2 * Real.log (1 + x) + gStar p s) (Ioc 0 1) :=
    (integrable_const _).add (gStar_integrable hp)
  have hI : Integrable (fun b => Real.log (starX p b - x)) starNu := by
    rw [starNu, integrable_prod_iff (potF_measurable p x).aestronglyMeasurable]
    refine ⟨Eventually.of_forall fun s => potF_slice p x s, ?_⟩
    refine Integrable.mono' hgi ?_ ?_
    · exact ((potF_measurable p x).norm.aestronglyMeasurable
        (μ := (volume.restrict (Ioc (0 : ℝ) 1)).prod angMeas)).integral_prod_right'
    · filter_upwards [ae_restrict_mem measurableSet_Ioc] with s hs
      rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]
      exact hbd s hs
  refine ⟨hI, ?_⟩
  have := integral_prod _ (show Integrable (fun b => ‖Real.log (starX p b - x)‖)
    ((volume.restrict (Ioc (0 : ℝ) 1)).prod angMeas) from hI.norm)
  simp_rw [Real.norm_eq_abs] at this
  rw [starNu, this]
  calc ∫ s in Ioc (0 : ℝ) 1, ∫ φ, |Real.log (starX p (s, φ) - x)| ∂angMeas
      ≤ ∫ s in Ioc (0 : ℝ) 1, (2 * Real.log (1 + x) + gStar p s) := by
        apply setIntegral_mono_on _ hgi measurableSet_Ioc
        · intro s hs; have := hbd s hs; simpa [Real.norm_eq_abs] using this
        · exact (hI.norm.integral_prod_left).congr (Eventually.of_forall fun s => by simp [Real.norm_eq_abs])
    _ = 2 * Real.log (1 + x) + gConst p := by
        rw [integral_add (integrable_const _) (gStar_integrable hp), setIntegral_const]
        simp [gConst]

/-- `∫₀¹ log (β_t/4) dt = log c + p`. -/
theorem integral_log_beta_one {p : ℝ} (hp : 0 < p) :
    ∫ s in Ioc (0 : ℝ) 1, Real.log (hallBeta p s / 4) = Real.log (hallC p) + p := by
  rw [← intervalIntegral.integral_of_le zero_le_one, integral_log_beta hp one_pos]; simp

/-- **Theorem 1.3(ii)**, `≥`: `U*(x) ≥ log c + p` for `x ≥ 0`. -/
theorem starPot_ge {p x : ℝ} (hp : 0 < p) (hx : 0 ≤ x) : Real.log (hallC p) + p ≤ starPot p x := by
  have hI := (potF_integrable hp hx).1
  rw [starPot, starNu, integral_prod _ hI, ← integral_log_beta_one hp]
  apply setIntegral_mono_on _ hI.integral_prod_left measurableSet_Ioc
  · intro s hs; exact inner_ge (hallBeta_pos hp hs.1) hx
  · refine Integrable.mono' (gStar_integrable hp)
      ((measurable_hallBeta p).div_const 4).log.aestronglyMeasurable ?_
    filter_upwards [ae_restrict_mem measurableSet_Ioc] with s hs
    have hβ := hallBeta_pos hp hs.1
    rw [Real.norm_eq_abs, gStar]
    have h1 : Real.log (hallBeta p s / 4) ≤ Real.log (1 + hallBeta p s) := Real.log_le_log (by positivity)
      (by linarith)
    have h2 : 0 ≤ Real.log (1 + hallBeta p s) := Real.log_nonneg (by linarith)
    rw [abs_le]; constructor <;> linarith

/-- **Theorem 1.3(ii)**, `=`: `U*(x) = log c + p` for `0 ≤ x ≤ 4c`. -/
theorem starPot_eq {p x : ℝ} (hp : 0 < p) (hx : 0 ≤ x) (hx4 : x ≤ 4 * hallC p) :
    starPot p x = Real.log (hallC p) + p := by
  have hI := (potF_integrable hp hx).1
  rw [starPot, starNu, integral_prod _ hI, ← integral_log_beta_one hp]
  apply setIntegral_congr_fun measurableSet_Ioc
  intro s hs
  have hβ := hallBeta_pos hp hs.1
  have : x ≤ hallBeta p s := hx4.trans (by rw [← hallBeta_one]; exact hallBeta_anti hp hs.1 hs.2)
  exact inner_eq hβ hx this

/-! ### `μ*_u` on `(0, u_s]` is Lebesgue measure -/

theorem muStar_Ioc_le_all {p : ℝ} (hp : 0 < p) (a b : ℝ) (hab : a ≤ b) :
    muStar p (Ioc a b) ≤ ENNReal.ofReal (b - a) :=
  Ioc_le_of_lip (muStar_Iic_zero hp) (fun _ _ ha hab => muStar_Ioc_le hp ha hab) hab

theorem muStar_le_volume {p : ℝ} (hp : 0 < p) : muStar p ≤ volume :=
  le_volume_of_lip (muStar_Ioc_le_all hp)

theorem muStar_Ioc_zero_us {p : ℝ} (hp : 0 < p) :
    muStar p (Ioc 0 (hallLam p / π)) = ENNReal.ofReal (hallLam p / π) := by
  set us := hallLam p / π
  have hus : 0 < us := div_pos (hallLam_pos hp) pi_pos
  apply le_antisymm (by simpa using muStar_Ioc_le_all hp 0 us hus.le)
  have hseq : ∀ k : ℕ, ENNReal.ofReal (us - us / (k + 2)) ≤ muStar p (Ioc 0 us) := by
    intro k
    have hpos : 0 < us / (k + 2) := by positivity
    have hle : us / (k + 2) ≤ us := div_le_self hus.le (by linarith [(Nat.cast_nonneg k : (0:ℝ) ≤ k)])
    rw [← muStar_Ioc_eq hp hpos hle le_rfl]
    exact measure_mono (Set.Ioc_subset_Ioc_left hpos.le)
  have hlim : Tendsto (fun k : ℕ => ENNReal.ofReal (us - us / (k + 2))) atTop (𝓝 (ENNReal.ofReal us)) := by
    apply ENNReal.tendsto_ofReal
    have : Tendsto (fun k : ℕ => us / ((k : ℝ) + 2)) atTop (𝓝 0) :=
      tendsto_const_nhds.div_atTop (tendsto_atTop_add_const_right _ 2 tendsto_natCast_atTop_atTop)
    simpa using tendsto_const_nhds.sub this
  exact le_of_tendsto' hlim hseq

theorem muStar_restrict_us {p : ℝ} (hp : 0 < p) :
    (muStar p).restrict (Ioc 0 (hallLam p / π)) = volume.restrict (Ioc 0 (hallLam p / π)) := by
  apply Measure.eq_of_le_of_measure_univ_eq (Measure.restrict_mono le_rfl (muStar_le_volume hp))
  rw [Measure.restrict_apply MeasurableSet.univ, Measure.restrict_apply MeasurableSet.univ]
  simp only [univ_inter]
  rw [muStar_Ioc_zero_us hp, Real.volume_Ioc, sub_zero]

/-! ### The x-variable measures -/

/-- `u ↦ u^{-p}`. -/
noncomputable def gmap (p : ℝ) (u : ℝ) : ℝ := u ^ (-p)

theorem measurable_gmap (p : ℝ) : Measurable (gmap p) := by unfold gmap; fun_prop

/-- `μ* = ∫ ω_{β_t} dt` in the x-variable. -/
noncomputable def Bstar (p : ℝ) : Measure ℝ := starNu.map (starX p)

instance Bstar_prob (p : ℝ) : IsProbabilityMeasure (Bstar p) := by unfold Bstar; infer_instance

theorem Bstar_singleton {p : ℝ} (hp : 0 < p) (x : ℝ) : Bstar p {x} = 0 := by
  rw [Bstar, Measure.map_apply (measurable_starX p) (measurableSet_singleton x)]
  have hnull : starNu {b | ¬ 0 < starX p b} = 0 := by
    rw [← ae_iff]; exact starX_pos_ae hp
  apply measure_mono_null (t := starU p ⁻¹' {x ^ (-(1 / p))} ∪ {b | ¬ 0 < starX p b})
  · intro b hb
    simp only [mem_preimage, mem_singleton_iff] at hb
    by_cases hX : 0 < starX p b
    · left; simp [starU, hb]
    · right; exact hX
  · apply measure_union_null _ hnull
    rw [← Measure.map_apply (measurable_starU p) (measurableSet_singleton _)]
    exact muStar_singleton hp _

theorem Amap_singleton {p U : ℝ} (hp : 0 < p) {μ : Measure ℝ} (h : AdmissibleOn U μ) (x : ℝ) :
    μ.map (gmap p) {x} = 0 := by
  rw [Measure.map_apply (measurable_gmap p) (measurableSet_singleton x)]
  apply measure_mono_null (t := {x ^ (-(1 / p))} ∪ Iic 0)
  · intro u hu
    simp only [mem_preimage, mem_singleton_iff, gmap] at hu
    by_cases hu0 : 0 < u
    · left
      rw [mem_singleton_iff, ← hu, ← rpow_mul hu0.le, show -p * -(1 / p) = 1 by field_simp, rpow_one]
    · right; exact not_lt.1 hu0
  · exact measure_union_null (measure_singleton_of_lip h.le_zero h.lip _) h.le_zero

/-! ### Integrability of the potential -/

theorem measurable_starPot (p : ℝ) : Measurable (starPot p) := by
  have hm : Measurable (fun z : ℝ × (ℝ × ℝ) => Real.log (starX p z.2 - z.1)) :=
    (((measurable_starX p).comp measurable_snd).sub measurable_fst).log
  exact (hm.stronglyMeasurable.integral_prod_right (ν := starNu)).measurable

theorem log_one_add_rpow_le {p u : ℝ} (hp : 0 < p) (hu : 0 < u) :
    Real.log (1 + u ^ (-p)) ≤ Real.log 2 + p * |Real.log u| := by
  rcases le_or_gt u 1 with h1 | h1
  · have hge : 1 ≤ u ^ (-p) := one_le_rpow_of_pos_of_le_one_of_nonpos hu h1 (by linarith)
    calc Real.log (1 + u ^ (-p)) ≤ Real.log (2 * u ^ (-p)) := Real.log_le_log (by positivity) (by linarith)
      _ = Real.log 2 + p * |Real.log u| := by
          rw [Real.log_mul (by norm_num) (by positivity), Real.log_rpow hu,
            abs_of_nonpos (Real.log_nonpos hu.le h1)]; ring
  · have hle : u ^ (-p) ≤ 1 := rpow_le_one_of_one_le_of_nonpos h1.le (by linarith)
    have : Real.log (1 + u ^ (-p)) ≤ Real.log 2 := Real.log_le_log (by positivity) (by linarith)
    have := abs_nonneg (Real.log u)
    nlinarith

theorem AdmissibleOn.le_volume {U : ℝ} {μ : Measure ℝ} (h : AdmissibleOn U μ) : μ ≤ volume := by
  have := h.prob
  exact le_volume_of_lip (fun a b hab => h.Ioc_le hab)

theorem AdmissibleOn.restrict_eq {U : ℝ} {μ : Measure ℝ} (h : AdmissibleOn U μ) :
    μ.restrict (Ioc 0 U) = μ := by
  apply Measure.restrict_eq_self_of_ae_mem
  rw [ae_iff]
  have : {a : ℝ | a ∉ Ioc 0 U} ⊆ Iic 0 ∪ Ioi U := by
    intro a ha
    simp only [mem_ofPred_eq, Set.mem_Ioc, not_and_or, not_lt, not_le] at ha
    rcases ha with ha | ha
    · exact Or.inl ha
    · exact Or.inr ha
  exact measure_mono_null this (measure_union_null h.le_zero h.gt_U)

theorem AdmissibleOn.ae_pos {U : ℝ} {μ : Measure ℝ} (h : AdmissibleOn U μ) : ∀ᵐ u ∂μ, 0 < u := by
  rw [ae_iff]
  have : {a : ℝ | ¬ 0 < a} = Iic 0 := by ext a; simp
  rw [this]; exact h.le_zero

/-- A bound integrable against every admissible `μ`. -/
theorem AdmissibleOn.integrable_logbound {U : ℝ} {μ : Measure ℝ} (h : AdmissibleOn U μ) (p C : ℝ) :
    Integrable (fun u => 2 * (Real.log 2 + p * |Real.log u|) + C) μ := by
  have := h.prob
  have hv : Integrable (fun u => 2 * (Real.log 2 + p * |Real.log u|) + C) (volume.restrict (Ioc 0 U)) := by
    have hl : IntegrableOn (fun u : ℝ => |Real.log u|) (Ioc 0 U) := by
      rcases le_or_gt 0 U with hU | hU
      · have := (intervalIntegral.intervalIntegrable_log' (a := 0) (b := U)).1.abs
        exact this
      · rw [Ioc_eq_empty (not_lt.2 hU.le)]; exact integrableOn_empty
    exact (((integrable_const _).add (hl.const_mul p)).const_mul 2).add (integrable_const _)
  rw [← h.restrict_eq]
  exact hv.mono_measure (Measure.restrict_mono le_rfl h.le_volume)

theorem cross_integrable {p U : ℝ} (hp : 0 < p) {μ : Measure ℝ} (h : AdmissibleOn U μ) :
    Integrable (fun z : ℝ × (ℝ × ℝ) => Real.log (starX p z.2 - gmap p z.1)) (μ.prod starNu) := by
  have := h.prob
  have hm : Measurable (fun z : ℝ × (ℝ × ℝ) => Real.log (starX p z.2 - gmap p z.1)) :=
    (((measurable_starX p).comp measurable_snd).sub ((measurable_gmap p).comp measurable_fst)).log
  rw [integrable_prod_iff hm.aestronglyMeasurable]
  constructor
  · filter_upwards [h.ae_pos] with u hu
    exact (potF_integrable hp (rpow_nonneg hu.le _)).1
  · refine Integrable.mono' (h.integrable_logbound p (gConst p)) hm.norm.stronglyMeasurable.integral_prod_right'.aestronglyMeasurable ?_
    filter_upwards [h.ae_pos] with u hu
    rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]
    simp_rw [Real.norm_eq_abs]
    have h1 := (potF_integrable hp (rpow_nonneg hu.le (-p))).2
    have h2 := log_one_add_rpow_le hp hu
    unfold gmap; linarith

theorem integral_cross {p U : ℝ} (hp : 0 < p) {μ : Measure ℝ} (h : AdmissibleOn U μ) :
    ∫ z, Real.log (starX p z.2 - gmap p z.1) ∂(μ.prod starNu) = ∫ u, starPot p (gmap p u) ∂μ := by
  have := h.prob
  rw [integral_prod _ (cross_integrable hp h)]; rfl

/-- `∫ U*(u^{-p}) dμ*_u(u) = κ_p`. -/
theorem starPot_muStar {p : ℝ} (hp : 0 < p) :
    Integrable (fun u => starPot p (gmap p u)) (muStar p) ∧
      ∫ u, starPot p (gmap p u) ∂(muStar p) = hallKappa p := by
  have hae : (fun a => starPot p (gmap p (starU p a))) =ᵐ[starNu] fun a => ∫ b, Hstar p (b, a) ∂starNu := by
    filter_upwards [starX_pos_ae hp] with a ha
    rw [starPot, gmap, starU, ← rpow_mul ha.le, show -(1 / p) * -p = 1 by field_simp, rpow_one]
    rfl
  have hI : Integrable (fun a => ∫ b, Hstar p (b, a) ∂starNu) starNu := (Hstar_integrable hp).integral_prod_right
  have hmeas : AEStronglyMeasurable (fun u => starPot p (gmap p u)) (muStar p) :=
    ((measurable_starPot p).comp (measurable_gmap p)).aestronglyMeasurable
  constructor
  · rw [muStar, integrable_map_measure (by rw [← muStar]; exact hmeas) (measurable_starU p).aemeasurable]
    exact hI.congr hae.symm
  · rw [muStar, integral_map (measurable_starU p).aemeasurable (by rw [← muStar]; exact hmeas),
      integral_congr_ae hae, ← integral_prod_symm _ (Hstar_integrable hp), Hstar_integral hp]

/-- **The comparison step** of Theorem 1.3(iii): `∫ U*(u^{-p}) dμ ≤ κ_p` for admissible `μ`. -/
theorem starPot_compare {p U : ℝ} (hp : 0 < p) {μ : Measure ℝ} (h : AdmissibleOn U μ)
    (hIμ : Integrable (fun u => starPot p (gmap p u)) μ) :
    ∫ u, starPot p (gmap p u) ∂μ ≤ hallKappa p := by
  have := h.prob
  obtain ⟨hIs, hVs⟩ := starPot_muStar hp
  set K0 := Real.log (hallC p) + p
  set us := hallLam p / π
  set W : ℝ → ℝ := fun u => starPot p (gmap p u) - K0
  set I := Ioo (0 : ℝ) us
  have hus : (4 * hallC p) ^ (-(1 / p)) = us := four_hallC_rpow_neg hp
  have hW0 : ∀ u, 0 < u → 0 ≤ W u := fun u hu => by
    have := starPot_ge hp (show 0 ≤ gmap p u from rpow_nonneg hu.le _)
    simp only [W]; linarith
  have hWz : ∀ u, us ≤ u → W u = 0 := by
    intro u hu
    have husp : 0 < us := div_pos (hallLam_pos hp) pi_pos
    have hc := hallC_pos hp
    have hle : gmap p u ≤ 4 * hallC p := by
      unfold gmap
      have := rpow_le_rpow_of_nonpos husp hu (by linarith : -p ≤ 0)
      rw [← hus, ← rpow_mul (by positivity), show -(1 / p) * -p = 1 by field_simp, rpow_one] at this
      exact this
    have := starPot_eq hp (show 0 ≤ gmap p u from rpow_nonneg (husp.le.trans hu) _) hle
    simp only [W]; rw [this]; ring
  have hWμ : Integrable W μ := hIμ.sub (integrable_const _)
  have hWs : Integrable W (muStar p) := hIs.sub (integrable_const _)
  -- Step 1: `∫ W dμ = ∫_I W dμ`
  have s1 : ∫ u, W u ∂μ = ∫ u in I, W u ∂μ := by
    rw [← integral_indicator measurableSet_Ioo]
    apply integral_congr_ae
    filter_upwards [h.ae_pos] with u hu
    by_cases huI : u ∈ I
    · rw [indicator_of_mem huI]
    · rw [indicator_of_notMem huI, hWz u (by simp only [I, Set.mem_Ioo, not_and, not_lt] at huI; exact huI hu)]
  -- Step 3: `Leb|_I = μ*|_I`
  have hIsub : I ⊆ Ioc 0 us := Ioo_subset_Ioc_self
  have s3 : volume.restrict I = (muStar p).restrict I := by
    calc volume.restrict I = (volume.restrict (Ioc 0 us)).restrict I :=
          (Measure.restrict_restrict_of_subset hIsub).symm
      _ = ((muStar p).restrict (Ioc 0 us)).restrict I := by rw [muStar_restrict_us hp]
      _ = (muStar p).restrict I := Measure.restrict_restrict_of_subset hIsub
  -- Step 2: `∫_I W dμ ≤ ∫_I W dLeb`
  have s2 : ∫ u in I, W u ∂μ ≤ ∫ u in I, W u ∂volume := by
    apply integral_mono_measure (Measure.restrict_mono le_rfl h.le_volume)
    · filter_upwards [ae_restrict_mem measurableSet_Ioo] with u hu; exact hW0 u hu.1
    · rw [s3]; exact hWs.restrict
  -- Step 4
  have s4 : ∫ u in I, W u ∂(muStar p) ≤ ∫ u, W u ∂(muStar p) := by
    apply setIntegral_le_integral hWs
    filter_upwards [(show ∀ᵐ u ∂(muStar p), 0 < u by
      rw [ae_iff]
      have : {a : ℝ | ¬ 0 < a} = Iic 0 := by ext a; simp
      rw [this]; exact muStar_Iic_zero hp)] with u hu
    exact hW0 u hu
  have e1 : ∫ u, W u ∂μ = ∫ u, starPot p (gmap p u) ∂μ - K0 := by
    simp only [W]; rw [integral_sub hIμ (integrable_const _), integral_const]; simp
  have e2 : ∫ u, W u ∂(muStar p) = hallKappa p - K0 := by
    simp only [W]; rw [integral_sub hIs (integrable_const _), integral_const, hVs]; simp
  rw [s3] at s2
  linarith

/-! ### Optimality -/

/-- **Optimality** (Paper 1 Theorem 1.3(iii); G2 Theorem B*(iii)): every admissible `μ` with bounded support and
`F_p` integrable satisfies `𝒥_p(μ) ≤ κ_p`. (Uniqueness of the maximiser is not formalized.) -/
theorem Jp_le_kappa {p U : ℝ} (hp : 0 < p) {μ : Measure ℝ} (h : AdmissibleOn U μ)
    (hint : Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) (μ.prod μ)) : Jp p μ ≤ hallKappa p := by
  have := h.prob
  have hg := measurable_gmap p
  have hX := measurable_starX p
  -- `A ⊗ A`
  have eAA : (μ.map (gmap p)).prod (μ.map (gmap p)) = (μ.prod μ).map (Prod.map (gmap p) (gmap p)) :=
    Measure.map_prod_map _ _ hg hg
  have iAA : Integrable logK ((μ.map (gmap p)).prod (μ.map (gmap p))) := by
    rw [eAA, integrable_map_measure measurable_logK.aestronglyMeasurable (hg.prodMap hg).aemeasurable]
    exact hint
  have vAA : ∫ z, logK z ∂((μ.map (gmap p)).prod (μ.map (gmap p))) = Jp p μ := by
    rw [eAA, integral_map (hg.prodMap hg).aemeasurable measurable_logK.aestronglyMeasurable]; rfl
  -- `B ⊗ B`
  have eBB : (Bstar p).prod (Bstar p) = (starNu.prod starNu).map (Prod.map (starX p) (starX p)) :=
    Measure.map_prod_map _ _ hX hX
  have fBB : logK ∘ Prod.map (starX p) (starX p) = Hstar p := by
    funext z; simp [logK, Hstar, Real.log_abs]
  have iBB : Integrable logK ((Bstar p).prod (Bstar p)) := by
    rw [eBB, integrable_map_measure measurable_logK.aestronglyMeasurable (hX.prodMap hX).aemeasurable, fBB]
    exact Hstar_integrable hp
  have vBB : ∫ z, logK z ∂((Bstar p).prod (Bstar p)) = hallKappa p := by
    rw [eBB, integral_map (hX.prodMap hX).aemeasurable measurable_logK.aestronglyMeasurable]
    rw [← Hstar_integral hp]; congr 1
  -- `A ⊗ B`
  have eAB : (μ.map (gmap p)).prod (Bstar p) = (μ.prod starNu).map (Prod.map (gmap p) (starX p)) :=
    Measure.map_prod_map _ _ hg hX
  have fAB : logK ∘ Prod.map (gmap p) (starX p) = fun z => Real.log (starX p z.2 - gmap p z.1) := by
    funext z; simp only [Function.comp_apply, logK, Prod.map_fst, Prod.map_snd]
    rw [abs_sub_comm, Real.log_abs]
  have iAB : Integrable logK ((μ.map (gmap p)).prod (Bstar p)) := by
    rw [eAB, integrable_map_measure measurable_logK.aestronglyMeasurable (hg.prodMap hX).aemeasurable, fAB]
    exact cross_integrable hp h
  have vAB : ∫ z, logK z ∂((μ.map (gmap p)).prod (Bstar p)) = ∫ u, starPot p (gmap p u) ∂μ := by
    rw [eAB, integral_map (hg.prodMap hX).aemeasurable measurable_logK.aestronglyMeasurable,
      ← integral_cross hp h]
    congr 1
  -- energy positivity
  have hm : (μ.map (gmap p)) univ = (Bstar p) univ := by rw [measure_univ, Bstar, measure_univ]
  have hEP := energy_pos hm iAA iBB iAB (diag_null2 (Amap_singleton hp h)) (diag_null2 (Bstar_singleton hp))
    (diag_null2 (Bstar_singleton hp))
  have hcmp := starPot_compare hp h (cross_integrable hp h).integral_prod_left
  rw [vAA, vBB, vAB] at hEP
  linarith

end JacobiAsym
