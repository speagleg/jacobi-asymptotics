"""Checks for CG.md §9 (closing GAP-1: Conjecture CG at p = 1, every s > 1). NUMERICAL (Rule N), mpmath.

[P1] WLXZ (2.1): psi(0) = 1/(3 pi), so f'(0) = pi psi(0) = 1/3; total mass of psi = 1 (transcription sanity check).
[P2] WLXZ (2.6) at alpha_W = 1, z = i r: D(i r) = exp(j(N/r^2)) (Binet remainder), hence D -> 1 as r -> 0.
[P3] Van (4.27), sector II, first column c(zeta) times W^{-1} = (-z)^{-a} along z = i r, zeta = N f(z):
     lim_{r->0} det[(cW^{-1})_r, cW^{-1}] = pi (N f'(0))^{2a+1} 2^{-2a} / (Gamma(a+1/2) Gamma(a+3/2)).
     (Tested with the linear map f(z) = z/3 and with a nonlinear odd map f(z) = z/3 + z^3/7.)
[P4] Assembly of the constants (E(0), v0(0), e^L, kappa, sigma_3 sign, d/dz = -i d/dr):
     sqrt(N) * kappa * tau~(0)^2 * [P3 value]/pi  ==  (N^3/36)^zeta / (Gamma(zeta) Gamma(zeta+1)).
[P5] Fold: lambda_m(0; sigma_{1,s}) = lambda_{2m-1}(0; nu_s) = lambda_{2m}(0; nu_s).
[P6] Theorem C (p = 1): r_m := lambda_m(0; sigma_{1,s}) (N^3/36)^zeta / (Gamma(zeta)Gamma(zeta+1)), N = 2m - 1,
     r_m - 1 = O(1/m), for s in {1.2, 1.5, 2, 2.5, 3.7, 5}; precision doubling dps 400 vs 800.
"""
import sys
import mpmath as mp
from cglib import recurrence, christoffel_at, richardson

out = []
def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True); out.append(s)

mp.mp.dps = 60

# [P1]
def psi(x):
    x = mp.mpf(x); ax = abs(x)
    if ax <= 2:
        return (4 * mp.atan(ax / mp.sqrt(4 - x**2)) / ax**3 - mp.sqrt(4 - x**2) / x**2) / mp.pi
    return 2 / ax**3
pr("[P1] psi(x)*3pi at x = 1e-3, 1e-5:", mp.nstr(psi(mp.mpf('1e-3')) * 3 * mp.pi, 20), mp.nstr(psi(mp.mpf('1e-5')) * 3 * mp.pi, 20))
mass = 2 * (mp.quad(psi, [mp.mpf('1e-30'), 1, 2]) + mp.quad(psi, [2, mp.inf]))
pr("[P1] total mass of psi - 1:", mp.nstr(mass - 1, 5))
fp0 = mp.pi * psi(mp.mpf('1e-12'))
pr("[P1] f'(0) = pi psi(0) =", mp.nstr(fp0, 25), " (1/3 expected)")

# [P2]
def D_wlxz(z, N):
    t = N / z**2                      # n/z^2
    mt = mp.exp(1j * mp.pi) / z**2 * N if mp.im(z) > 0 else mp.exp(-1j * mp.pi) / z**2 * N   # -n/z^2 with the WLXZ branch
    return mp.gamma(1 - t) / (mp.exp(t) * mp.sqrt(2 * mp.pi)) * mp.power(mt, t - mp.mpf(1) / 2)
def jbinet(T):
    return mp.loggamma(T) - ((T - mp.mpf(1) / 2) * mp.log(T) - T + mp.log(2 * mp.pi) / 2)
worst = 0
for N in [10, 101]:
    for r in ['0.9', '0.3', '0.1']:
        r = mp.mpf(r); z = 1j * r
        d = D_wlxz(z, N); e = mp.exp(jbinet(N / r**2))
        worst = max(worst, abs(d / e - 1))
pr("[P2] max |D(ir)/exp(j(N/r^2)) - 1| over N in {10,101}, r in {.9,.3,.1}:", mp.nstr(worst, 5))

# [P3]
def col_over_W(r, a, N, fmap):
    z = 1j * r
    zeta = N * fmap(z)                 # in i R_+ (sector II boundary value: arg zeta = pi/2)
    arg = zeta * mp.exp(-1j * mp.pi / 2)
    pref = mp.sqrt(zeta) * mp.exp(-a * mp.pi * 1j / 2)
    c1 = mp.sqrt(mp.pi) * pref * mp.besseli(a + mp.mpf(1) / 2, arg)
    c2 = -1j * mp.sqrt(mp.pi) * pref * mp.besseli(a - mp.mpf(1) / 2, arg)
    W = mp.power(-z, a)                # (-z)^a, principal: sector II has 0 < |arg f| < pi/2 (KV (5.9))
    return mp.matrix([c1 / W, c2 / W])
def det_lim(a, N, fmap, fp):
    vals = []
    for r in [mp.mpf('1e-6'), mp.mpf('1e-8')]:
        v = col_over_W(r, a, N, fmap)
        dv = mp.matrix([mp.diff(lambda rr: col_over_W(rr, a, N, fmap)[i], r) for i in range(2)])
        vals.append(dv[0] * v[1] - dv[1] * v[0])
    pred = mp.pi * (N * fp) ** (2 * a + 1) * mp.mpf(2) ** (-2 * a) / (mp.gamma(a + mp.mpf(1) / 2) * mp.gamma(a + mp.mpf(3) / 2))
    return vals, pred
worst = 0
for fmap, fp, name in [(lambda z: z / 3, mp.mpf(1) / 3, "linear"), (lambda z: z / 3 + z**3 / 7, mp.mpf(1) / 3, "cubic")]:
    for a in ['-0.3', '0', '0.5', '1', '2.2', '3.5']:
        a = mp.mpf(a)
        for N in [7, 40]:
            vals, pred = det_lim(a, N, fmap, fp)
            worst = max(worst, abs(vals[1] / pred - 1))
    pr("[P3]", name, "map: max |det(r=1e-8)/pred - 1| over a in {-.3,0,.5,1,2.2,3.5}, N in {7,40}:", mp.nstr(worst, 5))

# [P4]
eL = mp.sqrt(2) * 1j * mp.e / mp.sqrt(mp.pi)          # WLXZ (5.9) context: L = log(sqrt2 i Gamma(1)^2 e / sqrt pi)
E0 = mp.sqrt(2 * mp.pi) * mp.mpf(4) ** (-mp.mpf(1) / 2)  # WLXZ (4.19), alpha_W = 1
v00 = eL * 4                                           # v0(0) = e^L (4 - 0) Q_m(0), Q_m(0) = 1
worst = 0
for s in ['1.2', '1.5', '2', '2.5', '3.7', '5']:
    s = mp.mpf(s); a = s - mp.mpf(3) / 2; zt = s - 1
    for N in [9, 99]:
        _, P3 = det_lim(a, N, lambda z: z / 3, mp.mpf(1) / 3)
        # u = M sigma3 Nmat w / (E D v0^{1/2}), w = c W^{-1} (P3); det(M sigma3) = -1, D(0) = 1, d/dz = -i d/dr:
        detu = (-1j) * (-1) * P3 / (E0**2 * v00)
        kappa = 2 * mp.e * mp.mpf(N) ** a / mp.sqrt(2 * mp.pi)
        K = mp.sqrt(N) * kappa * detu
        pred = (mp.mpf(N) ** 3 / 36) ** zt / (mp.gamma(zt) * mp.gamma(zt + 1))
        worst = max(worst, abs(K / pred - 1))
pr("[P4] max |assembled K / (N^3/36)^zeta/(G(zeta)G(zeta+1)) - 1| (6 values of s, N in {9,99}):", mp.nstr(worst, 5))

# [P5], [P6]
def lam_sigma(s, m, dps):
    with mp.workdps(dps):
        al, be = recurrence(1, s, m + 2)
        P0, Px, h = christoffel_at(mp.mpf(0), al, be, m + 1)
        return [1 / mp.fsum(P0[k]**2 / h[k] for k in range(mm)) for mm in range(1, m + 1)]
def lam_nu(s, n, dps):
    with mp.workdps(dps):
        L = 2 * (n + 2) + 2
        mom = [(mp.zeta(mp.mpf(s) + j // 2) if j % 2 == 0 else mp.mpf(0)) for j in range(L)]
        al, be = recurrence(1, s, n + 2, moments=mom)
        P0, Px, h = christoffel_at(mp.mpf(0), al, be, n + 1)
        return 1 / mp.fsum(P0[k]**2 / h[k] for k in range(n))
with mp.workdps(200):
    for s in ['2.3', '1.2']:
        m = 10
        ls = lam_sigma(s, m, 200)[m - 1]
        pr("[P5] s=%s m=%d: lambda_m(sigma)/lambda_{2m-1}(nu) - 1 = %s, lambda_m(sigma)/lambda_{2m}(nu) - 1 = %s" % (
            s, m, mp.nstr(ls / lam_nu(s, 2 * m - 1, 200) - 1, 5), mp.nstr(ls / lam_nu(s, 2 * m, 200) - 1, 5)))

M = int(sys.argv[1]) if len(sys.argv) > 1 else 80
for s in ['1.2', '1.5', '2', '2.5', '3.7', '5']:
    sm = mp.mpf(s); zt = sm - 1
    lA = lam_sigma(s, M, 400); lB = lam_sigma(s, M, 800)
    with mp.workdps(800):
        r = {}
        for mm in range(1, M + 1):
            N = mp.mpf(2 * mm - 1)
            r[mm] = lB[mm - 1] * (N**3 / 36) ** zt / (mp.gamma(zt) * mp.gamma(zt + 1))
        dd = max(abs(lA[mm - 1] / lB[mm - 1] - 1) for mm in range(1, M + 1))
        ms = list(range(M - 12, M + 1))
        rich = richardson(r, ms, 12)
        pr("[P6] s=%s: r_m-1 at m=20,40,%d: %s %s %s | m(r_m-1) at m=%d: %s | Richardson(K=12) limit-1: %s | dps400 vs 800 max rel diff %s" % (
            s, M, mp.nstr(r[20] - 1, 4), mp.nstr(r[40] - 1, 4), mp.nstr(r[M] - 1, 4), M, mp.nstr(M * (r[M] - 1), 6),
            mp.nstr(rich - 1, 4), mp.nstr(dd, 3)))
