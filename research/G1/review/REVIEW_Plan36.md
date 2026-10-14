# Rule R review: Plan 36 (§3.9 Lemma TLw, Theorem T3-log)

Reviewer: independent second reader (Rule R). Worktree `ja-plan36`, branch `plan-36-log`, commit e2f563d.
Scope: research/G1/PROOF.md §3.9 (Definition, polylog bound, Lemma TLw, Theorem T3-log, remarks log1–log3), the status
row T3-log, the §4 bullet, missing-statements and stop-condition edits, the LOG Plan-36 entry, README, the plan doc
`docs/superpowers/plans/2026-10-14-plan-36-log.md` (every Review-focus item), and `checks/check_log_weights.py/.out`.
Read against §3.1 (Sat_p), §3.2 (Lemma FV), §3.3 (Sat_p⁺), §3.4 (Lemma TL, T3-sv), §3.5 (FVa, T3a) and §3.8 (TV, LP,
Theorem L, T3-all).

## Verdict: ACCEPT WITH FIXES

The architecture is correct and, I think, the right one. Truncating Ψ to [n/M₀, n^γ] gives an n-dependent family that
is uniformly sandwiched. The §3.8 proofs are per-n estimates whose constants depend only on the sandwich. The
truncation error is controlled by Sat_p⁺ (head) and Lemma TLw (tail), and polylog losses do not hurt either. I checked
every use of the weight in the §3.8 proofs. The "uniform version" is honest.

There is one **medium** gap (F1). Step 3 applies Lemma FV and Lemma FVa to the path u(t) = vΨ̃_n e^{th_n}. Both lemmas
are stated, and proved by dominated convergence, for **bounded** f. But h_n is unbounded on T = {k > n^γ} whenever Ψ is
unbounded or tends to 0. For Ψ = (log k)^α, h_n(k) = α(log log k − log log⌊n^γ⌋) + o(1) → ±∞. The fix is routine
(K-truncation plus continuity, or an extended FV/FVa), and no conclusion changes. The other findings are low or
cosmetic. After F1 is written in, I expect the labels below to hold. Only the F1 paragraph needs a short re-check.

## Independent checks done

1. **Definition and examples.**
   - Bounded slowly varying Ψ with c ≤ Ψ ≤ C satisfies (i) by definition and (ii) with D(γ) ≤ log(C/c) = G. So
     T3-log ⊇ T3-all. ✓
   - Ψ = (log(k + e))^α. For γ ≥ 1, (n + e)^γ ≥ n^γ + e^γ ≥ n^γ + e (superadditivity of x^γ). So for k ∈ [n, n^γ],
     1 ≤ log(k + e)/log(n + e) ≤ γ, and D(γ) ≤ |α|log γ (the stated |α|log(γ + 1) is true but loose). (i) holds:
     log log(λn + e) − log log(n + e) → 0. ✓
   - Ψ = (log log(k + e^e))^α. log log(n^γ + e^e) ≤ log(γ log(n + e^e)) = log γ + log log(n + e^e), and
     log log(·) ≥ 1. So the ratio is ≤ 1 + log γ, and D(γ) ≤ |α|log(1 + log γ). ✓ (No value is stated in the text;
     F6.)
   - Products: D and δ_n are subadditive under products. ✓
   - exp(√log k): it is slowly varying (√(log n + log λ) − √log n → 0), and at k = ⌊n^γ⌋ the difference is
     (√γ − 1)√log n − o(1) → ∞, so D(γ) = ∞. ✓
   - Remark: (ii) for γ = 2 already implies (ii) for every γ, by the same squaring chain: D(γ) ≤ ⌈log₂γ⌉·D(2).
     "For every γ > 1" is harmless but redundant (F6).
2. **Polylog bound.** n_j = 2^{2^j}. For k ∈ [n_j, n_{j+1}] with j = ⌊log₂log₂k⌋, the telescoping chain gives
   |log Ψ(k) − log Ψ(2)| ≤ (j + 1)D(2) ≤ D(2)(1 + log₂log₂k). The n_j are integers, so every link is a legal
   instance of (ii). Since log₂log₂k = (log log k − log log 2)/log 2, we get β = D(2)/log 2, and C_Ψ absorbs
   constants and k = 1 (log(k + 2) ≥ log 3 > 1). ✓
3. **Lemma TLw vs TL's proof.**
   - TL step 1 (norming set: atom spacing ≤ p·b/T′, Markov, T′ ≥ 8pn²) and step 2 (Chebyshev extrapolation,
     a/b ≤ n^{−2}, e^{√8} ≤ 17) involve only the nodes, deg P ≤ n and n ≥ 2. T′ ≥ 8pn² holds by definition
     (T′ = ⌈8pn²⌉).
   - Step 3: for k ≥ T″ and P(x_k) = 1, 1 ≤ 34|P(x_{j*})| for some j* ∈ [T′, T″]. So ∫P²du ≥ u_{j*}P(x_{j*})² ≥
     min_{[T′,T″]}u/1156. Hence 1/K_{n+1}^u(x_k, x_k) ≥ min u/1156 and ρ_{n+1}^u(k) = u_kK_{n+1}^u(x_k, x_k) ≤
     1156u_k/min_{[T′,T″]}u. Only u_k and the minimum over [T′, T″] enter. ✓
   - Σu < ∞ with x_k ≤ 1 gives all moments, so K is finite. The lemma inherits n ≥ 2 through "T′, T″ as in Lemma TL",
     but should say so (F7).
4. **Step 1.**
   - Ψ̃_n(n) = Ψ(π_n(n))/Ψ(n) = 1, since π_n(n) = n. ✓
   - If π_n(k) ∈ [⌈n/M₀⌉, n], |log Ψ̃_n(k)| ≤ δ_n(M₀). If π_n(k) ∈ [n, ⌊n^γ⌋], it is ≤ D(γ). So |log Ψ̃_n| ≤ D* < ∞
     uniformly in n. The condition "n ≥ n₁ so that ⌈n/M₀⌉ ≤ n ≤ n^γ" holds for every n ≥ 1 (cosmetic). ✓
5. **Step 2: every use of the weight in the §3.8 proofs.** The path is vΨ̃_n^t from v. The tilt is f = log Ψ̃_n = g_n,
   which is bounded by D*, so Lemma TV, FV and FVa apply as stated.
   - *Theorem L.*
     - (1) |g_n| ≤ G in the first and third TV terms and in ‖g_nq_m‖². Here G = D* suffices; 2D* is fine.
     - (2) |g_n| ≤ δ_n(M₁) on Mid = [n/M₀, Mn]. This holds because Ψ̃_n = Ψ/Ψ(n) on [⌈n/M₀⌉, ⌊n^γ⌋] ⊇ Mid once
       Mn ≤ n^γ, i.e. for n ≥ n(M). That is harmless, because the statement is a limsup at fixed M.
     - (3) Head mass η_n via Sat_p⁺. W/w_k ≤ e^{2D*}ζ(s)k^s along the path, the margin M₀ gives e^{−2(n−1)}, and
       η_n → 0 uniformly in the family.
     - (4) μ_m^v(A) → F_p(M) (Lemma LP). This uses only the starting point v of the path, which does not depend on n.
     - Grönwall runs at fixed n, so an n-dependent f is irrelevant. Result:
       limsup_n sup_t μ_m^{(t)}((Mn, ∞)) ≤ e^{4G}F_p(M). Ψ̃_n does not depend on M, so letting M → ∞ afterwards is
       legitimate. ✓
   - *T3-all step 1 (b).* The bound 2δ_n(M₁) + 2Gη_n + G·sup_t(μ_n + μ_{n−1})(A) uses (1)–(3) only. ✓
   - *T3-all step 2 (a), with T3a step 1.*
     - a_n^{(t)} ≤ (M₀/n)^p + head mass, and b_n ≤ ½(a_{n−1} + a_n). Both use only Sat_p⁺ on the sandwich class.
     - Off the head, x_k ≤ (M₀/n)^p.
     - Constant on the head, and constant beyond n^γ: the head is controlled by Sat_p⁺ whatever Ψ̃_n is there.
       Beyond n^γ ⊂ A it is controlled by |g| ≤ G and Theorem L. ✓
   - Nowhere is slow variation of Ψ̃_n itself needed. Only δ_n(M₁) of Ψ at the single index n enters. Items (a)–(d)
     are therefore a complete list. ✓
6. **Step 3: weights.**
   - Φ_t lies between Ψ̃_n and Ψ/Ψ(n). Both are bounded above and below by P_n(k), since
     Ψ(k)/Ψ(n) ≤ C_Ψ²(log(k + 2))^β(log(n + 2))^β and every factor is ≥ 1.
   - |h_n(k)| = |log Ψ(k) − log Ψ(π_n(k))| ≤ 2log C_Ψ + β(log log(k + 2) + log log(n^γ + 2)), which is ≤ ℓ_n. ✓
   - *Head.* W(t) ≤ Σ_jj^{−s}P_n(j) = O((log n)^β) and 1/u_k ≤ k^sP_n(k), so W/u_k ≤ n^{s+o(1)} for k < n. The factor
     ((m+1)/k)^{2(1−p)₊} is ≤ (n+1)². For k < n/M₀ and m ≥ n − 1 ≥ 1, k/m ≤ 2/M₀ and k < m, so Sat_p⁺ applies, and
     μ_m ≤ 1 − ρ_m. Summing over fewer than n values of k gives n^{O(1)}e^{−2(n−1)}, uniformly in t. ✓
   - *Tail.* μ_m ≤ ρ_{m+1} ≤ ρ_{n+1} (m ≤ n, since ρ is monotone in the index). TLw with u = vΦ_t gives
     μ_m(k) ≤ 1156k^{−s}P_n(k)·T″^s·max_{[T′,T″]}P_n.
     - T″ = ⌈⌈8pn²⌉n^{2/p}⌉ ≤ (8p + 1)n^{2+2/p} + 1.
     - So T″ ≤ n^γ for large n when γ > 2 + 2/p, and T″^s = O(n^{s(2+2/p)}). ✓
   - *Sums.* ℓ_n(k) = O(log(k + 2)) on T. Σ_{k>N}k^{−s}(log k)^{β+1} ≍ N^{1−s}(log N)^{β+1}/(s − 1). With N = n^γ
     this gives (log n)^{O(1)}n^{s(2+2/p) − γ(s−1)} (times n^p for a_n). Both → 0 when
     γ(s − 1) > s(2 + 2/p) + p. ✓
     - The extra "+1" in the stated choice is unneeded but harmless.
     - The condition γ > 2 + 2/p follows from the second one (γ > s(2 + 2/p)/(s − 1) = κ) (F7).
   - *FVa bound.* |ȧ_n| ≤ Σ|h||x − a_n|μ_n + b_nΣ|h|(μ_{n−1} + μ_n) ≤ 2Σ|h|(μ_n + μ_{n−1}), using 2|q_{n−1}q_n| ≤
     μ_{n−1} + μ_n and a_n, b_n ≤ 1. The stated 3 is loose but correct. ✓
   - **But** see F1: FV and FVa are invoked with an unbounded tilt.
7. **Numerics rerun.** From jacobi-asymptotics: `.venv/bin/python ../ja-plan36/research/G1/checks/check_log_weights.py`.
   Output is **identical** to the committed .out in all 6 lines.
   - K = 1.2·10⁵ vs 2.4·10⁵ agree to ≤ 1·10⁻⁶ absolute. ✓
   - The ratios α = 1 : −2 : 3 give deviations 1.0 : 2.0 : 3.0 at every n, so "proportional to |α|" ✓.
   - At n = 3200 the values are 1.9, 3.7 and 5.6 (5.7)·10⁻⁵, so "2–6·10⁻⁵" ✓.
   - The successive halving ratios are 2.16–2.25, not 2: the local exponent is about 1.1–1.15. n·dev drifts down
     (α = 1: 0.100 → 0.061), while n·log n·dev is nearly constant (0.46 → 0.49). So "roughly like 1/n" is loose;
     |α|/(n log n) fits better (F3).

## Findings

**F1 (medium; §3.9 T3-log step 3, b_n and a_n bullets).** The tilt h_n is unbounded, so Lemma FV and Lemma FVa are
used outside their hypotheses.
- Lemma FV (§3.2) and Lemma FVa (§3.5) assume f bounded. Their proofs use |∂_t(term)| ≤ m‖f‖_∞·(term), and in FVa,
  absolute convergence "since … g, f are bounded".
- h_n = log Ψ − log Ψ(π_n) is unbounded on T when Ψ → ∞ or Ψ → 0, which is the whole point of the theorem.
- The conclusion is not in danger. Σ_k sup_t u_k(t)|h_n(k)| ≤ Σ_k k^{−s}P_n(k)ℓ_n(k) < ∞, so the dominated
  convergence goes through. But this is not what the cited lemmas say.

*Fix* (either option):
- (a) **K-truncation.** Replace h_n by h_n^{(K)} := h_n·1[k ≤ K]. This is bounded, so FV/FVa apply. Its path weights
  still lie between Ψ̃_n and Ψ/Ψ(n), so every bound in step 3 holds uniformly in K. Then let K → ∞. The weights
  vΨ̃_ne^{h_n^{(K)}} → w_n in ℓ¹, with x_k ≤ 1. So the finitely many moments determining a_n, b_n converge, D_m > 0,
  and a_n, b_n converge.
- (b) **Extended lemmas.** Add one sentence to FV/FVa: they hold for any f with Σ_k sup_{t∈[0,1]}w_k(t)|f_k|^2 < ∞
  (dominated convergence and absolute convergence of the double sums as before). Then check this condition for h_n.

Option (a) is self-contained and needs no edits to REVIEWED sections.

**F2 (low; §3.9 remark log1, parenthetical).** The parenthetical "(k^{−s}k^{ε} is the pure power with s − ε, so
regularly varying weights k^{−s}L(k) with L log-type are covered)" is muddled.
- A regularly varying weight of index −σ is k^{−σ}L(k). It is covered exactly when σ > 1 and L is log-type, i.e. by
  the theorem itself with s = σ.
- A factor k^ε is not log-type (D(γ) = ∞). It must be absorbed into s, which needs s − ε > 1.
- Regularly varying weights with merely slowly varying L (e.g. L = exp(√log k)) are *not* covered.

*Fix:* "Regularly varying weights k^{−σ}L(k) of index −σ < −1 are covered when L is log-type. (A power factor k^ε is
absorbed into s, which needs s − ε > 1; general slowly varying L, e.g. exp(√log k), is open.)"

**F3 (low; §3.9 log3 and LOG Plan-36 "deviations ~ |α|/n").** The data decay slightly faster than 1/n. The halving
ratios are 2.16–2.25, and n·dev falls from 0.100 to 0.061 (α = 1), while n·log n·dev stays at 0.46–0.49.
*Fix:* "decrease slightly faster than 1/n (consistent with ≈ 0.47|α|/(n log n))". Or keep "roughly like 1/n" with
"(local exponent ≈ 1.1–1.15)". No rate is claimed as a theorem, so this is wording only.

**F4 (low; stale pointers).** Two remarks still say that log k is open.
- §3.8 remark L4 says "Unbounded slowly varying Ψ (e.g. log k): G = ∞ and the Grönwall factor is lost". Now log k is
  covered.
- §3.2's localization-reduction bullet (PROOF.md l. 380) says "Unbounded slowly varying Ψ (e.g. log k) would need
  additional quantitative tail control".

*Fix:* append "(log-type Ψ, e.g. (log k)^α: Theorem T3-log, §3.9; open for D(γ) = ∞, e.g. exp(√log k))" to both.
These are pointer edits to REVIEWED sections, which is the established practice. (LOG l. 143, Plan 35's "Open:
unbounded slowly varying Ψ", is a historical entry; leave it.)

**F5 (low; §4 labels/headers).**
- (a) The missing-statements bullet says "Unbounded log-type Ψ … : PROVED (Theorem T3-log)". It should say
  PROVED-mod-cite, matching the status row. (The preceding T3-all sentence has the same shorthand; fix both, or say
  "PROVED-mod-cite" once for the sentence.)
- (b) The stop-condition heading still reads "(Plan 9; updated through Plan 35)" while its body now cites Plan 36.
  Change it to "through Plan 36".

**F6 (cosmetic; §3.9 Definition/examples).**
- (a) (i) points to the §3.8 definition, which is stated for *bounded* Ψ. Say "δ_n(λ) as in §3.8, without the
  boundedness assumption".
- (b) (ii) for γ = 2 implies it for all γ (D(γ) ≤ ⌈log₂γ⌉D(2) by the same chain). Optionally say so, which shows that
  "log-type" is a single condition.
- (c) The bound D(γ) ≤ |α|log γ is sharper than the stated one. Give D(γ) ≤ |α|log(1 + log γ) for
  (log log(k + e^e))^α.

**F7 (cosmetic; §3.9 TLw / T3-log statement of constants).**
- (a) Lemma TLw should state "n ≥ 2" explicitly. It is inherited from TL, where it is needed for a/b ≤ ½ and
  e^{√8}.
- (b) The choice of γ: γ(s − 1) > s(2 + 2/p) + p suffices, and it implies γ > κ > 2 + 2/p. The first condition and the
  "+1" are redundant.
- (c) Step 1's "n ≥ n₁ (so that ⌈n/M₀⌉ ≤ n ≤ n^γ)" holds for all n ≥ 1. The real largeness conditions are Mn ≤ n^γ
  (step 2) and T″ ≤ n^γ (step 3). Say that instead.
- (d) In step 2, G := D* suffices (2D* is harmless).

## Plan doc Review-focus items

| Item | Result |
|---|---|
| Definition (ii), chain argument for the polylog bound, examples' D(γ) | ✓ (checks 1–2); F6 cosmetic |
| Step 1: D* finite, Ψ̃_n(n) = 1, sandwich uniform in n | ✓ (check 4) |
| Step 2: "verbatim" for an n-dependent family; every use of Ψ; (a)–(d) suffice incl. T3a step 1, LP | ✓ honest (check 5) |
| Step 3: Sat_p⁺ with polylog W/u_k; TLw gives min_{[T′,T″]}u; needs T′ ≥ 8pn², n ≥ 2 | ✓ (checks 3, 6); F7(a) |
| Choice of γ; n^γ ≥ T″ eventually | ✓; F7(b) redundancy |
| FV/FVa bounds and the n^p factor | exponents ✓; **F1** (unbounded tilt) |
| Labels; overclaims in remarks | F2 (regularly varying), F3 (rate wording), F4–F5 |

## Recommended labels (after F1 and the minor fixes)

- **Lemma TLw:** PROVED. It is a verbatim reading of the reviewed TL proof.
- **Theorem T3-log:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa (with F1), Sat_p⁺, TLw, L, T3-all).
  Rule R ACCEPT WITH FIXES (review/REVIEW_Plan36.md). REVIEWED once F1 is re-checked. Novelty UNCHECKED: comparison
  results for log-perturbed weights may be classical for other node sets; no literature check was done.
- **log3:** NUMERICAL (reproduced exactly by the reviewer).
- README "in review" → "REVIEWED" after the re-check.

## Re-check (HEAD 99e0487)

**Verdict: ACCEPT.**

- **F1 (resolved).** The new "Cutoff" bullet is correct.
  - For k ≤ K the path factor Φ_t = Ψ̃_n e^{t·h_n} lies between Ψ̃_n and Ψ/Ψ(n). For k > K it equals Ψ̃_n, an endpoint.
    So the P_n bound, Sat_p⁺ (head), TLw (tail) and |h_n^K| ≤ ℓ_n all hold uniformly in K and t.
  - FV and FVa now apply as stated, because h_n^K is bounded.
  - w_n^K(k) ∈ {vΨ̃_n(k), w_n(k)}, so it is dominated by vΨ̃_n + w_n, which is summable, and x_k ≤ 1. Every moment
    therefore converges.
  - b_n² = D_{n+1}D_{n−1}/D_n² and a_n are continuous in the moments of order ≤ 2n + 1, with D_m > 0. The K-uniform
    bounds on |log b_n²(w_n^K) − log b_n²(vΨ̃_n)| and n^p|a_n(w_n^K) − a_n(vΨ̃_n)| pass to the limit K → ∞.
  - Step 4 states the limit. ✓
- **F2 ✓** log1 now says "k^{−σ}L(k), σ > 1, L log-type = the case s = σ; general slowly varying L not covered".
- **F3 ✓** log3 and LOG give halving ratios 2.16–2.25 and n·log n·dev/|α| ≈ 0.46–0.49. These match my rerun.
- **F4 ✓** The L4 and §3.2 (l. 380) pointers now refer to §3.9.
- **F5 ✓** §4 now says PROVED-mod-cite for T3-log, and the stop-condition heading says "through Plan 36". The
  T3-all "PROVED" shorthand in the same sentence is unchanged; that was optional.
- **F6 ✓** (i) drops boundedness; (ii) notes the γ = 2 equivalence; the D bounds are |α|log γ and |α|log(1 + log γ).
- **F7 ✓** TLw states n ≥ 2. γ(s − 1) > s(2 + 2/p) + p is now the only condition. The largeness conditions
  M₁n ≤ n^γ and T″ ≤ n^γ are named. G := 2D* is kept (harmless).

**Remaining (cosmetic, non-blocking).**
- N1. Step 1 still has a leftover "n ≥ n₁" in "(t ∈ [0, 1], n ≥ n₁)" (PROOF.md l. 907). n₁ is no longer defined;
  delete the qualifier.
- N2. The §3.9 heading, the T3-log status row, LOG and README still say "Rule R pending" / "in review". Update them to
  the labels below.

**Final labels.**
- **Lemma TLw:** PROVED.
- **Theorem T3-log:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TLw, L, T3-all).
  Rule R ACCEPT WITH FIXES (review/REVIEW_Plan36.md), fixes applied, re-check ACCEPT — REVIEWED. Novelty UNCHECKED.
- **log3:** NUMERICAL.
