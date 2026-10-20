import sys, numpy as np, mpmath as mp
from math import comb
from pathlib import Path
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
from so_coeffs import c_p_mp
from so_fit import sequences
from scipy.special import roots_jacobi
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
NMAX = 1600
CACHE = Path(__file__).resolve().parents[5] / 'tmp' / 'spectral_cache'
CACHE.mkdir(parents=True, exist_ok=True)
def run(tag, lam, p, s, tail_delta, K):
    """atoms 1/lam_k, weights lam_k^{-s/p} (k<=K), pure-power continuum tail of (k+tail_delta)^p beyond K+1/2."""
    f = CACHE / f"{tag}.txt"; mp.mp.dps = 40
    if not f.exists():
        x, w = 1/lam, lam**(-s/p)
        beta = (s-1)/p - 1; u, wu = roots_jacobi(NMAX+8, 0.0, beta); X = (K+0.5+tail_delta)**(-p)
        mu = DiscreteMeasure.from_atoms(x, w, tail=(X*(1+u)/2, wu*(X/2)**(beta+1)/p))
        jc = jacobi_rkpw(mu, NMAX+1, prec="q")
        with open(f, "w") as fh:
            for a_, b2 in zip(jc.a[:NMAX], jc.b2[:NMAX]): fh.write(f"{mp.nstr(a_, 36)} {mp.nstr(mp.sqrt(b2), 36)}\n")
    rows = [l.split() for l in open(f)]
    al = np.array([mp.mpf(r[0]) for r in rows], dtype=object); b = np.array([mp.mpf(r[1]) for r in rows], dtype=object)
    n, y, *_ = sequences(p, al, b)
    return n.astype(float), y
def fit(n, r, p, skip, tgt, fr=(0.1, 0.2, 0.3), Js=(4, 5, 6, 7)):
    E_all = sorted({round(1+i+j*p, 9) for i in range(8) for j in range(8)})
    E0 = [e for e in E_all if all(abs(e-x) > 1e-9 for x in skip)]; out = []
    for J in Js:
        E = E0[:J]
        for f_ in fr:
            m = n >= f_*n.max(); n0 = n[m].min()
            A = np.vstack([(n0/n[m])**e for e in E]).T
            out.append((np.linalg.lstsq(A, r[m], rcond=None)[0]*np.array([n0**e for e in E]))[E.index(round(tgt, 9))])
    out = np.array(out); return float(np.median(out)), float((out.max()-out.min())/2)
