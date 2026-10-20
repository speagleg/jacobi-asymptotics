# Rule R review: Plan E3, reviewer A (analysis): E3.md, the n^{−1−kp} series, κ_p for p > 1, d₂ for 0 < p < 1

Reviewer: independent second reader (Rule R), reviewer **A**. My remit is the **analytic validity** of the file:
- Lemma F.1′ (the Mellin computation and the remainder);
- Lemma E3.4 (the tilted Szegő data and the gauge G_μ);
- Lemma E3.5 and Prop E3.6 (the second-order small norm with the band factor, transferred to 0 < p < 1);
- the proofs of Theorems E3.1 and E3.2 and of Corollaries E3.3 and E3.4;
- labels and scope.

The exact sympy values (Lemma E3.7) are re-run, not re-derived term by term. I tested them by an independent exact
computation that shares no code with check_e3_mu.py (§1.2, T1). That computation turns out to prove more than the file
claims (I1).

- **Target:** research/G1/RH/second_order/E3.md (status "NOT REVIEWED (Rule R pending)", 2026-10-20), and the checks
  check_e3_moments, check_e3_sym, check_e3_mu, check_e3_grid (.py/.out).
- **Context read:**
  - E_pgt1.md §§0–6 (Lemma E.2 with (E.2.1), Lemmas E.3–E.5, Prop E.5′);
  - E_plt1.md §§0–6 (Lemma F.1 (i)–(iv), Lemma F.2, Lemma E′.3, Lemma E′.5, Prop E′.5′, Remark F.3);
  - E2_pgt1.md §§0–9 (Lemma E2.3 with the review-A B2 sector argument, Lemma E2.4, Prop E2.5, Lemma E2.6, Remarks E2.10 and E2.14);
  - REVIEW_PlanE2_A.md;
  - RH/CITATIONS.md entries "(Plan E3)" and "(DLMF-zeta, Plan 67)";
  - E_p1.md (table rows E1.4–E1.10, for §8 only);
  - AGENTS.md and VERIFICATION_POLICY.md.
- I did not edit E3.md or any other file except this report. I did not write to the repo cache tmp/plan62_cache: new
  coefficients went to the scratchpad. All my scripts are in
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/reviewE3A/. The decisive one (T1) is
  reproduced in the Appendix.

## Overall verdict: **ACCEPT WITH FIXES** (analysis)

I found **no mathematical error**. Theorem E3.1, Theorem E3.2, Corollary E3.3, Corollary E3.4, Lemma F.1′, Lemma E3.4 and
Prop E3.6 are correct as stated, under the labels given. The fixes are:
- B1 (MINOR): one missing justification, the meromorphy of Δ₂^{mod} for p < 1;
- B2 (MINOR): one wrong expression in the Fubini bound of Lemma F.1′(i);
- B3–B5 (MINOR): label and hygiene items.

The most important finding is **I1**, which is positive. Conjecture E3.C's main claim, **e(μ) = cp·M_μ(4c) exactly**, follows in a few
lines from the file's own Lemma E3.4. The consequences are:
- ε_k = C(2k, k)pc^kζ(−kp) for **every** k ≤ K;
- the merged n⁻² coefficient at p = 1/j is d₂ − p/12 for **every** j ≥ 2.

Both are PROVED-mod-cite at the level of Theorem E3.2. I verified the identity by exact computer algebra to all orders in M
(not only to weighted order 3), and numerically at p = 1/4, where ε₄ is needed and is outside what E3 proves.

| Statement | Verdict (analysis) | Fixes |
|---|---|---|
| Lemma F.1′ (moments, remainder) | ACCEPT WITH FIXES (re-derived; independently tested from E_pgt1's raw definitions, T2) | B2 |
| Lemma E3.4 (Szegő data, entire gauge, conjugation) | ACCEPT (re-derived in full) | — |
| Lemma E3.5 (circle jumps with the band factor) | ACCEPT WITH FIXES | B1 |
| Prop E3.6 (second-order small norm, all p ≠ 1) | ACCEPT (re-derived; remainder justified) | — |
| Lemma E3.7 | ACCEPT; true exactly, not only to weighted order 3 | I1 |
| Thm E3.1 (p > 1, κ_p n^{−1−p}, O(n⁻³)) | ACCEPT | — |
| Thm E3.2 (0 < p < 1) | ACCEPT; ε_j can be stated for all j | I1, I2 |
| Cor E3.3, Cor E3.4 (exponent separation, p = 1/j) | ACCEPT (logic re-checked, including p ∈ (1/2, 1) for Cor E3.4(i)) | I1 |
| Conj E3.C | upgrade: the e(μ) part and the ε_k formula are provable (I1); the p = 1 statement stays CONJECTURE/E2.10 | B4, I1 |
| §8 (p = 1, GAP) | ACCEPT (correctly labelled GAP; references exist) | — |
| Numerics | ACCEPT (all four reproduced; NUMERICAL, not used in the proofs) | B3, I4 |

## 1. Re-runs and independent tests (Rule N)

Python: the session venv given in the brief, run from research/G1/RH/second_order/checks.

### 1.1 The authors' checks

| Script | Result |
|---|---|
| check_e3_moments.py | 5 s; output identical to check_e3_moments.out (timing lines aside) |
| check_e3_sym.py | 1 s; identical; "ALL ASSERTIONS PASSED" |
| check_e3_mu.py | **46 s** here (the brief expected 10+ min); identical to check_e3_mu.out; "ALL ASSERTIONS PASSED" |
| check_e3_grid.py | 5 s from the cached Plan 62 coefficients; identical |

These numbers agree with what §7 of E3 claims:
- n⁻² coefficient at p ∈ {3/4, 0.6}: d₂ to 2.8·10⁻⁶ … 7.4·10⁻⁵, with half-ranges 1.5·10⁻⁴ … 1.7·10⁻³;
- p = 1/2: d₂ − 1/24 to 6.7·10⁻⁷ and 2.5·10⁻⁶;
- κ_p at p ∈ {5/4, 3/2}: to 6.5·10⁻⁷ … 1.9·10⁻⁵;
- moments: relative error 0 to 5·10⁻⁴⁰, and the p = 2 zeros at 10⁻⁵⁰ … 10⁻⁵⁷.

### 1.2 Reviewer tests (scripts in the scratchpad)

**(T1) Exact tilted residues through the gauge, to all orders in the tilt** (gauge_res.py, Appendix).
- Input: E_pgt1 Lemma E.5's A_r, B_r, A₀, and the gauge of Lemma E3.4(ii) for an **arbitrary** entire M, written
  G = T[[C, −(z−4c)S], [−zS, C]]T⁻¹ with C = cosh(𝓡M/2) and S = sinh(𝓡M/2)/𝓡 as series in 𝓡² = z(z−4c).
- Computation: the Laurent data of GΔ₁^{mod}G⁻¹. At 4c the residue is G(4c)A_rG(4c)⁻¹ + G′B_rG⁻¹ + GB_r(G⁻¹)′. At 0 it is
  G(0)A₀G(0)⁻¹, since there is only a simple pole.
- Result (sympy, exact, with m₀ = M(4c), m₁ = M′(4c), … free symbols):
  - B_r^μ = B_r;
  - A₀^μ = A₀;
  - A_r^μ − A_r = c²m₀p[[−(α+1) + cm₀, i(α+2) − icm₀], [iα − icm₀, (α+1) − cm₀]];
  - **e(μ) = i((ΔA)₂₁ − (ΔA)₁₂)/(2c) = c·p·m₀ = cp·M_μ(4c), exactly.**
- The quadratic term cm₀ in A_r^μ cancels in the b-functional. Its linear part reproduces E_plt1's A_r^{lin}. This agrees with
  check_e3_mu.out at weighted order ≤ 3 and extends it to all orders (I1).

**(T2) Lemma F.1′(ii) from E_pgt1's definitions, not from (E.2.1) or the moments** (flat_pgt1.py, flat_cut.py).
- Method: compute G(z) − G(1) = −j(t(z)) + j(t(1)) + log B(z), with log B(z) = −(1/2π)∫𝔟(y)[1/(y−z) − 1/(y−1)]dy and
  𝔟 = 2Im(−j(t₊) − Log(1 − e^{−2πit₊})), by mpmath quadrature at 30 digits. Then subtract the k = 1, 2, 3 terms of
  Σ m_k(z^k − 1).
- Points: p ∈ {5/4, 3/2, 3}; z ∈ {0.3, 3, 2+1.5i}; n = 10, 20, 40. In every case:
  - n^{2p}·(residual after k = 1) tends to ζ(−2p)(z²−1)/2;
  - n^{3p}·(residual after k = 2) tends to ζ(−3p)(z³−1)/3. Examples:
    - p = 3/2, z = 3: −0.026792 against −0.026794;
    - p = 3, z = 3: −0.0656566 against −0.0656566, where the k = 2 term vanishes because ζ(−6) = 0;
  - n^{4p}·(residual after k = 3) is bounded.
- Boundary values near the cut: z = −0.5, −2, −4 at Im z = 0.05 and 0.005. Here n^{2p}·residual converges to the k = 2
  prediction at both p. For example, p = 3/2, z = −2 + 0.005i gives 0.012793 → 0.012604 → 0.012537 against 0.012500.
- So the ζ(−kp) law for p > 1 is confirmed through the Binet and B factors themselves, not only through the moment integral.
  This also confirms the sign bookkeeping y = −r (a sign error would flip the k-odd terms).
- (A first naive run without breakpoints at r = |Re z| gave garbage for z on or near the cut, from the near-pole of the
  Binet part of 𝔟. This was a quadrature artefact and is gone with breakpoints.)

**(T3) New (p, s), coefficients generated by me** (gen.py, myfit.py).
- Source: so_coeffs.measure and jacobi_rkpw at quad precision, n ≤ 1600, written to the scratchpad. Tail K = 200·nmax, and
  where marked 400·nmax as a tail-stability check.
- Fit: subtract the analytically known terms, then least squares over the remaining exponents {1 + i + jp}, orders 4–7,
  windows 0.1–0.3. This is the same fitting style as check_e3_grid, but with new data. The closed forms enter only in the
  comparison column. In the table below, ε_k := C(2k, k)pc^kζ(−kp).

| (p, s) | quantity | fit ± half-range | prediction | diff |
|---|---|---|---|---|
| (1/3, 5/2), K = 200n | n⁻² coeff | −2.36433 ± 4.1·10⁻³ | d₂ − 1/36 = −2.36458 | 2.5·10⁻⁴ |
| (1/3, 5/2), K = 400n | n⁻² coeff | −2.36445 ± 4.1·10⁻³ | −2.36458 | 1.3·10⁻⁴ (plain d₂ = −2.33681 is 7 half-ranges off) |
| (1/3, 5/2), K = 400n | ε₂ (n^{−5/3}) | −0.0421244 ± 1.3·10⁻⁴ | −0.0421269 | 2.5·10⁻⁶ |
| (1/4, 2), K = 400n | n⁻² coeff | −1.82424 ± 8.2·10⁻³ | **d₂ + ε₄ = d₂ − 1/48 = −1.82292** | 1.3·10⁻³ (plain d₂ = −1.80208 is 2.7 half-ranges off) |
| (1/4, 2), K = 400n | ε₂ (n^{−3/2}) | −0.0372737 ± 3.6·10⁻⁵ | −0.0372707 | 2.9·10⁻⁶ |
| (1/4, 2), K = 400n | ε₃ (n^{−7/4}) | −0.0276596 ± 4.3·10⁻⁴ | −0.0276116 | 4.8·10⁻⁵ |
| (0.4, 5/2) | n⁻² coeff | −1.1775 ± 6.1·10⁻² | d₂ = −1.16771 | 9.7·10⁻³ (dense exponents 1.8, 2, 2.2; weak test) |
| (0.4, 5/2) | ε₂ (n^{−1.8}) | −0.04384 ± 2.9·10⁻³ | −0.04342 | 4·10⁻⁴ |
| (0.7, 7/4) | n⁻² coeff | +0.3106987 ± 3.6·10⁻⁴ | d₂ = +0.3107037 | 4.9·10⁻⁶ |
| (7/4, 5/2) | n^{−11/4} coeff (after d₂) | −0.020575 ± 6.5·10⁻³ | κ_p = −0.020555 | 2·10⁻⁵ (weak: 1+p is close to 3) |

What this adds to the authors' grid:
- p = 1/3: the merged coefficient d₂ − p/12, at an s not used anywhere in E3. This is the second case of Cor E3.3(ii),
  which the authors' grid does not test (it has only p = 1/2).
- p = 1/4: the first data point for ε₄, which E3 leaves conjectural and I1 proves.
- Tail-doubling moves the values by less than the half-range.

**(T4) Identity behind I1.** Σ_{j<k}4^{k−1−j}C(2j, j) = kC(2k, k)/2, checked for k ≤ 30 (identity.py). It holds in general by
the generating functions (1 − 4x)^{−1/2}/(1 − 4x) = (1 − 4x)^{−3/2}.

## 2. Re-derivations (what I checked by hand)

### 2.1 Lemma F.1′(i) (Mellin computation)

**Boundary value and the exponent aₙ.**
- On (−∞, 0) put y = −r. The upper boundary value is y₊ = re^{iπ}, so t₊ = ny₊^{−1/p} = nr^{−1/p}e^{−iπ/p}.
- With θ = πt, e^{−2iθ₊} = exp(−aₙr^{−1/p}), where aₙ = 2πine^{−iπ/p}.
- Re aₙ = 2πn·Re(ie^{−iπ/p}) = 2πn sin(π/p) > 0 for p > 1, and arg aₙ = π/2 − π/p ∈ (−π/2, π/2). ✓

**Density.** 𝔢 = 2Im Log(1 − q) is E_pgt1's jump i𝔢 = G₊ − G₋. Since |q| < 1, the principal Log(1 − q) = −Σq^m/m. ✓

**Substitution.** With w = r^{−1/p}: r^{−k−1}dr = −pw^{kp−1}dw, and r: 0 → ∞ becomes w: ∞ → 0, so ∫₀^∞ = p∫₀^∞. ✓

**DLMF 5.9.1.** Take μ = 1, ν = kp (Re ν > 0) and z = maₙ (Re z > 0, principal power). Then (maₙ)^{−kp} =
(2πmn)^{−kp}e^{−ikp(π/2−π/p)} = (2πmn)^{−kp}e^{−iπkp/2}(−1)^k. ✓

**Sum and sign bookkeeping.**
- Summing over m: −2Im[pΓ(kp)ζ(1+kp)(2πn)^{−kp}(−1)^ke^{−iπkp/2}] = 2(−1)^kpΓζ(2πn)^{−kp}sin(πkp/2). ✓
- With y^{−k−1} = (−1)^{k+1}r^{−k−1} and ∫_{−∞}^0 g(y)dy = ∫_0^∞ g(−r)dr: m_k = −(1/π)pΓ(kp)ζ(1+kp)(2πn)^{−kp}sin(πkp/2).
  This is literally E_plt1 F.1(iii)'s intermediate expression, hence ζ(−kp)/(kn^{kp}) by DLMF 25.4.1. ✓
- A sign slip in y = −r would give (−1)^k·(the truth). T2 at odd k rules this out.

**Fubini.** The bound needs Σ_m(1/m)∫|q|^m r^{−k−1}dr < ∞. The integral is pΓ(kp)(m Re aₙ)^{−kp}, not pΓ(kp)|maₙ|^{−kp} as the
file writes (B2). Both are finite, so the conclusion stands.

**Citation.** The CITATIONS entry "(Plan E3)" quotes 5.9.1 with its hypotheses "ℜν > 0, μ > 0, ℜz > 0" and the principal-value
convention. The check of each hypothesis is in the entry and in the proof. Rule C ✓.

### 2.2 Lemma F.1′(ii) (remainder)

**Kernel expansion.** (z−1)/((y−z)(y−1)) = 1/(y−z) − 1/(y−1) = Σ_{k≥1}(z^k − 1)y^{−k−1}, with a tail O(|y|^{−K−2}) uniformly
for |y| ≥ 2R₁ and |z| ≤ R₁. Its z-derivative is also O(|y|^{−K−2}).

**Far part.** ∫_{|y|>2R₁}|𝔢||y|^{−K−2}dy ≤ π∫₀^∞e^{−2π sin(π/p)nr^{−1/p}}r^{−K−2}dr = C·n^{−(K+1)p} (substitute r = n^pw). ✓

**Near parts.**
- The near part of (E.2.1) is O(e^{−cn}), including boundary values and the derivative (E_pgt1 E.2(c), unchanged).
- The near parts of the m_k (k ≤ K) are O(e^{−cn}), so the full moments may replace the far ones. ✓

**Derivative bounds.** These are as claimed: differentiate under the far integral, and use Cauchy's estimate for the
η-version. T2 confirms the expansion including boundary values near the cut.

### 2.3 Lemma E3.4 (re-derived completely)

**(i) Tilted Szegő data.**
- For 𝔠 = −Σμ_kx^k: (𝔠(x) − 𝔠(z))/(z − x) = Σμ_k(x^k − z^k)/(x − z) = Σμ_kΣ_{j<k}x^jz^{k−1−j}.
- The arcsine moments: with x = 4c sin²φ, dx/√(x(4c−x)) = 2dφ, so (1/π)∫₀^{4c}x^jdx/√(x(4c−x)) = (2/π)(4c)^j∫₀^{π/2}sin^{2j}φ dφ =
  C(2j, j)c^j. ✓
- k = 1 gives back E_plt1 Lemma F.2 (Q₁ = 1). ✓
- ω ↦ ωD_q²/q = ωe^{𝓡M}, and ρ² = e^{∓iπα}/ω (E_pgt1 E.4(iii)) ↦ ρ²e^{−𝓡M}. ✓

**(ii) The gauge is entire.**
- T⁻¹σ₃T = σ₁ (direct multiplication), so T⁻¹e^{−hσ₃}T = e^{−hσ₁}, and conjugating by 𝔞_∞^{σ₃} gives the displayed G_μ. ✓
- (𝔞_∞²𝓡)² = ((z−4c)/z)·z(z−4c) = (z−4c)². Both 𝔞_∞²𝓡 and z − 4c are analytic on the connected set ℂ∖[0, 4c] and are ~ z at ∞,
  so 𝔞_∞²𝓡 ≡ z − 4c. Likewise 𝔞_∞^{−2}𝓡 ≡ z. ✓ (The branch of 𝓡 used here, ~ z at ∞ with cut [0, 4c], is the one in (i) and
  in E_plt1's check: 𝓡 = −v(4c+v²)^{1/2} on z = −v².)
- cosh(𝓡M/2) and sinh(𝓡M/2)/𝓡 are power series in 𝓡²M², hence entire in (z, μ). det = 1. ✓

**(iii) Conjugation of the jump data.**
- Airy datum: (−1/φ̃)^kP₀^∞(−ω)^{−σ₃/2}X_k(−ω)^{σ₃/2}(P₀^∞)⁻¹. The k = 2 prefactor 1/φ̃² of E2 is (−1/φ̃)². ✓
- Bessel datum: (2f^{1/2})^{−k}P₀^∞ρ^{σ₃}(σ₃Ξ_kσ₃)ρ^{−σ₃}(P₀^∞)⁻¹.
  - At k = 1 it reproduces E_plt1's Q₀/(16f^{1/2}): σ₃Ξ₁σ₃ = Q₀/8.
  - At k = 2 it reproduces E2's 1/(4f).
- Both edges pick up the **same** factor e^{−(𝓡M/2)σ₃} next to P₀^∞:
  - at the soft edge, from (−ω^μ)^{−σ₃/2};
  - at the hard edge, from (ρ^μ)^{σ₃}, which enters only through ρ², so the square-root branch is irrelevant.
- So Δ^μ = G_μΔ^{mod}G_μ⁻¹ at both edges, for both orders. ✓
- **The ρ-dependence.** For p < 1 the actual ρ is built from the glued W̃ with sector values of 𝒢. By E_plt1 F.1(iv) the
  polynomial part Σm_k(z^k − 1) is the **same** in S_in and S_out; only E_n^{(K)} has sector values. So the tilt is a
  single entire factor and the conjugation is legitimate. ✓

### 2.4 Lemma E3.5 and Prop E3.6 (transfer to 0 < p < 1)

**Sectors.**
- In the middle sector |arg ζ| < π − θ_L, |ph w| < π/2 − θ_L/2, so DLMF 10.40.1–4 apply with δ = θ_L/2 to any number of terms.
- In the outer sectors, ph 2(−ζ)^{1/2} ∈ (−θ_L/2, θ_L/2) lies well inside 10.17.5–6 and 10.17.11–12.
- E2's review-A B2 argument (the pattern of C_k is the same k-independent sign pattern in every sector, so Ξ_k is
  sector-independent) never uses the ray angle. So Ξ₂ is the same for the p < 1 parametrix. ✓

**Glue.** The glue changes the analytic prefactor by O(e^{−c′n}) (RH_plt1b §2), which is inside O(n⁻³). ✓

**n-dependence.**
- log(ω/ω^{μ_n}) = log(D²_{q₂}/q₂), with q₂ = e^{−2E_n^{(K)}}.
- This is O(n^{−(K+1)p}) on both circles, by E_plt1 E′.3's window argument with E_n replaced by E_n^{(K)}. The needed
  sup and derivative bounds are E_plt1 F.1(iv) for general K (p < 1) and F.1′(ii) (p > 1). ✓
- Δ_k depends analytically on (ρ²)^{±1} and (−ω)^{±1/2}, which are bounded above and below (e^{±𝓡M/2} → 1). Hence
  Δ_k = Δ_k^{μ_n} + O(n^{−(K+1)p}). ✓

**Small norm.**
- The off-circle jumps for p < 1 are E_plt1 Prop E′.5′'s list:
  - lips: O(n^{−K′}min(1, |z|^{K′})) for every K′;
  - seam segments: super-small;
  - far pieces: O(e^{−n/C}) or O(n^{−pn/4}).
  All are O(n^{−3}) in L¹∩L²∩L^∞ on a contour of length O(n^p), with the uniform Cauchy bound of Paper 2 F1 (all p).
- The Neumann expansion of E2 Prop E2.5 then gives R − I = 𝒞(J − I) + 𝒞(𝒞₋(J − I)(J − I)) + O(n⁻³).
- With J − I = Δ₁^{μ_n}/n + Δ₂^{μ_n}/n² + O(n⁻³ + n^{−1−(K+1)p}) on the circles, the first iterate produces the error
  n^{−1−(K+1)p}, and the second iterate produces n^{−2−(K+1)p}, which is smaller. **The stated remainder
  O(n⁻³ + n^{−1−(K+1)p}) is justified.** ✓
- The residue evaluation needs Δ_k^{μ_n} meromorphic with E2's pole orders: G is entire and invertible, so this follows from
  the μ = 0 statement. For k = 2 and p < 1 that statement is not quite cited (B1).

### 2.5 Proof of Theorem E3.2 (p-freeness of the μ = 0 data)

**Model data are p-free.**
- E_pgt1 Lemma E.4 and E2 Lemma E2.4 derive f, φ̃ and ω^{mod}, ρ^{mod} from μ*'s density λ_pI_{x/4c}(1/p + ½, ½). That
  density is valid for all p > 0 (E_plt1 §2 item 5, REVIEWED).
- The series in E2.4 use only a′ = 1/p + ½ > 0 and |e| < 1. Nothing uses p > 1.

**The computer algebra is p-free.**
- check_e2_sym.py declares p (and α, c) only as positive symbols, and asserts d₂ as an identity of rational functions in p
  and s. So 𝔡(0) = d₂(p, s) for 0 < p < 1 as well. ✓
- T3 at p = 0.7 and the authors' grid at p = 3/4 and 0.6 agree to 10⁻⁵, which is a separate confirmation.

**The bound 𝔡(μ_n) − 𝔡(0) = O(n^{−p}).**
- 𝔡 = 𝔟/2 − 𝔞²/8 is a polynomial in the entries of the entire functions a(μ), b(μ), so 𝔡(μ_n) − 𝔡(0) = O(|μ_n|).
- |μ_{n,k}| = O(n^{−kp}) ≤ O(n^{−p}). ✓
- (Writing O(‖μ_n‖_w) is correct but needlessly roundabout; see I3.)

**Grouping e(μ_n) by weighted degree.**
- This is legitimate because e is entire on a finite-dimensional space, and the tail of weighted degree ≥ K + 1 is
  O(n^{−(K+1)p}).
- Every ε_jn^{−1−jp} (j ≤ K) dominates both n^{−2−p} and n^{−1−(K+1)p}, since 1 + jp ≤ 2. ✓

### 2.6 Corollaries and exponent separation

**Cor E3.3(i).** If 1/p ∉ ℕ, the exponent 2 differs from every 1 + jp (j ≤ K). The remainder exponents are 2 + p and
1 + (K+1)p, and both are > 2, the second because (K+1)p > 1 strictly. So the n⁻² coefficient is identifiable. ✓

**Cor E3.3(ii).** At p = 1/j₀ we have K = j₀ and 1 + Kp = 2. Then ν_K = 2 + p > 2.
- I(1/j) = (√π/2)Γ(j+½)/Γ(j+1) = (π/2)C(2j, j)4^{−j}, so c(1/j)^j = 1/C(2j, j). ✓
- ε₂(½) = 3·(1/6)(−1/12) = −1/24 and ε₃(⅓) = (20/3)(1/20)(−1/12) = −1/36. ✓

**Cor E3.4** (apply Prop E3.6 with K = 3, legitimately for every p < 1, also when K > ⌊1/p⌋).
- (i) For p ∈ (1/2, 1), 1 + 2p ∈ (2, 3) still lies strictly below 2 + p, 3 and 1 + 3p, so ε₂ is identifiable on all of
  (0, 1)∖{½}. ✓
- (ii) For p < 1/2, 1 + 3p < 2 + p, and 1 + 3p ≠ 2 unless p = 1/3. ✓

### 2.7 §8 (p = 1)

The cited E_p1 results exist with the stated content: Prop E1.4(iii), Lemma E1.5 (m ≤ 2 closed forms), Thm E1.6 (s = 3/2,
5/2) and Thm E1.10 (first order, all s). The section correctly makes no claim (GAP). The obstruction it names is a real
one: the Darboux step for x^mTC, m ≥ 3, has no closed form, and Birkhoff–Adams theory is not read, so it cannot be used
under Rule C.

## 3. Findings

### Fixes required

**B1 (MINOR) — meromorphy of Δ₂^{mod} for 0 < p < 1 is not cited correctly.**

*The gap.* Lemma E3.4(iii) and Prop E3.6 say Δ_k^{μ} has "the pole orders of Δ_k^{mod} (E2 Lemma E2.6(a), E_pgt1 Lemma E.5)".
Those lemmas are stated and proved for p > 1. E_plt1 Lemma E′.5 covers Δ₁ for p < 1, but nothing covers Δ₂ for p < 1.

*Why the statement is still true.* The explicit formulas of Δ₂^{⋄,mod} are the same functions of z (with p as a parameter).
The structural argument of E_plt1 Lemma E′.5 extends to k = 2 in two lines:
- **Soft edge.** On (4c − ε, 4c), P₀^∞₊ = P₀^∞₋J with J = iσ₂, φ̃₊ = −φ̃₋ and (−ω)^{1/2}₊(−ω)^{1/2}₋ = 1. The prefactor
  1/φ̃² does not change sign. X₂ = ½(u₂+v₂)I − ½(u₂−v₂)σ₂ commutes with J, so Δ₂^r₊ = Δ₂^r₋.
- **Hard edge.** On (0, δ), f₊ = f₋, so 1/(4f) does not change sign. σ₃Ξ₂σ₃ = ½(a₂+b₂)I + ½(a₂−b₂)σ₂ commutes with J. With the
  ρ relations of E′.5, Δ₂⁰ has no jump on (0, δ). On (−δ, 0) the argument is unchanged.
- **Pole orders.** These follow from the growth bounds |Δ₂^r| ≤ C|z−4c|^{−7/2} and |Δ₂⁰| ≤ C|z|^{−3/2}. With single-valuedness
  they give poles of order ≤ 3 and ≤ 1 (the half-integer powers cancel). This is consistent with E2.6(a)'s "u⁷Δ₂^r odd in u" and
  "v⁴Δ₂⁰ even".

*Fix.* Add this paragraph to Lemma E3.5 (or to E3.4(iii)). Alternatively, state that E2 Lemma E2.6(a)'s argument uses no p > 1
input, with the p < 1 model parametrix (rays at π − θ_L) in place of KMVV's.

**B2 (MINOR) — the Fubini bound in Lemma F.1′(i) uses the wrong modulus.**

The file writes "Σ_m(1/m)pΓ(kp)|maₙ|^{−kp} < ∞, which is the Fubini bound". But ∫₀^∞|e^{−maₙw}|w^{kp−1}dw = Γ(kp)(m Re aₙ)^{−kp}.

*Fix.* Replace with Σ_m(1/m)pΓ(kp)(2πmn sin(π/p))^{−kp} = pΓ(kp)ζ(1+kp)(2πn sin(π/p))^{−kp} < ∞. The conclusion is unchanged.

**B3 (MINOR) — check-script hygiene (Rule N: the outputs are computed, so only docstrings and comments are affected).**
- check_e3_moments.py's docstring cites "E3_pgt1.md Lemma F.1′". The file is E3.md.
- check_e3_mu.py's docstring cites "E3.md Lemma E3.5, Theorem E3.3". It should cite Lemma E3.4 (Szegő data), Lemma E3.7 and
  Cor E3.4.
- `mtrunc`'s docstring says "keep 1, mu1, mu1², mu2 (drop mu1³, mu1 mu2…) … keep t^≤2". The code keeps t⁰…t³, i.e. weighted
  order ≤ 3, which is what E3 claims.
- `expM`'s comment says "to second order", but the code is cubic.

*Fix.* Correct the four comments. No code change is needed.

**B4 (MINOR) — labels around Conjecture E3.C.**
- The summary table says the p = 1 instance is "NUMERICAL at p = 1 via E2 Remark E2.10". E2.10 is PROVED-mod-cite at
  s ∈ {3/2, 5/2} (E_p1 Thm E1.6) and CONJECTURE otherwise, as E3 §1 itself says correctly. Make the table match.
- After I1, split the conjecture:
  - (a) e(μ) = cpM_μ(4c), ε_k = C(2k, k)pc^kζ(−kp) for all k ≤ K, and the merged coefficient d₂ − p/12 at every p = 1/j
    (j ≥ 2): PROVED-mod-cite, as Thm E3.2;
  - (b) the p = 1 statement d₂(1, s) − 1/12 for s ∉ {3/2, 5/2}: stays CONJECTURE, because p = 1 is outside Lemmas F.1/F.1′
    (§8);
  - the zeta-regularised formal sum: stays HEURISTIC.

**B5 (MINOR) — statements that I1 makes inaccurate.**
- Thm E3.2: "ε_j … a polynomial in ζ(−p), …, ζ(−jp) with coefficients depending on p, c and possibly s".
- §9: "ε_j for j ≥ 4 … values conjectural".
- §6 Lemma E3.7: "modulo monomials of weighted degree ≥ 4".

*Fix.* If I1 is adopted, ε_j = C(2j, j)pc^jζ(−jp): it is linear in ζ(−jp) alone and s-independent. Update the three places
(keep Lemma E3.7 as the order-3 sympy cross-check).

### INFO

**I1 (INFO; recommended upgrade) — e(μ) = cp·M_μ(4c) exactly, by a short proof from Lemma E3.4.**

*Proof.*
1. Δ₁^{μ} = G_μΔ₁^{mod}G_μ⁻¹ (Lemma E3.4(iii)). Δ₁^{r,mod} = B_r/y² + A_r/y + O(1), with y = z − 4c (E_pgt1 Lemma E.5). G is
   entire, so Res_{4c}Δ₁^μ = G₀A_rG₀⁻¹ + G₁B_rG₀⁻¹ − G₀B_rG₀⁻¹G₁G₀⁻¹, where G = G₀ + G₁y + ….
2. At z = 4c, 𝓡 = 0, so C = 1 and S = M/2. Hence G₀ = T[[1, 0], [−2cM(4c), 1]]T⁻¹. G₁ involves M(4c) and M′(4c).
3. At z = 0, G(0) = T[[1, 2cM(0)], [0, 1]]T⁻¹. This commutes with A₀ ∝ Te₁₂T⁻¹ (E_pgt1 Lemma E.5 method), so A₀^μ = A₀ exactly.
4. The b-functional at order 1/n is linear in R_1⁽¹⁾: i(A₂₁ − A₁₂)/(2c). Evaluated on step 1 it gives exactly cp·M(4c). The
   M′(4c) terms and the quadratic term c²m₀²p(·) cancel. This is T1, an exact sympy computation for arbitrary entire M. By
   hand it is a 2×2 computation with the explicit T, A_r, B_r.
5. With μ_{n,k} = 2ζ(−kp)/(kn^{kp}) and Q_k(4c) = c^{k−1}kC(2k, k)/2 (T4): ε_k = cp·(2ζ(−kp)/k)·c^{k−1}kC(2k, k)/2 =
   C(2k, k)pc^kζ(−kp) for every k ≤ K.
6. At p = 1/j, c^j = 1/C(2j, j) and ζ(−1) = −1/12, so ε_j = −p/12 for every j ≥ 2.

*Evidence.* T3 confirms the j = 4 case at p = 1/4: the fit gives d₂ − 1/48 within half a half-range, and plain d₂ is 2.7
half-ranges off.

*Consequences.* This closes the first two bullets of §9 for 0 < p < 1, p ≠ 1 (p = 1 stays open). B_r^μ = B_r also holds
exactly (step 1 with T1). This is the "structural identity for the gauge at 4c" that §9 asks for.

*Scope note.* For n^pα_n (the a-functional) the quadratic part of A_r^μ does **not** obviously cancel. So no analogous claim
should be made for α_n without computing it.

**I2 (INFO).** Thm E3.2 states "O(n^{−2−p} + n^{−ν_K})". One may add that the n⁻³ of Prop E3.6 is absorbed (n⁻³ ≤ n^{−2−p} for
p < 1); the proof says so already. Also, Cor E3.4(i)'s range (1/2, 1), where K = 1 < 2, is covered by the K = 3 application,
not by Thm E3.2. A half-sentence in Thm E3.2 ("ε₂ … whenever 2 ≤ K; for 1/2 < p < 1 see Cor E3.4") would prevent the
apparent mismatch.

**I3 (INFO).** "𝔡(μ_n) − 𝔡(0) = O(‖μ_n‖_w)". O(|μ_n|) is what entire-ness gives directly, and |μ_n| = O(n^{−p}). The current
wording is correct but indirect.

**I4 (INFO).**
- §7 last sentence ("Before subtraction the plain fits … had half-ranges ≈ 0.1; they agreed too") is not produced by any
  .out file. Either print it from check_e3_grid.py or drop it (Rule N 3).
- check_e3_mu.py ran in 46 s here, not 10+ min. Harmless.

**I5 (INFO).** Lemma F.1′ is used only with K = 1 (Thm E3.1). The general-K statement is correct (T2 tests K ≤ 3) and harmless.
For p > 2 the κ_p term is O(n⁻³) and Thm E3.1 reduces to E2 with the improved remainder. This is stated correctly.

**I6 (INFO; Rule A).** I tried the following and found no counterexample:
- the wrong branch of (maₙ)^{−kp} (flips the sign of sin(πkp/2); excluded by T2 and the 40-digit moments);
- a sign error in y = −r (odd-k sign flip; excluded by T2);
- a gauge acting differently on the two edges (excluded: both use the same factor e^{−(𝓡M/2)σ₃}, §2.3);
- a hidden μ-dependence of A₀ or B_r at higher order (excluded exactly by T1);
- nonlinear terms in e(μ) (excluded exactly by T1);
- d₂ being p > 1-specific (excluded: the sympy is in symbolic positive p, and T3 at p = 0.7 agrees to 5·10⁻⁶);
- merging at p = 1/3 (T3 confirms d₂ − 1/36 at a new s);
- exponent collisions for Cor E3.4 at p ∈ (1/2, 1) (none, §2.6).

## 4. Log

**Read.**
- AGENTS.md and VERIFICATION_POLICY.md.
- E3.md (all of it).
- E_pgt1.md §§0–6, E_plt1.md §§0–6, E2_pgt1.md §§0–9.
- REVIEW_PlanE2_A.md (for style).
- CITATIONS "(Plan E3)" and "(DLMF-zeta, Plan 67)".
- E_p1.md table.
- so_coeffs.py and so_fit.py.

**Re-derived by hand.**
- F.1′(i): branches, aₙ, substitution, sign bookkeeping, final constant.
- F.1′(ii): kernel tail and far/near split.
- E3.4(i): arcsine moments and the ω, ρ transforms.
- E3.4(ii): T⁻¹σ₃T = σ₁, both branch identities, det = 1.
- E3.4(iii): Airy and Bessel conjugation for k = 1, 2, including the ρ² dependence and the sector-uniform tilt.
- E3.5 and E3.6: sectors at π − θ_L, n-dependence, Neumann bookkeeping, remainder.
- Thm E3.2: p-freeness, 𝔡 bound, weighted grouping.
- Cor E3.3 and E3.4: exponent separation, c(1/j)^j, ε₂(½), ε₃(⅓).
- I1 (steps 1–6).
- B1 (jump argument for Δ₂ at both edges).

**Ran.**
- The four checks: identical outputs.
- gauge_res.py (T1, exact).
- flat_pgt1.py and flat_cut.py (T2, 30 digits, about 10 min).
- gen.py: new quad-precision coefficients at (1/3, 5/2) for K/n = 200 and 400, (1/4, 2) for K/n = 200 and 400, (0.4, 5/2),
  (0.7, 7/4), (7/4, 5/2); n ≤ 1600; 1–5 min each.
- myfit.py (T3) and identity.py (T4).

**Not done.**
- Hand re-derivation of every sympy coefficient of check_e3_mu (superseded by T1's exact gauge computation).
- Rule L.

## Appendix: gauge_res.py (T1)

```python
import sympy as sp
I = sp.I
al, p, c, y = sp.symbols('alpha p c y')
m = sp.symbols('m0:4')                       # M(4c+y) = m0 + m1 y + m2 y^2 + m3 y^3 (only m0, m1 matter)
T = sp.Matrix([[1, 1], [I, -I]]) / sp.sqrt(2); Ti = T.inv()
w = y * (y + 4 * c); M = sum(m[k] * y ** k for k in range(4)); X = w * M ** 2 / 4
C = sum(X ** j / sp.factorial(2 * j) for j in range(3)); S = M / 2 * sum(X ** j / sp.factorial(2 * j + 1) for j in range(3))
N = sp.Matrix([[C, -y * S], [-(y + 4 * c) * S, C]]); Ni = sp.Matrix([[C, y * S], [(y + 4 * c) * S, C]])
G = (T * N * Ti).applyfunc(lambda e: sp.series(sp.expand(e), y, 0, 2).removeO())
Gi = (T * Ni * Ti).applyfunc(lambda e: sp.series(sp.expand(e), y, 0, 2).removeO())
Br = sp.Rational(5, 12) * c ** 2 * p * sp.Matrix([[1, -I], [-I, -1]])
Ar = c / 48 * sp.Matrix([[12*al**2*p + 24*al*p + 11*p + 2, -I*(12*al**2*p + 48*al*p + 49*p + 2)],
                         [-I*(12*al**2*p + p + 2), -(12*al**2*p + 24*al*p + 11*p + 2)]])
G0, G1, H0, H1 = G.subs(y, 0), G.diff(y).subs(y, 0), Gi.subs(y, 0), Gi.diff(y).subs(y, 0)
dA = (G0 * Ar * H0 + G1 * Br * H0 + G0 * Br * H1 - Ar).applyfunc(sp.expand)
print(sp.factor(sp.simplify(I * (dA[1, 0] - dA[0, 1]) / (2 * c))))      # -> c*m0*p
print((G0 * Br * H0 - Br).applyfunc(sp.simplify))                       # -> 0
```
(The full script, with the A₀ check at z = 0, is gauge_res.py in the scratchpad directory above. Output: B_r^μ − B_r = 0,
e(μ) = c·m₀·p, A₀^μ − A₀ = 0.)
