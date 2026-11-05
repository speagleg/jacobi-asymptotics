"""JZC M3a, gap G2 (JZC_M3a_H_G12.md §2): the a-priori bound for the Hurwitz interpolant (NUMERICAL, mpmath dps 50).
Hurwitz measure sigma^d = sum_{k>=1} tau_k^{-s} delta_{tau_k^{-p}}, tau_k = k + d, a = 1 + d, alpha = (s-1-p)/p.
Moments m_j = zeta(s + j p, a) (Hurwitz zeta: the definition of the sum, nothing else). U_{j1}(z) := pi_j(z n^-p) with
pi_1 = P_n, pi_2 = P_{n-1} (monic OPs), U_{j2}(z) := sum_k n^p w_k U_{j1}(X_k)/(z - X_k) = sum_k w_k pi_j(x_k)/(zeta - x_k), zeta = z n^-p
(Paper 2 (eq:U-sum) up to the constant normalisations of U, which cancel in the bound since M below is computed for the same pi_j).
Claims checked:
  L2.1 (sum bound, Hurwitz):  |U_{j2}(z)| <= I1(z) <= I2(z) for 0 < |z| <= 1, |arg z| in {phi_1, pi/2, pi}, phi_1 = pi/6, where
       I1 = (M/sin phi_1)[sum_{tau_k <= T} tau_k^{p-s} + T^p sum_{tau_k > T} tau_k^{-s}],  T = n|z|^{-1/p},
       I2 = (M/sin phi_1)[max(a^g, T^g) + int_a^T u^g du + T^{p-s} + T^{1+p-s}/(s-1)],  g = p - s,  M = max_{[0, X_1]} |U_{j1}| (sampled:
       a lower estimate of M, so passing is conservative);
       and the exponent of |U_{j2}| as z -> 0 is alpha for alpha < 0 (0 for alpha > 0), the same for every d (no shift to alpha + 2d).
  L2.3 (Szego factor): D_{x^{2d}}(z) (eq:szego, quadrature) = (4cz/Upsilon)^d, and |(-z)^{-d} D_{x^{2d}}(z)| = |4c/Upsilon|^d in [1/2, 2] for |z| <= 1e-2.
Moments by mp.zeta (checked against hz below). Numerics of U_{j2}: direct sum for tau < tau_0, then either (A) the exact Hurwitz-zeta tail of the expansion 1/(zeta - x) = (1/zeta) sum (x/zeta)^r
(when |zeta| tau_0^p >= 4) or (B) Euler-Maclaurin from tau_0 = a + 60 (when |zeta| tau_0^p <= 1/4; derivatives from the exact power expansion,
integral by quadrature + exact tail). A and B are cross-validated where both apply."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 50
C_ = Checks(); I = mp.mpc(0, 1); PI = mp.pi


def monic_ops(n, p, s, a):
    m = [mp.zeta(s + j*p, a) for j in range(2*n + 1)]
    out = {}
    for deg in (n, n - 1):
        A = mp.matrix(deg, deg); b = mp.matrix(deg, 1)
        for i in range(deg):
            for j in range(deg): A[i, j] = m[i + j]
            b[i] = -m[deg + i]
        cs = mp.lu_solve(A, b) if deg > 0 else []
        out[deg] = [cs[i] for i in range(deg)] + [mp.mpf(1)]      # coefficients c_0..c_deg of pi(x) = sum c_i x^i
    return out[n], out[n - 1]


def hz(sig, b, J=30):
    """sum_{m>=0} (b+m)^{-sig} by direct summation to b+m >= max(60, sig) and Euler-Maclaurin (exact derivatives). mpmath's
    zeta(sig, b) is not used for the tails: it loses accuracy for large sig and b (relative error 4e-11 at sig = 20, b = 1200.5)."""
    tot = mp.mpf(0)
    while b < max(60, sig): tot += b**(-sig); b += 1
    tot += b**(1 - sig)/(sig - 1) + b**(-sig)/2
    return tot + sum(mp.bernoulli(2*j)/mp.factorial(2*j)*mp.rf(sig, 2*j - 1)*b**(-sig - 2*j + 1) for j in range(1, J + 1))


def poly(cs, x): return sum(c*x**i for i, c in enumerate(cs))


def S_A(zeta, cs, p, s, a, M0, R=90):
    tot = sum((a + m)**(-s)*poly(cs, (a + m)**(-p))/(zeta - (a + m)**(-p)) for m in range(M0))
    for i, ci in enumerate(cs):
        for r in range(R):
            tot += ci*zeta**(-1 - r)*hz(s + i*p + r*p, a + M0)
    return tot


def S_B(zeta, cs, p, s, a, M1=60, J=22, R=90):
    tot = sum((a + m)**(-s)*poly(cs, (a + m)**(-p))/(zeta - (a + m)**(-p)) for m in range(M1))
    t0 = a + M1
    g = lambda tau: tau**(-s)*poly(cs, tau**(-p))/(zeta - tau**(-p))
    def gder(k):   # k-th derivative at t0 from g = -sum_i c_i sum_r zeta^r tau^{p - s - i p + r p}
        return -sum(ci*zeta**r*mp.ff(p - s - i*p + r*p, k)*t0**(p - s - i*p + r*p - k) for i, ci in enumerate(cs) for r in range(R))
    vs = -mp.log(abs(zeta))/p; T1 = mp.exp(vs + mp.log(8)/p)      # |zeta| T1^p = 8
    v0, v1 = mp.log(t0), mp.log(T1)
    pts = sorted(set([v0, v1] + [x for x in (vs - 2, vs - 1, vs - 0.5, vs - 0.1, vs, vs + 0.1, vs + 0.5) if v0 < x < v1]
                     + [v0 + k*(vs - 2 - v0)/12 for k in range(1, 12)] if vs - 2 > v0 else [v0, v1]))
    integ = mp.quad(lambda v: g(mp.e**v)*mp.e**v, pts)
    integ += sum(ci*zeta**(-1 - r)*T1**(1 - (s + i*p + r*p))/((s + i*p + r*p) - 1) for i, ci in enumerate(cs) for r in range(R))
    em = integ + g(t0)/2 - sum(mp.bernoulli(2*j)/mp.factorial(2*j)*gder(2*j - 1) for j in range(1, J + 1))
    return tot + em


def S(zeta, cs, p, s, a):
    t0 = a + 60
    if abs(zeta)*t0**p <= mp.mpf(1)/4: return S_B(zeta, cs, p, s, a)
    M0 = int(mp.ceil((4/abs(zeta))**(1/p) - a)) + 1
    return S_A(zeta, cs, p, s, a, max(M0, 0))


def hsum(sig, a, K):     # sum_{m=0}^{K-1} (a+m)^{-sig}
    if K <= 0: return mp.mpf(0)
    if sig == 1: return mp.digamma(a + K) - mp.digamma(a)
    return mp.zeta(sig, a) - hz(sig, a + K)     # hz: EM continuation (valid for every sig != 1); mp.zeta is O(b) for sig < 1


n = 4; phi1 = PI/6
for (sig, b) in ((mp.mpf('2.75'), mp.mpf('0.1')), (mp.mpf(13), mp.mpf('0.5')), (mp.mpf('7.25'), mp.mpf(1)), (mp.mpf('-0.5'), mp.mpf(1000)), (mp.mpf('0.25'), mp.mpf('99.5'))):
    C_.check(f"moments: mp.zeta({sig},{b}) = hz", float(abs(mp.zeta(sig, b)/hz(sig, b) - 1)), 0.0, 1e-40)
# cross-validation of the two summation methods
for (p, s, d) in ((mp.mpf(3)/2, mp.mpf('1.75'), mp.mpf('-0.5')), (mp.mpf(3), mp.mpf('2.5'), mp.mpf('-0.9'))):
    a = 1 + d; P1, P0 = monic_ops(n, p, s, a)
    zeta = (mp.mpf('1e-4') if p < 2 else mp.mpf('5e-7'))*mp.expjpi(mp.mpf(1)/2)
    vA = S_A(zeta, P1, p, s, a, int(mp.ceil((4/abs(zeta))**(1/p))) + 1); vB = S_B(zeta, P1, p, s, a)
    print(f"cross-check p={mp.nstr(p,3)} s={s} d={d}: |S_A - S_B|/|S_A| = {mp.nstr(abs(vA - vB)/abs(vA), 3)}")
    C_.check(f"methods A/B agree p={mp.nstr(p,3)}", float(abs(vA - vB)/abs(vA)), 0.0, 1e-30)

radii = [mp.mpf(1), mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-16'), mp.mpf('1e-24')]
for (p, s) in ((mp.mpf(3)/2, mp.mpf('1.75')), (mp.mpf(3)/2, mp.mpf('2.5')), (mp.mpf(3)/2, mp.mpf('3.1')),
               (mp.mpf(3), mp.mpf('2.5')), (mp.mpf(3), mp.mpf('5.5'))):
    al = (s - 1 - p)/p; gam = p - s
    for d in (mp.mpf(0), mp.mpf('-0.5'), mp.mpf('-0.9')):
        a = 1 + d; P1, P0 = monic_ops(n, p, s, a); lab = f"p={mp.nstr(p,3)} s={s} (alpha={mp.nstr(al,3)}) d={d}"
        worst1, worst2, expo = 0, 0, []
        for cs in (P1, P0):
            M = max(abs(poly(cs, a**(-p)*k/2000)) for k in range(2001))
            mods = {}
            for r in radii:
                T = n*r**(-1/p); KT = int(mp.floor(T - a)) + 1
                I1 = (M/mp.sin(phi1))*(hsum(s - p, a, KT) + T**p*hz(s, a + KT))
                integ = mp.log(T/a) if gam == -1 else (T**(1 + gam) - a**(1 + gam))/(1 + gam)
                I2 = (M/mp.sin(phi1))*(max(a**gam, T**gam) + integ + T**(p - s) + T**(1 + p - s)/(s - 1))
                for ang in (phi1/PI, mp.mpf(1)/2, mp.mpf(1)):
                    z = r*mp.expjpi(ang); U2 = S(z/n**p, cs, p, s, a)
                    worst1 = max(worst1, abs(U2)/I1); worst2 = max(worst2, I1/I2)
                    if ang == mp.mpf(1)/2: mods[r] = abs(U2)
            expo.append(mp.log(mods[radii[-2]]/mods[radii[-1]])/mp.log(radii[-2]/radii[-1]))
        target = al if al < 0 else 0
        print(f"L2.1 {lab}: max |U_j2|/I1 = {mp.nstr(worst1,4)}, max I1/I2 = {mp.nstr(worst2,4)}; "
              f"exponent of |U_j2(iy)| (1e-16 -> 1e-24): {mp.nstr(expo[0],8)}, {mp.nstr(expo[1],8)} (alpha+2d = {mp.nstr(al+2*d,3)})")
        C_.check(f"L2.1 |U_j2| <= I1 {lab}", float(max(worst1 - 1, 0)), 0.0, 0.0)
        C_.check(f"L2.1 I1 <= I2 {lab}", float(max(worst2 - 1, 0)), 0.0, 0.0)
        if al != 0:
            for e in expo: C_.check(f"L2.1 exponent = min(alpha,0), d-free {lab}", float(e - target), 0.0, 1e-4)

# L2.3: Szego function of x^{2d}
c = mp.mpf('0.7')
def Rr(z): return z*mp.sqrt(1 - 4*c/z)
def Ups(z): return (mp.sqrt(z) + mp.sqrt(z - 4*c))**2
def Dq(z, d):
    x = lambda ph: 4*c*mp.sin(ph/2)**2                       # = 2c(1 - cos ph), without cancellation
    lx = lambda ph: mp.log(4*c) + 2*mp.log(mp.sin(ph/2))      # log x, finite for every ph in (0, pi]
    pts = [0, PI]
    if 0 < mp.re(z) < 4*c:
        ph0 = mp.acos(1 - mp.re(z)/(2*c)); w = abs(mp.im(z))/(2*c) + mp.mpf('1e-30')
        pts = sorted(set([0, PI] + [ph0 + k*w for k in (-1e3, -10, -1, 0, 1, 10, 1e3) if 0 < ph0 + k*w < PI]))
    elif abs(z) < 4*c:
        pts = sorted(set([0, PI] + [mp.sqrt(abs(z)/c)*k for k in (0.1, 1, 10, 100) if mp.sqrt(abs(z)/c)*k < PI]))
    E = Rr(z)/(2*PI)*mp.quad(lambda ph: 2*d*lx(ph)/(z - x(ph)) if ph > 0 else mp.mpf(0), pts)
    return mp.exp(E)
for d in (mp.mpf('-0.3'), mp.mpf('-0.9')):
    worst, gmin, gmax = 0, mp.inf, 0
    for z in (mp.mpf('1e-6')*I, mp.mpf('1e-6')*mp.expj(PI - mp.mpf('0.01')), mp.mpf('1e-3')*mp.expj(mp.mpf('0.3')), mp.mpf('0.5')*I,
              mp.mpf(-2), mp.mpc(3, '0.1'), 10*mp.expj(2)):
        e_ = abs(Dq(z, d)/(4*c*z/Ups(z))**d - 1)
        worst = max(worst, e_ if mp.isfinite(e_) else mp.inf)     # a nan must fail, not vanish in max()
    for r in (mp.mpf('1e-2'), mp.mpf('1e-5'), mp.mpf('1e-10')):
        for ang in (mp.mpf('0.01'), mp.mpf(1)/2, mp.mpf('0.99'), mp.mpf('-0.5')):
            z = r*mp.expjpi(ang); G = abs(mp.power(-z, -d))*abs(4*c*z/Ups(z))**d
            gmin, gmax = min(gmin, G), max(gmax, G)
    print(f"L2.3 d={d}: max |D_q/(4cz/Ups)^d - 1| = {mp.nstr(worst,3)};  |G| range on |z| <= 1e-2: [{mp.nstr(gmin,6)}, {mp.nstr(gmax,6)}]")
    C_.check(f"L2.3 D_(x^2d) = (4cz/Ups)^d d={d}", float(worst), 0.0, 1e-25)
    C_.check(f"L2.3 (control) D_(x^2d) != (4cz/Ups)^(2d) d={d}", float(abs(Dq(mp.mpf('0.5')*I, d)/(2*c*I/Ups(mp.mpf('0.5')*I))**(2*d) - 1)), 1.0, 0.99)
    C_.check(f"L2.3 |G| in [1/2, 2] d={d}", float(max(gmax - 2, 0.5 - gmin, 0)), 0.0, 0.0)
C_.finish()
