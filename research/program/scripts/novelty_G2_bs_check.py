import mpmath as mp
mp.mp.dps=60
def logH_formula(n,l,nu=mp.mpf(1)/2):
    if l in (0,1):
        s=-2*n*(n+l)*mp.log(2)+sum((k-2*n-l)*mp.log(nu+k) for k in range(1,2*n+l))
    elif l==2:
        s=-2*n*(n+2)*mp.log(2)+mp.log(n+1)+mp.log(n+nu+1)+sum((k-2*n-2)*mp.log(nu+k) for k in range(1,2*n+2))
    elif l==3:
        s=-2*n*(n+3)*mp.log(2)+sum((k-2*n-3)*mp.log(nu+k) for k in range(1,2*n+3))
    return s
def logdet_zeta_formula(n,l):
    # entries zeta(2(i+j)+2l-2) = pi^{2(i+j)+2l-2} sigma ; det scales by pi^{sum_i (2i + (2l-2)/2)*2}
    expo=sum(2*(2*i)+ (2*l-2) for i in range(1,n+1))  # row factor pi^{2i+l-1}, col factor same
    expo=sum(2*i+l-1 for i in range(1,n+1))*2
    return logH_formula(n,l)+expo*mp.log(mp.pi)
def logdet_zeta_direct(n,l):
    M=mp.matrix(n,n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            M[i-1,j-1]=mp.zeta(2*(i+j)+2*l-2)
    return mp.log(mp.det(M))
for l in range(4):
    for n in (2,4,6):
        print(l,n,mp.nstr(logdet_zeta_formula(n,l),15),mp.nstr(logdet_zeta_direct(n,l),15))
c2=mp.mpf(1)/4*(mp.pi/(2*(mp.sqrt(mp.pi)/2*mp.gamma(mp.mpf(1)/2+mp.mpf(1)/2)/mp.gamma(mp.mpf(1)/2+1))))**2
print('c(2)=',c2, mp.pi**2/16)
kap=3+mp.log(c2)
for l in range(4):
    for n in (1000,4000,16000):
        v=(logdet_zeta_formula(n,l)+2*n*n*mp.log(n))/n**2
        print(l,n,mp.nstr(v,12),mp.nstr(kap,12))
