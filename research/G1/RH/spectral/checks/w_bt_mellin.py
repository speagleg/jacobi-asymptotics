"""JZC_W_BT Lemmas BT.2-BT.3: numerical checks (Rule N: NUMERICAL, mpmath, stated precision) of the analytic inputs of the
lip-mismatch computation. Nothing here is fitted.

(1) Lemma BT.3(i): K(s) := int_0^inf w^{s-1} K_nu(w)^2 dw = 2^{s-3} Gamma(s/2+nu) Gamma(s/2-nu) Gamma(s/2)^2/Gamma(s), Re s > 2|nu|
    (proved from DLMF 10.32.9, 5.2.1, 5.12.3, 5.12.1); quadrature at 6 (s, nu).
(2) Lemma BT.3(ii): K(s+2) = q(s) K(s), q(s) = (s^2 - 4nu^2) s/(4(s+1)); M_3(s) := int w^{s-1} K K' = -((s-1)/2) K(s-1);
    M_2(s) := int w^{s-1} K'^2 = [(s-2)^2/2 - nu^2] K(s-2) - K(s)  (integration by parts and the ODE derived from 10.32.9).
(3) Lemma BT.3(iii): tan(pi rho) sin(pi(rho - nu)) K(2rho+2) = -2^{2rho} pi^2 Phi_nu(rho) (5.5.3 only).
(4) Lemma BT.1 inputs: M zeta^{s3/4}(2pi)^{s3/2} Phi_nu(zeta) = sum_k s3 Xi_k s3 (2 zeta^{1/2})^{-k} (asymptotic; the frame of the
    engine's Delta_k), and L(zeta) := M zeta^{s3/4}(2pi)^{s3/2}[e^{-4 zeta^{1/2}} Phi E21 Phi^{-1}](2pi)^{-s3/2} zeta^{-s3/4} M^{-1}
    = (w/pi) M [[i K K', K^2], [K'^2, -i K K']] M^{-1}, w = 2 zeta^{1/2}, at real and complex (lip-ray) zeta.
(5) Lemma BT.2 (deformation): for F(s) = G(s) L(-kappa n^2 s) with G entire, the lip integrals
    sum_{+/-} int_{lip+/-, away from 0} varrho_+/- (+/- i) s^rho F(s) ds = 2 sin(pi(rho - nu)) int_0^delta x^rho F(-x) dx + O(e^{-cn}),
    varrho_+/- = e^{-/+ i pi nu}; checked by direct quadrature on the rays at arg s = +/- theta.
Controls (must fail): (1) with Gamma(s/2) in place of Gamma(s/2)^2/Gamma(s) * 2^{s-1}...; (3) with sin(pi(rho+nu));
(5) with 2 cos(pi(rho - nu)); (4) with the K^2 and K'^2 entries swapped."""
import os, sys, hashlib
import mpmath as mp
print(f"sha256 {os.path.basename(__file__)}: {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}", flush=True)
mp.mp.dps = 30
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'numerical'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
def Kc(s, nu): return 2**(s - 3)*mp.gamma(s/2 + nu)*mp.gamma(s/2 - nu)*mp.gamma(s/2)**2/mp.gamma(s)
def Kp(nu, w): return -(mp.besselk(nu - 1, w) + mp.besselk(nu + 1, w))/2      # K' (cross-checked by mp.diff below)
def quadK(s, nu, f): return mp.quad(lambda w: w**(s - 1)*f(w), [0, mp.mpf(1)/100, mp.mpf(1)/10, 1, 5, 20, mp.inf])
w0 = mp.mpf("0.7")
chk("K'_nu by (K_{nu-1}+K_{nu+1})/(-2) equals mp.diff (nu = 0.3, w = 0.7), rel < 1e-25",
    abs(Kp(mp.mpf("0.3"), w0)/mp.diff(lambda t: mp.besselk(mp.mpf("0.3"), t), w0) - 1) < 1e-25)
# (1)
dev = 0; cases = [(mp.mpf("2.74"), mp.mpf("0.3")), (mp.mpf("3.5"), mp.mpf("-0.45")), (mp.mpf("1.6"), mp.mpf(0)),
                  (mp.mpf("4.2"), mp.mpf("0.8")), (mp.mpf("2.2"), mp.mpf("0.9")), (mp.mpf("6.0"), mp.mpf("0.25"))]
for s, nu in cases:
    q = quadK(s, nu, lambda w: mp.besselk(nu, w)**2); dev = max(dev, abs(q/Kc(s, nu) - 1))
chk(f"(1) K(s) closed form vs quadrature at 6 (s, nu): max rel dev {mp.nstr(dev, 3)} < 1e-12 (tanh-sinh at the endpoint singularity w^(s-1-2|nu|) limits the precision)", dev < 1e-12)
s, nu = cases[0]
chk("(1) control: closed form without the factor Gamma(s/2)/Gamma(s) 2^{s-1}... (i.e. sqrt(pi)Gamma(s/2+nu)Gamma(s/2-nu)/4)",
    abs(quadK(s, nu, lambda w: mp.besselk(nu, w)**2)/(mp.sqrt(mp.pi)*mp.gamma(s/2 + nu)*mp.gamma(s/2 - nu)/4) - 1) < 1e-10, must_fail=True)
# (2)
dev = 0
for s, nu in [(mp.mpf("3.74"), mp.mpf("0.3")), (mp.mpf("4.5"), mp.mpf("-0.45")), (mp.mpf("5.1"), mp.mpf("0.8"))]:
    qs = (s*s - 4*nu*nu)*s/(4*(s + 1))
    dev = max(dev, abs(Kc(s + 2, nu)/(qs*Kc(s, nu)) - 1))
    m3 = quadK(s, nu, lambda w: mp.besselk(nu, w)*Kp(nu, w)); dev = max(dev, abs(m3/(-(s - 1)/2*Kc(s - 1, nu)) - 1))
    m2 = quadK(s, nu, lambda w: Kp(nu, w)**2); dev = max(dev, abs(m2/(((s - 2)**2/2 - nu*nu)*Kc(s - 2, nu) - Kc(s, nu)) - 1))
chk(f"(2) recurrence q(s), M_3 and M_2 reductions vs quadrature at 3 (s, nu): max rel dev {mp.nstr(dev, 3)} < 1e-20", dev < 1e-20)
# (3)
def Phi(nu, r): return mp.gamma(-1 - 2*r)*mp.gamma(nu + r + 1)*mp.rgamma(-r)**2*mp.rgamma(nu - r)
dev = 0
for r, nu in [(mp.mpf("0.37"), mp.mpf("0.3")), (mp.mpf(2)/3, mp.mpf("-0.4")), (mp.mpf("1.3"), mp.mpf("0.25")), (mp.mpf("0.2"), mp.mpf(0))]:
    dev = max(dev, abs(mp.tan(mp.pi*r)*mp.sin(mp.pi*(r - nu))*Kc(2*r + 2, nu)/(-2**(2*r)*mp.pi**2*Phi(nu, r)) - 1))
chk(f"(3) tan(pi rho) sin(pi(rho-nu)) K(2rho+2) = -2^(2rho) pi^2 Phi_nu(rho) at 4 points: max rel dev {mp.nstr(dev, 3)}", dev < 1e-25)
r, nu = mp.mpf("0.37"), mp.mpf("0.3")
chk("(3) control: sin(pi(rho+nu))", abs(mp.tan(mp.pi*r)*mp.sin(mp.pi*(r + nu))*Kc(2*r + 2, nu)/(-2**(2*r)*mp.pi**2*Phi(nu, r)) - 1) < 1e-10,
    must_fail=True)
# (4)
s3 = mp.matrix([[1, 0], [0, -1]]); M = mp.matrix([[1, 1j], [1j, 1]])/mp.sqrt(2); Mi = M**-1
E21 = mp.matrix([[0, 0], [1, 0]])
def D(a): return mp.matrix([[a, 0], [0, 1/a]])
def Psi(z, nu):
    sq = mp.sqrt(z); w = 2*sq
    Ip = (mp.besseli(nu - 1, w) + mp.besseli(nu + 1, w))/2
    return mp.matrix([[mp.besseli(nu, w), 1j/mp.pi*mp.besselk(nu, w)], [2j*mp.pi*sq*Ip, -2*sq*Kp(nu, w)]])
def Phim(z, nu):
    sq = mp.sqrt(z); return s3*Psi(z, nu)*s3*mp.matrix([[mp.exp(-2*sq), 0], [0, mp.exp(2*sq)]])
def Xi(k, nu):
    a = mp.mpf(1); b = mp.mpf(1)
    for j in range(1, k + 1): a *= (4*nu**2 - (2*j - 1)**2)
    for j in range(1, k): b *= (4*nu**2 - (2*j - 1)**2)
    b *= (4*nu**2 + 4*k**2 - 1); d = mp.factorial(k)*8**k; a, b = a/d, b/d; sg = (-1)**k
    C = mp.matrix([[a*sg, a], [b*sg, b]]); H = mp.matrix(2, 2)
    for i in range(2):
        for j in range(2): H[i, j] = M[i, j]*C[i, j]
    return Mi*H
nu = mp.mpf("0.3"); z = mp.mpf(400)
lhs = M*D(z**mp.mpf("0.25"))*D(mp.sqrt(2*mp.pi))*Phim(z, nu); rhs = mp.eye(2)
for k in range(1, 12): rhs += s3*Xi(k, nu)*s3*(2*mp.sqrt(z))**(-k)
chk(f"(4) frame: M zeta^(s3/4)(2pi)^(s3/2) Phi = sum s3 Xi_k s3 (2 zeta^(1/2))^-k at zeta = 400, 11 terms (dev {mp.nstr(mp.mnorm(lhs - rhs, 1), 3)} < 1e-14)",
    mp.mnorm(lhs - rhs, 1) < 1e-14)
def Lphi(z, nu):
    B = mp.exp(-4*mp.sqrt(z))*Phim(z, nu)*E21*Phim(z, nu)**-1
    return M*D(z**mp.mpf("0.25"))*D(mp.sqrt(2*mp.pi))*B*D(mp.sqrt(2*mp.pi))**-1*D(z**mp.mpf("0.25"))**-1*Mi
def Lcl(z, nu, swap=False):
    w = 2*mp.sqrt(z); K = mp.besselk(nu, w); Kq = Kp(nu, w)
    a, b = (Kq**2, K**2) if swap else (K**2, Kq**2)
    return (w/mp.pi)*M*mp.matrix([[1j*K*Kq, a], [b, -1j*K*Kq]])*Mi
dev = 0; nrm = 0
for z in [mp.mpf("0.7"), mp.mpf(3), 2*mp.exp(2j*mp.pi/3*mp.mpf("0.95")), mp.mpf("1.5")*mp.exp(-2j*mp.pi/3*mp.mpf("0.95"))]:
    for nu in (mp.mpf("0.3"), mp.mpf("-0.6")):
        dev = max(dev, mp.mnorm(Lphi(z, nu) - Lcl(z, nu), 1)/mp.mnorm(Lcl(z, nu), 1))
chk(f"(4) L(zeta) closed form vs its definition from Phi_nu (real and lip-ray zeta, nu = 0.3, -0.6): max rel dev {mp.nstr(dev, 3)} < 1e-25", dev < 1e-25)
chk("(4) control: K^2 and K'^2 swapped", mp.mnorm(Lphi(mp.mpf("0.7"), mp.mpf("0.3")) - Lcl(mp.mpf("0.7"), mp.mpf("0.3"), swap=True), 1) < 1e-10, must_fail=True)
# (5) deformation: G(s) = [[1 + s, 2 - s^2], [s/3, 1]] (entire), kappa = 1/(p+2)^2 with p = 1.5, n = 12, delta = 0.3
mp.mp.dps = 25
def Gm(s): return mp.matrix([[1 + s, 2 - s*s], [s/3, 1]])
def F(s, nu, kap, n): return Gm(s)*Lcl(-kap*n*n*s, nu)
def lipint(r, nu, kap, n, th, dl, cosctl=False):
    tot = mp.matrix(2, 2)
    for sg in (1, -1):
        e = mp.exp(1j*sg*th); vr = mp.exp(-1j*sg*mp.pi*nu)
        def f(t, i, j):
            s = t*e; return vr*(1j*sg)*s**r*F(s, nu, kap, n)[i, j]*e
        for i in range(2):
            for j in range(2):
                tot[i, j] += mp.quad(lambda t: f(t, i, j), [0, mp.mpf(1)/n**2, mp.mpf(1)/n, dl])
    neg = mp.matrix(2, 2)
    for i in range(2):
        for j in range(2):
            neg[i, j] = mp.quad(lambda x: x**r*F(-x, nu, kap, n)[i, j], [0, mp.mpf(1)/n**2, mp.mpf(1)/n, dl])
    fac = 2*mp.cos(mp.pi*(r - nu)) if cosctl else 2*mp.sin(mp.pi*(r - nu))
    return tot, fac*neg
dev = 0
for r, nu in [(mp.mpf("0.37"), mp.mpf("0.3")), (mp.mpf("1.2"), mp.mpf("-0.4"))]:
    a, b = lipint(r, nu, 1/mp.mpf("3.5")**2, 100, mp.pi/3, mp.mpf("0.3"))
    dev = max(dev, mp.mnorm(a - b, 1)/mp.mnorm(b, 1))
chk(f"(5) lip integrals (rays at arg s = +/- pi/3, n = 100, delta = 0.3) = 2 sin(pi(rho-nu)) int_0^delta x^rho F(-x) dx: max rel dev {mp.nstr(dev, 3)} < 1e-7 (quadrature-limited; arc term ~e^-31)",
    dev < 1e-7)
a, b = lipint(mp.mpf("0.37"), mp.mpf("0.3"), 1/mp.mpf("3.5")**2, 100, mp.pi/3, mp.mpf("0.3"), cosctl=True)
chk("(5) control: 2 cos(pi(rho-nu)) in place of 2 sin", mp.mnorm(a - b, 1)/mp.mnorm(b, 1) < 1e-8, must_fail=True)
print(f"total {NCHK} checks")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
