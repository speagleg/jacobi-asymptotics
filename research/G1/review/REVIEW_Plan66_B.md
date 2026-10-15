# Rule R review: Plan 66, reviewer B (Route A, exact algebra and constants), E_p1.md

Reviewer: independent second reader B (Rule R). Reviewer A checks Route C (the Riemann–Hilbert part: Lemmas E1.7a/b, E1.7,
Prop E1.8, Thm E1.9 and the existence part of Thm E1.10). I did not review those and accept none of them here.

Branch `plan-66-E-p1`, commit 52e5980 (E_p1.md unchanged at cc8aab8). Targets:
- research/G1/RH/second_order/E_p1.md: §0, Lemmas E1.1, E1.2, E1.3, Prop E1.4, Lemma E1.5, Thm E1.6 with its Remarks, and the
  constants claimed in Thm E1.10 and §3.5 (d₁ = −(s−1)/2, nα_n coefficient −s/2, k₀ = ½ − s, the fold, the pairings and ng_{n−1});
- checks/check_e1_exact.py, check_e1_tc.py and their .out files; checks/check_so_grid.out (p = 1 rows);
- research/G1/RH/CITATIONS.md entries "(WLXZ-v1, Plan 66)" (the part used by Lemma E1.5) and "(Plan 66 reuse)" (DLMF §5.11, 5.5.1).

External source re-read: WLXZ arXiv:1410.3948v1, PDF fetched again from arxiv.org/pdf/1410.3948v1 today (2026-10-15) and
converted with pdftotext -layout; §1, (1.1)–(1.9).

My scratch computations are in the session scratchpad (`review66B/`, not committed). I wrote them before reading
check_e1_exact.py:
- r1_tc_exact.py: TC and x·TC coefficients from **exact rational moments** of the masses v_k (no WLXZ input);
- r2_zeta.py: σ_s coefficients from the exact moments ζ(s + j) by the Chebyshev algorithm in mpmath (500 and 1000 digits);
- r3_lemmas.py: exact-rational tests of Lemmas E1.1 (identity), E1.2 and (in floats) E1.3 on random measures; x²·TC from moments.

## Overall verdict: **ACCEPT WITH FIXES** (Route A and constants only)

I found no mathematical error in Route A. Every constant in my scope was re-derived by hand and confirmed by two independent
computations:
- exact rational arithmetic from the masses (Lemma E1.5, n ≤ 16);
- 500/1000-digit Jacobi coefficients of σ_{3/2}, σ_{5/2} computed from their exact moments ζ(s + j), with no truncation and
  no tail (Thm E1.6: all four ratios → −1/24 to 10–11 digits, d₂ = 5/96 and 53/96 to 12 digits; Thm E1.10 constants at
  s ∈ {1.25, 1.5, 2, 2.5, 3} to ≥ 9 digits).

The fixes are minor: one check script does not test what §6 says it tests (F1), and one citation pointer is wrong (F2).

| Statement | Verdict (B's scope) | Notes |
|---|---|---|
| §0 conventions (chain, E_n, TC, H, targets) | ACCEPT | k^{−3/2} = √(2π)H(k)v_k checked by hand |
| Lemma E1.1 | ACCEPT (F4 INFO) | E_n[x²] = α_n² + b_n² + b_{n+1}² exact on random measures |
| Lemma E1.2 | ACCEPT | formula, recursion and 1 ≤ ερ_n ≤ 1 + ε exact on random measures |
| Lemma E1.3 | ACCEPT | — |
| Prop E1.4 (i)–(iii) | ACCEPT | every error term re-derived (§1.3) |
| Lemma E1.5 (a)–(d) | ACCEPT (F5 INFO) | (a)–(c) reproduced from exact moments, no WLXZ input; (d) by hand + series |
| Thm E1.6 (all ratios, β_N, d₂, k₁, a_n) | ACCEPT | ε = 1/12, r₂ = 1/288; numerically to 10–12 digits |
| Thm E1.6 Remarks (1)–(3) | ACCEPT | Remark (3)'s hypotheses check |
| Thm E1.10 / §3.5 constants (fold, value, pairings, chain) | ACCEPT | algebra re-derived; existence (Thm E1.9) is reviewer A's |
| check_e1_exact | ACCEPT WITH FIXES (F1) | byte-identical re-run; no hard-coded pass flags; does not test E1.6's constants |
| check_e1_tc | ACCEPT (F3 INFO) | byte-identical re-run (2 min 4 s); prints only, no assertions |
| CITATIONS "(WLXZ-v1, Plan 66)" (1.3)–(1.9) | ACCEPT | matches the PDF verbatim |
| CITATIONS "(Plan 66 reuse)": DLMF §5.11, 5.5.1 | ACCEPT WITH FIXES (F2) | 5.5.1 is Γ(z+1) = zΓ(z), not "Binet's function" |

## 1. Independent re-derivations

### 1.1 Lemma E1.1 (comparability; E_n[x²])

- Minimum property: h_n = min over monic π of ∫π²dν, so c₁h_n(ν) ≤ h_n(ν′) ≤ c₂h_n(ν); b_n² = h_n/h_{n−1} gives the factor
  c₂/c₁; g_n = h_n(x·)/h_n(·) gives [c₁/c₂, c₂/c₁]; α_n = g_n + b_n²/g_{n−1} gives (c₂/c₁)². All correct.
- E_n[x²] = ‖xπ_n‖²/h_n with xπ_n = π_{n+1} + α_nπ_n + b_n²π_{n−1}: ‖·‖² = h_{n+1} + α_n²h_n + b_n⁴h_{n−1}, divided by h_n gives
  b_{n+1}² + α_n² + b_n². Exact match on three random rational measures on {1/k : k ≤ 25}, n ≤ 9 (r3).
- The higher-moment bounds via J^j: correct (see F4 for a small-n wording point).

### 1.2 Lemma E1.2 (Christoffel by 1 + εx) and Lemma E1.3

By hand:
- sign π_n(z₀) = (−1)^n for z₀ < 0 < zeros, so ρ_n > 0;
- q_n = (π_{n+1} + ρ_nπ_n)/(x − z₀) is the monic OP of (x − z₀)ν, and h_n((x − z₀)ν) = ρ_nh_n(ν);
- 1 + εx = ε(x − z₀); the three-term recurrence at z₀ gives ρ_n = α_n + 1/ε − b_n²/ρ_{n−1}, ρ₀ = α₀ + 1/ε.

r3 checks h_n((1 + εx)ν) = ερ_nh_n(ν), the recursion for ερ_n, and 1 ≤ ερ_n ≤ 1 + ε **exactly** (Fractions) for three random
measures and random rational ε, n ≤ 9. Lemma E1.3: both inequalities are the minimum property with the other measure's OP;
r3 confirms the sandwich in floats for random f with |f| ≤ 1.

### 1.3 Proposition E1.4 (every error term)

(i) |e^{±f₀} − 1| ≤ e^{C₀}C₀x², so the sandwich gives |Δ′_n| ≤ C max(E^{v′}[x²], E^w[x²]) = O(n⁻²) by Lemma E1.1 (v′, w are
comparable with v with constants (1, 1+ε) and e^{±C₀}). ερ_n − 1 = εα_n − ε²b_n²/(ερ_{n−1}) = εα_n + O(n⁻²), so
log(ερ_n) = εα_n(v) + O(n⁻²). The g-claim is (i) for the pair (xw, xv) minus (i) for (w, v); it uses only the coefficient
bounds of xv, which are in the hypotheses (no bound on x²v is needed). Correct.

(ii) Under (R1), α_n − α_{n−1} = O(n⁻²) and α_n(xv) − α_n(v) = O(n⁻²) (same A), so b and g ratios are 1 + O(n⁻²); h̃ and α
follow. (R1) for xw follows from SECOND Lemma 2.2 (α_n(xν) = g_n(ν) + h̃_{n+1}(ν), b_n(xν)² = h̃_n(ν)g_n(ν)); I checked this
lemma's two identities on TC → x·TC exactly (r1). No circularity: (ii) uses only (i) and (R1) of v, xv.

(iii) The O(n⁻³) bookkeeping:
- e^{±f₀} = 1 ± r₂x² + O(x³) uniformly, so log E^{v′}[e^{f₀}] = r₂E^{v′}[x²] + O(E[x³]) + O(E[x²]²) = r₂E^{v′}[x²] + O(n⁻³), using
  Lemma E1.1's E[x³] ≤ Cn⁻³; same for −log E^w[e^{−f₀}]. Both bounds are r₂(A² + 2B²)/n² + O(n⁻³), because v′ and w satisfy (R1)
  with the A, B of v (by (ii)), and E_n[x²] = α_n² + b_n² + b_{n+1}². The sign of r₂ does not matter (both bounds agree).
  So Δ′_n − Δ′_{n−1} = O(n⁻³).
- ερ_{n−1} = 1 + O(1/n) ⇒ ερ_n = 1 + εα_n − ε²b_n² + O(n⁻³), log(ερ_n) = εα_n − ε²b_n² − ½ε²α_n² + O(n⁻³). Under (R1),
  b_n² − b_{n−1}² = O(n⁻³) and α_n² − α_{n−1}² = O(n⁻³). This gives the b-claim.
- g-claim: the Δ′ terms of the pairs (xw, xv) and (w, v) are both r₂(A² + 2B²)/n² + O(n⁻³) because (R1) has the same A, B for
  v and xv; the −ε²b_n² − ½ε²α_n² terms cancel to O(n⁻³) for the same reason. Correct.

Rule A: if (R1) held with different constants for v and xv, the g-claim would pick up r₂((A_x² + 2B_x²) − (A² + 2B²))/n²;
the hypothesis "same A, B" is therefore necessary as stated, and it holds for TC/x·TC/x²·TC (A = 1, B = ½, Lemma E1.5(d)).

### 1.4 Lemma E1.5: TC, x·TC, x²·TC from exact rational moments (r1, r3; independent of WLXZ)

The moments of TC are rational. With F_j(z) := Σ_k k^{k−1−j}z^k/k! and the tree function T(z) = F₀(z) (T(1/e) = 1,
zT′ = T/(1 − T)), z d/dz F_{j+1} = F_j gives dF_{j+1}/dT = F_j(1 − T)/T, so m_j := Σ_k v_kk^{−j} = F_j(T)|_{T=1} ∈ ℚ
(m₀ = 1, m₁ = ½, m₂ = 5/12, m₃ = 7/18, …; m₂, m₃, m₅, m₁₀ agree with the direct sums to 5·10⁻¹² or better, the limit being
the slow convergence of the direct sums). I ran the exact
Stieltjes procedure on the moment functionals m_j, m_{j+1}, m_{j+2} (Fractions) and computed the chains from π_n(0):
- TC, n ≤ 16: α_n = 1/(2n+1) + 1/(2n+2) (α₀ = ½), b_n² = 1/(2n(2n+1)), g_n = 1/(2n+2), h̃_n = 1/(2n+1) — **exact match**;
- x·TC, n ≤ 16: α_n = 1/(2n+2) + 1/(2n+3), b_n² = 1/((2n+1)(2n+2)), g_n = (2n+5)/((2n+2)(2n+3)),
  h̃_n = n/((n+1)(2n+3)) — **exact match** (so γ′²_{2j+1} and γ′²_{2j} are as stated);
- x²·TC, n ≤ 14: α_n = (4n+7)(2n²+7n+8)/(2(n+1)(n+2)(2n+3)(2n+5)), b_n² = n(2n+5)/(2(n+1)²(2n+3)²) — **exact match**.

Consistency with the quoted WLXZ (1.4): the monic norms are h_n/γ_n² = 2e/(n+1)! at α_W = 1 (γ_n = 1), which gives
β_N = 1/(N+1) directly; and the total mass h₀ = 2e equals 2e·m₀ = 2e·T(1/e). The proof's derivation from (1.6), (1.9)
(β_N = γ_{N−1}/((N+α)γ_N) = N/((N+α)(N+α−1))) is also correct. (d): the series are elementary; I re-did them by hand
(e.g. α_n − α_{n−1} = −1/n² + O(n⁻³); α_n(xTC) − α_n(TC) = 1/(2n+3) − 1/(2n+1) = −1/(2n²) + O(n⁻³)).

### 1.5 Theorem E1.6 (by hand)

*Weights.* √(2π)H(k)v_k = k!e^k/k^{k+1/2} · k^{k−1}e^{−k}/k! = k^{−3/2}. LnΓ(t+1) = LnΓ(t) + ln t (5.5.1) turns log H(t) into
LnΓ(t) − (t − ½)ln t + t − ½ln(2π), the remainder of 5.11.1; with the sum terminated after k = 1 (n = 2 in §5.11(ii)) and
ph t = 0, |log H(t) − 1/(12t)| ≤ |B₄|/(12t³) = 1/(360t³). Numerically max_t 360t³|log H(t) − 1/(12t)| = 1.0 over t ∈ [0.1, 10⁷]
(40 digits). f₀ = log H − log(1 + x/12) = x²/288 + O(x³) (f₀/x² = 0.00102, 0.00318, 0.00344, 0.003469 at k = 1, 10, 100, 1000
→ 1/288 = 0.003472). So ε = 1/12, r₂ = 1/288, K = √(2π), and σ_{5/2} = xσ_{3/2} gives the second pair.

*Constants.* Prop E1.4(iii): log(b² ratio) = (1/12)(−1/n²), log(g ratio) = (1/12)(−1/(2n²)). So b, g ratios are
1 − 1/(24n²); h̃ = b²/g_{n−1}: (1 − 1/(12n²))/(1 − 1/(24n²)) = 1 − 1/(24n²); α = g + h̃ (positive summands, same ratio);
β_{2m}, β_{2m+1} with m² = N²/4 + O(N): 1 − 1/(6N²). 2nb_n(TC) = (1 + 1/(2n))^{−1/2} = 1 − 1/(4n) + 3/(32n²); 3/32 − 1/24 = 5/96.
2nb_n(xTC) = (1 + 1/(2n))^{−1/2}(1 + 1/n)^{−1/2} = 1 − 3/(4n) + (3/32 + 3/8 + 1/8)/n² = 1 − 3/(4n) + 19/(32n²); 19/32 − 1/24 =
53/96. a_n = α_{n−1}: shift costs O(n⁻³). k₀, k₁ of σ = those of the reference: (−1, 0) and (−2, −3). All correct.

### 1.6 Theorem E1.6 numerically, from exact moments (r2; no truncation, no tail)

σ_s has moments ζ(s + j). I computed α_n, b_n² (n ≤ 120) by Gautschi's Chebyshev algorithm in mpmath and the chain from
π_n(0). 350 digits is **not** enough (garbage); 500 and 1000 digits agree to all printed digits (r2_120_500.out vs r2_120_1000.out: every
line is identical except the two fitted values that are zero in exact arithmetic, k₁ ≈ 2.2·10⁻¹⁷ at s = 3/2, which differ in the
8th significant digit, i.e. by ~10⁻²⁵ absolute; a 750-digit run at s = 3/2, 5/2 agrees likewise). Values below: n = 119, and the c₀ of an exact 6-term fit c₀ + c₁/n + … + c₅/n⁵ through n = 114, …, 119 (also through the even
n = 108, …, 118; same to ≥ 9 digits).

| pair | quantity | n²(r − 1) at n = 119 | fitted limit | claim |
|---|---|---|---|---|
| σ_{3/2}/TC | b | −0.041492 | −0.0416666666667 | −1/24 |
| | α | −0.041147 | −0.0416666666666 | −1/24 |
| | g | −0.040975 | −0.0416666666666 | −1/24 |
| | h̃ | −0.041318 | −0.0416666666667 | −1/24 |
| | d₂ = lim n²(2nb_n − 1 + 1/(4n)) | 0.052017 | 0.0520833333333 | 5/96 = 0.0520833333333 |
| σ_{5/2}/xTC | b | −0.041147 | −0.0416666666666 | −1/24 |
| | α | −0.040806 | −0.041666666666 | −1/24 |
| | g | −0.039630 | −0.04166666665 | −1/24 |
| | h̃ | −0.042006 | −0.0416666666673 | −1/24 |
| | d₂ | 0.548755 | 0.552083333333 | 53/96 = 0.552083333333 |

The symmetric chains give k₀ = −1.0, k₁ = 2·10⁻¹⁷ (s = 3/2) and k₀ = −2.0, k₁ = −3.0 (s = 5/2). This is the same theorem tested
by check_e1_tc, but with a different measure construction (exact moments vs. truncated atoms + quadrature tail) and a different
algorithm (Chebyshev vs. RKPW); its n = 1499 values (−0.04165, …) are consistent with my fits.

### 1.7 Theorem E1.10 constants

*Fold (by hand).* With Nβ_N = 1 + (κ₀ + κ₁(−1)^N)/N + O(N⁻²): b_m² = β_{2m−1}β_{2m} = (4m²)^{−1}(1 + 1/(2m))(1 + κ₀/m) + …, so
mb_m = ½(1 + (κ₀ + ½)/(2m)); α_m = β_{2m} + β_{2m+1} = (2m)^{−1}(2 + (2κ₀ − 1)/(2m)), so mα_m = 1 + (κ₀ − ½)/(2m); κ₁ cancels in both.
d₁ = (κ₀ + ½)/2 = −(s−1)/2 ⇔ κ₀ = ½ − s, and then the α coefficient is −s/2. Pairings: (1 − s/(2n))/(1 − (s−1)/(2n)) = 1 − 1/(2n);
times b_{n−1}/b_n = 1 + 1/n gives +1/(2n). ng_{n−1} = nβ_{2n−1} = ½(1 + (1 + κ₀ − κ₁)/(2n)). With κ₁ = −3a: (1 + κ₀ − κ₁)/2 = a.
All correct.

*Data.* r2 (500 digits, n ≤ 120, 6-term fits through n = 114, …, 119; the k's from 6-term fits through even N = 226, …, 236 and odd
N = 227, …, 237):

| s | d₁ | nα_n coef. | e₁ˢ | e₁ | k₀ | k₁ | 1 + k₀ − k₁ (ng_{n−1}) |
|---|---|---|---|---|---|---|---|
| 1.25 | −0.125 | −0.625 | −0.5 | 0.5 | −0.75 | 0.75 | −0.5 |
| 1.5 | −0.25 | −0.75 | −0.5 | 0.5 | −1.0 | 2·10⁻¹⁷ | 0 |
| 2 | −0.5 | −1.0 | −0.5 | 0.5 | −1.5 | −1.5 | 1.0 |
| 2.5 | −0.75 | −1.25 | −0.5 | 0.5 | −2.0 | −3.0 | 2.0 |
| 3 | −1.0 | −1.5 | −0.5 | 0.5 | −2.5 | −4.5 | 3.0 |

These equal −(s−1)/2, −s/2, −½, ½, ½ − s, −3(s − 3/2) and 2s − 3 to all 10 printed digits. check_so_grid.out (p = 1 rows,
s = 1.5, 2, 3, 4) agrees as well: d₁, e₁, e₁ˢ, k₀ to all 9 printed decimals, and k₁ (the GAP value) to ≤ 3·10⁻⁸. The k₁ agreement at s ∉ {3/2, 5/2}
supports the §8 conjecture; it is NUMERICAL and E_p1 labels it so.

## 2. The check scripts

| Script | Re-run | Identical to .out | Tests what E_p1 claims? |
|---|---|---|---|
| check_e1_exact.py | < 10 s | yes (byte-identical) | [0]–[2] yes: β_N is derived symbolically from (1.6), (1.9); the chain of x·TC is checked as rational identities and positivity. [3] yes for (d). **No** for Theorem E1.6's own constants (F1). Nothing is hard-coded as a pass flag. Note that it relies on SECOND Lemma 2.2 for x·TC; r1 confirms this from moments. |
| check_e1_tc.py | 2 min 4 s | yes (byte-identical) | Numerical illustration of E1.6 for b, α, g (not h̃, not β_N); prints only (F3). The [2] bias line confirms the pipeline on TC/x·TC (3·10⁻¹⁰, 3·10⁻¹³ at tend = 10¹⁶), as E_p1 §6 says. Index conventions (b[n−1] = b_n, chain g_m = α_m − b_m²/g_{m−1}) are correct. |

## 3. Rule C

**(WLXZ-v1, Plan 66), (1.3)–(1.9).** I compared the quotes with the PDF text: (1.3), (1.4) with h_n = 2e^α/((n+α)n!), (1.5)
(jumps (k+α)^{k−1}e^{−k}/k! at ±x_k, x_k = (k+α)^{−1/2}, k = 0, 1, 2, …), (1.6) with f₀ = 1, f₁ = αx, (1.8), (1.9) are verbatim.
The hypothesis "α is a positive number" is recorded, and α_W = 1 satisfies it. The orthogonality is Carlitz's theorem as reported
by WLXZ; E_p1 says so (line 182). The fold in Lemma E1.5's proof (atoms 1/j, masses 2e·v_j) is correct. See F5 for a
suggested independent corroboration.

**(Plan 66 reuse): DLMF §5.11.** The quoted §5.11(ii) bound (sec^{2n}(½ph z) times the first neglected term) at ph t = 0 gives
exactly the bound used, with n = 2. Correct. **DLMF 5.5.1**: see F2.

## 4. Findings and required fixes

**F1 (minor; check_e1_exact.py [3], E_p1 §0 line 48–49 and §6 first bullet).** E_p1 says check_e1_exact gives "exact computer
algebra of Lemma E1.5 and of the constants in Theorem E1.6". The script asserts the differences that feed Prop E1.4(iii), but it
computes **none** of Theorem E1.6's own constants. Its last line, "eps * (−1)/2 = −1/24", prints a product of typed numbers
(ε = 1/12 is typed, not derived). Not checked: ε = 1/12 and r₂ = 1/288 from log H; the −1/24 for b, g, h̃, α; β_N ratio
1 − 1/(6N²); d₂ = 5/96 and 53/96. My checks (§1.5, §1.6) confirm all of them, so this is a scope/labelling defect, not an error.

*Required fix (either one):*
- add to [3]: (a) sympy series of loggamma(t+1) + t − (t + ½)log t − ½log(2π) at t = ∞ (or the Bernoulli coefficient
  B₂/2 = 1/12 and B₄/12 = −1/360) and of f₀ = that − log(1 + x/12) at x = 0, asserting ε = 1/12 and r₂ = 1/288;
  (b) asserts that coeff2 of 2n·sqrt(b2_ref)·(1 − 1/(24n²)) is [1, −(s−1)/2, 5/96] for TC and [1, −3/4, 53/96] for x·TC;
  (c) the h̃ and β_N ratio algebra as series identities; then regenerate the .out and update MANIFEST.sha256; or
- reword E_p1 §0 (line 48–49) and §6 (first bullet) to "exact computer algebra of Lemma E1.5 and of the coefficient
  differences used in Theorem E1.6 (Lemma E1.5(d)); the constants ε, r₂, −1/24, 5/96, 53/96 are hand computations (proof of
  Thm E1.6)" and drop the misleading final print line or mark it "(arithmetic display, not a check)".

**F2 (minor, Rule C wording; E_p1 line 186, §9 line 461, CITATIONS "(Plan 66 reuse)").** The text says log H(t) "is Binet's
function j(t) (DLMF 5.5.1)". DLMF 5.5.1 is Γ(z + 1) = zΓ(z) (as quoted in "(DLMF-5.11, Plan 51)"); it does not define Binet's
function. The mathematics is right: 5.5.1 is exactly the step needed to move from LnΓ(t+1) to the LnΓ(t) of 5.11.1.

*Required fix.* E_p1 line 186: replace "is Binet's function j(t) (DLMF 5.5.1)" by "equals LnΓ(t) − (t − ½)ln t + t − ½ln(2π)
by DLMF 5.5.1 (Γ(t+1) = tΓ(t)), i.e. the remainder in 5.11.1 after the leading terms". In §9 and in the CITATIONS entry
"(Plan 66 reuse)", replace "DLMF 5.5.1 (Binet's function form of log H)" by "DLMF 5.5.1 (Γ(t+1) = tΓ(t), to rewrite log H as
the remainder of 5.11.1)".

**F3 (INFO; check_e1_tc.py).** It prints b, α, g only; Theorem E1.6 also claims h̃ and β_N, and the script has no assertions.
That is acceptable for a NUMERICAL illustration (E_p1 does not claim it as a check of h̃), and §1.6 above covers h̃. *Suggested:*
add an h̃ column, or say in §6 "(b, α, g)".

**F4 (INFO; Lemma E1.1, last sentence of the proof).** "the entries of J^j in row n involve only coefficients with indices in
[n − j, n + j], each ≤ C′/n" holds as written for n ≥ 2j (then indices ≥ n/2); for n < 2j the moments are ≤ 1 because the support
is in (0, 1], so the constant C_j absorbs them. *Suggested:* add "(n ≥ 2j; smaller n are absorbed in C_j since x ≤ 1)".

**F5 (INFO; Lemma E1.5 / CITATIONS).** Lemma E1.5 rests on a single secondhand statement (Carlitz's orthogonality as stated by
WLXZ). The moments of TC are rational, m_j = F_j(1) with dF_{j+1}/dT = F_j(1 − T)/T, F₀ = T (tree function, T(1/e) = 1). The
exact Stieltjes procedure on these moments reproduces (a)–(c) for n ≤ 16 (§1.4). *Suggested (optional):* add this as a
corroborating exact check to check_e1_exact (it costs ~7 s), and record it after Lemma E1.5 next to the existing NUMERICAL
corroboration. It does not replace the citation for all n.

**Not findings (checked, correct):**
- k^{−3/2} = √(2π)H(k)v_k; σ_{5/2} = xσ_{3/2}; (w, v) = (σ_{5/2}, xTC) needs (R1) for x²TC, which Lemma E1.5(d) asserts;
- Remark (3) (s = 7/2): x³TC is comparable with σ_{9/2} (H(k) ∈ [1, e^{1/12}]), so the coefficient bounds come from Law P;
  only (i) is used, as stated;
- the table's "ερ_n ∈ [1, 1 + ε]" follows from ν ≤ (1 + εx)ν ≤ (1 + ε)ν on (0, 1] and Lemma E1.1;
- E_p1 §6's quoted check_e1_tc values (n = 1499) and the bias figures match the re-run;
- the "Consistency" paragraph after §3.5: with κ₁ = −3a, ng_{n−1} = ½(1 + a/n), confirmed numerically (last column above).

## 5. Summary for the integrator

Route A (Lemmas E1.1–E1.3, Prop E1.4, Lemma E1.5, Thm E1.6) is correct as written. The constants are confirmed:
- −1/24 for b, α, g, h̃ at (σ_{3/2}, TC) and (σ_{5/2}, x·TC), and 1 − 1/(6N²) for β_N;
- d₂(1, 3/2) = 5/96, d₂(1, 5/2) = 53/96, and k₁ = 0, −3 at these points;
- in Thm E1.10, d₁ = −(s−1)/2, the nα_n coefficient −s/2, e₁ˢ = −½, e₁ = ½ and k₀ = ½ − s.

These were confirmed by hand and by exact-moment computations that share no code or measure construction with the repo checks.

F1 and F2 are required (check scope and citation wording). F3–F5 are INFO. Reviewer B's verdict on Route A does not cover
Thm E1.9 (existence of the 1/N expansion for s ∉ {3/2, 5/2}), on which Thm E1.10 depends for general s; that is reviewer A's.
