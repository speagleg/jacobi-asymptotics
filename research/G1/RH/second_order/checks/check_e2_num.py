"""E2 (d2 for p > 1; NUMERICAL cross-check of the second-order local models used in check_e2_sym.py).
[1] Airy: xi^2 (M^{-1} zeta^{s3/4} Psi^j e^{-xi s3} - I - X1/xi) -> X2 = [[(u2+v2)/2, i(u2-v2)/2], [-i(u2-v2)/2, (u2+v2)/2]]
    in all four sectors (u2 = 385/10368, v2 = -455/10368, DLMF 9.7.2).
[2] Bessel: w^2 (M^{-1}(2 pi zeta^{1/2})^{s3/2} Psi e^{-w s3} - I - Xi1/w) -> Xi2 = (1/2)[[a2+b2, i(a2-b2)], [-i(a2-b2), a2+b2]],
    w = 2 zeta^{1/2}, a2 = (4a^2-1)(4a^2-9)/128, b2 = (4a^2-1)(4a^2+15)/128 (DLMF 10.17.1, 10.17.8), in all sectors.
Model definitions copied from check_e_num.py (Plan 65) [1]-[2]."""
import mpmath as mp

print("[1] Airy second-order matrix X2: error |X2(zeta) - X2| at |zeta| = 400, 1600 (should decrease like 1/xi)")
mp.mp.dps = 40
q = mp.exp(2j * mp.pi / 3); kA = mp.sqrt(2 * mp.pi) * mp.exp(1j * mp.pi / 12)
M = mp.matrix([[1, 1j], [1j, 1]]) / mp.sqrt(2)
y0 = lambda z: mp.matrix([mp.airyai(z), mp.airyai(z, 1)])
yp = lambda z: mp.matrix([mp.airyai(z / q), mp.airyai(z / q, 1) / q])
ym = lambda z: mp.matrix([mp.airyai(z * q), mp.airyai(z * q, 1) * q])
E4 = mp.diag([mp.exp(-1j * mp.pi / 4), mp.exp(1j * mp.pi / 4)])
col = lambda a, b: mp.matrix([[a[0], b[0]], [a[1], b[1]]])
def PsiA(j, z):
    m = {1: lambda: col(yp(z), q * y0(z)), 2: lambda: col(yp(z), -ym(z) / q),
         3: lambda: col(-ym(z) / q, -yp(z)), 4: lambda: col(-ym(z) / q, q * y0(z))}[j]()
    return kA * E4 * m
Xex = mp.matrix([[-mp.mpf(1) / 72, -1j / 12], [-1j / 12, mp.mpf(1) / 72]])
for j, ang in [(1, 0.3), (2, 2.0), (3, -2.0), (4, -0.3)]:
    errs = []
    for R in (400, 1600):
        z = R * mp.exp(1j * ang); xi = mp.mpf(2) / 3 * z ** 1.5
        L = mp.diag([z ** 0.25, z ** -0.25]) * PsiA(j, z) * mp.diag([mp.exp(-xi), mp.exp(xi)])
        u2, v2 = mp.mpf(385) / 10368, -mp.mpf(455) / 10368
        X2 = mp.matrix([[(u2 + v2) / 2, 1j * (u2 - v2) / 2], [-1j * (u2 - v2) / 2, (u2 + v2) / 2]])
        errs.append(mp.mnorm(xi ** 2 * (M ** -1 * L - mp.eye(2) - Xex / xi) - X2, 1))
    print(f"   sector {j} (arg {ang}): |X(zeta) - X| = {mp.nstr(errs[0], 3)} (|zeta| = 400), {mp.nstr(errs[1], 3)} (1600)")

print("[2] Bessel second-order matrix Xi2: error at |zeta| = 1e4, 4e4 (should decrease like 1/w)")
mp.mp.dps = 300
def PsiB(zeta, a):
    r = mp.sqrt(zeta); th = mp.arg(zeta)
    if abs(th) < 2 * mp.pi / 3:
        I0 = mp.besseli(a, 2 * r); K0 = mp.besselk(a, 2 * r)
        I1 = mp.besseli(a, 2 * r, derivative=1); K1 = -(mp.besselk(a - 1, 2 * r) + mp.besselk(a + 1, 2 * r)) / 2
        return mp.matrix([[I0, 1j / mp.pi * K0], [2 * mp.pi * 1j * r * I1, -2 * r * K1]])
    qq = 2 * mp.sqrt(-zeta)
    H1, H2 = mp.hankel1(a, qq), mp.hankel2(a, qq)
    H1d = (mp.hankel1(a - 1, qq) - mp.hankel1(a + 1, qq)) / 2
    H2d = (mp.hankel2(a - 1, qq) - mp.hankel2(a + 1, qq)) / 2
    if th > 0:
        return mp.matrix([[H1 / 2, H2 / 2], [mp.pi * r * H1d, mp.pi * r * H2d]]) * mp.diag([mp.expjpi(a / 2), mp.expjpi(-a / 2)])
    return mp.matrix([[H2 / 2, -H1 / 2], [-mp.pi * r * H2d, mp.pi * r * H1d]]) * mp.diag([mp.expjpi(-a / 2), mp.expjpi(a / 2)])
for a in (mp.mpf('0.3'), mp.mpf('-0.6')):
    Qex = mp.matrix([[-(1 + 4 * a * a), -2j], [-2j, 1 + 4 * a * a]])
    for ang in (0.2, 1.5, 2.5, 3.0, -2.5, -1.5):
        errs = []
        for R in (1e4, 4e4):
            z = R * mp.exp(1j * ang); r = mp.sqrt(z)
            L = mp.diag([(2 * mp.pi * r) ** 0.5, (2 * mp.pi * r) ** -0.5]) * PsiB(z, a) * mp.diag([mp.exp(-2 * r), mp.exp(2 * r)])
            w = 2 * r
            a1, b1 = (4 * a * a - 1) / 8, (4 * a * a + 3) / 8
            a2, b2 = (4 * a * a - 1) * (4 * a * a - 9) / 128, (4 * a * a - 1) * (4 * a * a + 15) / 128
            Xi1 = mp.matrix([[-(a1 + b1), 1j * (a1 - b1)], [1j * (a1 - b1), a1 + b1]]) / 2
            Xi2 = mp.matrix([[a2 + b2, 1j * (a2 - b2)], [-1j * (a2 - b2), a2 + b2]]) / 2
            errs.append(mp.mnorm(w ** 2 * (M ** -1 * L - mp.eye(2) - Xi1 / w) - Xi2, 1))
        print(f"   alpha = {mp.nstr(a, 2)}, arg {ang}: error {mp.nstr(errs[0], 3)} (|zeta| = 1e4), {mp.nstr(errs[1], 3)} (4e4)")

