"""JZC_W_plt1 §5, step 2: Jacobi coefficients of the kappa-family at p < 1 against the predictions written earlier by w_plt1_predict.py
(tmp/w_plt1_cache/predictions.json; Rule X: that file must predate every measure cache, verified by mtime).

Measures: atoms 1/lam_k, lam_k = (k + delta)^p + kappa, masses lam_k^{-s/p}, k = 1..K (K = 200 * 1600 = 320000, as for every p < 1 measure of
JZC_W), plus the continuum tail over the index t = k + delta > T0 = K + 1/2 + delta, written exactly in x = 1/(t^p + kappa):
  int_{T0}^inf (t^p + kappa)^{-s/p} f(1/(t^p + kappa)) dt = int_0^{X0} f(x) (1/p) x^{(s-1)/p - 1} (1 - kappa x)^{1/p - 1} dx,  X0 = 1/(T0^p + kappa),
by Gauss-Jacobi (weight x^{(s-1)/p - 1}) with nmax + 40 points times the analytic factor (1 - kappa x)^{1/p - 1} (|kappa X0| < 1e-3).
(w_common.run_measure's tail is the pure power t^{-s} at t^{-p}; for kappa != 0 it would drop the kappa-correction of the tail.)
Binary128 RKPW (jacobi_rkpw, prec="q"), n <= 1600; caches tmp/w_plt1_cache/<tag>__<sha>.txt.
Fits (as w_test / w_common.fit_target, with the pool extended by the pure powers m p): for a target e, subtract the predicted terms of order
< e, fit n^-e with the next J - 1 exponents of {i + j p : i, j >= 0} as nuisance, J = 3..6, windows n >= 100, 200, 400; median and
half-range. Pass: |fit - EQ| <= max(3 half-ranges, 2e-6 (1 + |EQ|)). Alternatives are reported in tolerances (excluded: > 10).
Truncation: p = 0.6, kappa = +0.5 is also run with 2K atoms; fits must agree to < tolerance/10.
NUMERICAL (Rule N): half-ranges are spreads over fit choices, not error bounds.
Usage: w_plt1_test.py [gen|fit]   (gen: generate/cached measures only; fit: full report; default: both)"""
import os, sys, json, time, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from scipy.special import roots_jacobi
from w_common import ROOT, NMAX, Checks
from so_fit import sequences
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
mp.mp.dps = 40
CACHE = ROOT / 'tmp' / 'w_plt1_cache'
PRED = json.load(open(CACHE / 'predictions.json')); TPRED = os.path.getmtime(CACHE / 'predictions.json')
K0 = 200*NMAX


def kmeasure(p, d, kap, s, K, nmax=NMAX):
    tag = f"K_p{p}_d{d}_k{kap:+.1f}_s{s}_K{K}"
    h = hashlib.sha256(repr((p, d, kap, s, K, nmax, 'v1')).encode()).hexdigest()[:16]
    f = CACHE / f"{tag}__{h}.txt"
    fresh = not f.exists()
    if fresh:
        k = np.arange(1, K + 1, dtype=np.float64) + d
        lam = k**p + kap
        T0 = K + 0.5 + d; X0 = 1/(T0**p + kap)
        be = (s - 1)/p - 1; u, wu = roots_jacobi(nmax + 40, 0.0, be)
        tx = X0*(1 + u)/2; tw = wu*(X0/2)**(be + 1)/p*(1 - kap*tx)**(1/p - 1)
        mu = DiscreteMeasure.from_atoms(1/lam, lam**(-s/p), tail=(tx, tw))
        jc = jacobi_rkpw(mu, nmax + 1, prec="q")
        with open(f, "w") as fh:
            for a_, b2 in zip(jc.a[:nmax], jc.b2[:nmax]): fh.write(f"{mp.nstr(a_, 36)} {mp.nstr(mp.sqrt(b2), 36)}\n")
    rows = [l.split() for l in open(f)]
    al = np.array([mp.mpf(r[0]) for r in rows], dtype=object); b = np.array([mp.mpf(r[1]) for r in rows], dtype=object)
    n, y, *_ = sequences(p, al, b)
    return n.astype(float), np.array(y, float), f, fresh


def pool(p, emax=9.0):
    return sorted({round(i + j*p, 6) for i in range(0, 10) for j in range(0, 16) if 0 < i + j*p <= emax})


def fit_target(n, y, p, target, pred, los=(100, 200, 400), Js=(3, 4, 5, 6)):
    r = y - sum(float(v)*n**(-e) for e, v in pred.items() if e < target - 1e-6)
    P = [e for e in pool(p) if e > target + 1e-6]
    est = []
    for J in Js:
        E = [target] + P[:J - 1]
        for lo in los:
            m = n >= lo; A = np.vstack([n[m]**(-e) for e in E]).T
            sc = np.abs(A).max(axis=0); co = np.linalg.lstsq(A/sc, r[m], rcond=None)[0]/sc
            est.append(co[0])
    est = np.array(est)
    return float(np.median(est)), float((est.max() - est.min())/2)


def report(C_, key, n, y, rec):
    p = rec['p']; pred = {round(float(e), 6): float(mp.mpf(v)) for e, v in rec['pred'].items()}
    res = {}
    for e in rec['targets']:
        e = round(float(e), 6); v, hr = fit_target(n, y, p, e, pred)
        w = pred.get(e, 0.0); tol = max(3*hr, 2e-6*(1 + abs(w)))
        ok = C_.check(f"{key} n^-{e}", abs(v - w) <= tol)
        alts = []
        for name, av in rec['alt'].items():
            if str(e) in av:
                a = float(mp.mpf(av[str(e)]))
                if abs(a - w) > 1e-12: alts.append(f"{name}: {a:+.7f} ({abs(v - a)/tol:.0f} tol)")
        print(f"  n^-{e:<6}: fit {v:+.9f} (half-range {hr:.1e})  EQ {w:+.9f}  diff {v - w:+.1e}  tol {tol:.1e}  "
              f"{'PASS' if ok else 'FAIL'}" + ("   | alternatives: " + "; ".join(alts) if alts else ""), flush=True)
        res[e] = (v, hr, tol)
    return res


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'both'
    print("w_plt1_test.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), "| predictions written",
          time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(TPRED)), flush=True)
    C_ = Checks(); Y = {}
    runs = [(k['p'], k['delta'], k['kappa'], k['s'], K0) for k in PRED.values() if 'kappa' in k]
    runs.append((0.6, -0.3, 0.5, 2.0, 2*K0))
    for (p, d, kap, s, K) in runs:
        t0 = time.time(); n, y, f, fresh = kmeasure(p, d, kap, s, K)
        Y[(p, kap, K)] = (n, y)
        print(f"measure p={p} delta={d} kappa={kap:+} s={s} K={K}: {f.name} ({'generated now' if fresh else 'cached'}, {time.time() - t0:.0f} s)", flush=True)
        C_.check(f"Rule X: predictions predate measure {f.name}", os.path.getmtime(f) > TPRED)
    if mode == 'gen': C_.finish(); sys.exit(0)
    for key, rec in PRED.items():
        p = rec['p']
        if 'kappa' in rec:
            n, y = Y[(p, rec['kappa'], K0)]
        else:
            comb = {float(k): float(mp.mpf(w)) for k, w in rec['comb'].items()}
            n = Y[(p, 0.5, K0)][0]; y = sum(w*Y[(p, k, K0)][1] for k, w in comb.items())
        print(f"=== {key} ===", flush=True)
        R = report(C_, key, n, y, rec)
        if key == 'p0.6_k+0.5':
            n2, y2 = Y[(0.6, 0.5, 2*K0)]
            for e, (v, hr, tol) in R.items():
                v2, _ = fit_target(n2, y2, p, e, {round(float(ee), 6): float(mp.mpf(vv)) for ee, vv in rec['pred'].items()})
                print(f"     truncation K -> 2K at n^-{e}: {v:+.9f} -> {v2:+.9f} (diff {abs(v2 - v):.1e}, tol/10 {tol/10:.1e})")
                C_.check(f"truncation {key} n^-{e}", abs(v2 - v) < tol/10)
    C_.finish()
