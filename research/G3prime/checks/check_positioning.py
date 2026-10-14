"""Plan 43 (PROOF.md §5.6): sanity checks of the elementary counting lemmas on random toy configurations.

NUMERICAL sanity only (finite random instances of a universally quantified statement; Rule N 2). Not zeta data.

[1] Lemma L (line structure) + Lemma CI (counting inequalities): for a random finite multiset of "zeros"
    (critical points 1/2+iv with multiplicity m >= 0, plus off-line pairs beta+iv, 1-beta+iv with multiplicities),
    check, at every height T,
        N - N_dist <= N - N0s <= N - A <= 2 (N - N_dist),   |E cap [1, N(T)]| = N - N_dist,
    where E = repeated indices of the ordinate list (with multiplicity), A = #{zeros with H(gamma) = 1}.
[2] Lemma D (decomposition): for random small ordinate lists with repeats and an energy that depends only on the
    values, check by brute force over all subsets that
        C(K) = C_dist(K) + K * |E cap (k2, K]|.
[3] The constant of Corollary Lz: C0 = 3/2 - (1/sqrt 2) cot(1/sqrt 2) ((C6) (1.1)) and 1 - C0 (double precision).
Exact integer / rational arithmetic in [1]; exact values and float energies (tolerance 1e-9) in [2].
"""
import itertools
import math
import random
from fractions import Fraction


def random_config(rng, n_lines):
    """Return list of zeros as (beta, v, mult); beta = Fraction(1,2) for critical."""
    zeros = []
    for v in range(1, n_lines + 1):
        kind = rng.random()
        if kind < 0.55:
            zeros.append((Fraction(1, 2), v, 1))
        elif kind < 0.65:
            zeros.append((Fraction(1, 2), v, rng.randint(2, 4)))
        elif kind < 0.8:
            b = Fraction(rng.randint(1, 9), 20)
            if b == Fraction(1, 2):
                b = Fraction(1, 4)
            m = rng.randint(1, 2)
            zeros += [(b, v, m), (1 - b, v, m)]
        else:
            # simple critical zero plus an off-line pair on the same line
            b = Fraction(1, 5)
            zeros += [(Fraction(1, 2), v, 1), (b, v, 1), (1 - b, v, 1)]
    return zeros


def check_counting(rng, trials=400):
    worst = 0
    for _ in range(trials):
        zs = random_config(rng, rng.randint(1, 40))
        # ordinate list with multiplicity
        gam = sorted(v for (_, v, m) in zs for _ in range(m))
        E = {k for k in range(2, len(gam) + 1) if gam[k - 1] == gam[k - 2]}  # 1-based
        H = {}
        for (_, v, m) in zs:
            H[v] = H.get(v, 0) + m
        for T in range(1, max(gam) + 1):
            N = sum(1 for g in gam if g <= T)
            Nd = len({g for g in gam if g <= T})
            N0s = sum(1 for (b, v, m) in zs if v <= T and b == Fraction(1, 2) and m == 1)
            A = sum(m for (b, v, m) in zs if v <= T and H[v] == 1)
            EN = sum(1 for k in E if k <= N)
            assert EN == N - Nd, (EN, N, Nd)
            assert N - Nd <= N - N0s <= N - A <= 2 * (N - Nd), (N, Nd, N0s, A)
            # H = 1 <=> simple, critical, alone on its line
            for (b, v, m) in zs:
                if v <= T and H[v] == 1:
                    assert b == Fraction(1, 2) and m == 1
            worst = max(worst, (N - N0s) - (N - Nd))
    return trials


def energy(vals):
    """Value-only pair energy: sum over pairs with |difference| < 1 of log(1/d), +inf on a repeat."""
    vals = sorted(vals)
    P = 0.0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            d = vals[j] - vals[i]
            if d == 0:
                return math.inf
            if d < 1:
                P += math.log(1 / d)
    return P


def check_decomposition(rng, trials=300):
    for _ in range(trials):
        L = rng.randint(2, 11)
        base = sorted(rng.choice([Fraction(i, 4) for i in range(0, 40)]) for _ in range(L))
        gam = base  # nondecreasing, repeats allowed
        K = len(gam)
        k2 = rng.randint(1, min(3, K))
        idx = list(range(k2, K + 1))
        best = math.inf
        for r in range(len(idx) + 1):
            for T in itertools.combinations(idx, r):
                c = energy([gam[t - 1] for t in T]) + K * (len(idx) - r)
                best = min(best, c)
        # representatives: first index >= k2 of each value
        reps, seen = [], set()
        for k in idx:
            if gam[k - 1] not in seen:
                seen.add(gam[k - 1])
                reps.append(k)
        best_d = math.inf
        for r in range(len(reps) + 1):
            for T in itertools.combinations(reps, r):
                c = energy([gam[t - 1] for t in T]) + K * (len(reps) - r)
                best_d = min(best_d, c)
        eK = sum(1 for k in range(k2 + 1, K + 1) if gam[k - 1] == gam[k - 2])
        assert len(idx) - len(reps) == eK
        assert abs(best - (best_d + K * eK)) < 1e-9, (gam, k2, best, best_d, eK)
    return trials


if __name__ == "__main__":
    rng = random.Random(43)
    t1 = check_counting(rng)
    print(f"[1] counting lemmas (L, CI): {t1} random configurations, all heights: OK")
    t2 = check_decomposition(rng)
    print(f"[2] decomposition C = C_dist + K*e_K (brute force over subsets): {t2} random instances: OK")
    C0 = 1.5 - (1 / math.sqrt(2)) / math.tan(1 / math.sqrt(2))
    print(f"[3] C0 = {C0:.10f}, 1 - C0 = {1 - C0:.10f}")
