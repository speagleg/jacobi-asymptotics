"""Plan 27 (NUMERICAL, long double RKPW as in check_tailsum.py): (CL) / tail-Cesàro a-law for ROUGH weights, p = 2.
Atoms x_k = k^{-2}, k ≤ K; weights (a) smooth k^{-2}; (b) parity k^{-2}(1 + ½(−1)^k); (c) random k^{-2}·U[½, 3/2]
(seed 27). Prints n^{p−1}Σ_{j≥n} a_j = n^{p-1}(Tr J − Σ_{j<n} a_j) vs 2c(p)/(p−1); this equals n^{p−1}E_n[Σ_{k∉S}x_k]
by A2 (up to the n vs n−1 shift), i.e. the (CL) quantity. Also prints a_n/(2b_n) at n = 1600 to show that rough
weights may keep the *pointwise* ratio off 1 (A4 claims only the tail-Cesàro form)."""
import numpy as np
from jacobi_asym.laws.weyl import c_p
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
p, K = 2.0, 200_000
k = np.arange(1, K+1, dtype=float); x = k**-p
rng = np.random.default_rng(27)
Wts = {"smooth": k**-2, "parity": k**-2*(1+0.5*(-1)**k), "random": k**-2*rng.uniform(0.5, 1.5, K)}
target = 2*c_p(p)/(p-1)
for name, w in Wts.items():
    r = jacobi_coeffs(DiscreteMeasure(atoms=x, weights=w), 3201, prec="ld")
    a = np.asarray(r.a, float); b = np.sqrt(np.asarray(r.b2, float))
    trJ = np.sum(x) + x[-1]*K/(p-1)
    row = [f"n={n}: {n**(p-1)*(trJ - np.sum(a[:n-1])):.6f}" for n in (100, 400, 1600, 3200)]
    print(f"{name:7s}: n^(p-1)Σ_(j≥n)a_j  " + "  ".join(row) + f"   target 2c/(p-1)={target:.6f}   a_n/(2b_n) at n=1599,1600: {a[1598]/(2*b[1599]):.4f}, {a[1599]/(2*b[1600]):.4f}")
