"""Plan 66 (E_p1.md Lemmas E1.7, E1.7a, E1.7b; NUMERICAL cross-checks of the inputs of the second-order matching at p = 1).
[1] WLXZ v1 at alpha_W = 1: the Airy-disc weight ratio G_TC := Dtilde^2/wtilde ((4.15), (4.27), (4.24), (3.4), (2.15)) equals
    G0 * H_n^{-1} with G0 := e^{-L}(z^2-4)^{1-2alpha_W}, e^L = sqrt(2) i Gamma(alpha)^2 e^alpha/sqrt(pi) ((5.9) context), and
    H_n(z) = H(n/z^2), H(t) = Gamma(t+1)e^t/(sqrt(2pi) t^{t+1/2}); and the model identity
    G0^{s3/2} N G0^{-s3/2} M0 = m_r ((5.11), (6.16), M0 = [[1,-i],[-i,1]]), on the circle |z - 2| = 0.3.
[2] equilibrium masses (2.1): int_0^2 psi = 1/4 and int_2^oo psi = 1/4, so phi_+(0) = -i pi/4 - i pi int_0^2 psi = -i pi/2 and
    e^{2 n phi_+(0)} = (-1)^n (the only n-periodic factor in the origin matching).
[3] Airy model (WLXZ (6.8)): in each of the four sectors, R(z) := sqrt(pi) z^{-s3/4} s2 Psi(z) s2 e^{(2/3)z^{3/2} s3} satisfies
    M0 R = I + X/xi + O(|xi|^-2) with ONE constant X = [[-1/72, i/12], [i/12, 1/72]] for all rays and all four sectors
    (Rule R A5: tests sector-constancy, not only the ray-wise two-term structure): printed |M0 R - I||xi| and
    |xi|^2 |M0 R - I - X/xi| (bounded).
[4] Bessel model (Vanlessen (4.26)-(4.33) = KV (5.23), lambda = a): in each of the eight sectors
    K(z) := B^{-1} Psi_a(z) (e^{pi i s3/4} e^{-i z s3} C_q)^{-1} = I + Psi1_j/z + O(|z|^-2), B = [[1,-i],[-i,1]]/sqrt2,
    C_q from (4.43)-(4.46), with ONE constant Psi1 = (lam/2) sigma1 - (i lam^2/2) sigma3 for all rays and all eight sectors
    (Rule R A5); printed |K - I| |z| and |z|^2 |K - I - Psi1/z| (bounded)."""
import mpmath as mp

mp.mp.dps = 40
I2 = mp.eye(2)
s1 = mp.matrix([[0, 1], [1, 0]]); s2 = mp.matrix([[0, -1j], [1j, 0]]); s3 = mp.matrix([[1, 0], [0, -1]])
dg = lambda u, v: mp.matrix([[u, 0], [0, v]])
nrm = lambda A: max(abs(A[i, j]) for i in range(2) for j in range(2))

# ---------- [1]
al = mp.mpf(1)
eL = mp.sqrt(2) * 1j * mp.gamma(al) ** 2 * mp.e ** al / mp.sqrt(mp.pi)
pw = lambda z, g: (z - 2) ** g * (z + 2) ** g                       # (z^2-4)^g with arg(z +- 2) in (-pi, pi)
vphi = lambda w: w + mp.sqrt(w - 1) * mp.sqrt(w + 1)                 # phi(w) = w + sqrt(w^2-1), cut [-1,1], ~ 2w
def Nmat(z):
    p = vphi(z / 2)
    return mp.matrix([[pw(z, mp.mpf(1) / 4 - al) * p ** (2 * al - mp.mpf(1) / 2), -1j * eL * pw(z, al - mp.mpf(3) / 4) * p ** (mp.mpf(1) / 2 - 2 * al)],
                      [1j / eL * pw(z, mp.mpf(1) / 4 - al) * p ** (2 * al - mp.mpf(3) / 2), pw(z, al - mp.mpf(3) / 4) * p ** (mp.mpf(3) / 2 - 2 * al)]])
M0 = mp.matrix([[1, -1j], [-1j, 1]])
def m_r(z):
    p = vphi(z / 2)
    A = mp.matrix([[p ** (2 * al - mp.mpf(1) / 2), -1j * p ** (mp.mpf(1) / 2 - 2 * al)], [1j * p ** (2 * al - mp.mpf(3) / 2), p ** (mp.mpf(3) / 2 - 2 * al)]])
    return dg(pw(z, mp.mpf(1) / 2 - al), pw(z, al - mp.mpf(1) / 2)) * A * M0 / pw(z, mp.mpf(1) / 4)
G0 = lambda z: pw(z, 1 - 2 * al) / eL
H = lambda t: mp.gamma(t + 1) * mp.e ** t / (mp.sqrt(2 * mp.pi) * t ** (t + mp.mpf(1) / 2))
def G_TC(z, n):
    t = n / z ** 2
    Dt = mp.sqrt(2 * mp.pi) * t ** (t - al + mp.mpf(1) / 2) / (mp.gamma(1 + t - al) * mp.e ** t)          # (4.15)
    zz = z / mp.sqrt(n)
    wd = (1 / zz ** 2) ** (1 / zz ** 2 - 1 - al) * mp.e ** (-1 / zz ** 2 + al) / mp.gamma(1 / zz ** 2 + 1 - al)   # (2.15)
    w = mp.sqrt(n) * wd                                                                                    # (3.4)
    gam = -2 * n * mp.pi / z ** 3                                                                          # (3.7)
    Et = mp.sqrt(2 * mp.pi) / mp.gamma(al) * pw(z, mp.mpf(1) / 2 - al)                                    # (4.24)
    wt = -2j * gam * w / Et ** 2                                                                           # (4.27)
    return Dt ** 2 / wt
worst_G, worst_m = 0, 0
for n in (40, 400):
    for th in [mp.pi * k / 8 + 0.1 for k in range(16)]:
        z = 2 + mp.mpf('0.3') * mp.expj(th)
        if abs(mp.im(z)) < 1e-6:
            continue
        worst_G = max(worst_G, abs(G_TC(z, n) / (G0(z) / H(n / z ** 2)) - 1))
for th in [mp.pi * k / 8 + 0.1 for k in range(16)]:
    z = 2 + mp.mpf('0.3') * mp.expj(th)
    sq = mp.sqrt(G0(z))
    lhs = dg(sq, 1 / sq) * Nmat(z) * dg(1 / sq, sq) * M0
    worst_m = max(worst_m, nrm(lhs - m_r(z)))
print(f"[1] max |G_TC/(G0 H_n^-1) - 1| on |z-2| = 0.3, n = 40, 400: {mp.nstr(worst_G, 3)}")
print(f"[1] max |G0^(s3/2) N G0^(-s3/2) M0 - m_r| on |z-2| = 0.3: {mp.nstr(worst_m, 3)}")

# ---------- [2]
psi = lambda x: (4 * mp.atan(x / mp.sqrt(4 - x ** 2)) / x ** 3 - mp.sqrt(4 - x ** 2) / x ** 2) / mp.pi
band = mp.quad(psi, [0, 1, 2]); sat = mp.quad(lambda x: 2 / x ** 3, [2, mp.inf])
print(f"[2] int_0^2 psi = {mp.nstr(band, 15)}, int_2^oo psi = {mp.nstr(sat, 15)}; phi_+(0)/(i pi) = {mp.nstr(-mp.mpf(1)/4 - band, 15)}")

# ---------- [3] Airy model
om = mp.expj(2 * mp.pi / 3)
Ai = lambda z: mp.airyai(z); Aip = lambda z: mp.airyai(z, derivative=1)
def PsiA(z):
    a = mp.arg(z)
    if 0 <= a < mp.pi / 2:
        return mp.matrix([[Ai(z), om ** 2 * Ai(om ** 2 * z)], [1j * Aip(z), 1j * om * Aip(om ** 2 * z)]])
    if mp.pi / 2 <= a <= mp.pi:
        return mp.matrix([[-om * Ai(om * z), om ** 2 * Ai(om ** 2 * z)], [-1j * om ** 2 * Aip(om * z), 1j * om * Aip(om ** 2 * z)]])
    if -mp.pi < a < -mp.pi / 2:
        return mp.matrix([[-om ** 2 * Ai(om ** 2 * z), -om * Ai(om * z)], [-1j * om * Aip(om ** 2 * z), -1j * om ** 2 * Aip(om * z)]])
    return mp.matrix([[Ai(z), -om * Ai(om * z)], [1j * Aip(z), -1j * om ** 2 * Aip(om * z)]])
def RA(z):
    xi = mp.mpf(2) / 3 * z ** mp.mpf(1.5)
    return M0 * mp.sqrt(mp.pi) * dg(z ** (-mp.mpf(1) / 4), z ** (mp.mpf(1) / 4)) * s2 * PsiA(z) * s2 * dg(mp.e ** (-xi), mp.e ** xi), xi
XA = mp.matrix([[-mp.mpf(1) / 72, 1j / 12], [1j / 12, mp.mpf(1) / 72]])     # one candidate constant for ALL sectors (A5)
for (lo, hi, name) in [(0.05, mp.pi / 2 - 0.05, "(0,pi/2)"), (mp.pi / 2 + 0.05, mp.pi - 0.05, "(pi/2,pi)"),
                       (-mp.pi + 0.05, -mp.pi / 2 - 0.05, "(-pi,-pi/2)"), (-mp.pi / 2 + 0.05, -0.05, "(-pi/2,0)")]:
    worst1, worst2 = 0, 0
    for th in [lo + (hi - lo) * k / 4 for k in range(5)]:
        for r in (25, 50, 100, 200, 400):
            R, xi = RA(r * mp.expj(th))
            worst1 = max(worst1, nrm(R - I2) * abs(xi))
            worst2 = max(worst2, nrm(R - I2 - XA / xi) * abs(xi) ** 2)
    print(f"[3] Airy sector arg in {name} (5 rays, |z| = 25..400): max |M0 R - I| |xi| = {mp.nstr(worst1, 5)},"
          f"  max |xi|^2 |M0 R - I - X/xi| = {mp.nstr(worst2, 5)}  (X = [[-1/72, i/12], [i/12, 1/72]] common to all sectors)")

# ---------- [4] Bessel (Fisher-Hartwig) model
def PsiB(z, lam):
    a = mp.arg(z); sp_ = mp.sqrt(mp.pi); h = mp.mpf(1) / 2
    # Hankel functions via K (DLMF 10.27.8), to avoid the cancellation in J +- iY for large |Im x| (evaluation only):
    # H1_nu(x) = (2/(pi i)) e^{-nu pi i/2} K_nu(-i x), H2_nu(x) = -(2/(pi i)) e^{nu pi i/2} K_nu(i x), valid for |ph x| <= pi/2
    H1 = lambda nu, x: 2 / (mp.pi * 1j) * mp.expj(-nu * mp.pi / 2) * mp.besselk(nu, -1j * x)
    H2 = lambda nu, x: -2 / (mp.pi * 1j) * mp.expj(nu * mp.pi / 2) * mp.besselk(nu, 1j * x)
    Iv = lambda nu, x: mp.besseli(nu, x); Kv = lambda nu, x: mp.besselk(nu, x)
    if 0 <= a < mp.pi / 4:
        return h * sp_ * mp.sqrt(z) * mp.matrix([[H2(lam + h, z), -1j * H1(lam + h, z)], [H2(lam - h, z), -1j * H1(lam - h, z)]]) * dg(mp.expj(-(lam + mp.mpf(1) / 4) * mp.pi), mp.expj((lam + mp.mpf(1) / 4) * mp.pi))
    if mp.pi / 4 <= a < 3 * mp.pi / 4:
        w = z * mp.expj(-mp.pi / 2)
        M = mp.matrix([[sp_ * mp.sqrt(z) * Iv(lam + h, w), -mp.sqrt(z) * Kv(lam + h, w) / sp_], [-1j * sp_ * mp.sqrt(z) * Iv(lam - h, w), -1j * mp.sqrt(z) * Kv(lam - h, w) / sp_]])
        e = -1 if a < mp.pi / 2 else 1
        return M * dg(mp.expj(e * lam * mp.pi / 2), mp.expj(-e * lam * mp.pi / 2))
    if 3 * mp.pi / 4 <= a <= mp.pi:
        return h * sp_ * mp.sqrt(-z) * mp.matrix([[1j * H1(lam + h, -z), -H2(lam + h, -z)], [-1j * H1(lam - h, -z), H2(lam - h, -z)]]) * dg(mp.expj((lam + mp.mpf(1) / 4) * mp.pi), mp.expj(-(lam + mp.mpf(1) / 4) * mp.pi))
    if -mp.pi < a < -3 * mp.pi / 4:
        return h * sp_ * mp.sqrt(-z) * mp.matrix([[-H2(lam + h, -z), -1j * H1(lam + h, -z)], [H2(lam - h, -z), 1j * H1(lam - h, -z)]]) * dg(mp.expj(-(lam + mp.mpf(1) / 4) * mp.pi), mp.expj((lam + mp.mpf(1) / 4) * mp.pi))
    if -3 * mp.pi / 4 <= a < -mp.pi / 4:
        w = z * mp.expj(mp.pi / 2)
        M = mp.matrix([[-1j * sp_ * mp.sqrt(z) * Iv(lam + h, w), -1j * mp.sqrt(z) * Kv(lam + h, w) / sp_], [sp_ * mp.sqrt(z) * Iv(lam - h, w), -mp.sqrt(z) * Kv(lam - h, w) / sp_]])
        e = -1 if a < -mp.pi / 2 else 1
        return M * dg(mp.expj(e * lam * mp.pi / 2), mp.expj(-e * lam * mp.pi / 2))
    return h * sp_ * mp.sqrt(z) * mp.matrix([[-1j * H1(lam + h, z), -H2(lam + h, z)], [-1j * H1(lam - h, z), -H2(lam - h, z)]]) * dg(mp.expj((lam + mp.mpf(1) / 4) * mp.pi), mp.expj(-(lam + mp.mpf(1) / 4) * mp.pi))
Bm = mp.matrix([[1, -1j], [-1j, 1]]) / mp.sqrt(2); J = mp.matrix([[0, -1], [1, 0]])
def Cq_inv(z, lam):
    # inverse of C_q in (4.43)-(4.46): q = 1: e^{-lam pi i s3/2}; q = 2: e^{lam pi i s3/2}; q = 3: e^{lam pi i s3/2} J;
    # q = 4: e^{-lam pi i s3/2} J, J = [[0,-1],[1,0]] (J^{-1} = -J)
    a = mp.arg(z)
    if 0 <= a < mp.pi / 2: return dg(mp.expj(lam * mp.pi / 2), mp.expj(-lam * mp.pi / 2))
    if mp.pi / 2 <= a <= mp.pi: return dg(mp.expj(-lam * mp.pi / 2), mp.expj(lam * mp.pi / 2))
    if -mp.pi < a < -mp.pi / 2: return -J * dg(mp.expj(-lam * mp.pi / 2), mp.expj(lam * mp.pi / 2))
    return -J * dg(mp.expj(lam * mp.pi / 2), mp.expj(-lam * mp.pi / 2))
Binv = mp.matrix([[1, 1j], [1j, 1]]) / mp.sqrt(2)
def KB(z, lam):
    lead_inv = Cq_inv(z, lam) * dg(mp.expj(z), mp.expj(-z)) * dg(mp.expj(-mp.pi / 4), mp.expj(mp.pi / 4))
    return Binv * PsiB(z, lam) * lead_inv
for lam in (mp.mpf('-0.25'), mp.mpf('0.5'), mp.mpf('1.5')):
    Psi1 = (lam / 2) * s1 - 1j * lam ** 2 / 2 * s3          # one candidate constant for ALL sectors (A5)
    for k in range(8):
        lo, hi = -mp.pi + k * mp.pi / 4 + 0.03, -mp.pi + (k + 1) * mp.pi / 4 - 0.03
        worst1, worst2 = 0, 0
        for th in [lo + (hi - lo) * t / 3 for t in range(4)]:
            for r in (25, 50, 100, 200, 400):
                z = r * mp.expj(th)
                Kz = KB(z, lam)
                worst1 = max(worst1, nrm(Kz - I2) * r)
                worst2 = max(worst2, nrm(Kz - I2 - Psi1 / z) * r ** 2)
        print(f"[4] lambda = {mp.nstr(lam, 3)}, arg in ({mp.nstr(lo, 3)}, {mp.nstr(hi, 3)}) (4 rays, |z| = 25..400): max |K - I| |z| = {mp.nstr(worst1, 5)},"
              f"  max |z|^2 |K - I - Psi1/z| = {mp.nstr(worst2, 5)}  (Psi1 = (lam/2) s1 - (i lam^2/2) s3 common to all sectors)")
