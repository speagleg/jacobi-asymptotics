"""CERTIFIED (ball-arithmetic) enclosures of the Law-P constants.

    I(p) = (sqrt(pi)/2) Gamma(1/p + 1/2) / Gamma(1/p + 1),   c(p) = (1/4) (pi / (2 I(p)))^p,
    u_s(p) = 2 I(p) / pi = (4 c(p))^(-1/p),                  kappa_p = 3p/2 + log c(p),
    (log c)'(p) = log(pi/2) - log I(p) + (1/p) (psi(1/p + 1/2) - psi(1/p + 1))   (differentiated by hand),
    kappa_zeta  = -2 (log(pi/2) - (1 - log 2))   (smooth-zeta constant, research/G1/RH/zeta/RH_zeta_close.md).

p is passed as an exact rational (fmpq, int, or "a/b" string), so the only rounding is inside Arb's rigorous
gamma / digamma / log / pi; every returned ball contains the exact value.  `dlogc_series` recomputes (log c)'(p) by
Taylor-mode differentiation in arb_series (rigorous power-series arithmetic), independently of the hand derivative."""
from flint import arb, arb_series, ctx, fmpq


def _q(p):
    if isinstance(p, fmpq):
        return p
    if isinstance(p, str) and "/" in p:
        a, b = p.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(p)) if float(p) == int(p) else fmpq(*float(p).as_integer_ratio())


class _prec:
    def __init__(self, bits):
        self.bits = bits

    def __enter__(self):
        self.old = ctx.prec
        ctx.prec = self.bits

    def __exit__(self, *exc):
        ctx.prec = self.old


def I_p(p, prec_bits=256):
    with _prec(prec_bits):
        P = arb(_q(p))
        return arb.pi().sqrt() / 2 * arb.gamma(1 / P + arb(1) / 2) / arb.gamma(1 / P + 1)


def c_p(p, prec_bits=256):
    with _prec(prec_bits):
        P = arb(_q(p))
        return (arb.pi() / (2 * I_p(p, prec_bits))) ** P / 4


def u_s(p, prec_bits=256):
    with _prec(prec_bits):
        return 2 * I_p(p, prec_bits) / arb.pi()


def u_s_from_c(p, prec_bits=256):
    with _prec(prec_bits):
        return (4 * c_p(p, prec_bits)) ** (-1 / arb(_q(p)))


def kappa_p(p, prec_bits=256):
    with _prec(prec_bits):
        return 3 * arb(_q(p)) / 2 + c_p(p, prec_bits).log()


def dlogc(p, prec_bits=256):
    """(log c)'(p) from the hand-differentiated closed form (digamma)."""
    with _prec(prec_bits):
        P = arb(_q(p))
        r = 1 / P
        return ((arb.pi() / 2).log() - I_p(p, prec_bits).log()
                + (arb.digamma(r + arb(1) / 2) - arb.digamma(r + 1)) / P)


def dlogc_series(p, prec_bits=256):
    """(log c)'(p) by Taylor-mode differentiation: log c(p + t) as an arb_series in t, coefficient of t."""
    with _prec(prec_bits):
        P = arb(_q(p))
        t = arb_series([P, 1], prec=2)
        r = t.inv()
        half = arb(1) / 2
        logI = (arb.pi().sqrt() / 2).log() + (r + half).lgamma() - (r + 1).lgamma()
        logc = t * (arb.pi() / 2).log() - t * logI - arb(4).log()
        return logc.coeffs()[1]


def kappa_zeta(prec_bits=256):
    with _prec(prec_bits):
        return -2 * ((arb.pi() / 2).log() - (1 - arb(2).log()))
