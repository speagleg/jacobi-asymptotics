# (a) e2 at (p,s)=(3,5/2) and F7 centring at p=0.7, s=2. Own code; precision doubling.
import mpmath as mp, sys
from hank import run, cfun
def Cconst(p, s):
    p = mp.mpf(p); s = mp.mpf(s); z = (s-1)/p
    return mp.gamma(z)*mp.gamma(z+1)*(cfun(p)*(p+2)**2)**z/p, (p+2)*z, z
def resid(p, s, n, dps):
    Dg, y, lam, logD = run(p, s, n, dps)
    C, E, z = Cconst(p, s)
    out = []
    for m in range(1, n+1):
        N = m + (mp.mpf(s)-1)/(2*mp.mpf(p))
        out.append((m, N, lam[m-1]*N**E/C - 1, lam[m-1]*mp.mpf(m)**E/C - 1))
    return out
if __name__ == "__main__":
    # --- e2 at (3, 2.5): predicted 25/192
    for dps in (500, 700):
        r = resid(3, mp.mpf(5)/2, 44, dps)
        print('p=3 s=2.5 dps', dps)
        for (m, N, rN, rm) in r[19::4]:
            print('  m=%d  N^2*(lam N^E/C-1)=%s   m*(lam m^E/C-1)=%s' % (m, mp.nstr(rN*N**2, 15), mp.nstr(rm*m, 8)))
        # fit e2 + a4 N^-2 + a5 N^-3 + a6 N^-4 (+...) on last points: remainder after e2 N^-2 is O(N^-4) (1+p=4 and integer N^-4)
        pts = r[-8:]
        import itertools
        exps = [2, 4, 5, 6, 7, 8, 9, 10]
        A = mp.matrix([[N**(-e) for e in exps] for (m, N, rN, rm) in pts]); b = mp.matrix([rN for (m, N, rN, rm) in pts])
        sol = mp.lu_solve(A, b)
        print('  fit e2 =', mp.nstr(sol[0], 15), ' predicted 25/192 =', mp.nstr(mp.mpf(25)/192, 15), ' (N^-3 not in basis)')
        exps = [2, 3, 4, 5, 6, 7, 8, 9]
        A = mp.matrix([[N**(-e) for e in exps] for (m, N, rN, rm) in pts]); sol = mp.lu_solve(A, b)
        print('  fit with N^-3 free: e2 =', mp.nstr(sol[0], 15), ' e3 =', mp.nstr(sol[1], 6))
    # --- F7 centring at p = 0.7, s = 2
    for dps in (150, 250):
        r = resid(mp.mpf('0.7'), 2, 70, dps)
        print('p=0.7 s=2 dps', dps, ': relative residual with N vs with m; N*resN should ->0 like N^-0.7')
        for (m, N, rN, rm) in r[9::10] + [r[-1]]:
            print('  m=%d  resN=%s  N*resN=%s  N^1.7*resN=%s   m*resm=%s' % (m, mp.nstr(rN, 8), mp.nstr(rN*N, 8), mp.nstr(rN*N**mp.mpf('1.7'), 8), mp.nstr(rm*m, 8)))
