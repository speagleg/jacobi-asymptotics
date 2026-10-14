"""Plan 14 A3/A5 probe (NUMERICAL): the comparison measure.
sigma_zeta has masses 2x_j; sigma_tilde has the same nodes with masses 2x_j / Lambda(x_j), Lambda = log(gamma/2pi),
gamma = sqrt(1/x - 1/4) (the log factor removed from the hard-edge weight; tail quadrature nodes treated the same way).
Both share the nodes, hence the constrained equilibrium and beta_N (Lemma E1).  Prediction (Plan 14, C-D comparison):
b_N(sigma_zeta)/b_N(sigma_tilde) - 1 = O(1/(N log N)), likewise for a_N/(2b_N).
Also a control: masses 2x_j * Lambda(x_j) (log squared) should differ by the same order with the opposite sign."""
import numpy as np
from jacobi_asym.measures import smooth_zeta
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi import jacobi_coeffs

ns = np.array([50, 100, 200, 400, 800, 1600, 3200])

def coeffs(mu, n):
    r = jacobi_coeffs(mu, n)
    b = np.sqrt(r.b2) if hasattr(r, "b2") else r.b
    return np.asarray(b), np.asarray(r.a)

for J in (400_000, 800_000):
    mu = smooth_zeta(J)
    x, w = mu.atoms, mu.weights
    Lam = np.log(np.sqrt(1 / x - 0.25) / (2 * np.pi))
    assert Lam.min() > 0
    out = {}
    for name, ww in (("zeta", w), ("tilde", w / Lam), ("sq", w * Lam)):
        out[name] = coeffs(DiscreteMeasure(x, ww, name), ns[-1] + 1)
    print(f"J={J}")
    print("    N   N*(b/bt-1)   N*logN*(b/bt-1)   N*(e-et)   N*logN*(e-et)   N*(bsq/b-1)")
    b, a = out["zeta"]; bt, at = out["tilde"]; bs, _ = out["sq"]
    for N in ns:
        i = N - 1
        rb = b[i] / bt[i] - 1
        de = a[i] / (2 * b[i]) - at[i] / (2 * bt[i])
        print(f"{N:5d}  {N*rb:+.5f}     {N*np.log(N)*rb:+.5f}        {N*de:+.5f}   {N*np.log(N)*de:+.5f}     {N*(bs[i]/b[i]-1):+.5f}")
