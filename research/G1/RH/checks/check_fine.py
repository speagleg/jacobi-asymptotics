"""Plan 10 Phase 0 (NUMERICAL; atoms beyond K replaced by an Euler-Maclaurin quadrature tail): fine asymptotics of beta_n := n^p b_n / c(p) and r_n := a_n/(2 b_n) for
sigma_{p,s} = sum_k k^{-s} delta_{k^{-p}}.  Fit beta_n - 1 = d1/n + d2/n^2 + d3/n^3 and r_n - 1 = e1/n + ... by least
squares on n in [nlo, nhi].  Rule N: K vs 2K.  Exact anchor: Lommel nu=1/2 has atoms (k pi)^{-2} exactly, weights
prop. k^{-2} (p=2, s=2): closed-form coefficients give d1 = -1/2 (and the item-11 value e1 = +1)."""
import numpy as np
import mpmath as mp
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.measures.reference import lommel_coeffs
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p


def power_with_tail(p, s, K, ratio=1.02, k=8, tend=1e12):
    """atoms k^-p (k <= K) plus a Gauss-Legendre (log-panels) quadrature of int_{K+1/2}^inf t^-s delta_{t^-p} dt
    (midpoint/Euler-Maclaurin continuation of the atom sum beyond K)."""
    kk = np.arange(1, K + 1, dtype=float)
    x, w = kk ** -p, kk ** -s
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(ratio))
    g, gw = np.polynomial.legendre.leggauss(k)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * g for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    return DiscreteMeasure.from_atoms(x, w, tail=(T ** -p, W * T * T ** -s))


def fit(n, y, deg=3):
    A = np.vstack([n ** -k for k in range(1, deg + 1)]).T
    return np.linalg.lstsq(A, y, rcond=None)[0]


# exact anchor
N = 3000
a_ex, b2_ex = lommel_coeffs(0.5, N)
n = np.arange(1, N + 1, dtype=float)
b_ex = np.sqrt(np.array([float(v) for v in b2_ex])); a_ex = np.array([float(v) for v in a_ex])
beta = n ** 2 * b_ex * np.pi ** 2 / c_p(2.0)     # atoms (k pi)^-2: C = 1/pi^2
r = a_ex / (2 * b_ex)
m = (n >= 200)
print(f"[Lommel nu=1/2 exact] d = {np.round(fit(n[m], beta[m]-1), 4)}   e = {np.round(fit(n[m], r[m]-1), 4)}")

CASES = [(2.0, 2.0, 30_000, 1500), (2.0, 3.0, 30_000, 1500), (2.0, 4.0, 30_000, 1500), (2.0, 6.0, 30_000, 1500),
         (3.0, 3.0, 10_000, 1200), (3.0, 4.0, 10_000, 1200), (3.0, 6.0, 10_000, 1200),
         (1.5, 1.5, 50_000, 1000), (1.5, 3.0, 50_000, 1000)]
for p, s, K, nhi in CASES:
    res = []
    for KK in (K, 2 * K):
        mu = power_with_tail(p, s, KK)
        jc = jacobi_coeffs(mu, nhi + 1, prec="ld")
        a = np.asarray(jc.a, float)[:nhi]; b = np.asarray(jc.b, float)[:nhi]
        nn = np.arange(1, nhi + 1, dtype=float)
        bet = nn ** p * b / c_p(p); rr = a / (2 * b)
        mm = (nn >= 150) & (nn <= nhi)
        res.append((fit(nn[mm], bet[mm] - 1), fit(nn[mm], rr[mm] - 1)))
    (d, e), (d2, e2) = res
    print(f"p={p} s={s}: d = {np.round(d, 4)}  e = {np.round(e, 4)}   (2K: d1={d2[0]:.4f}, e1={e2[0]:.4f})")
