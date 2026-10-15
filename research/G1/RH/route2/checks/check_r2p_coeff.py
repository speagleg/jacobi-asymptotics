"""Plan 51 (NUMERICAL): Route II for 0 < p < 1 (ROUTE2_plt1.md §§4-6). p = 1/2, Psi(k) = exp(L(log k)),
L(u) = sqrt(log(e^u + e)) (so Psi(k) = exp(sqrt(log(k + e))); L is analytic on |Im u| < pi, so (H_an^{<1}) holds with L1 = L).
alpha_x = (s - 1 - p)/p: s = 1.5 -> 0 (Theorem RII_{<1} directly), s = 1.75 -> 1/2 (directly), s = 2 -> 1 (boundary of the
comparison frame; covered only through Lemma CT from s = 1.5), s = 2.5 -> 2 (Lemma CT twice).

Measure model (as research/G1/checks/check_ql_numerics.py, Plan 45): atoms k = 1..K exactly, plus a Gauss-Legendre quadrature
on log-panels (ratio 1.02, 8 nodes) of int_{K+1/2}^{T_END} t^{-s}Psi(t) delta_{t^{-p}} dt, T_END = 1e48 (midpoint/Euler-Maclaurin
continuation of the atom sum).  For p = 1/2 the hard-edge scale of degree n is k ~ n^{1+2/p} = n^5 (1e16 at n = 1600), far
beyond any atom truncation, so the tail is essential ([4] shows the no-tail values).  Every row is repeated with K and 2K.
Coefficients: RKPW (csrc, long double); [3] compares with quad precision.
Index convention (as check_r2_coeff.py): b_n couples p_{n-1}, p_n (b_n = sqrt(b2[n-1])); a_n = a[n]; E pairing a[n]/(2 sqrt(b2[n])).
  nB := n (n^p b_n / c(p) - 1)    (Law P with O(1/n): bounded)        tilt baseline -(s - 1 - theta_n)/2, theta_n = L'(log n)
  E  := n (a_n/(2 b_n) - 1)         (bounded; pure power e1 = p/2)
[2] Lemma CT (Christoffel step): Cholesky J(sigma_s) = L L^T (l_j diagonal, m_j subdiagonal); L^T L must be the Jacobi matrix of
    x sigma_s = sigma_{s+p} (same quadrature nodes, weights multiplied by x exactly).  Reports the max relative difference and
    r_n := l_n/m_n (Lemma CT: r_n -> 1; with O(1/n) input, r_n - 1 = O(n^{-1/2}); observed O(1/n)).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan51/research/G1/RH/route2/checks/check_r2p_coeff.py"""
import time
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

T0 = time.time()
p = 0.5; c = c_p(p); T_END = 1e48
L = lambda k: np.sqrt(np.log(k + np.e))  # noqa: E731  (Psi = exp L(log k) at the atoms; L as a function of t = k)
dL = lambda u: np.exp(u) / (2 * (np.exp(u) + np.e) * np.sqrt(np.log(np.exp(u) + np.e)))  # noqa: E731
NS = (100, 200, 400, 800, 1600)
NMAX = 1602


def model(K, ratio=1.02, kq=8):
    kk = np.arange(1, K + 1, dtype=float)
    e = np.arange(np.log(K + 0.5), np.log(T_END), np.log(ratio))
    g, gw = np.polynomial.legendre.leggauss(kq)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * g for a, b in zip(e[:-1], e[1:])])
    Wt = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    lab = np.concatenate([kk, np.exp(U)]); W = np.concatenate([np.ones(K), Wt * np.exp(U)])
    return lab, W


def coeffs(lab, W, s, psi=True, N=NMAX, prec="ld"):
    lw = np.log(W) - s * np.log(lab) + (L(lab) if psi else 0.0); lw -= lw.max()
    r = jacobi_coeffs(DiscreteMeasure(lab ** -p, np.exp(lw)), N, prec=prec)
    if prec == "q":
        return np.array([float(v) for v in r.a]), np.sqrt(np.array([float(v) for v in r.b2]))
    return np.asarray(r.a, np.longdouble), np.sqrt(np.asarray(r.b2, np.longdouble))


def law(a, b, ns=NS):
    return [(float(n * (n ** p * b[n - 1] / c - 1)), float(n * (a[n] / (2 * b[n]) - 1))) for n in ns]


def cholesky(a, b):
    n = len(b) - 1; l = np.zeros(n + 1, a.dtype); m = np.zeros(n + 1, a.dtype); l[0] = np.sqrt(a[0])
    for j in range(n):
        m[j] = b[j] / l[j]; l[j + 1] = np.sqrt(a[j + 1] - m[j] ** 2)
    return l, m


print(f"[0] p = {p}, c(p) = {c:.10f}; theta_n = L'(log n) = " + ", ".join(f"{dL(np.log(n)):.4f}" for n in NS)
      + "  (n = 100..1600)", flush=True)
print("\n[1] Law P numerics, quadrature tail to 1e48; columns n = 100, 200, 400, 800, 1600", flush=True)
RES = {}
for K in (100000, 200000):
    lab, W = model(K)
    for s in (1.5, 1.75, 2.0, 2.5):
        aw, bw = coeffs(lab, W, s); av, bv = coeffs(lab, W, s, psi=False)
        RES[(K, s)] = law(aw, bw) + law(av, bv)
        al = (s - 1 - p) / p
        print(f"  K={K} s={s} (alpha_x={al:+.2f}): w=k^-s Psi: nB = " + ", ".join(f"{x[0]:+.4f}" for x in law(aw, bw))
              + " | E = " + ", ".join(f"{x[1]:+.4f}" for x in law(aw, bw)), flush=True)
        print(f"      {'':28s}v=k^-s    : nB = " + ", ".join(f"{x[0]:+.4f}" for x in law(av, bv))
              + " | E = " + ", ".join(f"{x[1]:+.4f}" for x in law(av, bv))
              + f"   (pure baseline -(s-1)/2 = {-(s-1)/2:+.3f}, p/2 = {p/2:.3f})", flush=True)
        print(f"      {'':28s}tilt baseline -(s-1-theta_n)/2 = "
              + ", ".join(f"{-(s - 1 - dL(np.log(n))) / 2:+.4f}" for n in NS), flush=True)
    print(f"  [{time.time() - T0:.0f}s]", flush=True)
print("  K-doubling: max |K=1e5 - K=2e5| over all nB, E entries above = "
      f"{max(np.abs(np.subtract(RES[(100000, s)], RES[(200000, s)])).max() for s in (1.5, 1.75, 2.0, 2.5)):.1e}", flush=True)

print("\n[2] Lemma CT: L^T L (from J(sigma_s)) vs J(sigma_{s+p}) computed directly; r_n = l_n/m_n", flush=True)
lab, W = model(200000)
for s in (1.5, 2.0):
    a, b = coeffs(lab, W, s); a2, b2 = coeffs(lab, W, s + p)
    l, m = cholesky(a, b); n = NMAX - 1
    at = l[:n] ** 2 + m[:n] ** 2; bt = m[:n] * l[1:n + 1]
    da = float(np.max(np.abs(at / a2[:n] - 1))); db = float(np.max(np.abs(bt / b2[:n] - 1)))
    r = l[:n] / m[:n]
    print(f"  s={s} -> s+p={s + p}: max rel diff diag {da:.1e}, offdiag {db:.1e} (j < {n})", flush=True)
    print("    r_n - 1 = " + ", ".join(f"{float(r[j] - 1):.3e}" for j in NS) + " | n(r_n - 1) = "
          + ", ".join(f"{float(j * (r[j] - 1)):.4f}" for j in NS), flush=True)
    print("    CT image law from Cholesky: nB~ = " + ", ".join(f"{float(j * (j ** p * bt[j - 1] / c - 1)):+.4f}" for j in NS)
          + " | E~ = " + ", ".join(f"{float(j * (at[j] / (2 * bt[j]) - 1)):+.4f}" for j in NS), flush=True)
# exact-arithmetic sanity check of the identity on a family with known coefficients (Laguerre, alpha -> alpha + 1)
print("  Laguerre sanity check (a_j = 2j+al+1, b_j = sqrt((j+1)(j+1+al))): L^T L vs Laguerre(al+1), j < 50:", end="", flush=True)
for al in (-0.5, 0.0, 1.3):
    j = np.arange(51, dtype=float); aL = 2 * j + al + 1; bL = np.sqrt((j + 1) * (j + 1 + al))
    l, m = cholesky(aL, bL); at = l[:50] ** 2 + m[:50] ** 2; bt = m[:50] * l[1:51]
    a1 = 2 * j[:50] + al + 2; b1 = np.sqrt((j[:50] + 1) * (j[:50] + 2 + al))
    print(f" al={al}: {max(np.abs(at - a1).max(), np.abs(bt - b1).max()):.1e};", end="", flush=True)
print(f"  [{time.time() - T0:.0f}s]", flush=True)

print("\n[3] precision check (K = 20000 with tail, s = 1.5, Psi): |ld - quad| in nB, E at n = 100, 200, 400", flush=True)
lab, W = model(20000)
vl = law(*coeffs(lab, W, 1.5, N=402), ns=(100, 200, 400)); vq = law(*coeffs(lab, W, 1.5, N=402, prec="q"), ns=(100, 200, 400))
print("  ld: " + ", ".join(f"{x[0]:+.6f}/{x[1]:+.6f}" for x in vl) + f" ; max|ld-q| = {np.abs(np.subtract(vl, vq)).max():.1e}",
      flush=True)

print("\n[4] no-tail comparison (atoms k <= 2e5 only), s = 1.5, Psi: nB, E (shows the tail is needed)", flush=True)
kk = np.arange(1, 200001, dtype=float)
x0 = law(*coeffs(kk, np.ones_like(kk), 1.5))
print("  nB = " + ", ".join(f"{x[0]:+.4f}" for x in x0) + " | E = " + ", ".join(f"{x[1]:+.4f}" for x in x0), flush=True)
print(f"[done {time.time() - T0:.0f}s]", flush=True)
