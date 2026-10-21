"""Route 1 test 2: pure lattice sigma_{p,s} with ONE node moved: k = m0 -> lam^{1/p} = m0 + h (node (m0+h)^{-p}, weight (m0+h)^{-s}).
Node-zeta prediction: Z(-j) changes by (m0+h)^{jp} - m0^{jp}; so d1 unchanged and eps_j changes by C(2j,j) p c^j [(m0+h)^{jp} - m0^{jp}]."""
import sys, numpy as np, mpmath as mp
from math import comb
from pathlib import Path
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
from so_coeffs import c_p_mp
from so_fit import sequences
from scipy.special import roots_jacobi
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
p, s, m0, h = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
NMAX = 1600; K = 200 * NMAX
from spec_common import run
k = np.arange(1, K + 1, dtype=np.float64); k[m0 - 1] = m0 + h
n, y = run(f"pert_p{p}_s{s}_m{m0}_h{h}", k**p, p, s, 0.0, K); c = c_p_mp(p)

dZ = lambda j: (m0 + h) ** (j * p) - m0 ** (j * p)
eps = lambda j: float(comb(2*j, j) * p * c**j * (mp.zeta(-j*mp.mpf(p)) + dZ(j)))
E_all = sorted({round(1+i+j*p, 9) for i in range(8) for j in range(8)})
def fit(r, skip, tgt):
    E0 = [e for e in E_all if all(abs(e-x) > 1e-9 for x in skip)]; out = []
    for J in (4, 5, 6, 7):
        E = E0[:J]
        for fr in (0.1, 0.2, 0.3):
            m = n >= fr*n.max(); n0 = n[m].min()
            A = np.vstack([(n0/n[m])**e for e in E]).T
            out.append((np.linalg.lstsq(A, r[m], rcond=None)[0]*np.array([n0**e for e in E]))[E.index(tgt)])
    out = np.array(out); return float(np.median(out)), float((out.max()-out.min())/2)
v1, h1 = fit(y, [], 1.0)
v, hh = fit(y + (s-1)/(2*n), [1.0], round(1+p, 9))
print(f"p={p} s={s} node {m0}->{m0+h}: d1 fit {v1:+.8f} ({h1:.1e}) pred {-(s-1)/2:+.8f} | n^-1-p fit {v:+.7f} ({hh:.1e}) "
      f"pred eps1 {eps(1):+.7f} diff {v-eps(1):+.1e} | unperturbed {float(2*p*c*mp.zeta(-p)):+.7f}", flush=True)
from spec_common import Checks
C_ = Checks(); C_.check("d1", v1, -(s-1)/2, max(3*h1, 1e-5)); C_.check("eps1", v, eps(1), max(3*hh, 1e-4)); C_.finish()
