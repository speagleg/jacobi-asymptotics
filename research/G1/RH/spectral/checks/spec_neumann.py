"""SPEC direction 3 (Maslov index): Neumann bouncer H = -d^2/dx^2 + x on (0, inf), psi'(0) = 0; E_k = -a'_k (zeros of Ai').
(1) Zeros: DLMF-type asymptotics a'_k = -U(3pi/8 (4k-3)), U(t) ~ t^{2/3}(1 - 7/48 t^-2 + 35/288 t^-4 - 181223/207360 t^-6
    + 18683371/12192768 t^-8), checked against mpmath.airyaizero(k, 1).
(2) Zeta values (exact): sum_k [1/(z + E_k) - 1/E_k] = Ai''/Ai' + const = z Ai/Ai' = -z^{1/2} [sum (-1)^k u_k zeta^-k]/[sum (-1)^k v_k zeta^-k];
    Z_E(-j) = (-1)^j [z^{-j-1}].  Prediction: Z_E(0) = +1/4 (Hurwitz a = 1/4, Maslov mu = 1), Z_E(-1) = Z_E(-2) = 0.
(3) Jacobi coefficients of sum lam'^{-s/p} delta_{1/lam'}, lam' = E/(3pi/2)^{2/3} = (k - 3/4)^{2/3}(1 + O(k^-2)), p = 2/3:
    S1 predicts d1 = -p alpha/2 + p Z(0) = -(s-1)/2 + p/2 + p/4 and eps1 = 0 (Dirichlet: -(s-1)/2 + p/2 - p/4; shift p/2)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, sympy as sp
from spec_common import Checks, run, fit, c_p_mp, NMAX
UC = [1.0, -7/48, 35/288, -181223/207360, 18683371/12192768]
def zeros_ap(K, kex=40):
    mp.mp.dps = 30; out = np.empty(K)
    for k in range(1, kex + 1): out[k - 1] = float(-mp.airyaizero(k, 1))
    k = np.arange(kex + 1, K + 1, dtype=np.float64); t = 3*np.pi/8*(4*k - 3)
    out[kex:] = t**(2/3)*sum(c*t**(-2*i) for i, c in enumerate(UC))
    return out
mp.mp.dps = 30
worst = max(abs(float(-mp.airyaizero(k, 1)) - (lambda t: t**(2/3)*sum(c*t**(-2*i) for i, c in enumerate(UC)))(3*np.pi/8*(4*k - 3)))
            / float(-mp.airyaizero(k, 1)) for k in (41, 60, 100, 200))
print(f"(1) series vs mpmath for k in 41..200: worst relative error {worst:.1e}"); assert worst < 1e-15
z, x = sp.symbols('z x', positive=True); KK = 8
def u(k): return sp.Rational(sp.prod([2*i + 1 for i in range(k, 3*k)]), 216**k*sp.factorial(k)) if k else sp.Integer(1)
def v(k): return -sp.Rational(6*k + 1, 6*k - 1)*u(k) if k else sp.Integer(1)
ratio = sp.series(sum((-1)**k*u(k)*x**k for k in range(KK))/sum((-1)**k*v(k)*x**k for k in range(KK)), x, 0, KK).removeO()
Z = {}
for k in range(KK):
    expo = sp.Rational(1, 2) - sp.Rational(3*k, 2)
    if expo < 0 and expo.is_integer:
        j = int(-expo - 1); Z[j] = (-1)**j*(-ratio.coeff(x, k)*sp.Rational(3, 2)**k)
print("(2) Neumann Z_E(-j) (others vanish):", {j: str(vv) for j, vv in Z.items()}); assert Z[0] == sp.Rational(1, 4)
s = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
p = 2/3; K = 200*NMAX
lam = zeros_ap(K)/float((3*mp.pi/2)**(mp.mpf(2)/3))
n, y = run(f"neumann_s{s}", lam, p, s, -0.75, K)
alpha = (s - 1 - p)/p
d1 = -p*alpha/2 + p*0.25
v1, h1 = fit(n, y, p, [], 1.0)
v, h = fit(n, y - d1/n, p, [1.0], 1 + p)
print(f"(3) s={s}: d1 fit {v1:+.8f} ({h1:.1e}) pred {d1:+.8f} [Dirichlet bouncer {-p*alpha/2 - p*0.25:+.8f}] | n^-5/3 fit {v:+.7f} ({h:.1e}) pred 0")
# pass/fail (REVIEW_SPEC2_B F4): |fit - prediction| <= max(3 * fit half-range, floor)
C_ = Checks(); C_.check(f"d1 s={s}", v1, d1, max(3*h1, 1e-5)); C_.check(f"eps1 s={s}", v, 0.0, max(3*h, 1e-4)); C_.finish()
