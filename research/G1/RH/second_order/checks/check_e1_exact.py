"""Plan 66 (E_p1.md, Lemma E1.5 and Theorem E1.6; exact computer algebra, sympy).

[0] Tricomi-Carlitz (alpha_W = 1) symmetric chain from WLXZ v1 (1.6), (1.9): monic y pi_N = pi_{N+1} + beta_N pi_{N-1} with
    beta_N = N/((N+a)(N+a-1)) (derived symbolically from the recurrence and the leading coefficients), = 1/(N+1) at a = 1.
[1] folded TC coefficients (SECOND Lemma 2.1): alpha_m = beta_{2m} + beta_{2m+1}, b_m^2 = beta_{2m-1} beta_{2m},
    g_m = beta_{2m+1} (chain), and the Darboux step (SECOND Lemma 2.2) for x*TC.
[2] the chain of x*TC: closed form gamma'_{2j+1}^2 = (2j+5)/((2j+2)(2j+3)), gamma'_{2j}^2 = j/((j+1)(2j+3)), verified as identities
    of rational functions against the three chain relations of x*TC (uniqueness remark after SECOND Lemma 2.2); hence the
    coefficients of x^2*TC.
[3] 1/n expansions (exact series): n b_n, n alpha_n, n g_n for TC (s = 3/2), x*TC (s = 5/2), x^2*TC (s = 7/2; b, alpha only),
    the symmetric chain N beta_N = 1 + (k0 + k1(-1)^N)/N + O(N^-2), and the differences used in Theorem E1.6 (via Proposition E1.4(iii)):
    alpha_n - alpha_{n-1} = -1/n^2 + O(n^-3), alpha_n(x v) - alpha_n(v) = -1/(2n^2) + O(n^-3).
All pass/fail values are computed (assertions)."""
import sympy as sp

n, N, j, m, a, y = sp.symbols('n N j m a y', positive=True)

# [0] monic recurrence from WLXZ (1.6): (N+1) f_{N+1} - (N+a) y f_N + f_{N-1} = 0, leading coeff gamma_N = Gamma(N+a)/(Gamma(a)Gamma(N+1))
gam = lambda K: sp.gamma(K + a) / (sp.gamma(a) * sp.gamma(K + 1))
# y pi_N = c1 pi_{N+1} + c2 pi_{N-1} with pi_K = f_K/gamma_K:  y f_N = ((N+1)/(N+a)) f_{N+1} + f_{N-1}/(N+a)
c1 = sp.simplify(sp.gammasimp((N + 1) / (N + a) * gam(N + 1) / gam(N)))
c2 = sp.simplify(sp.gammasimp(gam(N - 1) / (gam(N) * (N + a))))
assert sp.simplify(c1 - 1) == 0
beta_a = sp.simplify(c2)
assert sp.simplify(beta_a - N / ((N + a) * (N + a - 1))) == 0
beta = sp.simplify(beta_a.subs(a, 1))
print("[0] WLXZ (1.6),(1.9): monic coefficient of pi_{N+1} =", c1, "; beta_N =", beta_a, "; at alpha_W = 1:", beta)
assert sp.simplify(beta - 1 / (N + 1)) == 0
B = lambda K: sp.Integer(0) if K == 0 else sp.Rational(1, K + 1)   # beta_K for TC(1), beta_0 := 0


def first_order(expr):
    """expr ~ 1 + c/n + O(n^-2): return c, asserting the constant term 1."""
    t = sp.Symbol('t', positive=True)
    s_ = sp.series(expr.subs(n, 1 / t), t, 0, 2).removeO()
    c0 = s_.subs(t, 0)
    c1_ = sp.diff(s_, t).subs(t, 0)
    return sp.nsimplify(c0), sp.nsimplify(c1_)


def coeff2(expr):
    t = sp.Symbol('t', positive=True)
    s_ = sp.series(expr.subs(n, 1 / t), t, 0, 3).removeO()
    return [sp.nsimplify(s_.coeff(t, k)) for k in range(3)]


# [1] TC folded
al_TC = 1 / (2 * n + 1) + 1 / (2 * n + 2)          # alpha_n = beta_{2n} + beta_{2n+1}, n >= 1 (alpha_0 = 1/2)
b2_TC = 1 / ((2 * n) * (2 * n + 1))                # b_n^2 = beta_{2n-1} beta_{2n}
g_TC = 1 / (2 * n + 2)                             # g_n = beta_{2n+1}
# x*TC (Darboux, SECOND Lemma 2.2): alpha'_n = gamma_{2n+1}^2 + gamma_{2n+2}^2, b'_n^2 = gamma_{2n}^2 gamma_{2n+1}^2
al_xTC = 1 / (2 * n + 2) + 1 / (2 * n + 3)
b2_xTC = 1 / ((2 * n + 1) * (2 * n + 2))
print("[1] TC: alpha_n =", al_TC, " b_n^2 =", b2_TC, " g_n =", g_TC, "| x*TC: alpha'_n =", al_xTC, " b'_n^2 =", b2_xTC)
# check the folding numerically against beta for small n
for K in range(1, 8):
    assert al_TC.subs(n, K) == B(2 * K) + B(2 * K + 1)
    assert b2_TC.subs(n, K) == B(2 * K - 1) * B(2 * K)
    assert g_TC.subs(n, K) == B(2 * K + 1)
    assert al_xTC.subs(n, K) == B(2 * K + 1) + B(2 * K + 2)
    assert b2_xTC.subs(n, K) == B(2 * K) * B(2 * K + 1)
assert al_xTC.subs(n, 0) == B(1) + B(2)

# [2] chain of x*TC: closed form, verified as rational identities
godd = lambda J: sp.sympify(2 * J + 5) / ((2 * J + 2) * (2 * J + 3))      # gamma'_{2J+1}^2, J >= 0
gev = lambda J: sp.sympify(J) / ((J + 1) * (2 * J + 3))                   # gamma'_{2J}^2, J >= 0 (gamma'_0 = 0)
assert sp.simplify(godd(0) - al_xTC.subs(n, 0)) == 0                               # gamma'_1^2 = alpha'_0
assert sp.cancel(godd(m - 1) * gev(m) - b2_xTC.subs(n, m)) == 0                    # gamma'_{2m-1}^2 gamma'_{2m}^2 = b'_m^2
assert sp.cancel(gev(m) + godd(m) - al_xTC.subs(n, m)) == 0                        # gamma'_{2m}^2 + gamma'_{2m+1}^2 = alpha'_m
for J in range(0, 50):
    assert godd(J) > 0 and (J == 0 or gev(J) > 0)
print("[2] x*TC chain: gamma'_{2j+1}^2 = (2j+5)/((2j+2)(2j+3)), gamma'_{2j}^2 = j/((j+1)(2j+3)): identities verified (cancel)")
g_xTC = godd(n)                                    # g_n(x*TC) = gamma'_{2n+1}^2
al_x2TC = sp.cancel(godd(n) + gev(n + 1))          # alpha_n(x^2 TC) = gamma'_{2n+1}^2 + gamma'_{2n+2}^2
b2_x2TC = sp.cancel(gev(n) * godd(n))              # b_n^2(x^2 TC) = gamma'_{2n}^2 gamma'_{2n+1}^2
print("    x^2*TC: alpha_n =", sp.factor(al_x2TC), " b_n^2 =", sp.factor(b2_x2TC))

# [3] expansions
rows = []
for name, s_val, al_, b2_, g_ in [("TC", sp.Rational(3, 2), al_TC, b2_TC, g_TC),
                                   ("x*TC", sp.Rational(5, 2), al_xTC, b2_xTC, g_xTC),
                                   ("x^2*TC", sp.Rational(7, 2), al_x2TC, b2_x2TC, None)]:
    nb = sp.sqrt(n ** 2 * b2_)
    c0, d1 = first_order(2 * nb)
    c0a, ea = first_order(n * al_)
    assert c0 == 1 and c0a == 1
    assert d1 == -(s_val - 1) / 2, (name, d1)                                     # d1 = -(s-1)/2
    assert ea == -s_val / 2                                                         # n alpha_n = 1 - s/(2n)
    e1s = first_order((al_ / (2 * sp.sqrt(b2_))))[1]
    assert e1s == sp.Rational(-1, 2)                                               # alpha_n/(2 b_n) = 1 - 1/(2n)
    out = f"    {name} (s = {s_val}): 2 n b_n = 1 + ({d1})/n, n alpha_n = 1 + ({ea})/n, alpha_n/(2b_n) = 1 + ({e1s})/n"
    if g_ is not None:
        c0g, gg = first_order(2 * n * g_)
        assert c0g == 1
        out += f", 2 n g_n = 1 + ({gg})/n"
    print(out)
    rows.append((name, s_val, al_, b2_, g_))

# symmetric chains: N beta_N = 1 + (k0 + k1 (-1)^N)/N + O(N^-2), k0 = 1/2 - s, k1 = -3(s - 3/2) (P62 at p = 1)
t = sp.Symbol('t', positive=True)
for name, s_val, odd, even in [("TC", sp.Rational(3, 2), lambda K: 1 / (K + 1), lambda K: 1 / (K + 1)),
                               ("x*TC", sp.Rational(5, 2), lambda K: godd((K - 1) / 2), lambda K: gev(K / 2))]:
    co = sp.series((N * odd(N)).subs(N, 1 / t), t, 0, 2).removeO().coeff(t, 1)    # k0 - k1 (odd N)
    ce = sp.series((N * even(N)).subs(N, 1 / t), t, 0, 2).removeO().coeff(t, 1)   # k0 + k1 (even N)
    k0, k1 = sp.nsimplify((co + ce) / 2), sp.nsimplify((ce - co) / 2)
    assert k0 == sp.Rational(1, 2) - s_val and k1 == -3 * (s_val - sp.Rational(3, 2))
    print(f"    {name}: symmetric chain N beta_N = 1 + (k0 + k1(-1)^N)/N + O(N^-2) with k0 = {k0}, k1 = {k1}")

# differences used in Theorem E1.6 (second order)
for (name, s_val, al_, b2_, g_) in rows:
    d = coeff2(sp.cancel(al_ - al_.subs(n, n - 1)))
    assert d[0] == 0 and d[1] == 0 and d[2] == -1, (name, d)
print("[3] alpha_n - alpha_{n-1} = -1/n^2 + O(n^-3) for TC, x*TC, x^2*TC")
for (v, xv) in [(rows[0], rows[1]), (rows[1], rows[2])]:
    d = coeff2(sp.cancel(xv[2] - v[2]))
    assert d[0] == 0 and d[1] == 0 and d[2] == sp.Rational(-1, 2), d
    print(f"    alpha_n({xv[0]}) - alpha_n({v[0]}) = -1/(2n^2) + O(n^-3)")
for (name, s_val, al_, b2_, g_) in rows:
    d = coeff2(sp.cancel(b2_ - b2_.subs(n, n - 1)))
    assert d[0] == 0 and d[1] == 0 and d[2] == 0
print("    b_n^2 - b_{n-1}^2 = O(n^-3) for TC, x*TC, x^2*TC")
# the second-order constant of Theorem E1.6: (1/12) * (alpha_n - alpha_{n-1}) -> log(b^2 ratio) = -1/(12 n^2) -> b ratio 1 - 1/(24 n^2)
print("[3] Theorem E1.6 constant: eps = 1/12 (H(t) = 1 + 1/(12t) + ...), eps * (-1) / 2 =", sp.Rational(1, 12) * -1 / 2,
      "= -1/24")
print("ALL ASSERTIONS PASSED")
