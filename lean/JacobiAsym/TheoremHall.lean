import JacobiAsym.HallLower
import JacobiAsym.HallUpper
import JacobiAsym.TheoremHL

/-! # Plan 60, stage S5: Theorem H_all for pure powers — the named input `TheoremHPure` as a theorem

`theoremHPure_all`: for every `p > 0` and `s > 1`, `TheoremHPure p (hallKappa p) s` holds, with
`hallKappa p = 3p/2 + log c(p)`, `c(p) = (π/Λ(p))^p/4`, `Λ(p) = ∫₀¹ arccos (2s^p − 1) ds` (Paper 1 Theorem 1.1 for
`x_k = k^{-p}`, `w_k = k^{-s}`; G2 Corollary H-input). The `bdd` field is `heineK_bdd_of_summable`; `asymp` combines
the lower bound `hall_lower` (Theorem 5.2) and the upper bound `hall_upper` (Theorem 4.3, via Lemma EP and
optimality). The identification `Λ(p) = 2I(p) = √π Γ(1/p+1/2)/Γ(1/p+1)` is stage S6. -/

open Real Filter Topology

namespace JacobiAsym

/-- **Theorem H_all for pure powers** (Paper 1 Theorem 1.1, `x_k = k^{-p}`, `w_k = k^{-s}`): the Lean named input
`TheoremHPure p κ_p s` holds for every `p > 0`, `s > 1`. -/
theorem theoremHPure_all {p s : ℝ} (hp : 0 < p) (hs : 1 < s) : TheoremHPure p (hallKappa p) s where
  bdd := heineK_bdd_of_summable (fun k => (powSeq_pos s k).le) (powSeq_summable hs) (X := 1)
    (fun k => by
      rw [abs_of_pos (powSeq_pos p k)]
      exact rpow_le_one_of_one_le_of_nonpos (by have := Nat.cast_nonneg (α := ℝ) k; linarith) (by linarith))
  asymp := by
    rw [Metric.tendsto_atTop]
    intro ε hε
    obtain ⟨N, hN⟩ := eventually_atTop.1 ((hall_lower hp hs (half_pos hε)).and (hall_upper hp hs (half_pos hε)))
    refine ⟨N, fun n hn => ?_⟩
    obtain ⟨h1, h2⟩ := hN n hn
    rw [Real.dist_eq, sub_zero, abs_lt]
    constructor <;> linarith

/-- Theorem H_L (item 11) for every `p > 0` and `s, s0 > 1` **without named input**: `theoremHL` with both
instances of `TheoremHPure` discharged by `theoremHPure_all`. -/
theorem theoremHL_all {p s s0 c1 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ}
    (hL : SlowFactor p L L' E a0) (hs : 1 < s) (hs0 : 1 < s0) (hc1 : 0 < c1) (hc2 : 0 < c2)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hU1 : ∀ t, 1 ≤ U t) (hUmono : Monotone U)
    (hUsub : Tendsto (fun n : ℕ => Real.log (U n) / n) atTop (𝓝 0)) (hwsum : Summable w) :
    Tendsto (hnorm p (hallKappa p) (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)))
      atTop (𝓝 0) :=
  theoremHL hL (theoremHPure_all hL.p_pos hs) (theoremHPure_all hL.p_pos hs0) hc1 hc2 hwlo hwhi hU1 hUmono
    hUsub hwsum

end JacobiAsym
