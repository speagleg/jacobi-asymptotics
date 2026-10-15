"""Plan 62 (NUMERICAL tests of exact statements in SECOND.md section 3):

[A] Christoffel product identity (Prop. 3.1, exact):  prod_{m<=n} (b_m(s+p)/b_m(s))^2 = gamma_{2n+1}^2(s) / gamma_1^2(s),
    where gamma is the symmetric chain of sigma_{p,s} and b(s+p) is computed INDEPENDENTLY from sigma_{p,s+p}.
[B] Its limit (Thm 3.2):  S_n := sum_{m<=n} log(b_m(s+p)/b_m(s)) + (p/2) log n  ->  (1/2) log(c(p) zeta(s)/zeta(s+p)),
    and n^p gamma_{2n+1}^2 / c -> 1.
[C] Corollary 3.3: d1(s+p) - d1(s) = -p/2 (fits from check_so_grid's data).
[D] Tricomi-Carlitz comparison at p = 1 (Prop. 3.5):  T_n := sum_{j<=n} log(b_j(sigma_{1,3/2}) / b_j^TC)
    -> -(1/2) log(zeta(3/2)/sqrt(2 pi)) with rate O(1/n);  b_j^TC = 1/sqrt(2j(2j+1)) (RH_p1.md section 0).
Data: the 2K runs of check_so_grid.py (cached in tmp/; run that script first)."""
import sys
import os
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences, first_coef
from check_so_grid import Kof, NMAX

mp.mp.dps = 40
PAIRS = [(0.5, 1.5), (1.0, 2.0), (1.0, 3.0), (1.5, 1.5), (2.0, 2.0)]


def chain(alpha, b):
    nmax = len(b)
    g = [mp.mpf(0)] * (2 * nmax + 1)
    g[1] = alpha[0]
    for m in range(1, nmax):
        g[2 * m] = b[m - 1] ** 2 / g[2 * m - 1]
        g[2 * m + 1] = alpha[m] - g[2 * m]
    return g


print("[A]-[C] Christoffel shift s -> s + p")
for p, s in PAIRS:
    K = 2 * Kof(p)
    al, b = coeffs(p, s, K, NMAX)
    al2, b2 = coeffs(p, s + p, K, NMAX)
    g = chain(al, b)
    c = c_p_mp(p)
    lim = mp.log(c * mp.zeta(s) / mp.zeta(s + p)) / 2
    print(f" p={p} s={s} -> s+p={s+p}:  limit (1/2)log(c zeta(s)/zeta(s+p)) = {mp.nstr(lim, 12)}")
    logprod = mp.mpf(0)
    for n in range(1, NMAX):
        logprod += 2 * mp.log(b2[n - 1] / b[n - 1])
        if n in (1, 10, 100, 400, 800, 1599):
            ident = logprod - mp.log(g[2 * n + 1] / g[1])
            S = logprod / 2 + mp.mpf(p) / 2 * mp.log(n)
            print(f"   n={n:5d}: [A] log(prod) - log(g_(2n+1)/g_1) = {mp.nstr(ident, 3):>10}   "
                  f"[B] n^p g_(2n+1)/c - 1 = {mp.nstr(mp.mpf(n) ** p * g[2 * n + 1] / c - 1, 6):>12}   "
                  f"S_n - limit = {mp.nstr(S - lim, 6):>12}")
    n_, y, *_ = sequences(p, al, b)
    n2_, y2, *_ = sequences(p, al2, b2)
    d, dd = first_coef(n_, y, p)[:2]
    d2, dd2 = first_coef(n2_, y2, p)[:2]
    print(f"   [C] d1(s) = {d:+.9f} ({dd:.0e}), d1(s+p) = {d2:+.9f} ({dd2:.0e}), difference = {d2 - d:+.9f}  vs -p/2 = {-p/2:+.4f}")

print("\n[D] Tricomi-Carlitz comparison, p = 1, s = 3/2")
al, b = coeffs(1.0, 1.5, 2 * Kof(1.0), NMAX)
lim = -mp.log(mp.zeta(1.5) / mp.sqrt(2 * mp.pi)) / 2
print(f"   predicted limit -(1/2)log(zeta(3/2)/sqrt(2pi)) = {mp.nstr(lim, 12)}")
T = mp.mpf(0)
for j in range(1, NMAX + 1):
    T += mp.log(b[j - 1] * mp.sqrt(2 * j * (2 * j + 1)))
    if j in (10, 50, 100, 200, 400, 800, 1600):
        print(f"   n={j:5d}: T_n - limit = {mp.nstr(T - lim, 6):>12},  n (T_n - limit) = {mp.nstr(j * (T - lim), 6)},"
              f"  n^2 (b_n/b_n^TC - 1) = {mp.nstr(j**2 * (b[j-1] * mp.sqrt(2*j*(2*j+1)) - 1), 6)}")
