import JacobiAsym.HeineCompare

open Finset

namespace JacobiAsym

/-- `e_m(w restricted to s) ≤ (∑_{b∈s} w b)^m` for nonnegative weights (true also for `m = 0`). -/
theorem sum_prod_powersetCard_le {w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) (s : Finset ℕ) (m : ℕ) :
    ∑ T ∈ s.powersetCard m, ∏ b ∈ T, w b ≤ (∑ b ∈ s, w b) ^ m := by
  induction s using Finset.induction_on generalizing m with
  | empty =>
    cases m with
    | zero => simp
    | succ m => rw [powersetCard_eq_empty.2 (by simp)]; simp
  | insert a s ha ih =>
    cases m with
    | zero => simp
    | succ m =>
      have hW : 0 ≤ ∑ b ∈ s, w b := sum_nonneg fun b _ => hw b
      rw [powersetCard_succ_insert ha, sum_insert ha]
      calc ∑ T ∈ s.powersetCard (m + 1) ∪ (s.powersetCard m).image (insert a), ∏ b ∈ T, w b
          = ∑ T ∈ s.powersetCard (m + 1), ∏ b ∈ T, w b
            + ∑ T ∈ (s.powersetCard m).image (insert a), ∏ b ∈ T, w b := by
            apply sum_union
            rw [disjoint_left]
            intro T h1 h2
            obtain ⟨U, _, rfl⟩ := mem_image.1 h2
            exact ha ((mem_powersetCard.1 h1).1 (mem_insert_self a U))
        _ ≤ ∑ T ∈ s.powersetCard (m + 1), ∏ b ∈ T, w b
            + ∑ T ∈ s.powersetCard m, ∏ b ∈ insert a T, w b := by
            gcongr
            exact sum_image_le_of_nonneg (fun T _ => prod_nonneg fun b _ => hw b)
        _ = ∑ T ∈ s.powersetCard (m + 1), ∏ b ∈ T, w b
            + w a * ∑ T ∈ s.powersetCard m, ∏ b ∈ T, w b := by
            rw [mul_sum]; congr 1; apply sum_congr rfl; intro T hT
            have haT : a ∉ T := fun h => ha ((mem_powersetCard.1 hT).1 h)
            rw [prod_insert haT]
        _ ≤ (∑ b ∈ s, w b) ^ (m + 1) + w a * (∑ b ∈ s, w b) ^ m := by
            have h1 := ih (m + 1)
            have h2 := ih m
            have := hw a
            gcongr
        _ ≤ (w a + ∑ b ∈ s, w b) ^ (m + 1) := by
            have h1 : (∑ b ∈ s, w b) ^ m ≤ (w a + ∑ b ∈ s, w b) ^ m :=
              pow_le_pow_left₀ hW (le_add_of_nonneg_left (hw a)) m
            rw [pow_succ, pow_succ]
            nlinarith [hw a, pow_nonneg hW m]

/-- `N! ≤ ∏_{a∈S} (a+1)` when `|S| = N` (the `i`-th smallest element is `≥ i`). -/
theorem factorial_le_prod_succ (S : Finset ℕ) : ((S.card).factorial : ℝ) ≤ ∏ a ∈ S, ((a : ℝ) + 1) := by
  rw [prod_eq_prod_orderEmb S rfl (fun a => (a : ℝ) + 1), ← prod_range_add_one_eq_factorial, Nat.cast_prod,
    ← Fin.prod_univ_eq_prod_range]
  apply prod_le_prod₀ (fun i _ => by positivity)
  intro i _
  push_cast
  gcongr
  exact_mod_cast orderEmb_ge S rfl i

end JacobiAsym
