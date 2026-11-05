"""JZC_W_exact §3: the half-integer poles of the continued (symbolic-j) zeta-layer response and the branched hard-edge companion.
Exact engine (w_exact_engine.py = m4_rh_exact2 copy) at fixed rational p, symbolic (alpha = nu = beta, j), KORD = 5, first order in
mu_j (EO = 1), mu normalised by C(2j, j); g1[k] = natural-form coefficient of N^{-k} (JZC_M4 §6 convention).
History (Rule X): the predictions P0-P2 were registered by w_exact_predict.py (w_exact_predictions.json, 09:38:30) and tested by
w_exact_poles_prereg.py (the first version of this script, unchanged) -> w_exact_poles_prereg_A/B.out (runs started 09:39:09):
P0 and P1 held at all registered p; P2 (the "reflection" form of the subleading branched dressing) FAILED at all registered p,
i.e. P2 is REFUTED. This version re-runs the registered p (P0, P1 asserted against the registered values; the registered P2 is kept
as a check that must fail, labelled REFUTED) and adds post hoc p values (not registered), where P0 and P1 are asserted from the
same closed form H(rho) (now a tested law, labelled post hoc). It caches the residues for w_exact_xfit.py (tmp/w_exact/).
Asserted at each p, identically in (nu, j): g1[0] = g1[2] = g1[4] = 0, g1[1] = p j/2, g1[3]/g1[1] = A_j + B_j nu^2, the j-poles of
g1[5] are exactly j = 1/2, 3/2 (simple), P0: Res_{1/2} g1[3] = -Res_{1/2} H, P1: Res_{3/2} g1[5] = -Res_{3/2} H, with
H(rho) = (1/2)(p rho + 2 rho + 1)(p+2)^{2rho+1} Phi_nu(rho)/C(2rho, rho).
Controls (must fail): P1 with kappa^{-rho} (skipped at p = -1, where kappa = 1); P1 with the opposite sign; registered P2 (REFUTED); P2 with g(rho*) -> 0.
Usage: python w_exact_poles.py 3/2 2 3 ...   (registered: 1/2 3/2 2 5/2 3; any other rational p is post hoc)"""
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
CACHE = os.path.join(here, "..", "..", "..", "..", "..", "tmp", "w_exact"); os.makedirs(CACHE, exist_ok=True)
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
chk(f"Rule X: predictions written {pred['written']} before this run", pred["unix"] < T_START)
nu, J = sp.Symbol('alpha'), sp.Symbol('j')
def A(w, p): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def B(w, p): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)
def res(e, j0): return sp.factor(sp.cancel((J - j0)*e).subs(J, j0))
def ResH(r0, p, kexp=None):
    kexp = 2*r0 + 1 if kexp is None else kexp
    return sp.factor(sp.Rational(1, 2)*(p*r0 + 2*r0 + 1)*(p + 2)**kexp*L.PhiC_residue(r0))
h, t32 = sp.Rational(1, 2), sp.Rational(3, 2)
for ps in sys.argv[1:]:
    p = sp.Rational(ps); reg = str(p) in pred["p"]; tag = "registered" if reg else "post hoc"
    os.environ["PVAL"] = ps
    import importlib
    if "w_exact_engine" in sys.modules: del sys.modules["w_exact_engine"]
    X = importlib.import_module("w_exact_engine"); assert X.p == X.K(p) and X.SZ == X.al
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu='sym'); g1 = [x.as_expr() for x in g[1]]
    print(f"--- p = {p} ({tag}): engine KORD = {X.KORD} done ({time.time() - t0:.0f}s)", flush=True)
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
    if reg:
        P = {k: sp.sympify(v, locals={"alpha": nu}) for k, v in pred["p"][str(p)].items()}
        chk(f"p={p}: P0 Res_(j=1/2) g1[3] = registered", sp.simplify(r0 - P["P0"]) == 0)
        chk(f"p={p}: P1 Res_(j=3/2) g1[5] = registered (leading branched term, rho = 3/2)", sp.simplify(r1 - P["P1"]) == 0)
        chk(f"p={p}: registered P2 (reflection rho* = rho + (2rho+1)/p) -- REFUTED", sp.simplify(r2 - P["P2"]) == 0, must_fail=True)
    else:
        chk(f"p={p} (post hoc): P0 Res_(j=1/2) g1[3] = -Res_(1/2) H", sp.simplify(r0 + ResH(h, p)) == 0)
        chk(f"p={p} (post hoc): P1 Res_(j=3/2) g1[5] = -Res_(3/2) H", sp.simplify(r1 + ResH(t32, p)) == 0)
    if p + 2 != 1:                     # at p = -1, kappa = (p+2)^-2 = 1 and this control is degenerate (it holds trivially)
        chk(f"p={p}: control P1 with kappa^(-rho)", sp.simplify(r1 + ResH(t32, p, kexp=3)) == 0, must_fail=True)
    else:
        print(f"   p={p}: control 'kappa^(-rho)' skipped: kappa = 1 at p = -1 (degenerate)", flush=True)
    chk(f"p={p}: control P1 with the opposite sign", sp.simplify(r1 - ResH(t32, p)) == 0, must_fail=True)
    chk(f"p={p}: control P2 with g(rho*) -> 0 (Res_(1/2) g1[5] = 0)", sp.simplify(r2) == 0, must_fail=True)
    Xs = sp.factor(-r2/ResH(h, p))
    print(f"   X(p, nu) := -Res_(1/2) g1[5] / Res_(1/2) H = {Xs}  (post hoc: relative N^-2 dressing of the branched series at rho = 1/2)", flush=True)
    json.dump({"p": str(p), "registered": reg, "r0": str(r0), "r1": str(r1), "r2": str(r2), "X": str(Xs),
               "g1_5": str(sp.factor(g1[5])), "time": time.strftime("%Y-%m-%d %H:%M:%S")},
              open(os.path.join(CACHE, f"poles_p{str(p).replace('/', '_')}.json"), "w"), indent=1)
print(f"total {NCHK} checks ({time.time() - T_START:.0f}s)")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
