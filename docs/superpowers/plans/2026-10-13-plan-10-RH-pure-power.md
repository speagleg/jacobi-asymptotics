# Plan 10: Riemann–Hilbert analysis for pure powers (the pointwise Law P), staged research project

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native). Steps use checkbox (`- [ ]`)
> syntax. This is a multi-session research plan. Each phase ends at a **gate**: continue, or stop and write up.

**Goal.** Prove the pointwise Law P, with an error term, for the model family

  σ_{p,s} := Σ_{k≥1} k^{−s} δ_{k^{−p}},  p > 0, s > 1,

i.e. n^p b_n → c(p) and a_n/(2b_n) → 1, ideally with b_n n^p = c(p)(1 + d₁(p,s)/n + O(n^{−2})). The method is the
Deift–Zhou steepest descent for discrete orthogonal polynomials on infinitely many nodes with an accumulation point.

This closes G1 for the cases that matter most: pure powers with power weights, which include the Haynes–Zudilin
measures (s = 2a + b) and item 11's references. Combined with G1-T and A4 (Plan 9), it also discharges (T3) and (CL)
for this family.
*(Corrected — Plan 37 note, 2026-10-14: (CL) and A4 apply only for p > 1 (G1 PROOF.md §3.1, CL4). For p = 1 the RH
results give the pointwise law directly and nothing is claimed about (CL); for p > 1 (CL) is Theorem CL.)*

**Template and inputs.**
- WLXZ (arXiv:1410.3948, read in Plan 9). Interpolation problem → RHP via Π(z) = sin θ(z)/γ(z), with nodes = zeros
  of sin θ. Then the transformations R → T → Q (g-function), lenses, the global parametrix, local parametrices
  (including at the accumulation point z = 0, §6.2), and small norm. Their case is Tricomi–Carlitz (p = 1, symmetric).
- BKMM (math/0212149) and Bleher–Liechty, for band–saturated endpoints.
- **G2.** The equilibrium μ* is explicit (band (0, 4c(p)), saturated [4c, ∞) in x = n^p·atom). Its potential is known
  (B*(ii)), and the variational inequalities are proved (B*). This replaces WLXZ's equilibrium computation.

**The key new difficulty.** In the x-variable, the accumulation point z = 0 is the *left band edge*, with infinitely
many nodes accumulating there. In WLXZ's symmetric variable it is the band centre. Two options:
- (i) Symmetrize: s = ±x^{1/2}, atoms ±k^{−p/2}, with even OPs P_{2m}(s) = Q_m(s²). Then 0 is interior, as in WLXZ,
  with θ(z) = πn(z²)^{−1/p} piecewise analytic.
- (ii) Build a new edge parametrix at z = 0.

Phase 1 decides between them.

**Spec.** §7 G1 (route: discrete RH, Wu–Lin–Xu–Zhao type), §8 stop conditions. Inputs: research/G1/PROOF.md §4,
research/G2/PROOF.md.

## Global Constraints

- AGENTS.md rules 1–7. Commit prefix `G1:`. Work in `research/G1/RH/{RH.md, LOG.md, checks/}` on branch
  `plan-10-RH`.
- Every analytic object (θ, Π, g, φ, parametrix matching) gets a numerical check script (Rule N): residues and
  jumps verified at sample points, and matching errors measured as n grows.
- **Gates.** At the end of each phase, write a gate entry in LOG.md: GO, or STOP with the precise obstruction. On
  STOP, write up and finish; do not push past a failed construction.

## Review Focus

1. **The pole/IP → RHP step.** Π and w must be analytic in the needed regions and nonvanishing off the nodes. The
   branch cut of z^{−1/p} must not meet the nodes.
2. **g-function.** Its boundary values must reproduce G2's variational equalities and inequalities exactly, with the
   right signs in the saturated region (the △-factorization regions of WLXZ).
3. **The accumulation point.** Infinitely many poles accumulate. The local problem must be solvable, and the
   matching must be O(1/n) (or quantified).
4. **The top of the node set.** The largest nodes, z ≈ n^p, are in the saturated region. The contour must end
   correctly there (WLXZ use k_n = √(n/α) + δ).
5. **Extracting a_n, b_n.** b_n comes from the (1,2)·(2,1) entries at infinity. Track the normalization (monic P_n,
   item 11 indexing b_j). Check against exact cases: Lommel (p = 2), where a_n/(2b_n) = 1 + 1/n + O(n^{−2}) is known
   (item 11 Theorem A), and Tricomi–Carlitz (p = 1).

---

### Phase 0 (Task 1): Fine numerics (cheap; informs everything)

- [ ] `checks/check_fine.py`: for p ∈ {1, 2, 3} and s ∈ {p, p+1, 2p}, compute n^p b_n/c(p) − 1 and a_n/(2b_n) − 1 to
  n ≈ 3000 (q precision near the top; K-doubling). Fit d₁(p,s) in 1 + d₁/n + d₂/n². Check the exact Lommel and
  Tricomi–Carlitz references. Record whether d₁ depends on s, and any visible formula.
- [ ] **Gate 0.** If the corrections are not of the form 1 + O(1/n), for example log terms or oscillations, record it
  and adjust the target.

### Phase 1 (Task 2): Interpolation problem and RHP

- [ ] Write the Borodin–Boyarchenko interpolation problem for σ_{p,s}, rescaled by z = n^p x (or symmetrized, option
  (i)).
- [ ] Define θ(z) := πn z^{−1/p} (so that θ(z_k) = πk at the nodes z_k = (k/n)^{−p}), γ := θ′ and Π := sin θ/γ, and
  w(z) := (n z^{−1/p})^{−s} rescaled.
- [ ] Choose option (i) or (ii) by checking analyticity regions and the WLXZ contour geometry (Figure 3 analogue).
  Write the transformation Y → U → R (WLXZ (3.1)–(3.12) analogue) and the RHP for R.
- [ ] Numerical checks: Π(z_k) = 0, Π′(z_k)/… = (−1)^k as in WLXZ (3.8), the residue conditions, and the jump
  matrices at sample points.
- [ ] **Gate 1.** GO if the RHP for R is well posed, with jumps analytic off the contour and the correct behaviour at
  0 and ∞.

### Phase 2 (Task 3): g-function and φ-functions

- [ ] g(z) := ∫ log(z − y) dμ*(y), using G2's superposition μ* = ∫ω_{β_t} dt. Compute g′ in closed form, or as an
  explicit t-integral of arcsine resolvents (√(z(z−β_t))).
- [ ] Prove the WLXZ (4.3)–(4.5) analogues from G2 B*: g₊ + g₋ = l on the band, and the correct inequality on the
  saturated part, after the △-transformation. Define φ and φ̃ and their sign charts.
- [ ] Numerical check of the boundary values, l, and the sign charts.
- [ ] **Gate 2.** GO if the sign structure needed for lens opening holds on all regions.

### Phase 3 (Task 4): Lenses and global parametrix

- [ ] Open lenses on the band. Write the global parametrix N (a band (0, 4c), or (−2√c, 2√c) after symmetrization)
  with the Szegő-type function D for the weight k^{−s}.
- [ ] **Gate 3.** GO if the jumps outside small discs at the special points are I + O(e^{−cn}) or I + O(1/n).

### Phase 4 (Task 5): Local parametrices

- [ ] Band–saturated edge z = 4c: an Airy-type parametrix (BKMM / Bleher–Liechty). Write it and check the matching.
- [ ] The accumulation point z = 0: generalize WLXZ §6.2 (option (i)), or build a new edge parametrix (option (ii)).
  This is the main research risk.
- [ ] Top of the node set (z ≈ n^p): verify that no parametrix is needed (saturated, exponentially small jumps), or
  build one.
- [ ] **Gate 4.** GO if all matchings are I + O(n^{−1}) (or a quantified rate).

### Phase 5 (Task 6): Small norm and coefficient asymptotics

- [ ] Small-norm argument for the final RHP. Extract a_n and b_n.
- [ ] **Target theorem:** n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n) for σ_{p,s}. Optionally compute d₁ and
  compare with Phase 0.
- [ ] Corollaries: (T3) and (CL) hold for σ_{p,s}, so G1-T and A4 apply. The pointwise Law P for the Haynes–Zudilin
  measures.

### Phase 6 (Task 7): Rule R

- [ ] An independent reviewer (opus) on RH.md with all checks. Apply fixes, mark REVIEWED, update the G1 status, the
  README and the spec.

**Expected effort.** Several sessions. Phases 0–2 are likely within one session; Phase 4's accumulation-point
parametrix is the step most likely to need extended work. If any gate fails, the project stops with a precise
obstruction recorded. That is still a useful outcome.
