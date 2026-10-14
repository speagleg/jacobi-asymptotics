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
§1 (Introduction) and §3 (read 2026-10-14 for Plan 18: "(3.1) F(x, T) := Σ_{ρ,ρ′∈Z(T)} x^{ρ−ρ′}W(ρ − ρ′), where W(u) :=
4/(4 − u²)"; "While the definition of F(x, T) does not depend on RH, the asymptotic formula Montgomery obtained for
F(x, T) when 1 ≤ x ≤ T does depend on RH"; proof of Lemma 4: "Since W(ρ−ρ′) is complex-valued we need to remove this
weight").

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

**Plan 19 addendum (read 2026-10-14, §3).**
> "Montgomery Theorem (MT). For x ≥ 1 and T ≥ 3, we have F(x, T) ≥ 0, F(x, T) = F(1/x, T), and
> (3.2) F(x, T) = (T/2πx²) log²T (1 + O(1/√log T)) + (T/2π) log x + O(T √log T), uniformly for 1 ≤ x ≤ T."
> "the sum F(x, T) above is taken over zeros satisfying T < γ, γ′ ≤ 2T"; "the error terms appearing above have been
> corrected from those in the original statement"; footnote 2: "All the applications of Theorem 1 in [BGSTB24], such
> as Lemma 5 and Lemma 7, remain correct".

> §2.1: "Let Z(T) denote the multiset of those ρ ∈ Z for which T < γ ≤ 2T".

**Used in:** rhfree/RHFREE.md:
- Lemma PC: MT on |α| ≤ 1; positivity F ≥ 0 to bound the Q″ term; evenness F(x, T) = F(1/x, T).
- §0 and Theorem S: the multiset convention for Z(T).

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
> unconditionally for the 2k-th moments." **Secondary statement** (Rule R F4): Fujii's and Tsang's originals were not read;
> GLSS's statement is quoted, as was done for (C3).
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

## (C7) Montgomery–Soundararajan, "Primes in short intervals", arXiv:math/0409258 — READ (§0), for Plan 18

> "(18) M_K(N; H) = Σ_{n=1}^N (ψ(n + H) − ψ(n) − H)^K". "Theorem 3. Let E_k(x; D) be defined by the relation
> Σ_{n≤x}Π_{i=1}^k Λ(n + d_i) = S(D)x + E_k(x; D), and suppose that (20) E_k(x; D) ≪ N^{1/2+ε} uniformly for 1 ≤ k ≤ K,
> 0 ≤ x ≤ N, and distinct d_i satisfying 1 ≤ d_i ≤ H. Then M_K(N; H) = µ_K H^{K/2}∫_1^N(log x/H + B)^{K/2}dx + O(…)
> uniformly for log N ≤ H ≤ N^{1/K}". "In the case k = 1 … the hypothesis that E_1(N; {1}) ≪ N^{1/2+ε} is equivalent to
> the Riemann Hypothesis (RH)." "Conjecture 1. For each positive integer K, M_K(N; H) = (µ_K + o(1))N(H log N/H)^{K/2}
> uniformly for (log N)^{1+δ} ≤ H ≤ N^{1−δ}." "We recall that Goldston & Montgomery [8] showed that if RH is true, then
> the stronger form (F(α) ∼ 1) of the Pair Correlation Conjecture as formulated by Montgomery [13] is equivalent to the
> case K = 2 of the Conjecture above." Also (16): "R2(h) = −h log h + Ah + O(h^{1/2+ε})".

**Used in:** G3prime PROOF.md §9 (Theorem P, Proposition P′).

## (C8) Goldston, "Notes on pair correlation of zeros and prime numbers", arXiv:math/0412313 — READ (§§4–6, 9), for Plan 18

> "Strong Pair Correlation Conjecture (SPC). For any fixed bounded M, (6.6) F(α) = 1 + o(1), for 1 ≤ α ≤ M."
> "Pair Correlation Conjecture (PCC). For any fixed β > 0, (6.7) N(T, β) := (T log T/2π)^{−1}Σ_{0<γ,γ′≤T,
> 0<γ′−γ≤2πβ/log T} 1 ∼ ∫_0^β(1 − (sin πu/πu)²)du."
> "Theorem 4. Assume the Riemann Hypothesis. SPC implies PCC and SZC." (proof given via (6.12)–(6.15)).
> "Theorem 7. Assume the Riemann Hypothesis. … Conversely, if 1 ≤ A1 ≤ A2 < ∞, then (9.2) [F(x, T) ∼ (T/2π)log T]
> holds uniformly for T^{A1} ≤ X ≤ T^{A2} provided that (9.1) holds uniformly for X^{−1/A1}(log x)^{−3} ≤ δ ≤
> X^{−1/A2}(log x)³." "In particular, one can prove on RH that SPC is equivalent to (9.3) ∫_1^X(ψ(x + h) − ψ(x) − h)²dx ∼
> hX log(X/h) for 1 ≤ h ≤ X^{1−ε}". "it is a straightforward exercise to show that the twin prime conjecture in the
> form (6.3) implies (9.1) and (9.3) in the ranges X^{−1} ≤ δ ≤ X^{−1/2−ε} and 1 ≤ h ≤ X^{1/2−ε} respectively, and
> consequently we again obtain that (6.3) implies SPC in the range 1 ≤ α ≤ 2 − ε." (6.3): "Σ_{n≤N}Λ(n)Λ(n + k) = S(k)N +
> O(N^{1/2+ε})".

Also footnote 6: "If (9.3) holds for this range of h it implies RH."

**Used in:** §9. Theorem 7 is Goldston–Montgomery's (Goldston is a co-author). The SPC ⇔ (9.3) step via Saffari–Vaughan
is stated, not proved, in the notes, so it is a **secondary statement** here.

## (C9) Matomäki–Radziwiłł–Tao, arXiv:1707.01315v3 — READ (abstract), context for Plan 18

> "Our main result is that the expected asymptotic for the first three sums [incl. Σ_{X<n≤2X}Λ(n)Λ(n+h)] holds for
> almost all h ∈ [−H, H], provided that X^{σ+ε} ≤ H ≤ X^{1−ε} for some ε > 0, where σ := 8/33 = 0.2424…, with an error
> term saving on average an arbitrary power of the logarithm over the trivial bound."

**Used in:** §9 Proposition P′(b): log-power savings are insufficient for (V).

### (C6) addendum — READ (§2 Prop 2.1 and its proof; §3 Lemmas 3.1–3.2 and proof), for Plan 19

> "Proposition 2.1. Let λ > 0 be a real number and η ∈ L²(ℝ) be a real valued even function with supp(η) ⊂ (−λ, λ),
> such that η̂²(0) = 1. Let Z be a non-empty finite multiset of complex numbers which is invariant under complex
> conjugation. … Then we have (2.4) Σ_{z∈Z∩ℝ, m_z=1} 1 ⩾ 2Σ_{z∈Z} 1 − Σ_{z,s∈Z} K(z − s)², where K is the kernel
> K(ξ) := η̂²(ξ)."

From the proof:
- (2.8) "f_z(u) := η(u)e^{−2πiuz}". g_z and h_z are the symmetric and antisymmetric combinations of f_z and its
  conjugate partner.
- (2.10) "∫_{−λ}^{λ}|f_x(u)|²du = K(0) = 1".
- (2.11) "1 = ∫|g_z|² − ∫|h_z|²".
- (2.12) "Σ_{z,s∈Z} K²(z − s) = … = ∫∫|F(u, v)|² du dv".
- "f_{x_1}, …, f_{x_{n+r}}, g_{z_1}, …, g_{z_k}, h_{z_1}, …, h_{z_k} are linearly independent over ℂ".
- (2.15): the inner product of two functions with Φ(u) = conj Φ(−u) is real.
- (2.21) "Σ_{1⩽j⩽D_W} α_j = Σ m_{x_ℓ} + 2Σ m_{z_ℓ} = Σ_{z∈Z} 1".

From §3:
- "(3.2) r_{δ,T} := Q_δ − Q″_δ/(4(log T)²)".
- "Q̂″_δ(z) = (2πiz)²Q̂_δ(z) = −4π²z²K_δ(z)²".
- (3.3) "K_δ(i(ρ − ρ′)log T/2π)² = r̂_{δ,T}(…)w(ρ − ρ′)".

**Used in:** rhfree/RHFREE.md:
- Lemma PC: the weight-removal algebra, applied with support 2λ in place of 1. It is pure algebra and does not use the
  support.
- Lemma G, Step 1: tr A = N and ‖A‖²_HS = S, via (2.10)–(2.13), (2.15) and (2.21).
- Theorem S(a): (2.4).

Note: rendering of conjugation bars in the text extraction is lossy. g_z, h_z are reconstructed as
(f_z ± f_{z̄})/(2 or 2i), consistent with (2.11), (2.14) and the numerics in rhfree/checks.

### (C3) addendum — Plan 20 (read 2026-10-14, §3)
> (3.5) "F_{(0,T]}(x) = (T log²T/2πx²)(1 + O(1/√log T)) + (T/2π) log x + O(T √log T)"; "Thus we have obtained MT
> for F_{(0,T]}(x)".
> "The statement above has been modified from its original formulation in [BGSTB24], with two changes."
> After Lemma 1 (3.6)–(3.7): "This was proved unconditionally as Lemma 3 in [BGSTB24] with the sum over terms with
> 0 < γ ≤ T. That proof works line by line for both (3.6) and (3.7)."

[BGSTB24] itself has NOT been read. Full-window positivity in RHFREE2 §1 is made self-contained by an elementary
residue identity (`checks/check_pos_identity`).

### (C8) addendum — Plan 20 (read 2026-10-14, §9: Theorem 7 and its proof)
> "(9.9) L(x, T) = 4x³ ∫_x^∞ I(y, δ) dy/y⁵ + O(x³(log T)²/T³)". "Since the integrand is non-negative, if we have an
> asymptotic formula for L(x, T) then a simple differencing argument will give an asymptotic formula for I(x, δ). The
> converse is immediate."
> "In view of (4.4), since κ ∼ 1/T, R(x, T) can be related to F(x, T) through Abelian and Tauberian theorems."
> "All the details may be found in [18]".

Goldston–Montgomery [18] has NOT been read, and Goldston's (4.4) itself has not been quoted.

**Used in:** RHFREE2 §4 (obstruction analysis, HEURISTIC).
