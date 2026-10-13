"""(Committed from the Rule R review of RH_px; lens-sector points added for the F1 re-check.) Rule R probe of RH_px Section 4.1 (hard-edge Bessel parametrix), p = 2, s = 3 (alpha_x = 0).
 [A] Band jump of E_N := N W^{s3} M f^{s3/4} (2 pi N)^{s3/2} on (0, delta): E_-^{-1} E_+ = f_-^{-s3/4} M^{-1} [[0,1],[-1,0]] M f_+^{s3/4}
     (using N_+ = N_- [[0,w0],[-1/w0,0]], W analytic with W^2 = w0 at alpha_x = 0).  Doc: M = [[1,-i],[-i,1]]/sqrt2
     (KMVV (6.31), endpoint +1); KMVV (6.53) (endpoint -1, band to the right): M = [[1,i],[i,1]]/sqrt2.
 [B] Matching on |z| = delta outside the lens: |Dinf^{-s3}(P N^{-1} - I)Dinf^{s3}| for
     doc:  P = E_N(M-) Psi(N^2 f) W^{-s3} e^{-N phi s3}
     KMVV(-1) analogue: P = (-1)^N E_N(M+) s3 Psi(N^2 f) s3 W^{-s3} e^{+N phi s3}."""
import mpmath as mp

mp.mp.dps = 30
p, s = mp.mpf(2), mp.mpf(3)
I_ = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
c = (mp.pi / (2 * I_)) ** p / 4; c4 = 4 * c; l = 2 * (mp.log(c) + p)
s3 = mp.diag([1, -1])
def g(z):
    f = lambda tau: 2 * mp.log((mp.sqrt(z) + mp.sqrt(z - c4 * tau ** (-p))) / 2)
    return mp.quad(f, [0, mp.mpf("1e-8"), mp.mpf("1e-4"), mp.mpf("0.01"), 0.5, 1])
phi = lambda z: l / 2 - g(z)
def fmap(z):
    sg = 1 if mp.im(z) > 0 else -1
    return (phi(z) + sg * 1j * mp.pi) ** 2 / 4
Mm = mp.matrix([[1, -1j], [-1j, 1]]) / mp.sqrt(2)
Mp = mp.matrix([[1, 1j], [1j, 1]]) / mp.sqrt(2)
J0 = mp.matrix([[0, 1], [-1, 0]])
print("[A] E_N band jump at x (alpha_x = 0):")
for x in (mp.mpf("0.05"), mp.mpf("0.2")):
    e = mp.mpf("1e-20")
    fp, fm = fmap(x + 1j * e), fmap(x - 1j * e)
    for name, M in (("doc  [[1,-i],[-i,1]]", Mm), ("KMVV(6.53) [[1,i],[i,1]]", Mp)):
        Jm = mp.diag([fm ** -0.25, fm ** 0.25]) * mp.inverse(M) * J0 * M * mp.diag([fp ** 0.25, fp ** -0.25])
        print(f"   x={x} {name:26s}: E_-^-1 E_+ = {[[mp.nstr(Jm[i,j],6) for j in range(2)] for i in range(2)]}")

# ---------- [B] matching
def Psi(zeta, a=0):
    """KMVV (6.23) for |arg zeta| < 2pi/3, (6.24) for 2pi/3 < arg < pi, (6.25) for -pi < arg < -2pi/3 (order a)."""
    r = mp.sqrt(zeta)
    th = mp.arg(zeta)
    if abs(th) < 2 * mp.pi / 3:
        I0 = mp.besseli(a, 2 * r); K0 = mp.besselk(a, 2 * r)
        I1 = mp.besseli(a, 2 * r, derivative=1); K1 = -(mp.besselk(a - 1, 2 * r) + mp.besselk(a + 1, 2 * r)) / 2
        return mp.matrix([[I0, 1j / mp.pi * K0], [2 * mp.pi * 1j * r * I1, -2 * r * K1]])
    q = 2 * mp.sqrt(-zeta)
    H1, H2 = mp.hankel1(a, q), mp.hankel2(a, q)
    H1d = (mp.hankel1(a - 1, q) - mp.hankel1(a + 1, q)) / 2
    H2d = (mp.hankel2(a - 1, q) - mp.hankel2(a + 1, q)) / 2
    if th > 0:
        M = mp.matrix([[H1 / 2, H2 / 2], [mp.pi * r * H1d, mp.pi * r * H2d]])
        return M * mp.diag([mp.expjpi(a / 2), mp.expjpi(-a / 2)])
    M = mp.matrix([[H2 / 2, -H1 / 2], [-mp.pi * r * H2d, mp.pi * r * H1d]])
    return M * mp.diag([mp.expjpi(-a / 2), mp.expjpi(a / 2)])
# reuse the global-parametrix construction by a light re-implementation (alpha_x = 0, p = 2, s = 3)
def make_N(N):
    t = lambda z: N * mp.power(z, -1 / p)
    Dt = lambda z: mp.sqrt(2 * mp.pi) * mp.exp((t(z) - 0.5) * mp.log(t(z)) - t(z) - mp.loggamma(t(z)))
    def D(z):
        sg = 1 if mp.im(z) > 0 else -1
        return Dt(z) / (1 - mp.exp(-sg * 2j * mp.pi * t(z)))
    ellc = {}
    def ell(u):
        if u not in ellc:
            ellc[u] = 2 * mp.arg(D(-mp.exp(u) + 1j * mp.mpf("1e-28") * mp.exp(u)))
        return ellc[u]
    BR = [-80, -40, -20, -8, -3, 0, 3, 8, 20, 40, 80, 120]
    def S(z):
        f = lambda u: ell(u) * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u)
        return mp.exp(-mp.quad(f, BR) / (2 * mp.pi))
    Wabs = 2 * mp.pi / p * mp.power(N, 1 + p - s)
    lwc = {}
    def lw(th):
        if th not in lwc:
            x = c4 * mp.sin(th / 2) ** 2
            lwc[th] = mp.log(Wabs) + mp.log(c4) + 2 * mp.log(mp.cos(th / 2)) - 2 * mp.log(Dt(x) * S(x)) - 1j * mp.pi / 2
        return lwc[th]
    Dinf = mp.exp(mp.quad(lw, [0, mp.pi / 2, mp.pi]) / (2 * mp.pi))
    def Dw(z):
        r = z * mp.sqrt(1 - c4 / z)
        return mp.exp(r / (2 * mp.pi) * mp.quad(lambda th: lw(th) / (z - c4 * mp.sin(th / 2) ** 2), [0, mp.pi / 2, mp.pi]))
    def Ng(z):
        a = mp.power(1 - c4 / z, 0.25)
        N0 = mp.matrix([[(a + 1 / a) / 2, (a - 1 / a) / (2j)], [-(a - 1 / a) / (2j), (a + 1 / a) / 2]])
        d = Dw(z)
        return mp.diag([Dinf, 1 / Dinf]) * N0 * mp.diag([1 / d, d])
    Wf = lambda z: mp.sqrt(-1j * Wabs * (c4 - z) / (Dt(z) * S(z)) ** 2)
    return Ng, Wf, Dinf
print("[B] matching on |z| = delta = 0.4 (outside the lens: arg +-0.5pi, +-0.8pi; inside the lens: arg +-0.15pi)")
for N in (20, 40):
    Ng, Wf, Dinf = make_N(N)
    for ang in (0.5, 0.8, -0.5, -0.8, 0.15, -0.15):
        z = mp.mpf("0.4") * mp.expjpi(ang)
        f = fmap(z); zeta = N ** 2 * f; ph = phi(z); W = Wf(z); Nz = Ng(z)
        res = []
        for name, M, conj, sgn in (("doc", Mm, False, -1), ("KMVV(-1)", Mp, True, +1)):
            E = Nz * mp.diag([W, 1 / W]) * M * mp.diag([f ** 0.25, f ** -0.25]) * mp.diag([mp.sqrt(2 * mp.pi * N), 1 / mp.sqrt(2 * mp.pi * N)])
            Ps = Psi(zeta)
            if conj: Ps = s3 * Ps * s3
            P = E * Ps * mp.diag([1 / W, W]) * mp.diag([mp.exp(sgn * N * ph), mp.exp(-sgn * N * ph)])
            if conj: P = P * (-1) ** N
            R = mp.diag([1 / Dinf, Dinf]) * (P * mp.inverse(Nz) - mp.eye(2)) * mp.diag([Dinf, 1 / Dinf])
            res.append(f"{name}: {mp.nstr(max(abs(R[i,j]) for i in range(2) for j in range(2)), 4)}")
        print(f"   N={N} arg z={ang}pi: max|P N^-1 - I| ->", "   ".join(res))
