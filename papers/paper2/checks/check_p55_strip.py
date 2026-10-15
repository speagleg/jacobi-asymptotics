"""Plan 55 (NUMERICAL): the O(1/n) law at p = 2 for a factor analytic only in a THIN strip (PROOF.md §3.24).
Lambda(xi) = sqrt(xi + 1) + P(xi)/sqrt(xi + 2),  P(xi) = log(1 - q cos(2 xi)),  q = 1/cosh(0.6).
P has logarithmic branch points at xi = pi*m +- 0.3i for EVERY integer m (1 - q cos(2 xi) = 0 there), so Lambda is analytic on
{Re xi >= -1/2, |Im xi| < 0.3} and on no wider strip; on every closed substrip |Im xi| <= theta < 0.3, P and P' are bounded, so
Lambda' = O(xi^{-1/2}) -> 0, and Lambda is real on R and bounded on [-1/2, 0] x [-theta, theta]: (A_theta) holds for every
theta < 0.3. The pre-Plan-55 hypothesis (A_{pi/2}) at p = 2 (strip pi/p = pi/2) FAILS for this Lambda.
ell(k) = exp Lambda(log k) is unbounded (like exp sqrt(log k)) and carries a log-periodic oscillation of amplitude ~ 1/sqrt(log k).
Measure: x_k = k^{-2}, masses k^{-s} ell(k), atoms k <= K plus the Gauss-Legendre (log panels, ratio rho, g points) quadrature of
int_{K+1/2}^{tend} t^{-s} ell(t) delta_{t^{-2}} dt (as check_x1_coeff.py).  c(2) = pi^2/16.
Columns: nB := n (n^2 b_n/c - 1);  E := n (a_n/(2 b_n) - 1)  (pairing of Theorem 1(ii): b_n couples P_{n-1}, P_n; b_n = sqrt(b2[n-1]),
a_n = a[n]);  both O(1) under the O(1/n) law.  Pure-power column (ell = 1) for comparison.
n runs over 50 * 2^(j/4), j = 0..24 (50 ... 3200).  Truncation tests: K = 1e5, 2e5, 4e5 with tend = 1e16 (K-doubling), K = 2e5 with tend = 1e14, and (rho, g) = (1.01, 12); "spread" =
max - min over the five runs (a precision-variation diagnostic, NOT an error bound; Rule N).
Run from the repository root: .venv/bin/python research/G1/RH/route2/checks/check_p55_strip.py
(copy: papers/paper2/checks/check_p55_strip.py).  Rule N note (REVIEW_Plan55 F7): for s = 3 the five-run spread is 0 at small n,
which only shows the tail beyond K = 1e5 is invisible there; the Rule R reviewer cross-checked s = 2 at n = 50, 200, 400 with an
independent Lanczos run (double precision), identical to all printed digits."""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

p = 2.0
c = np.pi ** 2 / 16
q = 1 / np.cosh(0.6)
NS = tuple(int(round(50 * 2 ** (j / 4))) for j in range(25))  # 50 ... 3200, four points per doubling
NMAX = NS[-1] + 2
RUNS = [(100_000, 1e16, 1.02, 8), (200_000, 1e16, 1.02, 8), (400_000, 1e16, 1.02, 8),
        (200_000, 1e14, 1.02, 8), (200_000, 1e16, 1.01, 12)]


def Lam(xi):  # real argument
    return np.sqrt(xi + 1) + np.log(1 - q * np.cos(2 * xi)) / np.sqrt(xi + 2)


def measure(K, tend, rho, g, logw):
    k = np.arange(1, K + 1, dtype=float)
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(rho))
    gx, gw = np.polynomial.legendre.leggauss(g)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * gx for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    lw_atoms, lw_tail = logw(k), logw(T) + np.log(W * T)
    m = max(lw_atoms.max(), lw_tail.max())
    return DiscreteMeasure.from_atoms(k ** -p, np.exp(lw_atoms - m), tail=(T ** -p, np.exp(lw_tail - m)))


def coeffs(run, logw, N):
    r = jacobi_coeffs(measure(*run, logw), N, prec="ld")
    return np.sqrt(np.asarray(r.b2, float)), np.asarray(r.a, float)


def singularity_check():
    # 1 - q cos(2 xi) vanishes at xi = pi m + 0.3i: the strip of analyticity of Lambda is exactly |Im xi| < 0.3.
    for m in (0, 5, 50):
        xi = np.pi * m + 0.3j
        print(f"  |1 - q cos(2 xi)| at xi = pi*{m} + 0.3i: {abs(1 - q * np.cos(2 * xi)):.1e}")
    # sup |Lambda'| on Re xi = T, |Im xi| <= 0.25 (central differences), decaying like T^{-1/2}
    for T in (5.0, 50.0, 500.0):
        ys = np.linspace(-0.25, 0.25, 51); xs = T + np.linspace(0, np.pi, 201)
        Z = xs[None, :] + 1j * ys[:, None]
        h = 1e-6
        d = np.abs((lam_c(Z + h) - lam_c(Z - h)) / (2 * h))
        print(f"  sup |Lambda'| on [T, T + pi] x [-0.25, 0.25], T = {T:5.0f}: {d.max():.4f}")


def lam_c(z):  # complex argument, principal branches (no branch cut is crossed for Re z >= 0, |Im z| <= 0.25)
    return np.sqrt(z + 1) + np.log(1 - q * np.cos(2 * z)) / np.sqrt(z + 2)


if __name__ == "__main__":
    print("Singularities and epsilon_Lambda:")
    singularity_check()
    for s in (2.0, 3.0):
        table = {n: [] for n in NS}
        for run in RUNS:
            bw, aw = coeffs(run, lambda k: -s * np.log(k) + Lam(np.log(k)), NMAX)
            bv, av = coeffs(run, lambda k: -s * np.log(k), NMAX)
            for n in NS:
                table[n].append((n * (n ** p * bw[n - 1] / c - 1), n * (aw[n] / (2 * bw[n - 1]) - 1),
                                 n * (n ** p * bv[n - 1] / c - 1), n * (av[n] / (2 * bv[n - 1]) - 1)))
        print(f"p = 2, s = {s} (alpha = {(s - 1 - p) / p:+.2f})")
        for n in NS:
            A = np.array(table[n]); sp = A.max(0) - A.min(0)
            nB, E, nBv, Ev = A[1]
            print(f"  n={n:4d}: nB={nB:+.4f} (ell=1: {nBv:+.4f})  E={E:+.4f} (ell=1: {Ev:+.4f})   spread: nB {sp[0]:.1e}, E {sp[1]:.1e}",
                  flush=True)
        for lo, hi in ((50, 400), (400, 3200)):
            sel = [table[n][1] for n in NS if lo <= n <= hi]
            A = np.array(sel)
            print(f"  max over {lo} <= n <= {hi}: |nB| = {np.abs(A[:, 0]).max():.4f}, |E| = {np.abs(A[:, 1]).max():.4f}", flush=True)
