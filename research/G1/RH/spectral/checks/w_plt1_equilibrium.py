"""JZC_W_plt1 §2-§3 (NUMERICAL checks of the PROVED statements; Rule N: finite samples, quadrature, nothing fitted).

The kappa-node constrained equilibrium at scale n^p (JZC_W_plt1 Prop 1, Prop 2, Lemma 3): eps := kappa/n^p, constraint (node density per n)
  sigma_eps(y) = (1/p) y^-2 (1/y - eps)^{1/p - 1}  on  S_eps^tot := {y : 1/y - eps > 0} = (0, 1/eps) (eps > 0), (0, inf) u (-inf, -1/|eps|) (eps < 0),
band [0, a], saturated set S := S_eps^tot minus [0, a];  nu(x) = (1/pi) sqrt((a - x)/x) T(x), T(x) := int_S s(y)/(y - x) dy, s := sigma sqrt(y/(y - a)).
Checks (units n = 1, i.e. y in the n^p frame; c = c(p)):
 [A]  edge: closed form a = 4c (1 - a eps)^{1-p/2} vs the quadrature root of F(a) := int_S s = 1 (y-variables, independent of the closed form);
      control (eps < 0): Theorem Q verbatim on (0, inf) (no mass on the negative piece) gives a different root, relative shift ~ -p|eps|^{1/p}.
 [B]  unit mass: int_0^a nu + int_S sigma = 1.
 [C]  band: nu (explicit) = nu (balayage form, R(y) = sign(y) sqrt(y(y - a))); 0 < nu < sigma at 9 points of (0, a) (near both ends incl.).
 [D]  saturated: H(z) := PV int_S s(y)/(z - y) dy > 0 on a grid of (a, Y) (incl. near a and Y) -> U* strictly increasing there.
 [E]  direct potentials (two cases, dps 15): U*(x) := int log|x - y| dmu constant on the band (3 points); U* - l > 0 at saturated points, on the
      negative axis (eps < 0: between the pieces and inside the negative piece) and Re phi = l - Re g < 0 at complex points incl. Re z < 0.
 [F]  hard edge: sqrt(x) nu(x) -> C_eps := sqrt(a) T(0)/pi > 0; at eps = 0 the Theorem Q density equals Paper 2's psi* = lambda_p I_{x/4c}(1/p+1/2, 1/2)
      (validates the implementation); C_eps - C_0 = O(eps) (printed).
 [G]  soft edge: (sigma - nu)(x)/sqrt(a - x) -> -h(a)/(pi sqrt a) > 0, h(a) = int_a^Y (g(y) - g(a))(y - a)^{-3/2} dy - 2 g(a)/sqrt(Y - a)
      + int_{S-} s(y)/(y - a) dy  (g := sqrt(y) sigma; each term < 0).
 [H]  mass accounting behind the branch rule (Lemma 3): int_x^inf sigma = t_k(x) - gamma on (a, inf) for eps < 0 (gamma := |eps|^{1/p}, t_k(x) :=
      (1/x - eps)^{1/p}), mass of the negative piece = gamma; eps > 0: int_x^Y sigma = t_k(x). w-plane edge a_w = a/(1 - eps a) = 4c(1 - eps a)^{-p/2}.
 [I]  ranges: eps > 0 large (eps = 2, 10: Theorem Q applies for every eps > 0) and eps < 0 down to -0.9 (n = 1, |kappa| < a^p <= 1): the signs of [C], [D].
 [J]  Toda bookkeeping (Prop 3 (iii), algebra): the Taylor coefficients of -sum_k (2 zeta(-kp, a)/k) zeta(z)^k + (1/p - 2a) log(1 - eps z)
      (n = 1) equal -(2 Z_kappa(-j)/j - B_j) eps-scaled, with Z_kappa(-j) = sum_l binom(j, l) kappa^{j-l} zeta(-lp, a), B_j = -(1/p - 1) kappa^j/j."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from w_common import Checks
from so_coeffs import c_p_mp
C_ = Checks()
print("w_plt1_equilibrium.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), flush=True)


class Eq:
    def __init__(s, p, eps):
        s.p, s.eps = mp.mpf(p), mp.mpf(eps); s.c = mp.mpf(c_p_mp(s.p)); p_ = s.p
        s.a = mp.re(mp.findroot(lambda a: a - 4*s.c*(1 - a*s.eps)**(1 - p_/2), 4*s.c/(1 + 4*s.c*max(s.eps, 0))))
        s.Y = 1/s.eps if s.eps > 0 else mp.inf
        s.zp = 1/abs(s.eps) if s.eps < 0 else None

    def sig(s, y):
        u = 1/y - s.eps                       # > 0 on the constraint set; clamp the rounding at y = Y
        return (1/s.p)*y**-2*u**(1/s.p - 1) if u > 0 else mp.mpf(0)
    def g(s, y): return mp.sqrt(y)*s.sig(y)
    def s_(s, y, a=None):
        a = s.a if a is None else a
        return s.sig(y)*mp.sqrt(y/(y - a))

    def pos_pts(s, a):
        return [a, a + (s.Y - a)/2, s.Y] if s.Y != mp.inf else [a, a + 1, 4*a, 40*a, mp.inf]

    def qa(s, r, a, extra=()):
        """int over (a, Y) of r(y, v) (y - a)^{-1/2} dy = int 2 r(a + v^2, v) dv  (y = a + v^2; r is passed v so that no (y - a)
        is ever formed from the rounded y)"""
        top = mp.sqrt(s.Y - a) if s.Y != mp.inf else mp.inf
        pts = [mp.mpf(0)] + sorted(mp.sqrt(e - a) for e in extra) + ([top] if top != mp.inf else [1, 2, 7, mp.inf])
        return mp.quad(lambda v: 2*r(a + v*v, v), pts)

    def neg_pts(s): return [-mp.inf, -40*s.zp, -4*s.zp, -2*s.zp, -s.zp]

    def F(s, a, neg=True):
        v = s.qa(lambda y, w: s.g(y), a)                    # s(y) = g(y) (y - a)^{-1/2}
        if s.eps < 0 and neg: v += mp.quad(lambda y: s.s_(y, a), s.neg_pts())
        return v

    def T(s, x):
        f = lambda y: s.s_(y)/(y - x)
        v = s.qa(lambda y, w: s.g(y)/(y - x), s.a)
        if s.eps < 0: v += mp.quad(f, s.neg_pts())
        return v

    def nu(s, x): return mp.sqrt((s.a - x)/x)*s.T(x)/mp.pi

    def nu_bal(s, x):
        a = s.a; R = lambda y: (1 if y > 0 else -1)*mp.sqrt(y*(y - a))
        f = lambda y: s.sig(y)*R(y)/(y - x)
        v = mp.quad(f, s.pos_pts(a))
        if s.eps < 0: v += mp.quad(f, s.neg_pts())
        return (1 - v)/(mp.pi*mp.sqrt(x*(a - x)))

    def satmass(s):
        v = mp.quad(s.sig, s.pos_pts(s.a))
        if s.eps < 0: v += mp.quad(s.sig, s.neg_pts())
        return v

    def H(s, z):
        a = s.a; gz = s.g(z)
        v = s.qa(lambda y, w: (s.g(y) - gz)/(z - y) if y != z else -mp.diff(s.g, z), a, extra=(z,))
        if s.Y != mp.inf:   # the PV of (y - a)^{-1/2}/(z - y) over (a, Y), closed form (JZC_M1 Thm Q (iii))
            r1, r2 = mp.sqrt(s.Y - a), mp.sqrt(z - a); v += gz*mp.log((r1 + r2)/(r1 - r2))/r2
        if s.eps < 0: v += mp.quad(lambda y: s.s_(y)/(z - y), s.neg_pts())
        return v

    def h_soft(s):
        a = s.a; ga = s.g(a)
        dga = mp.diff(s.g, a)
        v = s.qa(lambda y, w: (s.g(y) - ga)/(w*w) if w > mp.mpf(10)**(-mp.mp.dps//2) else dga, a)
        if s.Y != mp.inf: v -= 2*ga/mp.sqrt(s.Y - a)
        if s.eps < 0: v += mp.quad(lambda y: s.s_(y)/(y - a), s.neg_pts())
        return v

    def U(s, z):
        """int log|z - y| dmu(y) (real z or complex)"""
        a = s.a; zr = mp.re(z)
        bp = [0, zr, a] if (mp.im(z) == 0 and 0 < zr < a) else [0, a/2, a]
        band = mp.quad(lambda y: s.nu(y)*mp.log(abs(z - y)), bp)
        pp = s.pos_pts(a)
        if mp.im(z) == 0 and zr > a and (s.Y == mp.inf or zr < s.Y): pp = sorted(set([q for q in pp if q != mp.inf] + [zr])) + ([mp.inf] if s.Y == mp.inf else [])
        sat = mp.quad(lambda y: s.sig(y)*mp.log(abs(z - y)), pp)
        if s.eps < 0:
            npts = s.neg_pts()
            if mp.im(z) == 0 and zr < -s.zp: npts = sorted(set([q for q in npts if q != -mp.inf] + [zr])); npts = [-mp.inf] + npts
            sat += mp.quad(lambda y: s.sig(y)*mp.log(abs(z - y)), npts)
        return band + sat


mp.mp.dps = 25
CASES = [(0.6, 0.05), (0.6, -0.05), (0.6, 0.3), (0.6, -0.3), (0.75, 0.05), (0.75, -0.2), (0.4, 0.1), (0.4, -0.1)]
for (p, eps) in CASES:
    E = Eq(p, eps); a = E.a; P = E.p
    print(f"\n=== p = {p}, eps = {eps}: c = {mp.nstr(E.c, 12)}, a = {mp.nstr(a, 15)} (4c = {mp.nstr(4*E.c, 12)}), a/4c - 1 = {mp.nstr(a/(4*E.c) - 1, 8)}", flush=True)
    aq = mp.re(mp.findroot(lambda x: E.F(x) - 1, a))
    print(f"  [A] quadrature root of F(a) = 1: {mp.nstr(aq, 18)}; |closed form - root| = {mp.nstr(abs(aq - a), 3)}")
    C_.check(f"[A] edge p={p} eps={eps}", abs(aq - a) < mp.mpf(10)**-18)
    if eps < 0:
        an = mp.re(mp.findroot(lambda x: E.F(x, neg=False) - 1, a))
        rel = an/a - 1; ref = -P*abs(E.eps)**(1/P)
        print(f"  [A] control (Theorem Q on (0, inf) only): root {mp.nstr(an, 12)}, relative shift {mp.nstr(rel, 6)} (leading -p|eps|^(1/p) = {mp.nstr(ref, 6)})")
        C_.check(f"[A] control naive root differs p={p} eps={eps}", abs(rel) > 10**-6 and abs(rel/ref - 1) < 0.5)
    m = mp.quad(E.nu, [0, a/2, a]) + E.satmass()
    print(f"  [B] mass = {mp.nstr(m, 20)}"); C_.check(f"[B] mass p={p} eps={eps}", abs(m - 1) < mp.mpf(10)**-13)
    xs = [a*mp.mpf(t) for t in ('1e-6', '0.01', '0.1', '0.3', '0.5', '0.7', '0.9', '0.99', '0.999999')]
    ratios = []
    for x in xs:
        nv, nb, sg = E.nu(x), E.nu_bal(x), E.sig(x)
        C_.check(f"[C] explicit = balayage p={p} eps={eps} x={mp.nstr(x, 4)}", abs(nv - nb) < mp.mpf(10)**-15*abs(nv))
        ratios.append(nv/sg)
        C_.check(f"[C] 0 < nu < sigma p={p} eps={eps} x={mp.nstr(x, 4)}", 0 < nv < sg)
    print("  [C] nu/sigma at x/a = 1e-6 .. 1-1e-6: " + ", ".join(mp.nstr(r, 6) for r in ratios))
    Y = E.Y
    zs = [a*(1 + mp.mpf(t)) for t in ('1e-6', '1e-3', '0.1', '0.5', '1', '3')] + ([a + (Y - a)*mp.mpf(t) for t in ('0.5', '0.9', '0.999')] if Y != mp.inf else [10*a, 1000*a])
    zs = [z for z in zs if Y == mp.inf or z < Y]
    Hs = [E.H(z) for z in zs]
    print("  [D] H on (a, Y): " + ", ".join(mp.nstr(h, 5) for h in Hs))
    for z, h in zip(zs, Hs): C_.check(f"[D] H > 0 p={p} eps={eps} z={mp.nstr(z, 4)}", h > 0)
    C0 = mp.sqrt(a)*E.T(0)/mp.pi; x = a*mp.mpf('1e-10')
    print(f"  [F] C_eps = {mp.nstr(C0, 15)}; sqrt(x) nu(x) at x/a = 1e-10: {mp.nstr(mp.sqrt(x)*E.nu(x), 15)}")
    C_.check(f"[F] hard-edge constant p={p} eps={eps}", C0 > 0 and abs(mp.sqrt(x)*E.nu(x)/C0 - 1) < 1e-9)
    hs = E.h_soft(); lim = -hs/(mp.pi*mp.sqrt(a)); x = a*(1 - mp.mpf('1e-8'))
    q_ = (E.sig(x) - E.nu(x))/mp.sqrt(a - x)
    print(f"  [G] h(a) = {mp.nstr(hs, 10)} < 0; (sigma - nu)/sqrt(a - x) at 1 - x/a = 1e-8: {mp.nstr(q_, 10)} vs -h(a)/(pi sqrt a) = {mp.nstr(lim, 10)}")
    C_.check(f"[G] soft edge p={p} eps={eps}", hs < 0 and abs(q_/lim - 1) < 1e-3)
    x = 2*a
    if eps < 0:
        gam = abs(E.eps)**(1/P); tk = (1/x - E.eps)**(1/P)
        v1 = mp.quad(E.sig, [x, 4*x, mp.inf]); v2 = mp.quad(E.sig, E.neg_pts())
        print(f"  [H] int_x^inf sigma = {mp.nstr(v1, 15)} = t_k(x) - gamma = {mp.nstr(tk - gam, 15)}; negative-piece mass {mp.nstr(v2, 15)} = gamma = {mp.nstr(gam, 15)}")
        C_.check(f"[H] mass accounting p={p} eps={eps}", abs(v1 - (tk - gam)) < 1e-18 and abs(v2 - gam) < 1e-18)
    else:
        tk = (1/x - E.eps)**(1/P); v1 = mp.quad(E.sig, [x, (x + Y)/2, Y])
        C_.check(f"[H] mass accounting p={p} eps={eps}", abs(v1 - tk) < 1e-18)
    aw = a/(1 - E.eps*a); C_.check(f"[H] w-plane edge p={p} eps={eps}", abs(aw - 4*E.c*(1 - E.eps*a)**(-P/2)) < 1e-20)
    if (p, eps) == (0.6, 0.0) or True:
        pass

# [F] lattice validation: Theorem Q's density at eps = 0 vs Paper 2's psi* = lambda_p(x) I_{x/4c}(1/p + 1/2, 1/2)
for p in (0.6, 0.75):
    E = Eq(p, 0); P = E.p
    for t in ('0.01', '0.3', '0.8'):
        x = E.a*mp.mpf(t); lam = (1/P)*x**(-1/P - 1); ps = lam*mp.betainc(1/P + mp.mpf(1)/2, mp.mpf(1)/2, 0, x/E.a, regularized=True)
        C_.check(f"[F] Theorem Q density = Paper 2 psi* p={p} x/4c={t}", abs(E.nu(x)/ps - 1) < mp.mpf(10)**-18)
    C0 = mp.sqrt(E.a)*E.T(0)/mp.pi; Cs = []
    for eps in ('1e-3', '-1e-3', '1e-4'):
        E2 = Eq(p, mp.mpf(eps)); Cs.append((mp.sqrt(E2.a)*E2.T(0)/mp.pi - C0)/mp.mpf(eps))
    print(f"\n  [F] p = {p}: C_0 = {mp.nstr(C0, 12)}; (C_eps - C_0)/eps at eps = 1e-3, -1e-3, 1e-4: " + ", ".join(mp.nstr(v, 8) for v in Cs))
    C_.check(f"[F] C_eps - C_0 = O(eps) p={p}", abs(Cs[0] - Cs[1]) < 0.05*abs(Cs[2]) + 1e-12 and abs(Cs[2] - (Cs[0] + Cs[1])/2) < 0.01*abs(Cs[2]) + 1e-12)

# [I] ranges
print()
for (p, eps) in [(0.6, 2), (0.6, 10), (0.6, -0.6), (0.6, -0.9), (0.75, -0.9), (0.4, -0.9)]:
    E = Eq(p, eps); a = E.a
    xs = [a*mp.mpf(t) for t in ('1e-6', '0.1', '0.5', '0.9', '0.999999')]
    r = [E.nu(x)/E.sig(x) for x in xs]
    zs = [a*(1 + mp.mpf(t)) for t in ('1e-6', '0.1', '1')]
    zs = [z for z in zs if E.Y == mp.inf or z < E.Y] + ([a + (E.Y - a)*mp.mpf('0.99')] if E.Y != mp.inf else [])
    Hs = [E.H(z) for z in zs]
    print(f"  [I] p = {p}, eps = {eps}: a = {mp.nstr(a, 10)}" + (f", a eps = {mp.nstr(a*E.eps, 6)}" if eps > 0 else f", z' = {mp.nstr(E.zp, 6)}")
          + "; nu/sigma: " + ", ".join(mp.nstr(v, 5) for v in r) + "; H: " + ", ".join(mp.nstr(v, 5) for v in Hs))
    C_.check(f"[I] nu < sigma and H > 0 (every eps) p={p} eps={eps}", all(v < 1 for v in r) and all(h > 0 for h in Hs))
    if eps > 0: C_.check(f"[I] nu > 0 (kappa > 0, every eps) p={p} eps={eps}", all(v > 0 for v in r))
# [I'] kappa < 0: positivity of nu fails for |eps| beyond a threshold eps_c(p) < 0, where the hard-edge constant C_eps changes sign
#      (the negative piece's attraction T_-(0) < 0 overcomes T_+(0)); Prop 2 (iii) holds exactly for eps_c < eps < 0.
for p in (0.4, 0.6, 0.75):
    Cf = lambda e: (lambda E: mp.sqrt(E.a)*E.T(0)/mp.pi)(Eq(p, e))
    ec = mp.findroot(Cf, (mp.mpf('-0.6'), mp.mpf('-0.9')), solver='anderson')
    E1, E2 = Eq(p, ec*mp.mpf('0.98')), Eq(p, ec*mp.mpf('1.02'))
    n1, n2 = E1.nu(E1.a*mp.mpf('1e-6')), E2.nu(E2.a*mp.mpf('1e-6'))
    print(f"  [I'] p = {p}: eps_c = {mp.nstr(ec, 10)} (kappa < 0 needs n^p > |kappa|/|eps_c|); nu(1e-6 a) at 0.98 eps_c: {mp.nstr(n1, 5)}, at 1.02 eps_c: {mp.nstr(n2, 5)}")
    C_.check(f"[I'] threshold p={p}", -1 < ec < -0.5 and n1 > 0 and n2 < 0)

# [E] direct potentials (dps 15)
mp.mp.dps = 15
for (p, eps) in [(0.6, 0.3), (0.6, -0.3)]:
    E = Eq(p, eps); a = E.a
    band = [E.U(a*mp.mpf(t)) for t in ('0.1', '0.5', '0.9')]; l = band[1]
    spread = max(band) - min(band)
    print(f"\n  [E] p = {p}, eps = {eps}: U* on the band at x/a = 0.1, 0.5, 0.9: " + ", ".join(mp.nstr(u, 12) for u in band) + f" (spread {mp.nstr(spread, 3)})")
    C_.check(f"[E] U* constant on band p={p} eps={eps}", spread < 1e-9)
    pts = [a*mp.mpf('1.01'), a*2] + ([E.Y*mp.mpf('0.9')] if E.Y != mp.inf else [a*20])
    if eps < 0: pts += [-E.zp/2, -E.zp*mp.mpf('0.99'), -E.zp*2, mp.mpf(-0.01)]
    pts += [mp.mpc(1, 0.5), mp.mpc(-0.3, 0.2), mp.mpc(-2, -1), mp.mpc(a, 0.01), mp.mpc(0.01, 0.001)]
    for z in pts:
        d = E.U(z) - l
        print(f"      z = {mp.nstr(z, 6)}: U* - l = Re g - l = -Re phi = {mp.nstr(d, 8)}")
        C_.check(f"[E] Re phi < 0 at z={mp.nstr(z, 5)} p={p} eps={eps}", d > 0)

# [J] Toda bookkeeping (exact algebra, checked numerically at random parameters)
mp.mp.dps = 30
for (p, d, kap) in [(0.6, -0.3, 0.5), (0.75, -0.3, -0.5), (1.5, -0.7, 0.9)]:
    P, D, K = mp.mpf(p), mp.mpf(d), mp.mpf(kap); a = 1 + D
    zk = lambda k: mp.zeta(-k*P, a)
    def lhs(z):  # n = 1: eps = kappa
        zeta_ = z/(1 - K*z)
        return -sum(2*zk(k)/k*zeta_**k for k in range(1, 12)) + (1/P - 2*a)*mp.log(1 - K*z)
    co = mp.taylor(lhs, 0, 4)
    for j in range(1, 5):
        Zj = sum(mp.binomial(j, l)*K**(j - l)*zk(l) for l in range(0, j + 1)); Bj = -(1/P - 1)*K**j/j
        C_.check(f"[J] Toda time j={j} p={p}", abs(co[j] + (2*Zj/j - Bj)) < mp.mpf(10)**-25)
    print(f"  [J] p = {p}, delta = {d}, kappa = {kap}: Taylor coefficients 1..4 = -(2 Z_kappa(-j)/j - B_j): " + ", ".join(mp.nstr(co[j], 10) for j in range(1, 5)))
C_.finish()
