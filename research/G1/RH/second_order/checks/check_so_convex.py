"""Plan 62 (NUMERICAL support for hypothesis (CVX), SECOND.md section 3.3): s -> log h_n(sigma_{p,s}) is convex.

(CVX) together with the fixed-s bound L_n(s) = log n + O(1) (QLP-Lambda + Law P) would make Theorem 3.8 unconditional:
for convex log h_n, -L_n(s0) <= (log h_n(s1) - log h_n(s0))/(s1 - s0) <= -L_n(s1).
[1] exact (mpmath, Hankel determinants of zeta values, dps 300): second differences of log h_n at
    s = 1.5, 2, ..., 4 (step 0.5), n in {1, 2, 4, 8}, p in {1/2, 1, 2}.
[2] from the coefficient data of check_so_grid.py (2K runs): log h_n(s) = log mass(s) + 2 sum_{j<=n} log b_j(s) at
    s = 1.5, 2, 3, 4; the two second divided differences, for n up to 1600 (minimum over n reported)."""
import sys
import os
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("[1] exact small n: second differences of log h_n(s), s = 1.5, 2.0, ..., 4.0")
mp.mp.dps = 300


def logh(n, p, s):
    def D(m):
        if m == 0:
            return mp.mpf(1)
        return mp.det(mp.matrix([[mp.zeta(s + p * (i + j)) for j in range(m)] for i in range(m)]))
    return mp.log(D(n + 1) / D(n))


for p in (mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2)):
    for n in (1, 2, 4, 8):
        v = [logh(n, p, mp.mpf(s) / 2) for s in range(3, 9)]
        sd = [v[i - 1] - 2 * v[i] + v[i + 1] for i in range(1, len(v) - 1)]
        print(f"   p={mp.nstr(p, 2):>3} n={n}: {[mp.nstr(x, 4) for x in sd]}  all > 0: {all(x > 0 for x in sd)}")

print("\n[2] grid data: min over n <= 1600 of the second divided differences of log h_n on s = 1.5, 2, 3, 4")
from so_coeffs import coeffs, measure
from check_so_grid import PS, SS, Kof, NMAX
mp.mp.dps = 40
for p in PS:
    K = 2 * Kof(p)
    L = []
    for s in SS:
        al, b = coeffs(p, s, K, NMAX)
        mass = float(np.sum(measure(p, s, K, NMAX + 8).weights))
        lb = np.cumsum([2 * float(mp.log(x)) for x in b])
        L.append(np.log(mass) + lb)
    L = np.array(L)
    s = np.array(SS)
    dd1 = ((L[2] - L[1]) / (s[2] - s[1]) - (L[1] - L[0]) / (s[1] - s[0])) / (s[2] - s[0])
    dd2 = ((L[3] - L[2]) / (s[3] - s[2]) - (L[2] - L[1]) / (s[2] - s[1])) / (s[3] - s[1])
    n = np.arange(1, NMAX + 1)
    print(f"   p={p}: min dd[1.5,2,3] = {dd1.min():.4e} (at n={n[dd1.argmin()]}),  min dd[2,3,4] = {dd2.min():.4e} "
          f"(at n={n[dd2.argmin()]});  values at n=1600: {dd1[-1]:.4e}, {dd2[-1]:.4e}")
