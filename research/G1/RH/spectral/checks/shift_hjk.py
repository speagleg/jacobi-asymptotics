"""JZC_SHIFT §5.3: a closed form, in (p, alpha, j, k), of the second-order dressing h(j, k) := natural N^-4 coefficient of the e1 e2
layer (e-units; lattice beta = nu = alpha), from the Toda flow of the integer layers (formal Toda engine, transfer recursion).
 Step 1 (exact at each point, given Theorem T): h(j, k) for integer 1 <= j <= k <= 9, symbolic (p, alpha), with f2 and a2 kept as free
         symbols: h = H0 + Hf f2 + Ha a2 (linear: relative order N^-2).
 Step 2 (interpolation; Rule X: FITTED in (j, k)): each of H0, Hf, Ha times (2j-1)(2k-1) is matched to a symmetric polynomial in (j, k) of
         total degree <= DEG with coefficients in Q(p); the fit uses the pairs with j + k <= 12 and is asserted at all other computed
         pairs (j, k <= 9) and against the exact symbolic-(j, k) engine output at p = 3/2 (w2_exact H) — independent checks.
 Step 3: the closed form is written to tmp/shift/hjk_closed.json and printed; shift_predict2.py registers its value at p = 5/2 for
         symbolic (j, k) BEFORE the engine run R7 (shift_exact2.py)."""
import os, sys, json, glob, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from shift_common import *
from sympy.polys.fields import field
from sympy import QQ
import importlib.util
provenance(__file__, os.path.join(HERE, 'shift_common.py'), os.path.join(HERE, 'shift_dressing.py'))
C = Checks()
P, AL, BE, J, KK, F2s, A2s = sp.symbols('p alpha beta j k f2 a2')
z = lambda e: sp.simplify(sp.cancel(sp.together(e))) == 0
ex = lambda c: sp.sympify(str(c.as_expr()))
DEL = (AL + 1)/2


class FTfast(FT):
    """as in shift_dressing.py: (J^j)_{n,n+r} by the transfer recursion"""
    def Jpow(s, a, b, j, r, cache):
        def sh(X, name, k):
            if (name, k) not in cache: cache[(name, k)] = s.shift(X, k) if k != 0 else X
            return cache[(name, k)]
        one = {(0, tuple([0]*s.r)): [s.one] + [s.zero]*s.D}
        v = {0: one}
        for i in range(j):
            rem = j - i - 1; nv = {}
            for m, X in v.items():
                for d in (0, 1, -1):
                    m2 = m + d
                    if abs(m2 - r) > rem: continue
                    f = sh(a, 'a', m) if d == 0 else (sh(b, 'b', m + 1) if d == 1 else sh(b, 'b', m))
                    nv[m2] = s.add(nv[m2], s.mul(X, f)) if m2 in nv else s.mul(X, f)
            v = nv
        return v.get(r, {})


JMAX = int(os.environ.get("JMAX", "9")); DEG = int(os.environ.get("DEG", "8"))
K, p, al, f2, a2 = field('p,alpha,f2,a2', QQ)
dl = (al + 1)/2; m_ = al/2 + 1
b0 = [K(1), -p*dl, p*(p + 1)*dl**2/2 + f2, K(0), K(0)]
a0 = [2*K(1), -2*p*m_, 2*(p*(p + 1)*m_**2/2 + a2), K(0), K(0)]
cache = os.path.join(SHC, f"hjk_data_J{JMAX}.json")
if os.path.exists(cache):
    data = {tuple(map(int, k.split(','))): [sp.sympify(x) for x in v] for k, v in json.load(open(cache)).items()}
else:
    data = {}; t0 = time.time()
    for j in range(1, JMAX + 1):
        for k in range(j, JMAX + 1):
            if j != k:
                a, b, _ = FTfast(K, p, (j, k), 4, 2).flow(a0, b0)
                n = to_natural([ex(c) for c in b[(1, (1, 1))]], (j + k + 1)*P, (1, 1), (j, k), DEL)
            else:
                a, b, _ = FTfast(K, p, (j,), 4, 2).flow(a0, b0)
                n = to_natural([2*ex(c) for c in b[(1, (2,))]], (2*j + 1)*P, (1, 1), (j, j), DEL)
            assert z(n[3]) and z(n[2] - LB((1, 1), (j, k), P)), (j, k)
            h = sp.expand(sp.cancel(n[4]))
            parts = [sp.factor(h.subs({F2s: 0, A2s: 0})), sp.factor(h.coeff(F2s)), sp.factor(h.coeff(A2s))]
            assert z(h - parts[0] - parts[1]*F2s - parts[2]*A2s)
            data[(j, k)] = parts
        print(f"   j = {j} done ({time.time() - t0:.0f}s)", flush=True)
    json.dump({f"{j},{k}": [str(x) for x in v] for (j, k), v in data.items()}, open(cache, 'w'))
C.check(f"(1) Toda h(j, k), 1 <= j <= k <= {JMAX}: e1 e2 natural N^-2 = LB and N^-3 = 0, h linear in (f2, a2)", True)
# ---- Step 2: symmetric polynomial interpolation of (2j-1)(2k-1) * part
mons = [(a, b) for a in range(DEG + 1) for b in range(a, DEG + 1 - a)]       # symmetric basis j^a k^b + j^b k^a
basis = lambda a, b: (J**a*KK**b + J**b*KK**a) if a != b else J**a*KK**a
fitpairs = [jk for jk in data if jk[0] + jk[1] <= 12]; testpairs = [jk for jk in data if jk not in fitpairs]
print(f"   basis size {len(mons)}, fit pairs {len(fitpairs)}, test pairs {len(testpairs)}", flush=True)
closed = []
for idx, name in enumerate(('H0', 'Hf', 'Ha')):
    cs = sp.symbols(f'c0:{len(mons)}')
    poly = sum(c*basis(a, b) for c, (a, b) in zip(cs, mons))
    eqs = [sp.expand(poly.subs({J: j, KK: k}) - (2*j - 1)*(2*k - 1)*data[(j, k)][idx]) for (j, k) in fitpairs]
    sol = sp.solve(eqs, cs, dict=True)
    assert len(sol) == 1, (name, "interpolation not unique / inconsistent")
    free = [c for c in cs if c not in sol[0]]
    assert not free, (name, "underdetermined", free)
    expr = sp.factor(poly.subs(sol[0]))
    closed.append(sp.factor(expr/((2*J - 1)*(2*KK - 1))))
    okt = all(z(closed[-1].subs({J: j, KK: k}) - data[(j, k)][idx]) for (j, k) in testpairs)
    C.check(f"(2) {name}(j, k): interpolant (fit on j + k <= 12) reproduces all {len(testpairs)} other computed pairs", okt)
    print(f"   {name}(j, k) = {closed[-1]}", flush=True)
f2l = (P + 1)/12 - (P + 2)*AL**2/8; a2l = -(P + 1)/24 + (P + 1)*(P + 2)*AL**2/8
hcl = sp.factor(closed[0] + closed[1]*f2l + closed[2]*a2l)
fn = glob.glob(os.path.join(W2C, "exact_H_*.json"))[0]; print(f"sha256 {os.path.basename(fn)}: {sha(fn)}")
hH = sp.sympify(json.load(open(fn))['nat']['1,1'][4], locals=dict(alpha=AL, beta=BE, j=J, k=KK))
C.check("(2) closed form at p = 3/2 = exact symbolic-(j, k) engine output (w2_exact H), identically in (alpha, j, k)",
        z(hcl.subs(P, sp.Rational(3, 2)) - hH))
C.check("(2) control: closed form with f2 := 0 at p = 3/2 = engine output", z((closed[0] + closed[2]*a2l).subs(P, sp.Rational(3, 2)) - hH),
        must_fail=True)
h2 = (P + 1)*(P + 2)*(3*P**2 + 2*P + 1)/(8*P**2) + (P + 2)*(2*P**3 - P**2 - 7*P - 6)*AL**2/(16*P**2)
C.check("(2) closed form at j = k = 1 = p^2 h2/2 (JZC_M4_proof N.6(ii)), identically in (p, alpha)", z(hcl.subs({J: 1, KK: 1}) - P**2*h2/2))
json.dump({'H0': str(closed[0]), 'Hf': str(closed[1]), 'Ha': str(closed[2]), 'h': str(hcl), 'JMAX': JMAX, 'DEG': DEG},
          open(os.path.join(SHC, 'hjk_closed.json'), 'w'), indent=1)
print("   h(j, k) =", hcl)
C.finish()
