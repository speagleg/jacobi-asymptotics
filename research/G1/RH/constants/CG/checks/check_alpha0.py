"""Rule A item 6: alpha = 0 with p != 1, (p,s) = (2,3); also alpha = 4/3 at (3,8). n=40, dps 500 vs 1000."""
import mpmath as mp
from cglib import recurrence, conj_constant, richardson
for (p, s) in [(2, 3), (3, 8)]:
    res = []
    for d in (500, 1000):
        mp.mp.dps = d
        al, be = recurrence(p, s, 40)
        P = [mp.mpf(1)]; h = be[0]; K = mp.mpf(0); r = {}
        C, E = conj_constant(p, s)
        for k in range(40):
            K += P[k] ** 2 / h; r[k + 1] = (1 / K) * mp.mpf(k + 1) ** E / C
            P.append(-al[k] * P[k] - (be[k] * P[k - 1] if k > 0 else 0)); h *= be[k + 1]
        res.append(r)
    r = res[1]
    lim = richardson(r, list(range(40 - 10, 41)), 10)
    mp.mp.dps = 20
    print('p=%s s=%s r_40-1=%s  Richardson(K=10) limit-1=%s  precision-doubling diff=%s' %
          (p, s, mp.nstr(r[40] - 1, 5), mp.nstr(lim - 1, 4), mp.nstr(abs(res[0][40] - res[1][40]), 3)))
