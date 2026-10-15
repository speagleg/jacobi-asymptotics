"""Plan 66 (E_p1.md Theorem E1.6 via Proposition E1.4; NUMERICAL illustration, not part of the proofs).  Run from the repo root.
sigma_{1,3/2} vs TC (masses v_k = k^{k-1}e^{-k}/k! on 1/k) and sigma_{1,5/2} = x sigma_{1,3/2} vs x*TC, both members of each
pair through the SAME pipeline (atoms k <= K, Gauss-Legendre log-panel tail up to tend; the measure construction is that of
RH/checks/check_p1_tc.py, which validates the TC pipeline against TC's exact coefficients), long-double RKPW.
Printed: n^2 (r - 1) for r = b_n/b_n^ref, alpha_n/alpha_n^ref, g_n/g_n^ref (standard indexing, g from the chain
g_0 = alpha_0, g_m = alpha_m - b_m^2/g_{m-1}); Theorem E1.6 asserts all six tend to -1/24 = -0.041667 (O(1/n) corrections).
Also [2]: the pipeline's TC and x*TC against the exact formulas (check_e1_exact.py), as a bias estimate."""
import math
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs


def logv(t):
    t = np.asarray(t, float)
    small = t <= 1e3
    out = np.empty_like(t)
    ts = t[small]
    out[small] = (ts - 1) * np.log(ts) - ts - np.array([math.lgamma(v + 1) for v in ts])
    tl = t[~small]
    out[~small] = -1.5 * np.log(tl) - 0.5 * np.log(2 * np.pi) - 1 / (12 * tl) + 1 / (360 * tl ** 3)
    return out


def measure(kind, shift, K, tend, ratio=1.02, k=8):
    """kind 'sigma': masses k^{-3/2}; 'tc': v_k.  shift m: masses multiplied by x^m = k^{-m}."""
    kk = np.arange(1, K + 1, dtype=float)
    lw = ((-1.5 * np.log(kk)) if kind == "sigma" else logv(kk)) - shift * np.log(kk)
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(ratio))
    g, gw = np.polynomial.legendre.leggauss(k)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * g for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    lwT = ((-1.5 * np.log(T)) if kind == "sigma" else logv(T)) - shift * np.log(T)
    return DiscreteMeasure.from_atoms(1 / kk, np.exp(lw), tail=(1 / T, W * T * np.exp(lwT)))


def chain_g(al, b):
    g = [al[0]]
    for mm in range(1, len(al)):
        g.append(al[mm] - b[mm - 1] ** 2 / g[mm - 1])
    return np.array(g)


M, K = 1500, 200_000
nn = np.arange(1, M + 1, dtype=float)
exact = {0: (1 / (2 * nn + 1) + 1 / (2 * nn + 2), np.sqrt(1 / ((2 * nn) * (2 * nn + 1)))),
         1: (1 / (2 * nn + 2) + 1 / (2 * nn + 3), np.sqrt(1 / ((2 * nn + 1) * (2 * nn + 2))))}
NS = (50, 100, 200, 400, 800, 1499)
for shift, sname in ((0, "sigma_{1,3/2} vs TC"), (1, "sigma_{1,5/2} vs x*TC")):
    for tend in (1e12, 1e16):
        res = {}
        for kind in ("tc", "sigma"):
            jc = jacobi_coeffs(measure(kind, shift, K, tend), M + 2, prec="ld")
            res[kind] = (np.asarray(jc.a, float)[:M + 1], np.asarray(jc.b, float)[:M + 1])
        aT, bT = res["tc"]; aS, bS = res["sigma"]
        gT, gS = chain_g(aT, bT), chain_g(aS, bS)
        exa, exb = exact[shift]
        bias = max(abs(bT[n - 1] / exb[n - 1] - 1) for n in NS) , max(abs(aT[n] / exa[n - 1] - 1) for n in NS)
        print(f"{sname}, tend = {tend:.0e}:   [2] pipeline ref vs exact: max|b/b_ex - 1| = {bias[0]:.1e}, "
              f"max|alpha/alpha_ex - 1| = {bias[1]:.1e}")
        for n in NS:
            rb = n * n * (bS[n - 1] / bT[n - 1] - 1)
            ra = n * n * (aS[n] / aT[n] - 1)
            rg = n * n * (gS[n] / gT[n] - 1)
            print(f"    n = {n:5d}:  n^2(b/b_ref - 1) = {rb:+.5f}   n^2(alpha/alpha_ref - 1) = {ra:+.5f}   "
                  f"n^2(g/g_ref - 1) = {rg:+.5f}")
print(f"target -1/24 = {-1/24:+.5f}")
