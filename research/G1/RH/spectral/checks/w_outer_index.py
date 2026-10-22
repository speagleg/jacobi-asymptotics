"""JZC_W_outer §1-§2, §4 (NUMERICAL / exact identities, mpmath dps 40): index map, interpolation, spectral data, gauge algebra
for lam_k = (k + d)^p + kappa.
  [I1] Moebius index map zeta(z) = z/(1 - z/zs), zs = n^p/kappa: zeta(X_k) = Xi_k := (n/(k + d))^p, t_k(X_k) = k + d,
       zeta maps C_+ into C_+; t_k(z) = (n^p/z - kappa)^{1/p} = t(zeta(z)).
  [I2] node masses: Res_{X_k} W_k/(e^{2 i theta_k} - 1) = n^p lam_k^{-s/p}, W_k = w_n z^alpha (1 - z/zs)^{1/p - 1}, theta_k = pi(t_k - d)
       (contour integrals; radius < 1/3 of the distance to zs); controls (must fail): the lattice-type weight w_n z^alpha (no
       density factor r_n), and the uncomposed Hurwitz phase pi(t(z) - d) (no pole at the kappa-node: circle of radius < 1/3 of the
       distance from X_k to the Hurwitz node Xi_k).
  [I3] zero count: 1 - e^{2 i theta_k} has exactly the kappa-nodes as zeros in {r1 < |z| < r2, |arg z| < 0.95 pi} (p > 1; argument
       principle).
  [Z0] Z(0) = -1/2 - d for p > 1 and every kappa > -a^p (binomial-Hurwitz series with w = +-h; for kappa >= a^p after splitting off
       K0 terms), and for p < 1 with 1/p not an integer; for p = 1/m: Z(0) = -1/2 - d + (-kappa)^m (control: the kappa-free value fails).
  [A]  the gauge density's branched coefficients: a_m := -binom(1/p, m)(-kappa)^m = -R_{q_m}/q_m, q_m = m - 1/p, with famK's
       residues R_{q_m} = -binom(q_m, m) kappa^m/p (m = 1..6; exact identity, checked at random p, kappa).
  [T]  Toda times: Hurwitz part composed with zeta + density + gauge FP moments = W's mu_j = 2 Z_kappa(-j)/j - B_j (j = 1..5):
       sum_{m<=j} (2/m) binom(j-1, m-1) kappa^{j-m} zeta(-mp, a) + 2 zeta(0, a) kappa^j/j - B_j,  B_j = -(1/p - 1) kappa^j/j ... (log r_n)
       against 2 Z_kappa(-j)/j - B_j with Z_kappa(-j) = sum_i binom(j, i) kappa^i zeta(-p(j - i), a).
  [PV] PV int_0^L y^q/(y - x) dy = -pi cot(pi q) x^q + sum_j x^j L^{q-j}/(q - j) (q in (-1, 1) non-integer), quadrature check.
  [FP] FP int_0^inf rho1(y) y^{-j-1} dy for kappa > 0 (closed form via B(-1/p - j, 1 + 1/p)/Gamma(1-j) = 0): the O(n) part vanishes."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from w_common import Checks
mp.mp.dps = 40
I = mp.mpc(0, 1); PI = mp.pi; HALF = mp.mpf(1)/2
C_ = Checks()
def say(*a): print(*a, flush=True)


# ---------------- [I1]-[I3] ----------------
for (p, d, kap, s) in [(1.5, -0.3, 0.5, 2.0), (1.5, -0.3, -0.3, 2.0), (3, -0.7, 1.0, 2.5), (3, -0.7, -0.02, 2.5), (2.5, 0, 0.7, 3.0)]:
    p, d, kap, s = mp.mpf(p), mp.mpf(d), mp.mpf(kap), mp.mpf(s); n = mp.mpf(4); lab = f"p={mp.nstr(p,3)} d={mp.nstr(d,2)} kappa={mp.nstr(kap,3)}"
    zs = n**p/kap; al = (s - 1 - p)/p; wn = -(2*PI*I/p)*n**(1 + p - s)
    zeta = lambda z: z/(1 - z/zs)
    t = lambda z: n*mp.power(z, -1/p)
    tk = lambda z: (n**p/z - kap)**(1/p)
    lam = lambda k: (k + d)**p + kap
    X = lambda k: n**p/lam(k)
    worst = 0
    for k in range(1, 7):
        worst = max(worst, abs(zeta(X(k)) - (n/(k + d))**p)/abs(X(k)), abs(tk(X(k)) - (k + d)), abs(t(zeta(X(k))) - (k + d)))
    C_.check(f"[I1] {lab}: zeta(X_k) = Hurwitz node, t_k(X_k) = k + d (k <= 6)", float(worst) < 1e-30)
    w2 = 0; up = True
    for z in (mp.mpc('0.3', '0.01'), mp.mpc('5', '2'), mp.mpc('-7', '0.5'), mp.mpc('100', '1e-3'), mp.mpc('-1e5', '3')):
        w2 = max(w2, abs(tk(z) - t(zeta(z)))); up = up and mp.im(zeta(z)) > 0
    C_.check(f"[I1] {lab}: t_k = t o zeta (principal branches) on sample points of C_+", float(w2) < 1e-30)
    C_.check(f"[I1] {lab}: zeta(C_+) in C_+", up)
    Wk = lambda z: wn*mp.power(z, al)*mp.power(1 - z/zs, 1/p - 1)
    Wl = lambda z: wn*mp.power(z, al)
    res = lambda f, x, r: mp.quad(lambda th: f(x + r*mp.expj(th))*I*r*mp.expj(th), [0, PI/2, PI, 3*PI/2, 2*PI])/(2*PI*I)
    for k in (1, 2, 3):
        x = X(k); r = (X(k) - X(k + 1))/5
        if kap > 0: r = min(r, (zs - x)/3)                       # keep the branch point zs outside the circle
        rc = min(r, abs(x - (n/(k + d))**p)/3)                    # control circle: excludes the Hurwitz node Xi_k
        mass = n**p*lam(k)**(-s/p)
        R1 = res(lambda z: Wk(z)/(mp.exp(2*PI*I*(tk(z) - d)) - 1), x, r)
        R2 = res(lambda z: Wl(z)/(mp.exp(2*PI*I*(tk(z) - d)) - 1), x, r)
        R3 = res(lambda z: Wk(z)/(mp.exp(2*PI*I*(t(z) - d)) - 1), x, rc)
        say(f"[I2] {lab} k={k}: Res = {mp.nstr(R1, 15)}  mass n^p lam_k^(-s/p) = {mp.nstr(mass, 15)};  ctrl no r_n: {mp.nstr(R2, 8)};  ctrl uncomposed phase: {mp.nstr(R3, 3)}")
        C_.check(f"[I2] {lab} k={k}: residue = node mass", float(abs(R1 - mass)/mass) < 1e-25)
        C_.check(f"[ctrl] {lab} k={k}: weight without r_n gives a wrong residue (must fail)", float(abs(R2 - mass)/mass) > 1e-3)
        C_.check(f"[ctrl] {lab} k={k}: uncomposed Hurwitz phase gives no pole (must fail)", float(abs(R3 - mass)/mass) > 0.5)
    # [I3] argument principle in an annulus sector containing X_1..X_4 (|t_k| in (k+d) +- 1/2 ranges)
    r1 = (X(4) + X(5))/2; r2 = X(1)*mp.mpf('1.05')
    if kap > 0: r2 = min(r2, (X(1) + zs)/2)
    phi = mp.mpf('0.95')*PI
    g = lambda z: 1 - mp.exp(2*PI*I*(tk(z) - d))
    def dlog(z, dz): return (g(z + dz) - g(z - dz))/(2*dz)/g(z)
    def seg(z0, z1):
        return mp.quad(lambda u: dlog(z0 + (z1 - z0)*u, mp.mpf(10)**-12*abs(z1 - z0))*(z1 - z0), [0, mp.mpf(1)/2, 1])
    def arc(r, a0, a1):
        return mp.quad(lambda th: dlog(r*mp.expj(th), mp.mpf(10)**-12*r)*I*r*mp.expj(th), mp.linspace(a0, a1, 9))
    tot = arc(r2, -phi, phi) + seg(r2*mp.expj(phi), r1*mp.expj(phi)) + arc(r1, phi, -phi) + seg(r1*mp.expj(-phi), r2*mp.expj(-phi))
    cnt = tot/(2*PI*I)
    nn = sum(1 for k in range(1, 10) if r1 < X(k) < r2)
    say(f"[I3] {lab}: zeros of 1 - e^(2i theta_k) in {{{mp.nstr(r1,5)} < |z| < {mp.nstr(r2,5)}, |arg z| < 0.95 pi}}: {mp.nstr(cnt, 8)}; kappa-nodes there: {nn}")
    C_.check(f"[I3] {lab}: zero count = number of kappa-nodes", float(abs(cnt - nn)) < 1e-6)

# ---------------- [Z0] ----------------
H = mp.mpf(10)**-15
def Zser(w, p, d, kap, K0=0, imax=300):
    a = K0 + 1 + d
    head = sum(((k + d)**p + kap)**(-w) for k in range(1, K0 + 1))
    return head + sum(mp.binomial(-w, i)*kap**i*mp.zeta(p*(w + i), a) for i in range(imax))
def Z0(p, d, kap, K0=0): return (Zser(H, p, d, kap, K0) + Zser(-H, p, d, kap, K0))/2
for (p, d, kap, K0) in [(2.5, -0.3, 0.3, 0), (2.5, -0.3, -0.3, 0), (1.5, -0.4, 0.4, 0), (3, -0.7, 2.0, 3), (2.5, 0, 5.0, 4),
                        (0.6, -0.3, 0.2, 0)]:
    p, d, kap = mp.mpf(p), mp.mpf(d), mp.mpf(kap)
    v = Z0(p, d, kap, K0)
    say(f"[Z0] p={mp.nstr(p,3)} d={mp.nstr(d,2)} kappa={mp.nstr(kap,3)} (K0={K0}): Z(0) = {mp.nstr(v, 25)}  (-1/2 - d = {mp.nstr(-HALF - d, 6)})")
    C_.check(f"[Z0] p={mp.nstr(p,3)} kappa={mp.nstr(kap,3)}: Z(0) = -1/2 - d (kappa-free)", float(abs(v + HALF + d)) < 1e-12)
for (m, d, kap) in [(2, -0.3, 0.2), (2, -0.3, -0.25), (3, -0.5, 0.15)]:
    p = mp.mpf(1)/m; d, kap = mp.mpf(d), mp.mpf(kap)
    v = Z0(p, d, kap); pred = -HALF - d + (-kap)**m
    say(f"[Z0] p=1/{m} d={mp.nstr(d,2)} kappa={mp.nstr(kap,3)}: Z(0) = {mp.nstr(v, 20)}  pred -1/2 - d + (-kappa)^{m} = {mp.nstr(pred, 20)}")
    C_.check(f"[Z0] p=1/{m} kappa={mp.nstr(kap,3)}: Z(0) = -1/2 - d + (-kappa)^{m}", float(abs(v - pred)) < 1e-12)
    C_.check(f"[ctrl] p=1/{m} kappa={mp.nstr(kap,3)}: the kappa-free value fails (must fail)", float(abs(v + HALF + d)) > 1e-3)

# ---------------- [A] branched coefficients = -R_q/q ----------------
for (p, kap) in [(mp.mpf('1.37'), mp.mpf('0.61')), (mp.mpf('2.9'), mp.mpf('-0.23')), (mp.mpf('0.7'), mp.mpf('0.4'))]:
    w = 0
    for m in range(1, 7):
        q = m - 1/p; a_m = -mp.binomial(1/p, m)*(-kap)**m; R = -mp.binomial(q, m)*kap**m/p
        w = max(w, abs(a_m + R/q))
    C_.check(f"[A] p={mp.nstr(p,3)} kappa={mp.nstr(kap,3)}: a_m = -R_qm/q_m (m <= 6)", float(w) < 1e-35)

# ---------------- [T] Toda times ----------------
for (p, d, kap) in [(2.5, -0.3, 0.3), (2.5, -0.3, -0.3), (1.5, -0.4, 0.4), (3, -0.7, 1.7)]:
    p, d, kap = mp.mpf(p), mp.mpf(d), mp.mpf(kap); a = 1 + d; w = 0
    for j in range(1, 6):
        hur = sum(2*mp.binomial(j - 1, m - 1)*kap**(j - m)*mp.zeta(-m*p, a)/m for m in range(1, j + 1))
        gauge = 2*mp.zeta(0, a)*kap**j/j
        Zj = sum(mp.binomial(j, i)*kap**i*mp.zeta(-p*(j - i), a) for i in range(0, j + 1))
        w = max(w, abs(hur + gauge - 2*Zj/j))
        if j == 1: g1 = abs(hur - 2*Zj/j)
    C_.check(f"[T] p={mp.nstr(p,3)} d={mp.nstr(d,2)} kappa={mp.nstr(kap,3)}: Hurwitz o zeta + gauge FP = 2 Z_kappa(-j)/j (j <= 5)", float(w) < 1e-30)
    C_.check(f"[ctrl] p={mp.nstr(p,3)} kappa={mp.nstr(kap,3)}: without the gauge share the identity fails (must fail)", float(g1) > 1e-3)
    # density: log r_n = (1/p - 1) log(1 - kappa x) = -sum_j (1/p - 1) kappa^j x^j / j  (W's B_j from D(x) = (1 - kappa x)^{1/p - 1})
    Bj = [-(1/p - 1)*kap**j/j for j in range(1, 6)]
    tay = mp.taylor(lambda x: (1/p - 1)*mp.log(1 - kap*x), 0, 5)
    C_.check(f"[T] p={mp.nstr(p,3)} kappa={mp.nstr(kap,3)}: density B_j = Taylor coefficients of log r_n", float(max(abs(tay[j] - Bj[j - 1]) for j in range(1, 6))) < 1e-30)

# ---------------- [PV] ----------------
for q in (mp.mpf('0.6'), mp.mpf('1')/3, mp.mpf('-0.4')):
    for x in (mp.mpf('0.3'), mp.mpf('1.7')):
        L = mp.mpf(5)
        num = mp.quad(lambda y: (y**q - x**q)/(y - x), [0, x, L]) + x**q*mp.log((L - x)/x)
        pred = -PI*mp.cot(PI*q)*x**q + mp.nsum(lambda j: x**j*L**(q - j)/(q - j), [0, mp.inf])
        C_.check(f"[PV] q={mp.nstr(q,3)} x={x}: PV int_0^L y^q/(y-x) = -pi cot(pi q) x^q + sum_j x^j L^(q-j)/(q-j)", float(abs(num - pred)) < 1e-25)

# ---------------- [FP] ----------------
for (p, d, kap, n) in [(2.5, -0.3, 0.3, 4), (1.5, -0.4, 0.4, 7)]:
    p, d, kap, n = mp.mpf(p), mp.mpf(d), mp.mpf(kap), mp.mpf(n); zs = n**p/kap
    for j in (1, 2, 3):
        sj = -1/p - j
        Bc = mp.gamma(sj)*mp.gamma(1 + 1/p)*mp.rgamma(sj + 1 + 1/p)
        # FP int_0^1 u^{s-1}(1 - (1-u)^{1/p}) du + int_1^inf u^{s-1} du = 1/s - B(s, 1 + 1/p) - 1/s
        val = n*zs**sj*(-Bc) - (d + HALF)*zs**(-j)/j
        pred = mp.zeta(0, 1 + d)*kap**j*n**(-j*p)/j
        C_.check(f"[FP] p={mp.nstr(p,3)} kappa={mp.nstr(kap,3)} j={j}: B(-1/p-j, 1+1/p) = 0 and FP_j = zeta(0,a) kappa^j n^-jp / j", float(abs(Bc)) < 1e-35 and float(abs(val - pred)) < 1e-35)
C_.finish()
