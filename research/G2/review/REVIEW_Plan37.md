# REVIEW — Plan 37 (consolidation pass: THEOREMS.md, G2 Corollary H-input, Theorem H discharge, stale-text fixes)

Reviewer: independent second reader (Rule R), 2026-10-14. Scope: `git diff 38bfb3b..HEAD` on branch
plan-37-consolidate (commits 8ac68a6, f9f09df). Sources re-read: AGENTS.md, VERIFICATION_POLICY.md, THEOREMS.md (all),
G2 PROOF.md §§0, 2 (A2), 3; G3′ PROOF.md §§0, 3, 4, 4.1, 5, 5.4 (grep), 7, 8.1 (grep); G1 PROOF.md §0, §4; RH file
headers; rhfree/ status tables; lean/JacobiAsym/{Inputs,Heine,HankelLimit}.lean; math-pursuits item 11 PROOF.md §§7, 7b
(read-only).

## Verdict: ACCEPT WITH FIXES

The new mathematics (Corollary H-input) is correct, the §3.3 discharge table is correct row by row, no label was
upgraded without justification, and no proof was changed. One major presentational defect (F1): the discharge is
attributed only to G2 mod-cite (P), although every G3′ instance was already supplied, citation-free, by item 11's
Theorem H (p = 2). This adds a spurious (P) dependency to G3′'s headline results. The repo's own Inputs.lean docstring
recorded the item 11 route before Plan 37. The fixes are textual.

## Checks done

1. **Corollary H-input vs `TheoremHPure p κ s`** (Inputs.lean: `bdd`, `asymp`; `heineD := ⨆ K, heineK`; `powSeq p k =
   (k+1)^{−p}`; `hnorm p κ D (fun _ => 0) n = (log D n − (−p n² log n + κ n²))/n²`).
   - `bdd`: heineK(x, w, K, n) = Σ_{|S|=n, S⊂[0,K)} Π_S w · Π_{pairs}(x_a − x_b)². Atoms lie in (0, 1], so each
     squared Vandermonde factor is < 1, and Σ_S Π_S w = e_n(w|_K) ≤ (Σ w)^n with Σ_k (k+1)^{−s} < ∞ for s > 1. Correct.
     (It is also already a Lean theorem: `heineK_bdd_of_summable`, HankelLimit.lean, hypotheses w ≥ 0, Summable w,
     |x| ≤ X; see F3.)
   - `heineD_eq_det` hypotheses: `0 ≤ w k` ✓, `Summable (powSeq s)` ✓ (s > 1), `|powSeq p k| ≤ 1` ✓. `hankel x w n` is
     the Fin n × Fin n matrix of Σ' w x^{i+j}, i.e. item 11's det(m_{i+j})_{0≤i,j≤n−1}, which is the D_n of H_all.
   - `asymp`: H_all with f(ξ) = ξ^{−p}: f ∈ C¹[1,∞), ξ^{p+1}f′(ξ) = −p, so C = 1 and ξ^{p+1}|f′| is constant (bounded
     above and below). Weights w_k = k^{−s}: Σw < ∞ (s > 1), w_k ≥ 1·k^{−s}. H_all gives log D_n = −pn² log n +
     (3p/2 + log c(p))n² + o(n²), which is exactly `hnorm → 0` with κ = κ_p. Index shift: Σ_{k≥0}(k+1)^{−s}δ_{(k+1)^{−p}}
     = Σ_{k≥1}k^{−s}δ_{k^{−p}}. ✓ D_n > 0 (`heineD_pos`), so log is meaningful. κ_p is right.
   - s ≤ 1 is correctly excluded (then `bdd` fails already at n = 1).
2. **§3.3 discharge table**, against item 11 §§7, 7b and G3′:
   - Item 11 H5, H6: MVT + (L1)–(L3) only. ✓ No Theorem H.
   - Item 11 H7 step 4 uses Theorem H only as the head upper bound for atoms k^{−p}, weights k^{−s₀}, "uniform in N".
     The o(N²) form suffices: `TheoremHPure.uniform_upper` gives log D_N ≤ −pN² log N + κN² + ηN² + C_η for all N, and
     sup_{N≤n}(ηN² + C_η) ≤ ηn² + C_η, so step 5's bound gets an extra ηn², removed by η → 0. (Lean's sorry-free
     `HL_upper` is the formal check of exactly this.) Instance (p, s₀, 1). ✓
   - Lower half "weights ≥ c₁j^{−s}" (H_L lower; G3′ Lemma K; Theorem T lower): monotonicity (H3) +
     instance (p, s, 1). This is a TheoremHPure use, not a general-atom use. H_all also covers it directly. ✓
   - Prop N: Theorem H_L at p = 2, s = s₀ = 2 for atoms f(ψ(j)) (a general-atom statement, but H_L itself consumes only
     the two pure instances). ✓
   - G3′-U: H7 with (Hw) s = s₀ = 2 → (2, 2, 1). ✓ Lemma Tr (s = 4 in L′ and Ch): Lemma K = H7 head (2, 2, 1, since
     j^{−4} ≤ j^{−2}) + lower half (2, 4, 1). ✓ T, T′, G3′*: (2, 2, 1), (2, s, 1) with s ≥ s₀ = 2 by (Hw). ✓
   - G3′-L: Lemma W with s = s_n = 4 + C″(1 + log n) → ∞. That use is uniform in s, so it is *not* a TheoremHPure
     instance. It is covered because Lemma W is proved from item 11 §7's explicit Lommel references, not from Theorem H.
     The table's "none" is right. The liminf half of B reuses G3′-L step 7. ✓
   - No use with C ≠ 1 and no use of (H-a) for general atoms through Theorem H itself. **No over-discharge found.**
   - Editor's remark: **correct.** Item 11 Theorem H (p = 2) assumes (H-b) c₁k^{−s} ≤ w_k ≤ c₂k^{−2}, s ≥ 2. Exact
     k^{−s} with s ≥ 2 satisfies it (c₁ = c₂ = 1), with error O(n log n), label PROVED + REVIEWED, Lommel references,
     no citation. Every G3′ instance is (2, s, 1) with s ≥ 2. Moreover Inputs.lean already stated before Plan 37 that
     "Item 11 supplies it … for p ∈ {1, 2} and s ≥ s0(p)". So citing item 11 changes no label and needs no new decision.
     See F1.
3. **No upgrade / no math change.** The full diff of every PROOF.md and RH file is labels, dated notes, pointers and
   new §0 rows, plus the new Corollary H-input. New labels: G2 Cor. A2 "PROVED" (re-derived: A1 + scaling
   sup_{𝒜_τ}I = τ²(E_p − p log τ), two lines, no citation; justified). G1 §0 rows for Sat_p, WC, A4′ are copied from the
   §3.1 header ✓. Sat_p⁺ "REVIEWED" is backed by review/REVIEW_Plan29.md ("Lemma Sat_p⁺ ACCEPT WITH FIXES") ✓. RH₁
   "(WLXZ v1 §§2–6)" matches RH_p1.md ✓. RH_p "G2 μ*, B*" matches RH_px.md's header, and its "Input from G2" uses only
   B*(i)–(ii) ✓. Historical text is kept: struck through plus a dated note (RH_p1_general.md), or a dated note after
   the old text (G1 A1, RH_px §6, RH_plt1 §6, RH_zeta §4.3, G3′ §8.3, plan-10). No history is rewritten. Lean diffs
   are inside `/-- … -/` docstrings only, and the added lines contain no nested `/-`.
4. **THEOREMS.md, 20+ rows sampled:** H_all, HZ, B*, A2, A-U, A-L, H-input (G2); G1-T, G1-L, A3, A4, CL, Sat_p, WC,
   A4′, Sat_p⁺, T3-conv, TL, T3-sv, TC, T3-avg, LP, T3-all, T3-log, G1-R, RH₁, RH₁(r), RH_p, seam, RH_ζ, E1 (G1); Z1,
   G3′-U, W, G3′-L, Tr, N, N″, B, Ch, Thm S, S′, V⁺, Lemmas P1–P3, 9.7*, 9.9*, N1, Q (G3′/rhfree); Lean rows. Labels
   are verbatim or faithfully abbreviated except as listed in F6–F7. Notation (c(2) = π²/16, κ = κ₂, β_n, Φ_n) is
   correct. Open problems (§4) are complete against G1 §4, G3′ §§5.5, 8.1, 9.3, RHFREE §4, RHFREE2 §§2, 4. Glossary
   entries checked: Theorem A, B, C, Lemma K, TC, P, κ, RH.
5. **README:** consistent with THEOREMS.md and the §0 tables. It writes "with no hypothesis on the zeros" rather than
   "unconditional", keeps the RH-disambiguation and the "nothing here is evidence about RH" line, and uses "certified"
   only for Arb. One inherited issue (F1, F9).
6. **VERIFICATION_POLICY.md:** the new table matches usage, with the gaps listed in F8.

## Findings

**F1 — MAJOR — discharge attributed only to (P); the p = 2 input was already supplied citation-free.**
Locations: G3′ PROOF.md §0 (20 notes and the new "Theorem H input" paragraph); G2 PROOF.md Cor. H-input,
"Consequence" sentence ("the result is PROVED-mod-cite (P) together with its other citations"); THEOREMS.md §1 H5
("named input Theorem H (p = 2), discharged on paper by G2 Cor. H-input (mod-cite (P))"), §3.1 last row, §3.2 last
sentence, §3.3 header and remark, §4 item 1 ("input discharged mod (P)"); README G3′ bullets and Lean bullet.
Issue: every G3′ instance is (2, s, 1) with s ≥ 2. Item 11 Theorem H (p = 2) supplies it, PROVED + REVIEWED with no
citation, and Inputs.lean already said so before Plan 37. Presenting G2 mod-cite (P) as *the* discharge makes G3′-U,
B, Ch, etc. appear to depend on (P), and through (P) on the unread Saff–Totik / Cegrell–Kolodziej–Levenberg. That is a
false dependency. It is not an overclaim, but it misstates the dependency graph, which is the main deliverable of a
consolidation. The remark's "would need a decision (and Rule R)" is too cautious: no label changes, only the
attribution of an input the repo already records. This review re-derived that all G3′ instances lie in item 11's
(H-b) range (Check 2).
Fix: replace the note with "; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there),
and also by G2 Cor. H-input (mod-cite (P))". In G2 Cor. H-input, reword the Consequence sentence so that (P) enters
only where G2 is the sole route: p ∉ {1, 2}, or p = 1 with s < 3/2, or p = 2 with s < 2. In practice that is Lean
`theoremHL` at general p. Update THEOREMS §§1, 3.1–3.3, 4 and the README to match, and turn the remark into the
recorded resolution.

**F2 — MINOR — G3′-L carries a (P) discharge note but uses no Theorem H instance.** G3′ §0 row G3′-L; THEOREMS §2.5.
§3.3 itself says "vacuously". The note implies a (P) dependence that does not exist by any route. Fix: for G3′-L, write
"; uses no Theorem H instance (THEOREMS §3.3)". Leave the original label text as is.

**F3 — MINOR — Cor. H-input `bdd`: cite the Lean proof; Lean label wording.** G2 PROOF.md §3. The `bdd` field is
already a sorry-free Lean theorem (`heineK_bdd_of_summable`), so only `asymp` is paper-only. "Lean `heineD_eq_det`,
PROVED" should read "sorry-free", per the repo's Lean vocabulary. Fix: add the pointer and change the word. Optional:
note in Inputs.lean that `bdd` is derivable for s > 1.

**F4 — MINOR — THEOREMS §1 overview wording.** (a) "The pointwise law with an O(1/n) rate is proved … and for the
smooth-ζ model" is wrong for ζ: there b_n/x_n has a κ/log n correction, and only b_N/(β_N/4) and a_N/(2b_N) are
1 + O(1/N). (b) "holds up to O(n²) unconditionally (mod (C1), (C5), Theorem H)": use "with no hypothesis on the zeros",
as the README does. Fix both phrases.

**F5 — MINOR — THEOREMS §3.1 (C1) row overclaims.** "(C1) ⇒ every G3′ result except S, W, Lemma G, Lemma N" is wrong.
Prop N, Lemmas R, K, Theorem T, T′, Lemma PC, Cor. N1, Prop. Q, Lemma P3 and Lemma 9.9* have no (C1) in their labels.
Fix: list the results that use (C1), or say "Z1, Z2 and every result built on them (G3′-U, G3′-L, N′–N‴, B, L′, Ch, C,
P, S, S′, V⁺, G3′*)".

**F6 — MINOR — Lemma W row drops "uniformly in s ≥ 4".** THEOREMS §2.5. That uniformity is the content of the lemma.
It is also why G3′-L (s = s_n → ∞) is not a TheoremHPure use. Fix: restore it, and add one sentence to §3.3's G3′-L
row saying that s_n grows with n, which no fixed-s instance covers, and that Lemma W is proved from item 11's Lommel
references instead.

**F7 — MINOR — "verbatim" deviations.** (a) RH_ζ: THEOREMS and G1 §0 have the annotated label "(… G2 — optimality,
for E1(iv) only, …)", but RH_zeta_close.md's header still reads "(…; DLMF; G2)". Either annotate the source header too
(as was done for RH_px.md) or say the label is "as in G1 §0". (b) Theorem S: THEOREMS copies G3′ §0's short citation
list but gives rhfree/RHFREE.md §3 as location, whose header lists "(C3) (3.1)–(3.2), (C6) Prop 2.1 (2.4) and §3
algebra, (C1)". Name the location of the copied label. (c) LP: THEOREMS uses §3.8's F_p(M) with min(1, ·), while G1 §0
row LP omits the min (pre-existing). Align G1 §0 with §3.8.

**F8 — MINOR — VERIFICATION_POLICY.md.**
- (a) "definitions copied from the G1 and G2 PROOF.md headers" is true only for PROVED-mod-cite, CONDITIONAL and GAP;
  PROVED-mod-input and REVIEWED come from elsewhere (this file's note, Rule R).
- (b) Labels used in the repo are undefined: PROOF SKETCH, DRAFT, REFUTED (vs RETRACTED), SUPERSEDED, PROVED-mod-G2,
  HYPOTHESIS, OBSTRUCTION, HEURISTIC, "sorry-free".
- (c) The G2 header sentence "item 11's convention, which VERIFICATION_POLICY.md's PROVED-mod-input generalizes" now
  contradicts the table, where mod-cite and mod-input are distinct.
- (d) "Optional — formalisation … Lean is not installed yet" is stale (pre-existing).

Fix: add one-line definitions and correct the attributions. Add a dated note to the G2 header and to the formalisation
paragraph.

**F9 — MINOR — README Lean bullet.** It says the input is supplied on paper "for all p > 0, s > 1 by G2" but omits
item 11 for p ∈ {1, 2}, s ≥ s₀(p) (the lean/README row has it). Fix with F1.

**F10 — INFO — Lean not rebuilt.** The edits are docstring-only and the added text contains no nested `/-`, so the
risk is negligible. Still, run `lean/check.sh` (AUDIT OK) in a checkout with the packages symlink before merging, and
record it.

**F11 — INFO — confirmations.** Corollary H-input is correct as stated, with κ_p = 3p/2 + log c(p) and s > 1 necessary
and sufficient for the `bdd` field. The §3.3 table has no over-discharge. The G2 A2 "PROVED" label is justified. History
was not rewritten.

## Re-check (2026-10-14, HEAD 4d1673f; commits 293fcbe, 4d1673f)

**Verdict: ACCEPT.** F1–F9 are resolved. One cosmetic nit remains (R1), and it does not block merge.

- **F1: resolved.**
  - Every G3′ §0 note (19 rows; G3′-L excepted, see F2), the G3′ §0 paragraph, README (G3′ and Lean bullets),
    lean/README, and THEOREMS header, §1 (H5), §§3.1–3.3 and §4 item 1 now name item 11 Theorem H (p = 2, s ≥ 2,
    PROVED + REVIEWED, citation-free) as the primary route, with G2 Cor. H-input (mod-cite (P)) as the alternative.
    `grep "discharged by G2"` finds only the historical mention in the THEOREMS §5 log.
  - **Sole-route claim verified.** Item 11's (H-b) is c₁k^{−s} ≤ w_k ≤ c₂k^{−s₀} with s ≥ s₀, where s₀(2) = 2 and
    s₀(1) = 3/2, and p ∈ {1, 2}. Exact weights k^{−s} satisfy it iff s ≥ s₀(p): the upper bound k^{−s} ≤ c₂k^{−s₀}
    needs s ≥ s₀, and the lower bound holds with c₁ = 1.
  - So within s > 1 the instances outside item 11's range are exactly: p ∉ {1, 2}; p = 1 with 1 < s < 3/2; p = 2 with
    1 < s < 2. This matches G2 Cor. H-input and THEOREMS §3.3.
  - The text correctly adds that the p = 1 item 11 route is itself mod-cite (Tricomi–Carlitz), so (P) is avoided there
    at the cost of a different citation.
  - "No G3′ result depends on (P)" is correct (Check 2 above).
- **F2: resolved.** G3′-L reads "uses no Theorem H instance (THEOREMS §3.3)" in G3′ §0 and THEOREMS §2.5. The original
  label text is kept.
- **F3: resolved** in G2 PROOF.md: it cites `heineK_bdd_of_summable` and says "sorry-free". The optional Inputs.lean
  note was not applied. That is acceptable, since lean/README now records that `bdd` is already sorry-free.
- **F4: resolved.** The overview gives the smooth-ζ law with its κ/log n correction and says "with no hypothesis on the
  zeros".
- **F5: resolved, with nit R1.** The §3.1 (C1) row now separates users from non-users.
- **F6: resolved.** The Lemma W row says "uniformly in s ≥ 4", and the §3.3 G3′-L row explains why s_n → ∞ is not a
  TheoremHPure instance.
- **F7: resolved.**
  - (a) RH_zeta_close.md has a dated note matching the G1 §0 annotation.
  - (b) The Thm S, S′ and V⁺ rows say "label as in G3′ §0; proof <rhfree file>".
  - (c) The G1 §0 LP row has min(1, ·), with a note.
- **F8: resolved.** Attributions are per label. The new definitions (PROVED-mod-G2, PROOF SKETCH/DRAFT, REFUTED vs
  RETRACTED, SUPERSEDED, HYPOTHESIS, OBSTRUCTION, HEURISTIC, sorry-free) match usage. The stale Lean sentence and the
  G2 header "generalizes" both have dated notes; nothing was rewritten.
- **F9: resolved.** The README Lean bullet names both routes.
- **F10:** the coordinator reports `lean/check.sh` AUDIT OK on this branch. lean/*.lean is unchanged since my first
  pass (comment-only edits).

**R1 (cosmetic, optional).** The THEOREMS §3.1 (C1) row lists neither Lemma P1 nor Lemma 9.7*. Both carry (C1) in their
labels (P1: "via RH99 Lemmas 9.7*, 9.9* …; (C1)"; 9.7*: "(C8) Prop. 1 (3.11), (C1)"), so both belong in the "uses"
list.
