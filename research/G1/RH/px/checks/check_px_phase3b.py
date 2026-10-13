"""Plan 12 Phase 3b (NUMERICAL): the scalar function F := D * S * (4c - z)^{-1/2}.
S(z) := exp( -(1/2 pi i) int_{-inf}^0 ell(y) [1/(y - z) - 1/(y - 1)] dy ),  ell(y) := log(D_+/D_-)(y) = 2 i arg D_+(y)
(continuous branch, ell(0-) = 0).  Then S_+/S_- = D_-/D_+ on (-inf,0) (Plemelj), S is analytic off (-inf,0].
 [1] DS has no jump on (-inf,0): |(DS)_+/(DS)_- - 1|.
 [2] S near 0 (bounded, nonzero, continuous): S(+-i eps), S(eps).
 [3] F -> const at infinity in every direction (predicted: S ~ z^{1/2 - 1/(2p)}, D ~ z^{1/(2p)}, so DS ~ z^{1/2}).
 [4] F's jump on (4c, inf) away from nodes: F_+/F_- = D_+/D_- * (-1) = e^{2 i theta}  (-e^{2i theta} from D, -1 from E),
     so conjugation by F^{sigma3} removes T's diag(e^{-2i theta}, e^{2i theta}) exactly."""
import mpmath as mp

mp.mp.dps = 30
p, N = mp.mpf(2), 20
I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
c4 = 4 * (mp.pi / (2 * I)) ** p / 4
t = lambda z: N * mp.power(z, -1 / p)
Dt = lambda z: mp.sqrt(2 * mp.pi) * mp.exp((t(z) - 0.5) * mp.log(t(z)) - t(z) - mp.loggamma(t(z)))
def D(z):
    sg = 1 if mp.im(z) > 0 else -1
    return Dt(z) / (1 - mp.exp(-sg * 2j * mp.pi * t(z)))
e = mp.mpf("1e-25")
def argDp(y):  # continuous arg of D_+ on (-inf,0); numerically |arg| < pi here so principal arg is continuous
    return mp.arg(D(y + 1j * e))
ell = lambda y: 2j * argDp(y)
def S(z):
    f = lambda u: ell(-mp.exp(u)) * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u)
    pts = [-60, -20, -5, 0, 5, 20, 40, 80]
    if mp.re(z) < 0:  # near-contour evaluation: put a breakpoint (and a fine window) at the singularity u = log|Re z|
        u0 = mp.log(-mp.re(z)); w = 50 * abs(mp.im(z)) / abs(mp.re(z)) + mp.mpf("1e-30")
        pts = sorted(set(pts + [u0 - 1, u0 - w, u0, u0 + w, u0 + 1]))
    val = mp.quad(f, pts)
    return mp.exp(-val / (2j * mp.pi))
E = lambda z: mp.power(c4 - z, -0.5)
F = lambda z: D(z) * S(z) * E(z)
print(f"p={p} N={N} 4c={mp.nstr(c4,8)}")
print("[1] (DS)_+/(DS)_- - 1 on (-inf,0):")
for x in ("-1e-3", "-1", "-1e3", "-1e6"):
    x = mp.mpf(x); h = mp.mpf("1e-10") * abs(x)
    r = D(x + 1j * h) * S(x + 1j * h) / (D(x - 1j * h) * S(x - 1j * h)) - 1
    print(f"   x={mp.nstr(x,3)}: {mp.nstr(abs(r), 3)}")
print("[2] S near 0:", [mp.nstr(S(z), 6) for z in (mp.mpc(0, 1e-6), mp.mpc(0, -1e-6), mp.mpf(1e-6), mp.mpc(-1e-6, 1e-9))])
print("[3] F at infinity:")
for R in ("1e6", "1e10", "1e14"):
    print(f"   |z|={R}:", [mp.nstr(F(mp.mpf(R) * mp.expjpi(a)), 6) for a in (0.1, 0.5, 0.9, -0.5)])
print("[4] F_+/F_- vs e^{2 i theta} on (4c, inf), off nodes:")
for x in (c4 * 1.3, mp.mpf(N) ** p * 0.77, mp.mpf(N) ** p * 5):
    h = mp.mpf("1e-12")
    r = F(x + 1j * h) / F(x - 1j * h) / mp.exp(2j * mp.pi * t(x)) - 1
    print(f"   x={mp.nstr(x,5)}: |ratio-1| = {mp.nstr(abs(r),3)}")
