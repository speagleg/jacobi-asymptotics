"""Plan 65 (E_pgt1.md; NUMERICAL cross-check of the symbolic computation check_e_sym.py, independent ingredients).

[1] Airy model: X(zeta) := xi (M^{-1} zeta^{s3/4} Psi^j(zeta) e^{-xi s3} - I), xi = (2/3) zeta^{3/2}, in all four sectors of
    Paper 2 (eq. airy-model), -> X = [[-1/72, -i/12], [-i/12, 1/72]] (from DLMF 9.7.2, 9.7.5-6: u_1 = 5/72, v_1 = -7/72).
[2] Bessel model (KMVV (6.23)-(6.25)): 16 zeta^{1/2} (M^{-1}(2 pi zeta^{1/2})^{s3/2} Psi(zeta) e^{-2 zeta^{1/2} s3} - I)
    -> [[-(1+4a^2), -2i], [-2i, 1+4a^2]] in all sectors (DLMF 10.40.1-4, 10.17.5-6, 10.17.11-12).
[3] Contour integrals of Delta_1 built from quadrature: g (hence phi, phit, f) by quadrature of the arcsine mixture,
    omega = D_W^2/W_0 by quadrature of the Szego integral of x^alpha (4c - x) -- no closed form from Lemma E.4 is used.
    R1 = (1/2 pi i) oint Delta_1, R2 = (1/2 pi i) oint s Delta_1, R^(1)(0) = -(1/2 pi i) oint Delta_1(s) ds/s (both circles ccw),
    then d1, e1 (std), gamma' (n^p g_{n-1} = c(1 + gamma'/n)) and k1 = k0 + p - 2 gamma' with k0 = 2 d1 - p/2 (numerical d1)."""
import mpmath as mp

print("[1] Airy correction matrix X (expected [[-0.013888889, -0.083333333 i], [-0.083333333 i, 0.013888889]])")
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
        errs.append(mp.mnorm(xi * (M ** -1 * L - mp.eye(2)) - Xex, 1))
    print(f"   sector {j} (arg {ang}): |X(zeta) - X| = {mp.nstr(errs[0], 3)} (|zeta| = 400), {mp.nstr(errs[1], 3)} (1600)")

print("[2] Bessel correction matrix (expected diag -(1+4a^2), +(1+4a^2), off-diagonal -2i)")
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
            errs.append(mp.mnorm(16 * r * (M ** -1 * L - mp.eye(2)) - Qex, 1))
        print(f"   alpha = {mp.nstr(a, 2)}, arg {ang}: error {mp.nstr(errs[0], 3)} (|zeta| = 1e4), {mp.nstr(errs[1], 3)} (4e4)")

print("[3] contour integrals of Delta_1 (quadrature ingredients); circle radii delta = eps = 0.3, 48-point trapezoid")
mp.mp.dps = 20
def run(p, s, delta=0.3, eps=0.3, K=48):
    p = mp.mpf(p); s = mp.mpf(s)
    Ip = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
    c = (mp.pi / (2 * Ip)) ** p / 4; c4 = 4 * c; gam = mp.log(c) + p
    al = (s - 1 - p) / p
    def g(z):
        f = lambda tau: 2 * mp.log((mp.sqrt(z) + mp.sqrt(z - c4 * tau ** (-p))) / 2)
        return mp.quad(f, [mp.mpf('1e-40'), mp.mpf('1e-6'), 0.01, 0.3, 1])
    sg = lambda z: 1 if mp.im(z) > 0 else -1
    phi = lambda z: gam - g(z)
    phit = lambda z: phi(z) + sg(z) * 1j * mp.pi * z ** (-1 / p)
    def logD2(z):
        R = z * mp.sqrt(1 - c4 / z)
        def f(th):
            x = c4 * mp.sin(th / 2) ** 2
            return (al * (2 * mp.log(mp.sin(th / 2)) + mp.log(c4)) + 2 * mp.log(mp.cos(th / 2)) + mp.log(c4)) / (z - x)
        return R / mp.pi * mp.quad(f, [0, mp.pi / 2, mp.pi])
    omega = lambda z: mp.exp(logD2(z)) / (z ** al * (c4 - z))
    def P0(z):
        a = (1 - c4 / z) ** 0.25
        return mp.matrix([[(a + 1 / a) / 2, (a - 1 / a) / (2j)], [-(a - 1 / a) / (2j), (a + 1 / a) / 2]])
    Q0 = mp.matrix([[-(1 + 4 * al ** 2), 2j], [2j, 1 + 4 * al ** 2]])
    X = mp.matrix([[-mp.mpf(1) / 72, -1j / 12], [-1j / 12, mp.mpf(1) / 72]])
    def D1bes(z):
        fh = -(phi(z) + sg(z) * 1j * mp.pi) / 2
        r = mp.sqrt(mp.exp(-sg(z) * 1j * mp.pi * al) / omega(z))
        Pz = P0(z)
        return Pz * mp.diag([r, 1 / r]) * Q0 * mp.diag([1 / r, r]) * mp.inverse(Pz) / (16 * fh)
    def D1airy(z):
        h = mp.sqrt(-omega(z)); Pz = P0(z)
        return -Pz * mp.diag([1 / h, h]) * X * mp.diag([h, 1 / h]) * mp.inverse(Pz) / phit(z)
    def mom(D, ctr, rad, wt):
        m = mp.zeros(2, 2)
        for k in range(K):
            th = 2 * mp.pi * (k + 0.5) / K
            z = ctr + rad * mp.exp(1j * th); dz = 1j * rad * mp.exp(1j * th) * 2 * mp.pi / K
            m += D(z) * wt(z) * dz
        return m / (2j * mp.pi)
    one = lambda z: 1; ide = lambda z: z; inv = lambda z: 1 / z
    A = mom(D1bes, 0, delta, one) + mom(D1airy, c4, eps, one)
    B2 = mom(D1bes, 0, delta, ide) + mom(D1airy, c4, eps, ide)
    R0 = -(mom(D1bes, 0, delta, inv) + mom(D1airy, c4, eps, inv))
    P1 = mp.matrix([[0, 1j * c], [-1j * c, 0]]); P2 = mp.matrix([[c ** 2 / 2, 2j * c ** 2], [-2j * c ** 2, c ** 2 / 2]])
    d1 = 1j * (A[1, 0] - A[0, 1]) / (2 * c)
    T2 = A * P1 + B2
    da = (T2[0, 1] / P1[0, 1] - P2[0, 1] * A[0, 1] / P1[0, 1] ** 2) - A[1, 1]
    e1s = da / (2 * c) - d1
    Mb = mp.matrix([[1, 1j], [1j, 1]]) / mp.sqrt(2)
    def wvec(r):
        z = -r + 1j * mp.mpf(10) ** -30
        fh = -(phi(z) + 1j * mp.pi) / 2; f4 = mp.sqrt(fh)
        rr = mp.sqrt(mp.exp(-1j * mp.pi * al) / omega(z))
        Bm = P0(z) * mp.diag([rr, 1 / rr]) * Mb
        return Bm * mp.matrix([f4, 0]), Bm * mp.matrix([0, -1j * al / (2 * f4)])
    va, vb = wvec(mp.mpf('1e-8')), wvec(mp.mpf('1e-8') / 4)
    w0 = 2 * vb[0] - va[0]; w1 = 2 * vb[1] - va[1]         # Richardson in r^{1/2}
    r0 = w0[0] / w0[1]; num = R0 * w0 + w1
    r1 = r0 * (num[0] / w0[0] - num[1] / w0[1])
    lead = 1j * c * r0
    gp = (-A[1, 0] * r0 + 1j * c * r1) / lead
    k0 = 2 * d1 - p / 2          # from the numerical d1 (RH.md Lemma 5.1 unfolding), not the closed form
    k1 = k0 + p - 2 * gp
    re = lambda x: mp.nstr(mp.re(x), 10)
    print(f"   p={mp.nstr(p,3)} s={mp.nstr(s,3)} (alpha={mp.nstr(al,4)}): d1={re(d1)} [-(s-1)/2={mp.nstr(-(s-1)/2,10)}]  "
          f"e1s={re(e1s)} [-p/2]  lead/c={re(lead/c)}  gamma'={re(gp)} [a={mp.nstr(al+0.5,10)}]  k0={re(k0)} [{mp.nstr(-(s-1)-p/2,10)}]  k1={re(k1)} [-(p+2)a={mp.nstr(-(p+2)*(al+0.5),10)}]")
    print(f"      Bessel residue (1,1) entry {re(mom(D1bes,0,delta,one)[0,0])} vs c(p+2)(4al^2-1)/16 = {mp.nstr(c*(p+2)*(4*al**2-1)/16,10)}")
for p, s in [(2, 3), (1.5, 2), (3, 2.5), (2.5, 4.5), (2, 2), (1.25, 4)]:
    run(p, s)
