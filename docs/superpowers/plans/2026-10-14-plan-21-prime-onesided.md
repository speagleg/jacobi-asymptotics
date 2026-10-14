# Plan 21: RH + one-sided prime variance ⇒ G3′ (question Q1; RHFREE2 §4)

**Goal:** bypass the Tauberian obstruction by keeping Goldston's Fejér weight on the zero side.

**Spec:** PROOF.md §9.3 (Q1); RHFREE2.md §4; AGENTS.md.

## Tasks
- [x] **T1.** Pair form of G = R/(2xκ²), with Ψ ∈ [0, 1] (exact, from (C8) (4.1)–(4.2)).
- [x] **T2.** Lemma P1: (V⁺) ⇒ G ≤ (1 + o(1))N_Ψ on [1, M], via (C8) (9.7)–(9.9) (full-range error as cited) and a
  trivial tail bound.
- [x] **T3.** Lemma P2: weighted MT on [0, 1], via (4.4), (C3) (3.5), a Stieltjes integral truncated at ΛT, and
  dyadic variation bounds.
- [x] **T4.** Lemma P3: weighted K² sum ≤ N_Ψ(1 + D), via the (C6) weight removal.
- [x] **T5.** Theorem V⁺: counting by positivity (RH), Ψ ≥ 0.7 on the bulk, then (SG) ⇒ G3′.
- [x] **T6.** Numerics `checks/check_weighted_pc.py` on the Odlyzko zeros.
- [x] **T7.** Rule R review: fixes, then re-check, then labels; CITATIONS (C8) Plan-21 addendum; LOG; PROOF.md row.

## Review focus
- (9.7)'s Σ_γ ranges over all zeros. Is G's pair form (with t ≥ 0 only) exactly Goldston's R/(2xκ²)?
- Lemma P1: the y-range bookkeeping against (V⁺)'s δ-range; the trivial tail bound; the reliance on (9.9)'s
  full-range error.
- Lemma P2: the dyadic variation bounds for φ = sinc²; the truncation at ΛT; the H = F + O(log³) identification;
  the N_Ψ asymptotic.
- Theorem V⁺: the Ψ ≥ 0.7 lower bound; ordered vs unordered pairs; repeats.
- Is the hypothesis (V⁺) correctly scoped (one-sided, bounded range for each M), and is RH used only as labelled?
