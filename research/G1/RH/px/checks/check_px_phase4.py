"""Plan 12 Phase 4 (NUMERICAL): local objects.
 [1] Hard-edge conformal map f := (phi +- i pi)^2/4 in C+-: continuous across the band (0,delta) and across (-delta,0)
     (so analytic in U(0,delta)), f(z)/z -> f'(0) < 0 (band -> arg zeta = pi, outside -> zeta > 0, KMVV orientation).
 [2] Soft edge 4c: phit(z) / (z - 4c)^{3/2} -> const (Airy, WLXZ (6.11) analogue), Re phit < 0 to the right.
 [3] Hard-edge mismatch: on the lip ray arg z = pi/3 (preimage of arg zeta = -2pi/3 to leading order) the discarded
     factors |e^{-2 i theta}| (D/Dt - 1) and |e^{-2N phit}| (upper-right) times the Bessel amplification
     (N^2 |z|)^{-|alpha|} (alpha = 3, i.e. s = 1 + 4p) stay below N^{-K}: report log10 of the product."""
import mpmath as mp

mp.mp.dps = 30
p = mp.mpf(2)
I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
c = (mp.pi / (2 * I)) ** p / 4
l = 2 * (mp.log(c) + p)
def g(z):
    f = lambda tau: 2 * mp.log((mp.sqrt(z) + mp.sqrt(z - 4 * c * tau ** (-p))) / 2)
    return mp.quad(f, [0, mp.mpf("1e-8"), mp.mpf("1e-4"), mp.mpf("0.01"), 0.5, 1])
phi = lambda z: l / 2 - g(z)
def fmap(z):
    sg = 1 if mp.im(z) > 0 else -1
    return (phi(z) + sg * 1j * mp.pi) ** 2 / 4
e = mp.mpf("1e-25")
print(f"p={p}: 4c={mp.nstr(4*c,8)}")
print("[1] f continuity and f(z)/z near 0")
for x in ("0.01", "0.1", "-0.01", "-0.1"):
    x = mp.mpf(x)
    fp, fm = fmap(x + 1j * e), fmap(x - 1j * e)
    print(f"   x={mp.nstr(x,3)}: f+={mp.nstr(fp,8)}  |f+-f-|={mp.nstr(abs(fp-fm),2)}  f/x={mp.nstr(fp/x,8)}")
for z in (mp.mpc(0.003, 0.004), mp.mpc(-0.002, 0.001), mp.mpc(0.0005, -0.0002), mp.mpc(1e-5, 2e-5)):
    print(f"   z={mp.nstr(z,3)}: f(z)/z = {mp.nstr(fmap(z)/z, 8)}")
print("[2] phit near 4c")
phit = lambda z: phi(z) + 1j * mp.pi * mp.power(z, -1 / p)
for d in ("1e-2", "1e-3", "1e-4"):
    z = 4 * c + mp.mpf(d) * mp.expjpi(mp.mpf("0.25"))
    print(f"   |z-4c|={d}: phit/(z-4c)^(3/2) = {mp.nstr(phit(z)/mp.power(z-4*c, 1.5), 8)}   Re phit(4c+{d}) = {mp.nstr(mp.re(phit(4*c+mp.mpf(d)+1j*e)),4)}")
print("[3] hard-edge mismatch x amplification, log10, alpha = 3, lip ray arg z = pi/3")
for N in (20, 80, 320):
    row = []
    for r in ("1e-1", "1e-3", "1e-6", "1e-10"):
        z = mp.mpf(r) * mp.expjpi(mp.mpf(1) / 3)
        th = mp.pi * N * mp.power(z, -1 / p)
        m1 = abs(mp.exp(-2j * th))
        m2 = abs(mp.exp(-2 * N * phit(z))) if mp.mpf(r) >= mp.mpf("1e-6") else mp.mpf(0)
        amp = (N ** 2 * mp.mpf(r)) ** (-3)
        row.append(f"|z|={r}: {mp.nstr(mp.log10(max(m1, m2) * max(amp, 1) + mp.mpf('1e-100000')), 5)}")
    print(f"   N={N}: " + "  ".join(row))
