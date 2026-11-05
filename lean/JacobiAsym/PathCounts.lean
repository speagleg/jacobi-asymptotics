import Mathlib

/-! # Path counts of the free Jacobi operator (Lemma R of JZC_SHIFT; Paper IV eq. `eq:Qk`)

* `pathH`, `pathG`: the dispersionless Hamiltonians `H_j(a,b)`, `G_j(a,b)` of
  research/G1/RH/spectral/JZC_SHIFT.md §2.2 (Lemma D), as the factorial sums stated there.
* `pathH_eq_coeff`, `pathG_eq_coeff`: they are the `X^j`, resp. `b·X^{j+1}`, coefficients of
  `(b + aX + bX²)^j`; `freeJacobi_pow_coeff_zero`, `freeJacobi_pow_coeff_one`: equivalently the
  `T⁰` coefficient and `b·`(`T¹` coefficient) of `J^j`, `J = a + bT + bT⁻¹` (path counts with
  stays `a`, up/down steps `b`).
* **Lemma R** (§2.3): `pathH_two_mul`, `pathG_two_mul` (`H_j(2b,b) = C(2j,j)b^j`,
  `G_j(2b,b) = C(2j,j)(j/(j+1))b^{j+1}`), and the derivative form `deriv_pathG_two_mul`.
* Paper IV (papers/paperIV/p2_frame.tex, eq. `eq:Qk`): `tiltQ_four_mul`,
  `Q_k(4c) = ½ c^{k−1} k C(2k,k)`, from `two_mul_sum_centralBinom_four_pow`.
* The resonance weight `W(j) = C(2j,j)c^j` (research/G1/RH/second_order/E3.md Cor. E3.3) and its
  ratio recursion `resW_succ`. -/

open Polynomial Finset

namespace JacobiAsym

/-- Path polynomial `P(X) = b + a X + b X²` (down ↦ `b`, stay ↦ `a X`, up ↦ `b X²`). -/
noncomputable def pathPoly {R : Type*} [CommRing R] (a b : R) : R[X] :=
  C b + C a * X + C b * X ^ 2

/-- Trinomial expansion: `[X^m](b + aX + bX²)^j = Σ_u C(j,u) C(j−u, m−2u) a^{m−2u} b^{j−m+u}`
(`u` up steps, `m − 2u` stays). -/
theorem coeff_pathPoly_pow {R : Type*} [CommRing R] (a b : R) (j m : ℕ) :
    ((pathPoly a b) ^ j).coeff m =
      ∑ u ∈ range (j + 1), if 2 * u ≤ m ∧ m - 2 * u ≤ j - u then
        b ^ u * a ^ (m - 2 * u) * b ^ (j - u - (m - 2 * u)) *
          ((j.choose u : R) * ((j - u).choose (m - 2 * u) : R)) else 0 := by
  have hP : pathPoly a b = C b * X ^ 2 + (C a * X + C b) := by unfold pathPoly; ring
  rw [hP, add_pow, finsetSum_coeff]
  refine sum_congr rfl fun u hu => ?_
  rw [add_pow, mul_sum, sum_mul, finsetSum_coeff]
  have key : ∀ v ∈ range (j - u + 1),
      ((C b * X ^ 2) ^ u * ((C a * X) ^ v * C b ^ (j - u - v) * ((j - u).choose v : R[X])) *
        (j.choose u : R[X])).coeff m =
      if v = m - 2 * u ∧ 2 * u ≤ m then
        b ^ u * a ^ v * b ^ (j - u - v) * ((j.choose u : R) * ((j - u).choose v : R)) else 0 := by
    intro v _
    have : (C b * X ^ 2) ^ u * ((C a * X) ^ v * C b ^ (j - u - v) * ((j - u).choose v : R[X])) *
        (j.choose u : R[X]) =
        C (b ^ u * a ^ v * b ^ (j - u - v) * ((j.choose u : R) * ((j - u).choose v : R))) *
          X ^ (2 * u + v) := by
      simp only [C_mul, C_pow, ← map_natCast C]; ring
    rw [this, coeff_C_mul_X_pow]
    split_ifs <;> first | rfl | omega
  rw [sum_congr rfl key]
  by_cases h : 2 * u ≤ m
  · simp only [h, and_true, true_and]
    rw [sum_ite_eq' (range (j - u + 1)) (m - 2 * u)]
    simp only [mem_range]
    split_ifs <;> first | rfl | omega
  · simp [h]

section Field

variable {K : Type*} [Field K] [CharZero K]

/-- `H_j(a,b) = Σ_k j!/(k!²(j−2k)!) a^{j−2k} b^{2k}` (JZC_SHIFT §2.2), summed over `2k ≤ j`. -/
noncomputable def pathH (j : ℕ) (a b : K) : K :=
  ∑ k ∈ range (j + 1), if 2 * k ≤ j then
    (j.factorial : K) / ((k.factorial : K) ^ 2 * ((j - 2 * k).factorial : K)) *
      a ^ (j - 2 * k) * b ^ (2 * k) else 0

/-- `G_j(a,b) = b·Σ_k j!/((k+1)!k!(j−2k−1)!) a^{j−2k−1} b^{2k+1}` (JZC_SHIFT §2.2), summed over
`2k + 1 ≤ j`. -/
noncomputable def pathG (j : ℕ) (a b : K) : K :=
  b * ∑ k ∈ range (j + 1), if 2 * k + 1 ≤ j then
    (j.factorial : K) / (((k + 1).factorial : K) * (k.factorial : K) *
      ((j - 2 * k - 1).factorial : K)) * a ^ (j - 2 * k - 1) * b ^ (2 * k + 1) else 0

/-- `H_j(a,b)` is the `X^j`-coefficient of `(b + aX + bX²)^j`. -/
theorem pathH_eq_coeff (j : ℕ) (a b : K) : pathH j a b = ((pathPoly a b) ^ j).coeff j := by
  rw [coeff_pathPoly_pow, pathH]
  refine sum_congr rfl fun u _ => ?_
  by_cases h : 2 * u ≤ j
  · rw [ite_eq_left h, ite_eq_left ⟨h, by omega⟩]
    have e1 : j - u - (j - 2 * u) = u := by omega
    have e2 : j - u - (j - 2 * u) = u := by omega
    rw [e1, Nat.cast_choose K (by omega : u ≤ j), Nat.cast_choose K (by omega : j - 2 * u ≤ j - u), e2]
    have : ((j - u).factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    have : ((j - 2 * u).factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    have : (u.factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    field_simp
    ring
  · rw [ite_eq_right h, ite_eq_right (by omega)]

/-- `G_j(a,b)` is `b` times the `X^{j+1}`-coefficient of `(b + aX + bX²)^j`. -/
theorem pathG_eq_coeff (j : ℕ) (a b : K) :
    pathG j a b = b * ((pathPoly a b) ^ j).coeff (j + 1) := by
  rw [coeff_pathPoly_pow, pathG, sum_range_succ, sum_range_succ' _ j]
  rw [ite_eq_right (by omega), ite_eq_right (by omega), add_zero, add_zero]
  congr 1
  refine sum_congr rfl fun k _ => ?_
  by_cases h : 2 * k + 1 ≤ j
  · rw [ite_eq_left h, ite_eq_left ⟨by omega, by omega⟩]
    have e0 : j + 1 - 2 * (k + 1) = j - 2 * k - 1 := by omega
    have e1 : j - (k + 1) - (j - 2 * k - 1) = k := by omega
    rw [e0, e1, Nat.cast_choose K (by omega : k + 1 ≤ j),
      Nat.cast_choose K (by omega : j - 2 * k - 1 ≤ j - (k + 1)), e1]
    have : ((j - (k + 1)).factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    have : ((j - 2 * k - 1).factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    have : (k.factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    have : ((k + 1).factorial : K) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
    field_simp
    ring
  · rw [ite_eq_right h, ite_eq_right (by omega)]

omit [CharZero K] in
/-- On the hard-edge line `a = 2b`: `b + 2bX + bX² = b(1+X)²`. -/
theorem coeff_pathPoly_two_mul_pow (j m : ℕ) (b : K) :
    ((pathPoly (2 * b) b) ^ j).coeff m = b ^ j * ((2 * j).choose m : K) := by
  have : pathPoly (2 * b) b ^ j = C (b ^ j) * (1 + X) ^ (2 * j) := by
    unfold pathPoly
    rw [C_pow, pow_mul, ← mul_pow, map_mul, map_ofNat]
    ring
  rw [this, coeff_C_mul, coeff_one_add_X_pow]

/-- **Lemma R** (JZC_SHIFT §2.3), first identity: `H_j(2b, b) = C(2j, j) b^j`. -/
theorem pathH_two_mul (j : ℕ) (b : K) : pathH j (2 * b) b = ((2 * j).choose j : K) * b ^ j := by
  rw [pathH_eq_coeff, coeff_pathPoly_two_mul_pow, mul_comm]

/-- **Lemma R** (JZC_SHIFT §2.3), second identity, binomial form:
`G_j(2b, b) = C(2j, j+1) b^{j+1}`. -/
theorem pathG_two_mul' (j : ℕ) (b : K) :
    pathG j (2 * b) b = ((2 * j).choose (j + 1) : K) * b ^ (j + 1) := by
  rw [pathG_eq_coeff, coeff_pathPoly_two_mul_pow]; ring

/-- `C(2j, j+1) = C(2j, j)·j/(j+1)`. -/
theorem choose_two_mul_succ_eq (j : ℕ) :
    ((2 * j).choose (j + 1) : K) = ((2 * j).choose j : K) * (j / (j + 1)) := by
  have h := Nat.choose_succ_right_eq (2 * j) j
  have h' : ((2 * j).choose (j + 1) : K) * (j + 1) = ((2 * j).choose j : K) * j := by
    have : 2 * j - j = j := by omega
    rw [this] at h
    exact_mod_cast h
  have : (j : K) + 1 ≠ 0 := Nat.cast_add_one_ne_zero j
  field_simp
  linear_combination h'

/-- **Lemma R** (JZC_SHIFT §2.3), second identity as stated there:
`G_j(2b, b) = C(2j, j)(j/(j+1)) b^{j+1}`. -/
theorem pathG_two_mul (j : ℕ) (b : K) :
    pathG j (2 * b) b = ((2 * j).choose j : K) * (j / (j + 1)) * b ^ (j + 1) := by
  rw [pathG_two_mul', choose_two_mul_succ_eq]

end Field

/-- **Lemma R** consequence (JZC_SHIFT §2.3), as a derivative identity in `b` along the line
`a = 2b`: `d/db G_j(2b, b) = b · d/db H_j(2b, b)` (both equal `j C(2j,j) b^j`). This is the
one-variable shadow of `∂_n G_j(2b,b) = b ∂_n H_j(2b,b)` (chain rule with `b = b(n)`). -/
theorem deriv_pathG_two_mul (j : ℕ) (b : ℝ) :
    deriv (fun x : ℝ => pathG j (2 * x) x) b =
      b * deriv (fun x : ℝ => pathH j (2 * x) x) b := by
  have hG : (fun x : ℝ => pathG j (2 * x) x) =
      fun x => ((2 * j).choose (j + 1) : ℝ) * x ^ (j + 1) := funext (pathG_two_mul' j)
  have hH : (fun x : ℝ => pathH j (2 * x) x) =
      fun x => ((2 * j).choose j : ℝ) * x ^ j := funext (pathH_two_mul j)
  rw [hG, hH, ((hasDerivAt_pow (j + 1) b).const_mul _).deriv, ((hasDerivAt_pow j b).const_mul _).deriv]
  have h := Nat.choose_succ_right_eq (2 * j) j
  have : 2 * j - j = j := by omega
  rw [this] at h
  have h' : ((2 * j).choose (j + 1) : ℝ) * (j + 1) = ((2 * j).choose j : ℝ) * j := by
    exact_mod_cast h
  rcases Nat.eq_zero_or_pos j with rfl | hj
  · simp
  · obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
    simp only [Nat.add_sub_cancel, Nat.cast_add, Nat.cast_one] at h' ⊢
    rw [pow_succ]
    linear_combination b ^ i * b * h'

section Laurent

open LaurentPolynomial

variable {K : Type*} [Field K] [CharZero K]

/-- The constant-coefficient (free) Jacobi operator as a Laurent polynomial in the shift `T`:
`J = a + b T + b T⁻¹` (stays weighted `a`, up/down steps weighted `b`). -/
noncomputable def freeJacobi (a b : K) : K[T;T⁻¹] :=
  LaurentPolynomial.C a + LaurentPolynomial.C b * T 1 + LaurentPolynomial.C b * T (-1)

omit [CharZero K] in
theorem freeJacobi_eq (a b : K) : freeJacobi a b = toLaurent (pathPoly a b) * T (-1) := by
  unfold freeJacobi pathPoly
  simp only [map_add, map_mul, Polynomial.toLaurent_C, Polynomial.toLaurent_X,
    Polynomial.toLaurent_X_pow, add_mul, mul_assoc, ← T_add]
  norm_num [T_zero]
  ring

omit [CharZero K] in
theorem freeJacobi_pow_coeff (a b : K) (j m : ℕ) :
    ((freeJacobi a b) ^ j).coeff ((m : ℤ) - j) = ((pathPoly a b) ^ j).coeff m := by
  rw [freeJacobi_eq, mul_pow, T_pow, ← map_pow]
  have : ((m : ℤ) - j) = (m : ℤ) + (j * -1 : ℤ) := by ring
  rw [this, T, AddMonoidAlgebra.coeff_mul_single_add, mul_one, coeff_toLaurent]
  exact Finsupp.mapDomain_apply_of_injective Nat.castEmbedding.injective _ m

/-- `H_j(a,b)` is the constant coefficient of `J^j`, i.e. the path count `(J^j)_{nn}` of the
constant-coefficient Jacobi matrix (JZC_SHIFT §2.2: "path counts of `(J^j)_{nn}`"). -/
theorem freeJacobi_pow_coeff_zero (a b : K) (j : ℕ) :
    ((freeJacobi a b) ^ j).coeff 0 = pathH j a b := by
  rw [pathH_eq_coeff, ← freeJacobi_pow_coeff]; simp

/-- `G_j(a,b) = b · [T¹] J^j`, i.e. `b (J^j)_{n+1,n}` of the constant-coefficient Jacobi matrix
(JZC_SHIFT §2.2). -/
theorem freeJacobi_pow_coeff_one (a b : K) (j : ℕ) :
    b * ((freeJacobi a b) ^ j).coeff 1 = pathG j a b := by
  rw [pathG_eq_coeff, ← freeJacobi_pow_coeff]; push_cast; ring_nf

end Laurent

/-- Natural-number core of Paper IV eq. `eq:Qk`:
`2 Σ_{j ≤ k} C(2j,j) 4^{k−j} = (k+1) C(2k+2, k+1)`. -/
theorem two_mul_sum_centralBinom_four_pow (k : ℕ) :
    2 * ∑ j ∈ range (k + 1), Nat.centralBinom j * 4 ^ (k - j) =
      (k + 1) * Nat.centralBinom (k + 1) := by
  induction k with
  | zero => simp [Nat.centralBinom_eq_two_mul_choose]
  | succ k ih =>
    rw [sum_range_succ, Nat.sub_self, pow_zero, mul_one]
    have : ∑ j ∈ range (k + 1), Nat.centralBinom j * 4 ^ (k + 1 - j) =
        4 * ∑ j ∈ range (k + 1), Nat.centralBinom j * 4 ^ (k - j) := by
      rw [mul_sum]
      refine sum_congr rfl fun j hj => ?_
      have : k + 1 - j = (k - j) + 1 := by rw [mem_range] at hj; omega
      rw [this, pow_succ]; ring
    rw [this, Nat.succ_mul_centralBinom_succ (k + 1)]
    have h2 := Nat.succ_mul_centralBinom_succ k
    nlinarith [ih, h2]

/-- `Q_k(z) = Σ_{j=0}^{k−1} C(2j, j) c^j z^{k−1−j}` (Paper IV `p2_frame.tex`, eq. `eq:Qk`). -/
noncomputable def tiltQ (c z : ℝ) (k : ℕ) : ℝ :=
  ∑ j ∈ range k, ((2 * j).choose j : ℝ) * c ^ j * z ^ (k - 1 - j)

/-- Paper IV eq. `eq:Qk`: `Q_k(4c) = ½ c^{k−1} k C(2k, k)` for `k ≥ 1`, any real `c`. -/
theorem tiltQ_four_mul (c : ℝ) {k : ℕ} (hk : 1 ≤ k) :
    tiltQ c (4 * c) k = 1 / 2 * c ^ (k - 1) * k * ((2 * k).choose k : ℝ) := by
  obtain ⟨n, rfl⟩ : ∃ n, k = n + 1 := ⟨k - 1, by omega⟩
  have h := two_mul_sum_centralBinom_four_pow n
  have hR : (2 : ℝ) * ∑ j ∈ range (n + 1), (Nat.centralBinom j : ℝ) * 4 ^ (n - j) =
      (n + 1) * Nat.centralBinom (n + 1) := by exact_mod_cast h
  unfold tiltQ
  simp only [Nat.add_sub_cancel, ← Nat.centralBinom_eq_two_mul_choose]
  have : ∑ j ∈ range (n + 1), (Nat.centralBinom j : ℝ) * c ^ j * (4 * c) ^ (n - j) =
      c ^ n * ∑ j ∈ range (n + 1), (Nat.centralBinom j : ℝ) * 4 ^ (n - j) := by
    rw [mul_sum]
    refine sum_congr rfl fun j hj => ?_
    have hjn : j + (n - j) = n := by rw [mem_range] at hj; omega
    rw [mul_pow]
    calc (Nat.centralBinom j : ℝ) * c ^ j * (4 ^ (n - j) * c ^ (n - j))
        = (Nat.centralBinom j : ℝ) * 4 ^ (n - j) * (c ^ j * c ^ (n - j)) := by ring
      _ = c ^ n * ((Nat.centralBinom j : ℝ) * 4 ^ (n - j)) := by rw [← pow_add, hjn]; ring
  rw [this]
  push_cast
  linear_combination c ^ n / 2 * hR

/-- The resonance weight `W(j) = C(2j, j) c^j` (research/G1/RH/second_order/E3.md Cor. E3.3,
JZC_SHIFT §2.3–2.4: `V_j(c) = (j C(2j,j)/2) c^j`). -/
noncomputable def resW (c : ℝ) (j : ℕ) : ℝ := ((2 * j).choose j : ℝ) * c ^ j

/-- `C(2j+2, j+1)(j+1) = 2(2j+1) C(2j, j)` (Mathlib `Nat.succ_mul_centralBinom_succ`). -/
theorem choose_succ_mul (j : ℕ) :
    (2 * (j + 1)).choose (j + 1) * (j + 1) = 2 * (2 * j + 1) * (2 * j).choose j := by
  have := Nat.succ_mul_centralBinom_succ j
  simp only [Nat.centralBinom_eq_two_mul_choose] at this
  linarith

/-- Ratio recursion of the resonance weight: `(j+1) W(j+1) = 2(2j+1) c W(j)`. -/
theorem resW_succ (c : ℝ) (j : ℕ) :
    (j + 1) * resW c (j + 1) = 2 * (2 * j + 1) * c * resW c j := by
  have h : (((2 * (j + 1)).choose (j + 1) : ℕ) : ℝ) * (j + 1) =
      2 * (2 * j + 1) * ((2 * j).choose j : ℝ) := by exact_mod_cast choose_succ_mul j
  unfold resW
  rw [pow_succ]
  linear_combination c ^ j * c * h

/-- `C(2j, j+1)(j+1) = C(2j, j) j`, the identity behind `G_j(2b,b) = C(2j,j)(j/(j+1)) b^{j+1}`. -/
theorem choose_two_mul_succ_mul (j : ℕ) :
    (2 * j).choose (j + 1) * (j + 1) = (2 * j).choose j * j := by
  have h := Nat.choose_succ_right_eq (2 * j) j
  rwa [show 2 * j - j = j by omega] at h

end JacobiAsym
