"""Plan 24 NUMERICAL (exact, mpmath 300 digits): near-twin cost in Hankel determinants.
Pure power atoms k⁻² (weights 2k⁻²), k ≤ 40n; add a twin atom at x_k(1 − ε) for one k.
Twin cost  T(k,ε) := log D_n(μ + twin) − log D_n(μ)  (≥ 0 by monotonicity)  and the 'pair penalty' view:
compare the configuration 'k replaced by twin pair' via  log D_n(μ ∖ {k} + {twin}) − log D_n(μ ∖ {k} ∪ ...).
We report  Δ(k,ε) := log D_n(μ) − log D_n(μ_ε),  μ_ε := μ with atom k moved to x_k(1 − ε) AND a copy kept at x_k,
minus its ε→0 limit structure: the claim tested is  log D_n(two atoms merged → one) vs  min(2 log(1/ε), C(k,n))."""
import mpmath as mp, math
mp.mp.dps = 300
def logD(X, W, n):
    K = len(X); h = mp.fsum(W); out = n*mp.log(h); P = [1/mp.sqrt(h)]*K; Pp = None; bp = None
    for j in range(1, n):
        al = mp.fsum(W[i]*X[i]*P[i]**2 for i in range(K))
        Q = [(X[i]-al)*P[i] - (bp*Pp[i] if Pp is not None else 0) for i in range(K)]
        b2 = mp.fsum(W[i]*Q[i]**2 for i in range(K)); bb = mp.sqrt(b2)
        out += (n-j)*mp.log(b2); Pp, P = P, [q/bb for q in Q]; bp = bb
    return out
n = 20; Ka = 40*n
X0 = [mp.mpf(1)/mp.mpf(i)**2 for i in range(1, Ka+1)]; W0 = [2*x for x in X0]
D0 = logD(X0, W0, n)
print(f"n={n}: comparison of a 'deleted' atom (σ-style repeat: index k lost) with a near-twin of relative gap ε")
for k in [3, 6, 10]:
    Xd = X0[:k-1] + X0[k:]; Wd = W0[:k-1] + W0[k:]
    C = D0 - logD(Xd, Wd, n)                     # deletion cost C(k,n): repeat = lost index
    row = [f"k={k}: C(k,n)={float(C):7.2f}"]
    for eps in [mp.mpf('1e-2'), mp.mpf('1e-8'), mp.mpf('1e-30'), mp.mpf('1e-80')]:
        # twin: atom k+... inserted: the sequence keeps all indices but atom k+1 is placed at x_k(1−ε) (index k+1 'collides')
        X = X0[:]; X[k] = X0[k-1]*(1-eps)          # 0-based: X[k] is index k+1
        D = logD(X, W0, n)
        loss = D0 - D
        row.append(f"ε=1e{int(mp.log10(eps))}: loss={float(loss):7.2f} (2log(1/ε)={float(2*mp.log(1/eps)):6.1f})")
    print("   " + "  ".join(row))
