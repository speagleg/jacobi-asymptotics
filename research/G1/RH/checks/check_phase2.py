"""Plan 10 Phase 2 (NUMERICAL).  mu*_sym = int_0^1 arcsine[-rho_t, rho_t] dt, rho_t = r* t^{-q}, r* = 2^{1+q} sqrt(c(p)).
g'(z) = int_0^1 dt / sqrt(z^2 - rho_t^2)  (branch ~ 1/z at infinity), g(z) = int log(z - y) dmu*_sym(y).
[1] p = 1: our density psi vs WLXZ (2.1) closed form, and our g' vs WLXZ (4.2) (C_+ branch).
[2] density psi = (constraint) on |x| > r*, < constraint on |x| < r*; constraint density from node counting:
    nodes Z_k = (k/N)^{-q}, each of mass 1/N: (1/q)|x|^{-1-1/q} on each side (WLXZ p=1: 2/|x|^3).
[5] Re phi~ on the saturated part (phi~ = phi -+ i theta/N, continuous across it): Re phi~(x) = l/2 - Re g(x) < 0.
[3] g_+ + g_- - l = 2 Re g(x) - l: = 0 on band, > 0 on saturated part (l from x = 0+).
[4] lens sign chart: Re phi(z), phi := l/2 - g, at points just above/below the band: sign must be constant (> 0)."""
import numpy as np
import mpmath as mp
from jacobi_asym.laws.weyl import c_p

mp.mp.dps = 25


def setup(p):
    q = mp.mpf(p) / 2
    rs = 2 ** (1 + q) * mp.sqrt(c_p(p))
    return q, rs


def psi(x, p):
    q, rs = setup(p)
    x = abs(mp.mpf(x))
    tx = (rs / x) ** (1 / q)
    top = min(mp.mpf(1), tx)
    return mp.quad(lambda t: 1 / mp.sqrt((rs * t ** (-q)) ** 2 - x ** 2), [0, top]) / mp.pi


def constraint(x, p):
    q, _ = setup(p)
    return abs(mp.mpf(x)) ** (-1 - 1 / q) / q       # N nodes chosen, mass 1/N each: density (1/q)|x|^{-1-1/q} per side


def gprime(z, p):
    q, rs = setup(p)
    f = lambda t: 1 / (z * mp.sqrt(1 - (rs * t ** (-q) / z) ** 2))
    return mp.quad(f, [0, 1])


def g(z, p):
    q, rs = setup(p)
    G = lambda t: mp.log((z + z * mp.sqrt(1 - (rs * t ** (-q) / z) ** 2)) / 2)
    return mp.quad(G, [0, 1])


# [1] p = 1 vs WLXZ
wl = lambda x: (4 * mp.atan(abs(x) / mp.sqrt(4 - x * x)) / abs(x) ** 3 - mp.sqrt(4 - x * x) / x ** 2) / mp.pi if abs(x) < 2 else 2 / abs(x) ** 3
print("[1] p=1 density ours vs WLXZ(2.1): " + "  ".join(f"x={x}: {mp.nstr(psi(x,1),10)}/{mp.nstr(wl(mp.mpf(x)),10)}" for x in ["0.3", "1.1", "1.9", "2.5", "5"]))
wlgp = lambda z: 4 / z ** 3 * mp.log(z + mp.sqrt(z * z - 4)) + mp.sqrt(z * z - 4) / z ** 2 - 4 * mp.log(2) / z ** 3 - 2j * mp.pi / z ** 3
for z in [mp.mpc(3, 1), mp.mpc(0.5, 0.7), mp.mpc(-1.5, 2)]:
    print(f"    g'({z}): ours {mp.nstr(gprime(z,1),10)}   WLXZ(4.2) {mp.nstr(wlgp(z),10)}")
for p in [1, 2, 3]:
    q, rs = setup(p)
    print(f"p={p}: r*={mp.nstr(rs,8)}")
    r2 = [mp.nstr(psi(x, p) / constraint(x, p), 6) for x in [rs * f for f in (0.2, 0.6, 0.95, 1.05, 2, 10)]]
    print("   [2] psi/constraint at x/r* = .2,.6,.95,1.05,2,10: " + " ".join(r2))
    eps = mp.mpf("1e-12")
    l = 2 * mp.re(g(mp.mpc(rs * mp.mpf("0.01"), eps), p))
    vals = [2 * mp.re(g(mp.mpc(rs * f, eps), p)) - l for f in (0.3, 0.7, 0.99, 1.01, 1.5, 4)]
    print("   [3] 2Re g - l at x/r* = .3,.7,.99 | 1.01,1.5,4: " + " ".join(mp.nstr(v, 3) for v in vals))
    sg = [mp.nstr(mp.re(l / 2 - g(mp.mpc(rs * f, s * 0.05), p)), 3) for f in (0.2, 0.5, 0.9) for s in (1, -1)]
    print("   [4] Re phi just above/below band (x/r* = .2,.5,.9; y = +-0.05): " + " ".join(sg))

for p in [1, 2, 3]:
    q, rs = setup(p)
    eps = mp.mpf("1e-12")
    l = 2 * mp.re(g(mp.mpc(rs * mp.mpf("0.01"), eps), p))
    print(f"p={p} [5] l/2 - Re g on saturated part x/r* = 1.05, 2, 10: " + " ".join(mp.nstr(l / 2 - mp.re(g(mp.mpc(rs * f, eps), p)), 3) for f in (1.05, 2, 10)))
