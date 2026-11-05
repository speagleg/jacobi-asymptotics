"""M1.1 checks (JZC_M1.md, Theorem Q): constrained equilibrium with upper constraint sigma on (0, Y], unit mass, no external field.
Claims checked numerically for several densities with y sigma(y) strictly decreasing:
  (Q)  soft-edge root a: int_a^Y sigma(y) (1 - a/y)^{-1/2} dy = 1 (unique);
  (N)  nu(x) = (1/pi) sqrt((a-x)/x) int_a^Y s(y)/(y-x) dy,  s(y) := sigma(y) sqrt(y/(y-a))   [explicit, positive]
       agrees with the balayage form [1 - int sigma(y) sqrt(y(y-a))/(y-x) dy]/(pi sqrt(x(a-x)));
  (M)  int_0^a nu + int_a^Y sigma = 1;
  (U)  0 <= nu <= sigma on (0, a);
  (E)  U^mu = const on [0, a]   and   U^mu < const on (a, Y]: via Phi(z) = (z-a) PV int s(y)/(z-y) dy > 0, AND by direct
       evaluation of the logarithmic potential (REVIEW_JZC_M1_A F5: (N) and (M) are identities in F(a), i.e. checks of the root only);
       and Phi is tied to the direct potential: -sqrt((z-a)/z) Phi(z)/(z-a) = U'(z) at z = 1.5a by a central difference
       (REVIEW_JZC_M1_B B5: without this, a sign error in Phi's finite-Y PV term passed all checks; it now fails).
(H2) is verified analytically (comments below) and on a fine grid of d(y sigma)/dy.
Densities: power laws (p = 0.6, 1.5); drum (p = 1, perimeter beta, cut at the first node); log law (Riemann-von Mangoldt-type,
lambda = T^2, cut at T = 2 pi e^{3/2}).
Analytic (H2): power: y sigma = y^{-1/p}/p; drum: y sigma = (1 - (beta/2) sqrt(y/n))/y, decreasing where positive;
log: y sigma = log(T/2pi)/(4 pi sqrt(y))... in T: decreasing in y iff T > 2 pi/e, which the cut satisfies."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 20; C_ = Checks()

def dens(kind):
    """sigma(y) on (0, Y] in the normalised edge variable (nodes z = n^p/lambda, mass-1 scaling), Y."""
    if kind.startswith("power"):
        p = mp.mpf(kind.split(":")[1]); return (lambda y: y**(-1/p - 1)/p), mp.inf
    if kind == "drum":   # N(lambda) = lambda - beta sqrt(lambda) on lambda >= lam0; nodes y = n/lambda, mass scaling 1/n, n = 50
        n, beta, lam0 = mp.mpf(50), mp.mpf('1.128379'), mp.mpf('1.5')
        return (lambda y: (1 - beta/2*mp.sqrt(y/n))/y**2), n/lam0
    if kind == "log":    # N(T) = (T/2pi) log(T/(2 pi e)), lambda = T^2 (p ~ 2), nodes y = n^2/lambda, mass 1/n, n = 40; cut at T0 = 2 pi e^1.5
        n = mp.mpf(40); T0 = 2*mp.pi*mp.e**mp.mpf('1.5')
        def sig(y):
            T = n/mp.sqrt(y); dNdT = mp.log(T/(2*mp.pi))/(2*mp.pi); return dNdT*(T/(2*y))/n
        return sig, (n/T0)**2

for kind in ("power:0.6", "power:1.5", "drum", "log"):
    sig, Y = dens(kind)
    pts = lambda a: [a, a*(1 + mp.mpf('1e-3')), 2*a, 10*a, Y] if Y != mp.inf else [a, a*(1 + mp.mpf('1e-3')), 2*a, 10*a, mp.inf]
    def F(a):   # int_a^Y sigma (1 - a/y)^{-1/2} dy - 1, with y = a + v^2
        top = mp.sqrt(Y - a) if Y != mp.inf else mp.inf
        vp = [0, mp.sqrt(a)/10, mp.sqrt(a)] + [top]
        return mp.quad(lambda v: 2*sig(a + v*v)*mp.sqrt(a + v*v), [x for x in vp if x <= top] if top != mp.inf else vp) - 1
    # monotonicity of y sigma(y) on a grid (hypothesis of Theorem Q)
    ys = [mp.mpf(10)**(mp.mpf(k)/40) for k in range(-120, 121)]; ys = [y for y in ys if y < Y]
    mono = all(mp.diff(lambda y: y*sig(y), y) < 0 for y in ys)          # fine grid of the derivative (F5(d))
    hi = mp.mpf(4) if Y == mp.inf else min(mp.mpf(4), Y*mp.mpf('0.999')); a = mp.findroot(F, (mp.mpf('0.05'), hi), solver='anderson')
    s = lambda y: sig(y)*mp.sqrt(y/(y - a))
    V = mp.sqrt(Y - a) if Y != mp.inf else mp.inf
    vpts = [0, mp.sqrt(a)/10, mp.sqrt(a), 3*mp.sqrt(a)] + ([V] if V != mp.inf else [mp.inf])
    vpts = [v for v in vpts if v <= V] if V != mp.inf else vpts
    sat = lambda fn: mp.quad(lambda v: 2*sig(a + v*v)*mp.sqrt(a + v*v)*fn(v), vpts)   # int_a^Y s(y) fn dy, y = a + v^2 (fn takes v)
    nu_exp = lambda x: mp.sqrt((a - x)/x)/mp.pi*sat(lambda v: 1/(v*v + (a - x)))
    nu_bal = lambda x: (1 - sat(lambda v: v*v/(v*v + (a - x))))/(mp.pi*mp.sqrt(x*(a - x)))      # sigma sqrt(y(y-a)) = s (y - a)
    xs = [a*t for t in (mp.mpf('0.01'), mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.8'), mp.mpf('0.99'))]
    agree = max(abs(nu_exp(x) - nu_bal(x))/abs(nu_bal(x)) for x in xs)
    rat = [nu_exp(x)/sig(x) for x in xs]
    mass = mp.quad(lambda w: 2*w*nu_exp(a - w*w), [0, mp.sqrt(a)/10, mp.sqrt(a)]) + mp.quad(sig, [a, 2*a, 10*a, Y] if Y != mp.inf else [a, 2*a, 10*a, mp.inf])
    def Phi(z):   # (z - a) PV int s/(z - y): PV via subtraction of s(z)
        f = lambda y: (s(y) - s(z))/(z - y)
        top = Y if Y != mp.inf else mp.inf
        main = mp.quad(f, [a, (a + z)/2, z, 2*z, top] if top == mp.inf or 2*z < top else [a, (a + z)/2, z, top])
        logpart = s(z)*(mp.log(z - a) - (mp.log(top - z) if top != mp.inf else 0)) if top != mp.inf else None
        if top == mp.inf:   # PV int_a^inf s(z)/(z - y) dy diverges logarithmically; s decays, so use the identity without subtraction tail
            return (z - a)*(mp.quad(lambda y: s(y)/(z - y), [a, (a + z)/2, z*(1 - mp.mpf('1e-9'))]) + mp.quad(lambda y: s(y)/(z - y), [z*(1 + mp.mpf('1e-9')), 2*z, mp.inf]))
        return (z - a)*(main + logpart)
    zs = [a*t for t in (mp.mpf('1.05'), mp.mpf('1.5'), mp.mpf(3))]; zs = [z for z in zs if z < Y]
    phis = [Phi(z) for z in zs]
    # direct potential (F5(b)): U(z) = -int log|z - x| dmu, band part with x = a - w^2 (smooth), saturated part with y = a + v^2
    def U(z):
        wb = sorted(set([mp.mpf(0), mp.sqrt(a)/10, mp.sqrt(a)/2, mp.sqrt(a)] + ([mp.sqrt(a - z)] if z < a else [])))
        ub = -mp.quad(lambda w: 2*w*nu_exp(a - w*w)*mp.log(abs(z - a + w*w)), wb)
        vb = sorted(set([v for v in vpts if v != mp.inf] + ([mp.sqrt(z - a)] if z > a else [])))
        us = -mp.quad(lambda v: 2*v*sig(a + v*v)*mp.log(abs(z - a - v*v)), vb + ([mp.inf] if mp.inf in vpts else []))
        return mp.re(ub + us)        # rounding near the edge leaves ~1e-20 imaginary parts
    mp.mp.dps = 12
    l0 = U(a/2); band = [U(a*t) - l0 for t in (mp.mpf('0.1'), mp.mpf('0.9'))]
    outer = [U(z) - l0 for z in zs]
    # Phi vs the direct potential (REVIEW_JZC_M1_B B5): U'(z) = -Re G(z) = -sqrt((z-a)/z) H(z) = -sqrt((z-a)/z) Phi(z)/(z-a),
    # by a central difference of the direct U at z = 1.5a (this ties the Phi code, incl. its finite-Y PV term, to U)
    zd = zs[1]; hd = zd*mp.mpf('1e-3'); dUd = (U(zd + hd) - U(zd - hd))/(2*hd)
    mp.mp.dps = 20
    dPhi = -mp.sqrt((zd - a)/zd)*phis[1]/(zd - a); drel = abs(dPhi - dUd)/abs(dUd)
    print(f"   Phi vs direct U': at z = 1.5a, -sqrt((z-a)/z) Phi/(z-a) = {mp.nstr(dPhi, 8)}, central difference of U = {mp.nstr(dUd, 8)}, rel diff {mp.nstr(drel, 2)}")
    C_.check(f"{kind}: Phi matches direct U'", float(drel), 0.0, 1e-4)
    print(f"   direct potential: U - l on band {[mp.nstr(b, 2) for b in band]};  on (a,Y) {[mp.nstr(o, 4) for o in outer]}")
    C_.check(f"{kind}: U const on band (direct)", float(max(abs(b) for b in band)), 0.0, 1e-6)
    C_.check(f"{kind}: U < l on (a,Y) (direct)", float(max(outer) < 0), 1.0, 0)
    print(f"{kind}: y sigma decreasing on grid: {mono};  a = {mp.nstr(a, 12)};  nu explicit vs balayage: max rel diff {mp.nstr(agree, 3)};"
          f"  nu/sigma {[mp.nstr(r, 4) for r in rat]};  total mass {mp.nstr(mp.re(mass), 12)};  Phi(z) on (a,Y): {[mp.nstr(v, 4) for v in phis]}")
    C_.check(f"{kind}: hypothesis", float(mono), 1.0, 0)
    C_.check(f"{kind}: nu formulas agree", float(agree), 0.0, 1e-8)
    C_.check(f"{kind}: 0 <= nu <= sigma", float(min(rat) > 0 and max(rat) < 1), 1.0, 0)
    C_.check(f"{kind}: mass 1", float(mp.re(mass)), 1.0, 1e-9)
    C_.check(f"{kind}: Phi >= 0 (outer inequality)", float(min(phis) > 0), 1.0, 0)
C_.finish()
