"""JZC M4: EXACT symbolic version of m4_rh4.py (order-k RH model computation), over the field Q(p, alpha)[i], c = 1.
Same formulas as m4_rh4.py (see its docstring); every input is a rational function of (p, alpha) once c = 1:
  - u_k, v_k (DLMF 9.7.2): u_k = (2k+1)(2k+3)...(6k-1)/(216^k k!), v_k = -(6k+1)/(6k-1) u_k  (rational);
  - a_k, b_k (DLMF 10.17.1, 10.17.8): polynomials in alpha;
  - the local-map series (E2 Lemma E2.4) have rational coefficients in p; pi cancels in f (f = -(pi^2/4) z a(z)^2,
    a(z) = (4c)^{-1/2}/(p pi) * sum ...), and the square roots are of series with leading coefficient 1 (or a perfect square:
    f^{1/2} ~ v/(p+2), sqrt(4 + v^2) ~ 2);
  - T, M carry 1/sqrt 2; they occur in pairs (T..T^{-1}, M^{-1}(M o C)), so we use T0 = sqrt2 T etc. and a factor 1/2 per pair.
Output: the exact rational functions d_1..d_K and f_1..f_K. Assertions (identities in p, alpha):
  d1 = -p(alpha+1)/2, d2 = E2 Thm E2.1, f1 = f3 = 0, f2 = -(p+2)alpha^2/8 + (p+1)/12, f4 = closed form (m4_rh4.f4_closed);
  for KORD >= 6 also f5 = 0 and f6 = closed form (m4_rh4.f6_closed). Also asserted: the DLMF coefficient identities b_k =
  a_k + (k - 1/2) a_{k-1} (10.17.8 vs term-wise differentiation of 10.40.2) and the 9.7.2 recurrence, k <= 8.
c-normalisation: the integer layer is c-free (all model inputs depend on z/c only); the zeta response is not -- mu_j enters
only through the combination c^j mu_j (Q_j(z) = sum_i C(2i,i) c^i z^{j-1-i} is homogeneous of degree j-1 in (z, c))."""
import os, sys, time
from sympy import QQ, symbols, factor, Rational, binomial, factorial
from sympy.polys.fields import field
KORD = int(os.environ.get("KORD", "4"))
K, p, al = field("p,alpha", QQ)
ONE, ZERO = K(1), K(0)


class G:
    """dual Gaussian element (a + b i) + eps (da + db i) over K, eps^2 = 0 (eps tracks first order in mu)"""
    __slots__ = ("a", "b", "da", "db")
    def __init__(s, a, b=None, da=None, db=None):
        s.a = K(a) if isinstance(a, int) else a; s.b = ZERO if b is None else (K(b) if isinstance(b, int) else b)
        s.da = ZERO if da is None else da; s.db = ZERO if db is None else db
    def __add__(s, o):
        if isinstance(o, S): return NotImplemented
        o = o if isinstance(o, G) else G(o); return G(s.a + o.a, s.b + o.b, s.da + o.da, s.db + o.db)
    __radd__ = __add__
    def __sub__(s, o):
        if isinstance(o, S): return NotImplemented
        o = o if isinstance(o, G) else G(o); return G(s.a - o.a, s.b - o.b, s.da - o.da, s.db - o.db)
    def __rsub__(s, o): return G(o) - s
    def __neg__(s): return G(-s.a, -s.b, -s.da, -s.db)
    def __mul__(s, o):
        if isinstance(o, S): return NotImplemented
        if not isinstance(o, G): return G(s.a*o, s.b*o, s.da*o, s.db*o)
        a = s.a*o.a - s.b*o.b; b = s.a*o.b + s.b*o.a
        if s.da == ZERO and s.db == ZERO and o.da == ZERO and o.db == ZERO: return G(a, b)
        da = s.a*o.da - s.b*o.db + s.da*o.a - s.db*o.b; db = s.a*o.db + s.b*o.da + s.da*o.b + s.db*o.a
        return G(a, b, da, db)
    __rmul__ = __mul__
    def inv(s):
        d = s.a*s.a + s.b*s.b; ia, ib = s.a/d, -s.b/d
        if s.da == ZERO and s.db == ZERO: return G(ia, ib)
        # 1/(x + eps y) = 1/x - eps y/x^2
        y2 = G(ia, ib)*G(ia, ib)*G(s.da, s.db)
        return G(ia, ib, -y2.a, -y2.b)
    def __truediv__(s, o): return s*(o.inv() if isinstance(o, G) else G(ONE/o))
    def iszero(s): return s.a == ZERO and s.b == ZERO and s.da == ZERO and s.db == ZERO
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
        t = s.trim(); assert t.lo == 0 and t.c[0].a == ONE and t.c[0].b == ZERO and t.c[0].da == ZERO and t.c[0].db == ZERO
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
    h2 = base.powr1(-(2 + 2*al)); ih2 = base.powr1(2 + 2*al)
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
    rho2 = (S(1, [G(HALF)]) + (one + S(2, [G(K(1)/4)])).powr1(HALF)).powr1(2*(al + 1))
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
    # ---------- linear band-factor gauge (E3 Lemma E3.4, first order in mu_j): Delta -> Delta + eps [Gc, Delta] ----------
    if jmu:
        def Qj(zser):
            out = S.const(0); zp = S.const(1)
            for i in range(jmu - 1, -1, -1):
                out = out + zp*G(K(int(binomial(2*i, i)))); zp = zp*zser
            return out
        def gen(zser):     # T [[0, -(z-4c) Q/2], [-z Q/2, 0]] T^{-1}, times eps
            Q = Qj(zser); E = G(ZERO, ZERO, -HALF, ZERO)
            return conjT([[S.const(0), (zser - 4)*Q*E], [zser*Q*E, S.const(0)]])
        Gr = gen(S(0, [G(K(4)), G1])); G0 = gen(S(1, [G1]))
        for k in Dr: Dr[k] = madd(Dr[k], msub(mmul(Gr, Dr[k]), mmul(Dr[k], Gr)))
        for k in D0: D0[k] = madd(D0[k], msub(mmul(G0, D0[k]), mmul(D0[k], G0)))
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
    assert all(x.b == ZERO and x.db == ZERO for x in dd), "imaginary part"
    d = [x.a for x in dd]; e = [x.da for x in dd]
    delta = al/2 + HALF
    x = S(1, [G1]); inv_n = x*(one - x*G(delta)).inv()
    tot = S.const(G(d[0])); q = S.const(1)
    for k in range(1, KORD + 1): q = q*inv_n; tot = tot + q*G(d[k])
    F = (one - x*G(delta)).powr1(-p)*tot
    f = [F.get(k).a for k in range(KORD + 1)]
    gz = None
    if jmu:      # zeta response: (N/n)^{(j+1)p} sum_k e_k n^{-k}, in powers of 1/N
        tz = S.const(G(e[0])); q = S.const(1)
        for k in range(1, KORD + 1): q = q*inv_n; tz = tz + q*G(e[k])
        Fz = (one - x*G(delta)).powr1(-(jmu + 1)*p)*tz
        gz = [Fz.get(k).a for k in range(KORD + 1)]
    S.HI = hi0
    return (d, f, gz) if jmu else (d, f)



def _provenance(*mods):
    import hashlib, os as _os
    for m in mods:
        fn = m if isinstance(m, str) else m.__file__
        print(f"sha256 {_os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)


if __name__ == "__main__":
    _provenance(__file__)
    # DLMF inputs (general k): b_k from 10.40.2 by termwise differentiation: b_k = a_k + (k - 1/2) a_{k-1};
    # u_k recurrence and v_k as quoted from DLMF 9.7.2
    for k in range(1, 9):
        ak, bk = bessel_ab(k); ak1 = bessel_ab(k - 1)[0] if k > 1 else ONE
        assert bk == ak + (k - HALF)*ak1, ("b_k", k)
        if k > 1:
            uk, vk = airy_uv(k); uk1 = airy_uv(k - 1)[0]
            assert uk == K(Rational((6*k - 5)*(6*k - 3)*(6*k - 1), (2*k - 1)*216*k))*uk1 and vk == K(Rational(6*k + 1, 1 - 6*k))*uk
    print("DLMF coefficient identities (k <= 8): b_k = a_k + (k-1/2) a_{k-1}; u_k recurrence; v_k = (6k+1)/(1-6k) u_k")
    d, f = run()
    E2 = (p + 1)*p*(al + 1)**2/8 - (p + 2)*al**2/8 + (p + 1)/12
    f4c = ((p + 1)*(6*p**3 + 46*p**2 + 55*p + 3)/(1440*p*(3*p + 2)) - 5*(p + 1)*(p + 2)*al**2/(96*(3*p + 2))
           - p*(p + 2)**2*al**4/(128*(3*p + 2)))
    ok = True
    for lab, val in (("d1 + p(alpha+1)/2", d[1] + p*(al + 1)/2), ("d2 - E2", d[2] - E2), ("f1", f[1]),
                     ("f2 - (-(p+2)alpha^2/8 + (p+1)/12)", f[2] + (p + 2)*al**2/8 - (p + 1)/12)) + \
                    ((("f3", f[3]), ("f4 - closed form", f[4] - f4c)) if KORD >= 4 else ()):
        z = (val == ZERO); ok &= z
        print(f"{lab} == 0 identically: {z}")
    if KORD >= 6:
        D = (3*p + 2)**2*(5*p + 2)
        f6c = (-(p + 1)*(450*p**8 + 1590*p**7 - 316*p**6 - 23761*p**5 - 66864*p**4 - 65507*p**3 - 18220*p**2 - 1632*p - 40)/(362880*p**2*D)
               + (p + 1)*(p + 2)*(90*p**6 + 270*p**5 + 664*p**4 - 165*p**3 - 1649*p**2 - 288*p + 28)*al**2/(11520*p*D)
               - (p + 1)*(p + 2)**2*(20*p**4 + 45*p**3 + 162*p**2 + 72*p + 16)*al**4/(1536*D)
               + p*(p + 2)**3*(16*p**3 + 7*p**2 - 4*p - 4)*al**6/(3072*D))
        for lab, val in (("f5", f[5]), ("f6 - closed form", f[6] - f6c)):
            z = (val == ZERO); ok &= z; print(f"{lab} == 0 identically: {z}")
    for k in range(1, min(KORD, 4) + 1): print(f"f{k} =", factor(f[k].as_expr()))
    print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
    assert ok
