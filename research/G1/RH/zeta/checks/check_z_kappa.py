"""Plan 13 (Z3) (NUMERICAL): asymptotics of the edge prediction beta_N/(4 x_N) for the smooth-zeta model.
Prediction from regular variation: beta_N = x(T), T J(p - eps) ~ N, eps = t l'(t)/l(t) ~ 2/log t (x(t) ~ t^{-2} l(t)):
    beta_N/(4 x_N) = c(2) (1 + kappa_rel/log N + O(log^{-2} N)),
    kappa_rel = -2 (2 J'(2)/J(2) + log J(2)) = -2 (-(1/2)(psi(3/2) - psi(1)) + log(pi/2)) = -0.28946...
Reports log N (beta_N/(4 x_N c2) - 1) for N up to 1e15 (edge equation only; no OPs needed)."""
import mpmath as mp

mp.mp.dps = 30
c2 = mp.pi ** 2 / 16
J = mp.pi / 2
dlogJ = -(mp.digamma(1.5) - mp.digamma(1)) / 4
kappa = -2 * (2 * dlogJ + mp.log(J))
print(f"predicted kappa_rel = {mp.nstr(kappa, 10)}")
N0 = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8
def xt(tv):  # atom as a function of index t: x = 1/(gamma^2 + 1/4), N0(gamma) = t - 1/2, gamma > 2 pi
    y = (tv - mp.mpf(1) / 2 - mp.mpf(7) / 8) / mp.e   # Lambert W closed form (toolkit Ninv), principal branch
    g = 2 * mp.pi * mp.e * mp.exp(mp.re(mp.lambertw(y)))
    return mp.re(1 / (g * g + mp.mpf(1) / 4))
def beta(N):
    # index form of the edge equation: (1/N) int_{3/8}^{T} (1 - x(T)/x(t))^{-1/2} dt = 1, solve for T
    def E(T):
        xT = xt(T)
        f = lambda u: 2 * u / mp.sqrt(abs(1 - xT / xt(T * (1 - u * u)))) * T  # t = T(1-u^2), removes endpoint singularity
        umax = mp.sqrt(1 - mp.mpf(3) / 8 / T)
        return mp.quad(f, [0, mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), umax]) / N
    T = mp.findroot(lambda T: E(T) - 1, (N / J * mp.mpf("0.8"), N / J * mp.mpf("1.2")), solver="anderson")
    return xt(T)
for e in (2, 3, 4, 6, 8, 10, 12, 15):
    N = mp.mpf(10) ** e
    r = beta(N) / (4 * xt(N) * c2) - 1
    print(f"N=1e{e:<3d} beta/(4 x_N c2) - 1 = {mp.nstr(r, 8):>14}   log N * (.) = {mp.nstr(mp.log(N) * r, 8)}")
