"""SPEC probes 1 and 3 at p = 1.5, s = 2 (Hurwitz lattices lam = (k + d)^p, d in {-1/2, 0, 1/2, 1}).
Subtract the known terms d1(d) = d1_0 - p d, d2(d) = index-shift rule, eps1(a) n^{-1-p} (a = 1 + d, Hurwitz), then fit the
n^-3 (d3) and n^-3.5 (f) coefficients. Compare:
  probe 3 (integer layer, third order): d3(d) vs the index-shift prediction built from d1_0, d2_0 (E2) and the fitted d3(0);
  probe 1 (zeta layer under the shift): f(d) vs
     H (whole expansion index-shifted, zeta values -> Hurwitz):  f(d) = eps1(a) [f(0)/eps1(1) - (1 + 2p) d]
     A (zeta layer not shifted):                                 f(d) = eps1(a) f(0)/eps1(1)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp, sympy as sp
from so_coeffs import coeffs, c_p_mp, CACHE as C62
from so_fit import sequences
p, s = 1.5, 2.0; NMAX = 1600; K = 100*NMAX
d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
d10, d20 = -(s - 1)/2, d2f(p, s); c = c_p_mp(p)
e1 = lambda a: float(2*p*c*mp.zeta(-mp.mpf(p), a))
# index-shift expansion: (1 + d/n)^{-p} (1 + d1/(n+d) + d2/(n+d)^2 + d3/(n+d)^3), coefficient of n^-3 as a function of d3_0
N, dd, D3 = sp.symbols('N d D3'); e = sp.Symbol('e')
expr = (1 + dd*e)**(-sp.Rational(3, 2))*(1 + d10*e/(1 + dd*e) + sp.Rational(d20).limit_denominator(10**9)*e**2/(1 + dd*e)**2 + D3*e**3/(1 + dd*e)**3)
ser = sp.expand(sp.series(expr, e, 0, 4).removeO())
c2, c3 = sp.lambdify((dd,), ser.coeff(e, 2)), sp.lambdify((dd, D3), ser.coeff(e, 3))
from spec_common import Checks
C_ = Checks()
res = {}
for d in (0.0, -0.5, 0.5, 1.0):
    f = C62 / (f"p{p}_s{s}_K{K}_n{NMAX}" + ("" if d == 0 else f"_d{d}") + ".txt")
    if not f.exists(): print(f"(no cache for d = {d})"); continue
    al, b = coeffs(p, s, K, NMAX, d); n, y, *_ = sequences(p, al, b); n = n.astype(float)
    a = 1 + d
    r = y - (d10 - p*d)/n - c2(d)/n**2 - e1(a)*n**(-1 - p)
    est3, est35 = [], []
    for J in (4, 5, 6):
        E = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0][:J]
        for lo in (100, 200, 400):
            m = n >= lo; n0 = n[m].min()
            A = np.vstack([(n0/n[m])**ee for ee in E]).T
            co = np.linalg.lstsq(A, r[m], rcond=None)[0]*np.array([n0**ee for ee in E])
            est3.append(co[0]); est35.append(co[1])
    est3, est35 = np.array(est3), np.array(est35)
    res[d] = (np.median(est3), (est3.max() - est3.min())/2, np.median(est35), (est35.max() - est35.min())/2, e1(a))
    print(f"d={d:+.1f}: d2 used {c2(d):+.6f} | d3 fit {res[d][0]:+.5f} ({res[d][1]:.1e}) | n^-3.5 fit {res[d][2]:+.5f} ({res[d][3]:.1e}) | eps1(a) {e1(a):+.5f}")
d30, _, f0, _, e10 = res[0.0]
print("\nprobe 3 (integer layer, third order): d3(d) vs index-shift prediction from d3(0)")
for d, (v3, h3, v35, h35, ea) in res.items():
    if d == 0: continue
    pr = c3(d, d30); print(f"  d={d:+.1f}: fit {v3:+.5f} ({h3:.1e})  index-shift {pr:+.5f}  diff {v3 - pr:+.1e}")
    C_.check(f"d3 d={d}", v3, pr, max(3*h3, 1e-3))
print("probe 1 (zeta layer under the shift): n^-3.5 coefficient")
for d, (v3, h3, v35, h35, ea) in res.items():
    if d == 0: continue
    H = ea*(f0/e10 - (1 + 2*p)*d); A_ = ea*f0/e10
    print(f"  d={d:+.1f}: fit {v35:+.5f} ({h35:.1e})  H {H:+.5f} (diff {v35 - H:+.1e})  A {A_:+.5f} (diff {v35 - A_:+.1e})")
    C_.check(f"n^-3.5 H d={d}", v35, H, max(3*h35, 1e-3))
    if abs(d) >= 0.5 and d > 0: C_.n += 1; (abs(v35 - A_) > 3*h35) or C_.fails.append(f"alternative A not excluded at d={d}")
C_.finish()
