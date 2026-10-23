"""REFIT: validation of refit_data.py (NUMERICAL).
(1) JZC_W2 case P15a (p = 3/2, delta = -1/4, kappa = 1/2, s = 11/5, nmax = 1200, K = 100 nmax): refit_data (u-panel far tail)
    against w2_data TAIL 3 (Gauss-Jacobi-in-x far tail, cached in tmp/w2): max |y_refit - y_w2| over n <= 1200.
(2) K-independence for a non-kappa family (A: lam = k^1.5 - 0.75 k^0.5, s = 2): K = 50 nmax vs 100 nmax, nmax = 1600."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
import refit_data as RD, w2_data as W2D, w2_common as W2C_
RD_W2C = W2D.W2C
def w2(*a, **k):
    W2D.W2C = W2C_.W2C
    try: return W2D.data(*a, **k)
    finally: W2D.W2C = RD_W2C
for f in (__file__, RD.__file__, W2D.__file__): W2C_.provenance(f)
n, ya = w2('3/2', '-1/4', '1/2', '11/5', nmax=1200, Kfac=100)
print("w2_data file:", os.path.basename(W2D.LAST))
fam = RD.fam_kappa(mp.mpf(3)/2, -mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(11)/5)
n, yb = RD.run('val_P15a', 1.5, fam, K=120000, nmax=1200)
d = [abs(a - b) for a, b in zip(ya, yb)]
print(f"(1) P15a: max |y_refit - y_w2| = {mp.nstr(max(d), 3)}; at n = 300, 600, 1200: {[mp.nstr(d[k-1], 3) for k in (300, 600, 1200)]}")
ok1 = max(d) < mp.mpf(10)**-26
famA = RD.fam_A(1.5, -0.75, 2.0)
n, y1 = RD.run('val_A15m_K50', 1.5, famA, K=80000)
n, y2 = RD.run('wA_p1.5_a-0.75_s2.0', 1.5, famA, K=160000)
d2 = [abs(a - b) for a, b in zip(y1, y2)]
print(f"(2) A15m K = 50 vs 100 nmax: max |dy| = {mp.nstr(max(d2), 3)}; n^4 |dy| at n = 400, 800, 1600: "
      f"{[mp.nstr(d2[k-1]*k**4, 3) for k in (400, 800, 1600)]}")
ok2 = max(d2) < mp.mpf(10)**-24
print("VALIDATION", "PASSED" if ok1 and ok2 else "FAILED", flush=True)
