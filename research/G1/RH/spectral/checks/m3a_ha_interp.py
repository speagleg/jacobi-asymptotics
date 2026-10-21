"""JZC M3a, step H-a (JZC_M3a_H_Ha.md): the interpolation problem for the Hurwitz lattice (NUMERICAL, mpmath dps 60).
Hurwitz measure sigma^d = sum_{k>=1} tau_k^{-s} delta_{x_k}, tau_k = k + d, x_k = tau_k^{-p}, -1 < d <= 0, a = 1 + d.
Rescaled nodes X_k = n^p x_k = (n/tau_k)^p, top node X_1 = (n/a)^p. t = n z^{-1/p}, theta_d = pi (t - d), w(z) = n^p t^{-s},
W = 2 i theta' w, theta' = -(pi/p) t/z (Paper 2 (eq:t), (eq:theta), (eq:W); theta_d' = theta').
U(z) = n^{p n sigma3} Y(z n^{-p}), Y = (eq:Y-solution) built from the monic OPs of sigma^d (moments by own Euler-Maclaurin, below).
U_{j2} is evaluated by DIRECT summation over the nodes k <= K plus an expanded tail (no use of the residue formula).
Claims checked (memo numbering):
  Ha.1  zeros of 1 - e^{2 i theta_d} in sectors |arg z| < phi, r1 < |z| < r2 (argument principle): for phi = theta_w (Paper 2
        (eq:thetaw): 7pi/16 for p > 1, 3pi p/8 for p < 1) and for p > 1 even phi = 0.95 pi, the count equals the number of
        Hurwitz nodes X_k in (r1, r2); the non-nodes t = d - m (m >= 0) do not appear.
        CONTROL (must fail): p = 0.6, phi = 0.95 pi > pi p: the count includes the points t = d - m on arg z = +-pi p.
  Ha.2  top node: the Laurent coefficients c_i of U_12 z^n at infinity have c_{i+1}/c_i -> X_1 = (n/a)^p (radius of |z| > X_1);
        extraction (eq:extractU) on the circle |z| = 2 X_1: b(U z^{-n s3}) = n^{2p} b_n^2, a(U z^{-n s3}) = n^p a_n, with a_n, b_n^2 from
        the three-term recurrence of the monic OPs (moments only).
        CONTROL (must fail, d < 0): the same extraction on the circle |z| = (n^p + X_1)/2, which lies outside
        Paper 2's lattice top node n^p but inside X_1.
  Ha.4  node masses: Res_{X_k} U_j2 = n^p tau_k^{-s} U_j1(X_k) (contour integral of the direct sum), and
        Res_{X_k} W/(e^{2 i theta_d} - 1) = Res_{X_k} w e^{-i theta_d}/Pi_d = n^p tau_k^{-s} (Pi_d := sin theta_d / theta'), k = 1, 2, 3;
        sin pi(t - d) = pi/(Gamma(t - d) Gamma(1 - t + d)) and D~_d = e^{-j_d} = sqrt(2 pi) t^{t-d-1/2} e^{-t}/Gamma(t - d) at sample t.
        CONTROL (must fail, d < 0): Res_{X_k} W/(e^{2 i theta} - 1) with the lattice phase is 0, not the mass.
  Ha.5  pole removal: R_j2 := U_j2 - U_j1 W/(e^{2 i theta_d} - 1) (lens) and R_j1 := kappa_+(U_j1 - U_j2/(kappa_+ W)) (saturated region),
        kappa_+ = 1/(1 - e^{-2 i theta_d}), are continuous at every node X_1, X_2, X_3: |R(X_k + eps e^{i phi})| bounded, and the
        values at eps = 1e-12 X_k, 1e-16 X_k (phi = pi/3, 2pi/3) agree to 1e-8 relative.
        CONTROL (must fail, d < 0): with the lattice kappa (theta in place of theta_d), eps |R| does not tend to 0.
Rule N: NUMERICAL (finite samples); nothing fitted; pass/fail computed."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_common import Checks
mp.mp.dps = 60
C_ = Checks(); I = mp.mpc(0, 1)
_chk = C_.check
C_.check = lambda lab, v, pr, tol: _chk(lab, float(mp.re(v)), float(mp.re(pr)), float(tol)); PI = mp.pi
KDIR = 400          # nodes summed directly


def hz_tail(sig, b, J=14):
    """sum_{m>=0} (m + b)^{-sig}, b >= 100, by Euler-Maclaurin with exact derivatives (error ~ ((sig+2J)/(2 pi b))^{2J})."""
    f = lambda m: (b + m)**(-sig)
    tot = b**(1 - sig)/(sig - 1) + f(0)/2
    for j in range(1, J + 1):
        k = 2*j - 1   # f^{(k)}(0) = (-1)^k sig (sig+1)...(sig+k-1) b^{-sig-k}
        tot -= mp.bernoulli(2*j)/mp.factorial(2*j)*(-1)**k*mp.rf(sig, k)*b**(-sig - k)
    return tot


def hsum(sig, d):
    """sum_{k>=1} (k + d)^{-sig} = sum_{k<=KDIR} + tail."""
    return mp.fsum((k + d)**(-sig) for k in range(1, KDIR + 1)) + hz_tail(sig, KDIR + 1 + d)


def monic(n, mom):
    """coefficients (low -> high) of the monic OP of degree n for moments mom."""
    if n == 0: return [mp.mpf(1)]
    A = mp.matrix(n, n); b = mp.matrix(n, 1)
    for i in range(n):
        for j in range(n): A[i, j] = mom[i + j]
        b[i] = -mom[n + i]
    c = mp.lu_solve(A, b)
    return [c[i] for i in range(n)] + [mp.mpf(1)]


def pev(c, x): return mp.fsum(ci*x**i for i, ci in enumerate(c))


class Hur:
    def __init__(self, p, s, d, n):
        self.p, self.s, self.d, self.n = mp.mpf(p), mp.mpf(s), mp.mpf(d), n
        self.a = 1 + self.d; P = self.p
        self.mom = [hsum(self.s + j*P, self.d) for j in range(2*n + 4)]
        self.Pn, self.Pm, self.Pp = monic(n, self.mom), monic(n - 1, self.mom), monic(n + 1, self.mom)
        h = lambda c: mp.fsum(c[i]*c[j]*self.mom[i + j] for i in range(len(c)) for j in range(len(c)))
        self.hn, self.hm = h(self.Pn), h(self.Pm)
        self.b2 = self.hn/self.hm                                   # b_n^2 = h_n/h_{n-1}
        self.an = self.Pn[n - 1] - self.Pp[n]                       # a_n = pi_n - pi_{n+1}
        self.np_ = mp.mpf(n)**P
        self.X = lambda k: (n/(k + self.d))**P
        self.mass = lambda k: (k + self.d)**(-self.s)

    def _prep(self, I_terms=40):
        """node data and tail moments (independent of zeta), computed once."""
        self.xs = [(k + self.d)**(-self.p) for k in range(1, KDIR + 1)]
        self.ws = [self.mass(k) for k in range(1, KDIR + 1)]
        b0 = KDIR + 1 + self.d
        T = [hz_tail(self.s + j*self.p, b0) for j in range(I_terms + self.n + 2)]
        self.cols = []
        for c, hh in ((self.Pn, 1), (self.Pm, self.hm)):
            wp = [w*pev(c, x) for w, x in zip(self.ws, self.xs)]
            tm = [mp.fsum(cl*T[l + i] for l, cl in enumerate(c)) for i in range(I_terms)]
            self.cols.append((c, hh, wp, tm))

    def Y(self, zeta):
        """Y(zeta) by direct summation over k <= KDIR plus the expanded tail sum_i zeta^{-i-1} sum_{k>KDIR} w_k pi(x_k) x_k^i."""
        if not hasattr(self, 'cols'): self._prep()
        out = []
        for c, hh, wp, tm in self.cols:
            direct = mp.fsum(v/(zeta - x) for v, x in zip(wp, self.xs))
            tail = mp.fsum(mi/zeta**(i + 1) for i, mi in enumerate(tm))
            out.append((pev(c, zeta)/hh, (direct + tail)/hh))
        return out   # [(Y11, Y12), (Y21, Y22)]

    def U(self, z):
        n, P = self.n, self.p; zeta = z/self.np_
        (y11, y12), (y21, y22) = self.Y(zeta)
        f = self.np_**n
        return (f*y11, f*y12), (y21/f, y22/f)

    def U1(self, z):
        """first column of U only (polynomials; safe at the nodes)."""
        f = self.np_**self.n; zeta = z/self.np_
        return (f*pev(self.Pn, zeta), pev(self.Pm, zeta)/(self.hm*f))

    def t(self, z): return self.n*mp.power(z, -1/self.p)
    def W(self, z):
        t = self.t(z); return 2*I*(-PI/self.p)*(t/z)*self.np_*t**(-self.s)
    def w(self, z): return self.np_*self.t(z)**(-self.s)
    def E(self, z, dd): return mp.expj(2*PI*(self.t(z) - dd))   # e^{2 i theta_dd}


def circle_int(f, z0, r, N=64):
    """(1/2 pi i) oint f over |z - z0| = r, trapezoid (exponentially accurate for f meromorphic with no other poles nearby)."""
    tot = 0
    for j in range(N):
        e = mp.expjpi(2*mp.mpf(j)/N); tot += f(z0 + r*e)*r*e
    return tot/N


def count_zeros(H, phi, tin, tout):
    """argument principle for f = 1 - e^{2 pi i (t - d)} on {r1 < |z| < r2, |arg z| < phi}, t(r1) = tout, t(r2) = tin (|t| values)."""
    p, n, d = H.p, H.n, H.d
    r1, r2 = (n/tout)**p, (n/tin)**p
    def dlog(z):
        t = n*mp.power(z, -1/p); E = mp.expj(2*PI*(t - d)); dt = -t/(p*z)
        return -2*PI*I*dt*E/(1 - E)
    def ray(ang, ra, rb):   # integral along z = r e^{i ang}, r: ra -> rb
        e = mp.expj(ang)
        g = lambda u: dlog(mp.e**u*e)*mp.e**u*e
        return mp.quad(g, mp.linspace(mp.log(ra), mp.log(rb), 9))
    def arc(r, a0, a1):
        brk = sorted(set([a0, a1] + [x for x in (-PI*p, 0, PI*p) if a0 < x < a1]))
        g = lambda th: dlog(r*mp.expj(th))*I*r*mp.expj(th)
        return mp.quad(g, brk)
    tot = ray(-phi, r1, r2) + arc(r2, -phi, phi) + ray(phi, r2, r1) - arc(r1, -phi, phi)
    return tot/(2*PI*I)


CASES = [(1.5, 0.0), (1.5, -0.3), (1.5, -0.9), (3.0, -0.3), (3.0, -0.9), (0.6, 0.0), (0.6, -0.3), (0.6, -0.9)]
ALPHA = mp.mpf(-3)/10; NDEG = 3
controls = {}
print("JZC M3a, H-a: Hurwitz interpolation problem.  n = 3, alpha = -0.3 (s = 1 + p + alpha p), dps", mp.mp.dps)

# sanity of the Euler-Maclaurin tail against mp.zeta at small b (where mp.zeta is reliable, G12 §3)
for sig, b in ((mp.mpf('1.4'), mp.mpf(101)), (mp.mpf('7.3'), mp.mpf('100.1'))):
    v1, v2 = hz_tail(sig, b), mp.zeta(sig, b)
    C_.check(f"EM tail vs mp.zeta sigma={sig} b={b} (rel)", abs(v1/v2 - 1), 0, mp.mpf(10)**-30)

for (p, d) in CASES:
    p = mp.mpf(p); d = mp.mpf(d); s = 1 + p + ALPHA*p
    H = Hur(p, s, d, NDEG); n = NDEG
    tag = f"p={mp.nstr(p,3)} d={mp.nstr(d,3)}"
    print(f"\n== {tag}: a = {mp.nstr(H.a,3)}, top node X_1 = (n/a)^p = {mp.nstr(H.X(1),10)}, n^p = {mp.nstr(H.np_,10)}")

    # ---- Ha.1: zeros in sectors
    thw = 7*PI/16 if p > 1 else 3*PI*p/8
    tin, tout = mp.mpf('0.5'), mp.mpf('5.5')     # |t| in (0.5, 5.5): |t| - frac avoids d + Z and -d + Z for these d
    expect = sum(1 for k in range(1, 10) if tin < k + d < tout)
    for phi, lab in ((thw, "theta_w"),) + (((0.95*PI, "0.95pi"),) if p > 1 else ()):
        cnt = count_zeros(H, phi, tin, tout)
        C_.check(f"Ha.1 {tag} integer count, sector {lab}", abs(cnt - mp.nint(cnt)), 0, mp.mpf(10)**-10)
        C_.check(f"Ha.1 {tag} zeros in sector {lab} = #nodes ({expect})", mp.re(cnt), expect, mp.mpf(10)**-10)
        print(f"Ha.1 sector |arg z| < {lab}: zero count {mp.nstr(mp.re(cnt), 12)}, Hurwitz nodes with |t| in (0.5, 5.5): {expect}")
    if p < 1:
        cnt = count_zeros(H, 0.95*PI, tin, tout)
        phantoms = 2*sum(1 for m in range(0, 10) if tin < m - d < tout)
        ok = abs(mp.re(cnt) - expect) <= mp.mpf(10)**-10
        controls[f"Ha.1 {tag} sector 0.95pi count = #nodes"] = ok
        print(f"   CONTROL sector 0.95pi (contains arg z = +-pi p): count {mp.nstr(mp.re(cnt), 12)} = nodes {expect} + "
              f"non-nodes t = d - m on both rays {phantoms}: {'PASS (unexpected)' if ok else 'fails as required'}")
        C_.check(f"Ha.1 {tag} control count = nodes + 2 x #(t = d - m)", mp.re(cnt), expect + phantoms, mp.mpf(10)**-10)
        # location of the non-nodes: arg z = +-pi p, outside Z_n (theta_w = 3 pi p/8) and outside S_in (pi p/2)
        C_.check(f"Ha.1 {tag} non-node ray pi p > theta_w", mp.mpf(1) if PI*p > thw else mp.mpf(0), 1, 0)

    # ---- Ha.2: top node and extraction
    momL = [hsum(s + j*p, d) for j in range(0, 2*n + 72)]
    cs = [mp.fsum(cl*momL[l + i] for l, cl in enumerate(H.Pn)) for i in range(n, n + 70)]   # int P_n x^i d sigma
    ratio = (cs[-1]/cs[-2])*H.np_      # U_12 z^n Laurent coefficient ratio (factor n^p from the rescaling)
    C_.check(f"Ha.2 {tag} Laurent radius -> X_1 (rel)", abs(ratio/H.X(1) - 1), 0, mp.mpf(10)**-6)
    print(f"Ha.2 c_(i+1)/c_i at i = {n+68}: {mp.nstr(ratio, 12)} vs X_1 = {mp.nstr(H.X(1), 12)} (n^p = {mp.nstr(H.np_, 8)})")

    def extract(Rc, N=96):
        U1 = [[0, 0], [0, 0]]; U2 = [[0, 0], [0, 0]]
        for j in range(N):
            e = mp.expjpi(2*mp.mpf(j)/N); z = Rc*e
            (u11, u12), (u21, u22) = H.U(z)
            M = [[u11*z**(-n) - 1, u12*z**n], [u21*z**(-n), u22*z**n - 1]]
            for r in range(2):
                for c in range(2):
                    U1[r][c] += M[r][c]*z/N; U2[r][c] += M[r][c]*z**2/N
        bb = U1[0][1]*U1[1][0]; aa = U2[0][1]/U1[0][1] - U1[1][1]
        return bb, aa
    bb, aa = extract(2*H.X(1))
    C_.check(f"Ha.2 {tag} b(Uz^-ns3) = n^2p b_n^2 (rel)", abs(bb/(H.np_**2*H.b2) - 1), 0, mp.mpf(10)**-20)
    C_.check(f"Ha.2 {tag} a(Uz^-ns3) = n^p a_n (rel)", abs(aa/(H.np_*H.an) - 1), 0, mp.mpf(10)**-20)
    print(f"Ha.2 extraction on |z| = 2X_1: b/(n^2p b_n^2) - 1 = {mp.nstr(bb/(H.np_**2*H.b2) - 1, 3)}, "
          f"a/(n^p a_n) - 1 = {mp.nstr(aa/(H.np_*H.an) - 1, 3)}   (b_n^2 = {mp.nstr(H.b2, 12)}, a_n = {mp.nstr(H.an, 12)})")
    if d < 0:
        Rl = (H.np_ + H.X(1))/2
        assert H.X(2) < Rl < H.X(1)
        bb2, aa2 = extract(Rl)
        ok = abs(bb2/(H.np_**2*H.b2) - 1) <= mp.mpf(10)**-20
        controls[f"Ha.2 {tag} extraction on circle |z| = (n^p + X_1)/2"] = ok
        print(f"   CONTROL on |z| = (n^p + X_1)/2 (< X_1): b/(n^2p b_n^2) - 1 = {mp.nstr(bb2/(H.np_**2*H.b2) - 1, 3)}: "
              f"{'PASS (unexpected)' if ok else 'fails as required'}")

    # ---- Ha.4: node masses / residues
    for k in (1, 2, 3):
        Xk = H.X(k); rr = min(Xk - H.X(k + 1), (H.X(k - 1) - Xk) if k > 1 else Xk)/4
        mass = H.np_*H.mass(k)
        # residue of the direct sum U_{j2}
        for j in (0, 1):
            res = circle_int(lambda z: H.U(z)[j][1], Xk, rr)
            pred = mass*H.U1(Xk)[j]
            C_.check(f"Ha.4 {tag} Res_X{k} U_{j+1}2 = n^p tau^-s U_{j+1}1(X_k) (rel)", abs(res/pred - 1), 0, mp.mpf(10)**-25)
        r1 = circle_int(lambda z: H.W(z)/(H.E(z, d) - 1), Xk, rr)
        Pi = lambda z: mp.sin(PI*(H.t(z) - d))/(-(PI/p)*H.t(z)/z)
        r2 = circle_int(lambda z: H.w(z)*mp.expj(-PI*(H.t(z) - d))/Pi(z), Xk, rr)
        C_.check(f"Ha.4 {tag} Res_X{k} W/(e^(2i theta_d)-1) = n^p tau^-s (rel)", abs(r1/mass - 1), 0, mp.mpf(10)**-25)
        C_.check(f"Ha.4 {tag} Res_X{k} w e^(-i theta_d)/Pi_d = n^p tau^-s (rel)", abs(r2/mass - 1), 0, mp.mpf(10)**-25)
        if k == 1: print(f"Ha.4 top node X_1: mass n^p a^-s = {mp.nstr(mass, 12)}; Res W/(e^(2i theta_d)-1) = {mp.nstr(r1, 12)}")
        if d < 0:
            r0 = circle_int(lambda z: H.W(z)/(H.E(z, 0) - 1), Xk, rr)
            ok = abs(r0/mass - 1) <= mp.mpf(10)**-25
            controls[f"Ha.4 {tag} lattice-phase residue at X_{k}"] = ok
            if k == 1: print(f"   CONTROL lattice phase: Res = {mp.nstr(r0, 5)}: {'PASS (unexpected)' if ok else 'fails as required'}")
    for tt in (mp.mpc('0.37', '-0.21'), mp.mpc('2.6', '0.4'), mp.mpc('7.1', '-3.3')):
        lhs = mp.sin(PI*(tt - d)); rhs = PI/(mp.gamma(tt - d)*mp.gamma(1 - tt + d))
        C_.check(f"Ha.4 {tag} reflection sin pi(t-d) at t={tt} (rel)", abs(lhs/rhs - 1), 0, mp.mpf(10)**-30)
        jd = mp.loggamma(tt - d) - (tt - d - mp.mpf(1)/2)*mp.log(tt) + tt - mp.log(2*PI)/2
        D2 = mp.sqrt(2*PI)*mp.power(tt, tt - d - mp.mpf(1)/2)*mp.e**(-tt)/mp.gamma(tt - d)
        C_.check(f"Ha.4 {tag} D~_d = sqrt(2pi) t^(t-d-1/2) e^-t / Gamma(t-d) at t={tt} (rel)", abs(mp.e**(-jd)/D2 - 1), 0, mp.mpf(10)**-30)

    # ---- Ha.5: pole removal
    worst_ctrl = 0
    for k in (1, 2, 3):
        Xk = H.X(k)
        def Rvals(z, dd):
            (u11, u12), (u21, u22) = H.U(z)
            K = H.W(z)/(H.E(z, dd) - 1)                  # = W e^{-2 i theta} kappa_+
            kap = 1/(1 - 1/H.E(z, dd))
            Wz = H.W(z)
            return [u12 - u11*K, u22 - u21*K, kap*(u11 - u12/(kap*Wz)), kap*(u21 - u22/(kap*Wz))]
        vals = {}
        for eps in (Xk*mp.mpf(10)**-12, Xk*mp.mpf(10)**-16):
            for ph in (PI/3, 2*PI/3):
                vals[(eps, ph)] = Rvals(Xk + eps*mp.expj(ph), d)
        ref = vals[(Xk*mp.mpf(10)**-16, PI/3)]
        for i, lab in enumerate(("lens R_12", "lens R_22", "sat R_11", "sat R_21")):
            scale = max(abs(ref[i]), mp.mpf(10)**-30)
            spread = max(abs(v[i] - ref[i]) for v in vals.values())/scale
            C_.check(f"Ha.5 {tag} {lab} continuous at X_{k} (rel spread)", spread, 0, mp.mpf(10)**-8)
        if d < 0:
            eps = Xk*mp.mpf(10)**-16
            v0 = Rvals(Xk + eps*mp.expj(PI/3), mp.mpf(0))
            worst_ctrl = max(worst_ctrl, max(abs(eps*v0[i])/max(abs(ref[i]), mp.mpf(10)**-30) for i in range(4)))
    if d < 0:
        ok = worst_ctrl <= mp.mpf(10)**-8
        controls[f"Ha.5 {tag} lattice kappa removes the poles"] = ok
        print(f"Ha.5 R continuous at X_1..X_3 (lens and saturated formulas); CONTROL lattice kappa: max eps|R|/|R_d| = "
              f"{mp.nstr(worst_ctrl, 3)}: {'PASS (unexpected)' if ok else 'fails as required'}")
    else:
        print("Ha.5 R continuous at X_1..X_3 (lens and saturated formulas)")

print("\nControls (each must fail):")
for k_, ok in controls.items(): print(f"  {k_}: {'PASSED -- ERROR' if ok else 'failed (required)'}")
assert controls and not any(controls.values()), "a control passed"
print(f"all {len(controls)} controls failed as required")
C_.finish()
