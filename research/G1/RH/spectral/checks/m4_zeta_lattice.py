"""JZC M4 section 6: lattice cross-check of the zeta-layer dressing. After subtracting the exact integer layer (1 + f2 N^-2 +
f4 N^-4 + f6 N^-6) and the bare zeta terms eps_j N^{-1-jp} from F(N) = (N/n)^p n^p b_n/c, fit the remainder on mid-range windows
with exponents {k + jp : k = 2, 3, 4; j = 1, 2} (< 7.6) plus 8, 10. Checks: N^{-2-p} coefficient = 0; N^{-3-p} coefficient =
eps_1 g_1(p, alpha) (m4_zeta_dressing.py: A_1 + B_1 alpha^2)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import NMAX, Checks
from m4_rh4 import f4_closed, f6_closed
C_ = Checks()
A1 = lambda p: (p + 1)*(p**2 + 3*p - 2)/(24*p); B1 = lambda p: (p + 2)*(p**2 + 2*p + 2)/(8*p)
for p, a in ((1.5, 0.0), (1.5, 1.0), (2.5, 0.0), (2.5, 0.5)):
    s = 1 + p*(1 + a); mp.mp.dps = 30; c = c_p_mp(p)
    eps = {j: float(mp.binomial(2*j, j)*p*c**j*mp.zeta(-j*p)) for j in range(1, 9)}
    al, b = coeffs(p, s, 100*NMAX, NMAX); n, y, *_ = sequences(p, al, b)
    N = n + a/2 + .5; F = (N/n)**p*(1 + y)
    f2 = -(p + 2)*a**2/8 + (p + 1)/12; f4 = float(f4_closed(mp.mpf(p), mp.mpf(a))); f6 = float(f6_closed(mp.mpf(p), mp.mpf(a)))
    R = F - 1 - f2*N**-2. - f4*N**-4. - f6*N**-6. - sum(e*N**(-1 - j*p) for j, e in eps.items() if 1 + j*p < 9)
    tgt = sorted({round(k + j*p, 9) for k in (2, 3, 4) for j in (1, 2) if k + j*p < 7.6})
    out = {e: [] for e in tgt}
    for lo, hi in ((8, 150), (10, 200), (15, 300), (20, 400)):
        for X in ([], [8.0], [8.0, 10.0]):
            E = tgt + X; sel = (n >= lo) & (n <= hi); A = np.vstack([N[sel]**-e for e in E]).T
            co = np.linalg.lstsq(A*N[sel, None]**tgt[0], R[sel]*N[sel]**tgt[0], rcond=None)[0]
            for e in tgt: out[e].append(co[E.index(e)])
    med = {e: (np.median(v), (max(v) - min(v))/2) for e, v in out.items()}
    e2, e3 = round(2 + p, 9), round(3 + p, 9); pred = eps[1]*(A1(p) + B1(p)*a**2)
    print(f"p={p} alpha={a:+.2f}: N^-(2+p) {med[e2][0]:+.2e} ({med[e2][1]:.0e});  N^-(3+p) {med[e3][0]:+.6e} ({med[e3][1]:.0e})"
          f"  pred eps1*g1 = {pred:+.6e}  diff {med[e3][0] - pred:+.1e}", flush=True)
    C_.check(f"p={p} a={a}: N^-(2+p) = 0", med[e2][0], 0.0, max(3*med[e2][1], 1e-7))
    C_.check(f"p={p} a={a}: N^-(3+p) = eps1 g1", med[e3][0], pred, max(3*med[e3][1], 1e-6))
C_.finish()
