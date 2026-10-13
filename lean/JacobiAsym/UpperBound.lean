import JacobiAsym.Exponent
import JacobiAsym.SlowVariation

open Finset Filter Topology

namespace JacobiAsym

/-- The atoms `slowAtom p L (k+1)` are strictly decreasing. -/
theorem SlowFactor.slowAtom_strictAnti {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    StrictAnti (fun k : ℕ => slowAtom p L ((k : ℝ) + 1)) := by
  intro a b hab
  obtain ⟨ρm, hρm0, _, hρm⟩ := h.exists_rhoMin
  have hp := h.p_pos
  have har : (1 : ℝ) ≤ (a : ℝ) + 1 := by have := Nat.cast_nonneg (α := ℝ) a; linarith
  have habr : (a : ℝ) + 1 < (b : ℝ) + 1 := by
    have : (a : ℝ) < b := by exact_mod_cast hab
    linarith
  have hlow := h.lower_pair hρm har habr
  have hg : 0 < ((a : ℝ) + 1) ^ (-p) - ((b : ℝ) + 1) ^ (-p) :=
    sub_pos.2 (Real.rpow_lt_rpow_of_neg (by linarith) habr (by linarith))
  have hlo : 0 < (if (a : ℝ) + 1 < a0 then ρm else (1 - E ((a : ℝ) + 1) / p) * L ((a : ℝ) + 1)) := by
    split_ifs with hlt
    · exact hρm0
    · have ha0u : (a0 : ℝ) ≤ (a : ℝ) + 1 := not_lt.1 hlt
      have : E ((a : ℝ) + 1) ≤ E a0 := h.E_anti ha0u
      have : E ((a : ℝ) + 1) / p < 1 := by rw [div_lt_one hp]; linarith [h.E_a0]
      exact mul_pos (by linarith) (h.L_pos _ har)
  show slowAtom p L ((b : ℝ) + 1) < slowAtom p L ((a : ℝ) + 1)
  nlinarith [mul_pos hlo hg]

/-- `log ∑_{m ≤ n} T m ≤ log (n+1) + Q` when every `T m ∈ (0, exp Q]`. -/
theorem log_sum_le_of_log_le {n : ℕ} {T : ℕ → ℝ} {Q : ℝ} (hT : ∀ m ∈ Finset.range (n + 1), 0 < T m)
    (hQ : ∀ m ∈ Finset.range (n + 1), Real.log (T m) ≤ Q) :
    Real.log (∑ m ∈ Finset.range (n + 1), T m) ≤ Real.log ((n : ℝ) + 1) + Q := by
  have hle : ∑ m ∈ Finset.range (n + 1), T m ≤ ((n : ℝ) + 1) * Real.exp Q := by
    calc ∑ m ∈ Finset.range (n + 1), T m ≤ ∑ m ∈ Finset.range (n + 1), Real.exp Q :=
          Finset.sum_le_sum fun m hm => (Real.log_le_iff_le_exp (hT m hm)).1 (hQ m hm)
      _ = ((n : ℝ) + 1) * Real.exp Q := by simp
  have hpos : 0 < ∑ m ∈ Finset.range (n + 1), T m :=
    Finset.sum_pos hT ⟨0, Finset.mem_range.2 (Nat.succ_pos n)⟩
  calc Real.log (∑ m ∈ Finset.range (n + 1), T m) ≤ Real.log (((n : ℝ) + 1) * Real.exp Q) :=
        Real.log_le_log hpos hle
    _ = Real.log ((n : ℝ) + 1) + Q := by
        rw [Real.log_mul (by positivity) (Real.exp_pos Q).ne', Real.log_exp]

theorem upperTerm_pos {p κ s0 c2 W : ℝ} {U : ℝ → ℝ} (hp : 0 < p) (hHup : TheoremHPure p κ s0)
    (hc2U : ∀ t, 0 < c2 * U t) (hW : 0 < W) {Mn n : ℕ} (hMn : 1 ≤ Mn) (m : ℕ) :
    0 < upperTerm p s0 c2 W U Mn n m := by
  have hanti : StrictAnti (powSeq p) := by
    intro a b hab
    exact Real.rpow_lt_rpow_of_neg (by positivity) (by exact_mod_cast Nat.add_lt_add_right hab 1) (by linarith)
  have hD := heineD_pos hanti (fun i => Real.rpow_pos_of_pos (by positivity : (0:ℝ) < (i:ℝ) + 1) (-s0))
    (hHup.bdd (n - m))
  have hF : (0 : ℝ) < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
  have hX : (0 : ℝ) < (Mn : ℝ) ^ (-p) := Real.rpow_pos_of_pos (by exact_mod_cast hMn) _
  unfold upperTerm
  have := hc2U Mn
  have := Real.rpow_pos_of_pos hF (-(2 * p * m))
  positivity

/-- `log n / n → 0` along ℕ. -/
theorem tendsto_log_div_nat : Tendsto (fun n : ℕ => Real.log n / n) atTop (𝓝 0) := by
  have := (Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero).comp tendsto_natCast_atTop_atTop
  simpa [Function.comp_def] using this

theorem tendsto_log_succ_div_sq : Tendsto (fun n : ℕ => Real.log ((n : ℝ) + 1) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  apply squeeze_zero' (Eventually.of_forall fun n => div_nonneg (Real.log_nonneg (by
    have := Nat.cast_nonneg (α := ℝ) n; linarith)) (sq_nonneg _)) _ tendsto_one_div_atTop_nhds_zero_nat
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hl : Real.log ((n : ℝ) + 1) ≤ n := by
    have := Real.log_le_sub_one_of_pos (by linarith : (0:ℝ) < (n:ℝ) + 1); linarith
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith

theorem HL_upper {p κ s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    (hHup : TheoremHPure p κ s0) (hc2 : 0 < c2)
    (hw0 : ∀ k, 0 < w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hU1 : ∀ t, 1 ≤ U t) (hUmono : Monotone U)
    (hUsub : Tendsto (fun n : ℕ => Real.log (U n) / n) atTop (𝓝 0)) (hwsum : Summable w)
    {M : ℕ} (hM : 2 ≤ M) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop,
      hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)) n ≤
        (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) + η := by
  have hp := hL.p_pos
  have hw : ∀ i, 0 ≤ w i := fun i => (hw0 i).le
  have hc2U : ∀ t, 0 < c2 * U t := fun t => mul_pos hc2 (by linarith [hU1 t])
  have hW : 0 < ∑' k, w k := hwsum.tsum_pos hw 0 (hw0 0)
  have hMr : (2 : ℝ) ≤ M := by exact_mod_cast hM
  have hMpos : (0 : ℝ) < M := by linarith
  obtain ⟨B, hB1, hB⟩ := hL.upper_pair
  obtain ⟨C, hC⟩ := hHup.uniform_upper (half_pos hη)
  set A2 := (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) with hA2
  -- the remainder
  set rem : ℕ → ℝ := fun n =>
    2 * a0 * n * Real.log B + (((n * (n - 1) : ℕ) : ℝ) * Real.log (L ((M : ℝ) * n)) - (n : ℝ) ^ 2 * Real.log (L n))
      + Real.log ((n : ℝ) + 1) + C
      + n * (|Real.log (c2 * U ((M : ℝ) * n))| + |Real.log (∑' k, w k)| + p * Real.log ((M : ℝ) * n)) with hrem
  -- (1) pointwise bound for n ≥ max 1 a0
  have hpt : ∀ n : ℕ, 1 ≤ n → a0 ≤ n →
      hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)) n ≤
        A2 + η / 2 + rem n / (n : ℝ) ^ 2 := by
    intro n hn hna
    have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
    have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by positivity
    have hMn : a0 ≤ M * n := hna.trans (Nat.le_mul_of_pos_left n (by omega))
    have hMn1 : 1 ≤ M * n := hn.trans (Nat.le_mul_of_pos_left n (by omega))
    have hDf := heineD_le (fun K => heineK_slow_le hL hB1 hB hHup hc2 hw0 hwhi hUmono hwsum hMn K)
    have hDpos := heineD_pos hL.slowAtom_strictAnti hw0 (slow_bdd hL hHup hc2 hw0 hwhi hUmono hwsum n)
    have hLMn : 0 < L ((M : ℝ) * n) := hL.L_pos _ (by nlinarith)
    have hTpos : ∀ m ∈ Finset.range (n + 1), 0 < upperTerm p s0 c2 (∑' k, w k) U (M * n) n m :=
      fun m _ => upperTerm_pos hp hHup hc2U hW hMn1 m
    have hsum := log_sum_le_of_log_le hTpos (fun m hm => by
      have := log_upperTerm_le hp (half_pos hη) hHup hC hc2U hW hM hn (Nat.lt_succ_iff.1 (Finset.mem_range.1 hm))
      exact this)
    have hlogD : Real.log (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w n) ≤
        (2 * a0 * n : ℕ) * Real.log B + ((n * (n - 1) : ℕ) : ℝ) * Real.log (L ((M : ℝ) * n)) +
        Real.log (∑ m ∈ Finset.range (n + 1), upperTerm p s0 c2 (∑' k, w k) U (M * n) n m) := by
      have hS : 0 < ∑ m ∈ Finset.range (n + 1), upperTerm p s0 c2 (∑' k, w k) U (M * n) n m :=
        Finset.sum_pos hTpos ⟨0, Finset.mem_range.2 (Nat.succ_pos n)⟩
      calc _ ≤ Real.log (B ^ (2 * a0 * n) * L ((M : ℝ) * n) ^ (n * (n - 1)) *
            ∑ m ∈ Finset.range (n + 1), upperTerm p s0 c2 (∑' k, w k) U (M * n) n m) := Real.log_le_log hDpos hDf
        _ = _ := by
          rw [Real.log_mul (by positivity) hS.ne', Real.log_mul (by positivity) (by positivity),
            Real.log_pow, Real.log_pow]
    unfold hnorm
    rw [div_le_iff₀ hn2]
    have e1 : (A2 + η / 2 + rem n / (n : ℝ) ^ 2) * (n : ℝ) ^ 2 = (A2 + η / 2) * (n : ℝ) ^ 2 + rem n := by
      field_simp
    rw [e1]
    simp only [hrem]
    push_cast at hlogD ⊢
    linarith [hlogD, hsum]
  -- (2) the remainder is o(n²)
  have hlogL := hL.logL_slow
  have hsh := slow_shift hL.E_lim hlogL (M : ℝ) (by linarith)
  have hP3 : Tendsto (fun n : ℕ => Real.log (L ((M : ℝ) * n)) / n) atTop (𝓝 0) := by
    have hb : Tendsto (fun n : ℕ => (|Real.log (L 1)| + E 1 * (Real.log M + Real.log n)) / n) atTop (𝓝 0) := by
      have h1 : Tendsto (fun n : ℕ => (|Real.log (L 1)| + E 1 * Real.log M) / (n : ℝ)) atTop (𝓝 0) :=
        tendsto_const_div_atTop_nhds_zero_nat _
      have h2 := tendsto_log_div_nat.const_mul (E 1)
      simp only [mul_zero] at h2
      have := h1.add h2
      simp only [add_zero] at this
      refine this.congr' ?_
      filter_upwards [eventually_ge_atTop 1] with n hn
      field_simp; ring
    apply squeeze_zero_norm' _ hb
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
    have hMn1 : (1 : ℝ) ≤ (M : ℝ) * n := by nlinarith
    have h := hlogL 1 ((M : ℝ) * n) le_rfl hMn1
    rw [div_one, Real.log_mul hMpos.ne' (by positivity)] at h
    rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0:ℝ) < n)]
    apply div_le_div_of_nonneg_right _ (by positivity)
    have := abs_sub_abs_le_abs_sub (Real.log (L ((M : ℝ) * n))) (Real.log (L 1))
    linarith
  have hU' : Tendsto (fun n : ℕ => Real.log (U ((M : ℝ) * n)) / n) atTop (𝓝 0) := by
    have hcomp : Tendsto (fun n : ℕ => M * n) atTop atTop :=
      tendsto_id.const_mul_atTop' (by omega : 0 < M)
    have := (hUsub.comp hcomp).const_mul (M : ℝ)
    simp only [mul_zero] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    simp only [Function.comp_apply]
    push_cast
    field_simp
  have hP6 : Tendsto (fun n : ℕ =>
      (|Real.log (c2 * U ((M : ℝ) * n))| + |Real.log (∑' k, w k)| + p * Real.log ((M : ℝ) * n)) / n) atTop (𝓝 0) := by
    have hb : Tendsto (fun n : ℕ =>
        (|Real.log c2| + |Real.log (∑' k, w k)| + p * Real.log M) / (n : ℝ) + Real.log (U ((M : ℝ) * n)) / n
          + p * (Real.log n / n)) atTop (𝓝 0) := by
      have := ((tendsto_const_div_atTop_nhds_zero_nat (|Real.log c2| + |Real.log (∑' k, w k)| + p * Real.log M)).add
        hU').add (tendsto_log_div_nat.const_mul p)
      simpa using this
    apply squeeze_zero' _ _ hb
    · filter_upwards [eventually_ge_atTop 1] with n hn
      have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
      apply div_nonneg _ (by positivity)
      have : 0 ≤ Real.log ((M : ℝ) * n) := Real.log_nonneg (by nlinarith)
      positivity
    · filter_upwards [eventually_ge_atTop 1] with n hn
      have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
      have hU1n := hU1 ((M : ℝ) * n)
      have hlogU : 0 ≤ Real.log (U ((M : ℝ) * n)) := Real.log_nonneg hU1n
      have habs : |Real.log (c2 * U ((M : ℝ) * n))| ≤ |Real.log c2| + Real.log (U ((M : ℝ) * n)) := by
        rw [Real.log_mul hc2.ne' (by linarith)]
        calc _ ≤ |Real.log c2| + |Real.log (U ((M : ℝ) * n))| := abs_add_le _ _
          _ = _ := by rw [abs_of_nonneg hlogU]
      have hlm : Real.log ((M : ℝ) * n) = Real.log M + Real.log n := Real.log_mul hMpos.ne' (by positivity)
      rw [hlm]
      have e : (|Real.log c2| + |Real.log (∑' k, w k)| + p * Real.log M) / (n : ℝ) +
          Real.log (U ((M : ℝ) * n)) / n + p * (Real.log n / n) =
          (|Real.log c2| + Real.log (U ((M : ℝ) * n)) + |Real.log (∑' k, w k)| + p * (Real.log M + Real.log n)) / n := by
        field_simp; ring
      rw [e]
      apply div_le_div_of_nonneg_right _ (by positivity)
      linarith
  have hremlim : Tendsto (fun n : ℕ => rem n / (n : ℝ) ^ 2) atTop (𝓝 0) := by
    have hP1 : Tendsto (fun n : ℕ => (2 * a0 * Real.log B) / (n : ℝ)) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat _
    have hP5 : Tendsto (fun n : ℕ => C / (n : ℝ) ^ 2) atTop (𝓝 0) := by
      have := (tendsto_const_div_atTop_nhds_zero_nat C).mul tendsto_one_div_atTop_nhds_zero_nat
      simp only [mul_zero] at this
      refine this.congr' ?_
      filter_upwards [eventually_ge_atTop 1] with n hn
      field_simp
    have hsum := ((((hP1.add hsh).sub hP3).add tendsto_log_succ_div_sq).add hP5).add hP6
    simp only [add_zero, sub_zero] at hsum
    refine hsum.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
    have hcast : (((n * (n - 1) : ℕ)) : ℝ) = (n : ℝ) * ((n : ℝ) - 1) := by
      rw [Nat.cast_mul, Nat.cast_sub hn]; push_cast; ring
    simp only [hrem, hcast]
    field_simp
    ring
  -- (3) combine
  have hev := hremlim.eventually (gt_mem_nhds (half_pos hη))
  filter_upwards [hev, eventually_ge_atTop (max 1 a0)] with n hrn hn
  have := hpt n (le_of_max_le_left hn) (le_of_max_le_right hn)
  linarith

end JacobiAsym
