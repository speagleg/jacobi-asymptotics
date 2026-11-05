"""Reviewer spot check (Rule R, JZC_TODA): derivatives in the tilt time tau of the Jacobi coefficients of the INFINITE tilted
lattice sigma_tau = exp(tau x^j) sigma_{p,s}, at tau = 0, in ball arithmetic, against the engine layers (Theorem T (i) / Lemma T.A).
Moments of sigma_tau as power series in tau: m_k(tau) = sum_r tau^r/r! zeta(s + p(k + j r)) (exact Taylor coefficients, Arb zeta).
Chebyshev algorithm over truncated power series (order 2) with arb coefficients -> B_n(tau) = b_n^2 as series.
Prediction: n^p b_n/c = sum_beta e^beta Bcoef_beta(n), e_a = C(2j_a, j_a) c^{j_a} mu_a, mu_a = 2 zeta(-j_a p)/(j_a n^{j_a p}) - tau_a n^{-j_a p}.
Usage: rv_tilted_lattice.py ENGINE_JSON p s jtilt "j1,j2" NMAX"""
import sys, json, math
from flint import arb, fmpq, ctx
import mpmath as mp
import sympy as sp
sys.path.insert(0, '/home/claude/speagleg/jacobi-asymptotics/src')
from jacobi_asym.certify.constants import c_p

mp.mp.dps = 60
fn, P, S, JT, JS, NMAX = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), tuple(int(x) for x in sys.argv[5].split(',')), int(sys.argv[6])
DL = sys.argv[7] if len(sys.argv) > 7 else '0'
dq = fmpq(*map(int, DL.split('/'))) if '/' in DL else fmpq(int(DL))
pq = fmpq(*map(int, P.split('/'))) if '/' in P else fmpq(int(P)); sq = fmpq(*map(int, S.split('/'))) if '/' in S else fmpq(int(S))
pf = mp.mpf(int(pq.p)) / int(pq.q); sf = mp.mpf(int(sq.p)) / int(sq.q); alf = (sf - 1) / pf - 1
ORD = 3   # series length in tau (orders 0, 1, 2)

def smul(a, b): return [sum((a[i] * b[k - i] for i in range(k + 1)), arb(0)) for k in range(ORD)]
def ssub(a, b): return [x - y for x, y in zip(a, b)]
def sdiv(a, b):
    q = []
    for k in range(ORD):
        t = a[k] - sum((q[i] * b[k - i] for i in range(k)), arb(0))
        q.append(t / b[0])
    return q

def run(bits, n):
    ctx.prec = bits
    Pa, Sa = arb(pq), arb(sq)
    Aa = 1 + arb(dq)
    mom = [[arb.zeta(Sa + Pa * (k + JT * r), Aa) / math.factorial(r) for r in range(ORD)] for k in range(2 * n + 2)]
    N = n + 1
    zero = [arb(0)] * ORD
    sig_prev = [zero] * (2 * N); sig = [list(m) for m in mom[:2 * N]]
    A = [sdiv(mom[1], mom[0])]; B = [mom[0]]
    for k in range(1, N):
        new = [zero] * (2 * N)
        for l in range(k, 2 * N - k):
            new[l] = ssub(ssub(sig[l + 1], smul(A[k - 1], sig[l])), smul(B[k - 1], sig_prev[l]))
        A.append(ssub(sdiv(new[k + 1], new[k]), sdiv(sig[k], sig[k - 1])))
        B.append(sdiv(new[k], sig[k - 1]))
        sig_prev, sig = sig, new
    return A, B

# engine layers
D = json.load(open(fn)); ps, als, bes = sp.Symbol('p'), sp.Symbol('alpha'), sp.Symbol('beta')
lay = {}
# exact alpha as rational: alpha = (s-1)/p - 1
alq = (sq - 1) / pq - 1
for key, lst in D['e'].items():
    a, b = map(int, key.split(','))
    lay[(a, b)] = [mp.mpf(sp.Rational(str(sp.sympify(s, locals={'p': ps, 'alpha': als, 'beta': bes}).subs({ps: sp.Rational(int(pq.p), int(pq.q)), als: sp.Rational(int(alq.p), int(alq.q)), bes: sp.Rational(int(alq.p), int(alq.q)) + 2 * sp.Rational(int(dq.p), int(dq.q))})))) if True else 0 for s in lst]
KORD = len(lay[(0, 0)]) - 1
cc = mp.mpf(c_p(pq, 300).mid().str(70, radius=False))
Cb = lambda j: mp.binomial(2 * j, j)

def predict(n, tau):
    n = mp.mpf(n)
    dlf = mp.mpf(int(dq.p)) / int(dq.q)
    mu = [2 * mp.zeta(-j * pf, 1 + dlf) / (j * n ** (j * pf)) - (tau if j == JT else 0) * n ** (-j * pf) for j in JS]
    e = [Cb(j) * cc ** j * m for j, m in zip(JS, mu)]
    return sum(e[0] ** a * e[1] ** b * sum(lay[(a, b)][m] * n ** (-m) for m in range(KORD + 1)) for (a, b) in lay)

print(f"delta = {DL}, p = {P}, s = {S}, alpha = {alq}, tilt x^{JT}, layers {fn.split('/')[-1]} exponents {JS}, KORD {KORD}; c(p) = {mp.nstr(cc, 20)}")
bits = 2048
for n in list(range(6, NMAX + 1, 2)):
    while True:
        A, B = run(bits, n)
        if all(x.rel_accuracy_bits() > 120 for x in B[n]): break
        bits *= 2
    Bn = [mp.mpf(x.mid().str(50, radius=False)) for x in B[n]]
    # b_n = sqrt(B_n) as series: b0 = sqrt(B0), b1 = B1/(2 b0), b2 = (B2 - b1^2)/(2 b0)  [B2 = coefficient of tau^2]
    b0 = mp.sqrt(Bn[0]); b1 = Bn[1] / (2 * b0); b2 = (Bn[2] - b1 ** 2) / (2 * b0)
    sc = mp.mpf(n) ** pf / cc
    F0, F1, F2 = b0 * sc, b1 * sc, 2 * b2 * sc          # F2 = second tau-derivative
    h = mp.mpf(10) ** -12
    P0 = predict(n, 0); P1 = (predict(n, h) - predict(n, -h)) / (2 * h); P2 = (predict(n, h) - 2 * P0 + predict(n, -h)) / h ** 2
    lead1 = -Cb(JT) * cc ** JT * mp.mpf(n) ** (-JT * pf) * (pf * JT / 2) / n
    print(f"n={n:3d} bits={bits:6d}  F0-P0={mp.nstr(F0 - P0, 5):>12}  dF/dtau={mp.nstr(F1, 12):>18} pred={mp.nstr(P1, 12):>18} "
          f"relerr1={mp.nstr((F1 - P1) / lead1, 4):>11}  F1/lead={mp.nstr(F1 / lead1, 10)}  d2F={mp.nstr(F2, 10):>14} pred2={mp.nstr(P2, 10):>14} rel2={mp.nstr((F2 - P2) / P2, 4) if P2 != 0 else "n/a"}", flush=True)
