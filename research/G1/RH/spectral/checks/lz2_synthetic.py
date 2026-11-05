"""LS_ZETA2 (pre-registration stage): targeted, per-frequency test for prime-power lines in the Lanczos coefficients of the
measure on reciprocal zeta ordinates.  Synthetic only (GUE null, explicit-formula positive control, off-prime controls); run
BEFORE the real ordinates are read.  NUMERICAL.  No claim about RH (ordinates are inputs).

Why (LS_ZETA §3 + ring experiments recorded in LS_ZETA2.md §1): the response of b_n to a sinusoidal displacement is edge-local,
D_n ~ G(w) h(lambda*(n)) (measured: instantaneous frequency w/2 per n on the unit lattice for w = 0.6, 1.0, 1.6), so prime
lines are sinusoids in T*(n); LS_ZETA's global CLEAN threshold was set by the ~10-node ringing band near l ~ 1.2.
Statistic: for each l in a fixed list, the least-squares amplitude of A cos(l T*) + B sin(l T*) in y_n = D_n/sqrt(n), after a
quadratic detrend in T*, on n in [40, 2000).  Null distribution per l from 200 GUE spectra (seeds 1..200), positive control
from 20 spectra (seeds 1001..1020) with S_P injected (p <= 13, k <= 3), as in lz_synthetic.py.
Frequencies: the registered lines log 2, log 3, log 4, log 5, log 7, and off-prime controls 0.80, 0.90, 1.25, 1.50, 1.75
(each at least 0.06 from every log p^k <= 2.1 and from the half-way aliases).  Per-l thresholds Q95(l), Q99(l)."""
import os, sys, json, hashlib, time, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from multiprocessing import Pool
import lz_synthetic as LZ
from lz_common import *
LINES = {'log2': math.log(2), 'log3': math.log(3), 'log4': math.log(4), 'log5': math.log(5), 'log7': math.log(7)}
CTRL = {'c0.80': 0.80, 'c0.90': 0.90, 'c1.25': 1.25, 'c1.50': 1.50, 'c1.75': 1.75}
FREQ = {**LINES, **CTRL}


def amplitudes(y, TS=LZ.TS):
    x = (TS - TS.mean())/TS.std()
    P = np.vstack([x**j for j in range(3)]).T
    y = y - P @ np.linalg.lstsq(P, y, rcond=None)[0]
    out = {}
    for k, l in FREQ.items():
        X = np.vstack([np.cos(l*TS), np.sin(l*TS)] + [x**j for j in range(3)]).T
        c = np.linalg.lstsq(X, y, rcond=None)[0]
        out[k] = (float(math.hypot(c[0], c[1])), float(math.atan2(-c[1], c[0])))
    return out


def series(T_nodes, bes):
    x, w = zero_measure(T_nodes, LZ.K)
    be = lanczos(x, w, LZ.NMAX)[1]
    D = D_of(be, bes)
    return np.array([D[int(n)]/math.sqrt(n) for n in LZ.NS])


def job(args):
    kind, seed = args
    u = gue_unfolded(8000, np.random.default_rng(seed))
    y = series(LZ.nodes_from_u(u, kind == 'P'), BES)
    np.save(os.path.join(LZ.OUT, f'series_{kind}{seed}.npy'), y)
    return kind, seed, amplitudes(y)


BES = None
if __name__ == '__main__':
    for f in (__file__, os.path.join(HERE, 'lz_synthetic.py'), os.path.join(HERE, 'lz_common.py')):
        print(f"sha256 {os.path.basename(f)}: {hashlib.sha256(open(f, 'rb').read()).hexdigest()}", flush=True)
    BES = LZ.comparator()
    jobs = [('N', s) for s in range(1, 201)] + [('P', s) for s in range(1001, 1021)]
    res = {'N': {}, 'P': {}}; t0 = time.time()
    with Pool(2, initializer=globals().update, initargs=({'BES': BES},)) as P:
        for kind, seed, am in P.imap_unordered(job, jobs): res[kind][seed] = am
    print(f"   {len(jobs)} spectra in {time.time() - t0:.0f}s", flush=True)
    Q = {}
    for k in FREQ:
        a = np.array([res['N'][s][k][0] for s in res['N']])
        Q[k] = (float(np.percentile(a, 95)), float(np.percentile(a, 99)), float(np.median(a)))
        pa = np.array([res['P'][s][k][0] for s in res['P']])
        print(f"{k:6s} l = {FREQ[k]:.4f}: null median {Q[k][2]:.4f}, Q95 {Q[k][0]:.4f}, Q99 {Q[k][1]:.4f};  positive control: "
              f"median {np.median(pa):.4f}, above Q99 in {int(np.sum(pa > Q[k][1]))}/20", flush=True)
    hits = [sum(res['P'][s][k][0] > Q[k][1] for k in LINES) for s in res['P']]
    fp = [sum(res['P'][s][k][0] > Q[k][1] for k in CTRL) for s in res['P']]
    print(f"positive control: log 2 above Q99 in {sum(res['P'][s]['log2'][0] > Q['log2'][1] for s in res['P'])}/20; "
          f">= 3 of 5 lines above Q99 in {sum(h >= 3 for h in hits)}/20; control frequencies above Q99: mean {np.mean(fp):.2f} per seed",
          flush=True)
    json.dump(dict(Q=Q, null={k: [res['N'][s][k][0] for s in res['N']] for k in FREQ},
                   P={str(s): res['P'][s] for s in res['P']}), open(os.path.join(LZ.OUT, 'lz2_null.json'), 'w'))
