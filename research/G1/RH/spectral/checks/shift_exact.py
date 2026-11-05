"""JZC_SHIFT §4.2: the registered exact engine runs (shift_predictions.json, Rule X) and their comparison.
Usage: shift_exact.py R1|...|R6 [registration json; default shift_predictions.json] (R7: shift_predictions2.json).  Runs w2_engine.py (NOT modified) by subprocess with the registered env, caches the exact output
(JSON of strings of rational functions) under tmp/shift/, asserts that the registration predates the engine output, and compares:
  (LB) every registered index-shift prediction (zeros below the leading order, the Lagrange-Buermann leading coefficient);
  (TD) every registered Toda-dressing prediction (R5, R6);
  (b)  for symbolic beta (R1): the leading coefficients are beta-free.
Controls (must fail): the leading coefficient with the shift coefficient 1/p replaced by 1/(2p) (kappa = 1/2) and with the exponent
p + 1 + S replaced by p + 2 + S, for every monomial of order >= 2; for TD: the bare index-shift law (dressing set to 0) at the
relative-N^-2 coefficients of order >= 2.
Untestable registrations (2026-11-05 fix, adversarial review): a registered key whose monomial the engine run does not produce (or
produces to too low an order) cannot be compared. It used to be skipped silently; it is now listed and counted as UNTESTED, and the
run reports "tested / registered" for LB and TD. An UNTESTED key is not a pass."""
import os, sys, json, subprocess, time, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *

name = sys.argv[1]
REG = os.path.join(HERE, sys.argv[2] if len(sys.argv) > 2 else 'shift_predictions.json'); ENGINE = os.path.join(HERE, 'w2_engine.py')
provenance(__file__, os.path.join(HERE, 'shift_common.py'), ENGINE, REG)
reg = json.load(open(REG)); run = reg['runs'][name]
assert sha(ENGINE) == reg['engine_sha256'], "engine changed since registration"
treg = datetime.datetime.fromisoformat(reg['timestamp']).timestamp()
env_r = run['env']
key = hashlib.sha256((repr(sorted(env_r.items())) + sha(ENGINE)).encode()).hexdigest()[:12]
fn = os.path.join(SHC, f"eng_{name}_{key}.json")
t0 = time.time()
if not os.path.exists(fn):
    env = {k: v for k, v in os.environ.items() if k not in ('PVAL', 'AVAL', 'BVAL', 'J1VAL', 'J2VAL', 'SZOFF', 'NT')}
    subprocess.run([PY, '-B', ENGINE], env=dict(env, **env_r, W2JSON=fn), check=True, stdout=subprocess.DEVNULL)
    print(f"engine {name} {env_r}: {time.time() - t0:.0f}s", flush=True)
else:
    print(f"engine {name} {env_r}: cached output {os.path.basename(fn)}", flush=True)
assert os.path.getmtime(fn) > treg, "engine output predates the registration (Rule X)"
print(f"registration {reg['timestamp']} predates the engine output ({datetime.datetime.fromtimestamp(os.path.getmtime(fn)).isoformat(timespec='seconds')})")
P, AL, BE, J, KK = sp.symbols('p alpha beta j k')
loc = dict(p=P, alpha=AL, beta=BE, j=J, k=KK)
D = json.load(open(fn))
nat = {tuple(map(int, k.split(','))): [sp.sympify(x, locals=loc) for x in v] for k, v in D['nat'].items()}
C = Checks()
z = lambda e: sp.simplify(sp.cancel(sp.together(e))) == 0
# (LB)
nLB = 0; leads = []; untested = []
def testable(kk):
    a, b, k = map(int, kk.split(','))
    return (a, b) in nat and k < len(nat[(a, b)])
for kk, v in run['LB'].items():
    a, b, k = map(int, kk.split(','))
    if not testable(kk): untested.append(('LB', kk, v)); continue
    got = nat[(a, b)][k]; pred = sp.sympify(v, locals=loc)
    ok = z(got - pred); nLB += 1
    if k == a + b: leads.append(((a, b), got))
    if not ok or k == a + b:
        C.check(f"{name} LB nat[e1^{a} e2^{b}][N^-{k}] = {pred if k == a + b else 0}", ok)
    else:
        assert ok, (kk, got)
print(f"   ({nLB} LB coefficients compared; the zero coefficients below the leading order are asserted silently, all hold)")
# (b) beta-free leads
if any(s.has(BE) for s in sum(nat.values(), [])):
    for mo, got in leads: C.check(f"{name} leading coefficient of e1^{mo[0]} e2^{mo[1]} is beta-free", sp.diff(got, BE) == 0)
# controls on the leading coefficients
p = sp.Rational(env_r['PVAL'])
js = (sp.Rational(env_r['J1VAL']) if 'J1VAL' in env_r else J, sp.Rational(env_r['J2VAL']) if 'J2VAL' in env_r else KK)
for mo, got in leads:
    if sum(mo) < 2: continue
    beta = mo if mo[1] > 0 else (mo[0],); jj = js if mo[1] > 0 else js[:1]
    C.check(f"{name} control e1^{mo[0]} e2^{mo[1]}: shift coefficient 1/(2p)", z(got - LB(beta, jj, p, kappa=sp.Rational(1, 2))), must_fail=True)
    C.check(f"{name} control e1^{mo[0]} e2^{mo[1]}: exponent p + 2 + S", z(got - LB(beta, jj, p, shiftc=2)), must_fail=True)
# (TD)
nTD = 0
for kk, v in sorted(run['TD'].items()):
    a, b, k = map(int, kk.split(','))
    if not testable(kk): untested.append(('TD', kk, v)); continue
    nTD += 1
    got = nat[(a, b)][k]; pred = sp.sympify(v, locals=loc)
    C.check(f"{name} TD nat[e1^{a} e2^{b}][N^-{k}] = {pred}", z(got - pred))
    if k == a + b + 2 and a + b >= 2:
        C.check(f"{name} control: bare shift law (no dressing) at nat[e1^{a} e2^{b}][N^-{k}]", z(got), must_fail=True)
for mo, v in sorted(nat.items()):
    if mo != (0, 0): print(f"   nat[e1^{mo[0]} e2^{mo[1]}] = {[str(sp.factor(x)) for x in v]}", flush=True)
print(f"REGISTERED vs TESTED: LB {nLB}/{len(run['LB'])}, TD {nTD}/{len(run['TD'])}")
for kind, kk, v in untested:
    print(f"   UNTESTED ({kind}, monomial/order not produced by this engine run): [{kk}] = {v}")
C.finish()
