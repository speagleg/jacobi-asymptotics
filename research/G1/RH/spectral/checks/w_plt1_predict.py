"""JZC_W_plt1 §5, step 1 (Rule X): write the predictions for the kappa-family at p < 1 BEFORE any of its measures exists.

Family: lam_k = (k + delta)^p + kappa, k >= 1, masses lam^{-s/p}; here delta = -0.3 (a = 0.7, zeta(0, a) = -0.2 != 0, so the gauge
share of the Toda times is visible), s = 2, p in {0.6, 0.75}, kappa in {0, +0.5, -0.5} (kappa > -a^p).
y_n := n^p b_n / c(p) - 1 (so_fit.sequences).  Combinations: O := (y(kappa) - y(-kappa))/2 (odd part), E := (y(kappa) + y(-kappa))/2 - y(0)
(even part, kappa^2 and higher).

Prediction "EQ" (JZC_W_plt1.md §4, Conjecture W_<1; nothing fitted):
  (i)   the pure-epsilon layer (no factor n^-1): the edge of the n-dependent constrained equilibrium g_kappa,
        A(eps) = a_eps/(4c), a_eps = 4c (1 - a_eps eps)^{1 - p/2}, eps = kappa/n^p (JZC_W_plt1 Prop 1), to every order in eps:
        the coefficient of n^{-pm} is [x^m]A * (4c kappa)^m  (x = 4c eps);
  (ii)  everything else at first order in the poles, from Conjecture W as implemented in w_common.predict (Szego shift beta' = alpha + 2 delta,
        kappa-free; Toda times t_j = -2 Z_kappa(-j)/j + B_j; natural-index shift of the pole terms), i.e. W with its pole terms at n^{-pm}
        (m >= 2) replaced by (i).  For m = 1 (i) and W agree identically (checked below).
Asserted targets (chosen here, before the measures): per measure with kappa != 0: n^-p, n^-1, n^-2p, n^-(1+p), n^-3p; kappa = 0: n^-1, n^-(1+p);
O: n^-p, n^-1 (= 0), n^-(1+p), n^-3p; E: n^-1 (= 0), n^-2p.  The n^-(1+pm) coefficients for m >= 2 (second-order natural index, products of
the eps-layer with Toda times) are NOT predicted; they are nuisance columns.
Alternatives (must be excluded by > 10 tolerances where they differ):
  'W1' : Conjecture W at first order (pole terms linear in the residues) at n^-2p, n^-3p;
  'naive': the constrained equilibrium on (0, inf) only for kappa < 0 (Theorem Q verbatim, no mass on (-inf, -n^p/|kappa|)): n^-1 shifted by
           -p |kappa|^{1/p} (its edge is a_eps (1 - p|eps|^{1/p} + ...)); kappa > 0: identical;
  'no shift': pole terms not at the natural index (the -2p dN L_1 part of n^-(1+p) dropped);
  'no share': Toda times without the gauge share (Z_kappa(-j) - kappa^j zeta(0, a) in place of Z_kappa(-j));
  'no density': Toda times without the density factor B_j (log (1 - kappa x)^{1/p - 1}).
Output: this .out and tmp/w_plt1_cache/predictions.json (read by w_plt1_test.py, which asserts that every measure cache is newer).
NUMERICAL tooling (Rule N); no statement is proved here."""
import os, sys, json, time, copy; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from w_common import predict, by_exponent, Checks, W, ROOT
from w_spectra import famK
from so_coeffs import c_p_mp
mp.mp.dps = 40
CACHE = ROOT / 'tmp' / 'w_plt1_cache'; CACHE.mkdir(parents=True, exist_ok=True)
print("w_plt1_predict.py run at", time.strftime("%Y-%m-%d %H:%M:%S %Z"), flush=True)
C_ = Checks()
DELTA, S, KAP = -0.3, 2.0, 0.5
PS = [0.6, 0.75]
EMAX = 3.2


def Acoef(p, M=5):
    """[x^m] A, A = (1 - x A)^{1 - p/2}: exact recursion via Lagrange-free power-series iteration (mp)"""
    p = mp.mpf(p); g = 1 - p/2
    A = [mp.mpf(1)] + [mp.mpf(0)]*M
    for _ in range(M + 2):
        # B := 1 - x A  (series), A_new := B^g
        B = [mp.mpf(1)] + [-A[m - 1] for m in range(1, M + 1)]
        L = [mp.mpf(0)]*(M + 1); pw = [mp.mpf(0)] + B[1:]; k = 1; term = pw[:]
        while k <= M:
            for i in range(M + 1): L[i] += (-1)**(k + 1)*term[i]/k
            term = [sum(term[j]*pw[i - j] for j in range(i + 1)) for i in range(M + 1)]; k += 1
        E = [mp.mpf(1)] + [mp.mpf(0)]*M; t = E[:]
        for k in range(1, M + 1):
            t = [sum(t[j]*L[i - j] for j in range(i + 1))*g/k for i in range(M + 1)]
            E = [E[i] + t[i] for i in range(M + 1)]
        A = E
    return A


def spec_variant(spec, kap, which):
    sp = copy.deepcopy(spec); a = 1 + mp.mpf(DELTA)
    if which == 'no share':
        sp['Zneg'] = {j: v - mp.mpf(kap)**j*mp.zeta(0, a) for j, v in sp['Zneg'].items()}
    # the model engine does not depend on Z(-j): keep the tag (same cached model responses)
    return sp


out = {}
for p in PS:
    P = mp.mpf(p); c = mp.mpf(c_p_mp(P)); Ac = Acoef(P)
    # internal check: the closed form edge equals the root of the continuum soft-edge condition (quadrature), and its first-order
    # coefficient equals W's pole term at m = 1 (Prop M1.2 / the kappa law)
    for eps in (mp.mpf('0.05'), mp.mpf('-0.05')):
        acf = mp.findroot(lambda a: a - 4*c*(1 - a*eps)**(1 - P/2), 4*c)
        ser = sum(Ac[m]*(4*c*eps)**m for m in range(len(Ac)))*4*c
        C_.check(f"p={p} eps={eps}: series of A vs root ({mp.nstr(abs(ser - acf)/acf, 3)})", abs(ser - acf)/acf < 5*abs(4*c*eps)**6)
    per = {}
    for kap in (0.0, KAP, -KAP):
        spec, lam, wts, tails = famK(p, DELTA, kap, S)
        terms, info = predict(spec, emax=EMAX)
        pe = by_exponent(terms)
        X = 4*c*mp.mpf(kap)
        # replace the pure-eps exponents m >= 2 by the equilibrium coefficients; check m = 1
        eq = dict(pe); w1 = dict(pe)
        for m in range(1, 6):
            e = round(float(m*P), 6)
            if e > EMAX + 1e-9: break
            pole = [v for ee, v, l in terms if abs(ee - e) < 1e-6 and l.startswith('pole q')]
            if kap == 0: continue
            Lm = pole[0] if pole else mp.mpf(0)
            if m == 1:
                C_.check(f"p={p} kappa={kap}: [x^1]A (4c kappa) = W's kappa-law pole term ({mp.nstr(Ac[1]*X - Lm, 3)})",
                         abs(Ac[1]*X - Lm) < 1e-25)
            eq[e] = pe.get(e, 0) - Lm + Ac[m]*X**m
        alt = {}
        alt['W1'] = {str(e): str(w1[e]) for e in w1 if abs(w1[e] - eq[e]) > 1e-30}
        if kap < 0:
            e1 = 1.0; alt['naive'] = {str(e1): str(eq[e1] - P*mp.mpf(-kap)**(1/P))}
        for var, kw in (('no shift', dict(variant={'no shift'})), ('no density', dict(variant={'no density tilt'}))):
            t2, _ = predict(spec, emax=EMAX, **kw); p2 = by_exponent(t2)
            e = round(float(1 + P), 6); alt[var] = {str(e): str(p2.get(e, 0))}
        t3, _ = predict(spec_variant(spec, kap, 'no share'), emax=EMAX); p3 = by_exponent(t3)
        e = round(float(1 + P), 6); alt['no share'] = {str(e): str(p3.get(e, 0))}
        tg = [round(float(x), 6) for x in ((P, 1, 2*P, 1 + P, 3*P) if kap != 0 else (1, 1 + P))]
        per[kap] = dict(eq=eq, alt=alt, targets=tg, info=info, terms=terms)
        key = f"p{p}_k{kap:+.1f}"
        out[key] = {'p': p, 'kappa': kap, 'delta': DELTA, 's': S, 'targets': tg, 'pred': {str(e): str(v) for e, v in eq.items()},
                    'alt': alt, 'logexps': info['logexps']}
        print(f"\n=== {key}: lam_k = (k {DELTA:+})^{p} {kap:+}, s = {S}: alpha = {mp.nstr(info['alpha'], 10)}, beta' = {mp.nstr(info['beta'], 10)}, "
              f"dN = {mp.nstr(info['N_shift'], 10)}; Toda mu_j = 2Z(-j)/j - B_j: "
              + ", ".join(f"{j}: {mp.nstr(v, 10)}" for j, v in info['X'].items()))
        for e in tg:
            comp = [(l, v) for ee, v, l in terms if abs(ee - e) < 1e-6]
            s_ = f"  n^-{e}: EQ = {mp.nstr(eq.get(e, 0), 12):>18}  [W pieces: " + "; ".join(f"{l} {mp.nstr(v, 8)}" for l, v in comp) + "]"
            al_ = [f"{nm} {mp.nstr(mp.mpf(d[str(e)]), 10)}" for nm, d in alt.items() if str(e) in d]
            print(s_ + ("  | alternatives: " + ", ".join(al_) if al_ else ""))
    # combinations
    for comb, (wts_, tg) in {'O': ({KAP: mp.mpf(1)/2, -KAP: -mp.mpf(1)/2}, (P, 1, 1 + P, 3*P)),
                             'E': ({KAP: mp.mpf(1)/2, -KAP: mp.mpf(1)/2, 0.0: -mp.mpf(1)}, (1, 2*P))}.items():
        exps = sorted(set().union(*[set(per[k]['eq']) for k in wts_]))
        eq = {e: sum(w*per[k]['eq'].get(e, 0) for k, w in wts_.items()) for e in exps}
        eq = {e: v for e, v in eq.items() if abs(v) > 1e-28}
        alt = {}
        for nm in ('W1', 'naive', 'no shift', 'no share', 'no density'):
            d = {}
            for e in [round(float(x), 6) for x in tg]:
                vals = []
                for k, w in wts_.items():
                    a_ = per[k]['alt'].get(nm, {})
                    vals.append(w*(mp.mpf(a_[str(e)]) if str(e) in a_ else per[k]['eq'].get(e, 0)))
                v = sum(vals)
                if abs(v - eq.get(e, 0)) > 1e-30: d[str(e)] = str(v)
            if d: alt[nm] = d
        key = f"p{p}_{comb}"
        tgr = [round(float(x), 6) for x in tg]
        out[key] = {'p': p, 'comb': {str(k): str(w) for k, w in wts_.items()}, 'targets': tgr, 'pred': {str(e): str(v) for e, v in eq.items()},
                    'alt': alt, 'logexps': []}
        print(f"\n=== {key} ({'odd' if comb == 'O' else 'even'} part, kappa = {KAP}) ===")
        for e in tgr:
            al_ = [f"{nm} {mp.nstr(mp.mpf(d[str(e)]), 10)}" for nm, d in alt.items() if str(e) in d]
            print(f"  n^-{e}: EQ = {mp.nstr(eq.get(e, 0), 12):>18}" + ("  | alternatives: " + ", ".join(al_) if al_ else ""))
    print(f"\n  p = {p}: c = {mp.nstr(c, 15)}; [x^m]A = " + ", ".join(mp.nstr(v, 10) for v in Ac))
json.dump(out, open(CACHE / 'predictions.json', 'w'), indent=1)
print(f"\nwrote {CACHE / 'predictions.json'} at", time.strftime("%Y-%m-%d %H:%M:%S %Z"))
C_.finish()
