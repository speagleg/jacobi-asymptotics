# JZC M4 proof: the lattice expansion to order n⁻⁶ in natural form (Theorem N.6)

Status (2026-10-21): NOT REVIEWED (Rule A pass in §7; Rule R pending). Labels per VERIFICATION_POLICY.md. This note turns
JZC_M4 §5–§6 (Props N.3, N.4: CONDITIONAL + NUMERICAL) into a theorem for p > 1. It follows the order-2 proofs of E2_pgt1
(Plan E2, REVIEWED) and E3 (Plan E3, REVIEWED) and generalises them to every order K. The algebra is exact computer algebra in
(p, α), not reconstruction.

| # | Statement | Label |
|---|---|---|
| Lemma N.6a | jumps on the two circles to every order: P̂(P₀^∞)⁻¹ = I + Σ_{k≤K}Δ_k/n^k + O(n^{−K−1}), Δ_k from the general-k DLMF coefficients; Δ_k = G_{μ_n}Δ_k^{mod}G_{μ_n}⁻¹ + O(n^{−(J+1)p}) | PROVED-mod-cite (E2 Lemma E2.3 argument [REVIEWED] with DLMF 10.17.1, 10.17.5–6, 10.40.1–4, 9.7.1–2, 9.7.5–6 at general k, quoted in §2; E3 Lemmas E3.4–E3.5 [REVIEWED]) |
| Lemma N.6b | Δ_k^{mod} meromorphic in both discs for every k; Δ_k^μ likewise with Laurent coefficients entire in μ | PROVED (E2 Lemma E2.6(a) and E3 Lemma E3.4(iii) arguments, which do not depend on k) |
| Prop N.6c | small norm to order K: R = I + Σ_{k≤K}R⁽ᵏ⁾/n^k + O(n^{−K−1} + n^{−1−(J+1)p}), with R⁽ᵏ⁾ given by the residue recursion | PROVED-mod-cite (Paper 2 F1, F5, RH_px §5, E_pgt1 Prop E.5′, as in E2 Prop E2.5 [REVIEWED]; induction on K) |
| Lemma N.6d | the exact algebra: integer layer to N⁻⁶ and first-order zeta layer (j ≤ 5) to N⁻⁴ relative, identities in (p, α) | PROVED (exact computer algebra over ℚ(p, α)[i], m4_rh_exact.py, m4_zeta_exact.py; outputs m4_rh_exact_k4.out, m4_rh_exact_k6.out, m4_zeta_exact.out) |
| **Thm N.6** | p > 1, s > 1, α = (s−1)/p − 1, N = n + α/2 + ½: n^pb_n/c = (n/N)^p[1 + f₂N⁻² + f₄N⁻⁴ + f₆N⁻⁶ + Σ_{j≤5}ε_jN^{−1−jp}(1 + g_jN⁻² + O(N⁻⁴))] + O(n⁻⁷ + n^{−2−2p}) | PROVED-mod-cite (the four items above; E3 Lemma F.1′, Lemma E3.7 [REVIEWED]; Paper 2 F8) |

Consequences:
- f₁ = f₃ = f₅ = 0: Conjecture S1-N's "no N⁻¹, no N⁻³" holds to N⁻⁶, for every p > 1.
- f₂, f₄, f₆ and g_j (j ≤ 5) are the closed forms of JZC_M4 §5–§6, now proved.
- Each ε_j term is even in 1/N to the order computed.

## 1. Statement

Notation as in E_pgt1 §0, E2 §0 and E3 §0 (Q-frame, P₀^∞, T, M, the circles ∂U_0, ∂U_r around 0 and 4c, c = c(p)). For μ ∈ ℂ^J
let G_μ be E3's gauge (Lemma E3.4(ii)), and put Δ_k^μ := G_μΔ_k^{mod}G_μ⁻¹. Here Δ_k^{mod} is defined in Lemma N.6a.

**Residue recursion.** Set R_in⁽⁰⁾ := I near each of e ∈ {0, 4c}, and for k ≥ 1 put
- F_k(μ) := Σ_{j=1}^k R_in⁽ᵏ⁻ʲ⁾(μ)Δ_j^μ, meromorphic in each disc;
- R_out⁽ᵏ⁾(μ) := the sum of the principal parts of F_k(μ) at 0 and at 4c;
- R_in⁽ᵏ⁾(μ) := R_out⁽ᵏ⁾(μ) − F_k(μ), analytic in each disc (the principal part at that point cancels);
- R_1⁽ᵏ⁾(μ) := Res₀F_k(μ) + Res_{4c}F_k(μ).

For k = 1, 2 this is E2 Prop E2.5 and E3 Prop E3.6.

**Theorem N.6 (PROVED-mod-cite).** Let p > 1, s > 1, K ≥ 1 and J ≥ 1, and let μ_n := (μ_{n,j})_{j≤J} with
μ_{n,j} = 2ζ(−jp)/(jn^{jp}) (E3 Lemma F.1′).
(i) n^{2p}b_n² = (Q₁)₁₂(Q₁)₂₁ with Q₁ = P₁ + Σ_{k≤K}R_1⁽ᵏ⁾(μ_n)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}).
(ii) Write 𝔇_K(n; μ) := √((Q₁)₁₂(Q₁)₂₁)/c, with Q₁ = P₁ + Σ_{k≤K}R_1⁽ᵏ⁾(μ)n^{−k}, expanded to order n^{−K}. Then
  - 𝔇_K(n; μ) = 𝔇_K(n; 0) + Σ_jμ_j∂_{μ_j}𝔇_K(n; 0) + O(|μ|²n⁻²) uniformly for |μ| ≤ 1;
  - hence n^pb_n/c = 𝔇_K(n; 0) + Σ_jμ_{n,j}∂_{μ_j}𝔇_K(n; 0) + O(n^{−K−1} + n^{−2−2p} + n^{−1−(J+1)p}).
(iii) With K = 6 and J = 5, and with the exact algebra of Lemma N.6d, this is
  n^pb_n/c = (n/N)^p[1 + f₂N⁻² + f₄N⁻⁴ + f₆N⁻⁶ + Σ_{j=1}^5ε_jN^{−1−jp}(1 + g_jN⁻² + O(N⁻⁴))] + O(n⁻⁷ + n^{−2−2p}),
  where:
  - ε_j = C(2j, j)pc^jζ(−jp);
  - f₂ = −(p+2)α²/8 + (p+1)/12;
  - f₄, f₆ are the closed forms of JZC_M4 §5;
  - g_j = A_j + B_jα² as in JZC_M4 §6 (A_j and B_j are proved for j ≤ 5; the formula in j is still a reconstruction).

  The term n^{−1−6p} = o(n⁻⁷) has been absorbed.

Remarks:
- The remainder n^{−2−2p} is the second order in μ (the ζ(−p)² layer). Its first term, (3p+1)/(2p)·ε₁²N^{−2−2p}, is
  NUMERICAL (JZC_M4 §6).
- The ε_j terms with 1 + jp ≥ 7 are inside the remainder; they are kept for uniformity.

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
- The proof of E2 Lemma E2.3 goes through verbatim with K + 1 terms in place of 3. In each sector, one column carries the
  (−1)^k pattern (I_α, Ai at the rotated argument) and the other the + pattern (K_α, the Hankel pair). Review A B2 of Plan E2
  showed that this sign assignment, hence C_k and Ξ_k, X_k, does not depend on the sector **for every k**. (The phases are
  k-independent, and the k-th terms carry (−1)^k exactly where y₀, I_α do.)
- With w = 2nf^{1/2} and ξ = −nφ̃ (both ≍ n on the circles), the Poincaré remainders O(w^{−K−1}) and O(ξ^{−K−1}) are
  O(n^{−K−1}) uniformly.
- The n-dependence of the weight is E3 Lemma E3.5. Its proof uses only that Δ_k depends analytically on (ρ²)^{±1} and
  (−ω)^{±1/2}, with no restriction on k; with E3 Lemma F.1′ at order J it gives the stated O(n^{−(J+1)p}).
- The conjugation formulas are E3 Lemma E3.4(iii), whose proof is also k-free: it commutes diagonal factors. ∎

## 3. Lemma N.6b: meromorphy for every k

E2 Lemma E2.6(a) (review A B1) argues as follows. G_n := P̂^{mod}(P₀^∞)⁻¹ is analytic in U_e ∖ {e}, the expansion of Lemma
N.6a holds uniformly on compacts K ⊂ U_e ∖ {e}, and so Δ_k = lim n^k(G_n − I − Σ_{i<k}Δ_in^{−i}) is analytic and single-valued in
U_e ∖ {e}. Its explicit formula grows at most polynomially at e, so e is a pole. Nothing in this depends on k. The gauge G_μ is
entire in (z, μ) (E3 Lemma E3.4(ii)), so Δ_k^μ is meromorphic with Laurent coefficients entire in μ.

Computer-algebra confirmation, exact, in m4_rh_exact.py:
- for every k ≤ 6, u^{3k+1}Δ_k^r has only even powers of u = (z − 4c)^{1/2}, and the v-series of Δ_k^0 (z = −v²) only even
  powers (asserted by `u_to_w`);
- each R_in⁽ᵏ⁾ is analytic at both points (asserted).

## 4. Proposition N.6c: small norm to order K

**Proposition N.6c.** Let p > 1. With R⁽ᵏ⁾ := R_out⁽ᵏ⁾(μ_n) outside the discs and R_in⁽ᵏ⁾(μ_n) inside,
R(z) = I + Σ_{k≤K}R⁽ᵏ⁾(z)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}) uniformly at distance ≥ d > 0 from Σ_R. Also
R_1 = Σ_{k≤K}R_1⁽ᵏ⁾(μ_n)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}).

*Proof.* Write η_n := n^{−K−1} + n^{−1−(J+1)p}.
- **Jumps.** As in E2 Prop E2.5, J − I = Σ_{k≤K}Δ_k^{μ_n}χ_circ n^{−k} + E. Off the circles E is O(e^{−n/C}), O(n^{−pn/4}) or
  O(n^{−K′}min(1, |z|^{K′})) for any K′ (hard-edge mismatch), on total length O(n^p), exactly as in E_pgt1 Prop E.5′. On the
  circles E = O(η_n) (Lemma N.6a). So ‖E‖_{L¹∩L²∩L^∞} = O(η_n) and ‖J − I‖_{L²∩L^∞} = O(1/n).
- **Small norm.** ‖𝒞₋‖_{L²→L²} ≤ C (Paper 2 F1), so for large n the equation R₋ = I + 𝒞₋(R₋(J − I)) has a unique solution
  with ‖R₋ − I‖_{L²} = O(1/n).
- **Induction claim:** R₋ = Σ_{k<K}R₋⁽ᵏ⁾n^{−k} + O_{L²}(n^{−K}). Here R₋⁽⁰⁾ = I, and R₋⁽ᵏ⁾ is the minus-side boundary value of
  R⁽ᵏ⁾, which is R_in⁽ᵏ⁾ on the clockwise circles and R_out⁽ᵏ⁾ elsewhere.
  - K = 1 is the small-norm bound.
  - Step: insert the claim into R = I + 𝒞(R₋(J − I)).
    - The terms with k + j ≥ K + 1 are O(n^{−K−1}).
    - The off-circle part of J − I paired with bounded R₋⁽ᵏ⁾ is O(η_n). Off the discs, R_out⁽ᵏ⁾ is bounded and O(1/|z|),
      and the super-small jump beats the polynomial length.
    - So R − I = Σ_{m=1}^{K}𝒞(Σ_{j=1}^mR₋⁽ᵐ⁻ʲ⁾Δ_j^{μ_n}χ_circ)n^{−m} + O(η_n) uniformly off the contour (Cauchy–Schwarz
      against the kernel, as in E_pgt1), and in L² on the contour (𝒞₋ bounded).
  - Identify each term: on the circles R₋⁽ᵐ⁻ʲ⁾ = R_in⁽ᵐ⁻ʲ⁾, so the integrand is F_m(μ_n)χ_circ with F_m meromorphic in the
    discs (Lemma N.6b). For such F, (1/2πi)∮_{cw}F(s)ds/(s − z) is the sum of the principal parts of F at 0 and 4c when z is
    outside the discs, and that sum minus F when z is inside (residue theorem). This is R_out⁽ᵐ⁾ and R_in⁽ᵐ⁾, so 𝒞(…) = R⁽ᵐ⁾
    and 𝒞₋(…) = R₋⁽ᵐ⁾. This closes the induction and gives the expansion of R.
- **Moment.** R_1 = −(1/2πi)∫_{Σ_R}R₋(J − I)ds with the same splitting, and −(1/2πi)∮_{cw}F_m ds = Res₀F_m + Res_{4c}F_m. ∎

(The proof is E2 Prop E2.5's, with the second Neumann iterate replaced by the K-th. The only new point is the identification
of iterated Cauchy transforms of circle restrictions with the residue recursion, which is the residue theorem applied once
per order.)

## 5. Lemma N.6d: the exact algebra

**Lemma N.6d (PROVED; exact computer algebra).**
- `checks/m4_rh_exact.py` carries out the residue recursion of §1 and the extraction of Theorem N.6(i) for the model weight
  (μ = 0), in exact arithmetic over the field ℚ(p, α)[i], with c = 1.
  - All inputs are rational functions of (p, α) once c = 1:
    - the series of E2 Lemma E2.4 have rational coefficients;
    - π cancels in f = −(π²/4)z𝔞²;
    - the square roots are of series with leading coefficient 1 or a perfect square: f^{1/2} ∼ v/(p+2), (4 + v²)^{1/2} ∼ 2;
    - the factors 1/√2 in T and M occur in conjugate pairs.
  - d₂ does not depend on c (E2 §1), and nothing does: every input depends on z/c only.
  - Truncation is controlled by tracking, for every series, the highest coefficient that is exactly known. Each principal
    part asserts that its coefficients down to the residue are known (the run fails otherwise).
- `checks/m4_zeta_exact.py` does the same with first-order dual numbers (ε² = 0) for the first-order gauge
  G_μ = I + μ_j𝒢_j + O(μ²), 𝒢_j = T[[0, −(z−4c)Q_j/2], [−zQ_j/2, 0]]T⁻¹. These are the μ_j-derivatives at μ = 0 of
  cosh h = 1 + O(μ²) and S = sinh(h)/𝓡 = M_μ/2 + O(μ³), from E3 Lemma E3.4(ii). Hence ∂_{μ_j}Δ_k^μ|₀ = [𝒢_j, Δ_k^{mod}].

Results:
- **K = 6** (m4_rh_exact_k6.out). Identically in (p, α):
  - d₁ = −p(α+1)/2 and d₂ = E2 Theorem E2.1;
  - in natural form (N = n + α/2 + ½), f₁ = f₃ = f₅ = 0, f₂ = −(p+2)α²/8 + (p+1)/12, and f₄, f₆ equal the closed forms of
    JZC_M4 §5.
- **First-order zeta layer, j = 1, …, 5, K = 5** (m4_zeta_exact.out). Identically in (p, α), the response to μ_j in natural
  form, (N/n)^{(j+1)p}Σ_k∂_{μ_j}d_k n^{−k}, has:
  - N^{−1−jp} coefficient C(2j, j)pj/2 (so μ_{n,j} gives ε_j);
  - vanishing N^{−2−jp} and N^{−4−jp} coefficients;
  - N^{−3−jp}/N^{−1−jp} = A_j + B_jα²;
  - for j = 1, N^{−5−p}/N^{−1−p} equal to the closed form g₁,₄ of JZC_M4 §6.
- The DLMF coefficient identities of §2 are asserted for k ≤ 8.

## 6. Proof of Theorem N.6

(i) is Paper 2 F8 / RH_px §5 (n^{2p}b_n² = (Q₁)₁₂(Q₁)₂₁ with Q₁ = P₁ + R_1, as in E2 §7), with Prop N.6c.

(ii) The R_1⁽ᵏ⁾(μ) are entire in μ (Lemma N.6b and the algebraic recursion), and (Q₁)₁₂(Q₁)₂₁ = c²(1 + O(1/n)) is bounded away
from 0. So 𝔇_K(n; μ) is analytic in μ for |μ| ≤ 1, with coefficients bounded uniformly in n, and Taylor's theorem in μ gives
the first-order expansion with remainder O(|μ|²). The n⁰ coefficient of 𝔇 is 1 (P₁ is μ-free). The n⁻¹ coefficient is
d₁ + e(μ) with e(μ) = cpM_μ(4c) exactly linear in μ (E3 Lemma E3.7, all μ). So the μ-quadratic remainder is O(|μ|²n⁻²). With
|μ_n| = O(n^{−p}) this is O(n^{−2−2p}).

(iii) Take K = 6 and J = 5, so that n^{−1−6p} = o(n⁻⁷) for p > 1. 𝔇₆(n; 0) is the integer layer computed exactly in Lemma N.6d.
Its natural form is (n/N)^p(1 + f₂N⁻² + f₄N⁻⁴ + f₆N⁻⁶) + O(n⁻⁷): re-expanding a finite series in 1/n as a series in 1/N, with
N − n = α/2 + ½ fixed, is exact algebra, done in the script.

For each j ≤ 5, μ_{n,j}∂_{μ_j}𝔇₅(n; 0) = (2ζ(−jp)/(jn^{jp}))Σ_{k≤5}∂_{μ_j}d_kn^{−k}. Its natural form is ε_jN^{−1−jp}·(1 + g_jN⁻² +
O(N⁻⁴)), using:
- n^{−jp} = N^{−jp}(N/n)^{jp};
- Lemma N.6d (the coefficient C(2j, j)pj/2 times 2ζ(−jp)/j is C(2j, j)pζ(−jp) = ε_j at c = 1; c-scaling restores c^j);
- the vanishing N^{−2−jp} coefficient.

The truncation at K = 5 for the zeta part costs O(n^{−6−p}) = o(n⁻⁷). Collecting terms proves (iii). ∎

## 7. Rule A (adversarial pass) — log

1. *Is "integer layer = model computation" circular?* No. Theorem N.6(ii) splits the full expansion at μ = 0, and μ = 0 is
   exactly the model weight (E3 Lemma E3.4: G₀ = I). The band factor enters only through μ_n, with E3's REVIEWED bounds.
2. *Exactness of the truncation logic.* Precision tracking follows the rules: product hi = min(hi₁ + lo₂, hi₂ + lo₁); inverse
   and powers keep relative precision; u → w halves hi; z → v gives 2hi + 1, since the next odd v-power is zero by parity.
   The principal-part guard makes the run fail rather than return a wrong residue. Two cross-checks:
   - the numerical version (m4_rh4.py), whose truncation depth was varied (14–64) with identical output;
   - the lattice fits (m4_f4_lattice.out, m4_zeta_lattice.out).
3. *Sector independence for all k* (Lemma N.6a). This is the one place where the order-2 proof said "for every k" without
   writing k > 2 out. The numerical check of Plan E2 (check_e2_num) tests k = 2 only. The argument itself is k-uniform:
   the phases are k-independent, and the (−1)^k sits on the same column in every sector. Two consistency checks at k ≤ 6:
   - meromorphy of every Δ_k (asserted; like E2's parity check, it tests branches and signs but does not detect every
     possible swap);
   - the independent lattice fits, which see the k ≤ 4 data through f₄: m4_f4_lattice.out agrees to 3·10⁻¹⁰ at p = 4.
   A Rule R reader should still re-derive one sector at k = 3 by hand.
4. *b_k.* Quoted from 10.17.8 at general k (CITATIONS, Plan 55). It is also cross-checked against the term-wise derivative of
   10.40.2 (asserted, k ≤ 8).
5. *Uniformity in μ* (Thm N.6(ii)). The bound on the μ-Taylor remainder needs the R_1⁽ᵏ⁾(μ) to be bounded on |μ| ≤ 1
   uniformly in n. They are n-independent (μ is a free parameter; n enters only through μ_n), so this holds.
6. *What is NOT proved:*
   - p ≤ 1. The p < 1 frame (E_plt1, E3 Prop E3.6) supports the same induction, but it is not written.
   - The ζ(−p)² coefficient (3p+1)/(2p) (NUMERICAL).
   - A_j, B_j as functions of j beyond j ≤ 5 (reconstruction).
   - The general-order evenness (proved here to N⁻⁶ only).
   - Any closed form for F.
7. *c-normalisation.* The exact algebra uses c = 1. Every model input depends on z/c only (E2 review B F2), and the gauge
   coefficient scales as c^{j−1} through Q_j. The leading coefficient C(2j, j)pj/2 at c = 1 becomes C(2j, j)pc^jj/2 in general,
   consistent with E3 Lemma E3.7 at j = 1 (cpμ₁) and with ε_j.
