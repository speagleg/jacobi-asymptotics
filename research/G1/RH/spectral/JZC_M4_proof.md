# JZC M4 proof: the lattice expansion as a double series in 1/N and the band-factor parameters (Theorem N.6)

Status (2026-10-21): Rule R review A done (REVIEW_JZC_M4_proof_A.md, ACCEPT WITH FIXES; all fixes applied in this revision,
log in §9). A second reader is pending before REVIEWED. Labels per VERIFICATION_POLICY.md.

This note turns JZC_M4 §5–§6 (Props N.3, N.4) into theorems, for every p > 0 with p ≠ 1. It generalises to every order K the
REVIEWED order-2 proofs of:
- E2_pgt1 (Plan E2, p > 1);
- E3 (Plan E3, all p ≠ 1);
- E_plt1 (Plan 67, p < 1).

The algebra is exact computer algebra in (p, α), and also in the zeta index j; it is not reconstruction.

| # | Statement | Label |
|---|---|---|
| Lemma N.6a | jumps on the two circles to every order K, from the general-k DLMF coefficients; Δ_k = G_{μ_n}Δ_k^{mod}G_{μ_n}⁻¹ + O(n^{−(J+1)p}) | PROVED-mod-cite (E2 Lemma E2.3 / E_plt1 Lemma E′.3 arguments [REVIEWED]; DLMF 10.17.1, .5–.6, .8, .11–.12, 10.40.1–4, 9.7.1–2, 9.7.5–6 at general k [CITATIONS]; E3 Lemmas F.1′, E3.4–E3.5, E_plt1 Lemma F.1 [REVIEWED]) |
| Lemma N.6b | Δ_k^{mod} meromorphic in both discs for every k (p > 1: limit argument; p < 1: parity argument); Δ_k^μ likewise, with Laurent coefficients entire in μ | PROVED |
| Prop N.6c | small norm to order K, residue recursion | PROVED-mod-cite (Paper 2 F1, F5, RH_px §5, E_pgt1 Prop E.5′ / E_plt1 Prop E′.5′ [REVIEWED]; induction on the order) |
| Lemma N.6d | exact algebra: the μ = 0 layer to N⁻⁶; the first-order μ_j layer for all j (symbolic j) to N⁻⁴ relative, and for j ≤ 5 to N⁻⁵ relative; the second-order μ₁ layer to N⁻⁵ relative | PROVED (exact computer algebra over ℚ(p, α)[i] and ℚ(p, α, j)[i]; m4_rh_exact.py, m4_rh_exact2.py, m4_zeta_exact.py, m4_zeta_exact2.py; outputs listed in §5) |
| **Thm N.6** | double expansion of n^pb_n/c in 1/n and μ_n (all orders, structural), with the natural forms of its layers (exact) and the explicit b_n expansion to O(n⁻⁷ + n^{−2−3p}) | PROVED-mod-cite (the four items above; E3 Lemma E3.7 [REVIEWED]; Paper 2 F8) |

## 1. Statement

Notation is that of E_pgt1 §0, E_plt1 §0, E2 §0 and E3 §0: the Q-frame, P₀^∞, T, M, the circles ∂U_0 and ∂U_r around 0 and
4c, and c = c(p). We also use:
- α = (s−1)/p − 1 and N := n + α/2 + ½;
- G_μ, E3's gauge (Lemma E3.4(ii)), for μ ∈ ℂ^J, and Δ_k^μ := G_μΔ_k^{mod}G_μ⁻¹, with Δ_k^{mod} as in Lemma N.6a;
- μ_{n,j} := 2ζ(−jp)/(jn^{jp}), the band-factor parameters of E3 Lemma F.1′ (p > 1) and E_plt1 Lemma F.1(iii) (p < 1);
- ε_j := C(2j, j)pc^jζ(−jp), as in E3.

**Residue recursion.** Set R_in⁽⁰⁾ := I near each e ∈ {0, 4c}. For m ≥ 1, define:
- F_m(μ) := Σ_{j=1}^m R_in⁽ᵐ⁻ʲ⁾(μ)Δ_j^μ, meromorphic in each disc;
- R_out⁽ᵐ⁾(μ) := the sum of the principal parts of F_m(μ) at 0 and 4c;
- R_in⁽ᵐ⁾(μ) := R_out⁽ᵐ⁾(μ) − F_m(μ), analytic in each disc;
- R_1⁽ᵐ⁾(μ) := Res₀F_m(μ) + Res_{4c}F_m(μ).

For m = 1, 2 these are E2 Prop E2.5 and E3 Prop E3.6. Define 𝔇_K(n; μ) := √((Q₁)₁₂(Q₁)₂₁)/c, expanded to order n^{−K}, where
Q₁ = P₁ + Σ_{m≤K}R_1⁽ᵐ⁾(μ)n^{−m}. Write 𝔇_K(n; μ) = Σ_β μ^β𝔇_{β,K}(n) for its Taylor series in μ. Each 𝔇_{β,K}(n) is a
polynomial in 1/n of degree ≤ K; 𝔇_{0,K} starts 1 + d₁/n, and 𝔇_{β,K} = O(n⁻²) for |β| ≥ 2.

**Theorem N.6 (PROVED-mod-cite).** Let p > 0, p ≠ 1, s > 1, and K, J, B ≥ 1.

(i) *Double expansion.*
  n^pb_n/c = Σ_{|β|≤B} μ_n^β𝔇_{β,K}(n) + O(n^{−K−1} + n^{−2−(B+1)p} + n^{−1−(J+1)p}).

(ii) *Natural forms of the layers* (exact; Lemma N.6d). The expansions below are of polynomials in 1/n, re-expanded in 1/N.
  - **μ = 0 (integer layer):** 𝔇_{0,6}(n) = (n/N)^p[1 + f₂N⁻² + f₄N⁻⁴ + f₆N⁻⁶ + O(N⁻⁷)], with no N⁻¹, N⁻³, N⁻⁵ terms,
    f₂ = −(p+2)α²/8 + (p+1)/12, and f₄, f₆ the closed forms of JZC_M4 §5.
  - **μ_j, first order, every j ≥ 1:** μ_{n,j}𝔇_{e_j,4}(n) = (n/N)^pε_jN^{−1−jp}[1 + g_jN⁻² + O(N⁻⁴)]. There is no N⁻¹ or N⁻³
    term in the bracket, and g_j = A_j + B_jα² with
    - A_j = [j²(j²+2j−2)p³ + 2(j+1)(2j²−1)p² + (5j²+2j−6)p + 2(j−2)]/(24(2j−1)p),
    - B_j = (p+2)(j²p² + (j+1)p + 2)/(8(2j−1)p).
    For j ≤ 5 at K = 5, the bracket error is O(N⁻⁵); for j = 1 the N⁻⁴ term is g₁,₄ (JZC_M4 §6).
  - **μ₁², second order:** μ_{n,1}²𝔇_{2e₁,5}(n) = (n/N)^pε₁²N^{−2−2p}[(3p+1)/(2p) + h₂N⁻² + O(N⁻⁴)]. There is no N^{−1−2p}
    term, no N⁻¹ term in the bracket, and the N⁻³ term in the bracket is zero; h₂ is given in §5.

(iii) *The b_n expansion.* With K = 6, B = 2 and J ≥ 6/p − 1:

  n^pb_n/c = (n/N)^p[1 + f₂N⁻² + f₄N⁻⁴ + f₆N⁻⁶ + ε₁N^{−1−p}(1 + g₁N⁻² + g₁,₄N⁻⁴) + Σ_{j≥2}ε_jN^{−1−jp}(1 + g_jN⁻²)
             + ε₁²N^{−2−2p}·(3p+1)/(2p)] + O(n⁻⁷ + n^{−2−3p}).

  The sum over j is finite: terms with 1 + jp ≥ min(7, 2 + 3p) are absorbed into the remainder.

**Remainder bookkeeping (review F5).**
- The first-order brackets.
  - j = 1: the bracket is known to N⁻⁵ relative (K = 5), so the error is O(n^{−6−p}). This is inside the remainder: 6 + p >
    2 + 3p iff p < 2, and 6 + p ≥ 8 for p ≥ 2.
  - j ≥ 2: the bracket error is O(N⁻⁴) relative (symbolic-j run at K = 4), i.e. O(n^{−5−jp}). This is inside the remainder:
    5 + jp ≥ 5 + 2p > 2 + 3p for p < 3, and 5 + 2p ≥ 11 for p ≥ 3.
- The μ₁² bracket's h₂N⁻² contributes O(n^{−4−2p}), which is inside the remainder: 4 + 2p > 2 + 3p iff p < 2, and 4 + 2p ≥ 7
  for p ≥ 3/2.
- The other |β| = 2 terms, μ₁μ₂, μ₂², μ₁μ₃, …, are O(n^{−2−3p}) because 𝔇_β = O(n⁻²). The |β| = 3 terms are O(n^{−2−3p}).
- The truncations K = 6 (μ = 0), K = 5 (|β| = 1, 2) and J ≥ 6/p − 1 give O(n⁻⁷ + n^{−6−p} + n^{−6−2p} + n^{−1−(J+1)p}) ⊂
  O(n⁻⁷ + n^{−2−3p}).

**Which coefficients of b_n are determined (review F1).** A term cN^{−e} in (iii) is a coefficient of n^pb_n/c exactly when
e < min(7, 2 + 3p). This gives:

| term | exponent e | determined for |
|---|---|---|
| f₂N⁻² | 2 | all p |
| f₄N⁻⁴ | 4 | p > 2/3 |
| f₆N⁻⁶ | 6 | p > 4/3 |
| ε_jN^{−1−jp} | 1 + jp | (j − 3)p < 1 and 1 + jp < 7; e.g. j ≤ 3 when p ≥ 1, j = 4 for p < 1, … |
| ε₁g₁N^{−3−p} | 3 + p | 1/2 < p < 4 |
| ε₂g₂N^{−3−2p} | 3 + 2p | 1 < p < 2 |
| ε₁g₁,₄N^{−5−p} | 5 + p | 3/2 < p < 2 |
| ε₁²N^{−2−2p}(3p+1)/(2p) | 2 + 2p | p < 5/2 |
| ε_jg_j (j ≥ 3), ε₁²h₂ | 3 + jp, 4 + 2p | never at this B; proved as layer identities (ii) |

**Consequences.**
- Conjecture S1-N holds to N⁻⁶ in the following form. The μ = 0 layer has no N⁻¹, N⁻³, N⁻⁵ terms. Every first-order zeta
  layer has no N⁻¹, N⁻³ terms relative to its leading power. The ζ(−p)² layer starts at (ε₁N^{−1−p})² with no odd
  correction to N⁻³ relative.
- As coefficients of b_n, the following hold in the ranges of the table: f₂, f₄, f₆, ε₁, ε₂, ε₃, ε₁g₁, ε₂g₂, ε₁g₁,₄, and
  (3p+1)/(2p)ε₁².
- Everything in (ii) holds as an identity of the layers, for every p.

## 2. Lemma N.6a: the jumps to every order

**Lemma N.6a.** Uniformly on ∂U_0 and ∂U_r (boundary values included), for every K:
- P̂(P₀^∞)⁻¹ = I + Σ_{k≤K}Δ_k/n^k + O(n^{−K−1}), with
  - Δ_k^0 = (2f^{1/2})^{−k}P₀^∞ρ^{σ₃}(σ₃Ξ_kσ₃)ρ^{−σ₃}(P₀^∞)⁻¹, Ξ_k = M⁻¹(M∘C_k), C_k = [[(−1)^ka_k, a_k], [(−1)^kb_k, b_k]];
  - Δ_k^r = (−1/φ̃)^kP₀^∞(−ω)^{−σ₃/2}X_k(−ω)^{σ₃/2}(P₀^∞)⁻¹, X_k = M⁻¹(M∘C_k′), C_k′ = [[u_k, (−1)^ku_k], [v_k, (−1)^kv_k]];
- Δ_k = G_{μ_n}Δ_k^{mod}G_{μ_n}⁻¹ + O(n^{−(J+1)p}), where "mod" means the model weight z^α(4c − z).

*Inputs* (DLMF, quoted in CITATIONS (DLMF-10.40, Paper 2), (DLMF-10.17, Plan 55), (DLMF-9, Paper 2), (DLMF-9.7.2, Plan 65);
re-read 2026-10-21):
- **10.17.1:** "a₀(ν) = 1, a_k(ν) = ((4ν² − 1²)(4ν² − 3²)⋯(4ν² − (2k−1)²))/(k!8^k)".
- **10.17.5:** "H^{(1)}_ν(z) ∼ (2/(πz))^{1/2}e^{iω}Σ_{k=0}^∞ i^k a_k(ν)/z^k", −π + δ ≤ ph z ≤ 2π − δ.
- **10.17.6:** "H^{(2)}_ν(z) ∼ (2/(πz))^{1/2}e^{−iω}Σ_{k=0}^∞(−i)^k a_k(ν)/z^k", −2π + δ ≤ ph z ≤ π − δ.
  §10.17(ii): "These results follow by differentiation of the corresponding expansions."
- **10.40.1:** I_ν(z) ∼ e^z(2πz)^{−1/2}Σ(−1)^ka_k(ν)z^{−k}, |ph z| ≤ π/2 − δ.
- **10.40.2:** K_ν(z) ∼ (π/(2z))^{1/2}e^{−z}Σa_k(ν)z^{−k}, |ph z| ≤ 3π/2 − δ.
- **10.40.3, 10.40.4:** the same for I_ν′ and −K_ν′, with b_k(ν).
- **9.7.1–9.7.2:** "ζ = (2/3)z^{3/2}"; "u_k = (2k+1)(2k+3)(2k+5)⋯(6k−1)/(216^k k!)", "v_k = ((6k+1)/(1−6k))u_k".
- **9.7.5–9.7.6:** "As z → ∞ the following asymptotic expansions are valid uniformly in the stated sectors":
  Ai(z) ∼ e^{−ζ}/(2√π z^{1/4})Σ(−1)^ku_k/ζ^k and Ai′(z) ∼ −z^{1/4}e^{−ζ}/(2√π)Σ(−1)^kv_k/ζ^k, |ph z| ≤ π − δ.

- **10.17.8**, general k (CITATIONS entry "(DLMF-10.17, Plan 55)"):
  b_k(ν) = ((4ν²−1²)(4ν²−3²)⋯(4ν²−(2k−3)²))(4ν²+4k²−1)/(k!8^k).

The code uses 10.17.8 as quoted. As a cross-check, m4_rh_exact.py asserts for k ≤ 8 that it equals a_k + (k − ½)a_{k−1}, the
coefficient obtained by differentiating 10.40.2 term by term:
d/dz[z^{−1/2}e^{−z}z^{−k}] = −z^{−1/2}e^{−z}z^{−k}(1 + (k + ½)/z). It also asserts the u_k recurrence and v_k of 9.7.2.
General-k 9.7.2 is quoted in "(DLMF-9.7.2, Plan 65)"; the reuse is listed in CITATIONS "(JZC M4 reuse)".

*Proof.*
- The proof of E2 Lemma E2.3 (p > 1), resp. E_plt1 Lemma E′.3 (p < 1, rays at π − θ_L with δ = θ_L/2), goes through verbatim
  with K + 1 terms in place of 3.
- *Sign pattern for every k* (the "tie" argument, review A F3). Every column of the Airy model is a k-independent constant
  times Ai(Z) or Ai′(Z), with Z = e^{2πim/3}ζ and |ph Z| ≤ π − δ.
  - Then Z^{3/2} = ±ζ^{3/2}, and 9.7.5–9.7.6 give e^{−ξ(Z)}Σ(−1)^ku_kξ(Z)^{−k} = e^{∓ξ}Σ(∓1)^ku_kξ^{−k}.
  - So (−1)^k sits exactly on the column that carries e^{−ξ}, whichever branch occurs.
  - The Bessel model is the same: H⁽¹⁾_α(x) = (const)e^{−Y}Σa_kY^{−k} with Y = −ix = ±w; H⁽²⁾ has Y = ix; I_α, K_α have
    Y = −w, w (10.17.5–6, .11–.12, 10.40.1–4).
  - Which column carries e^{±ξ} (resp. e^{±w}) is fixed at k = 0, so C_k and C_k′ — hence Ξ_k and X_k — are the same in
    every sector, for every k.
  - Review A re-derived k = 3 by hand in one Hankel sector and the rotated Airy sectors, and checked all sectors numerically
    (REVIEW_JZC_M4_proof_A, "Re-derivations").
  - The same wording in E2 Lemma E2.3 ("ξ(q^{±1}ζ) = −ξ(ζ)") is literally false in some subsectors. Its conclusion stands by
    this argument; textual fix only.
- With w = 2nf^{1/2} and ξ = −nφ̃ (both ≍ n on the circles), the Poincaré remainders O(w^{−K−1}) and O(ξ^{−K−1}) are
  O(n^{−K−1}) uniformly.
- The n-dependence of the weight is E3 Lemma E3.5 (all p ≠ 1). Its proof uses only that Δ_k depends analytically on
  (ρ²)^{±1} and (−ω)^{±1/2}, with no restriction on k. With E3 Lemma F.1′ (p > 1), resp. E_plt1 Lemma F.1(iv) (p < 1), at
  order J it gives the stated O(n^{−(J+1)p}). For p < 1, RH_plt1b's glue changes the prefactor by O(e^{−c′n}) (E_plt1
  Lemma E′.3).
- The conjugation formulas are E3 Lemma E3.4(iii), whose proof is also k-free: it commutes diagonal factors. ∎

## 3. Lemma N.6b: meromorphy for every k

E2 Lemma E2.6(a) (review A B1) argues as follows. G_n := P̂^{mod}(P₀^∞)⁻¹ is analytic in U_e ∖ {e}, the expansion of Lemma
N.6a holds uniformly on compacts K ⊂ U_e ∖ {e}, and so Δ_k = lim n^k(G_n − I − Σ_{i<k}Δ_in^{−i}) is analytic and single-valued in
U_e ∖ {e}. Its explicit formula grows at most polynomially at e, so e is a pole. Nothing in this depends on k. The gauge G_μ is
entire in (z, μ) (E3 Lemma E3.4(ii)), so Δ_k^μ is meromorphic with Laurent coefficients entire in μ.

*p < 1* (where the glued parametrix carries seam jumps inside U_0, so the limit argument is replaced by the explicit jump
argument of E_plt1 Lemma E′.5, which extends to every k by parity):
- Write X_k = ½(u_k + v_k)I − ½(u_k − v_k)σ₂ for even k, and X_k = ½(u_k + v_k)σ₃ + ½(v_k − u_k)iσ₁ for odd k (from
  X_k = M⁻¹(M∘C_k′)). So J X_k J⁻¹ = (−1)^kX_k for J = iσ₂.
- On (4c − ε, 4c), φ̃₊ = −φ̃₋, so the prefactor (−1/φ̃)^k picks up (−1)^k. With P₀^∞₊ = P₀^∞₋J and (−ω)^{1/2}₊(−ω)^{1/2}₋ = 1,
  Δ_k^r has no jump there.
- Likewise σ₃Ξ_kσ₃ = ½(a_k + b_k)I + ½(a_k − b_k)σ₂ (k even) or −½(a_k + b_k)σ₃ − ½(a_k − b_k)iσ₁ (k odd), so it commutes or
  anticommutes with J as (−1)^k. f^{1/2}₊ = −f^{1/2}₋ on (0, δ), and the ρ² relations of E_plt1 Lemma E′.5 hold, so Δ_k^0 has
  no jump on (0, δ). On (−δ, 0) the argument of E′.5 is unchanged.
- The growth bounds give poles. The gauge factors e^{±𝓡M_μ/2} satisfy the same relations (𝓡₊ = −𝓡₋ on the band), as in E3
  Lemma E3.4(iii).

Computer-algebra confirmation, exact, in m4_rh_exact.py (review A F4 wording):
- for every k ≤ 6, Δ_k^r contains only even powers of u = (z − 4c)^{1/2}, i.e. u^{3k+1}Δ_k^r only powers ≡ 3k + 1 (mod 2);
- the v-series of Δ_k^0 (z = −v²) contains only even powers (asserted by `u_to_w`);
- each R_in⁽ᵐ⁾ is analytic at both points (asserted).

Review A's mutation tests (F4) show that the parity assertion catches a flipped (−1)^k column at k = 3, 4 on both edges.
The swaps a₃ ↔ b₃ and u₃ ↔ v₃ are caught by f₃ = 0. Doubling u₄, v₄ is caught only by the f₄ closed form, which was
reconstructed from code with the same inputs, so that catch is not independent. The independent catch is the lattice fit
m4_f4_lattice.out (Rule X).

## 4. Proposition N.6c: small norm to order K

**Proposition N.6c.** Let p > 0, p ≠ 1. With R⁽ᵏ⁾ := R_out⁽ᵏ⁾(μ_n) outside the discs and R_in⁽ᵏ⁾(μ_n) inside,
R(z) = I + Σ_{k≤K}R⁽ᵏ⁾(z)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}) uniformly at distance ≥ d > 0 from Σ_R. Also
R_1 = Σ_{k≤K}R_1⁽ᵏ⁾(μ_n)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}).

*Proof.* Write η_n := n^{−K−1} + n^{−1−(J+1)p}.
- **Jumps.** As in E2 Prop E2.5, J − I = Σ_{k≤K}Δ_k^{μ_n}χ_circ n^{−k} + E.
  - Off the circles, E is O(e^{−n/C}), O(n^{−pn/4}) or O(n^{−K′}min(1, |z|^{K′})) for any K′ (hard-edge mismatch), on total
    length O(n^p), exactly as in E_pgt1 Prop E.5′ (p > 1).
  - For p < 1, E_plt1 Prop E′.5′ change (1) adds the lips at ±θ_L and the seam glue jumps, both super-small and vanishing to
    all orders at 0.
  - On the circles E = O(η_n) (Lemma N.6a).
  - So ‖E‖_{L¹∩L²∩L^∞} = O(η_n) and ‖J − I‖_{L²∩L^∞} = O(1/n).
- **Small norm.** ‖𝒞₋‖_{L²→L²} ≤ C (Paper 2 F1), so for large n the equation R₋ = I + 𝒞₋(R₋(J − I)) has a unique solution
  with ‖R₋ − I‖_{L²} = O(1/n).
- **Induction claim (on m = 1, …, K + 1; review A F2):** R₋ = Σ_{k<m}R₋⁽ᵏ⁾n^{−k} + O_{L²}(n^{−m} + n^{−1−(J+1)p}). Here
  R₋⁽⁰⁾ = I, and R₋⁽ᵏ⁾ is the minus-side boundary value of R⁽ᵏ⁾, which is R_in⁽ᵏ⁾ on the clockwise circles and R_out⁽ᵏ⁾
  elsewhere.
  - m = 1 is the small-norm bound.
  - Step m → m + 1: insert the claim into R = I + 𝒞(R₋(J − I)).
    - The terms with k + j ≥ m + 1 are O(n^{−m−1}).
    - The error term of the claim is multiplied by J − I = O(1/n). The jump error E (which contains the
      O(n^{−1−(J+1)p}) band-factor part) appears once. So the new error is O(n^{−m−1} + n^{−1−(J+1)p}).
    - The off-circle part of J − I paired with bounded R₋⁽ᵏ⁾ is O(η_n). Off the discs, R_out⁽ᵏ⁾ is bounded and O(1/|z|),
      and the super-small jump beats the polynomial length.
    - So R − I = Σ_{m=1}^{K}𝒞(Σ_{j=1}^mR₋⁽ᵐ⁻ʲ⁾Δ_j^{μ_n}χ_circ)n^{−m} + O(η_n) uniformly off the contour (Cauchy–Schwarz
      against the kernel, as in E_pgt1), and in L² on the contour (𝒞₋ bounded).
  - Identify each term: on the circles R₋⁽ᵐ⁻ʲ⁾ = R_in⁽ᵐ⁻ʲ⁾, so the integrand is F_m(μ_n)χ_circ with F_m meromorphic in the
    discs (Lemma N.6b). For such F, (1/2πi)∮_{cw}F(s)ds/(s − z) is the sum of the principal parts of F at 0 and 4c when z is
    outside the discs, and that sum minus F when z is inside (residue theorem). This is R_out⁽ᵐ⁾ and R_in⁽ᵐ⁾, so 𝒞(…) = R⁽ᵐ⁾
    and 𝒞₋(…) = R₋⁽ᵐ⁾. This closes the induction, and m = K + 1 gives the expansion of R.
- **Moment.** R_1 = −(1/2πi)∫_{Σ_R}R₋(J − I)ds with the same splitting, and −(1/2πi)∮_{cw}F_m ds = Res₀F_m + Res_{4c}F_m.
- **p < 1 at the point 0.** It is reached as in E_plt1 Prop E′.5′: the super-small local jumps, including the glue jumps on
  the seam segments, are dominated near 0. ∎

(The proof is E2 Prop E2.5's, with the second Neumann iterate replaced by the K-th. The only new point is the identification
of iterated Cauchy transforms of circle restrictions with the residue recursion, which is the residue theorem applied once
per order.)

## 5. Lemma N.6d: the exact algebra

**Lemma N.6d (PROVED; exact computer algebra).** The scripts carry out the residue recursion of §1 and the extraction of
Theorem N.6 in exact arithmetic, with c = 1. All inputs are rational functions of (p, α) once c = 1:
- the series of E2 Lemma E2.4 have rational coefficients;
- π cancels in f = −(π²/4)z𝔞²;
- the square roots are of series with leading coefficient 1 or a perfect square: f^{1/2} ∼ v/(p+2), (4 + v²)^{1/2} ∼ 2;
- the factors 1/√2 in T and M occur in conjugate pairs.

Truncation is controlled by tracking, for every series, the highest exactly known coefficient. Each principal part asserts
that its coefficients down to the residue are known; otherwise the run fails. Review A I1 checked every routine and the
guard, varied the truncation depth with identical exact results, and ran mutation tests.

The scripts:
- `m4_rh_exact.py`: the μ = 0 layer over ℚ(p, α)[i].
- `m4_zeta_exact.py`: first order in μ_j for integer j ≤ 5 (dual numbers, ε² = 0).
- `m4_rh_exact2.py` / `m4_zeta_exact2.py`, which generalise these in two ways:
  - **(A)** symbolic j over ℚ(p, α, j)[i]. Here μ_j is normalised by C(2j, j), and the gauge needs only the Taylor data of
    Q_j/C(2j, j) at 0 and at 4c. These are rational in j:
    - at 0: Π_{i≤m}(j−i)/(2(2j−2i−1)), which vanishes for m ≥ j;
    - at 4c: j(j−1)⋯(j−m)/(4^{m+1}(½)_{m+1}), from Σ_jQ_j(z)t^j = t/((1−zt)√(1−4t));
    - both are asserted against the integer-j polynomials for j ≤ 8.
  - **(B)** second order in μ₁, with the gauge to order μ²: cosh h = 1 + z(z−4c)μ²Q₁²/8 + O(μ⁴), S = μQ₁/2 + O(μ³)
    (E3 Lemma E3.4(ii)), over ε³ = 0.

The first-order gauge derivative is ∂_{μ_j}Δ_k^μ|₀ = [𝒢_j, Δ_k^{mod}], with 𝒢_j = T[[0, −(z−4c)Q_j/2], [−zQ_j/2, 0]]T⁻¹. Its sign
is pinned by the asserted leading coefficient, which is E3 Lemma E3.7 (review A I1(c)).

*c-normalisation* (review F7, I2). With z = cζ, (z − 4c)Q_j and zQ_j are c^j times their c = 1 values. So μ_j enters only as
c^jμ_j: the integer layer and the ratios g_j, h₂ are c-free, and ε_j carries c^j.

Every output starts with the sha256 of the scripts that produced it (review F6). The results, identically in the symbols:
- **μ = 0, K = 6** (`m4_rh_exact_k6.out`; K = 4: `m4_rh_exact_k4.out`):
  - d₁ = −p(α+1)/2 and d₂ = E2 Theorem E2.1;
  - natural form: f₁ = f₃ = f₅ = 0, f₂ = −(p+2)α²/8 + (p+1)/12, and f₄, f₆ as in JZC_M4 §5;
  - the DLMF coefficient identities of §2 (k ≤ 8).
- **First order, j = 1, …, 5, K = 5** (`m4_zeta_exact.out`):
  - leading coefficient C(2j, j)pj/2;
  - N^{−2−jp} = N^{−4−jp} = 0;
  - N^{−3−jp}/N^{−1−jp} = A_j + B_jα²;
  - for j = 1, N^{−5−p}/N^{−1−p} = g₁,₄.
- **First order, symbolic j, K = 4** (`m4_zeta_exact2_A.out`):
  - leading coefficient pj/2 per unit C(2j, j)μ_j;
  - N^{−2−jp} = N^{−4−jp} = 0;
  - N^{−3−jp}/N^{−1−jp} = A_j + B_jα², **as an identity in j**.
- **Second order in μ₁, K = 5** (`m4_zeta_exact2_B.out`), per unit μ₁²:
  - N^{−1−2p} = 0, N^{−2−2p} = p(3p+1)/2, N^{−3−2p} = 0, N^{−5−2p} = 0;
  - N^{−4−2p} = p²h₂, with **h₂ = (p+1)(p+2)(3p²+2p+1)/(8p²) + (p+2)(2p³−p²−7p−6)α²/(16p²)**.
  - With μ_{n,1}² = ε₁²n^{−2p}/(pc)², this is the bracket ε₁²N^{−2−2p}[(3p+1)/(2p) + h₂N⁻² + O(N⁻⁴)] of Theorem N.6(ii).

## 6. Proof of Theorem N.6

**(i)** By Paper 2 F8 / RH_px §5 (as in E2 §7, E_plt1 §7), n^{2p}b_n² = (Q₁)₁₂(Q₁)₂₁ with Q₁ = P₁ + R_1. By Prop N.6c,
R_1 = Σ_{m≤K}R_1⁽ᵐ⁾(μ_n)n^{−m} + O(n^{−K−1} + n^{−1−(J+1)p}). The n⁰ term of (Q₁)₁₂(Q₁)₂₁ is exactly c², since P₁ is μ-free
(review I2). So each d_k(μ) is a polynomial in the entries of R_1⁽ⁱ⁾(μ), i ≤ k. These entries are entire in μ (Lemma N.6b and
the algebraic recursion) and independent of n. Hence 𝔇_K(n; μ) is entire in μ with n-independent coefficients, and Taylor's
theorem with remainder in μ on |μ| ≤ 1 applies coefficientwise:
- the n⁰ coefficient is 1 for all μ;
- the n⁻¹ coefficient is d₁ + e(μ) with e(μ) = cpM_μ(4c), exactly linear (E3 Lemma E3.7, all μ);
- so for |β| ≥ 2, 𝔇_{β,K} = O(n⁻²), and the Taylor remainder after order B is O(|μ|^{B+1}n⁻²).

With |μ_n| = O(n^{−p}) this is O(n^{−2−(B+1)p}). Together with Prop N.6c this proves (i).

**(ii)** This is Lemma N.6d, read through the natural-form conversion: x = 1/N and 1/n = x/(1 − δx) with δ = α/2 + ½; the
μ^β layer carries n^{−|β|_w p} = N^{−|β|_w p}(N/n)^{|β|_w p}, where |β|_w = Σ_j jβ_j. This conversion is exact algebra, done in
the scripts (review A I1(d)). The normalisations are μ_{n,j}·C(2j, j)pc^jj/2 = ε_j and μ_{n,1}²·p(3p+1)/2 = ε₁²(3p+1)/(2p)
(c = 1, restored by the c-scaling of §5). The symbolic-j identity covers every j ≥ 1.

**(iii)** Take K = 6, B = 2, and J ≥ 6/p − 1, so that n^{−1−(J+1)p} = O(n⁻⁷). In (i), keep:
- β = 0 (the integer layer to K = 6);
- β = e_j for all j with 1 + jp < min(7, 2 + 3p), at K = 5 (j ≤ 5) or K = 4 (all j);
- β = 2e₁, at K = 5.

The remaining |β| = 2 terms are μ_n^β𝔇_β = O(n^{−3p}·n⁻²). Collecting the natural forms of (ii) with the remainder bookkeeping
of §1 proves (iii). ∎

## 7. Rule A (adversarial pass) — log

1. *Is "integer layer = model computation" circular?* No. Theorem N.6(i) splits the full expansion at μ = 0, which is exactly
   the model weight (E3 Lemma E3.4: G₀ = I). The band factor enters only through μ_n, with REVIEWED bounds (E3 Lemma F.1′,
   E_plt1 Lemma F.1).
2. *Exactness of the truncation logic.* Checked by review A (I1). Independent cross-checks:
   - the numerical version m4_rh4.py, at truncation depths 14–64;
   - the lattice fits, m4_f4_lattice.out and m4_zeta_lattice.out.
3. *Sector independence for all k.* This is now the tie argument (§2), with review A's k = 3 re-derivation and numerical
   sector checks.
4. *b_k.* Quoted from 10.17.8 at general k, and cross-checked against the term-wise derivative of 10.40.2 (k ≤ 8).
5. *Uniformity in μ.* The R_1⁽ᵐ⁾(μ) are n-independent, so the μ-Taylor bounds are uniform (§6).
6. *Visibility* (review F1). Theorem N.6 now separates the layer identities (ii), which hold for every p, from the b_n
   coefficients (iii), which come with the visibility table. A displayed term below the remainder is true but not
   determined, and the text says so.
7. *Symbolic j.* The Taylor data are valid for every integer j ≥ 1 (asserted against j ≤ 8; the formulas are exact
   consequences of the generating function). The rational functions in j have poles only at j = ½, which is not an
   integer.
8. *p < 1.* The changes are confined to §2 (sectors, glue), §3 (parity argument) and §4 (off-circle pieces). Each cites the
   REVIEWED p < 1 counterpart (E_plt1 Lemmas E′.3, E′.5, F.1; Prop E′.5′; E3 Prop E3.6). The algebra is p-free: the
   identities are rational in p, with poles only at p ∈ {0, −2/3, −2/5}.
9. *What is NOT proved:*
   - p = 1 (outside the frame, E3 §8);
   - the second-order layers other than μ₁² (μ₁μ₂, …), which sit in the remainder;
   - the μ₁² layer beyond N⁻⁵ relative;
   - evenness to all orders (proved here for the computed layers);
   - any closed form for F.

## 8. Note on 0 < p < 1

Theorem N.6 covers p < 1 with the same statement. The visibility table then gives, for example:
- f₄ is determined for p > 2/3, and f₆ for p > 4/3;
- for p < 2/3, f₄N⁻⁴ lies below the remainder O(n^{−2−3p}), which is controlled by the uncomputed μ₁μ₂ and μ₁³ layers.

For p < 1 the leading zeta terms ε_jN^{−1−jp} are determined for every j with (j − 3)p < 1. Their dressings g_j are
determined for j = 1 when p > ½ (j = 2 needs p > 1). At p = 1/j₀, ε_{j₀}N^{−1−j₀p} = ε_{j₀}N⁻² merges with f₂N⁻². This is
consistent with E3 Corollary E3.3(ii): there d₂ − p/12, here f₂ + ε_{j₀}, with ε_{j₀} = ζ(−1)/j₀ = −p/12.

## 9. Rule R review A (REVIEW_JZC_M4_proof_A.md, ACCEPT WITH FIXES): applied

- **F1 (MAJOR, visibility).** Theorem N.6 is restated as (i) double expansion, (ii) layer identities, (iii) b_n expansion
  with a visibility table. The review's alternative was also carried out: the μ₁² layer is now exact (m4_zeta_exact2 B), which
  improves the remainder from n^{−2−2p} to n^{−2−3p}. The Consequences and the JZC_M4.md labels are corrected.
- **F2.** The induction claim carries n^{−1−(J+1)p}, with running index m (§4).
- **F3.** The tie argument replaces "ξ(q^{±1}ζ) = −ξ(ζ)" (§2). E2 Lemma E2.3 has the same wording; a textual fix there is
  noted, not made, since E2 is REVIEWED and the fix belongs to its owner.
- **F4.** The parity statement is reworded, and the mutation-test results recorded (§3).
- **F5.** Remainder bookkeeping is added (§1).
- **F6.** All exact outputs are regenerated from the committed scripts, with sha256 lines.
- **F7.** The docstring is fixed; the c-scaling is stated as c^jμ_j (§5).
- **F8.** CITATIONS "(JZC M4 reuse)" now has the hypotheses line and the KMVV and Paper 2 model entries.
- **I2.** The μ-analyticity argument no longer uses "bounded away from 0" (§6).
