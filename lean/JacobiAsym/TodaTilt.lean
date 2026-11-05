import Mathlib

/-!
# Toda hierarchy for exponential tilts of a finite discrete measure

Source: `research/G1/RH/spectral/JZC_TODA.md` §2, **Lemma T.1** (and Remark (a), (b)).

**Specialisation.** μ = Σ_{i<M} w_i δ_{x_i} with `w_i > 0` and distinct real atoms `x_i` (the
"exactly M support points" case of Lemma T.1); a single time `t` with tilt `μ_t = e^{t x^j} μ`
(the multi-time version is automatic, Remark (b)). The monic orthogonal polynomial π_n(·;t),
`n ≤ M`, is defined by Cramer/Hankel: its lower coefficients solve `H_n(t) c = −(m_{n+l}(t))_l`.
Identities involving π_m as functions are stated on the support (i.e. in `L²(μ_t)`).

Covered: (2) `hasDerivAt_th`, `hasDerivAt_log_th`; (3) `hasDerivAt_log_tb2`, `hasDerivAt_tb`;
(1) `tpi_deriv_moment` (moment form) and `tpi_deriv_expansion` (expansion in π_m, on the
support); j = 1 Toda lattice `toda_log_b2`, `toda_a` (∂a_n = b_{n+1}² − b_n², 1 ≤ n, n + 1 ≤ M);
three-term recurrence `tpi_recurrence`. Not covered: (4) for general `j`, the case n = 0 of (3)/(4),
the matrix (L-form) identities, and real-analyticity (only differentiability is proved).
-/

open Finset Matrix

namespace JacobiAsym
namespace TodaTilt

/-- Determinant of a matrix-valued function with differentiable entries is differentiable. -/
theorem differentiableAt_det {n : ℕ} {A : ℝ → Matrix (Fin n) (Fin n) ℝ} {t : ℝ}
    (hA : ∀ a b, DifferentiableAt ℝ (fun s => A s a b) t) :
    DifferentiableAt ℝ (fun s => (A s).det) t := by
  simp only [Matrix.det_apply, Units.smul_def, zsmul_eq_mul]
  refine DifferentiableAt.fun_sum fun σ _ => ?_
  exact (differentiableAt_const _).mul (DifferentiableAt.fun_finsetProd fun i _ => hA _ _)

/-- Matrix inverse of a matrix-valued function with differentiable entries and nonzero
determinant is entrywise differentiable (Cramer's rule: `A⁻¹ = det⁻¹ • adj`). -/
theorem differentiableAt_inv_apply {n : ℕ} {A : ℝ → Matrix (Fin n) (Fin n) ℝ} {t : ℝ}
    (hA : ∀ a b, DifferentiableAt ℝ (fun s => A s a b) t) (hdet : ∀ s, (A s).det ≠ 0)
    (a b : Fin n) : DifferentiableAt ℝ (fun s => (A s)⁻¹ a b) t := by
  have e : (fun s => (A s)⁻¹ a b) =
      fun s => ((A s).det)⁻¹ * ((A s).updateRow b (Pi.single a 1)).det := by
    funext s
    rw [Matrix.inv_def, Ring.inverse_eq_inv', Matrix.smul_apply, Matrix.adjugate_apply, smul_eq_mul]
  rw [e]
  refine ((differentiableAt_det hA).inv (hdet t)).mul (differentiableAt_det fun c d => ?_)
  simp only [Matrix.updateRow_apply]
  split_ifs
  · exact differentiableAt_const _
  · exact hA c d

/-! ### The tilted finite measure -/

variable {M : ℕ} (x w : Fin M → ℝ) (j : ℕ)

/-- Weights of the tilted measure `μ_t = e^{t x^j} μ`, `μ = Σ_i w_i δ_{x_i}`. -/
noncomputable def tw (t : ℝ) (i : Fin M) : ℝ := w i * Real.exp (t * x i ^ j)

/-- Moments `m_k(t) = Σ_i w_i e^{t x_i^j} x_i^k`. -/
noncomputable def tmom (t : ℝ) (k : ℕ) : ℝ := ∑ i, tw x w j t i * x i ^ k

/-- Hankel matrix `H_n(t) = (m_{a+b}(t))_{a,b<n}`. -/
noncomputable def thank (n : ℕ) (t : ℝ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun a b => tmom x w j t ((a : ℕ) + b)

/-- Lower coefficients of the monic orthogonal polynomial: the solution of
`H_n(t) c = -(m_{n+l}(t))_{l<n}` (the orthogonality conditions `∫ π_n x^l dμ_t = 0`, `l < n`). -/
noncomputable def tcoef (n : ℕ) (t : ℝ) : Fin n → ℝ :=
  (thank x w j n t)⁻¹ *ᵥ fun l => -tmom x w j t (n + l)

/-- The monic orthogonal polynomial `π_n(y; t) = y^n + Σ_{k<n} c_k(t) y^k` (as a function of `y`). -/
noncomputable def tpi (n : ℕ) (t y : ℝ) : ℝ := y ^ n + ∑ k, tcoef x w j n t k * y ^ (k : ℕ)

/-- `h_n(t) = ∫ π_n(·;t)² dμ_t`. -/
noncomputable def th (n : ℕ) (t : ℝ) : ℝ := ∑ i, tw x w j t i * tpi x w j n t (x i) ^ 2

/-- `(J^r)_{nn}(t) = (1/h_n) ∫ x^r π_n² dμ_t` (diagonal of the `r`-th power of the Jacobi matrix). -/
noncomputable def tJdiag (r n : ℕ) (t : ℝ) : ℝ :=
  (∑ i, tw x w j t i * x i ^ r * tpi x w j n t (x i) ^ 2) / th x w j n t

theorem hasDerivAt_tw (t : ℝ) (i : Fin M) :
    HasDerivAt (fun s => tw x w j s i) (tw x w j t i * x i ^ j) t := by
  unfold tw
  have := ((hasDerivAt_id t).mul_const (x i ^ j)).exp.const_mul (w i)
  simpa [mul_assoc] using this

theorem differentiableAt_tmom (t : ℝ) (k : ℕ) :
    DifferentiableAt ℝ (fun s => tmom x w j s k) t := by
  unfold tmom
  exact DifferentiableAt.fun_sum fun i _ =>
    (hasDerivAt_tw x w j t i).differentiableAt.mul_const _

theorem quad_thank (n : ℕ) (t : ℝ) (c : Fin n → ℝ) :
    c ⬝ᵥ (thank x w j n t *ᵥ c) = ∑ i, tw x w j t i * (∑ k, c k * x i ^ (k : ℕ)) ^ 2 := by
  simp only [dotProduct, mulVec, thank, tmom, Matrix.of_apply, Finset.mul_sum, sq, Finset.sum_mul,
    pow_add]
  rw [Finset.sum_congr rfl fun a _ => Finset.sum_comm, Finset.sum_comm]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun a _ => ?_
  ring

variable {x w}

theorem tw_pos (hw : ∀ i, 0 < w i) (t : ℝ) (i : Fin M) : 0 < tw x w j t i :=
  mul_pos (hw i) (Real.exp_pos _)

/-- A coefficient vector of length `n ≤ M` whose polynomial vanishes at all (distinct) atoms is 0. -/
theorem coef_eq_zero_of_eval (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M) (c : Fin n → ℝ)
    (hc : ∀ i, ∑ k, c k * x i ^ (k : ℕ) = 0) : c = 0 := by
  set v : Fin n → ℝ := fun l => x (Fin.castLE hn l)
  have hv : Function.Injective v := hx.comp (Fin.castLE_injective hn)
  have hdet := (Matrix.det_vandermonde_ne_zero_iff (v := v)).2 hv
  by_contra hne
  apply hdet
  rw [← Matrix.exists_mulVec_eq_zero_iff]
  refine ⟨c, hne, ?_⟩
  funext l
  simp only [mulVec, dotProduct, Matrix.vandermonde_apply, Pi.zero_apply]
  rw [← hc (Fin.castLE hn l)]
  exact Finset.sum_congr rfl fun k _ => mul_comm _ _

theorem thank_det_ne_zero (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) : (thank x w j n t).det ≠ 0 := by
  intro h0
  obtain ⟨c, hc0, hc⟩ := Matrix.exists_mulVec_eq_zero_iff.2 h0
  apply hc0
  apply coef_eq_zero_of_eval hx hn
  have hq := quad_thank x w j n t c
  rw [hc, dotProduct_zero, eq_comm,
    Finset.sum_eq_zero_iff_of_nonneg fun i _ => mul_nonneg (tw_pos j hw t i).le (sq_nonneg _)] at hq
  intro i
  have := hq i (Finset.mem_univ _)
  rcases mul_eq_zero.1 this with h | h
  · exact absurd h (tw_pos j hw t i).ne'
  · exact pow_eq_zero_iff (two_ne_zero) |>.1 h

/-- `H_n(t) c(t) = -(m_{n+l}(t))_l`. -/
theorem thank_mulVec_tcoef (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) : thank x w j n t *ᵥ tcoef x w j n t = fun l : Fin n => -tmom x w j t (n + l) := by
  unfold tcoef
  rw [Matrix.mulVec_mulVec, Matrix.mul_nonsing_inv _ (isUnit_iff_ne_zero.2
    (thank_det_ne_zero j hw hx hn t)), Matrix.one_mulVec]

/-- Orthogonality: `∫ π_n(·;t) x^l dμ_t = 0` for `l < n`. -/
theorem tpi_orth (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M) (t : ℝ)
    (l : Fin n) : ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ (l : ℕ) = 0 := by
  have h := congrFun (thank_mulVec_tcoef j hw hx hn t) l
  simp only [mulVec, dotProduct, thank, Matrix.of_apply, tmom] at h
  have e : ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ (l : ℕ) =
      ∑ i, tw x w j t i * x i ^ (n + l) +
        ∑ k : Fin n, (∑ i, tw x w j t i * x i ^ ((l : ℕ) + k)) * tcoef x w j n t k := by
    simp only [tpi, Finset.sum_mul, mul_add, add_mul, Finset.mul_sum, Finset.sum_add_distrib, pow_add]
    congr 1
    · exact Finset.sum_congr rfl fun i _ => by ring
    · rw [Finset.sum_comm]
      exact Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun i _ => by ring
  rw [e, h]
  ring

/-- Orthogonality to every polynomial of degree `< n` (given by its coefficient vector `d`). -/
theorem tpi_orth_comb (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) (d : Fin n → ℝ) :
    ∑ i, tw x w j t i * tpi x w j n t (x i) * ∑ k, d k * x i ^ (k : ℕ) = 0 := by
  simp only [Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_eq_zero fun k _ => ?_
  have := tpi_orth j hw hx hn t k
  calc ∑ i, tw x w j t i * tpi x w j n t (x i) * (d k * x i ^ (k : ℕ))
      = d k * ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ (k : ℕ) := by
        rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring
    _ = 0 := by rw [this, mul_zero]

/-- The coefficients `c_k(t)` of `π_n(·;t)` are differentiable in `t` (Cramer's rule). -/
theorem differentiableAt_tcoef (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ}
    (hn : n ≤ M) (t : ℝ) (k : Fin n) : DifferentiableAt ℝ (fun s => tcoef x w j n s k) t := by
  unfold tcoef
  simp only [mulVec, dotProduct]
  refine DifferentiableAt.fun_sum fun l _ => ?_
  refine DifferentiableAt.mul ?_ (differentiableAt_tmom x w j t _).neg
  exact differentiableAt_inv_apply (fun a b => differentiableAt_tmom x w j t _)
    (fun s => thank_det_ne_zero j hw hx hn s) k l

/-- `∂_t π_n(x_i; t) = (∂_t π_n)(x_i)`, where `∂_t π_n = Σ_{k<n} c_k'(t) y^k` has degree `< n`. -/
theorem hasDerivAt_tpi (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t y : ℝ) : HasDerivAt (fun s => tpi x w j n s y)
      (∑ k, deriv (fun s => tcoef x w j n s k) t * y ^ (k : ℕ)) t := by
  unfold tpi
  refine HasDerivAt.const_add _ (HasDerivAt.fun_sum fun k _ => ?_)
  exact (differentiableAt_tcoef j hw hx hn t k).hasDerivAt.mul_const _

/-- **Lemma T.1 (2), derivative form.** `∂_t h_n = ∫ x^j π_n² dμ_t`
(the term `2∫ π_n ∂_tπ_n dμ_t` vanishes by orthogonality, `deg ∂_tπ_n < n`). -/
theorem hasDerivAt_th (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) : HasDerivAt (fun s => th x w j n s)
      (∑ i, tw x w j t i * x i ^ j * tpi x w j n t (x i) ^ 2) t := by
  set d : Fin n → ℝ := fun k => deriv (fun s => tcoef x w j n s k) t
  have hs := HasDerivAt.fun_sum (u := Finset.univ) fun i _ =>
    (hasDerivAt_tw x w j t i).mul ((hasDerivAt_tpi j hw hx hn t (x i)).pow 2)
  unfold th
  convert hs using 1
  have horth := tpi_orth_comb j hw hx hn t d
  rw [Finset.sum_add_distrib]
  have h2 : ∑ i, tw x w j t i * ((2 : ℕ) * tpi x w j n t (x i) ^ (2 - 1) *
      ∑ k, deriv (fun s => tcoef x w j n s k) t * x i ^ (k : ℕ)) = 0 := by
    rw [← mul_zero (2 : ℝ), ← horth, Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [d]
    push_cast
    ring
  rw [h2, add_zero]
  rfl

variable (x w) in
/-- Full coefficient vector `(c_0, …, c_{n-1}, 1)` of the monic `π_n`. -/
noncomputable def tfull (n : ℕ) (t : ℝ) : Fin (n + 1) → ℝ :=
  Fin.snoc (α := fun _ => ℝ) (tcoef x w j n t) 1

variable (x w) in
theorem tpi_eq_full (n : ℕ) (t y : ℝ) :
    tpi x w j n t y = ∑ k, tfull x w j n t k * y ^ (k : ℕ) := by
  rw [Fin.sum_univ_castSucc]
  simp [tfull, tpi, add_comm]

/-- `h_n(t) > 0` for `n < M` (a monic polynomial of degree `n < M` cannot vanish at all `M` atoms). -/
theorem th_pos (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n < M) (t : ℝ) :
    0 < th x w j n t := by
  unfold th
  refine lt_of_le_of_ne (Finset.sum_nonneg fun i _ => mul_nonneg (tw_pos j hw t i).le
    (sq_nonneg _)) fun h0 => ?_
  rw [eq_comm, Finset.sum_eq_zero_iff_of_nonneg fun i _ => mul_nonneg (tw_pos j hw t i).le
    (sq_nonneg _)] at h0
  have hz := coef_eq_zero_of_eval hx (n := n + 1) hn (tfull x w j n t) fun i => by
    rw [← tpi_eq_full]
    rcases mul_eq_zero.1 (h0 i (Finset.mem_univ _)) with h | h
    · exact absurd h (tw_pos j hw t i).ne'
    · exact pow_eq_zero_iff two_ne_zero |>.1 h
  have := congrFun hz (Fin.last n)
  simp [tfull] at this

/-- **Lemma T.1 (2).** `∂_t log h_n = (J^j)_{nn} = (1/h_n) ∫ x^j π_n² dμ_t`, `n < M`. -/
theorem hasDerivAt_log_th (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n < M)
    (t : ℝ) : HasDerivAt (fun s => Real.log (th x w j n s)) (tJdiag x w j j n t) t :=
  (hasDerivAt_th j hw hx hn.le t).log (th_pos j hw hx hn t).ne'

variable (x w) in
/-- `b_n² = h_n / h_{n-1}` (meaningful for `n ≥ 1`). -/
noncomputable def tb2 (n : ℕ) (t : ℝ) : ℝ := th x w j n t / th x w j (n - 1) t

variable (x w) in
/-- `a_n(t) = (1/h_n) ∫ x π_n² dμ_t = J_{nn}` (the diagonal recurrence coefficient, see
`ta_eq_of_recurrence`). -/
noncomputable def ta (n : ℕ) (t : ℝ) : ℝ := tJdiag x w j 1 n t

/-- **Lemma T.1 (3), log form.** `∂_t log b_n² = (J^j)_{nn} − (J^j)_{n−1,n−1}` for `1 ≤ n < M`. -/
theorem hasDerivAt_log_tb2 (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn1 : 1 ≤ n)
    (hn : n < M) (t : ℝ) : HasDerivAt (fun s => Real.log (tb2 x w j n s))
      (tJdiag x w j j n t - tJdiag x w j j (n - 1) t) t := by
  have e : (fun s => Real.log (tb2 x w j n s)) =
      fun s => Real.log (th x w j n s) - Real.log (th x w j (n - 1) s) := by
    funext s
    rw [tb2, Real.log_div (th_pos j hw hx hn s).ne' (th_pos j hw hx (by omega) s).ne']
  rw [e]
  exact (hasDerivAt_log_th j hw hx hn t).sub (hasDerivAt_log_th j hw hx (by omega) t)

/-- **Lemma T.1 (3).** `∂_t b_n = ½ b_n [(J^j)_{nn} − (J^j)_{n−1,n−1}]`, `b_n = √(h_n/h_{n−1})`,
`1 ≤ n < M`. -/
theorem hasDerivAt_tb (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn1 : 1 ≤ n)
    (hn : n < M) (t : ℝ) : HasDerivAt (fun s => Real.sqrt (tb2 x w j n s))
      (1 / 2 * Real.sqrt (tb2 x w j n t) * (tJdiag x w j j n t - tJdiag x w j j (n - 1) t)) t := by
  have hpos : ∀ s, 0 < tb2 x w j n s := fun s =>
    div_pos (th_pos j hw hx hn s) (th_pos j hw hx (by omega) s)
  have e : (fun s => Real.sqrt (tb2 x w j n s)) =
      fun s => Real.exp (Real.log (tb2 x w j n s) / 2) := by
    funext s
    rw [Real.exp_half, Real.exp_log (hpos s)]
  rw [e]
  have := ((hasDerivAt_log_tb2 j hw hx hn1 hn t).div_const 2).exp
  convert this using 1
  rw [Real.exp_half, Real.exp_log (hpos t)]
  ring

/-- **Toda lattice (Lemma T.1, Remark (a), `j = 1`).** For the tilt `e^{t x}`:
`∂_t log b_n² = a_n − a_{n−1}`, `1 ≤ n < M`. -/
theorem toda_log_b2 (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn1 : 1 ≤ n)
    (hn : n < M) (t : ℝ) : HasDerivAt (fun s => Real.log (tb2 x w 1 n s))
      (ta x w 1 n t - ta x w 1 (n - 1) t) t :=
  hasDerivAt_log_tb2 1 hw hx hn1 hn t

/-! ### Orthogonality of the family and identification of `a_n` -/

/-- Orthogonality of `π_n` to every polynomial `Σ_{k<r} d_k y^k`, `r ≤ n`. -/
theorem tpi_orth_le (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n r : ℕ} (hn : n ≤ M)
    (hr : r ≤ n) (t : ℝ) (d : Fin r → ℝ) :
    ∑ i, tw x w j t i * tpi x w j n t (x i) * ∑ k, d k * x i ^ (k : ℕ) = 0 := by
  simp only [Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_eq_zero fun k _ => ?_
  have := tpi_orth j hw hx hn t ⟨k, lt_of_lt_of_le k.2 hr⟩
  calc ∑ i, tw x w j t i * tpi x w j n t (x i) * (d k * x i ^ (k : ℕ))
      = d k * ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ (k : ℕ) := by
        rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring
    _ = 0 := by rw [this, mul_zero]

/-- `∫ π_n π_m dμ_t = 0` for `m < n ≤ M`. -/
theorem tpi_orth_pair (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n m : ℕ} (hn : n ≤ M)
    (hm : m < n) (t : ℝ) :
    ∑ i, tw x w j t i * tpi x w j n t (x i) * tpi x w j m t (x i) = 0 := by
  simp only [tpi_eq_full x w j m]
  exact tpi_orth_le j hw hx hn hm t _

/-- The coefficient `a_n` of the three-term recurrence `x π_n = π_{n+1} + a_n π_n + b_n² π_{n−1}`
(on the support of `μ_t`) is `ta = (1/h_n)∫ x π_n² dμ_t`; here `1 ≤ n`, `n + 1 ≤ M`. -/
theorem ta_eq_of_recurrence (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ}
    (hn1 : 1 ≤ n) (hn : n + 1 ≤ M) (t A B : ℝ)
    (hrec : ∀ i, x i * tpi x w j n t (x i) = tpi x w j (n + 1) t (x i) +
      A * tpi x w j n t (x i) + B * tpi x w j (n - 1) t (x i)) :
    A = ta x w j n t := by
  have h1 := tpi_orth_pair j hw hx hn (Nat.lt_succ_self n) t
  have h2 := tpi_orth_pair j hw hx (n := n) (m := n - 1) (by omega) (by omega) t
  have key : ∑ i, tw x w j t i * x i ^ 1 * tpi x w j n t (x i) ^ 2 =
      (∑ i, tw x w j t i * tpi x w j (n + 1) t (x i) * tpi x w j n t (x i)) +
      A * th x w j n t +
      B * ∑ i, tw x w j t i * tpi x w j n t (x i) * tpi x w j (n - 1) t (x i) := by
    simp only [th, Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    linear_combination (tw x w j t i * tpi x w j n t (x i)) * hrec i
  rw [h1, h2] at key
  have hpos := th_pos j hw hx (n := n) (by omega) t
  unfold ta tJdiag
  rw [key]
  field_simp
  ring

/-! ### Lemma T.1 (1) -/

/-- **Lemma T.1 (1), moment form.** Differentiating `∫ π_n x^l dμ_t = 0` (`l < n`):
`∫ (∂_tπ_n) x^l dμ_t = −∫ x^j π_n x^l dμ_t`, where `∂_tπ_n = Σ_{k<n} c_k'(t) y^k`. -/
theorem tpi_deriv_moment (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) (l : Fin n) :
    ∑ i, tw x w j t i * (∑ k, deriv (fun s => tcoef x w j n s k) t * x i ^ (k : ℕ)) *
        x i ^ (l : ℕ) =
      -∑ i, tw x w j t i * x i ^ j * tpi x w j n t (x i) * x i ^ (l : ℕ) := by
  have hF := HasDerivAt.fun_sum (u := Finset.univ) fun i _ =>
    ((hasDerivAt_tw x w j t i).mul (hasDerivAt_tpi j hw hx hn t (x i))).mul_const
      (x i ^ (l : ℕ))
  have h0 : (fun s => ∑ i, ((fun s => tw x w j s i) * fun s => tpi x w j n s (x i)) s *
      x i ^ (l : ℕ)) = fun _ => 0 := funext fun s => tpi_orth j hw hx hn s l
  rw [h0] at hF
  have := hF.unique (hasDerivAt_const t (0 : ℝ))
  simp only [add_mul, Finset.sum_add_distrib] at this
  linear_combination this

/-- Triangularity: a function on the atoms orthogonal (in `L²(μ_t)`) to `π_0, …, π_{n−1}` is
orthogonal to `1, y, …, y^{n−1}`. -/
theorem orth_pow_of_orth_tpi {n : ℕ} (t : ℝ) (D : Fin M → ℝ)
    (hD : ∀ m < n, ∑ i, tw x w j t i * D i * tpi x w j m t (x i) = 0) :
    ∀ l < n, ∑ i, tw x w j t i * D i * x i ^ l = 0 := by
  intro l
  induction l using Nat.strong_induction_on with
  | _ l ih =>
    intro hl
    have h := hD l hl
    have e : ∑ i, tw x w j t i * D i * tpi x w j l t (x i) =
        ∑ i, tw x w j t i * D i * x i ^ l +
          ∑ k : Fin l, tcoef x w j l t k * ∑ i, tw x w j t i * D i * x i ^ (k : ℕ) := by
      simp only [tpi, mul_add, Finset.sum_add_distrib, Finset.mul_sum]
      congr 1
      rw [Finset.sum_comm]
      exact Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun i _ => by ring
    have hz : ∑ k : Fin l, tcoef x w j l t k * ∑ i, tw x w j t i * D i * x i ^ (k : ℕ) = 0 :=
      Finset.sum_eq_zero fun k _ => by rw [ih k k.2 (by omega), mul_zero]
    linarith

/-- **Lemma T.1 (1).** `∂_tπ_n = −Σ_{m<n} (∫ x^j π_n π_m dμ_t / h_m) π_m` in `L²(μ_t)`, i.e. at every
atom `x_i` (`n ≤ M`). Here `∂_tπ_n(y) = Σ_{k<n} c_k'(t) y^k` is the `t`-derivative of `π_n(y;t)`
(`hasDerivAt_tpi`). -/
theorem tpi_deriv_expansion (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) (i : Fin M) :
    ∑ k, deriv (fun s => tcoef x w j n s k) t * x i ^ (k : ℕ) =
      -∑ m : Fin n, ((∑ a, tw x w j t a * x a ^ j * tpi x w j n t (x a) * tpi x w j m t (x a)) /
        th x w j m t) * tpi x w j m t (x i) := by
  set β : Fin n → ℝ := fun m =>
    (∑ a, tw x w j t a * x a ^ j * tpi x w j n t (x a) * tpi x w j m t (x a)) / th x w j m t
  set P' : Fin M → ℝ := fun a => ∑ k, deriv (fun s => tcoef x w j n s k) t * x a ^ (k : ℕ)
  set D : Fin M → ℝ := fun a => P' a + ∑ m : Fin n, β m * tpi x w j m t (x a)
  -- (i) `⟨∂π_n, π_m⟩ = −⟨x^j π_n, π_m⟩`
  have hi : ∀ m : ℕ, m < n → ∑ a, tw x w j t a * P' a * tpi x w j m t (x a) =
      -∑ a, tw x w j t a * x a ^ j * tpi x w j n t (x a) * tpi x w j m t (x a) := by
    intro m hm
    simp only [tpi_eq_full x w j m, Finset.mul_sum]
    rw [Finset.sum_comm, Finset.sum_comm (s := Finset.univ (α := Fin M)), ← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun k _ => ?_
    have := tpi_deriv_moment j hw hx hn t ⟨k, by omega⟩
    simp only [P'] at this ⊢
    calc ∑ a, tw x w j t a * (∑ k, deriv (fun s => tcoef x w j n s k) t * x a ^ (k : ℕ)) *
          (tfull x w j m t k * x a ^ (k : ℕ))
        = tfull x w j m t k * ∑ a, tw x w j t a *
          (∑ k, deriv (fun s => tcoef x w j n s k) t * x a ^ (k : ℕ)) * x a ^ (k : ℕ) := by
          rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun a _ => by ring
      _ = -∑ a, tw x w j t a * x a ^ j * tpi x w j n t (x a) *
          (tfull x w j m t k * x a ^ (k : ℕ)) := by
          rw [this, mul_neg, Finset.mul_sum]
          exact congrArg _ (Finset.sum_congr rfl fun a _ => by ring)
  -- (ii) `⟨Σ β_{m'} π_{m'}, π_m⟩ = β_m h_m`
  have hii : ∀ m : Fin n, ∑ a, tw x w j t a * (∑ m' : Fin n, β m' * tpi x w j m' t (x a)) *
      tpi x w j m t (x a) = β m * th x w j m t := by
    intro m
    simp only [Finset.mul_sum, Finset.sum_mul]
    rw [Finset.sum_comm]
    rw [Finset.sum_eq_single m]
    · simp only [th, Finset.mul_sum]
      exact Finset.sum_congr rfl fun a _ => by ring
    · intro m' _ hne
      have hne' : (m' : ℕ) ≠ m := fun h => hne (Fin.ext h)
      rcases lt_or_gt_of_ne hne' with hlt | hlt
      · have := tpi_orth_pair j hw hx (n := m) (m := m') (by omega) hlt t
        rw [← mul_zero (β m'), ← this, Finset.mul_sum]
        exact Finset.sum_congr rfl fun a _ => by ring
      · have := tpi_orth_pair j hw hx (n := m') (m := m) (by omega) hlt t
        rw [← mul_zero (β m'), ← this, Finset.mul_sum]
        exact Finset.sum_congr rfl fun a _ => by ring
    · intro h; exact absurd (Finset.mem_univ m) h
  -- (a) `D ⊥ π_m`, `m < n`
  have ha : ∀ m < n, ∑ a, tw x w j t a * D a * tpi x w j m t (x a) = 0 := by
    intro m hm
    have h1 := hi m hm
    have h2 := hii ⟨m, hm⟩
    have hpos := th_pos j hw hx (n := m) (by omega) t
    have e : ∑ a, tw x w j t a * D a * tpi x w j m t (x a) =
        ∑ a, tw x w j t a * P' a * tpi x w j m t (x a) +
        ∑ a, tw x w j t a * (∑ m' : Fin n, β m' * tpi x w j m' t (x a)) * tpi x w j m t (x a) := by
      rw [← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun a _ => by simp only [D]; ring
    rw [e, h1, h2]
    simp only [β]
    field_simp
    ring
  -- (b) `D ⊥ y^l`, `l < n`
  have hb := orth_pow_of_orth_tpi j t D ha
  -- (c) `⟨D, D⟩ = 0`
  have hc : ∑ a, tw x w j t a * D a ^ 2 = 0 := by
    have e : ∑ a, tw x w j t a * D a ^ 2 =
        ∑ k : Fin n, deriv (fun s => tcoef x w j n s k) t *
          ∑ a, tw x w j t a * D a * x a ^ (k : ℕ) +
        ∑ m : Fin n, β m * ∑ a, tw x w j t a * D a * tpi x w j m t (x a) := by
      simp only [Finset.mul_sum]
      rw [Finset.sum_comm, Finset.sum_comm (s := (Finset.univ : Finset (Fin n))) (t := Finset.univ),
        ← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun a _ => ?_
      conv_lhs => rw [sq]; enter [2, 2]; simp only [D, P']
      simp only [mul_add, Finset.mul_sum]
      congr 1 <;> exact Finset.sum_congr rfl fun k _ => by ring
    rw [e]
    rw [Finset.sum_eq_zero fun k _ => by rw [hb k k.2, mul_zero],
      Finset.sum_eq_zero fun m _ => by rw [ha m m.2, mul_zero], add_zero]
  rw [Finset.sum_eq_zero_iff_of_nonneg fun a _ => mul_nonneg (tw_pos j hw t a).le
    (sq_nonneg _)] at hc
  have hDi : D i = 0 := by
    rcases mul_eq_zero.1 (hc i (Finset.mem_univ _)) with h | h
    · exact absurd h (tw_pos j hw t i).ne'
    · exact pow_eq_zero_iff two_ne_zero |>.1 h
  simp only [D, P', β] at hDi
  linarith

/-! ### The three-term recurrence and the Toda equation for `a_n` (`j = 1`) -/

theorem tpi_inner_pow_self (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn : n ≤ M)
    (t : ℝ) : ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ n = th x w j n t := by
  have h := tpi_orth_comb j hw hx hn t (tcoef x w j n t)
  have e : th x w j n t = ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ n +
      ∑ i, tw x w j t i * tpi x w j n t (x i) * ∑ k, tcoef x w j n t k * x i ^ (k : ℕ) := by
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    conv_lhs => rw [sq]; enter [2, 2]; rw [tpi]
    ring
  rw [e, h, add_zero]

/-- `∫ x π_n π_m dμ_t = Σ_{k≤m} [π_m]_k ∫ π_n x^{k+1} dμ_t`. -/
theorem inner_x_tpi_eq (n m : ℕ) (t : ℝ) :
    ∑ i, tw x w j t i * x i * tpi x w j n t (x i) * tpi x w j m t (x i) =
      ∑ k : Fin (m + 1), tfull x w j m t k *
        ∑ i, tw x w j t i * tpi x w j n t (x i) * x i ^ ((k : ℕ) + 1) := by
  simp only [tpi_eq_full x w j m, Finset.mul_sum]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun i _ => by ring

/-- `∫ x π_n π_m dμ_t = 0` for `m + 1 < n ≤ M`. -/
theorem inner_x_tpi_lt (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n m : ℕ} (hn : n ≤ M)
    (hm : m + 1 < n) (t : ℝ) :
    ∑ i, tw x w j t i * x i * tpi x w j n t (x i) * tpi x w j m t (x i) = 0 := by
  rw [inner_x_tpi_eq]
  exact Finset.sum_eq_zero fun k _ => by
    rw [tpi_orth j hw hx hn t ⟨(k : ℕ) + 1, by omega⟩, mul_zero]

/-- `∫ x π_{m+1} π_m dμ_t = h_{m+1}` for `m + 1 ≤ M`. -/
theorem inner_x_tpi_succ (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {m : ℕ}
    (hm : m + 1 ≤ M) (t : ℝ) :
    ∑ i, tw x w j t i * x i * tpi x w j (m + 1) t (x i) * tpi x w j m t (x i) =
      th x w j (m + 1) t := by
  rw [inner_x_tpi_eq, Fin.sum_univ_castSucc]
  rw [Finset.sum_eq_zero fun k _ => by
    rw [Fin.val_castSucc, tpi_orth j hw hx hm t ⟨(k : ℕ) + 1, by omega⟩, mul_zero]]
  simp only [tfull, Fin.snoc_last, Fin.val_last, one_mul, zero_add]
  exact tpi_inner_pow_self j hw hx hm t

theorem tpi_orth_pair' (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n m : ℕ} (hn : n ≤ M)
    (hm : m < n) (t : ℝ) :
    ∑ i, tw x w j t i * tpi x w j m t (x i) * tpi x w j n t (x i) = 0 := by
  rw [← tpi_orth_pair j hw hx hn hm t]
  exact Finset.sum_congr rfl fun i _ => by ring

theorem th_eq_inner (n : ℕ) (t : ℝ) :
    ∑ i, tw x w j t i * tpi x w j n t (x i) * tpi x w j n t (x i) = th x w j n t :=
  Finset.sum_congr rfl fun i _ => by ring

/-- **Three-term recurrence** on the support of `μ_t`:
`x π_n = π_{n+1} + a_n π_n + b_n² π_{n−1}` with `a_n = ta`, `b_n² = h_n/h_{n−1}`
(`1 ≤ n`, `n + 1 ≤ M`; at the atoms, i.e. in `L²(μ_t)`). -/
theorem tpi_recurrence (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn1 : 1 ≤ n)
    (hn : n + 1 ≤ M) (t : ℝ) (a : Fin M) :
    x a * tpi x w j n t (x a) = tpi x w j (n + 1) t (x a) + ta x w j n t * tpi x w j n t (x a) +
      tb2 x w j n t * tpi x w j (n - 1) t (x a) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  have hmm : m + 1 - 1 = m := by omega
  rw [hmm]
  set A := ta x w j (m + 1) t with hA
  set B := tb2 x w j (m + 1) t with hB
  have hB' : B = th x w j (m + 1) t / th x w j m t := by rw [hB, tb2, hmm]
  have hp1 := th_pos j hw hx (n := m + 1) (by omega) t
  have hp0 := th_pos j hw hx (n := m) (by omega) t
  set R : Fin M → ℝ := fun a => x a * tpi x w j (m + 1) t (x a) - tpi x w j (m + 2) t (x a) -
    A * tpi x w j (m + 1) t (x a) - B * tpi x w j m t (x a) with hR
  have hRπ : ∀ m' < m + 2, ∑ a, tw x w j t a * R a * tpi x w j m' t (x a) = 0 := by
    intro m' hm'
    have e : ∑ a, tw x w j t a * R a * tpi x w j m' t (x a) =
        ∑ a, tw x w j t a * x a * tpi x w j (m + 1) t (x a) * tpi x w j m' t (x a) -
        ∑ a, tw x w j t a * tpi x w j (m + 2) t (x a) * tpi x w j m' t (x a) -
        A * ∑ a, tw x w j t a * tpi x w j (m + 1) t (x a) * tpi x w j m' t (x a) -
        B * ∑ a, tw x w j t a * tpi x w j m t (x a) * tpi x w j m' t (x a) := by
      simp only [Finset.mul_sum, ← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun a _ => by simp only [R]; ring
    rw [e]
    rcases lt_trichotomy m' m with h | h | h
    · rw [inner_x_tpi_lt j hw hx (n := m + 1) (by omega) (by omega) t,
        tpi_orth_pair j hw hx (n := m + 2) hn (by omega) t,
        tpi_orth_pair j hw hx (n := m + 1) (by omega) (by omega) t,
        tpi_orth_pair j hw hx (n := m) (by omega) h t]
      ring
    · rw [h, inner_x_tpi_succ j hw hx (by omega) t,
        tpi_orth_pair j hw hx (n := m + 2) hn (by omega) t,
        tpi_orth_pair j hw hx (n := m + 1) (by omega) (by omega) t, th_eq_inner, hB']
      field_simp
      ring
    · obtain rfl : m' = m + 1 := by omega
      have hxA : ∑ a, tw x w j t a * x a * tpi x w j (m + 1) t (x a) *
          tpi x w j (m + 1) t (x a) = A * th x w j (m + 1) t := by
        rw [hA, ta, tJdiag, div_mul_cancel₀ _ hp1.ne']
        exact Finset.sum_congr rfl fun a _ => by ring
      rw [hxA, tpi_orth_pair j hw hx (n := m + 2) hn (by omega) t, th_eq_inner,
        tpi_orth_pair' j hw hx (n := m + 1) (by omega) (by omega) t]
      ring
  have hRx := orth_pow_of_orth_tpi j t R hRπ
  have hRR : ∑ a, tw x w j t a * R a ^ 2 = 0 := by
    have e1 : ∑ k : Fin (m + 1), tcoef x w j (m + 1) t k *
          ∑ a, tw x w j t a * R a * x a ^ ((k : ℕ) + 1) =
        ∑ a, tw x w j t a * R a * (x a * ∑ k, tcoef x w j (m + 1) t k * x a ^ (k : ℕ)) := by
      simp only [Finset.mul_sum]
      rw [Finset.sum_comm]
      exact Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun k _ => by ring
    have e2 : ∑ k : Fin (m + 2), tcoef x w j (m + 2) t k *
          ∑ a, tw x w j t a * R a * x a ^ (k : ℕ) =
        ∑ a, tw x w j t a * R a * ∑ k, tcoef x w j (m + 2) t k * x a ^ (k : ℕ) := by
      simp only [Finset.mul_sum]
      rw [Finset.sum_comm]
      exact Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun k _ => by ring
    have e : ∑ a, tw x w j t a * R a ^ 2 =
        ∑ k : Fin (m + 1), tcoef x w j (m + 1) t k *
          ∑ a, tw x w j t a * R a * x a ^ ((k : ℕ) + 1) -
        ∑ k : Fin (m + 2), tcoef x w j (m + 2) t k * ∑ a, tw x w j t a * R a * x a ^ (k : ℕ) -
        A * ∑ a, tw x w j t a * R a * tpi x w j (m + 1) t (x a) -
        B * ∑ a, tw x w j t a * R a * tpi x w j m t (x a) := by
      rw [e1, e2, Finset.mul_sum _ _ A, Finset.mul_sum _ _ B, ← Finset.sum_sub_distrib,
        ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
      refine Finset.sum_congr rfl fun a _ => ?_
      have hRa : R a = x a * ∑ k, tcoef x w j (m + 1) t k * x a ^ (k : ℕ) -
          ∑ k, tcoef x w j (m + 2) t k * x a ^ (k : ℕ) -
          A * tpi x w j (m + 1) t (x a) - B * tpi x w j m t (x a) := by
        simp only [R, tpi]
        ring
      conv_lhs => rw [sq]; enter [2, 2]; rw [hRa]
      ring
    rw [e, Finset.sum_eq_zero fun k _ => by rw [hRx _ (by omega), mul_zero],
      Finset.sum_eq_zero fun k _ => by rw [hRx _ (by omega), mul_zero],
      hRπ _ (by omega), hRπ _ (by omega)]
    ring
  rw [Finset.sum_eq_zero_iff_of_nonneg fun a _ => mul_nonneg (tw_pos j hw t a).le
    (sq_nonneg _)] at hRR
  have hRa : R a = 0 := by
    rcases mul_eq_zero.1 (hRR a (Finset.mem_univ _)) with h | h
    · exact absurd h (tw_pos j hw t a).ne'
    · exact pow_eq_zero_iff two_ne_zero |>.1 h
  simp only [R] at hRa
  linarith

/-- **Toda lattice, `a`-equation (Lemma T.1 (4), Remark (a), `j = 1`).** For the tilt `e^{t x}`:
`∂_t a_n = b_{n+1}² − b_n²` for `1 ≤ n`, `n + 1 ≤ M`. (For `n + 1 = M`, `h_M = 0` since `π_M`
vanishes on the support, so `b_M² = 0`, matching the convention `b_M := 0` of Lemma T.1 (4).) -/
theorem toda_a (hw : ∀ i, 0 < w i) (hx : Function.Injective x) {n : ℕ} (hn1 : 1 ≤ n)
    (hn : n + 1 ≤ M) (t : ℝ) :
    HasDerivAt (fun s => ta x w 1 n s) (tb2 x w 1 (n + 1) t - tb2 x w 1 n t) t := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  have hmm : m + 1 - 1 = m := by omega
  have hp1 := th_pos 1 hw hx (n := m + 1) (by omega) t
  have hp0 := th_pos 1 hw hx (n := m) (by omega) t
  have hN := HasDerivAt.fun_sum (u := Finset.univ) fun a _ =>
    ((hasDerivAt_tw x w 1 t a).mul_const (x a ^ 1)).mul
      ((hasDerivAt_tpi 1 hw hx (n := m + 1) (by omega) t (x a)).pow 2)
  have hq := hN.div (hasDerivAt_th 1 hw hx (n := m + 1) (by omega) t) hp1.ne'
  have hfun : (fun s => ta x w 1 (m + 1) s) = fun s =>
      (∑ a, ((fun s => tw x w 1 s a * x a ^ 1) * (fun s => tpi x w 1 (m + 1) s (x a)) ^ 2) s) /
        th x w 1 (m + 1) s := by
    funext s
    rfl
  rw [hfun]
  convert hq using 1
  -- the cross term `∫ x π_n ∂π_n = −b_n² h_n`
  have hcross : ∑ a, tw x w 1 t a * x a * tpi x w 1 (m + 1) t (x a) *
      ∑ k, deriv (fun s => tcoef x w 1 (m + 1) s k) t * x a ^ (k : ℕ) =
      -(th x w 1 (m + 1) t / th x w 1 m t * th x w 1 (m + 1) t) := by
    have hexp := fun a => tpi_deriv_expansion 1 hw hx (n := m + 1) (by omega) t a
    simp only [pow_one] at hexp
    simp only [hexp, mul_neg, Finset.mul_sum, Finset.sum_neg_distrib]
    rw [Finset.sum_comm, Finset.sum_eq_single (⟨m, by omega⟩ : Fin (m + 1))]
    · have h1 := inner_x_tpi_succ 1 hw hx (m := m) (by omega) t
      rw [h1]
      congr 1
      calc _ = th x w 1 (m + 1) t / th x w 1 m t * ∑ a, tw x w 1 t a * x a *
            tpi x w 1 (m + 1) t (x a) * tpi x w 1 m t (x a) := by
            rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun a _ => by ring
        _ = _ := by rw [h1]
    · intro b _ hb
      have hb' : (b : ℕ) < m := by
        have := b.2
        have : (b : ℕ) ≠ m := fun h => hb (Fin.ext h)
        omega
      rw [inner_x_tpi_lt 1 hw hx (n := m + 1) (m := b) (by omega) (by omega) t]
      simp
    · intro h; exact absurd (Finset.mem_univ _) h
  -- `∫ x² π_n² = h_{n+1} + a_n² h_n + b_n⁴ h_{n−1}`
  have hrec := tpi_recurrence 1 hw hx (n := m + 1) (by omega) hn t
  rw [hmm] at hrec
  set A := ta x w 1 (m + 1) t with hA
  set B := tb2 x w 1 (m + 1) t with hB
  have hB' : B = th x w 1 (m + 1) t / th x w 1 m t := by rw [hB, tb2, hmm]
  have hsq : ∑ i, tw x w 1 t i * x i ^ 1 * x i ^ 1 * tpi x w 1 (m + 1) t (x i) ^ 2 =
      th x w 1 (m + 1 + 1) t + A ^ 2 * th x w 1 (m + 1) t + B ^ 2 * th x w 1 m t := by
    have e : ∀ i, tw x w 1 t i * x i ^ 1 * x i ^ 1 * tpi x w 1 (m + 1) t (x i) ^ 2 =
        tw x w 1 t i * (tpi x w 1 (m + 1 + 1) t (x i) + A * tpi x w 1 (m + 1) t (x i) +
          B * tpi x w 1 m t (x i)) ^ 2 := by
      intro i; rw [← hrec i]; ring
    rw [Finset.sum_congr rfl fun i _ => e i]
    have expand : ∑ i, tw x w 1 t i * (tpi x w 1 (m + 1 + 1) t (x i) +
          A * tpi x w 1 (m + 1) t (x i) + B * tpi x w 1 m t (x i)) ^ 2 =
        ∑ i, tw x w 1 t i * tpi x w 1 (m + 1 + 1) t (x i) * tpi x w 1 (m + 1 + 1) t (x i) +
        A ^ 2 * ∑ i, tw x w 1 t i * tpi x w 1 (m + 1) t (x i) * tpi x w 1 (m + 1) t (x i) +
        B ^ 2 * ∑ i, tw x w 1 t i * tpi x w 1 m t (x i) * tpi x w 1 m t (x i) +
        2 * A * ∑ i, tw x w 1 t i * tpi x w 1 (m + 1 + 1) t (x i) * tpi x w 1 (m + 1) t (x i) +
        2 * B * ∑ i, tw x w 1 t i * tpi x w 1 (m + 1 + 1) t (x i) * tpi x w 1 m t (x i) +
        2 * A * B * ∑ i, tw x w 1 t i * tpi x w 1 (m + 1) t (x i) * tpi x w 1 m t (x i) := by
      simp only [Finset.mul_sum, ← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun i _ => by ring
    rw [expand, th_eq_inner, th_eq_inner, th_eq_inner,
      tpi_orth_pair 1 hw hx (n := m + 1 + 1) hn (by omega) t,
      tpi_orth_pair 1 hw hx (n := m + 1 + 1) hn (by omega) t,
      tpi_orth_pair 1 hw hx (n := m + 1) (by omega) (by omega) t]
    ring
  have hN0 : ∑ i, tw x w 1 t i * x i ^ 1 * tpi x w 1 (m + 1) t (x i) ^ 2 =
      A * th x w 1 (m + 1) t := by
    rw [hA, ta, tJdiag, div_mul_cancel₀ _ hp1.ne']
  have hS : ∑ i, (tw x w 1 t i * x i ^ 1 * x i ^ 1 *
        ((fun s => tpi x w 1 (m + 1) s (x i)) ^ 2) t +
      tw x w 1 t i * x i ^ 1 * (((2 : ℕ) : ℝ) * tpi x w 1 (m + 1) t (x i) ^ (2 - 1) *
        ∑ k, deriv (fun s => tcoef x w 1 (m + 1) s k) t * x i ^ (k : ℕ))) =
      ∑ i, tw x w 1 t i * x i ^ 1 * x i ^ 1 * tpi x w 1 (m + 1) t (x i) ^ 2 +
      2 * ∑ i, tw x w 1 t i * x i * tpi x w 1 (m + 1) t (x i) *
        ∑ k, deriv (fun s => tcoef x w 1 (m + 1) s k) t * x i ^ (k : ℕ) := by
    rw [Finset.sum_add_distrib, Finset.mul_sum]
    congr 1
    exact Finset.sum_congr rfl fun i _ => by push_cast; ring
  have hN1 : (∑ i, ((fun y => tw x w 1 y i * x i ^ 1) *
      (fun s => tpi x w 1 (m + 1) s (x i)) ^ 2) t) = A * th x w 1 (m + 1) t := hN0
  rw [hS, hcross, hsq, hN0, hN1]
  rw [show tb2 x w 1 (m + 1 + 1) t = th x w 1 (m + 1 + 1) t / th x w 1 (m + 1) t from rfl, hB']
  field_simp
  ring

end TodaTilt
end JacobiAsym
