"""Plan 20 NUMERICAL probe for RHFREE2.md §2 (hypothesis NA): ratio dist(h_z, V)/‖h_z‖ on synthetic critical
configurations (GUE-like, Poisson) with one probed off-line pair at height y (normalized units), optionally with 5 extra
off-line g_w in V. Grid quadrature + QR least squares (double precision). Seed 20. Not a proof."""
# Probe: d_z := dist(h_z, V), V = span{f_x (critical), g_w (off-line)}; ratio d_z/||h_z|| vs λ, y, configuration.
import numpy as np
rng=np.random.default_rng(20)
def gue(n):
    M=3*n; H=rng.normal(size=(M,M))+1j*rng.normal(size=(M,M)); H=(H+H.conj().T)/2
    e=np.linalg.eigvalsh(H)/np.sqrt(M); R=np.sqrt(2.)
    F=lambda x:(lambda x:M*(0.5+(x*np.sqrt(1-x*x)+np.arcsin(x))/np.pi))(np.clip(x/R,-1,1))
    u=F(e); u=np.sort(u[np.argsort(np.abs(u-M/2))[:n]]); return u-u.mean()
def eta(u,lam): return np.sqrt(np.clip((1/lam)*np.cos(np.pi*u/(2*lam))**2,0,None))*(np.abs(u)<lam)
def run(lam,y,n=120,kind='gue',extra_off=0):
    xs=gue(n) if kind=='gue' else np.cumsum(rng.exponential(1,n))-n/2
    ug=np.linspace(-lam,lam,16001); w=np.full(ug.size,ug[1]-ug[0]); sw=np.sqrt(w); e=eta(ug,lam)
    f=lambda z: sw*e*np.exp(-2j*np.pi*ug*z)
    a=0.3  # Re position of the probed off-line zero (between points)
    z=a+1j*y
    h=(f(z)-f(np.conj(z)))/(2j)
    cols=[f(x) for x in xs]
    for _ in range(extra_off):
        wz=rng.uniform(-n/3,n/3)+1j*rng.uniform(0.05,y)
        cols.append((f(wz)+f(np.conj(wz)))/2)
    cols.append((f(z)+f(np.conj(z)))/2)   # g_z itself is in V
    Vm=np.array(cols).T
    Q,_=np.linalg.qr(Vm)
    r=h-Q@(Q.conj().T@h)
    return np.linalg.norm(r)/np.linalg.norm(h), np.linalg.norm(h)**2
for kind in ['gue','poisson']:
  for lam in [0.25,0.5,1,2,4]:
    row=[]
    for y in [0.02,0.1,0.3,1.0]:
        rat,hn=run(lam,y,kind=kind); row.append(f"y={y}: d/|h|={rat:.3f} |h|²={hn:.2e}")
    print(kind,f"λ={lam}"," | ".join(row))
print("with 5 extra off-line g_w in V:")
for lam in [0.5,1,2]:
    print(f"λ={lam}"," | ".join(f"y={y}: {run(lam,y,extra_off=5)[0]:.3f}" for y in [0.1,0.3,1.0]))
