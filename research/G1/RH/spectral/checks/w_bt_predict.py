"""JZC_W_BT §5 (Rule X): PRE-REGISTRATION of the half-integer pole residues of the engine's N^-7 zeta-layer coefficient g1[7],
from the lip-mismatch companion of w_bt_core (derived, not fitted), BEFORE any KORD = 7 engine run exists.

For the lattice frame (beta = nu = alpha, as in w_exact_poles.py) at fixed rational p, w_bt_core (KORD = 5) gives the natural-form
companion C(N) = (p+2)^{2rho+1} Phi_nu(rho) N^{-2rho-2} sum_k c_k(rho) N^{-k} per unit mu of exp(-mu z^rho), k <= 4.
The continued (symbolic-j) response g1[k] (per unit mu C(2j, j), w_exact_engine, natural form) plus C(N)/C(2rho, rho) is the full
first-order response (Theorem BT); its finiteness at half-integer rho0 forces, for every k,
  Res_{j=rho0} g1[k] = - (p+2)^{2rho0+1} c_{k-2rho0-2}(rho0) Res_{rho=rho0}[Phi_nu(rho)/C(2rho, rho)]       (P-k-rho0)
(c_k regular at rho0, asserted). Registered here for k = 7, rho0 in {1/2, 3/2, 5/2} (uses c_4, c_2, c_0), together with:
  P-6: g1[6] = 0;  P-poles: the j-poles of g1[7] are exactly 1/2, 3/2, 5/2 and simple.
The predictions are written to w_bt_predictions.json with a timestamp; w_bt_poles7.py asserts that its engine run started later.
Usage: python w_bt_predict.py 3/2 3"""
import os, sys, json, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["KORD"] = "5"; os.environ.setdefault("SHI", "20"); os.environ.pop("DECOUPLE", None); os.environ.pop("SZOFF", None)
import sympy as sp
import w_exact_lag as L
here = os.path.dirname(os.path.abspath(__file__))
for fn in [__file__, os.path.join(here, "w_bt_core.py"), os.path.join(here, "w_bt_engine.py"), L.__file__]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
J, nu = sp.Symbol('j'), sp.Symbol('alpha')
preds = {}
for ps in sys.argv[1:]:
    os.environ["PVAL"] = ps
    for m in ("w_bt_core", "w_bt_engine"):
        sys.modules.pop(m, None)
    import w_bt_core as C
    pv = sp.Rational(ps); t0 = time.time()
    r = C.run(5)
    c = [sp.factor(x.as_expr()) for x in r['comp_nat'][:5]]
    print(f"--- p = {pv}: companion through N^-4 ({time.time() - t0:.0f}s)", flush=True)
    for k, x in enumerate(c): print(f"   c_{k} = {x}", flush=True)
    P = {}
    for r0 in (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2)):
        k = 7 - int(2*r0 + 2)
        ck = c[k]
        assert sp.denom(sp.together(ck)).subs(J, r0) != 0, "c_k singular at rho0"
        val = sp.factor(-(pv + 2)**(2*r0 + 1)*ck.subs(J, r0)*L.PhiC_residue(r0).subs(L.al, nu))
        P[f"Res_{r0}_g1_7"] = str(val)
        print(f"   PREDICTION Res_(j={r0}) g1[7] = {val}", flush=True)
    P["c"] = [str(x) for x in c]
    preds[str(pv)] = P
out = {"written": time.strftime("%Y-%m-%d %H:%M:%S"), "unix": time.time(), "p": preds,
       "also": "g1[6] = 0; j-poles of g1[7] exactly 1/2, 3/2, 5/2, simple"}
# Registration guard (2026-11-05, adversarial review): a registration is never rewritten. To re-register on purpose, set
# W_REREGISTER=1 and commit the new json BEFORE running the test, so git (not mtimes) orders prediction and test.
if os.path.exists(os.path.join(here, "w_bt_predictions.json")) and os.environ.get("W_REREGISTER") != "1":
    print("w_bt_predictions.json exists: registration is never rewritten (set W_REREGISTER=1 to override)"); sys.exit(0)
json.dump(out, open(os.path.join(here, "w_bt_predictions.json"), "w"), indent=1)
print(f"written w_bt_predictions.json at {out['written']}")
