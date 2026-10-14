"""Paper 1, Lemma 3.3 sanity check (NUMERICAL, not a proof): for nu = omega_[0,1] - Unif[0,1],
-iint log|x-y| dnu dnu = -(log(1/4) - 2 log(1/4) - 3/2) = log(1/4) + 3/2, and the Fourier side is
int_0^oo |nu^(xi)|^2 / xi dxi with |nu^(xi)| = |J_0(xi/2) - sin(xi/2)/(xi/2)|."""
import mpmath as mp
mp.mp.dps = 20
f = lambda x: (mp.besselj(0, x/2) - mp.sinc(x/2))**2 / x
fourier = mp.quadosc(f, [0, mp.inf], period=4*mp.pi)
energy = mp.log(mp.mpf(1)/4) + mp.mpf(3)/2
print("Fourier side:", fourier)
print("energy side :", energy)
print("difference  :", mp.nstr(fourier - energy, 3), "(numerical quadrature of a slowly decaying oscillatory integrand; not an error bound)")
