import JacobiAsym.Basic

open Finset

namespace JacobiAsym

/-- Ordered pairs `(a, b)` of `S` with `a < b`. -/
def pairs (S : Finset ℕ) : Finset (ℕ × ℕ) := (S ×ˢ S).filter (fun p => p.1 < p.2)

/-- Heine term of configuration `S`: `(∏_{i∈S} w i) * ∏_{a<b in S} (x a - x b)^2`. -/
noncomputable def heineTerm (x w : ℕ → ℝ) (S : Finset ℕ) : ℝ :=
  (∏ i ∈ S, w i) * ∏ p ∈ pairs S, (x p.1 - x p.2) ^ 2

/-- Heine sum over `n`-subsets of `range K` (= the `n × n` Hankel determinant of `∑_{k<K} w k δ_{x k}`,
by Andreief; that identity is NOT used or proved here). -/
noncomputable def heineK (x w : ℕ → ℝ) (K n : ℕ) : ℝ :=
  ∑ S ∈ (range K).powersetCard n, heineTerm x w S

theorem card_pairs (S : Finset ℕ) : (pairs S).card = S.card * (S.card - 1) / 2 := by
  have hsplit : (S ×ˢ S).filter (fun p : ℕ × ℕ => p.1 ≠ p.2) =
      (pairs S) ∪ (S ×ˢ S).filter (fun p : ℕ × ℕ => p.2 < p.1) := by
    ext p; simp only [pairs, mem_filter, mem_union, mem_product]; constructor
    · rintro ⟨h, hne⟩; rcases lt_or_gt_of_ne hne with h' | h' <;> simp_all
    · rintro (⟨h, h'⟩ | ⟨h, h'⟩) <;> exact ⟨h, by omega⟩
  have hdisj : Disjoint (pairs S) ((S ×ˢ S).filter (fun p : ℕ × ℕ => p.2 < p.1)) := by
    rw [disjoint_left]; intro p hp hq
    simp only [pairs, mem_filter] at hp hq; omega
  have hswap : ((S ×ˢ S).filter (fun p : ℕ × ℕ => p.2 < p.1)).card = (pairs S).card := by
    apply card_bij (fun p _ => p.swap)
    · intro p hp; simp only [pairs, mem_filter, mem_product, Prod.fst_swap, Prod.snd_swap] at hp ⊢
      exact ⟨⟨hp.1.2, hp.1.1⟩, hp.2⟩
    · intro a _ b _ h; simpa using h
    · intro q hq; refine ⟨q.swap, ?_, by simp⟩
      simp only [pairs, mem_filter, mem_product, Prod.fst_swap, Prod.snd_swap] at hq ⊢
      exact ⟨⟨hq.1.2, hq.1.1⟩, hq.2⟩
  have hoff : ((S ×ˢ S).filter (fun p : ℕ × ℕ => p.1 ≠ p.2)).card = S.card * S.card - S.card := by
    rw [← offDiag_card]; congr 1; ext p; simp [mem_offDiag, and_assoc]
  have h2 : 2 * (pairs S).card = S.card * (S.card - 1) := by
    rw [hsplit, card_union_of_disjoint hdisj, hswap] at hoff
    rw [Nat.mul_sub_one]; omega
  omega

theorem heineTerm_nonneg {x w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) (S : Finset ℕ) : 0 ≤ heineTerm x w S :=
  mul_nonneg (prod_nonneg fun i _ => hw i) (prod_nonneg fun _ _ => sq_nonneg _)

theorem heineK_mono_K {x w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {K K' : ℕ} (hK : K ≤ K') (n : ℕ) :
    heineK x w K n ≤ heineK x w K' n :=
  sum_le_sum_of_subset_of_nonneg (powersetCard_mono (range_subset_range.2 hK))
    (fun S _ _ => heineTerm_nonneg hw S)

theorem heineK_mono_w {x w w' : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) (hww : ∀ i, w i ≤ w' i) (K n : ℕ) :
    heineK x w K n ≤ heineK x w' K n := by
  apply sum_le_sum; intro S _
  exact mul_le_mul_of_nonneg_right (prod_le_prod₀ (fun i _ => hw i) (fun i _ => hww i))
    (prod_nonneg fun _ _ => sq_nonneg _)

theorem heineK_smul_w (x w : ℕ → ℝ) (c : ℝ) (K n : ℕ) :
    heineK x (fun i => c * w i) K n = c ^ n * heineK x w K n := by
  unfold heineK heineTerm; rw [mul_sum]; apply sum_congr rfl; intro S hS
  rw [prod_mul_distrib, prod_const, (mem_powersetCard.1 hS).2]; ring

end JacobiAsym
