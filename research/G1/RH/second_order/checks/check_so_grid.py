"""Plan 62, Goal 1 (NUMERICAL): first-order coefficients for sigma_{p,s} = sum_k k^{-s} delta_{k^{-p}} on a grid.

  n^p b_n / c(p) = 1 + d1/n + ...,   alpha_{n-1}/(2 b_n) = 1 + e1/n + ...  (repo pairing a_n/(2b_n), a_n = alpha_{n-1}),
  alpha_n/(2 b_n) = 1 + e1s/n + ...  (standard / Paper 2 pairing),
  gamma_N^2 / (c (N/2)^{-p}) = 1 + (k0 + k1 (-1)^N)/N + ...   (symmetric chain).
Fits: least squares in the exponents {1 + i + j p} (non-integer powers n^{-1-p} are present for p < 1, see SECOND.md
section 1), J = 4..7 terms, windows [f nmax, nmax], f = 0.1, 0.2, 0.3; the chain fit adds (-1)^N terms.  "fit" = half
the range of the 12 estimates; "dK" = |estimate(K) - estimate(2K)|.  Both are error ESTIMATES (Rule N), not bounds.
Conjectured closed forms printed alongside: d1 = -(s-1)/2, e1 = p/2, e1s = -p/2, k0 = -(s-1) - p/2,
k1 = -(p+2) a with a = (2s-2-p)/(2p) (symmetric Fisher-Hartwig exponent, RH.md section 5).
Run: PYTHONPATH=src python research/G1/RH/second_order/checks/check_so_grid.py  (coefficients cached in tmp/)."""
import sys
import os
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs
from so_fit import sequences, first_coef

PS = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0]
SS = [1.5, 2.0, 3.0, 4.0]
NMAX = 1600


def Kof(p):
    return 200 * NMAX if p < 1 else 100 * NMAX


def job(args):
    p, s, K = args
    coeffs(p, s, K, NMAX)
    return args


def analyse(p, s, K):
    al, b = coeffs(p, s, K, NMAX)
    n, y, er, es, N, g = sequences(p, al, b)
    out = {}
    out["d1"] = first_coef(n, y, p)
    out["e1"] = first_coef(n, er, p)
    out["e1s"] = first_coef(n[:-1], es[:-1], p)
    out["k0"] = first_coef(N, g, p, parity=True)
    out["k1"] = first_coef(N, g, p, parity=True, which=("par", 1))
    return out


if __name__ == "__main__":
    tasks = [(p, s, K) for p in PS for s in SS for K in (Kof(p), 2 * Kof(p))]
    with Pool(int(os.environ.get("NPROC", "8"))) as pool:
        for _ in pool.imap_unordered(job, tasks):
            pass
    print(f"nmax = {NMAX}; K = 100 nmax (p >= 1), 200 nmax (p < 1), and 2K. Value: median (fit half-range) [dK]\n")
    hdr = f"{'p':>4} {'s':>4} | {'d1':>30} {'conj':>7} | {'e1 (repo)':>30} {'e1s (std)':>30} | {'k0':>30} {'conj':>7} | {'k1':>30} {'conj':>7}"
    print(hdr); print("-" * len(hdr))
    for p in PS:
        for s in SS:
            A, B = analyse(p, s, Kof(p)), analyse(p, s, 2 * Kof(p))
            cell = lambda key: f"{B[key][0]:+.9f} ({B[key][1]:.1e}) [{abs(A[key][0]-B[key][0]):.0e}]"
            a = (2 * s - 2 - p) / (2 * p)
            print(f"{p:>4} {s:>4} | {cell('d1'):>30} {-(s-1)/2:+7.3f} | {cell('e1'):>30} {cell('e1s'):>30} | "
                  f"{cell('k0'):>30} {-(s-1)-p/2:+7.3f} | {cell('k1'):>30} {-(p+2)*a:+7.3f}")
