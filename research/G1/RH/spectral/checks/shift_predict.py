"""JZC_SHIFT §4.1: REGISTRATION (Rule X) of predictions for new exact engine runs, written BEFORE any of these runs exists.
Writes shift_predictions.json (refuses to overwrite) with a timestamp and the sha256 of the scripts that produced it.

Engine: w2_engine.py (JZC_W2; imported by subprocess, NOT modified; sha256 printed).  Runs (env of w2_engine.py):
  R1  p = 3/2, symbolic (alpha, beta, j), DECOUPLE, E = (4, 0), KORD 4           e1^m, m <= 4, symbolic exponent j
  R2  p = 5/2, alpha = -3/5, beta = -11/10, symbolic (j, k), E = (2, 2), KORD 4   all e1^a e2^b, a, b <= 2 (incl. e1^2 e2^2)
  R3  p = 3/2, alpha = -1/5, beta = -7/10, j = 1/3 (= q_1), k = 1, E = (5, 1), KORD 5   orders <= 5 (e1^5, e1^4 e2)
  R4  p = 5/2, alpha = -3/5, beta = -11/10, j = 3/5 (= q_1), E = (6, 0), KORD 6   e1^6
  R5  p = 5/2, lattice (beta = alpha, DECOUPLE 0), symbolic alpha, j = 1, k = 2, E = (1, 1), KORD 4   (Toda dressings)
  R6  p = 5/2, lattice, alpha = -3/5, j = 1, E = (3, 0), KORD 5                    (Toda dressings, third order)
Predictions:
  (LB) the index-shift law (shift_common.LB): nat[beta][k] = 0 for k < |beta| and nat[beta][|beta|] = LB(beta), for every
       monomial of the run with |beta| <= KORD (R1-R6);
  (TD) Toda dressings (R5, R6): the full natural-form coefficients through relative order N^-2 of every monomial, computed by the
       formal Toda engine FT from the lattice integer layers (shift_common.lattice_initial: B from N.1/N.6(ii), A derived from the
       j = 1 first-order layer by (T1), shift_dressing.py), with generic symbols for the initial data beyond n^-2; only coefficients
       that do not depend on those symbols are registered (asserted)."""
import os, sys, json, time, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
from sympy.polys.fields import field
from sympy import QQ

OUT = os.path.join(HERE, 'shift_predictions.json')
if os.path.exists(OUT):
    print("shift_predictions.json exists: registration is immutable; not overwritten."); sys.exit(0)
ENGINE = os.path.join(HERE, 'w2_engine.py')
provenance(__file__, os.path.join(HERE, 'shift_common.py'), ENGINE)
P, AL, BE, J, KK = sp.symbols('p alpha beta j k')
R = lambda s: sp.Rational(s)
RUNS = {
    'R1': dict(env=dict(DECOUPLE='1', PVAL='3/2', E1='4', E2='0', KORD='4', SHI='14'), p=R('3/2'), js=(J, KK), E=(4, 0)),
    'R2': dict(env=dict(DECOUPLE='1', PVAL='5/2', AVAL='-3/5', BVAL='-11/10', E1='2', E2='2', KORD='4', SHI='16'),
               p=R('5/2'), js=(J, KK), E=(2, 2)),
    'R3': dict(env=dict(DECOUPLE='1', PVAL='3/2', AVAL='-1/5', BVAL='-7/10', J1VAL='1/3', J2VAL='1', E1='5', E2='1', KORD='5',
                        SHI='26', NT='18'), p=R('3/2'), js=(R('1/3'), 1), E=(5, 1)),
    'R4': dict(env=dict(DECOUPLE='1', PVAL='5/2', AVAL='-3/5', BVAL='-11/10', J1VAL='3/5', E1='6', E2='0', KORD='6', SHI='30',
                        NT='20'), p=R('5/2'), js=(R('3/5'), KK), E=(6, 0)),
    'R5': dict(env=dict(DECOUPLE='0', PVAL='5/2', J1VAL='1', J2VAL='2', E1='1', E2='1', KORD='4', SHI='16'),
               p=R('5/2'), js=(1, 2), E=(1, 1)),
    'R6': dict(env=dict(DECOUPLE='0', PVAL='5/2', AVAL='-3/5', J1VAL='1', E1='3', E2='0', KORD='5', SHI='26', NT='18'),
               p=R('5/2'), js=(1, KK), E=(3, 0)),
}
reg = {'timestamp': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'engine_sha256': sha(ENGINE),
       'script_sha256': {os.path.basename(f): sha(f) for f in (__file__, os.path.join(HERE, 'shift_common.py'))}, 'runs': {}}
for name, r in RUNS.items():
    kord = int(r['env']['KORD']); p = r['p']; js = r['js']
    preds = {}
    for a in range(r['E'][0] + 1):
        for b in range(r['E'][1] + 1):
            m = a + b
            if m == 0: continue
            beta = (a, b)
            for k in range(min(m, kord + 1)): preds[f"{a},{b},{k}"] = '0'
            if m <= kord:
                v = sp.factor(LB(beta, js, p)) if b > 0 else sp.factor(LB((a,), js[:1], p))
                preds[f"{a},{b},{m}"] = str(v)
    reg['runs'][name] = {'env': r['env'], 'LB': preds, 'TD': {}}
    print(f"{name}: {len(preds)} LB predictions; e.g. leads:",
          {kk: v for kk, v in preds.items() if v != '0' and int(kk.split(',')[2]) == sum(map(int, kk.split(',')[:2]))}, flush=True)

# ---- (TD) Toda dressings for R5, R6 ------------------------------------------------------------------------------------------
def toda_dressings(pval, alval, js, E, kord):
    D = kord; Mo = sum(E)
    gen = [f"A{i}" for i in range(3, D + 1)] + [f"B{i}" for i in range(3, D + 1)]
    names = (['alpha'] if alval is None else []) + gen
    Kf, *g = field(','.join(names), QQ)
    al = g[0] if alval is None else Kf(alval); extra = dict(zip(gen, g[(1 if alval is None else 0):]))
    p = Kf(pval)
    a0, b0 = lattice_initial(Kf, p, al, D, extra)
    jsl = [j for j, e in zip(js, E) if e > 0]
    ft = FT(Kf, p, tuple(jsl), D, Mo); a, b, nc = ft.flow(a0, b0)
    delta = ((AL if alval is None else alval) + 1)/2
    gsyms = sp.symbols(' '.join(gen))
    out = {}
    for key, v in b.items():
        beta = key[1]; m = sum(beta)
        if m == 0: continue
        vv = [sp.sympify(str(c.as_expr())) for c in v]
        nat = to_natural(vv, (sum(x*j for x, j in zip(beta, jsl)) + 1)*pval, beta, tuple(jsl), delta)
        full = tuple(beta) if len(beta) == 2 else (beta[0], 0)
        for kidx, val in enumerate(nat):
            if kidx > kord: continue
            if any(val.has(s) for s in gsyms): continue        # depends on initial data beyond n^-2: not registered
            out[f"{full[0]},{full[1]},{kidx}"] = str(sp.factor(val))
    return out

t0 = time.time()
reg['runs']['R5']['TD'] = toda_dressings(R('5/2'), None, (1, 2), (1, 1), 4)
reg['runs']['R6']['TD'] = toda_dressings(R('5/2'), R('-3/5'), (1, 1), (3, 0), 5)
print(f"TD predictions ({time.time() - t0:.0f}s):", flush=True)
for nm in ('R5', 'R6'):
    for kk, v in sorted(reg['runs'][nm]['TD'].items()): print(f"  {nm} nat[{kk}] = {v}", flush=True)
# consistency: TD leading terms agree with LB (a statement about the FT algebra, also proved in shift_toda.py)
for nm in ('R5', 'R6'):
    for kk, v in reg['runs'][nm]['TD'].items():
        if kk in reg['runs'][nm]['LB']:
            assert sp.simplify(sp.sympify(v) - sp.sympify(reg['runs'][nm]['LB'][kk])) == 0, (nm, kk)
json.dump(reg, open(OUT, 'w'), indent=1)
print(f"REGISTERED {OUT} at {reg['timestamp']}")
