"""Plan E2 (E2_pgt1.md §1, NUMERICAL): d2 fitted from the Plan 62 quad-precision coefficients (so_coeffs / so_fit, nmax = 1600,
K = 100 nmax, tail-corrected measure; fits over J = 4..7 terms of {n^{-1-i-jp}} and windows [f nmax, nmax], f = 0.1, 0.2, 0.3),
compared with the closed form of Theorem E2.1,
  d2 = (p+1)(s-1)^2/(8p) - (p+2)(s-1-p)^2/(8p^2) + (p+1)/12        (p > 1),
and, at p = 1 (outside Theorem E2.1; recorded for Remark E2.9), the same plus kappa_1 = 2 c(1) zeta(-1) = -1/12."""
from so_coeffs import coeffs
from so_fit import sequences, first_coef

NMAX = 1600
d2f = lambda p, s: (p + 1) * (s - 1) ** 2 / (8 * p) - (p + 2) * (s - 1 - p) ** 2 / (8 * p * p) + (p + 1) / 12
print(f"{'p':>4} {'s':>4} | {'d2 (fit)':>13} {'half-range':>10} | {'closed form':>13} | {'diff':>9} | pass")
npass = ntot = 0
for p in (1.0, 1.5, 2.0, 3.0, 4.0):
    for s in (1.5, 2.0, 3.0, 4.0, 5.0):
        al, b = coeffs(p, s, 100 * NMAX, NMAX)
        n, y, *_ = sequences(p, al, b)
        est, hr, _ = first_coef(n, y, p, which=("", 2))
        cf = d2f(p, s) - (1 / 12 if p == 1 else 0)
        ok = abs(est - cf) <= max(3 * hr, 1e-9)
        npass += ok; ntot += 1
        print(f"{p:4} {s:4} | {est:+13.8f} {hr:10.1e} | {cf:+13.8f} | {est - cf:+9.1e} | {ok}")
print(f"{npass}/{ntot} within 3x fit half-range")
