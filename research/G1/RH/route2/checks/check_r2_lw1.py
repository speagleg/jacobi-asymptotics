"""Plan 48 (NUMERICAL): Lemma LW1' (lip mismatch of the Szego function), ROUTE2.md §3.3.  p = 2, band [0, b], b = 4c(2).
Psi1(t) = exp(L1(log t)) with L1(u) = sqrt(log(e^u + e)) (principal branches; the analytic continuation of sqrt(log(t+e))).
q_N(z) := Psi1(N z^{-1/p}) / Psi1(N)  (the only new factor of the band weight w0, ROUTE2 §2).
Szego function on [0, b]:  log D_q(z) = (R(z)/2pi) int_0^b log q(x) dx / (sqrt(x(b-x)) (z - x)),  R(z) = z sqrt(1 - b/z),
computed with x = b(1 - cos phi)/2 (dx/sqrt(x(b-x)) = dphi), mpmath tanh-sinh, dps 30.
[1] mismatch m_N(z) := |D_q(z)^2/q_N(z) - 1| on the rays arg z = pi/3 (the lips of RH_px §4.1) and pi/6, |z| = 1e-14 .. 0.3;
    eta_N := sup{|L1'(u)|/p : Re u >= log N - log(b)/p, |Im u| <= pi/p} (sampled).  Lemma LW1' predicts sup_z m_N <= C eta_N.
[2] Fisher-Hartwig part: for q = x^alpha (alpha = -1/2, 1/3), |D^2/z^alpha - e^{-i pi alpha}| on arg z = pi/3 is O(|z|^{1/2}).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan48/research/G1/RH/route2/checks/check_r2_lw1.py"""
import mpmath as mp
from jacobi_asym.laws.weyl import c_p

mp.mp.dps = 30
p = 2; b = mp.mpf(4 * c_p(2.0))


def L1(u):
    return mp.sqrt(mp.log(mp.exp(u) + mp.e))


def dL1(u):
    return mp.diff(L1, u)


def logD(logq, z):
    z = mp.mpc(z); R = z * mp.sqrt(1 - b / z)
    ph0 = mp.sqrt(4 * abs(z) / b)
    pts = [0] + [x for x in (ph0 / 10, ph0, 10 * ph0) if x < mp.pi / 2] + [mp.pi]
    xx = lambda ph: b * mp.sin(ph / 2) ** 2  # noqa: E731  (= b(1 - cos ph)/2 without cancellation)
    f = lambda ph: logq(xx(ph)) / (z - xx(ph))  # noqa: E731
    return R / (2 * mp.pi) * mp.quad(f, pts)


RADII = [mp.mpf(10) ** e for e in (-14, -12, -10, -8, -6, -4, -3, -2, -1)] + [mp.mpf("0.3")]
print("[1] sup over rays of |D_q^2/q_N - 1| vs eta_N", flush=True)
for N in (mp.mpf(10) ** 2, mp.mpf(10) ** 4, mp.mpf(10) ** 6, mp.mpf(10) ** 9, mp.mpf(10) ** 12):
    lN = mp.log(N); L1N = L1(lN)
    logq = lambda x: L1(lN - mp.log(x) / p) - L1N  # noqa: E731
    T0 = lN - mp.log(b) / p
    eta = max(abs(dL1(mp.mpc(T0 + d, sg))) / p for d in (0, 1, 3, 10, 30) for sg in (-mp.pi / p, 0, mp.pi / p))
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

print("[2] Fisher-Hartwig factor x^alpha: |D^2/z^alpha - e^{-i pi alpha}| on arg z = pi/3", flush=True)
for al in (mp.mpf(-0.5), mp.mpf(1) / 3):
    row = []
    for r in (mp.mpf(10) ** -8, mp.mpf(10) ** -6, mp.mpf(10) ** -4, mp.mpf(10) ** -2):
        z = r * mp.expj(mp.pi / 3)
        d = abs(mp.exp(2 * logD(lambda x: al * mp.log(x), z) - al * mp.log(z)) - mp.expj(-mp.pi * al))
        row.append(f"|z|={mp.nstr(r, 2)}: {mp.nstr(d, 3)} (/|z|^.5 = {mp.nstr(d / mp.sqrt(r), 3)})")
    print(f"  alpha={mp.nstr(al, 3)}: " + ", ".join(row), flush=True)
