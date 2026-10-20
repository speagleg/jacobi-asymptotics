"""SPEC probe 2 (integer layer beyond Z(0)): synthetic lattice lam_k = (k + g/k)^p, weights lam^{-s/p} (k >= 1).
Z(0) unchanged (same count), so S1' predicts d1 = d1_0 and, if decaying index corrections enter the integer layer only at
n^-3, d2 = d2_0. Zeta layer: Z(-j) = zeta(-jp) + sum_k [(k + g/k)^{jp} - k^{jp}] (convergent for jp < 1, else regularised);
to first order Delta Z(-j) = jp g zeta(2 - jp); the script uses the exact regularised value (Hurwitz-type expansion)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from math import comb
from spec_common import run, fit, NMAX, c_p_mp
from so_coeffs import coeffs
from so_fit import sequences
p, s, g = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
K = (200 if p < 1 else 100)*NMAX
k = np.arange(1, K + 1, dtype=np.float64)
n, y = run(f"gamma_p{p}_s{s}_g{g}", (k + g/k)**p, p, s, 0.0, K)
mp.mp.dps = 30
def Zm(j, kex=4000, terms=8):
    # Z(-j) = sum_k (k + g/k)^{jp}: expand (k + g/k)^{jp} = k^{jp} sum_i binom(jp, i) g^i k^{-2i}; regularise term-wise
    q = j*mp.mpf(p); reg = sum(mp.binomial(q, i)*mp.mpf(g)**i*mp.zeta(2*i - q) for i in range(terms))
    corr = sum((mp.mpf(kk) + mp.mpf(g)/kk)**q - sum(mp.binomial(q, i)*mp.mpf(g)**i*mp.mpf(kk)**(q - 2*i) for i in range(terms)) for kk in range(1, kex + 1))
    return reg + corr
c = c_p_mp(p)
d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
D = n*(y - y0)
print(f"p={p} s={s} g={g}")
v1, h1 = fit(n, y, p, [], 1.0); print(f"  d1: fit {v1:+.8f} ({h1:.1e})  lattice {-(s-1)/2:+.8f}")
e1 = float(2*p*c*Zm(1)); e10 = float(2*p*c*mp.zeta(-p))
r = y + (s - 1)/(2*n); skip = [1.0]
v, h = fit(n, r, p, skip, 1 + p)
print(f"  eps1 (n^-1-p): fit {v:+.7f} ({h:.1e})  S1 {e1:+.7f} diff {v - e1:+.1e}  [lattice {e10:+.7f}; first order 2pc*p*g*zeta(2-p) = {float(2*p*c*p*g*mp.zeta(2-p)):+.6f}]")
r2 = r - e1*n**(-1 - p); skip = [1.0, round(1 + p, 9)]
if p < 1 and 1 + 2*p < 2.5:
    e2 = float(6*p*c**2*Zm(2)); r2 = r2 - e2*n**(-1 - 2*p); skip.append(round(1 + 2*p, 9))
v, h = fit(n, r2, p, skip, 2.0)
print(f"  n^-2: fit {v:+.6f} ({h:.1e})  lattice d2_0 {d2f(p, s):+.6f}  diff {v - d2f(p, s):+.1e}   [-p*g = {-p*g:+.4f} would be an O(n^-2) index effect]")
# n^-3 difference directly from D = n (y - y0): D ~ (eps1 - eps1_0) n^{-p} + Delta d2 / n + Delta d3 / n^2 + ...
DD = D - (e1 - e10)*n**(-p)
for lo in (200, 400, 800):
    m = n >= lo
    E = [1.0, 2.0, 1 + p, 2 + p, 3.0] if p > 1 else [1.0, 2.0, 2*p, 1 + p, 3*p]
    A = np.vstack([n[m]**-e for e in E]).T
    co = np.linalg.lstsq(A, DD[m], rcond=None)[0]
    print(f"  fit of n(y - y_lat) - Delta eps1 n^-p on n >= {lo}: Delta d2 = {co[0]:+.6f}, Delta d3 = {co[1]:+.6f}  (other: {', '.join(f'{c_:+.3g}' for c_ in co[2:])})")
