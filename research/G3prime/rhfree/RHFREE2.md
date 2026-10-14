# RHFREE2: open questions after Theorem S (Plan 20) — NOT REVIEWED (Rule R pending)

Follow-up to RHFREE.md, whose Theorem S, Lemma PC and Lemma G are REVIEWED. Notation is as there:
- Z(T), N_T, L = (1/2π)log T, F(x, T), 𝓕(α);
- η_λ, K, Q, D(η);
- the operator A on H_ℝ, with W = span{f_x, g_z, h_z} and E = S − 2N + N_d.

| Item | Content | Label |
|---|---|---|
| Theorem S′ | Full-window version: on RH the hypothesis is exactly the upper half of Montgomery's SPC | PROVED-mod-cite ((C3) (3.5) and Lemma-1 remark, (C6), (C1)) + mod-input SPC_ℂ⁺(full), Theorem H |
| Lemma N | Inertia bound: E ≥ k + 4Σ m_z dist(h_z, V)² | PROVED (deterministic) |
| Prop. Q | SPC_ℂ⁺ + (NA) ⇒ max_{T<γ≤2T}\|β − ½\| → 0 (quasi-RH) | PROVED-mod-input SPC_ℂ⁺, (NA) |
| (NA) | Non-approximation hypothesis | HYPOTHESIS; NUMERICAL support only |
| §4 | Prime-side one-sided transfer (Q1) | OBSTRUCTION identified; OPEN |

## 1. Theorem S′ (full window; removes the dyadic caveat of RHFREE Rule R F1)

**Inputs** ((C3), read 2026-10-14, BGST §3).
- For the full window 0 < γ ≤ T, BGST prove (3.5): "F_{(0,T]}(x) = (T log²T/2πx²)(1 + O(1/√log T)) +
  (T/2π)log x + O(T√log T)", for 1 ≤ x ≤ T, with the remark "Thus we have obtained MT for F_{(0,T]}(x)".
- Positivity: (3.6) expresses F_{(T,2T]}(x) as (2/π)∫|Σ_ρ …|²dt, and BGST add: "This was proved unconditionally as
  Lemma 3 in [BGSTB24] with the sum over terms with 0 < γ ≤ T."
- Hence F_{(0,T]}(x) ≥ 0. Evenness in log x follows from swapping ρ and ρ′, since W is even.

**Hypothesis SPC_ℂ⁺(full).** For every M ≥ 1: limsup_T sup_{1≤α≤M} F_{(0,T]}(T^α)/N(T) ≤ 1.

On RH, β = β′ = ½. Then x^{ρ−ρ′}W(ρ − ρ′) = x^{i(γ−γ′)}·4/(4 + (γ − γ′)²), so F_{(0,T]} is Montgomery's F(x, T).
**SPC_ℂ⁺(full) is then exactly the upper half of Montgomery's SPC:** F(α) ≤ 1 + o(1) uniformly on [1, M] for each M.
Without RH it is the RH-free complex-weighted version.

**Lemma PC′.** Assume SPC_ℂ⁺(full). Then Σ_{0<γ,γ′≤T}K(i(ρ − ρ′)L)² ≤ N(T)(1 + D(η)) + o(N(T)).

*Proof.* This is RHFREE Lemma PC verbatim, with three changes:
- Z(T) is replaced by the zeros with 0 < γ ≤ T, and N_T by N(T) = (T/2π)log T(1 + O(1/log T)) (C1).
- (3.2) is replaced by (3.5), which has the same shape and the same error terms.
- Positivity comes from the full-window form of (3.6) quoted above.

The weight-removal algebra does not depend on the window. ∎

**Theorem S′.** SPC_ℂ⁺(full) ⇒ the conclusions (a), (b), (c) of Theorem S. In particular:
- **RH + (upper half of Montgomery's SPC) ⇒ (SG) ⇒ G3′.**
- Without RH: SPC_ℂ⁺(full) ⇒ G3′, mod Theorem H.

*Proof.*
- Apply Lemma G to Z := {i(ρ − ½)L : 0 < γ ≤ T}. As in Theorem S:
  - E ≤ N(T)D + o(N(T)) and N_d − N₁ ≤ N(T)D + o(N(T)) (via (C6) (2.4));
  - Lemma G at gap 2δ, with λ = 1/(8πδ), bounds the consecutive simple-critical pairs with (γ′ − γ)L < 2δ by
    20D·N(T) + o(N(T));
  - pairs with an endpoint that is not simple-critical number ≤ 2D·N(T) + o(N(T)).
- Normalization: for γ_k ∈ (T/R, T], log(γ_k/2π)/2π ≥ L(1 − log R/log T − O(1/log T)), so g_k < δ implies
  (γ_{k+1} − γ_k)L < 2δ for large T. Indices with γ_k ≤ T/R number ≤ (1/R + o(1))N(T).
- Hence #{k ≤ N(T) : g_k < δ} ≤ (22D(η_λ) + 1/R + o(1))N(T), with D(η_λ) ≤ ‖Q₁″‖_∞(8πδ)³/12. Take R = 3/η.
  No dyadic summation is needed.
- (SG) follows, and G3′ follows from G3′-L (mod Theorem H) and G3′-U. ∎

**Remark S′1 (relation to Theorem C and Corollary P).**
- On RH, two-sided SPC ⇒ PCC is Goldston's Theorem 4 ((C8); this is Corollary P's route).
- Theorem S′ needs only the upper half, and for each (SG) tolerance η only the range [1, M(η)] with M ≍ η^{−1/3}.
- Novelty: UNCHECKED.

## 2. Does SPC_ℂ⁺ confine the zeros near the line? Lemma N and Proposition Q

**Lemma N (inertia bound; deterministic).** Take the setting of Lemma G.
- Let k be the number of distinct non-real z with Im z > 0, and V := span{f_x, g_z} ⊂ W, of dimension N_d − k.
- Let d_z := dist(h_z, V) in L².

Then A|_W has exactly k negative eigenvalues, and

  E = Σ_i(μ_i − 1)² ≥ k + 4Σ_{Im z>0} m_z d_z².

*Proof.*
1. **Inertia.** A|_W = VJV*, where V: ℝ^{N_d} → W maps the coordinate vectors to the basis (f_x, g_z, h_z). This basis
   is linearly independent (RHFREE Lemma G, Step 1), so V is bijective, and J = diag(m_x, 2m_z, −2m_z). By
   Sylvester's law of inertia, A|_W and J have the same inertia: exactly k negative eigenvalues.
2. **Ky Fan.** Let P be the orthogonal projection onto W ⊖ V, which has dimension k. Then P f_x = P g_z = 0, so
   tr(PAP) = −2Σ m_z‖P h_z‖² = −2Σ m_z d_z².
   - Ky Fan's minimum principle: the sum of the k smallest eigenvalues of A|_W is at most tr(PAP).
   - The k smallest eigenvalues are exactly the negative ones (step 1).
   - So Σ_{μ<0}|μ| ≥ 2Σ m_z d_z².
3. **Sum.** For μ < 0, (μ − 1)² = (1 + |μ|)² ≥ 1 + 2|μ|. Summing over the k negative eigenvalues gives
   E ≥ k + 4Σ m_z d_z². ∎

**Corollary N1 (unconditional, given SPC_ℂ⁺).** In the dyadic window, Σ_{Im z>0} m_z d_z² ≤ (D(η)N_T + o(N_T))/4 for
every admissible η (by Lemma PC). This is a weighted density statement for off-line zeros, measured by how far h_z sits
from the "critical" span V.

**Size of h_z.** For z = −γL + iyL with y := |β − ½| > 0 (choosing the representative with Im z > 0):
- ‖f_z‖² = ‖f_z̄‖² = K(2iyL) and ⟨f_z, f_z̄⟩ = K(0) = 1.
- Hence ‖h_z‖² = (K(2iyL) − 1)/2 and ⟨g_z, h_z⟩ = 0.
- For η_λ: K(2iyL) = ∫η_λ²(u)e^{4πuyL}du ≥ κ₁e^{2πλyL} = κ₁T^{λy}, where κ₁ := ∫_{u≥1/2}η₁² > 0.

**Hypothesis (NA) (non-approximation).** There are c > 0 and λ_j → ∞ such that for each j and all large T, every zero
ρ ∈ Z(T) with |β − ½| ≥ 1/log T satisfies d_z ≥ c‖h_z‖ (with η = η_{λ_j}).

**Proposition Q.** SPC_ℂ⁺ + (NA) ⇒ for every c₀ > 0 there is T₀ such that no zero with T > T₀ and T < γ ≤ 2T has
|β − ½| ≥ c₀. That is, max_{T<γ≤2T}|β − ½| → 0. This is quasi-RH, **not RH**.

*Proof.*
- Suppose a zero in Z(T) has |β − ½| ≥ c₀ (and ≥ 1/log T).
- By Lemma N, (NA) and the size computation: E ≥ 4c²‖h_z‖² ≥ 2c²(κ₁T^{λ_j c₀} − 1).
- By Lemma PC: E ≤ D·N_T + o(N_T) ≤ T log T for large T.
- Choose j with λ_j c₀ > 2. Then T^{λ_j c₀} ≫ T log T, a contradiction for large T. ∎

**Status of (NA).** HYPOTHESIS. It is not proved.
- NUMERICAL (`checks/check_dist_probe.out`, synthetic critical configurations of 120 points, GUE-like and Poisson,
  one probed off-line pair):
  - For λ = ¼, d_z/‖h_z‖ ≈ 0 (< 10⁻³). At λ = ½ it is mixed: 0 to 0.31 (GUE-like), ≈ 0 (Poisson). Exponentials of
    density 1 on an interval of length 2λ ≤ 1 are (nearly) complete, consistent with Beurling–Malliavin-type
    heuristics; that is a recollection, not cited.
  - For λ = 2 or 4 and Im z = yL ≥ 0.1, d_z/‖h_z‖ ∈ [0.53, 1.00].
  - With 5 extra off-line g_w in V, at λ = 2: d_z/‖h_z‖ ≥ 0.94.
  - Some λ = 1 Poisson cases dip to 0.001 (incomplete-but-close regime).
- A proof would need a quantitative incompleteness (Beurling-density) estimate for {η(u)e^{−2πiux}} against the
  exponentially tilted h_z. This is a natural harmonic-analysis lemma, but it would have to hold uniformly over the
  zero configuration. **OPEN.**

## 3. Remarks

- **Proposition Q is not RH.** Even with (NA), zeros at distance o(1) from the line, for example |β − ½| ≍ 1/log T,
  are not excluded. Their kernel growth T^{λ|β−½|} stays bounded.
- **Unconditionally,** Lemma N says that negative eigenvalues of A (one per distinct off-line pair) each cost at least
  1 in E. That recovers k ≤ E (weaker than (C6) (2.4)). The new content is the d_z-weighted term.

## 4. (Q1) prime side: why the one-sided transfer is obstructed (OBSTRUCTION; OPEN)

**Goal.** "RH + an *upper* bound for the prime variance (C8 (9.1)/(9.3)) on a bounded range ⇒ the hypothesis of
Theorem S′." That would give "RH + one-sided prime variance ⇒ G3′", weakening Corollary P.

**What the Theorem 7 route gives** ((C8) §9, read):
1. **Upper I ⇒ upper L** (immediate). By (9.9), "L(x, T) = 4x³∫_x^∞ I(y, δ)dy/y⁵ + O(…)", and "Since the integrand
   is non-negative …".
2. **L = R** on RH ((9.7)–(9.8)), where R(x, T) = (4xκ²/π)∫_0^∞ (sin(κt/2)/(κt/2))²|Σ_γ x^{iγ}/(1 + (t − γ)²)|²dt is
   a **Fejér-weighted** (in t) mean square.
3. **R → F** "through Abelian and Tauberian theorems". With only an upper bound on R, a Tauberian step for the
   increasing function t ↦ ∫_0^t|Σ|² gives F(x, T′) ≤ C·(main term). Here C > 1 is a fixed constant from the shape of
   the Fejér kernel: positive-kernel averages bounded above do not control the function at a sharp cutoff without a
   matching lower bound.

**Why a constant C > 1 is useless here.**
- Lemma PC with 𝓕 ≤ C on [1, 2λ] gives E ≤ N(D + 2(C − 1)∫_1^{2λ}Q_λ), and ∫_1^{2λ}Q_λ → ½ as λ → ∞.
- Lemma G then bounds small gaps by ≈ 20(C − 1)N, which does not tend to 0.
- So (SG) needs C → 1.

**Reduction (OPEN).** The natural fix is to bypass the sharp cutoff: run Lemma G with **smooth zero weights**
w_ρ = φ(γ/T) of Fejér type, matching R directly.
- This needs a *weighted* Lemma G: A_w := Σ w_z f_z⊗f_{z̄}. The identity Σ(μ − 1)² = E uses tr A = N and the count
  N_d of nonzero eigenvalues. Both fail with non-constant weights, and off-line pairs make tr A_w² − Σ w_z² of
  indefinite sign.
- A weighted analogue that is robust to slowly varying weights is the missing tool. Recorded as OPEN; not attempted
  rigorously.
