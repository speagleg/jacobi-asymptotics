"""Plan 13, Lemma Z (far field), NUMERICAL check of its hypothesis: log(F_out/F_in) is continuous and single-valued on
a closed curve C crossing R at -r and x_m (rescaled z = s x, s = 1/x_N).
  F_in  = D B K,  D = Dt/(1 - e^{-+2 pi i t}) (Dt continued Stirling-Binet), B = Binet-cut scalar on (-inf,0) (continued
          ell-hat), K = (bh - z)^{-1/8};
  F_out = exp( int_{bh}^{X_e} that(y) dy/(y - z) ) (used only outside C),  that = t - 3/8  (exact scalar with T's far jump; regular at X_e).
Reports: |arg t| max on C (Stirling sector), the jumps of arg(F_out/F_in) across the two crossing points (should be
~0 mod 2 pi -> continuity), and the total winding of F_out/F_in around C (should be 0)."""
import sys
import numpy as np
import mpmath as mp

mp.mp.dps = 25
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
SEVEN8 = mp.mpf(7) / 8
N0 = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + SEVEN8
def xt(tv):
    y = (tv - mp.mpf(1) / 2 - SEVEN8) / mp.e
    g = 2 * mp.pi * mp.e * mp.exp(mp.re(mp.lambertw(y)))
    return 1 / (g * g + mp.mpf(1) / 4)
s = 1 / xt(mp.mpf(N)); xe = 1 / (4 * mp.pi ** 2 + mp.mpf(1) / 4); Xe = s * xe; X1 = s * xt(mp.mpf(1))
# beta_N (canonical edge equation)
def Eedge(Tb):
    xT = xt(Tb); vmax = mp.sqrt(1 - mp.mpf(3) / 8 / Tb)
    f = lambda v: 2 * v * Tb / mp.sqrt(abs(1 - xT / xt(Tb * (1 - v * v))))
    return mp.quad(f, [0, mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), vmax]) / N
Tb = mp.findroot(lambda T: Eedge(T) - 1, (N / (mp.pi / 2) * mp.mpf("0.8"), N / (mp.pi / 2) * mp.mpf("1.2")), solver="anderson")
bh = s * xt(Tb)
tz = lambda z: N0(mp.sqrt(s / z - mp.mpf(1) / 4)) + mp.mpf(1) / 2
xcross = -s / (4 * mp.pi ** 2 * mp.e ** 2 - mp.mpf(1) / 4)
print(f"N={N}: s={mp.nstr(s,8)} bh={mp.nstr(bh,6)} X1={mp.nstr(X1,5)} Xe={mp.nstr(Xe,5)}  t-axis crossing at z={mp.nstr(xcross,5)}")
def lnDt(tv, Lt):
    return mp.log(mp.sqrt(2 * mp.pi)) + (tv - 0.5) * Lt - tv - mp.loggamma(tv) if abs(tv) > 50 else \
        mp.log(mp.sqrt(2 * mp.pi)) + (tv - 0.5) * Lt - tv + mp.log(mp.rgamma(tv))
def l1m(tv, sg):  # log(1 - e^{-sg 2 pi i t}) stable
    wv = -sg * 2j * mp.pi * tv
    if mp.re(wv) > 60: return wv + mp.log(-1 + mp.exp(-wv))
    if mp.re(wv) < -60: return mp.mpc(0)
    return mp.log(1 - mp.exp(wv))
# continued ell-hat on (-inf,0)
tt, ww = np.polynomial.legendre.leggauss(8)
lX, lW = [], []
for a in range(-40, 61):
    for ti, wi in zip(tt, ww):
        lX.append(a + 0.5 + 0.5 * mp.mpf(ti)); lW.append(0.5 * mp.mpf(wi))
Lprev = None; arg_prev = None; lE = []
for u in lX:
    z = -mp.exp(u) + 1j * mp.mpf("1e-20") * mp.exp(u)
    tv = tz(z); L0 = mp.log(tv)
    if Lprev is not None: L0 += 2j * mp.pi * mp.nint(mp.im(Lprev - L0) / (2 * mp.pi))
    Lprev = L0
    a = mp.im(lnDt(tv, L0) - l1m(tv, 1))
    if arg_prev is not None: a += 2 * mp.pi * mp.nint((arg_prev - a) / (2 * mp.pi))
    arg_prev = a; lE.append(2 * a)
lnB = lambda z: -mp.fsum(e * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u) * w for e, u, w in zip(lE, lX, lW)) / (2 * mp.pi)
r = mp.re(xcross) / 2 * -1           # cross the negative axis at -r, inside the t-axis crossing
xm = (X1 + Xe) / 2
c0 = (xm - r) / 2; R = (xm + r) / 2
def lnFout(z):
    f = lambda y: (tz(y) - mp.mpf(3) / 8) / (y - z)
    # cut on (bh, X_e): only its part outside C, (x_m, X_e), is ever used; regular at x_m (both sides jump alike)
    return mp.quad(f, [bh, bh * 2, bh * 8, xm, xm + (Xe - xm) * mp.mpf("0.5"), Xe])
def lnFin(z, Lt):
    tv = tz(z); sg = 1 if mp.im(z) > 0 else -1
    return lnDt(tv, Lt) - l1m(tv, sg) + lnB(z) - mp.mpf(1) / 8 * mp.log(bh - z)
# walk around C (counterclockwise from just above x_m), tracking log t and the ratio's arg continuously
M = 400
Lt = None; prev = None; jumps = []; total = mp.mpf(0); argmax = 0; vals = []
for k in range(M + 1):
    ang = 2 * mp.pi * (mp.mpf(k) + mp.mpf("1e-6")) / (M + mp.mpf("2e-6"))
    z = c0 + R * mp.expj(ang)
    tv = tz(z); L0 = mp.log(tv)          # principal sheet in each half-plane (B makes D B continuous across (-inf,0))
    argmax = max(argmax, abs(mp.im(L0)))
    v = mp.im(lnFout(z) - lnFin(z, L0))
    vals.append((ang, v))
    if prev is not None:
        d = v - prev; d -= 2 * mp.pi * mp.nint(d / (2 * mp.pi)); total += d
    prev = v
print(f"   C: center {mp.nstr(c0,5)}, radius {mp.nstr(R,5)} (crosses R at -r = {mp.nstr(-r,4)} and x_m = {mp.nstr(xm,5)})")
print(f"   max |arg t| on C (principal, per half-plane) = {mp.nstr(argmax,5)}  (< pi needed for Stirling D-tilde)")
print(f"   total winding of F_out/F_in around C = {mp.nstr(total/(2*mp.pi),6)} (turns)")
print(f"   arg ratio just above x_m = {mp.nstr(vals[0][1],8)}, just below (after full turn) = {mp.nstr(vals[-1][1],8)}")
ib = min(range(len(vals)), key=lambda k: abs(vals[k][0] - mp.pi))
print(f"   near -r: arg ratio at angle pi-: {mp.nstr(vals[ib-1][1],8)}, pi+: {mp.nstr(vals[ib+1][1],8)}")
# refined continuity test at -r: points at distance 1e-6 from the axis, B by adaptive quadrature with a breakpoint at
# the singular location u0 = log r
def ellf(u):
    k = min(range(len(lX)), key=lambda kk: abs(lX[kk] - u))
    return lE[k]
from bisect import bisect_left
def ell_interp(u):
    k = bisect_left(lX, u)
    if k <= 0: return lE[0]
    if k >= len(lX): return lE[-1]
    a0, a1 = lX[k - 1], lX[k]; return lE[k - 1] + (lE[k] - lE[k - 1]) * (u - a0) / (a1 - a0)
def lnB_fine(z):
    u0 = mp.log(-mp.re(z)); h = abs(mp.im(z)) / (-mp.re(z))
    f = lambda u: ell_interp(u) * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u)
    pts = [-40, -10, u0 - 1, u0 - 100 * h, u0 - h, u0, u0 + h, u0 + 100 * h, u0 + 1, 10, 60]
    return -mp.quad(f, sorted(pts)) / (2 * mp.pi)
def lnFin_fine(z):
    tv = tz(z); sg = 1 if mp.im(z) > 0 else -1
    return lnDt(tv, mp.log(tv)) - l1m(tv, sg) + lnB_fine(z) - mp.mpf(1) / 8 * mp.log(bh - z)
for eps in ("1e-3", "1e-6"):
    up = -r + 1j * mp.mpf(eps); dn = -r - 1j * mp.mpf(eps)
    vu = mp.im(lnFout(up) - lnFin_fine(up)); vd = mp.im(lnFout(dn) - lnFin_fine(dn))
    d = vu - vd; d -= 2 * mp.pi * mp.nint(d / (2 * mp.pi))
    print(f"   at -r +- i{eps}: arg ratio {mp.nstr(vu,8)} / {mp.nstr(vd,8)}; jump mod 2pi = {mp.nstr(d,4)}")
