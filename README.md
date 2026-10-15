# jacobi-asymptotics

**Asymptotics of orthogonal-polynomial recurrence coefficients for discrete measures whose atoms accumulate at 0.**

Take a positive measure with atoms at the points $x_k = k^{-p}$ and weights $w_k$,

$$\sigma = \sum_{k\ge 1} w_k\,\delta_{x_k}, \qquad x_k = k^{-p}\ (p>0),$$

and let $a_n, b_n$ be the coefficients of its orthogonal polynomials,
$x P_n = P_{n+1} + a_n P_n + b_n^2 P_{n-1}$. Equivalently, $\sigma$ is the spectral measure of a compact Jacobi matrix
whose eigenvalues are $k^{-p}$. This repository studies **"Law P"**:

$$n^p\, b_n \;\longrightarrow\; c(p) = \tfrac14\Bigl(\frac{\pi}{2I(p)}\Bigr)^{p},\qquad n^p a_n \longrightarrow 2c(p),
\qquad I(p)=\frac{\sqrt\pi}{2}\,\frac{\Gamma(1/p+\tfrac12)}{\Gamma(1/p+1)},$$

so $c(1) = \tfrac12$ and $c(2) = \pi^2/16$. The constant comes from an explicitly solvable constrained equilibrium
problem.

---

## Main results

| Result | Statement (short) | Where |
|---|---|---|
| **Averaged law** | For every $p>0$, atoms $x_k \sim Ck^{-p}$ and weights with $\sum w_k<\infty$, $w_k \ge c_1 k^{-s}$: $\log D_n = -pn^2\log n + (3p/2+\log(c(p)C))\,n^2 + o(n^2)$, where $D_n$ is the Hankel determinant. Corollary: the $n^2$ asymptotics of $\det\zeta(a(i+j)+b)$ for every real $a>0$. | `papers/paper1/`, `research/G2/` |
| **Pointwise law, slowly varying weights** | For every $p>0$, $s>1$ and **every slowly varying** $\ell$ (e.g. $\ell(k)=e^{\sqrt{\log k}}$), the weights $w_k=k^{-s}\ell(k)$ give $n^pb_n\to c(p)$ and $n^pa_n\to 2c(p)$; with rate $O(1/n)$ if $\ell$ extends analytically to a sector. | `papers/paper2/`, `research/G1/` |
| **Christoffel shift** | For any positive measure on $[0,\infty)$ with infinite support: Law P for $\sigma$ implies Law P for $x\,\sigma$, with the same rate if the rate is regular; conversely, Law P for $x\,\sigma$ implies it for $\sigma$. | `papers/paper2/` §3 |
| **Rough weights break it** | There are bounded weights $k^{-s}e^{f(k)}$ with $\lvert f\rvert\le\varepsilon$ for which $n^pb_n$ and $n^pa_n$ do not converge. | `research/G1/PROOF.md` §§3.6, 3.10, 3.12 |
| **Zeta-zero measure** | For $\sigma=\sum 2x_k\delta_{x_k}$, $x_k = 1/(\gamma_k^2+\tfrac14)$ with $\gamma_k$ the zeta ordinates: the averaged law holds **iff** a capped near-pair energy of the ordinates is $o(K^2)$; it holds under Montgomery's pair-correlation conjecture, and proving it unconditionally is at least as hard as showing that 100% of zeros are simple and on the critical line. | `research/G3prime/` |

The full index of every statement, with its exact status label and dependencies, is **[THEOREMS.md](THEOREMS.md)**.

### How much to trust these results

* **Not peer reviewed.** Nothing here has been refereed by a journal or read by a human specialist yet.
* **AI-assisted.** The research, proofs and write-ups were developed with an AI assistant (Claude Code, Anthropic).
  Every lemma went through an adversarial self-check and an independent AI referee pass before being marked
  `REVIEWED`. The referee reports are kept in `research/*/review/`. This verification trail is visible, but it is not a
  substitute for expert review.
* **Labels mean exactly what they say** (see [VERIFICATION_POLICY.md](VERIFICATION_POLICY.md)):
  * `PROVED`: self-contained proof in the repo.
  * `PROVED-mod-cite (X)`: proved, assuming the external results X. Each one is quoted with its exact hypotheses from
    a source that was read, and recorded in a `CITATIONS.md`.
  * `CONDITIONAL`: proved under a stated hypothesis.
  * `NUMERICAL`: computed, not proved.
  * `GAP`: a precise statement that is not proved.
  * "Certified" is used only for interval arithmetic (Arb).
* **Novelty.** A first-pass literature search is summarised in THEOREMS.md. Many statements are marked
  "novelty UNCHECKED", and some ingredients are known (for example, the chain-sequence lemma behind the Christoffel
  shift).
* **No claim about the Riemann Hypothesis.** Measures built from zeta zeros take the ordinates as given real numbers,
  and nothing here is evidence for or against RH.

---

## Papers (drafts)

| | Title | Status |
|---|---|---|
| [`papers/paper1`](papers/paper1/main.pdf) | Hankel determinants of discrete measures with power-law atoms, and of zeta values | draft, 16 pp |
| [`papers/paper2`](papers/paper2/main.pdf) | Recurrence coefficients of discrete measures with power-law atoms and slowly varying weights | draft, 67 pp |

Each paper folder has a `NOTES.md` that lists open items and sources still to be verified.

## Repository layout

```
THEOREMS.md            index of all results: statements, labels, dependencies, open problems
VERIFICATION_POLICY.md meaning of the status labels
papers/                paper drafts (LaTeX + PDF + numerical checks)
research/G2/           averaged law: constrained equilibrium, Hankel asymptotics
research/G1/           pointwise law: Tauberian reductions, weight transport, Riemann–Hilbert analyses (RH/)
research/G3prime/      the measure built from zeta zeros
research/*/review/     independent referee reports for each step
research/*/checks/     numerical checks (scripts + outputs)
lean/                  Lean 4 / Mathlib formalisation of the Heine/Hankel reduction (sorry-free; see lean/README.md)
src/jacobi_asym/       Python toolkit: measures, recurrence coefficients, Hankel determinants, certified (Arb) mode
tests/                 pytest suite
```

Reading order: this README, then THEOREMS.md §1, then the paper drafts. `research/*/PROOF.md` holds the full working
proofs, which are long and written as lab notebooks.

## Running the code

```bash
scripts/setup_env.sh                     # .venv on top of the system numpy/scipy/mpmath/sympy (Python ≥ 3.12),
                                         # adds python-flint, builds the C kernel in csrc/ (needs gcc + libquadmath)
.venv/bin/python -m pytest               # fast suite
.venv/bin/python -m pytest -m slow       # slow regression tests (minutes)
```

```python
from jacobi_asym.measures import pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import c_p

mu = pure_power(2, 200_000)                 # atoms k^-2, weights k^-2
r = jacobi_coeffs(mu, 2000)                 # recurrence coefficients (float64; numerical)
print(r.b[1999] / mu.atoms[1999], c_p(2))   # b_n / x_n  vs  pi^2/16
```

Certified coefficients for small exact measures: `jacobi_asym.certify.certified_jacobi`.

Lean: `cd lean && ./check.sh` builds the library and audits axioms. It should print `AUDIT OK`, meaning no `sorry`
and only the standard axioms.

## Provenance

This project continues item 11 of an earlier private notebook. Copied material and its sources are listed in
[PROVENANCE.md](PROVENANCE.md). Zeta-zero data come from A. Odlyzko's tables (`data/fetch.py`, with checksums).
Planning documents and working logs are kept outside the public tree, so a few internal cross-references to `LOG.md`
files or plan documents point to unpublished notes.
