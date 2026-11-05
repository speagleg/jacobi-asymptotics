"""SPEC probe: the n^-2 coefficient for Hurwitz lattices lam = (k + d)^p (weights (k+d)^{-s}), from the caches of spec_hur.py.
Fit after subtracting d1(a) = -(s-1)/2 - p d and eps_j(a) = C(2j,j) p c^j zeta(-jp, 1+d) (j with 1+jp < 2.5, 1+jp != 2;
at p = 1.5, eps_1's exponent is exactly 2.5, so it is not subtracted and stays in the fit pool instead).
Compared with the pure index-shift rule n -> n + d applied to the lattice expansion:
  d2_shift = d2_0 + p(p+1) d^2/2 - (p+1) d d1_0,   d1_0 = -(s-1)/2,  d2_0 = d2(p, s) (E2 closed form)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from math import comb
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import fit, NMAX, Checks
C_ = Checks()
d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
print(f"{'p':>5} {'s':>4} {'d':>5} | {'n^-2 fit':>12} {'(hr)':>8} | {'index-shift':>12} {'diff':>9} | {'lattice d2_0':>12}")
for p, s, d in [(0.6, 2.0, -0.5), (0.6, 2.0, 0.5), (0.6, 2.0, 1.0), (0.75, 3.0, 1.0), (1.5, 2.0, 0.5), (1.5, 2.0, 1.0)]:
    K = (200 if p < 1 else 100)*NMAX
    al, b = coeffs(p, s, K, NMAX, d); n, y, *_ = sequences(p, al, b); n = n.astype(float)
    c = c_p_mp(p); a = 1 + d
    r = y - (-(s - 1)/2 - p*d)/n; skip = [1.0]
    for j in (1, 2, 3):
        e = 1 + j*p
        if e < 2.5 and abs(e - 2) > 1e-9:
            r = r - float(comb(2*j, j)*p*c**j*mp.zeta(-j*mp.mpf(p), a))*n**(-e); skip.append(round(e, 9))
    v, h = fit(n, r, p, skip, 2.0)
    d10 = -(s - 1)/2; pred = d2f(p, s) + p*(p + 1)*d*d/2 - (p + 1)*d*d10
    print(f"{p:5} {s:4} {d:5} | {v:+12.6f} {h:8.1e} | {pred:+12.6f} {v - pred:+9.1e} | {d2f(p, s):+12.6f}")
    C_.check(f"d2 p={p} s={s} d={d}", v, pred, max(3*h, 1e-4))
C_.finish()
