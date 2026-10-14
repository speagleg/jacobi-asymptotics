# Rule R review — Plan 43 (D1: positioning G3′), PROOF.md §5.6

Reviewer: independent second reader (Rule R). Branch plan-43-d1, commit a1b6455 (`git diff master..HEAD`).
Date: 2026-10-14.

## Verdict: ACCEPT WITH FIXES

The mathematics of §5.6 is correct: Lemma L, Lemma CI (i)–(iii), Proposition I, Corollary Lz, Lemma D, Theorem Sp and
Corollary Pos all check, including the multiplicity conventions, the index↔height conversion, and the k₂ boundary.
All Plan 43 citation quotes were checked against freshly downloaded arXiv PDFs and match. The corrected claim (d(E) = 0
does NOT imply HMH, with the partial converse under o(K/log K)) is right. The fixes below are wording, consistency and
propagation fixes. None is a gap in a proof. F1 and F2 should be applied before promotion. F3–F8 are minor.

## Checks done

1. **Read:** AGENTS.md, the full diff, PROOF.md §§1, 2 (Z1), 3 (Z2, k₂), 5 (Prop N, N′), 5.2 (N″), 5.4 (Ch:
   definitions of d_ab, near, P, 𝒞), 5.5, 5.6; CITATIONS.md (C1) and the Plan 43 addenda; LOG.md entry; the plan doc,
   going through every Review-focus item; research/program/outline_D_G3p.md, RESEARCH_PROGRAM.md §D, novelty_G3p.md
   (Lamzouri lines); rhfree/RHFREE.md header (Theorem S).
2. **Sources fetched and read (arXiv PDFs, pdftotext):** GLSS 2503.15449v4 (abstract, §§1–3, 5, 7, 8); Lamzouri
   2609.02882v2 (abstract, §1 through Remark 1.2); Goldston math/0412313 (§5 Theorem 2 and after, §6 (6.7)–(6.11),
   Theorem 4 statement).
   - **(C5) addendum:** every quote is verbatim: abstract; §2 strip and four-zero sentences; §3 multiset and (3.1); §7 RH
     sentence, H(γ) bullets, HMH, Theorem 2 and its proof chain; §8 first sentence. Overbars and subscripts are lost in
     extraction only. GLSS L := (1/2π) log T, and (3.7) N(T) = TL + o(TL) is as used in P1.
   - **(C6) addendum:** verbatim: N(T) with footnote 1 ("0 ⩽ Re(s) ⩽ 1"), N0 and N0s, the Ns/Nd sentence, (1.1),
     the first sentence of Theorem 1.1, PRZD, CGdL 0.6792, Bui–Heath-Brown 19/27 "assuming only RH", and the GLSS
     sentence. The abstract says "unconditional proof". Theorem 1.1 has no hypothesis. The arXiv stamp is "8 Sep 2026".
   - **(C8) addendum:** verbatim: "It would be a major advance … even on RH." (§5, after Theorem 2, which assumes RH);
     SZC (6.9) and "Technically this is a conjecture on the average multiplicity …"; "refereed" [sic] sentence.
3. **Lamzouri's form.** Theorem 1.1 is liminf_{T→∞} N0s(T)/N(T) ⩾ C0 for the same multiset N(T) (0 < γ ⩽ T, with
   multiplicity). N0s is a count of simple zeros, so set and multiset counts agree. So 1 − N₀ˢ/N ≤ 1 − C₀ + o(1) for
   *all* large T, δ_sc ≤ 1 − C₀, and Prop I's upper bound gives d̄(E) ≤ 1 − C₀. Correct as stated. The strip
   convention ((C6) 0 ⩽ Re s ⩽ 1, (C1) 0 < β < 1) is reconciled by GLSS §2.
4. **Lemma L.** It uses only the existence of the zero 1 − β + iv ≠ β + iv, not equality of multiplicities, so r ∈ {0}
   ∪ [2, ∞) follows. (a)–(c) follow.
5. **Lemma CI.**
   - (i): the indices ≤ N(T) are whole lines, and h − 1 indices per line lie in E (index 1 and each line's first index
     do not). Correct.
   - (ii): N_dist ≥ N₀ˢ by L(b); A ≤ N₀ˢ by L(a); N − A = Σ_{H≥2} H ≤ 2Σ_{H≥2}(H − 1). Correct.
   - Sharpness lines: H = 3 (simple critical zero plus an off-line pair) gives equality in the first inequality, and
     H = 2 (an off-line pair) in the third. Correct. Any line containing a simple critical zero is an equality case of
     the first inequality.
   - (iii): Σ H² − Σ H = Σ H(H − 1) ≤ 2E(T)·Σ(H − 1). Correct, since all ordinates are > 14 > e and E increases on
     [e, ∞).
6. **Proposition I.**
   - Step 1 uses the subsequence K = N(T) → ∞. Correct.
   - Step 2 sets T = γ_K and uses [1, K] ⊂ [1, N(γ_K)], then K ≤ N(γ_K) ≤ K − 1 + 2E(γ_K). From
     K > N(γ_K − 0) ≥ N₀(γ_K) − E(γ_K) it gets E(γ_K) = o(K) and N(γ_K)/K → 1. The limsup over K is ≤ the limsup over
     T because γ_K → ∞. Correct.
   - Step 3, the chain (d) ⇒ (b) ⇒ (c) ⇒ (d): correct.
7. **Optimality of Cor Lz given (C6) (my check, informational).** Consider lines carrying one simple critical zero plus
   j ≥ 1 off-line pairs of simple zeros.
   - On each such line, H − 1 = 2j = #(zeros that are not simple-critical), and all zeros are simple and distinct.
   - So a configuration made of such lines plus isolated simple critical zeros satisfies every bound of (C6) Theorem 1.1
     (N0s/N ≥ C0, Nd = N, Ns∪0 = N, (Ns + N0)/2N ≥ C1).
   - It also has d̄(E) = 1 − N₀ˢ/N, which can equal 1 − C₀.
   - Hence 1 − C₀ is the best bound obtainable from (C6) Theorem 1.1 by counting. The text's remark that "83.62%
     distinct" does not help is right.
8. **Lemma D** (against §5.4's definitions).
   - near := γ̃_b − γ̃_a < 4C₀ (Z1 constant). P sums log⁺(1/d_ab) over near pairs. T ranges over subsets of [k₂, K].
   - For k₂ ≤ a < b, k₂ ≥ k₁ gives γ_a ≥ 10⁶, so 2π/log(γ_a/2π) ≈ 0.524 < 0.6 < 2C₀ = 5.32.
   - Pairs with d_ab < 1 are therefore near by Z1, and pairs with d_ab ≥ 1 contribute 0. So P(T) depends only on the
     values when they are distinct, and is +∞ on a repeat.
   - R_K = ([k₂, K] ∖ E) ∪ {k₂} is exactly the set of first indices ≥ k₂ of each value. If k₂ ∈ E, the earlier copy
     lies at an index < k₂, outside every T, so it does not matter.
   - |[k₂, K] ∖ R_K| = |E ∩ (k₂, K]|. The ≤ and ≥ steps are correct.
9. **Theorem Sp.** It applies Ch (REVIEWED) exactly as stated. Both terms are nonnegative. |e_K − |E ∩ [1, K]|| ≤ k₂.
   Correct.
   - Model-sequence remark: in σ^{(m)} the distinct values skip γ̃_{km+2}. Consecutive γ̃ have
     d ≥ log(γ̃_i/2π)/log(γ̃_{i+1}/2π) = 1 − o(1), and non-consecutive values have d ≳ 2. So 𝒞_dist = o(K), as claimed.
     The remark is labelled informal.
10. **Corollary Pos.** N″ (REVIEWED) and Prop I (a) ⇒ (d). Correct.
11. **P1, the HMH relations.**
    - HMH ⇒ (100%-SC) ⇒ d(E) = 0 (GLSS Thm 2 + Prop I). Correct.
    - Partial converse: with |E ∩ [1, N(T)]| = o(N/log N) and E(T) = O(log T), Σ H(H − 1) = o(N), so
      N^⊛ = N + o(N) = TL + o(TL). Correct.
    - Counting example: a proportion p = 1/h of the points on lines of multiplicity h → ∞ (h ≤ 2E) gives
      Σ(H − 1) ≈ N/h = o(N) and Σ H(H − 1) ≈ N. So d(E) = 0 while N^⊛ ≈ 2N. Correct. It is an abstract multiset,
      labelled as such.
    - The chain "PCC ⇒ (SG) ⇒ G3′ ⇒ (100%-SC) ⇐ HMH ⇐ PCC" matches Theorem C and GLSS §8. Correct.
12. **RH framing (AGENTS rule 3).**
    - RH appears only as a labelled hypothesis in quotes, and in P3/P4. No claim about RH. No "evidence" language.
    - P4's disclaimer is adequate.
13. **Numerics.** I ran `check_positioning.py` with the jacobi-asymptotics venv (14 s). The output is identical to the
    committed `.out`: [1] 400 OK, [2] 300 OK, [3] C0 = 0.6725007037, 1 − C0 = 0.3274992963. I read the script.
    - [1] checks L(a), CI(i), CI(ii) at every height on exact configurations.
    - [2] checks Lemma D by brute force with a value-only energy, i.e. the combinatorial core after step 1.
    - CI(iii) is not checked numerically. It is not claimed to be.
14. **Plan-doc Review focus.** I checked every item (see 4–10, 3, 12). Answers:
    - Lemma L needs only the zero set: yes.
    - Strip reconciliation: yes.
    - (C6) Theorem 1.1 is unconditional as stated: yes, but see F6.
    - Lemma D boundary: fine.

## Findings

**F1 (medium; PROOF §5.5 Plan 43 note, the last sentence before §5.6; §5.6 Remark P2, last bullet; LOG Plan 43
"Stop condition").** "the sources read obtain (100%-SC) only from PCC or HMH" is not accurate.
- Goldston (C8), a source read, states "Theorem 4. Assume the Riemann Hypothesis. SPC implies PCC and SZC." SZC
  "implies almost all the zeros are simple", and under RH every zero is critical. So (C8) also obtains (100%-SC) from
  RH + SPC.
- The repo's own Theorem S (SPC_ℂ⁺, REVIEWED) and Corollary P (RH + (V) ⇒ G3′, hence (100%-SC) by Cor Pos) are
  further conditional routes.
- **Fix:** reword to "the sources read obtain (100%-SC) only under hypotheses: PCC or HMH (GLSS Thms 1–2), RH + SPC
  ((C8) Thm 4 via SZC); see also this repo's Theorem S (SPC_ℂ⁺) and Corollary P (RH + (V))". Keep "none proves it
  unconditionally".

**F2 (medium; research/program/outline_D_G3p.md §1.2, lines 22–27, 56–66, table rows 86/88, D1 at 116–119, 348;
research/program/RESEARCH_PROGRAM.md §D, lines 80–81).** These files still assert the refuted claims:
- "d(E) = 0 ⟺ … HMH";
- "G3′ ⇒ HMH";
- "G3′ ⟺ HMH ∧ 𝒞_dist = o(K²)";
- "(GLSS's HMH)".

The correction is recorded only in PROOF §5.6 P1 and LOG. A reader of the program documents will meet the wrong
statement.
- **Fix:** add dated correction notes (do not rewrite history) at those places. The notes should say: HMH ⇒ d(E) = 0
  only; d(E) = 0 ⟺ (100%-SC) (Prop I); the split is G3′ ⟺ d(E) = 0 ∧ 𝒞_dist = o(K²) (Thm Sp); G3′ ⇒ HMH is NOT
  established; see PROOF §5.6. Use a `docs:` commit.

**F3 (low; §5.6 Cor Lz, Conventions, §5.5 Plan 43 note, §0 row, CITATIONS (C6) addendum usage).** There is a symbol
clash.
- C₀ already denotes Z1's constant 2.6613…, which §5.6 itself uses in Lemma D step 1 ("< 2C₀", "< 4C₀") and which
  §5.4's "near" uses.
- Cor Lz uses C₀ for Lamzouri's 0.67250… The Conventions renamed (C6)'s N₀ to avoid a clash but left C₀.
- **Fix:** rename Lamzouri's constant in PROOF (e.g. C_Lz := 3/2 − (1/√2)cot(1/√2), "(C6)'s C0"). Keep "C0" inside
  quotes.

**F4 (low; PROOF §5.5, the sentence "'As hard as a known open problem' is still *not* claimed: no surveyed source
states 'd(E) = 0' as open in this form").** This now sits next to a note, and P2/LOG, that invoke the AGENTS stop
condition "as hard as an open problem".
- **Fix:** append a dated qualifier. What is now claimed: G3′ ⇒ (100%-SC) ⇒ N_s/N → 1, which is Montgomery's
  simplicity conjecture as quoted in the GLSS abstract. Its open status rests only on the quoted status statements (P2,
  P3). The original sentence remains true for "d(E) = 0" as literally phrased.

**F5 (low; LOG Plan 43, "novelty note in research/program/novelty_G3p.md confirmed").** novelty_G3p.md (around line
204) says that Lamzouri's "83.62% distinct zeros updates the 0.4075 bound". §5.6 Cor Lz correctly says that this
proportion counts distinct *zeros*, does *not* bound N_dist, and is not used. The update comes from C₀ instead.
- **Fix:** change "confirmed" to "corrected (the update comes from C₀, not from 83.62% distinct zeros)". Optionally add a
  dated note in novelty_G3p.md.

**F6 (low; §5.6 Corollary Lz, §0 row).** Cor Lz rests on an arXiv v2 preprint whose refereeing status is unknown. This
is recorded in CITATIONS but not at the point of use.
- **Fix:** add "((C6) is arXiv v2, Sept 2026; refereeing status unknown)" to Cor Lz, and "(C6) preprint" in the §0
  row. The other results of §5.6 do not depend on (C6).

**F7 (low; §5.6 Lemma CI label and (iii) proof).** The label "PROVED (from Lemma L)" understates the dependencies.
- Lemma L is mod-cite (C5) §2, and (iii) uses the (C1) multiplicity bound. "Z1 step 5" is stated inside "fix k ≥ k₁".
  The bound H(v) ≤ N(v + 0) − N(v − 0) ≤ 2E(v) holds for every v ≥ e directly from (C1), and all ordinates exceed 14.
- **Fix:** relabel as "PROVED-mod-cite (C5) §2 [(i)–(ii)], (C1) [(iii)]", and cite (C1)/(C2) directly for H(v) ≤ 2E(v),
  v ≥ e.

**F8 (low; §5.6 Remark P3, last sentences).** "a statement that the sources read describe as not known on RH" goes
slightly beyond the quotes. Only Goldston (2004) says it ("a major advance … even on RH"). (C6) (2026) only lists
RH-conditional proportions below 1.
- **Fix:** "a statement that Goldston (C8, 2004) calls 'a major advance … even on RH', and for which the best
  RH-conditional proportions quoted in (C6) (2026) are 19/27 and 0.6792".

**F9 (informational, optional addition to Cor Lz).** The bound 1 − C₀ is optimal among bounds derivable by counting from
(C6) Theorem 1.1. The configuration in Check 7 meets all four of its inequalities and has d̄(E) = 1 − N₀ˢ/N. So any
improvement of Cor Lz needs new input on ordinate coincidences, not a better combination of (C6)'s bounds.

**F10 (informational).** "Sharpness of (ii): Each inequality can be an equality line by line" gives examples for the
first and third inequalities only. The middle one is an equality when no line with H ≥ 2 carries a simple critical
zero. This is trivial, but it could be said. In P1 the phrase "in each window" in the counting example is informal.
"Take h = h(T) slowly increasing, and on each dyadic block put a proportion 1/h of its points on lines of multiplicity
h" is cleaner.

## Recommended labels (after F1–F8)

- Lemma L: PROVED-mod-cite (C5) §2; REVIEWED.
- Lemma CI: PROVED-mod-cite (C5) §2 (via L), (C1) for (iii); REVIEWED.
- Proposition I: PROVED-mod-cite (C1), (C5) §2; REVIEWED; novelty UNCHECKED.
- Corollary Lz: PROVED-mod-cite (C6) Thm 1.1 (arXiv v2, refereeing unknown), (C1), (C5) §2; REVIEWED.
- Lemma D: PROVED-mod-cite (C1) (through Z1, Z2's k₂); REVIEWED.
- Theorem Sp: PROVED-mod-cite (C1) + mod-input Theorem H (as Ch); REVIEWED; novelty UNCHECKED.
- Corollary Pos: PROVED-mod-cite (C1), (C5) §2 + mod-input Theorem H (through N″); REVIEWED; novelty UNCHECKED.
- Remarks P1–P4: status/quote remarks. P1's partial converse is PROVED-mod-cite (C1), (C5) (3.7). "G3′ ⇒ HMH" and
  "G3′ ⇒ SZC" stay GAP (not established).
- §5.6 heading and §0 row: replace "Rule R pending" with "Rule R ACCEPT WITH FIXES (review/REVIEW_Plan43.md)". After a
  re-check of F1–F8, use REVIEWED.

## Re-check (2026-10-14; commits 785dce8 and 2b2571e)

**Verdict: ACCEPT.** F1–F10 are all resolved. Nothing blocks promotion to REVIEWED.

How I checked: I read `git diff a1b6455..HEAD` for PROOF.md, LOG.md and research/program/, then grepped for stale
symbols and status markers ("1 − C₀", "0.6725", "only from PCC", "Rule R pending").

- **F1: resolved.** The §5.5 note, Remark P2 and the LOG entry now say "only under hypotheses". They list PCC/HMH (GLSS
  Theorems 1–2), RH + SPC ((C8) Theorem 4 via SZC, with "under RH every zero is critical"), Theorem S and Corollary P,
  and add "None of them proves it unconditionally". This is accurate.
- **F2: resolved.** Dated correction notes were added without rewriting history:
  - outline_D_G3p.md: after §1 item 2, which sits directly below item 1's "this is GLSS's HMH"; after §1.2's
    "Consequence", with the corrected chain; in §1.3, with "HMH should read d(E) = 0"; after the §1.4 table; under D1;
    and in the paper-outline bullet;
  - RESEARCH_PROGRAM.md §D;
  - novelty_G3p.md (the F5 companion).

  All of these notes are correct.
- **F3: resolved.** Lamzouri's constant is C_Lz everywhere in PROOF.md and LOG.md. C₀ now means only Z1's constant
  (2.66…), which Lemma D uses. "C0" remains only inside verbatim quotes in CITATIONS.md, as it should. The plan doc's
  T5 line still reads "1 − C₀". That line is a historical task list, so I leave it alone (nit N1).
- **F4: resolved.** The qualifier on §5.5's "not claimed" sentence is precise. G3′ ⇒ (100%-SC) ⇒ N_s/N → 1, which is
  the simplicity conjecture attributed to Montgomery in the GLSS abstract. The open status rests only on quotes.
- **F5: resolved.** The LOG now says "corrected", with the right reason.
- **F6: resolved.** The preprint status is noted at Cor Lz, in the §0 row, in the §5.5 note and in P2. Cor Lz also says
  that the other §5.6 results do not depend on (C6). This is true: Lemma L, CI, Prop I, Lemma D, Sp and Pos do not use
  (C6).
- **F7: resolved.** The new label is "PROVED-mod-cite (C5) §2 [(i)–(ii), via Lemma L], (C1) [(iii)]". The proof of
  (iii) now gets H(v) ≤ N(v + 0) − N(v − 0) ≤ 2E(v) from (C1) for every v ≥ e, notes that all ordinates are > 14, and
  uses that E is monotone. Correct.
- **F8: resolved.** P3 now quotes Goldston (2004) and lists (C6)'s RH-conditional proportions without paraphrasing them
  as "not known". RH appears only as a labelled hypothesis.
- **F9: resolved.** The optimality remark at Cor Lz matches my check 7. Configurations with no repeats other than lines
  carrying one simple critical zero plus off-line simple pairs satisfy all four inequalities of (C6) Theorem 1.1. The
  remark is stated as a limit on what counting can give, with no claim about ζ.
- **F10: resolved.** Sharpness of the middle inequality was added. The counting example now uses dyadic blocks with a
  slowly increasing h(T) ≤ 2E(T). Nit N2: the old notation "h_T" survives in "Σ(H − 1) ≈ N/h_T" next to the new "h".
  This is cosmetic.
- **New P1 partial-converse label: correct.** The label "PROVED-mod-cite (C1), (C5) (3.7)" is right. The argument uses:
  - Lemma CI(iii), which itself uses (C1);
  - log N(T) ~ log T, from (C1);
  - GLSS (3.7), N(T) = TL + o(TL), which I checked verbatim against the PDF.

  Nothing else is needed.

**Remaining items (non-blocking).**
- N1: the plan doc's T5 still says "C₀", and T10 is unticked. Tick T10 and optionally add "(C_Lz in PROOF)" when
  promoting.
- N2: "h_T" vs "h" in P1's counting example.
- The status strings "re-check pending" in the §5.6 heading, the §0 row and the LOG should become "re-check ACCEPT —
  REVIEWED" at promotion.

**Final labels.**
- Lemma L: PROVED-mod-cite (C5) §2; REVIEWED.
- Lemma CI: PROVED-mod-cite (C5) §2 [(i)–(ii)], (C1) [(iii)]; REVIEWED.
- Proposition I: PROVED-mod-cite (C1), (C5) §2; REVIEWED; novelty UNCHECKED.
- Corollary Lz: PROVED-mod-cite (C6) Thm 1.1 (arXiv v2 preprint, refereeing unknown), (C1), (C5) §2; REVIEWED.
- Lemma D: PROVED-mod-cite (C1) (through Z1/Z2); REVIEWED.
- Theorem Sp: PROVED-mod-cite (C1) + mod-input Theorem H (as Ch); REVIEWED; novelty UNCHECKED.
- Corollary Pos: PROVED-mod-cite (C1), (C5) §2 + mod-input Theorem H (through N″); REVIEWED; novelty UNCHECKED.
- P1 partial converse: PROVED-mod-cite (C1), (C5) (3.7); REVIEWED.
- "G3′ ⇒ HMH" and "G3′ ⇒ SZC": GAP (not established).
- §5.6 heading and §0 row: "Rule R ACCEPT WITH FIXES (review/REVIEW_Plan43.md), fixes applied, re-check ACCEPT —
  REVIEWED; novelty UNCHECKED".
