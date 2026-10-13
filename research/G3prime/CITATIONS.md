# G3′ citations

Citation gate (AGENTS.md rule 4): each entry is quoted from a source read on 2026-10-13. Status is READ or GAP.

## (C1) Explicit Riemann–von Mangoldt formula — READ

T. S. Trudgian, "An improved upper bound for the argument of the Riemann zeta-function on the critical line II",
arXiv:1208.5846v2. Read from the arXiv PDF, §1. (The venue "J. Number Theory 134 (2014) 280–292" comes from the arXiv
abstract page; it is not in the PDF read.)

> Theorem 1. |S(T)| ≤ 0.111 log T + 0.275 log log T + 2.450, for T ≥ e.
>
> This implies the following result concerning N(T), the number of complex zeroes of ζ(s) with imaginary parts in
> (0, T).
>
> Corollary 1. For T ≥ T₀ ≥ e
>   | N(T) − (T/2π) log(T/2πe) − 7/8 | ≤ 0.111 log T + 0.275 log log T + 2.450 + 0.2/T₀.
>
> (1.2) |S(T)| ≤ 1, for 0 ≤ T ≤ 280, |S(T)| ≤ 2, for 0 ≤ T ≤ 6.8·10⁶.

**How it is used.** In this file, N₀(T) := (T/2π) log(T/2πe) + 7/8. Corollary 1 with T₀ = e gives, for all T ≥ e,

  |N(T) − N₀(T)| ≤ E(T) := 0.111 log T + 0.275 log log T + 2.524.

N is monotone and the right-hand side is continuous. So the same bound holds for the one-sided limits N(T ± 0), and
the convention for N at an ordinate does not matter. Trudgian defines N(T) as the number of zeros ρ = β + iγ with 0 < β < 1 and 0 < γ < T. Multiplicity is not stated in
words. It follows from his identity πN(T) = Δ_C arg ξ(s) (argument principle, §2), which counts zeros with
multiplicity. The
ordinate list γ_1 ≤ γ_2 ≤ … used for the G3′ measure is that count, so N(γ_k − 0) ≤ k − 1 and N(γ_k + 0) ≥ k.

## (C2) Multiplicity bound — derived, no citation

For each ordinate γ, the number of k with γ_k = γ is at most N(γ + 0) − N(γ − 0) ≤ 2E(γ) + (N₀(γ + 0) − N₀(γ − 0)),
which equals 2E(γ) = O(log γ), by (C1). See PROOF.md Lemma Z1.

## (C3) Proportion of simple zeros — READ

S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, "Pair correlation of zeros of the
Riemann zeta function I: proportions of simple zeros and critical zeros", arXiv:2501.14545v3. Read from the arXiv PDF,
§1 (Introduction).

> "In 2020 Pratt, Robles, Zaharescu, and Zeindler [PRZD20] proved that more than 41.72% of the zeros are on the
> critical line and that more than 40.75% of the zeros are on the critical line and simple."
>
> "Under RH, Montgomery [Mon73] showed asymptotically at least 2/3 of the zeros are simple, … Chirre, Gonçalves,
> and de Laat [CdL20] used Montgomery's method to show that, under RH, more than 67.92% of the zeros are simple."
>
> "[Conrey, Ghosh, Gonek] showed on RH and an additional hypothesis that at least 19/27 = .703 of the zeros are
> simple. Later Bui and Heath-Brown [BHB13] showed that this result holds on RH alone."

**What is used.** The source surveys the best-known proportions of simple zeros. The best unconditional result it
quotes is "more than 40.75%" (simple and on the line), and no result it quotes reaches proportion 1, conditional or
not. The source does not state in so many words that "density-one simplicity is open". In PROOF.md and LOG.md, that
status is therefore written as "not among the results surveyed in (C3); the best surveyed unconditional proportion is
> 40.75%". It is never written as a bare claim.

The secondary-source pointer to Bui–Conrey–Young, arXiv:1002.4127, was checked: its abstract concerns zeros on the
critical line (> 41%). It is not used.

## (C4) Small gaps — not needed (Ruling)

Hypothesis (SG) of Theorem G3′-L implies that the repeated ordinates have density 0, which in turn implies that
almost all zeros are simple. (SG) also forces almost all zeros to have horizontal multiplicity H(γ) = 1 ((C3) §1.3), which is the "simple and on
the line" type of quantity behind the 40.75% figure. So (SG) is at least as strong as a statement absent from (C3), and no separate
small-gaps citation is needed to record that (SG) is not available unconditionally. If a later revision needs the
precise status of small-gap density bounds, that becomes a new citation task.
