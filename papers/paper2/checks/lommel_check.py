"""Paper 2, remark after Theorem 2: (p, s) = (2, 2).  Compares the recurrence coefficients of
sigma_{2,2} = sum_k k^{-2} delta_{k^{-2}} (moments m_j = zeta(2j+2)), computed from Hankel determinants in mpmath,
with closed forms built from the Lommel recurrence (Van Assche, arXiv:math/9510214, Section 3, nu = 3/2):
gamma_m := 1/(2 sqrt((m + 1/2)(m + 3/2))), m >= 1 (orthonormal off-diagonal coupling p_{m-1}, p_m).
Paper convention: x P_n = P_{n+1} + a_n P_n + b_n^2 P_{n-1}, b_n^2 = h_n/h_{n-1}; h_n = D_{n+1}/D_n.
Candidates tested: b_n = pi^2 gamma_{2n-1} gamma_{2n}?  b_n = pi^2 gamma_{2n} gamma_{2n+1}?
a_n = pi^2 (gamma_{2n}^2 + gamma_{2n+1}^2)?  a_n = pi^2 (gamma_{2n-1}^2 + gamma_{2n}^2)? (gamma_0 := 0)
Run: <jacobi-asymptotics>/.venv/bin/python -I papers/paper2/checks/lommel_check.py"""
import mpmath as mp

mp.mp.dps = 120
NMAX = 10
mom = [mp.zeta(2 * j + 2) for j in range(2 * NMAX + 3)]
D = [mp.mpf(1)] + [mp.det(mp.matrix([[mom[i + j] for j in range(n)] for i in range(n)])) for n in range(1, NMAX + 3)]
h = [D[n + 1] / D[n] for n in range(NMAX + 1)]
# a_n via the monic recursion: a_n = (coefficient identity) use sum of zeros: a_n = s_{n+1} - s_n, s_n = sum of zeros of P_n
# s_n = -[x^{n-1}] P_n = (det of Hankel with last row shifted)/D_n
def s(n):
    if n == 0:
        return mp.mpf(0)
    M = mp.matrix([[mom[i + j + (1 if i == n - 1 else 0)] for j in range(n)] for i in range(n)])
    return mp.det(M) / D[n]
g = lambda m: mp.mpf(0) if m <= 0 else 1 / (2 * mp.sqrt((m + mp.mpf(1) / 2) * (m + mp.mpf(3) / 2)))  # noqa: E731
P2 = mp.pi ** 2
mx = [0, 0, 0, 0]
for n in range(1, NMAX):
    b = mp.sqrt(h[n] / h[n - 1]); a = s(n + 1) - s(n)
    c1 = P2 * g(2 * n - 1) * g(2 * n); c2 = P2 * g(2 * n) * g(2 * n + 1)
    d1 = P2 * (g(2 * n) ** 2 + g(2 * n + 1) ** 2); d2 = P2 * (g(2 * n - 1) ** 2 + g(2 * n) ** 2)
    errs = [abs(b / c1 - 1), abs(b / c2 - 1), abs(a / d1 - 1), abs(a / d2 - 1)]
    mx = [max(x, y) for x, y in zip(mx, errs)]
    print(n, mp.nstr(b, 15), mp.nstr(a, 15), [mp.nstr(e, 3) for e in errs])
a0 = mom[1] / mom[0]
print("a_0 =", mp.nstr(a0, 15), " pi^2 g_1^2 =", mp.nstr(P2 * g(1) ** 2, 15))
print("max rel errors (b: c1, c2; a: d1, d2):", [mp.nstr(e, 3) for e in mx])
# Simplified closed forms (n >= 1): b_n = pi^2/((4n+1) sqrt((4n-1)(4n+3))), a_n = 2 pi^2/((4n+1)(4n+5)); a_0 = pi^2/15.
mx2 = 0
for n in range(1, NMAX):
    b = mp.sqrt(h[n] / h[n - 1]); a = s(n + 1) - s(n)
    mx2 = max(mx2, abs(b * (4 * n + 1) * mp.sqrt((4 * n - 1) * (4 * n + 3)) / P2 - 1), abs(a * (4 * n + 1) * (4 * n + 5) / (2 * P2) - 1))
print("simplified closed forms, max rel error n = 1..%d:" % (NMAX - 1), mp.nstr(mx2, 3), "; a_0 - pi^2/15 =", mp.nstr(a0 - P2 / 15, 3))
