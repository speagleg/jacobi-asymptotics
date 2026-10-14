# Rule R review: Plan 19 (rhfree/RHFREE.md, Theorem S, Lemmas PC and G, numerics)

Reviewer: independent agent, fresh context, adversarial. Date: 2026-10-14. Worktree `ja-plan19`, branch
`plan-19-rhfree`, commit a92b3c4. Scope: rhfree/RHFREE.md (all sections), the Plan-19 parts of
`git diff 1854fe2..HEAD -- CITATIONS.md PROOF.md` ((C3) addendum, (C6) addendum, §9.3 pointer), the plan
docs/superpowers/plans/2026-10-14-plan-19-rhfree.md and its "Review focus", and
rhfree/checks/check_spectral_sg.py/.out. Read first: AGENTS.md; PROOF.md §1, §4 ((SG), G3′-L), §8.2 (Theorem C).

Sources checked against the text extractions (treated as data):
- Lamzouri arXiv:2609.02882v2: Prop. 2.1 statement, the full proof (2.8)–(2.25), §3 Lemma 3.1, Lemma 3.2 and its
  proof through (3.3).
- BGST arXiv:2501.14545v3: §2.1 (multiset convention, definition of Z(T)), §3 (3.1), MT (3.2), the window and
  correction remarks, footnote 2, Lemma 1 (3.6)/(3.7) and the start of the proof of (3.2).

Scratch work (scratchpad `p19rev/adv.py`, `.venv` python, outside the repo):
- (i) A quadrature check that the integral kernel of A is F(u, −v), and that ∫∫|F|² = S = ‖A‖²_HS for a multiset with a
  doubled real point and three off-line pairs. The kernel error is 3·10⁻¹⁴, and the quadrature agrees with S to 10 digits.
- (ii) An adversarial random search over 3000 configurations (clustered, perturbed-lattice and paired; λ ∈ {½, 1, 2, 4};
  0–3 off-line pairs near the axis) for violations of Lemma G or of E ≥ 0. None was found. The worst ratio
  small/rhs is 0.032 (about 1/32). This matches the proof: each near pair adds about 2 to E, and the bound charges
  4·4·2 = 32 per pair.
- (iii) The repo script was re-run: the output is byte-identical to `check_spectral_sg.out`. Wall time is 7 s, not the
  2–4 min stated in the brief.

## Verdict: ACCEPT WITH FIXES

**Mathematics.** I found no mathematical error. I checked every step listed in the brief and could not construct a
counterexample.
- **Lemma PC.** The weight removal is exact for any support. The |α| ≤ 1 term, the one-sided step and the bracket
  algebra are all correct.
- **Lemma G.** The real structure and the identities tr A = N and ‖A‖²_HS = S are correct. So are the Weyl and Cauchy
  bookkeeping, the chain factor and the constant 4(4E + N_d − N₁).
- **Theorem S.** The translation to (SG) is correct, including repeats, off-line ordinates, the normalization and the
  dyadic summation.

**What must change before REVIEWED.** The findings are minor or nit, in four groups:
- framing and wording: F1, F2, F7;
- making Lemma G independent of the lossy extraction of Lamzouri's conjugation bars: F3;
- Rule C bookkeeping: F4, F5, F6;
- process: F8.

There is no major finding.

## Checked and OK (details)

### Lemma PC

**Weight removal.**
- (Q″)^(z) = (2πiz)²Q̂(z) = −4π²z²K(z)², so r̂_T = (1 + π²z²/log²T)K².
- At z = i(ρ − ρ′)L with L = log T/2π: z² = −(ρ − ρ′)²log²T/4π², so π²z²/log²T = −(ρ − ρ′)²/4 and the factor is
  (4 − (ρ − ρ′)²)/4 = 1/W(ρ − ρ′).
- W has no pole, because |Re(ρ − ρ′)| < 1.
- Nothing here uses supp Q ⊂ [−1, 1]. This agrees with the source (Lamzouri §3, between (3.2) and (3.3), as quoted in
  the (C6) addendum).

**Fourier identity (0.1).**
- −2πiα·i(ρ − ρ′)L = α(ρ − ρ′)log T, so f̂(i(ρ − ρ′)L) = ∫f(α)T^{α(ρ−ρ′)}dα.
- The sums are finite, so the exchange is trivial.
- For α < 0 the identity uses F(T^α, T) itself. Evenness follows from MT's F(x) = F(1/x), or directly from ρ ↔ ρ′ and
  W being even.

**Normalization.**
- N_T = N(2T) − N(T) = (T/2π)(log T + 2 log 2 − 1 − log 2π + O(log T/T)) = (T/2π)log T(1 + O(1/log T)), by (C1).
- This matches MT's window T < γ, γ′ ≤ 2T, which BGST v3 states explicitly ("the sum F(x, T) above is taken over zeros
  satisfying T < γ, γ′ ≤ 2T").

**|α| ≤ 1.**
- Dividing (3.2) by N_T gives 𝓕(α) = log T·T^{−2α}(1 + O(1/√log T)) + α(1 + O(1/log T)) + O(1/√log T).
- The substitution v = α log T gives ∫_0^1 Q log T·T^{−2α} = Q(0)/2 + O(‖Q′‖_∞/log T). The O(1/√log T)-relative part
  of the spike integrates to O(1/√log T).
- So ∫_{−1}^1 Q𝓕 = Q(0) + 2∫_0^1 αQ + O(1/√log T). This is correct, and needs MT only on 1 ≤ x ≤ T.

**One-sided step.**
- Q = η² ∗ η² ≥ 0 automatically, since η² ≥ 0, so SPC_ℂ⁺ is used only where the weight is nonnegative.
- 𝓕 ≥ 0 (MT) is needed in exactly one place: |∫Q″𝓕| on 1 ≤ |α| ≤ 2λ, where SPC_ℂ⁺ bounds 𝓕 above and positivity
  bounds it below. On |α| ≤ 1 MT bounds |𝓕| directly. This is used correctly.

**Bracket.**
- 2∫_1^∞Q = 1 − 2∫_0^1Q, which gives Q(0) + 1 − 2∫_0^1(1 − α)Q = 1 + D.
- D ≥ 0 by Bochner, since Q̂ = K² ≥ 0 on ℝ.
- Sharpness: under PCC, S/N → 1 + ∫K² − ∫K²sinc² = 1 + D exactly. So Lemma PC is the sharp form.

**Scaling.**
- Q_λ(α) = λ^{−1}Q₁(α/λ), and ‖Q_λ″‖_∞ = λ^{−3}‖Q₁″‖_∞.
- D = 2∫_0^1(1 − α)(Q(0) − Q(α)) ≤ (‖Q₁″‖_∞/λ³)∫_0^1(1 − α)α² = ‖Q₁″‖_∞/(12λ³).
- The numerical limit 0.2054 matches −Q₁″(0)/12 = ∫((η₁²)′)²/12 = (π²/4)/12 = 0.2056.

**Consistency with Lamzouri.**
- At λ = ½, supp Q ⊂ [−1, 1], so 1 + D = Q(0) + 2∫_0^1 αQ, which is Lamzouri's main-term bracket.
- (2.4) then gives N₁ ≥ (2 − C_η)N. This is correct.

### Lemma G

**Real structure.**
- conj f_z(u) = f_{z̄}(−u). From this, g_z = (f_z + f_{z̄})/2 and h_z = (f_z − f_{z̄})/(2i) satisfy
  Φ(−u) = conj Φ(u).
- These are the only readings consistent with "g_z = g_{z̄}, h_z = −h_{z̄}, f_z = g_z + ih_z" in the extraction. The
  other candidate, (f_z + conj f_z)/2, fails g_z = g_{z̄}. So the reconstruction noted in the (C6) addendum is forced.
- A real orthonormal basis of H_ℝ is a complex orthonormal basis of L², since Φ = Φ_+ + iΦ_− with
  Φ_± ∈ H_ℝ.

**Pair identity.**
- f_z ⊗ f_{z̄} + f_{z̄} ⊗ f_z = 2(g ⊗ g − h ⊗ h), with the convention (v ⊗ v)Φ = ⟨Φ, v⟩v. I expanded this with the
  conjugate-linear slot.
- So A = Σ_{z∈Z} f_z ⊗ f_{z̄}: the operator Φ ↦ Σ_z⟨Φ, f_{z̄}⟩f_z.

**Kernel and HS norm.**
- The integral kernel of A is Σ_z f_z(u)conj f_{z̄}(v) = Σ_z f_z(u)f_z(−v) = F(u, −v). Lamzouri's F(u, v) = Σ f_z(u)f_z(v)
  is a *bilinear* (unconjugated) sum (2.13).
- Hence ‖A‖²_HS = ∫∫|F(u, −v)|² = ∫∫|F|² = S by (2.12).
- (2.12) itself follows from K(z − s) = ⟨f_z, f_{s̄}⟩ and the reindexing s → s̄. Verified by quadrature, scratch (i).
- The text does not mention the reflection v ↦ −v. See F3.

**Trace.** tr A = Σm_x‖f_x‖² + 2Σm_z(‖g_z‖² − ‖h_z‖²) = N. This uses ⟨f_z, f_{z̄}⟩ = K(0) = 1, which gives
‖g‖² − ‖h‖² = 1 and ⟨g, h⟩ = 0.

**Spectrum on W.**
- A = VJV* with V: ℂ^{N_d} → W a bijection, so V* is injective on W.
- Hence A|_W is invertible, self-adjoint and has N_d real nonzero eigenvalues, and A = 0 on W^⊥.
- Σ(μ − 1)² = E. Each |μ − 1| ≥ ½ costs ≥ ¼, so there are ≤ 4E of them.

**Step 3.**
- A − A₁ has rank ≤ r + 2k = N_d − N₁.
- The Weyl / finite-rank interlacing bound |n_X(t) − n_Y(t)| ≤ rank holds for every half-line, open or closed. Hence
  ≤ 2·rank for an interval, and for its complement.
- A₁|_W has the eigenvalue 0 with multiplicity exactly N_d − N₁, because the f_x are independent and rank A₁ = N₁. These
  eigenvalues lie outside (½, 3/2).
- The nonzero spectrum of A₁ = V₁V₁* equals that of V₁*V₁ = [⟨f_y, f_x⟩] = [K(x − y)] = G₁, which is real symmetric and
  positive definite.
- Result: ≤ 4E + 2(N_d − N₁) − (N_d − N₁). Correct.

**Step 4.**
- 1 − K(ξ) ≤ 2π²λ²ξ² gives ≤ 1/8 for |ξ| < 1/(4πλ).
- The w_{xy} for disjoint pairs are orthonormal, and C_{ii} = 1 − K(x − y).
- If m eigenvalues of C exceed 2τ, then 2τm < tr C ≤ pτ, so m < p/2 and at least ⌈p/2⌉ eigenvalues are ≤ 2τ. Cauchy
  interlacing (λ_k(G₁) ≤ λ_k(C)) transfers this to G₁.
- The chain factor holds: a chain of ℓ links contains ⌈ℓ/2⌉ ≥ ℓ/2 disjoint links.
- The constant 4(4E + N_d − N₁) is correct, if loose by about 30× (scratch (ii)).

### Theorem S

**The map.**
- i(ρ − ½)L = −γL + iδ_ρL. It is real exactly at critical zeros.
- ρ ↦ 1 − ρ̄ is a multiplicity-preserving involution of Z(T), and it conjugates the image. The map is injective, and
  N = N_T. BGST's Z(T) is the *multiset* T < γ ≤ 2T (BGST §2.1; see F4).

**Inequalities.** E ≤ ND + o(N) uses N_d ≤ N. N_d − N₁ ≤ N − N₁ ≤ S − N is (2.4).

**Translation to g_k.**
- Index the consecutive pairs (γ_k, γ_{k+1}) of the full ordinate list, with multiplicity.
- **Case 1: both endpoints are simple critical zeros.** They have distinct ordinates and are consecutive in the
  sublist. So they are among Lemma G's pairs; the order reversal γ ↦ −γL is harmless.
- **Case 2: otherwise.** An endpoint is a multiple zero or an off-line zero. This covers every repeat g_k = 0 and every
  off-line ordinate, and there are ≤ 2(N − N₁) such indices.
- The normalization log(γ_k/2π)/2π ≥ (log T − log 2π)/2π gives g_k < δ ⇒ (γ_{k+1} − γ_k)L < 2δ.
- Boundary pairs that straddle blocks are O(1) per block and are omitted harmlessly. Say so (F6).

**Constant.** 4(4 + 1) + 2 = 22, and λ = 1/(8πδ) gives D ≤ ‖Q₁″‖_∞(8πδ)³/12. So δ³ is correct.

**Dyadic summation.** Finitely many blocks for fixed R, each with an o(N) error, plus the 1/R tail, with K ↔ T via
(C1). This mirrors Theorem C's proof, and it yields (SG) in PROOF.md §4's exact form.

**(c).** (SG) feeds G3′-L (mod Theorem H) and G3′-U, exactly as in Theorem C.

**RH and two-sided use.**
- I found no hidden use of RH or of the lower half of SPC.
- The only zero-location facts used are the functional equation (conjugation invariance) and MT, which is unconditional.
- The upper half of SPC is used only on [1, 2λ].

### Numerics

- The output reproduces exactly.
- tr A − N and tr A² − S are at roundoff in all 27 rows (up to 1.7·10⁻⁹ absolute when S ~ 10⁵, i.e. relative 10⁻¹⁴).
- The "[3b] each pair adds ≈ 2 to S − N" claim matches the printed increments: 2.0, 2.0, 2.2, 2.07 per pair.
- cond(G) reaches 7·10¹⁷ in several [2] rows. The trace identities are insensitive to this, because the sqrt-Gram
  route has no inversion. The outG1 counts in those rows are less reliable. Nit N2.

## Findings

**F1 (minor; RHFREE §0 "Hypothesis SPC_ℂ⁺", second bullet; S1/S4).**
- **Issue.** The text says "On RH, SPC_ℂ⁺ is the upper half of Montgomery's strong pair correlation." This is imprecise.
  - Goldston's SPC (C8 (6.6)) is for the full window 0 < γ, γ′ ≤ T. SPC_ℂ⁺ is dyadic, T < γ, γ′ ≤ 2T, normalized by N_T.
  - On RH, two-sided full-window SPC does imply two-sided dyadic SPC. The cross-window pairs contribute
    Σ_{γ≤T<γ′}w(γ − γ′) = O(log³T) = o(N_T), and the change T^α ↔ (2T)^{α′} is handled by uniformity plus MT near α = 1.
  - So SPC_ℂ⁺ is implied by Goldston's SPC on RH.
  - But the *upper half* of the full-window version does **not** obviously give the dyadic upper half.
    F_{(T,2T]} = F_{(0,2T]} − F_{(0,T]} + O(log³T) needs a *lower* bound on F_{(0,T]}. Only F ≥ 0 is available, which gives
    ≤ 2N_T.
  - The converse direction (dyadic upper ⇒ full-window upper) does work, by summing blocks.
- **Fix.** Replace the sentence with: "On RH, two-sided SPC (C8 (6.6)) implies SPC_ℂ⁺ (cross-window terms O(log³T)), and
  SPC_ℂ⁺ at all heights implies the upper half of the full-window statement. The converse is not claimed." Then either
  add the three-line cross-term bound or mark it as a remark. Adjust S4's "neither … the lower half of SPC is needed"
  to "only the upper half of the *dyadic* SPC is needed".

**F2 (minor; RHFREE §4 title and "Status").**
- **Issue 1.** The title "does SPC_ℂ⁺ imply RH?" overstates what the heuristic would give. Made rigorous, the heuristic
  yields S ≥ c·T^{4cλ} against S ≪ T log T. For each fixed c > 0 that excludes zeros with |β − ½| ≥ c for T ≥ T₀(c),
  i.e. max_{T<γ≤2T}|β − ½| → 0. That is **not** RH.
- **Issue 2.** The Status bullet says that in that case "the RH-free gain of Theorem S would be formal, as with (V)
  (C8 fn 6)". This is wrong as stated. (V) implies RH outright. A "zeros approach the line" consequence would leave
  Theorem S's RH-freeness genuine.
- **Fix.**
  - Retitle: "Open: what does SPC_ℂ⁺ force about horizontal positions? (HEURISTIC)".
  - Say the heuristic, if made rigorous, gives sup_{T<γ≤2T}|β − ½| → 0, not RH.
  - Delete or qualify "would be formal". Only an implication SPC_ℂ⁺ ⇒ RH would make the RH-free gain formal, and that
    is not suggested by the heuristic.
  - Keep HEURISTIC/OPEN. The phrase "off-line height 0.5" refers to synthetic units, Im z = δ_ρL; say so.
  - AGENTS.md rule 3: §4 makes no claim about RH. Keep it phrased purely as an open implication question.

**F3 (minor; Lemma G Step 1, the "‖A‖²_HS = S" and "tr A = N" bullets; CITATIONS (C6) addendum note).**
- **Issue 1.** The step reads "from S = ∫∫|F(u, v)|² with F(u, v) = Σ f_z(u)f_z(v)". F is bilinear, not the operator
  kernel. The kernel of A is F(u, −v), and the equality needs this reflection, using conj Φ(v) = Φ(−v) on H_ℝ. As
  written, a reader could take F for the kernel.
- **Issue 2.** The step leans on an extraction that loses conjugation bars, as the addendum admits. The identities are
  three-line computations, so the lemma does not need the source at all.
- **Fix.** Make Step 1 self-contained:
  - (a) K(z − s) = ⟨f_z, f_{s̄}⟩, by direct integration;
  - (b) f_z ⊗ f_{z̄} + f_{z̄} ⊗ f_z = 2(g_z ⊗ g_z − h_z ⊗ h_z), hence A = Σ_{z∈Z} f_z ⊗ f_{z̄};
  - (c) tr A = Σ_z⟨f_z, f_{z̄}⟩ = N·K(0) = N;
  - (d) A is self-adjoint, so ‖A‖²_HS = tr(A²) = Σ_{z,s}⟨f_s, f_{z̄}⟩⟨f_z, f_{s̄}⟩ = Σ_{z,s}K(s − z)K(z − s) = S, using
    K even. No kernel or F is needed. Alternatively, note that the kernel of A is F(u, −v);
  - (e) linear independence of the exponentials e^{−2πiuz} for distinct z on a set of positive measure.
- **Label.** Lemma G then needs no citation, and the label **PROVED** is justified. Otherwise it must read PROVED-mod-cite
  (C6). Also write V* in place of Vᵀ in Step 2. It is the same matrix only because the Gram is real; say so.

**F4 (minor; CITATIONS (C3) Plan 19 addendum; Rule C).**
- **Issue.** Lemma G and Theorem S need Z(T) to be the *multiset* (with multiplicity) of zeros with T < γ ≤ 2T. The
  addendum quotes only the window. Lemma PC also uses MT's evenness F(x, T) = F(1/x, T); that is in the quote, but the
  "Used in" line omits it.
- **Fix.** Add the BGST §2.1 quote "Let Z(T) denote the multiset of those ρ ∈ Z for which T < γ ≤ 2T". Extend "Used in"
  to "MT on |α| ≤ 1; F ≥ 0; F(x) = F(1/x); multiset convention (Lemma G, Theorem S)".

**F5 (minor; RHFREE §1 Step 3 "cf. BGSTB24 Lemma 5 = Lamzouri Lemma 3.1, whose statement this reproduces").**
- **Issue.** Lamzouri Lemma 3.1 = BGSTB24 Lemma 5 is stated for 0 < γ, γ′ ≤ T and supp f ⊂ [−1, 1], with the
  normalization (T/2π)log T. The computation here is for the dyadic window and uses MT (3.2) directly. It is an
  analogue, not a reproduction.
- **Rule C.** Nothing relies on the unread proof of BGSTB24 Lemma 5, and footnote 2 is only context. That is
  acceptable, provided the wording does not suggest otherwise.
- **Fix.** Write "the dyadic analogue of Lamzouri Lemma 3.1 (= BGSTB24 Lemma 5, stated there for 0 < γ, γ′ ≤ T);
  derived here directly from MT (3.2); the proof of BGSTB24 Lemma 5 is not used".

**F6 (nit; Theorem S proof (b)).** Several small gaps in the write-up:
- (i) Pairs (γ_k, γ_{k+1}) with γ_k in a block and γ_{k+1} in the next one are not covered by the per-block count. There
  are O(1) per block, so the effect is negligible, but it should be said.
- (ii) "for 0 < δ ≤ δ₀": δ₀ is never defined. The bound holds for every δ > 0, trivially once Cδ³ ≥ 1. Drop δ₀.
- (iii) Say explicitly that a consecutive pair in the full list with both endpoints simple critical is consecutive in
  the simple-critical sublist, because two distinct simple critical zeros have distinct ordinates.
- (iv) Note that (a) is not needed for (c).

**F7 (nit; RHFREE header "Answer obtained here: Yes", §3 S4, plan; framing).**
- **Issue.** "Yes" answers (Q2) only conditionally.
- **Fix.** Write "Yes, conditionally: the one-sided dyadic hypothesis SPC_ℂ⁺ implies (SG) without assuming RH." Keep
  "novelty: UNCHECKED" everywhere, as now. S2's "rate matches GUE repulsion" is a remark and should stay unlabelled as
  a result.

**F8 (minor, process; research/G3prime/LOG.md; AGENTS.md rule 6).**
- **Issue 1.** There is no Plan 19 entry in LOG.md and no recorded Rule A pass for Lemma PC, Lemma G or Theorem S.
- **Issue 2.** Plan 17's recorded Rule A ruling reads: "Pairs of off-line zeros make BGST's complex-weighted pair sums
  indefinite. This rules out counting close pairs among critical zeros via Lamzouri's Hilbert-space identity." Lemma G
  does exactly that, through the spectrum rather than term positivity. The reversal should be logged.
- **Issue 3.** The Lemma A′ stall (a stop-condition-type finding) is recorded only in RHFREE §5.
- **Fix.** Add a LOG.md Plan 19 entry with:
  - the Rule A pass;
  - the Lemma A′ stall;
  - the explicit note that Lemma G supersedes the Plan 17 ruling.

**N1 (nit; RHFREE §5).**
- **Issue.** "Selberg-type density (exponent ¼ in u = (β − ½)log T)" states an external theorem that is not in
  CITATIONS.md. It is not used, but Rule C covers stated external facts.
- **Fix.** Mark it "(recollection; not cited, not used)", or quote a read source.

**N2 (nit; numerics [2]).**
- Several rows have cond(G) ≈ 10¹⁶–10¹⁸. The trace identities are robust there, but the outG1 ≤ bnd column is not
  numerically meaningful in those rows. Say so, or drop those rows from that column.
- Also state the run time (7 s here, not minutes) and the seed (19).

**N3 (nit; PROOF.md §0 status table).** Theorem S has no row yet. That is correct while it is NOT REVIEWED. Add a row
when it is promoted, with the label below.

## Recommended labels (after the fixes; then REVIEWED on re-check)

| Item | Label |
|---|---|
| Lemma PC | PROVED-mod-cite ((C3) MT (3.1)–(3.2) incl. multiset Z(T), F ≥ 0, evenness; (C1)) + mod-input SPC_ℂ⁺. (C6) §3 is provenance for the algebra, which is fully re-derived. |
| Lemma G | PROVED (deterministic), once Step 1 is made self-contained (F3). Otherwise PROVED-mod-cite (C6). |
| Theorem S | PROVED-mod-cite ((C3), (C6) (2.4), (C1)) + mod-input SPC_ℂ⁺, Theorem H. Novelty UNCHECKED. The hypothesis is described as "the upper half of the dyadic complex-weighted SPC" (F1). |
| §4 | HEURISTIC / OPEN, retitled per F2. No claim about RH. |
| §6 | HEURISTIC; the one-sided Goldston–Montgomery transfer is UNCHECKED and not claimed (as now). |
| Numerics | NUMERICAL (synthetic multisets; no evidence about zeros). |

## Re-check (fix commit 5f604b2)

Scope: `git diff a92b3c4..5f604b2` for rhfree/RHFREE.md, CITATIONS.md and LOG.md. The numerics script is unchanged.
Working tree clean before this append.

| Finding | Status | Where / note |
|---|---|---|
| F1 | RESOLVED | §0 hypothesis bullets. SPC_ℂ⁺ is described as the upper half of the *dyadic* SPC. The statement "two-sided full-window SPC ⇒ dyadic (cross terms O(log³T)) on RH" is given, and the one-sided transfer is disclaimed. S4 now says "(dyadic) SPC". |
| F2 | RESOLVED | §4 is retitled "does SPC_ℂ⁺ confine the zeros near the line?" and labelled HEURISTIC/OPEN. Status: at most a quasi-RH statement (max\|β − ½\| → 0), *not* RH. The "formal, as with (V)" sentence is removed, and "no claim about RH is made" is stated. |
| F3 | RESOLVED | Step 1 is now self-contained: ⟨f_z, f_w⟩ = K(z − w̄); A = Σ f_z ⊗ f_{z̄} with kernel F(u, −v); the grouping into g/h form; tr A = N; and ‖A‖²_HS = tr A² = Σ K(s − z)K(z − s) = S. I re-derived the last identity: A²Φ = Σ_{z,s}⟨Φ, f_{s̄}⟩⟨f_s, f_{z̄}⟩f_z. Linear independence is via exponentials. V* replaces Vᵀ. The label PROVED is justified. |
| F4 | RESOLVED | (C3) quotes §2.1: "Let Z(T) denote the multiset of those ρ ∈ Z for which T < γ ≤ 2T". This matches the source verbatim. "Used in" is extended (evenness, multiset convention). |
| F5 | RESOLVED | Step 3 is now the "dyadic analogue … derived directly from MT", and it says the proof of BGSTB24 Lemma 5 is not read and not used. |
| F6 | RESOLVED | All four points are covered: boundary pairs O(1) per block; δ₀ dropped ("for every δ > 0"); consecutive-in-sublist stated; (a) not needed for (c). |
| F7 | RESOLVED | The header now reads "Yes, conditionally on SPC_ℂ⁺". Novelty is UNCHECKED throughout. |
| F8 | RESOLVED | LOG.md has a Plan 19 entry covering the inputs read, the Lemma A′ stall (Selberg marked as recollection), the explicit reversal of the Plan 17 Rule A ruling (restricted to upper-bound counting), the Rule A notes and the Rule R outcome. |
| N1 | RESOLVED | §5 adds "from recollection, not cited and not used". |
| N2 | RESOLVED | [2] has the cond(Gram) caveat (the outG1 column is unreliable in those rows; the trace identities and the Lemma G inequality are unaffected). Seed 19 and the ≈ 7 s run time are stated. |
| N3 | DEFERRED | Deferred until promotion, as agreed. |

Residual nits. Neither blocks acceptance; both are cosmetic and can be fixed at promotion.
- **R1.** The RHFREE.md title line and LOG.md say "N1–N3 applied", but N3 is deferred. Write "N1–N2 applied, N3
  deferred to promotion".
- **R2.** RHFREE §2 Step 2 still says "These vectors are linearly independent (Lamzouri, read)". Since Step 1 now proves
  this, write "(Step 1)", so that the PROVED label carries no residual citation.

**Re-check verdict: ACCEPT.** With R1 and R2 applied when the items are promoted, the final labels are:
- **Lemma PC:** PROVED-mod-cite ((C3) MT (3.1)–(3.2) incl. the multiset Z(T), F ≥ 0 and evenness; (C1)) + mod-input
  SPC_ℂ⁺; REVIEWED.
- **Lemma G:** PROVED (deterministic, self-contained); REVIEWED.
- **Theorem S:** PROVED-mod-cite ((C3), (C6) (2.4), (C1)) + mod-input SPC_ℂ⁺ (the upper half of the dyadic
  complex-weighted SPC), Theorem H; REVIEWED; novelty UNCHECKED.
- **§4:** HEURISTIC/OPEN (quasi-RH question); no claim about RH.
- **§6:** HEURISTIC; the one-sided Goldston–Montgomery transfer is UNCHECKED and not claimed.
- **Numerics:** NUMERICAL (synthetic multisets only).
