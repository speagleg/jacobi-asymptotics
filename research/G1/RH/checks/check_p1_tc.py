"""p = 1, r = 3/2 vs Tricomi-Carlitz (alpha = 1) (NUMERICAL).  Run from the repo root.
Both measures go through the SAME pipeline (atoms 1/k for k <= K, plus a Gauss-Legendre log-panel quadrature tail up to
tend), so the tail-cutoff bias cancels in the comparison; the TC pipeline is also validated against TC's exact
coefficients (lam(m) = 1/(m+1), folded: a_j = lam(2j-2)+lam(2j-1), b_j^2 = lam(2j-1) lam(2j)).
sigma masses: k^{-3/2}.  TC masses: v_k = k^{k-1} e^{-k}/k!, log v(t) evaluated in Stirling form for t > 1e3
(-(3/2)log t - (1/2)log(2 pi) - 1/(12t) + 1/(360 t^3)) to avoid catastrophic cancellation.
[1] weight ratio ours/TC = k! e^k / k^{k+1/2} -> sqrt(2 pi)(1 + 1/(12k) + ...)
[2] pipeline validation: b_TC(pipeline)/b_TC(exact) - 1   (bias from the tail cutoff; reported for tend = 1e12, 1e16)
[3] sigma vs TC through the same pipeline: n^2 (b_sigma/b_TC - 1), n^2 (a_sigma/a_TC - 1): expected O(1) (O(n^-2) deviation)."""
import math
import numpy as np
import mpmath as mp
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs


def logv(t):
    t = np.asarray(t, float)
    small = t <= 1e3
    out = np.empty_like(t)
    ts = t[small]
    out[small] = (ts - 1) * np.log(ts) - ts - np.array([math.lgamma(v + 1) for v in ts])
    tl = t[~small]
    out[~small] = -1.5 * np.log(tl) - 0.5 * np.log(2 * np.pi) - 1 / (12 * tl) + 1 / (360 * tl ** 3)
    return out


def measure(kind, K, tend, ratio=1.02, k=8):
    kk = np.arange(1, K + 1, dtype=float)
    lw = (-1.5 * np.log(kk)) if kind == "sigma" else logv(kk)
    e = np.arange(np.log(K + 0.5), np.log(tend), np.log(ratio))
    g, gw = np.polynomial.legendre.leggauss(k)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * g for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    lwT = (-1.5 * np.log(T)) if kind == "sigma" else logv(T)
    return DiscreteMeasure.from_atoms(1 / kk, np.exp(lw), tail=(1 / T, W * T * np.exp(lwT)))


for kk in (1, 10, 100, 1000):
    rat = mp.factorial(kk) * mp.e ** kk / mp.power(kk, kk + mp.mpf(1) / 2)
    print(f"[1] k={kk}: ratio = {mp.nstr(rat, 10)}   sqrt(2pi)(1+1/(12k)) = {mp.nstr(mp.sqrt(2*mp.pi)*(1+mp.mpf(1)/(12*kk)), 10)}")
M, K = 1500, 200_000
lam = lambda m: 0.0 if m == 0 else 1.0 / (m + 1)
j = np.arange(1, M + 1)
aX = np.array([lam(2 * t - 2) + lam(2 * t - 1) for t in j]); bX = np.sqrt([lam(2 * t - 1) * lam(2 * t) for t in j])
res = {}
for tend in (1e12, 1e16):
    for kind in ("tc", "sigma"):
        jc = jacobi_coeffs(measure(kind, K, tend), M + 1, prec="ld")
        res[(kind, tend)] = (np.asarray(jc.a, float)[:M], np.asarray(jc.b, float)[:M])
NS = (50, 200, 800, 1500)
for tend in (1e12, 1e16):
    aT, bT = res[("tc", tend)]
    print(f"[2] tend={tend:.0e}: b_TC(pipeline)/b_TC(exact) - 1 at n={NS}: " + " ".join(f"{bT[n-1]/bX[n-1]-1:+.2e}" for n in NS))
for tend in (1e12, 1e16):
    aT, bT = res[("tc", tend)]; aS, bS = res[("sigma", tend)]
    print(f"[3] tend={tend:.0e}: n^2(b_s/b_TC-1) = " + " ".join(f"{n*n*(bS[n-1]/bT[n-1]-1):+.4f}" for n in NS)
          + "   n^2(a_s/a_TC-1) = " + " ".join(f"{n*n*(aS[n-1]/aT[n-1]-1):+.4f}" for n in NS))
