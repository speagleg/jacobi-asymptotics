# Rule R review: Plan 65, reviewer A (analysis): E_pgt1.md, (E) for pure powers with p > 1

Reviewer: independent second reader (Rule R), reviewer **A**. My remit is the **analytic validity** of the proof. Reviewer
B checks the algebra and the extraction constants separately.
- Branch `plan-65-E-pgt1`, commit 78cfd1f. Diff against 928a2b3.
- Target: research/G1/RH/second_order/E_pgt1.md (§§0–10), the checks check_e_flat and check_e_rate, and the CITATIONS.md
  entries "(DLMF-9.7.2, Plan 65)" and "(Plan 65 reuse)".

**Internal inputs I re-read:**
- RH_px.md §§1–5 (REVIEWED). Most relevant: Lemma 3.2, Lemma 4.2(iii), Lemma 4.3, and §5 (identification, small norm,
  extraction).
- papers/paper2 sec_6.tex, Frame Proposition (F1–F8 and the F1/F5 proof).
- papers/paper2 app_outer.tex, Lemma binetcut (i)–(iv), including (O3)–(O5).

**External sources:**
- The CITATIONS.md entries (KMVV), (KMVV-orient, Paper 2), (DLMF-10.40, Paper 2), (DLMF-10.17, Plan 55), (DLMF-9, Paper 2),
  (DLMF-9.7.2, Plan 65) and (DLMF-5).
- I fetched dlmf.nist.gov/9.7, /10.40, /10.17 and /10.25 myself on 2026-10-15 by curl, and read the TeX alttext of the
  equations used (see §3).

I did not edit E_pgt1.md.

## Overall verdict: **ACCEPT WITH FIXES** (analysis)

I found **no critical or major gap** in the analytic argument. Six fixes are listed in §4, all minor. One of them (A1) is a
genuine small error in the stated domain of Lemma E.2(ii); the fix is one sentence.

The analytic core holds, for these reasons:
- **Lemma E.2.** The exact cancellation of the 1/n Binet terms is correct, and it is a clean mechanism: G has only the
  jump i𝔢, 𝔢 = 2 Im Log(1 − e^{−2iθ₊}), which is super-exponentially small near 0. The O(n^{−p}) comes only from |y| ≍ n^p.
- **Lemma E.3.** It uses the DLMF expansions inside their sectors, with uniform O(n⁻²) remainders on both circles.
- **Prop E.5′.** Every non-circle jump is exponentially small (or O(n^{−K})), not merely O(1/n). The Cauchy operators are
  bounded uniformly on the n-dependent contour (Paper 2 F1).
- **Extraction.** It is the standard second-order small-norm expansion, plus the invariance lemma.

The checks reproduce byte for byte. The numerics are consistent with O(n⁻²), with a visible subleading n^{−1−p} term.

| Statement | Verdict (analysis) | Fixes |
|---|---|---|
| Lemma E.2 (H_n flat to O(n^{−p})) | ACCEPT WITH FIXES | A1 (domain of (ii)) |
| Lemma E.3 (circle jumps to second order; n-dependence only via H_n) | ACCEPT WITH FIXES | A1 (inherits), A4 |
| Lemma E.4 (local data) | ACCEPT (analytic content: expansions and branches); constants left to B | — |
| Lemma E.5 (Laurent data; meromorphy) | ACCEPT (meromorphy argument sound; values left to B) | — |
| Prop E.5′ (second-order small norm) | ACCEPT WITH FIXES | A2, A3, A4 |
| Theorem E.1 | ACCEPT WITH FIXES (analysis); PROVED-mod-cite once A1–A4 are applied | A1–A4 |
| Corollary E.6 (chain) | ACCEPT WITH FIXES | A2 |
| §8 consequences, §9 GAP, §10 Rule A log | ACCEPT | A5 (INFO) |
| Rule C (citations used by the analysis) | ACCEPT WITH FIXES | A6 |
| Numerics (check_e_flat, check_e_rate) | ACCEPT (reproduced; NUMERICAL, not used in the proof) | — |

## 1. Re-runs (Rule N)

I used the jacobi-asymptotics `.venv` python with `PYTHONPATH=src` (worktree src).
- **check_e_flat.py**: 4 min. The output is **byte-identical** to checks/check_e_flat.out.
- **check_e_rate.py**: the output is **byte-identical** to checks/check_e_rate.out.
  - The script reads coefficients from the Plan 62 cache (tmp/plan62_cache). So I also **recomputed from scratch**
    (fresh cache, binary128 RKPW, K = 8·10⁴) the cases (p, s) = (1.25, 4) and (1.5, 2).
  - All 30 printed residuals (rb, ra, rg at n = 50, …, 799) agree with the committed file to all 8 printed digits.

**Rate assessment.** The residuals stay bounded for n ≤ 799 (max |·| = 5.73). Their increments per doubling of n shrink
geometrically:
- rb at p = 1.25: 0.0062, 0.0043, 0.0033, 0.0026. The ratios 0.70 → 0.79 approach 2^{−1/4} = 0.84, which is the
  signature of an n^{1−p} term in n²·error, i.e. an n^{−1−p} term in the coefficient.
- rb at p = 1.5: the ratios are ≈ 0.6, roughly 2^{−1/2}.
- ra at p = 1.25: the ratios are ≈ 0.53.

This is exactly what Prop E.5′ predicts: a remainder O(n⁻² + n^{−1−p}), with n^{−1−p} = o(n⁻²) for p > 1. The pattern also
argues against an O(n⁻²log n) remainder, which would give constant increments per doubling. **Consistent with O(n⁻²).**
Numerics only; this is not used in the proof.

check_e_flat confirms the mechanism of Lemma E.2:
- n^p·max|G − G(1)| is n-stable at p = 3/2 and p = 3 (0.0577, 0.02297).
- It is ≤ 10⁻²⁴ at p = 2, the exact case.
- The Binet piece alone varies at order 1/n.

Sampling caveat (INFO): the sample points do not include boundary values on the cut (−R₁, 0) or points near 4c − ε off
the axis. The proof covers both, so this is not a defect.

## 2. Analytic verification, item by item

### 2.1 Lemma E.2

- **Jump.** I re-derived G₊ − G₋ = −2i Im j(t₊) − i𝔟 = 2i Im Log(1 − e^{−2iθ₊}) =: i𝔢.
  - The inputs are B₊ = B₋e^{−i𝔟} (binetcut (iii)), 𝔟 = 2 Im(−j(t₊) − Log(1 − e^{−2iθ₊})) (binetcut (ii)), and
    j(t₋) = conj j(t₊).
  - The Binet parts cancel identically.
  - With t₊ = n|y|^{−1/p}e^{−iπ/p}, |q| = exp(−2πn|y|^{−1/p}sin(π/p)) < 1. From |arg(1 − q)| ≤ arcsin|q| we get
    |𝔢| ≤ π|q|. Correct.
- **p = 2 exactness.** cos(π/2) = 0, so q = e^{−2πn|y|^{−1/2}} ∈ (0, 1) and 𝔢 ≡ 0. Hence G ≡ G(1), and at p = 2 H_n is
  exactly constant and Δ₁ = Δ₁^{mod} exactly. This is correct, and confirmed numerically (≤ 10⁻²⁷ at dps 30).
- **Representation (E.2.1).** Correct.
  - K is analytic across (−∞, 0): the Plemelj jumps agree, the boundary values are continuous, and Morera's theorem
    applies.
  - 0 is removable: j(t) → 0 as |t| → ∞ in |arg t| ≤ π/p < π; log B is bounded with its boundary values (binetcut (O5));
    and the integral is bounded because 𝔢 vanishes to infinite order at 0.
  - At ∞, K = O(log|z|): j(t) = O(log|t|) for |t| ≤ 1 in the sector (|1 + t| ≥ sin(π − π/p) > 0), and
    log B = O(log|z|) (binetcut (iii)). So K is constant.
- **Bounds.**
  - The far part, after the substitution |y| = n^p w, gives exactly n^{−p}∫min(1, e^{−c₁w^{−1/p}})w^{−2}dw < ∞. It is
    the only source, and this matches the claim that only |y| ≍ n^p contributes.
  - The near part [−2R₁, 0) has a density 𝔢 that is O(e^{−c₂n}) in C¹. Its Cauchy integral and boundary values are
    O(e^{−c₂n}) for |z| ≤ R₁. Here dist(z, −2R₁) ≥ R₁, so the endpoint log singularity is harmless.
  - Uniformity on the circles and the lens: both lie in {|z| ≤ R₁}, and (i) includes the boundary values on (−R₁, 0).
    Correct.
- **Remark (1)** is in fact provable from the lemma: log B(1) = 0 and −j(n) = −1/(12n) + O(n⁻³) give
  log B(z) = (z^{1/p} − 1)/(12n) + O(n^{−p}).
- **One defect: A1, domain of (ii).** c(p) ∈ (½, 1) for all p > 1. I computed c(1.01) = 0.5015, c(1.5) = 0.566,
  c(2) = 0.617, c(3) = 0.689, c(100) = 0.984. Hence R₁/2 = 2c + 1 < 4c for every p > 1. The derivative bound (ii),
  stated on |z| ≤ R₁/2, therefore does **not** reach the right end of the band or 4c − ε. Lemma E.3 uses it exactly
  there (see §4).

### 2.2 Lemma E.3

**Bessel, main sector.** I re-derived (E.3.1) entry by entry from DLMF 10.40.1–4, with a₁ = (4α² − 1)/8 (10.17.1) and
b₁ = (4α² + 3)/8 (10.17.8 at k = 1). The four relative corrections of (Ψ₁₁, Ψ₁₂, Ψ₂₁, Ψ₂₂) are
−a₁/w, +a₁/w, −b₁/w, +b₁/w with w = 2ζ^{1/2}. The matrix (1/(16ζ^{1/2}))[[−(1+4α²), −2i], [−2i, 1+4α²]] reproduces all
four. So the 1/16 normalisation is right.
- Sector conditions: |arg ζ| < 2π/3 gives |ph w| < π/3 ≤ π/2 − δ, inside 10.40.1/10.40.3.
- In the Hankel sectors, ph 2(−ζ)^{1/2} ∈ (−π/6, π/6), inside 10.17.5/6 and 10.17.11/12.
- Uniformity up to the sector boundaries holds because the closed sectors overlap.
- check_e_num [2] shows the error halving when |ζ| quadruples, i.e. the next term is O(ζ^{−1/2}) relative to the
  correction, in all six tested directions and for both α.

**Insertion into P₀.**
- σ₃Ψσ₃ conjugates the correction to Q₀/16.
- Ẽ_N σ₃(2πζ^{1/2})^{−σ₃/2}Mσ₃ = N W̃^{σ₃}MM^{−1}, using σ₃Mσ₃ = M^{−1}.
- The exponentials e^{2Nf^{1/2}σ₃}e^{Nφσ₃}(−1)^N = I commute through the diagonal W̃^{−σ₃}.

Hence P₀ = N W̃^{σ₃}(I + Q₀/(16Nf^{1/2}) + O(N⁻²))W̃^{−σ₃}. The O(N⁻²) is O(1/(N²|f|)), uniform on ∂U_0 (|f| ≍ δ). The
conjugating factors P₀^∞ρ^{σ₃} are bounded on ∂U_0 with bounded inverses (Paper 2 szego (vi)). Correct.

**Airy.**
- u₁ = 5/72 and v₁ = −7/72 (9.7.2, which I verified on the page) give X = [[−1/72, −i/12], [−i/12, 1/72]].
- The arguments ζ, e^{∓2πi/3}ζ of the sector-I columns lie in closed subsectors of |ph| < π, where 9.7.5–6 hold
  uniformly.
- On ∂U_r, |ξ| = n·(2/3)|f_r|^{3/2} ≍ n, so the remainder is O(n⁻²) uniformly.
- check_e_num [1] confirms this in all four sectors (error ∝ |ζ|^{−3/2} relative).

**n-dependence.**
- f, φ̃ = φ ± iπz^{−1/p}, the contour inside the discs and P₀^∞ are n-independent.
- The only n-dependence is ω (and hence ρ² = e^{∓iπα}/ω and (−ω)^{±1/2}) through H_n.
- With D_W = D_{W^{mod}}·D_{H°} (the Szegő function is multiplicative), ω/ω^{mod} = D²_{H°}/H°. The representation
  log D²_{H°}(z) − log H°(z) = (𝓡(z)/π)∫(log H°(x) − log H°(z))dx/(√(x(4c − x))(z − x)) needs no analyticity of H° at z.
  It holds for boundary values on the cut too, since it rests only on the identity (1/π)∫dx/(√(x(4c−x))(z−x)) = 1/𝓡(z).
- The sup bound from E.2(i) and the window argument then give O(n^{−p}) on both circles, provided the derivative bound
  holds near the two points where the circles meet [0, 4c], namely δ and 4c − ε. For 4c − ε this needs A1.

### 2.3 Prop E.5′: second-order small norm (the item asked about hardest)

I checked every non-circle jump of R separately. All are O(e^{−n/C}), O(n^{−pn/4}) or O(n^{−K}). None is merely O(1/n)
or o(1):
- **Inside U_r.** There is no jump: P̂_r has exactly the jumps of Q (Paper 2 F5 / Lemma airy(ii)), and H_n has no jump
  near 4c.
- **Band outside the discs.** There is no jump: P₀^∞ = T a^{σ₃}T^{−1} has jump J, and Q has J because D_W is the Szegő
  function of the true W₀.
- **Inside U_0** (the accumulation point 0, where the discrete-to-continuous interpolation lives):
  - There is no band mismatch: W̃₊W̃₋ = w₀ exactly.
  - The (h1) entries on the lips are exp(−cN|z|^{−1/p}) (Paper 2 F4). The amplification by P₀ is
    poly(N, |z|^{−1})e^{CN|z|^{1/2}}. The product is ≤ exp(−N(cδ^{−1/p} − Cδ^{1/2}))·poly, which is O(e^{−n/C})
    uniformly once δ is small (δ is free, F1).
  - The (h2) jump of W̃ on (−δ, 0) is likewise exp(−cN|z|^{−1/p}).
  - So RH_px Lemma 4.3's O(N^{−K}min(1, |z|^K)) is in fact exponentially small.
  - **No Conway–Deift-type comparison without a rate is used anywhere for p > 1.** The classical Bessel parametrix is
    available because H_n is only Hölder-1/p at 0 with a super-small jump (RH_px Lemma 3.4, Lemma 4.2(iii)). Its
    matching error on ∂U_0 is a genuine asymptotic expansion.
- **Lips outside U_0, Σ_v, the saturated segment, Σ^△, and the top.**
  - Paper 2 F5 gives |v − I| ≤ Ce^{−n/C} arc by arc, and ≤ Cn^{−pn/4} on the top segment. These bounds include the
    poly(n)·e^{C log²n} growth of ω and κ_±.
  - I checked that the F5 proof covers the region near the top, where |Im θ| on Σ^△ becomes small. The factor
    |κ_±| ≤ Cn^p is absorbed by e^{2n Re φ̃} ≤ x^{−n}.
- **Contour geometry.** The part of the contour inside U(0, 2δ) ∪ U(4c, 2ε) is n-independent. The rest is a translate of
  a fixed Carleson curve plus a Hilbert–Schmidt block, so ‖𝒞₋‖_{L²(Σ)} ≤ C uniformly although the length is O(n^p)
  (F1 proof).
  - Hence ‖J − I‖_{L²∩L^∞} = O(1/n): the circles give O(1/n), and the rest gives O(n^{p/2}e^{−n/C}).
  - The far pieces in the moment integrals carry |s|^{k−1} ≤ Cn^p, which is absorbed by the exponential bounds.
- **Second-order step.** The step "R − I = 𝒞(J − I) + 𝒞((R₋ − I)(J − I)), second term ≤ ‖R₋ − I‖₂‖J − I‖₂/d" is
  correct. The Δ₁ − Δ₁^{mod} = O(n^{−p}) term contributes O(n^{−1−p}) ≤ O(n⁻²) for p > 1.
- **Residues.** I checked the orientation and residue bookkeeping independently:
  - Clockwise circles give R₊ = R_out.
  - R⁽¹⁾_out − R⁽¹⁾_in = Δ₁, so R⁽¹⁾_out is the sum of the principal parts.
  - R_1 = −(1/2πi)∫R₋(J − I), R_2 = −(1/2πi)∫R₋(J − I)s.
  - So R_1⁽¹⁾ = A₀ + A_r and R_2⁽¹⁾ = 4cA_r + B_r: the 0-disc has no residue of Δ₁⁰·s, and the 4c-disc gives B_r + 4cA_r.
  - Inside U_0, R⁽¹⁾_in(0) = (principal parts)(0) − C₀ = −C₀ − A_r/(4c) + B_r/(16c²). This matches.
- **Meromorphy of Δ₁^{mod}** (needed for the residue evaluation). Only a^{±2} = ((z − 4c)/z)^{±1/2} enter
  P₀^∞Z(P₀^∞)^{−1} (through T^{−1}·T conjugation). In the variable v = (−z)^{1/2} (resp. u = (z − 4c)^{1/2}) every factor
  is meromorphic, so the vanishing of odd powers (asserted in check_e_sym) makes Δ₁^{mod} meromorphic in z. The formal
  coefficient Δ₁ has no lip jumps because (E.3.1) and the Airy expansion take the same form in every sector. Sound.

### 2.4 Extraction (Theorem E.1)

- Q₁ = P₁ + R_1 and Q₂ = P₂ + R_1P₁ + R_2. I re-expanded a = (1 − 4c/z)^{1/4} myself: P₁ = [[0, ic], [−ic, 0]],
  P₂ = [[c²/2, 2ic²], [−2ic², c²/2]].
- P₀^∞ is weight- and n-independent, so it contributes exactly c² to (Q₁)₁₂(Q₁)₂₁ and exactly 2c to a(Q), with no 1/n
  part. The weight enters only through D_W, which the invariance lemma (F8) removes.
- Independent sympy check (mine, not check_e_sym), from the stated A₀, A_r, B_r:
  - the e¹ coefficient of (Q₁)₁₂(Q₁)₂₁/c² is −p(α+1) = −(s−1);
  - that of a(Q) is −cp(α+2) = −c(s − 1 + p);
  - the α² terms cancel.
- The n ↔ N bookkeeping is consistent: the degree-n problem, U(z) = n^{pnσ₃}Y(z/n^p), b_n² = h_n/h_{n−1}, and α_n the
  diagonal coefficient of π_n (F8, RH_px §5).
- The repo-pairing conversion (n/(n−1))^p = 1 + p/n + O(n⁻²) is correct.

### 2.5 Corollary E.6

- (E.6.1) is correct. Y₂₁ = κ_nπ_{n−1} with κ_n = (Y₁)₂₁. Left constant diagonals and right scalar-diagonal factors
  cancel in (Q₁)₂₁·Q₁₁/Q₂₁. Near the negative axis only upper-triangular (R-step) and identity factors act, and they
  leave column 1 unchanged.
- U₁₁ and U₂₁ are polynomials, so the limit z → 0⁻ exists trivially on the U side.
- Ψ₂₁/Ψ₁₁ = πi·xI′_α(x)/I_α(x) → πiα follows from DLMF 10.25.2. For α > −1, Γ(α + 1) > 0, so I_α(x) > 0 for small
  x > 0. The ratio is exact in the limit at fixed n, so w = w⁽⁰⁾ + w⁽¹⁾/n holds with no remainder.
- Finiteness of w⁽⁰⁾, w⁽¹⁾. T^{−1}M = diag(1, i), so the a^{±1} ~ |z|^{∓1/4} factors pair with f^{±1/4}. The ρ-mixing
  term a·sh·f^{−1/4} has sh = O(|z|^{1/2}), so it is finite and nonzero. This is why w⁽¹⁾ depends on the v-linear part of
  log ρ.
- The "Remainder" paragraph correctly controls that v-linear coefficient (λ_n = O(n^{−p})), and also ρ(0) = 1 for the
  true weight.
- See A2 for R(0).
- The unfolding to G_m, H_m, k₀, k₁ re-derives correctly: k₀ + k₁ = −2(s − 1 + a), k₀ − k₁ = 2a − p, and
  s − 1 = p(a + ½).

## 3. Rule C spot-check

I fetched the DLMF pages myself (2026-10-15) and read the alttext of the equations used. Each matches CITATIONS.md:

| Eq. | Content | Sector |
|---|---|---|
| 9.7.2 | u₀ = v₀ = 1; u_k recursion; v_k = ((6k+1)/(1−6k))u_k | — |
| 9.7.5 | Ai ~ e^{−ζ}/(2√π z^{1/4})Σ(−1)^k u_k/ζ^k | |ph z| ≤ π − δ |
| 9.7.6 | Ai′ ~ −z^{1/4}e^{−ζ}/(2√π)Σ(−1)^k v_k/ζ^k | |ph z| ≤ π − δ |
| 10.40.1 | I_ν | ½π − δ |
| 10.40.2 | K_ν | 3π/2 − δ |
| 10.40.3 | I′_ν | ½π − δ |
| 10.40.4 | K′_ν | 3π/2 − δ |
| 10.17.1 | a_k(ν) | — |
| 10.17.8 | b_k(ν), with the (4ν² + 4k² − 1) factor, so b₁ = (4ν² + 3)/8 | — |
| 10.17.11 | (H^{(1)}_ν)′ | −π + δ ≤ ph ≤ 2π − δ |
| 10.17.12 | (H^{(2)}_ν)′ | −2π + δ ≤ ph ≤ π − δ |
| 10.25.2 | I_ν(z) = (½z)^ν Σ(¼z²)^k/(k!Γ(ν+k+1)) | — |

KMVV (6.23)–(6.28) and (6.42)–(6.53) are as quoted. E_pgt1 uses KMVV (6.28) only for the leading term. It derives the
next term itself from DLMF, through KMVV's own derivation route ("Inserting the asymptotics … 9.7.1–9.7.4 of [2]"). That
is legitimate. For the scope point, see A6.

## 4. Findings and required fixes

**A1 (minor; a genuine error in the stated domain).** Lemma E.2(ii) is stated for |z| ≤ R₁/2 = 2c + 1. Since c(p) > ½
for all p > 1, 2c + 1 < 4c. Lemma E.3 ("n-dependence") needs |(log H°)′| ≤ Cn^{−p} near 4c − ε, where ∂U_r meets the
band, and on the part of (0, 4c] that the window argument visits. Those points are outside the stated domain.
- *Fix:* state (ii) on {|z| ≤ R₁ − 1, z ∉ (−∞, 0]} (plus the boundary values on (−R₁/2, 0)). Or add the sentence: "for
  dist(z, (−∞, 0]) ≥ η and |z| ≤ R₁ − η, |G′(z)| ≤ Cn^{−p}/η by Cauchy's estimate applied to (i)." That covers
  [δ/2, 4c + ε] and both circle crossings.
- Nothing else changes, since the near-cut part of (ii) is only needed for |z| ≤ R₁/2.

**A2 (minor; rigour of R(0)).** Prop E.5′ ("value at 0") and Cor E.6 evaluate R at 0. That point lies on Σ_R: the lips
and (−δ, 0) meet there. The text bounds only the circle contribution ("∂U_0 is at distance δ from 0") and asserts that
the local pieces contribute O(n^{−K}).
- *Fix:* add the two-line argument. For z → 0 in a sector avoiding the contour pieces (non-tangentially), or by taking
  both boundary values along (−δ, 0), |s − z| ≥ c·max(|s|, |z|) on the pieces near 0. Then
  |𝒞((R₋ − I)(J − I))(z)| ≤ ‖R₋ − I‖₂·‖(J − I)/(s − z)‖₂ with |J − I| ≤ Ce^{−n|s|^{−1/p}/C}, and the same for 𝒞(J − I).
  Dominated convergence gives the limit R(0) := I + (1/2πi)∫R₋(J − I)ds/s, with the stated O(n⁻²) expansion.
- Also state that this limit is the one used in (E.6.1). Q is continuous across (−δ, 0), and R₊, R₋ have the same limit
  at 0.

**A3 (minor; hypotheses of a cited internal result).**
- *The problem:* Paper 2's Frame Proposition, cited in Prop E.5′ for F1 and F5, is stated for 1 < s < 1 + 2p (α < 1).
  Theorem E.1 claims all s > 1. The §10 bullet "Large α" asserts that the lemmas used do not use α < 1, but F1 (uniform
  Cauchy bound) and F5 (arc-by-arc bounds) are not in its list.
- *Fix:* add to §10 (and to the proof of E.5′) that the F1 contour/Cauchy-operator part depends only on the
  n-independent geometry, and that F5 uses only Lemma szego (vi)(b), (vi)(c), Lemma signs and Lemma gfunction. None of
  these uses α < 1.
- Alternatively, take the small-norm step and the identification from RH_px §5 (valid for all s > 1), and cite F1 only
  for the weight-independent Cauchy bound.

**A4 (minor; mixing two frames' contours).**
- *The problem:* the hard-edge parametrix and the mismatch bound are taken from RH_px (§4.1 and Lemma 4.3, with KMVV's
  standard lips at ±π/3 / Bessel rays at ±2π/3), but the outer contour, Cauchy bound and F5 come from Paper 2 (lips at
  angle θ_lip, Bessel rays at ±(π − θ_lip), F3). E_pgt1 does not say which choice is in force inside U_0.
- *Fix:* one sentence. Either take RH_px's lips inside U_0 (F1 allows any fixed n-independent choice there), or note that
  RH_px Lemma 4.3 holds verbatim for Paper 2's lips (F4 gives the same exp(−n|z|^{−1/p}/C) bound) and that (E.3.1) holds
  uniformly for the rotated rays (CITATIONS "(DLMF-10.17, Plan 55)").
- Either way, Δ₁⁰ is unchanged, because (E.3.1) has the same form in all sectors.

**A5 (INFO).**
- §9's d₂ bullet says the O(n^{−p}) part of H_n enters at order n^{−1−p}, "below an n⁻² term" for 1 < p < 2. That is
  right (n^{−1−p} = o(n⁻²) for p > 1), and check_e_rate shows it: the rb increments decay like 2^{−(p−1)} per doubling
  (§1).
- Suggestion: say in §8.1 that the "slow drift" is the n^{1−p} term in n²·error and that it is bounded. This is clearer
  than "as an n^{1−p} term would".

**A6 (minor; Rule C bookkeeping).** The "(DLMF-10.40, Paper 2)" entry records the application hypothesis "|α| < 1". E_pgt1
uses 10.40.1–4 and 10.17.x for any fixed α > −1, which DLMF permits (ν fixed, complex).
- *Fix:* in the "(Plan 65 reuse)" entry, add "ν = α > −1 fixed (α ≥ 1 allowed); sectors as checked in E_pgt1 Lemma E.3
  (|ph w| < π/3 for 10.40.1–4; ph 2(−ζ)^{1/2} ∈ (−π/6, π/6) for 10.17.5–6, 10.17.11–12)".
- Also list 10.25.2's use (Cor E.6, I_α(x) > 0 for small x > 0 when α > −1).

## 5. Things I tried to break (Rule A, reviewer side)

- **Is the cancellation only formal?** No. G has the exact jump i𝔢 and an exact Cauchy representation (E.2.1), so the
  cancellation holds at the level of functions, not just asymptotic series.
- **Could the far part be O(1/n) after all?** No. The substitution |y| = n^p w is exact, and the w-integral converges at
  both ends (super-exponential decay at w → 0, w⁻² at ∞) for p > 1. At p = 1, sin(π/p) = 0, and the bound and the lemma
  fail. That matches §9.
- **Could a non-circle jump be O(1/n)?** I went arc by arc (§2.3). The only candidates with polynomial growth (κ_± near the
  top, ω on the saturated segment) are multiplied by e^{−n/C} or x^{−n}.
- **Could the discrete-to-continuous step near 0 cost a power of n?** The interpolation removes the poles exactly. What
  remains near 0 is exponentially small in N|z|^{−1/p}, which beats the e^{CN|z|^{1/2}} Bessel amplification on U(0, δ)
  for small δ.
- **Could n-dependence leak through the D_W conjugation in the extraction?** No: invariance lemma (F8). Or through the
  global parametrix? No: P₀^∞ is weight-free in the Q-frame.
- **α ≥ 1 and α ∈ (−1, 0).** The Bessel expansion holds for any fixed order. The identification is RH_px's (all s > 1).
  Remaining issue: A3.

**Bottom line (analysis):** Theorem E.1 and Corollary E.6 are correctly proved modulo the cited inputs once A1–A4 are
applied. All four are wording-level additions; none changes the mathematics. Reviewer B's verdict on the constants
(A₀, A_r, B_r, C₀, w⁽¹⁾, Lemma E.4) is needed for REVIEWED.
