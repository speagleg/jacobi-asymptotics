"""Rule R checks of CG.md S4, S5, S8 (NUMERICAL, mpmath).

(1) |f'(0)| = pi^2 C_*^2 = 1/(c(p)(p+2)^2), with C_* = lim x^{1/2} psi*(x) computed from the incomplete beta form of
    psi* (Paper II prop:equilibrium(i)) by mpmath quadrature at small x and Richardson in x (psi* = C_* x^{-1/2}(1+O(x))).
(2) Bessel column: with Psi e1 = (I_a(2 r), 2 pi i r I_a'(2 r)), r = zeta^{1/2} (KMVV (6.23)), and
    sigma3 Psi e1 = zeta^{a/2} (beta1, beta2), compute W(zeta) = beta1' beta2 - beta2' beta1 from mpmath besseli
    (not from the series) at small zeta on the ray arg zeta = -pi/2, and compare with 2 pi i/(Gamma(a+1)Gamma(a+2)).
(3) Branch: (-X)^{-a/2} zeta^{a/2} = (zeta/(-X))^{a/2} at X = iy, zeta = n^2 f(X), f(X) ~ f'(0) X.
"""
import mpmath as mp

mp.mp.dps = 40


def cconst(p):
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
    return (mp.pi / (2 * I)) ** p / 4


def psistar(x, p):
    c = cconst(p)
    lam = x ** (-1 - 1 / p) / p
    return lam * mp.betainc(1 / p + 0.5, 0.5, 0, x / (4 * c), regularized=True)


for p in [mp.mpf('0.6'), mp.mpf('2.5'), mp.mpf('0.3'), mp.mpf(4)]:
    c = cconst(p)
    xs = [mp.mpf(10) ** (-k) for k in (6, 7)]
    v = [mp.sqrt(x) * psistar(x, p) for x in xs]
    Cs = (10 * v[1] - v[0]) / 9  # Richardson for 1 + O(x)
    print(f"p={p}: pi^2 C*^2 = {mp.nstr(mp.pi**2*Cs**2, 20)}, 1/(c(p+2)^2) = {mp.nstr(1/(c*(p+2)**2), 20)}, "
          f"rel diff {mp.nstr(mp.pi**2*Cs**2*c*(p+2)**2-1, 3)}")

for a in [mp.mpf('0.5'), mp.mpf('0.6'), mp.mpf('-0.7'), mp.mpf(0), mp.mpf(3)]:
    def b(z):
        r = mp.sqrt(z)
        Ia = mp.besseli(a, 2 * r)
        dIa = mp.besseli(a, 2 * r, derivative=1)
        return mp.matrix([Ia * z ** (-a / 2), -2j * mp.pi * r * dIa * z ** (-a / 2)])
    z0 = mp.mpf('1e-12') * mp.expj(-mp.pi / 2)
    h = mp.mpf('1e-14')
    B0 = b(z0); Bp = (b(z0 + h) - b(z0 - h)) / (2 * h)
    W = Bp[0] * B0[1] - Bp[1] * B0[0]
    print(f"alpha={a}: W = {mp.nstr(W, 15)}, target 2 pi i/(G(a+1)G(a+2)) = "
          f"{mp.nstr(2j*mp.pi/(mp.gamma(a+1)*mp.gamma(a+2)), 15)}")

# branch check
for a in [mp.mpf('0.5'), mp.mpf('-0.7'), mp.mpf('2.3')]:
    fp = -mp.mpf('0.37')  # f'(0) < 0
    for y in [mp.mpf('1e-3'), mp.mpf('0.1')]:
        X = 1j * y
        fX = fp * X * (1 + mp.mpf('0.2') * X)  # analytic f with f(0)=0, f'(0)<0
        n = 50
        zeta = n ** 2 * fX
        lhs = (-X) ** (-a / 2) * zeta ** (a / 2)
        rhs = (n ** 2 * fX / (-X)) ** (a / 2)
        print(f"alpha={a} y={y}: |lhs-rhs|/|rhs| = {mp.nstr(abs(lhs-rhs)/abs(rhs), 3)}")
