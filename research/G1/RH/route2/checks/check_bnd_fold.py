"""Plan 53 (NUMERICAL checks of the fold lemmas of ROUTE2_bnd.md; mpmath, 40 digits).
[1] Lemma F0 (exact fold of the OP RH matrix): for a finite symmetric measure nu (nodes +-k^{-1/2}, masses k^{-r}Psi(k)/2,
    k <= K) and mu = (y -> y^2)_* nu, fold(Y_nu^{(2m)})(x) := z^{-s3/2} Y_nu^{(2m)}(z) z^{s3/2} (x = z^2) equals
    [[1, 0], [-2 pi i gamma_{2m-1}^2, 1]] Y_mu^{(m)}(x)  (gamma_j^2 = 1/||pi_j||^2_nu).  Printed: max entry error, both
    choices z = +-sqrt(x).
[2] Lemma P (parity of WLXZ's scalar data): g(-z) = g(z) - i pi (z in C+), from (2.1)-(2.2); D(-z) = D(z) for (2.6) with the
    principal log of -n/z^2; Dhat(z) = Dtilde(-z) for (4.15), (4.22) (alpha_W = 1).
[3] Lemma FN (folded outer parametrix): with N0 the [-2,2] solution (jump [[0,1],[-1,0]]), D_a = (z/Phi)^a, and
    D^x_{alpha}(x)^2 = (4x/Phi_x(x))^alpha, Phi_x = (x^{1/2} + (x-4)^{1/2})^2 (ROUTE2 §3.3 with b = 4), the matrix
    M(x) := fold(N0)(z) Gamma(z)^{s3}, Gamma := D^x_{alpha}(z^2)/D_a(z), alpha = a - 1/2, satisfies M(x) N0x(x)^{-1} = const,
    N0x the [0,4] solution (jump [[0,1],[-1,0]]).  Printed: the constant at 6 points and its spread.
[4] Local amplification (the new local estimate behind OBSTRUCTION-a and its removal): on a lip ray,
    unfolded (KV/Vanlessen model at a = 1/2, Bessel orders 1, 0):  |Psi e2 e1^T Psi^{-1}| * |zeta|  ->  const  (NOT integrable
    against |dz| ~ |dzeta|/n near 0: the log-divergence of D1's main term);
    folded (KMVV Bessel model of order alpha_x = 0, ray arg zeta_K = pi/2):  |Psi e2 e1^T Psi^{-1}| / (1 + log^2|zeta_K|)
    bounded (integrable against |dx|).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan53/research/G1/RH/route2/checks/check_bnd_fold.py"""
import mpmath as mp

mp.mp.dps = 40
I2 = mp.matrix([[1, 0], [0, 1]])


def M2(a, b, c, d):
    return mp.matrix([[a, b], [c, d]])


def maxabs(A):
    return max(abs(A[i, j]) for i in range(A.rows) for j in range(A.cols))


# ---------------------------------------------------------------- [1] Lemma F0
def monic_ops(nodes, w, N):
    """Monic OPs pi_0..pi_N of sum w_j delta_{nodes_j} by the Stieltjes procedure (high precision)."""
    P = [[mp.mpf(1)] * len(nodes)]
    norms = [mp.fsum(w)]
    al, be = [], []
    prev = [mp.mpf(0)] * len(nodes)
    for k in range(N):
        cur = P[-1]
        a_k = mp.fsum(w[j] * nodes[j] * cur[j] ** 2 for j in range(len(nodes))) / norms[-1]
        b_k = norms[-1] / norms[-2] if k > 0 else mp.mpf(0)
        nxt = [(nodes[j] - a_k) * cur[j] - b_k * prev[j] for j in range(len(nodes))]
        al.append(a_k); be.append(b_k)
        prev = cur; P.append(nxt); norms.append(mp.fsum(w[j] * nxt[j] ** 2 for j in range(len(nodes))))
    return al, be, norms


def poly_eval(al, be, deg, z):
    p0, p1 = mp.mpf(1), z - al[0]
    if deg == 0:
        return p0
    for k in range(1, deg):
        p0, p1 = p1, (z - al[k]) * p1 - be[k] * p0
    return p1


def Ymat(nodes, w, al, be, norms, n, z):
    pn = poly_eval(al, be, n, z); pn1 = poly_eval(al, be, n - 1, z)
    C = lambda deg: mp.fsum(w[j] * poly_eval(al, be, deg, nodes[j]) / (nodes[j] - z) for j in range(len(nodes))) / (2j * mp.pi)  # noqa: E731
    g2 = 1 / norms[n - 1]
    return M2(pn, C(n), -2j * mp.pi * g2 * pn1, -2j * mp.pi * g2 * C(n - 1)), g2


def check1():
    K, r, m = 30, mp.mpf(2), 4
    Psi = lambda k: mp.e ** mp.sqrt(mp.log(k + mp.e))  # noqa: E731
    yk = [1 / mp.sqrt(k) for k in range(1, K + 1)]
    wk = [k ** (-r) * Psi(k) for k in range(1, K + 1)]
    nodes_nu = [y for y in yk] + [-y for y in yk]; w_nu = [w / 2 for w in wk] * 2
    nodes_mu = [y ** 2 for y in yk]; w_mu = wk
    an, bn, nn = monic_ops(nodes_nu, w_nu, 2 * m + 1)
    am, bm, nm = monic_ops(nodes_mu, w_mu, m + 1)
    print("[1] Lemma F0: fold(Y_nu^(2m)) = [[1,0],[-2 pi i gamma_{2m-1}^2, 1]] Y_mu^(m)   (K = 30, r = 2, m = 4)")
    for x in (mp.mpc(0.3, 0.2), mp.mpc(-0.5, 0.1), mp.mpc(2.0, -1.0), mp.mpc(0.01, 0.003)):
        errs = []
        for z in (mp.sqrt(x), -mp.sqrt(x)):
            Yn, g2 = Ymat(nodes_nu, w_nu, an, bn, nn, 2 * m, z)
            fold = M2(Yn[0, 0], Yn[0, 1] / z, z * Yn[1, 0], Yn[1, 1])
            Ym, _ = Ymat(nodes_mu, w_mu, am, bm, nm, m, x)
            errs.append(maxabs(fold - M2(1, 0, -2j * mp.pi * g2, 1) * Ym) / maxabs(Ym))
        print(f"    x = {mp.nstr(x, 4):>18}: relative error {mp.nstr(errs[0], 3)} (z = +sqrt x), {mp.nstr(errs[1], 3)} (z = -sqrt x)")
    # the fold relations for the recurrence coefficients (sanity): a_m = beta_{2m} + beta_{2m+1}, b_m^2 = beta_{2m+1} beta_{2m+2}
    # (0-based: am[j] couples ..., bn[k] = ||pi_k||^2/||pi_{k-1}||^2)
    e1 = max(abs(am[j] - (bn[2 * j] + bn[2 * j + 1])) for j in range(m))
    e2 = max(abs(bm[j] - bn[2 * j - 1] * bn[2 * j]) for j in range(1, m))
    print(f"    sanity: max|a_j(mu) - (beta_2j + beta_2j+1)| = {mp.nstr(e1, 3)}, max|b_j(mu)^2 - beta_2j-1 beta_2j| = {mp.nstr(e2, 3)}")


# ---------------------------------------------------------------- [2] Lemma P
def psi(x):
    x = abs(x)
    if x <= 2:
        return (4 * mp.atan(x / mp.sqrt(4 - x * x)) / x ** 3 - mp.sqrt(4 - x * x) / x ** 2) / mp.pi
    return 2 / x ** 3


def g(z):
    f = lambda s: mp.log(z - s) * psi(s)  # noqa: E731  (principal log: arg(z - s) in (-pi, pi))
    return mp.quad(f, [-mp.inf, -2, -1, 0, 1, 2, mp.inf])


def check2():
    mp.mp.dps = 20
    print("[2] Lemma P: WLXZ parity data (alpha_W = 1, n = 10)")
    tot = mp.quad(psi, [-mp.inf, -2, 0, 2, mp.inf])
    print(f"    int psi = {mp.nstr(tot, 15)}")
    for z in (mp.mpc(0.3, 0.4), mp.mpc(1.5, 0.2), mp.mpc(-0.7, 1.1), mp.mpc(3.0, 0.5)):
        print(f"    z = {mp.nstr(z, 3):>12}: g(-z) - g(z) = {mp.nstr(g(-z) - g(z), 12)}   (expected -i pi = {mp.nstr(-1j * mp.pi, 12)})")
    n, al = 10, 1

    def D(z):  # (2.6), principal log of -n/z^2
        t = -n / z ** 2
        return mp.gamma(al + t) * mp.e ** t * mp.power(t, -t - al + mp.mpf(1) / 2) / mp.sqrt(2 * mp.pi)

    def Dt(z):  # (4.15), log(n/z^2) := log n - 2 log z with log z principal
        L = mp.log(n) - 2 * mp.log(z); s = n / z ** 2
        return mp.sqrt(2 * mp.pi) * mp.e ** ((s - al + mp.mpf(1) / 2) * L) / (mp.gamma(1 + s - al) * mp.e ** s)

    def Dh(z):  # (4.22), with arg(-z) in (-pi, pi)
        L = mp.log(n) - 2 * mp.log(-z); s = n / z ** 2
        return mp.sqrt(2 * mp.pi) * mp.e ** ((s - al + mp.mpf(1) / 2) * L) / (mp.gamma(1 + s - al) * mp.e ** s)

    for z in (mp.mpc(0.6, 0.5), mp.mpc(2.5, 0.3), mp.mpc(0.4, -1.3)):
        print(f"    z = {mp.nstr(z, 3):>12}: |D(-z)/D(z) - 1| = {mp.nstr(abs(D(-z) / D(z) - 1), 3)},"
              f"  |Dhat(-z)/Dtilde(z) - 1| = {mp.nstr(abs(Dh(-z) / Dt(z) - 1), 3)}")
    mp.mp.dps = 40


# ---------------------------------------------------------------- [3] Lemma FN
def N0(z, b0=-2, b1=2):
    gam = mp.power((z - b1) / (z - b0), mp.mpf(1) / 4)
    return M2((gam + 1 / gam) / 2, (gam - 1 / gam) / (2j), -(gam - 1 / gam) / (2j), (gam + 1 / gam) / 2)


def Dsym(z, a):  # D_a = (z/Phi)^a, Phi = (z + R)/2, R = sqrt(z-2) sqrt(z+2)
    R = mp.sqrt(z - 2) * mp.sqrt(z + 2)
    return mp.power(2 * z / (z + R), a)


def Dx(x, al):  # D_{x^al} on [0,4]: D^2 = (4x/Phi_x)^al, Phi_x = (sqrt x + sqrt(x-4))^2
    Phx = (mp.sqrt(x) + mp.sqrt(x - 4)) ** 2
    return mp.power(4 * x / Phx, al / 2)


def check3():
    print("[3] Lemma FN: M(x) N0x(x)^{-1} is constant (M := fold(N0) Gamma^{s3}, Gamma = D^x_alpha(z^2)/D_a(z))")
    for a in (mp.mpf("0.5"), mp.mpf("0.8"), mp.mpf("0.1")):
        al = a - mp.mpf(1) / 2
        Cs = []
        for x in (mp.mpc(0.001, 0.0005), mp.mpc(-3, 0.2), mp.mpc(1, -2), mp.mpc(3.9, 0.01), mp.mpc(50, 7), mp.mpc(0.5, -0.0001)):
            z = mp.sqrt(x)
            N = N0(z); Gm = Dx(x, al) / Dsym(z, a)
            M = M2(N[0, 0], N[0, 1] / z, z * N[1, 0], N[1, 1]) * M2(Gm, 0, 0, 1 / Gm)
            Cs.append(M * N0(x, 0, 4) ** -1)
        spread = max(maxabs(C - Cs[0]) for C in Cs)
        C = Cs[0]
        print(f"    a = {a} (alpha_x = {al}): const = [[{mp.nstr(C[0,0], 6)}, {mp.nstr(C[0,1], 6)}], [{mp.nstr(C[1,0], 6)}, {mp.nstr(C[1,1], 6)}]],"
              f" spread over 6 points = {mp.nstr(spread, 3)}")
    # band jump of N0x and of fold(N0)Gamma^{s3} on (0,4) (x = 1.7): both [[0,1],[-1,0]]
    x, e = mp.mpf("1.7"), mp.mpf("1e-25")
    J = N0(x - 1j * e, 0, 4) ** -1 * N0(x + 1j * e, 0, 4)
    print(f"    N0x band jump at x = 1.7: [[{mp.nstr(J[0,0], 3)}, {mp.nstr(J[0,1], 6)}], [{mp.nstr(J[1,0], 6)}, {mp.nstr(J[1,1], 3)}]]")


# ---------------------------------------------------------------- [4] local amplification
def Psi_KV_II(zeta, lam):
    """Vanlessen (4.27), sector II (pi/4 < arg zeta < pi/2)."""
    w = zeta * mp.e ** (-1j * mp.pi / 2)
    s = mp.sqrt(zeta)
    A = M2(mp.sqrt(mp.pi) * s * mp.besseli(lam + 0.5, w), -s * mp.besselk(lam + 0.5, w) / mp.sqrt(mp.pi),
           -1j * mp.sqrt(mp.pi) * s * mp.besseli(lam - 0.5, w), -1j * s * mp.besselk(lam - 0.5, w) / mp.sqrt(mp.pi))
    return A * M2(mp.e ** (-0.5j * lam * mp.pi), 0, 0, mp.e ** (0.5j * lam * mp.pi))


def Psi_KMVV(zeta, al):
    """KMVV (6.23), |arg zeta| < 2 pi/3."""
    s = mp.sqrt(zeta); x = 2 * s
    Ip = mp.besseli(al + 1, x) + al / x * mp.besseli(al, x)   # DLMF 10.29.2
    Kp = -mp.besselk(al + 1, x) + al / x * mp.besselk(al, x)
    return M2(mp.besseli(al, x), 1j / mp.pi * mp.besselk(al, x), 2j * mp.pi * s * Ip, -2 * s * Kp)


def rank1(P):
    e = P ** -1
    return M2(P[0, 1] * e[0, 0], P[0, 1] * e[0, 1], P[1, 1] * e[0, 0], P[1, 1] * e[0, 1])  # (P e2)(e1^T P^{-1})


def check4():
    print("[4] local amplification on a lip ray (the D1/D^x main-term factor Psi e2 e1^T Psi^{-1})")
    print("    |zeta|      unfolded KV a=1/2 (arg pi/4+):  |.|*|zeta|     det      folded KMVV alpha=0 (arg pi/2): |.|/(1+log^2|zeta|)   det")
    for k in (1, 2, 4, 6, 8, 10, 12):
        rho = mp.mpf(10) ** (-k)
        zK = rho * mp.e ** (1j * (mp.pi / 4 + mp.mpf("1e-30")))
        PK = Psi_KV_II(zK, mp.mpf("0.5"))
        zB = rho * mp.e ** (1j * mp.pi / 2)
        PB = Psi_KMVV(zB, 0)
        u = maxabs(rank1(PK)) * rho; f = maxabs(rank1(PB)) / (1 + mp.log(rho) ** 2)
        print(f"    1e-{k:<2d}     {mp.nstr(u, 6):>14}                     {mp.nstr(mp.det(PK), 6):>10}      {mp.nstr(f, 6):>14}                      {mp.nstr(mp.det(PB), 6)}")


if __name__ == "__main__":
    check1(); check2(); check3(); check4()
