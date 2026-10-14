"""Plan 13 Phase 0 (NUMERICAL): pointwise Law P baseline for the smooth-zeta model (toolkit smooth_zeta: atoms
x_j = 1/(gamma_j^2 + 1/4), gamma_j = N0^{-1}(j - 1/2), weights 2 x_j, smooth Riemann-von Mangoldt tail).
Reports r_n := b_n/x_n vs c(2) = pi^2/16 and e_n := a_n/(2 b_n) - 1, and fits the deviation against 1/log n,
1/log^2 n and 1/n to see the actual rate.  J-doubling stability.  Indexing as README (b[n-1]/atoms[n-1])."""
import numpy as np
from jacobi_asym.measures import smooth_zeta
from jacobi_asym.jacobi import jacobi_coeffs

c2 = np.pi ** 2 / 16
ns = np.array([50, 100, 200, 400, 800, 1600, 3200])
res = {}
for J in (400_000, 800_000):
    mu = smooth_zeta(J)
    r = jacobi_coeffs(mu, ns[-1] + 1)
    b = np.sqrt(r.b2) if hasattr(r, "b2") else r.b
    res[J] = (b, r.a, mu.atoms)
b, a, x = res[800_000]
b4, a4, _ = res[400_000]
print(" n    b_n/x_n - c2     a_n/(2b_n) - 1     n*(dev_b)   log(n)*dev_b   (J-halving diff of b)")
for n in ns:
    db = b[n - 1] / x[n - 1] - c2
    ea = a[n - 1] / (2 * b[n - 1]) - 1
    print(f"{n:5d}  {db:+.6e}   {ea:+.6e}   {n*db:+.4f}   {np.log(n)*db:+.5f}   {abs(b4[n-1]/b[n-1]-1):.1e}")
