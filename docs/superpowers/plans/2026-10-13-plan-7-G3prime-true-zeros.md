# Plan 7: Research G3′ (averaged Law P for the true-zero measure)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Settle G3′ of spec §7. For the measure σ = Σ_k 2x_k δ_{x_k}, with x_k = 1/(γ_k² + ¼) and the ζ ordinates
γ_1 ≤ γ_2 ≤ … taken as real numbers and listed with multiplicity, decide whether

  log D_n(σ) = −2n² log n + 2Σ_{j<n}(n−j) log L(j) + κ n² + o(n²),  with L(j) = j² x̃_j and κ = 3 + log(π²/16)

holds. That is, decide whether the true-zero measure has the same n² asymptotics as the smooth model of Corollary
H_L-ζ, where x̃_j = 1/(γ̃_j² + ¼) and γ̃_j = N₀⁻¹(j − ½).

**Expected outcome**, from the pre-plan analysis. The tasks below test each part; none of it is assumed.
- **(U) Upper bound, unconditional:** limsup (1/n²)[log D_n(σ) − RHS] ≤ 0. The proof reuses the H_L upper-bound
  structure (Lemma H5 ratios, H7 tail cut). The one new input is |γ_k − γ̃_k| = O(1), from S(T) = O(log T).
- **(L) Lower bound, conditional** on a small-gaps hypothesis (SG): for every η > 0 there is δ > 0 such that the
  upper density of {k : γ_{k+1} − γ_k < δ·2π/log γ_k} is at most η. The proof deletes the bad indices and compares
  pair ratios on the good ones, using an index-shift lemma that costs at most 3n² log(1+η).
- **(N) Necessity:** the unconditional lower bound would be about as hard as "almost all zeros are simple"
  (density 1), which is open. The heuristic: a fraction φ of repeated indices removes distinct atoms and shifts the n²
  constant by about 2 log(1−φ). Proposition N tries to prove the needed deletion lemma for the smooth measure. If that
  fails, (N) is recorded as NUMERICAL with a precise missing step. Either way, the stop condition "as hard as an open
  problem" is written up in LOG.md.

**Architecture:** This is a research plan. The deliverables are `research/G3prime/{PROOF.md, LOG.md, CITATIONS.md,
checks/*.py + .out, review/}`, plus one toolkit helper with tests. Math tasks end in a written, labelled statement,
not a test. Every numerical claim comes from a committed check script and its `.out` file.

**Tech Stack:** Python toolkit (`jacobi_asym`, rkpw double), with Odlyzko zeros6 data (2·10⁶ ordinates, present in
`data/raw`). Lean is not used here; formalizing (U)/(L) is a follow-up plan, gated on Rule R acceptance (Task 7).

**Spec:** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` §7 (G3′), §8 (stop conditions).
Math source: math-pursuits item 11 `PROOF.md` §7b (H5, H6, H7, the H_L proof, "What H_L does not cover").

## Global Constraints

- AGENTS.md rules 1–7. In particular, there is no RH framing: the ordinates are inputs taken as real (item 11, E1),
  and simple-zero statements are quoted as literature facts only.
- **Citation gate:** every external theorem is quoted with its hypotheses from a source actually read (arXiv/WebFetch
  allowed). A citation that can't be read is labelled GAP, never PROVED-mod-cite.
- **Labels:** PROVED, PROVED-mod-cite, PROVED-mod-input, NUMERICAL, GAP. Nothing is REVIEWED without Rule R.
- Commit prefix `G3p:` (`toolkit:` for the helper). Co-Authored-By trailer as in previous plans.
- Branch `plan-7-G3prime` from `master`.

## Review Focus

1. **Multiplicity convention.** Atoms are indexed with multiplicity, so a repeated ordinate gives x_k = x_{k+1}. The
   Heine sum over index subsets then gives such terms weight 0, which is consistent with merging the atom and adding
   its weights. Check that every lemma uses one convention.
2. **Uniformity of |γ_k − γ̃_k| ≤ C₀.** This must hold for all k ≥ 1, not just large k, and the derivation from
   S(T) must handle N(γ_k) ≠ k at multiple zeros.
3. **Tail pairs in (U).** The ratio bound 1 + O(log γ_b/(b−a)) is unbounded for huge indices, so the tail must be
   rescaled exactly, as in H_L, and never compared pair by pair.
4. **Index-shift lemma in (L).** The cost of a factor (1+η)⁻³ per pair must not hide a dependence on n.
5. **Numerical normalization.** S_n must be computed with the true x_j (the statement) as well as with the smooth
   x̃_j (item 11's convention), and the two must not be conflated.

---

### Task 1: Workspace and sensitivity probe (numerical)

**Files:**
- Create: `research/G3prime/{PROOF.md, LOG.md, CITATIONS.md}`, `research/G3prime/checks/check_merge.py`,
  `research/G3prime/checks/check_merge.out`
- Modify: `src/jacobi_asym/measures/lfun.py` (add `merge_repeats`)
- Test: `tests/test_merge_repeats.py`

**Interfaces:**
- Produces: `merge_repeats(gammas, idx) -> np.ndarray`. It returns a copy of `gammas` in which γ_{k+1} := γ_k for each
  k in `idx` (0-based), giving synthetic double zeros. Measures are built with `zero_measure` as before; equal atoms
  are merged by `DiscreteMeasure.from_atoms`, or the check aggregates them first if it doesn't.

- [ ] **Step 1: Write the failing test**

```python
import numpy as np
from jacobi_asym.measures.lfun import merge_repeats, model_zeros

def test_merge_repeats_sets_pairs_equal_and_preserves_order():
    g = model_zeros(10)
    h = merge_repeats(g, [2, 5])
    assert h[3] == g[2] and h[6] == g[5]
    assert np.all(np.diff(h) >= 0)
    assert np.array_equal(np.delete(h, [3, 6]), np.delete(g, [3, 6]))

def test_merge_repeats_rejects_adjacent_overlap():
    import pytest
    with pytest.raises(ValueError):
        merge_repeats(model_zeros(10), [2, 3])
```

- [ ] **Step 2: Run it and check that it fails:** `.venv/bin/python -m pytest tests/test_merge_repeats.py -q`.
  Expected: ImportError, because `merge_repeats` doesn't exist yet.
- [ ] **Step 3: Implement** in `lfun.py`:

```python
def merge_repeats(gammas, idx):
    """Synthetic double zeros: gamma[k+1] := gamma[k] for k in idx (0-based, non-adjacent)."""
    g = np.array(gammas, float, copy=True)
    idx = np.sort(np.asarray(idx, int))
    if idx.size and (np.any(np.diff(idx) < 2) or idx[-1] + 1 >= g.size):
        raise ValueError("idx must be non-adjacent and < len(gammas) - 1")
    g[idx + 1] = g[idx]
    return g
```

  Then check how `DiscreteMeasure.from_atoms` treats duplicate atoms, by reading `measures/base.py`. If it doesn't
  merge them, aggregate in the check script with `np.unique(x, return_inverse=True)` and `np.bincount` on the weights,
  and record a Ruling.
- [ ] **Step 4: Run it and check that it passes**, then run the full suite: `.venv/bin/python -m pytest -q`.
  Expected: everything passes.
- [ ] **Step 5: Sensitivity probe** `checks/check_merge.py`, written to `.out` with `tee`:
  - [1] Smooth model, J = 2·10⁵ atoms plus tail. For φ ∈ {0, 0.1, 0.25, 0.5}, merge a fraction φ of indices spread
    evenly over all scales (every ⌈1/φ⌉-th index, with non-adjacent pairs). Compute b_j with rkpw, n ≤ 4000. Report
    two quantities at n ∈ {250, 500, 1000, 2000, 4000}:
    - **S_n^true**, i.e. `averaged_law` with the merged x_j, minus S_n of the φ = 0 run at the same n;
    - the prediction 2 log(1−φ).
  - [2] The same, but merging only in index windows [εn₀, n₀] for one fixed n₀ = 2000 (a localized defect). Report
    S_n for n around n₀, to see at which scale the shift appears.
  - [3] True zeros: Odlyzko M = 2·10⁶ plus tail, n ≤ 2·10⁴. Report S_n under both normalizations (true x_j and smooth
    x̃_j) against the smooth model. This reproduces item 11's 6e−6 agreement at n = 2·10⁴. Also report the minimum
    of (γ_{k+1} − γ_k)·log(γ_k/2π)/2π over the data, and the empirical fraction below δ for δ ∈ {0.01, 0.05, 0.1}.
    These are inputs for (SG) and are NUMERICAL only.

  Expected:
  - [1]: the shift is roughly 2 log(1−φ) (−0.21, −0.58, −1.39), with the O(1/log n) drift of S_n.
  - [3]: the two normalizations agree to below 1e−4 by n = 2·10⁴.

  If [1] shows no shift, the heuristic behind (N) is wrong. Record that in LOG.md and drop Task 5's necessity claim
  (Ruling).
- [ ] **Step 6: Commit** `G3p: workspace, merge_repeats helper, sensitivity probe (NUMERICAL)`. Include
  `toolkit:`-scoped files in the same commit; the message prefix is `G3p:`.

---

### Task 2: Citations (CITATIONS.md)

**Files:** Modify `research/G3prime/CITATIONS.md`, `research/G3prime/LOG.md`.

- [ ] **Step 1:** Fetch and read the sources, with WebFetch on arXiv abstracts and PDFs. Quote verbatim, with the
  hypotheses, the theorem number and the URL:
  - **(C1) Riemann–von Mangoldt with remainder:** N(T) = (T/2π) log(T/2πe) + 7/8 + S(T) + O(1/T), with an explicit
    bound |S(T)| ≤ a log T + b log log T + c for T ≥ T₀. Candidate: T. Trudgian, "An improved upper bound for the
    argument of the Riemann zeta-function on the critical line II", arXiv:1208.5846. It states both the formula and the
    explicit S(T) bound. Fallback: any arXiv paper quoting Backlund/Trudgian with hypotheses.
  - **(C2) Multiplicity:** m(γ) ≤ N(γ + 1) − N(γ − 1) ≪ log γ. This follows from (C1); derive it in PROOF.md rather
    than cite it.
  - **(C3) Status of simple zeros:** the best unconditional proportion of simple zeros, and a statement that
    "almost all zeros are simple" is open. Candidate: Bui–Conrey–Young, arXiv:1002.4127, intro (≥ 40.58% simple and
    on the line). Look for an explicit "it is conjectured that all zeros are simple" sentence.
  - **(C4) Small gaps, density statements:** what is known unconditionally about #{γ_{k+1} − γ_k < δ·mean gap}. It is
    likely that no unconditional density bound tending to 0 is known. Find a source that states the known
    results, for example a survey or a paper on small gaps, such as Conrey–Turnage-Butterbaugh arXiv:1708.xxxx or a
    Montgomery pair-correlation exposition. Record exactly what it claims. If nothing readable states the status,
    write "status not verified from a source" (GAP) and do not assert "open".
- [ ] **Step 2:** For each item, record READ (with the quote) or GAP in CITATIONS.md, and add a LOG.md entry.
- [ ] **Step 3: Commit** `G3p: citations for S(T), simple zeros, small gaps`.

---

### Task 3: Theorem G3′-U (unconditional upper bound)

**Files:** `research/G3prime/PROOF.md` §1–§3, `checks/check_ratio.py` + `.out`.

- [ ] **Step 1: Lemma Z1 (ordinate comparison).** For all k ≥ 1, |γ_k − γ̃_k| ≤ C₀, with C₀ explicit from (C1).
  - Proof outline. Let k be given and T := γ_k. Then N(T − 0) ≤ k − 1 < k ≤ N(T), which handles multiplicity.
    - N₀(T) = N(T) − S(T) − 7/8 + O(1/T) puts N₀(T) within E(T) := |S| + O(1) of [k − 1, k].
    - N₀(γ̃_k) = k − ½, and N₀′ ≥ (1/2π) log(T/2π) on the relevant range.
    - So |γ_k − γ̃_k| ≤ (E(T) + 1)/min N₀′ = O(log T / log T) = O(1).
  - Handle small T, e.g. γ_1 ≈ 14.13 against γ̃_1 ≈ 14.52, either by a direct finite check against the Odlyzko data
    for k ≤ k₀ or by using the explicit (C1) constants. Label the result PROVED-mod-cite (C1).
- [ ] **Step 2: Lemma Z2 (pair ratios, upper).** For 1 ≤ a < b:

      x_a − x_b ≤ (1 + C₁ log(γ̃_b)/(b − a)) · (1 + C₂/γ̃_a) · (x̃_a − x̃_b),

  with C₁ and C₂ explicit. Use x_a − x_b = (γ_b² − γ_a²)/((γ_a² + ¼)(γ_b² + ¼)), Z1, and
  γ̃_b − γ̃_a ≥ 2π(b − a)/log(γ̃_b/2π), which follows from (N₀⁻¹)′ = 2π/log(T/2π) decreasing. When γ_b = γ_a the left
  side is 0, which is fine.
  - Rule A: `checks/check_ratio.py` computes, over all pairs a < b ≤ 2·10⁵ with b − a ≤ 200 (plus a sample of far
    pairs), the observed ratio (x_a − x_b)/(x̃_a − x̃_b) against the Z2 bound. Expected: no violations, with the worst
    slack reported.
- [ ] **Step 3: Theorem G3′-U.** Write out the upper bound following the H_L upper-bound proof, with Lemma H7 used
  unchanged. Steps:
  - (i) Choose M. Let λ := (Mn)² x_{Mn}, the true atom. Define G(k) := k⁻² for k ≤ Mn and G(k) := x_k/λ for k > Mn.
    On the tail, 0 < G ≤ (Mn)⁻² because x is nonincreasing. Ties are allowed, since H7 only needs 0 < G ≤ (Mn)⁻².
  - (ii) Head pairs, both indices ≤ Mn: the true difference is at most Z2 times the smooth difference, and the smooth
    difference is at most r̃·(G(a) − G(b)) with r̃ ≤ L(a) ≤ L(Mn), by H5 and the (L3) check of Corollary H_L-ζ.
  - (iii) Cross pairs: split at Mn, as in H_L. The factor Z2(a, Mn) appears only once per pair.
  - (iv) Tail pairs: exact.
  - (v) Total: Σ over head and cross pairs of 2 log Z2 ≤ 2n · Σ_{d ≤ Mn} C₁ log(γ̃_{Mn})/d + O(n Σ_i 1/γ̃_i)
    = O(n log² n) = o(n²).
  - (vi) λ/L(Mn) → 1, by Z1, so n(n−1) log λ = n² log L(Mn) + o(n²).
  - (vii) Weights: 2x_k ≤ c·2x̃_k uniformly (Z1), and (Hw) holds with s₀ = 2. Then apply H6(c, d) and let M → ∞.

  Label: PROVED-mod-cite (C1) on top of Theorem H, p = 2 (which is PROVED in item 11).
- [ ] **Step 4: Rule A.** Look for counterexamples: does any step use a lower bound on γ_b − γ_a? It must not. Is
  Σ over k of 1/γ̃_k summed over head indices only? Record the pass in LOG.md.
- [ ] **Step 5: Commit** `G3p: Theorem G3′-U (unconditional upper bound) + ratio check`.

---

### Task 4: Theorem G3′-L (lower bound under (SG))

**Files:** `research/G3prime/PROOF.md` §4.

- [ ] **Step 1: State (SG) precisely, with no RH framing.** For every η > 0 there are δ > 0 and K₀ such that for all
  K ≥ K₀,

      #{k ≤ K : γ_{k+1} − γ_k < 2πδ / log(γ_k/2π)} ≤ ηK.

  Note that (SG) implies the repeated indices have density 0.
- [ ] **Step 2: Lemma S (index shift, elementary).** If π: ℕ → ℕ is strictly increasing with π(a) ≤ (1+η)a, then for
  a < b:

      π(a)⁻² − π(b)⁻² ≥ (1+η)⁻³ (a⁻² − b⁻²).

  Proof: π(b) − π(a) ≥ b − a and π(a) + s ≤ (1+η)(a + s), then substitute in ∫ 2t⁻³ dt. Rule A: check it numerically
  on random π, in a short `checks/check_shift.py`.
- [ ] **Step 3: Theorem G3′-L.** Assume (SG). Fix η, take the good set E (indices whose forward gap is
  ≥ 2πδ/log) and let π enumerate E. Restrict the Heine sum to subsets of E; all terms are ≥ 0. For pairs of good
  indices:
  - **Far pairs,** π(b) − π(a) ≥ R := ⌈C log γ̃⌉/δ: true/smooth ratio ≥ 1 − C₁ log/(π(b) − π(a)) ≥ ½. The total
    contribution is O(n log² n).
  - **Near pairs:** true difference ≥ the forward gap at π(a), which is ≥ 2πδ/log. The smooth difference is at most
    (π(b) − π(a))·2π/log(·)·(1 + o(1)), so the ratio is ≥ δ/(C R). Taking logs gives O(n·R·log(R/δ)) =
    O(n log n log log n) = o(n²).
  - **Then:** smooth (x̃∘π) against pure power by H5 composed with Lemma S, then Theorem H (lower half) with weights
    ≥ c j⁻² (since π(j) ≤ (1+η)j), then L(π(j)) ≥ L(j) by (L3).

  The result is liminf ≥ −3 log(1+η) − (weight-constant terms of O(1)·n). Let η → 0.

  Label: PROVED-mod-cite + mod-hypothesis (SG). Write this as "PROVED-mod-input (SG)".
- [ ] **Step 4: Rule A**, recorded in LOG.md. Is the (SG) threshold at the correct scale? Does π(j) ≤ (1+η)j follow
  from (SG) for all large j (yes, since the count of bad indices up to K is ≤ ηK)? Are weights at merged indices
  handled?
- [ ] **Step 5: Commit** `G3p: Theorem G3′-L (lower bound mod small-gaps hypothesis)`.

---

### Task 5: Proposition N (necessity / obstruction) — attempt

**Files:** `research/G3prime/PROOF.md` §5, `LOG.md`.

- [ ] **Step 1: Reduce the problem.** Show that if the repeated indices R have lower density ≥ φ > 0, then
  log D_n(σ) ≤ log D_n(σ̃|_E) + o(n²), where E = ℕ ∖ (R + 1) is the set of first indices of distinct zeros. This
  uses Z2 and the tail cut from Task 3. The reduction uses only upper bounds, so it should go through.
- [ ] **Step 2: Deletion Lemma (target).** If the set ℕ ∖ E has lower density ≥ φ, then
  limsup (1/n²)[log D_n(σ̃|_E) − log D_n(σ̃)] ≤ −c(φ) < 0. Attempt it, then try the following in order:
  - (a) If E is the explicit set {⌊j/(1−φ)⌋}: atoms x̃∘π with π(j) ≈ j/(1−φ) satisfy H_L's hypotheses up to the
    floor function. Get the constant shift 2 log(1−φ) from Theorem H_L applied to a smoothed π, and justify replacing
    π by its floor through a ratio comparison.
  - (b) For general E with lower density φ: try a monotonicity or rearrangement argument showing that, among index
    sets with given counting function, D_n is maximized by evenly spread sets. If no argument is found within the time
    box (one session of focused attempts), record it as a GAP with the exact missing statement.
- [ ] **Step 3: Write the obstruction in LOG.md.** "Proving the lower bound of G3′ unconditionally implies that the
  repeated indices of the ordinates have lower density 0 [needs the Deletion Lemma for general E; proven for
  evenly spread E if (a) succeeds]. By (C3)/(C4), density-one simplicity is not known unconditionally. Stop
  condition: as hard as an open problem."
  - If (C3)/(C4) are GAP, write instead: "status of density-one simplicity not verified from a source".
  - Cross-check with Task 1 probes [1] and [2].
- [ ] **Step 4: Commit** `G3p: Proposition N (necessity) and stop-condition write-up`.

---

### Task 6: Status table and docs

**Files:** `research/G3prime/PROOF.md` §0 (status table), `README.md` (research status line), spec §7 note.

- [ ] **Step 1:** Add a status table at the top of PROOF.md: Z1, Z2, S, G3′-U, G3′-L, Prop N, and the Deletion
  Lemma, each with its label and dependencies.
- [ ] **Step 2:** Update README.md with one line on the G3′ status, and the spec §7 note: "Plan 7: G3′ outcome …".
  Make no overclaims: "REVIEWED" is added only after Task 7.
- [ ] **Step 3: Commit** `docs: G3′ status`.

---

### Task 7: Rule R (independent second reader)

**Files:** `research/G3prime/review/REVIEW_G3prime.md`.

- [ ] **Step 1:** Dispatch an independent reviewer agent on the most capable model, with PROOF.md, CITATIONS.md,
  checks/*.out, item 11 §7b, and this plan's Review Focus. Ask it to verify each proof line by line, to try to break
  Z1, Z2 and Lemma S numerically, and to rule ACCEPT, ACCEPT WITH FIXES or REJECT per result.
- [ ] **Step 2:** Apply the fixes, mark the results REVIEWED where accepted, and update the status table.
- [ ] **Step 3: Commit** `G3p: Rule R review + fixes`.
- [ ] **Step 4:** If G3′-U and G3′-L are accepted, note in the spec §7 a follow-up plan, "Plan 8: Lean for G3′
  combinatorial core (Lemma S, the Z2 → Heine upper-bound assembly, mod named inputs Z1 and Theorem H)". That plan is
  not part of this one.
