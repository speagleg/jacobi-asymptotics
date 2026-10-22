"""JZC_W_BT §5: the PRE-REGISTERED test (w_bt_predictions.json, written by w_bt_predict.py before this run) of the companion's
N^-2 and N^-4 dressings against the engine's continued zeta layer at N^-7.

Engine: w_bt_engine.py (= w_exact_engine = m4_rh_exact2 copy; the w_bt change only exports objects), fixed rational p, symbolic
(alpha = nu = beta, j), KORD = 7, first order in mu_j (EO = 1), mu normalised by C(2j, j); g1[k] = natural-form coefficient of N^-k.
Asserted at each registered p, identically in (nu, j):
  g1[0] = g1[2] = g1[4] = g1[6] = 0, g1[1] = p j/2, g1[3]/g1[1] = A_j + B_j nu^2 (Theorem N.6(ii) at symbolic j);
  the j-poles of g1[7] are exactly 1/2, 3/2, 5/2, simple (registered);
  Res_{j=rho0} g1[7] = registered value, rho0 = 1/2 (tests c_4), 3/2 (tests c_2), 5/2 (tests c_0 = H) (registered).
Controls (must fail): rho0 = 1/2 with c_4 -> 0; rho0 = 3/2 with c_2 -> 0; rho0 = 1/2 with the opposite sign.
Usage: python w_bt_poles7.py 3/2   (one p per process; run several in parallel)"""
import os, sys, json, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
T_START = time.time()
os.environ["KORD"] = os.environ.get("KORD", "7"); os.environ.setdefault("SHI", "24"); os.environ["EO"] = "1"
os.environ.pop("DECOUPLE", None); os.environ.pop("SZOFF", None)
ps = sys.argv[1]; os.environ["PVAL"] = ps
import sympy as sp
import w_exact_lag as L
here = os.path.dirname(os.path.abspath(__file__))
for fn in [__file__, os.path.join(here, "w_bt_engine.py"), os.path.join(here, "w_bt_predict.py"), os.path.join(here, "w_bt_core.py"), L.__file__]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
pred = json.load(open(os.path.join(here, "w_bt_predictions.json")))
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
chk(f"Rule X: predictions written {pred['written']} before this run started ({time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(T_START))})",
    pred["unix"] < T_START)
nu, J = sp.Symbol('alpha'), sp.Symbol('j')
p = sp.Rational(ps); P = pred["p"][str(p)]
def A(w): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def B(w): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)
def res(e, j0): return sp.factor(sp.cancel((J - j0)*e).subs(J, j0))
import w_bt_engine as X
assert X.p == X.K(p) and X.SZ == X.al and X.KORD == 7
t0 = time.time(); d, f, g = X.run(verbose=False, jmu='sym'); g1 = [x.as_expr() for x in g[1]]
print(f"--- p = {p}: engine KORD = 7 done ({time.time() - t0:.0f}s)", flush=True)
chk(f"p={p}: g1[0] = g1[2] = g1[4] = g1[6] = 0", all(sp.simplify(g1[k]) == 0 for k in (0, 2, 4, 6)))
chk(f"p={p}: g1[1] = p j/2", sp.simplify(g1[1] - p*J/2) == 0)
chk(f"p={p}: g1[3]/g1[1] = A_j + B_j nu^2", sp.simplify(g1[3]/g1[1] - A(J) - B(J)*nu**2) == 0)
den = sp.factor(sp.denom(sp.cancel(sp.together(g1[7]))))
jp = [fa for fa in sp.factor_list(den)[1] if fa[0].has(J)]
print(f"   g1[7] denominator: {den}", flush=True)
chk(f"p={p}: registered: j-poles of g1[7] exactly 1/2, 3/2, 5/2, simple",
    sorted([sp.solve(fa[0], J)[0] for fa in jp]) == [sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2)] and all(fa[1] == 1 for fa in jp))
c = [sp.sympify(x, locals={"alpha": nu, "j": J}) for x in P["c"]]
for r0 in (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2)):
    rv = res(g1[7], r0); pv = sp.sympify(P[f"Res_{r0}_g1_7"], locals={"alpha": nu})
    print(f"   Res_(j={r0}) g1[7] = {rv}", flush=True)
    chk(f"p={p}: registered Res_(j={r0}) g1[7] = -(p+2)^(2rho0+1) c_{7 - int(2*r0 + 2)}(rho0) Res(Phi/C)", sp.simplify(rv - pv) == 0)
r12 = res(g1[7], sp.Rational(1, 2)); r32 = res(g1[7], sp.Rational(3, 2))
chk(f"p={p}: control rho0 = 1/2 with c_4 -> 0 (residue would vanish)", sp.simplify(r12) == 0, must_fail=True)
chk(f"p={p}: control rho0 = 3/2 with c_2 -> 0 (residue would vanish)", sp.simplify(r32) == 0, must_fail=True)
chk(f"p={p}: control rho0 = 1/2 with the opposite sign",
    sp.simplify(r12 + sp.sympify(P["Res_1/2_g1_7"], locals={"alpha": nu})) == 0, must_fail=True)
print(f"total {NCHK} checks ({time.time() - T_START:.0f}s)")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
