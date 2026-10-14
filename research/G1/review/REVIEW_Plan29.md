# REVIEW_Plan29: Rule R second reading of G1 §3.3 Theorem T3-conv (Plan 29), 2026-10-14

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files except this one.
- **Scope.** research/G1/PROOF.md §3.3 (Lemma Sat_p⁺, Theorem T3-conv, Remarks T3c1–T3c3, NUMERICAL block); the
  status row T3-conv; the G1 LOG Plan-29 entry; the README G1-R edit; docs/superpowers/plans/2026-10-14-plan-29-t3conv.md
  (Review focus); checks/check_t3_conv.py/.out. Context read: §3.1 Lemma Sat_p (REVIEWED), §3.2 Lemma FV (Rule R
  pending, checked here as far as T3-conv uses it), G3′ §5.2 Lemmas H and Sat, G3′ Lemma K (concentration) and
  Lemma Tr, statements of RH₁(r), RH_px, RH_plt1, RH_plt1b, G2's c(p).
- **Re-runs** (scratch in the session scratchpad `p29rev/`).
  - `check_t3_conv.py` reproduces `check_t3_conv.out` **byte-identically** (48 s).
  - `satp.py` / `sweep.py` (float64): the full concavity-bound chain for log Π (the Lagrange product of G3′ Lemma Sat
    with the p < 1 bounds j^p − k^p ≥ p j^{p−1}(j − k), k^p − j^p ≥ p k^{p−1}(k − j)) against −n·g_p⁺(θ), for
    p ∈ {0.02, 0.1, 0.3, 0.5, 0.7, 0.95}, every 1 ≤ k < n for n < 200, and n ∈ {500, 1000, 2000, 5000}; also exact
    log Π on a (k, n) grid up to n = 10⁵ for p ∈ {0.05, …, 2}. **No violation**; the margin is ≥ 2.0 in log Π
    everywhere (worst at n = 2, k = 1). So the stated inequality is true; the written proof has a gap (F1).
  - `plow.py` (long double RKPW, toolkit): T3-conv at p = ½ (K = 2·10⁵) and p = 1 (K = 1.2·10⁵), s = 2, n ≤ 1500.
    |β_n(ψ)/β_n(1) − 1| for ψ = 1 + ½(−1)^k/log(k+1): p = ½: 4.0e−3, 2.7e−3, 5.3e−4, 1.2e−3, 1.8e−4
    (n = 100, 200, 400, 800, 1500); p = 1: ≤ 7.3e−4. A head-only perturbation (ψ = 3 for k < 20) changes β_n by
    ≤ 2e−16 at n ≥ 100, as Lemma Sat_p⁺ predicts. (Absolute β_n for p = ½ is truncation-biased at this K; only ratios
    are meaningful.)

| Result | Verdict | Required fixes |
|---|---|---|
| Lemma Sat_p⁺ | **ACCEPT WITH FIXES** | F1: the proof misses a second sign change for p < 1 (the Σ log j comparison); statement true |
| Theorem T3-conv | ACCEPT WITH FIXES (minor) | F4: ζ(s) constant; termwise-differentiation sentence |
| Lemma FV (as used) | ACCEPT | — (correct; its own Rule R is separate) |
| Pure-power citations | ACCEPT | — |
| Remark T3c1 | ACCEPT WITH FIXES | F3 (hedge "can break"), F5 (example undefined at k = 1) |
| Remark T3c2 | **ACCEPT WITH FIXES** | F2: wrong lemma cited; averaged statement not formulated; scope p = 2 / p > 1 |
| Remark T3c3 | ACCEPT | — |
| Numerics | ACCEPT WITH FIXES | F6: "decreasing" is false for two variants |
| Status row / LOG / README / plan | ACCEPT WITH FIXES | F2 (LOG repeats T3c2), F7 (label) |

**Overall: ACCEPT WITH FIXES.** The theorem is correct and the proof is short and sound: the path w(t) = vψ^t stays
in a fixed sandwich; Lemma FV plus centering reduces everything to ⟨g, μ_n − μ_{n−1}⟩ with g → 0 at ∞; the finitely
many head atoms k < k_ε are deeply saturated at level m → ∞, uniformly in t. I found no counterexample, and the
numerics (repo's p = 2 and my p = ½, 1) are consistent. The only substantive defect is in Lemma Sat_p⁺'s one-line
proof (F1), which is repairable in a few lines and in any case irrelevant to the theorem (any polynomial prefactor is
absorbed by e^{−2m}). Recommend REVIEWED after F1–F7, without a further re-check beyond confirming F1's text.

## Verification notes (what was checked and holds)

1. **Concavity inequalities (p < 1).** Mean value: j^p − k^p = pξ^{p−1}(j − k), ξ ∈ (k, j); ξ^{p−1} is decreasing,
   so ≥ j^{p−1}. Likewise k^p − j^p ≥ p k^{p−1}(k − j) for j < k. Both directions as stated are correct. (For p ≥ 1,
   §3.1's p-free versions j^{p−1}(j − k) and k^{p−1}(k − j) are also correct.)
2. **Factor p^{−(n−1)}.** The product runs over the n − 1 indices j ≤ n, j ≠ k; each factor bound gains exactly 1/p
   (j < k: k/(p(k − j)); j > k: k^p/(p j^{p−1}(j − k))). Squared: p^{−2(n−1)} ≤ p^{−2n} = e^{2n log(1/p)}, so
   g_p⁺ = g_p − log(1/p) is the right exponent.
3. **g_p⁺ → ∞.** g_p(θ) = p log(1/θ) − θ log(1/θ) + (1 − θ)log(1 − θ) − p + (p − 1)θ ≥ p log(1/θ) − 2/e − p − 1
   on (0, 1). For p < 1, g_p′(θ) = log(θ/(1−θ)) − p/θ + p − 1 < 0 on (0, ½) as well, so a θ₁ with g_p⁺ ≥ 1 on (0, θ₁]
   exists (continuity and the limit suffice anyway).
4. **Lemma FV.** d/dt log D_m = Σ_k f_k P_m(k ∈ S) = Σ_k f_k ρ_m(k) (Heine; P_m(k ∈ S) = w_kK_m(x_k, x_k) by G3′
   Lemma H); log b_n² = log D_{n+1} − 2log D_n + log D_{n−1} from h_n = D_{n+1}/D_n; second difference of ρ gives
   w(p_n² − p_{n−1}²). Correct. Termwise differentiation is justified because each Heine term satisfies
   |∂_t term_S| ≤ m‖f‖_∞ term_S(t) ≤ m‖f‖_∞ e^{m‖f‖_∞}term_S(0), a summable majorant uniform in t ∈ [0, 1] (F4).
5. **Sandwich.** ψ_k > 0 and ψ_k → L > 0 give 0 < inf ψ ≤ sup ψ < ∞; ψ^t ∈ [min(1, inf ψ), max(1, sup ψ)] for
   t ∈ [0, 1]. So Σw(t) ≤ Cζ(s) and w_k(t) ≥ c k^{−s}, uniformly in t.
6. **Centering.** Σ_k w_k p_n(x_k)² = 1 for every n (orthonormality), so constants are annihilated by μ_n − μ_{n−1}.
7. **Head.** μ_m(k) = ρ_{m+1}(k) − ρ_m(k) ≤ 1 − ρ_m(k) since ρ_{m+1} ≤ 1. For k < k_ε and m ≥ k_ε/θ₁ (so k < m and
   k/m ≤ θ₁), Sat_p⁺ gives μ_m^{(t)}(k) ≤ (Cζ(s)/c)k^s e^{−2m}, uniformly in t. Applied at m = n and m = n − 1.
8. **Final estimate.** |⟨g, μ_n − μ_{n−1}⟩| ≤ 2ε + 2G(Cζ(s)/c)k_ε^{s+1}e^{−2(n−1)}; integrate in t, n → ∞,
   ε → 0. Correct.
9. **Transfer.** b_n is invariant under scaling σ ↦ λσ, so comparing with v (not Lv) is right. The inputs match:
   RH_px (σ_{p,s} = Σk^{−s}δ_{k^{−p}}, p > 1, s > 1: n^p b_n = c(p)(1 + O(1/n))); RH₁(r) with r = s > 1
   (n b_n = ½(1 + O(1/n)) = c(1)(1 + O(1/n))); RH_plt1b (0 < p < 1, s > 1, no numerical caveat). C = 1 for
   x_k = k^{−p}. The b_n index convention (b_n² = h_n/h_{n−1}) only shifts n by at most one, which is harmless for a
   limit. Hence n^p b_n(w) → c(p), β_n → 1, and (T3).
10. **T3c2's inequality.** Σ_{m=N}^{2N}μ_m(k) = ρ_{2N+1}(k) − ρ_N(k) ≤ ρ_{2N+1}(k); summing over A gives
    ≤ 𝔼_{2N+1}#(S ∩ A). Correct (but see F2 for what it is used for).

## Findings

**F1 (Moderate; §3.3 Lemma Sat_p⁺ proof; also LOG).** "As for Lemma Sat_p, with one change" is false. §3.1's proof
bounds the j > k product by k^{p(n−k)}/((n−k)!·(n!/k!)^{p−1}) and then uses Σ_{k<j≤n}log j ≥ ∫_k^n log t dt. For
p < 1 the exponent p − 1 is negative, so (n!/k!)^{1−p} sits in the *numerator* and that comparison goes the wrong way:
one needs an **upper** bound on Σ log j. With the crude upper bound the chain gains an extra (1 − p)·log(n/k) (or ½ of
it with a trapezoid estimate), which the written proof does not account for. The statement is nevertheless true
(numerically the full chain stays ≥ 2 below −n g_p⁺ for all tested p, k, n), because §3.1's chain has unused slack.
**Fix (either):**
- (a) Keep the statement and add the step: for concave log, the trapezoid rule gives Σ_{j=k+1}^n log j ≤
  ∫_k^n log t dt + ½log(n/k); absorb ½(1 − p)log(n/k) with the Stirling slack ½log(2π(n−k)) in log(n−k)! ≥ (n−k)log(n−k)
  − (n−k) + ½log(2π(n−k)) and ½log(2πk) in k^k/k! ≤ e^k/√(2πk) (and n/k ≤ 4π²k(n−k) for 1 ≤ k < n); or
- (b) state Sat_p⁺ for p < 1 with a harmless prefactor, 1 − ρ_n(k) ≤ (W/w_k)(n/k)^{1−p}e^{−2n g_p⁺(θ)}, and note that
  Theorem T3-conv's step 3 only needs e^{−2m}·poly(m). Option (b) is the minimal, obviously correct repair.
Also change "one change" to "two changes" (the 1/p per factor, and the direction of the Σ log j comparison).

**F2 (Moderate; Remark T3c2; LOG Plan-29 bullet "the averaged version follows from Lemma K").**
- In G1/PROOF.md, "Lemma K" is the §1 kernel identity for G(n). It has nothing to do with tail localization of
  μ_m. The relevant tool is a tail-count concentration bound 𝔼_n#(S ∩ (Mn, ∞)) ≤ ε(M)n + o(n), e.g. **G3′ Lemma K
  (concentration, from H7)** (stated for x_j = j^{−2}, i.e. p = 2, under (Hw)), or G2 Theorem A-U's splitting for
  p > 1 (as in Theorem CL step 3 / Lemma WC). None is stated for p ≤ 1 in the repo, and uniformity of the constants
  along the path w(t) (sandwich-only dependence) has to be checked.
- "The averaged version" is not formulated. What the inequality of note 10 actually yields, given such a tail bound
  uniform in t, is: (1/N)Σ_{n=N}^{2N}|log b_n²(w) − log b_n²(v)| → 0 (centering at log Ψ(N), slow variation on
  [θ₁N, 2MN], head by Sat_p⁺), i.e. β_n(w) → 1 along a set of n of density one. That is not implied by H_all and is
  worth stating precisely.
- **Fix:** replace "follows from Lemma K" by "would follow from a tail-count bound such as G3′ Lemma K (p = 2) / G2
  A-U (p > 1), uniform in the sandwich (not checked here)", state the averaged conclusion explicitly, and label it a
  SKETCH (not a result). Same edit in LOG.

**F3 (Minor; Remark T3c1).** "*Non-decaying* roughness of size ε can break it: Conjecture R" asserts what is only
conjectured. **Fix:** "is conjectured to break it (Conjecture R, §3.2; NUMERICAL evidence only; Lemma FV and
Conjecture R are under Rule R)". The section's "dichotomy" framing should carry the same hedge.

**F4 (Minor; Theorem T3-conv steps 1, 3, 4).**
- Step 3/4: Sat_p⁺ gives W(t)/w_k(t) ≤ Cζ(s)/(c k^{−s}), so the constant is (Cζ(s)/c)k^s, not (C/c)k^s (harmless).
- Step 1: "D_m(t) is a convergent sum of smooth functions" does not by itself give differentiability; add the
  majorant of note 4 (uniform convergence of the derivative series).
- Step 3: state explicitly that m ≥ k_ε/θ₁ also ensures k < m, which Sat_p⁺ requires.

**F5 (Minor; Remark T3c1 example).** ψ_k = 1 + (−1)^k/log k is undefined at k = 1 (log 1 = 0); with log(k + 1) and
coefficient 1 it would be negative at k = 1 (1 − 1/log 2 < 0). **Fix:** use the numerics' ψ_k = 1 + ½(−1)^k/log(k+1).

**F6 (Minor; NUMERICAL block).** "For random ±½/√log and block-sign ±½/log variants it is ≤ 2.3·10⁻³ and decreasing":
the bound is right, "decreasing" is not. Random: 4.9e−4, 3.9e−4, 4.2e−4, 4.3e−4, 2.5e−4; block: 5.4e−5, 2.3e−3,
5.0e−6, 2.5e−4, 2.1e−4 (n = 250 … 3600). **Fix:** "≤ 2.3·10⁻³, non-monotone, no growth". Optionally note that only
p = 2 is tested in the repo (the reviewer's p = ½ and p = 1 runs above are consistent), and that the 1/log decay of
ψ − 1 makes the numerics a consistency check, not evidence for the limit.

**F7 (Minor; status row T3-conv).** The label lists Lemma FV among the "mod-cite" items. Lemma FV is internal and
correct (note 4), but its own Rule R is pending. **Fix:** "PROVED-mod-cite (RH_px / RH₁(r) / RH_plt1b) + internal
Lemmas FV (Rule R pending, §3.2) and Sat_p⁺; Rule R ACCEPT WITH FIXES (REVIEW_Plan29)". Also cite the files
(RH_px.md, RH_p1_general.md, RH_plt1b.md) rather than "RH_p seam".

## Recommended labels (after fixes)

- Lemma Sat_p⁺: PROVED (after F1); REVIEWED.
- Theorem T3-conv: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b, each REVIEWED); REVIEWED, conditional only on Lemma FV's
  own Rule R (which I find correct as used); novelty UNCHECKED (a perturbation/ratio-asymptotics result of this kind
  may be classical — Nevai-class / Máté–Nevai–Totik style comparison for discrete measures should be searched).
- Remark T3c2 averaged claim: SKETCH (not a result) until a tail-count bound uniform in the sandwich is cited for the
  relevant p.
- T3c1 dichotomy: hedged per F3 (Conjecture R remains CONJECTURE, NUMERICAL).
- README: "in review" → "REVIEWED (Rule R ACCEPT WITH FIXES)" once applied.

## Re-check (commit 1a9d16c, after merging master; §3.2 is now the REVIEWED Plan-28 version), 2026-10-14

**Verdict: ACCEPT.** F1–F7 are resolved. The only residual items are bookkeeping (R1) and one optional wording
point (R2).

- **F1 — resolved.**
  - The statement now carries ((n+1)/k)^{2(1−p)₊}, and the proof names both changes for p < 1.
  - Checked: Σ_{j=k+1}^n log j ≤ ∫_{k+1}^{n+1}log t dt, since log is increasing. Also ∫_{k+1}^{n+1} − ∫_k^n =
    ∫_n^{n+1}log − ∫_k^{k+1}log ≤ log(n+1) − log k. Times (1 − p), this gives ((n+1)/k)^{1−p} in Π and the squared
    exponent 2(1 − p).
  - The integral term reproduces the p ≥ 1 algebra verbatim: the log n terms cancel and the remainder is −n·g_p.
    Together with step 1 (p^{−(n−1)} ≤ p^{−n}), the lemma is correct as stated.
  - My earlier sweep showed that even the prefactor-free chain stays below the bound, so the new statement is, if
    anything, loose.
  - Theorem step 3: ((m+1)/k)^{2(1−p)₊} ≤ (m+1)² for k ≥ 1. Step 4's (n+1)²e^{−2(n−1)} → 0. Correct.
- **F2 — resolved.**
  - T3c2 is now a SKETCH. It states the averaged conclusion (1/N)Σ|log b_n²(w) − log b_n²(v)| → 0, and the
    tail-count requirement O(n/log M) uniform along the path. It cites G2 A-U (p > 1) and G3′ §7 Lemma K (p = 2),
    which I confirmed are in §7 at line 846. It says that nothing is stated for p ≤ 1, and it disambiguates G1's
    Lemma K. The LOG matches.
  - Wording note (optional): A-U bounds the Heine mass T_m; turning that into a count bound also needs A-L, as in
    Lemma WC step 5. Fine for a sketch.
- **F3 — resolved.** T3c1 says "conjecturally", with numerical evidence only (p = s = 2). The README now says
  "numerical evidence".
- **F4 — resolved.**
  - ζ(s) is in steps 1, 3 and 4. k < m is explicit in step 3.
  - The smoothness majorant is stated. Minor: it should also note term_S(t) ≤ max(1, sup ψ)^m·term_S(0), which gives
    uniform domination in t. Implicit and harmless.
- **F5 — resolved.** The example is ψ_k = 1 + ½(−1)^k/log(k+1), which is positive for all k ≥ 1.
- **F6 — resolved.** "Not monotone in n" and "only p = 2 tested" are now stated.
- **F7 — resolved.** The status row names RH_px, RH₁(r) and RH_plt1b, lists Lemma FV (now REVIEWED) and Sat_p⁺ as
  internal, and adds a novelty pointer.

**Residual items.**
- **R1 (bookkeeping).** Update the "re-check pending" text in the §3.3 heading, the status row and the LOG, and
  "in review" in the README, to "re-check ACCEPT — REVIEWED".
- **R2 (optional).** The theorem's bullet list still says "RH_p for p > 1" and "the RH_p seam construction". The
  file names RH_px.md and RH_plt1b.md could be added there too, for consistency with the status row.

**Final labels.**
- Lemma Sat_p⁺: PROVED; REVIEWED.
- Theorem T3-conv: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b, each REVIEWED; internal Lemma FV REVIEWED, Lemma
  Sat_p⁺); REVIEWED; novelty UNCHECKED.
- T3c2 averaged version: SKETCH. The pointwise version for slowly varying Ψ: OPEN.
- Conjecture R: CONJECTURE (NUMERICAL), unchanged.
