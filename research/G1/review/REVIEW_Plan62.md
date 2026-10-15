# Rule R review: Plan 62 (the 1/n coefficient for pure powers, SECOND.md)

Reviewer: independent second reader (Rule R). Branch `plan-62-second-order`, HEAD d2a3264 (`git diff e57077c..HEAD`).
Targets:
- research/G1/RH/second_order/SECOND.md (all of §§0–6);
- checks/so_coeffs.py, so_fit.py, check_so_{grid,exact_p2,shift,convex,lattice}.py/.out;
- THEOREMS.md §2.10 (new) and §4 item 13 (update);
- research/G1/RH/CITATIONS.md, the "(Plan 62 reuse)" entry.

Internal inputs I re-read: G1 PROOF.md §3.1 (Lemma Sat_p), §3.3 (Lemma Sat_p⁺), §3.16 (Theorem QLP, Corollary QLP-Λ,
hypothesis (RU)), §3.21 (Lemmas CP, CT, CS, CS-r, Theorem SH, Remark SH-1/n); RH_p1.md §0–§1; RH.md §8.3 and Lemma 5.1;
papers/paper2 sec_front.tex Corollary thm:pure, Remarks rem:pure-lommel and rem:pure-zeta, sec_back.tex §sec:tilt;
toolkit `measures/reference.py` (tc_coeffs). External: only the CITATIONS.md entries (DLMF) §5.11, (VA, Paper 2),
(DLMF-Lommel, Paper 2), and (DLMF-10.40, Paper 2), (DLMF-9, Paper 2), (KMVV), (WLXZ-v1). The last four are named
only in the §4 PROOF SKETCH.

## Overall verdict: **ACCEPT WITH FIXES**

All fixes are minor or INFO. I found no mathematical error in any PROVED, PROVED-mod-cite or CONDITIONAL statement.
Every constant asked about checks out: the Theorem 3.2 limit, the Cor 3.6 limit and the TC 1/n coefficient, the
Theorem 3.10 base cases, and Theorem 3.4's ε > ½. The NUMERICAL, CONJECTURE, GAP and HEURISTIC labels are honest. The
word "certified" is not used anywhere.

| Statement | Verdict | Label after fixes |
|---|---|---|
| §1 grid numerics | ACCEPT WITH FIXES (F4) | NUMERICAL |
| Conjecture P62 | ACCEPT | CONJECTURE |
| Lemma 2.1 (symmetric chain) | ACCEPT | PROVED (elementary) |
| Lemma 2.2 (Darboux step, uniqueness remark) | ACCEPT | PROVED (= Lemma CT) |
| Theorem 2.3 (p = 2, s ∈ {2,…,10}) | ACCEPT WITH FIXES (F2, F4d–f) | PROVED-mod-cite + exact computer algebra |
| Prop 3.1 (Christoffel product) | ACCEPT | PROVED (classical; novelty not claimed, F9) |
| Theorem 3.2 (constant ½log(cζ(s)/ζ(s+p))) | ACCEPT | PROVED-mod-cite |
| Cor 3.3 | ACCEPT WITH FIXES (F3, F5) | CONDITIONAL on (E) at s, s+p; otherwise mod-cite (via Thm 3.2) |
| Theorem 3.4 (e₁ˢ = −p/2) | ACCEPT WITH FIXES (F3, F5) | CONDITIONAL on (E_ε), ε > ½, at s, s+p; otherwise mod-cite |
| Prop 3.5 | ACCEPT WITH FIXES (F1) | PROVED (internal Sat_p⁺) |
| Cor 3.6 (i) | ACCEPT WITH FIXES (F1, F6) | PROVED-mod-cite (RH_p1 §1, DLMF 5.11) |
| Cor 3.6 (ii), (iii) | ACCEPT (F3) | CONDITIONAL on (E) (+ mod-cite) |
| Prop 3.7 | ACCEPT | PROVED (elementary) |
| (UΛ), (CVX) and their status paragraphs | ACCEPT WITH FIXES (F4g, F10) | HYPOTHESIS; NUMERICAL support |
| Theorem 3.8 | ACCEPT WITH FIXES (F3) | CONDITIONAL on (UΛ) or (CVX) + mod-cite (QLP-Λ, Law P) |
| Cor 3.9 | ACCEPT (F3; optional strengthening O1) | CONDITIONAL |
| Theorem 3.10 (a)–(c) | ACCEPT | PROVED-mod-cite |
| Theorem 3.10 (d) | ACCEPT WITH FIXES (F3) | CONDITIONAL on (UΛ)/(CVX) |
| §4 (E), g(p): GAP and PROOF SKETCH | ACCEPT | GAP / PROOF SKETCH |
| §4.1 n_eff heuristic | ACCEPT WITH FIXES (F11) | HEURISTIC; NUMERICAL |
| THEOREMS §2.10, §4 item 13 | ACCEPT WITH FIXES (F4a, F8) | — |
| CITATIONS "(Plan 62 reuse)" entry | ACCEPT WITH FIXES (F2) | Rule C satisfied: no new external source |
| Novelty | — | UNCHECKED (F9) |

## 1. Checks performed

**Re-runs.** I re-ran the five check scripts with the repo venv and PYTHONPATH=src:
- check_so_exact_p2.py (10 s);
- check_so_grid.py, check_so_shift.py, check_so_lattice.py and check_so_convex.py (all from the coefficient cache).

All five outputs are byte-identical to the committed .out files. I also did the following:
- **Cache integrity.** I recomputed (p, s) = (1, 2), K = 1.6·10⁵, nmax = 1600 from scratch, bypassing the cache.
  - The max relative difference from the cached b_n and α_n is 5·10⁻³⁶.
  - The fits give d₁ = −0.4999999999, e₁ = +0.4999999997, e₁ˢ = −0.5000000003, each with a fit spread below 10⁻⁸.
- **SECOND §1.1 table vs .out.** I compared the two programmatically. All 24 rows match, every value.
- **p = ½ sequence (§1).** From the cache, n(n^{1/2}b_n/c − 1) + ½ = −8.57, −6.85, −5.21, −3.86, −2.81, −2.03 (×10⁻³)
  at n = 50 … 1600. This is the same for K and 2K and matches the text. The ratio per doubling drifts from 0.80 to 0.72,
  and the text's "≈ 0.72 … up to slower drifts" is fair.
- **Rule A claim on n^{−3/2} terms (Theorem 3.4 bullet).** I fitted the n^{−3/2} coefficient at p = ½ with so_fit:
  - in n^pb_n/c it is −0.0849 for s = 1.5, 2 and 3 (spread ≤ 3·10⁻³);
  - in α_n/(2b_n) it is ≈ 0 (|·| ≤ 10⁻⁴, within the spread).

  The claim is confirmed. INFO: the n^{−1−p} coefficient of n^pb_n/c looks s-independent. This could be recorded as a
  by-product.

**Independent exact verification of Theorem 2.3.** I did not use the script's chain logic for this. I scaled x ↦ x/π²,
so the moments of σ_{2,s} are ζ(s + 2j)/π^{s+2j}·π^s, i.e. rational multiples of π^s (Bernoulli numbers). I ran the
classical Chebyshev algorithm in exact rational arithmetic (`fractions.Fraction`) for n ≤ 13. Results:
- for s = 2, 4, 6, 8, the exact α_k and b_k² coincide with the γ-chain closed forms of check_so_exact_p2.py;
- for s = 10, they coincide with the Darboux step of the s = 8 chain;
- this verifies the base case CH[2] (the Lommel input), including α_0 = 1/15 = ζ(4)/(π²ζ(2)).

The script's own logic is also sound:
- r0 checks γ₁² = α′₀ = γ₁² + γ₂² of the previous chain;
- r1 and r2 are rational identities in m, valid for m ≥ 1, and at m = 0 r2 reduces to r0 because h₀ = 0;
- the expansions in (2) and the k₀/k₁ extraction in (3) (ev = k₀ + k₁, od = k₀ − k₁) are correct;
- the asserts check d₁, e₁ = 1, e₁ˢ = −1, k₀ = −s and k₁ = −2(s − 2).

I checked d₂ = (s² + 6s − 11)/16 by hand against the printed u² coefficients 5, 29, 61, 101, 149 (/16). It is not
asserted in the script (F4e).

**"Chain uniquely determined."** This is sound. If two sequences satisfy γ₁² = α₀, γ_{2m−1}²γ_{2m}² = b_m² and
γ_{2m}² + γ_{2m+1}² = α_m, they agree by induction, as long as the divisor γ_{2m−1}² is non-zero. For the true chain of
xσ_{2,s−2} this divisor is positive (Lemma 2.1). So positivity of the closed form is **not** needed; one only needs it
to be finite at integer m ≥ 0, which holds. The printed "(positivity: … > 0)" is typed, not computed (F4d), but it is
irrelevant to the logic.

**Lommel validation (§1, "3·10⁻¹⁵ at K = 4·10⁴, 2·10⁻¹³ at K = 2·10⁴").** No script or .out backs this up. I
reproduced it with so_coeffs.measure and the binary128 RKPW against Paper 2's exact b_n and α_n (n = 1 … 400):
- K = 2·10⁴: 2.2·10⁻¹³, which matches;
- K = 4·10⁴: 6.6·10⁻¹⁵, not 3·10⁻¹⁵ (F4b).

**Numerical figures in THEOREMS.** Maximum fit half-range / |K − 2K| per column, from check_so_grid.out:

| column | p ≥ 1 | p = ½ |
|---|---|---|
| d₁ | 1.6·10⁻⁸ / 7·10⁻¹⁰ | 1.3·10⁻⁴ / 1·10⁻⁷ (and \|value − conj\| ≤ 1.4·10⁻⁶) |
| e₁ / e₁ˢ | 5.9·10⁻⁹ / 1.6·10⁻⁷ | 2.5·10⁻⁴ / 3.4·10⁻⁴ |
| k₀ | 8.3·10⁻⁷ | 6.6·10⁻⁴ |
| k₁ | 2.5·10⁻⁶ (\|value − conj\| 5.3·10⁻⁸ at p = 2, s = 3/2) | 8.1·10⁻⁴ |

So the THEOREMS §2.10 phrase "errors ≤ 2·10⁻⁸ (p ≥ 1), ≤ 1.4·10⁻⁴ (p = ½)" holds only for d₁ (F4a). SECOND's §4 g(p)
row is correctly scoped to d₁.

## 2. Statement-by-statement re-derivation

**§0 conventions.**
- c(1) = ½, c(2) = π²/16: checked from I_p.
- e₁ = e₁ˢ + p follows from α_{n−1}/α_n = 1 + p/n + O(n^{−1−ε}).
- a − ½ = α_x: checked.
- g_n = γ_{2n+1}², h_n = γ_{2n}²: consistent with Lemma CT (§3.21), where β_n = b_n².
- Lemma CS's hypotheses are n^pα_n → 2c and n^p√β_n → c. Both follow from Paper 2 Corollary thm:pure (n^pb_n → c,
  α_n/(2b_n) → 1). The α-part is needed, so everything that uses Lemma CS is mod-cite (F3).
- Paper 2's "a_n/(2b_n)" is the standard pairing α_n/(2b_n). Its sec_back conjecture states the −p/2 / +p/2 switch the
  same way as SECOND. Consistent.

**Lemma 2.1 / 2.2.**
- Re-derived: even and odd parts, R_{2m+1} = tπ_m^{(1)}(t²), and evaluation at t = 0 giving
  π_{m+1}(0) + γ_{2m+1}²π_m(0) = 0.
- The two-step recurrences give α_m = γ_{2m}² + γ_{2m+1}², b_m² = γ_{2m−1}²γ_{2m}², α′_m = γ_{2m+1}² + γ_{2m+2}² and
  b′_m² = γ_{2m}²γ_{2m+1}².
- The x ↦ x/π² rescaling multiplies α, b and γ² by 1/π², so c(2) becomes 1/16, and γ_N²·4N² is the normalized chain.

Correct.

**Input (Lommel).** Paper 2 states b_n, α_n "(n ≥ 1)". α₀ = π²/15 (scaled: 1/15), not 2π²/5. Likewise
γ_N² = 1/((2N+1)(2N+3)) holds for N ≥ 1 only, with γ₀ = 0, as the script says. SECOND §2 and the CITATIONS entry drop
the range (F2).

**Prop 3.1 / Theorem 3.2.**
- Lemma CT gives (b′_m/b_m)² = g_m/g_{m−1}, and the product telescopes to g_n/g₀ with g₀ = α₀ = ζ(s+p)/ζ(s).
- Hence Σ_{m≤n}log(b′_m/b_m) + (p/2)log n = ½log(n^pg_n) − ½log g₀ → ½log c − ½log(ζ(s+p)/ζ(s)) = ½log(cζ(s)/ζ(s+p)).
- The constant is correct. Numerically, S_n − limit = O(1/n) in check [B] for five (p, s).

The remark on the a priori rate O(n^{−1/2}) is correct: Lemma CS-r gives |G_n − c| = O(√r_n).

**Cor 3.3.**
- Under (E_ε) at s and s + p: log(m^pb_m/c) = d₁/m + O(m^{−1−ε′}). The quadratic term of log(1 + x) contributes O(m⁻²),
  hence ε′, not ε (F5).
- The sum is (Δd₁)log n + O(1). Theorem 3.2 forces Δd₁ + p/2 = 0.
- Then log(n^pg_n) − log c = −Σ_{m>n}O(m^{−1−ε′}) = O(n^{−ε′}), G_n/G_{n−1} = 1 + O(n^{−1−ε′}) and
  n(G_n − G_{n−1}) = O(n^{−ε′}).

Correct. This is the converse direction of Remark SH-1/n's hypothesis.

**Theorem 3.4.**
- α_n = h_n + g_n = b_n²/g_{n−1} + g_n. With X = b_n/g_{n−1} = √(h_n/g_{n−1}),
  α_n/(2b_n) = ½(X + (g_n/g_{n−1})/X).
- g_n/g_{n−1} = 1 − p/n + O(n^{−1−ε′}), by Cor 3.3.
- X = (n^pb_n/c)/(n^pg_{n−1}/c) = 1 + O(n^{−ε′}). The O(n^{−ε′}) comes from G_{n−1}; b_n's own O(1/n) is dominated.
- So α_n/(2b_n) = 1 + (X − 1)²/(2X) − p/(2n) + O(n^{−1−ε′}) = 1 − p/(2n) + O(n^{−2ε′}), since 2ε′ ≤ 1 + ε′.
- The 1/n term is identified iff 2ε′ > 1, i.e. **ε > ½ is exactly what is needed**. The Rule A note that ε = ½ gives
  nothing is honest.
- Repo pairing: b_{n−1}/b_n = 1 + p/n + O(n^{−1−ε′}) under (E). Then (1 − p/(2n))(1 + p/n) gives +p/2.

Correct. "Determined by d₁ alone" is loose wording: the proof uses only the *existence* of d₁ at s and s + p, never its
value (F5).

**Prop 3.5.**
- Envelope: with w(t) = ve^{tf}, (d/dt)log h_n = Σ_kf(k)μ_n^{(t)}(k). The derivative of π_n has degree < n. The moments
  are C¹ in t by dominated termwise differentiation (|f| ≤ C, x_k ≤ 1, Σv < ∞).
- Tail: |f(k)| ≤ CM₀/n for k ≥ n/M₀.
- Head: μ_n(k) = ρ_{n+1}(k) − ρ_n(k) ≤ 1 − ρ_n(k). Sat_p⁺ (§3.3) is stated for arbitrary positive weights with W < ∞
  (only W/w_k enters), for all p > 0 and 1 ≤ k < n.
- g_p⁺ is decreasing on (0, ½) for every p > 0: g_p′ = log(θ/(1−θ)) − p(1/θ − 1) − 1 < 0, and the constant shift for
  p < 1 does not change this. g_p⁺ → ∞ as θ → 0. So M₀ with g_p⁺ ≥ 1 on (0, 1/M₀] exists.
- ((n+1)/k)^{2(1−p)₊} ≤ (n+1)², and W_t/w_k(t) ≤ e^{2C}(Σv)n^A·(1/c₁). The head is O(e^{−n}).
- The sum identity uses h_n = h₀Π_{j≤n}b_j².

Correct, but see F1 on the k = 1 normalization of the lower bound.

**Cor 3.6.**
- Γ(k+1) = √(2π)k^{k+½}e^{−k}H(k) gives v_k = k^{−3/2}/(√(2π)H(k)), i.e. k^{−3/2} = √(2π)H(k)v_k. Checked.
- DLMF 5.11.1 with the §5.11(ii) bound (n = 1, real argument, sec⁰ = 1) gives 0 < log H(k) ≤ 1/(12k) for every k ≥ 1.
  The hypothesis |log(w/v)| ≤ C/k holds with C = 1/12.
- Limit: −½log(Σw/Σv) = −½log(ζ(3/2)/(√(2π)W_TC)). Checked [D] with W_TC = 1 (tree function T(1/e) = 1, correctly
  marked uncited and unused): T_n − limit = 2.6·10⁻⁵ at n = 1600, n(T_n − limit) = 0.041647 → 1/24.
- (ii): nb_n^{TC} = n/√(2n(2n+1)) = ½(1 + 1/(2n))^{−1/2}, so d₁^{TC} = −¼. Under (E), Σ(d₁ + ¼)/j must converge, so
  d₁ = −¼.
- (iii): Cor 3.3 at p = 1 gives −¼ − m/2 = −(1 + 2m)/4 = −(s−1)/2 at s = 3/2 + m.

Correct.

**Prop 3.7.**
- D_n(s) = det(ζ(s + p(i+j))) > 0 is analytic, so h_n is real-analytic.
- The ∂_sπ_n term vanishes by orthogonality.
- ∂_s log h₀ = ζ′/ζ = −L₀. Checked.

Correct.

**(UΛ) status.**
- k ≥ n part: QLP-Λ (§3.16) gives Σ_{k≥n}log(k/n)μ_m(k) ≤ C_ϑ/ϑ for each fixed σ. Checked against the statement.
- k < n part: log y ≤ y^p/p for y ≥ 1, and Σ_kx_kμ_n(k) = α_n, so the bound is (1/p)n^pα_n → 2c/p.
- So |Λ_n(s)| = O(1) for fixed s. Correct.
- "(UΛ) ⇐ (RU)" also needs n^pα_n → 2c uniformly on [s₀, s₁] (the k < n part). That follows from the uniform
  small-norm bounds in (RU), but it should be said; it is a sketch-level implication (F10).

**(CVX).**
- The secant argument is correct: for convex φ = log h_n, φ′(s₀) ≤ secant ≤ φ′(s₁), with φ′ = −L_n = −log n − Λ_n and
  Λ_n = O(1) at the two fixed endpoints.
- Heuristic: log D_n is log-sum-exp, hence convex, with (log D_n)″ = Var_n. (log h_n)″ = Var_{n+1} − Var_n is a
  difference, so convexity of log h_n is a genuine hypothesis. Honestly labelled.
- Numerics: the grid second differences behave like ≈ 1/(2p²n) > 0. Examples: n·dd = 0.4996 at p = 1, 0.125 at p = 2,
  1.996 at p = ½.

**Theorem 3.8 / Cor 3.9.**
- Integration of Prop 3.7 and the convex secant bound: re-derived. The ∫L₀ ds term is −log(ζ(s₁)/ζ(s₀)), as stated.
- Cor 3.9: under (E) at both ends, (Δd₁)log n + O(1) = −(Δs/2)log n + o(log n). Correct.
- Optional strengthening O1: for the p = 1 and p = 2 bullets, (E) at the anchor is not needed. Theorem 3.10(b) or (a)
  plus Theorem 3.8 already give 𝒟_n(s) = −((s−1)/2)log n + o(log n), and (E) at s alone then gives
  d₁(s) = −(s−1)/2. At p = 2, s₀ = 2, (E) holds anyway by Theorem 2.3.

**Theorem 3.10.**
- Identity: 𝒟_n = p log n! + ½(log h_n − log ζ(s)) − n log c. Checked. So does the Hankel form
  log h_n = log ζ(s) − 2p log n! + 2n log c − (s−1)log n + O(1).
- **Base cases give d·log n + O(1), not o(log n):**
  - (a), s = 2: n²b_n/c = 1 − 1/(2n) + 5/(16n²) + O(n⁻³). This is exact from Paper 2's closed form, and I re-derived the
    series by hand. Hence 𝒟_n = −½H_n + O(1) = −½log n + O(1).
  - (b), s = 3/2: 𝒟_n = Σ_{j≤n}log(jb_j^{TC}/c) + Σ_{j≤n}log(b_j/b_j^{TC}) = −½Σlog(1 + 1/(2j)) + (const + O(1/n)) =
    −¼log n + O(1).
- (c): 𝒟_n(s+p) − 𝒟_n(s) = Σlog(b_j(s+p)/b_j(s)) = −(p/2)log n + const + o(1), by Theorem 3.2. The "iff" and the
  shift −p/2 follow.
- Induction: −½ − m (p = 2, s = 2 + 2m) and −¼ − m/2 (p = 1, s = 3/2 + m) both equal −(s−1)/2. Correct.
- (d) is CONDITIONAL, and under (UΛ) it gives only o(log n), which is weaker than the defined notion (F3).

**§4 and §4.1.**
- The GAP and PROOF SKETCH labelling is honest. Nothing is proved from the RH sources, and the CITATIONS entry says so.
- The TC(α) check: γ_N² = N/((N+α)(N+α−1)) (toolkit tc_coeffs) gives γ_N²·N = 1 − (2α−1)/N + O(N⁻²). So k₀ = 1 − 2α,
  k₁ = 0, and by RH.md Lemma 5.1, d₁ = (½ + k₀)/2 = ¾ − α. Checked.
- It equals −p(α_x/2 + j₀ − ½) with α_x = −½, j₀ = α. At α = 1 it reproduces b_n^{TC}. See F11.

## 3. Findings

**F1 (minor; SECOND Prop 3.5 hypothesis, Cor 3.6(i) application).**

*Issue.* Prop 3.5 assumes v_k ≥ k^{−A} "for all k ≥ 1". At k = 1 this reads v₁ ≥ 1 for every A. Cor 3.6 applies it with
v := √(2π)v_k, and v₁ = √(2π)/e ≈ 0.922 < 1. So the hypothesis literally fails at k = 1. The proof needs only a constant.

*Fix.* State the hypothesis as "v_k ≥ c₁k^{−A} for some c₁ > 0, A". Carry 1/c₁ in the head bound
(W_t/w_k(t) ≤ e^{2C}(Σv)n^A/c₁). Alternatively, in Cor 3.6 swap the roles: v := k^{−3/2}, w := √(2π)v_k. The conclusion
is symmetric.

**F2 (minor; SECOND §2 "Input", CITATIONS "(Plan 62 reuse)" entry).**

*Issue.*
- α_n = 2π²/((4n+1)(4n+5)) holds for n ≥ 1 only. Paper 2 says "(n ≥ 1)". α₀ = ζ(4)/ζ(2) = π²/15, whereas the formula
  gives 2π²/5.
- Likewise γ_N² = 1/((2N+1)(2N+3)) holds for N ≥ 1, with γ₀ = 0.

The script has it right; SECOND and CITATIONS drop the range.

*Fix.* Add "(n ≥ 1; α₀ = π²/15)" and "(N ≥ 1, γ₀ = 0)" in both places.

**F3 (minor; labels of Cor 3.3, Thm 3.4, Cor 3.6(ii)–(iii), Thm 3.8, Cor 3.9, Thm 3.10(d), SECOND label table and
THEOREMS §2.10).**

*Issue.*
- These results use Theorem 3.2 or Lemma CS, and so Law P including the α-part (Paper 2 Cor. thm:pure / RH_p, RH₁(r),
  RH_plt1b). Theorem 3.8 and Theorem 3.10(d) also use QLP-Λ, which is PROVED-mod-cite with KMVV and Vanlessen.
  "CONDITIONAL on (E)" alone hides the inherited citations.
- The Theorem 3.10 heading labels all of (a)–(d) PROVED-mod-cite, but (d) is CONDITIONAL. The label table says this; the
  theorem heading does not.
- (d) under (UΛ) gives 𝒟_n = −((s−1)/2)log n + o(log n). That is not a "log-average coefficient" in the sense just
  defined, which requires O(1).

*Fix.*
- Write "CONDITIONAL on (E) [resp. (E_ε), ε > ½; (UΛ)/(CVX)] + PROVED-mod-cite (Law P; QLP-Λ where used)".
- Mark (d) CONDITIONAL in the theorem heading.
- In (d), write "𝒟_n = −((s−1)/2)log n + o(log n) under (UΛ); log-average coefficient −(s−1)/2 under (CVX)".

**F4 (minor; numerics wording and check hygiene).**
- **(a) THEOREMS §2.10, "Grid numerics" row.** "errors ≤ 2·10⁻⁸ (p ≥ 1), ≤ 1.4·10⁻⁴ (p = ½)" holds for d₁ only. For
  e₁ˢ, k₀ and k₁ the fit half-ranges reach 1.6·10⁻⁷, 8.3·10⁻⁷ and 2.5·10⁻⁶ (p ≥ 1), and up to 8.1·10⁻⁴ at p = ½ (table
  in §1). *Fix:* scope the figure to d₁, or give per-quantity maxima.
- **(b) SECOND §1 "Validation".** No script or .out records it (Rule N.3: values must be computed and reproducible).
  The reviewer's reproduction gives 6.6·10⁻¹⁵ at K = 4·10⁴ (2.2·10⁻¹³ at 2·10⁴). *Fix:* add a small check script/.out
  (or a section of check_so_exact_p2 / check_so_shift), and quote its number.
- **(c) SECOND §5, Prop 3.1 bullet.** "discrepancy ≤ 10⁻¹²" is wrong: check [A] reaches 5.7·10⁻¹² (p = 1.5, n = 1599).
  *Fix:* "≤ 6·10⁻¹²".
- **(d) check_so_exact_p2.py, (1).** The "(positivity: numerators/denominators > 0 for m ≥ 1)" text is typed, not
  computed. It is also unnecessary for the uniqueness argument (see §1).
  - *Fix:* delete it from the print.
  - In SECOND's proof of Theorem 2.3, replace "All factors are positive … so by the uniqueness remark" with "the closed
    forms are finite at every integer m ≥ 0, and the true chain has γ_{2m−1}² > 0, so by the uniqueness remark …".
- **(e) check_so_exact_p2.py.** d₂ = (s² + 6s − 11)/16 is claimed in Theorem 2.3 but only printed. *Fix:* add
  `assert sp.expand(B - 1).coeff(u, 2) == sp.Rational(s*s + 6*s - 11, 16)`.
- **(f) check_so_exact_p2.py.** The base chain CH[2] is not checked against the Lommel input. *Fix:* add an assert of
  b_n² = ge(n)·go(n−1), α_n = ge(n) + go(n) against Paper 2's formulas (n ≥ 1), and of α₀ = go(0) = 1/15. The reviewer
  verified this independently by exact Chebyshev from ζ-moments (§1).
- **(g) SECOND §3.3 and the label table: (CVX) numerics.**
  - "exact Hankel determinants" are 300-digit mpmath determinants, not exact.
  - "(CVX) holds" on the grid means that second divided differences on s ∈ {1.5, 2, 3, 4} are positive. That is a
    necessary condition at those points.

  *Fix:* write "300-digit" and "consistent with (CVX) (positive second divided differences at the grid points)".

**F5 (minor; Cor 3.3, Thm 3.4 proofs).**

*Issue.*
- Several remainders are written O(m^{−1−ε}) where only O(m^{−1−ε′}) holds. This happens when ε > 1, because the (E)
  expansions and log(1 + x) produce O(m⁻²). Examples: "log(b_m(s+p)/b_m(s)) = … + O(m^{−1−ε})",
  "g_n/g_{n−1} = 1 − p/n + O(n^{−1−ε})", "b_{n−1}/b_n = 1 + p/n + O(n^{−1−ε})" and "log(n^pg_n) = log c + O(n^{−ε})".
  The conclusions are stated with ε′ and are correct.
- Theorem 3.4: "it is determined by d₁ alone" is misleading. The proof uses only the existence of d₁ at s and s + p,
  not its value.

*Fix.*
- Replace ε by ε′ in those places.
- Reword to "e₁ˢ = −p/2 whatever the values d₁(s), d₁(s + p); only their existence (with ε > ½) is used".

**F6 (minor; Cor 3.6 Remark (c)).**

*Issue.* "… and log b_n² by the *difference* O(1/n²)" is not proved. Prop 3.5 gives only O(1/n) for log h_n, and a
difference of two O(1/n) quantities need not be O(1/n²).

*Fix.* Label the remark HEURISTIC, or drop the O(1/n²) clause.

**F7 (INFO; SECOND §5, Theorem 3.2 bullet).**

*Issue.* "A measure with an atom at 0 would break Lemma CP (P_n(0) ≠ 0 needed)" is incorrect. For infinite support in
[0, ∞), the zeros of P_n lie in the *open* convex hull of the support, so P_n(0) ≠ 0 even with an atom at 0.

*Fix.* Delete the sentence, or replace it with "an atom at 0 changes g₀ = α₀ only through the moments; nothing breaks".

**F8 (minor; THEOREMS.md).**
- §4 item 13 says "§2.10 below", but §2.10 is above §4. *Fix:* "above".
- Item 13: "PROVED: … the Christoffel constraint … and e₁ˢ = −p/2 given existence (CONDITIONAL on (E))" mixes two
  labels in one clause. *Fix:* split into "PROVED(-mod-cite): …" and "CONDITIONAL on (E) (Thm 3.4: (E_ε), ε > ½): …".
- §2.10 row "Cor 3.3, Thm 3.4": the label column says "CONDITIONAL on (E)". *Fix:* "(E); Thm 3.4 (E_ε), ε > ½" (+ F3).

**F9 (INFO; novelty).**

*Issue.* SECOND states no novelty field, and the policy default is UNCHECKED.
- Prop 3.1 is the classical Christoffel / chain-sequence telescoping. Lemma CS is already recorded as KNOWN (Dai–Piao–Qiao
  Prop. 2.1).
- Theorem 3.10's Hankel form at p = 1 should be compared with the Monien/Zagier expansion and with Haynes–Zudilin, as
  Paper 2 Remark rem:pure-zeta reports.

*Fix.* Add "novelty UNCHECKED; Prop 3.1 classical, novelty not claimed; Rule L pointer: Monien, Haynes–Zudilin for
Theorem 3.10's Hankel form".

**F10 (INFO; SECOND §3.3, "Status of (UΛ)").**

*Issue.* "(UΛ) ⇐ (RU)" also needs Law P's α-part (n^pα_n → 2c) uniformly on [s₀, s₁], for the k < n half. (RU) gives
this through uniform small-norm bounds, but the text cites only QLP-Λ's uniformity. Both ingredients are sketch-level,
like Audit U.

*Fix.* Add "(and Law P uniform on [s₀, s₁], also from (RU))" and "(implication at PROOF SKETCH level, as Audit U)".

**F11 (minor; SECOND §4.1 and the label table row "§4.1").**

*Issue.*
- "Exact at p = 1 for TC(α), all α" is exact only for the chain computation d₁(TC(α)) = ¾ − α, from γ_N² of item 11 §7
  / the toolkit.
- The claim that TC(α) masses are ∝ (k+α)^{−3/2}(1 + O(1/k)) has no reference, and the heuristic's applicability rests
  on it.

*Fix.* Cite item 11 §7 / RH_p1 §1 for the TC(α) masses and check the asymptotics. If F1 is fixed, Prop 3.5 would then
make this a PROVED comparison of TC(α) with the shifted lattice at p = 1. Otherwise write "masses: not checked".

**O1 (optional strengthening; Cor 3.9).** For the p = 1 bullet, drop "(E) at 3/2": combine Theorem 3.10(b) with
Theorem 3.8 (see §2).

## 4. Required before REVIEWED

Apply F1–F6, F8 and F11 (text and label edits in SECOND.md, THEOREMS.md and CITATIONS.md, plus the three small script
edits F4d–f and the new validation output F4b). Then regenerate check_so_exact_p2.out and MANIFEST.sha256. F7, F9 and F10
are INFO and recommended. No re-review is needed beyond a diff check of these edits. None of them changes a mathematical
conclusion.
