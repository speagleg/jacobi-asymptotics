"""Plan 10 Phase 3b (NUMERICAL): D-functions for p = 2 (t(z) = N/z single-valued; theta = pi t = pi N/z, odd).
Dt(z) := sqrt(2pi) t^{t-1/2} e^{-t} / Gamma(t)   (t = N/z; principal powers; Stirling => Dt -> 1)
D(z)  := Dt(z) / (1 - e^{-+2 i theta(z)})  for z in C_+-        (poles at the nodes)
E(z)  := (z^2 - r*^2)^{(p-1)/(2p)} (r*^2 - z^2)^{-1/2}          (cuts on [-r*, r*] and |x| > r*)
Checks: [1] D_+ E_+ = D_- E_- e^{2 i theta} on |x| > k_N (T-jump there is diag(e^{-2i theta}, e^{2i theta}));
        [2] D(z) E(z) -> const as z -> infinity (several directions);
        [3] Dt -> 1 on compacts as N grows (right half-plane)."""
import mpmath as mp

mp.mp.dps = 40
p = 2
rs = 2 ** (1 + mp.mpf(p) / 2) * mp.sqrt(mp.pi ** 2 / 16)


def parts(N):
    th = lambda z: mp.pi * N / z
    t = lambda z: N / z
    Dt = lambda z: mp.sqrt(2 * mp.pi) * mp.power(t(z), t(z) - mp.mpf(1) / 2) * mp.exp(-t(z)) / mp.gamma(t(z))
    D = lambda z: Dt(z) / (1 - mp.exp((-2j if mp.im(z) > 0 else 2j) * th(z)))
    E = lambda z: mp.power(z * z - rs ** 2, mp.mpf(p - 1) / (2 * p)) * mp.power(rs ** 2 - z * z, -mp.mpf(1) / 2)
    return th, Dt, D, E


for N in (20, 40):
    th, Dt, D, E = parts(N)
    kN = mp.power(N, 1) + mp.mpf("0.5")          # top node Z_1 = N^q = N for p = 2
    for x in (kN + 3, -(kN + 3), kN + 50):
        e = mp.mpf("1e-25")
        lhs = D(x + 1j * e) * E(x + 1j * e)
        rhs = D(x - 1j * e) * E(x - 1j * e) * mp.exp(2j * th(x))
        print(f"[1] N={N} x={mp.nstr(x,6)}: |D+E+ / (D-E- e^(2i theta)) - 1| = {mp.nstr(abs(lhs/rhs - 1), 3)}")
    vals = [D(R * mp.expj(a)) * E(R * mp.expj(a)) for R in (mp.mpf(10) ** 6,) for a in (0.3, 1.2, 2.0, -0.7, -2.5)]
    print(f"[2] N={N} D E at |z|=1e6 (5 directions): " + " ".join(mp.nstr(v, 6) for v in vals))
    print(f"[3] N={N} |Dt - 1| at z = 1, 2+i, 3-0.5i: " + " ".join(mp.nstr(abs(Dt(mp.mpc(z)) - 1), 3) for z in (1, 2 + 1j, 3 - 0.5j)))
