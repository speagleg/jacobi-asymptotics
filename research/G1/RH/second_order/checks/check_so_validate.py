"""Plan 62 (NUMERICAL; SECOND.md section 1 "Validation"): the coefficient pipeline of so_coeffs.py against the exact
Lommel coefficients of sigma_{2,2} (Paper 2 Remark rem:pure-lommel): b_n = pi^2/((4n+1) sqrt((4n-1)(4n+3))),
alpha_n = 2 pi^2/((4n+1)(4n+5)) (n >= 1), alpha_0 = pi^2/15.  Max relative error over n = 1..400 (b_n) and
n = 0..399 (alpha_n), for K = 2e4 and 4e4 atoms (+ Gauss-Jacobi tail), binary128 RKPW."""
import sys
import os
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_coeffs import coeffs

mp.mp.dps = 40
pi2 = mp.pi ** 2
for K in (20000, 40000):
    al, b = coeffs(2.0, 2.0, K, 400)
    eb = max(abs(b[n - 1] / (pi2 / ((4 * n + 1) * mp.sqrt((4 * n - 1) * (4 * n + 3)))) - 1) for n in range(1, 401))
    ea = max([abs(al[0] / (pi2 / 15) - 1)] + [abs(al[n] / (2 * pi2 / ((4 * n + 1) * (4 * n + 5))) - 1) for n in range(1, 400)])
    print(f"K = {K}: max rel. error b_n = {mp.nstr(eb, 3)}, alpha_n = {mp.nstr(ea, 3)}, overall = {mp.nstr(max(ea, eb), 3)}")
