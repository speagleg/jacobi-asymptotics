# jacobi-asymptotics

[![python](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/python.yml/badge.svg)](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/python.yml)
[![lean](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/lean.yml/badge.svg)](https://github.com/speagleg/jacobi-asymptotics/actions/workflows/lean.yml)

**How do the entries of a Jacobi matrix behave when its eigenvalues are $1, 2^{-p}, 3^{-p}, \dots$?**

A Jacobi matrix is a symmetric tridiagonal matrix with diagonal entries $a_0, a_1, \dots$ and off-diagonal entries
$b_1, b_2, \dots > 0$. Equivalently, $a_n$ and $b_n$ are the recurrence coefficients of the orthogonal polynomials of
a measure, $xP_n = P_{n+1} + a_nP_n + b_n^2P_{n-1}$. This repository studies the inverse question for discrete measures
whose atoms pile up at 0 like a power,

$$\sigma = \sum_{k\ge1} w_k\,\delta_{x_k}, \qquad x_k = k^{-p}\quad(p>0),$$

that is, compact Jacobi matrices with eigenvalues $k^{-p}$ and spectral weights $w_k$. The answer, proved here in
increasing strength, is that the entries decay like the eigenvalues, with an explicit constant:

$$n^p\, b_n \to c(p),\qquad n^p a_n \to 2c(p),\qquad
c(p) = \frac14\Bigl(\frac{\pi}{2I(p)}\Bigr)^{p},\quad I(p) = \frac{\sqrt\pi}{2}\,\frac{\Gamma(1/p+\frac12)}{\Gamma(1/p+1)},$$

so $c(1)=\tfrac12$ and $c(2)=\pi^2/16$. The constant comes from an explicitly solvable equilibrium problem for a
logarithmic energy with an upper constraint. In the repository this limit statement is called **"Law P"**.

One application: the Hankel determinants $\det_{1\le i,j\le n}\zeta(a(i+j)+b)$ of zeta values are Hankel determinants
of such a measure. Haynes and Zudilin expected $\log\det\zeta(a(i+j)+b) = -an^2\log n + O(n^2)$ and proved the upper
bound $-\tfrac a2 n^2\log n+O(n^2)$; Monien described a heuristic and numerical evidence (due to Zagier) for $a=1$. Result 1
below proves the asymptotics, with the $n^2$ term, for every real $a>0$ with $2a+b>1$.

> **Status in one paragraph.** Nothing here has been refereed by a journal yet. The work was developed with an AI
> assistant (Claude, Anthropic), and every proof went through an independent AI referee pass whose reports are in the
> repository. The averaged result (1) is additionally **machine-checked in Lean 4**. The pointwise results (2–4) and the counterexamples in 5
> rely on published Riemann–Hilbert asymptotics, which are cited, not re-proved. Details are under
> [How much to trust these results](#how-much-to-trust-these-results).

---

## Results at a glance

Throughout, $\sigma_{p,s} = \sum_k k^{-s}\,\delta_{k^{-p}}$ (pure powers), with $p>0$ and $s>1$.

| # | Result | Status | Where |
|---|---|---|---|
| 1 | **Averaged law.** $\log D_n$ (Hankel determinants) is known to $o(n^2)$ for general power-like atoms and weights; zeta-value Hankel determinants as a corollary | proved; **Lean-verified** | [Paper I](papers/paper1/main.pdf) |
| 2 | **Pointwise law with rate.** $n^pb_n = c(p)(1+O(1/n))$ for every $p>0$, $s>1$ | proved, using cited Riemann–Hilbert results | [Paper II](papers/paperII/main.pdf) |
| 3 | **The $1/n$ term.** $n^pb_n = c(p)\bigl(1-\frac{s-1}{2n}+\dots\bigr)$ for every $p>0$, with an explicit $\zeta(-p)\,n^{-1-p}$ term when $p<1$ | proved, using cited Riemann–Hilbert results | [Paper II](papers/paperII/main.pdf) |
| 4 | **Slowly varying weights.** The pointwise law holds for weights $k^{-s}\ell(k)$ with any slowly varying $\ell$ | proved, using cited Riemann–Hilbert results | [Paper III](papers/paperIII/main.pdf) |
| 5 | **Christoffel shift and sharpness.** The law passes from $s$ to $s+p$; bounded but irregular weights can break it | proved (shift); proved using cited results (counterexamples) | [Paper II](papers/paperII/main.pdf) §3, [Paper III](papers/paperIII/main.pdf) |
| 6 | **Zeta zeros.** For the measure built from the zeros of $\zeta$, the averaged law is equivalent to a statement about close pairs of zeros | proved, using cited results on zeta zeros; the law itself is open | [`research/G3prime/`](research/G3prime/PROOF.md) |

---

## The results in more detail

### 1. The averaged law (the $n^2$ term of the Hankel determinants)

The Hankel determinants $D_n = \det(m_{i+j})_{0\le i,j<n}$ of the moments $m_j=\sum_k w_kx_k^j$ satisfy
$D_n = m_0^{\,n}\prod_{j=1}^{n-1} b_j^{2(n-j)}$, so their size is a weighted average of the $b_j$. Hence the name "averaged law".

**Theorem.** Let $x_k=f(k)$ with $\xi^{p+1}f'(\xi)\to -pC$ and $\xi^{p+1}|f'(\xi)|$ bounded above and away from 0
for $\xi \ge 1$, and let the weights satisfy $\sum_k w_k<\infty$ and $w_k\ge c_1k^{-s}$ for some real $s$. Then

$$\log D_n = -p\,n^2\log n + \Bigl(\tfrac{3p}{2}+\log\bigl(c(p)\,C\bigr)\Bigr)n^2 + o(n^2).$$

As a corollary, $\log\det_{1\le i,j\le n}\zeta(a(i+j)+b) = -an^2\log n + \bigl(\tfrac{3a}{2}+\log c(a)\bigr)n^2 + o(n^2)$
for every real $a>0$ with $2a+b>1$. For example, the constant is $\tfrac32-\log2$ for $a=1$.

*Status:* proved, with a self-contained proof. The theorem as stated, its Jacobi-matrix form and the zeta-value
corollary are also formalised in Lean 4 / Mathlib, with no unproved steps and only the standard axioms. See
[`lean/README.md`](lean/README.md) for the theorem names.

### 2. The pointwise law, with rate $O(1/n)$

For every $p>0$ and $s>1$, the pure-power measure $\sigma_{p,s}$ satisfies

$$n^pb_n = c(p)\bigl(1+O(1/n)\bigr),\qquad \frac{a_n}{2b_n} = 1+O(1/n).$$

The same method treats a smooth model of the zeta zeros, $x_j = 1/(\gamma_j^2+\tfrac14)$ with $\gamma_j$ given by the
smooth zero-counting function: $b_n/x_n = \tfrac{\pi^2}{16}\bigl(1+\kappa/\log n+O(\log\log n/\log^2 n)\bigr)$ with
$\kappa=-0.28946\ldots$

*Status:* proved, assuming the published Riemann–Hilbert constructions it cites (Wu–Lin–Xu–Zhao;
Kuijlaars–McLaughlin–Van Assche–Vanlessen; Conway–Deift; DLMF). Each citation is recorded with its exact hypotheses.

### 3. The $1/n$ correction

For every $p\ge1$ and $s>1$,

$$n^pb_n = c(p)\Bigl(1-\frac{s-1}{2n}+O(n^{-2})\Bigr),\qquad
n^pa_n = 2c(p)\Bigl(1-\frac{s-1+p}{2n}+O(n^{-2})\Bigr),\qquad \frac{a_n}{2b_n} = 1-\frac{p}{2n}+O(n^{-2}).$$

Equivalently, $b_n \approx c(p)\,\bigl(n+\tfrac{s-1}{2p}\bigr)^{-p}$, a shift of the index. For $0<p<1$ the same $1/n$
terms hold, followed by an explicit term of order $n^{-1-p}$ that involves the zeta function:

$$n^pb_n = c(p)\Bigl(1-\frac{s-1}{2n}+\kappa_p\,n^{-1-p}+O(n^{-1-2p}+n^{-2})\Bigr),\qquad \kappa_p = 2p\,c(p)\,\zeta(-p) < 0,$$

with the same $\kappa_p$ term in $n^pa_n/(2c(p))$, so that it cancels in $a_n/(2b_n)$. Since $\kappa_p\ne0$, the
remainder $O(n^{-1-p})$ after the $1/n$ term cannot be improved when $p<1$. At $p=1$ and $s=\tfrac32$, comparison with
the explicitly solvable Tricomi–Carlitz measure also gives $b_n/b_n^{\mathrm{TC}} = 1-\tfrac{1}{24n^2}+O(n^{-3})$.
In averaged form, $\sum_{j\le n}\log\bigl(j^pb_j/c(p)\bigr) = -\tfrac{s-1}{2}\log n + C + o(1)$, and the pointwise law
holds uniformly for $s$ in compact intervals.

*Status:* proved, using the same Riemann–Hilbert citations as result 2. Each of the three ranges $p>1$, $p=1$ and
$0<p<1$ has passed two independent referee passes. These are the newest results; they are proved in full in Paper II.

### 4. Slowly varying weights

For every $p>0$, $s>1$ and **every** slowly varying factor $\ell$ (for example $\ell(k)=e^{\sqrt{\log k}}$, or any
bounded, logarithmic or iterated-logarithmic factor), the measure $\sum_k k^{-s}\ell(k)\,\delta_{k^{-p}}$ satisfies
$n^pb_n\to c(p)$ and $n^pa_n\to 2c(p)$. If $\log\ell(e^u)$ extends analytically to some horizontal strip
$|\operatorname{Im}u|\le\vartheta$ (bounded, with derivative tending to 0), the rate is $O(1/n)$.

*Status:* proved, using the same citations as result 2.

### 5. Christoffel shift and sharpness

*Shift.* For any positive measure $\sigma$ on $[0,\infty)$ with infinite support, $\sigma$ satisfies the law if and
only if $x\,\sigma$ does, and the rate carries over when it is regular. Since
$x\cdot\sigma_{p,s}=\sigma_{p,s+p}$, one base case gives every larger $s$. *Status:* proved (self-contained). The
underlying limit lemma is known (chain sequences; Dai–Piao–Qiao 2025); the rate transfer was not found in the
literature.

*Sharpness.* Slow variation of the weights cannot be weakened to boundedness: for every $p>0$, $s>1$ and every small
enough $\varepsilon>0$ there are weights $k^{-s}e^{f(k)}$ with $|f(k)|\le\varepsilon$ for which $n^pb_n$ does not
converge. A separate construction does the same for $n^pa_n$. *Status:* proved, using the citations of result 2.

### 6. The measure built from the zeros of $\zeta$

Let $\gamma_k$ be the ordinates of the nontrivial zeros of $\zeta$, taken as given real numbers, and
$\sigma=\sum_k 2x_k\delta_{x_k}$ with $x_k=1/(\gamma_k^2+\tfrac14)$. Without any hypothesis, $\log D_n$ lies within
$o(n^2)$ above and $O(n^2)$ below the value predicted by the averaged law. The averaged law holds if and only if an
energy that counts close pairs of zeros is $o(K^2)$. It follows from Montgomery's pair-correlation conjecture, without
assuming the Riemann Hypothesis. Proving it unconditionally would imply that asymptotically all zeros are simple and on
the critical line, so it is at least as hard as that open problem.

*Status:* proved, using cited bounds on the zero-counting function and cited pair-correlation results. This says nothing
for or against the Riemann Hypothesis.

---

## How much to trust these results

* **Not peer reviewed.** Nothing here has been refereed by a journal or read by a human specialist yet.
* **AI-assisted.** The research, proofs and write-ups were developed with an AI assistant (Claude Code, Anthropic).
  Every lemma went through an adversarial self-check and at least one independent AI referee pass before being marked
  `REVIEWED`. The referee reports are in `research/*/review/`. This trail is visible, but it is not a substitute for
  expert review.
* **Machine-checked where possible.** Result 1 (Paper 1's main theorem and its two corollaries) and the Christoffel
  shift are formalised in Lean 4 / Mathlib ([`lean/`](lean/README.md)). The Riemann–Hilbert results are not; they rely
  on large published theorems that are not in Mathlib.
* **Status labels** (defined in [VERIFICATION_POLICY.md](VERIFICATION_POLICY.md)), as used in
  [THEOREMS.md](THEOREMS.md):
  * `PROVED`: self-contained proof in the repository.
  * `PROVED-mod-cite (X)`: proved, assuming the external results X, each quoted with its exact hypotheses from a source
    that was read, and recorded in a `CITATIONS.md` file.
  * `CONDITIONAL`: proved under a stated hypothesis.
  * `NUMERICAL`: computed, not proved. `CONJECTURE`: supported by evidence, not proved.
  * `GAP`: a precise statement that is not proved.
* **Certified numerics.** "Certified" means interval (ball) arithmetic with Arb. The constants and closed forms quoted
  in the README and papers are certified in [`certified/`](certified/README.md).
* **Reproducible outputs.** `scripts/reproduce.sh` re-runs the certified suite and 47 numerical checks and compares each
  output byte for byte with the committed one. `MANIFEST.sha256` records the SHA-256 of every check, output, paper PDF
  and Lean file. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
* **Novelty.** A first literature search is summarised in THEOREMS.md. Many statements are still marked
  "novelty UNCHECKED", and some ingredients are known (for example the chain-sequence lemma behind the Christoffel
  shift).

---

## Papers

The work is written up as a series of three papers, each built around one question.

| | Title | Question | Status |
|---|---|---|---|
| I | [Hankel determinants of discrete measures with power-law atoms, and of zeta values](papers/paper1/main.pdf) | What is the $n^2$ term of $\log D_n$? (result 1) | release candidate, 19 pp ([`ARXIV.md`](papers/paper1/ARXIV.md)) |
| II | [Recurrence coefficients of discrete measures with power-law atoms: pointwise asymptotics and the $1/n$ term](papers/paperII/main.pdf) | Does each $n^pb_n$ converge, how fast, and what is the next term? (results 2, 3) | draft, 105 pp; all sections refereed (two independent mathematical referee passes) |
| III | [Stability and instability of recurrence asymptotics for discrete measures with power-law atoms](papers/paperIII/main.pdf) | Which weights keep the law, and which break it? (results 4, 5) | draft, 29 pp |

[`papers/paper2/`](papers/paper2/main.pdf) is the earlier combined draft that Papers II and III replace. Each paper folder
has a `NOTES.md` listing open items.

---|---|---|
| [`papers/paper1`](papers/paper1/main.pdf) | Hankel determinants of discrete measures with power-law atoms, and of zeta values | release candidate, 17 pp ([`ARXIV.md`](papers/paper1/ARXIV.md)) |
| [`papers/paper2`](papers/paper2/main.pdf) | Recurrence coefficients of discrete measures with power-law atoms and slowly varying weights | draft, 67 pp; being reorganised |

Each paper folder has a `NOTES.md` listing open items.

---

## Finding your way around

Start with this README, then the summary in [THEOREMS.md](THEOREMS.md) §1, then the papers. The `research/` folders
hold the full working proofs; they are long and written as lab notebooks.

| Path | Contents |
|---|---|
| [`THEOREMS.md`](THEOREMS.md) | index of every statement, with exact hypotheses, status labels, dependencies and open problems |
| `papers/` | paper drafts (LaTeX, PDF, numerical checks) |
| `research/G2/` | the averaged law (result 1): equilibrium problem, Hankel asymptotics |
| `research/G1/` | the pointwise law (results 2–5); `research/G1/RH/` holds the Riemann–Hilbert analyses |
| `research/G3prime/` | the measure built from zeta zeros (result 6) |
| `research/*/review/`, `research/*/checks/` | referee reports; numerical checks (scripts and outputs) |
| `lean/` | Lean 4 / Mathlib formalisation (result 1 in full, the Christoffel shift, supporting lemmas) |
| `certified/` | interval-arithmetic (Arb) verification of quoted constants and closed forms |
| `src/jacobi_asym/`, `tests/` | Python toolkit (measures, recurrence coefficients, Hankel determinants) and its tests |

**Glossary of internal names.** *Law P*: the limits $n^pb_n\to c(p)$, $n^pa_n\to2c(p)$. *G1, G2, G3′*: the three
original goals (pointwise law, averaged law, zeta-zero measure). *RH* in folder and file names means
**Riemann–Hilbert**, never the Riemann Hypothesis. *Plan N*: a unit of work. Plans are referenced in the logs and
review reports.

---

## Running the code

CI (GitHub Actions) runs on every push to `master`. It runs the fast test suite with the C kernel, the manifest check
and the certified-output comparison (`python.yml`; slow regressions weekly), and the Lean build with axiom audit
(`lean.yml`, when `lean/` changes).

```bash
scripts/setup_env.sh                     # .venv on top of the system numpy/scipy/mpmath/sympy (Python >= 3.12),
                                         # adds python-flint, builds the C kernel in csrc/ (needs gcc + libquadmath)
.venv/bin/python -m pytest               # fast suite
.venv/bin/python -m pytest -m slow       # slow regression tests (minutes)
scripts/reproduce.sh                     # build, tests, certified suite, numerical checks diffed against committed
                                         # outputs, Lean audit, manifest check (~5 min; --quick ~20 s)
python scripts/manifest.py --check       # verify MANIFEST.sha256
cd lean && ./check.sh                    # Lean build + axiom audit; prints AUDIT OK
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

## Provenance

This project continues item 11 of an earlier private notebook. Copied material and its sources are listed in
[PROVENANCE.md](PROVENANCE.md). Zeta-zero data come from A. Odlyzko's tables (`data/fetch.py`, with checksums).
Planning documents and working logs are not published, so a few cross-references to `LOG.md` files or plan documents
point to unpublished notes.

## License

MIT; see [LICENSE](LICENSE).
