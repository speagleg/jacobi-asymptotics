"""Plan E2 (E2_pgt1.md; d2 for p > 1): exact symbolic second-order computation, extending check_e_sym.py (Plan 65) by one order.

Frame and notation as in E_pgt1.md (Q-frame of Paper 2; P0 = T a^{s3} T^{-1}, a = ((z-4c)/z)^{1/4}).
Jumps on the circles: J = I + Delta1/n + Delta2/n^2 + O(n^-3 + n^{-1-p}) with
  soft edge 4c: Delta_k^r = (-1/phit)^k P0 (-w)^{-s3/2} X_k (-w)^{s3/2} P0^{-1}            (xi = -n phit)
      X_1 = [[(u1+v1)/2, i(v1-u1)/2], [i(v1-u1)/2, -(u1+v1)/2]],  X_2 = [[(u2+v2)/2, i(u2-v2)/2], [-i(u2-v2)/2, (u2+v2)/2]]
  hard edge 0:  Delta_k^0 = (2 f^{1/2})^{-k} P0 rho^{s3} s3 Xi_k s3 rho^{-s3} P0^{-1}         (w = 2 n f^{1/2})
      Xi_1 = (1/2)[[-(a1+b1), i(a1-b1)], [i(a1-b1), a1+b1]],  Xi_2 = (1/2)[[a2+b2, i(a2-b2)], [-i(a2-b2), a2+b2]]
(DLMF 10.40.1-4 / 10.17.1, 10.17.8 and 9.7.2, 9.7.5-6; second coefficients verified numerically in check_e2_num.py).
Second-order small norm: R2_out = principal parts of (R1_in Delta1 + Delta2) at 0 and 4c, R1_in = R1_out - Delta1,
so the first moment R_1^(2) = sum of residues of (R1_in Delta1 + Delta2).
Model data (exact series, symbolic p): phit from the soft-edge expansion of the equilibrium density, f from the hard-edge one.
Output: d2 with n^p b_n / c = 1 + d1/n + d2/n^2 + ..., compared with the closed form of Theorem E2.1.
Provenance (Rule X): that closed form was first guessed from the Plan 62 grid fits (check_e2_grid) and then derived here;
the grid is therefore a consistency check of the formula, not independent evidence for it. The independent evidence is
this derivation and the quadrature route of Rule R review B (REVIEW_PlanE2_B.md).
c-independence of d2 is automatic (all model inputs depend on z/c only) and is NOT a test of the computation (review B F2).
Truncation: sufficiency was shown by review B (K = 4 terms of S and of the f-series suffice, K = 3 fails; d2 depends on
kappa2, kappa3 only, not on kappa4, f''(0), f'''(0)); this script keeps K = 6."""
import sympy as sp

I = sp.I
u, v, z = sp.symbols('u v z')
al, p, c = sp.symbols('alpha p c', positive=True)
T = sp.Matrix([[1, 1], [I, -I]]) / sp.sqrt(2)
Ti = T.inv()
sc = sp.sqrt(c)
O = 11                                   # keep powers u^0 .. u^{O-1}


def tr(e, var, o=O):
    e = sp.expand(e)
    return sp.Add(*[e.coeff(var, k) * var ** k for k in range(0, o)])


def ser(e, var, o=O):
    return sp.expand(sp.series(e, var, 0, o).removeO())


# ---------- model data: phit near 4c (u^2 = z - 4c) ----------
ap = 1 / p + sp.Rational(1, 2)
e_ = sp.Symbol('e')
K = 6
S = 0
for k in range(K):
    for m in range(K - k):
        S += sp.rf(1 - ap, k) / sp.factorial(k) * sp.rf(1 + 1 / p, m) / sp.factorial(m) * e_ ** (k + m) \
             / ((k + sp.Rational(1, 2)) * (k + m + sp.Rational(3, 2)))
# phit = -(1/p)(4c)^{-3/2} u^3 S(-u^2/(4c))
Su = sp.expand(S.subs(e_, -u ** 2 / (4 * c)))
phit_over = sp.expand(Su / S.subs(e_, 0))          # 1 + kappa2 u^2 + kappa3 u^4 + ...
kap = (S.subs(e_, 0) / p) / (4 * c) ** sp.Rational(3, 2)
assert sp.simplify(kap - 1 / (6 * p * c ** sp.Rational(3, 2))) == 0
assert sp.simplify(phit_over.coeff(u, 2) + (7 + 4 / p) / (40 * c)) == 0, "kappa2 must match Lemma E.4(ii)"
inv1 = tr(ser(1 / phit_over, u), u)               # 1/(1+kappa2 u^2+...)
inv2 = tr(ser(1 / phit_over ** 2, u), u)

# ---------- soft edge ----------
x = u ** 2 / (4 * c)
sq1 = tr(ser(sp.sqrt(1 + x), u), u)
sqz = 2 * sc * sq1
a2 = tr(ser(u / (2 * sc * sp.sqrt(1 + x)), u), u)       # a^2 = u / z^{1/2}
L = tr(ser(-sp.log(sp.sqrt(1 + x) + u / (2 * sc)), u), u)   # log(2 sqrt c/(z^{1/2}+u))
h2 = tr(ser(sp.exp((2 + 2 * al) * sp.log(1 / (sp.sqrt(1 + x) + u / (2 * sc)))), u), u)
ih2 = tr(ser(sp.exp(-(2 + 2 * al) * sp.log(1 / (sp.sqrt(1 + x) + u / (2 * sc)))), u), u)
u1, v1 = sp.Rational(5, 72), -sp.Rational(7, 72)
u2, v2 = sp.Rational(385, 10368), -sp.Rational(455, 10368)
X1 = sp.Matrix([[(u1 + v1) / 2, I * (v1 - u1) / 2], [I * (v1 - u1) / 2, -(u1 + v1) / 2]])
X2 = sp.Matrix([[(u2 + v2) / 2, I * (u2 - v2) / 2], [-I * (u2 - v2) / 2, (u2 + v2) / 2]])
assert sp.simplify((X1 - sp.Matrix([[-sp.Rational(1, 72), -I / 12], [-I / 12, sp.Rational(1, 72)]])).norm()) == 0
# det(I + X1/xi + X2/xi^2) = 1 + O(xi^-3)  <=>  tr X2 = -det X1
assert sp.simplify(X2.trace() + X1.det()) == 0


def conj_soft(X):
    """u * P0 (-w)^{-s3/2} X (-w)^{s3/2} P0^{-1}, as a u-series (entries)"""
    Z = sp.Matrix([[X[0, 0], X[0, 1] * ih2], [X[1, 0] * h2, X[1, 1]]])
    Y = (Ti * Z * T).applyfunc(sp.expand)
    M = T * sp.Matrix([[tr(u * Y[0, 0], u), tr(u * a2 * Y[0, 1], u)], [tr(sqz * Y[1, 0], u), tr(u * Y[1, 1], u)]]) * Ti
    return M.applyfunc(lambda e: tr(e, u))


kp = 1 / (6 * p * c ** sp.Rational(3, 2))
# Delta1^r = -(1/phit) (M1/u) = M1 inv1/(kappa u^4);   Delta2^r = (1/phit^2)(M2/u) = M2 inv2/(kappa^2 u^7)
D1r_u4 = conj_soft(X1).applyfunc(lambda e: tr(e * inv1 / kp, u))           # = u^4 Delta1^r
D2r_u7 = conj_soft(X2).applyfunc(lambda e: tr(e * inv2 / kp ** 2, u))      # = u^7 Delta2^r
for k in (1, 3, 5):
    assert all(sp.simplify(D1r_u4[i, j].coeff(u, k)) == 0 for i in range(2) for j in range(2)), "Delta1^r odd"
for k in (0, 2, 4, 6):
    assert all(sp.simplify(D2r_u7[i, j].coeff(u, k)) == 0 for i in range(2) for j in range(2)), "Delta2^r odd"
Br = D1r_u4.applyfunc(lambda e: sp.simplify(e.coeff(u, 0)))
Ar = D1r_u4.applyfunc(lambda e: sp.simplify(e.coeff(u, 2)))
reg0 = D1r_u4.applyfunc(lambda e: sp.simplify(e.coeff(u, 4)))    # constant term of Delta1^r at 4c
reg1 = D1r_u4.applyfunc(lambda e: sp.simplify(e.coeff(u, 6)))    # (z-4c)^1 term
assert sp.simplify((Br - (5 * c ** 2 * p / 12) * sp.Matrix([[1, -I], [-I, -1]])).norm()) == 0
Ar_ref = (c / 48) * sp.Matrix([[12 * al ** 2 * p + 24 * al * p + 11 * p + 2, -I * (12 * al ** 2 * p + 48 * al * p + 49 * p + 2)],
                               [-I * (12 * al ** 2 * p + p + 2), -(12 * al ** 2 * p + 24 * al * p + 11 * p + 2)]])
assert all(sp.simplify(sp.expand(Ar[i, j] - Ar_ref[i, j])) == 0 for i in range(2) for j in range(2)), "A_r (Lemma E.5)"
# Laurent of Delta2^r in z-4c: coefficient of (z-4c)^{-1} is the u^{-2} coefficient = u^5 coeff of u^7 Delta2
res_D2r = D2r_u7.applyfunc(lambda e: sp.simplify(e.coeff(u, 5)))
print("soft edge done: B_r, A_r reproduce Lemma E.5; Delta2^r meromorphic (odd powers of u in u^7 Delta2 only)")

# ---------- hard edge (z = -v^2, negative axis outside the lens) ----------
k_ = sp.Symbol('k')
aser = 0
for k in range(6):
    aser += sp.rf(sp.Rational(1, 2), k) / sp.factorial(k) * (z / (4 * c)) ** k / ((ap + k) * (k + sp.Rational(1, 2)))
aser = aser * (4 * c) ** sp.Rational(-1, 2) / (p * sp.pi)
fz = sp.expand(-(sp.pi ** 2 / 4) * z * aser ** 2)
F1 = sp.simplify(fz.coeff(z, 1))
assert sp.simplify(F1 + 1 / (c * (p + 2) ** 2)) == 0, "f'(0), Lemma E.4(i)"
fv = sp.expand(fz.subs(z, -v ** 2))                                   # f > 0 on the negative axis
fh = v * sp.sqrt(sp.expand(sp.simplify(fv / v ** 2 * c * (p + 2) ** 2))) / (sc * (p + 2))   # f^{1/2} > 0
a2h = sp.sqrt(4 * c + v ** 2) / v
rho = (v / (2 * sc) + sp.sqrt(1 + v ** 2 / (4 * c))) ** (al + 1)
s3 = sp.diag(1, -1)
a1b, b1b = (4 * al ** 2 - 1) / 8, (4 * al ** 2 + 3) / 8
a2b, b2b = (4 * al ** 2 - 1) * (4 * al ** 2 - 9) / 128, (4 * al ** 2 - 1) * (4 * al ** 2 + 15) / 128
Xi1 = sp.Matrix([[-(a1b + b1b), I * (a1b - b1b)], [I * (a1b - b1b), a1b + b1b]]) / 2
Xi2 = sp.Matrix([[a2b + b2b, I * (a2b - b2b)], [-I * (a2b - b2b), a2b + b2b]]) / 2
assert sp.simplify(Xi2.trace() + Xi1.det()) == 0
Q0 = sp.Matrix([[-(1 + 4 * al ** 2), 2 * I], [2 * I, 1 + 4 * al ** 2]])
assert (16 * s3 * Xi1 * s3 / 2 - Q0).applyfunc(lambda e: sp.simplify(sp.expand(e))) == sp.zeros(2, 2)   # Delta1^0 = Q0/(16 f^{1/2}) form


def conj_hard(Qm):
    Zh = sp.Matrix([[Qm[0, 0], rho ** 2 * Qm[0, 1]], [Qm[1, 0] / rho ** 2, Qm[1, 1]]])
    Yh = Ti * Zh * T
    return T * sp.Matrix([[Yh[0, 0], a2h * Yh[0, 1]], [Yh[1, 0] / a2h, Yh[1, 1]]]) * Ti


D10 = conj_hard(s3 * Xi1 * s3) / (2 * fh)
D20 = conj_hard(s3 * Xi2 * s3) / (4 * fh ** 2)
v2D1 = D10.applyfunc(lambda e: ser(e * v ** 2, v, 4))
v4D2 = D20.applyfunc(lambda e: ser(e * v ** 4, v, 6))
for k in (1, 3):
    assert all(sp.simplify(v2D1[i, j].coeff(v, k)) == 0 for i in range(2) for j in range(2))
for k in (1, 3, 5):
    assert all(sp.simplify(v4D2[i, j].coeff(v, k)) == 0 for i in range(2) for j in range(2)), "Delta2^0 odd"
A0 = v2D1.applyfunc(lambda e: sp.simplify(-e.coeff(v, 0)))
C0 = v2D1.applyfunc(lambda e: sp.simplify(e.coeff(v, 2)))
_dA = (A0 - c * (p + 2) * (4 * al ** 2 - 1) / 16 * sp.Matrix([[1, I], [I, -1]])).applyfunc(lambda e: sp.simplify(sp.expand(e))); print("A0 diff:", _dA); assert _dA == sp.zeros(2, 2)
# Delta2^0 = E2/z^2 + E1/z + ...; with z = -v^2: v^4 D2 = E2 - E1 v^2 + ...
E1h = v4D2.applyfunc(lambda e: sp.simplify(-e.coeff(v, 2)))
E2h = v4D2.applyfunc(lambda e: sp.simplify(e.coeff(v, 0)))
assert E2h == sp.zeros(2, 2), 'Delta2^0 has only a simple pole at 0 (review B F6)'
print("hard edge done: A_0 reproduces Lemma E.5; Delta2^0 meromorphic (even), simple pole at 0 (z^-2 coefficient = 0, asserted)")

# ---------- second-order moment R_1^(2) ----------
# R1_in near 4c = A0/z - (reg0 + reg1 (z-4c) + ...);  Delta1^r = Br/(z-4c)^2 + Ar/(z-4c) + ...
w_ = sp.Symbol('w')   # w = z - 4c
A0_at4c = (A0 / (4 * c), -A0 / (16 * c ** 2))        # A0/z = A0/(4c) - A0 w/(16 c^2) + ...
r0 = A0_at4c[0] - reg0
r1 = A0_at4c[1] - reg1
res_soft = r0 * Ar + r1 * Br + res_D2r
# R1_in near 0 = A_r/(z-4c) + B_r/(z-4c)^2 - (C0 + ...);  Delta1^0 = A0/z + C0 + ...
R0in = -Ar / (4 * c) + Br / (16 * c ** 2) - C0
res_hard = R0in * A0 + E1h
R12 = (res_soft + res_hard).applyfunc(lambda e: sp.simplify(sp.expand(e)))

# ---------- extraction ----------
P1 = sp.Matrix([[0, I * c], [-I * c, 0]])
eps = sp.Symbol('eps')
Atot = A0 + Ar
Q1 = P1 + eps * Atot + eps ** 2 * R12
bb = sp.expand(Q1[0, 1] * Q1[1, 0] / c ** 2)
bser = sp.series(sp.sqrt(bb), eps, 0, 3).removeO()
d1 = sp.simplify(bser.coeff(eps, 1))
d2 = sp.simplify(sp.expand(bser.coeff(eps, 2)))
s = sp.Symbol('s')
assert sp.simplify(d1 + p * (al + 1) / 2) == 0
d2_s = sp.factor(sp.simplify(d2.subs(al, (s - 1 - p) / p)))
conj = (p + 1) * (s - 1) ** 2 / (8 * p) - (p + 2) * (s - 1 - p) ** 2 / (8 * p ** 2) + (p + 1) / 12
print("d1 =", sp.factor(d1.subs(al, (s - 1 - p) / p)))
print("d2 (from RH, second order) =", d2_s)
print("d2 - closed form of Thm E2.1 =", sp.simplify(d2_s - conj))
print("depends on c?", sp.simplify(sp.diff(d2_s, c)) != 0, "(automatic: inputs depend on z/c only)")
assert sp.simplify(d2_s - conj) == 0 and sp.simplify(sp.diff(d2_s, c)) == 0
# Corollary E2.7: exponent of the Christoffel function at 0
d1f = lambda S: -(S - 1) / 2
dp = sp.simplify(conj - conj.subs(s, s + 2 * p) - (d1f(s) ** 2 - d1f(s + 2 * p) ** 2) / 2)
assert sp.simplify(dp - ((s - 1) / p - p / 2)) == 0
gam = sp.simplify(-p - (s - 1) - 2 * dp)
assert sp.simplify(gam + (p + 2) * (s - 1) / p) == 0
print("Cor E2.7: delta' =", sp.factor(dp), "; exponent gamma =", sp.factor(gam))
print("ALL ASSERTIONS PASSED")
