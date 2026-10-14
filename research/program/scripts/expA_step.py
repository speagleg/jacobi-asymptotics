"""Problem A, experiment E3 (NUMERICAL): integrated node kernel U_j for the pure power p = s = 2.
U_j := resp(1_{k>j}) − 2·1_{j<n}, resp = d log b_n^2/d eps under x_k -> x_k e^{eps g_k} (central differences).
Summation by parts: d log b_n^2 = 2 g_n + Σ_j (jΔg_j)(U_j/j). Reports U at j = lam n and Σ_j |U_j|/j over the lam grid."""
import sys, numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
p = 2.0; s = 2.0
n = int(sys.argv[1]); K = 200*n; eps = 1e-5
k = np.arange(1, K+1, dtype=float); x0 = k**-p; w = k**-s
def logb2(g, e):
    r = jacobi_coeffs(DiscreteMeasure(x0*np.exp(e*g), w), n+2, prec="ld")
    return np.log(float(r.b2[n]))
def resp(g): return (logb2(g, eps) - logb2(g, -eps))/(2*eps)
lams = 2.0**(np.arange(-12, 13)/2)
U = []
for lam in lams:
    j = max(1, int(round(lam*n)))
    U.append(resp((k > j).astype(float)) - 2.0*(j < n))
U = np.array(U)
print(f"n={n}: lam " + " ".join(f"{l:7.3g}" for l in lams))
print(f"n={n}: U   " + " ".join(f"{u:+7.3f}" for u in U))
# Σ_j |U_j|/j ≈ ∫ |U| dlam/lam = Σ |U| * (log 2)/2 on the grid
print(f"n={n}: int|U| dlog(lam) ≈ {np.abs(U).sum()*np.log(2)/2:.3f}; max|U| = {np.abs(U).max():.3f}")
