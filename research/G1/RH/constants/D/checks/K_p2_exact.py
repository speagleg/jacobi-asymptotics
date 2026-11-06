"""Pi(2) at s = 2 from Krattenthaler's exact product (Fukuhara-Yang App. A, Thm A), to ~40 digits, vs the PSLQ form
Pi(2) = 6 zeta'(-1) + 5/2 log pi - 89/24 log 2."""
import sys, mpmath as mp
sys.path.insert(0, __file__.rsplit('/', 3)[0] + '/CG/checks'); sys.path.insert(0, '../CG/checks')
from cglib import c_of_p
mp.mp.dps = 200
p = mp.mpf(2); s = mp.mpf(2); c = c_of_p(p); z = (s - 1) / p
d1 = -(s - 1) / 2; d2 = (s * s + 6 * s - 11) / 16; e = d1 + d1 ** 2 - 2 * d2
def logD(n):   # exact: D_n = 2^-n pi^(2n^2) prod_{i=1}^{2n-1} (2i+1)^-(2n-i)
    return -n * mp.log(2) + 2 * n * n * mp.log(mp.pi) - mp.fsum((2 * n - i) * mp.log(2 * i + 1) for i in range(1, 2 * n))
def A(n):
    return (n - 1) * (mp.log(2 * mp.pi / p) + z * mp.log(c)) + (n * n - 1) * mp.log(c) - p * z * mp.loggamma(n) \
        - 2 * p * mp.log(mp.barnesg(n + 1)) + e * mp.log(n)
ns = list(range(300, 301 + 40 * 15, 40)); ks = len(ns)
vals = {n: logD(n) - A(n) for n in ns}
M = mp.matrix([[mp.mpf(n) ** (-k) for k in range(ks)] for n in ns])
K = mp.lu_solve(M, mp.matrix([vals[n] for n in ns]))[0]
kap = mp.log(2 * mp.pi * (p + 2)) / 2 + 3 * mp.log(c) / 2
Pi = K + mp.log(mp.barnesg(z)) + z * (z - 1) / 2 * mp.log(p + 2) - kap * z
guess = 6 * mp.zeta(-1, derivative=1) + mp.mpf(5) / 2 * mp.log(mp.pi) - mp.mpf(89) / 24 * mp.log(2)
print('K(2,2)  =', mp.nstr(K, 45)); print('Pi(2)   =', mp.nstr(Pi, 45)); print('PSLQ    =', mp.nstr(guess, 45)); print('diff    =', mp.nstr(Pi - guess, 5))
