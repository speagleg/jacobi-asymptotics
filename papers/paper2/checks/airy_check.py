"""Paper 2, Lemma (Airy parametrix) in Section 6: numerical check of the soft-edge construction.

Model data (any choice with the structural properties used in the lemma; here c = 1, so the soft edge is 4c = 4):
  f_r(z)   = (z - 4c)(1 + 0.2 (z - 4c))                      conformal near 4c, f_r(4c) = 0, f_r'(4c) > 0, real on R
  phi~(z)  = -(2/3) f_r(z)^{3/2}                             principal power (cut f_r^{-1}((-inf, 0]))
  -omega   = (4c/Ups) * exp(R(z) gq(z)),  Ups = (sqrt z + sqrt(z - 4c))^2,  R = sqrt z sqrt(z - 4c),  gq real polynomial
             (so omega_+ omega_- = 1 on the band, -omega > 0 on (4c, oo), as for omega = D_W^2/W_0)
  (-omega)^{1/2} = 2 sqrt(c)/(sqrt z + sqrt(z - 4c)) * exp(R gq / 2)
  P0inf    = [[(a + 1/a)/2, (a - 1/a)/(2i)], [-(a - 1/a)/(2i), (a + 1/a)/2]],  a = ((z - 4c)/z)^{1/4}
Construction checked (paper's notation):
  y0 = (Ai(z), Ai'(z)),  y+ = (Ai(w2 z), w2 Ai'(w2 z)),  y- = (Ai(w z), w Ai'(w z)),  w = e^{2 pi i/3}, w2 = w^2
  Psi_I  = e^{-i pi s3/4} k (y+, w y0),  k = sqrt(2 pi) e^{i pi/12}   (region Re z > 4c, Im z > 0; regions II, III, IV
           counterclockwise; explicit columns in Psi() below)
  Psi_II = Psi_I [[1,1],[0,1]],  Psi_III = Psi_II J^{-1},  Psi_IV = Psi_I [[1,0],[1,1]]
  A_r    = P0inf (-omega)^{-s3/2} M^{-1} f_r^{s3/4},   M = [[1, i],[i, 1]]/sqrt 2
  Phat_r = A_r n^{s3/6} Psi(n^{2/3} f_r) ((-omega)^{1/2} e^{n phi~})^{s3}
Checks: jumps of Phat_r equal those of Q (Frame Proposition (F1)) on the band, on (4c, 4c+eps), on the two vertical
segments; det = 1; A_r has no jump on the band and is bounded near 4c; M J M^{-1} = diag(-i, i); matching
Phat_r P0inf^{-1} - I = O(1/n) on |z - 4c| = eps.
Run: <jacobi-asymptotics>/.venv/bin/python -I papers/paper2/checks/airy_check.py"""
import mpmath as mp

mp.mp.dps = 30
c = mp.mpf(1)
E = 4 * c
I2 = mp.eye(2)
J = mp.matrix([[0, 1], [-1, 0]])
Mm = mp.matrix([[1, 1j], [1j, 1]]) / mp.sqrt(2)


def s3pow(x):
    return mp.matrix([[x, 0], [0, 1 / x]])


def gq(z):
    return mp.mpf('0.3') + mp.mpf('0.1') * z


def sq(z):
    return mp.sqrt(z)  # principal


def fr(z):
    return (z - E) * (1 + mp.mpf('0.2') * (z - E))


def phit(z):
    return -mp.mpf(2) / 3 * mp.power(fr(z), mp.mpf(3) / 2)


def R(z):
    return sq(z) * sq(z - E)


def mom_half(z):  # (-omega)^{1/2}
    return 2 * mp.sqrt(c) / (sq(z) + sq(z - E)) * mp.exp(R(z) * gq(z) / 2)


def omega(z):
    return -mom_half(z) ** 2


def P0(z):
    a = mp.power(z - E, mp.mpf(1) / 4) / mp.power(z, mp.mpf(1) / 4)
    return mp.matrix([[(a + 1 / a) / 2, (a - 1 / a) / 2j], [-(a - 1 / a) / 2j, (a + 1 / a) / 2]])


def yvec(mult, zeta):
    return [mp.airyai(mult * zeta), mult * mp.airyai(mult * zeta, derivative=1)]


def Psi(zeta, region):
    """Explicit columns in each region (no cancellation):
    I: (k y+, k w y0), II: (k y+, -k w^2 y-), III: (-k w^2 y-, -k y+), IV: (-k w^2 y-, k w y0), times e^{-i pi s3/4}."""
    w = mp.exp(2j * mp.pi / 3)
    k = mp.sqrt(2 * mp.pi) * mp.exp(1j * mp.pi / 12)
    yp, ym, y0 = yvec(w * w, zeta), yvec(w, zeta), yvec(1, zeta)
    cols = {'I': ([k * t for t in yp], [k * w * t for t in y0]),
            'II': ([k * t for t in yp], [-k * w * w * t for t in ym]),
            'III': ([-k * w * w * t for t in ym], [-k * t for t in yp]),
            'IV': ([-k * w * w * t for t in ym], [k * w * t for t in y0])}[region]
    X = mp.matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])
    return s3pow(mp.exp(-1j * mp.pi / 4)) * X


def Psi_by_jumps(zeta, region):
    """The same matrices generated from region I by the constant jumps (checked against Psi below)."""
    P = Psi(zeta, 'I')
    return {'I': P, 'II': P * U1, 'III': P * U1 * J ** -1, 'IV': P * L1}[region]


U1 = mp.matrix([[1, 1], [0, 1]])
L1 = mp.matrix([[1, 0], [1, 1]])


def region_of(z):
    if mp.im(z) >= 0:
        return 'I' if mp.re(z) > E else 'II'
    return 'IV' if mp.re(z) > E else 'III'


def Ar(z):
    Mm = mp.matrix([[1, 1j], [1j, 1]]) / mp.sqrt(2)
    return P0(z) * s3pow(mom_half(z)) ** -1 * Mm ** -1 * s3pow(mp.power(fr(z), mp.mpf(1) / 4))


def Phat(z, n, region=None):
    region = region or region_of(z)
    zeta = mp.power(n, mp.mpf(2) / 3) * fr(z)
    h = mom_half(z) * mp.exp(n * phit(z))
    return Ar(z) * s3pow(mp.power(n, mp.mpf(1) / 6)) * Psi(zeta, region) * s3pow(h)


def nrm(X):
    return max(abs(X[i, j]) for i in range(2) for j in range(2))


tiny = mp.mpf('1e-25')
n = 50
worst = {}
# band (+ side above)
for x in [E - mp.mpf('0.05'), E - mp.mpf('0.01'), E - mp.mpf('0.002')]:
    Pp, Pm = Phat(x + 1j * tiny, n), Phat(x - 1j * tiny, n)
    worst['band'] = max(worst.get('band', 0), nrm(Pm ** -1 * Pp - J))
# saturated segment (+ side above)
for x in [E + mp.mpf('0.05'), E + mp.mpf('0.01'), E + mp.mpf('0.002')]:
    Pp, Pm = Phat(x + 1j * tiny, n), Phat(x - 1j * tiny, n)
    v = mp.matrix([[1, 0], [omega(x) * mp.exp(2 * n * phit(x)), 1]])
    worst['sat'] = max(worst.get('sat', 0), nrm(Pm ** -1 * Pp - v))
# vertical segments, oriented away from the axis; + side = left
for y in [mp.mpf('0.05'), mp.mpf('0.01'), mp.mpf('0.002')]:
    z = E + 1j * y  # upward: + side = west (II), - side = east (I)
    Pp, Pm = Phat(z - tiny, n, 'II'), Phat(z + tiny, n, 'I')
    v = mp.matrix([[1, -mp.exp(-2 * n * phit(z)) / omega(z)], [0, 1]])
    worst['vert+'] = max(worst.get('vert+', 0), nrm(Pm ** -1 * Pp - v))
    z = E - 1j * y  # downward: + side = east (IV), - side = west (III)
    Pp, Pm = Phat(z + tiny, n, 'IV'), Phat(z - tiny, n, 'III')
    v = mp.matrix([[1, -mp.exp(-2 * n * phit(z)) / omega(z)], [0, 1]])
    worst['vert-'] = max(worst.get('vert-', 0), nrm(Pm ** -1 * Pp - v))
# determinant
for z in [E + mp.mpf('0.03') * mp.exp(1j * t) for t in [0.3, 1.7, 2.9, 3.5, 4.4, 5.9]]:
    worst['det-1'] = max(worst.get('det-1', 0), abs(mp.det(Phat(z, n)) - 1))
# A_r: no jump on the band, bounded near 4c
for x in [E - mp.mpf('0.05'), E - mp.mpf('0.001')]:
    worst['A_r band jump'] = max(worst.get('A_r band jump', 0), nrm(Ar(x + 1j * tiny) - Ar(x - 1j * tiny)))
worst['max|A_r| near 4c (r=1e-8)'] = max(nrm(Ar(E + mp.mpf('1e-8') * mp.exp(1j * t))) for t in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
for zeta in [mp.mpc(1.3, 0.4), mp.mpc(-0.7, 1.1), mp.mpc(-2, -0.5), mp.mpc(0.4, -1.9)]:
    for reg in ['I', 'II', 'III', 'IV']:
        worst['Psi columns vs jumps'] = max(worst.get('Psi columns vs jumps', 0),
                                            nrm(Psi(zeta, reg) - Psi_by_jumps(zeta, reg)))
worst['M J M^-1 - diag(-i,i)'] = nrm(Mm * J * Mm ** -1 - mp.matrix([[-1j, 0], [0, 1j]]))
mhp = mom_half(E - mp.mpf('0.03') + 1j * tiny) * mom_half(E - mp.mpf('0.03') - 1j * tiny)
worst['(-om)^1/2_+ (-om)^1/2_- - 1'] = abs(mhp - 1)
for k, v in worst.items():
    print(f'{k:32s} {mp.nstr(v, 3)}')
# matching on the circle |z - 4c| = eps
eps = mp.mpf('0.2')
print('matching sup|Phat_r P0^{-1} - I| on |z-4c|=0.2, and n * sup:')
for n in [10, 40, 160, 640, 2560]:
  with mp.workdps(40 + n // 10):  # e^{n phi~} and the Airy functions cancel: extra digits needed
    m = max(nrm(Phat(E + eps * mp.exp(1j * t), n) * P0(E + eps * mp.exp(1j * t)) ** -1 - I2)
            for t in [0.2 + k * 0.5 for k in range(13)])
  print(f'  n={n:5d}  {mp.nstr(m, 4):>10s}  {mp.nstr(n * m, 4):>8s}')
