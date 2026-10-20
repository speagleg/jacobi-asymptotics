"""SPEC §3.2 (NUMERICAL): Lemma U and the ratio asymptotics behind S2, from the cached coefficients (36 digits).
sigma = sigma_{0.6,2} (Plan 62 cache), sigma' = sigma minus the atom k0 = 30 (spectral cache, spec_remove.py).
Orthonormal recurrence for sigma' at x0 = k0^{-p}: b_{j+1} P_{j+1} = (x0 - alpha_j) P_j - b_j P_{j-1}, P_0 = mass'^{-1/2};
F(m) = log(1 + w0 sum_{j<m} P_j^2);  asserted: F(n+1) - 2F(n) + F(n-1) = log b_n^2(sigma) - log b_n^2(sigma') (Lemma U, exact up to
the tail/precision of the caches); printed: P_n/P_{n-1} vs r(u_n) = (1 + sqrt(1-u))^2/u, u_n = 4c b... = 4 b_n/x0 and = 4c(k0/n)^p."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
from pathlib import Path
import mpmath as mp
from so_coeffs import coeffs, c_p_mp
mp.mp.dps = 40
p, s, k0, K, NMAX = 0.6, 2.0, 30, 320000, 1600
CACHE = Path(__file__).resolve().parents[5] / 'tmp' / 'spectral_cache'
rows = [l.split() for l in open(CACHE / f"rm_p{p}_s{s}_k{k0}.txt")]
al1 = [mp.mpf(r[0]) for r in rows]; b1 = [mp.mpf(r[1]) for r in rows]      # sigma': alpha_0.., b_1..
al0, b0 = coeffs(p, s, K, NMAX)                                            # sigma
x0 = mp.mpf(k0) ** (-p); w0 = mp.mpf(k0) ** (-s)
beta = (s - 1) / p - 1; X = (K + 0.5) ** (-p)
mass = mp.zeta(s) - w0                                                       # sum_{k != k0} k^{-s} (atoms + tail = exact sum to O(K^-3))
P = [1 / mp.sqrt(mass)]
P.append(((x0 - al1[0]) * P[0]) / b1[0])
for j in range(1, NMAX - 1):
    P.append(((x0 - al1[j]) * P[j] - b1[j - 1] * P[j - 1]) / b1[j])
S = mp.mpf(0); F = []
for j in range(len(P)):
    F.append(mp.log(1 + w0 * S)); S += P[j] ** 2                            # F[m] = log(1 + w0 K'_{m-1}), K'_{-1} = 0
c = c_p_mp(p); worst = 0
print(f"{'n':>5} {'Delta^2 F':>16} {'log b^2 ratio':>16} {'diff':>9} | {'P_n/P_n-1':>12} {'r(4c(k0/n)^p)':>14}")
for n in (100, 200, 400, 800, 1200, 1500):
    d2F = F[n + 1] - 2 * F[n] + F[n - 1]
    lb = 2 * mp.log(b0[n - 1] / b1[n - 1])
    worst = max(worst, abs(d2F - lb) / abs(lb))
    u = 4 * c * (mp.mpf(k0) / n) ** p
    r = (1 + mp.sqrt(1 - u)) ** 2 / u
    print(f"{n:5d} {mp.nstr(d2F, 12):>16} {mp.nstr(lb, 12):>16} {mp.nstr(abs(d2F - lb) / abs(lb), 2):>9} | {mp.nstr(P[n] / P[n - 1], 8):>12} {mp.nstr(r, 8):>14}")
print("worst relative difference (Lemma U):", mp.nstr(worst, 3)); assert worst < 1e-8
print("ALL ASSERTIONS PASSED")
