"""CERTIFIED: the Law-P constants quoted in README.md, THEOREMS.md and Paper 1 (Table "tab:constants", Section 5 text),
and the smooth-zeta constant kappa of Paper 2 / research/G1/RH/zeta.

Method: Arb ball arithmetic at PREC bits; p is an exact rational; Gamma, digamma, log, pi are Arb's rigorous
functions (no truncation of our own, so no tail bound is needed).  Three kinds of check:
  * rounding claims ("the printed decimal is the correctly rounded / truncated value"): rigorous, decided by ball bounds;
  * identities between two closed forms (c(2) = pi^2/16, u_s = (4c)^(-1/p), kappa = -2 (log c)'(2), ...): the two
    enclosures must overlap with tiny radii.  Overlap is a certified bound |difference| <= sum of radii, not a proof of
    equality; the equalities themselves are exact algebra, re-checked symbolically with sympy where marked [exact].
Run (from the repo root): .venv/bin/python -I certified/c01_constants.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import sympy as sp  # noqa: E402
from flint import arb, ctx  # noqa: E402
from jacobi_asym.certify.constants import (I_p, c_p, u_s, u_s_from_c, kappa_p, dlogc, dlogc_series,  # noqa: E402
                                           kappa_zeta)
from jacobi_asym.certify.report import Checker, show, rounds_to, truncates_to  # noqa: E402

PREC = 256
TINY = arb(2) ** -200  # radius bound required of every identity check


def tight(*xs):
    return all(x.rad() < TINY for x in xs)


def main():
    ctx.prec = PREC
    C = Checker(f"c01 constants (Arb, {PREC} bits)")
    pi = arb.pi()

    print("-- exact special values")
    c1, c2 = c_p(1, PREC), c_p(2, PREC)
    print("  c(1) =", show(c1)); print("  c(2) =", show(c2), "  pi^2/16 =", show(pi ** 2 / 16))
    C.check("c(1) ball contains 1/2", c1.contains(arb(1) / 2) and tight(c1))
    C.check("c(2) ball overlaps pi^2/16", c2.overlaps(pi ** 2 / 16) and tight(c2))
    # exact symbolic re-check
    p = sp.Symbol("p", positive=True)
    Isym = sp.sqrt(sp.pi) / 2 * sp.gamma(1 / p + sp.Rational(1, 2)) / sp.gamma(1 / p + 1)
    csym = (sp.pi / (2 * Isym)) ** p / 4
    C.check("[exact] sympy: c(1) = 1/2", sp.simplify(sp.gammasimp(csym.subs(p, 1)) - sp.Rational(1, 2)) == 0)
    C.check("[exact] sympy: c(2) = pi^2/16", sp.simplify(sp.gammasimp(csym.subs(p, 2)) - sp.pi ** 2 / 16) == 0)
    C.check("[exact] sympy: c(1/2) = sqrt(6)/6, u_s(1/2) = 3/8",
            sp.simplify(sp.gammasimp(csym.subs(p, sp.Rational(1, 2))) - sp.sqrt(6) / 6) == 0
            and sp.simplify(sp.gammasimp(2 * Isym.subs(p, sp.Rational(1, 2)) / sp.pi) - sp.Rational(3, 8)) == 0)
    C.check("I(2) ball contains 1", I_p(2, PREC).contains(1))

    print("-- Paper 1 Table tab:constants: c(p), u_s = 2I(p)/pi, kappa_p = 3p/2 + log c(p) (correct rounding)")
    table = [("1/2", "0.408248", "0.3750", "-0.145880"), ("1", "0.500000", "0.5000", "0.806853"),
             ("3/2", "0.566272", "0.5798", "1.681320"), ("2", "0.616850", "0.6366", "2.516871"),
             ("3", "0.689213", "0.7132", "4.127795"), ("4", "0.738565", "0.7628", "5.696954"),
             ("6", "0.801586", "0.8235", "8.778837")]
    for ps, cq, uq, kq in table:
        c, u, u2, k = c_p(ps, PREC), u_s(ps, PREC), u_s_from_c(ps, PREC), kappa_p(ps, PREC)
        print(f"  p={ps:>3}: c = {show(c, 25)}\n         u_s = {show(u, 25)}\n         kappa_p = {show(k, 25)}")
        C.check(f"p={ps}: c(p) rounds to {cq}", rounds_to(c, cq))
        C.check(f"p={ps}: u_s rounds to {uq}", rounds_to(u, uq))
        C.check(f"p={ps}: kappa_p rounds to {kq}", rounds_to(k, kq))
        C.check(f"p={ps}: 2I(p)/pi overlaps (4c(p))^(-1/p)", u.overlaps(u2) and tight(u, u2))
    k2 = kappa_p(2, PREC)
    C.check("kappa_2 overlaps 3 + log(pi^2/16) (papers/paper1/checks/bs_check.py)",
            k2.overlaps(3 + (pi ** 2 / 16).log()) and tight(k2))
    C.check("Paper 1 Sec. 5 text: 3a/2 + log c(a) = 0.806853..., 2.516871..., 4.127795..., 5.696954... (rounded)",
            all(rounds_to(kappa_p(a, PREC), s) for a, s in [(1, "0.806853"), (2, "2.516871"), (3, "4.127795"),
                                                             (4, "5.696954")]))

    print("-- smooth-zeta constant kappa = -2(log(pi/2) - (1 - log 2))")
    kz = kappa_zeta(PREC)
    d_hand, d_ser = dlogc(2, PREC), dlogc_series(2, PREC)
    print("  kappa              =", show(kz))
    print("  (log c)'(2) [hand] =", show(d_hand))
    print("  (log c)'(2) [AD]   =", show(d_ser))
    C.check("(log c)'(2): hand-differentiated closed form overlaps arb_series Taylor-mode derivative",
            d_hand.overlaps(d_ser) and tight(d_hand, d_ser))
    C.check("kappa overlaps -2 (log c)'(2)", kz.overlaps(-2 * d_ser) and kz.overlaps(-2 * d_hand) and tight(kz))
    psi = arb.digamma(arb(3) / 2) - arb.digamma(arb(1))
    C.check("psi(3/2) - psi(1) overlaps 2 - 2 log 2 (RH_zeta_close.md)", psi.overlaps(2 - 2 * arb(2).log()))
    C.check("README / RH_zeta.md: kappa = -0.28946 (rounded)", rounds_to(kz, "-0.28946"))
    C.check("RH_zeta_close.md: kappa = -0.289459... (truncated)", truncates_to(kz, "-0.289459"))
    C.check("checks/check_z_kappa.out: kappa = -0.2894597717 (rounded)", rounds_to(kz, "-0.2894597717"))
    C.check("REVIEW_RHzeta.md: d/dp[p log J] at 2 = log(pi/2) - (1 - log 2) = 0.14473 (rounded)",
            rounds_to(d_hand, "0.14473"))
    return C.finish()


if __name__ == "__main__":
    sys.exit(main())
