"""Problem B numerics [3]: oscillating non-log-type Psi, L(tau)=sqrt(tau)*sin(log tau), tau=log(k+e); p=s=2.
Tilt prediction: beta_w/beta_v - 1 ~ L'(log n)/(2n) (from d1 = -(s-1)/2 of the pure power)."""
import numpy as np, sys
sys.path.insert(0, "/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/src")
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p = 2.0; NS = (100, 200, 400, 800, 1600, 3200)
L = lambda t: np.sqrt(t)*np.sin(np.log(t)); dL = lambda t: np.sin(np.log(t))/(2*np.sqrt(t)) + np.cos(np.log(t))/np.sqrt(t)
def B(K, lpsi):
    k = np.arange(1, K+1, dtype=float); lw = -2*np.log(k) + lpsi(k); lw -= lw.max()
    r = jacobi_coeffs(DiscreteMeasure(k**-p, np.exp(lw)), 3202, prec="ld")
    return np.arange(3202)**p*np.sqrt(np.asarray(r.b2, float))[:3202]/c_p(p)
for K in (240000, 480000):
    Bv = B(K, lambda k: 0*k); Bw = B(K, lambda k: L(np.log(k+np.e)))
    print(f"K={K}: dev " + ", ".join(f"{Bw[n]/Bv[n]-1:+.2e}" for n in NS) + " | pred L'/(2n) "
          + ", ".join(f"{dL(np.log(n+np.e))/(2*n):+.2e}" for n in NS), flush=True)
