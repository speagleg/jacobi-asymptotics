"""JZC_W_outer §3-§5 (NUMERICAL, mpmath): the normalised outer scalar for lam_k = (k + d)^p + kappa, p > 1.
Notation (JZC_W_outer.md):
  t(z) = n z^{-1/p} (lattice), zeta(z) = z/(1 - z/zs), zs = n^p/kappa (Moebius index map), t_k(z) = t(zeta(z)) = (n^p/z - kappa)^{1/p};
  Phi_d := kappa_d D~_d B_d (the Hurwitz scalar of JZC_M3a_H_G12 without K), K = (4c - z)^{-1/2};
  F_k(z) := Phi_d(zeta(z)) K(z);  G_k := (-z)^{-d} E_k,  E_k := exp(C[rho1]),
  C[rho](z) := int_0^inf rho(y)[1/(y - z) - 1/(y + 1)] dy (+ for kappa < 0: int_{-inf}^{-|zs|} rho~(y)[1/(y - z) - 1/(y - 1)] dy);
  rho1 = t - t_k on (0, zs) [kappa > 0] or (0, inf) [kappa < 0];  rho1 = t - d - 1/2 on (zs, inf) [kappa > 0];
  rho~ = 1/2 + d - t_k on (-inf, -|zs|) [kappa < 0];   F_nat := F_k G_k.
Claims checked (labels of JZC_W_outer.md):
  [O1]  F_nat_+ / F_nat_- = e^{2 pi i t(x)} on (4c, inf) (lattice phase), at points between nodes and beyond zs; and
        F_k_+/F_k_- = e^{2 i theta_k} on (4c, zs), = -1 on (zs, inf) (kappa > 0), F_nat continuous across (-inf, 0) (kappa < 0).
  [zs]  F_nat bounded above and below near zs (kappa > 0) / -|zs| (kappa < 0); |F_k| ~ r^{-(d+1/2)}, |G_k| ~ r^{d+1/2} there.
  [inf] F_nat(R e^{i psi}) -> C_kappa (same constant on 4 rays, R = 1e20 vs 1e30); F_k ~ (-z)^{-1/2}: the fixed-n exponent of the
        UN-normalised scalar at infinity is -1/2, not d = -Z(0) - 1/2 (control: the literal reading "F_k ~ C(-z)^{-Z(0)-1/2} at
        infinity" fails), and G_k ~ (-z)^{+1/2}.
  [0]   hard edge: G_k(z)(-z)^d -> E_k(0) (exponent of the gauge at 0 is -d = Z(0) + 1/2: the Szego shift beta' = alpha + 2d);
        F_k(z)/F_d(z) -> 1 (Hurwitz scalar; nothing changes at 0).
  [W5]  decomposition of C[rho1] near 0: C[rho1](z) = C0 + sum_m a_m n^{-p q_m}(-pi/sin(pi q_m))(-z)^{q_m} + FP_1 z + FP_2 z^2 + ...,
        q_m = m - 1/p, a_m = -binom(1/p, m)(-kappa)^m, FP_j = zeta(0, a) kappa^j n^{-jp}/j (the gauge's share of Z_kappa(-j)).
  [W4]  jump algebra on the band: W_k/(F~_+ F~_-) = x^{alpha + 2d}(4c - x) r_n (D~B)(zeta)^{-2} e^{-2 PV C[rho1]} (real, > 0);
        lip phase: (W_k/F~^2)(x + i0) e^{2 pi i d} / W0(x) = e^{-2 pi i rho1(x)}; Sigma_v phase cancellation
        e^{-2 i theta_k} W_k/F~^2 = e^{-2 i theta} W0^k(z) at points of C_+ (W0^k continued with Psi0 = C - i pi rho1).
Controls (must fail): wrong branch on (zs, inf) (rho1 -/+ 1): F_nat ~ r^{-/+1} at zs and |z|^{+/-1} at infinity; no gauge Delta-part
  (G = (-z)^{-d} only, Hurwitz): the jump on (4c, inf) is wrong; the literal exponent d at infinity for F_k.
n = 4, c = 1 (c enters only through K and the band), w_n = 1.  dps 30."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from w_common import Checks
mp.mp.dps = 30
I = mp.mpc(0, 1); PI = mp.pi; HALF = mp.mpf(1)/2
C_ = Checks()


def say(*a): print(*a, flush=True)


# ---------------- Hurwitz scalar (copied from m3a_g12_outer.py, which runs its checks on import) ----------------
def jd(t, d): return mp.loggamma(t - d) - (t - d - HALF)*mp.log(t) + t - mp.log(2*PI)/2
def logm(t, d):                       # Log(1 - e^{-2 pi i (t - d)}) for t in the closed lower half plane (|.| <= 1)
    ex = -2*PI*I*(t - d)
    return mp.log(-mp.expm1(ex)) if mp.re(ex) > -500 else mp.mpc(0)
def tplus(y, n, p): return n*mp.power(-y, -1/p)*mp.expjpi(-1/p)
def bfun(y, n, p, d):
    tp = tplus(y, n, p); return 2*mp.im(-jd(tp, d) - logm(tp, d))


def logB(z, n, p, d):
    """log B_d(z), z in C_+ (Cauchy integral over (-inf, 0) in u = log|y|)"""
    f = lambda u: bfun(-mp.e**u, n, p, d)*(1/(-mp.e**u - z) - 1/(-mp.e**u - 1))*mp.e**u
    L = mp.log(abs(z)); ang = PI - mp.arg(z)                  # distance in angle from the negative axis
    ex = [s_*e for e in (ang, 10*ang, 100*ang) for s_ in (-1, 1) if e < 5]
    pts = sorted(set([mp.mpf(-150), mp.mpf(-20), mp.mpf(0), L - 5, L, L + 5, mp.mpf(400)] + [L + e for e in ex]))
    return -mp.quad(f, pts)/(2*PI)


def logPhi_up(zeta, n, p, d):        # log Phi_d(zeta) = log(kappa_d+ D~_d B_d), zeta in C_+ (principal t)
    t = n*mp.power(zeta, -1/p)
    return -jd(t, d) - logm(t, d) + logB(zeta, n, p, d)


def logPhi(zeta, n, p, d):
    return logPhi_up(zeta, n, p, d) if mp.im(zeta) > 0 else mp.conj(logPhi_up(mp.conj(zeta), n, p, d))


def logDB(zeta, n, p, d):            # log (D~_d B_d)(zeta) = log Phi - log kappa_d
    if mp.im(zeta) < 0: return mp.conj(logDB(mp.conj(zeta), n, p, d))
    t = n*mp.power(zeta, -1/p); return -jd(t, d) + logB(zeta, n, p, d)


# ---------------- the kappa objects ----------------
class Kap:
    def __init__(s, p, d, kap, n=4, c=1, branch=0, gauge=True):
        s.p, s.d, s.k, s.n, s.c = mp.mpf(p), mp.mpf(d), mp.mpf(kap), mp.mpf(n), mp.mpf(c)
        s.zs = s.n**s.p/s.k; s.branch = branch; s.gauge = gauge
        s.tinf = abs(s.k)**(1/s.p)
    def zeta(s, z): return z/(1 - z/s.zs)
    def t(s, z): return s.n*mp.power(z, -1/s.p)
    def tk(s, z): return s.t(s.zeta(z))
    def rho1(s, y):                    # y > 0 real
        if s.k > 0 and y > s.zs: return s.n*y**(-1/s.p) - s.d - HALF + s.branch
        u = y/s.zs                       # = kappa y/n^p (signed)
        return -s.n*y**(-1/s.p)*mp.expm1(mp.log1p(-u)/s.p)        # t - t_k = t (1 - (1-u)^{1/p})
    def rhot(s, y):                    # y < -|zs| (kappa < 0)
        return HALF + s.d - (s.n**s.p/y - s.k)**(1/s.p)
    def Cr(s, z):
        """C[rho1](z) (+ the (-inf, -|zs|) piece for kappa < 0); z off the supports"""
        if not s.gauge: return mp.mpc(0)
        L = mp.log(abs(z)); A = abs(mp.arg(z)); ex = [sg*e for e in (A, 10*A, 100*A) for sg in (-1, 1) if e < 5]
        f = lambda u: s.rho1(mp.e**u)*(1/(mp.e**u - z) - 1/(mp.e**u + 1))*mp.e**u
        lz = mp.log(abs(s.zs))
        pts = sorted(set([mp.mpf(-200), mp.mpf(-40), mp.mpf(0), lz, L - 5, L, L + 5, mp.mpf(500)] + [L + e for e in ex]
                         + ([lz + e for e in (-1e-3, -1e-6, 1e-6, 1e-3)] if s.k > 0 else [])))
        v = mp.quad(f, pts)
        if s.k < 0:
            B = PI - A
            exn = [sg*e for e in (B, 10*B, 100*B) for sg in (-1, 1) if e < 5]
            g = lambda u: s.rhot(-mp.e**u)*(1/(-mp.e**u - z) - 1/(-mp.e**u - 1))*mp.e**u
            cand = [lz + mp.mpf('1e-9'), lz + mp.mpf('1e-6'), lz + mp.mpf('1e-3'), lz + 1, L - 5, L, L + 5] + [L + e for e in exn]
            pts2 = [lz] + sorted(set(v for v in cand if v > lz)) + [mp.mpf(500)]
            v += mp.quad(g, pts2)
        return v
    def logK(s, z): return -mp.log(4*s.c - z)/2
    def logFk(s, z): return logPhi(s.zeta(z), s.n, s.p, s.d) + s.logK(z)
    def logG(s, z): return -s.d*mp.log(-z) + s.Cr(z)
    def logFnat(s, z): return s.logFk(z) + s.logG(z)
    def logkap(s, z):                  # log kappa_k(z) = log kappa_d(zeta(z)), sides as z
        tk = s.tk(z); sg = 1 if mp.im(z) > 0 else -1
        return -mp.log(-mp.expm1(-sg*2*PI*I*(tk - s.d)))


def boundary_ratio(F, x, eta):       # F(x + i eta) / F(x - i eta) in log form
    return F(x + I*eta) - F(x - I*eta)


def cmod(v):                          # distance of a log-ratio to 0 modulo 2 pi i
    return abs(v - 2*PI*I*mp.nint(mp.im(v)/(2*PI)))


CASES = [(1.5, -0.3, 0.5), (1.5, -0.3, -0.3), (3, -0.7, 1.0), (3, -0.7, -0.02)]
for (p, d, kap) in CASES:
    K = Kap(p, d, kap); lab = f"p={p} d={d} kappa={kap}"
    a = 1 + K.d; X = lambda k: K.n**K.p/((k + K.d)**K.p + K.k)
    say(f"===== {lab}: zs = n^p/kappa = {mp.nstr(K.zs, 8)}, top node X1 = {mp.nstr(X(1), 8)}, c = 1 =====")
    # [O1] jumps on (4c, inf): midpoints between nodes (t_k = k + d + 1/2) and beyond zs
    xs = [K.n**K.p/((k + K.d + HALF)**K.p + K.k) for k in (1, 2, 3)]
    xs = [x for x in xs if x > 4*K.c] + ([2*K.zs, 10*K.zs] if K.k > 0 else [3*X(1), 1e3*X(1)])
    for x in xs:
        eta = x*mp.mpf(10)**-14
        jn = boundary_ratio(K.logFnat, x, eta); jt = 2*PI*I*K.t(x)
        C_.check(f"[O1] {lab}: F_nat jump = e^(2 pi i t) at x = {mp.nstr(x, 6)}", float(cmod(jn - jt)) < 1e-8)
        jF = boundary_ratio(K.logFk, x, eta)
        if K.k < 0 or x < K.zs:
            jk = 2*PI*I*(K.tk(x + 0*I) - K.d)
            C_.check(f"[O1] {lab}: F_k jump = e^(2 i theta_k) at x = {mp.nstr(x, 6)}", float(cmod(jF - jk)) < 1e-8)
        else:
            C_.check(f"[O1] {lab}: F_k jump = -1 beyond zs at x = {mp.nstr(x, 6)}", float(cmod(jF - PI*I)) < 1e-8)
        if K.k > 0:                     # control: Hurwitz gauge only (no Delta part): the lattice jump fails
            Kh = Kap(p, d, kap, gauge=False)
            jh = boundary_ratio(Kh.logFnat, x, eta)
            ok = float(cmod(jh - jt)) > 1e-3
            C_.check(f"[ctrl] {lab}: Hurwitz gauge (-z)^(-d) alone gives the wrong jump at x = {mp.nstr(x, 6)} (must fail)", ok)
        say(f"  [O1] x = {mp.nstr(x, 8)}: |F_nat jump - e^(2 pi i t)| = {mp.nstr(cmod(jn - jt), 3)}")
    if K.k < 0:                         # no jump of F_nat on (-inf, 0), across -|zs| included
        for y in (-3*abs(K.zs), -abs(K.zs)*mp.mpf('1.5'), -abs(K.zs)/2, -mp.mpf(1)):
            v = cmod(boundary_ratio(K.logFnat, y, abs(y)*mp.mpf(10)**-14))
            C_.check(f"[O1] {lab}: F_nat continuous across (-inf, 0) at y = {mp.nstr(y, 6)}", float(v) < 1e-8)
            say(f"  [O1] y = {mp.nstr(y, 8)}: |jump of F_nat| = {mp.nstr(v, 3)}")
    # [zs] regularity at the moved Hurwitz infinity
    zc = K.zs
    def near(r, psi=mp.mpf(1)/3): return zc + abs(zc)*r*mp.expjpi(psi)
    rr = (mp.mpf('1e-6'), mp.mpf('1e-12'), mp.mpf('1e-18'))
    lF = [K.logFnat(near(r)) for r in rr]
    lFk = [mp.re(K.logFk(near(r))) for r in rr[1:]]
    lG = [mp.re(K.logG(near(r))) for r in rr[1:]]
    eFk = (lFk[1] - lFk[0])/mp.log(rr[2]/rr[1]); eG = (lG[1] - lG[0])/mp.log(rr[2]/rr[1])
    say(f"  [zs] log F_nat at r = 1e-6, 1e-12, 1e-18: {[mp.nstr(v, 10) for v in lF]};  exponents: F_k {mp.nstr(eFk, 8)} "
        f"(pred {mp.nstr(-(K.d + HALF), 6)}), G {mp.nstr(eG, 8)} (pred {mp.nstr(K.d + HALF, 6)})")
    C_.check(f"[zs] {lab}: F_nat converges at zs (Hoelder)", float(abs(lF[2] - lF[1])) < 1e-3 and abs(lF[2] - lF[1]) < abs(lF[1] - lF[0]))
    C_.check(f"[zs] {lab}: |F_k| ~ r^-(d+1/2)", float(abs(eFk + K.d + HALF)) < 1e-3)
    C_.check(f"[zs] {lab}: |G_k| ~ r^(d+1/2)", float(abs(eG - K.d - HALF)) < 1e-3)
    if K.k > 0:                         # controls: wrong integer branch on (zs, inf)
        for br in (-1, 1):
            Kb = Kap(p, d, kap, branch=br)
            l1, l2 = mp.re(Kb.logFnat(near(rr[1]))), mp.re(Kb.logFnat(near(rr[2])))
            e = (l2 - l1)/mp.log(rr[2]/rr[1])
            say(f"  [ctrl] branch {br:+d} on (zs, inf): exponent of |F_nat| at zs = {mp.nstr(e, 6)} (must be nonzero)")
            C_.check(f"[ctrl] {lab}: branch {br:+d} makes F_nat singular at zs (must fail)", float(abs(e)) > 0.5)
    # [inf] limit at infinity, uniform in direction; exponents of F_k and G_k
    rays = [mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4, mp.mpf(19)/20]
    vals = {R: [K.logFnat(R*mp.expjpi(ps)) for ps in rays] for R in (mp.mpf(10)**20, mp.mpf(10)**30)}
    spread = max(abs(v - vals[mp.mpf(10)**30][1]) for R in vals for v in vals[R])
    say(f"  [inf] log F_nat on rays pi/4, pi/2, 3pi/4, 0.95pi at R = 1e30: {[mp.nstr(v, 12) for v in vals[mp.mpf(10)**30]]}; spread (incl. R = 1e20) {mp.nstr(spread, 3)}")
    C_.check(f"[inf] {lab}: F_nat -> C_kappa uniformly (4 rays, R = 1e20, 1e30)", float(spread) < 1e-5)
    y1, y2 = mp.mpf(10)**20, mp.mpf(10)**30
    eF = (mp.re(K.logFk(I*y2)) - mp.re(K.logFk(I*y1)))/mp.log(y2/y1)
    eGi = (mp.re(K.logG(I*y2)) - mp.re(K.logG(I*y1)))/mp.log(y2/y1)
    say(f"  [inf] exponent of |F_k(iy)| = {mp.nstr(eF, 10)} (-1/2; the literal claim -Z(0)-1/2 = d = {mp.nstr(K.d, 4)}), of |G_k(iy)| = {mp.nstr(eGi, 10)}")
    C_.check(f"[inf] {lab}: |F_k(iy)| ~ y^(-1/2)", float(abs(eF + HALF)) < 1e-6)
    C_.check(f"[inf] {lab}: |G_k(iy)| ~ y^(+1/2)", float(abs(eGi - HALF)) < 1e-6)
    C_.check(f"[ctrl] {lab}: literal 'F_k ~ C(-z)^(-Z(0)-1/2) at infinity' (exponent d) fails", float(abs(eF - K.d)) > 0.1)
    if K.k > 0:
        Kb = Kap(p, d, kap, branch=1)
        eb = (mp.re(Kb.logFnat(I*y2)) - mp.re(Kb.logFnat(I*y1)))/mp.log(y2/y1)
        C_.check(f"[ctrl] {lab}: branch +1 gives |F_nat| ~ y^(-1) at infinity (must fail normalisation)", float(abs(eb)) > 0.5)
    # [0] hard edge
    E0 = mp.exp(K.Cr(mp.mpf('1e-40')*I))
    hs = []
    for r in (mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-12')):
        z = r*I; hs.append(abs(K.logG(z) + K.d*mp.log(-z) - mp.log(E0)))
    say(f"  [0] |log(G_k (-z)^d / E_k(0))| at |z| = 1e-4, 1e-8, 1e-12 (arg pi/2): {[mp.nstr(h, 3) for h in hs]}")
    eh = mp.log(hs[1]/hs[2])/mp.log(mp.mpf(10)**4); q1 = 1 - 1/K.p
    say(f"  [0] decay exponent of |log G_k(-z)^d - log E_k(0)|: {mp.nstr(eh, 6)} (pred q1 = 1 - 1/p = {mp.nstr(q1, 6)})")
    C_.check(f"[0] {lab}: G_k (-z)^d -> E_k(0) like |z|^(1-1/p) (gauge exponent at the hard edge = -d)", hs[2] < hs[1] < hs[0] and float(abs(eh - q1)) < 0.02)
    rk = []
    for r in (mp.mpf('1e-4'), mp.mpf('1e-8')):
        z = r*mp.expjpi(mp.mpf(1)/2)
        rk.append(abs(K.logFk(z) - (logPhi(z, K.n, K.p, K.d) + K.logK(z))))
    say(f"  [0] |log F_k(z) - log F_d(z)| at 1e-4, 1e-8: {[mp.nstr(v, 3) for v in rk]}")
    C_.check(f"[0] {lab}: F_k/F_d -> 1 at the hard edge", float(rk[1]) < 1e-6)
    # [W5] decomposition of C[rho1] near 0
    qs = [m - 1/K.p for m in range(1, 5)]
    am = [-mp.binomial(1/K.p, m)*(-K.k)**m for m in range(1, 5)]
    C0 = K.Cr(mp.mpf('1e-60')*I)
    FPpred = [mp.zeta(0, a)*K.k**j*K.n**(-j*K.p)/j for j in (1, 2)]
    def rem(z):
        br = sum(am[m]*K.n**(-K.p*qs[m])*(-PI/mp.sin(PI*qs[m]))*mp.power(-z, qs[m]) for m in range(4))
        return K.Cr(z) - C0 - br
    r1, r2 = mp.mpf('0.02'), mp.mpf('0.04'); z1, z2 = r1*I, r2*I
    R1, R2 = rem(z1), rem(z2)
    # R(z) = FP1 z + FP2 z^2 + O(z^3, z^{q_5}): solve the 2x2 system
    FP2 = (R2/z2 - R1/z1)/(z2 - z1); FP1 = R1/z1 - FP2*z1
    say(f"  [W5] FP_1: fit {mp.nstr(FP1, 10)}  pred zeta(0,a) kappa n^-p = {mp.nstr(FPpred[0], 10)};  FP_2: fit {mp.nstr(FP2, 8)}  pred {mp.nstr(FPpred[1], 8)}")
    C_.check(f"[W5] {lab}: gauge integer moment FP_1 = zeta(0,a) kappa n^-p", float(abs(FP1 - FPpred[0])) < 1e-3*float(abs(FPpred[0])))
    C_.check(f"[W5] {lab}: gauge integer moment FP_2 = zeta(0,a) kappa^2 n^-2p / 2", float(abs(FP2 - FPpred[1])) < 3e-2*float(abs(FPpred[1])))
    # control: drop the leading branched term -> the remainder is not O(z)
    Rb = R1 + am[0]*K.n**(-K.p*qs[0])*(-PI/mp.sin(PI*qs[0]))*mp.power(-z1, qs[0])
    C_.check(f"[ctrl] {lab}: without the (-z)^q1 term the remainder is not ~ FP_1 z (must fail)", float(abs(Rb/z1 - FPpred[0])) > 10*float(abs(FPpred[0])))
    # [W4] band and lip algebra at x in (0, 4c)
    al = mp.mpf('-0.3')
    for x in (mp.mpf('0.37'), mp.mpf('2.9')):
        eta = x*mp.mpf(10)**-14
        def logWk(z): return al*mp.log(z) + (1/K.p - 1)*mp.log(1 - z/K.zs)        # w_n = 1
        def logFt(z): return logDB(K.zeta(z), K.n, K.p, K.d) + K.logK(z) + K.logG(z)
        zp, zm = x + I*eta, x - I*eta
        W0 = logWk(zp) - logFt(zp) - logFt(zm)                     # log [W_k/(F~+ F~-)]
        # PV C[rho1](x) = (C+ + C-)/2
        PV = (K.Cr(zp) + K.Cr(zm))/2
        W0pred = (al + 2*K.d)*mp.log(x) + mp.log(4*K.c - x) + (1/K.p - 1)*mp.log(1 - x/K.zs) - 2*mp.re(logDB(K.zeta(x) + I*eta, K.n, K.p, K.d)) - 2*PV
        C_.check(f"[W4] {lab}: band weight W_k/(F~+F~-) at x = {x}", float(abs(W0 - W0pred)) < 1e-8)
        C_.check(f"[W4] {lab}: band weight real at x = {x}", float(abs(mp.im(W0))) < 1e-8)
        lip = logWk(zp) - 2*logFt(zp) + 2*PI*I*K.d - W0
        C_.check(f"[W4] {lab}: lip phase e^(-2 pi i rho1(x)) at x = {x}", float(cmod(lip + 2*PI*I*K.rho1(x))) < 1e-8)
        say(f"  [W4] x = {x}: log W0 = {mp.nstr(W0, 12)}; lip phase/(-2 pi i rho1) - 1 = {mp.nstr((lip/(-2*PI*I*K.rho1(x))) - 1, 3)}")
    # Sigma_v-type cancellation at a point of C_+ near the band: e^{-2 i theta_k} W_k/F~^2 = e^{-2 i theta} W0^k(z)
    z = mp.mpf('1.3') + mp.mpf('0.2')*I
    lhs = -2*PI*I*(K.tk(z) - K.d) + (al*mp.log(z) + (1/K.p - 1)*mp.log(1 - z/K.zs)) - 2*(logDB(K.zeta(z), K.n, K.p, K.d) + K.logK(z) + K.logG(z))
    rho1z = K.t(z) - K.tk(z)                                       # analytic continuation of rho1 near the band
    Psi0 = K.Cr(z) - PI*I*rho1z
    W0z = (al + 2*K.d)*mp.log(z) + mp.log(4*K.c - z) + (1/K.p - 1)*mp.log(1 - z/K.zs) - 2*logDB(K.zeta(z), K.n, K.p, K.d) - 2*Psi0
    rhs = -2*PI*I*K.t(z) + W0z
    C_.check(f"[W4] {lab}: Sigma_v/lip(1,2) phases cancel (W0 continued with Psi0)", float(cmod(lhs - rhs)) < 1e-8)
    say(f"  [W4] Sigma_v cancellation at z = 1.3 + 0.2i: |lhs - rhs| mod 2 pi i = {mp.nstr(cmod(lhs - rhs), 3)}")
C_.finish()
