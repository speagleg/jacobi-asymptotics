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
