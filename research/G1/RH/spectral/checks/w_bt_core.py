"""w_bt_core: the hard-edge companion of a branched tilt exp(-mu z^rho), computed from the lip mismatch (JZC_W_BT.md §2-§3).

Setting (JZC_W_BT.md §2): the decoupled model M(beta, nu) (JZC_M4 §7) with the tilt h = exp(-mu z^rho) on the band, c = 1. The
engine's parametrix uses the ANALYTIC part rho_a of the Szego ratio (A_rho-gauge; JZC_W_exact Lemma WE.1); the true lip jump uses
rho = rho_a rho_x, rho_x = exp(-/+ (i/2) mu tan(pi rho) z^rho) in C_+/-. So R = Q P0hat_a^{-1} acquires, inside U_0, the lip jump
  I + varrho_+/- (rho_x^{-2} - 1) C L(zeta) C^{-1},   C X C^{-1} := P0inf rho_mod^{s3} X rho_mod^{-s3} P0inf^{-1} (engine's conj_hard),
  L(zeta) = M zeta^{s3/4} (2 pi)^{s3/2} [e^{-4 zeta^{1/2}} Phi_nu E21 Phi_nu^{-1}] (2 pi)^{-s3/2} zeta^{-s3/4} M^{-1}
          = (w/pi) [K^2 L1 + K'^2 L2 + K K' L3],  w = 2 zeta^{1/2}, K = K_nu(w), L1 = M E12 M^-1, L2 = M E21 M^-1, L3 = M (i s3) M^-1.
First order in mu, after deforming both lips onto (-delta, 0) (JZC_W_BT Lemma BT.2):
  dR1_lip = (i mu tan(pi rho) sin(pi(rho - nu))/pi) int_0^delta x^rho Rin C L C^{-1} Rin^{-1} (z = -x) dx + O(e^{-cn}).
With z = -v^2, v = V(y) (inverse of f^{1/2} = fh), y = w/(2n), and the Mellin moments of K^2, K'^2, K K' (Lemma BT.3),
  dR1_lip = -(i/2) mu (p+2)^{2rho+1} Phi_nu(rho) n^{-2rho-2} Lambda(n)  (+ the 'odd-shift' part with K(2rho+3), asserted to vanish),
  Lambda(n) = sum_{i,m,k} tau_{i,m,k} a_{i,m} 2^{-m} n^{-m-k},
tau_{i,m,k} = [y^m n^-k] u^{2rho+1} V'(y) S_i(V(y)),  u = V/((p+2)y),  S_i = Rin C L_i C^{-1} Rin^{-1},
a_{i,m} = M_i(2rho+3+m)/K(2rho+2) (rational), M_1 = K(s), M_2(s) = [(s-2)^2/2 - nu^2] K(s-2) - K(s), M_3(s) = -((s-1)/2) K(s-1),
K(s) := int_0^inf w^{s-1} K_nu(w)^2 dw = 2^{s-3} Gamma(s/2+nu) Gamma(s/2-nu) Gamma(s/2)^2/Gamma(s),  K(s+2) = q(s) K(s),
q(s) = (s^2 - 4 nu^2) s/(4(s+1)),  and tan(pi rho) sin(pi(rho-nu)) K(2rho+2) = -2^{2rho} pi^2 Phi_nu(rho).
The extraction is the engine's: n^p b_n/c = sqrt(Q12 Q21), Q1 = P1 + R1.
Field: the engine's Q(p, alpha, j, beta) [or Q(alpha, j, beta) with PVAL], with alpha = nu (Bessel order), j = rho, beta = Szego exponent."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["EO"] = "0"
import w_bt_engine as X
from w_bt_engine import K, G, S, GZ, G1, GI, ONE, ZERO, HALF, mmul, madd, msub, mscal
p, nu, rho, be = X.p, X.al, X.jj, X.SZ
TWO = K(2)


def ser_deriv(s):
    return S(s.lo - 1, [s.get(t)*G(K(t)) for t in range(s.lo, s.hi + 1)], s.hi - 1)


def ser_pow_int(V, t, Vinv):
    out = S.const(1)
    b = V if t >= 0 else Vinv
    for _ in range(abs(t)): out = out*b
    return out


def compose(F, V, Vinv):
    """F(V(y)) for a Laurent series F (finitely many negative powers) and V = c y + ..., c != 0."""
    out = S.const(0)
    pw = {}
    for t in range(F.lo, F.hi + 1):
        c = F.get(t)
        if c.iszero(): continue
        out = out + ser_pow_int(V, t, Vinv)*c
    return out


def inverse_series(fh, hi):
    """V with fh(V(y)) = y; fh = v/(p+2) (1 + O(v^2)) odd."""
    phi = (fh*G((p + 2))).shift(-1)                      # fh (p+2)/v = 1 + ...
    V = S(1, [G(p + 2)], hi)
    for _ in range(hi + 2):
        Vinv = V.inv()
        V = S(1, [G(p + 2)], hi)*compose(phi, V, Vinv).inv()
        V = S(V.lo, [V.get(t) for t in range(V.lo, hi + 1)], hi)
    return V


def q(s): return (s*s - 4*nu*nu)*s/(4*(s + 1))


def Kc(o):
    """K(2rho+2+o) = (cB0, cB1) in the basis B0 = K(2rho+2), B1 = K(2rho+3)."""
    base, b = (2*rho + 2, 0) if o % 2 == 0 else (2*rho + 3, 1)
    oo = o - b                                           # even offset from base
    c = ONE
    if oo >= 0:
        for l in range(oo//2): c = c*q(base + 2*l)
    else:
        for l in range(-oo//2): c = c/q(base + oo + 2*l)
    return (c, ZERO) if b == 0 else (ZERO, c)


def Mom(i, m):
    """M_i(2rho+3+m) in the basis (B0, B1); i = 1: K^2, 2: K'^2, 3: K K'."""
    s = 2*rho + 3 + m; o = 1 + m                        # s = 2rho+2+o
    if i == 1: return Kc(o)
    if i == 3:
        a, b = Kc(o - 1); f = -(s - 1)/2; return (a*f, b*f)
    a2, b2 = Kc(o - 2); a0, b0 = Kc(o); f = (s - 2)**2/2 - nu*nu
    return (a2*f - a0, b2*f - b0)


M0 = [[G1, GI], [GI, G1]]; Mi0 = [[G1, -GI], [-GI, G1]]
E12 = [[GZ, G1], [GZ, GZ]]; E21 = [[GZ, GZ], [G1, GZ]]; iS3 = [[GI, GZ], [GZ, -GI]]
LB = {i: mscal(mmul(mmul(M0, E), Mi0), HALF) for i, E in ((1, E12), (2, E21), (3, iS3))}


def run(KC, verbose=False, control=None):
    """returns dict with: 'lam' (Lambda good part, list of 2x2 G by power n^{-e}, e from elo), 'lam_bad', 'elo',
    'comp_raw' [c_k] (companion of n^p b_n/c per unit mu, in units of (p+2)^{2rho+1} Phi n^{-2rho-2}, coefficient of n^{-k}),
    'comp_nat' (natural form, coefficients of N^{-k} after N^{-2rho-2}), 'R1', 'd'."""
    X.run(verbose=verbose)
    E = X.EXPORT
    Rin0, conj_hard, z_to_v, fh, delta = E['Rin']['0'], E['conj_hard'], E['z_to_v'], E['fh'], E['delta']
    KO = X.KORD; assert KC <= KO
    hi = KC + 6
    # Rin in v, and its inverse as a series in 1/n
    Rv = {k: [[z_to_v(Rin0[k][i][j]) for j in range(2)] for i in range(2)] for k in range(KC + 1)}
    Rv[0] = [[S.const(1), S.const(0)], [S.const(0), S.const(1)]]
    if control == 'rin_identity':                        # CONTROL: drop the R_in dressing (must fail)
        for k in range(1, KC + 1): Rv[k] = [[S.const(0), S.const(0)], [S.const(0), S.const(0)]]
    Rinv = {0: Rv[0]}
    for k in range(1, KC + 1):
        acc = [[S.const(0), S.const(0)], [S.const(0), S.const(0)]]
        for j in range(1, k + 1): acc = madd(acc, mmul(Rv[j], Rinv[k - j]))
        Rinv[k] = [[-acc[i][j] for j in range(2)] for i in range(2)]
    CL = {i: conj_hard(LB[i]) for i in LB}
    V = inverse_series(fh, hi); Vinv = V.inv(); Vp = ser_deriv(V)
    u = (V*G(1/(p + 2))).shift(-1); ue = u.powr1(2*rho + 1)
    pref = ue*Vp
    lam = {}; lam_bad = {}
    for i in CL:
        for k in range(KC + 1):
            Sk = [[S.const(0), S.const(0)], [S.const(0), S.const(0)]]
            for a in range(k + 1): Sk = madd(Sk, mmul(mmul(Rv[a], CL[i]), Rinv[k - a]))
            for r in range(2):
                for c in range(2):
                    T = pref*compose(Sk[r][c].trim() if not all(x.iszero() for x in Sk[r][c].c) else S.const(0), V, Vinv)
                    for m in range(T.lo, KC - k + 1):
                        tau = T.get(m)
                        if tau.iszero(): continue
                        aM, bM = Mom(i, m)
                        if control == 'no_K2' and i == 1: aM = ZERO   # CONTROL: drop the K^2 moments (must fail)
                        e = m + k; w = tau*G(1/TWO**m) if m >= 0 else tau*G(TWO**(-m))
                        lam.setdefault(e, [[GZ, GZ], [GZ, GZ]]); lam_bad.setdefault(e, [[GZ, GZ], [GZ, GZ]])
                        lam[e][r][c] = lam[e][r][c] + w*aM; lam_bad[e][r][c] = lam_bad[e][r][c] + w*bM
    elo = min(lam)
    # extraction: companion of sqrt(Q12 Q21) = (Lam12 Q21 + Q12 Lam21)/(2 sqrt(Q12 Q21)) times -(i/2)
    R1 = E['R1']
    Q12 = S(0, [GI] + [R1[k][0][1] for k in range(1, KC + 1)], KC); Q21 = S(0, [-GI] + [R1[k][1][0] for k in range(1, KC + 1)], KC)
    bh = (Q12*Q21).powr1(HALF)
    L12 = S(elo, [lam.get(e, [[GZ, GZ], [GZ, GZ]])[0][1] for e in range(elo, KC + 1)], KC)
    L21 = S(elo, [lam.get(e, [[GZ, GZ], [GZ, GZ]])[1][0] for e in range(elo, KC + 1)], KC)
    num = L12*Q21 + Q12*L21
    comp = num*bh.inv()*G(ZERO, -K(1)/4)                 # -(i/2) * 1/2
    craw = [comp.get(k) for k in range(comp.lo, KC + 1)]
    assert all(x.b == ZERO for x in craw), "imaginary companion"
    craw = {k: comp.get(k).a for k in range(comp.lo, KC + 1)}
    # natural form: N^{-2rho-2} (1 - delta x)^{-((rho+1)p + 2rho + 2)} sum_k c_k x^k (1 - delta x)^{-k}, x = 1/N
    x = S(1, [G1], KC); one = S.const(1)
    w1 = (one - x*G(delta))
    inv_n = x*w1.inv()
    tot = S.const(0); qn = S.const(1)
    pos = {k: v for k, v in craw.items() if k < 0 and v != ZERO}
    assert not pos, ("companion has positive powers of n", {k: v.as_expr() for k, v in pos.items()})
    for k in range(0, KC + 1):
        if k > 0: qn = qn*inv_n
        tot = tot + qn*G(craw.get(k, ZERO))
    Fn = w1.powr1(-((rho + 1)*p + 2*rho + 2))*tot
    cnat = [Fn.get(k).a for k in range(KC + 1)]
    return dict(lam=lam, lam_bad=lam_bad, elo=elo, comp_raw=craw, comp_nat=cnat, R1=R1, d=E['d'], delta=delta)
