# E2_pgt1: the second-order coefficient d₂ for pure powers, p > 1, by third-order Riemann–Hilbert analysis (Plan E2)

Status (2026-10-20): written by the Plan E2 agent; **NOT REVIEWED (Rule R pending)**. Labels per VERIFICATION_POLICY.md.
"RH" means Riemann–Hilbert throughout. This file extends E_pgt1.md (Plan 65, REVIEWED) by one order. It closes, for p > 1,
the GAP "d₂ (second order)" of E_pgt1 §9 and THEOREMS §4 item 13 ("the n^{−1−2p} coefficient and d₂ (p ≠ 1, 2)"), and the
"coefficient of n⁻² … known only in the cases (1, 3/2), (1, 5/2), (2, 2)" of Paper II §13.1, for every p > 1, s > 1.

**Summary of labels.**

| # | Statement | Label |
|---|---|---|
| Thm E2.1 | p > 1, s > 1: n^pb_n/c(p) = 1 − (s−1)/(2n) + d₂/n² + O(n^{−ν}), ν := min(3, 1+p), with d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12 | PROVED-mod-cite (E_pgt1 inputs [REVIEWED]; DLMF 10.17.1, 10.17.8, 9.7.2 at k = 2, as quoted in RH/CITATIONS.md) + exact computer algebra (check_e2_sym) |
| Lemma E2.3 | jumps on the two circles to third order: I + Δ₁/n + Δ₂/n² + O(n⁻³), Δ₂ explicit (second corrections of the Bessel and Airy models); Δ_k = Δ_k^{mod} + O(n^{−p}) | PROVED-mod-cite (as E_pgt1 Lemma E.3, with the k = 2 terms of DLMF 10.40.1–4, 10.17.5–6, .11–.12, 9.7.5–6) |
| Lemma E2.4 | full convergent series of the local maps f (at 0) and φ̃ (at 4c) | PROVED (from G2's μ*, as E_pgt1 Lemma E.4) |
| Prop E2.5 | R = I + R⁽¹⁾/n + R⁽²⁾/n² + O(n^{−ν}); R_1⁽²⁾ = Σ_{e∈{0,4c}} Res_e(R⁽¹⁾_in Δ₁^{mod} + Δ₂^{mod}) | PROVED-mod-cite (RH_px §5, Paper 2 Prop. frame F1, F5, as E_pgt1 Prop. E.5′) |
| Lemma E2.6 | Δ₂^{mod} is meromorphic in both discs; the Laurent data and R_1⁽²⁾ | PROVED (exact sympy, check_e2_sym.py, all assertions pass) |
| Cor E2.7 | Christoffel function at the hard edge: λ_n(0; σ_{p,s}) = C n^{−(p+2)(s−1)/p}(1 + o(1)), C = C(p, s) > 0 (p > 1, s > 1) | PROVED-mod-cite (Thm E2.1 at s and s + 2p, Thm E.1, UL Thm UF-lim [REVIEWED]) |
| Rem E2.8–E2.11 | index-shift form; p = 2 for all s; p = 1 with κ₁ = −1/12; the s² coefficient and Conjecture III-8.1; CG reading of Cor E2.7 | NUMERICAL / HEURISTIC as marked |

Numerical cross-checks (NUMERICAL, not used in the proofs): `checks/check_e2_grid.out` (d₂ fitted from the Plan 62
quad-precision coefficients, p ∈ {1, 3/2, 2, 3, 4} × s ∈ {3/2, 2, 3, 4, 5}: 25/25 agree with the closed form within 3× the
fit half-range; at p = 1 with the extra −1/12 of Remark E2.10), `checks/check_e2_num.out` (second-order Airy and Bessel
correction matrices X₂, Ξ₂ in all sectors), `checks/check_e2_christoffel.out` (exponent of Cor E2.7 at four (p, s)).

Novelty: UNCHECKED (Rule L not done; see §9).

## 0. Setting and conventions

As E_pgt1 §0: σ = σ_{p,s}, **p > 1**, s > 1, α = (s−1−p)/p > −1, c = c(p), the Q-frame of Paper 2, P₀^∞ = T𝔞_∞^{σ₃}T^{−1},
M = [[1, i], [i, 1]]/√2, the extraction (Q₁)₁₂(Q₁)₂₁ = n^{2p}b_n², and the error matrix R with clockwise circles, R₊ (outside)
= R₋ (inside)·J. Put **ν := min(3, 1 + p)** (> 2). Throughout, "mod" means computed for the model weight z^α(4c − z) (band
factor H_n replaced by a constant), as in E_pgt1 Lemma E.3.

## 1. Main result

**Theorem E2.1 (PROVED-mod-cite; inputs listed in the table).** Let p > 1 and s > 1. Then, as n → ∞,

  n^pb_n/c(p) = 1 − (s−1)/(2n) + d₂(p, s)/n² + O(n^{−min(3, 1+p)}),

  d₂(p, s) = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12
           = −[p³ + 7p² + 12p + 6 − 12(p+1)s + (6 − 3p²)s²]/(24p²).

At p = 2 this is (s² + 6s − 11)/16, the value of SECOND Thm 2.3 (proved there for s ∈ {2, 4, 6, 8, 10} by exact Lommel
chains); Theorem E2.1 gives it for every s > 1, with remainder O(n⁻³).

The proof occupies §§2–7. Mechanism: exactly as at first order (E_pgt1 §1), the only O(n⁻²) sources are the circles around
0 and 4c. There, the jump is I + Δ₁/n + Δ₂/n² + O(n⁻³) with Δ₂ built from the second asymptotic coefficients of the Bessel
and Airy functions, and the band factor H_n enters only through Δ₁, at order n^{−1}·n^{−p} = n^{−1−p} = o(n⁻²) (E_pgt1 Lemma
E.2). The second-order small-norm term is the sum of the principal parts of R⁽¹⁾_inΔ₁ + Δ₂ at 0 and 4c. Everything is then
an exact Laurent computation in closed form, carried out symbolically in p and α with c kept as a free symbol: the
result is independent of c, which is a non-trivial internal check since c(p) is transcendental.

## 2. Lemma E2.2: the band factor (no change)

E_pgt1 Lemma E.2 is used as is: log H_n(z) − log H_n(1) = O(n^{−p}) with one derivative, uniformly near both circles and the
points where they meet [0, 4c]. (At p = 2, H_n is exactly constant: E_pgt1 Remark E.2(3).)

## 3. Lemma E2.3: the jumps on the two circles to third order

**Lemma E2.3 (PROVED-mod-cite).** Uniformly on the circles ∂U_0, ∂U_r (boundary values where they cross the contour),

  P̂₀(P₀^∞)^{−1} = I + Δ₁⁰/n + Δ₂⁰/n² + O(n⁻³),   P̂_r(P₀^∞)^{−1} = I + Δ₁^r/n + Δ₂^r/n² + O(n⁻³),

with Δ₁⁰, Δ₁^r as in E_pgt1 Lemma E.3 and

  Δ₂⁰ := (1/(4f)) P₀^∞ ρ^{σ₃} (σ₃Ξ₂σ₃) ρ^{−σ₃}(P₀^∞)^{−1},   Ξ₂ := ½[[a₂ + b₂, i(a₂ − b₂)], [−i(a₂ − b₂), a₂ + b₂]],
  Δ₂^r := (1/φ̃²) P₀^∞ (−ω)^{−σ₃/2} X₂ (−ω)^{σ₃/2}(P₀^∞)^{−1},   X₂ := ½[[u₂ + v₂, i(u₂ − v₂)], [−i(u₂ − v₂), u₂ + v₂]],

where a₂ = (4α² − 1)(4α² − 9)/128, b₂ = (4α² − 1)(4α² + 15)/128 (DLMF 10.17.1, 10.17.8 at k = 2, ν = α) and u₂ = 385/10368,
v₂ = −455/10368 (DLMF 9.7.2 at k = 2). Moreover Δ_k^⋄ = Δ_k^{⋄,mod} + O(n^{−p}) (k = 1, 2; ⋄ ∈ {0, r}).

*Proof.* *Bessel, |arg ζ| < 2π/3.* With w = 2ζ^{1/2} and KMVV (6.23), DLMF 10.40.1–10.40.4 to three terms (relative errors
O(w⁻³), |ph w| < π/3) give, entrywise, Ψe^{−wσ₃} = 𝓛∘(𝟙 + C₁/w + C₂/w² + O(w⁻³)) with 𝓛 the leading matrix,
C₁ = [[−a₁, a₁], [−b₁, b₁]], C₂ = [[a₂, a₂], [b₂, b₂]] (∘ = entrywise product; the signs are (−1)^k for I_α, I_α′ and +1 for
K_α, −K_α′). Since 𝓛 = diag((2πw)^{−1/2}, (2πw)^{1/2}/2)·√2M = (2πζ^{1/2})^{−σ₃/2}M·(diagonal scalar factors absorbed as in
E_pgt1 (E.3.1)), 𝓛∘C = diag(…)√2(M∘C), and

  Ψe^{−wσ₃} = (2πζ^{1/2})^{−σ₃/2} M [I + Ξ₁/w + Ξ₂/w² + O(w⁻³)],  Ξ_k := M^{−1}(M∘C_k).

For k = 1 this is E_pgt1 (E.3.1) (Ξ₁/w = [[−(1+4α²), −2i], [−2i, 1+4α²]]/(16ζ^{1/2})); for k = 2 it is the Ξ₂ above.
Consistency: det(I + Ξ₁/w + Ξ₂/w²) = 1 + O(w⁻³) (det Ψ is constant) requires tr Ξ₂ = −det Ξ₁, i.e. a₂ + b₂ = a₁b₁, which holds
identically (both equal (4α² − 1)(4α² + 3)/64); asserted in check_e2_sym.py.
*Bessel, 2π/3 < ±arg ζ < π.* The same computation with DLMF 10.17.5, 10.17.6, 10.17.11, 10.17.12 to three terms (ph 2(−ζ)^{1/2} ∈
(−π/6, π/6), the sectors checked in E_pgt1 Lemma E.3 and RH/CITATIONS "(Plan 65 reuse)") gives the same Ξ₂: the factors i^k,
(−i)^k of 10.17.5–6/11–12 combine with the phases of KMVV (6.24)–(6.25) exactly as at k = 1. This is confirmed numerically in
all sectors (check_e2_num.out [2]: the error of w²(M^{−1}(2πζ^{1/2})^{σ₃/2}Ψe^{−wσ₃} − I − Ξ₁/w) − Ξ₂ halves when |ζ| is
multiplied by 4, at α = 0.3, −0.6 and six arguments). (Structural reason, not used: the formal solution of the Bessel
model's ODE of the form L(I + Σ_kΞ_kw^{−k})e^{wσ₃} with this L is unique, so its coefficients cannot depend on the sector.)
Inserting into P₀ as in E_pgt1 Lemma E.3 (σ₃Ψσ₃ conjugates each correction; w = 2nf^{1/2}, so Ξ₂/w² = Ξ₂/(4n²f)) gives the
first claim; the O(n⁻³) is uniform on ∂U_0 because |w| ≍ n there and P₀^∞, ρ^{±1} are bounded uniformly in n.
*Airy.* DLMF 9.7.5–9.7.6 to three terms give, in sector I, y₊ ∝ ζ^{−σ₃/4}(1 + u₁/ξ + u₂/ξ², 1 + v₁/ξ + v₂/ξ²)ᵀ and
y₀ ∝ ζ^{−σ₃/4}(1 − u₁/ξ + u₂/ξ², −(1 − v₁/ξ + v₂/ξ²))ᵀ (relative errors O(ξ⁻³)), so Ψ^I = ζ^{−σ₃/4}M(I + X₁/ξ + X₂/ξ² +
O(ξ⁻³))e^{ξσ₃} with X₁ = X of E_pgt1 and X₂ as stated (the same conjugation diag(1, i) and normalisation as at k = 1);
tr X₂ = u₂ + v₂ = −35/5184 = −det X₁ (asserted). The other sectors follow from the connection relations as in Paper 2, and
check_e2_num.out [1] confirms X₂ in all four sectors (error × 1/8 when |ζ| × 4, i.e. O(1/ξ)). With ξ = −nφ̃,
X₂/ξ² = X₂/(n²φ̃²), and the conjugation of E_pgt1 Lemma E.3 gives the second claim.
*n-dependence.* As in E_pgt1 Lemma E.3: f, φ̃, P₀^∞ are n-independent, and ω/ω^{mod} = 1 + O(n^{−p}) uniformly on both circles,
so Δ_k = Δ_k^{mod} + O(n^{−p}). ∎

## 4. Lemma E2.4: the local maps as convergent series

Notation of E_pgt1 Lemma E.4: a′ = 1/p + ½, B_p = B(a′, ½), (4c)^{1/p} = π/B_p, f = −(π²/4)z𝔞(z)² with μ*((0, x]) = x^{1/2}𝔞(x)
(Paper 2 Lemma signs(iii)), and φ̃₊(x) = iπ∫_x^{4c}(λ_p − ψ*) on the band (Paper 2 Lemma signs(iv)).

**Lemma E2.4 (PROVED).**
(i) For |z| < 4c,  𝔞(z) = ((4c)^{−1/2}/(pπ)) Σ_{k≥0} ((½)_k/k!)·(z/4c)^k/((a′ + k)(k + ½)).
(ii) With u = (z − 4c)^{1/2} and |u|² < 4c,  φ̃(z) = −(1/p)(4c)^{−3/2} u³ S(−u²/(4c)),
  S(e) := Σ_{k,m≥0} ((1 − a′)_k/k!)((1 + 1/p)_m/m!) e^{k+m}/((k + ½)(k + m + 3/2)).
In particular κ = (4/3)/(p(4c)^{3/2}) = 1/(6pc^{3/2}) and κ₂ = −(7 + 4/p)/(40c), as in E_pgt1 Lemma E.4.

*Proof.* (i) I_y(a′, ½) = (1/B_p)∫_0^y t^{a′−1}(1−t)^{−1/2}dt = (1/B_p)Σ_k((½)_k/k!)y^{a′+k}/(a′+k) for 0 ≤ y < 1 (binomial series,
non-negative terms, termwise integration). Multiply by λ_p(x) = (1/p)x^{−1−1/p} at y = x/4c and integrate from 0 to x:
μ*((0, x]) = ((4c)^{−a′}/(pB_p))Σ_k((½)_k/k!)(4c)^{−k}x^{k+½}/((a′+k)(k+½)), and (4c)^{−a′}/(pB_p) = (4c)^{−1/2}/(pπ). The
series has radius 4c; f and the right side are analytic in |z| < 4c (Paper 2 Lemma signs(iii)) and agree on (0, 4c).
(ii) As E_pgt1 Lemma E.4(ii) with full series: 1 − I_{1−e}(a′, ½) = (1/B_p)Σ_k((1 − a′)_k/k!)e^{k+½}/(k + ½) and
(1 − e)^{−1−1/p} = Σ_m((1 + 1/p)_m/m!)e^m (|e| < 1); integrate termwise in e. With u = iv^{1/2} on the band from ℂ₊ (v = 4c − x)
and (4c)^{−1/p}/(pB_p) = 1/(pπ), φ̃₊ = iπ(1/(pπ))(i u³/(4c)^{3/2})S(e), e = v/(4c) = −u²/(4c); φ̃/u³ is analytic at 4c
(E_pgt1 Lemma E.4(ii)), so the band values determine the series. S(0) = 4/3 gives κ; the e¹ coefficient of S is
14/15 + 8/(15p), giving κ₂ (both asserted in check_e2_sym.py). ∎

(ρ and ω near 0, resp. 4c, are the closed forms of E_pgt1 Lemma E.4(iii).)

## 5. Proposition E2.5: second-order small norm

**Proposition E2.5 (PROVED-mod-cite: RH_px §5, Paper 2 Prop. frame F1, F5 — as E_pgt1 Prop. E.5′).** For p > 1, s > 1, let
R⁽¹⁾ be as in E_pgt1 Prop. E.5′ (R⁽¹⁾_out = A₀/z + A_r/(z − 4c) + B_r/(z − 4c)² outside the discs) and R⁽¹⁾_in := R⁽¹⁾_out − Δ₁^{mod}
in each disc (analytic there, since R⁽¹⁾_out is the sum of the principal parts of Δ₁^{mod}). Put F := R⁽¹⁾_inΔ₁^{mod} + Δ₂^{mod},
meromorphic in each disc (Lemma E2.6). Then

  R(z) = I + R⁽¹⁾(z)/n + R⁽²⁾(z)/n² + O(n^{−ν})

uniformly at distance ≥ d > 0 from Σ_R, where R⁽²⁾_out is the sum of the principal parts of F at 0 and 4c; and for the first
moment at ∞, R_1 = R_1⁽¹⁾/n + R_1⁽²⁾/n² + O(n^{−ν}) with R_1⁽¹⁾ = A₀ + A_r and

  R_1⁽²⁾ = Res_{z=0}F + Res_{z=4c}F.

*Proof.* On the circles J − I = Δ₁^{mod}/n + Δ₂^{mod}/n² + O(n^{−ν}) (Lemma E2.3: Δ₁ − Δ₁^{mod} = O(n^{−p}) contributes n^{−1−p},
Δ₂ − Δ₂^{mod} contributes n^{−2−p}, the Bessel/Airy remainders n⁻³); on all other pieces of Σ_R, J − I = O(e^{−n/C}),
O(n^{−pn/4}), or O(n^{−K}min(1, |z|^K)) (hard-edge mismatch), on total length O(n^p), as in E_pgt1 Prop. E.5′. Hence
‖J − I‖_{L¹∩L²∩L^∞} = O(1/n), and with ‖𝒞₋‖_{L²→L²} ≤ C (Paper 2 F1) the equation R₋ = I + 𝒞₋(R₋(J − I)) gives
R₋ − I = 𝒞₋(J − I) + 𝒞₋(𝒞₋(J − I)(J − I)) + O(n⁻³) in L², hence

  R(z) − I = 𝒞(J − I)(z) + 𝒞(𝒞₋(J − I)·(J − I))(z) + O(n⁻³)

uniformly off the contour (Cauchy–Schwarz as in E_pgt1). In the second term only the circles matter to O(n^{−ν}), and there
𝒞₋(J − I) = 𝒞₋(Δ₁^{mod}χ_circ)/n + O(n^{−2} + n^{−1−p}) in L²; the Cauchy transform of the circle restriction of the
meromorphic Δ₁^{mod} is R⁽¹⁾ (principal parts outside, principal parts − Δ₁^{mod} inside; E_pgt1 Prop. E.5′), so its boundary
value from the inside (the minus side for clockwise circles) is R⁽¹⁾_in. Therefore

  R(z) − I = 𝒞(Δ₁^{mod}χ_circ)(z)/n + 𝒞((R⁽¹⁾_inΔ₁^{mod} + Δ₂^{mod})χ_circ)(z)/n² + O(n^{−ν}),

and for F meromorphic in the discs, (1/2πi)∮_{cw}F(s)ds/(s − z) is the sum of the principal parts of F at 0 and 4c (z outside
the discs), as at first order. The moment: R_1 = −(1/2πi)∫_{Σ_R}R₋(J − I)ds with the same splitting, and −(1/2πi)∮_{cw}F ds =
Res_0F + Res_{4c}F. ∎

## 6. Lemma E2.6: the Laurent data (exact computer algebra)

**Lemma E2.6 (PROVED; checks/check_e2_sym.py, sympy, all assertions pass, output check_e2_sym.out).** With the model data
of E_pgt1 Lemma E.4(iii) and Lemma E2.4 (series truncated at orders shown in the script to be sufficient for the
coefficients used):
(a) u⁷Δ₂^{r,mod} contains only odd powers of u = (z − 4c)^{1/2}, and v⁴Δ₂^{0,mod} (z = −v²) only even powers of v: Δ₂^{mod} is
  meromorphic in both discs (a non-trivial test of the branch choices, as in E_pgt1).
(b) The first-order data are reproduced: B_r, A_r, A₀ equal E_pgt1 Lemma E.5 (asserted), and κ, κ₂ equal E_pgt1 Lemma E.4(ii).
(c) Res_{4c}F = r₀A_r + r₁B_r + Res_{4c}Δ₂^{r,mod}, where R⁽¹⁾_in = r₀ + r₁(z − 4c) + O((z − 4c)²) near 4c, r₀ = A₀/(4c) − Δ^{reg}_0,
  r₁ = −A₀/(16c²) − Δ^{reg}_1 (Δ^{reg}_j the (z − 4c)^j coefficients of Δ₁^{r,mod}); Res₀F = R⁽¹⁾_in(0)A₀ + Res₀Δ₂^{0,mod}, with
  R⁽¹⁾_in(0) = −A_r/(4c) + B_r/(16c²) − C₀ (Δ₁^{0,mod} has a simple pole at 0, E_pgt1 Lemma E.5).
(d) With Q₁ = P₁ + (A₀ + A_r)/n + R_1⁽²⁾/n², the b-functional gives √((Q₁)₁₂(Q₁)₂₁)/c = 1 + d₁/n + d₂/n² + O(n⁻³) with
  d₁ = −p(α + 1)/2 = −(s−1)/2 and d₂ equal to the closed form of Theorem E2.1 (asserted symbolically in p and s; c-independent,
  asserted).

The intermediate matrices are long and are printed by the script rather than reproduced here; only d₂ enters Theorem E2.1.

## 7. Proof of Theorem E2.1

By Paper 2 F8 / RH_px §5 and the invariance lemma, as in E_pgt1 §7.1, n^{2p}b_n² = (Q₁)₁₂(Q₁)₂₁ with Q₁ = P₁ + R_1. By Prop.
E2.5, R_1 = (A₀ + A_r)/n + R_1⁽²⁾/n² + O(n^{−ν}), and (Q₁)₁₂(Q₁)₂₁ = c²(1 + O(1/n)) is bounded away from 0, so taking the
positive square root (n^pb_n > 0) and expanding, Lemma E2.6(d) gives n^pb_n/c = 1 − (s−1)/(2n) + d₂/n² + O(n^{−ν}). ∎

## 8. Corollary E2.7: the Christoffel function at the hard edge

For a positive measure σ on [0, ∞) with infinite support and finite moments, let

  λ_n(0; σ) := min{∫R²dσ : deg R ≤ n − 1, R(0) = 1}   (n ≥ 1).

**Corollary E2.7 (PROVED-mod-cite: Theorem E2.1 at s and s + 2p, E_pgt1 Theorem E.1, UL Theorem UF-lim [REVIEWED]).** For
p > 1 and s > 1 there is C = C(p, s) > 0 such that

  λ_n(0; σ_{p,s}) = C·n^{−(p+2)(s−1)/p}(1 + o(1))   (n → ∞).

*Proof.* (a) *Identity.* With H_n = (m_{i+j})_{0≤i,j<n} positive definite, minimising cᵀH_nc over c with c₀ = 1 gives
1/(H_n^{−1})₀₀ = det H_n/det(m_{i+j})_{1≤i,j<n}, and (m_{i+j})_{1≤i,j<n} is the Hankel matrix of x²σ of size n − 1. So
λ_n(0; σ) = D_n(σ)/D_{n−1}(x²σ). With D_n = Π_{j<n}h_j (h_j the monic norms, h_j = m₀Π_{i≤j}b_i²) and x²σ_{p,s} = σ_{p,s+2p}:

  log λ_n(0) = log h_{n−1}(s) + Σ_{j=0}^{n−2}[log h_j(s) − log h_j(s+2p)].

(b) *Expansions.* Write b_i = b_i(s), b_i″ = b_i(s + 2p), d_k = d_k(p, s), d_k″ = d_k(p, s + 2p). By Theorem E2.1 at both values
(s + 2p > 1), log(b_i/b_i″) = (d₁ − d₁″)/i + δ′/i² + O(i^{−ν}) with d₁ − d₁″ = p and δ′ := d₂ − d₂″ − (d₁² − d₁″²)/2. Using
Σ_{i≤j}1/i = log j + γ_E + 1/(2j) + O(j⁻²) and Σ_{i≤j}1/i² = ζ(2) − 1/j + O(j⁻²),

  log h_j(s) − log h_j(s + 2p) = 2p log j + K + (p − 2δ′)/j + O(j^{1−ν})   (j ≥ 1),

for a constant K; UL Theorem UF-lim (h_n(s)/h_n(s₀) = c^{(s−s₀)/p}n^{−(s−s₀)}(1 + o(1)), here s₀ = s + 2p) gives K = −2 log c.
By E_pgt1 Theorem E.1, log h_{n−1}(s) = 2(n − 1)log c − 2p log((n − 1)!) + 2d₁ log n + C₁ + o(1).
(c) *Summation.* Since ν > 2, Σ_j O(j^{1−ν}) converges. Summing (b) over 1 ≤ j ≤ n − 2 and adding the j = 0 term and
log h_{n−1}(s): the terms in n log c cancel (2(n−1)log c − 2(n−2)log c = 2 log c), −2p log((n−1)!) + 2p log((n−2)!) =
−2p log n + o(1), and the 1/j terms give (p − 2δ′)log n + O(1). Hence log λ_n(0) = γ log n + log C + o(1) with
γ = −2p + 2d₁ + p − 2δ′ = −p − (s − 1) − 2δ′. By the computation below, δ′ = (s − 1)/p − p/2, so γ = −(p + 2)(s − 1)/p. ∎

*Check of the exponent algebra.* d₂(s) − d₂(s + 2p) = −[(p+1)/(8p)][(s+2p−1)² − (s−1)²] + [(p+2)/(8p²)][(s+p−1)² − (s−1−p)²]
= −(p+1)(s−1+p)/2 + (p+2)(s−1)/(2p), and (d₁² − d₁″²)/2 = [(s−1)² − (s+2p−1)²]/8 = −p(s−1+p)/2; so
δ′ = −(s−1+p)/2 + (p+2)(s−1)/(2p) = (s−1)/p − p/2, and γ = −p − (s−1) − 2(s−1)/p + p = −(s−1)(p+2)/p (also asserted
symbolically at the end of check_e2_sym.py). NUMERICAL confirmation: check_e2_christoffel.out, local slopes over
n ∈ [800, 1600]: −2.33263 vs −7/3 at (3/2, 2), −1.99955 vs −2 at (2, 2), −3.99820 vs −4 at (2, 3), −1.66642 vs −5/3 at (3, 2).

## 9. Remarks, consequences, and what remains open

**Remark E2.8 (index-shift form).** Theorem E2.1 says n^pb_n/c = (1 + (s−1)/(2pn))^{−p}(1 + 𝖤/n² + O(n^{−ν})) with
𝖤 = (p+1)/12 − (p+2)(s−1−p)²/(8p²): the first term of d₂ is the second-order part of the index shift n ↦ n + (s−1)/(2p) of
SECOND §1 (README "a shift of the index"), and 𝖤 is the genuinely new part. Its s-dependent piece vanishes at s = 1 + p
(α = 0), the point that is also special for the a-law (TAIL.md GAP UP-1+p); no claim is made about a connection.

**Remark E2.9 (p = 2, all s).** At p = 2, H_n is exactly constant (E_pgt1 Remark E.2(3)), the remainder is O(n⁻³), and
d₂ = (s² + 6s − 11)/16 now holds for every s > 1 (SECOND Thm 2.3 had s ∈ {2, 4, 6, 8, 10}). The grid confirms it at
s ∈ {3/2, 3, 5} as well (check_e2_grid.out).

**Remark E2.10 (p = 1; NUMERICAL, outside Theorem E2.1).** At p = 1 the fitted n⁻² coefficient equals d₂(1, s) − 1/12 at
all five s on the grid (check_e2_grid.out, deviations ≤ 1.3·10⁻⁶). Here −1/12 = 2p c(p)ζ(−p) at p = 1 = κ₁, i.e. the n^{−1−p}
term of E_plt1 Theorem E′.1 (0 < p < 1) merges with the n⁻² term at p = 1. CONJECTURE (p = 1): n b_n/c(1) = 1 − (s−1)/(2n) +
(d₂(1, s) − 1/12)/n² + o(n⁻²). Not proved: at p = 1, Lemma E.2 fails (E_pgt1 §9) and the hard edge uses the RH₁(r) analysis.

**Remark E2.11 (the s² coefficient and Paper III Conjecture 8.1; HEURISTIC).** The s² coefficient of d₂ is (p² − 2)/(8p²) =
1/8 − 1/(4p²). If the expansion of Theorem E2.1 could be differentiated twice in s with the same remainder (not proved:
uniformity of the RH error in complex s is not established here), Euler–Maclaurin would give ∂_s²log h_n =
(2/n)(1/4 − ∂_s²d₂) + o(1/n) = 1/(p²n) + o(1/n) > 0, which is the convexity of Paper III Conjecture 8.1 and matches the
measured second differences ≈ 1/(2p²n) of check_so_convex.out (step-1 divided differences). This identifies what a proof of
the conjecture for p > 1 needs: the present analysis with error bounds uniform for s in a complex neighbourhood of a compact
K ⊂ (1, ∞).

**Remark E2.12 (CG reading of Cor E2.7).** For a positive compact operator A with eigenvalues k^{−p} and an initial error e₀
whose spectral weights λ_k|⟨e₀, φ_k⟩|² equal k^{−s}, the A-norm error of the conjugate gradient method after n − 1 steps is
λ_n(0; σ_{p,s}), so it decays like n^{−(1+2/p)(s−1)} (p > 1, s > 1). For comparison, a fixed-step gradient iteration gives
n^{−(s−1)/p} up to constants (elementary). Not used elsewhere.

**Open (GAP).**
- d₂ for 0 < p ≤ 1: at p = 1 see Remark E2.10; for p < 1 the seam terms (E_plt1) add n^{−1−p}, n^{−1−2p}, … whose
  coefficients beyond κ_p are not computed (THEOREMS §4 item 13).
- The second-order coefficient of n^pα_n (needs R_2⁽²⁾ as well); not computed here.
- Uniformity in s (Remark E2.11).
- Rule L (novelty) not done: higher-order RH expansions for fixed Jacobi weights are in KMVV §8; what is specific here is the
  discrete, saturated geometry (E_pgt1 Lemma E.2) and the closed form.

## 10. Rule A (adversarial pass) — log

- *Reproduction of first order.* The script recomputes B_r, A_r, A₀, κ, κ₂ from the new series and asserts equality with E_pgt1
  Lemmas E.4–E.5; and d₁ = −(s−1)/2.
- *Branches.* Odd powers of u in u⁴Δ₁^r and even powers in u⁷Δ₂^r (and the analogue at 0) vanish identically; a wrong branch
  of (−ω)^{1/2}, 𝔞_∞², ρ or f^{1/2} produces half-integer powers. The first run used √((p+2)²) unsimplified, which broke the A₀
  assertion; f^{1/2} is now written as v·(positive series)/(√c(p+2)).
- *Sign and normalisation of X₂, Ξ₂.* Checked three ways: the determinant identities tr X₂ = −det X₁, tr Ξ₂ = −det Ξ₁; the
  sector numerics (check_e2_num); and the final d₂ against the independent grid fits (25/25).
- *c-independence.* c is a free symbol; d₂ is asserted independent of it. An error in the relation between κ, f′(0) and c (e.g.
  a wrong power of 4c in Lemma E2.4) leaves a log-free but c-dependent remainder; none appears.
- *Truncation orders.* The Laurent coefficients used need u-series to u⁶ for Δ₁^r (κ up to κ₄) and u⁵ for u⁷Δ₂^r (κ up to κ₃),
  and v-series to v² for v⁴Δ₂⁰ (f up to its z³ coefficient); the script keeps u¹⁰, six terms of S and of 𝔞.
- *Where n^{−1−p} enters.* For 1 < p < 2 the remainder O(n^{−1−p}) dominates O(n⁻³); the grid fit basis {n^{−1−i−jp}}
  contains it, and the fitted d₂ is stable across fit orders and windows (half-ranges ≤ 3·10⁻⁴ at p = 3/2).
- *Converse / scope.* p > 1 is used exactly where E_pgt1 uses it (Lemma E.2; n^{−1−p} = o(n⁻²)). At p = 1 the formula needs the
  extra −1/12 (Remark E2.10), which is consistent with, and explained by, the merging of the κ_p n^{−1−p} term.

## 11. Integration

To be applied after Rule R (independent second reader). Proposed changes: THEOREMS.md §2.10 (new row "Thm E2.1, Cor E2.7
(Plan E2)"), §4 item 13 (d₂ for p > 1 closed; p ≤ 1 open; Remark E2.10 conjecture at p = 1), E_pgt1 §9 bullet "d₂" (pointer
to this file), SECOND Thm 2.3 row (d₂ at p = 2 for all s via Theorem E2.1), Paper II §13.1 and NOTES (the n⁻² coefficient for
p > 1), RH/CITATIONS.md "(Plan E2 reuse)" (the k = 2 instances of 10.17.1, 10.17.8, 9.7.2 already quoted there).
