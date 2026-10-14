"""Plan 14 A2 (NUMERICAL check of Lemma LW1): the log factor's Szego function on the band.
Rescaled variable z = s x, s = 1/x_N; band [0, bh] (bh = pi^2/4 used; LW1 is insensitive to the exact edge).
Lambda(z) = log(gamma(z)/2pi), gamma(z) = sqrt(s/z - 1/4) (principal branches).
G(z) = exp( R(z)/(2pi) int_0^bh log Lambda(x) / sqrt(x(bh-x)) dx/(z-x) ),  R(z) = sqrt(z(z-bh)) ~ z.
Claim (LW1): on the lens lips z = r e^{+-i theta} in |z| <= delta,  |G(z)^2/Lambda(z) - 1| <= C/log N, uniformly in r.
Also prints G_+G_-/Lambda on the band (must be 1: sanity of the Szego normalization)."""
import mpmath as mp
mp.mp.dps = 30
SEVEN8 = mp.mpf(7) / 8
bh = mp.pi ** 2 / 4

def x_of_t(t):
    g = 2 * mp.pi * mp.e * mp.exp(mp.re(mp.lambertw((t - mp.mpf(1) / 2 - SEVEN8) / mp.e)))
    return 1 / (g * g + mp.mpf(1) / 4)

def run(N):
    s = 1 / x_of_t(mp.mpf(N))
    Lam = lambda z: mp.log(mp.sqrt(s / z - mp.mpf(1) / 4) / (2 * mp.pi))
    # substitution x = bh sin^2(u/2): dx/sqrt(x(bh-x)) = du, u in (0, pi)
    def logG(z, extra=()):
        f = lambda u: mp.log(Lam(bh * mp.sin(u / 2) ** 2)) / (z - bh * mp.sin(u / 2) ** 2)
        br = sorted([mp.mpf(0)] + [mp.mpf(10) ** (-k) for k in range(12, 0, -1)] + [mp.mpf("0.3"), mp.mpf(1), mp.mpf(2),
                    mp.pi - mp.mpf("0.3"), mp.pi] + list(extra))
        I = mp.quad(f, br)
        R = mp.sqrt(z) * mp.sqrt(z - bh)
        return R / (2 * mp.pi) * I
    out = []
    for th in (mp.pi / 3, mp.pi / 6):
        worst = 0
        for k in range(0, 13):
            r = mp.mpf(10) ** (-k) * mp.mpf("0.5")
            z = r * mp.exp(1j * th)
            d = abs(mp.exp(2 * logG(z)) / Lam(z) - 1)
            worst = max(worst, d)
        out.append(worst)
    # band sanity at x = 0.3: G+ G- / Lambda
    x0 = mp.mpf("0.3"); eps = mp.mpf("1e-8")
    u0 = 2 * mp.asin(mp.sqrt(x0 / bh))
    ex = [u0 + d for d in (-mp.mpf("1e-4"), -mp.mpf("1e-6"), -mp.mpf("1e-8"), 0, mp.mpf("1e-8"), mp.mpf("1e-6"), mp.mpf("1e-4"))]
    gp, gm = mp.exp(logG(x0 + 1j * eps, ex)), mp.exp(logG(x0 - 1j * eps, ex))
    san = abs(gp * gm / Lam(x0) - 1)
    LN = mp.log(N)
    print(f"N=1e{int(mp.log10(N)):2d}  sup|G^2/Lam-1| lip pi/3: {mp.nstr(out[0],4):>10}  (x logN: {mp.nstr(out[0]*LN,4)})"
          f"   lip pi/6: {mp.nstr(out[1],4):>10}  (x logN: {mp.nstr(out[1]*LN,4)})   band G+G-/Lam-1 (eps=1e-8): {mp.nstr(san,2)}", flush=True)

for e in (2, 3, 4, 6, 9, 12):
    run(mp.mpf(10) ** e)
