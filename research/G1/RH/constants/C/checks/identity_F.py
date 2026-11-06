"""Check (Rule N, NUMERICAL): Lemma 2 (the outer-constant identity) for Paper II's own outer scalar F.

  X_n := |F(inf)|^2 * G_n,   G_n := exp( mean_arc log H_n ),  mean_arc = (1/pi) int_0^{4c} . dx/sqrt(x(4c-x)).
Lemma 2 claims  log X_n = -log c - 2np - M_n + S_n  (computed F-free in xn_freeform.py).

p = 1: F = D K, |F(inf)|^2 = 1/(2 pi n), H_n = exp(2 j(n/x))       (Paper II Lemma 5.1)
p = 2: F = D B K with the Binet-cut scalar B (Paper II Lemma A.1):
  log|F(inf)| = -1/2 log(2 pi n) - (1/2 - 1/(2p)) log 2 + (1/(2 pi)) int_{-inf}^0 b0(y)/(y-1) dy
  (derived in C.md, Step 3 of Remark 2.3), H_n = (D~ B)^{-2}, log B(x) = -(1/2pi) int b(y)[1/(y-x) - 1/(y-1)] dy.
"""
import mpmath as mp
from xn_freeform import cp, S_n, M_n

mp.mp.dps = 20


def j(t):
    # Binet's function; for |t| >= 30 use the Stirling series (DLMF 5.11.1) to avoid cancellation
    if abs(t) >= 30:
        B = [mp.mpf(1) / 6, -mp.mpf(1) / 30, mp.mpf(1) / 42, -mp.mpf(1) / 30, mp.mpf(5) / 66, -mp.mpf(691) / 2730]
        return sum(B[k] / ((2 * k + 2) * (2 * k + 1) * t ** (2 * k + 1)) for k in range(6))
    return mp.loggamma(t) - (t - mp.mpf(1) / 2) * mp.log(t) + t - mp.log(2 * mp.pi) / 2


def arcmean(f, c):
    # (1/pi) int_0^{4c} f(x) dx / sqrt(x(4c-x)),  x = 2c(1 - cos psi)
    return mp.quad(lambda ps: f(4 * c * mp.sin(ps / 2) ** 2), [0, mp.pi / 8, mp.pi / 2, mp.pi]) / mp.pi


def logX_p1(n):
    c = mp.mpf(1) / 2
    return -mp.log(2 * mp.pi * n) + arcmean(lambda x: 2 * j(n / x), c)


def logX_pgt1(p, n):
    p = mp.mpf(p)
    c = mp.mpf(cp(float(p)))
    binf = mp.pi / p - mp.pi

    def b(y):  # y < 0
        tp = n * (-y) ** (-1 / p) * mp.expjpi(-1 / p)
        e = -2j * mp.pi * tp
        L = 0 if mp.re(e) < -200 else mp.log(1 - mp.exp(e))
        return 2 * mp.im(-j(tp) - L)

    # nodes for quadrature in y: scale |y| ~ n^p
    pts = [-mp.inf, -100 * n ** p, -n ** p, -mp.mpf(n) ** p / 100, -1, -mp.mpf(1) / 100, 0]
    b0int = mp.quad(lambda y: (b(y) - (binf if y < -1 else 0)) / (y - 1), pts)
    logFinf = -mp.log(2 * mp.pi * n) / 2 - (mp.mpf(1) / 2 - 1 / (2 * p)) * mp.log(2) + b0int / (2 * mp.pi)

    def logB(x):
        return -mp.quad(lambda y: b(y) * (1 / (y - x) - 1 / (y - 1)), pts) / (2 * mp.pi)

    # log H_n(x) = 2 j(t(x)) - 2 log B(x), t(x) = n x^{-1/p}
    mean = arcmean(lambda x: 2 * j(n * x ** (-1 / p)) - 2 * logB(x), c)
    return 2 * logFinf + mean, logFinf


if __name__ == "__main__":
    print("p=1")
    for n in [10, 20, 40]:
        S, _ = S_n(1.0, n)
        M, _ = M_n(1.0, n)
        free = -mp.log(0.5) - 2 * n - M + S
        viaF = logX_p1(n)
        print(f"  n={n}: via F = {mp.nstr(viaF, 12)}   F-free = {mp.nstr(free, 12)}   diff = {mp.nstr(viaF - free, 3)}")
    for p in [2.0, 3.0]:
        print(f"p={p}")
        for n in [10, 20]:
            S, _ = S_n(p, n)
            M, _ = M_n(p, n)
            c = cp(p)
            free = -mp.log(c) - 2 * n * p - M + S
            viaF, lF = logX_pgt1(p, n)
            print(f"  n={n}: via F = {mp.nstr(viaF, 12)}   F-free = {mp.nstr(free, 12)}   diff = {mp.nstr(viaF - free, 3)}"
                  f"   [log|F(inf)| = {mp.nstr(lF, 10)}]")
