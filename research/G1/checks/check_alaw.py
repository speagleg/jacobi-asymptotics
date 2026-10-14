"""Plan 32 (NUMERICAL).
[1] Lemma FVa: d a_n/dt = ⟨(x − a_n) f, μ_n⟩ − 2 b_n ⟨f, q_{n−1} q_n⟩ (q_j = √w p_j, μ_n = q_n²), checked by central
    finite differences on full-reorthogonalized Lanczos (float64), x_k = k^{-2}, w = k^{-2}, random bounded f; also the
    Toda case f = x (expect b_{n+1}² − b_n²).
[2] a-law transfer: n^p a_n/(2c(p)) for w = k^{-2}ψ_k, ψ_k = 1 + ½(−1)^k/log(k+1) vs ψ ≡ 1 (long double RKPW)."""
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
rng = np.random.default_rng(32)
print("[1] Lemma FVa (central differences, h = 1e-5):")
for n in [20, 60, 150]:
    K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-2.0; v = k**-2.0
    for name, f in [("random", rng.uniform(-1, 1, K)), ("Toda f=x", x.copy())]:
        h = 1e-5
        ap, bp, _ = lanczos(x, v*np.exp(h*f), n+1); am, bm, _ = lanczos(x, v*np.exp(-h*f), n+1)
        a0, b0, Q = lanczos(x, v, n+1)
        fd = (ap[n] - am[n])/(2*h)
        # b[j] here = sqrt(h_j/h_{j-1}) couples Q[j-1], Q[j]; the lemma's b_n couples q_{n-1}, q_n -> b0[n]
        form = ((x - a0[n])*f) @ Q[n]**2 - 2*b0[n]*(f @ (Q[n-1]*Q[n]))
        extra = f"  Toda: b_(n+1)²−b_n² = {b0[n+1]**2-b0[n]**2:+.6e}" if name.startswith("Toda") else ""
        print(f"   n={n:3d} {name:9s}: finite diff {fd:+.6e}   formula {form:+.6e}   rel.err {abs(fd-form)/abs(fd):.1e}{extra}", flush=True)
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p, K = 2.0, 120000
k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
res = {}
for name, psi in [("pure", np.ones(K)), ("ψ=1+½(−1)^k/log(k+1)", 1 + 0.5*(-1)**k/np.log(k+1)), ("parity (no decay)", 1 + 0.5*(-1)**k)]:
    r = jacobi_coeffs(DiscreteMeasure(x, v*psi), 3700, prec="ld"); a = np.asarray(r.a, float)
    nn = np.arange(len(a)); res[name] = (nn+1)**p*a/(2*c_p(p))   # a[i] pairs with p_i (0-based): index n = i
print("[2] (n+1)^p a_n/(2c(p)) → 1:")
for name, A in res.items():
    print(f"   {name:24s} " + "  ".join(f"n={n}: {A[n]-1:+.2e}" for n in (250, 500, 1000, 2000, 3600)) +
          "   |A(ψ)−A(1)|: " + ", ".join(f"{abs(A[n]-res['pure'][n]):.1e}" for n in (250, 1000, 3600)))
