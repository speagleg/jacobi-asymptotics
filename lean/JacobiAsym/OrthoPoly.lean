import JacobiAsym.DiscreteMeasure

open Finset Matrix Polynomial

namespace JacobiAsym

/-- The `(k+1) × (k+1)` matrix: rows `i < k` are moments `m_{i+j}`, the last row is `1, X, …, X^k`. -/
noncomputable def opolyMat (x w : ℕ → ℝ) (k : ℕ) : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ[X] :=
  Matrix.of fun i j => if (i : ℕ) < k then C (mom x w ((i : ℕ) + j)) else (X : ℝ[X]) ^ (j : ℕ)

/-- Monic orthogonal polynomial of degree `k`. -/
noncomputable def opoly (x w : ℕ → ℝ) (k : ℕ) : ℝ[X] := C ((hankel x w k).det)⁻¹ * (opolyMat x w k).det

/-- The real `k × k` minor obtained by deleting the last row and column `j` (moment rows only). -/
noncomputable def opolyCof (x w : ℕ → ℝ) (k : ℕ) (j : Fin (k + 1)) : ℝ :=
  (Matrix.of fun (i l : Fin k) => mom x w ((i : ℕ) + (j.succAbove l : ℕ))).det

/-- Real matrix with moment rows `i < k` and an arbitrary last row `r`. -/
noncomputable def rowMat (x w : ℕ → ℝ) (k : ℕ) (r : Fin (k + 1) → ℝ) : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ :=
  Matrix.of fun i j => if (i : ℕ) < k then mom x w ((i : ℕ) + j) else r j

theorem rowMat_det_eq (x w : ℕ → ℝ) (k : ℕ) (r : Fin (k + 1) → ℝ) :
    (rowMat x w k r).det = ∑ j : Fin (k + 1), (-1) ^ (k + (j : ℕ)) * r j * opolyCof x w k j := by
  rw [det_succ_row _ (Fin.last k)]
  apply sum_congr rfl; intro j _
  simp only [rowMat, of_apply, Fin.val_last, lt_irrefl, ite_false]
  congr 2
  ext i l
  simp [Fin.succAbove_last, i.2]

theorem opolyMat_det_eq (x w : ℕ → ℝ) (k : ℕ) :
    (opolyMat x w k).det = ∑ j : Fin (k + 1), C ((-1) ^ (k + (j : ℕ)) * opolyCof x w k j) * X ^ (j : ℕ) := by
  rw [det_succ_row _ (Fin.last k)]
  apply sum_congr rfl; intro j _
  have hsub : (opolyMat x w k).submatrix (Fin.last k).succAbove j.succAbove =
      (Matrix.of fun (i l : Fin k) => mom x w ((i : ℕ) + (j.succAbove l : ℕ))).map C := by
    ext i l
    simp [opolyMat, Fin.succAbove_last, i.2]
  have hlast : opolyMat x w k (Fin.last k) j = X ^ (j : ℕ) := by simp [opolyMat]
  rw [hsub, hlast]
  rw [show ((Matrix.of fun (i l : Fin k) => mom x w ((i : ℕ) + (j.succAbove l : ℕ))).map C).det =
      C (Matrix.of fun (i l : Fin k) => mom x w ((i : ℕ) + (j.succAbove l : ℕ))).det from
      (RingHom.map_det C _).symm]
  unfold opolyCof
  simp only [Fin.val_last]
  simp only [map_mul, map_pow, map_neg, map_one]
  ring

/-- Pairing the determinant polynomial with `q` replaces the last row by `⟨X^j, q⟩`. -/
theorem dip_opolyMat_det {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) (q : ℝ[X]) :
    dip x w (opolyMat x w k).det q = (rowMat x w k (fun j => dip x w (X ^ (j : ℕ)) q)).det := by
  rw [opolyMat_det_eq, dip_sum_left h, rowMat_det_eq]
  apply sum_congr rfl; intro j _
  rw [dip_smul_left]; ring

theorem opoly_zero (x w : ℕ → ℝ) : opoly x w 0 = 1 := by
  have h0 : (hankel x w 0).det = 1 := det_isEmpty
  have h1 : (opolyMat x w 0).det = 1 := by
    rw [Matrix.det_fin_one]; simp [opolyMat]
  unfold opoly; rw [h0, h1]; simp

theorem dip_opoly_pow {x w : ℕ → ℝ} (h : DMeasure x w) {k j : ℕ} (hj : j < k) :
    dip x w (opoly x w k) (X ^ j) = 0 := by
  unfold opoly
  rw [dip_smul_left, dip_opolyMat_det h]
  have hrow : rowMat x w k (fun l => dip x w (X ^ (l : ℕ)) (X ^ j)) ⟨j, by omega⟩ =
      rowMat x w k (fun l => dip x w (X ^ (l : ℕ)) (X ^ j)) (Fin.last k) := by
    funext l
    simp [rowMat, hj, dip_pow_pow, add_comm]
  rw [det_zero_of_row_eq (by simp [Fin.ext_iff]; omega) hrow, mul_zero]

theorem dip_opoly_pow_self {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) :
    dip x w (opoly x w k) (X ^ k) = (hankel x w (k + 1)).det / (hankel x w k).det := by
  unfold opoly
  rw [dip_smul_left, dip_opolyMat_det h]
  have hmat : rowMat x w k (fun l => dip x w (X ^ (l : ℕ)) (X ^ k)) = hankel x w (k + 1) := by
    ext i l
    rw [hankel_eq_mom]
    simp only [rowMat, of_apply, dip_pow_pow]
    split_ifs with hi
    · rfl
    · have : (i : ℕ) = k := by omega
      rw [this, add_comm]
  rw [hmat, div_eq_inv_mul]

/-- Explicit expansion of `opoly` in monomials. -/
theorem opoly_eq_sum (x w : ℕ → ℝ) (k : ℕ) :
    opoly x w k = ∑ j : Fin (k + 1),
      C (((hankel x w k).det)⁻¹ * ((-1) ^ (k + (j : ℕ)) * opolyCof x w k j)) * X ^ (j : ℕ) := by
  unfold opoly
  rw [opolyMat_det_eq, mul_sum]
  apply sum_congr rfl; intro j _
  simp only [map_mul]; ring

theorem opolyCof_last (x w : ℕ → ℝ) (k : ℕ) : opolyCof x w k (Fin.last k) = (hankel x w k).det := by
  unfold opolyCof
  congr 1
  ext i l
  simp [hankel_eq_mom, Fin.succAbove_last]

theorem opoly_natDegree_le (x w : ℕ → ℝ) (k : ℕ) : (opoly x w k).natDegree ≤ k := by
  rw [opoly_eq_sum]
  apply natDegree_sum_le_of_forall_le
  intro j _
  exact (natDegree_C_mul_X_pow_le _ _).trans (by have := j.2; omega)

theorem opoly_coeff_self {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : (opoly x w k).coeff k = 1 := by
  rw [opoly_eq_sum, finsetSum_coeff]
  rw [Finset.sum_eq_single (Fin.last k)]
  · rw [coeff_C_mul_X_pow, if_pos (by simp), opolyCof_last, Fin.val_last, ← two_mul, pow_mul]
    simp only [neg_one_sq, one_pow, one_mul]
    exact inv_mul_cancel₀ (hankel_det_pos h k).ne'
  · intro j _ hj
    rw [coeff_C_mul_X_pow, if_neg]
    intro hk; apply hj; ext; simp [hk]
  · intro hn; exact absurd (mem_univ _) hn

theorem opoly_monic {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : (opoly x w k).Monic :=
  monic_of_natDegree_le_of_coeff_eq_one k (opoly_natDegree_le x w k) (opoly_coeff_self h k)

theorem opoly_natDegree {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : (opoly x w k).natDegree = k :=
  natDegree_eq_of_le_of_coeff_ne_zero (opoly_natDegree_le x w k) (by rw [opoly_coeff_self h k]; norm_num)

end JacobiAsym
