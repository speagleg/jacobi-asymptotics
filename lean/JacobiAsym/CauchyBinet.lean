import Mathlib

open Finset Matrix

namespace JacobiAsym

/-- Expansion: `det (A * B) = ∑_f det(A[·, f]) ∏_i B (f i) i`. -/
theorem det_mul_expand {n K : ℕ} (A : Matrix (Fin n) (Fin K) ℝ) (B : Matrix (Fin K) (Fin n) ℝ) :
    (A * B).det = ∑ f : Fin n → Fin K, (A.submatrix id f).det * ∏ i, B (f i) i := by
  simp only [det_apply', mul_apply, Finset.prod_univ_sum, Finset.mul_sum, Fintype.piFinset_univ]
  rw [Finset.sum_comm]
  apply sum_congr rfl; intro f _
  rw [sum_mul]; apply sum_congr rfl; intro σ _
  simp only [submatrix_apply, id]
  rw [prod_mul_distrib]; ring

/-- Non-injective column selections give zero. -/
theorem det_submatrix_of_not_injective {n K : ℕ} (A : Matrix (Fin n) (Fin K) ℝ) {f : Fin n → Fin K}
    (hf : ¬ Function.Injective f) : (A.submatrix id f).det = 0 := by
  simp only [Function.Injective, not_forall] at hf
  obtain ⟨i, j, hij, hne⟩ := hf
  exact det_zero_of_column_eq hne (fun k => by simp [hij])

/-- Cauchy–Binet for `A : n × K`, `B : K × n` over ℝ: sum over `n`-subsets `S` of the columns, enumerated
increasingly by `S.orderEmbOfFin`. -/
theorem det_mul_cauchyBinet {n K : ℕ} (A : Matrix (Fin n) (Fin K) ℝ) (B : Matrix (Fin K) (Fin n) ℝ) :
    (A * B).det = ∑ S : {S : Finset (Fin K) // S.card = n},
      (A.submatrix id (S.1.orderEmbOfFin S.2)).det * (B.submatrix (S.1.orderEmbOfFin S.2) id).det := by
  classical
  set F : (Fin n → Fin K) → ℝ := fun f => (A.submatrix id f).det * ∏ i, B (f i) i with hF
  rw [det_mul_expand]
  -- restrict to injective f
  have h1 : ∑ f : Fin n → Fin K, F f = ∑ f ∈ univ.filter (fun f : Fin n → Fin K => Function.Injective f), F f := by
    rw [sum_filter]
    apply sum_congr rfl; intro f _
    split_ifs with hf
    · rfl
    · simp [hF, det_submatrix_of_not_injective A hf]
  rw [h1]
  -- reindex injective f by (S, τ)
  have h2 : ∑ f ∈ univ.filter (fun f : Fin n → Fin K => Function.Injective f), F f =
      ∑ q : {S : Finset (Fin K) // S.card = n} × Equiv.Perm (Fin n),
        F (fun i => q.1.1.orderEmbOfFin q.1.2 (q.2 i)) := by
    symm
    apply Finset.sum_bij (fun q _ => fun i => q.1.1.orderEmbOfFin q.1.2 (q.2 i))
    · intro q _
      simp only [mem_filter, mem_univ, true_and]
      exact (q.1.1.orderEmbOfFin q.1.2).injective.comp q.2.injective
    · rintro ⟨⟨S, hS⟩, τ⟩ _ ⟨⟨S', hS'⟩, τ'⟩ _ heq
      have hrange : (S : Set (Fin K)) = S' := by
        have r1 : Set.range (fun i => S.orderEmbOfFin hS (τ i)) = S := by
          rw [Set.range_comp' (S.orderEmbOfFin hS) τ, τ.surjective.range_eq, Set.image_univ, range_orderEmbOfFin]
        have r2 : Set.range (fun i => S'.orderEmbOfFin hS' (τ' i)) = S' := by
          rw [Set.range_comp' (S'.orderEmbOfFin hS') τ', τ'.surjective.range_eq, Set.image_univ, range_orderEmbOfFin]
        rw [← r1, ← r2, heq]
      have hSS : S = S' := Finset.coe_inj.1 hrange
      subst hSS
      have hττ : τ = τ' := by
        ext i
        have := congrFun heq i
        exact congrArg Fin.val ((S.orderEmbOfFin hS).injective this)
      subst hττ
      rfl
    · intro f hf
      simp only [mem_filter, mem_univ, true_and] at hf
      set S := univ.image f with hSdef
      have hS : S.card = n := by rw [hSdef, card_image_of_injective _ hf]; simp
      set g : Fin n → Fin n := fun i => (S.orderIsoOfFin hS).symm ⟨f i, by simp [hSdef]⟩ with hg
      have hginj : Function.Injective g := by
        intro i j hij
        have := congrArg (fun z => ((S.orderIsoOfFin hS) z : Fin K)) hij
        simp only [hg, OrderIso.apply_symm_apply] at this
        exact hf this
      have hgbij : Function.Bijective g := Finite.injective_iff_bijective.1 hginj
      refine ⟨(⟨S, hS⟩, Equiv.ofBijective g hgbij), mem_univ _, ?_⟩
      funext i
      simp only [Equiv.ofBijective_apply, hg]
      rw [← coe_orderIsoOfFin_apply, OrderIso.apply_symm_apply]
    · intro q _; rfl
  rw [h2, Fintype.sum_prod_type]
  apply sum_congr rfl; intro S _
  -- inner sum over τ
  have hdet : ∀ τ : Equiv.Perm (Fin n),
      (A.submatrix id (fun i => S.1.orderEmbOfFin S.2 (τ i))).det =
        Equiv.Perm.sign τ * (A.submatrix id (S.1.orderEmbOfFin S.2)).det := by
    intro τ
    have := det_permute' τ (A.submatrix id (S.1.orderEmbOfFin S.2))
    simpa [Matrix.submatrix_submatrix, Function.comp_def] using this
  simp only [hF, hdet]
  rw [det_apply' (B.submatrix (S.1.orderEmbOfFin S.2) id), mul_sum]
  apply sum_congr rfl; intro τ _
  simp only [submatrix_apply, id]
  ring

end JacobiAsym
