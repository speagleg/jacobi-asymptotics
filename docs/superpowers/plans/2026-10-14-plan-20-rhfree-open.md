# Plan 20: open questions after Theorem S (RHFREE §4, §6)

**Goal:** remove the dyadic caveat of Theorem S, make the quasi-RH question precise, and analyse the prime-side
one-sided transfer.

**Spec:** research/G3prime/rhfree/RHFREE.md §4 and §6; AGENTS.md (Rules A, C, N, R).

## Tasks
- [x] **T1.** Theorem S′ (full window, via (C3) (3.5) and the full-window positivity remark). On RH the hypothesis is
  exactly the upper half of Montgomery's SPC.
- [x] **T2.** Lemma N (Sylvester inertia + Ky Fan): E ≥ k + 4Σ m_z dist(h_z, V)².
- [x] **T3.** Proposition Q: SPC_ℂ⁺ + (NA) ⇒ quasi-RH. (NA) is stated as a hypothesis, with a numerical probe
  (`checks/check_dist_probe.py`).
- [x] **T4.** Prime-side obstruction: (C8) Theorem 7's Fejér/Tauberian step loses a constant factor C > 1, but Lemma G
  needs C → 1. Reduced to a weighted Lemma G (OPEN).
- [x] **T5.** Rule R review: fixes, then re-check, then labels.

## Review focus
- Is the full-window positivity legitimately quoted, given that (3.6) is stated for (T, 2T]?
- Is "SPC_ℂ⁺(full) on RH = the upper half of Montgomery's SPC" correct, including the W vs w normalization?
- Lemma N: the bijectivity of V, the Sylvester inertia count k, and the Ky Fan direction.
- Proposition Q: the lower bound for K(2iyL), and the choice of representative with Im z > 0.
- The §4 obstruction claim: is it fair to say that Theorem 7's route gives only C > 1?
