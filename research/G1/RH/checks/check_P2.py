"""RH_proof Lemma P2 (NUMERICAL): E(x,y) := -2 pi y/|z|^2 + 2 Re g(z) - l  < 0 on the strip over the band, p = 2.
Report max E over x in [-0.95 r*, 0.95 r*] (x != 0) for heights y in {0.02, 0.05, 0.1, 0.2, 0.4}, and the first-order
prediction 2 pi y (psi(x) - 1/x^2)."""
import mpmath as mp
mp.mp.dps = 20
p = 2; q = mp.mpf(1); rs = mp.pi
g = lambda z: mp.quad(lambda t: mp.log((z + z * mp.sqrt(1 - (rs * t ** (-q) / z) ** 2)) / 2), [0, 1])
psi = lambda x: mp.quad(lambda t: 1 / mp.sqrt((rs / t) ** 2 - x * x), [0, 1]) / mp.pi
l = 2 * mp.re(g(mp.mpc(rs * mp.mpf("0.01"), mp.mpf("1e-14"))))
xs = [rs * mp.mpf(k) / 20 for k in range(-19, 20) if k != 0]
for y in (0.02, 0.05, 0.1, 0.2, 0.4):
    E = [(-2 * mp.pi * y / abs(mp.mpc(x, y)) ** 2 + 2 * mp.re(g(mp.mpc(x, y))) - l, x) for x in xs]
    mx = max(E, key=lambda e: e[0])
    pred = 2 * mp.pi * y * (psi(mx[1]) - 1 / mx[1] ** 2)
    print(f"y={y}: max_x E = {mp.nstr(mx[0], 4)} at x/r* = {mp.nstr(mx[1]/rs, 3)}   first-order 2 pi y (psi - 1/x^2) there = {mp.nstr(pred, 4)}")
