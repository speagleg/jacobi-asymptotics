"""JZC_SIGMA: NUMERICAL (mpmath, 40-50 digits) check of the frame identity of Lemma F to order 8, with the numeric engine
m4_rh4.py (imported, not edited; run(p, al, nu=...): al = the Szego exponent beta (rho^2 and the soft-edge phi-power),
nu = the Bessel order).

Integer layer, B(n; beta, nu) := sum_{k<=KORD} d_k n^{-k}:
  (FI)  B(n + gamma; nu - 2 gamma, nu) = (1 + gamma/n)^p B(n; nu, nu)   coefficientwise in 1/n, k <= 8.
First-order zeta layer (E3 gauge, central differences in mu_j as in m4_shift_zeta.py), E_j(n; beta, nu) := sum_k e_k n^{-k}:
  (FI_j) E_j(n + gamma; nu - 2 gamma, nu) = (1 + gamma/n)^{(j+1)p} E_j(n; nu, nu)    (k <= 6; mu_{m,j} = mu_{n,j}(n/m)^{jp}).
Controls (must fail): half shift beta = nu - gamma; no index shift; no frame factor; Bessel order moved (nu -> nu - 2 gamma);
zeta layer with the integer-layer frame factor (1 + gamma/n)^p.
Points: p in {1.7, 0.6, 3.2, sqrt 2}, nu in {0.3, -0.45}, gamma in {0.37, -0.21, 1, 2.5} (gamma = 1: integer, no lip phase)."""
import os, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "8"); os.environ.setdefault("SHI", "56")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
for fn in (__file__, M.__file__):
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
C_ = Checks()


def shifted(d, g, K):
    """coefficients of sum_k d_k (n+g)^{-k} in powers of 1/n, up to K"""
    return [sum(d[k]*mp.binomial(-k, Kk - k)*g**(Kk - k) for k in range(Kk + 1)) for Kk in range(K + 1)]


def framed(d, g, e, K):
    """coefficients of (1 + g/n)^e sum_k d_k n^{-k}"""
    return [sum(mp.binomial(e, j)*g**j*d[Kk - j] for j in range(Kk + 1)) for Kk in range(K + 1)]


def rel(a, b):
    return max(abs(x - y)/(1 + abs(y)) for x, y in zip(a, b))


K8 = M.KORD
for p in (mp.mpf('1.7'), mp.mpf('0.6'), mp.mpf('3.2'), mp.sqrt(2)):
    for nu in (mp.mpf('0.3'), mp.mpf('-0.45')):
        d0, _ = M.run(p, nu, nu=nu)
        rhs = framed(d0, 0, 0, K8)
        for g in (mp.mpf('0.37'), mp.mpf('-0.21'), mp.mpf(1), mp.mpf('2.5')):
            lab = f"p={mp.nstr(p, 4)} nu={mp.nstr(nu, 3)} gamma={mp.nstr(g, 3)}"
            dg, _ = M.run(p, nu - 2*g, nu=nu)
            res = rel(shifted(dg, g, K8), framed(d0, g, p, K8))
            C_.check(f"{lab}: FI integer layer, k <= {K8}", float(res), 0.0, 1e-25)
            dh, _ = M.run(p, nu - g, nu=nu)
            c1 = rel(shifted(dh, g, K8), framed(d0, g, p, K8))
            c2 = rel(dg, rhs)
            c3 = rel(shifted(dg, g, K8), rhs)
            dn, _ = M.run(p, nu - 2*g, nu=nu - 2*g)
            c4 = rel(shifted(dn, g, K8), framed(d0, g, p, K8))
            for cl, cv in (("half shift", c1), ("no index shift", c2), ("no frame factor", c3), ("Bessel order moved", c4)):
                C_.check(f"{lab}: CONTROL {cl} must fail", float(cv > 1e-6), 1.0, 0.0)
            print(f"{lab}: FI residual {mp.nstr(res, 3)}; controls (half, no-shift, no-frame, nu-moved) "
                  f"{mp.nstr(c1, 3)}, {mp.nstr(c2, 3)}, {mp.nstr(c3, 3)}, {mp.nstr(c4, 3)}", flush=True)

# first-order zeta layer, KORD = 6 (re-import engine at lower order for speed)
M.KORD = 6; K6 = 6
mp.mp.dps = 50; h = mp.mpf(10)**-15
for p in (mp.mpf('1.7'), mp.mpf('0.6')):
    for nu in (mp.mpf('0.3'),):
        for j in (1, 2):
            def resp(beta, nuu):
                a, _ = M.run(p, beta, mu={j: h}, nu=nuu); c, _ = M.run(p, beta, mu={j: -h}, nu=nuu)
                return [(x - y)/(2*h) for x, y in zip(a, c)]
            e0 = resp(nu, nu)
            for g in (mp.mpf('0.37'), mp.mpf('-0.21')):
                lab = f"zeta j={j} p={mp.nstr(p, 3)} nu={mp.nstr(nu, 3)} gamma={mp.nstr(g, 3)}"
                eg = resp(nu - 2*g, nu)
                res = rel(shifted(eg, g, K6), framed(e0, g, (j + 1)*p, K6))
                C_.check(f"{lab}: FI_j, k <= {K6}", float(res), 0.0, 1e-15)
                cw = rel(shifted(eg, g, K6), framed(e0, g, p, K6))
                C_.check(f"{lab}: CONTROL frame factor (1+g/n)^p must fail", float(cw > 1e-6), 1.0, 0.0)
                print(f"{lab}: FI_j residual {mp.nstr(res, 3)}; control (exponent p) {mp.nstr(cw, 3)}", flush=True)
C_.finish()
