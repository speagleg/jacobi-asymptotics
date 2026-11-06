# (a') precision confirmation for p=0.7 at m=60,70, and an exploratory look at p=0.4 (1/3<p<1/2), where the
# reviewer argues the proved rate is only O(N^-3p) (weight-3 second-order layers), not O(N^-1-p).
import mpmath as mp
from checkA_e2 import resid
for dps in (250, 350):
    r = resid(mp.mpf('0.7'), 2, 70, dps)
    print('p=0.7 s=2 dps', dps, [(m, mp.nstr(rN, 12)) for (m, N, rN, rm) in r[59::10]])
for (pp, ss) in ((mp.mpf('0.4'), mp.mpf(2)), (mp.mpf('0.4'), mp.mpf(3))):
    for dps in (200, 300):
        r = resid(pp, ss, 70, dps)
        print('p=%s s=%s dps %d' % (pp, ss, dps))
        for i in range(19, 70, 10):
            m, N, rN, _ = r[i]; m2, N2, rN2, _ = r[i-10]
            loc = -mp.log(abs(rN/rN2))/mp.log(N/N2)
            print('  m=%d resN=%s  local exponent (m-10..m)=%s  N^1.2 res=%s  N^1.4 res=%s' % (m, mp.nstr(rN, 10), mp.nstr(loc, 6), mp.nstr(rN*N**mp.mpf('1.2'), 8), mp.nstr(rN*N**mp.mpf('1.4'), 8)))
