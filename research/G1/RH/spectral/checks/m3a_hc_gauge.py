"""JZC M3a, step H-c (JZC_M3a_H_Hc.md Lemma Hc.3 (p > 1) and Hc.4 (p < 1)): the band-factor gauge on the two circles (NUMERICAL, mpmath dps 24).
The gauge lemma reduces to one scalar statement (Hc.3, proof step 2): with h := H_n^d/H_n^d(1) on the band, mu_k := 2 m_k(d) (Fourier-sum
moments, Lemma Hc.2 (i)), M_mu(z) := sum_k mu_k Q_k(z), Q_k(z) := sum_{j<k} z^{k-1-j} C(2j,j) c^j (E3 Lemma E3.4), R(z) := (z(z-4c))^{1/2}
(~ z at infinity, cut [0,4c]) and log h(z) := the value at z of the continuation used in rho / (-omega)^{1/2} (G1u L1; sector-wise for p < 1):
  T_J(z) := [log D_h(z)^2 - log h(z)] - R(z) M_{mu^{(J)}}(z),   mu^{(J)} := (mu_1, ..., mu_J),
  log D_h(z)^2 - log h(z) = (R(z)/pi) int_0^{4c} (log h(x) - log h(z)) dx/(sqrt(x(4c-x))(z - x))       (Paper 2 (eq:szego-repr), any number c),
evaluated by Gauss-Chebyshev quadrature (exact for the polynomial part; error estimated by N = 16 vs 48 nested nodes).
Claim (Hc.3 step 2 / Hc.4): sup over the circles |T_J| = O(n^{-(J+1)p}); then omega/omega^{mu} = e^{T_J}, rho/rho^{mu} = e^{-T_J/2}, and
Delta_k = G_mu Delta_k^{mod} G_mu^{-1} + O(n^{-(J+1)p}).
log h is computed from the jump representation: p > 1: G_d(z) - G_d(1) = (1/2pi) int_{-oo}^0 e_d(y)(z-1)/((y-z)(y-1)) dy (Lemma Hc.1 (b),
checked against the construction in m3a_hc_pgt1 [2]); p < 1: (F.1_d) with the complex seam densities l_pm (JZC_M3a_H_G23plt1.md, checked
against G3's construction in m3a_g23_F1 [G]; NOT this note's lemma). log h = -2(G_d - G_d(1)).
Circles: |z| = c/4 (hard edge) and |z - 4c| = c/4 (soft edge); points next to the negative axis (p > 1) resp. on both sides of the seam
arg z = pi p/2 (p < 1, angular distance 1e-6) included.
Asserted:
  [Q] quadrature error (N = 16 vs N = 48) < 1e-3 sup|T_J| (so the decay below is not quadrature noise);
  [T] sup|T_J| n^{(J+1)p} bounded and the fitted exponent log2(sup|T_J|(n)/sup|T_J|(2n)) is within 0.35 of (J+1)p for the last doubling
      (J = 1, 2; n = 8, 16, 32; p < 1: also 64);
  CONTROLS (must fail, asserted as failures):
  [C1] no gauge (mu = 0, i.e. "omega/omega^mod = 1 + O(n^{-2p})"): exponent within 0.35 of 2p fails (it is ~ p);
  [C2] lattice moments m_k(0) for d != 0: exponent within 0.35 of (J+1)p fails at J = 1."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from math import comb
from spec_common import Checks
mp.mp.dps = 24
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi


def cp(p): Ip = mp.sqrt(PI)/2*mp.gamma(1/p + mp.mpf(1)/2)/mp.gamma(1/p + 1); return (PI/(2*Ip))**p/4
def S(k, p, d, Q=20):
    """S_k(d) = sum_m sin(pi k p/2 - 2 pi m d)/m^{1+kp} by residue classes mod Q (Q d in Z): sum_{m = j mod Q} m^{-s} = Q^{-s} zeta(s, j/Q),
    the Hurwitz series (DLMF 25.11.1 as a definition, s > 1; mpmath zeta(s, a) with 0 < a <= 1 is accurate there). mp.nsum was used
    first and is inaccurate here (relative errors up to 1e-6 for non-oscillating terms): Rule A item 11."""
    assert abs(Q*d - mp.nint(Q*d)) < mp.mpf(10)**-20
    A = PI*k*p/2; s = 1 + k*p
    return Q**(-s)*mp.fsum(mp.sin(A - 2*PI*j*d)*mp.zeta(s, mp.mpf(j)/Q) for j in range(1, Q + 1))
def mhat(k, p, d): return -(p/PI)*mp.gamma(k*p)*(2*PI)**(-k*p)*S(k, p, d)
def Rf(z, c): return z*mp.sqrt(1 - 4*c/z)


def logm(t, d):
    ex = -2*PI*I*(t - d)
    return mp.log(-mp.expm1(ex)) if mp.re(ex) > -5000 else mp.mpc(0)


def G_pgt1(z, n, p, d):    # Lemma Hc.1 (b)
    f = lambda u: 2*mp.im(logm(n*mp.e**(-u/p)*mp.expjpi(-1/p), d))*(z - 1)/((-mp.e**u - z)*(-mp.e**u - 1))*mp.e**u
    L = mp.log(abs(z)); pts = sorted(set([mp.mpf(-60), mp.mpf(-10), mp.mpf(0), L - 2, L, L + 2, mp.mpf(30), mp.mpf(300)]))
    return mp.quad(f, pts)/(2*PI)


def G_plt1(z, n, p, d):    # (F.1_d), G23plt1; theta = pi p/2
    th = PI*p/2
    def lpm(r, s):
        ex = -2*PI*n*r**(-1/p)
        if ex < -5000: return mp.mpc(0)             # |l_pm| <= 2|w| < 1e-2000: below working precision
        w = mp.exp(s*2*PI*I*d)*mp.exp(ex); return -mp.log(1 - w)
    Kf = lambda zeta: (z - 1)/((zeta - z)*(zeta - 1))
    f = lambda u: (lpm(mp.e**u, 1)*mp.expj(th)*Kf(mp.e**u*mp.expj(th)) - lpm(mp.e**u, -1)*mp.expj(-th)*Kf(mp.e**u*mp.expj(-th)))*mp.e**u
    L = mp.log(abs(z)); pts = sorted(set([mp.mpf(-60), mp.mpf(-10), mp.mpf(0), L - 2, L, L + 2, mp.mpf(30), mp.mpf(300)]))
    return mp.quad(f, pts)/(2*PI*I)


def Qk(k, z, c): return sum(z**(k - 1 - j)*comb(2*j, j)*c**j for j in range(k))


CASES = [(mp.mpf(3)/2, mp.mpf('-0.7'), G_pgt1), (mp.mpf(3), mp.mpf('-0.3'), G_pgt1), (mp.mpf(5)/4, mp.mpf(0), G_pgt1),
         (mp.mpf('0.6'), mp.mpf('-0.5'), G_plt1), (mp.mpf('0.75'), mp.mpf('-0.3'), G_plt1)]
NS1 = [mp.mpf(8), mp.mpf(16), mp.mpf(32)]
NS0 = NS1 + [mp.mpf(64)]   # p < 1: one more doubling (pre-asymptotics at d = -1/2, where mhat_3 = 0.0018 and mhat_4 = -0.0016 nearly cancel)
NQ = 48
for p, d, Gf in CASES:
    NS = NS1 if p > 1 else NS0
    c = cp(p); lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,2)}"
    xs = [2*c*(1 - mp.cos((2*j - 1)*PI/(2*NQ))) for j in range(1, NQ + 1)]     # nodes of N = 48; every 3rd (j = 2, 5, ...) is N = 16
    if p > 1:
        circ = [c/4*mp.expjpi(f) for f in (mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.95'), mp.mpf('-0.6'))]
    else:
        circ = [c/4*mp.expjpi(f) for f in (mp.mpf('0.2')*p, p/2 - mp.mpf('1e-6'), p/2 + mp.mpf('1e-6'), mp.mpf('0.95'), -p/2 - mp.mpf('1e-6'))]
    circ += [4*c + c/4*mp.expjpi(f) for f in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('-0.7'))]
    mh = {k: mhat(k, p, d) for k in (1, 2, 3)}; mh0 = {k: mhat(k, p, mp.mpf(0)) for k in (1, 2, 3)}
    sups = {key: [] for key in ('J1', 'J2', 'mod', 'lat')}; qerr = 0
    for n in NS:
        cx = [-2*Gf(x, n, p, d) for x in xs]; cz = [-2*Gf(z, n, p, d) for z in circ]
        def T(z, czv, mus, idx):
            nodes = [(xs[i], cx[i]) for i in idx]
            return Rf(z, c)*mp.fsum((cxv - czv)/(z - x) for x, cxv in nodes)/len(nodes) - Rf(z, c)*sum(mu*Qk(k, z, c) for k, mu in mus.items())
        mus = {k: 2*mh[k]*n**(-k*p) for k in (1, 2)}; mus0 = {k: 2*mh0[k]*n**(-k*p) for k in (1, 2)}
        full = range(NQ); sub = range(1, NQ, 3)
        for key, mu in (('J1', {1: mus[1]}), ('J2', mus), ('mod', {}), ('lat', {1: mus0[1]})):
            vals = [abs(T(z, czv, mu, full)) for z, czv in zip(circ, cz)]
            sups[key].append(max(vals))
            if key in ('J1', 'J2'):
                qerr = max(qerr, max(abs(T(z, czv, mu, full) - T(z, czv, mu, sub)) for z, czv in zip(circ, cz))/max(vals))
    ex = {key: mp.log(v[-2]/v[-1], 2) for key, v in sups.items()}
    print(f"{lab}: sup|T| over {len(circ)} circle points, n = {[int(x) for x in NS]}:")
    for key in sups: print(f"   {key:4s}: {[mp.nstr(v, 4) for v in sups[key]]}  exponent (last doubling) {mp.nstr(ex[key], 4)}")
    print(f"   quadrature N=16 vs N=48, max relative: {mp.nstr(qerr, 3)}")
    C_.check(f"[Q] Gauss-Chebyshev converged {lab}", float(qerr), 0.0, 1e-3)
    for J, key in ((1, 'J1'), (2, 'J2')):
        tgt = (J + 1)*p
        if J == 2 and abs(mh[3]) < mp.mpf(10)**-12: tgt = 4*p
        C_.check(f"[T] exponent (J+1)p {lab} J={J}", float(ex[key]), float(tgt), 0.35)
        C_.check(f"[T] n^((J+1)p) sup|T| bounded (ratio 16->32 vs 8->16 <= 2) {lab} J={J}",
                 float(max(sups[key][-1]*NS[-1]**tgt/(sups[key][-2]*NS[-2]**tgt) - 2, 0)), 0.0, 0.0)
    C_.check(f"[C1] CONTROL no gauge: exponent 2p fails {lab}", float(abs(ex['mod'] - 2*p) <= 0.35), 0.0, 0.0)
    if d != 0:
        C_.check(f"[C2] CONTROL lattice moments: exponent 2p fails {lab}", float(abs(ex['lat'] - 2*p) <= 0.35), 0.0, 0.0)
C_.finish()
