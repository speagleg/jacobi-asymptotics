"""SPEC §3.5: first-order prediction of the kappa shift from the exact Moebius identity.
log b_n^2(sigma_kappa) - log b_n^2(sigma) ~ Delta_m^2 [ -2 kappa (m-1) T(m) ] at m = n, T(m) = sum_{j<m} alpha_j(sigma) = Tr J_m,
(first order in kappa y; the (1 + kappa y)^{-s/p} tilt and the N-dependence of alpha_j are O(n^{-1-p}), O(kappa^2 n^{-2p})).
Compared with the measured log-ratio from the cached runs of spec_kappa.py."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import CACHE, NMAX
from so_coeffs import coeffs
for p, kap in ((0.6, 1.0), (0.6, 0.5), (0.3, 1.0)):
    s = 2.0; K = 200*NMAX
    al0, b0 = coeffs(p, s, K, NMAX)
    rows = [l.split() for l in open(CACHE / f"kappa_p{p}_s{s}_k{kap}.txt")]
    b1 = [mp.mpf(r[1]) for r in rows]
    T = np.concatenate([[0.0], np.cumsum([float(a) for a in al0])])      # T[m] = sum_{j<m} alpha_j
    G = lambda m: -2*kap*(m - 1)*T[m]
    print(f"p={p} kappa={kap}:  n, measured log(b_n^2 ratio), predicted Delta^2 G, ratio, leading -4(2-p)c kappa n^-p")
    from so_coeffs import c_p_mp; c = float(c_p_mp(p))
    for n in (50, 100, 200, 400, 800, 1500):
        meas = float(2*mp.log(b1[n - 1]/b0[n - 1]))
        pred = G(n + 1) - 2*G(n) + G(n - 1)
        print(f"   n={n:5d}  {meas:+.6e}  {pred:+.6e}  {meas/pred:.5f}   {-4*(2 - p)*c*kap*n**-p:+.6e}")
