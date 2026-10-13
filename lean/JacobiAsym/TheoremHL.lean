import JacobiAsym.UpperBound
import JacobiAsym.LowerBound

open Filter Topology

namespace JacobiAsym

/-- **Item 11 Theorem H_L (PROVED-mod-input).**  Atoms `(k+1)^{-p} L(k+1)` with `L` slowly varying
(`SlowFactor`), weights sandwiched `c1 (k+1)^{-s} ≤ w k ≤ c2 (k+1)^{-s0} U(k+1)`; given the named input
Theorem H for the pure powers with exponents `s` and `s0` and constant `κ`:
`log D_n = -p n² log n + n² log L(n) + κ n² + o(n²)`.  `κ` is the constant of the input; item 11 supplies
`TheoremHPure p κ s` only for `p ∈ {1, 2}`, `s ≥ s0(p)`, with `κ = 3p/2 + log c(p)`, so the theorem is *usable*
only there.  `hU1`/`Monotone U` lose no generality (replace `U` by `t ↦ U (max t 1) / U 1`, or a running max). -/
theorem theoremHL {p κ s s0 c1 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ}
    (hL : SlowFactor p L L' E a0) (hHlo : TheoremHPure p κ s) (hHup : TheoremHPure p κ s0)
    (hc1 : 0 < c1) (hc2 : 0 < c2)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hU1 : ∀ t, 1 ≤ U t) (hUmono : Monotone U)
    (hUsub : Tendsto (fun n : ℕ => Real.log (U n) / n) atTop (𝓝 0))
    (hwsum : Summable w) :
    Tendsto (hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)))
      atTop (𝓝 0) := by
  have hp := hL.p_pos
  rw [Metric.tendsto_atTop]
  intro ε hε
  set A := 4 * p + 2 * |κ| with hAdef
  have hA : 0 < A := by have := abs_nonneg κ; linarith
  set X := 3 * A ^ 2 / (4 * p * ε) with hX
  have hXpos : 0 < X := by positivity
  set M : ℕ := ⌈Real.exp X⌉₊ + 2 with hMdef
  have hM2 : 2 ≤ M := by omega
  have hMgt : Real.exp X < M := by
    have := Nat.le_ceil (Real.exp X)
    have : ((⌈Real.exp X⌉₊ + 2 : ℕ) : ℝ) = (⌈Real.exp X⌉₊ : ℝ) + 2 := by push_cast; ring
    rw [hMdef, this]; linarith
  have hlogM : X < Real.log M := by
    rw [← Real.exp_lt_exp, Real.exp_log (by have := Real.exp_pos X; linarith)]; exact hMgt
  have hA2 : A ^ 2 / (4 * p * Real.log M) < ε / 3 := by
    have hlogpos : 0 < Real.log M := hXpos.trans hlogM
    rw [div_lt_iff₀ (by positivity)]
    have h1 : A ^ 2 = X * (4 * p * ε) / 3 := by rw [hX]; field_simp
    rw [h1]
    have : X * (4 * p * ε) < Real.log M * (4 * p * ε) := mul_lt_mul_of_pos_right hlogM (by positivity)
    nlinarith
  have hup := HL_upper hL hHup hc2
    (fun k => (mul_pos hc1 (Real.rpow_pos_of_pos (by positivity : (0:ℝ) < (k:ℝ) + 1) (-s))).trans_le (hwlo k))
    hwhi hU1 hUmono hUsub hwsum hM2 (by positivity : (0 : ℝ) < ε / 3)
  have hlo := HL_lower hL hHlo hHup hc1 hc2 hwlo hwhi hUmono hwsum (by positivity : (0 : ℝ) < ε / 2)
  obtain ⟨N, hN⟩ := eventually_atTop.1 (hup.and hlo)
  refine ⟨N, fun n hn => ?_⟩
  obtain ⟨h1, h2⟩ := hN n hn
  rw [Real.dist_eq, sub_zero, abs_lt]
  constructor <;> linarith

end JacobiAsym
