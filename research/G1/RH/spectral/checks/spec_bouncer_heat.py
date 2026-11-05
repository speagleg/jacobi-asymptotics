"""SPEC §6 (NUMERICAL): heat trace of the quantum bouncer H = -d^2/dx^2 + x on (0, inf), Dirichlet at 0:
  Theta(t) = sum_k exp(-t E_k), E_k = -a_k.  Bulk term (exact for the full-line linear potential, integrated over x > 0):
  W(t) = (4 pi)^{-1/2} t^{-3/2} exp(t^3/12).  Claim: Theta - W ~ -1/4 + b1 t^{3/2} + b2 t^3 + b3 t^{9/2} + ...  (boundary
  invariants depend only on V'(0) = 1, weight t^{3/2}), hence Z(-j) = (-1)^j j! [t^j]Theta = 0 unless 3 | j, Z(0) = -1/4, and
  b2 = -Z_E(-3)/6, where Z_E(-3) = (3pi/2)^2 Z_lam'(-3) (energy units; Z_lam'(-3) = 0.0105542899627 from spec_zeta_airy.out,
  normalised eigenvalues lam' = E/(3pi/2)^{2/3}). Observed: Z_E(-3) = 15/64, b1 = 1/(6 sqrt(pi)) (NUMERICAL identifications)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from spec_airy import zeros
E = zeros(20000)                 # eigenvalues E_k = -a_k > 0
mp.mp.dps = 30
def R(t):
    th = mp.fsum(mp.exp(-t * mp.mpf(x)) for x in E if t * x < 120)
    return th - (4 * mp.pi) ** -0.5 * t ** -1.5 * mp.exp(t ** 3 / 12) + mp.mpf(1) / 4
ts = [mp.mpf(x) / 40 for x in range(4, 33)]           # t in [0.1, 0.8]
vals = [R(t) for t in ts]
for J in (4, 5, 6):
    A = mp.matrix([[t ** (1.5 * (i + 1)) for i in range(J)] for t in ts]); b = mp.matrix(vals)
    co = mp.lu_solve(A.T * A, A.T * b)
    print(f"fit J={J}: b1 = {mp.nstr(co[0], 12)}, b2 = {mp.nstr(co[1], 12)}, b3 = {mp.nstr(co[2], 8)}")
ZE3 = (3 * mp.pi / 2) ** 2 * mp.mpf('0.0105542899627')
print("Z_E(-3) = (3pi/2)^2 Z_lam'(-3) =", mp.nstr(ZE3, 12), " vs 15/64 =", mp.nstr(mp.mpf(15) / 64, 12))
print("prediction b2 = -Z_E(-3)/6 =", mp.nstr(-ZE3 / 6, 12), " (-5/128 =", mp.nstr(-mp.mpf(5) / 128, 12), ");  1/(6 sqrt pi) =", mp.nstr(1 / (6 * mp.sqrt(mp.pi)), 12))
print("check: an integer-power term c t^1 would give Z(-1) = -c; fit with t^1 added:")
A = mp.matrix([[t, t ** 1.5, t ** 3, t ** 4.5, t ** 6] for t in ts]); co = mp.lu_solve(A.T * A, A.T * mp.matrix(vals))
print("  c(t^1) =", mp.nstr(co[0], 5), " b1 =", mp.nstr(co[1], 10), " b2 =", mp.nstr(co[2], 10))
