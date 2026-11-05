"""JZC_SHIFT §2-3: exact checks of the proof mechanism (dispersionless Toda + hard-edge reduction + hodograph) and of the
closed form of the index-shift prediction.  Exact algebra (sympy); nothing fitted.
 (L) Lagrange-Buermann closed form LB vs direct series reversion of x = N - (1/p) sum eps_a x^{-p j_a} (symbolic p and j's):
     1 time to order 6, 2 times to total order 5, 3 times to total order 4.  Controls: 1/(2p), exponent p + 2 + S.
 (S) dispersionless symbols: H_j(a, b) = (J^j)_nn-symbol, G_j(a, b) = (b J^j_{n+1,n})-symbol from path counting; on the hard-edge
     line a = 2b: H_j = C(2j, j) b^j and G_j = C(2j, j) j/(j+1) b^{j+1} (j <= 15); the line a = 2b is invariant
     (d_n G_j = b d_n H_j there, as functions of a(n), b(n); j <= 10); control: the soft line a = 3b is not invariant.
 (H) hodograph: b = c x^{-p}, x = n + sum_a t_a V_a(x), V_a = (j_a C(2j_a, j_a)/2) c^{j_a} x^{-p j_a}, solves the reduced
     dispersionless flows d_{t_a} b = (1/2) b d_n H_{j_a}(2b, b) (formal power series in t, symbolic p, c; j-sets {1}, {1,2}, {2,3});
     and its Taylor coefficients are LB (the parametrisation eps_a = -(p j_a/2) C(2j_a, j_a) c^{j_a} t_a).
 (D) Lemma D on the DISCRETE formal Toda hierarchy (shift_common.FT): generic initial data alpha_n = 2n^{-p}(1 + sum_i A_i n^{-i}),
     b_n = n^{-p}(1 + sum_i B_i n^{-i}) (A_i, B_i free symbols, p symbolic): every t^beta coefficient of n^p b_n starts at n^{-|beta|}
     and its n^{-|beta|} coefficient is LB (free of all A_i, B_i); flows commute (asserted inside FT.flow).  Exponent sets
     {1} (order 7), {2} (6), {3} (5), {1,2} (5), {1,3} (4), {1,2,3} (4).  Also the diagonal: alpha's leading parts are 2 b's.
     Controls: initial diagonal alpha_n = 0 (no hard edge) and alpha_n = 3n^{-p} (soft point): the leads are NOT LB.
 (A0) the normalisation of alpha_n's leading term from (T1) and E3.7: with alpha_n = 2 A0 n^{-p}(1 + ...), the first-order j = 1
     lead equals E3.7's p/2 (engine units) iff A0 = 1."""
import os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
from sympy.polys.rings import ring
from sympy import QQ
provenance(__file__, os.path.join(HERE, 'shift_common.py'))
C = Checks()
P = sp.Symbol('p', positive=True)
z = lambda e: sp.simplify(sp.cancel(sp.together(e))) == 0

# ---------------------------------------------------------------- (L)
t0 = time.time()
J = sp.symbols('j0:3', positive=True)
for nt, order in ((1, 6), (2, 5), (3, 4)):
    js = J[:nt]; ser = LB_series(js, P, order); bad = []; ctrl1 = ctrl2 = 0; nm = 0
    for mon, c in ser.items():
        if sum(mon) == 0: assert c == 1; continue
        # coefficient of s^beta (s_a = eps_a N^{-1-p j_a}) in (x/N)^{-p}:  LB / prod (p j_a/2)^{beta_a}
        pred = LB(mon, js, P)/sp.Mul(*[(P*j/2)**b for b, j in zip(mon, js)]); nm += 1
        if not z(c - pred): bad.append(mon)
        if sum(mon) >= 2:
            ctrl1 += z(c - LB(mon, js, P, kappa=sp.Rational(1, 2))/sp.Mul(*[(P*j/2)**b for b, j in zip(mon, js)]))
            ctrl2 += z(c - LB(mon, js, P, shiftc=2)/sp.Mul(*[(P*j/2)**b for b, j in zip(mon, js)]))
    C.check(f"(L) {nt} time(s), total order <= {order}: closed form = series reversion for all {nm} monomials", not bad)
    C.check(f"(L) control {nt} time(s): coefficient 1/(2p) reproduces some order >= 2 monomial", ctrl1 > 0, must_fail=True)
    C.check(f"(L) control {nt} time(s): exponent p + 2 + S reproduces some order >= 2 monomial", ctrl2 > 0, must_fail=True)
print(f"   (L) {time.time() - t0:.0f}s", flush=True)

# ---------------------------------------------------------------- (S)
a_, b_ = sp.symbols('a b')
def Hsym(j):   # (1/2pi) int (a + 2b cos th)^j: paths of length j returning to 0 (k up, k down, j-2k stay)
    return sum(sp.factorial(j)/(sp.factorial(k)**2*sp.factorial(j - 2*k))*a_**(j - 2*k)*b_**(2*k) for k in range(j//2 + 1))
def Gsym(j):   # b * (J^j)_{n+1,n}-symbol: paths with net +1 (k+1 up, k down, j-2k-1 stay)
    return b_*sum(sp.factorial(j)/(sp.factorial(k + 1)*sp.factorial(k)*sp.factorial(j - 2*k - 1))*a_**(j - 2*k - 1)*b_**(2*k + 1)
                  for k in range((j - 1)//2 + 1))
okH = all(sp.expand(Hsym(j).subs(a_, 2*b_) - sp.binomial(2*j, j)*b_**j) == 0 for j in range(1, 16))
okG = all(sp.expand(Gsym(j).subs(a_, 2*b_) - sp.binomial(2*j, j)*sp.Rational(j, j + 1)*b_**(j + 1)) == 0 for j in range(1, 16))
C.check("(S) H_j(2b, b) = C(2j, j) b^j, j <= 15", okH)
C.check("(S) G_j(2b, b) = C(2j, j) j/(j+1) b^{j+1}, j <= 15", okG)
nn = sp.Symbol('n'); af = sp.Function('A')(nn); bf = sp.Function('B')(nn)
def inv_ok(j, ratio):
    e = sp.diff(Gsym(j).subs({a_: af, b_: bf}), nn) - (ratio/2)*bf*sp.diff(Hsym(j).subs({a_: af, b_: bf}), nn)
    # d_t (a - ratio b) = d_n G - ratio (b/2) d_n H; on a = ratio*b it must vanish for invariance
    return sp.simplify(e.subs(af, ratio*bf).doit()) == 0
C.check("(S) the hard-edge line a = 2b is invariant under every flow j <= 10", all(inv_ok(j, 2) for j in range(1, 11)))
C.check("(S) control: the line a = 3b is invariant (j = 2)", inv_ok(2, 3), must_fail=True)

# ---------------------------------------------------------------- (H)
t0 = time.time()
cc, n_ = sp.symbols('c n', positive=True)
for jset, order in (((1,), 5), ((1, 2), 4), ((2, 3), 3)):
    ts = sp.symbols(f"t0:{len(jset)}"); lam = sp.Symbol('lam')
    V = lambda x, j: sp.Rational(j, 2)*sp.binomial(2*j, j)*cc**j*x**(-P*j)
    # fixed point x = n + sum t_a V_a(x) as a power series in lam (t_a -> lam t_a)
    x = n_
    for _ in range(order + 1):
        x = n_ + sum(lam*t*V(x, j) for t, j in zip(ts, jset))
        x = sp.series(x, lam, 0, order + 1).removeO()
    bb = sp.expand(sp.series(cc*x**(-P), lam, 0, order + 1).removeO())
    okpde = True
    for t, j in zip(ts, jset):
        lhs = sp.diff(bb, t)                      # bb is a function of lam*t: d_t bb = lam (d_T b)(lam t)
        rhs = lam*sp.Rational(1, 2)*bb*sp.diff(sp.binomial(2*j, j)*bb**j, n_)
        d = sp.series(sp.expand(lhs - rhs), lam, 0, order + 1).removeO()
        okpde &= sp.simplify(d) == 0
    C.check(f"(H) hodograph solves the reduced flows, exponents {jset}, to order {order}", okpde)
    # Taylor coefficients vs LB:  n^p b/c = (n/x)^p, eps_a = -(p j/2) C(2j, j) c^j t_a, in natural variable N -> n
    okLB = True
    Pl = sp.Poly(sp.expand(bb*n_**P/cc), lam)
    for (m,), cm in Pl.terms():
        if m == 0: continue
        Pt = sp.Poly(sp.expand(cm), *ts)
        for mon, cv in Pt.terms():
            S_ = P*sum(b*j for b, j in zip(mon, jset))
            eps = sp.Mul(*[(-(P*j/2)*sp.binomial(2*j, j)*cc**j)**b for b, j in zip(mon, jset)])
            pred = eps*poch(P + 1 + S_, m - 1)/(sp.Mul(*[sp.factorial(b) for b in mon])*P**(m - 1))*n_**(-S_ - m)
            okLB &= sp.simplify(sp.powsimp(cv - pred, force=True)) == 0
    C.check(f"(H) its Taylor coefficients are the LB coefficients (exponents {jset}, order {order})", okLB)
print(f"   (H) {time.time() - t0:.0f}s", flush=True)

# ---------------------------------------------------------------- (D)
t0 = time.time()
ps = sp.Symbol('p')
def generic_run(js, M, a_lead=2, a_zero=False):
    D = M
    names = ['p'] + [f'A{i}' for i in range(1, D + 1)] + [f'B{i}' for i in range(1, D + 1)]
    R, *g = ring(','.join(names), QQ); p = g[0]; A = g[1:D + 1]; B = g[D + 1:]
    ft = FT(R, p, js, D, M)
    a0 = [R(0)]*(D + 1) if a_zero else [R(a_lead)] + [a_lead*x for x in A]
    b0 = [R(1)] + list(B)
    a, b, nc = ft.flow(a0, b0)
    return a, b, nc
for js, M in (((1,), 7), ((2,), 6), ((3,), 5), ((1, 2), 5), ((1, 3), 4), ((1, 2, 3), 4)):
    a, b, nc = generic_run(js, M)
    low = lead = diag = True; nmon = 0
    for key, v in b.items():
        beta = key[1]; m = sum(beta)
        if m == 0: continue
        nmon += 1
        low &= all(v[i] == 0 for i in range(m))
        pred = LB(beta, js, ps)*sp.Mul(*[(-sp.binomial(2*j, j))**bb for bb, j in zip(beta, js)])
        lead &= sp.simplify(sp.sympify(str(v[m].as_expr())) - pred) == 0
        va = a[key]
        low &= all(va[i] == 0 for i in range(m))
        diag &= (va[m] - 2*v[m]) == 0
    C.check(f"(D) exponents {js}, order <= {M} ({nmon} monomials, {nc} commutation checks): coefficients below n^-|beta| vanish "
            f"(b and alpha)", low)
    C.check(f"(D) exponents {js}: the n^-|beta| coefficient of n^p b_n is LB, for generic A_i, B_i", lead)
    C.check(f"(D) exponents {js}: alpha's leading parts are twice b's (hard-edge line a = 2b preserved)", diag)
for lab, kw in (("alpha_n = 0 initially", dict(a_zero=True)), ("alpha_n = 3 n^-p (1 + ...) initially", dict(a_lead=3))):
    a, b, nc = generic_run((1, 2), 3, **kw); lead = True
    for key, v in b.items():
        beta = key[1]; m = sum(beta)
        if m < 2: continue
        pred = LB(beta, (1, 2), ps)*sp.Mul(*[(-sp.binomial(2*j, j))**bb for bb, j in zip(beta, (1, 2))])
        lead &= (m < len(v)) and sp.simplify(sp.sympify(str(v[m].as_expr())) - pred) == 0
    C.check(f"(D) control: {lab}: leads of order >= 2 are LB", lead, must_fail=True)
print(f"   (D) {time.time() - t0:.0f}s", flush=True)

# ---------------------------------------------------------------- (A0)
R, p, A0 = ring('p,A0', QQ)
ft = FT(R, p, (1,), 1, 1)
a, b, _ = ft.flow([2*A0, R(0)], [R(1), R(0)])
lead = sp.sympify(str(b[(1, (1,))][1].as_expr()))/(-2)         # engine units: e = mu C(2,1), mu = -t n^-p
A0s = sp.Symbol('A0')
sol = sp.solve(sp.Eq(lead, ps/2), A0s)
C.check(f"(A0) first-order j = 1 lead (= {sp.factor(lead)} in engine units) equals E3.7's p/2 iff A0 = 1", sol == [1])
C.finish()
