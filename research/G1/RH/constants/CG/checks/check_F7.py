"""Rule N check for CG.md §11 (N-centring, Theorem F7).
Prediction (p != 1, p > 1/3): log(lambda_m N^E / C) = O(N^-2 + N^-1-p), N = m + (s-1)/(2p);
for p > 1: lambda_m = C N^-E (1 + e2 N^-2 + O(N^-min(4,1+p))),
  e2 = E[(2p+1)(p+2)z^2 + p^2 - p - 1] / (24(3p+2)),  z = (s-1)/p, E = (p+2)z.
Printed: N^2 * log(r_m), r_m = lambda_m N^E / C, and an exponent-aware extrapolation; dps-doubling check."""
import sys, mpmath as mp
from cglib import recurrence, christoffel_at, conj_constant

def logr(p, s, M, dps):
    mp.mp.dps = dps
    p = mp.mpf(p); s = mp.mpf(s)
    al, be = recurrence(p, s, M + 1)
    P0, _, h = christoffel_at(0, al, be, M + 1)
    C, E = conj_constant(p, s)
    K = mp.mpf(0); out = {}
    for m in range(1, M + 1):
        K += P0[m - 1] ** 2 / h[m - 1]
        N = m + (s - 1) / (2 * p)
        out[m] = mp.log(1 / K * N ** E / C)
    return out

def e2(p, s):
    p = mp.mpf(p); s = mp.mpf(s); z = (s - 1) / p; E = (p + 2) * z
    return E * ((2 * p + 1) * (p + 2) * z ** 2 + p ** 2 - p - 1) / (24 * (3 * p + 2))

def fit(vals, ms, gams):
    A = mp.matrix([[1] + [mp.mpf(k) ** (-g) for g in gams] for k in ms])
    return mp.lu_solve(A, mp.matrix([vals[k] for k in ms]))[0]

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    cases = [(2, 2), (2, 3), (3, 2.5), (2.5, 4), (4, 3), (1.5, 2.5)]
    for (p, s) in cases:
        o1 = logr(p, s, M, 1200); o2 = logr(p, s, M, 2400)
        dd = max(abs(o1[m] - o2[m]) for m in range(M // 2, M + 1))
        q = {m: o2[m] * (m + mp.mpf(s - 1) / (2 * p)) ** 2 for m in o2}
        gams = [2, 4] if p >= 3 else ([2] if p == 2 else [p - 1, 1, 2])
        ms = [M - 6 * i for i in range(len(gams), -1, -1)]
        print(f"(p,s)=({p},{s}) predicted e2={mp.nstr(e2(p, s), 12)}  N^2 log r_m:",
              '  '.join(f"{m}:{mp.nstr(q[m], 10)}" for m in (M // 4, M // 2, M)),
              f"| extrap {mp.nstr(fit(q, ms, gams), 10)} | dps-diff {mp.nstr(dd, 3)}", flush=True)
    for (p, s) in [(0.5, 2.5), (0.4, 1.8), (0.7, 1.6), (0.3, 1.5), (0.25, 1.6)]:
        o2 = logr(p, s, M, 1200); o1 = logr(p, s, M, 600)
        dd = max(abs(o1[m] - o2[m]) for m in range(M // 2, M + 1))
        print(f"(p,s)=({p},{s}) N*log r_m (prediction -> 0 like N^-min(1,p)):",
              '  '.join(f"{m}:{mp.nstr(o2[m] * (m + mp.mpf(s - 1) / (2 * p)), 8)}" for m in (M // 8, M // 4, M // 2, M)),
              f"| dps-diff {mp.nstr(dd, 3)}", flush=True)
