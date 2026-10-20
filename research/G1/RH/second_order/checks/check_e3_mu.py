"""Plan E3 (E3.md Lemma E3.5, Theorem E3.3): first-order (1/n) Laurent data of Delta_1 for the band weight
    x^alpha (4c - x) exp(-mu1 x - mu2 x^2 - mu3 x^3),
to weighted order 3 (mu1 ~ n^{-p}, mu2 ~ n^{-2p}, mu3 ~ n^{-3p}: all monomials mu1, mu2, mu3, mu1^2, mu1 mu2, mu1^3), and the resulting 1/n coefficient of n^p b_n / c.

Generalised Lemma F.2 (E3 Lemma E3.4; Paper 2 (eq. szego-repr)): for q = exp(-sum_k mu_k x^k) on (0, 4c),
    log D_q^2 - log q = Rr(z) M(z),  M(z) = sum_k mu_k Q_k(z),  Q_k(z) = sum_{j<k} z^{k-1-j} binom(2j, j) c^j,
since (c(x) - c(z))/(z - x) = sum_k mu_k (x^k - z^k)/(x - z) and (1/pi) int_0^{4c} x^j dx / sqrt(x (4c - x)) = binom(2j, j) c^j.
So omega -> omega * exp(Rr M), rho^2 -> rho^2 * exp(-Rr M)  (E_plt1 Lemma F.2 is M = mu1).
Near 4c: Rr = z^{1/2} u (u = (z - 4c)^{1/2}); on z = -v^2: Rr = -v (4c + v^2)^{1/2} (E_plt1 Lemma E'.5 proof).
The band factor of E3 Lemma F.1'/E_plt1 Lemma F.1 is H_n ∝ exp(-2 sum_k m_k z^k), m_k = zeta(-kp)/(k n^{kp}), so
    mu1 = 2 m_1 = 2 zeta(-p) n^{-p},  mu2 = 2 m_2 = zeta(-2p) n^{-2p}.
Output: n^p b_n/c = 1 + [d1 + e(mu)]/n + ..., the Taylor coefficients of e(mu) to weighted order 3, and the n^{-1-kp}
coefficients eps_k (k = 1, 2, 3); asserted: e(mu) = c p M(4c) to this order (linear, no cross terms), hence
eps_k = binom(2k, k) p c^k zeta(-kp) for k <= 3, and at p = 1/j (j = 2, 3) eps_j = -p/12 exactly (c(1/j)^j = 1/binom(2j, j))."""
import sympy as sp
import mpmath as mp

I = sp.I
u, v = sp.symbols('u v', positive=True)
al, mu1, mu2, mu3, t = sp.symbols('alpha mu1 mu2 mu3 t')
p, c = sp.symbols('p c', positive=True)
T = sp.Matrix([[1, 1], [I, -I]]) / sp.sqrt(2)
Ti = T.inv()
sc = sp.sqrt(c)
O = 7


def tr(e, var, o=O):
    e = sp.expand(e)
    return sp.Add(*[e.coeff(var, k) * var ** k for k in range(0, o)])


def ser(e, var, o=O):
    return sp.expand(sp.series(e, var, 0, o).removeO())


def mtrunc(e):
    """keep 1, mu1, mu1^2, mu2 (drop mu1^3, mu1 mu2, mu2^2): substitute mu1 -> t mu1, mu2 -> t^2 mu2, keep t^<=2"""
    e = sp.expand(e.subs({mu1: t * mu1, mu2: t ** 2 * mu2, mu3: t ** 3 * mu3}))
    return sp.expand(sum(e.coeff(t, k) for k in range(4)))


def expM(x):            # exp(x) to second order, x = O(mu)
    return 1 + x + x ** 2 / 2 + x ** 3 / 6


# ---------- soft edge (Airy), first order Delta_1 ----------
x = u ** 2 / (4 * c)
sq1 = tr(ser(sp.sqrt(1 + x), u), u)
sqz = 2 * sc * sq1
z_s = 4 * c + u ** 2
a2 = tr(ser(u / (2 * sc * sp.sqrt(1 + x)), u), u)
h2 = tr(ser(sp.exp((2 + 2 * al) * sp.log(1 / (sp.sqrt(1 + x) + u / (2 * sc)))), u), u)
ih2 = tr(ser(sp.exp(-(2 + 2 * al) * sp.log(1 / (sp.sqrt(1 + x) + u / (2 * sc)))), u), u)
Rr_s = sp.expand(sqz * u)
M_s = mu1 + mu2 * (z_s + 2 * c) + mu3 * (z_s ** 2 + 2 * c * z_s + 6 * c ** 2)
Ep = tr(mtrunc(expM(Rr_s * M_s)), u)
Em = tr(mtrunc(expM(-Rr_s * M_s)), u)
h2m = tr(mtrunc(h2 * Ep), u)
ih2m = tr(mtrunc(ih2 * Em), u)
X1 = sp.Matrix([[-sp.Rational(1, 72), -I / 12], [-I / 12, sp.Rational(1, 72)]])
Z = sp.Matrix([[X1[0, 0], X1[0, 1] * ih2m], [X1[1, 0] * h2m, X1[1, 1]]])
Y = (Ti * Z * T).applyfunc(sp.expand)
Mu = (T * sp.Matrix([[tr(u * Y[0, 0], u), tr(u * a2 * Y[0, 1], u)], [tr(sqz * Y[1, 0], u), tr(u * Y[1, 1], u)]]) * Ti)
k2 = -(7 + 4 / p) / (40 * c)
kap = 1 / (6 * p * c ** sp.Rational(3, 2))
inv1 = 1 - k2 * u ** 2 + k2 ** 2 * u ** 4
D1u4 = Mu.applyfunc(lambda e: mtrunc(tr(e * inv1 / kap, u, 5)))
for k in (1, 3):
    assert all(sp.simplify(D1u4[i, j].coeff(u, k)) == 0 for i in range(2) for j in range(2)), "soft: odd powers"
Br = D1u4.applyfunc(lambda e: sp.expand(e.coeff(u, 0)))
Ar = D1u4.applyfunc(lambda e: sp.expand(e.coeff(u, 2)))
assert all(sp.simplify(Br[i, j] - Br.subs({mu1: 0, mu2: 0, mu3: 0})[i, j]) == 0 for i in range(2) for j in range(2)), "B_r mu-free"

# ---------- hard edge (Bessel), first order Delta_1, z = -v^2 ----------
ap = 1 / p + sp.Rational(1, 2)
C0 = 1 / (sp.sqrt(4 * c) * sp.pi * (1 + p / 2))
tau1 = ap / (8 * c * (ap + 1))
f1 = -sp.pi ** 2 * C0 ** 2
f2v = f1 * 2 * tau1 / 3
fh = v * sp.sqrt(sp.expand(sp.simplify((-f1 + f2v * v ** 2) * c * (p + 2) ** 2))) / (sc * (p + 2))
a2h = sp.sqrt(4 * c + v ** 2) / v
rho2 = (v / (2 * sc) + sp.sqrt(1 + v ** 2 / (4 * c))) ** (2 * al + 2)
Rr_h = -v * sp.sqrt(4 * c + v ** 2)
M_h = mu1 + mu2 * (-v ** 2 + 2 * c) + mu3 * (v ** 4 - 2 * c * v ** 2 + 6 * c ** 2)
rho2m = rho2 * expM(-Rr_h * M_h)
Q0 = sp.Matrix([[-(1 + 4 * al ** 2), 2 * I], [2 * I, 1 + 4 * al ** 2]])
Zh = sp.Matrix([[Q0[0, 0], rho2m * Q0[0, 1]], [Q0[1, 0] / rho2m, Q0[1, 1]]])
Yh = Ti * Zh * T
Dh = T * sp.Matrix([[Yh[0, 0], a2h * Yh[0, 1]], [Yh[1, 0] / a2h, Yh[1, 1]]]) * Ti / (16 * fh)
v2D = Dh.applyfunc(lambda e: mtrunc(ser(e * v ** 2, v, 3)))
assert all(sp.simplify(v2D[i, j].coeff(v, 1)) == 0 for i in range(2) for j in range(2)), "hard: odd powers"
A0 = v2D.applyfunc(lambda e: sp.simplify(-e.coeff(v, 0)))

# ---------- b-functional at order 1/n ----------
Atot = (A0 + Ar).applyfunc(sp.expand)
e1 = sp.expand(I * (Atot[1, 0] - Atot[0, 1]) / (2 * c))     # n^p b_n/c = 1 + e1/n + ...
s = sp.Symbol('s')
e1s = sp.expand(e1.subs(al, (s - 1 - p) / p))
d1 = sp.simplify(e1s.subs({mu1: 0, mu2: 0, mu3: 0}))
lin1 = sp.simplify(sp.diff(e1s, mu1).subs({mu1: 0, mu2: 0, mu3: 0}))
E11 = sp.factor(sp.simplify(sp.diff(e1s, mu1, 2).subs({mu1: 0, mu2: 0, mu3: 0}) / 2))
E2 = sp.factor(sp.simplify(sp.diff(e1s, mu2).subs({mu1: 0, mu2: 0, mu3: 0})))
Z0 = {mu1: 0, mu2: 0, mu3: 0}
E3 = sp.factor(sp.simplify(sp.diff(e1s, mu3).subs(Z0)))
E111 = sp.factor(sp.simplify(sp.diff(e1s, mu1, 3).subs(Z0) / 6))
E12 = sp.factor(sp.simplify(sp.diff(e1s, mu1, mu2).subs(Z0)))
print("mu3 coefficient E3 =", E3, "; mu1^3 coefficient =", E111, "; mu1 mu2 coefficient =", E12)
print("d1 =", d1, "; d/dmu1 =", lin1, "; mu1^2 coefficient E11 =", E11, "; mu2 coefficient E2 =", E2)
assert sp.simplify(d1 + (s - 1) / 2) == 0 and sp.simplify(lin1 - c * p) == 0
# A_0 (hard edge) mu-dependence, for the record
print("A_0 mu-dependence:", sp.simplify(A0 - A0.subs({mu1: 0, mu2: 0, mu3: 0})))


def cp(pv):
    pv = mp.mpf(pv)
    Ip = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / pv + 0.5) / mp.gamma(1 / pv + 1)
    return (mp.pi / (2 * Ip)) ** pv / 4


def e2val(pv, sv):
    cv = cp(pv)
    E11v = complex(sp.N(E11.subs({p: pv, c: cv, s: sv}), 30))
    E2v = complex(sp.N(E2.subs({p: pv, c: cv, s: sv}), 30))
    return 4 * mp.zeta(-pv) ** 2 * E11v.real + mp.zeta(-2 * mp.mpf(pv)) * E2v.real, E11v, E2v


print("n^{-1-2p} coefficient e_2(p, s) = 4 zeta(-p)^2 E11 + zeta(-2p) E2:")
for pv, sv in [(0.5, 2), (0.5, 3), (0.5, 1.5), (0.75, 2), (0.75, 3), (0.6, 2), (0.6, 3), (0.3, 2)]:
    val, a, b = e2val(pv, sv)
    print(f"  p = {pv}, s = {sv}: e_2 = {mp.nstr(val, 12)}")
assert E11 == 0 and E111 == 0 and E12 == 0, "no nonlinear terms to weighted order 3"
assert sp.simplify(E2 - 6 * c ** 2 * p) == 0 and sp.simplify(E3 - 30 * c ** 3 * p) == 0
# e(mu) = c p M(4c): M(4c) = mu1 + 6c mu2 + 30 c^2 mu3
assert sp.simplify(c * p * (mu1 + 6 * c * mu2 + 30 * c ** 2 * mu3) - (lin1 * mu1 + E2 * mu2 + E3 * mu3)) == 0
print("e(mu) = c p M(4c) to weighted order 3 (asserted)")
# eps_k with mu_k = 2 zeta(-kp)/(k n^{kp}): eps_1 = 2 c p zeta(-p), eps_2 = 6 c^2 p zeta(-2p), eps_3 = 20 c^3 p zeta(-3p)
from math import comb
for k, Ek in ((1, lin1), (2, E2), (3, E3)):
    assert sp.simplify(Ek * sp.Rational(2, k) - comb(2 * k, k) * p * c ** k) == 0
print("eps_k = binom(2k, k) p c^k zeta(-kp), k = 1, 2, 3 (asserted)")
for j in (2, 3):
    pv = sp.Rational(1, j)
    Ij = sp.sqrt(sp.pi) / 2 * sp.gamma(1 / pv + sp.Rational(1, 2)) / sp.gamma(1 / pv + 1)
    cj = (sp.pi / (2 * Ij)) ** pv / 4
    assert sp.simplify(cj ** j - sp.Rational(1, comb(2 * j, j))) == 0
    epsj = comb(2 * j, j) * pv * cj ** j * sp.zeta(-1)
    assert sp.simplify(epsj + pv / 12) == 0
    print(f"p = 1/{j}: c^{j} = 1/{comb(2 * j, j)}, eps_{j} = {sp.nsimplify(epsj)} = -p/12 (asserted)")
print("ALL ASSERTIONS PASSED")
