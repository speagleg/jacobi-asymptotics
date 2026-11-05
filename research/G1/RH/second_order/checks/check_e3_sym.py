"""Plan E3 (E3.md Theorem E3.1, p > 1): bookkeeping of the n^{-1-p} term on top of Theorem E2.1.
Inputs (all asserted/derived elsewhere, recomputed here where cheap):
  - E_plt1 Lemma E'.5 (p-generic algebra, lam a free symbol; check_e_plt1_sym.py): the residue of d/dlam Delta_1 at 4c is
    A_r^lin = c^2 p [[-(al+1), i(al+2)], [i al, al+1]], B_r^lin = 0, A_0^lin = 0;
  - E2 Theorem E2.1: R_1 = (A_0 + A_r)/n + R_1^(2)/n^2 + ..., n^p b_n/c = 1 + d1/n + d2/n^2 + ...;
  - E3 Lemma F.1': lam_n = 2 zeta(-p) n^{-p}.
With R_1 = (A_0 + A_r + lam A_r^lin)/n + R_1^(2)/n^2 the b-functional sqrt((Q1)_12 (Q1)_21)/c gains exactly c p lam / n at first
order in lam (cross terms lam/n^2 = O(n^{-2-p}), lam^2/n = O(n^{-1-2p}), both O(n^{-3}) for p > 1), so the n^{-1-p} coefficient
is kappa_p = 2 p c zeta(-p). This script recomputes that coefficient from A_r^lin symbolically and evaluates kappa_p."""
import sympy as sp
import mpmath as mp

I = sp.I
al, lam, eps = sp.symbols('alpha lam eps')
p, c = sp.symbols('p c', positive=True)
Arlin = c ** 2 * p * sp.Matrix([[-(al + 1), I * (al + 2)], [I * al, al + 1]])
P1 = sp.Matrix([[0, I * c], [-I * c, 0]])
A = sp.Matrix(2, 2, sp.symbols('a11 a12 a21 a22'))            # generic first-order matrix A_0 + A_r
R2 = sp.Matrix(2, 2, sp.symbols('r11 r12 r21 r22'))           # generic R_1^(2)
Q1 = P1 + eps * (A + lam * Arlin) + eps ** 2 * R2
b = sp.series(sp.sqrt(sp.expand(Q1[0, 1] * Q1[1, 0]) / c ** 2), eps, 0, 3).removeO()
lin = sp.simplify(sp.diff(b.coeff(eps, 1), lam).subs(lam, 0))
print("d/dlam of the 1/n coefficient of n^p b_n/c:", lin)
assert sp.simplify(lin - c * p) == 0
# lam enters the 1/n^2 coefficient only through cross terms (lam/n^2 = O(n^{-2-p}))
cross = sp.simplify(sp.diff(b.coeff(eps, 2), lam).subs(lam, 0))
print("d/dlam of the 1/n^2 coefficient (a cross term, contributes at n^{-2-p}):", sp.factor(cross))
print("kappa_p = 2 p c(p) zeta(-p):")
for pv in (1.25, 1.5, 1.75, 2, 3):
    pv = mp.mpf(pv)
    Ip = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / pv + 0.5) / mp.gamma(1 / pv + 1)
    cv = (mp.pi / (2 * Ip)) ** pv / 4
    print(f"  p = {mp.nstr(pv, 4)}: kappa_p = {mp.nstr(2 * pv * cv * mp.zeta(-pv), 12)}")
print("ALL ASSERTIONS PASSED")
