"""Problem A, experiment E1 (NUMERICAL, long double RKPW): pointwise Law P for non-pure-power nodes.
Reports R_n := b_n/(c(p) f(n)) and A_n := a_n/(2 b_n) for several node families, K vs 2K."""
import sys, numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p
p = 2.0; s = 2.0; c = c_p(p)
NMAX = 1601
def fam(name, K):
    k = np.arange(1, K+1, dtype=np.longdouble)
    if name == "pure":   x = k**-p
    elif name == "log1": x = k**-p*np.log(k+np.e)          # L = log k
    elif name == "logm2": x = k**-p*np.log(k+np.e)**-2     # L = log^-2 k
    elif name == "sinll": x = k**-p*(2+np.sin(np.log(np.log(k+3))))  # bounded slowly varying, smooth
    elif name == "Ha":   x = k**-p*(1+1/np.log(k+2))       # (H-a), L -> 1 slowly (non-analytic-type rate)
    elif name.startswith("par"):                            # rough spacings: Δx_k = p k^{-p-1}(1+eps(-1)^k)
        eps = float(name[3:]); d = p*k**(-p-1)*(1+eps*(-1)**np.arange(1, K+1))
        tail = np.cumsum(d[::-1])[::-1]; x = tail + (K+1.0)**-p  # x_k = sum_{j>=k} d_j + tail
    w = k**-s
    return np.asarray(x, float), np.asarray(w, float)
def run(name, K):
    x, w = fam(name, K)
    r = jacobi_coeffs(DiscreteMeasure(x, w), NMAX, prec="ld")
    a = np.asarray(r.a, float); b = np.sqrt(np.asarray(r.b2, float))
    return a, b, x
ns = (50, 100, 200, 400, 800, 1600)
for name in sys.argv[1:]:
    for K in (100000, 200000):
        a, b, x = run(name, K)
        # f(n): node at index n (1-based atoms: x[n-1] = f(n))
        R = [b[n]/(c*x[n-1]) for n in ns]; A = [a[n]/(2*b[n]) for n in ns]
        osc = [abs(np.log(b[n]*x[n-2]/(b[n-1]*x[n-1]))) for n in ns]  # |log(R_n/R_{n-1})|
        print(f"{name:7s} K={K}: R_n " + " ".join(f"{v:.5f}" for v in R) + " | A_n " + " ".join(f"{v:.5f}" for v in A)
              + " | |dlogR| " + " ".join(f"{v:.1e}" for v in osc), flush=True)
