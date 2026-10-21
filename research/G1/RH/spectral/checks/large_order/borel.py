import mpmath as mp, sys
mp.mp.dps=60
fn=sys.argv[1]
f={}
for line in open(fn):
    parts=line.split()
    if len(parts)==2 and parts[0].isdigit(): f[int(parts[0])]=mp.mpf(parts[1])
K=max(f)
# Borel in t: B(t) = sum_k f_{2k} t^{2k} / Gamma(2k)   (k>=1); work in s = t^2: B(s) = sum f_{2k} s^k / (2k-1)!
c=[mp.mpf(0)]+[f[2*k]/mp.factorial(2*k-1) for k in range(1,K//2+1)]
for (L,M) in [(K//4, K//4),(K//4-1,K//4),(K//4,K//4-1)]:
    if L+M+1>len(c): continue
    try:
        pq=mp.pade(c[:L+M+1],L,M)
    except Exception as e:
        print("pade fail",e); continue
    q=pq[1]
    roots=mp.polyroots(q[::-1],maxsteps=200,extraprec=200)
    rs=sorted(roots,key=lambda r: abs(r))
    print(f"[{L}/{M}] Borel s-plane poles (s = t^2), nearest:", [mp.nstr(r,8) for r in rs[:4]])
    print("     t = sqrt(s):", [mp.nstr(mp.sqrt(r),8) for r in rs[:4]], " |t|:", [mp.nstr(abs(mp.sqrt(r)),6) for r in rs[:4]])
# ratio test
for k in range(K//2-4,K//2):
    r=f[2*k+2]/f[2*k]; print(2*k, "ratio f_{2k+2}/f_{2k} / ((2k)(2k+1)):", mp.nstr(r/((2*k)*(2*k+1)),8))
