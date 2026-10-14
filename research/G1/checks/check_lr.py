"""Plan 40 (NUMERICAL): Lemma LR (linear response) and its a_n analogue LRa, G1 PROOF.md §3.11.

Measures: truncated pure power x_k = k^{-p}, v_k = k^{-s}, k <= K (K = 20n). The lemma is an identity-level inequality
valid for EVERY finite-moment weight, so the truncated measure is itself an admissible test case (no truncation error
enters the inequality being tested). Lanczos (float64, full double reorthogonalization), Q[j] = sqrt(w) p_j = q_j,
a[j] = <x q_j, q_j>, b[j] = <x q_{j-1}, q_j>.

Quantities (eps := (max f - min f)/2, the osc-radius):
  R_b := log b_n^2(v e^f) - log b_n^2(v) - <f, mu_n - mu_{n-1}>          claim |R_b| <= eps^2
  R_F := F_n(v e^f) - F_n(v) - <f, mu_n - 2mu_{n-1} + mu_{n-2}>          claim |R_F| <= 2 eps^2
  R_a := a_n(v e^f) - a_n(v) - (b_{n+1} g_n - b_n g_{n-1})(v),  g_m := <f q_m, q_{m+1}>
                                                                   claim |R_a| <= (e^eps - 1 - eps)(b_n + b_{n+1})(v)
[1] random f (uniform in [-eps, eps], and random signs +-eps) and adversarial f (sign power iteration on the Hessian of
    log b_n^2 / of a_n; sign(mu_n - mu_{n-1}); window signs), several eps and n, p = s = 2 and p = 1, s = 2.
[2] path uniformity: |g''(t)| / eps^2 (g = log b_n^2 along v e^{tf}) at t = 0, 0.5, 1 from the exact formula
    Var-differences, cross-checked by a central second difference; claim |g''(t)| <= 2 eps^2 for every t.
[3] Rule A: brute force over tiny measures (K = 3..6 atoms, random nodes/weights), all sign patterns f in {+-1}^K,
    every n with 1 <= n <= K - 3 (Lanczos needs q_0..q_{n+2}): max |R_b|/eps^2, |R_a|/bound, and max |R_F|/eps^2
    over n >= 2 (R_F needs b_{n-1} > 0). Exceptions are counted and printed (Rule R F4).
Runtime: about 30-60 s wall (a few CPU-minutes, multithreaded BLAS).
[4] Rule N: one case recomputed with longdouble Lanczos.
"""
import numpy as np, itertools, sys

def lanczos(x, w, n, dt=np.float64):
    x = np.asarray(x, dt); w = np.asarray(w, dt)
    K = len(x); Q = np.zeros((n + 2, K), dt); q = np.sqrt(w); q /= np.sqrt(q @ q); Q[0] = q
    a = np.zeros(n + 2, dt); b = np.zeros(n + 2, dt)
    for j in range(n + 1):
        z = x * Q[j]; a[j] = Q[j] @ z
        z = z - a[j] * Q[j]
        if j: z = z - b[j] * Q[j - 1]
        for _ in range(2): z = z - Q[:j + 1].T @ (Q[:j + 1] @ z)
        b[j + 1] = np.sqrt(z @ z); Q[j + 1] = z / b[j + 1]
    a[n + 1] = Q[n + 1] @ (x * Q[n + 1])
    return a, b, Q

def dV(Q, m, f):
    """Var_{m+1} - Var_m = ||f q_m||^2 - <f,mu_m>^2 - 2||K_m(f q_m)||^2 (exact formula, §3.11 step 2)."""
    u = f * Q[m]; al = u @ Q[m]; c = Q[:m] @ u
    return u @ u - al ** 2 - 2 * c @ c

def hess_b(Q, n, f):
    """Symmetric action H f with f^T H f = dV_n(f) - dV_{n-1}(f) (= g''(0) for g = log b_n^2)."""
    out = 0
    for m, sg in ((n, 1), (n - 1, -1)):
        mu = Q[m] ** 2
        out = out + sg * (mu * f - mu * (mu @ f) - 2 * Q[m] * (Q[:m].T @ (Q[:m] @ (Q[m] * f))))
    return out

def rem(x, v, n, f, base=None):
    a0, b0, Q = base if base is not None else lanczos(x, v, n + 1)
    a1, b1, _ = lanczos(x, v * np.exp(f), n + 1)
    eps = (f.max() - f.min()) / 2
    mu = [Q[n - i] ** 2 for i in range(3)]
    Rb = np.log(b1[n] ** 2) - np.log(b0[n] ** 2) - f @ (mu[0] - mu[1])
    RF = ((np.log(b1[n] ** 2 / b1[n - 1] ** 2) - np.log(b0[n] ** 2 / b0[n - 1] ** 2)) - f @ (mu[0] - 2 * mu[1] + mu[2])
          if n >= 2 else np.nan)
    La = b0[n + 1] * (f * Q[n]) @ Q[n + 1] - b0[n] * (f * Q[n - 1]) @ Q[n]
    Ra = a1[n] - a0[n] - La
    bnd_a = (np.expm1(eps) - eps) * (b0[n] + b0[n + 1])
    return Rb / eps ** 2, RF / eps ** 2, Ra / bnd_a, eps

def sign_iter(H, f0, it=30, sgn=1):
    f = np.sign(f0); f[f == 0] = 1
    for _ in range(it):
        g = np.sign(sgn * H(f)); g[g == 0] = 1
        if np.array_equal(g, f): break
        f = g
    return f

rng = np.random.default_rng(40)
worst = {"b": 0.0, "F": 0.0, "a": 0.0}
print("[1] remainder ratios  R_b/eps^2 (claim |.|<=1), R_F/eps^2 (claim <=2), R_a/bound_a (claim <=1)", flush=True)
for p, s, ns in ((2.0, 2.0, (50, 100, 200)), (1.0, 2.0, (50, 100))):
    for n in ns:
        K = 20 * n; k = np.arange(1, K + 1, dtype=float); x = k ** -p; v = k ** -s
        base = lanczos(x, v, n + 1); Q = base[2]
        H = lambda f: hess_b(Q, n, f)
        D = Q[n] ** 2 - Q[n - 1] ** 2
        win = np.zeros(K); win[int(0.6 * n):int(1.6 * n)] = 1
        shapes = {
            "unif": rng.uniform(-1, 1, K),
            "signs": rng.choice([-1.0, 1.0], K),
            "sgn(D)": np.sign(D) + (D == 0),
            "win*sgn(D)": win * np.sign(D),
            "advH+": sign_iter(H, rng.standard_normal(K), sgn=1),
            "advH-": sign_iter(H, rng.standard_normal(K), sgn=-1),
            "advH+(D)": sign_iter(H, D, sgn=1),
        }
        for name, f in shapes.items():
            f = f / ((f.max() - f.min()) / 2)       # osc-radius 1
            row = []
            for eps in (0.4, 0.2, 0.1, 0.05, 0.025):
                rb, rF, ra, e = rem(x, v, n, eps * f, base)
                worst["b"] = max(worst["b"], abs(rb)); worst["F"] = max(worst["F"], abs(rF)); worst["a"] = max(worst["a"], abs(ra))
                row.append(f"{eps}:{rb:+.3f}/{rF:+.3f}/{ra:+.3f}")
            q0 = f @ H(f)   # g''(0)/eps^2 for this shape
            print(f"p={p:g} s={s:g} n={n:3d} {name:10s} g''(0)/eps^2={q0:+.3f} | " + "  ".join(row), flush=True)
print(f"[1] worst |R_b|/eps^2 = {worst['b']:.4f} (<=1: {worst['b'] <= 1}); worst |R_F|/eps^2 = {worst['F']:.4f} (<=2: {worst['F'] <= 2}); "
      f"worst |R_a|/bound = {worst['a']:.4f} (<=1: {worst['a'] <= 1})", flush=True)

print("[2] path uniformity, p = s = 2, n = 100, f = advH+ shape at eps = 0.4: |g''(t)|/eps^2 (formula | central diff, h = 1e-3)", flush=True)
n = 100; K = 20 * n; k = np.arange(1, K + 1, dtype=float); x = k ** -2.0; v = k ** -2.0
_, _, Q = lanczos(x, v, n + 1); f = sign_iter(lambda f: hess_b(Q, n, f), rng.standard_normal(K)); eps = 0.4; f = eps * f
lb = lambda t: np.log(lanczos(x, v * np.exp(t * f), n + 1)[1][n] ** 2)
mx = 0.0
for t in (0.0, 0.5, 1.0):
    _, _, Qt = lanczos(x, v * np.exp(t * f), n + 1)
    form = dV(Qt, n, f) - dV(Qt, n - 1, f); h = 1e-3
    fd = (lb(t + h) - 2 * lb(t) + lb(t - h)) / h ** 2
    mx = max(mx, abs(form) / eps ** 2)
    print(f"    t={t}: {form/eps**2:+.5f} | {fd/eps**2:+.5f}", flush=True)
print(f"[2] max_t |g''(t)|/eps^2 = {mx:.4f} (<=2: {mx <= 2})", flush=True)

print("[3] Rule A: tiny measures, all sign patterns", flush=True)
wb = wa = wF = 0.0; cnt = skipped = 0
for K in (4, 5, 6):
    for trial in range(25):
        x = np.sort(rng.uniform(-1, 1, K)); v = rng.uniform(0.05, 1, K)
        for n in range(1, K - 2):
            base = lanczos(x, v, n + 1)
            for sg in itertools.product((-1.0, 1.0), repeat=K):
                f0 = np.array(sg)
                if f0.max() == f0.min(): continue
                for eps in (1.0, 0.05):
                    try:
                        rb, rF, ra, e = rem(x, v, n, eps * f0, base)
                    except Exception:
                        skipped += 1; continue
                    cnt += 1; wb = max(wb, abs(rb)); wa = max(wa, abs(ra))
                    if n >= 2: wF = max(wF, abs(rF))
print(f"[3] {cnt} cases ({skipped} skipped by exceptions): max |R_b|/eps^2 = {wb:.4f} (<=1: {wb <= 1}); "
      f"max |R_F|/eps^2 (n>=2) = {wF:.4f} (<=2: {wF <= 2}); max |R_a|/bound = {wa:.4f} (<=1: {wa <= 1})", flush=True)

print("[4] Rule N: p = s = 2, n = 40, K = 800, f = advH+ shape, eps = 0.05: float64 vs longdouble Lanczos", flush=True)
n = 40; K = 800; k = np.arange(1, K + 1, dtype=float); x = k ** -2.0; v = k ** -2.0
_, _, Q = lanczos(x, v, n + 1); f = 0.05 * sign_iter(lambda f: hess_b(Q, n, f), rng.standard_normal(K))
r64 = rem(x, v, n, f)
xl = x.astype(np.longdouble); vl = v.astype(np.longdouble); fl = f.astype(np.longdouble)
bl = lanczos(xl, vl, n + 1, np.longdouble)
a1, b1, _ = lanczos(xl, vl * np.exp(fl), n + 1, np.longdouble); a0, b0, Ql = bl
Rb = (np.log(b1[n] ** 2) - np.log(b0[n] ** 2) - fl @ (Ql[n] ** 2 - Ql[n - 1] ** 2)) / np.longdouble(0.05) ** 2
print(f"    R_b/eps^2: float64 {r64[0]:+.10f}  longdouble {float(Rb):+.10f}  diff {abs(r64[0]-float(Rb)):.1e}", flush=True)
