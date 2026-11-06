"""Rule R independent check of Theorem A (CG.md) at (p,s) not used by the author.

Independent of checks/cglib.py: lambda_m(0) = 1/(H_m^{-1})_{00}, H_m = [zeta(s+(i+j)p)]_{i,j<m} (Hankel moment
matrix), solved in Arb ball arithmetic (python-flint).  The ball radius of each lambda_m is printed, so the
finite-m values are enclosures (the moments zeta(s+jp) are Arb-enclosed by flint).  The asymptotic statement
(m -> infinity) is of course only NUMERICAL.  Precision: run at prec and 2*prec bits and compare.

Usage: rev_lambda.py p s mmax prec_bits
"""
import sys
from flint import arb, arb_mat, ctx


def q(x):
    from fractions import Fraction
    f = Fraction(x)
    return arb(f.numerator) / f.denominator


def const(p, s):
    p = q(p); s = q(s)
    I = arb.pi().sqrt() / 2 * (1 / p + arb(0.5)).gamma() / (1 / p + 1).gamma()
    c = (arb.pi() / (2 * I)) ** p / 4
    z = (s - 1) / p
    return z.gamma() * (z + 1).gamma() / p * (c * (p + 2) ** 2) ** z, (p + 2) * z


def lambdas(p, s, ms, prec):
    ctx.prec = prec
    P = q(p); S = q(s)
    M = max(ms)
    mom = [(S + j * P).zeta() for j in range(2 * M)]
    out = {}
    for m in ms:
        H = arb_mat(m, m, [mom[i + j] for i in range(m) for j in range(m)])
        e0 = arb_mat(m, 1, [1] + [0] * (m - 1))
        x = H.solve(e0)
        out[m] = 1 / x[0, 0]
    return out


if __name__ == "__main__":
    p, s, mmax, prec = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    step = int(sys.argv[5]) if len(sys.argv) > 5 else 10
    ms = list(range(step, mmax + 1, step))
    A = lambdas(p, s, ms, prec)
    B = lambdas(p, s, ms, 2 * prec)
    ctx.prec = 2 * prec
    C, E = const(p, s)
    print(f"p={p} s={s} E={E.mid().str(15)} C={C.mid().str(20)}  prec={prec}/{2*prec} bits")
    r = {}
    for m in ms:
        lam = B[m]
        r[m] = lam * arb(m) ** E / C
        rad = lam.rad() / abs(lam.mid())
        diff = abs((A[m] - B[m]).mid()) / abs(B[m].mid()) if A[m].is_finite() else float('nan')
        print(f"m={m:4d} r_m={r[m].mid().str(18)}  m(r_m-1)={(m*(r[m]-1)).mid().str(10)}  "
              f"relrad={arb(rad).str(3, radius=False)}  |lam(prec)-lam(2prec)|/lam={arb(diff).str(3, radius=False)}")
    # Richardson in 1/m on the last points (r_m = 1 + c1/m + c2/m^2 + ...)
    import itertools
    pts = ms[-4:]
    for order in (1, 2, 3):
        use = ms[-(order + 1):]
        # solve for limit with polynomial in 1/m of degree order
        from flint import arb_mat as AM
        rows = []
        rhs = []
        for m in use:
            rows += [arb(1)] + [arb(1) / arb(m) ** k for k in range(1, order + 1)]
            rhs.append(r[m])
        Amat = AM(order + 1, order + 1, rows)
        sol = Amat.solve(AM(order + 1, 1, rhs))
        print(f"Richardson order {order} on m={use}: limit-1 = {(sol[0,0]-1).mid().str(5)}, c1 = {sol[1,0].mid().str(8)}")
