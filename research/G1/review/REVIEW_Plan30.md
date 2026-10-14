# Rule R review: Plan 30 (Lemma TL, Theorem T3-sv), G1 PROOF.md §3.4

Reviewer: independent second reader (Rule R). Target: worktree `ja-plan30`, branch `plan-30-tail`, commit b56fcc7.
Scope: PROOF.md §3.4 (Lemma TL, Theorem T3-sv, Remarks TL1–TL2), the status rows TL and T3-sv, the T3c2 pointer,
the LOG Plan-30 entry, the README edit, `docs/superpowers/plans/2026-10-14-plan-30-tail.md`, and
`checks/check_tail_loc.py`/`.out`.

## Verdict: ACCEPT WITH FIXES

Both proofs are correct. I found no mathematical error that changes a statement. The fixes tighten constants and
hypotheses that the text leaves implicit: G, the head margin, explicit A, n ≥ 2, and integer T. Others make the
examples and numerics precise. Two are bookkeeping: quoting the two classical inequalities, and the novelty label.

## Line-by-line check (what was verified)

**Lemma TL.** Notation: a = x_{T″} = T″^{−p}, b = x_{T′} = T′^{−p}.
- **a/b.** a/b = (T′/T″)^p ≤ (n^{−2/p})^p = n^{−2}, because T″ ≥ T′n^{2/p}. The ceilings only help. ✓
- **Spacing.** By the MVT, x_j − x_{j+1} = p·ξ^{−p−1} for some ξ ∈ (j, j+1), so it is ≤ p·j^{−p−1} = p·x_j/j. This
  holds for every p > 0. For T′ ≤ j < T″ it gives x_j ≤ b and 1/j ≤ 1/T′, so the spacing is ≤ pb/T′. ✓
- **Atoms in [a, b].** These are exactly x_{T′}, …, x_{T″}, both endpoints included. Every point of [a, b] is therefore
  within half a spacing, ≤ pb/(2T′), of an atom. The text's pb/T′ is weaker but valid. ✓
- **Markov.** For deg P ≤ n, ‖P′‖_{[a,b]} ≤ 2n²/(b − a)·‖P‖_{[a,b]}. Since a ≤ b/4 for n ≥ 2, b − a ≥ b/2, which gives
  4n²/b. ✓
- **Norming.** |P(y)| ≤ |P(x_j)| + (pb/T′)(4n²/b)‖P‖ ≤ max_atoms|P| + ½‖P‖, using T′ ≥ 8pn². Hence
  ‖P‖_{[a,b]} ≤ 2·max_{T′≤j≤T″}|P(x_j)|. ✓
- **Extrapolation.** With y(x) = (2x − a − b)/(b − a), for x ∈ [0, a] we have |y| ≤ (a + b)/(b − a) = 1 + 2a/(b − a)
  ≤ 1 + 4a/b. The standard inequality |P(x)| ≤ |T_n(y(x))|·‖P‖_{[a,b]} for x outside [a, b] applies, and T_n is
  increasing on [1, ∞). ✓
- **T_n(1 + η).** cosh θ ≥ 1 + θ²/2 gives θ ≤ √(2η). With η ≤ 4/n², nθ ≤ √8 and cosh(√8) ≤ e^{√8} = 16.92 ≤ 17. ✓
- **Christoffel.** 1/K_{n+1}(x, x) = min{∫P² dσ : deg P ≤ n, P(x) = 1}, and K_{n+1} = Σ_{j=0}^{n} p_j². This is the
  right direction. If P(x_k) = 1 with k ≥ T″, then some j ∈ [T′, T″] has |P(x_j)| ≥ 1/34, so
  ∫P² ≥ w_j/1156 ≥ c·T″^{−s}/1156. Hence ρ_{n+1}(k) ≤ 1156(C/c)(T″/k)^s. ✓
- **Sum.** μ_n ≤ ρ_{n+1}, and μ_{n−1} ≤ ρ_n ≤ ρ_{n+1}. So "the same holds for μ_{n−1}" with the same T′, T″. ✓
  The tail sum Σ_{k>T}k^{−s} ≤ T^{1−s}/(s − 1) holds for integer T (F5).
- **κ.** T″ ≤ (8pn² + 1)n^{2/p} + 1 ≤ (8p + 2)n^{2+2/p}, so T″^{s/(s−1)} ≤ (8p + 2)^{s/(s−1)}n^κ with
  κ = (2 + 2/p)s/(s − 1). ✓
- **Uniformity.** Every constant depends only on (p, s, C/c), so the bound is uniform over the sandwich class. ✓

**Theorem T3-sv.**
- **Path.** Ψ^t ∈ [min(1, c), max(1, C)] for t ∈ [0, 1]. ✓
- **Lemma FV.** It applies, since f = log Ψ is bounded. Smoothness in t is as in T3-conv F4. Centering is valid
  because Σμ_n = Σμ_{n−1} = 1. ✓
- **Middle range.** On [n/M, n^γ], |g_n| ≤ δ_n(M, γ), which contributes ≤ 2δ_n. ✓
- **Head.** It works through Lemma Sat_p⁺, using that g_p is decreasing on (0, ½) (§3.1). This needs a margin for
  m = n − 1 (F2). ✓ after F2.
- **Tail.** Lemma TL is applied to w(t) with the constants C′/c′ = max(1, C)/min(1, c), for both μ_n and μ_{n−1}. ✓
- **Conclusion.** b_n(w)/b_n(v) → 1. The pure-power laws for every p > 0 and s > 1 (RH_px for p > 1, RH₁(r) for
  p = 1, RH_plt1b for 0 < p < 1) then give n^p b_n(w) → c(p) and β_n → 1. ✓

## Findings

**F1 (minor; §3.4, T3-sv proof, definition of G).**
- *Issue.* "G := log(C/c) + |log Ψ(n)|-type constant ≤ 2 max|log Ψ|" is not a definition.
- *Fix.* Both log Ψ(k) and log Ψ(n) lie in [log c, log C], so |g_n(k)| ≤ G := log(C/c) for all k and n. Use that.

**F2 (minor; §3.4, T3-sv proof, Head bullet).**
- *Issue.* "once g_p⁺(1/M) ≥ 1" covers m = n with k ≤ n/M, but not m = n − 1. There k/(n − 1) can exceed 1/M. The
  displayed factor e^{−2n·g_p⁺(1/M)} also suggests a pointwise evaluation where a uniform bound is needed.
- *Fix.* Fix M ≥ 4 with g_p⁺ ≥ 1 on (0, 2/M]; this exists because g_p⁺ is decreasing on (0, ½) and → ∞. Then for
  k < n/M, m ∈ {n − 1, n} and n ≥ 2, we get k < m and k/m ≤ 2/M. Lemma Sat_p⁺ with W(t)/w_k(t) ≤ (C′ζ(s)/c′)k^s
  and ((m+1)/k)^{2(1−p)₊} ≤ (n+1)² gives
  (μ_n + μ_{n−1})(k < n/M) ≤ 2(C′ζ(s)/c′)·n^{s+1}(n+1)²·e^{−2(n−1)} → 0, uniformly in t.
  Also say explicitly that M is fixed once, which is allowed because δ_n(M, γ) → 0 for every M.

**F3 (minor; Lemma TL statement, "A = A(p, s, C/c)").**
- *Issue.* A is not given. The conclusion also silently needs T ≥ T″, which the threshold must imply.
- *Fix.* For 0 < ε ≤ 1 (ε ≥ 1 is trivial), take
  A := (8p + 2)^{s/(s−1)}·max{1, 1156(C/c)/(s − 1)}^{1/(s−1)}.
  Then A·n^κ·ε^{−1/(s−1)} ≥ T″^{s/(s−1)} ≥ T″ and it exceeds the solved threshold. Here T″ ≤ (8p + 2)n^{2+2/p}
  because T″ ≤ (8pn² + 1)n^{2/p} + 1.

**F4 (minor; Lemma TL statement).**
- *Issue.* For n = 1, T″ = T′, so a = b and the interval [a, b] is degenerate. The proof assumes n ≥ 2, but the
  statement does not.
- *Fix.* Add "n ≥ 2" to the statement. This is harmless for T3-sv, where n → ∞.

**F5 (trivial; Lemma TL step 4).**
- *Issue.* Σ_{k>T}k^{−s} ≤ T^{1−s}/(s − 1) holds for integer T (compare with ∫_T^∞). For real T it holds with ⌊T⌋,
  which costs a factor ≤ 2^{s−1} when T ≥ 1.
- *Fix.* State T ∈ ℕ (indices), or put ⌊T⌋ and absorb the factor into A.

**F6 (cosmetic; Lemma TL steps 1, 3 and statement).**
- Step 3: "min_{j≤T″}w_j" should be min_{T′≤j≤T″}w_j. The bound c·T″^{−s} is unchanged.
- Step 1: "within p·b/T′" is correct, though half that also holds. No change needed.
- Make "the same holds for μ_{n−1}" explicit: μ_{n−1} ≤ ρ_n ≤ ρ_{n+1} pointwise.

**F7 (minor; T3-sv proof, Tail bullet).**
- *Issue.* The text does not say which sandwich constants Lemma TL uses along the path.
- *Fix.* Apply TL to w(t) with c′ = min(1, c) and C′ = max(1, C), so A = A(p, s, C′/c′), uniform in t.
- *Optional observation.* ε is not needed. With T = n^γ, Lemma TL gives a tail of order n^{(2+2/p)s − γ(s−1)}, which
  → 0 for every γ > κ. So the hypothesis can be weakened to "for every M and some γ > κ". Keeping the stronger "all
  M, γ" definition is fine.

**F8 (minor; Remark TL1, the examples).**
- *Domain.* 2 + sin√(log log k) and 2 + sin(log log log k) are undefined for small k: log log k < 0 for k ≤ 2, and
  log log log k needs k ≥ 3. Fix: say "for k ≥ k₀; any values in [1, 3] below k₀".
- *Lower range.* The justification "log log(k^γ) = log log k + log γ" covers only the upper range. Add the lower
  range: log log(n/M) = log log n + log(1 − log M/log n) = log log n + o(1).
- *Full argument.* Put L = log log n. Over k ∈ [n/M, n^γ], u = log log k ranges in [L − o(1), L + log γ]. Since
  2 + sin ≥ 1, |log(2 + sin α) − log(2 + sin β)| ≤ |α − β|. This gives:
  - for √u: δ_n ≤ (log γ + o(1))/(2√L) → 0 ✓;
  - for log u: δ_n ≤ (log γ + o(1))/L → 0 ✓;
  - for u itself (2 + sin(log log k)): the window has width ≥ log γ in phase. With γ = e^π, along the n with
    L ≡ π/2 (mod 2π) approximately (these exist infinitely often, because L increases with increments → 0),
    δ_n ≥ log 3 − o(1). So it is NOT polynomially slowly varying, while log log(λk) − log log k → 0 makes it slowly
    varying. ✓
- *Reviewer numerics* (log-space sampling, M ∈ {10, 10³}, γ ∈ {5, 20}, log n = 10² … 10³²): δ_n decays slowly for the
  first two and stays at 0.6–1.1 for the third. This is consistent with the above.

**F9 (minor; Remark TL1, third bullet; scope).**
- *Issue.* The bullet is correct but understated. If Ψ is bounded and polynomially slowly varying and χ → L > 0, then
  Ψχ is itself bounded and polynomially slowly varying, since |log χ(k) − log χ(n)| → 0 uniformly on k ≥ n/M. So
  the bullet is a direct instance of T3-sv, not a new proof.
- *Fix.* Say "T3-sv contains T3-conv (Ψ → L is polynomially slowly varying) and its products with such Ψ." Keep
  T3-conv's separate, simpler proof: it needs no Lemma TL.

**F10 (minor; Remark TL2 numerics; check_tail_loc).**
- *Rerun.* I reran `check_tail_loc.py` and it reproduces the committed `.out` exactly.
- *Ratio.* The committed max ratio is 7.67·10⁻¹⁰, so "≤ 8·10⁻¹⁰" ✓.
- *Beyond T″.* The committed values run 1.59·10⁻⁵ … 1.44·10⁻³, so "0.002–0.14%" ✓.
- *Beyond 10n.* The committed values are 9.33, 6.91, 4.49 and 7.64·10⁻². The text's "5–9%" should read "4.5–9.3%".
- *Truncation.* The measures are truncated at K = 6T″. My Rule N run at K = 12T″ leaves the ratio unchanged
  (7.67·10⁻¹⁰). It moves "mass beyond T″" by about 10% (p = s = 2, n = 6: 1.44 → 1.58·10⁻³), while the 10n and 3n
  masses are stable.
- *Fix.* Add "(truncated at K = 6T″; K = 12T″ changes the beyond-T″ mass by ≤ 10%)".
- The tested n is 6–10, so the "beyond 10n" percentages are pre-asymptotic. The text already says "small n".

**F11 (minor/bookkeeping; citation gate and novelty; status row TL).**
- *Inequalities.* Lemma TL uses two external classical inequalities. Under AGENTS.md rule 4, quote them with
  hypotheses, e.g.:
  - (Markov) real P with deg ≤ n: ‖P′‖_{[−1,1]} ≤ n²‖P‖_{[−1,1]};
  - (Chebyshev growth) real P with deg ≤ n and |y| ≥ 1: |P(y)| ≤ |T_n(y)|·‖P‖_{[−1,1]}.
  Each is to be stated from a source someone has read, e.g. Borwein–Erdélyi, *Polynomials and Polynomial
  Inequalities*, or Rivlin, *Chebyshev Polynomials*. Mark the proof "standard inequalities" in the way FV is marked.
- *Novelty.* The TL row lacks a novelty tag. Add "novelty UNCHECKED". The "n²-dense grid is a norming set" step is
  classical (Ehlich–Zeller 1964; Coppersmith–Rivlin 1992; Rakhmanov, Ann. Math. 2007, "Bounds for polynomials with a
  unit discrete norm"). Christoffel-function bounds by restriction and extrapolation are standard (Nevai; Máté–Nevai–
  Totik). These are pointers, not citations.

**F12 (minor; cross-references).**
- *§3.2 localization reduction.* It still says "The upper tail is a GAP". Add "(polynomial-scale tail: Lemma TL, §3.4;
  scale Mn: OPEN)".
- *Header.* The §3.4 header and status rows correctly say "Rule R pending". Update them after the fixes.
- *T3c2 pointer.* The edit is accurate.

**F13 (cosmetic; LOG Plan-30 entry).**
- "Tools that lose Markov's n² cannot reach it" reads as a theorem about methods. Rephrase as "this method (which pays
  Markov's n²) cannot reach it" (heuristic).
- The LOG drops the ceilings in T′ and T″. Acceptable in a log.
- README edit: accurate ("in review").
- Plan doc: the Review focus matches what was checked. T3 can be ticked after the re-check.

## Recommended labels (after fixes)
- **Lemma TL:** PROVED (standard Markov and Chebyshev inequalities, quoted per F11); Rule R ACCEPT WITH FIXES →
  REVIEWED after re-check; novelty UNCHECKED (pointers in F11).
- **Theorem T3-sv:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV, Lemma Sat_p⁺, Lemma TL); Rule R
  ACCEPT WITH FIXES → REVIEWED after re-check; novelty UNCHECKED.
- **TL1:** the examples hold as stated, after the F8 domain fix. **TL2:** Mn-scale localization stays OPEN;
  the numerics stay NUMERICAL.

## Re-check (commit 032fdd6)

I checked fixes F1–F13 against §3.4, the TL and T3-sv status rows, the §3.2 pointer and the LOG.

**Applied correctly (no further action):**
- **F1:** G := log(C/c). ✓
- **F2:** head margin, g_p⁺ ≥ 1 on (0, 2/M], with the explicit n^{s+1}(n+1)²e^{−2(n−1)} bound. ✓
  - Nit: say M ≥ 4. That makes 2/M ≤ ½, the range where g_p is monotone, and gives k < n/M < n − 1.
- **F3:** explicit A, 0 < ε ≤ 1, and "in particular T ≥ T″". ✓
- **F4:** n ≥ 2. ✓
- **F5:** integer T. ✓
  - Nit: the parenthetical "for non-integer T, use ⌊T⌋" does not carry the explicit A, which assumes integer T. Either
    say "integer T" in the ε-threshold sentence too, or note that the ⌊T⌋ version costs a factor 2^{s−1} in A^{s−1}.
    Not blocking.
- **F6:** the minimum now runs over [T′, T″], and μ_{n−1} ≤ ρ_n ≤ ρ_{n+1} is stated. ✓
- **F7:** path sandwich constants max(1, C)/min(1, c), and "any γ > κ". ✓
- **F8:** domain, lower range, and the O(1)-length window in log log k. The phrase "vanishing local oscillation" is
  correct, since (√u)′ and (log u)′ → 0. The non-example has δ_n ≥ log 3 − o(1). ✓
- **F10:** "4.5–9.3%", the truncation K = 6T″, and the doubling note match the `.out` and my run. ✓
- **F12:** the §3.2 pointer is accurate. ✓
- **F13:** the LOG line is now marked heuristic. ✓

**Residual items (all minor; none needs another re-check):**
- **R1 (F9 wording, §3.4 TL1).** "T3-sv contains T3-conv (constant Ψ)" gives the wrong reason. Constant Ψ is the
  trivial case. T3-conv is contained because a convergent ψ_k → L ∈ (0, ∞) is itself bounded and polynomially slowly
  varying.
  - Fix: "T3-sv contains T3-conv (take Ψ = ψ: ψ_k → L > 0 is polynomially slowly varying)".
- **R2 (F11, citation gate).** The Markov and Chebyshev inequalities are now quoted with hypotheses (deg ≤ n,
  interval, affine map), but no source is named. AGENTS.md rule 4 asks for a source someone actually read.
  - Fix: name one, e.g. Borwein–Erdélyi, *Polynomials and Polynomial Inequalities* (GTM 161), or Rivlin, *Chebyshev
    Polynomials*. Give section or theorem numbers only after checking them.
  - Alternatively, label them "textbook-standard", as FV is.
- **R3 (cosmetic, TL1).** Two adjacent bullets now both say 2 + sin(log log k) is not polynomially slowly varying.
  Merge them.
- **R4 (bookkeeping).** After R1–R3, set the §3.4 header, the TL and T3-sv rows and the LOG to "re-check ACCEPT —
  REVIEWED", and tick plan task T3.

**Re-check verdict: ACCEPT** (R1–R4 to apply; they are wording and bookkeeping, with no mathematical content).

**Final labels:**
- **Lemma TL:** PROVED (standard Markov and Chebyshev inequalities, quoted; source per R2); REVIEWED; novelty
  UNCHECKED (pointers: Ehlich–Zeller, Coppersmith–Rivlin, Rakhmanov 2007, Nevai, Máté–Nevai–Totik).
- **Theorem T3-sv:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV, Lemma Sat_p⁺, Lemma TL); REVIEWED;
  novelty UNCHECKED.
- **TL2:** Mn-scale localization stays OPEN; the numerics stay NUMERICAL.
