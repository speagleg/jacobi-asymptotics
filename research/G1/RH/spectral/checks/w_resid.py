"""JZC_W §2, secondary diagnostic (fit-free; reads the caches of w_test.py, no new measures).
For each spectrum and target exponent e: S_n := n^e (y_n - sum_{e' < e} W_e' n^-e') - W_e, at n = 200, 400, 800, 1600. Under W, S_n -> 0
like n^-(e_next - e) (times log n at a resonance); a wrong W_e (or a wrong lower term) leaves a constant offset (or growth).
Reported for W and for each alternative of w_predict (same subtraction with the alternative's coefficients).
Pass criterion (declared with this script, after w_test.py): |S_1600| < |S_400| or |S_1600| < 1e-4 (decay toward 0), for W.
Noise floor (printed, not used in the criterion): sigma_y from the 6th differences of y on n in [1200, 1600] (white-noise variance
924 sigma^2; the smooth part's 6th difference is negligible there), shown as n^e sigma_y at n = 800 and 1600."""
import os, sys, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from w_common import run_measure, WC, Checks
from w_spectra import SPECTRA
P = json.load(open(WC / 'predictions.json')); C_ = Checks()
NS = (200, 400, 800, 1600)
for key in (sys.argv[1:] or list(SPECTRA)):
    spec, lam, wts, tails = SPECTRA[key](); rec = P[key]
    n, y, _ = run_measure(spec['tag'], lam, wts, rec['p'], tails)
    pred = {float(e): float(mp.mpf(v)) for e, v in rec['pred'].items()}
    d6 = np.diff(np.array(y, float)[1199:1600], 6); sig = float(np.std(d6)/np.sqrt(924.0))
    print(f"=== {key}: {spec['name']}  (noise floor sigma_y = {sig:.1e}) ===")
    for e in rec['targets']:
        e = round(float(e), 6)
        def S(pr):
            r = np.array(y, float) - sum(v*n**(-ee) for ee, v in pr.items() if ee < e - 1e-6)
            return [n[k - 1]**e*r[k - 1] - pr.get(e, 0.0) for k in NS]
        s = S(pred); ok = abs(s[-1]) < abs(s[1]) or abs(s[-1]) < 1e-4
        C_.check(f"{key} n^-{e} residual decays", ok)
        line = (f"  n^-{e:<5} W: " + " ".join(f"{v:+.2e}" for v in s) + f"  {'decays' if ok else 'NO DECAY'}"
                + f"  [noise n^e sigma: {800**e*sig:.0e} @800, {1600**e*sig:.0e} @1600]")
        for name, av in rec['alt'].items():
            pa = dict(pred)
            for ee, vv in av.items(): pa[round(float(ee), 6)] = float(mp.mpf(vv))
            if all(abs(pa.get(ee, 0) - pred.get(ee, 0)) < 1e-12 for ee in pa if ee <= e + 1e-6): continue
            sa = S(pa); line += f" | {name}: {sa[-1]:+.2e}"
        print(line, flush=True)
C_.finish()
