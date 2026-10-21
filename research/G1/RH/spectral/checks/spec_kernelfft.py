"""SPEC §3.18 probe: the frequency response of the noise kernel, and a rigidity (form-factor) prediction of the noise variance.
Displacement field h_k = sin(2 pi k/Lam + phi) for k <= M = 3000 (zero beyond), nodes x_k = k + eps h_k, lam = x^p, weights x^{-s}
(p = 0.6, s = 2, eps = 0.02). Linear response per unit amplitude: R_phi(n) := n (y(eps) - y_lat)/eps.
Power |F_n(omega)|^2 := R_0^2 + R_{pi/2}^2 at omega = 2 pi/Lam.
Prediction for a displacement process with spectral density S_h(omega) (Var h_k = int_{-pi}^{pi} S_h d omega/2pi):
  Var L(n) = int_{-pi}^{pi} S_h(omega) |F_n(omega)|^2 d omega/(2 pi),
with S_h = K(omega)/(4 sin^2(omega/2)): K = 1 (Poisson increments), K_GUE(omega) = min(|omega|/(2 pi), 1) (spacing form factor);
the measured RMS of the linearised GUE/Poisson noise L is in spec_noiselin.out.
Usage: spec_kernelfft.py Lam [Lam ...]   (computes/caches both phases; prints |F|^2 at n = 200, 400, 800, 1600 windows)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np
from spec_common import run, NMAX
from so_coeffs import coeffs
from so_fit import sequences
p, s, M, eps = 0.6, 2.0, 3000, 0.02; K = 200*NMAX
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
k = np.arange(1, K + 1, dtype=np.float64)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..', 'tmp', 'kernelfft')
os.makedirs(out, exist_ok=True)
for Lam in [float(a) for a in sys.argv[1:]]:
    R = []
    for ph in (0.0, np.pi/2):
        x = k.copy(); x[:M] += eps*np.sin(2*np.pi*k[:M]/Lam + ph)
        n, y = run(f"kfft_L{Lam}_ph{ph:.4f}", x**p, p, s, 0.0, K); R.append(n*(y - y0)/eps)
    P = R[0]**2 + R[1]**2; np.save(os.path.join(out, f"P_L{Lam}.npy"), np.vstack([n, P, R[0], R[1]]))
    w = lambda lo: np.mean(P[(n >= lo) & (n < 2*lo)])
    print(f"Lam = {Lam:6.2f} (omega = {2*np.pi/Lam:.4f}): mean |F|^2 over n-octaves [100,200) {w(100):.4e}  [200,400) {w(200):.4e}  [400,800) {w(400):.4e}  [800,1600) {w(800):.4e}")
# Post-processing (run separately; reads tmp/kernelfft/*.npy): kappa(omega) := mean |F_n|^2 / n over an n-octave, interpolated in
# log-log (linear in omega below the smallest measured omega, flat above), then
#   Var L(n)/n = 2 int_0^pi kappa(w) S_h(w) dw/(2 pi),  S_h = K(w)/(4 sin^2(w/2)),  K_Poisson = 1, K_GUE = min(w/(2 pi), 1).
