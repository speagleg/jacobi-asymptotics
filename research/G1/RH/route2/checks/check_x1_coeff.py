"""Plan 54 (NUMERICAL): the pointwise law at p = 1 for w = k^{-r} Psi(k), r in {2, 2.5, 3}, x_k = 1/k (ROUTE2_xframe1.md §5).
r = 2 is GAP-int (alpha_x = 0); r = 2.5 (alpha_x = 1/2) is inside Theorem RII_x1 directly; r = 3 (alpha_x = 1) is reached only
through the Christoffel step (SH) from r = 2.
Psi in {A: exp sqrt(log(k + e)) (satisfies (H_an^x1) directly),
        B: exp(sqrt(log(k + e)) * (1 + sin(log log(k + e))/2)) (oscillating, D(gamma) = infinity; RedA's smoothing is not applied)}.
Measure: atoms 1/k (k <= K) with masses k^{-r} Psi(k), plus the Gauss-Legendre (log panels, ratio rho, g points) quadrature of
int_{K+1/2}^{tend} t^{-r} Psi(t) delta_{1/t} dt (Euler-Maclaurin continuation; as check_r2p1_coeff.py).  c(1) = 1/2.
Columns: nB := n (n b_n/c - 1), E := n (a_n/(2 b_n) - 1) (both O(1) under an O(1/n) law), and the pure-power value of nB.
Truncation tests: K = 1e5, 2e5, 4e5 with tend = 1e16 (K-doubling), and K = 2e5 with tend = 1e14 and with (rho, g) = (1.01, 12).
"spread" = max - min over the five runs.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan54/research/G1/RH/route2/checks/check_x1_coeff.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

c = 0.5
NS = (50, 100, 200, 400, 800)
RUNS = [(100_000, 1e16, 1.02, 8), (200_000, 1e16, 1.02, 8), (400_000, 1e16, 1.02, 8),
        (200_000, 1e14, 1.02, 8), (200_000, 1e16, 1.01, 12)]
PSI = {"A": lambda k: np.sqrt(np.log(k + np.e)),
       "B": lambda k: np.sqrt(np.log(k + np.e)) * (1 + 0.5 * np.sin(np.log(np.log(k + np.e))))}


def measure(K, tend, rho, g, logw):
    k = np.arange(1, K + 1, dtype=float)
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(rho))
    gx, gw = np.polynomial.legendre.leggauss(g)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * gx for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    lw_atoms, lw_tail = logw(k), logw(T) + np.log(W * T)
    m = max(lw_atoms.max(), lw_tail.max())
    return DiscreteMeasure.from_atoms(1 / k, np.exp(lw_atoms - m), tail=(1 / T, np.exp(lw_tail - m)))


def coeffs(run, logw, N):
    r = jacobi_coeffs(measure(*run, logw), N, prec="ld")
    return np.sqrt(np.asarray(r.b2, float)), np.asarray(r.a, float)


if __name__ == "__main__":
    for name, lpsi in PSI.items():
        for r in (2.0, 2.5, 3.0):
            table = {n: [] for n in NS}
            for run in RUNS:
                bw, aw = coeffs(run, lambda k: -r * np.log(k) + lpsi(k), 802)
                bv, _ = coeffs(run, lambda k: -r * np.log(k), 802)
                for n in NS:
                    table[n].append((n * (n * bw[n - 1] / c - 1), n * (aw[n] / (2 * bw[n]) - 1), n * (n * bv[n - 1] / c - 1)))
            print(f"Psi {name}, r = {r} (alpha_x = {r - 2:+.1f})")
            for n in NS:
                A = np.array(table[n]); sp = A.max(0) - A.min(0)
                nB, E, nBv = A[2]
                print(f"  n={n:4d}: nB={nB:+.4f} (pure power {nBv:+.4f})  E={E:+.4f}   spread: nB {sp[0]:.1e}, E {sp[1]:.1e}",
                      flush=True)
