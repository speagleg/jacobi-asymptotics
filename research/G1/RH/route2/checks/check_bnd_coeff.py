"""Plan 53 (NUMERICAL): the pointwise law at p = 1 on the boundary r = 2 (a = 1/2, alpha_x = 0) and beyond, for
w = k^{-r} Psi, Psi(k) = exp(L(log k)), L(u) = sqrt(log(e^u + e)) (Psi satisfies (H_an1) of ROUTE2_p1.md §2; D(gamma) = inf).
r = 2 is GAP-int of ROUTE2_p1 §7 (closed by Theorem RII1^f of ROUTE2_bnd.md); r = 2.5 (alpha_x = 1/2) is in the new range
1 < r < 3 of RII1^f; r = 3 (alpha_x = 1) is outside RII1^f and reached from r = 2 by one Christoffel step (SH-r).
Measure model (as check_r2p1_coeff.py): atoms 1/k (k <= K) with masses k^{-r} Psi(k), plus a Gauss-Legendre quadrature
(log panels, ratio rho, g points) of int_{K+1/2}^{tend} t^{-r} Psi(t) delta_{1/t} dt.
Index convention: b_n couples p_{n-1}, p_n (b_n = b[n-1]); a_n = a[n]; c(1) = 1/2.
Columns:
  nB := n (n b_n(w)/c - 1)            (RII1^f: O(1))
  E  := n (a_n/(2 b_n) - 1)           (RII1^f: O(1); pairing of RH/checks/check_fine.py)
  nBv: the same for the pure power v = k^{-r} (RH1(r))
  T  := n (b_n(w)/b_n(v) - 1)/theta_n, theta_n = L'(log n)   (tilt ratio; CONJECTURE -> 1/2)
Truncations: K-doubling K = 1e5, 2e5, 4e5 (tend = 1e16, rho = 1.02, g = 8) and two variations independent of K-doubling
(REVIEW_RH1r F10): K = 2e5 with tend = 1e14; K = 2e5 with (rho, g) = (1.01, 12). "spread" = max - min over the five runs;
"Kd" = |value(K=4e5) - value(K=2e5)| (the K-doubling difference).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan53/research/G1/RH/route2/checks/check_bnd_coeff.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

c = 0.5
L = lambda u: np.sqrt(np.log(np.exp(u) + np.e))  # noqa: E731
dL = lambda u: np.exp(u) / (2 * (np.exp(u) + np.e) * np.sqrt(np.log(np.exp(u) + np.e)))  # noqa: E731
NS = (50, 100, 200, 400, 800, 1600)
NMAX = max(NS) + 2
RUNS = [(100_000, 1e16, 1.02, 8), (200_000, 1e16, 1.02, 8), (400_000, 1e16, 1.02, 8),
        (200_000, 1e14, 1.02, 8), (200_000, 1e16, 1.01, 12)]


def measure(K, tend, rho, g, logw):
    k = np.arange(1, K + 1, dtype=float)
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(rho))
    gx, gw = np.polynomial.legendre.leggauss(g)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * gx for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    lw_atoms, lw_tail = logw(k), logw(T) + np.log(W * T)  # dt = T dU
    m = max(lw_atoms.max(), lw_tail.max())
    return DiscreteMeasure.from_atoms(1 / k, np.exp(lw_atoms - m), tail=(1 / T, np.exp(lw_tail - m)))


def coeffs(run, logw, N):
    r = jacobi_coeffs(measure(*run, logw), N, prec="ld")
    return np.sqrt(np.asarray(r.b2, float)), np.asarray(r.a, float)


if __name__ == "__main__":
    for r in (2.0, 2.5, 3.0):
        table = {n: [] for n in NS}
        for run in RUNS:
            bw, aw = coeffs(run, lambda k: -r * np.log(k) + L(np.log(k)), NMAX)
            bv, _ = coeffs(run, lambda k: -r * np.log(k), NMAX)
            for n in NS:
                th = dL(np.log(n))
                nB = n * (n * bw[n - 1] / c - 1); E = n * (aw[n] / (2 * bw[n]) - 1)
                nBv = n * (n * bv[n - 1] / c - 1); T = n * (bw[n - 1] / bv[n - 1] - 1) / th
                table[n].append((nB, E, T, nBv))
        print(f"r = {r} (a = {r - 1.5:+.2f}, alpha_x = {r - 2:+.2f}); runs (K, tend, rho, g) = {RUNS}")
        for n in NS:
            A = np.array(table[n]); sp = A.max(0) - A.min(0); kd = np.abs(A[2] - A[1])
            nB, E, T, nBv = A[2]
            print(f"  n={n:5d}: theta={dL(np.log(n)):.4f}  nB={nB:+.4f} (pure power {nBv:+.4f})  E={E:+.4f}  T={T:.4f}"
                  f"   spread: nB {sp[0]:.1e}, E {sp[1]:.1e}, T {sp[2]:.1e}   Kd: nB {kd[0]:.1e}, E {kd[1]:.1e}",
                  flush=True)
