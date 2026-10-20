"""E2 Corollary E2.7 (NUMERICAL check): the Christoffel function at the hard edge,
lambda_n(0) := min{ int R^2 dsigma : deg R <= n-1, R(0) = 1 } = D_n(sigma)/D_{n-1}(x^2 sigma),  x^2 sigma_{p,s} = sigma_{p,s+2p},
computed from the Plan 62 quad-precision coefficients (so_coeffs, tail-corrected measure) as
log lambda_n(0) = log h_{n-1}(s) + sum_{j<n-1} [log h_j(s) - log h_j(s+2p)],  h_j = m_0 prod_{i<=j} b_i^2.
Prediction (Cor E2.7, p > 1): lambda_n(0) ~ C n^{-(p+2)(s-1)/p}; printed: local slopes of log lambda_n(0) vs log n."""
import sys
import numpy as np
import mpmath as mp
from so_coeffs import coeffs, measure

mp.mp.dps = 40
NMAX = 1600


def logh(p, s):
    K = (100 if p >= 1 else 200) * NMAX
    _, b = coeffs(p, s, K, NMAX)
    m0 = mp.zeta(s)
    out = [mp.log(m0)]
    for i in range(NMAX - 1):
        out.append(out[-1] + 2 * mp.log(b[i]))
    return out                       # out[j] = log h_j, j = 0..NMAX-1


for p, s in [(1.5, 2.0), (2.0, 2.0), (2.0, 3.0), (3.0, 2.0)]:
    A, B = logh(p, s), logh(p, s + 2 * p)
    ns = [100, 200, 400, 800, 1600]
    lam = []
    for n in ns:
        lam.append(A[n - 1] + sum(A[j] - B[j] for j in range(n - 1)))
    sl = [float((lam[k + 1] - lam[k]) / mp.log(ns[k + 1] / ns[k])) for k in range(len(ns) - 1)]
    pred = -(p + 2) * (s - 1) / p
    print(f"p={p} s={s}: predicted exponent {pred:+.6f}; local slopes " + " ".join(f"{x:+.6f}" for x in sl), flush=True)
