"""Plan 46 (NUMERICAL, float64 Lanczos with full reorthogonalization): Lemma QLP, hard-edge localization for pure powers.

Measure: x_k = k^{-p}, v_k = k^{-sigma}. Exact atoms k <= K; the tail k > K is lumped into geometric cells
[K 2^j, K 2^{j+1}) (mass = integral of k^{-sigma} over the cell, node at the cell's geometric mean), j < 80, plus the rest
at x = 0. All lumped nodes lie far below the Bessel scale x ~ n^{-p-2} (checked: K >= 8 n^{1+2/p}), where polynomials of
degree <= n are essentially constant, so the lumping only perturbs the deep tail mass slightly (reported separately).

For each (p, sigma, n) and M on a geometric grid with Mn <= K:
  tail   := mu_n((Mn, inf))                                  (computed)
  F      := arcsine limit F_p(M) (Lemma LP)
  r1     := tail * M^{p/2}                                    (QLP (a): bounded for M <= n^{2/p})
  r2     := tail * n * (M/n^{2/p})^{beta}, beta = min(p, sigma-1) for p != 1, min(1/2, sigma-1) for p = 1   (QLP (b) shape beyond the Bessel scale; the proof
            also allows a log factor)
  ST     := (8/sqrt3) tau |S_n(tau e^{5 pi i/6})|, tau = M^{-p}, S_n(z) = sum_k mu_n(k)/(n^p x_k - z)
            (Lemma ST: tail <= ST, an exact inequality; checked)
Also: the fitted slope of log tail vs log M for M >= 8 n^{2/p} (heuristic prediction -(sigma-1); proved bound
exponent -beta).
"""
import numpy as np
from jacobi_asym.laws.weyl import c_p


def lanczos(x, w, m):
    K = len(x); Q = np.zeros((m + 1, K)); q = np.sqrt(w); Q[0] = q / np.linalg.norm(q)
    b = np.zeros(m + 1)
    for j in range(m):
        v = x * Q[j]; v -= (Q[j] @ v) * Q[j]
        if j: v -= b[j] * Q[j - 1]
        for _ in range(2): v -= Q[:j + 1].T @ (Q[:j + 1] @ v)
        b[j + 1] = np.linalg.norm(v); Q[j + 1] = v / b[j + 1]
    return Q


def measure(p, s, K):
    k = np.arange(1, K + 1, dtype=float)
    a = (K + 0.5) * 2.0 ** np.arange(0, 80); b = a * 2.0             # cells [a, b) in k
    m = (a ** (1 - s) - b ** (1 - s)) / (s - 1)
    kk = np.sqrt(a * b)
    rest = b[-1] ** (1 - s) / (s - 1)
    kidx = np.concatenate([k, kk, [np.inf]])
    x = np.concatenate([k ** -p, kk ** -p, [0.0]])
    w = np.concatenate([k ** -s, m, [rest]])
    return kidx, x, w


def run(p, s, n, K, Ms):
    kidx, x, w = measure(p, s, K)
    Q = lanczos(x, w, n)
    mu = Q[n] ** 2
    X = n ** p * x
    beta = min(0.5, s - 1) if p == 1 else min(p, s - 1)   # Theorem QLP (b); review F4
    MB = n ** (2 / p)
    rows = []
    for M in Ms:
        if M * n > K: break
        tail = float(mu[kidx > M * n].sum())
        tau = M ** -p
        z = tau * np.exp(5j * np.pi / 6)
        S = complex((mu / (X - z)).sum())
        ST = 8 / np.sqrt(3) * tau * abs(S)
        F = 2 / np.pi * np.arcsin(np.sqrt(min(1.0, tau / (4 * c_p(p)))))
        rows.append((M, tail, F, tail * M ** (p / 2), tail * n * (M / MB) ** beta, ST))
    lump = float(mu[kidx > K].sum())
    return rows, lump, MB, beta


def main():
    cases = [  # (p, n_list, K)
        (2.0, (20, 40), 400000),
        (1.0, (10, 20), 400000),
        (0.5, (4, 6), 1500000),
    ]
    for p, ns, K in cases:
        for s in (1.5, 2.0, 3.0):
            sup_r1 = {}
            for n in ns:
                assert K >= 8 * n ** (1 + 2 / p), "lumped cells must lie below the Bessel scale"
                Ms = 2.0 ** np.arange(0, 40)
                rows, lump, MB, beta = run(p, s, n, K, Ms)
                print(f"\n[p={p} sigma={s} n={n}] K={K}, Bessel scale M_B = n^(2/p) = {MB:.1f}, beta (Theorem QLP (b)) = "
                      f"{beta}, mass on lumped tail = {lump:.3e}", flush=True)
                print("      M        tail        F_p(M)   tail*M^(p/2)  tail*n*(M/M_B)^beta   ST bound   tail<=ST")
                ok = True
                for (M, t, F, r1, r2, ST) in rows:
                    ok &= t <= ST
                    print(f"{M:9.0f}  {t:11.4e}  {F:11.4e}  {r1:10.4f}  {r2:14.4f}  {ST:11.4e}  {t <= ST}")
                r1a = max(r[3] for r in rows if r[0] <= MB)
                sup_r1[n] = r1a
                deep = [(np.log(r[0]), np.log(r[1])) for r in rows if r[0] >= 8 * MB and r[1] > 0]
                if len(deep) >= 3:
                    A = np.array(deep); slope = np.polyfit(A[:, 0], A[:, 1], 1)[0]
                    print(f"  deep-tail slope d log tail / d log M (M >= 8 M_B, {len(deep)} pts) = {slope:.3f}"
                          f"   (heuristic -(sigma-1) = {-(s - 1):.3f}; proved bound exponent -beta = {-beta:.3f})")
                print(f"  sup_{{1<=M<=M_B}} tail*M^(p/2) = {r1a:.4f};  all ST checks pass: {ok}", flush=True)
            print(f"[summary p={p} sigma={s}] sup_(M<=M_B) tail*M^(p/2) by n: "
                  + ", ".join(f"n={n}: {v:.4f}" for n, v in sup_r1.items()), flush=True)


if __name__ == "__main__":
    main()
