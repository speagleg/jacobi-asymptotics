"""Plan 45 (NUMERICAL; outline_B_sv.md WP2, numerics N1-N3). Everything here is NUMERICAL (finite n, finite K,
floating point); nothing is certified and nothing here is a proof.

Setting (PROOF.md §3.14): x_k = k^{-p}, v = k^{-s} (s = 2), Psi = exp(L(log k)) with
  "sqrt":  L = sqrt(log(k+e))           (theta_n := L'(log n) ~ 1/(2 sqrt(log n)))
  "th0.8": L = (log(k+e))^0.8           (theta_n ~ 0.8 (log n)^(-0.2))
path w(t) = v Psi^t, f := log Psi, g_n := f - f(n); eps_n := sup_{m>=n} delta_m(2) (Lemma L0; sup over n <= m <= 10^7).

Measure model.  Atoms k = 1..K exactly, plus (as in RH/checks/check_fine.py, Plan 10 Phase 0) a Gauss-Legendre
quadrature on log-panels of int_{K+1/2}^{T_END} t^{-s} Psi(t)^t delta_{t^{-p}} dt (Euler-Maclaurin/midpoint continuation
of the atom sum beyond K; the summand varies on k-scales >> 1 for k >> n, see the .out header).  Every row is repeated with
K and 2K (truncation check).  Coefficients: RKPW (csrc, long double; quad precision for the precision check).
mu_m(k) = w_k p_m(x_k)^2 by the orthonormal three-term recurrence in long double, evaluated only for k >= k0(m)
(head atoms are e^{-cm}-small, Lemma Sat_p+), validated against float64 Lanczos with full reorthogonalisation.

[N1] tilt law: dev_b := beta_n(vPsi)/beta_n(v) - 1, dev_a := A_n(vPsi)/A_n(v) - 1 at p = 1, 0.5 (and p = 2 with the tail,
     for comparison with Plan 44's truncated p = 2 rows); report n*dev/theta_n.  Pure-power 1/n prediction: Phase 0
     (RH/LOG.md, NUMERICAL fits) n^p b_n/c = 1 - (s-1)/(2n) + O(n^-2), a_n/(2b_n) = 1 + p/(2n) + O(n^-2); locally
     Psi ~ k^theta_n turns s into s - theta_n, so d1 moves by +theta_n/2 and e1 = p/2 is unchanged: both ratios -> 0.5.
     Index convention as in check_sv_general.py (B[j] = j^p sqrt(b2[j])/c, A[j] = (j+1)^p a[j]/(2c)); ratios only.
[N2] QL-b slope: T_M(n,t) := mu_n^{(t)}((Mn, inf)) for M = 2^j up to >> n^{2/p} (the hard-edge scale k ~ n^{1+2/p});
     local slopes d log T/d log M vs the arcsine F_p(M) ~ (1/pi) c^{-1/2} M^{-p/2} and vs -(s-1) (far tail
     mu_n(k) ~ w_k p_n(0)^2); crossover M_x := the M where the local slope is halfway, reported as M_x / n^{2/p}.
     Lambda_n along t in {0, 1/2, 1} (m in {n-1, n}, n <= k <= n^gamma, gamma = kappa + 1/2, tail included).
[N3] Route I' (commutator lemma CB): X := <1_A q_m, K_m(f q_m)>, A = (Mn, inf), f = g_n, m = n;
     R := |X|/mu_m(A); compare R with eps_n (1 + log M) (CB) and with mu_m(A)^{-1/2} (Cauchy-Schwarz scale).
     K_m(f q_m) = sum_{j<m} <q_j, f q_m> q_j computed by streaming the recurrence (two passes).  Cross-checks: Lanczos
     (float64, full reorthogonalisation, no tail, K = 20000) and the TV identity
     d/dt mu_m(A) = <f 1_A q_m, q_m> - 2X - <f q_m, q_m> mu_m(A) by a central finite difference in t.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan45/research/G1/checks/check_ql_numerics.py"""
import time
import numpy as np
from scipy.integrate import quad
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

T0 = time.time()
s = 2.0
CASES = {"sqrt": (lambda k: np.sqrt(np.log(k + np.e)), lambda tau: 0.5 / np.sqrt(tau)),
         "th0.8": (lambda k: np.log(k + np.e) ** 0.8, lambda tau: 0.8 * tau ** -0.2)}
T_END = 1e48


def eps_L0(L, n, mmax=10**7):
    m = np.arange(n, mmax + 1, dtype=float)
    return np.maximum(L(2 * m) - L(m), L(m) - L(np.ceil(m / 2))).max()


def model(p, K, L=None, t=1.0, tail=True, ratio=1.02, kq=8):
    """(k-label, x, w) with x strictly decreasing; k-label = k for atoms, quadrature node t for the tail."""
    kk = np.arange(1, K + 1, dtype=float)
    lab, W = kk, np.ones(K)
    if tail:
        e = np.arange(np.log(K + 0.5), np.log(T_END), np.log(ratio))
        g, gw = np.polynomial.legendre.leggauss(kq)
        U = np.concatenate([(a + b) / 2 + (b - a) / 2 * g for a, b in zip(e[:-1], e[1:])])
        Wt = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
        lab = np.concatenate([kk, np.exp(U)]); W = np.concatenate([W, Wt * np.exp(U)])
    lw = np.log(W) - s * np.log(lab) + (t * L(lab) if L is not None else 0.0)
    lw -= lw.max()
    return lab, lab ** -p, np.exp(lw)


def rkpw(x, w, N, prec="ld"):
    r = jacobi_coeffs(DiscreteMeasure(x, w), N, prec=prec)
    if prec == "q":
        return np.array([float(v) for v in r.a]), np.array([float(v) for v in r.b2])
    return np.asarray(r.a, np.longdouble), np.asarray(r.b2, np.longdouble)


def BA(a, b2, p):
    b = np.sqrt(np.asarray(b2, float)); a = np.asarray(a, float); c = c_p(p)
    return np.arange(len(b)) ** p * b / c, (np.arange(len(a)) + 1) ** p * a / (2 * c)


def rows(x, w, a, b2, keep, p, i0=0):
    """mu_m(k) = q_m(k)^2, q_m = sqrt(w) p_m(x) orthonormal, for m in keep, by the three-term recurrence on the atoms
    i >= i0, run simultaneously in long double and float64.  Head atoms (saturated region) make the forward recurrence
    unstable; for each m the start index i0(m) is chosen as the first atom above which the two precisions agree to 1e-9
    relative or 1e-14 absolute in every atom (the instability is the same in both, amplified from 1e-16 vs 1e-19).  Returns
    {m: (i0(m), mu_m on atoms i >= i0(m) (long double), max abs ld-float64 difference there)}.
    Only atoms outside the arcsine band (x m^p > 4c(p)) are tested for the start index."""
    out = {}
    with np.errstate(all="ignore"):
        Q = {}
        for dt in (np.longdouble, np.float64):
            X = np.asarray(x[i0:], dt); sw = np.sqrt(np.asarray(w[i0:], dt) / np.asarray(w, dt).sum())
            A = np.asarray(a, dt); B = np.sqrt(np.asarray(b2, dt)); P0 = np.zeros_like(X); P1 = sw.copy()
            for j in range(max(keep) + 1):
                if j in keep:
                    Q[(dt, j)] = P1 * P1
                P0, P1 = P1, ((X - A[j]) * P1 - (B[j - 1] if j else 0) * P0) / B[j]
        for m in keep:
            ml, md = Q[(np.longdouble, m)], Q[(np.float64, m)]
            sat = np.asarray(x[i0:], float) * m ** p > 4 * c_p(p)  # outside the arcsine band: where instability lives
            dd = np.abs(ml - md); bad = sat & ~((dd <= 1e-9 * ml) | (dd <= 1e-14))
            ib = np.nonzero(bad)[0]
            j0 = ib.max() + 1 if ib.size else 0
            out[m] = (i0 + j0, ml[j0:], float(np.nanmax(np.abs(ml[j0:] - md[j0:]))))
    return out


def kernel_X(x, w, a, b2, m, i0, f):
    """q_m and h := K_m(f q_m) = sum_{j<m} <q_j, f q_m> q_j on the atoms i >= i0 (long double, two recurrence passes).
    Also returns max_{j<m} |<q_j, q_m>| (orthogonality of the recurrence vectors on the retained atoms)."""
    X = np.asarray(x[i0:], np.longdouble); sw = np.sqrt(np.asarray(w[i0:], np.longdouble) / np.asarray(w, np.longdouble).sum())
    A = np.asarray(a, np.longdouble); B = np.sqrt(np.asarray(b2, np.longdouble)); F = np.asarray(f[i0:], np.longdouble)

    def run(cb):
        P0 = np.zeros_like(X); P1 = sw.copy()
        for j in range(m + 1):
            if cb(j, P1):
                return P1
            P0, P1 = P1, ((X - A[j]) * P1 - (B[j - 1] if j else 0) * P0) / B[j]
    qm = run(lambda j, P: j == m)
    fq = F * qm; h = np.zeros_like(X); orth = [0.0]

    def acc(j, P):
        if j == m:
            return True
        h[:] += (P @ fq) * P; orth[0] = max(orth[0], abs(float(P @ qm)))
        return False
    run(acc)
    return qm, h, orth[0]


def lanczos(x, w, m):
    Q = np.zeros((m + 1, len(x))); q = np.sqrt(w); Q[0] = q / np.linalg.norm(q); b = np.zeros(m + 1)
    for j in range(m):
        u = x * Q[j]; u -= (Q[j] @ u) * Q[j]
        if j:
            u -= b[j] * Q[j - 1]
        for _ in range(2):
            u -= Q[:j + 1].T @ (Q[:j + 1] @ u)
        b[j + 1] = np.linalg.norm(u); Q[j + 1] = u / b[j + 1]
    return Q


def F_p(p, M):
    return 2 / np.pi * np.arcsin(np.sqrt(np.minimum(1.0, M ** -p / (4 * c_p(p)))))


def el():
    return f"[{time.time() - T0:.0f}s]"


# ------------------------------------------------------------------------------------------------------------------
print("[0] eps_n (Lemma L0) and theta_n = L'(log n):", flush=True)
NS1 = (100, 200, 400, 800, 1600)
for name, (L, dL) in CASES.items():
    print(f"  {name}: eps_n = " + ", ".join(f"{eps_L0(L, n):.4f}" for n in NS1)
          + " | theta_n = " + ", ".join(f"{dL(np.log(n)):.4f}" for n in NS1) + "  (n = 100..1600)", flush=True)

print(f"\n[N1] tilt law with quadrature tail to {T_END:.0e}; prediction n*dev/theta_n -> 0.5 (both b and a) {el()}",
      flush=True)
N1RES = {}
for p in (1.0, 0.5, 2.0):
    for K in (100000, 200000):
        lab, x, w0 = model(p, K)
        a0, b20 = rkpw(x, w0, 1602); B0, A0 = BA(a0, b20, p)
        for name, (L, dL) in CASES.items():
            _, _, w1 = model(p, K, L, 1.0)
            a1, b21 = rkpw(x, w1, 1602); B1, A1 = BA(a1, b21, p)
            db = [B1[n] / B0[n] - 1 for n in NS1]; da = [A1[n] / A0[n] - 1 for n in NS1]
            N1RES[(p, K, name)] = [[n * d / dL(np.log(n)) for n, d in zip(NS1, dd)] for dd in (db, da)]
            print(f"  p={p} K={K} {name:5s}: dev_b " + ", ".join(f"{d:+.3e}" for d in db)
                  + " | n*dev_b/theta_n " + ", ".join(f"{n*d/dL(np.log(n)):.4f}" for n, d in zip(NS1, db))
                  + " | n*dev_a/theta_n " + ", ".join(f"{n*d/dL(np.log(n)):.4f}" for n, d in zip(NS1, da)), flush=True)
    print(f"  {el()}", flush=True)
print("  K-doubling: max |(K=100000) - (K=200000)| over all normalised N1 entries = "
      f"{max(np.abs(np.subtract(N1RES[(p, 100000, c)], N1RES[(p, 200000, c)])).max() for p in (1.0, 0.5, 2.0) for c in CASES):.1e}",
      flush=True)
print("  extrapolation (illustrative only): least-squares fit y_n = Y + B/tau + C/tau^2, tau = log n, n = 100..1600, "
      "K = 200000", flush=True)
for (p, K, name), (yb, ya) in N1RES.items():
    if K != 200000:
        continue
    tau = np.log(np.array(NS1, float)); Am = np.vstack([np.ones(5), 1 / tau, 1 / tau ** 2]).T
    fb = np.linalg.lstsq(Am, np.array(yb), rcond=None)[0]; fa = np.linalg.lstsq(Am, np.array(ya), rcond=None)[0]
    print(f"    p={p} {name:5s}: Y_b = {fb[0]:.3f} (B = {fb[1]:+.3f}), Y_a = {fa[0]:.3f} (B = {fa[1]:+.3f})", flush=True)
# precision check: quad vs long double on the same measure (K = 20000 with tail), n <= 400
print("  precision check (K=20000 with tail, n = 100, 200, 400): |ld - q| in n*dev_b/theta_n and n*dev_a/theta_n",
      flush=True)
NSq = (100, 200, 400)
for p in (1.0, 0.5):
    L, dL = CASES["sqrt"]
    lab, x, w0 = model(p, 20000); _, _, w1 = model(p, 20000, L, 1.0)
    vals = {}
    for prec in ("ld", "q"):
        B0, A0 = BA(*rkpw(x, w0, 402, prec), p); B1, A1 = BA(*rkpw(x, w1, 402, prec), p)
        vals[prec] = np.array([[n * (B1[n] / B0[n] - 1) / dL(np.log(n)), n * (A1[n] / A0[n] - 1) / dL(np.log(n))]
                               for n in NSq])
    print(f"    p={p} sqrt: ld " + ", ".join(f"{v[0]:.6f}/{v[1]:.6f}" for v in vals["ld"])
          + f" ; max|ld-q| = {np.abs(vals['ld'] - vals['q']).max():.1e}", flush=True)
# tilt comparison (as outline B2(a)): pure power with s - theta_n in place of s, same tail model
print("  tilt comparison (K=100000 with tail, sqrt): dev_tilt := beta_n(k^-(s-theta_n))/beta_n(v) - 1; "
      "n*dev_tilt/theta_n and dev_w/dev_tilt (n = 100..1600)", flush=True)
for p in (1.0, 0.5, 2.0):
    L, dL = CASES["sqrt"]
    lab, x, w0 = model(p, 100000); _, _, w1 = model(p, 100000, L, 1.0)
    B0, _ = BA(*rkpw(x, w0, 1602), p); B1, _ = BA(*rkpw(x, w1, 1602), p); rt, rw = [], []
    for n in NS1:
        th = dL(np.log(n)); lw = np.log(w0) + th * np.log(lab)
        Bt, _ = BA(*rkpw(x, np.exp(lw - lw.max()), n + 2), p)
        rt.append(n * (Bt[n] / B0[n] - 1) / th); rw.append((B1[n] / B0[n] - 1) / (Bt[n] / B0[n] - 1))
    print(f"    p={p}: n*dev_tilt/theta_n = " + ", ".join(f"{v:.4f}" for v in rt)
          + " | dev_w/dev_tilt = " + ", ".join(f"{v:.4f}" for v in rw), flush=True)
# tail vs no tail (illustrates why the tail is needed at small p)
print("  no-tail comparison (K=200000, atoms only), sqrt: n*dev_b/theta_n", flush=True)
for p in (1.0, 0.5):
    L, dL = CASES["sqrt"]
    lab, x, w0 = model(p, 200000, tail=False); _, _, w1 = model(p, 200000, L, 1.0, tail=False)
    B0, _ = BA(*rkpw(x, w0, 1602), p); B1, _ = BA(*rkpw(x, w1, 1602), p)
    print(f"    p={p}: " + ", ".join(f"{n*(B1[n]/B0[n]-1)/dL(np.log(n)):.4f}" for n in NS1), flush=True)


# ------------------------------------------------------------------------------------------------------------------
print(f"\n[V] validation of the recurrence mu_m(k) (atoms above the adaptive start i0(m)) against float64 Lanczos with "
      f"full reorthogonalisation (no tail, K = 20000, sqrt, t = 1) {el()}", flush=True)
for p in (2.0, 1.0, 0.5):
    L = CASES["sqrt"][0]
    lab, x, w = model(p, 20000, L, 1.0, tail=False)
    Q = lanczos(x, w, 200); a, b2 = rkpw(x, w, 202)
    R = rows(x, w, a, b2, (100, 200), p)
    for m in (100, 200):
        i0, mu, dd = R[m]
        print(f"  p={p} m={m}: start k0 = {i0+1} (= {(i0+1)/m:.3f} m; band edge {(4*c_p(p))**(-1/p):.3f} m) "
              f"max|mu_rec - mu_Lanczos| = {np.abs(np.asarray(mu, float) - Q[m][i0:]**2).max():.1e}  "
              f"Lanczos mass below k0 = {(Q[m][:i0]**2).sum():.1e}  1 - sum mu_rec = {float(1 - mu.sum()):+.1e}", flush=True)

# ------------------------------------------------------------------------------------------------------------------
NS2 = (25, 50, 100, 200, 400)
NL = (100, 200, 400, 800, 1600)
MJ = 4.0 ** np.arange(0, 21)  # M = 1, 4, ..., 4^20 ~ 1.1e12
GAM = {2.0: 6.5, 1.0: 8.5, 0.5: 12.5}  # gamma = kappa + 1/2, kappa = (2 + 2/p) s/(s - 1)
print(f"\n[N2] tail masses T_M = mu_n^(t)((Mn, inf)), M = 4^j (j = 0..20), sqrt; local slope sl_j := "
      f"log(T_(j+1)/T_j)/log 4; arcsine slope -p/2, far-tail slope -(s-1) = -1 {el()}", flush=True)
L = CASES["sqrt"][0]
N2RES, LAM = {}, {}
for p in (2.0, 1.0, 0.5):
    for t in (0.0, 0.5, 1.0):
        for K in ((100000, 200000) if t != 0.5 else (100000,)):
            lab, x, w = model(p, K, L, t)
            a, b2 = rkpw(x, w, max(NL) + 2)
            keep = sorted({m for n in NL for m in (n - 1, n)} | set(NS2))
            R = rows(x, w, a, b2, keep, p)
            if t != 0.5:
                for n in NS2:
                    i0, mu, _ = R[n]; lb = lab[i0:]
                    T = np.array([float(mu[lb > M * n].sum()) for M in MJ])
                    N2RES[(p, t, K, n)] = T
            for n in NL:
                hi = n ** GAM[p]
                lam = max(float((R[m][1] * np.log(np.maximum(lab[R[m][0]:], n) / n) * (lab[R[m][0]:] <= hi)).sum())
                          for m in (n - 1, n))
                LAM[(p, t, K, n)] = lam
            print(f"  computed p={p} t={t} K={K}: max ld-float64 |dmu| on retained atoms = "
                  f"{max(R[m][2] for m in keep):.1e}; 1 - sum mu (max over kept m) = "
                  f"{max(abs(float(1 - R[m][1].sum())) for m in keep):.1e} {el()}", flush=True)
    print(f"  p={p}: arcsine F_p(M) M^(p/2) -> (1/pi) c^(-1/2) = {1/np.pi/np.sqrt(c_p(p)):.4f}; hard-edge scale "
          f"M ~ n^(2/p)", flush=True)
    for t in (0.0, 1.0):
        for n in NS2:
            T = N2RES[(p, t, 200000, n)]; T1 = N2RES[(p, t, 100000, n)]
            ok = T > 1e-280
            sl = np.log(T[1:] / T[:-1]) / np.log(4.0)
            kd = np.nanmax(np.abs(T1[ok] / T[ok] - 1))
            # crossover: first M where the local slope is below the midpoint between -p/2 and -(s-1)
            mid = 0.5 * (-p / 2 - (s - 1))
            jx = np.nonzero(sl < mid - 1e-9)[0] if p != 2.0 else np.array([])
            xs = (f"M_x ~ {np.sqrt(MJ[jx[0]]*MJ[jx[0]+1]):.1e} = {np.sqrt(MJ[jx[0]]*MJ[jx[0]+1])/n**(2/p):.2f} n^(2/p)"
                  if jx.size else ("no crossover (slopes coincide at p = 2, s = 2)" if p == 2.0 else "none in range"))
            print(f"   p={p} t={t} n={n:3d}: T_M/F_p(M) at M=4,16,64,256: "
                  + ", ".join(f"{T[j]/F_p(p, MJ[j]):.3f}" for j in (1, 2, 3, 4))
                  + " | sl_j (j=0..19): " + " ".join(f"{v:+.2f}" for v in sl)
                  + f" | T(4^20) = {T[-1]:.2e} | {xs} | K-doubling max rel diff {kd:.1e}", flush=True)
    al = min(p / 2, 0.8)
    print(f"   p={p}: QL-b constant C_n(alpha) := max_(1<=M<=4^20) T_M M^alpha, alpha = {al}: "
          + "; ".join(f"t={t}: " + ", ".join(f"{(N2RES[(p, t, 200000, n)] * MJ ** al).max():.3f}" for n in NS2)
                      for t in (0.0, 1.0)) + "  (n = 25..400)", flush=True)
    for t in (0.0, 1.0):
        n = 25; T = N2RES[(p, t, 200000, n)]
        js = np.arange(4, 15)
        fit = np.polyfit(np.log(MJ[js]), np.log(T[js]), 1)[0]
        print(f"   p={p} t={t} n=25: least-squares slope over M = 4^4..4^14: {fit:+.3f}", flush=True)
print(f"\n[N2'] QL log-moment Lambda_n(t) = max_(m in {{n-1,n}}) sum_(n <= k <= n^gamma) log(k/n) mu_m^(t)(k), "
      f"gamma = kappa + 1/2, tail included, sqrt {el()}", flush=True)
LPc = {}
for p in (2.0, 1.0, 0.5):
    with np.errstate(over="ignore"):
        LPc[p] = quad(lambda u: F_p(p, np.exp(u)), 0, 1500.0, limit=500)[0]  # F_p(e^u) < e^(-p u/2): rest negligible
    sup = [max(LAM[(p, t, 100000, n)] for t in (0.0, 0.5, 1.0)) for n in NL]
    for t in (0.0, 0.5, 1.0):
        print(f"  p={p} t={t}: Lambda_n = " + ", ".join(f"{LAM[(p, t, 100000, n)]:.4f}" for n in NL)
              + (" | K=200000: " + ", ".join(f"{LAM[(p, t, 200000, n)]:.4f}" for n in NL) if t != 0.5 else ""),
              flush=True)
    print(f"  p={p}: sup_t Lambda_n = " + ", ".join(f"{v:.4f}" for v in sup)
          + f" | LP constant int_0^inf F_p(e^u) du = {LPc[p]:.4f} | eps_n sup_t Lambda_n = "
          + ", ".join(f"{eps_L0(L, n)*v:.4f}" for n, v in zip(NL, sup)) + " (n = 100..1600)", flush=True)

# ------------------------------------------------------------------------------------------------------------------
NS3 = (50, 100, 200, 400)
ME = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25, 29])
M3 = 2.0 ** ME
print(f"\n[N3] Route I': X = <1_A q_m, K_m(f q_m)>, A = (Mn, inf), f = g_n = log Psi - log Psi(n) (sqrt), m = n; "
      f"R = |X|/mu_m(A); CB scale eps_n(1 + log M); Cauchy-Schwarz scale mu_m(A)^(-1/2) {el()}", flush=True)
L = CASES["sqrt"][0]


def X_of(lab, mu_q, h, n, Ms):
    return np.array([float((mu_q * h)[lab > M * n].sum()) for M in Ms])


# cross-check (a): Lanczos on the truncated measure (no tail), p = 2, t = 1, K = 20000, n = 100
lab, x, w = model(2.0, 20000, L, 1.0, tail=False)
Q = lanczos(x, w, 100); a, b2 = rkpw(x, w, 102); f = L(lab) - L(100.0)
hL = Q[:100].T @ (Q[:100] @ (f * Q[100]))
i0 = rows(x, w, a, b2, (100,), 2.0)[100][0]
qm, h, orth = kernel_X(x, w, a, b2, 100, i0, f)
Mc = 2.0 ** np.arange(1, 8)  # Mn < K
XL = np.array([(Q[100] * hL)[lab > M * 100].sum() for M in Mc]); XR = X_of(lab[i0:], qm, h, 100, Mc)
muA = np.array([(Q[100] ** 2)[lab > M * 100].sum() for M in Mc])
print("  check (a) p=2 t=1 n=100 K=20000 no tail: M = 2..2^7: |X_rec/X_Lanczos - 1| max = "
      f"{np.abs(XR / XL - 1).max():.1e}; mu(A) range {muA.min():.1e}..{muA.max():.1e}; max_(j<m)|<q_j,q_m>| = {orth:.1e}",
      flush=True)

R3 = {}
for p in (2.0, 1.0, 0.5):
    for t in (0.0, 0.5, 1.0):
        for K in ((100000, 200000) if (p == 2.0 and t == 1.0) else (100000,)):
            lab, x, w = model(p, K, L, t)
            a, b2 = rkpw(x, w, max(NS3) + 2)
            st = rows(x, w, a, b2, NS3, p)
            for n in NS3:
                i0 = st[n][0]; f = L(lab) - L(float(n))
                qm, h, orth = kernel_X(x, w, a, b2, n, i0, f)
                lb = lab[i0:]; mu = qm * qm
                X = X_of(lb, qm, h, n, M3)
                muA = np.array([float(mu[lb > M * n].sum()) for M in M3])
                fA = np.array([float((mu * f[i0:])[lb > M * n].sum()) for M in M3]) / muA
                R3[(p, t, K, n)] = (np.abs(X) / muA, muA, fA, orth, X)
        e = {n: eps_L0(L, n) for n in NS3}
        for n in NS3:
            R, muA, fA, orth, X = R3[(p, t, 100000, n)]
            print(f"  p={p} t={t} n={n:3d} (eps_n={e[n]:.3f}, max|<q_j,q_m>|={orth:.0e}): M=2^"
                  + ",".join(str(v) for v in ME) + f"\n    mu(A)     " + " ".join(f"{v:.1e}" for v in muA)
                  + f"\n    R         " + " ".join(f"{v:.1e}" for v in R)
                  + f"\n    R/(eps(1+logM)) " + " ".join(f"{v:.3f}" for v in R / (e[n] * (1 + np.log(M3))))
                  + f"\n    R*sqrt(mu(A))   " + " ".join(f"{v:.1e}" for v in R * np.sqrt(muA))
                  + f"\n    mean_A f / (eps(1+logM)) " + " ".join(f"{v:.3f}" for v in fA / (e[n] * (1 + np.log(M3))))
                  + f"\n    sign(X)   " + "".join("+" if v > 0 else "-" for v in X), flush=True)
        Rall = [R3[(p, t, 100000, n)] for n in NS3]
        cb = max((r[0] / (e[n] * (1 + np.log(M3)))).max() for n, r in zip(NS3, Rall))
        cs = [np.polyfit(np.log(1 / r[1][-5:]), np.log(r[0][-5:]), 1)[0] for r in Rall]
        print(f"  SUMMARY p={p} t={t}: max_(n,M) R/(eps_n(1+log M)) = {cb:.3f}; d log R / d log(1/mu(A)) over the 5 "
              f"deepest M (0: R bounded; 1/2: Cauchy-Schwarz scale) = " + ", ".join(f"{v:+.3f}" for v in cs)
              + "; R(2^29)/(eps_n log n) = " + ", ".join(f"{r[0][-1]/(e[n]*np.log(n)):.3f}" for n, r in zip(NS3, Rall))
              + f" (n = {NS3}) {el()}", flush=True)
R, _, _, _, _ = R3[(2.0, 1.0, 100000, 100)]; R2, _, _, _, _ = R3[(2.0, 1.0, 200000, 100)]
print(f"  K-doubling (p=2, t=1, n=100): max_M |R(K)/R(2K) - 1| = {np.abs(R / R2 - 1).max():.1e}; "
      f"all n: {max(np.abs(R3[(2.0, 1.0, 100000, n)][0] / R3[(2.0, 1.0, 200000, n)][0] - 1).max() for n in NS3):.1e}",
      flush=True)
# cross-check (b): the TV identity by a central difference in t (t = 1/2, n = 100, K = 100000, with tail),
# at p = 2 and (Plan 45 Rule R, F9) at p = 1/2 and p = 1, where the largest N3 ratios occur
for pb in (2.0, 0.5, 1.0):
    n, t0, dh = 100, 0.5, 1e-3
    lab, x, w = model(pb, 100000, L, t0); f = L(lab) - L(float(n))
    a, b2 = rkpw(x, w, n + 2); i0 = rows(x, w, a, b2, (n,), pb)[n][0]
    qm, h, _ = kernel_X(x, w, a, b2, n, i0, f); lb = lab[i0:]; mu = qm * qm; fm = float((mu * f[i0:]).sum())
    Mb = 2.0 ** np.array([1, 5, 9, 13, 17, 21, 25, 29])
    muP = {}
    for sg in (+1, -1):
        _, _, ws = model(pb, 100000, L, t0 + sg * dh); aa, bb = rkpw(x, ws, n + 2); st = rows(x, ws, aa, bb, (n,), pb)[n]
        muP[sg] = np.array([float(st[1][lab[st[0]:] > M * n].sum()) for M in Mb])
    out = []
    for i, M in enumerate(Mb):
        A_ = lb > M * n; muA = float(mu[A_].sum())
        XF = 0.5 * (float((mu * f[i0:])[A_].sum()) - fm * muA - (muP[1][i] - muP[-1][i]) / (2 * dh))
        XD = float((qm * h)[A_].sum())
        out.append(f"M=2^{int(np.log2(M))}: X={XD:+.4e} X_FD={XF:+.4e}")
    print(f"  check (b) TV identity by central difference (p={pb}, t=1/2, n=100, h=1e-3): " + "; ".join(out), flush=True)
print(f"\ndone {el()}", flush=True)
