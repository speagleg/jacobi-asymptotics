"""Plan 65 (E_pgt1.md Lemma E.2; NUMERICAL illustration): the band factor H_n = (D~ B)^{-2} of RH_px / Paper 2 is constant
up to O(n^{-p}) on {|z| <= 4c+1}, although D~ and B separately vary at order 1/n.
G := log D~ + log B = -j(t) + log B (j = Binet's function, t = n z^{-1/p}, B the Binet-cut scalar of Paper 2 (eq. B)).
Printed: max over sample points z of |G(z) - G(1)| (direct evaluation of j and of the Cauchy integral defining B), its
product with n^p, and the size of the separate first-order terms |j(t(z)) - j(t(1))| (which are of order 1/n).
Sample points: x in (0, 4c+1] on the band and the saturated side, and two points of the circle |z| = 0.3 (arg 2.5, 3.1)."""
import mpmath as mp
mp.mp.dps = 30


def j(t):
    return mp.loggamma(t) - (t - mp.mpf(1) / 2) * mp.log(t) + t - mp.log(2 * mp.pi) / 2


def run(p, n):
    p = mp.mpf(p)
    def bfrak(y):            # Paper 2 Lemma binetcut(ii): b(y) = 2 Im(-j(t_+) - Log(1 - e^{-2 i theta_+})), y < 0
        tp = n * (-y) ** (-1 / p) * mp.exp(-1j * mp.pi / p); th = mp.pi * tp
        lt = 0 if 2 * mp.im(th) < -300 else mp.log(1 - mp.exp(-2j * th))
        return 2 * mp.im(-j(tp) - lt)
    L = p * mp.log(n)
    brk = [-80, -20, -5, 0, L - 6, L - 2, L, L + 2, L + 6, L + 20, L + 60, L + 200]
    def logB(z):
        f = lambda u: bfrak(-mp.exp(u)) * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u)
        return -mp.quad(f, brk, maxdegree=10) / (2 * mp.pi)
    G = lambda z: -j(n * z ** (-1 / p)) + logB(z)
    Ip = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1); c4 = (mp.pi / (2 * Ip)) ** p
    pts = [mp.mpf('0.001'), mp.mpf('0.1'), mp.mpf('0.5'), c4 / 2, c4, c4 + 1, 0.3 * mp.exp(2.5j), 0.3 * mp.exp(3.1j)]
    G1 = G(mp.mpf(1)); j1 = j(mp.mpf(n))
    m = max(abs(G(z) - G1) for z in pts)
    mj = max(abs(j(n * z ** (-1 / p)) - j1) for z in pts)
    return m, mj


for p in (1.5, 2, 3):
    for n in (10, 20, 40, 80):
        m, mj = run(p, n)
        print(f"p = {p}, n = {n:3d}: max|G(z) - G(1)| = {mp.nstr(m, 5):>11}   n^p * max = {mp.nstr(m * mp.mpf(n) ** p, 5):>9}"
              f"   (max|j(t(z)) - j(t(1))| = {mp.nstr(mj, 4)}, n * that = {mp.nstr(mj * n, 4)})")
