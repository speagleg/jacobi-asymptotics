# Rule L novelty search: G1 Plans 39–45, 49 (LR, RL, R/RW/Ra, B-cond/QL/CB/BF/FM)

Date: 2026-10-14. Searcher: one agent session. Tools: WebSearch, zbMATH Open API (api.zbmath.org), Crossref,
Semantic Scholar and OpenAlex APIs, and direct downloads of arXiv, mp_arc, EMS Press and author-page PDFs into
scratchpad/program/dlLB/. The repo was read-only and was not modified. This file builds on
research/program/novelty_G1transport.md (cited as [T] below), and does not repeat what [T] already settled.

Rule C: every quote below is copied verbatim from a source opened in this session. "Opened" means I read the PDF or
TeX text, or a zbMATH/Crossref record. A **zbMATH review is not the paper**: where only a review was opened, I say so.
Leads I only saw in search snippets are listed in §7 and are not quoted. Scope caveat (as in [T]): this was one
session, not a MathSciNet sweep. Springer, Elsevier (ScienceDirect), AMS (PAMS) and Project Euclid all returned
bot walls or 403 for PDFs. "NOT FOUND" means "not found in what could be opened".

---

## 0. Verdicts

| Result | Verdict | Closest prior work (opened) |
|---|---|---|
| **LR / LR′ / LRa**: linear response with ε² remainder, ε = ½ osc f, any finite-moment measure, absolute constants | **First-order term KNOWN. The explicit uniform second-order bound (Bessel ⇒ \|ΔV_m\| ≤ Var_{μ_m}f ≤ ε², \|Γ_m\| ≤ ε²) is NOT FOUND.** | Fischer, ZAA 17 (1998) Lemmas 4–5: derivatives of recurrence coefficients with respect to any parameter of the functional, and with respect to a single weight of a discrete measure. Basor–Chen–Ehrhardt (Toda) and Breuer–Duits (3.7) (variance), both in [T] |
| **RL** (Law P ⟺ rescaled μ_n → arcsine, plus an a priori bound; moments 1, 2, 4) | **PARTIALLY KNOWN.** It is the fixed-scale theorem of Simon 2004 (Thm 3.2; for bounded support, Thm 1.x "p_n² dμ has a weak limit iff …"), transcribed to n-dependent scales s_n. The repo already disclaims novelty for RL and RL-b. **RL-loc, RL-n, RL-n2 (which indices suffice) and the a-priori-bound clause for unbounded rescaled support: NOT FOUND** | Simon, JAT 126 (2004), mp_arc 03-341 (TeX); Erb, arXiv:1803.05583 (restates Nevai 1979 Thm 14 and Simon's converse); Van Assche 1995 (forward, varying measures; in [T]) |
| **Theorem R / RW / Ra** (fixed-size bounded rough weights e^f, \|f\| ≤ ε, break pointwise ratio-type asymptotics of a_n, b_n for compact Jacobi operators; window form) | **NOT FOUND.** **Knopfmacher–Lubinsky–Nevai 1988 does not anticipate it**: by its zbMATH review it is a *sufficient* condition for Freud-type limits for weights on ℝ, with no counterexample (§3.1). In the bounded-support literature the known phenomena go the other way: discrete and singular measures *can* be in the Nevai class (Van Assche–Magnus 1989; Totik 1992), and a.c. measures with μ′ > 0 a.e. always are (Rakhmanov) | KLN 1988 (zbMATH review only); Totik, PAMS 114 (1992) (zbMATH review); Van Assche–Magnus, PAMS 106 (1989) (zbMATH summary); LMS 1988 (zbMATH review); Remling (in [T]) |
| **B-cond / QL / CB / BF / RF / FM / DB** | **NOT FOUND** (quick check). Ingredients are standard: BF(i)–(ii) is a weighted version of the determinantal "boundary" form of the number variance, and FM's Clausen function is an ordinary Fourier sum | Breuer–Duits (3.7) (in [T]); no source found for the commutator/flux identities as stated |
| **Plan 43 (G3′ ⇒ 100% simple and critical)** | **Skipped** (out of scope for a G1 search; see novelty_G3p.md) | — |

**Knopfmacher–Lubinsky–Nevai 1988: the full text was NOT read.** It is closed access (Springer bot wall; Unpaywall and
OpenAlex report "closed" with no repository copy). It is not hosted on Nevai's or Lubinsky's pages. I did open two
records: its **zbMATH review** (Zbl 0646.41002, reviewer L. Ciobanu), which states the main theorem, and its
**Crossref reference list**. §3.1 has what they say.

---

## 1. Lemma LR / LR′ / LRa (G1 §3.11, Plan 40)

**Verdict.** The first-order formulas are **KNOWN**: L_n^v(f) is FV, and the Lax/Toda form of a_n′ is the Toda
hierarchy. The repo already calls these standard. **The new content is the second-order control: an absolute,
measure-independent bound |second derivative| ≤ Var_{μ_n}f + Var_{μ_{n−1}}f ≤ 2ε², and |ä_n| ≤ ε²(b_n + b_{n+1}),
proved with Bessel's inequality. I did NOT FIND this, or any explicit remainder estimate for Jacobi parameters under
multiplicative perturbations e^{tf}dμ.**

### 1.1 New source this session: Fischer 1998 (first variation in full generality)

H.-J. Fischer, "On Generating Orthogonal Polynomials for Discrete Measures", Z. Anal. Anwend. (J. Anal. Appl.)
17 (1998), No. 1, 183–205. Opened as a PDF from ems.press (serial-article-files/34971); the text is OCR, so quotes are
of the prose only. Abstract:
> "The numerical condition of the problem as well as the stability properties of the new algorithm and of the
> well-known Stieltjes-procedure are investigated."

§4:
> "In this section we investigate the sensitivity of the map H : [...] from the nodes and weights of a discrete
> measure [...] to the recurrence coefficients b = b(a)."

> "Lemma 4. Let l be some positive linear functional on P_{2n−1}, differentiably depending on some parameter t, [...]
> The partial derivatives of the recursion coefficients with respect to t are [(20), (21)]"

His Lemma 5 then gives "the partial derivatives of the coefficients α_j and β_j with respect to a single node or
weight". In monic normalisation, (26) reads ∂β_j/∂λ = β_j[γ_j²p_j(τ)² − γ_{j−1}²p_{j−1}(τ)²] (my transcription of
the OCR). This is FV for f = δ_τ, i.e. the atom-by-atom form of d log b_n² = ⟨f, μ_n − μ_{n−1}⟩. On the history he
writes:
> "Unfortunately, his formulas were partially erroneous, and Gautschi corrected his statement in [9: Note added in
> proof]. But for all we know no correct estimates of the sensitivity of the map H_n appeared in the literature."

and, on the method:
> "Remark. The idea of this proof is not new. In the article [5] we analyzed the dependence on modified moments with
> essentially the same method"

**Differs.** Fischer has **first derivatives only**, and uses them for condition numbers (operator norms of the
Jacobian, bounded "by a polynomial in n and N"). He has no second-variation bound, no ε² remainder, and no
measure-independent constants.

### 1.2 Already in [T] (not re-opened)
- Toda form for f = x: Basor–Chen–Ehrhardt arXiv:0905.2620 §2, "This is not a new result."
- The variance formula behind ΔV_m = V_{m+1} − V_m: Breuer–Duits arXiv:1309.6224 (3.7). I re-opened it this session
  (bd_1309.6224.txt) to look for a bound on variance increments. Their main tool is right limits (Theorem 2.4, "for
  any polynomial f, we have lim E exp z X_f^{(n_j)} − … "). **I found no inequality of the form
  |Var_{n+1} − Var_n| ≤ Var_{μ_n}(f) there.**
- Lax form for multi-time Toda deformations (matrix case): Deaño–Eijsvoogel–Román, arXiv:1907.07447v1, abstract/§1:
  > "For the particular case of a multi-time Toda deformation, we give a Lax pair formulation"

  It covers polynomial deformations v(x, t) only, with no remainder bounds.

### 1.3 Assessment and positioning
- Cite Fischer 1998 Lemma 4/5 (and the Toda-hierarchy literature) for FV/FVa. Fischer's Lemma 4 is the general
  "functional depending on a parameter" statement.
- The **identity** ΔV_m = Var_{μ_m}(f) − 2‖K_m(fq_m)‖² (variance increment = one-point variance minus twice the
  projected part) is elementary but was **not found** stated. The **bounds** |ΔV_m| ≤ Var_{μ_m}f and |Γ_m| ≤ ε², which
  give the ε² remainders with absolute constants for *every* finite-moment measure, were also **not found**. Possibly
  new; modest. The natural framing is "a second-order (Hessian) bound for the Toda-hierarchy flow along e^{tf}dμ,
  uniform in n and in μ".
- The numerically sharp constants (C = 1, 2, e^ε − 1 − ε) had nothing to compare against.

## 2. Lemma RL and RL-loc / RL-n / RL-n2 (G1 §3.13, Plan 42)

**Verdict.** **RL itself: PARTIALLY KNOWN.** It is Simon 2004 Theorem 3.2 plus the forward Nevai/Van Assche
direction, carried over to scales s_n with s_{n+1}/s_n → 1. The repo already disclaims novelty for RL and RL-b, and
this search confirms that is right. **The (c′) clause (an a priori bound replacing bounded support), RL-loc
(three indices n − 1, n, n + 1 suffice for right limits), and RL-n/RL-n2 (one or two indices do not): NOT FOUND.**

- Simon, "Ratio asymptotics and weak asymptotic measures for orthogonal polynomials on the real line", JAT 126
  (2004); mp_arc 03-341, TeX source opened (simon_ratios.TEX). Abstract:
  > "For $\mu$'s with bounded support, we prove $p_n^2\, d\mu$ has a weak limit if and only if $\lim b_n$, $\lim
  > a_{2n}$, and $\lim a_{2n+1}$ all exist. In both cases, we write down the limits explicitly."

  Theorem 3.2 is quoted in [T] §4. **Differs:** the measure is fixed, μ_n is not rescaled, and bounded support makes
  the a priori bound automatic. RL is for measures that vary with n (images under x ↦ s_nx) with possibly unbounded
  rescaled support, which is why (c′) needs the explicit bound sup s_n(|a_n| + b_n) < ∞. In Simon's setting the
  period-2 limit ρ_{b;a,c} can occur. In RL the target is the arcsine law, so a = c is forced.
- Erb, "Weak limits for weighted means of orthogonal polynomials", arXiv:1803.05583v1, §1. It restates Nevai's
  forward theorem and Simon's converse:
  > "Theorem 1 (Nevai 1979, [13]). Let µ be a measure in the Nevai class M (a, b) with b > 0. If f is µ-measurable,
  > bounded on supp(µ) and Riemann integrable on [−2b + a, a + 2b], then [(1)]"

  > "In [17], also a converse statement is shown, namely that if supp(µ) is bounded and (1) holds true for all
  > continuous functions f on supp(µ) then µ is in the Nevai class M (a, b)."

  ([17] = Simon JAT 2004.) Erb's own "uniform/mean Nevai classes" are for **families** μ^{(k)}, but in the forward
  direction only (means of p_n² dμ^{(k)} → equilibrium measure). **Differs:** there is no converse for varying
  measures and no rescaling.
- Forward direction for varying measures: Van Assche 1995 (math/9401209), quoted in [T] §4.
- **Search for a converse with unbounded or regularly varying coefficients** ("rescaled weak limit of p_n² dμ ⇒ a_n/c_n
  converges"): nothing found. The Freud-weight literature (LMS 1988, §3.2) goes from weight to coefficients by
  extremal problems, not through weak limits of p_n² dμ.
- **Suggested citations:** Simon 2004 Thm 3.2 (method), Nevai 1979 Memoir Thm 14 (via Erb's statement; Memoir not
  opened), Van Assche 1995. Claim novelty only for RL-loc/RL-n/RL-n2 and the bound clause, and keep the claim
  modest: they are short consequences of the same path-counting.

## 3. Theorem R, RW, Ra (G1 §§3.6, 3.10, 3.12; Plans 33, 39, 41)

**Verdict: NOT FOUND.** No source was found with a construction of bounded multiplicative perturbations e^f,
|f| ≤ ε, of a fixed (here pure-point, compact-J) measure that destroy pointwise ratio-type asymptotics of a_n or b_n
while averaged laws survive. The Knopfmacher–Lubinsky–Nevai lead from [T] is resolved below: it is a sufficiency
theorem, not a counterexample.

### 3.1 Knopfmacher–Lubinsky–Nevai 1988: what could be obtained

A. Knopfmacher, D. S. Lubinsky, P. Nevai, "Freud's conjecture and approximation of reciprocals of weights by
polynomials", Constr. Approx. 4 (1988) 9–20, DOI 10.1007/BF02075446, MR 89e:42016, Zbl 0646.41002. An earlier version
is NRIMS Technical Report TWISK 473, CSIR Pretoria, 1986, 24 pp. (from Nevai's publication list, item 95a, opened at
people.math.osu.edu/nevai.1/MYMATH/paul_nevai_publ.pdf).

**Attempts to get the full text** (all failed): Springer article and PDF links (bot wall / 303 to idp.springer.com);
Semantic Scholar ("openAccessPdf": status "CLOSED", abstract "elided by the publisher"); OpenAlex
(`'is_oa': False, 'oa_status': 'closed', … 'any_repository_has_fulltext': False`); scholar.archive.org (no hit);
Nevai's directory MYMATH/PUBLICATIONS (two unrelated files only); Lubinsky's SelectedPapers page (papers 137–2025;
nothing from 1988). Citing works with open copies (Lubinsky–Saff RMJM 19 (1989), Project Euclid) returned HTML, not
PDF. JAT/JCAM citing papers on ScienceDirect returned 403.

**zbMATH review (opened; Zbl 0646.41002, reviewer L. Ciobanu), verbatim except that TeX is rendered and the review's
own dropped constants are marked [sic]:**
> "Let w(x) be the weight function, nonnegative in ℝ, positive on a set of positive measure, such that all the
> powers of moments of w(x) […] are finite. […] If there exist an increasing sequence of positive numbers {c_n} and
> a decreasing sequence of positive numbers {δ_n}, such that lim δ_n = 0, ‖PW‖_{L_2(ℝ)} ≤ (1+δ_n)‖PW‖_{L_2(−c_n,c_n)},
> for n ∈ ℕ and P ∈ 𝒫_n, and if there exist the polynomials s_{n−2} ∈ 𝒫_{n−2} with n ≥ 2, such that
> lim_{n→∞} (1/π)∫_{−1}^{1} |w(c_nx)s_{n−2}(x)(1−x²)^{1/4}|^p dx/√(1−x²) = 1 for p= [sic] and p=2. Then
> lim_{n→∞} α_n/c_n= [sic] and lim β_n/c_{n+1}=0. As a special case, we obtain a sufficient condition for Freud's
> conjecture with weights on ℝ."

(The garbled constants are presumably p = 1 and α_n/c_n → ½; I have **not verified** this against the paper.)

**Crossref reference list (opened).** It includes Freud 1976 ("On the coefficients in the recursion formulae of
orthogonal polynomials"), López Lagomasino 1985 (ratio asymptotics), Máté–Nevai–Totik 1985 ("Asymptotics for the
ratio of leading coefficients of orthogonal polynomials on the unit circle"), Rahmanov 1983 ("On the asymptotics of
the ratio of orthogonal polynomials, II"), LMS 1986/1988, Magnus 1986, Mhaskar–Saff 1984/85, and Nevai 1979/1986.

**What it says, as far as can be verified.** KLN give a *sufficient* condition for Freud-type recurrence asymptotics
(α_n/c_n → const, β_n/c_n → 0) for **absolutely continuous weights on ℝ** (unbounded J). The condition has two parts:
(i) the L₂ norm of weighted polynomials lives on [−c_n, c_n] up to 1 + δ_n; (ii) the rescaled weight w(c_n·) is
approximable, in an L^p(arcsine) sense with constant exactly 1, by reciprocals of polynomials of degree n − 2. Its
references point to the ratio-asymptotics/extremal-problem method (Máté–Nevai–Totik, Rakhmanov). Nothing in the review
or the reference list suggests a counterexample, a failure under bounded factors, or discrete measures.

**Bearing on Theorem R.** KLN is a positive-direction sufficiency theorem in the a.c./Freud setting. It does
**not** anticipate R/RW/Ra. One possible structural parallel: KLN's hypothesis (ii) asks that the weight look
"polynomial-reciprocal-like at scale c_n". Theorem R's rough e^f defeats the analogous local regularity at the index
scale. This is my analogy, not a statement in KLN. **Before publishing, the paper itself should still be read** (a
library copy, or MR 89e:42016) to check for remarks on necessity.

### 3.2 Other opened sources on stability/instability of recurrence limits
- **Lubinsky–Mhaskar–Saff**, Constr. Approx. 4 (1988) 65–83, DOI 10.1007/BF02075448, Zbl 0653.42024. zbMATH review
  opened, not the paper:
  > "When W(x)=w(x)exp(−Q(x)), x∈(−∞,∞), where w(x) is a ``generalized Jacobi factor'', and Q(x) satisfies various
  > restrictions, we show that lim_{n→∞}A_n/a_n= [sic] and lim_{n→∞}B_n/a_n=0"

  This is the Freud analog of **stability under a structured (generalized Jacobi) factor**, i.e. the analog of
  T3-all, not of R. **Differs:** a.c. weights on ℝ; the factor is explicit and piecewise analytic, not rough.
- **Knopfmacher–Lubinsky**, "Analogues of Freud's conjecture for Erdős type weights …", LNM 1287 (1987) 21–69,
  DOI 10.1007/bfb0078897, zbMATH 0638.41009 (review opened): "Here we obtain asymptotics for the associated
  recurrence relation coefficients, analogous to those obtained recently for weights such as exp(−|x|^α)". Positive
  results only.
- **Van Assche–Magnus**, "Sieved orthogonal polynomials and discrete measures with jumps dense in an interval",
  PAMS 106 (1989) 163–173, DOI 10.2307/2047388, Zbl 0681.42016. zbMATH summary opened:
  > "These polynomials are then used to give a proof, using only orthogonal polynomials on [-1,1], that the discrete
  > orthogonal polynomials introduced by Lubinsky have converging recurrence coefficients. We construct similar
  > discrete measures with jumps dense in [-1,1] and use sieved ultraspherical polynomials to show that their
  > recurrence coefficients converge."
- **Totik**, "Orthogonal polynomials with ratio asymptotics", PAMS 114 (1992) 491–495, DOI 10.2307/2159673,
  Zbl 0741.42015. Review by W. Van Assche opened:
  > "A result by E. A. Rakhmanov shows that μ′>0 almost everywhere on T (or [−1,1]) implies that μ∈M (or M(0,1)).
  > This seems to suggest that absolute continuity is a desired property for the classes M and M(0,1), but some
  > authors have constructed examples of discrete and singular continuous measures in M or M(0,1). The present paper
  > gives a very flexible construction of measures in the class M with certain prescribed properties."

  **Differs:** these are constructions of pure-point and singular measures **in** the Nevai class (unscaled, ess spec
  an interval). Theorem R goes the other way: a *fixed* pure-point measure whose n^p-scaled limits are destroyed by a
  bounded factor. Together they show that for pure-point measures, membership in a "limit class" is neither forced
  (R) nor excluded (Totik, Van Assche–Magnus). This is consistent with R and does not anticipate it.
- Remling (in [T]): "In general, both assumptions of the DR Theorem are needed." Same remark as [T].

### 3.3 Assessment
- R/RW/Ra remain **NOT FOUND**. RW's window form (a fixed window [aN, bN], admissibility b > u_s(p), explicit η_W,
  ε₀) and Ra's a-half (Toda-form non-degeneracy) were not seen anywhere.
- The mechanism is "Δ²μ_m non-degenerate on a window ⇒ a signed tilt moves F_m by ≍ ε". It is a quantitative
  contrapositive of Simon's Theorem 3.2 combined with linear response (LR′). This is a natural route, but no source
  was found carrying it out.
- **Suggested positioning:** "In the bounded-support theory, pure-point measures can be in the Nevai class (Lubinsky;
  Van Assche–Magnus; Totik). In the Freud theory, structured factors are harmless (LMS; KLN give sufficient
  conditions). We show that for compact Jacobi operators with power-law spectrum, *bounded rough* factors of any fixed
  size can destroy pointwise scaled asymptotics, while slowly varying factors cannot (T3-all, B_all)."

## 4. B-cond / QL / QL-CB / CB / BF / RF / FM / DB / NO (G1 §§3.14, 3.15, 3.18) — quick check

**Verdict: NOT FOUND.** These are tools internal to the repo's transport method. Spot checks:
- **BF(i)–(ii)** (commutator and TV derivative as fluxes Σ_{A×A^c}). The unweighted special case is the standard
  determinantal fact that variance is a boundary sum of K². Breuer–Duits (3.7) (quoted in [T]) is the opened
  instance. **Differs:** BF has a single-index weight q_m(k)q_m(l), the kernel K_m + K_{m+1}, and a
  Christoffel–Darboux form with the Toda density ψ (BF(iii)). Not found.
- **FM** (free/Toeplitz model: commutator = ½ covariance exactly; X/μ(A) = (ε/p)Cl₂(φ)/φ). A search for Clausen
  functions in Toeplitz/projection covariance turned up only unrelated variance identities (arXiv 2604.17150 seen in
  search results, not opened). Cl₂ is a standard Fourier sum, so this is a computation, not a citable result.
- **Lemma NO** (Nishida–Ovsyannikov-type comparison in a scale): attribution only; the repo already claims no
  novelty. Not searched further.
- **QL / CB as hypotheses:** no counterpart found. Any novelty would be in QL-CB/B-OD as conditional reductions, which
  Plans 48–54 have since superseded for the law itself.

## 5. Plan 43 (G3′ ⇒ 100% simple and on the critical line)

Skipped: number-theoretic positioning, outside this G1 search. See research/program/novelty_G3p.md.

## 6. Sources opened this session (with IDs)

1. Fischer, Z. Anal. Anwend. 17 (1998) 183–205 (EMS Press PDF, ems.press/content/serial-article-files/34971).
2. zbMATH Zbl 0646.41002, review of Knopfmacher–Lubinsky–Nevai, Constr. Approx. 4 (1988) 9–20,
   DOI 10.1007/BF02075446.
3. Crossref record (reference list) for DOI 10.1007/BF02075446. Semantic Scholar and OpenAlex records for the same
   (open-access status and citing works).
4. Nevai publication list (people.math.osu.edu/nevai.1/MYMATH/paul_nevai_publ.pdf), items 95a/95b.
5. zbMATH Zbl 0653.42024 (review of LMS 1988, DOI 10.1007/BF02075448).
6. zbMATH Zbl 0638.41009 (review of Knopfmacher–Lubinsky, LNM 1287, DOI 10.1007/bfb0078897).
7. zbMATH Zbl 0681.42016 (summary of Van Assche–Magnus, PAMS 106 (1989), DOI 10.2307/2047388).
8. zbMATH Zbl 0741.42015 (review of Totik, PAMS 114 (1992), DOI 10.2307/2159673).
9. zbMATH Zbl 0799.42013 (review of Lubinsky, Acta Appl. Math. 33 (1993), DOI 10.1007/BF00995486). It confirms the
   survey's scope only; no quote used.
10. Simon, mp_arc 03-341 (TeX source, re-opened).
11. Erb, arXiv:1803.05583v1 (PDF).
12. Breuer–Duits, arXiv:1309.6224v2 and arXiv:1301.2061v2 (PDFs; 1301.2061 abstract only).
13. Deaño–Eijsvoogel–Román, arXiv:1907.07447v1 (PDF).
14. Lubinsky, "A Survey of Weighted Polynomial Approximation with Exponential Weights" (2007), author PDF. Its
    abstract says it does not discuss "the asymptotics of orthogonal polynomials"; not relevant.
15. Levin–Lubinsky, "On recurrence coefficients for rapidly decreasing exponential weights" (author PDF, paper 194).
    Does not cite KLN; not relevant.

## 7. Seen but not opened (do not cite without reading)
- KLN 1988 full text; TWISK 473 (1986).
- Lubinsky–Saff, "Sufficient conditions for asymptotics associated with weighted extremal problems on ℝ", RMJM 19
  (1989) 261–270 (cites KLN; zbMATH has no review text; Project Euclid PDF blocked).
- Lubinsky, "An update on orthogonal polynomials and weighted approximation on the real line", Acta Appl. Math. 33
  (1993) (cites KLN).
- Bello Hernández–López Lagomasino, "Ratio and relative asymptotics of polynomials orthogonal on an arc of the unit
  circle", JAT (1998), DOI 10.1006/jath.1997.3126 (cites KLN; ScienceDirect 403).
- Lubinsky, "singularly continuous measures in Nevai's class" (the reviewer's lead; not located in zbMATH under that
  title search).
- Nevai, Memoirs AMS 213 (1979), Thm 14 (known only via Erb).
- Denisov, PAMS 132 (2004) (convex-combination trick; AMS 403).
- Gautschi's condition-number papers (Fischer's refs [7]–[9]).

## 8. Search terms used
WebSearch: KLN title; "Knopfmacher, Lubinsky and Nevai" recurrence coefficients; Freud's conjecture
counterexample/ratio non-convergence; "weak asymptotic measure" rescaled converse arcsine; discrete measure Nevai
class not preserved under bounded multipliers; Totik equivalent measure Nevai class; Gautschi condition of the map
weights → recurrence coefficients; recurrence coefficients e^{tf} second derivative variance linear response; Toda
hierarchy Lax f(J)_±; Jacobi parameters multiplicative perturbation remainder; Clausen function Toeplitz covariance.
zbMATH API: ti:"ratio asymptotics" & au:Totik; ti:"jumps dense" & au:"Van Assche"; ti:"Nevai class" & ti:singular;
the LMS, Knopfmacher–Lubinsky, Lubinsky 1993 and Lubinsky–Saff titles; several queries returned nothing (404).
**Suggested next terms:** MathSciNet MR 89e:42016 review text; "relative asymptotics" Máté–Nevai–Totik "bounded
weight"; "Hessian of Hankel determinant" / "second variation Toda flow"; "pure point spectrum" "Nevai class"
"multiplicative perturbation"; Simon, *Szegő's Theorem and Its Descendants*, chapter on weak limits/right limits.
