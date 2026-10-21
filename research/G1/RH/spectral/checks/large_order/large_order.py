import sys, os, time; sys.path.insert(0,'/home/claude/speagleg/jacobi-asymptotics/research/G1/RH/spectral/checks')
import m4_rh4 as M, mpmath as mp
mp.mp.dps=int(os.environ.get("DPS","80"))
p=mp.mpf(os.environ.get("PP","3")); nu=mp.mpf(os.environ.get("NU","0.3"))
t=time.time(); d,_=M.run(p,nu); f=M.natural(d,p,nu)
print(f"KORD={M.KORD} SHI={M.S.HI} dps={mp.mp.dps} p={p} nu={nu} ({time.time()-t:.0f}s)")
for k in range(2,M.KORD+1,2): print(k, mp.nstr(f[k],25))
print("odd max", mp.nstr(max(abs(f[k]) for k in range(1,M.KORD+1,2)),3))
