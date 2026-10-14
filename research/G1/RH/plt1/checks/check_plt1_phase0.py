"""Plan 15 Phase 0 (NUMERICAL): pointwise Law P baseline for sigma_{p,s} = sum k^-s delta_{k^-p}, 0<p<1.
Exact atoms k <= K plus a log-panel midpoint Euler-Maclaurin tail (Gauss-Legendre); K-doubling (x4) stability."""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import c_p

def measure(p, s, K, tend=1e40, ratio=1.25, k=8):
    kk = np.arange(1, K + 1, dtype=float)
    x, w = kk ** (-p), kk ** (-s)
    tt, ww = np.polynomial.legendre.leggauss(k)
    u0, u1 = np.log(K + 0.5), np.log(tend)
    edges = np.arange(u0, u1, np.log(ratio)); edges = np.append(edges, u1)
    X, W = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        u = (a + b) / 2 + (b - a) / 2 * tt
        t = np.exp(u)
        X.append(t ** (-p)); W.append(t ** (-s) * t * (b - a) / 2 * ww)
    return DiscreteMeasure.from_atoms(np.concatenate([x] + X), np.concatenate([w] + W))

ns = np.array([25, 50, 100, 200, 400])
for p, s in ((0.5, 2.0), (0.5, 3.0), (0.75, 2.0)):
    out = {}
    for K in (20_000, 80_000):
        r = jacobi_coeffs(measure(p, s, K), ns[-1] + 1, prec='ld')
        b = np.sqrt(r.b2) if hasattr(r, 'b2') else r.b
        out[K] = (np.asarray(b), np.asarray(r.a))
    c = c_p(p)
    b, a = out[80_000]; b1, _ = out[20_000]
    print(f"p={p} s={s} c(p)={c:.6f}")
    for n in ns:
        i = n - 1
        dev = n ** p * b[i] / c - 1
        print(f"   n={n:4d}  n^p b/c - 1 = {dev:+.5e}  n*dev = {n*dev:+.4f}   n*(a/(2b)-1) = {n*(a[i]/(2*b[i])-1):+.4f}   K-stab {abs(b1[i]/b[i]-1):.1e}")
