"""Plan 67 (E_plt1.md §8), NUMERICAL: test of Theorem E'.1 for 0 < p < 1 on the grid p in {0.3, 0.5, 0.7, 0.9},
s in {1.5, 2, 3}, n <= 1600 (Plan 62 machinery: so_coeffs.py, so_fit.py; atoms k <= K exactly + Gauss-Jacobi tail).

Predictions (Theorem E'.1), kappa_p := 2 p c(p) zeta(-p):
  y_n  := n^p b_n/c - 1          = -(s-1)/(2n)   + kappa_p n^{-1-p} + O(n^{-1-2p} + n^{-2}),
  ya_n := n^p alpha_n/(2c) - 1   = -(s-1+p)/(2n) + kappa_p n^{-1-p} + O(n^{-1-2p} + n^{-2}),
  es_n := alpha_n/(2b_n) - 1     = -p/(2n)       + 0 * n^{-1-p}     + O(n^{-1-2p} + n^{-2}),
  yg_n := n^p g_{n-1}/c - 1     = a/n            + kappa_p n^{-1-p} + O(n^{-1-2p} + n^{-2}),  a = (2s-2-p)/(2p)
  (E_plt1 Cor E'.6).
Fits: least squares in the exponents {1 + i + j p} (first J, J = 4..7), windows [f nmax, nmax], f = 0.1, 0.2, 0.3;
value = median of the 12 estimates, "fit" = half-range, "dK" = |value(K) - value(2K)| (Rule N: estimates, not bounds).
Also printed: the direct ratio n^{1+p}(y_n + (s-1)/(2n)) at n = 100, 200, 400, 800, 1600 (-> kappa_p, with a
correction O(n^{-p}) + O(n^{p-1})).
Run: PYTHONPATH=src python research/G1/RH/second_order/checks/check_e_plt1_num.py (coefficients cached in tmp/)."""
import sys
import os
from multiprocessing import Pool
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs, c_p_mp
from so_fit import first_coef

PS = [0.3, 0.5, 0.7, 0.9]
SS = [1.5, 2.0, 3.0]
NMAX = 1600
K1 = 200 * NMAX


def job(args):
    p, s, K = args
    coeffs(p, s, K, NMAX)
    return args


def seqs(p, s, K):
    mp.mp.dps = 40
    al, b = coeffs(p, s, K, NMAX)
    c = c_p_mp(p)
    n = np.arange(1, NMAX)                      # n = 1..nmax-1 (alpha_n needs index n)
    y = np.array([float(mp.mpf(int(k)) ** p * b[k - 1] / c - 1) for k in n])
    ya = np.array([float(mp.mpf(int(k)) ** p * al[k] / (2 * c) - 1) for k in n])
    es = np.array([float(al[k] / (2 * b[k - 1]) - 1) for k in n])
    # chain: g_{n-1} = -pi_n(0)/pi_{n-1}(0) via the continued fraction gamma (so_fit convention):
    gam = [mp.mpf(0)] * (2 * NMAX + 1)
    gam[1] = al[0]
    for m in range(1, NMAX):
        gam[2 * m] = b[m - 1] ** 2 / gam[2 * m - 1]
        gam[2 * m + 1] = al[m] - gam[2 * m]
    # g_m = gamma_{2m+1}^2 (SECOND §0); n^p g_{n-1}/c - 1 for n = 1..nmax-1
    yg = np.array([float(mp.mpf(int(k)) ** p * gam[2 * (k - 1) + 1] / c - 1) for k in n])
    return n, y, ya, es, yg, c


def coef(n, v, p, e):
    return first_coef(n, v, p, which=("", round(e, 9)))


def coef_given1(n, v, p, d1, Js=(3, 4, 5, 6), fracs=(0.1, 0.2, 0.3)):
    """the n^{-1-p} coefficient of v after subtracting the PROVED 1/n term d1/n: least squares in the exponents
    {1 + i + j p} minus {1} (first J of them), same windows; returns (median, half-range)."""
    n = np.asarray(n, float)
    w = np.asarray(v) - d1 / n
    E = [e for e in sorted({round(1 + i + j * p, 9) for i in range(9) for j in range(9)}) if abs(e - 1) > 1e-9]
    est = []
    for J in Js:
        for fr in fracs:
            m = n >= fr * n.max()
            n0 = n[m].min()
            A = np.vstack([(n0 / n[m]) ** e for e in E[:J]]).T
            co = np.linalg.lstsq(A, w[m], rcond=None)[0] * np.array([n0 ** e for e in E[:J]])
            est.append(co[E.index(round(1 + p, 9))])
    est = np.array(est)
    return float(np.median(est)), float((est.max() - est.min()) / 2)


if __name__ == "__main__":
    tasks = [(p, s, K) for p in PS for s in SS for K in (K1, 2 * K1)]
    with Pool(int(os.environ.get("NPROC", "8"))) as pool:
        for _ in pool.imap_unordered(job, tasks):
            pass
    tally = []
    print(f"nmax = {NMAX}; K = {K1} and 2K.  value (fit half-range) [dK];  kappa_p = 2 p c(p) zeta(-p)\n")
    for p in PS:
        c = float(c_p_mp(p))
        kap = 2 * p * c * float(mp.zeta(-p))
        print(f"p = {p}:  c(p) = {c:.12f},  zeta(-p) = {float(mp.zeta(-p)):.12f},  kappa_p = 2 p c zeta(-p) = {kap:+.9f}")
        for s in SS:
            A, B = seqs(p, s, K1), seqs(p, s, 2 * K1)
            n = B[0]
            rows = [("b:  d1 (n^-1)", 1, 1, -(s - 1) / 2), ("b:  n^-1-p", 1, 1 + p, kap),
                    ("a:  n^-1", 2, 1, -(s - 1 + p) / 2), ("a:  n^-1-p", 2, 1 + p, kap),
                    ("a/2b: n^-1", 3, 1, -p / 2), ("a/2b: n^-1-p", 3, 1 + p, 0.0),
                    ("g:  n^-1", 4, 1, (2 * s - 2 - p) / (2 * p)), ("g:  n^-1-p", 4, 1 + p, kap)]
            print(f"  s = {s}")
            for name, idx, e, pred in rows:
                vB = coef(n, B[idx], p, e)
                vA = coef(A[0], A[idx], p, e)
                tol = max(vB[1], abs(vA[0] - vB[0]), 1e-8)
                tally.append(abs(vB[0] - pred) <= tol)
                print(f"    {name:14s}: {vB[0]:+.7f} ({vB[1]:.1e}) [{abs(vA[0] - vB[0]):.0e}]   predicted {pred:+.7f}"
                      f"   |diff| = {abs(vB[0] - pred):.1e}  {'ok' if tally[-1] else 'OUTSIDE'}")
            for name, idx, d1 in (("b", 1, -(s - 1) / 2), ("a", 2, -(s - 1 + p) / 2), ("g", 4, (2 * s - 2 - p) / (2 * p))):
                vB, vA = coef_given1(n, B[idx], p, d1), coef_given1(A[0], A[idx], p, d1)
                tol = max(vB[1], abs(vA[0] - vB[0]), 1e-8)
                tally.append(abs(vB[0] - kap) <= tol)
                print(f"    {name}: n^-1-p coef. after subtracting the proved 1/n term: {vB[0]:+.7f} ({vB[1]:.1e}) "
                      f"[{abs(vA[0] - vB[0]):.0e}]   predicted {kap:+.7f}   |diff| = {abs(vB[0] - kap):.1e}  "
                      f"{'ok' if tally[-1] else 'OUTSIDE'}")
            yv = B[1]
            direct = [(m, (m ** (1 + p)) * (yv[m - 1] + (s - 1) / (2 * m))) for m in (100, 200, 400, 800, 1599)]
            print("    direct n^{1+p}(y_n + (s-1)/(2n)):  " + "  ".join(f"n={m}: {v:+.5f}" for m, v in direct))
        print()
    print(f"rows with |fit - prediction| <= max(fit half-range, dK, 1e-8): {sum(tally)}/{len(tally)}")
