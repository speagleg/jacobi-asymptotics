"""Plan 21 NUMERICAL sanity (Odlyzko's first 2,001,052 zeros; run from the main checkout, which has data/raw):
the Fejér-weighted pair statistic of RHPRIME.md, S_Ψ/N_Ψ with Ψ(γ,γ′) ≈ φ((γ+γ′)/2), φ(t) = sinc²(κt/2), κ = 1/T,
versus the value 1 + D(λ) predicted by Lemma PC_Ψ under RH + (V⁺) with equality (GUE / SPC).
Unfolding: (a) fixed scale L = log T/2π (as in the theorem); (b) local density log(γ̄/2π)/2π. Not a proof."""
import sys, numpy as np
sys.path.insert(0, "src")
from jacobi_asym.measures.lfun import load_odlyzko

g = np.sort(np.asarray(load_odlyzko(), float))

def K(xi, lam):
    xi = np.asarray(xi, float); a = 1 / (2 * lam)
    def S0(x):
        out = np.full_like(x, 2 * lam); m = np.abs(x) > 1e-12
        out[m] = np.sin(2 * np.pi * lam * x[m]) / (np.pi * x[m]); return out
    return (S0(xi) + 0.5 * S0(xi - a) + 0.5 * S0(xi + a)) / (2 * lam)

Dvals = {0.5: 0.7067, 1.0: 0.1560, 2.0: 0.02382}   # from check_spectral_sg.out [1]
print(f"zeros: {g.size}, γ_max = {g[-1]:.0f}")
for T in [2e4, 5e4, 1e5]:
    kap = 1 / T; L = np.log(T) / (2 * np.pi)
    phi = lambda t: np.sinc(kap * t / (2 * np.pi)) ** 2          # np.sinc(x) = sin(πx)/(πx)
    NPsi = np.sum(phi(g))
    for lam in [0.5, 1.0, 2.0]:
        Sa = NPsi; Sb = NPsi; close_a = 0.0
        for k in range(1, 400):
            d = g[k:] - g[:-k]; gm = (g[k:] + g[:-k]) / 2; w = phi(gm)
            ua = d * L; ub = d * np.log(gm / (2 * np.pi)) / (2 * np.pi)
            if ua.min() > 60 and ub.min() > 60: break
            Sa += 2 * np.sum(w * K(ua, lam) ** 2 * (ua <= 60))
            Sb += 2 * np.sum(w * K(ub, lam) ** 2 * (ub <= 60))
        print(f"T={T:7.0f} λ={lam:3.1f}  N_Ψ={NPsi:10.1f} (πN(T)={np.pi*T*np.log(T/(2*np.pi*np.e))/(2*np.pi):10.1f})  "
              f"S_Ψ/N_Ψ: fixed-L {Sa/NPsi:.4f}, local {Sb/NPsi:.4f}   1+D = {1+Dvals[lam]:.4f}   tail φ(γ_max)={phi(g[-1]):.1e}")
