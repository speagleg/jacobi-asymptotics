"""LS_ZETA §4: the registered run on the first 4000 nontrivial zeta ordinates (tests/data/zeta_zeros_4000_dps60.txt, pinned in
MANIFEST.sha256).  Written and committed with the pre-registration, before this pipeline read the file.  NUMERICAL.  No claim
about RH: the ordinates are inputs (item 11, E1); the test asks whether b_n of the measure on their reciprocals carries the
prime-power oscillations of the explicit formula, which are known."""
import os, sys, json, hashlib, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import lz_synthetic as LZ
from lz_common import clean_var
ROOT = LZ.ROOT
PIN = "4f9463671ca0ab9ae66ee08be96868a9058c74580557a8e59790180532645382"      # MANIFEST.sha256
for f in (__file__, os.path.join(HERE, 'lz_synthetic.py'), os.path.join(HERE, 'lz_common.py')):
    print(f"sha256 {os.path.basename(f)}: {hashlib.sha256(open(f, 'rb').read()).hexdigest()}", flush=True)
fn = os.path.join(ROOT, 'tests', 'data', 'zeta_zeros_4000_dps60.txt')
h = hashlib.sha256(open(fn, 'rb').read()).hexdigest()
print(f"sha256 data: {h} ({'MATCHES' if h == PIN else 'DOES NOT MATCH'} the manifest)", flush=True)
assert h == PIN
import mpmath as mp
g = [mp.mpf(s) for s in open(fn).read().split()]
mp.mp.dps = 30
chk = max(abs(g[k - 1] - mp.zetazero(k).imag) for k in (1, 2, 3, 10, 100, 1000))
print(f"independent check against mpmath.zetazero (k = 1, 2, 3, 10, 100, 1000): max |diff| = {mp.nstr(chk, 3)}", flush=True)
T = np.array([float(x) for x in g[:LZ.K]])
cal = json.load(open(os.path.join(LZ.OUT, 'lz_null.json')))
A95, A99 = cal['A95'], cal['A99']
BES = LZ.comparator()
cl = LZ.statistic(T, BES)
print(f"thresholds (null, 200 GUE): A95 = {A95:.4f}, A99 = {A99:.4f}", flush=True)
print("CLEAN lines (l, amplitude, phase):", [(round(l, 3), round(a, 4), round(p, 2)) for l, a, p in cl], flush=True)
pk = {f"log {q}": math.log(q) for q in (2, 3, 4, 5, 7, 8)}
for l, a, _ in cl:
    near = min(pk, key=lambda k: abs(pk[k] - l))
    p_emp = float(np.mean(np.array(cal['null_first']) >= a))
    print(f"   line {l:.3f}: amplitude {a:.4f} ({'>' if a > A99 else '<='} A99; null P(first >= a) = {p_emp:.3f}); "
          f"nearest {near} = {pk[near]:.4f} (diff {l - pk[near]:+.4f})", flush=True)
Z1 = abs(cl[0][0] - math.log(2)) <= 0.02 and cl[0][1] > A99
reg = [math.log(q) for q in (2, 3, 4, 5, 7)]
Z2 = sum(any(abs(l - v) <= 0.02 and a > A99 for l, a, _ in cl) for v in reg) >= 3
Z3 = all(any(abs(l - v) <= 0.02 for v in pk.values()) for l, a, _ in cl if a > A99)
power = cal['P_hit1'] >= 15
print(f"power (positive control first-line hits >= 15/20): {cal['P_hit1']}/20 -> {'ADEQUATE' if power else 'UNDERPOWERED'}",
      flush=True)
for k, v in (('Z1', Z1), ('Z2', Z2), ('Z3', Z3)): print(f"({k}) {'PASS' if v else 'FAIL'}", flush=True)
json.dump(dict(lines=cl, Z1=Z1, Z2=Z2, Z3=Z3), open(os.path.join(LZ.OUT, 'lz_zeta.json'), 'w'))
