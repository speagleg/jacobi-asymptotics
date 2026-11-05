"""JZC M3a, step H-c (JZC_M3a_H_Hc.md §§1-2): the Hurwitz band factor H_n^d = (D~_d B_d)^{-2} for p > 1 (NUMERICAL, mpmath dps 34).
Notation of JZC_M3a_H_G12.md §1 (-1 < d <= 0, t = n z^{-1/p}, theta_d = pi(t - d)):
  j_d(t)  = LnGamma(t - d) - (t - d - 1/2) ln t + t - 1/2 ln 2pi
  b_d(y)  = 2 Im(-j_d(t_+) - Log(1 - e^{-2 pi i (t_+ - d)}))          (y < 0, t_+ = n|y|^{-1/p} e^{-i pi/p})
  log B_d = -(1/2pi) int_{-oo}^0 b_d(y)[1/(y - z) - 1/(y - 1)] dy,   G_d := -j_d(t) + log B_d,   H_n^d = e^{-2 G_d}   (the CONSTRUCTION)
  e_d(y)  = 2 Im Log(1 - e^{-2 pi i (t_+ - d)})                       (the jump density of G_d, Lemma Hc.1 (a))
  m_k(d)  = (1/2pi) int_{-oo}^0 e_d(y) y^{-k-1} dy                    (moments, by quadrature)
  S_k(d)  = sum_{m>=1} sin(pi k p/2 - 2 pi m d)/m^{1+kp},  mhat_k(d) := -(p/pi) Gamma(kp) (2pi)^{-kp} S_k(d)   (Fourier sum; m_k = mhat_k n^{-kp})
Claims checked (asserted; lemma numbers of JZC_M3a_H_Hc.md):
  [1] Hc.1 (a): d-free majorants |e_d(y)| <= pi |q|, |e_d'(y)| <= 4 pi |q| |t_+| / (p |y| (1 - |q|)), |q| = exp(-2 pi sin(pi/p) |t_+|), on a grid
      of y in (-10^6, -10^-3); d in {0, -0.3, -0.7, -0.95}.
  [2] Hc.1 (b) (E.2.1)_d: G_d(z) - G_d(1) from the CONSTRUCTION = (1/2pi) int e_d(y)(z-1)/((y-z)(y-1)) dy at 4 points incl. next to the cut.
  [3] Hc.2 (i): m_k(d) by quadrature = mhat_k(d) n^{-kp} (S_k by residue classes mod 20 with Hurwitz series; cross-check by mp.lerchphi), k <= 3; at d = 0 also = zeta(-kp)/(k n^{kp})
      (E3 Lemma F.1'(i)). Remark 3.3 (NOT QUOTED, NUMERICAL only, not used): = zeta(-kp, 1 + d)/(k n^{kp}).
  [4] Hc.2 (ii): r_K(z) := [G_d(z) - G_d(1)] - sum_{k<=K} m_k(d)(z^k - 1), K = 1, 2, n in {8, 16, 32, 64} (p = 3: up to 32), z in 7 points of
      {|z| <= R_1 = 4c + 2} (incl. both sides of (-R_1, 0) at distance 1e-6, and |z| = R_1): (a) n^{(K+1)p} max_z |r_K| is bounded, and below the
      d-free majorant 2 Mbar_{K+1} max_z|z^{K+1} - 1|, Mbar_k := (p/pi)Gamma(kp)(2pi)^{-kp} zeta(1+kp); (b) r_K/(m_j(d)(z^j - 1)) -> 1 at rate
      n^{-p}, j the first index > K with m_j(d) != 0 (relative error at n_max < relative error at 8 times 8^{-p}·2.5, i.e. it decays like n^{-p}).
      (G_d - G_d(1) here from the representation (E.2.1)_d, which [2] identifies with the construction.)
  CONTROLS (must fail, asserted as failures):
  [C1] lattice moments m_k(0) in place of m_k(d), d != 0: the K = 1 rate test (b) fails (relative error does not decay).
  [C2] Hurwitz moments with the reflected parameter zeta(-kp, -d)/(k n^{kp}) (a -> 1 - a), d != -1/2, p not an integer (at p = 3, k = 1,
       zeta(-3, a) = zeta(-3, 1 - a) since B_4(1 - a) = B_4(a): the control is degenerate there): test (b) fails.
  [C3] sharpness: n^{jp + 1/2}|r_K| is NOT bounded (j as in (b)) (grows by > 1.5 from n = 8 to n_max; the exact factor is (n_max/8)^{1/2} >= 2).
c = c(p) = (1/4)(pi/(2 I_p))^p, I_p = (sqrt(pi)/2) Gamma(1/p + 1/2)/Gamma(1/p + 1)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 34
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi


def cp(p): Ip = mp.sqrt(PI)/2*mp.gamma(1/p + mp.mpf(1)/2)/mp.gamma(1/p + 1); return (PI/(2*Ip))**p/4
def jd(t, d): return mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*PI)/2
def logm(t, d):   # Log(1 - e^{-2 pi i (t - d)}); |e^{...}| < 1 for t in the lower half plane
    ex = -2*PI*I*(t - d)
    return mp.log(-mp.expm1(ex)) if mp.re(ex) > -5000 else mp.mpc(0)
def tplus(r, n, p): return n*mp.power(r, -1/p)*mp.expjpi(-1/p)      # y = -r
def bfun(r, n, p, d): tp = tplus(r, n, p); return 2*mp.im(-jd(tp, d) - logm(tp, d))
def efun(r, n, p, d): return 2*mp.im(logm(tplus(r, n, p), d))
K1 = lambda y, z: 1/(y - z) - 1/(y - 1)
K2 = lambda y, z: (z - 1)/((y - z)*(y - 1))


def cauchy(dens, z, n, p, d, kern):     # (1/2pi) int_{-oo}^0 dens(-y) kern(y, z) dy, y = -e^u
    f = lambda u: dens(mp.e**u, n, p, d)*kern(-mp.e**u, z)*mp.e**u
    L = mp.log(max(abs(z), mp.mpf('1e-3')))
    pts = sorted(set([mp.mpf(-60), mp.mpf(-10), mp.mpf(0), L - 3, L - mp.mpf('0.01'), L, L + mp.mpf('0.01'), L + 3, mp.mpf(30), mp.mpf(300)]))
    return mp.quad(f, pts)/(2*PI)


def G_cons(z, n, p, d): return -jd(n*mp.power(z, -1/p), d) - cauchy(bfun, z, n, p, d, K1)
def G_rep(z, n, p, d): return cauchy(efun, z, n, p, d, K2)
def S(k, p, d, Q=20):
    """S_k(d) = sum_m sin(pi k p/2 - 2 pi m d)/m^{1+kp} by residue classes mod Q (Q d in Z): sum_{m = j mod Q} m^{-s} = Q^{-s} zeta(s, j/Q),
    the Hurwitz series (DLMF 25.11.1 as a definition, s > 1; mpmath zeta(s, a) with 0 < a <= 1 is accurate there). mp.nsum was used
    first and is inaccurate here (relative errors up to 1e-6 for non-oscillating terms): Rule A item 11."""
    assert abs(Q*d - mp.nint(Q*d)) < mp.mpf(10)**-20
    A = PI*k*p/2; s = 1 + k*p
    return Q**(-s)*mp.fsum(mp.sin(A - 2*PI*j*d)*mp.zeta(s, mp.mpf(j)/Q) for j in range(1, Q + 1))
def S_lerch(k, p, d): z = mp.exp(-2*PI*I*d); return mp.im(mp.exp(I*PI*k*p/2)*z*mp.lerchphi(z, 1 + k*p, 1))
def mhat(k, p, d): return -(p/PI)*mp.gamma(k*p)*(2*PI)**(-k*p)*S(k, p, d)
def Mbar(k, p): return (p/PI)*mp.gamma(k*p)*(2*PI)**(-k*p)*mp.zeta(1 + k*p)


PS = [mp.mpf(5)/4, mp.mpf(3)/2, mp.mpf(3)]
DS = [mp.mpf(0), mp.mpf('-0.3'), mp.mpf('-0.7'), mp.mpf('-0.95')]

# [1] majorants of the jump density (d-free)
for p in PS:
    for d in DS:
        w1 = w2 = 0
        for E in [mp.mpf(e)/4 for e in range(-12, 25)]:
            r = mp.mpf(10)**E; n = mp.mpf(8); tp = tplus(r, n, p); q = mp.exp(-2*PI*mp.sin(PI/p)*abs(tp))
            w1 = max(w1, abs(efun(r, n, p, d))/(PI*q)) if q > mp.mpf(10)**-3000 else w1
            de = mp.diff(lambda rr: efun(rr, n, p, d), r)            # d/dr = -d/dy; modulus the same
            maj = 4*PI*q*abs(tp)/(p*r*(1 - q))
            if q > mp.mpf(10)**-3000: w2 = max(w2, abs(de)/maj)
        lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,2)}"
        print(f"[1] {lab}: max |e_d|/(pi|q|) = {mp.nstr(w1,4)},  max |e_d'|/majorant = {mp.nstr(w2,15)}")
        C_.check(f"[1] |e_d| <= pi|q| {lab}", float(max(w1 - 1, 0)), 0.0, 0.0)
        C_.check(f"[1] |e_d'| <= majorant {lab}", float(max(w2 - 1, 0)), 0.0, 1e-12)   # the majorant is attained when q_d > 0

# [2] the representation (E.2.1)_d against the construction
for p in PS:
    for d in DS:
        n = mp.mpf(8); g1 = G_cons(mp.mpf(1), n, p, d); worst = 0
        for z in (4*cp(p) + 1, mp.mpc(2, '1.5'), mp.mpc('-1.5', '0.5'), mp.mpc(-2, '1e-6'), mp.mpc('0.3', 0)):
            worst = max(worst, abs(G_cons(z, n, p, d) - g1 - G_rep(z, n, p, d)))
        print(f"[2] p={mp.nstr(p,3)} d={mp.nstr(d,2)} n=8: max |G_d(z) - G_d(1) - Cauchy(e_d)(z)| over 5 points = {mp.nstr(worst,3)}")
        C_.check(f"[2] (E.2.1)_d p={mp.nstr(p,3)} d={mp.nstr(d,2)}", float(worst), 0.0, 1e-25)

# [3] moments = Fourier sums
for p in PS:
    for d in DS:
        n = mp.mpf(8)
        for k in (1, 2, 3):
            mq = cauchy(efun, mp.mpf(0), n, p, d, lambda y, z: y**(-k - 1))
            mf = mhat(k, p, d)*n**(-k*p); sc = max(abs(mf), Mbar(k, p)*n**(-k*p))
            lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,2)} k={k}"
            C_.check(f"[3] quadrature = Fourier sum {lab}", float(abs(mq - mf)/sc), 0.0, 1e-20)
            C_.check(f"[3] residue classes = lerchphi {lab}", float(abs(S(k, p, d) - S_lerch(k, p, d))), 0.0, 1e-25)
            if d == 0:
                C_.check(f"[3] d=0: = zeta(-kp)/(k n^kp) {lab}", float(abs(mf - mp.zeta(-k*p)/(k*n**(k*p)))/sc), 0.0, 1e-25)
            hz = mp.zeta(-k*p, 1 + d)/(k*n**(k*p))
            C_.check(f"[3] Remark 3.3 (NUMERICAL, NOT QUOTED) {lab}", float(abs(mf - hz)/sc), 0.0, 1e-25)
            print(f"[3] {lab}: m_k quad {mp.nstr(mq,12)}  Fourier {mp.nstr(mf,12)}  |S_k|/zeta(1+kp) = {mp.nstr(abs(S(k,p,d))/mp.zeta(1+k*p),4)}")

# [4] remainder rate, and controls
def zpts(p):
    c = cp(p); return [4*c + 1, 4*c + 2, mp.mpc(2, '1.5'), mp.mpc('-1.5', '0.5'), mp.mpc(-2, '1e-6'), mp.mpc(-2, '-1e-6'), mp.mpc('0.3', 0)]


def rate_test(rel):   # rel: list of (n, max relative error); passes iff it decays like n^{-p} (ratio criterion below)
    (n0, e0), (n1, e1) = rel[0], rel[-1]
    return e1 <= 2.5*e0*(n0/n1)**PP


for p in PS:
    PP = p
    NS = [mp.mpf(x) for x in ((8, 16, 32) if p > 2 else (8, 16, 32, 64))]
    for d in DS:
        lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,2)}"
        mh = {k: mhat(k, p, d) for k in range(1, 6)}
        mh0 = {k: mhat(k, p, mp.mpf(0)) for k in range(1, 6)}
        mrefl = {k: mp.zeta(-k*p, -d)*k**-1 for k in range(1, 6)} if d != 0 else None
        Gs = {n: [G_rep(z, n, p, d) for z in zpts(p)] for n in NS}
        for K in (1, 2):
            j = next(jj for jj in range(K + 1, 6) if abs(mh[jj]) > mp.mpf(10)**-12)
            sup, rel, sharp, relC1, relC2 = [], [], [], [], []
            for n in NS:
                rs = [g - sum(mh[k]*n**(-k*p)*(z**k - 1) for k in range(1, K + 1)) for g, z in zip(Gs[n], zpts(p))]
                sup.append(max(abs(r) for r in rs)*n**((K + 1)*p)); sharp.append(max(abs(r) for r in rs)*n**(j*p + mp.mpf(1)/2))
                rel.append((n, max(abs(r/(mh[j]*n**(-j*p)*(z**j - 1)) - 1) for r, z in zip(rs, zpts(p)))))
                if d != 0:
                    r0 = [g - sum(mh0[k]*n**(-k*p)*(z**k - 1) for k in range(1, K + 1)) for g, z in zip(Gs[n], zpts(p))]
                    relC1.append((n, max(abs(r/(mh[j]*n**(-j*p)*(z**j - 1)) - 1) for r, z in zip(r0, zpts(p)))))
                    r2 = [g - sum(mrefl[k]*n**(-k*p)*(z**k - 1) for k in range(1, K + 1)) for g, z in zip(Gs[n], zpts(p))]
                    relC2.append((n, max(abs(r/(mh[j]*n**(-j*p)*(z**j - 1)) - 1) for r, z in zip(r2, zpts(p)))))
            maj = 2*Mbar(K + 1, p)*max(abs(z**(K + 1) - 1) for z in zpts(p))
            print(f"[4] {lab} K={K}: n^((K+1)p) max|r_K| = {[mp.nstr(x,5) for x in sup]} (d-free majorant {mp.nstr(maj,4)}); "
                  f"rel. err. vs m_{j} term = {[mp.nstr(e,3) for _, e in rel]}")
            C_.check(f"[4a] bounded, below d-free majorant {lab} K={K}", float(max(max(sup) - maj, 0)), 0.0, 0.0)
            C_.check(f"[4b] r_K ~ m_j(z^j-1), rate n^-p {lab} K={K}", float(not rate_test(rel)), 0.0, 0.0)
            C_.check(f"[C3] CONTROL n^(jp+1/2)|r_K| unbounded {lab} K={K}", float(not (sharp[-1] > mp.mpf("1.5")*sharp[0])), 0.0, 0.0)
            if d != 0 and K == 1:
                print(f"     [C1] lattice moments: rel. err. {[mp.nstr(e,3) for _, e in relC1]};  [C2] zeta(-kp,-d): {[mp.nstr(e,3) for _, e in relC2]}")
                C_.check(f"[C1] CONTROL lattice moments fail the rate test {lab}", float(rate_test(relC1)), 0.0, 0.0)
                if abs(d + mp.mpf(1)/2) > mp.mpf('0.01') and p != mp.nint(p):   # integer kp: zeta(-kp, a) = -B_{kp+1}(a)/(kp+1) is reflection-(anti)symmetric, control degenerate
                    C_.check(f"[C2] CONTROL zeta(-kp,-d) fails the rate test {lab}", float(rate_test(relC2)), 0.0, 0.0)
C_.finish()
