"""Plan 48 (NUMERICAL illustration of Lemma W', ROUTE2.md §4.2): Mellin symbols of the log-commutator kernel used for the
alpha_x = 0 hard edge.  Same ray: m(s) = int_0^inf u^{s-1} log(u)/(u - 1) du on Re s = 1/2 (absolutely convergent; the
proof needs only the bound |m| <= M0 := int_0^inf u^{-1/2}|log u|/|u - 1| du).  Printed: m(1/2 + i tau), the closed form
pi^2/sin^2(pi s) for comparison (not used in the proof), and M0.  Rays at angle difference d: the kernel
log(u)/(u e^{i d} - 1); printed sup_tau of its symbol over the tau-grid, and its absolute bound.
Run: .venv/bin/python ../ja-plan48/research/G1/RH/route2/checks/check_r2_mellin.py"""
import mpmath as mp

mp.mp.dps = 20
M0 = mp.quad(lambda u: u ** -0.5 * abs(mp.log(u)) / abs(u - 1), [0, 1, mp.inf])
print(f"M0 = int u^(-1/2)|log u|/|u-1| du = {mp.nstr(M0, 10)}  (pi^2 = {mp.nstr(mp.pi**2, 10)})")
for tau in (0, 0.5, 1, 3):
    s = mp.mpc(0.5, tau)
    m = mp.quad(lambda u: u ** (s - 1) * mp.log(u) / (u - 1), [0, 1, mp.inf])
    print(f"  tau={tau}: m = {mp.nstr(m, 10)}, pi^2/sin^2(pi s) = {mp.nstr(mp.pi**2 / mp.sin(mp.pi*s)**2, 10)}")
for d in (mp.pi / 3, 2 * mp.pi / 3, mp.pi):
    A = mp.quad(lambda u: u ** -0.5 * abs(mp.log(u)) / abs(u * mp.expj(d) - 1), [0, 1, mp.inf])
    sup = max(abs(mp.quad(lambda u: u ** (mp.mpc(0.5, t) - 1) * mp.log(u) / (u * mp.expj(d) - 1), [0, 1, mp.inf]))
              for t in (0, 0.5, 1, 2, 4))
    print(f"  angle {mp.nstr(d, 4)}: sup_tau |symbol| = {mp.nstr(sup, 6)} <= absolute bound {mp.nstr(A, 6)}")
