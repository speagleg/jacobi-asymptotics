"""G2 (NUMERICAL): averaged Law P statistic S_n = (2/n^2) sum (n-j) log(b_j/x_j) - log c(p) for pure powers
x_k = k^{-p}, weights k^{-s}, p not in {1,2}.  Rule N: truncation K vs 2K, and precision ld vs q (binary128)."""
import numpy as np
from jacobi_asym.measures.powers import pure_power
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.averaged import averaged_law

CASES = [(0.5, 2.0, 200_000, "d"), (1.5, 1.5, 50_000, "ld"), (3.0, 3.0, 20_000, "ld"), (4.0, 4.0, 6_000, "ld"), (6.0, 6.0, 2_000, "ld")]
for p, s, K, prec in CASES:
    ns = [n for n in (25, 50, 100, 200, 400, 800, 1600) if n <= K // 8]
    out = {}
    for KK, pr in ((K, prec), (2 * K, prec), (K, "q")):
        if pr == "q" and K > 30_000:
            continue
        mu = pure_power(p, KK, s=s)
        b = np.asarray(jacobi_coeffs(mu, max(ns), prec=pr).b, float)
        out[(KK, pr)] = averaged_law(b, mu.atoms, p, ns)
    base = out[(K, prec)]
    print(f"p={p} s={s} K={K} {prec}: S_n  " + " ".join(f"{n}:{base[n]:+.5f}" for n in ns))
    print(f"      S_n*log n            " + " ".join(f"{n}:{base[n]*np.log(n):+.4f}" for n in ns))
    for key, v in out.items():
        if key != (K, prec):
            print(f"      max|diff| vs {key}: {max(abs(v[n]-base[n]) for n in ns):.1e}")
