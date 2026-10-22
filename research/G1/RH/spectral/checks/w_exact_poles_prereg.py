"""JZC_W_exact §3: test of the PRE-REGISTERED predictions P0-P3 (w_exact_predict.py -> w_exact_predictions.json, written before this
run; asserted via the timestamps) with the exact engine (w_exact_engine.py = m4_rh_exact2 copy) at fixed rational p, symbolic
(alpha = nu = beta, j), KORD = 5, first order in mu_j (EO = 1), mu normalised by C(2j, j).
Usage: python w_exact_poles.py 3/2 2 3   (any subset of the registered p values)
Asserted, identically in (nu, j) at each p: g1[0] = g1[2] = g1[4] = 0, g1[1] = p j/2, g1[3]/g1[1] = A_j + B_j nu^2 (Theorem N.6(ii) at
this p, re-derived), and the residues P0 (j = 1/2, g1[3]), P1 (j = 3/2, g1[5]), P2 (j = 1/2, g1[5]) equal the registered values;
the only poles of g1[5] in j are j = 1/2, 3/2 (simple).
Controls (must fail): P1 with kappa^{-rho} in place of kappa^{-rho-1/2}; P1 with the opposite sign; P2 with rho* replaced by rho;
P2 with the leading coefficient only (g(rho*) -> 0)."""
import os, sys, json, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
T_START = time.time()
os.environ.setdefault("KORD", "5"); os.environ.setdefault("SHI", "18"); os.environ["EO"] = "1"
os.environ.pop("DECOUPLE", None); os.environ.pop("SZOFF", None)
import sympy as sp
import w_exact_lag as L
here = os.path.dirname(os.path.abspath(__file__))
for fn in [__file__, L.__file__, os.path.join(here, "w_exact_engine.py"), os.path.join(here, "w_exact_predict.py")]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
pred = json.load(open(os.path.join(here, "w_exact_predictions.json")))
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
chk(f"Rule X: predictions written {pred['written']} before this run started {time.strftime('%H:%M:%S', time.localtime(T_START))}",
    pred["unix"] < T_START)
nu, J = sp.Symbol('alpha'), sp.Symbol('j')
def A(w, p): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def B(w, p): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)
def res(e, j0): return sp.factor(sp.cancel((J - j0)*e).subs(J, j0))
def ResH(r0, p, kexp=None):
    kexp = 2*r0 + 1 if kexp is None else kexp
    return sp.factor(sp.Rational(1, 2)*(p*r0 + 2*r0 + 1)*(p + 2)**kexp*L.PhiC_residue(r0))
h, t32 = sp.Rational(1, 2), sp.Rational(3, 2)
for ps in sys.argv[1:]:
    p = sp.Rational(ps); assert str(p) in pred["p"], f"p = {p} not registered"
    os.environ["PVAL"] = ps
    import importlib
    if "w_exact_engine" in sys.modules: del sys.modules["w_exact_engine"]
    X = importlib.import_module("w_exact_engine"); assert X.p == X.K(p) and X.SZ == X.al
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu='sym'); g1 = [x.as_expr() for x in g[1]]
    print(f"--- p = {p}: engine KORD = {X.KORD} done ({time.time() - t0:.0f}s)", flush=True)
    chk(f"p={p}: g1[0] = g1[2] = g1[4] = 0", g1[0] == 0 and g1[2] == 0 and sp.simplify(g1[4]) == 0)
    chk(f"p={p}: g1[1] = p j/2", sp.simplify(g1[1] - p*J/2) == 0)
    chk(f"p={p}: g1[3]/g1[1] = A_j + B_j nu^2", sp.simplify(g1[3]/g1[1] - A(J, p) - B(J, p)*nu**2) == 0)
    den = sp.factor(sp.denom(sp.cancel(sp.together(g1[5]))))
    jpoles = [fa for fa in sp.factor_list(den)[1] if fa[0].has(J)]
    print(f"   g1[5] denominator: {den}", flush=True)
    chk(f"p={p}: the j-poles of g1[5] are exactly j = 1/2, 3/2, simple",
        sorted([sp.solve(fa[0], J)[0] for fa in jpoles]) == [h, t32] and all(fa[1] == 1 for fa in jpoles))
    r0 = res(g1[3], h); r1 = res(g1[5], t32); r2 = res(g1[5], h)
    print(f"   Res_(j=1/2) g1[3] = {r0}\n   Res_(j=3/2) g1[5] = {r1}\n   Res_(j=1/2) g1[5] = {r2}", flush=True)
    P = {k: sp.sympify(v, locals={"alpha": nu}) for k, v in pred["p"][str(p)].items()}
    chk(f"p={p}: P0 Res_(j=1/2) g1[3] = registered", sp.simplify(r0 - P["P0"]) == 0)
    chk(f"p={p}: P1 Res_(j=3/2) g1[5] = registered (leading branched term, rho = 3/2)", sp.simplify(r1 - P["P1"]) == 0)
    chk(f"p={p}: P2 Res_(j=1/2) g1[5] = registered (reflection rho* = rho + (2rho+1)/p)", sp.simplify(r2 - P["P2"]) == 0)
    chk(f"p={p}: control P1 with kappa^(-rho)", sp.simplify(r1 + ResH(t32, p, kexp=3)) == 0, must_fail=True)
    chk(f"p={p}: control P1 with the opposite sign", sp.simplify(r1 - ResH(t32, p)) == 0, must_fail=True)
    chk(f"p={p}: control P2 with rho* -> rho = 1/2 inside g (g(1/2) is singular: use g at rho* = 1/2 + 1/p)",
        sp.simplify(r2 + ResH(h, p)*(A(h + 1/p, p) + B(h + 1/p, p)*nu**2)) == 0, must_fail=True)
    chk(f"p={p}: control P2 with g(rho*) -> 0", sp.simplify(r2) == 0, must_fail=True)
print(f"total {NCHK} checks ({time.time() - T_START:.0f}s)")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
