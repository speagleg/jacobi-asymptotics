"""SPEC §3.14: where the pi cot kernel comes from. Assertion checks of
 (K)  Theorem K (lattice, p > 1): e_n := (cp/pi) int_0^inf E(-r) r^{-1/2} (r + 4c)^{-3/2} dr, E = 2 Im Log(1 - exp(-a_n r^{-1/p})),
      a_n = 2 pi i n e^{-i pi/p}, equals the Mellin-Barnes integral
      (1/2 pi i) int_(1/2) p W(w) zeta(-wp) n^{-wp} pi [cot(pi w p/2) - cot(pi w)] dw,  W(w) = (4c)^w Gamma(w+1/2)/(sqrt(pi) Gamma(w+1)),
      and its residue series sum_j p W(j) zeta(-jp) n^{-jp} (E3's eps_j) is asymptotic to it;
 (P)  the Mellin transform of the first-order phase perturbation (Prop. 3.14.4);
 (B)  the hard-edge Beta integral of a branched tilt z^q;
 (K0) Lemma K0, the Mellin transform of the truncated per-node law;
 (Q)  Lemma Q: the soft-edge condition of the constrained equilibrium gives a = 4c(p), with the variational inequalities.
mpmath only; about 10 min."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
C_ = Checks()
mp.mp.dps = 20

def cp_(p):
    I = mp.sqrt(mp.pi)/2*mp.gamma(1/p + mp.mpf(1)/2)/mp.gamma(1/p + 1)
    return (mp.pi/(2*I))**p/4

def W(w, c): return (4*c)**w*mp.gamma(w + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(w + 1))

def Efun(p, n):
    a = 2j*mp.pi*n*mp.exp(-1j*mp.pi/p)
    def E(r):
        X = -a*r**(-1/p)
        if mp.re(X) < -mp.mp.prec: return mp.mpf(0)
        return 2*mp.im(mp.log(1 - mp.exp(X)))
    return E, a

print("(K) Theorem K: e_n by quadrature vs Mellin-Barnes vs residue sums (J = 1, 2, 3, 5)")
for p, n in ((mp.mpf('1.5'), mp.mpf(10)), (mp.mpf('1.25'), mp.mpf(20)), (mp.mpf(3), mp.mpf(10))):
    c = cp_(p); E, _ = Efun(p, n); N = n**p
    eq = c*p/mp.pi*mp.quad(lambda r: E(r)*r**-0.5*(r + 4*c)**-1.5, [0, N/50, N/5, N, 5*N, 50*N, mp.inf])
    g = lambda w: p*W(w, c)*mp.zeta(-w*p)*n**(-w*p)*mp.pi*(mp.cot(mp.pi*w*p/2) - mp.cot(mp.pi*w))
    em = mp.quad(lambda t: g(mp.mpf('0.5') + 1j*t), [-30, -10, -3, 0, 3, 10, 30])/(2*mp.pi)
    res = [p*W(j, c)*mp.zeta(-j*p)*n**(-j*p) for j in range(1, 6)]
    print(f"  p={p} n={n}: quad {mp.nstr(eq, 16)}  MB {mp.nstr(mp.re(em), 16)}  residues", [mp.nstr(sum(res[:k]), 10) for k in (1, 2, 3, 5)])
    C_.check(f"K p={p} n={n} quad = MB", float(eq), float(mp.re(em)), 1e-15*float(abs(eq)) + 1e-25)
    C_.check(f"K p={p} n={n} residues(5) ~ MB", float(sum(res)), float(mp.re(em)), 1e-6*float(abs(eq)))

print("(P) first-order phase perturbation, p = 1.5, m = 1, n = 7, gamma = 1/2, Re w > (m+1)/p")
p, m, n, gm = mp.mpf('1.5'), mp.mpf(1), mp.mpf(7), mp.mpf('0.5')
E, a = Efun(p, n)
def dE(r):
    X = -a*r**(-1/p)
    if mp.re(X) < -mp.mp.prec: return mp.mpf(0)
    Fp = 2j*mp.pi*mp.exp(X)/(1 - mp.exp(X))
    return 2*mp.im(Fp*(-gm*n**(-m)*(r*mp.exp(1j*mp.pi))**(m/p)))
for w in (mp.mpf('2.3'), mp.mpf('3.1')):
    N = n**p
    lhs = mp.quad(lambda r: dE(r)*r**(-w - 1), [0, N/50, N/5, N, 5*N, 50*N, mp.inf])
    rhs = -2*mp.pi*gm*p*n**(-p*w)*mp.zeta(1 + m - p*w)*(mp.cos(mp.pi*w) + mp.sin(mp.pi*w)*mp.tan(mp.pi*(p*w - m)/2))
    print(f"  w={w}: quad {mp.nstr(lhs, 15)}  formula {mp.nstr(rhs, 15)}")
    C_.check(f"P w={w}", float(lhs), float(rhs), 1e-12*float(abs(rhs)))

print("(B) (1/pi) int_0^1 (1 - v^q)(1-v)^{-3/2} v^{-1/2} dv = 2 Gamma(q+1/2)/(sqrt(pi) Gamma(q))")
for q in (mp.mpf('0.4'), mp.mpf('1.7'), mp.mpf(3)):
    lhs = mp.quad(lambda v: (1 - v**q)*(1 - v)**-1.5*v**-0.5, [0, 0.5, 1])/mp.pi
    rhs = 2*mp.gamma(q + 0.5)/(mp.sqrt(mp.pi)*mp.gamma(q))
    print(f"  q={q}: {mp.nstr(lhs, 15)} vs {mp.nstr(rhs, 15)}"); C_.check(f"B q={q}", float(lhs), float(rhs), 1e-10)   # endpoint-singular quadrature: ~1e-12

print("(K0) int_0^1 u^{-w-1}(1-u)^{-1/2} du = -pi cot(pi w) Gamma(w+1/2)/(sqrt(pi) Gamma(w+1)), Re w < 0")
for w in (mp.mpf('-1.7'), mp.mpf(-2)/3, mp.mpf(-1)/mp.mpf('0.6')):
    lhs = mp.quad(lambda u: u**(-w - 1)*(1 - u)**-0.5, [0, 0.5, 1])
    rhs = -mp.pi*mp.cot(mp.pi*w)*mp.gamma(w + 0.5)/(mp.sqrt(mp.pi)*mp.gamma(w + 1))
    print(f"  w={mp.nstr(w, 6)}: {mp.nstr(lhs, 15)} vs {mp.nstr(rhs, 15)}"); C_.check(f"K0 w={mp.nstr(w, 6)}", float(lhs), float(rhs), 1e-10)

print("(Q) constrained equilibrium, constraint sigma = (1/p) y^{-1/p-1}, no external field")
mp.mp.dps = 15
for p in (mp.mpf('0.6'), mp.mpf('1.5')):
    c = cp_(p); sig = lambda y: y**(-1/p - 1)/p
    a = mp.findroot(lambda a: mp.quad(lambda y: sig(y)*(1 - a/y)**-0.5, [a, 2*a, 10*a, mp.inf]) - 1, 4*c*1.01)
    def nu(x):
        J = mp.quad(lambda y: sig(y)*mp.sqrt(y*(y - a))/(y - x), [a, 2*a, 10*a, mp.inf])
        return (1 - J)/(mp.pi*mp.sqrt(x*(a - x)))
    ratios = [nu(a*t)/sig(a*t) for t in (0.01, 0.3, 0.7, 0.99)]
    def U(z):
        ub = -mp.quad(lambda x: nu(x)*mp.log(abs(z - x)), [0, min(z, a)/2, min(z, a), a] if z < a else [0, a/2, a])
        us = -mp.quad(lambda y: sig(y)*mp.log(abs(z - y)), ([a, z, 2*z, mp.inf] if z > a else [a, 2*a, mp.inf]))
        return ub + us
    l = U(a/2); band = [U(a*t) - l for t in (0.1, 0.8)]; sat = [U(a*t) - l for t in (1.05, 1.5, 3)]
    print(f"  p={p}: a = {mp.nstr(a, 14)} (4c = {mp.nstr(4*c, 14)}); nu/sigma {[mp.nstr(r, 4) for r in ratios]}; "
          f"U - l band {[mp.nstr(b, 2) for b in band]}, saturated {[mp.nstr(s, 4) for s in sat]}")
    C_.check(f"Q p={p} a = 4c", float(a), float(4*c), 1e-11)
    C_.check(f"Q p={p} 0 <= nu <= sigma", float(min(min(ratios), 1 - max(ratios)) >= 0), 1.0, 0)
    C_.check(f"Q p={p} U const on band", float(max(abs(b) for b in band)), 0.0, 1e-8)
    C_.check(f"Q p={p} U < l on saturated region", float(max(sat) < 0), 1.0, 0)
C_.finish()
