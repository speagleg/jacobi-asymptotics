"""SPEC direction 4: the single-node response kernel through the turning point.
Move node k0 of sigma_{p,s} to k0 + h (node (k0+h)^{-p}, weight (k0+h)^{-s}). As n grows, u_n = 4c(k0/n)^p decreases through 1
at n* = k0 (4c)^{1/p}. Output: D(n) := n (y_n(moved) - y_n(pure)).
Prediction for u < 1 (S2' differentiated): D(n) = p[(1-u_a)^{-1/2} - (1-u_l)^{-1/2}] with u_a = 4c((k0+h)/n)^p, u_l = 4c(k0/n)^p
(both nodes outside the band). Near u = 1: turning point (Airy scale 1 - u ~ n^{-2/3}).
Also prints the antisymmetry test if both +h and -h caches exist."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np
from spec_common import run, c_p_mp, NMAX
from so_coeffs import coeffs
from so_fit import sequences
p, s, k0, h = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
K = 200*NMAX
def moved(hh):
    k = np.arange(1, K + 1, dtype=np.float64); k[k0 - 1] = k0 + hh
    return run(f"turn_p{p}_s{s}_k{k0}_h{hh}", k**p, p, s, 0.0, K)
n, y = moved(h)
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
c = float(c_p_mp(p)); D = n*(y - y0); nstar = k0*(4*c)**(1/p)
print(f"p={p} s={s} node {k0} -> {k0+h}: n* = {nstar:.1f}")
print(f"{'n':>6} {'u_l':>7} {'D(n)':>13} {'S2p-diff':>13} {'ratio':>8}")
for nv in [50, 100, 200, 300, 400, 500, 600, 650, 700, 720, 740, 760, 780, 800, 850, 900, 1000, 1200, 1600]:
    if nv > NMAX: continue
    ul = 4*c*(k0/nv)**p; ua = 4*c*((k0 + h)/nv)**p
    pr = p*((1 - ua)**-0.5 - (1 - ul)**-0.5) if max(ul, ua) < 1 else float('nan')
    print(f"{nv:6d} {ul:7.3f} {D[nv-1]:+13.6e} {pr:+13.6e} {D[nv-1]/pr if pr == pr else float('nan'):8.4f}")
if True:   # the -h run is always computed (linearity test)
    _, ym = moved(-h); Dm = n*(ym - y0)
    S, A = D + Dm, D - Dm
    for lo, hi in ((50, 500), (500, 900), (900, 1600)):
        sel = slice(lo - 1, hi)
        print(f"  linearity on n in [{lo},{hi}]: max|D(+h) + D(-h)| = {np.max(np.abs(S[sel])):.2e}  vs  max|D(+h) - D(-h)|/2 = {np.max(np.abs(A[sel]))/2:.2e}")
# turning-region profile: D vs the Airy variable
print("turning profile: tau = (n - n*)/n*^(1/3), D * n*^(?)")
for nv in range(int(nstar) - 80, int(nstar) + 81, 10):
    if 1 <= nv <= NMAX:
        print(f"  n={nv:5d} tau={(nv - nstar)/nstar**(1/3):+7.3f} D={D[nv-1]:+.5e}")
