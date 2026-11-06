"""Independent check (no Theorem C, no functional equation): direct H_n^(0) = det zeta(i+j), H_{n-1}^(1) = det zeta(i+j+1)
from exact moments (Chebyshev algorithm, cglib), divided by Monien-Zagier's asymptotic forms including their printed correction series
(arXiv:0901.1883v1 p.1). Compared with the closed forms A0 = e^{1/12} 2^{1/6} 3^{1/8} / A^3 and A1 = e^{9/8}/sqrt(6) * A0 (A = Glaisher)."""
import sys, mpmath as mp
sys.path.insert(0, '../CG/checks')
from cglib import recurrence
mp.mp.dps = 600
L = mp.log; R = mp.mpf
def logD(s, n):
    al, be = recurrence(1, s, n + 1); lh = L(be[0]); cum = {0: mp.mpf(0)}; c = mp.mpf(0)
    for k in range(1, n + 2): c += lh; cum[k] = c; lh += L(be[k])
    return cum
N = 90
D0 = logD(2, N); D1 = logD(3, N)
A0c = mp.e ** (R(1) / 12) * 2 ** (R(1) / 6) * 3 ** (R(1) / 8) / mp.glaisher ** 3
A1c = mp.e ** (R(9) / 8) / mp.sqrt(6) * A0c
for n in (30, 60, 90):
    x = R(1) / (2 * n + 1)
    corr0 = 1 + x ** 2 / 24 - R(12319) / 259200 * x ** 4 + R(504407873) / 217728 * x ** 6
    a0 = mp.exp(D0[n] + (n + R(1) / 2) ** 2 * L((2 * n + 1) / mp.e ** R(1.5))) / corr0
    y = R(1) / (2 * n)
    corr1 = 1 - R(17) / 240 * y ** 2 - R(199873) / 7257600 * y ** 4 - R(90789413) / 1741824000 * y ** 6
    a1 = mp.exp(D1[n - 1] + (-n * n + R(3) / 4) * -L(2 * n / mp.e ** R(1.5))) / corr1
    print(f"n={n}: A0_direct/A0_closed - 1 = {mp.nstr(a0 / A0c - 1, 4)},  A1_direct/A1_closed - 1 = {mp.nstr(a1 / A1c - 1, 4)}")
print('A0 closed =', mp.nstr(A0c, 25), '  A1 closed =', mp.nstr(A1c, 25))

# Fit A0 and the x^6, x^8, x^10 coefficients from the data instead of using the printed x^6 coefficient
ns = [60, 70, 80, 90]
rows = []; rhs = []
for n in ns:
    x = R(1) / (2 * n + 1)
    base = mp.exp(D0[n] + (n + R(1) / 2) ** 2 * L((2 * n + 1) / mp.e ** R(1.5))) / (1 + x ** 2 / 24 - R(12319) / 259200 * x ** 4)
    rows.append([1, x ** 6, x ** 8, x ** 10]); rhs.append(base)
sol = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
print('fitted A0 =', mp.nstr(sol[0], 25), ' rel. diff to closed form', mp.nstr(sol[0] / A0c - 1, 4))
print('fitted x^6 coefficient (relative) =', mp.nstr(sol[1] / sol[0], 15), ' printed 504407873/217728 =', mp.nstr(R(504407873) / 217728, 15))

# Fully data-driven: A0 * (1 + sum_{k=1..K} a_k x^k), no printed coefficients used; x = 1/(2n+1)
for K in (12, 16):
    ns = list(range(90 - 4 * K, 91, 4))
    M = mp.matrix([[(R(1) / (2 * n + 1)) ** k for k in range(K + 1)] for n in ns])
    v = mp.matrix([mp.exp(D0[n] + (n + R(1) / 2) ** 2 * L((2 * n + 1) / mp.e ** R(1.5))) for n in ns])
    sol = mp.lu_solve(M, v)
    print(f'K={K}: A0 = {mp.nstr(sol[0], 25)}  rel. diff {mp.nstr(sol[0] / A0c - 1, 4)}; a1..a4/A0 =', [mp.nstr(sol[k] / sol[0], 10) for k in range(1, 5)])
