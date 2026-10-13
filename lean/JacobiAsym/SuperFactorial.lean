import JacobiAsym.UpperBound

open Finset Filter Topology

namespace JacobiAsym

/-- One MVT step: if `g' = φ` on `[1, ∞)` with `φ` monotone there, then
`φ m ≤ g (m+1) - g m ≤ φ (m+1)` for `m ≥ 1`. -/
theorem mvt_step {g φ : ℝ → ℝ} (hg : ∀ t, 1 ≤ t → HasDerivAt g (φ t) t) (hφ : MonotoneOn φ (Set.Ici 1))
    {m : ℝ} (hm : 1 ≤ m) : φ m ≤ g (m + 1) - g m ∧ g (m + 1) - g m ≤ φ (m + 1) := by
  obtain ⟨c, hc, hcs⟩ := exists_hasDerivAt_eq_slope g φ (by linarith : m < m + 1)
    (fun t ht => (hg t (hm.trans ht.1)).continuousAt.continuousWithinAt)
    (fun t ht => hg t (hm.trans ht.1.le))
  rw [show m + 1 - m = 1 by ring, div_one] at hcs
  rw [← hcs]
  exact ⟨hφ (Set.mem_Ici.2 hm) (Set.mem_Ici.2 (hm.trans hc.1.le)) hc.1.le,
    hφ (Set.mem_Ici.2 (hm.trans hc.1.le)) (Set.mem_Ici.2 (by linarith)) hc.2.le⟩

/-- Telescoped MVT bounds over `Ico 1 n`. -/
theorem telescope_bounds {g φ : ℝ → ℝ} (hg : ∀ t, 1 ≤ t → HasDerivAt g (φ t) t)
    (hφ : MonotoneOn φ (Set.Ici 1)) (n : ℕ) (hn : 1 ≤ n) :
    ∑ m ∈ Ico 1 n, φ m ≤ g n - g 1 ∧ g n - g 1 ≤ ∑ m ∈ Ico 1 n, φ ((m : ℝ) + 1) := by
  induction n with
  | zero => omega
  | succ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn'
    · simp
    · obtain ⟨ih1, ih2⟩ := ih hn'
      have hstep := mvt_step hg hφ (show (1 : ℝ) ≤ n by exact_mod_cast hn')
      rw [sum_Ico_succ_top hn', sum_Ico_succ_top hn']
      push_cast
      constructor <;> linarith [hstep.1, hstep.2]

/-- `∑_{j=1}^{n-1} (n-j) log j = ∑_{m=1}^{n-1} ∑_{j=1}^{m} log j`. -/
theorem sum_weighted_eq_double (n : ℕ) :
    ∑ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log j = ∑ m ∈ Ico 1 n, ∑ j ∈ Ico 1 (m + 1), Real.log j := by
  induction n with
  | zero => simp
  | succ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp
    rw [sum_Ico_succ_top hn, sum_Ico_succ_top hn, ← ih]
    have e : ∑ j ∈ Ico 1 n, (((n + 1 : ℕ) : ℝ) - j) * Real.log j =
        ∑ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log j + ∑ j ∈ Ico 1 n, Real.log j := by
      rw [← sum_add_distrib]; apply sum_congr rfl; intro j _; push_cast; ring
    rw [e, sum_Ico_succ_top hn]
    push_cast; ring

/-- `∑_{j=1}^{n-1} (n-j) log j = (n²/2) log n - (3/4) n² + o(n²)`. -/
theorem sum_shift (f : ℝ → ℝ) (n : ℕ) (hn : 1 ≤ n) :
    ∑ m ∈ Ico 1 n, f ((m : ℝ) + 1) = ∑ m ∈ Ico 1 n, f m + (f n - f 1) := by
  induction n with
  | zero => omega
  | succ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn'
    · simp
    · rw [sum_Ico_succ_top hn', sum_Ico_succ_top hn', ih hn']; push_cast; ring

theorem sum_Ico_id (n : ℕ) : ∑ m ∈ Ico 1 n, (m : ℝ) = (n : ℝ) * ((n : ℝ) - 1) / 2 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn'
    · simp
    · rw [sum_Ico_succ_top hn', ih]; push_cast; ring

theorem g1_deriv {t : ℝ} (ht : 1 ≤ t) : HasDerivAt (fun t : ℝ => t * Real.log t - t) (Real.log t) t := by
  have := (Real.hasDerivAt_mul_log (by linarith : t ≠ 0)).sub (hasDerivAt_id t)
  convert this using 1
  · funext x; simp only [Pi.sub_apply, id]
  · ring

theorem g2_deriv {t : ℝ} (ht : 1 ≤ t) :
    HasDerivAt (fun t : ℝ => t ^ 2 / 2 * Real.log t - t ^ 2 / 4) (t * Real.log t) t := by
  have ht0 : t ≠ 0 := by linarith
  have := (((hasDerivAt_pow 2 t).div_const 2).mul (Real.hasDerivAt_log ht0)).sub ((hasDerivAt_pow 2 t).div_const 4)
  convert this using 1
  field_simp
  ring

theorem log_monoOn : MonotoneOn Real.log (Set.Ici 1) :=
  Real.strictMonoOn_log.monotoneOn.mono (fun _t ht => Set.mem_Ioi.2 (lt_of_lt_of_le one_pos (Set.mem_Ici.1 ht)))

theorem xlogx_monoOn : MonotoneOn (fun t : ℝ => t * Real.log t) (Set.Ici 1) := by
  intro a ha b hb hab
  have ha' : (1 : ℝ) ≤ a := ha
  exact mul_le_mul hab (log_monoOn ha hb hab) (Real.log_nonneg ha') (by linarith)

theorem sum_log_weighted_asymp :
    Tendsto (fun n : ℕ => (∑ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log j -
      ((n : ℝ) ^ 2 / 2 * Real.log n - 3 / 4 * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  -- pointwise bound for n ≥ 1
  have hbd : ∀ n : ℕ, 1 ≤ n →
      |∑ j ∈ Ico 1 n, ((n : ℝ) - j) * Real.log j - ((n : ℝ) ^ 2 / 2 * Real.log n - 3 / 4 * (n : ℝ) ^ 2)| ≤
        (n : ℝ) * Real.log n + (n : ℝ) / 2 + 1 / 4 := by
    intro n hn
    have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
    -- inner bounds on ∑_{j=1}^{m} log j
    have hin : ∀ m ∈ Ico 1 n, (m : ℝ) * Real.log m - m ≤ ∑ j ∈ Ico 1 (m + 1), Real.log j ∧
        ∑ j ∈ Ico 1 (m + 1), Real.log j ≤ ((m : ℝ) + 1) * Real.log ((m : ℝ) + 1) - m := by
      intro m hm
      have hm1 : (1 : ℝ) ≤ m := by exact_mod_cast (mem_Ico.1 hm).1
      obtain ⟨t1, t2⟩ := telescope_bounds (fun t ht => g1_deriv ht) log_monoOn (m + 1) (by omega)
      have hsh := sum_shift Real.log (m + 1) (by omega)
      push_cast at t1 t2 hsh
      rw [hsh] at t2
      simp only [Real.log_one, mul_zero, zero_sub, sub_zero] at t1 t2
      have hlog : Real.log m ≤ Real.log ((m : ℝ) + 1) := Real.log_le_log (by linarith) (by linarith)
      constructor
      · nlinarith
      · linarith
    rw [sum_weighted_eq_double]
    have hlo : ∑ m ∈ Ico 1 n, ((m : ℝ) * Real.log m - m) ≤ ∑ m ∈ Ico 1 n, ∑ j ∈ Ico 1 (m + 1), Real.log j :=
      sum_le_sum fun m hm => (hin m hm).1
    have hhi : ∑ m ∈ Ico 1 n, ∑ j ∈ Ico 1 (m + 1), Real.log j ≤
        ∑ m ∈ Ico 1 n, (((m : ℝ) + 1) * Real.log ((m : ℝ) + 1) - m) := sum_le_sum fun m hm => (hin m hm).2
    rw [sum_sub_distrib] at hlo hhi
    obtain ⟨T1, T2⟩ := telescope_bounds (fun t ht => g2_deriv ht) xlogx_monoOn n hn
    have hsh2 := sum_shift (fun t : ℝ => t * Real.log t) n hn
    rw [hsh2] at T2
    rw [hsh2] at hhi
    have hid := sum_Ico_id n
    simp only [Real.log_one, mul_zero, one_pow, sub_zero] at T1 T2 hsh2 hhi
    have hlogn : 0 ≤ Real.log n := Real.log_nonneg hnr
    rw [abs_le]
    constructor <;> nlinarith
  -- squeeze
  have hb : Tendsto (fun n : ℕ => Real.log n / n + 1 / (2 * (n : ℝ)) + 1 / (4 * (n : ℝ) ^ 2)) atTop (𝓝 0) := by
    have h1 := tendsto_log_div_nat
    have h2 : Tendsto (fun n : ℕ => 1 / (2 * (n : ℝ))) atTop (𝓝 0) := by
      have := (tendsto_const_div_atTop_nhds_zero_nat (1 / 2 : ℝ))
      refine this.congr' ?_
      filter_upwards with n; field_simp
    have h3 : Tendsto (fun n : ℕ => 1 / (4 * (n : ℝ) ^ 2)) atTop (𝓝 0) := by
      have := (tendsto_const_div_atTop_nhds_zero_nat (1 / 4 : ℝ)).mul tendsto_one_div_atTop_nhds_zero_nat
      simp only [mul_zero] at this
      refine this.congr' ?_
      filter_upwards with n; field_simp
    simpa using (h1.add h2).add h3
  apply squeeze_zero_norm' _ hb
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hnr : (0 : ℝ) < n := by exact_mod_cast hn
  rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0:ℝ) < (n:ℝ)^2)]
  rw [div_le_iff₀ (by positivity)]
  have := hbd n hn
  have e : (Real.log n / n + 1 / (2 * (n : ℝ)) + 1 / (4 * (n : ℝ) ^ 2)) * (n : ℝ) ^ 2 =
      (n : ℝ) * Real.log n + (n : ℝ) / 2 + 1 / 4 := by field_simp
  rw [e]; exact this

end JacobiAsym
