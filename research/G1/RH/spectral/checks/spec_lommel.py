"""SPEC probe: Bessel-zero measures (p = 2, s = 2) are an EXACT index shift of the p = 2 lattice.
Lommel polynomials: monic recurrence x h_n = h_{n+1} + beta_n^2 h_{n-1}, beta_n^2 = 1/(4(n+nu-1)(n+nu)), orthogonal w.r.t. a
symmetric measure on {+-1/j_{nu-1,k}} with masses proportional to j_{nu-1,k}^{-2} (Dickinson 1954; Van Assche 1996 §3; repo VA).
Even/odd splitting (y = x^2): b_n^(y) = beta_{2n-1} beta_{2n}. With mu = nu - 1, lam_k = (j_{mu,k}/pi)^2, c(2) = pi^2/16:
  n^2 b_n/c = 4 n^2/((2n+mu) sqrt((2n+mu)^2 - 1)) = (1 + mu/(2n))^{-2} (1 - (2n+mu)^{-2})^{-1/2}
            = [n/(n+delta)]^2 G(n + delta),  delta = mu/2 - 1/4,  G(N) = (1 - 1/(16 N^2))^{-1/2}... (lattice: mu = 1/2).
(1) Check of the closed form against Jacobi coefficients computed from the Bessel zeros (mpmath zeros for k <= 120, McMahon
    beyond, K = 40000 atoms + continuum tail), n <= 40.  (2) Expansion: d1 = -mu, d2 = 3mu^2/4 + 1/8, and the S1 j = 0 check
    d1 = -p alpha/2 + p zeta(0, mu/2 + 3/4)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, sympy as sp
from scipy.special import roots_jacobi
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
def zeros(mu, K, kex=120):
    mp.mp.dps = 30; out = np.empty(K)
    for k in range(1, kex + 1): out[k - 1] = float(mp.besseljzero(mu, k))
    k = np.arange(kex + 1, K + 1, dtype=np.float64); be = (k + mu/2 - 0.25)*np.pi; m4 = 4*mu*mu
    out[kex:] = (be - (m4 - 1)/(8*be) - 4*(m4 - 1)*(7*m4 - 31)/(3*(8*be)**3)
                 - 32*(m4 - 1)*(83*m4**2 - 982*m4 + 3779)/(15*(8*be)**5))
    return out
mp.mp.dps = 30
for mu in (0.0, 1.5):
    kk = 130
    err = abs(float(mp.besseljzero(mu, kk)) - zeros(mu, kk, kex=1)[kk - 1])/float(mp.besseljzero(mu, kk))
    print(f"mu={mu}: McMahon (4 terms) vs mpmath at k={kk}: rel {err:.1e}")
    K, NM = 40000, 40
    lam = (zeros(mu, K)/np.pi)**2; x, w = 1/lam, 1/lam          # weights lam^{-s/p} = lam^{-1}
    # continuum tail beyond K: lam ~ (k + mu/2 - 1/4)^2, nodes x = t^-2, weights t^-2 dt: Gauss-Jacobi as in so_coeffs (p=2, s=2, delta)
    p, s, dl = 2.0, 2.0, mu/2 - 0.25 - 1 + 1     # lam = (k + mu/2 - 1/4)^2 = (k + dl)^2 with dl = mu/2 - 1/4
    beta = (s - 1)/p - 1; u, wu = roots_jacobi(NM + 8, 0.0, beta); X = (K + 0.5 + dl)**(-p)
    mu_meas = DiscreteMeasure.from_atoms(x, w, tail=(X*(1 + u)/2, wu*(X/2)**(beta + 1)/p))
    jc = jacobi_rkpw(mu_meas, NM + 1, prec="q")
    c = mp.pi**2/16; worst = 0
    for n in (1, 2, 5, 10, 20, 40):
        num = mp.mpf(n)**2*mp.sqrt(jc.b2[n - 1])/c
        m = 2*n + mu
        exact = 4*mp.mpf(n)**2/(m*mp.sqrt(m*m - 1))
        worst = max(worst, abs(num - exact)/exact)
        print(f"   n={n:3d}: from zeros {mp.nstr(num, 14)}   closed form {mp.nstr(exact, 14)}")
    print(f"   worst relative difference {mp.nstr(worst, 2)}"); assert worst < 1e-7
n, mu = sp.symbols('n mu', positive=True)
expr = 4*n**2/((2*n + mu)*sp.sqrt((2*n + mu)**2 - 1))
ser = sp.series(expr.subs(n, 1/sp.Symbol('e')), sp.Symbol('e'), 0, 4).removeO()
e = sp.Symbol('e'); co = [sp.simplify(ser.coeff(e, k)) for k in range(4)]
print("expansion n^2 b_n/c = 1 + d1/n + d2/n^2 + d3/n^3:", [sp.factor(cc) for cc in co])
assert sp.simplify(co[1] + mu) == 0 and sp.simplify(co[2] - (3*mu**2/4 + sp.Rational(1, 8))) == 0
p_, alpha = 2, -sp.Rational(1, 2)                              # s = 2, p = 2: alpha = (s-1-p)/p = -1/2
Z0 = sp.Rational(1, 2) - (mu/2 + sp.Rational(3, 4))             # zeta(0, a) = 1/2 - a
assert sp.simplify(-p_*alpha/2 + p_*Z0 - co[1]) == 0
print("S1 j = 0: d1 = -p alpha/2 + p zeta(0, mu/2 + 3/4) = -mu (asserted, all mu)")
d10, d20 = -sp.Rational(1, 2), sp.Rational(5, 16); dl = mu/2 - sp.Rational(1, 4)
assert sp.simplify(d20 + 3*dl**2 - 3*dl*d10 - co[2]) == 0
print("d2 = index-shift rule d2_0 + p(p+1) delta^2/2 - (p+1) delta d1_0 with delta = mu/2 - 1/4 (asserted, all mu)")
print("ALL ASSERTIONS PASSED")
