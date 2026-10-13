"""Corollary HZ, Rule A (NUMERICAL).
[1] Indexing: det_{1<=i,j<=n} zeta(a(i+j)+b) equals D_n of sum_k k^{-(2a+b)} delta_{k^{-a}} (Heine/H2 via toolkit b_j),
    checked by mpmath determinants for small n.
[2] Averaged law for the HZ weights: S_n -> 0 for (a,b) = (3,1), (4,1)."""
import mpmath as mp
import numpy as np
from jacobi_asym.measures.powers import pure_power
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.averaged import averaged_law

mp.mp.dps = 120
for a, b in [(3, 1), (4, 1), (3, 2)]:
    s = 2 * a + b
    mu = pure_power(a, 4000, s=s)
    jc = jacobi_coeffs(mu, 12, method="mp", dps=120)
    for n in (4, 8, 12):
        M = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                M[i, j] = mp.zeta(a * (i + j + 2) + b)
        lhs = mp.log(mp.det(M))
        # D_n = m0^n prod_{j<n} b_j^{2(n-j)}, b2[i] = b_{i+1}^2 ; m0 = zeta(s) (full measure; K=4000 truncation is
        # negligible at this precision only for the moments used by mp? use exact m0)
        m0 = mp.zeta(s)
        rhs = n * mp.log(m0) + sum((n - j) * mp.log(mp.mpf(jc.b2[j - 1])) for j in range(1, n))
        print(f"[1] a={a} b={b} n={n}: log det zeta = {mp.nstr(lhs, 12)}  log D_n(toolkit, K=4000) = {mp.nstr(rhs, 12)}")
for a, b, K in [(3, 1, 20000), (4, 1, 6000)]:
    mu = pure_power(a, K, s=2 * a + b)
    ns = [25, 50, 100, 200, 400]
    bb = np.asarray(jacobi_coeffs(mu, max(ns), prec="ld").b, float)
    S = averaged_law(bb, mu.atoms, a, ns)
    print(f"[2] a={a} b={b}: S_n " + " ".join(f"{n}:{S[n]:+.4f}" for n in ns))
