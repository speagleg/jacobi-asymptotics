# JZC M4: the second-order layer — the natural index N = n + α/2 − Z(0) (Plan JZC, milestone M4; first results)

Status (2026-10-21): NOT REVIEWED. **Proof of Props N.3–N.4 (all p ≠ 1): JZC_M4_proof.md (Theorem N.6; Rule R review A applied).** §5 added 2026-10-21 (integer layer to order 8); §6 added 2026-10-21 (zeta layer in natural form); §7 added 2026-10-21 (reflection and shift). Labels per VERIFICATION_POLICY.md.

| # | Statement | Label |
|---|---|---|
| Identity N.1 | E2's d₂(p, s) = p(p+1)δ_N²/2 + f₂(p, α), δ_N := α/2 + ½, f₂ := −(p+2)α²/8 + (p+1)/12, α := (s−1)/p − 1 | PROVED (algebra) |
| Prop N.2 | Bessel-zero (Lommel) measures, p = s = 2 (α = −½): n²b_n/c = (n/N)²·(1 − 1/(4N²))^{−1/2} exactly, N = n + μ/2 = n + α/2 − Z(0) | PROVED (from the Lommel closed form, SPEC §3.10) |
| Conj S1-N | n^pb_n/c = (n/N)^p·F_{p,α}(N; Z), N := n + α/2 − Z(0). F has no 1/N term; its integer layer is even in 1/N; its N⁻² coefficient is f₂; the spectral terms (zeta layer, poles) appear as functions of N | CONJECTURE (NUMERICAL: m4_natural_index.out, 7 lattices; S1′, rule H, S1⁗ as instances). The integer-layer part is now established through order 8 for the Riemann–Hilbert model: Prop N.3 |
| Prop N.4 | Zeta layer with the band factor (E3 gauge added to the order-k computation): each ε_j term is ε_jN^{−1−jp}·(1 + g_jN⁻² + O(N⁻⁴)), even in 1/N, with g_j = A_j + B_jα² in closed form for all j (§6); the ζ(−p)² layer starts at (ε₁N^{−1−p})²·(3p+1)/(2p) | **PROVED-mod-cite for p ≠ 1, every j (Theorem N.6(ii); symbolic-j exact algebra m4_zeta_exact2_A), and the ζ(−p)² layer (3p+1)/(2p), h₂ (m4_zeta_exact2_B).** As coefficients of b_n: see the visibility table of Theorem N.6(iii) |
| Conj S1-N′ | refined S1-N: F_{p,α} is a function of N⁻² and the monomials X_j := ε_jN^{−1−jp} only, i.e. F = Σ_β c_β(N⁻²)ΠX_j^{β_j} with each c_β an even series | CONJECTURE in general; PROVED-mod-cite for β ∈ {0, e_j (all j), 2e₁} to the orders of Theorem N.6(ii) |
| Prop N.3 | Integer layer from the order-k Riemann–Hilbert model computation (E2's frame, extended from k = 2 to k = 8): f₁ = f₃ = f₅ = f₇ = 0; f₄, f₆ in closed form (§5); f_{2k} is even in α | **PROVED-mod-cite for p ≠ 1 (JZC_M4_proof.md Theorem N.6(ii): μ = 0 layer to N⁻⁶, exact).** As coefficients of b_n (Thm N.6(iii)): f₂ (all p), f₄ (p > 2/3), f₆ (p > 4/3). f₈ and beyond: NUMERICAL (m4_rh4.out, m4_f8_denominator.out) |

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

## 7. Reflection and shift: where the natural index and the evenness come from (Theorem R, Conjecture Σ)

**The decoupled model.** In the jump data of the order-k computation (JZC_M4_proof.md Lemma N.6a), the exponent α plays two
separate roles:
- the **Bessel order ν**, in the coefficients a_k(ν), b_k(ν) (DLMF 10.17.1, 10.17.8). These are polynomials in ν².
- the **Szegő exponent β**, in ρ² = φ^{2(β+1)} at the hard edge and the factor φ^{−2(β+1)} at the soft edge. Here
  φ(z) = (z^{1/2} + (z−4c)^{1/2})/(2c^{1/2}) is the exterior conformal map of [0, 4c].

For the lattice, ν = β = α. Decoupling them gives a two-parameter family of formal problems M(β, ν), with formal series
b(n; β, ν) (`m4_rh4.run(..., nu=)`, `checks/m4_shift_exact.py`).

**Theorem R (reflection; PROVED for the formal model).** b(n; β, ν) = b(−n; −β−2, ν) as formal series in 1/n. That is,
d_k(−β−2, ν) = (−1)^kd_k(β, ν).

*Proof.* With T = [[1, 1], [i, −i]]/√2 we have σ₂T = Tσ₃, so T⁻¹σ₂T = σ₃.
- Hence P₀^∞ = T𝔞_∞^{σ₃}T⁻¹ commutes with σ₂, and so does P₁ = −cσ₂.
- From X_k = M⁻¹(M∘C_k′) and Ξ_k = M⁻¹(M∘C_k): σ₂X_kσ₂ = (−1)^kX_k and σ₂(σ₃Ξ_kσ₃)σ₂ = (−1)^kσ₃Ξ_kσ₃ (even k: spanned by
  I, σ₂; odd k: by σ₃, iσ₁; JZC_M4_proof §3).
- σ₂d^{σ₃}σ₂ = d^{−σ₃} for scalar d. So σ₂Δ_k(β)σ₂ is Δ_k with ρ² ↦ ρ⁻² and (−ω) ↦ (−ω)⁻¹, i.e. β + 1 ↦ −(β + 1), times
  (−1)^k.
- The prefactors (−1/φ̃)^k and (2f^{1/2})^{−k} are β-free. So σ₂Δ_k(β)n^{−k}σ₂ = Δ_k(−β−2)(−n)^{−k}.
- The residue recursion is covariant under conjugation by a constant matrix, so R(n; β) = σ₂R(−n; −β−2)σ₂.
- The extraction (Q₁)₁₂(Q₁)₂₁ is invariant under σ₂-conjugation ([[a, b], [c, d]] ↦ [[d, −c], [−b, a]]), and Q₁ = P₁ + R₁ with
  P₁ = −cσ₂. ∎

Exact check: `m4_shift_exact.out` (identically in (p, α, β), orders ≤ 6). Numerical check: `m4_shift_num.out` (order 8).

**Proposition S (shift; exact computer algebra to order 6, NUMERICAL to order 8).** With N := n + (β+1)/2, the natural-form
coefficients f_k of F := (N/n)^p·b(n; β, ν)n^p/c are independent of β. The odd ones vanish. Checked:
- identically in (p, ν, β) for k ≤ 4 (and k ≤ 6 when m4_shift_exact.out reports it);
- at 40 digits for k ≤ 8 at 36 points (p, ν, β), m4_shift_num.out.

**The zeta layer too** (NUMERICAL, m4_shift_zeta.out, 40 checks). With the E3 gauge to first order in μ_j (j = 1, 2), the
natural-form response is β-independent and has no odd relative terms, at p ∈ {1.7, 0.6} and ν ∈ {0.3, 0.8}. So the shift
structure covers all of S1-N′: F = Φ_p(N²; ν², X_j), with β entering only through N.

**Conjecture Σ (shift lemma, all orders).** b(n; β, ν)n^p/c = (n/N)^p·F_p(N; ν²), with N = n + (β+1)/2 and F_p independent
of β.

**Corollary (given Σ; the proof is two lines).**
- *Evenness in N, all orders.* By Theorem R, (n/N′)^pF(N′) at β′ = −β−2 equals (n/N′)^pF(−N′), where N′ = n − (β+1)/2.
  So F(N′) = F(−N′) as formal series.
- *Evenness in α.* F depends on ν only through ν², since a_k and b_k do.
- *The natural index is the Szegő shift.* N = n + α/2 + ½ = n + (β+1)/2. In particular the lattice's −Z(0) = ½ is part of the
  Szegő exponent β + 1 = (s−1)/p, not a separate effect. (For general spectra −Z(0) enters through the outer scalar; that
  part of M4 remains.)
- So the integer layer is a function of (p, ν², N²) only: f_{2k} is a polynomial of degree k in ν², consistent with f₂, f₄,
  f₆.

Theorem R and Conjecture Σ together reduce **all-order** evenness to one statement about the β-dependence.

**Lemma BR (self-similar Buyarov–Rakhmanov identity; PROVED).** Let Φ(z) be the phase of the lattice equilibrium in the
Q-frame, with the hard-edge branch 2f^{1/2} and the soft-edge branch φ̃ (E2 Lemma E2.4, c = 1). Then (1 + p·z∂_z)Φ = −2 log φ,
up to the additive constants of the branches. Explicitly:
- (1 + p z∂_z)(2f^{1/2}) = 2 asinh(v/2) at z = −v²;
- (1 + p z∂_z)φ̃ = −2 log φ near 4c.
In particular the right-hand side does not depend on p.

*Proof.*
- *Hard edge.* f = −(π²/4)z𝔞², so 2f^{1/2} = π√(−z)𝔞(z). With 𝔞 = ((4c)^{−1/2}/(pπ))Σ_k((½)_k/k!)(z/4c)^k/((a′+k)(k+½)) and
  a′ = 1/p + ½, we have (1 + p z∂_z)[√(−z)z^k] = (1 + p(k+½))√(−z)z^k = p(a′+k)√(−z)z^k. This cancels the factor 1/(a′+k)
  term by term and leaves (4c)^{−1/2}√(−z)Σ_k((½)_k/k!)(z/4c)^k/(k+½), which is 2 asinh(√(−z)/(2√c)), the arcsine series.
- *Soft edge.* Both branches are local branches of Paper 2's phase function (f^{1/2} = −(φ_ph ± iπ)/2, φ̃ = −(2/3)f_r^{3/2}),
  so the identity continues analytically, and log φ continues with it.
- Exact rational check of both edges at p ∈ {3/2, 7/3, 5} through order 15: `checks/m4_br_identity.out`. ∎

*Reading.* Under the self-similar scaling of the lattice problem (nodes ∝ n^p), (1 + p z∂_z) is the n-derivative of n·Φ(xn^p).
So Lemma BR says that ∂_n(nΦ) = −2 log φ, the complex potential of the arcsine measure of the band. This is the
Buyarov–Rakhmanov identity d/dt(tμ_t) = ω_{supp}, proved here directly for the lattice equilibrium; no citation is needed. The
n-flow of the phase is therefore generated by the same function, log φ, as the β-flow (ρ² = φ^{2(β+1)}).

**Mechanism for Σ (HEURISTIC; a proof route).** Σ is equivalent to the flow identity
∂_β log b = ½(∂_n log b − p/n) on formal series. The β-flow is generated by the gauge log φ·σ₃: ∂_βρ² = 2 log φ·ρ². The n-flow
of an equilibrium problem with a fixed constraint is generated by the equilibrium measure of the support. This is the
Buyarov–Rakhmanov identity d/dt(tμ_t) = ω_{supp μ_t}, the arcsine measure of the band, whose complex potential is log φ. The
self-similar scaling of the lattice problem (nodes ∝ n^p) adds the p/n term. A proof would have to:
- (a) set up the n-flow of the full (not circle-only) Riemann–Hilbert problem;
- (b) identify its generator with log φ. This is now Lemma BR, proved.
- (c) show that the formal model inherits the identity.

Caveat for (c): at finite δ, Lemma BR integrates to ∫_n^{n+δ}log φ(xt^p)dt, which is not a single φ-power. So the exactness
of Σ (it holds to all computed orders, with no δ² defect) must also use the structure of the Bessel and Airy corrections, not
the phase alone. The analogue for varying weights is Bleher–Its 2005, Thm 5.2: evenness via the string equations
(NOVELTY_JZC, item N). Finding the model's string equation is the natural route to (c).

## 4. Open

- Derive N from the Riemann–Hilbert data. Candidates: the hard-edge parametrix gives α/2; the outer scalar j_δ (Bernoulli
  polynomials B_{k+1}(−δ), SPEC §3.1) gives −Z(0).
- A closed form for F_{p,α} (p = 2, α = −½: (1 − 1/(4N²))^{−1/2}). f₂, f₄, f₆ are known (§5); the hard-edge denominators
  ∏((2k+1)p + 2) suggest a hypergeometric structure in the parameter a′ = 1/p + ½.
- Proofs of evenness: reduced by §7 (Theorem R, PROVED) to the shift lemma, Conjecture Σ; proof route via Buyarov–Rakhmanov.
- ~~Write the order-k remainder estimates~~: done for every p ≠ 1 in JZC_M4_proof.md (Theorem N.6).
- The second-order edge kernel (§6 remark): derive g(w) for continuous w; test it on pole terms (S1⁗ data) and on drums.
- ~~Prove A_j, B_j for all j~~: done (symbolic-j exact algebra, Theorem N.6(ii)); also the ζ(−p)² layer to N⁻⁴ relative.
- The remaining second-order layers (μ₁μ₂, …) and third order: they control what b_n determines below n^{−2−3p}.
- How the Jacobian-tilt term of S1⁗ fits the natural form.
