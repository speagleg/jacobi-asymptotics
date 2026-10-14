"""Plan 44 (NUMERICAL): slowly varying weights with D(gamma) = infinity, p = s = 2 only.
Psi = exp(L(log k)) with L(tau) = sqrt(log(k+e)) ("sqrt") and log(k+e)^0.8 ("th0.8").
theta_n := L'(log n) (the local tilt; 1/(2 sqrt(log n)) resp. 0.8 (log n)^(-0.2)).
eps_n := sup_{m>=n} delta_m(2) is the constant of Lemma L0 (PROOF.md §3.14); for these increasing,
log-concave-in-log-k L, delta_m(2) = max(L(2m)-L(m), L(m)-L(ceil(m/2))), and the sup is taken over n <= m <= 10^7.

[1] long double RKPW, K = 120000 | 240000 (truncation check), plus quad precision at K = 120000 (precision check):
    dev_b := beta_n(vPsi)/beta_n(v) - 1, dev_a := A_n(vPsi)/A_n(v) - 1 (A_n := (n+1)^p a_n/(2c), 0-based a index as in
    check_log_weights.py), and the normalised n*dev/theta_n (tilt prediction: 0.5).
[2] mu_m^{(t)}(k) for k >= n/2 by the three-term recurrence (long double) from RKPW coefficients, validated against float64
    Lanczos with full reorthogonalisation at K = 20000, n = 100; then K = 120000 | 480000:
    the QL log-moment Lambda_n(t) := max_{m in {n-1,n}} sum_{n<=k<=min(n^gamma,K)} log(k/n) mu_m^{(t)}(k) along the path
    w(t) = v Psi^t, t in {0, 1/4, 1/2, 3/4, 1}; its sup over the t-grid; eps_n * sup_t Lambda_n; and mu_n^{(t)}((Mn, K]).
    The range n^gamma (gamma > kappa = 6 for p = s = 2) far exceeds K, so [2] sees only k <= K (truncated; illustrative).
Why the quad-precision rows stop at n = 400: cost.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan44/research/G1/checks/check_sv_general.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

p, s = 2.0, 2.0
CASES = {"sqrt": (lambda k: np.sqrt(np.log(k + np.e)), lambda tau: 0.5 / np.sqrt(tau)),
         "th0.8": (lambda k: np.log(k + np.e) ** 0.8, lambda tau: 0.8 * tau ** -0.2)}


def eps_L0(L, n, mmax=10**7):
    m = np.arange(n, mmax + 1, dtype=float)
    d = np.maximum(L(2 * m) - L(m), L(m) - L(np.ceil(m / 2)))
    return d.max()


def coeffs(K, L, N, prec):
    k = np.arange(1, K + 1, dtype=float)
    lw = -s * np.log(k) + (L(k) if L is not None else 0.0)
    lw -= lw.max()  # rescaling the weight does not change (a_n, b_n)
    r = jacobi_coeffs(DiscreteMeasure(k ** -p, np.exp(lw)), N, prec=prec)
    b = np.sqrt(np.asarray(r.b2, float)); a = np.asarray(r.a, float)
    return np.arange(len(b)) ** p * b / c_p(p), (np.arange(len(a)) + 1) ** p * a / (2 * c_p(p))


NS = (100, 200, 400, 800, 1600)
print("[1] coefficient deviations; tilt prediction n*dev/theta_n -> 0.5", flush=True)
for name, (L, dL) in CASES.items():
    th = {n: dL(np.log(n)) for n in NS}
    print(f"  {name}: eps_n (L0) = " + ", ".join(f"{eps_L0(L, n):.4f}" for n in NS)
          + " ; eps_n/theta_n = " + ", ".join(f"{eps_L0(L, n)/th[n]:.3f}" for n in NS) + f"  (log 2 = {np.log(2):.3f})",
          flush=True)
for K, prec, N in ((120000, "ld", 1601), (240000, "ld", 1601), (120000, "q", 401)):
    B0, A0 = coeffs(K, None, N, prec)
    for name, (L, dL) in CASES.items():
        B1, A1 = coeffs(K, L, N, prec)
        ns = [n for n in NS if n < N]
        db = [B1[n] / B0[n] - 1 for n in ns]; da = [A1[n] / A0[n] - 1 for n in ns]
        print(f"  K={K} {prec:2s} {name:5s}: dev_b " + ", ".join(f"{d:+.3e}" for d in db)
              + " | n*dev_b/theta_n " + ", ".join(f"{n*d/dL(np.log(n)):.4f}" for n, d in zip(ns, db))
              + " | n*dev_a/theta_n " + ", ".join(f"{n*d/dL(np.log(n)):.4f}" for n, d in zip(ns, da)), flush=True)


def mu_rows(K, L, t, ms, prec="ld"):
    """mu_m(k) = w_k p_m(x_k)^2 for m in ms, by the three-term recurrence (long double) from the RKPW coefficients of the
    truncated measure. Indexing: a[j] = <x p_j, p_j>, b2[j] = b_{j+1}^2 couples p_j, p_{j+1}. The recurrence is evaluated
    pointwise in x_k; for k >= m (x_k <= m^{-p}, outside the saturated region k/m < (4c(p))^{-1/p}) it runs in the
    oscillatory region. Head atoms (k << m) may be inaccurate; they are not used. Validated against Lanczos below."""
    k = np.arange(1, K + 1, dtype=np.longdouble)
    lw = -s * np.log(k) + (t * L(k) if L is not None else 0.0); lw -= lw.max(); w = np.exp(lw)
    r = jacobi_coeffs(DiscreteMeasure(np.asarray(k ** -p, float), np.asarray(w, float)), max(ms) + 2, prec=prec)
    a = np.asarray(r.a, np.longdouble); b = np.sqrt(np.asarray(r.b2, np.longdouble)); x = k ** -p
    P0 = np.zeros_like(x); P1 = np.full_like(x, 1 / np.sqrt(w.sum())); out = {}
    with np.errstate(over="ignore", invalid="ignore"):  # head atoms may overflow; only k >= m/2 is used
        for j in range(max(ms) + 1):
            if j in ms:
                out[j] = np.asarray(w * P1 ** 2, float)
            P0, P1 = P1, ((x - a[j]) * P1 - (b[j - 1] if j else 0) * P0) / b[j]
    return out


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


GAMMA = 6.5  # any gamma > kappa = (2+2/p)s/(s-1) = 6 for p = s = 2
print("[2] QL log-moment along the path (sum truncated at k <= K since n^gamma >> K)", flush=True)
L = CASES["sqrt"][0]; Kv = 20000; kk = np.arange(1, Kv + 1, dtype=float)
lw = -s * np.log(kk) + L(kk); Q = lanczos(kk ** -p, np.exp(lw - lw.max()), 100); R = mu_rows(Kv, L, 1.0, (99, 100))
print("  validation (sqrt, t=1, K=20000): max_{k>=n/2} |mu_rec - mu_Lanczos| = "
      + ", ".join(f"m={m}: {np.abs(R[m][m//2:] - Q[m][m//2:]**2).max():.1e}" for m in (99, 100))
      + " ; sum_{k>=n/2} mu_rec = " + ", ".join(f"{R[m][m//2:].sum():.10f}" for m in (99, 100)), flush=True)
NL = (100, 200, 400, 800); TS = (0.0, 0.25, 0.5, 0.75, 1.0)
for K in (120000, 480000):
    kf = np.arange(1, K + 1, dtype=float)
    for name, (L, dL) in CASES.items():
        Lam = {n: [] for n in NL}
        for t in TS:
            ms = sorted({m for n in NL for m in (n - 1, n)}); MU = mu_rows(K, L, t, ms); row = []
            for n in NL:
                hi = int(min(n ** GAMMA, K)); lg = np.log(kf[n - 1:hi] / n)
                lam = max((MU[m][n - 1:hi] * lg).sum() for m in (n - 1, n)); Lam[n].append(lam)
                row.append(f"n={n}: {lam:.4f} [mu_n(>8n)={MU[n][8*n:].sum():.4f}]")
            print(f"  K={K} {name:5s} t={t:.2f}: Lambda " + " | ".join(row), flush=True)
        print(f"  K={K} {name:5s} sup_t Lambda_n: " + ", ".join(f"n={n}: {max(Lam[n]):.4f}" for n in NL)
              + " ; eps_n*sup_t Lambda_n: " + ", ".join(f"{eps_L0(L, n)*max(Lam[n]):.4f}" for n in NL)
              + " ; trivial bound (gamma-1)log n: " + ", ".join(f"{(GAMMA-1)*np.log(n):.1f}" for n in NL), flush=True)
