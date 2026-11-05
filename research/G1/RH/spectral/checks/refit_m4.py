"""REFIT (REFIT.md): the Plan 62 lattice fits of JZC_M4 §3 (m4_natural_index: the N^-1, N^-2, N^-3 residuals of the natural form) and
of JZC_M3a_H_G1u §5a (m3a_g1u_endtoend, the two beta' = -2.1 Hurwitz cases) re-run on corrected data. NUMERICAL (Rule N).
Old data: so_coeffs.coeffs caches (tmp/plan62_cache: float64 atoms/weights, scipy float64 Gauss-Jacobi tail cut at K + 1/2 + delta,
i.e. the pure power is exact here but the midpoint Euler-Maclaurin defect and defect (b) remain). New data: refit_data.fam_hurwitz
(same K = 160000, nmax = 1600). The analysis code is copied verbatim from m4_natural_index.py / m3a_g1u_endtoend.py.
JZC_M4 §3 attributes the N^-3 residuals (up to 5e-4, ~1.5 spreads, sign flipping with alpha) to data noise at the N^-3/N^-4 scale;
the integer layer's f_3 = 0 is now PROVED-mod-cite (JZC_SIGMA Cor Sigma.1). Here: do the residuals shrink on corrected data?"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
os.environ.setdefault("KORD", "4")
import numpy as np, mpmath as mp
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import NMAX, fit
import refit_data as RD, w2_common as W2C_
import m4_rh4 as M
for f in (__file__, RD.__file__, RD.W2D.__file__): W2C_.provenance(f)


def ynew(p, s, d=0.0, K=160000):
    n, y = RD.run(f"lat_p{p}_s{s}_d{d}", p, RD.fam_hurwitz(p, s, d), K, NMAX)
    return np.array([float(v) for v in y]), y


def natural(n, y, p, s):                      # m4_natural_index.py, verbatim body
    alpha = (s - 1)/p - 1; Z0 = -0.5; N = n + alpha/2 - Z0
    F = (N/n)**p*(1 + y)
    mp.mp.dps = 30; c = c_p_mp(p)
    eps = {j: float(mp.binomial(2*j, j)*p*c**j*mp.zeta(-j*p)) for j in range(1, 6)}
    f2 = -(p + 2)*alpha**2/8 + (p + 1)/12
    R = F - 1 - f2*N**-2.0 - sum(e*N**(-1 - j*p) for j, e in eps.items() if 1 + j*p < 5.5)
    tgt = [1.0, 2.0, 3.0]
    nuis = sorted({round(e, 9) for e in [4.0, 5.0] + [2 + j*p for j in range(1, 4)] + [3 + j*p for j in range(1, 3)] if e < 6.5} - set(tgt))
    out = {e: [] for e in tgt}
    for lo in (200, 400):
        for J in (2, 3, 4):
            E = tgt + nuis[:J]; sel = n >= lo; A = np.vstack([N[sel]**-e for e in E]).T
            co = np.linalg.lstsq(A, R[sel], rcond=None)[0]
            for e in tgt: out[e].append(co[E.index(e)])
    mp.mp.dps = 40
    return {e: (np.median(v), (max(v) - min(v))/2) for e, v in out.items()}, R, N


print("== JZC_M4 §3 (m4_natural_index): residual coefficients, old -> new ==", flush=True)
for p, s in ((1.5, 2.0), (1.5, 3.0), (1.25, 2.0), (2.5, 2.0), (3.0, 2.0), (1.5, 2.5), (2.0, 3.0)):
    al, b = coeffs(p, s, 160000, NMAX); n, yo, *_ = sequences(p, al, b); n = n.astype(float)
    yn, ynm = ynew(p, s)
    mo, Ro, N = natural(n, yo, p, s); mn, Rn, _ = natural(n, yn, p, s)
    dy = [abs(mp.mpf(yo[k - 1]) - ynm[k - 1]) for k in (200, 400, 800, 1200, 1600)]
    tail = lambda R: float(np.std(N[(n >= 600)]**4*R[(n >= 600)]))
    print(f"p={p} s={s}: |dy| at n = 200..1600: {', '.join(mp.nstr(v, 2) for v in dy)};  sd of N^4 R on n >= 600: old {tail(Ro):.1e}, new {tail(Rn):.1e}")
    for e in (1.0, 2.0, 3.0):
        (vo, ho), (vn, hn) = mo[e], mn[e]
        to, tn = max(3*ho, 1e-5), max(3*hn, 1e-5)
        print(f"    N^-{e:g}: old {vo:+.2e} ({ho:.0e}) {'PASS' if abs(vo) <= to else 'FAIL'} | new {vn:+.2e} ({hn:.0e}) {'PASS' if abs(vn) <= tn else 'FAIL'}", flush=True)

print("== JZC_M3a_H_G1u §5a (m3a_g1u_endtoend), beta' = -2.1 cases at K = 160000: old -> new ==", flush=True)
for (p, s, d) in ((1.5, 1.75, -0.8), (3.0, 2.5, -0.8)):
    P = mp.mpf(p); al_ = (mp.mpf(s) - 1 - P)/P; D = mp.mpf(d); bp = al_ + 2*D; c = mp.mpf(c_p_mp(p)); a = 1 + D
    pred = {"d1": -P*(bp + 1)/2, "d2": P*(P + 1)*(bp + 1)**2/8 - (P + 2)*al_**2/8 + (P + 1)/mp.mpf(12)}
    if p == 1.5: pred["eps1"] = 2*P*c*mp.zeta(-P, a)
    if p == 3.0: pred["d3"] = M.run(P, bp, c=c, nu=al_)[0][3]
    alc, b = coeffs(p, s, 160000, 1600, d); n, yo, *_ = sequences(p, alc, b); n = n.astype(float)
    yn, ynm = ynew(p, s, d)
    for lab, y in (('old', yo), ('new', yn)):
        F = {"d1": fit(n, y, p, [], 1.0)}; r = y - float(pred["d1"])/n
        F["d2"] = fit(n, r, p, [1.0], 2.0); r2 = r - float(pred["d2"])/n**2
        if p == 1.5: F["eps1"] = fit(n, r2, p, [1.0, 2.0], 1 + p)
        if p == 3.0: F["d3"] = fit(n, r2, p, [1.0, 2.0], 3.0)
        print(f"  p={p} s={s} d={d} {lab}: " + "; ".join(f"{k} {F[k][0]:+.8f} (hr {F[k][1]:.1e}, pred {float(v):+.8f}, dev {F[k][0] - float(v):+.1e})" for k, v in pred.items()), flush=True)
