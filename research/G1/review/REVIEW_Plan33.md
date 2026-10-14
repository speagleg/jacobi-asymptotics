# Rule R review: Plan 33 (Lemma R2, Lemma R1, Theorem R)

Reviewer: independent Rule R pass, 2026-10-14. Target: worktree `ja-plan33`, branch `plan-33-thmR`, commit e3f12bd.
Scope: research/G1/PROOF.md §3.6 (Lemma R2, Lemma R1, Theorem R, Remarks R-a to R-d), the status row "Thm R", the
Conjecture R pointer edit in §3.2, the LOG Plan-33 entry, and docs/superpowers/plans/2026-10-14-plan-33-thmR.md
(Review focus). Context read: §3.2 (FV), §3.3 (Sat_p⁺, T3-conv), §3.4 (TL, T3-sv), §3.5 (FVa), §2 (G1-T and the
definition of (T3)), §4, the status table, and REVIEW_Plan32.md (index conventions of RH_px, RH₁(r) and RH_plt1b).

## Verdict

**ACCEPT WITH FIXES.** I redid every step of R2, R1 and Theorem R and found no mathematical error. The argument is
sound, and the constants hold (16 in R2 is valid; 8 also works). The fixes concern scope:
- one overclaim: Theorem CL "still holds" for all p, but CL is proved only for p > 1 (F1);
- "Conjecture R PROVED", when the theorem proves a modified form (F2);
- "G1-R is FALSE", which needs scoping, and the stale "conjectural" text it leaves elsewhere (F3);
- a LOG merge artifact (F4);
- minor presentation points in the proofs (F5–F9).

## Independent checks done

1. **Lemma R2.**
   - Var formula: ½Σ(f_k − f_l)²K_m(k,l)² is §3.5 step 3 with g = f. Correct.
   - Rank-one update: Var_{m+1} − Var_m = A + B, with the entrywise identity K_{m+1}² − K_m² = 2K_mq_mq_m + q_m²q_m².
     Correct.
   - K_mq_m = 0: K_m = Σ_{j<m}q_jq_jᵀ, and the q_j are orthonormal in ℓ²(atoms) (Σ_kw_kp_ip_j(x_k) = δ_ij). So K_mq_m
     = Σ_jq_j⟨q_j,q_m⟩ = 0 exactly. It is the orthogonal projection onto span{q_0..q_{m−1}}.
   - Absolute convergence: Σ|K(k,l)||q_m(k)||q_m(l)| ≤ ‖K‖_HS·‖q_m‖² = √m. So the rearrangement is legitimate.
   - The f_k² and f_l² parts vanish, and A = −2⟨fq_m, K_m(fq_m)⟩ ∈ [−2‖f‖², 0], since 0 ≤ K_m ≤ I and ‖fq_m‖₂ ≤ ‖f‖_∞.
     Correct.
   - B = Var_{μ_m}(f) ∈ [0, ‖f‖²_∞]. The stated bound 2‖f‖² is valid but loose.
   - Index bookkeeping: log b_n² = L_{n+1} − 2L_n + L_{n−1} (FV). So F_N = L_{N+1} − 3L_N + 3L_{N−1} − L_{N−2}, and
     F_N'' = δ_N − 2δ_{N−1} + δ_{N−2} with δ_m := Var_{m+1} − Var_m. Correct.
   - Since |δ_m| ≤ 2‖f‖², we get |F_N''| ≤ 8‖f‖². The stated 16 is valid (see F5).
   - Numerical check (reviewer, p = s = 2, N = 60, K = 1200, float64 Lanczos with full reorthogonalization, second
     differences with h = 10⁻²). Over t ∈ [−2, 2], max|F_N''| is:
     - 2.89 for f = sign(Δ²μ_N);
     - 0.72 for random ±1;
     - 0.33 for sign·cos k.

     All are well within 8.
2. **Lemma R1.**
   - **Step 1.** D_N − D_m = Σ_{m′=m+1}^{N}Δ²μ_{m′}, with at most J terms, all in [N−J+1, N]. So it is ≤ Jη.
     - Σ_{m=N−J+1}^{N}D_m = JD_N − Σ(D_N − D_m), so J‖D_N‖ ≤ 2 + J²η. Correct.
     - With J = ⌈2/δ⌉ and η = δ/J², ‖D_N‖ ≤ δ + δ/J ≤ 2δ.
     - ‖D_{N−1}‖ ≤ ‖D_N‖ + η, which is still ≤ 2δ for J ≥ 2. The text's "the same holds" glosses this (F6).
   - **Step 2.** (|a| − |b|)² ≤ |a² − b²| holds termwise. The worst pair is N vs N−2, with ≤ 4δ. So ‖e‖₂, ‖e′‖₂ ≤ 2√δ.
     Correct.
   - **Step 3, redone.**
     - The recurrence xq_{N−1} = b_Nq_N + a_{N−1}q_{N−1} + b_{N−1}q_{N−2} follows from the §3.5 convention. Correct.
     - Write s_k = sign q_{N−1}(k). Then q_{N−2} = σ_kq_{N−1} + σ_ks_ke_k, so
       b_Nq_N = (x − a − b_{N−1}σ)q_{N−1} − b_{N−1}σse, and the pointwise inequality follows.
     - With |q_N| = |q_{N−1}| + e′, this gives (|x − a − bσ| − b_N)|q_{N−1}| = b_Ne′ − r with |r| ≤ b_{N−1}|e|.
       Squaring and summing gives ≤ (2√δ·b_N + 2√δ·b_{N−1})² ≤ 16b̄²δ. Correct.
     - ||u| − c| = dist(u, {±c}) for c ≥ 0. So the bound is ⟨dist(y, Z)², μ_{N−1}⟩ ≤ 16δ with Z = {±β′ ± β}. Correct.
     - Zeros: if q_{N−1}(k) = 0, the atom has weight 0. If q_{N−2}(k) = 0 and q_{N−1}(k) ≠ 0, the identity holds for
       either choice σ_k = ±1, and σ_k = 0 (literal sign) would break the Z-membership. Choose σ_k ∈ {±1} (F6).
   - **Step 4.**
     - m_j = b̄^{−j}((J − a_{N−1})^j)_{N−1,N−1} is exact: x^jp_{N−1} is a polynomial, expanded in p_0..p_{N−1+j} by
       finitely many recurrence steps. Determinacy is not needed.
     - The entries involved are (a_m − a_{N−1})/b̄ → 0 (since a_m/(2b_m) → 1 and b_m/b_N → 1 for bounded |m − N|) and
       b_m/b̄ → 1. These hold for all p > 0 by RH_px, RH₁(r) and RH_plt1b (index conventions checked in
       REVIEW_Plan32).
     - The deep diagonal moments of the free matrix are the central binomials 2, 6 and 20, so m₄ − 4m₂ → −2. Correct.
     - |P(y) − P(z)| ≤ |y − z|·sup|P′| with |P′(ξ)| ≤ C(1 + |ξ|³) ≤ C′(1 + |y|³) for |z| ≤ 2. Adding the Hausdorff
       distance between Z and {−2, 0, 2} gives the stated bound, both near and far from Z.
     - Cauchy–Schwarz: ⟨(d + o(1))²⟩^{1/2} ≤ 4√δ + o(1), and ⟨(1 + |y|³)²⟩ ≤ 2(1 + m₆). Correct.
     - Quantifiers: δ is fixed (absolute, small enough that 4C√δ·√42 < 1, say). Then J and η are fixed, and every o(1)
       depends only on N. So infinitely many bad N give a contradiction, and N₀ exists. Correct.
   - **Numerical sanity check** (reviewer, p = s = 2, K = 20N, float64 Lanczos with full reorthogonalization):

     | N | ‖Δ²μ_m‖₁, m ∈ [N−6, N] | ‖D_N‖₁ | m₂, m₄, m₆ | m₄ − 4m₂ | ⟨dist(y,Z)², μ_{N−1}⟩ |
     |---|---|---|---|---|---|
     | 50 | 1.15–1.40 | 0.78 | 1.923, 5.581, 18.24 | −2.110 | 0.236 |
     | 100 | 1.19–1.36 | 0.84 | 1.961, 5.775, 18.96 | −2.067 | 0.246 |
     | 200 | 1.23–1.33 | 0.78 | 1.980, 5.884, 19.44 | −2.037 | 0.250 |

     - The moments converge to 2, 6 and 20, and m₂ agrees with (b_{N−1}² + b_N²)/b̄² to all printed digits.
     - The concentration is bounded away from 0, exactly as the mechanism requires.
     - Numerically every N is good (J = 0 would do).
3. **Theorem R.**
   - **Windows.** θN_{i+1} > N_i^γ·i gives the following:
     - W_j ⊂ [1, N_{i−1}^γ] ⊂ [1, θN_i) for j < i, using i − 1 ≥ 1;
     - W_j ⊂ [θN_{i+1}, ∞) ⊂ (N_i^γ, ∞) for j > i.

     The windows are disjoint, so |f| ≤ ε and w ∈ [e^{−ε}, e^{ε}]·v.
   - **Gain.** F(ve^{f_i}) − F(v) ≥ F′(0) − ½·sup|F″| ≥ ε‖Δ²μ^{(v)}|_{W_i}‖₁ − 8ε². Correct.
     - The signs come from v, and the first derivative is taken at v. Only the remainder is controlled along the path,
       so there is no circularity.
   - **Head (μ_N, μ_{N−1}, μ_{N−2} of v).** For k < θN and m ≥ N − 2, k/m ≤ θN/(N−2) ≤ 2θ for N ≥ 4. So Sat_p⁺
     gives total mass ≤ C·N^{s+1}(N+1)²e^{−2(N−2)} → 0.
   - **Tail.** μ_{N−2} ≤ ρ_{N−1} ≤ ρ_{N+1}, so Lemma TL at n = N covers all three. The TL exponent at T = N^{κ+1} is
     T″^sT^{1−s} ≍ N^{−(s−1)} → 0. Correct.
   - **Cross-scale step.** The path is ve^{f_i + t(f − f_i)}. It stays in the sandwich [e^{−ε}, e^{ε}]v, where Sat_p⁺
     (W/w_k ≤ e^{2ε}ζ(s)k^s) and TL (C/c = e^{2ε}) are uniform. FV with direction f − f_i, supported in head ∪ tail,
     gives o(1). Correct.
   - **Conclusion.** F_{N_i}(w) ≥ F_{N_i}(v) + εη − 8ε² − o(1). log(β_N²/β_{N−1}²) = F_N + 2p log(N/(N−1)), and
     F_N(v) → 0. So limsup ≥ εη/2 for ε ≤ η/16, stronger than the stated εη/4.
   - **(T3) fails.** By §2, (T3) is ω(δ) = limsup sup_{n≤m≤(1+δ)n}|β_m/β_n − 1| → 0. Taking m = N_i and n = N_i − 1 gives
     ω(δ) ≥ e^{εη/4} − 1 > 0 for every δ. So (T3) fails, β_n does not converge, and the pointwise b-law fails
     directly; G1-T is not even needed.
   - **H_all** needs Σw < ∞ and w_k ≥ c₁k^{−s}, both of which hold.

## Findings

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| F1 | Medium | §3.6 Theorem R statement ("H_all and Theorem CL still hold for w"); §3.2 Conjecture R bullet; R-a ("Averaged laws (H_all, CL) survive all sandwiched roughness") | Theorem CL is proved only for **p > 1** (status row CL; §4: "(CL) … open for general nodes or p ≤ 1"). Theorem R is stated for all p > 0, so the claim overreaches for 0 < p ≤ 1. | Write "H_all still holds for w, and Theorem CL too when p > 1". Same in R-a. |
| F2 | Medium | Status row "Thm R"; §3.2 pointer "now proved … as Theorem R"; §3.6 header; LOG | Conjecture R as stated says (a) every ε > 0, (b) c absolute, (c) windows [0.6N_i, 1.6N_i]. Theorem R proves (a′) ε ≤ ε₀ = η/32 (for larger ε the bound is c·min(ε, ε₀)), (b′) c = η/4 with η non-explicit, depending on p and s, and (c′) windows [θN_i, N_i^{κ+1}]. Windows of width O(N) would need localization at scale Mn, which is OPEN (TL2). So it is a proof of Conjecture R *in a modified form*, not verbatim. | Say "Conjecture R proved in the following form" and list (a′)–(c′). Note that the [0.6N, 1.6N]-window form remains open (it needs Mn-localization). Write c := η/4 (or η/2; see F7) in the status row. |
| F3 | Medium | R-a and LOG ("G1-R as posed in §4 is therefore false"); status rows G1-R and Conj R; §4 (two places); §3.2 "If Conjecture R holds" and "None of these is done here"; §3.3 T3c1 | **(i) Scope.** G1-R = "(T3) from the atoms alone; (CL) …". Theorem R refutes only the (T3) half, as an implication from (H-a) plus the weight conditions; even two-sided sandwiched weights do not suffice. The (CL) half (general nodes, p ≤ 1) is untouched. **(ii) Stale text.** Several places still describe Conjecture R as conjectural. | (i) Write "the (T3) half of G1-R, as an implication from (H-a) and sandwiched weights, is FALSE (Theorem R); positive (T3) results need regularity of Ψ (T3-conv, T3-sv)". (ii) Update the G1-R row (no longer GAP for (T3): REFUTED by Thm R; (CL) part unchanged) and the Conj R row (→ PROVED in modified form, §3.6). Update §4 "conjecturally breaks it (Conjecture R)" and "(T3) is conjecturally FALSE". Add "(done: §3.6)" pointers to §3.2's "What a proof needs" (iii)/(i)/(ii) and the F6 re-scoping bullet. Update §3.3 T3c1 ("conjecturally"). |
| F4 | Low | research/G1/LOG.md, Plan-32 entry | A merge artifact: a stray "- **Rule R:** pending." follows "Re-check: ACCEPT … REVIEWED." in the Plan-32 entry. | Delete that line. |
| F5 | Low | Lemma R2, "Bound on B" and "Combine" | The bounds give |δ_m| = |A + B| ≤ 2‖f‖² (A ∈ [−2,0]‖f‖², B ∈ [0,2]‖f‖²). The second difference (coefficients 1, −2, 1) then gives |F″| ≤ 8‖f‖². The text's "4·4" does not match its own bounds. Also B = Var_{μ_m}(f) ≤ ‖f‖². 16 is valid. | Write "|F_N''| ≤ 4·2‖f‖² = 8‖f‖² ≤ 16‖f‖²". Optionally sharpen B, and use 8 to get limsup ≥ εη − 4ε². |
| F6 | Low | Lemma R1, steps 1, 3, 4 | (a) Step 1: ‖D_{N−1}‖ ≤ ‖D_N‖ + η, not "the same". It is still ≤ 2δ for J ≥ 2. (b) Step 3: σ_k must be in {±1}. Fix σ_k := +1 when q_{N−1}(k)q_{N−2}(k) = 0. With σ_k = 0 the inequality holds but y ∉ Z-structure. (c) Step 4: the trailing "·C′" should read ⟨(1 + \|y\|³)²⟩^{1/2} ≤ (2(1 + m₆))^{1/2}. (d) Name clash: J is both the integer window length and the Jacobi matrix. | (a)–(c) one-line edits. (d) Rename the integer J to, say, L (in R1 and in Theorem R step 1). |
| F7 | Low | Theorem R statement and step 4 | (a) The proof gives ≥ εη/2 − o(1), so limsup ≥ εη/2. εη/4 is fine but weaker. (b) ε₀ = η/32 in the statement vs "ε ≤ η/16" in step 4: consistent but unexplained. (c) F_N(v) = −2p log(N/(N−1)) + O(1/N): the first term is absorbed by the O(1/N). Only F_N(v) → 0, i.e. b_N/b_{N−1} → 1, is used. (d) The ε of Lemma TL (tail tolerance) clashes with the roughness ε. | (a, b) State limsup ≥ εη/2 for ε ≤ η/16 (and drop ε₀ or set ε₀ := η/16). (c) Write "F_N(v) → 0 (b_N/b_{N−1} → 1 by RH)". (d) Call the TL tolerance ε′. |
| F8 | Low | Theorem R step 2 (head/tail) | The proof is correct but compressed. It does not say that Sat_p⁺ needs k < m and k/m ≤ 2θ for all three m ∈ {N, N−1, N−2} (true for N ≥ 4 as k < θN ≤ 2θ(N−2)), or that TL covers μ_{N−2} via μ_{N−2} ≤ ρ_{N−1} ≤ ρ_{N+1}. | Add these two clauses. They are also what step 3 uses along the path, with sandwich constants e^{±ε}. |
| F9 | Low | §3.6 header; status row; labels | R1 and R2 have no labels of their own. R2 also depends on the two-point formula of §3.5 step 3 (from the proof of Lemma H), which is internal. | Header: "Lemma R2 PROVED (self-contained given §3.5 step 3); Lemma R1 PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); Theorem R PROVED-mod-cite". Add "FVa step 3" to the internal list in the status row. |
| F10 | Info | R-d; README | Novelty is UNCHECKED, and R-d gives no concrete pointers. Pointers to check (recollection, unverified; Citation gate): (i) Lubinsky's counterexamples to Freud's conjecture for *non-smooth* exponential weights e^{−\|x\|^α}·h with h bounded between positive constants. If correctly recalled, this is the closest analogue: bounded multiplicative roughness destroying the asymptotics of the recurrence coefficients. (ii) Lubinsky's "jump distributions on [−1,1]" with prescribed leading-coefficient behaviour. (iii) Máté–Nevai–Totik ratio-asymptotics and comparison theorems. (iv) Simon, *Szegő's Theorem and Its Descendants*. The README has not been updated for Plan 33. | Add these to R-d as pointers to check. Update the README when merging (state the dichotomy, and that the (T3) half of G1-R is refuted). |

## Recommended labels (after fixes)

- **Lemma R2:** PROVED (self-contained given §3.5 step 3 / Lemma H proof); novelty not claimed.
- **Lemma R1:** PROVED-mod-cite (pure-power ratio and a-law asymptotics: RH_px, RH₁(r), RH_plt1b).
- **Theorem R:** PROVED-mod-cite (same citations; internal: FV, FVa step 3, Sat_p⁺, TL, Lemma H). It proves
  Conjecture R in modified form (F2). Novelty UNCHECKED (F10).
- **G1-R (T3) half:** REFUTED (Theorem R). The (CL) half is unchanged.
- REVIEWED once F1–F3 are applied. F4–F9 are editorial and can be checked at re-check.

Reviewer scripts (scratch, not committed): `p33rev/r1.py` (moments and ‖Δ²μ‖), `p33rev/r2.py` (F″ along paths).
