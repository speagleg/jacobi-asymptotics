# Plan 17: G3′ — an unconditional bounded defect, and the pair-correlation conditional

> Native execution. A research plan with Rule R at the end.

**Goal.**
- **Theorem B (unconditional).** For the true-zero measure σ there is an explicit θ₀ > 0 with
  liminf (1/n²)[log D_n(σ) − Φ_n] ≥ 2 log θ₀. So the averaged Law P holds for the true zeros up to a bounded
  multiplicative constant: log D_n = Φ_n + O(n²).
- **Theorem C (conditional, no RH).** Montgomery's pair-correlation conjecture (PCC, vertical distances only, as in
  GLSS) implies (SG), and therefore G3′.
- **Remark D.** The constant: what Lamzouri's 2026 bounds and better kernels would give (optional).

**Inputs (Rule C; read 2026-10-14).**
- Goldston–Lee–Schettler–Suriajaya, arXiv:2503.15449v4 (GLSS):
  - (6.1), the unconditional average pair correlation via Gallagher–Mueller Prop. 1 and Fujii's Prop. 2;
  - Theorem 1 (PCC ⇒ 100% simple and critical);
  - Theorem 2 (HMH);
  - the PCC statement;
  - the proof of Theorem 1 (N(λ₀) ≪ λ₀³TL).
- Lamzouri, arXiv:2609.02882v2: Theorem 1.1 (context; optional for the constant).
- Repo: G3prime PROOF.md (Z1, Z2, Theorem T/T′, Lemma K, G3′*-L, N′).

**Method for B.**
1. Pair count on dyadic blocks from GLSS (6.1) with λ = 2.
2. Cauchy–Schwarz on the horizontal multiplicities H(γ), giving many distinct ordinates.
3. Caro–Wei independent set: distinct ordinates pairwise more than 1 apart in normalized units, with positive density on
   every block.
4. Greedy thinning to a convergent density θ.
5. Monotonicity of D_n.
6. The G3′*-L argument transferred to the subset, with (SG*) holding trivially (as in N′'s transfer).
7. Normalization comparison: 2 log θ.

**Constraints.** AGENTS.md: no RH framing (zeros' ordinates are inputs; conditional statements are labelled as such);
Rule C; Rule R before REVIEWED; commit prefix `G3p:`.

- [x] CITATIONS entries (GLSS, Lamzouri).
- [x] Theorem B write-up (G3prime PROOF.md §8). Ruling: θ₀ is not explicit, because Fujii's O-constant is not explicit in GLSS.
- [x] Theorem C write-up.
- [x] Rule R (opus): ACCEPT WITH FIXES (F1 major → Fix A); re-check ACCEPT; Theorems B, C REVIEWED.
