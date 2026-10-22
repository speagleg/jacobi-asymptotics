"""JZC_W §2, step 1 (Rule X): write Conjecture W's predictions for every test spectrum BEFORE any of their measures exists.
Inputs: the spectral data of w_spectra.py only (Z(0), Z(-j), poles, mass tilt), and the model engine m4_rh4 (KORD = 4).
Output: this .out (human-readable, timestamped) and tmp/w_cache/predictions.json (read by w_test.py).
Also (no measure needed):
  W0  internal consistency of the spectral data: Z(0) by the regularised sum vs the closed form; residues vs h Z(-(q+h)).
  W1  the Lommel anchor (Bessel zeros at P = 2, s = 2; JZC_M4 Prop N.2): W's coefficients of n^-1..n^-4 vs the exact closed form
      (n/N)^2 (1 - 1/(4N^2))^{-1/2}, N = n + nu/2; and W's total Toda times t_j = -2Z(-j)/j + B_j must vanish (exactness).
  W2  special cases: Hurwitz (a -> famA with p a = ... no: a pure Hurwitz lattice) reduces to Theorem H's M(alpha + 2 delta, alpha)."""
import os, sys, json, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from w_common import predict, by_exponent, WC, Checks, W
from w_spectra import SPECTRA, TARGETS, bessel
print("w_predict.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), flush=True)
C_ = Checks(); out = {}
VARIANTS = {'beta=alpha': "S1 without the Szego shift (beta = alpha)", 'no pole': "no pole terms", 'no zeta': "Toda times without Z(-j)",
            'no density tilt': "no Jacobian/density tilt", 'no mass tilt': "no multiplicity/mass tilt", 'no shift': "pole/tilt terms not at N"}
for key, mk in SPECTRA.items():
    t0 = time.time(); spec, lam, wts, tails = mk()
    print(f"\n=== {key}: {spec['name']} ===")
    print(f"  Z(0) = {mp.nstr(spec['Z0'], 15)} (regularised sum: {mp.nstr(spec['Z0_direct'], 15)});  "
          + "  ".join(f"Z(-{j}) = {mp.nstr(v, 15)}" for j, v in spec['Zneg'].items()))
    C_.check(f"{key} Z(0) closed form = regularised", abs(spec['Z0'] - spec['Z0_direct']) < 1e-12)
    for q, R, Rn in spec.get('pole_check', []):
        print(f"  pole q = {mp.nstr(q, 10)}: R = {mp.nstr(R, 15)} (h Z(-(q+h)) = {mp.nstr(Rn, 12)})")
        C_.check(f"{key} residue q={float(q):.4f}", abs(R - Rn) < 1e-9*max(1, abs(R)))
    if 'mcmahon_check' in spec:
        print(f"  McMahon (5 terms) vs besseljzero, k = 150..300: max rel. error {mp.nstr(spec['mcmahon_check'], 3)}")
        C_.check(f"{key} McMahon", spec['mcmahon_check'] < 1e-20)
    print("  poles (q, R, L = p R W(q) pi cot(pi q)) at n^-(1+pq):",
          "; ".join(f"q={float(q):.4g} R={float(R):+.6g}" for q, R in spec['poles']))
    terms, info = predict(spec)
    pe = by_exponent(terms)
    print(f"  alpha = {mp.nstr(info['alpha'], 10)}, beta = alpha - 2Z(0) - 1 = {mp.nstr(info['beta'], 10)}, N = n + {mp.nstr(info['N_shift'], 10)};"
          f" Toda mu_j = 2Z(-j)/j - B_j: {{{', '.join(f'{j}: {mp.nstr(v, 10)}' for j, v in info['X'].items())}}};"
          f" branched tilts {{{', '.join(f'{r:.4g}: {mp.nstr(v, 8)}' for r, v in info['Bbr'].items())}}}; resonant j {info['resonant']}")
    rec = {'p': spec['p'], 'targets': TARGETS[key], 'pred': {str(e): str(v) for e, v in pe.items()}, 'logexps': info['logexps'], 'alt': {}}
    for e in TARGETS[key]:
        e = round(float(e), 6); comp = [(l, v) for ee, v, l in terms if abs(ee - e) < 1e-6]
        print(f"  n^-{e}: W = {mp.nstr(pe.get(e, 0), 12):>18}   = " + " + ".join(f"[{l}] {mp.nstr(v, 8)}" for l, v in comp))
    for var, desc in VARIANTS.items():
        tv, _ = predict(spec, variant={var}); pv = by_exponent(tv)
        diff = {e: pv.get(round(float(e), 6), 0) - pe.get(round(float(e), 6), 0) for e in TARGETS[key]}
        if any(abs(d) > 1e-12 for d in diff.values()):
            rec['alt'][var] = {str(round(float(e), 6)): str(pv.get(round(float(e), 6), 0)) for e in TARGETS[key]}
            print(f"  alternative '{desc}': changes " + ", ".join(f"n^-{e}: {mp.nstr(d, 6)}" for e, d in diff.items() if abs(d) > 1e-12))
    out[key] = rec; print(f"  ({time.time() - t0:.0f} s)", flush=True)

# ------------------------------------------------ W1: the Lommel anchor (P = 2, s = 2) ------------------------------------------
print("\n=== W1: Lommel anchor, Bessel zeros at P = 2, s = 2 (exact closed form, JZC_M4 Prop N.2) ===")
for nu in (0, 1):
    spec, *_ = bessel(nu, 2, 2.0)
    terms, info = predict(spec, emax=5.0); pe = by_exponent(terms)
    n = mp.mpf(1); x = mp.mpf(1)                           # exact series of (n/N)^2 (1 - 1/(4N^2))^{-1/2}, N = n + nu/2, in 1/n
    ex = mp.taylor(lambda e: (1/(1 + nu*e/2))**2*(1 - e**2/(4*(1 + nu*e/2)**2))**(-mp.mpf(1)/2), 0, 5)
    print(f"  nu = {nu}: total Toda parameters mu_j = 2Z(-j)/j - B_j = {{{', '.join(f'{j}: {mp.nstr(v, 6)}' for j, v in info['X'].items())}}}")
    for j, v in info['X'].items(): C_.check(f"W1 nu={nu} t_{j} = 0", abs(v) < 1e-10)
    for k in range(1, 5):
        w = pe.get(float(k), mp.mpf(0)); print(f"    n^-{k}: W {mp.nstr(w, 15):>20}  exact {mp.nstr(ex[k], 15):>20}  diff {mp.nstr(w - ex[k], 3)}")
        C_.check(f"W1 nu={nu} n^-{k}", abs(w - ex[k]) < 1e-10)

json.dump(out, open(WC / 'predictions.json', 'w'), indent=1)
print("\npredictions written to tmp/w_cache/predictions.json at", time.strftime("%Y-%m-%d %H:%M:%S %Z"))
C_.finish()
