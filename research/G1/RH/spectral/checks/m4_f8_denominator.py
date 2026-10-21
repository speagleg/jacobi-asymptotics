"""JZC M4 section 5: the hard-edge denominator prediction for f8. Runs the order-8 RH model computation (m4_rh4, KORD = 8) at
p = 3, alpha = 0 and p = 2, alpha = 0. Checks: f5 = f7 = 0; f8(3, 0) is the rational 1311857/632311515 with denominator
3^5 * 5 * (3p+2)^3 (5p+2) (7p+2) = 3^5 * 5 * 11^3 * 17 * 23; f8(2, 0) = 3899/2097152 (a power of 2 at p = 2)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["KORD"] = "8"; os.environ.setdefault("SHI", "56")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
C_ = Checks()
for p, num, den in ((3, 1311857, 632311515), (2, 3899, 2097152)):
    d, _ = M.run(mp.mpf(p), mp.mpf(0)); f = M.natural(d, mp.mpf(p), mp.mpf(0))
    print(f"p={p} alpha=0: f5 {mp.nstr(f[5], 3)}  f7 {mp.nstr(f[7], 3)}  f8 {mp.nstr(f[8], 30)}  vs {num}/{den} = {mp.nstr(mp.mpf(num)/den, 30)}")
    C_.check(f"p={p}: f5 = 0", float(f[5]), 0.0, 1e-30)
    C_.check(f"p={p}: f7 = 0", float(f[7]), 0.0, 1e-30)
    C_.check(f"p={p}: f8 = {num}/{den}", float((f[8] - mp.mpf(num)/den)*1e10), 0.0, 1e-20)
assert 632311515 == 3**5*5*11**3*17*23
C_.finish()
