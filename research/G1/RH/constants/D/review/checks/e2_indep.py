# Rule R independent re-derivation of F7's e2 and the vanishing N^-3 coefficient (p>1, integer layer only).
# Method: asymptotic series in u=1/N with Hurwitz-zeta (Euler-Maclaurin) tails; no code from D/checks used.
import sympy as sp
p, a, u = sp.symbols('p alpha u', positive=True)
zeta_ = a + 1
E = (p+2)*zeta_
f2 = lambda al: -(p+2)*al**2/8 + (p+1)/12
f4 = lambda al: (p+1)*(6*p**3+46*p**2+55*p+3)/(1440*p*(3*p+2)) - 5*(p+1)*(p+2)*al**2/(96*(3*p+2)) - p*(p+2)**2*al**4/(128*(3*p+2))
f6 = lambda al: 0  # only needed through N^-4 of log F, f6 enters at N^-6 -> final N^-4 (error term)
ORDER = 7
def logF(al):
    x = f2(al)*u**2 + f4(al)*u**4
    return sp.expand(sp.series(sp.log(1+x), u, 0, ORDER).removeO())
G = sp.expand(logF(a) - logF(a+2))
G = sp.collect(G, u)
print('g2 - E/2 =', sp.simplify(G.coeff(u,2) - E/2))
print('G coefficient of u^3 =', G.coeff(u,3))
# Hurwitz tail: H(a,N) = sum_{k>=0} (N+k)^{-a} ~ N^{1-a}/(a-1) + N^{-a}/2 + sum_i B_{2i}/(2i)! * rising(a,2i-1) N^{-a-2i+1}
def hurwitz(aa, order):
    s = u**(aa-1)/(aa-1) + u**aa/2
    for i in range(1, order):
        s += sp.bernoulli(2*i)/sp.factorial(2*i)*sp.rf(aa, 2*i-1)*u**(aa+2*i-1)
    return sp.expand(s)
# sum_{j>m} G(N_j) = sum_{k>=1} G(N+k) = sum_{k>=0}G(N+k) - G(N)
def tail_from(expr, include_zero):
    # expr polynomial in u; replace u^a by Hurwitz
    tot = 0
    for aa in range(2, ORDER):
        c = expr.coeff(u, aa)
        if c != 0:
            tot += c*hurwitz(aa, 5)
    if not include_zero:
        tot -= expr
    return sp.expand(sp.series(tot, u, 0, ORDER).removeO())
S1 = tail_from(G, include_zero=False)
D = sp.expand(-2*S1 + E*sp.series(sp.log(1+u), u, 0, ORDER).removeO())
D = sp.expand(sp.series(D, u, 0, 6).removeO())
for k in range(0, 6):
    print('D coeff u^%d:' % k, sp.factor(sp.simplify(D.coeff(u, k))))
# final: log lam_m - log C + E log N_m = -sum_{k>=0} D(N+k)
Fin = -tail_from(sp.expand(D), include_zero=True)
Fin = sp.expand(sp.series(Fin, u, 0, 4).removeO())
e2 = sp.factor(sp.simplify(Fin.coeff(u, 2)))
e3 = sp.simplify(Fin.coeff(u, 3))
print('final u^1 coeff:', sp.simplify(Fin.coeff(u,1)))
print('e2 =', e2)
print('final u^3 coeff =', e3)
z = sp.symbols('zeta')
claim = E*((2*p+1)*(p+2)*zeta_**2 + p**2 - p - 1)/(24*(3*p+2))
print('e2 - claim =', sp.simplify(e2 - claim))
s = sp.symbols('s')
for (pp, ss) in [(2,2),(2,3),(3,sp.Rational(5,2)),(sp.Rational(5,2),4)]:
    val = e2.subs({p: pp, a: (ss-1)/pp - 1})
    print('e2(p=%s,s=%s) =' % (pp, ss), sp.nsimplify(val), float(val))
