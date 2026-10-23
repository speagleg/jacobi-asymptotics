"""REFIT (REFIT.md): SPEC §3.15 row p = 2, s = 2, m = 1 (S = -W(1) = -pi^2/8 "to 1e-6", spec_subpole.out) re-run on corrected data.
Old: spec_common.run (lam_k = (k + g/k)^2, float64, pure-power tail) and the Plan 62 lattice; new: refit_data with the exact lam(t),
m(t) = lam(t)^{-s/p} in the tail, K = 160000, nmax = 1600. Analysis copied verbatim from spec_subpole.py. NUMERICAL (Rule N)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import run, NMAX, c_p_mp
from so_coeffs import coeffs
from so_fit import sequences
import refit_data as RD, w2_common as W2C_
for f in (__file__, RD.__file__): W2C_.provenance(f)
p, s, m = 2.0, 2.0, 1.0; K = 100*NMAX; k = np.arange(1, K + 1, dtype=np.float64)


def fam_g(g):
    P, S, G = mp.mpf(p), mp.mpf(s), mp.mpf(g)
    lam = lambda t: (mp.mpf(t) + G*mp.mpf(t)**(-1))**P; w = lambda t: lam(t)**(-S/P)
    return lam, w, lam, w, s


def analyse(y0, Y, n):
    D = {g: n*(Y[g] - y0) for g in Y}
    A = lambda g: (D[g] - D[-g])/2
    a1 = (8*A(0.25) - A(0.5))/1.5
    mp.mp.dps = 30; c = c_p_mp(p); pm = mp.mpf(p); mm = mp.mpf(m)
    W = lambda q: (4*c)**q*mp.gamma(q + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(q + 1))
    q, q1 = mm/pm, (mm + 1)/pm
    lead = float(-mm*W(q)*mp.pi*mp.cot(mp.pi*q))
    R = a1 - lead*n**(-m)
    for j in range(1, int(np.ceil(3.5/p))):
        arg = 1 + mm - pm*j
        if abs(arg - 1) < 1e-12: continue
        cj = float(pm*W(j)*pm*j*mp.zeta(arg)); R = R - cj*n**(-j*p)
    tgt = 1 + m
    pool = sorted({round(e, 9) for e in [tgt, tgt + 1, 1 + m + p, 1 + p, 1 + 2*p, 2 + p, m + p, 2 + m + p, 3 + m] if e > m + 1e-9})
    res = []
    for lo in (200, 400):
        for J in (4, 5, 6):
            E = [e for e in pool if e != tgt][:J - 1] + [tgt]
            sel = n >= lo; Am = np.vstack([n[sel]**-e for e in E]).T
            co = np.linalg.lstsq(Am, R[sel], rcond=None)[0]; res.append(co[E.index(tgt)])
    res = np.array(res); jac = -float(mm*pm*q1*W(q1)/2); shift = lead*(1 + m + p)*(-(s - 1)/2)/p
    mp.mp.dps = 40
    return float(np.median(res)), float((res.max() - res.min())/2), jac + shift


al, b = coeffs(p, s, K, NMAX); n, y0o, *_ = sequences(p, al, b); n = n.astype(float)
Yo = {g: np.array(run(f"pole_p{p}_s{s}_g{g}_m{m}", (k + g*k**(-m))**p, p, s, 0.0, K)[1], float) for g in (0.25, -0.25, 0.5, -0.5)}
_, y0n = RD.run(f"lat_p{p}_s{s}_d0.0", p, RD.fam_hurwitz(p, s), K)
Yn = {g: np.array([float(v) for v in RD.run(f"gam_p{p}_s{s}_g{g}_m{m}", p, fam_g(g), K)[1]]) for g in (0.25, -0.25, 0.5, -0.5)}
y0n = np.array([float(v) for v in y0n])
for lab, y0, Y in (('old', np.array(y0o, float), Yo), ('new', y0n, Yn)):
    S, hr, pred = analyse(y0, Y, n)
    print(f"p=2 s=2 m=1 {lab}: S = {S:+.9f} (half-range {hr:.1e})  prediction {pred:+.9f} (= -pi^2/8 = {-np.pi**2/8:+.9f})  S - pred = {S - pred:+.2e}", flush=True)
