"""Plan 50 (NUMERICAL): Lemma LW1_1 of ROUTE2_p1.md §3.3 (band-centre lip mismatch, p = 1), and the local form of the
KV/Vanlessen Bessel model (§3.2).

Setting (ROUTE2_p1 §2): symmetric rescaled variable z, band [-2, 2], t = n/z^2,
  q_n(z) = Psi1(n/z^2)/Psi1(n) = exp(L1(log n - Log z^2) - L1(log n)),  L1(u) = sqrt(log(e^u + e))
(Psi1(t) = exp sqrt(log(t + e)); analytic for |Im u| < pi; its branch points lie on Im u = +-pi).
Szegő function on [-2, 2]:  log D_q(z) = (R(z)/2pi) int_{-2}^{2} log q(x) dx / (sqrt(4 - x^2)(z - x)),  R = (z-2)^{1/2}(z+2)^{1/2}.
Subtracted, even form used here (q even on the band):
  log D_q(z)^2 - log q(z) = (R(z)/pi) int_0^2 (log q(x) - log q(z)) * 2z / ((z^2 - x^2) sqrt(4 - x^2)) dx.
[1] sup over the lip rays arg z = pi/4 (+ the rays pi/6, pi/3 and the mirror 3pi/4), |z| = 1e-14 .. 0.3, of |D_q^2/q_n - 1|,
    against the eps_1-sample eta_n := max |L1'(u)| over Re u = log n - 2 log 2, |Im u| <= pi/2.
[2] band sanity D_{q,+} D_{q,-} = q at x = 0.5, 1e-3 (computed from the unsubtracted form, z = x +- i 1e-12 is avoided: we use
    Plemelj directly, log D_+ + log D_- = log q).
[3] the other two factors of rho = e^L (4 - x^2) H_n(x)^2 q_n(x): |D_h^2/h - 1|/|z| for h = 4 - x^2 and n |D_H^2/H_n^2 - 1| for
    H_n(z) = H(n/z^2), H(t) = Gamma(t+1) e^t/(sqrt(2 pi) t^(t+1/2)), on the lip ray pi/4.
[4] local form (ROUTE2_p1 §3.2): Vanlessen (4.27) Psi_a in sector II; det Psi = 1, and Psihat := Psi S^{-1} zeta^{-a sigma3}
    (S = [[1, 1/(2 cos a pi)], [0, 1]] e^{-a pi i sigma3/2}) tends to a finite matrix with det 1 as zeta -> 0.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan50/research/G1/RH/route2/checks/check_r2p1_lw1.py"""
import mpmath as mp

mp.mp.dps = 20
E = mp.e


def L1(u):
    return mp.sqrt(mp.log(mp.exp(u) + E))


def dL1(u):
    w = mp.exp(u)
    return w / (2 * (w + E) * mp.sqrt(mp.log(w + E)))


def R(z):
    return mp.sqrt(z - 2) * mp.sqrt(z + 2)


def logq(z, n):
    return L1(mp.log(n) - mp.log(z * z)) - L1(mp.log(n))


def mismatch(z, n, lq=logq, lband=None):
    """|D^2/q - 1| at z; lband(theta) = log q(2 sin theta) on the band (defaults to lq on the real axis)."""
    lz = lq(z, n)
    r = abs(z)
    lb = lband if lband is not None else (lambda th: lq(2 * mp.sin(th), n))
    f = lambda th: (lb(th) - lz) * 2 * z / (z * z - 4 * mp.sin(th) ** 2)  # dx/sqrt(4-x^2) = dth
    br = sorted(set([mp.mpf(0)] + [mp.asin(min(mp.mpf(1), r * mp.mpf(10) ** j / 2)) for j in range(-3, 4)] + [mp.pi / 2]))
    integral = mp.quad(f, br)
    return abs(mp.exp(R(z) / mp.pi * integral) - 1)


if __name__ == "__main__":
    print("[1] q_n lip mismatch sup|D_q^2/q_n - 1| over |z| in [1e-14, 0.3]; eta_n = eps_1-sample; ratio = sup/eta_n")
    radii = [mp.mpf(10) ** (-e / 2) for e in range(1, 29)]
    for n in (mp.mpf(10) ** 2, mp.mpf(10) ** 4, mp.mpf(10) ** 6, mp.mpf(10) ** 9, mp.mpf(10) ** 12):
        T = mp.log(n) - 2 * mp.log(2)
        eta = max(abs(dL1(T + 1j * y)) for y in mp.linspace(-mp.pi / 2, mp.pi / 2, 41))
        out = []
        for ang in (mp.pi / 4, mp.pi / 6, mp.pi / 3, 3 * mp.pi / 4):
            vals = [mismatch(r * mp.expj(ang), n) for r in radii]
            out.append((ang, max(vals), vals[-1]))
        s = "  ".join(f"arg={float(a/mp.pi):.3f}pi: sup={float(m):.4f} (|z|=1e-14: {float(v0):.4f})" for a, m, v0 in out)
        print(f"  n=1e{int(mp.log10(n))}: eta_n={float(eta):.4f}  {s}  ratio(pi/4)={float(out[0][1]/eta):.3f}")

    print("[2] band sanity: |log D_+ + log D_- - log q| at x = 0.5, 1e-3 (n = 1e6), via eps -> 0 from both sides")
    n = mp.mpf(10) ** 6
    for x in (mp.mpf("0.5"), mp.mpf("1e-3")):
        def logD(z):
            f = lambda th: logq(2 * mp.sin(th), n) * 2 * z / (z * z - 4 * mp.sin(th) ** 2)
            th0 = mp.asin(x / 2)
            return R(z) / (2 * mp.pi) * mp.quad(f, [0, th0 * mp.mpf("0.5"), th0, th0 * mp.mpf("1.5"), mp.pi / 2])
        ep = mp.mpf("1e-9")
        val = logD(x + 1j * ep) + logD(x - 1j * ep) - logq(x, n)
        print(f"  x={float(x)}: {float(abs(val)):.2e}")

    print("[3] the analytic band factors on the lip ray pi/4: h = 4 - x^2 (|D_h^2/h - 1|/|z|), H_n^2 (n|D_H^2/H_n^2 - 1|)")
    lh = lambda z, n: mp.log(4 - z * z)
    lh_band = lambda th: 2 * mp.log(2 * mp.cos(th))  # log(4 - x^2) at x = 2 sin(theta), exact near x = 2

    def lH2(z, n):
        t = n / (z * z)
        if abs(t) > 10 ** 8:  # DLMF 5.11.1 (two terms; remainder < 1e-40 here)
            return 2 * (1 / (12 * t) - 1 / (360 * t ** 3))
        return 2 * (mp.loggamma(t + 1) + t - mp.log(mp.sqrt(2 * mp.pi)) - (t + mp.mpf(1) / 2) * mp.log(t))
    for r in (mp.mpf("1e-4"), mp.mpf("1e-2"), mp.mpf("0.1"), mp.mpf("0.3")):
        z = r * mp.expj(mp.pi / 4)
        hh = mismatch(z, 1, lh, lh_band) / r
        HH = [n * mismatch(z, n, lH2, (lambda th, n=n: lH2(2 * mp.sin(th), n) if th > 0 else mp.mpf(0)))
              for n in (mp.mpf(100), mp.mpf(10) ** 4)]
        print(f"  |z|={float(r)}: h-part/|z| = {float(hh):.4f};  n*H-part = {float(HH[0]):.4f} (n=1e2), {float(HH[1]):.4f} (n=1e4)")

    print("[4] local form of Vanlessen (4.27), sector II (arg zeta = 3pi/8): det Psi, |Psi| |zeta|^{|a|}, Psihat -> finite, det Psihat")
    for a in (mp.mpf("-0.4"), mp.mpf(0), mp.mpf("0.3"), mp.mpf("0.45")):
        S = mp.matrix([[1, 1 / (2 * mp.cos(a * mp.pi))], [0, 1]]) * mp.diag([mp.expj(-a * mp.pi / 2), mp.expj(a * mp.pi / 2)])
        rows = []
        for r in (mp.mpf("1e-1"), mp.mpf("1e-4"), mp.mpf("1e-8")):
            zt = r * mp.expj(3 * mp.pi / 8); w = zt * mp.expj(-mp.pi / 2); sq = mp.sqrt(zt); sp = mp.sqrt(mp.pi)
            Ps = mp.matrix([[sp * sq * mp.besseli(a + 0.5, w), -sq * mp.besselk(a + 0.5, w) / sp],
                            [-1j * sp * sq * mp.besseli(a - 0.5, w), -1j * sq * mp.besselk(a - 0.5, w) / sp]])
            Ps = Ps * mp.diag([mp.expj(-a * mp.pi / 2), mp.expj(a * mp.pi / 2)])
            Ph = Ps * mp.inverse(S) * mp.diag([zt ** (-a), zt ** a])
            nrm = max(abs(v) for v in Ps) * r ** abs(a)
            rows.append(f"|zeta|={float(r):.0e}: det={complex(mp.det(Ps)):.6f} |Psi||zeta|^|a|={float(nrm):.3f} "
                        f"Psihat21={complex(Ph[1, 0]):.4f} detPsihat={complex(mp.det(Ph)):.6f}")
        print(f"  a={float(a)}:\n    " + "\n    ".join(rows))
