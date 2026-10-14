"""Plan 42 (NUMERICAL, float64 Lanczos with full reorthogonalization): Lemma RL (§3.13).
ν_n := image of μ_n = w p_n² under x ↦ n^p x; arcsine law on [0, 4c] has moments m_ℓ = c^ℓ·binom(2ℓ, ℓ) (2c, 6c², 70c⁴).
[1] Identity check (pure power p = s = 2, n = 100): moments of ν_n by quadrature over the atoms vs the path sums
    ((n^pJ)^ℓ)_{nn} from the Lanczos coefficients, and the 4th-moment decomposition of the proof
    ∫y⁴dν_n = α⁴ + 4α³(K)_{nn} + 6α²(K²)_{nn} + 4α(K³)_{nn} + (K⁴)_{nn}, with α = 2c(p), K := n^pJ − α.
[2] Order parameters along n: dev_n := max(|n^pb_n/c − 1|, |n^pa_n/(2c) − 1|) and
    mom_n := max_{ℓ∈{1,2,4}} |∫y^ℓdν_n/m_ℓ − 1|, for
    (v) pure power w = k^{-2}; (sv) w = k^{-2}(2 + sin(log log(k+2))) (slowly varying, T3-all);
    (R) Theorem-R-type adversarial weight w = k^{-2}e^{f}, f = ε·sign(Δ²μ_N) on [0.6N, 1.6N] for N = 60, 240, ε = 0.2
        (the construction of checks/check_t3_rough.py [3]); (rnd) w = k^{-2}U_k, U_k iid uniform[1/2, 3/2].
    rdev_n, rmom_n: the same relative to the pure power at the same n and K (removes the common O(1/n) error);
    jump_n := |β_n/β_{n−1} − 1|. Lemma RL predicts: mom_n → 0 iff dev_n → 0 (the a priori bound
    sup n^p(a_n + b_n) < ∞ holds for all of these). A finite computation cannot show (non)convergence; it shows that
    the two order parameters move together.
[2b] Rule N: K doubling for (sv) at n = 200.
[3] Remarks RL-b and RL-loc (§3.13): prescribed Jacobi parameters (exact path sums, no measure computation).
    (b-only) a_m = 3c m^{-p}, b_m = c m^{-p}: the b-law holds, ν_n → arcsine on [c, 5c], not [0, 4c].
    (loc) a_m = 2β m^{-p}·1, b_m = 2β (m−1)^{-p/2}m^{-p/2}cos θ_{m−1} sin θ_m, θ ≡ π/4 except θ_{n_j} = arcsin(√t),
        t = 1/4: all moments of ν_{n_j} → arcsine moments, but n_j^p b_{n_j}/β → √(2t); neighbours n_j ± 1 deviate."""
import numpy as np
from math import comb
from jacobi_asym.laws.weyl import c_p

p, s = 2.0, 2.0
c = c_p(p)
mom_arc = {l: c ** l * comb(2 * l, l) for l in (1, 2, 4)}


def lanczos(x, w, m):
    K = len(x); Q = np.zeros((m + 2, K)); q = np.sqrt(w); Q[0] = q / np.linalg.norm(q)
    a = np.zeros(m + 2); b = np.zeros(m + 2)
    for j in range(m + 1):
        z = x * Q[j]; a[j] = Q[j] @ z; z -= a[j] * Q[j]
        if j: z -= b[j] * Q[j - 1]
        for _ in range(2): z -= Q[:j + 1].T @ (Q[:j + 1] @ z)
        b[j + 1] = np.linalg.norm(z); Q[j + 1] = z / b[j + 1]
    return a, b, Q          # x q_j = b_{j+1} q_{j+1} + a_j q_j + b_j q_{j−1}


def local_J(a, b, n, r, scale):
    """(2r+1)×(2r+1) block of scale·J centred at n (indices n−r..n+r)."""
    idx = np.arange(n - r, n + r + 1)
    return scale * (np.diag(a[idx]) + np.diag(b[idx[1:]], 1) + np.diag(b[idx[1:]], -1))


def path_moment(a, b, n, l, scale):
    B = local_J(a, b, n, l, scale); return np.linalg.matrix_power(B, l)[l, l]


# [1]
K = 20000; k = np.arange(1, K + 1, dtype=float); x = k ** -p
a, b, Q = lanczos(x, k ** -s, 110); n = 100; y = n ** p * x; mu = Q[n] ** 2
print(f"[1] p=s=2, n={n}, K={K}: total mass of mu_n = {mu.sum():.12f}")
for l in (1, 2, 3, 4):
    print(f"    l={l}: quadrature {np.sum(y ** l * mu):.10e}  path sum {path_moment(a, b, n, l, n ** p):.10e}")
al = 2 * c; Kb = local_J(a, b, n, 4, n ** p) - al * np.eye(9)
Kp = {j: np.linalg.matrix_power(Kb, j)[4, 4] for j in (1, 2, 3, 4)}
E = lambda m: n ** p * b[m]
K4f = (E(n) ** 2 + E(n + 1) ** 2) ** 2 + E(n + 1) ** 2 * E(n + 2) ** 2 + E(n) ** 2 * E(n - 1) ** 2
print(f"    4th-moment decomposition: {al**4 + 4*al**3*Kp[1] + 6*al**2*Kp[2] + 4*al*Kp[3] + Kp[4]:.10e} vs quadrature "
      f"{np.sum(y ** 4 * mu):.10e};  (K)_nn = {Kp[1]:.3e}, (K^3)_nn = {Kp[3]:.3e} (both → 0);  (K^4)_nn = {Kp[4]:.6e}, its off-diagonal-path part "
      f"{K4f:.6e}, limit 6c^4 = {6 * c ** 4:.6e}", flush=True)


# [2]
def order_params(a, b, ns, ref=None):
    """dev/mom vs the arcsine limit; with ref = (a_v, b_v): rdev/rmom relative to the pure power at the same n and K
    (removes the common O(1/n) finite-n error); jump := |β_n/β_{n−1} − 1|."""
    out = []
    for n in ns:
        dev = max(abs(n ** p * b[n] / c - 1), abs(n ** p * a[n] / (2 * c) - 1))
        ms = {l: path_moment(a, b, n, l, n ** p) for l in (1, 2, 4)}
        mom = max(abs(ms[l] / mom_arc[l] - 1) for l in (1, 2, 4))
        row = [n, dev, mom]
        if ref is not None:
            av, bv = ref
            row.append(max(abs(b[n] / bv[n] - 1), abs(a[n] / av[n] - 1)))
            row.append(max(abs(ms[l] / path_moment(av, bv, n, l, n ** p) - 1) for l in (1, 2, 4)))
            row.append(abs((b[n] / b[n - 1]) * (n / (n - 1)) ** p - 1))
        out.append(row)
    return out


def show(tag, rows):
    f = lambda r: (f"n={r[0]}: dev={r[1]:.1e} mom={r[2]:.1e}" +
                   (f" rdev={r[3]:.1e} rmom={r[4]:.1e} jump={r[5]:.1e}" if len(r) > 3 else ""))
    print(f"[2] {tag}:\n      " + "\n      ".join(f(r) for r in rows), flush=True)


K = 60000; k = np.arange(1, K + 1, dtype=float); x = k ** -p; v = k ** -s
ns = (50, 100, 200, 400)
av, bv, _ = lanczos(x, v, 405); show("(v)  pure power", order_params(av, bv, ns))
psi = 2 + np.sin(np.log(np.log(k + 2)))
a, b, _ = lanczos(x, v * psi, 405); show("(sv) slowly varying", order_params(a, b, ns, (av, bv)))
U = np.random.default_rng(7).uniform(0.5, 1.5, K)
a, b, _ = lanczos(x, v * U, 405); show("(rnd) iid U[1/2,3/2]", order_params(a, b, ns, (av, bv)))

K = 6000; k = np.arange(1, K + 1, dtype=float); x = k ** -p; v = k ** -s; eps = 0.2; f = np.zeros(K)
for N in (60, 240):
    _, _, Q = lanczos(x, v, N + 1); d2 = Q[N] ** 2 - 2 * Q[N - 1] ** 2 + Q[N - 2] ** 2
    sl = slice(int(0.6 * N), int(1.6 * N)); f[sl] = eps * np.sign(d2[sl])
av6, bv6, _ = lanczos(x, v, 395)
a, b, _ = lanczos(x, v * np.exp(f), 395)
print(f"[2] (R)  adversarial eps={eps}, f = eps*sign(D^2 mu_N) on [0.6N,1.6N], N = 60, 240 (f = 0 on [97,143] and n > 384), K={K}")
for N in (60, 240):
    show(f"(R)  near N={N}", order_params(a, b, (N - 2, N - 1, N, N + 1, N + 2), (av6, bv6)))
show("(R)  outside the windows", order_params(a, b, (20, 110, 130, 389), (av6, bv6)))

# [2b] Rule N
for Kt in (60000, 120000):
    k = np.arange(1, Kt + 1, dtype=float); a, b, _ = lanczos(k ** -p, k ** -s * (2 + np.sin(np.log(np.log(k + 2)))), 205)
    (n, d, m), = order_params(a, b, (200,))
    print(f"[2b] (sv) K={Kt}: n=200 dev={d:.6e} mom={m:.6e}", flush=True)

# [3]
beta = c; M = 20010
mm = np.arange(M, dtype=float); mm[0] = 1.0
a3 = 3 * c * mm ** -p; b3 = c * mm ** -p; b3[0] = 0.0
print("[3] (b-only) diag 3c m^-p, off-diag c m^-p (b-law holds): moments of nu_n / arcsine[0,4c] moments; "
      "arcsine[c,5c] has m_1 = 3c, m_2 = 11c^2, m_4 = 195c^4:")
for n in (100, 1000, 10000):
    print(f"    n={n}: " + "  ".join(f"m_{l}/c^{l}={path_moment(a3, b3, n, l, n ** p) / c ** l:.4f}" for l in (1, 2, 4)))
t = 0.25; nj = (100, 1000, 10000)
th = np.full(M, np.pi / 4); th[list(nj)] = np.arcsin(np.sqrt(t))
a4 = 2 * beta * mm ** -p
b4 = np.zeros(M); b4[1:] = 2 * beta * (mm[:-1] ** (-p / 2)) * (mm[1:] ** (-p / 2)) * np.cos(th[:-1]) * np.sin(th[1:])
b4[1] = 2 * beta * 1.0 * np.cos(th[0]) * np.sin(th[1])  # m = 1 uses (m−1)^{-p/2} := 1
arc = lambda l: c ** l * comb(2 * l, l)
print(f"[3] (loc) theta-construction, t = {t}: arcsine[0,4c] moments m_l/c^l = " + ", ".join(str(comb(2 * l, l)) for l in range(1, 9)))
for n in nj:
    for nn in (n - 1, n, n + 1):
        ms = [path_moment(a4, b4, nn, l, nn ** p) / arc(l) for l in range(1, 9)]
        print(f"    n={nn}: n^p b_n/beta={nn ** p * b4[nn] / beta:.4f}  (moment_l / arcsine moment_l, l=1..8) = "
              + " ".join(f"{r:.5f}" for r in ms))
Jt = np.diag(a4[:3000]) + np.diag(b4[1:3000], 1) + np.diag(b4[1:3000], -1)
ev0 = np.linalg.eigvalsh(Jt)[0]
print(f"    sanity: smallest eigenvalue of the leading 3000x3000 block of J = {ev0:.3e} (positive: {ev0 > 0}; J = LL^T + k_0^2 e_0e_0^T)",
      flush=True)
