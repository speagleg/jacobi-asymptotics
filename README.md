# jacobi-asymptotics

Jacobi coefficients (a_n, b_n) and Hankel determinants of discrete positive measures σ = Σ w_k δ_{x_k} with
x_k ↓ 0, and the "Law P" asymptotics b_n/x_n → c(p) = ¼(π/(2I(p)))^p for x_k ~ C k^{-p}
(c(2) = π²/16). Continues math-pursuits item 11.

Status: toolkit done (Plan 1). Lean: Theorem H_L and Corollary H_L-ζ (smooth ζ model, stated for the Hankel
determinant, and in its b_j form (2/n²)Σ(n−j)log(b_j/x_j) → log(π²/16)) proved from the named input Theorem H, plus Lemma P, Cauchy–Binet/Andreief and the Toeplitz eigenvalue count (S4) (Plans 2–6, lean/README.md). The Lean bridge plans are complete.
Research: research/G3prime, G2, G1.
- G3′ (true zeros, Plan 7; pending Rule R review): the upper bound is unconditional (mod the cited S(T) bound) and the
  lower bound holds under a small-gaps hypothesis (SG). Counting-function information provably cannot give the lower
  bound (Prop N). Stop condition: an unconditional lower bound needs multiplicity/small-gap input beyond the
  literature read. See research/G3prime/PROOF.md.
- G2 (Plan 8; Rule R REVIEWED): Theorem H (the averaged Law P) is proved for **every p > 0**, in
  research/G2/PROOF.md. The n² constant is identified as an explicitly solvable constrained logarithmic equilibrium,
  whose optimizer is a superposition of the Weyl-law arcsine measures. A corollary is the n² asymptotics of the
  Haynes–Zudilin determinants det ζ(a(i+j)+b) for all a ≥ 1.
- G1 (Plan 9, time-boxed; Rule R REVIEWED): the pointwise law is reduced to a single a priori regularity statement
  for b_n (slow oscillation, (T3)), via the averaged law and a windowed Tauberian argument. The a_n side has a lower
  bound and, for p > 1, a conditional upper bound via a Heine-ensemble tail identity. Stop report: GAP, with missing
  statements (T3) and (CL). See research/G1/PROOF.md §4.
- RH program (Plan 10; research/G1/RH): **Theorem RH₁**, the pointwise Law P with an O(1/n) rate for
  Σ k^{−3/2}δ_{1/k}, is proved via a Riemann–Hilbert perturbation of Wu–Lin–Xu–Zhao's Tricomi–Carlitz analysis
  (PROVED-mod-cite, REVIEWED).
  - Plan 11 extends it to **every r > 1**: Theorem RH₁(r) for Σ k^{−r}δ_{1/k}, using a Fisher–Hartwig Bessel parametrix
    at the band centre (RH/RH_p1_general.md; PROVED-mod-cite, REVIEWED).
  - Plan 12 covers **every p > 1** (Theorem RH_p, RH/px/RH_px.md; PROVED-mod-cite, REVIEWED). It works in the
    unsymmetrized x-variable, with an exact Binet-cut scalar and a hard-edge Bessel parametrix.
  - Together these give the pointwise Law P with an O(1/n) rate for all pure powers with power weights, p ≥ 1.
  - Plans 13–14 (smooth ζ model, RH/zeta/; Rule R REVIEWED): **Theorem RH_ζ**, the pointwise Law P for the smooth-ζ
    model with rate, b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log²n)), κ = −0.28946… (PROVED-mod-cite).

  - Plan 15 (RH/plt1/): **0 < p < 1**, REVIEWED. The seam construction covers all 0 < p < 1 with no numerical caveat.
    With RH₁(r) and RH_p, **the pointwise Law P with an O(1/n) rate holds for every pure power with power weights,
    p > 0, s > 1.**
- G3′ (research/G3prime/, Plans 7, 16, 17; all REVIEWED). For the true-zero measure:
  - **(U)** limsup ≤ 0, unconditionally;
  - **(B)** liminf ≥ −3 log C, unconditionally, so log D_n = Φ_n + O(n²);
  - **(L)** G3′ holds under (SG), or (C) under Montgomery's pair-correlation conjecture (no RH);
  - **(N′)** G3′ forces repeated ordinates to contain no positive-density family.

**Status (2026-10-14).** Open:
- G3′ exactly (D = 0) unconditionally. By N′ this needs proportion-one distinctness of ordinates, beyond the best known
  unconditional results (Lamzouri 2026: 67.25% simple and on the line).
- The residual N′ case (positive lower density with d_* = 0).
- An explicit constant in (B).
- G1-R: (T3)/(CL) for general, rough (non-analytic) weights and nodes. The analytic families done are pure powers
  (all p > 0) and the smooth-ζ model.

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
