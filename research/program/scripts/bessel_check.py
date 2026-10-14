"""NUMERICAL de-risk for Problem C (p = s = 2 unless noted). Lanczos as in G1 checks/check_t3_rough.py.
[A] phase-model predictions: ||Δμ_N||_1 -> 8/π², ||Δ²μ_N||_1 -> 4/π (universal), several N, p.
[B] Bessel / large-sieve frame constant: S(N) := max_{|f|<=1} Σ_{n∈[N,2N]} <f, μ_n−μ_{n−1}>² (sign power-iteration lower bound)
    vs random ±1 f. Prediction: S(N) = O(1) (bounded in N), random f: O(1) too (each term ~1/N).
[C] nonlinear: for the S(N)-maximiser f (ε=0.1), actual δ_n = log b_n²(w) − log b_n²(v) on [N,2N]: Σδ², count |δ|>δ0."""
import numpy as np, sys
def lanczos(x, w, n):
    K = len(x); Q = np.zeros((n+2, K)); q = np.sqrt(w); q /= np.linalg.norm(q); Q[0] = q
    a = np.zeros(n+2); b = np.zeros(n+2)
    for j in range(n+1):
        z = x*Q[j]; a[j] = Q[j] @ z; z -= a[j]*Q[j]
        if j: z -= b[j]*Q[j-1]
        for _ in range(2): z -= Q[:j+1].T @ (Q[:j+1] @ z)
        b[j+1] = np.linalg.norm(z); Q[j+1] = z/b[j+1]
    return a, b, Q
rng = np.random.default_rng(1)
print("[A] ||Δμ_N||_1 (pred 8/π²=%.4f), ||Δ²μ_N||_1 (pred 4/π=%.4f)" % (8/np.pi**2, 4/np.pi))
for p in (2.0, 1.0):
    N = 240; K = 40*N if p == 2 else 400*N
    k = np.arange(1, K+1, dtype=float); a, b, Q = lanczos(k**-p, k**-2.0, N+8)
    mu = Q**2
    row = []
    for n in range(N, N+8):
        row.append(f"{np.abs(mu[n]-mu[n-1]).sum():.3f}/{np.abs(mu[n]-2*mu[n-1]+mu[n-2]).sum():.3f}")
    print(f"  p={p} n={N}..{N+7}: " + " ".join(row), "  mean Δ²:", np.mean([np.abs(mu[n]-2*mu[n-1]+mu[n-2]).sum() for n in range(N, N+8)]))
    sys.stdout.flush()
print("[B]/[C] p=s=2")
p = 2.0
for N in (50, 100, 200):
    K = 40*N; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
    a0, b0, Q = lanczos(x, v, 2*N+1); mu = Q**2
    D = np.array([mu[n]-mu[n-1] for n in range(N, 2*N+1)])
    rnd = [((D @ rng.choice([-1.0, 1.0], K))**2).sum() for _ in range(20)]
    best = 0; fbest = None
    for trial in range(6):
        f = rng.choice([-1.0, 1.0], K)
        for it in range(60):
            g = D.T @ (D @ f); fn = np.sign(g); fn[fn == 0] = 1
            if np.array_equal(fn, f): break
            f = fn
        S = ((D @ f)**2).sum()
        if S > best: best, fbest = S, f.copy()
    L = D @ fbest
    print(f"  N={N}: random f Σ L² = {np.mean(rnd):.4f};  max-sign S(N) = {best:.4f};  max|L_n| = {np.abs(L).max():.3f};"
          f" #|L_n|>0.1: {(np.abs(L)>0.1).sum()}/{N+1};  single-n max ||Δμ||_1 = {np.abs(D).sum(1).max():.3f}")
    eps = 0.1
    a1, b1, _ = lanczos(x, v*np.exp(eps*fbest), 2*N+1)
    dl = np.array([np.log(b1[n]**2) - np.log(b0[n]**2) for n in range(N, 2*N+1)])
    print(f"     ε=0.1 nonlinear: Σδ_n² = {(dl**2).sum():.5f} (lin {eps**2*best:.5f}); max|δ| = {np.abs(dl).max():.4f};"
          f" #|δ|>0.02: {(np.abs(dl)>0.02).sum()}, #|δ|>0.01: {(np.abs(dl)>0.01).sum()} of {N+1};"
          f" corr(δ, εL) = {np.corrcoef(dl, eps*L)[0,1]:.3f}")
    sys.stdout.flush()
