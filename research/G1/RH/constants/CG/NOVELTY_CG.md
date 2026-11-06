# NOVELTY_CG: Rule L search for constants/CG (Christoffel function of σ_{p,s} at the accumulation point; exact CG/MINRES constant)

Date: 2026-11-06. Branch master. Searcher: a subagent (novelty pass, constants/CG). This is a Rule L check only: it records what
the search found. It does not review the mathematics (Rule R) or the citations (Rule C). Format and verdict scale follow
research/G1/RH/spectral/NOVELTY_ZETA.md. Searches already recorded elsewhere are not repeated, only referenced:
research/G1/RH/spectral/NOVELTY_*.md, research/program/novelty_*.md (especially novelty_G1transport.md on Lubinsky/Totik/
Máté–Nevai–Totik and Simanek), research/program/CONNECTIONS.md §1.1 (gitignored), and the LOG of CG.md (2026-11-05).

- **Network.** The shell cannot reach arxiv.org directly. There are two kinds of quote below.
  - **"(pdftotext)".** WebFetch saved the binary PDF, and I extracted the text locally with `pdftotext`, then read it. These
    quotes come from the source text itself, but the extraction mangles some formulas, so they are reproduced as faithfully as
    the extraction allows. Sources read this way: Velikanov–Yarotsky arXiv:2202.00992 (full); Simon arXiv:0806.1528 (full);
    Lubinsky, "A maximal function approach to Christoffel functions and Nevai's operators" (author PDF, full); Lubinsky, Texas
    Proceedings 2010 survey (author PDF, full); Frankenberger–Hanke, Numer. Algorithms (2000) preprint (Mainz PDF, full).
  - **"(WebFetch)".** These were summarised by WebFetch's small model, with quotes capped at about 125 characters. They are
    second-hand.
  - Under Rule C, every quote of either kind must be re-read in the source before it is cited. MathSciNet and zbMATH were not
    available. Springer (Numer. Algorithms 11), the Mainz bibliography, bohrium and Google Books all refused or rate-limited.
    **Hanke 1996 was not obtained beyond the MaRDI review summary.**
- **Verdict scale.**
  - KNOWN: found essentially as stated.
  - PARTIALLY KNOWN: the named part, or the phenomenon, was found in another setting.
  - NOT FOUND: not located by the queries listed. NOT FOUND describes this search; it is not evidence of novelty.
- **Items.**
  - (a) Theorems A/C constant: λ_m(0;σ_{p,s}) = (Γ(ζ)Γ(ζ+1)/p)(c(p)(p+2)²)^ζ m^{−(p+2)ζ}(1+O(1/m)), for every p > 0 and s > 1
    (Thm A for p ≠ 1, Thm C for p = 1, Thm B the TC special cases).
  - (b) The exponent/rate E = (p+2)ζ, ζ = (s−1)/p. For p > 1 this was already in the repo (second_order/E2_pgt1.md Cor E2.7).
  - (c) Lemma L (§4 of CG.md): λ_m(0;gμ)/λ_m(0;μ) → 1 if g → 1 at 0, c₁ ≤ g ≤ c₂, and a_k, b_k → 0.
  - (d) The CG reading: squared MINRES residual (and, via Christoffel shift, CG A-norm error) after m steps on diag(k^{−p}) with
    right-hand side k^{−s/2}.
  - (e) N-centring (F7, CONJECTURE NUMERICAL): N = m + (s−1)/(2p) removes the 1/m term.

## 0. Summary

| Item | Verdict | Closest prior work |
|---|---|---|
| (a) explicit constant Γ(ζ)Γ(ζ+1)(c(p)(p+2)²)^ζ/p | **NOT FOUND.** No source gives an exact asymptotic constant for CG/MINRES (or λ_m(0)) on a power-law discrete spectrum with a power-law source. Velikanov–Yarotsky (VY) give an explicit **upper-bound** constant (Thm 4.10, with a (n/2) loss factor, not sharp). VY also give an **exact** loss constant (Thm 4.12), but only for an engineered bidiagonal operator whose eigenvalues are merely O(k^{−ν}), not for σ_{p,s}. **Decisive unread: Hanke 1996**, which (per VY) proves CG lower bounds for ν = 1, 2 via Tricomi–Carlitz and modified Lommel polynomials. Whether it states constants is UNKNOWN. | VY arXiv:2202.00992 Thms 4.10, 4.12 (pdftotext); Hanke, Numer. Algorithms 11 (1996) 203–213 (MaRDI review only) |
| (b) exponent E = (p+2)ζ | **PARTIALLY KNOWN → essentially KNOWN as an order bound.** VY Thm 4.10 gives O(n^{−(2+ν)ζ}) for every problem with ρ((0,λ]) ≤ Qλ^ζ and λ_k ≤ Λk^{−ν}. σ_{p,s} satisfies both (ν = p, ζ = (s−1)/p; my check, below), so **the upper bound λ_m ≤ C m^{−E} for σ_{p,s} and all p > 0 follows from VY**. VY's matching lower bound is for a different instance. A lower bound for σ_{p,s} itself, i.e. the exact order (Θ), was not found outside the repo (E2.7, p > 1). Before VY: Hanke 1991/1996 (upper bound; tightness for ν = 1, 2), Nemirovskii–Polyak 1984 (discrete-spectrum improvement observed). | VY §3, App. A; Hanke 1991 Numer. Math. 60; Hanke 1996 |
| (c) Lemma L | **PARTIALLY KNOWN (method KNOWN; this setting NOT FOUND as a statement).** The ratio limit λ_n(g dμ,x₀)/λ_n(dμ,x₀) → g(x₀) for g, g⁻¹ bounded and g continuous at x₀ is Nevai's classical principle (Nevai, Memoirs AMS 213 (1979); the "elementary inequality [12, Thm 5, p. 77]" as quoted by Lubinsky). The localisation ingredient is the Nevai δ-convergence criterion (Simon CD-kernel survey §11; Breuer–Last–Simon). The stated results assume inf a_n > 0, Nevai class on an interval, or regularity with μ′ > 0. None treats x₀ at the accumulation point of a compact Jacobi matrix (a_n, b_n → 0). In that case δ-convergence at 0 is a two-line consequence of Simon's identity (11.9) (my derivation, §3). | Lubinsky, maximal-function paper, (1.1), (3.1); Lubinsky Texas 2010 (1.5); Simon arXiv:0806.1528 Thm 11.1, (11.9); BLS arXiv:0809.2255 |
| (d) CG/MINRES ↔ λ_m(0;σ) dictionary | **KNOWN (dictionary); NOT FOUND (instance).** The residual/kernel-polynomial identities are standard and are used explicitly: VY (54)–(55) compute an exact CG loss as 1/(2Σ v_m²), a Christoffel-function formula; Frankenberger–Hanke use kernel polynomials and Christoffel–Darboux; Stiefel's kernel polynomials are cited there. Nobody located applies the dictionary to diag(k^{−p}), b_k = k^{−s/2} with an exact constant. | VY (54)–(55); Frankenberger–Hanke 2000 |
| (e) N-centring N = m + (s−1)/(2p) | **NOT FOUND.** No source discusses a centring index for Krylov/Christoffel asymptotics on power-law spectra. VY fit only exponents. Scaling-law papers (Paquette et al. 4+3, Lin et al., Bordelon–Pehlevan) work with SGD/gradient flow and Θ-rates, not Krylov constants. | — |

## 1. (a) The constant of Theorems A/C

### 1.1 Findings

- **Velikanov & Yarotsky, "Tight convergence rate bounds for optimization under power law spectral conditions", JMLR 25 (2024)
  no. 81, arXiv:2202.00992** (pdftotext, full text). CONNECTIONS §1.1 had marked this "[seen, full text]". This pass re-read the
  passages relevant to constants and to Hanke.
  - Setting: L(w) = ½‖Jw − f*‖² (their (4); A = J†J, Ã = JJ†, spectral measure ρ of (Ã, f*), their (7)).
    - Main condition (8): "ρ((0, λ]) ≤ Qλ^ζ, λ ∈ [0, λmax]".
    - Eigenvalue condition (10): "λk ≤ Λk^{−ν}".
  - **Thm 4.10 (CG, discrete spectrum)**: "Assuming spectral conditions (9) and (10), the losses of CG satisfy L(wn) ≤ Cζ R(a, r,
    ζ)Λ^ζ (n/2)^{−(2+ν)ζ} (1 + o(1))". Cζ and R come from Cor 4.8 (the HB/Jacobi-schedule bound).
    - The proof sends half of the roots to the largest atoms: "assigning half of the roots of trial polynomials qn to the largest
      atoms λk". So the constant carries a factor of 2^{(2+ν)ζ} and is not sharp by construction.
  - **Thm 4.12 (lower bound example).** J is the bidiagonal operator (52) and f* = e₁. Their statement 1 is "L(wn) = ½
    (Σ_{m=1}^{n+1} m^{(2+ν)ζ−1})^{−1} = (1 + o(1)) ((2+ν)ζ/2) n^{−(2+ν)ζ}". The eigenvalues are only "λk = O(k^{−ν})"
    (statement 2), and ρ((0,λ]) = O(λ^ζ) holds for non-integer ζ (statement 3).
    - This is an exact constant for an instance built so that the Krylov spaces are coordinate spaces. It is **not** σ_{p,s}:
      the nodes are not k^{−p}, and the masses are not k^{−s}.
  - Their only "exact constant" discussion ("Tighter bounds: specifying the constant") concerns the reference problem with an
    absolutely continuous ρ = λ^ζ: "L_n^{(ζ)} = Cn^{−ζ}(1 + o(1)) with a specific constant C". It is used for GD/HB, not for CG with
    a discrete spectrum.
  - On Hanke (pdftotext):
    - "Hanke (1991, 1996) pointed out several important connections between CG and the theory of orthogonal polynomial and proved
      tight lower bounds for convergence of CG in some special cases".
    - "the only previously available lower bounds for CG in the power-law setting were given in Hanke (1996) and only covered two
      special cases ν = 1, 2 for which explicit orthogonal polynomials are known".
    - App. A: "Hanke (1991, 1996) gave a version of the L(wn) = O(n^{−(2+ν)ζ}) bound and proved its tightness in the cases ν = 1,
      2, for which a classical system of orthogonal polynomials is available."
    - "All of these works relied on the classical source condition and only considered problems with attainable solutions."
      Attainable means ζ > 1 in their notation, i.e. s > p + 1 here.
  - On Brakhage/Hanke 1991: these rely "on classical asymptotic properties of Jacobi polynomials ... e.g. Theorem 7.32.2 of Szego
    ... This approach quickly provides the desired O(n^{−2ζ}) rate but does not specify the constant."
- **Hanke, "Asymptotics of orthogonal polynomials and the numerical solution of ill-posed problems", Numer. Algorithms 11 (1996)
  203–213, DOI 10.1007/BF02142497.** Only the MaRDI Q1911450 review summary could be read (WebFetch; reviewer W. C. Rheinboldt).
  - The paper surveys Brakhage's ν-method and CG. "the asymptotics of Christoffel functions is shown to lead to a saturation
    result" for the ν-method. Fast decreasing polynomials are discussed.
  - Convergence-rate estimates for CG on compact operator equations are given "in the setting of two prototype problems related to
    the Tricomi-Carlitz polynomials and the modified Lommel polynomials".
  - WebFetch reports: "No specific constants are mentioned" and "No explicit asymptotic formulas" (in the review).
  - Springer, unpaywall/oadoi, the Mainz bibliography and bohrium all failed (auth redirect, 403, WAF). The Semantic Scholar API
    reports openAccessPdf "CLOSED" and lists 5 citing works: VY; "SGD with memory"; the mini-batch SGD generating-functions paper;
    Erb's co-dilated Landweber paper; a conjugate-residuals/Galerkin paper.
  - **Reading.** In our notation, ν = 1 is p = 1 (TC nodes ±(k+α)^{−1/2}, i.e. 1/(k+α) in x², the same family as Thms B/C) and
    ν = 2 is p = 2 (modified Lommel nodes, ~1/j_{ν,k}² ~ (πk)^{−2}). These are the exactly solvable neighbours of σ_{1,s} and
    σ_{2,s}.
  - If Hanke evaluated K_n(0,0) for these families **with constants**, then the p = 1 special case of Thm B (TC data), and perhaps
    a p = 2 analogue, would be partially anticipated. The transfer to σ_{p,s} itself needs a Lemma-L-type comparison, since the
    masses and nodes differ.
  - VY's wording ("lower bounds", "tightness") suggests order statements, Θ(n^{−(2+ν)ζ}), not constants. **UNCHECKED.**
- **Hanke, "Accelerated Landweber iterations for the solution of ill-posed equations", Numer. Math. 60 (1991/92) 341–374.**
  Record only (EuDML 133597, GDZ link not resolvable through WebFetch). Keywords: fast decreasing polynomials; CG. Not read.
- **Frankenberger & Hanke, "Kernel polynomials for the solution of indefinite and ill-posed problems", Numer. Algorithms (2000)**
  (pdftotext, Mainz preprint).
  - Semi-iterative schemes from kernel polynomials, equivalent for positive operators to Brakhage's ν-methods. "We determine the
    rate of convergence".
  - The weights are of Jacobi type on an interval; it uses Christoffel–Darboux and cites Nevai Memoirs and Stiefel's kernel
    polynomials.
  - No discrete power-law spectra and no constants of our type. Not prior art for (a).
- **Hard-edge Christoffel asymptotics (continuous weights).**
  - Danka–Totik, JEMS 20 (2018), arXiv:1504.03968: power-type weights on curves/arcs; the local limit uses Bessel zeros. Abstract
    level (WebSearch). Already in CG.md §1.
  - Lubinsky, "Universality limits at the hard edge ... compact support" (author PDF): search snippets only.
  - Kuijlaars–Vanlessen, math-ph/0204006: modified Jacobi weight (1−x)^α(1+x)^β h(x), h analytic.
  - All of these are absolutely continuous on a fixed support of positive capacity. For an a.c. weight ~ x^{ζ−1} at a hard edge,
    λ_n(0) ~ C n^{−2ζ}. The extra factor n^{−pζ} in E = (p+2)ζ comes from the saturated (discrete) region, which none of these
    sources contains. Consistent with CG.md §1.
- **Potential-theory CG asymptotics (Kuijlaars SIMAX 2001; Beckermann–Kuijlaars SINUM 2002, BIT 2001 "On the sharpness of an
  asymptotic error estimate for conjugate gradients"; ETNA 14 (2002)).** Abstract/record level (WebSearch).
  - These give n-th root (exponential-rate) asymptotics for a sequence of matrices of size N → ∞ with n/N fixed, via a constrained
    energy problem.
  - This is a different regime (exponential rate, no constant, no infinite-dimensional power law). Already "seen, abstracts" in
    CONNECTIONS §1.1.
- **RH approach to CG for random matrices (arXiv:2112.12354, Ding–Trogdon line).** Snippet level. Halting times / error asymptotics
  for sample-covariance-type spectra, not discrete power laws.
- **Padé/Stieltjes.**
  - Marklof–Tourigny arXiv:0708.1245: Padé of random Stieltjes series, with "explicit formulae (in terms of Bessel functions) for
    the leading term" (search snippet). Random coefficients, not a fixed power-law measure.
  - The J. Approx. Theory paper on Padé of Stieltjes-type meromorphic functions and relative asymptotics: title only.
  - No exact Padé-error constant at the accumulation point for σ_{p,s} was found.
- **Neural scaling laws.**
  - Paquette–Paquette–Xiao–Pennington arXiv:2405.15074 (4+3 phases): one-pass SGD on PLRF.
  - Lin–Wu–Kakade–Bartlett–Lee arXiv:2406.08466: SGD, Θ(M^{−(a−1)} + N^{−(a−1)/a}).
  - Bordelon–Pehlevan arXiv:2002.02561, 2402.01092: kernel learning curves, gradient flow.
  - All at abstract/summary level. None treats Krylov/CG optimal first-order lower bounds with constants.

### 1.2 Verdict (a)

**NOT FOUND.** The explicit constant, for any (p, s), was not located. Closest: VY Thm 4.10 (non-sharp explicit upper constant)
and Thm 4.12 (exact constant for an engineered instance). **Decisive unread: Hanke 1996** (TC/Lommel prototypes, p = 1, 2), and
Hanke's book (Pitman RNM 327, 1995) where the same prototypes may appear.

## 2. (b) The exponent E = (p+2)ζ

- **VY Thm 4.10 applies to σ_{p,s}.** My check, not a literature statement.
  - Take Ã = diag(k^{−p}), J = Ã^{1/2}, f*_k = k^{−s/2}. Then ρ = σ_{p,s}, and VY's CG loss is L(w_n) = ½ min{∫q²dσ : deg q ≤ n,
    q(0) = 1} = ½ λ_{n+1}(0; σ_{p,s}) (cf. VY (54)).
  - (10) holds with ν = p and Λ = 1.
  - (8) holds with ζ = (s−1)/p, because σ((0,λ]) = Σ_{k ≥ λ^{−1/p}} k^{−s} ≤ C λ^{(s−1)/p}.
  - Hence λ_m(0;σ_{p,s}) = O(m^{−(p+2)(s−1)/p}) for **all** p > 0 and s > 1, with VY's explicit (non-sharp) constant.
  - So the upper half of the exponent is literature for every p, not only p > 1. VY's lower bound (Thm 4.12) is for another
    instance. For σ_{p,s} itself, the lower bound and hence the exact order were found only in the repo (E2.7, p > 1).
- Earlier: Nemirovskii–Polyak 1984 (Engrg. Cybernetics 22) observed that the rate improves for discrete spectra (as reported by
  VY). Hanke 1991/1996 gave a version of the O(n^{−(2+ν)ζ}) bound, with tightness for ν = 1, 2 (VY). Nemirovskii, Zh. Vychisl.
  Mat. Mat. Fiz. 26 (1986) 332–347 (record only).
- **Verdict (b): PARTIALLY KNOWN.** The order upper bound is KNOWN (VY Thm 4.10, all p). Tightness in the class is KNOWN (VY Thm
  4.12; Hanke 1996 for ν = 1, 2). Θ for the specific measure σ_{p,s} was NOT FOUND outside the repo. Recommended wording for papers:
  "the exponent is that of the VY class bound; Thm A shows it is attained by σ_{p,s} and gives the constant."

## 3. (c) Lemma L

### 3.1 Findings

- **Nevai's ratio principle.**
  - Lubinsky, "A maximal function approach to Christoffel functions and Nevai's operators" (pdftotext), §1: "if μ is supported on
    [−1, 1], and μ′ > 0 a.e. on [−1, 1], while g^{±1} is bounded on supp[μ], and g is continuous at x, then (1.1) holds at x. This
    follows from results of Nevai [9], [12]". Here (1.1) is lim λ_n(g dμ, x)/λ_n(dμ, x) = g(x), and [12] = Nevai, Memoirs AMS 213
    (1979).
  - The key tool, quoted in his §3: "the elementary inequality [12, Theorem 5, p. 77] λ_n(g dμ, x)P²(x)/λ_{n−m}(dμ, x) ≤
    G_{n−m}[gP²](x)", with Nevai operator G_n[f](x) = ∫K_n²(x,t)f(t)dμ(t)/K_n(x,x).
  - This is exactly step (ii) of Lemma L (testing one minimiser in the other problem) with P ≡ 1.
  - Lubinsky Texas 2010 survey (pdftotext), around (1.5): "when μ is regular, and g^{±1} are bounded on supp[μ], while g is
    continuous at x, then methods pioneered by P. Nevai allow one to establish (1.5)". Lubinsky's own Theorem 1.2 gives convergence
    in measure on {μ′ > 0} for arbitrary compact support. That is irrelevant at an atom-accumulation point, where μ′ = 0.
- **Nevai δ-convergence.**
  - Simon, "The Christoffel–Darboux kernel", arXiv:0806.1528, §11 (pdftotext).
    - dη_n^{(x₀)} = |K_n(x,x₀)|²dμ/K_n(x₀,x₀), (11.3). The Nevai δ-convergence criterion is dη_n^{(x₀)} → δ_{x₀}, (11.4).
    - Thm 11.1: "If dμ is a measure on R with bounded support and inf_n a_n > 0 then for any fixed x₀ ∈ R, (11.4) ⇔ (11.5)", where
      (11.5) is |p_n(x₀)|²/K_n(x₀,x₀) → 0.
    - The proof uses the CD identity "(11.9) ∫|x − x₀|²|K_n(x,x₀)|²dμ = a²_{n+1}[p_n(x₀)² + p_{n+1}(x₀)²]".
    - Thm 11.4 (Nevai; Nevai–Totik–Zhang): the Nevai class on an interval.
  - Breuer–Last–Simon, "The Nevai condition", Constr. Approx. 32 (2010), arXiv:0809.2255 (WebFetch, first 100k characters): the
    same equivalence, under "0 < inf a_n ≤ sup a_n < ∞" (their (1.14)). WebFetch: the compact case a_n → 0 "is not treated", and
    Thm 1.2 "does not apply" when inf a_n = 0.
- **My derivation (not a literature statement).** Take x₀ = 0, a_n, b_n → 0, K_n(0,0) → ∞, and K_n = Σ_{j≤n} as in Simon.
  - From the recurrence, a_{n+1}p_{n+1}(0) = −b_{n+1}p_n(0) − a_np_{n−1}(0) (up to index convention). Hence
    a²_{n+1}p_{n+1}(0)² ≤ 2 max(a_n², b_{n+1}²)·K_n(0,0).
  - Then (11.9) gives ∫x²dη_n^{(0)} ≤ a²_{n+1} + 2 max(a_n², b²_{n+1}) → 0, with no hypothesis (11.5) and no inf a_n > 0.
  - Since η_n is a probability measure, ∫|x|dη_n ≤ (∫x²dη_n)^{1/2} → 0. This is Lemma L's ε_m(ν) → 0 (step (i)).
  - So the δ-convergence at the accumulation point is immediate. Combined with Nevai's inequality, it gives Lemma L. CG.md's own
    step (i) (the vᵀJ_mv bound) is an equally short alternative.
- Máté–Nevai–Totik ("Extensions of Szegő's theory II/III"), Totik J. Anal. Math. 81 (2000), Simanek: already in
  novelty_G1transport.md. They are all for a.c. or regular measures at points with μ′ > 0. Not re-opened.
- Nevai, "Géza Freud, orthogonal polynomials and Christoffel functions. A case study", J. Approx. Theory 48 (1986) 3–167: record
  only. A Scribd TOC snippet mentions "Theorem 4.5.8" on two measures. Not read.

### 3.2 Verdict (c)

**PARTIALLY KNOWN.** The mechanism is KNOWN, Nevai's ratio principle, with ingredients (Nevai Memoirs Thm 5 p. 77; Simon §11 /
BLS). No source located states it at the accumulation point of a compact Jacobi matrix. There it follows from Simon (11.9) in
two lines. Recommended label: "elementary; a special case of Nevai's comparison principle for Christoffel functions [Nevai 1979],
the localisation being automatic when a_n, b_n → 0". Do not claim novelty for Lemma L.

## 4. (d) The CG reading

- The identities MINRES residual² = λ_{m}(0;σ) and CG A-norm error = λ_m(0;σ_{p,s−p}) (Christoffel shift) are standard.
  - VY (54)–(55) use exactly this structure: L(w_n) = (2Σ_{m≤n+1} v_m²)^{−1} with v ⊥ the Krylov residuals. That is 1/(2K(0,0)) in
    their coordinates.
  - Frankenberger–Hanke 2000 build methods from kernel polynomials K_n(0,t)/K_n(0,0) and use Christoffel–Darboux.
  - Hanke's book (1995) is described as resting on "the connection of conjugate gradient type methods to real orthogonal
    polynomials" (WebSearch summary).
- **Verdict (d): KNOWN** as a dictionary (cite VY (54) and a textbook source after Rule C reading; "standard" is not a citation).
  **NOT FOUND:** an exact-constant statement for diag(k^{−p}), b_k = k^{−s/2}.

## 5. (e) N-centring

No source discusses an index shift N = m + (s−1)/(2p), or any centring, in Krylov or Christoffel asymptotics for power-law spectra.
VY fit only exponents, and none of the scaling-law papers reached treats Krylov constants. The analogous natural index of Paper IV
(n + α/2 − Z(0)) was already NOT FOUND in NOVELTY_ZETA (Z1). **Verdict (e): NOT FOUND.**

## 6. Unread decisive items

1. **Hanke, Numer. Algorithms 11 (1996) 203–213.** It holds the TC and modified-Lommel CG prototypes (ν = p = 1, 2). If it
   evaluates λ_n(0) or K_n(0,0) with constants, Thm B (p = 1, TC data) and perhaps a p = 2 analogue are partially anticipated.
   Needs library or Springer access.
2. **Hanke, Conjugate Gradient Type Methods for Ill-Posed Problems, Pitman RNM 327 (1995)**, the chapters on CG for compact
   operators and on the number of iterations. The same prototypes may appear there.
3. **Hanke, Numer. Math. 60 (1991) 341–374** (GDZ open access; the link did not resolve through WebFetch).
4. **Nemirovskii–Polyak 1984b** (lower bounds; Engrg. Cybernetics 22) and **Nemirovskii 1986** (ZhVMMF 26).
5. **Nevai, Memoirs AMS 213 (1979), Thm 5 p. 77**, and **Nevai JAT 48 (1986) §4.5**: needed for the Rule C quote behind Lemma L.
6. BLS arXiv:0809.2255, last 14k characters (not read). They may contain remarks on compact J.

## 7. Recommended labels and attribution wording

- Thm A/C constant: Rule L field "NOT FOUND (this search; Hanke 1996 unread)". Keep POSSIBLY-NEW, not NEW, until item 6.1 is read.
- Exponent: "order O(m^{−E}) for the class: Velikanov–Yarotsky 2024 Thm 4.10 (and Hanke 1991/1996 for ν = 1, 2); attained with
  explicit constant by σ_{p,s}: Thm A/C (and E2.7 for p > 1)".
- Lemma L: "a case of Nevai's comparison principle"; drop "novelty UNCHECKED" in favour of "PARTIALLY KNOWN (method)".
- CG reading: attribute the dictionary; claim only the instance constant.
- F7 centring: no prior art found; keep as CONJECTURE (NUMERICAL).

## 8. Queries (WebSearch; standard unless noted)

1. Hanke 1996 "Asymptotics of orthogonal polynomials and the numerical solution of ill-posed problems"
2. conjugate gradient convergence power law eigenvalues sharp asymptotic constant source condition
3. Christoffel function at accumulation point of mass points discrete measure asymptotics
4. Nemirovskii conjugate gradient optimal ill-posed problems lower bound rate
5. Hanke conjugate gradient Tricomi-Carlitz polynomials modified Lommel polynomials convergence rate compact operator
6. (extended) Hanke "Tricomi-Carlitz" conjugate gradient ill-posed prototype "Christoffel"
7. Velikanov Yarotsky "Tight convergence rate bounds for optimization under power law spectral conditions" lower bound constant conjugate gradients
8. Christoffel functions comparison lemma λ_n(gμ, x)/λ_n(μ, x) → g(x) continuous at x localization Máté Nevai Totik
9. Kuijlaars "Which eigenvalues are found by the Lanczos method" constrained equilibrium problem
10. Beckermann Kuijlaars superlinear convergence of conjugate gradients potential theory asymptotic convergence factor
11. Paquette "4+3 phases of compute-optimal neural scaling laws" power law random features
12. Breuer Last Simon "The Nevai condition" Constructive Approximation Christoffel-Darboux kernel
13. Nevai "Géza Freud, orthogonal polynomials and Christoffel functions. A case study" λ_n(dμ_1)/λ_n(dμ_2) comparison
14. Nevai class M(0,0) compact Jacobi matrix Christoffel function at 0 Nevai operator weak convergence point mass accumulation
15. Christoffel function at the hard edge λ_n(0) Laguerre weight exact formula Gamma n^{-α-1} asymptotics endpoint Jacobi λ_n(1)
16. Christoffel functions Tricomi-Carlitz polynomials OR Lommel polynomials asymptotics at zero conjugate gradient
17. Nemirovskii Polyak 1984 "Iterative methods for solving linear ill-posed problems under precise information" lower bounds conjugate gradient discrete spectrum
18. Hanke 1991 "Accelerated Landweber iterations for the solution of ill-posed equations" Numerische Mathematik orthogonal polynomials ν-method
19. conjugate gradient Krylov neural scaling laws power-law spectrum source exponent optimal first-order method lower bound constant 2024 2025
20. Bordelon Pehlevan "spectrum dependent learning curves" OR "dynamical model of neural scaling laws" power law exponent constant
21. Padé approximant error Stieltjes function at endpoint of support power-law measure asymptotics rate exact constant
22. (extended) MINRES residual asymptotics eigenvalues k^{-p} right-hand side power law exact asymptotic Christoffel function Bessel kernel
23. Lubinsky "universality limits at the hard edge of the spectrum for measures with compact support" Christoffel function endpoint asymptotics
24. Kuijlaars Vanlessen "universality for eigenvalue correlations from the modified Jacobi unitary ensemble" hard edge Bessel kernel
25. orthogonal polynomials discrete measure masses accumulating at zero Christoffel-Darboux kernel K_n(0,0) growth rate Lommel polynomials
26. Engl Hanke Neubauer "Regularization of inverse problems" chapter 7 conjugate gradient convergence rate discrete spectrum faster than ν-method example
27. (extended) "conjugate gradient" "Tricomi-Carlitz" eigenvalues 1/(k+α) residual polynomial lower bound ill-posed
28. Danka Totik "Christoffel functions with power type weights" λ_n(μ,0) n^{α+1} limit constant Bessel
29. Riemann-Hilbert conjugate gradient convergence asymptotics compact operator eigenvalues accumulating at zero exact error constant arXiv
30. Lin Wu Kakade Bartlett Lee "scaling laws in linear regression" compute optimal power-law spectrum source condition
31. Gauss quadrature error ∫ x^{-1} dμ discrete measure accumulating at zero asymptotics continued fraction Stieltjes truncation error power law
32. (extended) exact asymptotic constant conjugate gradient error power law spectrum hard edge Bessel Christoffel function 2025 2026 arXiv
33. "Christoffel function" "accumulation point" orthogonal polynomials point masses limit n^
34. Brakhage 1987 "On ill-posed problems and the method of conjugate gradients" ν-method Jacobi polynomials rate
- Auxiliary: Google Books feed query for Hanke's book (volume ids UEwPEAAAQBAJ, 0aGymxOggzwC). The follow-up googleapis calls
  returned HTTP 429.

**WebFetch reads.**
- Full text (pdftotext of the saved PDF):
  - arXiv:2202.00992 (VY);
  - arXiv:0806.1528 (Simon, CD kernel);
  - Lubinsky NevaiOpsJan10.pdf (maximal-function / Nevai operators);
  - Lubinsky TexasProceedings2010Vn2.pdf;
  - Mainz har.pdf (Frankenberger–Hanke 2000).
- Long text (WebFetch summary): ar5iv 0809.2255 (BLS, first 100k characters); ar5iv 1206.1950 (Erb; no attributable Hanke
  citation found).
- Records or abstracts:
  - MaRDI Q1911450 (Hanke 1996 review);
  - Semantic Scholar API for DOI 10.1007/BF02142497 (closed; 5 citations listed);
  - arXiv abs math/9510214 (Van Assche, compact Jacobi matrices: no Christoffel content in the abstract);
  - EuDML 133597 (Hanke 1991).
- Failed:
  - unpaywall → oadoi redirect (not followed);
  - Springer article (auth redirect);
  - bohrium (WAF);
  - bibliographie.ub.uni-mainz.de (403);
  - GDZ volume page (no article list);
  - Google Books API (429).

## 9. Actions (suggested; nothing done here)

1. Obtain Hanke 1996 (and the 1995 book chapter on compact operators) through a library. Check whether λ_n(0) or K_n(0,0) for TC or
   modified Lommel is stated with constants. Update CG.md §1 accordingly.
2. In CG.md §1, record that VY Thm 4.10 already gives the upper bound O(m^{−E}) for σ_{p,s} for every p > 0 (§2 above, my check;
   re-verify the hypotheses (8) and (10) and the identification L = ½λ_{n+1}(0;σ) under Rule C).
3. Re-label the Lemma L novelty as PARTIALLY KNOWN (Nevai's principle). Add a Rule C quote of Nevai Memoirs Thm 5 p. 77, and
   optionally the two-line δ-convergence argument from Simon (11.9).
4. Optional numerical comparison, not literature: evaluate VY's Thm 4.10 constant Cζ R Λ^ζ 2^{E} against Thm A's C at a few (p, s)
   to quantify the slack.
5. Rule L logging: the queries are here; the LOG.md pointer is left to the session.
