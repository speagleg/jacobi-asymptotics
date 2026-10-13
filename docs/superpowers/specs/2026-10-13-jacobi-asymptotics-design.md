# jacobi-asymptotics: design spec

Date: 2026-10-13. Status: draft for review.

## 1. Purpose

The repo has two purposes:
- **(b) Library.** A reusable toolkit for the Jacobi-coefficient and Hankel-determinant asymptotics of discrete
  positive measures Σ w_k δ_{x_k} that accumulate at 0.
- **(c) Research workspace.** A place to close the open problems of math-pursuits item 11 ("Law P"). The toolkit and a
  Lean 4 library support that work.

Success means four things:
1. The toolkit is installable and tested. It reproduces every recorded item-11 number it ports.
2. The Lean library builds with no `sorry`. Every theorem depends only on the standard axioms plus explicitly named
   input hypotheses.
3. Each of the open problems G3′, G2 and G1 ends in one of two states:
   - a proof that has been reviewed by a second reader and formalized where feasible; or
   - a written obstruction, following the stop conditions in §8.
4. Nothing is framed as evidence for RH (item 11, E1).

## 2. Background (from math-pursuits item 11, commit f5f6aef)

**Law P.** Suppose J is a positive compact Jacobi operator whose spectral measure has atoms x_k ~ C k^{−p}. Then:
- a_n/(2b_n) → 1;
- b_n/x_n → c(p) = ¼(π/(2I(p)))^p, where I(p) = (√π/2)Γ(1/p+½)/Γ(1/p+1);
- in particular c(2) = π²/16.

**Already proved and reviewed in item 11** (`items/11-*/work/proof/PROOF.md`):
- Theorem A: the Lommel family is exact.
- Theorem B: the forward Weyl law.
- Lemma P and Lemma E (tunnelling).
- Theorem C: a conditional inverse.
- Proposition D: the weight hypothesis is necessary.
- Theorem C′: a Tauberian inverse, relying on Wiener's theorem.
- Theorem H: the averaged Hankel law for p ∈ {1, 2}. The p = 1 case relies on the Tricomi–Carlitz measure.
- Theorem H_L: slowly varying atoms. This gives the averaged law with c(2) = π²/16 for the smooth ζ model.

**Open problems:**
- **G3′.** The averaged law for the measure built from the true ζ zeros, with ordinates taken as real.
- **G2.** Theorem H (the averaged law) for p ∉ {1, 2}.
- **G1.** The pointwise law: a priori regularity of n^p b_n, and a_n ~ 2b_n.

## 3. Repo and governance

- **Location.** `/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/`, a new git repo with no remote for now.
- **Sources are read-only.** math-pursuits (and the repos it draws from) are read-only sources. Material copied from
  them is recorded in `PROVENANCE.md` with the source path and commit. Corrections to math-pursuits go into its
  `FIXES.md`, through a human.
- **Rules.** `AGENTS.md` and `VERIFICATION_POLICY.md` are adapted from math-pursuits and keep these rules:
  - **Citation gate.** Every external theorem is quoted with its hypotheses from a source that someone has actually
    read.
  - **Certification.** "Certified" means ball or interval arithmetic with explicit tail bounds. High-precision floats
    are "numerical".
  - **Adversarial pass (Rule A).** It is recorded for every lemma.
  - **Second reader (Rule R).** A result is labelled REVIEWED only after a second reader, either a human or an
    independent agent, has checked it.
  - **Labels.** PROVED, PROVED-mod-cite, PROVED-mod-input, NUMERICAL and GAP.
  - **Framing.** No RH, GRH or Langlands framing.
  - **Commits.** Each commit message is prefixed with its area: `toolkit:`, `lean:`, `G3p:`, `G2:`, `G1:`, `docs:`.

## 4. Layout

```
jacobi-asymptotics/
  AGENTS.md  VERIFICATION_POLICY.md  README.md  PROVENANCE.md  pyproject.toml
  csrc/rkpw.c                     RKPW kernel (double / long double / binary128), from item 11
  src/jacobi_asym/
    measures/  base.py            DiscreteMeasure
               powers.py          pure powers C k^{-p}, weights k^{-s}
               lommel.py          Lommel family (Theorem A), exact coefficients
               tricomi_carlitz.py Tricomi–Carlitz family, exact coefficients
               smooth.py          smooth Riemann–von Mangoldt models (ζ, Dirichlet L, conductor q)
               zeros.py           true zeros: Odlyzko tables, PARI lfunzeros (with gap checks)
               synthetic.py       CUE / Poisson / jitter unfolded models
    jacobi/    rkpw.py            wrapper around the compiled kernels
               lanczos.py         float64 Lanczos with full reorthogonalisation (cross-check)
               mp.py              mpmath Stieltjes / Chebyshev (small n, high precision)
    hankel/    logdet.py          log D_n via H2
               heine.py           exact Heine sums (small n), Andreief checks
               compare.py         difference-ratio tools (Lemmas H4, H5)
    laws/      weyl.py            I(p), c(p), K(α,β,p), Weyl-law inversion (Law-P prediction)
               averaged.py        S_n and the related averaged statistics
    certify/   arb.py             python-flint ball-arithmetic versions of the certifiable pieces
  tests/                          pytest
  lean/                           Lean 4 project (lakefile, toolchain v4.34.1, Mathlib v4.34.1)
    JacobiAsym/  Inputs.lean  Heine.lean  Hankel.lean  RatioBounds.lean  SlowVariation.lean
                 TailCut.lean  TheoremHL.lean  WeylToeplitz.lean  LemmaP.lean
  research/  G3prime/  G2/  G1/   each: PROOF.md, checks/, review/, LOG.md
  data/      fetch.py + SHA256SUMS (large data is fetched, not committed)
  docs/superpowers/{specs,plans}/
```

## 5. Toolkit

**Core type.**
- `DiscreteMeasure(atoms, weights, tail=None)` has these invariants:
  - atoms are strictly decreasing and positive;
  - weights are positive;
  - the total mass is finite.
- `tail` is an optional quadrature for a smooth continuation (as in item 11's `measures.build`).
- Constructors include `pure_power(p, s, K)`, `lommel(nu, K)`, `tricomi_carlitz(alpha, K)`, `smooth_zeta(K, q=1)`,
  `true_zeta(M, tail=True)` and `from_atoms(x, w)`.

**Main functions.**
- `jacobi_coeffs(mu, n, method='rkpw'|'lanczos'|'mp', prec='d'|'ld'|'q')` returns arrays a[1..n] and b[1..n].
- `log_hankel(mu, n)` returns log D_n via H2.
- `lawP_prediction(mu, n)` gives the Weyl-inversion prediction b_n^W (item-11 note, (P)).
- `averaged_law(b, x, p)` returns S_n = (2/n²)Σ(n−j) log(b_j/x_j) − log c(p) on a grid of n.
- `reference_coeffs(family, n)` gives exact rational or closed-form coefficients for Lommel and Tricomi–Carlitz.

**Precision policy.** Float results are tagged with their method and precision. Only functions in `certify/` return
balls, and only those may be described as certified.

**Data.**
- Odlyzko `zeros6` (sha256 as in item 11) and PARI zero lists are fetched or regenerated by `data/fetch.py`.
- The `.npy`, `.npz` and raw zero files are gitignored. Small reference tables, under 1 MB, are committed.

## 6. Lean library (ambition level A)

> **Scope update (2026-10-13, Plan 2).** Mathlib v4.34.1 has neither Cauchy–Binet nor Hadamard's inequality. The
> Lean core is therefore split: Plan 2 (foundations on finite Heine sums; Hadamard replaced by e_m ≤ (Σw)^m),
> Plan 3 (assembly of H ⇒ H_L, Lemma P, Toeplitz), and a later plan (Andreief/Cauchy–Binet, H2, K → ∞). The list
> below is the target across those plans, not what currently exists; see lean/README.md for the current state.
> Plan 3 done: theoremHL, lemmaP. The Toeplitz count and the smooth-ζ `SlowFactor` instance moved to the bridge plan.
> Plan 4 done: Cauchy–Binet, Andreief, K → ∞, smooth-ζ instance, Corollary H_L-ζ (Hankel-determinant form).
> Plan 5 done: orthogonal polynomials, three-term recurrence, H2, b_j form of Corollary H_L-ζ.
> Plan 6 done: Toeplitz eigenvalue count (S4) in `Toeplitz.lean` (planned as WeylToeplitz.lean). Lean bridge complete.
> Plan 7 (G3′): U unconditional (mod-cite), L mod (SG), Prop N (counting info insufficient), GAP N′; stop condition recorded in research/G3prime/LOG.md.
> Plan 8 (G2): Theorem H for all p > 0 via the explicit constrained equilibrium μ* = ∫ω_{[0,4c t^{−p}]}dt (E_p = κ_p); Haynes–Zudilin corollary; Rule R REVIEWED (Monien p = 1 prior art recorded).
> Plan 9 (G1): G1-T (H_all + (T3) ⇒ pointwise b-law), G1-L, A1–A4 (a-side, A4 mod (CL)); stop report GAP ((T3), (CL)); Rule R REVIEWED (A4 density claim withdrawn).
> Plan 10 (RH): Theorem RH₁ (pointwise Law P, p = 1, r = 3/2) PROVED-mod-cite + REVIEWED; general r and p = 2 are proof sketches (review lists the missing steps).
> Plan 11 (RH general r): Theorem RH₁(r), pointwise Law P with O(1/n) rate for all r > 1 at p = 1, PROVED-mod-cite + REVIEWED (RH/RH_p1_general.md). p = 2 still a sketch.
> Plan 12 (RH general p): Theorem RH_p, pointwise Law P with O(1/n) rate for all p > 1, s > 1 (x-variable, hard-edge Bessel), PROVED-mod-cite + REVIEWED (RH/px/RH_px.md). Open: 0 < p < 1.

**Toolchain.** Lean 4.34.1 and Mathlib v4.34.1, the same versions math-pursuits uses. The Mathlib build cache is
reused through a `.lake` symlink, so Mathlib is not downloaded again. `autoImplicit` is off.

**Formalized, with no `sorry`:**
- **Heine / Andreief.** For finite atom sets:
  D_n = Σ_{S, |S|=n} Π w · Π_{i<j}(x_i − x_j)².
  This is extended to summable infinite families via `tsum` over finsets of size n.
- **H2.** D_n = m₀ⁿ Π_{j<n} b_j^{2(n−j)}, stated for the finite Gram–Schmidt / LDLᵀ data.
- **H3.** Monotonicity, log-convexity and scaling.
- **H4, H5.** Difference-ratio comparison, via Cauchy's mean value theorem.
- **H6.** The slow-variation lemmas.
- **H7.** The tail cut. The proof uses the Hadamard inequality for PSD matrices (from Mathlib if available, otherwise
  proved here) and the bound φ_M ≤ A²/(4p log M).
- **Theorem H ⇒ Theorem H_L.** The deduction, with Theorem H for pure powers as a hypothesis.
- **Lemma P.**
- **Theorem B's Toeplitz part.** The Toeplitz eigenvalue count for tridiagonal Toeplitz matrices.

**Named inputs** (`Inputs.lean`, as `structure`s passed as hypotheses, never `axiom`s):
- `TheoremH_pure p` (from Theorem A and Tricomi–Carlitz);
- `WienerTauberian`;
- facts about the ζ smooth model that are not worth formalizing, such as the Lambert-W inverse.

**Acceptance.** `lake build` passes, and `#print axioms` on every main theorem lists only `propext`,
`Classical.choice` and `Quot.sound`.

## 7. Research track

Work happens in this order. Each problem has its own `PROOF.md`, check scripts, Rule A log and Rule R review.

**G3′ (true zeros).** Target: the averaged law S_n → 0 for the measure built from the true ordinates.
- *Upper bound.* Compare true atoms with smooth ones using |γ_k − γ̃_k| = O(1). This follows unconditionally from
  S(T) = O(log T), which must be cited from a source we have read (Titchmarsh §9).
- *Lower bound.* The Heine sum is a sum of nonnegative terms, so it is bounded below by configurations that avoid a
  sparse set of bad indices: close pairs and multiple zeros. Show that the cost is o(n²), using the unconditional
  multiplicity bound m(γ) ≪ log γ.
- *Exit.* A reviewed proof, with Lean for the combinatorial core. Or, if the deletion argument fails, a precise
  statement of what is missing.

**G2 (p ∉ {1, 2}).**
1. Literature pass, read from the sources: Kuijlaars–Van Assche (Proc. LMS 1999), Dragnev–Saff, Rakhmanov, and
   constrained equilibrium in Monien's variable u = 1/x.
2. Attempt the averaged law via nth-root asymptotics, i.e. the n² constant of log D_n from a constrained energy
   problem. Alternatively, find a new exactly solvable reference family.

Exit: a proof, or a precise missing step. A proof would also settle the Haynes–Zudilin a ≥ 3 case.

**G1 (pointwise law).** Time-boxed.
- Candidate routes:
  - a priori ratio asymptotics from a discrete Riemann–Hilbert analysis (Wu–Lin–Xu–Zhao type);
  - comparison and perturbation from the exact families.
- Stop and report as soon as the problem is shown to be equivalent to, or as hard as, a known open problem.

## 8. Stop conditions

These carry over from math-pursuits §5. Stop and write it up in the problem's LOG.md if any of these happens:
- a step is as hard as an open problem;
- a claimed statement has a counterexample;
- the result turns out to be known (record the reference);
- a needed citation cannot be verified from a source;
- work would require editing a read-only source repo.

## 9. Testing

**pytest.**
- Exact families: computed coefficients match the closed forms of Theorem A and the Tricomi–Carlitz family
  (b_j² = 1/(2j(2j+1))) to working precision.
- Cross-method: RKPW and Lanczos agree to ≤ 1e−12 relative on 10⁵-atom measures; RKPW and mpmath agree for n ≤ 200.
- Regression against item 11:
  - A10 reproduction (4e−14);
  - S_n values for the smooth and true ζ models (`check_hankel_L.out` [3]), when the data is present;
  - the H_L adversarial table.

  Tests that need fetched data are skipped if the data is absent.
- `certify/`: the balls contain the float values, and the radii are reported.

**Lean.** CI-style script `lean/check.sh` runs `lake build` plus the axioms audit.

## 10. Environment

- **Python.** A project `.venv` with `--system-site-packages`, so numpy, scipy, mpmath and sympy come from the system.
  It adds only `python-flint` and `pytest`. Nothing is installed into shared environments.
- **Build.** The C kernels are built by `make -C csrc` with the system gcc (quadmath for binary128).
- **Lean.** The WSL elan (`$HOME/.elan`).

## 11. Build order (one plan each)

1. Repo scaffolding: rules, provenance, item-11 material copied in.
2. Toolkit port and tests.
3. Lean core.
4. Research G3′.
5. Research G2.
6. Research G1.

## 12. Out of scope

- Continuous or absolutely continuous measures, and general orthogonal-polynomial theory (YAGNI, option 3 rejected).
- Formalizing Bessel functions or Wiener's theorem in Lean (ambition levels B and C rejected).
- Publishing, or a GitHub remote, until a human asks for it.
