"""JZC M3a, Theorem H item 1 for 0 < p < 1 (JZC_M3a_H_G1u_plt1.md): the glued Hurwitz hard-edge parametrix with the alpha-frame
factor W~nat (Szego exponent beta' = alpha + 2 delta, Bessel order alpha) and the n-uniform hard-edge comparison (NUMERICAL, mpmath).
This is checks/m3a_g1u_hardedge.py ported to p < 1 WITH the actual seam band factor (not the model weight): every rho below is the
true glued rho_nat = W~nat/D_W of Lemma P2, computed from the Cauchy-integral representation of the seam band factor (Lemma F.1_d (ii),
JZC_M3a_H_G23plt1.md; the complex seam densities l_pm(r) = -Log(1 - e^{+-2 pi i d} e^{-2 pi n r^{-1/p}}) on Gamma_pm = {r e^{+-i th}},
th = pi p/2). Notation: G0(z) := Gd(z) - Gd(0) (Gd = the glued exponent of Lemma F.1_d, sector values),
  G0(z)  = (1/2 pi i) sum_{sg=+-} sg int_0^oo l_sg(r) e^{sg i th} [1/(zeta - z) - 1/zeta] dr,              zeta = r e^{sg i th},
  L_h(z) := log(D_{h0}(z)^2 / h0(z)),  h0 := e^{-2 G0}  (sector value of h0 at z; Paper 2 (eq:szego-repr) with c = log h0(z)),
         = 2 R(z) (1/2 pi i) sum_sg sg int_0^oo l_sg(r) e^{sg i th} dr / ((zeta - z) R(zeta))     (Lemma P1, Remark P1.4: Fubini),
  rho_nat(z) = rho_mod(z) exp(-L_h(z)/2),  rho_mod = (-z)^{beta'/2}(4c - z)^{1/2}/(D_{x^beta'} D_{4c-x}) = (Ups^/4c)^{(1+beta')/2}.
Claims checked (asserted):
  [0a] the single-integral formula for L_h equals Paper 2 (eq:szego-repr) evaluated by Gauss-Chebyshev quadrature over the band with
       log h0(x) = -2 G0(x) at the nodes (independent route; checks the Fubini step of Remark P1.4).
  [0b] G0 from the representation equals the literal glued exponent of G3 §2 (j_d, B_in^d with the Moebius factor, B_out^d, chi_d by
       quadrature of G3's seam densities) near 0, at relative angular distance 1e-12 (EPS) from the seams (both sides) and on the negative
       axis (fixed per Rule R review B, N-2).
  [1] Lemma P1 (b)-(d): with mu_k = 2 m_k(d) (Fourier sums S_k(d), Lemma F.1_d (iii)) and M_mu = sum_k mu_k Q_k,
        sup_z n^{(K+1)p} |G0(z) - sum_{k<=K} m_k z^k| / |z|   and   sup_z n^{(K+1)p} |L_h(z) - R(z) M_mu(z)| / |R(z)|
      are bounded in n (n = 10..640; K = 0, 1, 2), d-uniformly (d = -0.02, -0.5, -0.98), on a grid of 0 < |z| <= 0.3 incl. both
      boundary values on both seams, S_out, the negative axis, plus points near 4c (the Airy disc). Asserted as: every n is below
      twice the d-free majorant of the next term (|S_k(d)| <= zeta(1+kp)), and the n = 640 value is within 25% of the n = 160 value
      (the approach to the limit |m_{K+1}| n^{(K+1)p} max|z|^K is from below at d = -0.02, K = 2). CONTROL (must fail): the
      same sup with n^{(K+2)p} grows (the rate n^{-(K+1)p} is not beaten).
  [2] Lemma P2: |rho_nat|^{+-1} bounded on 1e-12 <= |z| <= c/2 uniformly in n in {10, 100, 1000} for |beta'| >= 1, incl. seams
      (both sides) and S_out; n^p |log(rho_nat/rho_mod)| / |z|^{1/2} bounded; band relation rho_+ rho_- = 1; glue
      rho_out/rho_in = e^{-l_pm(|z|)} on both seams. CONTROL (must fail): rho_w (Bessel-alpha W~, beta' Szego function) is unbounded.
  [3] Lemma P3 (i): |A^{+-1}| bounded near 0 with the true glued rho (seams incl.), A_+ = A_- on the band. CONTROL: A_w unbounded.
  [4] Lemma P2 (ii) / L3': on the lips, omega_nat := e^{-+ i pi alpha} rho_nat^{-2} (exact lip match) satisfies
      |omega_nat - e^{-+ i pi alpha}| <= C |z|^{1/2} uniformly in n; omega_nat computed independently as D_W^2 e^{+-2 pi i d}/W0 with
      D_W^2/W0 = (D_{x^b}^2/z^b)(D_{4c-x}^2/(4c-z)) e^{L_h}. CONTROL: omega_nat -> e^{-+ i pi beta'} fails.
  [5] Lemma P3 (iii), the matching rate in n on the circle |z| = c/2 (central-sector points incl. both boundary values on both seams):
      J := P0hat P0inf^{-1} with the TRUE glued rho_nat: n |J - I| flat; after Delta_1^nat/n the remainder is O(n^-2) (exponent
      log2(e(n)/e(2n)) in [1.9, 2.15]) or exponentially small (alpha = -1/2, Bessel order 1/2).
      Lemma P5 (band-factor gauge, = H-c for p < 1): with Delta_1^mu (rho_mod e^{-R M_mu/2}, J_g = floor(1/p) moments (the smallest J with (J+1)p > 1); fixed per Rule R review B, N-2) in place of
      Delta_1^nat the remainder exponent is >= min(2, 1 + (J_g+1)p) - 0.1.
      CONTROLS (must fail): (a) nu = beta' in Q0: O(1/n) remainder (asserted only if |beta'| != |alpha|: Q0 depends on nu^2);
      (b) band factor dropped (rho_mod in Delta_1): the remainder is not O(n^-2) (exponent ~ 1 + p) (asserted wherever the control is
      discriminating: if some of its exponents fall below the claim's window [1.9, 2.15], or if that remainder exceeds 10x the true
      one at n = 400; asserted in 4 of 5 sets; fixed per Rule R review B, N-1). The [1] n^{-2p} controls are asserted only if
      |S_1(d)| >= 0.05 zeta(1+p) (otherwise m_1 is too small for the n^{-p} rate to be visible: Remark P1.3).
      The glue test [2] uses an angular offset 1e-24 (with 1e-12 the offset error is O(1e-8) relative).
  [6] Lemma P3 (iv): |P0hat^{+-1}| |zeta|^{|alpha|/2} n^{-1/2} <= C (n = 10, 100, 1000; true glued rho; seam points included).
      CONTROL: with rho_w the same quantity is unbounded.
Parameters (p, alpha, d): (0.6, -1/2, -0.8), (0.6, -0.6, -0.8), (0.3, -0.3, -0.9), (0.75, 0.3, -0.3), (0.75, 0.6, -0.95);
beta' = -2.1, -2.2, -2.1, -0.3, -1.3. Precision: mpmath dps 30. Runtime ~ 25 min (2 cores not needed)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import mpmath as mp
from so_coeffs import c_p_mp
from spec_common import Checks
mp.mp.dps = 30
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi
s3 = mp.matrix([[1, 0], [0, -1]])
Mm = mp.matrix([[1, I], [I, 1]])/mp.sqrt(2)
EPS = mp.mpf(10)**-12          # relative angular offset for seam boundary values


def diag(a, b): return mp.matrix([[a, 0], [0, b]])
def nrm(A): return max(abs(A[i, j]) for i in range(2) for j in range(2))
def adj(A): return mp.matrix([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])
def Rr(z, c): return z*mp.sqrt(1 - 4*c/z)                     # R(z) = (z(z-4c))^{1/2} ~ z, analytic off [0, 4c]


def sub_int(f, r0, w, extra):
    """int_0^oo f(r) dr/(r - w), f(r0) subtracted on [r0/2, 2 r0] and added back exactly (as m3a_g23_F1.py)."""
    f0 = f(r0)
    g = lambda u: (f(mp.e**u) - (f0 if r0/2 <= mp.e**u <= 2*r0 else 0))/(mp.e**u - w)*mp.e**u
    L = mp.log(r0); pts = sorted(set([mp.mpf(-40), L - mp.log(2), L, L + mp.log(2), mp.mpf(60)] + [x for x in extra if -40 < x < 60]))
    return mp.quad(g, pts) + f0*(mp.log(2*r0 - w) - mp.log(r0/2 - w))


def S_series(k, p, dnum, dden):
    """S_k(d), d = dnum/dden, from the Hurwitz series by residue classes (as m3a_g23_F1.py)."""
    sig = 1 + k*p; Q = dden; d = mp.mpf(dnum)/dden
    Z = sum(mp.expj(-2*PI*j*d)*mp.zeta(sig, mp.mpf(j)/Q) for j in range(1, Q + 1))/mp.mpf(Q)**sig
    return mp.im(mp.expj(PI*k*p/2)*Z)


class Band:
    """the seam band factor of sigma^d at degree n (Lemma F.1_d), through its Cauchy-integral representation."""
    def __init__(s, p, dnum, dden, n, c):
        s.p, s.d, s.n, s.c = mp.mpf(p), mp.mpf(dnum)/dden, mp.mpf(n), c
        s.th = PI*s.p/2
        s.extra = [s.p*mp.log(s.n), s.p*mp.log(2*PI*s.n), mp.mpf(0), mp.log(4*c)]
        s.m = [None] + [-(s.p/PI)*mp.gamma(k*s.p)*(2*PI*s.n)**(-k*s.p)*S_series(k, s.p, dnum, dden) for k in (1, 2, 3, 4)]
        s.cG, s.cL = {}, {}

    def l(s, r, sg): return -mp.log1p(-mp.expj(sg*2*PI*s.d)*mp.exp(-2*PI*s.n*r**(-1/s.p)))

    def G0(s, z):
        if z in s.cG: return s.cG[z]
        tot = 0
        for sg in (1, -1):
            w = z*mp.expj(-sg*s.th)
            tot += sg*w*sub_int(lambda r: s.l(r, sg)/r, abs(z), w, s.extra)
        s.cG[z] = tot/(2*PI*I); return s.cG[z]

    def Lh(s, z):
        if z in s.cL: return s.cL[z]
        tot = 0
        for sg in (1, -1):
            e = mp.expj(sg*s.th); w = z/e
            tot += sg*sub_int(lambda r: s.l(r, sg)/Rr(r*e, s.c), abs(z), w, s.extra)
        s.cL[z] = 2*Rr(z, s.c)*tot/(2*PI*I); return s.cL[z]

    def MQ(s, K, z):              # M_mu(z) = sum_{k<=K} mu_k Q_k(z), mu_k = 2 m_k, Q_k = sum_{j<k} z^{k-1-j} C(2j,j) c^j  (E3 Lemma E3.4)
        return sum(2*s.m[k]*sum(z**(k - 1 - j)*mp.binomial(2*j, j)*s.c**j for j in range(k)) for k in range(1, K + 1))


class Model:
    def __init__(s, p, al, dnum, dden):
        s.p, s.al, s.de = mp.mpf(p), mp.mpf(al), mp.mpf(dnum)/dden; s.dn, s.dd = dnum, dden; s.bp = s.al + 2*s.de
        s.c = mp.mpf(c_p_mp(float(p))); c = s.c; ap = 1/s.p + mp.mpf(1)/2
        s.zc = [mp.rf(mp.mpf(1)/2, k)/mp.factorial(k)/(4*c)**k/((ap + k)*(k + mp.mpf(1)/2))*(4*c)**mp.mpf(-0.5)/(s.p*PI) for k in range(90)]
        s.bands = {}

    def band(s, n):
        if n not in s.bands: s.bands[n] = Band(s.p, s.dn, s.dd, n, s.c)
        return s.bands[n]

    def f(s, z): return -(PI**2/4)*z*mp.polyval(s.zc[::-1], z)**2

    def P0(s, z):
        a = mp.exp(mp.log((z - 4*s.c)/z)/4)
        return mp.matrix([[(a + 1/a)/2, (a - 1/a)/(2*I)], [-(a - 1/a)/(2*I), (a + 1/a)/2]])

    def Ups(s, z): return (mp.sqrt(z) + mp.sqrt(z - 4*s.c))**2

    def DW(s, z, b):
        U = s.Ups(z); c = s.c
        return (4*c*z/U)**(b/2)*(4*c*(z - 4*c)/U)**(mp.mpf(1)/2)

    def Wt(s, z, b): return (-z)**(b/2)*(4*s.c - z)**(mp.mpf(1)/2)
    def rho_mod(s, z): return s.Wt(z, s.bp)/s.DW(z, s.bp)
    def rho(s, z, n): return s.rho_mod(z)*mp.exp(-s.band(n).Lh(z)/2)                     # true glued rho_nat
    def rho_mu(s, z, n, K): return s.rho_mod(z)*mp.exp(-Rr(z, s.c)*s.band(n).MQ(K, z)/2)  # gauge model (Lemma P5)
    def rho_w(s, z, n): return s.Wt(z, s.al)/s.DW(z, s.bp)*mp.exp(-s.band(n).Lh(z)/2)    # control: Bessel-alpha W~

    def A(s, z, r):
        f4 = s.f(z)**(mp.mpf(1)/4)
        return s.P0(z)*diag(r, 1/r)*Mm*diag(f4, 1/f4)

    def Phi(s, zeta, nu):
        w = 2*mp.sqrt(zeta)
        Ia = mp.besseli(nu, w); Ka = mp.besselk(nu, w)
        Ip = (mp.besseli(nu - 1, w) + mp.besseli(nu + 1, w))/2
        Kp = -(mp.besselk(nu - 1, w) + mp.besselk(nu + 1, w))/2
        Psi = mp.matrix([[Ia, (I/PI)*Ka], [PI*I*w*Ip, -w*Kp]])
        e = mp.exp(-w)
        return s3*Psi*s3*diag(e, 1/e)

    def P0hat(s, z, n, r):
        sq = mp.sqrt(2*PI*mp.mpf(n))
        return s.A(z, r)*diag(sq, 1/sq)*s.Phi(mp.mpf(n)**2*s.f(z), s.al)*diag(1/r, r)

    def Delta1(s, z, r, nu):
        nu = mp.mpf(nu); P = s.P0(z)
        Q0 = mp.matrix([[-(1 + 4*nu**2), 2*I], [2*I, 1 + 4*nu**2]])
        return P*diag(r, 1/r)*Q0*diag(1/r, r)*mp.inverse(P)/(16*mp.sqrt(s.f(z)))


def seam_pts(r, th):
    return [r*mp.expj(th*(1 - EPS)), r*mp.expj(th*(1 + EPS)), r*mp.expj(-th*(1 - EPS)), r*mp.expj(-th*(1 + EPS))]


# ---------------- [0a] the single-integral formula for L_h vs (eq:szego-repr) by Gauss-Chebyshev over the band ----------------
p0 = mp.mpf('0.6'); c0 = mp.mpf(c_p_mp(0.6)); B0 = Band(p0, -1, 2, 4, c0); NG = 64
nodes = [2*c0*(1 - mp.cos((2*j - 1)*PI/(2*NG))) for j in range(1, NG + 1)]
Lx = [-2*B0.G0(x) for x in nodes]                                             # log h0(x) on the band
worst = 0
for z in (mp.mpc('0.1', '0.35'), mp.mpf('-0.3'), mp.mpc('1.2', '-0.4'), mp.mpf('0.5')*mp.expj(B0.th*(1 + EPS))):
    Lz = -2*B0.G0(z)
    quad = Rr(z, c0)*sum((Lx[j] - Lz)/(z - nodes[j]) for j in range(NG))/NG     # (R/pi) int (L(x) - L(z))/(z - x) dx/sqrt(x(4c-x))
    worst = max(worst, abs(quad - B0.Lh(z))/abs(B0.Lh(z)))
print(f"[0a] p=0.6 d=-1/2 n=4: max rel |Gauss-Chebyshev (eq:szego-repr) - single-integral L_h| = {mp.nstr(worst, 3)} (4 points, one on a seam)", flush=True)
C_.check("[0a] L_h single-integral formula = (eq:szego-repr) by band quadrature", float(worst), 0.0, 1e-12)


# ---------------- [0b] G0 from the representation vs the literal glued exponent of G3 §2, near 0 ----------------
def jd(t, d):
    with mp.extradps(int(max(0, mp.log10(abs(t)))) + 10):
        return +(mp.loggamma(t - d) - (t - d - mp.mpf(1)/2)*mp.log(t) + t - mp.log(2*PI)/2)
for (pp, dn, dd) in ((mp.mpf('0.6'), -1, 2), (mp.mpf('0.3'), -4, 5)):
    d = mp.mpf(dn)/dd; n = 4; th = PI*pp/2; wv = (1 - 1/pp)*(mp.mpf(1)/2 + d); lam = mp.gamma(1 + d)*(2*PI)**d
    Bd = Band(pp, dn, dd, n, mp.mpf(c_p_mp(float(pp))))
    tt = lambda z: n*mp.exp(-mp.log(z)/pp)
    logBin = lambda z: (wv + 1)*mp.log(1 + z) - mp.log(1 + lam*z)
    logBout = lambda z: (mp.mpf(1)/2 + d)*mp.log(1 - z/(2*PI*n))
    cache = {}
    def chip(r):
        if r in cache: return cache[r]
        z = r*mp.expj(th); t = tt(z); ex = -2*PI*I*(t - d)
        lg = mp.log(-mp.expm1(ex)) if mp.re(ex) > -300 else mp.mpc(0)
        cache[r] = -jd(t, d) - lg + logBin(z) - logBout(z); return cache[r]
    dens = lambda sg: (chip if sg == 1 else (lambda r: mp.conj(chip(r))))
    def chi(z):
        e = mp.expj(th); extra = [pp*mp.log(n), mp.log(2*PI*n), mp.mpf(0)]
        return (sub_int(dens(1), abs(z), z/e, extra) - sub_int(dens(-1), abs(z), z*e, extra))/(2*PI*I)
    def Glit(z):
        return (-jd(tt(z), d) + logBin(z) + chi(z)) if abs(mp.arg(z)) < th else (logBout(z) + chi(z))
    zref = mp.mpf('0.05'); gref = Glit(zref); worst = 0
    for z in seam_pts(mp.mpf('0.05'), th)[:2] + [mp.mpf('0.03')*mp.expj(-th*(1 + EPS)), mp.mpf('-0.04'), mp.mpf('0.02')*mp.expj(PI/2)]:
        worst = max(worst, abs((Glit(z) - gref) - (Bd.G0(z) - Bd.G0(zref))))
    print(f"[0b] p={mp.nstr(pp,2)} d={mp.nstr(d,2)} n=4: max |(G_lit(z) - G_lit(0.05)) - (G0(z) - G0(0.05))| = {mp.nstr(worst, 3)} "
          f"(5 points, 3 at angular distance 1e-12 th from a seam)", flush=True)
    C_.check(f"[0b] representation = literal glued exponent near 0 p={mp.nstr(pp,2)} d={mp.nstr(d,2)}", float(worst), 0.0, 1e-15)


# ---------------- [1] Lemma P1 (b)-(d): n-uniform, d-uniform rates ----------------
NS = (10, 40, 160, 640)
for (pp, rads) in ((mp.mpf('0.6'), (mp.mpf('1e-3'), mp.mpf('0.03'), mp.mpf('0.3'))), (mp.mpf('0.3'), (mp.mpf('1e-3'), mp.mpf('0.03'), mp.mpf('0.3')))):
    c = mp.mpf(c_p_mp(float(pp))); th = PI*pp/2
    Z = []
    for r in rads:
        Z += seam_pts(r, th) + [r*mp.expj(th/2), r*mp.expj(PI/2), r*mp.expj(mp.mpf('0.9')*PI), -r, r*mp.expj(-mp.mpf('0.6')*PI)]
    Z += [4*c + c*mp.expj(PI/3)/4, 4*c + c*mp.expj(-2*PI/3)/4, 4*c + c/4]
    Zr = Z + [mp.mpf('0.2'), mp.mpf('1e-3')]                                    # G0 also on the band
    for (dn, dd) in (((-1, 50), (-1, 2), (-49, 50)) if pp > mp.mpf('0.5') else ((-1, 2), (-49, 50))):
        lab = f"p={mp.nstr(pp,2)} d={mp.nstr(mp.mpf(dn)/dd,3)}"
        A = {K: {} for K in (0, 1, 2)}; B = {K: {} for K in (0, 1, 2)}; A2, B2 = {}, {}
        for n in NS:
            Bd = Band(pp, dn, dd, n, c)
            for K in (0, 1, 2):
                A[K][n] = max(abs(Bd.G0(z) - sum(Bd.m[k]*z**k for k in range(1, K + 1)))/abs(z) for z in Zr)*mp.mpf(n)**((K + 1)*pp)
                B[K][n] = max(abs(Bd.Lh(z) - Rr(z, c)*Bd.MQ(K, z))/abs(Rr(z, c)) for z in Z)*mp.mpf(n)**((K + 1)*pp)
            A2[n] = A[0][n]*mp.mpf(n)**pp; B2[n] = B[0][n]*mp.mpf(n)**pp
        for K in (0, 1, 2):
            print(f"[1] {lab} K={K}: sup n^((K+1)p)|G0 - sum m_k z^k|/|z| = " + ", ".join(f"{n}:{mp.nstr(A[K][n], 4)}" for n in NS)
                  + "; sup n^((K+1)p)|L_h - R M_mu|/|R| = " + ", ".join(f"{n}:{mp.nstr(B[K][n], 4)}" for n in NS), flush=True)
            # d-free majorants of the next term (|S_k(d)| <= zeta(1+kp)): n^{(K+1)p}|m_{K+1}| <= (p/pi) Gamma((K+1)p) (2 pi)^{-(K+1)p} zeta(1+(K+1)p)
            mk1 = (pp/PI)*mp.gamma((K + 1)*pp)*(2*PI)**(-(K + 1)*pp)*mp.zeta(1 + (K + 1)*pp)
            majA = mk1*max(abs(z)**K for z in Zr)
            majB = 2*mk1*max(abs(sum(z**(K - j)*mp.binomial(2*j, j)*c**j for j in range(K + 1))) for z in Z)
            C_.check(f"[1] P1(c) below 2 x d-free next-term majorant, all n, K={K} {lab}", float(max(max(A[K].values()) - 2*majA, 0)), 0.0, 0.0)
            C_.check(f"[1] P1(c) settled in n (640 vs 160) K={K} {lab}", float(max(A[K][640]/A[K][160] - 1.25, 0)), 0.0, 0.0)
            C_.check(f"[1] P1(d) below 2 x d-free next-term majorant, all n, K={K} {lab}", float(max(max(B[K].values()) - 2*majB, 0)), 0.0, 0.0)
            C_.check(f"[1] P1(d) settled in n (640 vs 160) K={K} {lab}", float(max(B[K][640]/B[K][160] - 1.25, 0)), 0.0, 0.0)
            print(f"    K={K}: 2 x majorant {mp.nstr(2*majA, 4)} (G0), {mp.nstr(2*majB, 4)} (L_h)")
        print(f"    control n^(2p) (K=0): G0 " + ", ".join(f"{n}:{mp.nstr(A2[n], 4)}" for n in NS) + "; L_h " + ", ".join(f"{n}:{mp.nstr(B2[n], 4)}" for n in NS))
        # the control is discriminating only if the k = 1 term dominates, i.e. S_1(d) is not small (Remark P1.3)
        S1rel = abs(S_series(1, pp, dn, dd))/mp.zeta(1 + pp)
        if S1rel >= mp.mpf('0.05'):
            C_.check(f"[1] CONTROL rate n^-2p for G0 fails {lab}", float(A2[640]/A2[40] < 1.5), 0.0, 0.0)
            C_.check(f"[1] CONTROL rate n^-2p for L_h fails {lab}", float(B2[640]/B2[40] < 1.5), 0.0, 0.0)
        else:
            print(f"    control not applicable: |S_1(d)|/zeta(1+p) = {mp.nstr(S1rel, 3)} < 0.05 (m_1 small; n^-2p control not discriminating)")


# ---------------- [2]-[6] the glued parametrix ----------------
PARAMS = [(0.6, -0.5, -4, 5), (0.6, -0.6, -4, 5), (0.3, -0.3, -9, 10), (0.75, 0.3, -3, 10), (0.75, 0.6, -19, 20)]
radii = [mp.mpf(10)**(-k) for k in (2, 4, 6, 8, 10, 12)]
for (p, al, dn, dd) in PARAMS:
    Md = Model(p, al, dn, dd); c = Md.c; bp = Md.bp; th = PI*Md.p/2; thL = th/2
    tag = f"p={p} alpha={al} delta={mp.nstr(Md.de, 3)} (beta'={float(bp):+.2f})"
    angs = lambda r: seam_pts(r, th) + [r*mp.expjpi(t) for t in (mp.mpf('0.5'), mp.mpf('0.95'), mp.mpf(-0.7))] + [r*mp.expj(1.5*thL)]
    # [2] rho_nat bounded n-uniformly; n^p |log(rho/rho_mod)|/|z|^(1/2) bounded; band relation; glue
    lo, hi, dev = mp.inf, 0, {}
    for n in (10, 100, 1000):
        dv = 0
        for r in radii + [c/2]:
            for z in angs(r):
                rv = abs(Md.rho(z, n)); lo, hi = min(lo, rv), max(hi, rv)
                dv = max(dv, abs(mp.log(Md.rho(z, n)/Md.rho_mod(z)))/mp.sqrt(abs(z))*mp.mpf(n)**Md.p)
        dev[n] = dv
    print(f"[2] {tag}: |rho_nat| in [{mp.nstr(lo, 6)}, {mp.nstr(hi, 6)}] (n = 10, 100, 1000; 1e-12 <= |z| <= c/2, seams both sides); "
          f"n^p|log(rho_nat/rho_mod)|/|z|^(1/2) = " + ", ".join(f"{n}:{mp.nstr(v, 4)}" for n, v in dev.items()), flush=True)
    C_.check(f"[2] rho_nat bounded above/below {tag}", float(hi/lo < 4 and lo > mp.mpf(1)/4), 1.0, 0.0)
    C_.check(f"[2] n^p|log(rho_nat/rho_mod)|/|z|^1/2 bounded in n {tag}", float(max(dev[1000]/dev[10] - 1.5, 0)), 0.0, 0.0)
    eb = mp.mpf(10)**-25
    band = max(abs(Md.rho(x + I*eb, 100)*Md.rho(x - I*eb, 100) - 1) for x in [mp.mpf('1e-6'), mp.mpf('1e-3'), c/4])
    C_.check(f"[2] rho_nat_+ rho_nat_- = 1 on the band {tag}", float(band), 0.0, 1e-18)
    glue = 0
    for r in (mp.mpf(2), mp.mpf(3)):                  # radius-free identity; at |z| >= 2 (n = 4) e^{-l} - 1 is resolvable
        for sg in (1, -1):
            eg = mp.mpf(10)**-24       # angular offset well below the size of e^{-l} - 1 (EPS = 1e-12 gives an O(1e-12) offset error)
            zo, zi = r*mp.expj(sg*th*(1 + eg)), r*mp.expj(sg*th*(1 - eg))
            ratio = Md.rho(zo, 4)/Md.rho(zi, 4); Bn = Md.band(4)
            glue = max(glue, abs(ratio - mp.exp(-Bn.l(r, sg)))/abs(mp.exp(-Bn.l(r, sg)) - 1))
    print(f"    band: max|rho_+ rho_- - 1| = {mp.nstr(band, 3)}; glue: max |rho_out/rho_in - e^(-l_pm)|/|e^(-l_pm) - 1| = {mp.nstr(glue, 3)} (n = 4, |z| = 2, 3)")
    C_.check(f"[2] glue rho_out/rho_in = e^(-l_pm) {tag}", float(glue), 0.0, 1e-8)
    vw = [abs(Md.rho_w(r*mp.expjpi(mp.mpf(1)/2), 100)) for r in radii]
    C_.check(f"[2] CONTROL rho_w bounded-ratio test fails {tag}", float(max(vw)/min(vw) < 4), 0.0, 0.0)
    # [3] A bounded near 0 with the glued rho, no band jump
    An = max(max(nrm(Md.A(z, Md.rho(z, 100))), nrm(adj(Md.A(z, Md.rho(z, 100))))) for r in radii for z in angs(r))
    jump = max(nrm(Md.A(x + I*eb, Md.rho(x + I*eb, 100)) - Md.A(x - I*eb, Md.rho(x - I*eb, 100))) for x in [mp.mpf('1e-6'), mp.mpf('1e-3'), c/4])
    Aw = [nrm(Md.A(r*mp.expjpi(mp.mpf(1)/2), Md.rho_w(r*mp.expjpi(mp.mpf(1)/2), 100)))*mp.sqrt(r) for r in radii]
    print(f"[3] {tag}: max |A^(+-1)| (1e-12 <= |z| <= 1e-2, seams both sides, n = 100) = {mp.nstr(An, 5)}; band jump {mp.nstr(jump, 3)}; "
          f"control |z|^(1/2)|A_w| from {mp.nstr(Aw[0], 4)} to {mp.nstr(Aw[-1], 4)}", flush=True)
    C_.check(f"[3] A bounded near 0 {tag}", float(An < 50), 1.0, 0.0)
    C_.check(f"[3] A_+ = A_- on the band {tag}", float(jump), 0.0, 1e-12)
    C_.check(f"[3] CONTROL A_w removability bound fails {tag}", float(max(Aw) < 50*min(Aw)), 0.0, 0.0)
    # [4] lip match / mismatch, n-uniform
    rat, ctrl, match = [], [], 0
    for n in (10, 1000):
        Bn = Md.band(n)
        for ang in (thL, 1.2*thL):
            for sg in (1, -1):
                for r in radii[:4]:
                    z = r*mp.expj(sg*ang)
                    om = Md.DW(z, bp)**2/(z**bp*(4*c - z))*mp.exp(Bn.Lh(z))*mp.expj(sg*2*PI*Md.de)     # D_W^2 e^{+-2 pi i d}/W0
                    match = max(match, abs(mp.expj(-sg*PI*Md.al)/Md.rho(z, n)**2/om - 1))
                    rat.append(abs(om - mp.expj(-sg*PI*Md.al))/mp.sqrt(r)); ctrl.append(abs(om - mp.expj(-sg*PI*bp)))
    print(f"[4] {tag}: lip match rel.err {mp.nstr(match, 3)}; |omega_nat - e^(-+i pi alpha)|/|z|^(1/2) in [{mp.nstr(min(rat), 4)}, {mp.nstr(max(rat), 4)}]"
          f" (n = 10, 1000); control min |omega_nat - e^(-+i pi beta')| = {mp.nstr(min(ctrl), 4)}", flush=True)
    C_.check(f"[4] exact lip match {tag}", float(match), 0.0, 1e-20)
    C_.check(f"[4] lip mismatch O(|z|^1/2), n-uniform {tag}", float(max(rat) < 10), 1.0, 0.0)
    C_.check(f"[4] CONTROL omega_nat -> e^(-+i pi beta') fails {tag}", float(min(ctrl) < 1e-3), 0.0, 0.0)
    # [5] circle matching rate with the true glued rho; gauge (Lemma P5); controls
    r0 = c/2; Jg = int(mp.floor(1/Md.p))            # smallest J with (J+1)p > 1
    zs = seam_pts(r0, th) + [r0*mp.expjpi(t) for t in (mp.mpf('0.6'), mp.mpf('0.999'), mp.mpf(-0.5), mp.mpf(-0.75))]
    zs = [z for z in zs if abs(mp.arg(Md.f(z))) < PI - thL - mp.mpf('0.02')]
    assert len(zs) >= 6, len(zs)
    ns = [25, 50, 100, 200, 400]; e1, eT, eG, eM, eB = [], [], [], [], []
    for n in ns:
        a1 = t1 = g1 = m1 = b1 = 0
        for z in zs:
            r = Md.rho(z, n); P = Md.P0(z); Jm = Md.P0hat(z, n, r)*mp.inverse(P) - mp.eye(2)
            a1 = max(a1, n*nrm(Jm))
            t1 = max(t1, nrm(Jm - Md.Delta1(z, r, Md.al)/n))
            g1 = max(g1, nrm(Jm - Md.Delta1(z, Md.rho_mu(z, n, Jg), Md.al)/n))
            m1 = max(m1, nrm(Jm - Md.Delta1(z, Md.rho_mod(z), Md.al)/n))
            b1 = max(b1, nrm(Jm - Md.Delta1(z, r, bp)/n))
        e1.append(a1); eT.append(t1); eG.append(g1); eM.append(m1); eB.append(b1)
    ex = lambda e: [mp.log(e[i]/e[i + 1], 2) for i in range(len(e) - 1)]
    xT, xG, xM, xB = ex(eT), ex(eG), ex(eM), ex(eB)
    print(f"[5] {tag}, |z| = c/2, {len(zs)} pts (4 on seams): n|J-I| = " + ", ".join(mp.nstr(x, 5) for x in e1)
          + "\n    remainder exponents log2(e(n)/e(2n)): true rho_nat " + ", ".join(mp.nstr(x, 4) for x in xT)
          + f"; gauge (J={Jg}) " + ", ".join(mp.nstr(x, 4) for x in xG) + "; CONTROL band factor dropped " + ", ".join(mp.nstr(x, 4) for x in xM)
          + "; CONTROL nu=beta' " + ", ".join(mp.nstr(x, 4) for x in xB), flush=True)
    C_.check(f"[5] n|J - I| bounded uniformly in n {tag}", float(max(e1)/min(e1) < 1.5), 1.0, 0.0)
    halfint = abs(abs(Md.al) - mp.mpf(1)/2) < mp.mpf(10)**-25
    if halfint:
        print(f"    nu = 1/2: true remainders " + ", ".join(mp.nstr(x, 3) for x in eT))
        C_.check(f"[5] nu = 1/2: J = I + Delta_1^nat/n up to exponentially small {tag}", float(eT[3] < 1e-20 and eT[2] < 1e-6*eT[0]), 1.0, 0.0)
        C_.check(f"[5] P5 gauge remainder exponent >= 1 + (J+1)p - 0.1 {tag}", float(min(xG[1:]) >= 1 + (Jg + 1)*Md.p - mp.mpf('0.1')), 1.0, 0.0)
    else:
        C_.check(f"[5] remainder after Delta_1^nat/n is O(n^-2) {tag}", float(all(mp.mpf('1.9') <= x <= mp.mpf('2.15') for x in xT[1:])), 1.0, 0.0)
        C_.check(f"[5] P5 gauge remainder exponent >= min(2, 1 + (J+1)p) - 0.1 {tag}", float(min(xG[1:]) >= min(2, 1 + (Jg + 1)*Md.p) - mp.mpf('0.1')), 1.0, 0.0)
    # discriminating if the dropped-factor exponents leave the claim's window, or if the band-factor part of Delta_1 (size ~ |m_1| n^{-1-p})
    # dominates the O(n^-2) remainder at n = 400 (guard widened per Rule R review B, N-1)
    if not all(mp.mpf('1.9') <= x for x in xM[1:]) or eM[-1] > 10*eT[-1]:
        C_.check(f"[5] CONTROL band factor dropped: O(n^-2) (resp. exp. small) fails {tag}", float(all(mp.mpf('1.9') <= x for x in xM[1:])), 0.0, 0.0)
    else:
        print(f"    control (band factor dropped) not applicable: exponents >= 1.9 and e_mod/e_true at n=400 = {mp.nstr(eM[-1]/eT[-1], 3)} < 10")
    if abs(abs(bp) - abs(Md.al)) > mp.mpf(10)**-12:   # alpha enters as a float (0.3 is not exact)     # Q0 depends on nu^2 only: nu = beta' = -alpha is not a different Bessel datum
        C_.check(f"[5] CONTROL nu = beta' fails the O(n^-2) test {tag}", float(all(mp.mpf('1.9') <= x <= mp.mpf('2.15') for x in xB[1:])), 0.0, 0.0)
    else:
        print("    control nu = beta' not applicable: |beta'| = |alpha|")
    # [6] Bessel-scale size with the glued rho
    worst = 0; worst_w = []
    fp0 = abs(Md.f(mp.mpf('1e-30'))/mp.mpf('1e-30'))
    for n in (10, 100, 1000):
        for zeta_abs in (mp.mpf('1e-8'), mp.mpf('1e-4'), mp.mpf('0.1'), mp.mpf(2)):
            zabs = zeta_abs/(n**2*fp0)
            for z in [zabs*mp.expj(th*(1 - EPS)), zabs*mp.expj(-th*(1 + EPS)), zabs*mp.expjpi(mp.mpf('0.55')), zabs*mp.expjpi(mp.mpf(-0.9))]:
                zeta = n**2*Md.f(z)
                if abs(mp.arg(zeta)) > PI - thL - mp.mpf('0.02'): continue
                P = Md.P0hat(z, n, Md.rho(z, n))
                worst = max(worst, max(nrm(P), nrm(adj(P)))*abs(zeta)**(abs(Md.al)/2)/mp.sqrt(n))
                if zeta_abs == mp.mpf('1e-8'):
                    Pw = Md.P0hat(z, n, Md.rho_w(z, n))
                    worst_w.append(max(nrm(Pw), nrm(adj(Pw)))*abs(zeta)**(abs(Md.al)/2)/mp.sqrt(n))
    print(f"[6] {tag}: max |P0hat^(+-1)| |zeta|^(|alpha|/2) n^(-1/2) = {mp.nstr(worst, 5)} (seam points incl.); control (rho_w, |zeta| = 1e-8) up to {mp.nstr(max(worst_w), 4)}", flush=True)
    C_.check(f"[6] Bessel-scale bound with exponent |alpha|/2, n-uniform {tag}", float(worst < 20), 1.0, 0.0)
    C_.check(f"[6] CONTROL rho_w violates the bound {tag}", float(max(worst_w) < 20), 0.0, 0.0)
C_.finish()
