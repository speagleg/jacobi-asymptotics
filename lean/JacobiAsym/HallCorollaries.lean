import JacobiAsym.TheoremHall
import JacobiAsym.HallGamma
import JacobiAsym.BLaw

/-! # Plan 60: consequences with no named input

With `theoremHPure_all` (stage S5) and the Gamma form of the constant (stage S6), the item-11 named input
`TheoremHPure p κ_p s`, `κ_p = 3p/2 + log c(p)`, `c(p) = ¼(π/(2I(p)))^p`, holds for all `p > 0`, `s > 1`
(`theoremHPure_kappa`), and the smooth-ζ corollaries of the library (which use the instance `p = s = 2`,
`κ = 3 + log(π²/16)`) become unconditional. -/

open Real Filter Topology Finset

namespace JacobiAsym

/-- **The named input, as a theorem, in the paper's normalisation**: `TheoremHPure p κ_p s` with
`κ_p = 3p/2 + log (¼ (π/(2 I(p)))^p)`, `I(p) = (√π/2) Γ(1/p + 1/2)/Γ(1/p + 1)`, for all `p > 0`, `s > 1`. -/
theorem theoremHPure_kappa {p s : ℝ} (hp : 0 < p) (hs : 1 < s) :
    TheoremHPure p (3 * p / 2 + Real.log ((π / (2 * hallI p)) ^ p / 4)) s := by
  rw [← hallKappa_eq hp]; exact theoremHPure_all hp hs

/-- The instance used by the smooth-ζ corollaries: `TheoremHPure 2 (3 + log (π²/16)) 2`. -/
theorem theoremHPure_two : TheoremHPure 2 (3 + Real.log (π ^ 2 / 16)) 2 := by
  rw [← hallKappa_two]; exact theoremHPure_all two_pos one_lt_two

/-- Corollary H_L-ζ (Heine form) with no named input. -/
theorem smoothZeta_HL_uncond :
    Tendsto (hnorm 2 (3 + Real.log (π ^ 2 / 16)) (heineD zetaAtom (fun k => 2 * zetaAtom k))
      (fun n => Real.log (zetaL n))) atTop (𝓝 0) :=
  smoothZeta_HL theoremHPure_two

/-- Corollary H_L-ζ (Hankel-determinant form) with no named input. -/
theorem smoothZeta_HL_det_uncond :
    Tendsto (hnorm 2 (3 + Real.log (π ^ 2 / 16)) (fun n => (hankel zetaAtom (fun k => 2 * zetaAtom k) n).det)
      (fun n => Real.log (zetaL n))) atTop (𝓝 0) :=
  smoothZeta_HL_det theoremHPure_two

/-- The `b_j` form of Corollary H_L-ζ with no named input. -/
theorem smoothZeta_bLaw_uncond :
    Tendsto (fun n : ℕ => 2 / (n : ℝ) ^ 2 *
      ∑ j ∈ Ico 1 n, ((n : ℝ) - j) *
        Real.log (Real.sqrt (jb2 zetaAtom (fun k => 2 * zetaAtom k) j) / zetaAtom (j - 1)))
      atTop (𝓝 (Real.log (π ^ 2 / 16))) :=
  smoothZeta_bLaw theoremHPure_two

end JacobiAsym
