"""Plan 26 NUMERICAL (exact, mpmath 300 digits): cluster costs vs the capped pair-energy functional of §5.4.
Pure power atoms k⁻², weights 2k⁻², k ≤ 40n, n = 20. A cluster: atoms k, k+1, …, k+m−1 are moved to
x_k(1 − iε), i = 0..m−1 (mutual relative gaps ≍ ε, pair energy per pair ≈ log(1/ε)). Report
 loss := log D_n(μ) − log D_n(clustered)   and   the bracket of §5.4's mechanism:
 lower/upper scale  min_s [ s(s−1)·log(1/ε) + Σ_{dropped} C ]  with C := deletion costs of the slots k..k+m−1.
Illustration only: moving atoms also shifts slots, so only the scaling (capping, m-dependence) is meaningful."""
import mpmath as mp
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
k = 3
Cdel = []
for j in range(k, k+4):     # deletion costs of slots j (1-based) for reference
    Xd = X0[:j-1] + X0[j:]; Wd = W0[:j-1] + W0[j:]; Cdel.append(D0 - logD(Xd, Wd, n))
print(f"n={n}, cluster starting at k={k}; slot deletion costs C(k..k+3,n) = " + ", ".join(f"{float(c):.2f}" for c in Cdel))
for m in [2, 3, 4]:
    row = []
    for eL in [2, 8, 30, 80]:
        eps = mp.mpf(10)**(-eL)
        X = X0[:]
        for i in range(m): X[k-1+i] = X0[k-1]*(1 - i*eps)
        loss = D0 - logD(X, W0, n)
        L = mp.log(1/eps)
        pred = min(s*(s-1)*L + mp.fsum(Cdel[1:1+m-s]) for s in range(1, m+1))
        row.append(f"ε=1e-{eL}: loss={float(loss):7.2f} [min_s s(s−1)L+ΣC={float(pred):7.2f}]")
    print(f"  m={m}: " + "  ".join(row))
