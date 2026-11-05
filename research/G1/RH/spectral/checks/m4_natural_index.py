"""JZC M4 probe: the natural index. Conjecture S1-N: for the lattice sigma_{p,s} (and, by rule H, Hurwitz lattices),
  n^p b_n / c = (n/N)^p * F_{p,alpha}(N),   N := n + alpha/2 - Z(0),   alpha := (s-1)/p - 1,
where F has NO 1/N term, its N^{-2} coefficient is f2 = -(p+2) alpha^2/8 + (p+1)/12 (equivalent to E2's d2 closed form), the
zeta layer appears as eps_j N^{-1-jp} (E3), and -- the new claim -- the integer layer of F is EVEN in 1/N (no N^{-3} term),
as for the exact Bessel-zero (Lommel) family: F = (1 - 1/(4N^2))^{-1/2} at p = 2, alpha = -1/2.
Test: compute F(N) := (N/n)^p n^p b_n/c from the Plan 62 lattice coefficients, subtract 1 + sum_j eps_j N^{-1-jp} + f2 N^{-2},
and fit the remainder in powers of 1/N: the N^{-1}, N^{-2} (after subtraction) and N^{-3} coefficients must vanish."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import NMAX, Checks
C_ = Checks()
for p, s in ((1.5, 2.0), (1.5, 3.0), (1.25, 2.0), (2.5, 2.0), (3.0, 2.0), (1.5, 2.5), (2.0, 3.0)):
    K = 100*NMAX
    al, b = coeffs(p, s, K, NMAX); n, y, *_ = sequences(p, al, b)
    alpha = (s - 1)/p - 1; Z0 = -0.5; N = n + alpha/2 - Z0
    F = (N/n)**p*(1 + y)
    mp.mp.dps = 30; c = c_p_mp(p)
    eps = {j: float(mp.binomial(2*j, j)*p*c**j*mp.zeta(-j*p)) for j in range(1, 6)}
    f2 = -(p + 2)*alpha**2/8 + (p + 1)/12
    R = F - 1 - f2*N**-2.0 - sum(e*N**(-1 - j*p) for j, e in eps.items() if 1 + j*p < 5.5)
    # fit R on N >= lo with exponents {1, 2, 3} (must vanish) plus nuisance {4, 5, 1+jp+1 (shifted zeta), ...}
    tgt = [1.0, 2.0, 3.0]
    nuis = sorted({round(e, 9) for e in [4.0, 5.0] + [2 + j*p for j in range(1, 4)] + [3 + j*p for j in range(1, 3)] if e < 6.5} - set(tgt))
    out = {e: [] for e in tgt}
    for lo in (200, 400):
        for J in (2, 3, 4):
            E = tgt + nuis[:J]; sel = n >= lo; A = np.vstack([N[sel]**-e for e in E]).T
            co = np.linalg.lstsq(A, R[sel], rcond=None)[0]
            for e in tgt: out[e].append(co[E.index(e)])
    med = {e: (np.median(v), (max(v) - min(v))/2) for e, v in out.items()}
    print(f"p={p} s={s} alpha={alpha:+.4f} N = n + {alpha/2 - Z0:+.4f}: residual coefficients of N^-1 {med[1.0][0]:+.2e} ({med[1.0][1]:.0e}),"
          f" N^-2 {med[2.0][0]:+.2e} ({med[2.0][1]:.0e}), N^-3 {med[3.0][0]:+.2e} ({med[3.0][1]:.0e})   [f2 = {f2:+.6f}]")
    for e in tgt: C_.check(f"p={p} s={s}: N^-{e:g} residual = 0", med[e][0], 0.0, max(3*med[e][1], 1e-5))
C_.finish()
