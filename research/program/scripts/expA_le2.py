"""E1b (NUMERICAL): local-exponent prediction R_n ≈ c(p_loc(n))/c(p) beyond p = 2 / log-type:
(i) p = 1, L = log(k+e), w = k^{-2}; (ii) p = 2, L = exp(sqrt(log(k+e))) (D(γ) = ∞ type), w = k^{-2}.
Reports obs/pred where pred = c(p_loc)/c(p) and also obs/pure (pure power same p, s) to remove the 1/n terms."""
import numpy as np
from scipy.special import gamma
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
def c(p): I = np.sqrt(np.pi)/2*gamma(1/p+.5)/gamma(1/p+1); return .25*(np.pi/(2*I))**p
def run(p, L, K, N, ns):
    k = np.arange(1, K+1, dtype=float); w = k**-2.0
    out = []
    for LL in (lambda k: np.ones_like(k), L):
        x = k**-p*LL(k); r = jacobi_coeffs(DiscreteMeasure(x, w), N, prec="ld")
        b = np.sqrt(np.asarray(r.b2, float)); out.append(np.array([b[n]/(c(p)*x[n-1]) for n in ns]))
    h = 1e-5; nn = np.array(ns, float)
    f = lambda t: t**-p*L(t)
    pl = -nn*(np.log(f(nn+h))-np.log(f(nn-h)))/(2*h)
    return out[1], out[0], c(pl)/c(p), pl
for (p, L, nm, Ks, N, ns) in ((1.0, lambda k: np.log(k+np.e), "p=1,L=log", (200000, 400000), 401, (25, 50, 100, 200, 400)),
                              (2.0, lambda k: np.exp(np.sqrt(np.log(k+np.e))), "p=2,L=exp(sqrt log)", (100000, 200000), 801, (50, 100, 200, 400, 800))):
    for K in Ks:
        R, R0, pred, pl = run(p, L, K, N, ns)
        print(f"{nm} K={K}: n={ns} p_loc " + " ".join(f"{v:.3f}" for v in pl) + " | R/R_pure " + " ".join(f"{v:.5f}" for v in R/R0)
              + " | pred " + " ".join(f"{v:.5f}" for v in pred) + " | (R/R_pure)/pred " + " ".join(f"{v:.5f}" for v in R/R0/pred), flush=True)
