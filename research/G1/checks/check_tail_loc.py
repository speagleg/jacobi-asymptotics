"""Plan 30 (NUMERICAL): Lemma TL (polynomial tail localization) sanity check.
x_k = k^{-p}, weights k^{-s}·ψ_k with ψ ∈ [c, C] (random), full-reorthogonalized Lanczos (float64) on K atoms.
Compares ρ_{n+1}(k) = Σ_{j≤n} w_k p_j(x_k)² for k ≥ T'' with the bound 1156 (C/c) (T''/k)^s, where
T' = ⌈8 p n²⌉, T'' = ⌈T' n^{2/p}⌉; and reports μ_n((T,∞)) at T = T'' and beyond, plus where μ_n actually lives."""
import numpy as np
def lanczos(x, w, n):
    K = len(x); Q = np.zeros((n+2, K)); q = np.sqrt(w); q /= np.linalg.norm(q); Q[0] = q
    a = np.zeros(n+2); b = np.zeros(n+2)
    for j in range(n+1):
        z = x*Q[j]; a[j] = Q[j] @ z; z -= a[j]*Q[j]
        if j: z -= b[j]*Q[j-1]
        for _ in range(2): z -= Q[:j+1].T @ (Q[:j+1] @ z)
        b[j+1] = np.linalg.norm(z); Q[j+1] = z/b[j+1]
    return a, b, Q
rng = np.random.default_rng(30)
for (p, s, n) in [(2.0, 2.0, 6), (2.0, 2.0, 10), (3.0, 2.0, 8), (1.5, 3.0, 6)]:
    T1 = int(np.ceil(8*p*n*n)); T2 = int(np.ceil(T1*n**(2/p))); K = 6*T2
    k = np.arange(1, K+1, dtype=float); x = k**-p; c, C = 0.5, 1.5; w = k**-s*rng.uniform(c, C, K)
    a, b, Q = lanczos(x, w, n+1)
    rho = (Q[:n+1]**2).sum(0)            # ρ_{n+1}(k)
    ks = np.arange(T2, K); ratio = rho[T2-1:K-1]/(1156*(C/c)*(T2/ks)**s)
    mu = Q[n]**2
    print(f"p={p} s={s} n={n}: T'={T1} T''={T2} K={K}: max ρ_(n+1)(k)/bound over k≥T'' = {ratio.max():.2e};  "
          f"μ_n mass beyond T'': {mu[T2:].sum():.2e}, beyond 10n: {mu[10*n:].sum():.2e}, beyond 3n: {mu[3*n:].sum():.2e}", flush=True)
