"""G1 Rule A (NUMERICAL): [1] Lemma K identity on random u; [2] G1-T on synthetic sequences: u_j with a zero double
average that is slowly oscillating (decays), vs a fast oscillating one (u_j = (-1)^j: G(n)=O(n), yet u_j does not -> 0)
showing (T3) cannot simply be dropped; [3] Prop A1 on real Jacobi data (p=2, parity weights): min over windows of the
sine-weighted average of a/(2b), L=20."""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

rng = np.random.default_rng(0)
u = rng.normal(size=400)
G = lambda n, u: sum((n - j) * u[j - 1] for j in range(1, n))
n, h = 200, 37
lhs = G(n + h, u) - 2 * G(n, u) + G(n - h, u)
rhs = sum(max(h - abs(j - n), 0) * u[j - 1] for j in range(1, 400))
print(f"[1] kernel identity: lhs={lhs:.10f} rhs={rhs:.10f} diff={lhs-rhs:.1e}")
N = 20000
j = np.arange(1, N + 1)
for name, uu in [("slow: u_j = 1/log(j+2) (slowly oscillating, -> 0)", 1 / np.log(j + 2)), ("fast: (-1)^j", (-1.0) ** j)]:
    Gs = np.cumsum(np.cumsum(uu))  # G(n+1) = sum_{j<=n} (n+1-j) u_j
    print(f"[2] {name}: G(n)/n^2 at n=1e3,1e4,2e4: {Gs[999]/1e6:.2e} {Gs[9999]/1e8:.2e} {Gs[-1]/4e8:.2e};  u_n at n=2e4: {uu[-1]:+.3f}")
k = np.arange(1, 60001, dtype=float)
mu = DiscreteMeasure(k ** -2.0, k ** -2.0 * (2 + (-1) ** k))
jc = jacobi_coeffs(mu, 2001, prec="ld")
a, b = np.asarray(jc.a, float), np.asarray(jc.b, float)
L = 20
s = np.sin(np.pi * np.arange(1, L + 1) / (L + 1))
avg = [np.sum(a[m:m + L] / (2 * b[m:m + L]) * s ** 2) / np.sum(s ** 2) for m in range(100, 1980)]
print(f"[3] Prop A1 (p=2, parity weights, L={L}): min window average of a/(2b) over n in [100,1980] = {min(avg):.4f}"
      f" (bound 2cos(pi/(L+1))*minb/(2b) ~ {np.cos(np.pi/(L+1)):.4f}); max = {max(avg):.4f}")
