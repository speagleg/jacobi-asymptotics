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
