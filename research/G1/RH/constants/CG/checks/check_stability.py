"""Precision-doubling check for the worst-conditioned cases of check_lambda.py (n=80): dps 800 vs 1600."""
import mpmath as mp
from cglib import recurrence, conj_constant
for (p, s) in [(3, "2.5"), (2, "3.5"), ("1.5", "4"), (2, 3)]:
    out = []
    for d in (800, 1600):
        mp.mp.dps = d
        al, be = recurrence(p, s, 80)
        P = [mp.mpf(1)]; h = be[0]; K = mp.mpf(0)
        for k in range(80):
            K += P[k] ** 2 / h
            P.append(-al[k] * P[k] - (be[k] * P[k - 1] if k > 0 else 0)); h *= be[k + 1]
        C, E = conj_constant(p, s)
        out.append((1 / K) * mp.mpf(80) ** E / C)
    mp.mp.dps = 30
    print('p=%s s=%s r_80(dps800) - r_80(dps1600) = %s' % (p, s, mp.nstr(out[0] - out[1], 3)))
