"""Rule R end-to-end probe for RH_px (p > 1), region Omega_infty.
True U from the discrete OPs of sigma_{p,s} (atoms k <= K exact; tail k > K replaced by an M-point Gauss rule built
from the exact tail moments zeta(s + p j, K+1), exact for the OPs up to degree M-1 and spectrally accurate for the
Cauchy transforms at |z| >> (N/K)^p).  Then
   V := Finf^{-s3} e^{-N l s3/2} U e^{N phi s3} F^{s3},  F = D S E,
compared with the global parametrix N = Dinf^{s3} N0 Dw^{-s3} (Jacobi-type on [0,4c], weight w0 = W (4c-x)/(Dt S)^2).
Reports max |Dinf^{-s3}(V N^{-1} - I) Dinf^{s3}| at test points; expected O(1/N) if Phases 1-3 are right."""
import sys
import mpmath as mp

p = mp.mpf(sys.argv[1]); s = mp.mpf(sys.argv[2]); Ns = [int(a) for a in sys.argv[3].split(",")]
I_ = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1)
c = (mp.pi / (2 * I_)) ** p / 4
c4 = 4 * c
l = 2 * (mp.log(c) + p)
PTS = [mp.mpc(1.2, 1.0), mp.mpc(0.5, 0.8), mp.mpc(-1.0, 0.5), mp.mpc(-1.5, 1e-40), mp.mpc(0, 2.5),
       mp.mpc(4.5, 1.5), mp.mpc(3.0, -1.2), mp.mpc(15, 8), mp.mpc(-6, -3)]


def gauss_tail(K, M, dps):
    """M-point Gauss rule for nu = sum_{k>K} k^{-s} delta_{k^{-p}} via the Chebyshev algorithm on scaled moments."""
    with mp.workdps(dps):
        sc = mp.mpf(K) ** p
        mom = [sc ** j * mp.zeta(s + p * j, K + 1) for j in range(2 * M)]
        # Chebyshev algorithm (Gautschi): sigma_{k,l}
        a = [mp.mpf(0)] * M; b = [mp.mpf(0)] * M
        sig_prev = [mp.mpf(0)] * (2 * M)
        sig = mom[:]
        a[0] = mom[1] / mom[0]; b[0] = mom[0]
        for k in range(1, M):
            new = [mp.mpf(0)] * (2 * M)
            for L in range(k, 2 * M - k):
                new[L] = sig[L + 1] - a[k - 1] * sig[L] - b[k - 1] * sig_prev[L]
            a[k] = new[k + 1] / new[k] - sig[k] / sig[k - 1]
            b[k] = new[k] / sig[k - 1]
            sig_prev, sig = sig, new
        J = mp.matrix(M, M)
        for i in range(M):
            J[i, i] = a[i]
            if i + 1 < M:
                J[i, i + 1] = J[i + 1, i] = mp.sqrt(b[i + 1])
        E, Q = mp.eigsy(J)
        nodes = [E[i] / sc for i in range(M)]
        wts = [mom[0] * Q[0, i] ** 2 for i in range(M)]
        return nodes, wts


def run(N):
    dps_hi = int(40 + 2.2 * float(p) * N * mp.log10(N) + 30)
    K = 4 * N; M = N + 12
    tn, tw = gauss_tail(K, M, dps_hi + 60)
    mp.mp.dps = dps_hi
    xs = [mp.mpf(k) ** (-p) for k in range(1, K + 1)] + tn
    ms = [mp.mpf(k) ** (-s) for k in range(1, K + 1)] + tw
    A, B2, h = [], [], [mp.fsum(ms)]
    P = [mp.mpf(1)] * len(xs); prev = [mp.mpf(0)] * len(xs); Pm1 = None
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
    scN = mp.mpf(N) ** p

    def U(z):
        x = z / scN
        y11 = poly(x, N); y21 = poly(x, N - 1) / h[N - 1]
        y12 = mp.fsum(m * q / (x - xx) for m, q, xx in zip(ms, PN, xs))
        y22 = mp.fsum(m * q / (x - xx) for m, q, xx in zip(ms, PN1, xs)) / h[N - 1]
        f = scN ** N
        return mp.matrix([[f * y11, f * y12], [y21 / f, y22 / f]])
    # ---- scalar functions at modest precision
    Us = {z: U(z) for z in PTS}
    mp.mp.dps = 30
    Us = {z: mp.matrix([[mp.mpc(Us[z][i, j]) for j in range(2)] for i in range(2)]) for z in PTS}

    def g(z):
        f = lambda tau: 2 * mp.log((mp.sqrt(z) + mp.sqrt(z - c4 * tau ** (-p))) / 2)
        return mp.quad(f, [0, mp.mpf("1e-8"), mp.mpf("1e-4"), mp.mpf("0.01"), 0.5, 1])
    t = lambda z: N * mp.power(z, -1 / p)
    Dt = lambda z: mp.sqrt(2 * mp.pi) * mp.exp((t(z) - 0.5) * mp.log(t(z)) - t(z) - mp.loggamma(t(z)))

    def D(z):
        sg = 1 if mp.im(z) > 0 else -1
        return Dt(z) / (1 - mp.exp(-sg * 2j * mp.pi * t(z)))
    ellc = {}

    def ell(u):  # ell-hat at y = -e^u
        if u not in ellc:
            ellc[u] = 2 * mp.arg(D(-mp.exp(u) + 1j * mp.mpf("1e-28") * mp.exp(u)))
        return ellc[u]
    BR = [-80, -40, -20, -8, -3, 0, 3, 8, 20, 40, 80, 120]

    def S(z):
        f = lambda u: ell(u) * (1 / (-mp.exp(u) - z) - 1 / (-mp.exp(u) - 1)) * mp.exp(u)
        pts = list(BR)
        if mp.re(z) < 0 and abs(mp.im(z)) < 1e-3:
            u0 = mp.log(-mp.re(z)); pts = sorted(set(pts + [u0 - 0.5, u0, u0 + 0.5]))
        return mp.exp(-mp.quad(f, pts) / (2 * mp.pi))
    E = lambda z: mp.power(c4 - z, -0.5)
    F = lambda z: D(z) * S(z) * E(z)
    # F_inf = lim F e^{-N(g - log z)}  (analytic at infinity)
    finf = [F(z) * mp.exp(-N * (g(z) - mp.log(z))) for z in (mp.mpf(10) ** 9 * mp.expjpi(0.37), mp.mpf(10) ** 9 * mp.expjpi(-0.81))]
    Finf = finf[0]
    # Szego function of w0 on [0,4c]
    Wabs = 2 * mp.pi / p * mp.power(N, 1 + p - s)
    al = (s - 1 - p) / p
    def logw0th(th):
        x = c4 * mp.sin(th / 2) ** 2
        return (mp.log(Wabs) + al * (mp.log(c4) + 2 * mp.log(mp.sin(th / 2))) + mp.log(c4) + 2 * mp.log(mp.cos(th / 2))
                - 2 * mp.log(Dt(x) * S(x)) - 1j * mp.pi / 2)
    lwc = {}

    def lw(th):
        if th not in lwc:
            lwc[th] = logw0th(th)
        return lwc[th]
    Dinf = mp.exp(mp.quad(lw, [0, mp.pi / 2, mp.pi]) / (2 * mp.pi))

    def Dw(z):
        r = z * mp.sqrt(1 - c4 / z)
        return mp.exp(r / (2 * mp.pi) * mp.quad(lambda th: lw(th) / (z - c4 * mp.sin(th / 2) ** 2), [0, mp.pi / 2, mp.pi]))

    def Nglob(z):
        a = mp.power(1 - c4 / z, 0.25)
        N0 = mp.matrix([[(a + 1 / a) / 2, (a - 1 / a) / (2j)], [-(a - 1 / a) / (2j), (a + 1 / a) / 2]])
        d = Dw(z)
        return mp.diag([Dinf, 1 / Dinf]) * N0 * mp.diag([1 / d, d])
    out = []
    for z in PTS:
        Fz = F(z); ph = l / 2 - g(z)
        V = mp.diag([1 / Finf, Finf]) * mp.diag([mp.exp(-N * l / 2), mp.exp(N * l / 2)]) * Us[z] * \
            mp.diag([mp.exp(N * ph) * Fz, mp.exp(-N * ph) / Fz])
        Nz = Nglob(z)
        R = V * mp.inverse(Nz)
        Rh = mp.diag([1 / Dinf, Dinf]) * (R - mp.eye(2)) * mp.diag([Dinf, 1 / Dinf])
        out.append((z, max(abs(Rh[i, j]) for i in range(2) for j in range(2)), mp.det(V)))
    return out, A, B2, finf, Dinf


for N in Ns:
    out, A, B2, finf, Dinf = run(N)
    print(f"p={p} s={s} N={N}: alpha_x={mp.nstr((s-1-p)/p,4)}  Finf(2 dirs)={[mp.nstr(f,8) for f in finf]}  Dinf={mp.nstr(Dinf,6)}")
    print(f"   N^p b_N/c = {mp.nstr(mp.sqrt(B2[N-1]) * mp.mpf(N)**p / c, 10)}   N^p a_(N-1)/(2c) = {mp.nstr(A[N-1]*mp.mpf(N)**p/(2*c),10)}")
    for z, e, dV in out:
        print(f"   z={mp.nstr(z,4):>22}: max|Dinf^-s3 (V N^-1 - I) Dinf^s3| = {mp.nstr(e,5):>10}   N*err = {mp.nstr(N*e,5):>8}  |detV-1|={mp.nstr(abs(dV-1),2)}")
    sys.stdout.flush()
