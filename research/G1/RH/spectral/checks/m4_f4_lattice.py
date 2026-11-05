"""JZC M4: lattice cross-check of the fourth-order closed form f4(p, alpha) (m4_rh4.py, JZC_M4.md section 5).
F(N) := (N/n)^p n^p b_n/c from the Plan 62 lattice coefficients, N = n + alpha/2 + 1/2. Subtract 1 + f2 N^-2 + sum_j eps_j N^{-1-jp}
(E3 zeta layer), multiply by N^4, and fit on a MID-RANGE window (the large-n end of the coefficients is noise-dominated at the
N^-4 scale: m4_natural_index's tail-window fits are what produced the spurious ~3e-4 'N^-3' residual at p = 1.5) with
exponents {3, 4, 5, 6} plus the non-integer cross exponents k + jp (k = 2, 3, 4). p is chosen so that no zeta exponent hits 4.
Checks: N^-3 coefficient = 0; N^-4 coefficient = f4 closed form."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import NMAX, Checks
from m4_rh4 import f4_closed
C_ = Checks()
for p, a in ((2.0, 0.0), (2.0, 1.0), (4.0, 0.0), (4.0, 1.0), (2.5, 0.5)):
    s = 1 + p*(1 + a)
    mp.mp.dps = 30; c = c_p_mp(p)
    eps = {j: float(mp.binomial(2*j, j)*p*c**j*mp.zeta(-j*p)) for j in range(1, 9)}
    al, b = coeffs(p, s, 100*NMAX, NMAX); n, y, *_ = sequences(p, al, b)
    N = n + a/2 + .5; F = (N/n)**p*(1 + y); f2 = -(p + 2)*a**2/8 + (p + 1)/12
    R = (F - 1 - f2*N**-2. - sum(e*N**(-1 - j*p) for j, e in eps.items() if 1 + j*p < 9))*N**4
    nu = sorted({round(e, 9) for k in (2, 3, 4) for j in range(1, 6) for e in [k + j*p] if e < 8.5 and abs(e - round(e)) > 1e-9})
    o3, o4 = [], []
    for lo, hi in ((10, 200), (15, 250), (20, 300), (25, 400)):
        for J in (len(nu)//2, len(nu)):
            E = [3, 4, 5, 6] + nu[:J]; sel = (n >= lo) & (n <= hi)
            A = np.vstack([N[sel]**(4 - e) for e in E]).T; co = np.linalg.lstsq(A, R[sel], rcond=None)[0]
            o3.append(co[0]); o4.append(co[1])
    f3, h3 = np.median(o3), (max(o3) - min(o3))/2; f4, h4 = np.median(o4), (max(o4) - min(o4))/2
    pred = float(f4_closed(mp.mpf(p), mp.mpf(a)))
    print(f"p={p} alpha={a:+.2f} (s={s}): N^-3 {f3:+.1e} ({h3:.0e});  f4 fit {f4:+.9f} ({h4:.0e})  closed form {pred:+.9f}  diff {f4 - pred:+.1e}", flush=True)
    C_.check(f"p={p} a={a}: N^-3 = 0", f3, 0.0, max(3*h3, 1e-7))
    C_.check(f"p={p} a={a}: f4 = closed form", f4, pred, max(3*h4, 2e-6))
C_.finish()
