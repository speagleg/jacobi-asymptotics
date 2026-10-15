import JacobiAsym.HallConst

/-! # Plan 60, stage S2a: the logarithmic potential of the arcsine law (Paper 1 Lemma 3.2, G2 Lemma B0)

The arcsine law `ω_β` on `[0, β]` is the image of `dφ/π` on `[0, π]` under `φ ↦ arcX β φ = β(1 − cos φ)/2`.
`arcsine_pot`: `∫₀^π log |arcX β φ − y| dφ = π log (β/4)` for `0 ≤ y ≤ β`; `arcsine_pot_ge`: `≥` for `y ≥ β`.
Proof: `cos φ₀ − cos φ = −2 sin((φ₀+φ)/2) sin((φ₀−φ)/2)`, π-periodicity of `log |sin|` and
`∫₀^π log sin = −π log 2` (Mathlib), in place of the Fourier series used in the paper. -/

open Real Set intervalIntegral MeasureTheory
open scoped Interval

namespace JacobiAsym

/-- `arcX β φ = β (1 − cos φ) / 2`. -/
noncomputable def arcX (β φ : ℝ) : ℝ := β * (1 - cos φ) / 2

theorem arcX_nonneg {β : ℝ} (hβ : 0 ≤ β) (φ : ℝ) : 0 ≤ arcX β φ := by
  unfold arcX; have := cos_le_one φ; have : 0 ≤ 1 - cos φ := by linarith
  positivity

theorem arcX_le {β : ℝ} (hβ : 0 ≤ β) (φ : ℝ) : arcX β φ ≤ β := by
  unfold arcX; have := neg_one_le_cos φ; nlinarith

/-- `log ∘ f` is interval integrable for real-analytic `f`. -/
theorem intervalIntegrable_log_of_analytic {f : ℝ → ℝ} (hf : ∀ x, AnalyticAt ℝ f x) (a b : ℝ) :
    IntervalIntegrable (fun x => Real.log (f x)) volume a b :=
  (show AnalyticOnNhd ℝ f [[a, b]] from fun x _ => hf x).meromorphicOn.intervalIntegrable_log

theorem intervalIntegrable_log_arcX_sub (β y a b : ℝ) :
    IntervalIntegrable (fun φ => Real.log (arcX β φ - y)) volume a b := by
  apply intervalIntegrable_log_of_analytic
  intro x
  unfold arcX
  exact ((analyticAt_const.mul (analyticAt_const.sub analyticAt_cos)).div analyticAt_const two_ne_zero).sub
    analyticAt_const

/-- `∫_t^{t+π} log sin = −π log 2` for every `t` (π-periodicity of `log |sin|`). -/
theorem integral_log_sin_period (t : ℝ) : ∫ x in t..t + π, Real.log (sin x) = -Real.log 2 * π := by
  have hper : Function.Periodic (fun x => Real.log (sin x)) π := by
    intro x; simp only [sin_add_pi, Real.log_neg_eq_log]
  have := hper.intervalIntegral_add_eq t 0
  rw [this, zero_add, integral_log_sin_zero_pi]

/-- **Arcsine potential** (Paper 1 Lemma 3.2): `∫₀^π log |β(1 − cos φ)/2 − y| dφ = π log (β/4)` for `0 ≤ y ≤ β`. -/
theorem arcsine_pot {β y : ℝ} (hβ : 0 < β) (hy0 : 0 ≤ y) (hyβ : y ≤ β) :
    ∫ φ in (0 : ℝ)..π, Real.log (arcX β φ - y) = π * Real.log (β / 4) := by
  set φ0 := arccos (1 - 2 * y / β) with hφ0
  have hc0 : cos φ0 = 1 - 2 * y / β := by
    rw [hφ0, cos_arccos]
    · have : 2 * y / β ≤ 2 := by rw [div_le_iff₀ hβ]; linarith
      linarith
    · have : 0 ≤ 2 * y / β := by positivity
      linarith
  -- the factorisation
  have hfac : ∀ φ, arcX β φ - y = -β * (sin ((φ0 + φ) / 2) * sin ((φ0 - φ) / 2)) := by
    intro φ
    have h := cos_sub_cos φ0 φ
    have e : arcX β φ - y = β / 2 * (cos φ0 - cos φ) := by
      unfold arcX; rw [hc0]; field_simp; ring
    rw [e, h]; ring
  -- a.e. identity of the logarithms
  set Z := {φ : ℝ | sin ((φ0 + φ) / 2) = 0} ∪ {φ : ℝ | sin ((φ0 - φ) / 2) = 0} with hZ
  have hZc : Z.Countable := by
    apply Set.Countable.union
    · apply (Set.countable_range (fun n : ℤ => 2 * (n : ℝ) * π - φ0)).mono
      intro φ hφ
      obtain ⟨n, hn⟩ := sin_eq_zero_iff.1 hφ
      exact ⟨n, by simp only; linarith⟩
    · apply (Set.countable_range (fun n : ℤ => φ0 - 2 * (n : ℝ) * π)).mono
      intro φ hφ
      obtain ⟨n, hn⟩ := sin_eq_zero_iff.1 hφ
      exact ⟨n, by simp only; linarith⟩
  have hae : ∀ᵐ φ ∂(volume : Measure ℝ), φ ∈ Ι (0 : ℝ) π →
      Real.log (arcX β φ - y) =
        Real.log β + (Real.log (sin ((φ0 + φ) / 2)) + Real.log (sin ((φ0 - φ) / 2))) := by
    have h0 : volume Z = 0 := hZc.measure_zero volume
    filter_upwards [measure_eq_zero_iff_ae_notMem.1 h0] with φ hφ _
    simp only [hZ, mem_union, mem_ofPred_eq, not_or] at hφ
    rw [hfac, Real.log_mul (by simpa using hβ.ne') (mul_ne_zero hφ.1 hφ.2), Real.log_neg_eq_log,
      Real.log_mul hφ.1 hφ.2]
  rw [integral_congr_ae hae]
  have i1 : IntervalIntegrable (fun φ => Real.log (sin ((φ0 + φ) / 2))) volume 0 π :=
    intervalIntegrable_log_of_analytic (fun x =>
      analyticAt_sin.comp ((analyticAt_const.add analyticAt_id).div analyticAt_const two_ne_zero)) _ _
  have i2 : IntervalIntegrable (fun φ => Real.log (sin ((φ0 - φ) / 2))) volume 0 π :=
    intervalIntegrable_log_of_analytic (fun x =>
      analyticAt_sin.comp ((analyticAt_const.sub analyticAt_id).div analyticAt_const two_ne_zero)) _ _
  rw [integral_add intervalIntegrable_const (i1.add i2), integral_add i1 i2]
  -- the two log-sin integrals
  have e1 : ∫ φ in (0 : ℝ)..π, Real.log (sin ((φ0 + φ) / 2)) =
      2 * ∫ x in φ0 / 2..φ0 / 2 + π / 2, Real.log (sin x) := by
    have : (fun φ => Real.log (sin ((φ0 + φ) / 2))) = fun φ => Real.log (sin (φ / 2 + φ0 / 2)) := by
      funext φ; ring_nf
    rw [this, integral_comp_div_add (fun x => Real.log (sin x)) two_ne_zero, smul_eq_mul]
    ring_nf
  have e2 : ∫ φ in (0 : ℝ)..π, Real.log (sin ((φ0 - φ) / 2)) =
      2 * ∫ x in φ0 / 2 - π / 2..φ0 / 2, Real.log (sin x) := by
    have : (fun φ => Real.log (sin ((φ0 - φ) / 2))) = fun φ => Real.log (sin (φ / (-2) + φ0 / 2)) := by
      funext φ; ring_nf
    rw [this, integral_comp_div_add (fun x => Real.log (sin x)) (by norm_num : (-2 : ℝ) ≠ 0), smul_eq_mul,
      integral_symm]
    ring_nf
  have hsum : (∫ x in φ0 / 2 - π / 2..φ0 / 2, Real.log (sin x)) +
      ∫ x in φ0 / 2..φ0 / 2 + π / 2, Real.log (sin x) = -Real.log 2 * π := by
    have ii : ∀ a b : ℝ, IntervalIntegrable (fun x => Real.log (sin x)) volume a b :=
      fun a b => intervalIntegrable_log_sin
    rw [integral_add_adjacent_intervals (ii _ _) (ii _ _)]
    have := integral_log_sin_period (φ0 / 2 - π / 2)
    rw [show φ0 / 2 - π / 2 + π = φ0 / 2 + π / 2 by ring] at this
    exact this
  rw [e1, e2, intervalIntegral.integral_const, smul_eq_mul, sub_zero]
  have h4 : Real.log (β / 4) = Real.log β - 2 * Real.log 2 := by
    rw [Real.log_div hβ.ne' (by norm_num), show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]; push_cast; ring
  rw [h4]
  linarith

/-- Outside the support the potential is larger: `∫₀^π log |arcX β φ − y| ≥ π log (β/4)` for `y ≥ β`. -/
theorem arcsine_pot_ge {β y : ℝ} (hβ : 0 < β) (hyβ : β ≤ y) :
    π * Real.log (β / 4) ≤ ∫ φ in (0 : ℝ)..π, Real.log (arcX β φ - y) := by
  rw [← arcsine_pot hβ hβ.le le_rfl]
  apply integral_mono_ae_restrict pi_pos.le (intervalIntegrable_log_arcX_sub _ _ _ _)
    (intervalIntegrable_log_arcX_sub _ _ _ _)
  have hcount : ({φ : ℝ | cos φ = -1}).Countable := by
    apply (Set.countable_range (fun n : ℤ => π + 2 * (n : ℝ) * π)).mono
    intro φ hφ
    obtain ⟨n, hn⟩ := (cos_eq_neg_one_iff (x := φ)).1 hφ
    exact ⟨n, by simp only; linarith⟩
  filter_upwards [ae_restrict_of_ae (measure_eq_zero_iff_ae_notMem.1 (hcount.measure_zero volume))] with φ hφ
  replace hφ : cos φ ≠ -1 := hφ
  have hlt : arcX β φ < β := by
    unfold arcX
    have : -1 < cos φ := lt_of_le_of_ne (neg_one_le_cos φ) (Ne.symm hφ)
    nlinarith
  rw [← Real.log_abs, ← Real.log_abs (arcX β φ - y), abs_of_neg (by linarith), abs_of_nonpos (by linarith)]
  exact Real.log_le_log (by linarith) (by linarith)

end JacobiAsym
