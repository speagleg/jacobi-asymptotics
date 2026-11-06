"""Check (Rule N, NUMERICAL): the F-free formula for the outer-scalar constant
   log X_n = -log c - 2np - M_n + S_n
and the claims  S_n = 2np + log c - p log(2 pi n) + o(1),  M_n -> 0,  hence X_n (2 pi n)^p -> 1.

  S_n = sum_{k: X_k > 4c} 4 arccosh( sqrt(X_k/(4c)) ),  X_k = (n/k)^p
  M_n = 2 * int_{kappa0}^inf log|2 sin(pi n tau)| rho(tau) d tau,  rho = arcsine law pushed to tau = x^{-1/p}
      rho(tau) = (p/pi) tau^{-p/2-1} / sqrt(4c - tau^{-p}),  kappa0 = (4c)^{-1/p}.
M_n is computed piecewise between the log singularities tau = m/n (scipy quad, log weight handled adaptively),
up to tau = T, plus a one-step integration-by-parts tail with the Clausen antiderivative.
"""
import sys
import numpy as np
from math import gamma, pi, log, sqrt, acosh, ceil, floor
from scipy.integrate import quad
import mpmath as mp


def cp(p):
    I = sqrt(pi) / 2 * gamma(1 / p + 0.5) / gamma(1 / p + 1)
    return 0.25 * (pi / (2 * I)) ** p


def S_n(p, n):
    c = cp(p)
    tot = 0.0
    k = 1
    while True:
        X = (n / k) ** p
        if X <= 4 * c:
            break
        tot += 4 * acosh(sqrt(X / (4 * c)))
        k += 1
    return tot, k - 1


def M_n(p, n, T=None):
    c = cp(p)
    k0 = (4 * c) ** (-1 / p)
    rho = lambda t: (p / pi) * t ** (-p / 2 - 1) / sqrt(4 * c - t ** (-p))
    f = lambda t: log(abs(2 * np.sin(pi * n * t))) * rho(t)
    if T is None:
        T = max(40.0, 4 * k0)
    tot = 0.0
    # first piece: from kappa0 to first singularity above it; substitute t = k0 + u^2 to remove (t-k0)^{-1/2}
    m1 = floor(n * k0) + 1
    a = m1 / n
    g = lambda u: 2 * u * f(k0 + u * u)
    tot += quad(g, 0, sqrt(a - k0), limit=200)[0]
    m = m1
    while m / n < T:
        lo, hi = m / n, (m + 1) / n
        tot += quad(f, lo, hi, limit=100)[0]
        m += 1
    TT = m / n
    # tail: int_TT^inf l(n t) rho dt, with Lam(t)=int_0^t l = -Cl2(2 pi t)/(2 pi) (periodic, mean 0);
    # Lam(n TT)=Lam(integer)=0, so tail = -(1/n) int Lam(n t) rho'(t) dt = O(rho'(TT)/n^2): neglected, bound printed
    tail_bound = (0.1 / n ** 2) * abs(rho(TT)) * (p / 2 + 1) / TT * 2
    return 2 * tot, tail_bound


if __name__ == "__main__":
    for p in [0.5, 1.0, 2.0, 3.0]:
        c = cp(p)
        print(f"p={p}  c={c:.12f}")
        for n in [10, 20, 40, 80, 160]:
            S, Ns = S_n(p, n)
            M, tb = M_n(p, n)
            pred_S = 2 * n * p + log(c) - p * log(2 * pi * n)
            logX = -log(c) - 2 * n * p - M + S
            r = logX + p * log(2 * pi * n)
            print(f"  n={n:4d} N_s={Ns:4d}  S_n-pred={S-pred_S:+.3e}  M_n={M:+.3e}  "
                  f"log(X_n(2pi n)^p)={r:+.3e}  n*that={n*r:+.4f}  (tail<{tb:.1e})")
