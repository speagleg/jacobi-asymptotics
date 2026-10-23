"""JZC_W2 Rule A cross-checks of the prediction machinery (NUMERICAL, independent code paths):
 (1) the exact engine's mu = 0 layer d_m vs the numeric engine m4_rh4 (w_common.model, decoupled M(beta', alpha), true c(p));
 (2) the exact first- and second-order Toda layers (normalised time e = X c^j C(2j, j), c = 1 frame) vs w_common.model's
     finite-difference responses r1, r2 at the true c (tests the c-scaling and the normalisation);
 (3) the first-order q1 lead vs W's pole term p R W(q) pi cot(pi q) (JZC_W_kappa P K.12);
 (4) the leading second-order pole layers vs the closed forms of Prop 2.2: q1^2 at n^{-2p}: L1^2 (3p - 1)/(2p);
     q1*t1 at n^{-1-2p}: 3 L1 eps_1 (eps_1 = first-order Toda lead).
Cases: P15a, P25a of w2_predict.py.  Tolerances: 1e-20 (exact vs exact), 1e-12 (vs finite differences)."""
import os, sys; os.environ['KORD'] = '8'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import mpmath as mp
from so_coeffs import c_p_mp
import w2_common as Wc
from w_common import model, W as Wq
Wc.provenance(__file__, Wc.__file__, Wc.ENGINE)
ok = True; nchk = 0
def chk(lab, c):
    global ok, nchk
    nchk += 1; ok &= c; print(f"[{nchk}] {lab}: {'PASS' if c else 'FAIL'}", flush=True)
for key, (p, d, kap, s, emax, kord) in {'P15a': ('3/2', '-1/4', '1/2', '11/5', 5.5, 6), 'P25a': ('5/2', '-1/4', '2/5', '2', 7.5, 8)}.items():
    case = Wc.kappa_case(p, d, kap, s, jmax=3, mmax=4); P = case['p_mp']; cp = mp.mpf(c_p_mp(P))
    terms, info = Wc.predict2(case, emax, cp, kord)
    fr = lambda x: mp.mpf(x.numerator)/x.denominator
    al, bp = fr(case['alpha']), fr(case['betap'])
    X = {l: x for l, j, x in info['times']}
    m = model(P, bp, al, (1,), ((1, 1),), 'w2cross_' + key)
    T = lambda lab, e: sum(v for ee, v, l, o in terms if l == lab and abs(ee - e) < 1e-9)
    for k in range(1, 6):
        chk(f"{key} (1) d{k}: exact {mp.nstr(T('model', k), 15)} vs numeric {mp.nstr(m['d'][k], 15)}", abs(T('model', k) - m['d'][k]) < 1e-20)
    s1 = float(P)
    for k in range(1, 4):
        chk(f"{key} (2) t1 first order n^-{s1 + k}: exact vs finite difference", abs(T('t1', s1 + k) - X['t1']*m['r1'][1][k]) < 1e-12)
    chk(f"{key} (2) t1^2 n^-{2*s1 + 2}: exact vs finite difference", abs(T('t1*t1', 2*s1 + 2) - X['t1']**2/2*m['r2'][(1, 1)][2]) < 1e-12)
    q = case['poles'][0]['q']; sq = float(P*fr(q)); L1 = P*case['poles'][0]['R']*Wq(fr(q), cp)*mp.pi*mp.cot(mp.pi*fr(q))
    chk(f"{key} (3) q1 lead = p R W(q) pi cot(pi q) = {mp.nstr(L1, 12)}", abs(T('q1', 1 + sq) - L1) < 1e-25)
    eps1 = T('t1', 1 + s1)
    chk(f"{key} (4) q1^2 lead n^-{2*sq + 2} = L1^2 (3p-1)/(2p)", abs(T('q1*q1', 2*sq + 2) - L1**2*(3*P - 1)/(2*P)) < 1e-25)
    chk(f"{key} (4) q1*t1 lead n^-{sq + s1 + 2} = 3 L1 eps1", abs(T('q1*t1', sq + s1 + 2) - 3*L1*eps1) < 1e-25)
print(f"ALL {nchk} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
