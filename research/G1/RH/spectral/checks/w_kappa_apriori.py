"""JZC_W_kappa §2 (NUMERICAL, mpmath dps 30): the a-priori bound H-b' for the kappa-family lam_k = (k + d)^p + kappa, p > 1, n fixed.
sigma = sum_k lam_k^{-s/p} delta_{1/lam_k}; alpha = (s - 1 - p)/p.  Moments m_j = Z(s/p + j), Z(w) := sum_k lam_k^{-w}, evaluated as
  sum_{k < K0} lam_k^{-w} + sum_{l >= 0} binom(-w, l) kappa^l zeta_H(p(w + l), K0 + a)      (JZC_W_outer (1.2); |kappa| < (K0 + a)^p),
with zeta_H by Euler-Maclaurin with exact derivatives (hz, as in m3a_g12_apriori.py). Monic OPs pi_n, pi_{n-1} from the Hankel system.
U_{j2}(z) := sum_k w_k pi_j(x_k)/(zeta - x_k), zeta = z n^-p, x_k = 1/lam_k (Paper 2 (eq:U-sum) up to constants that cancel below):
direct sum for k < M0 and, for x_k <= |zeta|/64, 1/(zeta - x) = (1/zeta) sum_r (x/zeta)^r with the tails sum_{k >= M0} lam_k^{-sigma} by the
same binomial/Hurwitz expansion. (kappa > -a^p is required: the case (3, 2.5, -0.9) uses kappa = -0.0005 > -0.1^3.)
Run history (Rule A item 13 of JZC_W_kappa.md): run 1 used |z| down to 1e-4 at p = 3/2 (exponents -0.55, -0.53, -0.08 vs -0.5, -0.5, 0:
pre-asymptotic, outside the declared tolerance 0.02) and an inadmissible kappa = -0.05 < -a^p at d = -0.9 (lam_1 < 0; crashed). Run 2 adds
|z| = 1e-6 at p = 3/2 (same tolerance) and kappa = -0.0005. A cross-validation of U_{j2} with two (M0, R) choices (|zeta|/4, R = 70 vs |zeta|/64,
R = 24) agreed to all 30 digits at p = 3/2, |z| = 1e-2 (scratch test, not part of this script).
Claims checked:
  [SB]  Lemma K.2: |U_{j2}(z)| <= I1^kappa(z) := (M/sin phi1)[sum_{lam_k <= T^p} lam_k^{1 - s/p} + T^p sum_{lam_k > T^p} lam_k^{-s/p}],
        T = n|z|^{-1/p}, phi1 = pi/6, M = max_{[0, x_1]} |pi_j| (sampled), for |z| in {1, 1e-2, 1e-4, 1e-6, (1e-8 at p = 3)},
        arg z in {pi/6, pi/2, pi}; and the exponent of |U_{j2}(iy)| at the two smallest radii is min(alpha, 0): kappa- and d-free.
        Control (must fail): the exponent alpha + 2d.
  [AR]  Lemma K.3: on arcs |s| = r with t_kappa(r) in d + N + 1/2 (t_kappa(z) = (n^p/z - kappa)^{1/p}), |arg s| <= pi/3:
        |e^{2 pi i (t_kappa(s) - d)} - 1| >= 2 e^{-pi/4} sin(3 pi/8) (Paper 2 L lenssector (4)'s constant). Control (must fail): arcs
        chosen with the lattice t(r) = n r^{-1/p} in d + N + 1/2 at a large kappa (the phase offset rho1(r) ~ 1/2 there)."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 30
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi; T0 = time.time()


def hz(sig, b, J=30):
    tot = mp.mpf(0)
    while b < max(60, sig): tot += b**(-sig); b += 1
    tot += b**(1 - sig)/(sig - 1) + b**(-sig)/2
    return tot + sum(mp.bernoulli(2*j)/mp.factorial(2*j)*mp.rf(sig, 2*j - 1)*b**(-sig - 2*j + 1) for j in range(1, J + 1))


_TZ = {}
def tailZ(sig, M0, p, d, kap, L=None):
    """sum_{k >= M0} ((k + d)^p + kappa)^{-sig}, M0 >= 1, via the binomial expansion (|kappa|/(M0 + d)^p <= 1/2 required); memoised."""
    key = (sig, M0, p, d, kap)
    if key not in _TZ: _TZ[key] = _tailZ(sig, M0, p, d, kap, L)
    return _TZ[key]
def _tailZ(sig, M0, p, d, kap, L=None):
    b = M0 + d; rr = abs(kap)/b**p; assert rr <= mp.mpf(1)/2
    L = L or int(mp.ceil(mp.mpf(mp.mp.dps + 5)*mp.log(10)/(-mp.log(rr)))) + 1 if rr > 0 else 1
    return mp.fsum(mp.binomial(-sig, l)*kap**l*hz(p*(sig + l), b) for l in range(L))


def K0for(p, d, kap): return max(1, int(mp.ceil((2*abs(kap))**(1/p) - d)) + 1)


def monic_ops(n, p, s, d, kap):
    K0 = K0for(p, d, kap); lam = lambda k: (k + d)**p + kap
    m = [mp.fsum(lam(k)**(-(s/p + j)) for k in range(1, K0)) + tailZ(s/p + j, K0, p, d, kap) for j in range(2*n + 1)]
    out = {}
    for deg in (n, n - 1):
        A = mp.matrix(deg, deg); b = mp.matrix(deg, 1)
        for i in range(deg):
            for j in range(deg): A[i, j] = m[i + j]
            b[i] = -m[deg + i]
        cs = mp.lu_solve(A, b)
        out[deg] = [cs[i] for i in range(deg)] + [mp.mpf(1)]
    return out[n], out[n - 1]


def poly(cs, x): return sum(c*x**i for i, c in enumerate(cs))


def U2(z, n, cs, p, s, d, kap, R=24):
    zeta = z/n**p; lam = lambda k: (k + d)**p + kap
    lam_need = 64/abs(zeta)          # x_k <= |zeta|/64 beyond M0: (x/zeta)^r <= 64^{-r}, R = 24 gives 2e-43
    M0 = max(K0for(p, d, kap), int(mp.ceil((lam_need + abs(kap))**(1/p) - d)) + 1, 60)
    tot = mp.fsum(lam(k)**(-s/p)*poly(cs, 1/lam(k))/(zeta - 1/lam(k)) for k in range(1, M0))
    for i, ci in enumerate(cs):
        for r in range(R):
            tot += ci*zeta**(-1 - r)*tailZ(s/p + i + r, M0, p, d, kap)
    return tot


def I1(z, n, M, p, s, d, kap, phi1):
    T = n*abs(z)**(-1/p); lam = lambda k: (k + d)**p + kap
    KT = 1
    while lam(KT) <= T**p: KT += 1
    head = mp.fsum(lam(k)**(1 - s/p) for k in range(1, KT))
    M0 = max(KT, K0for(p, d, kap))
    tail = mp.fsum(lam(k)**(-s/p) for k in range(KT, M0)) + tailZ(s/p, M0, p, d, kap)
    return (M/mp.sin(phi1))*(head + T**p*tail)


n = 4; phi1 = PI/6
SB = [(mp.mpf(3)/2, mp.mpf('1.75'), mp.mpf('-0.5'), mp.mpf('0.5')), (mp.mpf(3)/2, mp.mpf('1.75'), mp.mpf('-0.5'), mp.mpf('-0.3')),
      (mp.mpf(3)/2, mp.mpf('3.1'), mp.mpf('-0.3'), mp.mpf(2)), (mp.mpf(3), mp.mpf('2.5'), mp.mpf('-0.9'), mp.mpf(1)),
      (mp.mpf(3), mp.mpf('2.5'), mp.mpf('-0.9'), mp.mpf('-0.0005')), (mp.mpf(3), mp.mpf('5.5'), mp.mpf('-0.5'), mp.mpf('0.5'))]
for (p, s, d, kap) in SB:
    al = (s - 1 - p)/p; lab = f"p={mp.nstr(p,3)} s={s} (alpha={mp.nstr(al,3)}) d={d} kappa={kap}"
    radii = [mp.mpf(1), mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6')] + ([mp.mpf('1e-8')] if p > 2 else [])
    P1, P0 = monic_ops(n, p, s, d, kap)
    x1 = 1/((1 + d)**p + kap)
    worst, expo = 0, []
    for cs in (P1, P0):
        M = max(abs(poly(cs, x1*k/2000)) for k in range(2001))
        mods = {}
        for r in radii:
            b1 = I1(r, n, M, p, s, d, kap, phi1)
            for ang in (phi1/PI, mp.mpf(1)/2, mp.mpf(1)):
                z = r*mp.expjpi(ang); u = abs(U2(z, n, cs, p, s, d, kap))
                worst = max(worst, u/b1)
                if ang == mp.mpf(1)/2: mods[r] = u
        expo.append(mp.log(mods[radii[-2]]/mods[radii[-1]])/mp.log(radii[-2]/radii[-1]))
    tgt = al if al < 0 else 0
    print(f"[SB] {lab}: max |U_j2|/I1^kappa = {mp.nstr(worst, 4)}; exponent of |U_j2(iy)| ({mp.nstr(radii[-2],2)} -> {mp.nstr(radii[-1],2)}): "
          f"{mp.nstr(expo[0], 6)}, {mp.nstr(expo[1], 6)} (min(alpha,0) = {mp.nstr(tgt, 4)}; alpha + 2d = {mp.nstr(al + 2*d, 4)})  (t {time.time() - T0:.0f}s)", flush=True)
    C_.check(f"[SB] |U_j2| <= I1^kappa {lab}", float(max(worst - 1, 0)), 0.0, 0.0)
    for e in expo:
        etol = 1e-3 if p > 2 else 0.02          # p = 3/2: radii 1e-4 -> 1e-6 only (pre-asymptotic corrections ~ |z|^{min(|alpha|, 1/2)})
        C_.check(f"[SB] exponent = min(alpha, 0), kappa- and d-free {lab}", float(e), float(tgt), etol)
        C_.check(f"[ctrl] exponent alpha + 2d (must fail) {lab}", float(abs(e - (al + 2*d)) < 0.1), 0.0, 0.0)

# [AR] lens arcs
bound = 2*mp.exp(-PI/4)*mp.sin(3*PI/8)
def tk(z, n, p, kap): return mp.power(n**p/z - kap, 1/p)
def arc_min(r, n, p, d, kap, npts=801):
    return min(abs(mp.expm1(2*PI*I*(tk(r*mp.expj(PI/3*(2*mp.mpf(j)/(npts - 1) - 1)), n, p, kap) - d))) for j in range(npts))
for (p, d, kap, nn) in ((mp.mpf(3)/2, mp.mpf('-0.3'), mp.mpf('0.5'), 4), (mp.mpf(3)/2, mp.mpf('-0.3'), mp.mpf('-0.3'), 4),
                        (mp.mpf(3), mp.mpf('-0.7'), mp.mpf(1), 4), (mp.mpf(5)/4, mp.mpf('-0.5'), mp.mpf(2), 8),
                        (mp.mpf(3), mp.mpf('-0.5'), mp.mpf(60), 4)):
    lab = f"p={mp.nstr(p,3)} d={d} kappa={kap} n={nn}"; dels = mp.mpf('0.25')
    k0 = int(mp.ceil(tk(dels, nn, p, kap) - d - mp.mpf(1)/2))
    mins = []
    for k in range(k0, k0 + 6):
        u0 = k + d + mp.mpf(1)/2; r = nn**p/(u0**p + kap)         # t_kappa(r) = u0
        mins.append(arc_min(r, nn, p, d, kap))
    # control: lattice-chosen arcs t(r) = u0, i.e. r = (n/u0)^p
    ctrl = []
    for k in range(k0, k0 + 6):
        u0 = k + d + mp.mpf(1)/2; r = (nn/u0)**p
        ctrl.append(arc_min(r, nn, p, d, kap))
    print(f"[AR] {lab}: t_kappa-arcs min |e^(2 pi i(t_k - d)) - 1| = {mp.nstr(min(mins), 5)} (bound {mp.nstr(bound, 5)}); "
          f"lattice-t arcs: {mp.nstr(min(ctrl), 5)}", flush=True)
    C_.check(f"[AR] arc bound on t_kappa-arcs {lab}", float(max(bound - min(mins), 0)), 0.0, 0.0)
    if kap > 10:
        C_.check(f"[ctrl] lattice-t arcs keep the bound at large kappa (must fail) {lab}", float(min(ctrl) >= bound), 0.0, 0.0)
print(f"total time {time.time() - T0:.0f}s")
C_.finish()
