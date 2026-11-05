"""JZC M3a, gap 3 of Theorem H (JZC_M3a_H_G23plt1.md §2; fixed per Rule R review B, B23-8): E_plt1 Lemma F.1 (i)-(iv) with the complex seam jump densities
of JZC_M3a_H_G3.md (NUMERICAL, mpmath dps 30).  0 < p < 1, -1 < d < 0, theta := pi p/2 (seam angle), q(r) := exp(-2 pi n r^{-1/p}),
  l(r)   := -log(1 - q)                      (E_plt1's real density, d = 0)
  l_pm(r):= -Log(1 - e^{+-2 pi i d} q)       (the jump G_out - G_in on Gamma_pm, G3 §2 / Lemma F.1(i)_d)
  J(z)   := (1/2 pi i) int_0^oo [l_+(r) e^{i th} K(r e^{i th}, z) - l_-(r) e^{-i th} K(r e^{-i th}, z)] dr,  K(zeta,z) = (z-1)/((zeta-z)(zeta-1))
  m_k(d) := (1/2 pi i) int_0^oo [l_+ e^{i th}(r e^{i th})^{-k-1} - l_- e^{-i th}(r e^{-i th})^{-k-1}] dr   (literal (iii)_d, l_- NOT
            computed as conj(l_+)).
Claims checked (asserted):
  [M] majorants (the only property of l_pm used in (ii)/(iv)): |l_pm| <= l, |l_pm'| <= |l'| pointwise; l_- = conj l_+; |l_pm| <= pi + log(1/s_d).
  [E] (iii)_d: m_k(d) = -(p/pi) Gamma(kp) (2 pi n)^{-kp} S_k(d), S_k(d) = sum_m sin(pi k p/2 - 2 pi m d)/m^{1+kp}, with S_k computed from
      the series by residue classes (d rational: sum_m e^{-2 pi i m d} m^{-sig} = Q^{-sig} sum_{j=1}^Q e^{-2 pi i j d} zeta(sig, j/Q), the
      Hurwitz series of DLMF 25.11.1 as a definition, sig > 1); m_k real; |S_k(d)| <= zeta(1+kp) (d-free majorant).
      Remark (NOT QUOTED, Hurwitz's formula): m_k(d) = zeta(-kp, 1+d)/(k n^{kp}) with mpmath's analytic continuation.
      Controls that must FAIL (asserted as failures): the real density l (d dropped) gives S_k(0), not S_k(d); and zeta(-kp, 1-d) (wrong a).
  [P] Sokhotski-Plemelj with the complex density: J_out - J_in = l_+(|z|) across Gamma_+ (and l_-(|z|) across Gamma_-), boundary values
      by the exact subtraction of l(r*) on [r*/2, 2r*].
  [R] (iv)_d: res_K(z) := J(z) - sum_{k<=K} m_k(z^k - 1) satisfies n^{(K+1)p}|res_K| bounded, and res_K/(m_{K+1}(z^{K+1}-1)) -> 1, for
      K = 1, 2, n = 10..640, z in S_in, S_out, on the negative axis and on the seams (both boundary values), |z| <= R_1 = 6;
      d-uniformity: d in {-0.02, -0.5, -0.98}.
  [D] (iv)_d, last clause: |E_n(x) - E_n(0)| <= C n^{-2p}|x| for real x (both signs), E_n := J - m_1(z - 1) (J(0) by the same quadrature).
  [G] (ii)_d with the literal G_d (chi_d by quadrature of G3's seam densities chi_pm^d): G_d(z) - G_d(1) = J(z) at points next to the seams
      (both sides), in S_in, S_out (G3 §5 (F) did 4 points away from the seams)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 30
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi


def qq(r, n, p): return mp.exp(-2*PI*n*r**(-1/p))
def l_real(r, n, p): return -mp.log1p(-mp.exp(-2*PI*n*r**(-1/p)))
def l_pm(r, n, p, d, sg):
    Q = mp.expj(sg*2*PI*d)        # log1p: no cancellation when q underflows (r -> 0); 1 - Qq has |.| >= s_d as q -> 1
    return -mp.log1p(-Q*mp.exp(-2*PI*n*r**(-1/p)))
def dl_real(r, n, p):
    y = 2*PI*n*r**(-1/p); q = mp.exp(-y); dq = q*y/(p*r); return dq/(1 - q)
def dl_pm(r, n, p, d, sg):
    Q = mp.expj(sg*2*PI*d); y = 2*PI*n*r**(-1/p); q = mp.exp(-y); dq = q*y/(p*r)
    return Q*dq/(1 - Q*q)


def sub_int(f, r0, w, extra):
    """int_0^oo f(r) dr/(r - w), with f(r0) subtracted on [r0/2, 2 r0] and added back exactly (Im w != 0 or w off [r0/2, 2r0])."""
    f0 = f(r0)
    g = lambda u: (f(mp.e**u) - (f0 if r0/2 <= mp.e**u <= 2*r0 else 0))/(mp.e**u - w)*mp.e**u
    L = mp.log(r0); pts = sorted(set([mp.mpf(-40), L - mp.log(2), L, L + mp.log(2), mp.mpf(60)] + [x for x in extra if -40 < x < 60]))
    return mp.quad(g, pts) + f0*(mp.log(2*r0 - w) - mp.log(r0/2 - w))


def J(z, n, p, d, dens=None):
    """(F.1)_d.  dens(sg) -> density function on Gamma_sg; default l_pm (complex).  K = 1/(zeta - z) - 1/(zeta - 1) splits the
    integral into two Cauchy integrals, each computed with subtraction at r0 = |z| resp. 1."""
    th = PI*p/2; e = mp.expj(th)
    if dens is None: dens = lambda sg: (lambda r: l_pm(r, n, p, d, sg))
    extra = [p*mp.log(n), mp.log(2*PI*n)*p, mp.mpf(0)]
    tot = 0
    for sg in (1, -1):
        f = dens(sg); es = e if sg == 1 else mp.conj(e)
        # int f(r) es/(r es - z) dr = int f(r)/(r - z/es) dr
        Iz = sub_int(f, abs(z), z/es, extra) if z != 0 else mp.quad(lambda u: f(mp.e**u), [-40, 0, 60])
        I1 = sub_int(f, mp.mpf(1), 1/es, extra)
        tot += sg*(Iz - I1)
    return tot/(2*PI*I)


def m_lit(k, n, p, d):
    th = PI*p/2; e = mp.expj(th)
    f = lambda u: (l_pm(mp.e**u, n, p, d, 1)*e*(mp.e**u*e)**(-k - 1) - l_pm(mp.e**u, n, p, d, -1)*mp.conj(e)*(mp.e**u*mp.conj(e))**(-k - 1))*mp.e**u
    return mp.quad(f, [-40, p*mp.log(n), p*mp.log(2*PI*n), 10, 60])/(2*PI*I)


def S_series(k, p, dnum, dden):
    """S_k(d), d = dnum/dden, from sum_m e^{-2 pi i m d} m^{-sig} = Q^{-sig} sum_j e^{-2 pi i j d} zeta(sig, j/Q) (series definition, sig > 1)."""
    sig = 1 + k*p; Q = dden; d = mp.mpf(dnum)/dden
    Z = sum(mp.expj(-2*PI*j*d)*mp.zeta(sig, mp.mpf(j)/Q) for j in range(1, Q + 1))/mp.mpf(Q)**sig
    return mp.im(mp.expj(PI*k*p/2)*Z)


def m_fourier(k, n, p, S): return -(p/PI)*mp.gamma(k*p)*(2*PI*n)**(-k*p)*S


DEL = [(-1, 50), (-1, 4), (-1, 2), (-4, 5), (-49, 50)]          # d = -0.02, -0.25, -0.5, -0.8, -0.98
PS = [mp.mpf('0.3'), mp.mpf('0.6'), mp.mpf('0.75')]

# [M] majorants
for p in PS:
    for (dn, dd) in DEL:
        d = mp.mpf(dn)/dd; worst_l, worst_dl, worst_conj, worst_bd = 0, 0, 0, 0
        sd = abs(mp.sin(2*PI*d)) if mp.cos(2*PI*d) >= 0 else mp.mpf(1)
        for n in (4, 40):
            for j in range(-30, 61):
                r = mp.mpf(10)**(mp.mpf(j)/10)
                lr, dlr = l_real(r, n, p), dl_real(r, n, p)
                if lr == 0: continue
                for sg in (1, -1):
                    worst_l = max(worst_l, abs(l_pm(r, n, p, d, sg))/lr)
                    if dlr != 0: worst_dl = max(worst_dl, abs(dl_pm(r, n, p, d, sg))/abs(dlr))
                    worst_bd = max(worst_bd, abs(l_pm(r, n, p, d, sg)) - (PI + mp.log(1/sd)))
                worst_conj = max(worst_conj, abs(l_pm(r, n, p, d, -1) - mp.conj(l_pm(r, n, p, d, 1))))
        lab = f"p={mp.nstr(p,2)} d={mp.nstr(d,3)}"
        C_.check(f"[M] |l_pm| <= l {lab}", float(max(worst_l - 1, 0)), 0.0, 1e-25)
        C_.check(f"[M] |l_pm'| <= |l'| {lab}", float(max(worst_dl - 1, 0)), 0.0, 1e-25)
        C_.check(f"[M] l_- = conj l_+ {lab}", float(worst_conj), 0.0, 1e-25)
        C_.check(f"[M] |l_pm| <= pi + log(1/s_d) {lab}", float(max(worst_bd, 0)), 0.0, 0.0)
        print(f"[M] {lab}: max|l_pm|/l = {mp.nstr(worst_l, 8)}, max|l_pm'|/|l'| = {mp.nstr(worst_dl, 8)}, "
              f"max(|l_pm| - pi - log(1/s_d)) = {mp.nstr(worst_bd, 4)}", flush=True)

# [E] moments (iii)_d
n = 7
for p in PS:
    for (dn, dd) in DEL:
        d = mp.mpf(dn)/dd; lab = f"p={mp.nstr(p,2)} d={mp.nstr(d,3)}"; out = []
        for k in (1, 2, 3):
            mk = m_lit(k, n, p, d); S = S_series(k, p, dn, dd); mf = m_fourier(k, n, p, S)
            mh = mp.zeta(-k*p, 1 + d)/(k*mp.mpf(n)**(k*p))
            m0 = m_fourier(k, n, p, S_series(k, p, 0, 1))        # control: real density (d dropped)
            mw = mp.zeta(-k*p, 1 - d)/(k*mp.mpf(n)**(k*p))       # control: wrong Hurwitz parameter (a reflected)
            C_.check(f"[E] m_k literal = Fourier-sum formula k={k} {lab}", float(abs(mk - mf)/abs(mf)), 0.0, 1e-20)
            C_.check(f"[E] m_k real k={k} {lab}", float(abs(mp.im(mk))/abs(mf)), 0.0, 1e-20)
            C_.check(f"[E] |S_k(d)| <= zeta(1+kp) k={k} {lab}", float(max(abs(S) - mp.zeta(1 + k*p), 0)), 0.0, 0.0)
            C_.check(f"[E] Remark (NOT QUOTED): m_k = zeta(-kp,1+d)/(k n^kp) k={k} {lab}", float(abs(mk - mh)/abs(mh)), 0.0, 1e-20)
            C_.check(f"[E] CONTROL must fail: real density gives m_k(d) k={k} {lab}", float(abs(m0 - mk)/abs(mk)) > 1e-3, True, 0)
            C_.check(f"[E] CONTROL must fail: zeta(-kp,1-d) k={k} {lab}", float(abs(mw - mk)/abs(mk)) > 1e-3, True, 0)
            out.append((k, mk, abs(mk - mf)/abs(mf), abs(mk - mh)/abs(mh), abs(m0 - mk)/abs(mk)))
        print(f"[E] {lab}: " + "; ".join(f"k={k} m_k={mp.nstr(mp.re(mk), 12)} rel.dev Fourier {mp.nstr(e1, 2)}, Hurwitz {mp.nstr(e2, 2)}, "
                                         f"control (d dropped) {mp.nstr(e3, 3)}" for (k, mk, e1, e2, e3) in out), flush=True)

# [P] Plemelj jump with the complex density, across both seams
for p in (mp.mpf('0.3'), mp.mpf('0.6')):
    for d in (mp.mpf('-0.25'), mp.mpf('-0.8')):
        n = 4; th = PI*p/2; worst = 0
        for r in (mp.mpf('0.5'), mp.mpf(3), mp.mpf(40)):
            for sg in (1, -1):
                eps = mp.mpf(10)**-18
                zo, zi = r*mp.expj(sg*(th + eps)), r*mp.expj(sg*(th - eps))        # outside / inside S_in
                jump = J(zo, n, p, d) - J(zi, n, p, d)
                worst = max(worst, abs(jump - l_pm(r, n, p, d, sg))/max(abs(l_pm(r, n, p, d, sg)), mp.mpf(10)**-6))   # floor: l underflows at r = 1/2
        C_.check(f"[P] J_out - J_in = l_pm on both seams (rel., floor 1e-6) p={mp.nstr(p,2)} d={d}", float(worst), 0.0, 1e-12)
        print(f"[P] p={mp.nstr(p,2)} d={d}: max rel |jump - l_pm| = {mp.nstr(worst, 3)}  (|l_+(40)| = {mp.nstr(abs(l_pm(mp.mpf(40), 4, p, d, 1)), 4)})", flush=True)

# [R] (iv)_d: remainder scaling, d-uniformity, seams included
for p in (mp.mpf('0.6'), mp.mpf('0.3')):
    th = PI*p/2; eps = mp.mpf(10)**-18
    Z = [mp.mpf('0.5'), mp.mpf('-1.3'), 2*mp.expj(th/2), mp.mpf('1.5')*mp.expj(mp.mpf('0.8')*PI), 2*mp.expj(th + eps), 2*mp.expj(th - eps),
         2*mp.expj(-th - eps)]
    if p > mp.mpf('0.5'): Z += [6*mp.expj(mp.mpf('0.9')*PI), 6*mp.expj(th/3)]
    NS = (10, 40, 160, 640)
    for d in (mp.mpf('-0.02'), mp.mpf('-0.5'), mp.mpf('-0.98')):
        lab = f"p={mp.nstr(p,2)} d={d}"; dn = int(mp.nint(d*50))
        Jv = {(nn, z): J(z, nn, p, d) for nn in NS for z in Z}
        for K in (1, 2):
            scaled, ratios, scaled2 = {}, {}, {}
            for nn in NS:
                ms = [m_fourier(k, nn, p, S_series(k, p, dn, 50)) for k in range(1, K + 2)]
                for z in Z:
                    res = Jv[(nn, z)] - sum(ms[k - 1]*(z**k - 1) for k in range(1, K + 1))
                    nxt = ms[K]*(z**(K + 1) - 1)
                    scaled[(nn, z)] = abs(res)*mp.mpf(nn)**((K + 1)*p); ratios[(nn, z)] = abs(res/nxt - 1)
                    scaled2[(nn, z)] = abs(res - nxt)*mp.mpf(nn)**((K + 2)*p)
            sup = {nn: max(scaled[(nn, z)] for z in Z) for nn in NS}
            sup2 = {nn: max(scaled2[(nn, z)] for z in Z) for nn in NS}
            rat_last = max(ratios[(NS[-1], z)] for z in Z); rat_first = max(ratios[(NS[0], z)] for z in Z)
            # d-free majorant of n^{(K+1)p}|m_{K+1}| times max|z^{K+1} - 1|, times 2
            maj = 2*(p/PI)*mp.gamma((K + 1)*p)*(2*PI)**(-(K + 1)*p)*mp.zeta(1 + (K + 1)*p)*max(abs(z**(K + 1) - 1) for z in Z)
            C_.check(f"[R] n^((K+1)p)|res_K| bounded in n K={K} {lab}", float(max(sup[NS[-1]]/sup[NS[1]] - 1.5, 0)), 0.0, 0.0)
            C_.check(f"[R] res_K / next term -> 1 (n=640) K={K} {lab}", float(rat_last), 0.0, 0.4)
            C_.check(f"[R] next order: n^((K+2)p)|res_K - next| bounded in n K={K} {lab}", float(max(sup2[NS[-1]]/sup2[NS[1]] - 1.5, 0)), 0.0, 0.0)
            C_.check(f"[R] ratio improves with n K={K} {lab}", float(max(rat_last - rat_first, 0)), 0.0, 0.0)
            C_.check(f"[R] d-free majorant at n=640 K={K} {lab}", float(max(sup[NS[-1]] - maj, 0)), 0.0, 0.0)
            print(f"[R] {lab} K={K}: sup_z n^((K+1)p)|res| = " + ", ".join(f"{nn}:{mp.nstr(sup[nn], 5)}" for nn in NS)
                  + f" (d-free majorant {mp.nstr(maj, 4)}); n^((K+2)p)|res - next|: " + ", ".join(f"{nn}:{mp.nstr(sup2[nn], 4)}" for nn in NS) + f"; max|res/next - 1|: n=10 {mp.nstr(rat_first, 3)}, n=640 {mp.nstr(rat_last, 3)}", flush=True)

# [D] |E_n(x) - E_n(0)| <= C n^{-2p} |x| on the real axis (both signs)
for p in (mp.mpf('0.6'),):
    for d in (mp.mpf('-0.5'), mp.mpf('-0.98')):
        vals = {}
        for nn in (20, 80, 320):
            m1 = m_fourier(1, nn, p, S_series(1, p, int(mp.nint(d*50)), 50))
            E = lambda z: J(z, nn, p, d) - m1*(z - 1)
            E0 = E(mp.mpf(0))
            vals[nn] = max(abs(E(x) - E0)/abs(x)*mp.mpf(nn)**(2*p) for x in (mp.mpf('0.01'), mp.mpf('0.3'), mp.mpf(-0.01), mp.mpf(-2), mp.mpf(3)))
        C_.check(f"[D] n^2p |E_n(x)-E_n(0)|/|x| bounded p={mp.nstr(p,2)} d={d}", float(max(vals[320]/vals[20] - 1.5, 0)), 0.0, 0.0)
        print(f"[D] p={mp.nstr(p,2)} d={d}: max_x n^2p|E_n(x)-E_n(0)|/|x| = " + ", ".join(f"{k}:{mp.nstr(v, 5)}" for k, v in vals.items()), flush=True)

# [G] (ii)_d with the literal G_d next to the seams (G3's construction; chi_d by quadrature with the same subtraction)
def jd(t, d):
    with mp.extradps(int(max(0, mp.log10(abs(t)))) + 10):
        return +(mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*PI)/2)
for (p, d) in ((mp.mpf('0.6'), mp.mpf('-0.5')), (mp.mpf('0.3'), mp.mpf('-0.8'))):
    n = 4; th = PI*p/2; w = (1 - 1/p)*(mp.mpf(1)/2 + d); lam = mp.gamma(1 + d)*(2*PI)**d
    tt = lambda z: n*mp.exp(-mp.log(z)/p)
    logBin = lambda z: (w + 1)*mp.log(1 + z) - mp.log(1 + lam*z)
    logBout = lambda z: (mp.mpf(1)/2 + d)*mp.log(1 - z/(2*PI*n))
    cache = {}
    def chip(r):
        if r in cache: return cache[r]
        z = r*mp.expj(th); t = tt(z); ex = -2*PI*I*(t - d)
        lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -300 else mp.mpc(0)
        cache[r] = -jd(t, d) - lg + logBin(z) - logBout(z); return cache[r]
    dens = lambda sg: (chip if sg == 1 else (lambda r: mp.conj(chip(r))))
    def chi(z):
        e = mp.expj(th); extra = [p*mp.log(n), mp.log(2*PI*n), mp.mpf(0)]
        return (sub_int(dens(1), abs(z), z/e, extra) - sub_int(dens(-1), abs(z), z*e, extra))/(2*PI*I)
    def Gd(z):
        inside = abs(mp.arg(z)) < th
        return (-jd(tt(z), d) + logBin(z) + chi(z)) if inside else (logBout(z) + chi(z))
    G1 = Gd(mp.mpf(1)); worst = 0
    for z in (2*mp.expj(th*(1 - mp.mpf(10)**-8)), 2*mp.expj(th*(1 + mp.mpf(10)**-8)), mp.mpf('0.7')*mp.expj(-th*(1 - mp.mpf(10)**-8)),
              mp.mpf('0.7')*mp.expj(-th*(1 + mp.mpf(10)**-8)), mp.mpf('3.5')*mp.expj(th/2), -mp.mpf('2.5')):
        worst = max(worst, abs(Gd(z) - G1 - J(z, n, p, d)))
    C_.check(f"[G] (ii)_d: G_d(z) - G_d(1) = J(z) next to the seams p={mp.nstr(p,2)} d={d}", float(worst), 0.0, 1e-15)
    print(f"[G] p={mp.nstr(p,2)} d={d}: max |G_d(z) - G_d(1) - J(z)| over 6 points (4 at angular distance 1e-8 from a seam) = {mp.nstr(worst, 3)}", flush=True)
C_.finish()
