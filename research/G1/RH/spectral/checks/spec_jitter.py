"""Jittered lattice: nodes (k+xi_k)^{-p}, weights (k+xi_k)^{-s}, xi_k iid U(-A, A) (seed 1), k <= K.
Prediction: d1 unchanged; eps1 = 2pc Z(-1), Z(-1) = zeta(-p) + sum_k [(k+xi_k)^p - k^p]; fluctuation floor ~ n^{-3/2}."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_common import *
p, s, A = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]); K = 200*NMAX
xi = np.random.default_rng(1).uniform(-A, A, K)
k = np.arange(1, K+1, dtype=np.float64)
lam = (k+xi)**p
dZ = float(np.sum((k+xi)**p - k**p))
c = c_p_mp(p); e1 = float(2*p*c*(mp.zeta(-p) + dZ)); e10 = float(2*p*c*mp.zeta(-p))
n, y = run(f"jitter_p{p}_s{s}_A{A}", lam, p, s, 0.0, K)
v1, h1 = fit(n, y, p, [], 1.0)
v, h = fit(n, y + (s-1)/(2*n), p, [1.0], 1+p)
print(f"jitter p={p} s={s} A={A}: d1 fit {v1:+.8f} ({h1:.1e}) pred {-(s-1)/2:+.8f}")
print(f"  n^-1-p fit {v:+.7f} ({h:.1e}) pred eps1 {e1:+.7f} diff {v-e1:+.1e} [unjittered {e10:+.7f}; partial sums dZ to K/10, K: "
      f"{float(np.sum(((k+xi)**p - k**p)[:K//10])):+.5f}, {dZ:+.5f}]")
# fluctuation floor: residual after a smooth fit on n >= 100 (exponents up to ~3.5), RMS in octaves
r = y + (s-1)/(2*n) - e1*n**(-1-p)
m = n >= 100
E = sorted({round(1+i+j*p, 9) for i in range(4) for j in range(6)} - {1.0})[:7]
Am = np.vstack([n[m]**-e for e in E]).T
res = r[m] - Am @ np.linalg.lstsq(Am, r[m], rcond=None)[0]
nn = n[m]
for lo in (100, 200, 400, 800):
    sel = (nn >= lo) & (nn < 2*lo)
    print(f"  residual RMS n in [{lo},{2*lo}): {np.sqrt(np.mean(res[sel]**2)):.2e}   (n^-3/2 at {lo}: {lo**-1.5:.2e})")
