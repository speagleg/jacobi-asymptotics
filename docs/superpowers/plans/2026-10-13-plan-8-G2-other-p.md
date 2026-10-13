# Plan 8: Research G2 (Theorem H for p ∉ {1, 2})

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native) to implement this plan task by
> task. Steps use checkbox (`- [ ]`) syntax.

**Goal.** Prove item 11's Theorem H, the averaged Law P

  log D_n = −p n² log n + κ_p n² + o(n²),  κ_p := 3p/2 + log c(p),

for every p > 0 (or the largest range the method reaches), for atoms x_k = Ck^{−p} and weights k^{−s}. Then transfer
it to regularly spaced atoms (item 11 H4) and weight sandwiches (item 11 H3, Lemma W). A proof would also settle the
Haynes–Zudilin a ≥ 3 case, det ζ(a(i+j)+b) (spec §7).

**Pre-plan evidence** (NUMERICAL, scratch runs on 2026-10-13, reproduced in Task 1):
- *Averaged law.* The toolkit gives S_n → 0 for p = 1.5, 3 and 4, with the same slow decay as the proved cases
  p = 1, 2. For p = 3: −0.112 (n = 50) → −0.008 (n = 1600).
- *Energy constant.* The constrained equilibrium constant
  E_p := sup{ I(μ) := ∬ log|u^{−p} − v^{−p}| dμ(u)dμ(v) : μ a probability measure on (0,∞), μ ≤ du }
  matches 3p/2 + log c(p) to discretization accuracy for p = 1, 2, 3, 4 and 1.5:

  | p | E_p − (3p/2 + log c(p)) |
  |---|---|
  | 1 | +0.0003 |
  | 2 | +0.0005 |
  | 3 | +0.0006 |
  | 4 | +0.0006 |
  | 1.5 | +0.0004 |

  The optimizer saturates the constraint on (0, u_s] (u_s ≈ 0.35, 0.52, 0.69) and has a free part extending to
  large u.

**Architecture.** There are two parts.
- **Part A (variational limit, target PROVED).** For the pure power, (1/n²)[log D_n + p n² log n] → E_p. This is
  self-contained:
  - Upper bound: D_n ≤ (Σw)^n · sup_S V(S), with a discretization inequality bounding log V(S) by n²·I(smeared μ_S).
  - Lower bound: one Heine term, at a quantile discretization of a truncated optimizer.

  This replaces item 11's exact reference families, so it needs no Lommel or Tricomi–Carlitz input.
- **Part B (identify the constant).** E_p = 3p/2 + log c(p).
  - Route B1 (preferred): solve the constrained problem in closed form. The constraint is a power law, so the problem
    is scale-covariant and a Mellin-transform solution is plausible. The Beta function in I(p) suggests one.
  - Route B2 (fallback): use a reference Jacobi matrix with b_j = c(p)j^{−p}, a_j = 2b_j. H2 gives its D_n exactly,
    with constant κ_p. Item 11's Theorem B gives its atom counting. A Part A′ universality theorem (the constant
    depends only on the atom counting, given sub-exponential weights and no clumping) would then identify the two.
  - If both fail: Theorem H holds with κ_p = E_p (PROVED), and E_p = 3p/2 + log c(p) is NUMERICAL to the digits
    reached. That is a precise missing step.

**Tech stack.** The Python toolkit (rkpw ld/q, mpmath) and a constrained-energy solver (Frank–Wolfe on geometric grids;
a solver with a certified bound if B1 fails). Lean is out of scope; a later plan can follow Rule R acceptance.

**Spec.** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` §7 (G2), §8 (stop conditions). Math source:
item 11 PROOF.md §7 (Theorem H, H1–H4), §3 (Theorem B), and the weyl.py constants (I(p), c(p)).

## Global Constraints

- AGENTS.md rules 1–7: citation gate, labels, no RH framing, Rule A for every lemma, Rule R before REVIEWED.
- Commit prefix `G2:` (`toolkit:` for solver code). Co-Authored-By trailer.
- Work in `research/G2/{PROOF.md, LOG.md, CITATIONS.md, checks/, review/}` on branch `plan-8-G2`.

## Review Focus

1. **Discretization inequality (Part A, upper).** Point Vandermonde against smeared energy. Diagonal and adjacent
   cells must cost O(n log n) uniformly over all n-subsets of ℕ, including subsets with huge indices.
2. **Optimizer support.** The free part of μ* extends to large u. The lower bound must truncate it, at an energy cost
   → 0, with weights k^{−s} on indices up to Un costing only O(n log(Un)).
3. **The range of p.** Check whether p ≤ 1 or p → 0 changes anything: convergence of ∬ log near u → ∞ for small p,
   and Σw < ∞.
4. **Weights.** Which s₀(p) the transfer needs. Part A has a lower bound for any polynomial weights, and an upper
   bound needing only Σw < ∞. The H3/W transfer may make s₀ trivial.
5. **The p = 1, 2 sanity checks.** Part A plus B must reproduce item 11's κ₁ and κ₂ exactly.

---

### Task 1: Workspace, numerics to the precision B needs

**Files:** `research/G2/{PROOF.md, LOG.md, CITATIONS.md}`, `research/G2/checks/check_averaged.py` + `.out`,
`research/G2/checks/check_energy.py` + `.out`.

- [ ] **Step 1. Averaged law** for p ∈ {0.5, 1.5, 3, 4, 6}. Do K-doubling and ld vs q precision (Rule N). Report S_n
  and S_n·log n.
- [ ] **Step 2. E_p** on geometric grids, with N-doubling and umax-doubling, plus Richardson extrapolation, for
  p ∈ {0.5, 1, 1.5, 2, 3, 4, 6}. Report E_p − κ_p and the saturation point u_s(p). Also report the optimizer density
  on the free part, to suggest a closed form for B1. Expected: |E_p − κ_p| ≤ 1e−4 after extrapolation.
- [ ] **Step 3. Commit** `G2: workspace + numerics (averaged law all p, constrained energy E_p)`.

### Task 2: Citations

- [ ] Read and quote, with hypotheses, from arXiv or other sources actually read. Candidates:
  - Dragnev–Saff, constrained energy problems (J. Anal. Math. 1997);
  - Rakhmanov, equilibrium measure and the distribution of zeros of extremal polynomials of a discrete variable
    (Sb. Math. 1996);
  - Kuijlaars–Van Assche, Proc. LMS 1999 (extremal polynomials on discrete sets);
  - Kuijlaars–Rakhmanov 1998 (varying recurrence coefficients).

  Needed: existence, uniqueness and characterization (variational inequalities) of the constrained minimizer on
  unbounded sets with a non-integrable constraint near 0. Anything unread is GAP. Part A is written to be
  self-contained, so these citations matter only for B1's characterization of μ*.
- [ ] **Commit** `G2: citations`.

### Task 3: Part A (variational limit for the pure power)

- [ ] **Lemma A1 (existence).** E_p is finite and attained.
  - Upper semicontinuity of I on {μ ≤ du} under a tightness argument.
  - Finiteness: I(μ) ≤ C, because log|u^{−p} − v^{−p}| ≤ log(u^{−p} + v^{−p}) and the mass of μ near 0 is ≤ u.
- [ ] **Lemma A2 (discretization, upper).** For every n-subset S = {k_i} of ℕ, with u_i := k_i/n and μ̄_S the smeared
  measure (density 1 on each [(k_i − 1)/n, k_i/n]):
  Σ_{i≠j} log|u_i^{−p} − u_j^{−p}| ≤ n² I(μ̄_S) + C n log n, with C uniform in S. Rule A: check numerically on random
  and extreme S, such as consecutive blocks and geometric sequences.
- [ ] **Theorem A-U.** D_n ≤ (Σw)^n sup_S term-free V(S), so limsup (1/n²)[log D_n + p n² log n] ≤ E_p.
- [ ] **Theorem A-L.**
  - Take μ* truncated to [0, U], with I ≥ E_p − ε(U).
  - Take quantile integers k_i := ⌈n F*^{−1}(i/n)⌉. These are distinct because the density is ≤ 1.
  - Show log V(S*) ≥ n² I(μ*_U) − o(n²) and log Π w ≥ −s n log(Un).
- [ ] **Corollary A.** Combined with item 11's H4 (atoms) and H3/W (weights): for any regularly spaced atoms with
  constant C and weights sandwiched between polynomial powers, log D_n = −p n² log n + (E_p + log C)n² + o(n²).
- [ ] **Rule A pass; commit** `G2: Part A — Theorem H with variational constant E_p, all p`.

### Task 4: Part B (E_p = 3p/2 + log c(p))

- [ ] **Route B1.** Write the Euler–Lagrange conditions for μ*: saturated on (0, u_s], free beyond, with the
  potential condition on the free set. Solve via Mellin transform or a scaling ansatz, guided by the Task 1 density
  data. Compute I(μ*) in closed form and compare with κ_p. Check p = 1, 2 against item 11.
- [ ] **Route B2** (if B1 stalls by end of session). Write Part A′ (universality in the counting function) and check
  its hypotheses for the reference Jacobi matrix b_j = c(p)j^{−p}: counting via Theorem B, weights sub-exponential,
  no clumping. Record which hypothesis is missing.
- [ ] **Exit** in either case: Theorem H for p ∉ {1, 2} is either PROVED with κ_p, or PROVED with E_p, with the identity
  E_p = κ_p NUMERICAL and a precise missing step.
- [ ] **Commit** `G2: Part B — identification of E_p`.

### Task 5: Consequences and status

- [ ] Haynes–Zudilin: det ζ(a(i+j)+b) for a ≥ 3, with the covered b-range.
- [ ] Monien-type corollaries for p ∉ {1, 2}.
- [ ] PROOF.md status table, README and spec §7 notes.
- [ ] **Commit** `docs: G2 status`.

### Task 6: Rule R

- [ ] An independent reviewer (opus) on PROOF.md, CITATIONS.md, checks and this Review Focus. Apply fixes and mark
  REVIEWED. Commit `G2: Rule R review + fixes`.
