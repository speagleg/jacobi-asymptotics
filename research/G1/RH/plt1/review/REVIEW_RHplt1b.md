# Rule R review: RH_plt1b.md (Plan 15b, seam construction, 0 < p < 1)

Reviewer: independent agent, fresh context (worktree `ja-plan15`, branch `plan-15-p-lt-1`). Read: AGENTS.md,
VERIFICATION_POLICY.md, RH_plt1b.md, RH_plt1.md (incl. §0 amendments table), REVIEW_RHplt1.md (incl. Re-check), RH_px.md
(in full), CITATIONS.md (DLMF, DLMF-2, KMVV quotes incl. the angle-freedom quote), the three checks and their outputs.
Re-derived Lemma S by hand. Re-ran `check_plt1_seam_e2e.py 0.75 2 10` (10 min 44 s). Ran scratch probes (not committed):
the seam probe and the RH_plt1 B-probe on extra points near −1.5, and the size of X for p ∈ {0.2, 0.4}, N up to 10⁶.

## Verdict: **ACCEPT WITH FIXES**

The seam construction is correct and is a real simplification. F is continuous across the seams, jump-free on
(−∞, 0), has D·K's jumps on the positive axis, and tends to F_∞ = (2πN)^{−1/2} at ∞. **Lemma S(iii) does not need
numerics.** It follows from principal-branch bookkeeping (F2), so the "modulo NUMERICAL" can be dropped.

The write-up repeats RH_plt1's F2 error, though. With the stated θ_s = πp/2, the KMVV lips at ±π/3 leave S_in for every
p ≤ ⅔, not only for p ≤ ⅓. That includes the tested p = 0.4 (F1). The fix uses the KMVV angle freedom that is already
quoted. It is a one-line change and does not alter the theorem. The other findings are minor: X is bounded for each N
but not uniformly in N (F3), plus missing rate terms, a Rule C/Hölder gap for X, and numerics hygiene. One side finding
is outside this item: the RH_plt1 §5 entries at z = −1.5 + 10⁻⁴⁰i are a quadrature artifact (F6).

## Findings

### F1 (major: false as written for ⅓ < p ≤ ⅔; easy fix). Lip angle versus θ_s = πp/2
- **Location:** §1 ("θ_s := πp/2"); §2 "Lens angle" ("For p ≤ ⅓, take the Ψ-rays … θ_L < θ_s").
- **Problem.** With KMVV's angle 2π/3 the lips leave 0 at arg z = ±π/3 (f′(0) < 0; RH_px Lemma 4.1). They lie in
  S_in = {|arg z| < πp/2} only if π/3 < πp/2, i.e. **p > ⅔**.
  - For ⅓ < p ≤ ⅔ the text keeps the KMVV angle, so the lips cross the seam into S_out. There D̃ (hence F̃, w₀'s
    continuation, and the inner W̃) is not available, and the lip jumps are not "reproduced exactly".
  - Example: p = 0.4 has θ_s = 36° while the lips sit at 60°. This is the e2e case, and the e2e test does not see it
    (Ω_∞ only).
  - The "p ≤ ⅓" threshold would be right only for some θ_s ∈ (π/3, πp), which is RH_plt1's θ*. Everything else in the
    item (the winding check, the e2e probe, the seam-jump constant sin(θ_s/p) = 1) uses θ_s = πp/2.
- **Fix:** for **all** 0 < p < 1, take θ_L := πp/4 and θ_s := πp/2. The KMVV ζ-ray angle is then π − θ_L ∈ (0, π),
  which is covered by the quote.
  - Lemma 4.3 lip constant: c = 2π sin(θ_L/p) = 2π sin(π/4).
  - (Equivalently, θ_L := min(π/3, πp/4).)
  - State in §2 that the lips at ±θ_L, the band lens in U(0, δ), and the Ω_b/Ω^△ contours outside U(0, δ) all lie in
    S_in. For the last of these, choose the lens and Σ^△ heights at Re z ≥ δ below δ·tan(θ_s)/2. This is p-dependent and
    N-free. The top closing segment at N^p + δ′ ± iδ has arg ≈ δ/N^p, so it fits.

### F2 (upgrade: Lemma S(iii) is provable, so the NUMERICAL caveat can be removed)
- **Location:** Lemma S(iii).
- **Proof (any θ_s ∈ (0, πp)).** On Γ₊ put arg t = −θ_s/p ∈ (−π, 0). Write

    L₊ = −μ(t) − Log(1 − e^{−2πit}) + c·Log(1 + z) − ½Log(1 − z/(2πN)),

  with μ(t) := ½log 2π + (t − ½)Log t − t − LogΓ(t) and every Log principal.
  - **Each term is continuous on the open ray.**
    - μ is analytic on ℂ ∖ (−∞, 0], since LogΓ is principal (DLMF 5.11.1 setting).
    - |e^{−2πit}| = e^{2π Im t} < 1, so 1 − e^{−2πit} stays in the disc |w − 1| < 1.
    - 1 + z avoids (−∞, 0], since arg z = θ_s ∈ (0, π).
    - 1 − z/(2πN) is never real ≤ 0, since Im ≠ 0.
  - **Each term → 0 as z → 0.** Here t → ∞ (DLMF 5.11.1). So this sum *is* the continuous determination vanishing at 0.
  - **The sum → 0 at ∞.** As z → ∞:
    - t → 0, and −μ = ½log 2π + ½Log t + O(|t|log|t|), using LogΓ(t) = LogΓ(1 + t) − Log t;
    - Log(1 − e^{−2πit}) = log 2π + iπ/2 + Log t + O(t), since π/2 + arg t ∈ (−π/2, π/2);
    - c·Log(1 + z) = c·Log z + O(1/z);
    - Log(1 − z/(2πN)) = Log z − log 2πN − iπ + O(N/z), since arg(1 − z/2πN) → θ_s − π ∈ (−π, 0).
  - Collecting terms, with Log t = log N − Log z/p:
    - the real part is (1/(2p) + c − ½)log|z| + (−½log 2π − ½log N + ½log 2πN) = 0;
    - the imaginary part is θ_s/(2p) − π/2 + cθ_s − ½(θ_s − π) = 0.
  - Γ₋ follows by conjugation. ∎
- **Consistency.** The committed winding check sums exactly these principal logs. Its unwrapping never fired: the end
  value equals the raw value, ≈ 10⁻³¹. So the check is consistent with the proof.
- **Fix:** replace (iii) by this proof. Drop "modulo NUMERICAL" from §3, and keep `check_plt1_seam_winding` as a
  consistency check. (Also drop the "N-independent in t" sentence. B_in/B_out is N-free only asymptotically, so that
  sentence is imprecise and not needed.)

### F3 (minor; must be stated). X is bounded for each N, not uniformly in N
- **Location:** §1, "X is bounded and Hölder".
- **Problem.**
  - On the seam, L ≈ c·log|z| for 1 ≪ |z| ≪ N^p and ≈ ½log(|z|/N) for N^p ≪ |z| ≪ N. So max|L| ≍ log N.
  - X(0) is dominated by (1/π)∫Im L₊dr/r, so X = O(log N).
  - Scratch probe at p = 0.4: X(0) = −1.24, −1.93, −3.31, −4.70 for N = 10, 10², 10⁴, 10⁶. At p = 0.2 it is −1.66 … −6.26.
    In both cases max|L| grows like log N.
  - But X(2) − X(1) converges: 0.206, 0.264, 0.298, 0.303 at p = 0.4, and 0.40 … 0.79 at p = 0.2.
- **Why it is harmless.**
  - e^X = N^{O(1)}.
  - Constants in X cancel between w₀'s Szegő function, D_{w,∞} and C_∞. That is the same mechanism as RH_plt1 F3: "only
    N-uniform Hölder bounds of log h_N mod constants".
  - The uses outside the conjugated frame are the top end and Lemma 3.5. The top end only needs poly(N) ≪ N^{pN}, since
    |X(z) − X(x)| = O(log² N) even at |z| ~ N^p. Lemma 3.5 is for fixed N.
  - The N-uniform modulus of X − X(0) on compacts holds because ∫|L(ζ)||ζ|^{−2}|dζ| is N-uniformly bounded.
- **Fix:** state "|X| = O(log N), and X − X(0) has N-uniform Hölder/Lipschitz bounds on compacts". Add the
  corresponding entry (h_N mod constants) to the amendments list.

### F4 (minor). Rates and a misstatement in §1/Lemma S
- (ii) omits B_out's correction. D·B_in/B_out = 1 + O(N|z|^{−1/p}log|z| + 1/|z| + **N/|z|**). The density is still
  O(1/|ζ|) for fixed N, so X → 0.
- §1, first bullet: "D = 1 + O(1/|t|)" is false near the positive axis, where D has poles at the nodes. Say
  D̃ = 1 + O(1/|t|) on S_in, and D = 1 + O(1/|t|) on closed subsectors ε ≤ |arg z| < θ_s.
- (i): min(1, 1/p) = 1 for p < 1. Write O(|z|).

### F5 (minor; Rule C / proof completeness). Boundary behaviour of X
- **Problem.** "Bounded and Hölder up to the seams, Hölder at 0" and Plemelj are asserted without a citation or proof.
  RH_px Lemma 3.4 covers real-axis contours only. Here the contour is two rays meeting at a corner 0.
- **What I checked.** The density L± is real-analytic on the open rays, Lipschitz at 0 with L(0) = 0, and O(1/|ζ|) at ∞.
  - Orientation: Γ₊ outward has S_out on its left, so X_out − X_in = L₊. On Γ₋ the minus sign gives X_out − X_in = L₋.
    Correct.
  - Continuity at 0 holds, since the density vanishes there. X(0) = (1/2πi)Σ±∫L±dζ/ζ, the same from all sectors.
- **Fix:** add "Lemma 3.4 (half-line case), applied to each ray after rotation", or quote Muskhelishvili/Gakhov with
  hypotheses. Also add RH_plt1b to the "Used in" line of the DLMF 5.11 entry.

### F6 (minor; numerics, Rule N). The p = 0.75 row, and a side finding on the REVIEWED RH_plt1 §5
- **No committed output.** The (0.75, 2) row of the §4 table has no `.out` file (Rule N3: values must be computed, not
  typed).
  - My re-run reproduces it digit for digit: 0.39103, 0.2906, 0.18981, 0.16133, 0.16037, 0.16102, 0.29269, 0.032335,
    0.060432, 0.26689, 0.33194; N^p b_N/c = 0.9522058151.
  - Commit the output. "Stays O(1/N) at −1.5" cannot be concluded from one N; either drop it or add N = 20.
- **Theory gives exact agreement.** For ½ < p < 1, G := (D·B_in·e^X in S_in, B_out·e^X in S_out) and RH_plt1's D·B have
  the same jumps: those of D on (0, ∞), and none elsewhere. Both are bounded and nonzero at 0 and ~(−z)^{1/2} at ∞.
  So by Liouville G = const·D·B, and the two probes must agree **exactly** at every point.
- **They do, except at one point.** I ran both probes on extra points (p = 0.75, N = 10).
  - At 0.6 + 0.45i, 0.6 + 0.55i, −1.5 + 0.05i and −1.5 + 0.3i, both give 0.3148, 0.31416, 0.1613 and 0.16021.
  - At −1.5 + 10⁻⁴⁰i the seam probe gives 0.16133, but the B-probe gives 0.28323.
  - So the RH_plt1 §5 "−1.5" column (0.283/0.280/0.278; probably also 0.734/0.752/0.761 at (0.6, 2.5)) is an artifact of
    `check_plt1_e2e.py`. Its S(z) quadrature has the kernel pole 10⁻⁴⁰ off the contour and misses the half-residue.
    Since ℓ̂(−1.5) = O(1/N), the error is O(1/N) and N·err looks "stable", which is why REVIEW_RHplt1 did not catch it.
- **Fix:** in RH_plt1b §4, say that the seam and B-constructions agree to all printed digits off the axis (Liouville
  identity), and that the seam value at −1.5 is the correct one. **Flag to the RH_plt1 owner:** correct the −1.5 column of
  RH_plt1 §5, or move the point to −1.5 + 0.05i. This affects no proof step.

### F7 (minor; scope of evidence). The e2e gate is Ω_∞ only
- **What it does test.** Both sectors of F: for p = 0.4, 4.5 + 1.5i, 3 − 1.2i and 15 + 8i lie in S_in, the rest in
  S_out. It also tests X, the seam continuity implicitly, w₀ with B_in·e^X, and C_∞.
- **What it does not test.** The new parts:
  - the glued W̃ with B_out·e^X;
  - the KMVV ray angle π − θ_L;
  - P₀N^{−1} on ∂U(0, δ);
  - the seam mismatch inside U(0, δ).
- With F1's θ_L = πp/4 these are exactly the untested pieces.
- **Recommended (not blocking):** port `check_px_bessel.py` [B] to p = 0.4 (or 0.25) with θ_L = πp/4 and the glued W̃.
  Also note the pending N = 40 row.

### F8 (minor). Branch of W̃ and the seam-jump formula
- **Location:** §2, hard edge.
- **Problem.** The two W̃'s are written as (…/(·)²)^{1/2}. The claimed ratio D̃/D, rather than −D̃/D, needs a branch
  convention.
- **Fix:** define W̃ := (C(−z)^{α_x}(4c − z))^{1/2}/G̃, with G̃ = D̃·B_in·e^X in S_in and B_out·e^X in S_out, and one
  principal root. Then W̃_out/W̃_in = D̃/D = 1 − e^{∓2πit} exactly, with |e^{∓2πit}| = exp(−2πN|z|^{−1/p}) at
  θ_s = πp/2.

### F9 (cosmetic)
- §2: "Σ^△ and the band lens near 0 are thin" is wrong, since Σ^△ is not near 0. See F1 for the correct containment
  statement.
- The title says "0 < p ≤ ½", but the theorem covers 0 < p < 1. Align them.
- (Y4)_x: only φ₀ < πp is needed (Im θ < 0 on 0 < arg s < φ₀; Im θ > 0 on its mirror). φ₀ < θ_s is fine but stronger than
  necessary.
- The KMVV angle-freedom quote is the authors' remark without proof. It is acceptable as a citation, but say that (6.23)–
  (6.25) are used with the sectors |arg ζ| < π − θ_L, etc. The Bessel and Hankel asymptotics hold uniformly there.

## Checked and OK
1. **Lemma S(ii) phases** (Γ₊).
   - t^{−1/2} = N^{−1/2}z^{1/(2p)}, so D·B_in ~ −iN^{−1/2}z^{1/2}/√(2π).
   - −iz^{1/2} = |z|^{1/2}e^{i(θ_s−π)/2} = (−z)^{1/2} (principal, arg(−z) = θ_s − π).
   - B_out = (−z/2πN)^{1/2}(1 − 2πN/z)^{1/2}, consistent branch.
   - The ratio → 1. Γ₋ follows by conjugation.
2. **No hidden power or monodromy at ∞.**
   - F_out = B_out·K·e^X → (2πN)^{−1/2}, since K ~ (−z)^{−1/2} with no cut on (−∞, 0).
   - The probe gives F_∞ = 0.12615663 = (20π)^{−1/2} at N = 10 for both p = 0.4 and p = 0.75, as predicted.
   - κ := F^{−1}e^{N(g − log z)} is jump-free in |z| > N^p + δ′: the seams are continuous; on (−∞, 0) the 2πiN jump is
     trivial; on the positive axis D's e^{2iθ}·K's (−1)·(−1) matches g's 2iθ/N.
   - So κ is analytic at ∞ (Lemma 3.5 logic, fixed N).
3. **Branch points.**
   - z = −1 (B_in) lies in S_out, and B_in is used only on S̄_in, including the seams, which avoid (−∞, −1].
   - z = 2πN > N^p (B_out) lies in S_in, where B_out is not used. Neither point matters.
4. **Positive-axis jump structure.** B_in, e^X and (in S_in) the absence of seams leave exactly D's and K's jumps.
   RH_px Lemma 3.3(ii) on (N^p + δ′, ∞) and the band/V^△ structure are unchanged.
5. **Plemelj orientation and F's continuity** across Γ± (F5).
6. **Seam jump of W̃** = D̃/D, super-small with constant sin(θ_s/p) = 1.
   - The E^a + Φ split and removability transfer: B_in, B_out → 1 and e^X → e^{X(0)} from every sector, so D_w/W̃ is
     bounded above and below.
   - Outer W̃ is analytic across (−δ, 0): (−z)^{α_x}, B_out and e^X are analytic there, and f^{1/4} > 0.
7. **(Y4)_x without p > ½.** Correct. The p > ½ use in RH_plt1 came from the quadrant, which the G-sector argument does
   not need.
8. **Large α_x for small p** (e.g. α_x = 19 at p = 0.05, s = 2). KMVV requires only α > −1, and O1/removability are
   α-uniform in form.
   - μ* and B* are G2's for every p > 0.
   - c(p) via Γ(1/p + ½)/Γ(1/p + 1) is fine.
   - Lemma 2.2 signs are local to the axis, and Lemma 4.3 lips satisfy Re φ̃ ≈ π sin(θ_L/p)|z|^{−1/p} > 0.
   - Scope "all 0 < p < 1" is justified for each fixed p, after F1. The constants (δ, lens heights) depend on p.
9. **Winding check code.** Principal formulas, Binet for |t| > 10³ (remainder < 10⁻¹⁸), per-step assert < 0.5 rad. Valid
   for small p even though |t| spans ~10^{±800} at p = 0.05: everything stays on μ's principal domain (F2).
10. **The p = 0.4 e2e out file** matches the §4 table (N = 10, 20), with N·err stable. The (0.75, 2) N = 10 row was
    re-run and reproduced (F6).
11. **Baseline** `check_plt1_phase0_small.out` (p = 0.4, 0.3, 0.25) is consistent with d₁ = −(s − 1)/2 at n ≤ 200, where
    K-stab ≤ 1.3e−9.

## Recommended label
After F1 (required) and F2–F5, F8 (text):

**Theorem RH_p, 0 < p < 1, s > 1: PROVED-mod-cite (RH_px's cites: WLXZ v1 §§3–5, §6.1; KMVV §6 incl. (6.42)–(6.53)
and the §6 angle-freedom remark; G2 μ*/B*; DLMF 5.11.1/§5.11(ii)), pending re-check of F1–F5, F8.**
- With F2 adopted there is **no** NUMERICAL modulo for the seam route. Until then: "modulo the NUMERICAL Lemma S(iii)".
- Novelty: UNCHECKED.
- F6 (commit the output; RH_plt1 §5 artifact) and F7 (hard-edge numerics) are recommended, not blocking.

## Re-check (commit e3b5ae0)

| Fix | Status | Notes |
|---|---|---|
| F1 | VERIFIED | θ_L = πp/4 and θ_s = πp/2 for all p. Containment covers the lips, the band lens in U(0, δ), lens/Σ^△ heights < δ·tan(θ_s)/2, and the top segment. Lip constant 2π sin(π/4). |
| F2 | VERIFIED | The proof of Lemma S(iii) is reproduced correctly (real and imaginary cancellation at ∞, continuity of each principal term). The NUMERICAL caveat is dropped, and the winding check is kept as a consistency check. |
| F3 | VERIFIED | X = O(log N); X − X(0) is N-uniformly Lipschitz on compacts; constants cancel; the top end needs only poly(N). |
| F4 | VERIFIED | The N/|z| term is added. The D vs D̃ statement is corrected. (i) reads O(\|z\|). |
| F5 | VERIFIED | Plemelj orientation stated. Lemma 3.4's half-line case is applied per ray. X(0) is the same from every sector. |
| F6 | PARTIAL | See R1–R2. The Liouville identity and the RH_plt1 §5 correction note are present. |
| F7 | VERIFIED | Scope statement in §4. Hard-edge numerics are still recommended. |
| F8 | VERIFIED | W̃ = (C(−z)^{α_x}(4c − z))^{1/2}/G̃ with one root. The seam ratio is exactly D̃/D. |
| F9 | VERIFIED | Title is "all 0 < p < 1". (Y4)_x needs only φ₀ < πp. The KMVV sector usage is stated. |

**Residual items (non-blocking, hygiene):**
- **R1.** `checks/check_plt1_seam_e2e_p075s2.out` is committed **empty** (0 bytes).
  - The §4 table no longer has a 0.75 row. But §4 and RH_plt1 §5 now rest on the reviewer's scratch runs (Liouville
    agreement; 0.161 at −1.5), and those are not committed.
  - Fix: commit a real output, e.g. `check_plt1_seam_e2e.py 0.75 2 10`, about 11 min; the reviewer's run reproduced
    0.39103 … 0.33194 and gave 0.16133 at −1.5. Or delete the empty file and label those statements "reviewer scratch run".
- **R2.** The RH_plt1 §5 correction declares the (0.6, 2.5) −1.5 entries (0.734/0.752/0.761) artifacts too. Only (0.75, 2)
  was verified. The mechanism is the same, so this is very likely right, but write "presumably also", or re-run the B-probe
  at −1.5 + 0.05i for (0.6, 2.5).
- **R3.** CITATIONS.md:
  - the KMVV angle-freedom "Used in" line still says "For p ≤ ⅓ … π − θ_L". Update it to "all 0 < p < 1, θ_L = πp/4";
  - the DLMF 5.11 "Also used in" line should add RH_plt1b (Γ(t) on S_in; Lemma S(iii)).
- **R4.** The status lines (header, §3) still say "pending re-check". Update them to REVIEWED.

**Label (re-check): Theorem RH_p, 0 < p < 1, s > 1 — PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6 incl. (6.42)–(6.53)
and the §6 angle-freedom remark; G2 μ*/B*; DLMF 5.11.1/§5.11(ii)), REVIEWED, with no numerical caveat.**
- Novelty: UNCHECKED.
- R1–R4 are hygiene and do not affect the label.
- Hard-edge numerics (F7) are recommended.
