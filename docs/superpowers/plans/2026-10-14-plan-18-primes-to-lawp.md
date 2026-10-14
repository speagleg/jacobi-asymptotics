# Plan 18: from prime pairs to Law P for the true zeros (G3′ via the primes–zeros duality)

> Native execution. A research plan with Rule R at the end.

**Goal.** Place G3′ inside the primes–zeros duality. Prove:
- **Theorem P.** Assume RH and the variance of primes in short intervals,
  (V) ∫_1^X(ψ(x+h) − ψ(x) − h)²dx ~ hX log(X/h) uniformly for 1 ≤ h ≤ X^{1−ε}, for every ε > 0.
  Then G3′ holds: log D_n(σ) = Φ_n + o(n²).
  Chain: (V) ⇒ SPC (Goldston–Montgomery) ⇒ PCC (Goldston Thm 4) ⇒ (SG) (Theorem C) ⇒ G3′ (G3′-L, G3′-U).
- **Proposition P′ (why twin primes are the wrong input).** The pointwise Hardy–Littlewood pair conjecture with
  power-saving errors gives (V) only for h ≤ X^{1/2−ε}, i.e. SPC only on 1 ≤ α ≤ 2 − ε (Goldston notes §9;
  Montgomery–Soundararajan Thm 3). The missing range needs the pair-correlation errors to cancel *on average over long
  shifts* (M–S Conjecture 1, K = 2).
  - Record what α ≤ 2 − ε buys for G3′: a better constant in Theorem B (optional).
- **Numerical sanity** (NUMERICAL, Odlyzko zeros, data/raw):
  - the small-gap profile #{normalized gaps < δ}/N against the GUE prediction ~(π²/9)δ³ (repulsion, the content of
    (SG));
  - the G3′ defect (2/n²)Σ(n−j)log(b_j/x̃_j) − log(π²/16) for the true-zero measure.
- **Stretch.** Can RH be removed from the chain, in the spirit of GLSS's horizontal multiplicity? This is open; record
  the obstruction.

**Inputs read (Rule C).**
- Montgomery–Soundararajan, arXiv:math/0409258 (Thm 3, Conj. 1, the G–M equivalence statement).
- Goldston, "Notes on pair correlation of zeros and prime numbers", arXiv:math/0412313 (SPC, PCC, Thm 4, Thm 7,
  (9.3), §9 remarks).
- Matomäki–Radziwiłł–Tao, arXiv:1707.01315 (context: averaged H-L; why it falls short).

**Constraints.** AGENTS.md: no RH framing. RH appears only as a labelled hypothesis of a conditional theorem, never as
something supported or tested. Rule C; Rule R; commit prefix `G3p:`.

- [ ] CITATIONS (C7) M–S, (C8) Goldston notes, (C9) MRT.
- [ ] §9 Theorem P and Proposition P′.
- [ ] Numerical checks (gap profile, G3′ defect on true zeros).
- [ ] Rule R; fixes; re-check.
