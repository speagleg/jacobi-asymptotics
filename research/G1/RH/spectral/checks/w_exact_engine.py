"""w_exact_engine.py: a COPY of m4_rh_exact2.py (sha256 2d18e259...cbc06, not modified) with two changes, marked
"w_exact change": env PVAL fixes p to a rational number (faster field Q(alpha, j, beta)); env SZOFF sets the Szego exponent
beta = alpha + SZOFF (e.g. SZOFF=-1: the Laguerre model M(alpha - 1, alpha) at p = -1). With neither set it is m4_rh_exact2.
Original docstring:
JZC M4: EXACT symbolic computation, generalised (m4_rh_exact2): dual numbers to order EO in the band-factor parameter
(env EO, default 2), and optionally a SYMBOLIC zeta index j (field Q(p, alpha, j)).
Otherwise identical to m4_rh_exact.py (the version used for m4_rh_exact_k4/k6.out and m4_zeta_exact.out), whose docstring
follows.
JZC M4: EXACT symbolic version of m4_rh4.py (order-k RH model computation), over the field Q(p, alpha)[i], c = 1.
Same formulas as m4_rh4.py (see its docstring); every input is a rational function of (p, alpha) once c = 1:
  - u_k, v_k (DLMF 9.7.2): u_k = (2k+1)(2k+3)...(6k-1)/(216^k k!), v_k = -(6k+1)/(6k-1) u_k  (rational);
  - a_k, b_k (DLMF 10.17.1, 10.17.8): polynomials in alpha;
  - the local-map series (E2 Lemma E2.4) have rational coefficients in p; pi cancels in f (f = -(pi^2/4) z a(z)^2,
    a(z) = (4c)^{-1/2}/(p pi) * sum ...), and the square roots are of series with leading coefficient 1 (or a perfect square:
    f^{1/2} ~ v/(p+2), sqrt(4 + v^2) ~ 2);
  - T, M carry 1/sqrt 2; they occur in pairs (T..T^{-1}, M^{-1}(M o C)), so we use T0 = sqrt2 T etc. and a factor 1/2 per pair.
Output: the exact rational functions d_1..d_K and f_1..f_K. Assertions (identities in p, alpha):
  d1 = -p(alpha+1)/2, d2 = E2 Thm E2.1, f1 = f3 = 0, f2 = -(p+2)alpha^2/8 + (p+1)/12, f4 = closed form (m4_rh4.f4_closed)."""
import os, sys, time
from sympy import QQ, symbols, factor, Rational, binomial, factorial
from sympy.polys.fields import field
KORD = int(os.environ.get("KORD", "4"))
PVAL = os.environ.get("PVAL")          # w_exact change 1: p fixed to a rational number (field Q(alpha, j, beta))
if PVAL is None:
    K, p, al, jj, be = field("p,alpha,j,beta", QQ)
else:
    K, al, jj, be = field("alpha,j,beta", QQ); p = K(Rational(PVAL))
DECOUPLE = os.environ.get("DECOUPLE", "0") == "1"   # Szego exponent beta independent of the Bessel order alpha (JZC_M4 §7)
SZOFF = os.environ.get("SZOFF")        # w_exact change 2: Szego exponent beta = alpha + SZOFF (a rational shift)
SZ = be if DECOUPLE else (al + K(Rational(SZOFF)) if SZOFF is not None else al)
EO = int(os.environ.get("EO", "2"))
ONE, ZERO = K(1), K(0)


class G:
    """element of K[i][eps]/(eps^{EO+1}): parts[m] = (a_m, b_m) is the coefficient a_m + i b_m of eps^m"""
    __slots__ = ("r", "i")
    def __init__(s, a, b=None, r=None, i=None):
        if r is not None: s.r, s.i = r, i; return
        a = K(a) if isinstance(a, int) else a; b = ZERO if b is None else (K(b) if isinstance(b, int) else b)
        s.r = [a] + [ZERO]*EO; s.i = [b] + [ZERO]*EO
    @staticmethod
    def eps(m, coef=None):
        r = [ZERO]*(EO + 1); i = [ZERO]*(EO + 1)
        if m <= EO: r[m] = ONE if coef is None else coef
        return G(None, r=r, i=i)
    @property
    def a(s): return s.r[0]
    @property
    def b(s): return s.i[0]
    def __add__(s, o):
        if isinstance(o, S): return NotImplemented
        o = o if isinstance(o, G) else G(o); return G(None, r=[x + y for x, y in zip(s.r, o.r)], i=[x + y for x, y in zip(s.i, o.i)])
    __radd__ = __add__
    def __sub__(s, o):
        if isinstance(o, S): return NotImplemented
        o = o if isinstance(o, G) else G(o); return G(None, r=[x - y for x, y in zip(s.r, o.r)], i=[x - y for x, y in zip(s.i, o.i)])
    def __rsub__(s, o): return G(o) - s
    def __neg__(s): return G(None, r=[-x for x in s.r], i=[-x for x in s.i])
    def __mul__(s, o):
        if isinstance(o, S): return NotImplemented
        if not isinstance(o, G): return G(None, r=[x*o for x in s.r], i=[x*o for x in s.i])
        r = [ZERO]*(EO + 1); i = [ZERO]*(EO + 1)
        for m in range(EO + 1):
            if s.r[m] == ZERO and s.i[m] == ZERO: continue
            for l in range(EO + 1 - m):
                if o.r[l] == ZERO and o.i[l] == ZERO: continue
                r[m + l] += s.r[m]*o.r[l] - s.i[m]*o.i[l]; i[m + l] += s.r[m]*o.i[l] + s.i[m]*o.r[l]
        return G(None, r=r, i=i)
    __rmul__ = __mul__
    def inv(s):
        d = s.r[0]*s.r[0] + s.i[0]*s.i[0]; x0 = G(s.r[0]/d, -s.i[0]/d)        # 1/(x0 + y) = x0^{-1} sum (-y x0^{-1})^m
        y = G(None, r=[ZERO] + s.r[1:], i=[ZERO] + s.i[1:])
        out = G(1); term = G(1); q = -(y*x0)
        for _ in range(EO): term = term*q; out = out + term
        return out*x0
    def __truediv__(s, o): return s*(o.inv() if isinstance(o, G) else G(ONE/o))
    def iszero(s): return all(x == ZERO for x in s.r) and all(x == ZERO for x in s.i)
    def part(s, m): return G(s.r[m], s.i[m])
GZ, G1, GI = G(0), G(1), G(0, 1)


class S:
    """truncated Laurent series over G, valid up to t^hi"""
    HI = int(os.environ.get("SHI", "30"))
    def __init__(s, lo, c, hi=None):
        s.lo = lo; s.hi = S.HI if hi is None else min(hi, S.HI)
        c = [x if isinstance(x, G) else G(x) for x in list(c)[:max(s.hi - lo + 1, 0)]]
        s.c = c + [GZ]*(s.hi - lo + 1 - len(c))
    @staticmethod
    def const(a): return S(0, [a if isinstance(a, G) else G(a)])
    def get(s, k): i = k - s.lo; return s.c[i] if 0 <= i < len(s.c) else GZ
    def __add__(s, o):
        if not isinstance(o, S): o = S.const(o)
        lo = min(s.lo, o.lo); hi = min(s.hi, o.hi)
        return S(lo, [s.get(k) + o.get(k) for k in range(lo, hi + 1)], hi)
    __radd__ = __add__
    def __neg__(s): return S(s.lo, [-x for x in s.c], s.hi)
    def __sub__(s, o): return s + (-o if isinstance(o, S) else S.const(-o if isinstance(o, G) else G(-o)))
    def __rsub__(s, o): return (-s) + o
    def __mul__(s, o):
        if not isinstance(o, S): o = o if isinstance(o, G) else G(o); return S(s.lo, [x*o for x in s.c], s.hi)
        lo = s.lo + o.lo; hi = min(s.hi + o.lo, o.hi + s.lo, S.HI)
        out = [GZ]*(hi - lo + 1)
        for i, a in enumerate(s.c):
            if a.iszero(): continue
            for j, b in enumerate(o.c):
                k = i + j
                if k > hi - lo: break
                if b.iszero(): continue
                out[k] = out[k] + a*b
        return S(lo, out, hi)
    __rmul__ = __mul__
    def shift(s, m): return S(s.lo + m, s.c, s.hi + m)
    def trim(s):
        lo = s.lo
        while lo <= s.hi and s.get(lo).iszero(): lo += 1
        return S(lo, [s.get(k) for k in range(lo, s.hi + 1)], s.hi)
    def inv(s):
        t = s.trim(); a0i = t.c[0].inv(); n = t.hi - t.lo + 1
        b = [GZ]*n; b[0] = a0i
        for k in range(1, n):
            acc = GZ
            for j in range(1, k + 1): acc = acc + t.c[j]*b[k - j]
            b[k] = -(acc*a0i)
        return S(-t.lo, b, -t.lo + n - 1)
    def powr1(s, e):
        """(series with t^0 coefficient exactly 1)^e, e in K"""
        t = s.trim(); assert t.lo == 0 and t.c[0].r[0] == ONE and all(x == ZERO for x in t.c[0].r[1:] + t.c[0].i)
        n = t.hi + 1; q = t.c; b = [GZ]*n; b[0] = G1
        for k in range(1, n):
            acc = GZ
            for j in range(1, k + 1): acc = acc + q[j]*b[k - j]*(((e + 1)*j - k)/K(k))
            b[k] = acc
        return S(0, b, n - 1)


def mmul(A, B): return [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]
def mscal(A, f): return [[A[i][j]*f for j in range(2)] for i in range(2)]
T0 = [[G1, G1], [GI, -GI]]; Ti0 = [[G1, -GI], [G1, GI]]          # T = T0/sqrt2, T^{-1} = Ti0/sqrt2
M0 = [[G1, GI], [GI, G1]]; Mi0 = [[G1, -GI], [-GI, G1]]          # M = M0/sqrt2, M^{-1} = Mi0/sqrt2
HALF = K(1)/2
def conjT(Z): return mscal(mmul(mmul(T0, Z), Ti0), HALF)          # T Z T^{-1}
def conjTi(Z): return mscal(mmul(mmul(Ti0, Z), T0), HALF)         # T^{-1} Z T
def had(A, B): return [[A[i][j]*B[i][j] for j in range(2)] for i in range(2)]


def airy_uv(k):
    u = Rational(1)
    for j in range(2*k + 1, 6*k, 2): u *= j
    u = u/(Rational(216)**k*factorial(k))
    return K(u), K(-Rational(6*k + 1, 6*k - 1)*u)


def bessel_ab(k):
    a = ONE; b = ONE
    for j in range(1, k + 1): a = a*(4*al**2 - (2*j - 1)**2)
    for j in range(1, k): b = b*(4*al**2 - (2*j - 1)**2)
    b = b*(4*al**2 + 4*k**2 - 1)
    d = K(int(factorial(k))*8**k)
    return a/d, b/d


def Xk(k):
    u, v = airy_uv(k); sg = (-1)**k
    return mscal(mmul(Mi0, had(M0, [[G(u), G(u*sg)], [G(v), G(v*sg)]])), HALF)


def Xik(k):
    a, b = bessel_ab(k); sg = (-1)**k
    return mscal(mmul(Mi0, had(M0, [[G(a*sg), G(a)], [G(b*sg), G(b)]])), HALF)


def rf(x, k):
    r = ONE
    for j in range(k): r = r*(x + j)
    return r


def u_to_w(e):
    odd = [t for t in range(e.lo, e.hi + 1) if t % 2 != 0 and not e.get(t).iszero()]
    assert not odd, "not even"
    lo2 = (e.lo + (e.lo % 2))//2
    return S(lo2, [e.get(2*t) for t in range(lo2, e.hi//2 + 1)], e.hi//2)


def run(verbose=True, jmu=None):
    t0 = time.time(); c = ONE; ap = 1/p + HALF
    L = S.HI + 2
    # ---------- soft edge (u^2 = z - 4c) ----------
    Sc = [ZERO]*L
    for k in range(L):
        for m in range(L - k):
            Sc[k + m] = Sc[k + m] + rf(1 - ap, k)/K(int(factorial(k)))*rf(1 + 1/p, m)/K(int(factorial(m)))/((k + HALF)*(k + m + 3*HALF))
    Su = S(0, [G(Sc[t//2]*(K(-1)/4)**(t//2)) if t % 2 == 0 else GZ for t in range(2*L)])
    kp = Sc[0]/p/8                                       # (1/p)(4c)^{-3/2} S(0)
    phit_over = Su*G(1/Sc[0])
    xs = S(2, [G(K(1)/4)]); one = S.const(1)
    sq1 = (one + xs).powr1(HALF); sqz = sq1*G(K(2))
    a2 = S(1, [G1])*sqz.inv()
    base = sq1 + S(1, [G(HALF)])
    h2 = base.powr1(-(2 + 2*SZ)); ih2 = base.powr1(2 + 2*SZ)
    def conj_soft(X):
        Z = [[S.const(X[0][0]), ih2*X[0][1]], [h2*X[1][0], S.const(X[1][1])]]
        Y = conjTi(Z); uu = S(1, [G1])
        return conjT([[uu*Y[0][0], uu*a2*Y[0][1]], [sqz*Y[1][0], uu*Y[1][1]]])
    invpo = phit_over.inv(); Dr = {}
    for k in range(1, KORD + 1):
        Mk = conj_soft(Xk(k)); fac = S(-(3*k + 1), [G1])
        for _ in range(k): fac = fac*invpo
        fac = fac*G(1/kp**k)
        Dr[k] = [[u_to_w(Mk[i][j]*fac) for j in range(2)] for i in range(2)]
    if verbose: print(f"  soft edge done ({time.time() - t0:.0f}s)", flush=True)
    # ---------- hard edge (z = -v^2) ----------
    # a-series / ((4c)^{-1/2}/(p pi)) = sum_k (1/2)_k/k! z^k/(4^k (a'+k)(k+1/2)); f = -(pi^2/4) z a^2 = -z/(16 p^2) (sum)^2
    zc = [rf(HALF, k)/K(int(factorial(k)))/K(4)**k/((ap + k)*(k + HALF)) for k in range(L)]
    sumz = S(0, [G(x) for x in zc])
    fz = (sumz*sumz).shift(1)*G(-1/(16*p**2))
    def z_to_v(e):
        return S(2*e.lo, [e.get(t//2)*G(K((-1)**(t//2))) if t % 2 == 0 else GZ for t in range(2*e.lo, 2*e.hi + 2)], 2*e.hi + 1)
    g = z_to_v(fz).shift(-2)                              # f = v^2 g, g(0) = 1/(p+2)^2
    g0 = g.get(0); assert g0.b == ZERO and g0.a == 1/(p + 2)**2
    fh = (g*G((p + 2)**2)).powr1(HALF).shift(1)*G(1/(p + 2))
    a2h = (one + S(2, [G(K(1)/4)])).powr1(HALF).shift(-1)*G(K(2))     # sqrt(4 + v^2)/v
    rho2 = (S(1, [G(HALF)]) + (one + S(2, [G(K(1)/4)])).powr1(HALF)).powr1(2*(SZ + 1))
    irho2 = rho2.inv(); ia2h = a2h.inv(); ifh = fh.inv()
    s3 = [[G1, GZ], [GZ, -G1]]
    def conj_hard(Q):
        Zh = [[S.const(Q[0][0]), rho2*Q[0][1]], [irho2*Q[1][0], S.const(Q[1][1])]]
        Y = conjTi(Zh)
        return conjT([[Y[0][0], a2h*Y[0][1]], [Y[1][0]*ia2h, Y[1][1]]])
    D0 = {}
    for k in range(1, KORD + 1):
        Mk = conj_hard(mmul(mmul(s3, Xik(k)), s3)); fac = ifh
        for _ in range(k - 1): fac = fac*ifh
        fac = fac*G(K(1)/2**k)
        D0[k] = []
        for i in range(2):
            row = []
            for j in range(2):
                e = u_to_w(Mk[i][j]*fac)                  # series in v^2 = -z
                row.append(S(e.lo, [e.get(t)*G(K((-1)**t)) for t in range(e.lo, e.hi + 1)], e.hi))
            D0[k].append(row)
    if verbose: print(f"  hard edge done ({time.time() - t0:.0f}s)", flush=True)
    # ---------- band-factor gauge (E3 Lemma E3.4) to order EO in mu_j: G = T[[ch, -(z-4c)S], [-zS, ch]]T^{-1},
    # h = R M/2, M = mu Q_j, S = sinh(h)/R; cosh h = sum (z(z-4c) M^2/4)^m/(2m)!, S = (M/2) sum (z(z-4c) M^2/4)^m/(2m+1)!.
    # Symbolic j: mu is normalised by C(2j, j), i.e. Q_j is replaced by Q_j/C(2j, j), whose Taylor data are rational in j:
    #   at 0: coeff of z^m = prod_{i<=m} (j - i)/(2(2j - 2i - 1));  at 4: coeff of w^m = j(j-1)...(j-m)/(4^{m+1} (1/2)_{m+1}).
    if jmu:
        NQ = S.HI + 2
        def Qser(at):
            if jmu == 'sym':
                cs = []
                for m in range(NQ):
                    if at == 0:
                        v = ONE
                        for i in range(m + 1): v = v*(jj - i)/(2*(2*jj - 2*i - 1))
                    else:
                        v = ONE
                        for i in range(m + 1): v = v*(jj - i)
                        v = v/(K(4)**(m + 1)*rf(HALF, m + 1))
                    cs.append(G(v))
                return S(0, cs, NQ - 1)
            zser = S(0, [G(K(4)), G1]) if at == 4 else S(1, [G1])
            out = S.const(0); zp = S.const(1)
            for i in range(jmu - 1, -1, -1):
                out = out + zp*G(K(int(binomial(2*i, i)))); zp = zp*zser
            return out
        def gauge(at):
            zser = S(0, [G(K(4)), G1]) if at == 4 else S(1, [G1])
            Mq = Qser(at)*G.eps(1); h2 = zser*(zser - 4)*Mq*Mq*G(K(1)/4)
            ch = S.const(0); sh = S.const(0); hp = S.const(1)
            for m in range(EO//2 + 1):
                ch = ch + hp*G(K(1)/int(factorial(2*m))); sh = sh + hp*G(K(1)/int(factorial(2*m + 1))); hp = hp*h2
            Sg = sh*Mq*G(HALF)
            Gm = conjT([[ch, -(zser - 4)*Sg], [-(zser*Sg), ch]]); Gi = conjT([[ch, (zser - 4)*Sg], [zser*Sg, ch]])
            return Gm, Gi
        Gr, Gri = gauge(4); G0, G0i = gauge(0)
        for k in Dr: Dr[k] = mmul(mmul(Gr, Dr[k]), Gri)
        for k in D0: D0[k] = mmul(mmul(G0, D0[k]), G0i)
    # ---------- small norm ----------
    pts = {'r': (K(4), Dr), '0': (K(0), D0)}; other = {'r': '0', '0': 'r'}
    def pp(e):
        assert e.hi >= -1, "truncation too shallow: principal part not determined"
        return S(e.lo, [e.get(t) for t in range(e.lo, 0)]) if e.lo < 0 else S.const(0)
    NT = 12
    def reexpand(ps, frm, to):
        d = pts[to][0] - pts[frm][0]; out = S(0, [GZ]*NT, NT - 1)
        for m in range(1, -ps.lo + 1):
            Cm = ps.get(-m)
            if Cm.iszero(): continue
            out = out + S(0, [Cm*G(K(int(binomial(-m, k)))*d**(-m - k)) for k in range(NT)], NT - 1)
        return out
    Rin = {e: {0: [[S.const(1), S.const(0)], [S.const(0), S.const(1)]]} for e in pts}; R1 = {}
    for k in range(1, KORD + 1):
        prod = {}
        for e in pts:
            acc = [[S.const(0), S.const(0)], [S.const(0), S.const(0)]]
            for j in range(1, k + 1): acc = madd(acc, mmul(Rin[e][k - j], pts[e][1][j]))
            prod[e] = acc
        PP = {e: [[pp(prod[e][i][j]) for j in range(2)] for i in range(2)] for e in pts}
        R1[k] = [[PP['r'][i][j].get(-1) + PP['0'][i][j].get(-1) for j in range(2)] for i in range(2)]
        for e in pts:
            o = other[e]
            Rout = [[PP[e][i][j] + reexpand(PP[o][i][j], o, e) for j in range(2)] for i in range(2)]
            Rin[e][k] = msub(Rout, prod[e])
            for i in range(2):
                for j in range(2):
                    x = Rin[e][k][i][j]
                    assert all(x.get(t).iszero() for t in range(x.lo, 0)), ("R_in singular", k, e)
        if verbose: print(f"  order {k} done ({time.time() - t0:.0f}s)", flush=True)
    # ---------- extraction: sqrt(Q12 Q21)/c, Q1 = P1 + sum eps^k R1[k], P1 = [[0, i c], [-i c, 0]] ----------
    hi0 = S.HI; S.HI = KORD
    Q12 = S(0, [GI] + [R1[k][0][1] for k in range(1, KORD + 1)]); Q21 = S(0, [-GI] + [R1[k][1][0] for k in range(1, KORD + 1)])
    b = (Q12*Q21).powr1(HALF)
    dd = [b.get(k) for k in range(KORD + 1)]
    assert all(all(y == ZERO for y in x.i) for x in dd), "imaginary part"
    d = [x.r[0] for x in dd]; e = [[x.r[m] for x in dd] for m in range(EO + 1)]
    delta = SZ/2 + HALF
    x = S(1, [G1]); inv_n = x*(one - x*G(delta)).inv()
    tot = S.const(G(d[0])); q = S.const(1)
    for k in range(1, KORD + 1): q = q*inv_n; tot = tot + q*G(d[k])
    F = (one - x*G(delta)).powr1(-p)*tot
    f = [F.get(k).a for k in range(KORD + 1)]
    gz = None
    if jmu:      # order-m response: (N/n)^{(m j + 1)p} sum_k e^{(m)}_k n^{-k}, in powers of 1/N  (m = 1..EO)
        jv = jj if jmu == 'sym' else K(jmu); gz = {}
        for m in range(1, EO + 1):
            tz = S.const(G(e[m][0])); q = S.const(1)
            for k in range(1, KORD + 1): q = q*inv_n; tz = tz + q*G(e[m][k])
            Fz = (one - x*G(delta)).powr1(-(m*jv + 1)*p)*tz
            gz[m] = [Fz.get(k).a for k in range(KORD + 1)]
    S.HI = hi0
    return (d, f, gz) if jmu else (d, f)



def _provenance(*mods):
    import hashlib, os as _os
    for m in mods:
        fn = m if isinstance(m, str) else m.__file__
        print(f"sha256 {_os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)


if __name__ == "__main__":
    _provenance(__file__)
    mode = os.environ.get("JMU", "1"); jm = 'sym' if mode == 'sym' else int(mode)
    d, f, g = run(jmu=jm)
    for m, v in g.items():
        for k, x in enumerate(v): print(f"order mu^{m}, N^-({m}jp+{k}):", factor(x.as_expr()))
