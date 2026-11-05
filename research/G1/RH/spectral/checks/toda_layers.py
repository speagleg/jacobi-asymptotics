"""JZC_TODA (4b): EXACT check of Theorem T (ii) — the formal Toda hierarchy for the layers of the model — on the exact engine's
layers, with controls that must fail.  Usage: toda_layers.py [L1 L2 L3 ...] (default: all configurations below).

Engine: toda_engine.py (= w2_engine.py + the second moment R_2 and the alpha-extraction of Lemma T.B), run by subprocess, exact
outputs cached in tmp/toda/eng_<cfg>.json.  c = 1.  For exponents (j_1, j_2) the engine's times are e_a = C(2j_a, j_a) mu_a, and it
returns, per monomial beta = (b_1, b_2) (b_a <= E_a), the coefficients of e^beta n^{-m} (m <= KORD) of
    B := n^p b_n / c     and     A := n^p alpha_n / (2c).
Theorem T (ii) in the engine's units (JZC_TODA §3, eq. (T-b), (T-a); scaled Jacobi matrix calJ := n^p J / c with entries
calb_i := n^p b_{n+i}/c, cala_i := n^p alpha_{n+i}/c = 2 A shifted):
    d_{e_a} B      = -(1/(2 C_a)) B [ (calJ^{j_a})_{0,0} - (calJ^{j_a})_{-1,-1} ],
    d_{e_a} (2A)   = -(1/C_a)   [ calb_1 (calJ^{j_a})_{1,0} - calb_0 (calJ^{j_a})_{0,-1} ],
where the shift n -> n + i acts on the e^beta n^{-m} coefficient as
    (S_i F)_beta(x) = (1 + i x)^{-p(1 + |beta|_w)} F_beta(x/(1 + i x)),   x = 1/n,  |beta|_w = sum_a b_a j_a
(the unscaled times u_a = -mu_a n^{j_a p} do not shift; this is d_mu = -n^{jp} d_u, JZC_TODA §3).  Every identity is checked
coefficientwise (all monomials beta with beta + e_a computed, all orders m <= KORD), identically in the field symbols
(p, alpha[, beta]).  Controls (must fail): sign of the right side; (calJ^j)_{1,1} in place of (calJ^j)_{-1,-1}; F_j(n) with calb_0 in
place of calb_1; no 1/C_a; and the 'scaled-time' shift (1 + i x)^{-p} without the time weight (fails only at second order, as it must).
Also asserted (integer layers, exact): A's n^{-1} coefficient = -p(beta_Sz + 2)/2 (E_pgt1 Thm E.1 on the lattice line); the natural
form of A in M := n + beta_Sz/2 + 1 has no M^{-1}, M^{-3} terms and M^{-2} = -(p+1)/24 + (p+1)(p+2) nu^2/8, beta_Sz-free to M^{-4}."""
import os, sys, json, hashlib, subprocess, time
import sympy as sp
from sympy import QQ
from sympy.polys.fields import field

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
CACHE = os.path.join(ROOT, 'tmp', 'toda'); os.makedirs(CACHE, exist_ok=True)
ENGINE = os.path.join(HERE, 'toda_engine.py')
PY = sys.executable
sha = lambda fn: hashlib.sha256(open(fn, 'rb').read()).hexdigest()
for fn in (os.path.abspath(__file__), ENGINE, os.path.join(HERE, 'w2_engine.py')):
    print(f"sha256 {os.path.basename(fn)}: {sha(fn)}", flush=True)

CFG = {   # name: (env, exponents, decoupled)
    'L1': (dict(KORD='4', SHI='16', E1='2', E2='0', J1VAL='1'), (1, 1), False),
    'L2': (dict(KORD='4', SHI='16', E1='1', E2='1', J1VAL='2', J2VAL='3'), (2, 3), False),
    'L3': (dict(KORD='4', SHI='16', E1='1', E2='1', J1VAL='1', J2VAL='2', DECOUPLE='1'), (1, 2), True),
    'Q1': (dict(KORD='4', E1='2', E2='1', J1VAL='1', J2VAL='2', PVAL='3/2', AVAL='3/10'), (1, 2), False),    # quick, rational point
    'Q2': (dict(KORD='4', E1='1', E2='1', J1VAL='1', J2VAL='3', PVAL='3/5', AVAL='-2/7', BVAL='1/3', DECOUPLE='1'), (1, 3), True),
    'Q3': (dict(KORD='4', E1='1', E2='2', J1VAL='3', J2VAL='2', PVAL='7/3', AVAL='-1/2'), (3, 2), False),
    'Q4': (dict(KORD='4', E1='3', E2='0', J1VAL='1', PVAL='2/5', AVAL='5/8'), (1, 1), False),
}

Kf, p, al, be = field("p,alpha,beta", QQ)
def parse(s):
    return Kf.from_expr(sp.sympify(s, locals={'p': sp.Symbol('p'), 'alpha': sp.Symbol('alpha'), 'beta': sp.Symbol('beta')}))

NI = [0]; NC = [0]; FAILS = []
def check(label, ok, control=False):
    if control:
        NC[0] += 1
        if ok: FAILS.append("CONTROL HELD: " + label)
    else:
        NI[0] += 1
        if not ok: FAILS.append(label)
    print(f"  {'control' if control else 'identity'}: {label}: {'holds' if ok else 'fails'}", flush=True)


def run_cfg(name):
    env_r, js, dec = CFG[name]
    fn = os.path.join(CACHE, f'eng_{name}.json')
    if not os.path.exists(fn):
        t0 = time.time()
        subprocess.run([PY, '-B', ENGINE], env=dict(os.environ, **env_r, W2JSON=fn), check=True, stdout=subprocess.DEVNULL)
        print(f"{name}: engine {time.time() - t0:.0f} s", flush=True)
    D = json.load(open(fn))
    KORD = int(env_r['KORD']); E = (int(env_r['E1']), int(env_r['E2']))
    MON = [(a, b) for a in range(E[0] + 1) for b in range(E[1] + 1)]
    key = lambda mo: f"{mo[0]},{mo[1]}"
    B = {mo: [parse(s) for s in D['e'][key(mo)]] for mo in MON}
    A = {mo: [parse(s) for s in D['ea'][key(mo)]] for mo in MON}
    assert [str(x) for x in B[(0, 0)]] == [str(parse(s)) for s in D['d']]
    P_ = Kf(sp.Rational(env_r['PVAL'])) if 'PVAL' in env_r else p
    NU = Kf(sp.Rational(env_r['AVAL'])) if 'AVAL' in env_r else al
    SZ = (Kf(sp.Rational(env_r['BVAL'])) if 'BVAL' in env_r else be) if dec else NU   # Szego exponent; Bessel order nu = alpha
    print(f"== {name}: exponents {js}, E = {E}, KORD = {KORD}, {'decoupled M(beta, nu = alpha)' if dec else 'lattice line M(alpha, alpha)'}", flush=True)
    zero = Kf(0); one = Kf(1)
    W = lambda mo: mo[0]*js[0] + mo[1]*js[1]

    def binom_neg(e, l):            # binomial(-e, l)
        r = one
        for t in range(l): r = r*(-e - t)/(t + 1)
        return r
    def shift(F, i, timeweight=True):
        out = {}
        for mo, c in F.items():
            w = P_*(1 + (W(mo) if timeweight else 0))
            out[mo] = [sum((c[m]*binom_neg(m + w, k - m)*Kf(i**(k - m)) for m in range(k + 1)), zero) for k in range(KORD + 1)]
        return out
    def mul(F, G):
        out = {mo: [zero]*(KORD + 1) for mo in MON}
        for m1, c1 in F.items():
            for m2, c2 in G.items():
                mo = (m1[0] + m2[0], m1[1] + m2[1])
                if mo not in out: continue
                for k1, x1 in enumerate(c1):
                    if x1 == zero: continue
                    for k2 in range(KORD + 1 - k1):
                        if c2[k2] != zero: out[mo][k1 + k2] += x1*c2[k2]
        return out
    add = lambda F, G: {mo: [x + y for x, y in zip(F[mo], G[mo])] for mo in MON}
    sc = lambda F, f: {mo: [x*f for x in F[mo]] for mo in MON}
    def Jpow_entries(j, timeweight=True, want=((0, 0), (-1, -1), (1, 0), (0, -1), (1, 1))):
        R = j + 2
        a_ = {i: sc(shift(A, i, timeweight), Kf(2)) for i in range(-R, R + 1)}
        b_ = {i: shift(B, i, timeweight) for i in range(-R, R + 1)}
        def entry(r, s):
            if r == s: return a_[r]
            if abs(r - s) == 1: return b_[max(r, s)]
            return None
        out = {}
        for (r0, s0) in want:          # (calJ^j)_{r0,s0} = sum over paths r0 -> s0 of length j
            paths = {r0: {mo: [one if (mo == (0, 0) and k == 0) else zero for k in range(KORD + 1)] for mo in MON}}
            for _ in range(j):
                new = {}
                for r, val in paths.items():
                    for s in (r - 1, r, r + 1):
                        t = mul(val, entry(r, s))
                        new[s] = add(new[s], t) if s in new else t
                paths = new
            out[(r0, s0)] = paths.get(s0, {mo: [zero]*(KORD + 1) for mo in MON})
        return out, b_

    def compare(lhs, rhs, a_idx):
        ok = True
        for mo in MON:
            up = (mo[0] + (a_idx == 0), mo[1] + (a_idx == 1))
            if up not in MON: continue
            ok &= all(x == y for x, y in zip(lhs[mo], rhs[mo]))
        return ok
    def lhs_of(F, a_idx, f=one):
        out = {}
        for mo in MON:
            up = (mo[0] + (a_idx == 0), mo[1] + (a_idx == 1))
            out[mo] = [x*(up[a_idx])*f for x in F[up]] if up in MON else [zero]*(KORD + 1)
        return out

    for a_idx in range(2):
        if E[a_idx] == 0: continue
        j = js[a_idx]; Ca = Kf(sp.binomial(2*j, j))
        orders = sorted({mo[0] + mo[1] + 1 for mo in MON if (mo[0] + (a_idx == 0), mo[1] + (a_idx == 1)) in MON})
        lab = f"{name} flow e_{a_idx + 1} (j = {j}), orders {orders}"
        Jp, b_ = Jpow_entries(j)
        # (T-b)
        rb = sc(mul(B, add(Jp[(0, 0)], sc(Jp[(-1, -1)], Kf(-1)))), -one/(2*Ca))
        Lb = lhs_of(B, a_idx)
        check(lab + ": (T-b) d_e B = -(1/2C) B[(J^j)_00 - (J^j)_-1-1]", compare(Lb, rb, a_idx))
        # (T-a)
        ra = sc(add(mul(b_[1], Jp[(1, 0)]), sc(mul(b_[0], Jp[(0, -1)]), Kf(-1))), -one/Ca)
        La = lhs_of(A, a_idx, Kf(2))
        check(lab + ": (T-a) d_e (2A) = -(1/C)[b_1 (J^j)_10 - b_0 (J^j)_0,-1]", compare(La, ra, a_idx))
        # controls
        check(lab + ": control (T-b) opposite sign", compare(Lb, sc(rb, Kf(-1)), a_idx), control=True)
        check(lab + ": control (T-a) opposite sign", compare(La, sc(ra, Kf(-1)), a_idx), control=True)
        check(lab + ": control (T-b) with (J^j)_11", compare(Lb, sc(mul(B, add(Jp[(0, 0)], sc(Jp[(1, 1)], Kf(-1)))), -one/(2*Ca)), a_idx), control=True)
        check(lab + ": control (T-a) with F_j(n) = b_0 (J^j)_10", compare(La, sc(add(mul(b_[0], Jp[(1, 0)]), sc(mul(b_[0], Jp[(0, -1)]), Kf(-1))), -one/Ca), a_idx), control=True)
        check(lab + ": control (T-b) without 1/C_a", compare(Lb, sc(rb, Ca), a_idx), control=True)
        if max(orders) >= 2:
            Jq, bq = Jpow_entries(j, timeweight=False)
            rbq = sc(mul(B, add(Jq[(0, 0)], sc(Jq[(-1, -1)], Kf(-1)))), -one/(2*Ca))
            raq = sc(add(mul(bq[1], Jq[(1, 0)]), sc(mul(bq[0], Jq[(0, -1)]), Kf(-1))), -one/Ca)
            check(lab + ": control (T-b) scaled-time shift (1+ix)^{-p} (no n^{jp})", compare(Lb, rbq, a_idx), control=True)
            check(lab + ": control (T-a) scaled-time shift (1+ix)^{-p} (no n^{jp})", compare(La, raq, a_idx), control=True)
            # the first-order part of the scaled-time control coincides with the true identity (it uses only beta = 0 layers):
            fo = all(x == y for x, y in zip(Lb[(0, 0)], rbq[(0, 0)]))
            check(lab + ": scaled-time shift agrees at FIRST order (expected; the difference is second order)", fo)

    # integer layers of A
    A0 = A[(0, 0)]
    check(f"{name}: A n^-1 coefficient = -p(beta_Sz + 2)/2 (E_pgt1 Thm E.1 on the lattice line)", A0[1] == -P_*(SZ + 2)/2)
    dl = SZ/2 + 1                    # M = n + dl;  1/n = y/(1 - dl y), (M/n)^p = (1 - dl y)^{-p}, y = 1/M
    nat = [zero]*(KORD + 1)
    for m in range(KORD + 1):       # (1 - dl y)^{-p} * sum_m A_m y^m (1 - dl y)^{-m}
        for k in range(m, KORD + 1):
            pw = one
            for _ in range(k - m): pw = pw*(-dl)
            nat[k] += A0[m]*binom_neg(P_ + m, k - m)*pw
    print(f"  {name}: natural form of A in M = n + beta_Sz/2 + 1: " + "; ".join(f"M^-{k}: {sp.factor(nat[k].as_expr())}" for k in range(KORD + 1)), flush=True)
    check(f"{name}: A natural form: M^-1 = 0", nat[1] == zero)
    check(f"{name}: A natural form: M^-3 = 0", nat[3] == zero)
    check(f"{name}: A natural form: M^-2 = -(p+1)/24 + (p+1)(p+2)nu^2/8", nat[2] == -(P_ + 1)/24 + (P_ + 1)*(P_ + 2)*NU**2/8)
    check(f"{name}: A natural form: beta_Sz-free to M^-{KORD}", all(sp.Symbol('beta') not in x.as_expr().free_symbols for x in nat))
    check(f"{name}: control: A centred at N = n + beta_Sz/2 + 1/2 has an N^-1 term", (lambda: (A0[1] + P_*(SZ/2 + Kf(1)/2)) == zero)(), control=True)


def cross_checks():
    """(X1) toda_engine's b-part equals w2_engine's (not modified) at the Q1 configuration, exactly; (X2) NUMERICAL: the exact alpha
    layers (mu = 0 and first order in mu_1) against the independent numerical engine m4_rh4.run(..., want_a=True) (40 digits;
    first order by central differences, step 1e-12), p = 3/2, alpha = 3/10.  Engine units: e_1 = C(2,1) mu_1 = 2 mu_1 (c = 1)."""
    env_r = CFG['Q1'][0]; fn = os.path.join(CACHE, 'eng_Q1_w2.json')
    if not os.path.exists(fn):
        subprocess.run([PY, '-B', os.path.join(HERE, 'w2_engine.py')], env=dict(os.environ, **env_r, W2JSON=fn), check=True,
                       stdout=subprocess.DEVNULL)
    Dw = json.load(open(fn)); Dt = json.load(open(os.path.join(CACHE, 'eng_Q1.json')))
    same = Dw['d'] == Dt['d'] and Dw['e'] == Dt['e'] and Dw['nat'] == Dt['nat']
    check("X1: toda_engine b-part (d, e, nat) == w2_engine's at Q1 (string-identical)", same)
    os.environ['KORD'] = env_r['KORD']; sys.path.insert(0, HERE)
    import mpmath as mp
    import m4_rh4 as M4
    mp.mp.dps = 40
    P, AL = mp.mpf(3)/2, mp.mpf(3)/10
    d0, _, a0 = M4.run(P, AL, want_a=True)
    h = mp.mpf(10)**-12
    _, _, ap = M4.run(P, AL, mu={1: h}, want_a=True); _, _, am = M4.run(P, AL, mu={1: -h}, want_a=True)
    a1 = [(x - y)/(2*h)/2 for x, y in zip(ap, am)]          # d/de_1 = (1/2) d/dmu_1
    ex0 = [mp.mpf(sp.Rational(s).p)/sp.Rational(s).q for s in Dt['ea']['0,0']]
    ex1 = [mp.mpf(sp.Rational(s).p)/sp.Rational(s).q for s in Dt['ea']['1,0']]
    e0 = max(abs(x - y) for x, y in zip(ex0, a0)); e1 = max(abs(x - y) for x, y in zip(ex1, a1))
    print(f"  X2: |A_exact - A_m4rh4| = {mp.nstr(e0, 3)} (mu = 0), {mp.nstr(e1, 3)} (first order, central difference)", flush=True)
    check("X2 (NUMERICAL): exact alpha layer at mu = 0 = m4_rh4 numerical, to 1e-30", e0 < mp.mpf(10)**-30)
    check("X2 (NUMERICAL): exact first-order alpha layer = m4_rh4 central difference, to 1e-15", e1 < mp.mpf(10)**-15)
    # (X3) truncation-depth independence: L1 (symbolic p, alpha; SHI = 16) specialised to (3/2, 3/10) equals Q1 (SHI = 30, default)
    fL = os.path.join(CACHE, 'eng_L1.json')
    if os.path.exists(fL):
        DL = json.load(open(fL)); sub = {sp.Symbol('p'): sp.Rational(3, 2), sp.Symbol('alpha'): sp.Rational(3, 10)}
        ok = True
        for part in ('e', 'ea'):
            for mo in ('0,0', '1,0', '2,0'):
                for sL, sQ in zip(DL[part][mo], Dt[part][mo]):
                    ok &= sp.simplify(sp.sympify(sL).subs(sub) - sp.Rational(sQ)) == 0
        check("X3: L1 (symbolic, SHI = 16) at (p, alpha) = (3/2, 3/10) equals Q1 (SHI = 30): b- and alpha-layers, orders <= 2 in e_1", ok)


names = sys.argv[1:] or list(CFG)
for nm in names: run_cfg(nm)
if 'Q1' in names: cross_checks()
print(f"identities: {NI[0]}, controls: {NC[0]}")
for f in FAILS: print("FAIL", f)
assert not FAILS, f"{len(FAILS)} failures"
print(f"ALL {NI[0]} IDENTITIES HOLD; ALL {NC[0]} CONTROLS FAIL")
