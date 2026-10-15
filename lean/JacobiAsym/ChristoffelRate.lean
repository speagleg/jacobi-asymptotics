import JacobiAsym.Christoffel
import JacobiAsym.ChainRate

/-!
# The Christoffel shift with a rate (Paper 2 Theorem `thm:shift`, rate part)

If `s_n a_n − 2c = O(η_n)` and `s_n b_n − c = O(η_n)` for a regular rate `η` (and `s_n/s_{n+1} − 1 = O(η_n)`,
true for `s_n = n^p`), then the same holds for the Jacobi coefficients of `xσ`.
-/

open Finset Filter Topology Asymptotics Polynomial

namespace JacobiAsym

theorem bigO_shift {η : ℕ → ℝ} (hη : RegularRate η) : (fun n => η (n + 1)) =O[atTop] η :=
  bigO_of_bound (K := 1) (fun n => (hη.pos n).le) (Eventually.of_forall fun n => by
    rw [abs_of_pos (hη.pos _), one_mul]; exact hη.anti (Nat.le_succ n))

theorem bigO_mul_tendsto {f g η : ℕ → ℝ} {L : ℝ} (h : f =O[atTop] η) (hg : Tendsto g atTop (𝓝 L)) :
    (fun n => f n * g n) =O[atTop] η := by
  simpa using h.mul (hg.isBigO_one ℝ)

/-- Shift an `O(η)` statement by one index. -/
theorem bigO_succ {f η : ℕ → ℝ} (hη : RegularRate η) (h : f =O[atTop] η) :
    (fun n => f (n + 1)) =O[atTop] η :=
  (h.comp_tendsto (tendsto_add_atTop_nat 1)).trans (bigO_shift hη)

/-- Unshift: `f (n+1) = O(η_n)` implies `f n = O(η_n)`. -/
theorem bigO_of_succ {f η : ℕ → ℝ} (hη : RegularRate η) (h : (fun n => f (n + 1)) =O[atTop] η) :
    f =O[atTop] η := by
  obtain ⟨K, hK0, hK⟩ := bigO_bound hη.pos h
  refine bigO_of_bound (K := 2 * K) (fun n => (hη.pos n).le) (eventually_of_eventually_succ ?_)
  filter_upwards [hK, eventually_ge_atTop 1] with n hn hn1
  have := hη.le_two_mul hn1
  calc |f (n + 1)| ≤ K * η n := hn
    _ ≤ K * (2 * η (n + 1)) := mul_le_mul_of_nonneg_left this hK0
    _ = 2 * K * η (n + 1) := by ring

theorem abs_sqrt_sub_le {X c : ℝ} (hc : 0 < c) (hX : 0 ≤ X) : |Real.sqrt X - c| ≤ |X - c ^ 2| / c := by
  rw [le_div_iff₀ hc]
  have hs := Real.sq_sqrt hX
  have h0 := Real.sqrt_nonneg X
  have e : X - c ^ 2 = (Real.sqrt X - c) * (Real.sqrt X + c) := by linear_combination -hs
  rw [e, abs_mul, abs_of_pos (by linarith : 0 < Real.sqrt X + c)]
  exact mul_le_mul_of_nonneg_left (by linarith) (abs_nonneg _)

/-- **Christoffel shift with rate** (Paper 2 Theorem `thm:shift`, rate part; proof of §3 via Lemma
`lem:chain-rate`). For atoms `x_k ≥ 0`, a regular rate `η`, a scale `s_n > 0` with
`s_n / s_{n+1} − 1 = O(η_n)` (e.g. `s_n = (n+1)^p`), and `c > 0`: if `s_n a_n − 2c = O(η_n)` and
`s_n b_n − c = O(η_n)`, then the same holds for the Jacobi coefficients `ã_n, b̃_n` of `xσ`. -/
theorem christoffel_shift_rate {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) {c : ℝ} (hc : 0 < c)
    {s η : ℕ → ℝ} (hη : RegularRate η) (hs : ∀ n, 0 < s n)
    (hs1 : (fun n => s n / s (n + 1) - 1) =O[atTop] η)
    (hA : (fun n => s n * ja x w n - 2 * c) =O[atTop] η)
    (hB : (fun n => s n * Real.sqrt (jb2 x w n) - c) =O[atTop] η) :
    (fun n => s n * ja x (xw x w) n - 2 * c) =O[atTop] η ∧
      (fun n => s n * Real.sqrt (jb2 x (xw x w) n) - c) =O[atTop] η := by
  set U := fun n => s n * cg x w n with hUdef
  set V := fun n => s n * ch x w n with hVdef
  have hU : ∀ n, 0 < U n := fun n => mul_pos (hs n) (cg_pos h hx n)
  have hV : ∀ n, 0 < V (n + 1) := fun n => mul_pos (hs _) (ch_pos h hx n)
  set B := fun n => s n * Real.sqrt (jb2 x w n) with hBdef
  have hBt : Tendsto B atTop (𝓝 c) := tendsto_of_bigO hη.tendsto hB
  have hrt : Tendsto (fun n => s n / s (n + 1)) atTop (𝓝 1) := tendsto_of_bigO hη.tendsto hs1
  have hB1 : Tendsto (fun n => B (n + 1)) atTop (𝓝 c) := hBt.comp (tendsto_add_atTop_nat 1)
  -- hypotheses of the chain-rate lemma
  have hA' : (fun n => U n + V n - 2 * c) =O[atTop] η :=
    hA.congr_left fun n => by simp only [hUdef, hVdef, christoffel_ja_split h hx n]; ring
  have hQid : ∀ n, U n * V (n + 1) - c ^ 2 =
      (s n / s (n + 1) - 1) * (B (n + 1) * B (n + 1)) + (B (n + 1) - c) * (B (n + 1) + c) := by
    intro n
    have hb0 : 0 ≤ jb2 x w (n + 1) := (jb2_pos h _).le
    have hss : Real.sqrt (jb2 x w (n + 1)) * Real.sqrt (jb2 x w (n + 1)) = jb2 x w (n + 1) :=
      Real.mul_self_sqrt hb0
    simp only [hUdef, hVdef, hBdef]
    have e : s (n + 1) * Real.sqrt (jb2 x w (n + 1)) * (s (n + 1) * Real.sqrt (jb2 x w (n + 1))) =
        s (n + 1) * s (n + 1) * (cg x w n * ch x w (n + 1)) := by
      rw [← christoffel_jb2_split h hx]; linear_combination (s (n + 1) * s (n + 1)) * hss
    have e2 : (s n / s (n + 1) - 1) * (s (n + 1) * Real.sqrt (jb2 x w (n + 1)) *
        (s (n + 1) * Real.sqrt (jb2 x w (n + 1)))) + (s (n + 1) * Real.sqrt (jb2 x w (n + 1)) - c) *
        (s (n + 1) * Real.sqrt (jb2 x w (n + 1)) + c) =
        s n / s (n + 1) * (s (n + 1) * Real.sqrt (jb2 x w (n + 1)) *
        (s (n + 1) * Real.sqrt (jb2 x w (n + 1)))) - c ^ 2 := by ring
    rw [e2, e]
    field_simp [(hs (n + 1)).ne']
  have hQ' : (fun n => U n * V (n + 1) - c ^ 2) =O[atTop] η := by
    have t1 := bigO_mul_tendsto hs1 (hB1.mul hB1)
    have t2 := bigO_mul_tendsto (bigO_succ hη hB) (hB1.add_const c)
    exact (t1.add t2).congr_left fun n => (hQid n).symm
  obtain ⟨-, hinc⟩ := chain_rate_core hc hη hU hV hA' hQ'
  obtain ⟨hUt, hVt⟩ := chain_limit_core hc hU hV (tendsto_of_bigO hη.tendsto hA')
    (tendsto_of_bigO hη.tendsto hQ')
  constructor
  · -- s_n ã_n − 2c = (A_{n+1} − 2c) − (U_{n+1} − U_n) + (s_n/s_{n+1} − 1) V_{n+1}
    have t1 := bigO_succ hη hA'
    have t3 := bigO_mul_tendsto hs1 (hVt.comp (tendsto_add_atTop_nat 1))
    refine ((t1.sub hinc).add t3).congr_left fun n => ?_
    simp only [Function.comp, hUdef, hVdef, (christoffel_transfer h hx n).1]
    field_simp [(hs (n + 1)).ne']
    ring
  · -- s_{n+1} b̃_{n+1} = √(U_{n+1} V_{n+1}), and U_{n+1} V_{n+1} = (U_{n+1}/U_n) Q_n
    apply bigO_of_succ hη
    obtain ⟨Ki, hKi0, hKi⟩ := bigO_bound hη.pos hinc
    obtain ⟨KQ, hKQ0, hKQ⟩ := bigO_bound hη.pos hQ'
    have hQt : Tendsto (fun n => U n * V (n + 1)) atTop (𝓝 (c ^ 2)) := tendsto_of_bigO hη.tendsto hQ'
    have hQb : ∀ᶠ n in atTop, |U n * V (n + 1)| ≤ c ^ 2 + 1 := by
      have := hQt.abs.eventually (ge_mem_nhds (show |c ^ 2| < c ^ 2 + 1 by
        rw [abs_of_pos (by positivity)]; linarith))
      exact this
    have hUb : ∀ᶠ n in atTop, c / 2 ≤ U n := hUt.eventually (le_mem_nhds (by linarith))
    refine bigO_of_bound (K := (Ki * (2 / c) * (c ^ 2 + 1) + KQ) / c) (fun n => (hη.pos n).le) ?_
    filter_upwards [hKi, hKQ, hQb, hUb] with n hi hq hqb hub
    have hUn := hU n
    have hX : 0 ≤ U (n + 1) * V (n + 1) := (mul_pos (hU _) (hV n)).le
    have e1 : s (n + 1) * Real.sqrt (jb2 x (xw x w) (n + 1)) = Real.sqrt (U (n + 1) * V (n + 1)) := by
      simp only [hUdef, hVdef, (christoffel_transfer h hx n).2]
      exact sqrt_scale (hs _)
    rw [e1]
    refine (abs_sqrt_sub_le hc hX).trans ?_
    rw [div_le_iff₀ hc]
    have e2 : U (n + 1) * V (n + 1) - c ^ 2 =
        (U (n + 1) - U n) / U n * (U n * V (n + 1)) + (U n * V (n + 1) - c ^ 2) := by
      field_simp; ring
    rw [e2]
    have hη0 := (hη.pos n).le
    have h1 : |(U (n + 1) - U n) / U n| ≤ Ki * (2 / c) * η n := by
      rw [abs_div, abs_of_pos hUn, div_le_iff₀ hUn]
      have : Ki * η n ≤ Ki * (2 / c) * η n * U n := by
        have e : Ki * (2 / c) * η n * U n = Ki * η n * (2 * U n / c) := by ring
        rw [e]
        have : 1 ≤ 2 * U n / c := by rw [le_div_iff₀ hc]; linarith
        have := mul_nonneg hKi0 hη0
        nlinarith
      linarith
    calc |(U (n + 1) - U n) / U n * (U n * V (n + 1)) + (U n * V (n + 1) - c ^ 2)|
        ≤ |(U (n + 1) - U n) / U n| * |U n * V (n + 1)| + |U n * V (n + 1) - c ^ 2| := by
          rw [← abs_mul]; exact abs_add_le _ _
      _ ≤ Ki * (2 / c) * η n * (c ^ 2 + 1) + KQ * η n := by
          gcongr
      _ = (Ki * (2 / c) * (c ^ 2 + 1) + KQ) / c * η n * c := by field_simp

/-- `(1 + t_n)^p − 1 = O(t_n)` for `t_n → 0`. -/
theorem one_add_rpow_sub_one_bigO (p : ℝ) {t : ℕ → ℝ} (ht : Tendsto t atTop (𝓝 0)) :
    (fun n => (1 + t n) ^ p - 1) =O[atTop] t := by
  have hd := ((hasDerivAt_id (0 : ℝ)).const_add 1).rpow_const (p := p) (Or.inl (by norm_num))
  exact (hd.isBigO_sub.comp_tendsto ht).congr (fun n => by simp) (fun n => by simp)

theorem inv_nat_bigO {η : ℕ → ℝ} (hη : RegularRate η) : (fun n : ℕ => 1 / (n : ℝ)) =O[atTop] η := by
  refine bigO_of_bound (K := 1 / η 1) (fun n => (hη.pos n).le) ?_
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have := hη.ge_inv hn
  rw [abs_of_pos (by positivity), one_div_mul_eq_div, div_le_div_iff₀ hn' (hη.pos 1)]
  linarith

theorem inv_succ_bigO {η : ℕ → ℝ} (hη : RegularRate η) : (fun n : ℕ => 1 / ((n : ℝ) + 1)) =O[atTop] η := by
  have := bigO_succ hη (inv_nat_bigO hη)
  simpa using this

/-- At a regular rate, scaling by `n^p` or `(n+1)^p` gives the same `O(η)` law. -/
theorem bigO_rpow_succ_iff {η : ℕ → ℝ} (hη : RegularRate η) (p L : ℝ) (f : ℕ → ℝ) :
    (fun n : ℕ => (n : ℝ) ^ p * f n - L) =O[atTop] η ↔
      (fun n : ℕ => ((n : ℝ) + 1) ^ p * f n - L) =O[atTop] η := by
  have hρ : (fun n : ℕ => (1 + 1 / (n : ℝ)) ^ p - 1) =O[atTop] η :=
    (one_add_rpow_sub_one_bigO p tendsto_one_div_atTop_nhds_zero_nat).trans (inv_nat_bigO hη)
  have hσt : Tendsto (fun n : ℕ => -(1 / ((n : ℝ) + 1))) atTop (𝓝 0) := by
    simpa using (tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ)).neg
  have hσ : (fun n : ℕ => (1 + -(1 / ((n : ℝ) + 1))) ^ p - 1) =O[atTop] η :=
    (one_add_rpow_sub_one_bigO p hσt).trans (inv_succ_bigO hη).neg_left
  constructor
  · intro hf
    have hρt := tendsto_of_bigO hη.tendsto hρ
    refine ((bigO_mul_tendsto hf hρt).add (hρ.const_mul_left L)).congr' ?_ EventuallyEq.rfl
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    have e : ((n : ℝ) + 1) ^ p = (n : ℝ) ^ p * (1 + 1 / (n : ℝ)) ^ p := by
      rw [← Real.mul_rpow hn'.le (by positivity)]; congr 1; field_simp
    rw [e]; ring
  · intro hf
    have hσl := tendsto_of_bigO hη.tendsto hσ
    refine ((bigO_mul_tendsto hf hσl).add (hσ.const_mul_left L)).congr_left fun n => ?_
    have e : (n : ℝ) ^ p = ((n : ℝ) + 1) ^ p * (1 + -(1 / ((n : ℝ) + 1))) ^ p := by
      rw [← Real.mul_rpow (by positivity) (by rw [← sub_eq_add_neg, sub_nonneg, div_le_one (by positivity)]; linarith)]
      congr 1; field_simp; ring
    rw [e]; ring

/-- **Christoffel shift with rate at scale `n^p`** (Paper 2 Theorem `thm:shift`, exactly as stated there): for
atoms `x_k ≥ 0`, a regular rate `η` and `c > 0`, `n^p a_n − 2c = O(η_n)` and `n^p b_n − c = O(η_n)` imply the
same for `xσ`. -/
theorem christoffel_shift_rate_pow {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) {c p : ℝ} (hc : 0 < c)
    {η : ℕ → ℝ} (hη : RegularRate η)
    (hA : (fun n : ℕ => (n : ℝ) ^ p * ja x w n - 2 * c) =O[atTop] η)
    (hB : (fun n : ℕ => (n : ℝ) ^ p * Real.sqrt (jb2 x w n) - c) =O[atTop] η) :
    (fun n : ℕ => (n : ℝ) ^ p * ja x (xw x w) n - 2 * c) =O[atTop] η ∧
      (fun n : ℕ => (n : ℝ) ^ p * Real.sqrt (jb2 x (xw x w) n) - c) =O[atTop] η := by
  rw [bigO_rpow_succ_iff hη] at hA hB ⊢
  rw [bigO_rpow_succ_iff hη]
  have hσt : Tendsto (fun n : ℕ => -(1 / ((n : ℝ) + 1))) atTop (𝓝 0) := by
    simpa using (tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ)).neg
  have hσ : (fun n : ℕ => (1 + -(1 / ((n : ℝ) + 1))) ^ p - 1) =O[atTop] η :=
    (one_add_rpow_sub_one_bigO p hσt).trans (inv_succ_bigO hη).neg_left
  refine christoffel_shift_rate h hx hc hη (s := fun n : ℕ => ((n : ℝ) + 1) ^ p)
    (fun n => Real.rpow_pos_of_pos (by positivity) p) ?_ hA hB
  refine (bigO_succ hη hσ).congr_left fun n => ?_
  rw [← Real.div_rpow (by positivity) (by positivity)]
  congr 2
  push_cast
  field_simp
  ring

end JacobiAsym
