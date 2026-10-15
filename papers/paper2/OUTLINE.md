# Paper 2 — outline (for parallel drafting)

Status: OUTLINE, 2026-10-14, branch `paper-2-law`. No LaTeX prose yet. This file is the single contract for
the drafters. It fixes the statements, the notation, the order of the argument and the style. A drafter who
needs to depart from it records the reason in `papers/paper2/NOTES.md` (to be created when drafting starts).

Companion: Paper 1 = `papers/paper1/main.tex` ("Hankel determinants of discrete measures with power-law atoms,
and of zeta values"; averaged law and the constrained equilibrium problem). Paper 3 (announced here only) = rough
weights break the pointwise law.

Contents of this file:
- §0 Decisions at a glance
- §1 Title, abstract, story
- §2 Theorem statements for the introduction
- §3 Architecture of the proof (dependency diagram, main text vs appendices, the geometry table)
- §4 Notation table
- §5 Section-by-section plan, with sources
- §6 Style guide for the drafters
- §7 Risk list
- §8 Drafting split
- §9 Figure and table plan
- §10 Source map and renaming table (repo name → paper name)

---

## 0. Decisions at a glance

1. **One Riemann–Hilbert analysis, not five.** The repo proves the pure-power law three times by quotient
   (glued-parametrix) constructions: RH_px for p > 1, RH₁(r) for p = 1 (symmetric WLXZ frame) and the RH_plt1b
   seam construction for p < 1. It then proves the weighted law a second time by a Conway–Deift comparison: ROUTE2,
   ROUTE2_xframe1 and ROUTE2_plt1. The paper presents **only the comparison analysis**, once, for an analytic
   slowly varying factor ℓ₁. The pure powers are the case ℓ₁ ≡ 1 (Λ ≡ 0, so the mismatch has no slowly varying
   part). This is legitimate: the REVIEWED statements of RII, RII_x1 and RII_{<1} include Λ ≡ 0. ROUTE2 Rule A (a),
   ROUTE2_xframe1 Rule A (a) and ROUTE2_plt1 Rule A (a) check consistency in that case. The quotient constructions
   appear only in a remark.
2. **Base window plus shift.** The RH analysis covers exactly the range α ∈ (−1, 1), i.e. 1 < s < 1 + 2p, for
   every p > 0. Here α := (s − 1 − p)/p is the Bessel order at the hard edge. The Christoffel shift x·σ_{p,s,ℓ} =
   σ_{p,s+p,ℓ} transports the law and its rate, which reaches every s > 1. This holds uniformly in p, including
   p = 1 (window 1 < r < 3).
3. **p = 1 goes through the x-frame** (Plan 54, ROUTE2_xframe1). It is then literally the same frame as p > 1, with
   one lemma (reflection: D = e^{j(−n/z)}, no Binet cut) replacing another. The fold (Plan 53, ROUTE2_bnd) and the
   symmetric band-centre frame (Plan 50, ROUTE2_p1, and the WLXZ-based RH₁(r)) appear in one remark (§10 of the
   paper), with the honest statement that the fold shares the decisive α = 0 comparison step.
4. **Three geometries, one framework.** Everything except the outer scalar function F and a few angles is
   p-independent. The paper has one framework section (§5). One section (§6) treats the outer scalar in three short
   subsections. A table (§3.3 below) lists the ingredients that depend on the geometry. One "Frame Proposition"
   (end of §6) is the interface to the hard-edge section (§7).
5. **Order of operations (re-organisation R1).** Analytic factor, base window (Theorem 4) → shift (Theorem 3) →
   analytic factor, all s → smoothing reduction → arbitrary ℓ (Theorem 1). The repo's Corollary B_all applies the
   smoothing at the base exponent and shifts afterwards. The paper smooths last, which gives the cleaner rate
   O(1/n + ρ_ℓ(⌈n/M₀⌉)) with no "regular majorant". This is legitimate because the stability step (RedA(iii)) is
   REVIEWED for every p > 0 and s > 1. ROUTE2_plt1's Corollary B_{p<1} already uses this order, and so does Remark
   CT-px for p > 1. Flag it for the reviewer anyway (§7, item R10).
6. **Scope.** No smooth-ζ model (RH_ζ). No QLP, B-cond, T3-* or Theorem L transport results. No tilt law beyond an
   explicitly labelled conjecture in the closing section. The rough-weight counterexamples are announced only, as
   Paper 3. Lemma RL (law ⟺ arcsine limit) is not used and is mentioned in at most one sentence.
7. **Dependence on Paper 1:** only Paper 1 Theorem 1.3(i)–(ii) (the explicit μ*, its density and the equality
   U* = log c + p on the band). Optimality (iii) and the averaged law are not used in any proof. They appear only in
   the motivation.

---

## 1. Title, abstract, story

### 1.1 Title

**Recurrence coefficients of discrete measures with power-law atoms and slowly varying weights**

(This parallels Paper 1's title. The alternative "Pointwise asymptotics for compact Jacobi operators with
eigenvalues k^{−p}" was rejected because the eigenvalues are k^{−p} only when the measure is the spectral measure,
and the paper speaks about measures.)

### 1.2 Abstract (≤ 200 words)

> Let σ = Σ_{k≥1} k^{−s}ℓ(k) δ_{k^{−p}} with p > 0, s > 1 and ℓ slowly varying; its Jacobi matrix is a compact
> operator with eigenvalues k^{−p}. We prove that the recurrence coefficients satisfy n^p b_n → c(p) and
> n^p a_n → 2c(p), where c(p) = ¼(√π Γ(1/p + 1)/Γ(1/p + ½))^p is the constant of the constrained equilibrium problem
> solved in a companion paper. This holds for every p > 0, s > 1 and slowly varying sequence ℓ, including unbounded
> ones such as exp(√log k). If ℓ extends analytically to a sector, the error is O(1/n); for pure powers this gives
> n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n). The proof has three parts. A Riemann–Hilbert analysis of
> discrete orthogonal polynomials with nodes accumulating at a hard edge controls the non-analytic factor by a
> Conway–Deift comparison with a Bessel model instead of a local parametrix. A smoothing step reduces arbitrary to
> analytic slowly varying factors. The Christoffel transformation σ ↦ xσ shifts s by p and preserves the law with its
> rate. In a further paper we show that bounded but rough weights can destroy the pointwise law.

Drafters: keep the abstract formula-light in the LaTeX version (amsart abstracts render inline math fine; no
displays). Re-count words after edits.

### 1.3 The story (one paragraph, to be expanded into §1.1 of the paper)

A compact Jacobi operator is determined by its spectral measure. If the eigenvalues are k^{−p} and the spectral
weights are k^{−s}, how do the matrix entries behave? Paper 1 answers this on average. A constrained logarithmic
equilibrium problem, solved explicitly, gives log D_n and hence the double Cesàro means of log(n^p b_n). Its
constant c(p) is the value predicted by a pointwise "Law P": n^p b_n → c(p), n^p a_n → 2c(p). Averages do not give
pointwise limits: a Tauberian step needs regularity that the weights must supply. This paper shows that the
pointwise law is **stable under slowly varying perturbations of the weights**, including unbounded ones such as
exp(√log k), which the elementary perturbation arguments we know do not reach. Paper 3 shows that the law is **not stable
under bounded rough perturbations**: weights k^{−s}e^{f(k)} with |f| ≤ ε can destroy it, although Paper 1's
averaged law still holds for them. So regular variation of the weights is the natural condition, and the dichotomy
"slowly varying: yes; rough: no" is the conceptual message. Technically, the paper is a Riemann–Hilbert analysis of
discrete orthogonal polynomials on infinitely many nodes accumulating at a hard edge. Within the literature we read,
the only precedent is Wu–Lin–Xu–Zhao for the Tricomi–Carlitz polynomials. The slowly varying factor is not
analytic at the hard edge, so the standard local parametrix does not exist. It is replaced by the comparison
mechanism of Conway–Deift (their Theorem 4.7), extended here to a Bessel edge of any order |α| < 1 and to an
arbitrary slowly varying factor. Special cases connect to classical objects: (p, s) = (2, 2) is the Lommel family
(ν = 3/2, explicit coefficients), and σ_{a, 2a+b} is the measure whose Hankel determinants are det ζ(a(i+j)+b)
(Monien, Haynes–Zudilin, Paper 1).

---

## 2. Theorem statements for the introduction

The convention throughout is fixed in §4. P_n are monic orthogonal polynomials, and
x P_n = P_{n+1} + a_n P_n + b_n² P_{n−1} (n ≥ 0, b_0 := 0, b_n > 0), so b_n² = h_n/h_{n−1}, h_n := ∫P_n² dσ.
(Paper 1 writes a_{n+1} for our a_n; b_n agrees. Say so in a footnote in §2.)

Intro theorems are numbered Theorem 1–4 (a separate counter). Lemmas inside sections are numbered by section.

### Definitions needed before the statements (state them in §1.2 of the paper, briefly)

**Slow variation (sequence form).** A sequence ℓ: ℕ → (0, ∞) is *slowly varying* if, for every λ ≥ 1,

  osc_n(λ) := max{ |log ℓ(k) − log ℓ(n)| : k ∈ ℕ, n/λ ≤ k ≤ λn } → 0  (n → ∞).

(Source: PROOF.md §3.14, the "sequence form" of §3.8/§3.9(i). Equivalent formulation for the intro: ℓ(k)/ℓ(n) → 1
uniformly in k ∈ [n/λ, λn], for every fixed λ. λ = 2 suffices, by chaining (L0 remarks); state this as a remark in
§2, with the one-line proof.) Examples: (log(k+1))^β (β ∈ ℝ), exp((log k)^θ) (0 < θ < 1), exp(√log k ·
sin log log k); also, if ℓ is a measurable slowly varying function on [1, ∞) in Karamata's sense, its restriction
to ℕ is one, by the uniform convergence theorem. **Citation gate:** the Karamata remark needs BGT Thm 1.2.1, quoted
after it is read; otherwise drop the remark.

**Smoothing of ℓ.** Let L_ℓ: ℝ → ℝ be the piecewise-linear interpolant of the points (log k, log ℓ(k)), k ≥ 1,
extended by the constant log ℓ(1) on (−∞, 0]. Let G(y) := e^{−y²/2}/√(2π) and Λ_ℓ := L_ℓ * G, which is entire
(Lemma 4.1). Put

  ρ_ℓ(m) := sup_{k ≥ m} |log ℓ(k) − Λ_ℓ(log k)|  (→ 0 by Lemma 4.1).

**Analyticity hypothesis (A_ϑ)** (for ϑ > 0). ℓ(k) = exp Λ(log k) for all k ≥ 1, where for some c₀ > 0, Λ is
analytic on S_ϑ := {ξ ∈ ℂ : Re ξ ≥ −c₀, |Im ξ| ≤ ϑ}, real on S_ϑ ∩ ℝ, and bounded on S_ϑ ∩ {Re ξ ≤ 0}, and

  ε_Λ(T) := sup{ |Λ′(ξ)| : ξ ∈ S_ϑ, Re ξ ≥ T } → 0  (T → ∞).

The strip half-width used is **ϑ_p := π/p for p > 1 and ϑ_p := π/2 for 0 < p ≤ 1.** In words: ℓ extends to an
analytic function ℓ(t) = e^{Λ(log t)} on the sector |arg t| ≤ ϑ_p (near ∞, and bounded near t = 1) with
t ℓ′(t)/ℓ(t) → 0 there. Sources: (H_an) in ROUTE2 §2 (p > 1, with the Rule R F4 domain), (H_an^{x1}) in
ROUTE2_xframe1 §2 (p = 1) and (H_an^{<1}) in ROUTE2_plt1 §1 (p < 1). These are exactly the three REVIEWED
hypotheses. Do **not** unify them into a narrower strip (§7, R9). Examples (state only these):
ℓ(k) = exp √log(k + e) satisfies (A_{ϑ_p}) for every p > 0, since its branch points lie on |Im ξ| = π. The smoothed
Λ_ℓ of any slowly varying ℓ satisfies (A_ϑ) for every ϑ (Lemma 4.1(ii) together with the boundedness on Re ξ ≤ 0
from Rule R F4 of Plan 48). For p > 1 only, ROUTE2 §2 also lists Λ(ξ) = (log(e^ξ + e))^θ, θ < 1. A drafter who wants
this example for p ≤ 1 must check the strip π/2 explicitly (it holds for the same reason, but the repo does not say
so).

**Head margin.** M₀ = M₀(p) ≥ 4 is the least integer such that g_p⁺ ≥ 1 on (0, 2/M₀], where g_p⁺ is the exponent of
the saturation bound (Lemma 4.3). (Source: PROOF.md §3.14 notation line, §3.3.)

**Regular rate.** A sequence η_n > 0 is a *regular rate* if η_n is non-increasing, nη_n is non-decreasing, and
η_n → 0. Example: η_n = 1/n. (Source: ROUTE2_alpha §4.)

**Law P(c) at scale n^p, with rate η_n:** |n^p a_n − 2c| + |n^p b_n − c| = O(η_n).

### Theorem 1 (main theorem)

Let p > 0, s > 1, and let ℓ: ℕ → (0, ∞) be slowly varying. Let

  σ = σ_{p,s,ℓ} := Σ_{k≥1} k^{−s} ℓ(k) δ_{k^{−p}}.

Then

  (i)  n^p b_n → c(p) and n^p a_n → 2c(p);
  (ii) more precisely, |n^p b_n − c(p)| + |n^p a_n − 2c(p)| = O(1/n + ρ_ℓ(⌈n/M₀⌉));
  (iii) if ℓ satisfies (A_{ϑ_p}), then n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n).

Here c(p) = ¼(π/(2I(p)))^p = ¼(√π Γ(1/p + 1)/Γ(1/p + ½))^p, with I(p) = (√π/2)Γ(1/p + ½)/Γ(1/p + 1). For example,
c(1) = ½ and c(2) = π²/16.

Sources: THEOREMS.md §2.8 (the line "every p > 0, every s > 1 and every sequence-form slowly varying Ψ"). In detail:
PROOF.md §3.21 Cor. B_all (p > 1), §3.20 Cor. B_{p<1} (p < 1), §3.23 Cor. B_{p=1}^{all} (p = 1, with §3.19
B_{p=1}⁺ for non-integer r). Rate (ii) is the re-ordered form (§0 item 5). All are PROVED-mod-cite + REVIEWED.

Remarks to place right after Theorem 1:
- Σ_k k^{−s}ℓ(k) < ∞ by the Potter bounds (Lemma 2.1), so σ is a finite measure on (0, 1] with infinitely many atoms.
- No boundedness of ℓ is assumed. ℓ(k) = exp(√log k) and exp(√log k · sin log log k) are covered.
- (iii) does not identify the 1/n term. The relative effect of ℓ at order 1/n is open (§10 of the paper, the tilt
  conjecture).
- The averaged form (Paper 1, Corollary 1.2) holds for much rougher weights. Theorem 1 is the pointwise statement.

### Theorem 2 (pure powers, with rate)

For every p > 0 and s > 1 the measure σ_{p,s} := Σ_{k≥1} k^{−s} δ_{k^{−p}} satisfies

  n^p b_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

Equivalently, |n^p b_n − c(p)| + |n^p a_n − 2c(p)| = O(1/n).

Sources: THEOREMS.md H2 (RH₁(r), RH_p, RH_p seam; all PROVED-mod-cite + REVIEWED). The paper's proof is
Theorem 1(iii) with ℓ ≡ 1 (Λ ≡ 0 satisfies (A_ϑ) for every ϑ), i.e. Theorem 4 at Λ ≡ 0 plus Theorem 3. Both are
REVIEWED for Λ ≡ 0 (§0 item 1).

Remarks after Theorem 2:
- (Classical instances.) (p, s) = (2, 2): σ_{2,2} is, after scaling, the even part of the orthogonality measure of
  the Lommel polynomials with ν = 3/2, whose coefficients are explicit (novelty_G1RH §1.3). **Citation gate:** quote
  the explicit formula from a source that has been read (Van Assche's survey math/9510214 is the pointer) before
  using it. σ_{a,2a+b} (a > 0, 2a + b > 1) has moments ζ(a(i+j)+b) for its Hankel matrix (Paper 1, Corollary 1.4). So
  Theorem 2 gives n^a b_n = c(a)(1 + O(1/n)) for the recurrence coefficients behind det ζ(a(i+j)+b). At a = 1,
  b = 0 the Monien–Zagier numerical expansion (Monien arXiv:0901.1883) implies a stronger O(n^{−2}) behaviour
  numerically. Say "numerically", and cite Monien, quoting carefully (novelty_G1RH §1.2).
- (Numerically, the 1/n coefficients are −(s − 1)/2 for n^p b_n/c(p) and p/2 for a_n/(2b_n). This is NUMERICAL only
  (RH_px §0, check_fine.out), and is said only in §9 or §10 of the paper.)
- The constant c(p) is the saturation constant of the equilibrium measure (Paper 1 Thm 1.3(i)). Say in one sentence
  why it appears: the band of μ* is [0, 4c(p)], and the outer parametrix gives b_n ~ (band length)/4.

### Theorem 3 (Christoffel shift: law and rate)

Let σ be a positive Borel measure on [0, ∞) with infinite support and finite moments, let p > 0 and c > 0, and let
η_n be a regular rate. If

  |n^p a_n(σ) − 2c| + |n^p b_n(σ) − c| = O(η_n),

then the measure xσ (d(xσ) := x dσ(x)) satisfies the same estimate, with the same c and rate O(η_n). Without a rate:
if n^p a_n(σ) → 2c and n^p b_n(σ) → c, then the same holds for xσ. For x_k = k^{−p} one has exactly
x·σ_{p,s,ℓ} = σ_{p,s+p,ℓ}.

Sources: PROOF.md §3.21 (Theorems SH and SH-r, Lemmas CP, CT, CS, CS-r; all PROVED, self-contained, REVIEWED);
ROUTE2_alpha §§2–4. Second proof (Cholesky form): ROUTE2_plt1 §5.1 Lemma CT-Ch (REVIEWED). Credit (honest wording,
§6 style): the transfer formulas are classical (Christoffel/Darboux; LU ↦ UL, Derevyagin–Derkach §1; Bueno–Marcellán
2004, which must be read before it is cited). The no-rate statement follows from Dai–Piao–Qiao arXiv:2508.07653 Prop.
2.1 (chain sequences with a_n → ¼) together with those formulas. The rate transfer (Lemma 3.4 and the rate part of
Theorem 3) we have not found in the literature.

Remarks after Theorem 3:
- The parameter sequence converges only at rate O(√η_n) in general (sharp: ROUTE2_alpha §8(e), Rule R F4 of Plan
  52). Only its increments enter the transferred coefficients, so no rate is lost.
- Converse, without rate (PROOF.md §3.19 Lemma CT₁ "⟸" with Lemma D(b); REVIEWED): if xσ satisfies Law P(c), so
  does σ. Hence the law is insensitive to a point mass at 0. Credit: Dai–Piao–Qiao Prop. 2.1 covers every parameter
  sequence, so this direction is also a consequence of their proposition. State it as a remark, with that credit.

### Theorem 4 (the Riemann–Hilbert engine: analytic factor, base window)

Let p > 0 and 1 < s < 1 + 2p, i.e. α := (s − 1 − p)/p ∈ (−1, 1). Let ℓ₁ satisfy (A_{ϑ_p}). Then σ_{p,s,ℓ₁} satisfies

  n^p b_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

Sources: ROUTE2 §4.4 Theorem RII (p > 1); ROUTE2_xframe1 §4 Theorem RII_x1 (p = 1, 1 < r < 3, including r = 2,
α = 0); ROUTE2_plt1 §4.3 Theorem RII_{<1} (0 < p < 1). All PROVED-mod-cite + REVIEWED.

State Theorem 4 in §1.4 ("Strategy of the proof"), not in §1.2. It is the technical core, and a specialist wants to
see it stated separately. Immediately after it, state what is and is not proved about the slowly varying part:
relative to the comparison problem, the lip mismatch moves the first two moments at infinity by O(ε′_n/n). The
comparison problem itself depends on ℓ₁ at order 1/n, so **no claim** is made that b_n(σ_{p,s,ℓ₁})/b_n(σ_{p,s}) − 1 =
O(ε_Λ/n) (REVIEW_Plan48 F3).

### Corollaries

None in the intro. Theorem 2's zeta-Hankel remark is enough. Do **not** add a smooth-ζ corollary.

### Announcement of Paper 3 (in §1.3 "Context", no proof)

> In [Paper 3] we show that the regularity assumption cannot be replaced by boundedness. For every p > 0 and s > 1
> there is ε₀ > 0 such that, for every ε ∈ (0, ε₀], there are weights w_k = k^{−s}e^{f(k)} with |f(k)| ≤ ε for which
> n^p b_n does not converge, and weights of the same kind for which n^p a_n does not converge. Paper 1's averaged law
> holds for all of them.

Source: THEOREMS.md H4 Theorem R (b-law) and §2.6 Theorem Ra (a-law). Both are PROVED-mod-cite, with the pure-power
input that Theorem 2 of this paper supplies. Do not state the constants (η, ε₀ = η/16, η_a, …). Do not claim "the
same weights break both".

---

## 3. Architecture of the proof

### 3.1 Dependency diagram (reproduce as Figure 1, TikZ)

```
 Paper 1, Thm 1.3(i)-(ii)            WLXZ v1 (interpolation problem,          KMVV §6 (Bessel model,
 (mu*, U* = log c + p on [0,4c])      transformations, Airy parametrix)         angle freedom); DLMF
            |                                   |                                      |
            v                                   v                                      |
  §5  Common frame (all p > 0): rescaling, index function t(z), g, phi, signs,         |
      lenses, saturated region, top end                                                 |
            |                                                                           |
            v                                                                           |
  §6  Outer scalar F and band weight W0 in three geometries                            |
      [p > 1: Binet cut]   [p = 1: reflection]   [p < 1: seams]                         |
      ==> Frame Proposition 6.9 (interface)                                             |
            |                                                                           v
            +-------------------> §7 Hard edge: comparison with a Bessel model of order alpha
                                     (W~ := D_W; lip mismatch o(1) with no rate; uniform
                                     resolvent for |alpha| < 1 [App. A, B]; C-D Thm 4.4 +
                                     Neumann series; Bessel localization gives O(eps'/n))
                                              |
                                              v
                              §8 Extraction ==> THEOREM 4 (analytic l1, 1 < s < 1 + 2p, O(1/n))
                                              |
                 §3 THEOREM 3 (shift x.sigma_s = sigma_{s+p}, rate kept) --+
                                              |                           |
                                              v                           |
                          analytic l1, every s > 1, O(1/n)  ==>  THEOREM 2 (l = 1)
                                              |
                 §4 Gaussian smoothing (Lemma 4.1) + stability under l/l1 -> 1 (Prop. 4.5)
                                              |
                                              v
                                          THEOREM 1
```

The paper is ordered so that the reader meets the soft parts first. §3 (shift) and §4 (smoothing) are elementary and
self-contained. They reduce Theorem 1 to Theorem 4, and §4 ends with "Proof of Theorems 1 and 2 assuming
Theorem 4". §§5–8 then prove Theorem 4. This front-loads the logic and lets an RH specialist jump to §5.

### 3.2 Main text vs appendices

Main text:
- the statements and proofs of §§3–4 (elementary, short);
- the full construction of the frame (§5);
- the three outer scalars (§6), with the shorter proofs in full and the routine bookkeeping (Stirling bounds,
  where the weight is evaluated) as lemmas with compact proofs;
- the comparison argument of §7 at the level of: parametrix, mismatch lemma, statement of the uniform resolvent bound
  with a proof sketch, Neumann step, Bessel-localization estimate;
- extraction (§8).

Appendices:
- **A.** Mellin-type L² bounds on a star of arcs: the power-weighted Cauchy operator (|β| < ½) and the
  log-commutator (needed at α = 0).
- **B.** Proof of the uniform resolvent bound for the comparison problem: (a) the reduction to an inhomogeneous RHP;
  (b) membership in ∂C(L²) for every |α| < 1; (c) partition; (d) the hard-edge block; (e) the Airy block.
- **C.** The a priori bound at the hard edge (the "(Y4)" estimate, with the Potter loss) and the identification
  Q ∈ I + ∂C(L²(Σ)).
- (Optional) **D.** Proofs of the first-variation formulas (Lemma 4.2), if they are not taken from a cited source
  (§7, R7).

### 3.3 The three geometries: what depends on p (reproduce as Table 1 in §5)

Present the RH analysis once, for all p > 0. Each item in this table gets one short subsection or one row of a
lemma. Drafters may not repeat the common steps three times.

| Ingredient | p > 1 | p = 1 | 0 < p < 1 | Repo source |
|---|---|---|---|---|
| arg of t(z) = n z^{−1/p} on ℂ∖(−∞,0] | (−π/p, π/p) | (−π, π) (open) | (−π/p, π/p) ⊋ (−π, π): poles of Γ enter | RH_px L1.1; xframe §1 item 1; RH_plt1 §1 |
| where D̃ = e^{−j(t)} is used | slit plane | only \|arg z\| ≤ π/3 + π/24 | only the inner sector S_in = {\|arg z\| < πp/2} | RH_px §3; xframe §1; RH_plt1b §1 |
| outer scalar F | D·B·(4c − z)^{−1/2}, with the Binet-cut scalar B | D·(4c − z)^{−1/2}, with D = e^{j(−n/z)} (reflection; no cut on (−∞, 0), B ≡ 1) | seam construction: D·B_in·(4c − z)^{−1/2}e^{χ} in S_in, B_out·(4c − z)^{−1/2}e^{χ} in S_out; seams at arg z = ±πp/2 | RH_px L3.1–3.3; xframe L X1; RH_plt1b §1 |
| band factor H_n near 0 | Hölder-ν_p, ν_p = min(1/p, ½) (via the Hölder endpoint lemma) | C^∞, N-uniform | \|log H_n(z) − log H_n(0)\| ≤ C\|z\|(1 + log(1/\|z\|)) (corner lemma for χ) | RH_px L3.4 + consequence; xframe §2 row L3.4; ROUTE2_plt1 L X0, LW1′_{<1} |
| g(z) − log z at ∞ | ≍ z^{−1/p} | O(\|z\|^{−1}log\|z\|) (the first moment of μ* diverges) | ≍ 1/z | RH_px L3.5; REVIEW_Plan54 F1; RH_plt1 amendments |
| lips at the hard edge | ±π/3 (Bessel rays at ±2π/3) | ±π/3 | ±πp/4 (Bessel rays at ±(π − πp/4), KMVV angle freedom) | RH_px L4.1, L4.3; RH_plt1b §2 |
| super-small lip entries | exp(−c n \|z\|^{−1/p}) | exp(−c n/\|z\|) | exp(−2π sin(π/4)·n\|z\|^{−1/p}) | RH_px L4.3; xframe §2; ROUTE2_plt1 §3.1 (REVIEW_Plan51 F4 typo) |
| strip for ℓ₁: ϑ_p | π/p | π/2 | π/2 | ROUTE2 §2; xframe §2; ROUTE2_plt1 L S_w |
| ε′_n := n^{−2ν_p}log n + ε_Λ(T_n) | ν_p = min(1/p, ½) | ν_p = ½ | ν_p = ½ | ROUTE2 L LW1′; xframe L LW1-x1; ROUTE2_plt1 L LW1′_{<1} |
| quotient (glued) hard-edge parametrix | works for pure powers (not used) | **fails** even for pure powers (Lemma X2) | works with a seam glue (not used) | RH_px §4.1; xframe L X2; RH_plt1b §2 |

The common output of §§5–6 is the **Frame Proposition** (Proposition 6.9 below), the interface to §7.

---

## 4. Notation table

One symbol, one meaning, across the whole paper. The right column records the repo clash that is being resolved, so
that a drafter reading a repo file can translate. Symbols used only inside one proof may be introduced locally, but
must not reuse a symbol from this table.

### 4.1 Measures, coefficients, constants

| Symbol | Meaning | Repo clash resolved |
|---|---|---|
| p > 0 | node exponent, x_k = k^{−p} | — |
| s > 1 | weight exponent (p = 1: still s, not r) | repo writes r at p = 1, and σ for s in QLP |
| ℓ | slowly varying sequence ℕ → (0, ∞) | repo Ψ (clashes with the Bessel model Ψ) |
| ℓ₁ | analytic factor ℓ₁(t) = e^{Λ(log t)} | repo Ψ₁ |
| Λ, Λ_ℓ | the analytic log-factor; Λ_ℓ = L_ℓ * G is the Gaussian smoothing | repo L₁ |
| L_ℓ | piecewise-linear interpolant of (log k, log ℓ(k)) | repo L |
| G | standard Gaussian density | repo φ (clashes with the phase φ) |
| osc_n(λ) | slow-variation modulus | repo δ_n(λ) (clashes with the disc radius δ) |
| ρ_ℓ(m) | smoothing error sup_{k≥m}\|log ℓ(k) − Λ_ℓ(log k)\| | repo ρ(m) |
| ε_Λ(T) | sup of \|Λ′\| on S_ϑ ∩ {Re ξ ≥ T} | repo ε₁(T) |
| ε′_n | lip-mismatch size n^{−2ν_p}log n + ε_Λ(T_n) | repo ε′_N |
| ξ | log variable ξ = log t | repo u (clashes with the u_n of §3) |
| S_ϑ, ϑ_p | strip and its half-width | repo Σ_p, Σ_{1/2}, Σ_{x1} (Σ is the contour) |
| x_k = k^{−p}, w_k = k^{−s}ℓ(k) | atoms and masses | — |
| σ, σ_{p,s,ℓ}, σ_{p,s} | the measure (Paper 1's letter) | σ₃ is always written with its subscript |
| P_n, h_n | monic OPs and their norms ∫P_n²dσ | RH_px π_n |
| a_n, b_n | Jacobi coefficients: xP_n = P_{n+1} + a_nP_n + b_n²P_{n−1} | repo α_n, β_n = b_n² (ROUTE2_alpha), β_n = n^pb_n/c (G1); Paper 1 a_{n+1} |
| c = c(p), I(p) | as in Paper 1 (1.2) | c(p) vs the generic constant C: use C, C′ for generic constants, never c |
| μ* | Paper 1's equilibrium measure in the x-variable | repo μ_n (spectral weights) → m_n |
| ψ* | density dμ*/dx | repo ψ |
| λ_p(x) | node density (1/p)x^{−1−1/p} | repo ρ (clashes with ρ_ℓ) and Paper 1's σ(dx) |
| U* | ∫log\|x − y\|dμ*(y) (= log c + p on (0, 4c]) | — |
| γ_p | log c(p) + p | repo l = 2(log c + p) (clashes with ℓ) |
| α | hard-edge Bessel order (s − 1 − p)/p | repo α_x; never α_n |
| η_n | a regular rate | repo r_n (clashes with the ratio r_n) |
| M₀ = M₀(p) | head margin (g_p⁺ ≥ 1 on (0, 2/M₀]) | — |
| n | degree and coefficient index; **no N** anywhere | repo N in all RH files |

### 4.2 Christoffel section (§3)

| Symbol | Meaning | Repo clash |
|---|---|---|
| xσ | the measure x dσ(x) | — |
| u_n | −P_{n+1}(0)/P_n(0) > 0 (diagonal of U in J = LU) | repo g_n (clashes with g) |
| l_n | b_n²/u_{n−1} (subdiagonal of L), l_0 := 0 | repo h_n (clashes with h_n norms) |
| ã_n, b̃_n | coefficients of xσ | — |
| κ_n | ((n − 1)/n)^p | — |
| (Lemma CT in Cholesky form, if used: L = lower bidiagonal factor; write its entries λ_j, μ_j only locally, or omit the Cholesky proof) | | repo l_j, m_j |

### 4.3 Smoothing reduction (§4)

| Symbol | Meaning | Repo clash |
|---|---|---|
| ψ := ℓ/ℓ₁ | ratio, ψ(k) → 1 | — |
| τ ∈ [0, 1] | path parameter, w^{(τ)} := w^{(0)}ψ^τ | repo t (clashes with the index function t(z)) |
| m_n(k) | spectral weights w_kP_n(x_k)²/h_n (a probability vector in k) | repo μ_n(k) (clashes with μ*) |
| K_n(k) | Σ_{j<n} m_j(k) (diagonal Christoffel–Darboux sum) | repo ρ_n(k) |
| q_n(k) | w_k^{1/2}P_n(x_k)/h_n^{1/2} (so m_n = q_n²) | — |
| g_p, g_p⁺ | saturation exponents (Lemma 4.3) | — |

### 4.4 Riemann–Hilbert sections (§§5–8 and the appendices)

| Symbol | Meaning | Repo clash |
|---|---|---|
| Y | interpolation (discrete) RH problem of degree n | — |
| U | n^{pnσ₃}Y(z/n^p); nodes X_k = (n/k)^p, top node X₁ = n^p | — |
| t(z) | index function n z^{−1/p} (t(X_k) = k) | — |
| θ(z), Π(z) | πt(z); sin θ/θ′ | — |
| w(z) | n^p t(z)^{−s}ℓ₁(t(z)) (residue weight) | — |
| W(x) | 2iθ′(x)w(x) on the band | — |
| j(t) | Binet's function: LnΓ(t) − (t − ½)ln t + t − ½ln(2π) | repo μ(t) (clashes with μ*); RH_plt1b's sign slip (REVIEW_Plan51 F2): state the sign once |
| D̃, D | e^{−j(t)}; D̃/(1 − e^{∓2iθ}) in ℂ± | — |
| B | Binet-cut scalar (p > 1 only) | — |
| B_in, B_out, χ, χ_± | seam factors, seam scalar and its densities (p < 1 only) | repo X, L± (X clashes; L clashes with L_ℓ) |
| F, F̃ | outer and lens scalars | — |
| ϑ_lip, ϑ_seam | lip angle (π/3, or πp/4 for p < 1); seam angle πp/2 | repo θ_L, θ_s (θ = πt) |
| g, φ, φ̃ | g-function of μ*; φ := γ_p − g; φ̃ := φ ± iθ/n | — |
| R, T, S, V | transformations: unlensing poles → normalization → lens opening → outer scalar | repo uses Q for the lens-opened matrix: rename it S |
| Q, Q̃ | the C–D frame D_∞^{−σ₃}VD_W^{σ₃} and its comparison problem | — |
| W₀ | band weight W·(4c − x)/(D̃B)² (resp. the seam analogue) = C_n x^α(4c − x)H_n(x)r_n(x) | repo w₀ |
| H_n | the node-data band factor (Hölder at 0) | repo h_N |
| r_n(z) | ℓ₁(n z^{−1/p})/ℓ₁(n) | repo q_N |
| D_W, D_∞ | Szegő function of W₀ on [0, 4c]; D_W(∞) | repo D_w, D_∞ |
| P^∞, P^∞_0 | global parametrix D_∞^{σ₃}P^∞_0D_W^{−σ₃}; P^∞_0 built from a(z) = ((z − 4c)/z)^{1/4} | repo N, N₀ (N is retired) |
| f | conformal map at 0, f = (φ ± iπ)²/4, f(0) = 0, f′(0) < 0 | — |
| Ψ_α | KMVV Bessel model of order α | — |
| M | (1/√2)[[1, i], [i, 1]] (KMVV (6.53), endpoint −1) | — |
| E_n | hard-edge prefactor D_∞^{σ₃}P^∞_0 M f^{σ₃/4}(2πn)^{σ₃/2} | repo Ẽ_N |
| P̃₀, P_r | comparison parametrix at 0; Airy parametrix at 4c | — |
| 𝒵̃ | small-norm matrix of the comparison problem | — |
| Σ, v, ṽ | contour of Q; jumps of Q and Q̃ | — |
| C_±, C_v | Cauchy boundary operators; C_v f := C_−(f(v − I)) | — |
| c_± | e^{∓iπα} | — |
| d_n(z) | lip mismatch (D_W²/W₀ − c_±)e^{2nφ} | repo δ_N(z) |
| ν_p | Hölder exponent min(1/p, ½) (½ for p ≤ 1) | repo ν |
| β | exponent in the power-weighted Cauchy lemma, \|β\| < ½ (β = ±α/2) | repo a |
| U(z₀, r) | open disc; δ (disc radius at 0), ε (disc radius at 4c) | — |
| a(Q) | (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂ (extraction functional) | — |
| Q₁, Q₂ | coefficients of Q = I + Q₁/z + Q₂/z² + … | — |

### 4.5 Words

- "Hard edge" means x = 0 (Bessel). "Soft edge" means x = 4c (Airy). "Band" means (0, 4c). "Saturated region" means
  (4c, n^p).
- "Law P" is **not** used in the paper. Write "the pointwise law (1.x)", referring to the display in Theorem 1(i).
  A name is permissible only if it is defined once ("we call (1.3) the power law for the recurrence
  coefficients").
- "Riemann–Hilbert" is written in full at first use, then "RH problem". (In the repo "RH" in file names means
  Riemann–Hilbert. The Riemann hypothesis plays no role and is never mentioned.)

---

## 5. Section-by-section plan

Page estimates assume amsart 11pt with Paper 1's geometry. Total ≈ 62 pp (main text ≈ 48, appendices ≈ 14).

### §1 Introduction (≈ 7 pp)

**Purpose.** State the results, explain why the pointwise law is subtle (averages vs pointwise; rough weights), and
give a road map an RH specialist can follow.

- §1.1 *Setting.* Open with the inverse-spectral question in one paragraph (the story, §1.3 above). Introduce σ,
  Jacobi coefficients, c(p), and Paper 1's averaged law (quoted, with its exact hypothesis). End with the question:
  does n^p b_n converge?
- §1.2 *Results.* Define slow variation (sequence form), the smoothing error ρ_ℓ and (A_ϑ), then Theorem 1,
  Theorem 2, Theorem 3, each followed by its 2–4 remarks (§2 above).
- §1.3 *Context.* Use the honest wording of §6.6 throughout.
  - (a) Averaged vs pointwise: Paper 1; Tauberian obstruction.
  - (b) RH for discrete OPs: Baik–Kriecherbauer–McLaughlin–Miller (finite node sets, analytic data); WLXZ (infinite
    nodes accumulating at a point, Tricomi–Carlitz). Dai–Yao 2021 state that WLXZ is the only such analysis; quote
    them only after re-reading.
  - (c) Non-analytic weights by RH: Conway–Deift (log weight, comparison, Thm 4.7: **credit the mechanism
    explicitly**); Deift–Piorkowski (note on exponent 1; consistent with our restriction |α| < 1); Piorkowski 2019;
    Trogdon 2026; McLaughlin–Miller; Deift–Its–Krasovsky §6.2 (analytic approximation).
  - (d) Non-RH o(1) recurrence laws: Levin–Lubinsky (exponential weights). The framing as a "Freud-type theorem for
    compact Jacobi operators" may be mentioned. Lubinsky–Mhaskar–Saff must be read before it is cited.
  - (e) Special cases: Lommel (2, 2); Monien/Haynes–Zudilin (zeta Hankel); Tricomi–Carlitz (p = 1 in the squared
    variable).
  - (f) The Paper 3 announcement.
- §1.4 *Strategy of the proof.* State Theorem 4 here, then explain the three steps in prose (≈ 1.5 pp; the order of
  §3.1).
  - The window |α| < 1 and the shift.
  - Why the slowly varying factor is not analytic at the hard edge, and why a quotient (small-norm) argument
    fails: continuing r_n^{1/2} across (−δ, 0) produces a jump 1 + O(ε_Λ) with no rate. The Bessel scale amplifies it
    to O(nε_Λ). Source: ROUTE2 §2, last paragraph.
  - The C–D idea: build the Bessel parametrix with W̃ := D_W. Nothing then jumps on (−δ, 0). The price is a lip
    mismatch that is o(1) in sup norm with no rate, which suffices for the Neumann series. Bessel localization gives
    the 1/n.
  - What is new relative to C–D: an arbitrary slowly varying factor; any Bessel order |α| < 1; a comparison model
    that is an explicit parametrix rather than a second orthogonality problem; a discrete problem with nodes
    accumulating at the hard edge.
- §1.5 *Organisation and notation.* Point to the notation of §2 and the dependency figure.

Cited, not proved: Paper 1 Theorem 1.1/Corollary 1.2 (context only). Paper 3 (announcement).
Intuition paragraph: the story. Re-organisation: none. This is new writing.

### §2 Preliminaries (≈ 5 pp)

**Purpose.** Fix conventions, prove the two elementary facts about slow variation, quote Paper 1's input, and state
every external tool precisely.

- §2.1 Orthogonal polynomials and Jacobi coefficients (convention; Paper 1 shift footnote). Heine's formula, quoted
  from Paper 1 Lemma 2.1, is used only in §4.
- §2.2 Slow variation. **Lemma 2.1 (chaining and Potter bounds).** (i) |log ℓ(k) − log ℓ(n)| ≤ ε_n(1 + log₂(k/n))
  for k ≥ n, with ε_n := sup_{m≥n} osc_m(2) → 0. (ii) For every η > 0, e^{−A_η}k^{−η} ≤ ℓ(k) ≤ e^{A_η}k^η. Source:
  PROOF.md §3.14 Lemma L0 (PROVED, REVIEWED). Full proof (½ p). Remark: osc_n(2) → 0 implies osc_n(λ) → 0 for every
  λ (L0 remarks).
- §2.3 Regular rates (definition; every rate ρ_n ≥ 1/n with ρ_n ↓ 0 has the regular majorant max_{m≤n}(mρ_m)/n).
  Source: ROUTE2_alpha §4 (PROVED). Needed only in §3.
- §2.4 The equilibrium measure (input from Paper 1). State Paper 1 Theorem 1.3(i)–(ii) as Proposition 2.2: μ*, its
  density ψ* = λ_p · ℐ_{min(1, x/4c)}(1/p + ½, ½) (regularised incomplete beta), saturation ψ* = λ_p on [4c, ∞), ψ* <
  λ_p on (0, 4c), U* = γ_p on (0, 4c], U* ≥ γ_p on (0, ∞). Add: ψ*(x) ~ C x^{−1/2} at 0 (hard edge). Source: G2
  PROOF.md B*(i)–(ii) (citation-free); RH_px §2 "Input from G2". Say explicitly that optimality (Paper 1 Thm
  1.3(iii)) is not used.
- §2.5 **Tools.** Each item is quoted with its hypotheses, from the source files listed. It must be stated precisely
  enough that a reader can check our hypotheses. This subsection is ≈ 2 pp.
  - T1 (WLXZ v1, arXiv:1410.3948v1; Anal. Appl. 14 (2016)): the discrete interpolation problem and its solution by
    the OPs (their Theorem 2.3, attributed by them to Fokas–Its–Kitaev); the transformation patterns (3.10)–(3.15),
    (4.1), (4.12)–(4.13) (note the △ superscripts in (4.12): REVIEW_Plan53 Rule C item), (5.1); the Airy
    construction §6.1, (6.1)–(6.21). Quotes: RH/CITATIONS.md (WLXZ-v1) and its additional quotes; Plan 53 parity
    quotes (2.14), (3.1), (3.4) if used.
  - T2 (KMVV, arXiv:math/0111252v2 = Adv. Math. 188 (2004)): the Bessel RHP (6.16)–(6.21), the model (6.23)–(6.25),
    Theorem 6.3, large-ζ behaviour (6.28), the left-endpoint construction (6.42)–(6.53) (orientation reversal,
    σ₃-conjugation (6.51), the matrix in (6.53)), and the angle-freedom sentence after (6.21). Quotes: RH/CITATIONS.md
    (KMVV), (KMVV, additional quotes …), (KMVV, angle freedom).
  - T3 (Conway–Deift, arXiv:1711.01590v4 = SIGMA 14 (2018) 056): the Carleson boundedness statement of §4.1; the
    definition of ∂C(L^p); Theorem 4.4 (quoted in full); the identity µ = (1 − C_v)^{−1}I and the formula X =
    I + C(µ(v − I)) of §4.2; the Neumann-series argument of the proof of Theorem 4.7; formula (4.14) of Proposition
    4.9. State that we do **not** use their Theorem 4.5 (Legendre-specific) and that we re-prove the easy half of their
    Proposition 4.6 (App. B(a)). Quotes: RH/CITATIONS.md (C–D).
  - T4 (DLMF): 1.13.4 and 10.28.2 (Wronskian; det Ψ_α = 1), 1.14.32, 1.14.38–40 (Mellin–Parseval), 5.5.1, 5.5.3,
    5.11.1 with the §5.11(ii) remainder bound, 5.12.1, 5.12.3, 10.25.2 (with the principal-branch sentence of
    §10.25(ii)), 10.27.3–4, 10.31.2. Quotes: RH/CITATIONS.md (DLMF), (DLMF-2), (DLMF-4), (DLMF-5), (DLMF-5.11, Plan 51),
    (DLMF-5.5/5.11, Plan 54).

Cited vs proved: Lemma 2.1 proved; Proposition 2.2 cited (Paper 1); T1–T4 cited.
Intuition paragraph: "Two facts about slowly varying sequences are used repeatedly: they are locally almost
constant on dyadic scales, and they grow slower than any power."

### §3 The Christoffel shift (≈ 4 pp)

**Purpose.** Prove Theorem 3. This elementary section also gets the reader used to the conventions.

Opening paragraph: multiplying σ_{p,s,ℓ} by x shifts s by p exactly. The Jacobi matrix of xσ is the "UL" product of
the "LU" factors of the Jacobi matrix of σ. The factors are determined by the law alone, through a parabolic fixed
point, so no information about P_n(0) beyond positivity is needed. That last sentence is the conceptual point; say
it before computing.

Statements:
- Lemma 3.1 (zeros in (0, ∞), (−1)^nP_n(0) > 0). Source: ROUTE2_alpha §2.1 Lemma CP (PROVED). Full proof (5 lines).
- Lemma 3.2 (Christoffel transfer formulas): a_n = u_n + l_n, b_n² = u_{n−1}l_n; ã_n = u_n + l_{n+1},
  b̃_n² = u_n l_n. Source: §2.2 Lemma CT (PROVED, classical; novelty not claimed). Proof in full (½ p) or cite a source
  that has been read (Derevyagin–Derkach §1) and add the short proof for completeness. Prefer the short proof.
- Lemma 3.3 (the chain sequence converges): if n^pa_n → 2c and n^pb_n → c (c > 0), then n^pu_n → c and n^pl_n → c.
  Source: §3.1 Lemma CS. Credit Dai–Piao–Qiao Prop. 2.1 (the "chain-sequence form" sentence of §3.1), and keep the
  self-contained proof (½ p). It shows why: F(G) = 2c − c²/G has a double fixed point.
- Lemma 3.4 (rate for the chain sequence): with a regular rate η_n, |n^pu_n − c| = O(√η_n) and
  |n^pu_n − (n − 1)^pu_{n−1}| = O(η_n). Source: §4.1 Lemma CS-r (PROVED). Full proof (1 p).
- Proof of Theorem 3. Source: §3.2 Theorem SH, §4.2 Theorem SH-r.
- Remark 3.5 (sharpness of O(√η_n); only increments enter). Source: ROUTE2_alpha §8(e).
- Remark 3.6 (converse, mass at 0; credit DPQ). Source: PROOF.md §3.19 CT₁ "⟸", Lemma D(b); REVIEW_Plan50 F5, F9.
- Remark 3.7 (the 1/n coefficient shifts by −p/2 if and only if n(n^pu_n − (n − 1)^pu_{n−1}) → 0). Source: Remark
  SH-1/n. The identity and the equivalence are proved; the hypothesis is numerical only. Optional; keep to 3 lines, or
  move it to §10.

Cited vs proved: all proved. Credit as in §2 above.
Re-organisation: the repo has two proofs, LU (Plan 52) and Cholesky (Plan 51). **Use the LU proof (Plan 52) only.**
Mention the Cholesky form in one sentence. Rename g_n, h_n → u_n, l_n.

### §4 From analytic to arbitrary slowly varying factors (≈ 6 pp)

**Purpose.** Show that the law for ℓ₁ = e^{Λ_ℓ(log ·)} implies the law for ℓ, with an additive error
O(ρ_ℓ(⌈n/M₀⌉)). Then finish the proofs of Theorems 1 and 2, assuming Theorem 4.

Opening paragraph (motivation): a slowly varying sequence is "almost analytic". Gaussian smoothing in the log
variable produces an entire Λ_ℓ whose derivatives tend to 0 in every horizontal strip, and which differs from log ℓ
by o(1) at the integers. A multiplicative perturbation ψ = ℓ/ℓ₁ → 1 changes log b_n² by at most the sup of |log ψ|
over the bulk of the spectral weight. The only danger is the head k < n/M₀, where the weights are exponentially
saturated. Then one paragraph on why one cannot transport directly from the pure power: ℓ itself is unbounded and
not close to 1, and a transport from k^{−s} would need hard-edge localization of the spectral weights at the 1/n
level (outline_B_sv §4). Keep it heuristic and short, or omit it.

Statements:
- Lemma 4.1 (Gaussian smoothing). (o) Λ_ℓ is entire; (i) Λ_ℓ(log k) − log ℓ(k) → 0; (ii) for every ϑ ≥ 0 and j ≥ 0,
  sup_{|Im ξ|≤ϑ}|Λ_ℓ^{(j)}(ξ) − δ_{j0}Λ_ℓ(Re ξ)| → 0 as Re ξ → +∞, and Λ_ℓ is bounded on {Re ξ ≤ 0, |Im ξ| ≤ ϑ}.
  Hence Λ_ℓ satisfies (A_ϑ) for every ϑ. Source: ROUTE2 §1 Lemma RedA (o)–(ii) (PROVED, REVIEWED); REVIEW_Plan48
  check 1 and F4. Full proof (1 p). Credit: "This is a strip-uniform form of the smooth variation theorem [BGT
  Thm 1.8.2; Vuilleumier]". **Citation gate:** BGT §1.8 and Vuilleumier 1976 must be read before this sentence is
  written. If they are not read, write "Smoothing statements of this kind are familiar from the theory of regular
  variation; we include the short proof."
- Lemma 4.2 (first variation). For w^{(τ)} = w^{(0)}e^{τf} with f bounded: (d/dτ)log b_n² = ⟨f, m_n − m_{n−1}⟩ and
  (d/dτ)a_n = ⟨(x − a_n)f, m_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩. Source: PROOF.md §3.2 Lemma FV, §3.5 Lemma FVa (PROVED,
  standard, REVIEWED). Proof: FV from Heine (Paper 1 Lemma 2.1) in 6 lines. FVa uses the two-point function of the
  Heine ensemble (determinantal; from the Gram–Sylvester argument of G3prime PROOF.md Lemma H) plus
  Christoffel–Darboux. That is about 1 p in App. D, or cite a source that has been read (Fischer, Z. Anal. Anwend. 17
  (1998) Lemmas 4–5, pointer only; §7 R7). Only bounded f is needed here, so do **not** import FV⁺.
- Lemma 4.3 (saturation of the head). For 1 ≤ k < n and θ = k/n: 1 − K_n(k) ≤ (W/w_k)((n+1)/k)^{2(1−p)₊}e^{−2n
  g_p⁺(θ)}, with W := Σw. Source: PROOF.md §3.1 Lemma Sat_p and §3.3 Lemma Sat_p⁺; G3prime PROOF.md §5.2 Lemmas H and
  Sat. The proof is elementary (Christoffel's variational formula plus a Lagrange test polynomial; 1 p). Write it
  directly; do not chain through three repo lemmas.
- Lemma 4.4 (a priori size): a_n^{(τ)}, b_n^{(τ)} ≤ 2M₀^p(n − 1)^{−p} for n ≥ n₀, uniformly in τ. Source: PROOF.md
  §3.5 T3a step 1; B-cond step 7. Proof 5 lines.
- Proposition 4.5 (stability under ψ → 1). Let p > 0, s > 1, ℓ₁ = e^{Λ_ℓ(log ·)} and ψ := ℓ/ℓ₁. Then
  |log b_n²(σ_{p,s,ℓ}) − log b_n²(σ_{p,s,ℓ₁})| ≤ 2ρ_ℓ(⌈n/M₀⌉) + O(n^{O(1)}e^{−2(n−1)}) and
  n^p|a_n(σ_{p,s,ℓ}) − a_n(σ_{p,s,ℓ₁})| ≤ 6·2^pM₀^p ρ_ℓ(⌈n/M₀⌉) + O(n^{O(1)}e^{−2(n−1)}). Source: ROUTE2 §1 RedA(iii)
  (PROVED, REVIEWED; REVIEW_Plan48 check 2). Proof (1 p): path w^{(τ)} = w(ℓ₁)ψ^τ; Lemma 4.2; head by Lemma 4.3 with
  W/w_k ≤ C_η k^{s+η} (Potter for ℓ₁ = ℓ/ψ); bulk |log ψ| ≤ ρ_ℓ(⌈n/M₀⌉).
- §4.4 Proofs of Theorems 1 and 2 assuming Theorem 4.
  - Analytic ℓ₁, all s > 1: write s = s₀ + mp with s₀ ∈ (1, 1 + 2p). Theorem 4 at s₀, then Theorem 3 m times with
    η_n = 1/n.
  - Theorem 1(iii): that statement with ℓ₁ = ℓ.
  - Theorem 2: ℓ ≡ 1.
  - Theorem 1(ii): apply Proposition 4.5 at s with ℓ₁ = e^{Λ_ℓ(log ·)} (Lemma 4.1 gives (A_{ϑ_p})).
  - (i) follows.
  - Remark 4.6 (robustness of the base window): for s > 1 + p/2 one may choose s₀ ∈ (1 + p/2, 1 + 3p/2], so only
    |α| ≤ ½ is used, plus the α = 0 case, which cannot be avoided. Source: ROUTE2_alpha §5 Remarks (Rule R F2 of
    Plan 52).

Cited vs proved: all proved (FVa possibly cited). Re-organisation: **R1** (the order of operations, §0 item 5); **R6**
(write the head bound directly); **R7** (FVa: decide cite-or-appendix).

### §5 The Riemann–Hilbert problem and the common frame (≈ 8 pp)

**Purpose.** Set up the discrete RH problem for σ_{p,s,ℓ₁} (1 < s < 1 + 2p) and carry out every step that does not
depend on the geometry: rescaling, equilibrium g-function, unlensing the poles, the saturated region, the lenses, and
the sign structure.

Opening paragraph: the discrete measure is encoded by a meromorphic interpolation problem. After rescaling by n^p
the nodes fill (0, n^p], and the equilibrium measure μ* of Paper 1 governs the n-th root behaviour. On (0, 4c) the
polynomials oscillate (the band). On (4c, n^p) the nodes are saturated, and the problem reduces to an interpolation
with exponentially small corrections. Near 0 the band meets infinitely many nodes. Name the reference problem: the
frame is WLXZ's, in the one-sided x-variable.

Statements (all from RH_px §§1–3, with the ROUTE2 §2 table changes; each says "for every p > 0" when xframe §2 and the
RH_plt1 amendments confirm p-independence):
- Lemma 5.1 (the interpolation problem and its solution by the OPs). Source: RH_px §1 (rescaling, residue
  convention); WLXZ Thm 2.3 (T1). Weight w(z) = n^p t^{−s}ℓ₁(t), divided by ℓ₁(n) (harmless; ROUTE2 §2).
- Lemma 5.2 (band weight): |W(x)| = (2π/p)n^{1+p−s}x^α|r_n(x)| up to the constant ℓ₁(n), with arg W = −π/2. The hard
  edge has Bessel order α. Source: RH_px Lemma 1.2; ROUTE2 §2 table; xframe §2 row L1.2.
- Lemma 5.3 (g-function, φ, φ̃): (i) φ₊ + φ₋ = 0 on (0, 4c); (ii) φ̃ has no jump on (4c, ∞); (iii) Re φ̃ < 0 on
  (4c, ∞). Source: RH_px Lemma 2.1 (uses Proposition 2.2 only).
- Lemma 5.4 (signs off the axis). Source: RH_px Lemma 2.2.
- Transformations U → R → T → S (unlensing the poles with Π, WLXZ (3.10)–(3.15); normalization by g; lens and
  saturated-region factors V^△, WLXZ (4.12)–(4.13)). Write them out once with the explicit matrices. Source: RH_px §1
  "Transformations", §3 "Transformations", "Facts about the jumps". Rename Q → S (§4.4).
- Lemma 5.5 (where the weight is evaluated). On every contour and region where w (equivalently r_n) is evaluated,
  |arg z| stays below a geometry-dependent bound, so ξ = log t ∈ S_{ϑ_p}. The far region Ω_∞ = {|z| > n^p + δ′} never
  uses w. Source: ROUTE2 §2 (H_an) note (Rule R F4); ROUTE2_plt1 Lemma S_w; xframe §2 "Strip needed". This lemma
  explains why the three strips differ. Put the per-geometry angles in Table 1.
- Lemma 5.6 (Potter in the sector): |ℓ₁(t)|^{±1} ≤ C_η|t|^η for |arg t| ≤ ϑ_p, |t| ≥ 1. Hence |r_n|^{±1} =
  poly(n) on the saturated and top pieces. Source: ROUTE2 §2 (consequence of (H_an)); ROUTE2_plt1 §1.
- Table 1 (the geometry table of §3.3 above).

Cited vs proved: Proposition 2.2 (Paper 1) and WLXZ patterns cited; everything else proved.
Re-organisation: **R2** (the RH_px frame, ROUTE2's changes, the xframe transfer table and the RH_plt1 amendments are
merged into one presentation, for general ℓ₁ and all p); **R3** (rename WLXZ's/RH_px's Q to S); **R8** (Airy, top end
and saturated region are presented once).

### §6 The outer scalar function in the three geometries (≈ 8 pp)

**Purpose.** Construct the scalar F that removes the oscillatory factors from the jumps away from 0, and with it the
band weight W₀, the global parametrix, the Airy parametrix and the top-end bounds. Collect everything §7 needs in one
proposition.

Opening paragraph: the remaining obstacle away from the hard edge is a scalar one. Stirling's ratio D̃ = e^{−j(t)}
removes the Γ-function growth of the node masses, but it has the cut of t(z). How the cut is handled depends on how
far the sector of t(z) reaches: inside (−π, π) (p > 1), exactly onto ±π (p = 1), or beyond (p < 1). One sentence
for each case, then the three subsections.

Statements:
- §6.1 p > 1. Lemma 6.1 (D and the Binet-cut scalar B: analyticity, jumps, the Hölder exponent ν_p at 0, behaviour at
  ∞). Source: RH_px Lemmas 3.1–3.3. Lemma 3.2(v) is **not** needed; drop it, together with the (h2) jump.
- §6.2 p = 1. Lemma 6.2 (reflection): D = e^{j(−n/z)} on ℂ ∖ [0, ∞), with no jump on (−∞, 0), B ≡ 1, and Stirling
  needed only where |arg z| ≤ π/3 + π/24. Source: ROUTE2_xframe1 §1 Lemma X1 (PROVED-mod-cite DLMF 5.5.1, 5.5.3,
  5.11.1; REVIEWED). Remark 6.3 (why the classical quotient parametrix fails at p = 1; Lemma X2, PROVED + obstruction
  scoped to that construction). Use the wording of REVIEW_Plan54 F2: it obstructs "RH_px §4.1 as written", not every
  quotient construction.
- §6.3 0 < p < 1. Lemma 6.4 (seam scalar): the angles ϑ_seam = πp/2, ϑ_lip = πp/4; B_in, B_out; χ as a Cauchy
  integral of χ_± on the seam rays; no winding (Lemma S(i)–(iii)); F continuous across the seams; F → (2πn)^{−1/2} at
  ∞. Source: RH_plt1b §1 (REVIEWED; state the Binet sign once, REVIEW_Plan51 F2). Lemma 6.5 (n-uniform modulus of χ
  at the corner): |χ(z) − χ(0)| ≤ C|z|(1 + log(1/|z|)) off the seams. Source: ROUTE2_plt1 §3.2 Lemma X0 (PROVED-mod-cite;
  F3: (1 + log|z|)² for |z| ≥ 1). Remark: the seams do not see ℓ₁, and with W̃ := D_W the seam jump disappears.
  Source: ROUTE2_plt1 §2 "Do the seams … see Ψ₁?".
- §6.4 (common). Lemma 6.6 (Hölder endpoint bound for the Szegő integral). Source: RH_px Lemma 3.4 (self-contained).
  Lemma 6.7 (normalization at ∞: V = I + O(1/z) after a constant diagonal conjugation). Source: RH_px Lemma 3.5,
  with the p = 1 rate correction (REVIEW_Plan54 F1) and the p < 1 note (RH_plt1 amendments). Band weight
  W₀ = C_n x^α(4c − x)H_n(x)r_n(x) and its Szegő function D_W = D_{x^α}D_{(4c−x)H_n}D_{r_n}. Global parametrix P^∞.
  Airy parametrix at 4c (WLXZ §6.1, with r_n analytic in U(4c, 2ε) and |log r_n| ≤ Cε_Λ there). Top-end bound
  n^{−pn}poly(n) (RH_px §4.3; r_n^{±1} = poly(n)). Lemma 6.8 (super-small lip entries). Source: RH_px Lemma 4.3, first
  bullet only (the (h1) entries); xframe §2 row L4.3; ROUTE2_plt1 §3.1.
- **Proposition 6.9 (Frame Proposition; the interface to §7).** For p > 0, 1 < s < 1 + 2p, ℓ₁ with (A_{ϑ_p}) and
  n ≥ n₀, with Q := D_∞^{−σ₃}VD_W^{σ₃}:
  - (F1) Q → I at ∞, and its jumps v on Σ are listed: band [[0, 1], [−1, 0]]; lips [[1, 0], [(D_W²/W₀)e^{2nφ}, 1]]
    plus super-small entries; saturated region and vertical Airy segments as in WLXZ (6.4); Σ^△ lips and top pieces
    I + O(e^{−cn}poly(n)), resp. I + O(n^{−cn}); nothing on (−∞, 0), on the seams (p < 1), or beyond n^p + δ′.
  - (F2) W₀ = C_n x^α(4c − x)H_n(x)r_n(x), with log H_n − log H_n(0) Hölder-ν_p on [0, η₀], n-uniformly, and H_n
    analytic on (0, 4c + ε). The constants cancel in D_W²/W₀.
  - (F3) Lip angles: the lips leave 0 at ±ϑ_lip; the Bessel rays lie at ±(π − ϑ_lip).
  - (F4) Super-small entries: O(exp(−c n|z|^{−1/p})|z|^{−C}) on the lips in U(0, δ).
  - (F5) The global parametrix P^∞ and the Airy parametrix P_r (with P_r(P^∞)^{−1} = I + O(1/n) on ∂U(4c, ε)); all
    jumps of Q(P^∞)^{−1} outside the two discs are exponentially small.
  - (F6) f is conformal on U(0, δ), n-independent, f(0) = 0, f′(0) < 0, and |e^{2nφ}| ≤ e^{−cn|z|^{1/2}} on the lips.
  - (F7) The a priori bound: Q = O(|z|^{−|α|/2−η}) near 0 for every small η > 0 (n fixed), and Q is bounded at the
    other vertices. Hence Q± ∈ I + ∂C(L²(Σ)) (App. C).
  - (F8) Extraction: (Q₁)₁₂(Q₁)₂₁ = n^{2p}b_n² and a(Q) = n^pa_n (invariance lemma, §8).
  Sources: the union of the above; ROUTE2 §2 table; ROUTE2_plt1 §2 table; xframe §2 table; ROUTE2 §4.3 "(Q in L²)".

Cited vs proved: DLMF and WLXZ §6.1 cited; everything else proved.
Re-organisation: **R4** (each geometry gets ≤ 2 pages; everything shared goes to §6.4); **R5** (the Frame
Proposition is new as a statement: it collects existing lemmas, and the reviewer should check that every item has a
source).

### §7 The hard edge: comparison with a Bessel model (≈ 10 pp)

**Purpose.** Prove that the true problem Q and an explicitly solvable comparison problem Q̃ have the same first two
moments at ∞ up to O(ε′_n/n), with no rate on ε_Λ needed for uniform invertibility.

Opening paragraphs (two; this is the heart of the paper, so motivate carefully):
1. Why a local parametrix fails. The factor r_n(z) = z^{−ϑ/p}e^{ρ(z)}-type is not Fisher–Hartwig. Any W̃ with
   W̃₊W̃₋ = W₀ that is continued across (−δ, 0) jumps there by 1 + O(ε_Λ), with no rate. The Bessel matrix at the
   scale |z| ≍ n^{−2} amplifies this to O(nε_Λ). A drifting Bessel order removes only the leading tilt. Source:
   ROUTE2 §2 last paragraph; outline_B_sv §5. This is Conway–Deift's Remark 4.10 situation.
2. The remedy, credited to C–D Theorem 4.7. Build the Bessel parametrix with W̃ := D_W, the Szegő function of the
   whole band weight. It has no jump on (−δ, 0), so the comparison problem is exactly solvable, and the error moves
   to the lips, where it is small in sup norm but has no rate. A Neumann series needs only sup-norm smallness.
   Bessel localization (e^{2nφ} confines the mismatch to |z| ≲ n^{−2}, up to a tail) gives the factor 1/n.

Statements:
- Lemma 7.1 (local form of the Bessel model): for α ∉ ℤ, Ψ_α = Ψ̂(ζ)ζ^{ασ₃/2}S, with Ψ̂ entire and det Ψ̂ ≠ 0; for
  α = 0, Ψ_0 = Ψ̂(ζ)[[1, κ log ζ], [0, 1]]S with κ = −i/(2π). Consequences: |Ψ_α^{±1}| ≤ C|ζ|^{−|α|/2} (log for
  α = 0), and Ψ_αe₂e₁ᵀΨ_α^{−1} = O(|ζ|^{−|α|}) for |ζ| ≤ 3. Source: ROUTE2 §3.2 (PROVED-mod-cite KMVV (6.23)–(6.25);
  DLMF 1.13.4, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2). For p < 1 it holds on the sector |arg ζ| < π − ϑ_lip
  (ROUTE2_plt1 §3.1).
- Lemma 7.2 (comparison parametrix): P̃₀ := (−1)^nE_nσ₃Ψ_α(n²f)σ₃D_W^{−σ₃}e^{nφσ₃}, with E_n = D_∞^{σ₃}P^∞_0Mf^{σ₃/4}
  (2πn)^{σ₃/2}. (i) E_n is analytic in U(0, δ), det E_n = 1, and it is bounded with bounded inverse in the
  D_∞-frame, uniformly in n. **It does not involve the weight.** (ii) P̃₀ has V's band jump, no jump on (−δ, 0)
  (or on the seams), and lip jump [[1, 0], [c_±e^{2nφ}/D_W², 1]]. (iii) P̃₀(P^∞)^{−1} = I + O(1/n) on ∂U(0, δ).
  Source: ROUTE2 §3.1 Lemma H1′; RH_zeta_close §1.2 Lemma H1. Comparison solution P̃, 𝒵̃ = I + O(1/n), Q̃: ROUTE2 §3.1,
  RH_zeta_close §1.2 (geometry at 4c: v = ṽ there, Rule R F10 of Plan 14).
- Lemma 7.3 (lip mismatch): on the lips in U(0, δ), |D_W²/W₀ − c_±| ≤ C(|z|^{ν_p}log(2/|z|) + ε_Λ(T_n)). Hence
  ‖v − ṽ‖_∞ ≤ Cε′_n → 0 and v − ṽ = d_n e₂e₁ᵀ + (super-small). Source: ROUTE2 §3.3 LW1′; xframe §3; ROUTE2_plt1 §3.3.
  The proof has three factors: x^α (explicit, D_{x^α}² = (4cz/Φ)^α); (4c − x)H_n (Hölder, by Lemma 6.6 and, for
  p < 1, Lemma 6.5); r_n (the scale-invariant path integral, which is the new point). Give the r_n part in full;
  it is the paper's cleanest new idea.
- Proposition 7.4 (uniform resolvent for the comparison problem): for |α| < 1 there are n₀ and C with
  ‖(1 − C_ṽ)^{−1}‖_{L²(Σ)} ≤ C for n ≥ n₀. Source: ROUTE2 §4.1 UR′ (incl. (b′)); ROUTE2_plt1 §4.1; RH_zeta_close §1.4
  (a), (c)–(e). In the main text: the statement, the reduction to the inhomogeneous RHP (C–D Prop. 4.6, easy half), and
  a half-page sketch of where |α| < 1 enters (Lemma A.1 with β = ±α/2; area estimates; Hilbert–Schmidt bounds). Full
  proof: App. B.
- Theorem 7.5 (uniform resolvent for the true problem): ‖(1 − C_v)^{−1}‖ ≤ 2C for n ≥ n₁. Source: ROUTE2 §4.3 C′;
  C–D Thm 4.7's Neumann argument (quoted in T3). Proof: 5 lines. Say explicitly: "Here only ε′_n → 0 is used."
- Proposition 7.6 (the mismatch moves the moments by O(ε′_n/n)): Q₁ − Q̃₁ and Q₂ − Q̃₂ are O(ε′_n/n) in the D_∞-frame.
  Source: ROUTE2 §4.3 D′; RH_zeta_close §1.6; C–D Thm 4.4 + (4.14)–(4.15). Proof (1.5 p): main term in the two ζ-ranges,
  correction term O(ε′_n²/n).
- Remark 7.7 (what is not proved): Q̃ depends on ℓ₁ at order 1/n (through 𝒵̃ at the Airy edge), so the relative
  effect of ℓ₁ on b_n at order 1/n is not determined. Source: ROUTE2 Theorem RII "What is proved …" (Rule R F3).
- Remark 7.8 (α ≥ 1): the comparison frame fails (Q̃ ∉ L²_loc at the Bessel scale; Lemma A.1 needs |β| < ½); this
  is why the shift is used. Consistent with the Deift–Piorkowski remark on exponent 1. Source: ROUTE2 §6 GAP-α;
  novelty_lineB_B §2(b).

Cited vs proved: KMVV, DLMF, C–D Thm 4.4 and the 4.7/4.9 arguments cited; everything else proved.
Re-organisation: **R11** (present the comparison machinery once for general |α| < 1. Never "first α = −½ (RH_ζ),
then generalize". RH_ζ is not in this paper; credit the C–D mechanism, not our earlier note). **R12** (use only the
(b′) membership argument; the crude (b) of RH_zeta_close fails for |α| > ½: REVIEW_Plan48 F1).

### §8 Extraction: proof of Theorem 4 (≈ 2 pp)

**Purpose.** Read off a_n, b_n from Q₁, Q₂.

- Lemma 8.1 (invariance): (Y₁)₁₂(Y₁)₂₁ and a(Y) are unchanged under Y ↦ CYk^{σ₃}, for constant diagonal C and scalar
  k = k_∞(1 + k₁/z + …). For U: (U₁)₁₂(U₁)₂₁ = n^{2p}b_n², a(U) = n^pa_n. Source: RH_px §5 "Extraction" (convention
  checked against the toolkit `_fold`). For the D_W conjugation only finiteness of D_W's 1/z coefficient for each n
  is needed (REVIEW_Plan48 F6).
- Proof of Theorem 4: for Q̃ = (D_∞^{−σ₃}𝒵̃D_∞^{σ₃})P^∞_0 outside the discs, (Q̃₁)₁₂(Q̃₁)₂₁ = c(p)²(1 + O(1/n)) and
  a(Q̃) = 2c(p)(1 + O(1/n)); Proposition 7.6 adds O(ε′_n/n) = o(1/n). Source: ROUTE2 §4.4; xframe §4; ROUTE2_plt1 §4.3.
- Remark 8.2 (why c(p)): (P^∞_{0,1})₁₂(P^∞_{0,1})₂₁ = c², from a(z) = ((z − 4c)/z)^{1/4}. The band length 4c is fixed by
  saturation (Proposition 2.2).

### §9 Numerical illustrations (≈ 2 pp)

**Purpose.** Show the law and the O(1/n) rate in three geometries, including one s outside the base window (reached
only through the shift). Make clear that the computations are illustrations, not evidence for the proofs.

- Table 2 (§9.2 below), with a one-paragraph description of the method: extended-precision RKPW recursion on the
  truncated measure (atoms k ≤ K, plus a Gauss–Legendre quadrature of the continuum tail where the hard-edge scale
  k ≍ n^{1+2/p} exceeds K); K-doubling and truncation spreads reported. **Warning to include:** without the tail, the
  truncated measure has a soft edge and the law fails (ROUTE2_plt1 §6 [4]). That is a property of truncation, not a
  counterexample.
- Optional Figure 3: n(n^pb_n/c − 1) against log n for ℓ ≡ 1 and ℓ = e^{√log(k+e)}, three panels (p = ½, 1, 2), from
  the same data.
- One sentence: the deviation from the pure power drifts slowly toward 0, like L′(log n)/2. This is the content of the
  conjecture in §10.

Sources: `research/G1/RH/route2/checks/check_r2_coeff.out` (p = s = 2; K-converged for n ≤ 400 only, REVIEW_Plan48
F8); `check_x1_coeff.out` (p = 1, r = 2, 2.5, 3; five truncations); `check_r2p_coeff.out` (p = ½, s = 1.5, 1.75, 2,
2.5; tail to 10⁴⁸). Scripts must be re-run before submission (as for Paper 1), with the repository URL and commit hash
supplied.

### §10 Further remarks and open problems (≈ 2 pp)

- 10.1 The 1/n term. Conjecture (numerical only): n^pb_n/c(p) = 1 − (s − 1 − L′(log n))/(2n) + o(L′(log n)/n), with
  L = Λ_ℓ. Pure power: −(s − 1)/2 and p/2 (numerical, RH_px §0). Source: ROUTE2 §5 (CONJECTURE + NUMERICAL); xframe §5;
  ROUTE2_plt1 §6. Say that the shift maps this conjecture at s to s + p under a stated extra hypothesis (Remark
  SH-1/n, CONDITIONAL; implication proved). Keep it to 3 lines, or drop it.
- 10.2 Other routes at p = 1. (a) The symmetric WLXZ frame (band centre, Fisher–Hartwig exponent s − 3/2) covers only
  1 < s < 2 by this method, because the comparison needs the exponent in (−½, ½). The loss is a frame effect:
  L²(|dy|) on the symmetric contour is L²(|x|^{−1/2}|dx|) in x. Source: ROUTE2_p1, xframe §0. (b) Folding the
  symmetric problem gives a second proof on 1 < s < 3. It shares the α = 0 comparison step with §7, so it is not
  independent at the decisive step. Source: PROOF.md §3.22 "Relation to §3.23" (REVIEW_Plan53 F1–F2). (c) For pure
  powers and p ≠ 1, the classical quotient (glued) parametrix also works (RH_px §4.1, RH_plt1b §2). At p = 1 it fails
  (Remark 6.3).
- 10.3 Rough weights: the Paper 3 announcement (if not already in §1.3, put it here; one place only).
- 10.4 Other nodes. Nodes x_k = f(k) other than pure powers are open. So is an RH analysis of the weight itself for
  α ≥ 1, which would be needed for the 1/n term there. Source: PROOF.md §4 "Open now".

### Appendix A. Two L² bounds on a star of arcs (≈ 3 pp)

- Lemma A.1 (power-weighted Cauchy operator): for a finite star of C² arcs through z₀ at distinct angles and |β| < ½,
  f ↦ |z − z₀|^βC_±(|s − z₀|^{−β}f) is bounded on L², dilation-invariant. Source: RH_zeta_close §1.4 Lemma W (PROVED;
  DLMF 1.14.38–40, 5.5.3, 5.12.1/3). Include the flattening detail with the arclength factor γ′(ρ)dρ (REVIEW_Plan48
  F10).
- Lemma A.2 (log-commutator): the kernel (log(z − z₀) − log(s − z₀))/(s − z) is L²-bounded on such a star. Source:
  ROUTE2 §4.2 Lemma W′ (PROVED). (Numerically the Mellin constant is π² on one ray; mention it only as a check, or omit
  it.)

### Appendix B. Proof of Proposition 7.4 (≈ 5 pp)

(a) reduction (C–D Prop. 4.6, easy half, re-proved; uniqueness by an area estimate); (b′) membership m ∈ ∂C(L²) for
every |α| < 1 (the factorization Q̃ = G(z)(−z)^{ασ₃/2}Θ(z), the core bound |T_β(z)| ≤ C‖h‖d^{−1/2} via three ranges,
the area integral O(ε^{3/2})); (c) partition (Carleson constant uniform in n); (d) hard-edge block (two copies of Lemma
A.1 with β = ±α/2; Lemma A.2 at α = 0; Hilbert–Schmidt bounds ∬|s|^{−|α|}|z|^{−|α|} < ∞ and O(n^{−2}) for |ζ| ≤ 2);
(e) Airy block (α-free). Sources: ROUTE2 §4.1 (with the re-check of REVIEW_Plan48); RH_zeta_close §1.4 (a), (c), (d), (e);
ROUTE2_plt1 §4.1 (star of three arcs at 0, ±πp/4). Rename the local factor G → A₁ (G is the Gaussian).

### Appendix C. The a priori bound and Q ∈ I + ∂C(L²) (≈ 2 pp)

Source: RH_px §5 "(Y4)_x" (sum bound away from the band; the 𝒦± contour argument in the lens sectors), with the
Potter loss (ROUTE2 §4.3 "(Q in L²)"); RH_plt1b §2 (φ₀ < πp); xframe §2 row §5. Conclude Q = O(|z|^{−|α|/2−η}), and
L² at every vertex (RH_zeta_close §1.6 list).

### Appendix D (optional). First-variation formulas (≈ 1.5 pp)

Only if Lemma 4.2's a_n formula is not cited (§7, R7). Source: PROOF.md §3.5 Lemma FVa (steps 1–6); G3prime PROOF.md
§5.2 Lemma H (Gram–Sylvester).

---

## 6. Style guide for the drafters

### 6.1 Vocabulary: forbidden in the paper

- Repo process words: Plan, Rule A/C/L/N/R, REVIEWED, PROVED, PROVED-mod-cite, PROVED-mod-input, CONDITIONAL,
  NUMERICAL (as a label), GAP, OBSTRUCTION, HEURISTIC, "stop condition", "work package", "line B", "item 11", "G1",
  "G2", "Route II", "Q-frame", "transfer table", "delta to RH_px".
- Lemma codenames: every repo name gets a descriptive name (§10 renaming table). Never RII, RII_x1, UR′(b′), LW1′, D′,
  C′, H1′, X0, X1, X2, RedA, SH-r, CS-r, CT-Ch, CT₁, B_all, GAP-int, GAP-α, H_an, Sat_p⁺, FV, FVa, L0, QLP, T3-*.
- "Law P", "Ψ", "N" (the degree), "β_n" (in any sense), "α_n", "α_x", "σ" for an exponent.
- "new", "novel", "first", "for the first time". Use instead: "we have not found this in the literature" (Paper 1's
  wording), attached to a specific statement. Use "to our knowledge" at most once in the paper.
- "certified", "verified" (for numerics): say "computed in extended precision", "stable under doubling of K".
- "trivially", "obviously", "it is easy to see". Write the reason instead, even if it is short.

### 6.2 Structure

- Main results first (§1.2), before any history. Every theorem in §1 is followed by remarks that interpret it
  (examples, sharpness, what is not claimed).
- **Motivate before computing.** Every section and every lemma with a proof longer than half a page opens with a
  short paragraph: what the step achieves, why it is needed, and what the obstacle is. §5 above gives the opening
  paragraph for each section; use it.
- Short paragraphs (≤ 8 lines in the PDF). One idea per paragraph. Displays for every formula that is used later.
- Every proof that is a computation states its plan in its first sentence ("We bound the main term on |ζ| ≥ 2 and on
  |ζ| ≤ 2 separately.").
- Proofs longer than ~1.5 pages go to an appendix, with a proof sketch in the main text.
- No forward references inside proofs, except to the appendices and to the Frame Proposition.
- Do not repeat a construction for a second geometry: state the difference in one line, or put it in Table 1.

### 6.3 Notation and conventions

- Use exactly the notation table (§4). If a new local symbol is needed, check the table for clashes first.
- One convention for the Jacobi coefficients (§2), one for the Cauchy operator (C(f)(z) = (2πi)^{−1}∫f(s)ds/(s − z)),
  one for orientation (band left to right; KMVV's left-endpoint conventions, with the reversal absorbed by σ₃).
- British spelling, as in Paper 1 (regularised, normalised, organisation, behaviour).
- LaTeX: amsart 11pt; Paper 1's preamble and macros; \label prefixes thm:, lem:, prop:, rem:, sec:, eq:, tab:,
  fig:.

### 6.4 Tense and voice

- Present tense and "we" for mathematics ("We prove", "Lemma 4.3 shows"). Past tense only for computations that were
  carried out ("The coefficients were computed …").
- No first-person singular. No "the author".

### 6.5 Citations ("Tools", §2.5)

- Every external result that is used as input is stated once, precisely, with its hypotheses and its equation
  number, in §2.5. It is quoted from a source someone has actually read (RH/CITATIONS.md, research/G1/CITATIONS.md).
  Inside proofs, refer to it by the paper's tool label (T1–T4 plus equation number).
- Attribution-only citations (results we credit but do not use: Dai–Piao–Qiao, Derevyagin–Derkach, Monien, Haynes–
  Zudilin, Piorkowski, Trogdon, Deift–Piorkowski, McLaughlin–Miller, DIK, Levin–Lubinsky) are fine in §1.3 and in
  remarks. Quote them only from opened sources (novelty_*.md record which were opened).
- **Not yet read; do not cite until read:** Bueno–Marcellán 2004; Bingham–Goldie–Teugels §1.8; Vuilleumier 1976;
  Chihara 1978 Ch. III; Wall; Knopfmacher–Lubinsky–Nevai 1988; Lubinsky–Mhaskar–Saff; Fischer 1998 (only a pointer);
  Borodin–Boyarchenko; Gragg–Harrod (RKPW). Mark each \cite with a TODO comment until it is read.

### 6.6 Honest wording for positioning (use these, or close variants)

- C–D: "The comparison argument in §7 is that of Conway and Deift [CD, Theorem 4.7 and Proposition 4.9]. What we add
  is a comparison model built from the Szegő function of the full weight, a uniform resolvent bound for a Bessel edge
  of any order |α| < 1, and the treatment of an arbitrary slowly varying factor."
- WLXZ: "Within the literature we have read, the only Riemann–Hilbert analysis of discrete orthogonal polynomials on
  infinitely many nodes accumulating at a finite point is [WLXZ], for the Tricomi–Carlitz polynomials; our frame
  follows theirs."
- Lommel: "For (p, s) = (2, 2) the coefficients are explicit (Lommel polynomials), and Theorem 2 can be checked
  directly." (Only after the citation gate.)
- Chain sequences: "Lemma 3.3 is a special case of [DPQ, Proposition 2.1]; we include the short proof because the rate
  version, Lemma 3.4, follows the same lines. We have not found Lemma 3.4 in the literature."
- Smoothing: use the wording given in the Lemma 4.1 entry of §5 of this outline (citation gate on BGT/Vuilleumier).
- Main theorem: "We have not found Theorem 1 in the literature, even for bounded ℓ. The closest results we know
  concern continuous weights on an interval [CD, DP, Pio, Tro, MM] or exponential weights [LL]."

### 6.7 Numerics

- They are illustrations only. One table (and at most one figure), each with a caption that says how it was computed
  and how stable it is under truncation. They appear in §9 only, plus at most one sentence in §1.
- Never use numerics as an argument in a proof or remark. ("Numerically, the coefficient appears to be −(s − 1)/2"
  is fine in §10.)

---

## 7. Risk list (where the proofs are delicate or long, and what the reader must be told)

| # | Risk | Where | What to tell the reader / what the drafter must do |
|---|---|---|---|
| R1 | **Uniform resolvent at a Bessel edge of order \|α\| < 1.** This is the step experts will check first (novelty_lineB_B §2(b); Deift–Piorkowski's remark that C–D Thm 4.7 "requires a different proof" at exponent 1). | Prop. 7.4, App. B | State precisely where \|α\| < 1 enters: Lemma A.1 with \|β\| = \|α\|/2 < ½; ∫\|s\|^{−\|α\|} < ∞; the area estimate. Say that we do not use C–D's Theorem 4.5 (Legendre-specific), and that the comparison model is an explicit parametrix. Use only the (b′) membership argument: the crude product bound of the earlier write-up fails for \|α\| > ½ (REVIEW_Plan48 F1). Point to Remark 4.6 (only \|α\| ≤ ½ plus α = 0 is needed for s > 1 + p/2). |
| R2 | **"No rate" must be stated precisely.** The sup-norm mismatch is o(1) with no rate (it is O(ε_Λ)). That suffices for the Neumann series. The 1/n comes from Bessel localization. The relative 1/n effect of ℓ is **not** proved. | Lemma 7.3, Thm 7.5, Prop. 7.6, Remark 7.7 | Never write "the slowly varying factor costs O(ε/n)" (REVIEW_Plan48 F3). Theorem 1(iii)'s O(1/n) is absolute, not relative. |
| R3 | **The p = 1 x-frame transfer.** RH_px is stated for p > 1. At p = 1: Lemma 1.1 holds (open sector); Stirling for D̃ is non-uniform near arg z = ±π but is never needed there; the reflection lemma removes the Binet cut; the quotient parametrix fails (Lemma X2); g − log z = O(\|z\|^{−1}log\|z\|). | §6.2, Table 1, Remark 6.3 | Present p = 1 as a *simplification* of p > 1 (no cut), not as a special case to be checked. State in one sentence that the comparison parametrix uses band values only (D_W) and never continues anything across (−δ, 0). That is why Lemma X2 does not affect it. Do not say that the quotient construction fails "in general" (REVIEW_Plan54 F2). |
| R4 | **The seam geometry (p < 1).** Γ's poles enter the slit plane; D̃ is confined to the inner sector; the seam scalar χ has \|χ\| = O(log n), but χ − χ(0) is n-uniformly controlled at the corner (Lemma 6.5); Bessel rays at π − πp/4 use KMVV's angle freedom; the strip π/2 suffices (Lemma 5.5). | §6.3, Lemma 7.1, App. B (star of three arcs) | Tell the reader that the seams carry no weight and no jump once W̃ = D_W. The only trace of the seams in §7 is the factor e^{−2χ} in H_n, controlled by Lemma 6.5. Use one Binet sign convention (REVIEW_Plan51 F2). Note the (1 + log\|z\|)² for \|z\| ≥ 1 (REVIEW_Plan51 F3). |
| R5 | **Infinite discrete node set: identification and a priori bounds.** Q± ∈ I + ∂C(L²) needs the (Y4) estimate with a Potter loss \|z\|^{−η}. The top end has length O(n^p), killed by n^{−pn}. The saturated region uses WLXZ's V^△. | App. C, Frame Prop. (F7), §6.4 | State clearly that no existence theorem for the RH problem is needed: Q is built from the OPs, and only its membership in I + ∂C(L²) is used (C–D Thm 4.4's hypothesis). |
| R6 | **KMVV's hypothesis "h real analytic on the closed interval".** Our band factor is only Hölder at 0. | Lemma 7.2 | In the comparison construction the prefactor E_n involves no weight (P^∞D_W^{σ₃} = D_∞^{σ₃}P^∞_0), so KMVV's removability argument applies to an n-independent, weight-free object. Say this explicitly. It is a selling point, and it pre-empts the objection. |
| R7 | **First-variation formula for a_n.** The repo proof uses the two-point function of the Heine ensemble (determinantal) via G3′ Lemma H. | Lemma 4.2 | Decide: cite a source that has been read, or give App. D. Do not leave an unproved "standard" claim. FV (the b-formula) is 6 lines from Heine; give it in full. |
| R8 | **Chain-sequence rate.** u_n converges only at O(√η_n), and this is sharp. | Lemma 3.4, Remark 3.5 | Say why no rate is lost (only increments enter), with the sharpness example. |
| R9 | **Strip hypotheses differ by geometry** (π/p for p > 1; π/2 for p ≤ 1). For 1 < p < 2 the stated strip is wider than π/2. | (A_ϑ), Lemma 5.5 | Keep the REVIEWED strips. Do not claim that a narrower strip suffices for p > 1, although it is plausible (xframe §2 says ROUTE2 used π/p "for convenience"). The general case (Theorem 1(ii)) is unaffected, since Lemma 4.1 gives every strip. |
| R10 | **Re-ordering of the final assembly** (smooth last, §0 item 5). | §4.4 | It uses only REVIEWED statements (Prop. 4.5 holds for all p > 0, s > 1; Theorem 3 with η_n = 1/n). Tell the reviewer explicitly (NOTES.md), since the repo's B_all is assembled in the other order. |
| R11 | **Pure powers via the comparison route.** Theorem 2 is proved as Λ ≡ 0 of Theorem 4 plus Theorem 3, not by the repo's quotient constructions. | §4.4, Remark in §10.2 | The REVIEWED statements cover Λ ≡ 0. Rule A (a) of ROUTE2, xframe and ROUTE2_plt1 records the consistency checks. Tell the reviewer (NOTES.md). In the paper, one remark mentions the classical quotient route. |
| R12 | **Normalization at ∞ with unbounded support.** g − log z decays like z^{−1/p} (p > 1), like z^{−1}log z (p = 1), like 1/z (p < 1). Only boundedness and the absence of jumps of F^{−1}e^{n(g − log z)} beyond n^p + δ′ are used. | Lemma 6.7 | State it that way. Do not write a uniform rate. |
| R13 | **Numerical pitfalls** (only if the numerics are re-run). Truncation without a tail gives a soft edge (wrong law). The direct evaluation of D̃ at huge t is catastrophic in 30-digit arithmetic (use the Stirling series for \|t\| > 10⁴; xframe §2 "Numerical note"). K-convergence at n = 800 (p = 2) fails. | §9 | Report K-doubling spreads. Omit unconverged entries. |
| R14 | **Paper-length risk.** The RH part is long. | §§5–7 | Enforce one presentation for all geometries (Table 1, Frame Proposition). Push operator theory to the appendices. If the draft exceeds ~65 pp, move the full proof of Lemma 6.4 (seam scalar) to an appendix and shorten §6.1 by citing RH_px-style computations to WLXZ where they coincide. |

---

## 8. Drafting split (4 parallel chunks)

All drafters work against this outline and the notation table. Each chunk produces a self-contained `.tex` file
(`papers/paper2/sec_*.tex`) with the shared preamble and the \label prefixes. Cross-chunk references go only through
the labels fixed here: Theorems 1–4, Lemma/Prop numbers as in §5 above, and the Frame Proposition items (F1)–(F8).

| Chunk | Sections | Inputs to read | Interface obligations |
|---|---|---|---|
| **A. Front and back matter** | Abstract; §1 Introduction; §9 Numerics; §10 Remarks; bibliography | this outline (§§1–2, 6.6); papers/paper1/main.tex §1; research/program/novelty_*.md (lineB_A, lineB_B, G1RH); RESEARCH_PROGRAM §§1, 6; the three check outputs | Uses the theorem statements of §2 verbatim. Owns refs.bib. Owns the citation-gate TODO list. |
| **B. Elementary half** | §2 Preliminaries (incl. §2.5 Tools); §3 Christoffel shift; §4 Smoothing reduction (incl. §4.4 assembly); App. D if chosen | PROOF.md §§3.1–3.5, 3.14 (L0), 3.17 (RedA), 3.19 (CT₁ ⟸), 3.21; ROUTE2 §1; ROUTE2_alpha; ROUTE2_plt1 §5; G3prime PROOF.md §5.2; RH/CITATIONS.md (for §2.5) | Must state Theorem 4 exactly as in §2 and use it as a black box. §2.5 must contain every tool T1–T4 that chunks C and D cite. |
| **C. The frame** | §5 Common frame; §6 Outer scalar in three geometries, up to and including the Frame Proposition 6.9; App. C | RH_px (all); RH_plt1 §0 (amendments); RH_plt1b; ROUTE2 §2; ROUTE2_xframe1 §§1–2; ROUTE2_plt1 §§1–2, 3.2; RH_zeta_close §1.0 (frame); WLXZ quotes in RH/CITATIONS.md; reviews 48, 51, 54 | Delivers (F1)–(F8) exactly. Table 1 lives in §5. Uses Proposition 2.2 (Paper 1) by label. |
| **D. The hard edge** | §7; §8 Extraction; App. A; App. B | ROUTE2 §§3–4; ROUTE2_xframe1 §§3–4; ROUTE2_plt1 §§3.1, 3.3, 4; RH_zeta_close §§1.2–1.7; C–D and KMVV quotes; reviews 48, 50, 51, 54 | Uses only (F1)–(F8) from chunk C and the tools T2–T4. Must not re-derive anything from §6. |

Order of work: all four can start at once. A second pass is needed for (i) chunk A's §1.4 against chunks C and D's
final lemma names, and (ii) a consistency read of the notation by one person. A 5th chunk (optional) is a "reader"
pass: one agent reads the assembled draft as a specialist would and lists every place where a step is asserted
without proof or source. That is the Rule R analogue for the paper.

---

## 9. Figure and table plan

- **Figure 1 (dependency diagram, §1.4).** TikZ version of §3.1. Boxes: Paper 1 input; §5–6 frame; §7 comparison;
  Theorem 4; Theorem 3; Theorem 2; §4 smoothing; Theorem 1. Arrows labelled with the section numbers. Must fit in a
  third of a page.
- **Figure 2 (geometry near the hard edge, §5 or §6).** Three panels, p > 1, p = 1 and p < 1, in a disc U(0, δ): the
  band (0, δ), the lips at ±ϑ_lip, the negative axis (no jump), and for p < 1 the seam rays at ±πp/2 (dashed, labelled
  "no jump in the comparison problem"); the far contour pieces schematically (lens, saturated region, top segment) in
  a fourth, zoomed-out panel. Shared between chunks C and D (owner: chunk C).
- **Table 1 (geometry table, §5).** The table of §3.3, without the repo-source column.
- **Table 2 (numerics, §9).** ℓ(k) = exp √log(k + e) versus ℓ ≡ 1:

  | p | s | α | in window? | n | n(n^pb_n/c − 1), ℓ | same, ℓ ≡ 1 | n(a_n/(2b_n) − 1), ℓ |
  |---|---|---|---|---|---|---|---|
  | ½ | 2 | 1 | no (via the shift) | 100 … 1600 | −0.404 … −0.416 | −0.507 … −0.502 | 0.249 … 0.250 |
  | 1 | 2 | 0 | yes | 50 … 800 | −0.382 … −0.407 | −0.493 … −0.500 | 0.487 … 0.499 |
  | 2 | 2 | −½ | yes | 100 … 400 | −0.387 … −0.400 | (to be read from check output or recomputed) | 0.9985 … 0.9996 |

  Values from check_r2p_coeff.out [1] (K = 10⁵ vs 2·10⁵ agree to 10⁻⁷), check_x1_coeff.out (Ψ A; spreads ≤ 2·10⁻⁸)
  and check_r2_coeff.out (K = 4.8·10⁵; n ≤ 400 only). The final table shows each n separately, not ranges. The
  pure-power column for p = 2 must be recomputed (the check prints only the ratio columns T and R). Caption: the
  limits −(s − 1)/2 and p/2 are observed, not proved; the slow drift for ℓ is the effect of L′(log n).
- **Figure 3 (optional).** The same data, plotted.

---

## 10. Source map and renaming table

Every statement in the paper, its repo source and its repo label. The drafters cite the repo source in a LaTeX
comment next to the statement (`% src: ROUTE2.md §3.3`), so the reviewer can trace it. These comments are removed
before submission.

| Paper | Descriptive name | Repo name and location | Repo label |
|---|---|---|---|
| Thm 1 | main theorem | Cor. B_all (PROOF §3.21), B_{p<1} (§3.20), B_{p=1}^{all} (§3.23) + RedA(iii), re-ordered | PROVED-mod-cite, REVIEWED |
| Thm 2 | pure powers with rate | THEOREMS H2 (RH_px, RH₁(r), RH_p seam); in the paper via Thm 4 at Λ ≡ 0 + Thm 3 | PROVED-mod-cite, REVIEWED |
| Thm 3 | Christoffel shift | Thms SH, SH-r (§3.21; ROUTE2_alpha §§3–4) | PROVED, REVIEWED |
| Thm 4 | RH engine (analytic factor, base window) | RII (ROUTE2 §4.4), RII_x1 (xframe §4), RII_{<1} (ROUTE2_plt1 §4.3) | PROVED-mod-cite, REVIEWED |
| Lem 2.1 | chaining and Potter bounds | L0 (§3.14) | PROVED, REVIEWED |
| Prop 2.2 | equilibrium input | Paper 1 Thm 1.3(i)–(ii) = G2 B*(i)–(ii) | PROVED (citation-free) |
| Lem 3.1 | zeros of P_n | CP (ROUTE2_alpha §2.1) | PROVED |
| Lem 3.2 | Christoffel transfer formulas | CT (§2.2) | PROVED, classical |
| Lem 3.3 | chain-sequence limit | CS (§3.1) | PROVED; KNOWN (DPQ Prop. 2.1) |
| Lem 3.4 | chain-sequence rate | CS-r (§4.1) | PROVED; not found |
| Rem 3.6 | converse; mass at 0 | CT₁ "⟸", Lemma D(b) (PROOF §3.19) | PROVED; very likely KNOWN |
| Lem 4.1 | Gaussian smoothing | RedA (o)–(ii) (ROUTE2 §1) | PROVED; very likely KNOWN in substance |
| Lem 4.2 | first variation | FV (§3.2), FVa (§3.5) | PROVED, standard |
| Lem 4.3 | saturation of the head | Sat_p, Sat_p⁺ (§§3.1, 3.3); G3′ Lemmas H, Sat | PROVED |
| Lem 4.4 | a priori size of a_n, b_n | T3a step 1 (§3.5) | PROVED |
| Prop 4.5 | stability under ℓ/ℓ₁ → 1 | RedA(iii) (ROUTE2 §1) | PROVED, REVIEWED |
| Lem 5.1–5.4 | interpolation problem, band weight, g-function, signs | RH_px §§1–2 (L1.1, L1.2, L2.1, L2.2) | PROVED-mod-cite |
| Lem 5.5 | where the weight is evaluated | ROUTE2 §2 (H_an) note; ROUTE2_plt1 L S_w; xframe §2 | PROVED (bookkeeping) |
| Lem 5.6 | Potter in the sector | ROUTE2 §2 | PROVED |
| Lem 6.1 | Binet-cut scalar (p > 1) | RH_px L3.1–3.3 | PROVED-mod-cite |
| Lem 6.2 | reflection (p = 1) | X1 (xframe §1) | PROVED-mod-cite (DLMF 5.5.1, 5.5.3, 5.11.1) |
| Rem 6.3 | failure of the quotient parametrix at p = 1 | X2 (xframe §1) | PROVED + scoped obstruction |
| Lem 6.4 | seam scalar (p < 1) | RH_plt1b §1 (Lemma S, χ = X) | PROVED-mod-cite |
| Lem 6.5 | corner modulus of the seam scalar | X0 (ROUTE2_plt1 §3.2) | PROVED-mod-cite |
| Lem 6.6 | Hölder endpoint bound | RH_px L3.4 | PROVED |
| Lem 6.7 | normalization at ∞ | RH_px L3.5 (+ REVIEW_Plan54 F1) | PROVED |
| Lem 6.8 | super-small lip entries | RH_px L4.3 (first bullet) | PROVED |
| Prop 6.9 | Frame Proposition | union of the above + ROUTE2 §2 table | (new as a statement; collects REVIEWED items) |
| Lem 7.1 | local form of the Bessel model | ROUTE2 §3.2 | PROVED-mod-cite |
| Lem 7.2 | comparison parametrix | H1′ (ROUTE2 §3.1); H1 (RH_zeta_close §1.2) | PROVED-mod-cite |
| Lem 7.3 | lip mismatch | LW1′, LW1-x1, LW1′_{<1} | PROVED |
| Prop 7.4 | uniform resolvent, comparison problem | UR′ incl. (b′); UR′_{<1}; UR (RH_zeta_close §1.4) | PROVED-mod-cite |
| Thm 7.5 | uniform resolvent, true problem | C′; C (RH_zeta_close §1.5) | PROVED-mod-cite |
| Prop 7.6 | effect of the mismatch | D′; D (RH_zeta_close §1.6) | PROVED-mod-cite |
| Lem 8.1 | invariance of the extraction functionals | RH_px §5 "Extraction" | PROVED |
| Lem A.1 | power-weighted Cauchy operator on a star | Lemma W (RH_zeta_close §1.4) | PROVED |
| Lem A.2 | log-commutator on a star | Lemma W′ (ROUTE2 §4.2) | PROVED |
| App C | a priori bound at the hard edge | (Y4)_x (RH_px §5) + Potter (ROUTE2 §4.3) | PROVED |

Not in the paper: QLP, GS, ST, BK (§3.16); CB, BF, RF, FM, DB, QL-CB (§3.18); B-cond, QL (§3.14); T3-conv, T3-sv,
T3a, T3-avg, T3-all, T3-log, Theorem L, TV, LP, TL, TC (§§3.3–3.9); R, RW, Ra, LR, RL (Paper 3); RH_ζ; RH₁(r) and
the quotient constructions (one remark only); Route (a) of ROUTE2_alpha §6; Lemma IR of §3.22.
