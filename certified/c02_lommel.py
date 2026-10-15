"""CERTIFIED: the (p, s) = (2, 2) Lommel closed form of Paper 2, Remark rem:pure-lommel (papers/paper2/sec_front.tex):
for sigma_{2,2} = sum_k k^{-2} delta_{k^{-2}} and n >= 1,
    b_n = pi^2 / ((4n+1) sqrt((4n-1)(4n+3))),    a_n = 2 pi^2 / ((4n+1)(4n+5)),    a_0 = pi^2/15,
and its consequences n^2 b_n / c(2) = 1 - 1/(2n) + O(n^-2), a_n/(2b_n) = 1 - 1/n + O(n^-2) (the 1/n coefficient -p/2).

Method.
 (i)  Moments m_j = zeta(2j + 2), j < 2N: Arb's rigorous zeta, cross-checked against the exact Bernoulli formula.
 (ii) a_n, b_n^2 for n < N by the Chebyshev algorithm in ball arithmetic (jacobi_asym.certify.moments.chebyshev);
      precision doubled until every ball has >= TARGET relative bits.  Every operation is a ball operation, so the
      balls contain the exact coefficients of sigma_{2,2}; no truncation occurs (the moments are exact values).
 (iii) Independent route for n <= NDET: b_n^2 = D_{n+1} D_{n-1} / D_n^2 with D_n = det(m_{i+j}) by arb_mat.det.
 (iv) Closed forms evaluated in Arb; for each n the computed and closed-form balls must overlap.  This certifies
      |computed - closed| <= (sum of radii) for every n < N; it does not by itself prove the identity for all n
      (that is the proof in the Remark).
 (v)  [exact] The 1/n coefficients and the sign of a_n/(2b_n) - 1 for ALL n >= 1, by exact algebra (sympy) on the
      closed form.
Run (from the repo root): .venv/bin/python -I certified/c02_lommel.py [N]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import sympy as sp  # noqa: E402
from flint import arb, ctx  # noqa: E402
from jacobi_asym.certify.moments import (zeta_moments, zeta_even_bernoulli, chebyshev, hankel_det,  # noqa: E402
                                         adaptive, rel_bits_ok)
from jacobi_asym.certify.report import Checker, show, ub  # noqa: E402

N_DEFAULT = 300
NDET = 12
TARGET = 128  # relative accuracy (bits) demanded of every computed coefficient


def closed_a(n):
    pi2 = arb.pi() ** 2
    return pi2 / 15 if n == 0 else 2 * pi2 / ((4 * n + 1) * (4 * n + 5))


def closed_b2(n):
    pi2 = arb.pi() ** 2
    return pi2 ** 2 / ((4 * n + 1) ** 2 * (4 * n - 1) * (4 * n + 3))


def run(N, C, verbose=True):
    (A, B), bits = adaptive(lambda: chebyshev(zeta_moments(2, 2, 2 * N), N), rel_bits_ok(TARGET))
    ctx.prec = bits
    print(f"  Chebyshev on 2N = {2 * N} moments: precision {bits} bits")
    mom = zeta_moments(2, 2, 2 * N)
    C.check(f"moments zeta(2j+2), j < {2 * N}: arb.zeta overlaps exact Bernoulli formula",
            all(mom[j].overlaps(zeta_even_bernoulli(j + 1)) for j in range(2 * N)))
    C.check("B_0 = m_0 overlaps pi^2/6", B[0].overlaps(arb.pi() ** 2 / 6))
    C.check("a_0 overlaps pi^2/15", A[0].overlaps(closed_a(0)))
    worst_rel_a = worst_rel_b = arb(0)
    ok_a = ok_b = True
    for n in range(1, N):
        ca, cb = closed_a(n), closed_b2(n)
        ok_a &= A[n].overlaps(ca)
        ok_b &= B[n].overlaps(cb)
        worst_rel_a = max(worst_rel_a, ((A[n] - ca) / ca).abs_upper())
        worst_rel_b = max(worst_rel_b, ((B[n] - cb) / cb).abs_upper())
        if verbose and (n <= 5 or n in (10, 50, 100) or n == N - 1):
            print(f"  n={n:4d}  a_n = {show(A[n], 22)}\n          closed {show(ca, 22)}")
            print(f"          b_n^2 = {show(B[n], 22)}\n          closed  {show(cb, 22)}")
    C.check(f"a_n overlaps 2pi^2/((4n+1)(4n+5)) for 1 <= n < {N}", ok_a,
            f"certified max |a_n/closed - 1| <= {ub(worst_rel_a)}")
    C.check(f"b_n^2 overlaps pi^4/((4n+1)^2(4n-1)(4n+3)) for 1 <= n < {N}", ok_b,
            f"certified max |b_n^2/closed - 1| <= {ub(worst_rel_b)}")
    # (iii) independent Hankel-determinant route
    D = [hankel_det(mom, n) for n in range(NDET + 2)]
    ok = all((D[n + 1] * D[n - 1] / D[n] ** 2).overlaps(B[n]) for n in range(1, NDET + 1))
    C.check(f"Hankel route: D_(n+1) D_(n-1)/D_n^2 overlaps Chebyshev b_n^2, n <= {NDET}", ok,
            f"D_{NDET + 1} = {show(D[NDET + 1], 12)}")
    return A, B


def exact_algebra(C):
    n = sp.Symbol("n", positive=True)
    b = sp.pi ** 2 / ((4 * n + 1) * sp.sqrt((4 * n - 1) * (4 * n + 3)))
    a = 2 * sp.pi ** 2 / ((4 * n + 1) * (4 * n + 5))
    r1 = sp.simplify(n ** 2 * b / (sp.pi ** 2 / 16))
    r2 = sp.simplify(a / (2 * b))
    e = sp.Symbol("e", positive=True)  # e = 1/n
    s1 = sp.series(r1.subs(n, 1 / e), e, 0, 2).removeO()
    s2 = sp.series(r2.subs(n, 1 / e), e, 0, 2).removeO()
    print(f"  [exact] n^2 b_n/c(2) = {r1} = {sp.expand(s1)} + O(n^-2)  (e = 1/n)")
    print(f"  [exact] a_n/(2 b_n)  = {r2} = {sp.expand(s2)} + O(n^-2)")
    C.check("[exact] n^2 b_n / c(2) = 1 - 1/(2n) + O(n^-2)", sp.expand(s1 - (1 - e / 2)) == 0)
    C.check("[exact] a_n/(2b_n) = 1 - 1/n + O(n^-2), i.e. 1/n coefficient -p/2 = -1", sp.expand(s2 - (1 - e)) == 0)
    gap = sp.expand((4 * n + 5) ** 2 - (4 * n - 1) * (4 * n + 3))
    C.check("[exact] a_n/(2b_n) < 1 for every n >= 1: (4n+5)^2 - (4n-1)(4n+3) = 32n + 28 > 0", gap == 32 * n + 28)
    gap2 = sp.expand(((4 * n + 1) ** 2 * (4 * n - 1) * (4 * n + 3)) - (16 * n ** 2) ** 2)
    print(f"  [exact] (4n+1)^2(4n-1)(4n+3) - (4n)^4 = {gap2}")
    m = sp.Symbol("m")
    shifted = sp.Poly(sp.expand(gap2.subs(n, m + 1)), m)
    print(f"  [exact] same with n = m + 1: {shifted.as_expr()}")
    C.check("[exact] n^2 b_n < c(2) for every n >= 1 (n = m+1: all coefficients positive)",
            all(cf > 0 for cf in shifted.all_coeffs()))


def main(N=N_DEFAULT):
    C = Checker(f"c02 Lommel closed form for sigma_(2,2), n < {N}")
    old = ctx.prec
    try:
        run(N, C)
    finally:
        ctx.prec = old
    exact_algebra(C)
    return C.finish()


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else N_DEFAULT))
