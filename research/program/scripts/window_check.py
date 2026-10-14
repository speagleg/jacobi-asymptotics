"""NUMERICAL: window-restricted ||Δ²μ_N|_{[aN,bN]}||_1 (p=s=2) and the phase-model prediction (8/π)∫_{W} sin²θ dν_arcsine,
y = N^p x ∈ [0,4c], y = 2c(1+cos θ); k/N = y^{-1/p}."""
import numpy as np, sys
sys.path.insert(0, "/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/src")
from jacobi_asym.laws.weyl import c_p
exec(open("bessel_check.py").read().split("rng =")[0])
p = 2.0; c = c_p(p); print("c(2) =", c, " head edge k/N >= (4c)^{-1/p} =", (4*c)**(-1/p))
N = 240; K = 40*N; k = np.arange(1, K+1, dtype=float)
a, b, Q = lanczos(k**-p, k**-2.0, N+4); mu = Q**2
th = np.linspace(1e-6, np.pi-1e-6, 200001)
for (lo, hi) in [(0.6, 1.6), (0.6, 4.0), (1.0, 2.0)]:
    obs = [np.abs((mu[n]-2*mu[n-1]+mu[n-2])[int(lo*n):int(hi*n)]).sum() for n in range(N, N+4)]
    y = 2*c*(1+np.cos(th)); u = y**(-1/p); m = (u >= lo) & (u <= hi)
    pred = (8/np.pi)*np.trapezoid(np.sin(th)**2*m, th)/np.pi
    out = sum(mu[N][:int(lo*N)]) + sum(mu[N][int(hi*N):])
    print(f"W=[{lo}N,{hi}N]: obs {np.round(obs,3)}  pred {pred:.3f};  μ_N mass outside W {out:.3f}")
