"""Plan 23 NUMERICAL (exact, mpmath) checks for PROOF.md §5.2 (Theorem N″):
[1] Hadamard deletion bound: log D_n(μ∖E) ≤ log D_n(μ) + Σ_{k∈E} log(1 − ρ_n(k)),  ρ_n(k) = 1 − D_n(μ∖{k})/D_n(μ).
[2] Saturation bound for the pure power (atoms k⁻², weights 2k⁻²): C(k,n) := log D_n(μ) − log D_n(μ∖{k})
    ≥ 2n·g(k/n) − log(W_{>n}/w_k),  g(θ) := (2−θ)log(1/θ) + (1−θ)log(1−θ) − 2 + θ.
[3] Move-map ratio: for S collision-free, term(S)/term(S′) with S′ = S moved down on E′ (pure power) vs the bound.
Measures are truncated at 40n atoms (the inequalities hold for any finite measure)."""
import mpmath as mp, math, itertools, random
mp.mp.dps = 300
def logD(idx, n):
    X = [mp.mpf(1)/mp.mpf(i)**2 for i in idx]; W = [2*x for x in X]; K = len(X)
    h = mp.fsum(W); out = n*mp.log(h); P = [1/mp.sqrt(h)]*K; Pp = None; bp = None
    for j in range(1, n):
        al = mp.fsum(W[i]*X[i]*P[i]**2 for i in range(K))
        Q = [(X[i]-al)*P[i] - (bp*Pp[i] if Pp is not None else 0) for i in range(K)]
        b2 = mp.fsum(W[i]*Q[i]**2 for i in range(K)); bb = mp.sqrt(b2)
        out += (n-j)*mp.log(b2); Pp, P = P, [q/bb for q in Q]; bp = bb
    return out
g = lambda t: (2-t)*math.log(1/t) + (1-t)*math.log(1-t) - 2 + t
for n in [16, 24]:
    Ka = 40*n; full = list(range(1, Ka+1)); D0 = logD(full, n)
    C = {k: D0 - logD([i for i in full if i != k], n) for k in range(1, n)}
    print(f"[2] n={n}: " + "  ".join(f"k={k}: C={float(C[k]):.2f} ≥ {2*n*g(k/n) - math.log(sum(2/l**2 for l in range(n+1,Ka+1))/(2/k**2)):.2f}" for k in [1,2,4,8,n//2]) +
          f"   all k<n OK: {all(float(C[k]) >= 2*n*g(k/n) - math.log(sum(2/l**2 for l in range(n+1,Ka+1))/(2/k**2)) - 1e-9 for k in range(1,n))}")
    for E in [[3,5,7], [2,9,11,15], list(range(4, n//2, 2))]:
        lhs = logD([i for i in full if i not in E], n) - D0
        rhs = -mp.fsum(C[k] for k in E)
        print(f"[1] n={n} E={E}: log D(μ∖E) − log D(μ) = {float(lhs):.3f} ≤ −Σ C(k) = {float(rhs):.3f}: {lhs <= rhs}")
# [3] move-map ratio on explicit Heine terms (pure power, small sets)
random.seed(23)
def logterm(S):
    return sum(math.log(2/k**2) for k in S) + 2*sum(math.log(abs(1/a**2 - 1/b**2)) for a, b in itertools.combinations(S, 2))
worst = 0
for _ in range(2000):
    n = random.randint(5, 30); S = sorted(random.sample(range(1, 3*n), n))
    Ep = [k for k in S if k > 2 and (k-1) not in S and random.random() < 0.5]
    Ep = [k for i, k in enumerate(Ep) if i == 0 or Ep[i-1] != k-1]
    Sp = sorted([k-1 if k in Ep else k for k in S])
    r = logterm(S) - logterm(Sp); bound = sum(2*(math.log(k) + 2) + math.log(4) for k in Ep)
    worst = max(worst, r - bound)
print(f"[3] 2000 random collision-free S: max (log term(S) − log term(S′) − Σ_moved[2(log k + 2) + log 4]) = {worst:.3f} (≤ 0 required)")
