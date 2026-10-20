"""Exact per-node formula: delete node k0 from sigma_{p,s}. Prediction (gauge identity applied to the tilt (1 - x lam/n^p)^{-2} plus
the index shift): n * (y_removed - y_pure) -> -p (1 - u)^{-1/2},  u = 4c (k0/n)^p  (node outside the band: u < 1)."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_common import *
from so_coeffs import coeffs
p, s, k0 = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]); K = 200*NMAX
k = np.arange(1, K+1, dtype=np.float64); k = k[k != k0]
n, y = run(f"rm_p{p}_s{s}_k{k0}", k**p, p, s, 0.0, K)
al, b = coeffs(p, s, K, NMAX); n0, y0, *_ = sequences(p, al, b)
c = float(c_p_mp(p)); D = n*(y - y0)
print(f"p={p} s={s} remove k0={k0}; node leaves the band (u < 1) for n > k0 (4c)^(1/p) = {k0*(4*c)**(1/p):.1f}")
print(f"{'n':>6} {'u':>7} {'n*(y_rm - y)':>14} {'-p(1-u)^-1/2':>14} {'ratio':>8} {'series to eps1':>14}")
for nv in (100, 200, 400, 600, 800, 1000, 1200, 1400, 1600):
    i = nv-1; u = 4*c*(k0/nv)**p
    pred = -p*(1-u)**-0.5 if u < 1 else float('nan'); ser = -p*(1 + 2*c*(k0/nv)**p)
    print(f"{nv:6d} {u:7.3f} {D[i]:+14.6f} {pred:+14.6f} {D[i]/pred:8.4f} {ser:+14.6f}")
