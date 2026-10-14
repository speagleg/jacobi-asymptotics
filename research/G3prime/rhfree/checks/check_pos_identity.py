"""Plan 20 F1: NUMERICAL check of the elementary identity behind F ≥ 0 (any window):
(2/π)∫_ℝ g_ζ(t)·conj(g_ζ′(t)) dt = 4/(4 − (ζ + conj ζ′)²), g_ζ(t) := 1/(1 − (ζ − it)²), for |Re ζ|, |Re ζ′| < ½."""
import mpmath as mp
mp.mp.dps = 30
rng = __import__('random').Random(21)
worst = 0
for _ in range(25):
    z1 = mp.mpc(rng.uniform(-.45, .45), rng.uniform(-3, 3)); z2 = mp.mpc(rng.uniform(-.45, .45), rng.uniform(-3, 3))
    g = lambda z, t: 1 / (1 - (z - 1j * t) ** 2)
    I = 2 / mp.pi * mp.quad(lambda t: g(z1, t) * mp.conj(g(z2, t)), [-mp.inf, -10, 0, 10, mp.inf])
    rhs = 4 / (4 - (z1 + mp.conj(z2)) ** 2)
    worst = max(worst, abs(I - rhs) / abs(rhs))
print(f"25 random (ζ, ζ′) with |Re| < 0.45: max relative error {mp.nstr(worst, 3)}")
