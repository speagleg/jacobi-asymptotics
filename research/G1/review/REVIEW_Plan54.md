# Rule R review — Plan 54 (GAP-int: Route II in the unsymmetrized x-frame at p = 1)

Reviewer: independent second reader (Rule R). Branch `plan-54-r2xframe`, commits 55296c3, a713e97 (`git diff master...HEAD`).
Targets: `research/G1/RH/route2/ROUTE2_xframe1.md`; PROOF.md §3.23 and the §0 row "RII_x1 / GAP-int / B_{p=1}^{all}"; LOG.md
entry; CITATIONS.md "(DLMF-5.5/5.11, Plan 54)"; the note in ROUTE2_p1.md §7; checks `route2/checks/check_x1_{frame,e2e,coeff}`.
Templates read: RH_px.md (+ REVIEW_RHpx.md), ROUTE2.md (+ REVIEW_Plan48.md incl. UR′(b′)), ROUTE2_p1.md, PROOF.md §§3.19–3.21,
G2 PROOF.md (B* for every p > 0), AGENTS.md.

## Overall verdict: **ACCEPT WITH FIXES** (all fixes LOW/INFO; no mathematical error found in the main line)

| Item | Verdict | Label recommended |
|---|---|---|
| Lemma X1 (reflection, D = exp μ(−N/z), B ≡ 1) | **ACCEPT** | PROVED-mod-cite (DLMF 5.5.1, 5.5.3, 5.11.1) — REVIEWED after fixes |
| Lemma X2 (p = 1 failure of RH_px's quotient hard edge) | **ACCEPT** (wording F2) | PROVED (computation) + OBSTRUCTION scoped to RH_px §4.1 *as written* |
| §2 transfer table | **ACCEPT WITH FIXES** (F1) | PROVED (bookkeeping) |
| Lemma LW1-x1 | **ACCEPT** | PROVED (as ROUTE2 LW1′, ν = ½) |
| Theorem RII_x1 (p = 1, 1 < r < 3, incl. r = 2) | **ACCEPT** | PROVED-mod-cite — REVIEWED after fixes |
| Corollaries B_{p=1}^{x}, GAP-int (closed), B_{p=1}^{all}; "every p > 0, s > 1" | **ACCEPT** (cross-refs F6) | PROVED-mod-cite — REVIEWED after fixes |
| §6 Route (C) | ACCEPT (scoped; interpolation item is heuristic and labelled so) | OBSTRUCTION/HEURISTIC, not needed |
| Numerics | **ACCEPT**; all three checks reproduced bit-for-bit (F3–F5, F7 wording) | NUMERICAL |
| Novelty | — | UNCHECKED (no Rule L) |

## 1. Rule C: citation check (dlmf.nist.gov re-fetched by the reviewer, 2026-10-14)

- 5.5.1 "Γ(z+1) = zΓ(z)" (no condition) — **matches**.
- 5.5.3 "Γ(z)Γ(1−z) = π/sin(πz), z ≠ 0, ±1, …" — **matches**; used at t = N/z ∉ ℝ (z ∈ ℂ±), hypothesis satisfied.
- 5.11.1 "As z→∞ in the sector |ph z| ≤ π−δ, Ln Γ(z) ∼ (z−½)ln z − z + ½ln(2π) + Σ B_{2k}/(2k(2k−1)z^{2k−1})", Ln the general
  logarithm — **matches**. Used for μ(u) in |ph u| ≤ π − δ only. (Wording nit: X1's notation line calls μ's LnΓ a "principal
  branch"; DLMF's LnΓ is the continuous branch real on (0, ∞) — INFO.)

## 2. Verification of the mathematics

**Lemma X1.** Re-derived independently in both half-planes. ℂ₊: ph t ∈ (−π, 0), u = −t, ln u = ln t + iπ; sin(πt)/(1 − e^{−2πit})
= e^{iπt}/(2i); t^{t−½}e^{iπt} = e^{iπ/2}u^{t−½} = i·u^{−u−½}; D = u^{−u−½}e^{u}Γ(1+u)/√(2π) = e^{μ(u)} via 5.5.1. ℂ₋: ln u = ln t − iπ,
sin(πt)/(1 − e^{2πit}) = −e^{−iπt}/(2i), t^{t−½}e^{−iπt} = −i·u^{−u−½}; the signs combine to +1. Correct. Analyticity off [0, ∞),
reality/positivity on (−∞, 0) (u > 0) hence ℓ̂ ≡ 0, B ≡ 1, D ~ (−z/N)^{1/2}/√(2π) at ∞ (μ(u) = −½ln u − ½ln 2π + O(u ln u)),
poles of D at the nodes (Γ(1 + u) at u = −k ⇔ z = N/k) — all correct. The monodromy count: (−z)^{1/2}(2 − z)^{−1/2} has cut [0, 2]
only, so F = DK is analytic at ∞ (Finf = 1/√(2πN) = 0.126157 at N = 10 reproduced).

**Lemma X2.** On (−δ, 0) at p = 1, θ₊ = θ₋ real; (1 − e^{−2iθ})/(1 − e^{2iθ}) = −e^{−2iθ}, |J − 1| = 2|cos θ| — verified. Poles of the
continued h_N ∝ e^{2μ(N/z)} at t = −m (boundary values from both sides) — correct. The scope statement is correct: in RH_px the
jump of D̃B on (−δ, 0) enters only through W̃ = continuation of w₀^{1/2} (Lemmas 4.2(iii), 4.3 (h2)); V itself has no jump on
(−∞, 0) (F = DBK jump-free; e^{−Ngσ₃} jumps by e^{∓2πiN} = 1).

**Transfer table — every row re-audited for hidden p > 1:**
- *G2 μ*, B* at p = 1:* G2 PROOF.md is titled and proved "for every p > 0" (B* REVIEWED, Plan 47 citation-free). c(1) = ½
  (I = π/4, 4c = 2) checked. ψ = x^{−2}I_{x/2}(3/2, ½) ~ Cx^{−1/2}, so the hard edge and f analytic with f′(0) = −4π²C² < 0 (it is
  the square of i·real for every p) — p-free.
- *Lemmas 2.1–2.2* (strictness, signs; ρ = x^{−2}): p-free. Top: U*(x) = log x + o(1) still holds.
- *Lemma 3.5 (normalization):* see **F1** — the stated rate g − log z ≍ z^{−1} is wrong at p = 1, but the argument (κ bounded,
  jump-free, hence analytic at ∞) is unaffected.
- *Lens geometry / D̃ region:* D̃ is used only in Ω_b, Ω^△, U(b, ε) and on the top pieces. Near 0 the lips are KMVV's ζ-rays
  ±2π/3 pulled back by f (f′(0) < 0 ⇒ z-rays ∓π/3); elsewhere thin neighbourhoods of (0, N). So |ph t| = |arg z| ≤ π/3 + π/24
  where D̃ is needed, and |t| ≥ N/2 near the band (Stirling uniform). Correct.
- *(h1) entries on the lips:* |e^{∓2iθ}| = exp(−2πN sin|arg z|/|z|) and Re(iπ/z) = π sin(arg z)/|z| > 0 in ℂ₊ — verified.
- *Ω_∞:* uses D only; |D − 1| = O(1/|u|) needs |ph u| ≤ π − δ, i.e. |arg z| ≥ δ — near the positive axis Ω_∞ is either the top
  segment or |z| > N + δ′ (|u| < 1), where only analyticity/boundedness of D is used. Fine.
- *Airy at b = 2, top (|D| ≤ CN/δ′ from Γ(1 + u) at u = −1), (Y4)_x (𝒦₋ = O(e^{−cN/|s|}), left half-plane node-free):* p-free.
- *Weight-evaluation strip:* evaluations of w/q_N occur at |arg z| ≤ π/3 + π/24 (lips, lens, Ω^△, top, (Y4)_x sectors, LW1 paths).
  Even if RH_px's U → R transformation regions above the band were rectangles (arg z → π/2 at Re z → 0+), the closed strip
  |Im u| ≤ π/2 of (H_an^{x1}) still covers them. So the choice π/2 is safe in either reading. RedA's L₁ (entire) and
  √log(e^u + e) (branch points at Im u = ±π) satisfy it.
- *ROUTE2 §§3–4 (H1′, local form incl. α = 0 log form, LW1′, UR′ incl. (b′), W′, C′, D′, extraction):* re-read; none uses p
  beyond ν, the exponent |z|^{−1/p} in (h1) bounds and the strip. **Q̃** is an explicit construction (N, P̃₀ with W̃ := D_w, Airy,
  small-norm 𝒵̃) — it is *not* the pure-power RH solution and never needs RH_px's quotient hard edge, so Lemma X2 does not enter.
  D_w is a Cauchy integral of band values (t = N/x ∈ (N/2, ∞), μ smooth), analytic off [0, b]; neither D_w nor q_N on the lips
  sees the poles of e^{2μ(N/z)} at z = −N/m (they lie on the negative axis, at |arg z| = π, never evaluated).
- *α_x = 0 (r = 2):* log local form, Lemma W′, UR′(b′) α = 0 case, D′ with log² — reviewed in Plan 48 and p-free. Confirmed.
- *Consistency with p = 1 pure powers:* Ψ₁ ≡ 1 gives nb_n → ½ = c(1), agreeing with RH₁(r); the e2e probe gives
  Nb_N/c = 0.9531, 0.9758, 0.9877 (r = 2) = 1 − (r − 1)/(2N) + O(N^{−2}), and 0.9755 at r = 1.5, N = 10 (1 − 0.025).

**Corollaries.** B_{p=1}^{x} = RedA (every p > 0, entire L₁ ⇒ (H_an^{x1})) + RII_x1. GAP-int: r = 2 is in (1, 3); SH-r (§3.21,
any p > 0, positive σ on [0, ∞) with infinite support, same regular rate) gives r ≥ 3, with x·k^{−r′}Ψδ_{1/k} = k^{−r′−1}Ψδ_{1/k}.
B_{p=1}^{all} with B_{p=1}⁺ (REVIEWED) for non-integers. The "every p > 0, s > 1" statement then follows from §3.20 (p < 1) and
§3.21 (p > 1), both REVIEWED. Correct, and correctly marked pending for the p = 1 integer part.

## 3. Numerics (re-run from the jacobi-asymptotics root)

- `check_x1_frame.py` (14 s): output identical to the committed `.out`.
- `check_x1_coeff.py` (3 min): identical to the committed `.out`.
- `check_x1_e2e.py 1 2 10,20` and `1 1.5 10`: identical to the corresponding blocks of `_p1s2.out`, `_p1s1.5.out`. N·err stable;
  |det V − 1| ≤ 4·10⁻³¹ (a713e97's corrected bound is right).
- **Incident reproduced.** With RH_px's original D̃ formula in the Szegő quadrature (D kept as e^{μ(−N/z)}), p = 1, r = 2:
  D_inf = 0.516(1 − i) instead of 1.264(1 − i), N·err = 13.4 → 26.5 (N = 10 → 20), i.e. O(1) and N-independent error. Diagnosis
  confirmed. Mechanism measured at dps 30: (t − ½)ln t − t − LnΓ(t) is accurate to ~10⁻¹⁵ at t = 10¹⁵, wrong by 2·10⁻¹⁰ at
  10²⁰, by O(1) (bounded) for 10²⁵ ≲ t ≲ 10⁶⁰, and by ~10³⁸ at t ≈ 4·10⁶⁶. mp.quad's smallest tanh-sinh node at dps 30 is
  θ ≈ 2·10⁻³³, i.e. x ≈ 10⁻⁶⁶ and t = Nx^{−1/p}: ≈ N·10⁶⁶ at p = 1 (catastrophic), ≈ N·10³³ at p = 2, N·10⁴⁴ at p = 1.5, N·10²² at p = 3.
- **Side issue: the REVIEWED p > 1 probes.** `px/checks/check_px_e2e.py`, `check_px_bessel.py`, `check_px_phase3a/3b.py` use the
  same formula, so for p > 1 the Szegő quadrature *does* evaluate D̃ in the inaccurate range (O(1) errors at nodes of weight
  ~10⁻³³). The reviewer re-ran with the Plan 54 Stirling fix vs the original: `check_px_e2e` at (p, s) = (2, 3) N = 10, 20;
  (1.5, 3) N = 10; (3, 2.5) N = 10, and `check_px_bessel.py` (p = 2): **every printed digit identical** (bessel output also
  identical to the committed file). phase3a/3b evaluate D̃ at modest t or with weights e^{u} ≤ e^{−80} on the far nodes; not
  affected in any printed digit that a conclusion uses. **No reviewed conclusion depends on the flaw.** (The plt1 probes and
  `check_r2p_lw1.py` already used a Binet series for large t — precedent, see F3.)

## 4. Findings

**F1 (LOW). Location:** ROUTE2_xframe1 §2 table, row "Lemma 3.5" ("g − log z ≍ z^{−1}"). **Issue:** at p = 1, μ* has density
x^{−2} on [2, ∞) (mass beyond y is 1/y), so ∫y dμ* diverges and g(z) − log z = −(log z)/z·(1 + o(1)), not ≍ z^{−1}. Correspondingly
D = e^{μ(−N/z)} contains a u log u term. **Impact:** none — RH_px Lemma 3.5 only uses that κ = F^{−1}e^{N(g − log z)} is bounded
and jump-free in |z| > N + δ′ (both true; the log terms cancel), hence analytic at ∞. **Fix:** replace by "g − log z =
O(|z|^{−1}log|z|) (first moment of μ* diverges at p = 1); κ bounded and jump-free, hence analytic at ∞ — unchanged"; and add this
to §1's list of p-sensitive items (it is the one p-dependence the "grep" list missed).

**F2 (LOW/wording). Location:** Lemma X2 statement and label row; PROOF §3.23 "(OBSTRUCTION, scoped to that construction)".
**Issue:** "the only steps of RH_px that fail at p = 1" lists Lemma 1.1's non-uniformity, which does not *fail* anything (D̃ is
never needed there); and "OBSTRUCTION" should be explicitly an obstruction to RH_px §4.1 *as written* (W̃ = continuation of
w₀^{1/2} with D̃B), not to every quotient/small-norm construction. **Fix:** "the only step whose proof fails is Lemma 3.2(v)
and its uses (4.2(iii), 4.3 (h2)); Lemma 1.1 holds but Stirling is non-uniform near arg z = ±π, which is never needed"; label
"OBSTRUCTION (RH_px §4.1 as written)".

**F3 (LOW). Location:** §2 "Numerical note (Rule N)"; LOG; PROOF §3.23. **Issue:** "t ≳ 10⁶⁰" understates the range — the formula
is already O(1) wrong from t ≈ 10²⁵ (bounded) and becomes catastrophic near 10⁶⁶; and "p > 1 outputs not re-run" can now be
replaced by the reviewer's re-run. **Fix:** record: "Rule R re-ran check_px_e2e (2,3; 1.5,3; 3,2.5) and check_px_bessel with
the fix: outputs identical in every printed digit; no reviewed p > 1 conclusion is affected", and cite the plt1 precedent
(check_plt1_e2e.py already used the Binet series). Optional housekeeping (separate commit, not required): add the same guard to
the px probes.

**F4 (INFO). Location:** check_x1_frame.py [4]. **Issue:** μ is evaluated without the Stirling guard for x down to 10⁻⁴⁰
(t ≲ 2·10⁴²) — O(1) errors at nodes of negligible weight; and μ(N/x) = x/(12N) + … is tiny, so [4] essentially tests the
(b − x) factor (the text says so). Results are reproducible and unaffected at the printed precision. **Fix:** optional: use the
same `mu` as check_x1_e2e.

**F5 (LOW). Location:** §2 "NUMERICAL end-to-end validation of the frame". **Issue:** the probe tests V ≈ N outside the discs
for the *pure power* (validates D, B ≡ 1, K, l, w₀, D_w, N at p = 1). It does not probe the p = 1 hard-edge comparison
parametrix P̃₀ (the analogue of check_px_bessel [B]) nor any non-trivial Ψ in the RH frame. The text does not overclaim, but
"end-to-end validation of the frame" should say "outside the discs". **Fix:** wording; optional P̃₀ matching probe at α_x = 0.

**F6 (LOW). Location:** stale GAP statements not annotated: PROOF.md §0 row "RII₁ / B_{p=1} / CT₁" ("GAP: p = 1, r ∈ {2, 3, …}");
PROOF.md §3.19 "Remaining (GAP)" (≈ line 2756); ROUTE2_p1.md label table (line 28 "GAP-int … GAP (§7)") and §7 lines 521–522
("an unsymmetrized p = 1 hard-edge analysis … is not available in this repo"); ROUTE2.md §6 "WP5 (p = 1 …) is untouched";
THEOREMS.md lines 302, 306, 426–427. **Fix:** add "(Plan 54 note: closed, PROOF §3.23)" annotations when the label becomes
REVIEWED.

**F7 (INFO). Location:** §5 numerics bullets. **Issue:** oscillating Ψ "E = 0.488 … 0.500" — r = 3 gives E up to 0.5006; "spread
≤ 1.3·10⁻⁸" is the nB spread (E spread up to 1.9·10⁻⁸ at r = 2, n = 800). The r = 1.5 row of the e2e table gives one rounded value
for several columns (the three N agree to the shown digits only approximately: 0.0906/0.0912/0.0914). **Fix:** wording.

**F8 (INFO). Location:** X1 notation ("principal branches" for LnΓ). **Fix:** "LnΓ the branch analytic on ℂ ∖ (−∞, 0], real on
(0, ∞) (DLMF's Ln)".

## 5. Answers to the plan's Review focus

- *X1 branch bookkeeping:* correct in both half-planes; analytic across (−∞, 0); poles at the nodes; F_∞ = 1/√(2πN).
- *X2 scope:* the quotient construction is the only consumer of Lemma 3.2(v). No step of ROUTE2 (H1′, LW1′, UR′, C′, D′,
  extraction) continues w₀ across (−δ, 0) or needs uniform Stirling for D̃ near arg z = ±π.
- *Transfer table:* V has no jump on (−∞, 0); (h1) entries O(exp(−cN/|z|)); D̃ only in |arg z| ≤ π/3 + π/24; strip π/2 adequate
  (even for rectangle-shaped transformation regions); (Y4)_x p-free; G2 μ*, B* valid at p = 1. Only F1 needs correcting.
- *α_x = 0:* p-free as claimed.
- *Corollaries:* SH-r applies (any p > 0, same regular rate); combined "every p > 0, s > 1" correct modulo this plan's Rule R.
- *Numerics:* reproduced exactly; incident confirmed and explained; p > 1 outputs need no re-run (verified identical).
- *Labels:* as proposed by the author, with F2's scoping of OBSTRUCTION. After F1–F3, F6 are applied: X1, RII_x1, B_{p=1}^{x},
  GAP-int, B_{p=1}^{all} PROVED-mod-cite, **REVIEWED**; X2 PROVED + OBSTRUCTION (RH_px §4.1 as written); numerics NUMERICAL;
  novelty UNCHECKED.
