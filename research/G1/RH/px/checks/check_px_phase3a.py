"""Plan 12 Phase 3a (NUMERICAL): D-functions on the slit plane (x-variable, rescaled), p > 1.
t(z) = N z^{-1/p}, theta = pi t.  Dt(z) := sqrt(2 pi) t^{t-1/2} e^{-t} / Gamma(t)  (= exp(-mu(t)), mu = Binet),
D := Dt / (1 - e^{-+2 i theta}) in C_+-  (WLXZ (4.16) pattern).
 [1] On (-inf,0): D_- = conj(D_+), so D_+/D_- = e^{2 i arg D_+} is unimodular. Profile of arg D_+ from 0- to -inf;
     its limit L/2 at -inf (prediction: arg(-i t_+^{-1/2}) -> pi/(2p) - pi/2).
 [2] Size of the Dt jump on (-delta,0) (not small: O(|x|^{1/p}/N)) vs the jump of Dt*S where S cancels D's jump:
     (1 - e^{-2 i theta_+})/(1 - e^{2 i theta_-}) - 1 (super-small, ~ e^{-2 pi N sin(pi/p) |x|^{-1/p}}).
 [3] Growth of D at infinity: |D| ~ |t|^{-1/2}/sqrt(2 pi), i.e. ~ |z|^{1/(2p)} N^{-1/2}."""
import mpmath as mp

mp.mp.dps = 40
def setup(p, N):
    p = mp.mpf(p)
    t = lambda z: N * mp.power(z, -1 / p)
    Dt = lambda z: mp.sqrt(2 * mp.pi) * mp.exp((t(z) - 0.5) * mp.log(t(z)) - t(z) - mp.loggamma(t(z)))
    def D(z):
        sg = 1 if mp.im(z) > 0 else -1
        return Dt(z) / (1 - mp.exp(-sg * 2j * mp.pi * t(z)))
    return p, t, Dt, D
for p, N in ((1.5, 20), (2, 20), (3, 20), (2, 80)):
    p, t, Dt, D = setup(p, N)
    e = mp.mpf("1e-30")
    print(f"p={p} N={N}:  predicted limit arg D_+ -> pi/(2p) - pi/2 = {mp.nstr(mp.pi/(2*p) - mp.pi/2, 8)}")
    for x in ("-1e-3", "-0.1", "-1", "-10", "-1e3", "-1e5", "-1e8", "-1e12"):
        x = mp.mpf(x)
        Dp, Dm = D(x + 1j * e), D(x - 1j * e)
        th_p = mp.pi * t(x + 1j * e); th_m = mp.pi * t(x - 1j * e)
        jt = abs(Dt(x + 1j * e) / Dt(x - 1j * e) - 1)
        js = abs((1 - mp.exp(-2j * th_p)) / (1 - mp.exp(2j * th_m)) - 1)
        print(f"   x={mp.nstr(x,3):>7}: |D+/D- |-1 = {mp.nstr(abs(Dp/Dm)-1, 2):>8}  arg D+ = {mp.nstr(mp.arg(Dp), 8):>12}"
              f"   |Dt jump| = {mp.nstr(jt, 3):>9}   |Dt*S jump| = {mp.nstr(js, 3):>9}")
    for R in ("1e4", "1e8", "1e12"):
        z = mp.mpf(R) * mp.expjpi(mp.mpf("0.3"))
        print(f"   |z|={R}: |D| * |t|^(1/2) * sqrt(2pi) = {mp.nstr(abs(D(z)) * mp.sqrt(abs(t(z))) * mp.sqrt(2*mp.pi), 8)}")
