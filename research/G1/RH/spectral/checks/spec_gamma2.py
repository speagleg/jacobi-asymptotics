"""SPEC probe 2b: where does the d2 shift of the (k + g/k)^p lattice come from? Variants (p, s fixed):
  'kmin K0': index correction g/k only for k > K0 (far nodes untouched);  'pow m': index correction g/k^m.
Reports Delta d2 = n^-2 coefficient of n(y - y_lat) after removing the exact zeta-layer change (first order: Delta eps1 n^-p)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import run, NMAX, c_p_mp
from so_coeffs import coeffs
from so_fit import sequences
p, s, g, mode, val = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], float(sys.argv[5])
K = (200 if p < 1 else 100)*NMAX; k = np.arange(1, K + 1, dtype=np.float64)
if mode == 'kmin': corr = np.where(k > val, g/k, 0.0)
else: corr = g/k**val
n, y = run(f"gamma2_p{p}_s{s}_g{g}_{mode}{val}", (k + corr)**p, p, s, 0.0, K)
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
c = float(c_p_mp(p)); mp.mp.dps = 20
def Zreg(terms=8, kex=3000):
    # regularised Delta Z(-1) = sum_k [(k + corr_k)^p - k^p]: term-wise zeta regularisation of the 1/k^m expansion, minus the
    # unmodified head k <= kmin for the 'kmin' variant (a plain truncated sum diverges for p >= m + 1)
    q = mp.mpf(p); mm = 1 if mode == 'kmin' else int(val)
    full = sum(mp.binomial(q, i)*mp.mpf(g)**i*mp.zeta((mm + 1)*i - q) for i in range(1, terms)) + \
           sum((mp.mpf(kk) + mp.mpf(g)/mp.mpf(kk)**mm)**q - sum(mp.binomial(q, i)*mp.mpf(g)**i*mp.mpf(kk)**(q - (mm + 1)*i) for i in range(terms)) for kk in range(1, kex + 1))
    if mode == 'kmin': full -= sum((mp.mpf(kk) + mp.mpf(g)/kk)**q - mp.mpf(kk)**q for kk in range(1, int(val) + 1))
    return full
dZ1 = float(Zreg())
D = n*(y - y0) - 2*p*c*dZ1*n**(-p)
for lo in (200, 400, 800):
    m = n >= lo
    E = [1.0, 2.0, 1 + p, 2 + p, 3.0] if p > 1 else [1.0, 2.0, 2*p, 1 + p, 3*p]
    A = np.vstack([n[m]**-e for e in E]).T; co = np.linalg.lstsq(A, D[m], rcond=None)[0]
    print(f"p={p} s={s} g={g} {mode}={val}: n >= {lo}: Delta d2 = {co[0]:+.6f}  (Delta d2 / g = {co[0]/g:+.6f};  pi/sqrt3 = {np.pi/np.sqrt(3):.6f})")
