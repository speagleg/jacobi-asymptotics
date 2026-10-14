"""Plan 48 (NUMERICAL): Lemma RedA (smoothing reduction), ROUTE2.md §1.
L := piecewise-linear interpolant of tau -> log Psi(e^tau) at the nodes tau = log k (k >= 1; constant log Psi(1) for tau < 0),
L1 := L * phi (standard Gaussian), Psi1(k) := exp L1(log k).
For complex u = tau + i sigma:  L1(u)  = e^{sigma^2/2} int L(tau - z) phi(z) e^{-i sigma z} dz,
                                L1'(u) = -e^{sigma^2/2} int L(tau - z) (z + i sigma) phi(z) e^{-i sigma z} dz
(substitute y = tau - z in int L(y) phi^{(j)}(u - y) dy).  Trapezoid on z in [-14, 14], 56001 points.
Examples: "sqrt": log Psi(k) = sqrt(log(k+e));  "osc": log Psi(k) = sqrt(log k + 1)*sin(log(log k + 1)) (D(gamma) = inf,
oscillating, cf. outline B3).
[1] e_n := max_{k in sample, k >= n} |log Psi(k) - L1(log k)|  (RedA (i): -> 0).
[2] eta(T) := max over tau in [T, T+25], |sigma| <= pi/2 (p = 2: the strip |Im u| <= pi/p) of |L1'(tau+i sigma)| (RedA (ii)).
[3] p = s = 2, long double RKPW, K = 120000: |beta_n(v Psi)/beta_n(v Psi1) - 1| and n^p|a_n(v Psi) - a_n(v Psi1)|/c (RedA (iii)).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan48/research/G1/RH/route2/checks/check_r2_redA.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

LOGPSI = {"sqrt": lambda k: np.sqrt(np.log(k + np.e)),
          "osc": lambda k: np.sqrt(np.log(k) + 1) * np.sin(np.log(np.log(k) + 1))}
Z = np.linspace(-14, 14, 56001); DZ = Z[1] - Z[0]; PHI = np.exp(-Z ** 2 / 2) / np.sqrt(2 * np.pi)


def Lint(lp, y):
    """piecewise-linear interpolant of log Psi(e^y) at the nodes y = log k."""
    y = np.asarray(y, float); out = np.full(y.shape, lp(1.0))
    m = (y > 0) & (y <= 34); ym = y[m]; k = np.floor(np.exp(ym)); k = np.maximum(k, 1.0)
    t0 = np.log(k); lam = np.clip((ym - t0) / np.log1p(1 / k), 0, 1)
    out[m] = (1 - lam) * lp(k) + lam * lp(k + 1)
    big = y > 34  # k > 5.8e14: k+1 is not resolved in float; the interpolant equals log Psi(e^y) to O(|L''|/k^2) < 1e-28
    out[big] = lp(np.exp(y[big]))
    return out


def L1(lp, tau, sig=0.0, deriv=0):
    Lv = Lint(lp, tau - Z); osc = np.exp(sig ** 2 / 2 - 1j * sig * Z) * PHI
    if deriv == 0:
        return (Lv * osc).sum() * DZ
    return -(Lv * (Z + 1j * sig) * osc).sum() * DZ


print("[1] RedA (i): e_n = max_{k>=n} |log Psi(k) - L1(log k)| (k sampled log-uniformly up to 1e14)", flush=True)
ks = np.unique(np.round(np.logspace(0, 14, 1400)))
for name, lp in LOGPSI.items():
    err = np.array([abs(lp(k) - L1(lp, np.log(k)).real) for k in ks])
    row = [f"n=1e{e}: {err[ks >= 10 ** e].max():.3e}" for e in (2, 4, 6, 8, 10, 12)]
    print(f"  {name:4s}: " + ", ".join(row), flush=True)

print("[2] RedA (ii): eta(T) = max_{tau in [T,T+25], |sigma|<=pi/2} |L1'(tau + i sigma)|; compare max_{tau>=T}|L'| (smooth L)", flush=True)
for name, lp in LOGPSI.items():
    row = []
    for T in (5, 10, 20, 40):
        taus = np.linspace(T, T + 25, 126); sigs = np.linspace(-np.pi / 2, np.pi / 2, 9)
        eta = max(abs(L1(lp, t, sg, 1)) for t in taus for sg in sigs)
        h = 1e-4; Ls = lambda t: lp(np.exp(t))  # noqa: E731 (smooth reference: derivative of the un-interpolated L)
        ref = max(abs((Ls(t + h) - Ls(t - h)) / (2 * h)) for t in taus)
        row.append(f"T={T}: eta={eta:.4f} (sup|L'|={ref:.4f})")
    print(f"  {name:4s}: " + " | ".join(row), flush=True)

print("[3] RedA (iii): p = s = 2, K = 120000, long double RKPW; Psi vs Psi1 (should -> 0)", flush=True)
p, s, K = 2.0, 2.0, 120000
k = np.arange(1, K + 1, dtype=float)
for name, lp in LOGPSI.items():
    l1 = np.array([L1(lp, np.log(kk)).real for kk in k[:20000]])
    tail = lp(k[20000:])  # for k > 2e4, |log Psi - L1| < 1e-6 (see [1]); use log Psi there (difference below printed digits)
    res = {}
    for tag, lw in (("Psi", -s * np.log(k) + lp(k)), ("Psi1", -s * np.log(k) + np.concatenate([l1, tail]))):
        lw = lw - lw.max(); r = jacobi_coeffs(DiscreteMeasure(k ** -p, np.exp(lw)), 801, prec="ld")
        res[tag] = (np.sqrt(np.asarray(r.b2, float)), np.asarray(r.a, float))
    row = []
    for n in (25, 50, 100, 200, 400, 800):
        db = res["Psi"][0][n - 1] / res["Psi1"][0][n - 1] - 1
        da = n ** p * abs(res["Psi"][1][n] - res["Psi1"][1][n]) / c_p(p)
        row.append(f"n={n}: {db:+.2e}/{da:.2e}")
    print(f"  {name:4s} (beta ratio - 1 / n^p|da|/c): " + ", ".join(row), flush=True)
