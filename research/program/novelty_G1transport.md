# Rule L novelty search: G1 weight-transport results (G1 PROOF.md §§3.1–3.9)

Date: 2026-10-14. Searcher: one agent session, WebSearch plus direct downloads of arXiv PDFs, abstract pages and
TeX sources into scratchpad/program/dl/. The repo was read-only and was not modified. Rule C: every quote below
is copied verbatim from a source opened in this session (PDF text via pdftotext, TeX source, or arXiv/Crossref
metadata). Sources I could not open are listed separately as **unverified leads** and are not quoted.

Caveat on scope: this is one session of searching, not an exhaustive MathSciNet sweep. Paywalled 1980s–90s
Constructive Approximation and J. Approx. Theory papers could not be opened (Springer and AMS returned 303/403). A
"NOT FOUND" below means "not found in what could be opened", not "proved new".

---

## 0. Summary of verdicts

| Result | Verdict | Closest prior work (opened) |
|---|---|---|
| **CL / A4′** (tail-Cesàro a-law, rough weights, k^{−p}, p > 1) | **NOT FOUND** (ingredients standard) | BKMM math/0212149 (upper constraint, saturated regions; analytic weights only); Dimitrov–Zhang EJP 2023 (LDP, discrete β-ensembles); Johansson math/9903134 |
| **FV, FVa** (first variation) | **KNOWN** (repo already claims no novelty) | Toda equations: Basor–Chen–Ehrhardt arXiv:0905.2620 ("This is not a new result"); variance formula: Breuer–Duits arXiv:1309.6224 eq. (3.7) |
| **TV** (derivative of a tail mass μ_m(A) via K_m) | **PARTIALLY KNOWN**: the formula is an elementary Gram–Schmidt perturbation; using it for **Grönwall transport of localization along a tilting path was NOT FOUND** | Lubinsky arXiv:math/0701307 (Annals 2009): localization/comparison inequality for μ ≤ μ* |
| **LP** (rescaled p_n² dσ → arcsine on [0, 4c(p)]) | **KNOWN** once the pure-power law is known. It is a direct instance of Van Assche 1994 (math/9401209) and of Nevai 1979 / Simon 2004 Thm 3.1. The only new input is the pure-power Law P (RH_p etc.) | Van Assche, Indag. Math. 1995; Simon, JAT 2004 (mp_arc 03-341) |
| **Theorem L** (localization at scale Mn, uniform along the path) | **NOT FOUND** | Lubinsky 2009 localization principle (a different setting: a.c. measures, Christoffel functions on [−1,1]) |
| **T3-all, T3-log** (pointwise Law P for k^{−s}Ψ, Ψ slowly varying / log-type) | **NOT FOUND** | Nevai-class stability (Rakhmanov, Denisov) needs a.c. spectrum, so it does not apply; relative ratio asymptotics (Simanek 2017) are vacuous here without the n^p scaling; BKMM-type RH analysis needs analytic weights |
| **Theorem R + dichotomy** | **NOT FOUND** as a statement. Partially anticipated in spirit: fine recurrence asymptotics need regularity hypotheses beyond what is imposed | Remling arXiv:1006.2780 on the necessity of both DR hypotheses; Simon 2004 Thm 3.2 (weak limits of p_n² dμ pin down the parameters). Unverified lead: Knopfmacher–Lubinsky–Nevai 1988 |
| **TL / TLw** (polynomial tail localization) | **KNOWN technique** (Christoffel extremal property + Markov + Chebyshev extrapolation). The statement was not searched as a theorem; it is not worth a novelty claim | Textbook. Not verified against a specific source in this session |
| **TC / T3-avg** (density-one law) | **NOT FOUND** as a statement. Cesàro ⇒ density-one is standard (Koopman–von Neumann). Superseded by T3-all | — |
| **"Inverse spectral" framing** (spectrum + weights ⇒ entry asymptotics) | The **direction is well studied** in other regimes (Stieltjes/Krein, Killip–Simon, Denisov–Rakhmanov, Freud's conjecture). For compact J with power-law eigenvalues, **no quantitative "entries ~ c(p)·eigenvalue" theorem was found** | Van Assche math/9510214; Killip–Simon math-ph/0112008; Remling 1006.2780; Van Assche math/0512358 (Freud's conjecture history) |

Recommended positioning: the transport technique (FV/FVa + Sat_p⁺ head + TV/Grönwall localization, Theorem L) and its
consequences (T3-all, T3-log, Theorem R and the dichotomy) are **possibly new**. The cleanest framing is "a Freud-type
conjecture for compact Jacobi operators with pure-point spectrum, and its stability under weight perturbations".
Lemmas FV, FVa and LP are known or standard and should be cited as such. CL is possibly new as a statement, but its
method is the standard discrete-Coulomb-gas pattern.

---

## 1. Theorem CL / Corollary A4′ (§3.1)

**Verdict: NOT FOUND.** No source was found that proves a trace-tail (tail-Cesàro) law Σ_{j≥n}a_j ~ (2c/(p−1))n^{1−p}
for discrete measures on nodes k^{−p}, with or without rough weights. Each ingredient is standard.

- **Heine/trace identity (A2).** Classical; not searched.
- **Upper constraint / saturated region.** This is the key structure behind Lemma Sat_p. BKMM, arXiv:math/0212149
  (announcement), abstract and §2:
  > "The key new feature contributed by discreteness is the appearance of the upper constraint on the equilibrium
  > measure (i.e. the upper bound in (17))."

  Their hypotheses are analytic, not rough:
  > "The density function ρ0 (x) is real analytic in a complex neighborhood of the closed interval [a, b]"
  > "we assume that for each sufficiently large N , VN (x) may be taken to be a real analytic function"

  **Differs:** BKMM need analytic node density and analytic weights on a bounded interval, with finitely many nodes.
  CL has infinitely many nodes k^{−p} accumulating at 0, arbitrary rough weights (only Σw < ∞, w_k ≥ c₁k^{−s}), and an
  exponential saturation bound (Sat_p) obtained from a Christoffel/Lagrange test polynomial rather than from RH
  analysis.
- **LDP for discrete ensembles (Lemma WC).** Dimitrov–Zhang, "A global large deviation principle for discrete
  β-ensembles", Electron. J. Probab. 28 (2023), DOI 10.1214/23-EJP977. The abstract, from Crossref:
  > "We consider discrete β-ensembles, as introduced by Borodin, Gorin and Guionnet … Under general assumptions, we
  > establish a large deviation principle for the empirical (or spectral) measures corresponding to these models."

  **Differs:** their ensembles are on shifted lattices with interaction log|ℓ_i − ℓ_j|. The repo's Heine ensemble has
  interaction log|k^{−p} − l^{−p}| in the index variable u = k/n, and G2's constrained functional. WC is a speed-n²
  upper bound for that specific functional, not a full LDP. The pattern is standard. Johansson, "Shape fluctuations
  and random matrices", CMP (DOI 10.1007/s002200050027), arXiv:math/9903134, is an early discrete-Coulomb-gas
  large-deviation instance (abstract opened only; not checked in detail).
- **Suggested references:** BKMM (already in G1 CITATIONS.md); Dimitrov–Zhang 2023; Rakhmanov 1996 and Dragnev–Saff 1997
  (constrained equilibrium for discrete OPs; not opened, see §9).

## 2. Lemmas FV, FVa (first variation) and the projection/variance machinery (§§3.2, 3.5, 3.6 R2)

**Verdict: KNOWN.** The repo already says "standard; novelty not claimed".

- Basor–Chen–Ehrhardt, "Painlevé V and time dependent Jacobi polynomials", arXiv:0905.2620v1, §2:
  > "The purpose of this section is to derive two coupled Toda equations that involve the recursion coefficients of the
  > time-dependent Jacobi polynomials. This is not a new result."
  > "(log hn )′ = −αn , … and since βn = hn /hn−1 , we have the first Toda equation, βn′ = (αn−1 − αn )βn ."

  This is FV for f = −x, which the repo uses as its Toda sanity check. The general-f version of
  d/dt log h_n = ⟨f, p_n² dμ⟩ is the "Toda hierarchy" generalization they cite (their refs [23], [30], [37]).
- The variance/two-point formula behind FVa step 3 and R2 is in Breuer–Duits, "Central Limit Theorems for Biorthogonal
  Ensembles and Asymptotics of Recurrence Coefficients", arXiv:1309.6224v2, eq. (3.7):
  > "By the reproducing property, ( Kn (x, y)Kn (y, x)dµ(y) = Kn (x, x)), we can rewrite the latter in the following way
  > … Var Xf = ½ ∬ (f (x) − f (y))2 Kn (x, y)Kn (y, x)dµ(x)dµ(y). (3.7)"

  Breuer–Duits also express OPE fluctuations through right limits of the recurrence matrix. This is a close conceptual
  relative of R1's local free-Jacobi-limit argument.
- **Suggested citation:** Breuer–Duits (3.7) for the covariance formula; any Toda-flow reference for FV (Basor–Chen–
  Ehrhardt §2 as an opened instance).

## 3. Lemma TV and the Grönwall transport (§3.8)

**Verdict: PARTIALLY KNOWN.** The derivative formula is an elementary consequence of Gram–Schmidt and is unlikely to be
new. **Using it to transport index-scale localization of p_n² dμ along the tilting path w·Ψ^t, with a Grönwall bound
on √μ_m(A), was NOT FOUND.**

- **Closest analog:** Lubinsky, "A new approach to universality limits involving orthogonal polynomials", Annals 170
  (2009) 915–939, arXiv:math/0701307v1, §1:
  > "The most important new idea in this paper is a localization principle for universality. … Suppose that µ, µ∗ are
  > measures with µ ≤ µ∗ in [−1, 1]. Then for x, y ∈ [−1, 1], |Kn (x, y) − Kn∗ (x, y)| /Kn (x, x) ≤ …"

  followed by a bound in terms of Christoffel-function ratios, and:
  > "Observe that on the right-hand side, we have only Christoffel functions, and their asymptotics are very well
  > understood."
- **Differs:** Lubinsky compares reproducing kernels of two *ordered* measures (μ ≤ μ*) in x-space, for measures with an
  a.c. part, to get universality. TV/Theorem L compare *comparable* (sandwiched) discrete measures through a continuous
  path. They control the *index-space* tail of a single p_m² dμ (mass beyond Mn), and the gain of a factor n over
  ensemble counts comes from the projection structure (remark L2). I found no source doing this.

## 4. Lemma LP (§3.8)

**Verdict: KNOWN.** Given the pure-power law, LP is a direct corollary of a published theorem. The repo's
"novelty not claimed" is correct. LP could cite the theorem below instead of the textbook method of moments.

- Van Assche, "Weak convergence of orthogonal polynomials", Indag. Math. 6 (1995) 7–23, DOI 10.1016/0019-3577(95)98197-j,
  arXiv:math/9401209v1. Abstract:
  > "The weak convergence of orthogonal polynomials is given under conditions on the asymptotic behaviour of the
  > coefficients in the three-term recurrence relation."

  Main Theorem (§1), for a family of measures μ_n:
  > "Suppose that the recurrence coefficients in (1.2) satisfy (1.3) lim an+k,n = a0k > 0, lim bn+k,n = b0k ∈ R for every
  > k ∈ Z. Then lim ∫ f (x)pn+k (x; µn )pn+l (x; µn ) dµn (x) = … for every polynomial f . Here µ is the spectral matrix of
  > measures for the doubly infinite Jacobi matrix J with entries a0n , b0n (n ∈ Z)"

  Apply this with μ_n = the image of σ under x ↦ n^p x, k = l = 0, and the constant doubly infinite J (diagonal 2c(p),
  off-diagonal c(p)). This is exactly LP's moment step.
- Simon, "Ratio asymptotics and weak asymptotic measures for orthogonal polynomials on the real line", J. Approx.
  Theory 126 (2004); preprint mp_arc 03-341, TeX source opened. §1 attributes the case to Nevai:
  > "Nevai [Nev79] also proved that if $a_n\to a$ and $b_n\to b$, then $d\mu_n$ has a weak limit (he wrote down the
  > explicit form of $d\rho_{b;a,a}$ for $a=c$ …)."

  Theorem 3.1: "Suppose b_n→b, a_{2n}→a, a_{2n+1}→c … Then as n→∞, dμ_n has a weak limit dρ_{b;a,c}(x), and for every
  ℓ, ∫x^ℓ dμ_n → ∫x^ℓ dρ_{b;a,c}(x)".
- **Useful converse:** Simon 2004 Theorem 3.2:
  > "Suppose for $\ell=1,2$, and $4$, $\lim_{n\to\infty} \int x^\ell d\mu_n =A_\ell$. Then for some $a,b,c$, (3.1)
  > holds."

  A rescaled version (moments of n^p-rescaled μ_n^w → arcsine moments ⇒ n^p a_n, n^p b_n converge) would give a second
  route from localization to T3-all. Lemma R1's moment argument (m₂, m₄) is of this type.

## 5. Theorem L (§3.8)

**Verdict: NOT FOUND.** See §3 for the closest analog (Lubinsky 2009). No source found that bounds sup over a weight path
of the p_n² dμ mass beyond index Mn for pure-point measures accumulating at a point.

## 6. Theorems T3-all, T3-log (and T3-conv, T3-sv, T3a, which they contain)

**Verdict: NOT FOUND.** The obvious places where it could be known were checked.

- **Nevai-class stability (Rakhmanov / Denisov–Rakhmanov).** Remling, "Uniqueness of reflectionless Jacobi matrices and
  the Denisov–Rakhmanov theorem", arXiv:1006.2780v1, Theorem 1.1:
  > "Suppose that: (1) σess (J+ ) = [−2, 2]; (2) Σac (J+ ) = [−2, 2]. Then an → 1, bn → 0 as n → ∞."

  **Differs:** this needs a.c. spectrum. σ = Σ w_kδ_{x_k} is pure point, ess spec {0}, and the unscaled statement
  "a_n, b_n → 0" is trivial (Krein/Stieltjes, §8). The content of T3-all is the n^p-scaled limit with a constant, which
  is not a Nevai-class statement.
- **Relative asymptotics for comparable measures.** Simanek, "Relative asymptotics for general orthogonal polynomials",
  Michigan Math. J. 66 (2017), arXiv:1509.03343v2. Abstract:
  > "we study right limits of the Bergman Shift matrix. Our results have applications to ratio asymptotics, weak
  > asymptotic measures, relative asymptotics, and zero counting measures"

  Theorem 1.1 characterizes relative ratio asymptotics by "lim (hj,n (µ) − hj,n−q (ν)) = 0" for entries of the matrix.
  **Differs:** for compact J these unscaled differences tend to 0 trivially. The scaled statement n^p(b_n(w) − b_n(v)) → 0
  is not addressed. Simanek also cites Máté–Nevai–Totik "Extensions of Szegő's theory II" for "a different, but related
  notion of relative asymptotics" (not opened).
- **RH-based discrete OPs.** BKMM (§1) require analytic weights. WLXZ arXiv:1410.3948 (Tricomi–Carlitz, nodes
  accumulating at 0; already in G1 CITATIONS.md) treats one explicit family. **Differs:** neither covers merely
  slowly varying or rough weight factors. T3-all/T3-log's point is to *transport* the RH result to non-analytic Ψ.
- **Freud weights (unbounded support).** This is the closest *philosophical* analog (measure ⇒ entry asymptotics with an
  equilibrium constant). Van Assche, arXiv:math/0512358v2, §2:
  > "Freud's conjecture for general m > 0 was finally proved by Lubinsky, Mhaskar and Saff [14]. The proof for general
  > m > 0 no longer uses a recurrence relation for the recurrence coefficients but relies on the Mhaskar-Rakhmanov-Saff
  > number and results of weighted polynomial approximation and an equilibrium problem of logarithmic potential theory
  > with external field."

  Whether LMS/KLN prove stability under bounded or slowly varying factors could not be checked (§9).
- **Suggested references for positioning:** LMS 1988 (Constr. Approx. 4, 65–83) as the Freud analog; Remling/Denisov for
  why Nevai-class tools do not apply; Simanek 2017 for relative asymptotics.

## 7. Theorem R and the dichotomy (§3.6, remarks T3c1, R-a, L1)

**Verdict: NOT FOUND as stated.** The phenomenon is unsurprising given the literature: without a.c.-spectrum or
smoothness hypotheses, Jacobi-parameter limits are not forced.

- Remling (1006.2780), after the DR theorem:
  > "In general, both assumptions of the DR Theorem are needed."
- Simon 2004 Thm 3.2 (quoted in §4): convergence of three moments of p_n² dμ forces parameter convergence. Theorem R
  works by making Δ²μ_N non-degenerate, which is the contrapositive mechanism (Lemma R1 is a scaled Thm 3.2-type
  argument).
- **Differs / what is new:** an explicit construction, for every fixed small roughness size ε, of sandwiched weights
  k^{−s}e^{f} (|f| ≤ ε) on fixed nodes k^{−p} with limsup|log β_n²/β_{n−1}²| ≥ εη/2. Averaged laws survive (H_all, CL)
  and slowly varying Ψ preserve the pointwise law (T3-all). I found no comparable sharp dichotomy for compact Jacobi
  operators.
- **Unverified leads (could not open):**
  - Knopfmacher–Lubinsky–Nevai, "Freud's conjecture and approximation of reciprocals of weights by polynomials",
    Constr. Approx. 4 (1988) 9–20, DOI 10.1007/BF02075446 (Crossref-verified metadata only; abstract elided). It may
    contain a sufficiency condition, or a failure example, for Freud-type recurrence asymptotics under weight changes.
    **Must be read before any novelty claim for Theorem R.**
  - The reviewer's pointers: Lubinsky's counterexamples for non-smooth Freud weights; Lubinsky on singularly continuous
    measures in Nevai's class.

## 8. "Inverse spectral theorem for compact Jacobi operators" framing

**Assessment.** The *direction* (spectral data ⇒ Jacobi-entry asymptotics) is a mainstream theme. The *specific
quantitative regime* has no prior result that I found: compact J, eigenvalues x_k ~ Ck^{−p}, weights ~ k^{−s}, entry
asymptotics with the explicit equilibrium constant c(p).

- **Qualitative (Stieltjes/Krein).** Van Assche, "Compact Jacobi matrices: from Stieltjes to Krein and M(a,b)", Ann.
  Fac. Sci. Toulouse S5 (1996) 195–215, DOI 10.5802/afst.852, arXiv:math/9510214. Abstract:
  > "Stieltjes gave a necessary and sufficient condition when a continued fraction is represented by a meromorphic
  > function. This result is related to the study of compact Jacobi matrices."

  §1: "the point spectrum has 0 as its only accumulation point if and only if (8) holds". Compactness ⇔ entries → 0, with
  no rates.
- **Sum rules / L² theory (Killip–Simon).** "Sum Rules for Jacobi Matrices and Their Applications to Spectral Theory",
  arXiv:math-ph/0112008 (Annals 2003). Abstract:
  > "Among our results are a complete classification of the spectral measures of all Jacobi matrices J for which J-J_0 is
  > Hilbert--Schmidt"

  This is the canonical spectral ⇔ entries theorem, but for ess spec [−2, 2]. Simon's book *Szegő's Theorem and Its
  Descendants* (Princeton 2011, ISBN 9781400837052) is the monograph on this; only the catalog description was seen.
- **Denisov–Rakhmanov** (quoted in §6): spectral hypotheses ⇒ a_n → 1, b_n → 0.
- **Freud's conjecture / LMS** (quoted in §6): weight ⇒ a_n ~ c·n^{1/m}, with c from an equilibrium problem. This is the
  closest structural analog of Law P: G2 gets c(p) from a constrained equilibrium, and LMS get Freud's constant from an
  external-field equilibrium.
- **General inverse spectral bijections.** Pushnitski–Štampach, "An inverse spectral problem for non-self-adjoint Jacobi
  matrices", arXiv:2305.19608 (IMRN 2024):
  > "Our main result is that the map from J to the pair (ν,ψ) is a bijection between our class of Jacobi matrices and the
  > set of all spectral data."

  This gives a bijection, not asymptotics.
- **Compact-inverse / discrete-spectrum OPs (direct side).** Šťovíček–Świderski, "On positive Jacobi matrices with
  compact inverses", arXiv:2409.19644v2, J. Approx. Theory 313 (2026) 106217, DOI 10.1016/j.jat.2025.106217:
  > "if the inverse of $J$ belongs to some Schatten class, we identify the asymptotic behaviour of the sequence of
  > orthogonal polynomials and express it in terms of its regularized characteristic function."

  This is the J^{−1}-compact (unbounded J) side, giving OP asymptotics from J, not entries from spectrum. It is the
  nearest current group working on compact-resolvent Jacobi spectral theory and worth contacting or citing.
- **Direct problem (entries ⇒ eigenvalue distribution).** Krasovsky, arXiv:math-ph/9909020:
  > "We obtain the asymptotic distribution of eigenvalues of real symmetric tridiagonal matrices … whose diagonal and
  > off-diagonal elements asymptotically change with the index n as J_{nt+i nt+i}\sim a_i\phi(n) …"

  This covers nondecreasing φ only. Van Assche–Geronimo (regularly varying coefficients) and Tur (Mat. Zametki 2003,
  "very rapidly decreasing" weights) were seen only in search snippets and not opened.
- **Explicit models.** Van Assche, SIGMA 15 (2019) 005, arXiv:1901.09332 (abstract): "discrete orthogonal polynomials on
  a bounded countable set with one accumulation point at 0". WLXZ (Tricomi–Carlitz). Lommel polynomials (discussed in
  Van Assche 1996).

**Suggested framing sentence:** "Law P is a Freud-type theorem for compact Jacobi operators: from the eigenvalue
asymptotics x_k ~ Ck^{−p} and spectral weights k^{−s}Ψ(k) we recover b_n ~ c(p)Cn^{−p}, a_n ~ 2b_n, where c(p) comes
from a constrained equilibrium problem. Unlike the a.c. (Denisov–Rakhmanov, Killip–Simon) setting, the fine asymptotics
are stable under slowly varying weight changes but not under bounded rough ones."

## 9. Not opened / unverified (do not cite without reading)

- Lubinsky–Mhaskar–Saff, Constr. Approx. 4 (1988) 65–83 (known only via Van Assche's quote above).
- Knopfmacher–Lubinsky–Nevai, Constr. Approx. 4 (1988) 9–20, DOI 10.1007/BF02075446 (Springer blocked; S2 abstract
  elided). **Highest-priority read for Theorem R / T3-all.**
- Máté–Nevai–Totik, "Extensions of Szegő's theory of orthogonal polynomials II/III"; Nevai, Memoirs AMS 213 (1979).
- Denisov, Proc. AMS 132 (2004) 847–852 (statement known only via Remling).
- Rakhmanov, Sb. Math. 187 (1996) (constrained equilibrium for discrete OPs); Dragnev–Saff, J. Anal. Math. 72 (1997);
  Kuijlaars–Van Assche, "Extremal polynomials on discrete sets", Proc. LMS (1999); Kuijlaars–Rakhmanov (1998).
- Totik, "Asymptotics for Christoffel functions for general measures on the real line", J. Anal. Math. 81 (2000) (local
  comparison of Christoffel functions; relevant to TL/TV).
- Simon, *Szegő's Theorem and Its Descendants* (book text).
- Tur, Mat. Zametki (2003) (mathnet.ru connection refused).

## 10. Sources opened (with IDs)

1. BKMM, arXiv:math/0212149 (PDF).
2. Dimitrov–Zhang, EJP 28 (2023), DOI 10.1214/23-EJP977 (Crossref abstract).
3. Johansson, arXiv:math/9903134, DOI 10.1007/s002200050027 (abstract page).
4. Basor–Chen–Ehrhardt, arXiv:0905.2620v1 (PDF).
5. Breuer–Duits, arXiv:1309.6224v2 (PDF).
6. Lubinsky, arXiv:math/0701307v1 = Annals 170 (2009) 915–939 (PDF).
7. Van Assche, arXiv:math/9401209v1 = Indag. Math. 6 (1995), DOI 10.1016/0019-3577(95)98197-j (PDF).
8. Simon, mp_arc 03-341 = J. Approx. Theory 126 (2004) (TeX source).
9. Remling, arXiv:1006.2780v1 (PDF).
10. Simanek, arXiv:1509.03343v2 = Michigan Math. J. 66 (2017) (PDF).
11. Van Assche, arXiv:math/0512358v2 (PDF).
12. Van Assche, arXiv:math/9510214 = Ann. Fac. Sci. Toulouse S5 (1996), DOI 10.5802/afst.852 (PDF).
13. Killip–Simon, arXiv:math-ph/0112008 (abstract page).
14. Pushnitski–Štampach, arXiv:2305.19608 (abstract page).
15. Šťovíček–Świderski, arXiv:2409.19644v2, DOI 10.1016/j.jat.2025.106217 (arXiv API record).
16. Krasovsky, arXiv:math-ph/9909020 (abstract page).
17. Van Assche, arXiv:1901.09332 (abstract via arXiv API).
18. Soshnikov, arXiv:math/0002099, DOI 10.1070/RM2000v055n05ABEH000321 (PDF opened; no quote used).

## 11. Search terms used

WebSearch: "Jacobi matrix power decaying entries n^{-p} spectral measure discrete accumulating at zero asymptotics
recurrence coefficients"; "inverse spectral problem compact Jacobi matrix eigenvalue asymptotics implies asymptotics of
entries"; "relative asymptotics orthogonal polynomials comparable weights Máté Nevai Totik ratio asymptotics weight
perturbation"; "Lubinsky Freud conjecture fails recurrence coefficients weight multiplied by bounded function
counterexample" (and extended variants); "Van Assche Compact Jacobi matrices"; "Pushnitski Štampach Jacobi matrices
eigenvalues power asymptotics inverse"; "Freud's conjecture and approximation of reciprocals of weights by polynomials";
"Simon Ratio asymptotics and weak asymptotic measures"; "Denisov On Rakhmanov's theorem for Jacobi matrices";
"derivative of norm h_n … Toda hierarchy"; "large deviations discrete Coulomb gas constrained equilibrium";
"Van Assche Weak convergence of orthogonal polynomials"; "compact Jacobi operator recurrence coefficients decay rate
determined by eigenvalue decay"; "Lubinsky new approach to universality limits comparison lemma"; "Jacobi matrices
eigenvalue counting … entries tend to zero power law"; "Szegő's Theorem and Its Descendants".
arXiv API: abs:"discrete orthogonal polynomials" AND abs:"accumulation point"; abs:"Jacobi matrices" AND
abs:"eigenvalue asymptotics" AND abs:compact; ti:"inverse spectral" AND abs:Jacobi AND abs:asymptotic; and others
(several returned nothing; later calls hit HTTP 429).
Crossref/Semantic Scholar: the KLN 1988 title.

**Suggested follow-up terms:** "Freud conjecture" + "perturbation"/"generalized Freud weight h(x)"; "Nevai class M(0,0)
scaled"; "Jacobi matrices with regularly varying entries eigenvalues"; "Van Assche Geronimo regularly varying recurrence
coefficients"; "discrete orthogonal polynomials nodes 1/k" or "harmonic nodes"; "saturated region Christoffel function
discrete orthogonal polynomials exponential"; "Toda flow localization orthogonal polynomials tail"; "comparison of
Jacobi parameters for comparable measures" (MathSciNet: 42C05 with "comparison" and "recurrence coefficients").
