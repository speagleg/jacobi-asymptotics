# jacobi-asymptotics

[![python](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/python.yml/badge.svg)](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/python.yml)
[![lean](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/lean.yml/badge.svg)](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/lean.yml)

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

## Headline results

Throughout, $\sigma_{p,s,\ell}=\sum_k k^{-s}\ell(k)\,\delta_{k^{-p}}$, with $p>0$, $s>1$, and $\ell$ a positive weight
factor (pure powers: $\ell\equiv1$). The status label after each result is explained under
[How much to trust these results](#how-much-to-trust-these-results).

**1. The averaged law holds for every $p>0$.**
Let the atoms satisfy $x_k=f(k)$ with $\xi^{p+1}f'(\xi)\to-pC$ (and $\xi^{p+1}|f'(\xi)|$ bounded above and below), and let the weights satisfy $\sum w_k<\infty$ and
$w_k\ge c_1k^{-s}$. Then the Hankel determinants $D_n=\det(m_{i+j})_{i,j<n}$ satisfy

$$\log D_n=-p\,n^2\log n+\Bigl(\tfrac{3p}{2}+\log\bigl(c(p)\,C\bigr)\Bigr)n^2+o(n^2),$$

and $c(p)$ is identified through an explicitly solved constrained equilibrium problem. A corollary is the $n^2$
asymptotics of the Hankel determinants of zeta values, $\det_{1\le i,j\le n}\zeta(a(i+j)+b)$, for every real $a>0$
with $2a+b>1$.
*Status: PROVED; reviewed. The theorem in full (general atoms $f\in C^1[1,\infty)$ with the stated derivative
conditions, weights with $\sum w_k<\infty$ and $w_k\ge c_1k^{-s}$ for any real $s$, constant in Gamma form), the Jacobi
form (Corollary 1.2) and the zeta-value corollary are also **machine-checked in Lean 4 / Mathlib**, sorry-free with only
the standard axioms (`paper1_thm11`, `paper1_cor12`, `paper1_cor14`; `lean/JacobiAsym/GeneralAtoms.lean`,
`Paper1Corollaries.lean`). Not formalized: uniqueness of the equilibrium maximiser (not needed for the theorem).*
&nbsp;[Paper 1](papers/paper1/main.pdf), `research/G2/`

**2. The pointwise law holds for pure powers, with rate $O(1/n)$.**
For every $p>0$ and $s>1$, the measure $\sigma_{p,s,1}=\sum_k k^{-s}\delta_{k^{-p}}$ satisfies

$$n^p b_n=c(p)\bigl(1+O(1/n)\bigr),\qquad \frac{a_n}{2b_n}=1+O(1/n).$$

The same method gives the pointwise law for the smooth zeta model ($x_j=1/(\gamma_j^2+\tfrac14)$ with $\gamma_j$ from the
smooth zero-counting function): $b_n/x_n=\tfrac{\pi^2}{16}\bigl(1+\kappa/\log n+O(\log\log n/\log^2n)\bigr)$, with
$\kappa=-0.28946\ldots$
*Status: PROVED modulo cited Riemann–Hilbert constructions (Wu–Lin–Xu–Zhao, Kuijlaars–McLaughlin–Van Assche–Vanlessen,
Conway–Deift, DLMF); reviewed.* &nbsp;[Paper 2](papers/paper2/main.pdf), `research/G1/RH/`

**3. The pointwise law survives every slowly varying weight factor.**
For every $p>0$, every $s>1$ and **every** slowly varying $\ell$ (for example $\ell(k)=e^{\sqrt{\log k}}$, or any
bounded, logarithmic or iterated-logarithmic factor),

$$n^p b_n\longrightarrow c(p),\qquad n^p a_n\longrightarrow 2c(p).$$

If $\log\ell(e^u)$ extends analytically (bounded, with derivative tending to 0) to **some** horizontal strip
$|\operatorname{Im}u|\le\vartheta$, of any width $\vartheta>0$, the rate is $O(1/n)$.
*Status: PROVED modulo the same citations as result 2; reviewed.* &nbsp;[Paper 2](papers/paper2/main.pdf),
`research/G1/PROOF.md` §§3.17–3.23

**4. A Christoffel shift moves the law from $s$ to $s+p$.**
For any positive measure $\sigma$ on $[0,\infty)$ with infinite support: if $\sigma$ satisfies Law P, so does
$x\,\sigma$, with the same rate when that rate is regular. Conversely, Law P for $x\,\sigma$ implies Law P for $\sigma$.
Since $x\cdot\sigma_{p,s,\ell}=\sigma_{p,s+p,\ell}$, this extends any base case to every larger $s$.
*Status: PROVED; reviewed. The key limit lemma is known (chain sequences, Dai–Piao–Qiao 2025); the rate transfer was
not found in the literature.* &nbsp;[Paper 2](papers/paper2/main.pdf) §3

**5. Bounded rough weights can break the law.**
For every $p>0$, $s>1$ and every sufficiently small $\varepsilon>0$ there is a sequence $f$ with $|f(k)|\le\varepsilon$
such that, for the weights $k^{-s}e^{f(k)}$, the sequence $n^pb_n$ does not converge; a separate construction does the
same for $n^pa_n$. So result 3 is sharp in the sense that slow variation cannot be replaced by mere boundedness.
*Status: PROVED modulo the citations of result 2; reviewed.* &nbsp;`research/G1/PROOF.md` §§3.6, 3.10, 3.12

**6. For the true zeta zeros, the averaged law is equivalent to a statement about close pairs of zeros.**
Let $\sigma=\sum_k 2x_k\delta_{x_k}$ with $x_k=1/(\gamma_k^2+\tfrac14)$, where $\gamma_k$ are the ordinates of the
nontrivial zeros of $\zeta$, taken as given real numbers. Then:
* **unconditionally**, $\log D_n\le\Phi_n+o(n^2)$ and $\log D_n\ge\Phi_n-O(n^2)$, where $\Phi_n$ is the value
  predicted by the averaged law;
* the averaged law holds **if and only if** a capped "near-pair energy" of the ordinates is $o(K^2)$;
* it holds under Montgomery's pair-correlation conjecture (no RH needed), and also under several other stated
  hypotheses;
* proving it unconditionally would imply that asymptotically 100% of the zeros are simple and on the critical line,
  so it is at least as hard as that open problem.

*Status: PROVED modulo cited bounds on the zero-counting function and pair-correlation results; reviewed. Nothing here
is evidence about RH.* &nbsp;`research/G3prime/PROOF.md`

The full index of every statement, with exact hypotheses, labels and dependencies, is
**[THEOREMS.md](THEOREMS.md)**.

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
  * "Certified" is used only for interval arithmetic (Arb). The constants and closed forms the README and papers quote
    (c(p), κ_p, κ, the Lommel and Baricz–Štampach closed forms) are certified in [`certified/`](certified/README.md).
* **Reproducible outputs.** `scripts/reproduce.sh` re-runs the certified suite and 47 numerical checks and diffs each
  output byte-for-byte against the committed `.out`; `MANIFEST.sha256` pins the SHA-256 of every check, output, paper
  PDF and Lean file. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for what is re-run and what is excluded.
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
lean/                  Lean 4 / Mathlib formalisation (sorry-free; see lean/README.md): Heine/Hankel reduction, averaged law
                       for pure powers (all p > 0, s > 1), Christoffel shift
src/jacobi_asym/       Python toolkit: measures, recurrence coefficients, Hankel determinants, certified (Arb) mode
tests/                 pytest suite
```

Reading order: this README, then THEOREMS.md §1, then the paper drafts. `research/*/PROOF.md` holds the full working
proofs, which are long and written as lab notebooks.

## Running the code

CI (GitHub Actions) runs both on every push to `master`: the fast pytest suite with the C kernel built plus the manifest check and the certified-output comparison (`python.yml`; slow regressions weekly) and the Lean build + axiom audit `lean/check.sh` (`lean.yml`, when `lean/` changes).

```bash
scripts/setup_env.sh                     # .venv on top of the system numpy/scipy/mpmath/sympy (Python ≥ 3.12),
                                         # adds python-flint, builds the C kernel in csrc/ (needs gcc + libquadmath)
.venv/bin/python -m pytest               # fast suite
.venv/bin/python -m pytest -m slow       # slow regression tests (minutes)
scripts/reproduce.sh                     # build + tests + re-run certified suite and numerical checks, diff vs the
                                         # committed outputs, Lean audit, manifest check (~5 min; --quick ~20 s)
python scripts/manifest.py --check       # verify MANIFEST.sha256 (rerun without --check after changing a covered file)
```

```python
from jacobi_asym.measures import pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import c_p

mu = pure_power(2, 200_000)                 # atoms k^-2, weights k^-2
r = jacobi_coeffs(mu, 2000)                 # recurrence coefficients (float64; numerical)
print(r.b[1999] / mu.atoms[1999], c_p(2))   # b_n / x_n  vs  pi^2/16
```

Certified coefficients for small exact measures: `jacobi_asym.certify.certified_jacobi`. Certified (Arb) checks of the
quoted constants and closed forms: `certified/` (see [certified/README.md](certified/README.md)).

Lean: `cd lean && ./check.sh` builds the library and audits axioms. It should print `AUDIT OK`, meaning no `sorry`
and only the standard axioms.

## Provenance

This project continues item 11 of an earlier private notebook. Copied material and its sources are listed in
[PROVENANCE.md](PROVENANCE.md). Zeta-zero data come from A. Odlyzko's tables (`data/fetch.py`, with checksums).
Planning documents and working logs are kept outside the public tree, so a few internal cross-references to `LOG.md`
files or plan documents point to unpublished notes.

## License

MIT; see [LICENSE](LICENSE).
