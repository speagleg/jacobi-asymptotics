# NOVELTY_JZC: Rule L search for the Jacobi–zeta correspondence (Theorem K/K0, Theorem Q, natural index N, X_j structure)

> **Update (Rule L, 2026-10-23).** Three follow-up searches extend this file; their queries are listed in each (Rule L log):
> - **NOVELTY_Q.md** (item Q; supersedes §2 below): Theorem Q **PARTIALLY KNOWN** — endpoint equation and monotone criterion in
>   Beckermann–Kuijlaars, SINUM 39 (2001) Lemma 3.1(a) (unread; via Beckermann–Helart arXiv:1707.07871 Lemma 1.5), density = the
>   constrained Buyarov–Rakhmanov superposition (BK 2001 Thm 2.1); new = infinite mass / Y = ∞, closed form (G), edge constant.
>   Cor Q.1: no claim. Prop M1.2: POSSIBLY-NEW. Queries: NOVELTY_Q §5.
> - **Correction to §2.1 below:** Beckermann–Kuijlaars ETNA 2002 eq. (2.25) / Thms 2.7–2.8 are the *external-field* case (they cite
>   Kuijlaars–McLaughlin and Kuijlaars 2000, not BK 2001); they are not the nearest analogue of (Q). The Q ≡ 0 analogue is BH Lemma
>   1.5 / BK01 Lemma 3.1(a) (NOVELTY_Q §2.4).
> - **NOVELTY_TODA.md** (Theorem T, Theorem Σ, index-shift law): Lemma T.1 KNOWN (Van Assche arXiv:2202.11017); Theorem T (ii)–(iii),
>   Σ, Thm SH POSSIBLY-NEW for the setting only, mechanisms KNOWN (Ercolani arXiv:0912.1904; EMP math-ph/0606010; Kuijlaars–Tibboel
>   arXiv:0708.3956; Filipuk–Van Assche–Zhang arXiv:1105.5229). Queries: NOVELTY_TODA §6.
> - **NOVELTY_ZETA.md** (items K/N.6, H, W, large order): NOT FOUND → POSSIBLY-NEW; closest relatives Tricomi–Carlitz (arXiv:1410.3948),
>   Neumann–Bessel (arXiv:2406.09746), Murugan–Van Zyl–Watanabe (arXiv:2608.07258), Magnus / Foulquié Moreno et al. (arXiv:0905.2753);
>   large order: phenomenon PARTIALLY KNOWN (Mariño–Schiappa–Weiss, Costin–Garoufalidis), stays UNCHECKED. Queries: NOVELTY_ZETA §7.

Date: 2026-10-21. Branch plan-e2-d2. Searcher: a subagent of the JZC session. Rule L only: this file records what the search
found. It does not review the mathematics (Rule R) or the citations (Rule C). Structure follows research/program/novelty_SPEC.md.

- **Network.** The shell cannot reach arxiv.org (proxy 403). Every quote below came through WebFetch, which summarises the page
  with a small model and caps quotes at about 125 characters. All quotes marked "(WebFetch)" are therefore second-hand. Under
  Rule C, each must be re-read in the source before it is cited. Equation and theorem numbers are as WebFetch relayed them.
- **Verdict scale.** KNOWN: found essentially as stated. PARTIALLY KNOWN: the named part or the phenomenon was found in another
  setting. NOT FOUND: not located by the queries listed. NOT FOUND describes this search; it is not evidence of novelty.
  MathSciNet and zbMATH were unavailable.
- **Items.** K = SPEC §3.14 Theorem K / Lemma K0, JZC_M2 Theorem K′, and §3.16 (drums). Q = JZC_M1 Theorem Q, Cor Q.1,
  Prop M1.2. N = JZC_M4 Identity N.1, Prop N.2–N.4, Conj S1-N, JZC_M4_proof Thm N.6. T = Conj S1-N′ and the 1/(2j−1) remark
  (JZC_M4 §6).

## 0. Summary

| Item | Verdict | Closest prior work |
|---|---|---|
| K. Mellin–Barnes form of the b_n correction: kernel π[cot(πwp/2) − cot(πw)]·W(w) against Z(−wp); pole terms pRW(q)π cot(πq)n^{−1−pq}; drums (perimeter at n^{−1/2}, corners via Z(0)) | **NOT FOUND**, both the correspondence and the drum reading. Ingredients are KNOWN: the Beta/Mellin identity of K0 is elementary, and the Voros-type link between zeta values and large-λ expansions (novelty_SPEC §6). The closest structural analogue is OP asymptotics at fixed x written through the regularised characteristic function of J (Šťovíček–Świderski 2024). This concerns polynomials, not recurrence coefficients. | Šťovíček–Świderski, arXiv:2409.19644; Monien 2010; Voros 1987/1999 (from novelty_SPEC) |
| Q. Explicit constrained equilibrium (upper constraint σ, no external field), yσ decreasing, soft-edge condition (Q) | **PARTIALLY KNOWN.** Existence, uniqueness, characterisation, saturation and balayage are KNOWN (Dragnev–Saff 1997; Rakhmanov 1996; Kuijlaars–Van Assche 1999 on [0, ∞)). Beckermann–Kuijlaars 2002 eq. (2.25) has the same Cauchy-integral form as (Q), with Q ≠ 0, compact support and two soft edges. **Not read and decisive:** Beckermann–Kuijlaars, SINUM 2001, Thm 2.1, a "similar formula" for the **no-field** case (relayed by Beckermann–Güttel). The general formula (G), the criterion "yσ decreasing", and non-compact constraints of infinite mass with a hard edge at 0: NOT FOUND. | Beckermann–Kuijlaars ETNA 14 (2002) Thms 2.7–2.8; BK SINUM 39 (2001) Thm 2.1 (unread); Dragnev–Saff, J. Anal. Math. 72 (1997); Van Assche–Van Baelen, Constr. Approx. (2020), arXiv:1910.12518 |
| N. Natural index N = n + α/2 − Z(0); integer layer even in 1/N (f₁ = f₃ = … = 0), f₂, f₄, f₆ closed forms; even dressing g_j of ε_jN^{−1−jp} | **PARTIALLY KNOWN (the phenomenon, in other settings).** Evenness in N⁻² after a half-index shift is a theorem for varying weights e^{−NV}: Bleher–Its 2005 Thm 5.2 (diagonal coefficient at (n + ½)/N; odd terms killed by a reindexing symmetry of the string equations). Ercolani–McLaughlin–Pierce: b_k² ≃ k Σ z_g/k^{2g} for even weights. Exact cases: Laguerre b_n² = n(n + α); Jacobi. KMVV 2004 Thm 1.10: A₁ = B₁ = 0, A₂ quadratic in α, β. **NOT FOUND:** a natural index involving a spectral zeta value Z(0), evenness for a fixed (non-varying) discrete measure with no string equation, f₄/f₆/g_j, and the hard-edge denominators Π((2k+1)p + 2). | Bleher–Its, Ann. Inst. Fourier 55 (2005) 1943, Thm 5.2; Bleher–Deaño, arXiv:1011.6338, Thm 4.1; Ercolani–McLaughlin–Pierce, arXiv:math-ph/0606010, Thm 2.2; KMVV, arXiv:math/0111252, Thm 1.10 |
| T. F = Σ_β c_β(N⁻²)ΠX_j^{β_j}, X_j = ε_jN^{−1−jp} (trans-series-like); X₁² coefficient (3p+1)/(2p); 1/(2j−1) in g_j as the Mellin signature of (1 − u)^{1/2} | **NOT FOUND.** Nearest structure: the genus expansions above (coefficients z_g(s) as functions of a scaling variable, not of non-integer monomials). No expansion of recurrence coefficients in monomials n^{−1−jp} with zeta coefficients was located. | (as N) |

## 1. Item K: zeta function ↔ recurrence-coefficient asymptotics; drums

### 1.1 Prior work found
- **Šťovíček & Świderski, "On positive Jacobi matrices with compact inverses", arXiv:2409.19644 (2024; journal not checked)**
  (WebFetch, abstract): "if the inverse of $J$ belongs to some Schatten class, we identify the asymptotic behaviour" "of the
  sequence of orthogonal polynomials and express it in terms of its regularized characteristic function." Also "a formula for
  the trace of the inverse of $J$".
  - This is the closest structural relative found. The orthogonality measure lives on the reciprocal spectrum, and asymptotics
    are expressed through a regularised determinant, as in SPEC Heuristic S3.
  - It differs from K. It gives polynomial asymptotics at fixed x, not recurrence-coefficient asymptotics in n; it has no
    Mellin–Barnes kernel and no zeta values at negative arguments (from the abstract only).
  - It should be read in full before SPEC §3.7/S3 is called NOT FOUND.
- **Maltsev & Simm, "Moments at the hard edge and Rayleigh functions", arXiv:2604.18113 (2026)** (WebFetch): the work is
  "motivated by the analogy between spectral moments of random matrices and associated zeta functions", and in a low-temperature
  limit "the moments are given in terms of the Bessel zeta function." Context only: these are Laguerre-ensemble trace moments,
  with no recurrence coefficients.
- **Already recorded in novelty_SPEC §§1, 6.** Monien 2010 (Gauss quadrature for sums, σ_{2,2}, no asymptotics); Van Assche 1996
  §3 and Dickinson 1954 (Lommel); Voros 1987/1999 and Fucci–Piorkowski–Stanfill 2025 Thm 3.7 (zeta values ↔ large-λ expansion of
  log D). Nothing new on these was found.
- **Rayleigh functions** σ_n(ν) = Σ_k j_{ν,k}^{−2n} are the moments of the Lommel measure. The classical literature (e.g.
  arXiv:1305.0228, title only) computes them at positive n. No source located reads Lommel recurrence coefficients as zeta
  values at negative arguments.

### 1.2 What is not there
- No source gives n^pb_n (or any Jacobi parameter) as a Mellin–Barnes integral against a spectral zeta function.
- No source has cot-kernel pole terms R·W(q)π cot(πq)n^{−1−pq} from non-integer poles of Z.
- No source reads the perimeter (n^{−1/2} via the 0·∞ limit of W·cot) or the corner/curvature term Z(0) of a drum from Jacobi
  coefficients. Searches for "hear the shape of a drum" combined with Jacobi or Lanczos returned only Laplacian spectral-geometry
  papers.
- Lemma K0 itself (B(−w, ½) = −π cot(πw)Γ(w + ½)/(√πΓ(w + 1))) is the Beta integral plus reflection: elementary, KNOWN in
  substance.

### 1.3 Verdict K
- **The correspondence (Theorem K/K′, pole law as derived in §3.14): NOT FOUND.**
- **The drum reading (§3.16): NOT FOUND.**
- **Lemma K0: elementary.**

**Queries** (standard unless noted):
- "spectral zeta function values recurrence coefficients asymptotics Jacobi matrix orthogonal polynomials Mellin-Barnes"
- "Lanczos coefficients asymptotics determined by heat kernel coefficients spectral zeta function inverse spectral"
- "\"hear the shape of a drum\" Jacobi matrix recurrence coefficients Lanczos Laplacian eigenvalues perimeter"
- "orthogonal polynomials moments are zeta values Hankel determinant Σ λ_k^{-s} asymptotics recurrence coefficients Weyl law
  eigenvalues reciprocal" (extended)
- "Krylov complexity Lanczos coefficients asymptotics discrete spectrum zeta function regularized correction terms subleading"
- "Rayleigh function sums of inverse powers of Bessel zeros moments Lommel polynomials orthogonality measure continued fraction zeta"
- "Mellin-Barnes integral asymptotic expansion recurrence coefficients orthogonal polynomials discrete measure cot(pi s) kernel
  poles zeta function"
- "Jacobi matrix entries asymptotics determine spectral invariants heat trace coefficients regularized trace formula compact
  Jacobi operator eigenvalues power decay"
- "discrete orthogonal polynomials nodes accumulate at zero recurrence coefficients asymptotic expansion Riemann-Hilbert
  interpolation problem Hurwitz zeta Bernoulli"

## 2. Item Q: explicit constrained equilibrium with no external field

### 2.1 Prior work found
- **Dragnev & Saff, "Constrained energy problems with applications to orthogonal polynomials of a discrete variable", J. Anal.
  Math. 72 (1997) 223–259** (WebFetch, abstract): "we prove existence and uniqueness of a measure"; the abstract also lists a
  characterisation theorem, a saturation result and a balayage representation, with explicit results for Krawtchouk. WebFetch
  found no general explicit formula in the abstract. Full text not read.
- **Rakhmanov, "Equilibrium measure and the distribution of zeros of the extremal polynomials of a discrete variable", Sb. Math.
  187:8 (1996) 1213–1228** (WebFetch, abstract): "the degree $n$ of this polynomial and the number $N$ ($N>n$) of points of
  growth" "approach infinity so that $n/N\to c\in (0,1)$." The uniform-lattice constraint is compact, of finite mass. Full text not read.
- **Beckermann & Kuijlaars, "Superlinear CG convergence for special right-hand sides", ETNA 14 (2002) 1–19** (WebFetch; already
  cited in JZC_M1 §6):
  - The problem is to minimise the energy with external field Q "among all Borel measures on [0, R] that satisfy" 0 ≤ ν ≤ σ,
    ∫dν = t.
  - Thm 2.7, the ansatz criterion: "Let supp(σ) = [A, B]"; "the functions x ↦ (x − A)Q′(x) and x ↦ (B − x)Q̃′(x) are increasing
    functions on [A, B]."
  - Thm 2.8, endpoint equations (2.24)–(2.25), as transcribed by WebFetch:
    t = (1/π)∫_α^β λQ′(λ)dλ/√((β−λ)(λ−α)) − ∫_A^α λ dσ(λ)/√((β−λ)(α−λ)).
  - WebFetch: "The paper does not give a Cauchy-type integral or closed form for the density"; σ is a probability measure with
    compact support.
  - **Relation to (Q).** Mirror the saturated region to the right, put a hard edge at α = 0 and set Q = 0. The second equation
    then has the shape t = ∫_a λ dσ/√(λ(λ − a)), i.e. ∫σ(y)(1 − a/y)^{−1/2}dy = t. This is (Q) with t = 1. This is my reading of a
    second-hand transcription, not a statement of BK.
- **Beckermann & Güttel, "Superlinear convergence of the rational Arnoldi method …", Numer. Math. (preprint)** (WebFetch):
  "For constrained problems without external fields (or νt = 0), a similar formula was established in [7, Theorem 2.1]",
  where [7] = Beckermann–Kuijlaars, "Superlinear convergence of conjugate gradients", SIAM J. Numer. Anal. 39 (2001).
  **This is the most likely place for an explicit no-field formula. It was not read.** Theorem Q's POSSIBLY-NEW status depends
  on it.
- **Kuijlaars, "Which eigenvalues are found by the Lanczos method?", SIMAX 22 (2000) 306–321.** Title and DOI only. The CWI
  report fetched (MAS-R9934) turned out to be a different paper on probabilistic Lanczos bounds, with no equilibrium problem.
- **Kuijlaars & Van Assche, "Extremal polynomials on discrete sets", Proc. LMS 79 (1999) 191–221.** Not opened. Van Assche–Van
  Baelen state that its Theorem 2.1 (constrained problem with external field) is "stated for $[0,\infty)$" (WebFetch). So
  non-compact constraints are in the classical framework.
- **Van Assche & Van Baelen, "Zero distribution of orthogonal polynomials on a q-lattice", arXiv:1910.12518, doi
  10.1007/s00365-020-09513-2** (WebFetch). The constraint is σ′(t) = −1/(t log q) on (0, 1], with infinite mass at 0 and no
  external field, and "ν^σ coincides with the constraint σ on the interval [q,1] and has no mass on [0,q]." There is no band.
  - My observation, not theirs: here tσ(t) is **constant**, the boundary case of Theorem Q's (H2). A band [0, a] needs tσ(t)
    strictly decreasing; this example is consistent with that, and Theorem Q could cite it as the degenerate case.
- **Background, not explicit for this problem:** BKMM 2007 (arXiv:math/0310278); Liechty, IMRN DOP (title).

### 2.2 Verdict Q
- **PARTIALLY KNOWN.** The constrained framework, unbounded constraints, and the Cauchy-integral form of endpoint equations are
  KNOWN.
- **NOT FOUND** in what was read:
  - the explicit factorised formula (G) for a general σ with yσ decreasing;
  - the hard edge at 0 with an infinite-mass constraint and no void;
  - the identification a = 4c(p) (Law P's constant without RH).
- **Required before keeping POSSIBLY-NEW:** read BK 2001 Thm 2.1 and Kuijlaars 2000 (both Q = 0) in full.

**Queries:**
- "constrained equilibrium problem upper constraint no external field explicit solution discrete orthogonal polynomials
  Rakhmanov Dragnev Saff"
- "Kuijlaars \"Which eigenvalues are found by the Lanczos method\" constrained equilibrium explicit formula"
- "Dragnev Saff \"Constrained energy problems with applications to orthogonal polynomials of a discrete variable\" explicit
  solution"
- "Kuijlaars Van Assche asymptotic zero distribution orthogonal polynomials varying recurrence coefficients constrained equilibrium"
- "Rakhmanov 1996 equilibrium measure zeros extremal polynomials discrete variable constraint explicit formula Sbornik"
- "Kuijlaars Van Assche \"Extremal polynomials on discrete sets\" Proc. London Math. Soc. 1999 constrained equilibrium unbounded"
- "Beckermann Kuijlaars superlinear convergence conjugate gradients constrained equilibrium explicit formula eigenvalue
  distribution ETNA 2002"
- "Beckermann Kuijlaars \"Superlinear convergence of conjugate gradients\" SIAM J. Numer. Anal. 2001 constrained equilibrium
  measure explicit ansatz Q=0"
- "Kuijlaars \"Convergence analysis of Krylov subspace iterations with methods from potential theory\" SIAM Review constrained
  equilibrium example explicit"

## 3. Item N: the natural index and evenness in 1/N

### 3.1 Prior work found
- **Bleher & Its, "Asymptotics of the partition function of a random matrix model", Ann. Inst. Fourier 55 (2005) 1943–2000;
  arXiv:math-ph/0409082** (WebFetch, from the AIF PDF):
  - Thm 5.2 (one-cut regular V, weight e^{−NV}): the recurrence coefficients admit a uniform asymptotic expansion "as N →∞ in
    powers of N −2".
  - Eq. (5.5), as reconstructed by WebFetch: γ_n ~ γ(n/N) + Σ_k N^{−2k}f_{2k}(n/N) and β_n ~ β((n + ½)/N) + Σ_k N^{−2k}g_{2k}((n + ½)/N).
  - Proof: "What we have to prove is that f_k = g_k = 0 for odd k. This will be done by using the string equations."
  - Mechanism (Lemma 5.3): invariance under σ₀: γ_j → γ_{2n−j}, β_j → β_{2n−j−1}, a reflection of the index about n (resp. n − ½).
  - **This is the closest precedent for N.** It shows evenness after a half-index shift, proved by an index-reflection symmetry.
- **Bleher & Deaño, "Topological expansion in the cubic random matrix model", arXiv:1011.6338 (IMRN 2013)** (WebFetch), Thm 4.1
  (cited from Bleher–Its): "the coefficients $\beta_n$, $\gamma_n^2$ can be expanded in uniform asymptotic series"; "in the
  expansion of $\gamma_n^2$ the odd coefficients vanish"; β_n is even "if we consider $\beta_n$ as a function of the shifted
  parameter" (n + ½)/N.
- **Ercolani, McLaughlin & Pierce, "Random matrices, graphical enumeration and the continuum limit of Toda lattices",
  arXiv:math-ph/0606010 (CMP 2008)** (WebFetch). Thm 2.2: "b_k^2 has a valid asymptotic expansion of the form b_k^2 ≃ k(z_0(s) +
  (1/k^2) z_1(s) + (1/k^4) z_2(s) + ···)", for even monomial perturbations. §4.1: "an asymptotic expansion in even inverse powers
  of (k + ℓ)".
  - **Ercolani–Pierce, arXiv:1106.1143 (odd weights).** b²_{n+k,N} is even in n⁻¹, but the diagonal a_{n+k,N} has all powers.
    "The paper does not evaluate the expansions at n+1/2" (WebFetch).
- **Kuijlaars, McLaughlin, Van Assche & Vanlessen, arXiv:math/0111252 (Adv. Math. 188 (2004))**, Thm 1.10 (WebFetch):
  - a_n ~ ½ + Σ_{k≥2}A_k/n^k and b_n ~ Σ_{k≥2}B_k/n^k, with A₂ = −(4α² − 1)/32 − (4β² − 1)/32 and B₂ = (β² − α²)/4;
  - Remark 1.11: "Note that $A_1 = B_1 = 0$";
  - the weight factor h enters first at n⁻³.
  - These are expansions in 1/n; no natural-index or evenness statement was seen. WebFetch did not reach §8 (higher terms).
- **Classical exact cases.** Laguerre b_n² = n(n + α), so b_n = N√(1 − α²/(4N²)) with N = n + α/2, even in N. Jacobi
  coefficients are rational in 2n + α + β + 1. JZC_M4 §2 already uses both; they are textbook (Szegő; DLMF 18.9), not re-read here.
  - Singularly perturbed Laguerre work (Chen–Its and successors) uses the variable s = (2n + 1 + α)t. This is from memory and
    was not verified (arXiv:2511.09362 returned an empty PDF to WebFetch).
- **Deaño–Huybrechs–Opsomer, arXiv:1612.07578 (Laguerre-type) and arXiv:1502.07191 (Jacobi-type).** Constructive full RH
  expansions of OPs and recurrence coefficients. Titles only; no natural-index statement checked.
- **Deift–Piorkowski, SIGMA 2024, arXiv:2307.09277** (log weight). Abstract only; irrelevant to evenness.

### 3.2 What is (not) there
- **Known.**
  - The phenomenon: for weights with a string equation (Freud/polynomial V, varying), evenness in N⁻² holds with the diagonal
    coefficient at a half-shifted index, proved by an index-reflection symmetry.
  - The hard-edge α/2 shift: Laguerre, exact.
- **Not found.**
  - **A natural index containing a spectral zeta value (−Z(0)).**
  - Evenness for a fixed, non-semiclassical discrete measure (no string equation, nodes accumulating at 0).
  - f₄, f₆, g_j = A_j + B_jα², the X₁² coefficient (3p+1)/(2p).
  - Denominators Π((2k+1)p + 2) from the hard-edge local map.
- **Suggestion.** JZC_M4 §5 says the reflection symmetry N → −N is "not yet identified". Bleher–Its Lemma 5.3 (the σ₀
  reindexing) is the template to compare against, even though this measure has no string equation.

### 3.3 Verdict N
- **Index-shift evenness as a phenomenon: PARTIALLY KNOWN (other settings).**
- **N = n + α/2 − Z(0), Prop N.3/N.4 closed forms, Thm N.6: NOT FOUND.**

**Queries:**
- "Ercolani McLaughlin Pierce random matrices graphical enumeration continuum limit Toda lattices recurrence coefficients expansion
  even powers 1/N string equations"
- "Laguerre recurrence coefficients n(n+alpha) reflection symmetry n -> -n-alpha asymptotic expansion even powers shifted index
  orthogonal polynomials"
- "Freud weight recurrence coefficients full asymptotic expansion even powers of 1/n Máté Nevai Totik string equation"
- "Bleher Deaño topological expansion cubic random matrix model recurrence coefficients expansion in powers of N^{-2} shifted
  index n+1/2"
- "Ercolani Pierce continuum limit Toda lattices odd weights recurrence coefficients half-integer shift even expansion"
- "Bleher Its \"Asymptotics of the partition function of a random matrix model\" recurrence coefficients expansion in powers
  N^{-2} R_n at (n+1/2)/N"
- KMVV math/0111252 (direct fetch of abstract and PDF)

## 4. Item T: the X_j structure and the (1 − u)^{1/2} signature

### 4.1 Findings
- No source located expands recurrence coefficients in monomials of the form n^{−1−jp} with spectral-zeta coefficients. No
  source has a "universal function of N⁻² and X_j", or a second-order edge kernel with a 1/(2j−1) Mellin pole.
- The nearest structural relatives are the genus expansions of §3.1. Their coefficients z_g(s) are functions of one scaling
  variable, and their even-in-N⁻² structure comes from the string equations, not from a monomial expansion.
- Trans-series in OP asymptotics appear in Painlevé double-scaling settings (e.g. Bleher–Deaño arXiv:1310.3768, title only).
  Those concern exponentially small terms, not power monomials.
- The query on fractional powers from non-analytic weights at a hard edge returned only multi-interval / Fisher–Hartwig papers
  (arXiv:2412.18656, math/0212014; titles only).

### 4.2 Verdict T
**NOT FOUND.** The search here was thinner than for N; the terminology ("trans-series", "monomials") may not match how such a
structure would be described.

**Queries:**
- "trans-series asymptotic expansion recurrence coefficients orthogonal polynomials non-integer powers n^{-1-jp} resurgence
  Jacobi matrix"
- "orthogonal polynomials weight x^alpha perturbed by non-analytic factor recurrence coefficients asymptotic expansion fractional
  powers of n Riemann-Hilbert hard edge"
- "recurrence coefficients asymptotic expansion as function of shifted index squared and perturbation parameters Toda flow
  nonlinear corrections Hankel determinant multiplicative perturbation x^{k} moments"

## 5. Actions (suggested; nothing done here)
1. **Q, decisive.** Read Beckermann–Kuijlaars, SINUM 39 (2001), Thm 2.1, and Kuijlaars, SIMAX 22 (2000), the Q = 0 papers.
   - If Thm 2.1 gives ν explicitly for a general σ, downgrade Theorem Q to PARTIALLY KNOWN (non-compact / hard-edge
     extension).
   - Cite BK 2002 eq. (2.25) as the compact, Q ≠ 0 analogue of (Q).
   - Cite Van Assche–Van Baelen 2020 as the tσ = const boundary case (fully saturated).
2. **N.** In JZC_M4 §2/§5, cite Bleher–Its 2005 Thm 5.2 (and Lemma 5.3's index reflection) and EMP Thm 2.2 as the known
   evenness phenomenon for varying weights. State that the zeta-valued shift −Z(0) and the fixed-measure setting are what is
   claimed.
3. **K.** Read Šťovíček–Świderski 2024 in full (regularised characteristic function ↔ reciprocal-spectrum OPs) before keeping
   SPEC S3/§3.7 and Theorem K as NOT FOUND.
4. **Rule L logging.** VERIFICATION_POLICY Rule L asks for queries in LOG.md. This file holds them; the LOG.md pointer is left to
   the session.
5. **Still to search.** MathSciNet/zbMATH: "recurrence coefficients" + "zeta function" + "asymptotic expansion"; Kuijlaars–Van
   Assche PLMS 1999 full text; KMVV §8.
