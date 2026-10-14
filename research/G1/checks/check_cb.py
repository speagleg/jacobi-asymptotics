"""Plan 49 (G1 PROOF.md §3.18): numerical checks for the commutator lemma CB (Route I' of outline_B_sv.md §5).
Everything printed here is NUMERICAL (finite n, finite measure model, float64); nothing is certified, nothing is a proof.

Setting (§3.14): x_k = k^-p, v = k^-s (s = 2), Psi = exp(L(log k)), L(tau) = sqrt(tau) evaluated as sqrt(log(k+e)),
path w(t) = v Psi^t, g := g_n = log Psi - log Psi(n), eps_n of Lemma L0, theta_n := L'(log n) = 1/(2 sqrt(log n)).
A_M := (Mn, inf), y_M := mu_m(A_M), X_M := <1_A q_m, K_m(g q_m)>, m = n.

Measure model: atoms k = 1..K exactly, plus a Gauss-Legendre quadrature on log-panels of
int_{K+1/2}^{T_END} u^-s Psi(u)^t delta_{u^-p} du (as in Plan 45); all identities below are exact for this discrete
measure, and the checks are about it.  q_0..q_{m+1} by float64 Lanczos with full reorthogonalisation (validated against
the recurrence in Plan 45 to <= 4e-15).

[1] Lemma BF (exact identities), small model (K = 3000, no tail): (i) X_A = sum_{k in A, l notin A} q(k)K_m(k,l)q(l)(g(l)-g(k));
    (ii) d/dt mu_m(A) = sum_{A x A^c} q(k)(K_m+K_{m+1})(k,l)q(l)(g(k)-g(l)) vs a central finite difference in t;
    (iii) Lemma RF: X_A = sum_{k in A} mu_m(k) R_m(x_k), R_m := P_m/p_m, P_m := sum_{j<m} <g q_m, q_j> p_j.
[2] Free model (Proposition FM): sum_{d>=1} hhat(d) Fhat(d) = (eps/(pi p)) Cl_2(phi) and Cov = 2X (transport defect 0),
    by direct summation / quadrature.
[3] Main table (p = 2 discriminates best, p = 1 moderately; p = 1/2 cannot separate the CB scale from the CS scale on
    accessible windows -- REVIEW_Plan45.md -- and is omitted): for n in {50, 100, 200}, t in {0, 1/2, 1}, M = 2^j:
    R := X/y, R/(eps(1+log M)); free-model prediction R_FM := (theta/p) Cl_2(phi)/phi, 1 - cos phi = M^-p/(2c(p))
    (arcsine range only); transport defect T := Cov(g,1_A) - 2X = d/dt y, T/(eps y (1+log M)); the Cauchy-Schwarz
    scale ratio X/(sqrt(y) ||g q_m||).
[4] Lemma DB efficiency: blocks B_i = {d = m-j in [2^i, 2^{i+1})}; a_i := ||(E_{m,m-d})_{d in B_i}||,
    e_i := ||(G_{m-d,m})_{d in B_i}||, DB := sum_i a_i e_i >= |X|; report DB/|X|, and the two block hypotheses (OD) of Lemma DB(d):
    OD_E := max_i a_i/min(2^{i/2} y, 2^{-i/2}) and OD_F := max_i e_i 2^{i/2}/eps (bounded <=> (OD) with those constants).
[5] Deep-tail structure (review of Plan 45): beyond the hard edge, X/y -> R_m(0) = P_m(0)/p_m(0); report R_m at the
    deepest node and X/y at the deepest M, and |R_m(0)|/(eps log n).
[6] Moments Y_alpha := sum_k max(1,k/n)^alpha mu_m(k) along the path (Theorem QL-CB's quantity): Y_alpha(t)/Y_alpha(0).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan49/research/G1/checks/check_cb.py"""
import time
import numpy as np
import mpmath as mp
from jacobi_asym.laws.weyl import c_p

T0 = time.time()
s = 2.0
L = lambda k: np.sqrt(np.log(k + np.e))
dL = lambda tau: 0.5 / np.sqrt(tau)
T_END = 1e16


def el():
    return f"[{time.time() - T0:.0f}s]"


def eps_L0(n, mmax=10**7):
    m = np.arange(n, mmax + 1, dtype=float)
    return np.maximum(L(2 * m) - L(m), L(m) - L(np.ceil(m / 2))).max()


def model(p, K, t, tail=True, ratio=1.05, kq=4):
    kk = np.arange(1, K + 1, dtype=float); lab, W = kk, np.ones(K)
    if tail:
        e = np.arange(np.log(K + 0.5), np.log(T_END), np.log(ratio))
        g, gw = np.polynomial.legendre.leggauss(kq)
        U = np.concatenate([(a + b) / 2 + (b - a) / 2 * g for a, b in zip(e[:-1], e[1:])])
        Wt = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
        lab = np.concatenate([kk, np.exp(U)]); W = np.concatenate([W, Wt * np.exp(U)])
    lw = np.log(W) - s * np.log(lab) + t * L(lab)
    lw -= lw.max()
    return lab, lab ** -p, np.exp(lw)


def lanczos(x, w, m):
    Q = np.zeros((m + 1, len(x))); q = np.sqrt(w); Q[0] = q / np.linalg.norm(q); a = np.zeros(m + 1); b = np.zeros(m + 1)
    for j in range(m):
        u = x * Q[j]; a[j] = Q[j] @ u; u -= a[j] * Q[j]
        if j:
            u -= b[j] * Q[j - 1]
        for _ in range(2):
            u -= Q[:j + 1].T @ (Q[:j + 1] @ u)
        b[j + 1] = np.linalg.norm(u); Q[j + 1] = u / b[j + 1]
    a[m] = Q[m] @ (x * Q[m])
    return Q, a, b


def cl2(phi):
    return float(mp.clsin(2, phi))


# ---------------------------------------------------------------------------------------------------------------
print("[1] Lemma BF / RF identities (K = 3000, no tail, p = 2, n = m = 30, t = 1/2)", flush=True)
p, K, n = 2.0, 3000, 30
lab, x, w = model(p, K, 0.5, tail=False)
g = L(lab) - L(n)
Q, a, b = lanczos(x, w, n + 1); qm = Q[n]; Km = Q[:n].T @ Q[:n]; Km1 = Km + np.outer(qm, qm)
Kg = Km @ (g * qm)
for M in (1.5, 3.0, 8.0):
    A = lab > M * n; Ac = ~A
    X = (A * qm) @ Kg
    Xbf = (qm[A] @ (Km[np.ix_(A, Ac)] * (g[Ac][None, :] - g[A][:, None])) @ qm[Ac])
    Tbf = (qm[A] @ ((Km + Km1)[np.ix_(A, Ac)] * (g[A][:, None] - g[Ac][None, :])) @ qm[Ac])
    h = 1e-4
    ys = []
    for tt in (0.5 - h, 0.5 + h):
        _, _, ww = model(p, K, tt, tail=False); QQ, _, _ = lanczos(x, ww, n + 1); ys.append(QQ[n][A] @ QQ[n][A])
    fd = (ys[1] - ys[0]) / (2 * h)
    # Lemma RF: R_m = (K_m(g q_m))/q_m on atoms (P_m/p_m), X = sum_A mu R
    Xrf = np.sum((qm[A] ** 2) * (Kg[A] / qm[A]))
    tv = (g * A) @ qm ** 2 - (g @ qm ** 2) * (qm[A] @ qm[A]) - 2 * X
    print(f"  M={M:4.1f}: X = {X:+.10e}, BF(i) = {Xbf:+.10e}, RF = {Xrf:+.10e} | d/dt y: TV = {tv:+.8e}, "
          f"BF(ii) = {Tbf:+.8e}, finite diff = {fd:+.8e}", flush=True)

print(f"\n[2] Free model (Proposition FM): S(phi) := sum_d hhat(d)Fhat(d) (eps = p = 1) vs Cl_2(phi)/pi; "
      f"Cov(F,1_A) vs 2S (quadrature) {el()}", flush=True)
for phi in (0.5, 0.1, 0.01):
    d = np.arange(1, 2_000_001, dtype=float)
    S = np.sum((-1) ** d * np.sin(d * phi) / (np.pi * d) * (-1) ** d / d)
    F = lambda th: -2 * mp.log(abs(mp.cos(th / 2)))
    meanA = mp.quad(F, [mp.pi - phi, mp.pi, mp.pi + phi]) / (2 * phi); mean = mp.quad(F, [0, mp.pi, 2 * mp.pi]) / (2 * mp.pi)
    cov = (phi / mp.pi) * (meanA - mean)
    print(f"  phi={phi}: S = {S:.10f}, Cl2/pi = {cl2(phi) / np.pi:.10f}, Cov = {float(cov):.10f}, 2S = {2 * S:.10f}, "
          f"S/mu(A) = {S / (phi / np.pi):.6f}, 1 + log(1/phi) = {1 + np.log(1 / phi):.6f}", flush=True)

# ---------------------------------------------------------------------------------------------------------------
print(f"\n[3]-[6] main table {el()}", flush=True)
SUMMARY = {}
for p, NS, Kat in ((2.0, (50, 100, 200, 400), 60000), (1.0, (50, 100, 200), 60000)):
    c = c_p(p)
    for n in NS:
        eps = eps_L0(n); th = dL(np.log(n)); m = n
        print(f"\n p={p} n={n} K={Kat}+tail: eps_n = {eps:.4f}, theta_n = {th:.4f}, hard-edge scale n^(2/p) = "
              f"{n ** (2 / p):.0f}", flush=True)
        Ymom = {}
        for t in (0.0, 0.5, 1.0):
            lab, x, w = model(p, Kat, t)
            g = L(lab) - L(n)
            Q, a, b = lanczos(x, w, m + 1)
            qm = Q[m]; mu = qm ** 2
            G = Q[:m] @ (g * qm)                      # G_j = <q_j, g q_m>, j < m
            Kg = Q[:m].T @ G                          # K_m(g q_m) = sqrt(w) P_m
            gnorm = np.sqrt(mu @ g ** 2); gbar = mu @ g
            print(f"  t={t}: ||g q_m|| = {gnorm:.4f}, <g,mu_m> = {gbar:+.4f}, mu_m beyond last exact atom = "
                  f"{mu[lab > Kat].sum():.2e} {el()}", flush=True)
            print("     M        y_M      R=X/y   R/(eps(1+logM))  R/R_FM   T/(eps y(1+logM))  X/(sqrt(y)||gq||)"
                  "   DB/|X|   OD_E   OD_F", flush=True)
            rows = []
            for j in range(1, 60):
                M = 2.0 ** j
                A = lab > M * n
                y = mu[A].sum()
                if y < 1e-11 or not A.any():
                    break
                E = Q[:m, A] @ qm[A]                  # E_{m,j} = <1_A q_m, q_j>
                X = E @ G
                cov = (g * A) @ mu - gbar * y; T = cov - 2 * X
                R = X / y
                cosv = 1 - M ** -p / (2 * c)
                RFM = th / p * cl2(np.arccos(cosv)) / np.arccos(cosv) if M ** -p < 4 * c else np.nan
                # DB blocks (d = m - j)
                DB, ODE, ODF, i = 0.0, 0.0, 0.0, 0
                while 2 ** i <= m:
                    d = np.arange(2 ** i, min(2 ** (i + 1), m + 1)); jj = m - d
                    ai = np.linalg.norm(E[jj]); ei = np.linalg.norm(G[jj])
                    DB += ai * ei
                    ODE = max(ODE, ai / min(2 ** (i / 2) * y, 2 ** (-i / 2)))
                    ODF = max(ODF, ei * 2 ** (i / 2) / eps)
                    i += 1
                rows.append((M, y, R, R / (eps * (1 + np.log(M))), T / (eps * y * (1 + np.log(M))), X / (np.sqrt(y) * gnorm), DB / abs(X), ODE, ODF))
                if j % 2 == 1 or y < 1e-9:
                    print(f"  {M:9.3g}  {y:.3e}  {R:+.4f}   {R / (eps * (1 + np.log(M))):+.4f}        "
                          f"{R / RFM if RFM == RFM else float('nan'):6.3f}   {T / (eps * y * (1 + np.log(M))):+.4f}"
                          f"            {X / (np.sqrt(y) * gnorm):+.4f}           {DB / abs(X):6.2f}  {ODE:5.2f}  {ODF:5.2f}",
                          flush=True)
            rows = np.array(rows)
            SUMMARY[(p, n, t)] = (np.abs(rows[:, 3]).max(), np.abs(rows[:, 4]).max(), rows[:, 6].max(),
                                  np.abs(rows[:, 5]).max(), rows[:, 7].max(), rows[:, 8].max())
            # [5] deep-tail: R_m at the deepest node vs X/y at the deepest M
            kd = np.argmin(x); Rdeep = Kg[kd] / qm[kd]
            print(f"   [5] R_m(deepest node, x={x[kd]:.1e}) = {Rdeep:+.5f}; X/y at deepest M = {rows[-1, 2]:+.5f}; "
                  f"|R_m(0)|/(eps log n) = {abs(Rdeep) / (eps * np.log(n)):.3f}", flush=True)
            # [6] moments
            r = np.maximum(1.0, lab / n)
            Ymom[t] = [mu @ r ** al for al in (0.25 * p / 2, 0.5 * p / 2, 0.75 * p / 2)]
        print("   [6] Y_alpha(t)/Y_alpha(0), alpha = (1/4, 1/2, 3/4)*(p/2): t=1/2: "
              + ", ".join(f"{u / v:.4f}" for u, v in zip(Ymom[0.5], Ymom[0.0])) + "; t=1: "
              + ", ".join(f"{u / v:.4f}" for u, v in zip(Ymom[1.0], Ymom[0.0]))
              + "; Y_alpha(0) = " + ", ".join(f"{v:.4f}" for v in Ymom[0.0]), flush=True)

print(f"\n[summary] per (p, n): max over t, M of |R|/(eps(1+log M)), |T|/(eps y(1+log M)), DB/|X|, "
      f"|X|/(sqrt(y)||gq||), OD_E, OD_F {el()}", flush=True)
for p in (2.0, 1.0):
    for n in (50, 100, 200, 400):
        if (p, n, 0.0) not in SUMMARY:
            continue
        v = np.array([SUMMARY[(p, n, t)] for t in (0.0, 0.5, 1.0)]).max(axis=0)
        print(f"  p={p} n={n}: {v[0]:.3f}  {v[1]:.3f}  {v[2]:.2f}  {v[3]:.3f}  {v[4]:.2f}  {v[5]:.2f}", flush=True)
print(f"done {el()}")
