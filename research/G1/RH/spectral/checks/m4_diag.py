"""JZC M4 §8: the diagonal integer layer (NUMERICAL, 40 digits). n^p alpha_n/(2c) = A(n) from the a-functional
(m4_rh4.run(..., want_a=True)). With the Bessel order nu and the Szego exponent beta decoupled, its natural form
(M/n)^p A(n), M = n + beta/2 + 1 (= N + 1/2), is independent of beta and even in 1/M, and its M^-2 coefficient is
  a2 = -(p+1)/24 + (p+1)(p+2) nu^2/8   (rational reconstruction from p in {1/2,...,6}, nu in {0, 1}; asserted here at fresh
points). Bessel point (2, -1/2): (1 - 1/(4M^2))^{-1}, a2 = 1/4, a4 = 1/16."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "6")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
C_ = Checks(); S = M.S
def nat(A, p, sh):
    S.HI, h0 = M.KORD, S.HI; x = S(1, [1]); one = S.const(1); inv_n = x*(one - x*sh).inv(); tot = S.const(A[0]); q = S.const(1)
    for k in range(1, M.KORD + 1): q = q*inv_n; tot = tot + q*A[k]
    F = (one - x*sh).powr(-p)*tot; S.HI = h0
    return [mp.re(F.get(k)) for k in range(M.KORD + 1)]
for p, nu in [(mp.mpf('7')/3, mp.mpf('0.45')), (mp.mpf('0.7'), mp.mpf('-0.8')), (mp.mpf('4.4'), mp.mpf('1.3'))]:
    ref = None
    for beta in (nu, mp.mpf('0.2'), mp.mpf('-2.6')):
        _, _, A = M.run(p, beta, nu=nu, want_a=True); G = nat(A, p, beta/2 + 1)
        lab = f"p={mp.nstr(p, 4)} nu={mp.nstr(nu, 3)} beta={mp.nstr(beta, 3)}"
        C_.check(f"{lab}: odd coefficients vanish", float(max(abs(G[k]) for k in range(1, M.KORD + 1, 2))), 0.0, 1e-28)
        if ref is None:
            ref = G; a2 = -(p + 1)/24 + (p + 1)*(p + 2)*nu**2/8
            C_.check(f"{lab}: a2 closed form", float(G[2] - a2), 0.0, 1e-28)
            print(f"{lab}: {[mp.nstr(v, 12) for v in G]}", flush=True)
        else:
            C_.check(f"{lab}: independent of beta", float(max(abs(G[k] - ref[k]) for k in range(M.KORD + 1))), 0.0, 1e-28)
_, _, A = M.run(mp.mpf(2), mp.mpf(-0.5), want_a=True); G = nat(A, mp.mpf(2), mp.mpf(-0.5)/2 + 1)
C_.check("Bessel point: (1 - 1/(4M^2))^{-1}", float(abs(G[2] - 0.25) + abs(G[4] - 0.0625) + abs(G[6] - 0.015625)), 0.0, 1e-28)
C_.finish()
