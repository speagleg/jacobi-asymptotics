"""JZC M2.1 check: Theorem K for 0 < p < 1 (seam geometry, E_plt1 Lemma F.1). With theta = p pi/2 and
ell(r) = -log(1 - exp(-2 pi n r^{-1/p})), E3.7's functional on the full band factor is
  e_n = (2cp/pi) int_0^inf ell(r) Im[e^{i theta} k(r e^{i theta})] dr,   k(zeta) = zeta^{-2} (1 - 4c/zeta)^{-3/2},
and the claim is the same Mellin-Barnes form as for p > 1:
  e_n = (1/2 pi i) int_(c0) p W(w) zeta(-wp) n^{-wp} pi [cot(pi w p/2) - cot(pi w)] dw,  0 < c0 < 1,
whose residues are E3's eps_j = C(2j,j) p c^j zeta(-jp)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 20; C_ = Checks()
def cp_(p): I = mp.sqrt(mp.pi)/2*mp.gamma(1/p + mp.mpf(1)/2)/mp.gamma(1/p + 1); return (mp.pi/(2*I))**p/4
W = lambda w, c: (4*c)**w*mp.gamma(w + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(w + 1))
for p, n in ((mp.mpf('0.6'), mp.mpf(10)), (mp.mpf('0.3'), mp.mpf(8)), (mp.mpf('0.75'), mp.mpf(20))):
    c = cp_(p); th = p*mp.pi/2
    ell = lambda r: -mp.log(-mp.expm1(-2*mp.pi*n*r**(-1/p))) if 2*mp.pi*n*r**(-1/p) < mp.mp.prec else mp.mpf(0)
    kk = lambda z: z**-2*(1 - 4*c/z)**-1.5
    f = lambda r: ell(r)*mp.im(mp.exp(1j*th)*kk(r*mp.exp(1j*th)))
    N = n**p
    eq = 2*c*p/mp.pi*mp.quad(f, [0, N/50, N/5, N, 5*N, 50*N, mp.inf])
    g = lambda w: p*W(w, c)*mp.zeta(-w*p)*n**(-w*p)*mp.pi*(mp.cot(mp.pi*w*p/2) - mp.cot(mp.pi*w))
    em = mp.re(mp.quad(lambda t: g(mp.mpf('0.5') + 1j*t), [-40, -10, -3, 0, 3, 10, 40])/(2*mp.pi))
    res = [p*W(j, c)*mp.zeta(-j*p)*n**(-j*p) for j in range(1, 7)]
    print(f"p={p} n={n}: quad {mp.nstr(eq, 16)}  MB {mp.nstr(em, 16)}  residue partial sums {[mp.nstr(sum(res[:k]), 10) for k in (1, 2, 3, 6)]}")
    C_.check(f"Thm K p={p}<1: quad = MB", float(eq), float(em), 1e-13*abs(float(eq)))
C_.finish()
