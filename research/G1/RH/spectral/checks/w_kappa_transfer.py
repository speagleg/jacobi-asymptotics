"""JZC_W_kappa §4, Lemma K.11 (NUMERICAL, mpmath dps 24): transfer of the band-factor gauge (JZC_M3a_H_Hc.md Lemma Hc.3, step 2)
to the composite band factor of the kappa-family lam_k = (k + d)^p + kappa, p > 1, against the coherent BT model.
  log H_n^kappa(z) = -2 G_d(zeta(z)) + (1/p - 2a) log(1 - z/zs) - 2 pi cot(pi/p) rho1(z) + const     (Cor K.1, exact for |z| < |zs|)
  log h_BT(z)      = -P_mu(z) + sum_{m <= M} tau_m (z/n^p)^{q_m},   tau_m = -2 pi cot(pi/p) a_m,  a_m = -binom(1/p, m)(-kappa)^m,
  mu_j = 2 sum_{k<=j} m_k(d) binom(j-1, k-1)(kappa/n^p)^{j-k} + (1/p - 2a)(kappa/n^p)^j/j        (= (2Z_kappa(-j)/j - B_j) n^{-jp},
                                                                                                     P W-out.5(i), Fourier-sum form)
  E := log H_n^kappa - log h_BT,  T(z) := (R(z)/pi) int_0^{4c} (E(x) - E(z)) dx/(sqrt(x(4c-x))(z - x))    (Paper 2 (eq:szego-repr)).
Claim (Lemma K.11): sup over the two circles |T| = O(n^{-(J+1)p}) for M >= J + 1, and the hard-edge lip tail
sup_{|z| = delta_r} |rho1 - sum_{m<=M} a_m (z/n^p)^{q_m}| = O(n^{1 - p(M+1)}); then rho_kappa = rho_BT e^{-/+ i pi tail - T/2},
(-omega_kappa)^{1/2} = (-omega_BT)^{1/2} e^{T/2} and Delta_k^kappa = Delta_k^BT + O(n^{-(J+1)p}) on both circles.
G_d(w) - G_d(1) by (E.2.1)_d (JZC_M3a_H_Hc.md Lemma Hc.1 (b); same code as m3a_hc_gauge.py), m_k(d) by the Fourier sums of Hc.2 (i).
Asserted: [Q] Gauss-Chebyshev N = 16 vs 48 converged; [T] exponent of sup|T| (last doubling n = 16 -> 32) within 0.35 of (J+1)p
(J = 1, 2; M = J + 1), and n^{(J+1)p} sup|T| bounded; [L] exponent of the lip tail within 0.1 of p(M+1) - 1;
[T0] (Prop K.12 (iii)) against M(beta', alpha) itself (no branched terms, Toda mu_1 only) sup|T| = O(n^{1-p}): exponent within 0.1
of p - 1 (the same numbers as control C1).
CONTROLS (must fail): [C1] M = 0 (the model M(beta', alpha) with Toda times only, i.e. Hc.3 verbatim): exponent ~ p - 1;
[C2] Toda parameters without the gauge share 2 zeta(0,a) kappa^j n^{-jp}/j: exponent ~ p (J = 1; asserted only where zeta(0, a) != 0:
at d = -1/2 the share vanishes and the first run's C2 'failure to fail' at p = 1.25, d = -0.5 was this degeneracy, Rule A item 3); [C3] Hurwitz moments not
re-expanded through the Moebius map (mu_j = 2 m_j + density + gauge): exponent ~ 2p (J = 2)."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from math import comb
from spec_common import Checks
mp.mp.dps = 24
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi; HALF = mp.mpf(1)/2; T0 = time.time()


def cp(p): Ip = mp.sqrt(PI)/2*mp.gamma(1/p + HALF)/mp.gamma(1/p + 1); return (PI/(2*Ip))**p/4
def S(k, p, d, Q=20):
    assert abs(Q*d - mp.nint(Q*d)) < mp.mpf(10)**-20
    A = PI*k*p/2; s = 1 + k*p
    return Q**(-s)*mp.fsum(mp.sin(A - 2*PI*j*d)*mp.zeta(s, mp.mpf(j)/Q) for j in range(1, Q + 1))
def mhat(k, p, d): return -(p/PI)*mp.gamma(k*p)*(2*PI)**(-k*p)*S(k, p, d)
def Rf(z, c): return z*mp.sqrt(1 - 4*c/z)
def logm(t, d):
    ex = -2*PI*I*(t - d)
    return mp.log(-mp.expm1(ex)) if mp.re(ex) > -5000 else mp.mpc(0)
def G_pgt1(z, n, p, d):    # Lemma Hc.1 (b): G_d(z) - G_d(1)
    f = lambda u: 2*mp.im(logm(n*mp.e**(-u/p)*mp.expjpi(-1/p), d))*(z - 1)/((-mp.e**u - z)*(-mp.e**u - 1))*mp.e**u
    L = mp.log(abs(z)); pts = sorted(set([mp.mpf(-60), mp.mpf(-10), mp.mpf(0), L - 2, L, L + 2, mp.mpf(30), mp.mpf(300)]))
    return mp.quad(f, pts)/(2*PI)


CASES = [(mp.mpf(3)/2, mp.mpf('-0.3'), mp.mpf('0.5')), (mp.mpf(3)/2, mp.mpf('-0.3'), mp.mpf('-0.3')),
         (mp.mpf(3), mp.mpf('-0.7'), mp.mpf(1)), (mp.mpf(5)/4, mp.mpf('-0.5'), mp.mpf('0.4'))]
NS = [mp.mpf(8), mp.mpf(16), mp.mpf(32)]
NQ = 48
for p, d, kap in CASES:
    c = cp(p); a = 1 + d; lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,2)} kappa={mp.nstr(kap,2)}"
    xs = [2*c*(1 - mp.cos((2*j - 1)*PI/(2*NQ))) for j in range(1, NQ + 1)]
    hard = [c/4*mp.expjpi(f) for f in (mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.95'), mp.mpf('-0.6'))]
    circ = hard + [4*c + c/4*mp.expjpi(f) for f in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('-0.7'))]
    mh = {k: mhat(k, p, d) for k in (1, 2, 3)}
    gam = 1/p - 2*a
    keys = ('J1', 'J2', 'C1', 'C2', 'C3'); sups = {k_: [] for k_ in keys}; ltail = {1: [], 2: []}; qerr = 0
    for n in NS:
        zs = n**p/kap; kn = kap/n**p
        zeta = lambda z: z/(1 - z/zs)
        am = {m: -mp.binomial(1/p, m)*(-kap)**m for m in range(1, 6)}
        qm = {m: m - 1/p for m in range(1, 6)}
        def rho1z(z): return -n*mp.power(z, -1/p)*mp.expm1(mp.log(1 - z/zs)/p)
        def tail(z, M): return rho1z(z) - sum(am[m]*mp.power(z/n**p, qm[m]) for m in range(1, M + 1))
        def mus(J, gauge_share=True, reexpand=True):
            out = {}
            for j in range(1, J + 1):
                hur = 2*sum(mh[k]*n**(-k*p)*comb(j - 1, k - 1)*kn**(j - k) for k in range(1, j + 1)) if reexpand else 2*mh[j]*n**(-j*p)
                g = gam if gauge_share else gam - 2*mp.zeta(0, a)
                out[j] = hur + g*kn**j/j
            return out
        Gx = [G_pgt1(zeta(x), n, p, d) for x in xs]; Gz = [G_pgt1(zeta(z), n, p, d) for z in circ]
        def Efun(z, Gv, mu, M):
            return (-2*Gv + gam*mp.log(1 - z/zs) - 2*PI*mp.cot(PI/p)*tail(z, M) + sum(m_*z**j for j, m_ in mu.items()))
        variants = {'J1': (mus(1), 2), 'J2': (mus(2), 3), 'C1': (mus(1), 0), 'C2': (mus(1, gauge_share=False), 2),
                    'C3': (mus(2, reexpand=False), 3)}
        for key, (mu, M) in variants.items():
            Ex = [Efun(x, g, mu, M) for x, g in zip(xs, Gx)]
            def T(z, Ez, idx):
                return Rf(z, c)*mp.fsum((Ex[i] - Ez)/(z - xs[i]) for i in idx)/len(idx)
            vals = []
            for z, g in zip(circ, Gz):
                Ez = Efun(z, g, mu, M); tf = T(z, Ez, range(NQ)); vals.append(abs(tf))
                if key in ('J1', 'J2'):
                    qerr = max(qerr, abs(tf - T(z, Ez, range(1, NQ, 3)))/max(abs(tf), mp.mpf(10)**-40))
            sups[key].append(max(vals))
        for J in (1, 2): ltail[J].append(max(abs(tail(z, J + 1)) for z in hard))
        print(f"  {lab} n={int(n)}: sup|T| J1 {mp.nstr(sups['J1'][-1], 4)}, J2 {mp.nstr(sups['J2'][-1], 4)}, C1 {mp.nstr(sups['C1'][-1], 4)}, "
              f"C2 {mp.nstr(sups['C2'][-1], 4)}, C3 {mp.nstr(sups['C3'][-1], 4)}  (t {time.time() - T0:.0f}s)", flush=True)
    ex = {k_: mp.log(v[-2]/v[-1], 2) for k_, v in sups.items()}
    exl = {J: mp.log(ltail[J][-2]/ltail[J][-1], 2) for J in (1, 2)}
    print(f"{lab}: exponents (n = 16 -> 32): " + ", ".join(f"{k_} {mp.nstr(v, 4)}" for k_, v in ex.items())
          + f";  lip tail M = 2, 3: {mp.nstr(exl[1], 4)}, {mp.nstr(exl[2], 4)};  quadrature N=16 vs 48 rel. {mp.nstr(qerr, 3)}", flush=True)
    C_.check(f"[Q] Gauss-Chebyshev converged {lab}", float(qerr), 0.0, 1e-3)
    for J, key in ((1, 'J1'), (2, 'J2')):
        tgt = (J + 1)*p
        C_.check(f"[T] exponent (J+1)p {lab} J={J}", float(ex[key]), float(tgt), 0.35)
        C_.check(f"[T] n^((J+1)p) sup|T| bounded {lab} J={J}",
                 float(max(sups[key][-1]*NS[-1]**tgt/(sups[key][-2]*NS[-2]**tgt) - 2, 0)), 0.0, 0.0)
        C_.check(f"[L] lip tail exponent p(M+1) - 1 {lab} M={J+1}", float(exl[J]), float(p*(J + 2) - 1), 0.1)
    C_.check(f"[C1] CONTROL M = 0 (Hc.3 verbatim, no branched terms): exponent 2p fails {lab}", float(abs(ex['C1'] - 2*p) <= 0.35), 0.0, 0.0)
    # Prop K.12 (iii): against M(beta', alpha) itself the circle data differ by O(n^{1-p}) (the C1 variant, J = 1: the Toda part is
    # O(n^{-p}), smaller): exponent p - 1
    C_.check(f"[T0] comparison with M(beta', alpha): sup|T| = O(n^(1-p)) {lab}", float(ex['C1']), float(p - 1), 0.1)
    if abs(mp.zeta(0, a)) > mp.mpf('1e-20'):   # zeta(0, a) = 1/2 - a = 0 at d = -1/2: the gauge share vanishes, the control is degenerate
        C_.check(f"[C2] CONTROL no gauge share in mu: exponent 2p fails {lab}", float(abs(ex['C2'] - 2*p) <= 0.35), 0.0, 0.0)
    C_.check(f"[C3] CONTROL Hurwitz moments not re-expanded: exponent 3p fails {lab}", float(abs(ex['C3'] - 3*p) <= 0.35), 0.0, 0.0)
print(f"total time {time.time() - T0:.0f}s")
C_.finish()
