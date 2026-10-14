# Rule R review — Plan 40 (G1 PROOF.md §3.11: Lemmas LR, LR′, LRa; Corollary LR-law)

Reviewer: independent second reader (Rule R), 2026-10-14. Branch `plan-40-lr`, commit e01a0fc (`git diff master...HEAD`).
Read: AGENTS.md; §3.11 in full; §3.2 (Lemma FV), §3.5 (Lemma FVa, step 3), §3.6 (Lemma R2, Theorem R), §3.8 (Lemma TV);
G3′ §5.2 Lemma H (Gram/Sylvester proof); outline_C_rough §2.1 and §2.4 (3); §0 row; LOG entry; plan doc
`docs/superpowers/plans/2026-10-14-plan-40-lr.md`; `checks/check_lr.py` / `.out`.

## Verdict

**ACCEPT WITH FIXES.** All findings are minor or presentation. I re-derived every step of LR, LR′ and LRa and found no
error. The constants are correct, and numerically they are *sharp*: they are attained, not merely approached at 0.986.
The Corollary's logic is right. The Theorem R remark (ε₀ = η/4) is justified. The numerics reproduce exactly.

## Checks performed

**Step 0 (reductions, regularity).**
- Scale invariance holds: ve^{tf} = e^{tc}·ve^{tg}, and a constant factor leaves q_j, μ_j, a_j and b_j unchanged.
- L_n^v and L_n^{a,v} vanish on constants: Σμ_n = 1, ⟨x − a_n, μ_n⟩ = 0 and ⟨q_{n−1}, q_n⟩ = 0.
- Uniformity in t holds: w(t + h) = w(t)e^{hf}, and after centering w(t) ≤ e^{ε}v keeps the moments finite.
- The ℓ²-smoothness of √w(t)x^j uses only finite moments. The claim that TV's proof used x_k ≤ 1 only at this step is
  correct.
- The Heine sum has domination Π w_k(t)V(S) ≤ e^{m‖f‖}Π v_kV(S).
- The atom counts are adequate: LR needs n + 1 atoms, LRa needs n + 2, LR′ needs N + 1.

**Step 1.**
- log b_n² = L_{n+1} − 2L_n + L_{n−1}, using b_n² = D_{n+1}D_{n−1}/D_n².
- (d/dt)⟨f, μ_m⟩ = V_{m+1} − V_m, using ρ_{m+1} − ρ_m = μ_m.
- (log b_n²)″ = ΔV_n − ΔV_{n−1}.

**Step 2 (every term).**
- The rank-one update gives K_{m+1}² − K_m² = 2K_m(k,l)q_m(k)q_m(l) + q_m(k)²q_m(l)².
- In A_m, the f_k² part is Σ_k f_k²q_m(k)(K_mq_m)(k) = 0, because K_mq_m = 0 (q_m ⊥ range K_m). The f_l² part vanishes
  likewise. The cross part is −2⟨fq_m, K_m(fq_m)⟩ = −2‖K_m(fq_m)‖², since K_m is self-adjoint and idempotent.
- Absolute convergence holds: Σ|K_m(k,l)||q_m(k)||q_m(l)| ≤ Σ_{j<m}(Σ_k|q_j||q_m|)² ≤ m.
- B_m = Var_{μ_m}(f).
- **Bessel.** fq_m = K_m(fq_m) + α_mq_m + r, with r ⊥ q_0, …, q_m, and the three parts are pairwise orthogonal. So
  ‖K_m(fq_m)‖² ≤ ‖fq_m‖² − α_m² = Var_{μ_m}(f). This is correct, and no completeness is used: the residual r absorbs
  any non-density.
- Therefore ΔV_m ∈ [−B_m, B_m], |(log b_n²)″| ≤ B_n + B_{n−1} ≤ 2ε², and |F_N″| ≤ B_N + 2B_{N−1} + B_{N−2} ≤ 4ε².
- The TV cross-check, with 1_A replaced by f (linear in 1_A, f bounded), gives the same ΔV_m.
- m = 0: K_0 = 0, so ΔV_0 = B_0. Consistent.

**Step 3.** Taylor gives ∫(1 − t)·2ε² dt = ε² and ∫(1 − t)·4ε² dt = 2ε². The first derivatives at t = 0 come from FV.
Correct.

**Step 4.**
- ⟨(x − a_n)f, μ_n⟩ = ⟨fq_n, b_{n+1}q_{n+1} + b_nq_{n−1}⟩ = b_{n+1}γ_n + b_nγ_{n−1}. The recurrence holds pointwise at the
  atoms.
- With FVa this gives a_n′ = b_{n+1}γ_n − b_nγ_{n−1}. I checked this against the FVa form directly to 30 digits on
  random measures, including n = 0.
- Toda check: f = x gives γ_n = b_{n+1}.
- b_m′ = ½(α_m − α_{m−1})b_m, and |α_m − α_{m−1}| ≤ osc f = 2ε, so b_m(t) ≤ e^{εt}b_m(0). This follows from FV; it holds
  even without centering.

**Step 5.** I re-derived the formula.
- ⟨q̇_n, u′⟩ = ½⟨u,u′⟩ − S_n − ½α_nγ_n.
- ⟨u, q̇_{n+1}⟩ = ½⟨u,u′⟩ − S_n − α_nγ_n − ½α_{n+1}γ_n.
- ⟨u,u′⟩ = S_n + α_nγ_n + α_{n+1}γ_n + R_n, from the four-way orthogonal decomposition.
- The sum is γ_n′ = R_n − S_n + ½(α_{n+1} − α_n)γ_n. ✓

**Step 6.**
- a_n″ = b_{n+1}Γ_n − b_nΓ_{n−1}, with Γ_m = R_m − S_m + (α_{m+1} − α_m)γ_m. The b′-terms absorb the ½ factor. ✓
- Cauchy–Schwarz twice, then AM–GM: |R − S| ≤ ε² − γ² − ½(α_m² + α_{m+1}²).
- |γ|s ≤ γ² + s²/4, and s² ≤ 2(α_m² + α_{m+1}²). Hence |Γ_m| ≤ ε².
- This needs the centered f (‖u‖² ≤ ε²), which step 0 provides.
- ∫_0^1(1 − t)e^{εt}dt = (e^ε − 1 − ε)/ε², and e^ε − 1 − ε ≤ ½ε²e^ε since (j + 2)! ≥ 2·j!. ✓

**Corollary LR-law.**
- log β_n²(w) = (log b_n²(w) − log b_n²(v)) + log β_n²(v), so (i) follows from |limsup|X| − limsup|Y|| ≤ limsup|X − Y|.
- (ii): L_n^v(τf) = τL_n^v(f) and the osc-radius of τf is τε, so |E(τf) − τΛ(f)| ≤ τ²ε². Hence Λ = lim E(τf)/τ, and
  Λ = 0 ⟺ L_n → 0 (Λ is a limsup of |L_n|). The "iff" is correct. As the gaps paragraph says honestly, it is a
  statement about the τ-derivative at 0, not about the law for a fixed f.
- (iii): n^p(b_n + b_{n+1})(v) → 2c(p) follows from the b-law.
- The extension to other bases (T3-all, T3-log) is fine: those bases have finite moments, since x_k ≤ 1 and Σw < ∞.

**Remark LR-a (Theorem R, ε₀ = η/4).**
- In §3.6 step 2, f_i takes values in {−ε, 0, ε}, so its osc-radius is ≤ ε. LR′ at base v (pure power, finite moments)
  gives the loss 2ε² in place of 8ε².
- εη − 2ε² ≥ εη/2 ⟺ ε ≤ η/4. Justified.
- Leaving §3.6 unchanged is acceptable, since the remark is labelled as such.

**Remark LR-b.** One step of length h costs ∫_0^h(h − t)·2ε² dt = h²ε². ✓

**"Never assumes completeness".** Correct. Both Bessel (step 2) and the decomposition range K_m ⊕ ⟨q_m⟩ ⊕ ⟨q_{m+1}⟩ ⊕
range P (steps 5–6) are exact orthogonal decompositions of ℓ², with P = I − K_{m+2}.

**Absolute constants and path uniformity.**
- The constants are confirmed absolute: only orthonormality, the recurrence, and |f − c| ≤ ε enter.
- t-uniformity is automatic: every bound is a bound at an arbitrary base.

**Numerics (reproduced).**
- `.venv/bin/python ../ja-plan40/research/G1/checks/check_lr.py` reproduces `check_lr.out` line for line: [1] 0.5311 /
  0.6087 / 0.1896; [2] formula = central difference to 5 digits; [3] 13000 cases, 0.9863 / 0.8868; [4] 1.2·10⁻¹².
- It took 27 s wall (4 min CPU), not ≈ 7 min.
- stderr shows divide-by-zero warnings from [3] (see F4); they do not affect the reported numbers.

**Independent referee numerics** (scratchpad, not committed). The first check used mpmath at 50 digits on 300 random
measures, with 3–7 atoms at arbitrary real nodes in [−5, 5], random f (uniform or signs), ε ∈ {0.05, 0.5, 1.5, 3}, and
every admissible n including n = 0. Maximum ratios:

| Quantity | Max ratio |
|---|---|
| \|R_b\|/ε² | 0.986 |
| \|R_F\|/ε² | 1.837 (bound 2) |
| \|R_a\|/bound | 0.873 |
| pointwise \|(log b_n²)″(t)\| / (Var_{μ_n} + Var_{μ_{n−1}}) at random t (finite difference) | 0.9995 |
| pointwise \|a_n″(t)\| / (ε²(b_n + b_{n+1})(t)) | 0.926 |

The FVa form and the Lax form agree to 10⁻³⁰.

The second check was a hill-climb over nodes, weights and f (float64, 2–5 atoms). Maximum ratio to the stated bound:

| Remainder | Case | Max ratio |
|---|---|---|
| R_b | n = 1, K = 3 | 1.0000 |
| R_b | n = 1, K = 4 | 0.9999 |
| R_b | n = 2, K = 4 | 0.9994 |
| R_F | n = 2, K = 5 | 0.993 |
| R_a | n = 0, K = 2 | 0.9999 |
| R_a | n = 1, K = 3 | 0.998 |

No violation was found. All three constants are numerically sharp in the general class.

## Findings

**F1 (minor; §3.11 "What LR does not give", sharpness bullet; LOG).**
- Issue: The text says C = 1 is "close to optimal" (0.986), with no proof of optimality. It also cites no evidence on
  LR′ or LRa sharpness. The referee hill-climb attains ratio 1.0000 for LR, 0.993 for LR′ (against 2ε²) and 0.9999 for
  LRa, and the pointwise inequality |(log b_n²)″| ≤ Var_n + Var_{n−1} is attained to 0.9995. The current statement
  understates the result. (It is not an overclaim.)
- Fix: Say that "C = 1 in LR, 2 in LR′ and the factor (e^ε − 1 − ε)(b_n + b_{n+1}) in LRa are numerically sharp in the
  general finite-moment class (adversarial search on 2–5-atom measures reaches 0.993–1.000; NUMERICAL, Rule R)".
  Optionally add an explicit near-extremal family. For LRa with n = 0 and two atoms ±1: a_0 = tanh θ, b_1 = sech θ, so
  |a_0″| = 2ε²|tanh θ|sech²θ ≤ ε²sech θ, with equality at sinh θ = ±1. That gives a short proof that the pointwise LRa
  constant 1 is attained.
- Keep the observation that the pure-power ratios are ≤ 0.53.

**F2 (minor; §3.11 steps 1–2, "self-contained" in the heading).**
- Issue: Step 2 imports V_m = ½Σ(f_k − f_l)²K_m² from §3.5 step 3, whose setting is the pure-power one. That step rests
  on the Heine two-point function from the proof of G3′ Lemma H. The Gram/Sylvester proof of Lemma H is in fact valid
  for any finite-moment measure on distinct real atoms, but §3.11 extends it to the general setting without saying so.
  Moreover, the "cross-check" in step 2 is already a complete proof that bypasses the two-point function entirely:
  - (log b_n²)′ = α_n − α_{n−1} (FV);
  - α_m′ = 2⟨fq_m, q̇_m⟩ = ‖fq_m‖² − α_m² − 2‖K_m(fq_m)‖² (TV's q̇_m, whose smoothness is extended in step 0).
- Fix: Promote the TV route to the main proof of ΔV_m, or state it as an equivalent proof, and keep the Heine route as
  the cross-check. Either way, add one sentence noting that the Lemma H / §3.5 step 3 argument uses only the Gram form,
  so it holds for arbitrary distinct real atoms with finite moments.

**F3 (minor; Corollary LR-law (ii)–(iii)).**
- Issue: The plan's review focus asks that Λ be finite, but the text never states it. In (iii), E^a and Λ^a are not
  defined.
- Fix: Add "|L_n^v(f)| ≤ 2ε, so Λ(f) ≤ 2ε". Add "by step 4, L_n^{a,v}(f) = b_{n+1}γ_n − b_nγ_{n−1}, so
  n^p|L_n^{a,v}(f)|/(2c(p)) ≤ ε·n^p(b_n + b_{n+1})/(2c(p)) → ε". Define E^a(f) := limsup|n^pa_n(ve^f)/(2c(p)) − 1| and
  Λ^a(f) := limsup n^p|L_n^{a,v}(f)|/(2c(p)), and write (iii) as |E^a(τf) − τΛ^a(f)| ≤ e^{τε} − 1 − τε.

**F4 (minor; `checks/check_lr.py` [3]).**
- Issue: `rem` computes R_F at n = 1, where b_0 = 0, and this emits RuntimeWarnings (divide by zero) to stderr. R_F is
  then discarded, so LR′ is never tested on tiny measures. The `try/except: continue` silently drops failures, and the
  printed count does not show whether any were dropped. The docstring says "every admissible n", but the loop is
  n ≤ K − 3; the PROOF text correctly says n ≤ K − 3. The plan doc's "≈ 7 min" is ≈ 30 s wall on this machine.
- Fix: Compute R_F only for n ≥ 2 and report max |R_F|/ε² in [3]; the referee run reaches 1.84 ≤ 2. Count the skipped
  cases and print the count. Align the docstring and the runtime note. Regenerate `.out`.

**F5 (polish; §3.11).**
- (a) In "The constants", replace "LRa's bound is ≈ ε²e^εc(p)n^{−p}" with "≤ (1 + o(1))ε²e^εc(p)n^{−p}"; it is an upper
  bound, from (e^ε − 1 − ε)·2c(p)n^{−p}.
- (b) In the smoothness bullet, "bounded by (m‖f‖_∞)^r times the term times e^{m‖f‖_∞}" is ambiguous about which t.
  Write "≤ (m‖f‖_∞)^r e^{m‖f‖_∞}Π_{k∈S}v_kV(S), uniformly in t ∈ [0, 1]".
- (c) In the step 2 cross-check, "Lemma TV with A = all atoms, weighted by f" should say "TV's formula with 1_A replaced
  by f (linear in 1_A; f bounded)".

**F6 (info; Remark LR-a).** The claim that Theorem R's ε₀ could be η/4 is verified (see Checks). No change is needed.
When Plan 39 (§3.10, Theorem RW) or Plan 41 (§3.12) is merged, any R2-based loss there can cite LR′ in the same way.

**F7 (info; merge).** §3.10 is absent on this branch; it belongs to Plan 39 (`plan-39-rw`). The §0 row and the LOG entry
will need routine conflict resolution against Plans 39, 41, 42 and 44. No content issue.

## Recommended labels

- **LR, LR′, LRa:** PROVED (internal: FV, FVa, TV, §3.5 step 3, or TV only after F2) + Rule R ACCEPT WITH FIXES
  (review/REVIEW_Plan40.md). Once F1–F5 are applied: REVIEWED. Novelty UNCHECKED.
- **Corollary LR-law:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal LR, LRa) + Rule R ACCEPT WITH FIXES. Once F3
  is applied: REVIEWED. Novelty UNCHECKED.
- **Sharpness of the constants:** NUMERICAL (F1).
- **Fixed-f iff:** remains NOT PROVED, as the text says.

No re-check of the mathematics is needed. A quick confirmation that F1–F5 have been applied is enough.

## Re-check (2026-10-14; diff e01a0fc..7bb5cf4)

**Verdict: ACCEPT.** F1–F5 are applied correctly. The new main derivation in step 1 (F2) is correct. Nothing blocking
remains.

**F2: the new step 1 (FV + TV).** I checked every line.
- By FV, (log b_n²)′ = α_n − α_{n−1}, so (log b_n²)″ = α_n′ − α_{n−1}′ = ΔV_n − ΔV_{n−1}.
- α_m = ⟨fq_m, q_m⟩, with f fixed in t. Step 0 makes q_m C¹ as an ℓ²-valued map, so α_m′ = 2⟨fq_m, q̇_m⟩.
- Substituting q̇_m = ½fq_m − K_m(fq_m) − ½α_mq_m gives ‖fq_m‖² − 2⟨fq_m, K_m(fq_m)⟩ − α_m² = A_m + B_m. ✓
- The main route never uses the Heine two-point function. The vanishing of the f_k² and f_l² parts is needed only in the
  cross-check, where it is still stated. Step 2 (Bessel) and LR′ use only ΔV_m = A_m + B_m, so they are unchanged.
- The Heine cross-check is consistent with this. The added sentence on the generality of G3′ Lemma H (Gram form only)
  is correct.
- Polish, optional: the text says TV's q̇_m formula "uses only orthonormality and the C¹ property". Strictly, TV's proof
  also uses q_j = √w·p_j, with p_j of degree j and C¹ coefficients: that is what puts q̇_j − ½fq_j in span{q_0..q_j}.
  Those coefficients are C¹ by step 0's Gram–Schmidt, so "orthonormality, the polynomial structure q_j = √w p_j and
  step 0" would be exact. Not blocking.

**F1.**
- The sharpness bullet now gives NUMERICAL attained constants, attributed to the reviewer's hill-climb and to [3].
- The two-atom example is correct. With weights ∝ (e^θ, e^{−θ}) on atoms ±1, a_0 = tanh θ and b_1 = sech θ. Setting
  f = ±ε moves θ at rate ε. Then |a_0″| = 2ε²|tanh θ|sech²θ = ε²b_1·2|sinh θ|/cosh²θ, with equality iff |sinh θ| = 1.
- The pointwise LRa constant 1 is therefore attained. The bullet is correctly labelled "proved"; it shows the constant
  cannot be lowered.
- Optimality of the integrated constants is correctly left unproved.

**F3.**
- Λ(f) ≤ 2ε follows from |⟨f − c, μ_n − μ_{n−1}⟩| ≤ 2ε. ✓
- E^a and Λ^a are now defined. |γ_m| ≤ ε holds by Cauchy–Schwarz with the centred f, and L^{a,v} is shift-invariant.
  Hence Λ^a(f) ≤ ε, using n^p(b_n + b_{n+1})(v)/(2c(p)) → 1. ✓
- |E^a(f) − Λ^a(f)| ≤ e^ε − 1 − ε, the ray bound e^{τε} − 1 − τε = O(τ²), and the resulting iff are all ✓.

**F4.** I re-ran the script (`.venv/bin/python ../ja-plan40/research/G1/checks/check_lr.py`).
- The output is identical to the committed `check_lr.out`, and stderr is empty: no divide-by-zero warnings now.
- [3] reports 13000 cases with 0 skipped, |R_b|/ε² = 0.9863, |R_F|/ε² = 1.8886 ≤ 2 (n ≥ 2) and |R_a|/bound = 0.8868.
- The runtime note (30–60 s) is fine.
- Cosmetic leftovers: the docstring still says "K = 3..6 atoms", but the loop is K = 4, 5, 6. The "Runtime:" line sits
  between [3] and [4].

**F5.** (a), (b) and (c) are applied. The new LRa bound ≤ (e^ε − 1 − ε)·2c(p)n^{−p}(1 + o(1)) ≤
(1 + o(1))ε²e^εc(p)n^{−p} is correct.

**Labels.** The status row, the §3.11 heading, the LOG and the plan doc are consistent. "§3.5 step 3 only as a
cross-check" is accurate.

**Final labels.**
- **LR, LR′, LRa:** PROVED (internal: FV, FVa, TV) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT —
  REVIEWED. Novelty UNCHECKED.
- **Corollary LR-law:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) + Rule R ACCEPT WITH FIXES, fixes applied, re-check
  ACCEPT — REVIEWED. Novelty UNCHECKED.
- **Sharpness of the integrated constants:** NUMERICAL.
- **Pointwise LRa constant 1 attained:** PROVED (two-atom example).
- **Fixed-f iff:** NOT PROVED.

Remaining items, all optional polish: the TV wording in step 1, and the two docstring nits.
