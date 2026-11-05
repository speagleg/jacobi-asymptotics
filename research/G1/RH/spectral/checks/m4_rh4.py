"""JZC M4: the integer layer of the lattice to fourth order by the Riemann-Hilbert small-norm expansion (extends
second_order/checks/check_e2_sym.py, Plan E2, from order 2 to order KORD = 4).

Model problem exactly as E2_pgt1 (model weight z^alpha (4c - z); band factor H_n replaced by a constant, so the output is the
INTEGER layer: the zeta layer and pole terms come from H_n, E3 / SPEC). Jumps on the circles around 4c (Airy) and 0 (Bessel):
J = I + sum_k Delta_k / n^k with
  soft:  Delta_k^r = (-1/phit)^k P0 (-w)^{-s3/2} X_k (-w)^{s3/2} P0^{-1},  X_k = M^{-1}(M o C_k), C_k = [[u_k, (-1)^k u_k], [v_k, (-1)^k v_k]]
  hard:  Delta_k^0 = (2 f^{1/2})^{-k} P0 rho^{s3} s3 Xi_k s3 rho^{-s3} P0^{-1},  Xi_k = M^{-1}(M o C_k), C_k = [[(-1)^k a_k, a_k], [(-1)^k b_k, b_k]]
(u_k, v_k: DLMF 9.7.2; a_k: DLMF 10.17.1; b_k: DLMF 10.17.8, all k; for k = 1, 2 these reproduce X_1, X_2, Xi_1, Xi_2 of check_e2_sym,
asserted below). Small norm, order by order (R_out = R_in J on the circles):
  R_out^(k) = principal parts at {0, 4c} of  sum_{j=1..k} R_in^(k-j) Delta_j,   R_in^(k) = R_out^(k) - sum_{j=1..k} R_in^(k-j) Delta_j,
and R_1^(k) = sum of the residues. Extraction as E2: Q_1 = P_1 + sum_k eps^k R_1^(k), n^p b_n / c = sqrt(Q_12 Q_21)/c.
Everything is numerical (mpmath, dps 40) at given (p, alpha), as truncated Laurent series in the local variables.
Output: d_1..d_KORD (KORD = 6 by default; env KORD, series cap env SHI) of the integer layer, and f_1..f_KORD of F(N) = (N/n)^p n^p b_n/c, N = n + alpha/2 + 1/2.
Checks: d1 = -p(alpha+1)/2, d2 = E2 Thm E2.1, f1 = f3 = 0 (Conjecture S1-N), f2 = -(p+2)alpha^2/8 + (p+1)/12."""
import sys
import mpmath as mp
mp.mp.dps = 40
KORD = int(__import__("os").environ.get("KORD", "6"))
L = 44                                       # number of kept coefficients in each series


class S:
    """truncated Laurent series sum_{lo<=k<=hi} c[k-lo] t^k, valid (known) up to t^hi; hi is capped at S.HI"""
    HI = int(__import__("os").environ.get("SHI", "40"))
    def __init__(s, lo, c, hi=None):
        s.lo = lo; s.hi = S.HI if hi is None else min(hi, S.HI)
        c = list(c)[:max(s.hi - lo + 1, 0)]
        s.c = c + [mp.mpc(0)]*(s.hi - lo + 1 - len(c))
    @staticmethod
    def const(a): return S(0, [mp.mpc(a)])
    def get(s, k): i = k - s.lo; return s.c[i] if 0 <= i < len(s.c) else mp.mpc(0)
    def __add__(s, o):
        if not isinstance(o, S): o = S.const(o)
        lo = min(s.lo, o.lo); hi = min(s.hi, o.hi)
        return S(lo, [s.get(k) + o.get(k) for k in range(lo, hi + 1)], hi)
    __radd__ = __add__
    def __neg__(s): return S(s.lo, [-x for x in s.c], s.hi)
    def __sub__(s, o): return s + (-o if isinstance(o, S) else S.const(-o))
    def __rsub__(s, o): return (-s) + o
    def __mul__(s, o):
        if not isinstance(o, S): return S(s.lo, [x*o for x in s.c], s.hi)
        lo = s.lo + o.lo; hi = min(s.hi + o.lo, o.hi + s.lo, S.HI)
        out = [mp.mpc(0)]*(hi - lo + 1)
        for i, a in enumerate(s.c):
            if a == 0: continue
            for j, b in enumerate(o.c):
                k = i + j
                if k > hi - lo: break
                out[k] += a*b
        return S(lo, out, hi)
    __rmul__ = __mul__
    def shift(s, m): return S(s.lo + m, s.c, s.hi + m)
    def trim(s):
        lo = s.lo
        while lo <= s.hi and abs(s.get(lo)) < mp.mpf(10)**(-30): lo += 1
        return S(lo, [s.get(k) for k in range(lo, s.hi + 1)], s.hi)
    def inv(s):
        t = s.trim(); a0 = t.c[0]; n = t.hi - t.lo + 1
        b = [mp.mpc(0)]*n; b[0] = 1/a0
        for k in range(1, n):
            b[k] = -sum(t.c[j]*b[k-j] for j in range(1, k + 1))/a0
        return S(-t.lo, b, -t.lo + n - 1)
    def powr(s, e):
        """(series with nonzero t^0 coefficient)^e"""
        t = s.trim(); assert t.lo == 0, t.lo
        a0 = t.c[0]; n = t.hi + 1
        q = [x/a0 for x in t.c]; b = [mp.mpc(0)]*n; b[0] = mp.mpc(1)
        for k in range(1, n):     # J.C.P. Miller recurrence
            b[k] = sum(((e + 1)*j - k)*q[j]*b[k-j] for j in range(1, k + 1))/k
        return S(0, [x*a0**e for x in b], n - 1)


def Smat(m): return [[m[0][0], m[0][1]], [m[1][0], m[1][1]]]
def mmul(A, B): return [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]
def mscal(A, f): return [[A[i][j]*f for j in range(2)] for i in range(2)]
I_ = mp.mpc(0, 1)
T = [[1/mp.sqrt(2), 1/mp.sqrt(2)], [I_/mp.sqrt(2), -I_/mp.sqrt(2)]]
Ti = [[1/mp.sqrt(2), -I_/mp.sqrt(2)], [1/mp.sqrt(2), I_/mp.sqrt(2)]]
Mm = [[1/mp.sqrt(2), I_/mp.sqrt(2)], [I_/mp.sqrt(2), 1/mp.sqrt(2)]]
Mi = [[1/mp.sqrt(2), -I_/mp.sqrt(2)], [-I_/mp.sqrt(2), 1/mp.sqrt(2)]]
def had(A, B): return [[A[i][j]*B[i][j] for j in range(2)] for i in range(2)]


def airy_uv(k):
    u = mp.gamma(3*k + mp.mpf(1)/2)/(mp.mpf(54)**k*mp.factorial(k)*mp.gamma(k + mp.mpf(1)/2))
    return u, -(6*k + 1)/mp.mpf(6*k - 1)*u


def bessel_ab(k, al):
    a = mp.mpf(1); b = mp.mpf(1)
    for j in range(1, k + 1): a *= 4*al**2 - (2*j - 1)**2
    for j in range(1, k): b *= 4*al**2 - (2*j - 1)**2
    b *= 4*al**2 + 4*k**2 - 1
    return a/(mp.factorial(k)*8**k), b/(mp.factorial(k)*8**k)


def Xk(k):
    u, v = airy_uv(k); s = (-1)**k
    return mmul(Mi, had(Mm, [[u, s*u], [v, s*v]]))


def Xik(k, al):
    a, b = bessel_ab(k, al); s = (-1)**k
    return mmul(Mi, had(Mm, [[s*a, a], [s*b, b]]))


def run(p, al, c=mp.mpf(1), verbose=False, mu=None, nu=None, want_a=False):
    """al: the exponent alpha (Szego factor and natural index); nu: the Bessel order (default al; decoupled for JZC_M4 §7)"""
    nu = al if nu is None else mp.mpf(nu)
    p, al = mp.mpf(p), mp.mpf(al); ap = 1/p + mp.mpf(1)/2; sc = mp.sqrt(c)
    # ---------------- soft edge, u^2 = z - 4c ----------------
    Kt = S.HI//2 + 4                                        # enough terms of S(e) for u^{S.HI} (was the fixed L = 44)
    Scoef = [mp.mpf(0)]*Kt
    for k in range(Kt):
        for m in range(Kt - k):
            Scoef[k + m] += mp.rf(1 - ap, k)/mp.factorial(k)*mp.rf(1 + 1/p, m)/mp.factorial(m)/((k + mp.mpf(1)/2)*(k + m + mp.mpf(3)/2))
    # S(-u^2/(4c)) as a u-series
    Su = S(0, [Scoef[t//2]*(-1/(4*c))**(t//2) if t % 2 == 0 else 0 for t in range(2*Kt)])
    kp = Scoef[0]/p/(4*c)**mp.mpf(1.5)
    phit_over = Su*(1/Scoef[0])
    xs = S(2, [1/(4*c)])                                  # x = u^2/(4c)
    one = S.const(1)
    sq1 = (one + xs).powr(mp.mpf(1)/2)
    sqz = sq1*(2*sc)
    a2 = S(1, [1])*sqz.inv()                              # u / z^{1/2}
    base = sq1 + S(1, [1/(2*sc)])                          # sqrt(1+x) + u/(2 sqrt c)
    h2 = base.powr(-(2 + 2*al)); ih2 = base.powr(2 + 2*al)
    def conj_soft(X):
        Z = [[S.const(X[0][0]), ih2*X[0][1]], [h2*X[1][0], S.const(X[1][1])]]
        Y = mmul(mmul(Ti, Z), T)
        uu = S(1, [1])
        Mx = [[uu*Y[0][0], uu*a2*Y[0][1]], [sqz*Y[1][0], uu*Y[1][1]]]
        return mmul(mmul(T, Mx), Ti)
    invpo = phit_over.inv()
    Dr = {}
    for k in range(1, KORD + 1):
        Mk = conj_soft(Xk(k)); fac = S(-(3*k + 1), [1])*(invpo.powr(k) if k > 1 else invpo)*(1/kp**k)
        D = [[Mk[i][j]*fac for j in range(2)] for i in range(2)]
        # must be even in u -> Laurent in w = u^2
        Dw = []
        for i in range(2):
            row = []
            for j in range(2):
                e = D[i][j]; lo = e.lo
                odd = max([abs(e.get(t)) for t in range(lo, e.hi + 1) if t % 2 != 0] + [0])
                scale = max([abs(e.get(t)) for t in range(lo, e.hi + 1)] + [mp.mpf(1)])
                assert odd < scale*mp.mpf(10)**(-(mp.mp.dps*2)//3), ("soft Delta not even in u", k, i, j, odd)
                lo2 = (lo + (lo % 2))//2
                row.append(S(lo2, [e.get(2*t) for t in range(lo2, e.hi//2 + 1)], e.hi//2))
            Dw.append(row)
        Dr[k] = Dw
    # ---------------- hard edge, z = -v^2 ----------------
    LZ = S.HI + 4                                          # enough z-terms for the cap (was L//2 = 22, see JZC_M4 §9 note)
    zc = [mp.mpf(0)]*LZ                                    # a-series coefficients in z
    for k in range(LZ):
        zc[k] = mp.rf(mp.mpf(1)/2, k)/mp.factorial(k)/(4*c)**k/((ap + k)*(k + mp.mpf(1)/2))
    aser_z = S(0, [x*(4*c)**mp.mpf(-0.5)/(p*mp.pi) for x in zc])
    fz = (aser_z*aser_z).shift(1)*(-(mp.pi**2)/4)            # f(z) series in z
    # in v: z = -v^2
    def z_to_v(e):
        return S(2*e.lo, [e.get(t//2)*(-1)**(t//2) if t % 2 == 0 else 0 for t in range(2*e.lo, 2*e.hi + 2)], 2*e.hi + 1)
    fv = z_to_v(fz)                                         # = v^2 * g(v)
    g = fv.shift(-2)
    fh = g.powr(mp.mpf(1)/2).shift(1)                       # f^{1/2} > 0
    a2h = (S.const(4*c) + S(2, [1])).powr(mp.mpf(1)/2).shift(-1)
    rho2 = (S(1, [1/(2*sc)]) + (one + S(2, [1/(4*c)])).powr(mp.mpf(1)/2)).powr(2*(al + 1))
    irho2 = rho2.inv(); ia2h = a2h.inv()
    s3 = [[1, 0], [0, -1]]
    def conj_hard(Q):
        Zh = [[S.const(Q[0][0]), rho2*Q[0][1]], [irho2*Q[1][0], S.const(Q[1][1])]]
        Y = mmul(mmul(Ti, Zh), T)
        Mx = [[Y[0][0], a2h*Y[0][1]], [Y[1][0]*ia2h, Y[1][1]]]
        return mmul(mmul(T, Mx), Ti)
    ifh = fh.inv()
    D0 = {}
    for k in range(1, KORD + 1):
        Q = mmul(mmul(s3, Xik(k, nu)), s3)
        Mk = conj_hard(Q)
        facp = ifh
        for _ in range(k - 1): facp = facp*ifh
        facp = facp*(mp.mpf(1)/2**k)
        D = [[Mk[i][j]*facp for j in range(2)] for i in range(2)]
        Dz = []
        for i in range(2):
            row = []
            for j in range(2):
                e = D[i][j]; lo = e.lo
                odd = max([abs(e.get(t)) for t in range(lo, e.hi + 1) if t % 2 != 0] + [0])
                scale = max([abs(e.get(t)) for t in range(lo, e.hi + 1)] + [mp.mpf(1)])
                assert odd < scale*mp.mpf(10)**(-(mp.mp.dps*2)//3), ("hard Delta not even in v", k, i, j, odd)
                lo2 = (lo + (lo % 2))//2
                row.append(S(lo2, [e.get(2*t)*(-1)**t for t in range(lo2, e.hi//2 + 1)], e.hi//2))   # v^{2t} = (-z)^t
            Dz.append(row)
        D0[k] = Dz
    # ---------------- band-factor gauge (E3 Lemma E3.4): Delta_k^mu = G_mu Delta_k^mod G_mu^{-1} ----------------
    if mu:
        def Mpoly(zser):       # M_mu(z) = sum_k mu_k Q_k(z), Q_k(z) = sum_{j<k} z^{k-1-j} C(2j, j) c^j
            out = S.const(0)
            for k, m in mu.items():
                Qk = S.const(0); zp = S.const(1)
                for j in range(k - 1, -1, -1):
                    Qk = Qk + zp*(mp.binomial(2*j, j)*c**j)
                    zp = zp*zser
                out = out + Qk*m
            return out
        def gauge(zser):
            R2 = zser*(zser - 4*c); Mz = Mpoly(zser); h2 = R2*Mz*Mz*mp.mpf(0.25)
            ch = S.const(0); sh = S.const(0); hp = S.const(1)
            for m in range(0, 25):
                ch = ch + hp*(1/mp.factorial(2*m)); sh = sh + hp*(1/mp.factorial(2*m + 1)); hp = hp*h2
            Sg = sh*Mz*mp.mpf(0.5)                      # sinh(h)/R
            G = mmul(mmul(T, [[ch, -(zser - 4*c)*Sg], [-zser*Sg, ch]]), Ti)
            Gi = mmul(mmul(T, [[ch, (zser - 4*c)*Sg], [zser*Sg, ch]]), Ti)
            return G, Gi
        Gr, Gri = gauge(S(0, [4*c, 1]))                 # z = 4c + w
        G0, G0i = gauge(S(1, [1]))                      # z
        for k in Dr: Dr[k] = mmul(mmul(Gr, Dr[k]), Gri)
        for k in D0: D0[k] = mmul(mmul(G0, D0[k]), G0i)
    # ---------------- small norm ----------------
    pts = {'r': (4*c, Dr), '0': (mp.mpf(0), D0)}
    other = {'r': '0', '0': 'r'}
    def pp(e):            # principal part of a Laurent series
        assert e.hi >= -1, "truncation too shallow: principal part not determined"
        return S(e.lo, [e.get(t) for t in range(e.lo, 0)]) if e.lo < 0 else S(0, [mp.mpc(0)])
    def reexpand(ppser, frm, to):
        """sum_{m>=1} C_m (z - z_frm)^{-m}, expanded in t = z - z_to (Taylor), z_to - z_frm = d"""
        d = pts[to][0] - pts[frm][0]; NT = S.HI; out = S(0, [mp.mpc(0)]*NT, NT - 1)
        for m in range(1, -ppser.lo + 1):
            Cm = ppser.get(-m)
            if Cm == 0: continue
            # (d + t)^{-m} = d^{-m} sum_k binom(-m, k) (t/d)^k
            out = out + S(0, [Cm*mp.binomial(-m, k)*d**(-m - k) for k in range(NT)], NT - 1)
        return out
    Rin = {e: {0: [[S.const(1), S.const(0)], [S.const(0), S.const(1)]]} for e in pts}
    R1 = {}; R2 = {}
    for k in range(1, KORD + 1):
        prod = {}
        for e in pts:
            acc = [[S.const(0), S.const(0)], [S.const(0), S.const(0)]]
            for j in range(1, k + 1):
                acc = madd(acc, mmul(Rin[e][k - j], pts[e][1][j]))
            prod[e] = acc
        PP = {e: [[pp(prod[e][i][j]) for j in range(2)] for i in range(2)] for e in pts}
        R1[k] = [[PP['r'][i][j].get(-1) + PP['0'][i][j].get(-1) for j in range(2)] for i in range(2)]
        # second moment at infinity: (z - e)^{-1} = 1/z + e/z^2 + ..., (z - e)^{-2} = 1/z^2 + ...
        R2[k] = [[4*c*PP['r'][i][j].get(-1) + PP['r'][i][j].get(-2) + PP['0'][i][j].get(-2) for j in range(2)] for i in range(2)]
        for e in pts:
            o = other[e]
            Rout_e = [[PP[e][i][j] + reexpand(PP[o][i][j], o, e) for j in range(2)] for i in range(2)]
            Rin[e][k] = msub(Rout_e, prod[e])
            # R_in must be analytic at e
            for i in range(2):
                for j in range(2):
                    x = Rin[e][k][i][j]
                    bad = max([abs(x.get(t)) for t in range(x.lo, 0)] + [0])
                    scale = max([abs(y) for y in x.c] + [mp.mpf(1)])
                    assert bad < scale*mp.mpf(10)**(-(mp.mp.dps)//2), ("R_in singular", k, e, bad)
    # ---------------- extraction ----------------
    # Q1 = P1 + sum eps^k R1[k]; b = sqrt(Q12 Q21)/c as a series in eps
    Q12 = S(0, [I_*c] + [R1[k][0][1] for k in range(1, KORD + 1)])
    Q21 = S(0, [-I_*c] + [R1[k][1][0] for k in range(1, KORD + 1)])
    S.HI, hi0 = KORD, S.HI
    bb = (Q12*Q21)*(1/c**2)
    b = bb.powr(mp.mpf(1)/2)
    S.HI = hi0
    d = [mp.re(b.get(k)) for k in range(KORD + 1)]
    im = max(abs(mp.im(b.get(k))) for k in range(KORD + 1))
    if not want_a:
        return d, im
    # diagonal coefficient: n^p alpha_n = (Q2)_12/(Q1)_12 - (Q1)_22, Q2 = P2 + R1 P1 + R2 (E_pgt1 §0, Paper 2 F8),
    # P1 = [[0, ic], [-ic, 0]], P2 = [[c^2/2, 2ic^2], [-2ic^2, c^2/2]]
    S.HI, hi0 = KORD, S.HI
    ser = lambda lst: S(0, lst)
    R1s = [[ser([0] + [R1[k][i][j] for k in range(1, KORD + 1)]) for j in range(2)] for i in range(2)]
    R2s = [[ser([0] + [R2[k][i][j] for k in range(1, KORD + 1)]) for j in range(2)] for i in range(2)]
    P1m = [[S.const(0), S.const(I_*c)], [S.const(-I_*c), S.const(0)]]
    P2m = [[S.const(c**2/2), S.const(2*I_*c**2)], [S.const(-2*I_*c**2), S.const(c**2/2)]]
    Q1m = madd(P1m, R1s); Q2m = madd(madd(P2m, mmul(R1s, P1m)), R2s)
    A = Q2m[0][1]*Q1m[0][1].inv() - Q1m[1][1]
    S.HI = hi0
    aa = [mp.re(A.get(k))/(2*c) for k in range(KORD + 1)]          # n^p alpha_n/(2c) = sum aa_k n^{-k}
    return d, im, aa


def natural(d, p, al):
    """F(N) = (N/n)^p (1 + d1/n + ...), N = n + delta, in powers of 1/N"""
    delta = al/2 + mp.mpf(1)/2; p = mp.mpf(p)
    # with x = 1/N: n = N - delta, 1/n = x/(1 - delta x);  (N/n)^p = (1 - delta x)^{-p}
    S.HI, hi0 = KORD, S.HI
    x = S(1, [1]); one = S.const(1)
    inv_n = x*(one - x*delta).inv()
    tot = S.const(d[0]); pw = S.const(1)
    for k in range(1, KORD + 1):
        pw = pw*inv_n; tot = tot + pw*d[k]
    F = (one - x*delta).powr(-p)*tot
    S.HI = hi0
    return [mp.re(F.get(k)) for k in range(KORD + 1)]


def f4_closed(p, a):
    return ((p + 1)*(6*p**3 + 46*p**2 + 55*p + 3)/(1440*p*(3*p + 2)) - 5*(p + 1)*(p + 2)*a**2/(96*(3*p + 2))
            - p*(p + 2)**2*a**4/(128*(3*p + 2)))


def f6_closed(p, a):
    D = (3*p + 2)**2*(5*p + 2)
    c0 = -(p + 1)*(450*p**8 + 1590*p**7 - 316*p**6 - 23761*p**5 - 66864*p**4 - 65507*p**3 - 18220*p**2 - 1632*p - 40)/(362880*p**2*D)
    c2 = (p + 1)*(p + 2)*(90*p**6 + 270*p**5 + 664*p**4 - 165*p**3 - 1649*p**2 - 288*p + 28)/(11520*p*D)
    c4 = -(p + 1)*(p + 2)**2*(20*p**4 + 45*p**3 + 162*p**2 + 72*p + 16)/(1536*D)
    c6 = p*(p + 2)**3*(16*p**3 + 7*p**2 - 4*p - 4)/(3072*D)
    return c0 + c2*a**2 + c4*a**4 + c6*a**6


if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from spec_common import Checks
    C_ = Checks()
    # (1) the generic X_k, Xi_k reproduce check_e2_sym's k = 1, 2 matrices
    u1, v1 = mp.mpf(5)/72, -mp.mpf(7)/72; u2, v2 = mp.mpf(385)/10368, -mp.mpf(455)/10368
    X1 = [[(u1 + v1)/2, I_*(v1 - u1)/2], [I_*(v1 - u1)/2, -(u1 + v1)/2]]; X2 = [[(u2 + v2)/2, I_*(u2 - v2)/2], [-I_*(u2 - v2)/2, (u2 + v2)/2]]
    al0 = mp.mpf('0.37'); a1, b1 = (4*al0**2 - 1)/8, (4*al0**2 + 3)/8
    a2_, b2_ = (4*al0**2 - 1)*(4*al0**2 - 9)/128, (4*al0**2 - 1)*(4*al0**2 + 15)/128
    Xi1 = [[-(a1 + b1)/2, I_*(a1 - b1)/2], [I_*(a1 - b1)/2, (a1 + b1)/2]]; Xi2 = [[(a2_ + b2_)/2, I_*(a2_ - b2_)/2], [-I_*(a2_ - b2_)/2, (a2_ + b2_)/2]]
    dm = lambda A, B: float(max(abs(A[i][j] - B[i][j]) for i in range(2) for j in range(2)))
    C_.check("X_1, X_2 = check_e2_sym", max(dm(Xk(1), X1), dm(Xk(2), X2)), 0.0, 1e-30)
    C_.check("Xi_1, Xi_2 = check_e2_sym", max(dm(Xik(1, al0), Xi1), dm(Xik(2, al0), Xi2)), 0.0, 1e-30)
    # (2) points NOT used in the rational reconstruction (p in {1/2,1,3/2,2,5/2,3,...,12,1/3,2/3,3/4}; alpha in {0,1/2,1,3/2,2})
    pts = [(mp.mpf(9)/4, mp.mpf('0.3')), (mp.mpf('0.4'), mp.mpf('-0.7')), (mp.mpf(7)/5, mp.mpf('1.1')), (mp.mpf(11)/2, mp.mpf('-0.45')),
           (mp.mpf('0.8'), mp.mpf('2.6')), (mp.mpf(2), mp.mpf(-1)/2)]
    for p, al in pts:
        d, im = run(p, al); f = natural(d, p, al)
        d2 = (p + 1)*p*(al + 1)**2/8 - (p + 2)*al**2/8 + (p + 1)/12
        f2 = -(p + 2)*al**2/8 + (p + 1)/12
        lab = f"p={mp.nstr(p, 4)} al={mp.nstr(al, 3)}"
        print(f"{lab}: d = {[mp.nstr(x, 12) for x in d]};  f = {[mp.nstr(x, 12) for x in f]}")
        C_.check(f"{lab}: imaginary part", float(im), 0.0, 1e-30)
        C_.check(f"{lab}: d1 = -p(al+1)/2", float(d[1]), float(-p*(al + 1)/2), 1e-30)
        C_.check(f"{lab}: d2 = E2 Thm E2.1", float(d[2]), float(d2), 1e-28)
        C_.check(f"{lab}: f1 = 0", float(f[1]), 0.0, 1e-28)
        C_.check(f"{lab}: f2 = -(p+2)al^2/8 + (p+1)/12", float(f[2]), float(f2), 1e-28)
        C_.check(f"{lab}: f3 = 0", float(f[3]), 0.0, 1e-28)
        C_.check(f"{lab}: f4 closed form", float(f[4] - f4_closed(p, al)), 0.0, 1e-28)
        if KORD >= 6:
            C_.check(f"{lab}: f5 = 0", float(f[5]), 0.0, 1e-27)
            C_.check(f"{lab}: f6 closed form", float(f[6] - f6_closed(p, al)), 0.0, 1e-27)
    # (3) Bessel anchor (Prop N.2): F = (1 - 1/(4N^2))^{-1/2}: f4 = 3/128, f6 = 5/1024
    C_.check("Bessel f4 = 3/128", float(f4_closed(mp.mpf(2), mp.mpf(-1)/2)), 3/128, 1e-30)
    C_.check("Bessel f6 = 5/1024", float(f6_closed(mp.mpf(2), mp.mpf(-1)/2)), 5/1024, 1e-30)
    C_.finish()
