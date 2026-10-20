"""SPEC direction 3, hypothesis boundary: lam_k = k^p + kappa (all eigenvalues shifted by a constant), p = 0.6, s = 2.
lam^{1/p} = k + (kappa/p) k^{1-p} + ...: NOT of the form m + a + O(1/m), so S1 does not apply. The formal node zeta would give
Z(-1) = zeta(-p) + kappa zeta(0) at order n^{-1-p}; the band nodes move by relative kappa/lam ~ kappa x n^{-p}, which suggests an
effect already at relative order n^{-p}. Measured: Delta y_n := y_n(kappa) - y_n(0), and its scaling in n."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import run, c_p_mp, NMAX
from so_coeffs import coeffs
from so_fit import sequences
p, s, kap = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6, 2.0, float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
K = 200*NMAX; k = np.arange(1, K + 1, dtype=np.float64)
n, y = run(f"kappa_p{p}_s{s}_k{kap}", k**p + kap, p, s, 0.0, K)
al, b = coeffs(p, s, K, NMAX); n0, y0, *_ = sequences(p, al, b)
D = y - y0; c = float(c_p_mp(p))
print(f"kappa = {kap}, p = {p}: c = {c:.6f}")
for nv in (50, 100, 200, 400, 800, 1600):
    i = nv - 1
    print(f"  n={nv:5d}: Delta y = {D[i]:+.6e}   n^p Delta y = {nv**p*D[i]:+.6f}   n^(1+p) Delta y = {nv**(1+p)*D[i]:+.5f}")
# local slope of log|Delta y|
for lo, hi in ((100, 200), (400, 800), (800, 1600)):
    print(f"  slope d log|Dy|/d log n on [{lo},{hi}]: {np.log(abs(D[hi-1]/D[lo-1]))/np.log(hi/lo):+.4f}")
v = np.array([nv**p*D[nv-1] for nv in (400, 800, 1600)]); r = (v[2]-v[1])/(v[1]-v[0])
lim = v[2] + (v[2]-v[1])*r/(1-r)
print(f"  extrapolated lim n^p Delta y = {lim:+.5f} (geometric, ratio {r:.3f});  -2(2-p)c kappa = {-2*(2-p)*c*kap:+.5f}")
