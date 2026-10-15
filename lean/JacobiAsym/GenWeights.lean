import JacobiAsym.HallUpper
import JacobiAsym.HallLower

/-! # Plan 61, stage G1: the pure-power bounds for general weights (Paper 1 Theorems 4.3 and 5.2 as stated)

* `hall_upper_w` (Theorem 4.3): atoms `(k+1)^{-p}`, any positive summable weights `w` (the proof of `hall_upper` re-run
  with `W = Σ' w` in place of `Σ' (k+1)^{-s}`; only `w ≥ 0`, `Σ w < ∞` and `w > 0` (for positivity of the head sums) are
  used).
* `hall_lower_w` (Theorem 5.2): weights `w ≥ c₁ (k+1)^{-s}` with **any real `s`**, transferred from `hall_lower` by
  monotonicity in the weights (`(k+1)^{-s'} ≤ (k+1)^{-s}` for `s' = max s 2`).
* `pure_law_w`: `log D_n = -p n² log n + κ_p n² + o(n²)` for these weights. -/

open Real Set MeasureTheory Filter Topology

namespace JacobiAsym

/-- The `m`-th term: `(N!)^{−2pm} heineK(Mn, N) W^m ((Mn)^{−p})^{m(m−1)}`, `N = n − m`. -/
noncomputable def hTermW (p : ℝ) (w : ℕ → ℝ) (M n m : ℕ) : ℝ :=
  ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * heineK (powSeq p) w (M * n) (n - m) *
    (∑' k, w k) ^ m * (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1))

/-- Head/tail split for the pure powers, general weights (item 11 H7 / Paper 1 Theorem 4.3). -/
theorem heineK_le_hTermW {p : ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hw : ∀ k, 0 ≤ w k) (hws : Summable w) {M n : ℕ} (hMn : 1 ≤ M * n) (K : ℕ) :
    heineK (powSeq p) w K n ≤ ∑ m ∈ Finset.range (n + 1), hTermW p w M n m := by
  have hMnr : (0 : ℝ) < ((M * n : ℕ) : ℝ) := by exact_mod_cast hMn
  have h0 := heineK_mono_K hw (le_max_left K (M * n)) n (x := powSeq p)
  have h2 := heineK_tail_split (y := powSeq p) (w := w) hw (le_max_right K (M * n)) (n := n)
    (X := ((M * n : ℕ) : ℝ) ^ (-p)) (powSeq_pos p)
    (fun b hb => rpow_le_rpow_of_nonpos hMnr (by
      have : ((M * n : ℕ) : ℝ) ≤ b := by exact_mod_cast hb
      linarith) (by linarith))
    (fun a b ha hb => ((powSeq_strictAnti hp).antitone (by omega)))
  refine h0.trans (h2.trans (Finset.sum_le_sum fun m _ => ?_))
  have hX : 0 ≤ (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) := pow_nonneg (rpow_pos_of_pos hMnr _).le _
  have hF : 0 < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
  have hhead : ∑ SH ∈ (Finset.range (M * n)).powersetCard (n - m),
        heineTerm (powSeq p) w SH * ∏ a ∈ SH, powSeq p a ^ (2 * m) ≤
      ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * heineK (powSeq p) w (M * n) (n - m) := by
    rw [heineK, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro SH hSH
    have hcard := (Finset.mem_powersetCard.1 hSH).2
    have hP : ∏ a ∈ SH, powSeq p a ^ (2 * m) ≤ ((n - m).factorial : ℝ) ^ (-(2 * p * m)) := by
      have e : ∏ a ∈ SH, powSeq p a ^ (2 * m) = (∏ a ∈ SH, ((a : ℝ) + 1)) ^ (-(2 * p * m)) := by
        rw [← Real.finsetProd_rpow _ _ (fun a _ => by positivity)]
        apply Finset.prod_congr rfl; intro a _
        rw [powSeq, ← Real.rpow_natCast, ← Real.rpow_mul (by positivity)]
        congr 1; push_cast; ring
      rw [e]
      have hf := factorial_le_prod_succ SH
      rw [hcard] at hf
      exact Real.rpow_le_rpow_of_nonpos hF hf (by have : (0 : ℝ) ≤ m := Nat.cast_nonneg m; nlinarith)
    rw [mul_comm (((n - m).factorial : ℝ) ^ (-(2 * p * m)))]
    exact mul_le_mul_of_nonneg_left hP (heineTerm_nonneg hw SH)
  have htail : (∑ b ∈ Finset.Ico (M * n) (max K (M * n)), w b) ^ m ≤ (∑' k, w k) ^ m :=
    pow_le_pow_left₀ (Finset.sum_nonneg fun b _ => hw b)
      (Summable.sum_le_tsum _ (fun b _ => hw b) hws) m
  have hh0 : 0 ≤ ∑ SH ∈ (Finset.range (M * n)).powersetCard (n - m),
      heineTerm (powSeq p) w SH * ∏ a ∈ SH, powSeq p a ^ (2 * m) :=
    Finset.sum_nonneg fun SH _ => mul_nonneg (heineTerm_nonneg hw SH)
      (Finset.prod_nonneg fun a _ => pow_nonneg (powSeq_pos p a).le _)
  unfold hTermW
  calc _ ≤ (((n - m).factorial : ℝ) ^ (-(2 * p * m)) * heineK (powSeq p) w (M * n) (n - m)) *
        (∑' k, w k) ^ m * (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) := by
        apply mul_le_mul_of_nonneg_right _ hX
        exact mul_le_mul hhead htail (pow_nonneg (Finset.sum_nonneg fun b _ => hw b) _) (hh0.trans hhead)
    _ = _ := by ring

/-- The head bound in the form needed by `log_term_le`. -/
theorem head_log_bound_w {p : ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hwp : ∀ k, 0 < w k) (hws : Summable w) {M n m : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (hmn : m ≤ n) :
    0 < heineK (powSeq p) w (M * n) (n - m) ∧
    Real.log (heineK (powSeq p) w (M * n) (n - m)) ≤
      -p * ((n : ℝ) - m) ^ 2 * Real.log ((n : ℝ) - m) + hallKappa p * ((n : ℝ) - m) ^ 2 +
        n * (|Real.log (∑' k, w k)| + p * Real.log n + eDisc p n M) := by
  have hw : ∀ i, 0 ≤ w i := fun i => (hwp i).le
  have hWpos : 0 < ∑' k, w k := hws.tsum_pos hw 0 (hwp 0)
  have hNle : n - m ≤ M * n := (Nat.sub_le n m).trans (Nat.le_mul_of_pos_left n (by omega))
  have hpos := heineK_pos (powSeq_strictAnti hp) hwp hNle
  refine ⟨hpos, ?_⟩
  have hNr : ((n - m : ℕ) : ℝ) = (n : ℝ) - m := Nat.cast_sub hmn
  have hE := eDisc_nonneg hp hn hM
  have hlogn := Real.log_natCast_nonneg n
  have hR0 : 0 ≤ (n : ℝ) * (|Real.log (∑' k, w k)| + p * Real.log n + eDisc p n M) := by positivity
  rcases Nat.eq_zero_or_pos (n - m) with h0 | hN
  · rw [h0, heineK_zero_card, Real.log_one]
    have : (n : ℝ) - m = 0 := by rw [← hNr, h0]; simp
    rw [this]; simp; linarith
  · have hb := head_heineK_bound hp hw hn hM hN (W := ∑' k, w k)
      (Summable.sum_le_tsum _ (fun b _ => hw b) hws)
    have hl := Real.log_le_log hpos hb
    rw [Real.log_mul (pow_pos hWpos _).ne' (Real.exp_pos _).ne', Real.log_pow, Real.log_exp, hNr] at hl
    have hmr : (m : ℝ) ≤ n := by exact_mod_cast hmn
    have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
    have h1 : ((n : ℝ) - m) * Real.log (∑' k, w k) ≤ n * |Real.log (∑' k, w k)| :=
      (mul_le_mul_of_nonneg_left (le_abs_self _) (by linarith)).trans
        (mul_le_mul_of_nonneg_right (by linarith) (abs_nonneg _))
    have h2 : p * ((n : ℝ) - m) * Real.log n ≤ n * (p * Real.log n) := by
      have : p * ((n : ℝ) - m) * Real.log n = ((n : ℝ) - m) * (p * Real.log n) := by ring
      rw [this]; exact mul_le_mul_of_nonneg_right (by linarith) (by positivity)
    have h3 : ((n : ℝ) - m) * eDisc p n M ≤ n * eDisc p n M := by nlinarith
    linarith

/-- **Theorem A-U** (Paper 1 Theorem 4.3 for `w_k = k^{-s}`): for every `η > 0`, eventually
`hnorm ≤ η`, i.e. `limsup (log D_n + p n² log n)/n² ≤ κ_p`. -/
theorem hall_upper_w {p : ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hwp : ∀ k, 0 < w k) (hws : Summable w) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop, hnorm p (hallKappa p) (heineD (powSeq p) w) (fun _ => 0) n ≤ η := by
  set κ := hallKappa p
  set A := 4 * p + 2 * |κ|
  have hA : 0 < A := by have := abs_nonneg κ; simp only [A]; linarith
  set X := A ^ 2 / (2 * p * η)
  set M : ℕ := ⌈Real.exp X⌉₊ + 2
  have hM2 : 2 ≤ M := by omega
  have hMgt : Real.exp X < M := by
    have := Nat.le_ceil (Real.exp X)
    have : ((⌈Real.exp X⌉₊ + 2 : ℕ) : ℝ) = (⌈Real.exp X⌉₊ : ℝ) + 2 := by push_cast; ring
    simp only [M]; rw [this]; linarith
  have hlogM : X < Real.log M := by
    rw [← Real.exp_lt_exp, Real.exp_log (by have := Real.exp_pos X; linarith)]; exact hMgt
  have hXpos : 0 < X := by positivity
  have hpen : A ^ 2 / (4 * p * Real.log M) < η / 2 := by
    have hlp : 0 < Real.log M := hXpos.trans hlogM
    rw [div_lt_iff₀ (by positivity)]
    have h1 : A ^ 2 = X * (2 * p * η) := by simp only [X]; field_simp
    rw [h1]
    nlinarith [mul_lt_mul_of_pos_right hlogM (by positivity : (0:ℝ) < 2 * p * η)]
  set W := ∑' k, w k
  set K1 := 3 * |Real.log (p * (M : ℝ) ^ (-p - 1))| + 11 + (2 + 4 * p) * |Real.log M|
  set K2 := 5 + 4 * p
  -- the error term
  set err : ℕ → ℝ := fun n => n * (|Real.log W| + p * Real.log n + (K1 + K2 * Real.log n)) +
    n * (|Real.log W| + p * (Real.log M + Real.log n)) + Real.log ((n : ℝ) + 1)
  have herr : Tendsto (fun n : ℕ => err n / (n : ℝ) ^ 2) atTop (𝓝 0) := by
    have h1 := tendsto_const_div_atTop_nhds_zero_nat (2 * |Real.log W| + K1 + p * Real.log M)
    have h2 := tendsto_log_div_nat.const_mul (2 * p + K2)
    have h3 := tendsto_log_succ_div_sq
    have := (h1.add h2).add h3
    simp only [mul_zero, add_zero] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    simp only [err]; field_simp; ring
  filter_upwards [herr.eventually (gt_mem_nhds (half_pos hη)), eventually_ge_atTop 1] with n hen hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hMn : 1 ≤ M * n := Nat.one_le_iff_ne_zero.2 (by positivity)
  have hbdd := heineK_bdd_of_summable (x := powSeq p) (w := w) (X := 1)
    (fun k => (hwp k).le) hws
    (fun k => by
      rw [abs_of_pos (powSeq_pos p k)]
      exact rpow_le_one_of_one_le_of_nonpos (by have := Nat.cast_nonneg (α := ℝ) k; linarith) (by linarith))
  have hDpos := heineD_pos (powSeq_strictAnti hp) hwp (hbdd n)
  have hDle := heineD_le (fun K => heineK_le_hTermW hp (fun k => (hwp k).le) hws hMn K (n := n))
  set Q := -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2 + A ^ 2 / (4 * p * Real.log M) * (n : ℝ) ^ 2 +
    n * (|Real.log W| + p * Real.log n + eDisc p n M) + n * (|Real.log W| + p * Real.log ((M : ℝ) * n))
  have hW : 0 < W := hws.tsum_pos (fun k => (hwp k).le) 0 (hwp 0)
  have hT : ∀ m ∈ Finset.range (n + 1), 0 < hTermW p w M n m ∧ Real.log (hTermW p w M n m) ≤ Q := by
    intro m hm
    have hmn : m ≤ n := Nat.lt_succ_iff.1 (Finset.mem_range.1 hm)
    obtain ⟨hDp, hDb⟩ := head_log_bound_w hp hwp hws hn (by omega : 1 ≤ M) hmn (M := M)
    constructor
    · unfold hTermW
      have hF : (0 : ℝ) < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
      have hX : (0 : ℝ) < ((M * n : ℕ) : ℝ) ^ (-p) := rpow_pos_of_pos (by exact_mod_cast hMn) _
      have := rpow_pos_of_pos hF (-(2 * p * m))
      positivity
    · exact log_term_le hp hW hDp hM2 hn hmn hDb
  have hsum := log_sum_le_of_log_le (fun m hm => (hT m hm).1) (fun m hm => (hT m hm).2)
  have hlogD : Real.log (heineD (powSeq p) w n) ≤ Real.log ((n : ℝ) + 1) + Q :=
    (Real.log_le_log hDpos hDle).trans hsum
  have hED := eDisc_le hp hn (by omega : 1 ≤ M) (n := n) (M := M)
  have hlogMn : Real.log ((M : ℝ) * n) = Real.log M + Real.log n :=
    Real.log_mul (by have : (2 : ℝ) ≤ M := by exact_mod_cast hM2
                     linarith) hn'.ne'
  have hQ : Q ≤ -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2 + A ^ 2 / (4 * p * Real.log M) * (n : ℝ) ^ 2 +
      (err n - Real.log ((n : ℝ) + 1)) := by
    simp only [Q, err]; rw [hlogMn]
    have := mul_le_mul_of_nonneg_left hED hn'.le
    nlinarith
  rw [div_lt_iff₀ (by positivity)] at hen
  unfold hnorm
  rw [div_le_iff₀ (by positivity)]
  have hpen' := mul_le_mul_of_nonneg_right hpen.le (sq_nonneg (n : ℝ))
  nlinarith

/-! ### Theorem 5.2 for general weights `w ≥ c₁ (k+1)^{-s}`, any real `s` -/

theorem powSeq_anti_exp {s s' : ℝ} (hss : s ≤ s') (k : ℕ) : powSeq s' k ≤ powSeq s k :=
  Real.rpow_le_rpow_of_exponent_le (by have := Nat.cast_nonneg (α := ℝ) k; linarith) (by linarith)

theorem powSeq_abs_le_one {p : ℝ} (hp : 0 < p) (k : ℕ) : |powSeq p k| ≤ 1 := by
  rw [abs_of_pos (powSeq_pos p k)]
  exact rpow_le_one_of_one_le_of_nonpos (by have := Nat.cast_nonneg (α := ℝ) k; linarith) (by linarith)

/-- Weight comparison at the level of `heineD`: if `c₁ v ≤ w` (`v ≥ 0` summable, `w` summable) then
`c₁ⁿ heineD x v n ≤ heineD x w n` (Paper 1 Lemma 2.2(i), (iii)). -/
theorem heineD_weight_ge {x v w : ℕ → ℝ} {X c1 : ℝ} (hc1 : 0 < c1) (hv : ∀ k, 0 ≤ v k) (hw : ∀ k, 0 ≤ w k)
    (hws : Summable w) (hx : ∀ k, |x k| ≤ X) (hvw : ∀ k, c1 * v k ≤ w k) (n : ℕ) :
    c1 ^ n * heineD x v n ≤ heineD x w n := by
  have hbw := heineK_bdd_of_summable hw hws hx
  have hcn : 0 < c1 ^ n := pow_pos hc1 n
  rw [← le_div_iff₀' hcn]
  apply heineD_le
  intro K
  rw [le_div_iff₀' hcn, ← heineK_smul_w]
  exact (heineK_mono_w (fun k => mul_nonneg hc1.le (hv k)) hvw K n).trans (heineK_le_heineD (hbw n) K)

/-- **Theorem 5.2 (lower bound) for general weights** (Paper 1 Theorem 5.2 as stated): atoms `(k+1)^{-p}`, weights
`w ≥ 0`, `Σ w < ∞`, `w_k ≥ c₁ (k+1)^{-s}` with `c₁ > 0` and **any real `s`**. -/
theorem hall_lower_w {p s c1 : ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hc1 : 0 < c1) (hw0 : ∀ k, 0 ≤ w k) (hws : Summable w)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop, -η ≤ hnorm p (hallKappa p) (heineD (powSeq p) w) (fun _ => 0) n := by
  set s' := max s 2
  have hs' : 1 < s' := lt_of_lt_of_le one_lt_two (le_max_right _ _)
  have hge := heineD_weight_ge hc1 (fun k => (powSeq_pos s' k).le) hw0 hws (powSeq_abs_le_one hp)
    (fun k => (mul_le_mul_of_nonneg_left (powSeq_anti_exp (le_max_left s 2) k) hc1.le).trans (hwlo k))
  have hbdd := heineK_bdd_of_summable (fun k => (powSeq_pos s' k).le) (powSeq_summable hs')
    (powSeq_abs_le_one hp)
  have hlc : Tendsto (fun n : ℕ => Real.log c1 / n) atTop (𝓝 0) := tendsto_const_div_atTop_nhds_zero_nat _
  filter_upwards [hall_lower hp hs' (half_pos hη), hlc.eventually (Metric.ball_mem_nhds 0 (half_pos hη)),
    eventually_ge_atTop 1] with n h1 h2 hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hD' := heineD_pos (powSeq_strictAnti hp) (powSeq_pos s') (hbdd n)
  have hcn : 0 < c1 ^ n := pow_pos hc1 n
  have hlog : (n : ℝ) * Real.log c1 + Real.log (heineD (powSeq p) (powSeq s') n) ≤
      Real.log (heineD (powSeq p) w n) := by
    have := Real.log_le_log (mul_pos hcn hD') (hge n)
    rwa [Real.log_mul hcn.ne' hD'.ne', Real.log_pow] at this
  rw [Real.dist_eq, sub_zero, abs_lt, lt_div_iff₀ hn', div_lt_iff₀ hn'] at h2
  unfold hnorm at h1 ⊢
  rw [le_div_iff₀ (by positivity)] at h1 ⊢
  nlinarith

/-- **Pure powers, general weights** (Paper 1 Theorems 4.3 + 5.2 + 1.3(iii)): atoms `(k+1)^{-p}`, weights `w ≥ 0`,
`Σ w < ∞`, `w_k ≥ c₁ (k+1)^{-s}` (`c₁ > 0`, any real `s`): `log D_n = -p n² log n + κ_p n² + o(n²)`. -/
theorem pure_law_w {p s c1 : ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hc1 : 0 < c1) (hw0 : ∀ k, 0 ≤ w k) (hws : Summable w)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) :
    Tendsto (hnorm p (hallKappa p) (heineD (powSeq p) w) (fun _ => 0)) atTop (𝓝 0) := by
  have hwp : ∀ k, 0 < w k := fun k => (mul_pos hc1 (powSeq_pos s k)).trans_le (hwlo k)
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N, hN⟩ := eventually_atTop.1
    ((hall_lower_w hp hc1 hw0 hws hwlo (half_pos hε)).and (hall_upper_w hp hwp hws (half_pos hε)))
  refine ⟨N, fun n hn => ?_⟩
  obtain ⟨h1, h2⟩ := hN n hn
  rw [Real.dist_eq, sub_zero, abs_lt]
  constructor <;> linarith

end JacobiAsym
