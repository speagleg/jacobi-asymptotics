# Prop R check with the reviewer's own pivots h_n: (i) p=3, s=2.5: n*log(h_n/H_n) -> e (remainder O(1/n)+n^{1-p});
# (ii) p=0.7, s=2 (K=1): n*[log(h_n/H_n) + (2 eps1/p) n^-p] -> e, remainder O(n^{-p} + n^{1-2p}) -> fit.
import mpmath as mp
from hank import run, cfun
def go(p, s, n, dps):
    Dg, y, lam, logD = run(p, s, n, dps)
    p = mp.mpf(p); s = mp.mpf(s); c = cfun(p)
    d1 = -(s-1)/2; d2 = (p+1)*(s-1)**2/(8*p) - (p+2)*(s-1-p)**2/(8*p**2) + (p+1)/12
    e = d1 + d1**2 - 2*d2; eps1 = 2*p*c*mp.zeta(-p)
    out = []
    for k in range(1, n):
        H = (2*mp.pi/p)*c**(2*k+1)*(c**(1/p)/k)**(s-1)*mp.gamma(k+1)**(-2*p)
        out.append((k, mp.log(Dg[k]/H)))
    return e, eps1, out
e, eps1, out = go(3, mp.mpf(5)/2, 44, 500)
print('p=3 s=2.5 e =', mp.nstr(e, 12))
for k, L in out[19::6]: print('  n=%d n*log(h/H)=%s' % (k, mp.nstr(k*L, 10)))
pts = out[-10:]; ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sol = mp.lu_solve(mp.matrix([[mp.mpf(k)**(-a) for a in ex] for k, L in pts]), mp.matrix([L for k, L in pts]))
print('  fit 1/n coeff =', mp.nstr(sol[0], 12), ' (n^-2 coeff', mp.nstr(sol[1], 8), ')')
p = mp.mpf('0.7'); e, eps1, out = go(p, 2, 70, 300)
print('p=0.7 s=2 e =', mp.nstr(e, 12), ' eps1 =', mp.nstr(eps1, 10))
for k, L in out[19::10]: print('  n=%d n*(log(h/H)+(2eps1/p)n^-p)=%s' % (k, mp.nstr(k*(L + 2*eps1/p*mp.mpf(k)**(-p)), 10)))
pts = out[-12:]; ex = [p, 1, 1+p, 2*p, 2, 3*p, 1+2*p, 2+p, 4*p, 3, 1+3*p, 2+2*p]
sol = mp.lu_solve(mp.matrix([[mp.mpf(k)**(-a) for a in ex] for k, L in pts]), mp.matrix([L for k, L in pts]))
print('  fit: n^-p coeff', mp.nstr(sol[0], 10), ' vs -2eps1/p =', mp.nstr(-2*eps1/p, 10), ';  1/n coeff', mp.nstr(sol[1], 8), ' vs e')
