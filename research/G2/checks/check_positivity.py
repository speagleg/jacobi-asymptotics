"""G2 Lemma EP (Plan 47) Rule A check (NUMERICAL): the Fourier identity
    -iint log|x-y| dnu dnu = int_0^inf |nu^(xi)|^2 / xi dxi,   nu^(xi) = int e^{i xi x} dnu(x),
for zero-mass signed measures nu with log-integrable |nu|, on cases with closed-form left-hand sides.
[1] nu = omega_1 - omega_4 (arcsine laws on [0,1], [0,4]); LHS = log 4 by Lemma B0
    (I(omega_b) = log(b/4); mutual = int U_4 d omega_1 = log(4/4) = 0). nu^ of omega_b is e^{i xi b/2} J0(xi b/2).
[2] nu = U[0,1] - U[0,2] (uniform laws); LHS = -[I(U1) - 2 I(U1,U2) + I(U2)], with I(U[0,L]) = log L - 3/2 and the
    mutual energy by 2-d quadrature.
[3] Negative control (hypothesis nu(R) = 0 dropped): nu = omega_8 has -I = -log 2 < 0, so positivity needs mass 0.
Not a proof; the proof is PROOF.md Lemma EP."""
import numpy as np
from scipy import integrate, special


def fourier_side(nuhat, cut=4000.0):
    f = lambda xi: abs(nuhat(xi)) ** 2 / xi
    edges = np.concatenate(([0.0], np.geomspace(1e-6, cut, 400)))
    tot = sum(integrate.quad(f, a, b, limit=200)[0] for a, b in zip(edges[:-1], edges[1:]))
    # tail beyond cut not integrated: for [1] |nuhat|^2 averages ~ 5/(2 pi xi) - 1/(pi xi) = 3/(2 pi xi) (the cross
    # term has a non-oscillating part), so the tail is ~ (3/(2 pi))/cut = 1.19e-4 at cut 4000, matching the [1] diff
    # (corrected after Rule R, REVIEW_Plan47.md F5; was (5/(4 pi))/cut); it is O(1/cut^2) for [2]
    return tot


arc = lambda b: (lambda xi: np.exp(1j * xi * b / 2) * special.j0(xi * b / 2))
nu1 = lambda xi: arc(1.0)(xi) - arc(4.0)(xi)
lhs1 = np.log(4.0)
rhs1 = fourier_side(nu1)
print(f"[1] omega_1 - omega_4: LHS = log 4 = {lhs1:.6f}, Fourier side (cut 4000) = {rhs1:.6f}, diff = {rhs1-lhs1:+.2e}")

uni = lambda L: (lambda xi: (np.exp(1j * xi * L) - 1) / (1j * xi * L))
nu2 = lambda xi: uni(1.0)(xi) - uni(2.0)(xi)
I1, I2 = -1.5, np.log(2) - 1.5
# mutual energy: int_0^1 int_0^2 log|x-y| dy/2 dx; inner integral in closed form
F = lambda x: 0.5 * (((2 - x) * np.log(2 - x) - (2 - x)) + (x * np.log(x) - x if x > 0 else 0.0))
I12 = integrate.quad(F, 0, 1, limit=200)[0]
lhs2 = -(I1 - 2 * I12 + I2)
rhs2 = fourier_side(nu2)
print(f"[2] U[0,1] - U[0,2]: LHS = {lhs2:.6f}, Fourier side (cut 4000) = {rhs2:.6f}, diff = {rhs2-lhs2:+.2e}")

print(f"[3] negative control omega_8 (mass 1): -I = -log 2 = {-np.log(2):.6f} < 0 (Lemma EP needs nu(R) = 0)")
print("PASS" if abs(rhs1 - lhs1) < 1e-3 and abs(rhs2 - lhs2) < 1e-3 and lhs1 > 0 and lhs2 > 0 else "FAIL")
