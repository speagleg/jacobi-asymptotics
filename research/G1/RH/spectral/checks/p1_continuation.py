"""JZC_P1: the Paper IV expansion continued to p = 1 (NUMERICAL against exact algebra; NOT REVIEWED).

Question (JZC_W §1.6, §5.2; Paper IV Problem 7.4(c)): at p = 1 the zeta exponents 1 + jp are integers and Theorem N.6 is not
available.  Does the natural-form expansion (1.7), with its p != 1 coefficients continued to p = 1, still describe b_n?

Prediction (registered before the comparisons below; Rule X): the two integer layers at p = 1 are the p -> 1 values of the closed
forms (F: f2, f4, f6 of m4_rh4; diagonal: a2, a4 of JZC_TODA Prop T.4), and every zeta layer is the formal Toda flow of those
integer layers (Theorem T, which is exact for any measure and any exponential tilt), computed with the engine FT of shift_common
at p = 1.  No fitted parameter enters a prediction.  Data: p1_arb.py (Arb ball arithmetic, n <= 89, 4500 bits; caches tmp/p1).
Coefficients C_k are read off by a 30-term fit of N^p b_n/c - 1 in powers of 1/N on n in [40, 89]; a comparison passes iff
max_{k<=7} |C_k(data) - C_k(pred)| <= 3*spread + 1e-24, spread = the difference between the fits on [40, 89] and [55, 89].

 (I)  transcription guards: f4, f6 at the Bessel point (2, -1/2) = 3/128, 5/1024 (m4_rh4); a2, a4 at (2, -1/2) = 1/4, 1/16
      (JZC_TODA Prop T.4, copied here from the .md); FT at p = 1 reproduces g_j = A_j + B_j alpha^2 (j <= 6, copied from
      shift_dressing.py) and h2 of Theorem 4.3(ii).
 (B)  base (all t_j = 0, p = 1, s = 3/2): C_k = f_k (k <= 7), odd k = 0; diagonal (M/n)^p A = 1 + a2 M^-2 + a4 M^-4, odd = 0.
      f8 and a6 at (1, -1/2) are printed (NUMERICAL; no closed form at hand).
 (T)  every time-controlled tilt (single times t_j, j <= 6; cross times (t1, t2)): C_k, k <= 7, against the FT prediction.
 (H)  pure Hurwitz lattices sum (k+d)^{-s} delta_{1/(k+d)}, 11 shifts at alpha = -1/2 and two at alpha = 1/2, 3/2: C_k, k <= 7,
      against FT with the times t_j = -2 zeta(-j, d)/j in the natural index N = n + alpha/2 - zeta(0, d) (Theorem 6.1's index
      transfer, continued to p = 1).
 (C)  Tricomi-Carlitz on y = x^2 (exact b_n; mass tilt B_j = zeta(-j, a)/j, so t_j = -zeta(-j, a)/j): the exact expansion,
      identically in a, against the FT prediction, k <= 6.
 (P2) control at p = 2 (s = 3, alpha = 0): the t_2 layer has lead -p W(2) and dressing g_2 = A_2(2) = 11/4.
 Controls (must fail):
  - the A_j transcription j*(numerator)/(24(2j-1)p) at N^-5 of the d = 3/10 lattice;
  - the power (p+1+S)^{m-1} in place of the Pochhammer symbol for eps_1^3 at N^-6 of the t1 = 1 tilt;
  - the natural index shifted by 1/4 (base C_1 = 0);
  - FT with a2 := 0 against the t2 = 1/4 tilt."""
import os, sys, json, glob, time
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
from m4_rh4 import f4_closed, f6_closed
from sympy import QQ
from sympy.polys.fields import field
P1C = os.path.join(ROOT, 'tmp', 'p1')
provenance(__file__, os.path.join(HERE, 'shift_common.py'), os.path.join(HERE, 'm4_rh4.py'), os.path.join(HERE, 'p1_arb.py'))
mp.mp.dps = 150
C = Checks()
R = sp.Rational
TOL = mp.mpf(10)**-22
KMAX = 7


# ---------------------------------------------------------------- closed forms (copied, not retyped from the PDF)
# shift_dressing.py, lines gA, gB, h2 (string-identical except for the symbol names):
def gA(j, P): return (j**2*(j**2 + 2*j - 2)*P**3 + 2*(j + 1)*(2*j**2 - 1)*P**2 + (5*j**2 + 2*j - 6)*P + 2*(j - 2))/(24*(2*j - 1)*P)
def gB(j, P): return (P + 2)*(j**2*P**2 + (j + 1)*P + 2)/(8*(2*j - 1)*P)
def g(j, P, AL): return gA(j, P) + gB(j, P)*AL**2
def h2(P, AL): return (P + 1)*(P + 2)*(3*P**2 + 2*P + 1)/(8*P**2) + (P + 2)*(2*P**3 - P**2 - 7*P - 6)*AL**2/(16*P**2)
def f2(P, AL): return (P + 1)/12 - (P + 2)*AL**2/8
# JZC_TODA.md Prop T.4 (a2) and §7.2 / line "M^-4 = a4" (a4):
def a2(P, NU): return -(P + 1)/24 + (P + 1)*(P + 2)*NU**2/8
def a4(P, NU): return (P + 1)*(P + 3)*(45*P**2*(P + 2)**2*NU**4 + 30*P*(P**2 + 6*P + 8)*NU**2 - 21*P**2 - 38*P + 4)/(5760*P*(3*P + 2))
def W(j, c): return sp.binomial(2*j, j)*c**j


class FTfast(FT):
    """copy of shift_dressing.FTfast (not modified): (J^j)_{n,n+r} by the transfer recursion."""
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


# ---------------------------------------------------------------- (I) transcription guards
Pb, ALb = R(2), R(-1, 2)
C.check("(I) f4, f6 (m4_rh4) at the Bessel point (2, -1/2) = 3/128, 5/1024",
        sp.nsimplify(f4_closed(Pb, ALb)) == R(3, 128) and sp.nsimplify(f6_closed(Pb, ALb)) == R(5, 1024))
C.check("(I) a2, a4 (JZC_TODA Prop T.4) at the Bessel point (2, -1/2) = 1/4, 1/16", a2(Pb, ALb) == R(1, 4) and a4(Pb, ALb) == R(1, 16))


# ---------------------------------------------------------------- FT at given (p, alpha): natural-form layers
def integer_layers(p, al, D, K, a2zero=False):
    """(alpha_n, b_n) at t = 0 in FT form (c = 1, n^-p frames): B = (n/N)^p F(N), A = (n/M)^p (1 + a2 M^-2 + a4 M^-4),
    N = n + dl, M = N + 1/2, dl = (alpha + 1)/2 (lattice, Z(0) = -1/2)."""
    w = sp.Symbol('w'); dl = (al + 1)/2
    fk = {2: f2(p, al), 4: f4_closed(p, al), 6: f6_closed(p, al)}
    ak = {2: 0 if a2zero else a2(p, al), 4: a4(p, al)}
    Bn = sp.series((1 + dl*w)**(-p)*(1 + sum(v*(w/(1 + dl*w))**k for k, v in fk.items())), w, 0, D + 1).removeO()
    An = sp.series((1 + (dl + R(1, 2))*w)**(-p)*(1 + sum(v*(w/(1 + (dl + R(1, 2))*w))**k for k, v in ak.items())), w, 0, D + 1).removeO()
    return [K(2*An.coeff(w, i)) for i in range(D + 1)], [K(Bn.coeff(w, i)) for i in range(D + 1)], fk, dl


def ft_layers(p, al, js, M, D, a2zero=False):
    K, _z = field('z', QQ)
    a0, b0, fk, dl = integer_layers(p, al, D, K, a2zero)
    t0 = time.time()
    _, B_, _ = FTfast(K, K(p), js, D, M).flow(a0, b0, check_commute=False)
    ex = lambda c: sp.sympify(str(c.as_expr()))
    nat = {}
    for (kp, beta), v in B_.items():
        if sum(beta) == 0: continue
        sig = (sum(b*j for b, j in zip(beta, js)) + 1)*p
        nat[beta] = to_natural([ex(c) for c in v], sig, beta, js, dl)
    print(f"   FT p={p} alpha={al} js={js} M={M} D={D}: {len(nat)} layers ({time.time() - t0:.0f}s)", flush=True)
    return nat, fk


def predict(nat, fk, js, p, c, times, kmax=KMAX):
    """C_k (k <= kmax) of N^p b_n/c - 1: integer layer + sum_beta nat_beta[i] prod_a (-t_a C(2j_a, j_a) c^j_a)^beta_a at
    N^-(i + p sum beta_a j_a).  times: dict j -> value (sympy or mpf)."""
    out = [0]*(kmax + 1)
    for k, v in fk.items():
        if k <= kmax: out[k] += v
    for beta, v in nat.items():
        S = p*sum(b*j for b, j in zip(beta, js))
        mono = 1
        for b, j in zip(beta, js):
            if b: mono *= (-times.get(j, 0)*sp.binomial(2*j, j)*c**j)**b
        if mono == 0: continue
        for i, cf in enumerate(v):
            k = i + S
            if k <= kmax: out[int(k)] += cf*mono
    return out


# ---------------------------------------------------------------- data access and fits
def load(tag):
    D = json.load(open(os.path.join(P1C, tag.replace('/', '_') + '.json')))
    return D['cfg'], [mp.mpf(x) for x in D['b2']], [mp.mpf(x) for x in D['alpha']]


def fit(vals, off, kind='b', p=1, c=mp.mpf(1)/2, K=30, windows=((40, 89), (55, 89))):
    """coefficients C_1..C_K of X - 1 in powers of 1/X0, X = N^p b_n/c (kind b, X0 = N = n + off) or M^p alpha_n/(2c)
    (kind a, X0 = M = n + off); returns (C, spread)."""
    res = []
    for lo, hi in windows:
        pts = [int(round(lo + (hi - lo)*i/(K - 1))) for i in range(K)]; Ns = [n + off for n in pts]
        A = mp.matrix([[N**(-k) for k in range(1, K + 1)] for N in Ns])
        if kind == 'b': y = mp.matrix([N**p*mp.sqrt(vals[n])/c - 1 for n, N in zip(pts, Ns)])
        else: y = mp.matrix([N**p*vals[n]/(2*c) - 1 for n, N in zip(pts, Ns)])
        res.append(mp.lu_solve(A, y))
    Cf = [mp.mpf(0)] + [res[0][k] for k in range(K)]
    return Cf, max(abs(res[0][k] - res[1][k]) for k in range(KMAX))


def mpv(x): return mp.mpf(sp.Rational(x).p)/mp.mpf(sp.Rational(x).q) if isinstance(x, (int, sp.Rational, sp.Integer)) else mp.mpf(str(sp.N(x, 60)))


def compare(label, Cd, Cp, spread=0, kmax=KMAX, quiet=False):
    """pass iff max_k |C_k(data) - C_k(pred)| <= 3*spread + 1e-24 (spread = the two-window fit spread of that dataset: the
    comparison is fit-limited, and a model error would not track the spread)."""
    worst = max(abs(Cd[k] - mpv(Cp[k])) for k in range(1, kmax + 1))
    tol = 3*spread + mp.mpf(10)**-24
    if not quiet: print(f"   {label}: max_k<={kmax} |C_k(data) - C_k(pred)| = {mp.nstr(worst, 3)} (tol {mp.nstr(tol, 2)})", flush=True)
    return worst <= tol


# ---------------------------------------------------------------- FT runs
def eps_norm(beta, js, p=1): return sp.Mul(*[(R(p*j, 2))**b for b, j in zip(beta, js)])
P1, ALm = R(1), R(-1, 2); c1 = R(1, 2)
JS = (1, 2, 3, 4, 5, 6)
nat1, fk1 = ft_layers(P1, ALm, JS, 3, KMAX)

okg = all(sp.simplify(nat1[tuple(1 if t == j else 0 for t in JS)][3]/nat1[tuple(1 if t == j else 0 for t in JS)][1] - g(j, P1, ALm)) == 0
          for j in JS)
C.check("(I) FT at p = 1: first-order layers have dressing g_j(1, -1/2) = A_j + B_j alpha^2 (j = 1..6)", okg)
C.check("(I) FT at p = 1: the eps1^2 layer is N^-2-2p [(3p+1)/(2p) + h2 N^-2] in eps-units (Theorem 4.3(ii)), h2 = h2(1, -1/2)",
        nat1[(2, 0, 0, 0, 0, 0)][2]/eps_norm((2, 0, 0, 0, 0, 0), JS) == 2 and
        sp.simplify(nat1[(2, 0, 0, 0, 0, 0)][4]/eps_norm((2, 0, 0, 0, 0, 0), JS) - h2(P1, ALm)) == 0)

for beta, lab in (((0, 1, 0, 0, 0, 0), 'eps2'), ((1, 1, 0, 0, 0, 0), 'eps1 eps2'), ((3, 0, 0, 0, 0, 0), 'eps1^3'),
                  ((2, 1, 0, 0, 0, 0), 'eps1^2 eps2'), ((1, 0, 1, 0, 0, 0), 'eps1 eps3')):
    v = [x/eps_norm(beta, JS) for x in nat1[beta]]
    print(f"   FT(p = 1, alpha = -1/2) layer {lab} in eps-units, coefficients of N^-(i + S), i = 0..{KMAX}: {v}", flush=True)
C.check("(I) FT at p = 1: eps1^3 lead = (p+1+S)_2/(3! p^2) = 5 (Catalan C_3) and eps1^2 eps2 lead = (6)_2/2! = 21",
        nat1[(3, 0, 0, 0, 0, 0)][3]/eps_norm((3, 0, 0, 0, 0, 0), JS) == 5 and nat1[(2, 1, 0, 0, 0, 0)][3]/eps_norm((2, 1, 0, 0, 0, 0), JS) == 21)

# ---------------------------------------------------------------- (B) base
cfg, b2, al_ = load('tilt_p1_base')
off = mp.mpf(1)/4                                     # N = n + alpha/2 - Z(0) = n - 1/4 + 1/2
Cb, spb = fit(b2, off)
print(f"   base window spread {mp.nstr(spb, 3)}; f8(1, -1/2) [NUMERICAL] = {mp.nstr(Cb[8], 25)}", flush=True)
C.check("(B) base: C_k = f_k (f2, f4, f6 continued to p = 1), C_odd = 0, k <= 7", compare("base", Cb, predict({}, fk1, JS, 1, c1, {}), spb))
Ca, spa = fit(al_, off + mp.mpf(1)/2, kind='a')
print(f"   diagonal: a6(1, -1/2) [NUMERICAL] = {mp.nstr(Ca[6], 25)}", flush=True)
C.check("(B) diagonal: (M/n)A = 1 + a2 M^-2 + a4 M^-4 + O(M^-6), a2 = 5/48, a4 = 53/2304, odd = 0 (k <= 5)",
        max(abs(Ca[1]), abs(Ca[2] - mpv(a2(P1, ALm))), abs(Ca[3]), abs(Ca[4] - mpv(a4(P1, ALm))), abs(Ca[5])) < TOL)
Cbs, _ = fit(b2, off + mp.mpf(1)/4)
C.check("(B) control: natural index shifted by 1/4 still gives C_1 = 0", abs(Cbs[1]) < TOL, must_fail=True)

# ---------------------------------------------------------------- (T) tilts
tags = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(P1C, 'tilt_p1_t*.json')))
okT = True; nT = 0; Cdata = {}; Spread = {}
for tag in tags:
    cfg, b2, _ = load(tag)
    times = {int(k): R(v) for k, v in cfg['t'].items()}
    Cd, sp_ = fit(b2, off); Cdata[tag] = Cd
    Spread[tag] = sp_
    okT &= compare(f"{tag} (spread {mp.nstr(sp_, 2)})", Cd, predict(nat1, fk1, JS, 1, c1, times), sp_); nT += 1
C.check(f"(T) {nT} time-controlled tilts at p = 1: C_k (k <= 7) = FT(p = 1) prediction", okT and nT >= 30)

# control: power instead of Pochhammer for eps_1^3 (t1 = 1 tilt, N^-6)
Cd = Cdata['tilt_p1_t1=1']
e1 = -1*sp.binomial(2, 1)*c1                          # e-unit of t1 = 1
lead3 = nat1[(3, 0, 0, 0, 0, 0)][3]
pw = lead3*(1 + 1 + 3)**2/poch(1 + 1 + 3, 2)          # (p+1+S)^2 in place of (p+1+S)_2, S = 3
Cp = predict(nat1, fk1, JS, 1, c1, {1: R(1)}); Cp[6] += (pw - lead3)*e1**3
C.check("(T) control: (p+1+S)^{m-1} in place of the Pochhammer symbol for eps_1^3 (t1 = 1, N^-6)",
        compare("power-law control", Cd, Cp, Spread['tilt_p1_t1=1'], quiet=True),
        must_fail=True)
nat0, _ = ft_layers(P1, ALm, (2,), 1, KMAX, a2zero=True)
C.check("(T) control: FT with a2 := 0 reproduces the t2 = 1/4 tilt", compare("a2 := 0 control", Cdata['tilt_p1_t2=1_4'],
        predict(nat0, fk1, (2,), 1, c1, {2: R(1, 4)}), Spread['tilt_p1_t2=1_4'], quiet=True), must_fail=True)

# ---------------------------------------------------------------- (H) pure Hurwitz lattices
natA = {R(-1, 2): (nat1, fk1)}
for al in (R(1, 2), R(3, 2)): natA[al] = ft_layers(P1, al, JS, 3, KMAX)
okH = True; nH = 0
for fn in sorted(glob.glob(os.path.join(P1C, 'hur_*.json'))):
    tag = os.path.basename(fn)[:-5]; cfg, b2, _ = load(tag)
    d, s = R(cfg['d']), R(cfg['s']); al = s - 2
    nat, fk = natA[al]
    times = {j: -2*(-sp.bernoulli(j + 1, d)/(j + 1))/j for j in JS}     # zeta(-j, d) = -B_{j+1}(d)/(j+1)
    offH = mpv(al/2 - (R(1, 2) - d))                    # N = n + alpha/2 - zeta(0, d)
    Cd, sp_ = fit(b2, offH)
    okH &= compare(f"{tag} (alpha = {al}, spread {mp.nstr(sp_, 2)})", Cd, predict(nat, fk, JS, 1, c1, times), sp_); nH += 1
C.check(f"(H) {nH} pure Hurwitz lattices at p = 1 (alpha = -1/2, 1/2, 3/2): C_k (k <= 7) = FT(p = 1) with t_j = -2 zeta(-j, d)/j",
        okH and nH >= 15)
# control: the A_j transcription j*(numerator) (d = 3/10, N^-5)
cfg, b2, _ = load('hur_s3/2_d3/10'); d = R(3, 10)
Cd, spd = fit(b2, mpv(ALm/2 - (R(1, 2) - d)))
times = {j: 2*sp.bernoulli(j + 1, d)/(j*(j + 1)) for j in JS}
Cp = predict(nat1, fk1, JS, 1, c1, times)
gA_bad = lambda j, P: j*((j**2 + 2*j - 2)*P**3 + 2*(j + 1)*(2*j**2 - 1)*P**2 + (5*j**2 + 2*j - 6)*P + 2*(j - 2))/(24*(2*j - 1)*P)
eps2 = W(2, c1)*(-sp.bernoulli(3, d)/3)
Cp[5] += eps2*(gA_bad(2, P1) - gA(2, P1))
C.check("(H) control: the transcription A_j = j*(numerator)/(24(2j-1)p) at N^-5 (d = 3/10)", compare("A_j control", Cd, Cp, spd, quiet=True),
        must_fail=True)

# ---------------------------------------------------------------- (C) Carlitz, exact in a
a, u = sp.symbols('a u')
n_ = 1/u - a + R(3, 4)
Rc = 2*n_*sp.sqrt(2*n_*(2*n_ - 1))/((2*n_ + a - 1)*sp.sqrt((2*n_ + a - 2)*(2*n_ + a)))
ser = sp.expand(sp.series(Rc*(1/u)/n_, u, 0, 7).removeO())
timesC = {j: sp.bernoulli(j + 1, a)/(j*(j + 1)) for j in JS}            # t_j = -zeta(-j, a)/j
CpC = predict(nat1, fk1, JS, 1, c1, timesC, kmax=6)
okC = all(sp.expand(ser.coeff(u, k) - (CpC[k] if k else 0)) == 0 for k in range(1, 7))
C.check("(C) Tricomi-Carlitz: exact expansion = FT(p = 1) prediction, identically in a, through N^-6", okC)

# ---------------------------------------------------------------- (P2) p = 2 control
c2 = mp.pi**2/16
cfgp, b2p, _ = load('tilt_p2_t2=1/4'); cfgm, b2m, _ = load('tilt_p2_t2=-1/4')
offp = mp.mpf(1)/2                                      # alpha = 0, Z(0) = -1/2
Cp_, _ = fit(b2p, offp, p=2, c=c2); Cm_, _ = fit(b2m, offp, p=2, c=c2)
dlin = [(Cp_[k] - Cm_[k])/(mp.mpf(1)/2) for k in range(9)]               # d/dt2
lead = -2*6*c2**2
print(f"   p = 2: N^-5 coefficient of d/dt2 = {mp.nstr(dlin[5], 20)} (pred {mp.nstr(lead, 20)}); g2 = {mp.nstr(dlin[7]/dlin[5], 25)}",
      flush=True)
C.check("(P2) p = 2, s = 3: the t2 layer has lead -pW(2) and g2 = A2(2) + B2(2)*0 = 11/4",
        abs(dlin[5] - lead) < TOL and abs(dlin[7]/dlin[5] - mpv(g(2, R(2), R(0)))) < TOL and g(2, R(2), R(0)) == R(11, 4))
C.finish()
