"""p = 1, r = 3/2 vs Tricomi-Carlitz (alpha = 1) (NUMERICAL).
sigma = sum_k k^{-3/2} delta_{1/k} (with Euler-Maclaurin tail) vs TC(alpha=1) in the x-variable, whose coefficients are
exact: lam(m) = 1/(m+1) (item 11: lambda_m = m/((m+alpha)(m+alpha-1)) at alpha = 1), folded:
a_j = lam(2j-2) + lam(2j-1), b_j^2 = lam(2j-1) lam(2j)  (lam(0) = 0).
[1] weight ratio ours/TC at node k: k! e^k / k^{k+1/2} -> sqrt(2 pi) (1 + 1/(12k) + ...).
[2] b_n(ours)/b_n(TC) - 1 and a_n(ours)/a_n(TC) - 1: expected O(1/n) (weight-perturbation theorem)."""
import sys
import numpy as np
import mpmath as mp
sys.path.insert(0, "research/G1/RH/checks")
from check_fine import power_with_tail
from jacobi_asym.jacobi.dispatch import jacobi_coeffs

for k in (1, 10, 100, 1000):
    rat = mp.factorial(k) * mp.e ** k / mp.power(k, k + mp.mpf(1) / 2)
    print(f"[1] k={k}: ratio = {mp.nstr(rat, 10)}   sqrt(2pi)(1+1/(12k)) = {mp.nstr(mp.sqrt(2*mp.pi)*(1+mp.mpf(1)/(12*k)), 10)}")
lam = lambda m: 0.0 if m == 0 else 1.0 / (m + 1)
M = 1500
res = {}
for K in (200_000, 400_000):
    jc = jacobi_coeffs(power_with_tail(1.0, 1.5, K), M + 1, prec="ld")
    res[K] = (np.asarray(jc.a, float)[:M], np.asarray(jc.b, float)[:M])
a, b = res[200_000]
j = np.arange(1, M + 1)
aT = np.array([lam(2 * t - 2) + lam(2 * t - 1) for t in j]); bT = np.sqrt([lam(2 * t - 1) * lam(2 * t) for t in j])
for n in (50, 100, 200, 400, 800, 1500):
    print(f"[2] n={n}: b/bTC - 1 = {b[n-1]/bT[n-1]-1:+.4e} (x n = {n*(b[n-1]/bT[n-1]-1):+.4f})   a/aTC - 1 = {a[n-1]/aT[n-1]-1:+.4e} (x n = {n*(a[n-1]/aT[n-1]-1):+.4f})")
a2, b2 = res[400_000]
print(f"    Rule N: max|b(K)-b(2K)|/b = {np.max(np.abs(b-b2)/b):.1e}")
