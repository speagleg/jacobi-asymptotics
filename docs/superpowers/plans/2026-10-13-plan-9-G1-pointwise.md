# Plan 9: Research G1 (the pointwise Law P), time-boxed

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native). Steps use checkbox (`- [ ]`)
> syntax.

**Goal.** Item 11 §9 G1. Let x_k = f(k) be regularly spaced with index −p (H-a), and let the weights be sub-exponential
or polynomially sandwiched. Prove, or reduce as far as possible, the pointwise law

  (b) n^p b_n → c(p)C,   (a) a_n/(2b_n) → 1.

The spec says G1 is **time-boxed**, with the exit "stop and report as soon as the problem is shown to be equivalent
to, or as hard as, a known open problem".

**New leverage since item 11.** G2's Theorem H_all gives the averaged law for every p > 0, with weights only needing
Σw < ∞ plus a polynomial lower bound. In terms of u_j := log(j^p b_j/(c(p)C)) it reads

  G(n) := Σ_{j<n}(n−j)u_j = o(n²).

The second difference of G is u, and G(n+h) − 2G(n) + G(n−h) = Σ_j K_h(j−n)u_j, a triangle kernel of mass h². So
windowed averages of u over windows of width δn are o(1)/δ². A Tauberian condition on u then gives pointwise
convergence.

**Planned results.**
- **(G1-T) Tauberian reduction (target PROVED).** Under H_all's hypotheses, if β_n := n^p b_n is slowly oscillating
  ((T3) of item 11: ω(δ) := limsup_n sup_{n≤m≤(1+δ)n}|β_m/β_n − 1| → 0) and bounded above and below, then
  β_n → c(p)C. Unlike item 11's C′, this needs no (T2), no (T4) and no Wiener.
- **(G1-L) Landau upgrade (target PROVED).** If only limsup β_n < ∞ holds (a one-sided bound), then the single
  geometric Cesàro mean converges: (1/n)Σ_{j≤n} log(j^p b_j) → log(c(p)C). This is item 11's "single average"
  remark, now unconditional in p.
- **(G1-a) The a_n side (attempt).** Given β_n → c(p)C and the weight condition, derive a_n/(2b_n) → 1, at least in
  Cesàro mean. Use the trace identities Tr J^m = Σ_k x_k^m for m > 1/p and a generalized Weyl law with b_n regular,
  or Lemma P/E-type arguments (item 11 §4) in liminf/limsup form.
- **(G1-R) The regularity core (time-boxed attempt, then stop report).** (T3) for b_n, from atom regularity alone.
  Candidate routes:
  - local versions of Theorem H_all, i.e. windowed energy problems;
  - discrete Riemann–Hilbert (Wu–Lin–Xu–Zhao type);
  - comparison with exact families.

  Item 11's test A3 shows that coefficient oscillations decay only like a power of n when weights oscillate on the atom
  scale. Exit: a proof, or a precise statement of the missing a priori estimate, with literature status.

**Spec.** §7 G1, §8. Math sources:
- item 11 §4 (Lemma P, Lemma E), §5 (C, D), §6 (C′), §8 (test A3), §9 G1;
- research/G2/PROOF.md (H_all).

## Global Constraints

- AGENTS.md rules 1–7. Commit prefix `G1:`. Work in `research/G1/{PROOF.md, LOG.md, CITATIONS.md, checks/, review/}`
  on branch `plan-9-G1`.
- **Time box.** Task 4 (G1-R) gets one focused session. Then write the stop report whatever the outcome.

## Review Focus

1. **G1-T kernel algebra.** The second difference of G over ±h equals a triangle-kernel sum of u, and o(n²)/(δn)² → 0
   for fixed δ. Check the uniformity of the slow-oscillation estimate inside the window.
2. **Which bounds G1-T needs.** Is the lower bound on β_n needed (log β must stay bounded below for u to be bounded)?
   Can it be dropped using a one-sided Landau argument?
3. **G1-a.** Do not assume (T2) anywhere in a proof of (T2). Avoid circularity with Theorem C, which assumes limits.
4. **Numerics.** Distinguish slow convergence (A3-type power decay) from non-convergence.
5. **Novelty.** Pointwise ratio asymptotics for discrete measures accumulating at 0 may exist in the literature
   (Kuijlaars–Van Assche, Wu–Lin–Xu–Zhao, Damanik–Simon-type inverse spectral results). Check before claiming.

---

### Task 1: Workspace and regularity numerics

**Files:** `research/G1/{PROOF.md, LOG.md, CITATIONS.md}`, `research/G1/checks/check_regularity.py` + `.out`.

- [ ] For p ∈ {1, 2, 3} and weight classes:
  - k^{−s} for s ∈ {p, 2p, 6};
  - log-periodic modulation k^{−s}(2 + sin log k);
  - parity oscillation k^{−s}(2 + (−1)^k) (item 11's A3);
  - smooth ζ-model atoms with weights 2x_k.

  Compute β_n = n^p b_n and a_n/(2b_n) to n ≈ 4000 (rkpw ld, K-doubling; Rule N). Report:
  - |β_n − c(p)C| and |a_n/(2b_n) − 1| at log-spaced n, with fitted decay exponents;
  - the empirical slow-oscillation modulus ω_n(δ) for δ ∈ {0.1, 0.5};
  - monotonicity violations of b_n (for item 11's (T4)).
- [ ] **Expected.** Convergence in every class, with power-rate decay in the oscillating-weight classes. Any
  non-convergence is a stop-and-record finding.
- [ ] **Commit** `G1: workspace + regularity numerics`.

### Task 2: G1-T and G1-L (Tauberian reductions)

- [ ] Write G1-T with a full proof:
  - the triangle-kernel identity;
  - the window estimate u_n = (windowed average) ± ω-terms;
  - log-boundedness;
  - the limit.
- [ ] Write G1-L: Landau's one-sided argument from G(n) = o(n²) and u_j ≤ M.
- [ ] Rule A: numerically check the kernel identity, and test G1-T's conclusion on synthetic sequences: a slowly
  oscillating sequence with a zero double-average converges; a fast oscillating one need not.
- [ ] **Commit** `G1: Tauberian reductions (G1-T, G1-L)`.

### Task 3: G1-a (the a_n side)

- [ ] Attempt the following, in order:
  1. Prove liminf/limsup versions of item 11's Lemma P (J ≥ 0 ⇒ liminf a_n/(2b_n) ≥ 1 in Cesàro mean?) and Lemma E
     (an excess a_n ≥ (1+η)(b_{n−1} + b_n) on a set of positive upper density forces exponentially small weights on a
     corresponding set of atoms?).
  2. A trace-identity argument: with β_n → c(p)C, compare Σ_n φ_m(a_n, b_n) with Σ_k x_k^m = C^m ζ(pm)(1 + o(1))-type
     asymptotics as m ↓ 1/p.
- [ ] Record what is proved, and the precise missing step.
- [ ] **Commit** `G1: a_n side`.

### Task 4: G1-R (the regularity core; time-boxed) and the stop report

- [ ] Literature pass for ratio asymptotics of discrete OPs with an accumulation point. Read and quote what applies,
  per the citation gate.
- [ ] Attempt (T3) via local energy problems. Can windowed versions of A-U/A-L (Heine sums restricted to index windows)
  control b_n over windows of width δn?
- [ ] Write the stop report in LOG.md: the exact remaining statement, why the attempted routes fail, and the literature
  status. Label it.
- [ ] **Commit** `G1: regularity core attempt + stop report`.

### Task 5: Status and Rule R

- [ ] PROOF.md status table, README and spec notes.
- [ ] An independent reviewer (opus) on PROOF.md, CITATIONS.md, checks and this Review Focus. Apply fixes and mark
  REVIEWED.
- [ ] **Commit** `G1: Rule R review + fixes`.
