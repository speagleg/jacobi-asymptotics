"""JZC_SHIFT common helpers (exact algebra; nothing fitted).

(1) The index-shift (Lagrange-Buermann) prediction.  For exponents j_a and natural leads eps_a = (p j_a/2) e_a (e_a = the engine's
    normalised time, e_a = mu_a c^{j_a} C(2j_a, j_a)), let x solve  x = N - (1/p) sum_a eps_a x^{-p j_a}  (formal series).  Then
      x^{-p} = sum_beta  eps^beta (p + 1 + S)_{m-1} / (beta! p^{m-1})  N^{-p-S-m},   m = |beta|,  S = p sum_a beta_a j_a,
    (Lagrange-Buermann; derivation in JZC_SHIFT.md §1).  In the engine's natural form (w2_engine.py: nat[beta][k] = coefficient of
    N^{-k} of (N/n)^{(sum beta_a j_a + 1)p} e-layer) the prediction is
      nat[beta][k] = 0 (k < m),   nat[beta][m] = LB(beta) := prod_a (p j_a/2)^{beta_a} (p + 1 + S)_{m-1} / (beta! p^{m-1}).
(2) A formal discrete Toda engine (FT): formal series in 1/n with symbolic exponents p(kp + sum beta_a j_a), shifts n -> n + k,
    the Toda hierarchy for the orthonormal Jacobi matrix (JZC_M4 §8; diagonal alpha_n, off-diagonal b_n, b_n^2 = h_n/h_{n-1}):
      d_{t_j} b_n = (1/2) b_n [(J^j)_{nn} - (J^j)_{n-1,n-1}],      d_{t_j} alpha_n = F_j(n) - F_j(n-1),  F_j(n) := b_{n+1} (J^j)_{n+1,n},
    with the tilt exp(sum_j t_j x^j) (unscaled t_j; in the n^p frame mu_j = -t_j n^{-jp}).  Elements are dicts
      key (kp, beta) -> [c_0, ..., c_D]   meaning   t^beta n^{-p(kp + sum_a beta_a j_a)} sum_i c_i n^{-i},
    with coefficients in a sympy polynomial ring / field (caller's choice)."""
import os, sys, hashlib, json, time
from math import factorial
from itertools import product as iproduct
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
SHC = os.path.join(ROOT, 'tmp', 'shift'); os.makedirs(SHC, exist_ok=True)
W2C = os.path.join(ROOT, 'tmp', 'w2')
PY = sys.executable


def sha(fn): return hashlib.sha256(open(fn, 'rb').read()).hexdigest()


def provenance(*fns):
    for fn in fns: print(f"sha256 {os.path.basename(fn)}: {sha(fn)}", flush=True)


class Checks:
    def __init__(s): s.n = 0; s.ok = True; s.nf = 0; s.nc = 0
    def check(s, label, holds, must_fail=False):
        s.n += 1; passed = (not holds) if must_fail else bool(holds); s.ok &= passed
        if must_fail: s.nc += 1
        if not passed: s.nf += 1
        print(f"[{s.n}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'fails'} -> "
              f"{'PASS' if passed else 'FAIL'}", flush=True)
        return passed
    def finish(s):
        print(f"{'ALL' if s.ok else 'NOT ALL'} {s.n} CHECKS PASSED ({s.n - s.nc} identities, {s.nc} controls; failures: {s.nf})",
              flush=True)
        assert s.ok


def poch(x, m):
    r = sp.Integer(1)
    for i in range(m): r *= (x + i)
    return r


def LB(beta, js, p, kappa=1, shiftc=1):
    """index-shift prediction for nat[beta][|beta|] (engine natural form, e-units).  kappa, shiftc: deliberate distortions for
    controls (kappa: the 1/p in the shift becomes kappa/p; shiftc: the exponent p+1+S becomes p+shiftc+S)."""
    m = sum(beta); S = p*sum(b*j for b, j in zip(beta, js))
    bf = sp.Mul(*[sp.factorial(b) for b in beta])
    pre = sp.Mul(*[(p*j/2)**b for b, j in zip(beta, js)])
    return pre*poch(p + shiftc + S, m - 1)*kappa**(m - 1)/(bf*p**(m - 1))


def LB_series(js, p, order):
    """independent check of LB: solve y = -(1/p) sum_a s_a (1+y)^{-p j_a} by fixed-point iteration in the formal variables s_a
    (s_a = eps_a N^{-1-p j_a}, x = N(1+y)) and return the coefficients of (1+y)^{-p} as {beta: coeff}."""
    s = sp.symbols(f"s0:{len(js)}")
    y = sp.Integer(0)
    def trunc(e):
        e = sp.expand(e); P = sp.Poly(e, *s)
        return sum((c*sp.Mul(*[v**k for v, k in zip(s, mon)]) for mon, c in P.terms() if sum(mon) <= order), sp.Integer(0))
    def powser(y, a):     # (1+y)^a truncated at total degree `order` in s
        out = sp.Integer(1); term = sp.Integer(1)
        for k in range(1, order + 1):
            term = trunc(term*y); out += sp.binomial(a, k)*term
        return trunc(out)
    for _ in range(order + 1):
        y = trunc(-sum(sa*powser(y, -p*j) for sa, j in zip(s, js))/p)
    X = powser(y, -p)
    P = sp.Poly(X, *s)
    return {mon: sp.factor(c) for mon, c in P.terms()}


# ------------------------------------------------------------------------------------------------------------------------------
class FT:
    """formal discrete Toda engine (see module docstring).  R: coefficient domain (sympy ring or field), pp: element of R
    standing for p, js: tuple of exponents (positive integers), D: n^{-1} truncation degree, M: Taylor truncation order in t."""
    def __init__(s, R, pp, js, D, M):
        s.R, s.p, s.js, s.D, s.M = R, pp, tuple(js), D, M
        s.zero = R(0); s.one = R(1); s.r = len(js); s.Mcur = M
        s._binc = {}

    def sigma(s, key):
        kp, beta = key
        return s.p*(kp + sum(b*j for b, j in zip(beta, s.js)))

    def add(s, X, Y, cy=1):
        out = {k: list(v) for k, v in X.items()}
        for k, v in Y.items():
            if k in out: out[k] = [a + cy*b for a, b in zip(out[k], v)]
            else: out[k] = [cy*b for b in v]
        return out

    def scal(s, X, c): return {k: [c*a for a in v] for k, v in X.items()}

    def mul(s, X, Y):
        out = {}
        for (k1, b1), v1 in X.items():
            for (k2, b2), v2 in Y.items():
                b = tuple(x + y for x, y in zip(b1, b2))
                if sum(b) > s.Mcur: continue
                key = (k1 + k2, b)
                w = [s.zero]*(s.D + 1)
                for i, a in enumerate(v1):
                    if a == s.zero: continue
                    for j in range(s.D + 1 - i):
                        if v2[j] != s.zero: w[i + j] += a*v2[j]
                out[key] = [x + y for x, y in zip(out[key], w)] if key in out else w
        return out

    def binneg(s, sig, i, r):
        """binom(-sig - i, r) as an element of R"""
        key = (sig, i, r)
        if key not in s._binc:
            v = s.one
            for q in range(r): v = v*(-sig - i - q)
            s._binc[key] = v*s.R(sp.Rational(1, factorial(r)))
        return s._binc[key]

    def shift(s, X, k):
        """n -> n + k:  n^{-sig-i} -> n^{-sig-i} sum_r binom(-sig-i, r) k^r n^{-r}"""
        out = {}
        for key, v in X.items():
            sig = s.sigma(key); w = [s.zero]*(s.D + 1)
            for i, a in enumerate(v):
                if a == s.zero: continue
                for r in range(s.D + 1 - i):
                    w[i + r] += a*s.binneg(sig, i, r)*(k**r)
            out[key] = w
        return out

    def diff(s, X):
        """(1 - S_{-1}) X"""
        return s.add(X, s.shift(X, -1), -1)

    def paths(s, j, r):
        """lattice paths of length j from 0 to r: list of step lists (+1, 0, -1)"""
        return [st for st in iproduct((1, 0, -1), repeat=j) if sum(st) == r]

    def Jpow(s, a, b, j, r, cache):
        """(J^j)_{n, n+r} as an element: sum over paths of products of shifted entries (diag a_m, off-diag J_{m,m+1} = b_{m+1})"""
        def sh(X, name, k):
            if (name, k) not in cache: cache[(name, k)] = s.shift(X, k) if k != 0 else X
            return cache[(name, k)]
        tot = {}
        for st in s.paths(j, r):
            pos = 0; term = None
            for d in st:
                if d == 0: f = sh(a, 'a', pos)
                elif d == 1: f = sh(b, 'b', pos + 1)
                else: f = sh(b, 'b', pos)
                term = f if term is None else s.mul(term, f)
                pos += d
            tot = s.add(tot, term)
        return tot

    def rhs(s, a, b, ji):
        """(d_{t_j} a, d_{t_j} b) for j = js[ji], as truncated elements"""
        j = s.js[ji]; cache = {}
        Jnn = s.Jpow(a, b, j, 0, cache)
        Db = s.scal(s.mul(b, s.diff(Jnn)), s.R(sp.Rational(1, 2)))
        Fj = s.mul(s.shift(b, 1), s.Jpow(a, b, j, 1, cache))      # b_{n+1} (J^j)_{n, n+1}
        Da = s.diff(Fj)
        return Da, Db

    def flow(s, a0, b0, check_commute=True, verbose=False):
        """Taylor coefficients of (alpha_n(t), b_n(t)) to order M from the initial data (keys (1, 0)).  Returns (a, b, ncomm) where
        ncomm counts the commutativity checks made (new coefficient computed via two different flows, asserted equal)."""
        zb = tuple([0]*s.r)
        a = {(1, zb): list(a0)}; b = {(1, zb): list(b0)}; ncomm = 0
        for m in range(s.M):
            t0 = time.time()
            # the state holds orders <= m; every flow's rhs is needed to order m only
            s.Mcur = m
            R_ = [s.rhs(a, b, ji) for ji in range(s.r)]
            newa, newb = {}, {}
            for beta in iproduct(range(m + 2), repeat=s.r):
                if sum(beta) != m + 1: continue
                cands = []
                for ji in range(s.r):
                    if beta[ji] == 0: continue
                    src = tuple(x - (1 if t == ji else 0) for t, x in enumerate(beta))
                    key = (1 + s.js[ji], src)
                    fa = R_[ji][0].get(key, [s.zero]*(s.D + 1)); fb = R_[ji][1].get(key, [s.zero]*(s.D + 1))
                    c = s.R(sp.Rational(1, beta[ji]))
                    cands.append(([c*x for x in fa], [c*x for x in fb]))
                va, vb = cands[0]
                if check_commute:
                    for wa, wb in cands[1:]:
                        assert all(x == y for x, y in zip(va, wa)) and all(x == y for x, y in zip(vb, wb)), ("flows do not commute", beta)
                        ncomm += 1
                newa[(1, beta)] = va; newb[(1, beta)] = vb
            a.update(newa); b.update(newb)
            # sanity: rhs keys are exactly (1 + j, beta)
            if verbose: print(f"   FT order {m + 1} done ({time.time() - t0:.1f}s)", flush=True)
        s.Mcur = s.M
        return a, b, ncomm


# ------------------------------------------------------------------------------------------------------------------------------
# lattice integer layers (beta = nu = alpha) and the FT -> engine-natural-form conversion
def lattice_initial(K, p, al, D, extra=None):
    """(alpha_n, b_n) at t = 0 as FT coefficient lists (c = 1) to n^{-D}:
    b_n = n^{-p} B(n): B to n^{-2} from Identity N.1 / Theorem N.6(ii) (d1 = -p delta, d2 = p(p+1)delta^2/2 + f2, delta = (alpha+1)/2,
      f2 = (p+1)/12 - (p+2)alpha^2/8);
    alpha_n = 2 n^{-p} A(n): A1 = -p(alpha/2 + 1), A2 = (p+1)^2 alpha^2/4 + p(p+1)alpha/2 + p^2/2 + 11p/24 - 1/24, DERIVED in
      shift_dressing.py from Theorem T (T1) and the exact first-order j = 1 layer (m4_zeta_exact2 (A), Theorem N.6(ii)): it equals
      the natural form (n/M)^p (1 + a2 M^-2), M = n + alpha/2 + 1, a2 = -(p+1)/24 + (p+1)(p+2)alpha^2/8 (m4_diag, NUMERICAL there);
    the coefficients of n^{-3..-D} are the generic symbols in `extra` (dict name -> K element), to show that they do not enter."""
    dl = (al + 1)/2; f2 = (p + 1)/12 - (p + 2)*al**2/8
    b0 = [K(1), -p*dl, p*(p + 1)*dl**2/2 + f2]
    A1 = -al*p/2 - p; A2 = al**2*(p + 1)**2/4 + al*p*(p + 1)/2 + p**2/2 + p*K(11)/24 - K(1)/24
    a0 = [2*K(1), 2*A1, 2*A2]
    for i in range(3, D + 1):
        b0.append(extra[f"B{i}"] if extra else K(0)); a0.append(2*extra[f"A{i}"] if extra else K(0))
    return a0[:D + 1], b0[:D + 1]


def to_natural(v, sig, beta, js, delta):
    """FT layer t^beta of n^p b_n (coefficient list v in n^{-1}, c = 1) -> the engine's natural form for the monomial e^beta:
    e_a = mu_a C(2j_a, j_a), mu_a = -t_a n^{-p j_a}  =>  resp = v / prod(-C(2j_a, j_a))^{beta_a};  nat = coefficients in 1/N of
    (N/n)^{sig} resp, N = n + delta, sig = (sum beta_a j_a + 1) p  (sympy expressions in, sympy expressions out)."""
    W = sp.Symbol('w_')
    ser = sum(c*W**i*(1 - delta*W)**(-i) for i, c in enumerate(v))
    ser = ser*(1 - delta*W)**(-sig)/sp.Mul(*[(-sp.binomial(2*j, j))**b for b, j in zip(beta, js)])
    s = sp.series(ser, W, 0, len(v)).removeO()
    return [sp.factor(s.coeff(W, i)) for i in range(len(v))]
