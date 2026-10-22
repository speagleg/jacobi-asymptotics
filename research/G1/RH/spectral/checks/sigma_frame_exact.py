"""JZC_SIGMA (Conjecture Sigma): EXACT check of the frame identity (FI) of Lemma F, identically in (p, alpha, gamma).

Lemma F (JZC_SIGMA.md §2) analyses the SAME degree-n lattice problem in the frame of a real index m = n + gamma (scaling m^p,
g-function e^{m g}), with the gauge U_m z^{gamma s3}. Its conclusion is that m^p b_n / c is the double expansion of the
decoupled model M(beta = alpha - 2 gamma, nu = alpha) at index m. Comparing with the n-frame (Theorem N.6, M(alpha, alpha) at
index n), uniqueness of asymptotic expansions gives, for the integer layer B(n; beta, nu) := sum_k d_k(p, beta, nu) n^{-k}:

  (FI)    B(n + gamma; alpha - 2 gamma, alpha) = (1 + gamma/n)^p B(n; alpha, alpha)       (formal series in 1/n)

and, with beta in place of alpha on both sides (equivalent to Prop S / Conjecture Sigma), the infinitesimal form

  (FL)    d/dn B - 2 d/dbeta B = (p/n) B                                                 (the flow identity of JZC_M4 §7).

This script computes the d_k exactly (the engine of m4_shift_exact.py, imported, NOT edited: field Q(p, alpha, beta), alpha = the
Bessel order nu, beta = the Szego exponent, c = 1) and asserts, coefficient by coefficient of 1/n up to n^{-KORD}:
  [1] FI identically in (p, alpha, gamma);
  [2] FI with general base: B(n + gamma; beta - 2 gamma, alpha) = (1 + gamma/n)^p B(n; beta, alpha), identically in (p, alpha, beta, gamma);
  [3] FL identically in (p, alpha, beta);
  [4] gamma = 1/2 specialisation of [1] at the Bessel point p = 2, alpha = -1/2 (closed form (1 - 1/(4N^2))^{-1/2}, JZC_M4 §4):
      B(n; alpha, alpha) = (n/N)^2 (1 - 1/(4N^2))^{-1/2} with N = n + 1/4  (a consistency check of the engine at one point).
Controls (each must FAIL at some order k <= KORD, asserted):
  C1 half Szego shift beta = alpha - gamma;  C2 wrong sign beta = alpha + 2 gamma;  C3 no frame factor (1 + gamma/n)^p;
  C4 no index shift (gauge only: B(n; alpha - 2 gamma, alpha) = B(n; alpha, alpha), the n-frame H-d form without degree change);
  C5 Bessel order moved with the Szego exponent (nu = beta = alpha - 2 gamma: the 'genuine weight' change, H2 of JZC_M3a_Hd §4);
  C6 frame factor with exponent 2p (wrong power).
  [5] the natural form at general beta reproduces m4_shift_exact.out (f1 = f3 = 0, f2, f4 closed forms): the series cap used here
      (SHI = 18 instead of 30, for speed on a loaded machine) changes nothing; the engine's own guard asserts that every principal part
      is determined at the chosen cap ("truncation too shallow" otherwise).
Usage: SHI=18 KORD=4 python -B sigma_frame_exact.py. The engine output d_k is cached in <repo>/tmp/sigma_cache/ keyed by KORD, SHI and the
engine's sha256; delete the cache file to force a fresh engine run (the .out says which happened)."""
import os, sys, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "4")
import m4_shift_exact as E                      # imported, not edited
from sympy import QQ, Rational, factor, factorial
from sympy.polys.fields import field

KORD = E.KORD
K2, p, al, be, ga = field("p,alpha,beta,gamma", QQ)    # alpha = Bessel order nu, beta = Szego exponent
ONE, ZERO = K2(1), K2(0)


def provenance(*fns):
    for fn in fns:
        print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)


provenance(__file__, E.__file__)
t0 = time.time()
# engine output cache (keyed by the engine's sha256 and KORD): <repo>/tmp/sigma_cache/; delete it to force a fresh engine run
from pathlib import Path
from sympy import sympify
CACHE = Path(__file__).resolve().parents[5] / "tmp" / "sigma_cache"
sha_e = hashlib.sha256(open(E.__file__, 'rb').read()).hexdigest()[:16]
cf = CACHE / f"d_K{KORD}_SHI{E.S.HI}_{sha_e}.txt"
if cf.exists():
    lines = cf.read_text().splitlines()
    from sympy import Symbol
    loc = {nm: Symbol(nm) for nm in ("p", "alpha", "beta")}
    dexpr = [sympify(x, locals=loc) for x in lines]
    print(f"engine output read from cache {cf.name} (engine sha256 prefix {sha_e})", flush=True)
else:
    d, f = E.run(verbose=True)
    dexpr = [d[k].as_expr() for k in range(KORD + 1)]
    CACHE.mkdir(parents=True, exist_ok=True); cf.write_text("\n".join(str(x) for x in dexpr))
    print(f"engine done, KORD = {KORD} ({time.time() - t0:.0f}s); cached as {cf.name}", flush=True)
dK2 = [K2.from_expr(x) for x in dexpr]                  # elements of K2 not involving gamma


def lift(x, P, A, B):
    """element x(p, alpha, beta) of K2 -> x(P, A, B)"""
    def ev(poly):
        out = ZERO
        for (i, j, k, l), c in poly.terms():
            assert l == 0
            out += K2(c)*P**i*A**j*B**k
        return out
    return ev(x.numer)/ev(x.denom)


def pw(x, k):
    return ONE if k == 0 else x**k


def binom(e, j):
    r = ONE
    for i in range(j): r = r*(e - i)
    return r/int(factorial(j))


def Bcoef(P, A, B, shift, pref):
    """coefficients (x^0..x^KORD, x = 1/n) of (1 + gamma x)^pref * sum_k d_k(P, A, B) (x/(1 + shift x))^k"""
    dk = [lift(dK2[k], P, A, B) for k in range(KORD + 1)]
    out = [sum((dk[k]*binom(K2(-k), K - k)*pw(shift, K - k) for k in range(K + 1)), ZERO) for K in range(KORD + 1)]
    if pref is not None:
        pp = [binom(pref, j)*pw(ga, j) for j in range(KORD + 1)]
        out = [sum((pp[j]*out[K - j] for j in range(K + 1)), ZERO) for K in range(KORD + 1)]
    return out


def compare(lhs, rhs):
    for K in range(KORD + 1):
        r = lhs[K] - rhs[K]
        if r != ZERO:
            return K, r
    return None


def fmt(r):
    return "HOLDS identically" if r is None else "FAILS at order %d: %s" % (r[0], factor(r[1].as_expr()))


ok = True
rhs_FI = Bcoef(p, al, al, ZERO, p)                     # (1 + gamma/n)^p B(n; alpha, alpha)
lhs = Bcoef(p, al, al - 2*ga, ga, None)                # B(n + gamma; alpha - 2 gamma, alpha)
r = compare(lhs, rhs_FI); ok &= r is None
print(f"[1] FI  B(n+gamma; alpha-2gamma, alpha) = (1+gamma/n)^p B(n; alpha, alpha), orders 0..{KORD}: {fmt(r)}", flush=True)

r = compare(Bcoef(p, al, be - 2*ga, ga, None), Bcoef(p, al, be, ZERO, p)); ok &= r is None
print(f"[2] FI general base  B(n+gamma; beta-2gamma, alpha) = (1+gamma/n)^p B(n; beta, alpha), orders 0..{KORD}: {fmt(r)}",
      flush=True)

# [3] FL: x^{K+1} coefficient of dB/dn - 2 dB/dbeta - (p/n) B :  -K d_K - 2 d_{K+1,beta} - p d_K
D = dK2
fl_bad = None
for K in range(KORD):
    r = -K*D[K] - 2*D[K + 1].diff(be) - p*D[K]
    if r != ZERO and fl_bad is None: fl_bad = (K + 1, factor(r.as_expr()))
ok &= fl_bad is None
print(f"[3] FL  dB/dn - 2 dB/dbeta = (p/n) B, orders 1..{KORD}: {'HOLDS identically' if fl_bad is None else 'FAILS %s' % (fl_bad,)}",
      flush=True)

# [4] Bessel point p = 2, alpha = beta = -1/2: B(n) = (n/N)^2 (1 - 1/(4N^2))^{-1/2}, N = n + 1/4 (exact rational series)
from sympy import symbols, series
x = symbols("x")
h = Rational(-1, 2)
Bser = [lift(dK2[k], K2(2), K2(h), K2(h)).as_expr() for k in range(KORD + 1)]
N = (1 + x/4)/x
closed = series((1/(x*N))**2*(1 - 1/(4*N**2))**Rational(-1, 2), x, 0, KORD + 1).removeO()
r4 = [Bser[k] - closed.coeff(x, k) for k in range(KORD + 1)]
ok4 = all(v == 0 for v in r4); ok &= ok4
print(f"[4] Bessel point p=2, alpha=beta=-1/2: B(n) = (n/N)^2 (1-1/(4N^2))^(-1/2), N = n+1/4, orders 0..{KORD}: "
      f"{'HOLDS' if ok4 else 'FAILS ' + str(r4)}  (d_k = {Bser})", flush=True)

# [5] agreement with the reviewed engine run (m4_shift_exact.out, SHI = 30): natural form in N = n + (beta+1)/2 at general beta,
#     f_1 = f_3 = 0, f_2 and f_4 equal the closed forms printed there (so the series cap used here changes nothing)
dl = be/2 + ONE/2
nat = []                                                  # coefficients of (1 - dl y)^{-p} sum_k d_k (y/(1 - dl y))^k, y = 1/N
raw = [sum((D[k]*binom(K2(-k), K - k)*pw(-dl, K - k) for k in range(K + 1)), ZERO) for K in range(KORD + 1)]
pre = [binom(-p, j)*pw(-dl, j) for j in range(KORD + 1)]
nat = [sum((pre[j]*raw[K - j] for j in range(K + 1)), ZERO) for K in range(KORD + 1)]
f2c = -(p + 2)*al**2/8 + (p + 1)/12
f4c = -(45*al**4*p**4 + 180*al**4*p**3 + 180*al**4*p**2 + 300*al**2*p**3 + 900*al**2*p**2 + 600*al**2*p - 24*p**4 - 208*p**3
        - 404*p**2 - 232*p - 12)/(5760*p*(3*p + 2))
want = {1: ZERO, 2: f2c, 3: ZERO, 4: f4c}
ok5 = all(nat[k] == want[k] for k in want if k <= KORD); ok &= ok5
print(f"[5] natural form at general beta: f1 = f3 = 0, f2, f4 = the closed forms of m4_shift_exact.out (orders <= {KORD}): "
      f"{'HOLDS' if ok5 else 'FAILS ' + str([factor((nat[k] - want[k]).as_expr()) for k in want if k <= KORD])}", flush=True)

controls = [
    ("C1 half Szego shift beta = alpha - gamma", Bcoef(p, al, al - ga, ga, None), rhs_FI),
    ("C2 wrong sign beta = alpha + 2 gamma", Bcoef(p, al, al + 2*ga, ga, None), rhs_FI),
    ("C3 no frame factor (1+gamma/n)^p", lhs, Bcoef(p, al, al, ZERO, None)),
    ("C4 no index shift (gauge only, n-frame)", Bcoef(p, al, al - 2*ga, ZERO, None), Bcoef(p, al, al, ZERO, None)),
    ("C5 Bessel order moved too (nu = beta = alpha - 2 gamma)", Bcoef(p, al - 2*ga, al - 2*ga, ga, None), rhs_FI),
    ("C6 frame factor exponent 2p", lhs, Bcoef(p, al, al, ZERO, 2*p)),
]
nc = 0
for lab, L_, R_ in controls:
    r = compare(L_, R_); fails = r is not None; ok &= fails; nc += 1
    print(f"CONTROL (must fail) {lab}: " + (f"fails at order {r[0]} (residual {factor(r[1].as_expr())}) -> PASS" if fails else
          "HOLDS -> FAIL"), flush=True)
print(f"{nc} controls; total time {time.time() - t0:.0f}s")
print("ALL IDENTITIES HOLD, ALL CONTROLS FAIL" if ok else "IDENTITY OR CONTROL FAILURE")
assert ok
