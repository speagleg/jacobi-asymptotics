import JacobiAsym.Heine

open Finset

namespace JacobiAsym

/-- The `i`-th smallest element (0-based) of a finset of naturals is at least `i`. -/
theorem orderEmb_ge (S : Finset ℕ) {n : ℕ} (h : S.card = n) (i : Fin n) : (i : ℕ) ≤ S.orderEmbOfFin h i := by
  have key : ∀ k (hk : k < n), k ≤ S.orderEmbOfFin h ⟨k, hk⟩ := by
    intro k
    induction k with
    | zero => intro _; exact Nat.zero_le _
    | succ k ih =>
      intro hk
      have hlt : S.orderEmbOfFin h ⟨k, by omega⟩ < S.orderEmbOfFin h ⟨k + 1, hk⟩ :=
        (S.orderEmbOfFin h).strictMono (Fin.mk_lt_mk.2 (Nat.lt_succ_self k))
      have := ih (by omega)
      omega
  exact key i i.2

/-- `2 * |pairs S| = n (n - 1)`. -/
theorem two_mul_card_pairs (S : Finset ℕ) : 2 * (pairs S).card = S.card * (S.card - 1) := by
  rw [card_pairs]
  exact Nat.mul_div_cancel' (Nat.even_mul_pred_self S.card).two_dvd

/-- Uniform pair comparison: if every pair satisfies `(x a - x b)^2 ≤ lam^2 (y a - y b)^2`, then
`heineTerm x ≤ lam^(n(n-1)) heineTerm y`, `n = |S|`. -/
theorem heineTerm_le_of_pair_le {x y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {lam : ℝ} (_hlam : 0 ≤ lam)
    {S : Finset ℕ} (h : ∀ a ∈ S, ∀ b ∈ S, a < b → (x a - x b) ^ 2 ≤ lam ^ 2 * (y a - y b) ^ 2) :
    heineTerm x w S ≤ lam ^ (S.card * (S.card - 1)) * heineTerm y w S := by
  unfold heineTerm
  have hp : ∏ p ∈ pairs S, (x p.1 - x p.2) ^ 2 ≤ ∏ p ∈ pairs S, (lam ^ 2 * (y p.1 - y p.2) ^ 2) := by
    apply prod_le_prod₀ (fun _ _ => sq_nonneg _)
    intro p hp
    simp only [pairs, mem_filter, mem_product] at hp
    exact h p.1 hp.1.1 p.2 hp.1.2 hp.2
  rw [prod_mul_distrib, prod_const, ← pow_mul, two_mul_card_pairs] at hp
  calc (∏ i ∈ S, w i) * ∏ p ∈ pairs S, (x p.1 - x p.2) ^ 2
      ≤ (∏ i ∈ S, w i) * (lam ^ (S.card * (S.card - 1)) * ∏ p ∈ pairs S, (y p.1 - y p.2) ^ 2) :=
        mul_le_mul_of_nonneg_left hp (prod_nonneg fun i _ => hw i)
    _ = _ := by ring

/-- A product over `S` re-indexed by the increasing enumeration of `S`. -/
theorem prod_eq_prod_orderEmb (S : Finset ℕ) {k : ℕ} (h : S.card = k) (G : ℕ → ℝ) :
    ∏ a ∈ S, G a = ∏ i : Fin k, G (S.orderEmbOfFin h i) := by
  conv_lhs => rw [← map_orderEmbOfFin_univ S h]
  rw [prod_map]; rfl

/-- The element of rank `i` (0-based) is the smaller index of exactly `k - 1 - i` elements of `S`. -/
theorem card_filter_gt_orderEmb (S : Finset ℕ) {k : ℕ} (h : S.card = k) (i : Fin k) :
    (S.filter (fun b => S.orderEmbOfFin h i < b)).card = k - 1 - i := by
  have hS : univ.map (S.orderEmbOfFin h).toEmbedding = S := map_orderEmbOfFin_univ S h
  calc (S.filter (fun b => S.orderEmbOfFin h i < b)).card
      = ((univ.map (S.orderEmbOfFin h).toEmbedding).filter (fun b => S.orderEmbOfFin h i < b)).card := by
        rw [hS]
    _ = k - 1 - i := ?_
  rw [filter_map, card_map]
  have : univ.filter ((fun b => S.orderEmbOfFin h i < b) ∘ (S.orderEmbOfFin h).toEmbedding) = Ioi i := by
    ext j; simp
  rw [this, Fin.card_Ioi]

/-- A product over pairs of a function of the smaller index. -/
theorem prod_pairs_fst (S : Finset ℕ) (g : ℕ → ℝ) :
    ∏ p ∈ pairs S, g p.1 = ∏ a ∈ S, g a ^ (S.filter (fun b => a < b)).card := by
  unfold pairs
  rw [prod_filter, prod_product]
  apply prod_congr rfl; intro a _
  rw [← prod_filter]
  exact prod_const (g a)

/-- Rank-dependent lower comparison: if `ρ ≥ 0` is monotone and every pair `a < b` satisfies
`ρ a ^ 2 (y a - y b)^2 ≤ (x a - x b)^2`, then `(∏_{i<n} ρ i ^ (2(n-1-i))) heineTerm y ≤ heineTerm x`
(0-based ranks: the `i`-th smallest element is `≥ i` and is the smaller index of exactly `n-1-i` pairs). -/
theorem heineTerm_ge_of_pair_ge {x y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {ρ : ℕ → ℝ}
    (hρ0 : ∀ i, 0 ≤ ρ i) (hρ : Monotone ρ) {S : Finset ℕ}
    (h : ∀ a ∈ S, ∀ b ∈ S, a < b → ρ a ^ 2 * (y a - y b) ^ 2 ≤ (x a - x b) ^ 2) :
    (∏ i ∈ range S.card, ρ i ^ (2 * (S.card - 1 - i))) * heineTerm y w S ≤ heineTerm x w S := by
  unfold heineTerm
  have hrank : ∏ i ∈ range S.card, ρ i ^ (2 * (S.card - 1 - i)) ≤ ∏ p ∈ pairs S, ρ p.1 ^ 2 := by
    rw [prod_pairs_fst S (fun a => ρ a ^ 2), prod_eq_prod_orderEmb S rfl, ← Fin.prod_univ_eq_prod_range]
    apply prod_le_prod₀ (fun i _ => pow_nonneg (hρ0 _) _)
    intro i _
    rw [card_filter_gt_orderEmb S rfl i, ← pow_mul]
    exact pow_le_pow_left₀ (hρ0 _) (hρ (orderEmb_ge S rfl i)) _
  have hpair : ∏ p ∈ pairs S, (ρ p.1 ^ 2 * (y p.1 - y p.2) ^ 2) ≤ ∏ p ∈ pairs S, (x p.1 - x p.2) ^ 2 := by
    apply prod_le_prod₀ (fun _ _ => mul_nonneg (sq_nonneg _) (sq_nonneg _))
    intro p hp
    simp only [pairs, mem_filter, mem_product] at hp
    exact h p.1 hp.1.1 p.2 hp.1.2 hp.2
  rw [prod_mul_distrib] at hpair
  have hW : 0 ≤ ∏ i ∈ S, w i := prod_nonneg fun i _ => hw i
  have hY : 0 ≤ ∏ p ∈ pairs S, (y p.1 - y p.2) ^ 2 := prod_nonneg fun _ _ => sq_nonneg _
  calc (∏ i ∈ range S.card, ρ i ^ (2 * (S.card - 1 - i))) *
        ((∏ i ∈ S, w i) * ∏ p ∈ pairs S, (y p.1 - y p.2) ^ 2)
      ≤ (∏ p ∈ pairs S, ρ p.1 ^ 2) * ((∏ i ∈ S, w i) * ∏ p ∈ pairs S, (y p.1 - y p.2) ^ 2) :=
        mul_le_mul_of_nonneg_right hrank (mul_nonneg hW hY)
    _ = (∏ i ∈ S, w i) * ((∏ p ∈ pairs S, ρ p.1 ^ 2) * ∏ p ∈ pairs S, (y p.1 - y p.2) ^ 2) := by ring
    _ ≤ (∏ i ∈ S, w i) * ∏ p ∈ pairs S, (x p.1 - x p.2) ^ 2 := mul_le_mul_of_nonneg_left hpair hW

end JacobiAsym
