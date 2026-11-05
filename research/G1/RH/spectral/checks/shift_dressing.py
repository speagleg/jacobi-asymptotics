"""JZC_SHIFT §5: the dressings relative to the shift law are the dispersive (discrete) part of the Toda flow of the two integer
layers.  Exact algebra with the formal Toda engine FT (shift_common); lattice (beta = nu = alpha), c = 1.  Inputs: Theorem T (Toda
structure, PROVED-mod-cite), Theorem N.6(ii) (f2, the first-order layers g_j = A_j + B_j alpha^2 symbolic in j: m4_zeta_exact2 (A);
h2: m4_zeta_exact2 (B)), the exact p = 3/2 output h(j, k) (w2_exact H, cached JSON).
 (E1) the diagonal integer layer to n^-2 is DERIVED from (T1) and the exact j = 1 first-order layer (N^-2 = 0, N^-3 = (p/2) g_1):
      A1 = -p(alpha/2 + 1), A2 = ... ; equivalently (n/M)^p (1 + a2 M^-2), M = n + alpha/2 + 1, a2 = -(p+1)/24 + (p+1)(p+2)alpha^2/8
      (= m4_diag's NUMERICAL closed form); equals shift_common.lattice_initial.
 (E2) PREDICTED from (E1): the first-order layers for j = 2..8 (N^-2 = 0 and g_j = A_j + B_j alpha^2, the exact symbolic-j result).
 (E3) PREDICTED: the mu_1^2 layer (N^-3 = 0, h2 of JZC_M4_proof N.6(ii), all p, alpha).
 (E4) PREDICTED: h(j, k) at p = 3/2 for j, k <= 4 (vs the exact symbolic (j, k) output of w2_exact H); R1's e1^2 N^-4 at p = 3/2
      (symbolic j, shift_exact R1) at j <= 4.
 (E5) decomposition with f2, a2 as free symbols: g_j = [c0(j) + c_a(j) a2 + c_f(j) f2], closed forms in j (read off j <= 7, asserted
      j <= 10, and identically in symbolic j against A_j + B_j alpha^2 after substituting the lattice f2, a2).
 (E6) the "dressed index shift" ansatz n^p b/c = (n/x)^p F(x), F = 1 + f2 x^-2, x = N - (1/p) eps x^-p (1 + gamma x^-2), gamma fixed by
      g_1, does NOT give h2: control (must fail), and its defect is printed.
 (E7) parity (the odd relative orders vanish): with generic even integer layers (f2, f4, f6, a2, a4, a6 free; B centred at N, A at
      M = N + 1/2), every layer of exponents (1, 2) to order 3 has zero N^{-|beta|-1} and N^{-|beta|-3} coefficients.
 Controls (must fail): a2 := 0 in (E2); f2 := 0 in (E3); A centred at N instead of M in (E7)."""
import os, sys, json, glob, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
from sympy.polys.fields import field
from sympy import QQ
provenance(__file__, os.path.join(HERE, 'shift_common.py'))
C = Checks()
P, AL, BE, J, KK, F2s, A2s = sp.symbols('p alpha beta j k f2 a2')
z = lambda e: sp.simplify(sp.cancel(sp.together(e))) == 0
gA = lambda j: (j**2*(j**2 + 2*j - 2)*P**3 + 2*(j + 1)*(2*j**2 - 1)*P**2 + (5*j**2 + 2*j - 6)*P + 2*(j - 2))/(24*(2*j - 1)*P)
gB = lambda j: (P + 2)*(j**2*P**2 + (j + 1)*P + 2)/(8*(2*j - 1)*P)
g = lambda j: gA(j) + gB(j)*AL**2
f2l = (P + 1)/12 - (P + 2)*AL**2/8; a2l = -(P + 1)/24 + (P + 1)*(P + 2)*AL**2/8
h2 = (P + 1)*(P + 2)*(3*P**2 + 2*P + 1)/(8*P**2) + (P + 2)*(2*P**3 - P**2 - 7*P - 6)*AL**2/(16*P**2)
ex = lambda c: sp.sympify(str(c.as_expr()))
DEL = (AL + 1)/2

class FTfast(FT):
    """FT with (J^j)_{n,n+r} by the transfer recursion v_{i+1}(m') = sum_m v_i(m) J_{m,m'} (polynomial instead of exponential cost;
    same entries as FT.paths: J_{m,m} = S_m alpha, J_{m,m+1} = S_{m+1} b, J_{m,m-1} = S_m b)."""
    def Jpow(s, a, b, j, r, cache):
        def sh(X, name, k):
            if (name, k) not in cache: cache[(name, k)] = s.shift(X, k) if k != 0 else X
            return cache[(name, k)]
        one = {(0, tuple([0]*s.r)): [s.one] + [s.zero]*s.D}
        v = {0: one}
        for i in range(j):
            rem = j - i - 1; nv = {}
            for m, X in v.items():
                for d in (0, 1, -1):
                    m2 = m + d
                    if abs(m2 - r) > rem: continue
                    f = sh(a, 'a', m) if d == 0 else (sh(b, 'b', m + 1) if d == 1 else sh(b, 'b', m))
                    nv[m2] = s.add(nv[m2], s.mul(X, f)) if m2 in nv else s.mul(X, f)
            v = nv
        return v.get(r, {})


def run_ft(K, p, js, D, M, a0, b0):
    ft = FTfast(K, p, js, D, M); return ft.flow(a0, b0)

# ---------------------------------------------------------------- (FTfast = FT)
from sympy.polys.rings import ring
Rt, pt, *gt = ring('p,A1,A2,B1,B2', QQ)
a0t = [Rt(2), 2*gt[0], 2*gt[1]]; b0t = [Rt(1), gt[2], gt[3]]
same = True
for js in ((3,), (1, 4)):
    x1 = FT(Rt, pt, js, 2, 2).flow(a0t, b0t); x2 = FTfast(Rt, pt, js, 2, 2).flow(a0t, b0t)
    same &= all(x1[i][k] == x2[i][k] for i in (0, 1) for k in x1[i])
C.check("(FTfast) transfer-recursion engine = path-enumeration engine FT (exponents (3), (1, 4), order 2, generic data)", same)

# ---------------------------------------------------------------- (E1)
K, p, al, A1, A2, A3 = field('p,alpha,A1,A2,A3', QQ)
dl = (al + 1)/2; f2 = (p + 1)/12 - (p + 2)*al**2/8
b0 = [K(1), -p*dl, p*(p + 1)*dl**2/2 + f2, K(0)]
a, b, _ = run_ft(K, p, (1,), 3, 1, [2*K(1), 2*A1, 2*A2, 2*A3], b0)
n1 = to_natural([ex(c) for c in b[(1, (1,))]], 2*P, (1,), (1,), DEL)
s1, s2 = sp.symbols('A1 A2')
sol = sp.solve([n1[2], n1[3] - (P/2)*g(1)], [s1, s2], dict=True)
C.check("(E1) (T1) + exact j = 1 layer determine A1, A2 uniquely", len(sol) == 1)
A1v, A2v = sol[0][s1], sol[0][s2]
C.check("(E1) A1 = -p(alpha/2 + 1): A is centred at M = n + alpha/2 + 1", z(A1v + P*(AL/2 + 1)))
mu = AL/2 + 1
C.check("(E1) A2 = p(p+1)mu^2/2 + a2 with m4_diag's a2 = -(p+1)/24 + (p+1)(p+2)alpha^2/8", z(A2v - P*(P + 1)*mu**2/2 - a2l))
Kc, pc, alc = field('p,alpha', QQ)
a0l, b0l = lattice_initial(Kc, pc, alc, 2)
C.check("(E1) = shift_common.lattice_initial (used for the registered TD predictions)",
        z(ex(a0l[1])/2 - A1v) and z(ex(a0l[2])/2 - A2v))

# ---------------------------------------------------------------- (E2), (E3)
D = 4
K, p, al, a2s = field('p,alpha,a2', QQ)
dl = (al + 1)/2; f2 = (p + 1)/12 - (p + 2)*al**2/8; m_ = al/2 + 1
b0 = [K(1), -p*dl, p*(p + 1)*dl**2/2 + f2, K(0), K(0)]
a0 = [2*K(1), -2*p*m_, 2*(p*(p + 1)*m_**2/2 + a2s), K(0), K(0)]
okg = True; okz = True; ctrl = False
for j in range(2, 9):
    a, b, _ = run_ft(K, p, (j,), D, 1, a0, b0)
    n1 = to_natural([ex(c) for c in b[(1, (1,))]], (j + 1)*P, (1,), (j,), DEL)
    okz &= z(n1[2]); okg &= z(sp.cancel(n1[3]/n1[1]).subs(A2s, a2l) - g(j))
    ctrl |= z(sp.cancel(n1[3]/n1[1]).subs(A2s, 0) - g(j))
C.check("(E2) first-order layers j = 2..8: natural N^-2 = 0", okz)
C.check("(E2) first-order layers j = 2..8: g_j = A_j + B_j alpha^2 (JZC_M4 §6 / N.6(ii), exact symbolic j)", okg)
C.check("(E2) control: with a2 := 0 some g_j (j = 2..8) is reproduced", ctrl, must_fail=True)
K2, p2, al2, f2s = field('p,alpha,f2', QQ)
dl2 = (al2 + 1)/2; m2 = al2/2 + 1
a2v = -(p2 + 1)/24 + (p2 + 1)*(p2 + 2)*al2**2/8
b02 = [K2(1), -p2*dl2, p2*(p2 + 1)*dl2**2/2 + f2s, K2(0), K2(0)]
a02 = [2*K2(1), -2*p2*m2, 2*(p2*(p2 + 1)*m2**2/2 + a2v), K2(0), K2(0)]
a, b, _ = run_ft(K2, p2, (1,), D, 2, a02, b02)
n2 = to_natural([ex(c) for c in b[(1, (2,))]], 3*P, (2,), (1,), DEL)
C.check("(E3) mu_1^2 layer: N^-2 = p(3p+1)/8 (e-units) and N^-3 = 0", z(n2[2] - P*(3*P + 1)/8) and z(n2[3]))
C.check("(E3) mu_1^2 layer: N^-4 = (p^2/4) h2 (JZC_M4_proof h2, all p, alpha)", z(n2[4].subs(F2s, f2l) - P**2*h2/4))
C.check("(E3) control: with f2 := 0 the mu_1^2 N^-4 coefficient is reproduced", z(n2[4].subs(F2s, 0) - P**2*h2/4), must_fail=True)

# ---------------------------------------------------------------- (E4)
# (fixed per Rule R review A: (E4) needs both engine caches; a missing cache stops the run instead of silently skipping a check)
fh = sorted(glob.glob(os.path.join(W2C, "exact_H_*.json")))
if len(fh) != 1:
    sys.exit(f"ERROR: expected exactly one tmp/w2/exact_H_*.json (JZC_W2 H run), found {len(fh)}; run the JZC_W2 exact H engine first")
fn = fh[0]; print(f"sha256 {os.path.basename(fn)}: {sha(fn)}")
hH = sp.sympify(json.load(open(fn))['nat']['1,1'][4], locals=dict(alpha=AL, beta=BE, j=J, k=KK))
fr1 = sorted(glob.glob(os.path.join(SHC, "eng_R1_*.json")))
if len(fr1) != 1:
    sys.exit(f"ERROR: expected exactly one tmp/shift/eng_R1_*.json, found {len(fr1)}; run `shift_exact.py R1` first")
print(f"sha256 {os.path.basename(fr1[0])}: {sha(fr1[0])}")
r1 = sp.sympify(json.load(open(fr1[0]))['nat']['2,0'][4], locals=dict(alpha=AL, beta=BE, j=J))
Kh, alh = field('alpha', QQ); ph = Kh(sp.Rational(3, 2))
a0h, b0h = lattice_initial(Kh, ph, alh, D)
okh = True; okr = True; t0 = time.time()
for j in range(1, 5):
    for k in range(j, 5):
        js = (j, k) if j != k else (j,)
        a, b, _ = run_ft(Kh, ph, js, D, 2, a0h, b0h)
        if j != k:
            n = to_natural([ex(c) for c in b[(1, (1, 1))]], (j + k + 1)*sp.Rational(3, 2), (1, 1), (j, k), DEL)
        else:
            n = to_natural([2*ex(c) for c in b[(1, (2,))]], (2*j + 1)*sp.Rational(3, 2), (1, 1), (j, j), DEL)
            okr &= z(n[4]/2 - r1.subs(J, j))
        okh &= z(n[4] - hH.subs({J: j, KK: k}))
C.check("(E4) h(j, k) at p = 3/2, 1 <= j <= k <= 4: Toda = exact engine (w2_exact H)", okh)
C.check("(E4) e1^2 N^-4 at p = 3/2, j <= 4: Toda = exact engine (shift_exact R1, symbolic j)", okr)
print(f"   (E4) {time.time() - t0:.0f}s", flush=True)

# ---------------------------------------------------------------- (E5)
K5, p5, al5, f25, a25 = field('p,alpha,f2,a2', QQ)
dl5 = (al5 + 1)/2; m5 = al5/2 + 1
b05 = [K5(1), -p5*dl5, p5*(p5 + 1)*dl5**2/2 + f25, K5(0)]
a05 = [2*K5(1), -2*p5*m5, 2*(p5*(p5 + 1)*m5**2/2 + a25), K5(0)]
c0 = lambda j: j*(j*P + 2)*((j**2 + 2*j - 2)*P + 2*j - 1)/(24*(2*j - 1))
ca = lambda j: j*(j*P + 2)/((2*j - 1)*P)
cf = lambda j: ((j**2 + j - 1)*P + 2*(j - 1))/((2*j - 1)*P)
okd = True
for j in range(1, 11):
    a, b, _ = run_ft(K5, p5, (j,), 3, 1, a05, b05)
    n1 = to_natural([ex(c) for c in b[(1, (1,))]], (j + 1)*P, (1,), (j,), DEL)
    okd &= z(sp.cancel(n1[3]/n1[1]) - (c0(j) + ca(j)*A2s + cf(j)*F2s))
C.check("(E5) g_j = c0(j) + c_a(j) a2 + c_f(j) f2 for j = 1..10 (f2, a2 free symbols)", okd)
C.check("(E5) identically in symbolic j: c0 + c_a a2 + c_f f2 at the lattice f2, a2 = A_j + B_j alpha^2",
        z(c0(J) + ca(J)*a2l + cf(J)*f2l - g(J)))
print("   c0(j) =", sp.factor(c0(J)), "  c_a(j) =", sp.factor(ca(J)), "  c_f(j) =", sp.factor(cf(J)))

# ---------------------------------------------------------------- (E6)
w, L_, gam, s = sp.symbols('w lambda gam s'); y1, y2 = sp.symbols('y1 y2')
y = L_*y1 + L_**2*y2
ser = sp.expand(sp.series(-L_*s*(1 + y)**(-P)*(1 + gam*w**2*(1 + y)**-2)/P, L_, 0, 3).removeO())
so = sp.solve([sp.Eq(y1, ser.coeff(L_, 1)), sp.Eq(y2, ser.coeff(L_, 2))], [y1, y2], dict=True)[0]
Xs = sp.expand(sp.series((1 + y)**(-P)*(1 + f2l*w**2*(1 + y)**-2), L_, 0, 3).removeO()).subs(so)
c1 = sp.expand(sp.series(sp.expand(Xs.coeff(L_, 1)), w, 0, 3).removeO())
c2 = sp.expand(sp.series(sp.expand(Xs.coeff(L_, 2)), w, 0, 3).removeO())
gs = sp.solve(sp.Eq(c1.coeff(w, 2)/c1.coeff(w, 0), g(1)), gam)[0]
c2 = c2.subs(gam, gs); defect = sp.factor(c2.coeff(w, 2)/s**2 - h2)
C.check("(E6) control: the dressed-index-shift ansatz reproduces h2", z(defect), must_fail=True)
print("   (E6) index dressing gamma_1 = g_1 - (p+2) f2/p:", z(gs - (g(1) - (P + 2)*f2l/P)), "; ansatz h2 - exact h2 =", defect)

# ---------------------------------------------------------------- (E7)
t0 = time.time()
K7, p7, al7, f2_, f4_, f6_, a2_, a4_, a6_ = field('p,alpha,f2,f4,f6,a2,a4,a6', QQ)
D7 = 6; Ws = sp.Symbol('W')
def even_layer(shift, cs, Kf, pf):
    """(n/(n+shift))^p (1 + c2 X^-2 + c4 X^-4 + c6 X^-6), X = n + shift, as coefficients of n^0..n^-D7 (field elements)"""
    u = sp.Symbol('u'); sh = sp.Symbol('sh'); pp = sp.Symbol('pp'); c2_, c4_, c6_ = sp.symbols('c2_ c4_ c6_')
    e = (1 + sh*u)**(-pp)*(1 + c2_*u**2*(1 + sh*u)**-2 + c4_*u**4*(1 + sh*u)**-4 + c6_*u**6*(1 + sh*u)**-6)
    sr = sp.expand(sp.series(e, u, 0, D7 + 1).removeO())
    out = []
    for i in range(D7 + 1):
        ci = sp.Poly(sr.coeff(u, i), sh, pp, c2_, c4_, c6_)
        v = Kf(0)
        for mon, cv in ci.terms():
            v += Kf(cv)*shift**mon[0]*pf**mon[1]*cs[0]**mon[2]*cs[1]**mon[3]*cs[2]**mon[4]
        out.append(v)
    return out
dl7 = (al7 + 1)/2
b07 = even_layer(dl7, (f2_, f4_, f6_), K7, p7)
for lab, ashift, must in (("A centred at M = N + 1/2", dl7 + K7(1)/2, False), ("control: A centred at N", dl7, True)):
    a07 = [2*x for x in even_layer(ashift, (a2_, a4_, a6_), K7, p7)]
    a, b, _ = run_ft(K7, p7, (1, 2), D7, 3, a07, b07)
    odd0 = True
    for key, v in b.items():
        beta = key[1]; m = sum(beta)
        if m == 0: continue
        n = to_natural([ex(c) for c in v], (beta[0] + 2*beta[1] + 1)*P, beta, (1, 2), DEL)
        odd0 &= z(n[m + 1]) and z(n[m + 3])
    C.check(f"(E7) {lab}: all layers of exponents (1, 2), order <= 3, have zero N^(-|beta|-1) and N^(-|beta|-3) coefficients "
            f"(generic even f2, f4, f6, a2, a4, a6)", odd0, must_fail=must)
print(f"   (E7) {time.time() - t0:.0f}s", flush=True)
C.finish()
