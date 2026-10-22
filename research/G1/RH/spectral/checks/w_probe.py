"""JZC_W §2.4 probe (EXPLORATORY, added after the M1 n^-4 failure; Rule X: the predictions below are computed and saved before the
probe measures are generated, but the probe itself was designed after seeing the failure).
Questions: is the sphere's n^-4 excess (fit - W = +0.2313 ~ 3 pi^2/128) (i) a delta > 0 (phantom node) effect, or (ii) the second
order of the moved Weyl pole (kappa^2 n^-2p at p = 2)?  Measures (p = 2, s = 3, alpha = 0):
  H2  = (k + 1/2)^2                (Hurwitz delta = +1/2, no poles): W vs fit at n^-1..n^-4
  K2p = k^2 + 1/4, K2m = k^2 - 1/4 (moved Weyl pole q = 1/2, cot = 0; density tilt (1 - kappa x)^{-1/2}): W vs fit,
  and the kappa-even part (y(K2p) + y(K2m))/2 - y(lattice k^2) at n^-4, per kappa^2, against 0.2313 * 16 = 3.701 (sphere, kappa = -1/4)."""
import os, sys, json, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from w_common import predict, by_exponent, run_measure, fit_target, WC, Checks
from w_spectra import PROBE, famK
print("w_probe.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), flush=True)
C_ = Checks(); preds = {}
for key, mk in list(PROBE.items()) + [('L2', lambda: famK(2, 0, 0, 3.0))]:
    spec, lam, wts, tails = mk(); t, info = predict(spec); pe = by_exponent(t); preds[key] = (spec, lam, wts, tails, pe, info)
    print(f"{key}: {spec['name']}: Z(0) = {mp.nstr(spec['Z0'], 8)}, Z(-j) = {[mp.nstr(v, 8) for v in spec['Zneg'].values()]}, "
          f"poles {[(float(q), float(R)) for q, R in spec['poles'][:2]]}; mu_j = {{{', '.join(f'{j}: {mp.nstr(v, 8)}' for j, v in info['X'].items())}}}")
    print("   W: " + ", ".join(f"n^-{e}: {mp.nstr(v, 10)}" for e, v in pe.items() if e <= 4.000001), flush=True)
json.dump({k: {str(e): str(v) for e, v in v_[4].items()} for k, v_ in preds.items()}, open(WC / 'predictions_probe.json', 'w'))
tp = os.path.getmtime(WC / 'predictions_probe.json'); Y = {}
for key, (spec, lam, wts, tails, pe, info) in preds.items():
    n, y, fname = run_measure(spec['tag'], lam, wts, 2.0, tails); Y[key] = y
    C_.check(f"{key} Rule X (predictions first)", os.path.getmtime(WC / fname) > tp or key == 'L2')
    pr = {e: float(v) for e, v in pe.items()}
    print(f"=== {key} ({fname}) ===")
    for e in (1.0, 2.0, 3.0, 4.0):
        v, hr = fit_target(n, y, 2.0, e, pr); w = pr.get(e, 0.0); tol = max(3*hr, 2e-6*(1 + abs(w)))
        ok = abs(v - w) <= tol; print(f"  n^-{e}: fit {v:+.8f} ({hr:.1e})  W {w:+.8f}  diff {v - w:+.2e}  {'PASS' if ok else 'FAIL'}", flush=True)
        if e < 4: C_.check(f"{key} n^-{e}", ok)
# kappa-even part
ev = (np.array(Y['K2p'], float) + np.array(Y['K2m'], float))/2 - np.array(Y['L2'], float)
pe_ev = {e: (float(preds['K2p'][4].get(e, 0)) + float(preds['K2m'][4].get(e, 0)))/2 - float(preds['L2'][4].get(e, 0)) for e in (1.0, 2.0, 3.0, 4.0)}
for e in (1.0, 2.0, 3.0, 4.0):
    v, hr = fit_target(n, ev, 2.0, e, pe_ev)
    print(f"  kappa-even part, n^-{e}: fit {v:+.8f} ({hr:.1e})  W (first order) {pe_ev[e]:+.8f}  excess {v - pe_ev[e]:+.6f}"
          + (f"  -> per kappa^2: {(v - pe_ev[e])*16:+.5f} (sphere: {0.23132*16:+.4f}; 3 pi^2/8 = {3*np.pi**2/8:.5f})" if e == 4.0 else ""))
C_.finish()
