"""G1-a (NUMERICAL). For p > 1:
[1] Q_p := int_0^inf u^{-p} (1 - rho*(u)) du, rho*(u) = I_{min(1, u^{-p}/4c)}(1/p+1/2, 1/2) (G2 mu* density in u),
    vs 2c(p)/(p-1) (the value forced by a_j ~ 2c(p) j^{-p});
[2] n^{p-1} sum_{j>=n} a_j from the Jacobi coefficients of pure powers (tail completed with Tr J = sum x_k) vs Q_p."""
import numpy as np
from scipy import integrate, special
from jacobi_asym.laws.weyl import c_p
from jacobi_asym.measures.powers import pure_power
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

for p in [1.5, 2.0, 3.0, 4.0]:
    c = c_p(p); us = (4 * c) ** (-1 / p)
    f = lambda u: u ** (-p) * (1 - special.betainc(1 / p + 0.5, 0.5, min(1.0, u ** (-p) / (4 * c))))
    Q = integrate.quad(f, us, 50, limit=400)[0] + integrate.quad(f, 50, np.inf, limit=400)[0]
    print(f"[1] p={p}: Q_p = {Q:.8f}   2c/(p-1) = {2*c/(p-1):.8f}   ratio = {Q/(2*c/(p-1)):.8f}")
for p, K in [(2.0, 200_000), (3.0, 20_000)]:
    mu = pure_power(p, K, s=p)
    a = np.asarray(jacobi_coeffs(mu, 3000, prec="ld").a, float)
    trJ = np.sum(mu.atoms) + mu.atoms[-1] * K / (p - 1)        # sum x_k incl. tail estimate
    for n in (100, 400, 1600):
        tail = trJ - np.sum(a[:n - 1])                          # sum_{j>=n} a_j = Tr J - sum_{j<n} a_j
        print(f"[2] p={p} n={n}: n^(p-1) sum_(j>=n) a_j = {n**(p-1)*tail:.6f}   (2c/(p-1) = {2*c_p(p)/(p-1):.6f})")
