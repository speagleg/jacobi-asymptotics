# G2 citations

Citation gate (AGENTS.md rule 4): each entry is quoted from a source read on 2026-10-13.

## (P) Positivity of logarithmic energy for equal-mass measures — READ

B. Beckermann, V. Kalyagin, A. C. Matos, F. Wielonsky, "Equilibrium problems for vector potentials with semidefinite
interaction matrices and constrained masses", arXiv:1105.3088v2. Read from the arXiv PDF, §1 (definitions) and §2.

> (§1, eq. (1.2) ff.) "I(µ) = ∬ log(1/|x − y|) dµ(x)dµ(y) = ∫ U^µ(x)dµ(x) > −∞." … "M(Σ) = {µ Borel measure, of finite
> mass, supported in Σ, and I(µ) < ∞}" … (§1, before Corollary 1.10) "the set M(Σ) will consist of Borel measures µ of finite mass, supported on Σ, of
> finite energy, and such that ∫ log(1 + |t|) dµ(t) < ∞. (1.12)"
>
> "Lemma 2.1. Let µ, ν ∈ M(C) with ‖µ‖ = ‖ν‖. Then I(µ − ν) ≥ 0, and I(µ − ν) = 0 if and only if µ = ν.
> Proof. See [24, Lemma I.1.8] for measures µ, ν with compact support, and [7, Theorem 2.5] for the unbounded case."

Here [24] is Saff–Totik, *Logarithmic Potentials with External Fields* (1997), and [7] is Cegrell–Kolodziej–Levenberg,
Math. Scand. 83 (1998). The energy convention is I(µ) = ∬ log(1/|x − y|) dµ dµ, from the display after the paper's eq. (1.1).

> (§1, after (1.13)) "For two measures µ and ν of finite masses, satisfying (1.12), we have
> I(µ, ν) ≥ −‖µ‖∫log(1 + |t|)dν(t) − ‖ν‖∫log(1 + |t|)dµ(t) > −∞ … In particular, we have 2I(µ̃, ν̃) ≤ I(µ̃) + I(ν̃)."

Together these make the mutual energy of two measures in M(ℂ) finite, which is what the bilinear expansion in B*(iii)
needs. Lemma 2.1 itself rests on Saff–Totik Lemma I.1.8 (compact case) and Cegrell–Kolodziej–Levenberg Thm 2.5
(unbounded case). Neither was read; this is accepted under "mod-cite (P)".

**Used in:** PROOF.md Theorem B*(iii), optimality and uniqueness of μ*. Both measures there are positive, of mass 1,
with finite energy, and with ∫ log(1 + x) < ∞.

*(Plan 47 note, 2026-10-14: no longer used. B*(iii) now rests on PROOF.md Lemma EP, a self-contained Fourier proof
(ported from papers/paper1/main.tex Lemma 3.3), which also replaces the mutual-energy finiteness quoted from (P) §1 by a
direct bound through B*(ii). (P) is kept here as an alternative route; the old (P)-based argument is quoted in
PROOF.md after the proof of B*. Rule R ACCEPT WITH FIXES (review/REVIEW_Plan47.md), fixes applied — REVIEWED.)*

## (HZ) Haynes–Zudilin — READ

A. Haynes, W. Zudilin, "Hankel determinants of zeta values", SIGMA 11 (2015) 101, arXiv:1510.01901v3. Read from the
arXiv PDF, §1.

> "To be precise, for positive integers a and b, we expect that log det_{1≤i,j≤n} ζ(a(i + j) + b) = −an² log n + O(n²)
> as n → ∞."
>
> "In this brief note we demonstrate how elementary means can be used to prove the weaker asymptotic inequality
> log det_{1≤i,j≤n} ζ(a(i + j) + b) ≤ −(a/2) n² log n + O(n²) as n → ∞."

**Used in:** PROOF.md Corollary HZ, as context only. Nothing is assumed from it.

## Classical facts used without external citation (proved inline in PROOF.md)

- **The arcsine potential identity** ∫ log|x − y| dω_{[0,β]}(y) = log(β/4) on [0, β]. Proved from the Fourier series
  log|2 sin(θ/2)| = −Σ_{k≥1} cos(kθ)/k (Lemma B0).
- **Hadamard's inequality** for positive semidefinite matrices (det ≤ product of the diagonal entries), as used in item
  11 Lemma H7 step 3.

## (M) Monien, p = 1 prior art — READ

H. Monien, "Hankel determinants of Dirichlet series", arXiv:0901.1883v1. Read from the arXiv PDF, §1 and §3. (Found by
the Rule R reviewer.)

> (§1) "We do not know how to prove the full asymptotic expansions but will describe a method that lets one at least
> understand the weaker asymptotic form log H_n^{(0)}[ζ] ∼ log H_n^{(1)}[ζ] ∼ −n²(log(2n) − 3/2)."
>
> (§3) "We seek a continuous test function ρ(x) which maximizes the functional Eq. 3.5 subject to the constraint that
> 0 < ρ(x) ≤ 1 for all x and ρ(x) = 0 for x < 0 and Eq. 3.4. We assume that such a continuous functions exists."
>
> "Theorem 3.1. Define the function ρ(x) for x ∈ [0, ∞): ρ(x) = 1 (0 ≤ x ≤ 1/2), ρ(x) = (2/π)(arctan(1/√(2x−1))
> − √(2x−1)/(2x)) (x > 1/2). Then ρ(x) is the continuous solution of the stationary condition Eq. 3.7 for x > 1/2,
> is normalized and fulfills the condition 1 ≥ ρ(x) ≥ 0 for all positive x ∈ R."

**Relation to G2.** This is the p = 1 case of the constrained problem of PROOF.md §1, and Monien's ρ equals μ*_u at
p = 1 (the reviewer checked numerically). His argument assumes existence, checks only stationarity, and gives no
upper bound. (HZ) §1 also states: "In [5] Monien developed these ideas further and rigorously justified the above
asymptotics in the case r = 0", referring to the leading-order formula log H_n^{(r)} = −n² log n + O(n²).

## Constrained equilibrium literature for Paper 1 §1.2 — READ (Plan 68, 2026-10-15)

Read for decision D10 ("try to read, else cut"). Context only: Paper 1 uses none of these results in a proof. Each entry
says which text was read, from where, and what Paper 1 attributes to it. Statements are paraphrased from the text read.

### (R96) Rakhmanov 1996 — READ (§§1–4, statement of §5)
E. A. Rakhmanov, "Equilibrium measure and the distribution of zeros of the extremal polynomials of a discrete
variable", Sb. Math. 187:8 (1996) 1213–1228. Read the English journal PDF from mathnet.ru (paper sm153, "fullteng").
- Thm 1: discrete Chebyshev polynomials T_{n,N} (orthogonal w.r.t. (1/N)Σδ(ξ_{k,N}) on N equally spaced points of
  [−1,1]); as n/N → c ∈ (0,1) the zero counting measures converge to an explicit f_c(x)dx, with nth-root asymptotics.
- §2: f_c dx is the unique unit measure on [−1,1] of minimal energy with density ≤ 1/(2c).
- Thm 2: points ξ_{k,n} ∈ [−1,1], k ≤ N_n, separated (|ξ_{k+1,n} − ξ_{k,n}| > ρ/n), (1/n)Σδ(ξ_{k,n}) → σ weakly;
  weighted discrete L^p-extremal monic polynomials have zero distribution → λ^σ and nth-root asymptotics e^{−w^σ}.
- Thm 3: σ on [−1,1] with continuous potential and |σ| > 1; the constrained minimiser λ^σ ∈ M^σ = {unit μ ≤ σ} is
  well defined by each of six equivalent conditions (energy minimality, variational inequality, equilibrium
  conditions V^λ ≤ w on S_λ, ≥ w on S_{σ−λ}, max of w(μ), …).
**Paper 1 says:** introduced constrained problems; characterised the constrained equilibrium measure on [−1,1] for
σ of mass > 1 with continuous potential [Thm 3]; zero distribution of discrete extremal polynomials as n/N → c,
in particular discrete Chebyshev [Thms 1, 2].

### (DS97) Dragnev–Saff 1997 — READ (§§1–3, statements; §4 Example 4.1 opening)
P. D. Dragnev, E. B. Saff, "Constrained energy problems with applications to orthogonal polynomials of a discrete
variable", J. Anal. Math. 72 (1997) 223–259. Read the journal scan hosted on E. B. Saff's Vanderbilt publication page
(item 168).
- Def 1.2: an admissible constraint is a *finite* Borel measure σ with S_σ = E, σ(E_0) > 1, finite energy on compacts.
- Thm 2.1: admissible weight w = e^{−Q} on a closed E ⊂ ℂ, admissible constraint σ: the constrained weighted energy
  V_w^σ is finite, the minimiser λ_w^σ ∈ M^σ exists and is unique, and is characterised by the inequalities (2.1)–(2.2)
  (plus parts (d), (e)).
- Thm 2.6 (saturation): if U^σ and Q are continuous on E, then S_{μ_w} ⊂ S_{λ_w^σ}, and λ = σ where μ_w ≥ σ.
- Thm 2.13 (balayage representation); Thm 3.3: zero distribution of discrete L_p-extremal polynomials for admissible
  triangular schemes on [a, b], ray sequences N/n → C > 1; Thm 3.4: Krawtchouk polynomials.
**Paper 1 says:** added an external field; for a finite constraint on a closed set proved existence, uniqueness, a
characterisation and saturation [Thms 2.1, 2.6]; applications to discrete L_p-extremal polynomials on finite
intervals [Thm 3.3].

### (KVA-PLMS) Kuijlaars–Van Assche 1999 — READ (§§1–2: Thms 1.1, 2.1, 2.2 and the remarks after them)
A. B. J. Kuijlaars, W. Van Assche, "Extremal polynomials on discrete sets", Proc. London Math. Soc. (3) 79 (1999)
191–221. Read the authors' manuscript (discrete.pdf on W. Van Assche's KU Leuven page; no journal header, so
numbering is that of the manuscript), pp. 1–6, rendered as images (the PDF has no extractable text).
- §2: E = {t_k} ⊂ [0, ∞) countable "without finite accumulation points", t_k → ∞; weighted L_p-extremal polynomials.
- Thm 2.1: for α, β, γ > 0 there are B > A ≥ 0 such that v = b_α * ω_{[A,B]} (Mellin convolution of the beta density
  αt^{α−1} on [0,1] and the arcsine density of [A,B]) solves: minimise ∬log|x−y|^{−1} + 2γ∫x^α over probability
  measures μ ≤ σ_{α,β}, dσ_{α,β}/dx = αβ^{−α}x^{α−1} on [0, ∞); F = 1/α − log((B − A)/4).
- Thm 2.2: t_k = βk^{1/α}L*(k^{1/α})(1 + o(1)), separation t_{k+1} − t_k ≥ Ck^{1/α−1}L*(k^{1/α}),
  w(x) = exp(−γx^αL(x)^α): nth-root asymptotics of the extremal norms, contracted zero distribution v, largest zero.
**Paper 1 says:** discrete sets t_k ∼ βk^{1/α} without finite accumulation points, weights exp(−γx^α); constraint
density αβ^{−α}x^{α−1}, external field γx^α, extremal measure = Mellin convolution of the beta density with an
arcsine density [Thms 2.1, 2.2]. Also: "μ* has the same structure" — μ* is the law of SY (Y ~ arc_{4c}, S = T^{−p},
T uniform), checked directly from μ* = ∫_0^1 arc_{4ct^{−p}} dt (arc_β is the law of βY/(4c)); this is our own remark.

### (KVA-JAT) Kuijlaars–Van Assche 1999 — READ (§1, Thm 1.4, Remarks 1.5–1.7)
A. B. J. Kuijlaars, W. Van Assche, "The asymptotic zero distribution of orthogonal polynomials with varying recurrence
coefficients", J. Approx. Theory 99 (1999) 167–197. Read the authors' manuscript (varrec.pdf on W. Van Assche's
KU Leuven page).
- Thm 1.4: x p_{n,N} = a_{n+1,N}p_{n+1,N} + b_{n,N}p_{n,N} + a_{n,N}p_{n−1,N} (a off-diagonal > 0, b diagonal);
  if lim_{n/N→t} a_{n,N} = a(t), lim b_{n,N} = b(t) for continuous a: (0,∞) → [0,∞), b: (0,∞) → ℝ and all t > 0,
  then lim_{n/N→t} ν(p_{n,N}) = (1/t)∫_0^t ω_{[α(s),β(s)]} ds with α = b − 2a, β = b + 2a.
**Paper 1 says:** with off-diagonal φ(r) = c r^{−p} and diagonal ψ(r) = 2c r^{−p}, the interval is [0, 4cr^{−p}] and the
t = 1 limit is μ* (heuristic remark only). Previously quoted via CCV Thm 1.3; CCV is no longer cited.

### (Be00) Beckermann 2000 — READ (§1, pp. 1–4 of the manuscript)
B. Beckermann, "On a conjecture of E. A. Rakhmanov", Constr. Approx. 16 (2000) 427–448. Read the author's manuscript
"Revised version from March 26, 99" (ano385.pdf, Lille ANO preprint; retrieved from the Internet Archive copy of the
author's page, since the live page returned an error), rendered as images.
- Thm 1.1 (summary of [DrSa97]): constrained weighted problem on closed E ⊂ ℂ, Q continuous with Q − log|z| → ∞ if E
  is unbounded, σ with connected support, |σ| > 1, continuous potentials on compacts: unique λ_w^σ, equilibrium
  condition.
- Thm 1.2 (combination of DrSa97, DaSa98, KuRa98, KuVA98): conditions (i)–(iv) on E_n, w_n ⇒ nth-root asymptotics
  and zero distribution λ_w^σ.
- Thm 1.3: relaxes conditions (iii) (separation) and (iv) (growth) of Thm 1.2, also for complex E; proves two
  conjectures of Rakhmanov [KuRa98, Conj. 2 and 3].
**Paper 1 says:** "weakened the separation and growth hypotheses of these results and extended them to complex sets"
[Thm 1.3].

### (VAVB) Van Assche–Van Baelen — READ (§§1–2)
W. Van Assche, Q. Van Baelen, "Zero distribution of orthogonal polynomials on a q-lattice", arXiv:1910.12518v1
(Constr. Approx. 54 (2021) 117–144). Read the arXiv PDF, §1 and §2.
- Orthogonality on {q^k}, 0 < q < 1; zeros x_{j,n} scaled as x_{j,n}^{1/n}; limit is the radial part of a constrained
  equilibrium problem for circularly symmetric measures on the unit disc; constraint density −1/(t log q) on [0, 1],
  σ([0,1]) = ∞.
- Thm 2.2: weights with lim (1/n²) log w(x^n) = 0 uniformly on closed subintervals of (0, 1] (no external field):
  γ_n^{1/n²} → q^{−1/2} and the scaled zeros have density −1/(t log q) on [q, 1]. Thm 2.3: with an external field Q.
**Paper 1 says:** geometric lattice {q^k} accumulating at 0, weights without external field; the constraint has
infinite mass near 0; circularly symmetric measures in the disc after x ↦ x^{1/n} [Thm 2.2].

### Not cited any more (Plan 68)
CDLO (arXiv:2608.11987; abstract only) and CCV (replaced by KVA-JAT, now read directly); Lai (arXiv:2610.06838) and
the Fauzan Zenodo record (paragraph dropped per PAPER_I_AUDIT §2.2 / decision D10).
