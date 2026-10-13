import JacobiAsym.SmoothZetaHL
import JacobiAsym.H2
import JacobiAsym.SuperFactorial

open Finset Filter Topology

namespace JacobiAsym

theorem zeta_DMeasure : DMeasure zetaAtom (fun k => 2 * zetaAtom k) where
  w_pos k := mul_pos two_pos (zetaAtom_pos k)
  w_sum := zetaAtom_summable.mul_left 2
  x_bdd := ⟨1, zetaAtom_le_one⟩
  x_anti := by
    intro a b hab
    have ha : (1 : ℝ) ≤ (a : ℝ) + 1 := by have := Nat.cast_nonneg (α := ℝ) a; linarith
    have hb : (1 : ℝ) ≤ (b : ℝ) + 1 := by have := Nat.cast_nonneg (α := ℝ) b; linarith
    have hγ := zetaGamma_strictMonoOn (Set.mem_Ici.2 ha) (Set.mem_Ici.2 hb)
      (by have : (a : ℝ) < b := by exact_mod_cast hab
          linarith)
    have h9 := (zetaGamma_spec ha).2
    unfold zetaAtom
    apply one_div_lt_one_div_of_lt (by positivity)
    nlinarith

/-- `log D_n = n log m₀ + ∑_{j=1}^{n-1} (n-j) log b_j²` (from H2). -/
theorem log_hankel_eq {x w : ℕ → ℝ} (h : DMeasure x w) (n : ℕ) :
    Real.log (hankel x w n).det = n * Real.log (mom x w 0) + ∑ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log (jb2 x w j) := by
  have hm0 : 0 < mom x w 0 := by rw [← hankel_one_det]; exact hankel_det_pos h 1
  rw [hankel_det_eq_prod h, Real.log_mul (pow_pos hm0 n).ne' (prod_pos fun j _ => pow_pos (jb2_pos h j) _).ne',
    Real.log_pow, Real.log_prod (fun j _ => (pow_pos (jb2_pos h j) _).ne')]
  congr 1
  apply sum_congr rfl; intro j hj
  rw [Real.log_pow, Nat.cast_sub (mem_Ico.1 hj).2.le]

/-- `log L(j) = 2 log j + log x_j` with `x_j = zetaAtom (j-1)` (`j ≥ 1`). -/
theorem log_zetaL_eq {j : ℕ} (hj : 1 ≤ j) :
    Real.log (zetaL j) = 2 * Real.log j + Real.log (zetaAtom (j - 1)) := by
  have hcast : ((j - 1 : ℕ) : ℝ) + 1 = j := by rw [Nat.cast_sub hj]; push_cast; ring
  have hjpos : (0 : ℝ) < j := by exact_mod_cast hj
  unfold zetaAtom
  rw [hcast]
  unfold zetaL
  rw [div_eq_mul_one_div, Real.log_mul (by positivity) (by positivity), Real.log_pow]
  push_cast; ring

/-- **b_j form of Corollary H_L-ζ** (PROVED-mod-input): the doubly-Cesàro geometric mean of `b_j / x_j`
tends to `π²/16`; `x_j = zetaAtom (j-1)` is the `j`-th atom. -/
theorem smoothZeta_bLaw (hH : TheoremHPure 2 (3 + Real.log (Real.pi ^ 2 / 16)) 2) :
    Tendsto (fun n : ℕ => 2 / (n : ℝ) ^ 2 *
      ∑ j ∈ Ico 1 n, ((n : ℝ) - j) *
        Real.log (Real.sqrt (jb2 zetaAtom (fun k => 2 * zetaAtom k) j) / zetaAtom (j - 1)))
      atTop (𝓝 (Real.log (Real.pi ^ 2 / 16))) := by
  have hD := zeta_DMeasure
  obtain ⟨L', E, a0, hL⟩ := zetaL_slowFactor
  set κ := 3 + Real.log (Real.pi ^ 2 / 16) with hκ
  set x := zetaAtom with hx
  set w := fun k => 2 * zetaAtom k with hw
  set ℓ : ℝ → ℝ := fun t => Real.log (zetaL t) with hℓ
  set m0 := mom x w 0
  -- the five vanishing terms
  have h1 := smoothZeta_HL_det hH
  have h2 := weighted_cesaro_slow hL.E_nonneg hL.E_anti hL.E_lim hL.logL_slow
  have h3 := sum_log_weighted_asymp
  have h4 : Tendsto (fun n : ℕ => Real.log m0 / n) atTop (𝓝 0) := tendsto_const_div_atTop_nhds_zero_nat _
  have h5 : Tendsto (fun n : ℕ => ℓ n / n) atTop (𝓝 0) := by
    have hb : Tendsto (fun n : ℕ => (|ℓ 1| + E 1 * Real.log n) / n) atTop (𝓝 0) := by
      have := (tendsto_const_div_atTop_nhds_zero_nat |ℓ 1|).add (tendsto_log_div_nat.const_mul (E 1))
      simp only [mul_zero, add_zero] at this
      refine this.congr' ?_
      filter_upwards [eventually_ge_atTop 1] with n hn
      field_simp
    apply squeeze_zero_norm' _ hb
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
    have h := hL.logL_slow 1 n le_rfl hnr
    rw [div_one] at h
    rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0:ℝ) < n)]
    apply div_le_div_of_nonneg_right _ (by positivity)
    have := abs_sub_abs_le_abs_sub (ℓ n) (ℓ 1)
    simp only [hℓ] at this ⊢
    linarith
  have hall := ((((h1.sub h4).sub h2).add h5).add (h3.const_mul 4)).const_add (Real.log (Real.pi ^ 2 / 16))
  simp only [sub_zero, add_zero, mul_zero] at hall
  refine hall.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hn0 : (n : ℝ) ≠ 0 := by linarith
  -- termwise rewrite of the target sum
  have hterm : ∀ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log (Real.sqrt (jb2 x w j) / x (j - 1)) =
      (1 / 2) * (((n : ℝ) - j) * Real.log (jb2 x w j)) - ((n : ℝ) - j) * (ℓ j - ℓ n) - ℓ n * ((n : ℝ) - j)
        + 2 * (((n : ℝ) - j) * Real.log j) := by
    intro j hj
    have hj1 : 1 ≤ j := (mem_Ico.1 hj).1
    have hb := jb2_pos hD j
    have hxj := zetaAtom_pos (j - 1)
    rw [Real.log_div (Real.sqrt_pos.2 hb).ne' hxj.ne', Real.log_sqrt hb.le]
    have := log_zetaL_eq hj1
    simp only [hℓ, hx]
    rw [this]; ring
  have hsumw : ∑ j ∈ Ico 1 n, ((n : ℝ) - j) = (n : ℝ) * ((n : ℝ) - 1) / 2 := by
    rw [sum_sub_distrib, sum_const, Nat.card_Ico, nsmul_eq_mul, sum_Ico_id, Nat.cast_sub hn]
    push_cast; ring
  have hSb : ∑ i ∈ Ico 1 n, ((n : ℝ) - i) * Real.log (jb2 x w i) =
      Real.log (hankel x w n).det - n * Real.log m0 := by rw [log_hankel_eq hD n]; ring
  rw [sum_congr rfl hterm, sum_add_distrib, sum_sub_distrib, sum_sub_distrib, ← mul_sum, ← mul_sum, ← mul_sum,
    hsumw, hSb]
  unfold hnorm
  simp only [hℓ, hx, hw, hκ]
  field_simp
  ring

end JacobiAsym
