import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from spec_airy import TC
mp.mp.dps = 40; pm = mp.mpf(2)/3; C = (3*mp.pi/2)**pm; q = (3*mp.pi/2)**-2
def Zneg(j, kex):
    poly = [TC[i]*q**i for i in range(6)]; g = [mp.mpf(1)] + [mp.mpf(0)]*5
    for _ in range(j): g = [sum(g[a]*poly[i-a] for a in range(i+1)) for i in range(6)]
    reg = sum(g[i]*mp.zeta(2*i - j*pm, mp.mpf(3)/4) for i in range(6))
    return reg + sum((-mp.airyaizero(k)/C)**j - sum(g[i]*(k-mp.mpf(1)/4)**(j*pm-2*i) for i in range(6)) for k in range(1, kex+1))
for j in range(0, 6):
    print(j, mp.nstr(Zneg(j, 150), 12), mp.nstr(Zneg(j, 300), 12))
