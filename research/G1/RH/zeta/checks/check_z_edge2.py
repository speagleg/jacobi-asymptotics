"""Plan 13 (NUMERICAL): canonical edge equation (index form, constraint only on the monotone branch t >= 3/8 of
t(x) = N0(gamma(x)) + 1/2, i.e. x <= x_e = 1/(4 pi^2 + 1/4)):
      (1/N) int_{3/8}^{T} (1 - x(T)/x(t))^{-1/2} dt = 1,   beta_N := x(T).
Compares b_N (toolkit, J = 800k) with beta_N/4.  (check_z_edge.py used |t'| over (0,4), which also counts the
non-monotone leg x in (x_e, 4) and shifts beta_N by O(1/N).)"""
import numpy as np
import mpmath as mp
from jacobi_asym.measures import smooth_zeta
from jacobi_asym.jacobi import jacobi_coeffs

mp.mp.dps = 30
J = mp.pi / 2
def xt(tv):
    y = (tv - mp.mpf(1) / 2 - mp.mpf(7) / 8) / mp.e
    g = 2 * mp.pi * mp.e * mp.exp(mp.re(mp.lambertw(y)))
    return mp.re(1 / (g * g + mp.mpf(1) / 4))
def beta(N):
    def E(T):
        xT = xt(T)
        f = lambda u: 2 * u / mp.sqrt(abs(1 - xT / xt(T * (1 - u * u)))) * T
        umax = mp.sqrt(1 - mp.mpf(3) / 8 / T)
        return mp.quad(f, [0, mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), umax]) / N
    T = mp.findroot(lambda T: E(T) - 1, (N / J * mp.mpf("0.8"), N / J * mp.mpf("1.2")), solver="anderson")
    return xt(T)
mu = smooth_zeta(800_000)
r = jacobi_coeffs(mu, 3300)
b = np.sqrt(r.b2)
print("    N     b_N/(beta_N/4) - 1     N*(.)")
for N in (50, 100, 200, 400, 800, 1600, 3200):
    d = b[N - 1] / float(beta(mp.mpf(N)) / 4) - 1
    print(f"  {N:5d}   {d:+.6e}      {N*d:+.4f}")
