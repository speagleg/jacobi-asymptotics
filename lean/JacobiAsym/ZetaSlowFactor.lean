import JacobiAsym.ZetaSmooth
import JacobiAsym.SlowFactor

open Filter Topology Set

namespace JacobiAsym

/-- `ℓ(ξ) = log(γ(ξ)/2π)`. -/
noncomputable def zetaEll (ξ : ℝ) : ℝ := Real.log (zetaGamma ξ / (2 * Real.pi))

/-- Explicit derivative of `zetaL`. -/
noncomputable def zetaL' (ξ : ℝ) : ℝ :=
  2 * ξ / (zetaGamma ξ ^ 2 + 1 / 4) -
    ξ ^ 2 * (2 * zetaGamma ξ * (2 * Real.pi / zetaEll ξ)) / (zetaGamma ξ ^ 2 + 1 / 4) ^ 2

theorem zetaEll_pos {ξ : ℝ} (hξ : 1 ≤ ξ) : 0 < zetaEll ξ := by
  have hpi : 0 < 2 * Real.pi := by positivity
  exact Real.log_pos (by rw [one_lt_div hpi]; exact zetaGamma_gt_two_pi (by linarith))

theorem zetaL_hasDerivAt {ξ : ℝ} (hξ : 1 ≤ ξ) : HasDerivAt zetaL (zetaL' ξ) ξ := by
  have hγ := zetaGamma_hasDerivAt hξ
  have hD : zetaGamma ξ ^ 2 + 1 / 4 ≠ 0 := by positivity
  have hden : HasDerivAt (fun x => zetaGamma x ^ 2 + 1 / 4)
      (2 * zetaGamma ξ * (2 * Real.pi / zetaEll ξ)) ξ := by
    have := (hγ.pow 2).add_const (1 / 4)
    unfold zetaEll
    convert this using 1
    simp
  have h := (hasDerivAt_pow 2 ξ).div hden hD
  have hfun : zetaL = fun x => x ^ 2 / (zetaGamma x ^ 2 + 1 / 4) := rfl
  rw [hfun]
  convert h using 1
  unfold zetaL'
  generalize 2 * zetaGamma ξ * (2 * Real.pi / zetaEll ξ) = c
  field_simp
  ring

/-- The exact logarithmic derivative `ε = ξ L'/L`. -/
theorem zetaL_eps_eq {ξ : ℝ} (hξ : 1 ≤ ξ) :
    ξ * zetaL' ξ / zetaL ξ =
      (zetaEll ξ / 2 + 2 * zetaGamma ξ ^ 2 - 11 * Real.pi / 2 * zetaGamma ξ) /
        (zetaEll ξ * (zetaGamma ξ ^ 2 + 1 / 4)) := by
  have hpi : 0 < 2 * Real.pi := by positivity
  obtain ⟨hN, h9⟩ := zetaGamma_spec hξ
  have hℓ := zetaEll_pos hξ
  have hγpos : 0 < zetaGamma ξ := by linarith
  have hxi : ξ = N0 (zetaGamma ξ) + 1 / 2 := by linarith
  have hN0 : N0 (zetaGamma ξ) = zetaGamma ξ / (2 * Real.pi) * (zetaEll ξ - 1) + 7 / 8 := by
    unfold N0 zetaEll
    rw [Real.log_div hγpos.ne' (by positivity), Real.log_mul hpi.ne' (Real.exp_pos 1).ne', Real.log_exp,
      Real.log_div hγpos.ne' hpi.ne']
    ring
  have hξpos : 0 < ξ := by linarith
  have hξexpr : ξ = zetaGamma ξ / (2 * Real.pi) * (zetaEll ξ - 1) + 11 / 8 := by linarith
  have hD : 0 < zetaGamma ξ ^ 2 + 1 / 4 := by positivity
  have e1 : ξ * zetaL' ξ / zetaL ξ =
      2 - 4 * Real.pi * zetaGamma ξ * ξ / (zetaEll ξ * (zetaGamma ξ ^ 2 + 1 / 4)) := by
    unfold zetaL' zetaL
    generalize zetaEll ξ = ℓ at hℓ ⊢
    generalize zetaGamma ξ = γ at hD ⊢
    field_simp
    ring
  rw [e1, eq_div_iff (by positivity)]
  have e2 : 4 * Real.pi * zetaGamma ξ * ξ = 2 * zetaGamma ξ ^ 2 * (zetaEll ξ - 1) + 11 * Real.pi / 2 * zetaGamma ξ := by
    have h := hξexpr
    generalize zetaGamma ξ = γ at h ⊢
    generalize zetaEll ξ = ℓ at h ⊢
    rw [h]
    field_simp
    ring
  rw [sub_mul, div_mul_cancel₀ _ (by positivity), e2]
  ring

theorem zetaL_pos {ξ : ℝ} (hξ : 1 ≤ ξ) : 0 < zetaL ξ := by
  unfold zetaL; have : 0 < ξ := by linarith
  positivity

/-- `0 ≤ ε`, `ε < 2`, and `ε ≤ 1/(2γ²) + 2/ℓ`. -/
theorem zetaL_eps_bounds {ξ : ℝ} (hξ : 1 ≤ ξ) :
    0 ≤ ξ * zetaL' ξ / zetaL ξ ∧ ξ * zetaL' ξ / zetaL ξ < 2 ∧
      ξ * zetaL' ξ / zetaL ξ ≤ 1 / (2 * zetaGamma ξ ^ 2) + 2 / zetaEll ξ := by
  rw [zetaL_eps_eq hξ]
  obtain ⟨hN, h9⟩ := zetaGamma_spec hξ
  have hℓ := zetaEll_pos hξ
  have hpi := Real.pi_lt_d2
  have hpi0 := Real.pi_pos
  set γ := zetaGamma ξ
  set ℓ := zetaEll ξ
  have hD : 0 < γ ^ 2 + 1 / 4 := by positivity
  have hnum : 0 ≤ ℓ / 2 + 2 * γ ^ 2 - 11 * Real.pi / 2 * γ := by nlinarith
  refine ⟨div_nonneg hnum (by positivity), ?_, ?_⟩
  · -- ε < 2 ⇔ num < 2 ℓ D, using ξ = γ(ℓ-1)/(2π) + 11/8 > 0
    rw [div_lt_iff₀ (by positivity)]
    have hxi : 0 < γ / (2 * Real.pi) * (ℓ - 1) + 11 / 8 := by
      have hN0 : N0 γ = γ / (2 * Real.pi) * (ℓ - 1) + 7 / 8 := by
        unfold N0
        have hγpos : 0 < γ := by linarith
        rw [Real.log_div hγpos.ne' (by positivity), Real.log_mul (by positivity) (Real.exp_pos 1).ne',
          Real.log_exp]
        simp only [ℓ, zetaEll, γ]
        rw [Real.log_div (by linarith) (by positivity)]
        ring
      linarith
    have h4 : 0 < 4 * Real.pi * γ * (γ / (2 * Real.pi) * (ℓ - 1) + 11 / 8) := by positivity
    have e : 4 * Real.pi * γ * (γ / (2 * Real.pi) * (ℓ - 1) + 11 / 8) =
        2 * γ ^ 2 * (ℓ - 1) + 11 * Real.pi / 2 * γ := by field_simp; ring
    nlinarith
  · rw [div_le_iff₀ (by positivity)]
    have hγ2 : 0 < γ ^ 2 := by positivity
    have e : (1 / (2 * γ ^ 2) + 2 / ℓ) * (ℓ * (γ ^ 2 + 1 / 4)) =
        ℓ / 2 + 2 * γ ^ 2 + ℓ / (8 * γ ^ 2) + 1 / 2 := by field_simp; ring
    rw [e]
    have : 0 ≤ ℓ / (8 * γ ^ 2) := by positivity
    have : 0 ≤ 11 * Real.pi / 2 * γ := by nlinarith
    linarith

/-- Explicit antitone majorant of `|ε|`. -/
noncomputable def zetaE (t : ℝ) : ℝ := 1 / (2 * zetaGamma (max t 1) ^ 2) + 2 / zetaEll (max t 1)

theorem zetaE_nonneg (t : ℝ) : 0 ≤ zetaE t := by
  unfold zetaE
  have := zetaEll_pos (le_max_right t 1)
  positivity

theorem zetaE_anti : Antitone zetaE := by
  intro t t' htt
  have hm : max t 1 ≤ max t' 1 := max_le_max htt le_rfl
  have h1 := le_max_right t 1
  have h1' := le_max_right t' 1
  have hγ : zetaGamma (max t 1) ≤ zetaGamma (max t' 1) :=
    zetaGamma_strictMonoOn.monotoneOn (mem_Ici.2 h1) (mem_Ici.2 h1') hm
  have hγ9 := (zetaGamma_spec h1).2
  have hℓ := zetaEll_pos h1
  have hℓ' : zetaEll (max t 1) ≤ zetaEll (max t' 1) := by
    unfold zetaEll
    exact Real.log_le_log (by have := zetaGamma_gt_two_pi (by linarith : (3:ℝ)/8 < max t 1); positivity)
      (div_le_div_of_nonneg_right hγ (by positivity))
  unfold zetaE
  have a1 : 1 / (2 * zetaGamma (max t' 1) ^ 2) ≤ 1 / (2 * zetaGamma (max t 1) ^ 2) :=
    one_div_le_one_div_of_le (by positivity) (by nlinarith)
  have a2 : 2 / zetaEll (max t' 1) ≤ 2 / zetaEll (max t 1) := div_le_div_of_nonneg_left (by norm_num) hℓ hℓ'
  linarith

theorem zetaE_tendsto : Tendsto zetaE atTop (𝓝 0) := by
  have hmax : Tendsto (fun t : ℝ => max t 1) atTop atTop := tendsto_atTop_mono (fun t => le_max_left t 1) tendsto_id
  have hγ := zetaGamma_tendsto.comp hmax
  have h1 : Tendsto (fun t => 1 / (2 * zetaGamma (max t 1) ^ 2)) atTop (𝓝 0) := by
    have : Tendsto (fun t => 2 * zetaGamma (max t 1) ^ 2) atTop atTop :=
      (tendsto_pow_atTop (by norm_num : (2:ℕ) ≠ 0)).comp hγ |>.const_mul_atTop (by norm_num)
    refine (this.inv_tendsto_atTop).congr (fun t => ?_)
    simp [Pi.inv_apply, one_div]
  have h2 : Tendsto (fun t => 2 / zetaEll (max t 1)) atTop (𝓝 0) := by
    have : Tendsto (fun t => zetaEll (max t 1)) atTop atTop :=
      Real.tendsto_log_atTop.comp (hγ.atTop_div_const (by positivity))
    exact tendsto_const_nhds.div_atTop this
  have h := h1.add h2
  rw [add_zero] at h
  exact h

theorem zetaL'_continuousOn : ContinuousOn zetaL' (Ici 1) := by
  intro ξ hξ
  have hξ1 : 1 ≤ ξ := hξ
  have hγc := zetaGamma_continuousAt (by linarith : (3:ℝ)/8 < ξ)
  have hγ := zetaGamma_gt_two_pi (by linarith : (3:ℝ)/8 < ξ)
  have hℓ := zetaEll_pos hξ1
  have hℓc : ContinuousAt zetaEll ξ :=
    (hγc.div_const _).log (div_pos (by linarith [Real.pi_pos]) (by positivity)).ne'
  apply ContinuousAt.continuousWithinAt
  unfold zetaL'
  have hD : zetaGamma ξ ^ 2 + 1 / 4 ≠ 0 := by positivity
  apply ContinuousAt.sub
  · exact (continuousAt_const.mul continuousAt_id).div ((hγc.pow 2).add continuousAt_const) hD
  · exact ((continuousAt_id.pow 2).mul (continuousAt_const.mul hγc |>.mul (continuousAt_const.div hℓc hℓ.ne'))).div
      (((hγc.pow 2).add continuousAt_const).pow 2) (pow_ne_zero 2 hD)

theorem zetaL_monotoneOn : MonotoneOn zetaL (Ici 1) := by
  apply monotoneOn_of_deriv_nonneg (convex_Ici 1)
  · intro t ht; exact (zetaL_hasDerivAt ht).continuousAt.continuousWithinAt
  · intro t ht
    rw [interior_Ici] at ht
    exact (zetaL_hasDerivAt (le_of_lt ht)).differentiableAt.differentiableWithinAt
  · intro t ht
    rw [interior_Ici] at ht
    have ht1 : 1 ≤ t := le_of_lt ht
    rw [(zetaL_hasDerivAt ht1).deriv]
    have h := (zetaL_eps_bounds ht1).1
    have hL := zetaL_pos ht1
    have htpos : 0 < t := by linarith
    have : 0 ≤ t * zetaL' t := by
      have := mul_nonneg h hL.le
      rwa [div_mul_cancel₀ _ hL.ne'] at this
    nlinarith

/-- **The smooth-ζ factor is slowly varying in the sense of `SlowFactor 2`.** -/
theorem zetaL_slowFactor : ∃ (L' E : ℝ → ℝ) (a0 : ℕ), SlowFactor 2 zetaL L' E a0 := by
  obtain ⟨N, hN⟩ := eventually_atTop.1 (zetaE_tendsto.eventually (gt_mem_nhds (by norm_num : (0:ℝ) < 1)))
  set a0 : ℕ := max 1 ⌈N⌉₊
  have ha0 : (N : ℝ) ≤ a0 := (Nat.le_ceil N).trans (by exact_mod_cast le_max_right 1 ⌈N⌉₊)
  refine ⟨zetaL', zetaE, a0, ?_⟩
  exact
    { p_pos := by norm_num
      L_pos := fun t ht => zetaL_pos ht
      L_deriv := fun t ht => zetaL_hasDerivAt ht
      L'_cont := zetaL'_continuousOn
      E_nonneg := zetaE_nonneg
      E_anti := zetaE_anti
      E_lim := zetaE_tendsto
      eps_le := fun t ht => by
        obtain ⟨h0, _, hle⟩ := zetaL_eps_bounds ht
        rw [abs_of_nonneg h0]
        unfold zetaE
        rw [max_eq_left ht]
        exact hle
      a0_pos := le_max_left 1 _
      E_a0 := by have := hN a0 ha0; linarith
      L_mono := zetaL_monotoneOn.mono (Ici_subset_Ici.2 (by exact_mod_cast le_max_left 1 ⌈N⌉₊))
      f_dec := fun t ht => by
        have h := (zetaL_eps_bounds ht).2.1
        have hL := zetaL_pos ht
        rwa [div_lt_iff₀ hL] at h }

end JacobiAsym
