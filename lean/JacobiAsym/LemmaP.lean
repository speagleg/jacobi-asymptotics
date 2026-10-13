import JacobiAsym.Basic

open Finset Filter Topology

namespace JacobiAsym

/-- Item 11 Lemma P: if the Jacobi form is nonnegative, `(n+1)^p a_n → α` and `(n+1)^p b_n → β`, then
`α ≥ 2β`.  (0-based: `a n`, `b n` are item 11's `a_{n+1}`, `b_{n+1}`; `b n` couples `v n` and `v (n+1)`.) -/
theorem lemmaP {a b : ℕ → ℝ} {p α β : ℝ} (hp : 0 < p)
    (hJ : ∀ v : ℕ → ℝ, ∀ N, (∀ n, N ≤ n → v n = 0) →
      0 ≤ ∑ n ∈ range N, a n * v n ^ 2 + 2 * ∑ n ∈ range N, b n * v n * v (n + 1))
    (ha : Tendsto (fun n : ℕ => ((n : ℝ) + 1) ^ p * a n) atTop (𝓝 α))
    (hb : Tendsto (fun n : ℕ => ((n : ℝ) + 1) ^ p * b n) atTop (𝓝 β)) : 2 * β ≤ α := by
  by_contra hcon'
  have hcon := lt_of_not_ge hcon'
  set δ := 2 * β - α with hδ
  have hδpos : 0 < δ := by linarith
  set w : ℕ → ℝ := fun n => ((n : ℝ) + 1) ^ (-p) with hw
  have hwpos : ∀ n, 0 < w n := fun n => Real.rpow_pos_of_pos (by positivity) _
  have hwanti : ∀ m n : ℕ, m ≤ n → w n ≤ w m := by
    intro m n hmn
    apply Real.rpow_le_rpow_of_nonpos (by positivity) _ (by linarith)
    have : (m : ℝ) ≤ n := by exact_mod_cast hmn
    linarith
  -- eventual bounds a n ≤ (α + δ/4) w n, b n ≥ (β - δ/4) w n
  have hpw : ∀ n : ℕ, ((n : ℝ) + 1) ^ p * w n = 1 := by
    intro n; simp only [hw]
    rw [← Real.rpow_add (by positivity)]; simp
  obtain ⟨Na, hNa⟩ := eventually_atTop.1 (ha.eventually (gt_mem_nhds (by linarith : α < α + δ / 4)))
  obtain ⟨Nb, hNb⟩ := eventually_atTop.1 (hb.eventually (lt_mem_nhds (by linarith : β - δ / 4 < β)))
  have habd : ∀ n, max Na Nb ≤ n → a n ≤ (α + δ / 4) * w n := by
    intro n hn
    have h := hNa n (le_of_max_le_left hn)
    have hwn := hwpos n
    have e : a n = (((n : ℝ) + 1) ^ p * a n) * w n := by
      linear_combination (-(a n)) * hpw n
    rw [e]; exact mul_le_mul_of_nonneg_right h.le hwn.le
  have hbbd : ∀ n, max Na Nb ≤ n → (β - δ / 4) * w n ≤ b n := by
    intro n hn
    have h := hNb n (le_of_max_le_right hn)
    have hwn := hwpos n
    have e : b n = (((n : ℝ) + 1) ^ p * b n) * w n := by
      linear_combination (-(b n)) * hpw n
    rw [e]; exact mul_le_mul_of_nonneg_right h.le hwn.le
  -- choose L
  set c := |α + δ / 4| with hc
  obtain ⟨L, hL⟩ : ∃ L : ℕ, L = max (max Na Nb) ⌈4 * (c + 1) / δ⌉₊ + 1 := ⟨_, rfl⟩
  have hLN : max Na Nb ≤ L := by rw [hL]; omega
  have hLbig : 4 * (c + 1) / δ < L := by
    have := Nat.le_ceil (4 * (c + 1) / δ)
    have : ((⌈4 * (c + 1) / δ⌉₊ : ℕ) : ℝ) ≤ (max (max Na Nb) ⌈4 * (c + 1) / δ⌉₊ : ℕ) := by
      exact_mod_cast le_max_right _ _
    have : ((max (max Na Nb) ⌈4 * (c + 1) / δ⌉₊ + 1 : ℕ) : ℝ) = (max (max Na Nb) ⌈4 * (c + 1) / δ⌉₊ : ℕ) + 1 := by
      push_cast; ring
    rw [hL, this]; linarith
  -- the test vector
  set v : ℕ → ℝ := fun n => if L ≤ n ∧ n ≤ 2 * L then (-1 : ℝ) ^ n else 0 with hv
  have hsupp : ∀ n, 2 * L + 2 ≤ n → v n = 0 := by
    intro n hn; simp only [hv]; rw [if_neg]; omega
  have hform := hJ v (2 * L + 2) hsupp
  -- evaluate the form
  have hsq : ∀ n, a n * v n ^ 2 = if n ∈ Ico L (2 * L + 1) then a n else 0 := by
    intro n; simp only [hv, mem_Ico]
    split_ifs with h1 h2 h2
    · rw [show ((-1 : ℝ) ^ n) ^ 2 = 1 by rw [← pow_mul, mul_comm n 2, pow_mul]; simp]; ring
    · omega
    · omega
    · simp
  have hcross : ∀ n, b n * v n * v (n + 1) = if n ∈ Ico L (2 * L) then -b n else 0 := by
    intro n; simp only [hv, mem_Ico]
    by_cases h1 : L ≤ n ∧ n < 2 * L
    · rw [if_pos (by omega), if_pos (by omega), if_pos h1, pow_succ]
      have : ((-1 : ℝ) ^ n) ^ 2 = 1 := by rw [← pow_mul, mul_comm n 2, pow_mul]; simp
      rw [show b n * (-1 : ℝ) ^ n * ((-1) ^ n * -1) = -(b n * ((-1 : ℝ) ^ n) ^ 2) by ring, this]; ring
    · rw [if_neg h1]
      by_cases h2 : L ≤ n ∧ n ≤ 2 * L
      · rw [if_pos h2, if_neg (by omega)]; ring
      · rw [if_neg h2]; ring
  have hsub1 : Ico L (2 * L + 1) ⊆ range (2 * L + 2) := by
    intro n hn; rw [mem_Ico] at hn; exact mem_range.2 (by omega)
  have hsub2 : Ico L (2 * L) ⊆ range (2 * L + 2) := by
    intro n hn; rw [mem_Ico] at hn; exact mem_range.2 (by omega)
  have hA : ∑ n ∈ range (2 * L + 2), a n * v n ^ 2 = ∑ n ∈ Ico L (2 * L + 1), a n := by
    simp_rw [hsq]; rw [sum_ite_mem, inter_eq_right.2 hsub1]
  have hB : ∑ n ∈ range (2 * L + 2), b n * v n * v (n + 1) = -∑ n ∈ Ico L (2 * L), b n := by
    simp_rw [hcross]; rw [sum_ite_mem, inter_eq_right.2 hsub2, sum_neg_distrib]
  rw [hA, hB] at hform
  -- bounds
  set S := ∑ n ∈ Ico L (2 * L), w n with hS
  have hSge : (L : ℝ) * w (2 * L) ≤ S := by
    have : ∑ n ∈ Ico L (2 * L), w (2 * L) ≤ S := sum_le_sum fun n hn => hwanti n (2 * L) (by
      rw [mem_Ico] at hn; omega)
    rw [sum_const, Nat.card_Ico, nsmul_eq_mul] at this
    have e : ((2 * L - L : ℕ) : ℝ) = L := by rw [show 2 * L - L = L by omega]
    rwa [e] at this
  have hAle : ∑ n ∈ Ico L (2 * L + 1), a n ≤ (α + δ / 4) * (S + w (2 * L)) := by
    rw [sum_Ico_succ_top (by omega : L ≤ 2 * L)]
    have h1 : ∑ n ∈ Ico L (2 * L), a n ≤ (α + δ / 4) * S := by
      rw [hS, mul_sum]
      exact sum_le_sum fun n hn => habd n (hLN.trans (mem_Ico.1 hn).1)
    have h2 : a (2 * L) ≤ (α + δ / 4) * w (2 * L) := habd _ (hLN.trans (by omega))
    calc _ ≤ (α + δ / 4) * S + (α + δ / 4) * w (2 * L) := add_le_add h1 h2
      _ = _ := by ring
  have hBge : (β - δ / 4) * S ≤ ∑ n ∈ Ico L (2 * L), b n := by
    rw [hS, mul_sum]
    exact sum_le_sum fun n hn => hbbd n (hLN.trans (mem_Ico.1 hn).1)
  have hw2L := hwpos (2 * L)
  have hcabs : (α + δ / 4) * w (2 * L) ≤ c * w (2 * L) := mul_le_mul_of_nonneg_right (le_abs_self _) hw2L.le
  have hLδ : 4 * (c + 1) < δ * L := by
    have := hLbig; rw [div_lt_iff₀ hδpos] at this; linarith
  have hneg : (α + δ / 4) * (S + w (2 * L)) - 2 * (β - δ / 4) * S < 0 := by
    have e : (α + δ / 4) * (S + w (2 * L)) - 2 * (β - δ / 4) * S = -(δ / 4) * S + (α + δ / 4) * w (2 * L) := by
      rw [hδ]; ring
    rw [e]
    have h1 : -(δ / 4) * S ≤ -(δ / 4) * ((L : ℝ) * w (2 * L)) :=
      mul_le_mul_of_nonpos_left hSge (by linarith)
    have h2 : c * w (2 * L) < (δ / 4) * ((L : ℝ) * w (2 * L)) := by
      have : c < δ / 4 * L := by linarith
      nlinarith
    linarith
  linarith

end JacobiAsym
