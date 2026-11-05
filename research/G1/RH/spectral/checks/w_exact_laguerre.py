"""JZC_W_exact §2: an EXACTLY SOLVABLE instance of the model with a branched tilt -- Laguerre = the decoupled model M(nu - 1, nu) at
p = -1 (c = 1, z = x/n, N = n + nu/2) -- and the structure of the fractional response.

(A) Identification (exact): the engine (w_exact_engine.py, PVAL = -1, SZOFF = -1, KORD = 6, symbolic (nu, j)) gives the integer layer
    F = 1 - nu^2/(8N^2) - nu^4/(128N^4) - nu^6/(1024N^6) = sqrt(1 - nu^2/(4N^2)) (Laguerre: b_n = sqrt(n(n+nu))), and its symbolic-j
    response g1[k] (natural form) equals, for k = 0..6 and identically in (nu, j = rho), the ANALYTIC part G^A of the exact Laguerre
    response to the normalised tilt exp(-mu z^rho / C(2rho,rho)) (w_exact_lag.response_A, from (L1)-(L4) of w_exact_lag.py).
    For integer j this is the exact Laguerre response (the branched part vanishes: 1/Gamma(-j)^2 = 0).
(B) The branched part (exact for Laguerre, from (L3)-(L4)): G^B = (Phi_nu(rho)/C(2rho,rho)) N^{-2rho-2} sum_k rat_k N^{-k} with
    rat_k = G^A_{k+1}(rho -> -1-rho) for k <= 5 ("reflection"), rat_0 = (rho+1)/2, rat_1 = rat_3 = 0.
(C) Pole cancellation (exact): G^A_k has poles at half-integers rho0 (from (-2rho)_i); each is cancelled by the branched term of the same
    power: Res_{rho0} G^A_k + Res_{rho0} [Phi/C rat_{k-2rho0-2}] = 0, for rho0 in {1/2, 3/2}, k <= 6 (the pole at 5/2 first appears in G_7).
(D) NUMERICAL (mpmath, 50 digits): (L1) against quadrature; (L3) at sample points; the Gamma-ratio series against mpmath; Phi_nu(rho)
    against the oscillatory integral int_0^inf y^rho J_nu(2 sqrt y)^2 dy (-1-nu < rho < -1/2, where it converges; quadosc ~1e-9); the full two-series form
    m_n = m^A + m^B against the exact finite sums (n = 100..800; residual ~ 1e-15 or below; control: m^A alone leaves ~ n^{-2rho-1});
    at rho = 1/2 the response contains 2 r log N N^{-3}, r = Res_{rho=1/2} G^A_3 = -3(1-4nu^2)/1024, checked on exact sums.
Controls (must fail): G^A re-expanded in the wrong natural index N' = n + (nu+1)/2 (an N'^-2 term appears); G^A without the (-2rho)_i structure (only i = 0); reflection with rho -> -rho."""
import os, sys, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
T0 = time.time()
os.environ["PVAL"] = "-1"; os.environ["SZOFF"] = "-1"; os.environ.setdefault("KORD", "6"); os.environ.setdefault("SHI", "22")
os.environ["EO"] = "1"; os.environ.pop("DECOUPLE", None)
import sympy as sp, mpmath as mp
import w_exact_lag as L
here = os.path.dirname(os.path.abspath(__file__))
for fn in [__file__, L.__file__, os.path.join(here, "w_exact_engine.py")]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
al, rho, J = L.al, L.rho, sp.Symbol('j')
KORD = int(os.environ["KORD"])

# ================= (D0) numerical checks of the Laguerre inputs =================
mp.mp.dps = 50
def S_exact(n, a, r):
    """(L1) finite sum, by recurrences"""
    lam = a + r; ak = mp.gamma(lam + 1); bm = [mp.mpf(1)]
    for m in range(1, n + 1): bm.append(bm[-1]*(m - 1 - r)/m)
    tot = 0
    for k in range(n + 1):
        if k > 0: ak = ak*(lam + k)/k
        tot += ak*bm[n - k]**2
    return tot
def m_exact(n, a, r): return S_exact(n, a, r)*mp.factorial(n)/mp.gamma(n + a + 1)
a0, r0 = mp.mpf("0.3"), mp.mpf("0.37")
q = mp.quad(lambda x: x**(a0 + r0)*mp.exp(-x)*mp.laguerre(5, a0, x)**2, [0, 5, 20, mp.inf])
chk("(L1) finite-sum formula = quadrature (n = 5, alpha = 0.3, rho = 0.37), rel < 1e-30", abs(q/S_exact(5, a0, r0) - 1) < mp.mpf(10)**-30)
chk("(L1) rho = 1: m_n = 2n + alpha + 1 (n = 7)", abs(m_exact(7, a0, mp.mpf(1)) - (15 + a0)) < mp.mpf(10)**-40)
dev = 0
for r in (r0, mp.mpf(2)/3, mp.mpf("1.3")):
    for x in (mp.mpf("0.3"), mp.mpf("0.7")):
        lhs = mp.hyp2f1(-r, -r, 1, x)
        rhs = (mp.gamma(1 + 2*r)/mp.gamma(1 + r)**2*mp.hyp2f1(-r, -r, -2*r, 1 - x)
               + (1 - x)**(1 + 2*r)*mp.gamma(-1 - 2*r)/mp.gamma(-r)**2*mp.hyp2f1(1 + r, 1 + r, 2 + 2*r, 1 - x))
        dev = max(dev, abs(lhs - rhs))
chk(f"(L3) connection formula at 3 rho x 2 x (max dev {mp.nstr(dev, 3)} < 1e-40)", dev < mp.mpf(10)**-40)
Ns = sp.Symbol('N'); dev = 0
for (aa, bb) in ((sp.Rational(3, 10) + sp.Rational(37, 100), sp.Rational(13, 10)), (-sp.Rational(9, 5), sp.Rational(13, 10))):
    R = L.gamma_ratio_series(aa, bb, 14); Nv = mp.mpf(200)
    mq = lambda x: mp.mpf(sp.Rational(x).p)/sp.Rational(x).q
    approx = Nv**mq(aa - bb)*sum(mq(R[k])*Nv**(-k) for k in range(15))
    exact = mp.gamma(Nv + mq(aa))/mp.gamma(Nv + mq(bb))
    dev = max(dev, abs(approx/exact - 1))
chk(f"gamma_ratio_series (DLMF 5.11.8 differenced) vs mpmath at N = 200, 14 terms (rel {mp.nstr(dev, 3)} < 1e-25)", dev < 1e-25)
def Phi(nu_, r): return mp.gamma(-1 - 2*r)*mp.gamma(nu_ + r + 1)*mp.rgamma(-r)**2*mp.rgamma(nu_ - r)
mp.mp.dps = 25
nu0, rr = mp.mpf("1.5"), mp.mpf("-1.6")          # convergent range: -1 - nu < rho < -1/2
I = mp.quadosc(lambda t: (t*t/4)**rr*mp.besselj(nu0, t)**2*t/2, [0, mp.inf], omega=2)      # y = t^2/4
chk(f"Phi_nu(rho) = int y^rho J_nu(2 sqrt y)^2 dy at (nu, rho) = (1.5, -1.6): {mp.nstr(I, 15)} vs {mp.nstr(Phi(nu0, rr), 15)} (quadosc, rel < 1e-7)",
    abs(I/Phi(nu0, rr) - 1) < 1e-7)
mp.mp.dps = 50

# ================= (A) engine at p = -1 vs Laguerre =================
import w_exact_engine as X
assert X.p == X.K(-1) and X.SZ == X.al - 1
t0 = time.time(); d, f, g = X.run(verbose=False, jmu='sym'); g1 = [x.as_expr().subs(J, rho) for x in g[1]]
print(f"   engine p = -1, KORD = {KORD}: {time.time() - t0:.0f}s", flush=True)
Fl = sp.series(sp.sqrt(1 - al**2*L.u**2/4), L.u, 0, KORD + 1).removeO()
chk(f"(A) integer layer f_0..f_{KORD} = sqrt(1 - nu^2/(4N^2)) (Laguerre)", all(sp.simplify(f[k].as_expr() - Fl.coeff(L.u, k)) == 0 for k in range(KORD + 1)))
GA = L.response_A(KORD)
for k in range(KORD + 1):
    chk(f"(A) engine g1[{k}](j = rho) = Laguerre analytic G^A_{k}", sp.simplify(g1[k] - GA[k]) == 0)
print("   G^A_3 =", GA[3], "\n   G^A_5 =", sp.factor(GA[5]), flush=True)
# control: Laguerre analytic response in the index N' = n + (nu+1)/2 (re-expand G^A(N) with N = N' - 1/2)
Np = sp.Symbol('Np'); expr = sum(GA[k]*(Np - sp.Rational(1, 2))**(-k) for k in range(KORD + 1))
ser = sp.series(expr.subs(Np, 1/L.u), L.u, 0, 4).removeO()
chk("(A) control: G^A in N' = n + (nu+1)/2 has no N'^-2 term", sp.simplify(ser.coeff(L.u, 2)) == 0, must_fail=True)
GA0 = L.response_A(4, ladder=lambda i: sp.Integer(1) if i == 0 else sp.Integer(0))
chk("(A) control: only the i = 0 term of P_1 (no (-2rho)_i structure) reproduces g1[3]", sp.simplify(g1[3] - GA0[3]) == 0, must_fail=True)

# ================= (B) branched part: reflection =================
GB = L.response_B(KORD - 1)
chk("(B) rat_0 = (rho+1)/2, rat_1 = rat_3 = 0", sp.simplify(GB[0] - (rho + 1)/2) == 0 and GB[1] == 0 and GB[3] == 0)
refl = all(sp.simplify(GB[k] - GA[k + 1].subs(rho, -1 - rho)) == 0 for k in range(KORD))
chk(f"(B) reflection rat_k = G^A_(k+1)(rho -> -1-rho), k <= {KORD - 1}", refl)
chk("(B) control: reflection rho -> -rho", all(sp.simplify(GB[k] - GA[k + 1].subs(rho, -rho)) == 0 for k in range(KORD)), must_fail=True)

# ================= (C) pole cancellation =================
for r0_ in (sp.Rational(1, 2), sp.Rational(3, 2)):          # at KORD = 6 the pole at 5/2 is not yet reached (G_7)
    good = True; npole = 0
    for k in range(KORD + 1):
        resA = sp.cancel((rho - r0_)*GA[k]).subs(rho, r0_) if GA[k] != 0 else 0
        kB = k - int(2*r0_ + 2)
        resB = L.PhiC_residue(r0_)*GB[kB].subs(rho, r0_) if 0 <= kB < len(GB) else 0
        if resA != 0: npole += 1
        good &= sp.simplify(resA + resB) == 0
    chk(f"(C) rho0 = {r0_}: Res G^A_k + Res (Phi/C) rat_(k-2rho0-2) = 0 for k <= {KORD} ({npole} nonzero poles)", good and npole > 0)
r_half = sp.factor(sp.cancel((rho - sp.Rational(1, 2))*GA[3]).subs(rho, sp.Rational(1, 2)))
print(f"   r := Res_(rho=1/2) G^A_3 = {r_half}  (= G_1 Res g = -(1/4) Res g at p = -1)", flush=True)

# ================= (D) numerical: two-series form and the rho = 1/2 log =================
def mA_fin(n, a, r, I=14):
    c2 = mp.gamma(1 + 2*r)/mp.gamma(1 + r)**2; tot = 0
    for i in range(I):
        co = mp.rf(-r, i)**2/(mp.rf(-2*r, i)*mp.factorial(i))*mp.rf(a + r + 1 - i, i)
        tot += co*mp.gamma(n + a + r + 1 - i)/mp.gamma(n + a + 1)
    return c2*tot
def mB_fin(n, a, r, I=14):
    tot = 0
    for i in range(I):
        co = mp.rf(1 + r, i)**2/(mp.rf(2 + 2*r, i)*mp.factorial(i))*mp.rf(a - r - i, i)
        tot += co*mp.gamma(n + a - r - i)/mp.gamma(n + a + 1)
    return Phi(a, r)*tot
worst = 0; ctrl = []
for a in (mp.mpf("0.3"), mp.mpf("-0.4")):
    for r in (mp.mpf("0.37"), mp.mpf(2)/3, mp.mpf("1.3")):
        for n in (100, 200, 400, 800):
            me = m_exact(n, a, r); ma = mA_fin(n, a, r); mb = mB_fin(n, a, r)
            worst = max(worst, abs(me - ma - mb)/abs(me))
            if n == 800 and Phi(a, r) != 0: ctrl.append((float(r), float(abs(me - ma)/abs(me)), float(abs(mb)/abs(me)), float(mp.mpf(n)**(-2*r - 1))))
print(f"   max |m - m^A - m^B|/|m| = {mp.nstr(worst, 3)};  n = 800: (rho, |m - m^A|/|m|, |m^B|/|m|, n^(-2rho-1)) =",
      [tuple(round(x, 18) if i == 0 else float(f'{x:.3g}') for i, x in enumerate(t)) for t in ctrl], flush=True)
chk("(D) m_n = m^A + m^B (14 terms each) to < 1e-18 relative (2 alpha x 3 rho x n = 100..800)", worst < 1e-18)
chk("(D) control: m^A alone reproduces m_n to < 1e-18 at n = 800 in every case with Phi != 0 (Phi = 0 at alpha = 0.3, rho = 1.3)",
    all(t[1] < 1e-18 for t in ctrl), must_fail=True)
# rho = 1/2: response G(N) = -(1/2) sqrt(1 - a^2/(4N^2)) N^{-1/2} (m_n - m_{n-1}) / C(1, 1/2); y := N^3 (G - G_1/N) = c0 + 2 r log N + ...
for a in (mp.mpf("0.3"), mp.mpf(0)):
    rv = mp.mpf(1)/2; C1 = mp.gamma(2)/mp.gamma(mp.mpf(3)/2)**2; ys = []
    nlist = (1000, 2000, 4000, 8000)
    for n in nlist:
        Nn = n + a/2
        Gv = -mp.mpf(1)/2*mp.sqrt(1 - a**2/(4*Nn**2))*Nn**(-rv)*(m_exact(n, a, rv) - m_exact(n - 1, a, rv))/C1
        ys.append((Nn, Nn**3*(Gv + rv/2/Nn)))          # G_1 = -rho/2
    slopes = [(ys[i + 1][1] - ys[i][1])/(mp.log(ys[i + 1][0]) - mp.log(ys[i][0])) for i in range(3)]
    pred = 2*float(r_half.subs(al, sp.Float(str(a))))
    print(f"   rho = 1/2, alpha = {a}: d y / d log N = {[mp.nstr(s, 10) for s in slopes]}, predicted 2r = {pred:.10f}", flush=True)
    chk(f"(D) rho = 1/2, alpha = {a}: log N N^-3 coefficient = 2 Res_(1/2) G^A_3 (last slope, rel < 1e-5)", abs(slopes[-1]/pred - 1) < 1e-5)
print(f"total {NCHK} checks ({time.time() - T0:.0f}s)")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
