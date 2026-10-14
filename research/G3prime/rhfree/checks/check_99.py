"""Plan 22 NUMERICAL check of the proof of (C8) (9.9) in RH99.md (actual primes; no RH needed for the identities).
[1] Mellin identity ∫_0^∞ a_u(x)u^{-it}du = 2x^{1-it}/((1/2+it)(3/2-it)).
[2] Exact calculus identity ∫_0^∞ a_y(x)²D(y)²dy/y = 4x³∫_0^∞... = 4x³∫_x^∞ J(y)y^{-5}dy, J(y) := ∫_0^y D².
[3] L(x,T) vs 4x³∫_x^∞ I(y,δ)y^{-5}dy, and the remainder against the bound of Lemma 99: |L − main| ≤ 2√(main·E) + E,
    E := ∫R²dy/y with R := Δ − a_y D computed exactly.
Truncation: y ≤ Ymax (tail weight (x/y)³)."""
import numpy as np, mpmath as mp
from scipy.integrate import quad
# [1]
x0 = 7.3
for t in [0.0, 1.7, 25.0]:
    f = lambda u: min((u/x0)**0.5, (x0/u)**1.5)
    re = quad(lambda u: f(u)*np.cos(t*np.log(u)), 0, x0, limit=400)[0] + quad(lambda u: f(u)*np.cos(t*np.log(u)), x0, np.inf, limit=4000)[0]
    im = -quad(lambda u: f(u)*np.sin(t*np.log(u)), 0, x0, limit=400)[0] - quad(lambda u: f(u)*np.sin(t*np.log(u)), x0, np.inf, limit=4000)[0]
    rhs = complex(2*mp.power(x0, 1-1j*t)/((0.5+1j*t)*(1.5-1j*t)))
    print(f"[1] t={t:5.1f}: |lhs-rhs|/|rhs| = {abs(complex(re,im)-rhs)/abs(rhs):.1e}" + ("  (oscillatory quad; t=25 is loose)" if t>20 else ""))
# primes / Λ
Ymax = 4_000_000
sieve = np.ones(Ymax*2+2, bool); sieve[:2] = False
for p in range(2, int((Ymax*2+2)**0.5)+1):
    if sieve[p]: sieve[p*p::p] = False
Lam = np.zeros(Ymax*2+2)
for p in np.nonzero(sieve)[0]:
    pk = p
    while pk < Lam.size: Lam[pk] = np.log(p); pk *= p
psi = np.cumsum(Lam)
def run(x, T):
    kap = np.log1p(1/T); d = 1/T
    n = np.arange(Lam.size); a = np.where(n > 0, np.minimum(np.sqrt(np.maximum(n,1e-300)/x), (x/np.maximum(n,1))**1.5), 0)
    cumLa = np.cumsum(Lam*a)
    ys = np.exp(np.linspace(np.log(0.5), np.log(Ymax), 400000)); lny = np.log(ys)
    def A(u):  # ∫_0^u a_v(x) dv
        u = np.asarray(u, float)
        return np.where(u <= x, (2/3)*u**1.5/x**0.5, (2/3)*x + 2*x**1.5*(x**-0.5 - u**-0.5))
    hi = ys*np.exp(kap)
    Delta = cumLa[np.floor(hi).astype(int)] - cumLa[np.floor(ys).astype(int)] - (A(hi) - A(ys))
    D = psi[np.floor(hi).astype(int)] - psi[np.floor(ys).astype(int)] - d*ys
    ay = np.minimum(np.sqrt(ys/x), (x/ys)**1.5)
    Rr = Delta - ay*D
    L = np.trapezoid(Delta**2, lny); M0 = np.trapezoid(ay**2*D**2, lny); E = np.trapezoid(Rr**2, lny)
    # main via J
    J = np.concatenate([[0], np.cumsum(0.5*(D[1:]**2 + D[:-1]**2)*np.diff(ys))])
    m = ys >= x
    M1 = 4*x**3*np.trapezoid(J[m]*ys[m]**-5, ys[m]) + J[-1]*x**3/ys[-1]**4   # + boundary from truncation
    print(f"[2/3] x={x:8.0f} T={T:5.0f}: ∫a²D²dy/y={M0:.6e}  4x³∫J y⁻⁵(+bdry)={M1:.6e}  rel diff {abs(M0-M1)/M0:.1e} | "
          f"L={L:.6e}  |L−main|/main={abs(L-M0)/M0:.2e}  bound (2√(ME)+E)/main={(2*np.sqrt(M0*E)+E)/M0:.2e}  "
          f"E/(κ²x log⁴x)={E/(kap**2*x*np.log(x)**4):.2e}  main/(xδ log T)={M0/(x*d*np.log(T)):.3f}")
for (x, T) in [(2e3, 100), (2e4, 100), (2e4, 1000), (1e5, 1000), (1e5, 3000)]:
    run(x, T)
