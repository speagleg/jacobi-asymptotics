"""Plan 14 Phase B (CERTIFIED, Arb via python-flint): the winding number in Lemma Z is 0.

Setting (x-units; everything below is N-independent, see RH_zeta_close.md section 2):
  t(z) = gamma/(2 pi) log(gamma/(2 pi e)) + 11/8,  gamma = (1/z - 1/4)^{1/2};
  D_up = Dt/(1 - e^{-2 pi i t}) in C_+,  Dt = exp(-mu(t)),  mu = Binet's function (principal lgamma);
  C = circle through -r and x_m (r = 0.0017, x_m = 0.015; x_1 < x_m < x_e, r < |x_cross| = 1/(4 pi^2 e^2 - 1/4)).
Exact bookkeeping (RH_zeta_close.md section 2): winding(F_out/F_in, C) = -(lhat_arc(-r) - lhat_axis(-r))/(2 pi), where
  lhat_arc  = 2 x (continuous arg of D_up from x_m+i0 along the upper arc of C to -r+i0, starting from the principal value),
  lhat_axis = 2 x (continuous arg of D_+ along (-r, 0) from 0-, where it tends to 0).
Certification: every step's continuous arg increment is certified to be the principal Arg of the endpoint ratio, by
showing Re(D(Z)/D(z_a)) > 0 on a ball Z covering the step. On each ball, t(Z) avoids (-inf, 0] (lgamma/log continuity).
The near-0- tail (eta := (1/4 - 1/x)^{1/2} >= eta0) uses DLMF 5.11 (|mu(t)| <= sec^2(ph t/2)/(12|t|)) at eta0 together
with monotonicity in eta."""
from flint import acb, arb, ctx

ctx.prec = 128
PI = arb.pi()
E = arb(1).exp()
r = arb("0.0017")
xm = arb("0.015")
c0 = (xm - r) / 2
Rad = (xm + r) / 2
xe = 1 / (4 * PI ** 2 + arb("0.25"))
xcross = 1 / (4 * PI ** 2 * E ** 2 - arb("0.25"))
assert (r < xcross) and (xm < xe)


def t_of_gamma(g):
    return g / (2 * PI) * (g / (2 * PI * E)).log() + arb(11) / 8


def gamma_upper(z, rotated):
    """gamma(z) for z on/near the closed upper arc; 'rotated' = analytic continuation valid near the negative axis."""
    u = 1 / z - arb("0.25")
    return acb(0, -1) * (-u).sqrt() if rotated else u.sqrt()


def logD_up(t):
    mu = t.lgamma() - (t - arb("0.5")) * t.log() + t - (2 * PI).log() / 2
    return -mu - (1 - (acb(0, -2) * PI * t).exp()).log()


def D_up(t):
    mu = t.lgamma() - (t - arb("0.5")) * t.log() + t - (2 * PI).log() / 2
    return (-mu).exp() / (1 - (acb(0, -2) * PI * t).exp())


def t_ok(t):
    """t avoids (-inf, 0]: Im t excludes 0, or Re t > 0."""
    return (not t.imag.contains(0)) or (t.real > 0)


def certify_path(point, ball, a, b, depth=0, maxdepth=40):
    """Sum of certified arg increments of D along the path parameter [a, b] (arb endpoints).
    point(p) -> t at parameter p (point ball);  ball(a, b) -> t-enclosure over the whole sub-path."""
    stack = [(a, b, 0)]
    total = arb(0)
    nsteps = 0
    while stack:
        lo, hi, d = stack.pop()
        tZ = ball(lo, hi)
        ta, tb = point(lo), point(hi)
        ok = t_ok(tZ) and t_ok(ta) and t_ok(tb)
        if ok:
            Da = D_up(ta)
            w = D_up(tZ) / Da
            ok = w.real > 0
        if ok:
            total += (D_up(tb) / Da).arg()
            nsteps += 1
        else:
            if d >= maxdepth:
                raise RuntimeError(f"certification failed near parameter {lo.mid()}..{hi.mid()}")
            mid = (lo + hi) / 2
            stack.append((mid, hi, d + 1))
            stack.append((lo, mid, d + 1))
    return total, nsteps


# ---- (1) upper arc theta: 0 -> pi, z = c0 + Rad e^{i theta} ----
def z_of(th):
    return acb(c0) + acb(Rad) * acb(0, th).exp()


def arc_point(th):
    return t_of_gamma(gamma_upper(z_of(th), rotated=(th > PI / 2)))


def arc_ball(lo, hi):
    mid = (lo + hi) / 2
    zc = z_of(mid)
    rad = Rad * (hi - lo) / 2 * arb("1.000001")
    Z = acb(arb(zc.real.mid(), rad.upper()), arb(zc.imag.mid(), rad.upper()))
    return t_of_gamma(gamma_upper(Z, rotated=(mid > PI / 2)))


# split at pi/2 (switch of gamma's determination; both agree there)
t_xm = t_of_gamma(gamma_upper(acb(xm), rotated=False))
assert t_xm.imag.contains(0) and (t_xm.real > arb(3) / 8) and (t_xm.real < 1), t_xm
# D_up at x_m + i0: real t in (3/8, 1), principal formulas are continuous there
start_arc = logD_up(acb(t_xm.real)).imag
q1 = arc_point(PI / 2 - arb("1e-30")); q2 = arc_point(PI / 2 + arb("1e-30"))
assert (q1 - q2).abs_upper() < 1e-20, "gamma determinations disagree at pi/2"
inc1, n1 = certify_path(arc_point, arc_ball, arb(0), PI / 2)
inc2, n2 = certify_path(arc_point, arc_ball, PI / 2, PI)
lhat_arc = 2 * (start_arc + inc1 + inc2)


# ---- (1b) Im t < 0 on the upper arc (for the maximum principle: D_up analytic and zero-free inside C in C_+) ----
th1 = arb("1e-3")
def imt_neg(lo, hi, d=0):
    tZ = arc_ball(lo, hi)
    if tZ.imag < 0:
        return 1
    if d > 40:
        raise RuntimeError(f"Im t < 0 not certified near theta={lo.mid()}")
    m = (lo + hi) / 2
    return imt_neg(lo, m, d + 1) + imt_neg(m, hi, d + 1)
n_im = imt_neg(th1, PI)
# near x_m (theta in [0, th1]): Im t(z) = Im int_{x_m}^z t'(w) dw along the segment; z - x_m = rho e^{i psi} with
# psi in [pi/2, pi/2 + th1]; certify sin(psi) Re t' + cos(psi) Im t' < 0 for t' on a ball covering the segments.
def tprime(z):
    g = gamma_upper(z, rotated=False)
    return (g / (2 * PI)).log() / (2 * PI) * (-1 / (2 * z * z * g))
seg_rad = Rad * th1 * arb("1.01")
Zs = acb(arb(xm.mid(), seg_rad.upper()), arb(0, seg_rad.upper()))
tp = tprime(Zs)
PSI = arb((PI / 2 + th1 / 2).mid(), (th1 / 2 * arb("1.0001")).upper())
near_ok = (PSI.sin() * tp.real + PSI.cos() * tp.imag) < 0
assert near_ok, (tp, PSI)

# ---- (2) negative axis: x from -eps0 to -r, D_+ (z = x + i0), gamma_+ = -i (1/4 - 1/x)^{1/2} ----
eps0 = arb("1e-7")


def ax_point(x):
    return t_of_gamma(acb(0, -1) * acb(arb("0.25") - 1 / x).sqrt())


def ax_ball(lo, hi):  # lo, hi are x-values (lo > hi, i.e. moving left); enclose [hi, lo]
    X = arb((lo + hi) / 2, abs((lo - hi) / 2) * arb("1.000001"))
    return t_of_gamma(acb(0, -1) * acb(arb("0.25") - 1 / X).sqrt())


# parametrize by log|x| to resolve the approach to 0
def axp(v):  # v = log(-x)
    return ax_point(-(v.exp()))


def axb(lo, hi):
    V = arb((lo + hi) / 2, abs((hi - lo) / 2) * arb("1.000001"))
    return ax_point(-(V.exp()))


inc_ax, n3 = certify_path(axp, axb, eps0.log(), r.log())
t0 = axp(eps0.log())
start_ax = logD_up(t0).imag

# ---- (3) tail (-eps0, 0): bound |mu| and |e^{-2 pi i t}| at eta0 (both decrease with eta; see RH_zeta_close.md 2) ----
eta0 = (arb("0.25") + 1 / eps0).sqrt()
ph = t0.arg()
sec2 = 1 / ((ph / 2).cos() ** 2)
mu_bound = sec2 / (12 * t0.abs_lower())
exp_bound = (2 * PI * t0.imag).exp()  # |e^{-2 pi i t}| = e^{2 pi Im t}
assert (mu_bound < arb("0.1")) and (exp_bound < arb("0.1")), (mu_bound, exp_bound)
lhat_axis = 2 * (start_ax + inc_ax)

W = -(lhat_arc - lhat_axis) / (2 * PI)
print(f"t(x_m) = {t_xm.real.str(10)} (in (3/8, 1));  arc steps {n1}+{n2}, axis steps {n3}")
print(f"tail at eta0 = {eta0.str(6)}: |mu| <= {mu_bound.str(4)}, |e^(-2 pi i t)| <= {exp_bound.str(4)}, ph t = {ph.str(6)}")
print(f"Im t < 0 certified on the upper arc: {n_im} balls on [1e-3, pi] + derivative bound on [0, 1e-3] (t' = {tp.str(6)})")
print(f"lhat_arc(-r)  = {lhat_arc.str(15)}")
print(f"lhat_axis(-r) = {lhat_axis.str(15)}")
print(f"winding W = {W.str(15)}")
ok = (W.abs_upper() < arb("0.5"))
print("CERTIFIED: winding number of F_out/F_in around C is 0" if ok else "NOT certified")
