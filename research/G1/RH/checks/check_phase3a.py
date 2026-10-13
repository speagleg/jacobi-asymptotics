"""Plan 10 Phase 3a (NUMERICAL, end-to-end): build the interpolation-problem solution Y from the actual symmetric OPs
of nu = sum_k (k^-r/2)(delta_{s_k} + delta_{-s_k}), s_k = k^{-q}, rescale U(z) = N^{q N sigma3} Y(N^{-q} z), apply the
WLXZ-type factor R = U U_+ (upper-right region) and check:
 [1] R has no pole at nodes Z_k in the band region (|R| stays bounded approaching Z_k, while |U| ~ 1/dist);
 [2] the effective band weight W(x) = 2 i theta'(x) w(x) has |W| = 2 pi/p * N^{1+q-r} x^{2(r-1)/p - 1}: on the regular
     family r = 1 + p/2 it is exactly the constant 2 pi/p (checked against the definition of w).
Model: p = 2, r = 2 (regular; Lommel nu=1/2 up to scale), N = 24."""
import mpmath as mp

mp.mp.dps = 60
p, r, N, K = 2, 2, 24, 4000
q = mp.mpf(p) / 2
nodes = [mp.power(k, -q) for k in range(1, K + 1)]
masses = [mp.power(k, -r) / 2 for k in range(1, K + 1)]
S = nodes + [-s for s in nodes]
M = masses + masses
# monic OPs of nu by Stieltjes (symmetric => zero diagonal)
def ops(deg):
    P = [[mp.mpf(1)] * len(S)]
    prev = [mp.mpf(0)] * len(S)
    h = [sum(M)]
    g2 = []
    for n in range(deg):
        cur = P[-1]
        nxt = [S[i] * cur[i] - (g2[-1] if g2 else 0) * prev[i] for i in range(len(S))]
        hn = sum(M[i] * nxt[i] ** 2 for i in range(len(S)))
        g2.append(hn / h[-1]); h.append(hn)
        prev, P = cur, P + [nxt]
    return P, h, g2
P, h, g2 = ops(N)
# coefficients of R_N, R_{N-1} via recurrence on symbolic x: evaluate polynomials at arbitrary z with the recurrence
def Rpoly(z, n):
    a, b = mp.mpf(1), z
    if n == 0: return a
    for m in range(1, n):
        a, b = b, z * b - g2[m - 1] * a
    return b
def Y(s):
    y11 = Rpoly(s, N)
    y12 = sum(M[i] * P[N][i] / (s - S[i]) for i in range(len(S)))
    y21 = Rpoly(s, N - 1) / h[N - 1]
    y22 = sum(M[i] * P[N - 1][i] / (s - S[i]) for i in range(len(S))) / h[N - 1]
    return mp.matrix([[y11, y12], [y21, y22]])
def U(z):
    D = mp.matrix([[mp.power(N, q * N), 0], [0, mp.power(N, -q * N)]])
    return D * Y(z / mp.power(N, q))
theta = lambda z: mp.pi * N * mp.power(z * z, -1 / mp.mpf(p))
dth = lambda z: mp.diff(theta, z)
Pi = lambda z: mp.sin(theta(z)) / dth(z)
w = lambda z: mp.power(N, q) * mp.power(N * mp.power(z * z, -1 / mp.mpf(p)), -r) / 2
def Rmat(z):  # upper-right region: U_- (decaying e^{-i theta} upper-right) -- WLXZ: Omega_{r,+} uses U_-
    Uf = mp.matrix([[1, -w(z) * mp.exp(-1j * theta(z)) / Pi(z)], [0, 1]])
    return U(z) * Uf
k = 30                                   # a band node: Z_k = (k/N)^{-q}
Zk = mp.power(mp.mpf(k) / N, -q)
print(f"node Z_{k} = {mp.nstr(Zk, 8)}  (band edge r* = {mp.nstr(2 ** (1 + q) * mp.sqrt(mp.pi ** 2 / 16), 8)})")
for d in ["1e-3", "1e-5", "1e-7"]:
    z = Zk + mp.mpc(0, 1) * mp.mpf(d)
    print(f"  dist {d}: |U12| = {mp.nstr(abs(U(z)[0, 1]), 5)}   |R12| = {mp.nstr(abs(Rmat(z)[0, 1]), 8)}   |R22| = {mp.nstr(abs(Rmat(z)[1, 1]), 8)}")
for x in [mp.mpf("0.4"), mp.mpf("1.3"), mp.mpf("2.9")]:
    W = 2j * dth(x) * w(x)
    print(f"  x={x}: W(x) = {mp.nstr(W, 12)}   (2 pi/p = {mp.nstr(2 * mp.pi / p, 12)})")
