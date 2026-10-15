# Rule R review — Plan 45 (QL numerics N1–N3), PROOF.md §3.15

Reviewer: independent second reader (Rule R). Branch `plan-45-qlnum`, commit 8a568de (`git diff master...HEAD`).
Scope: PROOF.md §3.15, §0 row **QL-num**, LOG.md 2026-10-14 Plan 45 entry, plan doc
`docs/superpowers/plans/2026-10-14-plan-45-qlnum.md` (Review focus), `research/G1/checks/check_ql_numerics.py` / `.out`.

## Verdict

**ACCEPT WITH FIXES.** The numerics are sound and reproducible. The tail model is a legitimate stand-in for the
infinite measure on the tested range, and the LP constants are correct. Every label stays NUMERICAL / CONJECTURE /
HYPOTHESIS. No finding overturns a conclusion. The fixes are about how the evidence is read and worded:

- The main issue is F1. The N3 "no μ^{−1/2} blow-up / saturation" argument is structural (it happens for any f), so it
  is not evidence for CB. At p = ½, the CB scale and the Cauchy–Schwarz scale cannot be told apart on the tested window.
  "Route I′ not dead" still holds by the outline's literal criterion, but the supporting text must be reworded.
- The rest are wording and accuracy fixes: the crossover constants are quantized by the grid; one exception is really
  two; "two weights" in N3 should be one; the N1 defect description; the p = 2 plateau slopes; and Plan 44's "sup at
  t = 0" was a truncation artifact.

## Checks performed

1. **Rerun.** From `jacobi-asymptotics`: `.venv/bin/python ../ja-plan45/research/G1/checks/check_ql_numerics.py`
   (11.5 min wall). After stripping the `[Ns]` timing stamps, the output is **byte-identical** to the committed `.out`.
2. **LP constants (independent, mpmath 30 digits).** I(p) = (√π/2)Γ(1/p+½)/Γ(1/p+1) and c(p) = ¼(π/(2I))^p give:
   - I = 1, π/4, 0.58905;
   - c = 0.616850, 0.5, 0.408248 (these match `jacobi_asym.laws.weyl.c_p`);
   - 4c = 2.467, 2.0, 1.633. All exceed 1, so the min in F_p is never active for u ≥ 0.

   ∫_0^∞F_p(e^u)du, computed directly and via the closed form (2/p)(2/π)∫_0^{(4c)^{−1/2}}arcsin(y)/y dy, gives
   **0.4156299645 (p = 2), 0.9296953983 (p = 1), 2.076195126 (p = ½)**. The quoted 0.4156 / 0.9297 / 2.0762 are correct.
   The arcsine prefactors (1/π)c^{−1/2} = 0.4053, 0.4502, 0.4982 also match the `.out`. The Λ_n limit identity holds:
   Σ_{k≥n}log(k/n)μ(k) = ∫_0^∞μ(k > ne^u)du, and T_M → F_p(M).
3. **Tail model: finer quadrature** (referee script, same model code). I used log-panel ratio 1.005 instead of 1.02,
   12 Gauss points instead of 8, and T_END = 10⁶⁰ instead of 10⁴⁸, at p = 2 (n = 100) and p = 1 (n = 50), t = 1.
   - n·dev_b/ϑ_n is unchanged to 6 digits (0.469678; 0.435818).
   - Λ_n is unchanged to 5 digits.
   - T_M for M = 4^0 … 4^11 changes by ≤ 1.4·10⁻³ relative, and only for M with Mn > K.
4. **Tail model vs true atoms.** I compared against an atoms-only measure with K = 2·10⁷ (no quadrature), which is far
   beyond the hard edge for p = 2, n = 100 and p = 1, n = 50.
   - On k ≤ 2·10⁷, T_M agrees once the script model's own mass beyond 2·10⁷ is subtracted (1.14·10⁻⁵ resp. 1.95·10⁻⁴).
   - The residual is 0.05–0.08% at p = 2 and 0.7–0.9% at p = 1. That residual is the renormalization of the truncated
     measure, which has missing mass 2·10⁻⁴.
   - N1: 0.469678 (tail) vs 0.469670 (atoms only), and 0.435818 vs 0.435556. The tail matters at p = 1, as the script's
     own "no-tail comparison" shows.

   So the Euler–Maclaurin/GL continuation reproduces the atomic measure in the hard-edge region. The midpoint start at
   K + ½ is the correct continuation of Σ_{k>K}. There is no bias that grows with M: the only discrepancy is a
   **relative** O(10⁻³) error from where the boundary of A = (Mn, ∞) falls in the node grid, and it does not grow with M.
   The tail beyond 10⁴⁸ is negligible: μ_n(k > T_END) ≈ k_hard/T_END ≤ 10⁻³⁰.
5. **Recurrence / adaptive head cutoff.** The instability sits in the head atoms (x_k above the scaled band, where q_m is
   the minimal solution). The ld/f64 agreement test bounds the f64 roundoff-amplification error, and the ld error is about
   10³ times smaller. It does **not** detect coefficient error, which is common to both precisions. The independent
   Lanczos check covers that (μ_m to 3.9·10⁻¹⁵ at m ≤ 200, K = 2·10⁴, no tail).
   - The 1e−14 absolute clause affects at most about m head atoms, all outside every A = (Mn, ∞) with M ≥ 1.
   - The discarded head mass is ≤ 4.6·10⁻¹⁸ wherever it is measured.
   - The effect on N3 inner products is ≲ m·√(head mass)·|f|·√μ_j(A), which is many orders of magnitude below X.
   - The orthogonality defect max|⟨q_j, q_m⟩| = 10⁻⁹…10⁻⁷ comes from the dropped head (q_j for small j lives there). It
     is harmless for the same reason.

   I reran with my own implementation, which splits the head chunk (ld + f64) from the bulk (f64 only, since atoms are
   independent in the j-recurrence). It reproduces the script's T_M exactly.
6. **Text vs `.out`.** I checked every number in §3.15, the §0 row and the LOG. The mismatches are listed below
   (F3–F6, F8). Everything else matches, including:
   - N1 rows; the tilt comparison; K-doubling 1.8·10⁻⁷;
   - Λ_n rows and ε_nΛ_n;
   - QL-b constants 0.43–0.45 / 0.60–0.62 / 0.57–0.58;
   - N3 maxima 0.704 / 0.720 / 0.923; saturation 0.626–0.741 and 0.932–1.002;
   - X > 0 in all 36 (p, t, n) rows; Lanczos 6.1·10⁻¹³; TV-FD to 5 digits;
   - 4^20 / 400⁴ = 43.
7. **Crossover vs Plan 46 (QLP1, M ≍ n^{2/p}).** The exponent agrees (see F4 for the precision). Plan 46's heuristic
   picture also matches the N2 slopes: arcsine slope −p/2 above the Bessel scale and hard-edge slope −(σ−1) below it.

## Findings

**F1 (Medium) — §3.15 N3 bullets 2 and 4; LOG N3; §0 row. The "no μ^{−1/2} blow-up / saturation" argument is structural
and not evidence for CB, and at p = ½ the test does not discriminate.**

Beyond the hard edge (x_k → 0):
- q_m(k) = √w_k·p_m(x_k) → √w_k·p_m(0);
- h = K_m(g_nq_m) = √w·P, where P = Σ_{j<m}⟨q_j, g_nq_m⟩p_j has degree < m;
- so R(M) → |P(0)/p_m(0)| as M → ∞.

This holds for every f with fq_m ∈ L², at every fixed n. Therefore:
- the saturation, the fitted d log R/d log(1/μ_m(A)) ≈ 0 over the five deepest M, and "R·√μ decays like √μ" are
  automatic;
- the outline's stop condition (iii) ("scales like √(1/μ_m(A))") can never trigger in the M → ∞ direction.

The only window that can discriminate is the arcsine range M ≲ n^{2/p}. At p = ½ there, μ_m(A) ≍ M^{−1/4}, so the two
scales grow by almost the same factor over M = 2 … 2²⁹:
- the CB scale 1 + log M grows by 12.5×;
- the Cauchy–Schwarz scale μ^{−1/2} grows by about 11× (the data's μ goes 0.46 → 3.5·10⁻³ at n = 400).

The data cannot separate them. At n = 400, t = 1:
- the log-log slope of R against 1/μ is ≈ 0.36;
- R/(ε(1+log M)) falls 0.92 → 0.44;
- R√μ/ε falls 1.04 → 0.54, at the same rate.

At p = 1 the window separates the scales moderately: over M = 2 … 2¹⁷ the CS scale grows 16× and the CB scale 7.6×, while
R grows 5×. At p = 2 the separation is cleaner.

Fix: say that the saturation is structural (R → |P(0)/p_m(0)|) and is not evidence. State the actual evidence as
R ≤ 0.93·ε_n(1+log M) uniformly on the tested (n, M, t), with saturation value ≈ (0.6–1.0)·ε_n log n. Add that at p = ½
the tested arcsine window does not distinguish ε log M growth from μ^{−1/2} growth, so the go/no-go is informative mainly
at p = 2 (and partly p = 1). "Route I′ not dead" may stay, since the outline's literal criterion "bounded by C·ε·log M"
holds. Drop "R does not scale like μ_m(A)^{−1/2}" as a stand-alone claim, or restrict it to p ∈ {1, 2}. Optionally, note
that the CB hypothesis's real content at depth is the bound |P(0)/p_m(0)| ≲ ε_n log(n^{2/p}).

**F2 (Minor) — §3.15 N3 bullet 3. "R is of the same order as the mean of g_n over A (no Cauchy–Schwarz loss, no extra
cancellation)" is contradicted at depth.** mean_A g_n/(ε(1+log M)) stays ≈ 0.85–0.95 at M = 2²⁹, while
R/(ε(1+log M)) is 0.13–0.27 there (p ∈ {2, 1}). So R ≈ (0.15–0.3)·mean_A g_n, and the ratio keeps falling with M, because
mean_A g_n grows like log M and R saturates. There *is* cancellation, and it is structural (F1). In the arcsine range the
ratio is ≈ 0.3–0.45. Fix: "R ≤ mean_A g_n, comparable (factor 2–3) in the arcsine range and increasingly smaller beyond
the hard edge."

**F3 (Minor) — §3.15 N3 verdict "two weights"; §0 row. N3 (and all of N2) used only Ψ = exp(√log(k+e))**
(`L = CASES["sqrt"][0]`); θ = 0.8 appears only in N1. Fix: replace "two weights" with "one weight (√log), t ∈ {0, ½, 1}".
In the §0 row, say that N2–N3 use √log only.

**F4 (Minor) — §3.15 N2 "Crossover"; §0 row; LOG. The constants 3.3 and 0.34 are quantized by the grid, and the
"one exception" is two.**
- M_x is printed as the geometric mean of a factor-4 bracket, so M_x/n^{2/p} can only take the values 2·4^j/n^{2/p}:
  {0.82, **3.28**, 13.1} for p = 1 and {0.084, **0.336**, 1.34} for p = ½ (n = 25·2^i).
- "3.3n²" therefore means M_x ∈ [1.6, 6.6]·n², and "0.34n⁴" means M_x ∈ [0.17, 0.67]·n⁴.
- "Stable in n" is the genuine part: the bracket index moves exactly 1 grid step (p = 1) or 2 grid steps (p = ½) per
  doubling of n over four doublings. That pins the exponent to 2/p ± ½, consistent with Plan 46 QLP1 (M ≍ n^{2/p}).
- The `.out` shows 1.34·n^{2/p} at p = ½, t = 1 for **both** n = 25 and n = 50, not only n = 25. This is the adjacent
  grid value, so the t = 1 crossover sits near the 0.67 bracket boundary rather than being a "plateau grid effect".

Fix: quote the brackets, correct "one exception" to n ∈ {25, 50}, and state the exponent check explicitly.

**F5 (Minor) — §3.15 N2, p = 2 plateau "slope −0.3 … −0.6".** The `.out` has minimum slopes −0.40/−0.41 (n = 50, 200)
and −0.76…−0.79 (n = 25, 100, 400) at t = 0, and −0.33…−0.64 at t = 1. The depth depends on how n aligns with the 4^j
grid. Fix: "−0.3 … −0.8 (depending on the alignment of n with the 4^j grid)".

**F6 (Minor) — §3.15 N1 "Reading"; §0 row; LOG N1. Defect description and range.**
- (a) (1 − dev_w/dev_tilt)·log n *decreases* for every p from n = 100 to 1600: 0.56 → 0.51 (p = ½), 0.32 → 0.24 (p = 1),
  0.20 → 0.10 (p = 2). So the defect decays at least as fast as 1/log n, and faster at p ≥ 1. The text says "0.10 and
  decreasing (p = 2)" as if p = ½ and p = 1 were constant, and the LOG says "defect ≈ c_p/log n". Fix: give both ends and
  say "decays at least like 1/log n". This slightly *favours* the limit 0.5, but the wording "not established" stays right.
- (b) The tilt comparison (dev_tilt, dev_w/dev_tilt) is run for √log only. Say so.
- (c) The minimum at n = 1600 is 0.4650 (a_n, p = ½, √log), so "0.466–0.497" in the §0 row and "0.466–0.493" in the LOG
  should read 0.465.
- (d) Optional: note that the three-term 1/log n fit gives Y < 0.5 even at p = 2 (0.460/0.477). At p = 2 the B1/B2 tilt
  test already supports 0.5, so this shows the fit's bias. That makes the "illustrative only" label concrete.

**F7 (Minor) — §3.15 Method, "tail masses to ≤ 3·10⁻³ relative" (K-doubling).** This is mostly not a K-truncation
effect. It is the quantization of the boundary of A = (Mn, ∞) on the quadrature nodes: one GL node carries ≈ α·(0.36·log
1.02) ≈ 2–4·10⁻³ of T_M at slopes α = ½…1. The 3·10⁻³ entries occur exactly at n = 50 and 200, where 4^j·n lands just
above 2·10⁵. Referee check 3 confirms this: refining the tail moves T_M by ≤ 1.4·10⁻³ relative and does not grow with M.
Fix: add one sentence saying this. It also answers the plan's Review-focus question: the tail model is adequate, it is
started correctly at K + ½, and it introduces only a relative O(10⁻³) boundary error that does not grow with M.

**F8 (Minor) — §3.15 N2 Λ_n, "(Plan 44's truncated p = 2 values 0.4151–0.4232 are consistent)".** With the tail, the sup
over t is attained at **t = 1** in every row (t = 1 ≥ t = ½ ≥ t = 0). Plan 44's (REVIEWED) remark says "in every row
the sup over t is attained at t = 0 … the t = 1 values are smaller". That remark was an artifact of truncating at K: Ψ
puts extra mass in the far tail. The size is ≤ 5·10⁻³ and no conclusion changes, but "consistent" hides a reversal. Fix:
note it in §3.15 and add a one-line LOG note that Plan 44's sup-at-t = 0 statement is a truncation artifact.

**F9 (Minor) — §3.15 Method / N3; LOG Tooling note. The scope of the cross-checks is narrower than the claims.**
- All independent N3 cross-checks are at p = 2 only:
  - Lanczos: t = 1, n = 100, M ≤ 2⁷, μ(A) ≥ 3·10⁻³, no tail;
  - TV finite difference: t = ½, n = 100;
  - K-doubling: t = 1.
- p = 1 and p = ½, where the maximum ratio 0.93 occurs, rest on the recurrence alone.
- The Lanczos μ_m validation covers m ≤ 200, K = 2·10⁴, no tail. The LOG claim "the final rule loses ≤ 10⁻¹⁷" is
  verified only there; at m ≤ 1600 with the tail, the `.out` shows only |1 − Σμ| ≤ 2·10⁻¹³.

Fix: state this scope. Preferably also add a p = ½ TV-FD check, which costs a few seconds.

**F10 (Minor) — LOG Tooling note.** The fixed-cutoff failure ("garbage 10²⁰–10⁵⁰ for θ below ~0.8 of the band edge") and
the "first adaptive rule (missing mass 10⁻⁷)" cannot be reproduced from the committed script or `.out`. Fix: mark them
"(exploratory runs, not in the .out)", or add a short demonstration row to the script.

**F11 (Info) — §3.15 N2 QL-b.** C_n(α) uses m = n only and t ∈ {0, 1}. Lemma QLb's hypothesis has m ∈ {n − 1, n} and
sup over t. Λ_n does use both m. Fix: one parenthetical.

## Labels

Everything in §3.15, the §0 row and the LOG is marked NUMERICAL. The tilt law is kept as a CONJECTURE and QL as a
HYPOTHESIS. "Route I′ not dead" and "CB plausible numerically, unproved" are framed as evidence for a finite range.
README / THEOREMS are not edited. No certified claims are made. Labels are acceptable once F1 is applied.
