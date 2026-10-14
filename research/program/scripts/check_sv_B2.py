"""Problem B numerics [2]: p=s=2, Psi=exp(sqrt(log(k+e))). (a) tilt test: beta_n(w) vs pure power k^{-(2-eps_n)}.
(b) Lanczos: tail masses mu_n((Mn,inf)) and log-moment E_mu_n[log_+(k/n)] for w, v, and along path t=1/2."""
import numpy as np, sys
sys.path.insert(0, "/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/src")
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p = 2.0
def B(K, lw, N):
    k = np.arange(1, K+1, dtype=float); lw = lw - lw.max()
    r = jacobi_coeffs(DiscreteMeasure(k**-p, np.exp(lw)), N+1, prec="ld")
    return np.arange(N+1)**p*np.sqrt(np.asarray(r.b2, float))[:N+1]/c_p(p)
K = 240000; k = np.arange(1, K+1, dtype=float); L = np.sqrt(np.log(k+np.e))
Bv = B(K, -2*np.log(k), 1600); Bw = B(K, -2*np.log(k)+L, 1600)
for n in (100, 400, 1600):
    e = 0.5/np.sqrt(np.log(n)); Bt = B(K, -(2-e)*np.log(k), n)
    print(f"(a) n={n}: beta_w/beta_v-1={Bw[n]/Bv[n]-1:+.3e}  beta_tilt/beta_v-1={Bt[n]/Bv[n]-1:+.3e}  w/tilt-1={Bw[n]/Bt[n]-1:+.3e}", flush=True)
def lanczos(x, w, m):
    Q = np.zeros((m+1, len(x))); q = np.sqrt(w); Q[0] = q/np.linalg.norm(q); b = np.zeros(m+1)
    for j in range(m):
        v = x*Q[j]; v -= (Q[j]@v)*Q[j]
        if j: v -= b[j]*Q[j-1]
        for _ in range(2): v -= Q[:j+1].T@(Q[:j+1]@v)
        b[j+1] = np.linalg.norm(v); Q[j+1] = v/b[j+1]
    return Q
K = 100000; k = np.arange(1, K+1, dtype=float); x = k**-p; L = np.sqrt(np.log(k+np.e))
F = lambda M: 2/np.pi*np.arcsin(np.sqrt(min(1, M**-p/(4*c_p(p)))))
for lab, lw in (("v", -2*np.log(k)), ("t=1/2", -2*np.log(k)+0.5*L), ("w", -2*np.log(k)+L)):
    Q = lanczos(x, np.exp(lw-lw.max()), 400)
    for n in (100, 200, 400):
        mu = Q[n]**2; lm = (mu*np.log(np.maximum(k/n, 1))).sum()
        tails = [mu[M*n:].sum() for M in (2, 8, 32, 128)]
        print(f"(b) {lab:5s} n={n}: mu(>Mn) M=2,8,32,128: " + ", ".join(f"{t:.4f}" for t in tails)
              + f"  [F_p: {', '.join(f'{F(M):.4f}' for M in (2,8,32,128))}]  E[log+(k/n)]={lm:.4f}"
              + f"  E[|g_n|]={(mu*np.abs(L-L[n-1])).sum():.4f}", flush=True)
