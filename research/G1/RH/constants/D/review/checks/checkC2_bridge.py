# Bridge check of D.md §3.4: lim_n (A_n(1,2) - MZ_n) = (3/4)log2 - (3/2)log pi - 2 zeta'(-1), and Pi(1) + bridge = closed log A0.
import mpmath as mp
mp.mp.dps = 40
p = 1; s = 2; c = mp.mpf(1)/2; z = mp.mpf(1); e = -mp.mpf(11)/12
def A(n):
    n = mp.mpf(n)
    return (n-1)*(mp.log(2*mp.pi) + z*mp.log(c)) + (n**2-1)*mp.log(c) - z*mp.loggamma(n) - 2*mp.log(mp.barnesg(n+1)) + e*mp.log(n)
MZ = lambda n: -(n+mp.mpf(1)/2)**2*(mp.log(2*n+1) - mp.mpf(3)/2)
claim = mp.mpf(3)/4*mp.log(2) - mp.mpf(3)/2*mp.log(mp.pi) - 2*mp.zeta(-1, derivative=1)
for n in (10**3, 10**4, 10**5):
    print(n, mp.nstr(A(n) - MZ(n) - claim, 5))
logA = mp.log(mp.glaisher)
Pi1 = mp.mpf(1)/4 - 5*logA + mp.log(mp.pi) + mp.mpf(5)/12*mp.log(2) - mp.mpf(3)/8*mp.log(3)
K12 = Pi1 - mp.log(mp.barnesg(1)) + 0 + (mp.log(2*mp.pi*3)/2 + mp.mpf(3)/2*mp.log(c))*1
cand = mp.mpf(1)/12 + mp.log(2)/6 + mp.log(3)/8 - 3*logA
print('K(1,2)+bridge - log(closed A0) =', mp.nstr(K12 + claim - cand, 5))
