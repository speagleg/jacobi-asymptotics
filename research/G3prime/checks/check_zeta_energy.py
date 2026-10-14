"""Plan 31 (NUMERICAL; Odlyzko's first 2,001,052 zeros; run from the main checkout, which has data/raw):
Theorem Ch's criterion on the actual zeta ordinates. With d_ab := (γ_b − γ_a)·log(γ_a/2π)/2π and
P(K) := Σ_{a<b≤K, d_ab<1} log(1/d_ab) (all pairs at normalized distance < 1 are 'near' in the sense of §5.4, since
4C₀ ≫ 1 spacing), 𝒞(K) ≤ P(K) (take T = all indices). Report P(K)/K, 𝒞-bound/K², the GUE prediction
c_GUE := ∫_0^1 log(1/u)(1 − (sin πu/πu)²)du for the per-zero energy, and the smallest normalized gaps."""
import sys, numpy as np
from scipy.integrate import quad
sys.path.insert(0, "src")
from jacobi_asym.measures.lfun import load_odlyzko
g = np.sort(np.asarray(load_odlyzko(), float)); N = g.size
dens = np.log(g/(2*np.pi))/(2*np.pi)
contrib = np.zeros(N)
for m in range(1, 8):
    d = (g[m:] - g[:-m])*dens[:-m]
    mask = d < 1
    np.add.at(contrib, np.nonzero(mask)[0], np.log(1/np.maximum(d[mask], 1e-300)))
    if not mask.any(): break
cGUE = quad(lambda u: np.log(1/u)*(1-(np.sinc(u))**2), 0, 1)[0]
cum = np.cumsum(contrib)
print(f"zeros: {N}; c_GUE = ∫_0^1 log(1/u)(1−sinc²u)du = {cGUE:.5f}")
for K in [10**3, 10**4, 10**5, 10**6, N]:
    print(f"K={K:8d}: P(K)/K = {cum[K-1]/K:.5f}   𝒞(K)/K² ≤ P(K)/K² = {cum[K-1]/K**2:.3e}")
gap = np.diff(g)*dens[:-1]
idx = np.argsort(gap)[:5]
print("smallest normalized gaps: " + ", ".join(f"{gap[i]:.2e} (k={i+1}, γ≈{g[i]:.1f})" for i in idx))
print(f"max single pair energy log(1/d): {np.log(1/gap.min()):.2f};  #gaps<0.05: {np.sum(gap<0.05)}  (GUE expectation ≈ N·(π²/9)·0.05³ = {N*np.pi**2/9*0.05**3:.1f}… pair-count proxy)")
