"""Lemma S (index shift), NUMERICAL sanity check: for random strictly increasing pi with pi(a) <= (1+eta) a,
pi(a)^-2 - pi(b)^-2 >= (1+eta)^-3 (a^-2 - b^-2) for all b > a.  Reports min of LHS/RHS."""
import numpy as np

rng = np.random.default_rng(1)
worst = np.inf
for trial in range(200):
    eta = rng.uniform(0.01, 1.0)
    n = 2000
    # strictly increasing pi with pi(j) >= j; enforce pi(a) <= (1+eta) a only at the tested a
    steps = 1 + rng.poisson(eta * rng.uniform(0, 2), n)
    pi = np.cumsum(steps)
    j = np.arange(1, n + 1)
    ok = (pi <= (1 + eta) * j) & (j < n)
    for a in rng.choice(np.nonzero(ok)[0], size=min(50, ok.sum()), replace=False):
        b = np.arange(a + 1, n)
        lhs = pi[a] ** -2.0 - pi[b] ** -2.0
        rhs = (1 + eta) ** -3 * ((a + 1.0) ** -2 - (b + 1.0) ** -2)
        worst = min(worst, np.min(lhs / rhs))
print(f"Lemma S: min LHS/RHS over random trials = {worst:.6f} (must be >= 1)")
