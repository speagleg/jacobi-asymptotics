"""Tiny reporting helpers for the certified suite (certified/*.py).  Pass/fail values are computed, never typed."""
from flint import arb, fmpq


def show(x, digits=30):
    """midpoint +/- radius, with the radius as an upper bound."""
    return f"{x.mid().str(digits, radius=False)} +/- {ub(x.rad())}"


def ub(r):
    """Decimal string, 3 significant digits rounded up, that is a rigorous upper bound for the ball r >= 0
    (works far below the double-precision range)."""
    m, rad, e = arb(r.upper()).mid_rad_10exp(6)
    v = int(m) + int(rad)
    e = int(e)
    if v <= 0:
        return "0"
    L = len(str(v))
    if L > 3:
        k = 10 ** (L - 3)
        v, e = -(-v // k), e + L - 3
    ds = str(v)
    return f"{ds[0]}.{ds[1:]}e{e + len(ds) - 1}" if len(ds) > 1 else f"{ds}e{e}"


def decimal_ball(s):
    """Exact rational value of a decimal string such as '-0.28946'."""
    neg = s.startswith("-")
    s = s.lstrip("+-")
    if "." in s:
        ip, fp = s.split(".")
    else:
        ip, fp = s, ""
    q = fmpq(int(ip + fp), 10 ** len(fp))
    return arb(-q if neg else q), len(fp)


def rounds_to(x, s):
    """Rigorous: True iff every point of the ball x is within half a unit of the last printed digit of s."""
    q, d = decimal_ball(s)
    half = arb(fmpq(1, 2 * 10 ** d))
    return bool((x - q).abs_upper() < half)


def truncates_to(x, s):
    """Rigorous: True iff every point of x lies in [s, s + 10^-d) (for s >= 0) or (s - 10^-d, s] (for s < 0)."""
    q, d = decimal_ball(s)
    u = arb(fmpq(1, 10 ** d))
    if s.startswith("-"):
        return bool(x.upper() <= q and x.lower() > q - u)
    return bool(x.lower() >= q and x.upper() < q + u)


class Checker:
    def __init__(self, title):
        self.title = title
        self.results = []
        print(f"== {title} ==")

    def check(self, name, ok, detail=""):
        ok = bool(ok)
        self.results.append((name, ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
        return ok

    def finish(self):
        bad = [n for n, ok in self.results if not ok]
        print(f"{self.title}: {len(self.results) - len(bad)}/{len(self.results)} checks passed")
        print("RESULT:", "PASS" if not bad else "FAIL (" + "; ".join(bad) + ")")
        return 0 if not bad else 1
