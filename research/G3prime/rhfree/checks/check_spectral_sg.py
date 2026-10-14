"""Plan 19 numerical sanity for RHFREE.md §2 (Theorem S): NUMERICAL, not a proof.

[1] D(λ) := Q(0) − 2∫_0^1(1−α)Q(α)dα → 0 like λ^{-3}, for η_λ² = (1/λ)cos²(πu/2λ) on (−λ, λ), Q = η²∗η².
    Also reproduces Lamzouri's support-1 bracket check: 2 − C_η > 0.
[2] Operator identities on synthetic conjugation-invariant multisets Z (critical points + off-line pairs + doubles):
    nonzero spectrum of A = eig(J·G) on W = span{f_x, g_z, h_z}; check tr A = N and tr A² = S := Σ_{z,s} K(z−s)².
[3] Deterministic small-gap lemma (Lemma G): with δ := 1/(4πλ),
      #{consecutive gaps < δ among simple real elements} ≤ 4[4(S − 2N + N_d) + (N_d − N_1)].
    Checked on Poisson, GUE-like (sine-kernel surrogate), and clustered configurations.
"""
import numpy as np

rng = np.random.default_rng(19)

def S0(xi, lam):
    # ∫_{-λ}^{λ} e^{-2πiuξ} du = sin(2πλξ)/(πξ), entire; complex ξ allowed
    xi = np.asarray(xi, dtype=complex)
    out = np.empty_like(xi)
    small = np.abs(xi) < 1e-12
    out[small] = 2 * lam
    x = xi[~small]
    out[~small] = np.sin(2 * np.pi * lam * x) / (np.pi * x)
    return out

def K(xi, lam):
    # K = (η²)^ with η² = (1/λ)cos²(πu/2λ) = (1/2λ)(1 + cos(πu/λ)) on (−λ, λ)
    a = 1 / (2 * lam)
    return (S0(xi, lam) + 0.5 * S0(np.asarray(xi) - a, lam) + 0.5 * S0(np.asarray(xi) + a, lam)) / (2 * lam)

def D_of(lam, n=20001):
    u = np.linspace(-lam, lam, n); du = u[1] - u[0]
    f = (1 / lam) * np.cos(np.pi * u / (2 * lam)) ** 2
    from scipy.signal import fftconvolve; Q = fftconvolve(f, f) * du                     # on grid of spacing du, centered
    al = (np.arange(Q.size) - (Q.size - 1) / 2) * du
    Q0 = Q[(Q.size - 1) // 2]
    m = (al >= 0) & (al <= 1)
    return Q0 - 2 * np.trapezoid((1 - al[m]) * Q[m], al[m]), Q0, np.trapezoid(Q, al)

print("[1] D(λ) for η_λ² = (1/λ)cos²(πu/2λ)")
for lam in [0.25, 0.5, 1, 2, 4, 8, 16]:
    D, Q0, intQ = D_of(lam)
    print(f"  λ={lam:6.2f}  ∫Q={intQ:.6f}  Q(0)={Q0:.6f}  D={D:.3e}  λ³D={lam**3*D:.5f}  bracket 1+D={1+D:.6f}")

def spectrum_check(real_pts, offline, doubles, lam):
    """real_pts: simple real elements; offline: list of z (Im z > 0), each paired with conj, mult 1;
    doubles: real points with multiplicity 2."""
    Z = list(real_pts) + list(doubles) * 2 + list(offline) + [np.conj(z) for z in offline]
    Z = np.array(Z, dtype=complex)
    N = Z.size
    S = np.sum(K(Z[:, None] - Z[None, :], lam) ** 2)
    # real Gram of basis {f_x (distinct real), g_z, h_z}; <f_a, f_b> = K(a − conj b)
    xs = np.concatenate([np.array(real_pts, float), np.array(doubles, float)])
    mx = np.concatenate([np.ones(len(real_pts)), 2 * np.ones(len(doubles))])
    zs = np.array(offline, dtype=complex)
    def ip(a, b): return K(a[:, None] - np.conj(b)[None, :], lam)
    ff = ip(xs.astype(complex), xs.astype(complex))
    fz = ip(xs.astype(complex), zs); fzb = ip(xs.astype(complex), np.conj(zs))
    zz = ip(zs, zs); zzb = ip(zs, np.conj(zs)); zbz = ip(np.conj(zs), zs); zbzb = ip(np.conj(zs), np.conj(zs))
    # g = (f_z + f_zbar)/2, h = (f_z − f_zbar)/(2i)
    fg = (fz + fzb) / 2; fh = (fz - fzb) / (-2j)   # <f_x, h> = conj(1/(2i)) (…) = (…)/(−2i)
    gg = (zz + zzb + zbz + zbzb) / 4
    hh = (zz - zzb - zbz + zbzb) / 4
    gh = (zz - zzb + zbz - zbzb) / (-2j) / 2       # <g, h> = (1/2)·conj(1/(2i))·(<f_z,f_z> − <f_z,f_zb> + <f_zb,f_z> − <f_zb,f_zb>)
    G = np.block([[ff, fg, fh], [fg.conj().T, gg, gh], [fh.conj().T, gh.conj().T, hh]])
    imag_rel = np.abs(G.imag).max() / max(1e-300, np.abs(G.real).max())
    G = G.real
    J = np.concatenate([mx, 2 * np.ones(len(zs)), -2 * np.ones(len(zs))])
    w, V = np.linalg.eigh(G)
    Gh = (V * np.sqrt(np.clip(w, 0, None))) @ V.T
    mu = np.linalg.eigvalsh(Gh @ np.diag(J) @ Gh)
    Nd = len(xs) + 2 * len(zs); N1 = len(real_pts)
    # Lemma G
    delta = 1 / (4 * np.pi * lam)
    x1 = np.sort(np.array(real_pts, float))
    small = int(np.sum(np.diff(x1) < delta))
    rhs = 4 * (4 * (S.real - 2 * N + Nd) + (Nd - N1))
    G1 = np.real(K(x1[:, None] - x1[None, :], lam))
    g1 = np.linalg.eigvalsh(G1)
    out_G1 = int(np.sum((g1 <= 0.5) | (g1 >= 1.5)))
    out_A = int(np.sum((mu <= 0.5) | (mu >= 1.5)))
    return dict(N=N, Nd=Nd, N1=N1, S=S, imag_rel=imag_rel, trA=mu.sum(), trA2=(mu ** 2).sum(),
                small=small, rhs=rhs, out_G1=out_G1, out_A=out_A, bnd_G1=out_A + (Nd - N1), cond=np.linalg.cond(G))

def configs(n):
    pois = np.cumsum(rng.exponential(1.0, n))
    # GUE-like surrogate: eigenvalues of a GUE matrix, bulk, unfolded by semicircle density
    M = n * 3
    H = rng.normal(size=(M, M)) + 1j * rng.normal(size=(M, M)); H = (H + H.conj().T) / 2
    e = np.linalg.eigvalsh(H) / np.sqrt(M)                       # semicircle on [−√2·…]
    R = np.sqrt(2.0)
    def F(x): x = np.clip(x / R, -1, 1); return M * (0.5 + (x * np.sqrt(1 - x * x) + np.arcsin(x)) / np.pi)
    u = F(e); mid = np.argsort(np.abs(u - M / 2))[:n]; gue = np.sort(u[mid]); gue -= gue[0]
    clus = np.sort(np.concatenate([np.arange(n // 2) * 2.0, np.arange(n // 2) * 2.0 + rng.uniform(0, 0.05, n // 2)]))
    return {"poisson": pois, "gue": gue, "clustered": clus}

print("\n[2]/[3] operator identities and Lemma G on synthetic multisets")
for lam in [0.5, 1.0, 2.0]:
    for name, pts in configs(120).items():
        span = pts.max()
        for (k_off, k_dbl) in [(0, 0), (4, 2), (10, 5)]:
            off = list(rng.uniform(0, span, k_off) + 1j * rng.uniform(0.01, 0.5, k_off))
            dbl = list(rng.uniform(0, span, k_dbl))
            r = spectrum_check(pts, off, dbl, lam)
            ok_tr = abs(r["trA"] - r["N"]) < 1e-6 * r["N"] and abs(r["trA2"] - r["S"].real) < 1e-6 * r["S"].real
            ok_G = r["small"] <= r["rhs"] and r["out_G1"] <= r["bnd_G1"]
            print(f"  λ={lam:3.1f} {name:9s} off={k_off:2d} dbl={k_dbl} N={r['N']:3d} Nd={r['Nd']:3d} "
                  f"trA−N={r['trA']-r['N']:+.1e} trA²−S={r['trA2']-r['S'].real:+.1e} ImS={r['S'].imag:+.1e} "
                  f"S/N={r['S'].real/r['N']:.3f} small={r['small']:3d} ≤ rhs={r['rhs']:8.1f} "
                  f"outG1={r['out_G1']:3d} ≤ {r['bnd_G1']:3d} cond(G)={r['cond']:.1e} "
                  f"{'OK' if (ok_tr and ok_G) else 'FAIL'}")

print("\n[3b] Lemma G in a non-trivial regime: GUE-like + m injected near-pairs (gap 0.01), no off-line, λ = 2")
base = configs(200)["gue"]
for m in [0, 2, 5, 10, 20]:
    inj = rng.choice(base[1:-1], m, replace=False) + 0.01
    pts = np.sort(np.concatenate([base, inj]))
    r = spectrum_check(pts, [], [], 2.0)
    g1 = np.linalg.eigvalsh(np.real(K(pts[:, None] - pts[None, :], 2.0)))
    print(f"  m={m:2d} N={r['N']} small={r['small']:3d} ≤ rhs={r['rhs']:7.1f}  (S−N)={r['S'].real-r['N']:7.2f}  "
          f"#eig(G1)≤1/4={int(np.sum(g1<=0.25)):3d} ≥ p/2  outG1={r['out_G1']}  {'OK' if r['small']<=r['rhs'] else 'FAIL'}")
