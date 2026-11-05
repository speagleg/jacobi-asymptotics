"""JZC M4 §8: the zeta layer is the Toda flow of the integer layer (NUMERICAL, 50 digits, KORD = 6; exact up to the
central-difference error). Model quantities (c = 1, m4_rh4.run(..., want_a=True)): b_n = n^{-p}B(n), alpha_n = 2n^{-p}A(n)
(integer layer). The scaled tilt mu_j (weight e^{-mu_j z^j}, z = n^p x) is the Toda time t_j = -mu_j n^{jp}. Toda hierarchy
(exact for every measure; JZC_M4 §8): d_{t_j} log h_n = (J^j)_{nn}, b_n^2 = h_n/h_{n-1}. Checks, as formal series in 1/n:
 (T1) d_{mu_1}(n^p b_n) = -(1/2) n^p (alpha_n - alpha_{n-1}) n^p b_n;
 (T2) (1/2) d_{mu_1}^2 (n^p b_n) = (1/2) n^{2p} d_t^2 (n^p b_n), d_t^2 log b_n^2 = b_{n+1}^2 - 2b_n^2 + b_{n-1}^2, d_t log b_n^2 = alpha_n - alpha_{n-1};
 (T3) d_{mu_2}(n^p b_n) = -(1/2) n^{2p}[(J^2)_{nn} - (J^2)_{n-1,n-1}] n^p b_n, (J^2)_{nn} = alpha_n^2 + b_n^2 + b_{n+1}^2;
 (A)  the diagonal integer layer in natural form, (M/n)^p A(n) with M = n + alpha/2 + 1 = N + 1/2, has no odd powers of 1/M
      (KORD = 8)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KORD", "6")
import mpmath as mp
import m4_rh4 as M
from spec_common import Checks
mp.mp.dps = 50; C_ = Checks(); S = M.S; K = M.KORD
def shifted(a, p, s, power):
    S.HI, h0 = K, S.HI
    x = S(1, [1]); one = S.const(1); inv = x*(one + x*s).inv()
    tot = S.const(a[0]); q = S.const(1)
    for k in range(1, K + 1): q = q*inv; tot = tot + q*a[k]
    out = (one + x*s).powr(-power)*tot; S.HI = h0
    return [mp.re(out.get(k)) for k in range(K + 1)]
mul = lambda a, b: [sum(a[i]*b[k - i] for i in range(k + 1)) for k in range(len(a))]
add = lambda *xs: [sum(t) for t in zip(*xs)]
sc = lambda a, f: [f*x for x in a]
for p, al in [(mp.mpf('1.5'), mp.mpf('0.3')), (mp.mpf('0.6'), mp.mpf('-0.4')), (mp.mpf('2.7'), mp.mpf('1.1'))]:
    lab = f"p={mp.nstr(p, 3)} al={mp.nstr(al, 3)}"
    B, _, A = M.run(p, al, want_a=True); B2 = mul(B, B)
    Am1 = shifted(A, p, -1, p); B2p1 = shifted(B2, p, 1, 2*p); B2m1 = shifted(B2, p, -1, 2*p)
    D1 = sc(add(A, sc(Am1, -1)), 2); D2 = add(B2p1, sc(B2, -2), B2m1)
    h = mp.mpf(10)**-15
    dp, _ = M.run(p, al, mu={1: h}); dm, _ = M.run(p, al, mu={1: -h}); e1 = [(x - y)/(2*h) for x, y in zip(dp, dm)]
    T1 = sc(mul(D1, B), -mp.mpf(1)/2)
    C_.check(f"{lab}: (T1) mu_1 layer = Toda", float(max(abs(x - y) for x, y in zip(e1, T1))), 0.0, 1e-20)
    h2 = mp.mpf(10)**-10
    dp, _ = M.run(p, al, mu={1: h2}); dm, _ = M.run(p, al, mu={1: -h2}); e11 = [(x + y - 2*z)/(2*h2*h2) for x, y, z in zip(dp, dm, B)]
    T2 = sc(mul(B, add(sc(D2, mp.mpf(1)/2), sc(mul(D1, D1), mp.mpf(1)/4))), mp.mpf(1)/2)
    C_.check(f"{lab}: (T2) mu_1^2 layer = Toda", float(max(abs(x - y)/(1 + abs(y)) for x, y in zip(e11, T2))), 0.0, 1e-12)
    J2 = add(mul(sc(A, 2), sc(A, 2)), B2, B2p1); J2m1 = shifted(J2, p, -1, 2*p)
    dp, _ = M.run(p, al, mu={2: h}); dm, _ = M.run(p, al, mu={2: -h}); e2 = [(x - y)/(2*h) for x, y in zip(dp, dm)]
    T3 = sc(mul(B, add(J2, sc(J2m1, -1))), -mp.mpf(1)/2)
    C_.check(f"{lab}: (T3) mu_2 layer = Toda hierarchy", float(max(abs(x - y)/(1 + abs(y)) for x, y in zip(e2, T3))), 0.0, 1e-18)
    print(f"{lab}: mu1 {[mp.nstr(x, 10) for x in e1]}\n   mu1^2 {[mp.nstr(x, 10) for x in e11]}\n   mu2 {[mp.nstr(x, 10) for x in e2]}", flush=True)
os.environ["KORD"] = "8"
import importlib; M8 = importlib.reload(M); S8 = M8.S
for p, al in [(mp.mpf('1.5'), mp.mpf('0.3')), (mp.mpf('0.6'), mp.mpf('-0.4')), (mp.mpf(2), mp.mpf(-0.5))]:
    B, _, A = M8.run(p, al, want_a=True); sh = al/2 + 1
    S8.HI, h0 = M8.KORD, S8.HI
    x = S8(1, [1]); one = S8.const(1); inv_n = x*(one - x*sh).inv(); tot = S8.const(A[0]); q = S8.const(1)
    for k in range(1, M8.KORD + 1): q = q*inv_n; tot = tot + q*A[k]
    F = (one - x*sh).powr(-p)*tot; S8.HI = h0
    G = [mp.re(F.get(k)) for k in range(M8.KORD + 1)]
    print(f"p={mp.nstr(p, 3)} al={mp.nstr(al, 3)}: diagonal layer in M = N + 1/2: {[mp.nstr(v, 10) for v in G]}", flush=True)
    C_.check(f"p={mp.nstr(p, 3)} al={mp.nstr(al, 3)}: (A) diagonal layer even in M = N + 1/2", float(max(abs(G[k]) for k in range(1, M8.KORD + 1, 2))), 0.0, 1e-30)
C_.finish()
