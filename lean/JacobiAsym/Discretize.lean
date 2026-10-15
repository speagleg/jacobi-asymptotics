import JacobiAsym.Optimality
import JacobiAsym.HeineCompare

/-! # Plan 60, stage S3: discretisation (Paper 1 Lemma 4.1, G2 Lemma A1)

For `S ⊆ {0, …, Mn−1}` (0-based atoms; integer `k = a + 1 ≤ Mn`), `|S| = N ≤ n`, the cell measure
`μ̄_S = Leb|⋃_{a ∈ S} (a/n, (a+1)/n]` satisfies `2 Σ_{a<b} F(u_a, u_b) ≤ n² 𝒥_p(μ̄_S) + C_M n (log n + 1)`,
`u_a = (a+1)/n` (`disc_upper`).

Ingredients: `F` is integrable on `(Leb|(0,M])²` (`Fp_integrable_box`); `F(u,v) ≥ log (p M^{-p-1}) + log |u − v|`
on `(0,M]²`; `∫₀¹ log |x − s| dx ≥ −3` for all `s` (`integral_log_abs_sub_ge`), which bounds the averages over
diagonal and adjacent cells by `−log n − O(1)`; non-adjacent cells by an exact monotone comparison with error
`1/(b−a−1)` as in the paper. -/

open Real Set MeasureTheory Filter Topology
open scoped ENNReal

namespace JacobiAsym

/-! ### One-dimensional logarithmic integrals -/

theorem mul_log_ge_sub_one {x : ℝ} (hx : 0 < x) : x - 1 ≤ x * Real.log x := by
  have := Real.one_sub_inv_le_log_of_pos hx
  have h : x * (1 - x⁻¹) = x - 1 := by field_simp
  nlinarith [mul_le_mul_of_nonneg_left this hx.le]

/-- `Ψ(a+1) − Ψ(a) ≥ −2` for `Ψ(x) = x log x` (Lean's `log`, so `Ψ` is odd). -/
theorem psi_step_ge (a : ℝ) : -2 ≤ (a + 1) * Real.log (a + 1) - a * Real.log a := by
  rcases le_or_gt 0 a with ha | ha
  · rcases ha.eq_or_lt with rfl | ha
    · simp
    have h1 : a * Real.log a ≤ a * Real.log (a + 1) :=
      mul_le_mul_of_nonneg_left (Real.log_le_log ha (by linarith)) ha.le
    have h2 : 0 ≤ Real.log (a + 1) := Real.log_nonneg (by linarith)
    nlinarith
  rcases le_or_gt (a + 1) 0 with hb | hb
  · -- both nonpositive: reflect
    set c := -(a + 1)
    have hc : 0 ≤ c := by simp only [c]; linarith
    have e1 : (a + 1) * Real.log (a + 1) = -(c * Real.log c) := by
      simp only [c]; rw [Real.log_neg_eq_log]; ring
    have e2 : a * Real.log a = -((c + 1) * Real.log (c + 1)) := by
      have : a = -(c + 1) := by simp only [c]; ring
      rw [this, Real.log_neg_eq_log]; ring
    rw [e1, e2]
    rcases hc.eq_or_lt with h0 | hc
    · rw [← h0]; simp
    have h1 : c * Real.log c ≤ c * Real.log (c + 1) :=
      mul_le_mul_of_nonneg_left (Real.log_le_log hc (by linarith)) hc.le
    have h2 : 0 ≤ Real.log (c + 1) := Real.log_nonneg (by linarith)
    nlinarith
  · -- a < 0 < a + 1
    have h1 := mul_log_ge_sub_one hb
    have h2 := mul_log_ge_sub_one (show 0 < -a by linarith)
    rw [Real.log_neg_eq_log] at h2
    nlinarith

/-- `∫₀¹ log |x − s| dx ≥ −3` for every `s`. -/
theorem integral_log_abs_sub_ge (s : ℝ) : -3 ≤ ∫ x in (0 : ℝ)..1, Real.log |x - s| := by
  simp_rw [Real.log_abs]
  rw [intervalIntegral.integral_comp_sub_right (fun x => Real.log x) s, integral_log]
  have := psi_step_ge (0 - s)
  rw [show (0 - s) + 1 = 1 - s by ring] at this
  linarith

/-! ### Two-sided bounds on the kernel on `(0, M]²` -/

theorem Fp_le_box {p u v : ℝ} (hp : 0 < p) (hu : 0 < u) (hv : 0 < v) :
    Fp p u v ≤ p * |Real.log u| + p * |Real.log v| := by
  unfold Fp
  have hu' := rpow_pos_of_pos hu (-p)
  have hv' := rpow_pos_of_pos hv (-p)
  have h1 : 0 ≤ p * |Real.log u| := by positivity
  have h2 : 0 ≤ p * |Real.log v| := by positivity
  rcases eq_or_ne (u ^ (-p) - v ^ (-p)) 0 with h0 | h0
  · rw [h0, abs_zero, Real.log_zero]; linarith
  rcases le_total (v ^ (-p)) (u ^ (-p)) with h | h
  · have : Real.log |u ^ (-p) - v ^ (-p)| ≤ Real.log (u ^ (-p)) :=
      Real.log_le_log (abs_pos.2 h0) (by rw [abs_of_nonneg (by linarith)]; linarith)
    rw [Real.log_rpow hu] at this
    have := neg_abs_le (Real.log u)
    nlinarith
  · have : Real.log |u ^ (-p) - v ^ (-p)| ≤ Real.log (v ^ (-p)) :=
      Real.log_le_log (abs_pos.2 h0) (by rw [abs_of_nonpos (by linarith)]; linarith)
    rw [Real.log_rpow hv] at this
    have := neg_abs_le (Real.log v)
    nlinarith

/-- Lower bound on `(0, M]²`: `F(u,v) ≥ log (p M^{-p-1}) + log |u − v|` for `u ≠ v`. -/
theorem Fp_ge_box {p M u v : ℝ} (hp : 0 < p) (hu : 0 < u) (hv : 0 < v) (huM : u ≤ M) (hvM : v ≤ M)
    (huv : u ≠ v) : Real.log (p * M ^ (-p - 1)) + Real.log |u - v| ≤ Fp p u v := by
  wlog hlt : u < v generalizing u v
  · rw [Fp_comm, abs_sub_comm]
    exact this hv hu hvM huM huv.symm (lt_of_le_of_ne (not_lt.1 hlt) huv.symm)
  have hM : 0 < M := hu.trans_le huM
  have hmv := rpow_neg_sub_ge hp hu hlt.le
  have hb : M ^ (-p - 1) ≤ v ^ (-p - 1) := rpow_le_rpow_of_nonpos hv hvM (by linarith)
  have hpos : 0 < p * M ^ (-p - 1) * |u - v| := by
    have := rpow_pos_of_pos hM (-p - 1)
    have : 0 < |u - v| := abs_pos.2 (sub_ne_zero.2 huv)
    positivity
  rw [← Real.log_mul (by have := rpow_pos_of_pos hM (-p - 1); positivity) (abs_pos.2 (sub_ne_zero.2 huv)).ne', Fp]
  apply Real.log_le_log hpos
  rw [abs_sub_comm u v, abs_of_pos (sub_pos.2 hlt)]
  refine le_trans ?_ (hmv.trans (le_abs_self _))
  have := rpow_pos_of_pos hM (-p - 1)
  have : 0 ≤ v - u := by linarith
  nlinarith [mul_le_mul_of_nonneg_left hb hp.le]

/-! ### Integrability of `F` on `(Leb|(0,M])²` -/

/-- `Leb` restricted to `(0, M]`. -/
noncomputable abbrev boxM (M : ℝ) : Measure ℝ := volume.restrict (Ioc 0 M)

theorem intervalIntegrable_abs_log_abs (a b : ℝ) : IntervalIntegrable (fun t : ℝ => |Real.log t|) volume a b :=
  (intervalIntegral.intervalIntegrable_log' (a := a) (b := b)).abs

theorem slice_logdiff_integrable (M u : ℝ) : Integrable (fun v => abs (Real.log |u - v|)) (boxM M) := by
  simp_rw [Real.log_abs]
  rcases le_total 0 M with hM | hM
  · have := (intervalIntegrable_log_of_analytic (f := fun v => u - v)
      (fun x => analyticAt_const.sub analyticAt_id) 0 M).abs
    exact this.1
  · rw [boxM, Ioc_eq_empty (not_lt.2 hM)]; simp

theorem slice_logdiff_le {M u : ℝ} (hM : 0 ≤ M) (hu0 : 0 ≤ u) (huM : u ≤ M) :
    ∫ v, abs (Real.log |u - v|) ∂(boxM M) ≤ ∫ t in (-M)..M, |Real.log t| := by
  rw [boxM, ← intervalIntegral.integral_of_le hM]
  simp_rw [Real.log_abs]
  rw [intervalIntegral.integral_comp_sub_left (fun t => |Real.log t|) u, sub_zero]
  apply intervalIntegral.integral_mono_interval (by linarith) (by linarith) huM
    (Eventually.of_forall fun t => abs_nonneg _) (intervalIntegrable_abs_log_abs _ _)

theorem logdiff_integrable_box {M : ℝ} (hM : 0 ≤ M) :
    Integrable (fun z : ℝ × ℝ => abs (Real.log |z.1 - z.2|)) ((boxM M).prod (boxM M)) := by
  rw [integrable_prod_iff (by fun_prop : Measurable fun z : ℝ × ℝ => abs (Real.log |z.1 - z.2|)).aestronglyMeasurable]
  refine ⟨Eventually.of_forall fun u => slice_logdiff_integrable M u, ?_⟩
  refine Integrable.of_bound (C := ∫ t in (-M)..M, |Real.log t|) ?_ ?_
  · exact ((by fun_prop : Measurable fun z : ℝ × ℝ => abs (Real.log |z.1 - z.2|)).norm.stronglyMeasurable.integral_prod_right'
      (ν := boxM M)).aestronglyMeasurable
  · filter_upwards [ae_restrict_mem measurableSet_Ioc] with u hu
    simp_rw [Real.norm_eq_abs, abs_abs]
    rw [abs_of_nonneg (integral_nonneg fun _ => abs_nonneg _)]
    exact slice_logdiff_le hM hu.1.le hu.2

theorem abs_log_integrable_box (M : ℝ) : Integrable (fun u => |Real.log u|) (boxM M) := by
  rcases le_total 0 M with hM | hM
  · have := (intervalIntegral.intervalIntegrable_log' (a := 0) (b := M)).1.abs
    exact this
  · rw [boxM, Ioc_eq_empty (not_lt.2 hM)]; simp

/-- `F_p` is integrable on `(Leb|(0,M])²`. -/
theorem Fp_integrable_box {p M : ℝ} (hp : 0 < p) (hM : 0 < M) :
    Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) ((boxM M).prod (boxM M)) := by
  set c := |Real.log (p * M ^ (-p - 1))|
  have hG : Integrable (fun z : ℝ × ℝ => c + abs (Real.log |z.1 - z.2|) + p * |Real.log z.1| + p * |Real.log z.2|)
      ((boxM M).prod (boxM M)) :=
    (((integrable_const c).add (logdiff_integrable_box hM.le)).add
      (((abs_log_integrable_box M).const_mul p).comp_fst (boxM M))).add
      (((abs_log_integrable_box M).const_mul p).comp_snd (boxM M))
  refine Integrable.mono' hG (measurable_Fp p).aestronglyMeasurable ?_
  have hdiag : ((boxM M).prod (boxM M)) {z : ℝ × ℝ | z.1 = z.2} = 0 := by
    apply diag_null2
    intro x
    simp only [boxM]
    rw [Measure.restrict_apply (measurableSet_singleton x)]
    exact measure_mono_null inter_subset_left Real.volume_singleton
  have g1 := (Measure.quasiMeasurePreserving_fst (μ := boxM M) (ν := boxM M)).ae
    (ae_restrict_mem (μ := volume) measurableSet_Ioc)
  have g2 := (Measure.quasiMeasurePreserving_snd (μ := boxM M) (ν := boxM M)).ae
    (ae_restrict_mem (μ := volume) measurableSet_Ioc)
  have g3 : ∀ᵐ z ∂((boxM M).prod (boxM M)), z.1 ≠ z.2 := by rw [ae_iff]; simpa using hdiag
  filter_upwards [g1, g2, g3] with z h1 h2 h3
  rw [Real.norm_eq_abs, abs_le]
  have hup := Fp_le_box hp h1.1 h2.1 (u := z.1) (v := z.2)
  have hlo := Fp_ge_box hp h1.1 h2.1 h1.2 h2.2 h3 (M := M)
  have a1 := le_abs_self (Real.log (p * M ^ (-p - 1)))
  have a2 := neg_abs_le (Real.log (p * M ^ (-p - 1)))
  have a3 := neg_abs_le (Real.log |z.1 - z.2|)
  have a4 := abs_nonneg (Real.log |z.1 - z.2|)
  have a5 : 0 ≤ p * |Real.log z.1| := by positivity
  have a6 : 0 ≤ p * |Real.log z.2| := by positivity
  constructor <;> linarith

/-! ### Cells -/

/-- The cell `A_a = (a/n, (a+1)/n]` (0-based; Paper 1's `A_{a+1}`). -/
noncomputable def cell (n a : ℕ) : Set ℝ := Ioc ((a : ℝ) / n) (((a : ℝ) + 1) / n)

/-- `u_a = (a+1)/n`. -/
noncomputable def ucell (n a : ℕ) : ℝ := ((a : ℝ) + 1) / n

theorem cell_sub_box {n M a : ℕ} (hn : 1 ≤ n) (ha : a < M * n) : cell n a ⊆ Ioc 0 (M : ℝ) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  intro x hx
  refine ⟨lt_of_le_of_lt (by positivity) hx.1, hx.2.trans ?_⟩
  rw [div_le_iff₀ hn']
  have : (a : ℝ) + 1 ≤ (M * n : ℕ) := by exact_mod_cast ha
  push_cast at this; linarith

theorem rect_integrableOn {p : ℝ} (hp : 0 < p) {n M a b : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (ha : a < M * n)
    (hb : b < M * n) :
    IntegrableOn (fun z : ℝ × ℝ => Fp p z.1 z.2) (cell n a ×ˢ cell n b) ((volume : Measure ℝ).prod volume) := by
  have hM' : (0 : ℝ) < M := by exact_mod_cast hM
  have h := Fp_integrable_box hp hM'
  rw [boxM, Measure.prod_restrict] at h
  exact (show IntegrableOn _ (Ioc 0 (M : ℝ) ×ˢ Ioc 0 (M : ℝ)) _ from h).mono_set
    (Set.prod_mono (cell_sub_box hn ha) (cell_sub_box hn hb))

theorem logdiff_rect_integrableOn {n M a b : ℕ} (hn : 1 ≤ n) (_hM : 1 ≤ M) (ha : a < M * n) (hb : b < M * n) :
    IntegrableOn (fun z : ℝ × ℝ => Real.log |z.1 - z.2|) (cell n a ×ˢ cell n b) ((volume : Measure ℝ).prod volume) := by
  have hM' : (0 : ℝ) ≤ M := by exact_mod_cast (Nat.zero_le M)
  have h := (logdiff_integrable_box hM')
  rw [boxM, Measure.prod_restrict] at h
  have h2 := (show IntegrableOn _ (Ioc 0 (M : ℝ) ×ˢ Ioc 0 (M : ℝ)) _ from h).mono_set
    (Set.prod_mono (cell_sub_box hn ha) (cell_sub_box hn hb))
  exact Integrable.mono' h2
    (by fun_prop : Measurable fun z : ℝ × ℝ => Real.log |z.1 - z.2|).aestronglyMeasurable
    (Eventually.of_forall fun z => le_of_eq (Real.norm_eq_abs _))

/-- Inner integral over a cell: `∫_{A_b} log |u − v| dv ≥ (−log n − 3)/n`. -/
theorem cell_log_inner {n : ℕ} (hn : 1 ≤ n) (b : ℕ) (u : ℝ) :
    (-Real.log n - 3) / n ≤ ∫ v in cell n b, Real.log |u - v| := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [cell, ← intervalIntegral.integral_of_le (div_le_div_of_nonneg_right (by linarith) hn'.le)]
  have hsub := intervalIntegral.integral_comp_div_add (fun v => Real.log |u - v|) (a := 0) (b := 1)
    hn'.ne' ((b : ℝ) / n)
  rw [zero_div, zero_add, smul_eq_mul, show 1 / (n : ℝ) + b / n = ((b : ℝ) + 1) / n by ring] at hsub
  have hfin : ∫ v in (b : ℝ) / n..((b : ℝ) + 1) / n, Real.log |u - v| =
      (1 / n) * ∫ x in (0 : ℝ)..1, Real.log |u - (x / n + b / n)| := by
    rw [hsub]; field_simp
  rw [hfin, div_eq_mul_inv, mul_comm, one_div]
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  set s := n * u - b
  have hpt : ∀ x, Real.log |x - s| - Real.log n ≤ Real.log |u - (x / n + b / n)| := by
    intro x
    have e : u - (x / n + b / n) = -(x - s) / n := by simp only [s]; field_simp; ring
    rw [e, abs_div, abs_neg, Nat.abs_cast]
    rcases eq_or_ne (x - s) 0 with h0 | h0
    · rw [h0, abs_zero, zero_div, Real.log_zero]
      have := Real.log_natCast_nonneg n; linarith
    · rw [Real.log_div (abs_pos.2 h0).ne' hn'.ne']
  have i1 : IntervalIntegrable (fun x => Real.log |x - s| - Real.log n) volume 0 1 := by
    simp_rw [Real.log_abs]
    exact (intervalIntegrable_log_of_analytic (fun x => analyticAt_id.sub analyticAt_const) 0 1).sub
      intervalIntegrable_const
  have i2 : IntervalIntegrable (fun x => Real.log |u - (x / n + b / n)|) volume 0 1 := by
    simp_rw [Real.log_abs]
    exact intervalIntegrable_log_of_analytic (fun x => analyticAt_const.sub
      ((analyticAt_id.div analyticAt_const hn'.ne').add analyticAt_const)) 0 1
  have i0 : IntervalIntegrable (fun x => Real.log |x - s|) volume 0 1 := by
    simp_rw [Real.log_abs]
    exact intervalIntegrable_log_of_analytic (fun x => analyticAt_id.sub analyticAt_const) 0 1
  calc -Real.log n - 3 ≤ ∫ x in (0 : ℝ)..1, (Real.log |x - s| - Real.log n) := by
        rw [intervalIntegral.integral_sub i0 intervalIntegrable_const, intervalIntegral.integral_const]
        have := integral_log_abs_sub_ge s
        simp only [sub_zero, smul_eq_mul, one_mul]; linarith
    _ ≤ _ := intervalIntegral.integral_mono_on zero_le_one i1 i2 (fun x _ => hpt x)

theorem cell_real (n a : ℕ) (hn : 1 ≤ n) : (volume (cell n a)).toReal = 1 / n := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [cell, Real.volume_Ioc, show ((a : ℝ) + 1) / n - a / n = 1 / n by ring,
    ENNReal.toReal_ofReal (by positivity)]

theorem vol2_real_rect (n a b : ℕ) (hn : 1 ≤ n) :
    ((volume : Measure ℝ).prod volume).real (cell n a ×ˢ cell n b) = 1 / n * (1 / n) := by
  rw [Measure.real, Measure.prod_prod, ENNReal.toReal_mul, cell_real n a hn, cell_real n b hn]

theorem vol2_rect_ne_top (n a b : ℕ) : ((volume : Measure ℝ).prod volume) (cell n a ×ˢ cell n b) ≠ ⊤ := by
  rw [Measure.prod_prod]; exact ENNReal.mul_ne_top (by simp [cell]) (by simp [cell])

/-- Cell averages of `F` are `≥ log (p M^{-p-1}) − log n − 3`. -/
theorem cell_F_ge {p : ℝ} (hp : 0 < p) {n M a b : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (ha : a < M * n)
    (hb : b < M * n) :
    (Real.log (p * (M : ℝ) ^ (-p - 1)) - Real.log n - 3) / (n : ℝ) ^ 2 ≤
      ∫ z in cell n a ×ˢ cell n b, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  set c := Real.log (p * (M : ℝ) ^ (-p - 1))
  have hR : MeasurableSet (cell n a ×ˢ cell n b) := measurableSet_Ioc.prod measurableSet_Ioc
  have hlogI := logdiff_rect_integrableOn hn hM ha hb
  have hc : IntegrableOn (fun _ : ℝ × ℝ => c) (cell n a ×ˢ cell n b) ((volume : Measure ℝ).prod volume) :=
    integrableOn_const (vol2_rect_ne_top n a b) (by simp)
  -- pointwise lower bound off the diagonal
  have hdiag : ((volume : Measure ℝ).prod volume) {z : ℝ × ℝ | z.1 = z.2} = 0 :=
    diag_null2 (fun x => Real.volume_singleton)
  have hle : ∫ z in cell n a ×ˢ cell n b, (c + Real.log |z.1 - z.2|) ∂((volume : Measure ℝ).prod volume) ≤
      ∫ z in cell n a ×ˢ cell n b, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) := by
    apply setIntegral_mono_ae_restrict (hc.add hlogI) (rect_integrableOn hp hn hM ha hb)
    have g : ∀ᵐ z ∂((volume : Measure ℝ).prod volume), z.1 ≠ z.2 := by rw [ae_iff]; simpa using hdiag
    rw [Filter.EventuallyLE, ae_restrict_iff' hR]
    filter_upwards [g] with z hz hzR
    simp only [Pi.add_apply]
    exact Fp_ge_box hp (lt_of_le_of_lt (by positivity) hzR.1.1) (lt_of_le_of_lt (by positivity) hzR.2.1)
      (cell_sub_box hn ha hzR.1).2 (cell_sub_box hn hb hzR.2).2 hz
  refine le_trans ?_ hle
  rw [integral_add hc hlogI, setIntegral_const, vol2_real_rect n a b hn, smul_eq_mul, setIntegral_prod _ hlogI]
  have hin : ∀ u ∈ cell n a, (-Real.log n - 3) / n ≤ ∫ v in cell n b, Real.log |(u, v).1 - (u, v).2| :=
    fun u _ => cell_log_inner hn b u
  have hout : ∫ u in cell n a, (-Real.log n - 3) / n ≤
      ∫ u in cell n a, ∫ v in cell n b, Real.log |(u, v).1 - (u, v).2| := by
    have hint : IntegrableOn (fun u => ∫ v in cell n b, Real.log |(u, v).1 - (u, v).2|) (cell n a) := by
      have := hlogI
      rw [IntegrableOn, ← Measure.prod_restrict] at this
      exact this.integral_prod_left
    exact setIntegral_mono_on (integrableOn_const (by simp [cell]) (by simp)) hint measurableSet_Ioc hin
  rw [setIntegral_const, Measure.real, cell_real n a hn, smul_eq_mul] at hout
  have e2 : (c - Real.log n - 3) / (n : ℝ) ^ 2 = 1 / n * (1 / n) * c + 1 / n * ((-Real.log n - 3) / n) := by
    field_simp; ring
  rw [e2]
  linarith

/-- Mean value bound: `a^{-p} − b^{-p} ≤ p a^{-p-1} (b − a)` for `0 < a ≤ b`. -/
theorem rpow_neg_sub_le {p a b : ℝ} (hp : 0 < p) (ha : 0 < a) (hab : a ≤ b) :
    a ^ (-p) - b ^ (-p) ≤ p * a ^ (-p - 1) * (b - a) := by
  rcases hab.eq_or_lt with rfl | hab
  · simp
  have hcont : ContinuousOn (fun x : ℝ => x ^ (-p)) (Icc a b) := fun x hx =>
    (continuousAt_rpow_const x (-p) (Or.inl (ha.trans_le hx.1).ne')).continuousWithinAt
  have hder : ∀ x ∈ Ioo a b, HasDerivAt (fun x : ℝ => x ^ (-p)) (-p * x ^ (-p - 1)) x := fun x hx =>
    Real.hasDerivAt_rpow_const (Or.inl (ha.trans hx.1).ne')
  obtain ⟨c, hc, hcd⟩ := exists_hasDerivAt_eq_slope (fun x : ℝ => x ^ (-p)) (fun x => -p * x ^ (-p - 1))
    hab hcont hder
  have hc0 : 0 < c := ha.trans hc.1
  have hca : c ^ (-p - 1) ≤ a ^ (-p - 1) := rpow_le_rpow_of_nonpos ha hc.1.le (by linarith)
  have hba : 0 < b - a := by linarith
  rw [eq_div_iff hba.ne'] at hcd
  nlinarith [mul_le_mul_of_nonneg_right hca (mul_nonneg hp.le hba.le)]

/-- Non-adjacent cells (Paper 1 Lemma 4.1): `F(u_a, u_b) ≤ n² I(a,b) + 1/(b − a − 1)` for `b ≥ a + 2`. -/
theorem far_cell {p : ℝ} (hp : 0 < p) {n M a b : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (ha : a < M * n)
    (hb : b < M * n) (hab : a + 2 ≤ b) :
    Fp p (ucell n a) (ucell n b) ≤
      (n : ℝ) ^ 2 * ∫ z in cell n a ×ˢ cell n b, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) +
        1 / ((b : ℝ) - a - 1) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have habr : (a : ℝ) + 2 ≤ b := by exact_mod_cast hab
  set x := ucell n a
  set y0 := (b : ℝ) / n
  set y1 := ucell n b
  have hx : 0 < x := by simp only [x, ucell]; positivity
  have hxy : x < y0 := by simp only [x, y0, ucell]; rw [div_lt_div_iff_of_pos_right hn']; linarith
  have hy01 : y1 = y0 + 1 / n := by simp only [y1, y0, ucell]; ring
  have hy0 : 0 < y0 := hx.trans hxy
  -- lower bound of the cell integral
  have hR : MeasurableSet (cell n a ×ˢ cell n b) := measurableSet_Ioc.prod measurableSet_Ioc
  have hI := setIntegral_ge_of_const_le (c := Fp p x y0) hR (vol2_rect_ne_top n a b)
    (fun z hz => Fp_le_of hp (lt_of_le_of_lt (by positivity) hz.1.1) hz.1.2 hxy hz.2.1.le)
    (rect_integrableOn hp hn hM ha hb)
  rw [vol2_real_rect n a b hn, smul_eq_mul] at hI
  -- the point difference
  have hD0 : 0 < x ^ (-p) - y0 ^ (-p) := sub_pos.2 (rpow_lt_rpow_of_neg hx hxy (by linarith))
  have hy01le : y0 ≤ y1 := by
    rw [hy01]; have : 0 < 1 / (n : ℝ) := by positivity
    linarith
  have hΔ : y0 ^ (-p) - y1 ^ (-p) ≤ p * y0 ^ (-p - 1) * (1 / n) := by
    have := rpow_neg_sub_le hp hy0 hy01le
    rw [hy01, add_sub_cancel_left] at this
    rw [hy01]; exact this
  have hD0lo : p * y0 ^ (-p - 1) * (((b : ℝ) - a - 1) / n) ≤ x ^ (-p) - y0 ^ (-p) := by
    have := rpow_neg_sub_ge hp hx hxy.le
    have e : y0 - x = ((b : ℝ) - a - 1) / n := by simp only [y0, x, ucell]; field_simp; ring
    rwa [e] at this
  have hpt : Fp p x y1 - Fp p x y0 ≤ 1 / ((b : ℝ) - a - 1) := by
    have hy0' : y0 ^ (-p) - y1 ^ (-p) ≥ 0 := by
      have := rpow_le_rpow_of_nonpos hy0 hy01le (by linarith : -p ≤ 0)
      linarith
    have hD1 : 0 < x ^ (-p) - y1 ^ (-p) := by linarith
    unfold Fp
    rw [abs_of_pos hD1, abs_of_pos hD0, ← Real.log_div hD1.ne' hD0.ne']
    have hlog := Real.log_le_sub_one_of_pos (div_pos hD1 hD0)
    have hq : (x ^ (-p) - y1 ^ (-p)) / (x ^ (-p) - y0 ^ (-p)) - 1 =
        (y0 ^ (-p) - y1 ^ (-p)) / (x ^ (-p) - y0 ^ (-p)) := by field_simp; ring
    rw [hq] at hlog
    refine hlog.trans ?_
    have hbpos : (0 : ℝ) < (b : ℝ) - a - 1 := by linarith
    have hk : 0 < p * y0 ^ (-p - 1) := mul_pos hp (rpow_pos_of_pos hy0 _)
    rw [div_le_div_iff₀ hD0 hbpos]
    calc (y0 ^ (-p) - y1 ^ (-p)) * ((b : ℝ) - a - 1) ≤ p * y0 ^ (-p - 1) * (1 / n) * ((b : ℝ) - a - 1) :=
          mul_le_mul_of_nonneg_right hΔ hbpos.le
      _ = p * y0 ^ (-p - 1) * (((b : ℝ) - a - 1) / n) := by ring
      _ ≤ 1 * (x ^ (-p) - y0 ^ (-p)) := by linarith
  have hI' : Fp p x y0 ≤ (n : ℝ) ^ 2 * ∫ z in cell n a ×ˢ cell n b, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) := by
    have := mul_le_mul_of_nonneg_left hI (sq_nonneg (n : ℝ))
    calc Fp p x y0 = (n : ℝ) ^ 2 * (1 / n * (1 / n) * Fp p x y0) := by field_simp
      _ ≤ _ := this
  linarith

/-- The per-point error for adjacent cells. -/
noncomputable def eAdj (p : ℝ) (n M : ℕ) : ℝ :=
  2 * p * (Real.log n + |Real.log M|) + |Real.log (p * (M : ℝ) ^ (-p - 1))| + Real.log n + 3

theorem eAdj_nonneg {p : ℝ} (hp : 0 < p) (n M : ℕ) : 0 ≤ eAdj p n M := by
  unfold eAdj
  have := Real.log_natCast_nonneg n
  positivity

theorem abs_log_ucell_le {n M a : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (ha : a < M * n) :
    |Real.log (ucell n a)| ≤ Real.log n + |Real.log M| := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hM' : (1 : ℝ) ≤ M := by exact_mod_cast hM
  have hu : 0 < ucell n a := by unfold ucell; positivity
  have h1 : 1 / (n : ℝ) ≤ ucell n a := by
    unfold ucell; exact div_le_div_of_nonneg_right (by linarith [(Nat.cast_nonneg a : (0:ℝ) ≤ a)]) hn'.le
  have h2 : ucell n a ≤ M := by
    unfold ucell; rw [div_le_iff₀ hn']
    have : (a : ℝ) + 1 ≤ (M * n : ℕ) := by exact_mod_cast ha
    push_cast at this; linarith
  have l1 : -Real.log n ≤ Real.log (ucell n a) := by
    have := Real.log_le_log (by positivity) h1
    rwa [one_div, Real.log_inv] at this
  have l2 : Real.log (ucell n a) ≤ Real.log M := Real.log_le_log hu h2
  have := le_abs_self (Real.log M)
  have := abs_nonneg (Real.log M)
  have := Real.log_natCast_nonneg n
  rw [abs_le]; constructor <;> linarith

/-- Any pair of cells: `F(u_a, u_b) ≤ n² I(a,b) + eAdj`. -/
theorem any_cell {p : ℝ} (hp : 0 < p) {n M a b : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (ha : a < M * n)
    (hb : b < M * n) :
    Fp p (ucell n a) (ucell n b) ≤
      (n : ℝ) ^ 2 * ∫ z in cell n a ×ˢ cell n b, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) + eAdj p n M := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hup := Fp_le_box hp (by unfold ucell; positivity : 0 < ucell n a) (by unfold ucell; positivity : 0 < ucell n b)
  have h1 := abs_log_ucell_le hn hM ha
  have h2 := abs_log_ucell_le hn hM hb
  have hI := mul_le_mul_of_nonneg_left (cell_F_ge hp hn hM ha hb) (sq_nonneg (n : ℝ))
  rw [mul_div_cancel₀ _ (by positivity)] at hI
  have := neg_abs_le (Real.log (p * (M : ℝ) ^ (-p - 1)))
  unfold eAdj
  nlinarith

/-- `I(b, a) = I(a, b)`. -/
theorem rectI_swap {p : ℝ} (n a b : ℕ) :
    ∫ z in cell n b ×ˢ cell n a, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) =
      ∫ z in cell n a ×ˢ cell n b, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) := by
  have hR : MeasurableSet (cell n a ×ˢ cell n b) := measurableSet_Ioc.prod measurableSet_Ioc
  have hR' : MeasurableSet (cell n b ×ˢ cell n a) := measurableSet_Ioc.prod measurableSet_Ioc
  rw [← integral_indicator hR, ← integral_indicator hR']
  have e : (cell n b ×ˢ cell n a).indicator (fun z : ℝ × ℝ => Fp p z.1 z.2) =
      fun z => (cell n a ×ˢ cell n b).indicator (fun z : ℝ × ℝ => Fp p z.1 z.2) z.swap := by
    funext z
    by_cases hz : z.swap ∈ cell n a ×ˢ cell n b
    · have hz' : z ∈ cell n b ×ˢ cell n a := ⟨hz.2, hz.1⟩
      rw [indicator_of_mem hz', indicator_of_mem hz]; exact Fp_comm p _ _
    · have hz' : z ∉ cell n b ×ˢ cell n a := fun h => hz ⟨h.2, h.1⟩
      rw [indicator_of_notMem hz', indicator_of_notMem hz]
  rw [e]
  exact integral_prod_swap (μ := (volume : Measure ℝ)) (ν := volume)
    ((cell n a ×ˢ cell n b).indicator fun z : ℝ × ℝ => Fp p z.1 z.2)

/-! ### The cell measure and Lemma 4.1 -/

/-- `⋃_{a ∈ S} A_a`. -/
noncomputable def cellU (n : ℕ) (S : Finset ℕ) : Set ℝ := ⋃ a ∈ S, cell n a

/-- The cell measure `μ̄_S` (density 1 on `⋃_{a ∈ S} A_a`). -/
noncomputable def muBar (n : ℕ) (S : Finset ℕ) : Measure ℝ := volume.restrict (cellU n S)

theorem cell_disjoint {n a b : ℕ} (hn : 1 ≤ n) (hab : a ≠ b) : Disjoint (cell n a) (cell n b) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  wlog hlt : a < b generalizing a b
  · exact (this hab.symm (lt_of_le_of_ne (not_lt.1 hlt) hab.symm)).symm
  rw [Set.disjoint_left]
  intro x hxa hxb
  have : ((a : ℝ) + 1) / n ≤ (b : ℝ) / n := by
    apply div_le_div_of_nonneg_right _ hn'.le
    have : (a : ℝ) + 1 ≤ b := by exact_mod_cast hlt
    exact this
  exact absurd (hxa.2.trans this) (not_le.2 hxb.1)

theorem cellU_sub_box {n M : ℕ} (hn : 1 ≤ n) {S : Finset ℕ} (hS : S ⊆ Finset.range (M * n)) :
    cellU n S ⊆ Ioc 0 (M : ℝ) := by
  intro x hx
  simp only [cellU, mem_iUnion] at hx
  obtain ⟨a, ha, hx⟩ := hx
  exact cell_sub_box hn (Finset.mem_range.1 (hS ha)) hx

theorem muBar_le_box {n M : ℕ} (hn : 1 ≤ n) {S : Finset ℕ} (hS : S ⊆ Finset.range (M * n)) :
    muBar n S ≤ boxM M := Measure.restrict_mono (cellU_sub_box hn hS) le_rfl

theorem Jp_muBar {p : ℝ} (hp : 0 < p) {n M : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) {S : Finset ℕ}
    (hS : S ⊆ Finset.range (M * n)) :
    Jp p (muBar n S) = ∑ q ∈ S ×ˢ S, ∫ z in cell n q.1 ×ˢ cell n q.2, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume) := by
  rw [Jp, muBar, Measure.prod_restrict]
  have hU : cellU n S ×ˢ cellU n S = ⋃ q ∈ S ×ˢ S, cell n q.1 ×ˢ cell n q.2 := by
    ext z; simp only [cellU, mem_prod, mem_iUnion, Finset.mem_product, exists_prop, Prod.exists]
    constructor
    · rintro ⟨⟨a, ha, h1⟩, ⟨b, hb, h2⟩⟩; exact ⟨a, b, ⟨ha, hb⟩, h1, h2⟩
    · rintro ⟨a, b, ⟨ha, hb⟩, h1, h2⟩; exact ⟨⟨a, ha, h1⟩, ⟨b, hb, h2⟩⟩
  rw [hU, integral_biUnion_finset]
  · intro q _; exact measurableSet_Ioc.prod measurableSet_Ioc
  · intro q _ q' _ hne
    simp only [Function.onFun]
    rw [Set.disjoint_prod]
    by_cases h1 : q.1 = q'.1
    · right; exact cell_disjoint hn (fun h2 => hne (Prod.ext h1 h2))
    · left; exact cell_disjoint hn h1
  · intro q hq
    rw [Finset.mem_product] at hq
    exact rect_integrableOn hp hn hM (Finset.mem_range.1 (hS hq.1)) (Finset.mem_range.1 (hS hq.2))

/-- Symmetric double sums: `Σ_{S×S} f = 2 Σ_{pairs S} f + Σ_S f(a,a)`. -/
theorem sum_prod_symm (S : Finset ℕ) (f : ℕ × ℕ → ℝ) (hf : ∀ a b, f (a, b) = f (b, a)) :
    ∑ q ∈ S ×ˢ S, f q = 2 * ∑ q ∈ pairs S, f q + ∑ a ∈ S, f (a, a) := by
  rw [← Finset.sum_filter_add_sum_filter_not (S ×ˢ S) (fun q => q.1 < q.2)]
  rw [← Finset.sum_filter_add_sum_filter_not ((S ×ˢ S).filter fun q => ¬ q.1 < q.2) (fun q => q.2 < q.1)]
  have h1 : ∑ q ∈ ((S ×ˢ S).filter fun q => ¬ q.1 < q.2).filter (fun q => q.2 < q.1), f q =
      ∑ q ∈ pairs S, f q := by
    apply Finset.sum_nbij' Prod.swap Prod.swap
    · intro q hq
      simp only [pairs, Finset.mem_filter, Finset.mem_product, Prod.fst_swap, Prod.snd_swap] at hq ⊢
      exact ⟨⟨hq.1.1.2, hq.1.1.1⟩, hq.2⟩
    · intro q hq
      simp only [pairs, Finset.mem_filter, Finset.mem_product, Prod.fst_swap, Prod.snd_swap] at hq ⊢
      exact ⟨⟨⟨hq.1.2, hq.1.1⟩, not_lt.2 hq.2.le⟩, hq.2⟩
    · intro q _; simp
    · intro q _; simp
    · intro q _; obtain ⟨a, b⟩ := q; exact hf a b
  have h2 : ∑ q ∈ ((S ×ˢ S).filter fun q => ¬ q.1 < q.2).filter (fun q => ¬ q.2 < q.1), f q =
      ∑ a ∈ S, f (a, a) := by
    apply Finset.sum_nbij' (fun q => q.1) (fun a => (a, a))
    · intro q hq
      simp only [Finset.mem_filter, Finset.mem_product] at hq
      exact hq.1.1.1
    · intro a ha
      simp only [Finset.mem_filter, Finset.mem_product, lt_irrefl, not_false_eq_true, and_true]
      exact ⟨ha, ha⟩
    · intro q hq
      simp only [Finset.mem_filter, Finset.mem_product] at hq
      obtain ⟨a, b⟩ := q
      simp only at hq ⊢
      have : a = b := le_antisymm (not_lt.1 hq.2) (not_lt.1 hq.1.2)
      rw [this]
    · intro a _; rfl
    · intro q hq
      simp only [Finset.mem_filter, Finset.mem_product] at hq
      obtain ⟨a, b⟩ := q
      simp only at hq ⊢
      have : a = b := le_antisymm (not_lt.1 hq.2) (not_lt.1 hq.1.2)
      rw [this]
  rw [h1, h2]
  unfold pairs
  ring

/-- The pair error `e(a,b)`: `1/(b−a−1)` for non-adjacent, `eAdj` for adjacent cells. -/
noncomputable def ePair (p : ℝ) (n M : ℕ) (q : ℕ × ℕ) : ℝ :=
  if q.1 + 2 ≤ q.2 then 1 / ((q.2 : ℝ) - q.1 - 1) else eAdj p n M

theorem harmonic_sum_le {a K : ℕ} (T : Finset ℕ) (hT : ∀ b ∈ T, a + 2 ≤ b ∧ b < K) :
    ∑ b ∈ T, 1 / ((b : ℝ) - a - 1) ≤ 1 + Real.log K := by
  have hcast : ∀ b ∈ T, 1 / ((b : ℝ) - a - 1) = 1 / (((b - a - 1 : ℕ) : ℕ) : ℝ) := by
    intro b hb
    have := (hT b hb).1
    congr 1; rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; push_cast; ring
  rw [Finset.sum_congr rfl hcast]
  have hinj : Set.InjOn (fun b => b - a - 1) (T : Set ℕ) := by
    intro x hx y hy hxy
    have := (hT x hx).1; have := (hT y hy).1
    simp only at hxy; omega
  rw [← Finset.sum_image (f := fun j : ℕ => 1 / (j : ℝ)) hinj]
  have hsub : T.image (fun b => b - a - 1) ⊆ Finset.Icc 1 K := by
    intro j hj
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.1 hj
    have := hT b hb
    rw [Finset.mem_Icc]; omega
  calc ∑ j ∈ T.image (fun b => b - a - 1), 1 / (j : ℝ) ≤ ∑ j ∈ Finset.Icc 1 K, 1 / (j : ℝ) :=
        Finset.sum_le_sum_of_subset_of_nonneg hsub (fun j _ _ => by positivity)
    _ = (harmonic K : ℝ) := by rw [harmonic_eq_sum_Icc]; push_cast; simp [one_div]
    _ ≤ 1 + Real.log K := harmonic_le_one_add_log K

theorem sum_ePair_le {p : ℝ} (hp : 0 < p) {n M : ℕ} {S : Finset ℕ} (hS : S ⊆ Finset.range (M * n)) :
    ∑ q ∈ pairs S, ePair p n M q ≤ S.card * (1 + Real.log ((M * n : ℕ) : ℝ) + eAdj p n M) := by
  unfold pairs
  rw [Finset.sum_filter, Finset.sum_product]
  have hper : ∀ a ∈ S, ∑ b ∈ S, (if a < b then ePair p n M (a, b) else 0) ≤
      1 + Real.log ((M * n : ℕ) : ℝ) + eAdj p n M := by
    intro a ha
    have hsplit : ∀ b ∈ S, (if a < b then ePair p n M (a, b) else 0) =
        (if a + 2 ≤ b then 1 / ((b : ℝ) - a - 1) else 0) + (if b = a + 1 then eAdj p n M else 0) := by
      intro b _
      unfold ePair; simp only
      by_cases h1 : a + 2 ≤ b
      · rw [if_pos (by omega), if_pos h1, if_pos h1, if_neg (by omega), add_zero]
      · by_cases h2 : b = a + 1
        · rw [if_pos (by omega), if_neg h1, if_neg h1, if_pos h2, zero_add]
        · rw [if_neg (by omega), if_neg h1, if_neg h2, add_zero]
    rw [Finset.sum_congr rfl hsplit, Finset.sum_add_distrib, ← Finset.sum_filter, Finset.sum_ite_eq']
    have hh := harmonic_sum_le (a := a) (K := M * n) (S.filter fun b => a + 2 ≤ b) (fun b hb => by
      rw [Finset.mem_filter] at hb; exact ⟨hb.2, Finset.mem_range.1 (hS hb.1)⟩)
    have he := eAdj_nonneg hp n M
    split_ifs <;> linarith
  calc ∑ a ∈ S, ∑ b ∈ S, (if a < b then ePair p n M (a, b) else 0)
      ≤ ∑ a ∈ S, (1 + Real.log ((M * n : ℕ) : ℝ) + eAdj p n M) := Finset.sum_le_sum hper
    _ = _ := by rw [Finset.sum_const, nsmul_eq_mul]

/-- Constant of Lemma 4.1 (per point). -/
noncomputable def eDisc (p : ℝ) (n M : ℕ) : ℝ :=
  (|Real.log (p * (M : ℝ) ^ (-p - 1))| + Real.log n + 3) + 2 * (1 + Real.log ((M * n : ℕ) : ℝ) + eAdj p n M)

/-- **Lemma 4.1 (discretisation)**: for `S ⊆ {0,…,Mn−1}`,
`2 Σ_{a<b ∈ S} F(u_a, u_b) ≤ n² 𝒥_p(μ̄_S) + |S| · eDisc`, with `eDisc = O(log n)` for fixed `M`. -/
theorem disc_upper {p : ℝ} (hp : 0 < p) {n M : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) {S : Finset ℕ}
    (hS : S ⊆ Finset.range (M * n)) :
    2 * ∑ q ∈ pairs S, Fp p (ucell n q.1) (ucell n q.2) ≤
      (n : ℝ) ^ 2 * Jp p (muBar n S) + S.card * eDisc p n M := by
  set I : ℕ × ℕ → ℝ := fun q => ∫ z in cell n q.1 ×ˢ cell n q.2, Fp p z.1 z.2 ∂((volume : Measure ℝ).prod volume)
  have hJ : Jp p (muBar n S) = 2 * ∑ q ∈ pairs S, I q + ∑ a ∈ S, I (a, a) := by
    rw [Jp_muBar hp hn hM hS]
    exact sum_prod_symm S I (fun a b => (rectI_swap n a b).symm)
  have hmem : ∀ q ∈ pairs S, q.1 < M * n ∧ q.2 < M * n ∧ q.1 < q.2 := by
    intro q hq
    simp only [pairs, Finset.mem_filter, Finset.mem_product] at hq
    exact ⟨Finset.mem_range.1 (hS hq.1.1), Finset.mem_range.1 (hS hq.1.2), hq.2⟩
  have hpair : ∀ q ∈ pairs S, Fp p (ucell n q.1) (ucell n q.2) ≤ (n : ℝ) ^ 2 * I q + ePair p n M q := by
    intro q hq
    obtain ⟨h1, h2, h3⟩ := hmem q hq
    unfold ePair
    split_ifs with hfar
    · exact far_cell hp hn hM h1 h2 hfar
    · exact any_cell hp hn hM h1 h2
  have hdiag : ∀ a ∈ S, -(|Real.log (p * (M : ℝ) ^ (-p - 1))| + Real.log n + 3) ≤ (n : ℝ) ^ 2 * I (a, a) := by
    intro a ha
    have ha' := Finset.mem_range.1 (hS ha)
    have := mul_le_mul_of_nonneg_left (cell_F_ge hp hn hM ha' ha') (sq_nonneg (n : ℝ))
    have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    rw [mul_div_cancel₀ _ (by positivity)] at this
    have := neg_abs_le (Real.log (p * (M : ℝ) ^ (-p - 1)))
    simp only [I]; linarith
  have hsum1 : ∑ q ∈ pairs S, Fp p (ucell n q.1) (ucell n q.2) ≤
      (n : ℝ) ^ 2 * ∑ q ∈ pairs S, I q + ∑ q ∈ pairs S, ePair p n M q := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]; exact Finset.sum_le_sum hpair
  have hsum2 : -(S.card * (|Real.log (p * (M : ℝ) ^ (-p - 1))| + Real.log n + 3)) ≤
      (n : ℝ) ^ 2 * ∑ a ∈ S, I (a, a) := by
    rw [Finset.mul_sum]
    calc -(S.card * (|Real.log (p * (M : ℝ) ^ (-p - 1))| + Real.log n + 3)) =
        ∑ a ∈ S, -(|Real.log (p * (M : ℝ) ^ (-p - 1))| + Real.log n + 3) := by
          rw [Finset.sum_const, nsmul_eq_mul]; ring
      _ ≤ _ := Finset.sum_le_sum hdiag
  have hsum3 := sum_ePair_le hp hS (n := n)
  rw [hJ]
  unfold eDisc
  nlinarith

end JacobiAsym
