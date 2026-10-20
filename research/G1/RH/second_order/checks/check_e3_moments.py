"""Plan E3 (E3_pgt1.md Lemma F.1', NUMERICAL check of the closed form): for p > 1 the jump density of E_pgt1 Lemma E.2,
  e(y) = 2 Im Log(1 - exp(-2 i pi t_+(y))),  t_+(y) = n (y + i0)^{-1/p} = n r^{-1/p} e^{-i pi/p}  (y = -r < 0),
has moments m_k := (1/2pi) int_{-inf}^0 e(y) y^{-k-1} dy = zeta(-k p)/(k n^{k p})  (k >= 1),
the same law as E_plt1 Lemma F.1(iii) for 0 < p < 1. Quadrature at 40 digits."""
import mpmath as mp
mp.mp.dps = 40


def e_dens(r, p, n):
    t = n * r ** (-1 / mp.mpf(p)) * mp.expj(-mp.pi / p)
    a = -2j * mp.pi * t                       # q = e^a, |q| = e^{Re a} < 1 (Re a = -2 pi n r^{-1/p} sin(pi/p))
    if mp.re(a) < -300:                       # |q| < e^{-300}: e = -2 Im q + O(|q|^2), negligible at 40 digits
        return mp.mpf(0)
    return 2 * mp.im(mp.log(1 - mp.exp(a)))


def moment(k, p, n):
    p = mp.mpf(p)
    # y = -r: dy = -dr, y^{-k-1} = (-1)^{k+1} r^{-k-1}; int_{-inf}^0 ... dy = int_0^inf ... dr
    f = lambda r: e_dens(r, p, n) * (-1) ** (k + 1) * r ** (-k - 1)
    scale = n ** p
    return mp.quad(f, [0, scale * mp.mpf('0.01'), scale * 0.1, scale, 10 * scale, 100 * scale, mp.inf]) / (2 * mp.pi)


for p in (1.25, 1.5, 3, 2):
    for n in (5, 20):
        for k in (1, 2, 3):
            m = moment(k, p, n)
            ref = mp.zeta(-k * mp.mpf(p)) / (k * mp.mpf(n) ** (k * p))
            rel = abs(m - ref) / abs(ref) if ref != 0 else abs(m)
            tag = "rel.err" if ref != 0 else "abs (ref = 0)"
            print(f"p={p} n={n} k={k}: m_k = {mp.nstr(m, 15)}  zeta(-kp)/(k n^kp) = {mp.nstr(ref, 15)}  {tag} {mp.nstr(rel, 3)}")
