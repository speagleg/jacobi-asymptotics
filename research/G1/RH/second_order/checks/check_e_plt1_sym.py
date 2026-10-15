"""Plan 67 (E_plt1.md §§4-6): exact symbolic first-order variation of the 1/n correction R^(1) under the band-weight
factor exp(-lam z), for sigma_{p,s}, 0 < p < 1 (the formulas are the same for every p; lam is a free symbol).

Setting: E_pgt1.md §§3-5 and check_e_sym.py (Plan 65).  In the Q-frame the circle jumps are
  Airy:   Delta_1^r = -(1/phit) P0 (-w)^{-s3/2} X (-w)^{s3/2} P0^{-1},
  Bessel: Delta_1^0 = (1/(16 f^{1/2})) P0 rho^{s3} Q0 rho^{-s3} P0^{-1},   rho^2 = e^{-+ i pi alpha}/w,
and they depend on the weight only through w = D_W^2/W_0.  E_plt1 Lemma F.1 shows that the band factor of the seam
geometry is H_n(z) = H_n(1) exp(-lam_n (z - 1) + O(n^{-2p})), lam_n = 2 zeta(-p) n^{-p}.  For the weight factor
q = exp(-lam x) on [0, 4c] the Szego function is explicit:  D_q^2/q = exp(lam R(z)),  R(z) = (z(z-4c))^{1/2} ~ z
(E_plt1 Lemma F.2; asserted below from the Szego integral).  So  w = w^mod * exp(lam R):
  soft edge:  (-w) -> (-w) (1 + lam R + O(lam^2)),  R = z^{1/2} u, u = (z-4c)^{1/2};
  hard edge:  rho^2 -> rho^2 (1 - lam R + ...),  R = -v (4c + v^2)^{1/2} on z = -v^2.
Outputs (coefficients of lam, i.e. of the first-order variation):
  A_r^lin, B_r^lin (= 0), A_0^lin (= 0), C_0^lin; the lam parts of n^{2p} b_n^2/c^2, n^p alpha_n/(2c), alpha_n/(2b_n)
  and n^p g_{n-1}/c at order 1/n; [5] the unfolding to the symmetric chain gamma_N^2.  All asserted.  The model parts reproduce E_pgt1 Lemma E.5 / Thm E.1 / Cor E.6 (asserted).
Series are truncated polynomial expansions (exact to the orders used: Delta_1 is meromorphic with the pole orders of
E_plt1 Lemma E'.5, so the Laurent coefficients need only finitely many terms).  Inputs Q0, X and the Lemma E.4 closed forms as in check_e_sym.py."""
import sympy as sp

I = sp.I
u, v, x = sp.symbols('u v x', positive=True)
al, p, c = sp.symbols('alpha p c', positive=True)
lam, kap, k2, F2 = sp.symbols('lam kappa kappa2 F2')
T = sp.Matrix([[1, 1], [I, -I]]) / sp.sqrt(2)
Ti = T.inv()
Mm = sp.Matrix([[1, I], [I, 1]]) / sp.sqrt(2)
O = 6
sc = sp.sqrt(c)


def tr(e, var=u, o=O):
    e = sp.expand(e)
    return sum(e.coeff(var, k) * var ** k for k in range(0, o))


def lin(e):
    """drop lam^2 and higher (e polynomial in lam)."""
    e = sp.expand(e)
    return sp.expand(e.coeff(lam, 0) + lam * e.coeff(lam, 1))


# ---------------- [0] Szego function of exp(-lam x): log D_q^2 = -lam z + lam R  (check at a sample point)
import mpmath as mpm
mpm.mp.dps = 30
zs, cs = mpm.mpf(7), mpm.mpf(1)
Rz = mpm.sqrt(zs * (zs - 4 * cs))
val = mpm.quad(lambda ph: 2 * 4 * cs * mpm.sin(ph) ** 2 / (zs - 4 * cs * mpm.sin(ph) ** 2), [0, mpm.pi / 2]) / mpm.pi   # x = 4c sin^2(phi)
assert abs(val - (zs / Rz - 1)) < mpm.mpf('1e-25')
print("[0] (1/pi) int_0^{4c} x dx/(sqrt(x(4c-x))(z-x)) = z/R(z) - 1 at c = 1, z = 7 (so D_q^2/q = exp(lam R)): ok")

# ---------------- [1] soft edge, Laurent expansion in u = (z - 4c)^{1/2}
X = sp.Matrix([[-sp.Rational(1, 72), -I / 12], [-I / 12, sp.Rational(1, 72)]])
xx = u ** 2 / (4 * c)
sq1 = tr(1 + xx / 2 - xx ** 2 / 8)                          # sqrt(1 + u^2/(4c))
sqz = 2 * sc * sq1                                          # z^{1/2}
a2 = tr(u / (2 * sc) * tr(1 - xx / 2 + 3 * xx ** 2 / 8))    # a^2 = u / z^{1/2}
y = sq1 - 1 + u / (2 * sc)
L = tr(-(y - y ** 2 / 2 + y ** 3 / 3 - y ** 4 / 4 + y ** 5 / 5))   # log(2 sqrt c/(z^{1/2} + u))


def expser(e):
    s, t = 1, 1
    for k in range(1, O):
        t = tr(t * e / k)
        s += t
    return tr(s)


Rr = tr(sqz * u)                                            # R = z^{1/2} (z-4c)^{1/2}
h2 = lin(tr(expser((2 + 2 * al) * L) * (1 + lam * Rr)))     # -w
ih2 = lin(tr(expser(-(2 + 2 * al) * L) * (1 - lam * Rr)))   # (-w)^{-1}
Z = sp.Matrix([[X[0, 0], X[0, 1] * ih2], [X[1, 0] * h2, X[1, 1]]])
Y = (Ti * Z * T).applyfunc(sp.expand)
Mu = (T * sp.Matrix([[tr(u * Y[0, 0]), tr(u * a2 * Y[0, 1])], [tr(sqz * Y[1, 0]), tr(u * Y[1, 1])]]) * Ti).applyfunc(sp.expand)
D1u4 = Mu.applyfunc(lambda e: lin(tr(e * (1 - k2 * u ** 2 + k2 ** 2 * u ** 4) / kap)))
for k in (1, 3):
    assert all(sp.simplify(D1u4[i, j].coeff(u, k)) == 0 for i in range(2) for j in range(2)), "odd powers must vanish"
sub = {kap: 1 / (6 * p * c ** sp.Rational(3, 2)), k2: -(7 + 4 / p) / (40 * c)}
Br_all = D1u4.applyfunc(lambda e: sp.expand(sp.simplify(e.coeff(u, 0).subs(sub))))
ArK_all = D1u4.applyfunc(lambda e: sp.expand(sp.simplify(e.coeff(u, 2).subs({kap: sub[kap]}))))   # kappa2 free
Ar_all = ArK_all.applyfunc(lambda e: sp.expand(e.subs(sub)))
Br0, Brl = Br_all.applyfunc(lambda e: sp.factor(e.coeff(lam, 0))), Br_all.applyfunc(lambda e: sp.factor(e.coeff(lam, 1)))
Ar0, Arl = Ar_all.applyfunc(lambda e: sp.factor(e.coeff(lam, 0))), Ar_all.applyfunc(lambda e: sp.factor(e.coeff(lam, 1)))
print("[1] soft edge: odd powers of (z-4c)^{1/2} vanish including the lam terms (asserted)")
print("  B_r^lin =", Brl)
print("  A_r^lin =", Arl)
assert Brl == sp.zeros(2, 2)
assert sp.simplify(Arl - c ** 2 * p * sp.Matrix([[-(al + 1), I * (al + 2)], [I * al, al + 1]])) == sp.zeros(2, 2)
assert sp.simplify(Ar0 - (c / 48) * sp.Matrix([[12 * al ** 2 * p + 24 * al * p + 11 * p + 2, -I * (12 * al ** 2 * p + 48 * al * p + 49 * p + 2)],
                                                [-I * (12 * al ** 2 * p + p + 2), -(12 * al ** 2 * p + 24 * al * p + 11 * p + 2)]])) == sp.zeros(2, 2)
assert sp.simplify(sp.diff(ArK_all.applyfunc(lambda e: e.coeff(lam, 1)), k2)) == sp.zeros(2, 2)
print("  A_r^lin = c^2 p [[-(alpha+1), i(alpha+2)], [i alpha, alpha+1]],  B_r^lin = 0  (asserted; A_r^lin free of kappa2)")
assert sp.simplify(Br0 - (5 * c ** 2 * p / 12) * sp.Matrix([[1, -I], [-I, -1]])) == sp.zeros(2, 2)
print("  (A_r^mod, B_r^mod reproduce E_pgt1 Lemma E.5: asserted for both)")

# ---------------- [2] hard edge, Laurent expansion on the negative axis z = -v^2 (truncated power series in v)
ap = 1 / p + sp.Rational(1, 2)
C0c = 1 / (sp.sqrt(4 * c) * sp.pi * (1 + p / 2))
tau1 = ap / (8 * c * (ap + 1))
f1 = -sp.pi ** 2 * C0c ** 2
f2v = f1 * 2 * tau1 / 3
OV = 6


def tv(e, o=OV):
    return tr(e, v, o)


yv = v ** 2 / (4 * c)
sv = tv(2 * sc * (1 + yv / 2 - yv ** 2 / 8 + yv ** 3 / 16))          # (4c + v^2)^{1/2}
isv = tv((1 - yv / 2 + 3 * yv ** 2 / 8 - 5 * yv ** 3 / 16) / (2 * sc))  # 1/(4c + v^2)^{1/2}
wv = F2 * v ** 2 / (-f1)
gv = tv((1 - wv / 2 + 3 * wv ** 2 / 8) / sp.sqrt(-f1))               # 1/(-f1 + F2 v^2)^{1/2}; f^{1/2} = v/g
xa = v / (2 * sc)
ash = tv(xa - xa ** 3 / 6 + 3 * xa ** 5 / 40)                          # asinh(v/(2 sqrt c))


def expv(e):
    s_, t_ = 1, 1
    for k in range(1, OV):
        t_ = tv(t_ * e / k)
        s_ += t_
    return tv(s_)


Rv = -v * sv                                    # R on the negative axis (both sides)
r2 = lin(tv(expv(2 * (al + 1) * ash) * (1 - lam * Rv)))       # rho^2 (model: ((v/2sqrt c) + sqrt(1 + v^2/4c))^{2(alpha+1)})
ir2 = lin(tv(expv(-2 * (al + 1) * ash) * (1 + lam * Rv)))     # rho^{-2}
Q0 = sp.Matrix([[-(1 + 4 * al ** 2), 2 * I], [2 * I, 1 + 4 * al ** 2]])
Zh = sp.Matrix([[Q0[0, 0], r2 * Q0[0, 1]], [Q0[1, 0] * ir2, Q0[1, 1]]])
Yh = (Ti * Zh * T).applyfunc(sp.expand)
# v^2 Delta_1^0 = (g/16) T [[v Y11, s Y12], [(v^2/s) Y21, v Y22]] T^{-1}   (a^2 = s/v, f^{1/2} = v/g)
Mh = sp.Matrix([[tv(v * Yh[0, 0]), tv(sv * Yh[0, 1])], [tv(v ** 2 * isv * Yh[1, 0]), tv(v * Yh[1, 1])]])
v2D = (T * Mh * Ti).applyfunc(lambda e: lin(tv(e * gv / 16, 4)))
for k in (1, 3):
    assert all(sp.simplify(v2D[i, j].coeff(v, k)) == 0 for i in range(2) for j in range(2)), "odd powers must vanish"
A0_all = v2D.applyfunc(lambda e: sp.expand(sp.simplify(-e.coeff(v, 0).subs(F2, f2v))))
CzF_all = v2D.applyfunc(lambda e: sp.expand(e.coeff(v, 2)))
A0l = A0_all.applyfunc(lambda e: sp.factor(e.coeff(lam, 1)))
A0m = A0_all.applyfunc(lambda e: sp.factor(e.coeff(lam, 0)))
C0m = CzF_all.applyfunc(lambda e: sp.factor(sp.simplify(e.coeff(lam, 0).subs(F2, f2v))))
C0l = CzF_all.applyfunc(lambda e: sp.factor(sp.simplify(e.coeff(lam, 1).subs(F2, f2v))))
print("[2] hard edge: odd powers of z^{1/2} vanish including the lam terms (asserted)")
print("  A_0^lin =", A0l)
print("  C_0^lin =", C0l)
assert A0l == sp.zeros(2, 2)
assert sp.simplify(A0m - c * (p + 2) * (4 * al ** 2 - 1) / 16 * sp.Matrix([[1, I], [I, -1]])) == sp.zeros(2, 2)
C0ref = ((p + 2) / (96 * (3 * p + 2))) * sp.Matrix([[-(10 * al ** 2 * p + 8 * al ** 2 - 36 * al * p - 24 * al - 7 * p - 5),
                                                     I * (26 * al ** 2 * p + 16 * al ** 2 + 72 * al * p + 48 * al + 70 * p + 47)],
                                                    [I * (26 * al ** 2 * p + 16 * al ** 2 - 2 * p - 1),
                                                     10 * al ** 2 * p + 8 * al ** 2 - 36 * al * p - 24 * al - 7 * p - 5]])
assert sp.simplify(C0m - C0ref) == sp.zeros(2, 2)
assert sp.simplify(CzF_all.applyfunc(lambda e: sp.diff(e.coeff(lam, 1), F2))) == sp.zeros(2, 2)
print("  A_0^lin = 0; A_0^mod, C_0^mod = E_pgt1 Lemma E.5; C_0^lin is free of F2 (all asserted)")

# ---------------- [3] extraction at order 1/n
w = sp.Symbol('w')
aa = sp.series((1 - 4 * c * w) ** sp.Rational(1, 4), w, 0, 4).removeO()
P0w = sp.Matrix([[(aa + 1 / aa) / 2, (aa - 1 / aa) / (2 * I)], [-(aa - 1 / aa) / (2 * I), (aa + 1 / aa) / 2]])
P0w = P0w.applyfunc(lambda e: sp.series(e, w, 0, 3).removeO())
P1 = P0w.applyfunc(lambda e: e.coeff(w, 1))
P2 = P0w.applyfunc(lambda e: e.coeff(w, 2))
eps = sp.Symbol('eps')                      # eps = 1/n
A = A0m + Ar_all
Q1 = P1 + eps * A
Q2 = P2 + eps * A * P1 + eps * (4 * c * Ar_all + Br_all)
bfun = sp.series(sp.expand(Q1[0, 1] * Q1[1, 0]) / c ** 2, eps, 0, 2).removeO()
afun = sp.series(Q2[0, 1] / Q1[0, 1] - Q1[1, 1], eps, 0, 2).removeO()
b1 = sp.expand(sp.simplify(bfun.coeff(eps, 1)))
a1 = sp.expand(sp.simplify(afun.coeff(eps, 1) / (2 * c)))
d1, d1l = sp.factor(b1.coeff(lam, 0) / 2), sp.factor(b1.coeff(lam, 1) / 2)
ac, acl = sp.factor(a1.coeff(lam, 0)), sp.factor(a1.coeff(lam, 1))
print("[3] n^p b_n/c = 1 + (", d1, "+ lam *", d1l, ")/n + ...;  n^p alpha_n/(2c) = 1 + (", ac, "+ lam *", acl, ")/n + ...")
assert sp.simplify(d1 + p * (al + 1) / 2) == 0 and sp.simplify(ac + p * (al + 2) / 2) == 0
assert sp.simplify(d1l - c * p) == 0 and sp.simplify(acl - c * p) == 0
print("  lam-parts: c p for both (asserted); hence alpha_n/(2b_n) has no lam-part at order 1/n:", sp.simplify(acl - d1l))
print("  with lam = lam_n = 2 zeta(-p) n^{-p}:  the n^{-1-p} coefficient of n^p b_n/c and of n^p alpha_n/(2c) is 2 p c zeta(-p)")

# ---------------- [4] chain: n^p g_{n-1} = -(Q_1)_21 * Q_11(0)/Q_21(0)  (E_pgt1 §7.2, with lam)
R0 = -CzF_all.applyfunc(lambda e: e.subs(F2, f2v)) - Ar_all / (4 * c) + Br_all / (16 * c ** 2)
rho = lin(tv(expv((al + 1) * ash) * (1 - lam * Rv / 2)))      # rho -> rho exp(-lam R/2), first order
irho = lin(tv(expv(-(al + 1) * ash) * (1 + lam * Rv / 2)))
# Bm = T diag(a^{1/2}, a^{-1/2}) T^{-1} diag(rho, 1/rho) M, a^{1/2} = (s/v)^{1/2}, f^{1/4} = (v/g)^{1/2}:
#   w0 = lim T diag(h1, v h2) T^{-1}(rho M_11, M_21/rho) with h1 = (s/g)^{1/2}, h2 = (g s)^{-1/2};
#   w1 = lim (-i alpha/2) T diag(h3/v, h4) T^{-1}(rho M_12, M_22/rho), h3 = (s g)^{1/2}, h4 = (g/s)^{1/2}.
s0, g0 = sv.subs(v, 0), gv.subs(v, 0)
h1, h3, h4 = sp.sqrt(s0 / g0), sp.sqrt(s0 * g0), sp.sqrt(g0 / s0)
t0 = (Ti * sp.Matrix([rho * Mm[0, 0], irho * Mm[1, 0]])).applyfunc(lambda e: sp.expand(e).subs(v, 0))
w0 = (T * sp.Matrix([h1 * t0[0], 0])).applyfunc(sp.simplify)
t1 = (Ti * sp.Matrix([rho * Mm[0, 1], irho * Mm[1, 1]])).applyfunc(sp.expand)
assert sp.simplify(t1[0].subs(v, 0)) == 0
w1 = (-I * al / 2) * T * sp.Matrix([h3 * t1[0].coeff(v, 1), h4 * t1[1].subs(v, 0)])
w1 = w1.applyfunc(lambda e: sp.expand(sp.simplify(e)))
print("[4] Bessel column at 0: w0 =", list(w0), " w1 =", list(w1))
assert all(sp.simplify(sp.expand(e).coeff(lam, 1)) == 0 for e in w0)
r0 = sp.simplify(w0[0] / w0[1])
num = R0 * w0 + w1
r1 = sp.expand(sp.simplify(r0 * (num[0] / w0[0] - num[1] / w0[1])))
lead = sp.simplify(I * c * r0)
gp_all = sp.expand(sp.simplify((-A[1, 0] * r0 + I * c * r1) / lead))
gp, gpl = sp.factor(gp_all.coeff(lam, 0)), sp.factor(gp_all.coeff(lam, 1))
print("  n^p g_{n-1} = c (1 + (", gp, "+ lam *", gpl, ")/n + ...)")
assert sp.simplify(lead - c) == 0 and sp.simplify(gp - (al + sp.Rational(1, 2))) == 0
print("  lam-part of the 1/n coefficient of n^p g_{n-1}/c:", gpl)
assert sp.simplify(gpl - c * p) == 0
assert sp.simplify(C0l - (c * (p + 2) / 4) * sp.Matrix([[al + 1, I * (al + 2)], [I * al, -(al + 1)]])) == sp.zeros(2, 2)
print("  asserted: the lam-part is c p, the same as for b_n and alpha_n; so g_{n-1}, h_n, b_n, alpha_n all carry the same")
print("  relative n^{-1-p} correction kappa_p = 2 p c zeta(-p)")

# ---------------- [5] unfolding to the symmetric chain (E_plt1 §7.2, Cor E'.6), exact series algebra
# Inputs (proved above / Thm E'.1): g_{n-1} = c n^{-p}(1 + a/n + K n^{-1-p}), b_n^2 = c^2 n^{-2p}(1 - (s-1)/n + 2K n^{-1-p}),
# h_n = b_n^2/g_{n-1}; gamma_{2n}^2 = h_n, gamma_{2n-1}^2 = g_{n-1}.  Variables: e := 1/N, et := (N/2)^{-p} (so that
# N^{-1-p} = 2^{-p} e et); expansions to first order in e, keeping e*et, dropping e^2, e^2 et and et^2 (= O(N^{-2p})).
e, et, K, sv_ = sp.symbols('e eta K s', positive=True)
aa_ = (2 * sv_ - 2 - p) / (2 * p)


def trunc(expr):
    expr = sp.expand(sp.series(expr, e, 0, 2).removeO())
    return sp.expand(sum(e ** i * et ** j * expr.coeff(e, i).coeff(et, j) for i in (0, 1) for j in (0, 1)))


# N = 2n even: n = N/2, 1/n = 2e, n^{-p} = et, n^{-1-p} = 2 e et
ginv_even = 1 / (1 + aa_ * 2 * e + K * 2 * e * et)
ratio_even = trunc((1 - (sv_ - 1) * 2 * e + 2 * K * 2 * e * et) * ginv_even)          # gamma_N^2/(c (N/2)^{-p}) = h_n/(c n^{-p})
# N = 2n - 1 odd: n = (N+1)/2, 1/n = 2e/(1+e), n^{-p} = et (1+e)^{-p}; gamma_N^2 = g_{n-1}
ninv = 2 * e / (1 + e)
ratio_odd = trunc((1 + e) ** (-p) * (1 + aa_ * ninv + K * ninv * et * (1 + e) ** (-p)))
k0_, k1_ = -(sv_ - 1) - p / 2, -(p + 2) * aa_
for par, rat in ((1, ratio_even), (-1, ratio_odd)):
    rat = sp.expand(rat)
    assert sp.simplify(rat.coeff(e, 0) - 1) == 0
    c1 = rat.coeff(e, 1)
    assert sp.simplify(c1.coeff(et, 0) - (k0_ + par * k1_)) == 0, (par, sp.simplify(c1.coeff(et, 0)))
    assert sp.simplify(c1.coeff(et, 1) - 2 * K) == 0, (par, sp.simplify(c1.coeff(et, 1)))
print("[5] symmetric chain: gamma_N^2/(c(N/2)^{-p}) = 1 + (k0 + k1(-1)^N)/N + 2^{1+p} K N^{-1-p} + ..., both parities,")
print("    k0 = -(s-1) - p/2, k1 = -(p+2)a (asserted; K = kappa_p, no parity part in the N^{-1-p} term)")
print("ALL ASSERTIONS PASSED")
