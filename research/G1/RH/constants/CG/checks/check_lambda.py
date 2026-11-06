"""Rule N check of Theorem CG (and of the p=1 cases): lambda_m(0; sigma_{p,s}) * m^E / C -> 1.

Usage: python check_lambda.py n dps [i,j,...]   (optional: indices into `pairs`, to run pairs in parallel processes)
Computes lambda_m = 1/K_m(0,0), K_m(0,0) = sum_{k<m} P_k(0)^2/h_k, for m <= n+1, at precision dps and 2*dps
(precision doubling), prints raw ratio r_m = lambda_m m^E / C at a few m, and Richardson limits of r_m in powers of 1/m.
Also prints the profile check (step S7): P*_m(x) = K_m(x,0)/K_m(0,0) at x = w/(m^{p+2}|f'(0)|), compared with
Gamma(al+2) w^{-(al+1)/2} J_{al+1}(2 sqrt w).
"""
import sys
import mpmath as mp
from cglib import recurrence, christoffel_at, conj_constant, richardson, c_of_p

n = int(sys.argv[1]); dps = int(sys.argv[2])
pairs = [(2, '3.5'), (3, '2.5'), ('0.5', '1.3'), ('0.5', '2.5'), ('1.5', '4'), ('0.7', '1.2'), (2, 2),
         (1, '1.5'), (1, '2.5'), (1, 2), (1, '3.7')]


def run(p, s, d):
    mp.mp.dps = d
    p = mp.mpf(p); s = mp.mpf(s)
    al = (s - 1 - p) / p
    alpha, beta = recurrence(p, s, n)
    C, E = conj_constant(p, s)
    fp = 1 / (c_of_p(p) * (p + 2) ** 2)
    m = n + 1
    w = mp.mpf('2.5')
    x = w / (mp.mpf(m) ** (p + 2) * fp)
    P0, Px, h = christoffel_at(x, alpha, beta, m)
    K = mp.mpf(0); Kx = mp.mpf(0); r = {}
    for k in range(m):
        K += P0[k] ** 2 / h[k]
        Kx += P0[k] * Px[k] / h[k]
        r[k + 1] = (1 / K) * mp.mpf(k + 1) ** E / C
    prof = Kx / K
    prof_model = mp.gamma(al + 2) * w ** (-(al + 1) / 2) * mp.besselj(al + 1, 2 * mp.sqrt(w))
    return r, prof, prof_model


sel = [int(i) for i in sys.argv[3].split(',')] if len(sys.argv) > 3 else range(len(pairs))
for (p, s) in [pairs[i] for i in sel]:
    r1, pr1, pm = run(p, s, dps)
    r2, pr2, _ = run(p, s, 2 * dps)
    mp.mp.dps = 2 * dps
    m = n + 1
    stab = max(abs(r1[k] - r2[k]) for k in r1)
    ext = [richardson(r2, list(range(m - K, m + 1)), K) for K in (4, 8, 12)]
    print('p=%s s=%s  raw r_m-1 at m=%d,%d,%d: %s %s %s | precision-doubling diff %s' %
          (p, s, m // 4, m // 2, m, mp.nstr(r2[m // 4] - 1, 4), mp.nstr(r2[m // 2] - 1, 4), mp.nstr(r2[m] - 1, 4),
           mp.nstr(stab, 3)))
    print('      Richardson(1/m, K=4,8,12) limit-1: %s %s %s ;  m*(r_m-1)=%s' %
          tuple([mp.nstr(e - 1, 4) for e in ext] + [mp.nstr(m * (r2[m] - 1), 6)]))
    print('      profile P*(x) at w=2.5: %s  Bessel model %s  diff %s' %
          (mp.nstr(pr2, 10), mp.nstr(pm, 10), mp.nstr(pr2 - pm, 3)))
