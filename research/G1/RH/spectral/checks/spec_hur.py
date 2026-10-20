"""Route 1 test: shifted lattice nodes (k+d)^{-p}, weights (k+d)^{-s}, k>=1  (Hurwitz a = 1+d).
Prediction H: n^p b_n/c = 1 + [ -p*alpha/2 + p*zeta(0,a) ]/n + sum_{j>=1} C(2j,j) p c^j zeta(-jp,a) n^{-1-jp} + ..."""
import sys, numpy as np, mpmath as mp
from math import comb
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
p, s, d = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
NMAX = 1600; K = (200 if p < 1 else 100) * NMAX
al, b = coeffs(p, s, K, NMAX, d)
n, y, *_ = sequences(p, al, b); n = n.astype(float)
c = c_p_mp(p); a = 1 + d
eps = lambda j, aa: float(comb(2*j, j) * p * c**j * mp.zeta(-j*mp.mpf(p), aa))
d1H = -(s-1-p)/2 + p*float(mp.zeta(0, a))
E_all = sorted({round(1+i+j*p, 9) for i in range(8) for j in range(8)})
def fit(r, skip, tgt):
    E0 = [e for e in E_all if all(abs(e-x) > 1e-9 for x in skip)]
    out = []
    for J in (4, 5, 6, 7):
        E = E0[:J]
        for f in (0.1, 0.2, 0.3):
            m = n >= f*n.max(); n0 = n[m].min()
            A = np.vstack([(n0/n[m])**e for e in E]).T
            co = np.linalg.lstsq(A, r[m], rcond=None)[0]*np.array([n0**e for e in E])
            out.append(co[E.index(tgt)])
    out = np.array(out); return float(np.median(out)), float((out.max()-out.min())/2)
v1, h1 = fit(y, [], 1.0)
r = y - d1H/n
v, h = fit(r, [1.0], round(1+p, 9))
print(f"p={p} s={s} d={d} a={a}: d1 fit {v1:+.8f} ({h1:.1e}) pred {d1H:+.8f} | n^-1-p fit {v:+.7f} ({h:.1e}) "
      f"Hurwitz eps1(a) {eps(1,a):+.7f} diff {v-eps(1,a):+.1e} | unshifted eps1 {eps(1,1):+.7f}", flush=True)
if p < 1 and 1+2*p < 2.5:
    r2 = r - eps(1, a)*n**(-1-p)
    v, h = fit(r2, [1.0, round(1+p, 9)], round(1+2*p, 9))
    print(f"   n^-1-2p fit {v:+.7f} ({h:.1e}) Hurwitz eps2(a) {eps(2,a):+.7f} diff {v-eps(2,a):+.1e} | unshifted {eps(2,1):+.7f}", flush=True)
