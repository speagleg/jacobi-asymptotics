"""JZC M3a, lemma H-d (JZC_M3a_Hd.md §2): the Hurwitz outer scalar at z -> infinity (NUMERICAL, mpmath dps 30, p > 1).
Hurwitz lattice nodes at t in 1 + delta + N_0 (t = n z^{-1/p}), -1 < delta <= 0. Paper 2's construction with the shifted phase:
  j_d(t) = LnGamma(t - d) - (t - d - 1/2) ln t + t - 1/2 ln(2 pi),  Dt = exp(-j_d(t)),  kappa_pm = 1/(1 - exp(-+2 pi i (t - d))),
  D = kappa_pm Dt (z in C_pm),  b_d(y) = 2 Im(-j_d(t_+) - Log(1 - exp(-2 pi i (t_+ - d)))) on y < 0   (SPEC §3.1, Paper 2 (B)),
  B = exp(-(1/2pi) int_{-inf}^0 b_d(y) [1/(y - z) - 1/(y - 1)] dy)                                     (Paper 2 eq. (B)),
  F_d = D B K,  K = (4c - z)^{-1/2}                                                                     (Paper 2 Lemma outer).
Claims checked:
  (1) b_d(y) -> b_inf(d) := (pi/p - pi) + 2 pi d (1/p - 1) as y -> -inf (closed form, JZC_M3a_Hd.md (2.3));
  (2) |D_d| |t|^{d + 1/2} -> Gamma(1 + d)/sqrt(2 pi) as t -> 0 in the sector (|kappa| -> 1/(2|sin pi d|));
  (3) F_d(z) (-z)^{-d} -> a nonzero constant as z -> infinity (|z| = R1 = 1e16, R2 = 1e24), the same along three rays in C_+ (so F_d ~ C (-z)^d: the outer
      scalar's power at infinity is exactly delta, independent of p; delta = 0 is Paper 2's |F(iy)| ~ 1).
  (4) hard edge (t -> infinity): 2t j_d(t) -> B_2(-d) = d^2 + d + 1/6 (the Bernoulli-polynomial Stirling term; DLMF 5.11.8 NOT
      QUOTED, checked here directly), so H_n^d keeps Paper 2's Hoelder behaviour at 0 and the Bessel order is unchanged.
Exploratory (printed, not asserted): the same exponent for delta = +1/2 (outside -1 < delta <= 0)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 30
C_ = Checks(); I = mp.mpc(0, 1)


def jd(t, d): return mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*mp.pi)/2


def bfun(y, n, p, d):
    tp = n*mp.power(-y, -1/p)*mp.expjpi(-1/p)
    ex = -2*mp.pi*I*(tp - d)
    lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -400 else mp.mpc(0)     # |e^ex| < e^-400: below working precision
    return 2*mp.im(-jd(tp, d) - lg)


def logB(z, n, p, d):
    f = lambda u: bfun(-mp.e**u, n, p, d)*(1/(-mp.e**u - z) - 1/(-mp.e**u - 1))*mp.e**u
    L = mp.log(abs(z)); pts = sorted(set([mp.mpf(-90), mp.mpf(-20), mp.mpf(0), L - 5, L, L + 5, L + 90]))
    return -mp.quad(f, pts)/(2*mp.pi)


def logF(z, n, p, d, c):
    assert mp.im(z) > 0
    t = n*mp.power(z, -1/p)
    logD = -jd(t, d) - mp.log(-mp.expm1(-2*mp.pi*I*(t - d)))      # z in C_+: kappa_+ = 1/(1 - e^{-2 i theta_d})
    return logD + logB(z, n, p, d) - mp.log(4*c - z)/2


c = mp.mpf(1)            # the value of c only enters K = (4c - z)^{-1/2}, irrelevant at infinity
n = mp.mpf(4)
for p in (mp.mpf(3)/2, mp.mpf(3)):
    R1, R2 = mp.mpf(10)**16, mp.mpf(10)**24
    for d in (mp.mpf(0), mp.mpf('-0.3'), mp.mpf('-0.7')):
        lab = f"p={mp.nstr(p, 3)} d={mp.nstr(d, 2)}"
        binf = (mp.pi/p - mp.pi) + 2*mp.pi*d*(1/p - 1)
        C_.check(f"{lab}: b_d(-1e40) = b_inf", float(bfun(-mp.mpf(10)**40, n, p, d) - binf), 0.0, 1e-9)
        tb = mp.mpf(10)**8*mp.expjpi(-mp.mpf(1)/(3*p))
        C_.check(f"{lab}: 2t j_d(t) -> B_2(-d) at |t| = 1e8", float(abs(2*tb*jd(tb, d) - (d*d + d + mp.mpf(1)/6))), 0.0, 1e-7)
        if d != 0:
            t = mp.mpf(10)**-12*mp.expjpi(-mp.mpf(1)/(3*p))
            D = mp.exp(-jd(t, d))/(-mp.expm1(-2*mp.pi*I*(t - d)))
            C_.check(f"{lab}: |D| |t|^(d+1/2) -> Gamma(1+d)/sqrt(2pi)", float(abs(D)*abs(t)**(d + mp.mpf(1)/2) - mp.gamma(1 + d)/mp.sqrt(2*mp.pi)), 0.0, 1e-9)
        vals = {}
        for ang in (mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4):
            for R in (R1, R2):
                z = R*mp.expjpi(ang)
                vals[(ang, R)] = logF(z, n, p, d, c) - d*mp.log(-z)
        cst = vals[(mp.mpf(1)/2, R2)]
        spread = max(abs(v - cst) for k, v in vals.items() if k[1] == R2)
        drift = max(abs(vals[(a, R1)] - vals[(a, R2)]) for a in (mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4))
        # exponent fitted from the modulus along iy
        e_fit = (mp.re(logF(I*R2, n, p, d, c)) - mp.re(logF(I*R1, n, p, d, c)))/mp.log(R2/R1)
        print(f"{lab}: log F_d(z) - d log(-z) at |z| = R2 (arg z = pi/2): {mp.nstr(cst, 12)};  spread over 3 rays {mp.nstr(spread, 3)};"
              f"  drift R1 -> R2 {mp.nstr(drift, 3)};  fitted exponent of |F_d(iy)| {mp.nstr(e_fit, 10)}", flush=True)
        C_.check(f"{lab}: F_d (-z)^-d: same constant on three rays", float(spread), 0.0, 1e-5)
        C_.check(f"{lab}: F_d (-z)^-d: converged (R1 vs R2)", float(drift), 0.0, 1e-4)
        C_.check(f"{lab}: exponent of |F_d(iy)| = delta", float(e_fit - d), 0.0, 1e-5)
# exploratory: delta = +1/2 (the lattice {(k+1/2)^p}_{k>=1} = the delta = -1/2 lattice minus its top node)
p, d = mp.mpf(3)/2, mp.mpf(1)/2
e_fit = (mp.re(logF(I*mp.mpf(10)**14, n, p, d, c)) - mp.re(logF(I*mp.mpf(10)**10, n, p, d, c)))/mp.log(mp.mpf(10)**4)
print(f"exploratory p=1.5 d=+0.5: b_d(-1e40) = {mp.nstr(bfun(-mp.mpf(10)**40, n, p, d), 12)} (formula b_inf {mp.nstr((mp.pi/p - mp.pi) + 2*mp.pi*d*(1/p - 1), 12)});"
      f" fitted exponent of |F_d(iy)| {mp.nstr(e_fit, 10)}")
C_.finish()
