# Rule R review: Plan 35 (§3.8 Lemma TV, Lemma LP, Theorem L, Theorem T3-all)

Reviewer: independent second reader (Rule R). Worktree `ja-plan35`, branch `plan-35-loc`, commit a73950f.
Scope: research/G1/PROOF.md §3.8, the status rows TV/LP/Thm L/T3-all, the pointer edits in §3.2 (localization
reduction), §3.3 T3c2, §3.4 TL1/TL2, §3.7 avg1 and §4, the LOG Plan-35 entry, README, the plan doc
`docs/superpowers/plans/2026-10-14-plan-35-mnloc.md` (every Review-focus item), and `checks/check_mn_loc.py/.out`.

## Verdict: ACCEPT WITH FIXES

The architecture is correct. Lemma TV is right. The Grönwall transport in Theorem L is right line by line. Lemma LP is
right, apart from presentation. The reduction to T3-all is right. There is one **major** error. Theorem L and T3-all
use a fixed head H = {k < n/4} and call its mass "exponentially small (Sat_p⁺)". That is not proved for
p ≲ 1.28, and it is **false** for p ≲ 0.207: there the pure power puts macroscopic mass on k < n/4. The fix is local
and does not change any conclusion: take the head margin M₀(p) of T3-sv (F1). After F1 and the minor fixes, I expect
the labels below to hold. A short re-check of F1 is needed before REVIEWED.

## Independent checks done

1. **Lemma TV re-derived.** q_m = √w·p_m, so q̇_m = ½fq_m + √w·ṗ_m, with deg ṗ_m ≤ m. Differentiating
   ⟨q_m, q_j⟩ = 0 (j < m), using ⟨q_m, q̇_j⟩ = ½⟨fq_m, q_j⟩, gives ⟨r, q_j⟩ = −⟨fq_m, q_j⟩. Differentiating the
   normalization gives ⟨r, q_m⟩ = −½⟨fq_m, q_m⟩. Hence q̇_m = ½fq_m − K_m(fq_m) − ½⟨fq_m, q_m⟩q_m, and
   2⟨1_Aq_m, q̇_m⟩ is the stated formula.
   - **ℓ² smoothness.** t ↦ e^{tf/2} is analytic in operator norm on ℓ² (f bounded). The Gram matrix of finitely many
     vectors is smooth with positive determinant, so Gram–Schmidt is smooth.
   - **Invariance.** f ↦ f + c changes the three terms by cμ_m(A), 0 (because K_mq_m = 0) and −cμ_m(A). ✓
   - Numerically, [1] matches the finite difference to a relative error of 1·10⁻⁸. ✓
2. **Theorem L, line by line.**
   - The first and third terms are each ≤ G·y. The second is ≤ 2√y·‖g_nq_m‖, and
     ‖g_nq_m‖² ≤ δ²μ(Mid) + G²μ(H) + G²y.
   - So ẏ ≤ 4Gy + 2ε_n√y. With z = √(y + κ), y ≤ z² and √y ≤ z give ż ≤ 2Gz + ε_n. Then
     z(t) ≤ e^{2Gt}z(0) + ε_n(e^{2Gt} − 1)/(2G) ≤ e^{2Gt}(z(0) + ε_nt). ✓
   - **Mid.** Mid ⊂ [n/4, Mn] ⊂ [n/M, Mn] for M ≥ 4, so |g_n| ≤ δ_n(M) on Mid. The same set serves m = n and
     m = n − 1. ✓
   - **No circularity.** The only input at t = 0 is μ^v (Lemma LP), and the ODE bound is closed in y. ✓
   - The head bound is **not** ✓; see F1.
3. **Head mass, independently.**
   - *c(p), u_s and g_p⁺(1/4).* I computed c(p) = ¼(π/(2I(p)))^p (G2 §1), u_s(p) = (4c(p))^{−1/p} and g_p⁺(1/4).
     - g_p⁺(1/4) < 0 for p < 1.2767 (for example g_1(1/4) = −0.176), so Sat_p⁺ gives nothing on H there.
     - u_s(p) < 1/4 for p < 0.2067 (for example u_s(0.1) = 0.176).
   - *Consequence via Lemma LP itself.* For p = 0.1, ν_n has a weak limit, so μ_n^v({k < n/4}) → (2/π)arccos√(4^p/(4c(p))) = 0.119 ≠ 0.
   - *Numerical confirmation* (same Lanczos as the check script, p = 0.1, s = 2, K = 4·10⁵).
     - μ_n(k < n/4) = 0.023, 0.067, 0.082 at n = 40, 80, 120, rising toward 0.119.
     - The p = 1 control gives 0.0000.
4. **Lemma LP.**
   - *Conventions.* a_n = ⟨xq_n, q_n⟩ = J_{nn} and b_n = ⟨xq_{n−1}, q_n⟩, so J_{n,n+1} = b_{n+1}.
   - *Moments.* ⟨x^jq_n, q_n⟩ = (J^j)_{nn} is purely algebraic (three-term recurrence), and only entries within
     distance j/2 of n enter. ✓
   - *Pure-power inputs.* The b- and a-laws hold for σ_{p,s} = Σk^{−s}δ_{k^{−p}}, all p > 0, s > 1:
     - RH_px: n^pb_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n), for p > 1;
     - RH₁(r) (`RH/RH_p1_general.md` l. 28): nb_n = c(1)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n), for p = 1;
     - RH_plt1b: "the same" for 0 < p < 1, with no numerical caveat.

     Index shifts are irrelevant for the limits. Hence n^pa_m → 2c(p) and n^pb_m → c(p) for m = n + O(1). ✓
   - *Arcsine limit.* J_0 = 2c + c(S + S*) is unitarily equivalent to multiplication by 2c(1 + cos θ) on
     L²(dθ/2π), so the spectral measure of e_0 is the law of 4c·cos²(θ/2), which is the arcsine law on [0, 4c],
     CDF (2/π)arcsin√(y/4c). ✓
   - *The tail set.* {k > Mn} = {n^px_k < M^{−p}} ✓. No atoms ⇒ the tail converges ✓. The μ_{n−1} rescaling ✓.
     F_p ~ (1/π)c^{−1/2}M^{−p/2} ✓.
   - *Numerics.* Recomputed F_2(4) = 0.1018 by hand ✓.
5. **T3-all.**
   - *Step 1.* The constants 2δ + 2Gη + G·sup(μ_n + μ_{n−1})(A) and the limsup 2Ge^{4G}F_p(M) are correct.
   - *Step 2.* The FVa bound uses 2|q_{n−1}q_n| ≤ μ_{n−1} + μ_n. On Mid it gives 3C_pδ. On A, 2C_pG(μ_n + μ_{n−1})(A)
     suffices, so the stated 3C_p is a valid weaker constant.
   - *Order of limits.* Fix M, let n → ∞, then M → ∞. ✓
6. **Hypothesis comparison.** Each earlier hypothesis implies sequence-form slow variation (sv):
   - ψ_k → L > 0 ⇒ sv;
   - polynomial sv ⇒ sv: take γ = 2, since [n/λ, λn] ⊂ [n/λ, n²] for n ≥ λ;
   - uniform sv (§3.7) ⇒ sv: take N = n and M = M′ = λ.

   **Conversely,** sv ⇒ uniform sv: for n ∈ [N, 2N] and k ∈ [n/M, M′N] ⊂ [n/M, M′n], the oscillation is
   ≤ δ_n(max(M, M′)) ≤ sup_{n≥N} δ_n(·) → 0. So sv and uniform sv are **equivalent**. "T3-all contains T3-conv,
   T3-sv, T3-avg" is therefore correct, and for T3-avg it is exact (same weight class).
7. **Consistency with Theorem R.** Theorem R's f equals ε·sign(Δ²μ_{N_i}) on windows [θN_i, N_i^{κ+1}]. That f is not
   slowly varying: neighbouring signs differ inside the windows, so δ_n(λ) ↛ 0. There is no contradiction. ✓
8. **Numerics re-run.** I ran `check_mn_loc.py` from jacobi-asymptotics. Its output is **byte-identical** to the
   committed `.out` (≈1 min).
   - [2] deviations: ≤ 0.002 for p = 2, ≤ 0.004 for p = 1, and ≤ 0.006 for p = 0.5. This matches L5.
   - The p = 0.5 rows drift away from F_p as M grows (M = 8, 16). That fits L5's truncation caveat.

## Findings

**F1 (MAJOR; Theorem L proof bullet 2, T3-all step 2; plan Review focus "uniformity of the head bound").**
The head H = {k < n/4} is fixed, and η_n = sup_t μ_m^{(t)}(H) is called "exponentially small (Sat_p⁺; as in T3-sv
step 2)". T3-sv, T3a, T3-avg and Theorem R do **not** use n/4. They fix M ≥ 4 such that g_p⁺ ≥ 1 on (0, 2/M], so the
margin depends on p.
- With H = {k < n/4} and θ = k/m ≈ 1/4, Sat_p⁺ is vacuous when g_p⁺(1/4) ≤ 0, i.e. for p ≤ 1.2767.
- The claim is false for p < 0.2067. Lemma LP itself gives lim μ_n^v(k < n/4) = (2/π)arccos√(4^p/(4c(p))) > 0, which
  is 0.119 at p = 0.1. Numerics confirm it (check 3).
- Consequently η_n ↛ 0 and the Grönwall bound loses its √η_n → 0 term. As written, Theorem L and T3-all are
  unproved for p ≤ 1.28.

*Fix.* Let M₀ = M₀(p) ≥ 4 with g_p⁺ ≥ 1 on (0, 2/M₀] (the T3-sv head margin). Then:
- set H := {k < n/M₀} and Mid := [n/M₀, Mn];
- replace δ_n(M) by δ_n(max(M, M₀)), which still → 0;
- in T3-all step 2, replace "2·4^p(n−1)^{−p}" and "x_k ≤ (4/n)^p" by 2M₀^p(n−1)^{−p} and (M₀/n)^p, so C_p depends
  on M₀.

The statements (M ≥ 4, the bound e^{4G}F_p(M)) are unchanged. Also correct the plan doc focus item "Mid ⊂ [n/4, Mn]".
Optionally, add a sentence that the head margin must lie below u_s(p), which is < 1/4 for small p.

**F2 (minor; Lemma LP statement).** "For every M > 0", but the arcsin argument exceeds 1 when M^{−p} > 4c(p), i.e.
M < u_s(p). *Fix:* write F_p(M) := (2/π)arcsin√(min(1, M^{−p}/(4c(p)))), or restrict to M ≥ 1. Since 4c(p) > 1 for all
p > 0, M ≥ 1 is safe.

**F3 (minor; citation gate, Lemma LP).** Two inputs are used without being quoted.
- The method of moments: moment convergence to a moment-determinate limit implies weak convergence. Quote it as a
  textbook input with exact hypotheses, e.g. Billingsley, *Probability and Measure*, Thm 30.2, or mark it
  "textbook-standard, not checked against a source" as was done for TL's Markov/Chebyshev.
- The spectral measure of J_0. Add the one-line computation (multiplication by 2c(1 + cos θ); law of 4c·cos²(θ/2)).

**F4 (minor; LP/T3-all, the constant C_p).** C_p is not defined. State it: for example C_p := 3M₀^p·sup_n(n/(n−1))^p
bounds n^p|x_k − a_n| and n^pb_n off the head for n ≥ n₀. Also note that the tail coefficient 3C_p could be 2C_p
(harmless).

**F5 (minor; slowly varying definition, Remark L1).** "This is implied by … uniform slow variation (§3.7)" understates
the relation. Sequence-form sv is **equivalent** to uniform sv (check 6). State the equivalence. It makes "contains
T3-avg" exact and avoids two names for one class.

**F6 (minor; labels / novelty).**
- TV row: add "standard; novelty not claimed". The derivative of orthonormal polynomials under weight tilting is
  classical (cf. FV/FVa).
- LP row: add "novelty UNCHECKED / not claimed". Ratio asymptotics with constant scaled limits imply the arcsine weak
  limit of p_n²dμ; this is a classical pattern (Nevai; Máté–Nevai–Totik; pointer only, not read).
- Thm L and T3-all rows carry novelty UNCHECKED. ✓

**F7 (minor; stale text in §4 "Stop condition (Plan 9; updated)" and "Most promising next step").** These paragraphs
contradict the updated §4 bullets and the status table. They still say "(T3) … is not reached by the methods developed
here", that "the precise missing statement is (T3) above", and that an RH analysis for pure powers "would prove the
pointwise law for pure powers" (RH_p/RH₁(r)/RH_plt1b already do).
*Fix:* add a dated note. (T3) is refuted for rough weights (Thm R) and proved for bounded slowly varying weights
(T3-all); the pure-power laws are proved; the remaining GAP is unbounded sv Ψ and non-pure-power nodes (and (CL) for
p ≤ 1 / general nodes).

**F8 (minor; overclaim hygiene).**
- Remark L1 "(T3) target of G1-R is therefore settled for bounded slowly varying weights" and the §4 bullet "(T3) is
  settled": append "(PROVED-mod-cite, pure-power nodes x_k = k^{−p}, base k^{−s})". The nodes restriction matters: G1-R
  was posed for regularly spaced nodes f(k).
- README already says "in review". ✓ The LOG entry is accurate but should carry the same pure-power-nodes qualifier,
  and should note F1 once fixed.

**F9 (observation, optional; §3.2 Conjecture R text).** That text says the [0.6N, 1.6N] form "would need localization
at scale Mn". Lemma TV's transport also works for rough weights w = ve^f, |f| ≤ ε:
- centering gives |g| ≤ 2ε everywhere, so ‖gq_m‖ ≤ 2ε;
- Grönwall then gives √μ_m^w(A) ≤ e^{4ε}(√μ_m^v(A) + 2ε).

This is localization up to O(ε²). It may bring the [0.6N, 1.6N] form of Conjecture R within reach. It is not required
for this plan, but the §3.2 sentence could mention it as a lead.

**F10 (cosmetic; check script [3]).** The script's δ_n uses k ∈ [n/4, Mn] and the head k < n/4, mirroring the flawed
H. For p = 2 this is harmless (head ≈ 10⁻³²), but after F1 the docstring should say the head is n/M₀.

## Plan doc Review focus: item by item

| Item | Result |
|---|---|
| TV: ℓ² differentiability; q̇_m formula; invariance | ✓ (check 1) |
| L: ‖g_nq_m‖ ≤ δ + G√η + G√y | ✓ |
| L: Grönwall with z = √(y + κ) | ✓ |
| L: uniformity of the head bound (Sat_p⁺) along the path, m = n − 1 and m = n | ✗ for H = {k < n/4} when p ≤ 1.28 (F1). With H = {k < n/M₀} it is uniform: the path stays in [min(1, c), max(1, C)]·v and θ = k/m ≤ 2/M₀ for m ∈ {n−1, n}, exactly as in T3-sv |
| L: Mid ⊂ [n/4, Mn] so δ_n(M) applies | ✓ as stated; after F1 use δ_n(max(M, M₀)) |
| LP: only coefficients with \|m − n\| ≤ j | ✓ |
| LP: weak convergence via determinacy | ✓ (quote it, F3) |
| LP: pure-power laws (a and b) and labels | ✓ (all p > 0 covered by RH_px / RH₁(r) / RH_plt1b, all REVIEWED, PROVED-mod-cite) |
| T3-all: FV/FVa bounds, T3a step 1, order of limits | ✓ after F1/F4 (T3a step 1 needs M₀, not 4) |
| "slowly varying (sequence form)" implied by earlier hypotheses | ✓, and equivalent to uniform sv (F5) |
| Consistency with Theorem R | ✓ (check 7) |

## Recommended labels (after fixes F1–F8)

- **TV:** PROVED (standard; novelty not claimed).
- **LP:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; textbook method of moments); novelty not claimed / UNCHECKED.
- **Thm L:** PROVED-mod-cite (as LP; internal TV, Sat_p⁺ with the p-dependent head margin M₀); novelty UNCHECKED.
- **T3-all:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, L); novelty UNCHECKED.
- REVIEWED after a re-check confirming F1. F2–F8 are editorial.

## Re-check (HEAD 3855f52)

**Verdict: ACCEPT.** F1–F8 and F10 are fixed; F9 is recorded as Remark L2′. No new errors. The polish items N1–N3
below are optional and do not block REVIEWED.

**F1: fixed.**
- *Head and Mid.* Theorem L now fixes the T3-sv head margin M₀(p) ≥ 4 (g_p⁺ ≥ 1 on (0, 2/M₀]). It sets
  H = {k < n/M₀}, Mid ⊂ [n/M₀, Mn] and M₁ = max(M, M₀).
  - [n/M₀, Mn] ⊂ [n/M₁, M₁n], so |g_n| ≤ δ_n(M₁) on Mid for both m ∈ {n−1, n}.
  - δ_n(M₁) → 0, since M₁ is fixed once M is.
- *Head bound.* For k < n/M₀ and m ≥ n − 1 ≥ 1, θ = k/m ≤ 2/M₀. Sat_p⁺ along the path, with W(t)/w_k(t) ≤
  (max(1, C)/min(1, c))ζ(s)k^s, gives η_n ≤ poly(n)·e^{−2(n−1)} → 0, exactly as in T3-sv.
- *Unaffected parts.* The Grönwall step and the limit statement are unchanged and still correct.
- *T3-all.*
  - Step 1 uses δ_n(M₁).
  - Step 2 uses a_n, b_n ≤ 2M₀^p(n−1)^{−p} and x_k ≤ (M₀/n)^p off the head.
  - C_p := 4·2^pM₀^p bounds n^p|x_k − a_n| ≤ max(M₀^p, 2M₀^p(n/(n−1))^p) and n^pb_n ≤ 2^{p+1}M₀^p for n ≥ 2. ✓
  - The order of limits is unchanged. ✓
- The F1 remark (u_s(p) < 1/4 for small p) is accurate.

**F2: fixed.** The statement now reads M ≥ 1 with min(1, ·). Because 4c(p) > 1, the min is idle on that range. ✓

**F3: fixed, with one residual.** The Fourier computation is correct: J_0 = c(2 + S + S*), symbol 2c(1 + cos θ),
moments (1/2π)∫(2c(1 + cos θ))^j dθ, and the image of dθ/2π is the arcsine law on [0, 4c].
- *Is "method of moments; textbook-standard, not separately cited" acceptable under AGENTS.md?* Yes. The precedent is
  TL's Markov/Chebyshev ("textbook-standard, not checked against a specific source"), which passed Rule R.
- That precedent *quotes the statement*, though, and Hard rule 4 asks for exact hypotheses. **N1 (polish):** add the
  one line "if every moment of ν_n converges to the corresponding moment of ν and ν is determined by its moments, then
  ν_n → ν weakly". The hypotheses are met here: all ν_n are probability measures with all moments finite (support
  ⊂ [0, n^p]), and ν is compactly supported.

**F5: fixed** ("equivalent to uniform slow variation"). ✓

**F6: fixed.** The TV row reads "standard; novelty not claimed". The LP row reads "textbook method of moments … novelty
not claimed". ✓

**F7: fixed.** The §4 stop text is rewritten. The superseded Plan-9 text is kept and marked. The remaining-open list
(unbounded sv Ψ, other nodes, (CL) for general nodes or p ≤ 1) matches §3.8 L4 and the table. ✓

**F8: fixed.** Qualifiers ("PROVED-mod-cite; pure-power nodes k^{−p}, base k^{−s}") were added in L1, §4 and the LOG. ✓

**F9: recorded.** Remark L2′ reads "O(ε) in √μ … not examined". It matches the bound
√μ^w ≤ e^{4ε}(√μ^v + 2ε) and does not overclaim. ✓

**F10: fixed** (docstring). ✓ The numerics are unchanged; the earlier re-run was byte-identical.

**Polish items (non-blocking).**
- **N1.** Quote the method-of-moments statement in one line (see F3).
- **N2.** Status row LP still prints arcsin√(M^{−p}/(4c(p))) with no range. Add "M ≥ 1".
- **N3.** Theorem L proof bullet 2 says "as in T3-sv step 2". T3-sv's proof has a "Head" bullet, not a numbered step 2.
  Say "as in the T3-sv Head bullet".
- **Bookkeeping.** At REVIEWED, update the "Rule R pending" status rows (TV, LP, Thm L, T3-all), the §3.8 header and the
  LOG.

**Final labels.**
- **TV:** PROVED (standard; novelty not claimed); REVIEWED.
- **LP:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; textbook method of moments); novelty not claimed; REVIEWED.
- **Thm L:** PROVED-mod-cite (as LP; internal TV, Sat_p⁺ with head margin M₀(p)); novelty UNCHECKED; REVIEWED.
- **T3-all:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, L); pure-power nodes k^{−p}, base
  k^{−s}, Ψ bounded and slowly varying; novelty UNCHECKED; REVIEWED.
