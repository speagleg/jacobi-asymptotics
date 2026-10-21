"""M1.2 check (JZC_M1.md, Proposition M1.2): the continuum soft-edge root a_n carries the pole terms of Z with the pi cot kernel.
Continuum count N(lambda) of lam_k = (k + g/k^m)^p to first order in g: dN = [(1/p) lam^{1/p-1} + (m g/p) lam^{-(m+1)/p... ] -- written via
the index function kappa(lam) = lam^{1/p} - g lam^{-m/p} + O(g^2), dN = kappa'(lam) d lam on lam >= 1.
Soft-edge condition: int_1^{1/A} (1 - A lam)^{-1/2} dN(lam) = n,  A = 4c(1 + eta)/n^p.
Prediction (Prop. E / M1.2, first order in g): the g-part of n*eta contains p R W(q) pi cot(pi q) n^{-pq}, q = m/p, R = -m g/p;
extracted by antisymmetrising in g and fitting n*eta_odd(n) = C n^{-pq} + sum_j c_j n^{-jp} (integer terms depend on the cutoff)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp, numpy as np
from spec_common import Checks, c_p_mp
mp.mp.dps = 30; C_ = Checks()
for p, m in ((mp.mpf('1.5'), mp.mpf('0.5')), (mp.mpf('0.75'), mp.mpf('0.25')), (mp.mpf('1.25'), mp.mpf('0.5')), (mp.mpf('1.8'), mp.mpf('0.75'))):   # m not 1: pq = m must not hit the n^-1 cross term
    c = c_p_mp(float(p)); c = mp.mpf(c); q = m/p
    W = lambda w: (4*c)**w*mp.gamma(w + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(w + 1))
    def eta(n, g):
        dN = lambda lam: lam**(1/p - 1)/p + g*(m/p)*lam**(-m/p - 1)
        def G(e):
            A = 4*c*(1 + e)/n**p
            # int_1^{1/A} (1 - A lam)^{-1/2} dN, substitute lam = (1 - v^2)/A
            f = lambda v: 2*v*(1/v)*dN((1 - v*v)/A)/A
            return mp.quad(f, [0, mp.sqrt(1 - A)/2, mp.sqrt(1 - A)]) - n
        return mp.findroot(G, mp.mpf(0))
    ns = [int(round(100*2**(k/4))) for k in range(0, 25)]; g = mp.mpf('1e-6')   # n = 100 ... 6400
    odd = np.array([float(n*(eta(n, g) - eta(n, -g))/(2*g)) for n in ns]); nn = np.array(ns, dtype=float)
    pred = float(p*(-m/p)*W(q)*mp.pi*mp.cot(mp.pi*q))
    cand = [0.0, 1.0, float(p*q + 1), 2.0] + [float(j*p) for j in (1, 2, 3)] + [float(p*q + j*p) for j in (1, 2)] + [float(1 + j*p) for j in (1, 2)]
    E = [float(p*q)]
    for e in sorted(cand):
        if all(abs(e - x) > 1e-9 for x in E) and e < 4.5: E.append(e)
    # n^0: the count change (j = 0 term); n^-1, n^-1-pq: cross terms with the lattice part's own 1/n correction
    Am = np.vstack([nn**-e for e in E]).T; co = np.linalg.lstsq(Am, odd, rcond=None)[0]
    print(f"p={p} m={m}: q={mp.nstr(q, 4)}; fitted coefficient of n^-pq in n*eta_odd: {co[0]:+.8f}   predicted p R W(q) pi cot(pi q) = {pred:+.8f}")
    C_.check(f"continuum pole term p={p} m={m}", co[0], pred, 2e-3*abs(pred))
C_.finish()
