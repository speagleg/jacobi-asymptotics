"""(Rule R review probe, committed: the CANONICAL absolute test with the far-field scalar Xi built explicitly; no free constant.)
Plan 13 Phase 2 (NUMERICAL, end to end): RH global parametrix for the smooth-zeta model vs the true OPs.
Tail: atoms j <= 60N exact, the rest by the midpoint Euler-Maclaurin integral (log panels).
Model: atoms x_j = 1/(gamma_j^2 + 1/4), N0(gamma_j) = j - 1/2, masses 2 x_j.  Rescale z = s x with s := 1/x_N, so
U(z) = s^{N sigma3} Y(z/s); then Res_{X_j} U12 = w(X_j) U11(X_j) with w(z) = 2z exactly.
Equilibrium: Lemma E1 (finite-N, Abel inversion), A(u) = (1/N) int_{3/8}^{t(u)} (1 - u/x(r))^{-1/2} dr (x units),
   g(z) = 2 log((sqrt z + sqrt(z - bh))/2) - int_{beta}^{x_e} A(u) s du / (sqrt(z - s u)(sqrt z + sqrt(z - s u))),
   l/2  = log(bh/4) + int_{beta}^{x_e} A(u)/u du,      bh := s beta_N.
Scalars: D = Dt/(1 - e^{-+2 pi i t}) (Dt Stirling-Binet), B = Binet-cut scalar on (-inf,0), K = (bh - z)^{-1/2}.
Global N: Jacobi type on [0,bh] with weight w0 = |W| (bh - x)/(Dt B)^2 e^{-i pi/2}, |W| = 4 pi |dt/dz| x.
TEST (far-end scalars omitted; they are constant near the band up to O((band/dist)), dist ~ s x_e ~ N^2/log^2 N):
   M(z) := e^{-N l s3/2} U(z) e^{N phi s3} F^{s3} N(z)^{-1}  should be a CONSTANT diagonal matrix + O(1/N).
Reports, relative to a reference point z0: |M11(z)/M11(z0) - 1|, |M22/M22(z0) - 1|, |Dinf^-2 M12/M11|, |Dinf^2 M21/M22|."""
import sys
import mpmath as mp

Ns = [int(a) for a in sys.argv[1].split(",")] if len(sys.argv) > 1 else [20, 40]
PTS = [mp.mpc(1.2, 1.0), mp.mpc(0.5, 0.8), mp.mpc(-1.0, 0.5), mp.mpc(-1.5, 0.5), mp.mpc(0, 2.5),
       mp.mpc(3.0, -1.2), mp.mpc(4.5, 1.5)]
Z0 = PTS[0]
SEVEN8 = mp.mpf(7) / 8


import os
MODEL = os.environ.get("MODEL", "zeta")   # "zeta" (smooth-zeta) or "pp2" (pure power p = 2, masses 2 x_j; validation)


def N0(g):
    return g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + SEVEN8


def xt(tv):
    if MODEL == "pp2":
        return mp.power(tv, -2)
    y = (tv - mp.mpf(1) / 2 - SEVEN8) / mp.e
    g = 2 * mp.pi * mp.e * mp.exp(mp.re(mp.lambertw(y)))
    return 1 / (g * g + mp.mpf(1) / 4)


def gamma_of_t(tv):
    y = (tv - mp.mpf(1) / 2 - SEVEN8) / mp.e
    return 2 * mp.pi * mp.e * mp.exp(mp.re(mp.lambertw(y)))


def tail_nodes(K2, tend=mp.mpf(10) ** 30, ratio=mp.mpf("1.3"), k=6):
    """Midpoint Euler-Maclaurin tail sum_{j>K2} 2 x_j delta_{x_j} ~ int_{K2+1/2}^inf 2 x(t) delta_{x(t)} dt, discretized by
    k-point Gauss-Legendre on log-spaced panels in t (relative error O(1/K2^2) of a mass that sits at x <= x_{K2})."""
    import numpy as np
    tt, ww = np.polynomial.legendre.leggauss(k)
    u0, u1 = mp.log(mp.mpf(K2) + mp.mpf(1) / 2), mp.log(tend)
    nodes, wts = [], []
    a = u0
    while a < u1:
        b = min(a + mp.log(ratio), u1)
        for ti, wi in zip(tt, ww):
            u = (a + b) / 2 + (b - a) / 2 * mp.mpf(ti)
            tv = mp.exp(u)
            xv = xt(tv)
            nodes.append(xv); wts.append(2 * xv * tv * (b - a) / 2 * mp.mpf(wi))
        a = b
    return nodes, wts


def run(N):
    dps_hi = int(60 + 4.6 * N * mp.log10(N) + 40)
    K = int(os.environ.get("KFAC", "60")) * N
    mp.mp.dps = dps_hi
    xs = [xt(mp.mpf(j)) for j in range(1, K + 1)]
    tn, tw = tail_nodes(K)
    xs = xs + tn
    ms = [2 * x for x in xs[:K]] + tw
    A, B2, h = [], [], [mp.fsum(ms)]
    P = [mp.mpf(1)] * len(xs); prev = [mp.mpf(0)] * len(xs)
    for n in range(N):
        an = mp.fsum(m * x * q * q for m, x, q in zip(ms, xs, P)) / h[-1]
        nxt = [(x - an) * q - (B2[-1] if B2 else 0) * r for x, q, r in zip(xs, P, prev)]
        hn = mp.fsum(m * q * q for m, q in zip(ms, nxt))
        A.append(an); B2.append(hn / h[-1]); h.append(hn); prev, P = P, nxt
    PN, PN1 = P, prev

    def poly(x, n):
        a0, b0 = mp.mpf(1), x - A[0]
        if n == 0: return a0
        for m in range(1, n):
            a0, b0 = b0, (x - A[m]) * b0 - B2[m - 1] * a0
        return b0
    xN = xt(mp.mpf(N)); s = 1 / xN

    def U(z):
        x = z / s
        y11 = poly(x, N); y21 = poly(x, N - 1) / h[N - 1]
        y12 = mp.fsum(m * q / (x - xx) for m, q, xx in zip(ms, PN, xs))
        y22 = mp.fsum(m * q / (x - xx) for m, q, xx in zip(ms, PN1, xs)) / h[N - 1]
        f = s ** N
        return mp.matrix([[f * y11, f * y12], [y21 / f, y22 / f]])
    Us = {z: U(z) for z in PTS}
    bN_true = mp.sqrt(B2[N - 1]); aN_true = A[N - 1]
    mp.mp.dps = 25
    Us = {z: mp.matrix([[mp.mpc(Us[z][i, j]) for j in range(2)] for i in range(2)]) for z in PTS}
    s = mp.mpf(s); NN = mp.mpf(N)
    xe = 1 / (4 * mp.pi ** 2 + mp.mpf(1) / 4) if MODEL == "zeta" else None
    TMIN = (mp.mpf(os.environ["TMIN"]) if "TMIN" in os.environ else mp.mpf(3) / 8) if MODEL == "zeta" else mp.mpf(0)
    if MODEL == "zeta" and TMIN > mp.mpf(3)/8: xe = xt(TMIN)
    import numpy as np

    def gl(br, n):  # composite Gauss-Legendre on breakpoints br
        tt, ww = np.polynomial.legendre.leggauss(n)
        X, W = [], []
        for a, b in zip(br[:-1], br[1:]):
            for ti, wi in zip(tt, ww):
                X.append((a + b) / 2 + (b - a) / 2 * mp.mpf(ti)); W.append((b - a) / 2 * mp.mpf(wi))
        return X, W

    def tx(x):
        if MODEL == "pp2": return mp.power(x, -0.5)
        return N0(mp.sqrt(1 / x - mp.mpf(1) / 4)) + mp.mpf(1) / 2

    def Afun(u):  # Lemma E1, x units
        T = tx(u); vmax = mp.sqrt(1 - TMIN / T)
        f = lambda v: 2 * v * T / mp.sqrt(abs(1 - u / xt(T * (1 - v * v))))
        if os.environ.get("AFIX") == "1":
            return mp.quad(f, [0] + [mp.mpf(p) * vmax for p in ("0.1", "0.5", "0.9")] + [vmax]) / NN
        return mp.quad(f, [0, mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), vmax]) / NN

    def Eedge(Tb):
        xT = xt(Tb); vmax = mp.sqrt(1 - TMIN / Tb)
        f = lambda v: 2 * v * Tb / mp.sqrt(abs(1 - xT / xt(Tb * (1 - v * v))))
        return mp.quad(f, [0, mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), vmax]) / NN
    Tb = mp.findroot(lambda T: Eedge(T) - 1, (NN / (mp.pi / 2) * mp.mpf("0.8"), NN / (mp.pi / 2) * mp.mpf("1.2")),
                     solver="anderson")
    beta = xt(Tb); bh = s * beta
    if MODEL == "zeta":
        d = xe - beta
        ubr = [beta] + [beta + d * mp.mpf(r) for r in ("1e-4", "1e-3", "1e-2", "0.03", "0.1", "0.2", "0.35", "0.5",
                                                       "0.65", "0.8", "0.9", "0.97", "0.995", "1")]
        if os.environ.get("UFINE") == "1":
            extra = [beta * mp.mpf(v) for v in ("1.0001", "1.001", "1.01", "1.05", "1.1", "1.2", "1.5", "2", "3", "5", "8", "12", "20", "35", "60", "100")]
            ubr = sorted(set([u for u in ubr + extra if u <= xe]))
        print(f"   u-panels: {len(ubr)-1}", flush=True)
    else:  # log-spaced panels (ratio 2) out to 2^60 beta; A(u) ~ u^{-1/2}
        ubr = [beta * mp.mpf(v) for v in ("1", "1.001", "1.01", "1.05", "1.2", "1.5")] + [beta * 2 ** k for k in range(1, 61)]
    uX, uW = gl(ubr, int(os.environ.get("UGL", "12")))
    uA = [Afun(u) for u in uX]
    lhalf = mp.log(bh / 4) + mp.fsum(a * w / u for a, w, u in zip(uA, uW, uX))
    print(f"   l/2 = {mp.nstr(lhalf, 15)},  int A dmu-check: sum A w = {mp.nstr(mp.fsum(a*w for a,w in zip(uA,uW)), 12)}", flush=True)

    def g(z):
        corr = mp.fsum(a * w * s / (mp.sqrt(z - s * u) * (mp.sqrt(z) + mp.sqrt(z - s * u))) for a, w, u in zip(uA, uW, uX))
        return 2 * mp.log((mp.sqrt(z) + mp.sqrt(z - bh)) / 2) - corr

    def tz(z):
        if MODEL == "pp2": return mp.power(z / s, -0.5)
        return N0(mp.sqrt(s / z - mp.mpf(1) / 4)) + mp.mpf(1) / 2

    def dtdz(z):  # analytic: t'(x) = N0'(gamma) gamma'(x), x = z/s
        x = z / s
        if MODEL == "pp2": return -mp.power(x, -1.5) / 2 / s
        gm = mp.sqrt(1 / x - mp.mpf(1) / 4)
        return mp.log(gm / (2 * mp.pi)) / (2 * mp.pi) * (-1 / (2 * x * x * gm)) / s
    Dt = lambda z: mp.sqrt(2 * mp.pi) * mp.exp((tz(z) - 0.5) * mp.log(tz(z)) - tz(z) - mp.loggamma(tz(z)))

    def D(z):
        sg = 1 if mp.im(z) > 0 else -1
        return Dt(z) / (1 - mp.exp(-sg * 2j * mp.pi * tz(z)))
    lX, lWt = gl([mp.mpf(v)/2 for v in range(-120, 121)], int(os.environ.get("BGL","8")))
    # D_+ along (-inf,0) by ANALYTIC CONTINUATION from 0-: log t tracked continuously (principal log jumps where
    # t(x) crosses the negative real t-axis, |gamma| ~ 2 pi e), and 1/Gamma(t) = rgamma (entire, no branch).
    Lt_prev = None; lnD = []
    for u in lX:
        z = -mp.exp(u) + 1j * mp.mpf("1e-22") * mp.exp(u)
        tv = tz(z); L0 = mp.log(tv)
        if Lt_prev is not None:
            L0 += 2j * mp.pi * mp.nint(mp.im(Lt_prev - L0) / (2 * mp.pi))
        Lt_prev = L0
        lnDt = mp.log(mp.sqrt(2 * mp.pi)) + (tv - 0.5) * L0 - tv - mp.loggamma(tv) if abs(tv) > 50 else \
            mp.log(mp.sqrt(2 * mp.pi)) + (tv - 0.5) * L0 - tv + mp.log(mp.rgamma(tv))
        wv = -2j * mp.pi * tv   # stable log(1 - e^w): for Re w > 0 use w + log(e^{-w} - 1)
        if mp.re(wv) > 60:
            l1 = wv + mp.log(-1 + mp.exp(-wv)) if mp.re(wv) < 1e6 else wv + mp.log(-1)
        elif mp.re(wv) < -60:
            l1 = mp.mpc(0)          # |e^w| < e^{-60}
        else:
            l1 = mp.log(1 - mp.exp(wv))
        lnD.append(lnDt - l1)
    raw = [mp.im(v) for v in lnD]
    unw = [raw[0]]
    for r in raw[1:]:
        k = mp.nint((unw[-1] - r) / (2 * mp.pi))
        unw.append(r + 2 * mp.pi * k)
    lE = [2 * a for a in unw]
    if N == Ns[0]:
        for u0 in (-50, -20, -10, -5, 0, 2, 4, 6, 8, 10, 15, 20, 40, 60):
            k0 = min(range(len(lX)), key=lambda k: abs(lX[k] - u0))
            print(f"      u={u0:4d} (y=-e^u, x_unresc={mp.nstr(-mp.exp(lX[k0])/s,3)}): arg D+ = {mp.nstr(unw[k0],6)}", flush=True)

    def Bf(z):
        acc = mp.fsum(e * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u) * w for e, u, w in zip(lE, lX, lWt))
        return mp.exp(-acc / (2 * mp.pi))
    # WLXZ alpha-shift: nodes at t - TMIN = (j-1) + alpha_W, alpha_W = 1 - TMIN; their E ~ (4 - z^2)^{1/2 - alpha}
    # gives K = (bh - z)^{kap}, kap = 1/2 - alpha_W = TMIN - 1/2  (pure power: -1/2; smooth zeta: -1/8)
    kap = mp.mpf(os.environ["KAP"]) if "KAP" in os.environ else TMIN - mp.mpf(1) / 2
    Kf = lambda z: mp.power(bh - z, kap)
    Fin = lambda z: D(z) * Bf(z) * Kf(z)
    USEXI = os.environ.get("XI", "0") == "1" and MODEL == "zeta"
    if USEXI:
        Xe = s * xe; X1 = s * xt(mp.mpf(1))
        xcross = -s / (4 * mp.pi ** 2 * mp.e ** 2 - mp.mpf(1) / 4)
        rr = -xcross / 2; xm = (X1 + Xe) / 2; c0 = (xm - rr) / 2; RR = (xm + rr) / 2
        def lnFout(z):
            f = lambda y: (tz(y) - TMIN) / (y - z)
            return mp.quad(f, [bh, bh * 2, bh * 4, bh * 8, bh * 16, bh * 32, bh*64, xm*mp.mpf("0.5"), xm*mp.mpf("0.9"), xm*mp.mpf("0.99"), xm, xm*mp.mpf("1.01"), xm + (Xe - xm) * mp.mpf("0.5"), Xe] if os.environ.get("FINE")=="1" else [bh, bh * 2, bh * 8, xm, xm + (Xe - xm) * mp.mpf("0.5"), Xe])
        MC = int(os.environ.get("MC", "400")); Ls = []; zC = []; dzC = []; prevv = None
        for k in range(MC):
            ang = 2 * mp.pi * (mp.mpf(k) + mp.mpf("0.5")) / MC
            zz = c0 + RR * mp.expj(ang)
            v = lnFout(zz) - mp.log(Fin(zz))
            if prevv is not None:
                v = v - 2j * mp.pi * mp.nint(mp.im(v - prevv) / (2 * mp.pi))
            prevv = v; Ls.append(v); zC.append(zz); dzC.append(1j * RR * mp.expj(ang) * 2 * mp.pi / MC)
        print(f"   [Xi] C: -r={mp.nstr(-rr,5)} x_m={mp.nstr(xm,5)}; closure jump of L = {mp.nstr(Ls[-1]-Ls[0],4)}; sup|L|={mp.nstr(max(abs(v) for v in Ls),4)}", flush=True)
        lnXi = lambda z: mp.fsum(v * d / (zz - z) for v, d, zz in zip(Ls, dzC, zC)) / (2j * mp.pi)
    else:
        lnXi = lambda z: mp.mpc(0)
    F = lambda z: Fin(z) * mp.exp(lnXi(z))
    pi_ = mp.pi
    tbr = [mp.mpf(0), mp.mpf("1e-8"), mp.mpf("1e-5"), mp.mpf("1e-3"), mp.mpf("0.03"), mp.mpf("0.3"), mp.mpf(1), mp.mpf(2),
           pi_ - mp.mpf("0.3"), pi_ - mp.mpf("0.03"), pi_ - mp.mpf("1e-3"), pi_ - mp.mpf("1e-5"), pi_ - mp.mpf("1e-8"), pi_]
    thX, thW = gl(tbr, 12)

    def lw(th):
        x = bh * mp.sin(th / 2) ** 2
        Wabs = 4 * mp.pi * abs(dtdz(x)) * x
        return mp.log(Wabs) - 2 * kap * mp.log(bh - x) - 2 * mp.log(Dt(x) * Bf(x)) - 2 * lnXi(x) - 1j * mp.pi / 2
    thL = [lw(th) for th in thX]
    Dinf = mp.exp(mp.fsum(v * w for v, w in zip(thL, thW)) / (2 * mp.pi))

    def Dw(z):
        r = z * mp.sqrt(1 - bh / z)
        acc = mp.fsum(v * w / (z - bh * mp.sin(th / 2) ** 2) for v, w, th in zip(thL, thW, thX))
        return mp.exp(r / (2 * mp.pi) * acc)

    def Nglob(z):
        a = mp.power(1 - bh / z, 0.25)
        N0m = mp.matrix([[(a + 1 / a) / 2, (a - 1 / a) / (2j)], [-(a - 1 / a) / (2j), (a + 1 / a) / 2]])
        dd = Dw(z)
        return mp.diag([Dinf, 1 / Dinf]) * N0m * mp.diag([1 / dd, dd])
    print(f"   [N={N}] ell-hat range: {mp.nstr(min(mp.re(e) for e in lE),4)} .. {mp.nstr(max(mp.re(e) for e in lE),4)}"
          f"; bh={mp.nstr(bh,8)}, l/2={mp.nstr(lhalf,8)}", flush=True)
    Ms = {}
    for z in PTS:
        ph = lhalf - g(z); Fz = F(z)
        V = mp.diag([mp.exp(-NN * lhalf), mp.exp(NN * lhalf)]) * Us[z] * mp.diag([mp.exp(NN * ph) * Fz, mp.exp(-NN * ph) / Fz])
        Ms[z] = V * mp.inverse(Nglob(z))
    out = []
    m0 = Ms[Z0]
    for z in PTS:
        Mz = Ms[z]
        e11 = abs(Mz[0, 0] / m0[0, 0] - 1); e22 = abs(Mz[1, 1] / m0[1, 1] - 1)
        o12 = abs(Mz[0, 1] / Mz[0, 0] / Dinf ** 2); o21 = abs(Mz[1, 0] / Mz[1, 1] * Dinf ** 2)
        Ab = mp.diag([1 / Dinf, Dinf]) * (Mz - mp.eye(2)) * mp.diag([Dinf, 1 / Dinf])
        absmax = max(abs(Ab[i, j]) for i in range(2) for j in range(2))
        print("        Dinf-frame M - I =", [mp.nstr(Ab[i, j], 4) for i in range(2) for j in range(2)], flush=True)
        out.append((z, e11, e22, o12, o21, absmax))
    return out, bN_true, aN_true, beta, s


for N in Ns:
    out, bN, aN, beta, s = run(N)
    print(f"N={N}: s=1/x_N={mp.nstr(s,8)}  b_N/(beta_N/4)-1={mp.nstr(bN/(beta/4)-1,6)}  a_N/(2 b_N)-1={mp.nstr(aN/(2*bN)-1,6)}"
          f"  (x_e s = {mp.nstr(s/(4*mp.pi**2+0.25),5)})")
    for z, e11, e22, o12, o21, absmax in out:
        mx = max(e11, e22, o12, o21)
        print(f"      ABS |Dinf^-s3 (M - I) Dinf^s3|max = {mp.nstr(absmax,4)}   N*abs = {mp.nstr(N*absmax,4)}")
        print(f"   z={mp.nstr(z,4):>22}: |M11/M11(z0)-1|={mp.nstr(e11,3):>9} |M22/M22(z0)-1|={mp.nstr(e22,3):>9}"
              f" |off12|={mp.nstr(o12,3):>9} |off21|={mp.nstr(o21,3):>9}   N*max={mp.nstr(N*mx,4)}")
    sys.stdout.flush()
