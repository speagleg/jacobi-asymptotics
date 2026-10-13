"""p = 1, general r (NUMERICAL; run from repo root).  sigma_r = sum_k k^{-r} delta_{1/k} with Euler-Maclaurin tail to
tend = 1e16.  Symmetric recurrence beta_N (unfolded from a_m, b_m) fitted as
   N beta_N - 1 ... more precisely  beta_N / (c(1)(N/2)^{-1}) - 1 = (k0 + k1 (-1)^N)/N + (k2 + k3 (-1)^N)/N^2.
Predictions: k0 = 1 - r - p/2 = 1/2 - r (Phase 0 + Lemma 5.1); k1 = -4 alpha, alpha = r - 3/2 (Vanlessen Thm 1.1:
interior singularity |x|^{2 lambda} at x = 0 gives a_n = 1/2 - lambda (-1)^n / n + O(n^-2) for the orthonormal
recurrence on [-1,1], i.e. beta_N relative correction -4 lambda (-1)^N / N).
NOTE (Rule R F10): the printed "pred" for k1 is that fixed-weight -4a heuristic, which the data REJECT (observed
k1 ~ -3a); it is kept only for comparison. The 2K column is not an independent stability test: with the
Euler-Maclaurin tail to 1e16, K and 2K agree by construction."""
import sys
import numpy as np
sys.path.insert(0, "research/G1/RH/checks")
from check_fine import power_with_tail
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

M = 800
for r in (1.25, 1.5, 2.0, 2.5, 3.0):
    out = []
    for K in (100_000, 200_000):
        jc = jacobi_coeffs(power_with_tail(1.0, r, K, tend=1e16), M + 2, prec="ld")
        a = np.asarray(jc.a, float); b2 = np.asarray(jc.b2, float)
        g2 = [0.0]
        for m in range(1, M + 1):
            g2.append(a[m - 1] - g2[-1]); g2.append(b2[m - 1] / g2[-1])
        N = np.arange(80, 2 * M + 1)
        kap = np.array([g2[n] / (c_p(1.0) * (n / 2.0) ** -1) - 1 for n in N])
        A = np.vstack([1 / N, (-1.0) ** N / N, 1 / N ** 2, (-1.0) ** N / N ** 2]).T
        out.append(np.linalg.lstsq(A, kap, rcond=None)[0])
    k, k2 = out
    print(f"r={r}: k0={k[0]:+.4f} (pred {0.5-r:+.4f})  k1={k[1]:+.4f} (pred {-4*(r-1.5):+.4f})   [2K: k0={k2[0]:+.4f}, k1={k2[1]:+.4f}]")
