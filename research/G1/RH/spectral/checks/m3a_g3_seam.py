"""JZC M3a, gap G3 (JZC_M3a_H_G3.md): the Hurwitz outer scalar for 0 < p < 1 by the seam construction (NUMERICAL, mpmath dps 25).
Hurwitz nodes at t in 1 + d + N_0, t = n z^{-1/p}, -1 < d < 0.  Paper 2 app_outer.tex Lemma seam, with j -> j_d and the modified
elementary factors of JZC_M3a_H_G3.md §2:
  j_d(t) = LnGamma(t-d) - (t-d-1/2) ln t + t - 1/2 ln 2pi,  kappa_d,pm = 1/(1 - exp(-+2 pi i (t-d))),  D_d = kappa_d exp(-j_d(t)),
  w_d = (1/2 - 1/(2p))(1 + 2d) ... written as (1 - 1/p)(1/2 + d),  lam_d = (2pi)^{1+d}/(2|sin pi d| Gamma(-d))  (= Gamma(1+d)(2pi)^d),
  B_in = (1+z)^{w_d} (1+z)/(1+lam_d z),  B_out = (1 - z/(2 pi n))^{1/2+d},  K = (4c - z)^{-1/2},
  chi_+(zeta) = -j_d(t) - Log(1 - e^{-2pi i(t-d)}) + log B_in - log B_out on the seam arg zeta = pi p/2 (chi_- = conjugate),
  chi = Cauchy integral (Paper 2 eq. chi),  F_d = D_d B_in K e^chi in S_in,  B_out K e^chi in S_out.
Claims checked (asserted):
  (A) lam_d: the two closed forms agree (reflection formula);
  (B) seam densities: chi_+ -> 0 at both ends (|chi_+| at r = 1e-6 and r = 1e40); with Paper 2's lattice B_in, B_out instead,
      chi_+^lat - (d/p) Log zeta -> c_+ = ln Gamma(1+d) - d ln n - i pi d (the H-d memo's "(d/p) log zeta" growth, with its constant);
  (C) gluing: F_d continuous across the seam (inside/outside values at angular distance eps = 1e-4, 1e-6 differ by O(eps));
  (D) infinity: F_d(z)(-z)^{-d} -> C_d := (2 pi n)^{-1/2-d} on rays in S_in and S_out (|z| = 1e10, 1e14), fitted exponent = d;
  (E) zero: F_d(z) -> (4c)^{-1/2} e^{chi(0)} on a ray in S_in (off the lens) and one in S_out (nothing new at 0);
  (F) Lemma F.1(ii)_d: G(z) - G(1) equals the Cauchy integral of the pure jump l_pm = -Log(1 - e^{+-2 pi i d} e^{-2 pi n r^{-1/p}})
      (G = -j_d + log B_in + chi in S_in, log B_out + chi in S_out): the construction depends only on the jumps (uniqueness)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 25
C_ = Checks(); I = mp.mpc(0, 1); n = mp.mpf(4); c = mp.mpf(1)


def jd(t, d):                                      # extra digits: loggamma(t - d) ~ t log t cancels down to O(1/t)
    with mp.extradps(int(max(0, mp.log10(abs(t)))) + 10):
        return +(mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*mp.pi)/2)


class Seam:
    def __init__(s, p, d, lattice=False):
        s.p, s.d, s.th = p, d, mp.pi*p/2
        s.w = (1 - 1/p)*(mp.mpf(1)/2 + d); s.lam = mp.gamma(1 + d)*(2*mp.pi)**d; s.lat = lattice
        s.cache = {}

    def logBin(s, z):
        if s.lat: return (mp.mpf(1)/2 - 1/(2*s.p))*mp.log(1 + z)
        return (s.w + 1)*mp.log(1 + z) - mp.log(1 + s.lam*z)

    def logBout(s, z): return (mp.mpf(1)/2 if s.lat else mp.mpf(1)/2 + s.d)*mp.log(1 - z/(2*mp.pi*n))

    def t(s, z): return n*mp.exp(-mp.log(z)/s.p)

    def chip(s, r):                                   # density on Sigma_+ at zeta = r e^{i th}
        if r in s.cache: return s.cache[r]
        z = r*mp.expj(s.th); t = s.t(z); ex = -2*mp.pi*I*(t - s.d)
        lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -300 else mp.mpc(0)
        v = -jd(t, s.d) - lg + s.logBin(z) - s.logBout(z); s.cache[r] = v; return v

    def chi(s, z):
        e = mp.expj(s.th); L = mp.log(abs(z)); a = mp.arg(z)
        pts = sorted(set([mp.mpf(-30), s.p*mp.log(n), mp.mpf(0), mp.log(2*mp.pi*n), L - 3, L - mp.mpf('0.01'), L, L + mp.mpf('0.01'), L + 3, mp.mpf(110)]))
        if min(abs(a - s.th), abs(a + s.th)) < mp.mpf('1e-3'):     # near a seam: refine around |z|
            pts = sorted(set(pts + [L + k*mp.mpf(10)**-j for j in (3, 4, 5, 6, 7) for k in (-1, 1)]))
        f = lambda u: (s.chip(mp.e**u)*e/(mp.e**u*e - z) - mp.conj(s.chip(mp.e**u))*mp.conj(e)/(mp.e**u*mp.conj(e) - z))*mp.e**u
        return mp.quad(f, pts)/(2*mp.pi*I)

    def chi0(s):
        e = mp.expj(s.th)
        f = lambda u: s.chip(mp.e**u) - mp.conj(s.chip(mp.e**u))
        return mp.quad(f, [-30, s.p*mp.log(n), 0, mp.log(2*mp.pi*n), 110])/(2*mp.pi*I)

    def inside(s, z): return abs(mp.arg(z)) < s.th

    def logF(s, z, ch=None):
        ch = s.chi(z) if ch is None else ch
        K = -mp.log(4*c - z)/2
        if s.inside(z):
            t = s.t(z); sg = 1 if mp.im(z) > 0 else -1; ex = -sg*2*mp.pi*I*(t - s.d)
            lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -300 else mp.mpc(0)     # |e^ex| < e^-300: below working precision
            return -jd(t, s.d) - lg + s.logBin(z) + K + ch
        return s.logBout(z) + K + ch

    def G(s, z):                                       # E_plt1 §3's script-G (here with j_d and the modified B's)
        ch = s.chi(z)
        return (-jd(s.t(z), s.d) + s.logBin(z) + ch) if s.inside(z) else (s.logBout(z) + ch)

    def Jpure(s, z):
        e = mp.expj(s.th); q = mp.expj(2*mp.pi*s.d)
        Kk = lambda zeta: (z - 1)/((zeta - z)*(zeta - 1))
        def f(u):
            r = mp.e**u; em = mp.expm1(-2*mp.pi*n*r**(-1/s.p))
            lp = -mp.log((1 - q) - q*em); lm = -mp.log((1 - 1/q) - em/q)
            return (e*lp*Kk(r*e) - mp.conj(e)*lm*Kk(r*mp.conj(e)))*r
        L = mp.log(abs(z))
        return mp.quad(f, sorted(set([mp.mpf(-30), s.p*mp.log(n), mp.mpf(0), L - mp.mpf('0.5'), L, L + mp.mpf('0.5'), mp.mpf(110)])))/(2*mp.pi*I)


for p in (mp.mpf('0.3'), mp.mpf('0.6'), mp.mpf('0.75')):
    for d in (mp.mpf('-0.25'), mp.mpf('-0.5'), mp.mpf('-0.8')):
        lab = f"p={mp.nstr(p, 2)} d={mp.nstr(d, 2)}"; S = Seam(p, d); Sl = Seam(p, d, lattice=True)
        # (A)
        C_.check(f"{lab}: lam_d closed forms", float(abs(S.lam - (2*mp.pi)**(1 + d)/(2*abs(mp.sin(mp.pi*d))*mp.gamma(-d)))), 0.0, 1e-20)
        # (B)
        b0, binf = abs(S.chip(mp.mpf(10)**-6)), abs(S.chip(mp.mpf(10)**40))
        cp = mp.loggamma(1 + d) - d*mp.log(n) - I*mp.pi*d; z40 = mp.mpf(10)**40*mp.expj(S.th)
        glat = abs(Sl.chip(mp.mpf(10)**40) - d/p*mp.log(z40) - cp)
        C_.check(f"{lab}: chi_+ -> 0 at 0", float(b0), 0.0, 1e-5); C_.check(f"{lab}: chi_+ -> 0 at inf", float(binf), 0.0, 1e-22)
        C_.check(f"{lab}: lattice-B density = (d/p)Log zeta + c_+ + o(1)", float(glat), 0.0, 1e-22)
        # (C) gluing at r = 2 and r = 2e3
        glue = []
        for r in (mp.mpf(2), mp.mpf(2000)):
            for eps in (mp.mpf(10)**-4, mp.mpf(10)**-6):
                zi, zo = r*mp.expj(S.th - eps), r*mp.expj(S.th + eps)
                glue.append(abs(mp.exp(S.logF(zi) - S.logF(zo)) - 1)/eps)
        C_.check(f"{lab}: F continuous across the seam (|jump|/eps)", float(max(glue)), 0.0, 50.0)
        # (D) infinity
        Cd = (2*mp.pi*n)**(-mp.mpf(1)/2 - d); worst = 0; ex = []
        for ang in (S.th/2, -S.th/2, mp.pi/2, 3*mp.pi/4, -0.95*mp.pi):
            Fz = {}
            for R in (mp.mpf(10)**10, mp.mpf(10)**14):
                z = R*mp.expj(ang); Fz[R] = S.logF(z)
                worst = max(worst, abs(mp.exp(Fz[R] - d*mp.log(-z))/Cd - 1) if R > 10**12 else 0)
            ex.append(mp.re(Fz[mp.mpf(10)**14] - Fz[mp.mpf(10)**10])/mp.log(mp.mpf(10)**4) - d)
        C_.check(f"{lab}: F (-z)^-d / (2pi n)^(-1/2-d) -> 1 on 5 rays (|z|=1e14)", float(worst), 0.0, 1e-8)
        C_.check(f"{lab}: fitted exponent of |F| = d on 5 rays", float(max(abs(x) for x in ex)), 0.0, 1e-8)
        # (E) zero
        ch0 = S.chi0(); F0 = mp.exp(ch0)/mp.sqrt(4*c); dz = []
        for ang in (mp.mpf('0.45')*mp.pi*p, mp.pi/2):
            for rho in (mp.mpf(10)**-8,):
                dz.append(abs(mp.exp(S.logF(rho*mp.expj(ang)))/F0 - 1))
        C_.check(f"{lab}: F -> (4c)^(-1/2) e^chi(0) at 0 from S_in and S_out", float(max(dz)), 0.0, 1e-5)
        # (F) uniqueness: G(z) - G(1) = pure-jump Cauchy integral
        G1 = S.G(mp.mpf(1)); dF = []
        for z in (2*mp.expj(S.th/4), mp.mpf('0.3'), mp.mpf('1.5')*mp.expj(mp.mpf('0.8')*mp.pi), 50*mp.expj(-S.th/3)):
            dF.append(abs(S.G(z) - G1 - S.Jpure(z)))
        C_.check(f"{lab}: G(z) - G(1) = Cauchy integral of the jump l_d (4 points)", float(max(dF)), 0.0, 1e-12)
        print(f"{lab}: lam={mp.nstr(S.lam, 10)} |chi+(1e-6)|={mp.nstr(b0, 2)} |chi+(1e40)|={mp.nstr(binf, 2)} lattice-B dev={mp.nstr(glat, 2)} | "
              f"glue max |jump|/eps={mp.nstr(max(glue), 3)} | at inf: max|F(-z)^-d/C_d - 1|={mp.nstr(worst, 2)}, max|exp-d|={mp.nstr(max(abs(x) for x in ex), 2)} | "
              f"chi(0)={mp.nstr(mp.re(ch0), 8)} (Im {mp.nstr(mp.im(ch0), 1)}), at 0 dev={mp.nstr(max(dz), 2)} | F.1(ii)_d dev={mp.nstr(max(dF), 2)}", flush=True)
C_.finish()
