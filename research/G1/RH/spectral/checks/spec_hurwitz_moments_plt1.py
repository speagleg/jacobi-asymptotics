"""SPEC §3.1 (p < 1 analogue of Lemma H; NUMERICAL). E_plt1 Lemma F.1(iii): with theta = theta_s = p pi/2 (on Gamma_+,
t = n zeta^{-1/p} = -i|t|) and the seam jumps of the shifted lattice
  l_+(r) = -Log(1 - e^{2 pi i d} e^{-2 pi n r^{-1/p}}),  l_-(r) = -Log(1 - e^{-2 pi i d} e^{-2 pi n r^{-1/p}}),
  m_k(d) := (1/2 pi i) int_0^inf [e^{i theta}(r e^{i theta})^{-k-1} l_+(r) - e^{-i theta}(r e^{-i theta})^{-k-1} l_-(r)] dr
claim: m_k(d) = zeta(-k p, a)/(k n^{k p}),  a = d - ceil(d) + 1.  d = 0 is E_plt1 Lemma F.1(iii)."""
import mpmath as mp
mp.mp.dps = 30
def mk(k, p, n, d):
    p = mp.mpf(p); th = p * mp.pi / 2; e = mp.expj(2 * mp.pi * d)
    def f(r):
        em = mp.expm1(-2 * mp.pi * n * r ** (-1 / p))          # q - 1, accurate as q -> 1 (r -> inf)
        lp, lm = -mp.log((1 - e) - e * em), -mp.log((1 - 1 / e) - em / e)
        return mp.expj(th) * (r * mp.expj(th)) ** (-k - 1) * lp - mp.expj(-th) * (r * mp.expj(-th)) ** (-k - 1) * lm
    sc = mp.mpf(n) ** p
    return mp.quad(f, [0, sc / 100, sc / 10, sc, 10 * sc, 100 * sc, mp.inf]) / (2j * mp.pi)
worst = 0
for p in (0.3, 0.6, 0.75):
    for d in (mp.mpf(0), mp.mpf('-0.5'), mp.mpf('0.3'), mp.mpf('1.4')):
        for k in (1, 2, 3):
            n = 7; a = d - mp.ceil(d) + 1
            ref = mp.zeta(-k * mp.mpf(p), a) / (k * mp.mpf(n) ** (k * p)); m = mk(k, p, n, d)
            err = abs(m - ref) / abs(ref); worst = max(worst, err)
            print(f"p={p} d={mp.nstr(d,3)} k={k}: m_k = {mp.nstr(mp.re(m),14)} (Im {mp.nstr(mp.im(m),2)})  zeta(-kp,a)/(k n^kp) = {mp.nstr(ref,14)}  rel {mp.nstr(err,2)}")
print("worst relative error:", mp.nstr(worst, 3)); assert worst < 1e-14   # ~1e-16 for kp = 0.9, 1.8 (quadrature precision), 1e-30 otherwise
print("ALL ASSERTIONS PASSED")
