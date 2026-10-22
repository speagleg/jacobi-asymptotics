"""Theorem H, chain link C-2 (REVIEW_JZC_M3a_H_pgt1_chain_A.md; JZC_M3a_H.md §3.3): E3 Lemma E3.7 for the DECOUPLED model
M(beta, nu), with the Szego exponent beta and the Bessel order nu = alpha as INDEPENDENT symbols.

E3 Lemma E3.7 (second_order/E3.md §6): the 1/n coefficient of sqrt((Q1)12 (Q1)21)/c is d1 + c p M_mu(4c), exactly linear in mu,
for every mu (all orders). Its proof (second_order/checks/check_e3_gauge.py) is a sympy identity for the residues of
Delta_1^mu = G_mu Delta_1^mod G_mu^{-1} (E3 Lemma E3.4(iii)) at 4c and 0, with the model Laurent data
    Delta_1^mod = B_r/w^2 + A_r/w + O(1) at 4c (w = z - 4c),   A_0/z + O(1) at 0,
HARD-CODED there with a single exponent alpha (beta = nu). Here those data are NOT typed in: they are read from the exact engine
m4_rh_exact2.py (DECOUPLE=1, field Q(p, alpha, j, beta), alpha = Bessel order nu, beta = Szego exponent; c = 1 as in the engine),
from its local variables Dr[1], D0[1] (captured at the return of run() with sys.settrace; the engine is not modified).

Route 1 (all orders in mu; the check_e3_gauge identity with beta != nu): with M4 := M_mu(4c), M4p := M_mu'(4c), M0 := M_mu(0) free
symbols, asserted identically in (p, alpha, beta, M4, M4p, M0):
  det G(4c) = 1;  G(4c) B_r G(4c)^{-1} = B_r;  [G(0), A_0(beta, nu)] = 0;
  e(M) - e(0) = c p M4 (c = 1), where e = i(A21 - A12)/(2c) of Res_0 + Res_4c;  e(0) = d1 = -p(beta+1)/2;
  full shift Res_4c - A_r = M4 c^2 p [[M4 c - beta - 1, -i(M4 c - beta - 2)], [-i(M4 c - beta), -(M4 c - beta - 1)]].
Also: A_r, B_r are nu-free, A_0 is beta-free, and at beta = nu all three equal check_e3_gauge.py's data (c = 1).
Route 2 (independent of route 1's residue algebra: the engine's own gauge, small-norm recursion and extraction, dual numbers to
order EO = 3 in mu_j): the 1/n coefficient has mu_j-response exactly p Q_j(4) at first order and 0 at orders 2, 3, for integer
j = 1, 2, 3, and for SYMBOLIC j (mu normalised by C(2j, j): response p j/2), identically in (p, alpha, beta[, j]).
Controls (must fail, asserted to fail): the shift formula with nu in place of beta; e - e0 = c p M(0); soft-edge data nu-dependent
(i.e. A_r(beta) = A_r(nu)); G(4c) commuting with A_r; route 2 response at the wrong point
(p Q_j(0), j >= 2) or zero.
Rule X: nothing is fitted; the model data come from the engine, the identities are exact rational-function identities."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["DECOUPLE"] = "1"; os.environ["KORD"] = "1"; os.environ["EO"] = "3"; os.environ.setdefault("SHI", "10")
import m4_rh_exact2 as X
import sympy as sp
from math import comb

X._provenance(__file__, X)
assert X.DECOUPLE and X.SZ == X.be, "engine not in decoupled mode"
NCHK = 0; ok = True
def chk(label, is_identity, must_fail=False):
    """record a check: an identity (must hold) or a control (the identity must FAIL)"""
    global NCHK, ok
    NCHK += 1; passed = (not is_identity) if must_fail else is_identity; ok &= passed
    tag = "CONTROL (must fail)" if must_fail else "identity"
    print(f"[{NCHK:2d}] {tag}: {label}: {'holds' if is_identity else 'FAILS'} -> {'PASS' if passed else 'FAIL'}", flush=True)
def zero(e): return sp.simplify(sp.expand(e)) == 0
def mzero(Mx): return all(zero(e) for e in Mx)

def run_capture(jmu=None, shi=None):
    if shi is not None: X.S.HI = shi
    cap = {}
    def tr(frame, event, arg):
        if frame.f_code is X.run.__code__:
            def loc(f, ev, a):
                if ev == "return": cap.update(f.f_locals)
                return loc
            return loc
        return None
    sys.settrace(tr)
    try: out = X.run(verbose=False, jmu=jmu)
    finally: sys.settrace(None)
    return out, cap

def g2s(g): return g.a.as_expr() + sp.I * g.b.as_expr()          # eps^0 part of an engine element, as a sympy expression
def laurent(D, t): return sp.Matrix(2, 2, lambda i, j: g2s(D[i][j].get(t)))

# ---------------- model Laurent data from the engine (decoupled, no band factor) ----------------
t0 = time.time()
(d, f), cap = run_capture(None, 10)
Dr1, D01 = cap["Dr"][1], cap["D0"][1]
Br, Ar, A0 = laurent(Dr1, -2), laurent(Dr1, -1), laurent(D01, -1)
p, al, be = sp.Symbol("p"), sp.Symbol("alpha"), sp.Symbol("beta")
print("B_r =", Br.applyfunc(sp.factor)); print("A_r =", Ar.applyfunc(sp.factor)); print("A_0 =", A0.applyfunc(sp.factor))
# lowest Laurent order over ALL entries (Rule R review B, REVIEW_JZC_M3a_H_assembly_B.md B-4; was D01[0][0] only)
lo0 = min(D01[i][j].trim().lo for i in range(2) for j in range(2)); lor = min(Dr1[i][j].trim().lo for i in range(2) for j in range(2))
print(f"lowest Laurent order over all entries: {lo0} at 0, {lor} at 4c")
chk("no z^{-2} or deeper term at 0; no w^{-3} or deeper at 4c (all entries)", lo0 >= -1 and lor >= -2
    and all(laurent(D01, t) == sp.zeros(2) for t in range(min(lo0, -1), -1)))
(d2_, f2_), cap2 = run_capture(None, 14)
chk("Laurent data stable under truncation SHI 10 -> 14", mzero(laurent(cap2["Dr"][1], -2) - Br) and mzero(laurent(cap2["Dr"][1], -1) - Ar)
    and mzero(laurent(cap2["D0"][1], -1) - A0))
X.S.HI = 10
chk("A_r, B_r are nu-free (soft edge sees only beta)", not (Ar.has(al) or Br.has(al)))
chk("A_0 is beta-free (hard edge sees only nu)", not A0.has(be))
# check_e3_gauge.py's hard-coded data (single exponent), at c = 1
Ar_e3 = sp.Rational(1, 48) * sp.Matrix([[12*al**2*p + 24*al*p + 11*p + 2, -sp.I*(12*al**2*p + 48*al*p + 49*p + 2)],
                                         [-sp.I*(12*al**2*p + p + 2), -(12*al**2*p + 24*al*p + 11*p + 2)]])
Br_e3 = (5*p/12) * sp.Matrix([[1, -sp.I], [-sp.I, -1]])
A0_e3 = (p + 2)*(4*al**2 - 1)/16 * sp.Matrix([[1, sp.I], [sp.I, -1]])
chk("at beta = nu: (A_r, B_r, A_0) = check_e3_gauge.py data (c = 1)", mzero(Ar.subs(be, al) - Ar_e3) and mzero(Br - Br_e3)
    and mzero(A0 - A0_e3))
chk("A_r(beta) = A_r(nu), i.e. soft edge independent of beta", mzero(Ar - Ar.subs(be, al)), must_fail=True)
chk("engine d1 = -p(beta+1)/2", zero(d[1].as_expr() + p*(be + 1)/2))
print(f"   (model data: {time.time() - t0:.0f}s)", flush=True)

# ---------------- route 1: the gauge residue identity, all orders in mu (check_e3_gauge.py with beta != nu) ----------------
c = 1
M4, M4p, M0, w = sp.symbols("M4 M4p M0 w")
T = sp.Matrix([[1, 1], [sp.I, -sp.I]]) / sp.sqrt(2); Ti = T.inv()
Mz = M4 + M4p*w
H = (4*c + w)*w*Mz**2/4                                     # h^2 = Rr^2 M^2/4 = O(w): three terms suffice for w^0, w^1
ch = sum(H**m/sp.factorial(2*m) for m in range(3)); Sg = Mz/2*sum(H**m/sp.factorial(2*m + 1) for m in range(3))
G = T*sp.Matrix([[ch, -w*Sg], [-(4*c + w)*Sg, ch]])*Ti
G = G.applyfunc(lambda e: sp.expand(sp.series(e, w, 0, 2).removeO()))
Gw0 = G.applyfunc(lambda e: e.coeff(w, 0)); Gw1 = G.applyfunc(lambda e: e.coeff(w, 1))
chk("det G(4c) = 1", zero(Gw0.det() - 1))
Gw0i = Gw0.inv(); Gi1 = -Gw0i*Gw1*Gw0i
Res = (Gw0*Ar*Gw0i + Gw1*Br*Gw0i + Gw0*Br*Gi1).applyfunc(sp.expand)
chk("G(4c) B_r G(4c)^{-1} = B_r", mzero(Gw0*Br*Gw0i - Br))
Gz0 = T*sp.Matrix([[1, 2*c*M0], [0, 1]])*Ti                 # G(0): Rr = 0, S(0) = M0/2
chk("[G(0), A_0(beta, nu)] = 0 (Res_0 does not move)", mzero(Gz0*A0 - A0*Gz0))
chk("G(4c) commutes with A_r (Res_4c would not move)", mzero(Gw0*Ar - Ar*Gw0), must_fail=True)
e = sp.expand(sp.I*((A0 + Res)[1, 0] - (A0 + Res)[0, 1])/(2*c)); e0 = sp.expand(sp.I*((A0 + Ar)[1, 0] - (A0 + Ar)[0, 1])/(2*c))
chk("e(0) = d1 = -p(beta+1)/2 (residue route = engine)", zero(e0 + p*(be + 1)/2) and zero(e0 - d[1].as_expr()))
chk("E3.7 for M(beta, nu): e(M) - e(0) = c p M(4c), all orders in mu (M4p, M0 drop out)", zero(e - e0 - c*p*M4))
print("   e(M) - e(0) =", sp.factor(sp.simplify(e - e0)), flush=True)
chk("control: e(M) - e(0) = c p M(0)", zero(e - e0 - c*p*M0), must_fail=True)
shift = lambda x: M4*c**2*p*sp.Matrix([[M4*c - x - 1, -sp.I*(M4*c - x - 2)], [-sp.I*(M4*c - x), -(M4*c - x - 1)]])
chk("full shift Res_4c - A_r = M4 c^2 p [[M4c-beta-1, ...]] (Szego exponent beta)", mzero(Res - Ar - shift(be)))
chk("control: full shift with the Bessel order nu in place of beta", mzero(Res - Ar - shift(al)), must_fail=True)
for k in range(1, 40):
    assert sum(4**(k - 1 - j)*comb(2*j, j) for j in range(k))*2 == k*comb(2*k, k)
chk("Q_k(4c) = c^(k-1) k C(2k,k)/2 for k < 40 (combinatorial, beta/nu-free)", True)
print(f"   (route 1: {time.time() - t0:.0f}s)", flush=True)

# ---------------- route 2: the engine's own gauge + small norm + extraction, dual numbers to order 3 in mu_j ----------------
for jm in (1, 2, 3, "sym"):
    t1 = time.time()
    (dj, fj, gz), capj = run_capture(jm, 10)
    ee = capj["e"]                                           # ee[m][k]: coefficient of eps^m n^{-k} in sqrt(Q12 Q21)/c
    jsym = sp.Symbol("j")
    if jm == "sym":
        q4, q0 = jsym/2, jsym/(2*(2*jsym - 1))               # Q_j/C(2j,j) at 4 and at 0 (c = 1)
    else:
        q4 = sum(comb(2*i, i)*4**(jm - 1 - i) for i in range(jm)); q0 = comb(2*(jm - 1), jm - 1)
    chk(f"j={jm}: d1 at mu = 0 is -p(beta+1)/2", zero(ee[0][1].as_expr() + p*(be + 1)/2))
    chk(f"j={jm}: first-order mu_j response of the 1/n coefficient = p Q_j(4)", zero(ee[1][1].as_expr() - p*q4))
    chk(f"j={jm}: second- and third-order responses vanish (exactly linear to order 3)", zero(ee[2][1].as_expr()) and zero(ee[3][1].as_expr()))
    chk(f"j={jm}: control: first-order response = 0 (mu_j invisible)", zero(ee[1][1].as_expr()), must_fail=True)
    if jm != 1:                                              # Q_1 is constant, so Q_1(0) = Q_1(4): no control there
        chk(f"j={jm}: control: first-order response = p Q_j(0)", zero(ee[1][1].as_expr() - p*q0), must_fail=True)
    print(f"   (route 2, j={jm}: {time.time() - t1:.0f}s)", flush=True)

print(f"total {time.time() - t0:.0f}s")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
