"""JZC_SHIFT §5.3: REGISTRATION (Rule X) of the closed form h(j, k) (shift_hjk.py, interpolated in (j, k) from the Toda flow at
integer j, k <= 9) at p = 5/2, for SYMBOLIC (j, k), before the engine run R7 exists.  Writes shift_predictions2.json (refuses to
overwrite).  R7: w2_engine.py (not modified), DECOUPLE, p = 5/2, symbolic (alpha, beta, j, k), E = (1, 1), KORD 4 (the JZC_W2 H
configuration at p = 5/2 instead of 3/2).  Registered: LB at N^-1 (e1, e2) and N^-2 (e1 e2), zeros below, e1 e2 N^-3 = 0, and
e1 e2 N^-4 = h(j, k) at p = 5/2 with the Bessel order alpha (= nu) in f2, a2 (prediction: beta-free)."""
import os, sys, json, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
OUT = os.path.join(HERE, 'shift_predictions2.json')
if os.path.exists(OUT):
    print("shift_predictions2.json exists: registration is immutable; not overwritten."); sys.exit(0)
ENGINE = os.path.join(HERE, 'w2_engine.py'); CL = os.path.join(SHC, 'hjk_closed.json')
provenance(__file__, os.path.join(HERE, 'shift_common.py'), os.path.join(HERE, 'shift_hjk.py'), ENGINE, CL)
P, AL, J, KK = sp.symbols('p alpha j k')
h = sp.sympify(json.load(open(CL))['h'], locals=dict(p=P, alpha=AL, j=J, k=KK))
p = sp.Rational(5, 2)
preds = {'1,0,0': '0', '0,1,0': '0', '1,1,0': '0', '1,1,1': '0',
         '1,0,1': str(LB((1,), (J,), p)), '0,1,1': str(LB((1,), (KK,), p)), '1,1,2': str(sp.factor(LB((1, 1), (J, KK), p))),
         '1,1,3': '0', '1,1,4': str(sp.factor(h.subs(P, p)))}
reg = {'timestamp': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'engine_sha256': sha(ENGINE),
       'script_sha256': {os.path.basename(f): sha(f) for f in (__file__, os.path.join(HERE, 'shift_hjk.py'), CL)},
       'runs': {'R7': {'env': dict(DECOUPLE='1', PVAL='5/2', E1='1', E2='1', KORD='4', SHI='16'), 'LB': {}, 'TD': preds}}}
json.dump(reg, open(OUT, 'w'), indent=1)
for kk, v in preds.items(): print(f"  R7 nat[{kk}] = {v}")
print(f"REGISTERED {OUT} at {reg['timestamp']}")
