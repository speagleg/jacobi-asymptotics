"""Plan 34 (NUMERICAL, long double RKPW): merely slowly varying weights Ψ(k) = 2 + sin(log log(k+2)) (not polynomially
slowly varying), p = 2, s = 2. Reports |β_n(vΨ)/β_n(v) − 1| and |A_n(vΨ) − A_n(v)| (A_n := (n+1)^p a_n/(2c)) at
several n and their averages over [N, 2N], with K = 120000 | 240000."""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p = 2.0
def coeffs(K, psi):
    k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
    r = jacobi_coeffs(DiscreteMeasure(x, v*psi(k)), 3201, prec="ld")
    a = np.asarray(r.a, float); b = np.sqrt(np.asarray(r.b2, float)); nn = np.arange(len(b))
    return nn**p*b/c_p(p), (np.arange(len(a))+1)**p*a/(2*c_p(p))
for K in (120000, 240000):
    B0, A0 = coeffs(K, lambda k: np.ones_like(k)); B1, A1 = coeffs(K, lambda k: 2 + np.sin(np.log(np.log(k+2))))
    db = np.abs(B1/B0 - 1); da = np.abs(A1 - A0)
    print(f"K={K}: |β(Ψ)/β(1)−1| at n=200,400,800,1600,3200: " + ", ".join(f"{db[n]:.1e}" for n in (200, 400, 800, 1600, 3200)) +
          "  | avg over [N,2N], N=200,400,800,1600: " + ", ".join(f"{db[N:2*N].mean():.1e}" for N in (200, 400, 800, 1600)))
    print(f"          |A(Ψ)−A(1)| at the same n: " + ", ".join(f"{da[n]:.1e}" for n in (200, 400, 800, 1600, 3199)) +
          "  | avg: " + ", ".join(f"{da[N:2*N].mean():.1e}" for N in (200, 400, 800, 1600)), flush=True)
