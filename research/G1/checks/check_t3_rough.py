"""Plan 28 (NUMERICAL): rough weights vs (T3). Full-reorthogonalized Lanczos (float64) on truncated pure-power measures
x_k = k^{-2}, k <= K. [1] TV(μ_n, μ_{n-1}) for μ_n := w p_n^2 and the effect of an adversarial bounded log-weight perturbation
f = ε·sign(μ_n − μ_{n−1}) on |β_n/β_{n−1} − 1| (smooth → perturbed), with the first-order prediction ⟨f, μ_n − μ_{n−1}⟩
(Lemma FV). [2] Where |μ_n − μ_{n−1}| lives (k/n quantiles). [3] One weight sequence with adversarial windows [0.6N, 1.6N] at
N = 60, 240 (ε = 0.2)."""
import numpy as np
def lanczos(x, w, n):
    """Full-reorthogonalized Lanczos on diag(x) from sqrt(w)/||.||: returns a[0..n], b[1..n+1] and vectors q_0..q_{n+1}."""
    K = len(x); Q = np.zeros((n+2, K)); q = np.sqrt(w); q /= np.linalg.norm(q); Q[0] = q
    a = np.zeros(n+2); b = np.zeros(n+2)
    for j in range(n+1):
        z = x*Q[j]; a[j] = Q[j] @ z
        z -= a[j]*Q[j]
        if j: z -= b[j]*Q[j-1]
        for _ in range(2): z -= Q[:j+1].T @ (Q[:j+1] @ z)
        b[j+1] = np.linalg.norm(z); Q[j+1] = z/b[j+1]
    return a, b, Q
print("[1]")
p = 2.0
for n in [100, 200, 400]:
    K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
    a0, b0, Q = lanczos(x, v, n+1)
    mn, mn1 = Q[n]**2, Q[n-1]**2          # w_k p_n(x_k)^2, w_k p_{n-1}(x_k)^2 (probability vectors)
    tv = 0.5*np.abs(mn - mn1).sum()
    out = []
    for eps in [0.05, 0.2, 0.5]:
        f = eps*np.sign(mn - mn1)
        a1, b1, _ = lanczos(x, v*np.exp(f), n+1)
        r0 = np.log(b0[n]**2/b0[n-1]**2); r1 = np.log(b1[n]**2/b1[n-1]**2)
        pred = f @ (mn - mn1)
        out.append(f"ε={eps}: Δ={r1-r0:+.4f} (1st-order {pred:+.4f}), |β_n/β_(n-1)−1| {abs(np.exp(r0/2)*(n/(n-1))**p-1):.1e}→{abs(np.exp(r1/2)*(n/(n-1))**p-1):.3f}")
    print(f"n={n:4d} TV(μ_n,μ_(n−1))={tv:.3f}  " + "  ".join(out), flush=True)
# [A] where does |μ_n − μ_{n−1}| live (in k/n)?
n = 200; K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
a0, b0, Q = lanczos(x, v, n+1); d = np.abs(Q[n]**2 - Q[n-1]**2)
cum = np.cumsum(d)/d.sum()
print("[A] n=200: k/n quantiles of |μ_n−μ_(n−1)| mass: " + "  ".join(f"{q}:{(np.searchsorted(cum, q)+1)/n:.2f}" for q in [0.05, 0.25, 0.5, 0.75, 0.95, 0.99]))
# [B] one sequence, modifications on band windows [0.6N, 1.6N] at N1=60, N2=240 (disjoint), sign pattern from the smooth measure
K = 6000; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0; eps = 0.2
f = np.zeros(K)
for N in [60, 240]:
    a0, b0, Q = lanczos(x, v, N+1)
    sl = slice(int(0.6*N), int(1.6*N)); f[sl] = eps*np.sign(Q[N][sl]**2 - Q[N-1][sl]**2)
a0, b0, _ = lanczos(x, v, 400); a1, b1, _ = lanczos(x, v*np.exp(f), 400)
jump = lambda b, n: abs((b[n]/b[n-1])*(n/(n-1))**p - 1)
print("[B] single weight sequence, ε=0.2 (weights in [e^{−ε},e^{ε}]·k^{−2}); |β_n/β_(n−1)−1| smooth → modified:")
for n in [40, 60, 100, 160, 240, 320, 390]:
    print(f"    n={n:3d}: {jump(b0,n):.1e} → {jump(b1,n):.3f}")
