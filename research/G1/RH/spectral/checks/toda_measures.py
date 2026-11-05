"""JZC_TODA (4a): EXACT check of Lemma T.1 (the Toda hierarchy for exponential tilts) on finite truncations of the actual
discrete measures, with controls that must fail.  Exact rational arithmetic (fractions.Fraction); nothing numerical.

Measure: mu = sum_{k<=M} w_k delta_{x_k} (M atoms, rational).  Tilt: mu_tau = exp(sum_a tau_a x^{j_a}) mu.  Everything is a
truncated multivariate power series in tau (total degree <= R) with rational coefficients: the moments are
    m_i(tau) = sum_gamma tau^gamma/gamma! * sum_k w_k x_k^{i + gamma.j}            (exact; the exponential is expanded),
the monic OPs pi_n, h_n = <pi_n, pi_n>, a_n = <x pi_n, pi_n>/h_n, b_n^2 = h_n/h_{n-1} come from the Stieltjes procedure in this
series ring (n = 0..M-1; h_n has a nonzero constant term because the M nodes are distinct), and L is the M x M monic Jacobi matrix
L_{nn} = a_n, L_{n,n+1} = 1, L_{n+1,n} = b_{n+1}^2 (similar to the orthonormal J: (J^j)_{nn} = (L^j)_{nn},
b_{n+1}(J^j)_{n+1,n} = (L^j)_{n+1,n}, sqrt(h_n/h_m)(J^j)_{nm} = (L^j)_{nm}; JZC_TODA §2).
Identities of Lemma T.1, as power series in tau up to total degree R - 1 (d_a := d/d tau_a), for EVERY n = 0..M-1:
  (H) d_a h_n = h_n (L^{j_a})_{nn}
  (B) d_a b_n^2 = b_n^2 [(L^{j_a})_{nn} - (L^{j_a})_{n-1,n-1}]                  (n >= 1)
  (A) d_a a_n = (L^{j_a})_{n+1,n} - (L^{j_a})_{n,n-1}       (entries outside the M x M matrix are 0: b_0 = b_M = 0)
  (P) d_a pi_n = - sum_{m<n} (L^{j_a})_{nm} pi_m
Controls (must fail): (A) with the opposite sign; (B) with (L^j)_{n+1,n+1} in place of (L^j)_{n-1,n-1}; (H) with L^{j+1}
(wrong exponent); (P) with the opposite sign; (A) with F_j(n) := (L^j)_{n,n+1} (wrong off-diagonal entry).
Measures: the lattices sigma_{2,3} (x_k = k^-2, w_k = k^-3) and sigma_{3,2}, the Hurwitz lattice sigma^{-1/2} with p = 2, s = 3
(x_k = (k - 1/2)^-2, w_k = (k - 1/2)^-3), and a random rational measure; single times j = 1, 2, 3 and multi-times (1, 2), (1, 2, 3)."""
import os, sys, hashlib, random
from fractions import Fraction as Fr
from itertools import product as iprod
from math import factorial

HERE = os.path.abspath(__file__)
print(f"sha256 {os.path.basename(HERE)}: {hashlib.sha256(open(HERE, 'rb').read()).hexdigest()}", flush=True)


class Ser:
    """truncated power series in r variables, total degree <= R, dict exponent-tuple -> Fraction"""
    def __init__(s, r, R, c=None): s.r, s.R, s.c = r, R, {k: v for k, v in (c or {}).items() if v != 0}
    @staticmethod
    def const(r, R, a): return Ser(r, R, {(0,)*r: Fr(a)})
    def __add__(s, o):
        if not isinstance(o, Ser): o = Ser.const(s.r, s.R, o)
        c = dict(s.c)
        for k, v in o.c.items(): c[k] = c.get(k, 0) + v
        return Ser(s.r, s.R, c)
    __radd__ = __add__
    def __neg__(s): return Ser(s.r, s.R, {k: -v for k, v in s.c.items()})
    def __sub__(s, o): return s + (-o if isinstance(o, Ser) else Ser.const(s.r, s.R, -o))
    def __mul__(s, o):
        if not isinstance(o, Ser): return Ser(s.r, s.R, {k: v*o for k, v in s.c.items()})
        c = {}
        for k1, v1 in s.c.items():
            d1 = sum(k1)
            for k2, v2 in o.c.items():
                if d1 + sum(k2) > s.R: continue
                k = tuple(a + b for a, b in zip(k1, k2)); c[k] = c.get(k, 0) + v1*v2
        return Ser(s.r, s.R, c)
    __rmul__ = __mul__
    def inv(s):
        z = (0,)*s.r; a0 = s.c[z]; y = (s - a0)*(Fr(1)/a0); out = Ser.const(s.r, s.R, 1); t = Ser.const(s.r, s.R, 1)
        for _ in range(s.R): t = t*(-y); out = out + t
        return out*(Fr(1)/a0)
    def __truediv__(s, o): return s*o.inv() if isinstance(o, Ser) else s*(Fr(1)/Fr(o))
    def d(s, a):
        c = {}
        for k, v in s.c.items():
            if k[a] > 0: kk = list(k); kk[a] -= 1; c[tuple(kk)] = v*k[a]
        return Ser(s.r, s.R, c)
    def trunc(s, D): return Ser(s.r, s.R, {k: v for k, v in s.c.items() if sum(k) <= D})
    def eq(s, o, D): return (s - o).trunc(D).c == {}


def jacobi(xs, ws, js, R):
    r = len(js); M = len(xs)
    exps = [g for g in iprod(range(R + 1), repeat=r) if sum(g) <= R]
    mom = []
    for i in range(2*M + 1):
        c = {}
        for g in exps:
            gf = 1
            for gi in g: gf *= factorial(gi)
            e = i + sum(gi*ji for gi, ji in zip(g, js))
            c[g] = sum(w*x**e for x, w in zip(xs, ws))/gf
        mom.append(Ser(r, R, c))
    zero = Ser.const(r, R, 0)
    def inner(P, Q):
        out = zero
        for a, pa in enumerate(P):
            for b, qb in enumerate(Q): out = out + pa*qb*mom[a + b]
        return out
    def xmul(P): return [zero] + P
    pis = [[Ser.const(r, R, 1)]]; h = [inner(pis[0], pis[0])]; a = []; b2 = [None]
    for n in range(M):
        xp = xmul(pis[n]); a.append(inner(xp, pis[n])/h[n])
        if n == M - 1: break
        nxt = [xp[i] - (a[n]*pis[n][i] if i < len(pis[n]) else zero) - (b2[n]*pis[n - 1][i] if n >= 1 and i < len(pis[n - 1]) else zero)
               for i in range(n + 2)]
        pis.append(nxt); h.append(inner(nxt, nxt)); b2.append(h[n + 1]/h[n])
    return pis, h, a, b2


def matpow(L, j, M, r, R):
    I = [[Ser.const(r, R, 1 if i == k else 0) for k in range(M)] for i in range(M)]
    P = I
    for _ in range(j):
        P = [[sum((P[i][l]*L[l][k] for l in range(M) if L[l][k].c), Ser.const(r, R, 0)) for k in range(M)] for i in range(M)]
    return P


NCHK = [0]; NCTL = [0]; FAILS = []
def check(label, ok, control=False):
    if control:
        NCTL[0] += 1
        if ok: FAILS.append("CONTROL HELD: " + label)
    else:
        NCHK[0] += 1
        if not ok: FAILS.append(label)


def run(name, xs, ws, js, R):
    r = len(js); M = len(xs)
    pis, h, a, b2 = jacobi(xs, ws, js, R)
    Z = Ser.const(r, R, 0)
    L = [[Z for _ in range(M)] for _ in range(M)]
    for n in range(M):
        L[n][n] = a[n]
        if n + 1 < M: L[n][n + 1] = Ser.const(r, R, 1); L[n + 1][n] = b2[n + 1]
    ent = lambda P, i, k: P[i][k] if 0 <= i < M and 0 <= k < M else Z
    D = R - 1; nid = nct = 0
    for ai, j in enumerate(js):
        Lj = matpow(L, j, M, r, R); Lj1 = matpow(L, j + 1, M, r, R)
        for n in range(M):
            lab = f"{name} times {js} d_{{tau_{j}}} n={n}"
            check(lab + " (H)", h[n].d(ai).eq(h[n]*Lj[n][n], D))
            check(lab + " (A)", a[n].d(ai).eq(ent(Lj, n + 1, n) - ent(Lj, n, n - 1), D))
            dp = [c.d(ai) for c in pis[n]]
            rhs = [Z]*len(pis[n])
            for m in range(n):
                for i, cm in enumerate(pis[m]): rhs[i] = rhs[i] - Lj[n][m]*cm
            check(lab + " (P)", all(x.eq(y, D) for x, y in zip(dp, rhs)))
            nid += 3
            if n >= 1:
                check(lab + " (B)", b2[n].d(ai).eq(b2[n]*(Lj[n][n] - Lj[n - 1][n - 1]), D)); nid += 1
            # controls
            check(lab + " control (A) sign", a[n].d(ai).eq(-(ent(Lj, n + 1, n) - ent(Lj, n, n - 1)), D), control=True)
            check(lab + " control (H) L^{j+1}", h[n].d(ai).eq(h[n]*Lj1[n][n], D), control=True)
            check(lab + " control (A) F_j(n) = (L^j)_{n,n+1}", a[n].d(ai).eq(ent(Lj, n, n + 1) - ent(Lj, n - 1, n), D), control=True)
            nct += 3
            if n >= 1:
                check(lab + " control (P) sign", all(x.eq(-y, D) for x, y in zip(dp, rhs)), control=True)
                if n + 1 < M:
                    check(lab + " control (B) (L^j)_{n+1,n+1}", b2[n].d(ai).eq(b2[n]*(Lj[n][n] - Lj[n + 1][n + 1]), D), control=True)
                    nct += 1
                nct += 1
    print(f"{name}, M = {M} atoms, times x^{js}, tau-degree <= {R}: {nid} identities, {nct} controls", flush=True)


M = 6
lat = lambda p, s, d=Fr(0): ([Fr(1)/(Fr(k) + d)**p for k in range(1, M + 1)], [Fr(1)/(Fr(k) + d)**s for k in range(1, M + 1)])
random.seed(20261023)
rnd = (sorted({Fr(random.randint(1, 97), random.randint(1, 97)) for _ in range(3*M)})[:M], [Fr(random.randint(1, 50), 7) for _ in range(M)])
cases = [("sigma_{2,3}", lat(2, 3)), ("sigma_{3,2}", lat(3, 2)), ("Hurwitz sigma^{-1/2} (p=2, s=3)", lat(2, 3, Fr(-1, 2))),
         ("random rational measure", rnd)]
for name, (xs, ws) in cases:
    for js, R in [((1,), 4), ((2,), 4), ((3,), 3), ((1, 2), 3), ((1, 2, 3), 2)]:
        run(name, xs, ws, js, R)
print(f"identities checked: {NCHK[0]}, controls: {NCTL[0]}")
for f in FAILS: print("FAIL", f)
assert not FAILS, f"{len(FAILS)} failures"
print(f"ALL {NCHK[0]} IDENTITIES HOLD; ALL {NCTL[0]} CONTROLS FAIL")
