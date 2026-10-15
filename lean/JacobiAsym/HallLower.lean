import JacobiAsym.QuantileLower
import JacobiAsym.StarEnergy
import JacobiAsym.UpperBound
import JacobiAsym.HankelLimit

/-! # Plan 60, stage S1: the lower bound A-L (Paper 1 Theorem 5.2, G2 Theorem A-L)

* `Jp_scaleM` — Paper 1 Lemma 3.1 (scaling): `𝒥(μ_τ) = τ² (𝒥(μ) − p m² log τ)`.
* `exists_good_theta` — Step 1: truncating `μ*_u` to `(0, V]` and rescaling to mass 1 gives admissible `θ` with
  bounded support and `𝒥(θ) ≥ κ_p − η`.
* `hall_lower` — `liminf (log D_n + p n² log n)/n² ≥ κ_p` for the pure powers, in `hnorm` form. -/

open Real Set MeasureTheory Filter Topology
open scoped ENNReal

namespace JacobiAsym

/-! ### Atoms and the diagonal -/

theorem measure_singleton_of_lip {μ : Measure ℝ} (h0 : μ (Iic 0) = 0)
    (hlip : ∀ a b, 0 < a → a ≤ b → μ (Ioc a b) ≤ ENNReal.ofReal (b - a)) (x : ℝ) : μ {x} = 0 := by
  apply le_antisymm _ bot_le
  apply ENNReal.le_of_forall_pos_le_add
  intro ε hε _
  have hsub : ({x} : Set ℝ) ⊆ Ioc (x - ε) x := fun y hy => by
    rw [mem_singleton_iff] at hy; subst hy; exact ⟨by simp [hε], le_rfl⟩
  calc μ {x} ≤ μ (Ioc (x - ε) x) := measure_mono hsub
    _ ≤ ENNReal.ofReal (x - (x - ε)) := Ioc_le_of_lip h0 hlip (by simp)
    _ = 0 + ε := by rw [zero_add, sub_sub_cancel, ENNReal.ofReal_coe_nnreal]

theorem diag_null {μ : Measure ℝ} [SFinite μ] (hμ : ∀ x, μ {x} = 0) :
    (μ.prod μ) {z : ℝ × ℝ | z.1 = z.2} = 0 := by
  rw [Measure.prod_apply (measurableSet_eq_fun measurable_fst measurable_snd)]
  have : ∀ x : ℝ, Prod.mk x ⁻¹' {z : ℝ × ℝ | z.1 = z.2} = {x} := fun x => by ext y; simp [eq_comm]
  simp_rw [this, hμ]
  simp

/-! ### Scaling (Paper 1 Lemma 3.1) -/

/-- `μ_τ(B) = τ μ(B/τ)`. -/
noncomputable def scaleM (τ : ℝ) (μ : Measure ℝ) : Measure ℝ := ENNReal.ofReal τ • μ.map (fun u => τ * u)

theorem measurable_mul_left' (τ : ℝ) : Measurable (fun u : ℝ => τ * u) := measurable_const.mul measurable_id

theorem scaleM_apply {τ : ℝ} {μ : Measure ℝ} {s : Set ℝ} (hs : MeasurableSet s) :
    scaleM τ μ s = ENNReal.ofReal τ * μ ((fun u => τ * u) ⁻¹' s) := by
  rw [scaleM, Measure.smul_apply, Measure.map_apply (measurable_mul_left' τ) hs, smul_eq_mul]

theorem preimage_mul_Ioc {τ a b : ℝ} (hτ : 0 < τ) : (fun u => τ * u) ⁻¹' Ioc a b = Ioc (a / τ) (b / τ) := by
  ext u; simp only [Set.mem_preimage, Set.mem_Ioc]
  rw [div_lt_iff₀' hτ, le_div_iff₀' hτ]

theorem preimage_mul_Iic {τ a : ℝ} (hτ : 0 < τ) : (fun u => τ * u) ⁻¹' Iic a = Iic (a / τ) := by
  ext u; simp only [Set.mem_preimage, Set.mem_Iic]; rw [le_div_iff₀' hτ]

theorem preimage_mul_Ioi {τ a : ℝ} (hτ : 0 < τ) : (fun u => τ * u) ⁻¹' Ioi a = Ioi (a / τ) := by
  ext u; simp only [Set.mem_preimage, Set.mem_Ioi]; rw [div_lt_iff₀' hτ]

theorem scaleM_prod (τ : ℝ) (μ : Measure ℝ) [SFinite μ] :
    (scaleM τ μ).prod (scaleM τ μ) =
      (ENNReal.ofReal τ * ENNReal.ofReal τ) • (μ.prod μ).map (Prod.map (fun u => τ * u) (fun u => τ * u)) := by
  rw [scaleM, Measure.prod_smul_left, Measure.prod_smul_right, smul_smul,
    Measure.map_prod_map _ _ (measurable_mul_left' τ) (measurable_mul_left' τ)]

theorem Fp_scale {p τ u v : ℝ} (hτ : 0 < τ) (hu : 0 < u) (hv : 0 < v) (huv : u ≠ v) (hp : 0 < p) :
    Fp p (τ * u) (τ * v) = Fp p u v - p * Real.log τ := by
  have hne : u ^ (-p) - v ^ (-p) ≠ 0 := by
    intro h0
    rcases lt_or_gt_of_ne huv with h | h
    · have := rpow_lt_rpow_of_neg hu h (by linarith : -p < 0); linarith
    · have := rpow_lt_rpow_of_neg hv h (by linarith : -p < 0); linarith
  unfold Fp
  rw [mul_rpow hτ.le hu.le, mul_rpow hτ.le hv.le, ← mul_sub, abs_mul, abs_of_pos (rpow_pos_of_pos hτ _),
    Real.log_mul (rpow_pos_of_pos hτ _).ne' (abs_pos.2 hne).ne', Real.log_rpow hτ]
  ring

/-- Hypotheses on a finite measure used by the scaling lemma. -/
structure ScaleHyp (p : ℝ) (μ : Measure ℝ) : Prop where
  fin : IsFiniteMeasure μ
  le_zero : μ (Iic 0) = 0
  diag : (μ.prod μ) {z : ℝ × ℝ | z.1 = z.2} = 0
  int : Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) (μ.prod μ)

theorem ScaleHyp.ae_good {p : ℝ} {μ : Measure ℝ} (h : ScaleHyp p μ) :
    ∀ᵐ z ∂(μ.prod μ), 0 < z.1 ∧ 0 < z.2 ∧ z.1 ≠ z.2 := by
  have := h.fin
  have h0 : ∀ᵐ u ∂μ, 0 < u := by
    rw [ae_iff]
    have : {a : ℝ | ¬ 0 < a} = Iic 0 := by ext a; simp
    rw [this]; exact h.le_zero
  have g1 := (Measure.quasiMeasurePreserving_fst (μ := μ) (ν := μ)).ae h0
  have g2 := (Measure.quasiMeasurePreserving_snd (μ := μ) (ν := μ)).ae h0
  have g3 : ∀ᵐ z ∂(μ.prod μ), z.1 ≠ z.2 := by rw [ae_iff]; simpa using h.diag
  filter_upwards [g1, g2, g3] with z h1 h2 h3
  exact ⟨h1, h2, h3⟩

theorem Fp_scale_ae {p τ : ℝ} (hp : 0 < p) (hτ : 0 < τ) {μ : Measure ℝ} (h : ScaleHyp p μ) :
    (fun z : ℝ × ℝ => Fp p (Prod.map (fun u => τ * u) (fun u => τ * u) z).1
      (Prod.map (fun u => τ * u) (fun u => τ * u) z).2) =ᵐ[μ.prod μ]
      fun z => Fp p z.1 z.2 - p * Real.log τ := by
  filter_upwards [h.ae_good] with z hz
  exact Fp_scale hτ hz.1 hz.2.1 hz.2.2 hp

theorem scaleM_integrable {p τ : ℝ} (hp : 0 < p) (hτ : 0 < τ) {μ : Measure ℝ} (h : ScaleHyp p μ) :
    Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) ((scaleM τ μ).prod (scaleM τ μ)) := by
  have := h.fin
  rw [scaleM_prod]
  apply Integrable.smul_measure _ (by simp [ENNReal.mul_eq_top])
  rw [integrable_map_measure (measurable_Fp p).aestronglyMeasurable
    ((measurable_mul_left' τ).prodMap (measurable_mul_left' τ)).aemeasurable]
  exact (h.int.sub (integrable_const _)).congr (Fp_scale_ae hp hτ h).symm

/-- **Scaling** (Paper 1 Lemma 3.1): `𝒥(μ_τ) = τ² (𝒥(μ) − p m² log τ)`, `m = μ(ℝ)`. -/
theorem Jp_scaleM {p τ : ℝ} (hp : 0 < p) (hτ : 0 < τ) {μ : Measure ℝ} (h : ScaleHyp p μ) :
    Jp p (scaleM τ μ) = τ ^ 2 * (Jp p μ - p * Real.log τ * (μ.real univ) ^ 2) := by
  have := h.fin
  rw [Jp, scaleM_prod, integral_smul_measure, integral_map
    ((measurable_mul_left' τ).prodMap (measurable_mul_left' τ)).aemeasurable (measurable_Fp p).aestronglyMeasurable,
    integral_congr_ae (Fp_scale_ae hp hτ h), integral_sub h.int (integrable_const _), integral_const,
    smul_eq_mul, ENNReal.toReal_mul, ENNReal.toReal_ofReal hτ.le, Jp]
  rw [show (μ.prod μ).real univ = μ.real univ ^ 2 by
    rw [Measure.real, ← univ_prod_univ, Measure.prod_prod, ENNReal.toReal_mul, Measure.real]; ring]
  simp only [smul_eq_mul]
  ring

/-! ### Step 1: a compactly supported admissible approximant of `μ*_u` -/

/-- `μ*_u` restricted to `(0, V]`. -/
noncomputable def muTrunc (p V : ℝ) : Measure ℝ := (muStar p).restrict (Ioc 0 V)

theorem muStar_singleton {p : ℝ} (hp : 0 < p) (x : ℝ) : muStar p {x} = 0 :=
  measure_singleton_of_lip (muStar_Iic_zero hp) (fun _ _ ha hab => muStar_Ioc_le hp ha hab) x

theorem muTrunc_scaleHyp {p : ℝ} (hp : 0 < p) (V : ℝ) : ScaleHyp p (muTrunc p V) where
  fin := by unfold muTrunc; infer_instance
  le_zero := by
    rw [muTrunc, Measure.restrict_apply measurableSet_Iic]
    exact measure_mono_null inter_subset_left (muStar_Iic_zero hp)
  diag := by
    rw [muTrunc, Measure.prod_restrict, Measure.restrict_apply (measurableSet_eq_fun measurable_fst measurable_snd)]
    exact measure_mono_null inter_subset_left (diag_null (muStar_singleton hp))
  int := by
    rw [muTrunc, Measure.prod_restrict]
    exact (muStar_energy_integrable hp).integrableOn

/-- Mass of the truncation. -/
noncomputable def mTrunc (p V : ℝ) : ℝ := (muStar p (Ioc 0 V)).toReal

theorem muTrunc_real_univ (p V : ℝ) : (muTrunc p V).real univ = mTrunc p V := by
  simp [muTrunc, mTrunc, Measure.real, Measure.restrict_apply MeasurableSet.univ]

theorem mTrunc_tendsto {p : ℝ} (hp : 0 < p) : Tendsto (fun V : ℕ => mTrunc p V) atTop (𝓝 1) := by
  have hmono : Monotone (fun V : ℕ => Ioc (0 : ℝ) V) := fun a b hab =>
    Set.Ioc_subset_Ioc_right (by exact_mod_cast hab)
  have hU : (⋃ V : ℕ, Ioc (0 : ℝ) V) = Ioi 0 := by
    ext x; simp only [mem_iUnion, Set.mem_Ioc, Set.mem_Ioi]; constructor
    · rintro ⟨V, hx, _⟩; exact hx
    · intro hx; obtain ⟨V, hV⟩ := exists_nat_ge x; exact ⟨V, hx, hV⟩
  have h1 : muStar p (Ioi 0) = 1 := by
    rw [← compl_Iic, prob_compl_eq_one_sub measurableSet_Iic, muStar_Iic_zero hp]; simp
  have := tendsto_measure_iUnion_atTop (μ := muStar p) hmono
  rw [hU, h1] at this
  have h2 := (ENNReal.tendsto_toReal ENNReal.one_ne_top).comp this
  simpa [mTrunc, Function.comp_def] using h2

theorem Jp_muTrunc_tendsto {p : ℝ} (hp : 0 < p) :
    Tendsto (fun V : ℕ => Jp p (muTrunc p V)) atTop (𝓝 (hallKappa p)) := by
  have hmono : Monotone (fun V : ℕ => Ioc (0 : ℝ) V ×ˢ Ioc (0 : ℝ) V) := fun a b hab =>
    Set.prod_mono (Set.Ioc_subset_Ioc_right (by exact_mod_cast hab))
      (Set.Ioc_subset_Ioc_right (by exact_mod_cast hab))
  have hlim := tendsto_setIntegral_of_monotone (μ := (muStar p).prod (muStar p))
    (f := fun z : ℝ × ℝ => Fp p z.1 z.2) (fun V => measurableSet_Ioc.prod measurableSet_Ioc) hmono
    (muStar_energy_integrable hp).integrableOn
  have hfull : ∫ z in ⋃ V : ℕ, Ioc (0 : ℝ) V ×ˢ Ioc (0 : ℝ) V, Fp p z.1 z.2 ∂((muStar p).prod (muStar p)) =
      hallKappa p := by
    rw [Measure.restrict_eq_self_of_ae_mem, ← muStar_energy hp, Jp]
    have h0 : ∀ᵐ u ∂(muStar p), 0 < u := by
      rw [ae_iff]
      have : {a : ℝ | ¬ 0 < a} = Iic 0 := by ext a; simp
      rw [this]; exact muStar_Iic_zero hp
    have g1 := (Measure.quasiMeasurePreserving_fst (μ := muStar p) (ν := muStar p)).ae h0
    have g2 := (Measure.quasiMeasurePreserving_snd (μ := muStar p) (ν := muStar p)).ae h0
    filter_upwards [g1, g2] with z h1 h2
    simp only [mem_iUnion, mem_prod, Set.mem_Ioc]
    obtain ⟨V, hV⟩ := exists_nat_ge (max z.1 z.2)
    exact ⟨V, ⟨h1, (le_max_left _ _).trans hV⟩, h2, (le_max_right _ _).trans hV⟩
  rw [hfull] at hlim
  refine hlim.congr fun V => ?_
  rw [Jp, muTrunc, Measure.prod_restrict]

/-- The rescaled truncation `θ_V = (μ_V)_{1/m_V}`. -/
noncomputable def thetaV (p V : ℝ) : Measure ℝ := scaleM (1 / mTrunc p V) (muTrunc p V)

theorem thetaV_admissible {p V : ℝ} (hp : 0 < p) (hm : 0 < mTrunc p V) :
    AdmissibleOn (V / mTrunc p V) (thetaV p V) where
  prob := by
    constructor
    rw [thetaV, scaleM_apply MeasurableSet.univ, preimage_univ, muTrunc, Measure.restrict_apply MeasurableSet.univ,
      univ_inter, ← ENNReal.ofReal_toReal (measure_ne_top (muStar p) _), ← ENNReal.ofReal_mul (by positivity)]
    rw [show (1 / mTrunc p V) * (muStar p (Ioc 0 V)).toReal = 1 by rw [← mTrunc]; field_simp]
    simp
  le_zero := by
    rw [thetaV, scaleM_apply measurableSet_Iic, preimage_mul_Iic (by positivity), zero_div,
      (muTrunc_scaleHyp hp V).le_zero, mul_zero]
  gt_U := by
    rw [thetaV, scaleM_apply measurableSet_Ioi, preimage_mul_Ioi (by positivity),
      show V / mTrunc p V / (1 / mTrunc p V) = V by field_simp, muTrunc,
      Measure.restrict_apply measurableSet_Ioi]
    have : Ioi V ∩ Ioc 0 V = ∅ := by
      ext x; simp only [mem_inter_iff, Set.mem_Ioi, Set.mem_Ioc, mem_empty_iff_false, iff_false]
      rintro ⟨h1, _, h2⟩; linarith
    rw [this, measure_empty, mul_zero]
  lip := by
    intro a b ha hab
    have hτ : 0 < 1 / mTrunc p V := by positivity
    rw [thetaV, scaleM_apply measurableSet_Ioc, preimage_mul_Ioc hτ, muTrunc,
      Measure.restrict_apply measurableSet_Ioc]
    calc ENNReal.ofReal (1 / mTrunc p V) * muStar p (Ioc (a / (1 / mTrunc p V)) (b / (1 / mTrunc p V)) ∩ Ioc 0 V)
        ≤ ENNReal.ofReal (1 / mTrunc p V) *
            ENNReal.ofReal (b / (1 / mTrunc p V) - a / (1 / mTrunc p V)) := by
          gcongr
          exact (measure_mono inter_subset_left).trans
            (muStar_Ioc_le hp (by positivity) (div_le_div_of_nonneg_right hab hτ.le))
      _ = ENNReal.ofReal (b - a) := by
          rw [← ENNReal.ofReal_mul hτ.le]; congr 1; field_simp

theorem thetaV_integrable {p V : ℝ} (hp : 0 < p) (hm : 0 < mTrunc p V) :
    Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) ((thetaV p V).prod (thetaV p V)) :=
  scaleM_integrable hp (by positivity) (muTrunc_scaleHyp hp V)

theorem Jp_thetaV {p V : ℝ} (hp : 0 < p) (hm : 0 < mTrunc p V) :
    Jp p (thetaV p V) = Jp p (muTrunc p V) / mTrunc p V ^ 2 + p * Real.log (mTrunc p V) := by
  rw [thetaV, Jp_scaleM hp (by positivity) (muTrunc_scaleHyp hp V), muTrunc_real_univ, one_div,
    Real.log_inv]
  field_simp
  ring

/-- **Step 1 of Theorem 5.2**: admissible `θ` with bounded support and `𝒥(θ) ≥ κ_p − η`. -/
theorem exists_good_theta {p : ℝ} (hp : 0 < p) {η : ℝ} (hη : 0 < η) :
    ∃ U : ℝ, ∃ θ : Measure ℝ, ∃ _ : AdmissibleOn U θ,
      Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) (θ.prod θ) ∧ hallKappa p - η ≤ Jp p θ := by
  have hm := mTrunc_tendsto hp
  have hJ := Jp_muTrunc_tendsto hp
  have hlim : Tendsto (fun V : ℕ => Jp p (muTrunc p V) / mTrunc p V ^ 2 + p * Real.log (mTrunc p V)) atTop
      (𝓝 (hallKappa p / 1 ^ 2 + p * Real.log 1)) :=
    (hJ.div (hm.pow 2) (by norm_num)).add ((Real.continuousAt_log one_ne_zero).tendsto.comp hm |>.const_mul p)
  rw [one_pow, div_one, Real.log_one, mul_zero, add_zero] at hlim
  obtain ⟨V, hV⟩ := ((hlim.eventually (lt_mem_nhds (by linarith : hallKappa p - η < hallKappa p))).and
    (hm.eventually (lt_mem_nhds (by norm_num : (0 : ℝ) < 1)))).exists
  refine ⟨V / mTrunc p V, thetaV p V, thetaV_admissible hp hV.2, thetaV_integrable hp hV.2, ?_⟩
  rw [Jp_thetaV hp hV.2]; exact hV.1.le

/-! ### Step 4: the single Heine term -/

section HeineTerm

variable {U : ℝ} {θ : Measure ℝ}

/-- The configuration `S* = {k_i − 1 : i < n}` (0-based atom indices). -/
noncomputable def cfg (h : AdmissibleOn U θ) (n : ℕ) : Finset ℕ := (Finset.range n).image (fun i => kq h n i - 1)

theorem kq_strict (h : AdmissibleOn U θ) {n i j : ℕ} (hn : 1 ≤ n) (hij : i < j) (hj : j < n) :
    kq h n i < kq h n j := by
  have := kq_add_le h hn hij.le hj; omega

theorem kq_sub_inj (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) :
    Set.InjOn (fun i => kq h n i - 1) (Finset.range n : Set ℕ) := by
  intro i hi j hj hij
  simp only [Finset.coe_range, Set.mem_Iio] at hi hj
  have h1 := kq_pos h hn hi
  have h2 := kq_pos h hn hj
  simp only at hij
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hlt
  · have := kq_strict h hn hlt hj; omega
  · have := kq_strict h hn hlt hi; omega

theorem card_cfg (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) : (cfg h n).card = n := by
  rw [cfg, Finset.card_image_of_injOn (kq_sub_inj h hn), Finset.card_range]

theorem cfg_subset (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) : cfg h n ⊆ Finset.range (n * ⌈U⌉₊) := by
  intro a ha
  obtain ⟨i, hi, rfl⟩ := Finset.mem_image.1 ha
  have := kq_pos h hn (Finset.mem_range.1 hi)
  have := kq_le h (n := n) (i := i)
  rw [Finset.mem_range]; omega

theorem pairs_cfg (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) :
    pairs (cfg h n) = (ltS n).image (fun ij => (kq h n ij.1 - 1, kq h n ij.2 - 1)) := by
  ext ⟨a, b⟩
  simp only [pairs, cfg, ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_image, Finset.mem_range,
    Prod.mk.injEq, Prod.exists]
  constructor
  · rintro ⟨⟨⟨i, hi, rfl⟩, ⟨j, hj, rfl⟩⟩, hab⟩
    refine ⟨i, j, ⟨⟨hi, hj⟩, ?_⟩, rfl, rfl⟩
    by_contra hji; push Not at hji
    rcases hji.eq_or_lt with e | e
    · subst e; omega
    · have := kq_strict h hn e hi; omega
  · rintro ⟨i, j, ⟨⟨hi, hj⟩, hij⟩, rfl, rfl⟩
    have := kq_strict h hn hij hj
    have := kq_pos h hn hi
    exact ⟨⟨⟨i, hi, rfl⟩, ⟨j, hj, rfl⟩⟩, by omega⟩

theorem powSeq_kq (h : AdmissibleOn U θ) {p : ℝ} {n i : ℕ} (hn : 1 ≤ n) (hi : i < n) :
    powSeq p (kq h n i - 1) = (n : ℝ) ^ (-p) * uq h n i ^ (-p) := by
  have hk := kq_pos h hn hi
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  unfold powSeq
  rw [Nat.cast_sub hk, Nat.cast_one, sub_add_cancel, ← mul_rpow hn'.le (uq_pos h hn hi).le, uq,
    mul_div_cancel₀ _ hn'.ne']

theorem log_pair_term (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p) {n i j : ℕ} (hn : 1 ≤ n) (hij : i < j)
    (hj : j < n) :
    Real.log ((powSeq p (kq h n i - 1) - powSeq p (kq h n j - 1)) ^ 2) =
      2 * Fp p (uq h n i) (uq h n j) - 2 * p * Real.log n := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hui := uq_pos h hn (hij.trans hj)
  have hg := uq_gap h hn hij hj
  have hlt : uq h n i < uq h n j := by have : 0 < 1 / (n : ℝ) := by positivity
                                       linarith
  have hd : 0 < uq h n i ^ (-p) - uq h n j ^ (-p) := sub_pos.2 (rpow_lt_rpow_of_neg hui hlt (by linarith))
  rw [powSeq_kq h hn (hij.trans hj), powSeq_kq h hn hj, ← mul_sub, Real.log_pow,
    Real.log_mul (rpow_pos_of_pos hn' _).ne' hd.ne', Real.log_rpow hn', Fp, abs_of_pos hd]
  push_cast; ring

theorem pair_inj (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) :
    Set.InjOn (fun ij : ℕ × ℕ => (kq h n ij.1 - 1, kq h n ij.2 - 1)) (ltS n : Set (ℕ × ℕ)) := by
  intro x hx y hy hxy
  simp only [ltS, Finset.coe_filter, Finset.mem_product, Finset.mem_range, Set.mem_ofPred_eq] at hx hy
  simp only [Prod.mk.injEq] at hxy
  have i1 := kq_sub_inj h hn (by simpa using hx.1.1) (by simpa using hy.1.1) hxy.1
  have i2 := kq_sub_inj h hn (by simpa using hx.1.2) (by simpa using hy.1.2) hxy.2
  exact Prod.ext i1 i2

theorem card_ltS (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) : 2 * ((ltS n).card : ℝ) = n * (n - 1) := by
  have := two_mul_card_pairs (cfg h n)
  rw [pairs_cfg h hn, Finset.card_image_of_injOn (pair_inj h hn), card_cfg h hn] at this
  have hc : ((2 * (ltS n).card : ℕ) : ℝ) = ((n * (n - 1) : ℕ) : ℝ) := by rw [this]
  push_cast [Nat.cast_sub hn] at hc
  linarith

theorem pair_term_pos (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p) {n i j : ℕ} (hn : 1 ≤ n) (hij : i < j)
    (hj : j < n) : 0 < (powSeq p (kq h n i - 1) - powSeq p (kq h n j - 1)) ^ 2 := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hui := uq_pos h hn (hij.trans hj)
  have hg := uq_gap h hn hij hj
  have hn1 : 0 < 1 / (n : ℝ) := by positivity
  have hlt : uq h n i < uq h n j := by linarith
  have hd : 0 < uq h n i ^ (-p) - uq h n j ^ (-p) := sub_pos.2 (rpow_lt_rpow_of_neg hui hlt (by linarith))
  rw [powSeq_kq h hn (hij.trans hj), powSeq_kq h hn hj, ← mul_sub]
  have := rpow_pos_of_pos hn' (-p)
  positivity

/-- `log` of the Heine term at `S*` (Paper 1 Theorem 5.2, Step 4). -/
theorem log_heineTerm_cfg (h : AdmissibleOn U θ) {p s : ℝ} (hp : 0 < p) (hs : 0 < s) {n : ℕ} (hn : 1 ≤ n) :
    -(s * n * Real.log (n * ⌈U⌉₊)) - p * n * (n - 1) * Real.log n +
        2 * ∑ ij ∈ ltS n, Fp p (uq h n ij.1) (uq h n ij.2) ≤
      Real.log (heineTerm (powSeq p) (powSeq s) (cfg h n)) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hw : ∀ i ∈ Finset.range n, powSeq s (kq h n i - 1) ≠ 0 := fun i _ =>
    (rpow_pos_of_pos (by positivity) _).ne'
  have hwlog : ∀ i ∈ Finset.range n, -(s * Real.log (n * ⌈U⌉₊)) ≤ Real.log (powSeq s (kq h n i - 1)) := by
    intro i hi
    have hk := kq_pos h hn (Finset.mem_range.1 hi)
    have hkle := kq_le h (n := n) (i := i)
    unfold powSeq
    rw [Nat.cast_sub hk, Nat.cast_one, sub_add_cancel, Real.log_rpow (by exact_mod_cast hk)]
    have : Real.log (kq h n i) ≤ Real.log (n * ⌈U⌉₊) := by
      apply Real.log_le_log (by exact_mod_cast hk); exact_mod_cast hkle
    nlinarith
  have hpair : ∀ q ∈ ltS n, (powSeq p (kq h n q.1 - 1) - powSeq p (kq h n q.2 - 1)) ^ 2 ≠ 0 := by
    intro q hq
    simp only [ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_range] at hq
    exact (pair_term_pos h hp hn hq.2 hq.1.2).ne'
  have hpl : ∀ q ∈ ltS n, Real.log ((powSeq p (kq h n q.1 - 1) - powSeq p (kq h n q.2 - 1)) ^ 2) =
      2 * Fp p (uq h n q.1) (uq h n q.2) - 2 * p * Real.log n := by
    intro q hq
    simp only [ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_range] at hq
    exact log_pair_term h hp hn hq.2 hq.1.2
  unfold heineTerm
  rw [pairs_cfg h hn, cfg, Finset.prod_image (kq_sub_inj h hn), Finset.prod_image (pair_inj h hn),
    Real.log_mul (Finset.prod_ne_zero_iff.2 hw) (Finset.prod_ne_zero_iff.2 hpair), Real.log_prod hw,
    Real.log_prod hpair, Finset.sum_congr rfl hpl, Finset.sum_sub_distrib, ← Finset.mul_sum,
    Finset.sum_const, nsmul_eq_mul]
  have hsw : ∑ i ∈ Finset.range n, -(s * Real.log (n * ⌈U⌉₊)) ≤
      ∑ i ∈ Finset.range n, Real.log (powSeq s (kq h n i - 1)) := Finset.sum_le_sum hwlog
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at hsw
  have hc := card_ltS h hn
  have e1 : ((ltS n).card : ℝ) * (2 * p * Real.log n) = p * n * (n - 1) * Real.log n := by
    have : ((ltS n).card : ℝ) * (2 * p * Real.log n) = (2 * (ltS n).card) * (p * Real.log n) := by ring
    rw [this, hc]; ring
  have e2 : (n : ℝ) * -(s * Real.log (n * ⌈U⌉₊)) = -(s * n * Real.log (n * ⌈U⌉₊)) := by ring
  linarith

end HeineTerm

/-! ### The lower bound A-L -/

/-- **Theorem A-L** (Paper 1 Theorem 5.2 for `w_k = k^{-s}`): for every `η > 0`, eventually
`hnorm ≥ −η`, i.e. `liminf (log D_n + p n² log n)/n² ≥ κ_p`. -/
theorem hall_lower {p s : ℝ} (hp : 0 < p) (hs : 1 < s) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop, -η ≤ hnorm p (hallKappa p) (heineD (powSeq p) (powSeq s)) (fun _ => 0) n := by
  obtain ⟨U, θ, h, hint, hJ⟩ := exists_good_theta hp (half_pos (half_pos hη))
  have hq := quantile_lower h hp hint (half_pos (half_pos hη))
  have hU1 : 1 ≤ ⌈U⌉₊ := Nat.one_le_iff_ne_zero.2 (by
    rw [Ne, Nat.ceil_eq_zero, not_le]; exact h.U_pos)
  -- the error term `s n log (n ⌈U⌉) / n² → 0`
  have herr : Tendsto (fun n : ℕ => s * Real.log (n * ⌈U⌉₊) / n) atTop (𝓝 0) := by
    have h1 := tendsto_log_div_nat.const_mul s
    have h2 := tendsto_const_div_atTop_nhds_zero_nat (s * Real.log ⌈U⌉₊)
    have := h1.add h2
    simp only [mul_zero, add_zero] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    have hU' : (0 : ℝ) < ⌈U⌉₊ := by exact_mod_cast hU1
    rw [Real.log_mul hn'.ne' hU'.ne']; field_simp
  have hbdd := heineK_bdd_of_summable (x := powSeq p) (w := powSeq s) (X := 1)
    (fun k => (rpow_pos_of_pos (by positivity) _).le)
    (by
      have := (Real.summable_nat_rpow_inv.2 hs).comp_injective (add_left_injective 1)
      refine this.congr fun k => ?_
      simp [powSeq, rpow_neg (by positivity : (0 : ℝ) ≤ (k : ℝ) + 1)])
    (fun k => by
      unfold powSeq
      rw [abs_of_pos (rpow_pos_of_pos (by positivity) _)]
      exact rpow_le_one_of_one_le_of_nonpos (by have := Nat.cast_nonneg (α := ℝ) k; linarith) (by linarith))
  filter_upwards [hq, herr.eventually (gt_mem_nhds (half_pos hη)), eventually_ge_atTop 1] with n hqn hen hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  -- D_n ≥ heineTerm at S*
  have hterm_pos : 0 < heineTerm (powSeq p) (powSeq s) (cfg h n) := by
    unfold heineTerm
    apply mul_pos (Finset.prod_pos fun i _ => rpow_pos_of_pos (by positivity) _)
    rw [pairs_cfg h hn, Finset.prod_image (pair_inj h hn)]
    apply Finset.prod_pos
    intro q hq
    simp only [ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_range] at hq
    exact pair_term_pos h hp hn hq.2 hq.1.2
  have hDge : heineTerm (powSeq p) (powSeq s) (cfg h n) ≤ heineD (powSeq p) (powSeq s) n := by
    refine le_trans ?_ (heineK_le_heineD (hbdd n) (n * ⌈U⌉₊))
    exact Finset.single_le_sum (f := heineTerm (powSeq p) (powSeq s))
      (fun S _ => heineTerm_nonneg (fun k => (rpow_pos_of_pos (by positivity) _).le) S)
      (Finset.mem_powersetCard.2 ⟨cfg_subset h hn, card_cfg h hn⟩)
  have hlog := (log_heineTerm_cfg h hp (by linarith) hn).trans (Real.log_le_log hterm_pos hDge)
  -- assemble
  rw [div_lt_iff₀ hn'] at hen
  unfold hnorm
  rw [le_div_iff₀ (by positivity)]
  have hlogn : 0 ≤ Real.log n := Real.log_natCast_nonneg n
  have h3 : 0 ≤ p * n * Real.log n := by positivity
  nlinarith

end JacobiAsym
