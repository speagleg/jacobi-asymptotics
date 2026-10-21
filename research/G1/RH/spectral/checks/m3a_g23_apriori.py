"""JZC M3a, gap 2 of Theorem H for 0 < p < 1 (JZC_M3a_H_G23plt1.md §2): the a-priori bound for the Hurwitz interpolant in the
seam geometry (NUMERICAL, mpmath dps 40/30).  Hurwitz measure sigma^d = sum_{k>=1} tau_k^{-s} delta_{tau_k^{-p}}, tau_k = k + d,
a = 1 + d, alpha = (s-1-p)/p, 1 < s < 1 + 2p.  Summation engine (S_A: direct + exact Hurwitz tails; S_B: Euler-Maclaurin with analytic
derivatives; own EM tails hz) copied from m3a_g12_apriori.py (where it is described); seam engine from m3a_g3_seam.py, with the Cauchy
integral chi computed by exact subtraction of the density value on [r*/2, 2r*] (so that points next to a seam are reliable).
Claims checked (asserted):
  [X] the two summation methods agree for p < 1 (also at a small angle inside the lens).
  [A] L2.1 for p < 1 (the sum bound is p-free): |U_j2(z)| <= I1 <= I2 on 0 < |z| <= 1, arg z in {phi_1, pi/2, pi}, phi_1 = theta_lip/2 =
      pi p/8; exponent of |U_j2(iy)| as y -> 0 is min(alpha, 0) for every d (control: it is NOT alpha + 2d).
  [L] L2.2 (lens sectors): (a) R_j2 := U_j2 - U_j1 W/(e^{2 i theta_d} - 1) is continuous across the Hurwitz nodes X_k (the poles of the
      Cauchy sum are removed exactly: residue w(X_k)U_j1(X_k), theta_d' = theta'); CONTROL that must fail: with the lattice theta
      instead of theta_d the jump across X_k is ~ 2 Res/(eps X_k); (b) inside the lens (arg z = phi_1/2), |R_j2| has exponent min(alpha, 0)
      as z -> 0; (c) on the arcs |t| in d + N + 1/2, |arg t| < theta_lip/p, |e^{2 pi i(t-d)} - 1| >= min(1 - e^{-pi/2}, 2e^{-pi/4} sin(7pi/16)).
  [O] (O5) near 0 for the seam scalar F_d (G3 Lemma 3(iii)), the input of Prop 2.4(i): F_d/F_0 -> 1 off the lens in S_in, in S_out and at
      angular distance 1e-8 from both seams (both sides); F~_d/F_0 -> 1 in the lens (F_0 = (4c)^{-1/2} e^{chi_d(0)}).
  [W] Lemma 2.6 (seam scalar at infinity, uniformly up to the seams; the input of Lemma normalisation for F_nat): chi_d -> 0 and
      F_d (-z)^{-d}/(2 pi n)^{-1/2-d} -> 1 at angular distance 1e-8 from the seams, |z| = 1e8, 1e12; Plemelj: chi_out - chi_in = chi_+^d."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 40
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi


# ---------------- summation engine (m3a_g12_apriori.py) ----------------
def monic_ops(n, p, s, a):
    m = [mp.zeta(s + j*p, a) for j in range(2*n + 1)]
    out = {}
    for deg in (n, n - 1):
        A = mp.matrix(deg, deg); b = mp.matrix(deg, 1)
        for i in range(deg):
            for j in range(deg): A[i, j] = m[i + j]
            b[i] = -m[deg + i]
        cs = mp.lu_solve(A, b) if deg > 0 else []
        out[deg] = [cs[i] for i in range(deg)] + [mp.mpf(1)]
    return out[n], out[n - 1]


def hz(sig, b, J=30):
    tot = mp.mpf(0)
    while b < max(60, sig): tot += b**(-sig); b += 1
    tot += b**(1 - sig)/(sig - 1) + b**(-sig)/2
    return tot + sum(mp.bernoulli(2*j)/mp.factorial(2*j)*mp.rf(sig, 2*j - 1)*b**(-sig - 2*j + 1) for j in range(1, J + 1))


def poly(cs, x): return sum(c*x**i for i, c in enumerate(cs))


def S_A(zeta, cs, p, s, a, M0, R=90):
    tot = sum((a + m)**(-s)*poly(cs, (a + m)**(-p))/(zeta - (a + m)**(-p)) for m in range(M0))
    for i, ci in enumerate(cs):
        for r in range(R):
            tot += ci*zeta**(-1 - r)*hz(s + i*p + r*p, a + M0)
    return tot


def S_B(zeta, cs, p, s, a, M1=60, J=22, R=90):
    tot = sum((a + m)**(-s)*poly(cs, (a + m)**(-p))/(zeta - (a + m)**(-p)) for m in range(M1))
    t0 = a + M1
    g = lambda tau: tau**(-s)*poly(cs, tau**(-p))/(zeta - tau**(-p))
    def gder(k):
        return -sum(ci*zeta**r*mp.ff(p - s - i*p + r*p, k)*t0**(p - s - i*p + r*p - k) for i, ci in enumerate(cs) for r in range(R))
    vs = -mp.log(abs(zeta))/p; T1 = mp.exp(vs + mp.log(8)/p)
    v0, v1 = mp.log(t0), mp.log(T1)
    pts = sorted(set([v0, v1] + [x for x in (vs - 2, vs - 1, vs - 0.5, vs - 0.1, vs, vs + 0.1, vs + 0.5) if v0 < x < v1]
                     + [v0 + k*(vs - 2 - v0)/12 for k in range(1, 12)] if vs - 2 > v0 else [v0, v1]))
    integ = mp.quad(lambda v: g(mp.e**v)*mp.e**v, pts)
    integ += sum(ci*zeta**(-1 - r)*T1**(1 - (s + i*p + r*p))/((s + i*p + r*p) - 1) for i, ci in enumerate(cs) for r in range(R))
    em = integ + g(t0)/2 - sum(mp.bernoulli(2*j)/mp.factorial(2*j)*gder(2*j - 1) for j in range(1, J + 1))
    return tot + em


def S(zeta, cs, p, s, a):
    t0 = a + 60
    if abs(zeta)*t0**p <= mp.mpf(1)/4: return S_B(zeta, cs, p, s, a)
    M0 = int(mp.ceil((4/abs(zeta))**(1/p) - a)) + 1
    return S_A(zeta, cs, p, s, a, max(M0, 0))


def hsum(sig, a, K):
    if K <= 0: return mp.mpf(0)
    if sig == 1: return mp.digamma(a + K) - mp.digamma(a)
    return mp.zeta(sig, a) - hz(sig, a + K)


n = 4

# [A] L2.1 and [L](b) for p < 1 (one worker per (p, s, d); 2 processes)
radii = [mp.mpf(1), mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-16'), mp.mpf('1e-24')]
PSs = ((mp.mpf('0.5'), mp.mpf('1.25')), (mp.mpf('0.5'), mp.mpf('1.8')), (mp.mpf('0.75'), mp.mpf('1.375')),
       (mp.mpf('0.3'), mp.mpf('1.15')), (mp.mpf('0.3'), mp.mpf('1.45')))


def taskA(args):
    p, s, d = [mp.mpf(x) for x in args]; mp.mp.dps = 40
    al = (s - 1 - p)/p; gam = p - s; phi1 = PI*p/8; a = 1 + d; P1, P0 = monic_ops(n, p, s, a)
    worst1, worst2, expo, expo_lens = 0, 0, [], []
    for cs in (P1, P0):
        M = max(abs(poly(cs, a**(-p)*k/2000)) for k in range(2001))
        mods, lens = {}, {}
        for r in radii:
            T = n*r**(-1/p); KT = int(mp.floor(T - a)) + 1
            I1 = (M/mp.sin(phi1))*(hsum(s - p, a, KT) + T**p*hz(s, a + KT))
            integ = mp.log(T/a) if gam == -1 else (T**(1 + gam) - a**(1 + gam))/(1 + gam)
            I2 = (M/mp.sin(phi1))*(max(a**gam, T**gam) + integ + T**(p - s) + T**(1 + p - s)/(s - 1))
            for ang in (phi1/PI, mp.mpf(1)/2, mp.mpf(1)):
                z = r*mp.expjpi(ang); U2 = S(z/n**p, cs, p, s, a)
                worst1 = max(worst1, abs(U2)/I1); worst2 = max(worst2, I1/I2)
                if ang == mp.mpf(1)/2: mods[r] = abs(U2)
            if r <= mp.mpf('1e-16') and cs is P1:     # inside the lens: R_j2 = U_j2 - (super-small), arg z = phi_1/2
                z = r*mp.expj(phi1/2); lens[r] = abs(S(z/n**p, cs, p, s, a))
        expo.append(mp.log(mods[radii[-2]]/mods[radii[-1]])/mp.log(radii[-2]/radii[-1]))
        if lens: expo_lens.append(mp.log(lens[radii[-2]]/lens[radii[-1]])/mp.log(radii[-2]/radii[-1]))
    return [str(x) for x in (worst1, worst2, expo[0], expo[1], expo_lens[0])]


if __name__ == '__main__':
    import multiprocessing as mpr
    jobs = [(str(p), str(s), str(d)) for (p, s) in PSs for d in (mp.mpf(0), mp.mpf('-0.5'), mp.mpf('-0.9'))]
    with mpr.Pool(2) as pool: resA = pool.map(taskA, jobs)
    for (ps, ss, ds), res in zip(jobs, resA):
        p, s, d = mp.mpf(ps), mp.mpf(ss), mp.mpf(ds); al = (s - 1 - p)/p; lab = f"p={p} s={s} (alpha={mp.nstr(al,3)}) d={d}"
        worst1, worst2, e0, e1, el = [mp.mpf(x) for x in res]; target = al if al < 0 else 0
        print(f"[A] {lab}: max |U_j2|/I1 = {mp.nstr(worst1,4)}, max I1/I2 = {mp.nstr(worst2,4)}; exponent of |U_j2(iy)| (1e-16 -> 1e-24): "
              f"{mp.nstr(e0,8)}, {mp.nstr(e1,8)}; in the lens (arg phi_1/2): {mp.nstr(el,8)} (alpha+2d = {mp.nstr(al+2*d,3)})", flush=True)
        C_.check(f"[A] |U_j2| <= I1 {lab}", float(max(worst1 - 1, 0)), 0.0, 0.0)
        C_.check(f"[A] I1 <= I2 {lab}", float(max(worst2 - 1, 0)), 0.0, 0.0)
        for e in (e0, e1, el): C_.check(f"[A/L] exponent = min(alpha,0), d-free {lab}", float(e - target), 0.0, 1e-4)
        if d != 0:
            C_.check(f"[A] CONTROL must fail: exponent = min(alpha+2d, 0) {lab}", float(abs(e0 - min(al + 2*d, 0))) > 0.1, True, 0)


def main():
    global C_
    # [X] cross-validation for p < 1
    for (p, s, d) in ((mp.mpf('0.5'), mp.mpf('1.25'), mp.mpf('-0.5')), (mp.mpf('0.75'), mp.mpf('2.125'), mp.mpf('-0.9'))):
        a = 1 + d; P1, P0 = monic_ops(n, p, s, a)
        for ang in (PI*p/16, PI/2):
            zeta = mp.mpf('0.25')/(a + 60)**p*mp.expj(ang)
            vA = S_A(zeta, P1, p, s, a, int(mp.ceil((4/abs(zeta))**(1/p))) + 1); vB = S_B(zeta, P1, p, s, a)
            print(f"[X] p={p} s={s} d={d} arg={mp.nstr(ang,3)}: |S_A - S_B|/|S_A| = {mp.nstr(abs(vA - vB)/abs(vA), 3)}", flush=True)
            C_.check(f"[X] methods A/B agree p={p} arg={mp.nstr(ang,3)}", float(abs(vA - vB)/abs(vA)), 0.0, 1e-30)

    # [L](a): pole cancellation across Hurwitz nodes; control with the lattice phase
    for (p, s, d, ks) in ((mp.mpf('0.5'), mp.mpf('1.25'), mp.mpf('-0.5'), (5, 40)), (mp.mpf('0.75'), mp.mpf('2.125'), mp.mpf('-0.9'), (5, 40)),
                          (mp.mpf('0.3'), mp.mpf('1.15'), mp.mpf('-0.25'), (3, 12))):
        a = 1 + d; P1, P0 = monic_ops(n, p, s, a); lab = f"p={p} s={s} d={d}"
        def R(x, cs, dd):
            zeta = x/n**p; t = n*x**(-1/p)
            U2 = S_A(zeta, cs, p, s, a, int(mp.ceil((4/zeta)**(1/p) - a)) + 1)
            W = 2*I*(-(PI/p)*t/x)*n**p*t**(-s)
            return U2 - poly(cs, zeta)*W/(mp.expj(2*PI*(t - dd)) - 1), U2
        worst, ctrl, upole = 0, mp.inf, 0
        for cs in (P1, P0):
            for k in ks:
                Xk = (n/(k + d))**p; eps = mp.mpf(10)**-12
                Rp, Up = R(Xk*(1 + eps), cs, d); Rm, Um = R(Xk*(1 - eps), cs, d)
                Rmid, _ = R((n/(k + d + mp.mpf(1)/2))**p, cs, d)
                worst = max(worst, abs(Rp - Rm)/max(abs(Rmid), abs(Rp)))
                upole = max(upole, abs(Up - Um)/max(abs(Rmid), abs(Rp)))
                Cp, _ = R(Xk*(1 + eps), cs, 0); Cm, _ = R(Xk*(1 - eps), cs, 0)
                ctrl = min(ctrl, abs(Cp - Cm)/max(abs(Rmid), abs(Rp)))
        print(f"[L](a) {lab}: max |R(X_k+) - R(X_k-)|/|R| = {mp.nstr(worst,3)} (eps = 1e-12; the Cauchy sum itself jumps by {mp.nstr(upole,3)}); "
              f"control (lattice theta): min jump/|R| = {mp.nstr(ctrl,3)}", flush=True)
        C_.check(f"[L](a) R_j2 continuous across X_k with theta_d {lab}", float(worst), 0.0, 1e-8)
        C_.check(f"[L](a) CONTROL must fail: lattice theta leaves the pole {lab}", float(ctrl) > 1e6, True, 0)

    # [L](c): arcs
    for p in (mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.75')):
        for d in (mp.mpf('-0.1'), mp.mpf('-0.5'), mp.mpf('-0.9')):
            lo = min(abs(mp.expj(2*PI*(rho*mp.expj(psi) - d)) - 1)
                     for rho in [d + N + mp.mpf(1)/2 for N in range(1, 40)] for psi in [PI/4*j/50 for j in range(-49, 50)])
            bound = min(1 - mp.exp(-PI/2), 2*mp.exp(-PI/4)*mp.sin(7*PI/16))
            C_.check(f"[L](c) arc lower bound p={p} d={d}", float(max(bound - lo, 0)), 0.0, 0.0)
    print(f"[L](c) arcs: lower bound {mp.nstr(min(1 - mp.exp(-PI/2), 2*mp.exp(-PI/4)*mp.sin(7*PI/16)), 6)} holds on all samples", flush=True)


    # ---------------- seam engine (m3a_g3_seam.py, chi with subtraction) ----------------
    mp.mp.dps = 30
    c = mp.mpf(1)


    def jd(t, d):
        with mp.extradps(int(max(0, mp.log10(abs(t)))) + 10):
            return +(mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*PI)/2)


    def sub_int(f, r0, w, extra):
        f0 = f(r0)
        g = lambda u: (f(mp.e**u) - (f0 if r0/2 <= mp.e**u <= 2*r0 else 0))/(mp.e**u - w)*mp.e**u
        L = mp.log(r0); pts = sorted(set([mp.mpf(-40), L - mp.log(2), L, L + mp.log(2), mp.mpf(120)] + [x for x in extra if -40 < x < 120]))
        return mp.quad(g, pts) + f0*(mp.log(2*r0 - w) - mp.log(r0/2 - w))


    class Seam:
        def __init__(s, p, d, n):
            s.p, s.d, s.n, s.th = p, d, n, PI*p/2
            s.w = (1 - 1/p)*(mp.mpf(1)/2 + d); s.lam = mp.gamma(1 + d)*(2*PI)**d; s.cache = {}
        def logBin(s, z): return (s.w + 1)*mp.log(1 + z) - mp.log(1 + s.lam*z)
        def logBout(s, z): return (mp.mpf(1)/2 + s.d)*mp.log(1 - z/(2*PI*s.n))
        def t(s, z): return s.n*mp.exp(-mp.log(z)/s.p)
        def chip(s, r):
            if r in s.cache: return s.cache[r]
            z = r*mp.expj(s.th); t = s.t(z); ex = -2*PI*I*(t - s.d)
            lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -300 else mp.mpc(0)
            v = -jd(t, s.d) - lg + s.logBin(z) - s.logBout(z); s.cache[r] = v; return v
        def chi(s, z):
            e = mp.expj(s.th); extra = [s.p*mp.log(s.n), mp.mpf(0), mp.log(2*PI*s.n)]
            return (sub_int(s.chip, abs(z), z/e, extra) - sub_int(lambda r: mp.conj(s.chip(r)), abs(z), z*e, extra))/(2*PI*I)
        def chi0(s):
            return mp.quad(lambda u: s.chip(mp.e**u) - mp.conj(s.chip(mp.e**u)), [-40, s.p*mp.log(s.n), 0, mp.log(2*PI*s.n), 120])/(2*PI*I)
        def logF(s, z, tilde=False):
            ch = s.chi(z); K = -mp.log(4*c - z)/2
            if abs(mp.arg(z)) < s.th:
                t = s.t(z); sg = 1 if mp.im(z) > 0 else -1; ex = -sg*2*PI*I*(t - s.d)
                lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -300 else mp.mpc(0)
                return -jd(t, s.d) + s.logBin(z) + K + ch - (0 if tilde else lg)
            return s.logBout(z) + K + ch


    for p in (mp.mpf('0.3'), mp.mpf('0.6')):
        for d in (mp.mpf('-0.25'), mp.mpf('-0.8')):
            nn = 4; Sm = Seam(p, d, nn); th = Sm.th; lab = f"p={p} d={d}"; e8 = mp.mpf(10)**-8
            F0 = mp.exp(Sm.chi0())/mp.sqrt(4*c)
            off = [0.8*th, th*(1 - e8), th*(1 + e8), -th*(1 + e8), -th*(1 - e8), PI/2, 0.95*PI, -0.7*PI]
            lensang = [0.1*th, -0.05*th, mp.mpf(10)**-6*th]
            dev = {}
            for r in (mp.mpf('1e-4'), mp.mpf('1e-8')):
                dev[r] = max([abs(mp.exp(Sm.logF(r*mp.expj(ang)))/F0 - 1) for ang in off]
                             + [abs(mp.exp(Sm.logF(r*mp.expj(ang), tilde=True))/F0 - 1) for ang in lensang])
            print(f"[O] {lab}: max |F_d/F_0 - 1| (off the lens, 4 angles next to the seams; F~ in the lens): |z|=1e-4: {mp.nstr(dev[mp.mpf('1e-4')],3)}, "
                  f"|z|=1e-8: {mp.nstr(dev[mp.mpf('1e-8')],3)}", flush=True)
            C_.check(f"[O] (O5) near 0, F_d/F_0 -> 1 incl. next to the seams {lab}", float(dev[mp.mpf('1e-8')]), 0.0, 1e-4)
            C_.check(f"[O] decreasing {lab}", float(max(dev[mp.mpf('1e-8')] - dev[mp.mpf('1e-4')], 0)), 0.0, 0.0)
            # [W] infinity next to the seams
            Cd = (2*PI*nn)**(-mp.mpf(1)/2 - d); wch, wF = {}, {}
            for R_ in (mp.mpf('1e8'), mp.mpf('1e12')):
                angs = [th*(1 - e8), th*(1 + e8), -th*(1 - e8), -th*(1 + e8)]
                wch[R_] = max(abs(Sm.chi(R_*mp.expj(ang))) for ang in angs)
                wF[R_] = max(abs(mp.exp(Sm.logF(R_*mp.expj(ang)) - d*mp.log(-R_*mp.expj(ang)))/Cd - 1) for ang in angs)
            # Plemelj at |z| = 1e3 across Sigma_+
            r3 = mp.mpf(1000); pj = abs(Sm.chi(r3*mp.expj(th + mp.mpf(10)**-20)) - Sm.chi(r3*mp.expj(th - mp.mpf(10)**-20)) - Sm.chip(r3))
            mid = max(abs(Sm.chi(r_*mp.expj(th*(1 + sg*e8)))) for r_ in (mp.mpf(1), mp.mpf(10), mp.mpf(1000), mp.mpf(10)**5) for sg in (1, -1))
            print(f"[W] {lab}: next to the seams max|chi_d| at |z| = 1..1e5: {mp.nstr(mid,4)}; at 1e8: {mp.nstr(wch[mp.mpf('1e8')],3)}, "
                  f"1e12: {mp.nstr(wch[mp.mpf('1e12')],3)}; max|F(-z)^-d/C_d - 1|: 1e8 {mp.nstr(wF[mp.mpf('1e8')],3)}, 1e12 {mp.nstr(wF[mp.mpf('1e12')],3)}; "
                  f"Plemelj |chi_out - chi_in - chi_+| at 1e3 = {mp.nstr(pj,3)}", flush=True)
            C_.check(f"[W] chi_d -> 0 next to the seams {lab}", float(wch[mp.mpf('1e12')]), 0.0, 1e-5)
            C_.check(f"[W] chi_d decreasing next to the seams {lab}", float(max(wch[mp.mpf('1e12')] - wch[mp.mpf('1e8')], 0)), 0.0, 0.0)
            C_.check(f"[W] F_nat -> C_d next to the seams {lab}", float(wF[mp.mpf('1e12')]), 0.0, 1e-5)
            C_.check(f"[W] Plemelj chi_out - chi_in = chi_+ {lab}", float(pj), 0.0, 1e-15)
            C_.check(f"[W] chi_d bounded next to the seams, |z| in [1, 1e5] {lab}", float(max(mid - 2, 0)), 0.0, 0.0)
    C_.finish()


if __name__ == '__main__':
    main()
