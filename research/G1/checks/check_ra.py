"""Plan 41 (NUMERICAL; float64, full-reorthogonalized Lanczos on a truncated measure, as in check_alaw.py).
Convention: Lanczos vector Q[j] = sqrt(w) p_j, a[j] = a_j, b[j] couples Q[j-1], Q[j] (b_j of PROOF.md §3.5).
E_n := b_{n+1} q_n q_{n+1};  ΔE_n := E_n − E_{n−1}.
[1] Toda form: d a_n/dt = <f, ΔE_n> vs central finite differences and vs Lemma FVa (random f); atomwise identity
    ΔE_n = (x − a_n)μ_n − 2 b_n q_{n−1} q_n (recurrence).
[2] Lemma R2a: |d² a_n/dt²| ≤ 2(b_n + b_{n+1})‖f‖²_∞ (second central differences; random and adversarial f).
[3] Lemma R1a: ‖n^p ΔE_n^v‖₁ for the pure power; I := (1/π)∫ min(1, H(2cos θ)) dθ and η_a := c(p) I / 2.
[4] a-law failure: f = ±ε·sign(ΔE_n^v) on [θn, K]; n^p(a_n(w) − a_n(v)) vs first-order ε‖n^pΔE_n|_W‖₁ and vs εη_a/2;
    and a two-scale f (alternating signs) on one measure.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ.setdefault(_v, "1")
import numpy as np
from jacobi_asym.laws.weyl import c_p

def lanczos(x, w, n):
    K = len(x); Q = np.zeros((n+2, K)); q = np.sqrt(w); q /= np.linalg.norm(q); Q[0] = q
    a = np.zeros(n+2); b = np.zeros(n+2)
    for j in range(n+1):
        z = x*Q[j]; a[j] = Q[j] @ z; z -= a[j]*Q[j]
        if j: z -= b[j]*Q[j-1]
        for _ in range(2): z -= Q[:j+1].T @ (Q[:j+1] @ z)
        b[j+1] = np.linalg.norm(z); Q[j+1] = z/b[j+1]
    return a, b, Q

def dE(b, Q, n):          # ΔE_n = b_{n+1} q_n q_{n+1} − b_n q_{n−1} q_n
    return b[n+1]*Q[n]*Q[n+1] - b[n]*Q[n-1]*Q[n]

rng = np.random.default_rng(41)
p = s = 2.0
print("[1] Toda form (p = s = 2, K = 20n, central differences h = 1e-5):")
for n in [20, 60, 150]:
    K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-s
    f = rng.uniform(-1, 1, K); h = 1e-5
    ap, _, _ = lanczos(x, v*np.exp(h*f), n+1); am, _, _ = lanczos(x, v*np.exp(-h*f), n+1)
    a0, b0, Q = lanczos(x, v, n+1)
    fd = (ap[n] - am[n])/(2*h); toda = f @ dE(b0, Q, n)
    fva = ((x - a0[n])*f) @ Q[n]**2 - 2*b0[n]*(f @ (Q[n-1]*Q[n]))
    atom = np.max(np.abs(dE(b0, Q, n) - ((x - a0[n])*Q[n]**2 - 2*b0[n]*Q[n-1]*Q[n])))
    print(f"   n={n:3d}: FD {fd:+.6e}  Toda {toda:+.6e}  FVa {fva:+.6e}  rel.err(FD,Toda) {abs(fd-toda)/abs(fd):.1e}"
          f"  |Toda−FVa| {abs(toda-fva):.1e}  max atomwise residual {atom:.1e}", flush=True)

print("[2] Lemma R2a: |ä_n| / (2(b_n + b_{n+1})‖f‖²_∞) (second central differences, h = 1e-3; must be ≤ 1):")
for n in [20, 60, 150]:
    K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-s
    a0, b0, Q = lanczos(x, v, n+1)
    for name, f in [("random ±1", rng.choice([-1.0, 1.0], K)), ("sign(ΔE_n)", np.where(dE(b0, Q, n) >= 0, 1.0, -1.0)),
                     ("sign(q_n q_{n+1})", np.where(Q[n]*Q[n+1] >= 0, 1.0, -1.0))]:
        h = 1e-3
        ap, _, _ = lanczos(x, v*np.exp(h*f), n+1); am, _, _ = lanczos(x, v*np.exp(-h*f), n+1)
        dd = (ap[n] - 2*a0[n] + am[n])/h**2
        print(f"   n={n:3d} {name:18s}: ratio {abs(dd)/(2*(b0[n]+b0[n+1])):.3f}", flush=True)

def Hfun(z, m=4001):
    ph = np.linspace(0, np.pi, m)[:, None]; u = np.cos(ph); w_ = np.sin(ph)
    return np.min(np.abs(2*u*w_ - z*u*u) + np.abs(z*w_*w_ - 2*u*w_), axis=0)
th = (np.arange(20000) + 0.5)*np.pi/20000
I = np.mean(np.minimum(1.0, Hfun(2*np.cos(th))))
print(f"[3] H(−2), H(0), H(2) = {Hfun(np.array([-2.0, 0.0, 2.0]))};  I = (1/π)∫min(1,H(2cosθ))dθ = {I:.4f}")
for pp in [2.0, 1.0, 0.5]:
    c = c_p(pp); eta = c*I/2
    row = []
    for n in ([100, 101, 200, 201] if pp >= 1 else [60, 61]):
        K = 20*n if pp == 2 else (40*n if pp == 1 else 2000*n)
        k = np.arange(1, K+1, dtype=float); x = k**-pp; v = k**-s
        a0, b0, Q = lanczos(x, v, n+1)
        row.append(f"n={n}: {n**pp*np.abs(dE(b0, Q, n)).sum()/c:.3f}")
    print(f"   p={pp}: c(p)={c:.4f}, η_a = c I/2 = {eta:.4f} (η_a/c = {I/2:.4f});  ‖n^pΔE_n^v‖₁/c(p):  " + "  ".join(row),
          flush=True)

print("[4] a-law failure (p = s = 2, K = 20n, f = ±ε·sign(ΔE_n^v) on W = [θn, K], θ = 1/4):")
c = c_p(2.0); eta = c*I/2
for n in [100, 200]:
    K = 20*n; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-s
    a0, b0, Q = lanczos(x, v, n+1); g = dE(b0, Q, n); W = k >= n/4
    lin = n**p*np.abs(g[W]).sum()
    for eps in [0.05, 0.2]:
        out = []
        for sg in [+1, -1]:
            f = sg*eps*np.where(g >= 0, 1.0, -1.0)*W
            a1, _, _ = lanczos(x, v*np.exp(f), n+1)
            out.append(f"{'+' if sg > 0 else '−'}: n^pΔa_n = {n**p*(a1[n]-a0[n]):+.4f}")
        print(f"   n={n} ε={eps}: first order ±ε‖n^pΔE|_W‖₁ = ±{eps*lin:.4f};  " + "  ".join(out) +
              f";  guaranteed εη_a/2 = {eps*eta/2:.4f};  n^p a_n(v)/(2c) − 1 = {n**p*a0[n]/(2*c)-1:+.1e}", flush=True)

print("[4b] two scales on one measure (K = 8000, n₁ = 40 on [10, 100], n₂ = 400 on [100, K], signs +, −; ε = 0.1):")
K = 8000; k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-s; eps = 0.1
a0, b0, Q = lanczos(x, v, 402)
f = np.zeros(K)
for n_i, lo, hi, sg in [(40, 10, 99, +1), (400, 100, K, -1)]:
    Wi = (k >= lo) & (k <= hi); f += sg*eps*np.where(dE(b0, Q, n_i) >= 0, 1.0, -1.0)*Wi
a1, _, _ = lanczos(x, v*np.exp(f), 402)
dev = np.array([n**p*(a1[n]-a0[n]) for n in range(10, 402)])
for n_i in [40, 400]:
    print(f"   n={n_i}: n^p(a_n(w) − a_n(v))/c(p) = {n_i**p*(a1[n_i]-a0[n_i])/c:+.4f}")
print(f"   max over n∈[10,401] of n^p|a_n(w) − a_n(v)|/c(p): {np.max(np.abs(dev))/c:.4f};"
      f" median {np.median(np.abs(dev))/c:.4f}; εη_a/(2c) = {eps*I/4:.4f}")
