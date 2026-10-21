"""JZC M4 section 6, exact: the first-order zeta response by the exact symbolic computation (m4_rh_exact.run(jmu=j): dual numbers,
the E3 gauge to first order in mu_j). Asserts, as identities in (p, alpha), for j = 1..JMAX (env, default 5), at order KORD (env,
default 5): the N^{-1-jp} coefficient per unit mu_j is C(2j, j) p j/2 (c = 1; i.e. eps_j = C(2j,j) p c^j zeta(-jp), E3 Lemma E3.7);
the N^{-2-jp} and N^{-4-jp} coefficients vanish; N^{-3-jp}/N^{-1-jp} = A_j + B_j alpha^2 (m4_zeta_dressing.py); for j = 1 the
N^{-5-jp} ratio = g1_4."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "5"); os.environ.setdefault("SHI", "18")
import m4_rh_exact as X
from sympy import binomial
K, p, al, ZERO = X.K, X.p, X.al, X.ZERO
A = lambda j: (j**2*(j**2 + 2*j - 2)*p**3 + 2*(j + 1)*(2*j**2 - 1)*p**2 + (5*j**2 + 2*j - 6)*p + 2*(j - 2))/(24*(2*j - 1)*p)
B = lambda j: (p + 2)*(j**2*p**2 + (j + 1)*p + 2)/(8*(2*j - 1)*p)
g14 = ((p + 1)*(9*p**6 + 117*p**5 + 161*p**4 - 569*p**3 - 1550*p**2 - 976*p + 48)/(5760*p**2*(3*p + 2))
       + (p + 1)*(p + 2)*(3*p**4 + 33*p**3 + 124*p**2 + 182*p + 108)*al**2/(192*p*(3*p + 2))
       + (p + 2)**3*(p**3 - 4*p - 4)*al**4/(128*p*(3*p + 2)))
ok = True
for j in range(1, int(os.environ.get("JMAX", "5")) + 1):
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu=j)
    checks = [("lead = C(2j,j) p j/2", g[1] - K(int(binomial(2*j, j)))*p*j/2), ("N^-(2+jp) = 0", g[2]),
              ("N^-(3+jp)/N^-(1+jp) = A_j + B_j al^2", g[3]/g[1] - A(j) - B(j)*al**2)]
    if X.KORD >= 4: checks.append(("N^-(4+jp) = 0", g[4]))
    if X.KORD >= 5 and j == 1: checks.append(("N^-(5+p)/N^-(1+p) = g1_4", g[5]/g[1] - g14))
    for lab, v in checks:
        z = (v == ZERO); ok &= z; print(f"j={j}: {lab} identically: {z}", flush=True)
    print(f"   ({time.time() - t0:.0f}s)", flush=True)
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE"); assert ok
