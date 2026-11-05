"""JZC M4 section 6: the zeta layer in natural form, from the order-k RH computation WITH the band factor (E3 Lemma E3.4 gauge:
Delta_k^mu = G_mu Delta_k^mod G_mu^{-1}, G_mu = T[[cosh h, -(z-4c) S], [-z S, cosh h]]T^{-1}, h = R M_mu/2, S = sinh(h)/R;
m4_rh4.run(..., mu = {k: mu_k})). The band factor is H_n ~ exp(-sum_k mu_{n,k} x^k), mu_{n,k} = 2 zeta(-kp)/(k n^{kp}) (E3 Lemma F.1').

Derivatives in mu by central differences (dps 50; step 1e-15 for first, 1e-12 for second derivatives). For a response
sum_k e_k n^{-k} (per unit mu) multiplying n^{-jp}, the natural form is (N/n)^{(j+1)p} sum_k e_k n^{-k} expanded in 1/N.
Claims checked at points NOT used in the reconstructions (reconstruction grids: p in {1/2, 2/3, 3/4, 5/4, 3/2, 5/2, 3, 7/2, 4, 5,
6, 8, 10}, alpha in {0, +-1, +-2, 3}):
  (Z1) first order in mu_j (j = 1..5): leading coefficient = C(2j, j) p c^j * (per-unit normalisation) [E3 Lemma E3.7];
       the N^{-2-jp}, N^{-4-jp} coefficients vanish; N^{-3-jp} / N^{-1-jp} = g_j := A_j + B_j alpha^2 with
       A_j = [j^2(j^2+2j-2)p^3 + 2(j+1)(2j^2-1)p^2 + (5j^2+2j-6)p + 2(j-2)] / (24(2j-1)p),
       B_j = (p+2)(j^2 p^2 + (j+1)p + 2) / (8(2j-1)p).
  (Z2) j = 1, next order: N^{-5-p}/N^{-1-p} = g1_4 (closed form below).
  (Z3) second order in mu_1: no N^{-1-2p} term (E3 Lemma E3.7), no N^{-3-2p}, N^{-5-2p}; the zeta(-p)^2 layer starts at
       N^{-2-2p} = (N^{-1-p})^2 with coefficient (3p+1)/(2p) * eps_1^2 (eps_1 = 2pc zeta(-p)), independent of alpha.
c = 1 throughout (all inputs depend on z/c only)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "5")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
mp.mp.dps = 50
C_ = Checks()


def toN(e, p, al, pw):
    delta = mp.mpf(al)/2 + mp.mpf(1)/2; S = M.S; S.HI, h0 = M.KORD, S.HI
    x = S(1, [1]); one = S.const(1); inv_n = x*(one - x*delta).inv()
    tot = S.const(e[0]); q = S.const(1)
    for k in range(1, M.KORD + 1): q = q*inv_n; tot = tot + q*e[k]
    F = (one - x*delta).powr(-pw)*tot; S.HI = h0
    return [mp.re(F.get(k)) for k in range(M.KORD + 1)]


def first(p, al, j, h=mp.mpf(10)**-15):
    a, _ = M.run(p, al, mu={j: h}); b, _ = M.run(p, al, mu={j: -h})
    return toN([(x - y)/(2*h) for x, y in zip(a, b)], p, al, (j + 1)*p)


def A_j(p, j): return (j**2*(j**2 + 2*j - 2)*p**3 + 2*(j + 1)*(2*j**2 - 1)*p**2 + (5*j**2 + 2*j - 6)*p + 2*(j - 2))/(24*(2*j - 1)*p)
def B_j(p, j): return (p + 2)*(j**2*p**2 + (j + 1)*p + 2)/(8*(2*j - 1)*p)
def g1_4(p, a):
    return ((p + 1)*(9*p**6 + 117*p**5 + 161*p**4 - 569*p**3 - 1550*p**2 - 976*p + 48)/(5760*p**2*(3*p + 2))
            + (p + 1)*(p + 2)*(3*p**4 + 33*p**3 + 124*p**2 + 182*p + 108)*a**2/(192*p*(3*p + 2))
            + (p + 2)**3*(p**3 - 4*p - 4)*a**4/(128*p*(3*p + 2)))


pts = [(mp.mpf(7)/3, mp.mpf('0.6')), (mp.mpf('0.45'), mp.mpf('-0.3')), (mp.mpf('2.2'), mp.mpf(2)), (mp.mpf(9)/2, mp.mpf('1.3'))]
for p, al in pts:
    lab = f"p={mp.nstr(p, 4)} al={mp.nstr(al, 3)}"
    for j in range(1, 6):
        B = first(p, al, j)
        lead = mp.binomial(2*j, j)*p*(mp.mpf(j)/2)                 # per unit mu_j: eps_j = C(2j,j) p c^j zeta(-jp), mu_j = 2 zeta(-jp)/j
        g = B[3]/B[1]; pred = A_j(p, j) + B_j(p, j)*al**2
        print(f"{lab} j={j}: lead {mp.nstr(B[1], 12)} (pred {mp.nstr(lead, 12)});  N^-(2+jp) {mp.nstr(B[2], 3)}  N^-(4+jp) {mp.nstr(B[4], 3)};"
              f"  g_j {mp.nstr(g, 15)}  pred {mp.nstr(pred, 15)}", flush=True)
        C_.check(f"{lab} j={j}: leading = C(2j,j) p c^j (E3.7)", float(B[1] - lead), 0.0, 1e-18)
        C_.check(f"{lab} j={j}: N^-(2+jp) = 0", float(B[2]), 0.0, 1e-18)
        C_.check(f"{lab} j={j}: N^-(4+jp) = 0", float(B[4]), 0.0, 1e-15)
        C_.check(f"{lab} j={j}: g_j = A_j + B_j al^2", float(g - pred), 0.0, 1e-15)
        if j == 1:
            C_.check(f"{lab}: N^-(5+p) dressing = g1_4", float(B[5]/B[1] - g1_4(p, al)), 0.0, 1e-13)
    # second order in mu_1
    h = mp.mpf(10)**-12
    d0, _ = M.run(p, al); a, _ = M.run(p, al, mu={1: h}); b, _ = M.run(p, al, mu={1: -h})
    Q = toN([(x + y - 2*z)/h**2 for x, y, z in zip(a, b, d0)], p, al, 3*p)
    X11 = 2*Q[2]/(4*p**2)          # coefficient of eps_1^2 N^{-2-2p}  (c = 1: (1/2) mu1'' (2 zeta)^2 = 2 zeta^2 = eps_1^2/(2p^2))
    print(f"{lab} mu1^2: N^-(1+2p) {mp.nstr(Q[1], 3)}  N^-(3+2p) {mp.nstr(Q[3], 3)}  N^-(5+2p) {mp.nstr(Q[5], 3)};  eps1^2 coeff {mp.nstr(X11, 14)}"
          f"  pred (3p+1)/(2p) = {mp.nstr((3*p + 1)/(2*p), 14)}", flush=True)
    C_.check(f"{lab}: mu1^2 N^-(1+2p) = 0 (E3.7)", float(Q[1]), 0.0, 1e-9)
    C_.check(f"{lab}: mu1^2 N^-(3+2p) = 0", float(Q[3]), 0.0, 1e-8)
    C_.check(f"{lab}: mu1^2 N^-(5+2p) = 0", float(Q[5]), 0.0, 1e-6)
    C_.check(f"{lab}: eps1^2 N^-(2+2p) coefficient = (3p+1)/(2p)", float(X11 - (3*p + 1)/(2*p)), 0.0, 1e-9)
C_.finish()
