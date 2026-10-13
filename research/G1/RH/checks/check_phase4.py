"""Plan 10 Phase 4 (NUMERICAL).
[1] Airy edges: (constraint - psi)(x) ~ C sqrt(r* - x) as x -> r*- (ratio to sqrt stabilizes), and psi(r*) finite.
[2] Origin is a regular interior band point: psi(0) = 1/(pi r* (q+1)) > 0.
[3] Top end (p = 2, r in {2, 4}): sup over saturated x in [1.3 r*, k_N] (outside a fixed Airy disc) of
    |theta'(x)/w(x)| * |Dt(x)|^2 * exp(N (l - 2 Re g(x)))  -> 0 exponentially as N grows
    (raw lower-triangular saturated jump entry, without the Szegő/E normalization, so it carries polynomial N-factors;
    inside the fixed disc around r* the Airy parametrix takes over)."""
import mpmath as mp
from jacobi_asym.laws.weyl import c_p

mp.mp.dps = 25


def setup(p):
    q = mp.mpf(p) / 2
    return q, 2 ** (1 + q) * mp.sqrt(c_p(p))


def psi(x, p):
    q, rs = setup(p)
    tx = (rs / abs(x)) ** (1 / q)
    return mp.quad(lambda t: 1 / mp.sqrt((rs * t ** (-q)) ** 2 - x * x), [0, min(mp.mpf(1), tx)]) / mp.pi


def cons(x, p):
    q, _ = setup(p)
    return abs(x) ** (-1 - 1 / q) / q


def reg(x, p):
    q, rs = setup(p)
    return mp.quad(lambda t: mp.re(mp.log((x + x * mp.sqrt(1 - (rs * t ** (-q) / x) ** 2)) / 2)), [0, 1])


for p in (1, 2, 3):
    q, rs = setup(p)
    rat = [mp.nstr((cons(rs * (1 - e), p) - psi(rs * (1 - e), p)) / mp.sqrt(rs * e), 6) for e in (mp.mpf("1e-2"), mp.mpf("1e-4"), mp.mpf("1e-6"))]
    print(f"[1] p={p}: (constraint-psi)/sqrt(r*-x) at r*-x = r*(1e-2,1e-4,1e-6): {rat}")
    print(f"[2] p={p}: psi(0+) = {mp.nstr(psi(mp.mpf('1e-8'), p), 10)}   1/(pi r* (q+1)) = {mp.nstr(1/(mp.pi*rs*(q+1)), 10)}")
p = 2
q, rs = setup(p)
l = 2 * reg(rs * mp.mpf("0.01"), p)
for r in (2, 4):
    for N in (20, 40, 80, 160):
        kN = mp.mpf(N) ** q
        th1 = lambda x: -mp.pi * N / x ** 2          # theta'(x) for theta = pi N / x
        w = lambda x: mp.power(N, q) * mp.power(N / x, -r) / 2
        t = lambda x: N / x
        Dt = lambda x: mp.sqrt(2 * mp.pi) * mp.power(t(x), t(x) - mp.mpf(1) / 2) * mp.exp(-t(x)) / mp.gamma(t(x))
        xs = [rs * mp.mpf("1.3") + (kN - rs * mp.mpf("1.3")) * j / 60 for j in range(61)]
        sup = max(abs(th1(x) / w(x)) * abs(Dt(x)) ** 2 * mp.exp(N * (l - 2 * reg(x, p))) for x in xs)
        print(f"[3] p=2 r={r} N={N}: sup over [1.3 r*, k_N] of |theta'/w| |Dt|^2 e^(N(l-2Re g)) = {mp.nstr(sup, 4)}")
