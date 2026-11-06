"""Closed forms (CONJECTURE, identified by PSLQ, see D.md) vs the numerical K(p,s) of K_numeric.py outputs.
K(p,s) = Pi(p) - log G(z) - z(z-1)/2 log(p+2) + kappa_p z,  z = (s-1)/p,  kappa_p = 1/2 log(2pi(p+2)) + 3/2 log c(p).
Pi(1) = 1/4 - 5 log A + log pi + 5/12 log 2 - 3/8 log 3;  Pi(2) = 1/2 - 6 log A + 5/2 log pi - 89/24 log 2  (A = Glaisher)."""
import re, glob, mpmath as mp
mp.mp.dps = 40
L = mp.log; R = mp.mpf
def c_of_p(p):
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + R(1) / 2) / mp.gamma(1 / p + 1); return (mp.pi / (2 * I)) ** p / 4
Pi = {1: R(1) / 4 - 5 * L(mp.glaisher) + L(mp.pi) + R(5) / 12 * L(2) - R(3) / 8 * L(3),
      2: R(1) / 2 - 6 * L(mp.glaisher) + R(5) / 2 * L(mp.pi) - R(89) / 24 * L(2)}
def K(p, s):
    p = R(p); s = R(s); z = (s - 1) / p
    return Pi[int(p)] - L(mp.barnesg(z)) - z * (z - 1) / 2 * L(p + 2) + (L(2 * mp.pi * (p + 2)) / 2 + R(3) / 2 * L(c_of_p(p))) * z
for f in sorted(glob.glob('checks/K_p[12].out')) + ['checks/K_p2_quick.out']:
    for line in open(f):
        m = re.match(r'p=(\S+) s=(\S+) .*K=(\S+)\s', line)
        if m and float(m.group(1)) in (1.0, 2.0):
            p, s, Kn = float(m.group(1)), m.group(2), mp.mpf(m.group(3))
            print(f'{f}: p={p} s={s}  K_numeric - K_closed = {mp.nstr(Kn - K(p, s), 4)}')
