"""JZC M3a, gap G1 (JZC_M3a_H_G12.md §1): the Hurwitz outer scalar F_d = D_d B_d K for p > 1 (NUMERICAL, mpmath dps 40).
Hurwitz nodes at t in 1 + d + N_0 (t = n z^{-1/p}), -1 < d <= 0, a = 1 + d. Notation of Paper 2 Lemma binetcut with theta -> theta_d:
  j(u)   = LnGamma(u) - (u - 1/2) ln u + u - 1/2 ln 2pi              (Paper 2 §6, Binet's function)
  j_d(t) = LnGamma(t - d) - (t - d - 1/2) ln t + t - 1/2 ln 2pi,   D = kappa_d D~, D~ = e^{-j_d}, kappa_d+ = 1/(1 - e^{-2 pi i (t - d)})
  b_d(y) = 2 Im(-j_d(t_+) - Log(1 - e^{-2 pi i (t_+ - d)})),  B_d = exp(-(1/2pi) int_{-inf}^0 b_d(y)[1/(y-z) - 1/(y-1)] dy),  K = (4c - z)^{-1/2}.
Claims checked (G12 note numbering):
  L1.1  j_d(t) = j(t - d) + (t - d - 1/2) Log(1 - d/t) + d   (exact identity; random t in the sector |arg t| < pi/p)
  L1.2  |t j_d(t)| <= C_J := sec^2(pi/(2p))/6 + 2/3 for |t| >= 2, |arg t| <= pi/p  (grid sup, printed)
  L1.3  b_d(y) -> b_inf(d) = (pi/p - pi) + 2 pi d (1/p - 1), with |b_d - b_inf| / (|t| log(1/|t|)) bounded (printed)
  C1.5  F_nat := F_d (-z)^{-d} -> C_d uniformly in direction as z -> infinity (|z| = 1e30, arg z in {1e-3, pi/4, pi/2, 3pi/4, pi - 1e-3}),
        C_d real and positive, and
        log C_d = ln Gamma(1 + d) - (d + 1/2) ln n - 1/2 ln 2pi + (b_inf/2pi) ln 2 + I_r,  I_r = (1/2pi) int (b_d - b_inf 1_{y<-1}) dy/(y - 1).
  P1.4  (O5) near 0 for F_d: F_d(z) -> (4c)^{-1/2} B_d(0) as z -> 0 outside the lens (|z| = 1e-12, arg in {pi/3, pi/2, pi - 1e-3}).
c = 1 (c enters only K; the claims hold for every c > 0). n = 4. p in {3/2, 3}, d in {0, -0.3, -0.7, -0.95}."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 40
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi


def jb(u): return mp.loggamma(u) - (u - mp.mpf(1)/2)*mp.log(u) + u - mp.log(2*PI)/2
def jd(t, d): return mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*PI)/2


def logm(t, d):   # Log(1 - e^{-2 pi i (t - d)}), |e^{...}| < 1 for t in the lower half plane
    ex = -2*PI*I*(t - d)
    return mp.log(-mp.expm1(ex)) if mp.re(ex) > -500 else mp.mpc(0)


def tplus(y, n, p): return n*mp.power(-y, -1/p)*mp.expjpi(-1/p)
def bfun(y, n, p, d):
    tp = tplus(y, n, p); return 2*mp.im(-jd(tp, d) - logm(tp, d))
def binf(p, d): return (PI/p - PI) + 2*PI*d*(1/p - 1)


def logB(z, n, p, d, extra=()):
    f = lambda u: bfun(-mp.e**u, n, p, d)*(1/(-mp.e**u - z) - 1/(-mp.e**u - 1))*mp.e**u
    L = mp.log(abs(z)); pts = sorted(set([mp.mpf(-120), mp.mpf(-20), mp.mpf(0), L - 5, L, L + 5, L + 400] + [L + e for e in extra]))
    return -mp.quad(f, pts)/(2*PI)


def logB0(n, p, d):   # log B_d(0) = -(1/2pi) int b_d(y) [1/y - 1/(y-1)] dy
    f = lambda u: bfun(-mp.e**u, n, p, d)*(1/(-mp.e**u) - 1/(-mp.e**u - 1))*mp.e**u
    return -mp.quad(f, [-120, -20, 0, 20, 400])/(2*PI)


def logF(z, n, p, d, c, extra=()):    # z in C_+
    t = n*mp.power(z, -1/p)
    return -jd(t, d) - logm(t, d) + logB(z, n, p, d, extra) - mp.log(4*c - z)/2


def Ir(n, p, d):
    bi = binf(p, d)
    f = lambda u: (bfun(-mp.e**u, n, p, d) - (bi if u > 0 else 0))/(-mp.e**u - 1)*mp.e**u
    return mp.quad(f, [-120, -20, 0, 20, 100, 400])/(2*PI)


c = mp.mpf(1); n = mp.mpf(4)
mp.mp.dps = 40
# L1.1 exact identity, L1.2 explicit constant
rng = [mp.mpf(x) for x in ('0.37', '1.9', '7.3', '55.1', '1234.5')]
for p in (mp.mpf(3)/2, mp.mpf(3), mp.mpf(11)/10):
    for d in (mp.mpf(0), mp.mpf('-0.3'), mp.mpf('-0.95')):
        worst = 0
        for r in rng:
            for fr in (mp.mpf('-0.99'), mp.mpf('-0.5'), mp.mpf(0), mp.mpf('0.7'), mp.mpf('0.99')):
                t = r*mp.expjpi(fr/p)
                worst = max(worst, abs(jd(t, d) - (jb(t - d) + (t - d - mp.mpf(1)/2)*mp.log(1 - d/t) + d)))
        C_.check(f"L1.1 identity p={mp.nstr(p,3)} d={mp.nstr(d,2)}", float(worst), 0.0, 1e-35)
        CJ = mp.sec(PI/(2*p))**2/6 + mp.mpf(2)/3
        sup = max(abs(t*jd(t, d)) for t in (r*mp.expjpi(fr/p) for r in (2, 2.5, 4, 10, 100, 10**6)
                                            for fr in (-1, -0.75, -0.4, 0, 0.4, 0.75, 1)))
        print(f"L1.2 p={mp.nstr(p,3)} d={mp.nstr(d,2)}: sup |t j_d(t)| (|t|>=2) = {mp.nstr(sup,6)}  <=  C_J = {mp.nstr(CJ,6)}")
        C_.check(f"L1.2 |t j_d| <= C_J p={mp.nstr(p,3)} d={mp.nstr(d,2)}", float(max(sup - CJ, 0)), 0.0, 0.0)

for p in (mp.mpf(3)/2, mp.mpf(3)):
    for d in (mp.mpf(0), mp.mpf('-0.3'), mp.mpf('-0.7'), mp.mpf('-0.95')):
        lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,3)}"; bi = binf(p, d)
        # L1.3: limit density and rate
        rat = []
        for E in (10, 20, 30):
            y = -mp.mpf(10)**E; tt = abs(tplus(y, n, p))
            rat.append(abs(bfun(y, n, p, d) - bi)/(tt*mp.log(1/tt)))
        C_.check(f"L1.3 {lab}: b_d(-1e80) = b_inf", float(bfun(-mp.mpf(10)**80, n, p, d) - bi), 0.0, 1e-20)
        C_.check(f"L1.3 {lab}: |b_d - b_inf|/(|t|log(1/|t|)) bounded (<= 10)", float(max(rat)), 0.0, 10.0)
        # C1.5: uniform limit of F_nat and the closed form of C_d
        lC = mp.log(mp.gamma(1 + d)) - (d + mp.mpf(1)/2)*mp.log(n) - mp.log(2*PI)/2 + bi/(2*PI)*mp.log(2) + Ir(n, p, d)
        R = mp.mpf(10)**30; vals = []
        for ang in (mp.mpf('1e-3'), mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4, 1 - mp.mpf('1e-3')):
            z = R*mp.expjpi(ang); eps = mp.pi*min(ang, 1 - ang)
            ex = [s_*e for e in (eps, 10*eps, 100*eps) for s_ in (-1, 1)]
            vals.append(logF(z, n, p, d, c, ex) - d*(mp.log(z) - I*PI))      # Log(-z) = Log z - i pi on C_+
        spread = max(abs(v - lC) for v in vals)
        tol = 1e-12 if p < 2 else 1e-6
        print(f"L1.3 {lab}: max |b_d - b_inf|/(|t|log(1/|t|)) at y = -1e10, -1e20, -1e30: {mp.nstr(max(rat), 4)}")
        print(f"C1.5 {lab}: log C_d (closed form) = {mp.nstr(lC, 15)};  max over 5 rays |log F_nat(1e30 e^(i psi)) - log C_d| = {mp.nstr(spread, 3)}")
        C_.check(f"C1.5 {lab}: F_nat -> C_d on 5 rays incl. near both axes", float(spread), 0.0, tol)
        C_.check(f"C1.5 {lab}: C_d real", float(max(abs(mp.im(v)) for v in vals)), 0.0, tol)
        # P1.4: (O5) near 0, unchanged
        lim0 = -mp.log(4*c)/2 + logB0(n, p, d); w0 = 0
        for ang in (mp.mpf(1)/3, mp.mpf(1)/2, 1 - mp.mpf('1e-3')):
            z = mp.mpf(10)**-12*mp.expjpi(ang); eps = mp.pi*min(ang, 1 - ang)
            w0 = max(w0, abs(logF(z, n, p, d, c, [s_*e for e in (eps, 10*eps) for s_ in (-1, 1)]) - lim0))
        print(f"P1.4 {lab}: max |log F_d(1e-12 e^(i psi)) - log((4c)^(-1/2) B_d(0))| = {mp.nstr(w0, 3)}")
        C_.check(f"P1.4 {lab}: F_d -> (4c)^(-1/2) B_d(0) at 0 off the lens", float(w0), 0.0, 1e-5)
C_.finish()
