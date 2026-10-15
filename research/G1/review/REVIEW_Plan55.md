# Rule R review: Plan 55 (any strip, Theorem AS)

Reviewer: independent second reader (Rule R). Branch `plan-55-strip`, commit a35b579 (`git diff master...HEAD`; master's later
untracking of docs/superpowers, LOG.md and research/program is ignored).
Targets:
- PROOF.md §3.24 (Theorem AS, the 26-row audit table, Rule A, numerics) and the §0 row "AS (Plan 55)";
- the dated notes in §§3.17 and 3.19–3.23, in ROUTE2*.md (6 files) and in THEOREMS.md §§2.7–2.8;
- the CITATIONS.md "(KMVV, angle freedom)" addendum;
- LOG.md;
- papers/paper2 revision 3 (sec_front, sec_2, sec_4–sec_8, sec_back, app_outer);
- checks/check_p55_strip.py/.out.

I also read the unchanged Paper 2 text the audit relies on: Lemmas 5.5, 5.6, 5.9, §5.6, Lemma 5.7, Lemmas 6.1, 6.3, 6.5, the
Frame Proposition, App. A (p > 1 and p < 1), §7.1–7.3, App. B (a priori bound; source app_c.tex), App. C (star lemmas;
app_a.tex) and App. D (app_b.tex).

## Overall verdict: **ACCEPT WITH FIXES** (all fixes LOW/INFO; no mathematical error; no hidden minimum angle found)

| Item | Verdict | Label recommended |
|---|---|---|
| Angles (33)–(34): m = min(1, pϑ/ϑ_w⁰) | **ACCEPT** | PROVED (bookkeeping) |
| Lemma 5.7 + Remark 5.8 (weight only in Z_n, ξ ∈ S_ϑ) | **ACCEPT** | PROVED |
| 26-row audit (PROOF.md §3.24) | **ACCEPT**; every row re-checked against the tex (§2) | — |
| Theorem AS (all p > 0, s > 1, (A_ϑ) for some ϑ > 0) | **ACCEPT WITH FIXES** (F2 label wording, F3 citation) | PROVED-mod-cite, proof of record Paper 2 rev. 3: REVIEWED after fixes |
| Consequences for RII, RII_{<1}, RII_x1 and the rate clauses of B_all, B_{p<1}, B_{p=1}^{all} | **ACCEPT** | PROVED-mod-cite (via Theorem AS): REVIEWED after fixes |
| RII₁, RII₁ᶠ conclusions under (A_ϑ) "via RII_x1" (band-centre and fold proofs not re-examined) | **ACCEPT** (correctly scoped) | as stated |
| Paper 2 rev. 3 edits | **ACCEPT WITH FIXES** (F1, F4, F5) | — |
| Numerics check_p55_strip | **ACCEPT** (wording F1); reproduced | NUMERICAL |
| Novelty | — | UNCHECKED (no Rule L) |

## 1. Checks performed

- **Build.** I built a scratch copy of papers/paper2 with pdflatex, bibtex, pdflatex ×2. Result: 0 errors, 0 undefined
  references, 0 overfull boxes, 68 pp. This agrees with NOTES.md.
- **Stale fixed angles.** I grepped all .tex files for π/3, 7π/16, πp/4, 3πp/8, 3π/16, π/12, πp/8, 2π/3, √3 and ϑ_p. What
  remains:
  - T2(a): KMVV's own 2π/3, which is correct as a quotation; (b) then frees the angle.
  - Defaults in (33), Table 1 and the Fig. 1 caption, all labelled "default".
  - π/12, 11π/12, 5π/12 in Lemmas 5.5(iv) and 5.6, and e^{iπ/12}, e^{iπ/6} in the Airy lemma. These are soft-edge angles,
    independent of ϑ_lip and ϑ_w.
  - e^{−π/4}sin(3π/8) in App. B: distance of Re t from ℤ on the arcs |t| ∈ ℕ + ½, independent of the angles.
  - "for ϑ_lip = π/3 these are the rays of KMVV" in §7.2, which is correct.

  There is no leftover ϑ_p in the tex. NOTES.md and OUTLINE.md still mention it (F4).
- **Order of choices.** The order is: ϑ, then (ϑ_w, ϑ_lip) by (33), then δ₀, ε₀, r_*, then δ₁, then δ, then h₁(δ), then
  h₀, then ε, δ′, then n₀.
  - r_* depends only on the constant C of (47), which is angle-free.
  - δ₁ depends on ϑ_lip. It must keep the first lip piece in ¾ϑ_lip ≤ arg z ≤ 5/4ϑ_lip.
  - h₁ depends on ϑ_lip and ϑ_w, through φ < arg z₁, arctan(2y₁/r_*) < ϑ_w and arcsin(h₀/4c) < ϑ_w.
  - Further "δ small" requirements appear later:
    - Lemma 6.5(b): 2C|z|^{1/2} ≤ πs_p|z|^{−1/p}, which depends on s_p = sin(¾ϑ_lip/p);
    - Lemma 7.3: principal powers multiply when |arg(−z)| ≤ π − ¾ϑ_lip;
    - the removability margin in Lemma 7.4(i).

  Each of these depends only on p, s, ℓ₁ and the angles, never on n, and all are allowed by the Frame Proposition ("δ, ε may
  be taken as small as we wish, but fixed"). Nothing is used before it is fixed, and no smallness depends on n. The
  bookkeeping could be made explicit (F5).
- **Hidden lower bounds (risk a).**
  - Lemma 5.5(iii) needs only ϑ_w/p < π/2.
  - Lemma 5.6 works for any ϑ_lip with (5/4)ϑ_lip < ϑ_w. The first piece is in S₀ ⊂ G₊. Corner rounding happens in the
    open set G₊ minus a closed disc. y₁ = h₀ sin(π/12) is the height of the point 4c + h₀e^{11iπ/12}, a soft-edge quantity
    that does not depend on the angles. The constraint φ < arg z₁ forces h₀ smaller when ϑ_lip is small, but h₀ is chosen
    afterwards.
  - The lips stay in the (¾, 5/4)ϑ_lip sectors inside U(0, 2δ) by the choice of δ₁. Outside U(0, δ) the lip is a compact
    arc in ℂ₊, so |arg z| is bounded below there and (F5) holds.
  - App. B:
    - φ₁ = ½ϑ_lip;
    - |z − X| ≥ sin φ₁·max;
    - poles at |arg s| = πp > ϑ_lip, since ϑ_lip < (4/5)πp/2 for p < 1;
    - the super-small factors sin(ϑ_lip/p) and sin(φ₁/p);
    - lens points with arg ≥ φ₁ are handled by Lemma B.1.

    Every bound is positive for ϑ_lip > 0.
  - Lemma 6.3:
    - (ii)/(iii): the near-zone segment [x, z] lies in Z(η_*) because the sector is convex (ϑ_w < π/2); the off-zone bound
      |x − z| ≥ (x + |z|)/8 is angle-free;
    - (vi)(a): the lips in U(0, δ) lie in Z(¼η_*), since δ ≤ min(¼, c/2) ≤ ¼η_*;
    - the last claim of (vi) is a fixed-n bound and uses |arg z| ≥ ½ϑ_lip.
  - (O5) for p = 1 uses φ = π − ¾ϑ_lip < π in (eq:binet-bound).

  None of these needs a positive minimum angle.
- **Bessel model with rays near the negative axis (risk c).**
  - Central sector: |ph 2ζ^{1/2}| ≤ ½(π − ϑ_lip), a closed subsector of the sector of 10.40.1/10.40.3. I re-fetched DLMF
    10.40 on 2026-10-15: the sector is |ph z| ≤ ½π − δ, and the K sector (10.40.2/10.40.4) is |ph z| ≤ 3π/2 − δ.
  - Thin sectors: ph 2(−ζ)^{1/2} ∈ (−½ϑ_lip, 0). The Hankel expansions are valid there, but the paper and CITATIONS cite
    only 10.40.x (F3).
  - The jumps (6.16)–(6.18) on the moved rays are constants of analytic continuation, so they do not depend on the ray
    position.
  - The App. C star constants are ~1/sin(ϑ_lip/2). The localisation constant in (84) is ~1/sin(ϑ_lip/2)². Both are finite
    for fixed ϑ_lip.
  - The matching on ∂U(0, δ) uses |ζ| ≥ n²δ/C → ∞ with fixed rays. Uniformity as ϑ_lip → 0 is not needed and not claimed.
- **Seams, p < 1 (risk d).**
  - Z_n ⊂ S_in, because ϑ_w < πp/2.
  - dist(z, seams) ≥ sin(ϑ_seam − ϑ_w)|z| for |arg z| < ϑ_w. The far seam is at angle < π, and an angle > π/2 gives
    distance |z|.
  - Lemma A.3 is stated for any τ₀ ∈ (0, 1).
  - (O5): ¾ϑ_lip/p ≤ |arg t| < π/2.
  - D, B_in, χ are Gamma/elementary functions, not the weight. So the use of D in S_in ∖ Z_n is harmless, which is the
    point of Lemma 5.7.
- **Binet cut, p > 1, and reflection, p = 1 (risk e).**
  - The B bounds need |arg z| < π/2 on Z_n; a smaller ϑ_w only helps.
  - (O3) uses |arg t| ≤ ϑ_w/p.
  - (O5) uses min(sin(¾ϑ_lip/p), sin(π/p)) > 0.
  - Lemma 6.1 needs |arg t| < ϑ_w < π/2.

  The cut and the reflection themselves do not depend on the lens.
- **Airy edge (risk f).** U(4c, 4ε) ⊂ Z_n follows from ε < c sin ϑ_w. The construction uses |arg f_r − arg(z − 4c)| ≤ π/12,
  the vertical segments and Lemma 6.6; none of these involves ϑ_lip. **Confirmed independent.**
- **Weight domain.**
  - Every evaluation of w, W, r_n, W₀ or ω is in Z_n: the lens and saturated regions by convexity, the lips, the top segment,
    and the sectors {|arg z| ≤ 5/4ϑ_lip} ∩ U(0, δ). This covers App. B's 𝒢 ⊂ {|arg s| < ϑ_lip}, (F5) and Lemma 6.3(vi)(b)/(c).
  - D_W is a band integral and needs only real x.
  - The path bound of Lemma 5.9(iii) runs in |Im ξ| ≤ |arg z|/p < ϑ_w/p ≤ ϑ.

  **Correct.**
- **Hypotheses.**
  - (H_an₁) ⇒ (A_ϑ) for ϑ < π, after shrinking c₀.
  - RedA/Lemma 4.1(iii): Λ_ℓ is entire, and (ii) holds uniformly on every strip, so (A_ϑ) holds for every ϑ.
  - §1 example: 1 − q cos 2ξ = 0 exactly at ξ = πm ± 0.3i. The case sin x = 0, cos x = +1 is the only one possible. On
    |Im ξ| < 0.3, Re(1 − q cos 2ξ) ≥ 1 − q cosh 2y > 0, so the principal log is analytic. √(ξ+1) and (ξ+2)^{−1/2} need
    c₀ < 1. The derivative is O(ξ^{−1/2}) on closed substrips. So (A_ϑ) holds iff ϑ < 0.3. **Correct.**
  - Other examples: (log(e^ξ + e))^β is analytic on |Im ξ| < π, since log(e^ξ + e) ∉ (−∞, 0] there. **Correct.**
- **Numerics.**
  - Full run, from the repo's .out: the singularity check, all 25 n for s = 2 and 3, the maximum spread 1.9·10⁻⁹ and every
    quoted interval match.
  - Spot re-run (K = 10⁵, ld RKPW): values at n = 50, 400, 951 and 3200 for s = 2 and 3 agree with the .out to all printed
    digits.
  - Independent cross-check with **Lanczos** (double, same measure): s = 2 gives n = 50: (−0.0293, −0.9993); n = 200:
    (−0.5322, −0.9850); n = 400: (−0.6031, −0.9971). These are identical to RKPW.
  - Pure-power columns and the s = 3 shift by ≈ ½ match the .out.
- **Labelling and scope.** The ROUTE2*.md notes say "this file is unchanged and proves its results as stated". §3.24 Scope
  says the band-centre and fold proofs were not re-examined. THEOREMS rows say "Rule R pending". This is consistent. See F2
  for the label column.

## 2. Audit table, row by row

All 26 rows match the tex.
- "§5.1" and "imtheta": the wording says "ϑ_w < π/2 ≤ πp/2 or < πp/2", which is correct for both p ≥ 1 and p < 1.
- "Lemma 5.6" and "§5.6": the parenthetical "possible for any ϑ_w > 0 by taking h₀ small" is right. Small additions:
  - the constraint φ < arg z₁ also depends on ϑ_lip (through arg z₁ ≥ ¾ϑ_lip);
  - with h₀ ≤ ½δ tan ϑ_w and δ ≤ c/2, arcsin(h₀/4c) < ϑ_w holds automatically whenever cos ϑ_w > 1/16.

  INFO only.
- "Lemma 6.5": "δ after ϑ_lip" is correct.
- "§7.2": correct in substance; for the citation see F3.
- "App. B/C/D": correct. App. C labels refer to the printed letters: App. B is app_c.tex, App. C is app_a.tex, App. D is
  app_b.tex. The table uses printed letters consistently.
- No row is missing that matters. Rows not listed are angle-free: Lemma 7.4 (comparison parametrix), Lemma 6.3(vi)(b)/(c),
  and §8. They are covered by the "Frame Proposition" and "§4…§8" rows.

## 3. Findings

**F1 (LOW, numerics wording; PROOF.md §3.24 NUMERICAL, LOG.md, Paper 2 §9 sec_back.tex).**

*Issue.* The claim "|·| ≤ 0.603 (resp. 1.101) on both 50 ≤ n ≤ 400 and 400 ≤ n ≤ 3200 / same maximum modulus on both
halves" is vacuous: both windows contain n = 400, and the maximum is attained exactly there (s = 2: −0.6031; s = 3:
−1.1014). The range also covers only log(3200/50)/π ≈ 1.3 periods of the log-periodic factor (period π in log n).

*Fix.* Use disjoint windows:

| s | max \|nB\|, 50 ≤ n < 400 | max \|nB\|, 400 < n ≤ 3200 |
|---|---|---|
| 2 | 0.5983 (n = 336) | 0.5893 (n = 476) |
| 3 | 1.0966 | 1.0882 |

Alternatively, drop the "same maximum" sentence and say that the deviations stay bounded over ~1.3 oscillation periods,
consistent with the theorem, which is weak evidence of no growth. The conclusion "bounded, as predicted" is unaffected.

**F2 (LOW, labelling; PROOF.md §0 row "AS (Plan 55)", §3.24 heading, THEOREMS.md §2.8 row).**

*Issue.* The label "PROVED-mod-cite (inherits RII / RII_{<1} / RII_x1 citations)" reads as if the proof were the ROUTE2
proofs plus a remark. The proof of record is in fact Paper 2 rev. 3's consolidated x-frame engine (§§5–7, App. A–D), with
the §3.24 audit. Paper 2 has had two independent referee reads (REFEREE_REPORT.md, REFEREE2_REPORT.md: "minor revision")
but no repo Rule R of the engine as a whole. This review read the parts that the angle change touches.

*Fix.* In the label column write: "PROVED-mod-cite; proof of record papers/paper2 rev. 3 (§§5–7, App. A–D) with the §3.24
audit; ROUTE2*.md do not prove AS as written; same external citations". The Scope paragraph already says this; the label
column should say it too.

**F3 (LOW, citation gate; Paper 2 sec_7.tex l. 90–93, CITATIONS.md "(DLMF-10.40, Paper 2)", §3.24 audit row "§7.2").**

*Issue.* The thin-sector formulas (6.24)–(6.25) involve Hankel functions H^{(1,2)}_α(2(−ζ)^{1/2}). Their large-argument
expansions are DLMF 10.17.5–10.17.6. These have sectors −π + δ ≤ ph z ≤ 2π − δ and −2π + δ ≤ ph z ≤ π − δ (reviewer's
recollection; not re-fetched). §10.40 covers only I_ν, K_ν (10.40.1–10.40.5), which I re-fetched on 2026-10-15. The paper
says "(10.40.1)–(10.40.5)" for "the Bessel and Hankel functions", and CITATIONS quotes only 10.40.x and 10.17.1. The
mathematics is fine: here ph ∈ (−½ϑ_lip, 0), deep inside both sectors. Alternatively, 10.27.8 (H^{(1)}_ν(z) =
(2/πi)e^{−νπi/2}K_ν(ze^{−πi/2})) together with 10.40.2 gives the same result with ph(ze^{−πi/2}) ∈ (−π/2 − ϑ_lip/2, −π/2).
This gap predates Plan 55, but Plan 55's audit relies on it explicitly.

*Fix.* Quote 10.17.5–10.17.6, or 10.27.8, in CITATIONS (DLMF-10.40) after reading them, and cite them in sec_7 l. 92 and
T4.

**F4 (INFO, stale docs; papers/paper2/NOTES.md l. 39, 154, 236; OUTLINE.md l. 143–148, 172, 240, 345, 375, 625, 659,
662, 703).**

*Issue.* These still say (A_{ϑ_p}) / eq:thetap. OUTLINE is "the binding contract", and NOTES records departures; the
Revision 3 section records this one only globally.

*Fix.* Add one line under OUTLINE or NOTES §1 ("ϑ_p superseded by (A_ϑ), some ϑ > 0; rev. 3"), and update the NOTES §1
claim→source row for def:A. Copy check_p55_strip.py into papers/paper2/checks; this is already a TODO.

**F5 (INFO, Paper 2 §5.6 / Remark 5.8; readability of the order of choices).**

*Issue.* §5.6 says δ, h₀, ε are fixed "once and for all", but later lemmas add further "δ small" conditions (Lemma 6.5(b),
Lemma 7.3, Lemma 7.4(i)). Some of these now depend on ϑ_lip (s_p, π − ¾ϑ_lip). This is correct, because the Frame
Proposition allows shrinking and none of them depends on n, but the reader has to assemble it.

*Fix.* Add one sentence to Remark 5.8 or §5.6: "δ ≤ δ₁ is also taken so small that Lemmas 6.5(b), 7.3 and 7.4(i) hold;
these depend only on p, s, ℓ₁, ϑ_w, ϑ_lip; h₀, ε are then chosen, and n₀ last."

**F6 (INFO/nit, Paper 2 abstract).**

*Issue.* "a sector |arg t| ≤ ϑ, of any opening ϑ > 0": ϑ is the half-opening.

*Fix.* Write "on some sector |arg t| ≤ ϑ, ϑ > 0" (or "half-angle"). The §1 sentence "The opening ϑ may be arbitrarily small"
has the same nit.

**F7 (INFO, numerics Rule N).**

*Issue.* For s = 3 the five-run spread is exactly 0 at n ≤ 168. This shows only that the tail beyond K = 10⁵ is invisible at
these n; it does not test the long-double recurrence.

*Fix.* None needed. The Lanczos cross-check above (identical digits at n = 50, 200, 400) addresses this; optionally mention
it in the .out header.

## 4. Readability (Paper 2)

- **Remark 5.8** reads well. It says where ϑ enters (ϑ_w ≤ pϑ), why ϑ_lip can shrink (T2(b)), lists the lower-bound uses and
  the three upper bounds, and closes with the default strips. Suggestions:
  - add F5's sentence;
  - optionally mention that ϑ_lip < πp (App. B poles) and ϑ_w < πp ((eq:imtheta)) are implied by (34).
- **§1 "In words" paragraph and example** are clear. The PDF line-breaking near the √ and (ξ+2)^{−1/2} formulas is ugly in
  pdftotext but fine in the rendered PDF.
- **§9 "A factor analytic only in a thin strip"** is clear apart from F1.
- **Table 1** is clear. The super-small row as a multicolumn with the defaults is good.

## 5. Recommended labels after fixes

- Theorem AS: **PROVED-mod-cite** (WLXZ v1, KMVV §6 incl. angle freedom, C–D Thm 4.4 + 4.7/4.9 arguments, DLMF incl.
  10.17.5–6 or 10.27.8 after F3, G2 μ*, B*(i)–(ii)); proof of record Paper 2 rev. 3 plus the §3.24 audit. **Rule R ACCEPT
  WITH FIXES (review/REVIEW_Plan55.md), fixes applied: REVIEWED.**
- The weakened forms of RII, RII_{<1}, RII_x1 and the rate clauses of B_{p>1}, B_all, RII⁺_{<1}, B_{p<1}, B_{p=1}^{x}, GAP-int,
  B_{p=1}^{all}: same label, via Theorem AS.
- RII₁, RII₁ᶠ under (A_ϑ): the conclusion holds via RII_x1 (same label). Their own proofs are unchanged and keep (H_an₁).
- Numerics: NUMERICAL. Novelty: UNCHECKED.
