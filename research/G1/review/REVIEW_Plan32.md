# Rule R review: Plan 32 (Lemma FVa, Theorem T3a)

Reviewer: independent Rule R pass, 2026-10-14. Target: worktree `ja-plan32`, branch `plan-32-alaw`, commit 3f73b79.
Scope: research/G1/PROOF.md §3.5 (Lemma FVa, Theorem T3a, Remarks T3a1–T3a2), status rows FVa and T3a, LOG Plan-32
entry, README edit, docs/superpowers/plans/2026-10-14-plan-32-alaw.md (Review focus), research/G1/checks/check_alaw.py/.out.

## Verdict

**ACCEPT WITH FIXES.** I found no mathematical error. Every step of FVa was redone independently, and every bound in T3a
holds (the constants 14 and 7 are valid for large n, with slack). The fixes below are about precision of a citation,
hidden "n large" conditions, misquoted numerics and stale text elsewhere in the file. None changes a statement.

## Independent checks done

1. **FVa, step by step.**
   - a_n = ⟨x, μ_n⟩ = Σx_k(ρ_{n+1} − ρ_n)(k) = 𝔼_{n+1}⟨x,X⟩ − 𝔼_n⟨x,X⟩: correct. ⟨x,X⟩ ≤ m, so it is bounded.
   - Tilting: d/dt 𝔼_{m,t}F = Cov_{m,t}(F, ⟨f,X⟩) for P_{m,t}(S) ∝ Π_{k∈S}v_ke^{tf_k}V(S), with domination exactly as in
     Lemma FV (|∂_t| ≤ m‖f‖_∞ × term): correct.
   - Two-point function: inclusion–exclusion 1 − (1 − K_kk) − (1 − K_ll) + [(1 − K_kk)(1 − K_ll) − K_kl²] = K_kkK_ll − K_kl²: correct.
     Var X_k = K_kk − K_kk² on the diagonal. K_m = QᵀQ with orthonormal rows in ℓ²(atoms), so K_m² = K_m and
     Σ_lK_kl² = K_kk (absolutely convergent; Σ_{k,l}K_kl² = m). Then
     Cov(⟨g,X⟩,⟨f,X⟩) = Σ_kg_kf_kK_kk − Σ_{k,l}g_kf_lK_kl² = Σ_{k,l}K_kl²(g_kf_k − g_kf_l) = ½Σ(g_k − g_l)(f_k − f_l)K_kl²: correct.
   - Rank-one update: K_{n+1}² − K_n² = 2K_nq_n(k)q_n(l) + q_n(k)²q_n(l)² entrywise: correct. The rank-one part gives
     ⟨xf, μ_n⟩ − a_n⟨f, μ_n⟩ = ⟨(x − a_n)f, μ_n⟩ (Σμ_n = 1): correct.
   - Christoffel–Darboux: with xp_j = b_{j+1}p_{j+1} + a_jp_j + b_jp_{j−1}, (x − y)Σ_{j<n}p_j(x)p_j(y) =
     b_n(p_n(x)p_{n−1}(y) − p_{n−1}(x)p_n(y)). Checked at n = 1 by hand. This matches b_n = ⟨xq_{n−1}, q_n⟩ and the
     sign used.
   - The −2b_n term, redone: let A(k,l) := q_n(k)q_{n−1}(l) − q_{n−1}(k)q_n(l), which is antisymmetric. Then
     A·q_n(k)q_n(l)·(f_k − f_l) is symmetric, so the sum is 2Σ_{k,l}A(k,l)q_n(k)q_n(l)f_k =
     2[⟨f,μ_n⟩⟨q_{n−1},q_n⟩ − ⟨f,q_{n−1}q_n⟩⟨q_n,q_n⟩] = −2⟨f, q_{n−1}q_n⟩. Times b_n, this is the stated term. Correct.
   - Invariance under f ↦ f + 1 and the Toda case f = x (‖xq_n‖² = b_{n+1}² + a_n² + b_n², so the result is
     b_{n+1}² − b_n²): correct. The n = 0 case (K_0 = 0, b_0 := 0) is also correct.
   - **Independent numerics** (reviewer, mpmath at 60 digits, h = 10⁻²⁰, p = ½, s = 3/2, K = 40 atoms, random f): the
     formula matches central differences to ≤ 1.1·10⁻⁴¹ for n = 0, 1, 3, 7. This is a different p from the committed
     check (p = 2).
2. **Index conventions of the cited a-laws.**
   - RH/px/RH_px.md §convention: xπ_N = π_{N+1} + a_Nπ_N + b_N²π_{N−1} with b_N² = h_N/h_{N−1}. This is the same as
     §3.5. It states n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n) (lines 373, 381).
   - RH/RH_p1_general.md (lines 28, 425) and RH/plt1/RH_plt1b.md (line 116) state the same a-law, for all r > 1 and for
     0 < p < 1 with s > 1. All three are REVIEWED.
   - An index shift by one would not matter in any case, since b_{n±1}/b_n = 1 + O(1/n). See F9 for a harmless
     pre-existing index point in RH_p1.md.
3. **T3a, line by line.**
   - x_k = k^{−p} ≤ (M/n)^p for k ≥ n/M: correct.
   - The head mass is bounded uniformly in t by Sat_p⁺ with the path sandwich (W(t) ≤ max(1,C)ζ(s), w_k(t) ≥ min(1,c)k^{−s}),
     as in T3-sv. So a_n^{(t)} ≤ M^pn^{−p} + O(n^{O(1)}e^{−2(n−1)}) ≤ 2M^pn^{−p} for n ≥ n₀ uniformly in t: correct.
   - b_n = Σx_kq_{n−1}q_n ≤ ½Σx_k(q_{n−1}² + q_n²) uses x ≥ 0: correct. Also ≤ 2M^p(n−1)^{−p} (step 1 at n − 1).
   - The centered bound |⟨g, q_{n−1}q_n⟩| ≤ ½Σ|g|(μ_{n−1} + μ_n) gives the displayed inequality.
   - Middle: honest constant 3n^{−p} + 4(n−1)^{−p} ≤ 7M^p(n−1)^{−p}, which is ≤ 14M^pn^{−p} once (n/(n−1))^p ≤ 2.
   - Tail: (3 + 2(n/(n−1))^p)μ_n + 2(n/(n−1))^pμ_{n−1} ≤ 7(μ_n + μ_{n−1}) for large n. With Lemma TL at T = ⌊n^γ⌋
     (valid for μ_{n−1} too, since μ_{n−1} ≤ ρ_n ≤ ρ_{n+1}) this gives 14GM^pεn^{−p}.
   - Order of limits: M, γ = κ + 1 and G are fixed before ε. The threshold n₀ depends on ε. Then limsup is ≤ 14GM^pε,
     and ε → 0. Correct.
   - Conclusion: n^p a_n(v) = 2·n^p b_n(v)·(a_n/2b_n) → 2c(p). Correct.
4. **Numerics.** I re-ran check_alaw.py from jacobi-asymptotics. The output is identical, digit for digit, to the
   committed .out.

## Findings

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| F1 | minor (citation precision) | FVa step 3 | Lemma H (G3′ §5.2), *as stated*, gives only the inequality D_n(μ∖E′)/D_n(μ) ≤ Π(1 − ρ_n) and the single-deletion equality. The equality D_n(μ∖E′)/D_n(μ) = det(I − K_{E′}) is in its *proof* (Gram/Sylvester steps). The identification D_n(μ∖E′)/D_n(μ) = P_n(S ∩ E′ = ∅) is the Heine sum restricted to S avoiding E′. | Cite "the Gram/Sylvester steps of Lemma H's proof (the equality before Hadamard)", as G3′ §5.4 line 253 does. Add the one-line Heine identification. |
| F2 | minor (completeness) | FVa step 3 | The covariance identity also uses the diagonal Var X_k = K_kk − K_kk², and absolute convergence of the infinite double sums (Σ_{k,l}K_kl² = m, with f, g bounded). Neither is mentioned. K² = K is in ℓ²(atoms). | Add one sentence. |
| F3 | minor (exposition) | FVa step 4 | "Expanding … gives −2b_n⟨f,q_{n−1}q_n⟩" skips the only non-obvious algebra. The CD identity is quoted without its recurrence convention. | Insert the antisymmetry computation from check 1 above. State CD for xp_j = b_{j+1}p_{j+1} + a_jp_j + b_jp_{j−1} as textbook-standard (as Lemma FV's inputs are). Note n = 0 (b_0 := 0, K_0 = 0). |
| F4 | minor (constants / hidden n₀) | T3a step 2 | The constants are valid but use unstated "n ≥ n₀(p)" conditions: (n/(n−1))^p ≤ 2 for 14, and ≤ 7/5 for 7. The head coefficient "(1 + 2)" overstates b_n: b_n ≤ ½(a_{n−1} + a_n) ≤ 1, so "1 + 1" suffices. Also |x_k − a_n| ≤ max(x_k, a_n) ≤ 2M^pn^{−p} in the middle (both are nonnegative), not 3. | Say "for n ≥ n₀(p, M, ε)". Optionally tighten to 2 + 4(n/(n−1))^p ≤ 7 (middle). Nothing downstream changes. |
| F5 | minor (labels) | §0 rows FVa, T3a | The FVa row lacks the "(standard; novelty not claimed)" tag that FV carries and that Remark T3a1 asserts. The T3a row omits its internal inputs, unlike the T3-sv row. | FVa: "PROVED (standard; novelty not claimed; self-contained via Lemma H's Gram/Sylvester step and CD)". T3a: "PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FVa, Lemma Sat_p⁺, Lemma TL)". |
| F6 | minor (misquoted numerics) | §3.5 NUMERICAL bullet 1; LOG | "relative error ≤ 1.3·10⁻⁸ (n = 20, 60, 150)" is false: the .out has 8.0·10⁻⁸ at n = 150 (random f). The LOG's "agree to 10⁻⁸" has the same problem. | Write "≤ 8·10⁻⁸". |
| F7 | minor (numerics presentation) | Remark T3a2; check_alaw.py [2] | (a) The script computes (n+1)²a_n/(2c), but the remark says n²a_n. (b) The three quoted n (250, 1000, 3600) hide non-monotone behaviour. From the same .out, n = 500 and 2000 give \|A(ψ) − A(1)\| ≈ 8.7·10⁻⁴ and 5.3·10⁻⁴ (ψ), and ≈ 1.6·10⁻³ and 1.8·10⁻⁵ (parity). The "decay" in the parity row is a selection artifact of even/odd-scale oscillation. (c) The pure reference stalls at +3.0·10⁻⁴ → +3.2·10⁻⁴ (n = 2000 → 3600) instead of decaying like 1/n. That suggests a truncation (K = 1.2·10⁵ ≈ 33n) or precision floor, and there is no K vs 2K run (Rule N). | State (n+1)². Report all five n and say "non-monotone". Add a K-doubling run, or note the ≈3·10⁻⁴ floor so the 2.1·10⁻⁵ at n = 3600 is not read as a rate. Not load-bearing (the theorem is proved). |
| F8 | minor (stale text) | §3.3 Remark T3c3; §4 "a_n side"; README | T3c3 still says the a_n first variation is "Not done". §4's a_n bullet does not mention that the pointwise a-law is now proved for the T3-sv class. README says "in review". | Point T3c3 to §3.5. Add one line to §4. Update the README after acceptance. |
| F9 | info (pre-existing, no effect) | RH/RH_p1.md §3 "Fold" | Take xP_k = P_{k+1} + β_kP_{k−1} with β_n = ‖π_n‖²/‖π_{n−1}‖². With 0-based m and β_0 := 0, the fold is a_m = β_{2m} + β_{2m+1}, b_m² = β_{2m−1}β_{2m}. The file's a_m = β_{2m−2} + β_{2m−1} is shifted by one (or uses 1-based a). With β_N = N^{−1}(1 + O(1/N)) this changes only O(1/n) terms, so RH₁(r)'s a-law and T3a are unaffected. | Optional note in RH_p1.md (via its own review trail). |
| F10 | info (pre-existing path) | §3.3 Theorem T3-conv bullet | It cites `RH/RH_px.md`, but the file is `RH/px/RH_px.md`. §3.5 cites it by name only. | Fix the path. |

## Novelty

Remark T3a1 is appropriate. First variations of recurrence coefficients under weight tilting (Toda/Volterra flows,
Christoffel–Darboux/determinantal covariance) are classical, and "novelty not claimed" is the right label for FVa.
For T3a, "novelty UNCHECKED" is right too. Ratio and comparison asymptotics of Máté–Nevai–Totik type, and
Lubinsky-style universality comparisons, are candidate prior art for "a slowly varying weight factor does not change
the leading recurrence asymptotics". None was checked here.

## Recommended labels (after F1–F8)

- **FVa:** PROVED (standard; novelty not claimed); REVIEWED.
- **T3a:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FVa, Lemma Sat_p⁺, Lemma TL); REVIEWED; novelty
  UNCHECKED.
- check_alaw [1]: NUMERICAL (float64, validates FVa). [2]: NUMERICAL, illustrative only (F7).
