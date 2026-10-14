# Rule R review — Plan 42 (G1 §3.13: Lemma RL, RL-loc, Remarks RL-n, RL-b, RL-UI, Corollaries RL1–RL3)

Reviewer: independent second reader (Claude agent, adversarial referee), 2026-10-14.
Scope: branch `plan-42-t0p`, commit 7b5b987, `git diff master...HEAD` (PROOF.md §0 row + §3.13, LOG.md, CITATIONS.md
(Simon), plan doc `docs/superpowers/plans/2026-10-14-plan-42-rl.md`, `checks/check_rl.py/.out`).

## Verdict

**ACCEPT WITH FIXES (minor).** The mathematics of Lemma RL, RL-loc, RL-n and RL-b is correct. I re-derived every step
listed under the plan's "Review focus" and found no gap. All findings are about wording, labels, one missing citation
under Rule C, and the accuracy of the numerics summary. One finding (F1) is an overclaim in the status row and headings,
where the a priori bound is dropped. It must be fixed before REVIEWED.

## Checks performed

1. **(M) path-sum formula.** J has diagonal a_m and off-diagonal J_{m−1,m} = b_m. So a step between m and m′ has
   weight b_{max(m,m′)}, a stay at m has weight a_m, and every entry is multiplied by s_n (not s_m). ∫y^ℓdν_n =
   s_n^ℓ⟨p_n, x^ℓp_n⟩ = ((s_nJ)^ℓ)_{nn}. Closed paths stay within ⌊ℓ/2⌋ of n, so n ≥ ℓ is enough to avoid the
   boundary. Correct. This matches Simon's Prop. 3.3, read in the source with the a/b swap and index shift.
2. **Step 2.** ∫y²dν_n = s_n²(a_n² + b_n² + b_{n+1}²) is correct. The bound u_m ≤ ∫y²dν_m at index m gives U < ∞, and
   then (s_n/s_{n+1})²u_{n+1} = u_{n+1} + o(1). (∗) is correct.
3. **Step 3.** The binomial expansion is valid because αI commutes with K. For j = 3, closed length-3 paths have an
   odd number of stays and lie within distance 1, so they contain some D_m with |m − n| ≤ 1. For j = 4, I enumerated
   the six ±1 paths: ++−− → E_{n+1}²E_{n+2}², +−+− → E_{n+1}⁴, +−−+ and −++− → E_n²E_{n+1}² each, −+−+ → E_n⁴, and
   −−++ → E_{n−1}²E_n². Their sum is (E_n² + E_{n+1}²)² + E_{n+1}²E_{n+2}² + E_{n−1}²E_n², as written. Only D_m with
   |m − n| ≤ 1 and E_m with n − 1 ≤ m ≤ n + 2 occur. The arcsine values check out: centred 4th moment
   16β⁴·(3/8) = 6β⁴, ∫y⁴dρ = α⁴ + 12α²β² + 6β⁴, and for α = 2c, β = c the moments are 2c, 6c², 70c⁴. (∗∗) → 2β⁴ is
   correct. It agrees with Simon's (3.11) (A_4 − A_2² = 2β⁴ in the centred case).
4. **Step 4.** At a limit point γ, (∗) at n_j − 1, n_j, n_j + 1 gives u_{n_j−1}, u_{n_j+1} → 2β² − γ and
   u_{n_j+2} → γ. (∗∗) then gives 2γ(2β² − γ) = 2β⁴ ⇔ (γ − β²)² = 0. Limit points exist because U < ∞ (step 2). The
   limit of a_n is forced by step 1 (ℓ = 1). Correct.
5. **(a) ⇒ (c′).** Tightness comes from Chebyshev. Uniform integrability of y^ℓ follows from the bounded (2ℓ + 2)-th
   moments. The support bound ν(|y| > R + δ) ≤ (R/(R + δ))^{2ℓ} holds, and Weierstrass gives uniqueness. Complete
   and self-contained.
6. **(c′) ⇒ (c).** This step does **not** use bounded support. ν_n lives on [0, s_nx_1], which is unbounded in n, and
   the proof does not need that fact. It uses the 6th-moment path bound ≤ 3⁶(2L)⁶ for n ≥ n₀, where every weight is
   s_n|a_m| or s_nb_m with |m − n| ≤ 3, so it is ≤ (s_n/s_m)L ≤ 2L. Then ∫_{|y|>R}y⁴ ≤ M₆/R². Correct.
7. **(c) ⇒ (b).** The cutoff argument with |g| ≤ 1 + y⁴ ≤ 2y⁴ on |y| > R ≥ 1 is correct, and the ρ-tail vanishes for
   R ≥ |α| + 2β. The equivalence chain (a) ⇒ (c′) ⇒ (c) ⇒ (b) ⇒ (a) is closed.
8. **RL-loc.** Step 1 at n + i (i = −1, 0, 1) gives D_{n+i} → 0. Step 2 at n + i bounds u_{n−1}, …, u_{n+2}; at
   i = 1 this uses s_{n+1}²b_{n+2}² ≤ ∫y²dν_{n+1}. It also gives the three pair sums. Step 3 at n then needs exactly
   these quantities. Step 4 runs along subsequences of N₀, and u_{n+1} → β² follows from (∗) at n. Correct. The
   indices used are moments ℓ = 1, 2, 4 at n − 1, n, n + 1 (ℓ = 4 is used only at n; at n ± 1 only ℓ = 1, 2 are used —
   see F7).
9. **RL-n, doubly infinite model.** The excursion decomposition is unique. The inner left and right paths live on two
   free half-lines (bonds β, diagonal α), and reflection preserves weights. So each excursion contributes
   (B_0² + B_1²)W = 2β²W. Hence (J_t^ℓ)_{00} = (J_{α,β}^ℓ)_{00} for all ℓ, and since J_t is bounded the e_0-spectral
   measure is the arcsine law ρ_{α,β}. Correct.
10. **RL-n, realization.** (LLᵀ)_{mm} = ℓ_m² + k_m² for m ≥ 1 (ℓ_0² for m = 0, hence the + k_0²e_0e_0ᵀ), and
    (LLᵀ)_{m,m−1} = k_mℓ_{m−1}, so a_m = 2β⟨m⟩^{−p} and b_m = ℓ_{m−1}k_m. Injectivity follows from
    ‖Lᵀu‖² + k_0²u_0² = 0 and the forward recursion. J is compact because it is banded with entries → 0.
    P_m(J)e_0 = e_m follows by induction. Infinite support follows because infinitely many P_m are orthonormal in
    L²(σ). The atoms are the positive eigenvalues, which accumulate only at 0, so they can be listed as x_k ↓ 0.
    Limits (n = n_j, gaps → ∞): s_nb_n → 2β·(1/√2)·√t = β√(2t) and s_nb_{n+1} → 2β·√(1 − t)·(1/√2) = β√(2(1 − t)).
    These are exactly B_0, B_1 of J_t. The diagonal tends to 2β = α and the other bonds to β. All moments converge to
    the arcsine moments, while n_j^pb_{n_j} → β√(2t). The neighbour 2nd moment α² + (1 + 2t)β² is correct; at t = ¼
    the ratio is (5 + 2t)/6 = 0.9167. Correct.
11. **RL-b.** ⟨u, Ju⟩ ≥ Σ(a_m − b_m − b_{m+1})u_m² ≥ cΣ⟨m⟩^{−p}u_m², using b_0 + b_1 = c ≤ 2c at m = 0. So J is positive
    definite (hence injective) and compact. The moments 3c, 11c², 195c⁴ are correct. The remark that α ≥ 2β is forced
    for positive atoms is correct, since weak limits of measures on [0, ∞) live on [0, ∞).
12. **Corollaries.** I checked T3a step 1 (§3.5): a_n ≤ 2M^pn^{−p} and b_n ≤ 2M^p(n − 1)^{−p}, using only x_k ≤ 1 and
    Sat_p⁺. Sat_p⁺ needs the lower sandwich bound through W/w_k, so the bound in (c′) holds for every sandwiched weight
    on k^{−p}, which RL1 needs. For RL2, Theorem R (§3.6) gives limsup|log(β_n²/β_{n−1}²)| ≥ εη/2 for
    e^{−ε}k^{−s} ≤ w_k ≤ e^{ε}k^{−s}. So β_n ↛ 1, (a) fails, and RL2's conclusions follow (see F2 for the wording).
13. **Simon citation (Rule C).** I fetched the mp_arc 03-341 TeX source myself
    (`web.ma.utexas.edu/mp_arc-bin/mpp/simon_ratios.TEX?yn=03-341`, 48418 bytes; title "Ratio Asymptotics and Weak
    Asymptotic Measures for Orthogonal Polynomials on the Real Line"). Every quote in CITATIONS.md (Simon) matches the
    source verbatim: the §1 nontriviality and normalization sentence, (1.1), (1.3), the §3 opener, Thms 3.1 and 3.2,
    Remark 2 after Thm 3.1, Prop. 3.3, and (3.10), (3.11), (3.13). The only change is that the TeX `{\rm{(}}…{\rm{)}}`
    in Thm 3.2 is rendered as "(…)" and the equation label is dropped, which is acceptable. The claim that **Thm 3.2
    does not apply as stated** is correct. Simon's μ_n = p_n²dμ is for a fixed μ with unscaled moments, while ν_n is
    the push-forward under the n-dependent dilation s_n. Applied literally to our σ, Thm 3.2 only gives the trivial
    limits A_ℓ = 0. "Attribution only" is the right status: nothing in §3.13 uses Simon's statements.
14. **Numerics.** I ran `.venv/bin/python ../ja-plan42/research/G1/checks/check_rl.py` from jacobi-asymptotics. It took
    2 min, and the output is **byte-identical** to the committed `check_rl.out`. The script reproduces the prescribed
    RL-b and RL-n parameters correctly (⟨m⟩ handled by mm[0] = 1). The [3] values match §3.13. See F4 for three
    misquoted numbers in the [2] summary.
15. **Independent check of a Rule A item** (scratch script, not committed; see F7). Let β = 1, α = 2,
    u_{n−1} = u_{n+3} = ((γ − 1)² + 1)/γ, u_n = u_{n+2} = γ, u_{n+1} = 2 − γ, and u = 1 elsewhere. Then the moments
    ℓ = 1, 2, 4 at **both** n and n + 1 equal 2, 6, 70 exactly (for γ = 0.5, 0.8, 1.3).

## Findings

**F1 (Medium; §0 table row, §3.13 heading, LOG heading, plan goal; overclaim).** The §0 row ends with "Law P (constant
c) ⟺ ν_n → arcsine on [0, 4c]". The §3.13 heading and LOG title say "Law P ⟺ the rescaled μ_n converge to the arcsine
law". As written, this is weak convergence alone, which RL does **not** prove. The converse without the a priori bound
is exactly RL-UI, which is open. The body of the lemma ("…together with the a priori bound…; and iff the three moments
ℓ = 1, 2, 4 converge") is correct.
*Fix:* everywhere this shorthand appears, write "⟺ ν_n → arcsine on [0, 4c] weakly **with sup n^p(a_n + b_n) < ∞**
(equivalently: moments ℓ = 1, 2, 4 converge)". Alternatively, write "in moments".

**F2 (Low; Corollary RL2).** "β_n does not converge" is stronger than Theorem R states. Theorem R gives
limsup|log(β_n²/β_{n−1}²)| > 0, i.e. no **positive** limit. Excluding β_n → 0 needs H_all / G1-L (Cesàro mean of
log β_j → 0), which is fine but not cited. RL only needs β_n ↛ 1. Also, the claim that ν_n does not converge *weakly*
uses (c′) and hence the a priori bound. That bound holds, by T3a step 1 for sandwiched weights, but RL2 does not say so;
the plan's review focus assumes it does.
*Fix:* write "β_n ↛ 1 (indeed no positive limit)". Add "the a priori bound holds by T3a step 1 (sandwiched weights)".
Give RL2 the label **PROVED-mod-cite (inherits Theorem R: RH_px, RH₁(r), RH_plt1b)**. Its "moments" half needs no
bound.

**F3 (Low; RL-n realization; Rule C).** The spectral theorem for compact self-adjoint operators is used with the
comment "textbook-standard, not separately cited". VERIFICATION_POLICY Rule C.3 says "Classical/well known/standard are
not citations". The repo's precedent (method of moments in LP) is not a waiver. In fact RL re-proves the method of
moments precisely to avoid this.
*Fix:* quote a source actually read, e.g. the Hilbert–Schmidt theorem (Reed–Simon I, Thm VI.16) with its hypotheses
(compact, self-adjoint, separable Hilbert space ⇒ orthonormal eigenbasis of ker^⊥, eigenvalues → 0). Alternatively,
label RL-n and RL-b PROVED-mod-cite (Hilbert–Schmidt). Only polynomial functional calculus on the eigenbasis is used
after that, and it is elementary as written.

**F4 (Low; §3.13 Numerics [2]; Rule N.3 accuracy of exported text).** Three quoted values disagree with
`check_rl.out`:
- "(R) … rmom ≈ 4e−2–1e−1 on N − 2 … N": rmom at n = N − 1 is **6.8e−3** (N = 60) and **8.2e−3** (N = 240).
- "(sv) … ≈ 2e−5 for n ≥ 100": rmom is 2.8e−5, **6.9e−5**, **6.3e−5** (rdev ≈ 1e−5).
- "(rnd) … slowly decreasing": rmom is 6.1e−2, 1.3e−2, 1.7e−2, **2.2e−2**, which is not decreasing.

*Fix:* correct the numbers. Note that the N − 1 rows (rdev ≈ 6e−2, rmom < 1e−2) are a numerical instance of RL-n:
single-index moments are near arcsine while the parameters are off. That supports the lemma.

**F5 (Low; RL1).** "Lemma LP (§3.8) is the forward direction for v = k^{−s}" is too strong. LP is stated for M ≥ 1,
i.e. for the CDF of ν_n on (0, 1]. But 4c(2) ≈ 2.43, so this is only part of [0, 4c(p)]. The forward direction is
RL (a) ⇒ (c′) applied to the pure-power Law P (RH_px etc.).
*Fix:* "Lemma LP is a special case of the forward direction (its CDF form for y ≤ 1)".

**F6 (Low; RL3 and the Setting).** "Regularly varying nodes ⇒ s_{n+1}/s_n → 1" is used without proof. It needs either
the uniform convergence theorem (cite it) or monotonicity. Monotonicity suffices: x_k ↓ 0 gives
f(λn)/f(n) ≤ f(n + 1)/f(n) ≤ 1 for n + 1 ≤ λn, then let λ ↓ 1. Also, "Law P (constant c(p)C)" uses C, which is not
defined in §3.13.
*Fix:* add the one-line monotone argument and define C (or point to the §1 definition).

**F7 (Low/Info; Rule A, "Neighbours"; RL-loc remark).** "Whether {n, n + 1} suffices was not settled". For the
hypotheses of RL-loc (moments ℓ = 1, 2, 4), it can be settled in the negative by check 15 above. Take u_n = u_{n+2} = γ,
u_{n+1} = 2β² − γ, u_{n−1} = u_{n+3} = ((γ − β²)² + β⁴)/γ, a = α/s_m, and all other bonds β/s_m, inserted at a sparse
N₀ as in RL-n. Then (∗) at n and at n + 1, and (∗∗) at n and at n + 1, hold exactly, while u_n → γ ≠ β². RL does not
need positivity, so a bounded Jacobi matrix suffices. With α = 2β (positive atoms), the local model's smallest
truncated eigenvalue is +5.6e−5 at γ = 1.3, consistent with the free spectral edge, but −0.016 at γ = 0.8. A positive
realization therefore needs γ > β² and a check; this is not claimed. Separately, RL-loc uses ℓ = 4 only at n. Its
hypothesis could be weakened to "ℓ = 1, 2 at n ± 1; ℓ = 1, 2, 4 at n".
*Fix (optional):* record this in Rule A. If it is added as a remark, label it PROVED (general measures) and leave
positivity open. Weaken the RL-loc hypothesis.

**F8 (Nit; Rule A "Scale ratios").** "Every use of s_n/s_m → 1 is for |m − n| ≤ 6" is false for the "(a) ⇒ all
moments" part, where |m − n| ≤ ℓ/2 for any fixed ℓ.
*Fix:* "for |m − n| bounded by a constant depending only on ℓ".

**F9 (Nit; labels consistency).** The §3.13 heading gives novelty "UNCHECKED for RL-n" but omits RL-loc. The §0 row
and LOG give "UNCHECKED (RL-loc, RL-n)". RL-b has no novelty field.
*Fix:* align the three places and add "novelty not claimed" for RL-b.

**F10 (Nit; §3.13 opening).** "the outline's statement is corrected in three places". Outline T0′ already assumes
sup a_n/f(n), sup b_n/f(n) < ∞ and every fixed j, so it is not wrong. RL refines it: j is redundant for the full
sequence, the neighbours are needed for right limits, the bound-free case is open, and the b-law alone fails.
*Fix:* "refined".

**F11 (Nit).**
- s_n = n^p gives s_0 = 0, but the Setting requires s_n > 0. Use ⟨n⟩^p, or start at n ≥ 1.
- RL-UI writes M₀ while T3a uses M.
- CITATIONS "verbatim from the TeX source" should add "modulo TeX markup ({\rm{(}} → "(")".
- §3.13 follows §3.9 on this branch; §3.10–3.12 are on plan-40/41 branches. Merge order and §0 row placement need
  care at merge.

## Recommended labels (after fixes)

| Item | Label |
|---|---|
| Lemma RL ((a) ⟺ (b) ⟺ (c) ⟺ (c′)) | PROVED (self-contained) + REVIEWED once F1 is applied; novelty not claimed (scaled Simon Thm 3.1/3.2) |
| Lemma RL-loc | PROVED + REVIEWED; novelty UNCHECKED |
| Remark RL-n | PROVED-mod-cite (Hilbert–Schmidt), or PROVED once a quoted source is added (F3); + REVIEWED; novelty UNCHECKED |
| Remark RL-b | as RL-n (same realization step); novelty not claimed |
| Remark RL-UI | open (GAP); correctly stated |
| RL1 | PROVED (internal: RL, T3a step 1 / Sat_p⁺) |
| RL2 | PROVED-mod-cite (inherits Theorem R) after F2 |
| RL3 | reformulation of RL (PROVED) after F6; the a priori bound for non-power nodes is open |
| Simon citation | READ, quotes verified verbatim; attribution only, which is correct |
| Numerics | NUMERICAL (float64; K-doubling only); re-run byte-identical; summary text to be corrected (F4) |

## Re-check (fix commit 502a6ba; diff 7b5b987..502a6ba)

Reviewer: same second reader, 2026-10-14. I re-ran `check_rl.py` from jacobi-asymptotics. The output, including the
new [4], is byte-identical to the committed `check_rl.out`.

**Verdict: ACCEPT.** The mathematics is correct, including the new material. Three label and wording items remain
(R1–R3, all Low/Nit). Fix them before the REVIEWED stamp; no further review round is needed.

| Finding | Status |
|---|---|
| F1 bound dropped in row/heading/LOG/plan | **Fixed** (§0 row, §3.13 heading, LOG title, plan goal) |
| F2 RL2 wording, bound, label | **Fixed** (β_n ↛ 1, no positive limit; T3a step 1 cited; PROVED-mod-cite inheriting Theorem R) |
| F3 Hilbert–Schmidt | **Partially fixed.** The statement is now precise, with its hypotheses. The label is questionable; see R1 |
| F4 numerics text | **Fixed.** I checked all quoted values against `.out`; one nit remains in the LOG (R3) |
| F5 LP is a special case | **Fixed** in RL1; one residual sentence remains in the §3.13 opening (R3) |
| F6 RL3 monotone argument, C | **Fixed.** The argument is correct: n + 1 ≤ λn ⇔ n ≥ 1/(λ − 1). C points to §1 (item 11 (H-a)), line 59 |
| F7 RL-n2, check [4], RL-loc weakening | **Fixed.** Verified below. Label nit in R1, γ range in R2 |
| F8 scale ratios | **Fixed** (≤ ℓ/2, ≤ 3, ≤ 2: all correct) |
| F9 novelty fields | **Fixed** (RL-n2 is missing from the heading's list; nit) |
| F10 "refined" | **Fixed** |
| F11 nits | **Fixed** (⟨n⟩^p, M, "modulo TeX markup") |

**Verification of the RL-loc weakening.** The new hypotheses are: ℓ = 1, 2, 4 at n, and ℓ = 1, 2 at n ± 1. The proof
uses ℓ = 1 at n + i (D_{n+i} → 0) and ℓ = 2 at n + i. That gives boundedness of u_{n−1}, …, u_{n+2}, with u_{n+2}
coming from s_{n+1}²b_{n+2}² ≤ ∫y²dν_{n+1}, and the three pair sums. The proof uses ℓ = 4 only at n, in step 3. Step 4
needs only these. **Correct.** The RL-n parenthesis was updated to match ("cannot both have arcsine 1st/2nd moments")
and is correct under the weakened lemma.

**Verification of RL-n2.** At n: u_n + u_{n+1} = 2 and u_{n+1}u_{n+2} + u_{n−1}u_n = γ(2 − γ) + γX = 2. At n + 1:
u_{n+1} + u_{n+2} = 2 and u_{n+2}u_{n+3} + u_nu_{n+1} = γX + γ(2 − γ) = 2. Here γX = (γ − 1)² + 1. So (∗) and (∗∗)
hold exactly at both indices, and step 3 gives the limits 2, 6, 70 while n_j^pb_{n_j} = √γ. Correct. Check [4] confirms
this: relative errors ≤ 3e−4 at n_j = 9995 and ≤ 3e−3 at n_j = 1000, with O(1/n) decay.

**Remaining items.**

- **R1 (Low; Rule C / labels; RL-n, RL-b, RL-n2).**
  - The fix labels RL-n and RL-b "PROVED-mod-cite (Hilbert–Schmidt)", but nothing was read or quoted, and there is no
    CITATIONS.md entry.
  - VERIFICATION_POLICY defines PROVED-mod-cite (X) as "proved from explicitly cited external results X, each read and
    quoted with its hypotheses in a CITATIONS.md". The current label therefore does not match its own definition.
  - The repo's actual practice, accepted in earlier Rule R reviews, is: textbook facts stated precisely with their
    hypotheses and marked "textbook-standard, not checked against a specific source" keep PROVED. This covers TL's
    Markov/Chebyshev (§0 row TL), LP's method of moments (§3.8, REVIEW_Plan35 l.200) and FV's inputs (§3.4 l.473).
  - My original F3 was stricter than that precedent. Either of these complies:
    - (a) return RL-n, RL-b and RL-n2 to **PROVED**, with "Hilbert–Schmidt theorem: textbook-standard, stated with
      hypotheses above, not checked against a specific source", as for TL and LP; or
    - (b) keep PROVED-mod-cite and add a CITATIONS.md entry quoted from a source actually read (e.g. Teschl, *Jacobi
      Operators*, free PDF).
  - Either way, **RL-n2 must carry the same label as RL-n**. It currently says "PROVED for general measures" while its
    text uses the same spectral-theorem step "mod Hilbert–Schmidt".
  - Recommended: (a).
- **R2 (Low; RL-n2).** The text says "(γ > 0)". It must be **0 < γ < 2**, since u_{n+1} = 2 − γ must be > 0 for
  b_{n+1} > 0. The numerics use γ ∈ {0.5, 0.8, 1.3}, which is fine.
- **R3 (Nit).**
  - The §3.13 opening sentence still says "Lemma LP (§3.8) is the forward direction for the pure power". Align it with
    RL1 ("a special case of").
  - The LOG numerics bullet still says "Slowly varying Ψ: rdev, rmom ~ 1e−5". rmom is 3–7e−5.
  - RL3's monotone argument evaluates f at λn, which is not an integer. Say "f decreasing on [1, ∞)", or use
    f(⌈λn⌉).
  - The §3.13 heading's novelty list omits RL-n2 (UNCHECKED).

## Final labels

| Item | Label |
|---|---|
| Lemma RL | PROVED (self-contained) + REVIEWED; novelty not claimed |
| Lemma RL-loc (weakened form) | PROVED + REVIEWED; novelty UNCHECKED |
| Remark RL-n | PROVED (Hilbert–Schmidt textbook-standard, per precedent; R1(a)) + REVIEWED, or PROVED-mod-cite (Hilbert–Schmidt) + REVIEWED if a CITATIONS entry is added (R1(b)); novelty UNCHECKED |
| Remark RL-n2 | same label as RL-n (general measures; positivity open, not claimed), with 0 < γ < 2 (R2); novelty UNCHECKED |
| Remark RL-b | same label as RL-n; novelty not claimed |
| Remark RL-UI | open (GAP) |
| RL1 | PROVED (internal: RL, T3a step 1 / Sat_p⁺) + REVIEWED |
| RL2 | PROVED-mod-cite (inherits Theorem R: RH_px, RH₁(r), RH_plt1b) + REVIEWED |
| RL3 | PROVED (reformulation of RL with the monotone ratio argument) + REVIEWED; the a priori bound for non-power nodes is open |
| Simon citation | READ, verbatim (modulo TeX markup), attribution only |
| Numerics [1]–[4] | NUMERICAL (float64; reproducible, byte-identical re-run) |
