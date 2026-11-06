# Rule N check for NOVELTY_C.md §2.2a. Source: Fukuhara-Yang arXiv:math/0608372v2, App. A (Krattenthaler), Thm A, read first-hand (pdftotext).
# Krattenthaler Thm A (Fukuhara-Yang App. A) -> exact D_n for sigma_{2,s}, s=2,4,6 ; compare h_n with Theorem C.
from mpmath import mp, mpf, pi, log, loggamma, exp, zeta, bernoulli, factorial, matrix, det
mp.dps=40


def logD(n,s):
    n=int(n)
    if n==0: return mpf(0)
    # zeta(2k) = (-1)^{k+1} B_{2k}(2pi)^{2k}/(2(2k)!); Hankel of zeta(2(i+j)+s): sign (-1)^{i+j} cancels
    if s==2:   # det B_{2i+2j+2}/(2i+2j+2)!  = 4^{-n^2} prod_{i=1}^{2n-1}(2i+1)^{-(2n-i)}
        L=-n*n*log(4)-sum((2*n-i)*log(2*i+1) for i in range(1,2*n))
        sc=2*n*n            # (2pi)^{sum(2(i+j)+2)} over diagonal: 2n + 4*n(n-1)/2*... -> total exponent
    elif s==4:  # (-1)^n 4^{-n^2-n} 9^{-n} prod (2i+3)^{-(2n-i)}
        L=-(n*n+n)*log(4)-n*log(9)-sum((2*n-i)*log(2*i+3) for i in range(1,2*n))
        sc=2*n*n+2*n
    elif s==6:
        L=-(n*n+2*n)*log(4)+log((n+1)*(2*n+3))-sum((2*n+2-i)*log(2*i+1) for i in range(1,2*n+2))
        sc=2*n*n+4*n
    return L + sc*log(2*pi) - n*log(2)
# check exactness at small n against direct determinant
for s in (2,4,6):
    for n in (1,2,3,5):
        M=matrix(n,n)
        for i in range(n):
            for j in range(n): M[i,j]=zeta(2*(i+j)+s)
        print(s,n, mp.nstr(log(det(M))-logD(n,s),5))
c=pi**2/16; p=2
def logC(n,s): return log(2*pi/p)+(2*n+1)*log(c)+(s-1)*(log(c)/p-log(n))-2*p*loggamma(n+1)
for s in (2,4,6):
    for n in (10,100,1000,4000):
        r=exp(logD(n+1,s)-logD(n,s)-logC(n,s)); print('s',s,'n',n,'h_n/ThmC',mp.nstr(r,15),' n(r-1)',mp.nstr(n*(r-1),8))
