"""Quantum bouncer: lam'_k = -a_k/(3pi/2)^{2/3} = (k-1/4)^{2/3}(1 + O(k^-2)), p = 2/3. Prediction (node-zeta conjecture):
d1 = -p alpha/2 + p Z(0), Z(0) = zeta(0, 3/4) = -1/4;  eps_j = C(2j,j) p c^j Z(-j), Z(-j) Hurwitz-regularised via the DLMF series."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_common import *
from spec_common import Checks
from spec_airy import zeros, TC
s = float(sys.argv[1]); p = 2/3; pm = mp.mpf(2)/3; K = 200*NMAX
mp.mp.dps = 40
C = (3*mp.pi/2)**pm; q = (3*mp.pi/2)**-2
def Zneg(j, kex=200):
    # lam'^j = (k-1/4)^{jp} (sum_i TC_i q^i u^i)^j, u = (k-1/4)^-2; gamma_i = coefficients of u^i, i <= 5
    poly = [TC[i]*q**i for i in range(6)]
    g = [mp.mpf(1)] + [mp.mpf(0)]*5
    for _ in range(j):
        g = [sum(g[a]*poly[i-a] for a in range(i+1)) for i in range(6)]
    reg = sum(g[i]*mp.zeta(2*i - j*pm, mp.mpf(3)/4) for i in range(6))
    corr = sum((-mp.airyaizero(k)/C)**j - sum(g[i]*(k-mp.mpf(1)/4)**(j*pm-2*i) for i in range(6)) for k in range(1, kex+1))
    return reg + corr
Z1, Z2 = Zneg(1), Zneg(2)
c = c_p_mp(p)
lam = zeros(K)/float(C)
n, y = run(f"bouncer_s{s}", lam, p, s, -0.25, K)
alpha = (s-1-p)/p
d1 = -p*alpha/2 - p/4
e1 = float(2*p*c*Z1); e2 = float(6*p*c**2*Z2)
v1, h1 = fit(n, y, p, [], 1.0)
v, h = fit(n, y - d1/n, p, [1.0], 1+p)
r2 = y - d1/n - e1*n**(-1-p)
w, hw = fit(n, r2, p, [1.0, 1+p], 1+2*p)
print(f"bouncer s={s}: Z(-1) = {mp.nstr(Z1, 15)}, Z(-2) = {mp.nstr(Z2, 15)}")
print(f"  d1 fit {v1:+.8f} ({h1:.1e}) pred {d1:+.8f} [pure-lattice value {-(s-1)/2:+.4f}]")
print(f"  n^-1-p fit {v:+.7f} ({h:.1e}) pred eps1 {e1:+.7f} diff {v-e1:+.1e} [Hurwitz-only {float(2*p*c*mp.zeta(-pm, 0.75)):+.7f}]")
print(f"  n^-1-2p fit {w:+.6f} ({hw:.1e}) pred eps2 {e2:+.6f} diff {w-e2:+.1e}", flush=True)
# pass/fail (REVIEW_SPEC2_B F4): |fit - prediction| <= max(3 * fit half-range, floor)
C_ = Checks(); C_.check(f"d1 s={s}", v1, d1, max(3*h1, 1e-5)); C_.check(f"eps1 s={s}", v, e1, max(3*h, 1e-4)); C_.finish()
