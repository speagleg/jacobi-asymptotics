"""Paper 2, Section 9, Table 2 (numerical illustration; floating point, not certified).

Measure sigma_{p,s,l} = sum_k k^{-s} l(k) delta_{k^{-p}} for l(k) = exp(sqrt(log(k + e))) and l = 1.
Model of the measure: atoms k = 1..K exactly, plus a Gauss-Legendre quadrature (log-panels of ratio 1.02, 8 nodes per
panel) of the continuum tail int_{K+1/2}^{T_END} t^{-s} l(t) delta_{t^{-p}} dt.  The tail is essential: the hard-edge
scale of degree n is k ~ n^{1+2/p}, far beyond K for p <= 1 (without it the truncated measure has a soft edge).
Recurrence coefficients: RKPW (toolkit C kernel, long double).

Paper convention (Section 2): x P_n = P_{n+1} + a_n P_n + b_n^2 P_{n-1}, b_n^2 = h_n/h_{n-1}.
Toolkit convention (jacobi_asym JacobiCoeffs): a[i] = diagonal entry at P_i, b2[i] = h_{i+1}/h_i.
Hence a_n = a[n] and b_n = sqrt(b2[n-1]).
Printed columns, for each n:
  B(l)  := n (n^p b_n / c(p) - 1)   for l = exp sqrt log(k+e)
  B(1)  := the same for l = 1 (pure power)
  A(l)  := n (a_n / (2 b_n) - 1)    for l = exp sqrt log(k+e)
  A(1)  := the same for l = 1
and the truncation spread (max - min over the runs listed in RUNS[p]) of each column.

Also printed: theta_n/2 with theta_n := L'(log n), L(xi) = sqrt(log(e^xi + e)) (the quantity in the conjecture of
Section 10.1), to compare with B(l) - B(1).
Run: /mnt/c/Users/gspea/source/repos/jacobi-asymptotics/.venv/bin/python papers/paper2/checks/table2.py > checks/table2.out
(the script puts the main repository's src/ on sys.path; it needs the toolkit's built C kernels; runtime about 1 min).
"""
import sys
import time
import numpy as np

sys.path.insert(0, "/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/src")
from jacobi_asym.measures.base import DiscreteMeasure  # noqa: E402
from jacobi_asym.jacobi.dispatch import jacobi_coeffs  # noqa: E402
from jacobi_asym.laws.weyl import c_p  # noqa: E402

T0 = time.time()
CASES = {  # p: (s, n values, runs (K, T_END))
    0.5: (2.0, (100, 200, 400, 800, 1600), [(100_000, 1e48), (200_000, 1e48), (200_000, 1e44)]),
    1.0: (2.0, (50, 100, 200, 400, 800), [(100_000, 1e16), (200_000, 1e16), (200_000, 1e14)]),
    2.0: (2.0, (50, 100, 200, 400, 800), [(100_000, 1e16), (200_000, 1e16), (200_000, 1e14)]),
}
LOGL = lambda t: np.sqrt(np.log(t + np.e))  # noqa: E731
th = lambda n: n / (2 * (n + np.e) * np.sqrt(np.log(n + np.e)))  # noqa: E731  (L'(log n))


def measure(p, s, K, tend, with_l):
    k = np.arange(1, K + 1, dtype=float)
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(1.02))
    gx, gw = np.polynomial.legendre.leggauss(8)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * gx for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    la = -s * np.log(k) + (LOGL(k) if with_l else 0.0)
    lt = -s * np.log(T) + (LOGL(T) if with_l else 0.0) + np.log(W * T)
    m = max(la.max(), lt.max())
    return DiscreteMeasure.from_atoms(k ** -p, np.exp(la - m), tail=(T ** -p, np.exp(lt - m)))


def cols(p, s, run, with_l, ns):
    r = jacobi_coeffs(measure(p, s, *run, with_l), max(ns) + 2, prec="ld")
    a = np.asarray(r.a, np.longdouble); b2 = np.asarray(r.b2, np.longdouble)
    c = c_p(p); out = []
    for n in ns:
        bn = np.sqrt(b2[n - 1]); an = a[n]
        out.append((float(n * (n ** p * bn / c - 1)), float(n * (an / (2 * bn) - 1))))
    return out


for p, (s, ns, runs) in CASES.items():
    alpha = (s - 1 - p) / p
    print(f"p = {p}, s = {s}, alpha = {alpha:+.2f}, c(p) = {c_p(p):.10f}; runs (K, T_END) = {runs}", flush=True)
    data = []  # per run: array [n, (B_l, A_l, B_1, A_1)]
    for run in runs:
        wl = cols(p, s, run, True, ns); w1 = cols(p, s, run, False, ns)
        data.append(np.array([[x[0], x[1], y[0], y[1]] for x, y in zip(wl, w1)]))
    D = np.array(data); ref = D[1]; spread = D.max(0) - D.min(0)
    print("     n    B(l)      B(1)      A(l)      A(1)     B(l)-B(1)  theta_n/2 | spreads B(l), B(1), A(l), A(1)")
    for i, n in enumerate(ns):
        print(f"  {n:5d}  {ref[i,0]:+.4f}  {ref[i,2]:+.4f}  {ref[i,1]:+.4f}  {ref[i,3]:+.4f}   {ref[i,0]-ref[i,2]:+.4f}   {th(n)/2:.4f}  | "
              + ", ".join(f"{v:.1e}" for v in (spread[i, 0], spread[i, 2], spread[i, 1], spread[i, 3])), flush=True)
    print(f"  [{time.time() - T0:.0f}s]", flush=True)
print("[done]")
