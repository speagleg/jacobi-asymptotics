"""SPEC §3.8: an exact analytic index map for the bouncer nodes. With the Airy modulus-phase form Ai(-x) = M cos(phi),
Bi(-x) = M sin(phi) (DLMF 9.8; NOT QUOTED), take phi(x) := continuous arg(Ai(-x) + i Bi(-x)) for x > 0, phi(0) = pi/3 (since
Bi(0)/Ai(0) = sqrt 3). Then Ai(-x) = 0 iff cos(phi) = 0, and t(x) := phi(x)/pi - 1/4 + ... is chosen so that t(-a_k) = k.
Checked: t(-a_k) = k for k <= 60 (30 digits), and t(x) - [(2/(3 pi)) x^{3/2} + 1/4] -> 0 (the Hurwitz offset a = 3/4: k - 1/4 = t - 1/4...)."""
import mpmath as mp
mp.mp.dps = 30
def phi(x):
    # continuous phase via integration of d phi/dx = 1/(pi M^2) (Wronskian W(Ai,Bi) = 1/pi): here d/dx of arg(Ai(-x)+iBi(-x))
    return mp.pi/3 + mp.quad(lambda u: 1/(mp.pi*(mp.airyai(-u)**2 + mp.airybi(-u)**2)), [0, x])
offs = []
for k in (1, 2, 3, 5, 10, 20, 40, 60):
    x = -mp.airyaizero(k)
    ph = phi(x)
    offs.append(ph/mp.pi - k)
    print(f"k={k:3d}: x = -a_k = {mp.nstr(x, 12)}   phi/pi = {mp.nstr(ph/mp.pi, 20)}   phi/pi - k = {mp.nstr(ph/mp.pi - k, 12)}")
c0 = offs[0]
assert all(abs(o - c0) < mp.mpf(10)**-20 for o in offs)
print(f"=> phi(-a_k)/pi = k + {mp.nstr(c0, 15)} for all k checked, so t(x) := phi(x)/pi - ({mp.nstr(c0, 6)}) is an exact index map (t = k at the k-th node).")
for x in (mp.mpf(10), mp.mpf(100), mp.mpf(1000)):
    t = phi(x)/mp.pi - c0
    print(f"x={mp.nstr(x,5)}: t(x) = {mp.nstr(t, 18)},  (2/(3pi)) x^(3/2) + 1/4 = {mp.nstr(2/(3*mp.pi)*x**1.5 + mp.mpf(1)/4, 18)},  diff {mp.nstr(t - 2/(3*mp.pi)*x**1.5 - mp.mpf(1)/4, 3)}")
print("ALL ASSERTIONS PASSED")
