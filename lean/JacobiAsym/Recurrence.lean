import JacobiAsym.OrthoPoly

open Finset Matrix Polynomial

namespace JacobiAsym

/-- `b_k² = D_{k+1} D_{k-1} / D_k²` (`k ≥ 1`). -/
noncomputable def jb2 (x w : ℕ → ℝ) (k : ℕ) : ℝ :=
  (hankel x w (k + 1)).det * (hankel x w (k - 1)).det / (hankel x w k).det ^ 2

/-- `a_k = ⟨X P_k, P_k⟩ / ⟨P_k, P_k⟩`. -/
noncomputable def ja (x w : ℕ → ℝ) (k : ℕ) : ℝ :=
  dip x w (X * opoly x w k) (opoly x w k) / dip x w (opoly x w k) (opoly x w k)

/-- `P_k` is orthogonal to every polynomial whose coefficients vanish from degree `k` on. -/
theorem dip_opoly_of_coeff {x w : ℕ → ℝ} (h : DMeasure x w) {k : ℕ} {q : ℝ[X]}
    (hq : ∀ i, k ≤ i → q.coeff i = 0) : dip x w (opoly x w k) q = 0 := by
  rw [dip_comm, q.as_sum_range_C_mul_X_pow, dip_sum_left h]
  apply sum_eq_zero; intro i _
  rw [dip_smul_left, dip_comm]
  rcases lt_or_ge i k with hik | hik
  · rw [dip_opoly_pow h hik, mul_zero]
  · rw [hq i hik, zero_mul]

/-- A polynomial orthogonal to all `X^i` (`i < k`) and to `P_k`, of degree `≤ k`, is zero. -/
theorem eq_zero_of_orth {x w : ℕ → ℝ} (h : DMeasure x w) {k : ℕ} {R : ℝ[X]}
    (hdeg : ∀ i, k < i → R.coeff i = 0) (hlow : ∀ i, i < k → dip x w R (X ^ i) = 0)
    (htop : dip x w R (opoly x w k) = 0) : R = 0 := by
  apply dip_self_eq_zero h
  set c := R.coeff k
  have hS : ∀ i, k ≤ i → (R - C c * opoly x w k).coeff i = 0 := by
    intro i hi
    rw [coeff_sub, coeff_C_mul]
    rcases eq_or_lt_of_le hi with heq | hlt
    · subst heq
      have : (opoly x w k).coeff k = 1 := by
        have := (opoly_monic h k).coeff_natDegree; rwa [opoly_natDegree h] at this
      rw [this]; ring
    · rw [hdeg i hlt, coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; exact hlt)]; ring
  have hsplit : R = C c * opoly x w k + (R - C c * opoly x w k) := by ring
  -- dip R R = c ⟨R, P_k⟩ + ⟨R, rest⟩, and rest is a combination of X^i, i < k
  have hrest : dip x w R (R - C c * opoly x w k) = 0 := by
    rw [dip_comm, (R - C c * opoly x w k).as_sum_range_C_mul_X_pow, dip_sum_left h]
    apply sum_eq_zero; intro i _
    rw [dip_smul_left, dip_comm]
    rcases lt_or_ge i k with hik | hik
    · rw [hlow i hik, mul_zero]
    · rw [hS i hik, zero_mul]
  calc dip x w R R = dip x w (C c * opoly x w k + (R - C c * opoly x w k)) R := by congr 1
    _ = c * dip x w (opoly x w k) R + dip x w (R - C c * opoly x w k) R := by
        rw [dip_add_left h, dip_smul_left]
    _ = 0 := by
        rw [dip_comm x w (opoly x w k) R, htop, dip_comm x w (R - C c * opoly x w k) R, hrest]
        ring

theorem dip_opoly_self {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) :
    dip x w (opoly x w k) (opoly x w k) = (hankel x w (k + 1)).det / (hankel x w k).det := by
  have hrest : dip x w (opoly x w k) (opoly x w k - X ^ k) = 0 := by
    apply dip_opoly_of_coeff h
    intro i hi
    rw [coeff_sub, coeff_X_pow]
    rcases eq_or_lt_of_le hi with heq | hlt
    · subst heq
      have := (opoly_monic h k).coeff_natDegree; rw [opoly_natDegree h] at this; rw [this]; simp
    · rw [coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; exact hlt), if_neg (by omega)]; ring
  calc dip x w (opoly x w k) (opoly x w k) = dip x w (X ^ k + (opoly x w k - X ^ k)) (opoly x w k) := by
        congr 1; ring
    _ = dip x w (opoly x w k) (X ^ k) + dip x w (opoly x w k) (opoly x w k - X ^ k) := by
        rw [dip_add_left h, dip_comm x w (X ^ k), dip_comm x w (opoly x w k - X ^ k)]
    _ = _ := by rw [hrest, add_zero, dip_opoly_pow_self h]

theorem jb2_pos {x w : ℕ → ℝ} (h : DMeasure x w) (k : ℕ) : 0 < jb2 x w k := by
  unfold jb2
  have := hankel_det_pos h (k + 1); have := hankel_det_pos h (k - 1); have := hankel_det_pos h k
  positivity

/-- **Three-term recurrence** (item 11 §1 convention: monic `P_k`, `b_k²` the squared off-diagonal). -/
theorem opoly_recurrence {x w : ℕ → ℝ} (h : DMeasure x w) {k : ℕ} (hk : 1 ≤ k) :
    X * opoly x w k = opoly x w (k + 1) + C (ja x w k) * opoly x w k + C (jb2 x w k) * opoly x w (k - 1) := by
  have hDk := hankel_det_pos h k
  have hDk1 := hankel_det_pos h (k + 1)
  have hDkm := hankel_det_pos h (k - 1)
  have hPP : 0 < dip x w (opoly x w k) (opoly x w k) := by rw [dip_opoly_self h]; positivity
  set R := X * opoly x w k - opoly x w (k + 1) - C (ja x w k) * opoly x w k - C (jb2 x w k) * opoly x w (k - 1)
    with hR
  -- degree: coefficients above k vanish
  have hdeg : ∀ i, k < i → R.coeff i = 0 := by
    intro i hi
    simp only [hR, coeff_sub, coeff_C_mul, coeff_X_mul_zero, coeff_X_mul]
    have hk1 : (opoly x w (k + 1)).coeff i = if i = k + 1 then 1 else 0 := by
      split_ifs with hik
      · subst hik; have := (opoly_monic h (k + 1)).coeff_natDegree; rwa [opoly_natDegree h] at this
      · exact coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega)
    have hk : (opoly x w k).coeff i = 0 := coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega)
    have hkm : (opoly x w (k - 1)).coeff i = 0 := coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega)
    rw [hk1, hk, hkm]
    obtain ⟨j, rfl⟩ : ∃ j, i = j + 1 := ⟨i - 1, by omega⟩
    rw [coeff_X_mul]
    rcases eq_or_lt_of_le (Nat.succ_le_of_lt hi) with hj | hj
    · have hjk : j = k := by omega
      subst hjk
      have := (opoly_monic h j).coeff_natDegree; rw [opoly_natDegree h] at this
      rw [this, if_pos rfl]; ring
    · rw [coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega), if_neg (by omega)]; ring
  -- low powers
  have hlow : ∀ i, i < k → dip x w R (X ^ i) = 0 := by
    intro i hi
    simp only [hR]
    rw [show X * opoly x w k - opoly x w (k + 1) - C (ja x w k) * opoly x w k - C (jb2 x w k) * opoly x w (k - 1)
        = X * opoly x w k + (C (-1) * opoly x w (k + 1) + (C (-(ja x w k)) * opoly x w k +
          C (-(jb2 x w k)) * opoly x w (k - 1))) by simp only [map_neg, map_one]; ring]
    rw [dip_add_left h, dip_add_left h, dip_add_left h, dip_smul_left, dip_smul_left, dip_smul_left,
      dip_X_mul, ← pow_succ', dip_opoly_pow h (by omega : i < k + 1), dip_opoly_pow h hi]
    rcases lt_or_eq_of_le (Nat.le_sub_one_of_lt hi) with hlt | heq
    · rw [dip_opoly_pow h (by omega : i + 1 < k), dip_opoly_pow h hlt]; ring
    · subst heq
      have hk1 : k - 1 + 1 = k := by omega
      rw [hk1, dip_opoly_pow_self h, dip_opoly_pow_self h, hk1]
      unfold jb2
      field_simp
      ring
  -- top: orthogonal to P_k by definition of a_k
  have htop : dip x w R (opoly x w k) = 0 := by
    simp only [hR]
    rw [show X * opoly x w k - opoly x w (k + 1) - C (ja x w k) * opoly x w k - C (jb2 x w k) * opoly x w (k - 1)
        = X * opoly x w k + (C (-1) * opoly x w (k + 1) + (C (-(ja x w k)) * opoly x w k +
          C (-(jb2 x w k)) * opoly x w (k - 1))) by simp only [map_neg, map_one]; ring]
    rw [dip_add_left h, dip_add_left h, dip_add_left h, dip_smul_left, dip_smul_left, dip_smul_left]
    have h1 : dip x w (opoly x w (k + 1)) (opoly x w k) = 0 :=
      dip_opoly_of_coeff h (fun i hi => coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega))
    have h2 : dip x w (opoly x w (k - 1)) (opoly x w k) = 0 := by
      rw [dip_comm]
      exact dip_opoly_of_coeff h (fun i hi => coeff_eq_zero_of_natDegree_lt (by rw [opoly_natDegree h]; omega))
    rw [h1, h2]
    unfold ja
    field_simp
    ring
  have hR0 := eq_zero_of_orth h hdeg hlow htop
  rw [hR] at hR0
  linear_combination hR0

end JacobiAsym
