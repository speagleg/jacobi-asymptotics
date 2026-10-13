import JacobiAsym.ZetaSlowFactor
import JacobiAsym.TheoremHL
import JacobiAsym.HankelLimit

open Filter Topology

namespace JacobiAsym

/-- Smooth-ζ atoms `x_k = 1/(γ(k+1)² + 1/4)` and weights `2 x_k` (item 11's measure with the smooth model). -/
noncomputable def zetaAtom (k : ℕ) : ℝ := 1 / (zetaGamma ((k : ℝ) + 1) ^ 2 + 1 / 4)

theorem zetaAtom_eq (k : ℕ) : slowAtom 2 zetaL ((k : ℝ) + 1) = zetaAtom k := by
  have ht : (0 : ℝ) < (k : ℝ) + 1 := by positivity
  unfold slowAtom zetaL zetaAtom
  rw [Real.rpow_neg ht.le, Real.rpow_two]
  field_simp

theorem zetaAtom_pos (k : ℕ) : 0 < zetaAtom k := by unfold zetaAtom; positivity

theorem zetaAtom_le_one (k : ℕ) : |zetaAtom k| ≤ 1 := by
  rw [abs_of_pos (zetaAtom_pos k)]
  unfold zetaAtom
  rw [div_le_one (by positivity)]
  have := (zetaGamma_spec (by have := Nat.cast_nonneg (α := ℝ) k; linarith : (1 : ℝ) ≤ (k : ℝ) + 1)).2
  nlinarith

/-- Summability of the smooth-ζ weights (via slow variation: `L(t) ≤ C t^{1/2}` eventually). -/
theorem zetaAtom_summable : Summable zetaAtom := by
  obtain ⟨L', E, a0, hL⟩ := zetaL_slowFactor
  obtain ⟨A, hA⟩ := eventually_atTop.1 (hL.E_lim.eventually (gt_mem_nhds (by norm_num : (0:ℝ) < 1 / 2)))
  set a : ℝ := max A 1 with ha
  have ha1 : 1 ≤ a := le_max_right _ _
  have hEa : E a < 1 / 2 := hA a (le_max_left _ _)
  have hLa := hL.L_pos a ha1
  set C : ℝ := zetaL a * a ^ (-(1 / 2 : ℝ)) with hC
  have hg : Summable (fun k : ℕ => C * (((k : ℝ) + 1) ^ (3 / 2 : ℝ))⁻¹) := by
    have h := (summable_nat_add_iff 1).2 (Real.summable_nat_rpow_inv.2 (by norm_num : (1 : ℝ) < 3 / 2))
    simpa [Nat.cast_add, Nat.cast_one] using h.mul_left C
  apply Summable.of_norm_bounded_eventually_nat hg
  filter_upwards [eventually_ge_atTop ⌈a⌉₊] with k hk
  have hka : a ≤ (k : ℝ) + 1 := by
    have := Nat.le_ceil a
    have : (⌈a⌉₊ : ℝ) ≤ k := by exact_mod_cast hk
    linarith
  have ht : (0 : ℝ) < (k : ℝ) + 1 := by positivity
  rw [Real.norm_eq_abs, abs_of_pos (zetaAtom_pos k), ← zetaAtom_eq k]
  -- slow variation: log L(t) ≤ log L(a) + (1/2) log(t/a)
  have hsl := hL.logL_slow a ((k : ℝ) + 1) ha1 hka
  have hlog0 : 0 ≤ Real.log (((k : ℝ) + 1) / a) := Real.log_nonneg (by rw [le_div_iff₀ (by linarith)]; linarith)
  have hLt := hL.L_pos ((k : ℝ) + 1) (by linarith)
  have hle : Real.log (zetaL ((k : ℝ) + 1)) ≤ Real.log (zetaL a) + 1 / 2 * Real.log (((k : ℝ) + 1) / a) := by
    have := (abs_le.1 hsl).2
    nlinarith [hL.E_nonneg a]
  have hLbound : zetaL ((k : ℝ) + 1) ≤ zetaL a * (((k : ℝ) + 1) / a) ^ (1 / 2 : ℝ) := by
    rw [← Real.log_le_log_iff hLt (by positivity), Real.log_mul hLa.ne' (by positivity),
      Real.log_rpow (by positivity)]
    linarith
  unfold slowAtom
  calc ((k : ℝ) + 1) ^ (-(2 : ℝ)) * zetaL ((k : ℝ) + 1)
      ≤ ((k : ℝ) + 1) ^ (-(2 : ℝ)) * (zetaL a * (((k : ℝ) + 1) / a) ^ (1 / 2 : ℝ)) :=
        mul_le_mul_of_nonneg_left hLbound (by positivity)
    _ = C * (((k : ℝ) + 1) ^ (3 / 2 : ℝ))⁻¹ := by
        rw [hC, Real.div_rpow ht.le (by linarith), Real.rpow_neg (by linarith : (0:ℝ) ≤ a),
          ← Real.rpow_neg ht.le]
        have e : ((k : ℝ) + 1) ^ (-(2 : ℝ)) * ((k : ℝ) + 1) ^ (1 / 2 : ℝ) = ((k : ℝ) + 1) ^ (-(3 / 2 : ℝ)) := by
          rw [← Real.rpow_add ht]; norm_num
        rw [Real.rpow_neg ht.le (3 / 2)]
        rw [show ((k : ℝ) + 1) ^ (-(2 : ℝ)) * (zetaL a * (((k : ℝ) + 1) ^ (1 / 2 : ℝ) / a ^ (1 / 2 : ℝ))) =
          zetaL a * (a ^ (1 / 2 : ℝ))⁻¹ * (((k : ℝ) + 1) ^ (-(2 : ℝ)) * ((k : ℝ) + 1) ^ (1 / 2 : ℝ)) by
            field_simp]
        rw [e, Real.rpow_neg ht.le]

/-- **Corollary H_L-ζ** (PROVED-mod-input `TheoremHPure 2 κ 2`). -/
theorem smoothZeta_HL {κ : ℝ} (hH : TheoremHPure 2 κ 2) :
    Tendsto (hnorm 2 κ (heineD zetaAtom (fun k => 2 * zetaAtom k)) (fun n => Real.log (zetaL n)))
      atTop (𝓝 0) := by
  obtain ⟨L', E, a0, hL⟩ := zetaL_slowFactor
  have hL1 := zetaL_pos (le_refl (1 : ℝ))
  set U : ℝ → ℝ := fun t => max 1 (zetaL (max t 1) / zetaL 1) with hUdef
  have hfun : (fun k : ℕ => slowAtom 2 zetaL ((k : ℝ) + 1)) = zetaAtom := funext zetaAtom_eq
  have hk1 : ∀ k : ℕ, (1 : ℝ) ≤ (k : ℝ) + 1 := fun k => by have := Nat.cast_nonneg (α := ℝ) k; linarith
  have h := theoremHL (p := 2) (κ := κ) (s := 2) (s0 := 2) (c1 := 2 * zetaL 1) (c2 := 2 * zetaL 1) (U := U)
    (w := fun k => 2 * zetaAtom k) hL hH hH (by positivity) (by positivity)
    (fun k => by
      rw [← zetaAtom_eq k]; unfold slowAtom powSeq
      have hm := zetaL_monotoneOn (Set.mem_Ici.2 (le_refl (1:ℝ))) (Set.mem_Ici.2 (hk1 k)) (hk1 k)
      have : 0 < ((k : ℝ) + 1) ^ (-(2 : ℝ)) := by positivity
      nlinarith)
    (fun k => by
      rw [← zetaAtom_eq k]; unfold slowAtom powSeq
      simp only [hUdef, max_eq_left (hk1 k)]
      have hp : 0 < ((k : ℝ) + 1) ^ (-(2 : ℝ)) := by positivity
      have hq : zetaL ((k : ℝ) + 1) / zetaL 1 ≤ max 1 (zetaL ((k : ℝ) + 1) / zetaL 1) := le_max_right _ _
      have e : 2 * (((k : ℝ) + 1) ^ (-(2 : ℝ)) * zetaL ((k : ℝ) + 1)) =
          2 * zetaL 1 * ((k : ℝ) + 1) ^ (-(2 : ℝ)) * (zetaL ((k : ℝ) + 1) / zetaL 1) := by
        field_simp
      rw [e]
      exact mul_le_mul_of_nonneg_left hq (by positivity))
    (fun t => le_max_left _ _)
    (fun t t' htt => by
      simp only [hUdef]
      apply max_le_max le_rfl
      apply div_le_div_of_nonneg_right _ hL1.le
      exact zetaL_monotoneOn (Set.mem_Ici.2 (le_max_right _ _)) (Set.mem_Ici.2 (le_max_right _ _))
        (max_le_max htt le_rfl))
    (by
      -- log U(n)/n → 0 since 0 ≤ log U(n) ≤ E 1 log n
      have hb : Tendsto (fun n : ℕ => E 1 * (Real.log n / n)) atTop (𝓝 0) := by
        simpa using tendsto_log_div_nat.const_mul (E 1)
      apply squeeze_zero' _ _ hb
      · filter_upwards with n
        exact div_nonneg (Real.log_nonneg (le_max_left _ _)) (Nat.cast_nonneg n)
      · filter_upwards [eventually_ge_atTop 1] with n hn
        have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
        simp only [hUdef, max_eq_left hn']
        rw [mul_div_assoc']
        apply div_le_div_of_nonneg_right _ (by positivity)
        rcases le_total (zetaL n / zetaL 1) 1 with h1 | h1
        · rw [max_eq_left h1, Real.log_one]
          exact mul_nonneg (hL.E_nonneg 1) (Real.log_nonneg hn')
        · rw [max_eq_right h1, Real.log_div (zetaL_pos hn').ne' hL1.ne']
          have := hL.logL_slow 1 n le_rfl hn'
          rw [div_one] at this
          linarith [(abs_le.1 this).2])
    (zetaAtom_summable.mul_left 2)
  rwa [hfun] at h

/-- The same, stated for the Hankel determinant of the infinite smooth-ζ measure. -/
theorem smoothZeta_HL_det {κ : ℝ} (hH : TheoremHPure 2 κ 2) :
    Tendsto (hnorm 2 κ (fun n => (hankel zetaAtom (fun k => 2 * zetaAtom k) n).det) (fun n => Real.log (zetaL n)))
      atTop (𝓝 0) := by
  have hfun : (fun n => (hankel zetaAtom (fun k => 2 * zetaAtom k) n).det) =
      heineD zetaAtom (fun k => 2 * zetaAtom k) := by
    funext n
    exact (heineD_eq_det (fun k => (mul_pos two_pos (zetaAtom_pos k)).le) (zetaAtom_summable.mul_left 2)
      zetaAtom_le_one n).symm
  rw [hfun]
  exact smoothZeta_HL hH

end JacobiAsym
