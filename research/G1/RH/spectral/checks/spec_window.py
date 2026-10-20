"""Localise the jitter noise: iid jitter only on nodes k in [k1, k2]. Soft-edge threshold node k*(n) = n/(4c)^{1/p}."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_common import *
p, s, A, k1, k2 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); K = 200*NMAX
xi = np.random.default_rng(1).uniform(-A, A, K); kk = np.arange(1, K+1); xi[(kk < k1) | (kk > k2)] = 0
k = kk.astype(np.float64); lam = (k+xi)**p
dZ = float(np.sum((k+xi)**p - k**p)); c = c_p_mp(p); e1 = float(2*p*c*(mp.zeta(-p) + dZ))
print(f"k*(n) = n * {float(1/(4*c)**(1/p)):.4f}")
n, y = run(f"win_p{p}_s{s}_A{A}_{k1}_{k2}", lam, p, s, 0.0, K)
for lo in (100, 200, 400, 800):
    m = n >= lo
    v1, h1 = fit(n[m], y[m], p, [], 1.0, fr=(0.1, 0.2, 0.3))
    v, h = fit(n[m], (y + (s-1)/(2*n))[m], p, [1.0], 1+p)
    print(f"window [{k1},{k2}] fit from n>={lo}: d1 {v1:+.7f} ({h1:.1e}) pred {-(s-1)/2:+.4f} | eps1 {v:+.6f} ({h:.1e}) pred(reg Z) {e1:+.6f} unjittered {float(2*p*c*mp.zeta(-p)):+.6f}")
r = y + (s-1)/(2*n) - e1*n**(-1-p); m = n >= 50
E = sorted({round(1+i+j*p, 9) for i in range(4) for j in range(6)} - {1.0})[:7]
Am = np.vstack([n[m]**-e for e in E]).T; res = r[m] - Am @ np.linalg.lstsq(Am, r[m], rcond=None)[0]; nn = n[m]
for lo in (50, 100, 200, 400, 800):
    sel = (nn >= lo) & (nn < 2*lo); print(f"  residual RMS [{lo},{2*lo}): {np.sqrt(np.mean(res[sel]**2)):.2e}")
