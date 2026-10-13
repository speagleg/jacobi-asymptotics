# G3′ log

## 2026-10-13: Plan 7 execution

- **Setup.** Workspace created. Added the toolkit helper `merge_repeats`, with tests. `DiscreteMeasure.from_atoms`
  rejects duplicate atoms, so the checks merge equal atoms and add their weights first (Ruling, Plan 7 Task 1).
- **Sensitivity probe** (`checks/check_merge.out`, NUMERICAL).
  - [1] Making a fraction φ of the indices into double values shifts S_n by −0.17, −0.47 and −1.13
    (φ = 0.1, 0.25, 0.5; n = 4000). The predicted values are 2 log(1−φ) = −0.21, −0.58 and −1.39. The shifts still
    drift toward these slowly, like the O(1/log n) drift of S_n itself. The heuristic is not refuted, so Task 5 goes
    ahead.
  - [2] A defect confined to the index window [1000, 2000) is invisible for n ≤ 1500 and appears for n ≥ 2000. Only
    indices up to about n affect D_n at the n² scale.
  - [3] True zeros: see `.out`.
- **Citations.** (C1) Trudgian's Corollary 1 was read from the arXiv PDF and quoted. (C3) was read from
  arXiv:2501.14545 §1, which surveys simple-zero proportions; the best unconditional result quoted is > 40.75%.
  (C4) was ruled unnecessary (CITATIONS.md).
- **Z1, Z2, G3′-U** written. Rule A pass:
  - No step uses a lower bound on any γ_b − γ_a, checked line by line in §3.
  - The log γ̃_b factor of Z2 appears only for b ≤ Mn. Tail pairs are rescaled exactly.
  - H7 tolerates ties in G on the tail: its proof uses only 0 < G ≤ (Mn)⁻² there (item 11 §7b steps 2–3).
  - A potential issue checked: Z1 is proved only for γ_k ≥ 10⁶ (k ≥ k₁). The finitely many smaller indices are
    handled by the constant B (Z2, "small indices") and by c in Z1′. Both are positive and finite, so they cost O(n).
  - Numerical ratio check: `checks/check_ratio.out`.
- **G3′-L** written under (SG). Rule A pass:
  - *Danger: tail subsets.* The far-pair losses carry a log γ̃_a factor, so they are unbounded for deep indices. A
    pairwise uniform comparison (as in the H_L lower bound) therefore fails. This was resolved by turning the losses
    into weights a^{−C log n} and proving Lemma W: item 11's log-convexity weight step loses only (s−3)·K n log n,
    uniformly in s. With s_n ≍ log n the loss is O(n log² n).
  - Lemma S checked numerically: `checks/check_shift.out` (min ratio 1.0005 ≥ 1).
  - (SG) gives π(j) ≤ (1+2η)j eventually: yes, since #bad ≤ ηK.
- **Proposition N.** A rigorous obstruction (mod Theorem H): smooth ordinates with every m-th value doubled have the
  same counting information, yet the law fails by 2 log(1 − 1/m). The general converse (GAP N′) needs a deletion lemma
  for clustered index sets; it is not proved.

## Stop: the unconditional lower bound needs inputs beyond (C1) (Prop N); hardness not established (GAP N′)

The unconditional lower bound of G3′ needs information that the counting function does not give (Prop N), for example
about multiplicities or small gaps. The sufficient input (SG) implies that almost all ordinates are simple values
(horizontal multiplicity 1, (C3) §1.3). In the
literature read (CITATIONS.md (C3)), the best unconditional simple-zero proportion is > 40.75%, and no surveyed
result, conditional or not, reaches proportion one. G3′ is therefore closed in the following form:

- **G3′-U:** unconditional (PROVED-mod-cite (C1) on top of item 11).
- **G3′-L:** PROVED-mod-input (SG).
- **Prop N:** counting information is insufficient (PROVED-mod-input Theorem H).
- **GAP N′:** general deletion. It would make density-zero repeated ordinates necessary. Together with (SG) being
  sufficient, this sandwiches G3′; it is not an equivalence.

- **Rule R (2026-10-13):** ACCEPT WITH FIXES (`review/REVIEW_G3prime.md`). Fixes applied the same day: Z1 (2E bound,
  analytic C₀, all-k form); Z2 (small indices for all b > a); G3′-L (ℓ_n bound with the (1+log n)² term and the
  min(n−1, ·) near count, e^{−C(1+log n)²} weights, π(j) ≤ C_η j, lower sum/denominator factors, far-partner case
  split); N ((log h)′ proof, sup domain, |π − ψ| ≤ 1); N′ and stop-condition framing corrected.
