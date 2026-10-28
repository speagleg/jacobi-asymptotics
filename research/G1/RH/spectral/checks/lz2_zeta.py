"""LS_ZETA2 §4: the registered targeted run on the first 4000 zeta ordinates (tests/data/zeta_zeros_4000_dps60.txt, pinned in
MANIFEST.sha256).  Committed with the pre-registration, before this pipeline read the file.  NUMERICAL.  No claim about RH:
the ordinates are inputs; the prime-power oscillations of their counting function are classical."""
import os, sys, json, hashlib, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import lz_synthetic as LZ
import lz2_synthetic as L2
PIN = "4f9463671ca0ab9ae66ee08be96868a9058c74580557a8e59790180532645382"
for f in (__file__, os.path.join(HERE, 'lz2_synthetic.py'), os.path.join(HERE, 'lz_synthetic.py'), os.path.join(HERE, 'lz_common.py')):
    print(f"sha256 {os.path.basename(f)}: {hashlib.sha256(open(f, 'rb').read()).hexdigest()}", flush=True)
fn = os.path.join(LZ.ROOT, 'tests', 'data', 'zeta_zeros_4000_dps60.txt')
h = hashlib.sha256(open(fn, 'rb').read()).hexdigest()
print(f"sha256 data: {h} ({'MATCHES' if h == PIN else 'DOES NOT MATCH'} the manifest)", flush=True)
assert h == PIN
import mpmath as mp
g = [mp.mpf(s) for s in open(fn).read().split()]
mp.mp.dps = 30
chk = max(abs(g[k - 1] - mp.zetazero(k).imag) for k in (1, 2, 3, 10, 100, 1000))
print(f"independent check against mpmath.zetazero (k = 1, 2, 3, 10, 100, 1000): max |diff| = {mp.nstr(chk, 3)}", flush=True)
cal = json.load(open(os.path.join(LZ.OUT, 'lz2_null.json')))
Q = cal['Q']
T = np.array([float(x) for x in g[:LZ.K]])
y = L2.series(T, LZ.comparator())
am = L2.amplitudes(y)
res = {}
for k, l in L2.FREQ.items():
    a, ph = am[k]; nul = np.array(cal['null'][k]); p = float((1 + np.sum(nul >= a))/(1 + len(nul)))
    res[k] = dict(l=l, amp=a, phase=ph, Q99=Q[k][1], p=p)
    print(f"{k:6s} l = {l:.4f}: amplitude {a:.4f}  (null median {Q[k][2]:.4f}, Q99 {Q[k][1]:.4f}; empirical p = {p:.4f})"
          f"{'  ABOVE Q99' if a > Q[k][1] else ''}", flush=True)
Z1 = res['log2']['amp'] > res['log2']['Q99']
Z2 = sum(res[k]['amp'] > res[k]['Q99'] for k in L2.LINES) >= 3
Z3 = sum(res[k]['amp'] > res[k]['Q99'] for k in L2.CTRL) <= 1
for k, v in (('Z1', Z1), ('Z2', Z2), ('Z3', Z3)): print(f"({k}) {'PASS' if v else 'FAIL'}", flush=True)
json.dump(dict(res=res, Z1=Z1, Z2=Z2, Z3=Z3), open(os.path.join(LZ.OUT, 'lz2_zeta.json'), 'w'))
