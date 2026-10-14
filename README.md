# jacobi-asymptotics

Jacobi coefficients (a_n, b_n) and Hankel determinants of discrete positive measures σ = Σ w_k δ_{x_k} with
x_k ↓ 0, and the "Law P" asymptotics b_n/x_n → c(p) = ¼(π/(2I(p)))^p for x_k ~ C k^{-p}
(c(2) = π²/16). Continues math-pursuits item 11.

**Index: [THEOREMS.md](THEOREMS.md)** lists every result with its exact label, location and dependencies, the open
problems, and a name glossary. Labels are defined in VERIFICATION_POLICY.md. "RH" in file names (research/G1/RH)
means Riemann–Hilbert. The Riemann Hypothesis occurs only as a labelled hypothesis of conditional G3′ results.

## Status (2026-10-14)

- **Toolkit** (Plan 1): done (`src/jacobi_asym`).
- **Lean** (Plans 2–6, lean/README.md): Theorem H_L (`theoremHL`) and Corollary H_L-ζ (`smoothZeta_HL`,
  `smoothZeta_bLaw`) are PROVED-mod-input `TheoremHPure` (Theorem H for pure powers, a named input). The foundations
  (Andreief/Heine, H2, three-term recurrence, Lemma P, the Toeplitz count (S4)) are sorry-free. On paper, the input
  is supplied for all p > 0, s > 1 by G2 Corollary H-input, mod-cite (P). That proof is not formalized.
- **G2** (Plan 8, research/G2): **Theorem H_all**, the averaged Law P for every p > 0, is PROVED-mod-cite (P) and
  REVIEWED. The n² constant is an explicitly solvable constrained logarithmic equilibrium, a superposition of arcsine
  laws. Corollary HZ: log det ζ(a(i+j)+b) = −an² log n + (3a/2 + log c(a))n² + o(n²) for real a > 0 and 2a + b > 1
  (PROVED-mod-cite (P)).
- **G1, pointwise law for pure powers** (Plans 10–15, research/G1/RH): the pointwise Law P with an O(1/n) rate holds
  for every σ_{p,s} = Σ k^{−s}δ_{k^{−p}}, p > 0, s > 1. The results are RH₁(r) (p = 1), RH_p (p > 1) and the seam
  construction (0 < p < 1). For the smooth-ζ model, Theorem RH_ζ gives
  b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log²n)). All are PROVED-mod-cite + REVIEWED.
- **G1, weights k^{−s}Ψ** (Plans 27–36, research/G1/PROOF.md):
  - full pointwise Law P for bounded slowly varying Ψ (Theorem T3-all) and for log-type Ψ such as (log k)^α
    (Theorem T3-log), both PROVED-mod-cite + REVIEWED;
  - fixed-size rough weights can break (T3) and the pointwise b-law (Theorem R, PROVED-mod-cite + REVIEWED);
  - (CL) and the tail-Cesàro a-law for p > 1 with rough weights (Theorem CL, A4′; PROVED-mod-cite (P), REVIEWED).
- **G3′, the true ζ-zero measure** (Plans 7, 16–26, research/G3prime; the ordinates are taken as real numbers):
  - **(U)** limsup (1/n²)[log D_n − Φ_n] ≤ 0, with no hypothesis on the zeros. Label: PROVED-mod-cite + mod-input
    Theorem H (Lean `TheoremHPure`) + REVIEWED; Theorem H input discharged by G2 Cor. H-input (mod-cite (P)). The
    cited input is (C1).
  - **(B)** liminf ≥ −3 log C > −∞, so log D_n = Φ_n + O(n²) with no hypothesis on the zeros. Label: PROVED-mod-cite
    (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED; Theorem H input discharged by G2 Cor.
    H-input (mod-cite (P)).
  - **Theorem Ch:** G3′ ⟺ 𝒞(K) = o(K²) (capped near-pair energy of the ordinates). Label: PROVED-mod-cite (C1) +
    mod-input Theorem H; REVIEWED; Theorem H input discharged by G2 Cor. H-input (mod-cite (P)).
  - Necessary conditions: G3′ forces repeated ordinates (N″) and exponentially small gaps (N‴) to have density zero.
    Prop N shows that counting-function information alone cannot decide G3′.
  - Sufficient conditions, each a labelled hypothesis: (SG) (G3′-L), (LG*) (L′), PCC with no RH (Theorem C), SPC_ℂ⁺
    (Theorem S), SPC_ℂ⁺(full) (Theorem S′), RH + (V⁺) (Theorem V⁺), RH + (V) (Corollary P). All are REVIEWED.
  - The Theorem H input of every G3′ result is p = 2 only (THEOREMS.md §3.3).

**Open** (details in THEOREMS.md §4):
- G3′ with no hypothesis, i.e. 𝒞(K) = o(K²) for the ζ ordinates. By N″ this implies proportion-one distinct ordinates,
  beyond the best unconditional results read (Lamzouri 2026: 67.25% simple and on the line).
- An explicit constant in Theorem B.
- G1: slowly varying Ψ with D(γ) = ∞ (e.g. exp(√log k)); nodes other than pure powers; (CL) for general nodes or
  p ≤ 1; pointwise a_n for rough weights.
- Lean: Theorem H_all (and with it the discharge of `TheoremHPure`) is not formalized.

## Setup
    scripts/setup_env.sh
    .venv/bin/python -m pytest            # fast suite
    .venv/bin/python -m pytest -m slow    # regressions against item 11 (minutes)

Measures built from L-function zeros take the ordinates as real numbers. Nothing here is evidence about RH.

## Quick use
```python
from jacobi_asym.measures import smooth_zeta, pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import c_p, averaged_law, predict_b

mu = pure_power(2, 200_000)                 # atoms k^-2, weights = atoms
r = jacobi_coeffs(mu, 2000)                 # RKPW, float64 (numerical)
print(r.b[1999] / mu.atoms[1999], c_p(2))   # b_n/x_n vs pi^2/16
print(averaged_law(r.b, mu.atoms, 2, [2000]))
```
Certified (Arb) coefficients for small exact-float measures: `jacobi_asym.certify.certified_jacobi`.
