"""Plan 29 (NUMERICAL, long double RKPW as in check_regularity.py): pointwise b-law for decaying rough weight perturbations.
x_k = k^{-2}, w_k = k^{-2}ψ_k with ψ_k → 1 (decaying roughness) vs a non-decaying rough ψ (control).
Prints |β_n(ψ)/β_n(1) − 1| (relative to the pure power) and the local oscillation mean|β_{m+1}/β_m − 1| over [n, 1.1n]."""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p, K, nmax = 2.0, 120000, 4000
k = np.arange(1, K+1, dtype=float); x = k**-p; v = k**-2.0
rng = np.random.default_rng(29)
psis = {"pure": np.ones(K),
        "parity/log": 1 + 0.5*(-1)**k/np.log(k+1),
        "random/√log": 1 + 0.5*rng.uniform(-1, 1, K)/np.sqrt(np.log(k+1)),
        "adversarial-ish ±0.5/log (signs random blocks)": 1 + 0.5*np.repeat(rng.choice([-1, 1], K//7+1), 7)[:K]/np.log(k+1),
        "parity (no decay)": 1 + 0.5*(-1)**k}
B = {}
for name, psi in psis.items():
    r = jacobi_coeffs(DiscreteMeasure(x, v*psi), nmax+2, prec="ld")
    b = np.sqrt(np.asarray(r.b2, float)); n = np.arange(len(b)); B[name] = n**p*b/c_p(p)
for name in psis:
    rel = [f"n={n}: {abs(B[name][n]/B['pure'][n]-1):.1e}" for n in (250, 500, 1000, 2000, 3600)]
    osc = [f"{np.abs(B[name][np.arange(n,int(1.1*n))+1]/B[name][np.arange(n,int(1.1*n))]-1).mean():.1e}" for n in (250, 1000, 3600)]
    print(f"{name:48s} |β(ψ)/β(1)−1|: " + "  ".join(rel) + "   osc@250,1000,3600: " + ", ".join(osc))
