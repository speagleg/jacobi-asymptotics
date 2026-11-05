import JacobiAsym.H2

/-!
# Lemma U (Uvarov / one-atom perturbation of Hankel determinants)

Source: `research/G1/RH/spectral/SPEC.md` §3.2, Lemma U. For `σ = σ′ + w₀ δ_{x₀}` and
`F(m) = log D_m(σ) − log D_m(σ′)`:
* `H_m(σ) = H_m(σ′) + w₀ v vᵀ`, `v = (x₀^i)_{i<m}`, so by the matrix determinant lemma
  `D_m(σ) = D_m(σ′) (1 + w₀ vᵀ H_m(σ′)⁻¹ v)` (`det_momHankel_add_atom`, `hankel_det_add_atom`);
* `vᵀ H_m(σ′)⁻¹ v = Σ_{j<m} p′_j(x₀)² = K′_{m−1}(x₀,x₀)` (`hankelQuad_eq_kernel`);
* `F(m) = log(1 + w₀ K′_{m−1}(x₀,x₀))` (`logDetDiff_add_atom`, `logDetDiff_add_atom_kernel`);
* `log b_n²(σ) − log b_n²(σ′) = F(n+1) − 2F(n) + F(n−1)` (`log_jb2_sub`).
-/

open Finset Matrix Polynomial

namespace JacobiAsym

/-- Hankel matrix `(μ_{i+j})_{i,j<n}` of an arbitrary moment sequence `μ`. -/
def momHankel (μ : ℕ → ℝ) (n : ℕ) : Matrix (Fin n) (Fin n) ℝ := Matrix.of fun i j => μ ((i : ℕ) + j)

/-- The moment vector `v = (x₀^i)_{i<n}`. -/
def powVec (x₀ : ℝ) (n : ℕ) : Fin n → ℝ := fun i => x₀ ^ (i : ℕ)

/-- `vᵀ H_n(μ)⁻¹ v`, `v = (x₀^i)_{i<n}`. -/
noncomputable def hankelQuad (μ : ℕ → ℝ) (x₀ : ℝ) (n : ℕ) : ℝ :=
  powVec x₀ n ⬝ᵥ ((momHankel μ n)⁻¹ *ᵥ powVec x₀ n)

theorem hankel_eq_momHankel (x w : ℕ → ℝ) (n : ℕ) : hankel x w n = momHankel (mom x w) n := rfl

/-- Rank-one update: `H_n(μ + w₀ x₀^·) = H_n(μ) + w₀ v vᵀ`. -/
theorem momHankel_add_atom (μ : ℕ → ℝ) (w₀ x₀ : ℝ) (n : ℕ) :
    momHankel (fun k => μ k + w₀ * x₀ ^ k) n =
      momHankel μ n + replicateCol (Fin 1) (w₀ • powVec x₀ n) * replicateRow (Fin 1) (powVec x₀ n) := by
  ext i j
  simp [momHankel, powVec, Matrix.mul_apply, pow_add]

/-- **Matrix determinant lemma for a Hankel matrix plus one atom** (SPEC §3.2 Lemma U, proof):
for any moment sequence `μ` with `det H_n(μ) ≠ 0`,
`det H_n(μ + w₀ x₀^·) = det H_n(μ) · (1 + w₀ vᵀ H_n(μ)⁻¹ v)`. -/
theorem det_momHankel_add_atom (μ : ℕ → ℝ) (w₀ x₀ : ℝ) (n : ℕ) (hdet : (momHankel μ n).det ≠ 0) :
    (momHankel (fun k => μ k + w₀ * x₀ ^ k) n).det =
      (momHankel μ n).det * (1 + w₀ * hankelQuad μ x₀ n) := by
  have key := det_add_replicateCol_mul_replicateRow (ι := Fin 1) (A := momHankel μ n)
    (isUnit_iff_ne_zero.2 hdet) (w₀ • powVec x₀ n) (powVec x₀ n)
  rw [momHankel_add_atom]
  refine (Eq.trans (by congr) key).trans ?_
  simp only [Matrix.det_unique]
  congr 1
  simp only [hankelQuad, Matrix.add_apply, Matrix.one_apply_eq, Matrix.mul_apply, replicateRow_apply,
    replicateCol_apply, dotProduct, mulVec, Pi.smul_apply, smul_eq_mul, Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_comm]
  congr 1
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  ring

/-- `F(m) = log D_m(σ) − log D_m(σ′)` for `σ = (x, w)`, `σ′ = (x', w')`. -/
noncomputable def logDetDiff (x w x' w' : ℕ → ℝ) (m : ℕ) : ℝ :=
  Real.log (hankel x w m).det - Real.log (hankel x' w' m).det

theorem log_jb2_eq (x w : ℕ → ℝ) (hD : ∀ m, 0 < (hankel x w m).det) (n : ℕ) :
    Real.log (jb2 x w n) = Real.log (hankel x w (n + 1)).det - 2 * Real.log (hankel x w n).det +
      Real.log (hankel x w (n - 1)).det := by
  unfold jb2
  have h1 := hD (n + 1); have h2 := hD (n - 1); have h3 := hD n
  rw [Real.log_div (by positivity) (by positivity), Real.log_mul h1.ne' h2.ne', Real.log_pow]
  push_cast; ring

/-- SPEC §3.2 Lemma U, second part: `log b_n²(σ) − log b_n²(σ′) = F(n+1) − 2F(n) + F(n−1)`
for any two moment data with positive Hankel determinants (library convention
`jb2 n = D_{n+1} D_{n−1} / D_n²`, natural subtraction; at `n = 0` both sides use `D_{0−1} = D_0`). -/
theorem log_jb2_sub (x w x' w' : ℕ → ℝ) (hD : ∀ m, 0 < (hankel x w m).det)
    (hD' : ∀ m, 0 < (hankel x' w' m).det) (n : ℕ) :
    Real.log (jb2 x w n) - Real.log (jb2 x' w' n) =
      logDetDiff x w x' w' (n + 1) - 2 * logDetDiff x w x' w' n + logDetDiff x w x' w' (n - 1) := by
  rw [log_jb2_eq x w hD, log_jb2_eq x' w' hD']
  unfold logDetDiff; ring

theorem log_jb2_sub_of_DMeasure {x w x' w' : ℕ → ℝ} (hσ : DMeasure x w) (hσ' : DMeasure x' w') (n : ℕ) :
    Real.log (jb2 x w n) - Real.log (jb2 x' w' n) =
      logDetDiff x w x' w' (n + 1) - 2 * logDetDiff x w x' w' n + logDetDiff x w x' w' (n - 1) :=
  log_jb2_sub x w x' w' (hankel_det_pos hσ) (hankel_det_pos hσ') n

/-- SPEC §3.2 Lemma U, atom level: if `σ = σ′ + w₀ δ_{x₀}` at the level of moments,
`m_k(σ) = m_k(σ′) + w₀ x₀^k`, then `D_m(σ) = D_m(σ′) (1 + w₀ vᵀ H_m(σ′)⁻¹ v)`. -/
theorem hankel_det_add_atom {x w x' w' : ℕ → ℝ} (hσ' : DMeasure x' w') {w₀ x₀ : ℝ}
    (hmom : ∀ k, mom x w k = mom x' w' k + w₀ * x₀ ^ k) (m : ℕ) :
    (hankel x w m).det = (hankel x' w' m).det * (1 + w₀ * hankelQuad (mom x' w') x₀ m) := by
  rw [hankel_eq_momHankel, hankel_eq_momHankel, show mom x w = fun k => mom x' w' k + w₀ * x₀ ^ k from
    funext hmom]
  exact det_momHankel_add_atom _ _ _ _ (hankel_det_pos hσ' m).ne'

/-- SPEC §3.2 Lemma U, first part: `F(m) = log(1 + w₀ vᵀ H_m(σ′)⁻¹ v)`. -/
theorem logDetDiff_add_atom {x w x' w' : ℕ → ℝ} (hσ : DMeasure x w) (hσ' : DMeasure x' w') {w₀ x₀ : ℝ}
    (hmom : ∀ k, mom x w k = mom x' w' k + w₀ * x₀ ^ k) (m : ℕ) :
    logDetDiff x w x' w' m = Real.log (1 + w₀ * hankelQuad (mom x' w') x₀ m) := by
  have h' := hankel_det_pos hσ' m
  have hq : 0 < 1 + w₀ * hankelQuad (mom x' w') x₀ m := by
    have := hankel_det_pos hσ m
    rw [hankel_det_add_atom hσ' hmom] at this
    exact pos_of_mul_pos_right this h'.le
  unfold logDetDiff
  rw [hankel_det_add_atom hσ' hmom, Real.log_mul h'.ne' hq.ne']; ring

/-! ### `vᵀ H⁻¹ v` as the Christoffel–Darboux kernel -/

/-- Coefficient matrix of the monic OPs: row `j` holds the coefficients of `P_j`. -/
noncomputable def opolyCoeffMat (x w : ℕ → ℝ) (m : ℕ) : Matrix (Fin m) (Fin m) ℝ :=
  Matrix.of fun j i => (opoly x w j).coeff i

theorem opolyCoeffMat_mulVec (x w : ℕ → ℝ) (m : ℕ) (x₀ : ℝ) :
    opolyCoeffMat x w m *ᵥ powVec x₀ m = fun j : Fin m => (opoly x w j).eval x₀ := by
  funext j
  have hdeg : (opoly x w j).natDegree < m := (opoly_natDegree_le x w j).trans_lt j.2
  rw [eval_eq_sum_range' hdeg]
  simp only [mulVec, dotProduct, opolyCoeffMat, of_apply, powVec]
  exact Fin.sum_univ_eq_sum_range (fun i => (opoly x w j).coeff i * x₀ ^ i) m

theorem opolyCoeffMat_det {x w : ℕ → ℝ} (h : DMeasure x w) (m : ℕ) : (opolyCoeffMat x w m).det = 1 := by
  rw [det_of_isLowerTriangular]
  · refine Finset.prod_eq_one fun j _ => ?_
    exact opoly_coeff_self h j
  · intro i j hij
    simp only [opolyCoeffMat, of_apply]
    refine coeff_eq_zero_of_natDegree_lt ((opoly_natDegree_le x w i).trans_lt ?_)
    exact hij

theorem dip_eq_coeff_sum {x w : ℕ → ℝ} (h : DMeasure x w) {m : ℕ} {p q : Polynomial ℝ}
    (hp : p.natDegree < m) (hq : q.natDegree < m) :
    dip x w p q = ∑ a : Fin m, ∑ b : Fin m, p.coeff a * mom x w ((a : ℕ) + b) * q.coeff b := by
  conv_lhs => rw [p.as_sum_range' m hp]
  simp only [← C_mul_X_pow_eq_monomial]
  rw [dip_sum_left h, ← Fin.sum_univ_eq_sum_range (fun a => dip x w (Polynomial.C (p.coeff a) *
    Polynomial.X ^ a) q)]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [dip_smul_left, dip_comm]
  conv_lhs => rw [q.as_sum_range' m hq]
  simp only [← C_mul_X_pow_eq_monomial]
  rw [dip_sum_left h,
    ← Fin.sum_univ_eq_sum_range (fun b => dip x w (Polynomial.C (q.coeff b) * Polynomial.X ^ b)
      (Polynomial.X ^ (a : ℕ))), Finset.mul_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [dip_smul_left, dip_pow_pow, add_comm (b : ℕ)]; ring

theorem dip_opoly_opoly {x w : ℕ → ℝ} (h : DMeasure x w) (j k : ℕ) :
    dip x w (opoly x w j) (opoly x w k) = if j = k then dip x w (opoly x w j) (opoly x w j) else 0 := by
  split_ifs with hjk
  · rw [hjk]
  · rcases lt_or_gt_of_ne hjk with hlt | hlt
    · rw [dip_comm]
      exact dip_opoly_of_coeff h fun i hi => coeff_eq_zero_of_natDegree_lt
        ((opoly_natDegree_le x w j).trans_lt (hlt.trans_le hi))
    · exact dip_opoly_of_coeff h fun i hi => coeff_eq_zero_of_natDegree_lt
        ((opoly_natDegree_le x w k).trans_lt (hlt.trans_le hi))

/-- `C H_m Cᵀ = diag(⟨P_j, P_j⟩)` (orthogonality of the monic OPs). -/
theorem opolyCoeffMat_hankel {x w : ℕ → ℝ} (h : DMeasure x w) (m : ℕ) :
    opolyCoeffMat x w m * hankel x w m * (opolyCoeffMat x w m)ᵀ =
      diagonal fun j : Fin m => dip x w (opoly x w j) (opoly x w j) := by
  ext j k
  have hj : (opoly x w j).natDegree < m := (opoly_natDegree_le x w j).trans_lt j.2
  have hk : (opoly x w k).natDegree < m := (opoly_natDegree_le x w k).trans_lt k.2
  have e := dip_eq_coeff_sum h hj hk
  rw [dip_opoly_opoly h] at e
  have e' : (if j = k then dip x w (opoly x w j) (opoly x w j) else 0) =
      ∑ a : Fin m, ∑ b : Fin m, (opoly x w j).coeff a * mom x w ((a : ℕ) + b) * (opoly x w k).coeff b := by
    rw [← e]; simp only [Fin.val_inj]
  rw [diagonal_apply, e']
  simp only [Matrix.mul_apply, transpose_apply, opolyCoeffMat, of_apply, hankel_eq_mom, Finset.sum_mul]
  rw [Finset.sum_comm]

/-- `H_m⁻¹ = Cᵀ diag(⟨P_j,P_j⟩⁻¹) C`. -/
theorem hankel_inv_eq {x w : ℕ → ℝ} (h : DMeasure x w) (m : ℕ) :
    (hankel x w m)⁻¹ = (opolyCoeffMat x w m)ᵀ *
      (diagonal fun j : Fin m => dip x w (opoly x w j) (opoly x w j))⁻¹ * opolyCoeffMat x w m := by
  have hC : IsUnit (opolyCoeffMat x w m).det := by rw [opolyCoeffMat_det h]; exact isUnit_one
  have hCt : IsUnit (opolyCoeffMat x w m)ᵀ.det := by rw [det_transpose]; exact hC
  rw [← opolyCoeffMat_hankel h m, Matrix.mul_inv_rev, Matrix.mul_inv_rev]
  rw [show ∀ A B D E : Matrix (Fin m) (Fin m) ℝ, A * (B * (D * E)) * (opolyCoeffMat x w m) =
      (A * B) * D * (E * opolyCoeffMat x w m) from fun A B D E => by simp only [Matrix.mul_assoc]]
  rw [mul_nonsing_inv _ hCt, nonsing_inv_mul _ hC, Matrix.one_mul, Matrix.mul_one]

/-- SPEC §3.2 Lemma U, kernel identity: `vᵀ H_m(σ)⁻¹ v = Σ_{j<m} p_j(x₀)² = K_{m−1}(x₀,x₀)`,
with `p_j = P_j / ‖P_j‖` the orthonormal polynomials (`P_j = opoly`, `‖P_j‖² = ⟨P_j, P_j⟩`). -/
theorem dip_opoly_self_pos {x w : ℕ → ℝ} (h : DMeasure x w) (j : ℕ) :
    0 < dip x w (opoly x w j) (opoly x w j) := by
  rw [dip_opoly_self h]; exact div_pos (hankel_det_pos h _) (hankel_det_pos h _)

theorem inv_diagonal_opoly {x w : ℕ → ℝ} (h : DMeasure x w) (m : ℕ) :
    (diagonal fun j : Fin m => dip x w (opoly x w j) (opoly x w j))⁻¹ =
      diagonal fun j : Fin m => (dip x w (opoly x w j) (opoly x w j))⁻¹ := by
  refine inv_eq_left_inv ?_
  rw [diagonal_mul_diagonal, ← diagonal_one]
  congr 1; funext j
  exact inv_mul_cancel₀ (dip_opoly_self_pos h j).ne'

theorem hankelQuad_eq_kernel {x w : ℕ → ℝ} (h : DMeasure x w) (m : ℕ) (x₀ : ℝ) :
    hankelQuad (mom x w) x₀ m =
      ∑ j ∈ range m, (opoly x w j).eval x₀ ^ 2 / dip x w (opoly x w j) (opoly x w j) := by
  unfold hankelQuad
  rw [← hankel_eq_momHankel, hankel_inv_eq h, ← mulVec_mulVec, ← mulVec_mulVec, dotProduct_mulVec,
    vecMul_transpose, opolyCoeffMat_mulVec, inv_diagonal_opoly h]
  rw [← Fin.sum_univ_eq_sum_range (fun j => (opoly x w j).eval x₀ ^ 2 / dip x w (opoly x w j) (opoly x w j))]
  simp only [dotProduct, mulVec_diagonal]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [div_eq_mul_inv]; ring

/-- Lemma U assembled: `F(m) = log(1 + w₀ Σ_{j<m} p′_j(x₀)²)` for `σ = σ′ + w₀ δ_{x₀}` (moment level). -/
theorem logDetDiff_add_atom_kernel {x w x' w' : ℕ → ℝ} (hσ : DMeasure x w) (hσ' : DMeasure x' w')
    {w₀ x₀ : ℝ} (hmom : ∀ k, mom x w k = mom x' w' k + w₀ * x₀ ^ k) (m : ℕ) :
    logDetDiff x w x' w' m = Real.log (1 + w₀ *
      ∑ j ∈ range m, (opoly x' w' j).eval x₀ ^ 2 / dip x' w' (opoly x' w' j) (opoly x' w' j)) := by
  rw [logDetDiff_add_atom hσ hσ' hmom, hankelQuad_eq_kernel hσ']

end JacobiAsym
