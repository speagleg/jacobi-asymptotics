"""Plan 65 (E_pgt1.md Theorem E.1; NUMERICAL illustration of the remainder rate, not part of the proof).
Coefficients of sigma_{p,s} from so_coeffs.py (atoms k <= K = 100 nmax + Gauss-Jacobi tail, binary128 RKPW; K -> 2K as the
truncation estimate).  Printed: the second-order residuals
  rb(n) = n^2 (n^p b_n/c - 1 + (s-1)/(2n)),  ra(n) = n^2 (n^p alpha_n/(2c) - 1 + (s-1+p)/(2n)),
  rg(n) = n^2 (n^p g_{n-1}/c - 1 - a/n),  a = (2s-2-p)/(2p),  g from the chain g_0 = alpha_0, g_m = alpha_m - b_m^2/g_{m-1},
which Theorem E.1 / Corollary E.6 assert to be bounded (all three O(n^-2))."""
import sys, os
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs, c_p_mp

nmax = 800
for p, s in [(1.5, 2.0), (2.0, 3.0), (3.0, 2.5), (1.25, 4.0)]:
    rows = {}
    for K in (100 * nmax, 200 * nmax):
        al, b = coeffs(p, s, K, nmax)
        mp.mp.dps = 40
        c = c_p_mp(p); P = mp.mpf(p); S = mp.mpf(s); a = (2 * S - 2 - P) / (2 * P)
        g = [al[0]]
        for m in range(1, nmax):
            g.append(al[m] - b[m - 1] ** 2 / g[m - 1])
        out = []
        for n in (50, 100, 200, 400, 799):
            N = mp.mpf(n)
            rb = N ** 2 * (N ** P * b[n - 1] / c - 1 + (S - 1) / (2 * N))
            ra = N ** 2 * (N ** P * al[n] / (2 * c) - 1 + (S - 1 + P) / (2 * N))
            rg = N ** 2 * (N ** P * g[n - 1] / c - 1 - a / N)
            out.append((n, rb, ra, rg))
        rows[K] = out
    print(f"p = {p}, s = {s}:")
    for (n, rb, ra, rg), (_, rb2, ra2, rg2) in zip(rows[100 * nmax], rows[200 * nmax]):
        print(f"   n = {n:4d}: rb = {mp.nstr(rb, 8):>12}  ra = {mp.nstr(ra, 8):>12}  rg = {mp.nstr(rg, 8):>12}   "
              f"[K->2K: {mp.nstr(max(abs(rb - rb2), abs(ra - ra2), abs(rg - rg2)), 2)}]")
