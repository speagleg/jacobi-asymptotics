# Rule R review — Plan 47 (removing citation (P); G2 Lemma EP)

Reviewer: independent second reader (Rule R), 2026-10-14. Branch `plan-47-noP`, commit 28c6339, diff `master...HEAD`.
Read: AGENTS.md, VERIFICATION_POLICY.md, docs/superpowers/plans/2026-10-14-plan-47-noP.md, the full diff, G2 PROOF.md
(§§0–3), G2 CITATIONS.md, `git show master:research/G2/PROOF.md` (B*(iii)), papers/paper1/main.tex §3.2–3.3
(Lemma 3.3, Remark 3.4, proof of Thm 1.3(iii)), papers/paper1/REVIEW_Paper1.md, G1 PROOF.md §§0–2, 3.1, 3.7, G3′ PROOF.md
§0 and Lemma Sat, RH_zeta.md E1, item 11 PROOF.md §7 headers (H2–H4 labels), THEOREMS.md, README.md, lean/README.md,
G2 LOG.md, and a repo-wide grep for "(P)".

## Verdict: **ACCEPT WITH FIXES**

Lemma EP is correct, and so is its port from Paper 1 Lemma 3.3. The new B*(iii) optimality proof checks every
hypothesis of Lemma EP and needs nothing from (P) (Lemma 2.1 or §1). The relabel list is complete and correct: (P) was
the only external citation of each relabelled result, and no label was upgraded past what removing (P) allows. The
G3′, Lean and RH_ζ labels are rightly left unchanged. The numerics reproduce exactly. All findings are minor
(wording, a script comment, stale docstrings, local notes). None affects a label. Once F1–F4 are applied, the Plan 47
labels can drop "Rule R pending (Plan 47)" and add REVIEWED (see "Recommended labels").

## Checks performed

### 1. Lemma EP (G2 PROOF.md §1): re-derived

- **Port fidelity.** Line by line, the statement and proof match papers/paper1/main.tex `lem:positivity` (ll. 421–476).
  The only additions are the sign-convention sentence, the Source and Rule A paragraphs, the explicit
  Re(ν̂ conj ν̂) = |ν̂|² and e^{−ξ}ν(ℝ)² = 0 in Step 3, and "(G_t is even)" in Step 4. These are all correct. The Paper 1
  referee's fixes F2 (2/A, limits along sequences, k₀ remark) are already in the text.
- **(a)** Integrating by parts: |∫_A^B cos t/t| ≤ 1/A + 1/B + (1/A − 1/B) = 2/A. ✓
- **(b)** ∫(1 − cos t)/t ∈ [0, (B² − A²)/4] ⊂ [0, ¼]. ✓
- **(c)** ∫_ε^1 e^{−ξ}/ξ = log(1/ε) − ∫_ε^1 (1 − e^{−ξ})/ξ, and the subtracted part lies in [0, 1]. Also
  ∫_1^R e^{−ξ}/ξ ≤ e^{−1}. So θ′ ∈ [−1, 0.37], and |θ′| ≤ 2 holds with room. ✓
- **The three cases cover a ≠ 0.** ε|a| < 1 splits into R|a| ≤ 1 and R|a| > 1; the remaining case is ε|a| ≥ 1.
  - Case 1: K = −log|a| − θ + O(2) − θ′.
  - Case 2: K = log R − θ − θ′ with 0 < log R ≤ log(1/|a|) = |log|a||.
  - Case 3: K = O(2) − log(1/ε) − θ′ with log(1/ε) ≤ log|a|.
  - Every O(1) is ≤ 2 + ¼ + 2 < 6, so (EP-K) holds. ✓
- **Step 2.** K(a) − K(1) = ∫_{ε|a|}^{ε} + ∫_R^{R|a|} (orientation checked). The first term tends to log(1/|a|) by (b).
  The second is ≤ 2/min(R, R|a|) → 0 by (a). k₀ converges (the integrand is bounded at 0, and ∫^∞ cos ξ/ξ converges).
  Also k₀ = Re Frullani = log|1/i| = 0, which is not needed. ✓
- **Step 3.**
  - (EP-int) makes the diagonal |ν|⊗|ν|-null.
  - Dominated convergence with dominating function |log|x − y|| + 6, writing dν = h d|ν| with |h| = 1, is legitimate.
  - The Fubini step on [ε, R] × ℝ² uses an integrand bounded by 2/ε against a finite measure. ✓
  - Monotone convergence holds on the right because the domains increase and the integrand is ≥ 0. ✓
- **Sign and normalisation.** −log|a| = ∫_0^∞(cos(aξ) − e^{−ξ})dξ/ξ (Frullani with k₀ = 0) gives
  −∬log dνdν = ∫_0^∞|ν̂|²/ξ for ν̂(ξ) = ∫e^{iξx}dν. This agrees with the numerics (§4). The G2 form "∬log dνdν ≤ 0" is
  the correct sign for I = +∬log. ✓
- **Step 4 (equality).**
  - ∫|ν̂|²/ξ = 0 gives ν̂ = 0 a.e. on (0, ∞), hence everywhere by continuity (dominated convergence).
  - ν̂(−ξ) = conj ν̂(ξ) and ν̂(0) = 0.
  - The Gaussian inversion G_t(x) = (1/2π)∫e^{−tξ²/2}e^{−iξx}dξ has the right sign for this ν̂. So (G_t*ν)(x) =
    (1/2π)∫e^{−tξ²/2}e^{−iξx}ν̂(ξ)dξ = 0.
  - Then ∫ψdν = lim∫(G_t*ψ)dν = lim∫ψ(G_t*ν)dx = 0 for bounded continuous ψ, which determines a finite signed Borel
    measure. ✓
- **Rule A.** The ω_8 counterexample is right: I(ω_8) = log(8/4) = log 2 by B0, so −I = −log 2 < 0. The δ_0 − δ_1
  example is worded inaccurately (F1).

### 2. B*(iii) optimality (new text vs master)

- **The measures.** μ^x = g_*μ ≤ σ and μ* ≤ σ (B*(i)) are probability measures on (0, ∞) ⊂ ℝ, so ν = μ^x − μ* is a
  finite signed Borel measure on ℝ (extended by 0) with ν(ℝ) = 0. ✓
- **Log moment.** ∫log(1+x)dα ≤ log 2 + ∫_1^∞log(1+x)σ(dx) < ∞ for α ∈ {μ^x, μ*}. Also
  log⁺|x − y| ≤ log((1+x)(1+y)), since |x − y| ≤ max(x, y). ✓
- **μ^x self-energy.** ∬log⁺ < ∞ by the log moment. ∬log⁻ = ∬log⁺ − I(μ) < ∞ because I(μ) > −∞. ✓
- **μ* self-energy.** Tonelli over the mixture gives ∫∫ C(1 + |log s| + |log t|) ds dt < ∞. This uses the **Value**
  bound, which G2 states without derivation; the derivation is one line (F2). ✓ (modulo F2)
- **Mutual energy.**
  - For each x > 0, U*(x) is finite: B*(ii)'s Fubini bound, and U* ≥ log c + p > −∞.
  - So ∫|log|x − y||dμ*(y) = 2∫log⁺|x − y|dμ*(y) − U*(x) is a legitimate identity.
  - It is bounded by 2log(1+x) + 2∫log(1+y)dμ* − (log c + p), which is μ^x-integrable. Tonelli then gives the double
    integral. ✓
  - U* ∈ L¹(μ^x) ∩ L¹(μ*) follows from |U*| ≤ ∫|log|·−y||dμ*(y). ✓
- **(EP-int).** |ν| ≤ μ^x + μ*, so the integral is bounded by the four finite cross-integrals. ✓
- **Expansion.** All terms are absolutely convergent, so ∬log d(μ* + ν)d(μ* + ν) = I(μ*) + 2∫U*dν + ∬log dνdν. ✓
- **Middle term.** ∫U*dν = ∫(U* − log c − p)dν because ν has mass 0. The integrand is 0 on (0, 4c] and ≥ 0 on (4c, ∞),
  where ν = μ^x − σ ≤ 0. So the middle term is ≤ 0. ✓
- **Equality.** Both terms are ≤ 0, so I(μ) = κ_p forces ∬log dνdν = 0, hence ν = 0 (Lemma EP), hence μ = μ*_u (g is
  a bijection). ✓
- **"Each of the three energies converges directly": correct.** None of the three bullets uses (P).
- **The old second use of (P) is replaced.** On master, (P) §1 (after (1.13)) gave finiteness of the mutual energy, and
  hence the legitimacy of ∫U*dμ^x and of the bilinear expansion. That role is now played by the third bullet, through
  B*(ii). ✓
- **Agreement with Paper 1.** The new text matches Paper 1's proof of Thm 1.3(iii) (main.tex ll. 545–568) step for step.
- **(P) remark.** The master text is quoted verbatim (checked against `git show master:`). ✓

### 3. Relabel list and dependency chains

| Result | External citations other than (P) in the proof? | Verdict |
|---|---|---|
| G2 B* | None. B0 is self-proved; (i), (ii) and Value are computations. | PROVED ✓ |
| H_all | None. Internal inputs: A-U, A-L, B*, and item 11 H2/H3/H4 (PROVED in item 11 §7; internal, as in the pre-Plan-47 label). | PROVED ✓ |
| HZ | None. (HZ) Haynes–Zudilin is context only ("Nothing is assumed from it"). The reindexing to weights k^{−(2a+b)} checks out. | PROVED ✓ |
| Cor. H-input | H_all; Lean `heineD_eq_det`, `heineK_bdd_of_summable` (sorry-free). | PROVED ✓; Lean labels rightly unchanged |
| G1-T, G1-L | Only H_all (b_j form via H2), Lemma K, and elementary Landau arguments. | PROVED ✓ |
| WC | G2 A1, A-U, A-L, B*(iii) uniqueness, scaling. Prokhorov/Portmanteau are textbook, as before. | PROVED ✓ |
| CL | WC; Sat_p (G3′ Lemma Sat: Christoffel + Lagrange, elementary; Sat_p already PROVED); A3; B*(i). | PROVED ✓ |
| A4′ | A2, A3, CL. | PROVED ✓ |
| TC | G2 A-U, A-L, B*(iii). | PROVED ✓ |
| T3-avg | Keeps RH_px, RH₁(r), RH_plt1b (via pure-power laws); (P) entered only via TC. | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) ✓ |
| G3′ §0 notes (19 rows) | Annotation only; no G3′ result depended on (P) (all instances (2, s ≥ 2), item 11 route). | labels unchanged ✓ |
| Lean `theoremHL` | Not formalized on the G2 side. | PROVED-mod-input unchanged ✓ |

- **No label was upgraded beyond removing (P).** Results already REVIEWED keep REVIEWED and say "proof unchanged".
- **Missed dependencies.** A repo-wide grep for "(P)" and "mod-cite (P" finds no live dependence outside the annotated
  history. The remaining mentions are of four kinds:
  - history blocks marked pre-Plan-47 (THEOREMS §§1, 3.2, 3.3 and §5 Plan 37 items; G2 §3 Cor. H-input paragraph;
    G1 §3.1/§3.7 headers; G3′ §0 paragraph; review files; G1 LOG);
  - the retained (P) remark and CITATIONS entry;
  - a different "(P)" (weyl.py and the design spec: item 11 note (P); check_trunc.py: a variable name);
  - three stale items: the Lean docstrings (F3), RH_zeta.md E1(iv) (F4) and novelty_G2.md l. 300 (info).
- **Other results that use H_all, CL or TC** (remarks in Thm R, RW, Ra; the G1 §4 stop report; A4; RH_p) never carried
  (P) in their labels, or carried it only through B*(i)–(ii). Nothing needs relabelling.
- **RH_ζ unchanged: right.**
  - Its label is PROVED-mod-cite for independent reasons (WLXZ, KMVV, C–D, DLMF), so removing (P) could not change it.
  - E1(iv) is declared unused.
  - For the record, the reviewer believes Lemma EP applies to E1(iv) as well. All arcsine components there have edges
    β(τ) ∈ [β, x_e], bounded away from 0, and the support is compact, so (EP-int) is immediate. U^μ ≥ ℓ/2 gives the
    mutual bound, and the middle-term sign argument is the same. This is not needed and was not written up.

### 4. Numerics

- `check_positivity.py` was re-run with the jacobi-asymptotics `.venv` python (1.1 s). Its output is byte-identical to
  `check_positivity.out` (PASS).
- **[1] ω_1 − ω_4.**
  - LHS: −[log(1/4) − 2·0 + 0] = log 4, by B0. ✓
  - ν̂ of ω_b is e^{iξb/2}J₀(ξb/2). ✓
  - Fourier side at cut 4000: 1.386175, a gap of −1.19·10⁻⁴.
  - The reviewer extended the run to cut 16000 (1200 geometric panels). The gap is −2.98·10⁻⁵, scaling as 1/cut.
- **[2] U[0,1] − U[0,2].** Gap −4.5·10⁻⁸. ✓
- **The [1] tail constant.** The gap matches 3/(2π·cut) to four digits: 1.1937·10⁻⁴ and 2.9842·10⁻⁵. It does not match
  the script comment's (5/(4π))/cut. The cross term 2Re(ν̂_1 conj ν̂_4) does not average to zero, so the comment is
  wrong (F5).
- The NUMERICAL label is correct. The check is evidence only.

### 5. Docs and history

- THEOREMS.md, README, lean/README, G1/G2/G3′ PROOF.md, CITATIONS.md, LOG.md, RESEARCH_PROGRAM.md and
  outline_A_nodes.md agree with each other. Every changed label says "Rule R pending (Plan 47)".
- Pre-Plan-47 sentences are kept with dated notes. Nothing was deleted except label cells, and each of those keeps
  "was …".
- The plan's Review focus items are all addressed above.
- Minor wording issues: F6, F7.

## Findings

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| F1 | Minor | G2 PROOF.md Lemma EP, *Rule A* bullet 1; G2 LOG.md "Rule A (Lemma EP)" | "dropping (EP-int) loses the statement (ν = δ_0 − δ_1 has +∞ diagonal energy, so the left side is undefined)" is inaccurate. The diagonal carries Σν({x})² ≥ 0 against log 0 = −∞, so −∬log dνdν = +∞. The Fourier side ∫(2 − 2cos ξ)/ξ dξ is also +∞, so the identity holds in [0, ∞] and the example shows no failure. | Reword: "(EP-int) is what makes every integral absolutely convergent (dominated convergence in Step 3). Without it the left side can be +∞ (ν = δ_0 − δ_1: both sides are +∞) or of the form ∞ − ∞. The example shows (EP-int) cannot be dropped from the finite-valued statement; it is not a counterexample to positivity." |
| F2 | Minor | G2 PROOF.md B*(iii) **Value** (and B*(ii)) | The bound ∬\|log\|x−y\|\|dω_{β_s}dω_{β_t} ≤ C(1 + \|log s\| + \|log t\|) is asserted, not derived. It is now load-bearing for (EP-int), as the μ* self-energy bullet. Paper 1 derives it (eq. `absbound`, main.tex ll. 412–417). | Add one line: for s ≤ t, by \|t\| = 2t⁺ − t and B0, ∬\|log\| dω_{β_s}dω_{β_t} = 2∬log⁺ − log(β_s/4) ≤ 2log(1 + β_s + β_t) + \|log(β_s/4)\|, which is ≤ C(1 + \|log s\| + \|log t\|) since β_s = 4c s^{−p}. Similarly ∫\|log\|x−y\|\|dω_β(y) ≤ 2log(1+x+β) − log(β/4) in B*(ii). |
| F3 | Minor | lean/JacobiAsym/Inputs.lean l. 23; lean/JacobiAsym/TheoremHL.lean l. 13 | The docstrings still say G2 H-input is "mod-cite (P)". This is disclosed in G2 LOG.md, but they are now the only live, unannotated statements of the old label. | In a follow-up `lean:` commit, change the docstrings to "PROVED on paper since Plan 47 (was mod-cite (P))" and re-run `lean/check.sh` (must print AUDIT OK). Or keep them and add the reason to lean/README. |
| F4 | Minor | research/G1/RH/zeta/RH_zeta.md l. 44–45 (E1(iv)) | "using only (i), (ii) and the positivity lemma (P)" has no local dated note. A reader of RH_zeta.md alone will not see that G2 no longer uses (P). | Add a dated note: "(Plan 47, 2026-10-14: G2 now uses Lemma EP in place of (P). E1(iv) is unchanged and unused; whether Lemma EP's (EP-int) holds here has not been written up.)". Optionally, write up the reviewer's sketch (§3 above). |
| F5 | Minor (numerics comment) | research/G2/checks/check_positivity.py, comment in `fourier_side` | The comment says the [1] tail is ~(5/(4π))/cut. The correct asymptotic is (3/(2π))/cut: \|ν̂\|² averages 5/(2πξ) − 1/(πξ), because the cross term has a non-oscillating part. This gives 1.19·10⁻⁴ at cut 4000, exactly the observed gap (the reviewer confirmed this at cut 16000). | Correct the comment to 3/(2π·cut). Optionally, add the tail estimate to the printed Fourier side and compare the corrected gap (O(10⁻⁷)). Regenerate `.out`. |
| F6 | Info | THEOREMS.md header, ll. 3–7 | The Plan 37 sentence "Nothing has been upgraded; the only label change is …" is now superseded by the Plan 47 note directly below it. | Prefix it with "(Plan 37:)" or add "— see the Plan 47 note below for the label upgrades of 2026-10-14". |
| F7 | Info | THEOREMS.md §3.2, Plan 47 line | Listing G1-T, G1-L, WC, CL, A4′, TC (and H_all) as "fully self-contained" is accurate only in the repo's sense: no external *citation*, but internal item 11 lemmas (H2–H4, H7) and textbook Prokhorov/Portmanteau (WC). This matches how A-U was already listed. | Optionally append "(internal item 11 inputs, as for A-U)". |
| F8 | Info | research/program/novelty_G2.md l. 300 | "Saff–Totik (already in G2 via (P))" is stale. It is a literature pointer, recorded as history in LOG. | Optional dated note. |

## Recommended labels (after F1–F4; F5–F8 optional)

- **G2 Lemma EP:** PROVED + REVIEWED (Plan 47). Novelty: not claimed (Fourier proof of a classical fact; the statement
  is contained in (P) / Saff–Totik I.1.8 for the positivity part).
- **G2 B\*:** PROVED + REVIEWED (B*(iii) re-reviewed here; (i), (ii) and Value REVIEWED 2026-10-13).
- **G2 H_all, HZ, Cor. H-input:** PROVED + REVIEWED.
- **G1 G1-T, G1-L:** PROVED + REVIEWED.
- **G1 WC, CL, A4′, TC:** PROVED + REVIEWED (proofs unchanged; relabel reviewed here).
- **G1 T3-avg:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) + REVIEWED (still SUPERSEDED by T3-all).
- **G3′ (all rows), Lean `theoremHL` / `smoothZeta_*`:** unchanged (mod-input Theorem H / PROVED-mod-input
  `TheoremHPure`). The annotation "(PROVED since Plan 47; was mod-cite (P))" is correct.
- **RH_ζ:** unchanged (PROVED-mod-cite (WLXZ, KMVV, C–D, DLMF; G2 optimality for unused E1(iv))) + REVIEWED.
- **(P) in CITATIONS.md:** status "not used (alternative route)". Correct.
