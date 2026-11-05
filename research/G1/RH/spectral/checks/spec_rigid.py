"""Rigid jitter: xi_k = A (eta_k - eta_{k-1}), eta iid U(-1/2,1/2): node displacements whose partial sums stay bounded."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_common import *
p, s, A = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]); K = 200*NMAX
eta = np.random.default_rng(2).uniform(-0.5, 0.5, K+1); xi = A*(eta[1:] - eta[:-1])
k = np.arange(1, K+1, dtype=np.float64); lam = (k+xi)**p
dZ = float(np.sum((k+xi)**p - k**p)); c = c_p_mp(p); e1 = float(2*p*c*(mp.zeta(-p) + dZ))
n, y = run(f"rigid_p{p}_s{s}_A{A}", lam, p, s, 0.0, K)
v1, h1 = fit(n, y, p, [], 1.0); v, h = fit(n, y + (s-1)/(2*n), p, [1.0], 1+p)
print(f"rigid p={p} s={s} A={A}: d1 fit {v1:+.8f} ({h1:.1e}) pred {-(s-1)/2:+.8f}; n^-1-p fit {v:+.6f} ({h:.1e}) pred {e1:+.6f} [dZ {dZ:+.5f}]")
r = y + (s-1)/(2*n) - e1*n**(-1-p); m = n >= 100
E = sorted({round(1+i+j*p, 9) for i in range(4) for j in range(6)} - {1.0})[:7]
Am = np.vstack([n[m]**-e for e in E]).T; res = r[m] - Am @ np.linalg.lstsq(Am, r[m], rcond=None)[0]; nn = n[m]
for lo in (100, 200, 400, 800):
    sel = (nn >= lo) & (nn < 2*lo); print(f"  residual RMS [{lo},{2*lo}): {np.sqrt(np.mean(res[sel]**2)):.2e}")
