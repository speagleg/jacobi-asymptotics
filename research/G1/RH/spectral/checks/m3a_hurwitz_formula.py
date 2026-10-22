# Check: Hurwitz (Dixit-Kumar arXiv:1912.01199 Thm 1.1) at s=-kp, a=1+delta gives m_k(delta) = zeta(-kp,a)/(k n^{kp}) (n=1)
import mpmath as mp
mp.mp.dps=40
def L(sig,x): return mp.polylog(sig, mp.exp(2j*mp.pi*x))   # sum_m e^{2 pi i m x}/m^sig
def S(k,p,d):   # sum_m sin(pi k p/2 - 2 pi m d)/m^{1+kp} = Im( e^{i pi kp/2} * conj(L) )
    return mp.im(mp.exp(1j*mp.pi*k*p/2)*mp.conj(L(1+k*p,d)))
def hurwitz_rhs(s,a):
    l=L(1-s,a)
    return 2*mp.gamma(1-s)/(2*mp.pi)**(1-s)*(mp.sin(mp.pi*s/2)*mp.re(l)+mp.cos(mp.pi*s/2)*mp.im(l))
worst=0; n=0
for p in (mp.mpf(3)/2, 3, mp.mpf(3)/5, mp.mpf(5)/4):
  for d in (0, -mp.mpf(3)/10, -mp.mpf(1)/2, -mp.mpf(9)/10):
    for k in (1,2,3):
      a=1+d; z=mp.zeta(-k*p,a)
      r1=abs(hurwitz_rhs(-k*p,a)-z)/max(1,abs(z))
      mk=-(p/mp.pi)*mp.gamma(k*p)*(2*mp.pi)**(-k*p)*S(k,p,d)
      r2=abs(mk-z/k)/max(1,abs(z/k)); worst=max(worst,r1,r2); n+=2
# control: reflected parameter a -> -delta must fail for generic p
ctl=abs(-(mp.mpf(3)/2/mp.pi)*mp.gamma(mp.mpf(3)/2)*(2*mp.pi)**(-1.5)*S(1,mp.mpf(3)/2,-mp.mpf(3)/10) - mp.zeta(-1.5,mp.mpf(3)/10))
print(f"{n} comparisons, worst scaled dev {mp.nstr(worst,3)}; control (a -> -delta) dev {mp.nstr(ctl,3)}")
assert worst<1e-30 and ctl>1e-3; print("ALL CHECKS PASSED")
