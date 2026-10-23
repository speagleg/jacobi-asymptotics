"""JZC_W2 §3: PRE-REGISTRATION (Rule X) of the second-order pole predictions for sigma^{delta,kappa}.
Writes w2_predictions.json (with timestamp) BEFORE any Jacobi coefficient of these measures is computed (w2_fit.py asserts
this from the file times). Nothing here reads measure data.

Prediction (JZC_W2 Prop 2.1 / 2.3): n^p b_n / c = formal BT_coh layers, all orders in the times (model + Toda + pole times),
from the exact two-parameter engine w2_engine.py at the case's rational data (w2_common.predict2). Registered per case:
  - 'pred': the predicted coefficient of n^{-e} for every e <= emax, and its split by order (0, 1, 2, 3) and by monomial;
  - targets T1 = 2p (leading q1^2 layer, kappa^2) and T2 = 1 + 2p (leading q1*t1 layer + q1^2 dressing);
  - alternatives (same everything, second- and higher-order POLE monomials replaced):
      A0 'none'      : no pole monomial of order >= 2 (first order in the poles only, P K.12's refined form);
      A1 'Toda-only' : pole monomials of order 2 given the integer-time bracket of the mu_1^2 layer (j = k = 1), i.e. natural
                       leading coefficient (1 + 3p)/p per eps_a eps_b (diagonal /2), at the pole exponents;
      A2 'exp'       : naive exponentiation of the first-order leads: 1/2 (sum_a eps_a N^{-1-p j_a})^2 (n/N)^p;
      A3 'square'    : naive square: (sum_a eps_a N^{-1-p j_a})^2 (n/N)^p;
    where eps_a = (p j_a/2) e_a is the natural first-order lead (= W's pole term pR_qW(q)pi cot(pi q) for a pole);
  - the kappa-structure: at n^{-2p} the coefficient is d_{2p} + kappa^2 C (C = C_first(q2) + C_second(q1^2)).
Cases: p = 3/2 (delta = -1/4, s = 11/5) and p = 5/2 (delta = -1/4, s = 2), three kappa each (+k, -k, +k/2)."""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import mpmath as mp
from fractions import Fraction
from so_coeffs import c_p_mp
import w2_common as W

CASES = {
    'P15a': ('3/2', '-1/4', '1/2', '11/5'), 'P15b': ('3/2', '-1/4', '-1/2', '11/5'), 'P15c': ('3/2', '-1/4', '1/4', '11/5'),
    'P25a': ('5/2', '-1/4', '2/5', '2'), 'P25b': ('5/2', '-1/4', '-2/5', '2'), 'P25c': ('5/2', '-1/4', '1/5', '2'),
}
EMAX = {'3/2': 5.5, '5/2': 7.5}
KORD = {'3/2': 6, '5/2': 8}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'w2_predictions.json')


def nat_to_n(coef, E, p, dN, emax):
    """coef (n/N)^p N^{-E} as {exponent: coefficient} in powers of 1/n up to emax (N = n + dN)"""
    out = {}; k = 0
    while E + k <= emax + 1e-9:
        out[round(E + k, 6)] = coef*mp.binomial(-p - E, k)*dN**k; k += 1
    return out


if __name__ == "__main__":
    W.provenance(__file__, W.__file__, W.ENGINE)
    if os.path.exists(OUT):
        print("w2_predictions.json exists: registration is never rewritten"); sys.exit(0)
    t0 = time.time(); R = {}
    for key, (p, d, kap, s) in CASES.items():
        case = W.kappa_case(p, d, kap, s, jmax=3, mmax=4)
        P = case['p_mp']; cp = mp.mpf(c_p_mp(P)); emax = EMAX[p]
        terms, info = W.predict2(case, emax, cp, KORD[p], maxorder=3)
        # 4th order (diagonal q1) must not reach emax: assert that its first nonzero n-coefficient is n^{-4}
        e4 = W.engine(case['p'], case['alpha'], case['betap'], case['poles'][0]['q'], Fraction(1), 4, 0, 4)['e'][(4, 0)]
        assert all(x == 0 for x in e4[:4]), "q1^4 layer starts before n^-4"
        assert 4*float(case['p']*case['poles'][0]['q']) + 4 > emax, "q1^4 layer would reach emax"
        pe = W.by_exp(terms)
        dN = (mp.mpf(case['betap'].numerator)/case['betap'].denominator + 1)/2
        ev, sv = info['ev'], info['sv']
        jv = {lab: j for lab, j, X in info['times']}
        eps = {lab: (P*mp.mpf(jv[lab].numerator)/jv[lab].denominator/2)*ev[lab] for lab in ev}
        # pole-pole and pole-Toda monomials of order >= 2
        def ispole(lab): return lab.startswith('q')
        alt_base = {e: v for e, v in W.by_exp([t for t in terms if not (t[3] >= 2 and any(ispole(x) for x in t[2].split('*')))]).items()}
        alts = {'A0 none': dict(alt_base)}
        for name, fac in (('A1 Toda-only', None), ('A2 exp', mp.mpf(1)/2), ('A3 square', mp.mpf(1))):
            A = dict(alt_base); labs = [lab for lab, j, X in info['times']]
            for i, a in enumerate(labs):
                for b in labs[i:]:
                    if not (ispole(a) or ispole(b)): continue
                    E = 2 + sv[a] + sv[b]
                    if E > emax + 1e-9: continue
                    if fac is None: c0 = (1 + 3*P)/P*(mp.mpf(1)/2 if a == b else 1)
                    else: c0 = fac*(1 if a == b else 2)
                    for e, v in nat_to_n(c0*eps[a]*eps[b], E, P, dN, emax).items(): A[e] = A.get(e, 0) + v
            alts[name] = A
        T1, T2 = round(2*float(case['p']), 6), round(1 + 2*float(case['p']), 6)
        R[key] = dict(p=p, d=d, kap=kap, s=s, alpha=str(case['alpha']), betap=str(case['betap']), c=str(cp), emax=emax,
                      targets=[T1, T2], pred={str(e): str(v) for e, v in pe.items()},
                      by_order={str(o): {str(e): str(v) for e, v in W.by_exp(terms, orders={o}).items()} for o in range(4)},
                      terms=[(e, str(v), l, o) for e, v, l, o in terms],
                      alts={nm: {str(e): str(v) for e, v in A.items()} for nm, A in alts.items()},
                      eps={lab: str(v) for lab, v in eps.items()}, times={lab: [str(j), str(X)] for lab, j, X in info['times']})
        print(f"{key}: p={p} d={d} kappa={kap} s={s}  alpha={case['alpha']}  beta'={case['betap']}  ({time.time() - t0:.0f}s)", flush=True)
        for e in (T1, T2):
            sec = sum(v for ee, v, l, o in terms if abs(ee - e) < 1e-9 and o >= 2)
            print(f"   n^-{e}: total {mp.nstr(pe[e], 12)}   order>=2 part {mp.nstr(sec, 12)}   "
                  + "  ".join(f"{nm}: {mp.nstr(A[e], 10)}" for nm, A in alts.items()), flush=True)
    stamp = time.time()
    json.dump(dict(written=time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(stamp)), unix=stamp, cases=R), open(OUT, 'w'), indent=0)
    print(f"REGISTERED {OUT} at {time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(stamp))}")
