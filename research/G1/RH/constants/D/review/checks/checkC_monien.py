# (c) A^(0) of Monien-Zagier by a direct fit of det_{1<=i,j<=n} zeta(i+j) (reviewer's own LDL code), n <= 70,
#     nothing from D.md used except the normalisation H_n = A0 ((2n+1)/e^{3/2})^{-(n+1/2)^2} (1 + sum a_k x^k), x = 1/(2n+1).
# (d) Monien's printed H_100 ~ 4.9e-16684 against both candidate A0 values (asymptotic formula, and a_2 correction).
import mpmath as mp
from hank import run
def fit(n, dps, nfit):
    Dg, y, lam, logD = run(1, 2, n, dps)       # moments zeta(2+k): D_n(sigma_{1,2}) = det zeta(i+j), 1<=i,j<=n
    vals = {}
    for nn in range(1, n+1):
        x = mp.mpf(1)/(2*nn+1)
        vals[nn] = logD[nn-1] + (nn+mp.mpf(1)/2)**2*(mp.log(2*nn+1) - mp.mpf(3)/2)
    pts = list(range(n-nfit+1, n+1))
    M = mp.matrix([[(mp.mpf(1)/(2*nn+1))**k for k in range(nfit)] for nn in pts])
    b = mp.matrix([vals[nn] for nn in pts])
    sol = mp.lu_solve(M, b)
    return sol, vals
res = {}
for (n, dps, nfit) in ((60, 500, 24), (70, 700, 28), (70, 900, 32)):
    sol, vals = fit(n, dps, nfit)
    mp.mp.dps = 60
    A0 = mp.exp(sol[0])
    res[(n, dps, nfit)] = A0
    print('n<=%d dps %d nfit %d: A0 = %s ; log-series coeffs c1..c4 = %s' % (n, dps, nfit, mp.nstr(A0, 35), [mp.nstr(sol[k], 12) for k in range(1, 5)]))
mp.mp.dps = 60
cand = mp.exp(mp.mpf(1)/12)*mp.mpf(2)**(mp.mpf(1)/6)*mp.mpf(3)**(mp.mpf(1)/8)/mp.glaisher**3
print('closed form e^{1/12} 2^{1/6} 3^{1/8} / A^3 =', mp.nstr(cand, 35))
for k, v in res.items():
    print('  fit', k, ' - closed =', mp.nstr(v - cand, 3))
print('Monien printed A0 = 0.351466738331; ratio closed/printed =', mp.nstr(cand/mp.mpf('0.351466738331'), 15))
# (d) H_100 from the asymptotic form
n = 100; x = mp.mpf(1)/(2*n+1)
base = -(n+mp.mpf(1)/2)**2*(mp.log(2*n+1) - mp.mpf(3)/2)
for name, A in (('closed 0.66360', cand), ('printed 0.351466738331', mp.mpf('0.351466738331'))):
    lg = (mp.log(A) + base + mp.log(1 + x**2/24))/mp.log(10)
    ex = mp.floor(lg); mant = 10**(lg-ex)
    print('H_100 with A0 %s: %s e%d' % (name, mp.nstr(mant, 8), int(ex)))
