# (b) Pi_2 at a new s (3.3; zeta = 1.15) from the reviewer's own Hankel code, A_n of D.md §3.1, the Barnes form of §3.2,
# compared with the PSLQ closed form Pi(2) = 1/2 - 6 log A + (5/2) log pi - (89/24) log 2 and the recorded -0.70112294215566899568.
import mpmath as mp
from hank import run, cfun
def Pi(p, s, n, dps, nfit):
    Dg, y, lam, logD = run(p, s, n, dps)
    p = mp.mpf(p); s = mp.mpf(s); c = cfun(p); z = (s-1)/p
    d1 = -(s-1)/2
    d2 = (p+1)*(s-1)**2/(8*p) - (p+2)*(s-1-p)**2/(8*p**2) + (p+1)/12
    e = d1 + d1**2 - 2*d2
    vals = []
    for nn in range(1, n+1):
        nn_ = mp.mpf(nn)
        A = (nn_-1)*(mp.log(2*mp.pi/p) + z*mp.log(c)) + (nn_**2-1)*mp.log(c) - p*z*mp.loggamma(nn_) - 2*p*mp.log(mp.barnesg(nn_+1)) + e*mp.log(nn_)
        vals.append(logD[nn-1] - A)
    # extrapolate K: vals_n = K + sum_k a_k n^-k (p = 2: zeta(-2j) = 0, integer powers only); exact solve on last nfit points
    pts = list(range(n-nfit+1, n+1))
    M = mp.matrix([[mp.mpf(nn)**(-k) for k in range(nfit)] for nn in pts]); b = mp.matrix([vals[nn-1] for nn in pts])
    K = mp.lu_solve(M, b)[0]
    kap = mp.log(2*mp.pi*(p+2))/2 + mp.mpf(3)/2*mp.log(c)
    Pi_ = K + mp.log(mp.barnesg(z)) + z*(z-1)/2*mp.log(p+2) - kap*z
    return K, Pi_, vals
mp.mp.dps = 50
closed = mp.mpf(1)/2 - 6*mp.log(mp.glaisher) + mp.mpf(5)/2*mp.log(mp.pi) - mp.mpf(89)/24*mp.log(2)
print('closed form Pi(2) =', mp.nstr(closed, 25), ' recorded: -0.70112294215566899568')
for (n, dps, nfit) in ((60, 700, 20), (70, 900, 24), (70, 1100, 28)):
    K, P, vals = Pi(2, mp.mpf('3.3'), n, dps, nfit)
    mp.mp.dps = 50
    print('n<=%d dps %d nfit %d: K(2,3.3)=%s  Pi=%s  Pi-closed=%s' % (n, dps, nfit, mp.nstr(K, 25), mp.nstr(P, 25), mp.nstr(P-closed, 3)))
# control: same at s = 2 (zeta = 1/2), where D.md has Pi(2) proved-mod-cite via Krattenthaler
K, P, vals = Pi(2, 2, 60, 700, 20); mp.mp.dps = 50
print('control s=2: Pi=%s  Pi-closed=%s' % (mp.nstr(P, 25), mp.nstr(P-closed, 3)))
# FE direct check without Barnes form: K(2,5.3)-K(2,3.3) vs RHS of FE at zeta=1.15
K1, _, _ = Pi(2, mp.mpf('3.3'), 60, 700, 20); K2, _, _ = Pi(2, mp.mpf('5.3'), 60, 700, 20); mp.mp.dps = 50
p = mp.mpf(2); c = cfun(p); z = mp.mpf('1.15')
rhs = mp.log(2*mp.pi*(p+2))/2 + mp.mpf(3)/2*mp.log(c) - z*mp.log(p+2) - mp.loggamma(z)
print('FE: K(2,5.3)-K(2,3.3) =', mp.nstr(K2-K1, 25), ' RHS =', mp.nstr(rhs, 25), ' diff =', mp.nstr(K2-K1-rhs, 3))
