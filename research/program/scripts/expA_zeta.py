"""Problem A, experiment E4 (NUMERICAL, long double RKPW): pointwise Law P for TRUE zeta ordinates (Odlyzko,
taken as real numbers: an input, not evidence; AGENTS rule 3) vs the smooth-zeta model. M tabulated ordinates
plus the smooth Riemann-von Mangoldt tail. Reports R_n := b_n/(c(2) x_n) and the jump |log(R_n/R_{n-1})|."""
import sys, numpy as np
from jacobi_asym.measures.lfun import true_zeta, smooth_zeta, load_odlyzko, model_zeros
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
c2 = np.pi**2/16; NMAX = 1201
for M in (100000, 200000):
    out = {}
    for nm, mu, g in (("true", true_zeta(M), load_odlyzko(M)), ("smooth", smooth_zeta(M), model_zeros(M))):
        r = jacobi_coeffs(mu, NMAX, prec="ld")
        b = np.sqrt(np.asarray(r.b2, float)); a = np.asarray(r.a, float)
        x = 1/(np.asarray(g, float)**2 + .25)
        n = np.arange(1, NMAX-1)
        R = b[n]/(c2*x[n-1]); A = a[n]/(2*b[n])
        out[nm] = (R, A)
    Rt, At = out["true"]; Rs, As = out["smooth"]
    for lo, hi in ((50, 100), (100, 200), (200, 400), (400, 800), (800, 1199)):
        sl = slice(lo-1, hi-1)
        jt = np.abs(np.diff(np.log(Rt)))[sl]; js = np.abs(np.diff(np.log(Rs)))[sl]
        d = np.abs(np.log(Rt/Rs))[sl]
        print(f"M={M} n in [{lo},{hi}): true R mean {Rt[sl].mean():.4f} (min {Rt[sl].min():.4f}, max {Rt[sl].max():.4f}); "
              f"smooth R mean {Rs[sl].mean():.4f}; max|log Rt/Rs| {d.max():.3f}, mean {d.mean():.4f}; "
              f"max jump true {jt.max():.3f} (mean {jt.mean():.4f}) vs smooth {js.max():.1e}; "
              f"A_true range [{At[sl].min():.3f},{At[sl].max():.3f}]", flush=True)
