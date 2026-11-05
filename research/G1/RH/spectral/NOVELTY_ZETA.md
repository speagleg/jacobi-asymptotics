# NOVELTY_ZETA: Rule L search for cluster Z (spectral zeta values in recurrence coefficients)

Date: 2026-10-23. Branch plan-e2-d2. Searcher: a subagent (novelty pass, cluster Z). Rule L only: this file records what the search
found. It does not review the mathematics (Rule R) or the citations (Rule C). Format and verdict scale follow NOVELTY_JZC.md; this
pass extends that one and research/program/novelty_SPEC.md. Their findings are not repeated, only referenced.

- **Network.** The shell cannot reach arxiv.org. Every quote below came through WebFetch, which summarises the page with a small
  model and caps quotes at about 125 characters. **All quotes are second-hand and marked "(WebFetch)".** Under Rule C, each one must
  be re-read in the source before it is cited. Equation and theorem numbers are as WebFetch relayed them. MathSciNet and zbMATH
  were unavailable.
- **Verdict scale.** KNOWN: found essentially as stated. PARTIALLY KNOWN: the named part or the phenomenon was found in another
  setting. NOT FOUND: not located by the queries listed. NOT FOUND describes this search; it is not evidence of novelty.
- **Items.**
  - Z1 = Theorem K / Theorem N.6 (JZC_M4_proof): the double expansion of b_n for σ = Σk^{−s}δ_{k^{−p}} in 1/N and monomials
    N^{−1−jp}, coefficients ε_j = C(2j,j)pc^jζ(−jp); natural index N = n + α/2 − Z(0); exact even dressings g_j = A_j + B_jα²; the
    ζ(−p)² layer (3p+1)/(2p).
  - Z2 = Theorem H (JZC_M3a_H): Hurwitz lattices (k+δ)^p; the Hurwitz shift is the Szegő-exponent shift β′ = α + 2δ; constants
    ζ(−jp, 1+δ).
  - Z3 = Conjecture W and the κ-family theorem (JZC_W, JZC_W_kappa): Jacobi matrix of a measure on reciprocals of a Weyl-type spectrum
    = Toda flow of a decoupled Bessel/Szegő model with spectral-zeta times, plus pRW(q)π cot(πq) pole terms; drums (perimeter and
    corners from b_n, SPEC §3.16).
  - Z4 = large order (JZC_M4 §9): the integer layer is Gevrey-1 divergent with complex-conjugate Borel singularities.
- **Paper IV numbering.** In papers/paperIV/main.tex the order is sec1–sec5, secS (§6), secH (§7), sec6.tex = §8 "Examples and
  numerical evidence", sec7.tex = §9 "Conjectures", sec8.tex = §10 "Relation to the literature". So "§8" is sec6.tex and "§10" is
  sec8.tex below.

## 0. Summary

| Item | Verdict | Closest prior work |
|---|---|---|
| Z1. ζ(−jp)-monomial double expansion of b_n; N = n + α/2 − Z(0); g_j; (3p+1)/(2p) | **NOT FOUND** (strengthened). **Exact special cases are classical:** Lommel polynomials (reciprocal Bessel zeros) and, newly found here, Tricomi–Carlitz polynomials (nodes ±(k+α)^{−1/2}, a Hurwitz-type lattice at p = 1 in x²). Both have explicit rational recurrence coefficients. No source reads them through zeta values. q-analogues have geometric, not power, corrections. The general principle "singularities of the weight → identifiable power terms in the recurrence coefficients" is **PARTIALLY KNOWN** for continuous weights (Hodges; Magnus; Foulquié Moreno–Martínez-Finkelshtein–Sousa; Murugan–Van Zyl–Watanabe 2026 at hard/soft edges). | VA 1996 §3; Dickinson 1954; Grosjean 1985; Wu–Lin–Xu–Zhao arXiv:1410.3948 (Tricomi–Carlitz); Koelink–Van Assche math/9502227; Joshi–Lasic Latimer arXiv:2211.12658; Šťovíček–Świderski arXiv:2409.19644 (now read: no Jacobi-parameter asymptotics); Magnus 1995; arXiv:0905.2753; arXiv:2608.07258 |
| Z2. Hurwitz shift = Szegő-exponent shift; ζ(−jp, 1+δ) | **NOT FOUND** as a statement. Hurwitz's formula is KNOWN (Dixit–Kumar, already cited). ζ_Bessel(0) = −(ν+½)/2 is KNOWN (Naber–Bruck–Costello; Hawkins). The index transfer appears **implicitly** in the two exactly solvable families: the lattice offset enters the recurrence only through n + const (Lommel: n + ν; Tricomi–Carlitz: n + α). Nobody located states this as a Hurwitz/Szegő identity. | as Z1; Naber–Bruck–Costello arXiv:2211.05765 |
| Z3. Conjecture W, κ-family theorem, spectral-zeta Toda times, pole law π cot(πq), drum reading | **NOT FOUND.** The ingredients are KNOWN: Toda flow = exponential tilt of the measure (classical); spectral zeta values and residues of Weyl-type spectra (Voros; Bessel and Airy zetas); leading-order density ↔ coefficient-growth correspondence (Freud/Lubinsky; Parker et al. 2019 for Lanczos). Subleading Lanczos asymptotics from **continuous** endpoint data are PARTIALLY KNOWN (Murugan–Van Zyl–Watanabe 2026: hard-edge n⁻² term from the edge exponent; no Weyl/zeta/discrete spectra). Discrete-spectrum Lanczos (CFT on S³) is reported only qualitatively, as staggering (Avdoshkin–Dymarsky–Smolkin). Billiard Krylov papers give no Weyl/perimeter/corner reading. Inverse spectral theory (Killip–Simon/Case sum rules; Silva–Weder two spectra; Boutet de Monvel–Janas–Zielinski; Yafaev) does not touch this question. | arXiv:2608.07258; arXiv:1812.08657; arXiv:2212.14429; arXiv:2306.11632; arXiv:2409.19644; arXiv:1206.1763; arXiv:2202.02087 |
| Z4. Gevrey-1 integer layer, complex Borel pair, action A(p) unidentified | **PARTIALLY KNOWN (phenomenon, other settings).** Divergent 1/N (genus) expansions of matrix-model recurrence/free-energy data, with large order fixed by an instanton action, are KNOWN (Mariño–Schiappa–Weiss 2008). Euler–Maclaurin remainders are Gevrey-1 and resurgent, with Borel singularities on 2πiℤ·ω (Costin–Garoufalidis 2007). **NOT FOUND:** large-order analysis of the 1/N expansion of recurrence coefficients of a fixed (non-varying) discrete measure, and a complex-conjugate action pair. | arXiv:0711.1954; arXiv:math/0703641 |

## 1. Z1: zeta-valued expansion of b_n, the natural index, and the dressings

### 1.1 Prior work found (new in this pass)

- **Šťovíček & Świderski, "On positive Jacobi matrices with compact inverses", arXiv:2409.19644v2 (2024).** Read via WebFetch of the
  full arXiv HTML. This discharges NOVELTY_JZC action 3, second-hand. WebFetch's verdict (WebFetch): "The paper gives no asymptotics
  for the Jacobi parameters. Its asymptotic results concern the polynomials $P_n$, their zeros, zero counting measures,
  Christoffel–Darboux kernels, and the regularized characteristic function."
  - Zeta functions appear only as convergence conditions Σ_j|ζ_j|^{−k} < ∞ (their (4.19), Example 4.4). Here ζ_j are eigenvalues,
    not zeta values. "Zeta values at negative arguments and the Riemann zeta function are not discussed." (WebFetch)
  - Main results (WebFetch):
    - Thm 2.1: trace-class criterion for J⁻¹ and a formula for Tr J⁻¹.
    - Thm 4.7: "det[E_{k−1}(zJ_n^{−1})] → F_k(z) locally uniformly", assuming "J is positive and J_F^{−1} belongs to S_k".
    - Cor 4.10: p_n(z)/p_n(0) → F₁(z).
  - Examples: Al-Salam–Carlitz II, modified q-Laguerre (birth–death). No Weyl law.
  - **Conclusion.** This paper is the regularised-determinant side of SPEC Heuristic S3 (polynomials at fixed z). It does not
    contain recurrence-coefficient asymptotics. It remains the right citation for "OPs on reciprocal spectra via regularised
    characteristic functions"; it is not prior art for K/N.6.
- **Štampach & Šťovíček, related papers (abstract level, WebFetch).** None gives Jacobi-parameter asymptotics from spectral data.
  - arXiv:1301.2125, "Special functions and spectrum of Jacobi matrices": the spectrum is the zero set of a special function (Coulomb,
    ₁F₁, q-Bessel). "The paper does not derive asymptotics of the parameters themselves."
  - arXiv:1510.01454, "Factorization of the characteristic function of a Jacobi matrix": "an explicit expression for the power
    series expansion of the logarithm of the characteristic function is obtained". This is the parameters → Σλ^{−k} (positive k)
    direction.
  - arXiv:1904.13199, "On infinite Jacobi matrices with a trace class resolvent".
  - arXiv:1702.07496.
- **Tricomi–Carlitz polynomials: Wu, Lin, Xu & Zhao, "Uniform asymptotics for discrete orthogonal polynomials on infinite nodes with
  an accumulation point", arXiv:1410.3948** (WebFetch, PDF).
  - Quoted: recurrence "(n+1)f_{n+1}^{(α)}(x) − (n+α)xf_n^{(α)}(x) + f_{n−1}^{(α)}(x) = 0", f₀ = 1, f₁ = αx (1.6).
  - Quoted: jumps "(k+α)^{k−1}e^{−k}/k!" at x = ±x_k, "x_k = (k+α)^{−1/2}", α > 0 (1.4)–(1.5). Earlier asymptotics: Goh–Wimp,
    SIAM J. Math. Anal. 25 (1994) 420–428; Carlitz for the orthogonality.
  - The paper does Plancherel–Rotach asymptotics of the polynomials, not of the recurrence coefficients.
  - **My derivation (not a literature statement).**
    - From (1.6), the monic recurrence is xπ_n = π_{n+1} + a_nπ_{n−1} with **a_n = n/((n+α)(n+α−1))**. Check: a₁ = 1/(α(α+1)).
    - The standard even-part reduction (Chihara, symmetric functionals; not re-read here) gives the measure on y = x² = 1/(k+α). Its
      Jacobi parameters are β_n = a_{2n−1}a_{2n} = (2n−1)(2n)/(M²(M²−1)) with M = 2n − 1 + α, and diagonal a_{2n} + a_{2n+1}.
    - This is an **exactly solvable Hurwitz-type lattice**: nodes 1/λ with λ = k + α, i.e. p = 1, δ = α − 1. The masses are
      ~ (e^α/√(2π))λ^{−3/2}(1 + O(1/λ)) by Stirling, a W3-type mass tilt with s = 3/2.
    - The lattice offset α enters the recurrence only through the index M = 2n − 1 + α, which is the Theorem H phenomenon in exact
      form. It is at p = 1, which N.6/H/W exclude (JZC_W §1.6), and with a non-trivial v(λ).
    - Not checked numerically here (no mpmath/PARI in this shell).
- **Neumann–Bessel family: arXiv:2406.09746, "Complex zeros of Bessel function derivatives and associated orthogonal polynomials"
  (2024)** (WebFetch, PDF).
  - Thm 2.4 (WebFetch): for ν > 0 the measure is supported on {±1/j′_{ν,k}} with mass "2ν/((j′_{ν,k})²−ν²)". The moment functional
    "L(f) = Σ_{k≠0} f(1/j′_{ν,k})/(j′_{ν,k})²" gives "the Rayleigh-type sums".
  - Thm 3.2: γ₁ = (ν+2)/(2ν(ν+1)) and γ_n = [4(ν+n−1)(ν+n−2)]^{−1}·q_{n+1,ν}(1/ν)q_{n−2,ν}(1/ν)/(q_{n,ν}(1/ν)q_{n−1,ν}(1/ν)), with
    q_{n,ν} Lommel-type polynomials (β_n = 1/[4(ν+n−1)(ν+n)]). "The paper does not give asymptotics for γ_n" (WebFetch).
  - **Relevance.** This is a Christoffel/Geronimus-type modification of the Lommel measure on a Neumann Bessel spectrum, with a mass
    tilt (1 − ν²/λ)^{−1} (in W's language: integer Toda times). The q_{n,ν}(1/ν) at fixed argument have 1/n expansions with
    coefficients rational in ν. So γ_n has a computable all-order expansion. This is an **exact, non-trivial test case for Conjecture
    W** (Neumann McMahon offset j′_{ν,k} ~ (k + ν/2 − ¾)π, Z(0) ≠ the Dirichlet value, nonzero t_j). It is not prior art for any claim.
- **Lommel / Rayleigh sums (classical, positive arguments).**
  - Grosjean, "The orthogonality property of the Lommel polynomials and a twofold infinity of relations between Rayleigh's σ-sums",
    J. Comput. Appl. Math. (1984/85; received Jan 1984), doi:10.1016/0377-0427(84)90044-X (WebFetch, abstract; the author's name
    and volume were not shown on the page and are not checked). It derives Lommel orthogonality from the continued fraction for J_{ν−1}/J_ν. "One of its corollaries is a twofold
    infinity of linear relations between the sums" (WebFetch).
  - So the moment problem with moments = Bessel spectral zeta values at positive integers is classical (the Dickinson/VA facts are in
    novelty_SPEC §1.1). Nothing about n-asymptotics or zeta values at non-positive arguments.
  - arXiv:1305.0228 (Rayleigh sums), title only.
- **Kvitsinsky (Kvitsinskiy), "Spectral functions of zeros for q-Bessel functions", Theor. Math. Phys. 107:3 (1996) 740–754 (TMF
  397–414)** (WebFetch, mathnet abstract).
  - It treats ζ_ν(z; q) and Z_ν(t; q) of q-Bessel zeros: "explicit formulas for ζ_ν(2n; q)" at n = ±1, ±2, …; the poles and residues
    "found"; the t ↓ 0 asymptotics "derived".
  - WebFetch: no mention of Lommel polynomials or recurrence coefficients.
  - The J. Phys. A (1995) paper "Spectral zeta functions for q-Bessel equations" was not located.
  - Conclusion: spectral-zeta side only.
- **q-analogues (recurrence coefficients explicit or geometric).**
  - Koelink–Van Assche, arXiv:math/9502227 (WebFetch). The measures are supported on ±1/j_k^{ν−1} (Hahn–Exton q-Bessel zeros), with
    explicit λ_{2n} = q^n, λ_{2n+1} = q^{ν+3n+1} (resp. q^{n+ν}).
  - Joshi–Lasic Latimer, arXiv:2211.12658, q-Freud II on q^k. Thm 1.6 has "α_n = q^{−n}(q + O(q^{n/2}))" (WebFetch).
  - In the q-world the corrections are geometric. The analogue of ζ(−jp)-monomials does not arise.
  - My observation: on a q-lattice a Hurwitz offset q^{k+δ} is a dilation, so "shift = exponent change" is trivial there.
- **Bessel zeta at 0: Naber, Bruck & Costello, "The Bessel zeta function", arXiv:2211.05765 (2022)** (WebFetch).
  - "ζ_ν(0) = −(1/2)(ν + 1/2)".
  - ζ_ν(−2k) via their β_{2k} (Eq. 106); Hawkins cited for ζ_ν(−2m) (Eq. 21).
  - Poles at s = 1 and at negative odd integers, with residues (Eqs. 14, 108).
  - This confirms the input Z(0) = −ν/2 − ¼ used in JZC_W §1.4 and Paper IV §8 for Bessel zeros (invariant under λ = (j/π)^P at w = 0).
    KNOWN input.
- **Weight singularities ↔ power terms in recurrence coefficients (continuous weights; the closest "phenomenon" precedent for the
  pole law).**
  - Magnus, "Asymptotics for the simplest generalized Jacobi polynomials recurrence coefficients from Freud's equations: numerical
    explorations", Ann. Numer. Math. 2 (1995) 311–325, arXiv:math/9403214 (WebFetch). Features of the weight "can somehow be 'read'
    in the sequence of the recurrence coefficients". For a mild interior singularity, Hodges' result gives a_n − ½ decaying like
    n^{−γ−1}, oscillating. Endpoint singularities are referred to Aptekarev.
  - Foulquié Moreno, Martínez-Finkelshtein & Sousa, arXiv:0905.2753 (WebFetch). Magnus's conjecture is proved: a complete 1/n
    expansion, with leading oscillating n⁻¹ terms whose amplitude M depends on the singularity exponent γ and the jump.
  - Wu, arXiv:1807.00088: Fisher–Hartwig factor at the soft edge; n^{−1/3}, n^{−2/3} terms with Painlevé coefficients (WebFetch).
  - Trogdon, arXiv:2412.18656: non-analytic perturbations change error sizes, not the form (WebFetch).
  - **Reading.** For continuous weights it is known that singularity data (location, exponent) determine specific power/oscillating
    terms in a_n, b_n. K/W is an instance at an accumulation point of a discrete spectrum, where the "singularity data" are the poles
    and values of Z(−w), and the kernel W(q)π cot(πq) is new as far as located.
  - The Magnus 1985 recursion-method chapter ("Asymptotic behaviour of continued fraction coefficients related to singularities of
    the weight function") was **not** confirmed: WebFetch of Magnus 1995 found no such title in its references.
- **Murugan, Van Zyl & Watanabe, "Spectral Topology and Universal Krylov Dynamics", arXiv:2608.07258 (7 Aug 2026)** (WebFetch,
  abstract and section summary).
  - "determine their sub-leading corrections from endpoint data".
  - Soft edge: O(n⁻²) corrections from the density's endpoint values.
  - Hard edge: "the n⁻² coefficient depends on the edge exponent α, using a Bessel parametrix"; Jacobi is checked.
  - Gaps: quasiperiodic oscillation at the filling fraction.
  - Meixner–Pollaczek offset b₀ = α(λ − ½); a "cross-class law for the 1/n correction (7.19)", conjectural.
  - WebFetch: "The paper does not discuss Weyl laws, zeta functions, heat-kernel coefficients, or discrete spectra."
  - **The closest physics relative of Z1/Z3. It must be read in full** (unread decisive item U3): its hard-edge n⁻² law is the
    continuum analogue of f₂ = −(p+2)α²/8 + (p+1)/12 and should be compared.
- **Other searches with nothing relevant.** Monien/Gauss-for-sums follow-ups: Milovanović, "Summation of series and Gaussian
  quadratures II" (WebFetch): hyperbolic/Einstein/Fermi weights, numerical coefficients only. Basor–Chen–Haq, arXiv:1401.2073:
  elliptic weights, continuous. Dai–Yao, arXiv:2104.03563: nodes k²/N², not accumulating, O(1/n) only. Ou–Wong, Anal. Appl. 8
  (2010/11): Charlier.

### 1.2 What is (not) there
- **Known.**
  - Moment problems whose moments are spectral zeta values at positive integers, for Bessel zeros (Lommel; Grosjean 1984 relations;
    2406.09746 for J′ zeros) and q-Bessel zeros.
  - Exact rational recurrence coefficients in the Lommel and Tricomi–Carlitz families, in which the lattice offset enters only through
    a shifted index.
  - The continuous-weight principle that singularity data fix specific power/oscillating terms.
  - Hard/soft-edge subleading laws for continuous equilibrium densities.
- **Not found.**
  - Any large-n expansion of recurrence coefficients whose coefficients are spectral zeta values at non-positive arguments
    (ζ(−jp), Z(0), Z(−j)).
  - Monomials n^{−1−jp} with C(2j,j)pc^j weights.
  - A natural index containing −Z(0).
  - The g_j = A_j + B_jα² dressings with the 1/(2j−1) pole.
  - The (3p+1)/(2p) second-order coefficient.

### 1.3 Verdict Z1
- **Theorem K / N.6 as stated: NOT FOUND.**
- **Exact special cases: KNOWN as formulas, not as zeta statements.** Lommel (p = 2), plus Tricomi–Carlitz (p = 1, excluded by N.6),
  newly recorded here.
- **Phenomenon (singularity → power term): PARTIALLY KNOWN** for continuous weights.

## 2. Z2: Theorem H (Hurwitz shift = Szegő-exponent shift)

### 2.1 Findings
- Hurwitz's formula ζ(−jp, a) as a Fourier series: KNOWN, quoted from Dixit–Kumar (Paper IV §10 already says so).
- No source located states that shifting a power lattice (k+δ)^p acts on the Jacobi coefficients as the Szegő-exponent change
  β → β + 2δ at fixed Bessel order.
- Exact instances where a lattice offset enters only through the index:
  - Lommel: recurrence in n + ν, nodes j_{ν−1,k} with McMahon offset ν/2 − ¼ (novelty_SPEC §1.3 already checked d₁ = −pα/2 + pZ(0) = −μ);
  - Tricomi–Carlitz: recurrence in n + α, nodes 1/(k + α) (§1.1 above);
  - the q-lattice case, where the offset is a dilation (trivial).
- None of these sources makes the Hurwitz/Szegő identification. In Lommel, ν also changes the Bessel order, so it is not a pure
  Hurwitz test (JZC_W Prop W.2 row "Bessel zeros").

### 2.2 Verdict Z2
**NOT FOUND** as a theorem. **Implicit exact instances: PARTIALLY KNOWN** (classical recurrences; the zeta reading is this repo's).
Suggestion, not done: Tricomi–Carlitz is a pure-offset family (order fixed, offset α free). Its exact β_n gives a clean check of the
p = 1 analogue of rule H, with the Stirling mass tilt handled by W3.

## 3. Z3: Conjecture W, the κ-family theorem, Toda times, pole law, drums

### 3.1 Findings
- **Toda.** That the Toda flow is the exponential tilt dμ_t ∝ e^{−tx}dμ is classical; Paper IV proves its identities in the text
  (Lemma todatilt).
  - Continuum-limit Toda for recurrence coefficients: Ercolani–McLaughlin–Pierce (NOVELTY_JZC §3).
  - Unbounded-Jacobi Toda via τ-functions: arXiv:2604.05434 (emergentmind summary only; arXiv blocked by the WebFetch allowlist).
  - None of these has Toda times equal to spectral zeta values, or "one linear response −(pρW(ρ)/2)t_ρ for every time".
- **Lanczos / recursion method / Krylov.**
  - Parker, Cao, Avdoshkin, Scaffidi & Altman, "A Universal Operator Growth Hypothesis", arXiv:1812.08657 (WebFetch). "the
    hypothesis is equivalent to the exponential decay of the spectral function at high frequency". For b_n ~ n^δ ↔
    Φ(ω) ~ exp(−|ω/ω₀|^{1/δ}) they cite Lubinsky's survey and Magnus's recursion-method proceedings. This is leading order only.
  - Avdoshkin, Dymarsky & Smolkin, arXiv:2212.14429 (WebFetch), on discrete spectra (CFT on S³). Two slopes are "probably due to
    periodicity of C(t) … or more broadly due to f²(ω) being a sum of delta-functions". Persistent staggering ↔ "mass gap",
    conjectural. "Zeta functions do not appear in the analysis of b_n"; a polygamma term appears in d_n for S³.
  - Camargo et al., arXiv:2306.11632 (PRD 109, 046017), circle and stadium billiards. Integrability vs erratic b_n. No Weyl,
    perimeter, corner or zeta terms (WebFetch, abstract).
  - Qu, JHEP 05 (2026) 225 and arXiv:2608.16982: large-N mapping between Lanczos and recursion coefficients; leading density only.
  - Viswanath–Müller, *The Recursion Method* (Springer LNP m23, 1994): only the book page was reached. The abstract mentions
    "infrared singularities, bandwidths, and line shapes" (WebFetch). Chapters not seen.
- **Inverse spectral theory.**
  - Killip–Simon / Case sum rules (math-ph/0112008, math-ph/0206023; titles only) concern perturbations of the free Jacobi matrix
    with essential spectrum [−2, 2]. They are not the compact/discrete regime.
  - Silva–Weder, arXiv:0707.1732 and math-ph/0511078: exact two-spectra reconstruction, "no asymptotic formulas" (WebFetch).
  - Boutet de Monvel–Janas–Zielinski, arXiv:1206.1763, Thm 1.1 (WebFetch): diagonal-dominated band matrices,
    λ_n = d(n) + O(n^{δ−κ}). This is the direct problem, in a different regime, with no zeta constants.
  - Yafaev, arXiv:2202.02087 and arXiv:2011.14987: polynomial asymptotics for growing a_n; Freud a_n = αn^{1/β}(1 + o(1)).
  - Tur, Math. Notes 74 (2003) 425: "very rapidly decreasing weights", abstract only.
  - Kasahara–Watanabe (Krein/Kotani strings, Kyoto J. Math. 2010): the page was blocked. To my knowledge it is Tauberian/leading
    order (unverified).
- **Voros / zeta-regularised determinants.** Voros 1987 (CMP 110, "Spectral functions, special functions and the Selberg zeta
  function") was located; the PDF was not read. novelty_SPEC §6 already records the Voros-type link between zeta values and large-λ
  expansions of log D. Nothing new.
- **Drums.** Looi–Sher, arXiv:2512.04422 (heat trace with curved corners, to t^{1/2}) is spectral geometry with no Lanczos content
  (WebFetch). Together with the first pass, no source reads perimeter or corner invariants from Jacobi/Lanczos coefficients.

### 3.2 Verdict Z3
- **Conjecture W (general statement), the κ-family theorem (P K.12 + Prop K.12′), the identification of Toda times with −2Z(−j)/j
  + B_j, the multiplicity rule, W′'s half-integer term: NOT FOUND.**
- **Ingredients: KNOWN** (Toda = tilt; spectral zeta values/residues; leading-order growth ↔ tail).
- **"Subleading Lanczos asymptotics from spectral endpoint data": PARTIALLY KNOWN for continuous densities** (arXiv:2608.07258).
- **Drum reading: NOT FOUND** (second pass).

## 4. Z4: large order

### 4.1 Findings
- **Mariño, Schiappa & Weiss, "Nonperturbative effects and the large-order behavior of matrix models and topological strings",
  arXiv:0711.1954** (WebFetch).
  - Genus coefficients are F_g ~ (A^{−2g−b}/π)Γ(2g+b)μ₁[1 + …] (Eq. 2.17), with A the one-instanton action, computed "directly in
    the matrix model" from "geometric data which only depend on the spectral curve".
  - The excerpt covers free energies, not the R_n string-equation expansion. Complex or oscillating actions are not discussed in the
    excerpt.
  - Setting: varying weights e^{−NV}.
- **Costin & Garoufalidis, "Resurgence of the Euler–MacLaurin summation formula", arXiv:math/0703641** (WebFetch).
  - "for a typical analytic function, it is a divergent (Gevrey-1) series".
  - The Borel transform has singularities "at points 2πin·ω and 2πin(ω−1), where ω is a singularity of f′" (Thm 2).
  - Relevance (HEURISTIC, mine): the zeta layer comes from Euler–Maclaurin-type sums over the lattice. Complex Borel singularities of
    this kind are a candidate source for a complex action. This was not tested, and JZC_M4 §9 locates the divergence in the
    β-free **integer** layer (the decoupled continuum model), so the link is unclear.
- arXiv:1904.07217, arXiv:1802.10441 (resurgence primers): titles only.

### 4.2 Verdict Z4
- **The phenomenon (divergent 1/N expansions of OP/matrix-model data, Borel singularities = actions): PARTIALLY KNOWN** (varying
  weights).
- **For a fixed discrete measure with a hard edge, and the complex pair A(p): NOT FOUND.** A(p) is unidentified in the repo, so there
  is nothing to compare.

## 5. Unread decisive items

| # | Item | Why decisive | For |
|---|---|---|---|
| U1 | Grosjean, JCAM (1984), doi:10.1016/0377-0427(84)90044-X, full text | Only classical place found that systematically ties Rayleigh sums to Lommel orthogonality; check it has no n-asymptotics or analytic continuation | Z1 |
| U2 | Kvitsinsky, J. Phys. A 28 (1995) "Spectral zeta functions for q-Bessel equations" (not located) and TMF 107 (1996) full text | Spectral zeta of q-Bessel zeros with poles/residues; check for any link to Lommel recurrences | Z1, Z3 |
| U3 | Murugan–Van Zyl–Watanabe, arXiv:2608.07258, §4.4, §7 | Hard-edge n⁻² law from the edge exponent; the closest modern relative; compare with f₂ and with W's d₁ | Z1, Z3 |
| U4 | Magnus, recursion-method chapter (Pettifor–Weaire eds., Springer 1985; title unconfirmed); Hodges 1977; Turchi–Ducastelle–Tréglia 1982 | Classical singularity ↔ continued-fraction-coefficient dictionary; may contain endpoint power-law terms analogous to the pole law | Z1, Z3 |
| U5 | Avdoshkin–Dymarsky–Smolkin, arXiv:2212.14429, App. C–E (S³ discrete spectrum, polygamma in d_n) | Only located case of Lanczos coefficients of a discrete spectrum with a special-function subleading term | Z3 |
| U6 | arXiv:2406.09746 §3 (Neumann–Bessel γ_n) | Exact test of W (Neumann offset, mass tilt), not prior art | Z3 (test) |
| U7 | Wu–Lin–Xu–Zhao arXiv:1410.3948 and Goh–Wimp 1994 (Tricomi–Carlitz) | Confirm recurrence/masses at the source; check that no recurrence-coefficient asymptotics with a zeta reading exists | Z1, Z2 |
| U8 | Mariño–Schiappa–Weiss §§3–5 (string-equation R_n large order, complex actions) | Phenomenon precedent for Z4 | Z4 |
| U9 | Beckermann–Kuijlaars, SINUM 39 (2001), Thm 2.1 | Carried over from NOVELTY_JZC (Theorem Q) | (Q) |
| U10 | MathSciNet/zbMATH: "recurrence coefficients" ∧ ("zeta function" ∨ "Rayleigh") ∧ "asymptotic expansion" | Unavailable here | all |

## 6. Recommended novelty labels and attribution wording

### 6.1 Labels (Rule L field; each remains subject to U1–U10)
- Theorem K / Theorem N.6 (ζ(−jp)-monomial expansion, natural index with −Z(0), g_j, (3p+1)/(2p)): **POSSIBLY-NEW**.
- Theorem Σ / Cor Σ.1 (evenness without a string equation): **POSSIBLY-NEW**, with Bleher–Its as the known varying-weight analogue
  (NOVELTY_JZC).
- Theorem H (Hurwitz = Szegő shift): **POSSIBLY-NEW**, citing Lommel and Tricomi–Carlitz as exact instances, and Dixit–Kumar for
  Hurwitz's formula.
- κ-family theorem: **POSSIBLY-NEW**.
- Conjecture W: novelty of the statement **POSSIBLY-NEW** (it is a CONJECTURE). The pole-law kernel W(q)π cot(πq) and the zeta-time
  Toda reading: NOT FOUND.
- Drum reading (§8 "Drums"): **POSSIBLY-NEW** (NUMERICAL).
- Large order: **UNCHECKED → keep UNCHECKED**, phrased as a numerical observation with a known phenomenon class. A(p) is unidentified.

### 6.2 Suggested wording for Paper IV §10 (sec8.tex), "Spectral data and Jacobi parameters"
All cited works are second-hand (WebFetch) and need Rule C reading and bib entries before use.

> Orthogonal polynomials whose moments are spectral zeta values at positive integers are classical for Bessel zeros: the Lommel
> polynomials are orthogonal on the reciprocal zeros [Dickinson; VA], and their orthogonality yields linear relations between
> Rayleigh's sums [Grosjean]; analogues exist for zeros of $J_\nu'$ [arXiv:2406.09746] and for $q$-Bessel zeros [Koelink–Van Assche].
> The Tricomi–Carlitz polynomials, orthogonal on $\pm(k+\alpha)^{-1/2}$ [Carlitz; Goh–Wimp], give a further family with nodes
> accumulating at $0$ and explicit recurrence coefficients; there the lattice offset enters only through the index $n+\alpha$, as it
> does in Theorem~\ref{thm:H}. Positive Jacobi matrices with compact inverse are studied in \cite{StovicekSwiderski}, where the
> asymptotics of the polynomials at fixed argument are expressed through a regularised characteristic function; asymptotics of the
> Jacobi parameters are not treated there. We know of no expansion of recurrence coefficients in terms of spectral zeta values at
> non-positive arguments, as in Theorems~\ref{thm:K} and~\ref{thm:N6}. For continuous weights it is known that singularities of the
> weight produce identifiable power-law or oscillating terms in the recurrence coefficients [Magnus 1995; Foulquié
> Moreno–Martínez-Finkelshtein–Sousa]; the pole terms of Theorem~\ref{thm:K} and Conjecture~\ref{conj:W} may be viewed as an instance
> of this principle at the accumulation point of a discrete spectrum, with the poles of $Z(-w)$ as singularity data.

> In the recursion-method and Krylov-complexity literature the growth of Lanczos coefficients is tied to the tail of the spectral
> function [Parker et al., citing Lubinsky], and subleading corrections have recently been derived from the endpoint data of
> continuous equilibrium densities, including a hard-edge $n^{-2}$ term [Murugan–Van Zyl–Watanabe]; for discrete spectra only
> qualitative effects such as staggering are reported [Avdoshkin–Dymarsky–Smolkin]. We have not found a reading of Weyl-law or
> heat-trace invariants (perimeter, corners) from Jacobi or Lanczos coefficients.

> Divergent $1/N$ expansions whose large-order behaviour is governed by an instanton action are familiar for matrix models with
> varying weights [Mariño–Schiappa–Weiss], and Euler–Maclaurin remainders are resurgent [Costin–Garoufalidis]; we have not found a
> large-order analysis for a fixed discrete measure, and the action of Section~\ref{sec:conj-even} is not identified.

Keep the existing sentence on Bessel zeros, and add for Z(0): "the value $Z(0)=-\frac{\nu}{2}-\frac14$ for Bessel zeros is the value
at $0$ of the Bessel zeta function [Naber–Bruck–Costello; Hawkins]".

### 6.3 Suggested additions to Paper IV §8 (sec6.tex), as tests only (no claims)
- Tricomi–Carlitz (p = 1, pure offset α, exact β_n) as the p = 1 analogue of the Hurwitz test of §8 "Hurwitz lattices", once a p = 1
  version of rule H exists (JZC_W §1.6 obstacle).
- Neumann–Bessel (arXiv:2406.09746): an exact all-order check of Conjecture W with a non-Dirichlet offset and nonzero Toda times.
  Derive γ_n's 1/n expansion from Lommel asymptotics at fixed argument and compare with W's prediction **before** looking at the
  coefficients (Rule X).

## 7. Queries (WebSearch; standard unless noted)

1. Kvitsinsky spectral zeta functions Lommel polynomials Bessel zeros
2. Šťovíček Świderski orthogonal polynomials moments Riemann zeta function Jacobi matrix
3. Štampach Šťovíček spectral zeta function Jacobi operator compact inverse Bessel zeros
4. operator growth hypothesis Lanczos coefficients asymptotics spectral density singularity subleading corrections
5. Ismail Bessel zeros Rayleigh function sums Lommel polynomials orthogonality measure moments continued fraction
6. Kvitsinsky "spectral zeta functions" q-Bessel equations J. Phys. A 1995 Lommel
7. "spectral zeta function" Jacobi matrix Štampach Šťovíček explicit formula Rayleigh
8. Štampach Šťovíček spectral zeta function of Jacobi matrix "zeta function" eigenvalues formula Jacobi parameters
9. Grosjean Lommel polynomials Bessel zeros sums of inverse powers recurrence
10. Magnus asymptotic behaviour of continued fraction coefficients related to singularities of the weight function recursion method
11. Lanczos coefficients discrete spectrum Krylov complexity b_n asymptotics determined by density of states Weyl law power law n^{1/d}
12. Lanczos coefficients compact space discrete spectrum "zeta function" Krylov complexity sphere CFT staggering subleading
13. eigenvalue asymptotics Jacobi matrices power-like entries Boutet de Monvel Zielinski Malejki higher order terms
14. Janas Naboko spectral asymptotics unbounded Jacobi matrices discrete spectrum eigenvalues λ_k asymptotic expansion entries n^α
15. Yafaev Jacobi operators rapidly increasing coefficients eigenvalue asymptotics quasiclassical
16. (extended) orthogonal polynomials whose moments are values of the Riemann zeta function ζ(n+2) recurrence coefficients asymptotics
17. Hankel determinants Dirichlet series moments ζ(s+k) asymptotic recurrence coefficients orthogonal polynomials measure Σ n^{-s} δ_{1/n}
18. Gaussian quadrature for sums Monien follow-up recurrence coefficients asymptotic expansion zeta function continued fraction Riemann sums of 1/k^s
19. Riemann-Hilbert asymptotics discrete orthogonal polynomials nodes accumulating at a point infinite lattice non-uniform hard edge saturated region
20. Bleher Liechty uniform asymptotics discrete orthogonal polynomials infinite lattice recurrence coefficients full asymptotic expansion
21. Kasahara Krein string spectral function asymptotics regular variation Stieltjes continued fraction coefficients eigenvalue counting inverse problem
22. "Lanczos coefficients" "heat kernel" coefficients asymptotic expansion inverse spectral geometry Laplacian eigenvalues recurrence coefficients perimeter
23. regularized trace formula compact Jacobi operator eigenvalues power decay sum rules Jacobi parameters zeta-regularized determinant
24. Viswanath Müller recursion method continued fraction coefficients asymptotic behavior spectral density band edge singularity terminator
25. "Lanczos coefficients" "zeta function" asymptotic expansion
26. (extended) recurrence coefficients orthogonal polynomials asymptotic expansion "Hurwitz zeta" OR "zeta(-" coefficients discrete measure accumulation point
27. Mariño Schiappa Weiss nonperturbative effects large-order behavior matrix models recurrence coefficients R_n instanton action Borel
28. resurgence asymptotic expansion recurrence coefficients orthogonal polynomials fixed weight large n divergent series Borel singularities complex conjugate
29. Toda lattice flow times spectral zeta function values Jacobi matrix discrete spectrum asymptotics recurrence coefficients regularized determinant tau function
30. Voros zeta-regularized determinant spectral asymptotics large eigenvalue expansion zeta values negative integers Weyl series "Voros" 1987 spectral functions
31. arXiv 2412.14463 (to identify a Toda hit; not identified)
32. (extended) asymptotics of recurrence coefficients discrete measure supported on {1/k^p} masses k^{-s} orthogonal polynomials Riemann-Hilbert lattice accumulating at origin
33. Krylov complexity quantum billiards Lanczos coefficients Weyl law density of states Hashimoto stadium spread complexity
34. (extended) "Lanczos coefficients" inverse problem reconstruct density of states boundary terms Weyl expansion perimeter corner billiard
35. (extended) recurrence coefficients asymptotic expansion weight with non-analytic perturbation at hard edge x^alpha(1 + c x^gamma) fractional powers n^{-2gamma} terms Riemann-Hilbert
36. Case sum rules Killip Simon Jacobi parameters spectral measure higher order sum rules eigenvalue power sums compact perturbation
37. Silva Jacobi matrices discrete spectrum eigenvalue asymptotics inverse problem two spectra power growth entries
38. Dickinson Pollak Wannier Lommel polynomials orthogonality spectral measure reciprocal Bessel zeros Rayleigh function moments 1956
39. zeta function of Bessel zeros analytic continuation value at zero ζ_ν(0) = -(2ν+1)/4 Stolarsky Elizalde Leseduarte Romeo
40. Lubinsky Freud conjecture recurrence coefficients exponential weights asymptotics a_n/n^{1/beta} Mhaskar Saff proof 1988
41. Hodges 1977 Van Hove singularities continued fraction coefficients asymptotic oscillations Turchi Ducastelle Treglia band gaps
42. Aptekarev endpoint singularity weight recurrence coefficients asymptotics power n^{-2gamma} Jacobi weight non-smooth at endpoint
43. (extended) Jacobi matrix whose moments are spectral zeta values Tr L^{-k} of a differential operator, continued fraction of resolvent at zero, recurrence coefficients asymptotics Weyl

**WebFetch reads.**
- Full or long text: arXiv:2409.19644v2 (HTML), arXiv:1410.3948 (PDF), arXiv:2406.09746 (PDF), arXiv:2212.14429v3 (HTML),
  arXiv:0905.2753 (ar5iv), Magnus 1995 (author PDF), arXiv:1206.1763 (ar5iv).
- Abstract or summary pages: mathnet tmf1165, arXiv:1904.13199, 1702.07496, 1510.01454, 1301.2125, 2608.07258, 2104.03563,
  2211.12658, math/9502227, 2211.05765, 1812.08657, 0711.1954, math/0703641, 2306.11632, 2608.16982, JHEP05(2026)225, 2512.04422,
  1807.00088, 2412.18656, 2202.02087, 2011.14987, math-ph/0511078, 0707.1732, 1401.2073, Milovanović (SANU PDF), the Grosjean
  datalearner page, the Ou–Wong ResearchGate page, the recursion-method book page, Tur (Springer).
- Failed: the Kasahara–Watanabe Project Euclid PDF (bot wall); arXiv:2604.05434 and export.arxiv.org/abs/2412.14463 (not on the
  allowlist); arXiv:2608.08455 (empty PDF).

## 8. Actions (suggested; nothing done here)
1. Discharged (second-hand): NOVELTY_JZC action 3 (Šťovíček–Świderski has no Jacobi-parameter asymptotics). Rule C reading is still
   needed before citing.
2. Read U3 (arXiv:2608.07258) and U4 (Hodges/Magnus recursion-method literature). These are the two places where a "spectral data →
   subleading recurrence coefficients" dictionary could already exist.
3. Add bib entries (Grosjean; Carlitz/Goh–Wimp; Koelink–Van Assche; Naber–Bruck–Costello; Magnus 1995; Foulquié Moreno et al.;
   Parker et al.; Murugan et al.; Avdoshkin et al.; Mariño–Schiappa–Weiss; Costin–Garoufalidis) only after Rule C reading.
4. Tests, not literature: Tricomi–Carlitz (p = 1 offset) and Neumann–Bessel (W) as in §6.3.
5. Rule L logging: the queries are here; the LOG.md pointer is left to the session.
