"""JZC_W §2.4, second probe (pre-registered test of the post-hoc refinement W'): the pole term carries the zeta layer's natural-form
dressing, p R_q W(q) pi cot(pi q) (n/N)^p N^{-1-pq} [1 + g(q) N^-2], g(w) = A(w) + B(w) nu^2 (JZC_M4 §6, Theorem N.6(ii)) continued
from integer j to w = q; at q = 1/2 the product cot * g is finite (0 * infinity).  W' was identified from K2p/K2m/M1 (w_probe.out) and
the Lommel anchor; these two NEW measures test it (predictions saved before the measures are generated):
  K2p_s2   = k^2 + 1/4, s = 2   (alpha = -1/2: W' predicts NO extra n^-4 term, like Lommel)
  K2p_s35  = k^2 + 1/4, s = 3.5 (alpha = 1/4: W' predicts an extra -0.17349 at n^-4)"""
import os, sys, json, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from w_common import predict, by_exponent, run_measure, fit_target, WC, Checks
from w_spectra import famK
print("w_probe2.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), flush=True)
C_ = Checks(); cases = {'K2p_s2': famK(2, 0, 0.25, 2.0), 'K2p_s35': famK(2, 0, 0.25, 3.5)}; pr = {}
for key, (spec, lam, wts, tails) in cases.items():
    t0, _ = predict(spec); t1, _ = predict(spec, variant={'dressing'})
    pr[key] = (by_exponent(t0), by_exponent(t1))
    print(f"{key}: W   " + ", ".join(f"n^-{e}: {mp.nstr(v, 10)}" for e, v in pr[key][0].items() if e <= 4.000001))
    print(f"{key}: W'  " + ", ".join(f"n^-{e}: {mp.nstr(v, 10)}" for e, v in pr[key][1].items() if e <= 4.000001)
          + "   [" + "; ".join(f"{l}: {mp.nstr(v, 8)}" for e, v, l in t1 if 'dress' in l or 'shift2' in l) + "]", flush=True)
json.dump({k: {str(e): str(v) for e, v in v_[1].items()} for k, v_ in pr.items()}, open(WC / 'predictions_probe2.json', 'w'))
tp = os.path.getmtime(WC / 'predictions_probe2.json')
for key, (spec, lam, wts, tails) in cases.items():
    n, y, fname = run_measure(spec['tag'], lam, wts, 2.0, tails)
    C_.check(f"{key} Rule X", os.path.getmtime(WC / fname) > tp)
    print(f"=== {key} ({fname}) ===")
    for e in (1.0, 2.0, 3.0, 4.0):
        w0, w1 = float(pr[key][0].get(e, 0)), float(pr[key][1].get(e, 0))
        v, hr = fit_target(n, y, 2.0, e, {k: float(v) for k, v in pr[key][1].items()}); tol = max(3*hr, 2e-6*(1 + abs(w1)))
        ok = C_.check(f"{key} n^-{e} W'", abs(v - w1) <= tol)
        print(f"  n^-{e}: fit {v:+.8f} ({hr:.1e})  W' {w1:+.8f} (diff {v - w1:+.2e}, {'PASS' if ok else 'FAIL'})   W {w0:+.8f} (diff {v - w0:+.2e}, {abs(v - w0)/tol:.0f} tol)", flush=True)
C_.finish()
