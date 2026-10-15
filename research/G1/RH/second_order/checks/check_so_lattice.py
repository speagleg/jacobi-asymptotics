"""Plan 62 (NUMERICAL test of a HEURISTIC, SECOND.md section 4.1): shifted lattices.

Measure: sum_{k>=1} (k+delta)^{-s} delta_{(k+delta)^{-p}}  (first lattice index j0 = 1 + delta).
Heuristic "effective index": b_n ~ c(p) (n + alpha_x/2 + j0 - 1/2)^{-p}, alpha_x = (s-1-p)/p, i.e.
    d1 = -p (alpha_x/2 + j0 - 1/2) = -(s-1)/2 - p*delta,   e1 (repo pairing) = p/2 unchanged.
Exact support at p = 1, s = 3/2 (not computed here): Tricomi-Carlitz(alpha) has atoms 1/(k+alpha), k >= 0 (j0 = alpha),
masses asymptotically prop. to (k+alpha)^{-3/2}(1 + O(1/k)), and chain gamma_N^2 = N/((N+alpha)(N+alpha-1)), whence
d1 = 3/4 - alpha = -(1/2)/2 - (alpha - 1): the same formula.
nmax = 800; K = 100 nmax (p >= 1), 200 nmax (p < 1), and 2K."""
import sys
import os
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs
from so_fit import sequences, first_coef

NMAX = 800
CASES = [(p, 2.0, d) for p in (0.5, 1.0, 3.0) for d in (-0.5, 0.0, 0.5)]


def Kof(p):
    return 200 * NMAX if p < 1 else 100 * NMAX


def job(a):
    p, s, d, K = a
    coeffs(p, s, K, NMAX, d)


if __name__ == "__main__":
    with Pool(int(os.environ.get("NPROC", "8"))) as pool:
        list(pool.imap_unordered(job, [(p, s, d, K) for p, s, d in CASES for K in (Kof(p), 2 * Kof(p))]))
    print(f"nmax = {NMAX}. value (fit half-range) [K vs 2K]; predicted d1 = -(s-1)/2 - p*delta, e1 = p/2\n")
    for p, s, d in CASES:
        res = []
        for K in (Kof(p), 2 * Kof(p)):
            al, b = coeffs(p, s, K, NMAX, d)
            n, y, er, es, N, g = sequences(p, al, b)
            res.append((first_coef(n, y, p)[:2], first_coef(n, er, p)[:2]))
        (dA, eA), (dB, eB) = res
        print(f"p={p:<4} s={s} delta={d:+.1f}:  d1 = {dB[0]:+.8f} ({dB[1]:.0e}) [{abs(dA[0]-dB[0]):.0e}]  pred {-(s-1)/2 - p*d:+.4f}"
              f"   e1 = {eB[0]:+.8f} ({eB[1]:.0e}) [{abs(eA[0]-eB[0]):.0e}]  pred {p/2:+.4f}")
