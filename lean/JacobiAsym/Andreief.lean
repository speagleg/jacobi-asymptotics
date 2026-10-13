import JacobiAsym.CauchyBinet
import JacobiAsym.Heine

open Finset Matrix

namespace JacobiAsym

/-- Truncated Hankel moment matrix `(∑_{k<K} w k x k^(i+j))_{i,j<n}`. -/
noncomputable def hankelK (x w : ℕ → ℝ) (K n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun i j => ∑ k ∈ range K, w k * x k ^ ((i : ℕ) + j)

/-- `heineTerm` on the image of a strictly increasing `g : Fin n → ℕ`. -/
theorem heineTerm_map_strictMono (x w : ℕ → ℝ) {n : ℕ} (g : Fin n → ℕ) (hg : StrictMono g) :
    heineTerm x w (univ.map ⟨g, hg.injective⟩) =
      (∏ i, w (g i)) * ∏ i, ∏ j ∈ Ioi i, (x (g j) - x (g i)) ^ 2 := by
  unfold heineTerm
  congr 1
  · rw [prod_map]; rfl
  · have hpairs : pairs (univ.map ⟨g, hg.injective⟩) =
        ((univ : Finset (Fin n × Fin n)).filter (fun q => q.1 < q.2)).map
          ⟨fun q => (g q.1, g q.2), fun q r h =>
            Prod.ext (hg.injective (congrArg Prod.fst h)) (hg.injective (congrArg Prod.snd h))⟩ := by
      ext ⟨a, b⟩
      simp only [pairs, mem_filter, mem_product, mem_map, mem_univ, true_and, Function.Embedding.coeFn_mk]
      constructor
      · rintro ⟨⟨⟨i, rfl⟩, ⟨j, rfl⟩⟩, hab⟩
        exact ⟨(i, j), hg.lt_iff_lt.1 hab, rfl⟩
      · rintro ⟨⟨i, j⟩, hij, h⟩
        have h1 : g i = a := congrArg Prod.fst h
        have h2 : g j = b := congrArg Prod.snd h
        subst h1; subst h2
        exact ⟨⟨⟨i, rfl⟩, ⟨j, rfl⟩⟩, hg hij⟩
    rw [hpairs, prod_map, prod_filter, Fintype.prod_prod_type]
    apply prod_congr rfl; intro i _
    rw [← prod_filter]
    have : (univ : Finset (Fin n)).filter (fun j => i < j) = Ioi i := by ext j; simp
    rw [this]
    apply prod_congr rfl; intro j _
    change (x (g i) - x (g j)) ^ 2 = (x (g j) - x (g i)) ^ 2
    ring

/-- Andreief / Heine (item 11 Lemma H1, finite form). -/
theorem heineK_eq_det (x w : ℕ → ℝ) (K n : ℕ) : heineK x w K n = (hankelK x w K n).det := by
  classical
  set A : Matrix (Fin n) (Fin K) ℝ := Matrix.of fun i k => w k * x k ^ (i : ℕ) with hA
  set B : Matrix (Fin K) (Fin n) ℝ := Matrix.of fun k j => x k ^ (j : ℕ) with hB
  have hfac : hankelK x w K n = A * B := by
    ext i j
    simp only [hankelK, hA, hB, of_apply, mul_apply]
    rw [← Fin.sum_univ_eq_sum_range (fun k => w k * x k ^ ((i : ℕ) + j))]
    apply sum_congr rfl; intro k _; ring
  rw [hfac, det_mul_cauchyBinet]
  -- each Cauchy–Binet term is a Heine term
  have hterm : ∀ S : {S : Finset (Fin K) // S.card = n},
      (A.submatrix id (S.1.orderEmbOfFin S.2)).det * (B.submatrix (S.1.orderEmbOfFin S.2) id).det =
        heineTerm x w (S.1.map Fin.valEmbedding) := by
    intro S
    set e := S.1.orderEmbOfFin S.2
    set g : Fin n → ℕ := fun i => (e i : ℕ) with hg
    have hgm : StrictMono g := fun i j hij => by
      simp only [hg]; exact Fin.lt_def.1 (e.strictMono hij)
    have hmap : S.1.map Fin.valEmbedding = univ.map ⟨g, hgm.injective⟩ := by
      conv_lhs => rw [← map_orderEmbOfFin_univ S.1 S.2]
      rw [Finset.map_map]; rfl
    rw [hmap, heineTerm_map_strictMono x w g hgm]
    have hBS : B.submatrix e id = Matrix.vandermonde (fun i => x (g i)) := by
      ext i j; simp [hB, hg, Matrix.vandermonde_apply]
    have hAS : A.submatrix id e = (B.submatrix e id)ᵀ * Matrix.diagonal (fun j => w (g j)) := by
      ext i j; simp [hA, hB, hg, Matrix.mul_diagonal]; ring
    rw [hAS, det_mul, det_transpose, det_diagonal, hBS, det_vandermonde]
    rw [show ∏ i, ∏ j ∈ Ioi i, (x (g j) - x (g i)) ^ 2 = (∏ i, ∏ j ∈ Ioi i, (x (g j) - x (g i))) ^ 2 by
      rw [← prod_pow]; apply prod_congr rfl; intro i _; rw [← prod_pow]]
    ring
  simp_rw [hterm]
  -- reindex subsets of `Fin K` as subsets of `range K`
  unfold heineK
  symm
  apply Finset.sum_bij (fun S _ => S.1.map Fin.valEmbedding)
  · intro S _
    rw [mem_powersetCard]
    refine ⟨fun a ha => ?_, by rw [card_map, S.2]⟩
    obtain ⟨k, _, rfl⟩ := mem_map.1 ha
    exact mem_range.2 k.2
  · intro S _ S' _ h
    exact Subtype.ext (map_injective _ h)
  · intro T hT
    obtain ⟨hTsub, hTcard⟩ := mem_powersetCard.1 hT
    set S : Finset (Fin K) := univ.filter (fun k : Fin K => (k : ℕ) ∈ T) with hS
    have hmapS : S.map Fin.valEmbedding = T := by
      ext a
      simp only [hS, mem_map, mem_filter, mem_univ, true_and, Fin.valEmbedding_apply]
      constructor
      · rintro ⟨k, hk, rfl⟩; exact hk
      · intro ha; exact ⟨⟨a, mem_range.1 (hTsub ha)⟩, ha, rfl⟩
    have hScard : S.card = n := by rw [← card_map Fin.valEmbedding, hmapS, hTcard]
    exact ⟨⟨S, hScard⟩, mem_univ _, hmapS⟩
  · intro S _; rfl

end JacobiAsym
