"""LS_ZETA (pre-registration stage): validation, GUE null distribution and positive control for the "primes in Lanczos
coefficients" test, run BEFORE the zeta zeros are read by this pipeline.  NUMERICAL.  No claim about RH (ordinates are inputs).

Pipeline (lz_common): atoms 1/T_k, masses T_k^{-2}, k <= K = 4000, continuum tail beyond N̄ = K (shared by data and comparator);
Lanczos with full reorthogonalisation, n < NMAX = 2000; D_n = n (b_n/b_n^smooth - 1); the CLEAN statistic is computed on
D_n/sqrt(n) (the linear response to a fixed sinusoid grows like sqrt(n), SPEC §3.18) as constant-amplitude sinusoids in
T*(n), n in [40, 2000), l in [0.3, 2.1] (step 0.002; below the Nyquist limit log(T*/2pi) >= 2.4 of the sampling in T*), k = 6.
 (V)  validation: the Lanczos pipeline reproduces the Arb pipeline (ls_common, exact Hurwitz tail) on the smooth Hurwitz
      comparator nu = 2/5, a = 3/10 (n < 300) to relative 1e-10.
 (N)  null: 200 GUE spectra (Dumitriu–Edelman beta = 2, N = 8000, middle 60 %, unfolded; seeds 1..200) placed on the zero
      density by N̄(T_k) = u_k - 1/2.  Records the first CLEAN amplitude: its 95th and 99th percentiles A95, A99 are the
      registered detection thresholds.
 (P)  positive control: 20 GUE spectra (seeds 1001..1020) with the truncated explicit formula injected,
      N̄(T_k) + S_P(T_k) = u_k - 1/2,  S_P = -(1/pi) sum_{p <= 13, k <= 3} sin(k T log p)/(k p^{k/2}).
      Reports how often CLEAN's first line is within 0.02 of log 2 above A99, and how many of
      {log 2, log 3, log 4, log 5, log 7} are recovered within 0.02 above A99 among the 6 lines."""
import os, sys, json, hashlib, time, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from multiprocessing import Pool
from lz_common import *
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'tmp', 'lz'); os.makedirs(OUT, exist_ok=True)
K, NMAX = 4000, 2000
NS = np.arange(40, NMAX)
ELLS = np.round(np.arange(0.3, 2.1 + 1e-9, 0.002), 3)
LOGS = {'log2': math.log(2), 'log3': math.log(3), 'log4': math.log(4), 'log5': math.log(5), 'log7': math.log(7)}
TS = np.array([Tstar(int(n)) for n in NS])
SMOOTH = smooth_nodes(1, K + 1)


def comparator():
    x, w = zero_measure(SMOOTH, K)
    return lanczos(x, w, NMAX)[1]


def nodes_from_u(u, lines):
    """solve N̄(T) + S(T) = u_k - 1/2 for the first K entries of u (Newton from the smooth inverse)."""
    y = np.asarray(u[:K]) - 0.5
    T = np.array([Nbar_inv(float(v)) if v > 0.2 else Nbar_inv(0.2) for v in y])
    for _ in range(40):
        f = T/(2*np.pi)*np.log(T/(2*np.pi)) - T/(2*np.pi) + 7/8 + (S_lines(T) if lines else 0) - y
        fp = np.log(T/(2*np.pi))/(2*np.pi)
        T = T - f/fp
    return np.sort(T)


def statistic(T_nodes, bes):
    x, w = zero_measure(T_nodes, K)
    be = lanczos(x, w, NMAX)[1]
    D = D_of(be, bes)
    y = np.array([D[int(n)]/math.sqrt(n) for n in NS])
    return clean_var(TS, y, ELLS, k=6)


def job(args):
    kind, seed = args
    rng = np.random.default_rng(seed)
    u = gue_unfolded(8000, rng)
    T = nodes_from_u(u, kind == 'P')
    return kind, seed, statistic(T, BES)


BES = None
if __name__ == '__main__':
    for f in (__file__, os.path.join(HERE, 'lz_common.py')):
        print(f"sha256 {os.path.basename(f)}: {hashlib.sha256(open(f, 'rb').read()).hexdigest()}", flush=True)
    # (V)
    import mpmath as mp
    from ls_common import b2_series
    b2a, _ = b2_series([], [], mp.mpf(2)/5, mp.mpf('0.3'), 1, 2, 300, 11000)
    lat = (np.arange(1, 20000) + 0.3)/0.4; xK = 1/((20000 - 0.5 + 0.3)/0.4)
    xq, wq = tail_quadrature(xK, 0.4, 400)
    be = lanczos(np.concatenate([1/lat, xq]), np.concatenate([lat**-2.0, wq]), 300)[1]
    rel = max(abs(be[n]/float(b2a[n]) - 1) for n in range(1, 300))
    print(f"(V) Lanczos + quadrature tail vs Arb (Hurwitz nu = 2/5, a = 3/10, n < 300): max relative error {rel:.2e}", flush=True)
    assert rel < 1e-10
    BES = comparator()
    print(f"comparator: {len(SMOOTH)} smooth atoms, T_K = {SMOOTH[-1]:.2f}; T*(40) = {TS[0]:.2f}, T*(1999) = {TS[-1]:.2f}", flush=True)
    t0 = time.time()
    jobs = [('N', s) for s in range(1, 201)] + [('P', s) for s in range(1001, 1021)]
    res = {'N': {}, 'P': {}}
    with Pool(2, initializer=globals().update, initargs=({'BES': BES},)) as P:
        for kind, seed, cl in P.imap_unordered(job, jobs):
            res[kind][seed] = cl
    print(f"   {len(jobs)} spectra in {time.time() - t0:.0f}s", flush=True)
    a1 = np.array([res['N'][s][0][1] for s in res['N']])
    A95, A99 = float(np.percentile(a1, 95)), float(np.percentile(a1, 99))
    print(f"(N) null (200 GUE): first-line amplitude median {np.median(a1):.4f}, A95 = {A95:.4f}, A99 = {A99:.4f}; "
          f"first-line positions spread over [{min(res['N'][s][0][0] for s in res['N']):.3f}, "
          f"{max(res['N'][s][0][0] for s in res['N']):.3f}]", flush=True)
    hit1 = 0; rec = []
    for s, cl in sorted(res['P'].items()):
        if abs(cl[0][0] - LOGS['log2']) <= 0.02 and cl[0][1] > A99: hit1 += 1
        got = [k for k, v in LOGS.items() if any(abs(l - v) <= 0.02 and a > A99 for l, a, _ in cl)]
        rec.append(len(got))
        print(f"   P seed {s}: lines {[(round(l, 3), round(a, 4)) for l, a, _ in cl]}  recovered {got}", flush=True)
    print(f"(P) positive control: first line = log 2 above A99 in {hit1}/20; mean number of the 5 registered lines recovered "
          f"above A99 = {np.mean(rec):.2f}", flush=True)
    json.dump(dict(A95=A95, A99=A99, null_first=a1.tolist(), P_hit1=hit1, P_rec=rec,
                   P_lines={str(s): cl for s, cl in res['P'].items()}), open(os.path.join(OUT, 'lz_null.json'), 'w'))
