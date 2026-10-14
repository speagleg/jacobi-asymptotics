"""Plan 36 (NUMERICAL, long double RKPW): unbounded log-type weights Ψ(k) = log(k+e)^α, α ∈ {1, −2, 3}, p = s = 2.
Reports |β_n(vΨ)/β_n(v) − 1| and |A_n(vΨ) − A_n(v)| (A_n := (n+1)^p a_n/(2c)) with K = 120000 | 240000."""
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
    B0, A0 = coeffs(K, lambda k: np.ones_like(k))
    for al in (1, -2, 3):
        B1, A1 = coeffs(K, lambda k: np.log(k+np.e)**al)
        print(f"K={K} alpha={al:+d}: |β(Ψ)/β(1)−1| at n=100,200,400,800,1600,3200: "
              + ", ".join(f"{abs(B1[n]/B0[n]-1):.1e}" for n in (100, 200, 400, 800, 1600, 3200))
              + " | |A(Ψ)−A(1)| at n=100,400,1600,3199: " + ", ".join(f"{abs(A1[n]-A0[n]):.1e}" for n in (100, 400, 1600, 3199)), flush=True)
