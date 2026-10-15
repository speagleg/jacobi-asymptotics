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
  is supplied by item 11's Theorem H for p ∈ {1, 2}, s ≥ s₀(p) (p = 2 citation-free, which covers Corollary H_L-ζ),
  and for all p > 0, s > 1 by G2 Corollary H-input, PROVED since Plan 47 (was mod-cite (P); REVIEWED, research/G2/review/REVIEW_Plan47.md). Neither
  proof is formalized.
- **G2** (Plan 8, research/G2): **Theorem H_all**, the averaged Law P for every p > 0, is PROVED (Plan 47: the citation
  (P) is replaced by the self-contained Lemma EP; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED); previously PROVED-mod-cite (P) and
  REVIEWED. The n² constant is an explicitly solvable constrained logarithmic equilibrium, a superposition of arcsine
  laws. Corollary HZ: log det ζ(a(i+j)+b) = −an² log n + (3a/2 + log c(a))n² + o(n²) for real a > 0 and 2a + b > 1
  (PROVED since Plan 47, was PROVED-mod-cite (P); REVIEWED).
- **G1, pointwise law for pure powers** (Plans 10–15, research/G1/RH): the pointwise Law P with an O(1/n) rate holds
  for every σ_{p,s} = Σ k^{−s}δ_{k^{−p}}, p > 0, s > 1. The results are RH₁(r) (p = 1), RH_p (p > 1) and the seam
  construction (0 < p < 1). For the smooth-ζ model, Theorem RH_ζ gives
  b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log²n)). All are PROVED-mod-cite + REVIEWED.
- **G1, weights k^{−s}Ψ** (Plans 27–36, research/G1/PROOF.md):
  - full pointwise Law P for bounded slowly varying Ψ (Theorem T3-all) and for log-type Ψ such as (log k)^α
    (Theorem T3-log), both PROVED-mod-cite + REVIEWED;
  - fixed-size rough weights can break (T3) and the pointwise b-law (Theorem R, PROVED-mod-cite + REVIEWED);
  - (CL) and the tail-Cesàro a-law for p > 1 with rough weights (Theorem CL, A4′; PROVED since Plan 47, was PROVED-mod-cite (P);
    REVIEWED, relabel REVIEWED by research/G2/review/REVIEW_Plan47.md).
- **G3′, the true ζ-zero measure** (Plans 7, 16–26, research/G3prime; the ordinates are taken as real numbers):
  - **(U)** limsup (1/n²)[log D_n − Φ_n] ≤ 0, with no hypothesis on the zeros. Label: PROVED-mod-cite + mod-input
    Theorem H (Lean `TheoremHPure`) + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H
    (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)). The cited input is (C1).
  - **(B)** liminf ≥ −3 log C > −∞, so log D_n = Φ_n + O(n²) with no hypothesis on the zeros. Label: PROVED-mod-cite
    (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by
    item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)).
  - **Theorem Ch:** G3′ ⟺ 𝒞(K) = o(K²) (capped near-pair energy of the ordinates). Label: PROVED-mod-cite (C1) +
    mod-input Theorem H; REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED
    there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)).
  - Necessary conditions: G3′ forces repeated ordinates (N″) and exponentially small gaps (N‴) to have density zero.
    Prop N shows that counting-function information alone cannot decide G3′.
  - Sufficient conditions, each a labelled hypothesis: (SG) (G3′-L), (LG*) (L′), PCC with no RH (Theorem C), SPC_ℂ⁺
    (Theorem S), SPC_ℂ⁺(full) (Theorem S′), RH + (V⁺) (Theorem V⁺), RH + (V) (Corollary P). All are REVIEWED.
  - The Theorem H input of every G3′ result is p = 2, s ≥ 2 only, supplied citation-free by item 11, so no G3′ result
    depends on G2's citation (P) (THEOREMS.md §3.3). Since Plan 47 G2 uses no citation at all.

**Plans 39–44 (2026-10-14, all REVIEWED; THEOREMS.md §2.6):** Conjecture R in window form for ε ≤ ε₀ (Theorem RW);
linear response with sharp ε² remainder (Lemma LR); rough weights also break the pointwise a-law (Theorem Ra); Law P ⟺
arcsine limit of the rescaled μ_n, given an a priori bound (Lemma RL); the law for every slowly varying weight,
conditional on one localization hypothesis QL (Theorem B-cond); G3′ is at least as hard as "100% of zeros simple and on
the critical line", and d̄(E) ≤ 0.3275 unconditionally (G3′ §5.6). Novelty first pass and research program:
research/program/RESEARCH_PROGRAM.md.

**Plans 45–49 (2026-10-14, all REVIEWED; THEOREMS.md §2.7):** the pointwise Law P now holds for p > 1, 1 < s < 1 + 2p and
**every** slowly varying weight factor Ψ, including exp(√log k) (Theorem RII / Corollary B_{p>1}, Route II Riemann–Hilbert
analysis); pure-power hard-edge localization QLP; the commutator route reduces the remaining cases to one open lemma (CB);
G2's last external citation (P) is replaced by a self-contained proof (Lemma EP), so Theorem H_all and the zeta-value
Hankel asymptotics are PROVED. Paper 1 draft: papers/paper1/.

**Plans 50–52 (REVIEWED; THEOREMS.md §2.8):** with the Christoffel shift (Theorem SH: Law P for σ ⇒ for x·σ), the
pointwise Law P holds for nodes k^{−p} and weights k^{−s}Ψ with Ψ **any** slowly varying function, for every p > 0 and
s > 1 (the last case, p = 1 with integer r ≥ 2, closed by Plan 54's x-frame analysis at p = 1).

**Open** (details in THEOREMS.md §4):
- G3′ with no hypothesis, i.e. 𝒞(K) = o(K²) for the ζ ordinates. It implies that 100% of zeros are simple and on the
  critical line (§5.6), beyond the best unconditional results read (Lamzouri 2026: 67.25%).
- An explicit constant in Theorem B.
- G1: slowly varying Ψ with D(γ) = ∞ (PROVED for all p > 0 and s > 1; open: the 1/n coefficient); nodes other than pure powers; (CL)
  for general nodes or p ≤ 1; density-one law for rough weights; sharp constants in Theorems R/RW/Ra.
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
