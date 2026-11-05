"""JZC M4 §7: the shift structure extends to the zeta layer (NUMERICAL, 50 digits). With the Bessel order nu and the Szego
exponent beta decoupled and the E3 band-factor gauge to first order in mu_j (central differences), the natural-form response
(N/n)^{(j+1)p} sum_k e_k n^{-k}, N = n + beta/2 + 1/2, is independent of beta (j = 1, 2; KORD = 5), and its odd relative
coefficients vanish."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "5")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
mp.mp.dps = 50; C_ = Checks()
def toN(e, p, beta, pw):
    delta = beta/2 + mp.mpf(1)/2; S = M.S; S.HI, h0 = M.KORD, S.HI
    x = S(1, [1]); one = S.const(1); inv_n = x*(one - x*delta).inv()
    tot = S.const(e[0]); q = S.const(1)
    for k in range(1, M.KORD + 1): q = q*inv_n; tot = tot + q*e[k]
    F = (one - x*delta).powr(-pw)*tot; S.HI = h0
    return [mp.re(F.get(k)) for k in range(M.KORD + 1)]
h = mp.mpf(10)**-15
for p in (mp.mpf('1.7'), mp.mpf('0.6')):
    for nu in (mp.mpf('0.3'), mp.mpf('0.8')):
        for j in (1, 2):
            ref = None
            for beta in (nu, mp.mpf('0.9'), mp.mpf('-2.1')):
                a, _ = M.run(p, beta, mu={j: h}, nu=nu); c, _ = M.run(p, beta, mu={j: -h}, nu=nu)
                g = toN([(x - y)/(2*h) for x, y in zip(a, c)], p, beta, (j + 1)*p)
                lab = f"p={mp.nstr(p, 3)} nu={mp.nstr(nu, 3)} j={j} beta={mp.nstr(beta, 3)}"
                C_.check(f"{lab}: odd relative coefficients (N^-(2+jp), N^-(4+jp)) vanish", float(abs(g[2]) + abs(g[4])), 0.0, 1e-20)
                if ref is None: ref = g; print(f"{lab}: {[mp.nstr(x, 12) for x in g]}", flush=True)
                else: C_.check(f"{lab}: response independent of beta", float(max(abs(g[k] - ref[k]) for k in (1, 3, 5))), 0.0, 1e-15)
C_.finish()
