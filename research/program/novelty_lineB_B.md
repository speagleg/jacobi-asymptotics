# Rule L novelty search: Line B (Route II, RedA, QLP), pointwise Law P for k^{−s}Ψ with Ψ slowly varying

Date: 2026-10-14. Searcher: one subagent session. The repo was read-only and was not modified.

**Repo files read:**
- AGENTS.md
- THEOREMS.md §2.7–§2.8
- research/G1/PROOF.md §3.16 (QLP), §3.17 (RedA / RII / B_{p>1}), and the headers of §3.19–§3.23
- research/G1/RH/route2/ROUTE2.md, in full
- research/program/novelty_G1RH.md and novelty_G1transport.md (earlier searches). This search builds on them and does not
  redo them.

**Rule C.** Every quote below is copied verbatim from a source opened in this session: arXiv PDF via pdftotext, a Crossref
abstract, or a PDF on an author's homepage. PDF extraction loses some math glyphs; where it did, this is flagged. Sources
seen only in search snippets are listed separately as "seen, not opened" and are not quoted.

**Access limits.**
- The arXiv API was rate-limited ("Rate exceeded") for the whole session, so no systematic arXiv keyword sweep could be
  run. Discovery used web search plus the Semantic Scholar citation list of Conway–Deift.
- AMS (Vuilleumier 1976) returned 403. Bingham–Goldie–Teugels (BGT) is a book and was not opened; its theorems are cited
  here only through verbatim quotations in opened papers.
- "NOT FOUND" means not found in what could be opened. It does not mean proved new.

---

## 0. Summary of verdicts

| # | Result | Verdict | Closest prior work (opened) |
|---|---|---|---|
| 1 | **Headline.** Pointwise Law P (n^pb_n → c(p), n^pa_n → 2c(p)) for Σk^{−s}Ψ(k)δ_{k^{−p}}, with Ψ any sequence-form slowly varying function (including D(γ) = ∞, e.g. exp √log k), for all p > 0 and s > 1 | **NOT FOUND** | Nearest RH results on non-analytic weights are all *continuous* weights on a fixed interval: Conway–Deift (one explicit log weight), Deift–Piorkowski, Piorkowski 2019, Trogdon 2026, McLaughlin–Miller. Nearest "o(1) recurrence asymptotics without analyticity" is Levin–Lubinsky (exponential weights, non-RH). Discrete accumulating case: only WLXZ (one explicit family; earlier search). |
| 2 | **Technique.** (a) Gaussian smoothing to an entire log-weight plus a stability transfer; (b) Conway–Deift comparison at a Bessel hard edge of order α ∈ (−1, 1), with comparison parametrix built from W̃ = D_w and a lip mismatch o(1) without rate | **PARTIALLY KNOWN** | (b) C–D Thm 4.4 + Thm 4.7 is exactly "sup-norm mismatch → 0 suffices for uniform invertibility", and C–D's weight log(2k/(1−x)) *is* a slowly varying factor at the edge. (a) DIK §6.2 approximates non-analytic V by analytic (trigonometric) V^{(n)} and redoes the RH analysis. **New relative to these:** an arbitrary (smoothed) slowly varying factor rather than one explicit log; Bessel order α ∈ (−1, 1) rather than the Legendre edge (α = 0); a discrete, accumulating-node RH problem; the comparison parametrix built from the Szegő function D_w of the whole weight rather than from a second, reference orthogonality problem. |
| 3 | **QLP.** Uniform hard-edge (index-tail) localization μ_m((Mn, ∞)) ≤ CM^{−p/2}, …, via a Stieltjes-transform bound at a point in the non-oscillatory RH region | **NOT FOUND** as a statement. Ingredients are **KNOWN**: Lemma GS is the classical Green-function identity; Lemma ST is elementary | Teschl, *Jacobi Operators*, (1.99)–(1.100), (2.122). Lubinsky 2009 localization, already in the earlier search. |
| 4 | **RedA.** Sequence-form slowly varying Ψ ⇒ entire L₁ with L₁^{(j)} → 0 uniformly in horizontal strips and Ψ/Ψ₁ → 1 | **PARTIALLY KNOWN** (very likely KNOWN in substance) | The real-variable part (a C^∞ equivalent with all log-derivatives → 0) is BGT Thm 1.3.3 / 1.8.2 (smooth variation), quoted via Eichinger–Winter, Benaim–Friz and Alouin–Bigot. The complex-sector notion and the characterization zf′/f → 0 in sectors is Vuilleumier, Trans. AMS 1976 (abstract opened). Whether Vuilleumier or BGT state "every slowly varying function is ~ an analytic slowly varying function in a sector" is **not verified**, because the paper and the book could not be opened. RedA(iii) (base change) is repo-internal (T3-conv); the earlier search covered it. |

**Positioning.** The headline theorem looks new: a scaled, pointwise recurrence-coefficient law for a discrete measure
whose atoms accumulate at 0 and whose weight carries an arbitrary non-analytic slowly varying factor. Its method is a
recognizable combination of known pieces: the C–D comparison, the DIK-style analytic-approximation reduction, and
smooth/analytic variation from regular-variation theory.

The honest novelty claims are narrower:
- Lemma LW1′ and the observation that a *slowly varying* (not merely logarithmic) non-Fisher–Hartwig hard-edge factor
  costs only an o(1) sup-norm lip mismatch when D_w is used as W̃.
- The extension of the C–D frame (UR′, including (b′)) to a Bessel edge of order |α| < 1.
- Applying all of this to a discrete RH problem with accumulating nodes.

RedA should be presented as a (strip-uniform) form of the smooth variation theorem, citing BGT and Vuilleumier, not as a
new lemma.

---

## 1. Headline (Corollaries B_{p>1}, B_all, B_{p<1}, B_{p=1}^{all}): NOT FOUND

**What is claimed** (THEOREMS §2.8, verbatim): "With Plan 54 the pointwise Law P holds for every p > 0, every s > 1 and
every sequence-form slowly varying Ψ."

**Earlier searches (not redone).**
- novelty_G1RH.md §0: "WLXZ remains the only RH analysis of discrete OPs on infinitely many nodes accumulating at a finite
  point".
- novelty_G1transport.md §6: T3-all and T3-log are NOT FOUND, and "BKMM-type RH analysis needs analytic weights".
- The only exact instance in the family is Ψ ≡ 1, (p, s) = (2, 2) (Lommel ν = 3/2). It has no non-trivial Ψ.

This search adds the following for the *non-analytic weight* aspect.

**Closest prior work (opened).**

1. **Conway–Deift**, arXiv:1711.01590v4, SIGMA 14 (2018) 056, DOI 10.3842/SIGMA.2018.056. Abstract: "we compute the
   asymptotic behavior of the recurrence coefficients for polynomials orthogonal with respect to a logarithmic weight
   w(x)dx = log 2k/(1−x) dx on (−1, 1), k > 1 … but not in the standard way as there is no known parametrix for the
   Riemann–Hilbert problem in a neighborhood of the logarithmic singularity at x = 1." (The fraction is flattened by
   extraction.)
   - *Differs:* a single explicit continuous weight on [−1, 1], with the Legendre edge (α = 0). The result is a full
     second-order term, 2C/(n log n)².
2. **Deift–Piorkowski**, arXiv:2307.09277v2, SIGMA 20 (2024) 004, DOI 10.3842/SIGMA.2024.004. Abstract: "We prove an
   asymptotic formula for the recurrence coefficients of orthogonal polynomials with orthogonality measure log 2/(1−x) dx
   on (−1, 1). The asymptotic formula confirms a special case of a conjecture by Magnus and extends earlier results by
   Conway and one of the authors."
   - On Magnus's general conjecture (§1): "Magnus considered wM(x) … satisfying the following two conditions:
     • wM(x)/(1 + x)^β has a positive finite limit for x → −1, • wM(x)/[−(1 − x)^α log(1 − x)] has a positive finite limit
     for x → +1, where α, β > −1."
   - *Differs:* Magnus's class (Jacobi exponent times one log) is still conjectural in general. The repo proves only the
     *leading-order* law, for a discrete measure and a general slowly varying factor, so there is no overlap in
     statements.
3. **Piorkowski**, arXiv:1910.00564v2, "Riemann–Hilbert theory without local parametrix problems: applications to
   orthogonal polynomials". Abstract: "We show that this can be done, provided an a priori estimate for the exact
   solution of the Riemann–Hilbert problem is known. This enables us to derive asymptotic results for orthogonal
   polynomials on [−1, 1] with a new class of weight functions."
   - §5: "We impose analytic continuation of ρ to a lense-shaped neighbourhood of (−1, 1) and a growth condition at the
     endpoints (cf. Figure 1 and Eq. (4.8)). In particular, we do not require any sort of analytic continuation around
     x = ±1."
   - Condition (4.8): "|ρ(z)| = O(|z ± 1|^{−1/ν+ +ε}), |ρ(z)^{−1}| = O(|z ± 1|^{−1/ν− +ε})".
   - *Differs:* continuous weights on [−1, 1]. Pointwise OP asymptotics with error O(n^{−λ}) off the edges (Thm 4.4); no
     recurrence-coefficient statement was found in the text (grep for "recurrence": none). This class *does* contain
     edge factors such as exp √log(1/(1−x)) that are analytic in a lens. It is the closest continuous-weight competitor
     to "RH with a non-analytic slowly varying edge factor", and the repo should cite it.
4. **Trogdon**, arXiv:2412.18656v5, SIGMA 22 (2026) 006, DOI 10.3842/SIGMA.2026.006. Abstract: "We consider the
   asymptotics of orthogonal polynomials for measures that are differentiable, but not necessarily analytic,
   multiplicative perturbations of Jacobi-like measures supported on disjoint intervals … what appears to be the first
   result for asymptotics when the perturbation of the measure is only assumed to be differentiable with bounded second
   derivative."
   - Hypothesis (§1): "For general αj, βj, we assume that hj ∈ Ck,1([aj, bj]), k ≥ 1 …".
   - *Differs:* h must be C^{k,1} *up to the endpoint*. A slowly varying edge factor such as log(1/(1−x)) or
     exp √log(1/(1−x)) is not C¹ at the endpoint, so it is excluded.
5. **McLaughlin–Miller**, arXiv:0805.1980v1. Abstract: "orthogonal polynomials with varying weights of the form e^{−NV(x)}
   on the real line, assuming that V has only two Lipschitz continuous derivatives … a new technique of asymptotic
   analysis for matrix Riemann-Hilbert problems with nonanalytic jump matrices".
   - *Differs:* continuous, varying weights; C^{1,1}-type regularity; soft edges. McLaughlin–Miller arXiv:math/0406484
     (unit circle) was downloaded but not quoted.
6. **Kuijlaars–McLaughlin–Van Assche–Vanlessen (KMVV)**, arXiv:math/0111252. Abstract: "a modified Jacobi weight
   (1 − x)^α(1 + x)^β h(x), with α, β > −1 and h real analytic and stricly positive". This is the analytic baseline the
   repo perturbs.
7. **Levin–Lubinsky**, "Asymptotics associated with Exponential Weights" (announcement, 1999; Lubinsky homepage,
   IMRNAsymExpWtsPaper146.pdf).
   - Their Theorem 10, for W = e^{−Q} in the class F(dini) (convex Q, quasi-increasing T = tQ′/Q, a local Dini-type
     condition on Q′): "Let W ∈ F(dini). Then as n → ∞, An/δn − 1/2 = o(1), (Bn − βn)/δn = o(1)", where
     "δt := ½(at + |a−t|); βt := ½(at + a−t)" are built from the Mhaskar–Rakhmanov–Saff numbers. (Fraction bars and Greek
     letters were reconstructed from the garbled extraction.)
   - *Differs:* this is the closest structural analogue. It is an o(1)-without-rate recurrence law with the constant
     taken from an equilibrium problem, no analyticity, and a non-RH proof. But it covers continuous exponential weights
     on (c, d), not discrete measures with accumulating atoms and power-type masses.
8. **Deift–Its–Krasovsky**, arXiv:0905.0443v3, Annals 174 (2011) 1243–1299: §2 below.

**What differs overall.** No opened source treats an RH problem for a *discrete* measure with a non-analytic weight. BKMM
and Bleher–Liechty assume analytic weights (earlier search; Bleher–Liechty arXiv:0909.1985 abstract: "with weight
e^{−NV(x)}" and V real analytic). No source gives a scaled (n^p) recurrence law for a compact Jacobi operator under a
slowly varying perturbation of the spectral weights. The earlier search also found that Nevai-class and
relative-asymptotics tools are vacuous for this problem without the n^p scaling.

**Verdict:** NOT FOUND.

---

## 2. Technique: Route II (RedA reduction + C–D comparison at the Bessel edge): PARTIALLY KNOWN

### 2(b) Conway–Deift comparison with a rate-free mismatch

- **C–D §1** (verbatim): "The main new feature of our analysis is that, for the problem at hand, no local solution is
  needed. The strategy here is to compare the modified Riemann–Hilbert problem above to the corresponding modified
  Riemann–Hilbert problem for the Legendre case. In the standard approach, a comparison is made by examining the quotient
  of solutions to two Riemann–Hilbert problems as the solution to a Riemann–Hilbert problem in its own right. However,
  for the case at hand, the log singularity renders this approach ineffective. Instead we compare the problems through
  the operator theory that underlies Riemann–Hilbert problems".
  - This matches ROUTE2 §2 last paragraph and §6(i) exactly: the quotient argument fails, and the operator comparison
    works.
- **C–D Theorem 4.4** (verbatim, modulo extraction): "Suppose vA, vB ∈ L∞(Σ) and A± solves the RHP: A+(x) = A−(x)vA(x),
  … A± ∈ I + ∂C(Lp(Σ)) … Suppose further that vB^{−1} ∈ L∞(Σ) and B±^{−1} ∈ I + ∂C(Lq(Σ)) where 1/p + 1/q = 1, then …
  AB^{−1} = I + CΣ(A−(vA vB^{−1} − I)B−^{−1})."
- **C–D Theorem 4.7 and its proof** (verbatim): "The operator 1 − CvΣ is uniformly invertible for all sufficiently large
  n. … So it follows from Propositions 2.1 and 2.3 that ‖vΣ − ṽΣ‖L∞(Σ) → 0,".
  - So **"the sup-norm mismatch need only tend to 0, with no rate, for uniform invertibility" is already C–D's
    mechanism.** ROUTE2 Theorem C′ says as much ("C–D Theorem 4.7's Neumann argument (quoted)"). This is not new.
- **C–D's weight is itself a slowly varying edge factor.** log(2k/(1 − x)) = L(1/(1 − x)) with L(t) = log(2kt) slowly
  varying. So "RH with a slowly varying factor at the edge via comparison" has a precedent for one explicit L and the
  α = 0 (Legendre) edge.
- **Deift–Piorkowski §1** (verbatim) on how far C–D's frame extends: "While, an analogous comparison to the Jacobi problem
  with weight function wJac(x) = 1 + x (or something similar) seems suggestive, significant challenges remain due to the
  presence of the simple zero. In particular, the crucial Theorem 4.7 in [4] requires a different proof in this case: now
  one needs to control the behaviour of the Cauchy operator acting on spaces with Muckenhoupt weights."
  - **Relevance for Rule R:** ROUTE2's UR′ extends C–D's uniform resolvent to a Bessel edge of order |α_x| < 1, and
    ROUTE2 §6 records that the frame *fails* at α_x ≥ 1 (GAP-α). That matches Deift–Piorkowski's warning: a simple zero
    is exponent 1.
  - So the claim "UR′ holds for every |α| < 1 by the area estimate plus (b′)" is the step a specialist (Piorkowski,
    Deift) would scrutinize first. It is consistent with, but not covered by, any opened source.
- **Piorkowski 2019** is a *different* parametrix-free route: an a priori L^p estimate rather than a comparison. Quote:
  "provided an a priori estimate for the exact solution of the Riemann–Hilbert problem is known."

**Repo-specific elements not found in the sources:**
- (i) The comparison parametrix is the *exact* KMVV Bessel model of the fixed order α_x, with W̃ := D_w (the Szegő function
  of the full weight). The comparison object is therefore not a second orthogonality problem (C–D use Legendre;
  Deift–Piorkowski use Legendre/Jacobi-type). It is a model RH solution with a lip-only mismatch.
- (ii) Lemma LW1′: the scale-invariant bound |log q_N(x) − log q_N(z)| ≤ ε₁(π + |log(x/|z|)|)/p, which makes the
  mismatch O(ε₁) for an *arbitrary* slowly varying factor.
- (iii) The discrete, accumulating-node frame (WLXZ / RH_px).
- (iv) Proposition D′'s factor 1/N from Bessel localization, giving the law with O(1/n), but not the 1/n coefficient
  (GAP-rate). C–D *do* get the explicit second-order term for their weight.

### 2(a) Analytic approximation, then stability

- **DIK §6.2** (verbatim): "6.2. Extension to smooth V(z). If V(z) is just sufficiently smooth, in particular C∞, on the
  unit circle C so that (1.14) holds for s from zero up to and including some s ≥ 0, we can approximate V(z) by
  trigonometric polynomials V^{(n)}(z) = Σ_{k=−p(n)}^{p(n)} V_k z^k … First, we need to extend the RH analysis of the
  previous sections to symbols which depend on n".
  - Remark 1.7: "Theorem 1.1 as proved by Ehrhardt (and as a consequence, Theorems 1.13, 1.20, 1.25 that we proved below)
    hold for C∞ functions V(z) on the unit circle."
- *Differs:* DIK use an n-dependent analytic approximant and carry it through the RH analysis. RedA uses one n-independent
  entire L₁ and moves the error *outside* RH, through the non-RH stability estimate (iii) (T3-conv with base vΨ₁).
  - The two-step pattern "replace the weight by an analytic one, then control the difference" is standard (DIK; also
    Trogdon's "close-to-analytic" extensions).
  - The specific stability input (the transport bound with Sat_p⁺ head control) is the repo's own and was assessed in
    novelty_G1transport.md.

**Verdict for 2:** PARTIALLY KNOWN.
- Mechanism: C–D (comparison, rate-free sup-norm mismatch) and DIK (analytic approximation).
- Plausibly new: generality of the factor, the Bessel order |α| < 1, the discrete setting, and the W̃ = D_w comparison
  model.

---

## 3. QLP (quantitative hard-edge localization via a Stieltjes-transform bound): NOT FOUND (ingredients KNOWN)

- **Lemma GS** (S_N(z) = −Y₁₁Y₁₂/(Y₁)₁₂ = ∫p_N² dμ/(X − z)) is the classical diagonal Green-function / Weyl-solution
  identity. Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS Math. Surveys Monogr. 72 (author
  PDF jacop.pdf), opened:
  - (2.122): "G+(z, n, m) = ∫_R s(λ, n)s(λ, m)/(λ − z) dρ+(λ)";
  - (1.100): "g(z, n) = G(z, n, n) = u+(z, n)u−(z, n)/W(u−(z), u+(z))", where u+ is the Weyl solution (by (2.121),
    "u+(z, n) = c(z, n)/a(0) − m+(z)s(z, n) = ∫_R s(λ, n)/(z − λ) dρ+(λ)", the function of the second kind).
  - So GS is "Green's function = OP × second-kind function". It is classical and should be labelled KNOWN, citing Teschl
    (or Deift's Courant notes for the Y₁₂ = Cauchy-transform form).
- **Lemma ST** (ν([0, τ]) ≤ (4τ/|cos θ|)|S(τe^{iθ})|) is an elementary positivity bound; no novelty is claimed.
- **QLP itself** (μ_m((Mn, ∞)) ≤ CM^{−p/2} up to M ≍ n^{2/p}, with the exponent change below the Bessel scale, and the
  QL bound Λ_n = O(1) at t = 0): no source found states an index-tail bound for p_m² dμ over atoms near the accumulation
  point of a discrete measure. It is also not found as a method: reading the hard-edge mass off the Green function at
  |z| ≍ τ in the RH outer region, avoiding band asymptotics.
  - The closest analogue (earlier search) is Lubinsky's localization principle (arXiv:math/0701307, Annals 2009). It is a
    different setting: a.c. measures, kernel comparison in x-space.
  - For continuous Jacobi-type weights, the analogous information near the hard edge comes from the Bessel asymptotics
    themselves (KMVV / Vanlessen), not from a Stieltjes bound.
- **Verdict:** NOT FOUND as a statement. The method is a short, natural combination of classical identities with RH outer
  asymptotics; a specialist would call it "standard once stated". Keep "novelty not claimed" for GS and ST.

---

## 4. RedA (smoothing slowly varying sequences to entire functions with strip-uniform derivative decay): PARTIALLY KNOWN

**Real-variable smooth variation: KNOWN (BGT).** BGT was not opened; the quotes below are from opened papers quoting it.
- Eichinger–Winter, arXiv:1703.09140v1, Theorem 4.13 (verbatim): "(cf. [3, Theorem 1.3.3]). Let ℓ ∈ R0. Then there is a
  smoothly varying function ℓ1 ∈ SR0 asymptotically equivalent to ℓ … ℓ1 can be chosen in such a way that all derivatives
  of the function p1 defined by p1(x) := log(ℓ1(e^{−x})), … vanish, i.e., for all n ∈ N, p1^{(n)}(x) → 0, as x → ∞." Here
  [3] = BGT.
- Benaim–Friz, arXiv:math/0608619v1, §2.2 (verbatim): "A positive function g defined in some neighbourhood of ∞ varies
  smoothly with index α, g ∈ SRα, iff h(x) := log(g(e^x)) is C∞ and h′(x) → α, h^{(n)}(x) → 0 for n = 2, 3, ... as
  x → ∞. Theorem 1 (Smooth Variation Theorem, Thm 1.8.2 in [5]) If f ∈ Rα then there exist fi ∈ SRα, i = 1, 2, with
  f1 ∼ f2 and f1 ≤ f ≤ f2 on some neighbourhood of ∞."
- Alouin–Bigot, arXiv:2502.13529v2, Theorem A.2 (verbatim): "(Smooth variation theorem, [BGT89]). Let ρ be a slowly varying
  function. There exist ρ̃1, ρ̃2 slowly varying such that • for any n ⩾ 1 and any i = 1, 2, x^n ρ̃i^{(n)}(x) ρ̃i(x)^{−1}
  −→ 0, • ρ̃1 ∼ ρ̃2 and ρ̃1 ⩽ ρ ⩽ ρ̃2 on a neighborhood of +∞."
- Peša, arXiv:2304.14148v2 (Proc. Edinburgh Math. Soc. 2024), abstract (verbatim): "We show, that every slowly varying
  function of this type is equivalent to a slowly varying function that has continuous classical derivatives of all
  orders." This is a weaker "≈" definition, and only C^∞.
- So RedA(i) plus the real-axis part of (ii) (L₁^{(j)}(τ) → 0, L₁(log k) − log Ψ(k) → 0) is **the smooth variation
  theorem in log-coordinates**.

**Complex-sector analytic slow variation: the notion is KNOWN; the approximation statement is UNVERIFIED.**
- Vuilleumier, "Slowly varying functions in the complex plane", Trans. AMS 218 (1976) 343–348, DOI
  10.1090/S0002-9947-1976-0399479-4. Abstract opened via Crossref (verbatim from the MathML alttext; the inequality signs
  look garbled in the deposited metadata): "Let f be analytic and have no zeros in |arg z| > α ⩽ π; f is called slowly
  varying if, for every λ > 0, f(λz)/f(z) → 1 uniformly in |arg z| ⩽ β > α, when |z| → ∞. One shows that f is slowly
  varying if and only if zf′(z)/f(z) → 0 uniformly in |arg z| ⩽ β > α, when |z| → ∞."
  - With t = e^u, "zf′/f → 0 uniformly in a sector" is exactly "L₁′(u) → 0 uniformly in a horizontal strip", i.e. RedA(ii)
    for j = 1 and hypothesis (H_an)'s ε₁ → 0. **(H_an) is therefore "Ψ₁ is slowly varying in Vuilleumier's sense in the
    sector |arg t| ≤ π/p".**
  - Whether Vuilleumier, or BGT §1.8/§1.11, proves that *every* real slowly varying function is asymptotic to the
    restriction of a sector-analytic one could not be checked (AMS 403; BGT not available). **This is the highest-priority
    read for RedA.**
- **Sequence form.** RedA works with sequences (no measurability; no representation theorem). The classical bridge
  "regularly varying sequences ↔ functions" is Galambos–Seneta, "Regularly varying sequences", Proc. AMS (1973), DOI
  10.1090/s0002-9939-1973-0323963-5 (Crossref metadata only; no abstract; *not opened*). The repo's direct route via the
  piecewise-linear interpolant and the local-oscillation bound ω(τ) ≤ 2δ_m(2e²) avoids it.
- **What RedA adds**, as far as could be checked:
  - an explicit construction (Gaussian convolution in log-coordinates, which gives an *entire* L₁);
  - uniform decay of all derivatives in every horizontal strip;
  - a sequence-form hypothesis only.
  The proof is short and elementary: ∫φ^{(j)}(c − y)dy = 0 for complex c, plus the chaining bound.
- **Verdict:** PARTIALLY KNOWN; very likely KNOWN in substance. Recommend relabelling "PROVED (self-contained); a
  strip-analytic form of the smooth variation theorem (BGT Thm 1.3.3 / 1.8.2; cf. Vuilleumier 1976); novelty not
  claimed".

---

## 5. Suggested references to add (CITATIONS / novelty paragraph)

1. Conway–Deift, SIGMA 14 (2018) 056, arXiv:1711.01590: already cited. Add an explicit sentence saying that Thm 4.7's
   rate-free mismatch is the mechanism used, and that their weight is a slowly varying edge factor.
2. Deift–Piorkowski, SIGMA 20 (2024) 004, arXiv:2307.09277: the k = 1 case and Magnus's conjecture. Its remark on
   Muckenhoupt weights explains why the frame stops at exponent 1 (cf. GAP-α).
3. Piorkowski, arXiv:1910.00564: parametrix-free RH for weights non-analytic at the endpoints. The closest
   continuous-weight competitor.
4. Trogdon, SIGMA 22 (2026) 006, arXiv:2412.18656, and McLaughlin–Miller, arXiv:0805.1980 / math/0406484: ∂̄ methods for
   non-analytic weights (C^{k,1} up to the edge, so not slowly varying edge factors).
5. Deift–Its–Krasovsky, Annals 174 (2011), arXiv:0905.0443, §6.2: analytic approximation of non-analytic symbols in an RH
   analysis.
6. Levin–Lubinsky, *Orthogonal Polynomials for Exponential Weights* (CMS Books, 2001); announcement opened. The o(1)
   recurrence law via MRS numbers, without analyticity: the structural analogue of Law P.
7. Bingham–Goldie–Teugels, *Regular Variation* (CUP 1987), Thm 1.3.3 / 1.8.2, and Vuilleumier, Trans. AMS 218 (1976):
   for RedA.
8. Teschl, *Jacobi Operators …*, (1.99)–(1.100), (2.122): for Lemma GS.

## 6. Seen, not opened (do not cite without reading)

- BGT book: Thm 1.3.3, 1.8.2, §1.9 (sequences), and any analytic-in-a-sector result.
- Vuilleumier 1976 full text (403).
- Galambos–Seneta 1973.
- Lubinsky–Mhaskar–Saff, Constr. Approx. 4 (1988); Kriecherbauer–McLaughlin (Freud weights, IMRN 1999).
- Yattselev (Chebyshev-like non-analytic weights; cited by Trogdon).
- Ou–Wong, Dai–Wong (regular lattices; per earlier search).
- Simić 2007 (entire functions / de Haan class; search snippet only).
- Kuijlaars–Tibboel arXiv:0708.3956; Vanlessen arXiv:math/0504604; Kuijlaars–Vanlessen generalized Jacobi
  arXiv:math/0212014 (titles/snippets only).

## 7. Natural expert readers

- **Percy Deift** (NYU) and **Mateusz Piorkowski** (KU Leuven): the C–D comparison, parametrix-free RH, and the
  uniform-resolvent question for |α| < 1 (UR′). The best-placed readers for Theorem RII.
- **Thomas Trogdon** (UW), **Ken McLaughlin**, **Peter Miller**, **Maxim Yattselev**: non-analytic weights.
- **Arno Kuijlaars**, **Walter Van Assche**: KMVV Bessel edge; compact Jacobi matrices.
- **Doron Lubinsky**, **Eli Levin**: o(1) recurrence laws without analyticity; MRS numbers; the Freud-type framing.
- **Yu-Qiu Zhao**, **Dan Dai**, **Roderick Wong**: discrete RH with accumulating or non-uniform lattices (WLXZ frame).
- **Igor Krasovsky**: Fisher–Hartwig, and analytic approximation of smooth symbols.
- **Nick Bingham** (or Charles Goldie): to confirm whether RedA's strip-analytic smooth variation is in BGT or Vuilleumier.

## 8. Sources opened (IDs)

1. Conway–Deift, arXiv:1711.01590v4, DOI 10.3842/SIGMA.2018.056 (PDF).
2. Deift–Piorkowski, arXiv:2307.09277v2, DOI 10.3842/SIGMA.2024.004 (PDF).
3. Piorkowski, arXiv:1910.00564v2 (PDF).
4. Trogdon, arXiv:2412.18656v5, DOI 10.3842/SIGMA.2026.006 (PDF).
5. McLaughlin–Miller, arXiv:0805.1980v1 (PDF); arXiv:math/0406484 (PDF, not quoted).
6. KMVV, arXiv:math/0111252 (PDF).
7. Deift–Its–Krasovsky, arXiv:0905.0443v3 (PDF).
8. Levin–Lubinsky, "Asymptotics associated with Exponential Weights" (1999 announcement; PDF from
   lubinsky.math.gatech.edu).
9. Teschl, *Jacobi Operators* (author PDF, mat.univie.ac.at/~gerald/ftp/book-jac/jacop.pdf).
10. Eichinger–Winter, arXiv:1703.09140v1 (PDF).
11. Benaim–Friz, arXiv:math/0608619v1 (PDF).
12. Alouin–Bigot, arXiv:2502.13529v2 (PDF).
13. Peša, arXiv:2304.14148v2 (PDF).
14. Vuilleumier 1976: Crossref abstract only, DOI 10.1090/S0002-9947-1976-0399479-4.
15. Wong–Zhao, arXiv:2204.09305 (survey; head only, not quoted).
16. Semantic Scholar citation list of arXiv:1711.01590. It shows five citing works: 2502.02273, 2307.09277, 2204.09305,
    1912.00500, 1910.00564. None is a discrete or slowly varying generalization.

## 9. Search terms

**Web:**
- "Riemann-Hilbert orthogonal polynomials weight with slowly varying factor recurrence coefficients asymptotics
  non-analytic weight"
- "smooth variation … Bingham Goldie Teugels Theorem 1.8.2"
- "McLaughlin Miller dbar … nonanalytic weights recurrence coefficients"
- "slowly varying function asymptotically equivalent analytic function in a sector …"
- "Lubinsky Freud weight multiplied by slowly varying function recurrence coefficients"
- "Riemann-Hilbert discrete orthogonal polynomials non-analytic weight lattice dbar Bleher Liechty"
- "… logarithmic factor at hard edge … Bessel … recurrence coefficients"
- "… weight not analytic at endpoint slowly varying or log log factor Jacobi-type"
- "Deift Its Krasovsky Fisher-Hartwig …"
- "slowly varying … entire function … smooth variation … Gaussian kernel"
- "… slowly varying weight recurrence coefficients Riemann-Hilbert hard edge Bessel parametrix non-analytic factor"
  (extended mode)

**APIs:**
- Semantic Scholar citations of 1711.01590.
- Crossref for Vuilleumier and Galambos–Seneta.
- The arXiv API was attempted with abs:"slowly varying" ∧ Riemann-Hilbert, abs:"orthogonal polynomials" ∧ "slowly varying",
  and abs:"local parametrix", but was rate-limited throughout. **These queries should be rerun.**
