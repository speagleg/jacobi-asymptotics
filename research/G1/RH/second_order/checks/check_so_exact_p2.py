"""Plan 62 (exact, sympy): p = 2, s in {2, 4, 6, 8, 10}.

sigma_{2,2} is the Lommel case (papers/paper2 Remark rem:pure-lommel, from VA section 3 and DLMF; RH/CITATIONS.md
entries VA and DLMF-Lommel): after x -> x/pi^2 (atoms (k pi)^{-2}; c(2) becomes 1/16) its symmetric chain is
gamma_N^2 = 1/((2N+1)(2N+3)), N >= 1, gamma_0 = 0.  Chain relations (SECOND.md Lemma 2.1):
  alpha_0 = gamma_1^2,  b_m^2 = gamma_{2m-1}^2 gamma_{2m}^2,  alpha_m = gamma_{2m}^2 + gamma_{2m+1}^2  (m >= 1);
Darboux (Lemma 2.2): x sigma has alpha'_m = gamma_{2m+1}^2 + gamma_{2m+2}^2, b'_m^2 = gamma_{2m}^2 gamma_{2m+1}^2.
Given (alpha', b'), the chain with gamma'_0 = 0 is unique (solve recursively), so a closed form that satisfies the
chain relations identically in m IS the chain of x sigma.  This script (1) verifies the closed forms for s = 4, 6, 8
as rational identities in m, (2) expands n^2 b_n/c - 1, alpha_{n-1}/(2b_n) - 1 (repo pairing), alpha_n/(2b_n) - 1
(standard pairing) in 1/n for s = 2, ..., 10, and (3) the chain coefficients k0, k1."""
import sympy as sp

m, n, u = sp.symbols('m n u', positive=True)
CH = {
    2: (1 / ((4*m + 1)*(4*m + 3)), 1 / ((4*m + 3)*(4*m + 5))),
    4: (m*(2*m + 1)/((m + 1)*(2*m + 3)*(4*m + 3)*(4*m + 5)),
        (m + 2)*(2*m + 5)/((m + 1)*(2*m + 3)*(4*m + 5)*(4*m + 7))),
    6: (m*(2*m + 1)*(4*m**2 + 6*m - 1)/((m + 1)*(2*m + 3)*(4*m + 5)*(4*m + 7)*(4*m**2 + 14*m + 9)),
        (m + 3)*(2*m + 7)*(4*m**2 + 22*m + 27)/((m + 2)*(2*m + 5)*(4*m + 7)*(4*m + 9)*(4*m**2 + 14*m + 9))),
    8: (m*(2*m + 1)*(4*m**2 + 22*m + 27)*(16*m**4 + 80*m**3 + 80*m**2 - 50*m + 9)
        / ((m + 2)*(2*m + 5)*(4*m + 7)*(4*m + 9)*(4*m**2 + 14*m + 9)*(16*m**4 + 144*m**3 + 416*m**2 + 414*m + 135)),
        (m + 4)*(2*m + 9)*(4*m**2 + 14*m + 9)*(16*m**4 + 208*m**3 + 944*m**2 + 1742*m + 1125)
        / ((m + 2)*(2*m + 5)*(4*m + 9)*(4*m + 11)*(4*m**2 + 22*m + 27)*(16*m**4 + 144*m**3 + 416*m**2 + 414*m + 135))),
}
# ge(m) = gamma_{2m}^2 (m >= 1), go(m) = gamma_{2m+1}^2 (m >= 0)


def darboux(s):
    ge, go = CH[s]
    al = go + ge.subs(m, m + 1)                 # alpha'_m, m >= 0
    b2 = ge * go                                # b'_m^2, m >= 1
    return al, b2


print("(1) closed forms of the chains satisfy the chain relations of x * sigma_{2,s-2}:")
for s in (4, 6, 8):
    al, b2 = darboux(s - 2)
    ge, go = CH[s]
    r0 = sp.simplify(go.subs(m, 0) - al.subs(m, 0))
    r1 = sp.cancel(go.subs(m, m - 1) * ge - b2)
    r2 = sp.cancel(ge + go - al)
    print(f"   s = {s}: gamma_1^2 - alpha_0 = {r0};  gamma_(2m-1)^2 gamma_(2m)^2 - b_m^2 = {r1};"
          f"  gamma_(2m)^2 + gamma_(2m+1)^2 - alpha_m = {r2}   (positivity: numerators/denominators > 0 for m >= 1)")


def ser(expr, order=4):
    e = sp.cancel(expr.subs(n, 1 / u))
    return sp.expand(sp.series(e, u, 0, order).removeO())


def sqrt_ser(expr2, order=4):
    """series in u of sqrt(expr2) where expr2 = 1 + O(u) after normalization"""
    s2 = ser(expr2, order)
    return sp.expand(sp.series(sp.sqrt(s2), u, 0, order).removeO())


print("\n(2) expansions in u = 1/n  (c = 1/16 after x -> x/pi^2):")
print("    s | n^2 b_n/c - 1 | alpha_{n-1}/(2b_n) - 1 (repo) | alpha_n/(2b_n) - 1 (standard) | conj d1 = -(s-1)/2")
rows = []
for s in (2, 4, 6, 8, 10):
    if s <= 8:
        ge, go = CH[s]
        b2 = (go.subs(m, n - 1) * ge.subs(m, n))
        a_rep = ge.subs(m, n - 1) + go.subs(m, n - 1) if s > 2 else go.subs(m, n - 1) + ge.subs(m, n - 1)
        a_std = ge.subs(m, n) + go.subs(m, n)
    else:
        al, b2m = darboux(8)
        b2 = b2m.subs(m, n); a_rep = al.subs(m, n - 1); a_std = al.subs(m, n)
    B = sqrt_ser(256 * n**4 * b2)                 # n^2 b_n / c with c = 1/16
    bb = sqrt_ser(b2 * 256 * n**4) / (16 * n**2)  # b_n as series times n^-2
    rep = ser(a_rep * 16 * n**2 / 2) * sp.series(1 / B, u, 0, 4).removeO()
    std = ser(a_std * 16 * n**2 / 2) * sp.series(1 / B, u, 0, 4).removeO()
    rep = sp.expand(sp.series(rep, u, 0, 4).removeO()); std = sp.expand(sp.series(std, u, 0, 4).removeO())
    print(f"   {s:2d} | {B - 1} | {rep - 1} | {std - 1} | {sp.Rational(-(s - 1), 2)}")
    assert sp.expand(B - 1).coeff(u, 1) == sp.Rational(-(s - 1), 2)
    assert sp.expand(rep - 1).coeff(u, 1) == 1 and sp.expand(std - 1).coeff(u, 1) == -1

print("\n(3) chain: gamma_N^2 * 4 N^2 - 1 = (k0 + k1 (-1)^N)/N + ...  (conj k0 = -(s-1) - p/2 = -s, k1 = -(p+2)(2s-2-p)/(2p) = -2(s-2))")
N = sp.symbols('N', positive=True)
for s in (2, 4, 6, 8):
    ge, go = CH[s]
    ev = sp.expand(sp.series(sp.cancel((ge.subs(m, N / 2) * 4 * N**2).subs(N, 1 / u)), u, 0, 2).removeO()).coeff(u, 1)
    od = sp.expand(sp.series(sp.cancel((go.subs(m, (N - 1) / 2) * 4 * N**2).subs(N, 1 / u)), u, 0, 2).removeO()).coeff(u, 1)
    k0, k1 = (ev + od) / 2, (ev - od) / 2
    print(f"   s = {s}: k0 = {k0}, k1 = {k1}")
    assert k0 == -s and k1 == -2 * (s - 2)
print("\nall assertions passed")
