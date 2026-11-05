"""CAUER: the Stieltjes / Cauer-ladder coefficients of a distributed RC line from the Paper IV dictionary (p = 2).  NUMERICAL.

Line: x in [0, 1], series resistance r = e^{-2 gamma x}, shunt capacitance c = e^{2 gamma x} per unit length, far end shorted.
Input impedance Z(s) = 1/(gamma + kappa coth kappa), kappa = sqrt(s + gamma^2) (gamma = 0: tanh sqrt(s)/sqrt(s), Lambert).
Poles s = -lambda_k, lambda_k = q_k^2 + gamma^2, tan q = -q/gamma; residues rho_k = 2(lambda - gamma^2)/(lambda + gamma).
Z(s) = sum_k mu_k/(1 + s x_k), x_k = 1/lambda_k, mu_k = rho_k x_k: the measure mu on reciprocal poles (p = 2, s = 2, alpha = -1/2).
Its S-fraction Z = c_0/(1 + c_1 s/(1 + c_2 s/(1 + ...))) has b_n^2 = c_{2n-1}c_{2n}, a_n = c_{2n} + c_{2n+1}.
 (L)  gamma = 0: c_k = 1/((2k-1)(2k+1)) (Lambert) recovered by Lanczos + Gauss–Jacobi tail.
 (Z)  regularised node zeta values: Z(-1) = -gamma^2/2, Z(-2) = -gamma^4/2 (Hurwitz-regularised via the expansion of lambda_k).
 (K)  kappa-family (k - 1/2)^2 + kappa, constant masses: the N^-3 coefficient is -c kappa, the density ("Jacobian") tilt of
      Conjecture W (w_common.predict: D(x) = 1 - p sum_q R_q x^{q+1/p}); without it the Toda-time layer predicts 0.
 (T)  tapered line: Toda time t_1 = -2Z'(-1) + B_1(mass) + B_1(density) = gamma^2/(2 pi^2), eps_1 = -gamma^2/16 at N^-3;
      N^-5 (relative to the Lambert line, same numerics) = eps_2 + eps_1 g_1; the b_n fit is float64-limited, so the N^-5
      tolerance is 6e-4 max(1, gamma^2) (the measured window spread of the gamma = 0 fit is ~5e-4); N^-6 is not resolvable.
 (C)  Cauer law: c_k (4k^2 - 1) = 1 - gamma^2/(2k^3) + 0/k^4 - (5 gamma^2/4 + 3 gamma^4/8)/k^5 + O(k^-6), both parities."""
import os, sys, math, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
print(f"sha256 {os.path.basename(__file__)}: {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}", flush=True)
import sympy as sp
import numpy as np, mpmath as mp
from lz_common import lanczos
from scipy.special import roots_jacobi
def poles(g,K):
    Q=(np.arange(1,K+1)-0.5)*np.pi
    if g==0: q=Q.copy()
    else:
        q=Q+np.arctan(g/Q)
        for _ in range(60): q=Q+np.arctan(g/q)        # tan(eps)=g/q, q=Q+eps
    lam=q*q+g*g; rho=2*(lam-g*g)/(lam+g)
    return q,lam,rho
def measure(g,K=20000,m=200):
    q,lam,rho=poles(g,K)
    x=1/lam; w=rho*x
    # continuum tail beyond k=K+1/2: nodes lambda ~ pi^2 (k-1/2)^2 (+2g+g^2), density in x: rho/(2 pi sqrt(x)) with rho -> 2
    lamK=(K*np.pi)**2+2*g+g*g; xe=1/lamK
    t,wt=roots_jacobi(m,0.0,-0.5)          # weight (1+t)^{-1/2} on [-1,1]
    xx=xe*(t+1)/2; ww=wt*(xe/2)**0.5/(2*np.pi)*2*(1-g*g*xx)/(1+g*xx)   # sqrt(xe/2)... jacobian for x^{-1/2}
    return np.concatenate([x,xx]),np.concatenate([w,ww])
def cfrac(al,be):
    c=[al[0]]
    for n in range(1,len(be)):
        c.append(be[n]/c[-1]); c.append(al[n]-c[-1])
    return np.array(c)

mp.mp.dps=30
def Zreg(g,j,K=20000,I=None):
    """regularised Z(-j) = sum_k lambda_k^j, lambda_k = q_k^2 + g^2, tan q = -q/g, via the expansion lambda = Q^2 + sum e_i Q^{-2i+2}"""
    I=I or j+6
    L=2*I+10
    def mul(A,B): return [mp.fsum(A[i]*B[n-i] for i in range(n+1)) for n in range(L)]
    def inv1(A):
        R=[mp.mpf(0)]*L; R[0]=1/A[0]
        for n in range(1,L): R[n]=-mp.fsum(A[i]*R[n-i] for i in range(1,n+1))/A[0]
        return R
    def atan_s(Z):
        out=[mp.mpf(0)]*L; P=Z[:]; k=1
        while k<L:
            out=[o+((-1)**((k-1)//2))*pv/k for o,pv in zip(out,P)]
            P=mul(mul(P,Z),Z); k+=2
        return out
    G=mp.mpf(g); eps=[mp.mpf(0)]*L
    for _ in range(L):
        den=[mp.mpf(1)+(eps[n-1] if n>0 else 0) if n==0 else (eps[n-1]) for n in range(L)]
        Zs=[mp.mpf(0)]*L; Zs[1]=G; eps=atan_s(mul(Zs,inv1(den)))
    one_ue=[mp.mpf(1)]+eps[:L-1]
    sq=mul(one_ue,one_ue); base=[s_+(G*G if n==2 else 0) for n,s_ in enumerate(sq)]
    pw=[mp.mpf(1)]+[mp.mpf(0)]*(L-1)
    for _ in range(j): pw=mul(pw,base)
    E=[pw[2*i] for i in range(I+5)]
    # exact lambda_k
    Q=[(k-mp.mpf(1)/2)*mp.pi for k in range(1,K+1)]
    lamk=[]
    for Qk in Q:
        q=Qk+mp.atan(g/Qk) if g else Qk
        for _ in range(200): q=Qk+mp.atan(g/q) if g else Qk
        lamk.append(q*q+g*g)
    reg=mp.fsum(mp.mpf(E[i])*mp.pi**(2*j-2*i)*mp.zeta(2*i-2*j,mp.mpf(1)/2) for i in range(j+1,I+1))
    rem=mp.fsum(lamk[k]**j-mp.fsum(mp.mpf(E[i])*Q[k]**(2*j-2*i) for i in range(I+1)) for k in range(K))
    tail=mp.fsum(mp.mpf(E[i])*mp.pi**(2*j-2*i)*mp.zeta(2*i-2*j,K+mp.mpf(1)/2) for i in range(I+1,I+5))
    return reg+rem+tail

ok = True
x, w = measure(0.0); a0, b0 = lanczos(x, w, 200); c0 = cfrac(a0, b0)
k = np.arange(1, len(c0) + 1, dtype=float); ex = 1/((2*k - 1)*(2*k + 1))
e = float(np.max(np.abs(c0/ex - 1)[:300])); print(f"(L) Lambert: max_k<=300 |c_k(4k^2-1) - 1| = {e:.1e}"); ok &= e < 1e-10
for g in (0.5, 1.0, 2.0):
    z1 = Zreg(g, 1, K=2000, I=11) + mp.mpf(g)**2/2; z2 = Zreg(g, 2, K=2000, I=12) + mp.mpf(g)**4/2
    print(f"(Z) gamma = {g}: Z(-1) + gamma^2/2 = {mp.nstr(z1, 3)}, Z(-2) + gamma^4/2 = {mp.nstr(z2, 3)}"); ok &= abs(z1) < 1e-15 and abs(z2) < 1e-10
from scipy.special import roots_jacobi
c2 = math.pi**2/16; K = 20000; kk = np.arange(1, K + 1)
for kap in (0.1, 0.25, -0.1):
    lam = (kk - 0.5)**2 + kap; xe = 1/(K**2 + kap); t, wt = roots_jacobi(200, 0.0, -0.5)
    al, be = lanczos(np.concatenate([1/lam, xe*(t + 1)/2]), np.concatenate([1/lam, wt*(xe/2)**0.5/2]), 200)
    n = np.arange(1, 200); N = n - 0.25; R = N**2*np.sqrt(be[1:])/c2 - 1
    sel = (n >= 30) & (n <= 180); A = np.vstack([N[sel]**(-m) for m in range(1, 10)]).T; cf = np.linalg.lstsq(A, R[sel], rcond=None)[0]
    print(f"(K) kappa = {kap:+}: N^-3 = {cf[2]:+.7f}, -c kappa = {-c2*kap:+.7f}"); ok &= abs(cf[2] + c2*kap) < 1e-5
n = np.arange(1, 200); N = n - 0.25; R0 = N**2*np.sqrt(b0[1:])*math.pi**2/c2 - 1
g1 = 9/8
for g, p5 in ((0.5, -75/4096), (1.0, -21/256), (2.0, -15/32)):
    x, w = measure(g); al, be = lanczos(x, w, 200); c = cfrac(al, be)
    R = N**2*np.sqrt(be[1:])*math.pi**2/c2 - 1
    sel = (n >= 20) & (n <= 120); A = np.vstack([N[sel]**(-m) for m in range(1, 9)]).T
    cf = np.linalg.lstsq(A, (R - R0)[sel], rcond=None)[0]
    print(f"(T) gamma = {g}: N^-3 {cf[2]:+.6f} (pred {-g*g/16:+.6f}); N^-5 {cf[4]:+.6f} (pred eps2 + eps1 g1 = {p5:+.6f})")
    ok &= abs(cf[2] + g*g/16) < 1e-5 and abs(cf[4] - p5) < 6e-4*max(1, g*g)
    d = c/c0 - 1 + g*g/(2*k**3); sel = (k >= 20) & (k <= 320)
    A = np.vstack([k[sel]**(-m) for m in (5, 6, 7, 8, 9)]).T; d5 = np.linalg.lstsq(A, d[sel], rcond=None)[0][0]
    d34 = [np.linalg.lstsq(np.vstack([k[(k%2 == par) & sel]**(-m) for m in (2, 3, 4, 5, 6)]).T, (c/c0 - 1)[(k%2 == par) & sel], rcond=None)[0] for par in (0, 1)]
    print(f"(C) gamma = {g}: k^-3 (even, odd) = {d34[0][1]:+.5f}, {d34[1][1]:+.5f} (pred {-g*g/2:+.5f}); k^-4 = {d34[0][2]:+.4f}, "
          f"{d34[1][2]:+.4f} (pred 0); k^-5 = {d5:+.4f} (pred {-(5/4)*g*g - (3/8)*g**4:+.4f})")
    ok &= abs(d34[0][1] + g*g/2) < 1e-3*max(1, g*g) and abs(d5 + (5/4)*g*g + (3/8)*g**4) < 1e-3*max(1, g**4)
print("ALL PASSED" if ok else "NOT ALL PASSED")
