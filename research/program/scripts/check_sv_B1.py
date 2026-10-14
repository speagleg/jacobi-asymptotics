"""Problem B numerics [1]: p=s=2, Psi = exp(sqrt(log(k+e))) and exp(log(k+e)^0.8).
|beta_n(vPsi)/beta_n(v)-1| vs n, normalized by eps_n/n with eps_n = L'(log n); also vs tilted pure power k^{-(s-eps_n)}."""
import numpy as np, sys
sys.path.insert(0, "/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/src")
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p = 2.0; NS = (100, 200, 400, 800, 1600, 3200)
def coeffs(K, logpsi, N=3201):
    k = np.arange(1, K+1, dtype=float)
    lw = -2.0*np.log(k) + logpsi(k); lw -= lw.max()
    r = jacobi_coeffs(DiscreteMeasure(k**-p, np.exp(lw)), N, prec="ld")
    b = np.sqrt(np.asarray(r.b2, float)); a = np.asarray(r.a, float)
    return np.arange(len(b))**p*b/c_p(p), (np.arange(len(a))+1)**p*a/(2*c_p(p))
cases = {"sqrt": (lambda k: np.sqrt(np.log(k+np.e)), lambda t: 0.5/np.sqrt(t)),
         "th0.8": (lambda k: np.log(k+np.e)**0.8, lambda t: 0.8*t**-0.2)}
for K in (120000, 480000):
    B0, A0 = coeffs(K, lambda k: 0*k)
    for name, (lp, dL) in cases.items():
        B1, A1 = coeffs(K, lp)
        dev = [abs(B1[n]/B0[n]-1) for n in NS]; adev = [abs(A1[n]-A0[n]) for n in NS[:-1]]
        print(f"K={K} {name}: |b-dev| " + ", ".join(f"{d:.2e}" for d in dev)
              + " | n*dev/eps_n " + ", ".join(f"{n*d/dL(np.log(n)):.3f}" for n, d in zip(NS, dev))
              + " | |A-dev| " + ", ".join(f"{d:.1e}" for d in adev), flush=True)
