# Rule R review — Plan 53 (GAP-int, boundary frame: folding the symmetric p = 1 problem)

Reviewer: independent second reader (Rule R). Branch `plan-53-r2bnd`, commit bd810e1 (`git diff master...HEAD`).
Targets: `research/G1/RH/route2/ROUTE2_bnd.md`; PROOF.md §3.22 and the §0 row "RII₁ᶠ / B_{p=1}^{all}"; LOG.md entry; CITATIONS.md
"(WLXZ-v1, Plan 53)" and "(Fold-attrib, Plan 53)"; the note in ROUTE2_p1.md §7; checks `route2/checks/check_bnd_{fold,coeff}`.
Plan: docs/superpowers/plans/2026-10-14-plan-53-r2bnd.md (Review focus). Also read: ROUTE2_p1.md §§2–3 (LW1₁, comparison problem),
RH_p1_general.md (statement/range), px/RH_px.md §3 (transformations), CITATIONS.md WLXZ entries; and, in the master checkout
(read-only), PROOF.md §3.23 (Plan 54) and review/REVIEW_Plan54.md. Context: master has since merged Plan 54 (REVIEWED), which
closes GAP-int by a different global frame. This branch predates it.

## Overall verdict: **ACCEPT WITH FIXES**

No mathematical error found in the main line. The fixes are about integration with Plan 54 (framing, names, the statement of
what is shared) plus LOW/INFO items on citations, wording and numerics.

| Item | Verdict | Label recommended |
|---|---|---|
| §1.1 range check (option iii) | ACCEPT | PROVED (reading of RH₁(r)) |
| §1.2 weaker targets | ACCEPT | PROVED (bookkeeping) |
| §1.3 Remark Div | ACCEPT (honestly labelled; F9 wording) | HEURISTIC + NUMERICAL |
| §1.4 option (i) | ACCEPT WITH FIX (F5 wording) | OBSTRUCTION (heuristic), not pursued |
| §2.1 Lemma F0 | **ACCEPT** (re-derived; F4 convention note) | PROVED (self-contained) + NUMERICAL |
| §2.2 Lemma P | **ACCEPT** (every factor re-checked against the PDF; F3 additions) | PROVED-mod-cite (WLXZ v1) + NUMERICAL |
| §2.3 Lemma FS | ACCEPT | PROVED |
| §2.4 Lemma FJ | ACCEPT (F10 range sentence) | PROVED-mod-cite |
| §2.5 Lemma FN | ACCEPT | PROVED + NUMERICAL |
| §2.6 Lemma Fφ | ACCEPT | PROVED-mod-cite |
| §2.7 Lemma FY | ACCEPT | PROVED-mod-cite |
| §3 H1ᶠ, LW1ᶠ, URᶠ, Q^x ∈ I + ∂C, Cᶠ, Dᶠ, extraction | ACCEPT | PROVED-mod-cite |
| **Theorem RII₁ᶠ** (p = 1, 1 < r < 3, (H_an₁)) | **ACCEPT** | PROVED-mod-cite: REVIEWED after fixes; a **second, partly independent proof** of the a_m, b_m part of Plan 54's RII_x1 on 1 < r < 3 (F1, F2, F6) |
| **Corollary B_{p=1}^{all}** | **ACCEPT** (the mathematics); **rename/reframe** (F1) | PROVED-mod-cite: REVIEWED after fixes, as a second proof of Plan 54's B_{p=1}^{all}, not a new closure |
| §4 Remark (β_n) | ACCEPT WITH FIX (F7) | PROVED (from CT₁ / Lemma D, REVIEWED), no rate |
| OBSTRUCTION-a (Plan 50), scoped | ACCEPT | unchanged, scoped to the symmetric band-centre frame |
| §5 Lemma IR | ACCEPT (checked; not used) | PROVED (not used); hybrid route HEURISTIC |
| Numerics | ACCEPT; both checks reproduced (F8, F9) | NUMERICAL |
| Novelty | — | UNCHECKED (no Rule L) |

## 1. Rule C: citation check (arXiv:1410.3948v1 re-fetched by the reviewer, 2026-10-14; pdftotext -layout, and page 10 rendered as an image for (4.12))

- (2.1) ψ, (2.2) g with "arg(z − s) ∈ (−π, π)", (2.3) φ and l, (2.6) D with the branch "−1/z² = e^{±πi}/z² for z ∈ ℂ±, with
  arg z ∈ (−π, π)": **match**.
- (3.2) the nodes ±X_k in (−√(n/α), √(n/α)); (3.6) Π = sin θ/γ; (3.7) θ = nπ/z² − πα, γ = −2nπ/z³; (3.9) U±: **match**.
- Figure 3 caption and the sentence "we choose the contour like Σ_{l,±} and Σ_{r,±} so as to avoid the zeros of Π(z) and w(z)":
  **match**. The figure is symmetric under z ↦ −z.
- (4.4), (4.5): **match**.
- **(4.12)**: the rendered page shows Q := T × {−𝒱^△₋ on Ω^△_{l,+} ∪ Ω^△_{r,−}; 𝒱^△₊ on Ω^△_{l,−} ∪ Ω^△_{r,+}; 𝒱₊ on Ω_{l,+} ∪ Ω_{r,−};
  𝒱₋ on Ω_{l,−} ∪ Ω_{r,+}; I on Ω∞}. **The Plan 53 transcription is correct, and the correction is right**: the RH_px entry's
  "−V₋(z), z ∈ Ω_{l,+} ∪ Ω_{r,−}" lost the △ superscripts. (pdftotext drops them too. The text alone would list Ω_{l,+} ∪ Ω_{r,−}
  twice, which shows they were lost.) The loss is in the quotation only: RH_px.md §3 uses V^△± in Ω^△± "with their signs" (line
  144), so no REVIEWED result is affected.
- (4.15) with its branch sentence and "non-zero analytic function on ℂ \ (−∞, 0]"; (4.18); (4.19) principal branches; (4.20)
  with "D(z)E(z) tends to n^{1/2−α}"; (4.22) "analytic in z ∈ ℂ \ [0, +∞), with the branch taken as arg(−z) ∈ (−π, π)":
  **match**.
- Gap (F3): the entry says (3.1) is "used as quoted in the two WLXZ entries above", but neither earlier entry quotes (3.1).
  (3.4) (w := n^{1/2}w_d(n^{−1/2}z)) and (2.14) (the residue form) are used implicitly and are not quoted either. The reviewer
  read all three in the PDF: (3.1) "U(z) := n^{nσ3/2}Y(n^{−1/2}z)", (3.4) "w(z) := n^{1/2}w_d(n^{−1/2}z)", (2.14) "Res_{z=±x_k}
  Y(z) = lim Y(z)[[0, w_d(z)], [0, 0]]".
- "(Fold-attrib, Plan 53)" is attribution only and is not used as input. Acceptable.

## 2. Verification of the mathematics

**Lemma F0.** Re-derived. Parity of the FIK matrix: Y₁₁ = π_{2m} even; Y₁₂ = C(π_{2m}ν) odd (s ↦ −s); Y₂₁ ∝ π_{2m−1} odd;
Y₂₂ = C(π_{2m−1}ν) even. Row 1: the even pairing gives z/(s² − x), hence z·C_x(P_mμ). Row 2: s²/(s² − x) gives C_x(x′P̃_{m−1}μ), and
xP̃_{m−1} = P_m + cP_{m−1} (orthogonality to x^j, j ≤ m − 2). det fold = det = 1 forces c′ = 1. μ = (y ↦ y²)_*ν has the full masses
k^{−r}Ψ₁(k) at 1/k. The constant Ψ₁(n) in q_n and WLXZ's normalisation of w do not change a_m or b_m. So **μ = σ_{r,Ψ₁} up to a
constant factor, exactly as claimed.** Convention: see F4.

**Lemma P.** Each factor was checked against the PDF.
- (a) w_d is a function of 1/z², so w is even; θ is even, γ is odd, Π is odd.
- U± ((3.9)): the (1,2) entry is odd, so U± is σ₃-even with the **same** ± on mirrored regions (θ is even and is not
  conjugated).
- U^△± = Π^{−σ₃}·(σ₃-even triangle): Π^{−σ₃}(−z) = −Π^{−σ₃}(z), so U^△±(−z) = −σ₃U^△±σ₃.
- (3.11) pairs Ω_{l,+} ∪ Ω_{r,−} and Ω_{l,−} ∪ Ω_{r,+}. Each pair is closed under z ↦ −z.
- (b) g(−z) = g(z) ∓ iπ needs only ψ even and ∫ψ = 1. Hence e^{−ng} and e^{2nφ} are even for n even.
- (4.12)–(4.13): 𝒱± has (2,1) entry ±e^{2nφ}/(2iγw), which is odd. 𝒱^△± = diag(e^{±iθ}/(2iγ), 2iγe^{∓iθ}) is odd and cancels
  U^△'s −1. The leading "−" in (4.12) multiplies a mirror-closed pair, so it does not affect parity.
- (c) D: the reviewer checked that both z ∈ ℂ₊ and −z ∈ ℂ₋ give arg(−1/z²) = π − 2 arg z. This is the principal argument, so
  D(−z) = D(z). D̂(z) = D̃(−z) holds literally from (4.15) and (4.22). E is even.
- In (5.1), the left/right regions pair with D̂ ↔ D̃.
- Contour admissibility: Re φ is even. The text does not show the Re φ̃ > 0 and Re φ̂ > 0 conditions of (5.8). The reviewer
  checked them from (2.4) and (4.28) with g′ odd: **φ̂(−z) = φ̃(z)** (F3).
- Plan 50's 𝔇 = D_aD_ϱ, F = H_n(z²)^a and q_n are even. The lips f^{−1}(arg ζ = ±π/4, ±3π/4) are symmetric (f is odd).

Lemma P is correct.

**Fold calculus / FS / FJ.**
- fold X = [[X₁₁, X₁₂/z], [zX₂₁, X₂₂]]. Multiplicativity is clear.
- Band at y < 0: z ↦ z² reverses the orientation. The folded jump [[0, −w_x], [1/w_x, 0]] is the inverse of the y > 0 jump,
  as required.
- Γ₊Γ₋ = x^α/|y|^{2a} = 1/|y| on both halves.
- Lip (2,1) entry: z(z²)^{−a} = x^{−α} for Re z > 0. KV's ω = (z²)^a is even, so the preimage at Re z < 0 gives the same folded
  jump.
- ℝ₋ (the image of iℝ) has no jump: near 0, iℝ lies between the lips, in the Ω∞-type region. Off 0, w and (z²)^a appear only
  in lens/△ factors, which do not touch iℝ. D (cut ℝ) is used only in Ω∞, off the real axis.
- **(Q^x₁)₂₁ = (Q₃)₂₁ − (Q₁)₂₁(Q₂)₁₁**, and the γ₁ terms of Γ cancel. Re-derived. This is consistent with Rule A (i). The
  combination contains (Q₁)₂₁, but it is estimated as a whole by the folded C–D integral, which is absolutely convergent.

**FN.**
- Singularity orders: O(|z|^{−1/2}) = O(|x|^{−1/4}) for row 1 of fold(N₀^{KV})Γ^{σ₃}, and the product is O(|x|^{−1/2}), so the
  singularity is removable. The constant is −i.
- [0, 4] coefficients from γ = 1 − 1/x − (3/2)x^{−2}: (N₁)₁₂ = i, (N₁)₂₁ = −i, (N₂)₁₂ = 2i, (N₁)₂₂ = 0. So a(N₀^x) = 2 and the
  product is 1.

**Fφ.** φ_W,₊(0) = l/2 − g₊(0) = −iπ/2, using half of ψ's mass on s > 0. −2nφ_KV = ±2inf ∓ iπn. f_K^{1/2} = ∓(i/2)f(√x) has
Re > 0 in ℂ±. The ζ-rays at ∓π/2 lie inside KMVV's angle freedom. f_K′(0) < 0 with band ↦ ζ < 0 matches KMVV's left-endpoint
orientation. All checked.

**FY.** The pairing gives fold U₁₂ = Σ2w(X_k)U₁₁(X_k)/(x − X_k²) under WLXZ's residue convention. γ/z = −2nπ/z⁴ = 2θ_x′ with
θ_x = nπ/x − π (α_W = 1). The difference 𝒦₋ − 𝒦₊ ≍ n|z|^{2a−1}|q_n| = n|x|^α|q_n|. Correct.

**§3.4 / column structure.** The naive bound, with V = O(1, log) and the factor 1/z in the (1,2) entry, would give
|x|^{−1/2} at a = ½, which is not in L². The correct bound uses FY's fold R₁₂ = O(1 + |x|^{α−η}), i.e. the one-sided
x-interpolation structure. With D^x_w ≍ |x|^{α/2}, this gives Q^x = O(|x|^{−|α|/2−2η}). The text does this, and the reviewer
confirms it. This is exactly where the fold gains over the symmetric frame.

**§3.1–3.5.** The folded local problem near 0 consists of:
- the constant band jump;
- no jump on ℝ₋;
- two lips at ±π/2 with (2,1) entry (D^x_w)²w_x^{−1}e^{2nφ^x}, plus (J2) entries that are diagonal and upper-right and of size
  O(e^{−cn/|x|}).

These are the only inputs ROUTE2's H1′/UR′(a), (b′), (d)/D′ use at the hard edge. Rule A (e) is complete. The ray angle ±π/2
changes only the constants of Lemma W on the star; Plans 51 (±πp/4) and 54 (±π/3) are precedents (INFO).

Other checks:
- LW1ᶠ: c_± = e^{∓iπα} from Φ_x(0) = −4, consistent with ROUTE2. LW1₁'s proof (ROUTE2_p1 §3.3) is independent of a (h_W, H_n,
  q_n only), so it holds on 1 < r < 3.
- Dᶠ: on |ζ| ≤ 2, ∫ε n|ζ|^{−|α|}|dζ|/n² = O(ε/n); on |ζ| ≥ 2 the bound is O(n^{−2} + ε/n). Correct.

**Extraction (§3.6).**
- fold_z of Y(n^{−1/2}z) = n^{−σ₃/4}·fold_y Y(x/n)·n^{σ₃/4}. h is even and h z^n → const, so the expansion is in 1/x. M is
  constant and lower triangular, and Q^x → I forces it to be diagonal.
- Invariance of a(Q) = (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂ under right multiplication by (1 + κ₁/x + …)^{σ₃}: the −κ₁ terms cancel.
  Re-derived.
- Scaling: Y_μ(x/n) gives nY₁ and n²Y₂, hence n²b_m² and n·a_m.
- Against the [0, 4] values: b_m = 1/(2m)(1 + O(1/m)) and a_m = (1/m)(1 + O(1/m)), i.e. c(1) = ½. Consistency check: the band
  in the original variable is [0, 4/n] = [0, 2/m], the same as RH_px/Plan 54's [0, b/N] with b = 2, N = m.

**Corollaries.** B_{p=1}^{bnd} = RedA + RII₁ᶠ. RedA's entire L₁ satisfies (H_an₁). B_{p=1}^{all}: r₀ ∈ (1, 3), then j steps
of SH-r (REVIEWED). Correct.

**Lemma IR.** FV⁺, plus the fact that the constant part of δ log k integrates to 0 against μ_n − μ_{n−1}, gives the bound.
Correct; not used.

## 3. Comparison with master's §3.23 (Plan 54) and REVIEW_Plan54

**Consistent.**
- Same statement on 1 < r < 3 (a_m, b_m, rate O(1/n)).
- Same band in the original variable.
- Same phenomenon at ℝ₋. Plan 53's "no jump on ℝ₋ (image of iℝ, Ω∞ uses WLXZ's D)" is the folded form of Plan 54's Lemma X1
  (D = exp μ(−N/z) analytic on ℂ ∖ [0, ∞)). Plan 54's Lemma X2 (RH_px's *quotient* construction fails at p = 1 through the
  continuation across (−δ, 0)) is not triggered here either: Plan 53 continues nothing across ℝ₋.
- Plan 54 lists "symmetrization (Chihara) = the RH₁(r) frame itself (OBSTRUCTION-a)" among its other routes. That is about the
  symmetric band-centre comparison and does not contradict Plan 53: Plan 53 symmetrizes, then folds back to x before comparing.
- The hypotheses differ only in the strip: (H_an₁) |Im u| < π versus (H_an^{x1}) |Im u| ≤ π/2. Both are met by RedA's entire
  L₁, so the corollaries coincide.

**Independent parts.**
- The global frame: WLXZ's symmetric chain plus Lemma P plus the fold, versus RH_px at p = 1 with Lemma X1 and the transfer table.
- The outer model: FN, versus the p = 1 RH_px outer model.
- The Airy disc: the fold of Plan 50/WLXZ §6.1 at +2, versus RH_px's at b = 2.
- The lip mismatch: LW1₁ (even-pairing Szegő integral) × the x^α factor, versus LW1-x1 = LW1′ with ν = ½.
- The g-function/equilibrium input: WLXZ's ψ, versus G2 μ*/B* at p = 1, including F1 of REVIEW_Plan54.

**Shared steps (a common failure point that would sink both at r = 2):**
- ROUTE2's α_x = 0 hard-edge comparison: H1′, the log local form of §3.2, **Lemma W′**, **UR′(a), (b′), (d)**, C′, D′ with the
  log² bound (Plan 48, REVIEWED);
- KMVV §6 (Bessel model, (6.28), angle freedom);
- C–D Theorem 4.4 and the arguments of 4.7/4.9;
- RH_px's invariance lemma and its (Y4)_x argument;
- RedA; §3.21 SH-r (r ≥ 3);
- WLXZ v1 itself (Plan 54 uses it through RH_px §§3–5).

The coefficient numerics are **the same computation**: check_bnd_coeff.out and Plan 54's check_x1_coeff.out agree in every
printed digit for n ≤ 800. They validate the law, not either route. So Plan 53 independently cross-validates the **global
frame**, but not the α_x = 0 local comparison on which GAP-int really rests (F2).

## 4. Numerics (re-run from the jacobi-asymptotics root)

- `check_bnd_fold.py` (2 s): output **identical** to the committed `.out`.
- `check_bnd_coeff.py` (3 min 39 s, all five truncations, r = 2, 2.5, 3, n ≤ 1600): output **identical** to the committed
  `.out`. The table in ROUTE2_bnd §6 matches it: spreads 4.7·10⁻⁸ / 5.2·10⁻⁹ / 3.7·10⁻⁹ (nB at n = 1600), E spread 6.6·10⁻⁸ at
  r = 2, baseline −(1 − ϑ_n)/2 = −0.408 at r = 2, n = 1600. Exception: the K-doubling sentence (F8).
- [1] F0 to 10⁻³⁹, and the β-relations a_j = β_{2j} + β_{2j+1}, b_j² = β_{2j−1}β_{2j} (0-based) to 10⁻⁴¹. These are genuine
  checks.
- [3] FN constant [[1, 0], [−i, 1]] for α_x = 0, 0.3, −0.4: genuine.
- [2] The g-parity test is genuine (−iπ to 4·10⁻¹⁰; ∫ψ = 1 − 7·10⁻¹¹). The D and D̂/D̃ tests are **tautological**: the code
  evaluates the same expression on both sides. These two parities rest on the analytic branch argument (re-derived above), not
  on [2] (F9).
- [4] compares model rank-one factors (KV Ψ_½ vs KMVV Ψ_0). The unfolded |·||ζ| → 0.31831 = 1/π (5 digits) and the folded
  |·|/(1 + log²) ≤ 0.126 are reproduced. It does not probe the folded problem itself.
- No end-to-end probe of the folded frame exists (e.g. Q^x ≈ N₀^x outside the discs from true OPs). It is optional (F9).

## 5. Findings

**F1 (MEDIUM; integration/framing).**
*Location:* ROUTE2_bnd.md title, label table rows "Corollary B_{p=1}^{all}" and "GAP-int (Plan 50) … closed", §4, §7
"Remaining"; PROOF.md §0 row and §3.22 heading/body; LOG entry; ROUTE2_p1.md §7 note.
*Issue:* Plan 54, now on master and REVIEWED, already closes GAP-int and uses the **same name "Corollary B_{p=1}^{all}"** for the
same statement. Merged as written, the repo would have two "GAP-int closed" claims and a name collision. `git merge-tree` also
reports textual conflicts (append-at-end) in LOG.md, PROOF.md and CITATIONS.md.
*Fix:*
- Retitle §3.22 / ROUTE2_bnd as "second proof (folded symmetric frame)".
- Rename the corollary, e.g. "B_{p=1}^{all,ᶠ} (second proof of §3.23's B_{p=1}^{all})", and B_{p=1}^{bnd} similarly.
- Change "GAP-int closed" to "GAP-int: second proof (closed by §3.23)".
- In the ROUTE2_p1 note, point to both §3.23 and §3.22.
- §3.22 and §3.23 can keep their numbers (master skipped §3.22). Resolve the append conflicts by keeping both entries in plan
  order.

**F2 (MEDIUM; independence statement).**
*Location:* ROUTE2_bnd §3.7 / §7; PROOF §3.22.
*Issue:* The text does not say what Plans 53 and 54 share. As §3 above shows, the decisive α_x = 0 step (ROUTE2 UR′(b′)/(d),
Lemma W′, D′ log²; KMVV; C–D) is common, and so are the coefficient numerics.
*Fix:* Add a paragraph "Relation to §3.23", listing the independent parts (global frame, outer model, Airy, LW1) and the shared
ones. State that a failure of ROUTE2's α_x = 0 comparison would sink both, and that the coefficient numerics are identical to
check_x1_coeff.

**F3 (LOW; Rule C).**
*Location:* CITATIONS "(WLXZ-v1, Plan 53)", last paragraph; ROUTE2_bnd §2.2 admissibility sentence.
*Issue:* (3.1), (3.4) and (2.14) are not quoted anywhere, contrary to "used as quoted in the two WLXZ entries above". The
admissibility claim cites (5.8) (Re φ̃ > 0, Re φ̂ > 0), but (a)–(c) do not cover φ̃ and φ̂.
*Fix:*
- Add the three quotes (verbatim text in §1 above).
- Add to Lemma P: "φ̂(−z) = φ̃(z) by (2.4), (4.28) and g′ odd, so (5.8) is mirror-invariant." Also quote (4.28): "φ̂(z) :=
  ∫_{−2}^{z}(−g′(s) ± 2πi/s³)ds for z ∈ ℂ±".

**F4 (LOW; convention).**
*Location:* §2.1 / §2.2 "Y_ν is σ₃-even (Lemma F0)".
*Issue:* Lemma F0 uses the FIK convention C(fν) = (2πi)^{−1}∫f dν/(s − z). WLXZ's Y uses the residue form (2.14), so Y₁₂ =
Σwπ/(z − x_k) = −2πi·C(πν). The two differ by a constant diagonal conjugation, which changes L but not σ₃-evenness, M's
diagonality or the invariance lemma.
*Fix:* One sentence.

**F5 (LOW; wording, §1.4).**
*Issue:* "Column-dependent exponents are excluded …", followed by "the fold … is the matrix-weighted space that works", reads
as a contradiction. On σ₃-even X, the norm ‖fold X‖_{L²(|dx|)} weights the entries by |z|, |z|^{−1}, |z|³, |z| (a row-and-column,
conjugation-type weight) on a subspace.
*Fix:* Say that a column weight on the full space is excluded heuristically, and that the fold restricts to σ₃-even functions
and changes variable. The label stays heuristic.

**F6 (LOW).**
*Location:* §3.7 "For 1 < r < 2 this is a second proof of Theorem RII₁"; Rule A (a) "third proof of RH₁(r)".
*Issue:* RII₁ and RH₁(r) also assert nβ_n = 1 + O(1/n), which is not obtained here.
*Fix:* "of the (a_n, b_n) part of RII₁ / RH₁(r)". Recount "third" in view of Plan 54.

**F7 (LOW).**
*Location:* §4 Remark (β_n).
*Issue:* The claim nβ_n → 1 has no label. Its index convention (Plan 50's a_m = β_{2m−2} + β_{2m−1}) differs from check [1]'s
0-based a_j = β_{2j} + β_{2j+1}.
*Fix:* Label it "PROVED (CT₁ ⟸ + Lemma D(b), REVIEWED; no rate)" and state both conventions.

**F8 (LOW; numerics wording).**
*Location:* ROUTE2_bnd §6.
*Issue:* "The K-doubling differences are ≤ 6·10⁻¹⁰" is false for E: 1.1·10⁻⁹ at r = 2.5 and 6.8·10⁻¹⁰ at r = 3. For nB it is
true (max 5.8·10⁻¹⁰).
*Fix:* "≤ 6·10⁻¹⁰ (nB), ≤ 1.1·10⁻⁹ (E)".

**F9 (INFO; numerics scope).**
*Issues:*
- check_bnd_fold [2]'s D and D̂ tests are tautological, so "WLXZ parities exact" (PROOF §3.22, LOG) overstates them.
- [4] probes model factors only.
- PROOF §3.22 "the rank-one factor times |ζ| is 1/π exactly" is a 5-digit numerical observation.

*Fix:*
- Say "g-parity numerical; D, D̂ parities analytic (branch argument)".
- Say "→ 1/π (5 digits)".
- Optional: add an end-to-end probe of the folded frame outside the discs (analogue of check_x1_e2e).

**F10 (INFO; range).**
*Location:* §2.4 (d), (e), §3.1 Airy, §7 (h).
*Issue:* Plan 50's non-local ingredients are stated for 1 < r < 2 and are used here on 1 < r < 3. These are W1(r) with the q_n
factors, the Airy discs with ϱ₁ = |x|^{2a}q_n, the (J2) bounds and LW1₁. The reviewer checked that their proofs do not use
|a| < ½: RH₁(r) holds for every r > 1, LW1₁ is a-free, and ϱ₁ is analytic near ±2 for every a.
*Fix:* Add one sentence to §7 (h).

**F11 (INFO).** KMVV rays at ±π/2 change only Lemma W's star constants; cite the Plan 51/54 precedents in §3.3.

## 6. Answers to the plan's Review focus

- *Lemma P:* every factor and region pairing is correct, including the Ω^△ sign: U^△ odd × 𝒱^△ odd. The (4.12) transcription
  correction is accurate (rendered PDF). The symmetric contour is admissible (add φ̂(−z) = φ̃(z), F3).
- *F0 / fold calculus:* correct. The normalization [[1, 0], [−(Q₁)₂₁, 1]] is right, and the (Q^x₁)₂₁ formula of Rule A (i) is
  re-derived.
- *FJ (b):* z(z²)^{−a} = x^{−α} (principal); the weight is continued from the band; (J2) entries are e^{−cn/|x|}-small.
- *FN:* removable (order |x|^{−1/2}); constant [[1, 0], [−i, 1]]; [3] re-run identical.
- *Fφ:* φ_KV,₊(0) = iπ/2; e^{∓iπn} = 1; the root branch is correct; the ordering is reversed; angle π/2 is allowed.
- *FY:* the identification with RH_px's 𝒦± at p = 1 (weight 2w, θ_x = nπ/x − π) is correct, and so is the size of 𝒦₋ − 𝒦₊.
- *§3 transfer:* complete for the hard edge (Rule A (e)). Lemma W′ applies at α = 0. The Airy disc is handled by folding with
  bounded factors. Long pieces have length ≍ n with uniform Carleson constants.
- *Extraction:* correct, including the invariance under the scalar κ^{σ₃} and the n-scalings.
- *Labels:* as proposed, with F1's reframing. After F1–F3 and F6–F8: F0, FS, FN PROVED; P, FJ, Fφ, FY PROVED-mod-cite; RII₁ᶠ and
  the renamed corollaries PROVED-mod-cite, **REVIEWED**, as a second proof of §3.23. §1.3 HEURISTIC; §1.4 OBSTRUCTION
  (heuristic); OBSTRUCTION-a unchanged in scope; Lemma IR PROVED (not used); GAP-rate₁ open; novelty UNCHECKED.
- *OBSTRUCTION-a scoping:* honest. The δ_n/(πζ) claim is HEURISTIC + NUMERICAL. The L^p claim is explicitly heuristic, with the
  Hunt–Muckenhoupt–Wheeden "only if" recorded as not read.
