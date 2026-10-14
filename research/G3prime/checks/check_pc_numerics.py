"""Plan 18 (NUMERICAL, Odlyzko zeros data/raw): sanity checks for the primes–zeros picture behind G3′.
[1] Small-gap profile: with the normalized gaps g_k = (γ_{k+1} − γ_k) log(γ_k/2π)/2π over k ≤ 2·10⁶,
    the fraction #{g_k < δ}/K against the GUE nearest-neighbour CDF (Wigner surmise, 32/(3π²)δ³ to leading order),
    and the pair count N(β)/K (forward pairs among the next 7 neighbours; enough for β ≤ 0.5) against ∫_0^β(1 − (sin πu/πu)²)du ~ (π²/9)β³.
    The β³ law is the repulsion that gives (SG).
[2] G3′ defect for the true-zero measure (toolkit true_zeta): D(n) := (2/n²)Σ_{j<n}(n−j)log(b_j/x̃_j) − log(π²/16),
    against the smooth model (smooth_zeta) at the same n.
[3] Stability (Rule N): D_true at J = 1e5, 2e5, 4e5 (double) and J = 2e5 (long double), n ≤ 1600.
NB: the data are a finite sample; this is evidence about the sample, not about the asymptotics (AGENTS.md rule 3)."""
import numpy as np
from scipy.integrate import quad
from jacobi_asym.measures.lfun import load_odlyzko, true_zeta, smooth_zeta, model_zeros
from jacobi_asym.jacobi import jacobi_coeffs

g = np.asarray(load_odlyzko(), float)
K = len(g) - 1
gap = np.diff(g) * np.log(g[:-1] / (2 * np.pi)) / (2 * np.pi)
print(f"[1] K = {K} gaps, γ up to {g[-1]:.1f}; mean normalized gap {gap.mean():.5f}; min {gap.min():.5f}")
wig = lambda s: 32 / np.pi**2 * s**2 * np.exp(-4 * s**2 / np.pi)
pcdens = lambda u: 1 - (np.sinc(u))**2
for d in (0.02, 0.05, 0.1, 0.2, 0.3, 0.5):
    frac = np.mean(gap < d)
    cdf = quad(wig, 0, d)[0]
    # pair count within β (normalized by local density), forward pairs
    L = np.log(g / (2 * np.pi)) / (2 * np.pi)
    cnt = 0
    for m in range(1, 8):
        dd = (g[m:] - g[:-m]) * L[:-m]
        cnt += np.count_nonzero(dd <= d)
    pc = quad(pcdens, 0, d)[0]
    print(f"   δ=β={d:4.2f}: #{{g<δ}}/K = {frac:.3e} (GUE NN CDF {cdf:.3e});  N(β)/K = {cnt/K:.3e} (PCC {pc:.3e})")

print("[2] G3′ defect D(n) = (2/n²)Σ(n−j)log(b_j/x̃_j) − log(π²/16), true zeros vs smooth model")
J = 400_000
mu_t = true_zeta(J)
mu_s = smooth_zeta(J)
nmax = 3200
xt = np.sort(1 / (model_zeros(J) ** 2 + 0.25))[::-1]
res = {}
for name, mu in (("true", mu_t), ("smooth", mu_s)):
    r = jacobi_coeffs(mu, nmax + 1)
    b = np.sqrt(r.b2) if hasattr(r, "b2") else np.asarray(r.b)
    res[name] = np.asarray(b)
for n in (100, 200, 400, 800, 1600, 3200):
    out = []
    for name in ("true", "smooth"):
        b = res[name][:n]
        j = np.arange(1, n + 1)
        Dn = 2.0 / n**2 * np.sum((n - j) * np.log(b / xt[:n])) - np.log(np.pi**2 / 16)
        out.append(Dn)
    print(f"   n={n:5d}: D_true = {out[0]:+.5f}   D_smooth = {out[1]:+.5f}   difference {out[0]-out[1]:+.2e}")

print("[3] stability of D_true(n): J doubling (double) and long double")
def Dtrue(J, prec, ns):
    mu = true_zeta(J)
    r = jacobi_coeffs(mu, max(ns) + 1, prec=prec)
    b = np.sqrt(r.b2) if hasattr(r, "b2") else np.asarray(r.b)
    xt_ = np.sort(1 / (model_zeros(J) ** 2 + 0.25))[::-1]
    out = []
    for n in ns:
        j = np.arange(1, n + 1)
        out.append(2.0 / n**2 * np.sum((n - j) * np.log(np.asarray(b[:n], float) / xt_[:n])) - np.log(np.pi**2 / 16))
    return out
ns3 = [100, 400, 1600]
for J, prec in ((100_000, 'd'), (200_000, 'd'), (400_000, 'd'), (200_000, 'ld')):
    print(f"   J={J:7d} {prec:2s}: " + "  ".join(f"n={n}: {v:+.6f}" for n, v in zip(ns3, Dtrue(J, prec, ns3))))
