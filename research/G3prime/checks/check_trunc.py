"""Plan 25 NUMERICAL (exact, mpmath) checks for Lemma Tr (truncation) in PROOF.md §4.1:
ν = Σ_{j≤Ka} j^{-4} δ_{j^{-2}} (Ka = 40n); A := {l > J}.
[1] gap: 1 − λ_max(K_A) = λ_min(G_head), G_head := Σ_{l≤J} w_l p(x_l)p(x_l)ᵀ   vs   e^{−C n}  (report −log/n)
[2] log D_n(ν_J) − log D_n(ν) = log det(I − K_A)  ≥  −(f(λ_max)/λ_max)·tr K_A,  f(λ) = −log(1−λ)
[3] tr K_A = E#(S∩A) as J/n grows.
ν is cut off at Ka = 40n atoms (reviewer: moving to 80n changes values by ≤ 2.2e-4). [2] checks only the convexity
step (automatically true), not the constant C_s n + 2."""
import mpmath as mp
mp.mp.dps = 200
def orthopolys(X, W, n):
    K = len(X); h = mp.fsum(W); P = [1/mp.sqrt(h)]*K; Pp = None; bp = None; Ps = [P]
    for j in range(1, n):
        al = mp.fsum(W[i]*X[i]*P[i]**2 for i in range(K))
        Q = [(X[i]-al)*P[i] - (bp*Pp[i] if Pp is not None else 0) for i in range(K)]
        bb = mp.sqrt(mp.fsum(W[i]*Q[i]**2 for i in range(K))); Pp, P = P, [q/bb for q in Q]; bp = bb; Ps.append(P)
    return Ps
for n in [8, 12, 16]:
    Ka = 40*n
    X = [mp.mpf(1)/mp.mpf(j)**2 for j in range(1, Ka+1)]; W = [mp.mpf(1)/mp.mpf(j)**4 for j in range(1, Ka+1)]
    Ps = orthopolys(X, W, n)
    for Jm in [2, 3, 4, 6]:
        J = Jm*n
        Gh = mp.matrix(n, n)
        for a in range(n):
            for b in range(a, n):
                v = mp.fsum(W[l]*Ps[a][l]*Ps[b][l] for l in range(J)); Gh[a, b] = v; Gh[b, a] = v
        ev = mp.eigsy(Gh)[0]; lmin = min(ev[i] for i in range(n))
        trKA = mp.fsum(W[l]*mp.fsum(Ps[a][l]**2 for a in range(n)) for l in range(J, Ka))
        logdet = mp.log(mp.det(Gh))
        lmax = 1 - lmin; f = -mp.log(lmin)
        bound = -(f/lmax)*trKA
        print(f"n={n:2d} J={Jm}n: 1−λmax={mp.nstr(lmin,4):>10} (−log/n={float(f/n):.3f})  tr K_A={float(trKA):.4e}  "
              f"log det(I−K_A)={float(logdet):.4e} ≥ bound {float(bound):.4e}: {logdet >= bound}")
