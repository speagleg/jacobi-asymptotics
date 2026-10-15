import Mathlib

/-! # Plan 60, stage S4: energy positivity (Paper 1 Lemma 3.3, inequality part; G2 Lemma EP)

For finite measures `A`, `B` on ℝ of equal mass, with `log |x − y|` integrable against `A⊗A`, `B⊗B`, `A⊗B` and
null diagonals,
`∬ log|x−y| dA dA + ∬ log|x−y| dB dB ≤ 2 ∬ log|x−y| dA dB` (`energy_pos`).

Proof (differs from the paper's Fourier argument): Frullani's integral (Mathlib `Frullani.integral_Ioi_eq`)
`2 log |a| = ∫₀^∞ t⁻¹ (e^{−t} − e^{−a² t}) dt`, Fubini, and positive definiteness of the Gaussian kernel,
`e^{−t(x−y)²} = √(4t/π) ∫ e^{−2t(x−w)²} e^{−2t(y−w)²} dw` (`gauss_conv`). -/

open Real Set MeasureTheory Filter Topology

namespace JacobiAsym

/-! ### The Frullani kernel -/

/-- `k_t(a) = t⁻¹ (e^{−t} − e^{−a² t})`. -/
noncomputable def frK (t a : ℝ) : ℝ := t⁻¹ * (exp (-(1 * t)) - exp (-(a ^ 2 * t)))

theorem exp_sub_exp_le {u v : ℝ} (_h : v ≤ u) : exp u - exp v ≤ (u - v) * exp u := by
  have h1 := add_one_le_exp (-(u - v))
  have h2 : exp v = exp u * exp (-(u - v)) := by rw [← exp_add]; ring_nf
  rw [h2]
  have := exp_pos u
  nlinarith

theorem abs_exp_sub_exp_le {u v w : ℝ} (hu : u ≤ w) (hv : v ≤ w) : |exp u - exp v| ≤ |u - v| * exp w := by
  rcases le_total v u with h | h
  · rw [abs_of_nonneg (by linarith [exp_le_exp.2 h]), abs_of_nonneg (by linarith)]
    exact (exp_sub_exp_le h).trans (mul_le_mul_of_nonneg_left (exp_le_exp.2 hu) (by linarith))
  · rw [abs_of_nonpos (by linarith [exp_le_exp.2 h]), abs_of_nonpos (by linarith)]
    have := exp_sub_exp_le h
    have := mul_le_mul_of_nonneg_left (exp_le_exp.2 hv) (by linarith : 0 ≤ v - u)
    linarith

theorem frK_bound {t a : ℝ} (ht : 0 < t) :
    |frK t a| ≤ |a ^ 2 - 1| * exp (-(min 1 (a ^ 2) * t)) := by
  have hm1 : -(1 * t) ≤ -(min 1 (a ^ 2) * t) := by
    have := min_le_left 1 (a ^ 2); nlinarith
  have hm2 : -(a ^ 2 * t) ≤ -(min 1 (a ^ 2) * t) := by
    have := min_le_right 1 (a ^ 2); nlinarith
  have := abs_exp_sub_exp_le hm1 hm2
  unfold frK
  rw [abs_mul, abs_inv, abs_of_pos ht]
  have e : |-(1 * t) - -(a ^ 2 * t)| = |a ^ 2 - 1| * t := by
    rw [show -(1 * t) - -(a ^ 2 * t) = (a ^ 2 - 1) * t by ring, abs_mul, abs_of_pos ht]
  rw [e] at this
  calc t⁻¹ * |exp (-(1 * t)) - exp (-(a ^ 2 * t))| ≤ t⁻¹ * (|a ^ 2 - 1| * t * exp (-(min 1 (a ^ 2) * t))) :=
        mul_le_mul_of_nonneg_left this (by positivity)
    _ = _ := by field_simp

theorem frK_integrable {a : ℝ} (ha : a ≠ 0) : IntegrableOn (fun t => frK t a) (Ioi 0) := by
  have hm : 0 < min 1 (a ^ 2) := lt_min one_pos (by positivity)
  have hb : IntegrableOn (fun t => |a ^ 2 - 1| * exp (-(min 1 (a ^ 2) * t))) (Ioi 0) := by
    have := (exp_neg_integrableOn_Ioi 0 hm).const_mul |a ^ 2 - 1|
    have e : (fun t => |a ^ 2 - 1| * exp (-(min 1 (a ^ 2) * t))) =
        fun t => |a ^ 2 - 1| * exp (-min 1 (a ^ 2) * t) := by funext t; rw [neg_mul]
    rw [e]; exact this
  refine Integrable.mono' hb ?_ ?_
  · apply ContinuousOn.aestronglyMeasurable _ measurableSet_Ioi
    intro t ht
    unfold frK
    exact ((continuousAt_inv₀ (ne_of_gt ht)).mul (by fun_prop)).continuousWithinAt
  · filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
    rw [Real.norm_eq_abs]; exact frK_bound ht

/-- Frullani: `∫₀^∞ k_t(a) dt = 2 log |a|`. -/
theorem frK_integral {a : ℝ} (ha : a ≠ 0) : ∫ t in Ioi 0, frK t a = 2 * Real.log |a| := by
  have hf : LocallyIntegrableOn (fun y : ℝ => exp (-y)) (Ioi 0) :=
    (continuous_exp.comp continuous_neg).locallyIntegrable.locallyIntegrableOn _
  have hL : Tendsto (fun y : ℝ => exp (-y)) (𝓝[>] 0) (𝓝 1) := by
    have : Tendsto (fun y : ℝ => exp (-y)) (𝓝 0) (𝓝 (exp (-0))) :=
      ((continuous_exp.comp continuous_neg).tendsto 0)
    rw [neg_zero, exp_zero] at this
    exact this.mono_left nhdsWithin_le_nhds
  have hR : Tendsto (fun y : ℝ => exp (-y)) atTop (𝓝 0) := Real.tendsto_exp_neg_atTop_nhds_zero
  have h := Frullani.integral_Ioi_eq hf one_pos (by positivity : (0 : ℝ) < a ^ 2) hL hR
    (by simpa [frK, smul_eq_mul] using frK_integrable ha)
  simp only [smul_eq_mul, div_one, sub_zero, mul_one] at h
  unfold frK
  rw [h, Real.log_pow, ← Real.log_abs]; push_cast; ring

/-- `k_t(a)` has constant sign in `t`, so `∫ |k| = |∫ k|`. -/
theorem frK_abs_integral {a : ℝ} (ha : a ≠ 0) : ∫ t in Ioi 0, |frK t a| = abs (2 * Real.log |a|) := by
  rw [← frK_integral ha]
  rcases le_total 1 (a ^ 2) with h | h
  · have hnn : ∀ t ∈ Ioi (0 : ℝ), 0 ≤ frK t a := fun t ht => by
      unfold frK
      apply mul_nonneg (inv_nonneg.2 (le_of_lt ht))
      rw [sub_nonneg, exp_le_exp]; have : (0:ℝ) < t := ht; nlinarith
    rw [abs_of_nonneg (setIntegral_nonneg measurableSet_Ioi hnn)]
    exact setIntegral_congr_fun measurableSet_Ioi (fun t ht => abs_of_nonneg (hnn t ht))
  · have hnp : ∀ t ∈ Ioi (0 : ℝ), frK t a ≤ 0 := fun t ht => by
      unfold frK
      apply mul_nonpos_of_nonneg_of_nonpos (inv_nonneg.2 (le_of_lt ht))
      rw [sub_nonpos, exp_le_exp]; have : (0:ℝ) < t := ht; nlinarith
    rw [abs_of_nonpos (setIntegral_nonpos measurableSet_Ioi hnp), ← integral_neg]
    exact setIntegral_congr_fun measurableSet_Ioi (fun t ht => abs_of_nonpos (hnp t ht))

/-! ### Frullani representation of the logarithmic energy -/

/-- `log |x − y|`. -/
noncomputable def logK (z : ℝ × ℝ) : ℝ := Real.log |z.1 - z.2|

/-- `e^{−t (x − y)²}`. -/
noncomputable def gaussK (t : ℝ) (z : ℝ × ℝ) : ℝ := exp (-((z.1 - z.2) ^ 2 * t))

theorem measurable_logK : Measurable logK := by unfold logK; fun_prop

theorem measurable_frK_prod : Measurable (fun w : ℝ × (ℝ × ℝ) => frK w.1 (w.2.1 - w.2.2)) := by
  unfold frK; fun_prop

theorem gaussK_le_one {t : ℝ} (ht : 0 ≤ t) (z : ℝ × ℝ) : gaussK t z ≤ 1 := by
  rw [gaussK, ← exp_zero, exp_le_exp]
  have := mul_nonneg (sq_nonneg (z.1 - z.2)) ht; linarith

theorem gaussK_integrable {P Q : Measure ℝ} [IsFiniteMeasure P] [IsFiniteMeasure Q] {t : ℝ} (ht : 0 ≤ t) :
    Integrable (gaussK t) (P.prod Q) := by
  refine Integrable.of_bound (C := 1) (show Measurable (gaussK t) by unfold gaussK; fun_prop).aestronglyMeasurable
    (Eventually.of_forall fun z => ?_)
  rw [Real.norm_eq_abs, abs_of_pos (show 0 < gaussK t z from exp_pos _)]; exact gaussK_le_one ht z

section Frullani

variable {P Q : Measure ℝ} [IsFiniteMeasure P] [IsFiniteMeasure Q]

omit [IsFiniteMeasure P] [IsFiniteMeasure Q] in
theorem ae_ne_of_diag (hdiag : (P.prod Q) {z | z.1 = z.2} = 0) : ∀ᵐ z ∂(P.prod Q), z.1 - z.2 ≠ 0 := by
  rw [ae_iff]; simpa [sub_eq_zero] using hdiag

theorem frK_prod_integrable (hint : Integrable logK (P.prod Q)) (hdiag : (P.prod Q) {z | z.1 = z.2} = 0) :
    Integrable (fun w : ℝ × (ℝ × ℝ) => frK w.1 (w.2.1 - w.2.2)) ((volume.restrict (Ioi 0)).prod (P.prod Q)) := by
  rw [integrable_prod_iff' measurable_frK_prod.aestronglyMeasurable]
  constructor
  · filter_upwards [ae_ne_of_diag hdiag] with z hz
    exact frK_integrable hz
  · refine (hint.abs.const_mul 2).congr ?_
    filter_upwards [ae_ne_of_diag hdiag] with z hz
    simp only [Real.norm_eq_abs]
    rw [frK_abs_integral hz, abs_mul, abs_two, logK]

/-- `2 𝓛(P, Q) = ∫₀^∞ t⁻¹ (e^{−t} |P||Q| − ∬ e^{−t(x−y)²} dP dQ) dt`, with integrable right side. -/
theorem two_logEnergy_eq (hint : Integrable logK (P.prod Q)) (hdiag : (P.prod Q) {z | z.1 = z.2} = 0) :
    IntegrableOn (fun t => t⁻¹ * (exp (-(1 * t)) * (P.prod Q).real univ - ∫ z, gaussK t z ∂(P.prod Q)))
        (Ioi 0) ∧
      2 * ∫ z, logK z ∂(P.prod Q) =
        ∫ t in Ioi 0, t⁻¹ * (exp (-(1 * t)) * (P.prod Q).real univ - ∫ z, gaussK t z ∂(P.prod Q)) := by
  have hF := frK_prod_integrable hint hdiag
  have hinner : ∀ t ∈ Ioi (0 : ℝ), ∫ z, frK t (z.1 - z.2) ∂(P.prod Q) =
      t⁻¹ * (exp (-(1 * t)) * (P.prod Q).real univ - ∫ z, gaussK t z ∂(P.prod Q)) := by
    intro t ht
    have e : (fun z : ℝ × ℝ => frK t (z.1 - z.2)) = fun z => t⁻¹ * (exp (-(1 * t)) - gaussK t z) := by
      funext z; simp [frK, gaussK]
    rw [e, integral_const_mul, integral_sub (integrable_const _) (gaussK_integrable (le_of_lt ht)),
      integral_const, smul_eq_mul, mul_comm (exp _)]
  constructor
  · exact (show IntegrableOn (fun t => ∫ z, frK t (z.1 - z.2) ∂(P.prod Q)) (Ioi 0) volume from
      hF.integral_prod_left).congr_fun (fun t ht => hinner t ht) measurableSet_Ioi
  · have h1 := integral_prod_symm _ hF
    have h2 := integral_prod _ hF
    rw [h1] at h2
    have hz : ∀ᵐ z ∂(P.prod Q), ∫ t in Ioi 0, frK t (z.1 - z.2) = 2 * logK z := by
      filter_upwards [ae_ne_of_diag hdiag] with z hz
      rw [frK_integral hz, logK]
    rw [integral_congr_ae hz, integral_const_mul, setIntegral_congr_fun measurableSet_Ioi hinner] at h2
    exact h2

end Frullani

/-! ### Positive definiteness of the Gaussian kernel -/

theorem gauss_split {t : ℝ} (x y w : ℝ) :
    exp (-(2 * t) * (x - w) ^ 2) * exp (-(2 * t) * (y - w) ^ 2) =
      exp (-((x - y) ^ 2 * t)) * exp (-(4 * t) * (w - (x + y) / 2) ^ 2) := by
  rw [← exp_add, ← exp_add]; congr 1; ring

/-- `∫ e^{−2t(x−w)²} e^{−2t(y−w)²} dw = √(π/4t) e^{−t(x−y)²}`. -/
theorem gauss_conv {t : ℝ} (_ht : 0 < t) (x y : ℝ) :
    ∫ w, exp (-(2 * t) * (x - w) ^ 2) * exp (-(2 * t) * (y - w) ^ 2) =
      √(π / (4 * t)) * exp (-((x - y) ^ 2 * t)) := by
  simp_rw [gauss_split x y]
  rw [integral_const_mul, integral_sub_right_eq_self (fun w => exp (-(4 * t) * w ^ 2)) ((x + y) / 2),
    integral_gaussian]
  ring

theorem gauss_conv_integrable {t : ℝ} (ht : 0 < t) (x y : ℝ) :
    Integrable (fun w => exp (-(2 * t) * (x - w) ^ 2) * exp (-(2 * t) * (y - w) ^ 2)) := by
  simp_rw [gauss_split x y]
  exact ((integrable_exp_neg_mul_sq (by linarith : 0 < 4 * t)).comp_sub_right ((x + y) / 2)).const_mul _

/-- Gaussian amplitude `a_P(w) = ∫ e^{−2t(x−w)²} dP(x)`. -/
noncomputable def gAmp (t : ℝ) (P : Measure ℝ) (w : ℝ) : ℝ := ∫ x, exp (-(2 * t) * (x - w) ^ 2) ∂P

section Gauss

variable {P Q : Measure ℝ} [IsFiniteMeasure P] [IsFiniteMeasure Q]

theorem gauss_prod_integrable {t : ℝ} (ht : 0 < t) :
    Integrable (fun v : ℝ × (ℝ × ℝ) => exp (-(2 * t) * (v.2.1 - v.1) ^ 2) * exp (-(2 * t) * (v.2.2 - v.1) ^ 2))
      (volume.prod (P.prod Q)) := by
  rw [integrable_prod_iff' (by fun_prop : Measurable fun v : ℝ × (ℝ × ℝ) =>
    exp (-(2 * t) * (v.2.1 - v.1) ^ 2) * exp (-(2 * t) * (v.2.2 - v.1) ^ 2)).aestronglyMeasurable]
  refine ⟨Eventually.of_forall fun z => gauss_conv_integrable ht z.1 z.2, ?_⟩
  refine Integrable.of_bound (C := √(π / (4 * t))) ?_ (Eventually.of_forall fun z => ?_)
  · apply Measurable.aestronglyMeasurable
    have : (fun z : ℝ × ℝ => ∫ w, ‖exp (-(2 * t) * (z.1 - w) ^ 2) * exp (-(2 * t) * (z.2 - w) ^ 2)‖) =
        fun z => √(π / (4 * t)) * exp (-((z.1 - z.2) ^ 2 * t)) := by
      funext z
      simp_rw [Real.norm_eq_abs, abs_of_pos (mul_pos (exp_pos _) (exp_pos _))]
      exact gauss_conv ht z.1 z.2
    rw [this]; fun_prop
  · simp_rw [Real.norm_eq_abs, abs_of_pos (mul_pos (exp_pos _) (exp_pos _))]
    rw [gauss_conv ht, abs_of_nonneg (by positivity)]
    have : exp (-((z.1 - z.2) ^ 2 * t)) ≤ 1 := by
      rw [← exp_zero, exp_le_exp]; have := mul_nonneg (sq_nonneg (z.1 - z.2)) ht.le; linarith
    have := Real.sqrt_nonneg (π / (4 * t))
    nlinarith

theorem gAmp_mul_integrable {t : ℝ} (ht : 0 < t) : Integrable (fun w => gAmp t P w * gAmp t Q w) := by
  have := (gauss_prod_integrable (P := P) (Q := Q) ht).integral_prod_left
  refine this.congr (Eventually.of_forall fun w => ?_)
  simp only [gAmp]
  exact integral_prod_mul (fun x => exp (-(2 * t) * (x - w) ^ 2)) (fun y => exp (-(2 * t) * (y - w) ^ 2))

/-- `∬ e^{−t(x−y)²} dP dQ = √(4t/π) ∫ a_P a_Q`. -/
theorem gaussK_conv {t : ℝ} (ht : 0 < t) :
    ∫ z, gaussK t z ∂(P.prod Q) = √(4 * t / π) * ∫ w, gAmp t P w * gAmp t Q w := by
  have hI := gauss_prod_integrable (P := P) (Q := Q) ht
  have h1 : ∫ w, gAmp t P w * gAmp t Q w = ∫ w, ∫ z, exp (-(2 * t) * (z.1 - w) ^ 2) *
      exp (-(2 * t) * (z.2 - w) ^ 2) ∂(P.prod Q) := by
    congr 1; funext w
    exact (integral_prod_mul (fun x => exp (-(2 * t) * (x - w) ^ 2)) (fun y => exp (-(2 * t) * (y - w) ^ 2))).symm
  have h2 := integral_integral_swap (μ := volume) (ν := P.prod Q)
    (f := fun w z => exp (-(2 * t) * (z.1 - w) ^ 2) * exp (-(2 * t) * (z.2 - w) ^ 2)) hI
  rw [h1, h2]
  simp_rw [gauss_conv ht]
  rw [integral_const_mul, ← mul_assoc, ← Real.sqrt_mul (by positivity),
    show 4 * t / π * (π / (4 * t)) = 1 by field_simp, Real.sqrt_one, one_mul]
  rfl

end Gauss

/-- Positive definiteness: `G(A,A) + G(B,B) − 2 G(A,B) ≥ 0`. -/
theorem gauss_pd {A B : Measure ℝ} [IsFiniteMeasure A] [IsFiniteMeasure B] {t : ℝ} (ht : 0 < t) :
    0 ≤ (∫ z, gaussK t z ∂(A.prod A)) + (∫ z, gaussK t z ∂(B.prod B)) - 2 * ∫ z, gaussK t z ∂(A.prod B) := by
  rw [gaussK_conv ht, gaussK_conv ht, gaussK_conv ht]
  have hAA := gAmp_mul_integrable (P := A) (Q := A) ht
  have hBB := gAmp_mul_integrable (P := B) (Q := B) ht
  have hAB := gAmp_mul_integrable (P := A) (Q := B) ht
  set IAA := ∫ w, gAmp t A w * gAmp t A w
  set IBB := ∫ w, gAmp t B w * gAmp t B w
  set IAB := ∫ w, gAmp t A w * gAmp t B w
  have hsq : ∫ w, (gAmp t A w - gAmp t B w) ^ 2 = IAA + IBB - 2 * IAB := by
    have e : (fun w => (gAmp t A w - gAmp t B w) ^ 2) =
        fun w => (gAmp t A w * gAmp t A w + gAmp t B w * gAmp t B w) - 2 * (gAmp t A w * gAmp t B w) := by
      funext w; ring
    have h1 := integral_sub (hAA.add hBB) (hAB.const_mul 2)
    have h2 := integral_add hAA hBB
    simp only [Pi.add_apply] at h1 h2
    rw [e, h1, h2, integral_const_mul]
  have hnn : 0 ≤ IAA + IBB - 2 * IAB := hsq ▸ integral_nonneg fun w => sq_nonneg _
  have := Real.sqrt_nonneg (4 * t / π)
  nlinarith [mul_nonneg this hnn]

/-! ### Lemma EP -/

/-- **Energy positivity** (Paper 1 Lemma 3.3, inequality; G2 Lemma EP): for finite measures of equal mass
with the logarithmic kernel integrable and null diagonals,
`∬ log|x−y| dA dA + ∬ log|x−y| dB dB ≤ 2 ∬ log|x−y| dA dB`. -/
theorem energy_pos {A B : Measure ℝ} [IsFiniteMeasure A] [IsFiniteMeasure B] (hm : A univ = B univ)
    (hAA : Integrable logK (A.prod A)) (hBB : Integrable logK (B.prod B)) (hAB : Integrable logK (A.prod B))
    (dAA : (A.prod A) {z | z.1 = z.2} = 0) (dBB : (B.prod B) {z | z.1 = z.2} = 0)
    (dAB : (A.prod B) {z | z.1 = z.2} = 0) :
    (∫ z, logK z ∂(A.prod A)) + (∫ z, logK z ∂(B.prod B)) ≤ 2 * ∫ z, logK z ∂(A.prod B) := by
  obtain ⟨iAA, eAA⟩ := two_logEnergy_eq hAA dAA
  obtain ⟨iBB, eBB⟩ := two_logEnergy_eq hBB dBB
  obtain ⟨iAB, eAB⟩ := two_logEnergy_eq hAB dAB
  have hmass : (A.prod A).real univ = (A.prod B).real univ ∧ (B.prod B).real univ = (A.prod B).real univ := by
    constructor <;>
    rw [Measure.real, Measure.real, ← univ_prod_univ, Measure.prod_prod, Measure.prod_prod, hm]
  set LAA := ∫ z, logK z ∂(A.prod A)
  set LBB := ∫ z, logK z ∂(B.prod B)
  set LAB := ∫ z, logK z ∂(A.prod B)
  set hAAf := fun t : ℝ => t⁻¹ * (exp (-(1 * t)) * (A.prod A).real univ - ∫ z, gaussK t z ∂(A.prod A))
  set hBBf := fun t : ℝ => t⁻¹ * (exp (-(1 * t)) * (B.prod B).real univ - ∫ z, gaussK t z ∂(B.prod B))
  set hABf := fun t : ℝ => t⁻¹ * (exp (-(1 * t)) * (A.prod B).real univ - ∫ z, gaussK t z ∂(A.prod B))
  have hcomb : 2 * LAA + 2 * LBB - 2 * (2 * LAB) = ∫ t in Ioi 0, (hAAf t + hBBf t - 2 * hABf t) := by
    have h1 := integral_sub (iAA.add iBB) (iAB.const_mul 2)
    have h2 := integral_add iAA iBB
    simp only [Pi.add_apply] at h1 h2
    rw [h1, h2, integral_const_mul, ← eAA, ← eBB, ← eAB]
  have hle : ∫ t in Ioi 0, (hAAf t + hBBf t - 2 * hABf t) ≤ 0 := by
    apply setIntegral_nonpos measurableSet_Ioi
    intro t ht
    have hg := gauss_pd (A := A) (B := B) ht
    have hti : 0 ≤ t⁻¹ := inv_nonneg.2 (le_of_lt ht)
    simp only [hAAf, hBBf, hABf]
    rw [hmass.1, hmass.2]
    nlinarith [mul_nonneg hti hg]
  linarith

end JacobiAsym
