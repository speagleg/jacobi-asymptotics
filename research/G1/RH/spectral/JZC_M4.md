# JZC M4: the second-order layer — the natural index N = n + α/2 − Z(0) (Plan JZC, milestone M4; first results)

Status (2026-10-21): NOT REVIEWED. **Proof of Props N.3–N.4 (p > 1, to N⁻⁶): JZC_M4_proof.md (Theorem N.6).** §5 added 2026-10-21 (integer layer to order 8); §6 added 2026-10-21 (zeta layer in natural form). Labels per VERIFICATION_POLICY.md.

| # | Statement | Label |
|---|---|---|
| Identity N.1 | E2's d₂(p, s) = p(p+1)δ_N²/2 + f₂(p, α), δ_N := α/2 + ½, f₂ := −(p+2)α²/8 + (p+1)/12, α := (s−1)/p − 1 | PROVED (algebra) |
| Prop N.2 | Bessel-zero (Lommel) measures, p = s = 2 (α = −½): n²b_n/c = (n/N)²·(1 − 1/(4N²))^{−1/2} exactly, N = n + μ/2 = n + α/2 − Z(0) | PROVED (from the Lommel closed form, SPEC §3.10) |
| Conj S1-N | n^pb_n/c = (n/N)^p·F_{p,α}(N; Z), N := n + α/2 − Z(0). F has no 1/N term; its integer layer is even in 1/N; its N⁻² coefficient is f₂; the spectral terms (zeta layer, poles) appear as functions of N | CONJECTURE (NUMERICAL: m4_natural_index.out, 7 lattices; S1′, rule H, S1⁗ as instances). The integer-layer part is now established through order 8 for the Riemann–Hilbert model: Prop N.3 |
| Prop N.4 | Zeta layer with the band factor (E3 gauge added to the order-k computation): each ε_j term is ε_jN^{−1−jp}·(1 + g_jN⁻² + O(N⁻⁴)), even in 1/N, with g_j = A_j + B_jα² in closed form for all j (§6); the ζ(−p)² layer starts at (ε₁N^{−1−p})²·(3p+1)/(2p) | **p > 1, j ≤ 5, first order in μ, to N⁻⁴ relative: PROVED-mod-cite (Theorem N.6; exact algebra m4_zeta_exact).** The j-dependence of A_j, B_j for j > 5 and the ζ(−p)² coefficient (3p+1)/(2p): NUMERICAL (m4_zeta_dressing.out) |
| Conj S1-N′ | refined S1-N: F_{p,α} is a function of N⁻² and the monomials X_j := ε_jN^{−1−jp} only, i.e. F = Σ_β c_β(N⁻²)ΠX_j^{β_j} with each c_β an even series | CONJECTURE (evidence: Prop N.3, N.4; tested for β ∈ {0, e_j (j ≤ 5), 2e₁}) |
| Prop N.3 | Integer layer from the order-k Riemann–Hilbert model computation (E2's frame, extended from k = 2 to k = 8): f₁ = f₃ = f₅ = f₇ = 0; f₄, f₆ in closed form (§5); f_{2k} is even in α | **p > 1, through N⁻⁶: PROVED-mod-cite (JZC_M4_proof.md Theorem N.6; exact computer algebra m4_rh_exact).** f₈ and orders beyond N⁻⁶: NUMERICAL (m4_rh4.out, m4_f8_denominator.out); p < 1: CONDITIONAL (frame of E_plt1/E3, not written) |

## 1. The identity

E2 Theorem E2.1: d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12. With α = (s−1)/p − 1, s − 1 = p(α + 1) and s − 1 − p = pα.
- The first term is (p+1)p(α+1)²/8 = p(p+1)δ_N²/2, with δ_N = (α+1)/2.
- The second term is −(p+2)α²/8.
So **d₂ = p(p+1)δ_N²/2 + f₂**. The first term is exactly the n⁻² term produced by the index shift n → n + δ_N in (n/N)^p:
(1 + δ/n)^{−p} = 1 − pδ/n + p(p+1)δ²/(2n²) − …

The 1/n term of the same shift is −pδ_N = −p(α + 1)/2 = −(s − 1)/2 = d₁. So **the lattice's d₁ and the (s − 1)² part of d₂ are a
single index shift by δ_N = α/2 + ½**, and f₂ is what is left.

## 2. The natural index

For a regular spectrum, d₁ = −pα/2 + pZ(0) (S1) = −p(α/2 − Z(0)). So the shift is N = n + α/2 − Z(0). It has two parts:
- **α/2: the hard-edge shift.** The band [0, 4c] has a hard edge at 0 with Jacobi exponent α (the model weight z^α). As for
  Laguerre (b_n = √(n(n + α)) = N√(1 − α²/(4N²)), N = n + α/2) and Jacobi (rational in 2n + α + β + 1) polynomials, the hard
  edge shifts the natural index by α/2. The soft edge (Airy) is symmetric and contributes no shift.
- **−Z(0): the spectral shift.** The regularised count of the nodes (S1), i.e. the Hurwitz offset δ in rule H.

**Proposition N.2 (Bessel zeros; exact).** The Lommel closed form (SPEC §3.10) is n²b_n/c = 4n²/((2n + μ)√((2n + μ)² − 1)). With
N := n + μ/2 this is (n/N)²·(1 − 1/(4N²))^{−1/2}. For these measures p = 2 and s = 2, so α = −½, and Z(0) = −μ/2 − ¼ (SPEC §3.9).
Hence α/2 − Z(0) = μ/2: the natural index. The bare function F = (1 − 1/(4N²))^{−1/2} = 1 + 1/(8N²) + 3/(128N⁴) + … has
- no 1/N term;
- only even powers;
- N⁻² coefficient 1/8 = f₂(2, −½) = −4·(1/4)/8 + 3/12. ∎
(At μ = ½, the lattice λ = (πk)², this gives d₂ = 3·(1/16) + 1/8 = 5/16 = E3's d₂(2, 2), as noted in SPEC §3.9.)

## 3. Conjecture S1-N and evidence

**Conjecture S1-N.** For a regular spectrum, n^pb_n/c = (n/N)^p·F_{p,α}(N; Z) with N = n + α/2 − Z(0), where:
- the integer layer of F is 1 + f₂N⁻² + f₄N⁻⁴ + …: even, with no N⁻¹ and no N⁻³ term;
- f₂ = −(p+2)α²/8 + (p+1)/12;
- the spectral terms are those of S1′/S1″ written in N: ε_jN^{−1−jp}, pole terms pRW(q)π cot(πq)N^{−1−pq};
- the Jacobian-tilt term of S1⁗ (SPEC §3.15) is a separate first-order density effect.

Its instances:
- **S1′ (I)** (the integer layer is the lattice's at n + δ) and **rule H** (both layers at n + δ, with Hurwitz ζ). These are
  S1-N with Z(0) = ζ(0, a) = ½ − a, i.e. −Z(0) = ½ + δ.
- **S1⁗'s shift term** (the pole term evaluated at n + δ_eff, δ_eff = (s − 1)/(2p)). This is S1-N's δ_N for the lattice, since
  (s − 1)/(2p) = (α + 1)/2. The identification there came from data; here it is structural.

**New test: no N⁻³ term** (`checks/m4_natural_index.py`, `checks/m4_natural_index.out`). Plan 62 lattice coefficients are mapped
to F(N) = (N/n)^p·n^pb_n/c. The script subtracts 1 + f₂N⁻² + Σε_jN^{−1−jp} and fits the remainder in powers of 1/N, with
nuisance exponents (4, 5, 2 + jp, 3 + jp). Results:

| p | s | α | N⁻¹ residual | N⁻² residual | N⁻³ residual (spread) |
|---|---|---|---|---|---|
| 1.5 | 2 | −⅓ | −4·10⁻¹¹ | +1.5·10⁻⁷ | −3.0·10⁻⁴ (2·10⁻⁴) |
| 1.5 | 3 | +⅓ | +5·10⁻¹¹ | −1.6·10⁻⁷ | +3.2·10⁻⁴ (2·10⁻⁴) |
| 1.25 | 2 | −0.2 | +4·10⁻¹¹ | −1.5·10⁻⁷ | +5.2·10⁻⁴ (4·10⁻⁴) |
| 2.5 | 2 | −0.6 | −2·10⁻¹¹ | +5·10⁻⁸ | −6·10⁻⁵ (6·10⁻⁵) |
| 3 | 2 | −⅔ | +2·10⁻¹² | −4·10⁻⁹ | +2.3·10⁻⁶ (5·10⁻⁷) |
| 1.5 | 2.5 | 0 | +2·10⁻¹² | −7·10⁻⁹ | +1.3·10⁻⁵ (2·10⁻⁵) |
| 2 | 3 | 0 | −2·10⁻¹³ | +4·10⁻¹⁰ | −3·10⁻⁷ (3·10⁻⁷) |

- The N⁻¹ and N⁻² rows re-confirm E2's d₁ and d₂ (PROVED) in natural form.
- The N⁻³ row is the new content. It is zero to ≤ 5·10⁻⁴, against lattice d₃ values of order 0.1–1 (for example −0.267 at
  p = 1.5, s = 2). At α = 0 it is ≤ 10⁻⁵.
- *Resolved (§5).* The residual at p = 1.5 flips sign with α (−3.0·10⁻⁴ at α = −⅓, +3.2·10⁻⁴ at α = +⅓, both about 1.5
  spreads), and p = 3 shows 2·10⁻⁶ at about 4 spreads. This is fit noise, not an odd-in-α N⁻³ term. The large-n end of the
  coefficients is noise-dominated at the N⁻³/N⁻⁴ scale (residual·N⁴ wanders by 10⁻³ beyond n ≈ 600), and these fits used the
  tail windows n ≥ 200, 400. Mid-range windows (n ∈ [10, 400]) give N⁻³ coefficients ≤ 4·10⁻⁸ (m4_f4_lattice.out), and the
  Riemann–Hilbert model gives f₃ = 0 to 10⁻³⁸.

**What S1-N buys.** It halves the unknowns of the integer layer, since only the even f_{2k}(p, α) remain. It unifies d₁, rule H and
the S1⁗ shift. And it gives M3/M4 a precise target: the Riemann–Hilbert analysis should produce exactly the shift α/2 (hard-edge
Bessel parametrix of order α) and −Z(0) (the Γ normalisation of the interpolation), with the soft edge contributing only even
terms.

## 5. The integer layer to eighth order (Proposition N.3)

**Method** (`checks/m4_rh4.py`). E2 (E2_pgt1, check_e2_sym) obtained d₂ from the second-order small-norm expansion of the
Riemann–Hilbert problem with the *model* weight z^α(4c − z), i.e. with the band factor H_n replaced by a constant. H_n is the
source of the zeta layer and the pole terms (E3, SPEC §3.12), so the model computation is the **integer layer**. The script
extends E2's computation to arbitrary order k:
- jumps J = I + Σ_k Δ_k/n^k on the circles around 4c (Airy) and 0 (Bessel), with
  - X_k = M⁻¹(M∘C_k), C_k = [[u_k, (−1)^k u_k], [v_k, (−1)^k v_k]] (u_k, v_k: DLMF 9.7.2);
  - Ξ_k = M⁻¹(M∘C_k), C_k = [[(−1)^k a_k, a_k], [(−1)^k b_k, b_k]] (a_k: DLMF 10.17.1; b_k: DLMF 10.17.8);
  - for k = 1, 2 these reproduce check_e2_sym's matrices (asserted);
- the same conjugations and local maps as E2 (Lemma E2.4 series);
- the small-norm recursion R_out⁽ᵏ⁾ = principal parts at {0, 4c} of Σ_{j=1}^k R_in⁽ᵏ⁻ʲ⁾Δ_j, R_in⁽ᵏ⁾ = R_out⁽ᵏ⁾ − Σ_j R_in⁽ᵏ⁻ʲ⁾Δ_j
  (analyticity of R_in⁽ᵏ⁾ at both points is asserted at each step);
- E2's extraction, n^pb_n/c = √(Q₁₂Q₂₁)/c with Q₁ = P₁ + Σ_k n⁻ᵏR₁⁽ᵏ⁾.
The arithmetic is numerical (mpmath, 40 digits) on truncated Laurent series with tracked precision, at given (p, α). The
results do not change when the truncation depth is raised (40 → 56 → 64).

**Results.**
- d₁ and d₂ reproduce E2 Theorem E2.1 to 10⁻²⁸ at every point, including p < 1 and α up to 2.6.
- **f₁ = f₃ = f₅ = f₇ = 0** (≤ 10⁻³⁵) at every sampled (p, α), p ∈ [⅓, 12]: the integer layer of F is even in 1/N.
- **f_{2k} is even in α.** Each f_{2k} is a polynomial of degree 2k in α with only even powers.
- **Closed forms.** Exact rationals at 12 (f₄) and 16 (f₆) values of p, each at 5–6 values of α, were interpolated by
  rational functions of p. f₄'s constant term needed 5 points and was checked on 7 more; f₆'s coefficients needed 8–10 points
  and were checked on 6–8 more:

  **f₄** = (p+1)(6p³ + 46p² + 55p + 3)/(1440 p(3p+2)) − 5(p+1)(p+2)α²/(96(3p+2)) − p(p+2)²α⁴/(128(3p+2)),

  **f₆** = [c₀ + c₂α² + c₄α⁴ + c₆α⁶]/((3p+2)²(5p+2)), with
  - c₀ = −(p+1)(450p⁸ + 1590p⁷ − 316p⁶ − 23761p⁵ − 66864p⁴ − 65507p³ − 18220p² − 1632p − 40)/(362880p²),
  - c₂ = (p+1)(p+2)(90p⁶ + 270p⁵ + 664p⁴ − 165p³ − 1649p² − 288p + 28)/(11520p),
  - c₄ = −(p+1)(p+2)²(20p⁴ + 45p³ + 162p² + 72p + 16)/1536,
  - c₆ = p(p+2)³(16p³ + 7p² − 4p − 4)/3072.

  Both are asserted at six points not used in the interpolation (`m4_rh4.out`, 58 checks):
  (9/4, 0.3), (0.4, −0.7), (7/5, 1.1), (11/2, −0.45), (0.8, 2.6), and the Bessel anchor (2, −½), where f₄ = 3/128 and
  f₆ = 5/1024, the coefficients of (1 − 1/(4N²))^{−1/2} (Prop N.2).
- **The denominators come from the hard-edge local map.** The series of 𝔞 (E2 Lemma E2.4(i)) has the factors
  1/(a′ + k), a′ = 1/p + ½, and a′ + k = ((2k+1)p + 2)/(2p). f₄ carries 3p+2, f₆ carries (3p+2)²(5p+2), and the prediction
  for f₈ is (3p+2)³(5p+2)(7p+2). It is confirmed at p = 3: the exact f₈(3, 0) = 1311857/632311515, with denominator
  3⁵·5·11³·17·23 = 3⁵·5·(3p+2)³(5p+2)(7p+2) (`m4_f8_denominator.out`; f₅ = f₇ = 0 there too, and f₈(2, 0) = 3899/2²¹).
- **Lattice cross-check** (`m4_f4_lattice.out`, 10 checks). Mid-window fits of the Plan 62 coefficients agree with f₄ to
  3·10⁻¹⁰ (p = 4, α = 0), 8·10⁻⁸ (p = 2, α = 0; p = 4, α = 1), 4·10⁻⁷ (p = 2, α = 1), and 5·10⁻⁵ at p = 2.5 (fit spread
  10⁻⁴). The fitted N⁻³ coefficient is ≤ 4·10⁻⁸ in all five cases. The model's integer layer is therefore the lattice's at
  N⁻⁴, as it should be when no zeta exponent 1 + jp lands on 4.

**Status and labels.**
- The computation is the formal order-k expansion. Making it a theorem needs E2's estimates at order k: jumps to order k + 1
  with uniform remainders (the DLMF expansions to k + 1 terms, as in Lemma E2.3), and the small-norm series to order k
  (Prop E2.5). Both are routine extensions, but they are not written: **CONDITIONAL**.
- The closed forms rest on rational reconstruction from finitely many exact evaluations, with out-of-sample verification:
  **NUMERICAL**.
- Rule X: the f₄(2, α) polynomial (23 − 40α² − 16α⁴)/512 was first read off lattice fits. The Riemann–Hilbert computation
  was then built independently and reproduced it exactly, then gave all p.

**Why even in α (HEURISTIC).** The Bessel data a_k(α), b_k(α) depend on α only through α² (DLMF 10.17.1, 10.17.8). Elsewhere,
α enters only through the power ρ^{2(α+1)} at the hard edge and the matching power at the soft edge (the Szegő-type
factor of z^α). For Laguerre polynomials, the same structure produces exactly the index shift n → n + α/2. So, to all
orders, the α-odd part should be absorbed by the shift in N = n + α/2 + ½. This is a candidate route to deriving the α/2 part
of the natural index. The evenness in 1/N suggests a reflection symmetry N → −N of the model problem, also not yet
identified.

## 6. The zeta layer in natural form (Proposition N.4, Conjecture S1-N′)

**Method** (`checks/m4_zeta_dressing.py`). E3 (Lemmas E3.4–E3.5, REVIEWED) gives the band factor exactly: up to O(n^{−(K+1)p}),
H_n ∝ exp(−Σ_kμ_{n,k}x^k) with μ_{n,k} = 2ζ(−kp)/(kn^{kp}). Every jump transforms by the entire gauge,
Δ_k^μ = G_μΔ_k^{mod}G_μ^{−1}, with G_μ = T[[cosh h, −(z−4c)S], [−zS, cosh h]]T⁻¹, h = 𝓡M_μ/2, S = sinh(h)/𝓡,
M_μ = Σμ_kQ_k. Adding this gauge to the order-k computation (`m4_rh4.run(..., mu=...)`) gives the zeta layer to every order in
1/n. Derivatives in μ are taken by central differences at 50 digits. A response Σ_ke_kn^{−k} multiplying n^{−jp} becomes, in
natural form, (N/n)^{(j+1)p}Σ_ke_kn^{−k} expanded in 1/N.

**Results.**
- **First order in μ_j (j = 1, …, 5).** The leading coefficient is ε_j = C(2j, j)pc^jζ(−jp), E3's Lemma E3.7, reproduced at
  10⁻¹⁸. The N^{−2−jp} and N^{−4−jp} coefficients vanish (≤ 10⁻¹⁷). So each zeta term is **ε_jN^{−1−jp}·(1 + g_jN⁻² + …)**,
  even in 1/N, with

  **g_j = A_j + B_jα²**,
  - B_j = (p+2)(j²p² + (j+1)p + 2)/(8(2j−1)p),
  - A_j = [j²(j²+2j−2)p³ + 2(j+1)(2j²−1)p² + (5j²+2j−6)p + 2(j−2)]/(24(2j−1)p).

  For j = 1 these are (p+1)(p²+3p−2)/(24p) and (p+2)(p²+2p+2)/(8p).
  - Each j was reconstructed in p from exact values at 12–14 values of p, with 8–10 spare points as checks.
  - The j-dependence was read off from j = 1, …, 5. B_j was guessed from j ≤ 3 and then confirmed at j = 4, 5; the p³ and p¹
    coefficients of A_j were guessed from j ≤ 3 and confirmed at j = 4, 5; the p² coefficient (cubic in j) is determined by
    j ≤ 4 and checked at j = 5.
  - g_j is even in α (verified at α = ±1, ±2) and exactly quadratic: there is no α⁴ term.
- **Next order, j = 1.** The N^{−5−p}/N^{−1−p} ratio is
  (p+1)(9p⁶+117p⁵+161p⁴−569p³−1550p²−976p+48)/(5760p²(3p+2)) + (p+1)(p+2)(3p⁴+33p³+124p²+182p+108)α²/(192p(3p+2)) +
  (p+2)³(p³−4p−4)α⁴/(128p(3p+2)). The hard-edge denominator 3p+2 appears again.
- **Second order in μ₁.** There is no N^{−1−2p} term (E3.7), and no N^{−3−2p} or N^{−5−2p} term. The ζ(−p)² layer starts at
  **N^{−2−2p} = (N^{−1−p})²**, with coefficient **(3p+1)/(2p)·ε₁²**, independent of α (18 grid points and 4 fresh points).
- **Out-of-sample checks** (100, all pass): (7/3, 0.6), (0.45, −0.3), (2.2, 2), (9/2, 1.3), for all j ≤ 5.
- **Lattice cross-check** (`m4_zeta_lattice.out`, 8 checks). After subtracting the exact integer layer and the bare ε_j terms,
  mid-window fits give an N^{−2−p} coefficient ≤ 4·10⁻⁷ and an N^{−3−p} coefficient equal to ε₁g₁ within 4·10⁻⁶ – 6·10⁻⁵ (fit
  spreads 8·10⁻⁴ – 10⁻²), at p ∈ {1.5, 2.5}. Rule X: the p = 1.5 values g₁ ≈ 0.330 (α = 0) and 2.443 (α = 1) were first seen in
  the fits; the gauge computation then gave 95/288 and 22/9.

**Conjecture S1-N′.** F_{p,α} depends on n only through N⁻² and the monomials X_j := ε_jN^{−1−jp}:
F = Σ_β c_β(N⁻²)Π_jX_j^{β_j}, each c_β an even power series. Established instances: β = 0 (Prop N.3, to N⁻⁸), β = e_j for j ≤ 5
(to N⁻⁴ relative), and β = 2e₁ (to N⁻⁴ relative), with c_{2e₁}(0) = (3p+1)/(2p).

**Remarks.**
- *The 1/(2j−1) factor.* Read as a function of a continuous Mellin variable w (w = j at the zeta poles), g has a simple pole at
  w = ½. That is the Mellin signature of a (1−u)^{+1/2} kernel: Γ(w−½)/Γ(w+½) = 1/(w−½), against the leading kernel's
  (1−u)^{−1/2} (Lemma K0). Partial fractions give B_j = (p+2)/(8p)·[p²j/2 + p(p+2)/4 + (p+2)(p+4)/(4(2j−1))]. So the N⁻²
  dressing looks like a **second-order edge kernel**: a polynomial in θ = u d/du acting on (1−u)^{−1/2}, plus a (1−u)^{1/2}
  term. This points to an order-N⁻² version of Theorem K. If it holds for continuous w, it predicts the N^{−3−pq} dressing of
  every pole term, which can be tested against the S1⁗ data. (At w = ½, cot(πw) vanishes, so the product W·cot·g stays finite.)
  HEURISTIC.
- *The X₁² coefficient.* (3p+1)/(2p) = 1 + (p+1)/(2p) is α-free, like the leading ε_j. A resummation in the spirit of Conjecture
  E3.C should produce it, but this is not attempted here.

## 4. Open

- Derive N from the Riemann–Hilbert data. Candidates: the hard-edge parametrix gives α/2; the outer scalar j_δ (Bernoulli
  polynomials B_{k+1}(−δ), SPEC §3.1) gives −Z(0).
- A closed form for F_{p,α} (p = 2, α = −½: (1 − 1/(4N²))^{−1/2}). f₂, f₄, f₆ are known (§5); the hard-edge denominators
  ∏((2k+1)p + 2) suggest a hypergeometric structure in the parameter a′ = 1/p + ½.
- Proofs of evenness: N → −N (all orders), and α → −α after the shift (heuristic in §5).
- ~~Write the order-k remainder estimates~~: done for p > 1 in JZC_M4_proof.md (Theorem N.6); p < 1 open.
- The second-order edge kernel (§6 remark): derive g(w) for continuous w; test it on pole terms (S1⁗ data) and on drums.
- Prove A_j, B_j for all j (the gauge computation is uniform in j; the j-dependence is reconstructed from j ≤ 5).
- How the Jacobian-tilt term of S1⁗ fits the natural form.
