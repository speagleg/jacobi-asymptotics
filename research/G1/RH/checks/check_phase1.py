"""Plan 10 Phase 1 (NUMERICAL checks of the symmetrized interpolation-problem data).
Symmetric variable: atoms x_k = k^{-p} = s_k^2, s_k = k^{-q}, q = p/2; degree-N symmetric OPs (N = 2m).
Rescaled nodes Z_k = N^q s_k = (k/N)^{-q} (and -Z_k).  theta(z) := pi N (z^2)^{-1/p} (principal branch of
(z^2)^{-1/p}, cut where z^2 <= 0, i.e. on the imaginary axis), Pi := sin(theta)/theta'.
Checks: [1] theta(+-Z_k) = pi k; [2] Pi(+-Z_k) = 0 and Pi'(+-Z_k) = (-1)^k (so w e^{+-i theta}/Pi has residue w(Z_k) at
+-Z_k); [3] no other zeros of sin(theta) in the sectors |arg(+-z)| < pi/2 - eps (argument-principle count on a box);
[4] |e^{-i theta}| < 1 in the upper-right/upper-left sectors, |e^{+i theta}| < 1 in the lower ones (decay directions for
the U_+- factorizations), for p in {1, 2, 3}."""
import numpy as np
import mpmath as mp

mp.mp.dps = 30


def theta(z, N, p):
    return mp.pi * N * mp.power(z * z, -mp.mpf(1) / p)


def dtheta(z, N, p):
    return mp.diff(lambda t: theta(t, N, p), z)


def Pi(z, N, p):
    return mp.sin(theta(z, N, p)) / dtheta(z, N, p)


for p in [1, 2, 3]:
    q = mp.mpf(p) / 2
    N = 40
    worst1 = worst2 = worst3 = 0
    for k in [1, 2, 5, 17, 60]:
        for sgn in (1, -1):
            Z = sgn * mp.power(mp.mpf(k) / N, -q)
            worst1 = max(worst1, abs(theta(Z, N, p) - mp.pi * k))
            worst2 = max(worst2, abs(Pi(Z, N, p)))
            dPi = mp.diff(lambda t: Pi(t, N, p), Z)
            worst3 = max(worst3, abs(dPi - (-1) ** k))
    print(f"p={p}: max|theta(Z_k)-pi k|={mp.nstr(worst1,3)}  max|Pi(Z_k)|={mp.nstr(worst2,3)}  max|Pi'(Z_k)-(-1)^k|={mp.nstr(worst3,3)}")
    # [3] count zeros of sin(theta) in box [a,b] x [-h,h] (right half-plane, off the cut) via argument principle
    ka, kb = 300, 20                        # edges midway between nodes: theta = pi (k + 1/2)
    a = mp.power((ka + mp.mpf(1) / 2) / N, -q); b = mp.power((kb + mp.mpf(1) / 2) / N, -q); h = mp.mpf("0.2")
    f = lambda z: mp.sin(theta(z, N, p))
    df = lambda z: mp.cos(theta(z, N, p)) * dtheta(z, N, p)
    corners = [a - 1j * h, b - 1j * h, b + 1j * h, a + 1j * h, a - 1j * h]
    cnt = 0
    for i in range(4):
        pts = [corners[i] + (corners[i + 1] - corners[i]) * t for t in mp.linspace(0, 1, 400)]
        cnt += mp.quad(lambda z: df(z) / f(z), pts)
    cnt /= (2j * mp.pi)
    print(f"      zeros of sin(theta) in box (arg principle) = {mp.nstr(mp.re(cnt), 8)} (+ i {mp.nstr(mp.im(cnt), 2)})   nodes in box = {ka - kb}")
    # [4] decay directions
    for z, lab in [(1 + 0.3j, "upper-right"), (-1 + 0.3j, "upper-left"), (1 - 0.3j, "lower-right"), (-1 - 0.3j, "lower-left")]:
        th = theta(mp.mpc(z), N, p)
        print(f"      {lab:11s}: |e^(-i theta)| = {mp.nstr(abs(mp.exp(-1j * th)), 3)}   |e^(+i theta)| = {mp.nstr(abs(mp.exp(1j * th)), 3)}")
