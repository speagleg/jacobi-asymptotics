# Rule R review: Plan 67, reviewer B (algebra and constants), E_plt1.md

Reviewer: independent second reader B (Rule R). My remit is the explicit computation behind the constants of Theorem E′.1
and Corollary E′.6. Reviewer A checks the analytic estimates separately (Lemma F.1 (i), (ii), (iv), Lemma E′.3's
n-dependence, the small-norm bounds of Prop. E′.5′, the chain remainder). I did not review those estimates and accept none
of them here.

Branch `plan-67-E-plt1`, commits d0f67bb and 2d7f6f4 (diff against a5cce25). Targets:
- research/G1/RH/second_order/E_plt1.md: Thm E′.1 and Cor E′.6 (constants), Lemma F.1(iii) (moment identity), Lemma F.2,
  Lemma E′.5 (Laurent data of Δ₁^{lin}), Prop. E′.5′ (the algebraic part: R_1⁽¹⁾, R_2⁽¹⁾, R⁽¹⁾(0)), §7.1, §7.2, §8, §9
  (numbers only), Remark F.3 (numbers only);
- checks/check_e_plt1_sym.py and .out; the data in check_e_plt1_num.out and check_so_grid.out (p = ½ rows);
- research/G1/RH/CITATIONS.md entry "(DLMF-zeta, Plan 67)".

Internal inputs I re-read: E_pgt1.md §0, Lemma E.3 (Q₀, X, prefactors), Lemma E.4 (local data), Lemma E.5, Prop. E.5′,
§7 (all REVIEWED in Plan 65); SECOND.md §1 and §1.1; REVIEW_Plan62.md (p = ½ fits); REVIEW_Plan65_B.md (format).
External: dlmf.nist.gov/5.2, /25.2, /25.4, fetched by me today (2026-10-15, curl, TeX alttext read).

My scratch work is in the session scratchpad (`review67B/`, not committed). I wrote all of it before reading
check_e_plt1_sym.py:
- m1_moments.py: mpmath, the seam moments m_k from the *unsimplified* complex integrand of Lemma F.1(iii);
- m2_sym.py: sympy re-derivation of Lemma E′.5, the extraction (§7.1) and the chain (§7.2), keeping λ to first order.
  It uses its own truncated-series code. Its only inputs are Q₀, X and Lemma E.4, all REVIEWED in Plan 65;
- rkpw.c, mktail.py, fit.py, chain.py: a from-scratch computation of b_n, α_n, g_n and γ_N² for σ_{p,s}. It uses RKPW
  (Gragg–Harrod, as in Gautschi's OPQ) in long double and __float128, exact atoms k ≤ K, and a Gauss–Jacobi rule for the
  tail Σ_{k>K} (midpoint-corrected integral in t = x^{−p}). No repo code was used.

## Overall verdict: **ACCEPT WITH FIXES** (algebra and constants only)

I re-derived every constant in my scope independently and found **no mathematical error**. Checked:
- the seam moment identity m_k = ζ(−kp)/(kn^{kp});
- Lemma F.2 (D_q²/q = e^{λ𝓡}, including the sign);
- B_r^{lin} = 0, A_r^{lin}, A₀^{lin} = 0, C₀^{lin}, and the λ-part of w⁽¹⁾;
- the λ-parts of the 1/n coefficients of n^pb_n/c, n^pα_n/(2c) and n^pg_{n−1}/c: each is exactly cp, so each gets the
  same shift κ_pn^{−1−p}, which is s-independent and cancels in α_n/(2b_n);
- d₁ = −(s−1)/2 and the cancellation of p in it;
- the unfolding to γ_N², with 2^{1+p}κ_p and no parity part;
- κ_{1/2} = ζ(−½)/√6 and c(½) = 1/√6;
- the limits p → 2 and p = 1.

The from-scratch numerics reproduce κ_p in b_n, α_n, g_{n−1} and γ_N² (both parities) at p = 0.3, 0.5 and 0.7 (§2.3).
check_e_plt1_sym.py re-runs byte-identically, and its assertions test the claims. The DLMF entry matches the live pages.

The fixes below are minor (one provenance error, one scope/label statement) or INFO (rounding, notation).

| Statement | Verdict (B's scope) | Notes |
|---|---|---|
| Lemma F.1(iii): m_k = ζ(−kp)/(kn^{kp}) | ACCEPT | hand re-derivation + mpmath, 50 digits, 45 cases (§1.1) |
| Lemma F.1 consequence λ_n = 2ζ(−p)n^{−p}, H_n ∝ e^{−λ_nz} | ACCEPT | sign bookkeeping −2(𝒢 − 𝒢(1)) re-checked |
| Lemma F.2 D_q²/q = e^{λ𝓡} | ACCEPT | own Plemelj check of (eq. szego-repr) and of 𝓡₊ = i√(x(4c−x)) (§1.2) |
| Lemma E′.5: B_r^{lin} = 0, A_r^{lin}, A₀^{lin} = 0, C₀^{lin} | ACCEPT | independent sympy, exact match; model parts reproduce E_pgt1 Lemma E.5 |
| Prop. E′.5′: R_1⁽¹⁾, R_2⁽¹⁾, R⁽¹⁾(0) with λ_n-parts (algebra) | ACCEPT | linear in the residues; estimates are A's |
| §7.1 / Thm E′.1 constants | ACCEPT | λ-part cp in both b and α; d₁ = −(s−1)/2; e₁ˢ = −p/2; repo pairing +p/2 |
| §7.2 / Cor E′.6 (g, G_m, H_m, γ_N², k₀, k₁) | ACCEPT WITH FIXES (B2) | algebra correct; the γ_N² step is hand algebra, not "computer algebra" |
| κ_p < 0, κ_{1/2}, c(½) | ACCEPT WITH FIXES (B3, INFO) | −0.0848692; text says "−0.084870…" |
| p → 2, p = 1 consistency | ACCEPT | ζ(−2) = 0; −2ζ(−1)z/n = z/(6n) = 1/n term of 2j(n/z) |
| §8, §9 numbers vs check_e_plt1_num.out, check_so_grid.out | ACCEPT WITH FIXES (B1) | all numbers match; the "−0.0849" is attributed to the wrong file |
| Remark F.3 numbers | ACCEPT WITH FIXES (B4, INFO) | 4c(3) = 2.75685, not 2.7570 |
| check_e_plt1_sym.py / .out | ACCEPT WITH FIXES (B2, B6 INFO) | reproduces byte-identically; assertions are genuine |
| CITATIONS "(DLMF-zeta, Plan 67)" | ACCEPT | verbatim match with the live pages; hypothesis checks correct |

## 1. Independent re-derivations

### 1.1 Lemma F.1(iii): the seam moments (by hand + m1_moments.py)

On Γ₊, e^{iθ}(re^{iθ})^{−k−1} = r^{−k−1}e^{−ikθ}, and on Γ₋ the conjugate. So the bracket is −2i sin(kθ)r^{−k−1}, and
m_k = −(sin kθ/π)∫_0^∞ℓ(r)r^{−k−1}dr with θ = πp/2.

Substitute u = 2πnr^{−1/p}. Then ∫ℓ r^{−k−1}dr = p(2πn)^{−kp}∫_0^∞ −log(1−e^{−u})u^{kp−1}du. Expand
−log(1 − e^{−u}) = Σ_m e^{−mu}/m (Tonelli). By DLMF 5.2.1 with Re(kp) > 0 and 25.2.1 at 1 + kp, this is
p(2πn)^{−kp}Γ(kp)ζ(1+kp).

DLMF 25.4.1 at s = 1 + kp gives:
- cos(π(1+kp)/2) = −sin(πkp/2);
- ζ(−kp) = −2(2π)^{−1−kp}sin(πkp/2)Γ(1+kp)ζ(1+kp);
- hence ζ(−kp)/k = −(p/π)(2π)^{−kp}sin(πkp/2)Γ(kp)ζ(1+kp).

This is m_k·n^{kp}. ✓

*Numerical check.* I integrated the unsimplified complex integrand of (iii) directly, at 50 digits, for:
- p ∈ {0.25, 0.3, 0.5, 0.7, 0.9};
- n ∈ {1, 7, 100};
- k ∈ {1, 2, 3}.

The worst relative error against ζ(−kp)/(kn^{kp}) is 2.3·10⁻⁵⁰, and the imaginary parts are 0. Three further points:
- the sign changes at p = 0.7, 0.9 for k = 3 (ζ(−2.1), ζ(−2.7) > 0) are reproduced;
- the Mellin integral equals Γ(a)ζ(1+a) at a = 1.4 and 2.7 to 10⁻⁵⁰;
- 25.4.1 holds at x = 0.3, 0.5, 1.7 to 10⁻⁵¹.

*Consequence.* With 𝒢(z) − 𝒢(1) = m₁(z − 1) + O(n^{−2p}) (reviewer A) and H_n = e^{−2𝒢}, we get
log H_n(z) − log H_n(1) = −2ζ(−p)n^{−p}(z−1) + O(n^{−2p}), i.e. H_n ∝ e^{−λ_nz} with λ_n = 2ζ(−p)n^{−p} < 0. ✓

### 1.2 Lemma F.2 (by hand)

Paper 2's (eq. szego-repr), with 𝔠(x) = −λx, gives log D_q² + λz = (λ𝓡/π)∫_0^{4c}dx/√(x(4c−x)) = λ𝓡. ✓

I also checked the representation and its sign independently:
- 𝓡₊ = i√(x(4c−x)) on (0, 4c), since 𝓡 = (z(z−4c))^{1/2} ~ z;
- Plemelj gives log D₊² + log D₋² = 2 log q;
- D² = e^{−λz+λ𝓡} → e^{−2cλ} at ∞.

So D_q²/q = e^{+λ𝓡}. The E_plt1 §11 bullet on "ωe^{λ𝓡}, not e^{−λ𝓡}" is right.

Constants in the weight cancel in ω = D_W²/W₀. Hence "H_n ∝ e^{−λ_nz} modulo constants" is all the proof needs.

### 1.3 Lemma E′.5 (m2_sym.py, sympy)

Data: P₀^∞ = T diag(𝔞_∞, 𝔞_∞^{−1})T^{−1}, with Q₀, X and Lemma E.4 as in E_pgt1. The perturbation is
(−ω) → (−ω^{mod})e^{λ𝓡}, with 𝓡 = z^{1/2}u near 4c. Near 0 the perturbation is ρ² → (ρ^{mod})²e^{−λ𝓡}, with
𝓡(−v²) = −v(4c+v²)^{1/2}. I re-derived that sign myself: 𝓡 ~ z < 0 on (−∞, 0). Everything is expanded as truncated
series, first order in λ. κ₂ and the second Taylor coefficient F₂ of f are kept free.

Results (all exact):
- *Soft edge.* Only u^{−4} and u^{−2} occur; the odd powers u^{−3}, u^{−1} vanish, λ-terms included.
  - B_r = (5c²p/12)[[1, −i], [−i, −1]], and B_r^{lin} = 0.
  - A_r reproduces E_pgt1 Lemma E.5 after substituting κ₂ = −(7+4/p)/(40c).
  - **A_r^{lin} = c²p[[−(α+1), i(α+2)], [iα, α+1]]**, free of κ₂. ✓
- *Hard edge.* Only v^{−2} and v⁰ occur; v^{−1} and v¹ vanish, λ-terms included.
  - A₀ = (c(p+2)(4α²−1)/16)[[1, i], [i, −1]], and **A₀^{lin} = 0**.
  - **C₀^{lin} = (c(p+2)/4)[[α+1, i(α+2)], [iα, −(α+1)]]**, free of F₂. ✓
  - C₀ reproduces E_pgt1 Lemma E.5 with F₂ = −2τ₁/3.

The structural argument for meromorphy (E_plt1 §5) is also correct algebraically:
- e^{±λ𝓡/2} satisfies the band relations (·)₊(·)₋ = 1 because 𝓡₊ = −𝓡₋ on (0, 4c);
- 𝓡 is analytic on (−δ, 0) and on (4c, 4c+ε);
- J d^{σ₃}J^{−1} = d^{−σ₃}, JXJ^{−1} = −X and JQ₀J^{−1} = −Q₀, which I checked by hand.

### 1.4 Extraction, §7.1 (m2_sym.py)

Setup:
- Q₁ = P₁ + R_1 and Q₂ = P₂ + R_1P₁ + R_2;
- R_1 = ε(A₀ + A_r + LA_r^{lin}) and R_2 = ε(4c(A_r + LA_r^{lin}) + B_r), with ε = 1/n and L = λ_n;
- the functionals are b = (Q₁)₁₂(Q₁)₂₁ and a = (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂.

Coefficients of ε, with α = (s−1−p)/p:
- n^pb_n/c: **Lcp − (s−1)/2**;
- n^pα_n/(2c): **Lcp − (s−1+p)/2**;
- α_n/(2b_n): **−p/2**, L-free.

By hand, for b: A₂₁^{lin} − A₁₂^{lin} = c²p(iα − i(α+2)) = −2ic²p. So the shift in n^{2p}b_n²/c² is
i(−2ic²p)L/(cn) = 2cpL/n, and it halves to cpL/n. ✓

With L = 2ζ(−p)n^{−p}, cpλ_n/n = 2pcζ(−p)n^{−1−p} = κ_pn^{−1−p}. The shift is equal in b and α, and it is α-free,
hence s-free. ✓

*The p-cancellation in d₁.* The L⁰ part is −p(α+1)/2, and p(α+1) = s−1, so d₁ = −(s−1)/2 with no p left. ✓

*Repo pairing.* The κ_p-terms of α_{n−1} and b_n differ by O(n^{−2−p}), so α_{n−1}/(2b_n) = 1 + p/(2n) + O(n^{−1−2p} + n^{−2}). ✓

### 1.5 Chain, §7.2 and Cor E′.6 (m2_sym.py + hand)

Bessel column at 0:
- w⁽⁰⁾ = (1, i)ᵀ/√(p+2), with λ-part 0;
- w⁽¹⁾ = √(p+2)(α(α+2), iα²)ᵀ/4 + λ·**αc√(p+2)/2·(1, i)ᵀ**, as stated in §7.2;
- the v^{−1} coefficients of both limits vanish, so the limits are finite.

With R(0) = I + ε(−C₀ − A_r/(4c) + B_r/(16c²)) (λ-parts included) and (E.6.1):
- **n^pg_{n−1}/c = 1 + ε(α + ½ + Lcp)**;
- the result is free of κ₂ and F₂. ✓

*Unfolding (by hand).* Both expansions follow (constant factor c omitted):
- n^pg_{n−1} = (1 + p/n + O(n⁻²))G_{n−1} gives G_m = 1 + (a−p)/m + κ_pm^{−1−p}.
- H_n = n^{2p}b_n²/(n^pg_{n−1}) = (1 − (s−1)/n + 2κ_pn^{−1−p})/(1 + a/n + κ_pn^{−1−p}) = 1 − (s−1+a)/n + κ_pn^{−1−p}.

In the symmetric variable, m^{−1−p} = 2^{1+p}N^{−1−p} exactly for N = 2m, and (1 + O(1/N)) times that for N = 2m+1. Both
parities therefore carry +2^{1+p}κ_pN^{−1−p}, with no (−1)^N part. The 1/N terms do not involve κ_p, so k₀ and k₁ are
E_pgt1's:
- k₀ + k₁ = −2(s−1+a) and k₀ − k₁ = 2a − p;
- hence k₀ = −(s−1) − p/2 and k₁ = −(p+2)a. ✓

### 1.6 Constants and limits

- **c(½).** I_{1/2} = (√π/2)Γ(5/2)/Γ(3) = 3π/16, so π/(2I) = 8/3. Then c = ¼√(8/3) = 1/√6 = 0.40824829. ✓
- **κ_{1/2}.** κ_{1/2} = 2·½·c·ζ(−½) = ζ(−½)/√6 = −0.20788622/2.44948974 = **−0.0848691960**. ✓
- **Sign.** ζ(−p) < 0 on (0, 1): in 25.4.1 at s = 1+p every factor after the minus sign is positive. Hence κ_p < 0. ✓
- **p → 2.** ζ(−2) = 0. ✓
- **p = 1.** −2ζ(−1)z/n = z/(6n). This is the 1/n term of 2j(n/z) ~ 2·z/(12n). The full series identity of Remark F.3 also
  holds: ζ(−(2m−1)) = −B_{2m}/(2m), and the even k ≥ 2 terms vanish. ✓
- **Remark F.3.** I recomputed the numbers:
  - 4c(3)ζ(−3) = 2.756851/120 = 0.0229738 (data 0.022974);
  - 4c(3/2)|ζ(−3/2)| = 0.0577263.

## 2. Data

### 2.1 check_e_plt1_num.out and the §8 / §9 text

Every number quoted in §8 matches the .out:
- the p = ½ row-(b) diffs are 4.9·10⁻⁹, 3.4·10⁻⁷ and 6.6·10⁻⁶;
- the d₁ bounds are 2.5·10⁻⁷ for p ≥ ½, and 8.3·10⁻⁵ with half-range 4.0·10⁻³ at (0.3, 3);
- the p = 0.7 and p = 0.9 bounds are 3·10⁻⁵ and 1·10⁻⁴;
- the α_n/(2b_n) bounds are 3.5·10⁻⁴ and 10⁻⁴;
- "131/132" holds; the single OUTSIDE row is g's 1/n coefficient at (0.9, 1.5), 5.9·10⁻⁸ against a half-range of 5.4·10⁻⁸,
  as stated.

The ok/OUTSIDE flags are computed from |fit − prediction| ≤ max(half-range, dK, 10⁻⁸) (check_e_plt1_num.py lines
96–114), not typed (Rule N.3).

§9 SECOND sequence: −2.0·10⁻³ at n = 1600. The .out's direct n^{3/2}y at n = 1599 is −0.08112, and −0.08112/40 = −2.03·10⁻³.
REVIEW_Plan62 gives −2.03·10⁻³. ✓

### 2.2 check_so_grid.out, p = ½ rows

| s | d₁ | e₁ | e₁ˢ | k₀ | k₁ |
|---|---|---|---|---|---|
| 1.5 | −0.25 | +0.25 | −0.25 | −0.75 | −1.25 |
| 2 | −0.5 | +0.25 | −0.25 | −1.25 | −3.75 |
| 3 | −1 | +0.25 | −0.25 | −2.25 | −8.75 |
| 4 | −1.5 | +0.25 | −0.25 | −3.25 | −13.75 |

These are exactly −(s−1)/2, p/2, −p/2, −(s−1) − p/2 and −(p+2)a with a = 2s − 5/2. All agree within the half-ranges. ✓

### 2.3 Own from-scratch computation (rkpw.c, fit.py, chain.py)

*Setup.*
- σ_{p,s} with atoms k ≤ K exact and the tail by a Gauss–Jacobi rule of 1200 nodes;
- RKPW for n ≤ 1000;
- K = 2·10⁵ and 4·10⁵ (1·10⁵ and 2·10⁵ at p = ½); the K-difference of b_n is ≤ 1.4·10⁻¹¹ relative at n = 1000;
- long double and __float128 agree to the printed precision.

*Fits.* y_b := n^pb_n/c − 1 + (s−1)/(2n) and y_a := n^pα_n/(2c) − 1 + (s−1+p)/(2n). I fitted them in the exponents
{1+i+jp} ∖ {1}, with J = 4…7 terms and windows from n = 100, 200, 300. Values are medians, with the half-range in
brackets. These are estimates, not bounds (Rule N).

| (p, s) | κ_p (pred.) | b | α | α/(2b) | g_{n−1} | γ_N², N even / odd (pred. 2^{1+p}κ_p) |
|---|---|---|---|---|---|---|
| (0.5, 2) | −0.0848692 | −0.0848691 (5e−6) | −0.0848689 (1e−5) | +6·10⁻⁸ (2e−5) | −0.0848686 (4e−6) | −0.240048 / −0.240044 (−0.240046) |
| (0.7, 3) | −0.0919311 | −0.092006 (5e−4) | −0.091657 (4e−3) | +3·10⁻⁴ (3e−3) | −0.091947 (3e−4) | −0.2958 (4e−2) / −0.2990 (5e−3) (−0.29868) |
| (0.3, 1.5) | −0.0633920 | −0.063389 (2e−4) | −0.063470 (4e−4) | +6·10⁻⁶ (4e−4) | −0.063361 (7e−4) | −0.1555 (8e−3) / −0.1563 (4e−3) (−0.15609) |

The free fits (with n⁻¹ in the basis) give d₁ = −0.499999992 at (0.5, 2), −0.999999578 at (0.7, 3) and −0.2500044 at
(0.3, 1.5). For α they give −0.750000013, −1.350001636 and −0.4000122. All agree with −(s−1)/2 and −(s−1+p)/2.

So, independently of the repo's data pipeline:
- the sign and size of κ_p are confirmed;
- κ_p is the same in b_n, α_n and g_{n−1};
- the n^{−1−p} term is absent in α_n/(2b_n);
- the symmetric chain carries 2^{1+p}κ_p with no parity part.

*Rule X.* The value at p = ½ also matches the −0.0849 that the Plan 62 reviewer fitted before any theory existed
(REVIEW_Plan62.md, "Rule A claim on n^{−3/2} terms").

## 3. check_e_plt1_sym.py

I re-ran it with `PYTHONPATH=src .venv/bin/python check_e_plt1_sym.py` (17 s). The output is **byte-identical** to
check_e_plt1_sym.out. The MANIFEST.sha256 entries of all six check_e_plt1_* files match their current contents.

I read the script. Its assertions compare *computed* quantities with the claimed closed forms:
- odd powers vanish, λ-terms included;
- B_r^{lin} = 0 and A_r^{lin};
- A_r^{mod} against E_pgt1;
- A_r^{lin} is free of κ₂;
- A₀^{lin} = 0, A₀^{mod} and C₀^{mod} against E_pgt1;
- C₀^{lin} is free of F₂;
- the λ-parts cp of b, α and g;
- d₁ and the α 1/n coefficient;
- the g 1/n coefficient α + ½;
- C₀^{lin}.

No pass flag is hard-coded. The truncation orders are sufficient: the u^{−2} coefficient needs N(u) to u¹ with κ₂, and
the v⁰ coefficient needs v-series to v³. Both are covered, and my independent code at higher orders gives the same values.

Two scope remarks (B2, B6 below):
- the final printed sentence about γ_N² is not computed by the script;
- B_r^{mod} is printed but not asserted.

## 4. Rule C: CITATIONS "(DLMF-zeta, Plan 67)"

I fetched dlmf.nist.gov/5.2, /25.2 and /25.4 (curl, 2026-10-15) and read the alttext at the equation anchors:
- 5.2.1 is `\Gamma\left(z\right)=\int_{0}^{\infty}e^{-t}t^{z-1}\,\mathrm{d}t,` with `\Re z>0`;
- 25.2.1 is `\zeta\left(s\right)=\sum_{n=1}^{\infty}\frac{1}{n^{s}}.`, preceded by "When ℜ s > 1,";
- 25.4.1 is `\zeta\left(1-s\right)=2(2\pi)^{-s}\cos\left(\tfrac{1}{2}\pi s\right)\Gamma\left(s\right)\zeta\left(s\right),`, preceded
  by "For s ≠ 0, 1,".

All three match the entry verbatim. The hypothesis checks are correct:
- kp > 0;
- Re(1+kp) > 1;
- 1 + kp ∉ {0, 1};
- for the sign of ζ(−p): ζ(1+p) > 0 from the series, and Γ(1+p) > 0 from the integral.

**ACCEPT.**

## 5. Findings and exact fixes

**B1 (minor, provenance; E_plt1.md lines 28, 374 and 424).** The text attributes "the n^{−3/2} coefficient ≈ −0.0849"
at p = ½ to "the Plan 62 table (SECOND §1.1 …)" (line 28), to "SECOND §1.1 (p = ½) and the remark '−0.0849 at p = ½'"
(line 374), and to "(SECOND §1: n^{−3/2} coefficient −0.0849 at all s)" (line 424). SECOND.md contains no −0.0849. §1 has
only the raw sequence −8.6·10⁻³ … −2.0·10⁻³, and the §1.1 table has no n^{−1−p} column. The value is in
research/G1/review/REVIEW_Plan62.md, bullet "Rule A claim on n^{−3/2} terms": "in n^pb_n/c it is −0.0849 for s = 1.5, 2
and 3".

*Required fix.* In the three places, replace the SECOND attribution with "REVIEW_Plan62.md (Rule R fit of the Plan 62
data, bullet 'Rule A claim on n^{−3/2} terms')". The SECOND §1 sequence may still be cited as the raw data.

**B2 (minor, scope of a label; summary table row Cor E′.6, the Cor E′.6 heading, and check_e_plt1_sym.py [4] last
print).** Cor E′.6 is labelled "+ exact computer algebra". The script ends by printing "(and the symmetric chain gets
2^{1+p}κ_p N^{−1−p}, no parity part)". The script computes n^pg_{n−1} only. The G_m/H_m/γ_N² unfolding is hand algebra,
and check_e_plt1_num.py has no γ_N² row. The algebra is correct (§1.5), and my γ_N² fits confirm it (§2.3).

*Required fix (either one):*
- (a) add a short sympy block to check_e_plt1_sym.py that does the unfolding and asserts the N^{−1−p} coefficient
  2^{1+p}κ_p for both parities, then regenerate the .out and MANIFEST.sha256; or
- (b) reword the print to "(hand computation, E_plt1 §7.2)" and, in the Cor E′.6 label, write "exact computer algebra for
  n^pg_{n−1}; the unfolding to γ_N² by hand (§7.2)".

Optionally add a γ_N² parity row to check_e_plt1_num.

**B3 (INFO, rounding; E_plt1.md line 70).** "κ_{1/2} = … = −0.084870…" should be "−0.0848692…": the value is
−0.08486919596, and the ellipsis suggests truncation. Line 28's "−0.08487" is fine.

**B4 (INFO, rounding; Remark F.3, line 207).** "4c(3)·ζ(−3) = 2.7570/120 = 0.022975" should be "2.7569/120 = 0.022974",
since 4c(3) = 2.756851. The corrected value matches the data 0.022974 exactly. The 4c(3/2)|ζ(−3/2)| = 0.0577 figure is
correct (0.057726).

**B5 (INFO, notation; summary table row Cor E′.6 and §9 Conj. P62 bullet).** "γ_p" is used ("γ_p = κ_p", "γ_p for the
chain") but never defined in Cor E′.6, whose statement uses κ_p. *Suggested:* drop γ_p and write κ_p for g, and
2^{1+p}κ_p for γ_N².

**B6 (INFO; check_e_plt1_sym.py [1]).** The print says "(A_r^mod, B_r^mod reproduce E_pgt1 Lemma E.5: asserted for A_r)".
B_r^{mod} is not asserted. That is harmless, because B_r^{mod} is independent of λ, was REVIEWED in Plan 65, and my
re-derivation gives (5c²p/12)[[1, −i], [−i, −1]]. *Suggested:* add the one-line assertion.

**Not findings (checked, correct):**
- the line 13 table entries for H_m and G_m match §7.2;
- in §7.1, (λ_n²/n = O(n^{−1−2p})) and the O(n^{−2−p}) difference of the κ_p-terms at n−1 and n are both correct;
- the Mechanism paragraph's claim that only A_r among the b/α-relevant residues changes is correct
  (B_r^{lin} = A₀^{lin} = 0, and C₀ enters only the chain);
- Remark (1) of §3: exp(−2Σζ(−kp)x^k/k) is the zeta-regularised ∏_m(1 − x/x_m)², x_m = m^{−p}, as stated;
- the §10 note that at p = 1, λ_n = −1/(6n) is consistent with E_pgt1 §9.

## 6. Summary for the integrator

Reviewer B finds every constant of Theorem E′.1 and Corollary E′.6 correct:
- d₁ = −(s−1)/2;
- the 1/n coefficient of n^pα_n/(2c) is −(s−1+p)/2;
- κ_p = 2pc(p)ζ(−p), the same in b_n, α_n and g_{n−1};
- there is no n^{−1−p} term in α_n/(2b_n);
- the symmetric chain has 2^{1+p}κ_pN^{−1−p} with no parity part;
- k₀ and k₁ are as for p > 1.

These were confirmed by independent symbolic re-derivation and by an independent from-scratch numerical computation.
B1 and B2 are required (provenance and label scope). B3–B6 are INFO.

REVIEWED status also needs reviewer A's verdict on the estimates.
