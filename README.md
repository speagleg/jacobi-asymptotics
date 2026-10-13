# jacobi-asymptotics

Jacobi coefficients (a_n, b_n) and Hankel determinants of discrete positive measures σ = Σ w_k δ_{x_k} with
x_k ↓ 0, and the "Law P" asymptotics b_n/x_n → c(p) = ¼(π/(2I(p)))^p for x_k ~ C k^{-p}
(c(2) = π²/16). Continues math-pursuits item 11.

Status: toolkit done (Plan 1). Lean: Theorem H_L proved from the named input Theorem H, plus Lemma P (Plans 2–3,
lean/README.md).
Research: research/G3prime, G2, G1.

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
