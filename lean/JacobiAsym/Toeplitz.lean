import JacobiAsym.Basic

open Finset Matrix Polynomial

namespace JacobiAsym

/-- `ℓ × ℓ` tridiagonal Toeplitz matrix: diagonal `A`, off-diagonals `B`. -/
noncomputable def toeplitzTri (ℓ : ℕ) (A B : ℝ) : Matrix (Fin ℓ) (Fin ℓ) ℝ :=
  Matrix.of fun i j => if i = j then A else if (i : ℕ) + 1 = j ∨ (j : ℕ) + 1 = i then B else 0

/-- `λ_i = A + 2B cos(π i/(ℓ+1))`. -/
noncomputable def toepEig (ℓ : ℕ) (A B : ℝ) (i : ℕ) : ℝ := A + 2 * B * Real.cos (Real.pi * i / (ℓ + 1))

/-- Sine eigenvector `v_i(j) = sin(π i (j+1)/(ℓ+1))`. -/
noncomputable def toepVec (ℓ : ℕ) (i : ℕ) : Fin ℓ → ℝ := fun j => Real.sin (Real.pi * i * ((j : ℝ) + 1) / (ℓ + 1))

/-- Summing a Kronecker delta over `Fin ℓ`. -/
theorem sum_fin_delta (ℓ c : ℕ) (h : ℕ → ℝ) :
    ∑ k : Fin ℓ, (if c = (k : ℕ) then h k else 0) = if c < ℓ then h c else 0 := by
  rw [Fin.sum_univ_eq_sum_range (fun k => if c = k then h k else 0) ℓ, sum_ite_eq]
  simp only [mem_range]

theorem toeplitz_eigen (ℓ : ℕ) (A B : ℝ) (i : ℕ) :
    toeplitzTri ℓ A B *ᵥ toepVec ℓ i = toepEig ℓ A B i • toepVec ℓ i := by
  funext j
  set a := Real.pi * i / (ℓ + 1) with ha
  set g : ℕ → ℝ := fun m => Real.sin (a * m) with hg
  have hv : ∀ k : Fin ℓ, toepVec ℓ i k = g ((k : ℕ) + 1) := by
    intro k; simp only [toepVec, hg, ha]; push_cast; ring_nf
  have hg0 : g 0 = 0 := by simp [hg]
  have hgl : g (ℓ + 1) = 0 := by
    simp only [hg, ha]; push_cast
    rw [show Real.pi * i / ((ℓ : ℝ) + 1) * ((ℓ : ℝ) + 1) = i * Real.pi by field_simp]
    exact Real.sin_nat_mul_pi i
  have hcoef : ∀ k : Fin ℓ, toeplitzTri ℓ A B j k = A * (if (j : ℕ) = k then 1 else 0) +
      B * (if (j : ℕ) + 1 = k then 1 else 0) + B * (if (j : ℕ) = (k : ℕ) + 1 then 1 else 0) := by
    intro k
    simp only [toeplitzTri, of_apply, Fin.ext_iff]
    split_ifs <;> first | (exfalso; omega) | simp
  -- the two off-diagonal neighbours, with boundary values supplied by `g 0 = g (ℓ+1) = 0`
  have hup : ∑ k : Fin ℓ, (if (j : ℕ) + 1 = k then g ((k : ℕ) + 1) else 0) = g ((j : ℕ) + 2) := by
    rw [sum_fin_delta ℓ ((j : ℕ) + 1) (fun k => g (k + 1))]
    split_ifs with hj
    · rfl
    · have : (j : ℕ) + 1 = ℓ := by omega
      simp only [show (j : ℕ) + 2 = ℓ + 1 by omega, hgl]
  have hdn : ∑ k : Fin ℓ, (if (j : ℕ) = (k : ℕ) + 1 then g ((k : ℕ) + 1) else 0) = g (j : ℕ) := by
    rcases Nat.eq_zero_or_eq_succ_pred (j : ℕ) with h0 | hs
    · rw [h0, hg0]; apply sum_eq_zero; intro k _; split_ifs <;> first | (exfalso; omega) | rfl
    · have hc : ∀ k : Fin ℓ, ((j : ℕ) = (k : ℕ) + 1) ↔ ((j : ℕ) - 1 = k) := fun k => by omega
      simp_rw [hc]
      rw [sum_fin_delta ℓ ((j : ℕ) - 1) (fun k => g (k + 1))]
      split_ifs
      · congr 1; omega
      · exfalso; omega
  have hmid : ∑ k : Fin ℓ, (if (j : ℕ) = k then g ((k : ℕ) + 1) else 0) = g ((j : ℕ) + 1) := by
    rw [sum_fin_delta ℓ (j : ℕ) (fun k => g (k + 1))]; simp [j.2]
  rw [mulVec, dotProduct]
  simp only [hcoef, hv, add_mul, sum_add_distrib, mul_assoc, ite_mul, one_mul, zero_mul]
  rw [← mul_sum, ← mul_sum, ← mul_sum, hmid, hup, hdn]
  simp only [Pi.smul_apply, smul_eq_mul, toepEig, hv]
  -- sin(a j) + sin(a (j+2)) = 2 cos a sin(a (j+1))
  have htrig : g (j : ℕ) + g ((j : ℕ) + 2) = 2 * Real.cos a * g ((j : ℕ) + 1) := by
    simp only [hg]; push_cast
    rw [show a * (j : ℝ) = a * ((j : ℝ) + 1) - a by ring, show a * ((j : ℝ) + 2) = a * ((j : ℝ) + 1) + a by ring,
      Real.sin_sub, Real.sin_add]
    ring
  rw [← ha]
  linear_combination B * htrig

theorem toepVec_ne_zero {ℓ i : ℕ} (hi1 : 1 ≤ i) (hiℓ : i ≤ ℓ) : toepVec ℓ i ≠ 0 := by
  intro h0
  have hℓ : 0 < ℓ := by omega
  have h := congrFun h0 ⟨0, hℓ⟩
  simp only [toepVec, Nat.cast_zero, zero_add, mul_one, Pi.zero_apply] at h
  have hi : (1 : ℝ) ≤ i := by exact_mod_cast hi1
  have hil : (i : ℝ) ≤ ℓ := by exact_mod_cast hiℓ
  have hpos : 0 < Real.sin (Real.pi * i / (ℓ + 1)) := by
    apply Real.sin_pos_of_pos_of_lt_pi
    · positivity
    · rw [div_lt_iff₀ (by positivity)]
      nlinarith [Real.pi_pos]
  linarith

/-- Number of eigenvalues `> μ` **counted as roots of the characteristic polynomial, with multiplicity**.
For real symmetric matrices (all eigenvalues real) this is the spectral count `N(M; μ)` of item 11 (S3). -/
noncomputable def eigCount {ℓ : ℕ} (M : Matrix (Fin ℓ) (Fin ℓ) ℝ) (μ : ℝ) : ℕ :=
  (M.charpoly.roots.filter (fun t => μ < t)).card

end JacobiAsym
