# Rule R review: Plan 25 (PROOF.md §4.1, Lemma Tr and Theorem L′)

Reviewer: independent Rule R referee (adversarial). Target: branch plan-25-suff, commit bbf2fed.

Read:
- AGENTS.md;
- PROOF.md §0 (status table, row L′), §1, §2 (Z1, Z1′), §3 (Z2, G3′-U), §4 (Lemma S, Lemma W, G3′-L steps 1–7),
  §4.1 (all), §5.2 (Lemma H, Lemma Sat), §5.3 (N‴, Remark N‴1), §7 (Setting T, Lemma K);
- LOG.md Plan-25 entry; README.md status block; docs/superpowers/plans/2026-10-14-plan-25-suff.md (Review focus);
- checks/check_trunc.py and check_trunc.out.

Numerics:
- I re-ran `check_trunc.py` from the jacobi-asymptotics venv. The output is byte-identical to `check_trunc.out`.
- My scratch scripts (mpmath, 150–400 digits) are under "Independent checks".

## Verdict: ACCEPT WITH FIXES

I found no error that affects the conclusion. Lemma Tr is correct, Theorem L′ is correct, and (LG*) ⊇ (SG), (LG) holds.
- **Lemma Tr.** I re-derived the determinantal identity, the Lagrange bound, the λ_max bound and Lemma K's use at M/2.
- **Theorem L′.** I re-derived the window restriction, the near-pair cost, the o(n²) total and the comparison with
  exactly ν_J. The order of limits (n → ∞, then M → ∞, then η → 0) is right.

There are no major findings.
- **Medium.** F1: a numerical claim ("log det(I − K_A) is O(1)") is false, and the committed `.out` already
  contradicts it. F2: the convexity step of Lemma Tr is garbled as written, although its conclusion is true.
- **Minor.** F3–F6.
- **Info.** F7–F9.

## Checked and OK

### Lemma Tr (Review focus 1)
- **(a) Determinantal form.**
  - Lemma H's Gram form gives D_n(ν_J)/D_n(ν) = det G(ν_J) = det(I_n − VᵀV), with V_{lj} = √v_l p_j(x_l) for
    l ∈ A = (J, ∞).
  - Σ_{l∈A}‖V_l‖² = Σ_A ρ_n(l) ≤ n, so V is Hilbert–Schmidt of rank ≤ n. Sylvester then holds for this finite-rank
    operator, and det(I − K_A) is the product over the ≤ n nonzero eigenvalues.
  - K_A = VVᵀ ⪰ 0. Since I − VᵀV = G(ν_J) ⪰ 0, ‖K_A‖ ≤ 1.
  - tr K_A = Σ_A ρ_n(l). Also ρ_n(l) = 1 − D_n(ν∖{l})/D_n(ν) = P_ν(l ∈ S), by Lemma H with one deletion and the
    Heine sum. So tr K_A = E_ν#(S ∩ A). ✔ (Wording: F3.)
  - Independent check: Hankel determinants from moments (400 digits) at n = 6, 8 and J = 2n, 4n reproduce
    log det G_head from the `.out` to all printed digits. For example, at n = 8, J = 2n: −1.250933 vs −1.2509. ✔
- **(b) Lagrange.**
  - For a tail atom x = l⁻² with l > J ≥ 2n, 0 < x < x_m for every node, so |x − x_m| ≤ x_m.
  - x_m/|x_i − x_m| = i²/(|m − i|(m + i)). Since m + i > i, i²/(m + i) < i ≤ 2n.
  - Π_{m≠i}2n/|m − i| = (2n)^{n−1}/((i−n−1)!(2n−i)!) ≤ (2n)^{n−1}2^{n−1}/(n−1)! ≤ (4en/(n−1))^{n−1} ≤ (8e)^n.
  - P = ΣP(x_i)ℓ_i gives P(x)² ≤ n²(8e)^{2n} max P(x_i)². ✔
  - Numerically, max_i Π x_m/|x_i − x_m| has log/n = 0.81, 1.08, 1.25, 1.36 at n = 4, 8, 16, 32, against
    log(8e) = 3.08. The full Σ|ℓ_i| over tail points is below n·(8e)^n. ✔
- **(c) λ_max.**
  - K_A = P_A Π P_A, with Π the projection onto {√v·P(x) : deg P < n}. So λ_max = ‖P_AΠ‖² =
    sup_P Σ_A vP²/Σ_all vP².
  - The denominator is ∫P²dν = head (l ≤ J) + tail. Tail ≤ R·head gives λ_max ≤ R/(1 + R), with R = e^{C_sn}.
  - R absorbs n²(8e)^{2n}·Σv/(c₁(2n)^{−s}). This uses only the lower half of (Hw) and Σv < ∞. ✔
- **(d) Convexity.** The conclusion log det(I − K_A) ≥ −(C_sn + 2)tr K_A is true, but the written derivation is not
  (F2).
- **(e) Lemma K at M/2.**
  - Lemma K (§7, REVIEWED) needs both halves of (Hw), which hold for v_j = j⁻⁴ (c₁ = c₂ = 1, s = 4, U ≡ 1), and
    M/2 ≥ 2.
  - It gives P_ν(|S ∩ ((M/2)n, ∞)| ≥ t₀n) ≤ exp(−(A²/log(M/2))n² + o(n²)), using Theorem H's lower half or
    Lemma W for D_n(ν).
  - A ⊂ ((M/2)n, ∞), and #(S ∩ A) ≤ n. Hence E# ≤ t₀n + n·P(·) = t₀n + o(n), so "fraction o(1)" is enough.
  - The constant A = 4p + 2|κ| of H7 does not depend on s.
  - When t₀ ≥ 1 the bound C_sn·n ≤ C_sAn²/log(M/2) holds trivially. ✔

### Theorem L′ (Review focus 2, 3)
- **Good set.**
  - #(E_g ∩ [1, K]) ≥ (1 − η − o(1))K − k₂, from d̄(B_η) ≤ η.
  - 1/(1 − η) < 1 + 2η for η < ½, so π(j) ≤ (1+2η)j for j ≥ j₀. ✔
- **Near pairs.**
  - a ∈ E_g means a ∉ B_η, so γ_{a+1} > γ_a. Index a + 1 need not lie in E_g; this does not matter.
  - Every b > a has γ_b ≥ γ_{a+1}, because γ is nondecreasing. So γ_b − γ_a ≥ 2πg_a/log(γ_a/2π) > 0.
  - Two distinct elements of E_g never share an atom.
  - The near-partner count is O(log γ̃_a) = O(log(Mn)), independent of S.
  - The total is ≤ C log(Mn)·Σ_{a∈E_g, a≤Mn}log⁺(1/g_a) + O(n log n log log n). The sum runs over the whole window,
    so the bound is uniform in S.
  - At K = Mn, (LG*) gives o((Mn)²/log(Mn)), so the total is o(M²n²) = o(n²) for fixed M and η. ✔
- **Far pairs.**
  - log ratio ≥ −4C₀/(γ̃_b − γ̃_a).
  - With a ≤ Mn, log γ̃_{a+n} = O(log n), so each element costs O(log² n).
  - The sum and denominator factors cost Σ 10C₀n/γ̃_a = O(n log² n). ✔
- **Comparison measure.**
  - S ⊂ E_g ∩ [1, Mn] corresponds bijectively, via π, to T ⊂ [1, J], with J = |E_g ∩ [1, Mn]| ≥ (1 − 2η)Mn ≥ (M/2)n.
  - The weights are 2c⁻¹x̃_{π(j)} = 2c⁻¹L(π(j))π(j)⁻² ≥ c′j⁻² ≥ c′j⁻⁴, with π(j) ≤ C_ηj.
  - So the comparison measure is exactly c′ν_J, with ν = Σ j⁻⁴δ_{j⁻²}.
  - The pair inequality of G3′-L step 6 (H5(i), Lemma S, j < j₀ handled by a positive constant) is pointwise in
    (j, i). It does not care about the window.
  - The L-factor bookkeeping uses t_k ≥ k for the k-th element of T, with log L + log(1 − ε*/2) nondecreasing. ✔
- **Lemma W (s = 4).** log D_n(ν) ≥ Λ_n − Kn log n, with Λ_n = −2n² log n + κn² (C = 1). ✔
- **Order of limits.** The o(n²) terms depend on (M, η) only. Then M → ∞ (the C′/log(M/2) term), then η → 0. ✔
- **(SG) ⇒ (LG*).** Take B_η = {g_k < δ(η)}. It contains every g_k = 0, has d̄ ≤ η, and off it
  log⁺(1/g) ≤ log(1/δ). ✔
- **(LG) ⇒ (LG*).** Here E = {k ≥ 2 : γ_k = γ_{k−1}} (§5), so E − 1 = {k : γ_{k+1} = γ_k}, and d(E − 1) = d(E) = 0. ✔
  - The examples k⁻¹⁰⁰ (sum ≍ 50K log K) and e^{−√k} (sum ≍ K^{3/2}) are o(K²/log K), and both violate (SG). ✔
- **Remark L′1 example.** g_k = e^{−k/log k} on half of all k.
  - Off any B_η with d̄ ≤ η < ½, a set of upper density ≥ ½ − η remains. Its sum is ≍ K²/log K, not o.
  - g_k > e^{−βk} eventually for every β > 0, so T_β is finite.
  - So it is covered by neither L′ nor N‴. ✔
- **Consistency sanity (Info, F9).** (LG*) implies d(E) = 0 and d(T_β) = 0 for all β, as the necessity results
  require.

### Labels, framing, novelty
- **Label.** "PROVED-mod-cite + mod-input (LG*), Theorem H; Rule R pending" is correct. The only citation is (C1),
  through Z1.
- **Framing.** No claim about RH, and (LG*) is called a hypothesis (L′3). ✔
- **Novelty.** UNCHECKED is appropriate. The determinantal identities are standard. The Lagrange spectral-gap
  argument is elementary.

## Findings

**F1 (Medium). §4.1, NUMERICAL bullet 3 ("log det(I − K_A) is O(1), so the bound above is far from sharp").**
- **Issue.** This is false, and the committed `.out` already contradicts it. At J = 2n the values are −1.25, −3.03,
  −5.63 for n = 8, 12, 16.
- **My runs** (Ka = 20n, 150 digits; they agree with the `.out` where the two overlap):

  | J | quantity | n = 8 | n = 16 | n = 24 | n = 32 |
  |---|---|---|---|---|---|
  | 2n | log det/n² | −0.0195 | −0.0220 | −0.0231 | −0.0238 |
  | 4n | log det/n² | −0.0031 | −0.0040 | −0.0045 | −0.0048 |
  | 8n | log det/n² | −0.0004 | −0.0006 | −0.0007 | −0.0008 |
  | 2n | tr K_A/n | 0.090 | 0.095 | 0.097 | 0.098 |
  | 4n | tr K_A/n | 0.023 | 0.040 | 0.043 | 0.045 |
  | 8n | tr K_A/n | 0.003 | 0.009 | 0.014 | 0.018 |

- **What the data show.** The truncation cost at fixed J/n is genuinely of order n², with a constant that decays
  quickly as J/n grows. The expected tail count is linear in n. This is exactly the regime that Lemma Tr + Lemma K
  describe, and it is why M → ∞ is needed.
- **Sharpness.** The convexity bound with the true λ_max is near-sharp: −7.49 vs −5.63 at n = 16, J = 2n. The slack
  is in the analytic constant C_s, not in the method.
- **Fix.** Replace the bullet with: "log det(I − K_A) grows like −c(J/n)n², with c ≈ 0.024, 0.005, 0.0008 at
  J/n = 2, 4, 8 (n ≤ 32, scratch); tr K_A/n tends to a constant. This is consistent with the n²/log M scale of
  Lemma Tr. The convexity bound with the true λ_max is within a factor 1.33 of log det."

**F2 (Medium). §4.1 Lemma Tr proof step 3 (convexity).**
- **Issue.**
  - The expression "λ·max(f(λ_max)/λ_max, 2 log 2·2)" is garbled.
  - The next step infers f(λ_max)/λ_max ≤ C_sn + 2 from f(λ_max) ≤ C_sn + 1. That inference is invalid, because
    step 2 bounds λ_max only from above. For example, λ_max = ½ gives f/λ = 2 log 2, but λ_max ∈ (½, 1) can give a
    ratio up to 2(C_sn + 1) for the same bound on f.
- **The conclusion is still true.** f(λ) = −log(1 − λ) is convex with f(0) = 0, so f(λ)/λ is nondecreasing. Put
  u := C_sn and λ* := eᵘ/(1 + eᵘ) ≥ λ_max. Then for every eigenvalue λ_i ≤ λ_max ≤ λ*:

  f(λ_i) ≤ λ_i·f(λ*)/λ* = λ_i(1 + e^{−u})log(1 + eᵘ) ≤ λ_i(u + 1/e + 2 log 2) ≤ λ_i(u + 2).

- **Fix.** Replace step 3 with this two-line argument. There is no need for f(λ_max) ≤ C_sn + 1 or for a case
  split.

**F3 (Minor). §4.1 Lemma Tr step 1.**
- **Issue.**
  - Lemma H (§5.2) is stated for a *finite* deletion set E′, but A = (J, ∞) is infinite.
  - "tr K_A = Σρ_n(l) = E_ν#(S ∩ A)" is asserted without saying why ρ_n(l) is the one-point probability.
- **Fix.** Add one sentence: "V : ℝⁿ → ℓ²(A) has rank ≤ n and Σ_{l∈A}‖V_l‖² = Σ_Aρ_n(l) ≤ n. So the Gram form and
  Sylvester hold verbatim, and det(I − K_A) is a finite product. By Lemma H with E′ = {l},
  ρ_n(l) = 1 − D_n(ν∖{l})/D_n(ν) = P_ν(l ∈ S)."

**F4 (Minor). Remark L′1 ("What remains: … between o(K²/log K) and O(βK²)"), README status bullet ("Open window:
between that and N‴'s e^{−βk} threshold") and LOG Plan-25 "Remaining window".**
- **Issue.** The two conditions are of different types, so "between" is not an ordering.
  - (LG*) is a sum condition off a deletable set of small upper density. It absorbs any density-zero family, however
    tiny its gaps, for example g_k = e^{−k²} on a density-zero set.
  - N‴ is a pointwise condition on a set of positive upper density.
- **Fix.** Phrase the open case as: "gap sequences that satisfy neither (LG*) nor d̄(T_β) > 0 for any β. For example,
  g_k = e^{−k/log k} on half of all k, where Σ log(1/g) ≍ K²/log K."
  - Optionally record the heuristic target from N‴1: Σ min(log⁺(1/g), K) = o(K²).

**F5 (Minor). check_trunc.py / §4.1 NUMERICAL header.**
- **Issue.**
  - "ν" in the script is truncated at Ka = 40n atoms, not the infinite measure.
  - Item [2] checks the convexity inequality with the computed λ_max. That inequality holds automatically for any
    PSD contraction, so it does not test the C_sn + 2 constant.
- **Measured.** Replacing Ka = 40n by 80n changes log D_n(ν_J)/D_n(ν) by ≤ 2.2·10⁻⁴ at n = 6, 8 (400-digit Hankel
  check).
- **Fix.** State "ν truncated at 40n atoms (moving the cutoff to 80n changes the values by < 10⁻³)". Describe [2]
  as "the sharp convexity bound with the true λ_max (a sanity check)".

**F6 (Minor). §0 status row L′, "Depends on".**
- **Issue.** The row lists G3′-L, Lemma Tr, Lemma K, Lemma W. The final sentence "With G3′-U, G3′ holds" also uses
  G3′-U.
- **Fix.** Add G3′-U, or say "(lower half)". Optionally list Lemma Tr as its own row (PROVED from Lemma H, Lemma K;
  status as L′), since Remark L′2 presents it as a reusable tool.

**F7 (Info). Theorem L′ step 3.**
- "a near pair costs ≤ log⁺(1/g_a) + log(C log γ̃_a)" means the positive part of minus the log of the ratio. The
  constant C absorbs 4C₀/2π and the replacement of log(γ_a/2π) by log γ̃_a + O(1) (Z1).
- Correct as is. A parenthetical would help a reader.

**F8 (Info). Theorem L′ step 4.**
- The hypothesis is used at the single scale K = Mn, with M fixed before n → ∞. That is legitimate.
- The resulting o(n²) depends on (M, η), and the later limits are taken in the right order.
- Optionally make this explicit: "for fixed M and η, as n → ∞".

**F9 (Info, suggested remark). Consistency of L′ with N″/N‴.**
- (LG*) forces E − 1 ⊂ B_η for every η, so d(E) = 0.
- If d̄(T_β) = θ > 0, then T_β ∖ B_η has upper density ≥ θ − η, and Σ_{k≤K, k∉B_η}log(1/g_k) ≥ β(θ − η)²K²/2 for
  infinitely many K. This contradicts o(K²/log K).
- So (LG*) ⇒ d(E) = 0 and d(T_β) = 0 for all β, as the necessity theorems require. A one-line remark would make the
  sandwich visibly consistent.

## Independent checks (scratch, `/tmp/…/scratchpad/p25rev/`)
- `a_hankel.py`:
  - Hankel moment determinants at 400 digits, n = 6, 8, J ∈ {2n, 4n}, Ka ∈ {40n, 80n}. They agree with the Gram
    determinant in `.out`, and the Ka sensitivity is ≤ 2.2·10⁻⁴.
  - Lagrange product and Σ|ℓ_i| at tail points for n = 4, 8, 16, 32. Both are far below (8e)^n.
- `b_growth.py`: log det(I − K_A) and tr K_A for n = 8, 16, 24, 32 and J ∈ {2n, 4n, 8n}, at 150 digits. The table
  is in F1. Σρ_n = n to 12 digits.
- Re-run of `check_trunc.py`: byte-identical to `check_trunc.out`.

## Recommended labels (after F1–F6 are applied)
- **Lemma Tr:** PROVED (from Lemma H, Lemma K, Lemma W) + REVIEWED.
- **Theorem L′:** PROVED-mod-cite (C1) + mod-input (LG*), Theorem H; REVIEWED; novelty UNCHECKED.
- **Status row L′:** drop "Rule R pending" and cite this file.
- **README and LOG:** "in review" → "REVIEWED (review/REVIEW_Plan25.md)", with F4's rewording of the open window.

## Re-check (commit 78999d5)

I checked each fix against the diff bbf2fed..78999d5. `check_trunc.out` is unchanged, since the edit to
`check_trunc.py` touches only the docstring.

- **F1 ✔.** The numerics bullet now reports order-n² truncation, with the n ≤ 32 figures, and the false "O(1)" remark
  is gone. The figures quoted for n = 16 (tr K_A = 1.5 and log det = −5.6 at J = 2n) match the `.out`.
- **F2 ✔.** Step 3 now uses "f(λ)/λ is nondecreasing", λ* ≥ λ_max and f(λ*)/λ* = (1 + e^{−u})log(1 + eᵘ) ≤ u + 2.
  This is correct: the left side is ≤ u + 1/e + 2 log 2.
- **F3 ✔.** The finite-rank / trace-class sentence, with finite approximations A_N ↑ A, and ρ_n(l) = P_ν(l ∈ S) via
  single-deletion Lemma H are both in.
- **F4 ✔.** The README, Remark L′1 and LOG no longer speak of "between".
- **F5 ✔.** The cutoff and the scope of [2] are now stated, both in the docstring and in PROOF.md.
- **F6 ✔ with one residual (R1).** The L′ row lists G3′-U and Lemma Tr has its own row, but the Tr label needs a fix.
- **F7, F8 ✔.**
- **F9 ✔.** The remark is brief but correct. If T_β ∖ B_η had upper density θ′ > 0, the summands ≥ βk would give a
  sum ≥ βθ′²K²/2 infinitely often. So d̄(T_β) ≤ η for every η. The d(E) = 0 part follows from E − 1 ⊂ B_η.

### Residual items
- **R1 (Minor; my own error in the first-pass label recommendation).** Lemma Tr uses Lemma K. Lemma K is
  PROVED-mod-input Theorem H (status row "R, K"), because its fraction bound needs Theorem H's lower half for D_n(ν).
  - So Lemma Tr is **PROVED-mod-input Theorem H**, not "PROVED".
  - Alternatively, it is unconditional for v_j = j⁻⁴ only if both of the following are argued:
    - Lemma W supplies the lower bound in Lemma K's proof;
    - H7's tail bound itself does not use Theorem H.
  - Simplest fix: label it mod-input Theorem H.
- **R2 (Trivial).** The §4.1 heading says "PROVED-mod-cite", while the table row says "PROVED-mod-cite (C1)". Add
  "(C1)" to the heading.
- **R3 (bookkeeping, at merge).** Set README "in review", LOG "Re-check pending" and the status-row / heading
  "re-check pending" to REVIEWED.

### Re-check verdict: ACCEPT
This is conditional only on R1–R3, which are label and bookkeeping edits. No mathematical issue remains.

**Final labels.**
- **Lemma Tr:** PROVED-mod-input Theorem H (via Lemma K / item 11 H7); depends on Lemma H and Lemma K; REVIEWED.
- **Theorem L′:** PROVED-mod-cite (C1) + mod-input (LG*), Theorem H; depends on G3′-L, G3′-U, Lemma Tr, Lemma K and
  Lemma W; REVIEWED; novelty UNCHECKED.
