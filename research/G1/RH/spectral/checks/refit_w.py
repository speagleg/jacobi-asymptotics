"""REFIT (REFIT.md): JZC_W §2.3-§2.4 (w_test, w_probe, w_probe2) and JZC_W_outer §8 (w_outer_e2e) re-run on corrected data.
NUMERICAL; fits are not error bounds (Rule N). No prediction is recomputed or changed: the stored prediction files of the original
runs (tmp/w_cache/predictions*.json, written before the original measures; Rule X) are read; W' for probe 2 and M1 is recomputed
from w_common.predict(variant={'dressing'}) exactly as w_probe2.py does (cached engine values) and checked against the stored
predictions_probe2.json. The fit routines are the original ones (w_common.fit_target; w_outer_e2e's fit_ext, copied verbatim),
with the original pass rules. The only change is the measure: old = the original cache (w_common.run_measure, float64 atoms and
Gauss rules, pure-power tail beyond the last atom); new = refit_data.py (dps-40 atoms, exact lam(t) and m(t) in the tail, smooth
cut, refined Gauss rules), same nmax and same atom count K.
Reported per target: old fit (half-range), new fit (half-range), the prediction, pass/fail under the original rule; and the data
change D_e = max over n in {200, 400, 800, 1200, nmax} of n^e |y_old - y_new|, and the 6th-difference noise floor sigma_y.
Usage: refit_w.py GROUP   (probe | test | outer)"""
import os, sys, json, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from w_common import run_measure, fit_target, predict, by_exponent, WC, Checks
import w_spectra as WS
import refit_data as RD, w2_common as W2C_
GROUP = sys.argv[1]
for f in (__file__, RD.__file__, RD.W2D.__file__): W2C_.provenance(f)
print(f"refit_w.py {GROUP} run at {time.strftime('%Y-%m-%d %H:%M:%S %Z')}", flush=True)
C_ = Checks()

NEWFAM = {   # key: (refit_data family, K) -- same atom count as the original run
    'A15m': (lambda: RD.fam_A(1.5, -0.75, 2.0), 160000), 'A15p': (lambda: RD.fam_A(1.5, 0.6, 2.0), 160000),
    'A3': (lambda: RD.fam_A(3.0, -0.6, 2.0), 160000), 'A06': (lambda: RD.fam_A(0.6, -0.3, 2.0), 320000),
    'M1': (lambda: RD.fam_M1(4.0), 160000), 'M2': (lambda: RD.fam_M2(3.0), 160000),
    'B0_15': (lambda: RD.fam_bessel(0, 1.5, 2.0), 160000), 'B1_15': (lambda: RD.fam_bessel(1, 1.5, 2.0), 160000),
    'B0_3': (lambda: RD.fam_bessel(0, 3.0, 2.0), 160000),
    'H2': (lambda: RD.fam_kappa(2, 0.5, 0, 3.0), 160000), 'K2p': (lambda: RD.fam_kappa(2, 0, 0.25, 3.0), 160000),
    'K2m': (lambda: RD.fam_kappa(2, 0, -0.25, 3.0), 160000), 'L2': (lambda: RD.fam_kappa(2, 0, 0, 3.0), 160000),
    'K2p_s2': (lambda: RD.fam_kappa(2, 0, 0.25, 2.0), 160000), 'K2p_s35': (lambda: RD.fam_kappa(2, 0, 0.25, 3.5), 160000),
    'KO1': (lambda: RD.fam_kappa(2.5, -0.3, 0.3, 2.0), 120000), 'KO2': (lambda: RD.fam_kappa(2.5, -0.3, -0.3, 2.0), 120000),
    'KO3': (lambda: RD.fam_kappa(1.5, -0.4, 0.4, 2.5), 120000),
}


def new_data(key, p, nmax=1600):
    fam, K = NEWFAM[key]
    n, y = RD.run(f"new_{key}", p, fam(), K, nmax)
    return n.astype(float), y


def floor(y, nmax):
    a, b = int(0.75*nmax) - 1, nmax
    d6 = np.diff(np.array([float(v) for v in y[a:b]]), 6); return float(np.std(d6)/np.sqrt(924.0))


def dprofile(n, yo, yn, e, nmax):
    NS = [k for k in (200, 400, 800, 1200, 1600) if k <= nmax]
    return max(float(k**e*abs(mp.mpf(yo[k - 1]) - yn[k - 1])) for k in NS), [float(abs(mp.mpf(yo[k - 1]) - yn[k - 1])) for k in NS]


def line(key, e, W, fo, ho, fn, hn, tolf, extra=""):
    to, tn = max(3*ho, tolf), max(3*hn, tolf)
    oo, on = abs(fo - W) <= to, abs(fn - W) <= tn
    print(f"  {key} n^-{e:<5}: W {W:+.9f} | old {fo:+.9f} ({ho:.1e}) diff {fo - W:+.1e} {'PASS' if oo else 'FAIL'}"
          f" | new {fn:+.9f} ({hn:.1e}) diff {fn - W:+.1e} [{abs(fn - W)/tn:.2f} tol] {'PASS' if on else 'FAIL'}"
          f" | new - old {fn - fo:+.1e}" + extra, flush=True)
    return oo, on, tn


def summary(key, n, yo, yn, emax, nmax=1600):
    D, prof = dprofile(n, yo, yn, emax, nmax)
    print(f"  {key}: |y_old - y_new| at n = 200, 400, 800, 1200, 1600: {', '.join(f'{v:.1e}' for v in prof)};"
          f"  max n^{emax}|dy| = {D:.1e};  noise sigma_y old {floor(yo, nmax):.1e}, new {floor(yn, nmax):.1e}", flush=True)


if GROUP == 'test':
    P = json.load(open(WC / 'predictions.json'))
    keys = sys.argv[2:] or ['A3', 'B0_3', 'M2', 'A15m', 'A15p', 'B0_15', 'B1_15', 'M1', 'A06']
    for key in keys:
        spec, lam, wts, tails = WS.SPECTRA[key](); rec = P[key]; p = rec['p']
        n, yo, fname = run_measure(spec['tag'], lam, wts, p, tails)
        n2, yn = new_data(key, p)
        print(f"=== {key}: {spec['name']} (old {fname}; new tmp/refit/new_{key}__*) ===", flush=True)
        summary(key, n, yo, yn, max(rec['targets']))
        pred = {float(e): float(mp.mpf(v)) for e, v in rec['pred'].items()}
        ynf = np.array([float(v) for v in yn])
        for e in rec['targets']:
            e = round(float(e), 6); W = pred.get(e, 0.0)
            fo, ho = fit_target(n, yo, p, e, pred, rec['logexps']); fn, hn = fit_target(n, ynf, p, e, pred, rec['logexps'])
            alts = []
            for name, av in rec['alt'].items():
                a = float(mp.mpf(av[str(e)])) if str(e) in av else W
                if abs(a - W) > 1e-12: alts.append((name, a))
            tn = max(3*hn, 2e-6*(1 + abs(W)))
            ex = ("   alts(new): " + "; ".join(f"{nm} {abs(fn - a)/tn:.0f} tol" for nm, a in alts)) if alts else ""
            oo, on, _ = line(key, e, W, fo, ho, fn, hn, 2e-6*(1 + abs(W)), ex)
            C_.check(f"{key} n^-{e}: verdict unchanged (old {'PASS' if oo else 'FAIL'})", oo == on)
        if key == 'M1':          # W' (post hoc, JZC_W §2.4) at n^-4
            t1, _ = predict(spec, variant={'dressing'}); pe1 = {e: float(v) for e, v in by_exponent(t1).items()}
            fo, ho = fit_target(n, yo, p, 4.0, pe1); fn, hn = fit_target(n, ynf, p, 4.0, pe1)
            line(key + " W'", 4.0, pe1[4.0], fo, ho, fn, hn, 2e-6*(1 + abs(pe1[4.0])),
                 f"   (3 pi^2/128 = {3*np.pi**2/128:.7f}; new fit - M(1,0) = {fn - pred[4.0]:+.7f})")

elif GROUP == 'probe':
    Q = json.load(open(WC / 'predictions_probe.json')); Y = {}
    for key in ('H2', 'K2p', 'K2m', 'L2'):
        spec, lam, wts, tails = (WS.PROBE[key]() if key != 'L2' else WS.famK(2, 0, 0, 3.0))
        n, yo, fname = run_measure(spec['tag'], lam, wts, 2.0, tails); n2, yn = new_data(key, 2.0)
        ynf = np.array([float(v) for v in yn]); Y[key] = (yo, ynf)
        print(f"=== {key}: {spec['name']} (old {fname}) ===", flush=True); summary(key, n, yo, yn, 4)
        pr = {float(e): float(mp.mpf(v)) for e, v in Q[key].items()}
        t1, _ = predict(spec, variant={'dressing'}); pe1 = {e: float(v) for e, v in by_exponent(t1).items()}
        for e in (1.0, 2.0, 3.0, 4.0):
            W = pr.get(e, 0.0)
            fo, ho = fit_target(n, yo, 2.0, e, pr); fn, hn = fit_target(n, ynf, 2.0, e, pr)
            oo, on, tn = line(key, e, W, fo, ho, fn, hn, 2e-6*(1 + abs(W)),
                              f"   W' {pe1.get(e, 0):+.9f}: new diff {fn - pe1.get(e, 0):+.1e} ({abs(fn - pe1.get(e, 0))/tn:.2f} tol)" if e == 4.0 else "")
            if e < 4: C_.check(f"{key} n^-{e}: verdict unchanged", oo == on)
            if e == 4.0 and key in ('K2p', 'K2m'):
                C_.check(f"{key} n^-4: W' passes on new data (post hoc; JZC_W §2.4)", abs(fn - pe1[4.0]) <= tn)
    for i, lab in ((0, 'old'), (1, 'new')):
        ev = (np.array(Y['K2p'][i], float) + np.array(Y['K2m'][i], float))/2 - np.array(Y['L2'][i], float)
        pe_ev = {e: (float(mp.mpf(Q['K2p'].get(str(e)[:-2] if False else str(int(e)), 0))) + float(mp.mpf(Q['K2m'].get(str(int(e)), 0))))/2
                 - float(mp.mpf(Q['L2'].get(str(int(e)), 0))) for e in (1.0, 2.0, 3.0, 4.0)}
        v, hr = fit_target(n, ev, 2.0, 4.0, pe_ev)
        print(f"  kappa-even part n^-4 ({lab}): fit {v:+.9f} ({hr:.1e})  W {pe_ev[4.0]:+.9f}  excess {v - pe_ev[4.0]:+.2e}", flush=True)
    Q2 = json.load(open(WC / 'predictions_probe2.json'))
    for key, args in (('K2p_s2', (2, 0, 0.25, 2.0)), ('K2p_s35', (2, 0, 0.25, 3.5))):
        spec, lam, wts, tails = WS.famK(*args)
        t0, _ = predict(spec); t1, _ = predict(spec, variant={'dressing'}); W0, W1 = by_exponent(t0), by_exponent(t1)
        C_.check(f"{key}: W' reproduces predictions_probe2.json (1e-25)", all(abs(W1[float(e)] - mp.mpf(v)) < mp.mpf(10)**-25 for e, v in Q2[key].items()))
        n, yo, fname = run_measure(spec['tag'], lam, wts, 2.0, tails); n2, yn = new_data(key, 2.0)
        ynf = np.array([float(v) for v in yn])
        print(f"=== {key}: {spec['name']} (old {fname}) ===", flush=True); summary(key, n, yo, yn, 4)
        pr = {k: float(v) for k, v in W1.items()}
        for e in (1.0, 2.0, 3.0, 4.0):
            W = pr.get(e, 0.0); w0 = float(W0.get(e, 0))
            fo, ho = fit_target(n, yo, 2.0, e, pr); fn, hn = fit_target(n, ynf, 2.0, e, pr)
            tn = max(3*hn, 2e-6*(1 + abs(W)))
            oo, on, _ = line(key + " W'", e, W, fo, ho, fn, hn, 2e-6*(1 + abs(W)), f"   W (unrefined) {w0:+.9f}: {abs(fn - w0)/tn:.0f} tol" if e == 4.0 else "")
            C_.check(f"{key} n^-{e} W': verdict unchanged", oo == on)

elif GROUP == 'outer':
    PO = json.load(open(WC / 'predictions_outer.json'))
    CASES = {'KO1': ((2.5, -0.3, 0.3, 2.0), [1.0, 2.0], [2.5, 3.0, 3.5]), 'KO2': ((2.5, -0.3, -0.3, 2.0), [1.0, 2.0], [2.5, 3.0, 3.5]),
             'KO3': ((1.5, -0.4, 0.4, 2.5), [1.0], [1.5, 2.0])}
    def pool_ext(p, emax=9.0):                        # verbatim from w_outer_e2e.py
        return sorted({round(m + j*p, 6) for m in range(0, 10) for j in range(0, 12) if 0 < m + j*p <= emax})
    def fit_ext(n, y, p, target, pred, los=(100, 200, 400), Js=(3, 4, 5, 6)):
        r = np.array(y, float) - sum(float(v)*n**(-e) for e, v in pred.items() if e < target - 1e-6)
        Pn = [e for e in pool_ext(p) if e > target + 1e-6]; est = []
        for J in Js:
            E = [target] + Pn[:J - 1]; cols = [n**(-e) for e in E]
            for lo in los:
                m = n >= lo; A = np.vstack([cc[m] for cc in cols]).T
                sc = np.abs(A).max(axis=0); est.append((np.linalg.lstsq(A/sc, r[m], rcond=None)[0]/sc)[0])
        est = np.array(est); return float(np.median(est)), float((est.max() - est.min())/2)
    for key, ((p, d, kap, s), tR, tW) in CASES.items():
        K = 120000; k = np.arange(1, K + 2, dtype=np.float64); lam = (k + d)**p + kap
        T0 = ((lam[K - 1] - kap)**(1/p) + (lam[K] - kap)**(1/p))/2
        n, yo, fname = run_measure(f"wO_p{p}_d{d}_k{kap}_s{s}", lam[:K], lam[:K]**(-s/p), p, [(float(T0), 1.0, float(s))], nmax=1200)
        n2, yn = new_data(key, p, nmax=1200); ynf = np.array([float(v) for v in yn])
        print(f"=== {key}: p={p} d={d} kappa={kap} s={s} (old {fname}) ===", flush=True); summary(key, n, yo, yn, 3.5, nmax=1200)
        spec_, *_ = WS.famK(p, d, kap, s); _, info_ = predict(spec_, emax=3.6)   # run-2 fields of w_outer_e2e (not in the stored file)
        PO[key].setdefault('X', {str(j): str(v) for j, v in info_['X'].items()}); PO[key].setdefault('gauge1', str(2*kap*mp.zeta(0, 1 + mp.mpf(d))))
        Wd = {float(e): float(mp.mpf(v)) for e, v in PO[key]['W'].items()}; R = {float(k_): float(mp.mpf(v)) for k_, v in PO[key]['R'].items()}
        for e in sorted(set(tR) | set(tW)):
            ref = R[e] if e in tR else Wd.get(e, 0.0)
            fo, ho = fit_ext(n, yo, p, e, Wd); fn, hn = fit_ext(n, ynf, p, e, Wd)
            tn = max(3*hn, 2e-6*(1 + abs(Wd.get(e, 0.0))))
            ex = ""
            if e not in tR and any('pole' in l for ee, v, l in PO[key]['Wterms'] if abs(ee - e) < 1e-9):
                nopole = Wd.get(e, 0.0) - sum(float(mp.mpf(v)) for ee, v, l in PO[key]['Wterms'] if abs(ee - e) < 1e-9 and 'pole' in l)
                ex += f"   no-pole control (new): {abs(fn - nopole)/tn:.1f} tol"
            if abs(e - 3.5) < 1e-9 and p == 2.5:
                tm = [float(mp.mpf(v)) for ee, v, l in PO[key]['Wterms'] if abs(ee - e) < 1e-9 and l == 'toda mu1'][0]
                alt = Wd[e] - tm*float(mp.mpf(PO[key]['gauge1']))/float(mp.mpf(PO[key]['X']['1']))
                to_ = max(3*ho, 2e-6*(1 + abs(Wd[e])))
                ex += f"   no-gauge-share control: old {abs(fo - alt)/to_:.1f} tol, new {abs(fn - alt)/tn:.1f} tol"
            oo, on, _ = line(key, e, ref, fo, ho, fn, hn, 2e-6*(1 + abs(Wd.get(e, 0.0))), ex)
            C_.check(f"{key} n^-{e}: verdict unchanged", oo == on)
C_.finish()
