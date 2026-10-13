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

/-- Each `λ_i` (`1 ≤ i ≤ ℓ`) is a root of the characteristic polynomial. -/
theorem toeplitz_isRoot {ℓ i : ℕ} (A B : ℝ) (hi1 : 1 ≤ i) (hiℓ : i ≤ ℓ) :
    (toeplitzTri ℓ A B).charpoly.IsRoot (toepEig ℓ A B i) := by
  rw [IsRoot, eval_charpoly, ← exists_mulVec_eq_zero_iff]
  refine ⟨toepVec ℓ i, toepVec_ne_zero hi1 hiℓ, ?_⟩
  rw [sub_mulVec, toeplitz_eigen]
  funext k
  simp [Matrix.scalar_apply]

/-- For `B > 0`, `i ↦ λ_i` is injective on `[1, ℓ]` (cos is injective on `[0, π]`). -/
theorem toepEig_injOn (ℓ : ℕ) (A B : ℝ) (hB : 0 < B) : Set.InjOn (toepEig ℓ A B) (Icc 1 ℓ) := by
  intro i hi i' hi' h
  simp only [coe_Icc, Set.mem_Icc] at hi hi'
  have hc : Real.cos (Real.pi * i / (ℓ + 1)) = Real.cos (Real.pi * i' / (ℓ + 1)) := by
    unfold toepEig at h
    have h2 : 2 * B * Real.cos (Real.pi * i / (ℓ + 1)) = 2 * B * Real.cos (Real.pi * i' / (ℓ + 1)) := by linarith
    exact mul_left_cancel₀ (by positivity) h2
  have hmem : ∀ m : ℕ, m ≤ ℓ → Real.pi * m / (ℓ + 1) ∈ Set.Icc 0 Real.pi := by
    intro m hm
    have hml : (m : ℝ) ≤ ℓ := by exact_mod_cast hm
    refine ⟨by positivity, ?_⟩
    rw [div_le_iff₀ (by positivity)]
    nlinarith [Real.pi_pos]
  have ha := Real.injOn_cos (hmem i hi.2) (hmem i' hi'.2) hc
  have : (i : ℝ) = i' := by
    have hp : (0 : ℝ) < Real.pi / (ℓ + 1) := by positivity
    have : Real.pi / (ℓ + 1) * i = Real.pi / (ℓ + 1) * i' := by
      rw [div_mul_eq_mul_div, div_mul_eq_mul_div, mul_comm _ (i : ℝ), mul_comm _ (i' : ℝ),
        mul_comm (i : ℝ), mul_comm (i' : ℝ)]; exact ha
    exact mul_left_cancel₀ hp.ne' this
  exact_mod_cast this

theorem toeplitz_charpoly_roots (ℓ : ℕ) (A B : ℝ) (hB : 0 < B) :
    (toeplitzTri ℓ A B).charpoly.roots = ((Icc 1 ℓ).image (toepEig ℓ A B)).val := by
  set S := (Icc 1 ℓ).image (toepEig ℓ A B)
  have hmon := charpoly_monic (toeplitzTri ℓ A B)
  have hle : S.val ≤ (toeplitzTri ℓ A B).charpoly.roots := by
    rw [Multiset.le_iff_subset S.nodup]
    intro x hx
    obtain ⟨i, hi, rfl⟩ := mem_image.1 (show x ∈ S from hx)
    rw [mem_Icc] at hi
    exact (mem_roots hmon.ne_zero).2 (toeplitz_isRoot A B hi.1 hi.2)
  have hcardS : S.card = ℓ := by
    rw [card_image_of_injOn (toepEig_injOn ℓ A B hB), Nat.card_Icc]; omega
  have hcard : Multiset.card (toeplitzTri ℓ A B).charpoly.roots ≤ Multiset.card S.val := by
    calc Multiset.card (toeplitzTri ℓ A B).charpoly.roots ≤ (toeplitzTri ℓ A B).charpoly.natDegree :=
          card_roots' _
      _ = Multiset.card S.val := by rw [charpoly_natDegree_eq_dim, Fintype.card_fin, card_val, hcardS]
  exact (Multiset.eq_of_le_of_card_le hle hcard).symm

theorem toeplitz_eigCount (ℓ : ℕ) (A B μ : ℝ) (hB : 0 < B) :
    eigCount (toeplitzTri ℓ A B) μ = ((Icc 1 ℓ).filter (fun i => μ < toepEig ℓ A B i)).card := by
  unfold eigCount
  rw [toeplitz_charpoly_roots ℓ A B hB, ← filter_val, card_val, filter_image,
    card_image_of_injOn ((toepEig_injOn ℓ A B hB).mono (by intro i hi; exact (mem_filter.1 hi).1))]

theorem toeplitz_eigCount_zero (ℓ : ℕ) (A μ : ℝ) :
    eigCount (toeplitzTri ℓ A 0) μ = if μ < A then ℓ else 0 := by
  have hT : toeplitzTri ℓ A 0 = diagonal (fun _ => A) := by
    ext i j
    simp only [toeplitzTri, of_apply, diagonal_apply]
    split_ifs <;> rfl
  unfold eigCount
  rw [hT, charpoly_diagonal, prod_const, card_univ, Fintype.card_fin, roots_pow, roots_X_sub_C,
    Multiset.nsmul_singleton]
  split_ifs with h
  · rw [Multiset.filter_eq_self.2 (fun a ha => by rw [Multiset.eq_of_mem_replicate ha]; exact h),
      Multiset.card_replicate]
  · rw [Multiset.filter_eq_nil.2 (fun a ha => by rw [Multiset.eq_of_mem_replicate ha]; exact h)]
    rfl

/-- Weyl angle `θ = arccos(clip((μ - A)/(2B)))`, with `θ = π·1{μ < A}` when `B = 0`. -/
noncomputable def weylAngle (A B μ : ℝ) : ℝ :=
  if B = 0 then (if μ < A then Real.pi else 0) else Real.arccos (max (-1) (min 1 ((μ - A) / (2 * B))))

/-- Counting lemma: `#{i ∈ [1, ℓ] : s < cos(π i/(ℓ+1))}` is within 1 of `ℓ · arccos(clip s)/π`. -/
theorem cos_count (ℓ : ℕ) (s : ℝ) :
    |(((Icc 1 ℓ).filter (fun i : ℕ => s < Real.cos (Real.pi * i / (ℓ + 1)))).card : ℝ) -
      ℓ / Real.pi * Real.arccos (max (-1) (min 1 s))| ≤ 1 := by
  set c := max (-1) (min 1 s) with hc
  have hc1 : -1 ≤ c := le_max_left _ _
  have hc2 : c ≤ 1 := max_le (by norm_num) (min_le_left _ _)
  set θ := Real.arccos c with hθ
  have hθ0 : 0 ≤ θ := Real.arccos_nonneg c
  have hθπ : θ ≤ Real.pi := Real.arccos_le_pi c
  have hN : (0 : ℝ) < ℓ + 1 := by positivity
  set y := θ * (ℓ + 1) / Real.pi with hy
  have hy0 : 0 ≤ y := by positivity
  have hyN : y ≤ ((ℓ + 1 : ℕ) : ℝ) := by
    rw [hy, div_le_iff₀ Real.pi_pos]; push_cast; nlinarith
  set m := ⌈y⌉₊ with hm
  have hmN : m ≤ ℓ + 1 := Nat.ceil_le.2 hyN
  have hpred : ∀ i ∈ Icc 1 ℓ, (s < Real.cos (Real.pi * i / (ℓ + 1)) ↔ i < m) := by
    intro i hi
    rw [mem_Icc] at hi
    have hi1 : (1 : ℝ) ≤ i := by exact_mod_cast hi.1
    have hil : (i : ℝ) ≤ ℓ := by exact_mod_cast hi.2
    set φ := Real.pi * i / (ℓ + 1) with hφ
    have hφ0 : 0 < φ := by positivity
    have hφπ : φ < Real.pi := by rw [hφ, div_lt_iff₀ hN]; nlinarith [Real.pi_pos]
    have hφmem : φ ∈ Set.Icc 0 Real.pi := ⟨hφ0.le, hφπ.le⟩
    have hcos1 : Real.cos φ < 1 := by
      have := Real.strictAntiOn_cos ⟨le_refl 0, Real.pi_pos.le⟩ hφmem hφ0
      rwa [Real.cos_zero] at this
    have hcosm1 : -1 < Real.cos φ := by
      have := Real.strictAntiOn_cos hφmem ⟨Real.pi_pos.le, le_refl _⟩ hφπ
      rwa [Real.cos_pi] at this
    have h1 : s < Real.cos φ ↔ c < Real.cos φ := by
      rcases le_or_gt 1 s with hs | hs
      · have : c = 1 := by rw [hc, min_eq_left hs]; norm_num
        rw [this]; constructor <;> intro h <;> linarith
      rcases lt_or_ge s (-1) with hs' | hs'
      · have : c = -1 := by rw [hc, min_eq_right hs.le]; exact max_eq_left hs'.le
        rw [this]; constructor <;> intro _ <;> linarith
      · have : c = s := by rw [hc, min_eq_right hs.le]; exact max_eq_right hs'
        rw [this]
    have h2 : c < Real.cos φ ↔ φ < θ := by
      have hcc := Real.cos_arccos hc1 hc2
      rw [← hθ] at hcc
      conv_lhs => rw [← hcc]
      exact Real.strictAntiOn_cos.lt_iff_gt ⟨hθ0, hθπ⟩ hφmem
    have h3 : φ < θ ↔ (i : ℝ) < y := by
      rw [hφ, hy, div_lt_iff₀ hN, lt_div_iff₀ Real.pi_pos]
      constructor <;> intro h <;> linarith
    rw [h1, h2, h3, Nat.lt_ceil]
  rw [filter_congr hpred]
  have hset : (Icc 1 ℓ).filter (fun i => i < m) = Ico 1 m := by
    ext i; simp only [mem_filter, mem_Icc, mem_Ico]; omega
  rw [hset, Nat.card_Ico]
  have hey : (ℓ : ℝ) / Real.pi * θ = y - θ / Real.pi := by
    rw [hy]; field_simp; ring
  have ht1 : θ / Real.pi ≤ 1 := by rw [div_le_one Real.pi_pos]; exact hθπ
  have ht0 : 0 ≤ θ / Real.pi := by positivity
  rw [hey, abs_le]
  rcases Nat.eq_zero_or_pos m with h0 | hpos
  · have : y ≤ 0 := Nat.ceil_eq_zero.1 h0
    rw [h0]; simp only [Nat.zero_sub, Nat.cast_zero]
    constructor <;> linarith
  · have hle : y ≤ m := Nat.le_ceil y
    have hlt : (m : ℝ) < y + 1 := Nat.ceil_lt_add_one hy0
    rw [Nat.cast_sub hpos]; push_cast
    constructor <;> linarith

/-- **Item 11 (S4)**: `|N(T_ℓ(A,B); μ) - (ℓ/π) θ| ≤ 1`. -/
theorem toeplitz_count (ℓ : ℕ) (A B μ : ℝ) (hB : 0 ≤ B) :
    |(eigCount (toeplitzTri ℓ A B) μ : ℝ) - ℓ / Real.pi * weylAngle A B μ| ≤ 1 := by
  rcases eq_or_lt_of_le hB with h0 | hpos
  · subst h0
    rw [toeplitz_eigCount_zero]
    unfold weylAngle
    simp only [↓reduceIte]
    split_ifs
    · rw [div_mul_cancel₀ _ Real.pi_ne_zero, sub_self, abs_zero]; norm_num
    · simp
  · rw [toeplitz_eigCount ℓ A B μ hpos]
    unfold weylAngle
    simp only [hpos.ne', ↓reduceIte]
    have hf : (Icc 1 ℓ).filter (fun i => μ < toepEig ℓ A B i) =
        (Icc 1 ℓ).filter (fun i : ℕ => (μ - A) / (2 * B) < Real.cos (Real.pi * i / (ℓ + 1))) := by
      apply filter_congr
      intro i _
      unfold toepEig
      rw [div_lt_iff₀ (by positivity)]
      constructor <;> intro h <;> linarith
    rw [hf]
    exact cos_count ℓ _

end JacobiAsym
