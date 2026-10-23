# NOVELTY_TODA: Rule L search for cluster T (Theorem T, Theorem Σ, index-shift law Thm SH)

Date: 2026-10-23. Branch plan-e2-d2. Searcher: a subagent of the JZC session. This file covers Rule L only. It records what the search
found. It does not review the mathematics (Rule R) or the citations (Rule C). The format follows NOVELTY_JZC.md.

- **Network.** The shell cannot reach arxiv.org. Every quote below came through WebFetch, which summarises the page with a small model
  and caps quotes at about 125 characters. All quotes marked "(WebFetch)" are therefore second-hand. Under Rule C, each must be re-read
  in the source before it is cited. Equation, theorem and section numbers are as WebFetch relayed them. Where WebFetch had only an
  abstract or a partial excerpt, this is stated.
- **Verdict scale.** KNOWN: found essentially as stated. PARTIALLY KNOWN: the named part or the mechanism was found in another setting.
  NOT FOUND: not located by the queries listed. NOT FOUND describes this search; it is not evidence of novelty. MathSciNet and zbMATH
  were unavailable.
- **Items.**
  - T = JZC_TODA Theorem T / T_H, Lemma T.1, Lemma T.2 (the Baire transfer); Paper IV Lemma `lem:todatilt`, Theorem `thm:toda`.
  - Σ = JZC_SIGMA Theorem Σ (frame identity FI, m-frame); Paper IV Theorem `thm:reflect`, Theorem `thm:shift`, Corollary `cor:even`.
  - SH = JZC_SHIFT Thm SH, Lemmas D, R, H, LB, Prop DR; Paper IV Theorem `thm:indexshift`.

## 0. Summary

| Item | Verdict | Closest prior work |
|---|---|---|
| **T.1** Toda hierarchy for exponential tilts e^{Σt_jx^j}μ: ∂_{t_j}log h_n = (J^j)_{nn}, etc. | **KNOWN** (classical). JZC_TODA §9 already says so. | Van Assche, arXiv:2202.11017, Lemma 2.1, Lemma 2.3, Thm 2.4 (recorded in JZC_TODA §9; abstract re-checked here) |
| **T (ii)** The layers of the asymptotic expansion in n of a *fixed* measure satisfy the Toda hierarchy as formal identities in the rescaled times u_j (μ_j = −u_jn^{−jp}, shifts at fixed unscaled time), with zeta values as base times and a Baire transfer from exact flows to formal series | **PARTIALLY KNOWN as a mechanism, NOT FOUND in this setting.** The mechanism (Toda equations with shifted indices, re-expanded in 1/n, as a hierarchy of equations for the coefficients of an asymptotic expansion) is the "continuum limit of Toda" method of Ercolani–McLaughlin–Pierce (EMP 2008, §4 "Fundamental Asymptotic Principle") for *varying* weights e^{−N(x²/2+tx^{2ν})}, with s = n/N. NOT FOUND: the same for a fixed measure with no N, where the times enter as n^{−jp}u_j; zeta values as times; the Baire argument. | EMP, arXiv:math-ph/0606010 (CMP 2008), Thm 2.2, §4, Lemma 4.3; Ercolani–Pierce arXiv:1106.1143; Ercolani arXiv:0912.1904 |
| **Σ (reflection)** d_k(p, −β−2, ν) = (−1)^k d_k(p, β, ν), via the ℤ₂-grading span{I, σ₂} (even k) / span{σ₃, iσ₁} (odd k) of the jump corrections | **PARTIALLY KNOWN (the mechanism).** Kuijlaars–Tibboel prove the vanishing of the odd powers of a_{n,n} with the same grading: "For k odd, R_k(z) is a linear combination of σ₁ and σ₃", and for k even of I and σ₂ (Lemma 4.1). This is for varying weights and soft (Airy) edges; there is no β ↦ −β−2 reflection. | Kuijlaars–Tibboel, arXiv:0708.3956 (2007), Lemma 4.1, eqs. (3.21)–(3.22) |
| **Σ (shift / FI / natural index N = n + (β+1)/2; evenness of F_p in N to all orders)** | **PARTIALLY KNOWN (the phenomenon), NOT FOUND (the mechanism and the setting).** Evenness after a half-index shift is a theorem for varying weights (Bleher–Its 2005 Thm 5.2 via string-equation reflection; see NOVELTY_JZC item N). There is an exact index–exponent coupling in a semiclassical Laguerre case: z_n = n + α/2 and PIV parameters A = 1 + 2n + α, B = −2α² (Filipuk–Van Assche–Zhang). That is the same pairing as "N and ν²" at β = ν = α. NOT FOUND: the decoupled (β, ν) model; the frame identity B(n+γ; β−2γ, ν) = (1+γ/n)^pB(n; β, ν); a proof by steepest descent in a non-integer frame m = n + γ with the gauge z^{γσ₃}. | Bleher–Its AIF 55 (2005) Thm 5.2, Lemma 5.3; Filipuk–Van Assche–Zhang arXiv:1105.5229, Thm 2.1, eq. (13); EMP Thm 2.2 |
| **SH (i)–(ii)** Defect grading; the defect-0 parts solve dispersionless Toda; the hard-edge line a = 2b is invariant; Hopf equations ∂_{t_j}b = V_j(b)∂_nb solved by characteristics: b = cx^{−p}, x = n + Σt_jV_j(cx^{−p}); Lagrange–Bürmann coefficients (p+1+S)_{m−1}/(β!p^{m−1}) | **Mechanism KNOWN (genus zero of map enumeration). Setting NOT FOUND.** Leading-order continuum Toda = inviscid Burgers with power nonlinearity, solved implicitly by characteristics: Ercolani 2011 §2.3, "f_s = c_ν f^ν f_w", f(0, w) = w, "1 = z_0(s) − c_νs z_0(s)^ν" (eq. 30); EMP eq. (2.6). The planar string equation R = t + 3tR² and Lagrange inversion for planar-map counts are textbook (Bouttier, arXiv:1104.3003, §26.4). The endpoints of the support evolve by dToda (Konopelchenko–Martínez Alonso–Medina); a ± 2b as endpoints is standard. NOT FOUND: power-law initial data b(n, 0) = cn^{−p} on a fixed measure; the hard-edge reduction a = 2b as the invariant line; fractional and pole exponents; the explicit multi-time closed form with rising factorial; zeta times. | Ercolani, arXiv:0912.1904 (Nonlinearity 2011) §§2.3–2.4; EMP math-ph/0606010 eq. (2.6), (2.7); Ercolani–Waters arXiv:1907.08026; Bouttier arXiv:1104.3003; Konopelchenko–Martínez Alonso–Medina arXiv:1005.4773 |
| **SH dressings** (defect ≥ 2 parts = dispersive corrections; not an index reparametrisation) | **Mechanism KNOWN** (the higher-genus z_g of EMP come from the k^{−2g} orders of the same continuum Toda scheme, as forced linear ODEs). The specific results (g_j split, h₂, h(j, k), the "dressed shift fails" observation): NOT FOUND. | EMP Thm 2.2, eqs. (2.7)–(2.9) |

**Bottom line.** The *integrable mechanisms* of cluster T are known.
- Toda for tilts is classical.
- Genus zero of continuum Toda is a Hopf/Burgers equation solved by characteristics; its implicit equation gives coefficients by Lagrange inversion.
- Odd-order vanishing comes from a ℤ₂-grading of the RH corrections.
- Evenness holds after a half-index shift.

What was NOT FOUND is the *setting*: a fixed discrete measure whose nodes accumulate at a hard edge (b_n ~ cn^{−p}, no large parameter N), with fractional and pole exponents and zeta-valued base times. Also NOT FOUND are two devices:
- the transfer from exact flows to formal layers (Baire);
- the second, non-integer steepest-descent frame that proves FI.

## 1. Item T: Toda flows and the layers of a fixed measure

### 1.1 Prior work found
- **Van Assche, "Orthogonal polynomials, Toda lattices and Painlevé equations", arXiv:2202.11017.** (WebFetch, abstract): "We give
  a survey of the connection between orthogonal polynomials, Toda lattices and related lattices". WebFetch summary: the survey
  "doesn't treat large-n asymptotic expansions of recurrence coefficients for a fixed measure"; there is no zeta and no hard-edge
  scaling.
  - The content of Lemma T.1 (Lemma 2.1, Thm 2.4 there) is recorded in JZC_TODA §9.
  - **Lemma T.1: KNOWN.** Paper IV already calls it classical in substance. It should cite Van Assche's survey, and Moser/Flaschka for j = 1.
- **Ercolani, McLaughlin & Pierce, "Random matrices, graphical enumeration and the continuum limit of Toda lattices",
  arXiv:math-ph/0606010 (CMP 278 (2008)).** (WebFetch, PDF):
  - Thm 2.2: "b²k ≃ k(z0(s) + 1/k² z1(s) + 1/k⁴ z2(s) + ···)", with s = −2k^{ν−1}t "the self-similar variable" (eq. 4.8).
  - Method: the Toda equations in the coupling t, with shifted indices k ± ℓ Taylor-expanded in ℓ/k and re-summed ("Fundamental
    Asymptotic Principle", §4). A centered-difference lemma (Lemma 4.3) "produces only even orders".
  - Genus zero: "z′0(s) = cν z0(s)^ν (z0(s) + (ν − 1)s z′0(s))", z_0(0) = 1, integrated to eq. (2.6)/(5.1) "1 = z0(s) − cν s z0(s)^ν".
  - Higher orders: "the k^{−2g} equation of the scheme gives the linear ODE (2.7) for z_g, with forcing from lower orders" (WebFetch
    paraphrase).
  - Lagrange inversion is not named; Taylor coefficients are extracted by a contour integral (§3.5).
  - **Relation to T.** This is the closest precedent for turning exact Toda equations into a hierarchy for the coefficients of an
    asymptotic expansion. Their large parameter is N (varying weight), and the expansion variable is k with s self-similar.
    - In T there is no N. The "self-similar" structure comes from b_n ~ cn^{−p} and the substitution μ_j = −u_jn^{−jp}.
    - T's statement that the shift acts at fixed unscaled time (μ_j(n+i) = μ_j(n)(1+i/n)^{−jp}) is the analogue of EMP's
      re-expansion of shifted terms at fixed t.
    - EMP's validity of the expansion comes from the RH analysis of the partition function (EM 2003). T's comes from Theorem N.6
      plus the Baire argument (Lemma T.2), which has no counterpart found.
- **Ercolani & Pierce, arXiv:1106.1143 (odd weights).** (WebFetch): a 2×2 leading system (eq. 4.6) with matrix
  [[1+6sh₀, 6s], [6sf₀, 1+6sh₀]]. It is integrated directly; "Riemann invariants, characteristics, or hodograph" are not mentioned.
  The higher orders are "a hierarchy of near-conservation laws". Endpoints [A, B] = [u₀ − 2√z₀, u₀ + 2√z₀]. Expansion: a_{n+k} in all
  powers of 1/n, b² in even powers; "no n+1/2 shift".
- **Ercolani & Waters, arXiv:1907.08026** (the fetched PDF is titled "A PDE Approach to the Combinatorics of the Full Map Enumeration
  Problem: Exact Solutions and their Universal Character"; the search listing gave a different title, so check which version is
  cited). (WebFetch): general V_t = ½λ² + Σt_jλ^j (eq. 2.3); string equations "0 = (ℒ + jξℒ^{j−1})_{n,n}", "n/N = (ℒ +
  jξℒ^{j−1})_{n,n−1}" (2.12–2.13); the even-valence implicit relation ξ = (x − f₀)/(c_jf₀^{j/2}), c_j = j·binom(j−1, j/2−1).
  No hard edge.
- **Peherstorfer; Nakamura; Kac–van Moerbeke; Moser; Flaschka.** Not re-searched individually. These are classical Toda/OP
  connections (finite or infinite lattices, long-time asymptotics). None located treats the n → ∞ expansion of a fixed measure.
- **Simon, arXiv:math/0610987** (title only, from search): long-time asymptotics of Schur/Toda-type flows. This is the t → ∞
  direction, not n → ∞.

### 1.2 What is (not) there
- **KNOWN:** Lemma T.1, and the use of Toda equations with re-expanded index shifts to generate the hierarchy of expansion coefficients
  (EMP, varying weights).
- **NOT FOUND:**
  - formal Toda identities for the layers of the expansion in n of a **fixed** measure;
  - the base times t_k = −2ζ(−kp)/k (band-factor constants) and the reading of a zeta layer as an n-independent Toda flow of the
    integer layers;
  - the Baire-category transfer that avoids differentiating expansions or needing uniformity in the tilt;
  - T_H and the rational continuation to the decoupled model.

### 1.3 Verdict T
- Lemma T.1: **KNOWN**.
- Theorem T (ii)–(iii), T_H: **PARTIALLY KNOWN (mechanism: EMP's continuum-Toda hierarchy for varying weights); NOT FOUND (fixed
  measure, zeta times, Baire transfer).**

## 2. Item Σ: reflection, shift, evenness

### 2.1 Prior work found
- **Kuijlaars & Tibboel, "The asymptotic behaviour of recurrence coefficients for orthogonal polynomials with varying exponential
  weights", arXiv:0708.3956** (submitted 2007-08-29; journal not verified, probably J. Comput. Appl. Math. 2010, **check**).
  (WebFetch, PDF):
  - Thm 1.1 (one-cut regular real-analytic V): a_{n,n} ~ (b−a)²/16 + Σ_m α_{2m}/n^{2m}, and b_{n,n} ~ (b+a)/2 + Σ_m β_m/n^m.
  - The odd powers vanish "from the structure of the local Airy parametrices".
  - Lemma 4.1: "For k odd, R_k(z) is a linear combination of σ₁ and σ₃". For even k, the span is that of I and σ₂.
  - Formulas (3.21)–(3.22): Δ_k for odd k are multiples of "(σ₃ + iσ₁)" and "(σ₃ − iσ₁)".
  - Bleher–Its is cited as using "so-called string equations"; Toda is not mentioned.
  - **This is the same ℤ₂-grading as Paper IV's proof of Theorem `thm:reflect`.** There, the core matrices lie in span{I, σ₂} for
    even k and span{σ₃, iσ₁} for odd k, and conjugation by σ₂ gives (−1)^k. The difference: K–T use the grading to kill the odd
    powers of a product (a_{n,n} = X² − p²). Paper IV uses it to get a covariance under (n, β) ↦ (−n, −β−2). **Cite K–T as the
    origin of the grading argument.**
- **Bleher & Its 2005, Thm 5.2 / Lemma 5.3** (recorded in NOVELTY_JZC §3.1; not re-read). This is evenness in N⁻² with β_n at
  (n+½)/N, proved through the string-equation reindexing σ₀: γ_j → γ_{2n−j}. Paper IV already cites it.
- **Filipuk, Van Assche & Zhang, "The recurrence coefficients of semi-classical Laguerre polynomials and the fourth Painlevé
  equation", arXiv:1105.5229** (J. Phys. A 45 (2012), **check**). (WebFetch, ar5iv):
  - Weight x^α e^{−x²+tx}.
  - Thm 2.1 (from earlier work): "2a_{n}^{2}=y_{n}+n+\alpha/2", and "x_{n}x_{n-1}=\frac{y_{n}+z_{n}}{y_{n}^{2}-\alpha^{2}/4}" with
    "z_{n}=n+\alpha/2".
  - PIV parameters (13): "A=1+2n+\alpha,\qquad B=-2\alpha^{2}".
  - This is an *exact* instance of the pairing (index + half the hard-edge exponent, exponent²). It is the semiclassical analogue
    of Paper IV's N = n + (β+1)/2 with ν² (at β = ν = α, 2N = 2n + α + 1 = A).
  - It is not a frame identity, and β and ν are not decoupled. Paper IV could mention it next to the Laguerre example
    b_n² = n(n+α).
- **Laguerre / Jacobi exact cases.** Textbook (recorded in NOVELTY_JZC). The Christoffel transform x·μ moves β and ν together
  (JZC_SIGMA Remark C). Nothing found moves the Szegő exponent with the Bessel order fixed.
- **Ercolani–Pierce 2011.** Odd weights: the diagonal has all powers and there is no n+½ shift.
- **Deaño–Huybrechs–Opsomer, arXiv:1612.07578 (Laguerre-type, hard edge).** (WebFetch, PDF): explicit expansions of recurrence
  coefficients. They found no evenness or shifted-index statement: "The text does not discuss whether odd powers vanish, and it does
  not use a shifted index such as n+α/2"; "Unlike in the Jacobi case, the expressions for the left and right disks are not
  symmetric." So in the hard-edge RH literature, the natural index is not noticed even for Laguerre-type weights. (Laguerre-type
  weights there are varying/MRS-rescaled; the setting differs.)
- **Kriecherbauer–McLaughlin, IMRN 1999 (Freud weights).** Bibliographic data only (experts.arizona.edu); abstract not available.
  It is unknown whether their recurrence-coefficient expansion is stated in n^{−2}. **Unread.**
- **Search for the mechanism.** A non-integer steepest-descent frame, the gauge z^{γσ₃}, and the Szegő exponent shifted by −2γ:
  one extended query; nothing relevant.

### 2.2 Verdict Σ
- Theorem `thm:reflect`: **PARTIALLY KNOWN**. The grading argument is Kuijlaars–Tibboel's Lemma 4.1. The reflection (n, β) ↦
  (−n, −β−2) on the decoupled model: NOT FOUND.
- Theorem `thm:shift` (FI, β-independence of F_p in N), the m-frame proof, Cor `cor:even` for a fixed measure: **NOT FOUND**.
- The phenomenon "even in a half-shifted index": **PARTIALLY KNOWN** (Bleher–Its; EMP; KT; exact Laguerre/semiclassical-Laguerre
  pairing n + α/2 with α²).

## 3. Item SH: the index-shift law as dispersionless Toda on the hard edge

### 3.1 Prior work found
- **Ercolani, "Caustics, counting maps and semi-classical asymptotics", arXiv:0912.1904 (Nonlinearity 24 (2011), check).**
  (WebFetch, PDF and ar5iv):
  - The equations are "founded on a continuum limit of the well-known system of differential equations (the Toda Lattice equations)".
  - The leading order is "an instance of the inviscid Burgers equation, well-known from the theory of shock waves". It has a power
    nonlinearity, f_s = c_ν f^ν f_w, with initial data f(0, w) = w (§2.3).
  - "The solution is given implicitly by" 1 = z_0(s) − c_νs z_0(s)^ν (eq. 30). Also: "From the method of characteristics one may
    conclude that" z_0(−t) continues to a slit plane.
  - §2.4 "The Burgers Caustic": the shock time s_c = (ν−1)^{ν−1}/(c_νν^ν).
  - The abstract: z_0 "is itself the generating function for the Catalan numbers (or generalized Catalan numbers...)".
  - **This is the closest prior work for SH, as the task anticipated.** In Ercolani, genus-zero Toda for one time is a Hopf/Burgers
    equation with power-law speed, solved by characteristics into an implicit algebraic equation whose Taylor coefficients count
    maps. Thm SH is the same mechanism with these differences:
    - the initial profile b(n, 0) = cn^{−p}, a fixed measure accumulating at a hard edge, instead of b² = n/N (Gaussian);
    - the invariant line a = 2b (hard edge), instead of a = 0 (even weight);
    - several times;
    - fractional and pole exponents;
    - the explicit Lagrange–Bürmann closed form.
- **EMP 2008.** As in §1.1. Genus zero: eq. (2.6) "1 = z0(s) − cν s z0(s)^ν". Coefficient extraction by contour integral (§3.5).
- **Bouttier, "Enumeration of maps", arXiv:1104.3003** (chapter in the Oxford Handbook of RMT). (WebFetch):
  - (26.4.15) "R = t + 3tR^2", with "R is the generating function for planar maps with two distinguished vertices of degree 1"
    (quartic).
  - Lagrange inversion is used for trivalent maps (26.4.20) and for Eulerian maps: "This paves the way to an application of the
    Lagrange inversion formula" (26.4.22).
  - Lagrange inversion of the genus-zero string equation is therefore textbook in map enumeration (BIPZ 1978, BIZ 1980, Tutte;
    not read here).
- **Bleher, Fields minicourse notes** (gfs.fields.utoronto.ca, bleher1.pdf). (WebFetch): the quartic string equation, and the
  fixed-point solution γ_n² = R(n/N), R(λ) = (−t + √(t² + 12gλ))/(6g). The algebraic form R(t + 3gR) = λ is WebFetch's
  rearrangement.
- **Konopelchenko, Martínez Alonso & Medina, "On the singular sector of the Hermitian random matrix model in the large N limit",
  arXiv:1005.4773.** (WebFetch):
  - The endpoints "evolve with the temperature T and the coupling constants tk according to the dispersionless Toda (dToda)
    hierarchy".
  - u = ½(β₁ + β₂), v = (1/16)(β₁ − β₂)² (eq. 20). So the endpoints u ± 2√v are the Riemann invariants (WebFetch's inference; the
    paper does not say "Riemann invariant").
  - "hodograph equations exhibit gradient catastrophe".
  - For Paper IV's Lemma R this means: the hard edge a − 2b = 0 is the statement that the left endpoint (a Riemann invariant) stays
    at 0. That is a specialisation of a known structure.
- **Martínez Alonso & Medina, arXiv:nlin/0409002**: hodograph solutions of dToda constrained by string equations (2D gravity,
  Laplacian growth). No OPs. **Mañas, arXiv:nlin/0404022**: r-th dToda; cites Tsarev's generalised hodograph. **Takasaki–Takebe,
  arXiv:hep-th/9405096**: dispersionless KP/Toda, twistor construction. **Kodama–Pierce, arXiv:0811.0351 (CMP 2009)**: dToda ↔
  free energy of unitary ensembles. "the leading orders of the free energy for large matrices agree"; counts of ribbon graphs; no
  hodograph, Riemann invariants or hard edge in the excerpt. **Álvarez–Martínez Alonso–Medina, arXiv:1101.2727 (Nucl. Phys. B)**:
  genus expansions of recurrence coefficients via the Toda resolvent; coefficients rational in r₀. **Benassi–Moro,
  arXiv:1903.11473**: dispersive regularisation, Volterra reduction. All are background; none has a hard edge or a fixed measure.
- **Hard-edge / Laguerre dispersionless Toda.** Three searches (one extended) found no source treating the a = 2b line as a
  reduction of dToda for Laguerre-type or hard-edge OPs. Hard-edge tilts appear in Painlevé settings: Chen–Its arXiv:0808.3590, weight
  x^αe^{−x}e^{−s/x}, "an integral of the combination of a particular third Painlevé function"; Filipuk–Van Assche–Zhang (PIV).
  These are double-scaling or exact results, not genus-zero hodograph solutions.

### 3.2 What is (not) there
- **KNOWN (mechanism):**
  - genus zero of the continuum Toda hierarchy = Hopf/Burgers equations, solved by characteristics or hodograph;
  - the implicit equation x = n + Σt_jV_j(b) (EMP/Ercolani, one time; Ercolani–Waters, string equations for general V_t);
  - Lagrange inversion of that equation (map enumeration);
  - endpoints = Riemann invariants (dToda);
  - higher orders = forced linear equations from the k^{−2g} terms (EMP). That is the analogue of "dressings = dispersive part".
- **Elementary:** Lemma LB, the Lagrange–Bürmann coefficients of (1+y)^{−p} for y = λψ(y) with ψ a sum of powers. This is the
  generalised binomial series.
- **NOT FOUND:**
  - b(n, 0) = cn^{−p} as initial data. This is a Hopf problem for a fixed measure, in n alone, with no N.
  - The hard-edge invariant line a = 2b used as the reduction.
  - Continuation to fractional and pole exponents by rationality.
  - Zeta-valued times and the band-factor parameters ε̂_a.
  - The explicit multi-time rising-factorial formula as a statement about recurrence coefficients.
  - The rigid case: the Szegő "time" log x has speed V = ½, so the shift n ↦ n − γ is rigid and matches Theorem Σ.
  - The specific dressing results (g_j split, h₂, h(j, k)).

### 3.3 Verdict SH
- **Mechanism: KNOWN** (Ercolani 2011; EMP 2008; map-enumeration string equations + Lagrange inversion).
- **Thm SH as a statement about the fixed lattice and hard-edge measures, including fractional/pole exponents: NOT FOUND.**
- **Novelty label: POSSIBLY-NEW for the setting only.** It must not be presented as a new mechanism.

## 4. Unread decisive items
1. **Ercolani 2011 full text**, §§2–4. Check whether initial data other than f(0, w) = w, or a hard edge or Laguerre case, are treated.
   Check also whether a multi-time hodograph formula with Lagrange inversion is given (§4.1 "uses the implicit relation to change
   variables in coefficient extraction").
2. **Ercolani–Waters 2019/2020** (arXiv:1907.08026, all versions): the "universal symbol calculus … Bessel–Appell polynomials"
   version. Check for multi-time genus-zero closed forms and for any Laguerre or hard-edge analogue.
3. **Kuijlaars–Tibboel**: the journal version and the exact text of Lemma 4.1. Paper IV's `thm:reflect` should cite it.
4. **Deift–McLaughlin, Mem. AMS 624 (1998)**, the continuum limit of Toda (Lax–Levermore, shocks). Riemann invariants a ± 2b for slowly
   varying initial data: not confirmed from the description.
5. **Kriecherbauer–McLaughlin, IMRN 1999 (Freud)** and **DKMVZ, CPAM 1999** (Thm 2.20-type expansions of a_n, b_n): check for
   evenness or a shifted index in a fixed (non-varying) Freud weight. Fixed Freud weights are the closest *fixed-measure* setting where
   an evenness statement could already exist.
6. **Laguerre-ensemble map enumeration** (bipartite maps, hypermaps, Ambjørn–Chekhov dessins, Kazarian–Zograf). These are the hard-edge
   genus-zero counterpart of the Gaussian theory and could contain the a = 2b reduction. Not searched by name.
7. **Dubrovin** (Hamiltonian PDEs, universality; Toda as the example) and **Bonora–Xiong** (dToda for matrix models): not read.
8. **Moser 1975, Flaschka 1974, Kac–van Moerbeke, Nakamura, Peherstorfer**: classical Toda/OP references for Lemma T.1, by title only.

## 5. Recommended labels and attribution wording (Paper IV, secS.tex)

**Labels (novelty field, VERIFICATION_POLICY):**
- Lemma `lem:todatilt`: KNOWN.
- Theorem `thm:toda` (ii)–(iii): POSSIBLY-NEW for the setting (fixed measure, zeta base times, Baire transfer); mechanism KNOWN
  (EMP).
- Theorem `thm:reflect`: KNOWN mechanism (Kuijlaars–Tibboel grading); the (n, β) reflection on M(β, ν) is POSSIBLY-NEW (minor).
- Theorem `thm:shift`, Cor `cor:even`: POSSIBLY-NEW (statement and proof); phenomenon PARTIALLY KNOWN.
- Theorem `thm:indexshift`: POSSIBLY-NEW for the setting only; mechanism KNOWN (Ercolani 2011, EMP 2008).
- Keep each at POSSIBLY-NEW, not NEW, until the unread items of §4 (1, 2, 5, 6) are checked.

**Suggested wording (drafts; the citations must pass Rule C first):**

1. After Lemma `lem:todatilt`:
   > The Toda hierarchy for exponential tilts is classical (Moser, Flaschka; see the survey of Van Assche [arXiv:2202.11017,
   > Lemma 2.1, Theorem 2.4]); we include the short proof for the identities in the form used below.

2. Before Theorem `thm:toda`:
   > Using the Toda equations, with shifted indices re-expanded in $1/n$, to generate the coefficients of an asymptotic expansion is
   > the method of Ercolani, McLaughlin and Pierce [CMP 2008, §4] for varying weights $e^{-N(x^2/2+tx^{2\nu})}$. Here there is no
   > large parameter other than $n$, the measure is fixed, the times enter as $u_jn^{-jp}$ with base values
   > $t_k=-2\zeta(-kp)/k$, and the identities are transferred from the exact flows by a category argument rather than derived from a
   > string equation.

3. In the proof of Theorem `thm:reflect`:
   > The grading of the jump corrections into $\mathrm{span}\{I,\sigma_2\}$ and $\mathrm{span}\{\sigma_3,i\sigma_1\}$ is the device
   > that Kuijlaars and Tibboel [arXiv:0708.3956, Lemma 4.1] use to show that the odd powers of the off-diagonal recurrence
   > coefficient vanish for one-cut varying weights; here it gives a covariance under $(n,\beta)\mapsto(-n,-\beta-2)$.

4. After Corollary `cor:even`, extending the existing Bleher–Its remark:
   > Evenness in a half-shifted index is known for varying weights with a string equation [Bleher–Its, Thm 5.2; EMP Thm 2.2;
   > Kuijlaars–Tibboel Thm 1.1]. In the semiclassical Laguerre case the index and the hard-edge exponent enter the discrete
   > Painlevé system through $n+\alpha/2$ and $\alpha^2$ [Filipuk–Van Assche–Zhang, Thm 2.1, eq. (13)]. What is new here is the
   > decoupling of the Szegő exponent from the Bessel order and the frame identity~\eqref{eq:FI} for a fixed discrete measure.

5. In §`sec:indexshift`, before or after the outline proof:
   > At leading order the mechanism is the genus-zero one of random-matrix map enumeration: the continuum limit of the Toda
   > equations is an inviscid Burgers (Hopf) equation with power-law speed, solved implicitly by characteristics, and the
   > coefficients of the implicit solution are obtained by Lagrange inversion (Ercolani [Nonlinearity 2011, §2.3, eq. (30)];
   > Ercolani–McLaughlin–Pierce [eq. (2.6)]; for the string equations of general potentials Ercolani–Waters; for Lagrange
   > inversion in map counting, e.g. Bouttier [§26.4]). The endpoints of the support are Riemann invariants of the dispersionless
   > Toda hierarchy (cf. Konopelchenko–Martínez Alonso–Medina). The hard edge fixes one of them at $0$, which is Lemma R. What
   > differs here is the initial profile $b=cn^{-p}$ of a fixed measure accumulating at a hard edge (instead of the Gaussian
   > $b^2=n/N$), the reduction to the line $a=2b$, arbitrary real and pole exponents, and zeta-valued times.

   Also change the sentence "Theorem `thm:toda` determines the leading term of every layer in closed form" so that it does not
   suggest the closed-form mechanism is new: e.g. "…in closed form, by the genus-zero mechanism of [Ercolani 2011]".

6. Remark `rem:parity`: the "1/(2j−1)" heuristic via (1/2π)∫(a + 2b cos θ)^j dθ is the standard symbol of a constant Jacobi
   matrix. No attribution is needed beyond "the dispersionless symbol".

**Do not claim:** that the dispersionless/Hopf/characteristics reading or the Lagrange-inversion form is new, or that evenness after
an index shift is new as a phenomenon.

## 6. Queries (all WebSearch standard unless marked)
1. Ercolani "Caustics, counting maps and semi-classical asymptotics" Toda Burgers characteristics
2. Ercolani McLaughlin "Asymptotics of the partition function for random matrices via Riemann-Hilbert techniques" graphical
   enumeration z_0 Lagrange inversion
3. Ercolani Pierce "continuum limit of Toda lattices for random matrices with odd weights"
4. dispersionless Toda hierarchy orthogonal polynomials recurrence coefficients genus zero hodograph solution string equation
5. Dubrovin Elaeva / Dubrovin "Hermitian matrix model free energy" Toda hierarchy dispersionless Riemann invariants recurrence
   coefficients hodograph
6. Bessis Itzykson Zuber 1980 quantum field theory techniques in graphical enumeration recurrence coefficients R_n planar limit implicit
   equation r = x + g r^2
7. planar limit recursion coefficients orthogonal polynomials "string equation" genus zero "x = W'(r)" OR "x = r + 12 g r^2" Bessis
   Itzykson Zuber quartic
8. Benassi Moro thermodynamic limit dispersive regularisation matrix models Toda lattice Riemann invariants hodograph recurrence
   coefficients
9. Laguerre ensemble Wishart Toda lattice continuum limit hard edge Riemann invariant recurrence coefficients hodograph solution
   dispersionless
10. Deift McLaughlin "A continuum limit of the Toda lattice" Memoirs AMS 1998 Riemann invariants hyperbolic system a ± 2b
11. Deift Kriecherbauer McLaughlin Venakides Zhou strong asymptotics orthogonal polynomials exponential weights recurrence coefficients
    asymptotic expansion powers of 1/n Freud weight even powers
12. Freud weight |x|^beta exp(-|x|^m) recurrence coefficients asymptotic expansion only even powers n^{-2} Máté Nevai Totik half-integer
    shift
13. Kuijlaars Tibboel "The asymptotic behaviour of recurrence coefficients for orthogonal polynomials with varying exponential weights"
    journal
14. recurrence coefficients asymptotic expansion Laguerre-type weight hard edge Bessel parametrix odd powers vanish shifted index
    Riemann-Hilbert full expansion
15. Kodama Pierce "Combinatorics of dispersionless integrable systems and universality in random matrix theory"
16. Filipuk Van Assche Zhang recurrence coefficients semi-classical Laguerre polynomials fourth Painlevé equation parameters depend on n
    and alpha
17. Laguerre unitary ensemble perturbed potential genus expansion recurrence coefficients Toda lattice continuum limit bipartite maps
    generating function implicit equation
18. Ercolani "Lagrange inversion" Toda continuum limit random matrices maps "Hopf" OR "Burgers" characteristics generating function
    recurrence coefficients
19. Wishart Laguerre ensemble Volterra lattice dispersionless limit hard edge Riemann invariant zero hodograph matrix model
20. Toda flow exponential tilt asymptotic expansion recurrence coefficients large n fixed measure derivative with respect to tilt
    parameter Jacobi matrix asymptotics
21. Chen Its "Painlevé III and a singular linear statistics in Hermitian random matrix ensembles" recurrence coefficients
    x^alpha e^{-x-t/x}
22. (extended) "dispersionless Toda" "orthogonal polynomials" "Laguerre" OR "hard edge" genus zero recurrence coefficients
    characteristics a = 2b
23. quartic matrix model planar limit R = 1 + 12 g R^2 Lagrange inversion number of planar quadrangulations Tutte formula recursion
    coefficient
24. Takasaki Takebe "Integrable hierarchies and dispersionless limit" Toda hierarchy hodograph orthogonal polynomials
25. (extended) Riemann-Hilbert steepest descent non-integer index shifted degree n+gamma gauge z^{gamma sigma_3} exponent of weight at
    hard edge alpha - 2 gamma recurrence coefficients expansion natural variable n + (alpha+1)/2
26. Kriecherbauer McLaughlin "Strong asymptotics of polynomials orthogonal with respect to Freud weights" recurrence coefficients
    asymptotic expansion n^{-2}
27. Bloch Golse Paul Uribe "Dispersionless Toda and Toeplitz operators" Duke

**WebFetch (pages read):**
- arXiv:0912.1904 (ar5iv and PDF);
- math-ph/0606010 (abstract and PDF);
- 1106.1143 (PDF);
- nlin/0409002 (ar5iv);
- 1005.4773 (PDF);
- nlin/0404022 (PDF);
- 1903.11473 (abstract);
- Deift–McLaughlin Memoir (experts.arizona.edu, AMS bookstore);
- 1101.2727 (ar5iv);
- Bleher Fields notes (PDF);
- AMS Math. Comp. 73 (2004) S0025-5718-03-01553-9 (abstract; Freud-equation main term, weight |x|^ρ e^{−Q});
- 0708.3956 (PDF, twice; abstract page);
- 1612.07578 (PDF);
- 0811.0351 (ar5iv and PDF);
- 2202.11017 (abstract);
- 1105.5229 (ar5iv, twice);
- 1907.08026 (PDF);
- 0808.3590 (abstract);
- math-ph/0211022 (PDF);
- 1104.3003 (PDF);
- hep-th/9405096 (abstract);
- Kriecherbauer–McLaughlin (experts.arizona.edu, bibliographic only).

**Refused:** arXiv hep-th/9306153 (Di Francesco–Ginsparg–Zinn-Justin review; not on the allowlist).
