"""Plan 69 (NUMERICAL sanity checks for TAIL.md; finite checks of proved statements, Rule N: not certified).

[1] Proposition TB-S / TB-A (comparison frame, window 1 < s < 1 + 2p): for z = tau e^{5 pi i/6},
      tau^{1/2} |S_n(z)|,  S_n(z) = sum_k mu_n(k) / (n^p x_k - z),
    stays bounded uniformly in n for 2 n^{-2} <= tau <= 1/2 (the proof bounds |Q(z)| <= C |z|^{-1/4}, and
    |S_n| = |Q_11 Q_12| / |(Q_1)_12|), and hence tail_n(M) := mu_n((Mn, inf)) <= C M^{-p/2} for 1 <= M <= n^{2/p}/2.
    Also printed: sup over all M (up to the truncation) of tail_n(M) * M^{theta_*}, theta_* = (s-1)/(s(1+2/p)+2)
    (Corollary TB-C). Cases p in {0.5, 1}, s near both window edges and in the middle.
    Method: float64 Lanczos with full reorthogonalisation on atoms k <= K plus geometric cells for k > K (as in
    research/G1/checks/check_qlp.py); K >= 8 n^{1 + 2/p}, so the lumped cells lie below the Bessel scale.
[2] Lemma TS (telescoping): Gamma_n(s0, s1) := sum_{j<=n} log(b_j(s1)/b_j(s0)) + ((s1-s0)/2) log n
      - (1/2) log(c^{(s1-s0)/p} zeta(s0)/zeta(s1))  -> 0
    at p = 1/2 (window (1, 2)) for pairs with one or both points outside the window, plus a window pair and a
    Christoffel step (s, s + p) as controls; and the exact additivity Gamma(s0,s2) = Gamma(s0,s1) + Gamma(s1,s2).
    Method: binary128 RKPW (csrc) on atoms k <= K plus the Gauss-Jacobi continuum tail (so_coeffs.measure);
    truncation effect estimated by K -> 2K (an estimate, not a bound).
Run: make -C csrc; PYTHONPATH=src .venv/bin/python research/G1/RH/second_order/checks/check_tail.py
"""
import sys
import os
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jacobi_asym.laws.weyl import c_p  # noqa: E402


# ---------------------------------------------------------------------------------------------------------------
# [1] spectral weights by Lanczos (float64), as in research/G1/checks/check_qlp.py
def lanczos(x, w, m):
    K = len(x)
    Q = np.zeros((m + 1, K))
    q = np.sqrt(w)
    Q[0] = q / np.linalg.norm(q)
    b = np.zeros(m + 1)
    for j in range(m):
        v = x * Q[j]
        v -= (Q[j] @ v) * Q[j]
        if j:
            v -= b[j] * Q[j - 1]
        for _ in range(2):
            v -= Q[:j + 1].T @ (Q[:j + 1] @ v)
        b[j + 1] = np.linalg.norm(v)
        Q[j + 1] = v / b[j + 1]
    return Q


def lumped_measure(p, s, K):
    k = np.arange(1, K + 1, dtype=float)
    a = (K + 0.5) * 2.0 ** np.arange(0, 80)
    b = a * 2.0
    m = (a ** (1 - s) - b ** (1 - s)) / (s - 1)
    kk = np.sqrt(a * b)
    rest = b[-1] ** (1 - s) / (s - 1)
    kidx = np.concatenate([k, kk, [np.inf]])
    x = np.concatenate([k ** -p, kk ** -p, [0.0]])
    w = np.concatenate([k ** -s, m, [rest]])
    return kidx, x, w


def part1():
    print("[1] Prop TB-Q / TB-A in the window: z = tau e^{5 pi i/6};  R_S := sup_{2/n^2 <= tau <= 1/2} tau^{1/2}|S_n(z)|,")
    print("    R_A := sup_{1 <= M <= n^{2/p}/2} tail_n(M) M^{p/2},  R_C := sup_{M >= 1} tail_n(M) M^{theta_*} (M n <= K)")
    cases = [(0.5, (4, 6, 8), 400000, (1.1, 1.5, 1.9)),
             (1.0, (8, 16, 32), 400000, (1.2, 2.0, 2.8))]
    allfinite = True
    for p, ns, K, ss in cases:
        for s in ss:
            alpha = (s - 1 - p) / p
            th = (s - 1) / (s * (1 + 2 / p) + 2)
            line = []
            for n in ns:
                assert K >= 8 * n ** (1 + 2 / p)
                kidx, x, w = lumped_measure(p, s, K)
                Q = lanczos(x, w, n)
                mu = Q[n] ** 2
                X = n ** p * x
                taus = np.exp(np.linspace(np.log(2.0 / n ** 2), np.log(0.5), 60))
                RS = max(t ** 0.5 * abs(complex((mu / (X - t * np.exp(5j * np.pi / 6))).sum())) for t in taus)
                Ms = 2.0 ** np.arange(0, 60)
                Ms = Ms[Ms * n <= K]
                tails = np.array([mu[kidx > M * n].sum() for M in Ms])
                MB = n ** (2 / p) / 2
                RA = float(max(tails[Ms <= MB] * Ms[Ms <= MB] ** (p / 2)))
                RC = float(max(tails * Ms ** th))
                lump = float(mu[kidx > K].sum())
                allfinite &= bool(np.isfinite([RS, RA, RC]).all()) and abs(mu.sum() - 1) < 1e-8
                line.append(f"n={n}: R_S={RS:.4f} R_A={RA:.4f} R_C={RC:.4f} (lumped {lump:.1e})")
            print(f"   p={p} s={s} alpha={alpha:+.2f} theta_*={th:.4f}: " + ";  ".join(line), flush=True)
    print(f"   all finite and sum mu_n = 1: {allfinite}")


# ---------------------------------------------------------------------------------------------------------------
# [2] telescoping at p = 1/2
def part2():
    import so_coeffs as sc
    mp.mp.dps = 40
    p = 0.5
    c = sc.c_p_mp(p)
    NMAX = 200
    ns = (25, 50, 100, 200)
    svals = (1.25, 1.5, 1.75, 2.25, 2.5, 2.75, 3.0)
    print(f"\n[2] Lemma TS at p = {p} (window (1, {1 + 2 * p})): Gamma_n(s0, s1) -> 0; columns n = {ns}; K = 100*NMAX and 2x")
    logb = {}
    for K in (100 * NMAX, 200 * NMAX):
        for s in svals:
            _, b = sc.coeffs(p, s, K, NMAX)
            logb[(K, s)] = np.array([mp.log(v) for v in b], dtype=object)

    def Gam(K, s0, s1, n):
        S = sum(logb[(K, s1)][:n] - logb[(K, s0)][:n])
        d = mp.mpf(s1) - mp.mpf(s0)
        return S + d / 2 * mp.log(n) - mp.log(c ** (d / p) * mp.zeta(s0) / mp.zeta(s1)) / 2

    pairs = [(1.5, 1.75, "window pair"), (1.5, 2.25, "s1 outside"), (1.25, 3.0, "s1 outside, 3 steps"),
             (2.25, 2.75, "both outside"), (2.5, 3.0, "Christoffel step (s, s+p), s outside"),
             (1.75, 2.25, "Christoffel step (s, s+p), s inside")]
    for s0, s1, lab in pairs:
        v = [Gam(100 * NMAX, s0, s1, n) for n in ns]
        dK = max(abs(Gam(200 * NMAX, s0, s1, n) - Gam(100 * NMAX, s0, s1, n)) for n in ns)
        print(f"   ({s0}, {s1}) [{lab}]: " + ", ".join(f"{float(x):+.3e}" for x in v)
              + f"   |K->2K change| <= {float(dK):.1e}", flush=True)
    add = max(abs(Gam(100 * NMAX, 1.25, 3.0, n) - Gam(100 * NMAX, 1.25, 1.75, n) - Gam(100 * NMAX, 1.75, 2.25, n)
                  - Gam(100 * NMAX, 2.25, 3.0, n)) for n in ns)
    print(f"   additivity Gamma(1.25,3) - Gamma(1.25,1.75) - Gamma(1.75,2.25) - Gamma(2.25,3): max |.| = {float(add):.1e}")


if __name__ == "__main__":
    part1()
    part2()
