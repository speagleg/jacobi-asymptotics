"""Plan 35 (NUMERICAL, float64 Lanczos with full reorthogonalization): Mn-scale localization.
[1] Lemma TV derivative formula vs central finite difference (p = s = 2, random f, n = 100, A = (4n, ∞)).
[2] Pure power v = k^{-s} (s = 2): μ_n((Mn, ∞)) vs the arcsine limit F_p(M) = (2/π)arcsin(√(M^{-p}/(4c(p)))) (Lemma LP).
[3] Ψ = 2 + sin(log log(k+2)): μ_n^w((Mn, ∞)) vs μ_n^v((Mn, ∞)) and the Theorem L bound e^{4G}(√μ^v + δ_n + G√h)², with
    δ_n := max |log Ψ(k) − log Ψ(n)| over k ∈ [n/4, Mn] and h := μ_n^w(k < n/4) (computed, not bounded). The
    n/4 head here is only for this p = 2 illustration; the proof uses the p-dependent margin M₀(p) (review F10)."""
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

def tail(Q, n, L): return float((Q[n, L:] ** 2).sum())   # index L ↔ k = L + 1, so this is μ_n(k > L)

# [1]
K = 20000; k = np.arange(1, K + 1, dtype=float); x = k ** -2.0; v = k ** -2.0
f = np.random.default_rng(3).uniform(-1, 1, K); n = 100; A = k > 4 * n; t, h = 0.3, 1e-5
mu = lambda tt: (lanczos(x, v * np.exp(tt * f), n)[n] ** 2)[A].sum()
fd = (mu(t + h) - mu(t - h)) / (2 * h)
Q = lanczos(x, v * np.exp(t * f), n); qn = Q[n]; Kf = Q[:n].T @ (Q[:n] @ (f * qn))
form = (f * qn * qn)[A].sum() - 2 * (qn * A) @ Kf - (f * qn) @ qn * (qn ** 2)[A].sum()
print(f"[1] d/dt mu_n(A): finite difference {fd:.10e}, Lemma TV formula {form:.10e}", flush=True)

# [2]
F = lambda p, M: 2 / np.pi * np.arcsin(np.sqrt(M ** -p / (4 * c_p(p))))
for p, K, ns in ((2.0, 60000, (100, 200, 400)), (1.0, 200000, (50, 100, 200)), (0.5, 400000, (25, 50, 100))):
    k = np.arange(1, K + 1, dtype=float); Q = lanczos(k ** -p, k ** -2.0, max(ns))
    for M in (2, 4, 8, 16):
        print(f"[2] p={p} M={M:2d}: mu_n((Mn,inf)) at n={ns}: " + ", ".join(f"{tail(Q, n, M * n):.4f}" for n in ns)
              + f"   arcsine limit F_p(M) = {F(p, M):.4f}", flush=True)

# [3]
p, K = 2.0, 60000; k = np.arange(1, K + 1, dtype=float); x = k ** -p; v = k ** -2.0
psi = 2 + np.sin(np.log(np.log(k + 2))); G = np.log(3.0)
Qv = lanczos(x, v, 400); Qw = lanczos(x, v * psi, 400)
for M in (4, 16):
    for n in (100, 200, 400):
        mv, mw = tail(Qv, n, M * n), tail(Qw, n, M * n)
        idx = np.arange(n // 4 - 1, M * n); dl = np.abs(np.log(psi[idx]) - np.log(psi[n - 1])).max()
        hh = float((Qw[n, :n // 4 - 1] ** 2).sum())
        bound = np.exp(4 * G) * (np.sqrt(mv) + dl + G * np.sqrt(hh)) ** 2
        print(f"[3] M={M:2d} n={n}: mu^w={mw:.4f} mu^v={mv:.4f} delta_n={dl:.4f} head={hh:.1e} Theorem L bound={bound:.3f}"
              f" (holds: {mw <= bound})", flush=True)
