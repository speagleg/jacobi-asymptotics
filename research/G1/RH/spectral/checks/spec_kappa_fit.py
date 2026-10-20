"""SPEC direction 3: leading coefficient of Delta y_n = y_n(kappa) - y_n(0) for lam_k = k^p + kappa, from the cached runs of
spec_kappa.py: least-squares fits of n^p Delta y = L + sum_i A_i n^{-e_i}, e_i in {p, 2p, 1, 3p, 1+p, ...}, several windows/orders.
Compared with the candidate L = -2(2-p) c kappa (identified from p = 0.6, kappa = 1)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np
from spec_common import run, c_p_mp, NMAX
from so_coeffs import coeffs
from so_fit import sequences
for p, kap in ((0.6, 1.0), (0.6, 0.5), (0.3, 1.0)):
    s = 2.0; K = 200*NMAX; k = np.arange(1, K + 1, dtype=np.float64)
    n, y = run(f"kappa_p{p}_s{s}_k{kap}", k**p + kap, p, s, 0.0, K)
    al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
    F = n**p*(y - y0); c = float(c_p_mp(p))
    E_all = sorted({round(i + j*p, 9) for i in range(4) for j in range(8)} - {0.0})
    est = []
    for J in (3, 4, 5, 6):
        E = E_all[:J]
        for lo in (100, 200, 400):
            m = n >= lo
            A = np.vstack([np.ones(m.sum())] + [n[m]**-e for e in E]).T
            est.append(np.linalg.lstsq(A, F[m], rcond=None)[0][0])
    est = np.array(est)
    print(f"p={p} kappa={kap}: L = {np.median(est):+.5f} (half-range {(est.max()-est.min())/2:.1e})   -2(2-p)c kappa = {-2*(2-p)*c*kap:+.5f}"
          f"   ratio {np.median(est)/(-2*(2-p)*c*kap):.4f}")
