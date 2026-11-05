# Rule R review: Plan E2, reviewer A (analysis): E2_pgt1.md, d₂ for pure powers with p > 1

Reviewer: independent second reader (Rule R), reviewer **A**. My remit is the **analytic validity** of the proof: Lemma E2.3
(second-order Bessel/Airy corrections), Lemma E2.4, Prop E2.5 (second-order small norm), the extraction, Corollary E2.7,
labels and scope. The exact sympy values (Lemma E2.6) are re-run, not re-derived by hand; I tested them independently by
numerics that share no code with check_e2_sym.py (§1.2).
- Target: research/G1/RH/second_order/E2_pgt1.md (§§0–11, status "NOT REVIEWED", 2026-10-20), the checks check_e2_sym,
  check_e2_num, check_e2_grid, check_e2_christoffel (.py/.out).
- Context read: E_pgt1.md (Plan 65, REVIEWED), REVIEW_Plan65_A.md, REVIEW_Plan65_B.md, RH/CITATIONS.md entries (KMVV-orient,
  Paper 2), (DLMF-10.40, Paper 2), (DLMF-9, Paper 2), (DLMF-10.17, Plan 55), (DLMF-9.7.2, Plan 65), (Plan 65 reuse);
  second_order/UL.md (Thm UF-lim and the definition F_n(s) = log h_n(s) + s log n); E_p1.md Thm E1.6; E_plt1.md Thm E′.1;
  SECOND.md Thm 2.3; THEOREMS.md §4 item 13.
- I did not edit E2_pgt1.md or any other file except this report. My own scripts live in the session scratchpad; the one
  that matters most (the contour test) is reproduced in the Appendix so it can be re-run.

## Overall verdict: **ACCEPT WITH FIXES** (analysis)

I found **no error in the value of d₂ and no gap that changes the mathematics**. Theorem E2.1 is correct as stated, and
Corollary E2.7 is correct. Three fixes are required (B1–B3, all MINOR). B1 and B2 are places where a proof step is
currently a finite or numerical check that the text presents as proof. Both have short rigorous replacements, given
below. B3 is a missing reference to an already PROVED result. The other items are INFO.

Why I trust the result:
- **Lemma E2.3.** I re-derived Ξ₂ and X₂ from the DLMF quotations. The sector-independence holds term by term at every
  order (B2 gives the one-line argument). The conjugation Δ₂⁰ = (1/(4f))P₀^∞ρ^{σ₃}(σ₃Ξ₂σ₃)ρ^{−σ₃}(P₀^∞)^{−1} is the k = 2
  instance of E_pgt1's insertion: the correction sits between σ₃Lσ₃ and e^{wσ₃}, so it is conjugated by σ₃ and then by
  P₀^∞ρ^{σ₃}, and w² = 4n²f.
- **Prop E2.5.** I re-derived the second Neumann iterate, the order of factors (R₋ − I)·(J − I) (because R₊ = R₋J), the
  inside/outside boundary values for clockwise circles, and the remainder bookkeeping. All are right.
- **Independent numerics** (§1.2). I built Δ₁ and Δ₂ from closed-form integral representations, with no series and no
  code from check_e2_sym, integrated over circles of two different radii, and extracted d₂ at five (p, s) not on the grid
  (α from −0.93 to 1.46). The result matches the closed form to 10⁻²⁰. Three things the grid cannot isolate are confirmed
  by perturbation:
  - swapping the factor order to Δ₁R⁽¹⁾_in changes d₂ by 0.16 and 6.5;
  - dropping Ξ₂, X₂ or the hard-edge part of F changes it by order 1;
  - so each ingredient is actually tested by the 25/25 grid agreement.
- **Off-grid residuals at large α** (p = 2, s = 6, 7; p = 3, s = 8) stay bounded at the predicted rate n^{−ν}.

| Statement | Verdict (analysis) | Fixes |
|---|---|---|
| Thm E2.1 | ACCEPT WITH FIXES; PROVED-mod-cite once B1–B2 are applied | B1, B2 |
| Lemma E2.3 (Ξ₂, X₂, Δ₂, n-dependence) | ACCEPT WITH FIXES | B2, I8 |
| Lemma E2.4 (series of f, φ̃) | ACCEPT (re-checked by quadrature, §1.3) | I5 |
| Prop E2.5 (second-order small norm) | ACCEPT WITH FIXES | B1 |
| Lemma E2.6 (Laurent data) | ACCEPT as computation; (a) is a test, not a proof of meromorphy | B1 |
| Cor E2.7 (Christoffel function) | ACCEPT; shorter and stronger proof available | I1 |
| Rem E2.8–E2.12, §9, §10 | ACCEPT WITH FIXES | B3, I2, I3, I4, I6, I7 |
| Rule C | ACCEPT (general-k quotations cover k = 2); entry still to be written | I9 |
| Numerics | ACCEPT (all four reproduced byte-identically; NUMERICAL, not used in the proof) | — |

## 1. Re-runs and independent tests (Rule N)

Python: the session venv given in the brief, PYTHONPATH = repo src, run from checks/.

### 1.1 The authors' checks

| Script | Result |
|---|---|
| check_e2_sym.py | several minutes; output **byte-identical** to check_e2_sym.out; "ALL ASSERTIONS PASSED" |
| check_e2_num.py | **byte-identical** |
| check_e2_grid.py | from the tmp/plan62_cache coefficients, about 1 min; **byte-identical**, 25/25 |
| check_e2_christoffel.py | **byte-identical** |

The grid fits are a genuine Rule X-clean test. They fit the n⁻² coefficient from quad-precision coefficients with the
basis {n^{−1−i−jp}}, and the closed form enters only in the comparison column.

### 1.2 Reviewer tests (NUMERICAL; scripts in the session scratchpad)

**(T1) d₂ by contour integration from closed-form model data** (rev_contour.py, Appendix). The ingredients:
- φ̃ = −(1/p)(4c)^{−3/2}u³S(−u²/4c), with S evaluated as the integral 2∫₀¹t^{1/2}(1 − Et)^{−1−1/p}·₂F₁(1−a′, ½; 3/2; Et)dt
  (analytic continuation, no truncation).
- 𝔞 from 2∫₀¹t^{a′−1}arcsin(√(yt))/√(yt)dt.
- Δ₁ and Δ₂ assembled from the definitions of Lemma E2.3 with mpmath.
- A₀, A_r, B_r and R_1⁽²⁾ = −(1/2πi)∮_cw(R⁽¹⁾_inΔ₁ + Δ₂) by the trapezoid rule (96 nodes), with
  R⁽¹⁾_in = (A₀/z + A_r/(z−4c) + B_r/(z−4c)²) − Δ₁.
- Then d₂ from √((Q₁)₁₂(Q₁)₂₁)/c.

| (p, s) | α | d₂ closed form | \|d₂(T1) − closed form\|, radii (0.9c, 0.9c) | radii (1.6c, 1.7c) |
|---|---|---|---|---|
| (2.5, 2.7) | −0.32 | 0.739816666667 | 7·10⁻²¹ | 2·10⁻²¹ |
| (1.3, 4.2) | 1.46 | 1.57514299803 | 1·10⁻²⁰ | 1·10⁻²⁰ |
| (3, 1.2) | −0.93 | −0.204444444444 | 1·10⁻²⁰ | 1·10⁻²⁰ |
| (1.1, 1.7) | −0.36 | 0.24069214876 | 2·10⁻²¹ | 7·10⁻²² |
| (2, 2) | −0.5 | 0.3125 | 7·10⁻²¹ | 3·10⁻²¹ |

d₁ = −(s−1)/2 and A₀, B_r (Lemma E.5) are also reproduced to 10⁻²¹. Radius independence is a numerical test of the
meromorphy of Δ₁, Δ₂ and F on the whole discs, which a finite list of odd coefficients cannot give (B1).

**(T2) Perturbation tests (what d₂ actually depends on).** Starting from T1 at (2.5, 2.7):

| Change to the model | Effect on d₂ | What it shows |
|---|---|---|
| order of factors in F swapped to Δ₁R⁽¹⁾_in | +0.157 (and +6.51 at (1.3, 4.2)) | the factor order matters |
| Ξ₂ dropped | −0.28 | Ξ₂ is tested by the grid |
| X₂ dropped | −1.23 | X₂ is tested by the grid |
| hard-edge part of F dropped | −0.23 | the 0-disc contribution is tested by the grid |
| κ₂ perturbed (S → (1 + 0.1E)S) | changes | d₂ depends on κ₂ |
| κ₃ perturbed (S → (1 + 0.1E²)S) | changes | d₂ depends on κ₃ |
| κ₄ perturbed (S → (1 + 0.1E³)S) | unchanged to 10⁻²⁰ | d₂ does not depend on κ₄ |
| 𝔞 → (1 + 0.1)𝔞, i.e. f′(0) changed | changes | d₂ depends on f′(0) |
| 𝔞 → (1 + 0.3z)𝔞 | unchanged | d₂ does not depend on f's z² coefficient |
| 𝔞 → (1 + 0.3z²)𝔞 | unchanged | d₂ does not depend on f's z³ coefficient |

Combined with 25/25 on the grid, this means:
- the factor order of Prop E2.5 is confirmed by data;
- the normalisations of Ξ₂, X₂ and of the hard-edge term are confirmed by data;
- κ₃ is confirmed by data. My value is κ₃ = (149p² + 136p + 32)/(4480c²p²), the u⁴ coefficient of φ̃/(−κu³).

**(T3) Off-grid residuals** (rev_resid.py, cached Plan 62 coefficients). The table shows r_n := n^ν(n^pb_n/c − 1 + (s−1)/(2n)
− d₂/n²) at n = 100, 200, …, 1600:

| (p, s) | α | ν | r_n |
|---|---|---|---|
| (2, 6) | 1.5 | 3 | −3.453, −3.446, −3.442, −3.440, −3.439 |
| (2, 7) | 2 | 3 | −3.141 → −3.009 |
| (3, 8) | 4/3 | 3 | −11.23 → −11.34 |
| (1.5, 3) | 0 | 5/2 | −0.143 → −0.069 |

All are bounded, so the remainder O(n^{−ν}) and d₂ are confirmed at α ≥ 1 and off the 25-point grid.

**(T4) The n^{−1−p} term for 1 < p < 2** (rev_kappa.py). At p = 3/2 I fitted the residual after d₂ with the basis
{n^{−1−p}, n^{−3}, n^{−2−p}, n^{−1−2p}, n^{−4}} over n ∈ [160, 1600]. The leading coefficient is:

| s | fitted n^{−5/2} coefficient |
|---|---|
| 3/2 | −0.04329 |
| 2 | −0.04329 |
| 3 | −0.04329 |
| 4 | −0.04329 |
| 5 | −0.04335 |

This equals κ_p = 2p·c(p)·ζ(−p) = −0.04329, the constant of E_plt1 Thm E′.1, and it does not depend on s. See I2.

**(T5) Christoffel function by a second route** (rev_resid.py [2]). I computed λ_n(0) = 1/K_n(0, 0), where
K_n = Σ_{k<n}π_k(0)²/h_k and π_k(0) comes from the recurrence. The local slopes coincide with check_e2_christoffel (for
example −2.332632 at (3/2, 2) over [800, 1600]). This is the same data through a different algebraic route.

**(T6) Lemma E2.4 by quadrature** (rev_maps.py). At p = 1.3 and 2.5:
- μ*((0, x]) = ∫₀ˣλ_pI_{y/4c}(a′, ½)dy agrees with x^{1/2}𝔞(x) from series (i) to ≤ 3·10⁻¹⁸ at x/c = 0.3, 2, 3.5.
- φ̃₊(x) = iπ∫_x^{4c}(λ_p − ψ*) agrees with series (ii) to ≤ 2·10⁻³¹ at v/c = 0.2, 1, 2.5.

**(T7) Symbolic consistency** (rev_chain.py, sympy). SECOND Prop 3.1 ((b_n(s+p)/b_n(s))² = g_n/g_{n−1}) together with
E_pgt1 Cor E.6 (n^pg_{n−1} = c(1 + a/n + …)) predicts, at order n⁻²:

  [d₂(s+p) − d₂(s)] − [d₁(s+p)² − d₁(s)²]/2 = (p/2 − a)/2.

The closed form of Theorem E2.1 satisfies this identically in (p, s). This is a formal check: it assumes the
second-order remainders of g_n difference to O(n⁻³). It is independent of the RH computation and fixes the
s-dependence of d₂ up to a p-periodic function.

## 2. Analytic verification, item by item

### 2.1 Lemma E2.3

**Bessel coefficients.** From DLMF 10.40.1–4 with ν = α fixed:
- the relative corrections of (I_α, (i/π)K_α, πiwI′_α, −wK′_α) at order w^{−k} are
  ((−1)^ka_k, a_k, (−1)^kb_k, b_k);
- so C₂ = [[a₂, a₂], [b₂, b₂]] is right.

From 10.17.1 and 10.17.8:
- a₂ = (4α²−1)(4α²−9)/128;
- b₂ = (4α²−1)(4α²+15)/128, using the factor (4ν² + 4k² − 1) = 4α² + 15 at k = 2.

The leading matrix is exactly 𝓛 = diag((2πw)^{−1/2}, (πw/2)^{1/2})·√2M = (πw)^{−σ₃/2}M = (2πζ^{1/2})^{−σ₃/2}M. The phrase
"diagonal scalar factors absorbed" in line 76 is unnecessary (I8). Then:
- 𝓛∘C = D(M∘C) for D diagonal;
- Ξ₂ = M^{−1}(M∘C₂) = ½[[a₂+b₂, i(a₂−b₂)], [−i(a₂−b₂), a₂+b₂]], as stated;
- tr Ξ₂ = a₂ + b₂ = a₁b₁ = −det Ξ₁ = (4α²−1)(4α²+3)/64.

Structurally, Mσ₃Ξ₂σ₃M^{−1} = diag(b₂, a₂) and Mσ₃Ξ₁σ₃M^{−1} is off-diagonal (sympy, rev_struct.py). Even orders are
diagonal and odd orders off-diagonal, as they must be.

**Airy coefficients.** From DLMF 9.7.2:
- u₂ = (7·9·11)/(3·432)·u₁ = 385/10368;
- v₂ = (13/(−11))u₂ = −455/10368.

The sector-I columns are evaluated at ζ and e^{∓2πi/3}ζ. There ξ ↦ −ξ, so (−1)^ku_k/(−ξ)^k = u_k/ξ^k, and the k = 2 terms
enter both columns with the same sign. This gives X₂ = ½[[u₂+v₂, i(u₂−v₂)], [−i(u₂−v₂), u₂+v₂]] and MX₂M^{−1} = diag(u₂, v₂).
check_e2_num [1] confirms it in all four sectors.

**Hankel sectors (B2).** The write-up states that the k = 2 factors "combine … exactly as at k = 1", confirms this
numerically, and offers a "structural reason, not used". As written, the proof for these sectors is therefore numerical,
which Rule N does not allow inside a PROVED-mod-cite proof. The fix is one line valid for every k (B2). I checked both
sectors, including which Hankel function sits in which column (the same as check_e2_num's PsiB).

**Conjugation of Δ₂⁰.** In E_pgt1 the inserted object is σ₃Ψσ₃ = σ₃Lσ₃·σ₃(I + Ξ₁/w + Ξ₂/w² + …)σ₃·e^{wσ₃}. The prefactor
Ẽ_Nσ₃Lσ₃ = N W̃^{σ₃}MM^{−1} and the exponentials cancel exactly, as at first order, so no further term is generated at
order 2. Hence P̂₀(P₀^∞)^{−1} = P₀^∞ρ^{σ₃}(I + σ₃Ξ₁σ₃/w + σ₃Ξ₂σ₃/w² + O(w⁻³))ρ^{−σ₃}(P₀^∞)^{−1}, with w = 2nf^{1/2} and
w² = 4n²f. This is exactly Δ₂⁰ as stated. Consistency at k = 1 holds: 16σ₃Ξ₁σ₃/2 = Q₀, which the script asserts.

On ∂U_r: ξ = −nφ̃ and ξ⁻² = 1/(n²φ̃²), and the (−ω)^{∓σ₃/2} conjugation is the same as at k = 1.

**Hypotheses.**
- ν = α > −1 fixed (α ≥ 1 allowed): DLMF imposes no restriction (CITATIONS "(Plan 65 reuse)" hypothesis check).
- Sectors: |ph w| < π/3; ph 2(−ζ)^{1/2} ∈ (−π/6, π/6); |ph| ≤ π − δ for the Airy arguments.
- |w| ≍ n and |ξ| ≍ n uniformly on the circles, so the three-term remainders are O(n⁻³) uniformly.

All are satisfied.

**n-dependence.** Δ₂ depends on n only through ω (via ρ and (−ω)^{1/2}), smoothly, with bounds above and below. So
Δ₂ − Δ₂^{mod} = O(n^{−p}) follows from E_pgt1's ω/ω^{mod} = 1 + O(n^{−p}) (Lemma E.2 with the A1 domain fix of Plan 65).
Correct.

### 2.2 Lemma E2.4

**(i).** The binomial series and termwise integration are correct. The radius is 4c, and f, 𝔞 are analytic in
|z| < 4c (Paper 2 Lemma signs(iii)). With (4c)^{−a′}/(pB_p) = (4c)^{−1/2}(4c)^{−1/p}/(pB_p) = (4c)^{−1/2}/(pπ), (i) follows.

**(ii).**
- 1 − I_{1−e}(a′, ½) = (1/B_p)∫₀^e(1−τ)^{a′−1}τ^{−1/2}dτ, and binomial expansion gives the k-series.
- (1 − e)^{−1−1/p} gives the m-series.
- The integration in e produces 1/((k+½)(k+m+3/2)). The sign chain iπ·(1/(pπ))·(iu³/(4c)^{3/2}) = −u³/(p(4c)^{3/2}) is right.
- S(0) = 4/3 and the e¹ coefficient 14/15 + 8/(15p) are right.

Confirmed by T6.

### 2.3 Prop E2.5 (second-order small norm)

**Neumann iteration.** With W := J − I on Σ_R:
- R₋ = I + 𝒞₋(R₋W), so R₋ − I = 𝒞₋W + 𝒞₋((𝒞₋W)W) + 𝒞₋((R₋ − I − 𝒞₋W)W).
- The last term is O(‖W‖_∞²‖W‖₂) = O(n⁻³) in L², using ‖𝒞₋‖ ≤ C (Paper 2 F1).
- Then R − I = 𝒞(R₋W) = 𝒞W + 𝒞((𝒞₋W)W) + O(n⁻³) uniformly at distance d (Cauchy–Schwarz).
- Because R₊ = R₋J, R₋ multiplies W **on the left**, so the n⁻² integrand is R⁽¹⁾_inΔ₁ + Δ₂, as stated. T2 shows the
  other order is excluded by the data.

**Boundary values.**
- Clockwise circles: the left of the direction of travel is the outside, so + = outside and − = inside.
- For z outside, (1/2πi)∮_cw Δ(s)ds/(s − z) = −Σ_e Res_e[Δ(s)/(s−z)] = PP_e(z), using Res_e[PP(s)/(s−z)] = −PP(z).
- For z inside a disc, the extra residue Δ(z) at s = z gives PP(z) − Δ(z) = R⁽¹⁾_in(z), which is continuous up to the
  circle.
- So 𝒞₋(Δ₁^{mod}χ_circ) = R⁽¹⁾_in on the circles. Correct.
- Cross-disc terms are included: R⁽¹⁾_in on ∂U_0 contains A_r/(z−4c) + B_r/(z−4c)².
- Contributions of the far pieces to 𝒞₋W on the circles are O(e^{−n/C}).

**Moment.** R_1 = −(1/2πi)∫R₋W, so R_1⁽²⁾ = −(1/2πi)∮_cw F = Σ_e Res_e F. Correct.

**Remainder bookkeeping.**

| Source | Order |
|---|---|
| Δ₁ − Δ₁^{mod} in the first iterate | n^{−1−p} |
| the same inside R⁽¹⁾_in in the second iterate | n^{−2−p} |
| Δ₂ − Δ₂^{mod} | n^{−2−p} |
| (Δ₂/n²)·(Δ₁/n) cross terms | n⁻³ |
| model remainders | n⁻³ |
| third iterate | n⁻³ |
| non-circle pieces | e^{−n/C}, n^{−pn/4}, n^{−K} |

The total is O(n^{−min(3, 1+p)}).
- The O(n^{−p}) replacement in Δ₁ really enters only at n^{−1−p}: it multiplies 1/n in the first iterate.
- In the second iterate it appears only at n^{−2−p}.
- For p ∈ (1, 2) the bound is sharp: T4 finds a nonzero n^{−1−p} coefficient.

**Meromorphy (B1).** The residue evaluation needs Δ₂^{mod} and F to be meromorphic on all of U_0 and U_r, not merely to
have a finite Laurent jet. Lemma E2.6(a) checks that the odd coefficients of u⁷Δ₂^r, v⁴Δ₂⁰ vanish only up to a finite
order, so it is a test, not a proof (B1). T1's radius independence supports the claim numerically. The same reasoning
was accepted for Δ₁ in Plan 65; it is cleaner to close it now for every k.

### 2.4 Extraction (Theorem E2.1)

- Q₁ = P₁ + R_1 with P₁ = [[0, ic], [−ic, 0]] is exact (P₀^∞ is weight- and n-free; invariance lemma F8).
- The b-functional √((Q₁)₁₂(Q₁)₂₁)/c expanded to second order is
  d₂ = x₂/2 − x₁²/8, x₁ = i(A₂₁ − A₁₂)/c, x₂ = (A₁₂A₂₁ + ic((R_1⁽²⁾)₂₁ − (R_1⁽²⁾)₁₂))/c².
  I implemented this independently in T1, and it reproduces the closed form.
- The positive root is legitimate: (Q₁)₁₂(Q₁)₂₁ → c² > 0.

The two forms of d₂ in Theorem E2.1 agree (sympy). At p = 2 they give (s² + 6s − 11)/16, which matches SECOND Thm 2.3.

### 2.5 Corollary E2.7

**(a) Identity.**
- min{cᵀH_nc : c₀ = 1} = 1/(H_n^{−1})₀₀ = det H_n/det(m_{i+j})_{1≤i,j≤n−1}.
- The minor is the order-(n−1) Hankel matrix of x²σ.
- x²σ_{p,s} has weights k^{−s−2p} at k^{−p}, i.e. σ_{p,s+2p}.

Correct.

**(b) Expansions.**
- log(b_i/b_i″) = p/i + δ′/i² + O(i^{−ν}).
- Σ_{i≤j} gives 2p(log j + γ_E + 1/(2j)) + 2δ′(ζ(2) − 1/j) + const − Σ_{i>j}O(i^{−ν}), and the last sum is O(j^{1−ν}).
- That K must equal −2 log c is forced: the (n−2)K term has to cancel the 2(n−1)log c of log h_{n−1}.
- UF-lim gives it exactly. UL's F_n = log h_n + s log n, so h_n(s)/h_n(s+2p) = c^{−2}n^{2p}(1 + o(1)).

**(c) Summation.**
- −2p log(n−1)! + 2p log(n−2)! = −2p log(n−1).
- Σ_{j≤n−2}(p − 2δ′)/j = (p − 2δ′)log n + O(1).
- Σ O(j^{1−ν}) converges since ν > 2.

**Exponent.** I re-derived δ′ = (s−1)/p − p/2 and γ = −(p+2)(s−1)/p by hand, and sympy agrees.

The corollary is correct, but it does not need Theorem E2.1 or UF-lim (I1).

### 2.6 Remarks and scope

- Rem E2.8: (1 + (s−1)/(2pn))^{−p} = 1 − (s−1)/(2n) + (p+1)(s−1)²/(8pn²) + … ✓.
- Rem E2.11: the s² coefficient of d₂ is (p² − 2)/(8p²) ✓. ∂_s²log h_n ≈ (2/n)(¼ − ∂_s²d₂) = 1/(p²n) ✓ (formally). The
  check_so_convex.out second *divided* differences at n = 1600 are 1/(2p²n) to 4 digits for every p on the grid
  (7.8127·10⁻⁵ vs 7.8125·10⁻⁵ at p = 2; 3.4740·10⁻⁵ vs 3.4722·10⁻⁵ at p = 3). The HEURISTIC label is right.
- Rem E2.10 (p = 1): see B3.
- Rem E2.12: see I6.

## 3. Rule C spot-check

The quotations in RH/CITATIONS.md used here are general in k, which covers every instance at k = 2:
- 10.17.1 (a_k), 10.17.8 (b_k with (4ν² + 4k² − 1));
- 9.7.2 (u_k recursion, v_k = ((6k+1)/(1−6k))u_k);
- 10.40.1–4, 10.17.5–6, 10.17.11–12 and 9.7.5–6 (full series, sectors, "ν fixed").

The hypotheses (ν = α > −1 fixed; the sectors listed in §2.1) are checked in E_pgt1/CITATIONS "(Plan 65 reuse)" and are
unchanged at k = 2. Nothing new was read, so no new external source is needed. The "(Plan E2 reuse)" entry announced in §11
is not yet written (I9).

## 4. Findings and required fixes

**B1 (MINOR; a proof step is a finite check).** Lemma E2.6(a), and with it the residue evaluation in Prop E2.5, infer that
Δ₂^{mod} (and F) is meromorphic on the discs from the vanishing of finitely many odd coefficients of u⁷Δ₂^r and v⁴Δ₂⁰.
That establishes a finite Laurent jet. It does not exclude a cut inside the disc, which would make the circle integral
differ from Σ Res. The same reasoning stood for Δ₁ in E_pgt1. Replace it by a proof valid for every k. Either:
- *(Structural.)* E := P̂(P₀^∞)^{−1} (model weight) satisfies E₊ = E₋ exactly on the band inside the disc, because P̂ and
  P₀^∞ have the same band jump. On the negative axis and the lips inside U ∖ {e}, its jump is I + O(e^{−n/C}) on compacts.
  The expansion E = I + Σ_{k≤2}Δ_kn^{−k} + O(n⁻³) holds on compacts of U ∖ {e} from both sides. Asymptotic coefficients
  are unique, so Δ_{k,+} = Δ_{k,−} on every contour piece in U ∖ {e}. Hence Δ_k is analytic in U ∖ {e} with
  |Δ_k| = O(|z − e|^{−m}), so it is meromorphic. F is then meromorphic, since R⁽¹⁾_in is analytic.
- *(Algebraic.)* Verify the band jump cancellation of the formula directly, using φ̃₊ = −φ̃₋, (f^{1/2})₊ = −(f^{1/2})₋, the
  jump of P₀^∞, the relation between the boundary values of (−ω)^{1/2} (resp. ρ), and the parity "MX_kM^{−1} diagonal for
  even k, off-diagonal for odd k" (§2.1).

Keep the coefficient check as the Rule A test it is. T1's radius independence can be cited as NUMERICAL support.

**B2 (MINOR; the Hankel-sector step is numerical as written).** In Lemma E2.3, "Bessel, 2π/3 < ±arg ζ < π" rests on
"combine … exactly as at k = 1" plus check_e2_num. Replace it with the all-orders identity:
- for 2π/3 < arg ζ < π, 2(−ζ)^{1/2} = −iw, so the 10.17.5 term is i^ka_k/(−iw)^k = (−1)^ka_k/w^k (the I_α pattern) and the
  10.17.6 term is (−i)^ka_k/(−iw)^k = a_k/w^k (the K_α pattern);
- likewise 10.17.11–12 give (−1)^kb_k/w^k and b_k/w^k after the i, −i prefactors and the chain-rule factor;
- for −π < arg ζ < −2π/3, 2(−ζ)^{1/2} = +iw and the roles of H⁽¹⁾ and H⁽²⁾ swap, matching KMVV (6.25)'s column order;
- the k-independent constant factors of KMVV (6.24)–(6.25) are those already checked at k = 0, 1 (E_pgt1).

So C_k, and hence Ξ_k, is the same in all three sectors for every k. Add the analogous sentence for the Airy sectors
(ξ ↦ −ξ at e^{∓2πi/3}ζ gives (−1)^ku_k/(−ξ)^k = u_k/ξ^k). Then the "structural reason" can be dropped, or stated as an
alternative with the uniqueness of formal solutions made precise.

**B3 (MINOR; a missing PROVED anchor).** Remark E2.10 conjectures n b_n/c(1) = 1 − (s−1)/(2n) + (d₂(1, s) − 1/12)/n² + o(n⁻²)
at p = 1 on NUMERICAL grounds. E_p1 Theorem E1.6 (PROVED-mod-cite, REVIEWED) already gives d₂(1, 3/2) = 5/96 and
d₂(1, 5/2) = 53/96. The conjectured formula gives exactly these: d₂(1, 3/2) − 1/12 = 13/96 − 8/96 and
d₂(1, 5/2) − 1/12 = 61/96 − 8/96.
- *Fix:* state that the conjecture is PROVED at s ∈ {3/2, 5/2} (E_p1 Thm E1.6) and is CONJECTURE (NUMERICAL) elsewhere.
- Optionally note that Paper II §13.1's (1, 3/2) and (1, 5/2) cases fit the p = 1 formula.

**I1 (INFO, recommended; stronger and shorter proof of Cor E2.7).** The exponent of λ_n(0) is first-order information. With
K_n(0, 0) = Σ_{k<n}π_k(0)²/h_k = 1/λ_n(0):
- π_{k+1}(0) = −g_kπ_k(0) and h_{k+1}/h_k = b_{k+1}²;
- so the ratio of consecutive terms is t_{k+1}/t_k = g_k²/b_{k+1}² = 1 + 2(a − d₁)/(k+1) + O(k⁻²), using E_pgt1 Cor E.6
  (n^pg_{n−1} = c(1 + a/n + O(n⁻²))) and Thm E.1;
- hence t_k = C′k^{2(a−d₁)}(1 + O(1/k)), and since 2(a − d₁) + 1 = (p+2)(s−1)/p > 0, K_n = C″n^{(p+2)(s−1)/p}(1 + O(n^{−θ}))
  with θ = min(1, (p+2)(s−1)/p).

So λ_n(0) = C n^{−(p+2)(s−1)/p}(1 + O(n^{−θ})), PROVED-mod-cite from E_pgt1 alone (REVIEWED). It needs neither Thm E2.1 nor
UL UF-lim, and it gives a rate. The present proof is correct. Recommendation: either switch to this proof, or add it and
relabel Cor E2.7's dependence. Calling it a "Corollary of Thm E2.1" overstates what it uses. T5 confirms numerically that
both routes give identical λ_n.

**I2 (INFO; the n^{−1−p} term is κ_p).** At p = 3/2 the n^{−1−p} coefficient of n^pb_n/c equals κ_p = 2p·c(p)ζ(−p) to 4
digits, independently of s ∈ {3/2, …, 5} (T4). Consequences:
- the remainder O(n^{−1−p}) of Theorem E2.1 is sharp for 1 < p < 2;
- the E_plt1 term κ_pn^{−1−p} continues to p > 1;
- at p = 1 it merges with n⁻², which is exactly Remark E2.10's −1/12 = κ₁;
- at p = 2, κ₂ = 4c·ζ(−2) = 0, consistent with H_n being exactly constant (E_pgt1 Remark E.2(3)).

Suggest a CONJECTURE remark: for 1 < p < 2, n^pb_n/c = 1 + d₁/n + d₂/n² + κ_pn^{−1−p} + o(n^{−1−p}). It also gives a natural
route to proving it: the O(n^{−p}) part of H_n inserted into Δ₁. Add it to the §9 Open list.

**I3 (INFO; scope of the opening claim).** Lines 4–6 say the file closes THEOREMS §4 item 13's GAP "the n^{−1−2p} coefficient
and d₂ (p ≠ 1, 2)". It closes only the d₂ part, and only for p > 1. The n^{−1−2p} coefficient (p < 1), d₂ for p < 1, and
the n^{−1−p} coefficient for 1 < p < 2 (I2) remain open. §9 says this correctly; make the opening sentence and the §11
integration text match.

**I4 (INFO; what the c-independence tests).** "c is a free symbol … non-trivial internal check since c(p) is transcendental"
(§1, §10) misdescribes the check. Under z ↦ λz all model data are homogeneous, so a correct computation is automatically
c-free whatever c is. The check detects inhomogeneous slips (for example a wrong power of 4c), not number-theoretic
coincidences. Rephrase.

**I5 (INFO; dependence record and truncation claim).** By T2, d₂ depends on f′(0), κ₂ and κ₃, and not on κ₄ or on f's z²
and z³ coefficients. §10's "u-series to u⁶ for Δ₁^r (κ up to κ₄)" is more than is needed (harmless). Suggest a remark in the
style of E_pgt1 §5 "what the constants depend on", recording κ₃ = (149p² + 136p + 32)/(4480c²p²) (sympy from Lemma E2.4(ii)).

**I6 (INFO; Remark E2.12 wording).**
- The CG statement should read "the **squared** A-norm error after n − 1 steps equals λ_n(0; σ_{p,s})" (CG minimises
  Σλ_k|c_k|²R(λ_k)² over deg R ≤ n − 1, R(0) = 1). Both rates quoted are for the squared norm.
- The fixed-step comparison Σk^{−s}(1 − k^{−p})^{2n} ≍ n^{−(s−1)/p} is right for the squared norm.

**I7 (INFO; bookkeeping).**
- The label table says "Rem E2.8–E2.11" but lists five items, and Remark E2.12 exists: renumber.
- Remark E2.9's "d₂(2, s) for every s > 1" is a specialisation of Theorem E2.1 (PROVED-mod-cite), not NUMERICAL/HEURISTIC.
- check_e2_sym.py's docstring cites a non-existent "check_e2_coef"; it means check_e2_num.

**I8 (INFO; Lemma E2.3 line 76).** Replace "(diagonal scalar factors absorbed as in E_pgt1 (E.3.1))" with the exact identity
𝓛 = diag((2πw)^{−1/2}, (πw/2)^{1/2})·√2M = (2πζ^{1/2})^{−σ₃/2}M. This is how the factor (2πζ^{1/2})^{−σ₃/2} arises, and it
makes 𝓛∘C = (2πζ^{1/2})^{−σ₃/2}(M∘C) immediate.

**I9 (INFO; Rule C).** Write the "(Plan E2 reuse)" CITATIONS entry before integration, listing the k = 2 uses and the
hypothesis check (ν = α fixed; the sectors of §2.1). Harmonise the citation lists of the Thm E2.1 and Lemma E2.3 rows in
the label table: the theorem row omits 10.40.1–4, 10.17.5–6, 10.17.11–12 and 9.7.5–6, which the proof uses.

## 5. Things I tried to break (Rule A, reviewer side)

- **Wrong factor order or wrong side.** Swapping to Δ₁R⁽¹⁾_in, or using R⁽¹⁾_out instead of R⁽¹⁾_in, would change d₂ by order
  1 (T2). The grid would have caught it, and it does not.
- **Sign of b₂ or of the k = 2 Hankel factor.** A sign error in Ξ₂ or X₂ would shift d₂ by about 0.3 to 1 (T2: dropping
  them shifts by 0.28 and 1.23). check_e2_num independently fixes both matrices to 10⁻⁶ in all sectors.
- **A hidden cut in Δ₂ or F inside the discs.** Contour integrals at two radii agree to 10⁻²⁰ (T1). See B1 for the proof.
- **α ≥ 1, α near −1.** T1 at α = 1.46 and −0.93, and T3 at α = 1.5, 2, 4/3, agree.
- **Could the H_n correction enter at n⁻²?** Only through Δ₁ at n^{−1}·n^{−p}. T4 shows it is present exactly at n^{−1−p} for
  p = 3/2, and κ₂ = 0 at p = 2 (I2). No n⁻² leak.
- **The c(p) cancellation in Cor E2.7.** K = −2 log c is forced by the linear-in-n terms and supplied by UF-lim. It is
  independently unnecessary in the I1 route.
- **Rule X.** The grid fits do not use the closed form; T1 uses no code or series from check_e2_sym; T3 uses
  (p, s) not on the authors' grid.

**Bottom line (analysis):** Theorem E2.1 and Corollary E2.7 are correct and, once B1–B3 are applied, correctly proved modulo
the cited inputs. B1 and B2 replace a finite or numerical step by a short all-orders argument; B3 adds a proved anchor. None
changes a formula. Reviewer B's re-derivation of the Lemma E2.6 algebra is still needed for REVIEWED.

## Appendix: reviewer contour test (rev_contour.py, abridged to the computational core)

```python
import mpmath as mp; mp.mp.dps = 20; I = mp.mpc(0, 1)
mat = lambda a, b, c_, d: mp.matrix([[a, b], [c_, d]])
T = mat(1, 1, I, -I) / mp.sqrt(2); Ti = T ** -1; s3 = mat(1, 0, 0, -1)
def run(p, s, N=96, radii=((0.9, 0.9), (1.6, 1.7))):
    p = mp.mpf(p); s = mp.mpf(s); al = (s - 1 - p) / p; ap = 1 / p + mp.mpf(1) / 2
    Ip = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + 0.5) / mp.gamma(1 / p + 1); c = (mp.pi / (2 * Ip)) ** p / 4
    u1, v1, u2, v2 = mp.mpf(5)/72, -mp.mpf(7)/72, mp.mpf(385)/10368, -mp.mpf(455)/10368
    X1 = mat((u1+v1)/2, I*(v1-u1)/2, I*(v1-u1)/2, -(u1+v1)/2); X2 = mat((u2+v2)/2, I*(u2-v2)/2, -I*(u2-v2)/2, (u2+v2)/2)
    a1, b1 = (4*al**2-1)/8, (4*al**2+3)/8; a2, b2 = (4*al**2-1)*(4*al**2-9)/128, (4*al**2-1)*(4*al**2+15)/128
    Xi1 = mat(-(a1+b1), I*(a1-b1), I*(a1-b1), a1+b1)/2; Xi2 = mat(a2+b2, I*(a2-b2), -I*(a2-b2), a2+b2)/2
    S = lambda E: 2*mp.quad(lambda t: mp.sqrt(t)*(1-E*t)**(-1-1/p)*mp.hyp2f1(1-ap, 0.5, 1.5, E*t), [0, 1])
    def frak_a(z):
        y = z/(4*c); g = lambda t: mp.asin(mp.sqrt(y*t))/mp.sqrt(y*t) if t > 0 else mp.mpf(1)
        return (4*c)**-0.5/(p*mp.pi)*2*mp.quad(lambda t: t**(ap-1)*g(t), [0, 1])
    def conjP(Z, A2):  # P0inf Z P0inf^{-1}, P0inf = T a^{s3} T^{-1}, A2 = a^2
        Y = Ti*Z*T; return T*mat(Y[0,0], A2*Y[0,1], Y[1,0]/A2, Y[1,1])*Ti
    def soft(z):
        u = mp.sqrt(z-4*c); zh = mp.sqrt(z); phit = -(1/p)*(4*c)**mp.mpf(-1.5)*u**3*S(-u**2/(4*c))
        mw = (2*mp.sqrt(c)/(zh+u))**(2+2*al)
        D = lambda X: conjP(mat(X[0,0], X[0,1]/mw, X[1,0]*mw, X[1,1]), u/zh)
        return -D(X1)/phit, D(X2)/phit**2
    def hard(z):
        v = mp.sqrt(-z); fh = v*mp.pi/2*frak_a(z); rho = (v/(2*mp.sqrt(c))+mp.sqrt(1+v**2/(4*c)))**(al+1)
        def D(X):
            Q = s3*X*s3; return conjP(mat(Q[0,0], rho**2*Q[0,1], Q[1,0]/rho**2, Q[1,1]), mp.sqrt(4*c-z)/v)
        return D(Xi1)/(2*fh), D(Xi2)/(4*fh**2)
    for rd, rr in radii:
        p0 = [rd*c*mp.expj(2*mp.pi*(k+.5)/N) for k in range(N)]; pr = [4*c+rr*c*mp.expj(2*mp.pi*(k+.5)/N) for k in range(N)]
        H = [hard(z) for z in p0]; Sf = [soft(z) for z in pr]
        ci = lambda V, P, e, fn: sum((fn(x, z)*(z-e) for x, z in zip(V, P)), mp.zeros(2, 2))/N  # (1/2πi)∮_ccw
        A0 = ci(H, p0, 0, lambda D, z: D[0]); Ar = ci(Sf, pr, 4*c, lambda D, z: D[0])
        Br = ci(Sf, pr, 4*c, lambda D, z: D[0]*(z-4*c)); PP = lambda z: A0/z + Ar/(z-4*c) + Br/(z-4*c)**2
        R12 = sum((ci(V, P, e, lambda D, z: (PP(z)-D[0])*D[0] + D[1]) for V, P, e in ((H, p0, 0), (Sf, pr, 4*c))), mp.zeros(2, 2))
        A = A0 + Ar; x1 = I*(A[1,0]-A[0,1])/c; x2 = (A[0,1]*A[1,0] + I*c*(R12[1,0]-R12[0,1]))/c**2
        print(p, s, rd, rr, "d1 =", mp.nstr(x1/2, 12), "d2 =", mp.nstr(x2/2 - x1**2/8, 12))
```
