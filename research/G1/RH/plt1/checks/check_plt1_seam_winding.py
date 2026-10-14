"""Plan 15b Lemma S(iii) (NUMERICAL): along the upper seam z = r e^{i th_s}, th_s = pi p/2, the continuous
determination of L = log(D B_in / B_out), started at 0 (z -> 0, L -> 0), tends to 0 (no 2 pi k) as z -> infinity.
D = Dt/(1 - e^{-2 pi i t}) principal (|arg t| = pi/2 on the seam), B_in = (1+z)^{1/2-1/(2p)}, B_out = (1 - z/(2 pi N))^{1/2}.
The lower seam is the complex conjugate."""
import mpmath as mp
mp.mp.dps = 30

def L(r, p, N):
    z = r * mp.expj(mp.pi * p / 2)
    lt = mp.log(N) - mp.log(z) / p
    t = mp.exp(lt)
    if abs(t) > 1e3:
        ld = -(1 / (12 * t) - 1 / (360 * t ** 3))
        w = -2j * mp.pi * t
        ld -= mp.log(1 - mp.exp(w)) if mp.re(w) > -80 else 0
    else:
        with mp.workdps(60):
            ld = mp.log(mp.sqrt(2 * mp.pi)) + (t - 0.5) * lt - t - mp.loggamma(t) - mp.log(-mp.expm1(-2j * mp.pi * t))
    c = mp.mpf(1) / 2 - 1 / (2 * p)
    return ld + c * mp.log(1 + z) - 0.5 * mp.log(1 - z / (2 * mp.pi * N))

worst = 0
for p in [mp.mpf(k) / 20 for k in range(1, 20)]:
    for N in (10, 100, 10000):
        us = [mp.mpf(-40) + mp.mpf(80) * j / 8000 for j in range(8001)]   # log10 r
        prev = None; tot = None; mx = 0
        for u in us:
            v = mp.im(L(mp.mpf(10) ** u, p, N))
            if prev is None:
                tot = v
            else:
                d = v - prev; d -= 2 * mp.pi * mp.nint(d / (2 * mp.pi)); assert abs(d) < 0.5, (p, N, u, d)
                tot += d
            prev = v; mx = max(mx, abs(tot))
        endre = mp.re(L(mp.mpf(10) ** 40, p, N))
        worst = max(worst, abs(tot))
        print(f"p={mp.nstr(p,3)} N={N}: max|Im L| = {mp.nstr(mx,4)}, Im L(end) = {mp.nstr(tot,4)}, Re L(end) = {mp.nstr(endre,3)}")
print(f"max |Im L(end)| over all = {mp.nstr(worst,3)}  (0 = no winding)")
