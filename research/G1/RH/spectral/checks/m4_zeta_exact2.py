"""JZC M4 proof, gaps closed by exact computer algebra (m4_rh_exact2.py):
 (A) SYMBOLIC zeta index j (field Q(p, alpha, j); gauge Taylor data of Q_j/C(2j, j) at 0 and 4c, rational in j), first order in
     mu_j, KORD = 4: identically in (p, alpha, j):
       N^{-1-jp} coefficient (per unit mu_j C(2j, j)) = p j/2;  N^{-2-jp} = 0;  N^{-3-jp}/N^{-1-jp} = A_j + B_j alpha^2;  N^{-4-jp} = 0.
     Validity of the symbolic Taylor data for every integer j >= 1: at 0 the coefficient of z^m of Q_j(z) = sum_{i<j} C(2i,i) z^{j-1-i}
     is C(2(j-1-m), j-1-m) for m <= j-1 and 0 for m >= j; divided by C(2j, j) this is prod_{i=0}^m (j-i)/(2(2j-2i-1)) (from
     C(2k,k)/C(2k+2,k+1) = (k+1)/(2(2k+1))), which vanishes for m >= j through the factor i = j. At 4c (c = 1): the generating
     function sum_j Q_j(z) t^j = t/((1 - zt) sqrt(1 - 4t)) gives, with z = 4 + w, sum_j [w^m]Q_j t^j = t^{m+1}(1-4t)^{-m-3/2}, so
     [w^m]Q_j / C(2j, j) = j(j-1)...(j-m)/(4^{m+1} (1/2)_{m+1}) (a polynomial in j). Both are asserted below against the
     integer-j polynomials for j <= 8.
 (B) second order in mu_1 (j = 1), KORD = 5: per unit mu_1^2, natural form (N/n)^{3p} sum_k e2_k n^{-k}:
       N^{-1-2p} = 0 (E3 Lemma E3.7), N^{-2-2p} = p(3p+1)/2 (i.e. (3p+1)/(2p) eps_1^2), N^{-3-2p} = 0,
       N^{-4-2p} = p^2 h2 with h2 = (p+1)(p+2)(3p^2+2p+1)/(8p^2) + (p+2)(2p^3-p^2-7p-6) alpha^2/(16p^2), N^{-5-2p} = 0.
     (mu_{n,1}^2 = (2 zeta(-p))^2 n^{-2p} = eps_1^2 n^{-2p}/(p c)^2, c = 1.)"""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["EO"] = os.environ.get("EO", "1")
import m4_rh_exact2 as X
from sympy import binomial, factor, Rational
K, p, al, jj, ZERO, ONE = X.K, X.p, X.al, X.jj, X.ZERO, X.ONE
A = (jj**2*(jj**2 + 2*jj - 2)*p**3 + 2*(jj + 1)*(2*jj**2 - 1)*p**2 + (5*jj**2 + 2*jj - 6)*p + 2*(jj - 2))/(24*(2*jj - 1)*p)
B = (p + 2)*(jj**2*p**2 + (jj + 1)*p + 2)/(8*(2*jj - 1)*p)
part = sys.argv[1] if len(sys.argv) > 1 else "A"
X._provenance(__file__, X)
ok = True
def chk(lab, v):
    global ok
    z = (v == ZERO); ok &= z; print(f"{lab} identically: {z}", flush=True)
if part == "A":
    # symbolic Taylor data vs integer-j polynomials
    for j in range(1, 9):
        Q = [int(binomial(2*i, i)) for i in range(j)]                 # Q_j(z) = sum_i Q[i] z^{j-1-i}
        cj = int(binomial(2*j, j))
        for m in range(0, 10):
            at0 = Rational(Q[j - 1 - m], cj) if m <= j - 1 else 0
            v = ONE
            for i in range(m + 1): v = v*(jj - i)/(2*(2*jj - 2*i - 1))
            assert v.as_expr().subs('j', j) == at0, ("Taylor at 0", j, m)
            at4 = sum(Rational(Q[i]*int(binomial(j - 1 - i, m))*4**(j - 1 - i - m), cj) for i in range(j) if j - 1 - i >= m)
            w = ONE
            for i in range(m + 1): w = w*(jj - i)
            w = w/(K(4)**(m + 1)*X.rf(X.HALF, m + 1))
            assert w.as_expr().subs('j', j) == at4, ("Taylor at 4", j, m)
    print("symbolic Taylor data of Q_j/C(2j,j) at 0 and 4 agree with the integer-j polynomials (j <= 8, m <= 9)")
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu='sym'); g1 = g[1]
    print(f"   ({time.time() - t0:.0f}s)")
    chk("lead N^-(1+jp) = p j/2", g1[1] - p*jj/2)
    chk("N^-(2+jp) = 0", g1[2])
    chk("N^-(3+jp)/N^-(1+jp) = A_j + B_j alpha^2", g1[3]/g1[1] - A - B*al**2)
    if X.KORD >= 4: chk("N^-(4+jp) = 0", g1[4])
else:
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu=1); g2 = g[2]
    print(f"   ({time.time() - t0:.0f}s)")
    chk("mu1^2: N^-(1+2p) = 0", g2[1])
    chk("mu1^2: N^-(2+2p) = p(3p+1)/2", g2[2] - p*(3*p + 1)/2)
    chk("mu1^2: N^-(3+2p) = 0", g2[3])
    if X.KORD >= 5:
        h2 = (p + 1)*(p + 2)*(3*p**2 + 2*p + 1)/(8*p**2) + (p + 2)*(2*p**3 - p**2 - 7*p - 6)*al**2/(16*p**2)
        chk("mu1^2: N^-(4+2p) = p^2 h2 (h2 = eps1^2-bracket N^-2 coefficient)", g2[4] - p**2*h2)
        chk("mu1^2: N^-(5+2p) = 0", g2[5])
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE"); assert ok
