# (Rule R review probe, committed) traces the saddle level curve Im t = 0 leaving x_e; it must stay outside C.
import mpmath as mp
mp.mp.dps=30
S78=mp.mpf(7)/8
N0=lambda g: g/(2*mp.pi)*mp.log(g/(2*mp.pi*mp.e))+S78
t=lambda x: N0(mp.sqrt(1/x-mp.mpf(1)/4))+mp.mpf(1)/2
def xt(tv):
    y=(tv-mp.mpf(1)/2-S78)/mp.e; g=2*mp.pi*mp.e*mp.exp(mp.re(mp.lambertw(y))); return 1/(g*g+mp.mpf(1)/4)
xe=1/(4*mp.pi**2+mp.mpf(1)/4); x1=xt(1); xc=-1/(4*mp.pi**2*mp.e**2-mp.mpf(1)/4)
r=-xc/2; xm=(x1+xe)/2; c0=(xm-r)/2; R=(xm+r)/2
# second derivative of t at xe
h=mp.mpf('1e-8'); c=(t(xe+h)-2*t(xe)+t(xe-h))/(2*h*h)
tau=mp.mpf(3)/8-mp.mpf('1e-6'); z=xe+1j*mp.sqrt((mp.mpf(3)/8-tau)/c)
out=[]
taus=[mp.mpf(3)/8-mp.mpf(k)/400 for k in range(1,1400)]
for tau in taus:
    try:
        z=mp.findroot(lambda zz: t(zz)-tau, z)
    except Exception as e:
        print("fail at tau",tau); break
    out.append((tau,z,abs(z-c0)<R))
for tau,z,ins in out[::50]+[out[-1]]:
    print("t=",mp.nstr(tau,5)," z=",mp.nstr(z,6), "IN C" if ins else "out", " |z-c0|/R=",mp.nstr(abs(z-c0)/R,4))
print("any inside C:", any(i for _,_,i in out))
