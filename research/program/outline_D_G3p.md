# Problem D — G3′ unconditionally, and its side questions: research-program outline

Source repo: /mnt/c/Users/gspea/source/repos/jacobi-asymptotics (read-only; nothing there was modified).
Read for this outline: AGENTS.md, THEOREMS.md (§§1, 2.5, 3.3, 4, 6), research/G3prime/PROOF.md (§0, §1, §4, §4.1,
§5.2 head, §5.4, §5.5, §6, §7.1 head, §8, §9), research/G3prime/CITATIONS.md (all), research/G3prime/rhfree/
RHFREE.md (§§0, 2–6), RHFREE2.md (status table, §§2–4), RHPRIME.md (header, §0, §4), G3prime/LOG.md (Plans 17, 19).

**Framing (AGENTS.md rule 3).** Nothing in this outline is, or should be presented as, evidence about RH. The
ordinates are inputs. RH appears only as a labelled hypothesis of conditional statements that already exist in the
repo. Several targets below concern zeros *off* the critical line, or deformations of ξ. Results about those say
nothing about where ζ's zeros lie. Write-ups must say so explicitly.

Labels used below: **[repo]** = a REVIEWED result in the repo; **[derived here]** = a short deduction made for this
outline, which needs Rule A/R before it enters the repo; **[recollection]** = my memory of the literature, NOT read
under the citation gate, so it must be checked before use; **[heuristic]** = not a proof.

---

## 0. Executive summary

1. **The main target is out of reach, and this can be shown rigorously.** G3′ ⇒ d(E) = 0 [repo, N″]. Also
   d(E) = 0 ⟺ "100% of zeros (with multiplicity) are simple and on the critical line" [derived here, §1.2; this is
   GLSS's HMH, (C5)]. So an unconditional proof of G3′ would prove that almost all zeros are on the critical line,
   and that almost all are simple. Even **assuming RH**, G3′ would imply "almost all zeros are simple", which is open
   on RH: the best result surveyed in (C3) is 19/27 (Bui–Heath-Brown). This meets the AGENTS.md stop condition "a
   step is as hard as an open problem". It should be logged, once a citation stating the status is read (§1.4).
2. **G3′ splits into two parts** [derived here]: G3′ ⟺ HMH ∧ (𝒞_dist(K) = o(K²)), where 𝒞_dist is the capped
   energy of pairs of *distinct* ordinates. The first part is "algebraic" (no coincidences); the second is "metric"
   (no positive-density clustering at super-exponentially small scales). Unconditionally, neither part is known.
   Even on RH + HMH, nothing that was read controls the metric part.
3. **Statistically, the criterion is very weak.** Any point process with a log-integrable pair correlation at 0
   satisfies it. Poisson does. GUE/sine does, with about 0.24 units of energy per point, which matches Odlyzko's data
   (§5.5). All the difficulty sits in *excluding pathological arithmetic*, not in *proving repulsion*.
4. **Realistic, publishable outputs** are the following:
   - (a) the HMH reduction plus a quantitative two-sided form of Theorem Ch;
   - (b) natural *unconditional* examples where the law **fails** (Dedekind zeta functions of non-abelian Galois
     fields, where Artin factorization forces doubled zeros);
   - (c) examples where it **holds**: the sine-process model a.s., function-field zeta functions (decidable
     exactly), and possibly zeros of the de Bruijn–Newman deformations H_t, t > 0;
   - (d) an explicit constant in Theorem B through BGST's unconditional MT, with uncertain success.
   Together, (a)–(c) make a coherent short paper: "the averaged Jacobi law as a detector of zero coincidences".

---

## 1. What 𝒞(K) = o(K²) says about the zeros

### 1.1 Definitions recalled (PROOF.md §5.4)
- d_ab = (γ_b − γ_a)log(γ_a/2π)/2π.
- (a, b) is near if γ̃_b − γ̃_a < 4C₀.
- P(T) = Σ_{near a<b∈T} log⁺(1/d_ab), which is +∞ on a repeat.
- 𝒞(K) = min_T [P(T) + K·#dropped].
- Theorem Ch (REVIEWED, mod (C1) + Theorem H): G3′ ⟺ 𝒞(K) = o(K²). Quantitatively, limsup 𝒞/K² = c > 0 ⇒
  liminf defect ≤ −θ_c²c.
- Trivially 𝒞(K) ≤ K² (drop everything).

### 1.2 Necessary content: G3′ ⇒ HMH (100% simple and critical) [derived here; elementary]
- A zero ρ = β + iγ with β ≠ ½ has the partner 1 − ρ̄ (functional equation plus conjugation; RHFREE §3 uses the same
  map). The partner has the same ordinate, so the line γ has H(γ) ≥ 2.
- A multiple zero also has H ≥ 2. On a line with H ≥ 2 there are H zeros and H − 1 repeated indices. Hence
  #{ρ : γ ≤ T, H(γ) ≥ 2} ≤ 2·|E ∩ [1, N(T)]|.
- H(γ) = 1 means the zero is simple and critical.
- So d(E) = 0 ⟺ N^{s,crit}(T) = N(T)(1 + o(1)) ⟺ (by the counting in GLSS (7.1)) N^⊛(T) = TL + o(TL), i.e. HMH.
  - The direction "⇐" is Theorem C's "Repeats" bullet.
  - The direction "⇒" is the 2·|E| bound above. (C1) converts index density to height density.
- **Consequence.** G3′ ⇒ HMH. With Theorem C: PCC ⇒ (SG) ⇒ G3′ ⇒ HMH. G3′ sits strictly between two named
  hypotheses of GLSS (C5), and it is not equivalent to HMH (§1.3).

### 1.3 Exact decomposition [derived here, from Ch]
- Let 𝒞_dist(K) be 𝒞(K) computed on [k₂, K] ∖ E, so that repeats are dropped for free.
- If d(E) = 0, dropping E costs ≤ K·|E ∩ [1, K]| = o(K²). Hence **G3′ ⟺ d(E) = 0 ∧ 𝒞_dist(K) = o(K²)**.
- The metric part cannot be omitted. N‴ and the "former sliver" example of §5.4 show that HMH plus gaps
  ≤ e^{−βk} at positive density kill the law, while gaps e^{−k/log k} are harmless.
- Heuristic dictionary [heuristic; it ignores far-zero factors in the Hadamard product]: for an isolated near pair,
  log(1/d_ab) ≈ log(1/|ζ′(ρ_a)|) + O(log log γ_a). So the metric part reads roughly: "for all but o(K) of the first K
  zeros, |ζ′(ρ)| ≥ exp(−o(K))".
  - This is an absurdly weak lower bound for |ζ′| at zeros, compared with the Hejhal-type Gaussian behaviour with
    variance ½ log log T that is expected (on RH) [recollection].
  - It is still not provable, because ζ′(ρ) = 0 at a multiple zero cannot be excluded unconditionally, and no
    quantitative lower bound for |ζ′(ρ)| at simple zeros is known [recollection; verify].

### 1.4 Relation with known open problems and standard conjectures

| Statement | Relation to G3′ | Status |
|---|---|---|
| RH | Neither implies the other as far as is known. RH alone does not give G3′ (100% simple is still needed). G3′ gives only "almost all critical", not "all critical". | Do not discuss beyond this line (rule 3). |
| 100% of zeros on the critical line | Implied by G3′ (§1.2) | Open unconditionally. (C3): best surveyed > 41.72% on the line. (C6) Lamzouri: ≥ 67.25% simple-critical (arXiv v2, Sept 2026, after my training data; **verify its status independently before relying on it**) |
| 100% simple (Essentially Simple Zeros) | Implied by G3′ | Open even on RH: (C3) surveys 19/27 on RH (BHB13) and 67.92% on RH (CdL20) |
| HMH (GLSS) | G3′ ⇒ HMH; HMH ⇏ G3′ in general (metric part) | Hypothesis in GLSS; PCC ⇒ HMH (GLSS Thm 1) |
| PCC (GLSS form, no RH) | PCC ⇒ G3′ (Theorem C) | Open |
| SPC_ℂ⁺, SPC_ℂ⁺(full) | ⇒ G3′ (Thm S, S′) | Open for M > 1 |
| RH + (V⁺) / RH + (V) | ⇒ G3′ (Thm V⁺, Cor P) | Open |
| Small *gaps exist* (liminf of g_k < c: Conrey–Ghosh–Gonek, Bui–Milinovich–Ng, …) | Opposite direction: G3′ needs small gaps to be *rare*. Existence results are irrelevant except as sanity checks | — |
| Upper density of small gaps → 0 as δ → 0 (the content of (SG)) | Sufficient. Not necessary (L′ allows any density of positive gaps of size e^{−o(k/log k)}) | Not known even on RH, since F(α) is known only on [0, 1] |

- **Citation-gate action.** To log the stop condition, quote a read source that calls "almost all zeros simple" (or
  "on the line") open or conjectural.
- Candidates already cited: (C8) Theorem 4, "SPC implies PCC and SZC". Check §6 of (C8) for SZC's definition; if it
  is "almost all zeros simple", that is a named conjecture in a read source. Also GLSS §7 (HMH stated as a
  hypothesis), and the (C3) introduction.
- Until then, the repo's own wording must stay: "beyond the results surveyed".

### 1.5 Probability for the main target
- Unconditional G3′: **< 1%** in any foreseeable horizon. It implies 100%-critical and 100%-simple.
- G3′ on RH alone: also < 1% (100% simple is open on RH).
- **Recommendation:** close Problem D's main line with the §1.2 reduction and redirect effort to §2.

---

## 2. Targets ranked by tractability

Effort is in focused agent-plus-human weeks, under the repo's Rule A/R workflow. Probabilities are for a correct,
REVIEWED result.

### Tier 1 (high tractability)

**D1. HMH reduction and decomposition (§1.2–1.3).**
- Statement:
  - G3′ ⇒ HMH;
  - G3′ ⟺ HMH ∧ 𝒞_dist = o(K²);
  - corollary: G3′ is at least as hard as "almost all zeros simple and critical", and on RH at least as hard as
    "almost all simple".
- Needs:
  - N″ [repo];
  - (C1) for the index ↔ height conversion;
  - GLSS (7.1) [read];
  - one more status quote (§1.4).
- Effort 0.5–1 week. Probability 95%.
- Publishable as part of the paper (it is the honest positioning of the problem).

**D2. Quantitative Theorem Ch (two-sided rate).**
- Target: with c := limsup 𝒞(K)/K² and D := liminf defect, prove −F(c) ≤ D ≤ −θ_c²c, with F(c) → 0 as c → 0.
- Sketch [heuristic]: rerun Ch(i) with drops Δ ≤ cMn. The costs are:
  - index shift ≈ 6n²h(cM), where h(t) = (1+t)log(1+t) − t log t;
  - energy ≤ 2cM²n²;
  - truncation C′/log(M/2) (Lemma Tr).
  - Optimizing over M gives F(c) ≍ 1/log(1/c).
- Needs C′ (Lemma Tr / item 11 H7's constant A) explicit, or at least kept symbolic.
- Effort 1–2 weeks. Probability 70% (symbolic C′), 40% (numeric C′).
- Use: it makes Ch a genuine two-sided quantitative equivalence. It does not improve Theorem B (F(c) is useless for
  c near 1).

**D3. Unconditional failure for Dedekind zeta functions of non-abelian Galois fields.**
- Example: K = ℚ(2^{1/3}, ω), so ζ_K = ζ·L(s, sgn)·L(s, ρ₂)², where L(s, ρ₂) is a Hecke L-function of ℚ(√−3)
  (entire) [recollection; Artin factorization is standard].
  - Every zero of L(ρ₂) appears at least twice in ζ_K. The repeated-index density is ≥ (2/6) = 1/3.
  - So by N″ (adapted), the averaged law for σ_K := Σ 2x_kδ_{x_k} fails: liminf ≤ −0.2397/3.
- **Unconditional and RH-free.** It is the arithmetic instance of Prop N's doubled sequences. In general: for every
  Galois K whose group has an irreducible representation of dimension ≥ 2.
- Needs:
  - a Riemann–von Mangoldt formula with O(log T) error for ζ_K (degree-n L-functions; e.g. Iwaniec–Kowalski Thm
    5.8 [recollection]), the analogue of (C1);
  - the smooth model for the degree-n Weyl law and its Cor H_L-ζ analogue (L(j) := j²x̃_j is still slowly varying;
    check (L1)–(L3) of Theorem H_L);
  - re-running Z1/Z2 and G3′-U steps 1–5 (which N″ uses) with the new N₀.
- Effort 2–4 weeks. Probability 80%.
- Publishable: a clean, natural, decided example. (Prop N's counterexamples are artificial.)

**D4. Random-matrix / sine-process model: G3′ holds almost surely.**
- Model: let (s_k) be the sine process (density 1). Put γ_k := N₀⁻¹(s_k). Then:
  - (i) (C1)-type discrepancy |N − N₀| = O(log T) holds a.s. Counts of a determinantal process in an interval are
    sums of independent Bernoullis (Hough–Krishnapur–Peres–Virág [recollection]), with variance ~ π⁻² log ℓ (Costin–
    Lebowitz, Soshnikov [recollection]). Bernstein's inequality plus a union bound give O(log K) uniformly.
  - (ii) P(K)/K → c_GUE = 0.2410 a.s. (ergodicity of the sine process; E[energy per point] =
    ∫_0^1 log(1/u)(1 − sinc²(u))du < ∞).
  - Hence 𝒞(K) = O(K), and G3′ holds a.s. by Ch, whose proof uses only (C1) and Theorem H (§5.4, "former sliver").
- Side result: Poisson ordinates also have finite pair energy, but their discrepancy is ≍ √K, which violates (C1).
  Whether the law survives √K discrepancy is a nice small question; probably yes, because the index shifts are o(K).
- Effort 1–2 weeks. Probability 75%. Publishable as a section ("the criterion is generic"), not standalone.
- **Framing:** a statement about a model process. It is not evidence about ζ (rule 3; §5.5's caution applies).

**D5. Function-field zeta functions: the law is decided exactly.**
- For a curve C/𝔽_q, the ordinates of Z_C(q^{−s}) are (±θ_j + 2πm)/log q: a periodic configuration with a *linear*
  Weyl law N(T) ~ (2g log q/2π)T. The smooth model is then the pure power x̃_k ≍ k^{−2}, which item 11's Theorem H
  covers citation-free at p = 2.
- Prediction [derived here, heuristic until checked]:
  - Law holds ⟺ the Frobenius angles {±θ_j} mod 2π are pairwise distinct. If they are distinct, all gaps are
    bounded below, (SG) holds trivially, and the law holds.
  - Any coincidence repeats periodically at positive density, so N″ makes the law fail.
  - Example of failure: supersingular curves with repeated eigenvalues (e.g. a Jacobian isogenous to E^g).
- Needs a version of G3′-U/L and N″ for a linear Weyl law (simpler than ζ's).
- Effort 1–3 weeks. Probability 70%. A good worked example (RH is a theorem here, Weil; it plays no role in the
  argument).

### Tier 2 (moderate; uncertain)

**D6. Explicit constant in Theorem B (and an explicit bound limsup 𝒞(K)/K² ≤ 1 − c₀/2).**
- Already implicit [derived here]: Theorem B's separated set (lower density ≥ c₀/2, pairwise normalized distance
  ≥ ¼) has P = O(K log K). So limsup 𝒞(K)/K² ≤ 1 − c₀/2 unconditionally. This is the only unconditional upper bound
  on 𝒞; c₀ is not explicit.
- Obstruction (B3; LOG Plan 17): c₀ comes from the O-constant of Fujii's second moment via GLSS (6.1). At fixed λ
  the O-term is the same order as the main term, so the implicit constant really matters. Taking λ large does not
  help: the O-term still decides when λ is "large enough".
- **Route A (literature):** find an explicit constant for ∫(Δ_U S)² (Fujii 1974/1981; Tsang 1984/86 thesis). Look
  for a stated explicit O-constant, or for an explicit Selberg mollified moment of S(t + h) − S(t).
  - If none is published, deriving one means redoing Selberg's method with constants: months of work, high risk.
  - Probability 20–30%.
- **Route B (new):** replace GLSS (6.1) by BGST's unconditional MT (C3 (3.2)/(3.5)), whose *main term is explicit*
  (errors are relatively o(1)). With Q supported in [−1, 1] (no hypothesis needed), Lemma PC gives
  S_T = N_T(1 + D(η_{1/2})) + o(N_T) unconditionally. Lamzouri-type operator arguments then bound close pairs among
  simple critical zeros.
  - Risk: Lemma G's thresholds (eigenvalues outside (½, 3/2), the factor 4(4E + N_d − N₁)) are far too lossy at
    λ ≤ ½. As stated, the bound exceeds N.
  - A sharpened Lemma G is needed: optimal spectral counting, using that the mass of μ_i is concentrated, not just
    Σ(μ_i − 1)² ≤ E. The target output is an explicit c₁ > 0 such that at least c₁N simple-critical zeros have both
    neighbours at normalized distance ≥ δ₀.
  - The c₀ in hand would then be asymptotically explicit (the limit constant is explicit; "for T ≥ T₀" is not).
  - Probability 35%. Effort 3–6 weeks.
- Secondary improvement: Theorem B's loss −3 log C comes from Lemma S. Make the separated set have **convergent
  density**: run Caro–Wei on short blocks (T, T(1 + 1/m)], then thin each block to an exact quota and spread it
  uniformly. This should let the Theorem T machinery give ≈ 2 log c₀ in place of −3 log(2/c₀ + 1) [heuristic].
  Effort 1–2 weeks. Probability 60%. Repairs Rule R F1's objection constructively.
- Publishability: modest. An explicit constant is a nice remark in the paper; on its own it is a note at most.

**D7. G3′ for the zeros of H_t (de Bruijn–Newman deformation), t > 0.**
- Inputs [recollection, MUST be read under the citation gate]:
  - Ki–Kim–Lee (Adv. Math. 2009): for t > 0, all but finitely many zeros of H_t are real and simple.
  - Rodgers–Tao (Forum Math. Pi 2020): for t > 0 the zeros become asymptotically evenly spaced at large height, with
    an explicit Riemann–von Mangoldt formula including a (t/16) log T-type correction.
- If the spacing statement is as strong as recalled, it gives (SG) directly. Then G3′-L/U, with N₀ replaced by N_t,
  give the law for every t > 0, unconditionally.
- **Framing hazard (rule 3): mandatory text.** The case t = 0 is ζ. Nothing passes to t = 0. Λ ≥ 0 (Rodgers–Tao)
  and the Polymath15 upper bounds are statements about the H_t family and are not used to say anything about RH. Any
  write-up must state that the result is about different functions.
- Effort 2–4 weeks (mostly reading, plus adapting Z1/smooth model). Probability 55% (depends on the exact gap
  statement).

**D8. Weighted Lemma G (deterministic; RHFREE2 §4 OPEN).**
- State it as pure linear algebra / harmonic analysis: for a conjugation-invariant multiset with slowly varying
  positive weights w_z, bound the number of close consecutive simple-real pairs by a defect functional that vanishes
  when tr A_w² is close to Σw_z².
- Obstruction (RHFREE2 §4): the ideal eigenvalues are w_z, not 1, and tr A_w² − Σw² has indefinite sign with
  off-line pairs. A natural attempt: the local-constancy decomposition A_w ≈ ⊕_blocks w̄_B A_B, with Weyl
  perturbation for the variation of w inside blocks (rank/HS control from slow variation).
- Payoff: only the RH-free form of (Q1). Its value is limited because, by (C8) fn 6, strong prime-side hypotheses
  already force RH; see D9.
- Effort 3–6 weeks. Probability 30%. Publishable as a lemma only if Lemma G itself is (novelty UNCHECKED).

### Tier 3 (low tractability or low value; recommend deprioritizing)

**D9. (Q1): one-sided prime variance ⇒ (SG) without RH.**
- Status:
  - on RH it is done (Theorem V⁺);
  - RH-free, the Theorem 7 route is obstructed (Tauberian constant C ≈ 2.17 > 1, RHFREE2 §4);
  - the weighted route needs D8.
- Conceptual problem: prime-variance hypotheses on long ranges already imply RH ((C8) fn 6). Whether a one-sided or
  restricted-range version does is unclear [recollection: off-line zeros inflate the variance through x^{2β}
  terms]. So an "RH-free prime-side" hypothesis may be RH in disguise, and a theorem of that shape has little
  independent content.
- The clean RH-free formulation already exists on the zero side (SPC_ℂ⁺, Thm S/S′).
- Before investing, read Goldston–Montgomery 1987 ([18] in C8) for novelty, together with Heath-Brown's one-sided
  transfer (C8 §8).
- Probability of a meaningful result: 15%. Effort 1–3 months.

**D10. (NA) non-approximation.**
- (NA) is a statement about *hypothetical off-line zeros*. It is vacuous on RH, and its conclusion (Prop Q) is a
  quasi-RH statement.
- **Recommend not pursuing** inside this repo: the rule-3 framing risk is high, and the payoff for Law P is zero (Thm S
  already gives G3′ without (NA)).
- If pursued at all, it should be *only* the deterministic harmonic-analysis lemma (uniform incompleteness of
  {η(u)e^{−2πiux}} against tilted h_z; Beurling–Malliavin / Landau density theory), with no zeta content.
- Probability 10%.

**D11. G3′\* unconditionally.**
- Needs (D∞): N_d/N converges. That is an unconditional *convergence* theorem for the distinct-ordinate proportion.
  No technique for it is known; only liminf bounds exist ((C3), (C6)). HMH gives θ = 1.
- It also needs (SG\*), which on the distinct ordinates is as open as (SG).
- Weak target: G3′\*-U under liminf/limsup density bounds only (an upper bound with a defect controlled by the
  oscillation, as in Remark T′'s ω(η)). Probability 50%, effort 2 weeks. Low value.

---

## 3. Obstructions (with the repo's citations)

1. **Coincidence obstruction.**
   - Counting information (C1) cannot decide G3′ (Prop N, §5).
   - Every unconditional pair-correlation input read ((C5) GLSS (6.1) / Fujii; (C3) BGST MT on |α| ≤ 1) controls
     pair counts at *fixed* normalized scale λ, with a bound that does not tend to 0 as λ → 0. The diagonal-type
     contribution is ≍ TL/λ (GLSS (6.1)).
   - Such inputs cannot distinguish a double zero from two zeros at distance 10^{−K}. Hence they cannot give HMH, let
     alone the metric part.
2. **F(α) range obstruction.**
   - (SG)-type rarity needs F on [1, M(η)] with M(η) ≍ η^{−1/3} (Thm S remark S1). Only |α| ≤ 1 is known (MT; on RH,
     Montgomery).
   - Upper bounds F ≤ C on average with C > 1 (Brun–Titchmarsh-type [recollection]) give only a constant proportion,
     not → 0 (RHFREE2 §4: "a constant C > 1 is useless").
3. **Off-line indefiniteness.**
   - RH-free, the pair weights K(i(ρ − ρ′)L)² are complex and can be of size T^{λ|β−β′|} (RHFREE §4–5).
   - Lamzouri's Hilbert-space identity (C6 Prop 2.1) absorbs this for upper-bound counting (Lemma G), but not with
     weights (D8).
4. **Constant obstruction (Theorem B).** The non-explicit O-constant in Fujii's second moment (C5 Prop 2, secondary),
   plus Lemma S's crude shift (B3).
5. **Metric obstruction.** Even granting HMH, nothing read excludes positive-density near-coincidences at scale
   e^{−βk}. Heuristically, this is a lower bound on |ζ′(ρ)| for almost all zeros, and no such unconditional
   statement is known [recollection].

---

## 4. Literature to read (and what to look for)

Already in the repo:
- **(C5) GLSS §7:** the exact wording of HMH and whether it is called open (for D1's stop-condition citation).
  §6: whether the O-term in (6.1) is traceable to an explicit constant.
- **(C8) Goldston §6:** the definition of "SZC" in Theorem 4 (D1 citation).
- **(C3) BGST §§4–5:** their unconditional simple-zero argument, as a template for D6 Route B. Check the corrected
  MT error terms.
- **(C6) Lamzouri:** verify the 67.25% claim (arXiv v2, Sept 2026; refereeing status). Read §§2–3 in full for
  sharpening Lemma G (D6 Route B).

New:
- **Fujii 1974/1981; Tsang 1984/86 (thesis):** an explicit constant in ∫(S(t + h) − S(t))² (D6 Route A).
- **Selberg 1946 / Fujii, "On the distribution of zeros in short intervals":** unconditional positive proportions of
  small/large gaps, and whether constants are explicit.
- **Montgomery 1973; Cheer–Goldston; Bui–Heath-Brown 2013; Chirre–Gonçalves–de Laat 2020:** RH-conditional simple
  proportions, to calibrate how far "100% simple" is even on RH (D1).
- **Conrey 1989 ("more than two fifths"); Pratt–Robles–Zaharescu–Zeindler 2020:** the current critical-line
  proportion (D1).
- **Soundararajan 1996 (gaps between zeros, RH); Conrey–Turnage-Butterbaugh (r-gaps):** what is known about the
  *density* of small gaps, as opposed to their existence.
- **Hejhal 1989 (log|ζ′(½ + iγ)|); Gonek 1984 (J_{−1}); Milinovich–Ng; Hughes–Keating–O'Connell:** what is known
  about the distribution of |ζ′(ρ)| and negative moments, and under which hypotheses (RH, spacing assumptions). This
  is for the metric half (§1.3).
- **Iwaniec–Kowalski Ch. 5 (zero counting for general L-functions); Artin factorization of ζ_K (Neukirch, Lang);
  Conrey–Ghosh–Gonek on simple zeros of quadratic Dedekind zeta functions:** for D3.
- **Rudnick–Sarnak 1996; Murty–Perelli 1999 (pair correlation of distinct L-functions):** for the abelian-field
  conditional counterpart of D3 (the law conditional on joint PCC).
- **Hough–Krishnapur–Peres–Virág (determinantal processes); Costin–Lebowitz 1995; Soshnikov 2000:** for D4.
- **Ki–Kim–Lee 2009; Rodgers–Tao 2020; Polymath15:** for D7. Find the exact gap and simplicity statements for t > 0.
- **Weil / Katz–Sarnak:** for D5, the Frobenius angle multiplicities and examples with repeated eigenvalues.
- **Goldston–Montgomery 1987:** novelty check for Thm V⁺ and D9.

---

## 5. Suggested plan sequence

| Order | Target | Effort | P(success) | Output |
|---|---|---|---|---|
| 1 | D1 (HMH reduction + status citation) | 0.5–1 wk | 95% | Stop-condition log entry for main G3′; THEOREMS §4 item 1 rewritten |
| 2 | D3 (Dedekind ζ_K failure) | 2–4 wk | 80% | Unconditional natural counterexample |
| 3 | D4 (sine process a.s.) + D5 (function fields) | 2–4 wk | 70–75% | "Generic holds / arithmetic coincidences fail" pair |
| 4 | D2 (quantitative Ch) | 1–2 wk | 70% | Two-sided rate |
| 5 | D6 Route B + convergent-density thinning | 3–8 wk | 35% / 60% | Explicit θ₀ in Theorem B |
| 6 | D7 (H_t, t > 0) | 2–4 wk | 55% | Unconditional positive theorem for a deformation (strict framing) |
| 7 | D8 | 3–6 wk | 30% | Deterministic lemma |
| — | D9, D10, D11 | — | ≤ 15% (useful) | Deprioritize; record as OPEN |

**Paper outline (realistic, about 25 pp.):**
- the averaged Jacobi/Hankel law for zero measures, and Theorem Ch;
- G3′ ⇒ HMH (positioning);
- the conditional closures that already exist (PCC, SPC_ℂ⁺, RH + (V⁺)), stated as hypotheses;
- natural decided examples: ζ_K non-abelian (fails), function fields (exact criterion), sine process (holds a.s.),
  optionally H_t (holds);
- Theorem B, with an explicit constant if D6 succeeds.

Novelty of the core results is UNCHECKED throughout, and a literature search on Hankel determinants / Jacobi matrices of
zero-built measures should precede submission.

**Honesty notes.**
- (i) No item here proves or supports any statement about the location of ζ's zeros.
- (ii) D1 shows only that G3′ is *at least as hard as* known open problems.
- (iii) Numerical agreement (§5.5, §9.4) is about a finite sample.
- (iv) Every [recollection] item must pass the citation gate (AGENTS rule 4) before use.
