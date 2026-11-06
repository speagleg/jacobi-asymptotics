# NOVELTY_C: Rule L search for Theorem C (absolute constant 2π/p in h_n; Hankel determinants of ζ(p(i+j)+s))

Date: 2026-11-06. Branch master (no edits elsewhere, no commit). Searcher: a subagent (novelty pass, item C). Rule L only: this
file records what the search found. It does not review the mathematics (Rule R) or the citations (Rule C). Format and verdict
scale follow research/G1/RH/spectral/NOVELTY_ZETA.md. Its findings and those of NOVELTY_JZC.md, research/program/novelty_G1RH.md,
novelty_G2.md, novelty_SPEC.md and novelty_lineB_*.md are not repeated, only referenced.

- **Network.** WebFetch reached arxiv.org/ar5iv this session. Two PDFs (arXiv:1410.3948, Finch's OEIS note) were saved by
  WebFetch as binaries and read **first-hand** with `pdftotext` (quotes marked "(PDF)"). Every other quote came through WebFetch's
  summariser, which paraphrases and caps quotes at about 125 characters: these are **second-hand**, marked "(WebFetch)". Under
  Rule C each must be re-read in the source before it is cited. The Semantic Scholar API answered from the shell for two
  citation lists, and was rate-limited (429) for the third. AMS (Proc. AMS 1988) returned 403. MathSciNet and zbMATH were not used.
- **Verdict scale.** KNOWN: found essentially as stated. PARTIALLY KNOWN: the named part or the phenomenon was found in another
  setting, or a special case is a direct corollary of a published exact formula. NOT FOUND: not located by the queries listed.
  NOT FOUND describes this search; it is not evidence of novelty.
- **Items.**
  - C(a) = Theorem C (C.md §0): h_n(σ_{p,s}) = (2π/p)c^{2n+1}(c^{1/p}/n)^{s−1}Γ(n+1)^{−2p}(1+o(1)) for all p > 0, s > 1,
    with c = c(p) = ¼(π/(2I(p)))^p.
  - C(b) = the special cases p = 1 (Monien/Zagier ζ(i+j+r), Tricomi–Carlitz) and p = 2 (Lommel, even zeta values).
  - C(c) = (C_ℓ): the same with a slowly varying analytic factor ℓ, 1 < s < 1+2p.
- **A correction to the brief's framing, needed for the verdicts.** Theorem C controls each h_n = D_{n+1}/D_n to a factor 1+o(1).
  Summing gives log D_n = Σ_{k<n}log(explicit_k) + o(n), **not** + o(1). Theorem C therefore determines the Hankel determinant
  D_n = det ζ(p(i+j)+s) up to a factor e^{o(n)}. It does **not** determine the Szegő/Widom-type multiplicative constant of D_n,
  such as Monien–Zagier's A^{(0)} ≈ 0.351466738331. To get that constant one needs a summable error rate in h_n and the value of
  the infinite product of the corrections. Theorem 1 of C.md has O(1/n) only in the frame step; Lemmas 3–4 are o(1). What Theorem
  C gives is the "ratio constant" 2π/p, i.e. the n-independent prefactor of h_n. This is what is checked against the literature below.

## 0. Summary

| Item | Verdict | Closest prior work |
|---|---|---|
| C(a). Theorem C for general p > 0, s > 1 (h_n to 1+o(1), prefactor 2π/p) | **NOT FOUND.** No source gives norms, leading coefficients or consecutive-determinant ratios for Σk^{−s}δ_{k^{−p}} beyond the n²-level log D_n (repo's H_all, novelty_G2) or the upper bound −(a/2)n²log n (Haynes–Zudilin). Strong (constant-level) asymptotics for discrete measures accumulating at a point exist only for one explicit family (Tricomi–Carlitz, via exact formulas; WLXZ do polynomials, not norms). | Monien arXiv:0901.1883; Haynes–Zudilin arXiv:1510.01901; WLXZ arXiv:1410.3948; Finch 2014 (OEIS A249185 note) |
| C(a′). The Hankel-determinant constant (Widom-type constant of D_n) | **Not claimed by Theorem C** (see the correction above). For (p, s) = (1, 2), (1, 3) it is open in print: Finch 2014 (PDF): "No closed-form expression for the constant C = 0.351466738331... is known." For (p, s) = (2, 2), (2, 4), (2, 6) it is **KNOWN** via exact closed forms (Krattenthaler, appendix to Fukuhara–Yang). | Finch 2014; Fukuhara–Yang arXiv:math/0608372 App. A; Baricz–Štampach arXiv:1708.07729 (novelty_G2) |
| C(b), p = 1, s = 2 and s = 3 (det ζ(i+j), det ζ(i+j+1)) | **PARTIALLY KNOWN (conjectural/numerical).** Monien–Zagier's experimental expansions of H_n^{(0)}, H_n^{(1)} imply, by taking ratios, exactly Theorem C's h_n at (1, 2) and (1, 3) (own check, §2.1). They are unproved (Monien: "We do not know how to prove the full asymptotic expansions"). The only reported rigorous work is at n²-level and unpublished (personal communication, via Haynes–Zudilin). So Theorem C would be the first proof of the ratio-level statement. | Monien arXiv:0901.1883 §§1–3; Finch 2014; Coons–Sutherland arXiv:1404.2699; Haynes–Zudilin |
| C(b), p = 2, s ∈ {2, 4, 6} (and s = 2 + 2m) | **KNOWN implicitly (exact formulas).** det ζ(2(i+j)+2) has a closed product (Krattenthaler; checked here to 16 digits for n ≤ 7). Equivalently the Lommel ν = 3/2 recurrence (Van Assche math/9510214 §3, already in RH/CITATIONS.md) gives h_n exactly. Theorem C at (2, 2) is a two-line corollary (own check, §2.2: ratio → 1 with error ≈ 0.875/n). No source states the asymptotic form. | Fukuhara–Yang App. A (Krattenthaler); Van Assche 1996 §3; Baricz–Štampach 2018 (novelty_G2) |
| C(b), p = 1 with a slowly varying factor (Tricomi–Carlitz, α = 1) | **KNOWN implicitly (exact formula).** The TC measure at α = 1, folded to y = x², is Σ_m 2e·m^{m−1}e^{−m}/m! δ_{1/m} = Σ m^{−3/2}ℓ(m)δ_{1/m} with ℓ(m) → 2e/√(2π). Its monic norms are exactly 2e/(2n+1)! (from Carlitz's h_n, quoted from WLXZ (1.4)). This matches (C_ℓ) at (p, s) = (1, 3/2) (own check, §2.3, error ≈ 0.375/n). No source states it this way. | WLXZ arXiv:1410.3948 (1.4)–(1.5) (PDF); Carlitz 1958 (not read) |
| C(c). (C_ℓ) for general analytic slowly varying ℓ | **NOT FOUND.** Apart from the TC instance above (a single explicit ℓ), no strong asymptotics of norms for discrete weights k^{−s}ℓ(k) on k^{−p} were found. Line B's pointwise Law P (novelty_lineB_B) remains the nearest repo-internal relative. | WLXZ; Dai–Yao arXiv:2104.03563 (non-accumulating nodes, varying weight) |
| Relation to Hilbert/Cauchy determinants | **KNOWN, different setting.** det(1/(i+j−1)) = G(n+1)⁴/G(2n+1), with constant 2^{1/12}e^{1/4}A^{−3} (Finch, quoting Wikipedia). This is the continuous Lebesgue measure on [0, 1]. Generalised Hilbert matrices with power-type entries (Gebert–Küttler arXiv:2609.00255; Otte arXiv:2207.11029) concern det(I ± H), not moment Hankels of a discrete measure. Monien calls det ζ(i+j) a "discrete analogue of the Selberg integral". | Finch 2014; Gebert–Küttler 2026; Monien |

Recommended Rule L label for Theorem C: **POSSIBLY-NEW** for general (p, s) and for (C_ℓ). The attribution sentence should name the
classical exact anchors (p, s) = (2, 2), (2, 4), (2, 6) [Krattenthaler / Lommel] and TC at (1, 3/2) with ℓ, and the conjectural
Monien–Zagier expansions at (1, 2), (1, 3) [Monien; Finch]. It should say explicitly that the Hankel constant A^{(0)} is not obtained.

## 1. C(a): general p, the 2π/p prefactor

### 1.1 Prior work found
- **Monien, "Hankel determinants of Dirichlet series", arXiv:0901.1883** (WebFetch, ar5iv; already OPENED in novelty_G2/G1RH).
  - Exact Heine-type formulas: Thm 2.1 for any Dirichlet series, Thm 2.5 multiplicative f, Ex. 2.7 1/ζ.
  - Asymptotics only for F = ζ, moments ζ(i+j+r), r = 0, 1 (p = 1). No ζ(a(i+j)+b), a ≠ 1.
  - (WebFetch) "It gives no formula for H_{n+1}/H_n alone" and does not mention orthogonal polynomials, norms or leading
    coefficients.
  - The constant: (WebFetch) A^{(0)} "≈ 0.351466738331", numerical only; A^{(1)} = e^{9/8}/√6·A^{(0)}.
  - Status: heuristic Coulomb-gas / equilibrium analysis; "We do not know how to prove the full asymptotic expansions."
- **Haynes & Zudilin, arXiv:1510.01901 (SIGMA 11 (2015) 101)** (WebFetch, ar5iv). Only Theorem 1.1 (Diophantine) and Lemma 2.3:
  (WebFetch) "log|H_n^{(a,b)}[f]| ≤ −(a/2) n² log n + O(n²)". The expected −an²log n + O(n²) is stated as an expectation. No
  constant term, no ratios, no norms. Ref. [5] is Monien's personal communication.
- **Finch, "Hankel and Toeplitz Determinants", 17 Mar 2014, oeis.org/A249185/a249185.pdf** (PDF, first-hand).
  - "More difficult are determinants of Riemann zeta function values: a_n^{(0)} = |ζ(i+j)|_{1≤i,j≤n}, a_n^{(1)} = |ζ(i+j+1)|"
    "which evidently satisfy a_n^{(0)} ∼ C·((2n+1)/e^{3/2})^{−(n+1/2)²}, a_n^{(1)} ∼ (e^{9/8}/√6) C·(2n/e^{3/2})^{−n²+3/4}
    thanks to numerical experiments by Zagier [11]. No closed-form expression for the constant C = 0.351466738331... is known."
  - Also the Hilbert matrix constant and Krattenthaler's Bernoulli Hankels (§2.2 below). Acknowledges "Hartmut Monien for helpful
    correspondence". This is the best single survey of what was known in 2014; nothing on general p.
- **Coons & Sutherland, arXiv:1404.2699**: O(n²) upper bound only (already in novelty_G2).
- **Citations of 1510.01901 (Semantic Scholar API, shell).** 2610.06838 "The linear independence of 1, ζ(3), and ζ(4)" (2026);
  2201.09262; 2104.13223; Green–Wen arXiv:1908.08426 (JHEP 11 (2019) 079); 1901.10373; 1711.04746. Green–Wen (WebFetch, abstract):
  "positivity constraints on determinants of Hankel matrices involving polynomials of multiple zeta values"; no asymptotics. The
  others are arithmetic (titles only). None treats Hankel asymptotics.
- **Citations of 1410.3948 (Semantic Scholar API).** Dai–Yao 2104.03563; 1912.00500; "Asymptotics of Orthogonal Polynomials"
  (IJNAM 2018); WLXZ's sieved-Pollaczek JAT 2016; 1412.8580. Same list as novelty_G1RH §1.1; none treats norms on k^{−p}.
- **Citations of 0901.1883**: rate-limited (429). novelty_G2 recorded 5 citers via OpenAlex (2026-10-14), none by Monien.
- **Discrete-ensemble constants.** Searches for Widom/DIK-type constants of discrete OP ensembles (Charlier, Meixner, Plancherel /
  discrete Bessel) returned only continuous-weight constant computations (Charlier–Fahs–Webb–Wong multi-cut FH; Charlier–Deaño;
  Charlier–Lenells–Mauersberger hard-edge Meijer-G; Gharakhloo arXiv:1902.08162). These are titles/snippets, not read. No
  constant for a discrete measure with an accumulation point was located.
- **q-lattice analogue.** Joshi–Lasic Latimer arXiv:2111.11663 (WebFetch, abstract): a q-RH problem; norms' asymptotics
  "are independent of the weight function as n→∞". This is the geometric-lattice analogue (corrections geometric); NOVELTY_ZETA
  already places it. Not prior art for power lattices.
- **Lubinsky 1988, Proc. AMS 104, 516–524**, "Jump distributions on [−1,1] whose orthogonal polynomials have leading coefficients
  with given asymptotic behavior" (title from search; page 403). A construction (inverse problem), compact support [−1, 1].
  Probably not about prescribed power-lattice atoms, but **unread** (U3).

### 1.2 Verdict C(a)
- **Theorem C as stated (general p > 0, s > 1, ratio constant 2π/p): NOT FOUND.**
- **Hankel constant of D_n**: not part of Theorem C. It is open in print for p = 1 (Finch 2014) and classical for p = 2 at even s (§2.2).

## 2. C(b): special cases (own numerical checks, mpmath 40–120 digits, R/.venv/bin/python, not certified)

### 2.1 p = 1, s = 2, 3 (Monien–Zagier)
- Here c(1) = ½ (I(1) = π/4), so Theorem C reads h_n = 2π·2^{−2n−1}(2n)^{−(s−1)}/n!².
- From Monien–Zagier, h_n = H_{n+1}/H_n (H_n = det ζ(i+j) over 1 ≤ i, j ≤ n, i.e. moments of Σk^{−2}δ_{1/k}). The ratio to Theorem
  C is 0.91598 (n = 10), 0.990916 (10²), 0.999084 (10³), 0.9999083 (10⁴). It tends to 1 like 1 − 0.917/n.
- Direct Hankel determinants (120 digits) give the same ratio, e.g. 0.9159845 at n = 10, matching the MZ value to 8 digits.
- s = 3 (H^{(1)}, index shift as in Monien): ratio 0.98595 (10²), 0.9998583 (10⁴).
- **Conclusion.** At (1, 2) and (1, 3), Theorem C is the ratio form of the Monien–Zagier conjecture, and it agrees. The conjecture
  is stronger (a full expansion in (2n+1)^{−2} including A^{(0)}) and unproved. Theorem C proves its ratio-leading term for every s > 1.

### 2.2 p = 2, s = 2 (Lommel ν = 3/2; Krattenthaler)
- **Krattenthaler (Appendix A to Fukuhara–Yang, arXiv:math/0608372; Math. Proc. Camb. Phil. Soc. 146 (2009) 321–350)**, as
  reproduced by Finch (PDF): "|B_{2i+2j+2}/(2i+2j+2)!|_{0≤i,j≤n−1} = 4^{−n²} Π_{k=1}^{2n−1}(2k+1)^{−2n+k}", plus two more formulas
  for B_{2i+2j+4}, B_{2i+2j+6} (garbled in extraction). With ζ(2m) = |B_{2m}|(2π)^{2m}/(2(2m)!) this gives
  **det ζ(2i+2j+2)_{0≤i,j<n} = 2^{−n}π^{2n²}Π_{k=1}^{2n−1}(2k+1)^{k−2n}.** Checked here for n = 1..7 (ratio 1 to about 1e−16;
  my derivation of the conversion, not a quoted statement). Krattenthaler's appendix was **not** opened (U1).
- So for σ_{2,2} the Hankel determinant, all h_n, and the full asymptotic expansion with explicit constant (via Barnes G /
  Glaisher) are classical.
- Lommel route: h_n = (π²/6)Π_{j≤n}(π²c_{2j−2}c_{2j−1})², with c_m = 1/(2√((m+3/2)(m+5/2))) (novelty_G1RH §1.3, from Van Assche
  math/9510214 §3). It agrees with the Hankel value at n = 1 to 40 digits. The ratio to Theorem C at (2, 2) (c(2) = π²/16) is
  0.91923 (10), 0.991322 (10²), 0.9991257 (10³), 0.99999125 (10⁵).
- Even s = 2 + 2m follow by Christoffel transforms of the same family. s = 4, 6 have explicit Krattenthaler products. Baricz–Štampach
  2018, Cor. 3 (novelty_G2) covers a = 2, b ∈ {−2, 0, 2}.
- Odd or non-integer s at p = 2 (the case Haynes–Zudilin care about, ζ(2(i+j)+odd)): no exact formula, NOT FOUND.

### 2.3 p = 1 with a slowly varying factor: Tricomi–Carlitz α = 1
- **WLXZ arXiv:1410.3948v1 (PDF, first-hand), (1.4)–(1.5):** "∫ f_m^{(α)}(x)f_n^{(α)}(x)dψ^{(α)}(x) = h_nδ_mn, h_n = 2e^α/((n+α)n!)";
  "ψ^{(α)}(x) is the step function with jumps dψ^{(α)}(x) = (k+α)^{k−1}e^{−k}/k! at x = ±x_k", "x_k = (k+α)^{−1/2}". Leading
  coefficient (from the recurrence (1.6), my derivation; WebSearch snippet also states it): γ_n = (α)_n/n!.
- My derivation: the measure is symmetric, so P_{2n}(x) = Q_n(x²) and the monic norm of Q_n is that of P_{2n}. At α = 1 this is
  2e(2n)!/((2n+1)(2n)!²) = **2e/(2n+1)!**. The folded measure is Σ_{m≥1}2e·m^{m−1}e^{−m}/m! δ_{1/m} (factor 2 from ±x_k). That is
  m^{−3/2}ℓ(m) with ℓ(m) = (2e/√(2π))e^{−μ(m)}, where μ is Binet's function.
- Ratio of the exact norm to (C_ℓ) at (p, s) = (1, 3/2), with ℓ → 2e/√(2π): 0.96436 (10), 0.996269 (10²), 0.9996252 (10³),
  0.99996250 (10⁴).
- Whether this ℓ satisfies Paper II Definition 1.1 ("analytic of angle ϑ") was not checked here; Binet's μ is analytic for
  Re m > 0 and → 0 in sectors, which suggests it does. For α ≠ 1 the nodes 1/(k+α) are a Hurwitz-shifted lattice, outside σ_{p,s,ℓ}.
- Older TC asymptotics: Goh–Wimp, SIAM J. Math. Anal. 25 (1994) 420–428; Lee–Wong, Proc. AMS 138 (2010). Bibliographic only; both
  are polynomial (Plancherel–Rotach / zero) asymptotics according to their abstracts/titles.

### 2.4 Verdict C(b)
- p = 1, s ∈ {2, 3}: **PARTIALLY KNOWN** (conjectural/numerical full expansion, Monien–Zagier; Theorem C consistent and proves its
  ratio term). Other s at p = 1: NOT FOUND.
- p = 2, s ∈ {2, 4, 6, …}: **KNOWN implicitly** (exact products; asymptotic form not stated). Other s at p = 2: NOT FOUND.
- TC α = 1 as a (C_ℓ) instance: **KNOWN implicitly** (exact norms), with the reading this repo's.
- Suggested test (not done): turn §2.1–2.3 into a check script under checks/ with mpmath and fitted 1/n rates.

## 3. C(c): slowly varying extension
- Queries 20, 26 and the citation sweeps found nothing on norms or Hankel ratios for weights k^{−s}ℓ(k) on power lattices.
- Dai–Yao arXiv:2104.03563 (search snippet): "asymptotics for the normalizing coefficient and recurrence coefficients" for discrete
  Laguerre on k²/N². The nodes don't accumulate (varying weight, regular lattice in √x), so this is a different regime.
- **Verdict: NOT FOUND**, apart from the single exact instance §2.3.

## 4. Unread decisive items

| # | Item | Why decisive | For |
|---|---|---|---|
| U1 | Krattenthaler, Appendix A of Fukuhara–Yang arXiv:math/0608372 | Source of the exact p = 2 Hankel products; check s = 4, 6 formulas and whether a general-b (odd) statement or asymptotics appear | C(b) |
| U2 | Monien personal-communication RH work (unpublished; cited by Haynes–Zudilin [5]); Monien's later papers; citers of 0901.1883 (S2 API rate-limited) | The only claimed rigorous RH analysis of det ζ(i+j); could contain h_n-level asymptotics at p = 1 | C(a), C(b) |
| U3 | Lubinsky, Proc. AMS 104 (1988) 516–524; Van Assche–Magnus Proc. AMS 106 (1989) | Leading-coefficient asymptotics for jump measures (inverse direction); confirm no power-lattice direct result | C(a), C(c) |
| U4 | Carlitz 1958 (Duke) / Goh–Wimp 1994 full text | Original TC norm h_n; confirm (1.4) normalisation at source (Rule C) | C(b) |
| U5 | Van Deun, "continued fraction coefficients for Stieltjes transforms … application to continued fraction expansions for the Riemann zeta function" (Antwerp repository; record not reachable) | Continued-fraction coefficient asymptotics involving ζ; probably continuous weights, but unread | C(a) |
| U6 | MathSciNet/zbMATH: "Hankel determinant" ∧ ("zeta" ∨ "Dirichlet series") ∧ asymptotic, post-2015 | Not available here | all |

## 5. Queries (WebSearch; standard unless noted)

1. Hankel determinants of zeta values asymptotics constant term det zeta(i+j)
2. Hankel determinant Dirichlet series asymptotic expansion Riemann-Hilbert proof Monien Zagier constant A
3. norms of orthogonal polynomials discrete measure masses accumulating at zero strong asymptotics leading coefficient
4. Tricomi-Carlitz polynomials orthogonality relation norm leading coefficient explicit
5. (extended) "Hankel determinants" "zeta values" asymptotics proved Riemann-Hilbert ζ(an+b) 2020 OR … 2025
6. Widom constant Hankel determinant discrete orthogonal polynomial ensemble asymptotics constant term Charlier Meixner
7. Lommel polynomials orthogonality norm Hankel determinant closed form reciprocal Bessel zeros moments Rayleigh sums determinant
8. Baricz Štampach Hankel determinants Rayleigh function zeta values Bessel closed form
9. Van Assche orthogonal polynomials zeros accumulating at a point compact Jacobi matrix norms asymptotics
10. Lubinsky asymptotics leading coefficients orthogonal polynomials discrete measure compact support countable atoms accumulating rapidly decreasing recurrence coefficients
11. Dai Yao discrete Laguerre orthogonal polynomials nodes k^2/N^2 Riemann-Hilbert Hankel determinant asymptotics
12. Hankel determinant asymptotics discrete measure hard edge saturated region constant term explicit Riemann-Hilbert partition function discrete ensemble
13. Goh Wimp asymptotics Tricomi-Carlitz polynomials SIAM J. Math. Anal. 1994
14. Hilbert matrix determinant asymptotics constant generalized Hilbert matrix det 1/(i+j+a)^s power exponent
15. "discrete analogue of the Selberg integral" Hankel determinant zeta asymptotic
16. Hankel determinants of zeta(2k) even zeta values closed form det zeta(2i+2j+2) Lommel Krattenthaler
17. Szegő asymptotics leading coefficient orthogonal polynomials compact Jacobi operator recurrence coefficients tending to zero power law n^{-p} norms Gamma(n)
18. Charlier ensemble partition function asymptotics Hankel determinant discrete orthogonal polynomials constant Barnes G explicit Deift Its Krasovsky discrete
19. Ismail orthogonal polynomials masses at reciprocals of integers 1/n moment problem Hankel determinant Dirichlet series
20. Hankel determinants Dirichlet series asymptotics arbitrary coefficients regularly varying lower bound -n^2 log n Coons Sutherland follow-up
21. arXiv 2610.06838 Hankel determinants zeta Lai
22. Hilbert matrix determinant asymptotic formula Barnes G function det 1/(i+j-1) Choi 1983 Tricks or treats with the Hilbert matrix
23. (extended) orthogonal polynomials discrete measure nodes k^{-p} power lattice accumulation point Riemann-Hilbert recurrence coefficients asymptotics 2025 2026
24. Hankel determinant "multiple zeta values" superstring amplitudes unitarity positivity asymptotics
25. Lommel polynomials leading coefficient explicit h_{n,ν}(x) leading coefficient 2^n (ν)_n norm reciprocal Bessel zeros orthogonality 1/(2(n+ν))
26. Hankel determinant moments sum f(k) k^{-s} slowly varying weight discrete measure accumulating at origin asymptotic norms orthogonal polynomials regularly varying masses
27. "Stieltjes" continued fraction Dirichlet series zeta coefficients asymptotics "J-fraction" zeta(s+k) moments Stieltjes transform
28. (extended) Monien "Hankel determinants" zeta Riemann-Hilbert rigorous proof published 2012..2026 orthogonal polynomials 1/k nodes
29. Fukuhara Yang period polynomials Hankel determinant Bernoulli numbers B_{2i+2j+2}/(2i+2j+2)! closed form
30. discrete Bessel kernel Plancherel measure Hankel Toeplitz determinant asymptotics constant term Baik Deift Johansson Widom constant discrete

**API (shell, curl).** Semantic Scholar citations of arXiv:1510.01901 and arXiv:1410.3948 (answered); of arXiv:0901.1883 and the
paper record of 1908.08426 (429, rate-limited).

**Reads.**
- First-hand (PDF via pdftotext): arXiv:1410.3948v1 pp. 1–4 (WLXZ); Finch, oeis.org/A249185/a249185.pdf (full).
- WebFetch summaries: ar5iv 0901.1883 (Monien); ar5iv 1510.01901 (Haynes–Zudilin); arXiv abs 1908.08426 (Green–Wen), 2111.11663
  (Joshi–Lasic Latimer), 2609.00255 (Gebert–Küttler: (WebFetch) "log det(I_N ± H_N^δ) = −((θ_δ² ± θ_δ)/2) log N + O(1)",
  "The page does not give" a constant; det(I ± H) not a moment Hankel).
- Failed: ams.org Proc. AMS 1988 (403); repository.uantwerpen.be/link/irua/95663 (frameset, no record).

**Own computations (NUMERICAL, not certified; inline mpmath via R/.venv/bin/python, no files written).** §2.1 (MZ ratios, direct
Hankel ratios n ≤ 28); §2.2 (Krattenthaler-derived closed form, n ≤ 7; Lommel product to n = 10⁵); §2.3 (TC exact norms vs (C_ℓ)).

## 6. Actions (suggested; nothing done here)
1. Set C.md "Novelty UNCHECKED" → "Rule L: NOVELTY_C.md (POSSIBLY-NEW; exact anchors (2,2),(2,4),(2,6), TC(1,3/2,ℓ); MZ conjecture
   at (1,2),(1,3))". Add a LOG.md pointer.
2. Rule C reads before citing: U1 (Krattenthaler appendix), U4 (Carlitz/WLXZ (1.4)), Finch 2014 (citable as a survey of the open constant).
3. Paper wording: say that Theorem C proves the ratio-level (h_n) form of the Monien–Zagier expansion for all s > 1 and its
   general-p analogue. Do **not** claim the Hankel constant A^{(0)}.
4. Optional test: a checks/ script that reproduces §2.1–2.3 with fitted O(1/n) rates (≈ −0.917/n, −0.875/n, −0.375/n). These
   rates are candidates for the first correction term of Theorem C.

## 2.2a Addendum (lead session, 2026-11-06): Krattenthaler's appendix read first-hand

Source: S. Fukuhara, Y. Yang, "Period polynomials and explicit formulas for Hecke operators on Γ₀(2)", arXiv:math/0608372v2
(10 Jul 2007), **Appendix A, "Evaluation of Hankel determinants of Bernoulli numbers", by Christian Krattenthaler**, pp. 26–28.
PDF fetched by curl from arxiv.org/pdf/math/0608372, text by pdftotext -layout. This closes unread item U1.

- **Theorem A (verbatim up to typesetting).** det_{0≤i,j≤n−1} B_{2i+2j+2}/(2i+2j+2)! = 4^{−n²} Π_{i=1}^{2n−1}(2i+1)^{−(2n−i)};
  det B_{2i+2j+4}/(2i+2j+4)! = (−1)ⁿ4^{−n²−n}9^{−n}Π_{i=1}^{2n−1}(2i+3)^{−(2n−i)};
  det B_{2i+2j+6}/(2i+2j+6)! = 4^{−n²−2n}(n+1)(2n+3)Π_{i=1}^{2n+1}(2i+1)^{−(2n+2−i)}. No hypotheses beyond n ≥ 1.
- **Method.** Theorem CF (Hankel determinants from a Stieltjes continued fraction; Krattenthaler's "Advanced determinant
  calculus" Thm 7.2 and "a complement" Thm 30) applied to Gauss's ₂F₁ continued fraction in the limit ₀F₁(−;5/2;x/16)/
  ₀F₁(−;3/2;x/16), with S-fraction coefficients a_n = 1/(4(2n+1)(2n+3)). This is the Lommel/Bessel ν = 3/2 continued fraction,
  consistent with Van Assche math/9510214 §3.
- **Translation.** ζ(2k) = (−1)^{k+1}B_{2k}(2π)^{2k}/(2(2k)!), and the signs (−1)^{i+j} cancel in the determinant, so the three
  identities are exact closed forms for D_n(σ_{2,s}), s = 2, 4, 6. Checked against direct determinants of ζ(2(i+j)+s) for
  n ≤ 5 to 1e−30 (checks/krattenthaler_p2.py, .out; mpmath 40 digits, not certified).
- **Comparison with Theorem C.** h_n = D_{n+1}/D_n from Theorem A divided by Theorem C's formula at p = 2:
  n(ratio − 1) = −0.8748, −2.8736, −3.8731 at n = 4000 for s = 2, 4, 6 (apparently → −7/8, −23/8, −31/8; not proved).
  So **Theorem C at (p, s) = (2, 2), (2, 4), (2, 6) is a direct consequence of Theorem A plus Stirling**, with rate O(1/n).
  Krattenthaler states no asymptotics. With Paper III's ratio theorem (C.md's reduction), Theorem A at s = 2 alone would
  already give Theorem C for every s on the p = 2 line. The p = 2 case should therefore be attributed, not claimed.
- Verdict C(b), p = 2: **KNOWN implicitly (exact formulas, first-hand)**, unchanged in substance; now Rule-C quotable.
