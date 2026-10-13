import JacobiAsym.Basic

open Filter Topology Set

namespace JacobiAsym

/-- Smooth Riemann–von Mangoldt counting function `N₀(T) = (T/2π) log(T/2πe) + 7/8`. -/
noncomputable def N0 (T : ℝ) : ℝ := T / (2 * Real.pi) * Real.log (T / (2 * Real.pi * Real.exp 1)) + 7 / 8

theorem N0_hasDerivAt {T : ℝ} (hT : 0 < T) :
    HasDerivAt N0 (Real.log (T / (2 * Real.pi)) / (2 * Real.pi)) T := by
  have hpi : 0 < 2 * Real.pi := by positivity
  have hc : 0 < 2 * Real.pi * Real.exp 1 := by positivity
  have h1 : HasDerivAt (fun T : ℝ => T / (2 * Real.pi)) (1 / (2 * Real.pi)) T := (hasDerivAt_id T).div_const _
  have h2 : HasDerivAt (fun T : ℝ => T / (2 * Real.pi * Real.exp 1)) (1 / (2 * Real.pi * Real.exp 1)) T :=
    (hasDerivAt_id T).div_const _
  have h3 := h2.log (by positivity)
  have h4 := (h1.mul h3).add_const (7 / 8)
  unfold N0
  convert h4 using 1
  have hlog : Real.log (T / (2 * Real.pi * Real.exp 1)) = Real.log (T / (2 * Real.pi)) - 1 := by
    rw [Real.log_div hT.ne' hc.ne', Real.log_mul hpi.ne' (Real.exp_pos 1).ne', Real.log_exp,
      Real.log_div hT.ne' hpi.ne']; ring
  rw [hlog]
  field_simp
  ring

theorem N0_strictMonoOn : StrictMonoOn N0 (Ici (2 * Real.pi)) := by
  have hpi : 0 < 2 * Real.pi := by positivity
  apply strictMonoOn_of_deriv_pos (convex_Ici _)
  · intro T hT
    exact (N0_hasDerivAt (hpi.trans_le hT)).continuousAt.continuousWithinAt
  · intro T hT
    rw [interior_Ici] at hT
    have hTpos : 0 < T := hpi.trans hT
    rw [(N0_hasDerivAt hTpos).deriv]
    apply div_pos _ hpi
    apply Real.log_pos
    rw [one_lt_div hpi]; exact hT

/-- `γ(ξ) := N₀⁻¹(ξ - 1/2)` on `[2π, ∞)` (via `invFunOn`; meaningful for `ξ ≥ 1`). -/
noncomputable def zetaGamma (ξ : ℝ) : ℝ := Function.invFunOn N0 (Ici (2 * Real.pi)) (ξ - 1 / 2)

theorem N0_two_pi : N0 (2 * Real.pi) = -1 / 8 := by
  have hpi : (2 * Real.pi) ≠ 0 := by positivity
  unfold N0
  rw [div_self hpi, div_mul_cancel_left₀ hpi, Real.log_inv, Real.log_exp]
  ring

theorem N0_tendsto : Tendsto N0 atTop atTop := by
  have hpi : 0 < 2 * Real.pi := by positivity
  have hlin : Tendsto (fun T : ℝ => T / (2 * Real.pi) + 7 / 8) atTop atTop :=
    tendsto_atTop_add_const_right _ _ (tendsto_id.atTop_div_const hpi)
  apply tendsto_atTop_mono' _ _ hlin
  filter_upwards [eventually_ge_atTop (2 * Real.pi * Real.exp 1 * Real.exp 1)] with T hT
  have hc : 0 < 2 * Real.pi * Real.exp 1 := by positivity
  have hTpos : 0 < T := lt_of_lt_of_le (by positivity) hT
  have hlog : 1 ≤ Real.log (T / (2 * Real.pi * Real.exp 1)) := by
    rw [Real.le_log_iff_exp_le (by positivity), le_div_iff₀ hc]
    linarith
  unfold N0
  have : T / (2 * Real.pi) ≤ T / (2 * Real.pi) * Real.log (T / (2 * Real.pi * Real.exp 1)) :=
    le_mul_of_one_le_right (by positivity) hlog
  linarith

theorem N0_continuousOn : ContinuousOn N0 (Ici (2 * Real.pi)) := fun T hT =>
  (N0_hasDerivAt (lt_of_lt_of_le (by positivity) hT)).continuousAt.continuousWithinAt

/-- Specification of `γ` on `y ≥ 3/8` (where `y - 1/2 ≥ N0 (2π) = -1/8`). -/
theorem zetaGamma_spec' {y : ℝ} (hy : 3 / 8 ≤ y) :
    N0 (zetaGamma y) = y - 1 / 2 ∧ 2 * Real.pi ≤ zetaGamma y := by
  have hsurj := intermediate_value_Ici N0_continuousOn N0_tendsto
  have hmem : y - 1 / 2 ∈ Ici (N0 (2 * Real.pi)) := by rw [N0_two_pi, mem_Ici]; linarith
  obtain ⟨T, hT, hTy⟩ := hsurj hmem
  have h := Function.invFunOn_pos (f := N0) (s := Ici (2 * Real.pi)) ⟨T, hT, hTy⟩
  exact ⟨h.2, h.1⟩

theorem zetaGamma_N0 {T : ℝ} (hT : 2 * Real.pi ≤ T) : zetaGamma (N0 T + 1 / 2) = T := by
  have hy : 3 / 8 ≤ N0 T + 1 / 2 := by
    have := N0_strictMonoOn.monotoneOn (mem_Ici.2 (le_refl _)) (mem_Ici.2 hT) hT
    rw [N0_two_pi] at this; linarith
  obtain ⟨h1, h2⟩ := zetaGamma_spec' hy
  exact N0_strictMonoOn.injOn (mem_Ici.2 h2) (mem_Ici.2 hT) (by rw [h1]; ring)

theorem N0_nine_lt : N0 9 < 1 / 2 := by
  have hpi1 := Real.pi_gt_d2
  have hpi2 := Real.pi_lt_d2
  have hpi : 0 < 2 * Real.pi := by positivity
  set u := (9 : ℝ) / (2 * Real.pi) with hu
  have hu1 : 1.428 < u := by rw [hu, lt_div_iff₀ hpi]; linarith
  have hu2 : u < 1.434 := by rw [hu, div_lt_iff₀ hpi]; linarith
  have hlog : Real.log (9 / (2 * Real.pi * Real.exp 1)) ≤ u - 2 := by
    rw [Real.log_div (by norm_num) (by positivity), Real.log_mul hpi.ne' (Real.exp_pos 1).ne', Real.log_exp]
    have := Real.log_le_sub_one_of_pos (by positivity : (0:ℝ) < u)
    rw [hu, Real.log_div (by norm_num) hpi.ne'] at this
    linarith
  unfold N0
  rw [← hu]
  nlinarith

theorem zetaGamma_spec {ξ : ℝ} (hξ : 1 ≤ ξ) : N0 (zetaGamma ξ) = ξ - 1 / 2 ∧ 9 ≤ zetaGamma ξ := by
  obtain ⟨h1, h2⟩ := zetaGamma_spec' (by linarith : (3 : ℝ) / 8 ≤ ξ)
  refine ⟨h1, ?_⟩
  by_contra hlt
  push Not at hlt
  have h9 : 2 * Real.pi ≤ 9 := by have := Real.pi_lt_d2; linarith
  have := N0_strictMonoOn (mem_Ici.2 h2) (mem_Ici.2 h9) hlt
  have := N0_nine_lt
  linarith

theorem zetaGamma_strictMonoOn : StrictMonoOn zetaGamma (Ici 1) := by
  intro a ha b hb hab
  obtain ⟨ha1, ha2⟩ := zetaGamma_spec' (by linarith [mem_Ici.1 ha] : (3 : ℝ) / 8 ≤ a)
  obtain ⟨hb1, hb2⟩ := zetaGamma_spec' (by linarith [mem_Ici.1 hb] : (3 : ℝ) / 8 ≤ b)
  by_contra hle
  push Not at hle
  have := N0_strictMonoOn.monotoneOn (mem_Ici.2 hb2) (mem_Ici.2 ha2) hle
  linarith

theorem zetaGamma_tendsto : Tendsto zetaGamma atTop atTop := by
  rw [tendsto_atTop]
  intro R
  set R' := max R (2 * Real.pi)
  filter_upwards [eventually_gt_atTop (N0 R' + 1 / 2), eventually_ge_atTop (1 : ℝ)] with ξ hξ hξ1
  obtain ⟨h1, h2⟩ := zetaGamma_spec' (by linarith : (3 : ℝ) / 8 ≤ ξ)
  by_contra hlt
  push Not at hlt
  have hlt' : zetaGamma ξ ≤ R' := hlt.le.trans (le_max_left _ _)
  have := N0_strictMonoOn.monotoneOn (mem_Ici.2 h2) (mem_Ici.2 (le_max_right _ _)) hlt'
  linarith

theorem zetaGamma_strictMonoOn' : StrictMonoOn zetaGamma (Ici (3 / 8)) := by
  intro a ha b hb hab
  obtain ⟨ha1, ha2⟩ := zetaGamma_spec' (mem_Ici.1 ha)
  obtain ⟨hb1, hb2⟩ := zetaGamma_spec' (mem_Ici.1 hb)
  by_contra hle
  push Not at hle
  have := N0_strictMonoOn.monotoneOn (mem_Ici.2 hb2) (mem_Ici.2 ha2) hle
  linarith

theorem zetaGamma_gt_two_pi {y : ℝ} (hy : 3 / 8 < y) : 2 * Real.pi < zetaGamma y := by
  obtain ⟨h1, h2⟩ := zetaGamma_spec' hy.le
  rcases eq_or_lt_of_le h2 with heq | hlt
  · rw [← heq, N0_two_pi] at h1; linarith
  · exact hlt

theorem zetaGamma_continuousAt {ξ : ℝ} (hξ : 3 / 8 < ξ) : ContinuousAt zetaGamma ξ := by
  apply StrictMonoOn.continuousAt_of_image_mem_nhds (s := Ioi (3 / 8))
    (zetaGamma_strictMonoOn'.mono Ioi_subset_Ici_self) (Ioi_mem_nhds hξ)
  apply mem_of_superset (Ioi_mem_nhds (zetaGamma_gt_two_pi hξ))
  intro T hT
  refine ⟨N0 T + 1 / 2, ?_, zetaGamma_N0 (le_of_lt hT)⟩
  have := N0_strictMonoOn (mem_Ici.2 (le_refl _)) (mem_Ici.2 (le_of_lt hT)) hT
  rw [N0_two_pi] at this
  show 3 / 8 < N0 T + 1 / 2
  linarith

theorem zetaGamma_hasDerivAt {ξ : ℝ} (hξ : 1 ≤ ξ) :
    HasDerivAt zetaGamma (2 * Real.pi / Real.log (zetaGamma ξ / (2 * Real.pi))) ξ := by
  have hγ := zetaGamma_gt_two_pi (by linarith : (3 : ℝ) / 8 < ξ)
  have hpi : 0 < 2 * Real.pi := by positivity
  have hd : HasDerivAt (fun T => N0 T + 1 / 2) (Real.log (zetaGamma ξ / (2 * Real.pi)) / (2 * Real.pi))
      (zetaGamma ξ) := (N0_hasDerivAt (hpi.trans hγ)).add_const _
  have hlog : 0 < Real.log (zetaGamma ξ / (2 * Real.pi)) := Real.log_pos (by rw [one_lt_div hpi]; exact hγ)
  have := hd.of_local_left_inverse (zetaGamma_continuousAt (by linarith)) (by positivity) ?_
  · rwa [inv_div] at this
  · filter_upwards [Ioi_mem_nhds (by linarith : (3 : ℝ) / 8 < ξ)] with y hy
    rw [(zetaGamma_spec' (le_of_lt hy)).1]; ring

/-- `L(ξ) = ξ² / (γ(ξ)² + 1/4)` (so that `ξ^{-2} L(ξ) = 1/(γ² + 1/4)`). -/
noncomputable def zetaL (ξ : ℝ) : ℝ := ξ ^ 2 / (zetaGamma ξ ^ 2 + 1 / 4)

end JacobiAsym
