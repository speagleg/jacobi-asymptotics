"""SPEC §6 Lemma H (exact; NUMERICAL check at 30 digits). Shifted band-factor jump for p > 1:
  e_d(y) = 2 Im Log(1 - exp(-2 i pi (t_+(y) - d))),  t_+ = n (y + i0)^{-1/p},  y = -r < 0,
moments m_k(d) := (1/2pi) int_{-inf}^0 e_d(y) y^{-k-1} dy  =  zeta(-k p, a)/(k n^{k p}),  a = d - ceil(d) + 1 in (0, 1]
(Hurwitz's formula DLMF 25.11.9). d = 0 is E3 Lemma F.1'(i)."""
import mpmath as mp
mp.mp.dps = 30
def e_dens(r, p, n, d):
    t = n * r ** (-1 / mp.mpf(p)) * mp.expj(-mp.pi / p)
    a = -2j * mp.pi * (t - d)
    if mp.re(a) < -200: return mp.mpf(0)
    return 2 * mp.im(mp.log(1 - mp.exp(a)))
def moment(k, p, n, d):
    p = mp.mpf(p); sc = n ** p
    f = lambda r: e_dens(r, p, n, d) * (-1) ** (k + 1) * r ** (-k - 1)
    return mp.quad(f, [0, sc * mp.mpf('0.01'), sc * 0.1, sc, 10 * sc, 100 * sc, mp.inf]) / (2 * mp.pi)
worst = 0
for p in (1.25, 1.5, 3):
    for d in (mp.mpf('-0.5'), mp.mpf('0.3'), mp.mpf('0.75'), mp.mpf('1.4')):
        for k in (1, 2, 3):
            n = 7
            a = d - mp.ceil(d) + 1
            ref = mp.zeta(-k * mp.mpf(p), a) / (k * mp.mpf(n) ** (k * p))
            m = moment(k, p, n, d)
            rel = abs(m - ref) / abs(ref) if abs(ref) > 1e-25 else abs(m) * mp.mpf(n) ** (k * p)   # ref = 0: zeta(-kp, 1/2) = 0 for even integer kp (B_{kp+1}(1/2) = 0); compare n^{kp}·m_k with 0
            worst = max(worst, rel)
            print(f"p={p} d={mp.nstr(d,3)} (a={mp.nstr(a,3)}) k={k}: m_k = {mp.nstr(m, 14)}  zeta(-kp,a)/(k n^kp) = {mp.nstr(ref, 14)}  rel {mp.nstr(rel, 2)}")
print("worst relative error:", mp.nstr(worst, 3)); assert worst < 1e-20
print("ALL ASSERTIONS PASSED")
