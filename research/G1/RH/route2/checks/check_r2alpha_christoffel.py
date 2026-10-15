"""Plan 52 (NUMERICAL): direct check of the Christoffel transfer (ROUTE2_alpha.md §2, Lemma CT) on truncated measures.
sigma_s := sum_{k<=K} k^{-s} Psi(k) delta_{k^{-p}};  x * sigma_s = sigma_{s+p} EXACTLY (also after truncation).
Index convention (toolkit): monic x P_n = P_{n+1} + al_n P_n + be_n P_{n-1}, al_n = a[n], be_n = b2[n-1].
Lemma CT: g_0 = al_0, g_n = al_n - be_n/g_{n-1} (g_n = -P_{n+1}(0)/P_n(0) > 0), h_n := al_n - g_n (h_0 = 0); then
  al~_n = g_n + h_{n+1},  be~_n = g_n h_n   are the coefficients of x*sigma.
[1] mpmath RKPW (Gautschi's OPQ `lanczos` = Gragg-Harrod, written out below; dps 60) for sigma_s and sigma_{s+p},
    K = 1200, n <= 300: max relative error of the transfer, and min g_n, min h_n (positivity, Lemma CP). (A first version
    used the discretized Stieltjes procedure, which loses many digits per step for these clustered atoms and gave O(1)
    "errors" even at dps 250 for p = 2: an artefact of the coefficient computation, not of Lemma CT.)
[2] binary128 RKPW (prec 'q'), K = 40000, n <= 600: same comparison; the atoms/weights are passed to the kernel in
    double, so the two measures agree only to ~1e-16 relative and that is the expected floor.
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan52/research/G1/RH/route2/checks/check_r2alpha_christoffel.py"""
import mpmath as mp
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.jacobi.mp import jacobi_mp


def transfer(al, be, n):
    """al[0..n], be[0..n-1] (be[i] = be_{i+1}) -> (al~[0..n-1], be~[0..n-2]) via Lemma CT."""
    g = [al[0]]
    for i in range(1, n + 1):
        g.append(al[i] - be[i - 1] / g[i - 1])
    h = [al[i] - g[i] for i in range(n + 1)]
    at = [g[i] + h[i + 1] for i in range(n)]
    bt = [g[i] * h[i] for i in range(1, n)]  # be~_i, i = 1..n-1  -> list index i-1
    return at, bt, g, h


def logpsi(k, kind):
    if kind == "1":
        return 0.0 * k
    return np.sqrt(np.log(k + np.e))


def measure(K, s, p, kind, mpw=False):
    k = np.arange(1, K + 1, dtype=float)
    if mpw:
        x = [mp.mpf(int(i)) ** (-p) for i in range(1, K + 1)]
        w = [mp.mpf(int(i)) ** (-s) * (mp.e ** mp.sqrt(mp.log(i + mp.e)) if kind != "1" else 1) for i in range(1, K + 1)]
        return x, w
    lw = -s * np.log(k) + logpsi(k, kind)
    return DiscreteMeasure(k ** -p, np.exp(lw - lw.max()))


def rkpw_mp(x, w, n):
    """Gragg-Harrod / Gautschi OPQ lanczos.m in mpmath. Returns (a[0..n-1], b2[0..n-1]) in the toolkit convention."""
    Nc = len(x); p0 = list(x); p1 = [mp.mpf(0)] * Nc; p1[0] = w[0]
    for m in range(Nc - 1):
        pn = w[m + 1]; gam = mp.mpf(1); sig = mp.mpf(0); tt = mp.mpf(0); xlam = x[m + 1]
        for k in range(m + 2):
            rho = p1[k] + pn; tmp = gam * rho; tsig = sig
            if rho <= 0:
                gam, sig = mp.mpf(1), mp.mpf(0)
            else:
                gam, sig = p1[k] / rho, pn / rho
            tk = sig * (p0[k] - xlam) - gam * tt
            p0[k] = p0[k] - (tk - tt); tt = tk
            pn = tsig * p1[k] if sig <= 0 else tt ** 2 / sig
            p1[k] = tmp
    return p0[:n], p1[1:n + 1]


print("[1] mpmath RKPW dps=60, K=1200, n=300 (exact-arithmetic identity up to rounding)")
mp.mp.dps = 60
K, n = 1200, 300
for p, s, kind in ((2.0, 3.0, "1"), (2.0, 3.0, "sqrtlog"), (1.5, 2.5, "sqrtlog"), (0.5, 1.5, "1")):
    x, w = measure(K, s, p, kind, mpw=True)
    a, b2 = rkpw_mp(x, w, n + 2)
    xs = x; ws = [w[i] * x[i] for i in range(K)]
    a2, b22 = rkpw_mp(xs, ws, n + 1)
    at, bt, g, h = transfer(a, b2, n)
    ea = max(abs(at[i] / a2[i] - 1) for i in range(n))
    eb = max(abs(bt[i] / b22[i] - 1) for i in range(n - 1))
    print(f"  p={p} s={s} Psi={kind}: max|a~/a(s+p)-1|={mp.nstr(ea, 3)}  max|b~^2/b^2(s+p)-1|={mp.nstr(eb, 3)}  "
          f"min g={mp.nstr(min(g), 3)} min h(n>=1)={mp.nstr(min(h[1:]), 3)}", flush=True)

print("[2] binary128 RKPW, K=40000, n=600")
K, n = 40000, 600
for p, s, kind in ((2.0, 3.0, "1"), (2.0, 4.0, "sqrtlog"), (2.0, 5.0, "1")):
    with mp.workdps(40):
        r1 = jacobi_coeffs(measure(K, s, p, kind), n + 2, prec="q")
        r2 = jacobi_coeffs(measure(K, s + p, p, kind), n + 1, prec="q")
        at, bt, g, h = transfer(list(r1.a), list(r1.b2), n)
        ea = max(abs(at[i] / r2.a[i] - 1) for i in range(n))
        eb = max(abs(bt[i] / r2.b2[i] - 1) for i in range(n - 1))
        print(f"  p={p} s={s}->{s+p} Psi={kind}: max|a~/a-1|={mp.nstr(ea, 3)}  max|b~^2/b^2-1|={mp.nstr(eb, 3)}  "
              f"min g={mp.nstr(min(g), 3)} min h(n>=1)={mp.nstr(min(h[1:]), 3)}", flush=True)
