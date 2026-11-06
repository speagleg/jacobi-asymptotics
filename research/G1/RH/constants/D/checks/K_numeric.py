"""Rule N: the constant K(p,s) of log D_n and its periodic part.
log D_n(s) = A_n(s) + K(s) + o(1),
A_n(s) = (n-1)[log(2pi/p) + z log c] + (n^2-1) log c - p z logGamma(n) - 2p log G(n+1) + e(s) log n   (p > 1, no zeta layers at p = 2;
for 1 < p < 2 add the layer sum L_n = -2 eps1/p * sum_{k<n} k^-p, eps1 = 2pc zeta(-p), and K absorbs its constant).
Prediction (functional equation): K(s+p) - K(s) = 1/2 log(2pi(p+2)) + 3/2 log c - z log(p+2) - logGamma(z),  z = (s-1)/p.
Printed: K(s), and Pi(s) := K(s) + log G(z) + z(z-1)/2 log(p+2) - kappa z, kappa = 1/2 log(2pi(p+2)) + 3/2 log c (1-periodic in z)."""
import sys, mpmath as mp
sys.path.insert(0, '../CG/checks'); sys.path.insert(0, __file__.rsplit('/', 3)[0] + '/CG/checks')
from cglib import recurrence, c_of_p

def eval_K(p, s, n, dps, ks=10):
    ks = int(__import__('os').environ.get('KS', ks))
    mp.mp.dps = dps
    p = mp.mpf(p); s = mp.mpf(s); c = c_of_p(p); z = (s - 1) / p
    al, be = recurrence(p, s, n)
    d1 = -(s - 1) / 2
    d2 = (p + 1) * (s - 1) ** 2 / (8 * p) - (p + 2) * (s - 1 - p) ** 2 / (8 * p ** 2) + (p + 1) / 12
    if p == 1: d2 -= mp.mpf(1) / 12          # p = 1: d2(1,s) - 1/12 (PROVED at s = 3/2, 5/2 only; CONJECTURE otherwise)
    e = d1 + d1 ** 2 - 2 * d2
    eps1 = 2 * p * c * mp.zeta(-p) if (1 < p < 2) else 0
    logh = mp.log(be[0]); logD = {}; cum = mp.mpf(0); Lsum = mp.mpf(0)
    for N in range(1, n + 1):
        cum += logh                          # cum = log D_N = sum_{k<N} log h_k
        if N >= 2: Lsum += mp.mpf(N - 1) ** (-p)
        A = (N - 1) * (mp.log(2 * mp.pi / p) + z * mp.log(c)) + (N * N - 1) * mp.log(c) - p * z * mp.loggamma(N) \
            - 2 * p * mp.log(mp.barnesg(N + 1)) + e * mp.log(N) - 2 * eps1 / p * Lsum
        logD[N] = cum - A
        logh += mp.log(be[N])
    ms = list(range(n - ks + 1, n + 1)) if p != 1 else list(range(n - 2 * ks + 2, n + 1, 2))
    gam = [1 + i for i in range(ks - 1)] if eps1 == 0 else sorted(set([k for k in range(1, ks)] + [p - 1 + k for k in range(ks // 2)]))[:ks - 1]
    Am = mp.matrix([[1] + [mp.mpf(k) ** (-g) for g in gam] for k in ms])
    return mp.lu_solve(Am, mp.matrix([logD[k] for k in ms]))[0]

def Pi(p, s, K):
    p = mp.mpf(p); s = mp.mpf(s); c = c_of_p(p); z = (s - 1) / p
    kap = mp.log(2 * mp.pi * (p + 2)) / 2 + 3 * mp.log(c) / 2
    return K + mp.log(mp.barnesg(z)) + z * (z - 1) / 2 * mp.log(p + 2) - kap * z

if __name__ == '__main__':
    p = float(sys.argv[1]); n = int(sys.argv[2]); svals = [float(x) for x in sys.argv[3:]]
    for s in svals:
        D = int(__import__('os').environ.get('DPS', 1500)); K1 = eval_K(p, s, n, D); K2 = eval_K(p, s, n - 10, D)
        print(f"p={p} s={s} z={(s-1)/p:.4f}  K={mp.nstr(K1, 25)}  Pi={mp.nstr(Pi(p, s, K1), 25)}  (n vs n-10: {mp.nstr(K1-K2, 3)})", flush=True)
