# Rule L novelty search — G1/RH pointwise laws (RH₁, RH₁(r), RH_p, RH_plt1b seam, RH_ζ)

Date: 2026-10-14. Searcher: subagent (read-only on jacobi-asymptotics). Repo files read: AGENTS.md, THEOREMS.md (§§1, 2.4, 4),
research/G1/CITATIONS.md, research/G1/RH/CITATIONS.md, research/G1/PROOF.md §0 and §4, headers/§0 of RH_p1.md,
RH_p1_general.md, px/RH_px.md, plt1/RH_plt1b.md, zeta/RH_zeta_close.md. Also read (read-only) the earlier item-11 search
math-pursuits/items/11-*/work/lit/LITERATURE.md (2026-10-12) so as not to duplicate it.

Absence of evidence is not evidence of absence: no MathSciNet/zbMATH access; several journal pages were paywalled (403).

---

## 0. Summary of verdicts

| Result | Verdict | One-line reason |
|---|---|---|
| RH₁ (p = 1, r = 3/2): Σk^{−3/2}δ_{1/k}, b_n = b_n^{TC}(1+O(1/n)) | **NOT FOUND** (method KNOWN) | Only Tricomi–Carlitz itself has an RH analysis (WLXZ); no perturbation of it to other weights on {1/k} found. |
| RH₁(r) (p = 1, all r > 1) | **PARTIALLY KNOWN (r = 2 only, non-rigorously)**; general r **NOT FOUND** | r = 2 is Monien's ζ(i+j) Hankel measure: a full expansion of log H_n is known *numerically* (Monien–Zagier), not proved; a rigorous RH proof of only the n²-order log H_n is *reported as unpublished* (personal communication). |
| RH_p (p > 1, s > 1) | **PARTIALLY KNOWN: (p, s) = (2, 2) is classical and exact** (Lommel, ν = 3/2); general p > 1, s **NOT FOUND** | σ_{2,2} = Σk^{−2}δ_{k^{−2}} is, after scaling by π², the squared (even-part) measure of the ν = 3/2 Lommel polynomials; its b_n are explicit. Checked here numerically to 15 digits. |
| RH_p, 0 < p < 1 (seam) | **NOT FOUND** | No explicit family and no RH analysis with atoms k^{−p}, p < 1, located. |
| RH_ζ (smooth-ζ model, κ/log n correction, κ = −0.28946…) | **NOT FOUND** | No source treats OPs on {1/(γ_j² + ¼)} pointwise; closest are Conway–Deift (log-weight hard edge, continuous weight) and the ζ-Hankel papers (different measure, n² level). |

Overall: the *method* (Deift–Zhou steepest descent for discrete OPs via the Borodin–Boyarchenko interpolation problem,
saturated regions, Bessel/Airy parametrices) is KNOWN. As of the sources opened, **WLXZ remains the only RH analysis of
discrete OPs on infinitely many nodes accumulating at a finite point**, and it is for one explicit family. Dai–Yao (2021)
say this explicitly (quoted in §2). The repo's pure-power results look new as theorems, except the exact (2, 2) case. The
smooth-ζ law also looks new.

---

## 1. Per-result detail

### 1.1 RH₁ (p = 1, r = 3/2) — NOT FOUND (method KNOWN)

**Closest prior work.**
- **WLXZ**, arXiv:1410.3948v1 (Anal. Appl. 14 (2016) 705–737). Abstract (arXiv API, verbatim): "In this paper, we
  develop the Riemann-Hilbert method to study the asymptotics of discrete orthogonal polynomials on infinite nodes with an
  accumulation point. To illustrate our method, we consider the Tricomi-Carlitz polynomials $f_n^{(α)}(z)$ where $α$ is a
  positive parameter. Uniform Plancherel-Rotach type asymptotic formulas are obtained in the entire complex plane including
  a neighborhood of the origin". §1 (PDF, verbatim): "We illustrate our method by concentrating on the Tricomi-Carlitz
  polynomials. It is worth noting that there are other polynomials share such a structure. For example, there is a class
  of sieved Pollaczek polynomials …". Also: "The objective of this paper is to derive the uniform asymptotics of the
  Tricomi-Carlitz polynomials, based only on the weight function".
- **Van Assche**, arXiv:math/9510214 §3 (verbatim): "(n + 1)f_{n+1}(x) − (n + α)xf_n(x) + f_{n−1}(x) = 0 … For the
  orthonormal polynomials [n!(α + n)/α]^{1/2} f_n this gives a_n = 0 and λ_n = n/[(n + α)(n + α − 1)] … The spectral
  measure now is supported on the set {±1/√(k + α) : k = 0, 1, 2, . . .}". So TC's coefficients are explicit, and WLXZ's
  RH result for them is a direct analysis of a known-coefficient family.

**What differs.** RH₁ changes the masses from the TC masses (≈ k^{−3/2} up to the Stirling factor H) to exact k^{−3/2}. It
proves a_n, b_n = TC values × (1 + O(1/n)) by absorbing H_n into WLXZ's band jump. No source found perturbs WLXZ's
construction, or treats any other weight on {1/k} or {±k^{−1/2}}. Semantic Scholar lists five citing works of
arXiv:1410.3948: Dai–Yao 2021, arXiv:1912.00500, a 2016 sieved-Pollaczek RH paper, a 2018 "Asymptotics of Orthogonal
Polynomials" item and arXiv:1412.8580. None of them treats this measure; titles and abstracts only, except Dai–Yao, which
was read (§2).

### 1.2 RH₁(r) (p = 1, every r > 1) — PARTIALLY KNOWN at r = 2 (numerical/unpublished); otherwise NOT FOUND

**Closest prior work.**
- **Monien**, arXiv:0901.1883v1, "Hankel determinants of Dirichlet series". H_n^{(0)}[ζ] = det ζ(i+j) is the Hankel
  determinant of Σk^{−2}δ_{1/k}, i.e. p = 1, r = 2. Verbatim (p. 2): "more detailed numerical experiments by D. Zagier
  confirmed our findings with the result H_n^{(0)}[ζ] = A^{(0)} ((2n+1)/√e …)^{−(n+½)²}(1 + … )". (The formula is
  garbled in the pdftotext extraction. The repo already transcribes it as ((2n+1)/(e√e))^{−(n+½)²}(1 + 1/(24(2n+1)²) −
  12319/(259200(2n+1)⁴) + …).) Also: "We do not know how to prove the full asymptotic expansions but will describe a method
  that lets one at least understand the weaker asymptotic form log H_n^{(0)}[ζ] ∼ log H_n^{(1)}[ζ] ∼ −n²(log(2n) − 3/2)."
- **Haynes–Zudilin**, arXiv:1510.01901v3 (SIGMA 11 (2015) 101), §1 (verbatim): "In [5] Monien developed these ideas
  further and rigorously justified the above asymptotics in the case r = 0, by explicitly constructing a family of
  orthogonal polynomials related to the corresponding Riemann–Hilbert problem. However, his approach does not readily
  generalize to prove the expected asymptotics for determinants built on the zeta values ζ(an + b) along an arithmetic
  progression". Here [5] = "Monien H., Personal communication, 2011". "The above asymptotics" is
  log H_n^{(r)} = −n² log n + O(n²).

**What differs.**
- At r = 2 the Monien–Zagier expansion implies (by second differences) nb_n = ½(1 + O(n^{−2})). That is stronger than
  RH₁(r)'s O(1/n), but it is **numerical only**.
- The reported rigorous RH work is unpublished, and per Haynes–Zudilin it is at the n² level (log H_n = −n² log n + O(n²)),
  not pointwise.
- No source covers r ≠ 2 or the a_n/(2b_n) law.
- RH₁(r) is therefore, as far as found, the first rigorous pointwise result even at r = 2. **Recommend** citing Monien and
  Monien–Zagier as the numerical precedent at r = 2. Note also that the repo's numerical k₀ = ½ − r gives k₀ = −3/2 at
  r = 2, but in the symmetric variable N. A check that RH₁(r)'s fit agrees with Zagier's 1/(24(2n+1)²) term after folding
  would be a cheap, useful cross-validation.

### 1.3 RH_p (p > 1, s > 1) — PARTIALLY KNOWN: (p, s) = (2, 2) exact; general NOT FOUND

**Closest prior work.**
- **Van Assche**, math/9510214 §3, verbatim: "Dickinson [7], Dickinson, Pollak, and Wannier [8], and Goldberg [13] also
  considered the polynomials h_{n,ν} satisfying the recurrence relation h_{n+1,ν}(x) = 2x(n + ν)h_{n,ν}(x) − h_{n−1,ν}(x)
  … considering p_n = √((n + ν)/ν) h_n, the three-term recurrence is of the form x p_n(x) = [2√((n+ν)(n+ν+1))]^{−1}
  p_{n+1}(x) + [2√((n+ν)(n+ν−1))]^{−1} p_{n−1}(x), which corresponds to a J-fraction and Jacobi operator with coefficients
  a_n = 0 and λ_n = [4(n + ν)(n + ν − 1)]^{−1} … the spectrum consists of the closure of the set {1/j_{k,ν−1} : k ∈ Z},
  where j_{k,ν−1} are the zeros of the Bessel function J_{ν−1}."
  - With ν = 3/2, j_{k,1/2} = πk, so the squared measure has atoms (πk)^{−2}.
  - **Own check (NUMERICAL, mpmath, 200 digits).** For σ_{2,2} (moments ζ(2j+2)), b_n from Hankel determinants equals
    π²c_{2n−2}c_{2n−1}, c_m = 1/(2√((m+3/2)(m+5/2))), to all 15 printed digits for n = 1..7. (This is the item-11
    observation, re-verified here.)
  - So n²b_n → π²/16 = c(2) with an explicit rate, and a_n similarly: **the (2, 2) instance of RH_p is classical.**
  - Even s = 2 + 2m follow from (2, 2) by Christoffel transforms (multiplying by x^m). Pointwise asymptotics there should
    be routine from the explicit kernel; this is my inference, not found in a source.
- Štampach–Šťovíček, arXiv:1403.8083 (abstract, verbatim): "These polynomials play a role analogous to that the Lommel
  polynomials do in the theory of Bessel functions … a Jacobi (tridiagonal) matrix J_L whose eigenvalues coincide with
  reciprocal values of the zeros of the regular Coulomb wave function F_L(η, ρ)". This is another p = 2 explicit family,
  but its atoms are not pure powers.
- Dai–Yao, arXiv:2104.03563: nodes k²/N², weight x^α e^{−Ncx}. These are growing nodes on a quadratic lattice, with an
  exponential weight (§2). Under x ↦ 1/x this is not σ_{p,s}, because the weight is exponential, not a power.

**What differs.** General p > 1 (non-integer, or p = 2 with s ≠ 2 + 2m) and general s: no source found. RH_p's
hard-edge Jacobi exponent α_x = (s−1−p)/p at 0, run through KMVV's endpoint −1, has no precedent in a discrete accumulating
setting. **Recommend** stating explicitly in THEOREMS/RH_px that the (2, 2) case is the classical Lommel ν = 3/2 family,
and using it as an exact check (the repo's plan-10 already mentions Lommel checks).

### 1.4 RH_p, 0 < p < 1 (seam) — NOT FOUND

- No explicit family with atoms ~k^{−p}, p < 1 (eigenvalues growing more slowly than 1/k) was found.
- No RH analysis was found where Γ-function poles enter the slit plane on rays arg z = ±pπ, which is the seam construction's
  motivation.
- The item-11 search reached the same conclusion for exact families ("Bessel ratios (0F1) only give p = 2, and
  Tricomi–Carlitz gives p = 1"); that is not a source.
- The arXiv API searches for "Tricomi-Carlitz", "accumulation point" + RH, and "infinite nodes" return only WLXZ (plus
  arXiv:2205.12815, a Krylov-complexity tutorial that treats TC as an example).

### 1.5 RH_ζ (smooth-ζ model) — NOT FOUND

**Closest prior work.**
- **Conway–Deift**, arXiv:1711.01590v4 (SIGMA 14 (2018) 056), abstract verbatim: "we compute the asymptotic behavior of
  the recurrence coefficients for polynomials orthogonal with respect to a logarithmic weight $w(x){\rm d}x = \log
  \frac{2k}{1-x}{\rm d}x$ on $(-1,1)$, $k > 1$, and verify a conjecture of A. Magnus for these coefficients. We use
  Riemann-Hilbert/steepest-descent methods, but not in the standard way as there is no known parametrix for the
  Riemann-Hilbert problem in a neighborhood of the logarithmic singularity at $x=1$."
  - This is the method RH_ζ §1 borrows for its hard edge (log N-size weight factor).
  - It is a continuous weight on a fixed interval. It does not give the 1/log n correction of a discrete ζ-zero-type
    measure.
- **Search for Jacobi matrices with spectrum {1/(γ²+¼)}.** Web search found only unrelated Hilbert–Pólya-style
  constructions (e.g. arXiv:2310.18423, "Zeta zeros and prolate wave operators", snippet only, not opened; it is not this
  measure).
- No source stating b_n/x_n = (π²/16)(1 + κ/log n + …) or κ = −2(log(π/2) − (1 − log 2)) was found.

**What differs.** The repo's measure (atoms 1/(γ_j²+¼) with smooth counting N₀(γ_j) = j − ½, masses 2x_j) is a model
with x_n ≍ log²n/n², not a pure power. It produces a second-order κ/log n term, which looks unrecorded.

---

## 2. Other sources consulted (opened)

- **Dai–Yao**, arXiv:2104.03563v1 (2021), §1, verbatim: "Wu et al. [21] studied the case where the orthogonality lattice
  consists of infinite nodes with an accumulation point. Except [21], the orthogonality lattices are always equally spaced.
  In the present paper, we will consider another example where the lattice is not uniformly distributed."
  - It also cites Van Assche–Van Baelen (q-lattice zero distribution, Constr. Approx., DOI 10.1007/s00365-020-09513-2):
    "Van Assche and Van Baelen consider polynomials orthogonal on a q-lattice {q^k …}". That is geometric accumulation,
    nth-root level only.
  - Dai–Yao do obtain recurrence-coefficient asymptotics: "The asymptotics for the normalizing coefficient h_{n,N},
    recurrence coefficients … are also obtained". This is the nearest *methodological* analogue of RH_p (non-uniform
    power lattice, band + saturated region + Gamma-function origin parametrix). But it has an exponential varying weight
    and nodes growing to ∞.
- **BKMM announcement**, math/0212149, and **Bleher–Liechty**, arXiv:0909.1985. Abstract verbatim: "We consider the
  large-N asymptotics of a system of discrete orthogonal polynomials on an infinite regular lattice of mesh 1/N, with
  weight e^{−NV(x)}". Regular lattices only.
- **Haynes–Zudilin** and **Monien**: §1.2.
- **Joshi–Lasic Latimer q-RH papers**, arXiv:2111.11663 (abstract). Verbatim: "We describe a Riemann-Hilbert problem for
  a family of q-orthogonal polynomials … the asymptotic behaviour near the location of their smallest zeros, x ∼ q^{n/2},
  and norm, ‖P_n‖₂, are independent of the weight function". Geometric lattice {±q^k}, so b_{n+1}/b_n → q, outside
  Law P.
- **Van Assche math/9510214**: also lists the van Doorn / Chihara–Ismail birth–death families (compact J + μI,
  accumulation at μ). Their coefficients are explicit, so these are direct, not inverse.
- **Direct-problem literature** (web-search snippets only; not opened, so not citable under Rule C): Kozhan
  arXiv:1210.1292; Janas–Naboko–Stolz (mp_arc 03-378); Boutet de Monvel–Janas–Zieliński arXiv:1206.1763; Pruckner
  arXiv:1704.06789. All of them go coefficients → eigenvalues, mostly unbounded. None is an inverse pointwise result.
- **Secondary only**: MathWorld "Riemann Zeta Function Zeta(5)". It reports Fauzan (2026, Zenodo DOI
  10.5281/zenodo.22826419) "uses rationally normalized determinants of Hankel matrices" for ζ(5) irrationality.
  - Not opened. If it uses det ζ(a(i+j)+b)-type asymptotics, it is relevant to H1/HZ (G2), not to G1/RH.
  - Lai, arXiv:2610.06838 (cites Haynes–Zudilin) builds on Fauzan; abstract only.

## 3. Not obtained (no claims made)

- Ou–Wong, Anal. Appl. 8 (2010) 247–286, "The Riemann–Hilbert approach to global asymptotics of discrete orthogonal
  polynomials with infinite nodes" (World Scientific 403). Per Dai–Yao and WLXZ it is a regular infinite lattice.
- The BKMM monograph (Ann. Math. Stud. 164).
- Goh–Wimp 1994; Lee–Wong (PAMS 2010; JCAM 2014) on TC uniform expansions (abstract/snippet only).
- Chen–Ismail; Ismail's book Ch. 6; Dickinson 1954 / DPW 1956 / Goldberg 1965 (only as quoted by Van Assche).
- Kuijlaars–Van Assche, Proc. LMS 1999 (nth-root only, per item 11).
- The 2016 sieved-Pollaczek RH paper citing WLXZ: the title shows an a.c. part plus masses accumulating; the measure
  differs, but the paper was not opened.
- The WLXZ Anal. Appl. 2016 version.

## 4. Suggested references to add (CITATIONS / novelty paragraph)

1. Van Assche, arXiv:math/9510214 §3 (Lommel ν = 3/2 ⇒ exact (p, s) = (2, 2); TC recurrence). Primary sources: Dickinson,
   PAMS 5 (1954); Dickinson–Pollak–Wannier, Pacific J. Math. 6 (1956); Goldberg, Pacific J. Math. 15 (1965).
2. Monien, arXiv:0901.1883 (numerical full expansion at p = 1, r = 2), and Haynes–Zudilin, arXiv:1510.01901 (unpublished
   rigorous n²-level RH claim; conjecture for ζ(a(i+j)+b)).
3. Dai–Yao, arXiv:2104.03563 (states WLXZ is the only accumulating-lattice RH analysis; nearest method analogue).
4. Conway–Deift, arXiv:1711.01590 (already cited for RH_ζ).
5. Štampach–Šťovíček, arXiv:1403.8083 (another explicit compact family, p = 2, non-pure atoms; possible extra check).

## 5. Search terms used

Web: "orthogonal polynomials discrete measure masses at 1/k accumulating at zero recurrence coefficients asymptotics
Riemann-Hilbert"; "Wu Lin Xu Zhao Tricomi-Carlitz … cited by"; "Jacobi matrix eigenvalues k^{-p} asymptotics …
compact Jacobi operator"; "Hankel determinants of zeta values asymptotics proof orthogonal polynomials …";
"\"accumulation point\" discrete orthogonal polynomials Riemann-Hilbert 2017–2025"; "discrete orthogonal polynomials
non-uniform lattice Riemann-Hilbert …"; "Monien Zagier Hankel determinant zeta(i+j) …"; "inverse spectral problem Jacobi
matrix eigenvalues power law accumulating at zero …"; "Jacobi matrix off-diagonal n^{-alpha} compact eigenvalue
asymptotics … Janas Naboko"; "Jacobi matrix spectrum Riemann zeta zeros recurrence coefficients …"; "Haynes Zudilin …
conjecture … proved"; "Fauzan irrationality of zeta(5) determinant method Hankel".

arXiv API: abs:"Tricomi-Carlitz"; au:Monien_H AND abs:Hankel/orthogonal; abs:"accumulation point" AND "orthogonal
polynomials" AND Riemann-Hilbert; abs:"zeta values" AND Hankel; abs:"discrete orthogonal polynomials" AND "infinite
nodes"; abs:"Lommel polynomials"; abs:"compact Jacobi" AND asymptotic; abs:"orthogonal polynomials" AND "non-uniform
lattice" AND Riemann-Hilbert.

Semantic Scholar citations of: 1410.3948 (WLXZ), 0901.1883 (Monien), 1510.01901 (Haynes–Zudilin). Citations of 2104.03563
and 1711.01590 were not retrieved (rate-limited or empty).

## 6. Natural expert readers (for Rule R / verification)

- **Yu-Qiu Zhao** (Sun Yat-sen), **Yu Lin** (South China Univ. of Technology), **Shuai-Xia Xu**, **Xiao-Bo Wu**: the WLXZ
  authors; RH₁/RH₁(r)/RH_p perturb their construction directly.
- **Dan Dai** (City Univ. Hong Kong): discrete Laguerre on a k²/N² lattice; Krawtchouk.
- **Roderick Wong**: the Wong school of global asymptotics of discrete OPs.
- **Arno Kuijlaars**, **Walter Van Assche** (KU Leuven): KMVV/KV/Vanlessen parametrices used here; constrained
  equilibrium; compact Jacobi matrices.
- **Pavel Bleher**, **Karl Liechty**: band–saturated endpoint parametrices.
- **Percy Deift**, **Thomas O. Conway**: for RH_ζ's log-weight hard edge.
- **Wadim Zudilin**, **Hartmut Monien**: ζ-Hankel side. Monien may hold the unpublished r = 2 RH analysis.
- **František Štampach**, **Pavel Šťovíček**: explicit compact Jacobi families; good for spotting further exact cases.
