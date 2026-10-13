import JacobiAsym.UpperChain
import JacobiAsym.Penalty

open Finset

namespace JacobiAsym

theorem log_factorial_ge (N : ℕ) : (N : ℝ) * Real.log N - N ≤ Real.log (N.factorial) := by
  rcases Nat.eq_zero_or_pos N with rfl | hN
  · simp
  have h := Real.pow_div_factorial_le_exp (N : ℝ) (Nat.cast_nonneg N) N
  have hF : (0 : ℝ) < N.factorial := by exact_mod_cast Nat.factorial_pos N
  have hNr : (0 : ℝ) < N := by exact_mod_cast hN
  have hpos : 0 < (N : ℝ) ^ N / N.factorial := by positivity
  have := Real.log_le_log hpos h
  rw [Real.log_exp, Real.log_div (by positivity) hF.ne', Real.log_pow] at this
  linarith

/-- The exact exponent identity of item 11 Lemma H7 step 5 (`log 0 = 0` makes `m = n` work too). -/
theorem exponent_identity {p κ M n m : ℝ} (hn : 0 < n) (_hm0 : 0 ≤ m) (hmn : m ≤ n) (_hM : 0 < M) :
    -2 * p * m * ((n - m) * Real.log (n - m)) + 2 * p * m * (n - m) - p * (n - m) ^ 2 * Real.log (n - m)
      + κ * (n - m) ^ 2 - p * m ^ 2 * (Real.log M + Real.log n)
    = -p * n ^ 2 * Real.log n + κ * n ^ 2 + n ^ 2 * (-p * (1 - (m / n) ^ 2) * Real.log (1 - m / n)
      + 2 * p * (m / n) * (1 - m / n) - κ * (m / n) * (2 - m / n) - p * (m / n) ^ 2 * Real.log M) := by
  rcases eq_or_lt_of_le hmn with rfl | hlt
  · simp only [sub_self, Real.log_zero, div_self hn.ne']
    ring
  have h1 : (0 : ℝ) < 1 - m / n := by rw [sub_pos, div_lt_one hn]; exact hlt
  have hlog : Real.log (n - m) = Real.log n + Real.log (1 - m / n) := by
    rw [← Real.log_mul hn.ne' h1.ne']
    congr 1; field_simp
  rw [hlog]
  field_simp
  ring

/-- Uniform bound on the m-th term: for `n ≥ 1`, `m ≤ n`, `M ≥ 2`, any `C` from `uniform_upper` at level `η`:
`log upperTerm ≤ -p n² log n + κ n² + (A²/(4p log M) + η) n² + C + n (|log (c2 U(Mn))| + |log W| + p log (Mn))`,
`A = 4p + 2|κ|`. -/
theorem log_upperTerm_le {p κ s0 c2 W η C : ℝ} {U : ℝ → ℝ} (hp : 0 < p) (hη : 0 < η)
    (hHup : TheoremHPure p κ s0)
    (hC : ∀ N : ℕ, Real.log (heineD (powSeq p) (powSeq s0) N) ≤
      -p * (N : ℝ) ^ 2 * Real.log N + κ * (N : ℝ) ^ 2 + η * (N : ℝ) ^ 2 + C)
    (hc2U : ∀ t, 0 < c2 * U t) (hW : 0 < W) {M n m : ℕ} (hM : 2 ≤ M) (hn : 1 ≤ n) (hmn : m ≤ n) :
    Real.log (upperTerm p s0 c2 W U (M * n) n m) ≤
      -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2
        + ((4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) + η) * (n : ℝ) ^ 2 + C
        + n * (|Real.log (c2 * U (M * n))| + |Real.log W| + p * Real.log (M * n)) := by
  have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hnpos : (0 : ℝ) < n := by linarith
  have hmr : (m : ℝ) ≤ n := by exact_mod_cast hmn
  have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
  have hMr : (2 : ℝ) ≤ M := by exact_mod_cast hM
  have hMpos : (0 : ℝ) < M := by linarith
  have hNr : ((n - m : ℕ) : ℝ) = (n : ℝ) - m := Nat.cast_sub hmn
  have hMn : ((M * n : ℕ) : ℝ) = (M : ℝ) * n := by push_cast; ring
  have hMn1 : (1 : ℝ) ≤ (M : ℝ) * n := by nlinarith
  have hlogMn : Real.log ((M : ℝ) * n) = Real.log M + Real.log n := Real.log_mul hMpos.ne' hnpos.ne'
  have hlogMn0 : 0 ≤ Real.log ((M : ℝ) * n) := Real.log_nonneg hMn1
  have hmm : (((m * (m - 1) : ℕ)) : ℝ) = (m : ℝ) ^ 2 - m := by
    rcases m with _ | m
    · simp
    · push_cast [Nat.succ_sub_one]; ring
  -- positivity
  have hanti : StrictAnti (powSeq p) := by
    intro a b hab
    exact Real.rpow_lt_rpow_of_neg (by positivity) (by exact_mod_cast Nat.add_lt_add_right hab 1) (by linarith)
  have hD : 0 < heineD (powSeq p) (powSeq s0) (n - m) :=
    heineD_pos hanti (fun i => Real.rpow_pos_of_pos (by positivity) _) (hHup.bdd _)
  have hF : (0 : ℝ) < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
  have hX : (0 : ℝ) < ((M * n : ℕ) : ℝ) ^ (-p) := Real.rpow_pos_of_pos (by rw [hMn]; linarith) _
  have hcU := hc2U ((M * n : ℕ) : ℝ)
  have hDb := hC (n - m)
  rw [hNr] at hDb
  -- expand the logarithm
  set F := ((n - m).factorial : ℝ)
  set cU := c2 * U ((M * n : ℕ) : ℝ)
  set D := heineD (powSeq p) (powSeq s0) (n - m)
  set X := ((M * n : ℕ) : ℝ) ^ (-p)
  have hlog : Real.log (upperTerm p s0 c2 W U (M * n) n m) =
      -(2 * p * m) * Real.log F + ((n - m : ℕ) : ℝ) * Real.log cU + Real.log D + m * Real.log W
        + (((m * (m - 1) : ℕ)) : ℝ) * Real.log X := by
    unfold upperTerm
    have h1 : F ^ (-(2 * p * m)) ≠ 0 := (Real.rpow_pos_of_pos hF _).ne'
    have h2 : cU ^ (n - m) ≠ 0 := (pow_pos hcU _).ne'
    have h3 : W ^ m ≠ 0 := (pow_pos hW _).ne'
    have h4 : X ^ (m * (m - 1)) ≠ 0 := (pow_pos hX _).ne'
    rw [Real.log_mul (by positivity) h4, Real.log_mul (by positivity) h3, Real.log_mul (by positivity) hD.ne',
      Real.log_mul h1 h2, Real.log_rpow hF, Real.log_pow, Real.log_pow, Real.log_pow]
  have hlogX : Real.log X = -p * Real.log ((M : ℝ) * n) := by
    simp only [X]; rw [Real.log_rpow (by rw [hMn]; linarith), hMn]
  -- termwise bounds
  have hfact : -(2 * p * m) * Real.log F ≤ -(2 * p * m) * (((n : ℝ) - m) * Real.log ((n : ℝ) - m) - ((n : ℝ) - m)) := by
    have := log_factorial_ge (n - m)
    rw [hNr] at this
    exact mul_le_mul_of_nonpos_left this (by nlinarith)
  have hcUb : ((n - m : ℕ) : ℝ) * Real.log cU ≤ n * |Real.log cU| := by
    rw [hNr]
    calc ((n : ℝ) - m) * Real.log cU ≤ ((n : ℝ) - m) * |Real.log cU| :=
          mul_le_mul_of_nonneg_left (le_abs_self _) (by linarith)
      _ ≤ n * |Real.log cU| := mul_le_mul_of_nonneg_right (by linarith) (abs_nonneg _)
  have hWb : (m : ℝ) * Real.log W ≤ n * |Real.log W| :=
    (mul_le_mul_of_nonneg_left (le_abs_self _) hm0).trans (mul_le_mul_of_nonneg_right hmr (abs_nonneg _))
  have hXb : (((m * (m - 1) : ℕ)) : ℝ) * Real.log X ≤
      -p * (m : ℝ) ^ 2 * (Real.log M + Real.log n) + n * (p * Real.log ((M : ℝ) * n)) := by
    rw [hmm, hlogX, ← hlogMn]
    have : (m : ℝ) * (p * Real.log ((M : ℝ) * n)) ≤ n * (p * Real.log ((M : ℝ) * n)) :=
      mul_le_mul_of_nonneg_right hmr (mul_nonneg hp.le hlogMn0)
    nlinarith
  have hη2 : η * ((n : ℝ) - m) ^ 2 ≤ η * (n : ℝ) ^ 2 := by
    apply mul_le_mul_of_nonneg_left _ hη.le; nlinarith
  -- identity and penalty
  have hid := exponent_identity (p := p) (κ := κ) (M := M) hnpos hm0 hmr hMpos
  have hphi := phi_bound (κ := κ) (M := M) (t := m / n) hp (by linarith) (div_nonneg hm0 hnpos.le)
    ((div_le_one hnpos).2 hmr)
  have hphin := mul_le_mul_of_nonneg_left hphi (sq_nonneg (n : ℝ))
  rw [hlog]
  have hcU_eq : cU = c2 * U ((M : ℝ) * n) := by simp only [cU, hMn]
  have hcUb' : ((n - m : ℕ) : ℝ) * Real.log cU ≤ n * |Real.log (c2 * U ((M : ℝ) * n))| := by
    rw [← hcU_eq]; exact hcUb
  set φ := -p * (1 - ((m : ℝ) / n) ^ 2) * Real.log (1 - (m : ℝ) / n) + 2 * p * ((m : ℝ) / n) * (1 - (m : ℝ) / n)
    - κ * ((m : ℝ) / n) * (2 - (m : ℝ) / n) - p * ((m : ℝ) / n) ^ 2 * Real.log M with hφ
  set A2 := (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M)
  calc -(2 * p * m) * Real.log F + ((n - m : ℕ) : ℝ) * Real.log cU + Real.log D + m * Real.log W
        + (((m * (m - 1) : ℕ)) : ℝ) * Real.log X
      ≤ -(2 * p * m) * (((n : ℝ) - m) * Real.log ((n : ℝ) - m) - ((n : ℝ) - m))
        + n * |Real.log (c2 * U ((M : ℝ) * n))|
        + (-p * ((n : ℝ) - m) ^ 2 * Real.log ((n : ℝ) - m) + κ * ((n : ℝ) - m) ^ 2 + η * ((n : ℝ) - m) ^ 2 + C)
        + n * |Real.log W|
        + (-p * (m : ℝ) ^ 2 * (Real.log M + Real.log n) + n * (p * Real.log ((M : ℝ) * n))) := by
        linarith [hfact, hcUb', hWb, hXb, hDb]
    _ = -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2 + (n : ℝ) ^ 2 * φ + η * ((n : ℝ) - m) ^ 2 + C
        + n * (|Real.log (c2 * U ((M : ℝ) * n))| + |Real.log W| + p * Real.log ((M : ℝ) * n)) := by
        linear_combination hid
    _ ≤ _ := by linear_combination hphin + hη2

end JacobiAsym
