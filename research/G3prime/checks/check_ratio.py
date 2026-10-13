"""G3' Lemma Z1 constant and Lemma Z2 pair-ratio bound (NUMERICAL Rule A pass, Odlyzko zeros, double precision).
[1] C0 := sup_{T >= 1e6} 2 pi E(T)/log(T/4pi), E(T) = 0.111 log T + 0.275 log log T + 2.524 (Trudgian Cor. 1, T0 = e).
[2] observed max |gamma_k - gamma~_k| on the data, against C0.
[3] Z2: for pairs a < b (b - a <= 200, all a in a range, plus random far pairs), observed (x_a - x_b)/(x~_a - x~_b)
    against rho(a,b) = (1 + C0 log(g~_b/2pi)/(pi (b-a))) (1 + 2 C0/g~_a)^5.  Report violations and worst slack."""
import numpy as np
from jacobi_asym.measures.lfun import load_odlyzko, model_zeros


def E(T):
    return 0.111 * np.log(T) + 0.275 * np.log(np.log(T)) + 2.524


def part1():
    T = np.exp(np.linspace(np.log(1e6), np.log(1e300), 200001))
    r = 2 * np.pi * E(T) / np.log(T / (4 * np.pi))
    print(f"[1] 2piE(T)/log(T/4pi) on [1e6, 1e300]: max {r.max():.4f} at T={T[r.argmax()]:.3e}; "
          f"monotone decreasing: {bool(np.all(np.diff(r) <= 0))}; value at 1e300 {r[-1]:.4f} (limit 2pi*0.111={2*np.pi*0.111:.4f})")
    return float(np.ceil(r.max() * 10) / 10)


def part2(g, gs, C0):
    d = np.abs(g - gs)
    print(f"[2] max |gamma_k - gamma~_k| over k <= {g.size}: {d.max():.4f} (k={int(d.argmax())+1}); "
          f"over gamma_k >= 1e6: {d[g >= 1e6].max() if np.any(g >= 1e6) else float('nan'):.4f}; C0 used = {C0}")


def part3(g, gs, C0, A=200_000, W=200, nfar=2_000_000, seed=0):
    x, xs = 1 / (g ** 2 + 0.25), 1 / (gs ** 2 + 0.25)
    worst, viol, cnt = np.inf, 0, 0
    a = np.arange(0, A)
    for d in range(1, W + 1):
        b = a + d
        num = x[a] - x[b]
        den = xs[a] - xs[b]
        rho = (1 + C0 * np.log(gs[b] / (2 * np.pi)) / (np.pi * d)) * (1 + 2 * C0 / gs[a]) ** 5
        slack = rho - num / den
        viol += int(np.sum(slack < 0)); worst = min(worst, slack.min()); cnt += a.size
    rng = np.random.default_rng(seed)
    aa = rng.integers(0, g.size - 1, nfar)
    bb = np.minimum(aa + 1 + rng.integers(0, g.size // 4, nfar), g.size - 1)
    m = bb > aa
    aa, bb = aa[m], bb[m]
    num, den = x[aa] - x[bb], xs[aa] - xs[bb]
    rho = (1 + C0 * np.log(gs[bb] / (2 * np.pi)) / (np.pi * (bb - aa))) * (1 + 2 * C0 / gs[aa]) ** 5
    slack = rho - num / den
    viol += int(np.sum(slack < 0)); worst = min(worst, slack.min()); cnt += aa.size
    print(f"[3] Z2 checked on {cnt} pairs (near: a<{A}, b-a<={W}; far: {aa.size} random): violations {viol}, "
          f"min slack rho - ratio = {worst:.3e}")
    r = (x[a] - x[a + 1]) / (xs[a] - xs[a + 1])
    print(f"    adjacent-pair ratio (x_a - x_a+1)/(x~_a - x~_a+1): max {r.max():.3f}, min {r.min():.2e}")


if __name__ == "__main__":
    C0 = part1()
    g = load_odlyzko()
    gs = model_zeros(g.size)
    part2(g, gs, C0)
    part3(g, gs, C0)
