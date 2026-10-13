"""Plan 10 Phase 5 (NUMERICAL acceptance tests), p = 2.
Symmetric recurrence gamma_N^2 obtained by unfolding the x-variable coefficients (a_m, b_m) of sigma_{p,r} (with the
Euler-Maclaurin tail, as in check_fine): gamma_1^2 = a_1, gamma_{2m}^2 = b_m^2/gamma_{2m-1}^2, gamma_{2m+1}^2 = a_{m+1} - gamma_{2m}^2.
[A] Outer strong asymptotics: T11(z) := N^{qN} pi_N(N^{-q} z) e^{-N g(z)} (Omega_inf), for z off the band.
    The RH analysis predicts T11 = O(N^{+-1/2}) (D E normalization) times a limit; so ratios T11(z1)/T11(z2) must converge
    at rate 1/N (a wrong g would give exponential drift).
[B] Extraction: kappa_N := gamma_N^2 / (c(p) (N/2)^{-p}) - 1; fit kappa_N = (k0 + k1 (-1)^N)/N + O(N^-2)."""
import sys
import numpy as np
import mpmath as mp
sys.path.insert(0, "research/G1/RH/checks")
from check_fine import power_with_tail
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

mp.mp.dps = 30
p = 2
q = mp.mpf(p) / 2
rs = 2 ** (1 + q) * mp.sqrt(c_p(p))


def gammas(r, M, K=30_000):
    jc = jacobi_coeffs(power_with_tail(p, r, K), M + 2, prec="ld")
    a = [mp.mpf(float(v)) for v in jc.a]; b2 = [mp.mpf(float(v)) for v in jc.b2]
    g2 = [mp.mpf(0)]                      # gamma_0^2 = 0
    for m in range(1, M + 1):
        g2.append(a[m - 1] - g2[-1])      # gamma_{2m-1}^2
        g2.append(b2[m - 1] / g2[-1])     # gamma_{2m}^2
    return g2                             # index N -> gamma_N^2 (N = 1..2M)


def g(z):
    return mp.quad(lambda t: mp.log((z + z * mp.sqrt(1 - (rs * t ** (-q) / z) ** 2)) / 2), [0, 1])


def T11(z, N, g2):
    s = z / mp.power(N, q)
    a, b = mp.mpf(1), s                    # R_0, R_1 (monic, zero diagonal)
    for n in range(1, N):
        a, b = b, s * b - g2[n] * a
    return mp.power(N, q * N) * b * mp.exp(-N * g(z))


for r in (2, 3):
    g2 = gammas(r, 120)
    print(f"r={r} (alpha = {(2*r-2-p)/(2*p)}):")
    z1, z2, z3 = mp.mpc(0, 2), mp.mpc(3, 3), mp.mpc(-5, 1)
    for N in (20, 40, 80, 160, 240):
        t1, t2, t3 = T11(z1, N, g2), T11(z2, N, g2), T11(z3, N, g2)
        print(f"   [A] N={N:3d}: |T11(2i)| = {mp.nstr(abs(t1),6)}  T11(3+3i)/T11(2i) = {mp.nstr(t2/t1,8)}  T11(-5+i)/T11(2i) = {mp.nstr(t3/t1,8)}")
    Ns = np.arange(40, 241)
    kap = np.array([float(g2[N] / (c_p(p) * (N / 2.0) ** (-p)) - 1) for N in Ns])
    A = np.vstack([1 / Ns, (-1.0) ** Ns / Ns, 1 / Ns ** 2, (-1.0) ** Ns / Ns ** 2]).T
    k = np.linalg.lstsq(A, kap, rcond=None)[0]
    print(f"   [B] gamma_N^2/(c (N/2)^-p) - 1 = ({k[0]:+.4f} {k[1]:+.4f}(-1)^N)/N + ({k[2]:+.3f} {k[3]:+.3f}(-1)^N)/N^2")
