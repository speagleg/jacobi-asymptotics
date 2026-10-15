"""Plan 66 (E_p1.md Theorem E1.10; NUMERICAL illustration of the remainder rate at p = 1, not part of the proof).
Coefficients of sigma_{1,s} from so_coeffs.py (atoms k <= K = 100 nmax + Gauss-Jacobi tail, binary128 RKPW; K -> 2K as the
truncation estimate).  Printed, with c(1) = 1/2:
  rb(n) = n^2 (2 n b_n - 1 + (s-1)/(2n)),   ra(n) = n^2 (n alpha_n - 1 + s/(2n)),
which Theorem E1.10 asserts to be bounded (both O(n^-2) remainders); and for the symmetric chain beta_N (gamma_N^2 of SECOND
Lemma 2.1: beta_{2m} = h_m, beta_{2m+1} = g_m)
  rc(N) = N^2 (N beta_N - 1 - (k0 + k1 (-1)^N)/N),  k0 = 1/2 - s (Thm E1.10), k1 = -3(s - 3/2) (CONJECTURE P62 at p = 1),
printed at an even N = 2n and an odd N = 2n - 1 (both should stay bounded; their limits differ: the (-1)^N part of the N^-2 term).
Period-4 test (an i^N term at order 1/N would put a (-1)^n term into b_n): the class means over N in [1180, 1220) of
N (N beta_N - 1) - k0 - k1(-1)^N for N = 0, 1, 2, 3 mod 4; classes 0 vs 2 and 1 vs 3 must agree up to the drift of the window
(they differ from each other only through the O(1/N) parity term).  Not a proof (Rule N)."""
import sys, os
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs

nmax = 800
for s in (1.25, 1.5, 2.0, 3.0, 4.5):
    rows = {}
    for K in (100 * nmax, 200 * nmax):
        al, b = coeffs(1.0, s, K, nmax)
        mp.mp.dps = 40
        S = mp.mpf(s)
        g = [al[0]]
        for m in range(1, nmax):
            g.append(al[m] - b[m - 1] ** 2 / g[m - 1])
        beta = {}
        for m in range(1, nmax - 1):
            beta[2 * m] = b[m - 1] ** 2 / g[m - 1]      # h_m
            beta[2 * m + 1] = g[m]
        k0, k1 = mp.mpf(1) / 2 - S, -3 * (S - mp.mpf(3) / 2)
        out = []
        for n in (50, 100, 200, 400, 798):
            N = mp.mpf(n)
            rb = N ** 2 * (2 * N * b[n - 1] - 1 + (S - 1) / (2 * N))
            ra = N ** 2 * (N * al[n] - 1 + S / (2 * N))
            rcs = []
            for NN in (2 * n, 2 * n - 1):
                rcs.append(mp.mpf(NN) ** 2 * (NN * beta[NN] - 1 - (k0 + k1 * (-1) ** NN) / NN))
            out.append((n, rb, ra, rcs[0], rcs[1]))
        spread = []
        for r in range(4):
            vals = [Nn * (Nn * beta[Nn] - 1) - k0 - k1 * (-1) ** Nn for Nn in range(1180, 1220) if Nn % 4 == r]
            spread.append(sum(vals) / len(vals))
        rows[K] = (out, spread)
    print(f"p = 1, s = {s}:")
    (o1, sp1), (o2, sp2) = rows[100 * nmax], rows[200 * nmax]
    for (n, rb, ra, rce, rco), (_, rb2, ra2, rce2, rco2) in zip(o1, o2):
        print(f"   n = {n:4d}: rb = {mp.nstr(rb, 8):>12}  ra = {mp.nstr(ra, 8):>12}   rc(2n) = {mp.nstr(rce, 8):>12}"
              f"  rc(2n-1) = {mp.nstr(rco, 8):>12}"
              f"   [K->2K: {mp.nstr(max(abs(rb - rb2), abs(ra - ra2), abs(rce - rce2), abs(rco - rco2)), 2)}]")
    print("   N(N beta_N - 1) - k0 - k1(-1)^N, class means over N in [1180,1220) for N = 0,1,2,3 mod 4: "
          + "  ".join(mp.nstr(v, 6) for v in sp1)
          + f"   |0 - 2| = {mp.nstr(abs(sp1[0] - sp1[2]), 2)}, |1 - 3| = {mp.nstr(abs(sp1[1] - sp1[3]), 2)}")
