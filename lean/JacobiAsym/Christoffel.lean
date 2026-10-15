import JacobiAsym.Recurrence
import JacobiAsym.ChainLimit

/-!
# The Christoffel shift (Paper 2 §3)

For a discrete measure `σ = ∑ w_k δ_{x_k}` (`DMeasure x w`) with atoms `x_k ≥ 0`, the measure
`xσ = ∑ (x_k w_k) δ_{x_k}` (weights `xw x w`) is again a `DMeasure`.

* `opoly_eval_zero`: `P_n(0) = (−1)ⁿ D_n(xσ) / D_n(σ)`; hence `christoffel_sign`: `(−1)ⁿ P_n(0) > 0`
  (Lemma `lem:zeros`, sign part).
* `cg n = −P_{n+1}(0)/P_n(0) > 0` (`u_n` of the paper), `ch 0 = 0`, `ch (n+1) = b_{n+1}²/cg n > 0` (`l_n`).
* `christoffel_ja_split`, `christoffel_jb2_split`: `a_n = u_n + l_n`, `b_{n+1}² = u_n l_{n+1}` (Lemma `lem:transfer`(i)).
* `christoffel_poly`: `X · P̃_n = P_{n+1} + u_n P_n`, where `P̃_n` are the monic OPs of `xσ`;
  `christoffel_transfer`: `ã_n = u_n + l_{n+1}`, `b̃_{n+1}² = u_{n+1} l_{n+1}` (Lemma `lem:transfer`(ii)).
* `christoffel_shift_law`: Theorem `thm:shift` without rate; `christoffel_shift_law_converse`: Remark `rem:converse`.
-/

open Finset Filter Topology Matrix Polynomial

namespace JacobiAsym

/-- Weights of the Christoffel-shifted measure `xσ`. -/
def xw (x w : ℕ → ℝ) : ℕ → ℝ := fun k => x k * w k

theorem DMeasure.x_pos {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (k : ℕ) : 0 < x k :=
  lt_of_le_of_lt (hx (k + 1)) (h.x_anti (Nat.lt_succ_self k))

/-- `xσ` is again a discrete measure satisfying the standing hypotheses. -/
theorem christoffel_DMeasure {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) : DMeasure x (xw x w) where
  w_pos k := mul_pos (h.x_pos hx k) (h.w_pos k)
  w_sum := by
    obtain ⟨B, hB⟩ := h.x_bdd
    refine Summable.of_norm_bounded (h.w_sum.mul_left B) (fun k => ?_)
    rw [Real.norm_eq_abs, xw, abs_mul, abs_of_pos (h.w_pos k)]
    exact mul_le_mul_of_nonneg_right (hB k) (h.w_pos k).le
  x_bdd := h.x_bdd
  x_anti := h.x_anti

theorem dip_xw (x w : ℕ → ℝ) (p q : ℝ[X]) : dip x (xw x w) p q = dip x w (X * p) q := by
  unfold dip xw; congr 1; funext k; rw [eval_mul, eval_X]; ring

theorem dip_sub_left {x w : ℕ → ℝ} (h : DMeasure x w) (p q r : ℝ[X]) :
    dip x w (p - q) r = dip x w p r - dip x w q r := by
  have := dip_add_left h (p - q) q r
  rw [sub_add_cancel] at this; linarith

/-- The minor of the first column is the Hankel determinant of `xσ`. -/
theorem opolyCof_zero (x w : ℕ → ℝ) (n : ℕ) : opolyCof x w n 0 = (hankel x (xw x w) n).det := by
  unfold opolyCof
  congr 1
  ext i l
  simp only [hankel, xw, mom, of_apply, Fin.succAbove_zero, Fin.val_succ]
  congr 1; funext k; ring

/-- `P_n(0) = (−1)ⁿ D_n(xσ) / D_n(σ)`. -/
theorem opoly_eval_zero (x w : ℕ → ℝ) (n : ℕ) :
    (opoly x w n).eval 0 = (-1) ^ n * (hankel x (xw x w) n).det / (hankel x w n).det := by
  rw [opoly_eq_sum, eval_finsetSum, Fin.sum_univ_succ]
  simp only [eval_mul, eval_C, eval_pow, eval_X, Fin.val_zero, pow_zero, mul_one, Fin.val_succ,
    zero_pow (Nat.succ_ne_zero _), mul_zero, sum_const_zero, add_zero, add_zero, opolyCof_zero]
  ring

/-- **Sign lemma** (Paper 2 Lemma `lem:zeros`, sign part): `(−1)ⁿ P_n(0) > 0` for atoms `x_k ≥ 0`. -/
theorem christoffel_sign {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    0 < (-1) ^ n * (opoly x w n).eval 0 := by
  rw [opoly_eval_zero, ← mul_div_assoc, ← mul_assoc, ← pow_add, ← two_mul, pow_mul, neg_one_sq, one_pow,
    one_mul]
  exact div_pos (hankel_det_pos (christoffel_DMeasure h hx) n) (hankel_det_pos h n)

theorem opoly_eval_zero_ne {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    (opoly x w n).eval 0 ≠ 0 := by
  intro h0; have := christoffel_sign h hx n; rw [h0, mul_zero] at this; exact lt_irrefl _ this

/-- `u_n = −P_{n+1}(0)/P_n(0)`. -/
noncomputable def cg (x w : ℕ → ℝ) (n : ℕ) : ℝ := -(opoly x w (n + 1)).eval 0 / (opoly x w n).eval 0

/-- `l_0 = 0`, `l_{n+1} = b_{n+1}² / u_n`. -/
noncomputable def ch (x w : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n + 1 => jb2 x w (n + 1) / cg x w n

theorem cg_pos {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) : 0 < cg x w n := by
  have h1 := christoffel_sign h hx (n + 1)
  have h0 := christoffel_sign h hx n
  have e : cg x w n = ((-1) ^ (n + 1) * (opoly x w (n + 1)).eval 0) / ((-1) ^ n * (opoly x w n).eval 0) := by
    unfold cg; rw [pow_succ]
    have : ((-1 : ℝ) ^ n) ≠ 0 := pow_ne_zero _ (by norm_num)
    field_simp
  rw [e]; exact div_pos h1 h0

theorem ch_pos {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) : 0 < ch x w (n + 1) :=
  div_pos (jb2_pos h _) (cg_pos h hx n)

/-- `X P_0 = P_1 + a_0 P_0` (the `k = 0` case of the recurrence). -/
theorem opoly_recurrence_zero {x w : ℕ → ℝ} (h : DMeasure x w) :
    X * opoly x w 0 = opoly x w 1 + C (ja x w 0) * opoly x w 0 := by
  have hPP : 0 < dip x w (opoly x w 0) (opoly x w 0) := by
    rw [dip_opoly_self h]; exact div_pos (hankel_det_pos h _) (hankel_det_pos h _)
  set R := X * opoly x w 0 - opoly x w 1 - C (ja x w 0) * opoly x w 0 with hR
  have hdeg : ∀ i, 0 < i → R.coeff i = 0 := by
    intro i hi
    simp only [hR, opoly_zero, mul_one, coeff_sub, coeff_X, coeff_C, if_neg hi.ne']
    rcases eq_or_lt_of_le (Nat.succ_le_of_lt hi) with heq | hlt
    · subst heq; rw [opoly_coeff_self h]; simp
    · rw [coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; exact hlt), if_neg (by omega)]; simp
  have htop : dip x w R (opoly x w 0) = 0 := by
    simp only [hR]
    rw [dip_sub_left h, dip_sub_left h, dip_smul_left]
    have h1 : dip x w (opoly x w 1) (opoly x w 0) = 0 := by
      rw [opoly_zero, ← pow_zero (X : ℝ[X])]; exact dip_opoly_pow h (by norm_num)
    rw [h1]
    unfold ja
    field_simp
    ring
  have hR0 := eq_zero_of_orth h hdeg (fun i hi => absurd hi (Nat.not_lt_zero _)) htop
  rw [hR] at hR0
  linear_combination hR0

/-- **Transfer (i)**: `a_n = u_n + l_n`. -/
theorem christoffel_ja_split {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    ja x w n = cg x w n + ch x w n := by
  have hne := opoly_eval_zero_ne h hx
  cases n with
  | zero =>
    have e := congrArg (eval 0) (opoly_recurrence_zero h)
    simp only [eval_X, eval_add, eval_C, opoly_zero, mul_one] at e
    simp only [ch, cg, opoly_zero, eval_one, div_one, add_zero]
    linarith
  | succ m =>
    have e := congrArg (eval 0) (opoly_recurrence h (k := m + 1) (by omega))
    simp only [eval_mul, eval_X, zero_mul, eval_add, eval_C, Nat.add_sub_cancel] at e
    simp only [ch, cg]
    have h1 := hne (m + 1); have h0 := hne m
    field_simp
    linear_combination -e

/-- **Transfer (i)**: `b_{n+1}² = u_n l_{n+1}`. -/
theorem christoffel_jb2_split {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    jb2 x w (n + 1) = cg x w n * ch x w (n + 1) := by
  simp only [ch]; field_simp [(cg_pos h hx n).ne']

/-- **Transfer (ii), polynomials**: `X · P̃_n = P_{n+1} + u_n P_n`, `P̃_n` the monic OPs of `xσ`. -/
theorem christoffel_poly {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    X * opoly x (xw x w) n = opoly x w (n + 1) + C (cg x w n) * opoly x w n := by
  have h' := christoffel_DMeasure h hx
  set R := opoly x w (n + 1) + C (cg x w n) * opoly x w n with hR
  have hR0 : R.coeff 0 = 0 := by
    rw [coeff_zero_eq_eval_zero, hR, eval_add, eval_mul, eval_C]
    unfold cg; field_simp [opoly_eval_zero_ne h hx n]; ring
  obtain ⟨R', hR'⟩ := X_dvd_iff.2 hR0
  rw [hR']
  congr 1
  -- coefficients of `R` from degree `n+1` on
  have hRc : ∀ j, n + 1 ≤ j → R.coeff j = if j = n + 1 then 1 else 0 := by
    intro j hj
    rw [hR, coeff_add, coeff_C_mul,
      coeff_eq_zero_of_natDegree_lt (p := opoly x w n) (by rw [opoly_natDegree h]; omega), mul_zero, add_zero]
    split_ifs with hj'
    · subst hj'; exact opoly_coeff_self h _
    · exact coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega)
  have hR'c : ∀ i, R'.coeff i = R.coeff (i + 1) := fun i => by rw [hR', coeff_X_mul]
  symm
  rw [← sub_eq_zero]
  have hS : ∀ i, n ≤ i → (R' - opoly x (xw x w) n).coeff i = 0 := by
    intro i hi
    rw [coeff_sub, hR'c, hRc _ (by omega)]
    rcases eq_or_lt_of_le hi with heq | hlt
    · subst heq; rw [if_pos rfl, opoly_coeff_self h']; ring
    · rw [if_neg (by omega), coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h']; exact hlt)]; ring
  apply eq_zero_of_orth h' (k := n) (fun i hi => hS i hi.le)
  · intro i hi
    rw [dip_sub_left h', dip_opoly_pow h' hi, dip_xw, ← hR', hR, dip_add_left h, dip_smul_left,
      dip_opoly_pow h (by omega), dip_opoly_pow h hi]
    ring
  · rw [dip_comm]; exact dip_opoly_of_coeff h' hS

/-- `P_{n+1} = P̃_{n+1} + l_{n+1} P̃_n`. -/
theorem christoffel_back {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    opoly x w (n + 1) = opoly x (xw x w) (n + 1) + C (ch x w (n + 1)) * opoly x (xw x w) n := by
  have e1 := opoly_recurrence h (k := n + 1) (by omega)
  simp only [Nat.add_sub_cancel] at e1
  rw [christoffel_ja_split h hx, christoffel_jb2_split h hx, map_add, map_mul] at e1
  have e2 := christoffel_poly h hx (n + 1)
  have e3 := christoffel_poly h hx n
  apply mul_left_cancel₀ (X_ne_zero : (X : ℝ[X]) ≠ 0)
  linear_combination e1 - e2 - C (ch x w (n + 1)) * e3

/-- **Transfer (ii), coefficients**: the Jacobi coefficients of `xσ` are `ã_n = u_n + l_{n+1}` and
`b̃_{n+1}² = u_{n+1} l_{n+1}` (Paper 2 Lemma `lem:transfer`(ii), eq. `eq:transfer`). -/
theorem christoffel_transfer {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) (n : ℕ) :
    ja x (xw x w) n = cg x w n + ch x w (n + 1) ∧
      jb2 x (xw x w) (n + 1) = cg x w (n + 1) * ch x w (n + 1) := by
  have h' := christoffel_DMeasure h hx
  -- `X P̃_n = P̃_{n+1} + (u_n + l_{n+1}) P̃_n + u_n l_n P̃_{n-1}`
  have hP : X * opoly x (xw x w) n = opoly x (xw x w) (n + 1) +
      C (cg x w n + ch x w (n + 1)) * opoly x (xw x w) n +
      C (cg x w n) * (opoly x w n - opoly x (xw x w) n) := by
    rw [christoffel_poly h hx, christoffel_back h hx, map_add]; ring
  constructor
  · cases n with
    | zero =>
      have e := opoly_recurrence_zero h'
      rw [hP, opoly_zero, opoly_zero, sub_self, mul_zero, add_zero, zero_add] at e
      have e' := add_left_cancel e
      simp only [mul_one] at e'
      exact (C_injective e').symm
    | succ m =>
      have e := opoly_recurrence h' (k := m + 1) (by omega)
      rw [hP, christoffel_back h hx m, Nat.add_sub_cancel] at e
      have := congrArg (coeff · (m + 1)) e
      simp only [coeff_add, coeff_C_mul, add_sub_cancel_left, opoly_coeff_self h',
        coeff_eq_zero_of_natDegree_lt (p := opoly x (xw x w) m) (n := m + 1) (by rw [opoly_natDegree h']; omega)] at this
      linarith
  · have e := opoly_recurrence h' (k := n + 1) (by omega)
    have hP1 : X * opoly x (xw x w) (n + 1) = opoly x (xw x w) (n + 1 + 1) +
        C (cg x w (n + 1) + ch x w (n + 2)) * opoly x (xw x w) (n + 1) +
        C (cg x w (n + 1) * ch x w (n + 1)) * opoly x (xw x w) n := by
      rw [christoffel_poly h hx, christoffel_back h hx, christoffel_back h hx n, map_add, map_mul]; ring
    rw [hP1, Nat.add_sub_cancel] at e
    have ha : ja x (xw x w) (n + 1) = cg x w (n + 1) + ch x w (n + 2) := by
      have := congrArg (coeff · (n + 1)) e
      simp only [coeff_add, coeff_C_mul, opoly_coeff_self h',
        coeff_eq_zero_of_natDegree_lt (p := opoly x (xw x w) n) (n := n + 1) (by rw [opoly_natDegree h']; omega)] at this
      linarith
    rw [ha] at e
    have e2 : C (jb2 x (xw x w) (n + 1) - cg x w (n + 1) * ch x w (n + 1)) * opoly x (xw x w) n = 0 := by
      rw [map_sub]; linear_combination e.symm
    rcases mul_eq_zero.1 e2 with h0 | h0
    · rw [C_eq_zero, sub_eq_zero] at h0; exact h0
    · exact absurd h0 (opoly_monic h' n).ne_zero

theorem sqrt_scale {s g l : ℝ} (hs : 0 < s) :
    s * Real.sqrt (g * l) = Real.sqrt ((s * g) * (s * l)) := by
  rw [show s * g * (s * l) = (s * s) * (g * l) by ring, Real.sqrt_mul (mul_self_nonneg s),
    Real.sqrt_mul_self hs.le]

/-- **Christoffel shift law** (Paper 2 Theorem `thm:shift`, without rate). For a discrete measure with atoms
`x_k ≥ 0` and a scale `s_n > 0` with `s_n / s_{n+1} → 1` (e.g. `s_n = n^p`): if `s_n a_n → 2c` and
`s_n b_n → c` (`c > 0`), then the same holds for the Jacobi coefficients of `xσ`. -/
theorem christoffel_shift_law {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) {c : ℝ} (hc : 0 < c)
    {s : ℕ → ℝ} (hs : ∀ n, 0 < s n) (hs1 : Tendsto (fun n => s n / s (n + 1)) atTop (𝓝 1))
    (hA : Tendsto (fun n => s n * ja x w n) atTop (𝓝 (2 * c)))
    (hB : Tendsto (fun n => s n * Real.sqrt (jb2 x w n)) atTop (𝓝 c)) :
    Tendsto (fun n => s n * ja x (xw x w) n) atTop (𝓝 (2 * c)) ∧
      Tendsto (fun n => s n * Real.sqrt (jb2 x (xw x w) n)) atTop (𝓝 c) := by
  obtain ⟨hU, hL⟩ := chain_limit hc hs hs1 (cg_pos h hx) (ch_pos h hx)
    (fun n => christoffel_ja_split h hx (n + 1)) (christoffel_jb2_split h hx) hA hB
  constructor
  · have := hU.add (hs1.mul (hL.comp (tendsto_add_atTop_nat 1)))
    rw [one_mul, ← two_mul] at this
    refine this.congr fun n => ?_
    simp only [Function.comp, (christoffel_transfer h hx n).1]
    field_simp [(hs (n + 1)).ne']
  · have := ((hU.mul hL).sqrt).comp (tendsto_add_atTop_nat 1)
    rw [Real.sqrt_mul_self hc.le] at this
    apply (tendsto_add_atTop_iff_nat 1).1
    refine this.congr fun n => ?_
    simp only [Function.comp, (christoffel_transfer h hx n).2]
    exact (sqrt_scale (g := cg x w (n + 1)) (l := ch x w (n + 1)) (hs _)).symm

/-- **Converse** (Paper 2 Remark `rem:converse`, without rate): the law for `xσ` implies the law for `σ`. -/
theorem christoffel_shift_law_converse {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) {c : ℝ}
    (hc : 0 < c) {s : ℕ → ℝ} (hs : ∀ n, 0 < s n) (hs1 : Tendsto (fun n => s n / s (n + 1)) atTop (𝓝 1))
    (hA : Tendsto (fun n => s n * ja x (xw x w) n) atTop (𝓝 (2 * c)))
    (hB : Tendsto (fun n => s n * Real.sqrt (jb2 x (xw x w) n)) atTop (𝓝 c)) :
    Tendsto (fun n => s n * ja x w n) atTop (𝓝 (2 * c)) ∧
      Tendsto (fun n => s n * Real.sqrt (jb2 x w n)) atTop (𝓝 c) := by
  have hs2 : Tendsto (fun n => s (n + 1) / s n) atTop (𝓝 1) := by
    have := hs1.inv₀ one_ne_zero
    rw [inv_one] at this
    exact this.congr fun n => inv_div _ _
  obtain ⟨hW, hU⟩ := chain_limit_core hc (U := fun n => s n * ch x w (n + 1)) (V := fun n => s n * cg x w n)
    (fun n => mul_pos (hs n) (ch_pos h hx n)) (fun n => mul_pos (hs _) (cg_pos h hx _))
    (hA.congr fun n => by rw [(christoffel_transfer h hx n).1]; ring)
    (by
      have hB1 := (hB.comp (tendsto_add_atTop_nat 1)).pow 2
      have := hs1.mul hB1
      rw [one_mul] at this
      refine this.congr fun n => ?_
      simp only [Function.comp]
      have hb0 : 0 ≤ jb2 x (xw x w) (n + 1) := (jb2_pos (christoffel_DMeasure h hx) _).le
      rw [mul_pow, Real.sq_sqrt hb0, (christoffel_transfer h hx n).2]
      field_simp [(hs (n + 1)).ne'])
  constructor
  · apply (tendsto_add_atTop_iff_nat 1).1
    have := (hU.comp (tendsto_add_atTop_nat 1)).add (hs2.mul hW)
    rw [one_mul, ← two_mul] at this
    refine this.congr fun n => ?_
    simp only [Function.comp, christoffel_ja_split h hx (n + 1)]
    field_simp [(hs n).ne']
  · apply (tendsto_add_atTop_iff_nat 1).1
    have := hs2.mul ((hU.mul hW).sqrt)
    rw [Real.sqrt_mul_self hc.le, one_mul] at this
    refine this.congr fun n => ?_
    simp only [christoffel_jb2_split h hx n]
    rw [← sqrt_scale (hs n)]
    field_simp [(hs n).ne']

/-- `(n/(n+1))^p → 1`. -/
theorem tendsto_ratio_rpow (p : ℝ) :
    Tendsto (fun n : ℕ => (n : ℝ) ^ p / ((n : ℝ) + 1) ^ p) atTop (𝓝 1) := by
  have := (tendsto_natCast_div_add_atTop (1 : ℝ)).rpow_const (p := p) (Or.inl one_ne_zero)
  rw [Real.one_rpow] at this
  refine this.congr fun n => ?_
  rw [Real.div_rpow (Nat.cast_nonneg n) (by positivity)]

/-- Scaling by `n^p` or by `(n+1)^p` gives the same limit. -/
theorem tendsto_rpow_succ_iff {p L : ℝ} (f : ℕ → ℝ) :
    Tendsto (fun n : ℕ => (n : ℝ) ^ p * f n) atTop (𝓝 L) ↔
      Tendsto (fun n : ℕ => ((n : ℝ) + 1) ^ p * f n) atTop (𝓝 L) := by
  have hr := tendsto_ratio_rpow p
  constructor
  · intro hf
    have := hf.div hr one_ne_zero
    rw [div_one] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    have h1 : (0 : ℝ) < (n : ℝ) ^ p := Real.rpow_pos_of_pos (by exact_mod_cast hn) p
    have h2 : (0 : ℝ) < ((n : ℝ) + 1) ^ p := Real.rpow_pos_of_pos (by positivity) p
    simp only [Pi.div_apply]
    field_simp
  · intro hf
    have := hr.mul hf
    rw [one_mul] at this
    refine this.congr fun n => ?_
    have h2 : (0 : ℝ) < ((n : ℝ) + 1) ^ p := Real.rpow_pos_of_pos (by positivity) p
    field_simp

/-- **Christoffel shift law at scale `n^p`** (Paper 2 Theorem `thm:shift` without rate, exactly as stated there):
for atoms `x_k ≥ 0`, `p > 0`, `c > 0`: `n^p a_n → 2c` and `n^p b_n → c` for `σ` imply the same for `xσ`, and
conversely. -/
theorem christoffel_shift_law_pow {x w : ℕ → ℝ} (h : DMeasure x w) (hx : ∀ k, 0 ≤ x k) {c p : ℝ} (hc : 0 < c) :
    (Tendsto (fun n : ℕ => (n : ℝ) ^ p * ja x w n) atTop (𝓝 (2 * c)) ∧
      Tendsto (fun n : ℕ => (n : ℝ) ^ p * Real.sqrt (jb2 x w n)) atTop (𝓝 c)) ↔
    (Tendsto (fun n : ℕ => (n : ℝ) ^ p * ja x (xw x w) n) atTop (𝓝 (2 * c)) ∧
      Tendsto (fun n : ℕ => (n : ℝ) ^ p * Real.sqrt (jb2 x (xw x w) n)) atTop (𝓝 c)) := by
  have hs : ∀ n : ℕ, 0 < ((n : ℝ) + 1) ^ p := fun n => Real.rpow_pos_of_pos (by positivity) p
  have hs1 : Tendsto (fun n : ℕ => ((n : ℝ) + 1) ^ p / (((n + 1 : ℕ) : ℝ) + 1) ^ p) atTop (𝓝 1) :=
    ((tendsto_ratio_rpow p).comp (tendsto_add_atTop_nat 1)).congr fun n => by simp [Function.comp]
  simp only [tendsto_rpow_succ_iff]
  constructor
  · rintro ⟨hA, hB⟩
    exact christoffel_shift_law h hx hc (s := fun n => ((n : ℝ) + 1) ^ p) hs hs1 hA hB
  · rintro ⟨hA, hB⟩
    exact christoffel_shift_law_converse h hx hc (s := fun n => ((n : ℝ) + 1) ^ p) hs hs1 hA hB

end JacobiAsym
