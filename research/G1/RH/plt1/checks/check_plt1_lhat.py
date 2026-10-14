"""Plan 15 Rule R F4 (NUMERICAL): continuous determination of lhat = 2 arg D_+ along (-inf, 0), 1/2 < p < 1.
Along arg z = pi (upper side) one has arg t = -pi/p, so D_+ depends on r := |t| only (N-independent). Track arg D_+ from
r = 1e12 (z -> 0-, D_+ -> 1) down to r = 1e-12 (z -> -inf) with step control, and compare the end value with the
claimed lhat(-inf)/2 = (pi/p - pi)/2. Reports max |arg D_+| (no wrap if < pi) per p."""
import mpmath as mp
mp.mp.dps = 40

def logD(r, p):
    L = mp.log(r) - 1j * mp.pi / p           # log t, continuous: arg t = -pi/p
    extra = int(max(0, mp.log10(r))) * 2 + 10
    with mp.workdps(mp.mp.dps + extra):
        tv = r * mp.expj(-mp.pi / p)
        return (tv - 0.5) * L - tv + 1j * mp.pi * tv + mp.loggamma(1 - tv) - mp.log(1j * mp.sqrt(2 * mp.pi))

worst = 0
for k in range(51, 100):
    p = mp.mpf(k) / 100
    us = [mp.mpf(12) - mp.mpf(24) * j / 4800 for j in range(4801)]   # log10 r from 12 to -12
    prev = None; tot = None; mx = 0
    for u in us:
        a = mp.im(logD(mp.mpf(10) ** u, p))
        if prev is None:
            tot = a
        else:
            d = a - prev; d -= 2 * mp.pi * mp.nint(d / (2 * mp.pi))
            assert abs(d) < 0.5, (p, u, d)
            tot += d
        prev = a; mx = max(mx, abs(tot))
    target = (mp.pi / p - mp.pi) / 2
    worst = max(worst, abs(tot - target))
    print(f"p={mp.nstr(p,3)}: max|arg D+| = {mp.nstr(mx,5)} (< pi: {mx < mp.pi}),  end = {mp.nstr(tot,8)}, (pi/p - pi)/2 = {mp.nstr(target,8)}")
print(f"max |end - target| = {mp.nstr(worst,3)}")
