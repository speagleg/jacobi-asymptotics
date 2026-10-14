# Novelty search (Rule L): G2, Theorem H_all, B*, Corollary HZ

Date: 2026-10-14. Searcher: subagent (read-only on the repo). Inputs read first: AGENTS.md, THEOREMS.md (G2 rows),
research/G2/PROOF.md, research/G2/CITATIONS.md (there is no top-level CITATIONS.md; the per-area files were used).

Rule C: "OPENED" means I fetched the source text (arXiv PDF or abstract page, publisher abstract page) and the quotes
below are copied from it. "SEEN" means the source appeared only in search results or as a citation inside another source.
I make no claims about SEEN sources beyond their bibliographic data.

---

## Verdicts

| Result | Verdict |
|---|---|
| H_all, general p > 0 (n² term with explicit constant, discrete measure with atoms ~ Ck^{−p}) | **NOT FOUND (apparently new)** |
| B*: the explicit constrained equilibrium (average of arcsine laws, saturated on (0, 4c(p)]), proved optimal and unique | **PARTIALLY KNOWN**: the framework is known, and for p = 1 the optimizer is known heuristically (Monien). The general-p solution and the optimality proof were not found. |
| Cor. HZ, a = 1 (det ζ(i+j+r)) | **PARTIALLY KNOWN**: the n² constant 3/2 − log 2 is stated by Monien, derived heuristically and checked numerically (with Zagier's numerics). A rigorous proof of the leading term for r = 0 is attributed to Monien only as a personal communication. No rigorous published n² constant was found. |
| Cor. HZ, integer a ≥ 2 | **a = 2, b ∈ {−2, 0, 2}: KNOWN implicitly** (exact closed forms, Baricz–Štampach 2018; the n² asymptotic is an immediate corollary, though not stated there). **All other integer a ≥ 2** (including a = 2 with b odd, the case Haynes–Zudilin care about): **NOT FOUND (apparently new)**. Only the weaker bounds (≤ −(a/2)n² log n + O(n²), and a −cn² upper bound) are in print. The leading-order expectation is stated as a conjecture by Haynes–Zudilin. |
| Cor. HZ, real a > 0 | **NOT FOUND (apparently new)**. |
| Lemma Sat-type saturation | The *notion* of saturation in constrained problems is **KNOWN** in general form (Dragnev–Saff 1997 abstract: "a saturation result"). The specific saturation interval (0, 4c(p)], fixed by the defining equation of c(p), was not found. |

---

## 1. Theorem H_all (general p > 0)

**Closest prior work.**

(a) Monien, arXiv:0901.1883 (OPENED). He handles only F = ζ, i.e. p = 1 with atoms 1/k:

> "We derive a general expression for the Hankel determinants of a Dirichlet series F(s) and derive the asymptotic
> behavior for the special case that F(s) is the Riemann zeta function. In this case the Hankel determinant is a
> discrete analogue of the Selberg integral and can be viewed as a matrix integral with discrete measure."
>
> "We do not know how to prove the full asymptotic expansions but will describe a method that lets one at least
> understand the weaker asymptotic form log H_n^{(0)}[ζ] ∼ log H_n^{(1)}[ζ] ∼ −n²(log(2n) − 3/2)."

Monien's Theorem 2.1 (the general multiple-sum, or Heine, formula) holds for any Dirichlet series. His asymptotic
analysis covers only f ≡ 1 and moments ζ(i+j+r), that is, exponent a = 1. He does not treat ζ(a(i+j)+b) with a ≠ 1.

(b) Haynes–Zudilin, SIGMA 11 (2015) 101, arXiv:1510.01901, DOI 10.3842/SIGMA.2015.101 (OPENED; abstract via the arXiv
API, §1 via ar5iv):

> "We study the asymptotics of Hankel determinants constructed using the values ζ(an+b) of the Riemann zeta function
> at positive integers in an arithmetic progression. Our principal result is a Diophantine application of the
> asymptotics."
>
> "However, his approach does not readily generalize to prove the expected asymptotics for determinants built on the
> zeta values ζ(an+b) along an arithmetic progression, which are more interesting from an arithmetical point of view.
> To be precise, for positive integers a and b, we expect that log det_{1≤i,j≤n} ζ(a(i+j)+b) = −an² log n + O(n²)
> as n → ∞."

The repo's CITATIONS.md (HZ) already quotes their proved bound, ≤ −(a/2)n² log n + O(n²).

(c) Coons–Sutherland, arXiv:1404.2699 (OPENED, PDF). They prove only an O(n²) upper bound, for general nonnegative
Dirichlet series:

> "Theorem 1.3. Let F(s) = Σ_{n⩾1} f(n)n^{−s} be a nondegenerate ordinary Dirichlet series with f(n) ⩾ 0 for all n,
> which is convergent for ℜ(s) ⩾ s0. Then H_n^{(r)}[F] > 0 for all n ⩾ 1 and r ⩾ s0 − 2, and there is a c > 0 such
> that log H_n^{(r)}[F] < −cn², for all sufficiently large integers n and r."

**What differs.** None of these papers proves a leading term −pn² log n for any p ≠ 1, or any n² constant. Nor does
any of them treat general discrete measures Σ w_k δ_{x_k} with x_k ~ Ck^{−p} and weights subject only to Σw < ∞ and a
polynomial lower bound. Searches of the constrained-equilibrium and discrete-OP literature (§2) turned up only
lattices of integer type (Charlier, Meixner, Krawtchouk), compact intervals (Rakhmanov) and geometric q-lattices (Van
Assche–Van Baelen). None of these has nodes accumulating at a point with polynomial spacing, and none gives n²-level
Hankel asymptotics of this type. **Verdict: NOT FOUND.**

Caveat: no full-text access to Kuijlaars–Van Assche, *Proc. LMS* 79 (1999) or *J. Approx. Theory* 99 (1999), or to
Beckermann, *Constr. Approx.* 16 (2000). A paywalled paper could in principle contain the power-law lattice case.
Judging from their abstracts (§2), they treat zero distributions and n-th root asymptotics on Charlier/Meixner-type
sets, not Hankel determinants of measures accumulating at 0.

---

## 2. B*: the explicit constrained equilibrium

**Closest prior work.**

(a) Monien §3 (OPENED). He gives the p = 1 optimizer, heuristically:

> "We seek a continuous test function ρ(x) which maximizes the functional Eq. 3.5 subject to the constraint that
> 0 < ρ(x) ≤ 1 for all x and ρ(x) = 0 for x < 0 and Eq. 3.4. We assume that such a continuous functions exists."
>
> "Theorem 3.1. Define the function ρ(x) for x ∈ [0, ∞): ρ(x) = 1 (0 ≤ x ≤ 1/2), ρ(x) = (2/π)(arctan(1/√(2x−1))
> − √(2x−1)/(2x)) (x > 1/2). Then ρ(x) is the continuous solution of the stationary condition Eq. 3.7 for x > 1/2…"

(These quotes are already in the repo's CITATIONS.md (M). I re-opened the PDF and confirmed the wording of the first
and of the "We do not know how to prove" sentence.)

(b) The constrained-equilibrium framework (Rakhmanov 1996; Dragnev–Saff 1997; Kuijlaars–Van Assche 1999).

- Coroian–Dragnev–Legg–Orive, arXiv:2608.11987 (OPENED, abstract):
  > "The constrained equilibrium problem for the logarithmic potential was introduced by Rakhmanov (1996) as he
  > realized that the asymptotic distribution of the zeros of discrete orthogonal polynomials in a compact interval
  > could be described in terms of the equilibrium measure of this interval in a class of measures subject to a
  > certain constraint. Other authors such as Dragnev and Saff (1997), and Kuijlaars and Van Assche (1999), extended
  > this approach to more general settings."
- Dragnev–Saff, *J. Anal. Math.* 72 (1997) 223–259, DOI 10.1007/BF02843160 (OPENED, Springer abstract page; part of
  the abstract was garbled on the page):
  > "we prove existence and uniqueness of a measure … that minimizes the weighted logarithmic energy over the class …
  > We also obtain a characterization theorem, a saturation result and a balayage representation … As applications of
  > our results, we determine the (normalized) limiting zero distribution for ray sequences of a class of orthogonal
  > polynomials of a discrete variable. Explicit results are given for the class of Krawtchouk polynomials."
- Kuijlaars–Van Assche, "Extremal polynomials on discrete sets", *Proc. LMS* 79 (1999) 191–221,
  DOI 10.1112/S0024611599011867 (OPENED, Cambridge abstract page):
  > "We study asymptotics for orthogonal polynomials and other extremal polynomials on infinite discrete sets, typical
  > examples being the Meixner polynomials and the Charlier polynomials. Following ideas of Rakhmanov, Dragnev and
  > Saff, we show that the asymptotic behaviour is governed by a constrained extremal energy problem for logarithmic
  > potentials, which can be solved explicitly. We give formulas for the contracted zero distributions, the nth root
  > asymptotics and the asymptotics of the largest zeros."
- Van Assche–Van Baelen, arXiv:1910.12518, *Constr. Approx.* 2020 (OPENED, abstract + intro). This is the
  geometric-lattice analogue, with nodes accumulating at 0:
  > "We give the asymptotic behavior of the zeros of orthogonal polynomials, after appropriate scaling, for which the
  > orthogonality measure is supported on the q-lattice {q^k, k=0,1,2,3,…}, where 0 < q < 1. The asymptotic
  > distribution of the zeros is given by the radial part of the equilibrium measure of an extremal problem in
  > logarithmic potential theory for circular symmetric measures with a constraint imposed by the q-lattice."

(c) The "average of arcsine laws" structure. This is the Kuijlaars–Van Assche varying-coefficient theorem, quoted from
Coussement–Coussement–Van Assche, arXiv:math/0606440 (OPENED, PDF), Theorem 1.3:

> "Theorem 1.3 (Kuijlaars, Van Assche [20]). Let for each N ∈ ℕ, two sequences {a_{n,N}}, a_{n,N} > 0, and {b_{n,N}},
> b_{n,N} ∈ ℝ, of recurrence coefficients be given. Furthermore, suppose there exist two continuous functions
> a : (0,+∞) → [0,+∞), b : (0,+∞) → ℝ, such that lim_{n/N→t} a_{n,N} = a(t), lim_{n/N→t} b_{n,N} = b(t), t > 0, and
> define γ(t) := b(t) − 2a(t), δ := b(t) + 2a(t), t > 0. For the (orthogonal) polynomials generated by the recurrence
> zP_{n,N}(z) = P_{n+1,N}(z) + b_{n,N}P_{n,N}(z) + a²_{n,N}P_{n−1,N}(z) … we then have
> lim_{n/N→t} ν(P_{n,N}) = (1/t)∫_0^t ω_{[γ(s),δ(s)]} ds, t > 0."
>
> [20] "A. B. J. Kuijlaars and W. Van Assche. The asymptotic zero distribution of orthogonal polynomials with varying
> recurrence coefficients. J. Appr. Theory 99 (1999), 167–97."

**What differs.**
- Monien handles only p = 1. He assumes existence, checks only stationarity, and gives no upper bound, no uniqueness
  and no discretization. His §3 never mentions Rakhmanov or constrained equilibrium (checked on ar5iv).
- The framework papers have different settings:
  - Rakhmanov: compact interval.
  - Dragnev–Saff: weighted problem with a general constraint; Krawtchouk worked out.
  - Kuijlaars–Van Assche 1999: Charlier/Meixner.
  - Van Assche–Van Baelen: q-lattice with x^{1/n} scaling.

  None solves the problem with constraint σ = (1/p)x^{−1−1/p}dx on (0, ∞), i.e. Lebesgue on (0, ∞) after the u = k/n
  change of variables, which has infinite mass at the accumulation point. None gives the closed form
  dμ*/dσ = I_{min(1,x/4c)}(1/p + ½, ½) or the value κ_p = 3p/2 + log c(p).
- KVA's theorem gives the forward direction: recurrence coefficients ⇒ averaged arcsine zero distribution. Applied with
  a(t) = 2c t^{−p}, b(t) = c t^{−p} (a continuous function on (0, ∞), as the hypothesis requires), it yields the
  *shape* μ* = ∫_0^1 ω_{[0,4ct^{−p}]} dt as the zero distribution of Jacobi matrices obeying Law P. This is the
  "forward Weyl law" of item 11 Theorem B. B* adds three things:

  *(Correction, 2026-10-14, Paper 1 drafting and Rule R review `papers/paper1/REVIEW_Paper1.md` F9. The coefficient
  assignment above is swapped relative to KVA's convention. KVA's recurrence is zP = P_{n+1} + b P_n + a² P_{n−1}, so b
  is diagonal and a is off-diagonal, with γ = b − 2a and δ = b + 2a. With a(t) = 2ct^{−p} and b(t) = ct^{−p} one gets
  [γ, δ] = [−3ct^{−p}, 5ct^{−p}], which is wrong. The correct assignment is a(t) = ct^{−p} (off-diagonal) and
  b(t) = 2ct^{−p} (diagonal). It gives [0, 4ct^{−p}] and the shape μ* stated here, and it matches item 11's Law P
  (diagonal ∼ 2 × off-diagonal). The conclusion of this paragraph is unchanged.)*
  1. the identification of this average as the unique constrained energy maximizer;
  2. the fact that saturation pins c = c(p);
  3. the energy value.

**Verdict: PARTIALLY KNOWN.** The method and framework are known, and the p = 1 optimizer is known heuristically.
**Suggestion:** a paper should cite KVA 1999 (JAT) for the averaged-arcsine structure, and Rakhmanov / Dragnev–Saff /
KVA (PLMS) for constrained equilibria. It should state that the novelty lies in the specific accumulating-lattice
problem, its explicit general-p solution, and the rigorous variational ⇒ Hankel-determinant transfer (A1, A-U, A-L).

---

## 3. Corollary HZ

### a = 1 (det ζ(i+j+r))

Monien (OPENED) records the full Zagier conjectural expansion, with the same n² constant:

> "In fact more detailed numerical experiments by D. Zagier confirmed our findings with the result
> H_n^{(0)}[ζ] = A^{(0)} ((2n+1)/(e√e))^{−(n+½)²}(1 + (1/24)(2n+1)^{−2} − …)"

Then log H_n^{(0)} = −n² log(2n) + (3/2)n² + O(n log n) = −n² log n + (3/2 − log 2)n² + …. This matches Cor. HZ at
a = 1, since c(1) = ½. The same expansion is repeated in Coons–Sutherland (OPENED): "according to Monien, detailed
numerical experiments by Zagier suggest that…".

On rigor, Haynes–Zudilin §1 (OPENED) says:

> "In [5] Monien developed these ideas further and rigorously justified the above asymptotics in the case r=0, by
> explicitly constructing a family of orthogonal polynomials related to the corresponding Riemann–Hilbert problem."

Their reference [5] is only **"H. Monien, Personal communication, 2011"** (bibliography checked on ar5iv). The
"above asymptotics" is the weak form −n² log n + O(n²), not the n² constant. No published Monien follow-up was found:
OpenAlex lists 5 citers of 0901.1883, and none is by Monien.

**Verdict: PARTIALLY KNOWN.** The constant is conjectured and numerically confirmed, with a heuristic derivation. A
rigorous leading-order result for r = 0 exists only as an unpublished claim. A rigorous published n² constant was not
found. Cor. HZ (and item 11 Theorem H for p = 1) would give the first written proof of the constant 3/2 − log 2, for
all r > −1.

### Integer a ≥ 2

**a = 2, even b: KNOWN in closed form.** Baricz–Štampach, "The Hurwitz-type theorem for the regular Coulomb wave
function via Hankel determinants", arXiv:1708.07729, *Linear Algebra Appl.* 548 (2018) 259–272 (OPENED, PDF):

> "Corollary 3. For n ∈ ℕ, ν ∉ −ℕ, and ℓ ∈ {0, 1}, one has det H_n^{(ℓ)}(ν) = 2^{−2n(n+ℓ)} Π_{k=1}^{2n+ℓ−1}
> (ν + k)^{k−2n−ℓ}."
>
> (Remark 5) "det H_n^{(2)}(ν) = 2^{−2n(n+2)} (n + 1)(n + ν + 1) Π_{k=1}^{2n+1} (ν + k)^{k−2n−2}"
>
> (22) "σ_{2n}(1/2) = ζ(2n)/π^{2n} = (−1)^{n+1} (2^{2n−1}/(2n)!) B_{2n}"

Here H_n^{(ℓ)}(ν) has (i, j) entry σ_{2(i+j)+2ℓ−2}(ν), the Rayleigh function. At ν = ½ and after a diagonal rescaling by
powers of π, this gives det_{1≤i,j≤n} ζ(2(i+j)+b) exactly for b = 2ℓ − 2 ∈ {−2, 0, 2}. The case b = 2 is in
Haynes–Zudilin's range. The paper also has an ℓ = 3 formula (b = 4), but my text extraction of it did not reproduce the
numbers, so I treat it as unverified.

My numerical check (NUMERICAL; script `program/novelty_G2_bs_check.py`, mpmath at 60 digits):
- The ℓ = 0, 1, 2 formulas agree with direct determinants of ζ-values at n = 2, 4, 6, to 15 digits.
- (log det + 2n² log n)/n² from the closed form is 2.5162 (ℓ = 0), 2.5150 (ℓ = 1) and 2.5139 (ℓ = 2) at n = 16000,
  approaching κ_2 = 3 + log(π²/16) = 2.51687 like O(log n/n).

So Cor. HZ for a = 2, b ∈ {−2, 0, 2} is an elementary consequence of a published closed form, though Baricz–Štampach
do not state the asymptotics. More generally, the p = 2 Lommel/Rayleigh family (atoms j_{ν,k}^{−2}) is exactly solvable;
item 11 already uses this.

**a = 2 with b odd (the arithmetically interesting case in HZ), and every a ≥ 3:** no proof of even the leading term
−an² log n was found. Only the Haynes–Zudilin bound (≤ −(a/2)n² log n + O(n²)) and the Coons–Sutherland bound
(< −cn²) are in print. **NOT FOUND (apparently new):** both the leading term (which settles Haynes–Zudilin's stated
expectation) and the n² constant 3a/2 + log c(a).

### Real a > 0

**NOT FOUND (apparently new).** Not even conjectured in the sources opened.

### Related but different: Fauzan's ζ(5) work

Fauzan (2026) uses Hankel determinants and a logarithmic-energy estimate, but for a different moment functional:

- Fauzan, "ζ(5) is irrational", zenodo:22826419 (OPENED, record page: abstract describes "normalized Hankel
  determinants", "a positive moment representation and a logarithmic-energy estimate"; the full manuscript is "in
  preparation").
- Li Lai, arXiv:2610.06838 (OPENED): "Fauzan's proof uses Hankel determinants, which were previously studied by
  Haynes–Zudilin [23] and Zudilin [55]."
- Romik's Lean formalization README (OPENED) mentions "the arcsine measures and ρ, U^ρ, the field V of (6.1)", which
  suggests an equilibrium-type energy estimate.
- MathWorld (OPENED) describes integer polynomials Q_n of degree 37n with 0 < Q_n(ζ(5)) < e^{−139n²/5}.

None of these states asymptotics of det ζ(a(i+j)+b). Because of the topical overlap (Hankel determinants of zeta-type
moments, log energy, arcsine measures), a paper on HZ should cite Fauzan and say what differs. The full Fauzan
manuscript should be re-checked once it is available.

---

## 4. Sources consulted

**OPENED (text read; quotes above are copied from these):**
1. H. Monien, Hankel determinants of Dirichlet series, arXiv:0901.1883 (PDF + ar5iv).
2. A. Haynes, W. Zudilin, Hankel determinants of zeta values, SIGMA 11 (2015) 101, arXiv:1510.01901,
   DOI 10.3842/SIGMA.2015.101 (ar5iv §1 + bibliography; arXiv API abstract).
3. M. Coons, D. Sutherland, Towards the (ir)rationality of values of Dirichlet series, arXiv:1404.2699 (PDF).
4. Á. Baricz, F. Štampach, The Hurwitz-type theorem for the regular Coulomb wave function via Hankel determinants,
   arXiv:1708.07729, Linear Algebra Appl. 548 (2018) 259–272 (PDF).
5. E. Coussement, J. Coussement, W. Van Assche, Asymptotic zero distribution for a class of multiple orthogonal
   polynomials, arXiv:math/0606440 (PDF; source of the KVA Theorem 1.3 quote).
6. W. Van Assche, Q. Van Baelen, Zero distribution of orthogonal polynomials on a q-lattice, arXiv:1910.12518,
   Constr. Approx. 2020 (abstract + intro, PDF).
7. P. D. Dragnev, E. B. Saff, Constrained energy problems with applications to orthogonal polynomials of a discrete
   variable, J. Anal. Math. 72 (1997) 223–259, DOI 10.1007/BF02843160 (Springer abstract page only).
8. A. B. J. Kuijlaars, W. Van Assche, Extremal polynomials on discrete sets, Proc. LMS 79 (1999) 191–221,
   DOI 10.1112/S0024611599011867 (Cambridge abstract page only).
9. D. Coroian, P. Dragnev, A. Legg, R. Orive, On constrained Riesz minimum energy problems, arXiv:2608.11987 (abstract).
10. Li Lai, The linear independence of 1, ζ(3), and ζ(4), arXiv:2610.06838 (HTML).
11. A. Fauzan, ζ(5) is irrational, zenodo:22826419 (record page only).
12. D. Romik, zeta5-irrationality GitHub README (formalization of Fauzan).
13. MathWorld, "Riemann Zeta Function zeta(5)" (secondary; for Fauzan's announced bound).
14. M. B. Green, C. Wen, Superstring amplitudes, unitarity, and Hankel determinants of MZVs, arXiv:1908.08426
    (abstract; positivity only, not relevant).
15. T. Ferguson, Rational approximations via Hankel determinants, arXiv:2003.10616 (abstract; not relevant).
16. S.-Y. Chung, S. Lee, Y. W. Park, arXiv:2406.09746 (abstract; Hankel formula for Rayleigh-type sums of J_ν′ zeros).
17. H.-J. Fischer, Z. Anal. Anwend. 14 (1995) 141–155, DOI 10.4171/ZAA/667 (abstract page; means of recurrence
    coefficients for self-similar measures; not relevant).
18. G. Świderski, B. Trojan, arXiv:2311.04853 (abstract; unbounded Jacobi matrices; not relevant).

**SEEN only (search results / citations; nothing claimed about content):**
- E. A. Rakhmanov, Equilibrium measure and the distribution of zeros of the extremal polynomials of a discrete
  variable, Sb. Math. 187:8 (1996) 1213–1228 (mathnet sm153: connection refused).
- A. B. J. Kuijlaars, W. Van Assche, The asymptotic zero distribution of OPs with varying recurrence coefficients,
  J. Approx. Theory 99 (1999) 167–197 (ScienceDirect 403; statement taken from source 5).
- B. Beckermann, On a conjecture of E. A. Rakhmanov, Constr. Approx. 16 (2000) 427–448 (Springer redirect, not read).
- W. Zudilin, A determinantal approach to irrationality, Constr. Approx. 45 (2017) 301–310,
  DOI 10.1007/s00365-016-9333-7.
- Daniel Sutherland, Arithmetic applications of Hankel determinants (thesis, Newcastle 2015).
- N. Kishore, The Rayleigh function, PAMS 14 (1963) 527–533; Serra-Capizzano 2001 (measurable a, b extension of KVA);
  Maki 1980 (Ullman distribution); Janas–Naboko / Janas–Malejki (eigenvalue asymptotics, unbounded case).

## 5. Suggested references for a paper

Essential:
- Monien (arXiv:0901.1883): p = 1 heuristic and the same optimizer.
- Haynes–Zudilin (SIGMA 2015): the conjecture and the weak bound.
- Coons–Sutherland (arXiv:1404.2699).
- Baricz–Štampach (LAA 2018): exact a = 2, even b.

Framework:
- Rakhmanov 1996; Dragnev–Saff 1997; Kuijlaars–Van Assche (PLMS 1999) and (JAT 1999, averaged arcsine); Beckermann 2000.
- Van Assche–Van Baelen 2020 (accumulating q-lattice analogue).
- Saff–Totik (already in G2 via (P)). *(Plan 47 note, 2026-10-14: G2 no longer uses (P); B*(iii) rests on G2 Lemma EP,
  a self-contained Fourier proof. Saff–Totik remains a literature pointer.)*
- Beckermann–Kalyagin–Matos–Wielonsky (already cited).

Context:
- Fauzan 2026 / Lai 2026 (Hankel determinants in irrationality proofs).
- Zudilin 2017 (Constr. Approx.).
- Lommel/Tricomi–Carlitz (item 11's exactly solvable families).

## 6. Search terms tried

- "Hankel determinants of zeta values" (asymptotics; citing works; 2020–2025).
- Monien "Hankel determinants" rigorous / Riemann–Hilbert.
- "Hankel determinants of Dirichlet series" citations.
- Constrained equilibrium for discrete OPs with nodes accumulating at zero.
- Dragnev–Saff constrained energy; Rakhmanov discrete variable.
- Kuijlaars–Van Assche varying recurrence coefficients / averaged arcsine.
- OPs with mass points 1/k^p, recurrence asymptotics n^p b_n.
- Compact Jacobi matrices with n^{−p} entries, Weyl law.
- Ullman distribution / Nevai–Dehesa contracted zeros.
- "discrete analogue of the Selberg integral".
- Hankel determinant of the Rayleigh function / Lommel / Bernoulli; Hurwitz zeta Hankel.
- "n^2 log n" Hankel discrete measure / Stieltjes / Widom-type.
- Fauzan ζ(5) Hankel; Zudilin determinantal approach.
- arXiv API queries:
  - "Hankel determinants" AND zeta
  - "constrained equilibrium" AND Hankel
  - "Lommel polynomials" AND asymptotic
  - "constrained energy" AND "orthogonal polynomials"
- OpenAlex citers of Monien 0901.1883 and of Haynes–Zudilin (3 citers: Green–Wen ×2, a Ramanujan-type formula paper).

Limitations: no MathSciNet access. Paywalled full texts (KVA JAT/PLMS, Beckermann, Rakhmanov, Dragnev–Saff) could not
be read beyond their abstracts. The Semantic Scholar API was rate-limited, so Google-Scholar-style "cited by" coverage
comes only from OpenAlex.
