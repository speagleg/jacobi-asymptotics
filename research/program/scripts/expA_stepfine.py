"""E3b (NUMERICAL): U_j for EVERY j in [n/4, 3n] (pure power p = s = 2), to estimate the summation-by-parts
constant B_n := Σ_j |U_j|/j and the max of |U_j| near the saturation/band boundary j ≈ 0.64 n."""
import sys, numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
p = 2.0; s = 2.0
n = int(sys.argv[1]); K = 100*n; eps = 1e-5
k = np.arange(1, K+1, dtype=float); x0 = k**-p; w = k**-s
def logb2(g, e):
    r = jacobi_coeffs(DiscreteMeasure(x0*np.exp(e*g), w), n+2, prec="ld")
    return np.log(float(r.b2[n]))
js = np.arange(n//4, 3*n+1)
U = np.array([(logb2((k > j)*1.0, eps) - logb2((k > j)*1.0, -eps))/(2*eps) - 2.0*(j < n) for j in js])
i = np.argmax(np.abs(U))
print(f"n={n}: B_n = sum_j |U_j|/j over [n/4,3n] = {np.sum(np.abs(U)/js):.3f}; max|U_j| = {abs(U[i]):.3f} at j/n = {js[i]/n:.3f};"
      f" sum_j U_j/j = {np.sum(U/js):+.3f}; #(|U_j|>1) = {(np.abs(U)>1).sum()}")
for lo, hi in ((0.25, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 1.0), (1.0, 1.5), (1.5, 3.0)):
    m = (js >= lo*n) & (js < hi*n)
    print(f"   j/n in [{lo},{hi}): sum|U|/j = {np.sum(np.abs(U[m])/js[m]):.3f}, max|U| = {np.abs(U[m]).max():.3f}")
