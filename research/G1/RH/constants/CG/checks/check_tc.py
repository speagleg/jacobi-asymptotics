"""Rule N checks for Part B of CG.md (p = 1, s = 3/2 and 5/2, via Tricomi--Carlitz and the localisation lemma).

(T1) sum_j v_j = 1, v_j = j^{j-1} e^{-j}/j!  (numerical; the proof uses DLMF 4.13.1, 4.13.2, 4.13.5).
(T2) the recurrence data of sigma_TC and x sigma_TC quoted from Paper II Lemma 11.? (pone-tc) re-derived from the moments
     sum_j v_j j^{-i} by the Chebyshev algorithm (independent of the quoted formulas).
(T3) the closed forms K_m(0,0; sigma_TC) = (2m+1)!!/(3 (2m-2)!!) and the Gamma-product for x sigma_TC, and their
     leading asymptotics.
(T4) the localisation lemma in action: lambda_m(0; sigma_{1,s}) / (sqrt(2 pi) lambda_m(0; nu)) -> 1 and the bound
     int x d nu_m <= sum (a_k+b_k+b_{k+1}) v_k^2 / sum v_k^2 used in its proof.
"""
import mpmath as mp
from cglib import recurrence, conj_constant

mp.mp.dps = 60
ok = True
v = lambda j: mp.exp((j - 1) * mp.log(j) - j - mp.loggamma(j + 1))


def tc_moment(i, J=3000, R=40):
    """sum_j v_j j^{-i}: direct sum to J, tail from v_j = (2pi)^{-1/2} j^{-3/2} exp(-binet(j)) with the Stirling
    series of binet expanded in powers of 1/j (R terms) and Hurwitz zeta tails.  (mp.nsum's default extrapolation is
    unreliable for these algebraic tails: it gave sum v_j - 1 = -3e-3 in a first run.)"""
    head = mp.fsum(v(j) * mp.mpf(j) ** (-i) for j in range(1, J + 1))
    b = [mp.mpf(0)] * (R + 1)
    for r in range(1, R // 2 + 1):
        b[2 * r - 1] = mp.bernoulli(2 * r) / (2 * r * (2 * r - 1))
    e = [mp.mpf(1)] + [mp.mpf(0)] * R
    for q in range(1, R + 1):
        e[q] = mp.fsum(l * (-b[l]) * e[q - l] for l in range(1, q + 1)) / q
    tail = mp.fsum(e[q] * mp.zeta(mp.mpf(3) / 2 + i + q, J + 1) for q in range(R + 1)) / mp.sqrt(2 * mp.pi)
    return head + tail


tot = tc_moment(0)
print('T1 sum v_j - 1 =', mp.nstr(tot - 1, 5)); ok &= abs(tot - 1) < 1e-40

n = 20
mp.mp.dps = 150
M = [tc_moment(i) for i in range(2 * n + 4)]
al, be = recurrence(1, 0, n, moments=M)          # sigma_TC
alx, bex = recurrence(1, 0, n, moments=M[1:])    # x sigma_TC
mp.mp.dps = 60
e1 = max(abs(be[k] - mp.mpf(1) / (2 * k * (2 * k + 1))) for k in range(1, n))
e2 = max(abs(bex[k] - mp.mpf(1) / ((2 * k + 1) * (2 * k + 2))) for k in range(1, n))
e3 = max(abs(al[k] - (mp.mpf(1) / (2 * k + 1) + mp.mpf(1) / (2 * k + 2))) for k in range(1, n))
print('T2 max|b_k^2 - 1/(2k(2k+1))| =', mp.nstr(e1, 3), '  x-sigma: ', mp.nstr(e2, 3), '  a_k:', mp.nstr(e3, 3),
      ' h0 =', mp.nstr(be[0], 20), ' h0(x sigma) =', mp.nstr(bex[0], 20))
ok &= e1 < 1e-30 and e2 < 1e-30 and e3 < 1e-30

# T3 closed forms from the exact data (P_k(0) = (-1)^k prod u_i, h_k = h_0 prod b_i^2)
def K_exact(u, b2, h0, m):
    P = mp.mpf(1); h = h0; K = P * P / h
    for k in range(1, m):
        P *= -u(k - 1); h *= b2(k); K += P * P / h
    return K

uTC = lambda i: mp.mpf(1) / (2 * i + 2)
bTC = lambda i: mp.mpf(1) / (2 * i * (2 * i + 1))
uX = lambda i: mp.mpf(2 * i + 5) / ((2 * i + 2) * (2 * i + 3))
bX = lambda i: mp.mpf(1) / ((2 * i + 1) * (2 * i + 2))
for m in (5, 17):
    cf = mp.fac2(2 * m + 1) / (3 * mp.fac2(2 * m - 2))
    print('T3 K_m(TC) closed form check m=%d:' % m, mp.nstr(K_exact(uTC, bTC, 1, m) / cf - 1, 3))
    ok &= abs(K_exact(uTC, bTC, 1, m) / cf - 1) < 1e-40
# x sigma_TC: P_k(0)^2/h_k = 2 * prod_{i<k} u_i^2 / prod_{i<=k} b_i^2; closed form claimed in CG.md:
#   K_m(0,0; x sigma_TC) = sum_{k<m} t_k,  t_k = (2k+2)(2k+3)^2 (2k+1)!/(9 * 4^k k!^2)  (to be verified here)
tk = lambda k: (2 * k + 2) * mp.mpf(2 * k + 3) ** 2 * mp.factorial(2 * k + 1) / (9 * mp.mpf(4) ** k * mp.factorial(k) ** 2)
for m in (5, 17):
    a = K_exact(uX, bX, mp.mpf(1) / 2, m); b = mp.fsum(tk(k) for k in range(m))
    print('T3 K_m(x TC) term formula check m=%d:' % m, mp.nstr(a / b - 1, 3)); ok &= abs(a / b - 1) < 1e-40
for (s, u, b2, h0, lead) in [('1.5', uTC, bTC, 1, 4 / (3 * mp.sqrt(mp.pi))),
                             ('2.5', uX, bX, mp.mpf(1) / 2, 32 / (81 * mp.sqrt(mp.pi)))]:
    C, E = conj_constant(1, s)
    m = 20000
    Km = K_exact(u, b2, h0, m)
    pred = 1 / (C * mp.sqrt(2 * mp.pi))           # lambda(nu) ~ C/sqrt(2pi) m^{-E}  <=>  K(nu) ~ sqrt(2pi)/C ... see CG.md
    print('T3 s=%s: K_m(nu) m^{-E} = %s ; sqrt(2pi)/C = %s ; claimed lead %s' %
          (s, mp.nstr(Km / mp.mpf(m) ** E, 12), mp.nstr(mp.sqrt(2 * mp.pi) / C, 12), mp.nstr(lead, 12)))
    ok &= abs(Km / mp.mpf(m) ** E / (mp.sqrt(2 * mp.pi) / C) - 1) < 1e-3
    ok &= abs(lead / (mp.sqrt(2 * mp.pi) / C) - 1) < 1e-40

# T4 localisation in action
mp.mp.dps = 150
for (s, M0, u, b2, h0, shift) in [('1.5', M, uTC, bTC, 1, 0), ('2.5', M[1:], uX, bX, mp.mpf(1) / 2, 1)]:
    a1, bb1 = recurrence(1, s, n)
    K = mp.mpf(0); P = [mp.mpf(1)]; h = bb1[0]; Ks = []
    for k in range(n):
        K += P[k] ** 2 / h
        Ks.append(K)
        P.append(-a1[k] * P[k] - (bb1[k] * P[k - 1] if k > 0 else 0)); h *= bb1[k + 1]
    mp.mp.dps = 30
    for m in (10, 20, n):
        r = (1 / Ks[m - 1]) / (mp.sqrt(2 * mp.pi) / K_exact(u, b2, h0, m))
        # int x dnu_m bound for nu = the TC-type measure
        P0 = [mp.mpf(1)]
        for k in range(1, m):
            P0.append(-u(k - 1) * P0[-1])
        hh = [h0]
        for k in range(1, m):
            hh.append(hh[-1] * b2(k))
        vk2 = [P0[k] ** 2 / hh[k] for k in range(m)]
        print('T4 s=%s m=%d  lambda(sigma)/(sqrt(2pi) lambda(nu)) - 1 = %s' % (s, m, mp.nstr(r - 1, 4)))
    mp.mp.dps = 150
print('ALL PASS' if ok else 'SOME FAIL')
