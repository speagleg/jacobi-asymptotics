# Rule R review — Plan 44 (Theorem B-cond, PROOF.md §3.14)

Reviewer: independent second reader (Rule R). Branch `plan-44-bcond`, commit db55182, `git diff master...HEAD`
(PROOF.md §0 row + §3.14, LOG.md, plan doc, `checks/check_sv_general.py/.out`). Compared against §3.1 (Sat_p),
§3.2 (FV), §3.3 (Sat_p⁺), §3.4 (TL), §3.5 (FVa, T3a), §3.8 (TV, LP, L, T3-all), §3.9 (TLw, T3-log) and
`research/program/outline_B_sv.md` §2.

## Verdict

**ACCEPT WITH FIXES** (all fixes minor / polish; no mathematical error found).

Lemma L0, Lemma FV⁺ and Lemma QLb are correct as stated. Theorem B-cond is correct as a conditional theorem: every
unconditional estimate (head, lower bulk, far tail, a_n constants) checks, and the law follows from QL₀ (and from QL,
which implies QL₀). The accounting of what is proved about QL is honest. QL is not proved in any case beyond T3-log /
T3-all, and the text does not claim otherwise. Numerics re-run in full (reproduced digit for digit). The issues below are
mis-quoted numbers in Bc2, two missing one-line justifications, and wording.

## Checks performed

**L0 (dyadic chaining, Potter).**
- ε_n = sup_{m≥n}δ_m(2) is finite, nonincreasing and → 0: each δ_m(2) is a max over finitely many integers and δ_m(2) → 0. OK.
- (i): the chain n, 2n, …, 2^jn, k uses only δ_{2^in}(2) with 2^in ≥ n. Steps: j links plus the final one, j + 1 ≤ 1 + log₂(k/n).
  Membership 2^{i+1}n ∈ [2^in/2, 2·2^in] and k ∈ [2^jn, 2^{j+1}n] ⊂ [2^jn/2, 2·2^jn] are correct. OK.
- (ii) Potter: this uses only (i) at a fixed N with ε_N ≤ η log 2, plus finitely many k < N. ε_N/log 2·log(k/N) ≤ η log k. So
  λ = 2 alone suffices. No UCT/BGT is needed, and none is cited. All k ≥ 1 are covered, including k < n (the bound is
  global, not centred at n). OK.
- The downward direction (k < n) is never needed with ε_n. In B-cond, k ∈ [n/M₀, n) uses δ_n(M₀) and k < n/M₀ uses
  Potter. OK (see F3 for the remark's wording).

**FV⁺.**
- (A): T_S = Π_{k∈S}w_k(t)V(S), with V(S) ≤ 1 because x ∈ (0, 1]. Also ∂_tT_S = (Σ_Sf)T_S, 1 + |Σ_Sf| ≤ Π_S(1 + |f_k|) and
  w_k(t) ≤ v_k max(1, e^{f_k}). So |T_S| + |∂_tT_S| ≤ Π_SU_k and Σ_{|S|=m}Π_SU_k ≤ (ΣU)^m.
  The Weierstrass M-test on [0, 1] then gives D_m ∈ C¹ with the termwise derivative. The same holds for N_F (|F| ≤ m). OK.
- (B): Σ_k|f_k|ρ_m(k) = Σ_S(Σ_S|f|)T_S/D_m ≤ (ΣU)^m/min_{[0,1]}D_m. This is uniform in t. μ_j ≤ ρ_m for j < m, and
  |q_{n−1}q_n| ≤ ½(μ_{n−1} + μ_n). OK.
- FV: interchange of Σ_S and Σ_k by Tonelli/Fubini under (B). OK.
- FVa step 2: (N_F/D_m)′ = 𝔼[F⟨f, X⟩] − 𝔼F𝔼⟨f, X⟩. Domination by mΠU. OK.
- FVa step 3: Σ_{k,l}x_k|f_l|P(k, l ∈ S) ≤ mΣ_l|f_l|ρ_m(l) (x ≤ 1, |S| = m). Covariance terms are dominated by
  Σ_{k,l}|f_l|K_m(k,l)² = Σ_l|f_l|K_m(l,l) < ∞, and the diagonal terms by Σ|f_k|K_m(k,k). OK.
- **x-moments:** none are needed beyond x ≤ 1 (the atoms lie in (0, 1]). The hypothesis "x_k ∈ (0, 1] distinct" covers k^{−p}. OK.
- FVa step 4: the cross term after Christoffel–Darboux satisfies Σ|A_{kl}||f_k|, Σ|A_{kl}||f_l| ≤ 2⟨|f|, μ_n + |q_{n−1}q_n|⟩ < ∞, so
  the split Σ A(f_k − f_l) = ΣAf_k − ΣAf_l is legitimate. The absolute convergence of the cross piece *before*
  Christoffel–Darboux is asserted rather than shown; it is immediate (F4).
- Application: U_k ≤ e^{A}k^{−s+η}(1 + A + η log k), summable for η ≤ (s − 1)/2. OK.
- Rationale against the K-cutoff (cut paths are off vΨ^t, so QL would be needed on them too): correct, and a good reason.

**QL ⇒ QL₀.**
- By L0(i), Σ_R|g_n|(μ_n + μ_{n−1}) ≤ ε_n[(μ_n + μ_{n−1})(R) + (1/log 2)Σ_Rlog(k/n)(μ_n + μ_{n−1})], which is
  ≤ 2ε_n + (2ε_n/log 2)Λ_n. OK.
- Monotonicity in γ: Λ_n increases with γ, so QL(γ) ⇒ QL(γ′) for κ < γ′ ≤ γ. OK.
- The "t-average suffices" claim: steps 1 and 7 integrate over t. R is finite, so t ↦ Σ_R|g_n|μ_m^{(t)} is continuous,
  and the head and tail bounds are uniform in t. OK.

**Theorem B-cond.**
- Choice of η: at η = 0 the inequality γ(s − 1) > (2 + 2/p)s is exactly γ > κ, so by continuity some η ∈ (0, (s − 1)/2] works. OK.
- (∗) with min(1, Ψ) ≤ Ψ^t ≤ max(1, Ψ):
  - W(t) ≤ e^{A}ζ(s − η) and w_k(t) ≥ e^{−A}k^{−s−η}. OK.
  - |g_n(k)| ≤ 2A + η log k + η log n ≤ 2A + 2η log max(k, n). OK.
- Head (step 2): n ≥ 2, M₀ ≥ 4, so k < n/4 < n − 1 ≤ m. k/m ≤ n/(M₀(n − 1)) ≤ 2/M₀, so g_p⁺ ≥ 1.
  Also ((m + 1)/k)^{2(1−p)₊} ≤ (n + 1)², e^{−2m g} ≤ e^{−2(n−1)}, μ_m ≤ 1 − ρ_m, and W/w_k ≤ e^{2A}ζ(s − η)n^{s+η}.
  The polynomial factors are crushed by e^{−2n}, so n^ph_n → 0. The factor 4n is generous. Sat_p⁺ (via Sat_p) uses only
  W and w_k, as already used for unbounded weights in T3-log. OK.
- Lower bulk: B ⊂ ℕ ∩ [n/M₀, M₀n], so |g_n| ≤ δ_n(M₀) and the contribution is ≤ 2δ_n(M₀). OK.
- Range R = [n, n^γ]: ≤ Q_n by definition. The tail T = (n^γ, ∞) is disjoint from R. OK.
- Far tail (step 5):
  - T″ ≤ (8p + 2)n^{2+2/p}, so the stated (8p + 3) is safe. κ > 2 + 2/p, so n^γ ≥ T″ eventually.
  - μ_{n−1}, μ_n ≤ ρ_{n+1}. TLw with u = w(t) gives the ratio ≤ e^{2A}T″^{s+η}k^{−s+η}.
  - Σ_{k>X}(1 + log k)k^{−(s−η)} ≲ X^{1−(s−η)}(1 + log X) (integral comparison).
  - The exponent (2 + 2/p)(s + η) − γ(s − 1 − η) < 0 by the choice of η. The (1 + γ log n) factor is harmless.
  - So for γ > κ and small η, the far tail → 0 even with the k^η Potter growth and the log k weight. OK.
- a_n (step 7):
  - Off H, x_k ≤ (M₀/n)^p.
  - a_n^{(t)}, a_{n−1}^{(t)} ≤ (M₀/n)^p + h_n, and b_n ≤ ½⟨x, μ_{n−1} + μ_n⟩ ≤ (M₀/n)^p + h_n. Once h_n ≤ (M₀/n)^p, all three
    are ≤ 2M₀^pn^{−p}.
  - Off H, |x_k − a_n| ≤ max(x_k, a_n) ≤ 2M₀^pn^{−p} (both are nonnegative).
  - Hence n^p|ȧ| ≤ 2M₀^pΣ_{k∉H}|g_n|(2μ_n + μ_{n−1}) + n^pΣ_H|g_n|(2μ_n + μ_{n−1}) ≤ 4M₀^p(2δ_n + Q_n + τ_n) + 2n^ph_n.
  - The constant 4M₀^p is correct. There is no n^p loss in the tail, unlike the outline's L2 / T3-log step 3, which used
    x, a_n ≤ 1. OK.
- Conclusion via RH_px / RH₁(r) / RH_plt1b for v only. OK.

**QLb.**
- Layer cake: for u < (γ − 1)log n, {k ∈ [n, n^γ] : log(k/n) > u} ⊂ (e^un, ∞) with M = e^u ∈ [1, n^{γ−1}). The set is empty beyond that.
- So Λ_n ≤ ∫_0^∞min(1, Ce^{−αu})du = (1 + log C)/α (C ≥ 1). OK.

**"What is proved about QL".**
- Trivial range: Λ_n ≤ (γ − 1)log n. If ε_n log n → 0, then D(γ) ≤ sup_nε_n(1 + (γ − 1)log₂n) < ∞ by L0(i), so
  T3-log applies. Correct.
- Bounded Ψ: T3-all step 1's bound is pointwise in t, so sup_t of the full sum (⊇ Q_n) has limsup ≤ 2Ge^{4G}F_p(M) for
  every M. Hence QL₀. Correct.
- "Theorem L does not give QL": correct (fixed M only), and phrased as "does not give", not "QL fails". Correct.
- Log-type: T3-log runs on the truncated path, so QL₀ on vΨ^t is not established. Correct and appropriately cautious.
- D(γ) = ∞: "no case of QL is proved". Correct.
- No overclaim found anywhere (§0 row, heading, LOG, plan doc).

**Remarks.**
- Bc1 is labelled HEURISTIC / OBSTRUCTION. I spot-checked the Grönwall-floor arithmetic for exp((log k)^θ): H_n ≍ (log n)^θ,
  so e^{4H_n} beats any power of log n. The claims about "every available transport" and the "1/n-order information"
  structural reason are outline-level and are correctly not claimed as proved.
- Bc2 is labelled NUMERICAL, and the tilt law ϑ_n/(2n) is labelled CONJECTURE.
- Bc3: the renaming s := σ − ρ is fine, and the UCT is correctly neither cited nor used.
- Bc4: entries (a)–(f) are correct.

**Numerics.**
- I re-ran `check_sv_general.py` in full from the jacobi-asymptotics root. The output is identical to the committed `.out`.
- Independent cross-check (mine, not in the repo): for the pure power, Lemma LP predicts Λ_n(v) → ∫_0^∞F_2(e^u)du = 0.41563
  (p = 2, c(2) = 0.61685). Truncated at M = K/n this gives 0.41495 (M = 600) and 0.41529 (M = 1200). The script gives
  0.4151 at n = 800, K = 4.8·10⁵ and 0.4165 at n = 400 (M = 1200). Also μ_n(>8n) ≈ 0.051 against F_2(8) = 0.0507.
- So the t = 0 values are consistent with LP, and the "slow decrease in n" is convergence to the LP constant (see F2).

## Findings

**F1 (minor; §3.14 Bc2, numbers).** Two quoted ranges do not match the `.out` file:
- "ε_n/ϑ_n ≈ 0.69–0.71": the output gives 0.691–0.708 (√log) and 0.676–0.698 (θ = 0.8), i.e. 0.676–0.708.
- "flat in t (variation ≤ 1.2·10⁻³)": this holds at K = 4.8·10⁵. At K = 1.2·10⁵ the θ = 0.8, n = 100 row varies by
  1.8·10⁻³ (0.4220 vs 0.4202).

*Fix:* write 0.68–0.71, and "variation ≤ 1.2·10⁻³ at K = 4.8·10⁵ (≤ 1.8·10⁻³ at K = 1.2·10⁵)".

**F2 (minor; Bc2, interpretation).** In every row sup_tΛ_n is attained at t = 0, i.e. at the pure power v. That is why
the two weights give identical sup_t values ("for both weights" is a tautology at t = 0). The t = 1 values are smaller
(by ≤ 1.2·10⁻³). The decrease in n is the approach to the LP constant ∫_0^∞F_p(e^u)du = 0.4156 (p = 2).

*Fix:* add one sentence saying so. This strengthens the reading "QL in the natural form Λ_n = O(1)" at t = 0. It also
makes clear that at t = 0 QL is a uniform-in-M version of LP (the outline's QLP), which the numerics support but nothing
proves.

**F3 (minor; L0 remark and Bc4(b)).** "λ = 2 implies all λ by the same chaining" is true. However, the downward half
(k ∈ [n/λ, n)) needs ε_{⌈n/λ⌉}, not ε_n: |g_n(k)| ≤ ε_k(1 + log₂(n/k)) ≤ ε_{⌈n/λ⌉}(1 + log₂λ).

*Fix:* add that parenthesis. Bc4(b) then reads consistently: downward chaining is available with ε at the lower index,
but it is not needed.

**F4 (minor; FV⁺ proof, FVa step 4).** "The rank-one update is a termwise identity between absolutely convergent
series" asserts the absolute convergence of the cross piece Σ(x_k − x_l)(f_k − f_l)K_n(k,l)q_n(k)q_n(l) without showing it.

*Fix (one line):* 2|K_nq_nq_n| ≤ K_{n+1}² + K_n² + μ_n⊗μ_n entrywise, and each of these is summable against
|f_k| + |f_l| (by Σ_lK_m(k,l)² = K_m(k,k) and Σ|f|μ_n < ∞). Alternatively, use Cauchy–Schwarz:
Σ_{k,l}|f_k||K_n(k,l)q_n(k)q_n(l)| ≤ ½Σ_k|f_k|(μ_n(k) + K_n(k,k)).

**F5 (minor; Bc2, truncation sensitivity).** "K = 1.2·10⁵ vs 2.4·10⁵ agree to ≤ 2·10⁻³" is correct, but the gap grows
with n: 0, 0, 3·10⁻⁴, 8·10⁻⁴ and 1.9·10⁻³ for θ = 0.8 b_n, and 2.0·10⁻³ for the a_n analogue at n = 1600. The n = 1600
values are therefore truncation-limited at the 0.2% level. This does not change the conclusion "≈ 0.49 → 0.5".

*Fix:* say "the K-gap grows with n, ≤ 2·10⁻³ at n = 1600".

**F6 (polish; framing of QL₀).** QL₀ is the first-variation bound itself, restricted to [n, n^γ]. The mathematical content
of B-cond is therefore: (a) the unconditional control of the head, the lower bulk and the far tail for every sequence-form
slowly varying Ψ, with no boundedness; (b) FV⁺ on the single path vΨ^t; (c) the reduction QL ⇒ QL₀ via L0. The text
already says this in effect ("The only hypothesis beyond …"). One explicit sentence would keep a reader from mistaking
QL₀ for an independent, weaker-looking hypothesis.

*Fix:* add "QL₀ is precisely the range part of the first-variation bound; B-cond shows that everything outside
[n, n^γ] is controlled unconditionally."

**F7 (polish; labels and wording).**
- (a) Label Lemma FV⁺ "PROVED (standard extension; novelty not claimed)", as for FV and FVa.
- (b) The §0 row's PROVED-mod-cite internal list should include L0 alongside FV⁺, Sat_p⁺ and TLw.
- (c) "for all n, every p > 0 and s > 1" in the Theorem B-cond conclusion: "for all n" means "along the full sequence
  (not a density-one subsequence)". Say so, or drop it.

No major or blocking findings.

## Recommended labels

- Lemma L0: **PROVED**.
- Lemma FV⁺: **PROVED** (standard extension of FV/FVa; novelty not claimed).
- Lemma QLb: **PROVED** (as an implication; its hypothesis is not verified for any new Ψ).
- Hypothesis QL / QL₀: **HYPOTHESIS** (open for D(γ) = ∞; holds only where T3-log/T3-all already apply, and in the
  log-type unbounded case not even QL₀ on vΨ^t is established).
- Theorem B-cond:
  - the unconditional bounds are **PROVED-mod-cite** (RH_px, RH₁(r), RH_plt1b; internal L0, FV⁺, Sat_p⁺, TLw);
  - the law is **CONDITIONAL (QL₀, implied by QL)**;
  - Rule R: ACCEPT WITH FIXES (this file). After F1–F7 it can be marked REVIEWED on a re-check. Novelty UNCHECKED.
- Bc1: **HEURISTIC / OBSTRUCTION**. Bc2: **NUMERICAL** (p = s = 2 only; truncated, k ≤ K ≪ n^γ). Tilt law ϑ_n/(2n): **CONJECTURE**.
- No new case of the pointwise Law P is proved by Plan 44.
