"""JZC_W_exact §1: the band-factor gauge of a BRANCHED tilt exp(-mu z^rho), rho not an integer (c = 1, band [0, 4]).

For an entire tilt V = z^j the E3 gauge uses M = Q_j, the polynomial part of z^j/R(z), R = sqrt(z(z-4)) (check_e3_gauge.py).
For V = z^rho (principal branch, cut (-inf, 0]) the analogue is M_rho := z^rho/R - 2 C_rho, C_rho the Cauchy transform of
x^rho/R_+(x) on [0, 4]; M_rho is analytic off (-inf, 0] and its jump there is that of z^rho/R. For -1/2 < rho < 1:
    M_rho(z) = (sin(pi rho)/pi) int_0^inf s^{rho-1/2} (s+4)^{-1/2} (s+z)^{-1} ds          (Stieltjes form; Cauchy transform of the jump).
Lemma WE.1 (asserted here):
  (i)  Taylor data at 4:  [w^m] M_rho(4 + w) = C(2rho,rho) rho(rho-1)...(rho-m)/(4^{m+1} (1/2)_{m+1})  -- EXACT (Beta integral + Gamma
       identities, sympy, symbolic rho, m <= 8); = the engine's symbolic-j data at 4 (m4_zeta_exact2.py docstring) at j = rho.
  (ii) M_rho = A_rho + tan(pi rho) z^{rho-1/2} (4 - z)^{-1/2} near 0, A_rho analytic at 0 with
       [z^m] A_rho = C(2rho,rho) prod_{i=0}^m (rho-i)/(2(2rho-2i-1))  -- the engine's symbolic-j data at 0, at j = rho.
       The Taylor coefficients: EXACT (Mellin continuation of the Stieltjes form, Gamma identities, symbolic rho); the branched term:
       EXACT from the jump condition (it is the unique z^{rho-1/2} x analytic function with the jump of z^rho/R on (-4, 0)), and
       the full decomposition is checked NUMERICALLY (mpmath quad, 30 digits) at rho in {0.3, -0.2, 2/3, 0.9}.
  (iii) Hence R M_rho = R A_rho -/+ i tan(pi rho) z^rho near 0 (sign = side of the band): the branched part of the gauge exponent is
       a multiple of z^rho with a side-dependent sign, i.e. NOT of the form of the engine's jump conjugation (the engine handles A_rho).
  (iv) E3.7 for the branched tilt at the n^{-1} level: the response of the 1/n coefficient is c p M_rho(4c) = p rho C(2rho,rho)/2 per
       unit mu (route 1 of m3a_e37_decoupled: e(M) - e(0) = c p M(4c) for ARBITRARY M analytic at 4c, all orders in mu), i.e. W's
       -(p rho W(rho)/2) t_rho with W(rho) = (4c)^rho Gamma(rho+1/2)/(sqrt(pi) Gamma(rho+1)) = C(2rho,rho) c^rho  -- EXACT algebra.
  (v)  Exact linearity to third order of the 1/n coefficient for the A-gauge with SYMBOLIC j (route 2, engine copy, DECOUPLE=1,
       EO = 3, identically in (p, nu, beta, j)): first-order response p j/2 (per mu C(2j,j)), second and third order 0.
Controls (must fail): (ii) with sin(pi rho) in place of tan(pi rho); (ii) without the branched term; (i) with (1/2)_m in place of
(1/2)_{m+1}; route 2 first-order response = 0."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, mpmath as mp

NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)

def _prov():
    import hashlib
    for fn in [__file__, os.path.join(os.path.dirname(os.path.abspath(__file__)), "w_exact_engine.py")]:
        print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
_prov()

r = sp.Symbol('rho')
def C2(x): return sp.gamma(2*x + 1)/sp.gamma(x + 1)**2
def eqg(a, b):
    return sp.simplify(sp.gammasimp(sp.combsimp(sp.expand_func(a/b))) - 1) == 0

# ---- (i) Taylor data at 4 ----
ok_i = True; ok_ic = True
for m in range(9):
    lhs = (-1)**m*sp.sin(sp.pi*r)/sp.pi*4**(r - m - 1)*sp.gamma(r + sp.Rational(1, 2))*sp.gamma(m + 1 - r)/sp.gamma(m + sp.Rational(3, 2))
    lhs = lhs.subs(sp.sin(sp.pi*r), sp.pi/(sp.gamma(r)*sp.gamma(1 - r)))          # reflection formula
    rhs = C2(r)*sp.prod([r - i for i in range(m + 1)])/(4**(m + 1)*sp.rf(sp.Rational(1, 2), m + 1))
    ok_i &= eqg(lhs, rhs)
    if m >= 1: ok_ic &= eqg(lhs, C2(r)*sp.prod([r - i for i in range(m + 1)])/(4**(m + 1)*sp.rf(sp.Rational(1, 2), m)))
chk("(i) [w^m] M_rho(4+w) = C(2rho,rho) rho(rho-1)..(rho-m)/(4^{m+1}(1/2)_{m+1}), m <= 8, symbolic rho", ok_i)
chk("(i) control: (1/2)_m in place of (1/2)_{m+1}", ok_ic, must_fail=True)

# ---- (ii) analytic part at 0: Mellin continuation of the Stieltjes form ----
ok_ii = True
for m in range(9):
    lhs = (-1)**m/(sp.gamma(r)*sp.gamma(1 - r))*4**(r - m - 1)*sp.gamma(r - sp.Rational(1, 2) - m)*sp.gamma(m + 1 - r)/sp.sqrt(sp.pi)
    rhs = C2(r)*sp.prod([(r - i)/(2*(2*r - 2*i - 1)) for i in range(m + 1)])
    ok_ii &= eqg(lhs, rhs)
chk("(ii) [z^m] A_rho = C(2rho,rho) prod_{i<=m} (rho-i)/(2(2rho-2i-1)), m <= 8, symbolic rho", ok_ii)

# ---- (ii) numerical: the full decomposition ----
mp.mp.dps = 40
def M_stieltjes(rh, z, S=1000, KT=60):
    """head [0, S] by tanh-sinh quadrature; tail [S, inf) by the exact termwise integral of the convergent expansion
    (s+4)^{-1/2}(s+z)^{-1} = s^{-3/2} sum_k e_k s^{-k} (|4/S|, |z/S| << 1)."""
    rh = mp.mpf(rh); h = mp.mpf(1)/2
    f = lambda s: s**(rh - h)*(s + 4)**(-h)/(s + z)
    q = 2/(2*rh + 1)                                    # s = t^q on [0, 1] removes the endpoint singularity s^{rho-1/2}
    g = lambda t: q*(t**q + 4)**(-h)/(t**q + z)
    head = mp.quad(g, [0, mp.mpf(1)/2, 1]) + mp.quad(f, [1, 10, 100, S])
    a = [mp.binomial(-h, k)*4**k for k in range(KT)]; b = [(-z)**k for k in range(KT)]
    e = [sum(a[i]*b[k - i] for i in range(k + 1)) for k in range(KT)]
    tail = sum(e[k]*mp.mpf(S)**(rh - 1 - k)/(1 + k - rh) for k in range(KT))
    return mp.sin(mp.pi*rh)/mp.pi*(head + tail)
def A_ser(rh, z, M=260):
    rh = mp.mpf(rh); c2 = mp.gamma(2*rh + 1)/mp.gamma(rh + 1)**2; tot = 0; t = c2
    for m in range(M):
        t = t*(rh - m)/(2*(2*rh - 2*m - 1)); tot += t*z**m
    return tot
def M_dec(rh, z, branch=True, fn=mp.tan):
    rh = mp.mpf(rh)
    return A_ser(rh, z) + (fn(mp.pi*rh)*z**(rh - mp.mpf(1)/2)*(4 - z)**(-mp.mpf(1)/2) if branch else 0)
def T4_ser(rh, w, M=80):
    rh = mp.mpf(rh); c2 = mp.gamma(2*rh + 1)/mp.gamma(rh + 1)**2; tot = 0; num = 1
    for m in range(M):
        num = num*(rh - m); tot += c2*num/(4**(m + 1)*mp.rf(mp.mpf(1)/2, m + 1))*w**m
    return tot
worst = 0; worst_c1 = mp.inf; worst_c2 = mp.inf; worst4 = 0
for rv in (mp.mpf("0.3"), mp.mpf("-0.2"), mp.mpf(2)/3, mp.mpf("0.9")):
    for z in (mp.mpf("0.5"), mp.mpc(1, 1), mp.mpf("2.5"), mp.mpc("-1.5", "0.7")):
        ms = M_stieltjes(rv, z)
        worst = max(worst, abs(ms - M_dec(rv, z))/abs(ms))
        worst_c1 = min(worst_c1, abs(ms - M_dec(rv, z, fn=mp.sin))/abs(ms))
        worst_c2 = min(worst_c2, abs(ms - M_dec(rv, z, branch=False))/abs(ms))
    for w in (mp.mpf("0.3"), mp.mpc("-0.5", "1.1")):
        ms = M_stieltjes(rv, 4 + w); worst4 = max(worst4, abs(ms - T4_ser(rv, w))/abs(ms))
print(f"   max rel. deviation: decomposition near 0 {mp.nstr(worst, 3)}; Taylor series at 4 {mp.nstr(worst4, 3)}")
chk("(ii) M_rho = A_rho + tan(pi rho) z^{rho-1/2}(4-z)^{-1/2} (4 rho x 4 z, quad at 40 digits, rel. dev < 1e-20)", worst < mp.mpf(10)**-20)
chk("(i) M_rho(4+w) = its Taylor series (4 rho x 2 w, rel. dev < 1e-20)", worst4 < mp.mpf(10)**-20)
chk("(ii) control: sin(pi rho) in place of tan(pi rho) (rel. dev < 1e-6 somewhere)", worst_c1 < 1e-6, must_fail=True)
chk("(ii) control: no branched term (rel. dev < 1e-6 somewhere)", worst_c2 < 1e-6, must_fail=True)

# ---- (iii) the branched part of R M near 0 ----
# R = sqrt(z(z-4)) (R ~ z at inf); tan(pi rho) z^{rho-1/2}(4-z)^{-1/2} R = s i tan(pi rho) z^rho, s = +-1 by the side
rv = mp.mpf("0.3"); vals = []
for z in (mp.mpc("0.5", "0.2"), mp.mpc("0.5", "-0.2"), mp.mpc("-0.7", "0.3"), mp.mpc("-0.7", "-0.3")):
    R = mp.sqrt(z)*mp.sqrt(z - 4)                     # = sqrt(z(z-4)) with R ~ z at infinity (cut [0, 4])
    vals.append((mp.tan(mp.pi*rv)*z**(rv - 0.5)*(4 - z)**(-0.5)*R)/(1j*mp.tan(mp.pi*rv)*z**rv))
print("   R M_br / (i tan(pi rho) z^rho) at Im z > 0, < 0, > 0, < 0:", [mp.nstr(v, 8) for v in vals])
chk("(iii) R M_br = s i tan(pi rho) z^rho with s = +1 (Im z > 0), -1 (Im z < 0)",
    all(abs(v - s) < 1e-25 for v, s in zip(vals, (1, -1, 1, -1))))

# ---- (iv) E3.7 coefficient -> W's linear response ----
p, c, t = sp.symbols('p c t', positive=True)
Wr = (4*c)**r*sp.gamma(r + sp.Rational(1, 2))/(sp.sqrt(sp.pi)*sp.gamma(r + 1))
chk("(iv) W(rho) = C(2rho,rho) c^rho (Legendre duplication)", eqg(Wr, C2(r)*c**r))
# response of the n^{-1} coefficient of n^p b_n/c to the tilt exp(t x^rho) = exp(-mu z^rho), mu = -t n^{-p rho} (z = n^p x):
# per unit mu: c p M(4c) with M(4c) = c^{rho-1} rho C(2rho,rho)/2 (scaling of (i) to general c); so the n^{-1-p rho} coefficient is
M4c = c**(r - 1)*r*C2(r)/2
chk("(iv) c p M(4c) (-t) = -(p rho W(rho)/2) t", sp.simplify(sp.gammasimp(c*p*M4c*(-t) + p*r*Wr/2*t)) == 0)

# ---- (v) route 2: exact linearity of the 1/n coefficient, symbolic j, decoupled, EO = 3 ----
os.environ["DECOUPLE"] = "1"; os.environ["KORD"] = "1"; os.environ["EO"] = "3"; os.environ["SHI"] = "10"
os.environ.pop("PVAL", None); os.environ.pop("SZOFF", None)
import w_exact_engine as X
assert X.DECOUPLE and X.PVAL is None
cap = {}
def tr(frame, event, arg):
    if frame.f_code is X.run.__code__:
        def loc(f, ev, a):
            if ev == "return": cap.update(f.f_locals)
            return loc
        return loc
    return None
t0 = time.time(); sys.settrace(tr)
try: X.run(verbose=False, jmu='sym')
finally: sys.settrace(None)
ee = cap["e"]; P, NU, BE, J = sp.symbols('p alpha beta j')
e0, e1, e2, e3 = (ee[m][1].as_expr() for m in range(4))
print(f"   route 2 ({time.time() - t0:.0f}s): d1 = {sp.factor(e0)}, first-order = {sp.factor(e1)}")
chk("(v) d1 = -p(beta+1)/2 (decoupled)", sp.simplify(e0 + P*(BE + 1)/2) == 0)
chk("(v) first-order mu response of the 1/n coefficient = p j/2 (per mu C(2j,j)), identically in (p, nu, beta, j)", sp.simplify(e1 - P*J/2) == 0)
chk("(v) second- and third-order responses of the 1/n coefficient vanish identically", e2 == 0 and e3 == 0)
chk("(v) control: first-order response = 0", sp.simplify(e1) == 0, must_fail=True)

print(f"total {NCHK} checks")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
