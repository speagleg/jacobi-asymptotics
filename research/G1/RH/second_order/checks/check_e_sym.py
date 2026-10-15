"""Plan 65 (E_pgt1.md §§3-5): exact symbolic computation of the first-order correction R^(1) for sigma_{p,s}, p > 1.

All objects are in the Q-frame of Paper 2 (Q = D_inf^{-s3} V D_W^{s3}); global parametrix P0 = T a^{s3} T^{-1},
a = ((z-4c)/z)^{1/4}, T = [[1,1],[i,-i]]/sqrt2.  Model weight x^alpha (4c-x) (H_n replaced by a constant; Lemma E.2
shows the error is O(n^{-p}) in Delta_1).

 Airy (soft edge 4c):  Delta_1^r = -(1/phit) P0 (-w)^{-s3/2} X (-w)^{s3/2} P0^{-1},  X = [[-1/72,-i/12],[-i/12,1/72]],
     (-w)^{1/2} = (2 sqrt c/(z^{1/2}+(z-4c)^{1/2}))^{1+alpha},  phit = -kappa u^3 (1 + kappa2 u^2 + O(u^4)), u = (z-4c)^{1/2},
     kappa = 1/(6 p c^{3/2}), kappa2 = -(7+4/p)/(40c)   (Lemma E.4).
 Bessel (hard edge 0): Delta_1^0 = (1/(16 f^{1/2})) P0 rho^{s3} Q0 rho^{-s3} P0^{-1}, Q0 = [[-(1+4al^2), 2i],[2i, 1+4al^2]],
     rho = ((-z)^{1/2}/(2 sqrt c) + (1-z/(4c))^{1/2})^{1+alpha},  f = f1 z (1 + (2 tau1/3) z + O(z^2)),
     f1 = -pi^2 C0^2, C0 = (4c)^{-1/2}/(pi(1+p/2)), tau1 = a'/(8c(a'+1)), a' = 1/p + 1/2   (Lemma E.4).
Outputs: Laurent coefficients (A_r, B_r at 4c; A_0, C_0 at 0), and d1, the 1/n coefficient of n^p alpha_n/(2c), e1 (std),
gamma' (n^p g_{n-1} = c(1 + gamma'/n)), k0, k1.  Asserts the closed forms of Theorem E.1."""
import sympy as sp

I = sp.I
u, v = sp.symbols('u v', positive=True)
al, p, c = sp.symbols('alpha p c', positive=True)
kap, k2 = sp.symbols('kappa kappa2')
T = sp.Matrix([[1, 1], [I, -I]]) / sp.sqrt(2)
Ti = T.inv()
Mm = sp.Matrix([[1, I], [I, 1]]) / sp.sqrt(2)
O = 6
sc = sp.sqrt(c)


def tr(e, var=u, o=O):
    e = sp.expand(e)
    return sum(e.coeff(var, k) * var ** k for k in range(0, o))


# ---------------- soft edge: Laurent expansion in u = (z - 4c)^{1/2}
X = sp.Matrix([[-sp.Rational(1, 72), -I / 12], [-I / 12, sp.Rational(1, 72)]])
x = u ** 2 / (4 * c)
sq1 = tr(1 + x / 2 - x ** 2 / 8)                      # sqrt(1 + u^2/(4c))
sqz = 2 * sc * sq1                                      # z^{1/2}
a2 = tr(u / (2 * sc) * tr(1 - x / 2 + 3 * x ** 2 / 8))  # a^2 = u / z^{1/2}
y = sq1 - 1 + u / (2 * sc)
L = tr(-(y - y ** 2 / 2 + y ** 3 / 3 - y ** 4 / 4 + y ** 5 / 5))   # log(2 sqrt c/(z^{1/2} + u))


def expser(e):
    s, t = 1, 1
    for k in range(1, O):
        t = tr(t * e / k)
        s += t
    return tr(s)


h2, ih2 = expser((2 + 2 * al) * L), expser(-(2 + 2 * al) * L)        # (-w), (-w)^{-1}
Z = sp.Matrix([[X[0, 0], X[0, 1] * ih2], [X[1, 0] * h2, X[1, 1]]])
Y = (Ti * Z * T).applyfunc(sp.expand)
Mu = (T * sp.Matrix([[tr(u * Y[0, 0]), tr(u * a2 * Y[0, 1])], [tr(sqz * Y[1, 0]), tr(u * Y[1, 1])]]) * Ti).applyfunc(sp.expand)
# Delta_1^r = -(1/phit) P0(..)P0^{-1} = Mu/(kappa u^4) * (1 - kappa2 u^2 + ...)
D1u4 = Mu.applyfunc(lambda e: tr(e * (1 - k2 * u ** 2 + k2 ** 2 * u ** 4) / kap))
for k in (1, 3):
    assert all(sp.simplify(D1u4[i, j].coeff(u, k)) == 0 for i in range(2) for j in range(2)), "odd powers must vanish"
sub = {kap: 1 / (6 * p * c ** sp.Rational(3, 2)), k2: -(7 + 4 / p) / (40 * c)}
Br = D1u4.applyfunc(lambda e: sp.factor(sp.simplify(e.coeff(u, 0).subs(sub))))
Ar = D1u4.applyfunc(lambda e: sp.factor(sp.simplify(e.coeff(u, 2).subs(sub))))
print("soft edge: Delta_1^r = B_r/(z-4c)^2 + A_r/(z-4c) + O(1); odd powers of (z-4c)^{1/2} vanish")
print("  B_r =", Br)
print("  A_r =", Ar)

# ---------------- hard edge: Laurent expansion on the negative axis z = -v^2
ap = 1 / p + sp.Rational(1, 2)
C0 = 1 / (sp.sqrt(4 * c) * sp.pi * (1 + p / 2))
tau1 = ap / (8 * c * (ap + 1))
f1 = -sp.pi ** 2 * C0 ** 2
f2 = f1 * 2 * tau1 / 3
fh = v * sp.sqrt(-f1 + f2 * v ** 2)            # f^{1/2} (f > 0 on the negative axis)
a2h = sp.sqrt(4 * c + v ** 2) / v              # a^2
rho = (v / (2 * sc) + sp.sqrt(1 + v ** 2 / (4 * c))) ** (al + 1)
Q0 = sp.Matrix([[-(1 + 4 * al ** 2), 2 * I], [2 * I, 1 + 4 * al ** 2]])
Zh = sp.Matrix([[Q0[0, 0], rho ** 2 * Q0[0, 1]], [Q0[1, 0] / rho ** 2, Q0[1, 1]]])
Yh = Ti * Zh * T
Dh = T * sp.Matrix([[Yh[0, 0], a2h * Yh[0, 1]], [Yh[1, 0] / a2h, Yh[1, 1]]]) * Ti / (16 * fh)
v2D = Dh.applyfunc(lambda e: sp.expand(sp.series(e * v ** 2, v, 0, 4).removeO()))
for k in (1, 3):
    assert all(sp.simplify(v2D[i, j].coeff(v, k)) == 0 for i in range(2) for j in range(2)), "odd powers must vanish"
A0 = v2D.applyfunc(lambda e: sp.factor(sp.simplify(-e.coeff(v, 0))))   # v^2 D = -z D = -A0 - C0 z ... with z = -v^2
Cz = v2D.applyfunc(lambda e: sp.factor(sp.simplify(e.coeff(v, 2))))    # constant Laurent term C_0
print("hard edge: Delta_1^0 = A_0/z + C_0 + O(z)")
print("  A_0 =", A0)
assert sp.simplify(A0 - c * (p + 2) * (4 * al ** 2 - 1) / 16 * sp.Matrix([[1, I], [I, -1]])) == sp.zeros(2, 2)
print("  A_0 = c(p+2)(4 alpha^2-1)/16 [[1,i],[i,-1]]  (asserted)")
print("  C_0 =", Cz)

# ---------------- extraction: R^(1)(z) = A_0/z + A_r/(z-4c) + B_r/(z-4c)^2 outside the discs
w = sp.Symbol('w')
aa = sp.series((1 - 4 * c * w) ** sp.Rational(1, 4), w, 0, 4).removeO()
P0w = sp.Matrix([[(aa + 1 / aa) / 2, (aa - 1 / aa) / (2 * I)], [-(aa - 1 / aa) / (2 * I), (aa + 1 / aa) / 2]])
P0w = P0w.applyfunc(lambda e: sp.series(e, w, 0, 3).removeO())
P1 = P0w.applyfunc(lambda e: e.coeff(w, 1))
P2 = P0w.applyfunc(lambda e: e.coeff(w, 2))
eps = sp.Symbol('eps')            # eps = 1/n
A = A0 + Ar
R1 = eps * A
R2 = eps * (4 * c * Ar + Br)
Q1 = P1 + R1
Q2 = P2 + R1 * P1 + R2
bfun = sp.series(sp.expand(Q1[0, 1] * Q1[1, 0]) / c ** 2, eps, 0, 2).removeO()
afun = sp.series(Q2[0, 1] / Q1[0, 1] - Q1[1, 1], eps, 0, 2).removeO()
d1 = sp.factor(sp.simplify(bfun.coeff(eps, 1) / 2))
aco = sp.factor(sp.simplify(afun.coeff(eps, 1) / (2 * c)))
e1s = sp.factor(sp.simplify(aco - d1))
print("P1 =", P1, " P2 =", P2)
print("b(Q)/c^2 = 1 +", sp.factor(bfun.coeff(eps, 1)), "/n;  a(Q) =", sp.simplify(afun.coeff(eps, 0)), "+ (", sp.factor(afun.coeff(eps, 1)), ")/n")
print("d1 =", d1, ";  n^p alpha_n/(2c) = 1 + (", aco, ")/n;  e1 (std, alpha_n/(2b_n)) =", e1s)
assert sp.simplify(d1 + p * (al + 1) / 2) == 0
assert sp.simplify(aco + p * (al + 2) / 2) == 0
assert sp.simplify(e1s + p / 2) == 0

# ---------------- chain: n^p g_{n-1} = -(Q_1)_21 * Q_11(0)/Q_21(0)
R0 = -Cz - Ar / (4 * c) + Br / (16 * c ** 2)         # R^(1)(0)
aroot = sp.sqrt(a2h)
f4 = sp.sqrt(fh)
Bm = T * sp.diag(aroot, 1 / aroot) * Ti * sp.diag(rho, 1 / rho) * Mm
w0 = (Bm * sp.Matrix([f4, 0])).applyfunc(lambda e: sp.simplify(sp.limit(e, v, 0)))
w1 = (Bm * sp.Matrix([0, -I * al / (2 * f4)])).applyfunc(lambda e: sp.simplify(sp.limit(e, v, 0)))
print("Bessel column at zeta = 0: w0 =", list(w0), " w1 =", list(w1))
r0 = sp.simplify(w0[0] / w0[1])
num = R0 * w0 + w1
r1 = sp.simplify(r0 * (num[0] / w0[0] - num[1] / w0[1]))
lead = sp.simplify(I * c * r0)
gp = sp.factor(sp.simplify((-A[1, 0] * r0 + I * c * r1) / lead))
print("n^p g_{n-1} = (", lead, ") (1 + (", gp, ")/n)")
assert sp.simplify(lead - c) == 0 and sp.simplify(gp - (al + sp.Rational(1, 2))) == 0
k0 = sp.simplify(2 * d1 - p / 2)
k1 = sp.factor(sp.simplify(k0 + p - 2 * gp))
print("k0 =", sp.factor(k0), "= -(s-1) - p/2 ;  k1 =", k1, "= -(p+2) a, a = alpha + 1/2")
assert sp.simplify(k1 + (p + 2) * (al + sp.Rational(1, 2))) == 0
print("ALL ASSERTIONS PASSED")
