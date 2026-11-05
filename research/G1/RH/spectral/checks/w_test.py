"""JZC_W §2, step 2: Jacobi coefficients of the test measures, fitted, against the predictions written earlier by w_predict.py
(tmp/w_cache/predictions.json; Rule X: that file must predate the measure caches, which this script verifies by mtime).
For each target exponent e: subtract W's predicted terms of order < e, fit the n^-e coefficient with the next exponents of
{i + jp} as nuisance (plus n^-e' log n at resonant e' >= e), windows n >= 100, 200, 400, 3..6 exponents; report median and
half-range. Pass: |fit - W| <= max(3 half-ranges, 2e-6 (1 + |W|)).  Alternatives (pieces of W switched off) are reported in
tolerances; an alternative is "excluded" when it misses by > 10 tolerances.
Usage: w_test.py KEY [KEY ...]   (keys of w_spectra.SPECTRA)."""
import os, sys, json, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from w_common import run_measure, fit_target, WC, Checks
from w_spectra import SPECTRA
P = json.load(open(WC / 'predictions.json')); tpred = os.path.getmtime(WC / 'predictions.json')
C_ = Checks()
for key in sys.argv[1:]:
    t0 = time.time(); spec, lam, wts, tails = SPECTRA[key](); rec = P[key]; p = rec['p']
    fresh = not any(f.name.startswith(spec['tag'] + "__") for f in WC.iterdir())
    n, y, fname = run_measure(spec['tag'], lam, wts, p, tails)
    tm = os.path.getmtime(WC / fname)
    print(f"=== {key}: {spec['name']}  (measure {fname}, {'generated now' if fresh else 'cached'}, "
          f"{len(lam)} atoms + tail {tails}; {time.time() - t0:.0f} s) ===")
    C_.check(f"{key} Rule X: predictions predate the measure", tm > tpred)
    pred = {float(e): float(mp.mpf(v)) for e, v in rec['pred'].items()}
    for e in rec['targets']:
        e = round(float(e), 6); v, hr = fit_target(n, y, p, e, pred, rec['logexps'])
        w = pred.get(e, 0.0); tol = max(3*hr, 2e-6*(1 + abs(w)))
        ok = C_.check(f"{key} n^-{e}", abs(v - w) <= tol)
        alts = []
        for name, av in rec['alt'].items():
            a = float(mp.mpf(av[str(e)])) if str(e) in av else w
            if abs(a - w) > 1e-12: alts.append(f"{name}: {a:+.6f} ({abs(v - a)/tol:.0f} tol)")
        print(f"  n^-{e:<5}: fit {v:+.8f} (half-range {hr:.1e})  W {w:+.8f}  diff {v - w:+.1e}  tol {tol:.1e}  "
              f"{'PASS' if ok else 'FAIL'}" + (f"   | alternatives: " + "; ".join(alts) if alts else ""), flush=True)
C_.finish()
