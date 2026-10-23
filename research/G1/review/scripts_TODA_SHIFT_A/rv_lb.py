"""Reviewer spot check of JZC_SHIFT Thm SH (i), (ii)/LB on exact engine layers NOT used in JZC_SHIFT: the toda_engine outputs of
JZC_TODA (L1, L2, L3, Q1-Q4; b-part = w2_engine), including p < 1 (Q2: p = 3/5 decoupled beta != nu; Q4: p = 2/5) and beta != nu
(L3 symbolic, Q2).  Also the alpha_n-layers (A = n^p alpha_n/(2c)), for which Lemma R predicts the same defect-0 part (alpha^0 = 2 b^0).
For every monomial e^beta: coefficients of n^-k vanish for k < |beta|, and the n^-|beta| coefficient is
LB(beta) = prod (p j_a/2)^{beta_a} (p + 1 + S)_{|beta|-1} / (beta! p^{|beta|-1}),  S = p sum beta_a j_a  (rising factorial).
Control: p + 2 + S in place of p + 1 + S (orders >= 2)."""
import json, sys, math
import sympy as sp
p, al, be = sp.symbols('p alpha beta')
CFG = {'L1': ((1, 1), {}), 'L2': ((2, 3), {}), 'L3': ((1, 2), {}), 'Q1': ((1, 2), {p: sp.Rational(3, 2)}),
       'Q2': ((1, 3), {p: sp.Rational(3, 5)}), 'Q3': ((3, 2), {p: sp.Rational(7, 3)}), 'Q4': ((1, 1), {p: sp.Rational(2, 5)})}
def rf(x, k): return sp.prod([x + i for i in range(k)]) if k > 0 else 1
def LB(beta, js, P, shift=1):
    m = sum(beta); S = P * sum(b * j for b, j in zip(beta, js))
    return sp.prod([(P * j / 2) ** b for b, j in zip(beta, js)]) * rf(P + shift + S, m - 1) / (sp.prod([sp.factorial(b) for b in beta]) * P ** (m - 1))
root = sys.argv[1]
ni = nok = nc = nch = 0
for name, (js, sub) in CFG.items():
    D = json.load(open(f"{root}/eng_{name}.json"))
    P = sub.get(p, p)
    for part in ('e', 'ea'):
        for key, lst in D[part].items():
            beta = tuple(map(int, key.split(',')))
            if js[0] == js[1] and beta[1]: continue
            m = sum(beta)
            if m == 0: continue
            cs = [sp.sympify(s, locals={'p': p, 'alpha': al, 'beta': be}) for s in lst]
            okz = all(sp.simplify(cs[k]) == 0 for k in range(min(m, len(cs))))
            if m < len(cs):
                lead = sp.simplify(cs[m] - LB(beta, js, P)) == 0
                ctrl = (m >= 2) and sp.simplify(cs[m] - LB(beta, js, P, 2)) == 0
                nc += (m >= 2); nch += bool(ctrl)
            else:
                lead = None
            ni += 1 + (lead is not None); nok += okz + bool(lead)
            print(f"{name} {part:2s} exps {js} beta {beta}: zeros below n^-{m}: {okz}; lead = LB: {lead}")
print(f"TOTAL {nok}/{ni} hold; controls (p+2+S) holding: {nch}/{nc}")
