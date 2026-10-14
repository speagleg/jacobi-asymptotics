# Plan 16: G3′ closure — Theorem N′ (necessity of no positive-density repeats)

> Native execution; small plan (one theorem + Rule R).

**Goal.** Replace GAP N′ in research/G3prime/PROOF.md by a theorem. If the repeated indices E of the true ordinates
contain a subset of convergent positive density (d_*(E) > 0), the multiplicity-normalized law fails, with
limsup (1/n²)[log D_n − Φ_n] ≤ 2 log(1 − d_*(E)). Then record the final G3′ sandwich: U unconditional, L under (SG),
and necessity of d_*(E) = 0.

**Method.**
1. Monotonicity of D_n under enlarging the measure.
2. Re-add the repeats outside E′ as tiny-shifted atoms. This gives a Z1-thinning of convergent density 1 − δ′.
3. Apply the reviewed G3′*-U argument (§7.1) verbatim.
4. Compare normalizations via Theorem T (P1) and H6(a).

**Not attempted (residual GAP).** E with positive lower density but d_*(E) = 0 (oscillating, gappy repeats). This
needs a thinning law for non-convergent densities, which Theorem T excludes.

**Constraints.** AGENTS.md: no RH framing; Rule C; Rule R before REVIEWED; commit prefix `G3p:`.

- [x] Write Theorem N′, the remarks and the sandwich (§5 of PROOF.md); update the status table.
- [x] Rule R (opus): ACCEPT WITH FIXES; F1–F8 applied; re-check confirmed REVIEWED.
