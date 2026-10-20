"""Plan E3 (E3.md Lemma E3.7, all orders): exact residues of Delta_1^mu = G_mu Delta_1^mod G_mu^{-1} (Lemma E3.4(iii)).

Inputs: the gauge G_mu = P0 exp(-Rr M sigma3/2) P0^{-1} of Lemma E3.4(ii), written as
    G = T [[cosh h, -w S], [-(4c + w) S, cosh h]] T^{-1},  h = Rr M/2,  S = sinh(h)/Rr,  w = z - 4c,
(an entire function of z: cosh h and S are even in Rr, Rr^2 = z(z - 4c) = w(4c + w)), and the model Laurent data of
Delta_1^mod (E_pgt1 Lemma E.5, as asserted in check_e_plt1_sym.py):
    Delta_1^mod = B_r/w^2 + A_r/w + O(1) at 4c,   A_0/z + O(1) at 0.
M is an ARBITRARY analytic function (any polynomial tilt): only M(4c) =: M4, M'(4c) =: M4p and M(0) =: M0 enter.
Asserted (all orders in mu, no truncation in M):
  det G(4c) = 1;  G(4c) B_r G(4c)^{-1} = B_r;  G(0) A_0 G(0)^{-1} = A_0 (G(0) commutes with A_0 -- structural, F2 of
  REVIEW_PlanE3_B);  the b-functional e = i(A21 - A12)/(2c) of Res_0 + Res_{4c} shifts by exactly c p M(4c);
  the full shift Res_{4c} - A_r = M4 c^2 p [[M4 c - a - 1, -i(M4 c - a - 2)], [-i(M4 c - a), -(M4 c - a - 1)]] (quadratic
  in M4, symmetric off-diagonal part cancels in the b-functional);
  Q_k(4c) = c^{k-1} k binom(2k, k)/2 (k < 40), hence c p M_{mu_n}(4c) has weighted-degree-k part binom(2k,k) p c^k zeta(-kp).
Origin: reviewer B's gauge.py (REVIEW_PlanE3_B §1.5), adopted with assertions added."""
import sympy as sp
from math import comb

I = sp.I
al, p, c = sp.symbols('alpha p c', positive=True)
M4, M4p, M0, w = sp.symbols('M4 M4p M0 w')
T = sp.Matrix([[1, 1], [I, -I]]) / sp.sqrt(2)
Ti = T.inv()
Ar = (c / 48) * sp.Matrix([[12 * al**2 * p + 24 * al * p + 11 * p + 2, -I * (12 * al**2 * p + 48 * al * p + 49 * p + 2)],
                           [-I * (12 * al**2 * p + p + 2), -(12 * al**2 * p + 24 * al * p + 11 * p + 2)]])
Br = (5 * c**2 * p / 12) * sp.Matrix([[1, -I], [-I, -1]])
A0 = c * (p + 2) * (4 * al**2 - 1) / 16 * sp.Matrix([[1, I], [I, -1]])

# G near 4c to O(w^2): H = h^2 = Rr^2 M^2/4 = O(w), so three terms of each series suffice for w^0, w^1
Mz = M4 + M4p * w
H = (4 * c + w) * w * Mz**2 / 4
ch = sum(H**m / sp.factorial(2 * m) for m in range(3))
S = Mz / 2 * sum(H**m / sp.factorial(2 * m + 1) for m in range(3))
G = T * sp.Matrix([[ch, -w * S], [-(4 * c + w) * S, ch]]) * Ti
G = G.applyfunc(lambda e: sp.expand(sp.series(e, w, 0, 2).removeO()))
G0 = G.applyfunc(lambda e: e.coeff(w, 0))
G1 = G.applyfunc(lambda e: e.coeff(w, 1))
assert sp.simplify(G0.det() - 1) == 0, "det G(4c) = 1"
G0i = G0.inv()
Gi1 = -G0i * G1 * G0i
Res = (G0 * Ar * G0i + G1 * Br * G0i + G0 * Br * Gi1).applyfunc(sp.expand)
assert all(sp.simplify(e) == 0 for e in (G0 * Br * G0i - Br)), "B_r unchanged"

# at z = 0: Rr = 0, h = 0, S(0) = M0/2, G(0) = T [[1, 4c M0/2], [0, 1]] T^{-1}
Gz0 = T * sp.Matrix([[1, 2 * c * M0], [0, 1]]) * Ti
assert all(sp.simplify(e) == 0 for e in (Gz0 * A0 - A0 * Gz0)), "G(0) commutes with A_0 (structural)"

e = sp.expand(I * ((A0 + Res)[1, 0] - (A0 + Res)[0, 1]) / (2 * c))
e0 = sp.expand(I * ((A0 + Ar)[1, 0] - (A0 + Ar)[0, 1]) / (2 * c))
s = sp.Symbol('s')
assert sp.simplify(e0.subs(al, (s - 1 - p) / p) + (s - 1) / 2) == 0, "d1 = -(s-1)/2"
assert sp.simplify(e - e0 - c * p * M4) == 0, "e(M) - e(0) = c p M(4c), all orders"
print("e(M) - e(0) =", sp.factor(sp.simplify(e - e0)), " (asserted = c p M(4c); M4p and M0 drop out)")
shift = M4 * c**2 * p * sp.Matrix([[M4 * c - al - 1, -I * (M4 * c - al - 2)], [-I * (M4 * c - al), -(M4 * c - al - 1)]])
assert all(sp.simplify(x) == 0 for x in (Res - Ar - shift)), "full residue shift"
print("Res_4c - A_r =", (Res - Ar).applyfunc(sp.factor), " (asserted)")

for k in range(1, 40):
    assert sum(4**(k - 1 - j) * comb(2 * j, j) for j in range(k)) * 2 == k * comb(2 * k, k)
print("Q_k(4c) = c^(k-1) k binom(2k,k)/2 for k < 40 (asserted); eps_k = binom(2k,k) p c^k zeta(-kp) for all k")
print("ALL ASSERTIONS PASSED")
