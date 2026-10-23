"""REFIT (REFIT.md): SPEC §3.5 (spec_kappa_fit, spec_mobius_pred) re-run on corrected data. NUMERICAL (Rule N).
These are the SPEC results with the largest defect (a): spec_common.run gives lam_k = k^p + kappa a pure-power tail beyond
K = 200 nmax = 320000, a relative node error kappa/K^p = 5e-4 (p = 0.6) and 2.2e-2 (p = 0.3) in the tail. Old data: the spectral_cache
(kappa) and plan62_cache (lattice) files; new: refit_data.fam_kappa / fam_hurwitz at the same K. Analysis copied verbatim."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import run, c_p_mp, NMAX, load_raw
from so_coeffs import coeffs
from so_fit import sequences
import refit_data as RD, w2_common as W2C_
for f in (__file__, RD.__file__, RD.W2D.__file__): W2C_.provenance(f)
K = 200*NMAX


def newab(tag, p, fam):
    RD.run(tag, p, fam, K, NMAX)
    fn = [f for f in os.listdir(RD.RC) if f.startswith(tag + "__") and f.endswith('.txt')][0]
    rows = [l.split() for l in open(os.path.join(RD.RC, fn))]
    with mp.workdps(40):
        al = [mp.mpf(r[1]) for r in rows[:NMAX]]; b = [mp.sqrt(mp.mpf(r[2])) for r in rows[1:NMAX + 1]]
    return np.array(al, dtype=object), np.array(b, dtype=object)


def Lfit(n, y, y0, p):                         # spec_kappa_fit.py, verbatim
    F = n**p*(y - y0); est = []
    E_all = sorted({round(i + j*p, 9) for i in range(4) for j in range(8)} - {0.0})
    for J in (3, 4, 5, 6):
        E = E_all[:J]
        for lo in (100, 200, 400):
            m = n >= lo
            A = np.vstack([np.ones(m.sum())] + [n[m]**-e for e in E]).T
            est.append(np.linalg.lstsq(A, F[m], rcond=None)[0][0])
    est = np.array(est); return np.median(est), (est.max() - est.min())/2


for p, kap in ((0.6, 1.0), (0.3, 1.0)):
    s = 2.0; k = np.arange(1, K + 1, dtype=np.float64); c = float(c_p_mp(p))
    n, yo = run(f"kappa_p{p}_s{s}_k{kap}", k**p + kap, p, s, 0.0, K)
    al0o, b0o = coeffs(p, s, K, NMAX); _, y0o, *_ = sequences(p, al0o, b0o)
    _, b1o = load_raw(f"kappa_p{p}_s{s}_k{kap}")
    al0n, b0n = newab(f"lat_p{p}_s{s}_d0.0_K{K}", p, RD.fam_hurwitz(p, s))
    al1n, b1n = newab(f"kap_p{p}_s{s}_k{kap}", p, RD.fam_kappa(p, 0, kap, s))
    _, yn, *_ = sequences(p, al1n, b1n); _, y0n, *_ = sequences(p, al0n, b0n)
    cand = -2*(2 - p)*c*kap
    for lab, y, y0 in (('old', yo, y0o), ('new', yn, y0n)):
        L, hr = Lfit(n, np.array(y, float), np.array(y0, float), p)
        print(f"p={p} kappa={kap} {lab}: L = {L:+.5f} (half-range {hr:.1e})  candidate {cand:+.5f}  ratio {L/cand:.4f}", flush=True)
    dy = [abs(float(yo[m - 1]) - float(yn[m - 1])) for m in (50, 200, 800, 1500)]
    dy0 = [abs(float(y0o[m - 1]) - float(y0n[m - 1])) for m in (50, 200, 800, 1500)]
    print(f"   |dy| kappa measure at n = 50, 200, 800, 1500: {', '.join(f'{v:.1e}' for v in dy)}; lattice: {', '.join(f'{v:.1e}' for v in dy0)}")
    T = lambda al: np.concatenate([[0.0], np.cumsum([float(a) for a in al])])
    for lab, al0, b0, b1 in (('old', al0o, b0o, b1o), ('new', al0n, b0n, b1n)):
        Tm = T(al0); G = lambda m: -2*kap*(m - 1)*Tm[m]
        rat = []
        for m in (50, 200, 800, 1500):
            meas = float(2*mp.log(b1[m - 1]/b0[m - 1])); pred = G(m + 1) - 2*G(m) + G(m - 1); rat.append(meas/pred)
        print(f"   mobius ratio ({lab}) at n = 50, 200, 800, 1500: {', '.join(f'{r:.6f}' for r in rat)}", flush=True)
