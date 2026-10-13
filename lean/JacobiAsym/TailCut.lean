import JacobiAsym.Combinatorics

open Finset

namespace JacobiAsym

variable {K0 : ℕ}

theorem pairs_filter_head (S : Finset ℕ) :
    (pairs S).filter (fun p => p.2 < K0) = pairs (S.filter (· < K0)) := by
  ext ⟨a, b⟩; simp only [pairs, mem_filter, mem_product]; constructor
  · rintro ⟨⟨⟨ha, hb⟩, hab⟩, hbK⟩; exact ⟨⟨⟨ha, by omega⟩, hb, hbK⟩, hab⟩
  · rintro ⟨⟨⟨ha, _⟩, hb, hbK⟩, hab⟩; exact ⟨⟨⟨ha, hb⟩, hab⟩, hbK⟩

theorem pairs_filter_tail (S : Finset ℕ) :
    (pairs S).filter (fun p => ¬ p.2 < K0 ∧ ¬ p.1 < K0) = pairs (S.filter (fun b => ¬ b < K0)) := by
  ext ⟨a, b⟩; simp only [pairs, mem_filter, mem_product]; constructor
  · rintro ⟨⟨⟨ha, hb⟩, hab⟩, hb', ha'⟩; exact ⟨⟨⟨ha, ha'⟩, hb, hb'⟩, hab⟩
  · rintro ⟨⟨⟨ha, ha'⟩, hb, hb'⟩, hab⟩; exact ⟨⟨⟨ha, hb⟩, hab⟩, hb', ha'⟩

theorem pairs_filter_cross (S : Finset ℕ) :
    (pairs S).filter (fun p => ¬ p.2 < K0 ∧ p.1 < K0) =
      (S.filter (· < K0)) ×ˢ (S.filter (fun b => ¬ b < K0)) := by
  ext ⟨a, b⟩; simp only [pairs, mem_filter, mem_product]; constructor
  · rintro ⟨⟨⟨ha, hb⟩, _⟩, hb', ha'⟩; exact ⟨⟨ha, ha'⟩, hb, hb'⟩
  · rintro ⟨⟨ha, ha'⟩, hb, hb'⟩; exact ⟨⟨⟨ha, hb⟩, by omega⟩, hb', ha'⟩

/-- Pointwise form of Lemma H7 for one configuration `S`. -/
theorem heineTerm_tail_pointwise {y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {X : ℝ}
    (hpos : ∀ i, 0 < y i) (htail : ∀ b, K0 ≤ b → y b ≤ X) (hord : ∀ a b, a < K0 → K0 ≤ b → y b ≤ y a)
    (S : Finset ℕ) :
    heineTerm y w S ≤ heineTerm y w (S.filter (· < K0)) *
      (∏ a ∈ S.filter (· < K0), y a ^ (2 * (S.filter (fun b => ¬ b < K0)).card)) *
      (∏ b ∈ S.filter (fun b => ¬ b < K0), w b) *
      X ^ ((S.filter (fun b => ¬ b < K0)).card * ((S.filter (fun b => ¬ b < K0)).card - 1)) := by
  set SH := S.filter (· < K0) with hSH
  set ST := S.filter (fun b => ¬ b < K0) with hST
  set F : ℕ × ℕ → ℝ := fun p => (y p.1 - y p.2) ^ 2 with hF
  have hF0 : ∀ p, 0 ≤ F p := fun p => sq_nonneg _
  -- weights
  have hwS : ∏ i ∈ S, w i = (∏ i ∈ SH, w i) * ∏ i ∈ ST, w i := (prod_filter_mul_prod_filter_not S (· < K0) w).symm
  -- pairs split
  have hpS : ∏ p ∈ pairs S, F p =
      (∏ p ∈ pairs SH, F p) * ((∏ p ∈ SH ×ˢ ST, F p) * ∏ p ∈ pairs ST, F p) := by
    rw [← prod_filter_mul_prod_filter_not (pairs S) (fun p => p.2 < K0), pairs_filter_head,
      ← prod_filter_mul_prod_filter_not ((pairs S).filter (fun p => ¬ p.2 < K0)) (fun p => p.1 < K0),
      filter_filter, filter_filter, pairs_filter_cross, pairs_filter_tail]
  -- cross bound
  have hcross : ∏ p ∈ SH ×ˢ ST, F p ≤ ∏ a ∈ SH, y a ^ (2 * ST.card) := by
    rw [prod_product]
    apply prod_le_prod₀ (fun a _ => prod_nonneg fun b _ => hF0 _)
    intro a ha
    rw [pow_mul, ← prod_const]
    apply prod_le_prod₀ (fun b _ => hF0 _)
    intro b hb
    have haK : a < K0 := (mem_filter.1 ha).2
    have hbK : K0 ≤ b := not_lt.1 (mem_filter.1 hb).2
    have h1 := hord a b haK hbK
    have h2 := hpos b
    simp only [hF]
    nlinarith
  -- tail bound
  have htailp : ∏ p ∈ pairs ST, F p ≤ X ^ (ST.card * (ST.card - 1)) := by
    rw [← two_mul_card_pairs, pow_mul, ← prod_const]
    apply prod_le_prod₀ (fun p _ => hF0 _)
    intro p hp
    simp only [pairs, mem_filter, mem_product] at hp
    have ha := htail p.1 (not_lt.1 (mem_filter.1 hp.1.1).2)
    have hb := htail p.2 (not_lt.1 (mem_filter.1 hp.1.2).2)
    have h1 := hpos p.1
    have h2 := hpos p.2
    simp only [hF]
    nlinarith
  have hWH : 0 ≤ ∏ i ∈ SH, w i := prod_nonneg fun i _ => hw i
  have hWT : 0 ≤ ∏ i ∈ ST, w i := prod_nonneg fun i _ => hw i
  have hPH : 0 ≤ ∏ p ∈ pairs SH, F p := prod_nonneg fun p _ => hF0 p
  have hPT : 0 ≤ ∏ p ∈ pairs ST, F p := prod_nonneg fun p _ => hF0 p
  have hYa : 0 ≤ ∏ a ∈ SH, y a ^ (2 * ST.card) := prod_nonneg fun a _ => pow_nonneg (hpos a).le _
  unfold heineTerm
  rw [hwS, hpS]
  calc (∏ i ∈ SH, w i) * (∏ i ∈ ST, w i) *
        ((∏ p ∈ pairs SH, F p) * ((∏ p ∈ SH ×ˢ ST, F p) * ∏ p ∈ pairs ST, F p))
      ≤ (∏ i ∈ SH, w i) * (∏ i ∈ ST, w i) *
        ((∏ p ∈ pairs SH, F p) * ((∏ a ∈ SH, y a ^ (2 * ST.card)) * X ^ (ST.card * (ST.card - 1)))) := by
        gcongr
    _ = _ := by ring

/-- Lemma H7 core.  Split each `n`-subset `S ⊆ range K` into head `S ∩ range K0` (size `n - m`) and tail
`S ∩ Ico K0 K` (size `m`).  Cross pairs: `0 < y b ≤ y a` gives `(y a - y b)^2 ≤ (y a)^2`; tail pairs:
`(y b - y b')^2 ≤ X^2`; tail weights: `e_m ≤ (∑ w)^m`. -/
theorem heineK_tail_split {y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {K0 K n : ℕ} (_hK : K0 ≤ K) {X : ℝ}
    (hpos : ∀ i, 0 < y i) (htail : ∀ b, K0 ≤ b → y b ≤ X) (hord : ∀ a b, a < K0 → K0 ≤ b → y b ≤ y a) :
    heineK y w K n ≤ ∑ m ∈ range (n + 1),
      (∑ SH ∈ (range K0).powersetCard (n - m), heineTerm y w SH * ∏ a ∈ SH, y a ^ (2 * m)) *
      (∑ b ∈ Ico K0 K, w b) ^ m * X ^ (m * (m - 1)) := by
  classical
  have hXe : ∀ m : ℕ, 0 ≤ X ^ (m * (m - 1)) := fun m => (Nat.even_mul_pred_self m).pow_nonneg X
  set A := (range K).powersetCard n with hA
  set T := (range (n + 1)).sigma
    (fun m => ((range K0).powersetCard (n - m)) ×ˢ ((Ico K0 K).powersetCard m)) with hT
  set G : (Σ _ : ℕ, Finset ℕ × Finset ℕ) → ℝ := fun t =>
    heineTerm y w t.2.1 * (∏ a ∈ t.2.1, y a ^ (2 * t.1)) * (∏ b ∈ t.2.2, w b) * X ^ (t.1 * (t.1 - 1))
    with hG
  set ι : Finset ℕ → (Σ _ : ℕ, Finset ℕ × Finset ℕ) := fun S =>
    ⟨(S.filter (fun b => ¬ b < K0)).card, (S.filter (· < K0), S.filter (fun b => ¬ b < K0))⟩ with hι
  have hG0 : ∀ t, 0 ≤ G t := by
    intro t
    have h1 := heineTerm_nonneg (x := y) hw t.2.1
    have h2 : 0 ≤ ∏ a ∈ t.2.1, y a ^ (2 * t.1) := prod_nonneg fun a _ => pow_nonneg (hpos a).le _
    have h3 : 0 ≤ ∏ b ∈ t.2.2, w b := prod_nonneg fun b _ => hw b
    have h4 := hXe t.1
    simp only [hG]; positivity
  have step1 : heineK y w K n ≤ ∑ S ∈ A, G (ι S) :=
    sum_le_sum fun S _ => heineTerm_tail_pointwise hw hpos htail hord S
  have hinj : Set.InjOn ι A := by
    intro S _ S' _ h
    simp only [hι, Sigma.mk.injEq] at h
    obtain ⟨_, h⟩ := h
    have h' : (Prod.mk (S.filter (· < K0)) (S.filter (fun b => ¬ b < K0))) =
        (S'.filter (· < K0), S'.filter (fun b => ¬ b < K0)) := eq_of_heq h
    simp only [Prod.mk.injEq] at h'
    rw [← filter_union_filter_not_eq (fun x => x < K0) S, ← filter_union_filter_not_eq (fun x => x < K0) S', h'.1, h'.2]
  have hsub : A.image ι ⊆ T := by
    intro t ht
    obtain ⟨S, hS, rfl⟩ := mem_image.1 ht
    obtain ⟨hSK, hSn⟩ := mem_powersetCard.1 hS
    have hcard := card_filter_add_card_filter_not (s := S) (fun x => x < K0)
    simp only [hT, hι, mem_sigma, mem_range, mem_product, mem_powersetCard]
    refine ⟨by omega, ⟨?_, by omega⟩, ?_, trivial⟩
    · intro b hb; exact mem_range.2 (mem_filter.1 hb).2
    · intro b hb
      have hbS := (mem_filter.1 hb)
      exact mem_Ico.2 ⟨not_lt.1 hbS.2, mem_range.1 (hSK hbS.1)⟩
  have step2 : ∑ S ∈ A, G (ι S) ≤ ∑ t ∈ T, G t := by
    rw [← sum_image hinj]
    exact sum_le_sum_of_subset_of_nonneg hsub (fun t _ _ => hG0 t)
  refine step1.trans (step2.trans ?_)
  rw [hT, sum_sigma]
  apply sum_le_sum
  intro m _
  rw [sum_product]
  have hfac : ∑ SH ∈ (range K0).powersetCard (n - m), ∑ ST ∈ (Ico K0 K).powersetCard m, G ⟨m, (SH, ST)⟩ =
      (∑ SH ∈ (range K0).powersetCard (n - m), heineTerm y w SH * ∏ a ∈ SH, y a ^ (2 * m)) *
      (∑ ST ∈ (Ico K0 K).powersetCard m, ∏ b ∈ ST, w b) * X ^ (m * (m - 1)) := by
    simp only [hG, sum_mul, mul_sum]
    exact sum_comm
  rw [hfac]
  have hH : 0 ≤ ∑ SH ∈ (range K0).powersetCard (n - m), heineTerm y w SH * ∏ a ∈ SH, y a ^ (2 * m) :=
    sum_nonneg fun SH _ => mul_nonneg (heineTerm_nonneg hw SH) (prod_nonneg fun a _ => pow_nonneg (hpos a).le _)
  have hX := hXe m
  gcongr
  exact sum_prod_powersetCard_le hw (Ico K0 K) m

end JacobiAsym
