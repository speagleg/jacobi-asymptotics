"""G1 (NUMERICAL): pointwise regularity of Jacobi coefficients.
beta_n = n^p b_n / (c(p) C) (target 1) and a_n/(2 b_n) (target 1), for atoms x_k = k^{-p} (C=1) or the smooth zeta model,
with several weight classes. Rule N: K vs 2K for each case. Reports at log-spaced n, fitted decay exponents of the errors,
the slow-oscillation modulus omega_n(delta) = max_{n<=m<=(1+delta)n} |beta_m/beta_n - 1| (n ~ nmax/2), and the count of
monotonicity violations of b_n for n >= 50."""
import sys
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.measures.lfun import smooth_zeta
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

NMAX = 2000
NS = [50, 100, 200, 400, 800, 1600]


def measure(p, K, wkind):
    k = np.arange(1, K + 1, dtype=float)
    x = k ** -p
    s = {1.0: 2.0, 2.0: 2.0, 3.0: 3.0}[p]
    base = k ** -s
    w = {"pow": base, "pow6": k ** -6.0, "logper": base * (2 + np.sin(np.log(k))),
         "parity": base * (2 + (-1) ** k)}[wkind]
    return DiscreteMeasure(x, w), x


def run(p, K, wkind, prec="ld"):
    if wkind == "zeta":
        mu = smooth_zeta(K)
        x = mu.atoms[:K]
        C = 1.0
    else:
        mu, x = measure(p, K, wkind)
    jc = jacobi_coeffs(mu, NMAX + 1, prec=prec)
    a = np.asarray(jc.a, float); b = np.asarray(jc.b, float)
    n = np.arange(1, NMAX + 1)
    if wkind == "zeta":
        beta = b[:NMAX] / (c_p(2.0) * x[:NMAX])      # zeta: law is b_n / x_n -> c(2)
    else:
        beta = n ** p * b[:NMAX] / c_p(p)
    ratio = a[:NMAX] / (2 * b[:NMAX])
    return beta, ratio, b[:NMAX]


def fit(err):
    e = np.array([abs(err[n - 1]) for n in NS])
    m = e > 0
    return np.polyfit(np.log(np.array(NS)[m]), np.log(e[m]), 1)[0] if m.sum() > 2 else float("nan")


CASES = [(1.0, 200_000, "pow"), (1.0, 200_000, "parity"), (1.0, 200_000, "logper"),
         (2.0, 60_000, "pow"), (2.0, 60_000, "pow6"), (2.0, 60_000, "parity"), (2.0, 60_000, "logper"),
         (3.0, 20_000, "pow"), (3.0, 20_000, "parity"), (2.0, 400_000, "zeta")]
for p, K, wk in CASES:
    prec = "d" if (wk == "zeta" or p == 1.0) else "ld"
    beta, ratio, b = run(p, K, wk, prec)
    beta2, ratio2, _ = run(p, 2 * K, wk, prec)
    print(f"p={p} weights={wk} K={K} ({prec})")
    print("   beta_n-1:     " + " ".join(f"{n}:{beta[n-1]-1:+.2e}" for n in NS) + f"   decay exp {fit(beta-1):+.2f}")
    print("   a/(2b)-1:     " + " ".join(f"{n}:{ratio[n-1]-1:+.2e}" for n in NS) + f"   decay exp {fit(ratio-1):+.2f}")
    n0 = NMAX // 2
    for d in (0.1, 0.5):
        m1 = int(n0 * (1 + d))
        print(f"   omega({d}) at n={n0}: {np.max(np.abs(beta[n0-1:m1]/beta[n0-1]-1)):.2e}", end="")
    viol = int(np.sum(np.diff(b[49:]) > 0))
    print(f"   monotonicity violations (n>=50): {viol}   Rule N max|beta(K)-beta(2K)| = {np.max(np.abs(beta-beta2)):.1e}")
    sys.stdout.flush()
