"""Rule N checks of the algebraic/analytic identities used in CG.md (steps S3, S5, S6).

(I1) |f'(0)| = pi^2 C_*^2 = 1/(c(p)(p+2)^2), with f'(0) computed from the equilibrium measure
     mu*((0,x]) = x^{1/2} a(x), f'(0) = -pi^2 a(0)^2/4 (Paper II Lemma 4.? (signs)(iii)), a(0) from quadrature of psi*.
(I2) det[bhat'(0), bhat(0)] = 2 pi i/(Gamma(al+1)Gamma(al+2)), bhat from the series (10.25.2), checked against
     mpmath besseli at small zeta as well.
(I3) Laguerre calibration: lambda_n(0; x^a e^{-x}dx) = Gamma(a+1)Gamma(a+2)Gamma(n)/Gamma(n+a+1)  (exact), i.e.
     ~ Gamma(a+1)Gamma(a+2) n^{-a-1}; computed from the explicit Laguerre data.
(I4) The scalar identity F*Wtilde = upsilon * wn^{1/2} (-z)^{alpha/2} (p>1, C_+) is checked by evaluating the factors
     D = upsilon*exp(-j(t)), K, Wtilde = wn^{1/2}(-z)^{al/2}(4c-z)^{1/2} e^{-G}, G = -j(t) + log B at a test point with an
     arbitrary value for log B (it cancels identically; this is a bookkeeping check of branches only).
"""
import mpmath as mp
from cglib import c_of_p

mp.mp.dps = 40
ok = True

# (I1)
for p in [mp.mpf('0.5'), mp.mpf('0.7'), mp.mpf(1), mp.mpf('1.5'), mp.mpf(2), mp.mpf(3)]:
    c = c_of_p(p)
    astar = 1 / p + mp.mpf(1) / 2
    psi = lambda x: (1 / p) * x ** (-1 - 1 / p) * mp.betainc(astar, mp.mpf(1) / 2, 0, x / (4 * c), regularized=True)
    vals = []
    xs = [mp.mpf(10) ** (-k) for k in (6, 7, 8)]
    for x in xs:
        mass = mp.quad(psi, [0, x])
        vals.append(mass / mp.sqrt(x))
    a0 = vals[-1]
    fprime = -mp.pi ** 2 * a0 ** 2 / 4
    target = 1 / (c * (p + 2) ** 2)
    Cstar = (4 * c) ** (-1 / p - mp.mpf(1) / 2) / (p * astar * mp.beta(astar, mp.mpf(1) / 2))
    r1 = abs(-fprime / target - 1); r2 = abs(mp.pi ** 2 * Cstar ** 2 / target - 1)
    print('I1 p=%s  |f\'(0)|*c(p+2)^2-1 = %s (quadrature at x=1e-8, error O(x))   pi^2C*^2 vs target: %s'
          % (mp.nstr(p, 3), mp.nstr(r1, 3), mp.nstr(r2, 3)))
    ok &= r1 < 1e-6 and r2 < 1e-30

# (I2)
for al in [mp.mpf('-0.5'), mp.mpf('-0.9'), mp.mpf(0), mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf(4)]:
    b1 = lambda z: mp.nsum(lambda k: z ** k / (mp.factorial(k) * mp.gamma(al + k + 1)), [0, mp.inf])
    b2 = lambda z: -mp.pi * 1j * mp.nsum(lambda k: (al + 2 * k) * z ** k / (mp.factorial(k) * mp.gamma(al + k + 1)), [0, mp.inf])
    d = mp.diff(b1, 0) * b2(0) - mp.diff(b2, 0) * b1(0)
    tgt = 2 * mp.pi * 1j / (mp.gamma(al + 1) * mp.gamma(al + 2))
    # cross-check bhat against zeta^{-al/2} (I_al(2 zeta^{1/2}), -2 pi i zeta^{1/2} I_al'(2 zeta^{1/2}))
    z = mp.mpf('0.37')
    u = 2 * mp.sqrt(z)
    e1 = abs(z ** (al / 2) * b1(z) - mp.besseli(al, u))
    e2 = abs(z ** (al / 2) * b2(z) - (-2 * mp.pi * 1j * mp.sqrt(z) * mp.besseli(al, u, derivative=1)))
    print('I2 al=%s  det/target-1 = %s   series vs besseli: %s %s' % (mp.nstr(al, 3), mp.nstr(abs(d / tgt - 1), 3),
                                                                     mp.nstr(e1, 3), mp.nstr(e2, 3)))
    ok &= abs(d / tgt - 1) < 1e-25 and e1 < 1e-25 and e2 < 1e-25

# (I3) Laguerre: monic L_k^{(a)} has value at 0: (-1)^k Gamma(k+a+1)/Gamma(a+1); h_k = k! Gamma(k+a+1)
for a in [mp.mpf('-0.5'), mp.mpf('0.25'), mp.mpf(2)]:
    for n in [10, 200]:
        K = mp.fsum((mp.gamma(k + a + 1) / mp.gamma(a + 1)) ** 2 / (mp.factorial(k) * mp.gamma(k + a + 1)) for k in range(n))
        exact = mp.gamma(a + 1) * mp.gamma(a + 2) * mp.gamma(n) / mp.gamma(n + a + 1)
        print('I3 a=%s n=%d  (1/K)/formula - 1 = %s ; n^{a+1}/K = %s vs G(a+1)G(a+2) = %s' %
              (mp.nstr(a, 3), n, mp.nstr(1 / K / exact - 1, 3), mp.nstr(n ** (a + 1) / K, 8),
               mp.nstr(mp.gamma(a + 1) * mp.gamma(a + 2), 8)))
        ok &= abs(1 / K / exact - 1) < 1e-30

# (I4)
p = mp.mpf(2); s = mp.mpf('3.3'); n = 7; al = (s - 1 - p) / p
c = c_of_p(p)
wn = -2 * mp.pi * 1j / p * mp.mpf(n) ** (1 + p - s)
sq = mp.sqrt(wn)
z = mp.mpc('-0.013', '0.021')
t = n * z ** (-1 / p)
jt = mp.loggamma(t) - (t - mp.mpf(1) / 2) * mp.log(t) + t - mp.log(2 * mp.pi) / 2
theta = mp.pi * t
ups = 1 / (1 - mp.exp(-2j * theta))
logB = mp.mpc('0.123', '-0.045')
F = ups * mp.exp(-jt) * mp.exp(logB) * (4 * c - z) ** (-mp.mpf(1) / 2)
G = -jt + logB
Wt = sq * (-z) ** (al / 2) * (4 * c - z) ** (mp.mpf(1) / 2) * mp.exp(-G)
r = abs(F * Wt / (ups * sq * (-z) ** (al / 2)) - 1)
print('I4 F*Wtilde/(ups wn^{1/2}(-z)^{al/2}) - 1 =', mp.nstr(r, 3))
ok &= r < 1e-30
print('ALL PASS' if ok else 'SOME FAIL')
