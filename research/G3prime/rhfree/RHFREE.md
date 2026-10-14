# RHFREE: G3′ from an RH-free, one-sided pair-correlation hypothesis (Plan 19) — Rule R pending, NOT REVIEWED

**Question.** (Q2) of PROOF.md §9.3: does strong pair correlation, in BGST's unconditional complex-weighted form, imply
(SG), and hence G3′, without RH?

**Answer obtained here (Theorem S, §3).** Yes, and only the **upper half** is needed:

  SPC_ℂ⁺ ⇒ (a) 100% of zeros are simple and on the critical line; (b) #{small normalized gaps < δ} ≪ δ³·N;
  (c) (SG), hence G3′.

**Route.**
- No real-kernel positivity and no zero-density estimate are used.
- Small gaps come from a **Hilbert–Schmidt / spectral** reading of Lamzouri's Prop. 2.1 operator (Lemma G, §2).
- This bypasses the "Lemma A′" obstruction of the first draft (§5).

**Label.** Lemma PC: PROVED-mod-cite. Lemma G: PROVED. Theorem S: PROVED-mod-cite + mod-input SPC_ℂ⁺, Theorem H.
Rule R review pending. Novelty: UNCHECKED.

## 0. Objects, inputs, hypothesis

- **Zeros.** Z(T) := zeros ρ = ½ + δ_ρ + iγ of ζ with T < γ ≤ 2T, with multiplicity. N_T := |Z(T)| = (T/2π)log T·(1 + o(1)).
  L := (1/2π)log T.
- **BGST's function** ((C3) = BGST, arXiv:2501.14545v3, (3.1); read):
  "F(x, T) := Σ_{ρ,ρ′∈Z(T)} x^{ρ−ρ′}W(ρ − ρ′), W(u) := 4/(4 − u²)".
- **MT** ((C3) (3.2), unconditional, corrected form; read). "For x ≥ 1 and T ≥ 3": F(x, T) ≥ 0, F(x, T) = F(1/x, T),
  and uniformly for 1 ≤ x ≤ T, with the sum over T < γ, γ′ ≤ 2T,

    F(x, T) = (T/2πx²)log²T(1 + O(1/√log T)) + (T/2π)log x + O(T√log T).

- **Normalized form.** 𝓕(α) := F(T^α, T)/N_T, a continuous function of α ∈ ℝ, with 𝓕 ≥ 0 and 𝓕(−α) = 𝓕(α).
- **Hypothesis SPC_ℂ⁺ (one-sided, RH-free).** For every M ≥ 1: limsup_{T→∞} sup_{1≤α≤M} 𝓕(α) ≤ 1.
  - Two-sided SPC_ℂ (𝓕 = 1 + o(1) on [1, M]) implies it.
  - On RH, SPC_ℂ⁺ is the upper half of Montgomery's strong pair correlation.
  - Without RH it is a statement about the zero multiset with complex weights x^{ρ−ρ′}.
  - It is a hypothesis, labelled as such (AGENTS.md framing): ordinates are inputs, and RH is not assumed.
- **Fourier identity (exact; no hypothesis).** Take f ∈ L¹(ℝ) even, compactly supported, and
  f̂(ξ) := ∫f(α)e^{−2πiαξ}dα (entire). Since T^{α(ρ−ρ′)} = e^{−2πiα·i(ρ−ρ′)L},

    (0.1)  Σ_{ρ,ρ′∈Z(T)} f̂(i(ρ − ρ′)L)·W(ρ − ρ′) = N_T ∫ f(α)𝓕(α)dα.

## 1. Lemma PC (the K² sum under SPC_ℂ⁺) — PROVED-mod-cite ((C3) (3.1)–(3.2); (C6) §3 algebra) + mod-input SPC_ℂ⁺

**Setting.**
- Let η ∈ C_c^∞((−λ, λ)) be real and even, with ∫η² = 1.
- K := (η²)^, so K(0) = 1. K is entire and real-valued and even on ℝ.
- Q := η² ∗ η². Then Q ≥ 0, Q is even, Q ∈ C_c^∞((−2λ, 2λ)), Q̂ = K², and ∫Q = 1.
- D(η) := Q(0) − 2∫_0^1(1 − α)Q(α)dα. D(η) ≥ 0 because Q(α) ≤ Q(0) (Q is positive-definite) and 2∫_0^1(1 − α)dα = 1.

**Lemma PC.** Assume SPC_ℂ⁺. Then

  S_T := Σ_{ρ,ρ′∈Z(T)} K(i(ρ − ρ′)L)² ≤ N_T(1 + D(η)) + o(N_T)  (T → ∞, η fixed).

*Proof.*
1. **Remove the weight** (Lamzouri (3.2)–(3.3), read; the computation is pure algebra and valid for any support).
   - Put r_T := Q − Q″/(4 log²T).
   - Integrating by parts twice gives (Q″)^(z) = −4π²z²K(z)².
   - Hence r̂_T(z) = (1 + π²z²/log²T)K(z)².
   - At z = i(ρ − ρ′)L, the factor 1 + π²z²/log²T = 1 − (ρ − ρ′)²/4 = 1/W(ρ − ρ′).
   - So K(z)² = Q̂(z)W − (Q″)^(z)W/(4 log²T) exactly.
   - Sum over pairs and apply (0.1) to Q and to Q″:

     S_T = N_T∫Q𝓕 − (N_T/(4 log²T))∫Q″𝓕.

2. **The Q″ term.** Since 𝓕 ≥ 0 (MT), |∫Q″𝓕| ≤ ‖Q″‖_∞∫_{|α|≤2λ}𝓕.
   - On |α| ≤ 1, MT gives ∫𝓕 = O(1). The spike (T/2πx²)log²T integrates to O(N_T) against dα.
   - On 1 ≤ |α| ≤ 2λ, SPC_ℂ⁺ gives ∫𝓕 ≤ 4λ.
   - So this term is O_η(N_T/log²T) = o(N_T).
3. **|α| ≤ 1** (directly from MT; cf. BGSTB24 Lemma 5 = Lamzouri Lemma 3.1, whose statement this reproduces).
   - By evenness, ∫_{−1}^{1}Q𝓕 = 2∫_0^1Q(α)𝓕(α)dα.
   - With x = T^α and N_T = (T/2π)log T·(1 + O(1/log T)), MT gives
     𝓕(α) = log T·T^{−2α}(1 + O(1/√log T)) + α(1 + O(1/log T)) + O(1/√log T).
   - ∫_0^1Q(α)log T·T^{−2α}dα = ∫_0^{log T}Q(v/log T)e^{−2v}dv = Q(0)/2 + O(‖Q′‖_∞/log T).
   - Hence ∫_{−1}^{1}Q𝓕 = Q(0) + 2∫_0^1 αQ(α)dα + O_η(1/√log T).
4. **1 ≤ |α| ≤ 2λ.** Here Q ≥ 0, so SPC_ℂ⁺ gives ∫_{1≤|α|≤2λ}Q𝓕 ≤ (1 + o(1))·2∫_1^{2λ}Q.
5. **Sum.** S_T/N_T ≤ Q(0) + 2∫_0^1αQ + 2∫_1^∞Q + o(1) = Q(0) + ∫Q − 2∫_0^1(1 − α)Q + o(1) = 1 + D(η) + o(1). ∎

**Scaling.**
- Take η_λ(u) := λ^{−1/2}η₁(u/λ) for a fixed η₁ ∈ C_c^∞((−1, 1)). Then Q_λ(α) = λ^{−1}Q₁(α/λ).
- Q_λ(0) − Q_λ(α) ≤ ‖Q₁″‖_∞α²/(2λ³).
- So **D(η_λ) ≤ ‖Q₁″‖_∞/(12λ³)**.
- NUMERICAL ([1] of `checks/check_spectral_sg.out`, with η₁² = cos²(πu/2), C¹ only, which is enough for the
  illustration): λ³D(η_λ) → 0.2054.

**Consistency.** At support λ = ½ the bracket 1 + D is Lamzouri's C_η, and 2 − C_η > 0 is his 67%-type bound.
- The cos² η gives 1 + D = 1.7067 at λ = ½.
- Lamzouri optimizes η to get C_MT = 1.3275.

## 2. Lemma G (spectral small-gap lemma; deterministic) — PROVED

**Setting.**
- Z is a finite multiset of complex numbers, invariant under complex conjugation (mult(z̄) = mult(z)).
- N := |Z| counts with multiplicity. N_d is the number of distinct elements. N₁ is the number of simple real
  elements.
- η is real, even, in L², with supp η ⊂ (−λ, λ) and ∫η² = 1; K := (η²)^.
- S := Σ_{z,s∈Z}K(z − s)².

**Lemma G.** S is real and E := S − 2N + N_d ≥ 0. Moreover, for 0 < δ ≤ 1/(4πλ),

  #{consecutive pairs x < x′ of simple real elements of Z with x′ − x < δ} ≤ 4(4E + N_d − N₁).

(Consecutive is taken in the ordered list of simple real elements.)

*Proof.*

**Step 1 (a real operator).**
- H_ℝ := {Φ ∈ L²(−λ, λ) : Φ(−u) = conj Φ(u)} is a real Hilbert space. ⟨Φ₁, Φ₂⟩ = ∫Φ₁Φ̄₂ is real on it (Lamzouri
  (2.15)), and H_ℝ ⊕ iH_ℝ = L²(−λ, λ).
- With f_z(u) := η(u)e^{−2πiuz}: for real x, f_x ∈ H_ℝ. For non-real z, g_z := (f_z + f_z̄)/2 and
  h_z := (f_z − f_z̄)/(2i) lie in H_ℝ. (Lamzouri (2.8), (2.14), read.)
- Write Z = {x with mult m_x} ∪ {z, z̄ with mult m_z}, with Im z > 0. Define the real self-adjoint finite-rank operator

    A := Σ_x m_x f_x⊗f_x + 2Σ_z m_z(g_z⊗g_z − h_z⊗h_z),  where (v⊗v)Φ := ⟨Φ, v⟩v.

- Lamzouri's (2.10)–(2.13) and (2.21) (read) give:
  - **tr A = N**, from ‖f_x‖² = 1 and ‖g_z‖² − ‖h_z‖² = 1;
  - **‖A‖²_HS = S**, from S = ∫∫|F(u, v)|²du dv with F(u, v) = Σ_{z∈Z}f_z(u)f_z(v).
- The HS norm on H_ℝ equals that on L², since a real orthonormal basis of H_ℝ is a complex orthonormal basis of L².
- So S is real and ≥ 0.

**Step 2 (spectrum on W).**
- W := span{f_x, g_z, h_z} has dimension N_d. These vectors are linearly independent (Lamzouri, read).
- A = VJVᵀ with V injective and J = diag(m_x, 2m_z, −2m_z) invertible, so A|_W has N_d nonzero real eigenvalues μ_i,
  and A = 0 on W^⊥.
- Hence Σ_i(μ_i − 1)² = Σμ_i² − 2Σμ_i + N_d = S − 2N + N_d = E ≥ 0.
- So #{i : |μ_i − 1| ≥ ½} ≤ 4E.

**Step 3 (restriction to simple real elements).**
- A₁ := Σ_{x simple real} f_x⊗f_x satisfies rank(A − A₁) ≤ N_d − N₁.
- For self-adjoint operators on W differing by rank ≤ ρ, eigenvalue counts in any half-line differ by ≤ ρ (Weyl
  interlacing). In any interval they differ by ≤ 2ρ.
- A₁|_W has the eigenvalue 0 with multiplicity N_d − N₁. Its nonzero eigenvalues are those of the Gram matrix
  G₁ := [K(x − y)]_{x,y simple real}, which is positive definite.
- Hence #{spec G₁ ∉ (½, 3/2)} ≤ 4E + 2(N_d − N₁) − (N_d − N₁) = 4E + (N_d − N₁).

**Step 4 (near pairs give small eigenvalues).**
- For real ξ, 1 − K(ξ) = ∫η²(u)(1 − cos 2πuξ)du ≤ 2π²λ²ξ². So |x − y| < δ ≤ 1/(4πλ) gives 1 − K(x − y) ≤ 1/8 =: τ.
- Let P be a set of p disjoint close consecutive pairs. The unit vectors w_{xy} := (e_x − e_y)/√2 are orthonormal.
- The compression C := WᵀG₁W (p × p) is positive semidefinite, with diagonal entries 1 − K(x − y) ≤ τ, so tr C ≤ pτ.
- At least ⌈p/2⌉ eigenvalues of C are ≤ 2τ = ¼. By Cauchy–Poincaré interlacing, G₁ has ≥ ⌈p/2⌉ eigenvalues ≤ ¼.
- So p ≤ 2(4E + N_d − N₁).
- Close consecutive pairs form chains. A chain with ℓ links contains ⌈ℓ/2⌉ disjoint links, so the total count is
  ≤ 2p_max. ∎

**NUMERICAL** (`checks/check_spectral_sg.py` → `.out`).
- [2] On synthetic multisets (Poisson, GUE-like, clustered; with off-line conjugate pairs and doubled points), tr A = N
  and tr A² = S hold to roundoff via eig(J·Gram). Im S = 0, and Lemma G holds in all 27 cases.
- [3b] GUE-like + m injected near-pairs: each pair produces exactly one Gram eigenvalue ≤ ¼ and adds ≈ 2 to S − N, as
  in the proof.

## 3. Theorem S — PROVED-mod-cite ((C3) (3.1)–(3.2), (C6) Prop 2.1 (2.4) and §3 algebra, (C1)) + mod-input SPC_ℂ⁺, Theorem H

**Theorem S.** Assume SPC_ℂ⁺. Then:
- (a) N^{s,crit}(T) = N(T)(1 + o(1)): almost all zeros are simple and on the critical line.
- (b) There is an absolute C such that for 0 < δ ≤ δ₀, the normalized gaps g_k of PROOF.md §4 satisfy
  limsup_K K⁻¹#{k ≤ K : g_k < δ} ≤ Cδ³.
- (c) (SG) holds. Hence log D_n(σ) = Φ_n + o(n²): G3′ holds for the true zeros.

*Proof.* Apply §1–§2 to Z := {i(ρ − ½)L : ρ ∈ Z(T)}, so that z − s = i(ρ − ρ′)L and S = S_T.
- ρ ↦ 1 − ρ̄ (the functional equation plus conjugation) preserves γ and maps i(ρ − ½)L to its conjugate. So Z is
  conjugation-invariant, its real elements are the critical zeros (z = −γL), and N = N_T.
- By Lemma PC, S ≤ N(1 + D) + o(N) with D := D(η_λ).

(a)
- Lamzouri (2.4) (read) gives N₁ ≥ 2N − S ≥ N(1 − D) − o(N).
- Let λ → ∞ after T → ∞, using D(η_λ) ≤ c/λ³.

(b)
- Fix δ. Let λ := 1/(8πδ), so that 2δ ≤ 1/(4πλ).
- E = S − 2N + N_d ≤ ND + o(N), since N_d ≤ N.
- N_d − N₁ ≤ N − N₁ ≤ S − N ≤ ND + o(N).
- Lemma G at gap 2δ: consecutive critical simple zeros with (γ′ − γ)L < 2δ number ≤ 4(4 + 1)ND + o(N).
- Consecutive pairs (with multiplicity, all zeros) with an endpoint not simple-critical, including every repeat
  (g_k = 0), number ≤ 2(N − N₁) ≤ 2ND + o(N).
- For γ ∈ (T, 2T], log(γ/2π)/2π = L(1 + O(1/log T)), so g_k < δ implies (γ_{k+1} − γ_k)L < 2δ for large T.
- Per dyadic block this gives ≤ 22D(η_λ)N_T + o(N_T) ≤ (22·‖Q₁″‖_∞(8π)³/12)δ³N_T + o(N_T).
- Sum over the dyadic blocks (T/2^j, T/2^{j−1}] with j ≤ log₂R. The rest, γ ≤ T/R, has ≤ (1/R + o(1))N(T) indices.
  Index K and height T correspond via (C1), as in Theorem C's proof.

(c)
- (b) gives (SG): given η, take δ with Cδ³ ≤ η/2.
- Then G3′-L (§4, mod Theorem H) and G3′-U (§3) give the law. ∎

**Remarks.**
- **S1 (only the upper half).** (SG) is an *upper* bound on small-gap counts, and Theorem S uses only the *upper* half
  of SPC on [1, 2λ].
  - For a given (SG) tolerance η it uses only the bounded range [1, M(η)], with M(η) ≍ η^{−1/3}.
  - Compare Theorem C (two-sided PCC, all ranges) and Corollary P (RH + two-sided (V)).
- **S2 (the δ³ rate).** The rate matches GUE repulsion: Theorem C gives (8π²/9)δ³ from PCC, and the numerics in §9.4
  show δ³.
- **S3 (why no zero-density is needed).** Off-line zeros enter Lemma G only through E and N_d − N₁. Lemma PC bounds
  these *exactly*, because the Fourier identity (0.1) holds for complex arguments.
  - The large kernel values |K(z − s)| ~ T^{λ|β−β′|} (the first draft's obstruction) are never estimated
    individually.
  - Lamzouri's Hilbert-space positivity absorbs them.
- **S4 (scope).** Theorem S does not prove G3′ unconditionally. SPC_ℂ⁺ for M > 1 is open, as is two-sided SPC on RH.
  - What is new (novelty UNCHECKED) is that **neither RH nor the lower half of SPC is needed**.
  - The zero-side hypothesis is the BGST-weighted, RH-free quantity, used only as an upper bound.

## 4. Open: does SPC_ℂ⁺ imply RH? (HEURISTIC; not attempted rigorously)

**Heuristic.**
- A single off-line pair at δ_ρ = c > 0, isolated from other off-line zeros, makes ‖g_z‖², ‖h_z‖² ≍ K(2icL) =
  ∫η²e^{4πucL}, which is ≍ T^{2cλ} up to factors in λ.
- So A gets eigenvalues of size ±T^{2cλ}, and S ≥ T^{4cλ}·(const), which contradicts Lemma PC once 4cλ > 1. The
  numerics [2] at λ = 2 show this blow-up (S/N up to 4·10³ with off-line height 0.5).
- Making this rigorous for *many*, possibly clustered, off-line zeros needs a lower bound for Σ_j α_j² on Lamzouri's
  third range D_V < j ≤ D_W. This means controlling ‖P_{V^⊥}h_z‖, i.e. how far h_z lies from the span of the other
  vectors.

**Status.**
- If SPC_ℂ⁺ ⇒ "no zeros with β ≥ ½ + c" for each c > 0, the RH-free gain of Theorem S would be formal, as with (V)
  (C8 fn 6).
- Even then, S4 (one-sided, bounded range) stands.
- Open; recorded for a future plan.

## 5. Superseded first-draft route (for the record)

The first draft tried to:
- restrict Goldston's Theorem-4 Fourier argument to critical–critical pairs;
- bound off-line contributions through a local zero-density "Lemma A′": Σ_{β≠½}T^{2M|β−½|}n(ρ) = o(N_T).

Selberg-type density (exponent ¼ in u = (β − ½)log T) cannot beat T^{2M|β−½|} for M ≥ ⅛, so that route stalled.
Lemma G replaces it.

## 6. (Q1) after Theorem S (HEURISTIC remark)

- On RH, Goldston–Montgomery (C8) link SPC on [1, M] to the prime variance (V) on a corresponding range. A one-sided
  analogue (upper F ⇔ upper variance) would turn Theorem S into "RH + an upper prime-variance bound on a bounded range
  per tolerance ⇒ G3′". That is a weakening of Corollary P's input.
- The one-sided Goldston–Montgomery transfer has not been checked against the source. Not claimed.
