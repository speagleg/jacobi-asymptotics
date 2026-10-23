"""JZC_SHIFT §1.3: the index-shift law (shift_common.LB) against ALL existing exact engine outputs (no new engine run).
Sources (exact rational functions, cached by w2_exact.py under tmp/w2/; sha256 printed; produced by w2_engine.py versions b5d60698...
(B, T, M) and 8e69b2e3... (Q, H), JZC_W2 Rule A item 8):
  B: symbolic (p, alpha, beta, j, k), E = (1, 1), KORD 2;   T: symbolic (p, alpha, beta, j), E = (3, 0), KORD 3;
  M: symbolic (p, alpha, beta, j, k), E = (2, 1), KORD 3;   Q: p = 5/2, symbolic (alpha, beta, j), E = (4, 0), KORD 4;
  H: p = 3/2, symbolic (alpha, beta, j, k), E = (1, 1), KORD 4.
For every monomial e1^a e2^b with a + b <= KORD: nat[k] = 0 for k < a + b and nat[a + b] = LB; the lead is beta-free.  Plus the
asserted closed forms of m4_zeta_exact2_B.out (mu_1^2 bracket (3p+1)/(2p)) and of JZC_W2 Cor 2.4 (pole x pole, pole x Toda
brackets), which are specialisations.  Controls (must fail): 1/(2p) and p + 2 + S for every order >= 2 lead."""
import os, sys, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
provenance(__file__, os.path.join(HERE, 'shift_common.py'))
P, AL, BE, J, KK = sp.symbols('p alpha beta j k'); loc = dict(p=P, alpha=AL, beta=BE, j=J, k=KK)
C = Checks()
z = lambda e: sp.simplify(sp.cancel(sp.together(e))) == 0
PV = {'B': None, 'T': None, 'M': None, 'Q': sp.Rational(5, 2), 'H': sp.Rational(3, 2)}
for part in ('B', 'T', 'M', 'Q', 'H'):
    fns = glob.glob(os.path.join(W2C, f"exact_{part}_*.json")); assert len(fns) == 1, (part, fns)
    print(f"sha256 {os.path.basename(fns[0])}: {sha(fns[0])}")
    D = json.load(open(fns[0]))
    nat = {tuple(map(int, k.split(','))): [sp.sympify(x, locals=loc) for x in v] for k, v in D['nat'].items()}
    p = P if PV[part] is None else PV[part]
    for (a, b), v in sorted(nat.items()):
        m = a + b
        if m == 0 or m >= len(v): continue
        beta, js = ((a, b), (J, KK)) if b > 0 else ((a,), (J,))
        if a == 0: beta, js = (b,), (KK,)
        lows = all(z(v[i]) for i in range(m))
        C.check(f"{part}: e1^{a} e2^{b}: N^0..N^-{m - 1} vanish and N^-{m} = LB = {sp.factor(LB(beta, js, p))}", lows and z(v[m] - LB(beta, js, p)))
        C.check(f"{part}: e1^{a} e2^{b}: lead is beta-free", sp.diff(v[m], BE) == 0)
        if m >= 2:
            C.check(f"{part}: control e1^{a} e2^{b}: 1/(2p)", z(v[m] - LB(beta, js, p, kappa=sp.Rational(1, 2))), must_fail=True)
            C.check(f"{part}: control e1^{a} e2^{b}: p + 2 + S", z(v[m] - LB(beta, js, p, shiftc=2)), must_fail=True)
# specialisations stated in the notes
eps = lambda j: P*j/2
C.check("m4_zeta_exact2_B: mu_1^2 bracket (3p+1)/(2p) = LB((2,), (1,))/eps_1^2", z(LB((2,), (1,), P)/eps(1)**2 - (3*P + 1)/(2*P)))
C.check("JZC_W2 Prop 2.2(i): e1 e2 bracket (1 + p + pj + pk)/p = LB((1,1), (j,k))/(eps_j eps_k)",
        z(LB((1, 1), (J, KK), P)/(eps(J)*eps(KK)) - (1 + P + P*J + P*KK)/P))
m_, mp_, j_ = sp.symbols('m mprime jj')
q = lambda m: m - 1/P
C.check("JZC_W2 Cor 2.4: pole x pole bracket (p(1 + m + m') - 1)/p", z(LB((1, 1), (q(m_), q(mp_)), P)/(eps(q(m_))*eps(q(mp_))) - (P*(1 + m_ + mp_) - 1)/P))
C.check("JZC_W2 Cor 2.4: pole x Toda bracket 1 + m + j (integer)", z(LB((1, 1), (q(m_), j_), P)/(eps(q(m_))*eps(j_)) - (1 + m_ + j_)))
C.finish()
