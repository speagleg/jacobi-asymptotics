import JacobiAsym.ChainLimit

/-!
# Chain rate (Paper 2 §3, Lemma `lem:chain-rate`)

A *regular rate* `η` (Paper 2 §1, before Theorem `thm:shift`): `η_n > 0`, non-increasing, `n η_n`
non-decreasing, `η_n → 0`. If `U, V > 0`, `U_n + V_n − 2c = O(η_n)` and `U_n V_{n+1} − c² = O(η_n)`, then
`U_n − c = O(√η_n)` and `U_{n+1} − U_n = O(η_n)`.
-/

open Finset Filter Topology Asymptotics

namespace JacobiAsym

/-- Regular rate: `η_n > 0` non-increasing, `n η_n` non-decreasing, `η_n → 0`. -/
structure RegularRate (η : ℕ → ℝ) : Prop where
  pos : ∀ n, 0 < η n
  anti : Antitone η
  mono : Monotone fun n : ℕ => (n : ℝ) * η n
  tendsto : Tendsto η atTop (𝓝 0)

namespace RegularRate

variable {η : ℕ → ℝ}

theorem ge_inv (hη : RegularRate η) {n : ℕ} (hn : 1 ≤ n) : η 1 ≤ n * η n := by
  have := hη.mono hn; simpa using this

theorem le_two_mul (hη : RegularRate η) {n : ℕ} (hn : 1 ≤ n) : η n ≤ 2 * η (n + 1) := by
  have h := hη.mono (Nat.le_succ n)
  simp only [Nat.cast_succ] at h
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have := hη.pos (n + 1)
  nlinarith

theorem not_summable (hη : RegularRate η) : ¬ Summable η := by
  intro hs
  apply Real.not_summable_one_div_natCast
  have h1 : Summable fun n : ℕ => η 1 * (1 / (n : ℝ)) := by
    refine Summable.of_nonneg_of_le (fun n => mul_nonneg (hη.pos 1).le (by positivity)) (fun n => ?_) hs
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp [(hη.pos 0).le]
    · have := hη.ge_inv hn
      have hn' : (0 : ℝ) < n := by exact_mod_cast hn
      rw [mul_one_div, div_le_iff₀ hn']; linarith
  exact (summable_mul_left_iff (hη.pos 1).ne').1 h1

/-- A sequence bounded below cannot decrease by `M η_k` at every step `k ≥ m`. -/
theorem no_drift (hη : RegularRate η) {y : ℕ → ℝ} {B M : ℝ} {m : ℕ} (hM : 0 < M) (hy : ∀ k, -B ≤ y k)
    (h : ∀ k, m ≤ k → y (k + 1) ≤ y k - M * η k) : False := by
  have hsum : ∀ j, y (j + m) ≤ y m - M * ∑ i ∈ range j, η (i + m) := by
    intro j
    induction j with
    | zero => simp
    | succ j ih =>
      rw [sum_range_succ, show j + 1 + m = (j + m) + 1 by omega]
      have := h (j + m) (by omega)
      linarith
  apply hη.not_summable
  apply (summable_nat_add_iff m).1
  apply summable_of_sum_range_le (fun i => (hη.pos _).le) (c := (y m + B) / M)
  intro j
  rw [le_div_iff₀ hM]
  have := hsum j; have := hy (j + m)
  linarith

/-- `√η_n − √η_{n+1} ≤ η_n / √η_1` (`n ≥ 1`). -/
theorem sqrt_sub_le (hη : RegularRate η) {n : ℕ} (hn : 1 ≤ n) :
    Real.sqrt (η n) - Real.sqrt (η (n + 1)) ≤ η n / Real.sqrt (η 1) := by
  set a := Real.sqrt (η n)
  set b := Real.sqrt (η (n + 1))
  set r := Real.sqrt (η 1)
  have ha : 0 < a := Real.sqrt_pos.2 (hη.pos n)
  have hb : 0 < b := Real.sqrt_pos.2 (hη.pos _)
  have hr : 0 < r := Real.sqrt_pos.2 (hη.pos 1)
  have ha2 : a ^ 2 = η n := Real.sq_sqrt (hη.pos n).le
  have hb2 : b ^ 2 = η (n + 1) := Real.sq_sqrt (hη.pos _).le
  have hr2 : r ^ 2 = η 1 := Real.sq_sqrt (hη.pos 1).le
  have hba : b ≤ a := Real.sqrt_le_sqrt (hη.anti (Nat.le_succ n))
  have hmono := hη.mono (Nat.le_succ n)
  simp only [Nat.cast_succ] at hmono
  have hinv := hη.ge_inv hn
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
  -- (n+1)(a − b) ≤ a
  have h1 : ((n : ℝ) + 1) * (a - b) ≤ a := by
    have : ((n : ℝ) + 1) * (a - b) * a ≤ a * a := by
      have e : (n : ℝ) * a ^ 2 ≤ ((n : ℝ) + 1) * b ^ 2 := by rw [ha2, hb2]; exact hmono
      nlinarith
    exact le_of_mul_le_mul_right this ha
  -- r ≤ (n+1) a
  have h2 : r ≤ ((n : ℝ) + 1) * a := by
    by_contra hcon
    push Not at hcon
    have e : r ^ 2 ≤ (n : ℝ) * a ^ 2 := by rw [hr2, ha2]; exact hinv
    have := mul_self_lt_mul_self (by positivity : 0 ≤ ((n : ℝ) + 1) * a) hcon
    nlinarith [sq_nonneg a]
  rw [le_div_iff₀ hr, ← ha2]
  nlinarith

end RegularRate

theorem bigO_bound {f η : ℕ → ℝ} (hη : ∀ n, 0 < η n) (h : f =O[atTop] η) :
    ∃ K, 0 ≤ K ∧ ∀ᶠ n in atTop, |f n| ≤ K * η n := by
  obtain ⟨K, hK⟩ := h.bound
  refine ⟨max K 0, le_max_right _ _, hK.mono fun n hn => ?_⟩
  rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos (hη n)] at hn
  exact hn.trans (mul_le_mul_of_nonneg_right (le_max_left _ _) (hη n).le)

theorem bigO_of_bound {f η : ℕ → ℝ} {K : ℝ} (hη : ∀ n, 0 ≤ η n) (h : ∀ᶠ n in atTop, |f n| ≤ K * η n) :
    f =O[atTop] η :=
  IsBigO.of_bound K (h.mono fun n hn => by rwa [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg (hη n)])

theorem tendsto_of_bigO {f η : ℕ → ℝ} {L : ℝ} (hη : Tendsto η atTop (𝓝 0))
    (h : (fun n => f n - L) =O[atTop] η) : Tendsto f atTop (𝓝 L) := by
  have := (h.trans_tendsto hη).add_const L
  simpa using this

/-- Drift: far from `c`, the chain recursion decreases by `M η`. -/
theorem drift_ineq {c u u' y2 M e l : ℝ} (hc : 0 < c) (h : u' ≤ u - y2 / (2 * c) + M * e)
    (hy : l ^ 2 * e ≤ y2) (hl : 4 * c * M ≤ l ^ 2) (he : 0 ≤ e) : u' ≤ u - M * e := by
  have h1 : l ^ 2 * e / (2 * c) ≤ y2 / (2 * c) := div_le_div_of_nonneg_right hy (by positivity)
  have h2 : 2 * M * e ≤ l ^ 2 * e / (2 * c) := by
    rw [le_div_iff₀ (by positivity)]; nlinarith
  linarith

theorem far_sq {y l e : ℝ} (hl : 0 ≤ l) (he : 0 ≤ e) (h : l * Real.sqrt e ≤ |y|) : l ^ 2 * e ≤ y ^ 2 := by
  have := pow_le_pow_left₀ (by positivity) h 2
  rwa [sq_abs, mul_pow, Real.sq_sqrt he] at this

/-- **Chain rate, core form** (Paper 2 Lemma `lem:chain-rate`). -/
theorem chain_rate_core {c : ℝ} (hc : 0 < c) {U V η : ℕ → ℝ} (hη : RegularRate η)
    (hU : ∀ n, 0 < U n) (hV : ∀ n, 0 < V (n + 1))
    (hA : (fun n => U n + V n - 2 * c) =O[atTop] η)
    (hQ : (fun n => U n * V (n + 1) - c ^ 2) =O[atTop] η) :
    (fun n => U n - c) =O[atTop] (fun n => Real.sqrt (η n)) ∧
      (fun n => U (n + 1) - U n) =O[atTop] η := by
  obtain ⟨KA, hKA0, hKA⟩ := bigO_bound hη.pos hA
  obtain ⟨KQ, hKQ0, hKQ⟩ := bigO_bound hη.pos hQ
  have hUt := (chain_limit_core hc hU hV (tendsto_of_bigO hη.tendsto hA) (tendsto_of_bigO hη.tendsto hQ)).1
  set M1 := KA + 2 * KQ / c + 1 with hM1def
  have hM1 : 0 < M1 := by have : 0 ≤ 2 * KQ / c := by positivity
                          linarith
  have hwin : ∀ᶠ n in atTop, c / 2 ≤ U n ∧ U n ≤ 2 * c := by
    have := hUt.eventually (Icc_mem_nhds (show c / 2 < c by linarith) (show c < 2 * c by linarith))
    exact this.mono fun n hn => hn
  -- the perturbed recursion
  have hkey : ∀ᶠ n in atTop, c / 2 ≤ U n ∧ U n ≤ 2 * c ∧
      |U (n + 1) - (U n - (U n - c) ^ 2 / U n)| ≤ M1 * η n := by
    filter_upwards [hwin, (tendsto_add_atTop_nat 1).eventually hKA, hKQ] with n hw hA' hQ'
    refine ⟨hw.1, hw.2, ?_⟩
    have hUn := hU n
    have e : U (n + 1) - (U n - (U n - c) ^ 2 / U n) =
        (U (n + 1) + V (n + 1) - 2 * c) - (U n * V (n + 1) - c ^ 2) / U n := by
      field_simp; ring
    rw [e]
    have hη1 : η (n + 1) ≤ η n := hη.anti (Nat.le_succ n)
    have hd : |(U n * V (n + 1) - c ^ 2) / U n| ≤ 2 * KQ / c * η n := by
      rw [abs_div, abs_of_pos hUn, div_le_iff₀ hUn]
      have h3 : KQ ≤ 2 * KQ / c * U n := by
        rw [div_mul_eq_mul_div, le_div_iff₀ hc]; nlinarith [hw.1]
      have := hη.pos n
      calc _ ≤ KQ * η n := hQ'
        _ ≤ 2 * KQ / c * U n * η n := mul_le_mul_of_nonneg_right h3 this.le
        _ = _ := by ring
    have hηn := hη.pos n
    have hdd : 0 ≤ 2 * KQ / c * η n := by positivity
    calc _ ≤ |U (n + 1) + V (n + 1) - 2 * c| + |(U n * V (n + 1) - c ^ 2) / U n| := abs_sub _ _
      _ ≤ KA * η n + 2 * KQ / c * η n :=
          add_le_add (hA'.trans (mul_le_mul_of_nonneg_left hη1 hKA0)) hd
      _ ≤ M1 * η n := by rw [hM1def]; nlinarith
  -- one-sided form
  have hI : ∀ n, c / 2 ≤ U n → U n ≤ 2 * c → |U (n + 1) - (U n - (U n - c) ^ 2 / U n)| ≤ M1 * η n →
      U (n + 1) ≤ U n - (U n - c) ^ 2 / (2 * c) + M1 * η n := by
    intro n h1 h2 h3
    have : (U n - c) ^ 2 / (2 * c) ≤ (U n - c) ^ 2 / U n :=
      div_le_div_of_nonneg_left (sq_nonneg _) (hU n) h2
    have := (abs_le.1 h3).2
    linarith
  -- the constant λ
  set r := Real.sqrt (η 1) with hr
  have hr0 : 0 < r := Real.sqrt_pos.2 (hη.pos 1)
  set lam := max (4 * c / r) (2 * Real.sqrt (c * M1)) with hlam
  have hlam0 : 0 ≤ lam := le_max_of_le_left (by positivity)
  have hlam1 : 4 * c * M1 ≤ lam ^ 2 := by
    have h := le_max_right (4 * c / r) (2 * Real.sqrt (c * M1))
    have hs : Real.sqrt (c * M1) ^ 2 = c * M1 := Real.sq_sqrt (by positivity)
    have h0 : 0 ≤ 2 * Real.sqrt (c * M1) := by positivity
    nlinarith
  have hlam2 : lam / r ≤ lam ^ 2 / (2 * c) - M1 := by
    have h := le_max_left (4 * c / r) (2 * Real.sqrt (c * M1))
    have h' : 4 * c ≤ lam * r := by rw [div_le_iff₀ hr0] at h; exact h
    have e1 : lam / r ≤ lam ^ 2 / (4 * c) := by
      rw [div_le_div_iff₀ hr0 (by positivity)]; nlinarith
    have e2 : M1 ≤ lam ^ 2 / (4 * c) := by rw [le_div_iff₀ (by positivity)]; linarith
    have e3 : lam ^ 2 / (2 * c) = lam ^ 2 / (4 * c) + lam ^ 2 / (4 * c) := by field_simp; ring
    linarith
  -- the threshold N
  have hsmall : ∀ᶠ n in atTop, lam * Real.sqrt (η n) ≤ c := by
    have : Tendsto (fun n => lam * Real.sqrt (η n)) atTop (𝓝 (lam * Real.sqrt 0)) :=
      (hη.tendsto.sqrt).const_mul lam
    rw [Real.sqrt_zero, mul_zero] at this
    exact this.eventually (ge_mem_nhds hc)
  obtain ⟨N, hN⟩ := eventually_atTop.1 (hkey.and (hsmall.and (eventually_ge_atTop 1)))
  have hsq : ∀ n, (Real.sqrt (η n)) ^ 2 = η n := fun n => Real.sq_sqrt (hη.pos n).le
  have hsqrt_anti : ∀ n, Real.sqrt (η (n + 1)) ≤ Real.sqrt (η n) :=
    fun n => Real.sqrt_le_sqrt (hη.anti (Nat.le_succ n))
  -- drift when far
  have hfar : ∀ n, N ≤ n → lam ^ 2 * η n ≤ (U n - c) ^ 2 → U (n + 1) ≤ U n - M1 * η n := by
    intro n hn hy
    obtain ⟨⟨h1, h2, h3⟩, -, -⟩ := hN n hn
    exact drift_ineq hc (hI n h1 h2 h3) hy hlam1 (hη.pos n).le
  -- lower bound
  have hlow : ∀ n, N ≤ n → -(lam * Real.sqrt (η n)) < U n - c := by
    intro m hm
    by_contra hcon
    push Not at hcon
    have hstay : ∀ k, m ≤ k → U k - c ≤ -(lam * Real.sqrt (η k)) := by
      intro k hk
      induction k, hk using Nat.le_induction with
      | base => exact hcon
      | succ k hk ih =>
        have hy : lam ^ 2 * η k ≤ (U k - c) ^ 2 :=
          far_sq hlam0 (hη.pos k).le (le_abs.2 (Or.inr (by linarith)))
        have := hfar k (by omega) hy
        have := mul_le_mul_of_nonneg_left (hsqrt_anti k) hlam0
        have := hη.pos k
        nlinarith
    apply hη.no_drift (y := fun k => U k - c) (B := c) (m := m) hM1 (fun k => by linarith [hU k])
    intro k hk
    have hy : lam ^ 2 * η k ≤ (U k - c) ^ 2 :=
      far_sq hlam0 (hη.pos k).le (le_abs.2 (Or.inr (by linarith [hstay k hk])))
    have := hfar k (by omega) hy
    linarith
  -- upper bound: step
  have hstep : ∀ n, N ≤ n → U n - c ≤ lam * Real.sqrt (η n) →
      U (n + 1) - c ≤ lam * Real.sqrt (η (n + 1)) := by
    intro n hn hy
    obtain ⟨⟨h1, h2, h3⟩, h4, h5⟩ := hN n hn
    have hrec := hI n h1 h2 h3
    set t := lam * Real.sqrt (η n) with ht
    have ht0 : 0 ≤ t := by positivity
    have hφ : (U n - c) - (U n - c) ^ 2 / (2 * c) ≤ t - t ^ 2 / (2 * c) := by
      have : t ^ 2 / (2 * c) - (U n - c) ^ 2 / (2 * c) ≤ t - (U n - c) := by
        rw [← sub_div, div_le_iff₀ (by positivity)]
        nlinarith
      linarith
    have ht2 : t ^ 2 = lam ^ 2 * η n := by rw [ht, mul_pow, hsq]
    have hdec := mul_le_mul_of_nonneg_left (hη.sqrt_sub_le h5) hlam0
    have hηn := (hη.pos n).le
    have hl2 : lam / r * η n ≤ (lam ^ 2 / (2 * c) - M1) * η n := mul_le_mul_of_nonneg_right hlam2 hηn
    have e1 : t ^ 2 / (2 * c) = lam ^ 2 / (2 * c) * η n := by rw [ht2]; ring
    have e2 : lam * (η n / r) = lam / r * η n := by ring
    rw [e2] at hdec
    nlinarith
  -- upper bound: entry
  have hentry : ∃ m, N ≤ m ∧ U m - c ≤ lam * Real.sqrt (η m) := by
    by_contra hcon
    push Not at hcon
    apply hη.no_drift (y := fun k => U k - c) (B := c) (m := N) hM1 (fun k => by linarith [hU k])
    intro k hk
    have hy : lam ^ 2 * η k ≤ (U k - c) ^ 2 :=
      far_sq hlam0 (hη.pos k).le (le_abs.2 (Or.inl (hcon k hk).le))
    have := hfar k hk hy
    linarith
  obtain ⟨m, hNm, hm⟩ := hentry
  have hup : ∀ k, m ≤ k → U k - c ≤ lam * Real.sqrt (η k) := by
    intro k hk
    induction k, hk using Nat.le_induction with
    | base => exact hm
    | succ k hk ih => exact hstep k (by omega) ih
  have hboth : ∀ k, m ≤ k → |U k - c| ≤ lam * Real.sqrt (η k) :=
    fun k hk => abs_le.2 ⟨(hlow k (by omega)).le, hup k hk⟩
  constructor
  · refine bigO_of_bound (fun n => Real.sqrt_nonneg _) (K := lam) ?_
    exact eventually_atTop.2 ⟨m, hboth⟩
  · refine bigO_of_bound (fun n => (hη.pos n).le) (K := 2 * lam ^ 2 / c + M1) ?_
    refine eventually_atTop.2 ⟨m, fun n hn => ?_⟩
    obtain ⟨⟨h1, h2, h3⟩, -, -⟩ := hN n (by omega)
    have hb := hboth n hn
    have hy2 : (U n - c) ^ 2 ≤ lam ^ 2 * η n := by
      rw [← hsq n, ← mul_pow]; exact sq_le_sq' (abs_le.1 hb).1 (abs_le.1 hb).2
    have hdiv : (U n - c) ^ 2 / U n ≤ 2 * lam ^ 2 / c * η n := by
      rw [div_le_iff₀ (hU n)]
      have : lam ^ 2 * η n ≤ 2 * lam ^ 2 / c * η n * U n := by
        have e : 2 * lam ^ 2 / c * η n * U n = lam ^ 2 * η n * (2 * U n / c) := by ring
        rw [e]
        have : 1 ≤ 2 * U n / c := by rw [le_div_iff₀ hc]; linarith
        have := mul_nonneg (sq_nonneg lam) (hη.pos n).le
        nlinarith
      linarith
    have e : U (n + 1) - U n = (U (n + 1) - (U n - (U n - c) ^ 2 / U n)) - (U n - c) ^ 2 / U n := by ring
    rw [e]
    have h0 : 0 ≤ (U n - c) ^ 2 / U n := div_nonneg (sq_nonneg _) (hU n).le
    calc _ ≤ |U (n + 1) - (U n - (U n - c) ^ 2 / U n)| + |(U n - c) ^ 2 / U n| := abs_sub _ _
      _ ≤ M1 * η n + 2 * lam ^ 2 / c * η n := by rw [abs_of_nonneg h0]; linarith
      _ = _ := by ring

end JacobiAsym
