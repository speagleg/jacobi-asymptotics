"""Theorem H, gap G5 (JZC_M3a_H.md): the decoupled model M(beta, nu) in exact arithmetic over Q(p, alpha, j, beta)[i]
(m4_rh_exact2 with DECOUPLE=1: alpha = Bessel order nu, beta = Szego exponent), first order in mu_j for integer j = 1, 2, 3
(KORD = 4). Asserted identically in (p, alpha, beta): in the natural form N = n + (beta+1)/2, the response
(N/n)^{(j+1)p} sum_k e_k n^{-k} has leading coefficient C(2j,j) p j/2, vanishing N^{-2-jp} and N^{-4-jp} coefficients, and
N^{-3-jp}/N^{-1-jp} = A_j + B_j alpha^2 -- i.e. the zeta layer depends on beta only through N (Prop S for the zeta layer,
exact), with the lattice dressings g_j evaluated at the Bessel order. Also asserts the integer layer f_1..f_4 is beta-free."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["DECOUPLE"] = "1"; os.environ.setdefault("EO", "1"); os.environ.setdefault("KORD", "4"); os.environ.setdefault("SHI", "14")
import m4_rh_exact2 as X
from sympy import binomial, Symbol
K, p, al, ZERO = X.K, X.p, X.al, X.ZERO
X._provenance(__file__, X)
A = lambda j: (j**2*(j**2 + 2*j - 2)*p**3 + 2*(j + 1)*(2*j**2 - 1)*p**2 + (5*j**2 + 2*j - 6)*p + 2*(j - 2))/(24*(2*j - 1)*p)
B = lambda j: (p + 2)*(j**2*p**2 + (j + 1)*p + 2)/(8*(2*j - 1)*p)
f4 = ((p + 1)*(6*p**3 + 46*p**2 + 55*p + 3)/(1440*p*(3*p + 2)) - 5*(p + 1)*(p + 2)*al**2/(96*(3*p + 2))
      - p*(p + 2)**2*al**4/(128*(3*p + 2)))
ok = True
def chk(lab, v):
    global ok
    z = (v == ZERO); ok &= z; print(f"{lab} identically: {z}", flush=True)
for j in (1, 2, 3):
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu=j); g1 = g[1]
    if j == 1:
        chk("integer layer f1 = f3 = 0 (beta-free)", f[1]); chk("f3 = 0", f[3])
        chk("f2 = (p+1)/12 - (p+2)alpha^2/8 (beta-free)", f[2] - (p + 1)/12 + (p + 2)*al**2/8)
        chk("f4 = closed form at the Bessel order (beta-free)", f[4] - f4)
    chk(f"j={j}: lead = C(2j,j) p j/2", g1[1] - K(int(binomial(2*j, j)))*p*j/2)
    chk(f"j={j}: N^-(2+jp) = 0", g1[2])
    chk(f"j={j}: N^-(3+jp)/N^-(1+jp) = A_j + B_j alpha^2 (beta-free)", g1[3]/g1[1] - A(j) - B(j)*al**2)
    chk(f"j={j}: N^-(4+jp) = 0", g1[4])
    print(f"   ({time.time() - t0:.0f}s)", flush=True)
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE"); assert ok
