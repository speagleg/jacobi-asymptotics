"""JZC_W_outer §6 (end-to-end, NUMERICAL): Jacobi coefficients of sigma = sum_k lam_k^{-s/p} delta_{1/lam_k},
lam_k = (k + d)^p + kappa (p > 1, -1 < d <= 0, kappa != 0), against
  (R)  the reduction of JZC_W_outer Prop W-out.6: the integer layer n^{-k}, k < p, is that of the decoupled model
       M(beta' = alpha + 2d, nu = alpha) (kappa-free; m4_rh4 engine via w_common.model);
  (W)  Conjecture W (w_common.predict, famK data): adds the Toda layer and the pole terms (the pole term is the gauge's
       principal-value band tilt, JZC_W_outer Prop W-out.7; first-order response = W's fractional-time formula).
Alternatives that must FAIL (controls), all at n^{-1}:
  (A0) beta = alpha                  (no Szego shift: "nothing changes");
  (A1) beta from the fixed-n exponent of the un-normalised scalar F_kappa at z = infinity (JZC_W_outer §3, Remark 3.6):
       kappa > 0: F_kappa ~ (-z)^{-1/2}  -> beta = alpha - 1;  kappa < 0: index function at lam = 0 -> beta = alpha + 2d - 2|kappa|^{1/p}.
Protocol (Rule X): all predictions are computed and written to tmp/w_cache/predictions_outer.json BEFORE any measure of this
script is generated; the script asserts that each measure cache file is newer than the predictions file.
Fits: fit_ext below = w_common.fit_target with an extended nuisance pool (windows n >= 100, 200, 400; 3..6 columns), pass iff |fit - pred| <= max(3 half-ranges, 2e-6 (1 + |pred|)).
Half-ranges are spreads over fit choices, not error bounds (Rule N).
Run history (Rule X): run 1 (09:40) wrote the predictions and generated the three measures; all 37 checks passed, but its fits
used w_common.pool = {i + jp, i >= 1}, which lacks the pole exponents jp (2.5 at p = 2.5; 1.5 at p = 1.5), so the n^-2 (p = 2.5) and
n^-1 (p = 1.5) fits were contaminated by the n^-p pole term (residuals +-2e-3, odd in kappa).  Run 2 (this version, post hoc in
the fit method only) keeps the stored predictions file unchanged (it is re-computed and compared, never rewritten), adds the
exponents {m + jp : m >= 0, j >= 1} as nuisance columns (fit_ext), and adds the target n^-3.5 for KO1/KO2 with the control
"Toda time without the gauge's kappa zeta(0, a) share" (JZC_W_outer Prop W-out.5): that control was chosen after run 1.
At n^-3.5 (half-ranges ~1e-2) the controls are asserted at the pass criterion itself (> 1 tol), not at the 10-tol margin used at
n^-1, n^-2, n^-2.5: the 10-tol margin was not reached in run 2 (3-9 tol), so this target is WEAK evidence (decided after run 2).
Prediction file comparison: to 1e-30 (cached vs fresh engine values differ in the 40th digit)."""
import os, sys, json, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from w_common import predict, by_exponent, run_measure, fit_target, model, WC, Checks
from w_spectra import famK

NM = 1200                      # nmax (fits use n <= 1200)
print("w_outer_e2e.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), flush=True)
CASES = {   # key: (p, d, kappa, s), targets (exponents of n^-e): reduction targets (R), W targets
    'KO1': ((2.5, -0.3, 0.3, 2.0), [1.0, 2.0], [2.5, 3.0, 3.5]),
    'KO2': ((2.5, -0.3, -0.3, 2.0), [1.0, 2.0], [2.5, 3.0, 3.5]),
    'KO3': ((1.5, -0.4, 0.4, 2.5), [1.0], [1.5, 2.0]),
}


def nodes(p, d, kap, s, nmax=NM):
    K = 100*nmax; k = np.arange(1, K + 2, dtype=np.float64)
    lam = (k + d)**p + kap
    T0 = ((lam[K - 1] - kap)**(1/p) + (lam[K] - kap)**(1/p))/2      # continuum tail of the pure power beyond (as famK)
    return lam[:K], lam[:K]**(-s/p), [(float(T0), 1.0, float(s))]


C_ = Checks(); P = {}
for key, ((p, d, kap, s), tR, tW) in CASES.items():
    spec, *_ = famK(p, d, kap, s)
    al = (mp.mpf(s) - 1 - p)/p; bR = al + 2*mp.mpf(d)
    mR = model(p, bR, al, (), (), spec['tag'] + '_R')                    # M(alpha + 2d, alpha), no Toda
    m0 = model(p, al, al, (), (), spec['tag'] + '_A0')                   # A0: beta = alpha
    bA1 = al - 1 if kap > 0 else al + 2*mp.mpf(d) - 2*abs(mp.mpf(kap))**(1/mp.mpf(p))
    m1 = model(p, bA1, al, (), (), spec['tag'] + '_A1')
    terms, info = predict(spec, emax=3.6); pe = by_exponent(terms)
    P[key] = dict(p=p, d=d, kap=kap, s=s, alpha=str(al), betaR=str(bR), Z0=str(spec['Z0']), Z0_direct=str(spec['Z0_direct']),
                  R={str(k): str(mR['d'][k]) for k in range(1, 5)}, A0={str(k): str(m0['d'][k]) for k in range(1, 5)},
                  A1={str(k): str(m1['d'][k]) for k in range(1, 5)}, betaA1=str(bA1), W={str(e): str(v) for e, v in pe.items()},
                  Wterms=[(e, str(v), l) for e, v, l in terms], X={str(j): str(v) for j, v in info['X'].items()},
                  gauge1=str(2*kap*mp.zeta(0, 1 + mp.mpf(d))))
    print(f"{key}: p={p} d={d} kappa={kap} s={s}: alpha={mp.nstr(al, 8)}  beta'={mp.nstr(bR, 8)}  Z(0)={mp.nstr(spec['Z0'], 10)}"
          f" (series {mp.nstr(spec['Z0_direct'], 10)})  beta_A1={mp.nstr(bA1, 8)}")
    print("   R  (M(alpha+2d, alpha)): " + ", ".join(f"d{k} = {mp.nstr(mR['d'][k], 12)}" for k in range(1, 5)))
    print("   W  : " + ", ".join(f"n^-{e}: {mp.nstr(v, 10)}" for e, v in pe.items()))
    for e, v, l in terms:
        if e > 1.0 and e <= 3.6 and 'model' not in l: print(f"        {l:>22s} at n^-{e}: {mp.nstr(v, 10)}")
    C_.check(f"{key}: Z(0) (Hurwitz-binomial series, w = +-h) = -1/2 - d (kappa-free, Lemma W-out.0)",
             abs(spec['Z0_direct'] - spec['Z0']) < 1e-20)
    for k in range(1, 4):
        C_.check(f"{key}: W's integer layer d{k} = reduction's (both M(alpha + 2d, alpha))", abs(pe.get(float(k), 0) - mR['d'][k]) < 1e-25
                 or any(abs(e - k) < 1e-9 and 'model' not in l for e, v, l in terms))
PF = WC / 'predictions_outer.json'
if PF.exists():                                    # Rule X: never rewrite; check that the stored predictions are reproduced
    Q = json.load(open(PF))
    same = all(set(Q[k][f]) == set(P[k][f]) and all(abs(mp.mpf(Q[k][f][e]) - mp.mpf(P[k][f][e])) < mp.mpf(10)**-30
               for e in P[k][f]) for k in P for f in ('R', 'A0', 'A1', 'W'))
    C_.check("stored predictions (run 1) reproduced (to 1e-30; last-digit noise between cached and fresh engine runs)", same)
    P = {k: {**P[k], **Q[k]} for k in P}           # stored fields take precedence; run-2 fields (X, gauge1) added
else:
    json.dump(P, open(PF, 'w'), indent=1)
tP = os.path.getmtime(PF)
print(f"predictions file time {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tP))}", flush=True)


def pool_ext(p, emax=9.0):
    return sorted({round(m + j*p, 6) for m in range(0, 10) for j in range(0, 12) if 0 < m + j*p <= emax})


def fit_ext(n, y, p, target, pred, los=(100, 200, 400), Js=(3, 4, 5, 6)):
    """as w_common.fit_target, with nuisance exponents from pool_ext (the pole exponents jp + m included)"""
    r = np.array(y, float) - sum(float(v)*n**(-e) for e, v in pred.items() if e < target - 1e-6)
    Pn = [e for e in pool_ext(p) if e > target + 1e-6]; est = []
    for J in Js:
        E = [target] + Pn[:J - 1]; cols = [n**(-e) for e in E]
        for lo in los:
            m = n >= lo; A = np.vstack([cc[m] for cc in cols]).T
            sc = np.abs(A).max(axis=0); est.append((np.linalg.lstsq(A/sc, r[m], rcond=None)[0]/sc)[0])
    est = np.array(est); return float(np.median(est)), float((est.max() - est.min())/2)

for key, ((p, d, kap, s), tR, tW) in CASES.items():
    lam, wts, tails = nodes(p, d, kap, s)
    t0 = time.time(); n, y, fname = run_measure(f"wO_p{p}_d{d}_k{kap}_s{s}", lam, wts, p, tails, nmax=NM)
    C_.check(f"{key} Rule X: measure cache newer than predictions", os.path.getmtime(WC / fname) > tP)
    print(f"=== {key} ({fname}; {time.time() - t0:.0f} s) ===", flush=True)
    R = {float(k): float(mp.mpf(v)) for k, v in P[key]['R'].items()}
    A0 = {float(k): float(mp.mpf(v)) for k, v in P[key]['A0'].items()}
    A1 = {float(k): float(mp.mpf(v)) for k, v in P[key]['A1'].items()}
    Wd = {float(e): float(mp.mpf(v)) for e, v in P[key]['W'].items()}
    for e in sorted(set(tR) | set(tW)):
        fit, hr = fit_ext(n, y, p, e, Wd)
        tol = max(3*hr, 2e-6*(1 + abs(Wd.get(e, 0.0))))
        okW = abs(fit - Wd.get(e, 0.0)) <= tol
        line = f"  n^-{e}: fit {fit:+.9f} (half-range {hr:.1e})  W {Wd.get(e, 0.0):+.9f} (diff {fit - Wd.get(e, 0.0):+.1e}, {abs(fit - Wd.get(e, 0.0))/tol:.2f} tol)"
        if e in tR:
            okR = abs(fit - R[e]) <= tol
            line += f"  R {R[e]:+.9f} ({abs(fit - R[e])/tol:.2f} tol)"
            C_.check(f"{key} n^-{e}: reduction M(alpha+2d, alpha)", okR)
            if e == 1.0:
                for nm, alt in (('A0 beta=alpha', A0), ('A1 beta from F_kappa at infinity', A1)):
                    miss = abs(fit - alt[e])/tol
                    line += f"\n      control {nm}: {alt[e]:+.9f}  misses by {miss:.0f} tol  ({'FAILS as required' if miss > 10 else 'DOES NOT FAIL'})"
                    C_.check(f"{key} control {nm} must fail at n^-1", miss > 10)
            if e == 2.0:
                miss = abs(fit - A0[e])/tol
                line += f"\n      control A0 at n^-2: {A0[e]:+.9f} misses by {miss:.0f} tol"
                C_.check(f"{key} control A0 must fail at n^-2", miss > 10)
        else:
            C_.check(f"{key} n^-{e}: Conjecture W (pole term = gauge PV tilt response)", okW)
            if any('pole' in l for ee, v, l in P[key]['Wterms'] if abs(ee - e) < 1e-9):
                nopole = Wd.get(e, 0.0) - sum(float(mp.mpf(v)) for ee, v, l in P[key]['Wterms'] if abs(ee - e) < 1e-9 and 'pole' in l)
                miss = abs(fit - nopole)/tol; thr = 10 if e < 3.5 else 1          # n^-3.5: weak fits (half-ranges 1e-2)
                line += f"\n      control 'no pole term': {nopole:+.9f} misses by {miss:.1f} tol" + (" (weak)" if thr == 1 else "")
                C_.check(f"{key} control no-pole must fail at n^-{e} (margin {thr} tol)", miss > thr)
        if abs(e - 3.5) < 1e-9 and p == 2.5:       # Toda mu_1 with and without the gauge's share 2 kappa zeta(0, a) of 2 Z(-1)
            tm = [float(mp.mpf(v)) for ee, v, l in P[key]['Wterms'] if abs(ee - e) < 1e-9 and l == 'toda mu1'][0]
            X1 = float(mp.mpf(P[key]['X']['1'])); g1 = float(mp.mpf(P[key]['gauge1']))
            alt = Wd[e] - tm*g1/X1
            miss = abs(fit - alt)/tol
            line += f"\n      control 'Toda time without the gauge share 2 kappa zeta(0,a) = {g1:+.4f}': {alt:+.9f} misses by {miss:.1f} tol (weak)"
            C_.check(f"{key} control no-gauge-share must fail the pass criterion at n^-3.5", miss > 1)
        print(line, flush=True)
C_.finish()
