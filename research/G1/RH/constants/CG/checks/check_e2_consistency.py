"""CG.md §10: consistency of Theorem A (and the index-shift form F7) with Cor E2.7's numerical slopes.

The local slopes are copied from research/G1/RH/second_order/checks/check_e2_christoffel.out (do not recompute; that file is
not ours). Cor E2.7 predicts slope -> -E. Theorem A with N = m + (s-1)/(2p) predicts, over [n, 2n],
  -E log((2n+d)/(n+d))/log 2 + O(n^-2),  d = (s-1)/(2p)   (the constant C cancels in a slope).
NUMERICAL."""
import math
data = {(1.5, 2.0): [-2.327747, -2.330534, -2.331932, -2.332632], (2.0, 2.0): [-1.996407, -1.998200, -1.999099, -1.999549],
        (2.0, 3.0): [-3.985674, -3.992812, -3.996400, -3.998198], (3.0, 2.0): [-1.664671, -1.665667, -1.666166, -1.666416]}
ns = [100, 200, 400, 800, 1600]
for (p, s), sl in data.items():
    E = (p + 2) * (s - 1) / p; d = (s - 1) / (2 * p)
    pred = [-E * math.log((ns[k + 1] + d) / (ns[k] + d)) / math.log(2) for k in range(4)]
    print(f"p={p} s={s}: E={E:.6f}; E2 slope - shifted prediction: " + " ".join(f"{a - b:+.2e}" for a, b in zip(sl, pred))
          + f" | E2 slope + E: " + " ".join(f"{a + E:+.2e}" for a in sl))
