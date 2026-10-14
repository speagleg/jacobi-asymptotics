"""Plan 28 (NUMERICAL, rewritten after Rule R F1/F7/F8): rough weights vs (T3). Full-reorthogonalized Lanczos (float64)
on truncated pure-power measures x_k = k^{-2}, w = k^{-2}, k <= K (Lanczos vector Q[j] = √w·p_j; b[n]² = h_n/h_{n−1}).
[1] TV(μ_n, μ_{n−1}) (μ_n := w p_n²) and an adversarial bounded log-weight perturbation f = ε·sign(Δ²μ),
    Δ²μ := μ_n − 2μ_{n−1} + μ_{n−2}, with |β_n/β_{n−1} − 1| smooth → perturbed; first-order checks of Lemma FV:
    change of log b_n² vs ⟨f, μ_n − μ_{n−1}⟩, and change of log(b_n²/b_{n−1}²) vs ⟨f, Δ²μ⟩.
[1b] Rule N: K = 20n vs 40n at n = 200 (pattern recomputed on each measure).
[2] Where |μ_n − μ_{n−1}| lives (k/n quantiles).
[3] One weight sequence, adversarial windows [0.6N, 1.6N] at N = 60, 240 (ε = 0.2); |β_n/β_{n−1} − 1| at every n ≤ 390
    reported as max outside the windows' spikes.
[4] Generic rough weights (parity, random U[½,3/2]; long double RKPW, K = 120000 and 240000): mean |β_{m+1}/β_m − 1|
    over [n, 1.1n]."""
import numpy as np
def lanczos(x, w, n):
    K = len(x); Q = np.zeros((n+2, K)); q = np.sqrt(w); q /= np.linalg.norm(q); Q[0] = q
    a = np.zeros(n+2); b = np.zeros(n+2)
    for j in range(n+1):
        z = x*Q[j]; a[j] = Q[j] @ z
        z -= a[j]*Q[j]
        if j: z -= b[j]*Q[j-1]
        for _ in range(2): z -= Q[:j+1].T @ (Q[:j+1] @ z)
        b[j+1] = np.linalg.norm(z); Q[j+1] = z/b[j+1]
    return a, b, Q
p = 2.0
jump = lambda b, n: abs((b[n]/b[n-1])*(n/(n-1))**p - 1)
def adversarial(n, Kmul, eps_list):
    K = Kmul*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
    a0, b0, Q = lanczos(x, v, n+1)
    m0, m1, m2 = Q[n]**2, Q[n-1]**2, Q[n-2]**2
    tv = 0.5*np.abs(m0 - m1).sum(); d2 = m0 - 2*m1 + m2
    out = []
    for eps in eps_list:
        f = eps*np.sign(d2)
        a1, b1, _ = lanczos(x, v*np.exp(f), n+1)
        dlogb = np.log(b1[n]**2) - np.log(b0[n]**2); pred1 = f @ (m0 - m1)
        dratio = np.log(b1[n]**2/b1[n-1]**2) - np.log(b0[n]**2/b0[n-1]**2); pred2 = f @ d2
        out.append(f"ε={eps}: Δlog b_n²={dlogb:+.4f} (FV {pred1:+.4f}); Δlog(b_n²/b_(n−1)²)={dratio:+.4f} (⟨f,Δ²μ⟩ {pred2:+.4f}); "
                   f"|β_n/β_(n−1)−1| {jump(b0,n):.1e}→{jump(b1,n):.3f}")
    return tv, np.abs(d2).sum(), out
print("[1]")
for n in [100, 200, 400]:
    tv, l1, out = adversarial(n, 20, [0.05, 0.2])
    print(f"n={n:4d} TV(μ_n,μ_(n−1))={tv:.3f} ‖Δ²μ‖₁={l1:.3f}\n    " + "\n    ".join(out), flush=True)
print("[1b] Rule N (n=200, ε=0.2): " + "  ".join(f"K={m}n: {adversarial(200, m, [0.2])[2][0].split('|β_n/β_(n−1)−1| ')[1]}" for m in (20, 40)), flush=True)
n = 200; K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
a0, b0, Q = lanczos(x, v, n+1); d = np.abs(Q[n]**2 - Q[n-1]**2); cum = np.cumsum(d)/d.sum()
print("[2] n=200: k/n quantiles of |μ_n−μ_(n−1)| mass: " + "  ".join(f"{q}:{(np.searchsorted(cum, q)+1)/n:.2f}" for q in [0.05, 0.25, 0.5, 0.75, 0.95, 0.99]), flush=True)
K = 6000; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0; eps = 0.2; f = np.zeros(K)
for N in [60, 240]:
    a0, b0, Q = lanczos(x, v, N+1); d2 = Q[N]**2 - 2*Q[N-1]**2 + Q[N-2]**2
    sl = slice(int(0.6*N), int(1.6*N)); f[sl] = eps*np.sign(d2[sl])
a0, b0, _ = lanczos(x, v, 400); a1, b1, _ = lanczos(x, v*np.exp(f), 400)
J = np.array([jump(b1, n) for n in range(10, 391)]); ns = np.arange(10, 391)
spikes = np.isin(ns, [59, 60, 61, 239, 240, 241])
print(f"[3] one sequence, ε=0.2: jumps at N=60: {jump(b1,60):.3f} (N+1: {jump(b1,61):.3f}); N=240: {jump(b1,240):.3f} (N+1: {jump(b1,241):.3f}); "
      f"max over all other n∈[10,390]: {J[~spikes].max():.3f}; smooth max {max(jump(b0,n) for n in range(10,391)):.1e}", flush=True)
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
def beta(K, kind, nmax):
    k = np.arange(1, K+1, dtype=float); x = k**-p
    w = {"parity": k**-2*(2+(-1)**k), "random": k**-2*np.random.default_rng(28).uniform(0.5, 1.5, K)}[kind]
    r = jacobi_coeffs(DiscreteMeasure(x, w), nmax+1, prec="ld"); b = np.sqrt(np.asarray(r.b2, float))
    nn = np.arange(len(b)); return nn**p*b/c_p(p)
for kind in ["parity", "random"]:
    B1, B2 = beta(120000, kind, 4000), beta(240000, kind, 4000)
    row = [f"n={n}: {np.abs(B1[np.arange(n,int(1.1*n))+1]/B1[np.arange(n,int(1.1*n))]-1).mean():.2e}|{np.abs(B2[np.arange(n,int(1.1*n))+1]/B2[np.arange(n,int(1.1*n))]-1).mean():.2e}" for n in (250, 500, 1000, 2000, 3600)]
    print(f"[4] {kind:6s} mean|β_(m+1)/β_m−1| over [n,1.1n] (K|2K): " + "  ".join(row), flush=True)
