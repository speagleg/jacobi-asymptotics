"""JZC_W_kappa §1, §3, §5 (NUMERICAL, mpmath dps 30): the gauge of the kappa-family lam_k = (k + d)^p + kappa in closed form,
the factor X = E_kappa D_{e^{-2 Psi0}}, coherence of the branched band/lip data, and the 1 < p < 2 Hoelder exponent.
Notation (JZC_W_outer.md, JZC_W_kappa.md): t = n z^{-1/p}, zs = n^p/kappa, rho1(y) = t(y) - t_kappa(y) (y < |zs|), and the gauge
C[rho1](z) = int_0^inf rho1(y)[1/(y-z) - 1/(y+1)] dy (+ the (-inf, -|zs|) piece for kappa < 0), computed by quadrature exactly as in
w_outer_scalar.py (class copied, since that script runs its checks on import).
Claims checked:
  [CF]  Lemma K.1: for |z| < |zs|, z not in [0, |zs|):
          C[rho1](z) = C(0) - zeta(0, a) log(1 - z/zs) + (pi/sin(pi/p)) rho1^-(z),   rho1^-(z) := n(-z)^{-1/p}(1 - (1 - z/zs)^{1/p})
        i.e. C[rho1](z) - [-zeta(0,a) log(1 - z/zs) + (pi/sin(pi/p)) rho1^-(z)] is constant (spread over 7 points incl. both sides of
        the band and next to the negative axis). Controls (must fail): pi cot(pi/p) in place of pi/sin(pi/p); the log term dropped.
  [PSI] Cor K.1: on the band, Psi0(x) = PV C[rho1](x) = C(0) + pi cot(pi/p) rho1(x) - zeta(0,a) log(1 - x/zs).
  [COH] Lemma K.10 (coherence): the branched factor exp(-(pi/sin(pi/p)) rho1^-(z)) of W~_kappa has no jump across (-delta_r, 0) and
        its band boundary values multiply to exp(-2 pi cot(pi/p) rho1(x)) (the band tilt); control (must fail): the non-coherent
        choice (band tilt without lip factor, W~^2 = h only) jumps across (-delta_r, 0) by ~ n^{1-p}|y|^{q1}.
  [X]   Lemma K.4: X := E_kappa D_{e^{-2 Psi0}} satisfies X_+ X_- = 1 on the band and log X = R(z) A_X(z) with A_X analytic at 0
        (A_X := log X/R has no jump across the band or (-delta_r, 0)), hence
          |log X(z)| <= C n^{1-p} |z|^{1/2}   (|z| <= 0.1),  C n-free, for every p > 1;
        tested at n = 4, 16, 64, 6 radii, 4 directions. Control (must fail): the rate n^{-p} (sup |log X| n^p bounded).
  [NU]  Section 5 (1 < p < 2): (a) the band factor alone has the Hoelder exponent q1 = 1 - 1/p < 1/2 = nu_p at 0 (gauge part
        -2 pi cot(pi/p) rho1 of log H_n^kappa, local exponent q1 at p = 1.25, 1.5): (O3) with nu_p fails for H_n^kappa; (b) the lip
        entry's gauge factor X^2 has exponent 1/2 for every p > 1 (local exponent of |log X| on the lip, 1e-6 -> 1e-8), control (must
        fail): exponent q1; (c) the route-A lip mismatch from the gauge, localised on the Bessel scale, S(n) := sup_r |X^2 - 1| e^{-n r^{1/2}}
        (r on the lip), decays like n^{-p}; control (must fail): the q1-based rate n^{-(p+2)(p-1)/p}.
        History (Rule A item 1 of JZC_W_kappa.md): the first version of this script asserted the exponent min(q1, 1/2) for log X and
        log X ~ -/+ i pi rho1 on the lips; the run gave exponent 1/2 and a relative deviation 3 from -/+ i pi rho1 (the leading z^{q1}
        terms of the lip phase and of the Szego remainder cancel); this led to Lemma K.4 as now stated. The run was aborted and the
        assertions replaced before any completed output was kept.
D_q by (eq:szego) with x = 4c sin^2(phi/2): log D_q^2(z) = (R(z)/pi) int_0^pi log q(x(phi)) dphi/(z - x(phi)), R(z) = z sqrt(1 - 4c/z).
c = c(p) of Paper 2 (cp below, as in m3a_hc_gauge.py)."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 30
I = mp.mpc(0, 1); PI = mp.pi; HALF = mp.mpf(1)/2
C_ = Checks(); T0 = time.time()


def say(*a): print(*a, flush=True)
def cp(p): Ip = mp.sqrt(PI)/2*mp.gamma(1/p + HALF)/mp.gamma(1/p + 1); return (PI/(2*Ip))**p/4


class Kap:
    def __init__(s, p, d, kap, n=4):
        s.p, s.d, s.k, s.n = mp.mpf(p), mp.mpf(d), mp.mpf(kap), mp.mpf(n)
        s.zs = s.n**s.p/s.k; s.a = 1 + s.d; s.c = cp(s.p); s.q1 = 1 - 1/s.p
    def rho1(s, y):                    # y > 0 real
        if s.k > 0 and y > s.zs: return s.n*y**(-1/s.p) - s.d - HALF
        u = y/s.zs
        return -s.n*y**(-1/s.p)*mp.expm1(mp.log1p(-u)/s.p)
    def rho1z(s, z):                   # analytic continuation (principal z^{-1/p}), |z| < |zs|
        return -s.n*mp.power(z, -1/s.p)*mp.expm1(mp.log(1 - z/s.zs)/s.p)
    def rho1m(s, z):                   # rho1^-(z) = n(-z)^{-1/p}(1 - (1 - z/zs)^{1/p})
        return -s.n*mp.power(-z, -1/s.p)*mp.expm1(mp.log(1 - z/s.zs)/s.p)
    def rhot(s, y): return HALF + s.d - (s.n**s.p/y - s.k)**(1/s.p)
    def Cr(s, z):
        L = mp.log(abs(z)); A = abs(mp.arg(z)); ex = [sg*e for e in (A, 10*A, 100*A) for sg in (-1, 1) if e < 5]
        f = lambda u: s.rho1(mp.e**u)*(1/(mp.e**u - z) - 1/(mp.e**u + 1))*mp.e**u
        lz = mp.log(abs(s.zs))
        pts = sorted(set([mp.mpf(-200), mp.mpf(-40), mp.mpf(0), lz, L - 5, L, L + 5, mp.mpf(500)] + [L + e for e in ex]
                         + ([lz + e for e in (-1e-3, -1e-6, 1e-6, 1e-3)] if s.k > 0 else [])))
        v = mp.quad(f, pts)
        if s.k < 0:
            B = PI - A; exn = [sg*e for e in (B, 10*B, 100*B) for sg in (-1, 1) if e < 5]
            g = lambda u: s.rhot(-mp.e**u)*(1/(-mp.e**u - z) - 1/(-mp.e**u - 1))*mp.e**u
            cand = [lz + mp.mpf('1e-9'), lz + mp.mpf('1e-6'), lz + mp.mpf('1e-3'), lz + 1, L - 5, L, L + 5] + [L + e for e in exn]
            pts2 = [lz] + sorted(set(v for v in cand if v > lz)) + [mp.mpf(500)]
            v += mp.quad(g, pts2)
        return v
    def gpart(s, z, coef=None, logterm=True):   # the claimed z-dependence of C[rho1]
        coef = PI/mp.sin(PI/s.p) if coef is None else coef
        return (-mp.zeta(0, s.a)*mp.log(1 - z/s.zs) if logterm else 0) + coef*s.rho1m(z)
    def logqhat(s, x):                 # -2 Psi0(x) + 2 C(0) on the band (closed form, Cor K.1)
        return -2*PI*mp.cot(PI/s.p)*s.rho1(x) + 2*mp.zeta(0, s.a)*mp.log(1 - x/s.zs)
    def logD2(s, z, logq):             # log D_q(z)^2 by (eq:szego)
        c = s.c; xf = lambda ph: 4*c*mp.sin(ph/2)**2
        Rz = z*mp.sqrt(1 - 4*c/z)
        if 0 < mp.re(z) < 4*c and abs(mp.im(z)) < mp.re(z):
            ph0 = 2*mp.asin(mp.sqrt(mp.re(z)/(4*c))); w = abs(mp.im(z))/(2*c) + mp.mpf(10)**-40
            pts = sorted(set([mp.mpf(0), PI] + [ph0 + k*w for k in (-1e4, -1e2, -10, -1, 0, 1, 10, 1e2, 1e4) if 0 < ph0 + k*w < PI]
                             + [ph0*k for k in (0.01, 0.1, 0.5, 2) if ph0*k < PI]))
        else:
            r0 = mp.sqrt(abs(z)/c)
            pts = sorted(set([mp.mpf(0), PI] + [r0*k for k in (0.01, 0.1, 0.3, 1, 3, 10, 100) if r0*k < PI]))
        return Rz/PI*mp.quad(lambda ph: logq(xf(ph))/(z - xf(ph)) if ph > 0 else mp.mpf(0), pts)
    def logX(s, z):                    # log X = [C(z) - C(0)] + (1/2) log D_{qhat}^2(z)  (constant-free)
        return s.gpart(z) + s.logD2(z, s.logqhat)/2


def spread(vals): return max(abs(v - vals[0]) for v in vals)


# ---------------- [CF], [PSI] ----------------
CASES = [(1.5, -0.3, 0.5), (1.5, -0.3, -0.3), (3, -0.7, 1.0), (3, -0.7, -0.02), (1.25, -0.5, 2.0), (2, -0.5, 0.7)]
for (p, d, kap) in CASES:
    K = Kap(p, d, kap); lab = f"p={p} d={d} kappa={kap}"; zp = abs(K.zs)
    pts = [mp.mpc('0.3', '0.2'), mp.mpc(-1, '0.01'), 2*mp.expjpi(mp.mpf('0.9')), mp.mpc('1.1', '1e-12'), mp.mpc('1.1', '-1e-12'),
           mp.mpc('-0.5', '-1e-12'), (zp*mp.mpf('0.6'))*mp.expjpi(mp.mpf('0.5'))]
    cr = [K.Cr(z) for z in pts]
    v = [c_ - K.gpart(z) for c_, z in zip(cr, pts)]
    v1 = [c_ - K.gpart(z, coef=PI*mp.cot(PI/K.p)) for c_, z in zip(cr, pts)]
    v2 = [c_ - K.gpart(z, logterm=False) for c_, z in zip(cr, pts)]
    sp, sp1, sp2 = spread(v), spread(v1), spread(v2)
    say(f"[CF] {lab}: |zs| = {mp.nstr(zp, 6)}; spread of C[rho1] - closed form over 7 points = {mp.nstr(sp, 3)}; controls: "
        f"cot in place of 1/sin {mp.nstr(sp1, 3)}, no log term {mp.nstr(sp2, 3)};  C(0) = {mp.nstr(mp.re(v[0]), 15)}")
    C_.check(f"[CF] {lab}: closed form of the gauge (Lemma K.1)", float(sp), 0.0, 1e-18)
    C_.check(f"[CF] {lab}: imaginary part of the constant C(0) vanishes", float(abs(mp.im(v[0]))), 0.0, 1e-18)
    C_.check(f"[ctrl] {lab}: pi cot(pi/p) in place of pi/sin(pi/p) fails (must fail)", float(sp1 > 1e3*1e-18), 1.0, 0.0)
    if abs(mp.zeta(0, K.a)) > mp.mpf('1e-20'):     # zeta(0, a) = 1/2 - a vanishes at d = -1/2: the control is degenerate there
        C_.check(f"[ctrl] {lab}: dropping -zeta(0,a) log(1 - z/zs) fails (must fail)", float(sp2 > 1e3*1e-18), 1.0, 0.0)
    # [PSI] band: PV C = (C(x+i0) + C(x-i0))/2 at x = 1.1 vs the closed form of Psi0
    PV = (cr[3] + cr[4])/2; x = mp.mpf('1.1')
    Psi = mp.re(v[0]) + PI*mp.cot(PI/K.p)*K.rho1(x) - mp.zeta(0, K.a)*mp.log(1 - x/K.zs)
    # tolerance: the boundary values are taken at x +/- 1e-12 i, so PV is reproduced only to O(1e-12 |C'| log) (|C'| <= 1e2 here)
    C_.check(f"[PSI] {lab}: Psi0(x) = C(0) + pi cot(pi/p) rho1(x) - zeta(0,a) log(1 - x/zs) on the band", float(abs(PV - Psi)), 0.0, 1e-9)
    say(f"  [PSI] |PV C(1.1) - closed form| = {mp.nstr(abs(PV - Psi), 3)}")
say(f"  (time {time.time() - T0:.0f}s)")

# ---------------- [COH] ----------------
for (p, d, kap) in [(1.5, -0.3, 0.5), (3, -0.7, 1.0), (1.25, -0.5, -0.4)]:
    for n in (4, 64):
        K = Kap(p, d, kap, n=n); lab = f"p={p} kappa={kap} n={n}"
        coh = lambda z: -(PI/mp.sin(PI/K.p))*K.rho1m(z)               # log of the branched factor of W~_kappa (coherent)
        nco = lambda z: -PI*mp.cot(PI/K.p)*K.rho1z(z)                 # non-coherent: W~^2 = band tilt only (sigma = 0)
        jc, jn = 0, mp.inf
        for y in (mp.mpf('-0.2'), mp.mpf('-0.05'), mp.mpf('-1e-3')):
            eps = abs(y)*mp.mpf(10)**-25
            jc = max(jc, abs(coh(y + I*eps) - coh(y - I*eps)))
            jn = min(jn, abs(nco(y + I*eps) - nco(y - I*eps))/(K.n**(1 - K.p)*abs(y)**K.q1))
        bb = 0
        for x in (mp.mpf('0.05'), mp.mpf('0.7')):
            eps = x*mp.mpf(10)**-25
            bb = max(bb, abs(coh(x + I*eps) + coh(x - I*eps) - (-2*PI*mp.cot(PI/K.p)*K.rho1(x))))
        say(f"[COH] {lab}: coherent factor jump on (-delta_r,0) {mp.nstr(jc, 3)}; band product vs tilt {mp.nstr(bb, 3)}; "
            f"non-coherent jump / (n^(1-p)|y|^q1) >= {mp.nstr(jn, 4)}")
        C_.check(f"[COH] {lab}: coherent branched factor continuous across (-delta_r, 0)", float(jc), 0.0, 1e-20)
        C_.check(f"[COH] {lab}: band boundary values multiply to the band tilt exp(-2 pi cot(pi/p) rho1)", float(bb), 0.0, 1e-20)
        C_.check(f"[ctrl] {lab}: non-coherent data are continuous across (-delta_r, 0) (must fail)", float(jn > 0.1), 1.0, 0.0)

# ---------------- [X], [NU] ----------------
RAD = [mp.mpf('0.1'), mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]
DIRS = [mp.mpf(1)/3, -mp.mpf(1)/3, mp.mpf(2)/3, mp.mpf('0.99')]
def Rz(z, c): return z*mp.sqrt(1 - 4*c/z)
for (p, d, kap) in [(1.5, -0.3, 0.5), (1.25, -0.5, -0.4), (3, -0.7, 1.0), (2, -0.5, 0.7)]:
    supr = {}; supp = {}
    for n in (4, 16, 64):
        K = Kap(p, d, kap, n=n); lab = f"p={p} d={d} kappa={kap}"
        rmax, pmax = 0, 0
        for r in RAD:
            for th in DIRS:
                z = r*mp.expjpi(th); lx = K.logX(z)
                rmax = max(rmax, abs(lx)/(K.n**(1 - K.p)*r**HALF)); pmax = max(pmax, abs(lx)*K.n**K.p)
        supr[n] = rmax; supp[n] = pmax
        bp, ja = 0, 0
        for x in (mp.mpf('0.01'), mp.mpf('0.5')):          # X_+ X_- = 1 and A_X = log X/R continuous across the band
            eps = x*mp.mpf(10)**-20; lp, lm = K.logX(x + I*eps), K.logX(x - I*eps)
            bp = max(bp, abs(lp + lm)); ja = max(ja, abs(lp/Rz(x + I*eps, K.c) - lm/Rz(x - I*eps, K.c)))
        for y in (mp.mpf('-0.01'), mp.mpf('-0.1')):       # and across (-delta_r, 0)
            eps = abs(y)*mp.mpf(10)**-20
            ja = max(ja, abs(K.logX(y + I*eps)/Rz(y + I*eps, K.c) - K.logX(y - I*eps)/Rz(y - I*eps, K.c)))
        C_.check(f"[X] {lab} n={n}: X_+ X_- = 1 on the band", float(bp), 0.0, 1e-12)
        C_.check(f"[X] {lab} n={n}: A_X = log X/R has no jump on the band or on (-delta_r, 0)", float(ja), 0.0, 1e-12)
        say(f"[X] {lab} n={n}: max |log X|/(n^(1-p)|z|^(1/2)) = {mp.nstr(rmax, 4)};  max |log X| n^p = {mp.nstr(pmax, 4)}; "
            f"|log(X+X-)| on band {mp.nstr(bp, 3)}; jump of A_X {mp.nstr(ja, 3)}  (t {time.time() - T0:.0f}s)")
    C_.check(f"[X] {lab}: |log X| <= C n^(1-p)|z|^(1/2), C <= 10", float(max(supr.values())), 0.0, 10.0)
    C_.check(f"[X] {lab}: that constant is n-free (n = 64 vs 4: ratio <= 2)", float(max(supr[64]/supr[4] - 2, 0)), 0.0, 0.0)
    C_.check(f"[ctrl] {lab}: rate n^-p (sup |log X| n^p bounded) fails (must fail)", float(supp[64]/supp[4] > 4), 1.0, 0.0)

# [NU] (a) band factor exponent q1, (b) lip-entry exponent 1/2, (c) localised mismatch
for (p, d, kap) in [(1.25, -0.5, -0.4), (1.5, -0.3, 0.5), (3, -0.7, 1.0)]:
    K = Kap(p, d, kap, n=16); lab = f"p={p} kappa={kap}"
    r1, r2 = mp.mpf('1e-6'), mp.mpf('1e-8'); z1, z2 = r1*mp.expjpi(mp.mpf(1)/3), r2*mp.expjpi(mp.mpf(1)/3)
    hb = lambda z: -2*PI*mp.cot(PI/K.p)*K.rho1z(z) + 2*mp.zeta(0, K.a)*mp.log(1 - z/K.zs)   # gauge part of log H_n^kappa - const
    slH = mp.log(abs(hb(z1))/abs(hb(z2)))/mp.log(r1/r2)
    slX = mp.log(abs(K.logX(z1))/abs(K.logX(z2)))/mp.log(r1/r2)
    say(f"[NU] {lab}: local exponents on the lip (1e-6 -> 1e-8): band factor (gauge part) {mp.nstr(slH, 6)} (q1 = {mp.nstr(K.q1, 6)}); "
        f"lip-entry factor log X {mp.nstr(slX, 6)} (1/2)")
    C_.check(f"[NU] {lab}: band factor's gauge part has Hoelder exponent q1 at 0", float(slH), float(K.q1), 0.01)
    C_.check(f"[NU] {lab}: lip-entry gauge factor X has exponent 1/2 at 0", float(slX), 0.5, 0.01)
    if K.q1 < HALF - mp.mpf('0.1'):
        C_.check(f"[ctrl] {lab}: exponent q1 for the lip-entry factor (must fail)", float(abs(slX - K.q1) < 0.03), 0.0, 0.0)
for (p, d, kap) in [(1.25, -0.5, -0.4), (1.5, -0.3, 0.5)]:
    Sn = {}
    for n in (64, 256, 1024):
        K = Kap(p, d, kap, n=n)
        grid = [mp.mpf(10)**(-mp.mpf(k)/4) for k in range(4, 49)]
        Sn[n] = max(abs(mp.expm1(2*K.logX(r*mp.expjpi(mp.mpf(1)/3))))*mp.exp(-n*mp.sqrt(r)) for r in grid)
    e1 = mp.log(Sn[256]/Sn[1024])/mp.log(4); naive = (p + 2)*(p - 1)/p
    say(f"[NU] p={p} kappa={kap}: S(n) at n = 64, 256, 1024: {[mp.nstr(v, 4) for v in Sn.values()]}; decay exponent {mp.nstr(e1, 5)} "
        f"(pred p = {p}; q1-based (p+2)(p-1)/p = {mp.nstr(naive, 4)})")
    C_.check(f"[NU] p={p}: localised gauge lip mismatch decays like n^-p", float(e1), float(p), 0.06)
    C_.check(f"[ctrl] p={p}: q1-based rate n^-(p+2)(p-1)/p (must fail)", float(abs(e1 - naive) < 0.06), 0.0, 0.0)
say(f"total time {time.time() - T0:.0f}s")
C_.finish()
