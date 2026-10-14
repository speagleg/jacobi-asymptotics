# G2 log

## 2026-10-13: Plan 8

- **Averaged law** (`checks/check_averaged.out`, NUMERICAL). S_n → 0 for p = 1.5, 3, 4 and 6.
  - Rule N: K-doubling changes S_n by ≤ 5.4e−4, 2.8e−5, 1.4e−6 and 7e−8 respectively. ld and q agree.
  - p = 0.5 is truncation-limited: K-doubling changes S_n by 1.1e−2 and S_n is not monotone. The atoms k^{−1/2} decay
    too slowly for K = 2·10⁵ at n ≥ 400. The theory (Part A) covers p = 0.5; the numerics do not.
- **Explicit optimizer** (`checks/check_energy.out`, NUMERICAL). μ* := ∫_0^1 ω_{[0, 4c(p)t^{−p}]} dt, in x = u^{−p}.
  - Its density equals the constraint for x ≥ 4c and is strictly below it for x < 4c. The one exception, 0.9862 at
    p = 0.5, x = 1000·4c, is quadrature error; the closed form I_{min(1,x/4c)}(1/p+½, ½) gives exactly 1.
  - Its potential is constant, log c + p, on (0, 4c) (to 1e−15) and larger beyond. These are the KKT conditions. The
    1e−15 is circular (Rule X): it plugs B0's value into the t-quadrature. B0 was checked independently by the
    reviewer's direct quadrature.
  - Monte Carlo I(μ*) = κ_p within error for p ∈ {0.5, 1, 1.5, 2, 3, 4, 6}.
  - So Route B1 is realized by superposing Weyl-law arcsine measures (in the Buyarov–Rakhmanov spirit), not by a
    Mellin transform. (Ruling, Plan 8 Task 4.)
- **Frank–Wolfe solver** (scratch, pre-plan). E_p − κ_p is +3e−4 to +6e−4 for p ∈ {1, 1.5, 2, 3, 4}. That this gap
  is discretization error was asserted without N-doubling or Richardson extrapolation. Plan Task 1 Step 2 (precision
  1e−4) was **superseded** by the exact Theorem B* and not done (Ruling). The geometric-grid saturation points underestimate u_s = (4c)^{−1/p}, because Frank–Wolfe
  does not fully converge at the saturation edge; the uniform grid came closer (0.641 vs 0.637 for p = 2).

## Rule A (adversarial pass), per lemma

- **B0.** Checked by direct quadrature, independent of the Fourier proof (reviewer `r1.py`). Edge cases: x = 0 and
  x = β (continuity by domination), and x ≫ β (monotone).
- **B\*.**
  - Degenerate p: small p (0.3, 0.5) and large p (6, 7). J(p) − (2/p)I(p) ≈ 1e−17 (reviewer).
  - Sign conventions checked against (P).
  - μ ∈ 𝒜 with I(μ) = −∞ is trivially allowed.
  - E_p < ∞ is shown in the proof.
- **A1.**
  - Excess divided by n log n stays in [−4, 1.8] (reviewer `a1.py`; explicit bound ≈ 5.4) for p ∈ {0.5, 1, 3},
    n ≤ 80, M = 4, on degenerate S: consecutive block, evens, random, geometric.
  - The cell A_1 = [0, 1/n], where g blows up, is fine because only a lower bound on the cell average is needed.
  - Isolated far points are excluded by the k ≤ Mn cap. This is why the H7 split is needed.
- **A-U.**
  - The N = 0 edge case (t = 1) is checked.
  - Only Σw < ∞ is used.
  - Uniform in m.
- **A-L.**
  - The i = 1 block (B_1 starts at 0) is handled in steps 3(a) and 3(d).
  - Near pairs (j ≤ i + 2) are handled separately (3c), because h(b) = −∞ at j = i + 2.
  - The quantile configuration of the untruncated μ* tracks κ_p within O(log n/n) (reviewer `al.py`).
- **H_all.**
  - H4's hypotheses for general p: f′ < 0 is derived.
  - The error is o(n²), not O(n log n).
- **HZ.**
  - Indexing exact to 12 digits (`check_hz.out`).
  - Prior art: Monien (p = 1, heuristic) recorded in CITATIONS (M).

## Rule R

`review/REVIEW_G2.md`: ACCEPT WITH FIXES, all fixes applied 2026-10-13. The main fixes:
- A-L step 3 written out in full (the reviewer's scheme);
- the A-L step 1 scaling formula corrected;
- A-L restated as ≥ κ_p, citation-free;
- the mutual-energy finiteness citation added;
- Monien prior art recorded, with the novelty wording narrowed.

## 2026-10-14: Plan 47 — removing the citation (P)

**What changed.** PROOF.md §1 gained **Lemma EP** (energy positivity): for a finite signed Borel measure ν on ℝ with
ν(ℝ) = 0 and ∬|log|x − y|| d|ν|d|ν| < ∞, −∬ log|x − y| dν dν = ∫_0^∞ |ν̂(ξ)|²/ξ dξ ≥ 0, with equality iff ν = 0. It is
papers/paper1/main.tex Lemma 3.3 with its proof (refereed: papers/paper1/REVIEW_Paper1.md, "Lemma 3.3: CORRECT"; fixes
F2/F3 already in the Paper 1 text that was ported). B*(iii)'s optimality step was rewritten to use it:
- (EP-int) for ν = μ^x − μ* is checked through |ν| ≤ μ^x + μ*, with the three energies made absolutely convergent
  directly: μ^x by the log moment and I(μ) > −∞; μ* by the existing Fubini bound in **Value**; the mutual energy by
  |t| = 2t⁺ − t and U* ≥ log c + p (B*(ii)). This also replaces the mutual-energy finiteness previously quoted from
  (P) §1 (Rule R fix of 2026-10-13).
- The 2026-10-13 (P)-based text is kept verbatim as a remark after the proof (alternative route). CITATIONS.md (P)
  has a dated "no longer used" note.

**Rule A (Lemma EP).** Hypotheses tested: mass zero is needed (ν = ω_8 gives −∬log = −log 2 < 0); (EP-int) is needed
for the left side to be defined (δ_0 − δ_1). `checks/check_positivity.py` (NUMERICAL, output in `.out`): the Fourier
identity for ω_1 − ω_4 (log 4; gap 1.2e−4 = uncomputed tail beyond ξ = 4000) and U[0,1] − U[0,2] (log 2; gap 5e−8).
Paper 1's referee also tested an unbounded-support case (Exp(1) − Exp(2), REVIEW_Paper1.md).

**Dependency check for each relabel.** (P) entered only through B*(iii) (G2 §0 and CITATIONS.md "Used in"). For each
result the chain was read back to its inputs; a result is relabelled PROVED only if (P) was its sole external citation.
Item 11 inputs (H1–H4, H7 algebra; math-pursuits f5f6aef, PROVED there, citation-free) are internal program inputs, as
in the pre-Plan-47 labels, which listed (P) alone. CITATIONS.md (M) Monien and (HZ) Haynes–Zudilin are prior-art /
context entries, not proof inputs.

| Result | File | Old label | New label | Inputs checked |
|---|---|---|---|---|
| Lemma EP (new) | G2 PROOF.md §1 | — | PROVED; Rule R pending (Plan 47) | Fubini, dominated/monotone convergence, Gaussian Fourier transform |
| B* | G2 PROOF.md §0, §1 | PROVED-mod-cite (P) | PROVED; Rule R pending (Plan 47) | B0, EP; (i), (ii) and the value were already citation-free |
| H_all | G2 §0, §3 | PROVED-mod-cite (P) | PROVED; Rule R pending (Plan 47) | A-U (PROVED), A-L (PROVED), B* (now PROVED), item 11 H2–H4 |
| HZ | G2 §0, §3 | PROVED-mod-cite (P) | PROVED; Rule R pending (Plan 47) | H_all only |
| Cor. H-input | G2 §3 | PROVED-mod-cite (P), as H_all | PROVED, as H_all; Rule R pending (Plan 47) | H_all; Lean `heineD_eq_det`, `heineK_bdd_of_summable` (sorry-free) |
| G1-T | G1 PROOF.md §0 | PROVED-mod-cite (G2 (P)) | PROVED; Rule R pending (Plan 47) | H_all (via G2 §3 b_j form), Lemma K; (T3) is the stated hypothesis |
| G1-L | G1 §0 | PROVED-mod-cite (G2 (P)) | PROVED; Rule R pending (Plan 47) | H_all, Lemma K; one-sided bound is the stated hypothesis |
| WC | G1 §0, §3.1 | PROVED-mod-cite (P) (through G2 B*(iii)); REVIEWED | PROVED; REVIEWED (proof unchanged); relabel Rule R pending (Plan 47) | G2 A1, A-U, A-L, B*(iii), scaling; Portmanteau (textbook) |
| CL | G1 §0, §3.1 | PROVED-mod-cite (P) (through G2 B*(iii); internal …); REVIEWED | PROVED; REVIEWED (proof unchanged); relabel Rule R pending (Plan 47) | WC, Sat_p (from G3′ Lemma Sat: Christoffel + Lagrange, elementary), A3, G2 B*(i) |
| A4′ | G1 §0, §3.1 | PROVED-mod-cite (P) (through G2 B*(iii)); REVIEWED | PROVED; REVIEWED (proof unchanged); relabel Rule R pending (Plan 47) | A2, A3, CL |
| TC | G1 §0, §3.7 | PROVED-mod-cite (P) (through G2 B*(iii); internal …) + REVIEWED | PROVED; REVIEWED (proof unchanged); relabel Rule R pending (Plan 47) | G2 A-U, A-L, B*(iii) |
| T3-avg | G1 §0, §3.7 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; (P) via TC) + REVIEWED | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) + REVIEWED; relabel Rule R pending (Plan 47) | (P) entered only via TC; the RH citations remain |
| 19 G3′ §0 rows (all but G3′-L) | G3prime PROOF.md §0 | note "… and also by G2 Cor. H-input (mod-cite (P))" | note "… (PROVED since Plan 47; was mod-cite (P))"; labels unchanged (still mod-input Theorem H) | annotation only; no G3′ result depended on (P) (THEOREMS §3.3) |
| Lean `theoremHL` | lean/README.md, THEOREMS H6, §2.1 | PROVED-mod-input (… G2 Cor. H-input, mod-cite (P) …) | PROVED-mod-input (… G2 Cor. H-input, citation-free since Plan 47 …) | Lean label unchanged: H_all is not formalized |

**Left unchanged (dependence not verified, or history).**
- RH_ζ (G1 §0, RH_zeta.md E1(iv), RH_zeta_close.md header): E1(iv) applies G2's optimality argument "verbatim" to a
  different measure μ (constraint ρ, not σ). Lemma EP would replace (P) there only if (EP-int) holds for that μ, which
  was not re-checked. E1(iv) is not needed for RH_ζ, so its label (which also cites WLXZ, KMVV, C–D, DLMF) is unchanged.
- Lean docstrings in lean/JacobiAsym/Inputs.lean (l. 23) and TheoremHL.lean (l. 13) still say "mod-cite (P)". Not
  edited: .lean files, no rebuild in this plan.
- Review files (G1/review/*, G2/review/*, RH_zeta review), G1 LOG.md, THEOREMS §5 Plan 37 items: history.
- research/program/novelty_G2.md l. 300 ("Saff–Totik (already in G2 via (P))"): novelty notes, history.
- research/program/outline_A_nodes.md T0 (a proposed label, not a result) and RESEARCH_PROGRAM.md §4: dated notes only.
- G1 A4 (CONDITIONAL on (CL)): its label never cited (P).

**Status.** Rule R pending (Plan 47): a second reader should check Lemma EP's hypotheses against the measures in B*(iii)
and the completeness and correctness of the table above (docs/superpowers/plans/2026-10-14-plan-47-noP.md).
