# Rule R review — Plan 49 (commutator lemma CB; CB ⇒ QL ⇒ law; PROOF.md §3.18)

Reviewer: independent second reader (Rule R). Branch `plan-49-cb`, commit 0a715c2, `git diff master...HEAD`
(PROOF.md §0 row + §3.18, LOG.md, plan doc `docs/superpowers/plans/2026-10-14-plan-49-cb.md`,
`checks/check_cb.py/.out`). Compared against §3.8 (TV), §3.14 (L0, FV⁺, B-cond, QLb), §3.16 on master (QLP, Plan 46),
and branch `plan-48-route2` (§3.17, Route II, in review).

## Verdict

**ACCEPT WITH FIXES.** All fixes are minor: wording, labels, one proof step and one exponent condition. I found no
mathematical error that affects a stated result.

- TV⁺, BF(i)–(iii), RF, DB(a)–(d) and NO are correct as stated.
- FM(i)–(ii) are correct. FM(iii) is true, but the proof as written covers only φ ≤ 2 (F2).
- **Theorem QL-CB is correct.** The moment Grönwall closes with η₀ = L/(32(L+1)C₃), which depends only on (p, s, α, a).
  The constants check. The exponent condition in the Fubini step needs a factor 2 (F3).
- Theorem B-OD follows from DB(d) and QL-CB.
- The text says **no new case of the law**: it is in the Summary, the §0 row and the LOG. The CB-ob obstruction is labelled
  HEURISTIC.
- The main overclaim is "the log M in CB is sharp". That sharpness is proved only in the free model (F1).
- The numerics re-ran in 110 s and match the committed `.out` digit for digit.

## Checks performed

**TV⁺.**
- The moments are C¹ by the M-test, since |f_k|w_k(t)x_k^i ≤ U_k.
- The coefficients of p_m are Hankel-determinant ratios over √(D_mD_{m+1}) > 0, so they are C¹ and C_m < ∞.
- Termwise differentiation is dominated by 3C_mC_jU_k.
- Differentiating ⟨q_m, q_j⟩ = δ_{mj} gives ⟨fq_m, q_j⟩ + ⟨√wṗ_m, q_j⟩ + ⟨q_m, √wṗ_j⟩ = 0.
  - For j < m the last term vanishes because deg ṗ_j ≤ j < m.
  - For j = m the two derivative terms are equal.
  - Hence √wṗ_m = −Σ_{j<m}⟨fq_m, q_j⟩q_j − ½⟨f, μ_m⟩q_m. This uses only finitely many inner products, so fq_m ∈ ℓ² is not
    needed.
- Then μ̇_m(k) = f μ_m − 2q_mK_m(fq_m) − ⟨f, μ_m⟩μ_m, and summing over A gives the formula. OK.

**BF.**
- (i) uses Σ_lK_m(k, l)q_m(l) = 0 and antisymmetry on A × A. Absolute convergence holds since |q_jq_m| ≤ C w. OK.
- (ii): K_{m+1} = K_m + q_mq_mᵀ. The rank-one flux is μ(A^c)⟨f1_A, μ⟩ − μ(A)⟨f1_{A^c}, μ⟩ = Cov_μ(f, 1_A), and the 2K_m flux
  is −2X_A. The signs check. It agrees with TV⁺. OK.
- (iii): with CD in the form K_m(k, l) = b_m[q_m(k)q_{m−1}(l) − q_{m−1}(k)q_m(l)]/(x_k − x_l), I get
  q_mK_mq_m = b_m[μ(k)π₋(l) − π₋(k)μ(l)]/(x_k − x_l) and q_mK_{m+1}q_m = b_{m+1}[π₊(k)μ(l) − μ(k)π₊(l)]/(x_k − x_l).
  The sum is [μ(l)ψ(k) − μ(k)ψ(l)]/(x_k − x_l). The signs are correct.
- Toda check: with f = x and Σψ = 0, the flux is ψ(A). OK.
- See F10 on absolute convergence of the CD form.

**RF.**
- K_m(fq_m) = √w P_m, so X_A = Σ_A w p_mP_m = Σ_A μ_mR_m. OK.
- The zeros of p_m (m ≥ 1) lie in (inf supp, sup supp) = (0, 1), so z₁(m) > 0.
- X_A/μ_m(A) is a convex combination of the values R_m(x_k). R_m is continuous on [0, τ], so these values fill an interval
  and the "range" claim holds. The deep limit is R_m(0).
- The "equivalent up to constants" sentence in *Use* is overstated (F4).

**FM.**
- The coefficients check: ĥ(d) = (−1)^d sin(dφ)/(πd) and F̂(d) = (−1)^d/|d|. The latter follows from
  log|cos(θ/2)| = −log 2 − Σ(−1)^d cos(dθ)/d, which is the series at u = θ + π.
- ĥF̂ = sin(dφ)/(πd²), which gives S = Cl₂(φ)/π.
- Parseval with even real sequences gives Cov = 2S.
- (iii) decomposition: Cl₂ = φ − φlog φ + ∫_0^φ −log(sin(u/2)/(u/2))du, so r ≥ 0. The bound r ≤ φ²/60 follows from
  −log(sin x/x) ≤ x²/5 on (0, π/2]. That inequality is true (max ratio 0.1830 at π/2), but the given proof covers only x ≤ 1
  (F2).
- Model reading:
  - y = 4c cos²(θ/2), so −(ε/p)log(y/4c) = (ε/p)F.
  - A = {y < τ} is the arc with 1 − cos φ = τ/(2c), and log(1/φ) = (p/2)log M + ½log c + O(M^{−p}).
  - X = (ε/p)S and Cov − 2X = 0.
  - The prediction 1/(2 log 2) = 0.721 is correct given ε_n ≈ ϑ_n log 2.
- The proposition header labels the relevance HEURISTIC, but elsewhere the text does not (F1).

**DB.**
- (a) Cauchy–Schwarz per block.
- (b) |E_d| ≤ ‖1_Aq_m‖‖1_Aq_{m−d}‖. By Bessel, Σa_i² = ‖K_m(1_Aq_m)‖² ≤ μ(A) − μ(A)².
- (c) ⟨Pq_m, q_{m−d}⟩ = ⟨p_m, Pp_{m−d}⟩_σ = 0 when D + m − d < m, i.e. d > D. B_i ⊂ {d ≥ 2^i}, so D = 2^i − 1 is right.
  Bessel then applies to (f − P)q_m ∈ ℓ².
- (d) Σ_i min(y, 2^{−i}) ≤ y(1 + log₂(1/y)) + 2y.
- The split y log(1/y) = a y log M + M^{−a}u log(1/u) with u = yM^a, and u log(1/u) ≤ 1/e. OK.

**NO.** I re-derived it line by line.
- With β′(r) = β + (c_β − r/T)/2:
  - c_{β′} = (c_β + r/T)/2;
  - (β′, r) ∈ D;
  - u_{β′} ≤ N(c_β + r/T)/(c_β − r/T);
  - the integrand is ≤ 4κNc_β/(c_β − r/T)²;
  - the integral is ≤ 4κTN·c_β/(c_β − t/T), and 4κT = ½;
  - hence N ≤ a + N/2, which gives N ≤ 2a because N < ∞ (u is continuous on a compact set).
- This is a correct comparison principle for the integral inequality as used:
  - "for every continuous β′" is exactly what step 2 supplies, since the pointwise-in-r bound holds for every β′ ∈ (β, α₂];
  - joint continuity makes r ↦ Y_{β′(r)}(r) continuous.
- Monotonicity in β is not used. Any a ≥ sup_β u_β(0) works (F9).

**Theorem QL-CB** (the core; checked in full).
- *Start.*
  - QLP(c) for fixed σ = s and ϑ′ < ϑ gives Y_β(0) ≤ 1 + α₂C_{ϑ′}/(ϑ′ − α₂) = a₀, with layer cake
    Y_β = 1 + β∫M^{β−1}y_M dM.
  - Only t = 0 and fixed σ are used, so (RU) is not needed. Correct.
  - ϑ′ > α₂ holds because α₂ < min(ϑ, a).
- *Step 1.*
  - The TLw/Potter tail μ_m ≤ C_nk^{−s+η₁} gives uniform convergence of Y_β for β ≤ α₂ < s − 1 − η₁.
  - Continuity in t comes from TV⁺. Joint continuity and boundedness hold for each fixed n.
- *Step 2.*
  - (I): Tonelli identity, L0(i), and log₂u ≤ u^δ/(eδ log 2) give ε_n(1 + 1/(eδ log 2))Y_{β′}. OK.
  - (II): ⟨g, μ⟩(Y_β − 1). The head h_n, bulk δ_n(M₀) and k ≥ n bound gives ω_n + ε_nY_α/(eα log 2). L0(i) holds for
    all k ≥ n, far tail included. OK.
  - (III), I₁: substitution M = 2u, with u ∈ [½, 1] handled by y_u ≤ 1 and log u ≤ 0. I get
    I₁ ≤ 2^β[(1 + log 2)/β + (1 + log 2)(Y_β − 1)/β + (Y_{β′} − 1)/(eδβ′)].
  - (III), I₂: by Tonelli, I₂ = ∫y(M′^β − 1)/(βM′) ≤ (Y_β − 1)/β². I₃ = 1/(a − β).
  - (III), collecting terms: 2βη(I₁ + I₂ + I₃) ≤ η[2^{α₂+1}(1 + log 2) + 2^{α₂+1}/(eδ) + 2/α + 2α₂/(a − α₂)]Y_{β′}
    ≤ ηC₃(1 + 1/δ)Y_{β′}, with C₃ as stated (2^{α₂+1}/e < 2^{α₂+1}(1 + log 2)). OK.
  - Combination: each term has the form c₁ + c₂/δ ≤ (c₁ + c₂)(1 + 1/δ) ≤ (L + 1)(c₁ + c₂)/δ, using δ ≤ L. This gives κ(r). OK.
  - Fubini: see F3.
- *Step 3.*
  - On [0, T*], κ ≤ κ*. Note 1 + 1/(e log 2) = 1.53 ≤ 2.
  - NO gives Y_α ≤ 2a₀/(1 − 8κ*t/L) ≤ 4a₀ when 16κ* ≤ L. The continuity bootstrap then gives T* = 1.
  - η ≤ L/(32(L + 1)C₃) makes the η part ≤ L/2. The ε_n and ω_n part is ≤ L/2 for n ≥ n₁. OK.
- *Quantifier question.* η₀ is an absolute constant depending on (p, s, α, a) (through L, C₃ and ϑ), not on n or Ψ.
  - κ* is computed per n, so a hypothesis with an n-dependent constant η_n works as long as η_n ≤ η₀ for n ≥ n₀.
  - In particular CB(C_Bε_n, a) works for any C_B, since ε_n → 0 (the theorem's last sentence). So for the outline's form of
    CB, the smallness is automatic for large n.
  - The text's statement that "only a small absolute η is needed, not η ∝ ε_n" is correct as a weakening of the hypothesis
    (see F5 on wording).
- *Conclusion.*
  - Markov gives y_M ≤ Y_αM^{−α} ≤ 4a₀M^{−α} for all M ≥ 1 and m ∈ {n − 1, n}, uniformly in t. This is QL-b with C = 4a₀ ≥ 1.
  - Lemma QLb needs only 1 ≤ M ≤ n^{γ−1}, so it gives Λ_n ≤ (1 + log C)/α, i.e. QL.
  - QL implies QL₀ (§3.14), and B-cond (CONDITIONAL on QL₀; PROVED-mod-cite) gives the law. Correctly invoked.
  - The m = n − 1 case is consistent: everything is centred at n, as in §3.14 Bc4(f).

**B-OD.**
- DB(d) gives |X| ≤ C_EC_Fε_n[(3 + a/log 2)(1 + log M)y_M + M^{−a}/(e log 2)].
- y_M ≤ y_{M/2}, and 1/(e log 2) ≤ 3 + a/log 2, so this is CB(η_n, a) with η_n → 0.
- QL-CB applies with a = ϑ and α = ϑ/2 (α < ϑ, a > α). OK.

**Labels / overclaims.**
- "CB itself NOT proved" and "No new case of the law is proved" are present in the Summary, the §0 row and the LOG.
- CB-ob is labelled HEURISTIC/OBSTRUCTION and is scoped "about the routes tried here".
- The deep-range numerics are presented as a test of RF, not of the arcsine-range CB, as REVIEW_Plan45 asked.

**Consistency with Plan 48** (`plan-48-route2`, §3.17).
- Plan 48 claims the law for p > 1 and 1 < s < 1 + 2p for every sequence-form Ψ. It states explicitly that it "does not go
  through QL".
- Plan 49 claims nothing unconditional about the law or QL. The §3.17/§3.18 numbering is compatible.
- There is no conflicting claim. Cross-references are needed at merge time (F8).

**Numerics.**
- `check_cb.py` re-run from the jacobi-asymptotics root: 110 s wall. The output equals the committed `.out` except for a
  stderr RuntimeWarning and a blank line.
- Spot-checked claims:
  - [1] identities agree to 9–10 digits;
  - [2] FM agrees to 10 digits;
  - summary maxima 0.670–0.736 / 0.703–0.718, T ≤ 0.579, DB/|X| ≤ 1.26, OD_E ≤ 1.03, OD_F 0.67–0.68 / 1.26;
  - [5] R_m(0)/(ε log n) 0.626–0.741 / 0.932–1.002;
  - R/R_FM on M ≤ n^{2/p}/4 (my extraction): 0.856–0.929 (p = 2), 0.687–0.881 (p = 1);
  - |T|/(εy(1 + log M)) on the same window: ≤ 0.049 (p = 2), ≤ 0.096 (p = 1).
- Small quoting issues are in F7.

## Findings

**F1 (moderate; overclaim; Summary (2), §0 row "(FM; log M in CB sharp)", LOG "the log M in CB is sharp", Rule A (c), FM
model-reading paragraph "the log M in CB is necessary").**
- Issue: Proposition FM proves the identity in the Toeplitz model only. Its relevance to μ_m^{(t)} is HEURISTIC (the
  proposition header says so, and the plan's Review focus asks for that label). The statements that the factor 1 + log M
  "in CB is sharp" or "necessary" are therefore unproved for the actual measures.
- Fix: write "sharp in the free model (PROVED there; relevance to μ_m^{(t)} HEURISTIC; NUMERICAL agreement, `check_cb.out`
  [3])" everywhere.
- Fix: in the §0 row and the heading, split FM into "FM (i)–(iii) PROVED; model reading HEURISTIC".

**F2 (minor; proof gap; FM proof of (iii)).**
- Issue: the chain sin x/x ≥ 1 − x²/6 and −log(1 − z) ≤ z/(1 − z) gives −log(sin x/x) ≤ x²/5 only when z ≤ 1/6, i.e. x ≤ 1.
  But x = u/2 ranges up to φ/2 < π/2. The inequality is true on (0, π/2]; only the proof is short.
- Fix: −log(sin x/x) = Σ_{k≥1} −log(1 − x²/(k²π²)) has nonnegative Taylor coefficients in x². So −log(sin x/x)/x² is
  nondecreasing on (0, π), and at x = π/2 it equals log(π/2)/(π²/4) = 0.1830 ≤ 1/5.

**F3 (minor; exponent; QL-CB step 1 and Rule A (i)).**
- Issue: step 2's bound |ẏ_M| ≤ C′_nM^{1−s+2η₁} makes the Fubini integrand M^{β−s+2η₁}. This is integrable only if
  β < s − 1 − 2η₁. Step 1 chooses η₁ with only α₂ < s − 1 − η₁. Rule A (i) writes the right condition but does not connect
  it to the choice.
- Fix: in step 1 choose η₁ > 0 with α₂ < s − 1 − 2η₁.

**F4 (minor; overstatement; RF "Use" paragraph).**
- Issue: "CB for all A ⊂ {x < z₁(m)/2} is equivalent (up to constants) to sup_{[0,z₁/2]}|R_m| ≲ ε_n log n" is too strong.
  - CB is a hypothesis on tail sets A_M, and its right side carries 1 + log M, which is unbounded as M → ∞.
  - So CB constrains only tail averages of R_m at nodes, with weight log M. It gives no bound on R_m(0): the tail averages
    converge to R_m(0) while CB's bound diverges.
  - Only one direction holds. sup|R_m| ≲ ε_n log n on [0, z₁/2] implies CB for those A_M, because log M ≳ (2/p)log n − C
    there (z₁ is at the Bessel scale).
- Fix: replace "is equivalent (up to constants) to" by "is implied by". Add that the converse fails, and that
  |R_m(0)| ≲ ε_n log n is a separate, sharper statement that CB does not contain.

**F5 (minor; wording/quantifiers; §0 row, LOG, Remark (3) on QL-CB).**
- Issue 1: the theorem has η₀ = η₀(p, s, α, a), but the §0 row and the LOG write η₀(p, s, α).
- Issue 2: Remark (3) calls CB with a constant ≤ η₀ "the precise sufficient condition". It is *a* sufficient condition; no
  necessity is shown (Rule A (d) correctly says so).
- Fix: write η₀(p, s, α, a); "a sufficient condition".
- Fix: add one sentence noting that the outline's CB(C_Bε_n, a) meets the smallness automatically for n large.

**F6 (minor; label inheritance; §0 row, heading, Theorem QL-CB label).**
- Issue: "PROVED-mod-cite (QLP at t = 0, §3.16; B-cond chain)" hides the external citations. The proof inherits them:
  - through QLP: RH_px, RH₁(r), RH_plt1b; KMVV (6.23); Vanlessen (4.27); DLMF via Lemma BK;
  - through B-cond: RH_px, RH₁(r), RH_plt1b.
- Also, §3.16 is not on this branch.
- Fix: list the inherited citations, as the B-cond row does. After merging master, check that every §3.16 reference
  resolves (QLP(c) for fixed σ, all M ≥ 1, n ≥ n₀, m ∈ {n − 1, n}: verified against master), and that §3.18 sits after
  §3.17 if Plan 48 merges first.

**F7 (minor; numerics quoting; CB-ob third bullet, numerics list [4], [6]).**
- R/R_FM window: CB-ob says "R/R_FM = 0.86–1.03, p = 2". That is the range over M ≤ n^{2/p}. Everywhere else 0.86–0.93
  refers to M ≤ n^{2/p}/4. Fix: state the window.
- C_F (p = 2): the printed values are 0.67–0.68 (0.68 at n = 50). Fix: "≤ 0.68".
- [6], p = 1: the printed values are 1.0013 and 1.0083, against "≤ 1.001, ≤ 1.008". Fix: "≤ 1.002, ≤ 1.009".
- All numerics use m = n only. Fix: say so.
- `check_cb.py` line 149 emits a 0/0 RuntimeWarning when cos φ rounds to 1 (the row prints nan). Optional fix: guard it.

**F8 (minor; cross-reference with Plan 48; Summary (5), Remark CB-ob last bullet, "Ψ₁ of RedA" in CB-ob first bullet).**
- No conflict.
- Issue: if Plan 48 is accepted, the law is already established (PROVED-mod-cite) for p > 1, 1 < s < 1 + 2p and every
  sequence-form Ψ, including D(γ) = ∞.
  - The sentences "the loop closes only when ε_n log n = O(1) … (already covered by T3-log)" and "Route-II information
    would close it" should then point to §3.17.
  - The prospective new content of QL-CB/B-OD is then (i) the regimes p ≤ 1 and s ≥ 1 + 2p, and (ii) QL itself along the
    path, which Plan 48 does not give.
  - "Ψ₁ of RedA" refers to the outline on this branch; after merge it is Plan 48's Lemma RedA (PROVED).
- Fix: add these cross-references at merge time. Keep "no new case of the law" (still true for Plan 49 itself).

**F9 (minor; attribution and statement of NO).**
- Issue 1: the name Nishida–Ovsyannikov is attribution only. No source is quoted, which is fine since the proof is
  self-contained (Rule 4 applies only to cited theorems).
- Issue 2: "a := sup_βu_β(0)" sits awkwardly with the application, which uses the upper bound a₀.
- Fix: write "attribution only; proof self-contained; novelty not claimed".
- Fix: state NO for any a ≥ 0 with the inequality (u_β(0) ≤ a is implied). Note that monotonicity in β is not used.

**F10 (minor; BF(iii) convergence and small-m conventions).**
- Issue 1: the CD form is a termwise rewriting of the (ii) summand, so its double sum converges absolutely as a whole.
  Splitting it into Σμ(l)ψ(k)/(x_k − x_l) and Σμ(k)ψ(l)/(x_k − x_l) is not justified, because 1/(x_k − x_l) is unbounded at
  the accumulation point. The text does not split, but the *Reading* paragraph's "absolute-value bound of (iii)" implicitly
  does.
- Issue 2: no conventions are stated for m = 0 (q_{−1} := 0, K_0 := 0) or for RF and z₁ with m ≥ 1.
- Fix: one sentence covering both.

## Recommended labels (after fixes)

- TV⁺: PROVED (standard extension; novelty not claimed).
- BF, RF, DB, NO: PROVED (NO: attribution only, novelty not claimed).
- FM: (i)–(iii) PROVED; model reading and "sharpness of log M for μ_m^{(t)}" HEURISTIC, with NUMERICAL support.
- Theorem QL-CB: CONDITIONAL (CB(η, a), η ≤ η₀(p, s, α, a)) + PROVED-mod-cite (inherits QLP §3.16: RH_px, RH₁(r),
  RH_plt1b, KMVV, Vanlessen, DLMF; B-cond: RH_px, RH₁(r), RH_plt1b).
- Theorem B-OD: CONDITIONAL (OD-E, OD-F).
- Remark CB-ob: HEURISTIC/OBSTRUCTION (scoped to the routes tried).
- Numerics: NUMERICAL.
- Overall: no new case of the law. Novelty UNCHECKED.
- After F1–F10 are applied: Rule R ACCEPT WITH FIXES (review/REVIEW_Plan49.md) — REVIEWED.
