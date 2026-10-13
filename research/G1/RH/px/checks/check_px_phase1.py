"""Plan 12 Phase 1 (NUMERICAL, end-to-end): interpolation problem for sigma = sum_k k^{-s} delta_{k^{-p}} in the
x-variable.  Rescale U(z) = N^{pN sigma3} Y(z/N^p): nodes X_k = (N/k)^p, t(z) = N z^{-1/p} (cut (-inf,0]),
theta = pi t, Pi = sin(theta)/theta', w(z) = N^p t(z)^{-s} (so Res_{X_k} U12 = w(X_k) U11(X_k)).
 [1] band node (X_k < 4c): R = U [[1, -w e^{-i theta}/Pi],[0,1]] (upper half) has no pole; |U12| ~ 1/dist.
 [2] saturated node (X_k > 4c): R = U Pi^{-sigma3}[[1,0],[-e^{-i theta}/(Pi w),1]]-type (WLXZ (3.10)/(3.15)):
     R12 = U12 Pi, R11 = U11/Pi - U12 e^{-i theta}/w; both stay bounded.
 [3] effective band weight W = 2 i theta' w: |W| = (2 pi/p) N^{1+p-s} x^{(s-1-p)/p}, i.e. hard-edge exponent
     alpha_x = (s-1-p)/p at x = 0 (> -1 iff s > 1).
 [4] t on the slit plane: arg t = -arg z/p in (-pi/p, pi/p) subset (-pi, pi) for p > 1 (Gamma(t) pole-free)."""
import mpmath as mp

mp.mp.dps = 80
p, s, N, K = mp.mpf(2), mp.mpf(3), 12, 3000
xs = [mp.power(k, -p) for k in range(1, K + 1)]
ms = [mp.power(k, -s) for k in range(1, K + 1)]
# monic OPs by Stieltjes (discrete inner product on the K atoms)
P = [[mp.mpf(1)] * K]; prev = [mp.mpf(0)] * K; h = [sum(ms)]; A = []; B2 = []
for n in range(N):
    cur = P[-1]
    an = sum(ms[i] * xs[i] * cur[i] ** 2 for i in range(K)) / h[-1]
    nxt = [(xs[i] - an) * cur[i] - (B2[-1] if B2 else 0) * prev[i] for i in range(K)]
    hn = sum(ms[i] * nxt[i] ** 2 for i in range(K))
    A.append(an); B2.append(hn / h[-1]); h.append(hn); prev = cur; P.append(nxt)
def poly(x, n):
    a, b = mp.mpf(1), x - A[0]
    if n == 0: return a
    for m in range(1, n):
        a, b = b, (x - A[m]) * b - B2[m - 1] * a
    return b
def Y(x):
    return mp.matrix([[poly(x, N), sum(ms[i] * P[N][i] / (x - xs[i]) for i in range(K))],
                      [poly(x, N - 1) / h[N - 1], sum(ms[i] * P[N - 1][i] / (x - xs[i]) for i in range(K)) / h[N - 1]]])
sc = mp.power(N, p)
def U(z):
    return mp.diag([mp.power(sc, N), mp.power(sc, -N)]) * Y(z / sc)
t = lambda z: N * mp.power(z, -1 / p)
th = lambda z: mp.pi * t(z)
dth = lambda z: -mp.pi * N / p * mp.power(z, -1 / p - 1)
Pi = lambda z: mp.sin(th(z)) / dth(z)
w = lambda z: sc * mp.power(t(z), -s)
c = mp.pi ** 2 / 16   # c(2)
print(f"p={p} s={s} N={N}: band (0, 4c) = (0, {mp.nstr(4*c, 6)})")
print("[1] band node")
k = 3 * N; Xk = mp.power(mp.mpf(N) / k, p)
for d in ["1e-4", "1e-8", "1e-12"]:
    z = Xk + 1j * mp.mpf(d)
    Uz = U(z); R12 = Uz[0, 1] - Uz[0, 0] * w(z) * mp.exp(-1j * th(z)) / Pi(z)
    R22 = Uz[1, 1] - Uz[1, 0] * w(z) * mp.exp(-1j * th(z)) / Pi(z)
    print(f"  X_{k}={mp.nstr(Xk,5)} dist {d}: |U12|={mp.nstr(abs(Uz[0,1]),5)}  |R12|={mp.nstr(abs(R12),10)}  |R22|={mp.nstr(abs(R22),10)}")
print("[2] saturated node")
k = N // 2; Xk = mp.power(mp.mpf(N) / k, p)
for d in ["1e-4", "1e-8", "1e-12"]:
    z = Xk + 1j * mp.mpf(d)
    Uz = U(z)
    R11 = Uz[0, 0] / Pi(z) - Uz[0, 1] * mp.exp(-1j * th(z)) / w(z)
    R12 = Uz[0, 1] * Pi(z)
    print(f"  X_{k}={mp.nstr(Xk,5)} dist {d}: |U12|={mp.nstr(abs(Uz[0,1]),5)}  |R11|={mp.nstr(abs(R11),10)}  |R12|={mp.nstr(abs(R12),10)}")
print("[3] band weight")
for x in [mp.mpf("0.05"), mp.mpf("0.5"), mp.mpf("2")]:
    W = 2j * dth(x) * w(x)
    pred = 2 * mp.pi / p * mp.power(N, 1 + p - s) * mp.power(x, (s - 1 - p) / p)
    print(f"  x={x}: |W|={mp.nstr(abs(W),12)}  pred={mp.nstr(pred,12)}  arg W/pi={mp.nstr(mp.arg(W)/mp.pi,6)}")
print("[4] arg t on the slit plane, p=2: arg z = +-(pi - 1e-9) -> arg t =",
      [mp.nstr(mp.arg(t(mp.mpf(2) * mp.expjpi(sg * (1 - mp.mpf('1e-9'))))) / mp.pi, 6) for sg in (1, -1)], "(units of pi)")
