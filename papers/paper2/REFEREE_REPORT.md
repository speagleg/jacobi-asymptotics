# Referee report: "Recurrence coefficients of discrete measures with power-law atoms and slowly varying weights" (Paper 2 draft, 14 Oct 2026)

Reviewer: AI referee (orthogonal polynomials, RH steepest descent, discrete OPs). This is not an independent human review
(Rule R). Files read in full: main.tex, sec_front, sec_2–sec_8, sec_back, app_a–app_d, NOTES.md. Also read:
research/G1/RH/CITATIONS.md (C–D, KMVV, WLXZ, DLMF entries), research/program/novelty_lineB_A.md §§1–2, the C–D (4.14)
usages in research/G1/RH (zeta/RH_zeta_close.md §1.6 and its review F3, route2/ROUTE2*.md), ROUTE2.md §4 (UR′(b′)).
No source PDF was opened by this referee. All quotations below come from the repository records.

## Recommendation

**Minor revision.** I found no mathematical error in the parts that are new and unreviewed. The new resolvent proof
(App. B), the new assembly order (§4), the direct first-variation and saturation proofs, the recomputed jumps (§5) and the
derived C–D moment formula all check out, and I verified them line by line. One item is **MAJOR** in the sense of
completeness: the soft-edge Airy parametrix (F5)/(6.x eq:airy) is asserted by reference, with branch and sign conventions
left unchecked. Every downstream estimate uses it: App. B's soft-edge block, the circle terms Ξ_k = O(1/n), and therefore
Theorem 4. It is standard and very likely true, but it has to be written out. The other findings are minor: the lens
existence is a one-sentence assertion, a remark about WLXZ's sign is misleading, notation clashes, and citation-registry
hygiene.

## Summary of the paper

For σ = Σ k^{−s}ℓ(k)δ_{k^{−p}} with ℓ slowly varying, the paper proves:

- n^p b_n → c(p) and n^p a_n → 2c(p) (Thm 1(i)).
- A rate O(1/n + ρ_ℓ(⌈n/M₀⌉)) (Thm 1(ii)).
- A rate O(1/n) for analytic ℓ and for pure powers (Thm 1(iii), Thm 2).

The proof chain is:

1. An RH "engine" (Thm 4) on the window |α| < 1, α = (s−1−p)/p. It is a WLXZ-type frame with three outer-scalar
   geometries, and the hard edge is handled by a Conway–Deift comparison with an explicit Bessel/Airy/global parametrix.
2. The Christoffel shift σ ↦ xσ with rate (Thm 3).
3. Gaussian smoothing with first-variation stability (§4).

## Numbered findings

### F1 (MAJOR) — §6 "The soft edge", eq. (airy), Frame Prop. (F5); used in App. B (eq. B-airy-structure) and Prop. 7.7 (Ξ_k)

**Issue.** The Airy parametrix is not constructed. The text takes Ψ_r = "σ₂Ψσ₂ of WLXZ (6.12)" with "sectorial
constants and the branch of ω^{1/2} chosen as there". That construction is written in WLXZ's symmetric variable, with
WLXZ's orientations and scalar data. The following are then asserted without proof:

- (a) P̂_r has exactly the jumps v of (F1) in U(4c, ε). The orientation of Σ_v^± is "away from the axis", while WLXZ
  orient theirs differently.
- (b) A_r = P^∞₀ ω^{−σ₃/2} N_r^{−1} f_r^{σ₃/4} is analytic in U(4c, ε) ("its jumps on the band cancel").
- (c) The expansion Ψ_r(ζ) = ζ^{−σ₃/4}N_r(I + O(ζ^{−3/2}))e^{+(2/3)ζ^{3/2}σ₃}.

On (b): f_r′(4c) > 0 and f_r^{1/4} is principal, so on the band f_{r,+}^{σ₃/4} = f_{r,−}^{σ₃/4}·diag(i, −i). The
cancellation then needs two things:

- ω_+^{1/2}ω_−^{1/2} = 1 for the chosen branch;
- N_r J N_r^{−1} = diag(−i, i).

For comparison, at the hard edge (Lemma 7.2(i)) the analogous identity is M^{−1}JM = diag(i, −i), which I checked. With
N_r = M the soft-edge relation holds; with N_r = M^{−1} it fails.

On (c): conjugating the textbook Airy model by σ₂ turns ζ^{−σ₃/4} into ζ^{+σ₃/4}. So the stated form of the expansion
depends on WLXZ's normalisation of Ψ, which is not quoted in CITATIONS.md: only (6.10)–(6.12) and the jump form (6.4)
are recorded.

The construction is standard, so I expect it to be correct up to conventions. But the paper presents it as proved, and the
following all rest on it:

- (B2)/(B3) at the soft edge (App. B);
- the bound O(1/n) on ∂U(4c, ε) (circle terms Ξ_k);
- Remark 7.9's statement that Ξ_k may depend on ℓ₁.

**Fix.** Write Ψ_r explicitly: Airy functions, the sectors, the jumps with the paper's orientations, and N_r. Verify jump by
jump that P̂_r = A_r n^{σ₃/6}M_{r,n} has the jumps of Lemma 5.8(a), (c), (d) conjugated by D_W^{σ₃}. Prove that A_r is
analytic, including the branch of ω^{1/2}, the relation N_rJN_r^{−1} = diag(−i, i) and removability at 4c. State the
matching P̂_r(P^∞₀)^{−1} = I + O(1/n) with constants uniform in n; this uses Lemma 6.7(vi)(b). Record the WLXZ Airy model
quote, or the DLMF Airy section if the model is rebuilt from DLMF 9.2 and 9.7, in RH/CITATIONS.md.

### F2 (MINOR) — §5.6 "The contour": existence of the lips

**Issue.** The lips outside U(0, δ) need four properties: they are n-independent, they lie in C_± ∩ {|arg z| < ϑ_w}, they
satisfy Re φ̃ > 0 (and Re φ < 0, which is global), and they are connected. Existence rests on one sentence that patches
together Lemma 5.6(ii) (a strip of height y_K over a compact K), (iii) (near 0) and (iv) (near 4c). As stated, (ii) and
(iii) need not overlap:

- (iii) gives Re φ̃ > 0 only where arg z ≳ C|z|^{1/2+1/p};
- y_K in (ii) is not quantified as K approaches 0.

**Fix.** Add a short lemma with an explicit lens. One way: show directly that

Re φ̃(x + iy) ≥ c·y·x^{−1−1/p} for 0 < y ≤ c′x, 0 < x ≤ 4c − h₀/2.

This follows from ∂_y Re φ̃ = π(λ_p − ψ*) ≍ λ_p near 0 and a second-derivative bound on the analytic continuation of g
across (0, 4c). Then take the lip to be the graph y = c″x near 0, joined to the circle |z − 4c| = h₀. Also state that the
lips do not meet the saturated lips Σ^△ except at 4c ± ih₀.

### F3 (MINOR) — §5.7, sentence after (VM): "With the literal product a constant jump −I would appear"

**Issue.** I verified that the paper's choice A^△_− κ_−^{σ₃} in Ω^△_− gives the jump (d). The literal product Π^{−σ₃}V^△_−
equals −κ_−^{σ₃}.

However, WLXZ (4.12) as printed already contains the factor −V^△_−. See the corrected transcription in RH/CITATIONS.md,
"(4.12), as printed": "−V^△₋(z), z ∈ Ω^△_{l,+} ∪ Ω^△_{r,−}". Under z_WLXZ² ↔ x, both Ω_{l,+} and Ω_{r,−} map to C_−. So
WLXZ's minus sign sits exactly in the region the paper calls Ω^△_−.

The sentence (and the task description's "sign −1 discrepancy") suggests an error in WLXZ, whereas WLXZ handle it in
(4.12). Ignoring (4.12)'s minus sign gives −I.

**Fix.** Rephrase: "the factor in Ω^△_− is −Π^{−σ₃}V^△_−, the sign being that of −V^△_− in [WLXZ, (4.12)]". A human should
confirm the region correspondence against WLXZ Fig. 3.

### F4 (MINOR) — §2.5 T3(b), eq. (CD-moments) vs C–D (4.14)

**Issue.** C–D (4.14) as recorded reads "Q₁ − Q̃₁ = −∫_Σ µ(v_Σ − ṽ_Σ)µ̃^{−1} đz", with no ṽ^{−1}.

The paper's derived formula, with H = A_−(v_A − v_B)v_B^{−1}B_−^{−1}, is the correct consequence of C–D Thm 4.4, because
v_Av_B^{−1} − I = (v_A − v_B)v_B^{−1}. I verified both moment identities, including the second-moment correction
+(A₁ − B₁)B₁.

The two forms agree only when (v − ṽ)ṽ^{−1} = v − ṽ:

- On the lips this holds, since e₁ᵀṽ^{−1} = e₁ᵀ for lower-triangular ṽ.
- On the new circles Σ_∘ it does not: (ṽ^{−1} − I) vs (I − ṽ) differ by O(n^{−2}). This is harmless but not zero.

**No REVIEWED repo proof used the defective form.** All of the following use h = µ(v − ṽ)ṽ^{−1}µ̃^{−1}:

- RH_ζ_close §1.6, after Rule R F3 of REVIEW_RHzeta_close;
- ROUTE2 D′;
- ROUTE2_p1 D₁;
- ROUTE2_bnd Dᶠ, ROUTE2_plt1 D′_{<1} and ROUTE2_xframe1, each "D′ verbatim".

The grep over research/G1 finds no other use. PROOF.md §§3.16–3.23 do not invoke (4.14).

**Fix.** Add one sentence to T3(b): "(4.14) of [CD] is printed without v_B^{−1}; it agrees with the identity above when
(v_A − v_B)v_B^{−1} = v_A − v_B, as in their setting. We use the form derived from Theorem 4.4."

### F5 (MINOR) — Citation registry (Rule C)

**Issue.**

- The quotations of Dai–Piao–Qiao (Prop. 2.1), Derevyagin–Derkach (§1) and Deift–Piorkowski (§1, "requires a different
  proof … Muckenhoupt weights") are recorded only in research/program/novelty_lineB_A.md and novelty_lineB_B.md. They are
  not in research/G1/CITATIONS.md or RH/CITATIONS.md.
- DPQ's proof was read only through a summarising tool. The paper uses DPQ only as attribution and proves Lemma 3.3
  itself, so this is acceptable.
- The DPQ hypotheses match the paper's use. Their chain sequence is a_n = g_n(1 − g_{n−1}) with 0 ≤ g_n ≤ 1, and
  Prop. 2.1 states "lim a_n = 1/4 ⇒ lim g_n = 1/2". The paper's 𝖺_n = (1 − 𝗆_{n−1})𝗆_n with 𝗆_0 = 0 has this form, and
  I checked the identity 𝖺_n = κ_n b̂_n²/(â_{n−1}â_n).
- WLXZ's Airy model normalisation is not recorded (see F1).

**Fix.** Copy these entries into the citation registry before submission. This is already on NOTES §7's checklist.

### F6 (MINOR) — Lemma 5.6(iv), sign statement near the soft edge

**Issue.** "Re φ̃ > 0 on {π/3 < |arg(z − 4c)| < π}" is derived from arg f_r^{3/2} = (3/2)arg(z − 4c) + o(1). Near the
boundary rays this holds only up to the o(1) correction. Near arg = π, i.e. near the band, Re φ̃ → 0.

**Fix.** State the sign region as {π/3 < |arg f_r(z)| < π}, or as a subsector {π/3 + δ₁ ≤ |arg| ≤ π − δ₁} together with
the band neighbourhood from (ii). Only Σ_v (arg = π/2) and (4c, 4c + ε) (arg 0) are used, so nothing downstream changes.

### F7 (MINOR) — App. B, Step 2 (density/extension argument)

**Issue.** The map f ↦ µ = m_− + f on 𝒟 must be linear before it can be extended. Linearity follows from uniqueness (R2),
which is proved in Step 3, so the order should be "Step 3 ⇒ the solution of (R1) is unique ⇒ f ↦ µ is linear".

The rest of the argument is correct as written, and it works for every |α| < 1. I checked the right inverse
(1 − C_ṽ)ℛ = 1 by continuity, injectivity via (R2), and the norm bound.

**Fix.** Add the sentence "by (R2) the solution in (R1) is unique, so 𝔣 ↦ µ is linear".

### F8 (MINOR) — The seam constant χ(0) (p < 1)

**Issue.** The paper makes no claim about the size of χ(0), and none is needed: H_n(0⁺) = e^{−2χ(0)} cancels in ω and in
(DW-factor). If the drafters' report says χ(0) = O(log²n), in contrast with the repo's O(log n), that statement is only a
weaker upper bound. Two reasons:

- **Exact reduction.** χ(0) = π^{−1}∫₀^∞ Im L₊(ρe^{iϑ_seam}) dρ/ρ, using L₋(ζ̄) = conj(L₊(ζ)). Im L₊ is bounded, and it
  equals ϖϑ_seam on 1 ≲ ρ ≲ n^p and πp/4 − π/2 on n^p ≲ ρ ≲ n. So χ(0) = O(log n).
- **Numerical check (p = ½, mpmath).** χ(0) ≈ −0.25 log n + O(1) for n = 10…10⁶. Values: −1.035, −1.611, −2.186, −2.762,
  −3.338, −3.913. This matches the predicted −(1/16 + 3/16)log n.

Lemma 6.5(ii)'s bound |χ(z) − χ(0)| ≤ C(1 + log|z|)² for |z| ≥ 1 is correct as an upper bound; I verified it. It is the
bound used, through (O4).

**Fix.** None required. If the paper mentions sup|χ|, say "O(log² n) on |z| ≤ n^p, and χ(0) = O(log n)".

### F9 (MINOR) — Notation clashes

**Issue.** Several symbols carry more than one meaning:

- Π: Π(z) = sinθ/θ′ in §5, the functional Π(X) in §8, and the product Π in Lemma 4.3.
- Φ: the Bessel model Φ_α in §7, and Φ(z) = 2z − 4c + 2𝓡 in Lemma 6.7(i). §7 calls the same function Υ.
- κ: κ_± in §5, the Bessel log constant κ in §7, and κ in Lemma 6.5.
- A₀: an analytic function in Lemma 5.6(iii), and the Bessel prefactor in §7.
- ω: ω(z) = D_W²/W₀, the weight ω(ζ) in Lemma B.2, and ω(T) in Lemma 4.1.
- Incomplete beta: 𝓑_y in §5 vs 𝓘_V in §2.
- c_p in Lemma 4.3 vs c(p).

App. C, Cor. C.4: "|Q_±| is bounded away from 0" should read "bounded on Σ away from the vertex 0".

**Fix.** Rename these.

### F10 (MINOR) — (F1) uniform Cauchy bound; "sketched"

**Issue.** The proof is complete in substance. It uses three blocks: a fixed Carleson curve, a translate of a fixed
infinite curve (three half-lines and a segment), and Hilbert–Schmidt cross blocks. I checked that the nine blocks are
covered. Two points are left implicit:

- the fixed infinite curve is Carleson, so T3(a) applies to it;
- restricting a bounded C_± to a sub-curve is a compression.

**Fix.** State both in one line each.

### F11 (MINOR) — Lemma 4.4

**Issue.** The head bound gives n^{s+4}e^{−2n}; the paper states n^{s+5}, which is weaker but true. No change is needed.

## Steps verified

### §2

- T1(a) extraction identities: (Y₁)₁₂ = h_n, (Y₂)₁₂ = −π_{n+1}h_n, (Y₁)₂₂ = −π_n, and 𝖺 = a_n.
- Prop. 2.2(iii): the constant C_*.
- Lemma 2.1, Rem. 2.2 and Rem. 2.4.

### §3 (item 6)

- Lemma 3.1, Lemma 3.2 (LU → UL).
- Lemma 3.3: a priori bounds and both monotonicity arguments.
- Lemma 3.4, line by line:
  - choice of λ₋ and λ₊;
  - 1 − √(n/(n+1)) ≤ 1/(2n) via √(n(n+1)) ≥ n − 1;
  - 1/n ≤ √(η_n/η₁);
  - increments O(η_n).
- Rate transfer in the proof of Thm 3, with the exact identities for n^{2p}b̃_n² and n^p ã_n.
- Rem. 3.5 (sharpness): I recomputed the expansion â_n − 2c = (θ₀²/c − pc)/n + O(n^{−3/2}).
- Rem. 3.6 (converse).
- The DPQ special-case identification.

### §4 (items 2 and 3)

- Lemma 4.1 (o), (ii), (i), (iii), including the chaining constants.
- Lemma 4.2. The b-formula comes from ∂_τ h_n = h_n⟨f, m_n⟩. The a-formula comes from ϖ_j = −⟨f, q_nq_j⟩ (j < n),
  ϖ_n = −½⟨f, m_n⟩ and ∫xp_nṗ_n = ϖ_na_n + ϖ_{n−1}b_n.
- Lemma 4.3:
  - the Lagrange test polynomial and Christoffel's bound;
  - |k^p − j^p| ≥ c_p max(j, k)^{p−1}|k − j|;
  - the product formula;
  - the identity k + p(n−k)log k + (1−p)I − (n−k)log(n−k) + (n−k) = −n g_p(θ), expanded by hand.
- Lemma 4.4. Prop. 4.5: the constants 2ρ and 6M₀^pρ.
- Assembly. Step 1 uses the base s₀ ∈ (1, 1 + 2p) (s₀ ≥ 1 + p when m ≥ 1) and applies Thm 3 m times with η_n = 1/n to
  positive measures with infinite support. Step 4 applies stability at the final s. The rate O(1/n + ρ_ℓ(⌈n/M₀⌉)) matches
  Thm 1(ii). Every hypothesis holds in the new order.
- Rem. 4.6 (base window, α = 0 unavoidable).

### §5 (item 4)

- Lemma 5.1 (det Y = 1, extraction).
- Lemma 5.2. Lemma 5.3(i)–(iii).
- Lemma 5.6:
  - (i) the global sign Re φ < 0 on ℂ∖[0, 4c], all three cases;
  - (iii) f = (φ ± iπ)²/4 and the branch φ = ∓iπ − 2f^{1/2}.
- ϑ_w = 7π/16 (p ≥ 1), 3πp/8 (p < 1). Checks: ϑ_w/p < ϑ_p; (5/4)ϑ_lip < ϑ_w; ϑ_w < πp/2 for p < 1; ϑ_w < π/2 (needed for
  convexity in Lemma 6.7(ii) and for the B-bounds); the path in Lemma 7.4 Step 3 stays in |Im ξ| ≤ 5ϑ_lip/(4p) < ϑ_p.
- Lemma 5.8, all jumps.
  - (a), (b±), (c±): symbolically, with sympy (script in the scratchpad). The lower vertical segment's + side is Ω^△_−,
    consistent with "mirror image".
  - (d): by hand, including the sign of A^△_−.
  - (e), (f): by hand.

### §6

- Lemma 6.1: ℓ̂ → π/p − π; the B-bounds.
- Lemma 6.2: the reflection computation.
- Lemmas 6.4–6.5 (seam): main-term cancellation in L_±, and the corner bounds.
- Lemma 6.7(i): the Szegő formulas, with Φ = (√z + √(z−4c))² matching §7's Υ.
- Lemma 6.8 (normalisation).
- Lemma 6.9: super-small entries.
- Frame Proposition (F1)–(F8) against their uses in §§7–8. Every item used in §7 is delivered, (F5) modulo F1. (F7) is
  delivered by App. C. I checked the exponents in App. C: (1 + |α|)/4 < ½, and the lens-sector residue argument, including
  |e^{2πit} − 1| ≥ c on |t| ∈ ℕ + ½.

### §7 (item 1, together with App. B)

- Lemma 7.1: the S-matrix factorisation, det Ψ̂ = −2i sin πα, the α = 0 log term with κ = −i/(2π), and the rank-one bound.
- Φ-jumps: the orientation reversal, and c_± ↔ rays.
- (6.28) in the enlarged sector via DLMF 10.40 (|ph 2ζ^{1/2}| ≤ (π − ϑ_lip)/2).
- Lemma 7.2(i): M^{−1}JM = diag(i, −i); f_±^{1/4} ratio −i; removability.
- Lemma 7.2(iii): matching P̂₀ = P^∞₀(I + O(1/n)).
- Lemma 7.4 (lip mismatch), all four steps:
  - D_{x^α}² = (4cz/Υ)^α, giving the factor c_± = e^{∓iπα};
  - the Hölder step;
  - the scale-invariant path bound;
  - ε′_n.
- Thm 7.6 (Neumann step).
- Prop. 7.7 (moments):
  - circle term identity Q̃₋Δ₂Q̃₋^{−1} = Q̃_inQ̃_out^{−1} − I;
  - Bessel localisation integrals for |α| < 1 and α = 0;
  - correction term via Cauchy–Schwarz;
  - Q_k = P_k + O(1/n).

### App. B (item 1)

- Lemma B.1:
  - (a) the shell sum;
  - (b) Cauchy–Pompeiu: sign, orientation and continuity of Ω;
  - (c) Cauchy's formula on the complement of small discs; the vertex condition ρ·sup|F| → 0.
- Lemma B.2:
  - weights Ξ and ∫Ξ² ≤ C for |β| < ½;
  - Step 1 and Step 2 kernels;
  - the partition of source/target pairs into S×S, (B×B)∖(N×N) and the two separated parts;
  - the S×S commutator; the power and log cases;
  - the separated-part Hilbert–Schmidt bounds.
- Prop. 7.5 proof:
  - Step 0 block decomposition;
  - Step 1 for all |α| < 1: L² needs |α| < 1, and the vertex condition holds with O(ρ^{1−|α|/2});
  - Step 2: density, right inverse by continuity, injectivity;
  - Step 3: uniqueness from C–D Thm 4.4 with p = q = 2;
  - Step 4: the partition A×A, B×B, R×R minus overlaps, and the remaining pairs at distance ≥ min(δ, ε)/4;
  - Step 5.

  Nothing else needed the old UR′(b′) argument. App. C proves (F7) for the true Q by the area/Laurent argument, which works
  for all |α| < 1 (O(ρ^{2−(1+|α|)/4}) = o(ρ)). The old small-norm 𝒵̃ is no longer used, because Q̃_k = P_k exactly and the
  circle terms are explicit.

### App. A

- The Minkowski/Mellin bound. Flat kernels for |β| < ½. Curvature errors via e_{ij} = O(1), with the dS factor kept.
- Lemma A.2: modulus and argument parts.
- Dilation invariance and compression to subsets, as needed for Lemma B.2.

### §8

- Lemma 8.1 (invariance).
- P^∞₀ expansions a = 1 − c/z − (3/2)c²/z², a^{−1} = 1 + c/z + (5/2)c²/z², giving Π = c² and 𝖺 = 2c.
- The final O(1/n) bookkeeping.

### Theorems vs proofs

Thm 1(i)–(iii), Thm 2, Thm 3 and Thm 4 as stated in §1 are exactly what is proved, conditional on F1 for Thm 4.

### Item 7 (convention)

The closed form for σ_{2,2} was confirmed independently. I wrote a separate mpmath script (Stieltjes procedure on the
moments ζ(2j + 2), 150 digits). It agrees with b_n = π²/((4n+1)√((4n−1)(4n+3))) and a_n = 2π²/((4n+1)(4n+5)) to
relative error < 10^{−120} for n ≤ 9. Since a_n/(2b_n) = √((4n−1)(4n+3))/(4n+5) = 1 − 1/n + O(n^{−2}), the coefficient
is −p/2 in the paper's pairing.

The repo's +p/2 is the pairing a_n/(2b_{n+1}), since b_{n+1}/b_n = 1 − p/n + O(n^{−2}). Table 2 (−p/2 column) and
Conjecture 10.1(a) are consistent with this.

### Citations

T1–T4 quotes match RH/CITATIONS.md:

- C–D: §4.1, Thm 4.4, §4.2, Prop. 4.6, the Thm 4.7 Neumann step, Prop. 4.9/(4.14).
- KMVV: (6.16)–(6.18), (6.23)–(6.25), (6.28) "uniformly … ζ ∈ ℂ∖Σ_Ψ", angle freedom, (6.51), (6.53), the Prop. 6.5
  removability, the Figure 3 orientation.
- WLXZ: (2.14), (3.9)–(3.11), (4.12)–(4.13), (6.4), (6.10)–(6.12).
- DLMF: 5.5.1, 5.5.3, 5.11.1 with the §5.11(ii) remainder, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2, 10.40.1–5.

The hypotheses at each use match.

The LaTeX log shows no undefined references, and 5 overfull boxes, one of which is 70pt.

## What a human expert should still check

1. **F1.** The soft-edge Airy parametrix, written out in the paper's orientations and frame, including N_r and the
   ω^{1/2} branch. Check this against WLXZ §6.1 (the source PDF, not the repo transcription).
2. **F3.** The region correspondence Ω^△_{l,+} ∪ Ω^△_{r,−} ↔ ℂ_− in WLXZ Fig. 3 / (3.11)–(4.12).
3. **F2.** An explicit lens construction.
4. **Lemma 7.1 in the thin sectors** for p < 1: rays at ±(π − πp/4). KMVV's Hankel formulas (6.24)–(6.25) must be used in
   the narrower sectors, and the continuation of (6.23) in 2π/3 < |arg ζ| < π − ϑ_lip. A specialist should confirm that
   no sectorial constant changes when the rays move.
5. **Lemma B.1(c) applied to Q̃^{±1} − I.** Q̃ is continuous up to Σ̂ at the intersection points of the lips with
   ∂U(0, δ), and of Σ_v and the saturated segment with ∂U(4c, ε). These are listed as vertices, and Q̃ is bounded there;
   confirm against the final contour figure.
6. **Rule R second reader.** A second reader for App. B and §5.7 (the new material). This report is a single AI reading.
7. **Primary sources.** Re-read DPQ Prop. 2.1's proof from the PDF, and DP §1, before submission (citation gate).
