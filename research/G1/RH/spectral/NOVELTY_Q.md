# NOVELTY_Q: Rule L search for cluster Q (Theorem Q, Cor Q.1, Prop M1.2 = Paper IV Theorem C, Cor. cor:Q1, Prop. prop:M12)

Date: 2026-10-23. Branch plan-e2-d2. Searcher: a subagent of the JZC session. Rule L only. This file records what the search
found. It does not review the mathematics (Rule R) or the citations (Rule C). It follows the format of NOVELTY_JZC.md and
supersedes that file's §2 (item Q).

- **Network.** The shell cannot reach arxiv.org or any publisher (proxy 403 on CONNECT). Every quote below came through
  WebFetch. WebFetch summarises the page with a small model and caps quotes at about 125 characters, so every quote marked
  "(WebFetch)" is second-hand. Under Rule C, each must be re-read in the source before it is cited. Equation, lemma and theorem
  numbers are as WebFetch relayed them.
- **Robots-blocked.** These were blocked: A. Kuijlaars' KU Leuven publication PDFs (perswww.kuleuven.be/~u0017946/…,
  robots_disallowed), dl.acm.org, ResearchGate, Semantic Scholar and web.archive.org. A human with a browser can probably
  download BK 2001, BIT 2001 and SIREV 2006 from Kuijlaars' publication page (see §4).
- **Verdict scale** (as in NOVELTY_JZC). KNOWN: found essentially as stated. PARTIALLY KNOWN: the named part or the phenomenon
  was found in another setting. NOT FOUND: not located by the queries listed. NOT FOUND describes this search; it is not evidence
  of novelty. MathSciNet and zbMATH were unavailable.

## 0. Summary

**Headline: the decisive item is partly resolved, and it moves Theorem Q towards KNOWN in the compact case.** BK 2001 itself
could not be opened. Three independent restatements of it were read through WebFetch:
- Beckermann–Helart 2017, Lemma 1.5, "following [BK01, Lemma 3.1(a)]";
- Beckermann–Güttel, §4;
- Beckermann's Madrid talk, slide 4.7.

Together they show the following for constraints of finite mass with compact support and **no external field**:
- **the endpoint equation (Q) is in the literature;**
- **a monotonicity criterion of the same kind as (H2) gives the one-band/one-saturated structure**;
- **the constrained equilibrium is given by a Buyarov–Rakhmanov-type superposition of arcsine measures, μ_t = ∫_0^t ω_{S(τ)}dτ,
  with S(τ) shrinking.**

A numerical check (§2.3) shows that Theorem Q's density ν is exactly this superposition. What remains NOT FOUND is the
extension to a constraint of infinite mass at a hard edge and to Y = ∞, the closed single-Cauchy-integral form (G), and
Prop M1.2.

| Item | Verdict | Closest prior work (exact reference) |
|---|---|---|
| Thm Q (i): the soft-edge equation (Q), its unique root, and the monotonicity criterion | **KNOWN for compact support and finite mass (relayed second-hand); NOT FOUND for an infinite-mass hard edge or Y = ∞.** After the reflection y = b − x, Beckermann–Helart Lemma 1.5 states S(t) = [a(t), b], where a(t) is the unique root of t = ∫_{a(0)}^{a(t)}√((b − x)/(a(t) − x))dσ(x). Under the same reflection this equation is (Q) with t = 1. Their criterion, √((x − a(0))(b − x))σ′(x) vanishing at a(0) and strictly increasing, reads in our variables as √(y(Y − y))σ(y) strictly decreasing and → 0 at Y. For Y < ∞ it is *implied by* "g = √yσ decreasing" (F7), so it is weaker than (H2). | Beckermann & Helart, arXiv:1707.07871 (2017), Lemma 1.5, Examples 1.8–1.9; source: Beckermann & Kuijlaars, SIAM J. Numer. Anal. 39 (2001) 300–329, Lemma 3.1(a) (**unread**) |
| Thm Q (ii): the explicit ν | **PARTIALLY KNOWN.** The Q ≡ 0 constrained Buyarov–Rakhmanov formula (μ_t = ∫_0^tω_{S(τ)}dτ, equivalently σ = ∫_0^{‖σ‖}ω_{S(t)}dt and w_t − U^{μ_t} = ∫_0^tg_{S(τ)}dτ) is attributed to BK 2001 Thm 2.1 / its proof. With S(τ) = [0, a(τ)] and F(a(τ)) = τ, it gives ν(x) = ∫_a^Y|F′(b)|ω_{[0,b]}(x)db. This search verified numerically that this equals Theorem Q's ν (§2.3). **The closed single-integral form (G), the balayage form, and the per-point (k_y) proof: NOT FOUND.** | BK 2001 Thm 2.1 (relayed by Beckermann–Güttel §4, ETNA 2002 eq. (2.10), Beckermann Madrid talk slide 4.7); Buyarov–Rakhmanov, Sb. Math. 190:6 (1999) 791–802 |
| Thm Q (ii) 0 < ν < σ, (iii) strict outer inequality, (iv) uniqueness | **KNOWN in the compact finite-mass setting** as general theory: existence and uniqueness (Rakhmanov 1996 Thm 3; Dragnev–Saff 1997 Thm 2.1). Under BK's hypothesis, the structure S(t) = [a(t), b] is BK Lemma 3.1(a). **NOT FOUND for σ of infinite mass (σ(0, Y] = ∞) with Y ≤ ∞.** Dragnev–Saff Def. 1.2 requires a finite constraint; Kuijlaars–Van Assche PLMS 1999 Thm 2.1 works on [0, ∞) but with an external field and a constraint αβ^{−α}x^{α−1} that is finite near 0. | R96, DS97, KVA-PLMS in research/G2/CITATIONS.md (READ) |
| Cor Q.1 (a = 4c(p)) | **The computation is elementary**, of the same kind as Beckermann–Helart Examples 1.8–1.9 (a(t) = t²; a(t)/b = t^{1/(β+½)}). The lattice constrained problem itself is the project's Paper I Thm 1.3. Paper I's μ* = ∫_0^1 arc_{4ct^{−p}}dt is exactly the constrained Buyarov–Rakhmanov superposition with a(τ) = 4cτ^{−p} (observation of this search). No external source has the infinite-mass lattice σ = (1/p)y^{−1/p−1}. | Paper I Thm 1.3 (own); VAVB (boundary case yσ = const) |
| Prop M1.2 (soft-edge root expanded in the poles of Z_N with the π cot kernel) | **NOT FOUND.** No source expands the root of a constrained endpoint equation along a counting-function asymptotic. The termwise Mellin asymptotics of ∫L(Aλ)dN is a standard technique (harmonic-sum Mellin asymptotics; Flajolet–Gourdon–Dumas, TCS 144 (1995) 3–58, located but **not read**). | — |

## 1. Item map

These are the project statements under test (research/G1/RH/spectral/JZC_M1.md; papers/paperIV/sec3.tex):
- **Theorem Q.** No external field; σ on (0, Y], Y ≤ ∞, with ∫_0σ = ∞. (H2): yσ decreasing. (Q): ∫_a^Yσ(y)(1 − a/y)^{−1/2}dy = 1.
  (G): ν(x) = (1/π)√((a − x)/x)∫_a^Y s(y)/(y − x)dy, with s = σ√(y/(y − a)). Plus 0 < ν < σ, the strict outer inequality, and
  uniqueness.
- **Cor Q.1.** The lattice σ = (1/p)y^{−1/p−1} gives a = 4c(p).
- **Prop M1.2.** The expansion of the root A_n of ∫L(Aλ)dN = n, with poles weighted by W(q)π cot(πq).

**Dictionary to the CG literature.** In the CG literature the eigenvalue distribution σ lives on [a(0), b]. The constraint is
saturated near a(0), the small eigenvalues found first, and S(t) = supp(σ − μ_t) = [a(t), b] is the band. Reflect by y = b − x:
- the hard edge 0 of Theorem Q corresponds to b;
- the soft edge a corresponds to a(t);
- Y corresponds to b − a(0);
- the mass t corresponds to 1.
Then √((b − x)/(a(t) − x)) = (1 − a/y)^{−1/2}, and the CG endpoint equation becomes (Q).

## 2. Per-source findings

### 2.1 Beckermann & Kuijlaars, "Superlinear convergence of conjugate gradients", SIAM J. Numer. Anal. 39 (2001) 300–329 (BK01). NOT READ (decisive, still)

- **Abstract** (epubs.siam.org/doi/10.1137/S0036142999363188, WebFetch): "We give a theoretical explanation for superlinear
  convergence behavior." WebFetch paraphrased the rest as follows. The bound depends on the eigenvalue distribution and n/N,
  and is sharp under suitable conditions. The paper "connects to asymptotic results for discrete orthogonal polynomials and
  uses a constrained energy problem from logarithmic potential theory". It has Toeplitz and Poisson examples.
- **What Thm 2.1 is (three relays agree).**
  - It is the asymptotic CG error bound. ETNA 2002 §2 says "the asymptotic bound (1.3) was established in [5, Theorem 2.1]
    under Assumptions 2.1(a)–(d)" (WebFetch).
  - Its proof uses the Q ≡ 0 constrained Buyarov–Rakhmanov formula. ETNA 2002 §2: "we showed using fundamental ideas of
    Buyarov and Rakhmanov [9] that in the case Q ≡ 0 there holds" (2.10) ∫_0^tg_{S(τ)}(0)dτ = F_t − U^{ν_t}(0) (WebFetch).
  - Beckermann–Güttel §4: "For constrained problems without external fields (or νt = 0), a similar formula was established
    in [7, Theorem 2.1]". The formula meant is the Buyarov–Rakhmanov formula, with S(t) = supp(σ − μ_t) decreasing in t
    (WebFetch).
  - Beckermann–Helart cite "[3, Proof of Theorem 2.1]" for the monotonicity of tν_{t,σ} in t (WebFetch).
- **Hypotheses**, as relayed by ETNA 2002 Assumption 2.1 (WebFetch):
  - the eigenvalues lie in [0, R], so "σ has a compact support in [0, R]";
  - U^σ "is a continuous, real-valued function on C" (hence no point masses);
  - (c)–(d) are separation conditions for small eigenvalues.
  - Under Q ≡ 0, "supp(ν_t) = supp(σ)" and "S(t) ⊂ S(τ) for 0 < τ < t < 1".
- **Lemma 3.1(a)** is the band criterion and endpoint equation (§2.2). It is cited, not quoted, by Beckermann–Helart.
- **Consequence.** BK01 is the right comparison for Theorem Q, as NOVELTY_JZC guessed. Relayed, its Q = 0 content is:
  - general constraint, compact, finite mass, continuous potential;
  - μ_t = ∫_0^tω_{S(τ)}dτ (Buyarov–Rakhmanov type);
  - a monotonicity criterion under which S(t) is one interval touching an end of supp σ, with endpoint equation (Q).
  **Theorem Q's novelty claim must be reduced accordingly** (§3).

### 2.2 Beckermann & Helart, "On the sharpness of the weighted Bernstein-Walsh inequality, with applications to the superlinear convergence of conjugate gradients", arXiv:1707.07871v1 (25 Jul 2017; journal not checked). READ via WebFetch (PDF)

- §1.2 constrained problem (WebFetch): "there exists a unique minimizer νt,σ of I(ν) under all candidates ν ∈ M1(supp(σ)) with
  ν ≤ σ/t". σ has compact support and continuous potential, and 0 < t < ‖σ‖. The minimiser is "uniquely characterized by the
  existence of a constant Ct,σ".
- Before Lemma 1.5 (WebFetch): "In our proof of the conjecture, following [3, Lemma 3.1(a)], we will impose sufficient
  conditions on σ" "such that S(t) = [a(t), b] for all t." Here [3] = BK01.
- **Lemma 1.5** (WebFetch; the hypothesis formula was garbled in extraction and is reconstructed):
  - "Suppose that σ is supported on the interval [a(0), b] with density with respect to Lebesgue measure denoted by σ′", such
    that √((x − a(0))(b − x))σ′(x) "vanishes at x = a, and is strictly increasing in [a(0), b]."
  - "Then for all t ∈ (0, kσk) we have S(t) = [a(t), b], with a(t) being the unique solution of the equation"
    t = ∫_{a(0)}^{a(t)}√((b − x)/(a(t) − x))dσ(x); "in particular t 7→ a(t) is strictly increasing."
  - No proof is given there. It points to BK01 Lemma 3.1(a).
- **Internal check of the reconstruction.** Both examples are reproduced exactly by the equation as written above:
  - Ex. 1.8: σ′ = ½(1 − x)^{−1/2} on [0, 1] gives t = ½∫_0^a(a − x)^{−1/2}dx = √a, so "a(t) = t" squared.
  - Ex. 1.9: σ′ = γx^β/√(b − x) gives t = γa^{β+½}B(β + 1, ½), so a(t)/b = t^{1/(β+½)}.
  - In both, h(x) = √((x − a(0))(b − x))σ′(x) is ½√x, resp. γx^{β+½}, which is increasing and 0 at a(0). This supports the
    reconstruction √((x − a(0))(b − x))σ′.
- **Comparison with Theorem Q** (this search's reading, not the authors'). In our variables the criterion is
  h(y) = √(y(Y − y))σ(y) strictly decreasing on (0, Y) with h(Y⁻) = 0.
  - For Y < ∞, g = √yσ decreasing implies h strictly decreasing, so BH/BK's criterion is *weaker* than (H2) and than F7.
  - h stays finite at the hard edge in their setting (σ′ ~ (b − x)^{−1/2} at most, finite mass). Theorem Q has h → ∞ there
    (infinite mass) and allows Y = ∞. Neither is covered.
  - BH also say "there are no longer explicit formulas" (Ex. 1.9 context, for their Ritz-type quantities λ_j, not for a(t)).
- No density formula for ν_{t,σ} and no ∂g_{S(t)} in the paper (WebFetch).

### 2.3 The constrained Buyarov–Rakhmanov superposition = Theorem Q's ν (this search; NUMERICAL)

- **Sources** (relayed):
  - Beckermann, Madrid talk (pro.univ-lille.fr/…/talk_madrid_beckermann.pdf), slide 4.7, attributed to "BB & Kuijlaars'99"
    for Q = 0 (WebFetch): σ = ∫_0^{‖σ‖}ω_{S(t)}dt, and w_{t,0,σ} − U^{μ_{t,0,σ}}(z) = ∫_0^tg_{S(τ)}(z)dτ.
  - Endpoint system for S(t) = [a, b] ⊂ (A, B) with two soft edges: "t = ∫ … √((b−u)/(a−u)) dσ(u), t = ∫ … √((a−u)/(b−u))
    dσ(u)". The constant c and the integration sets were garbled in extraction.
  - The unconstrained original: Buyarov & Rakhmanov, "Families of equilibrium measures in an external field on the real
    axis", Sb. Math. 190:6 (1999) 791–802, doi 10.1070/sm1999v190n06ABEH000407 (mathnet sm407; abstract only).
- **Reading for Theorem Q.** With S(τ) = [0, a(τ)], F(a(τ)) = τ (F decreasing, so S shrinks as τ grows, as in BK) and
  ω_{[0,b]}(x) = 1/(π√(x(b − x))):

    ν_BR(x) = ∫_0^1ω_{[0,a(τ)]}(x)dτ = ∫_a^Y|F′(b)|/(π√(x(b − x))) db,   0 < x < a.

- **Check.** Scratch script, not committed: scipy quad in double precision, not certified. It compares ν_BR with Theorem Q's
  (G) at x = a/10, a/2, 0.9a:
  - lattice p = 0.6: relative difference ≤ 6.3·10⁻¹⁵;
  - lattice p = 1.5: ≤ 4.1·10⁻¹⁶;
  - σ = e^{−y}/y on (0, ∞), a = 0.61032057: ≤ 3.7·10⁻¹¹ (numerical F′).
  - The two representations agree, so **Theorem Q's ν is the constrained Buyarov–Rakhmanov superposition**, extended to
    infinite mass. (G) is a closed single-integral form of it. An analytic proof of the identity was not written here.
- Paper I's μ* = ∫_0^1 arc_{4ct^{−p}}dt (G2/CITATIONS.md, KVA-PLMS note) is the same superposition with a(τ) = 4cτ^{−p}.
- Kuijlaars–Van Assche PLMS Thm 2.1 (v = b_α * ω_{[A,B]}, with a field) has the same superposition structure.

### 2.4 Beckermann & Kuijlaars, "Superlinear CG convergence for special right-hand sides", ETNA 14 (2002) 1–19. READ via WebFetch (emis mirror PDF)

- §2 relays BK01 as in §2.1 (Thm 2.1; eq. (2.10); eq. (2.9) S(t) = supp(σ − ν_t) ∩ supp(ν_t); Assumption 2.1).
- Thms 2.7–2.8 and (2.24)–(2.25) (external field, left ansatz) cite [20, 21] (Kuijlaars–McLaughlin; Kuijlaars, Duke 2000)
  and [11], not BK01. The excerpt has no Q ≡ 0 endpoint equation. This corrects NOVELTY_JZC §2.1, which took (2.25) as the
  nearest analogue. The Q ≡ 0 analogue is BH Lemma 1.5 / BK01 Lemma 3.1(a).

### 2.5 Beckermann & Güttel, "Superlinear convergence of the rational Arnoldi method …", Numer. Math. (revised preprint, pro.univ-lille.fr/…/revised_Beckermann_Guettel_Numer_Math.pdf). READ via WebFetch

- §4 (WebFetch): "For constrained problems without external fields (or νt = 0), a similar formula was established in
  [7, Theorem 2.1]". [7] = BK01. Similar to the Buyarov–Rakhmanov formula [11], with S(t) = supp(σ − μ_t) decreasing.
- Remark 6.1: μ_t = ∫_0^tμ̃_τdτ (balayage version, with an external field).
- No endpoint equation is attributed to [7].

### 2.6 Lapik & Beckermann, "The interval of equilibrium for the constrained energy problem in the presence of an external field" (Univ. Lille preprint, 2006; pro.univ-lille.fr/…/abs/LapikMAv2.pdf). READ via WebFetch

- Thm 1 gives endpoint equations (9) for S = [α, β], with Q, σ on [A, B], U^σ continuous, and ∫|y − γ|^{−1/2}dσ < ∞.
- Thm 2 covers continuity and monotonicity of the endpoints in the mass x.
- An example shows that the endpoint system can have infinitely many solutions.
- Cites Kuijlaars 2000 Prop. 4.1(a): "for y > x, µ_y − µ_x ≥ 0", and its eq. (4.12) and Lemma 4.4(c).
- **It states that a Buyarov–Rakhmanov result for the constrained case with external field is unknown** (WebFetch paraphrase).
  This is consistent with BK01 having it only for Q ≡ 0.
- No density formula, and no √(…)σ′ criterion.

### 2.7 Beckermann, Güttel & Vandebril, "On the convergence of rational Ritz values" (SIMAX 2010; preprint BB_SG_RV.pdf). READ via WebFetch

- Relays Kuijlaars 2000. The Ritz-value distribution is the minimiser of mass t with μ ≤ σ, reflecting interlacing. The
  hypotheses (H1)–(H3), (H5) are Kuijlaars'.
- Equidistant example: "supp(σ − µ) = [−a(t), a(t)] with a(t) = √(1 − t²) (cf. [6])" (Rakhmanov's case).
- No general formula.

### 2.8 Kuijlaars, "Which eigenvalues are found by the Lanczos method?", SIMAX 22 (2000) 306–321. NOT READ

- ResearchGate preview (WebFetch, abstract paraphrase): the region is "characterized by an extremal problem in potential
  theory which was first considered by Rakhmanov".
- Content relayed through Lapik–Beckermann: Prop. 4.1 (monotonicity of μ_t in t, weak continuity), eq. (4.12), Lemma 4.4(c).
- The full text was not reached: epubs.siam.org/doi/10.1137/S089547989935527X is robots-blocked, and the dspace.library.uu.nl
  handle 1874/2041 shows only an abstract fragment.

### 2.9 Other constrained-equilibrium sources

- **Dragnev–Saff 1997 (DS97), Rakhmanov 1996 (R96), Kuijlaars–Van Assche PLMS 1999 (KVA-PLMS), Van Assche–Van Baelen (VAVB).**
  Already READ and quoted in research/G2/CITATIONS.md. Nothing to add, apart from the Q ≡ 0 identity relayed from Dragnev's
  SSPT10 slides (renyi.hu, WebFetch): "If Q ≡ 0, then σ − λσ = (‖σ‖ − 1)µQ for Q(x) = −Uσ(x)/(‖σ‖ − 1)". This needs
  ‖σ‖ < ∞, so it is not applicable to Theorem Q. DS97 §4 beyond Example 4.1's opening is still unread. The Springer page
  (doi 10.1007/BF02843160) shows only the abstract ("explicit results for Krawtchouk polynomials", paraphrased).
- **Coroian–Dragnev–Legg–Orive, "On constrained Riesz minimum energy problems", arXiv:2608.11987 (Aug 2026).** HTML read via
  WebFetch.
  - The log case appears only as background, and the paper assumes compact K and continuous U^σ.
  - Its explicit result is a Riesz ball.
  - It does not cite BK01.
  - It is not relevant to Q beyond context.
- **Dai & Yao, "Uniform asymptotics for the discrete Laguerre polynomials", arXiv:2104.03563 (2021).** PDF via WebFetch.
  - Nodes k²/N², constraint density 1/(2√x) on (0, ∞), field V = cx.
  - For c > π²/4: saturated on (0, a), band (a, b), void beyond. Density on the band (Prop. 2):
    (c/2π)√((b−x)/(x−a)) + (1/2π)√((b−x)/(x−a))∫_0^a√((a−s)/(s(b−s)))ds/(s − x).
  - This is the same Cauchy-integral type as (G), but in the mirror configuration: saturation at the hard end 0, finite σ
    near 0, an external field and a void. It is not Theorem Q's configuration.
- **Bleher–Liechty, arXiv:0909.1985.** Kuijlaars' structural form ρ = (1/π)√q₁ on bands; no closed formula (WebFetch).
- **Lapik, Keldysh preprints 2015/2016/2018 and Sb. Math. 206:2 (2015)** (mathnet abstracts). These give
  Buyarov–Rakhmanov-type "recovering formulas" for vector problems, one (preprint 2018-203) "with constraints and external
  fields". Abstracts only. They are vector problems; the upper-constraint content was not confirmed.
- **Kessinger & Martínez-Finkelshtein, arXiv:2603.17913.** Field = multiple of the uniform charge on [−1, 1]; not constrained.
- **Krasovsky, arXiv:math-ph/9811018.** Meixner zero distribution by a WKB-type method; no constraint formula in the abstract.
- **Reciprocal lattices x_k = k^{−p}.** No external zero-distribution result was found. The only hits were the project's own
  setting, VAVB (q-lattice, the yσ = const case), and Šťovíček–Świderski arXiv:2409.19644 (NOVELTY_JZC §1).

## 3. Verdicts and recommended labels

- **Theorem Q: novelty POSSIBLY-NEW → change to PARTIALLY KNOWN** (recommended). Two of its three structural components are in
  BK01 for compact, finite-mass constraints with no external field, as relayed by BH 2017, Beckermann–Güttel and ETNA 2002:
  - the endpoint equation (Q), with a monotone criterion (weaker than (H2) when Y < ∞) that guarantees one band touching the
    hard end;
  - the Buyarov–Rakhmanov superposition, which gives the density.
  What remains, and may be claimed as NOT FOUND:
  - (a) the infinite-mass constraint at a hard edge (h → ∞) and Y = ∞, with existence, uniqueness and the outer inequality
    proved directly (Lemma EP), with no finite-mass theory;
  - (b) the closed single-Cauchy-integral form (G), its balayage form, and the per-point k_y proof;
  - (c) the explicit soft-edge constant C = −h(a)/(π√a).
  Until BK01 is read, the exact form of Lemma 3.1(a)'s hypothesis and whether Thm 2.1 states μ_t = ∫ω_{S(τ)}dτ in that form
  rest on relays. Mathematical labels (PROVED + REVIEWED) are unaffected.
- **Cor Q.1: no novelty claim.** It is an elementary evaluation of a known-type endpoint equation (cf. BH Ex. 1.8–1.9). The
  lattice problem itself is Paper I. The link a = 4c(p) to Law P is the project's.
- **Prop M1.2: NOT FOUND (POSSIBLY-NEW may stay).** The Mellin technique is standard. The statement (the root of the constrained
  endpoint equation carries the non-Weyl poles of Z_N with weight W(q)π cot(πq)) was not found.
- **Suggested edit to JZC_M1 §6 (for the session, not done here).** Add BK01 Lemma 3.1(a) / BH Lemma 1.5 and the BR
  superposition. Note that (G) = ∫|F′(b)|ω_{[0,b]}db (NUMERICAL, §2.3). That identity could be added as a remark with a short
  proof.

### Suggested wording for Paper IV §8, first paragraph (replace from "For conjugate-gradient convergence …" to "… hard edge at $0$.")

> For constraints of finite mass with compact support and no external field, the structure of Theorem~\ref{thm:Q} appears in
> the analysis of conjugate-gradient convergence by Beckermann and Kuijlaars \cite{BeckermannKuijlaars2001}. According to
> \cite[Lemma~1.5]{BeckermannHelart}, which follows \cite[Lemma~3.1(a)]{BeckermannKuijlaars2001}, if
> $\sqrt{(x-A)(B-x)}\,\sigma'(x)$ vanishes at $A$ and increases on $[A,B]$, then the support of $\sigma-\mu_t$ is a single
> interval $[a(t),B]$, and $a(t)$ solves an equation that becomes~\eqref{eq:Q} after the reflection $y=B-x$. According to
> \cite{BeckermannGuettel,BeckermannKuijlaars2002}, \cite[Theorem~2.1]{BeckermannKuijlaars2001} and its proof also give a
> constrained analogue of the Buyarov--Rakhmanov formula \cite{BuyarovRakhmanov}, in which $\mu_t$ is a superposition of the
> equilibrium measures of the decreasing sets $\operatorname{supp}(\sigma-\mu_\tau)$, $\tau<t$. In the present setting this
> superposition is $\nu=\int_a^Y|F'(b)|\,\omega_{[0,b]}\diff b$, and \eqref{eq:nu} is a closed form of it. What is new here, as
> far as we know, is the constraint of infinite mass at a hard edge, with $Y=\infty$ allowed. In this case the finite-mass theory
> \cite{Rakhmanov,DragnevSaff} does not apply, and existence, uniqueness and the strict outer inequality are proved directly.
> Also new are the single-integral form~\eqref{eq:nu} and the edge constant of Remark~\ref{rem:Q}(b). We have not been able to
> consult \cite{BeckermannKuijlaars2001} itself.

Bib entries this wording needs:
- BeckermannHelart: B. Beckermann, T. Helart, arXiv:1707.07871 (2017).
- BeckermannGuettel: B. Beckermann, S. Güttel, Numer. Math. (check the volume).
- BuyarovRakhmanov: Sb. Math. 190:6 (1999) 791–802.

All were relayed second-hand. Under Rule C, use "according to" until each is read and quoted in a CITATIONS.md. If BK01 is read
and Lemma 3.1(a) / Thm 2.1 are confirmed, drop the last sentence and replace "According to …" by direct citations.

## 4. What remains unread (priority order)

1. **BK01 itself.** Lemma 3.1(a) (exact hypothesis, and whether it covers h unbounded at the hard end), Thm 2.1 and its proof
   (the form of the Buyarov–Rakhmanov formula; whether ν_t's density is written out), and §§ on examples (Toeplitz, Poisson).
   Probably downloadable by a human from A. Kuijlaars' KU Leuven publication page (perswww.kuleuven.be/~u0017946/publications/,
   robots-blocked for WebFetch; the BIT 2001 file is at …/Papers01/art2001h-Beckermann-Kuijlaars-BIT/…, so SINUM is likely in
   the same folder).
2. Kuijlaars, SIAM Rev. 48 (2006) 3–40 (…/Papers06/art2006a-Kuijlaars-SIREV/Kuijlaars-SIREV2006.pdf, robots-blocked). It
   probably restates BK01 Thm 2.1 and Lemma 3.1 with examples.
3. Kuijlaars, SIMAX 22 (2000) 306–321 (Prop. 4.1, (4.12), Lemma 4.4).
4. Beckermann–Kuijlaars, BIT 41 (2001) 856–867 (Springer abstract read; full text robots-blocked).
5. Beckermann, "A note on the convergence of Ritz values for sequences of matrices", ANO 408, Lille (2000). Not online in the
   ANO index (which lists ano448–468 only).
6. Dragnev–Saff 1997 §4 beyond Example 4.1. Kuijlaars–Rakhmanov, J. Comput. Appl. Math. 99 (1998) 255–274 (not located
   online). Lapik 2018 Keldysh preprint 203 (constraints + BR-type recovery formulas).
7. Flajolet–Gourdon–Dumas 1995 (for the Prop M1.2 technique attribution only).

## 5. Queries run (Rule L)

WebSearch (standard unless noted):
1. "Beckermann Kuijlaars \"Superlinear convergence of conjugate gradients\" SIAM J. Numer. Anal. 39 2001 constrained equilibrium
   Theorem 2.1"
2. "Beckermann Kuijlaars superlinear convergence conjugate gradients pdf"
3. "Beckermann Kuijlaars \"Superlinear convergence of conjugate gradients\" preprint ANO Lille pdf"
4. "Kuijlaars \"Convergence analysis of Krylov subspace iterations with methods from potential theory\" SIAM Review 2006 pdf
   constrained equilibrium"
5. "\"Superlinear convergence of conjugate gradients\" Beckermann Kuijlaars SIAM Journal on Numerical Analysis 2001 doi 10.1137"
6. "Beckermann Kuijlaars \"On the sharpness of an asymptotic error estimate for conjugate gradients\" BIT 2001"
7. (extended) "constrained equilibrium problem \"eigenvalue distribution\" conjugate gradient Buyarov Rakhmanov formula \"S(t)\"
   Green function integral explicit example interval density"
8. "Kuijlaars Krylov subspace potential theory survey \"constrained equilibrium\" \"conjugate gradient\" pdf kuleuven 2006"
9. "\"Which eigenvalues are found by the Lanczos method\" Kuijlaars arXiv"
10. "Beckermann \"A note on the convergence of Ritz values for sequences of matrices\" constrained equilibrium"
11. (extended) "\"constrained equilibrium\" \"Buyarov\" \"Rakhmanov\" integral formula \"decreasing\" support S(t) Beckermann
    Kuijlaars \"Theorem 2.1\" Ritz values"
12. "citeseerx \"Superlinear convergence of conjugate gradients\" Beckermann Kuijlaars 1999"
13. (extended) "Beckermann Kuijlaars conjugate gradients \"constrained energy problem\" \"asymptotic eigenvalue distribution\"
    \"S(t)\" \"Lemma 3.1\""
14. "perswww.kuleuven.be u0017946 publications Beckermann Kuijlaars SIAM Numer Anal 2001 superlinear"
15. (extended) "constrained equilibrium measure derivative with respect to mass \"equilibrium measure of\" \"S(t)\" \"d/dt\"
    Kuijlaars Rakhmanov \"decreasing family\" σ constraint no external field"
16. "Kuijlaars Rakhmanov \"Zero distributions for discrete orthogonal polynomials\" J. Comput. Appl. Math. 1998 constrained
    equilibrium explicit Meixner Charlier"
17. "zero distribution discrete orthogonal polynomials nodes 1/k^2 OR \"k^{-p}\" accumulating at zero constrained equilibrium
    infinite mass hard edge"
18. "Dragnev Saff 1997 \"Constrained energy problems with applications to orthogonal polynomials of a discrete variable\" pdf
    Vanderbilt"
19. "researchgate \"Superlinear Convergence of Conjugate Gradients\" Beckermann Kuijlaars abstract \"constrained\" \"eigenvalues\""
20. (extended) "Kuijlaars SIAM Review 2006 Krylov potential theory \"constrained equilibrium\" example eigenvalue distribution
    \"S(t)\" superlinear Lemma integral formula ω_{S(t)}"
21. "arXiv Ritz values asymptotic distribution Lanczos \"constrained equilibrium\" Kuijlaars 2000 theorem restated support
    supp(σ − μ_t) explicit"
22. "Buyarov Rakhmanov \"families of equilibrium measures\" external field real axis formula μ_t = ∫ ω_{S_τ} dτ constrained
    analogue"
23. "Lapik 2018 \"Recovering formulas for equilibrium measures\" vector potential theory constraints external fields Keldysh
    preprint 203 pdf"
24. (extended) "\"constrained equilibrium\" logarithmic potential constraint \"infinite mass\" OR \"infinite total mass\" OR
    \"unbounded constraint\" explicit density saturated region band hard edge"
25. "orthogonal polynomials discrete measure points accumulating at zero \"x_k = k^{-p}\" OR \"1/k^2\" OR \"reciprocal\" zeros
    asymptotic distribution equilibrium constraint Jacobi matrix compact inverse"
26. "Flajolet Gourdon Dumas \"Mellin transforms and asymptotics: harmonic sums\" Theoretical Computer Science 1995"
27. "equilibrium endpoint equation soft edge asymptotic expansion poles spectral zeta function \"cot\" Mellin constrained
    equilibrium discrete orthogonal polynomials Weyl law corrections"

WebFetch (✓ content obtained; ✗ blocked or failed):
- ✓ arxiv.org/pdf/1707.07871 (×2), arxiv.org/abs/1707.07871
- ✓ talk_madrid_beckermann.pdf; ✓ revised_Beckermann_Guettel_Numer_Math.pdf; ✓ LapikMAv2.pdf; ✓ BB_SG_RV.pdf
- ✓ the ANO index (no 1999–2000 files); ✓ pro.univ-lille.fr/bernhard-beckermann/publications
- ✓ emis ETNA 14 pp1-19.pdf; ✓ epubs.siam.org BK01 abstract
- ✓ Springer BIT 2001 abstract; ✓ Springer DS97 abstract; ✓ Springer Beckermann–Gryson 2010 abstract
- ✓ simoncin superminres2.pdf; ✓ Carson Dublin2023.pdf; ✓ Embree 39860.pdf (all irrelevant)
- ✓ researchgate Kuijlaars 2000 (preview only); ✓ dspace.uu.nl 1874/2041 (fragment)
- ✓ arxiv.org/html/2608.11987; ✓ arxiv 2104.03563 abs + pdf; ✓ arxiv 0909.1985 pdf; ✓ arxiv 2603.17913 abs;
  ✓ arxiv 1604.03070 abs; ✓ arxiv math-ph/9811018 abs; ✓ arxiv 1309.4882 pdf (irrelevant)
- ✓ mathnet sm407, sm8347, ipmp2562, ipmp2189, ipmp2045, ipmp2632; ✓ renyi.hu Dragnev_SSPT10_External.pdf;
  ✓ w3.ual.es FoCMworkshop6.pdf
- ✗ perswww.kuleuven.be BIT2001 and SIREV2006 PDFs (robots); ✗ epubs SIREV (robots); ✗ dl.acm.org; ✗ researchgate SIREV;
  ✗ semanticscholar (page and API); ✗ web.archive.org; ✗ pro.univ-lille.fr/bernhard-beckermann (allowlist);
  ✗ arxiv abs 2501.09199 and math/0312063 (allowlist); ✗ proquest
