import JacobiAsym.Basic

open Finset Filter Topology

namespace JacobiAsym

/-- `∑_{1≤i<n} log (n/i) ≤ n` (from `nⁿ/n! ≤ eⁿ`). -/
theorem sum_log_div_le (n : ℕ) : ∑ i ∈ Ico 1 n, Real.log ((n : ℝ) / i) ≤ n := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  have hsplit : ∑ i ∈ Ico 1 n, Real.log ((n : ℝ) / i) ≤ ∑ k ∈ range n, Real.log ((n : ℝ) / (k + 1)) := by
    rw [sum_Ico_eq_sum_range]
    obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    rw [show m + 1 - 1 = m by omega, sum_range_succ (fun k => Real.log (((m + 1 : ℕ) : ℝ) / (k + 1)))]
    have : Real.log (((m + 1 : ℕ) : ℝ) / ((m : ℝ) + 1)) = 0 := by
      rw [Nat.cast_add, Nat.cast_one, div_self (by positivity), Real.log_one]
    rw [this, add_zero]
    apply le_of_eq; apply sum_congr rfl; intro k _; push_cast; ring_nf
  refine hsplit.trans ?_
  rw [← Real.log_prod (fun k _ => by positivity), prod_div_distrib, prod_const, card_range]
  have hfac : ∏ k ∈ range n, ((k : ℝ) + 1) = (n.factorial : ℝ) := by
    rw [← prod_range_add_one_eq_factorial, Nat.cast_prod]; push_cast; rfl
  rw [hfac, Real.log_le_iff_le_exp (by positivity)]
  exact Real.pow_div_factorial_le_exp _ (by positivity) n

/-- Lemma H6(b): `(2/n²) ∑_{1≤i<n} (n-i)(ℓ i - ℓ n) → 0` under `|ℓ y - ℓ x| ≤ E x · log (y/x)` (`1 ≤ x ≤ y`),
`E ≥ 0` antitone, `E → 0`. -/
theorem weighted_cesaro_slow {ℓ E : ℝ → ℝ} (hE0 : ∀ x, 0 ≤ E x) (hEanti : Antitone E)
    (hE : Tendsto E atTop (𝓝 0))
    (hℓ : ∀ x y : ℝ, 1 ≤ x → x ≤ y → |ℓ y - ℓ x| ≤ E x * Real.log (y / x)) :
    Tendsto (fun n : ℕ => (2 * ∑ i ∈ Ico 1 n, ((n : ℝ) - i) * (ℓ i - ℓ n)) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  -- (1) termwise bound by (2/n) ∑ E i log (n/i)
  have hbound : ∀ n : ℕ, 1 ≤ n →
      ‖(2 * ∑ i ∈ Ico 1 n, ((n : ℝ) - i) * (ℓ i - ℓ n)) / (n : ℝ) ^ 2‖ ≤
        2 * (∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)) / n := by
    intro n hn
    have hnpos : (0 : ℝ) < n := by exact_mod_cast hn
    have hterm : ∀ i ∈ Ico 1 n, |((n : ℝ) - i) * (ℓ i - ℓ n)| ≤ n * (E i * Real.log ((n : ℝ) / i)) := by
      intro i hi
      obtain ⟨hi1, hin⟩ := mem_Ico.1 hi
      have hi1' : (1 : ℝ) ≤ i := by exact_mod_cast hi1
      have hin' : (i : ℝ) ≤ n := by exact_mod_cast hin.le
      have h := hℓ i n hi1' hin'
      have hni : 0 ≤ (n : ℝ) - i := by linarith
      rw [abs_mul, abs_of_nonneg hni, abs_sub_comm]
      calc ((n : ℝ) - i) * |ℓ n - ℓ i| ≤ n * |ℓ n - ℓ i| := by gcongr; linarith
        _ ≤ n * (E i * Real.log ((n : ℝ) / i)) := by gcongr
    have hsum : |∑ i ∈ Ico 1 n, ((n : ℝ) - i) * (ℓ i - ℓ n)| ≤
        n * ∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i) := by
      rw [mul_sum]; exact (abs_sum_le_sum_abs _ _).trans (sum_le_sum hterm)
    rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0 : ℝ) < (n : ℝ) ^ 2), abs_mul, abs_two]
    calc 2 * |∑ i ∈ Ico 1 n, ((n : ℝ) - i) * (ℓ i - ℓ n)| / (n : ℝ) ^ 2
        ≤ 2 * (n * ∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)) / (n : ℝ) ^ 2 := by gcongr
      _ = 2 * (∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)) / n := by field_simp
  -- (2) the bound tends to 0
  have hlim : Tendsto (fun n : ℕ => 2 * (∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)) / n) atTop (𝓝 0) := by
    rw [Metric.tendsto_atTop]
    intro ε hε
    obtain ⟨X0, hX0⟩ := (Metric.tendsto_atTop.1 hE) (ε / 8) (by positivity)
    obtain ⟨N0, hN0X, hN01⟩ : ∃ N0 : ℕ, X0 ≤ N0 ∧ 1 ≤ N0 :=
      ⟨⌈max X0 1⌉₊, (le_max_left _ _).trans (Nat.le_ceil _),
        by exact_mod_cast (le_max_right X0 1).trans (Nat.le_ceil _)⟩
    have hlogn : Tendsto (fun n : ℕ => Real.log n / n) atTop (𝓝 0) := by
      have := (Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero).comp tendsto_natCast_atTop_atTop
      simpa [Function.comp_def] using this
    set C : ℝ := 2 * N0 * E 1 + 1 with hC
    have hCpos : 0 < C := by have := hE0 1; positivity
    obtain ⟨N1, hN1⟩ := (Metric.tendsto_atTop.1 hlogn) (ε / (2 * C)) (by positivity)
    refine ⟨max N1 1, fun n hn => ?_⟩
    have hn1 : 1 ≤ n := le_of_max_le_right hn
    have hnN1 : N1 ≤ n := le_of_max_le_left hn
    have hnpos : (0 : ℝ) < n := by exact_mod_cast hn1
    have hlog_n : 0 ≤ Real.log n := Real.log_nonneg (by exact_mod_cast hn1)
    -- termwise split
    have hsplit : ∀ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i) ≤
        (if i < N0 then E 1 * Real.log n else 0) + ε / 8 * Real.log ((n : ℝ) / i) := by
      intro i hi
      obtain ⟨hi1, hin⟩ := mem_Ico.1 hi
      have hi1' : (1 : ℝ) ≤ i := by exact_mod_cast hi1
      have hipos : (0 : ℝ) < i := by linarith
      have hlog0 : 0 ≤ Real.log ((n : ℝ) / i) :=
        Real.log_nonneg (by rw [le_div_iff₀ hipos, one_mul]; exact_mod_cast hin.le)
      split_ifs with hiN
      · have hEi : E i ≤ E 1 := hEanti hi1'
        have hlogle : Real.log ((n : ℝ) / i) ≤ Real.log n :=
          Real.log_le_log (by positivity) (div_le_self hnpos.le hi1')
        have := hE0 i
        nlinarith
      · have hiX : X0 ≤ (i : ℝ) := hN0X.trans (by exact_mod_cast not_lt.1 hiN)
        have hEi := hX0 i hiX
        rw [Real.dist_eq, sub_zero, abs_lt] at hEi
        nlinarith
    have hS : ∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i) ≤
        N0 * (E 1 * Real.log n) + ε / 8 * n := by
      calc ∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)
          ≤ ∑ i ∈ Ico 1 n, ((if i < N0 then E 1 * Real.log n else 0) + ε / 8 * Real.log ((n : ℝ) / i)) :=
            sum_le_sum hsplit
        _ = (((Ico 1 n).filter (· < N0)).card : ℝ) * (E 1 * Real.log n) +
              ε / 8 * ∑ i ∈ Ico 1 n, Real.log ((n : ℝ) / i) := by
            rw [sum_add_distrib, sum_ite, sum_const_zero, add_zero, sum_const, nsmul_eq_mul, mul_sum]
        _ ≤ N0 * (E 1 * Real.log n) + ε / 8 * n := by
            have hc : (((Ico 1 n).filter (· < N0)).card : ℝ) ≤ N0 := by
              have : ((Ico 1 n).filter (· < N0)) ⊆ range N0 := fun i hi => mem_range.2 (mem_filter.1 hi).2
              exact_mod_cast (card_le_card this).trans (card_range N0).le
            have hE1 : 0 ≤ E 1 * Real.log n := mul_nonneg (hE0 1) hlog_n
            gcongr
            exact sum_log_div_le n
    have hlogsmall := hN1 n hnN1
    rw [Real.dist_eq, sub_zero, abs_lt] at hlogsmall
    have hval_nonneg : 0 ≤ 2 * (∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)) / n := by
      apply div_nonneg _ hnpos.le
      apply mul_nonneg two_pos.le
      apply sum_nonneg; intro i hi
      obtain ⟨hi1, hin⟩ := mem_Ico.1 hi
      have hi1' : (1 : ℝ) ≤ i := by exact_mod_cast hi1
      apply mul_nonneg (hE0 _)
      exact Real.log_nonneg (by rw [le_div_iff₀ (by linarith), one_mul]; exact_mod_cast hin.le)
    rw [Real.dist_eq, sub_zero, abs_of_nonneg hval_nonneg]
    have hfirst : 2 * (N0 * (E 1 * Real.log n)) / n < ε / 2 := by
      have h1 : 2 * (N0 * (E 1 * Real.log n)) / n = (2 * N0 * E 1) * (Real.log n / n) := by
        field_simp
      rw [h1]
      have h2 : (2 * N0 * E 1) * (Real.log n / n) ≤ C * (Real.log n / n) := by
        apply mul_le_mul_of_nonneg_right (by linarith) (div_nonneg hlog_n hnpos.le)
      have h3 : C * (Real.log n / n) < C * (ε / (2 * C)) := mul_lt_mul_of_pos_left hlogsmall.2 hCpos
      have h4 : C * (ε / (2 * C)) = ε / 2 := by field_simp
      linarith
    calc 2 * (∑ i ∈ Ico 1 n, E i * Real.log ((n : ℝ) / i)) / n
        ≤ 2 * (N0 * (E 1 * Real.log n) + ε / 8 * n) / n := by gcongr
      _ = 2 * (N0 * (E 1 * Real.log n)) / n + ε / 4 := by field_simp; ring
      _ < ε := by linarith
  -- (3) squeeze
  apply squeeze_zero_norm' _ hlim
  filter_upwards [eventually_ge_atTop 1] with n hn
  exact hbound n hn

/-- Lemma H6(d): `ℓ (M n) - ℓ n → 0` for fixed `M ≥ 1`. -/
theorem slow_shift {ℓ E : ℝ → ℝ} (hE : Tendsto E atTop (𝓝 0))
    (hℓ : ∀ x y : ℝ, 1 ≤ x → x ≤ y → |ℓ y - ℓ x| ≤ E x * Real.log (y / x)) (M : ℝ) (hM : 1 ≤ M) :
    Tendsto (fun n : ℕ => ℓ (M * n) - ℓ n) atTop (𝓝 0) := by
  have hlim : Tendsto (fun n : ℕ => E n * Real.log M) atTop (𝓝 0) := by
    simpa using (hE.comp tendsto_natCast_atTop_atTop).mul_const (Real.log M)
  apply squeeze_zero_norm' _ hlim
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hle : (n : ℝ) ≤ M * n := le_mul_of_one_le_left (by linarith) hM
  have h := hℓ n (M * n) hn' hle
  rw [mul_div_assoc, div_self (by positivity), mul_one] at h
  rwa [Real.norm_eq_abs]

end JacobiAsym
