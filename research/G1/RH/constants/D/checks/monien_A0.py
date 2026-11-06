"""Prediction of Monien-Zagier's A^(0) (arXiv:0901.1883 eq. after (1.2): H_n^(0) = A^(0) ((2n+1)/e^{3/2})^{-(n+1/2)^2}(1 + 1/(24(2n+1)^2) + ...))
from the conjectural closed form of the constant at p = 1:  Pi(1) = 1/4 - 5 log A + log pi + 5/12 log 2 - 3/8 log 3  (A = Glaisher)."""
import mpmath as mp
mp.mp.dps = 50
p = 1; s = 2; c = mp.mpf(1) / 2; z = mp.mpf(1)
L = mp.log
Pi1 = mp.mpf(1) / 4 - 5 * L(mp.glaisher) + L(mp.pi) + mp.mpf(5) / 12 * L(2) - mp.mpf(3) / 8 * L(3)
kap = L(2 * mp.pi * 3) / 2 + 3 * L(c) / 2
K = Pi1 - L(mp.barnesg(z)) - z * (z - 1) / 2 * L(3) + kap * z
d1 = -mp.mpf(1) / 2; d2 = (p + 1) * (s - 1) ** 2 / mp.mpf(8 * p) - (p + 2) * (s - 1 - p) ** 2 / mp.mpf(8 * p * p) + mp.mpf(p + 1) / 12 - mp.mpf(1) / 12
e = d1 + d1 ** 2 - 2 * d2
def A(n): return (n - 1) * (L(2 * mp.pi / p) + z * L(c)) + (n * n - 1) * L(c) - p * z * mp.loggamma(n) - 2 * p * L(mp.barnesg(n + 1)) + e * L(n)
def MZ(n): return -(n + mp.mpf(1) / 2) ** 2 * L((2 * n + 1) / mp.e ** mp.mpf(1.5))
for n in (10**3, 10**4, 10**5):
    print(n, 'predicted A0 =', mp.nstr(mp.exp(K + A(n) - MZ(n)), 20))
print('Monien-Zagier: A0 ~ 0.351466738331')

# Richardson in 1/n for the predicted log A0, then PSLQ, then Monien's own sample value H_100
ns = [2000 * k for k in range(1, 13)]
vals = {n: K + A(n) - MZ(n) for n in ns}
M = mp.matrix([[mp.mpf(n) ** (-k) for k in range(len(ns))] for n in ns])
logA0 = mp.lu_solve(M, mp.matrix([vals[n] for n in ns]))[0]
print('predicted A0 (extrapolated) =', mp.nstr(mp.exp(logA0), 30))
print('PSLQ log A0 vs [1, log Glaisher, log2, log3, logpi]:', mp.pslq([logA0, 1, L(mp.glaisher), L(2), L(3), L(mp.pi)], maxcoeff=10**4, maxsteps=10**6))
for A0 in (mp.exp(logA0), mp.mpf('0.351466738331')):
    v = A0 * ((201) / mp.e ** mp.mpf(1.5)) ** (-(mp.mpf(100.5)) ** 2) * (1 + mp.mpf(1) / (24 * 201 ** 2))
    print('A0 =', mp.nstr(A0, 12), '-> H_100^(0) ~', mp.nstr(v, 5), '(Monien prints 4.9e-16684)')
