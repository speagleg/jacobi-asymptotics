"""JZC_W_kappa §6 (NUMERICAL, mpmath dps 30): the p < 1 obstruction for the lattice-g route, in numbers.
rho1(z) = t(z) - t_kappa(z) = n z^{-1/p}(1 - (1 - kappa z/n^p)^{1/p}) (principal), the index offset that the gauge must carry (forced by
Prop K.14 (a)); q1 = 1 - 1/p (< 0 for p < 1); e(p) := (1 - p)(2 + p)/p.
Claims checked:
  [P1a] hard edge: rho1(y) y^{-q1} -> (kappa/p) n^{1-p} as y -> 0+, so rho1 is unbounded at 0+ for p < 1. Control (must fail):
        "unbounded" at p = 3/2.
  [P1b] Bessel scale: |rho1(n^{-2} e^{i theta_lip})| ~ (|kappa|/p) n^{e(p)}; local exponent in n (n = 1e3 -> 1e5) = e(p) for
        p in {0.6, 0.75, 1.5, 3}: > 0 exactly for p < 1 (the gauge's lip phase is not small where the Bessel model lives).
  [P1c] lips at fixed n: log|lip factor| = -/+ 2 pi Im rho1(r e^{+/- i theta}) on the two lips (theta = pi p/4, Paper 2's p < 1 lip
        angle) -> +inf for kappa > 0 (both lips; F1 |v| <= C fails) and -> -inf for kappa < 0 (the lip entry vanishes, |omega - rho_pm|
        -> 1), as r -> 0.
  [P1d] band factor: the gauge part -2 pi cot(pi/p) rho1(x) of log H_n^kappa is unbounded at 0+ (p = 0.6), except when cot(pi/p) = 0
        (p = 2/3: identically 0).
  [P1e] soft edge: rho1(4c) n^{p-1} -> (kappa/p)(4c)^{q1}, so rho1(4c) -> inf with n for p < 1 (n-uniformity of (O4) / Lemma szego
        (vi)(b) fails when cot(pi/p) != 0).
  [P1f] p <= 1/2: int_eps^1 rho1(y) dy diverges like eps^{2 - 1/p} (p = 0.4): C[rho1] does not exist as a Cauchy integral.
  [P1g] 1/2 < p < 1 (p = 0.75): the closed form of Lemma K.1 still holds numerically (spread over 5 points), and |E_kappa| = e^{Re C}
        is unbounded near 0 (max over two rays of |Re C| exceeds 10 at r = 1e-8 and grows by more than 5x from r = 1e-4; it tends to
        +inf for kappa > 0 and -inf for kappa < 0 on both rays) -- (O5) at 0 fails for F_nat."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 30
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi; HALF = mp.mpf(1)/2


def cp(p): Ip = mp.sqrt(PI)/2*mp.gamma(1/p + HALF)/mp.gamma(1/p + 1); return (PI/(2*Ip))**p/4
def rho1(z, n, p, kap): return -n*mp.power(z, -1/p)*mp.expm1(mp.log(1 - kap*z/n**p)/p)
def ep(p): return (1 - p)*(2 + p)/p

# [P1a]
for (p, kap) in ((mp.mpf('0.6'), mp.mpf('0.3')), (mp.mpf('0.75'), mp.mpf('-0.3')), (mp.mpf('1.5'), mp.mpf('0.3'))):
    n = mp.mpf(4); q1 = 1 - 1/p; lead = kap/p*n**(1 - p)
    y = mp.mpf('1e-12'); r = rho1(y, n, p, kap)
    rel = abs(r*y**(-q1)/lead - 1)
    print(f"[P1a] p={p} kappa={kap}: rho1(1e-12) = {mp.nstr(r, 6)}; rho1 y^-q1/((kappa/p) n^(1-p)) - 1 = {mp.nstr(rel, 3)}")
    C_.check(f"[P1a] p={p}: leading term (kappa/p) n^(1-p) y^q1", float(rel), 0.0, 1e-6)
    if p < 1: C_.check(f"[P1a] p={p}: rho1 unbounded at 0+ (|rho1(1e-12)| > 1e3)", float(abs(r) > 1e3), 1.0, 0.0)
    else: C_.check(f"[ctrl] p={p}: rho1 unbounded at 0+ (must fail)", float(abs(r) > 1e3), 0.0, 0.0)

# [P1b]
for p in (mp.mpf('0.6'), mp.mpf('0.75'), mp.mpf('1.5'), mp.mpf(3)):
    kap = mp.mpf('0.3'); th = PI*p/4 if p < 1 else PI/3
    vals = {n: abs(rho1(n**-2*mp.expj(th), n, p, kap)) for n in (mp.mpf(10)**3, mp.mpf(10)**5)}
    sl = mp.log(vals[mp.mpf(10)**5]/vals[mp.mpf(10)**3])/mp.log(100)
    print(f"[P1b] p={p}: |rho1| on the Bessel scale at n = 1e3, 1e5: {mp.nstr(vals[mp.mpf(10)**3], 4)}, {mp.nstr(vals[mp.mpf(10)**5], 4)}; "
          f"exponent {mp.nstr(sl, 6)} (e(p) = {mp.nstr(ep(p), 6)})")
    C_.check(f"[P1b] p={p}: exponent e(p) = (1-p)(2+p)/p", float(sl), float(ep(p)), 1e-3)
    C_.check(f"[P1b] p={p}: Bessel-scale phase grows iff p < 1", float((sl > 0) == (p < 1)), 1.0, 0.0)

# [P1c]
for kap in (mp.mpf('0.3'), mp.mpf('-0.3')):
    p = mp.mpf('0.6'); n = mp.mpf(4); th = PI*p/4
    out = []
    for r in (mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-12')):
        up = -2*PI*mp.im(rho1(r*mp.expj(th), n, p, kap))          # log|e^{+2 pi i rho1}| on the upper lip
        lo = 2*PI*mp.im(rho1(r*mp.expj(-th), n, p, kap))          # log|e^{-2 pi i rho1}| on the lower lip
        out.append((up, lo))
    print(f"[P1c] p={p} kappa={kap}: log|lip factor| (upper, lower) at r = 1e-4, 1e-8, 1e-12: "
          + "; ".join(f"({mp.nstr(u, 4)}, {mp.nstr(l, 4)})" for u, l in out))
    sgn = 1 if kap > 0 else -1
    C_.check(f"[P1c] kappa={kap}: lip factor modulus -> e^(+/-inf) on both lips (sign of kappa)",
             float(all(sgn*u > 100 and sgn*l > 100 for u, l in out[2:]) and sgn*out[2][0] > sgn*out[1][0] > sgn*out[0][0]), 1.0, 0.0)

# [P1d]
for p in (mp.mpf('0.6'), mp.mpf(2)/3):
    n = mp.mpf(4); kap = mp.mpf('0.3')
    g = [abs(2*PI*mp.cot(PI/p)*rho1(x, n, p, kap)) for x in (mp.mpf('1e-6'), mp.mpf('1e-12'))]
    print(f"[P1d] p={mp.nstr(p, 4)}: |gauge part of log H| at x = 1e-6, 1e-12: {mp.nstr(g[0], 4)}, {mp.nstr(g[1], 4)}  (cot(pi/p) = {mp.nstr(mp.cot(PI/p), 3)})")
    if abs(mp.cot(PI/p)) > mp.mpf('1e-20'):
        C_.check(f"[P1d] p={mp.nstr(p,4)}: band factor unbounded at 0+", float(g[1] > 1e3 and g[1] > g[0]), 1.0, 0.0)
    else:
        C_.check(f"[P1d] p=2/3: cot(pi/p) = 0, band factor's gauge part vanishes", float(g[1]), 0.0, 1e-15)

# [P1e]
for p in (mp.mpf('0.6'), mp.mpf('0.75')):
    kap = mp.mpf('0.3'); c = cp(p); q1 = 1 - 1/p
    v = {n: rho1(4*c, n, p, kap) for n in (mp.mpf(10)**3, mp.mpf(10)**6)}
    lim = kap/p*(4*c)**q1
    print(f"[P1e] p={p}: rho1(4c) at n = 1e3, 1e6: {mp.nstr(v[mp.mpf(10)**3], 5)}, {mp.nstr(v[mp.mpf(10)**6], 5)}; rho1(4c) n^(p-1) -> {mp.nstr(lim, 6)}")
    C_.check(f"[P1e] p={p}: rho1(4c) n^(p-1) -> (kappa/p)(4c)^q1", float(abs(v[mp.mpf(10)**6]*mp.mpf(10)**(6*(p - 1))/lim - 1)), 0.0, 1e-3)
    C_.check(f"[P1e] p={p}: rho1(4c) -> inf with n", float(v[mp.mpf(10)**6] > 10*v[mp.mpf(10)**3]/10 and v[mp.mpf(10)**6] > 10), 1.0, 0.0)

# [P1f]
p = mp.mpf('0.4'); n = mp.mpf(4); kap = mp.mpf('0.3')
ints = {e: mp.quad(lambda u: rho1(mp.e**u, n, p, kap)*mp.e**u, [mp.log(e), mp.log(e)/2, 0]) for e in (mp.mpf('1e-4'), mp.mpf('1e-8'))}
sl = mp.log(ints[mp.mpf('1e-8')]/ints[mp.mpf('1e-4')])/mp.log(mp.mpf('1e4'))
print(f"[P1f] p=0.4: int_eps^1 rho1 at eps = 1e-4, 1e-8: {mp.nstr(ints[mp.mpf('1e-4')], 5)}, {mp.nstr(ints[mp.mpf('1e-8')], 5)}; growth exponent {mp.nstr(sl, 5)} (1/p - 2 = {mp.nstr(1/p - 2, 4)})")
C_.check("[P1f] p=0.4: int rho1 diverges like eps^(2-1/p)", float(sl), float(1/p - 2), 0.02)

# [P1g] 1/2 < p < 1: closed form and unbounded gauge
class KapL:
    def __init__(s, p, d, kap, n=4):
        s.p, s.d, s.k, s.n = mp.mpf(p), mp.mpf(d), mp.mpf(kap), mp.mpf(n); s.zs = s.n**s.p/s.k; s.a = 1 + s.d
    def r1(s, y):
        if s.k > 0 and y > s.zs: return s.n*y**(-1/s.p) - s.d - HALF
        return -s.n*y**(-1/s.p)*mp.expm1(mp.log1p(-y/s.zs)/s.p)
    def rhot(s, y): return HALF + s.d - (s.n**s.p/y - s.k)**(1/s.p)
    def Cr(s, z):
        L = mp.log(abs(z)); A = abs(mp.arg(z)); ex = [sg*e for e in (A, 10*A, 100*A) for sg in (-1, 1) if e < 5]
        f = lambda u: s.r1(mp.e**u)*(1/(mp.e**u - z) - 1/(mp.e**u + 1))*mp.e**u
        lz = mp.log(abs(s.zs))
        pts = sorted(set([mp.mpf(-200), mp.mpf(-40), mp.mpf(0), lz, L - 5, L, L + 5, mp.mpf(500)] + [L + e for e in ex]
                         + ([lz + e for e in (-1e-3, -1e-6, 1e-6, 1e-3)] if s.k > 0 else [])))
        v = mp.quad(f, pts)
        if s.k < 0:
            B = PI - A; exn = [sg*e for e in (B, 10*B, 100*B) for sg in (-1, 1) if e < 5]
            g = lambda u: s.rhot(-mp.e**u)*(1/(-mp.e**u - z) - 1/(-mp.e**u - 1))*mp.e**u
            cand = [lz + mp.mpf('1e-9'), lz + mp.mpf('1e-6'), lz + mp.mpf('1e-3'), lz + 1, L - 5, L, L + 5] + [L + e for e in exn]
            v += mp.quad(g, [lz] + sorted(set(v_ for v_ in cand if v_ > lz)) + [mp.mpf(500)])
        return v
    def g(s, z):
        rm = -s.n*mp.power(-z, -1/s.p)*mp.expm1(mp.log(1 - z/s.zs)/s.p)
        return -mp.zeta(0, s.a)*mp.log(1 - z/s.zs) + PI/mp.sin(PI/s.p)*rm
for kap in (mp.mpf('0.3'), mp.mpf('-0.3')):
    K = KapL(mp.mpf('0.75'), mp.mpf('-0.3'), kap)
    pts = [mp.mpc('0.3', '0.2'), mp.mpc(-1, '0.01'), 2*mp.expjpi(mp.mpf('0.9')), mp.mpc('1.1', '1e-12'), mp.mpc('-0.5', '-1e-12')]
    v = [K.Cr(z) - K.g(z) for z in pts]; sp = max(abs(x - v[0]) for x in v)
    re = [mp.re(K.Cr(mp.mpf('1e-8')*mp.expjpi(ps))) for ps in (mp.mpf('0.5'), mp.mpf('0.95'))]
    re4 = [mp.re(K.Cr(mp.mpf('1e-4')*mp.expjpi(ps))) for ps in (mp.mpf('0.5'), mp.mpf('0.95'))]
    print(f"[P1g] p=0.75 kappa={kap}: closed-form spread {mp.nstr(sp, 3)}; Re C[rho1] at r = 1e-4, 1e-8 on arg pi/2, 0.95 pi: "
          f"{[mp.nstr(x, 5) for x in re4]}, {[mp.nstr(x, 5) for x in re]}")
    C_.check(f"[P1g] p=0.75 kappa={kap}: closed form of Lemma K.1 (numerical, p < 1)", float(sp), 0.0, 1e-15)
    C_.check(f"[P1g] p=0.75 kappa={kap}: |log E_kappa| unbounded near 0 (max |Re C| grows by > 5x from 1e-4 to 1e-8 and exceeds 10)",
             float(max(abs(x) for x in re) > 10 and max(abs(x) for x in re) > 5*max(abs(x) for x in re4)), 1.0, 0.0)
C_.finish()
