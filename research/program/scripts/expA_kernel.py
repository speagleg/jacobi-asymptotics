"""Problem A, experiment E2 (NUMERICAL, long double RKPW, central differences):
node-transport response of log b_n^2 to moving atoms x_k -> x_k e^{eps g_k} (pure power p = s = 2, K = 200n).
Smooth bump g_k = phi((log k - log(lam n))/h); rough bump g_k = (-1)^k (p/k) phi(...) (shift = phi * fraction of a spacing).
Identity check: g == 1 gives exactly 2 (scaling). Reports R(lam) = d log b_n^2 / d eps."""
import sys, numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
p = 2.0; s = 2.0; h = 0.25
n = int(sys.argv[1]); K = 200*n; eps = 1e-5
k = np.arange(1, K+1, dtype=float); x0 = k**-p; w = k**-s
def logb2(g, e):
    r = jacobi_coeffs(DiscreteMeasure(x0*np.exp(e*g), w), n+2, prec="ld")
    return np.log(float(r.b2[n]))
def resp(g): return (logb2(g, eps) - logb2(g, -eps))/(2*eps)
print(f"n={n} K={K}: constant g -> {resp(np.ones(K)):.6f} (exact 2)")
lams = 2.0**(np.arange(-10, 15)/2)
rs, rr = [], []
for lam in lams:
    phi = np.exp(-0.5*((np.log(k) - np.log(lam*n))/h)**2)
    rs.append(resp(phi)); rr.append(resp(((-1.0)**k)*(p/k)*phi))
rs, rr = np.array(rs), np.array(rr)
norm = 0.5*np.log(2)/(h*np.sqrt(2*np.pi))   # partition-of-unity factor: sum_j phi_j ~ 1/norm
print("lam      " + " ".join(f"{l:8.3g}" for l in lams))
print("smooth   " + " ".join(f"{v:+8.4f}" for v in rs))
print("rough    " + " ".join(f"{v:+8.4f}" for v in rr))
print(f"sum smooth * norm = {rs.sum()*norm:.4f} (should be ~2); sum|smooth|*norm = {np.abs(rs).sum()*norm:.4f}; max|smooth| = {np.abs(rs).max():.4f}; max|rough| = {np.abs(rr).max():.4f}")
