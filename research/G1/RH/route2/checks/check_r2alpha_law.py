"""Plan 52 (NUMERICAL): the law for s >= 1 + 2p (alpha_x >= 1), p = 2, s = 5, 6 (alpha_x = 1, 3/2), and the chain sequence
g_n of the Christoffel transfer (ROUTE2_alpha.md §§2-4). Psi = 1 and Psi = exp sqrt(log(k + e)) (H_an holds).
Index convention as check_r2_coeff.py: b_n := sqrt(b2[n-1]); a_n := a[n].  Columns:
  nB := n (n^p b_n / c(p) - 1)        (law with rate: bounded; Corollary B_all predicts O(1/n));
  E  := n (a[n]/(2 sqrt(b2[n])) - 1)   (pairing of check_fine.py; pure-power baseline e1 = p/2 = 1);
  e  := (1/2) log(g_n/h_n)  with g_n = -P_{n+1}(0)/P_n(0), h_n = al_n - g_n computed from sigma_s (Lemma CT); Lemma CS / CS-r
        says e -> 0 and, under an O(1/n) law, e = O(n^{-1/2}); columns sqrt(n)*e and n*e (the data suggest e = O(1/n)).
  dB := nB(s) - nB(s - p): the 1/n coefficient shift under one Christoffel step (Remark SH-1/n, §4.3, predicts -> -p/2 = -1).
long double RKPW, K = 60000, 120000, 240000 (truncation check).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan52/research/G1/RH/route2/checks/check_r2alpha_law.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

p = 2.0; c = c_p(p); NS = (100, 200, 400, 800); NMAX = 802
PSI = {"1": lambda k: 0.0 * k, "sqrtlog": lambda k: np.sqrt(np.log(k + np.e))}


def coeffs(K, s, kind):
    k = np.arange(1, K + 1, dtype=float); lw = -s * np.log(k) + PSI[kind](k); lw = lw - lw.max()
    r = jacobi_coeffs(DiscreteMeasure(k ** -p, np.exp(lw)), NMAX, prec="ld")
    return np.asarray(r.a, np.longdouble), np.asarray(r.b2, np.longdouble)


def chain(a, b2):
    g = np.empty_like(a); g[0] = a[0]
    for i in range(1, len(a)):
        g[i] = a[i] - b2[i - 1] / g[i - 1]
    return g, a - g


for kind in ("1", "sqrtlog"):
    for K in (60000, 120000, 240000):
        nbs = {}
        for s in (3.0, 4.0, 5.0, 6.0):
            a, b2 = coeffs(K, s, kind); g, h = chain(a, b2)
            nb = {n: n * (n ** p * np.sqrt(b2[n - 1]) / c - 1) for n in NS}
            rows = []
            for n in NS:
                E = n * (a[n] / (2 * np.sqrt(b2[n])) - 1); e = 0.5 * np.log(g[n] / h[n])
                dB = "" if (s - p) not in nbs else f" dB={float(nb[n] - nbs[s - p][n]):+.4f}"
                rows.append(f"n={n}: nB={float(nb[n]):+.4f} E={float(E):+.4f} sqrt(n)e={float(np.sqrt(n) * e):+.4f} n*e={float(n * e):+.4f}{dB}")
            print(f"Psi={kind} K={K} s={s} (alpha_x={(s - 1 - p) / p:+.2f}, min g={float(g.min()):.3g}, min h(n>=1)={float(h[1:].min()):.3g}):\n  "
                  + "\n  ".join(rows), flush=True)
            nbs[s] = nb
