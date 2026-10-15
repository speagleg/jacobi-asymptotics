"""Plan 51 (NUMERICAL): Lemma LW1'_{<1} (ROUTE2_plt1.md §3) at p = 1/2.  Band [0, b], b = 4c(p); lips at arg z = theta_L = pi p/4,
seams at theta_s = pi p/2 (RH_plt1b §1-§2).
[1] q_N-part: q_N(z) := Psi1(N z^{-1/p})/Psi1(N), Psi1(t) = exp(L1(log t)), L1(u) = sqrt(log(e^u + e)).  Szego function on [0, b]
    log D_q(z) = (R(z)/2pi) int_0^b log q(x) dx/(sqrt(x(b-x))(z - x)) (as check_r2_lw1.py).  m_N := sup |D_q^2/q_N - 1| over the
    rays arg z = theta_L, theta_L/2, |z| = 1e-14..0.3, against eta_N := sup{|L1'(u)|/p : Re u >= log N - log(b)/p,
    |Im u| <= pi/2} (sampled).  Lemma LW1'_{<1}: m_N <= C eta_N.  Only |Im u| <= theta_L/p = pi/4 is visited.
[2] seam scalar X (RH_plt1b §1): X(z) = (1/2 pi i)[int_{Gamma+} L+ dzeta/(zeta - z) - int_{Gamma-} L- dzeta/(zeta - z)].
    (a) implementation check: X(0) at p = 0.4, N = 10, 1e2, 1e4, 1e6 (RH_plt1b F3 probe: -1.24, -1.93, -3.31, -4.70).
    (b) Lemma X0: Q_N := sup |X(z) - X(0)| / (|z|(1 + log(1/|z|))) over z on the band (arg 0) and the lips (arg theta_L),
        |z| = 1e-8 .. 0.5, at p = 1/2 and N = 1e2, 1e4, 1e6: bounded uniformly in N.
L+ = log(D B_in/B_out) = lam(t) - Log(1 - e^{-2 pi i t}) + c Log(1 + z) - (1/2)Log(1 - z/(2 pi N)) with
lam(t) := log D~(t) = (1/2)log 2pi + (t - 1/2)Log t - t - LogGamma(t) = -mu(t), mu = Binet's function (RH_px §1).  RH_plt1b §1's L+ = -mu - ...
is correct with Binet's mu; only its displayed definition of mu has the opposite sign (REVIEW_Plan51.md F2; ROUTE2_plt1.md §3.2).
lam is evaluated by Stirling's series (3 terms) for |t| > 60 and by mpmath loggamma otherwise.
[2b] also prints the sup over |z| <= 1e-2 separately (REVIEW_Plan51.md F7(b): the overall sup sits at |z| = 0.5).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan51/research/G1/RH/route2/checks/check_r2p_lw1.py"""
import mpmath as mp
from jacobi_asym.laws.weyl import c_p

mp.mp.dps = 30


def L1(u):
    return mp.sqrt(mp.log(mp.exp(u) + mp.e))


def dL1(u):
    return mp.diff(L1, u)


def logD(logq, z, b):
    z = mp.mpc(z); R = z * mp.sqrt(1 - b / z)
    ph0 = mp.sqrt(4 * abs(z) / b)
    pts = [0] + [x for x in (ph0 / 10, ph0, 10 * ph0) if x < mp.pi / 2] + [mp.pi]
    xx = lambda ph: b * mp.sin(ph / 2) ** 2  # noqa: E731
    f = lambda ph: logq(xx(ph)) / (z - xx(ph))  # noqa: E731
    return R / (2 * mp.pi) * mp.quad(f, pts)


p = mp.mpf(1) / 2; b = mp.mpf(4 * c_p(0.5)); thL = mp.pi * p / 4
RADII = [mp.mpf(10) ** e for e in (-14, -12, -10, -8, -6, -4, -3, -2, -1)] + [mp.mpf("0.3")]
print(f"[1] p = 1/2, b = 4c(p) = {mp.nstr(b, 8)}, lips at theta_L = pi/8: sup |D_q^2/q_N - 1| vs eta_N (strip |Im u| <= pi/2)",
      flush=True)
for N in (mp.mpf(10) ** 2, mp.mpf(10) ** 4, mp.mpf(10) ** 6, mp.mpf(10) ** 9, mp.mpf(10) ** 12):
    lN = mp.log(N); L1N = L1(lN)
    logq = lambda x: L1(lN - mp.log(x) / p) - L1N  # noqa: E731
    T0 = lN - mp.log(b) / p
    eta = max(abs(dL1(mp.mpc(T0 + d, sg))) / p for d in (0, 1, 3, 10, 30) for sg in (-mp.pi / 2, 0, mp.pi / 2))
    worst = 0
    for th in (thL, thL / 2):
        for r in RADII:
            z = r * mp.expj(th)
            worst = max(worst, abs(mp.exp(2 * logD(logq, z, b) - logq(z)) - 1))
    print(f"  N=1e{int(mp.nint(mp.log10(N)))}: eta_N = {mp.nstr(eta, 4)}, sup m_N = {mp.nstr(worst, 4)}, "
          f"ratio = {mp.nstr(worst / eta, 4)}", flush=True)

BERN = [mp.bernoulli(2 * k) / (2 * k * (2 * k - 1)) for k in (1, 2, 3)]


def lam(t):
    if abs(t) > 60:
        return -sum(B / t ** (2 * k - 1) for k, B in zip((1, 2, 3), BERN))
    return mp.log(2 * mp.pi) / 2 + (t - mp.mpf(1) / 2) * mp.log(t) - t - mp.loggamma(t)


def Lplus(rho, pp, N):
    ths = mp.pi * pp / 2; zeta = rho * mp.expj(ths); c = mp.mpf(1) / 2 - 1 / (2 * pp)
    logt = mp.log(N) - mp.log(zeta) / pp; t = mp.exp(logt)
    e2 = mp.exp(-2j * mp.pi * t) if abs(t) < 1e3 else 0  # |e^{-2 pi i t}| = e^{-2 pi |t|} < 1e-2700 otherwise
    return (lam(t) - mp.log(1 - e2) + c * mp.log(1 + zeta) - mp.log(1 - zeta / (2 * mp.pi * N)) / 2)


def brk(pp, N, extra=()):
    """log-spaced breakpoints 0, 1e-3, ..., 10^6 N^p (each quad piece within one decade: the integrands are smooth there).
    The integral is truncated at R = 10^6 N^p: there |L+| = O(N^p/rho) (L+ -> 0 at infinity, RH_plt1b Lemma S(ii)), so the
    neglected tail of int L dzeta/zeta-type integrals is O(|L+(R)|) (printed as 'tail')."""
    top = int(mp.ceil(mp.log10(N ** pp))) + 6
    return sorted(set([mp.mpf(0)] + [mp.mpf(10) ** k for k in range(-3, top + 1)] + [mp.mpf(x) for x in extra]))


def X0(pp, N):
    return mp.quad(lambda r: mp.im(Lplus(r, pp, N)) / r, brk(pp, N)) / mp.pi


def Xdiff(z, pp, N):
    ths = mp.pi * pp / 2; e1 = mp.expj(ths); e2 = mp.expj(-ths)
    f = lambda r: (Lplus(r, pp, N) / (r * (r * e1 - z)) - mp.conj(Lplus(r, pp, N)) / (r * (r * e2 - z)))  # noqa: E731
    return z / (2j * mp.pi) * mp.quad(f, brk(pp, N, (abs(z) / 10, abs(z), 10 * abs(z))))


mp.mp.dps = 30
print("[2a] X(0) at p = 0.4 (RH_plt1b probe: -1.24, -1.93, -3.31, -4.70): "
      + ", ".join(f"N=1e{e}: {mp.nstr(X0(mp.mpf('0.4'), mp.mpf(10) ** e), 4)} (tail {mp.nstr(abs(Lplus(brk(mp.mpf('0.4'), mp.mpf(10) ** e)[-1], mp.mpf('0.4'), mp.mpf(10) ** e)), 2)})" for e in (1, 2, 4, 6)), flush=True)
print("[2b] p = 1/2: Q_N = sup |X(z) - X(0)|/(|z|(1 + log(1/|z|))), z on arg 0 and arg theta_L, |z| = 1e-8..0.5", flush=True)
for e in (2, 4, 6):
    N = mp.mpf(10) ** e; worst = 0; arg_w = None; small = 0
    for th in (mp.mpf(0), thL):
        for r in [mp.mpf(10) ** k for k in (-8, -6, -4, -3, -2, -1)] + [mp.mpf("0.5")]:
            z = r * mp.expj(th); q = abs(Xdiff(z, p, N)) / (r * (1 + mp.log(1 / r)))
            if r <= mp.mpf("0.01"):
                small = max(small, q)
            if q > worst:
                worst, arg_w = q, (mp.nstr(th, 3), mp.nstr(r, 2))
    print(f"  N=1e{e}: X(0) = {mp.nstr(X0(p, N), 5)}, Q_N = {mp.nstr(worst, 4)} (attained at arg, |z| = {arg_w}); "
          f"sup over |z| <= 1e-2: {mp.nstr(small, 4)}", flush=True)
