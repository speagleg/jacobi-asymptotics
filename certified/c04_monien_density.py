"""CERTIFIED (pointwise): at p = 1, Monien's limiting zero density (arXiv:0901.1883 Thm 3.1, as quoted in
research/G2/CITATIONS.md (M)) equals the density of mu*_u from Theorem B*, rho*(u) = I_{min(1, u^{-p}/(4c(p)))}(1/p + 1/2,
1/2) (regularized incomplete beta), at the sample points of papers/paper1/checks/monien_check.py (the NUMERICAL mpmath
version of this check).

Method: x is an exact rational, so the branch min(1, 1/(2x)) (4c(1) = 2) is decided exactly; Monien's
2/pi (atan(1/r) - r/(2x)), r = sqrt(2x - 1), and the regularized incomplete beta (arb.beta_lower, regularized) are Arb
ball evaluations.  Overlap certifies |Monien - rho*| <= sum of radii at each listed point; equality for all x is the
identity proved in Paper 1 (not certified here).  The total-mass check of monien_check.py (an improper integral) is
NOT certified: it would need a rigorous quadrature with an explicit tail bound.
Run (from the repo root): .venv/bin/python -I certified/c04_monien_density.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from flint import arb, ctx, fmpq  # noqa: E402
from jacobi_asym.certify.constants import c_p  # noqa: E402
from jacobi_asym.certify.report import Checker, show, ub  # noqa: E402

PREC = 256
POINTS = ["1/10", "1/2", "5001/10000", "3/5", "3/4", "1", "2", "5", "10", "100", "10000"]


def monien(x):
    if x <= fmpq(1, 2):
        return arb(1)
    X = arb(x)
    r = (2 * X - 1).sqrt()
    return 2 / arb.pi() * ((1 / r).atan() - r / (2 * X))


def rho_star_p1(x):
    V = fmpq(1) / (2 * x)            # u^{-1}/(4c(1)), 4c(1) = 2 exactly
    if V >= 1:
        return arb(1)
    return arb(V).beta_lower(arb(3) / 2, arb(1) / 2, regularized=True)


def main():
    ctx.prec = PREC
    C = Checker(f"c04 Monien density vs rho* at p = 1 (Arb, {PREC} bits)")
    C.check("4c(1) ball contains 2 (branch point of min(1, 1/(2u)))", (4 * c_p(1, PREC)).contains(2))
    worst = arb(0)
    ok = True
    for s in POINTS:
        a, b = (s.split("/") + ["1"])[:2]
        x = fmpq(int(a), int(b))
        m, r = monien(x), rho_star_p1(x)
        ok &= m.overlaps(r)
        worst = max(worst, (m - r).abs_upper())
        print(f"  x = {s:>10}: Monien {show(m, 22)}\n                 rho*   {show(r, 22)}")
    C.check(f"Monien density overlaps rho*(x) at all {len(POINTS)} sample points", ok,
            f"certified max |diff| <= {ub(worst)}")
    return C.finish()


if __name__ == "__main__":
    sys.exit(main())
