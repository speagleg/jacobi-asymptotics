"""CERTIFIED: Hankel determinants of zeta values H_n(a, b) = det_{1<=i,j<=n} zeta(a(i+j)+b) (Paper 1, Corollary
cor:zeta), and their agreement with the Baricz-Stampach closed forms for a = 2, b in {-2, 0, 2} (Paper 1, Remark rem:bs;
papers/paper1/checks/bs_check.py, which is the NUMERICAL mpmath version of this check).

Method.  H_n(a, b) is the Hankel determinant D_n of sigma_{a, 2a+b} = sum_k k^{-(2a+b)} delta_{k^{-a}}, whose moments
are zeta(2a + b + a j).  Moments: Arb's rigorous zeta (exact rational arguments).  Determinants: arb_mat.det (ball
Gaussian elimination, rigorous), precision doubled until every determinant has >= TARGET relative bits.
Closed forms (nu = 1/2): det H^(l)_n(nu) = 2^{-2n(n+l)} prod_{k=1}^{2n+l-1} (nu+k)^{k-2n-l} (l = 0, 1) and
2^{-2n(n+2)} (n+1)(n+nu+1) prod_{k=1}^{2n+1} (nu+k)^{k-2n-2} (l = 2), times pi^{2 sum_i (2i+l-1)} (rows and columns
rescaled, zeta(2m) = pi^{2m} sigma_{2m}(1/2)); these are exact rationals times a power of pi.  Overlap of the two
balls certifies |direct - closed| <= sum of radii for each listed n; it is not a proof of the closed form for all n.
The last block compares (log H_n + a n^2 log n)/n^2 with kappa_a = 3a/2 + log c(a): the values are enclosures, but
the comparison only ILLUSTRATES the o(n^2) theorem (no finite n certifies a limit).
Run (from the repo root): .venv/bin/python -I certified/c03_zeta_hankel.py [NMAX]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from flint import arb, ctx, fmpq  # noqa: E402
from jacobi_asym.certify.moments import zeta_moments, hankel_det, adaptive, rel_bits_ok  # noqa: E402
from jacobi_asym.certify.constants import kappa_p  # noqa: E402
from jacobi_asym.certify.report import Checker, show, ub  # noqa: E402

NMAX_DEFAULT = 30
TARGET = 100
CASES = [(fmpq(1), fmpq(0)), (fmpq(1), fmpq(1)), (fmpq(3, 2), fmpq(0)), (fmpq(2), fmpq(-2)), (fmpq(2), fmpq(0)),
         (fmpq(2), fmpq(2)), (fmpq(3), fmpq(0))]


def zeta_dets(a, b, nmax):
    """[H_1, ..., H_nmax] for H_n = det zeta(a(i+j)+b), via D_n of sigma_{a, 2a+b}."""
    mom = zeta_moments(a, 2 * a + b, 2 * nmax)
    return [hankel_det(mom, n) for n in range(1, nmax + 1)]


def bs_closed_rational(n, l):
    """Exact rational factor of the Baricz-Stampach closed form at nu = 1/2; zeta det = this * pi^(2 E)."""
    nu = fmpq(1, 2)
    if l in (0, 1):
        r = fmpq(1, 2 ** (2 * n * (n + l)))
        top = 2 * n + l - 1
        ex = lambda k: k - 2 * n - l  # noqa: E731
    else:
        r = fmpq(1, 2 ** (2 * n * (n + 2))) * (n + 1) * (n + nu + 1)
        top = 2 * n + 1
        ex = lambda k: k - 2 * n - 2  # noqa: E731
    for k in range(1, top + 1):
        e = ex(k)
        r *= (nu + k) ** e if e >= 0 else 1 / (nu + k) ** (-e)
    E = sum(2 * i + l - 1 for i in range(1, n + 1))
    return r, 2 * E


def log_bs_closed(n, l):
    """log of the closed form, as a ball: sum of exact-rational logs (cheap for large n)."""
    nu = arb(1) / 2
    if l in (0, 1):
        v = -2 * n * (n + l) * arb(2).log()
        v += sum(((k - 2 * n - l) * (nu + k).log() for k in range(1, 2 * n + l)), arb(0))
    else:
        v = -2 * n * (n + 2) * arb(2).log() + arb(n + 1).log() + (n + nu + 1).log()
        v += sum(((k - 2 * n - 2) * (nu + k).log() for k in range(1, 2 * n + 2)), arb(0))
    return v + 2 * sum(2 * i + l - 1 for i in range(1, n + 1)) * arb.pi().log()


def main(nmax=NMAX_DEFAULT):
    C = Checker(f"c03 zeta Hankel determinants, n <= {nmax}")
    old = ctx.prec
    try:
        dets = {}
        for a, b in CASES:
            D, bits = adaptive(lambda: zeta_dets(a, b, nmax), rel_bits_ok(TARGET))
            dets[(a, b)] = (D, bits)
            ctx.prec = bits
            print(f"-- a = {a}, b = {b}: {bits} bits")
            for n in sorted({1, 2, 3, 5, 8, 12, nmax} & set(range(1, nmax + 1))):
                print(f"   H_{n:<3d} = {show(D[n - 1], 25)}")
            C.check(f"a={a}, b={b}: all H_n (n <= {nmax}) enclosed with >= {TARGET} relative bits and > 0",
                    all(d > 0 for d in D))
        print("-- Baricz-Stampach closed forms, a = 2 (b = 2l - 2)")
        for l in (0, 1, 2):
            D, bits = dets[(fmpq(2), fmpq(2 * l - 2))]
            ctx.prec = bits
            ok, worst = True, arb(0)
            for n in range(1, nmax + 1):
                r, e = bs_closed_rational(n, l)
                cl = arb(r) * arb.pi() ** e
                ok &= D[n - 1].overlaps(cl)
                worst = max(worst, ((D[n - 1] - cl) / cl).abs_upper())
            print(f"   l={l}: H_{nmax} closed = {show(arb(r) * arb.pi() ** e, 25)}")
            C.check(f"a=2, b={2 * l - 2}: direct det overlaps closed form for 1 <= n <= {nmax}", ok,
                    f"certified max rel. difference <= {ub(worst)}")
        print("-- ILLUSTRATION ONLY (not a certified claim): (log H_n + a n^2 log n)/n^2 vs kappa_a = 3a/2 + log c(a)")
        ctx.prec = 256
        for a, b in CASES:
            D, _ = dets[(a, b)]
            k = kappa_p(a, 256)
            A = arb(a)
            vals = [(n, (D[n - 1].log() + A * n * n * arb(n).log()) / (n * n)) for n in (5, 10, nmax)]
            print(f"   a={a}, b={b}: kappa_a = {k.str(8, radius=False)};  "
                  + ";  ".join(f"n={n}: {v.str(8, radius=False)}" for n, v in vals))
        print("   a=2 via the closed forms, log evaluated as a ball sum (enclosures of the closed-form values):")
        for l in (0, 1, 2):
            out = []
            for n in (100, 1000, 10000):
                v = (log_bs_closed(n, l) + 2 * n * n * arb(n).log()) / (n * n)
                out.append(f"n={n}: {v.str(10, radius=False)}")
            print(f"   l={l}: kappa_2 = {kappa_p(2, 256).str(10, radius=False)};  " + ";  ".join(out))
    finally:
        ctx.prec = old
    return C.finish()


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else NMAX_DEFAULT))
