"""Plan 39 (NUMERICAL, float64 Lanczos with full reorthogonalization, as in check_t3_rough.py / check_mn_loc.py):
Theorem RW (Conjecture R in window form), §3.10 of PROOF.md. Windows W = [aN, bN], default [0.6N, 1.6N].
[0] Lemma FV (second-difference form) vs a central finite difference, p = s = 2, n = 60 (index convention check).
[1] The explicit constants of Lemma R1W / Theorem RW (pure quadrature, no Lanczos): u_s(p) = (4c(p))^{-1/p},
    c_W, δ_W = c_W/32, J_W = ⌈2/δ_W⌉, η_W = δ_W/J_W², ε₀ = η_W/16, θ₁(p), M_W, R_W; and the phase-model value
    η_W^ph = (8/π)∫_W sin²θ dθ/π (outline_C_rough.md §0; HEURISTIC, not used in the proof).
[2] The R1W mechanism for the pure power v = k^{-s} (s = 2): Q_N := <dist(y, Z_N)² 1_{S_N}, μ_{N-1}> (its limit is
    c_W by the weak convergence in R1W step 4); ‖D_N|_S‖₁, ‖D_{N-1}|_S‖₁; min over m ∈ [N-7, N] of ‖Δ²μ_m|_{S_N}‖₁.
[3] The Theorem RW construction, p = s = 2, W = [0.6N, 1.6N]: f = Σ_i ε·sign(Δ²μ^v_{m_i})·1_{W_i}, m_i ∈ [N_i-3, N_i]
    maximising ‖Δ²μ^v_m|_{W_i}‖₁. Report F_{m_i}(w), the linear prediction F_{m_i}(v) + <f, Δ²μ^v_{m_i}>, the
    cross-window part of <f, Δ²μ^v>, with Δ_n := F_n(w) − F_n(v) (F_n(v) = O(1/n) is the pure-power drift); the
    off-spike maximum of |Δ_n|; and a truncation-doubling check (Rule N).
Pass/fail flags are computed, never typed."""
import numpy as np
from jacobi_asym.laws.weyl import c_p


def lanczos(x, w, m):
    """Q[j] = √w p_j (j ≤ m), b[j] = b_j: x q_{j-1} = b_j q_j + a_{j-1} q_{j-1} + b_{j-1} q_{j-2}."""
    K = len(x); Q = np.zeros((m + 1, K)); a = np.zeros(m + 1); b = np.zeros(m + 1)
    q = np.sqrt(w); Q[0] = q / np.linalg.norm(q)
    for j in range(m):
        v = x * Q[j]; a[j] = Q[j] @ v; v -= a[j] * Q[j]
        if j: v -= b[j] * Q[j - 1]
        for _ in range(2): v -= Q[:j + 1].T @ (Q[:j + 1] @ v)
        b[j + 1] = np.linalg.norm(v); Q[j + 1] = v / b[j + 1]
    return a, b, Q


def F(b, n): return float(np.log(b[n] ** 2 / b[n - 1] ** 2))
def d2(mu, m): return mu[m] - 2 * mu[m - 1] + mu[m - 2]
def win(k, a, b, N): return (k >= a * N) & (k <= b * N)


TH = np.linspace(0.0, np.pi, 2_000_001)
DIST2 = np.minimum(np.abs(2 * np.cos(TH)), 2 - 2 * np.abs(np.cos(TH))) ** 2   # dist(2cosθ, {-2,0,2})²


def c_W(p, a, b):
    Y = 2 * c_p(p) * (1 + np.cos(TH)); m = (Y > b ** -p) & (Y < a ** -p)
    return float(np.trapezoid(DIST2 * m, TH) / np.pi), float((8 / np.pi) * np.trapezoid(np.sin(TH) ** 2 * m, TH) / np.pi)


def g_plus(p, t):
    g = (p - t) * np.log(1 / t) + (1 - t) * np.log(1 - t) - p + (p - 1) * t
    return g - (np.log(1 / p) if p < 1 else 0.0)


def theta1(p):
    t = np.linspace(1e-9, 0.5, 2_000_001); ok = g_plus(p, t) >= 1
    return float(t[np.argmin(ok) - 1]) if not ok.all() else 0.5   # ok[0] holds since g_p⁺ → ∞ as θ → 0


def constants(p, a, b):
    cw, eph = c_W(p, a, b); d = cw / 32; J = int(np.ceil(2 / d)); eta = d / J ** 2
    th1 = theta1(p)
    # F_p(M_W) = η_W/16  <=>  M_W = (4c sin²(π η_W / 32))^{-1/p}  (F_p(M) = (2/π)arcsin√(M^{-p}/(4c)), M ≥ 1)
    MW = max(1.0, (4 * c_p(p) * np.sin(np.pi * eta / 32) ** 2) ** (-1 / p))
    RW = max(b / a, 2 * b / th1, MW / a)
    return dict(cW=cw, ph=eph, delta=d, J=J, eta=eta, eps0=eta / 16, th1=th1, MW=MW, RW=RW)


# [0] FV check
K = 6000; k = np.arange(1, K + 1, dtype=float); x = k ** -2.0; v = k ** -2.0
f = np.random.default_rng(7).uniform(-1, 1, K); n = 60; h = 1e-5
fd = (F(lanczos(x, v * np.exp(h * f), n)[1], n) - F(lanczos(x, v * np.exp(-h * f), n)[1], n)) / (2 * h)
mu0 = lanczos(x, v, n)[2] ** 2
print(f"[0] dF_n/dt at t=0, n={n}: finite difference {fd:.9e}; Lemma FV <f, Δ²μ_n> = {f @ d2(mu0, n):.9e}", flush=True)

# [1] constants
print("[1] explicit constants (quadrature on 2·10⁶ points; c_W > 0 is all the proof needs)")
for p in (0.5, 1.0, 2.0, 4.0):
    us = (4 * c_p(p)) ** (-1 / p)
    for (a, b) in ((0.6, 1.6), (1.0, 2.0)):
        C = constants(p, a, b)
        print(f"    p={p} u_s={us:.4f} (b > u_s: {b > us})  W=[{a}N,{b}N]: c_W={C['cW']:.5f} δ_W={C['delta']:.3e}"
              f" J_W={C['J']} η_W={C['eta']:.3e} ε₀={C['eps0']:.3e} θ₁={C['th1']:.4f} M_W={C['MW']:.3e}"
              f" R_W={C['RW']:.3e} | phase-model η_W^ph={C['ph']:.3f}", flush=True)

# [2] R1W mechanism, pure power
print("[2] R1W mechanism for v = k^-2, W = [0.6N, 1.6N]: Q_N -> c_W; window norms vs η_W")
for p, Kf, Ns in ((2.0, 40, (100, 200, 300)), (1.0, 400, (50, 100))):
    C = constants(p, 0.6, 1.6); Nmax = max(Ns); K = Kf * Nmax
    k = np.arange(1, K + 1, dtype=float); a_, b_, Q = lanczos(k ** -p, k ** -2.0, Nmax + 1); mu = Q ** 2
    for N in Ns:
        S = win(k, 0.6, 1.6, N); bb = max(b_[N], b_[N - 1])
        y = (k ** -p - a_[N - 1]) / bb
        Z = np.array([s1 * b_[N - 1] / bb + s2 * b_[N] / bb for s1 in (-1, 1) for s2 in (-1, 1)])
        dist2 = np.min((y[:, None] - Z[None, :]) ** 2, axis=1)
        QN = float((dist2 * mu[N - 1])[S].sum())
        DN = np.abs(mu[N] - mu[N - 1])[S].sum(); DN1 = np.abs(mu[N - 1] - mu[N - 2])[S].sum()
        wn = [np.abs(d2(mu, m))[S].sum() for m in range(N - 7, N + 1)]
        print(f"    p={p} N={N} (K={K}): Q_N={QN:.4f} (limit c_W={C['cW']:.4f}; contradiction threshold 8δ_W="
              f"{8 * C['delta']:.4f}; Q_N > 8δ_W: {QN > 8 * C['delta']})  ‖D_N|S‖₁={DN:.3f} ‖D_N-1|S‖₁={DN1:.3f}"
              f"  min_m∈[N-7,N] ‖Δ²μ_m|S‖₁={min(wn):.3f} (≥ η_W: {min(wn) >= C['eta']}; phase model {C['ph']:.3f})",
              flush=True)

# [3] construction, p = s = 2
print("[3] Theorem RW construction, p = s = 2, W_i = [0.6N_i, 1.6N_i]")
p, A, B = 2.0, 0.6, 1.6
C = constants(p, A, B)
for scales, Kfs in (((30, 240), (40, 80)), ((15, 60, 240), (40,))):   # K-doubling (Rule N) on the 2-scale run
    for Kf in Kfs:
        K = Kf * max(scales); k = np.arange(1, K + 1, dtype=float); x = k ** -p; v = k ** -2.0
        nmax = max(scales) + 6
        _, bv, Qv = lanczos(x, v, nmax); muv = Qv ** 2
        ms, fs = [], []
        for N in scales:
            Wn = win(k, A, B, N)
            m = max(range(N - 3, N + 1), key=lambda mm: np.abs(d2(muv, mm))[Wn].sum())
            sg = np.sign(d2(muv, m)); sg[sg == 0] = 1.0
            ms.append(m); fs.append(sg * Wn)
        for eps in (0.05, 0.2):
            f = eps * sum(fs)
            _, bw, _ = lanczos(x, v * np.exp(f), nmax)
            dF = {n: F(bw, n) - F(bv, n) for n in range(10, nmax + 1)}   # Δ_n := F_n(w) − F_n(v); F_n(v) = O(1/n)
            spikes = []
            for i, (N, m) in enumerate(zip(scales, ms)):
                lin_own = float(eps * np.abs(d2(muv, m))[win(k, A, B, N)].sum())
                lin_all = float(f @ d2(muv, m))
                spikes.append(f"N={N} m={m}: Δ_m={dF[m]:+.4f} (linear <f,Δ²μ^v_m>={lin_all:+.4f}; own window"
                              f" ε‖Δ²μ^v_m|W‖₁={lin_own:.4f}; cross-window {lin_all - lin_own:+.1e}); F_m(w)={F(bw, m):+.4f}")
            off = max(abs(dF[n]) for n in dF if min(abs(n - m) for m in ms) > 2)
            print(f"    scales={scales} K={K} ε={eps}: " + "; ".join(spikes), flush=True)
            print(f"        off-spike max |Δ_n| (n ∈ [10,{nmax}], |n-m_i| > 2) = {off:.4f}; every spike Δ_m > off-spike max:"
                  f" {all(dF[m] > off for m in ms)}; |F_n(v)| at n = {max(scales)}: {abs(F(bv, max(scales))):.4f}",
                  flush=True)
print(f"    (proved lower bound at ε ≤ ε₀ = {C['eps0']:.2e}: liminf_i F_(m_i)(w) ≥ εη_W/2; the runs use ε ≫ ε₀"
      f" and test the mechanism, not the constants)")
