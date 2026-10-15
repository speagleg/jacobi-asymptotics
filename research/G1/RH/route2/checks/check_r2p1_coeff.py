"""Plan 50 (NUMERICAL): the pointwise law for p = 1, w = k^{-s} Psi, Psi(k) = exp(L(log k)), L(u) = sqrt(log(e^u + e))
(Psi1 = Psi satisfies (H_an1) of ROUTE2_p1.md §2 directly), s in {1.5, 2}.  s = 1.5 (a = 0) is inside Theorem RII_1
(1 < s < 2); s = 2 (a = 1/2) is GAP-int (ROUTE2_p1 §6): it is NOT covered by RII_1 nor by Corollary CT.
Measure: atoms 1/k (k <= K) with masses k^{-s} Psi(k), plus a Gauss-Legendre (log panels, ratio rho, g points) quadrature of
int_{K+1/2}^{tend} t^{-s} Psi(t) delta_{1/t} dt (Euler-Maclaurin continuation of the atom sum, as RH/checks/check_fine.py).
Index convention: b_n couples p_{n-1}, p_n (b_n^2 = b2[n-1]); a_n = a[n]; c(1) = 1/2.
Columns:
  nB := n (n b_n(w)/c - 1)                 (Theorem RII_1 for s = 1.5: O(1); the law: nB/n -> 0)
  E  := n (a[n]/(2 sqrt(b2[n])) - 1)       (pairing of RH/checks/check_fine.py; RII_1: O(1))
  T  := n (b_n(w)/b_n(v) - 1)/theta_n,     v = k^{-s}, theta_n = L'(log n)  (tilt law, CONJECTURE: -> 1/2)
  R  := n (b_n(w)/b_n(v_sig) - 1)/theta_n, v_sig = k^{-(s - theta_n)}   (drifting-order model residual)
Truncation tests (REVIEW_RH1r F10: K-doubling with the same tail agrees almost by construction, so two independent
variations are added): (A) K = 1e5, 2e5, 4e5 with tend = 1e16, rho = 1.02, g = 8; (B) K = 2e5 with tend = 1e14 and with
(rho, g) = (1.01, 12).  Printed "spread" = max - min over the five runs.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan50/research/G1/RH/route2/checks/check_r2p1_coeff.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

p, c = 1.0, 0.5
L = lambda u: np.sqrt(np.log(np.exp(u) + np.e))  # noqa: E731
dL = lambda u: np.exp(u) / (2 * (np.exp(u) + np.e) * np.sqrt(np.log(np.exp(u) + np.e)))  # noqa: E731
NS = (50, 100, 200, 400, 800)
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
    for s in (1.5, 2.0):
        table = {n: [] for n in NS}
        for run in RUNS:
            bw, aw = coeffs(run, lambda k: -s * np.log(k) + L(np.log(k)), 802)
            bv, _ = coeffs(run, lambda k: -s * np.log(k), 802)
            for n in NS:
                th = dL(np.log(n)); sig = s - th
                bs, _ = coeffs(run, lambda k: -sig * np.log(k), n + 2)
                nB = n * (n * bw[n - 1] / c - 1); E = n * (aw[n] / (2 * bw[n]) - 1)
                nBv = n * (n * bv[n - 1] / c - 1)
                T = n * (bw[n - 1] / bv[n - 1] - 1) / th; R = n * (bw[n - 1] / bs[n - 1] - 1) / th
                table[n].append((nB, E, T, R, nBv))
        print(f"s = {s} (a = {s - 1.5:+.2f}); runs (K, tend, rho, g) = {RUNS}")
        for n in NS:
            A = np.array(table[n]); sp = A.max(0) - A.min(0)
            nB, E, T, R, nBv = A[2]
            print(f"  n={n:4d}: theta={dL(np.log(n)):.4f}  nB={nB:+.4f} (pure power {nBv:+.4f})  E={E:+.4f}  T={T:.4f}  "
                  f"R={R:+.4f}   spread: nB {sp[0]:.1e}, E {sp[1]:.1e}, T {sp[2]:.1e}, R {sp[3]:.1e}", flush=True)
