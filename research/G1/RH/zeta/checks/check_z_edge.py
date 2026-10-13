"""Plan 13 (NUMERICAL): finite-N edge equation for the smooth-zeta model.
Generalizing G2 B*: for a decreasing node density rho_N, the superposition mu = int_0^1 omega_{[0,beta(tau)]} dtau
saturates rho_N beyond its band edge beta iff (Abel inversion, mass 1)
      E_N(beta) := int_beta^inf sqrt(x/(x - beta)) rho_N(x) dx = 1,     rho_N := |t'(x)|/N,
t(x) = N0(gamma(x)) + 1/2, gamma(x) = sqrt(1/x - 1/4) (t(x_j) = j at the model atoms).  Prediction: b_N ~ beta_N/4.
 [0] pure-power sanity: rho = (1/p) x^{-1-1/p} gives beta = 4c(p).
 [1] smooth zeta: N, b_N (toolkit, J = 800k), beta_N/4, and b_N/(beta_N/4) - 1 (times N), vs b_N/x_N - c(2).
The x-integral is cut at x = 4 (gamma = 0), where t -> 11/8; the remaining far-end mass is reported."""
import numpy as np
import mpmath as mp
from jacobi_asym.measures import smooth_zeta
from jacobi_asym.jacobi import jacobi_coeffs

mp.mp.dps = 30
def edge_powers(p):
    p = mp.mpf(p)
    E = lambda b: mp.quad(lambda x: mp.sqrt(x / (x - b)) * mp.power(x, -1 - 1 / p) / p, [b, 2 * b, 10 * b, mp.inf])
    beta = mp.findroot(lambda b: E(b) - 1, 2)
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
    return beta, 4 * (mp.pi / (2 * I)) ** p / 4
for p in (1.5, 2, 3):
    b, c4 = edge_powers(p)
    print(f"[0] p={p}: beta={mp.nstr(b,12)}  4c(p)={mp.nstr(c4,12)}")
def N0(g):
    return g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8
def t(x):
    return N0(mp.sqrt(1 / x - mp.mpf(1) / 4)) + mp.mpf(1) / 2
def dt(x):  # analytic: t'(x) = N0'(gamma) gamma'(x), N0'(g) = log(g/2pi)/(2pi), gamma' = -1/(2 x^2 gamma)
    g = mp.sqrt(1 / x - mp.mpf(1) / 4)
    return mp.log(g / (2 * mp.pi)) / (2 * mp.pi) * (-1 / (2 * x * x * g))
def beta_N(N):
    # change variables x = b(1+u^2): sqrt(x/(x-b)) dx = 2 b sqrt(1+u^2) du, removes the endpoint singularity
    def E(b):
        umax = mp.sqrt(4 / b - 1)
        f = lambda u: 2 * b * mp.sqrt(1 + u * u) * abs(dt(b * (1 + u * u))) / N
        return mp.quad(f, [0, mp.mpf("0.1"), 1, 10, 100, umax])
    gN = mp.findroot(lambda g: N0(g) - (N - mp.mpf(1) / 2), 2 * mp.pi * N / mp.log(N + 2))
    guess = (mp.pi ** 2 / 4) / (gN ** 2 + mp.mpf(1) / 4)       # 4 c(2) x_N
    lo, hi = guess / 3, guess * 3
    return mp.findroot(lambda b: E(b) - 1, (lo, hi), solver="anderson")
mu = smooth_zeta(800_000)
r = jacobi_coeffs(mu, 3300)
b = np.sqrt(r.b2); x = mu.atoms
c2 = np.pi ** 2 / 16
print("[1]   N      b_N/x_N-c2    b_N/(beta_N/4)-1    N*(.)       b_{N+1}/(beta_N/4)-1")
for N in (50, 100, 200, 400, 800, 1600, 3200):
    B = beta_N(N) / 4
    d0 = b[N - 1] / float(B) - 1; d1 = b[N] / float(B) - 1
    print(f"   {N:5d}  {b[N-1]/x[N-1]-c2:+.5e}    {d0:+.5e}      {N*d0:+.4f}     {d1:+.5e}")
