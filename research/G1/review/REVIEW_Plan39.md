# Rule R review — Plan 39 (Theorem RW: Conjecture R in window form)

Reviewer: independent second reader (Rule R). Branch plan-39-rw, commit f425b7b, `git diff master...HEAD`.
Scope: research/G1/PROOF.md §3.10 (Lemma u_s, Lemma LP-w, Lemma R1W, Theorem RW, Corollary RW′, remarks RW-a–f),
§0 rows RW and Conj R, the §3.2 dated pointer, LOG.md entry, plan doc 2026-10-14-plan-39-rw.md (Review focus),
checks/check_rw.py/.out. Compared against §3.6 (Theorem R, Lemmas R1, R2), §3.8 (Lemma LP), §3.3 (Sat_p⁺), §3.1 (g_p),
§2 ((T3), ω(δ)), G2 PROOF.md §1 (μ*, Theorem B*(i)).

## Verdict

**ACCEPT WITH FIXES.** The mathematics is correct. Every step of R1W and RW checks out, and the crux (R1W step 4)
is sound. The fixes are presentation and labelling: one normalisation slip in the constant claimed for Conjecture
R's form (F1), a sign typo (F2), an overclaim in remark RW-d (F3), notation (F4), and status bookkeeping (F5–F6).
None of them affects the theorem as stated.

## Checks performed

1. **R1W steps 1–3 (restricted telescoping, moduli, recurrence).**
   - Step 1: J·D_N = (μ_N − μ_{N−J}) + Σ_{m=N−J+1}^{N}(D_N − D_m). Each D_N − D_m = Σ_{j=m+1}^{N}Δ²μ_j uses only
     j ∈ [N−J+1, N], which is exactly the hypothesis. This gives ‖D_N|_S‖₁ ≤ 2/J + (J−1)η/2 and
     ‖D_{N−1}|_S‖₁ ≤ 2/J + (J+1)η/2 ≤ δ + δ(J+1)/(2J²) ≤ 2δ. Verified.
   - Step 2 is the restriction of R1 step 2 to S. Verified.
   - Step 3: I re-derived the claim |q_{N−1}|·||t_k| − b_N| ≤ b_{N−1}|e_k| + b_N|e′_k| from
     b_N q_N = (x − a_{N−1})q_{N−1} − b_{N−1}q_{N−2}. This is the orthonormal recurrence with b_n² = h_n/h_{n−1}, the
     same as the Lanczos convention in check_rw.py. The cases q_{N−1}(k) = 0 and q_{N−2}(k) = 0 are handled
     correctly.
   - Also in step 3: ||t| − b_N| = dist(t, {±b_N}) ≥ dist(x_k − a_{N−1}, {±b_{N−1} ± b_N}). Squaring with
     (α+β)² ≤ 2α² + 2β² and b_{N−1}, b_N ≤ b̄ gives (∗) with constant 2(2δ + 2δ) = 8δ = c_W/4. Verified. This is
     sharper than R1's 16b̄²δ and consistent with it.
2. **R1W step 4, the crux.** The question was how weak convergence (all of μ_m, μ_{m−1}, μ_{m−2} tend to the same
   arcsine law) can give a nonzero lower bound for ‖Δ²μ|_W‖₁. The answer is that it does not do so directly.
   - Steps 1–3 turn "‖Δ²μ_m|_S‖₁ < η for all m ∈ [N−J+1, N]" into a statement about the single measure μ_{N−1}
     restricted to S: it concentrates near the 3–4-point set Z_N in the variable y = (x − a_{N−1})/b̄. That is (∗).
     The recurrence carries the information that links the different indices, exactly as in R1 steps 1–3.
   - Step 4 needs only the weak limit of the one measure μ_{N−1}. That limit is absolutely continuous (arcsine on
     [0, 4c]), so its mass on supp h ⊂ I_W cannot sit near the 3 preimages of Z.
   - Quantitatively, the image of dθ/π under θ ↦ 2c(1 + cos θ), composed with φ(Y) = (Y − 2c)/c, is 2cos θ. Hence
     ∫_{I_W}dist(φ, Z)²dν = (1/π)∫_{Θ_W}dist(2cos θ, {−2,0,2})²dθ = c_W. This explains the definition of c_W and Θ_W,
     and why dist(2cos θ, {−2, 0, 2})² appears: Z = lim{±b_{N−1}/b̄ ± b_N/b̄} = {−2, 0, 2}.
   - Checked in detail:
     - y_k = φ_N(Y_k) with n = N−1.
     - n^pa_{N−1} → 2c and n^pb̄ → c (LP-w; bounded index shifts).
     - Uniform convergence of dist(φ_N, Z_N)² on compacts, via 1-Lipschitz dist and the Hausdorff convergence
       Z_N → Z.
     - The moving window: S ⇔ Y_k ∈ [(n/(bN))^p, (n/(aN))^p] → [b^{−p}, a^{−p}]. Since supp h is compact in the
       open I_W, h(Y_k) ≤ 1_S(k) for every atom once N is large, so the lower bound needs no continuity-set
       argument.
     - G_N → G uniformly on [0, ∞). ∫G dν_n → ∫G dν ≥ c_W/2 > c_W/4.
   - Conclusion: the argument is correct, and it is cleaner than R1 step 4 (no moments, no Cauchy–Schwarz, explicit
     δ).
3. **Lemma LP-w.** The LP proof (§3.8, REVIEWED) does establish weak convergence of ν_n, by the method of moments
   with a compactly supported limit. The limits n^pa_n → 2c and n^pb_n → c are the inputs to LP. Correct as a
   restatement.
4. **Admissibility, c_W > 0, Lemma u_s.**
   - I_W ≠ ∅ ⇔ b^{−p} < 4c ⇔ b > u_s (a < b gives b^{−p} < a^{−p}). Θ_W is open and non-empty, and the integrand
     vanishes only at θ ∈ {0, π/2, π}, so c_W > 0. Verified.
   - Lemma u_s: G2 Theorem B*(i) gives μ*_u density 1 on (0, u_s]. With g(u) = u^{−p} this is μ*([4c, ∞)) = u_s, so
     u_s = 1 − μ*((0, 4c)).
   - The lower bound μ*((0, 4c)) ≥ ½·(2/π)arcsin(2^{−p/2}) follows from μ* = ∫_0^1ω_{β_t}dt with β_t = 4ct^{−p}
     (G2 §1 Definition). Correct.
   - The B*(i) proof is a direct density computation that does not use (P), consistent with the RH_p row.
   - [0.6, 1.6] is admissible for all p because b = 1.6 ≥ 1 > u_s. Correct.
5. **Theorem RW, step 1 (R2 along the direct path).**
   - Lemma R2 is stated for every bounded f and every v with finite moments. Its proof uses only the ℓ² projection
     structure, so f with infinitely many windows is fine.
   - Smoothness in t: the Heine series argument of FV / T3-conv step 1.
   - The constant used is R2's stated 16, so the Taylor remainder is ∫_0^1(1−t)F″ ≥ −8ε². Correct. (R2's proof gives
     8, hence 4ε² and ε₀ = η_W/8; RW-e(6) notes this correctly.)
   - Remark RW-c is right: only the linear term needs localisation, and it is evaluated at v. This removes the
     sandwich-uniform tail bound (TL) that Theorem R needed.
6. **Theorem RW, step 2 (sign choice and own window).**
   - m_i ∈ [N_i − J_W + 1, N_i] is exactly R1W's range, and W_i = W_{N_i} is R1W's window. So
     ⟨f1_{W_i}, Δ²μ^v_{m_i}⟩ = ε‖Δ²μ^v_{m_i}|_{W_i}‖₁ ≥ εη_W exactly, with no o(1).
   - The pointwise ±1 sign function makes the sign(0) convention irrelevant.
   - Cross-window coefficients (1, 2, 1). Correct.
7. **Step 3 (head, Sat_p⁺).**
   - m′ ∈ [N_i − J_W − 1, N_i], and m′ ≥ N_i/2 ⇔ N_i ≥ 2J_W + 2. Verified.
   - Case (B): k ≤ bN_{i−1} < bN_i/R_W ≤ 2bm′/R_W ≤ θ₁m′. Verified.
   - μ_{m′} ≤ 1 − ρ_{m′}, then Sat_p⁺ with W = ζ(s), w_k = k^{−s}, ((m′+1)/k)^{2(1−p)₊} ≤ (m′+1)², and g_p⁺ ≥ 1.
     This gives ≤ ζ(s)(m′+1)^{s+3}e^{−2m′}. Verified (same pattern as T3-conv step 3).
8. **Step 4 (tail, LP), including uniformity over the infinitely many windows above scale i.**
   - T_i = ∪_{j>i}W_j ⊂ [aN_{i+1}, ∞) ⊂ (Mm′, ∞). So the whole future is bounded by one tail mass,
     μ_{m′}((Mm′, ∞)), and no uniformity over windows is needed.
   - LP's limit holds as n → ∞ through all integers, so it holds along n = m′(i) → ∞.
   - (A): M is arbitrary, so the limit is 0. (B): aR_W ≥ M_W, so limsup ≤ F_p(M_W).
   - F_p(M_W) = η_W/16 checked analytically and numerically (16F_p(M_W)/η_W = 1.0000).
   - limsup E_i ≤ 4ε·η_W/16 = εη_W/4. Verified.
9. **Step 5.**
   - 8ε² ≤ εη_W/2 ⇔ ε ≤ η_W/16. The arithmetic for (A) and (B) is correct, and F_m(v) → 0.
   - The (T3) conclusion follows from the §2 definition of ω(δ) (index m = n+1 ∈ [n, (1+δ)n]), and the bound
     |r − 1| ≥ 1 − e^{−c′/2} is correct. One sign typo; see F2.
10. **Numerical constants (independent quadrature, scipy.quad with a breakpoint at π/2).**
    - p = 2, W = [0.6, 1.6], c(2) = π²/16:
      - c_W = 0.2344521
      - J_W = 273
      - η_W = 9.8306·10⁻⁸
      - ε₀ = 6.1441·10⁻⁹
      - M_W = 6.596·10⁷
    - All match check_rw.out [1]. u_s(2) = 2/π. R_W = M_W/a ≈ 1.099·10⁸ matches.
11. **Numerics reproduced.**
    - The command `.venv/bin/python ../ja-plan39/research/G1/checks/check_rw.py` from jacobi-asymptotics took
      73 s, and its output is byte-identical to check_rw.out.
    - The quoted figures in §3.10 RW-f and LOG check out: Q_N, window norms 1.06–1.09, linear match ≤ 2% (worst 1.8%),
      cross-window ≤ 1.4·10⁻³, off-spike maxima, and K-doubling ≤ 10⁻³.
    - Caveats, correctly disclaimed: [3] chooses m_i by maximising over [N−3, N], not by R1W's rule; the top scale
      has no tail windows; ε ≫ ε₀.
12. **Plan doc Review focus.** Every item has been gone through: items 1–9 above, plus labels below. T7 remains
    open until fixes are applied.

## Findings

**F1 (Medium; Corollary RW′ last sentence; "What is and is not proved", first bullet; §0 RW row wording).**
- **Issue.** The constant "c = η_W/2 ≈ 4.9·10⁻⁸" is quoted as Conjecture R's c. Conjecture R (§3.2) is stated for
  |β_n/β_{n−1} − 1| ≥ cε, but η_W/2 is the constant for |log(β_n²/β_{n−1}²)|.
- From limsup |log(β²_m/β²_{m−1})| ≥ εη_W/2 one gets only |β_m/β_{m−1} − 1| ≥ 1 − e^{−εη_W/4}, which is
  ≥ (η_W/4)(1 − ε₀η_W/8)·ε. So in Conjecture R's normalisation c ≈ η_W/4 ≈ 2.5·10⁻⁸ in case (A), and ≈ η_W/8 in
  case (B). The claim is off by a factor of 2.
- **Fix.** State the normalisation explicitly. For example: "c = η_W/5 ≈ 2.0·10⁻⁸ in Conjecture R's normalisation
  (case (A); η_W/9 in case (B)); η_W/2 for |log(β_n²/β_{n−1}²)|." In the "What is proved" bullet, say "explicit c
  (η_W/2 for log β², about η_W/4 for |β_n/β_{n−1} − 1|)".

**F2 (Minor; Theorem RW proof step 5).**
- **Issue.** "log(β_m²/β_{m−1}²) = F_m(w) − 2p·log(m/(m − 1))" has the wrong sign. Since β_m = m^pb_m/c, the correct
  identity is log(β_m²/β_{m−1}²) = F_m(w) + 2p·log(m/(m−1)). This matches §3.6 step 4, where
  F_N(v) ≈ −2p log(N/(N−1)).
- Harmless, because the term → 0.
- **Fix.** Change − to +.

**F3 (Minor; remark RW-d).**
- **Issue.** The remark says that if b ≤ u_s then "‖Δ²μ_m^v|_{W_N}‖₁ → 0 exponentially fast (Sat_p⁺)". Sat_p⁺ gives
  exponential smallness only where g_p⁺(k/m) > 0, i.e. k/m < θ₀(p). Here θ₀(p) is the zero of g_p⁺: ≈ 0.056, 0.218,
  0.315, 0.427 for p = 0.5, 1, 2, 4, strictly below u_s = 0.375, 0.5, 0.637, 0.763.
- For θ₀ < b ≤ u_s the vanishing follows from LP-w (ν has no mass beyond 4c and no atom at 4c) and is only o(1),
  not exponential. The conclusion (first-order gain → 0, c_W = 0) is still correct.
- **Fix.** Replace the remark with: "then μ_m^v(W_N) → 0 for m − N = O(1) (LP-w; exponentially fast when
  b < θ₀(p), by Sat_p⁺), so ‖Δ²μ_m^v|_{W_N}‖₁ ≤ 4 max μ(W_N) → 0 and c_W = 0."

**F4 (Minor; Theorem RW statement; §0 RW row).**
- **Issue.** "s_i := sign(Δ²μ_{m_i}^v)" reads as a scalar, but it must be the pointwise sign function
  k ↦ sign(Δ²μ_{m_i}^v(k)), as in Theorem R. Step 2's identity depends on this.
- **Fix.** Write s_i(k) := sign(Δ²μ^v_{m_i}(k)), and f = ε Σ_i s_i 1_{W_i} pointwise.

**F5 (Minor, labels; §3.10 header, §0).**
- **Issue.** Lemma u_s and Lemma LP-w carry no status label, and the §0 RW row lists "G2 B*(i)" as an internal
  input. G2's B* row is PROVED-mod-cite (P) as a whole, and only (i)–(ii) are (P)-free.
- **Fix.**
  - Label Lemma u_s as PROVED (internal: G2 B*(i), which does not use (P)).
  - Label LP-w as PROVED-mod-cite (restatement of LP; REVIEWED).
  - In the §0 RW row, write "G2 B*(i) ((P)-free)".
  - Also state "for N ≥ N₀" in the inline R1W statement in the §0 row.

**F6 (Minor, stale text; §0 Conj R row; §3.2 Conjecture R paragraph and §3.2 header).**
- **Issue.** The undated sentences "The [0.6N, 1.6N]-window form remains NUMERICAL" (§0 row, and §3.2 "… would need
  localization at scale Mn and remains NUMERICAL (F2)") now sit directly before a dated pointer saying it is proved.
  The §3.2 header still reads "Conjecture R NUMERICAL (proved in modified form, §3.6)".
- **Fix.** Qualify the old sentences ("as of Plan 33" / "superseded by Plan 39 for ε ≤ ε₀"). Amend the §3.2 header
  to "… (modified forms proved: §3.6, §3.10)".

**F7 (Info; RW-e(6), Theorem RW step 1).** R2 is applied with its stated constant 16, giving 8ε². That is consistent
and correct. No fix needed. Optionally note in the statement that ε₀ = η_W/8 is available from R2's proof.

**F8 (Info; header label "Conjecture R in window form").**
- The title is acceptable given the explicit "What is and is not proved" list.
- The proved statement differs from Conjecture R as posed in three ways: ε ≤ ε₀ ≈ 6·10⁻⁹ only (not every ε);
  c depends on (p, a, b) (absolute for fixed p = 2, W = [0.6, 1.6], which is the conjecture's setting, so this is
  fine); and the separation is ×R_W ≈ 1.1·10⁸, or → ∞.
- **Suggestion.** Add "for ε ≤ ε₀" to the §3.10 header and the §0 Conj R pointer (the latter already says so).

## Recommended labels (after F1–F6 are applied)

- Lemma u_s: PROVED (internal G2 B*(i), (P)-free) — REVIEWED.
- Lemma LP-w: PROVED-mod-cite (= Lemma LP) — REVIEWED.
- Lemma R1W: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b via LP-w) — REVIEWED.
- Theorem RW and Corollary RW′: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, R2, LP, Sat_p⁺, G2 B*(i)) —
  REVIEWED; novelty UNCHECKED.
- Conjecture R: "window form (incl. [0.6N, 1.6N]) PROVED-mod-cite for ε ≤ ε₀ with separation → ∞ or ×R_W; every-ε
  with absolute c, and ×4 separation, NUMERICAL". This matches the current text, modulo F1 and F6.
- The plan's T7 can be ticked once the fixes are applied. A light re-check suffices.

## Re-check (fix commit e20b84f; diff f425b7b..e20b84f)

**Verdict: ACCEPT.** All findings are resolved. Nothing blocking remains.

- **F1 (resolved, and better than the suggested fix).** The author did not use my η_W/5 and η_W/9. Instead they
  argue that the spikes are one-signed and conclude c = η_W/4 (A) and η_W/8 (B). I checked the one-signedness claim
  in detail:
  - The sign function s_i(k) = sign(Δ²μ^v_{m_i}(k)) makes the own-window term +ε‖Δ²μ^v_{m_i}|_{W_i}‖₁ ≥ εη_W.
    It is a signed quantity, not an absolute value.
  - Steps 1–5 give a signed lower bound for F_{m_i}(w): the Taylor bound F(1) ≥ F(0) + F′(0) − 8ε² holds with signs,
    and |E_i| enters with a minus. So liminf_i F_{m_i}(w) ≥ c′ > 0, which is what the theorem already stated.
  - log(β_m²/β_{m−1}²) = F_m(w) + 2p log(m/(m−1)) ≥ F_m(w), since the correction term is positive after the F2 fix.
    Hence liminf_i log(β_{m_i}/β_{m_i−1}) ≥ c′/2.
  - Therefore limsup_n (β_n/β_{n−1} − 1) ≥ e^{c′/2} − 1 ≥ c′/2. That is εη_W/4 in case (A) and εη_W/8 in case (B).
  - Corollary RW′, the "What is proved" bullet and the §0 RW row now state both normalisations consistently.
    Values: η_W/4 ≈ 2.46·10⁻⁸ and η_W/8 ≈ 1.23·10⁻⁸ at p = 2.
  - Cosmetic: step 5 cites "c′ as below" before defining it. The ω(δ) line still uses the weaker
    1 − e^{−c′/2}, which is valid.
- **F2 (resolved).** The sign is now +.
- **F3 (resolved).** RW-d now uses LP-w (no mass beyond 4c and no atom at 4c) for the o(1) statement. It claims
  exponential decay only for b < θ₀(p), and the θ₀ values match my computation. The bound ≤ 4 max μ_{m′}(W_N) is correct.
- **F4 (resolved).** s_i(k) is pointwise, both in the statement and in the §0 row.
- **F5 (resolved).** The labels are in place:
  - Lemma u_s: PROVED, with B*(i) noted as (P)-free.
  - LP-w: PROVED-mod-cite.
  - The §0 row now says "for N ≥ N₀" and "G2 B*(i) ((P)-free)".
- **F6 (resolved).** The stale sentences are now dated "as of Plan 33", with "superseded by Plan 39 for ε ≤ ε₀" in
  §3.2. The §3.2 header now reads "modified forms proved: §3.6, §3.10".
- **F7.** No change, as recommended. RW-e(6) records this.
- **F8 (resolved).** The §3.10 header now says "for ε ≤ ε₀".
- **Remaining (optional, non-blocking).** Swap the order of the c′ definition and its use in step 5.

**Final labels.**
- Lemma u_s: PROVED — REVIEWED.
- Lemma LP-w: PROVED-mod-cite — REVIEWED.
- Lemma R1W: PROVED-mod-cite — REVIEWED.
- Theorem RW and Corollary RW′: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, R2, LP, Sat_p⁺, G2 B*(i)
  (P)-free) — REVIEWED; novelty UNCHECKED.
- Conjecture R: the window form (incl. [0.6N, 1.6N], all p > 0, s > 1) is PROVED-mod-cite for ε ≤ ε₀, with
  separation → ∞ (c = η_W/4) or ×R_W (c = η_W/8). The every-ε form with an absolute c, and ×4 separation, remain
  NUMERICAL.
- The "re-check pending" strings in the §0 rows, the §3.2 pointer, the §3.10 header, LOG and plan T7 can be updated to
  "re-check ACCEPT — REVIEWED", and T7 ticked.
