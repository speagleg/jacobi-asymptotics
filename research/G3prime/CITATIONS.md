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

## (C5) Goldston–Lee–Schettler–Suriajaya, arXiv:2503.15449v4 (GLSS) — READ (§§1–8), for Plan 17

> (3.6) "L := (1/2π) log T", "(3.7) N(T) = (T/2π) log T + O(T) = TL + o(TL) … the average vertical spacing between zeros
> is 1/L". Zeros are taken from the multiset Z ("a zero ρ … with multiplicity mρ is counted as mρ zeros").
>
> "(4.3) N(λ) := N(T, U) = Σ_{ρ,ρ′: 0<γ,γ′≤T, 0<(γ′−γ)L≤λ} 1." "Pair Correlation Conjecture (PCC). For UL = λ > 0, then
> N(λ) = TL∫_0^λ(1 − (sin πα/πα)²)dα + o(TL), as T → ∞, uniformly in each interval 0 < λ0 = U0L ≤ λ = UL ≤ λ1 = U1L < ∞."
>
> "Proposition 2 (Fujii). For 0 < U ≤ 1, we have as T → ∞, ∫_0^T (∆_U S(t))² dt = (T/π²) log(2 + UL) + O(T√log(2 + UL)).
> For the proof of this Proposition, see Fujii [Fuj74, Fuj81] and Tsang [Tsa84, Tsa86]. They both prove this
> unconditionally"
>
> "6. An Unconditional Average Pair Correlation Formula. We take UL = λ and assume 0 < U ≤ 1 … imposing 0 < λ² ≤ L and
> multiplying by L/λ, we get (6.1) Σ_{ρ,ρ′: 0<γ,γ′≤T, |γ′−γ|L≤λ} (1 − |γ′ − γ|L/λ) = TL(λ + log(2 + λ)/(π²λ) + O(√log(2 + λ)/λ))."
>
> "(7.1) N^⊛(T) = Σ_{ρ,ρ′: 0<γ,γ′≤T, γ=γ′} 1 = Σ_ρ H(γ), where H(γ) := Σ_{ρ′: γ′=γ} 1."
>
> "Theorem 1. Assuming the pair correlation conjecture PCC, then asymptotically 100% of the zeros of ζ(s) are simple
> and on the critical line." Proof of Theorem 1: "By PCC we have upon using the Taylor expansion of sin x around the
> origin, N(λ0) ≪ TL∫_0^{λ0} α²dα = O(λ0³TL)", and it concludes "N^⊛(T) = TL + o(TL) which establishes HMH".
> GLSS state: "In this paper we do not assume the Riemann Hypothesis (RH) is true or make use of results that depend on RH."

**Used in:** PROOF.md §8 (Plan 17). Theorem B uses (6.1) with fixed λ; the implied constant in its O-term is not explicit.
Theorem C uses PCC ⇒ N(λ0) = O(λ0³TL) and N^⊛(T) = TL + o(TL).

## (C6) Lamzouri, arXiv:2609.02882v2 — READ (§§1–3 statements), context for Plan 17

> "Theorem 1.1. … lim inf N0^s(T)/N(T) ⩾ C0 = 0.67250…, and lim inf Nd(T)/N(T) ⩾ C1 := (C0 + 1)/2 = 0.83625 …"
> (N_d = number of distinct zeros; N0^s = simple zeros on the critical line), unconditional; it is proved via
> "Montgomery's pair correlation theorem in the unconditional form obtained by Baluyot, Goldston, Suriajaya and
> Turnage-Butterbaugh (see Lemma 5 of [3])".

**Used in:** PROOF.md §8 remarks only (distinct *zeros* are not distinct *ordinates*; off-line pairs share ordinates).
It updates (C3)'s 0.4075 to 0.6725 for "simple and on the line".
