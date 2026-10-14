import JacobiAsym.TailCut

open Finset Filter Topology

namespace JacobiAsym

/-- Heine-sum surrogate for `D_n` of `∑_k w k δ_{x k}`: the supremum of the truncated Heine sums (meaningful only
under `BddAbove`; otherwise Lean's junk value 0). It equals `det (m_{i+j})` by Andreief + `K → ∞`; that identity is
proved separately (`heineD_eq_det`, Plan 4), not by this definition. -/
noncomputable def heineD (x w : ℕ → ℝ) (n : ℕ) : ℝ := ⨆ K, heineK x w K n

/-- Pure-power sequence `(k+1)^{-p}` (0-based index `k` = item-11 atom `k+1`). -/
noncomputable def powSeq (p : ℝ) : ℕ → ℝ := fun k => ((k : ℝ) + 1) ^ (-p)

/-- `(log D n - (-p n² log n + n² ℓ n + κ n²)) / n²`. -/
noncomputable def hnorm (p κ : ℝ) (D ℓ : ℕ → ℝ) (n : ℕ) : ℝ :=
  (Real.log (D n) - (-p * (n : ℝ) ^ 2 * Real.log n + (n : ℝ) ^ 2 * ℓ n + κ * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2

/-- NAMED INPUT — item 11 Theorem H for atoms `(k+1)^{-p}`, weights `(k+1)^{-s}` (PROVED in item 11 via the
Lommel / Tricomi–Carlitz families; NOT formalized): bounded in `K`, and `log D_n = -p n² log n + κ n² + o(n²)`.
This is item 11's Theorem H transported to `heineD` via H1. Item 11 supplies it only for `p ∈ {1, 2}` and
`s ≥ s0(p)` (`s0(2) = 2`, `s0(1) = 3/2`), with `κ = 3p/2 + log c(p)`. On paper, G2 Corollary H-input
(research/G2/PROOF.md §3) supplies it for all `p > 0`, `s > 1` with `κ = 3p/2 + log c(p)`, mod-cite (P); that
proof is not formalized, so this stays a named input. -/
structure TheoremHPure (p κ s : ℝ) : Prop where
  bdd : ∀ n, BddAbove (Set.range fun K => heineK (powSeq p) (powSeq s) K n)
  asymp : Tendsto (hnorm p κ (heineD (powSeq p) (powSeq s)) (fun _ => 0)) atTop (𝓝 0)

theorem heineK_zero_card (x w : ℕ → ℝ) (K : ℕ) : heineK x w K 0 = 1 := by
  simp [heineK, heineTerm, pairs]

theorem heineK_pos {x w : ℕ → ℝ} (hx : StrictAnti x) (hw : ∀ i, 0 < w i) {K n : ℕ} (hKn : n ≤ K) :
    0 < heineK x w K n := by
  have hmem : range n ∈ (range K).powersetCard n :=
    mem_powersetCard.2 ⟨range_subset_range.2 hKn, card_range n⟩
  have hterm : 0 < heineTerm x w (range n) := by
    unfold heineTerm
    apply mul_pos (prod_pos fun i _ => hw i)
    apply prod_pos
    intro q hq
    simp only [pairs, mem_filter] at hq
    have : x q.2 < x q.1 := hx hq.2
    exact pow_pos (by linarith) 2
  exact hterm.trans_le (single_le_sum (f := heineTerm x w)
    (fun S _ => heineTerm_nonneg (fun i => (hw i).le) S) hmem)

theorem heineK_le_heineD {x w : ℕ → ℝ} {n : ℕ} (hb : BddAbove (Set.range fun K => heineK x w K n)) (K : ℕ) :
    heineK x w K n ≤ heineD x w n :=
  le_ciSup hb K

theorem heineD_le {x w : ℕ → ℝ} {n : ℕ} {C : ℝ} (h : ∀ K, heineK x w K n ≤ C) : heineD x w n ≤ C :=
  ciSup_le h

theorem heineD_pos {x w : ℕ → ℝ} (hx : StrictAnti x) (hw : ∀ i, 0 < w i) {n : ℕ}
    (hb : BddAbove (Set.range fun K => heineK x w K n)) : 0 < heineD x w n :=
  (heineK_pos hx hw (le_refl n)).trans_le (heineK_le_heineD hb n)

/-- Uniform-in-`N` upper form of the input. -/
theorem TheoremHPure.uniform_upper {p κ s : ℝ} (h : TheoremHPure p κ s) {η : ℝ} (hη : 0 < η) :
    ∃ C : ℝ, ∀ N : ℕ, Real.log (heineD (powSeq p) (powSeq s) N) ≤
      -p * (N : ℝ) ^ 2 * Real.log N + κ * (N : ℝ) ^ 2 + η * (N : ℝ) ^ 2 + C := by
  set g : ℕ → ℝ := fun N => Real.log (heineD (powSeq p) (powSeq s) N) -
    (-p * (N : ℝ) ^ 2 * Real.log N + κ * (N : ℝ) ^ 2 + η * (N : ℝ) ^ 2) with hg
  obtain ⟨N0, hN0⟩ := eventually_atTop.1 (h.asymp.eventually (gt_mem_nhds hη))
  set N1 := max N0 1
  refine ⟨∑ N ∈ range N1, |g N|, fun N => ?_⟩
  have hC0 : 0 ≤ ∑ N ∈ range N1, |g N| := sum_nonneg fun _ _ => abs_nonneg _
  suffices hgN : g N ≤ ∑ N ∈ range N1, |g N| by simp only [hg] at hgN; linarith
  rcases lt_or_ge N N1 with hN | hN
  · exact (le_abs_self _).trans (single_le_sum (f := fun N => |g N|) (fun _ _ => abs_nonneg _)
      (mem_range.2 hN))
  · have hN1 : 1 ≤ N := le_trans (le_max_right _ _) hN
    have hpos : (0 : ℝ) < (N : ℝ) ^ 2 := by positivity
    have := hN0 N (le_trans (le_max_left _ _) hN)
    simp only [hnorm, mul_zero, add_zero] at this
    rw [div_lt_iff₀ hpos] at this
    have : g N ≤ 0 := by simp only [hg]; linarith
    linarith

end JacobiAsym
