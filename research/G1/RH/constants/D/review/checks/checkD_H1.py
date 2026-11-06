# (d') Monien's second printed value H^(1)_100 ~ 4.3e-16871 vs A1 = (e^{9/8}/sqrt 6) A0 for both A0 candidates (asymptotic form, n-1 = 100).
import mpmath as mp
mp.mp.dps = 40
cand = mp.exp(mp.mpf(1)/12)*mp.mpf(2)**(mp.mpf(1)/6)*mp.mpf(3)**(mp.mpf(1)/8)/mp.glaisher**3
n = 101; x = mp.mpf(1)/(2*n)
for name, A0 in (('closed', cand), ('printed', mp.mpf('0.351466738331'))):
    A1 = mp.exp(mp.mpf(9)/8)/mp.sqrt(6)*A0
    lg = (mp.log(A1) - (n**2 - mp.mpf(3)/4)*(mp.log(2*n) - mp.mpf(3)/2) + mp.log(1 - mp.mpf(17)/240*x**2))/mp.log(10)
    ex = mp.floor(lg); print('H^(1)_100 with A0 %s: %s e%d' % (name, mp.nstr(10**(lg-ex), 6), int(ex)))
