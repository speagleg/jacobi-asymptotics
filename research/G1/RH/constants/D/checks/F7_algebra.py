"""Exact algebra for D.md §2 (Theorem F7): e2(p, alpha) from f2, f4 of Theorem N.6(ii); sympy."""
import sympy as sp
p,a,x=sp.symbols('p alpha x',positive=True)  # x = 1/N
f2=lambda A: -(p+2)*A**2/8+(p+1)/12
f4=lambda A: (p+1)*(6*p**3+46*p**2+55*p+3)/(1440*p*(3*p+2)) - 5*(p+1)*(p+2)*A**2/(96*(3*p+2)) - p*(p+2)**2*A**4/(128*(3*p+2))
lf=lambda A: sp.series(sp.log(1+f2(A)*x**2+f4(A)*x**4),x,0,6).removeO()
G=sp.expand(lf(a)-lf(a+2))           # = g2 x^2 + g4 x^4
g2=G.coeff(x,2); g4=G.coeff(x,4)
z=a+1; E=(p+2)*z
print('g2 - E/2 =',sp.simplify(g2-E/2))
# sum_{j>=1} (N+j)^{-s} ~ zeta(s,N+1) asymptotics: N^{1-s}/(s-1) - N^{-s}/2 + s N^{-s-1}/12 - s(s+1)(s+2) N^{-s-3}/720
def tail(s_): return x**(s_-1)/(s_-1) - x**s_/2 + s_*x**(s_+1)/12 - s_*(s_+1)*(s_+2)*x**(s_+3)/720
D=-E*sp.series(sp.log(1+x),x,0,7).removeO() + 2*(g2*tail(2)+g4*tail(4))
D=sp.expand(sp.series(D,x,0,5).removeO())
print('D coeffs x^1..x^4:',[sp.factor(D.coeff(x,k)) for k in range(1,5)])
# sum_{k>=0} D(N+k): D = d3 x^3 + d4 x^4 -> sum_{k>=0}(N+k)^{-3} ~ N^{-2}/2 + N^{-3}/2 ...
d3=D.coeff(x,3)
e2=sp.factor(d3/2)
print('e2(p,alpha) =',e2)
for (pp,ss) in [(2,2),(2,3),(1,2),(1,3),(3,2.5),(0.5,2.5)]:
    al=sp.Rational(ss)-1-pp; al=al/pp
    print((pp,ss), sp.nsimplify(e2.subs({p:pp,a:al})))
