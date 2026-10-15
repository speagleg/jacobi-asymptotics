"""Plan 64 (NUMERICAL sanity checks for UL.md): the variational sandwich (Lemma V), the second-variation identity
(Proposition SV), the finite-truncation failure of (CVX) (Remark CVX-fin), and the uniform-in-s boundedness of
F_n(s) - F_n(s0), F_n(s) := log h_n(sigma_{p,s}) + s log n (Theorem UF), with the uniform Law P on compacts (Thm UP; b- and alpha-parts).

These are finite checks of proved statements (Rule N: NUMERICAL, not certified).
[1]-[3]: mpmath, Hankel matrices of zeta values / zeta derivatives (dps 60), small n.
[4]: binary128 RKPW (csrc) on atoms k <= K plus the Gauss-Jacobi continuum tail of so_coeffs.measure, n <= NMAX.
Run: PYTHONPATH=src .venv/bin/python research/G1/RH/second_order/checks/check_ul.py"""
import sys
import os
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mp.mp.dps = 60


def hankel(r, p, n, d=0):
    """H_ij = sum_k k^{-r} (log k)^d x_k^{i+j}, x_k = k^{-p}  (= (-1)^d zeta^{(d)}(r + p(i+j)))."""
    return mp.matrix([[(-1) ** d * mp.zeta(r + p * (i + j), derivative=d) for j in range(n)] for i in range(n)])


def monic(t, p, n):
    """coefficient vector (length n+1) of the monic OP pi_n of sigma_{p,t}, and h_n(t)."""
    H = hankel(t, p, n + 1)
    if n == 0:
        return mp.matrix([1]), H[0, 0]
    A = H[:n, :n]
    rhs = mp.matrix([-H[i, n] for i in range(n)])
    c = mp.lu_solve(A, rhs)
    v = mp.matrix([c[i] for i in range(n)] + [1])
    return v, (v.T * H * v)[0]


def quad(v, r, p, d=0):
    return (v.T * hankel(r, p, len(v), d) * v)[0]


print("[1] Lemma V (exact, small n): with u := s - t,")
print("    (U) log h_n(s) - log h_n(t) <= log E_t[k^{-u}],   (D) log h_n(s) - log h_n(t) >= -log E_t[k^{u}]")
worst = mp.inf
for p in (mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2)):
    for t in (mp.mpf(3) / 2, mp.mpf(2), mp.mpf(3)):
        for u in (mp.mpf(-2) / 5, mp.mpf(-1) / 4, mp.mpf(1) / 4, mp.mpf(2) / 5):
            if t - abs(u) <= 1:
                continue
            s = t + u
            for n in (1, 2, 4, 8):
                v, ht = monic(t, p, n)
                _, hs = monic(s, p, n)
                Em = quad(v, t + u, p) / ht      # E_t[k^{-u}] = sum k^{-t-u} pi_t^2 / h_t
                Ep = quad(v, t - u, p) / ht      # E_t[k^{u}]
                d = mp.log(hs) - mp.log(ht)
                sU = mp.log(Em) - d
                sD = d + mp.log(Ep)
                worst = min(worst, sU, sD)
    print(f"   p={mp.nstr(p, 2)}: done")
print(f"   min slack over all (p, t, u, n): {mp.nstr(worst, 6)}  (both inequalities hold: {worst >= 0})")

print("\n[2] Proposition SV: d^2/ds^2 log h_n = Var_{mu_n}(log k) - 2 sum_{i<n} f_{in}^2 (exact, small n)")


def sv_rhs(s, p, n, N=None):
    """Var_{mu_n}(log k) - 2 sum_{i<n} f_in^2 for sigma_{p,s} (N=None) or its truncation to k <= N."""
    if N is None:
        H0, H1, H2 = (hankel(s, p, n + 1, d) for d in (0, 1, 2))
    else:
        def Hf(d):
            return mp.matrix([[mp.fsum(mp.mpf(k) ** (-s) * mp.log(k) ** d * mp.mpf(k) ** (-p * (i + j))
                                       for k in range(1, N + 1)) for j in range(n + 1)] for i in range(n + 1)])
        H0, H1, H2 = Hf(0), Hf(1), Hf(2)
    L = mp.cholesky(H0)                      # H0 = L L^T; orthonormal polys: rows of L^{-1}
    Li = L ** -1
    F1 = Li * H1 * Li.T                      # f_ij = <P_i, log k P_j>
    F2 = Li * H2 * Li.T
    var = F2[n, n] - F1[n, n] ** 2
    down = mp.fsum(F1[i, n] ** 2 for i in range(n))
    return var - 2 * down, down


def logh(s, p, n, N=None):
    if N is None:
        return mp.log(monic(s, p, n)[1])

    def D(m):
        if m == 0:
            return mp.mpf(1)
        return mp.det(mp.matrix([[mp.fsum(mp.mpf(k) ** (-s) * mp.mpf(k) ** (-p * (i + j)) for k in range(1, N + 1))
                                  for j in range(m)] for i in range(m)]))
    return mp.log(D(n + 1) / D(n))


errs = []
for p in (mp.mpf(1), mp.mpf(2)):
    for s in (mp.mpf(3) / 2, mp.mpf(5) / 2):
        for n in (1, 2, 4):
            lhs = mp.diff(lambda z: logh(z, p, n), s, 2)
            rhs, _ = sv_rhs(s, p, n)
            errs.append(abs(lhs - rhs) / abs(lhs))
            print(f"   p={mp.nstr(p, 2)} s={mp.nstr(s, 3)} n={n}: (log h_n)'' = {mp.nstr(lhs, 12)},  "
                  f"Var - 2*down = {mp.nstr(rhs, 12)}")
print(f"   max relative discrepancy: {mp.nstr(max(errs), 3)}  (identity holds to working precision: {max(errs) < 1e-20})")

print("\n[3] Remark CVX-fin: truncation sigma^(N) = sum_{k<=N} k^{-s} delta_{k^{-p}}, n = N - 1: (log h_{N-1})'' = -sum_{i<n} f_in^2 < 0")
mp.mp.dps = 40
allneg = True
for p in (mp.mpf(1), mp.mpf(2)):
    for N in (3, 5, 8):
        s = mp.mpf(2)
        n = N - 1
        lhs = mp.diff(lambda z: logh(z, p, n, N), s, 2)
        rhs, down = sv_rhs(s, p, n, N)
        allneg = allneg and lhs < 0
        print(f"   p={mp.nstr(p, 2)} N={N}: (log h_n)'' = {mp.nstr(lhs, 8)},  -down = {mp.nstr(-down, 8)},  "
              f"Var-2down = {mp.nstr(rhs, 8)}")
print(f"   all negative: {allneg}")

print("\n[4] Theorems UF, UF-lim / Thm UP: s on a grid in [1.5, 4], n <= NMAX; F_n(s) := log h_n(s) + s log n")
from so_coeffs import measure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
NMAX = 400
SG = [1.5 + 0.25 * i for i in range(11)]
for p in (1.0, 2.0):
    K = 100 * NMAX
    c = float((mp.pi / (2 * (mp.sqrt(mp.pi) / 2 * mp.gamma(1 / mp.mpf(p) + 0.5) / mp.gamma(1 / mp.mpf(p) + 1)))) ** p / 4)
    Fs, nb, na = [], [], []
    for s in SG:
        jc = jacobi_rkpw(measure(p, s, K, NMAX + 8), NMAX + 1, prec="q")
        b2 = np.array([float(v) for v in jc.b2[:NMAX]])
        n = np.arange(1, NMAX + 1)
        logh_ = float(mp.log(mp.zeta(s))) + np.cumsum(np.log(b2))
        Fs.append(logh_ + s * np.log(n))
        nb.append(n ** p * np.sqrt(b2) / c)
        al = np.array([float(v) for v in jc.a[:NMAX + 1]])   # alpha_0..alpha_NMAX
        na.append(n ** p * al[1:NMAX + 1] / (2 * c))          # n^p alpha_n / (2c), n = 1..NMAX
    Fs, nb, na = np.array(Fs), np.array(nb), np.array(na)
    D = Fs - Fs[0]                              # F_n(s) - F_n(1.5)
    lim = (np.array(SG) - SG[0])[:, None] * np.log(c) / p   # Theorem UF-lim: (s - s0) log c / p
    print(f"   p={p}: sup_s |F_n(s) - F_n(1.5)| at n = 50, 100, 200, 400: "
          + ", ".join(f"{np.abs(D[:, m - 1]).max():.4f}" for m in (50, 100, 200, 400)))
    print(f"          sup_s |F_n(s) - F_n(1.5) - (s - 1.5) log c / p| at n = 50, 100, 200, 400: "
          + ", ".join(f"{np.abs(D[:, m - 1] - lim[:, 0]).max():.2e}" for m in (50, 100, 200, 400)))
    lam = -(Fs[1:] - Fs[:-1]) / 0.25            # secant proxy for Lambda_n on each cell
    print(f"          secant proxy of Lambda_n, min/max over cells at n = 100, 400: "
          f"{lam[:, 99].min():.4f}/{lam[:, 99].max():.4f}, {lam[:, 399].min():.4f}/{lam[:, 399].max():.4f}"
          f"   (fixed-s limit -(log c)/p = {-np.log(c) / p:.4f})")
    print(f"          n^p b_n(s)/c over s in grid, n in [10, 400]: min {nb[:, 9:].min():.4f}, max {nb[:, 9:].max():.4f}")
    print(f"          sup_s |n^p b_n(s)/c - 1| at n = 50, 100, 200, 400: "
          + ", ".join(f"{np.abs(nb[:, m - 1] - 1).max():.2e}" for m in (50, 100, 200, 400)))
    print(f"          sup_s |n^p alpha_n(s)/(2c) - 1| at n = 50, 100, 200, 400: "
          + ", ".join(f"{np.abs(na[:, m - 1] - 1).max():.2e}" for m in (50, 100, 200, 400)))
