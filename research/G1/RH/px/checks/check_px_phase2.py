"""Plan 12 Phase 2 (NUMERICAL): g-function and sign structure in x (rescaled), from G2's mu* = int_0^1 omega_{[0,beta_tau]} dtau,
beta_tau = 4c tau^{-p}.  g(z) = int_0^1 2 log((sqrt z + sqrt(z - beta_tau))/2) dtau (arcsine log-potential, branch ~ log z).
phi := l/2 - g, l := 2(log c + p) (G2 B*(ii)); phit := phi + i theta/N (C+), theta/N = pi z^{-1/p}.
 [1] U* = Re g = log c + p on the band (0,4c); U* - (log c + p) > 0 and increasing on (4c, inf)  (=> Re phit < 0 there).
 [2] psi/rho = I_{x/4c}(1/p+1/2, 1/2) < 1 on the band (closed form from G2), rho = (1/p) x^{-1-1/p}.
 [3] Lips above the band: Re phi(x+i eps) < 0 and Re phit(x+i eps) > 0 (both needed on band lips).
 [4] Above the saturated region: Re phit(x + i eps) < 0."""
import mpmath as mp

mp.mp.dps = 30
def run(p):
    p = mp.mpf(p)
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
    c = (mp.pi / (2 * I)) ** p / 4
    l = 2 * (mp.log(c) + p)
    def g(z):
        f = lambda tau: 2 * mp.log((mp.sqrt(z) + mp.sqrt(z - 4 * c * tau ** (-p))) / 2)
        return mp.quad(f, [0, mp.mpf("1e-6"), mp.mpf("0.01"), 0.5, 1])
    phi = lambda z: l / 2 - g(z)
    phit = lambda z: phi(z) + 1j * mp.pi * mp.power(z, -1 / p)
    print(f"p={p}: 4c={mp.nstr(4*c,8)}, l={mp.nstr(l,10)}")
    e = mp.mpf("1e-25")
    band = [mp.mpf(v) * 4 * c for v in ("0.01", "0.3", "0.7", "0.97")]
    sat = [mp.mpf(v) * 4 * c for v in ("1.05", "1.5", "4", "50")]
    print("  [1] U*-(log c+p):", "band", [mp.nstr(mp.re(g(x + 1j * e)) - (mp.log(c) + p), 3) for x in band],
          " sat", [mp.nstr(mp.re(g(x + 1j * e)) - (mp.log(c) + p), 4) for x in sat])
    print("  [2] psi/rho on band:", [mp.nstr(mp.betainc(1 / p + 0.5, 0.5, 0, x / (4 * c), regularized=True), 4) for x in band])
    for eps in ("1e-3", "1e-2"):
        ep = mp.mpf(eps)
        print(f"  [3] eps={eps}: Re phi(x+ie)", [mp.nstr(mp.re(phi(x + 1j * ep)), 3) for x in band],
              " Re phit(x+ie)", [mp.nstr(mp.re(phit(x + 1j * ep)), 3) for x in band])
        print(f"  [4] eps={eps}: Re phit above saturated", [mp.nstr(mp.re(phit(x + 1j * ep)), 3) for x in sat])
for p in (1.5, 2, 3):
    run(p)
