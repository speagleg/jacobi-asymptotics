"""JZC_W2 common helpers (NUMERICAL tooling; nothing here is a proof).

The kappa-family sigma^{delta,kappa} = sum_k lam_k^{-s/p} delta_{1/lam_k}, lam_k = (k + delta)^p + kappa (JZC_W_kappa (S)).
Times (JZC_W_kappa Prop K.12/K.12', P W-out.5): in the n^p frame the band factor of BT_coh is exp(-sum_a mu_a z^{j_a}) with
  - Toda times (integer j): mu_j = X_j n^{-jp}, X_j = 2 Z_kappa(-j)/j - B_j   (w_common.predict's X, P W-out.5(i));
  - pole times (j = q_m = m - 1/p): mu_{q_m} = -tau_m n^{-p q_m}, tau_m = 2 pi cot(pi q_m) a_m, a_m = -binom(1/p, m)(-kappa)^m.
Normalised engine time (c = 1 frame, tilt e * z'^j / C(2j, j), z' = z/c): e_a(n) = X_a c^{j_a} C(2 j_a, j_a) n^{-p j_a}.
Prediction of n^p b_n / c (formal layers of BT_coh, all orders in the times; JZC_W2 Prop 2.1):
  sum_m d_m n^{-m} + sum_{monomials e^beta} e^beta(n) sum_m R_beta[m] n^{-m},
with d_m and R_beta[m] exact rational outputs of w2_engine.py at the case's rational (p, alpha, beta', j's).
Layers are labelled by their order |beta| (1: first order, 2: second order, 3: third order) and by which times they contain."""
import os, sys, json, hashlib, subprocess, time
from fractions import Fraction
from itertools import combinations_with_replacement
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mpmath as mp
import sympy as sp
mp.mp.dps = 40
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
W2C = os.path.join(ROOT, 'tmp', 'w2'); os.makedirs(W2C, exist_ok=True)
PY = sys.executable
ENGINE = os.path.join(HERE, 'w2_engine.py')


def sha(fn): return hashlib.sha256(open(fn, 'rb').read()).hexdigest()


def provenance(*fns):
    for fn in fns: print(f"sha256 {os.path.basename(fn)}: {sha(fn)}", flush=True)


# ------------------------------------------------------------------ exact engine (cached) --------------------------------------
def engine(p, alpha, beta, j1, j2, E1, E2, kord):
    """exact outputs of w2_engine.py at rational data; returns {'d': [Fraction], 'e': {(a,b): [Fraction]}, 'nat': ...}"""
    args = dict(PVAL=str(p), AVAL=str(alpha), BVAL=str(beta), J1VAL=str(j1), J2VAL=str(j2), E1=str(E1), E2=str(E2),
                KORD=str(kord), SHI=str(4*kord + 6), NT=str(2*kord + 8), DECOUPLE='1')
    key = hashlib.sha256((repr(sorted(args.items())) + sha(ENGINE)).encode()).hexdigest()[:16]
    fn = os.path.join(W2C, f"eng_{key}.json")
    if not os.path.exists(fn):
        env = dict(os.environ, **args, W2JSON=fn)
        t0 = time.time()
        subprocess.run([PY, '-B', ENGINE], env=env, check=True, stdout=subprocess.DEVNULL)
        print(f"   [engine p={p} j1={j1} j2={j2} E=({E1},{E2}) KORD={kord}: {time.time() - t0:.0f}s]", flush=True)
    D = json.load(open(fn))
    fr = lambda s: Fraction(str(sp.Rational(sp.sympify(s))))
    return {'d': [fr(x) for x in D['d']],
            'e': {tuple(map(int, k.split(','))): [fr(x) for x in v] for k, v in D['e'].items()},
            'nat': {tuple(map(int, k.split(','))): [fr(x) for x in v] for k, v in D['nat'].items()}}


def fmp(x): return mp.mpf(x.numerator)/x.denominator


# ------------------------------------------------------------------ the kappa family -------------------------------------------
H = mp.mpf(10)**-12
def sym(f, w): return (f(w + H) + f(w - H))/2


def kappa_case(p, d, kap, s, jmax=3, mmax=4, imax=900):
    """data of sigma^{d,kap}: Z(0), Z(-j) (j <= jmax), poles q_m (m <= mmax) with a_m, tau_m, R_m; exact rationals kept"""
    P, D, Kp = Fraction(p), Fraction(d), Fraction(kap)
    p_, d_, k_ = mp.mpf(P.numerator)/P.denominator, mp.mpf(D.numerator)/D.denominator, mp.mpf(Kp.numerator)/Kp.denominator
    a = 1 + d_
    assert abs(k_) < a**p_ and k_ > -a**p_
    def Zm(w): return sum(mp.binomial(w, i)*k_**i*mp.zeta(-p_*(w - i), a) for i in range(imax))
    S_ = Fraction(s); alpha = (S_ - 1 - P)/P; betap = alpha + 2*D
    poles = []
    for m in range(1, mmax + 1):
        q = m - 1/P; qm = m - 1/p_
        am = -mp.binomial(1/p_, m)*(-k_)**m
        tau = 2*mp.pi*mp.cot(mp.pi*qm)*am
        poles.append(dict(m=m, q=q, a=am, tau=tau, R=-qm*am))
    return dict(p=P, d=D, kap=Kp, s=S_, alpha=alpha, betap=betap, p_mp=p_, kap_mp=k_, Zm=Zm, Z0=sym(Zm, mp.mpf(0)),
                Zneg={j: sym(Zm, mp.mpf(j)) for j in range(1, jmax + 1)}, poles=poles,
                tag=f"w2_p{float(P)}_d{float(D)}_k{float(Kp)}_s{float(S_)}")


def toda_X(case, js):
    """X_j = 2 Z(-j)/j - B_j (w_common.predict's convention, B from log D(x), D(x) = 1 - p sum_q R_q x^{q + 1/p})."""
    p_ = case['p_mp']
    # log D with D = 1 - p sum_m R_m x^m (q_m + 1/p = m): integer-exponent band tilt B_j
    Dc = {pl['m']: -p_*pl['R'] for pl in case['poles']}
    B = defaultdict(lambda: mp.mpf(0)); pw = dict(Dc); k = 1
    while pw and k < 40:
        for r, c in pw.items():
            if r <= max(js): B[r] += (-1)**(k + 1)*c/k
        new = defaultdict(lambda: mp.mpf(0))
        for r1, c1 in pw.items():
            for r2, c2 in Dc.items():
                if r1 + r2 <= max(js): new[r1 + r2] += c1*c2
        pw = dict(new); k += 1
    return {j: 2*case['Zneg'][j]/j - B[j] for j in js}


def times(case, emax, cp):
    """list of times (label, j (Fraction), X (mp), s = p j) with first-order exponent 1 + p j <= emax"""
    P = case['p']; out = []
    for pl in case['poles']:
        if 1 + float(P*pl['q']) <= emax + 1e-9: out.append((f"q{pl['m']}", pl['q'], -pl['tau']))
    js = [j for j in range(1, 10) if 1 + float(P*j) <= emax + 1e-9]
    X = toda_X(case, js) if js else {}
    for j in js: out.append((f"t{j}", Fraction(j), X[j]))
    return out


def C2(j):
    j = mp.mpf(j.numerator)/j.denominator; return mp.gamma(2*j + 1)/mp.gamma(j + 1)**2


def predict2(case, emax, cp, kord, maxorder=3, verbose=True):
    """terms [(exponent, coefficient, label, order)] of the formal BT_coh prediction with all exponents <= emax.
    Order-k monomials start at n^{-k} for k >= 2 (n^{-1} for k = 1); this is used only to decide which monomials can reach emax,
    and it is asserted on the engine output (e_m = 0 for m < k)."""
    P = case['p']; al, bp = case['alpha'], case['betap']
    T = times(case, emax, cp)
    sv = {lab: float(P*j) for lab, j, X in T}
    ev = {lab: X*cp**(mp.mpf(j.numerator)/j.denominator)*C2(j) for lab, j, X in T}
    jv = {lab: j for lab, j, X in T}
    terms = []
    # monomials
    monos = []
    for order in range(1, maxorder + 1):
        for combo in combinations_with_replacement([t[0] for t in T], order):
            e0 = sum(sv[c] for c in combo) + (1 if order == 1 else order)
            if e0 <= emax + 1e-9: monos.append(combo)
    runs = {}
    def get(combo):
        labs = sorted(set(combo), key=lambda c: [t[0] for t in T].index(c))
        assert len(labs) <= 2, ("three distinct times needed", combo)
        a = combo.count(labs[0]); b = combo.count(labs[1]) if len(labs) == 2 else 0
        j1 = jv[labs[0]]; j2 = jv[labs[1]] if len(labs) == 2 else Fraction(1)
        E1 = max(a, 1); E2 = b
        # one run per (j1, j2) with the maximal orders needed
        key = (labs[0], labs[1] if len(labs) == 2 else None)
        return key, (j1, j2), (a, b)
    need = defaultdict(lambda: [0, 0, None])
    for combo in monos:
        key, jj, ab = get(combo)
        nd = need[key]; nd[0] = max(nd[0], ab[0]); nd[1] = max(nd[1], ab[1]); nd[2] = jj
    res = {}
    for key, (E1, E2, jj) in need.items():
        res[key] = engine(P, al, bp, jj[0], jj[1], max(E1, 1), E2, kord)
    anyrun = next(iter(res.values()))
    for m in range(1, kord + 1):
        if m <= emax + 1e-9: terms.append((float(m), fmp(anyrun['d'][m]), 'model', 0))
    for combo in monos:
        key, jj, ab = get(combo)
        R = res[key]['e'][ab]
        order = len(combo)
        for m in range(order if order >= 2 else 1):
            assert R[m] == 0, ("layer does not start where expected", combo, m)
        coef0 = mp.mpf(1)
        for c in combo: coef0 *= ev[c]
        s0 = sum(sv[c] for c in combo)
        lab = '*'.join(combo)
        for m in range(1, kord + 1):
            e = s0 + m
            if e <= emax + 1e-9 and R[m] != 0: terms.append((round(e, 6), coef0*fmp(R[m]), lab, order))
    # all monomials whose first exponent <= emax must be complete through emax: kord large enough
    for combo in monos:
        s0 = sum(sv[c] for c in combo)
        assert s0 + kord >= emax - 1e-9, ("KORD too small for", combo)
    assert kord >= emax - 1e-9
    return terms, dict(times=T, ev=ev, sv=sv, monos=monos)


def by_exp(terms, orders=None, exclude=()):
    out = defaultdict(lambda: mp.mpf(0))
    for e, v, l, o in terms:
        if orders is not None and o not in orders: continue
        if any(x in l.split('*') for x in exclude) and o >= 2: continue
        out[e] += v
    return dict(sorted(out.items()))
