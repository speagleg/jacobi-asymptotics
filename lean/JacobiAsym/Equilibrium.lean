import JacobiAsym.Arcsine

/-! # Plan 60, stage S2b: the maximiser μ*_u and its admissibility (Paper 1 Theorem 1.3(i), G2 Theorem B*(i))

`μ* = ∫₀¹ ω_{β_t} dt`, `β_t = 4c t^{-p}`, is realised as the image of the parameter measure
`starNu = Leb|(0,1] ⊗ π⁻¹ Leb|(0,π]` under `(t, φ) ↦ starX = β_t (1 − cos φ)/2` (x-variable) and
`muStar p` is its image under `x ↦ x^{-1/p}` (u-variable; Paper 1's `μ*_u`).

Admissibility `μ*_u (a, b] ≤ b − a` (`muStar_Ioc_le`) is proved from the explicit tail
`starNu {starX < y} = π⁻¹ ∫₀¹ arccos (1 − 2y/β_t) dt` (`starNu_X_lt`) and the identity
`π⁻¹∫₀¹ arccos (1 − 2y/β_t) dt + y^{-1/p} = 1 + (π r)⁻¹ ∫_r^1 (π − arccos (1 − 2σ^p)) dσ`, `r = (y/4c)^{1/p}`
(`tailQ_eq`), whose right side is nonincreasing in `y` and equals `1` for `y ≥ 4c` (saturation,
`muStar_Ioc_eq`). -/

open Real Set MeasureTheory Filter Topology intervalIntegral
open scoped ENNReal Interval

namespace JacobiAsym

/-- `β_t = 4 c(p) t^{-p}`. -/
noncomputable def hallBeta (p t : ℝ) : ℝ := 4 * hallC p * t ^ (-p)

/-- The angular factor `π⁻¹ Leb|(0,π]`. -/
noncomputable def angMeas : Measure ℝ := ENNReal.ofReal π⁻¹ • volume.restrict (Ioc (0 : ℝ) π)

/-- The parameter measure `Leb|(0,1] ⊗ π⁻¹ Leb|(0,π]`. -/
noncomputable def starNu : Measure (ℝ × ℝ) := (volume.restrict (Ioc (0 : ℝ) 1)).prod angMeas

/-- The x-variable: `starX p (t, φ) = β_t (1 − cos φ)/2`. -/
noncomputable def starX (p : ℝ) (z : ℝ × ℝ) : ℝ := arcX (hallBeta p z.1) z.2

/-- The u-variable: `starU p z = (starX p z)^{-1/p}`. -/
noncomputable def starU (p : ℝ) (z : ℝ × ℝ) : ℝ := starX p z ^ (-(1 / p))

/-- **The maximiser** `μ*_u` (Paper 1 Theorem 1.3), as a measure on ℝ (u-variable). -/
noncomputable def muStar (p : ℝ) : Measure ℝ := starNu.map (starU p)

instance angMeas_prob : IsProbabilityMeasure angMeas := by
  constructor
  simp only [angMeas, Measure.smul_apply, MeasurableSet.univ, Measure.restrict_apply, univ_inter,
    Real.volume_Ioc, sub_zero, smul_eq_mul]
  rw [← ENNReal.ofReal_mul (inv_nonneg.2 pi_pos.le), inv_mul_cancel₀ pi_pos.ne', ENNReal.ofReal_one]

instance restrictIoc01_prob : IsProbabilityMeasure (volume.restrict (Ioc (0 : ℝ) 1)) := by
  constructor; simp

instance starNu_prob : IsProbabilityMeasure starNu := by
  unfold starNu; infer_instance

theorem measurable_hallBeta (p : ℝ) : Measurable (hallBeta p) := by
  unfold hallBeta; fun_prop

theorem measurable_starX (p : ℝ) : Measurable (starX p) := by
  unfold starX arcX hallBeta; fun_prop

theorem measurable_starU (p : ℝ) : Measurable (starU p) := by
  unfold starU; exact (measurable_starX p).pow_const _

instance muStar_prob (p : ℝ) : IsProbabilityMeasure (muStar p) := by
  unfold muStar; infer_instance

theorem hallBeta_pos {p t : ℝ} (hp : 0 < p) (ht : 0 < t) : 0 < hallBeta p t := by
  unfold hallBeta; have := hallC_pos hp; have := rpow_pos_of_pos ht (-p); positivity

/-- `β_t/4 = c t^{-p}`, so `log (β_t/4) = log c − p log t`. -/
theorem log_hallBeta_div_four {p t : ℝ} (hp : 0 < p) (ht : 0 < t) :
    Real.log (hallBeta p t / 4) = Real.log (hallC p) - p * Real.log t := by
  unfold hallBeta
  rw [show 4 * hallC p * t ^ (-p) / 4 = hallC p * t ^ (-p) by ring,
    Real.log_mul (hallC_pos hp).ne' (rpow_pos_of_pos ht _).ne', Real.log_rpow ht]
  ring

theorem hallBeta_anti {p s t : ℝ} (hp : 0 < p) (hs : 0 < s) (hst : s ≤ t) : hallBeta p t ≤ hallBeta p s := by
  unfold hallBeta
  have := hallC_pos hp
  have : t ^ (-p) ≤ s ^ (-p) := rpow_le_rpow_of_nonpos hs hst (by linarith)
  nlinarith

/-- `β_1 = 4c`. -/
theorem hallBeta_one (p : ℝ) : hallBeta p 1 = 4 * hallC p := by simp [hallBeta]

/-- a.e. on the parameter space, `t ∈ (0,1]` and `φ ∈ (0,π]`. -/
theorem starNu_ae_mem : ∀ᵐ z ∂starNu, z.1 ∈ Ioc (0 : ℝ) 1 ∧ z.2 ∈ Ioc (0 : ℝ) π := by
  have h1 : ∀ᵐ t ∂(volume.restrict (Ioc (0 : ℝ) 1)), t ∈ Ioc (0 : ℝ) 1 := ae_restrict_mem measurableSet_Ioc
  have h2 : ∀ᵐ φ ∂angMeas, φ ∈ Ioc (0 : ℝ) π :=
    Measure.ae_smul_measure (ae_restrict_mem measurableSet_Ioc) _
  have g1 := (Measure.quasiMeasurePreserving_fst (μ := volume.restrict (Ioc (0 : ℝ) 1)) (ν := angMeas)).ae h1
  have g2 := (Measure.quasiMeasurePreserving_snd (μ := volume.restrict (Ioc (0 : ℝ) 1)) (ν := angMeas)).ae h2
  unfold starNu
  filter_upwards [g1, g2] with z hz1 hz2
  exact ⟨hz1, hz2⟩

/-! ### The tail of `starX` -/

theorem arcX_lt_iff {β y φ : ℝ} (hβ : 0 < β) : arcX β φ < y ↔ 1 - 2 * y / β < cos φ := by
  have key : arcX β φ < y ↔ β * (1 - cos φ) < β * (2 * y / β) := by
    unfold arcX; rw [mul_div_cancel₀ _ hβ.ne']; constructor <;> intro h <;> linarith
  rw [key, mul_lt_mul_iff_right₀ hβ]; constructor <;> intro h <;> linarith

/-- `|{φ ∈ (0, π] : arcX β φ < y}| = arccos (1 − 2y/β)`. -/
theorem volume_arcX_lt {β y : ℝ} (hβ : 0 < β) :
    volume ({φ | arcX β φ < y} ∩ Ioc 0 π) = ENNReal.ofReal (arccos (1 - 2 * y / β)) := by
  set z := 1 - 2 * y / β with hz
  have hsub : {φ | arcX β φ < y} ∩ Ioc 0 π ⊆ Ioc 0 (arccos z) := by
    rintro φ ⟨hφ, h0, hπ⟩
    simp only [mem_ofPred_eq, arcX_lt_iff hβ] at hφ
    refine ⟨h0, ?_⟩
    rcases le_or_gt z (-1) with hz1 | hz1
    · rw [arccos_of_le_neg_one hz1]; exact hπ
    · have hz2 : z < 1 := lt_of_lt_of_le hφ (cos_le_one φ)
      rw [← arccos_cos h0.le hπ]
      exact (strictAntiOn_arccos ⟨hz1.le, hz2.le⟩ ⟨neg_one_le_cos φ, cos_le_one φ⟩ hφ).le
  have hsup : Ioo 0 (arccos z) ⊆ {φ | arcX β φ < y} ∩ Ioc 0 π := by
    rintro φ ⟨h0, h1⟩
    have hπ : φ < π := lt_of_lt_of_le h1 (arccos_le_pi z)
    refine ⟨?_, h0, hπ.le⟩
    simp only [mem_ofPred_eq, arcX_lt_iff hβ]
    rcases le_or_gt z (-1) with hz1 | hz1
    · have : cos π < cos φ := cos_lt_cos_of_nonneg_of_le_pi h0.le le_rfl hπ
      rw [cos_pi] at this; linarith
    · rcases lt_or_ge z 1 with hz2 | hz2
      · have := cos_lt_cos_of_nonneg_of_le_pi h0.le (arccos_le_pi z) h1
        rwa [cos_arccos hz1.le hz2.le] at this
      · rw [arccos_of_one_le hz2] at h1; linarith
  apply le_antisymm
  · calc _ ≤ volume (Ioc 0 (arccos z)) := measure_mono hsub
      _ = _ := by rw [Real.volume_Ioc, sub_zero]
  · calc ENNReal.ofReal (arccos z) = volume (Ioo 0 (arccos z)) := by rw [Real.volume_Ioo, sub_zero]
      _ ≤ _ := measure_mono hsup

theorem angMeas_arcX_lt {β y : ℝ} (hβ : 0 < β) :
    angMeas {φ | arcX β φ < y} = ENNReal.ofReal (π⁻¹ * arccos (1 - 2 * y / β)) := by
  have hm : MeasurableSet {φ | arcX β φ < y} := by
    apply measurableSet_lt _ measurable_const; unfold arcX; fun_prop
  rw [angMeas, Measure.smul_apply, Measure.restrict_apply hm, volume_arcX_lt hβ, smul_eq_mul,
    ← ENNReal.ofReal_mul (inv_nonneg.2 pi_pos.le)]

/-- `T(y) = π⁻¹ ∫₀¹ arccos (1 − 2y/β_t) dt`, the `starNu`-measure of `{starX < y}`. -/
noncomputable def starTail (p y : ℝ) : ℝ := π⁻¹ * ∫ t in (0 : ℝ)..1, arccos (1 - 2 * y / hallBeta p t)

theorem measurableSet_starX_lt (p y : ℝ) : MeasurableSet {z | starX p z < y} :=
  measurableSet_lt (measurable_starX p) measurable_const

theorem starNu_X_lt {p : ℝ} (hp : 0 < p) (y : ℝ) :
    starNu {z | starX p z < y} = ENNReal.ofReal (starTail p y) := by
  rw [starNu, Measure.prod_apply (measurableSet_starX_lt p y)]
  have hslice : ∀ t ∈ Ioc (0 : ℝ) 1, angMeas (Prod.mk t ⁻¹' {z | starX p z < y}) =
      ENNReal.ofReal (π⁻¹ * arccos (1 - 2 * y / hallBeta p t)) := by
    intro t ht
    exact angMeas_arcX_lt (hallBeta_pos hp ht.1)
  rw [setLIntegral_congr_fun measurableSet_Ioc hslice]
  have hmeas : Measurable fun t => π⁻¹ * arccos (1 - 2 * y / hallBeta p t) := by
    have := measurable_hallBeta p
    exact measurable_const.mul (continuous_arccos.measurable.comp (measurable_const.sub
      (measurable_const.div this)))
  have hint : Integrable (fun t => π⁻¹ * arccos (1 - 2 * y / hallBeta p t)) (volume.restrict (Ioc (0:ℝ) 1)) := by
    refine Integrable.of_bound (C := π⁻¹ * π) hmeas.aestronglyMeasurable (Eventually.of_forall fun t => ?_)
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (inv_nonneg.2 pi_pos.le) (arccos_nonneg _))]
    exact mul_le_mul_of_nonneg_left (arccos_le_pi _) (inv_nonneg.2 pi_pos.le)
  rw [← ofReal_integral_eq_lintegral_ofReal hint (Eventually.of_forall fun t =>
    mul_nonneg (inv_nonneg.2 pi_pos.le) (arccos_nonneg _)), MeasureTheory.integral_const_mul, starTail,
    intervalIntegral.integral_of_le zero_le_one]

/-! ### The tail identity and admissibility -/

/-- `h(σ) = arccos (1 − 2σ^p)` (`= π` for `σ ≥ 1`). -/
noncomputable def hfun (p σ : ℝ) : ℝ := arccos (1 - 2 * σ ^ p)

theorem continuousOn_hfun {p : ℝ} (hp : 0 < p) : ContinuousOn (hfun p) (Ici 0) := by
  apply continuous_arccos.comp_continuousOn
  apply ContinuousOn.sub continuousOn_const
  apply ContinuousOn.mul continuousOn_const
  exact fun x _ => (continuousAt_rpow_const x p (Or.inr hp.le)).continuousWithinAt

theorem intervalIntegrable_hfun {p a b : ℝ} (hp : 0 < p) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    IntervalIntegrable (hfun p) volume a b :=
  ((continuousOn_hfun hp).mono (by
    intro x hx; exact le_trans (le_min ha hb) hx.1)).intervalIntegrable

theorem hfun_of_one_le {p σ : ℝ} (hp : 0 < p) (hσ : 1 ≤ σ) : hfun p σ = π := by
  unfold hfun; apply arccos_of_le_neg_one
  have := one_le_rpow hσ hp.le; linarith

theorem hallLam_eq_int (p : ℝ) : hallLam p = ∫ σ in (0 : ℝ)..1, (π - hfun p σ) := by
  unfold hallLam hfun
  apply integral_congr; intro σ _
  simp only
  rw [show 2 * σ ^ p - 1 = -(1 - 2 * σ ^ p) by ring, arccos_neg]

/-- The tail integrand after the substitution `t ↦ r t`. -/
theorem arccos_tail_eq {p y t : ℝ} (hp : 0 < p) (hy : 0 < y) (ht : 0 ≤ t) :
    arccos (1 - 2 * y / hallBeta p t) = hfun p ((y / (4 * hallC p)) ^ (1 / p) * t) := by
  have hc := hallC_pos hp
  unfold hfun
  rcases ht.eq_or_lt with rfl | ht
  · simp [hallBeta, zero_rpow (neg_ne_zero.2 hp.ne'), zero_rpow hp.ne']
  · congr 1
    unfold hallBeta
    rw [mul_rpow (by positivity) ht.le, ← rpow_mul (by positivity), one_div_mul_cancel hp.ne', rpow_one,
      rpow_neg ht.le]
    have : 0 < t ^ p := rpow_pos_of_pos ht p
    field_simp

/-- `G(r) = ∫_r^1 (π − h)`. -/
noncomputable def tailG (p r : ℝ) : ℝ := ∫ σ in r..1, (π - hfun p σ)

theorem pi_sub_hfun_nonneg (p σ : ℝ) : 0 ≤ π - hfun p σ := by unfold hfun; linarith [arccos_le_pi (1 - 2 * σ ^ p)]

theorem tailG_eq_zero {p r : ℝ} (hp : 0 < p) (hr : 1 ≤ r) : tailG p r = 0 := by
  unfold tailG
  rw [integral_symm, neg_eq_zero]
  have : ∫ σ in (1 : ℝ)..r, (π - hfun p σ) = ∫ σ in (1 : ℝ)..r, (0 : ℝ) := by
    apply integral_congr; intro σ hσ
    rw [uIcc_of_le hr] at hσ
    simp [hfun_of_one_le hp hσ.1]
  rw [this, intervalIntegral.integral_zero]

theorem tailG_nonneg {p r : ℝ} (hp : 0 < p) (_hr : 0 ≤ r) : 0 ≤ tailG p r := by
  rcases le_or_gt r 1 with h | h
  · exact integral_nonneg h (fun σ _ => pi_sub_hfun_nonneg p σ)
  · rw [tailG_eq_zero hp h.le]

theorem tailG_anti {p r r' : ℝ} (hp : 0 < p) (hr : 0 ≤ r) (hrr : r ≤ r') : tailG p r' ≤ tailG p r := by
  unfold tailG
  have hi : ∀ a b, 0 ≤ a → 0 ≤ b → IntervalIntegrable (fun σ => π - hfun p σ) volume a b :=
    fun a b ha hb => intervalIntegrable_const.sub (intervalIntegrable_hfun hp ha hb)
  rw [← integral_add_adjacent_intervals (hi r r' hr (hr.trans hrr)) (hi r' 1 (hr.trans hrr) zero_le_one)]
  have : 0 ≤ ∫ σ in r..r', (π - hfun p σ) := integral_nonneg hrr (fun σ _ => pi_sub_hfun_nonneg p σ)
  linarith

/-- `Q(r) = 1 + (π r)⁻¹ G(r)`. -/
noncomputable def tailQ (p r : ℝ) : ℝ := 1 + (π * r)⁻¹ * tailG p r

theorem tailQ_anti {p r r' : ℝ} (hp : 0 < p) (hr : 0 < r) (hrr : r ≤ r') : tailQ p r' ≤ tailQ p r := by
  unfold tailQ
  have h1 : (π * r')⁻¹ ≤ (π * r)⁻¹ := inv_anti₀ (by positivity) (by nlinarith [pi_pos])
  have h2 := tailG_anti hp hr.le hrr
  have h3 := tailG_nonneg hp (hr.le.trans hrr)
  have h4 : 0 ≤ (π * r)⁻¹ := by positivity
  nlinarith [mul_le_mul h1 h2 h3 h4]

theorem tailQ_eq_one {p r : ℝ} (hp : 0 < p) (hr : 1 ≤ r) : tailQ p r = 1 := by
  simp [tailQ, tailG_eq_zero hp hr]

/-- **The tail identity**: `T(y) + y^{-1/p} = Q((y/4c)^{1/p})`. -/
theorem starTail_add {p y : ℝ} (hp : 0 < p) (hy : 0 < y) :
    starTail p y + y ^ (-(1 / p)) = tailQ p ((y / (4 * hallC p)) ^ (1 / p)) := by
  have hc := hallC_pos hp
  set r := (y / (4 * hallC p)) ^ (1 / p) with hr
  have hr0 : 0 < r := rpow_pos_of_pos (by positivity) _
  have hL := hallLam_pos hp
  -- the integral after substitution
  have hT : ∫ t in (0 : ℝ)..1, arccos (1 - 2 * y / hallBeta p t) = r⁻¹ * ∫ σ in (0 : ℝ)..r, hfun p σ := by
    rw [integral_congr (g := fun t => hfun p (r * t)) (fun t ht => by
      rw [uIcc_of_le zero_le_one] at ht; exact arccos_tail_eq hp hy ht.1)]
    rw [integral_comp_mul_left (hfun p) hr0.ne', mul_zero, mul_one, smul_eq_mul]
  -- y^{-1/p} = (Λ/π) r⁻¹
  have hy' : y = 4 * hallC p * r ^ p := by
    rw [hr, ← rpow_mul (by positivity), one_div_mul_cancel hp.ne', rpow_one]; field_simp
  have hY : y ^ (-(1 / p)) = hallLam p / π * r⁻¹ := by
    rw [hy', mul_rpow (by positivity) (rpow_pos_of_pos hr0 _).le, four_hallC_rpow_neg hp, ← rpow_mul hr0.le,
      show p * -(1 / p) = -1 by field_simp, rpow_neg_one]
  -- Λ = ∫₀^r (π − h) + G(r)
  have hi : ∀ a b, 0 ≤ a → 0 ≤ b → IntervalIntegrable (fun σ => π - hfun p σ) volume a b :=
    fun a b ha hb => intervalIntegrable_const.sub (intervalIntegrable_hfun hp ha hb)
  have hLam : hallLam p = (π * r - ∫ σ in (0 : ℝ)..r, hfun p σ) + tailG p r := by
    rw [hallLam_eq_int, tailG, ← integral_add_adjacent_intervals (hi 0 r le_rfl hr0.le) (hi r 1 hr0.le zero_le_one),
      integral_sub intervalIntegrable_const (intervalIntegrable_hfun hp le_rfl hr0.le), intervalIntegral.integral_const,
      smul_eq_mul, sub_zero]
    ring
  rw [starTail, hT, hY, tailQ, hLam]
  field_simp
  ring

/-- `starX > 0` a.e. -/
theorem starX_pos_ae {p : ℝ} (hp : 0 < p) : ∀ᵐ z ∂starNu, 0 < starX p z := by
  filter_upwards [starNu_ae_mem] with z hz
  unfold starX arcX
  have hβ := hallBeta_pos hp hz.1.1
  have : cos z.2 < 1 := by
    have := cos_lt_cos_of_nonneg_of_le_pi le_rfl hz.2.2 hz.2.1
    rwa [cos_zero] at this
  have : 0 < 1 - cos z.2 := by linarith
  positivity

theorem lt_rpow_neg_inv_iff {X a p : ℝ} (hX : 0 < X) (ha : 0 < a) (hp : 0 < p) :
    a < X ^ (-(1 / p)) ↔ X < a ^ (-p) := by
  have hXX : (X ^ (-(1 / p))) ^ (-p) = X := by
    rw [← rpow_mul hX.le, show -(1 / p) * -p = 1 by field_simp, rpow_one]
  constructor
  · intro h
    have := rpow_lt_rpow_of_neg ha h (neg_neg_of_pos hp)
    rwa [hXX] at this
  · intro h
    by_contra h'
    push Not at h'
    have := rpow_le_rpow_of_nonpos (rpow_pos_of_pos hX _) h' (neg_nonpos.2 hp.le)
    rw [hXX] at this
    linarith

theorem muStar_Ioc {p a b : ℝ} (hp : 0 < p) (ha : 0 < a) (hab : a ≤ b) :
    muStar p (Ioc a b) = ENNReal.ofReal (starTail p (a ^ (-p)) - starTail p (b ^ (-p))) := by
  have hb : 0 < b := ha.trans_le hab
  rw [muStar, Measure.map_apply (measurable_starU p) measurableSet_Ioc]
  have hset : starU p ⁻¹' Ioc a b =ᵐ[starNu] {z | starX p z < a ^ (-p)} \ {z | starX p z < b ^ (-p)} := by
    filter_upwards [starX_pos_ae hp] with z hz
    apply propext
    simp only [mem_preimage, mem_Ioc, Set.mem_sdiff, mem_ofPred_eq, starU]
    rw [lt_rpow_neg_inv_iff hz ha hp, ← not_lt, lt_rpow_neg_inv_iff hz hb hp]
  rw [measure_congr hset]
  have hsub : {z | starX p z < b ^ (-p)} ⊆ {z | starX p z < a ^ (-p)} := by
    intro z hz
    exact lt_of_lt_of_le hz (rpow_le_rpow_of_nonpos ha hab (neg_nonpos.2 hp.le))
  rw [measure_sdiff hsub (measurableSet_starX_lt p _).nullMeasurableSet (measure_ne_top _ _),
    starNu_X_lt hp, starNu_X_lt hp, ENNReal.ofReal_sub]
  exact mul_nonneg (inv_nonneg.2 pi_pos.le) (integral_nonneg zero_le_one (fun _ _ => arccos_nonneg _))

theorem rpow_neg_rpow_neg_inv {a p : ℝ} (ha : 0 < a) (hp : 0 < p) : (a ^ (-p)) ^ (-(1 / p)) = a := by
  rw [← rpow_mul ha.le, show -p * -(1 / p) = 1 by field_simp, rpow_one]

/-- **Admissibility** (Paper 1 Theorem 1.3(i)): `μ*_u (a, b] ≤ b − a`. -/
theorem muStar_Ioc_le {p a b : ℝ} (hp : 0 < p) (ha : 0 < a) (hab : a ≤ b) :
    muStar p (Ioc a b) ≤ ENNReal.ofReal (b - a) := by
  have hb : 0 < b := ha.trans_le hab
  have hc := hallC_pos hp
  rw [muStar_Ioc hp ha hab]
  apply ENNReal.ofReal_le_ofReal
  have h1 := starTail_add hp (rpow_pos_of_pos ha (-p))
  have h2 := starTail_add hp (rpow_pos_of_pos hb (-p))
  rw [rpow_neg_rpow_neg_inv ha hp] at h1
  rw [rpow_neg_rpow_neg_inv hb hp] at h2
  have hy : b ^ (-p) ≤ a ^ (-p) := rpow_le_rpow_of_nonpos ha hab (neg_nonpos.2 hp.le)
  have hr : (b ^ (-p) / (4 * hallC p)) ^ (1 / p) ≤ (a ^ (-p) / (4 * hallC p)) ^ (1 / p) :=
    rpow_le_rpow (by have := rpow_pos_of_pos hb (-p); positivity)
      (div_le_div_of_nonneg_right hy (by positivity)) (by positivity)
  have hq := tailQ_anti hp (rpow_pos_of_pos (by have := rpow_pos_of_pos hb (-p); positivity) _) hr
  linarith

/-- **Saturation**: `μ*_u = Leb` on `(0, u_s]`, `u_s = Λ(p)/π`. -/
theorem muStar_Ioc_eq {p a b : ℝ} (hp : 0 < p) (ha : 0 < a) (hab : a ≤ b) (hbs : b ≤ hallLam p / π) :
    muStar p (Ioc a b) = ENNReal.ofReal (b - a) := by
  have hb : 0 < b := ha.trans_le hab
  have hc := hallC_pos hp
  rw [muStar_Ioc hp ha hab]
  congr 1
  have h1 := starTail_add hp (rpow_pos_of_pos ha (-p))
  have h2 := starTail_add hp (rpow_pos_of_pos hb (-p))
  rw [rpow_neg_rpow_neg_inv ha hp] at h1
  rw [rpow_neg_rpow_neg_inv hb hp] at h2
  -- both radii are ≥ 1
  have hus : (hallLam p / π) ^ (-p) = 4 * hallC p := by
    rw [← four_hallC_rpow_neg hp, ← rpow_mul (by positivity), show -(1 / p) * -p = 1 by field_simp, rpow_one]
  have hge : ∀ x, 0 < x → x ≤ hallLam p / π → 1 ≤ (x ^ (-p) / (4 * hallC p)) ^ (1 / p) := by
    intro x hx hxs
    apply one_le_rpow _ (by positivity)
    rw [le_div_iff₀ (by positivity), one_mul, ← hus]
    exact rpow_le_rpow_of_nonpos hx hxs (neg_nonpos.2 hp.le)
  rw [tailQ_eq_one hp (hge a ha (hab.trans hbs))] at h1
  rw [tailQ_eq_one hp (hge b hb hbs)] at h2
  linarith

/-- `μ*_u` lives on `(0, ∞)`. -/
theorem muStar_Iic_zero {p : ℝ} (hp : 0 < p) : muStar p (Iic 0) = 0 := by
  rw [muStar, Measure.map_apply (measurable_starU p) measurableSet_Iic]
  apply measure_mono_null (t := {z | ¬ 0 < starX p z})
  · intro z hz
    simp only [mem_preimage, mem_Iic, starU] at hz
    simp only [mem_ofPred_eq]
    intro hX
    have := rpow_pos_of_pos hX (-(1 / p))
    linarith
  · exact measure_eq_zero_iff_ae_notMem.2 (by filter_upwards [starX_pos_ae hp] with z hz; simpa using hz)

end JacobiAsym
