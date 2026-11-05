"""Plan E3 (E3.md §6, NUMERICAL): the n^{-2} coefficient for 0 < p < 1 from the Plan 62 quad-precision coefficients
(so_coeffs; nmax = 1600, K = 200 nmax), after subtracting the terms determined analytically:
  y_n - d1/n - sum_k e_k n^{-1-kp},  d1 = -(s-1)/2,  e_k = binom(2k,k) p c^k zeta(-kp)  (k = 1: E_plt1 Thm E'.1; k = 2, 3: E3),
then least-squares fits over the remaining exponents {1 + i + j p} \\ {1, 1 + kp} (orders J = 4..7, windows f = 0.1..0.3).
Compared with d2(p, s) of Theorem E2.1 for generic p, and with d2 + e_j at p = 1/j (merged exponents)."""
import numpy as np
import mpmath as mp
from math import comb
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences

NMAX = 1600
d2f = lambda p, s: (p + 1) * (s - 1) ** 2 / (8 * p) - (p + 2) * (s - 1 - p) ** 2 / (8 * p * p) + (p + 1) / 12


def ek(p, k):
    return float(comb(2 * k, k) * p * c_p_mp(p) ** k * mp.zeta(-k * mp.mpf(p)))


def fit_n2(n, r, p, J, frac, skip):
    E = sorted({round(1 + i + j * p, 9) for i in range(8) for j in range(8)})
    E = [e for e in E if all(abs(e - x) > 1e-9 for x in skip)][:J]
    assert 2.0 in E
    m = n >= frac * n.max()
    n0 = n[m].min()
    A = np.vstack([(n0 / n[m]) ** e for e in E]).T
    co = np.linalg.lstsq(A, r[m], rcond=None)[0] * np.array([n0 ** e for e in E])
    return co[E.index(2.0)]


print(f"{'p':>5} {'s':>4} | {'n^-2 coeff (fit)':>17} {'half-range':>10} | {'prediction':>12} | {'diff':>9} | note")
for p, S in [(0.75, (1.5, 2.0, 3.0, 4.0)), (0.6, (2.0, 3.0)), (0.5, (2.0, 3.0))]:
    for s in S:
        al, b = coeffs(p, s, 200 * NMAX, NMAX)
        n, y, *_ = sequences(p, al, b)
        n = n.astype(float)
        ks = [k for k in (1, 2, 3) if abs(1 + k * p - 2) > 1e-9 and 1 + k * p < 2.5]
        r = y + (s - 1) / (2 * n)
        for k in ks:
            r = r - ek(p, k) * n ** (-1 - k * p)
        skip = [1.0] + [1 + k * p for k in ks]
        est = np.array([fit_n2(n, r, p, J, f, skip) for J in (4, 5, 6, 7) for f in (0.1, 0.2, 0.3)])
        v, hr = float(np.median(est)), float((est.max() - est.min()) / 2)
        jm = [k for k in (1, 2, 3) if abs(k * p - 1) < 1e-9]
        pred = d2f(p, s) + (ek(p, jm[0]) if jm else 0.0)
        note = f"merged: d2 + e_{jm[0]} (= {ek(p, jm[0]):+.6f})" if jm else "generic: d2"
        print(f"{p:5} {s:4} | {v:+17.7f} {hr:10.1e} | {pred:+12.7f} | {v - pred:+9.1e} | {note}")

print()
print("p > 1 (Theorem E3.1): n^{-1-p} coefficient after subtracting d1/n and d2/n^2 (both proved), vs kappa_p = 2 p c zeta(-p)")
print(f"{'p':>5} {'s':>4} | {'n^-1-p coeff (fit)':>18} {'half-range':>10} | {'kappa_p':>12} | {'diff':>9}")
for p, S in [(1.25, (2.0, 3.0)), (1.5, (1.5, 2.0, 3.0, 4.0, 5.0))]:
    for s in S:
        al, b = coeffs(p, s, 100 * NMAX, NMAX)
        n, y, *_ = sequences(p, al, b)
        n = n.astype(float)
        r = y + (s - 1) / (2 * n) - d2f(p, s) / n ** 2
        E_all = sorted({round(1 + i + j * p, 9) for i in range(8) for j in range(8)})
        E_all = [e for e in E_all if e not in (1.0, 2.0)]
        tgt = round(1 + p, 9)
        est = []
        for J in (4, 5, 6, 7):
            E = E_all[:J]
            for f in (0.1, 0.2, 0.3):
                m = n >= f * n.max()
                n0 = n[m].min()
                A = np.vstack([(n0 / n[m]) ** e for e in E]).T
                co = np.linalg.lstsq(A, r[m], rcond=None)[0] * np.array([n0 ** e for e in E])
                est.append(co[E.index(tgt)])
        est = np.array(est)
        v, hr = float(np.median(est)), float((est.max() - est.min()) / 2)
        kp = ek(p, 1)
        print(f"{p:5} {s:4} | {v:+18.7f} {hr:10.1e} | {kp:+12.7f} | {v - kp:+9.1e}")
