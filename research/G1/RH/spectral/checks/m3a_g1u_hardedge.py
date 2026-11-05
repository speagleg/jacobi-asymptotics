"""JZC M3a, gap 1 of Theorem H (JZC_M3a_H_G1u.md): the hard-edge comparison for the decoupled Hurwitz model
M(beta' = alpha + 2 delta, nu = alpha) (NUMERICAL, mpmath dps 40). Pure model weight W0 = z^{beta'} (4c - z) (w_n = 1, H = 1:
the band factor enters only through the bounded Holder ratio D_H^2/H, Paper 2 Lemma szego (ii), and is not what is tested here).
Objects (Paper 2 sec_6, sec_7; E_pgt1 §3; JZC_M4_proof N.6a):
  f(z) = -(pi^2/4) z a(z)^2, a the series of mu*((0,x]) = x^{1/2} a(x) (as in m4_rh4.py; E_pgt1 Lemma E.4(i));
  P0inf = Paper 2 (eq:Pinf0), M = (1/sqrt2)[[1, i], [i, 1]], Psi_alpha = KMVV (6.23) in the central sector |arg zeta| < 2pi/3
  (= [[I_a(w), (i/pi)K_a(w)], [pi i w I_a'(w), -w K_a'(w)]], w = 2 zeta^{1/2}), Phi_alpha = s3 Psi s3 e^{-2 zeta^{1/2} s3};
  D_W = (4cz/Ups)^{beta'/2} (4c(z-4c)/Ups)^{1/2} (Paper 2 Lemma szego (i)), Wt := (-z)^{beta'/2}(4c - z)^{1/2} (classical W-tilde
  with the Szego exponent beta'), rho := Wt/D_W; A := P0inf rho^{s3} M f^{s3/4}; P0hat := A (2 pi n)^{s3/2} Phi_alpha(n^2 f) rho^{-s3}.
Claims checked:
  [1] Szego exponent function: (R/2pi) int log x dx/(sqrt(x(4c-x))(z-x)) = (1/2) log(4cz/Ups) by quadrature (so D_{x^b} for any real b).
  [2] rho is bounded above and below on 1e-12 <= |z| <= c/2 for |beta'| >= 1 (G12 L2.3 generalised: rho = rho^(alpha)/G); and
      rho_+ rho_- = 1 on the band (so A has no band jump). CONTROL (must fail): rho_w := (-z)^{alpha/2}(4c-z)^{1/2}/D_W (Bessel-alpha
      W-tilde, beta' Szego function, no gauge) is unbounded.
  [3] A is analytic at 0 in the sense used (removable): |A^{+-1}| bounded as z -> 0 off the band, A_+ = A_- on the band.
      CONTROL (must fail): A_w built with rho_w violates the removability bound |z|^{1/2}|A_w| <= C.
  [4] Lip match and lip mismatch: on rays arg z = +-theta (in C_+-), omega_nat := D_W^2 e^{+-2 pi i delta}/W0 satisfies
      e^{-+ i pi alpha} rho^{-2} = omega_nat (exact lip match of P0hat), and |omega_nat - e^{-+ i pi alpha}| <= C |z|^{1/2}
      (Paper 2 Lemma lip-mismatch with rho_pm = e^{-+ i pi alpha}). CONTROL (must fail): omega_nat - e^{-+ i pi beta'} does not -> 0.
  [5] Circle matching, n-uniform: on |z| = r (central-sector points), J := P0hat P0inf^{-1} = I + Delta_1/n + O(n^-2) with
      Delta_1 = (1/(16 f^{1/2})) P0inf rho^{s3} Q0 rho^{-s3} P0inf^{-1}, Q0 = [[-(1+4 nu^2), 2i], [2i, 1+4 nu^2]], nu = alpha (Bessel order),
      for n = 25..400: n |J - I| bounded and the O(n^-2) remainder ratio e(2n)/e(n) in [0.2, 0.3].
      CONTROL (must fail): Delta_1 with the Szego exponent beta' in Q0 (nu = beta') leaves an O(1/n) remainder.
  [6] Bessel-scale size (n-uniform): |P0hat^{+-1}(z)| |zeta|^{|alpha|/2} n^{-1/2} <= C for |zeta| <= 2, n in {10, 100, 1000}
      (exponent |alpha|/2, not |beta'|/2). CONTROL (must fail): with rho_w the same quantity is unbounded.
Parameters: (p, alpha, delta) in {(1.5, -0.5, -0.8), (1.5, -0.6, -0.8), (3, -0.5, -0.8), (3, -0.3, -0.9), (1.5, 0.3, -0.3), (3, 0.6, -0.95), (0.6, -0.5, -0.8), (1.5, -0.5, 0)}:
beta' = -2.1, -2.2, -2.1, -2.1, -0.3, -1.3, -2.1, -0.5 (alpha = -1/2: Bessel order 1/2, terminating Hankel series; p = 0.6: the local analysis at 0 is p-free once f is given; delta = 0: lattice)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import mpmath as mp
from so_coeffs import c_p_mp
from spec_common import Checks
mp.mp.dps = 40
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi
s3 = mp.matrix([[1, 0], [0, -1]])
Mm = mp.matrix([[1, I], [I, 1]])/mp.sqrt(2)


def diag(a, b): return mp.matrix([[a, 0], [0, b]])
def nrm(A): return max(abs(A[i, j]) for i in range(2) for j in range(2))
def adj(A): return mp.matrix([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])     # = A^{-1} when det A = 1


class Model:
    def __init__(s, p, al, de):
        s.p, s.al, s.de = mp.mpf(p), mp.mpf(al), mp.mpf(de); s.bp = s.al + 2*s.de
        s.c = mp.mpf(c_p_mp(float(p))); c = s.c; ap = 1/s.p + mp.mpf(1)/2
        s.zc = [mp.rf(mp.mpf(1)/2, k)/mp.factorial(k)/(4*c)**k/((ap + k)*(k + mp.mpf(1)/2))*(4*c)**mp.mpf(-0.5)/(s.p*PI) for k in range(90)]

    def f(s, z):
        a = mp.polyval(s.zc[::-1], z)
        return -(PI**2/4)*z*a**2

    def P0(s, z):
        c = s.c; a = mp.exp(mp.log((z - 4*c)/z)/4)
        return mp.matrix([[(a + 1/a)/2, (a - 1/a)/(2*I)], [-(a - 1/a)/(2*I), (a + 1/a)/2]])

    def Ups(s, z): return (mp.sqrt(z) + mp.sqrt(z - 4*s.c))**2

    def DW(s, z, b):          # Szego function of x^b (4c - x): Paper 2 Lemma szego (i), principal powers
        U = s.Ups(z); c = s.c
        return (4*c*z/U)**(b/2)*(4*c*(z - 4*c)/U)**(mp.mpf(1)/2)

    def Wt(s, z, b): return (-z)**(b/2)*(4*s.c - z)**(mp.mpf(1)/2)

    def rho(s, z): return s.Wt(z, s.bp)/s.DW(z, s.bp)
    def rho_w(s, z): return s.Wt(z, s.al)/s.DW(z, s.bp)        # control: no gauge

    def A(s, z, rho=None):
        r = s.rho(z) if rho is None else rho
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

    def P0hat(s, z, n, rho=None):
        r = s.rho(z) if rho is None else rho
        n = mp.mpf(n); sq = mp.sqrt(2*PI*n)
        return s.A(z, r)*diag(sq, 1/sq)*s.Phi(n**2*s.f(z), s.al)*diag(1/r, r)

    def Delta1(s, z, nu):
        nu = mp.mpf(nu); r = s.rho(z); P = s.P0(z)
        Q0 = mp.matrix([[-(1 + 4*nu**2), 2*I], [2*I, 1 + 4*nu**2]])
        return P*diag(r, 1/r)*Q0*diag(1/r, r)*mp.inverse(P)/(16*mp.sqrt(s.f(z)))


def quad_L(c, z):
    """(R(z)/2pi) int_0^{4c} log x dx/(sqrt(x(4c-x))(z-x)), x = 2c(1 - cos t)."""
    R = z*mp.sqrt(1 - 4*c/z)
    g = lambda t: mp.log(4*c*mp.sin(t/2)**2)/(z - 4*c*mp.sin(t/2)**2) if t > 0 else mp.mpf(0)
    return R/(2*PI)*mp.quad(g, [0, PI/8, PI/2, PI])


PARAMS = [(1.5, -0.5, -0.8), (1.5, -0.6, -0.8), (3, -0.5, -0.8), (3, -0.3, -0.9), (1.5, 0.3, -0.3), (3, 0.6, -0.95), (0.6, -0.5, -0.8), (1.5, -0.5, 0)]
radii = [mp.mpf(10)**(-k) for k in (2, 4, 6, 8, 10, 12)]
args_off = [PI/3, PI/2, 3*PI/4, PI - mp.mpf('1e-3'), -PI/4, -2*PI/3, -PI + mp.mpf('1e-3')]

# ---------------- [1] the Szego exponent function, by quadrature ----------------
M0 = Model(1.5, -0.5, -0.8); c0 = M0.c
for z in [mp.mpc('-0.3', '0.01'), mp.mpc('0.2', '0.4'), mp.mpc('1e-4', '-1e-3'), 4*c0 + mp.mpc('0.5', '0.5')]:
    q = quad_L(c0, z); cl = mp.log(4*c0*z/M0.Ups(z))/2
    print(f"[1] z = {mp.nstr(z, 4)}: |quadrature - (1/2)log(4cz/Ups)| = {mp.nstr(abs(q - cl), 3)}")
    C_.check(f"[1] log D_x(z) quadrature = (1/2)log(4cz/Ups) at z={mp.nstr(z, 4)}", float(abs(q - cl)), 0.0, 1e-25)

for (p, al, de) in PARAMS:
    Md = Model(p, al, de); c = Md.c; bp = Md.bp
    tag = f"p={p} alpha={al} delta={de} (beta'={float(bp):+.2f})"
    # ---------------- [2] rho bounded, rho_+ rho_- = 1 ----------------
    vals = [abs(Md.rho(r*mp.expjpi(t/PI))) for r in radii + [c/2] for t in args_off]
    lo, hi = min(vals), max(vals)
    print(f"[2] {tag}: |rho| in [{mp.nstr(lo, 6)}, {mp.nstr(hi, 6)}] on 1e-12 <= |z| <= c/2", flush=True)
    C_.check(f"[2] rho bounded above/below {tag}", float(hi/lo < 4 and lo > mp.mpf(1)/4), 1.0, 0.0)
    eps = mp.mpf('1e-30')
    band = max(abs(Md.rho(x + I*eps)*Md.rho(x - I*eps) - 1) for x in [mp.mpf('1e-9'), mp.mpf('1e-4'), c/4])
    C_.check(f"[2] rho_+ rho_- = 1 on the band {tag}", float(band), 0.0, 1e-20)
    if de != 0:
        vw = [abs(Md.rho_w(r*mp.expjpi(mp.mpf(1)/2)))*r**de for r in radii]       # |rho_w| ~ |z|^{-delta}
        fails = max(abs(Md.rho_w(r*mp.expjpi(mp.mpf(1)/2))) for r in radii)/min(abs(Md.rho_w(r*mp.expjpi(mp.mpf(1)/2))) for r in radii) < 4
        print(f"    control rho_w: |rho_w| |z|^delta in [{mp.nstr(min(vw), 4)}, {mp.nstr(max(vw), 4)}] (|rho_w| ~ |z|^(-delta): unbounded ratio)")
        C_.check(f"[2] CONTROL rho_w bounded-ratio test fails {tag}", float(fails), 0.0, 0.0)
    # ---------------- [3] A removable: bounded at 0, no band jump ----------------
    An = [max(nrm(Md.A(r*mp.expjpi(t/PI))), nrm(mp.inverse(Md.A(r*mp.expjpi(t/PI))))) for r in radii for t in args_off]
    print(f"[3] {tag}: max |A^(+-1)| over 1e-12 <= |z| <= 1e-2 = {mp.nstr(max(An), 6)}")
    C_.check(f"[3] A bounded near 0 {tag}", float(max(An) < 50), 1.0, 0.0)
    jump = max(nrm(Md.A(x + I*eps) - Md.A(x - I*eps)) for x in [mp.mpf('1e-9'), mp.mpf('1e-4'), c/4])
    C_.check(f"[3] A_+ = A_- on the band {tag}", float(jump), 0.0, 1e-12)
    if de != 0:
        Aw = [nrm(Md.A(r*mp.expjpi(mp.mpf(1)/2), Md.rho_w(r*mp.expjpi(mp.mpf(1)/2))))*mp.sqrt(r) for r in radii]
        bounded = max(Aw) < 50*min(Aw)
        print(f"    control A_w: |z|^(1/2)|A_w| from {mp.nstr(Aw[0], 4)} (|z|=1e-2) to {mp.nstr(Aw[-1], 4)} (|z|=1e-12)")
        C_.check(f"[3] CONTROL A_w removability bound fails {tag}", float(bounded), 0.0, 0.0)
    # ---------------- [4] lip match and lip mismatch ----------------
    worst_match = 0; ratios = []; ctrl = []
    for th in (PI/3, PI/4):
        for sg in (1, -1):
            for r in radii:
                z = r*mp.expj(sg*th)
                om = Md.DW(z, bp)**2*mp.expj(sg*2*PI*de)/(z**bp*(4*c - z))
                worst_match = max(worst_match, abs(mp.expj(-sg*PI*al)/Md.rho(z)**2/om - 1))
                ratios.append(abs(om - mp.expj(-sg*PI*al))/mp.sqrt(r))
                ctrl.append(abs(om - mp.expj(-sg*PI*bp)))
    print(f"[4] {tag}: lip match rel.err {mp.nstr(worst_match, 3)}; |omega - rho_pm|/|z|^(1/2) in [{mp.nstr(min(ratios), 4)}, {mp.nstr(max(ratios), 4)}];"
          f" control min |omega - e^(-+i pi beta')| = {mp.nstr(min(ctrl), 4)}")
    C_.check(f"[4] exact lip match e^(-+i pi alpha) rho^-2 = omega_nat {tag}", float(worst_match), 0.0, 1e-25)
    C_.check(f"[4] lip mismatch O(|z|^1/2) {tag}", float(max(ratios) < 10), 1.0, 0.0)
    if de != 0:
        C_.check(f"[4] CONTROL omega_nat -> e^(-+i pi beta') fails {tag}", float(min(ctrl) < 1e-3), 0.0, 0.0)
    # ---------------- [5] circle matching ----------------
    r0 = c/2
    zs = [r0*mp.expjpi(t) for t in (mp.mpf('0.45'), mp.mpf('0.6'), mp.mpf('0.8'), mp.mpf('0.999'), mp.mpf(-0.5), mp.mpf(-0.75))]
    zs = [z for z in zs if abs(mp.arg(Md.f(z))) < 2*PI/3 - mp.mpf('0.05')]
    assert len(zs) >= 4, len(zs)
    e1, e2, e2w = [], [], []
    ns = [25, 50, 100, 200, 400]
    for n in ns:
        a1 = b1 = b2 = 0
        for z in zs:
            J = Md.P0hat(z, n)*mp.inverse(Md.P0(z)); Id = mp.eye(2)
            a1 = max(a1, n*nrm(J - Id))
            b1 = max(b1, nrm(J - Id - Md.Delta1(z, al)/n))
            b2 = max(b2, nrm(J - Id - Md.Delta1(z, bp)/n))
        e1.append(a1); e2.append(b1); e2w.append(b2)
    rat = [e2[i + 1]/e2[i] for i in range(len(ns) - 1)]
    ratw = [e2w[i + 1]/e2w[i] for i in range(len(ns) - 1)]
    print(f"[5] {tag}, |z| = c/2, {len(zs)} pts: n|J-I| = " + ", ".join(mp.nstr(x, 5) for x in e1)
          + "; e(2n)/e(n) = " + ", ".join(mp.nstr(x, 4) for x in rat) + "; control (nu = beta') ratios " + ", ".join(mp.nstr(x, 4) for x in ratw))
    C_.check(f"[5] n|J - I| bounded uniformly in n {tag}", float(max(e1)/min(e1) < 1.5), 1.0, 0.0)
    if abs(abs(Md.al) - mp.mpf(1)/2) < mp.mpf(10)**-30:
        # nu = +-1/2: the Hankel expansion terminates (a_k(1/2) = 0 for k >= 1, b_k = 0 for k >= 2), so J = I + Delta_1/n + O(e^{-cn})
        print(f"    nu = +-1/2: remainders " + ", ".join(mp.nstr(x, 3) for x in e2))
        C_.check(f"[5] nu = 1/2: J = I + Delta_1/n up to exponentially small {tag}", float(max(e2[3:]) < 1e-30 and e2[2] < 1e-6*e2[0]), 1.0, 0.0)
    else:
        C_.check(f"[5] remainder after Delta_1/n is O(n^-2) {tag}", float(all(mp.mpf('0.2') <= x <= mp.mpf('0.3') for x in rat[1:])), 1.0, 0.0)
    if abs(bp) != abs(al):
        C_.check(f"[5] CONTROL Delta_1 with nu = beta' fails the O(n^-2) test {tag}", float(all(mp.mpf('0.2') <= x <= mp.mpf('0.3') for x in ratw[1:])), 0.0, 0.0)
    # ---------------- [6] Bessel-scale size ----------------
    worst = 0; worst_w = []
    for n in (10, 100, 1000):
        for zeta_abs in (mp.mpf('1e-8'), mp.mpf('1e-4'), mp.mpf('0.1'), mp.mpf(2)):
            for t in (mp.mpf('0.55'), mp.mpf('0.9'), mp.mpf(-0.7)):
                # solve |n^2 f(z)| = zeta_abs approximately via the linear term (f'(0) < 0): |z| ~ zeta_abs/(n^2 |f'(0)|)
                z = zeta_abs/(n**2*abs(Md.f(mp.mpf('1e-30'))/mp.mpf('1e-30')))*mp.expjpi(t)
                zeta = n**2*Md.f(z)
                if abs(mp.arg(zeta)) > 2*PI/3 - mp.mpf('0.05'): continue
                P = Md.P0hat(z, n)
                q = max(nrm(P), nrm(adj(P)))*abs(zeta)**(abs(al)/2)/mp.sqrt(n)
                worst = max(worst, q)
                if de != 0 and zeta_abs == mp.mpf('1e-8'):
                    Pw = Md.P0hat(z, n, Md.rho_w(z))
                    worst_w.append(max(nrm(Pw), nrm(adj(Pw)))*abs(zeta)**(abs(al)/2)/mp.sqrt(n))
    print(f"[6] {tag}: max |P0hat^(+-1)| |zeta|^(|alpha|/2) n^(-1/2) = {mp.nstr(worst, 5)}"
          + (f"; control (rho_w, |zeta| = 1e-8) up to {mp.nstr(max(worst_w), 4)}" if worst_w else ""), flush=True)
    C_.check(f"[6] Bessel-scale bound with exponent |alpha|/2, n-uniform {tag}", float(worst < 20), 1.0, 0.0)
    if worst_w:
        C_.check(f"[6] CONTROL rho_w violates the bound {tag}", float(max(worst_w) < 20), 0.0, 0.0)
C_.finish()
