"""SPEC §3.3: closed forms for the quantum bouncer (H = -d^2/dx^2 + x on (0, inf), Dirichlet; E_k = -a_k).
Resolvent trace: sum_k [1/(z + E_k) - 1/E_k] = Ai'(z)/Ai(z) - Ai'(0)/Ai(0) (Hadamard product of Ai, order 3/2).
Large-z expansion from DLMF 9.7.5-9.7.6 with u_k, v_k of 9.7.2 (quoted in RH/CITATIONS.md):
  Ai'/Ai = -z^{1/2} [sum (-1)^k v_k zeta^-k]/[sum (-1)^k u_k zeta^-k],  zeta = (2/3) z^{3/2}.
Mellin correspondence: a term c_a t^a of the heat trace <-> c_a Gamma(a+1) z^{-a-1}; Z_E(-j) = (-1)^j j! c_j, i.e.
  Z_E(-j) = (-1)^j [z^{-j-1}] (Ai'/Ai).
Integer powers z^{(1-3k)/2} occur only for odd k, so Z_E(-j) = 0 unless 3 | j.
Part 2 (NUMERICAL, independent): Z_E(-3), Z_E(-6) from the Hurwitz-regularised zero sums (spec_zeta_airy.py)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
z, x = sp.symbols('z x', positive=True)
K = 9
def u(k): return sp.Rational(sp.prod([2*i + 1 for i in range(k, 3*k)]), 216**k*sp.factorial(k)) if k else sp.Integer(1)
def v(k): return -sp.Rational(6*k + 1, 6*k - 1)*u(k) if k else sp.Integer(1)
assert u(1) == sp.Rational(5, 72) and v(1) == sp.Rational(-7, 72)
ratio = sp.series(sum((-1)**k*v(k)*x**k for k in range(K))/sum((-1)**k*u(k)*x**k for k in range(K)), x, 0, K).removeO()
Z = {}; heat = {}
for k in range(K):
    coef = -ratio.coeff(x, k)*sp.Rational(3, 2)**k          # coefficient of z^{1/2 - 3k/2}
    expo = sp.Rational(1, 2) - sp.Rational(3*k, 2)
    if expo < 0 and expo.is_integer:
        j = int(-expo - 1); Z[j] = (-1)**j*coef
    elif expo < 0:
        a = -expo - 1; heat[a] = sp.nsimplify(coef/sp.gamma(a + 1))
print("Z_E(-j) (others vanish):", {j: str(val) for j, val in Z.items()})
print("total heat coefficients of half-integer powers t^a:", {str(a): str(c) for a, c in heat.items()})
W = {sp.Rational(3, 2): 1/(24*sp.sqrt(sp.pi)), sp.Rational(9, 2): 1/(2*144*2*sp.sqrt(sp.pi))}   # (4pi)^{-1/2} t^{-3/2} e^{t^3/12}
beta1 = sp.simplify(heat[sp.Rational(3, 2)] - W[sp.Rational(3, 2)]); beta3 = sp.simplify(heat[sp.Rational(9, 2)] - W[sp.Rational(9, 2)])
print("boundary beta1 =", beta1, " beta3 =", beta3, " beta2 = -Z_E(-3)/6 =", -Z[3]/6)
assert Z[0] == sp.Rational(-1, 4) and Z[3] == sp.Rational(15, 64) and Z[6] == sp.Rational(-1695, 1024)
assert sp.simplify(beta1 - 1/(6*sp.sqrt(sp.pi))) == 0 and sp.simplify(beta3 - sp.Rational(25, 1512)/sp.sqrt(sp.pi)) == 0
# Part 2: independent numerics
mp.mp.dps = 40
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec_zeta_airy.py')).read()
src = src.replace('__file__', repr(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec_zeta_airy.py'))).split('for j in')[0]
exec(src)
for j in (0, 3, 6):
    num = (3*mp.pi/2)**(2*j/mp.mpf(3))*Zneg(j, 200)
    ref = mp.mpf(sp.Rational(Z[j]).p)/sp.Rational(Z[j]).q
    print(f"Z_E(-{j}): Hurwitz-regularised zero sum {mp.nstr(num, 15)}  closed form {mp.nstr(ref, 15)}  diff {mp.nstr(num - ref, 2)}")
    assert abs(num - ref) < 1e-8
print("fit values (spec_bouncer_heat.out): beta1 0.094031587 vs", mp.nstr(1/(6*mp.sqrt(mp.pi)), 10), "; beta3 ~0.00933 vs", mp.nstr(mp.mpf(25)/1512/mp.sqrt(mp.pi), 6))
print("ALL ASSERTIONS PASSED")
