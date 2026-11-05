"""JZC M4 §7: numerical (40-digit) check of the shift and reflection structure at higher order (KORD = 8), with the Bessel
order nu and the Szego exponent beta decoupled (m4_rh4.run(..., nu=...): beta = the 'al' argument enters rho^2 and the soft-edge
phi-power; nu enters the Bessel coefficients).
Checks: (R) d_k(-beta-2, nu) = (-1)^k d_k(beta, nu); (S) the natural-form f_k (N = n + beta/2 + 1/2) do not depend on beta;
odd f_k vanish; f_k at nu = beta reproduce m4_rh4.f4_closed / f6_closed."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "8"); os.environ.setdefault("SHI", "56")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
C_ = Checks()
for p in (mp.mpf('1.7'), mp.mpf('0.6'), mp.mpf('3.2')):
    for nu in (mp.mpf('0.3'), mp.mpf('-0.45'), mp.mpf('1.6')):
        ref = None
        for beta in (nu, mp.mpf('0.9'), mp.mpf('-1.7'), mp.mpf('2.4')):
            d, _ = M.run(p, beta, nu=nu); f = M.natural(d, p, beta)
            dr, _ = M.run(p, -beta - 2, nu=nu)
            lab = f"p={mp.nstr(p, 3)} nu={mp.nstr(nu, 3)} beta={mp.nstr(beta, 3)}"
            C_.check(f"{lab}: reflection", float(max(abs(dr[k] - (-1)**k*d[k])/(1 + abs(d[k])) for k in range(M.KORD + 1))), 0.0, 1e-25)
            C_.check(f"{lab}: odd f_k = 0", float(max(abs(f[k]) for k in range(1, M.KORD + 1, 2))), 0.0, 1e-25)
            if ref is None:
                ref = f
                C_.check(f"{lab}: f4, f6 closed forms at nu = beta", float(abs(f[4] - M.f4_closed(p, nu)) + abs(f[6] - M.f6_closed(p, nu))), 0.0, 1e-25)
            else:
                C_.check(f"{lab}: f_k independent of beta", float(max(abs(f[k] - ref[k]) for k in range(M.KORD + 1))), 0.0, 1e-25)
        print(f"p={mp.nstr(p, 3)} nu={mp.nstr(nu, 3)}: f = {[mp.nstr(x, 12) for x in ref]}", flush=True)
C_.finish()
