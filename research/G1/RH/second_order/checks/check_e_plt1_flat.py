"""Plan 67 (E_plt1.md Lemma F.1), NUMERICAL: the log band factor of the seam geometry, built literally from Paper 2
Lemma seam (app_outer.tex, eqs. (Lpm), (chi), (F-seam)), against the closed form of Lemma F.1:

  G(z) := log(Dtilde B_in e^chi)  in S_in,   G(z) := log(B_out e^chi)  in S_out     (H_n = e^{-2G}),
  G(z) - G(1) = sum_{k>=1} zeta(-k p) (z^k - 1)/(k n^{k p})   (asymptotic; Lemma F.1 proves the k = 1 term + O(n^{-2p})).

chi is computed by quadrature of the seam densities chi_pm over the two rays (no use of Lemma F.1).  Printed:
  r1 := n^{2p} (G(z) - G(1) - zeta(-p)(z-1) n^{-p})   and the k = 2 prediction zeta(-2p)(z^2-1)/2,
  r2 := n^{3p} (G(z) - G(1) - [k=1] - [k=2])  and the k = 3 prediction zeta(-3p)(z^3-1)/3.
Also checks the closed form of the first seam moment, (sin(pi p/2)/pi) int_0^inf log(1 - e^{-2 pi n r^{-1/p}}) r^{-2} dr
= zeta(-p) n^{-p} (Lemma F.1, step (c)), by quadrature."""
import mpmath as mp

mp.mp.dps = 40


def jfun(t):
    """Binet's function j(t) = LogGamma(t) - (t - 1/2) Log t + t - log(2 pi)/2 (|arg t| < pi); Stirling series
    (DLMF 5.11.1, 8 terms, error < 1e-60 for |t| > 1e4 in |arg t| <= pi/2) for large |t| to avoid cancellation."""
    if abs(t) > 1e4:
        B = [mp.bernoulli(2 * k) for k in range(1, 9)]
        return sum(B[k - 1] / (2 * k * (2 * k - 1) * t ** (2 * k - 1)) for k in range(1, 9))
    return mp.loggamma(t) - (t - mp.mpf(1) / 2) * mp.log(t) + t - mp.log(2 * mp.pi) / 2


def setup(p, n):
    p, n = mp.mpf(p), mp.mpf(n)
    th = mp.pi * p / 2
    vp = mp.mpf(1) / 2 - 1 / (2 * p)
    e = mp.exp(1j * th)

    def chi_plus(r):
        zeta = r * e
        tt = n * r ** (-1 / p)                      # t = -i tt on the upper seam (arg t = -pi/2 exactly)
        t = mp.mpc(0, -tt)
        return (-jfun(t) - mp.log(-mp.expm1(-2 * mp.pi * tt)) + vp * mp.log(1 + zeta)
                - mp.log(1 - zeta / (2 * mp.pi * n)) / 2)

    sc = n ** p
    pts = [0] + [sc * f for f in (mp.mpf('1e-3'), mp.mpf('1e-2'), mp.mpf('0.1'), 1, 10, 100, 1000)] + [mp.inf]
    pts = sorted(set(pts + [mp.mpf(q) for q in (0.5, 1, 2, 4)]))

    def chi(z):
        f1 = lambda r: chi_plus(r) * e / (r * e - z)
        f2 = lambda r: mp.conj(chi_plus(r)) * mp.conj(e) / (r * mp.conj(e) - z)
        return (mp.quad(f1, pts) - mp.quad(f2, pts)) / (2j * mp.pi)

    def G(z):
        z = mp.mpc(z)
        if abs(mp.arg(z)) < th:
            t = n * mp.exp(-mp.log(z) / p)
            return -jfun(t) + vp * mp.log(1 + z) + chi(z)
        return mp.log(1 - z / (2 * mp.pi * n)) / 2 + chi(z)

    return G


if __name__ == "__main__":
    print("[A] first seam moment: (sin(pi p/2)/pi) int_0^inf log(1-exp(-2 pi n r^{-1/p})) r^{-2} dr  vs  zeta(-p) n^{-p}")
    for p in (0.3, 0.5, 0.7, 0.9):
        for n in (1, 10):
            P = mp.mpf(p)
            val = mp.sin(mp.pi * P / 2) / mp.pi * mp.quad(lambda r: mp.log(-mp.expm1(-2 * mp.pi * n * r ** (-1 / P))) / r ** 2,
                                                         [0, n ** P / 10, n ** P, 10 * n ** P, mp.inf])
            ref = mp.zeta(-P) * mp.mpf(n) ** (-P)
            print(f"  p={p} n={n:3d}: quad {mp.nstr(val, 15):>22}  zeta(-p) n^-p {mp.nstr(ref, 15):>22}  rel.diff {mp.nstr(abs(val/ref-1), 3)}")
            assert abs(val / ref - 1) < mp.mpf('1e-20')
    print("\n[B] G(z) - G(1) from the literal seam construction vs Lemma F.1")
    for p in (0.5, 0.3, 0.7):
        P = mp.mpf(p)
        print(f" p = {p}, seam angle pi p/2 = {float(mp.pi*P/2):.4f}")
        zs = [mp.mpf('0.2'), mp.mpf('1.5'), mp.mpc(1, 0.2), mp.mpf(-0.5), mp.mpc(0.3, 1), mp.mpc(-1, 0.3)]
        for n in (10, 40, 160, 640):
            G = setup(p, n)
            G1 = G(1)
            for z in zs:
                d = G(z) - G1
                k1 = mp.zeta(-P) * (z - 1) * mp.mpf(n) ** (-P)
                k2 = mp.zeta(-2 * P) * (z ** 2 - 1) / 2 * mp.mpf(n) ** (-2 * P)
                k3 = mp.zeta(-3 * P) * (z ** 3 - 1) / 3 * mp.mpf(n) ** (-3 * P)
                r1 = (d - k1) * mp.mpf(n) ** (2 * P)
                r2 = (d - k1 - k2) * mp.mpf(n) ** (3 * P)
                side = "in " if abs(mp.arg(z)) < mp.pi * P / 2 else "out"
                print(f"  n={n:4d} z={mp.nstr(z, 3):>14} ({side}): G-G(1) = {mp.nstr(d, 10):>34}  "
                      f"r1 = {mp.nstr(r1, 6):>24} (k=2 pred {mp.nstr(k2 * mp.mpf(n) ** (2 * P), 6)})  "
                      f"r2 = {mp.nstr(r2, 5):>22} (k=3 pred {mp.nstr(k3 * mp.mpf(n) ** (3 * P), 5)})")
