"""JZC_W2 §2: exact identities of the second- (and third-/fourth-) order layers of the formal model with two symbolic exponents
(w2_engine.py = m4_rh_exact2 copy with two nilpotent parameters). Identities of rational functions; nothing fitted.
Parts (argv[1]):
  B  : symbolic (p, alpha, beta, j, k), DECOUPLE, KORD 2, E = (1, 1): natural N^0 = N^-1 = 0 and
       N^-2 coefficient of e1 e2 = j k p (p j + p k + p + 1)/4                                   [Prop 2.2 (i)]
       (eps-form: eps_j eps_k (1 + p + p j + p k)/p, eps_x = (p x/2) e_x; at j = k = 1 the mu_1^2 layer (3p+1)/(2p) of N.6(ii));
  T  : symbolic (p, alpha, beta, j), KORD 3, E = (3, 0): e1^2 natural N^-2 = j^2 p(2jp + p + 1)/8 (= B/2 on the diagonal),
       e1^3: N^0..N^-2 = 0, N^-3 = j^3 p (3jp+p+1)(3jp+p+2)/48                                   [Prop 2.2 (ii)]
  M  : symbolic (p, alpha, beta, j, k), KORD 3, E = (2, 1): e1^2 e2: N^0..N^-2 = 0,
       N^-3 = (pj/2)^2 (pk/2) (p+1+S)(p+2+S)/(2p^2), S = p(2j + k)                               [Prop 2.2 (ii)]
  Q  : p = 5/2 fixed, symbolic (alpha, beta, j), KORD 4, E = (4, 0): e1^4: N^0..N^-3 = 0, N^-4 = (pj/2)^4 (p+1+S)_3/(24 p^3), S = 4pj
  H  : p = 3/2 fixed, symbolic (alpha, beta, j, k), KORD 4, E = (1, 1): N^-3 = 0, N^-4 = h(j, k) (printed, factored); beta-free;
       at j = k = 1 and beta = alpha: N^-4 = p^2 h2/2 with JZC_M4_proof's h2.
The orders 2-4 leading terms are the Lagrange-Buermann coefficients of x^{-p}, x = N - (1/p) sum_a eps_a x^{-p j_a}
(CONJECTURE for orders >= 5 and mixed orders not listed; JZC_W2 Obs 2.4).
Controls (must fail): B with (p j + p k + 1) in place of (p j + p k + p + 1); T with (3jp+p+1)^2; M with S = p(j + 2k)."""
import os, sys, json, subprocess, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sympy as sp
from w2_common import W2C, PY, ENGINE, provenance
p, al, be, j, k = sp.symbols('p alpha beta j k')
part = sys.argv[1] if len(sys.argv) > 1 else 'B'
provenance(__file__, ENGINE)
CFG = {'B': dict(DECOUPLE='1', E1='1', E2='1', KORD='2', SHI='8'),
       'T': dict(DECOUPLE='1', E1='3', E2='0', KORD='3', SHI='10'),
       'M': dict(DECOUPLE='1', E1='2', E2='1', KORD='3', SHI='10'),
       'Q': dict(DECOUPLE='1', E1='4', E2='0', KORD='4', SHI='14', PVAL='5/2'),
       'H': dict(DECOUPLE='1', E1='1', E2='1', KORD='4', SHI='16', PVAL='3/2')}[part]
fn = os.path.join(W2C, f"exact_{part}_{hashlib.sha256((repr(sorted(CFG.items())) + open(ENGINE).read()).encode()).hexdigest()[:12]}.json")
t0 = time.time()
if not os.path.exists(fn):
    env = {kk: vv for kk, vv in os.environ.items() if kk not in ('PVAL', 'AVAL', 'BVAL', 'J1VAL', 'J2VAL', 'SZOFF')}
    subprocess.run([PY, '-B', ENGINE], env=dict(env, **CFG, W2JSON=fn), check=True, stdout=subprocess.DEVNULL)
print(f"engine config {CFG}: {time.time() - t0:.0f}s", flush=True)
D = json.load(open(fn))
nat = {tuple(map(int, kk.split(','))): [sp.sympify(x, locals=dict(p=p, alpha=al, beta=be, j=j, k=k)) for x in v] for kk, v in D['nat'].items()}
if 'PVAL' in CFG: p = sp.Rational(CFG['PVAL'])
ok = True; n = 0
def chk(label, expr, must_fail=False):
    global ok, n
    n += 1; z = sp.simplify(sp.cancel(sp.together(expr))) == 0; passed = (not z) if must_fail else z; ok &= passed
    print(f"[{n}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if z else 'fails'} -> {'PASS' if passed else 'FAIL'}", flush=True)
L = lambda S, m: sp.Mul(*[(p + i + S) for i in range(1, m)])/(sp.factorial(m)*p**(m - 1))     # Lagrange-Buermann
if part == 'B':
    g = nat[(1, 1)]
    chk("e1 e2: natural N^0 = 0", g[0]); chk("e1 e2: natural N^-1 = 0", g[1])
    chk("e1 e2: natural N^-2 = j k p (pj + pk + p + 1)/4", g[2] - j*k*p*(p*j + p*k + p + 1)/4)
    chk("e1 e2 at N^-2 in eps-form = 2 * Lagrange(m=2), eps = p x e/2", g[2] - (p*j/2)*(p*k/2)*2*L(p*(j + k), 2))
    chk("first order: natural N^-1 = p j/2", nat[(1, 0)][1] - p*j/2)
    chk("j = k = 1: (eps_1^2 bracket) (3p+1)/(2p) (JZC_M4_proof N.6(ii))", (g[2]/2).subs({j: 1, k: 1})/(p/2)**2 - (3*p + 1)/(2*p))
    chk("control: (pj + pk + 1)", g[2] - j*k*p*(p*j + p*k + 1)/4, must_fail=True)
    print("N^-2 (e1 e2) =", sp.factor(g[2]))
elif part == 'T':
    g2, g3 = nat[(2, 0)], nat[(3, 0)]
    chk("e1^2: N^-2 = j^2 p (2jp+p+1)/8 (= B(j, j)/2)", g2[2] - j**2*p*(2*j*p + p + 1)/8)
    for m in range(3): chk(f"e1^3: N^-{m} = 0", g3[m])
    chk("e1^3: N^-3 = j^3 p (3jp+p+1)(3jp+p+2)/48", g3[3] - j**3*p*(3*j*p + p + 1)*(3*j*p + p + 2)/48)
    chk("e1^3 = Lagrange(m=3) in eps-form", g3[3] - (p*j/2)**3*L(3*p*j, 3))
    chk("control: (3jp+p+1)^2", g3[3] - j**3*p*(3*j*p + p + 1)**2/48, must_fail=True)
    print("e1^2 N^-3 =", sp.factor(g2[3]), "  e1^3 N^-3 =", sp.factor(g3[3]))
elif part == 'M':
    g = nat[(2, 1)]
    for m in range(3): chk(f"e1^2 e2: N^-{m} = 0", g[m])
    S = p*(2*j + k)
    chk("e1^2 e2: N^-3 = (pj/2)^2 (pk/2) (p+1+S)(p+2+S)/(2 p^2)", g[3] - (p*j/2)**2*(p*k/2)*(p + 1 + S)*(p + 2 + S)/(2*p**2))
    chk("control: S = p(j + 2k)", g[3] - (p*j/2)**2*(p*k/2)*(p + 1 + p*(j + 2*k))*(p + 2 + p*(j + 2*k))/(2*p**2), must_fail=True)
    print("e1^2 e2 N^-3 =", sp.factor(g[3]))
elif part == 'Q':
    g = nat[(4, 0)]
    for m in range(4): chk(f"e1^4: N^-{m} = 0 (p = 5/2)", g[m])
    chk("e1^4: N^-4 = Lagrange(m=4) in eps-form (p = 5/2)", g[4] - (p*j/2)**4*L(4*p*j, 4))
    print("e1^4 N^-4 =", sp.factor(g[4]))
elif part == 'H':
    g = nat[(1, 1)]
    chk("e1 e2: N^-3 = 0 (p = 3/2)", g[3])
    chk("e1 e2: N^-4 is beta-free (p = 3/2)", sp.diff(g[4], be))
    h2 = (p + 1)*(p + 2)*(3*p**2 + 2*p + 1)/(8*p**2) + (p + 2)*(2*p**3 - p**2 - 7*p - 6)*al**2/(16*p**2)
    chk("j = k = 1: N^-4 = p^2 h2/2 (JZC_M4_proof h2, p = 3/2)", g[4].subs({j: 1, k: 1}) - p**2*h2/2)
    print("h(j,k) := e1 e2 natural N^-4 at p = 3/2:", sp.factor(g[4]))
    print("symmetric in (j, k):", sp.simplify(g[4] - g[4].subs({j: k, k: j}, simultaneous=True)) == 0)
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE"); assert ok
