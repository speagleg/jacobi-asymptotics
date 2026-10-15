"""Plan 54 (NUMERICAL): the unsymmetrized x-frame of RH_px / ROUTE2 at p = 1 (ROUTE2_xframe1.md §§1-3).

Setting (RH_px §1 at p = 1): t(z) = N/z, theta = pi t, Dt(z) = sqrt(2 pi) t^(t-1/2) e^(-t)/Gamma(t) = exp(-mu(t)),
D := Dt/(1 - e^{-+2 i theta}) in C+-, band [0, b], b = 4c(1) = 2.
[1] Lemma X1 (reflection): D(z) = exp(mu(-N/z)) (principal branches), so D has no jump on (-inf, 0); ell-hat := 2 arg D_+
    vanishes identically on (-inf, 0) and the Binet-cut scalar B of RH_px Lemma 3.2 is identically 1.
[2] Lemma X2 (why the quotient construction of RH_px §4.1 fails at p = 1): on (-delta, 0) the jump of Dt*B is
    (1 - e^{-2 i theta_+})/(1 - e^{2 i theta_-}); its distance from 1 is O(exp(-2 pi N sin(pi/p)|x|^{-1/p})) for p > 1 and O(1)
    for p = 1; and exp(2 mu(N/z)) (the continuation of the band factor h_N) blows up at z = -N/m + i0.
[3] Lemma LW1-x1 (the q_N part at p = 1): sup over the lip rays arg z = pi/3, pi/6 (|z| = 1e-14 .. 0.3) of |D_q^2/q_N - 1|,
    q_N(z) = Psi1(N/z)/Psi1(N), Psi1(t) = exp sqrt(log(t + e)), against eta_N := sampled sup |L1'(u)| over
    Re u >= log N - log b, |Im u| <= pi/2.
[4] the h-part at p = 1: q = (b - x) h_N(x), h_N = exp(2 mu(N/x)); |D_q^2/q - 1| / |z|^(1/2) on arg z = pi/3.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan54/research/G1/RH/route2/checks/check_x1_frame.py"""
import mpmath as mp

mp.mp.dps = 30
E = mp.e
b = mp.mpf(2)  # 4 c(1), c(1) = 1/2


def mu(u):
    return mp.loggamma(u) - (u - mp.mpf(1) / 2) * mp.log(u) + u - mp.log(2 * mp.pi) / 2


def Dt(z, N, p=1):
    t = N * mp.power(z, -mp.mpf(1) / p)
    return mp.exp(-mu(t))


def Dwlxz(z, N, p=1):
    sg = 1 if mp.im(z) > 0 else -1
    t = N * mp.power(z, -mp.mpf(1) / p)
    return Dt(z, N, p) / (1 - mp.exp(-sg * 2j * mp.pi * t))


print("[1] D = Dt/(1 - e^{-+2i theta}) versus exp(mu(-N/z)), p = 1, N = 20", flush=True)
N = 20
worst = 0
for z in [mp.mpc(-1.3, 1e-20), mp.mpc(-1.3, -1e-20), mp.mpc(-0.013, 1e-22), mp.mpc(0.3, 0.5), mp.mpc(-0.01, 0.002),
          mp.mpc(-7, -3), mp.mpc(3, -0.2), mp.mpc(25, 1), mp.mpc(-1e4, 1)]:
    d1, d2 = Dwlxz(z, N), mp.exp(mu(-N / z))
    worst = max(worst, abs(d1 / d2 - 1))
    print(f"  z={mp.nstr(z, 4):>26}: D = {mp.nstr(d1, 12):>32}   exp(mu(-N/z)) = {mp.nstr(d2, 12)}")
print(f"  max relative difference = {mp.nstr(worst, 3)}")
ells = [2 * mp.arg(mp.exp(mu(mp.mpf(N) / x))) for x in (mp.mpf("1e-6"), mp.mpf("0.01"), mp.mpf("0.37"), mp.mpf(5), mp.mpf(1000))]
print(f"  ell-hat(-x) = 2 arg D_+(-x) via exp(mu(N/x)) (N/x > 0, mu real): {[mp.nstr(e, 3) for e in ells]}  => B == 1")
# direct evaluation of the WLXZ form at non-integer t (0/0 only at the integers t = -m)
ell2 = [2 * mp.arg(Dwlxz(mp.mpc(-x, mp.mpf("1e-25")), N)) for x in (mp.mpf("0.0137"), mp.mpf("0.371"), mp.mpf("5.3"), mp.mpf(1003))]
print(f"  ell-hat from the WLXZ form (x = 0.0137, 0.371, 5.3, 1003): {[mp.nstr(e, 3) for e in ell2]}", flush=True)

print("[2] the (h2) jump on (-delta, 0): |(1 - e^{-2i theta+})/(1 - e^{2i theta-}) - 1| at x = -0.0123, -0.0517, -0.1043 (N = 20)", flush=True)
for p in (mp.mpf(2), mp.mpf("1.5"), mp.mpf("1.1"), mp.mpf(1)):
    row = []
    for x in (mp.mpf("0.0123"), mp.mpf("0.0517"), mp.mpf("0.1043")):
        zp, zm = mp.mpc(-x, mp.mpf("1e-25")), mp.mpc(-x, -mp.mpf("1e-25"))
        tp, tm = N * mp.power(zp, -1 / p), N * mp.power(zm, -1 / p)
        J = (1 - mp.exp(-2j * mp.pi * tp)) / (1 - mp.exp(2j * mp.pi * tm))
        row.append(mp.nstr(abs(J - 1), 3))
    print(f"  p = {mp.nstr(p, 3)}: {row}   (sin(pi/p) = {mp.nstr(mp.sin(mp.pi / p), 3)})")
row = []
for m in (40, 400, 4000):
    z0 = -mp.mpf(N) / m
    row.append(f"m={m}: |exp(2 mu(N/z))| at z = -N/m + i 1e-12 |z|: {mp.nstr(abs(mp.exp(2 * mu(N / mp.mpc(z0, abs(z0) * mp.mpf('1e-12'))))), 3)}")
print("  continuation of h_N ~ exp(2 mu(N/z)) to the negative axis (p = 1): " + "; ".join(row), flush=True)


def L1(u):
    return mp.sqrt(mp.log(mp.exp(u) + E))


def dL1(u):
    w = mp.exp(u)
    return w / (2 * (w + E) * mp.sqrt(mp.log(w + E)))


def logD(logq, z):
    """log D_q(z) = (R(z)/2pi) int_0^b log q(x) dx/(sqrt(x(b-x))(z-x)), x = b sin^2(ph/2)."""
    z = mp.mpc(z); R = z * mp.sqrt(1 - b / z)
    ph0 = mp.sqrt(4 * abs(z) / b)
    pts = [0] + [x for x in (ph0 / 10, ph0, 10 * ph0) if x < mp.pi / 2] + [mp.pi]
    xx = lambda ph: b * mp.sin(ph / 2) ** 2  # noqa: E731
    return R / (2 * mp.pi) * mp.quad(lambda ph: logq(xx(ph)) / (z - xx(ph)), pts)


RADII = [mp.mpf(10) ** e for e in (-14, -12, -10, -8, -6, -4, -3, -2, -1)] + [mp.mpf("0.3")]
print("[3] q_N part (p = 1): sup over rays arg z = pi/3, pi/6 of |D_q^2/q_N - 1| vs eta_N", flush=True)
for N in (mp.mpf(10) ** 2, mp.mpf(10) ** 4, mp.mpf(10) ** 6, mp.mpf(10) ** 9, mp.mpf(10) ** 12):
    lN = mp.log(N); L1N = L1(lN)
    logq = lambda x: L1(lN - mp.log(x)) - L1N  # noqa: E731
    T0 = lN - mp.log(b)
    eta = max(abs(dL1(mp.mpc(T0 + d, sg))) for d in (0, 1, 3, 10, 30) for sg in (-mp.pi / 2, 0, mp.pi / 2))
    worst = 0; rows = []
    for th in (mp.pi / 3, mp.pi / 6):
        for r in RADII:
            z = r * mp.expj(th)
            m = abs(mp.exp(2 * logD(logq, z) - logq(z)) - 1)
            worst = max(worst, m)
            if th == mp.pi / 3 and r in (RADII[0], RADII[4], RADII[-1]):
                rows.append(f"|z|={mp.nstr(r, 2)}: {mp.nstr(m, 3)}")
    print(f"  N=1e{int(mp.nint(mp.log10(N)))}: eta_N = {mp.nstr(eta, 4)}, sup m_N = {mp.nstr(worst, 4)}, "
          f"ratio = {mp.nstr(worst / eta, 4)} ; arg pi/3: " + ", ".join(rows), flush=True)

print("[4] h-part (p = 1): q = (b - x) exp(2 mu(N/x)); |D_q^2/q - 1| and its ratio to |z|^(1/2) on arg z = pi/3", flush=True)
for N in (20, 200):
    logq = lambda x: (mp.log(b - x) + 2 * mu(mp.mpf(N) / x)  # noqa: E731
                      if isinstance(x, mp.mpc) else
                      mp.log(max(b - x, b * mp.mpf(10) ** -40)) + (2 * mu(mp.mpf(N) / x) if x > mp.mpf(10) ** -40 else 0))
    row = []
    for r in (mp.mpf(10) ** -8, mp.mpf(10) ** -6, mp.mpf(10) ** -4, mp.mpf(10) ** -2, mp.mpf("0.1")):
        z = r * mp.expj(mp.pi / 3)
        d = abs(mp.exp(2 * logD(logq, z) - logq(z)) - 1)
        row.append(f"|z|={mp.nstr(r, 2)}: {mp.nstr(d, 3)} (/|z|^.5 = {mp.nstr(d / mp.sqrt(r), 3)})")
    print(f"  N={N}: " + ", ".join(row), flush=True)
