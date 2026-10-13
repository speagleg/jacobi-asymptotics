r"""RH_1 for general r (p = 1): checks of the new analytic objects in RH_p1_general.md (NUMERICAL, Rule N).
Run from the repo root.
[1] Szego function of |x|^{2a} on [-2,2]: D_a(z) = (z/Phi(z))^a, Phi(z) = (z + sqrt(z^2-4))/2 (branch ~ z at infinity).
    Check D_a(+) D_a(-) = |x|^{2a} on (-2,2)\{0}, D_a(z) -> 1 at infinity, and |D_a(z)|/|z|^a bounded above and below near 0.
[2] Stirling truncation: kappa := H(t)^2 / Q_m(z), t = n/z^2, log Q_m = 2 sum_{k<=m} B_{2k}/(2k(2k-1)) t^{-(2k-1)}.
    Report max |kappa - 1| / (|z|^2/n)^{2m+1} over z in the sector |arg z| <= pi/3 (the contours inside U(0,eps)).
[3] Bessel model Psi_a (KV (5.23), sector I).  det = 1; amplification on the band ray (arg zeta = 0+) of a diagonal
    mismatch, A_band = |Psi sigma3 Psi^{-1}|, and on the lip ray (arg zeta = pi/4) of the lip mismatch,
    A_lip = |Psi (J - I) Psi^{-1}|, J - I = [[0,0],[e^{-2 pi i a},0]].  Expected: <= C rho^{-2|a|} (1+|log rho|)^2 for
    rho <= 1 and <= C for rho >= 1 (Lemma M of RH_p1_general.md)."""
import mpmath as mp

mp.mp.dps = 150


def Phi(z):
    s = mp.sqrt(z - 2) * mp.sqrt(z + 2)  # principal branches: ~ z at infinity, cut [-2,2]
    return (z + s) / 2


def D(z, a):
    return mp.exp(a * mp.log(z / Phi(z)))


def check_szego():
    print("[1] Szego function D_a(z) = (z/Phi(z))^a")
    for a in (-0.4, 0.5, 1.5, 2.5):
        err = 0
        for x in (-1.9, -1.0, -0.3, -1e-3, 1e-3, 0.3, 1.0, 1.9):
            e = mp.mpf("1e-25")
            prod = D(mp.mpc(x, e), a) * D(mp.mpc(x, -e), a)
            err = max(err, abs(prod / abs(x) ** (2 * a) - 1))
        inf = abs(D(mp.mpc(1e8, 3e7), a) - 1)
        rat = [abs(D(r * mp.expjpi(th), a)) / r ** a for r in (1e-2, 1e-4, 1e-6) for th in (0.1, 0.5, 0.9, -0.5)]
        print(f"  a={a:+.2f}: max|D+D-/|x|^2a - 1| = {mp.nstr(err, 3)}   |D(1e8)-1| = {mp.nstr(inf, 3)}   "
              f"|D|/|z|^a in [{mp.nstr(min(rat), 4)}, {mp.nstr(max(rat), 4)}]")


def logH(t):
    return mp.loggamma(t + 1) + t - mp.log(2 * mp.pi) / 2 - (t + mp.mpf(1) / 2) * mp.log(t)


def logQ(t, m):
    return 2 * sum(mp.bernoulli(2 * k) / (2 * k * (2 * k - 1)) * t ** (-(2 * k - 1)) for k in range(1, m + 1))


def check_stirling():
    print("[2] kappa = H(n/z^2)^2/Q_m(z): max |kappa-1| / (|z|^2/n)^(2m+1), z in |arg z| <= pi/3, |z| <= 0.5")
    for n in (100, 1000, 10000):
        row = []
        for m in (0, 1, 2):
            worst = 0
            for r in (0.5, 0.2, 0.05, 0.01):
                for th in (0, 1 / 12, 1 / 6, 1 / 4, 1 / 3):
                    z = r * mp.expjpi(th)
                    t = n / z ** 2
                    kap = mp.exp(2 * logH(t) - logQ(t, m))
                    worst = max(worst, abs(kap - 1) / (r ** 2 / n) ** (2 * m + 1))
            row.append(f"m={m}: {mp.nstr(worst, 4)}")
        print(f"  n={n}: " + "   ".join(row))


def Psi_I(zeta, a):
    h = lambda f, nu: f(nu, zeta)
    M = mp.matrix([[h(mp.hankel2, a + 0.5), -1j * h(mp.hankel1, a + 0.5)],
                   [h(mp.hankel2, a - 0.5), -1j * h(mp.hankel1, a - 0.5)]])
    c = mp.sqrt(mp.pi) / 2 * mp.sqrt(zeta)
    ph = mp.exp(-(a + 0.25) * mp.pi * 1j)
    return c * M * mp.diag([ph, 1 / ph])


def norm(M):
    return mp.mnorm(M, 1)


def inv(M):  # det Psi = 1 (KV/Vanlessen (4.53)); adjugate avoids LU breakdown when |e^{i zeta}| is huge
    return mp.matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]])  # det = 1 exactly; dividing by the numerical det loses everything at large rho


def check_psi():
    print("[3] Psi_a amplification (sector I, KV (5.23))")
    s3 = mp.diag([1, -1])
    for a in (-0.4, 0.0, 0.5, 1.5, 2.5):
        JmI = mp.matrix([[0, 0], [mp.exp(-2j * mp.pi * a), 0]])
        print(f"  a={a:+.2f}:")
        for rho in (1e-6, 1e-4, 1e-2, 1, 10, 1e2):
            Pb = Psi_I(rho * mp.expjpi(mp.mpf("1e-12")), a)
            Pl = Psi_I(rho * mp.expjpi(mp.mpf(1) / 4 - mp.mpf("1e-12")), a)
            Ab = norm(Pb * s3 * inv(Pb))
            Al = norm(Pl * JmI * inv(Pl))
            w = rho ** (-2 * abs(a)) * (1 + abs(mp.log(rho))) ** 2 if rho < 1 else 1
            print(f"    rho={rho:7.0e}  det={mp.nstr(mp.det(Pb), 6)}  A_band={mp.nstr(Ab, 4):>10}  "
                  f"A_lip={mp.nstr(Al, 4):>10}  A/weight: {mp.nstr(Ab / w, 3)}, {mp.nstr(Al / w, 3)}")


if __name__ == "__main__":
    check_szego()
    check_stirling()
    check_psi()
