# Rule R review: Plan E3, reviewer B (computation), E3.md

Reviewer: independent second reader B (Rule R, computation side). My scope is:
- check_e3_mu.py against Lemma E3.4 and Lemma E3.7. This covers the generalised Szegő factor, the branches of 𝓡, the
  weighted truncation, the series orders and the extraction.
- The closed-form values (ε_k, c(1/j)^j, the merged constants).
- check_e3_sym.py, check_e3_moments.py and check_e3_grid.py.

I did not review the analytic estimates and accept none of them here. These are the uniformity in Lemma E3.5, the small-norm
bounds of Prop E3.6, Lemma F.1′(ii) and the remainder exponents. They belong to reviewer A.

Date 2026-10-20. Targets:
- research/G1/RH/second_order/E3.md;
- checks/check_e3_mu.py, check_e3_sym.py, check_e3_moments.py, check_e3_grid.py and their .out files.

The standard I compared against is check_e_plt1_sym.py, check_e2_sym.py, check_e_num.py and REVIEW_PlanE2_B.md.

No repository file other than this report was modified. The Plan 62 cache was only read. The new p = 1/3 coefficients went to
a scratch cache, and every script I ran in the repo used `python -B`. My scratch work is in the session scratchpad
`reviewE3B/`, which is not committed:

| File | Purpose |
|---|---|
| orig.py | byte copy of check_e3_mu.py |
| v_*.py (16 variants) | sabotage and truncation tests (§2) |
| dump.py, d_exp1.py, d_exp2.py | the same plus a pickle of A_r(μ), B_r(μ), A₀(μ) |
| gauge.py | exact all-orders residue of G_μΔ₁^{mod}G_μ^{−1} from Lemma E3.4(ii) (§1.5) |
| cmp.py | compares the script's matrices with gauge.py |
| num_mu.py, num_bad.py | independent quadrature route at finite μ (§3) |
| closed.py | closed forms, arcsine moments, Szegő integrals for k = 2, 3, Q_k(4c) identity (§4) |
| g_zero2.py, g_dbl2.py, g_zero1.py | sensitivity of check_e3_grid to ε₂ and ε₁ |
| freefit.py | free fits with ε₂ and ε₃ unconstrained |
| p13.py, fit13.py | new p = 1/3 coefficients (scratch cache) and the merged n⁻² test |

## Overall verdict: **ACCEPT WITH FIXES** (computation only)

Every value the computation claims is correct:
- e(μ) = cp·M_μ(4c), with M_μ(4c) = μ₁ + 6cμ₂ + 30c²μ₃;
- ε_k = C(2k,k)pc^kζ(−kp) for k ≤ 3;
- ε₂(1/2) = −1/24 and ε₃(1/3) = −1/36;
- κ_p = 2pcζ(−p).

I confirmed these by three routes that share only the model data:
1. **Re-run.** The check_e3_mu.py output is identical to check_e3_mu.out (46 s here, not "10+ minutes"). check_e3_sym, check_e3_moments
   and check_e3_grid are also identical on re-run.
2. **An exact all-orders argument (§1.5).** Res_{4c} of G_μΔ₁^{mod}G_μ^{−1} depends only on G_μ(4c) and G_μ′(4c). The
   b-functional then changes by exactly cp·M(4c), **for every polynomial (indeed analytic) tilt and to all orders in μ**. The
   script's full A_r(μ), B_r(μ) and A₀(μ) matrices agree with this formula identically to weighted order 3.
3. **Independent quadrature (§3).** Δ₁ is built pointwise from the Szegő integral of the tilted weight, with no series, no
   Lemma E3.4 closed form and no Laurent bookkeeping. At p ∈ {1/2, 0.6, 3/4} with finite |μ| up to 1, e(μ) = cpM(4c) to ≤ 2·10⁻¹⁰.
   The quadratic finite-difference coefficients are ≤ 5·10⁻¹⁰.

The main finding is not an error. Route 2 turns Conjecture E3.C's linearity statement, and with it ε_k for all k and the merged
value d₂ − p/12 at every p = 1/j (j ≥ 2), into a short proof (F1).

The other findings are:
- F2: the hard-edge half of check_e3_mu cannot detect any error;
- F3: what the script asserts versus what it computes;
- F4: stale text in the scripts;
- F5: an overstatement of what the grid numerics test.

| Item | Verdict (B's scope) | Notes |
|---|---|---|
| Lemma E3.4(i): Szegő factor, sign, arcsine moments, Q_k | ACCEPT | §1.1; quadrature at k = 2, 3 (§4); quadrature route §3 |
| Lemma E3.4(ii) gauge, det = 1 | ACCEPT | re-derived; det G(4c) = 1 asserted in gauge.py |
| 𝓡 branches: z^{1/2}u at 4c, −v(4c+v²)^{1/2} on z = −v² | ACCEPT (F2) | correct by hand; the hard-edge branch is untestable by this check |
| weighted truncation, series orders | ACCEPT WITH FIXES (F3, F4) | O = 7 is ample; O ≥ 4 is the minimum for non-vacuous assertions |
| Lemma E3.7 extraction, e(μ) = cpM(4c) | ACCEPT; **upgrade available (F1)** | §1.4, §1.5, §3 |
| Thm E3.2 constants ε₁, ε₂, ε₃; Cor E3.3(ii), E3.4 values | ACCEPT | §4 |
| Conj E3.C | **provable (F1)** for all p = 1/j, j ≥ 2, given the rest of the E3 framework | §1.5 |
| check_e3_sym (Thm E3.1 bookkeeping) | ACCEPT | identical re-run |
| check_e3_moments (Lemma F.1′(i)) | ACCEPT (F4: stale filename) | identical re-run |
| check_e3_grid | ACCEPT WITH FIXES (F5) | identical re-run; sensitivity in §4 |

## 1. Audit of check_e3_mu.py

### 1.1 Szegő factor (Lemma E3.4(i); script lines 5–8, 55–58, 84–86)

**Sign.** With 𝔠 = log q = −P, Paper 2's representation gives:
- log D² − 𝔠(z) = (𝓡/π)∫(𝔠(x) − 𝔠(z))/(z−x)·dx/√(x(4c−x));
- (𝔠(x)−𝔠(z))/(z−x) = (P(z)−P(x))/(z−x) = Σ_kμ_kΣ_{j<k}x^jz^{k−1−j}.

So log D² + P(z) = 𝓡·Σ_kμ_kΣ_j C(2j,j)c^jz^{k−1−j} = 𝓡M. Hence ω^μ = ω^{mod}e^{+𝓡M} and (ρ^μ)² = (ρ^{mod})²e^{−𝓡M}.

**Where the script applies it.** Line 57 multiplies (−ω) by e^{+𝓡M} (Ep), line 58 multiplies (−ω)⁻¹ by e^{−𝓡M} (Em), and line 86
multiplies ρ² by e^{−𝓡M}. This is the same pattern as check_e_plt1_sym.py lines 70–71 and 127 with λ → M.

**Arcsine moments and Q_k.**
- The moments (1/π)∫₀^{4c}x^j dx/√(x(4c−x)) = C(2j,j)c^j are confirmed by quadrature for j ≤ 5 (closed.py).
- At c = 1, z = 7, the Szegő integral (𝓡/π)∫(P(z)−P(x))/(z−x)dμ_arcsine equals 𝓡Q_k(z) to 20 digits for P = x² and P = x³.
- The script's polynomials M_s (line 56) and M_h (line 85) are Q₂ = z+2c and Q₃ = z²+2cz+6c², evaluated at z = 4c+u² and at
  z = −v². The expansions are correct: (−v²)² + 2c(−v²) + 6c² = v⁴ − 2cv² + 6c².

### 1.2 Branches of 𝓡

**Near 4c.** For z > 4c, 𝓡 = √z·√(z−4c) > 0. With u = (z−4c)^{1/2} this is z^{1/2}u, as in line 55 and in E_plt1's check.

**On the negative axis.** At z = −r, z(z−4c) = r(r+4c) > 0, and 𝓡 ~ z < 0 at −∞ with no cut on (−∞, 0). So
𝓡 = −√(r(r+4c)) = −v(4c+v²)^{1/2} (line 84). This matches check_e_plt1_sym.py line 126. Both branches are right.

The hard-edge branch, however, is not tested by the script; see F2.

### 1.3 Weighted truncation and series orders

**Weighted truncation.** mtrunc substitutes μ_k ↦ t^kμ_k and keeps t⁰…t³ (`range(4)`). This is weighted order 3, as Lemma E3.7
states. It keeps μ₁, μ₂, μ₃, μ₁², μ₁μ₂ and μ₁³, and drops μ₂², μ₁μ₃, μ₁²μ₂ and so on, which are of weighted degree ≥ 4. The
docstring of mtrunc ("keep t^<=2", "drop mu1^3, mu1 mu2") is stale (F4).

**Is O = 7 enough after the 1/(κu⁴) division?** Yes, with a wide margin.
- 𝓡M = z^{1/2}u·M brings only **non-negative** powers of u, so it never lowers the order.
- Mu is u·(Laurent-free polynomial). D1u4 = Mu·inv1/κ is truncated at u⁴ (`tr(…, u, 5)`), and the extraction reads its u⁰
  coefficient (B_r) and its u² coefficient (A_r).
- Every factor is exact to u^{O−1} = u⁶, so the u⁰…u⁴ coefficients are exact. inv1 is only correct to u² (its u⁴ term lacks
  the κ₃ contribution), but the u⁴ coefficient is never used.
- Experiments: O = 5, 4 and 3 all pass every assertion, and O = 2 fails (d₁ = 0). At O = 3 the u³ "odd power" assertion
  is vacuous, so **O = 4 is the smallest truncation at which every assertion is non-vacuous**.

**Hard edge.** `ser(e·v², v, 3)` reads v⁰ and v¹. The exp series in rho2m enters through sympy's own series and is exact.

**expM.** The cubic term of expM (line 44) is redundant. It enters only through (𝓡M)³ = O(u³), and the residue needs (−ω)'s
relative expansion only to u². With expM = 1 + x + x²/2 the dumped A_r(μ) is identical to the cubic version.

With expM = 1 + x (linear only), **all assertions still pass**. Yet the dumped A_r(μ) is then wrong by
c³μ₁p(μ₁ + 12cμ₂)·[[1, −i], [−i, −1]]. The error is invisible because it is symmetric off the diagonal and the b-functional
reads only A₂₁ − A₁₂. See F3.

### 1.4 Extraction

e₁ = i(A₂₁ − A₁₂)/(2c) is the 1/n coefficient of √((P₁+A/n)₁₂(P₁+A/n)₂₁)/c for P₁ = [[0, ic], [−ic, 0]]. This is the same as
check_e_plt1_sym [3] and check_e3_sym. The substitution α = (s−1−p)/p and the derivative read-outs are correct.

**Conversion to ε_k.** μ_{n,1} = 2ζ(−p)n^{−p}, μ_{n,2} = ζ(−2p)n^{−2p} and μ_{n,3} = (2/3)ζ(−3p)n^{−3p}. So:
- ε₂ = 6c²p·ζ(−2p);
- ε₃ = 30c³p·(2/3)ζ(−3p) = 20c³pζ(−3p);
- the line-140 assertion E_k·(2/k) = C(2k,k)pc^k is the right identity.

The printed "e₂ = 4ζ(−p)²E11 + ζ(−2p)E2" uses the right weights.

### 1.5 The exact all-orders statement (gauge.py, cmp.py)

By Lemma E3.4(iii), Δ₁^μ = G_μΔ₁^{mod}G_μ^{−1}, with G_μ entire. Near 4c, Δ₁^{mod} = B_r/w² + A_r/w + O(1) with w = z − 4c. Hence,
**exactly**:

  Res_{4c}Δ₁^μ = G(4c)A_rG(4c)^{−1} + G′(4c)B_rG(4c)^{−1} + G(4c)B_r(G^{−1})′(4c).

From Lemma E3.4(ii), G = T[[cosh h, −wS], [−(4c+w)S, cosh h]]T^{−1} with h = 𝓡M/2 and S = sinh h/𝓡. Only M(4c) and M′(4c) enter.

At 0, Δ₁^{mod} has a simple pole, so Res₀ = G(0)A₀G(0)^{−1}. Here G(0) = T[[1, 2cM(0)], [0, 1]]T^{−1}, and this commutes with
A₀ ∝ [[1, i], [i, −1]].

The sympy results, with M(4c) = M₄ and M′(4c) symbolic and A_r, B_r, A₀ from E_pgt1 Lemma E.5, are:
- det G(4c) = 1;
- G(4c)B_rG(4c)^{−1} = B_r, and A₀ is unchanged;
- Res_{4c} − A_r = M₄c²p·[[M₄c − α − 1, −i(M₄c − α − 2)], [−i(M₄c − α), −(M₄c − α − 1)]];
- **e(M) − e(0) = cp·M₄**, exactly, with no truncation in μ.

The matrix shift is **quadratic** in M(4c), but the quadratic part is symmetric off the diagonal and cancels in A₂₁ − A₁₂.

**Comparison with the script (cmp.py).** I substituted M₄ = μ₁ + 6cμ₂ + 30c²μ₃ and M′(4c) = μ₂ + 10cμ₃ and truncated at
weighted order 3. The script's dumped A_r(μ), B_r(μ) and A₀(μ) then agree with gauge.py **entry by entry** (difference 0, after
unifying symbol assumptions). So check_e3_mu's whole first-order Laurent output, not just the b-functional, is the gauge
formula.

## 2. Making it fail (v_*.py)

Each variant is a textual edit of the copy, run to completion.

| Variant | Result | Failing assertion / printed coefficients |
|---|---|---|
| as in the script | passes | — |
| flip exponent at the soft edge (Ep ↔ Em) | **fails** | line 110: d/dμ₁ = −cp (E2 = −6c²p, E3 = −30c³p) |
| flip the sign of 𝓡 at the soft edge (Rr_s = −z^{1/2}u) | **fails** | line 110, same output as above |
| flip both edges | **fails** | line 110 |
| drop the soft-edge tilt | **fails** | line 110: all μ-coefficients 0 |
| Q₂ = z + c (both edges) | **fails** | line 133: E2 = 5c²p |
| Q₃ with 4c² instead of 6c² | **fails** | line 133: E3 = 28c³p |
| weighted truncation t^{≤2} | **fails** | line 133: E3 = 0 |
| O = 2 | **fails** | line 110: d₁ = 0 |
| O = 3, 4, 5 | passes | (O = 3: the u³ check is vacuous) |
| expM = 1 + x + x²/2 | passes | A_r(μ) identical to the original (correct: cubic redundant) |
| expM = 1 + x | **passes** | A_r(μ) wrong by c³μ₁p(μ₁+12cμ₂)[[1,−i],[−i,−1]]; invisible (F3) |
| **flip exponent at the hard edge** | **passes** | A₀ μ-dependence 0 (F2) |
| **drop the hard-edge tilt** | **passes** | (F2) |
| **flip the sign of 𝓡 on z = −v²** | **passes** | (F2) |
| **wrong M on z = −v² (z = +v²)** | **passes** | (F2) |

**Soft-edge errors.** The script catches every soft-edge error I tried: the sign, the branch, Q₂, Q₃, the weighted order and
the truncation.

**Hard-edge errors.** It catches none of them. This is structural. Res₀ = G(0)A₀G(0)^{−1} = A₀ for every value of M(0) (§1.5),
so A₀ cannot move whatever the hard-edge tilt is. The hard-edge branch is therefore verified only by hand (§1.2). It is
irrelevant to the b-functional at order 1/n.

## 3. Independent route (num_mu.py; NUMERICAL)

**Construction.** As in check_e_num.py [3]:
- g, φ, φ̃ and f come from quadrature of the arcsine mixture;
- ω = D_W²/W₀, where log D_W² is the Szegő integral of log W = α log x + log(4c−x) − P(x) and W₀(z) contains e^{−P(z)}.

The Lemma E3.4 closed form, the gauge and all u- and v-series are bypassed. Δ₁ is formed pointwise at both circles (radii 0.3,
K = 48 nodes, dps 20). A = (1/2πi)∮Δ₁ and e(μ) = i(A₂₁ − A₁₂)/(2c) − d₁. The g-values are computed once per node and reused
for all μ.

**Results at finite μ (not infinitesimal).**

| (p, s) | d₁ (vs −(s−1)/2) | max \|e(μ) − cpM(4c)\| over 7 μ-vectors, \|μ_k\| ≤ 1 | ∂e/∂μ_k vs cp, 6c²p, 30c³p | μ₁², μ₁μ₂, μ₂² coefficients |
|---|---|---|---|---|
| (1/2, 2) | −0.5 (exact to print) | 2.8·10⁻¹¹ | agree to 10 digits | 1.5·10⁻¹¹, 4.6·10⁻¹¹, 3.7·10⁻¹¹ |
| (0.6, 3/2) | −0.25000000004 | 4.1·10⁻¹¹ | agree to 10 digits | −1.1·10⁻¹¹, −3.2·10⁻¹¹, −2.1·10⁻¹¹ |
| (3/4, 3) | −1.00000000005 | 2.0·10⁻¹⁰ | agree to 10 digits | −1.3·10⁻¹⁰, −4.9·10⁻¹⁰, −4.9·10⁻¹⁰ |

The second-difference coefficients were taken with step h = 0.2.

What this covers:
- The μ-vectors include (1, −0.5, 0.3) and (−0.5, 0.4, −0.2). Linearity therefore holds well beyond weighted order 3,
  including μ₂², μ₁μ₃ and higher. This numerically confirms F1.
- s = 3/2 (α = 1/6 at p = 0.6) and s = 3 (α = 1 at p = 3/4) extend the α-range.

**Sabotage (num_bad.py).** I flipped the sign of P inside the Szegő integral only, giving a tilt inconsistent with W₀. At
(1/2, 2), e − cpM(4c) is then 0.21 … 0.86, with quadratic coefficients of order 1. The route therefore discriminates by about
nine orders of magnitude.

**Independence.** This route shares with check_e3_mu only:
- the DLMF matrices X₁ and Q₀;
- the conjugation structure of E_pgt1 Lemma E.3;
- the orientation convention.

Rule N: the differences above are quadrature noise, not error bounds.

## 4. Closed forms, the other scripts, and the grid

**Closed forms (closed.py, 40 digits).**
- Q_k(4c) = c^{k−1}·kC(2k,k)/2. This is the exact integer identity Σ_{j<k}4^{k−1−j}C(2j,j) = kC(2k,k)/2, checked for k < 40.
  So cp·M_{μ_n}(4c) has weighted-degree-k part C(2k,k)pc^kζ(−kp) for **every** k.
- c(1/j)^j·C(2j,j) = 1 to ≤ 7·10⁻⁴¹ for j = 1…8, and ε_j(1/j) + 1/(12j) = 0 to ≤ 7·10⁻⁴³. The proof in E3.md §6 (via
  I(1/j) = (π/2)C(2j,j)4^{−j}) is correct as written.
- Values of ε₁, ε₂, ε₃:

| p | ε₁ | ε₂ | ε₃ |
|---|---|---|---|
| 0.3 | −0.0633920 | −0.0406378 | −0.0282319 |
| 1/2 | −0.0848692 | −1/24 | −0.0173405 |
| 0.6 | −0.0899767 | −0.0363766 | −0.0071501 |
| 3/4 | −0.0918692 | −0.0240861 | +0.0083144 |
| 5/4 | −0.0654820 | — | — |
| 3/2 | −0.0432947 | — | — |
| 3 | +0.0344606 | 0 | — |

The p < 1 entries match the check_e3_mu.out printout. The p > 1 values of ε₁ match κ_p in check_e3_sym.out.

**Re-runs.** check_e3_sym.out, check_e3_moments.out (4.7 s) and check_e3_grid.out (3.9 s, from the cache) are identical on
re-run.

**Grid sensitivity (g_*.py).** In these variants, ek is replaced inside a copy of check_e3_grid.py.

| Change | p = 3/4 rows | p = 0.6 rows | p = 1/2 rows |
|---|---|---|---|
| none | diff ≤ 7.4·10⁻⁵ | diff ≤ 3.9·10⁻⁵ | diff ≤ 2.5·10⁻⁶ |
| ε₂ → 0 | **unchanged** | −3.1·10⁻³ (half-range 0.7–1.6·10⁻³) | −4.2·10⁻² |
| ε₂ → 2ε₂ | **unchanged** | +3.1·10⁻³ | +4.2·10⁻² |
| ε₁ → 0 | −1.5 | −6.2 | −12 |

At p = 3/4 the exponent 1 + 2p = 5/2 is not subtracted (`1 + kp < 2.5`). It is fitted freely, so those rows do not test ε₂.

The test of ε₂ is about 2–4 half-ranges at p = 0.6 and about 500 at p = 1/2. ε₃ is never subtracted, so it is never tested.

**Free fits (freefit.py).** With ε₂ and ε₃ left as free fit parameters, the n^{−1−2p} coefficient is not resolved at generic
p: half-ranges are 6.5 at p = 3/4 and 1.4 at p = 0.6. So the grid gives no direct measurement of ε₂ off p = 1/2.

**New p = 1/3 data (p13.py, fit13.py).** I computed Plan 62-style coefficients at p = 1/3 (s = 2, 3; K = 200·1600, n ≤ 1600)
into a scratch cache. This is the Cor E3.3(ii) prediction d₂ − 1/36, which is not tested in the repo.

| s | n⁻² fit (after d₁, ε₁, ε₂) | half-range | d₂ − 1/36 | diff | d₂ alone: diff | free n^{−5/3} fit vs ε₂ = −0.0421269 |
|---|---|---|---|---|---|---|
| 2 | −0.5834434 | 1.3·10⁻² | −0.5833333 | −1.1·10⁻⁴ | −2.8·10⁻² | −0.042189 (half-range 1.4·10⁻³) |
| 3 | −5.2084630 | 2.9·10⁻² | −5.2083333 | −1.3·10⁻⁴ | −2.8·10⁻² | −0.042394 (half-range 5.8·10⁻³) |

The medians agree with d₂ − 1/36 to about 10⁻⁴. The half-ranges, however, are comparable to the 1/36 discrimination, so this
is supportive rather than decisive. At p = 1/3 the free n^{−5/3} fit is a direct measurement of ε₂, and it agrees to
6·10⁻⁵ at s = 2.

## 5. Findings and required fixes

**F1 (MAJOR as a scope and label issue, not an error; E3.md Lemma E3.7, Conj E3.C, Thm E3.2 wording, §9, §10 "Gauge").**
Lemma E3.4(iii) together with the pole orders of Δ₁^{mod} gives Res_{4c}Δ₁^μ in closed form through G(4c) and G′(4c) alone, and
Res₀ = A₀ (§1.5). The consequence is e(μ) = cp·M_μ(4c) **exactly, for all μ and any polynomial tilt**. This is a 10-line
argument plus a 2×2 sympy identity. Consequences:
- **Lemma E3.7** holds with no O(‖μ‖⁴_w) remainder.
- **ε_j = C(2j,j)pc^jζ(−jp) for all j ≤ K** in Thm E3.2. This uses Q_k(4c) = c^{k−1}kC(2k,k)/2 (§4). The ε_j are
  s-independent, so "possibly s" in Thm E3.2 can go.
- **At every p = 1/j (j ≥ 2) the merged n⁻² coefficient is d₂ − p/12.** This is Cor E3.3(ii) for all j, with Prop E3.6
  at K = j.
- **Conj E3.C** is then proved except at p = 1 (outside the framework) and for the HEURISTIC zeta-regularised sum.
- The full A_r(μ) shift is quadratic in M(4c). This matters for any future α_n computation (F6).

*Required fix.*
- Add the gauge-residue proof to §6, either as the proof of Lemma E3.7 or as a new lemma. Keep check_e3_mu as the
  independent cross-check.
- Add a short script asserting the residue identity (gauge.py is a template; it runs in seconds) and its agreement with
  check_e3_mu's dumped A_r(μ).
- Relabel Conj E3.C (all k; the p = 1/j merged values for j ≥ 2) as PROVED-mod-cite with the same inputs as Thm E3.2.
- Update §9 and the Rule A "Gauge" bullet, which already states the key fact ("change only through G(4c), G′(4c)") but does
  not draw the conclusion.

Reviewer A should confirm that Prop E3.6 is stated for general K, which the proof of Thm E3.2 already uses.

**F2 (MINOR; check_e3_mu.py hard-edge block, E3.md §6 "Asserted: … A₀ … μ-independent", §10 "Gauge").** The hard-edge part of
the check has no teeth. Flipping the exponent, dropping the tilt, flipping 𝓡's sign on z = −v², or using M at z = +v² all pass
(§2). The reason is that G(0) commutes with A₀ for every M(0). The same is true of check_e_plt1_sym's "A₀^lin = 0". The branch
−v(4c+v²)^{1/2} is correct (§1.2), but it is verified by hand, not by the script.

*Required fix.* In §6, state that the A₀ assertion is structural (it follows from G(0)A₀ = A₀G(0)) and is not a test of the
hard-edge branch or sign. Optionally, replace the assertion with the identity G(0)A₀G(0)^{−1} = A₀ itself.

**F3 (MINOR; check_e3_mu.py assertions).** The script asserts only the b-functional. With a wrong exponential (expM = 1 + x)
the dumped A_r(μ) is wrong at weighted order 2–3, yet every assertion passes. The error is symmetric off the diagonal, so the
b-functional cannot see it. The truncation orders (O = 7, cubic expM) are generous: O = 4 is the minimum for non-vacuous
assertions, and the cubic term of expM is redundant.

*Required fix.*
- Assert the full A_r(μ) − A_r against the closed form of §1.5 (with M₄ = M_μ(4c) and the weighted-order-3 truncation).
- Replace the "~10 minutes" expectation with the actual run time (46 s).
- *Suggested:* a second pass at O = 4 asserting the same output, as in REVIEW_PlanE2_B F3.

**F4 (MINOR; stale text).**
- check_e3_mu.py line 1 cites "E3.md Lemma E3.5, Theorem E3.3". The computation is Lemma E3.7 and the target is Thm E3.2 /
  Cor E3.4; Lemma E3.5 is the circle-jump lemma, and E3.3 is a corollary.
- The mtrunc docstring ("keep t^<=2", "drop mu1^3, mu1 mu2") contradicts the code, which keeps t^{≤3}.
- The expM comment says "to second order", but the code is third order.
- check_e3_moments.py line 1 cites "E3_pgt1.md Lemma F.1′". The file is E3.md.

*Required fix:* correct these four lines and regenerate the .out files. The printed output does not change.

**F5 (MINOR; E3.md summary "Numerical cross-checks" and §7).** The text reads as though check_e3_grid confirms ε₂ and d₂
across all listed p. In fact:
- the p = 3/4 rows are independent of ε₂ (fitted freely);
- the p = 0.6 rows test ε₂ at only 2–4 fit half-ranges;
- ε₃ is never tested;
- only p = 1/2 tests a merged constant decisively.

*Required fix.* Add one sentence to §7 saying which rows test what. *Suggested:* add p = 1/3 to the grid. My scratch result
(§4) gives n⁻² = d₂ − 1/36 to 1.3·10⁻⁴ (half-range 1–3·10⁻²) and a direct n^{−5/3} measurement of ε₂ to 6·10⁻⁵.

**F6 (INFO; §9 "second-order coefficients of n^pα_n").** The first-order residue shift is Res_{4c} − A_r = M₄c²p[[…]] (§1.5),
which is quadratic in M(4c). The a-functional reads (Q₁)₂₂ and (Q₂)₁₂, not only A₂₁ − A₁₂. So for α_n the n^{−1−2p}
coefficient need not be linear in ζ(−2p). The α-analogue of Lemma E3.7 should be computed, not inferred from the
b-functional.

**F7 (INFO; Rule X; §10 "Independent test of ε₂").** −1/24 was first seen in the grid numerics. The p = 1/2 grid rows are
therefore the origin of the value, not independent evidence for it. The independent evidence is the symbolic computation, the
gauge identity (§1.5) and the quadrature route (§3). Wording suggestion: "the grid anomaly motivated the computation; the
value is derived symbolically without it."

**F8 (INFO).** check_e3_sym.py is correct. A wrong coefficient for P₁ or A_r^{lin} would change the printed cp; I re-derived
cp by hand. Its cross term I·p(a₁₂+a₂₁)(α+1)/2 is consistent with A_r^{lin}. check_e3_moments' numbers are reproduced exactly.

**Not findings (checked, correct):**
- the 𝓡 branches at both edges;
- the arcsine moments;
- Q₂ and Q₃, and Q_k(4c) for all k;
- the inv1 truncation (u⁴ coefficient unused);
- the e₁ extraction;
- the μ_{n,k} ↔ ε_k conversion, including the 2/k factor;
- c(1/j)^j = 1/C(2j,j);
- ε₂(1/2) = −1/24 and ε₃(1/3) = −1/36;
- κ_p values;
- the byte-identical re-runs.

## 6. Log of what I ran (scratchpad venv python; scratchpad `reviewE3B/`)

| Run | Time | Result |
|---|---|---|
| orig.py (copy of check_e3_mu.py) | 46 s | output identical to check_e3_mu.out; ALL ASSERTIONS PASSED |
| 16 variants v_*.py | ≤ 1 min each, run in parallel | §2 table |
| dump.py, d_exp1.py, d_exp2.py | ~1 min each | pickled A_r(μ), B_r(μ), A₀(μ) |
| gauge.py | 2 s | exact residue identity; e(M) − e(0) = cpM(4c) |
| cmp.py (×3) | ~10 s | script = gauge (orig, exp2); exp1 differs by c³μ₁p(μ₁+12cμ₂)[[1,−i],[−i,−1]] |
| num_mu.py at (1/2, 2), (0.6, 3/2), (3/4, 3); K = 48 | ~5 min each | §3 table |
| num_bad.py at (1/2, 2); K = 32 | ~4 min | sabotage detected (0.2–0.9) |
| closed.py | 2 s | §4 closed forms; Szegő integrals for k = 2, 3 |
| check_e3_sym.py, check_e3_moments.py, check_e3_grid.py (`-B`) | 1 s / 4.7 s / 3.9 s | identical to the .out files |
| g_zero2.py, g_dbl2.py, g_zero1.py | 4 s each | §4 sensitivity table |
| freefit.py | 5 s | ε₂, ε₃ not resolvable by free fits at p = 3/4, 0.6 |
| p13.py (scratch cache), fit13.py | 248 s + 174 s; 3 s | §4 p = 1/3 table |

## 7. Summary for the integrator

On the computation:
- Every value in E3.md is correct: e(μ) = cpM(4c), ε₁, ε₂, ε₃, −1/24, −1/36 and κ_p. I confirmed them by re-run, by sabotage
  tests, by an exact all-orders gauge identity and by an independent quadrature route at finite μ.
- **The gauge identity (F1) proves Lemma E3.7 to all orders.** With it, Conj E3.C (ε_k for all k; d₂ − p/12 at every
  p = 1/j, j ≥ 2) follows within the E3 framework. E3.md should adopt the proof and relabel.

F1–F5 are required. F1 is a label and proof upgrade. F2–F5 cover test coverage, stale text and the wording of the numerics.
F6–F8 are INFO.

REVIEWED status also needs reviewer A's verdict on Lemmas E3.5 and F.1′(ii) and Prop E3.6, including its general-K statement.
