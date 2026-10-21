"""SPEC: a real operator with a continuous parameter. Robin bouncer H = -d^2/dx^2 + x on (0, inf), psi'(0) = h psi(0).
Eigenvalues E_k: zeros of F(-E), F(z) := Ai'(z) - h Ai(z); E^N_k < E_k < E^D_k (Neumann/Dirichlet), found by vectorised bisection.
Zeta values (exact, as Prop. B): sum_k [1/(z + E_k) - 1/E_k] = F'/F + const = (z Ai - h Ai')/(Ai' - h Ai); with Ai'/Ai = -sqrt(z) R,
R = [sum (-1)^k v_k zeta^-k]/[sum (-1)^k u_k zeta^-k], zeta = (2/3) z^{3/2}:  F'/F = (z + h sqrt(z) R)/(-sqrt(z) R - h);
Z_E(-j) = (-1)^j [z^{-j-1}] F'/F.  Normalised lam' = E/(3pi/2)^{2/3}, p = 2/3.
S1 predictions: d1 = -p alpha/2 + p Z(0); eps1 = 2pc Z_lam'(-1) (h-dependent); pole law: the Robin index corrections ~ h k^{-1/3}
(q = 1/2), h^3 k^{-1} (q = 3/2), Neumann WKB k^{-1} (q = 3/2) all have cot = 0, so d2 = index-shift value with delta = -Z(0) - 1/2."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, sympy as sp
from scipy.special import airy
from spec_common import run, fit, NMAX, c_p_mp, Checks
from spec_airy import zeros as zeros_D
h = float(sys.argv[1]); s = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
p = 2/3; K = 200*NMAX
# --- exact zeta values ---
z, u, hh = sp.symbols('z u h', positive=True); KK = 9
def uk(k): return sp.Rational(sp.prod([2*i + 1 for i in range(k, 3*k)]), 216**k*sp.factorial(k)) if k else sp.Integer(1)
def vk(k): return -sp.Rational(6*k + 1, 6*k - 1)*uk(k) if k else sp.Integer(1)
x = sp.Rational(3, 2)*u**3                                   # 1/zeta with u = z^{-1/2}
R = sp.series(sum((-1)**k*vk(k)*x**k for k in range(KK))/sum((-1)**k*uk(k)*x**k for k in range(KK)), u, 0, 16).removeO()
# F'/F in u: z = u^-2, sqrt z = 1/u
expr = (u**-2 + hh*R/u)/(-R/u - hh)
ser = sp.expand(sp.series(expr, u, 0, 9).removeO())
Z = {j: sp.simplify((-1)**j*ser.coeff(u, 2*j + 2)) for j in range(0, 4)}   # z^{-j-1} = u^{2j+2}
print("Robin Z_E(-j) as functions of h:", {j: str(sp.factor(v)) for j, v in Z.items()})
assert sp.simplify(Z[0] - sp.Rational(1, 4)) == 0
# --- eigenvalues ---
UC = [1.0, -7/48, 35/288, -181223/207360, 18683371/12192768]
k = np.arange(1, K + 1, dtype=np.float64)
mp.mp.dps = 30
EN = np.empty(K); 
for kk in range(1, 41): EN[kk - 1] = float(-mp.airyaizero(kk, 1))
t = 3*np.pi/8*(4*k[40:] - 3); EN[40:] = t**(2/3)*sum(c*t**(-2*i) for i, c in enumerate(UC))
ED = zeros_D(K)
Fv = lambda E: (lambda a: a[1] - h*a[0])(airy(-E))
lo, hi = EN.copy(), ED.copy(); flo = Fv(lo)
for _ in range(80):
    mid = (lo + hi)/2; fm = Fv(mid); same = np.sign(fm) == np.sign(flo)
    lo = np.where(same, mid, lo); flo = np.where(same, fm, flo); hi = np.where(same, hi, mid)
E = (lo + hi)/2
resid = float(np.max(np.abs(Fv(E[:1000]))))
print(f"bisection bracket width max {np.max(hi - lo):.1e}; E_1 = {E[0]:.12f}, residual max |F| {resid:.1e}")
assert resid < 1e-9 and np.all(E > EN) and np.all(E < ED), "Robin roots bracketed strictly between Neumann and Dirichlet"

C = (3*np.pi/2)**(2/3); lam = E/C
n, y = run(f"robin_h{h}_s{s}", lam, p, s, -0.75, K)
c = float(c_p_mp(p)); alpha = (s - 1 - p)/p
Z0 = float(Z[0].subs(hh, h)); Z1 = float(Z[1].subs(hh, h))/C; Z2 = float(Z[2].subs(hh, h))/C**2
d1 = -p*alpha/2 + p*Z0; e1 = 2*p*c*Z1; e2 = 6*p*c*c*Z2
delta = -Z0 - 0.5; d10 = -(s - 1)/2
d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
d2 = d2f(p, s) + p*(p + 1)*delta**2/2 - (p + 1)*delta*d10
v1, h1 = fit(n, y, p, [], 1.0)
v, hv = fit(n, y - d1/n, p, [1.0], 1 + p)
w, hw = fit(n, y - d1/n - e1*n**(-1 - p), p, [1.0, round(1 + p, 9)], 2.0)
print(f"h={h} s={s}: Z(0) = {Z0:.6f}, Z_lam'(-1) = {Z1:+.6f}, Z_lam'(-2) = {Z2:+.6f}")
print(f"  d1: fit {v1:+.8f} ({h1:.1e})  pred {d1:+.8f}")
print(f"  eps1 (n^-5/3): fit {v:+.7f} ({hv:.1e})  pred {e1:+.7f}  diff {v - e1:+.1e}   [Neumann h=0: 0]")
print(f"  n^-2: fit {w:+.6f} ({hw:.1e})  pred (index shift, delta = {delta:+.3f}) {d2:+.6f}  diff {w - d2:+.1e}")
C_ = Checks(); C_.check(f"d1 h={h}", v1, d1, max(3*h1, 1e-5)); C_.check(f"eps1 h={h}", v, e1, max(3*hv, 1e-4)); C_.check(f"d2 h={h}", w, d2, max(3*hw, 1e-4)); C_.finish()
