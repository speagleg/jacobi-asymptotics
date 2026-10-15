# Paper II — notes (draft of 2026-10-15)

Local working notes; not part of the paper. Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main`
(no latexmk). Current build (after the referee fixes and the completion of Theorem 1.4 for every p > 0, 2026-10-15): 105 pp., 0 errors,
0 LaTeX/bibtex warnings, 0 overfull/underfull boxes.

Sources: `papers/paper2/` (old combined draft, unchanged), `research/G1/RH/second_order/E_pgt1.md` (Theorem 1.4),
`research/G1/RH/px/RH_px.md` (§8), `research/G1/RH/second_order/TAIL.md` (Proposition 8.6; reviewed and merged on
master), planning documents `research/program/papers_split/{SERIES.md, PAPER_II_OUTLINE.md}` and
`research/program/paper_style.md` (local, main checkout).

## 1. Section map (page numbers of the current build)

| § | Title (short) | pp. | Source |
|---|---|---|---|
| — | title, abstract | 1 | new |
| 1 | Introduction (Def 1.1, Thm 1.2, Cor 1.3, Thm 1.4 on p. 2; Rem 1.5, 1.6) | 1–5 | new prose; Paper 2 sec_front reused in part |
| 2 | Preliminaries (Def 2.1, Rem 2.2, Prop 2.3, tools §§2.4–2.7) | 5–10 | Paper 2 sec_2 (slow variation and Christoffel extremal property removed) |
| 3 | The Christoffel shift (Thm 3.1, Lemmas 3.2–3.5, Rem 3.6) | 10–14 | Paper 2 sec_3 without the converse |
| 4 | Riemann–Hilbert problem and common frame | 14–25 | Paper 2 sec_5 (now for every α > −1) |
| 5 | Outer scalar and properties of the frame (Lemma 5.1, Table 5.1, Prop 5.6) | 25–34 | Paper 2 sec_6 |
| 6 | Hard edge: comparison with a Bessel model (Props 6.4, 6.5, 6.6; Prop 6.5 was "Theorem 6.5") | 35–44 | Paper 2 sec_7 |
| 7 | Proof of Theorems 7.1, 1.2, Corollary 1.3 | 44–45 | Paper 2 sec_8 + sec_4 assembly Steps 1–3 |
| 8 | Pure powers, p > 1: classical hard-edge parametrix (Lemmas 8.1–8.3, Prop 8.4, Rem 8.5; §8.4 states Prop 8.6) | 45–52 | NEW: RH_px §§4–5, E_pgt1 Lemma E.2, TAIL.md §§3, 6 |
| 9 | The 1/n term for p > 1 (Lemmas 9.1–9.4, Prop 9.5, Rem 9.6 incl. derivation of the Lommel closed form) | 52–58 | NEW: E_pgt1 §§2–7.1 |
| 10 | Numerical illustrations (Tables 10.1, 10.2) | 58–60 | Paper 2 §9 + SECOND §1.1 grid (check_so_grid.out) |
| 11 | Further remarks (Conjectures 11.1, 11.2) | 60–62 | Paper 2 §10 rewritten |
| A | Outer scalar for p ≠ 1 | 62–67 | Paper 2 app_outer |
| B | A priori bound at the hard edge | 67–70 | Paper 2 app_c |
| C | Two L² bounds on a star | 70–73 | Paper 2 app_a |
| D | Uniform invertibility of the comparison problem | 73–76 | Paper 2 app_b |
| E | First corrections and Laurent coefficients | 76–77 | NEW: E_pgt1 §5 |
| F | Proof of the localisation bound (Lemmas F.1 Stieltjes bound, F.2 row product; proof of Prop 8.6) | 77–79 | moved verbatim from §8.4 in the editor pass |

Numbering versus PAPER_II_OUTLINE.md: everything matches except **Proposition 5.6** (outline: 5.7; the quotient
remark moved to §8 removed one item before it), Definition 4.10 (the outer-scalar properties, formerly (O1)–(O5)), Proposition 6.5 (was Theorem 6.5) and the two
lemmas of the tail bound (F.1, F.2; outline: in §8).
Paper III must cite the numbers of the frozen version; exported labels: thm:analytic (1.2), cor:pure (1.3), thm:onen
(1.4), rem:lommel (1.6), thm:shift (3.1), lem:transfer (3.3), lem:chain-limit (3.4), prop:tail (8.6).

## 2. Placeholders

- Author line "Gordon [Surname]"; date line; repository tag "[to be fixed at submission]" in the data statement.
- MSC codes, affiliation, e-mail: not yet present.
- Paper III bibliography entry: title provisional ("Stability and instability of recurrence asymptotics …").

## 3. Open items and items pending review

1. **Prop 8.6 and its lemmas (now F.1, F.2; the proof is in App. F)**: written from TAIL.md, which is now reviewed (REVIEW_Plan69, fixes applied);
   the Paper II text itself is new writing and still needs an independent reading against TAIL.md. Part (a) is stated only
   for 1 ≤ M ≤ γ_* n^{2/p} (the deep-tail polynomial-inequality step is left to Paper III, as agreed). The L² bound
   ‖Q₋ − Q̃₋‖ ≤ C(ε′_n n^{−1/2} + n^{−1}) is now in the statement of Prop 6.6 (review fix F7), label eq:he-L2-diff.
2. **§§8–9 and App. E are new LaTeX** from reviewed research notes; they need a second reading against RH_px.md and
   E_pgt1.md. Points flagged by the drafting agent:
   - Prop 8.4, Step 2 (identification of the error matrix at the hard edge for every α > −1): follows RH_px §5 at the
     same level of detail; the step "the local solution has no jump on Γ \ {0}" takes boundary regularity for granted as
     the source does. A referee may ask for more. App. B's L² corollary (which needs |α| < 1) is not used; Lemmas
     sumbound, lenssector and Prop apriori(ii)–(iii) are cited, whose proofs use only α > −1 (stated in App. B's opening).
   - Uniform bound on ρ_n near the negative axis: obtained from the flatness bound Lemma 8.1(iv) (E_pgt1 Lemma E.2)
     instead of RH_px's Hölder lemma.
   - Two inputs taken from inside the proof of Lemma A.1 (lem:binetcut), not its statement (log B bounded near 0 with
     boundary values; |log B| ≤ C_n log|z| at ∞). Consider adding them to the statement of Lemma A.1.
   - Meromorphy of the model corrections is proved by "no jump plus growth bound" and the residue combinations are
     derived by hand in §9; values identical to E_pgt1 (re-checked symbolically by the drafting agent, scratch only).
   - Rem 8.5's sentence for p < 1 is weaker than E_pgt1 §9 (says only that the available bound does not give flatness
     to o(1/n)).
3. **Prop 5.6(vii)** (a priori bound and admissibility of Q) is stated under |α| < 1, conservatively; Prop B.4 holds for
   all α > −1 and only Cor B.5 needs |α| < 1. Could be relaxed.
4. **(Resolved 2026-10-15, see §8: now Theorem 1.4 for every p > 0.)** Former Conjecture 11.1 (p ≤ 1): other agents (E_p1.md for p = 1, E_plt1.md for 0 < p < 1) claim proofs, review in
   progress. Keep as a conjecture until reviewed; then Theorem 1.4 extends and §§8–9 need a p ≤ 1 counterpart.
   The sentence attributing the p = 1 averaged statement to Paper III relies on TAIL.md's telescoping (every s > 1).
5. Human expert reading of §§4–6 and Apps. B, D (REFEREE2 "what a human expert should still check") is still needed.
6. Intro length: §2 starts about 45% down p. 5; the introduction is just under 4 pages after the abstract.
7. Disc notation renamed U(z₀, r) → 𝔻(z₀, r) in the editor pass (EDIT_REPORT N12 resolved); C_± now defined in §2.
8. Length 80 pp (outline estimate 70–76 + 3–4 for Prop 8.6). §8 is now about 7 pp; the proof of Prop 8.6 (≈2.5 pp) is
   in App. F. Further cuts would need deleting mathematics or the numerical tables; see §7 below.

## 4. Sources to verify (citations)

- All 19 printed references are READ/OPENED in the repo's citation records (see papers/paper2/NOTES.md §4 and
  research/G1/RH/CITATIONS.md). No UNREAD key is cited (BGT, Vuil, Fischer, BueMar are uncited and do not print).
- DPQ: only the statement of Prop. 2.1 is recorded verbatim; used for attribution only.
- LL: printed as "Research announcement, 1999"; journal/book data not verified. Monien: arXiv only; publication status
  not verified. DD: volume 435(12), pp. 3056–3084 added from Crossref (doi 10.1016/j.laa.2011.05.035). DLMF release date from pages fetched 2026-10-14.
- Quotations (CD abstract, DP §1) to be re-verified character by character before submission.
- DLMF 10.32.4, 10.32.9 (used in Prop 8.6(b)) are recorded in research/G1/CITATIONS.md "(DLMF-3)", cited directly in §8,
  not listed in §2.7. KMVV (6.19)–(6.21) cited directly in §8, not in §2.5. Teschl (row product) not cited: Lemma 8.8
  proves the identity.
- Novelty: UNCHECKED for Thm 1.4 and Prop 8.6 (no literature search done for this draft).

## 5. Symbol choices (series notation, SERIES.md §4)

κ is not used. ς_n := ((n−1)/n)^p (§3); υ_± := 1/(1 − e^{∓2iθ}) (§§4–6); 𝗁_∞ (normalisation lemma); 𝗏_n (regular
majorant); 𝗀₃, 𝗀₅ (Airy coefficients of φ̃, E_pgt1's κ, κκ₂); 𝔄₀, 𝔄_r, 𝔅_r, 𝔠₀ (Laurent coefficients, E_pgt1's A₀, A_r,
B_r, C₀); 𝖱 error matrix of §§8–9; γ_* the range constant of Prop 8.6(a); zeta-Hankel parameters (q, r) instead of
(a, b) to avoid a_n, b_n; incomplete beta 𝓑_y; arc_β; λ_p; ℓ (Paper 2's ℓ₁).

## 6. Process

Drafted in parallel chunks (front + §§1–3; §§4–5 + App. A; §§6–7 + Apps. B–D; §§8–9 + App. E; §§10–11) against a
shared brief, then integrated, rebuilt and style-checked (see STYLE_CHECK.md). Commits: one per chunk, prefix `docs:`.

## 7. Editor pass (2026-10-15, branch plan-70-paperII)

Human-readability pass; no mathematical statement, hypothesis, constant or proof step changed (a separate referee is
checking §§8–9 and App. E). Exported numbers unchanged (1.2, 1.3, 1.4, 1.6, 3.1, 3.3, 3.4, 8.6).
- Introduction: "Context" now opens with the relation to Papers I and III, then a paragraph "Two difficulties" (nodes
  accumulating at the hard edge; non-analytic r_n) that the literature paragraphs answer; r_n and the rescaling z = n^p x
  defined there and used in the method paragraph; organisation rewritten with corrected reading paths (Thm 1.4 needs
  App. B and the Bessel model of §6.2 / (6.7), which the old text omitted). Lommel derivation moved from Rem 1.6 to the
  end of Rem 9.6 (Rem 1.6 keeps the formulas); the (2,2) check is no longer repeated three times.
- Footnote on Paper I's a_{k+1} deleted. "Jacobi coefficients" → "recurrence coefficients" everywhere (title term).
- Proof of Prop 8.6 with Lemmas 8.7–8.8 moved verbatim to App. F (now Lemmas F.1, F.2); statement stays as Prop 8.6.
- Theorem 6.5 → Proposition 6.5 (label prop:UR-true). Labels renamed: rem:not-proved → rem:circle-terms; App. B/C/D
  legacy prefixes (lem:B-cauchy, lem:A-power, lem:B-block, …) → lem:cauchy-arcs, lem:star-power, lem:star-log,
  lem:edge-block, sec:apriori-*, sec:resolvent-*, eq:star-*, eq:resolvent-*.
- Theorem-environment titles in one style (initial capital, no leading article for lemmas).
- Section openers of §§5, 7, 8, 9 and Apps. B, D, F rewritten (what and why, not "This section proves").
- Bibliography: DD volume 435(12), pp. 3056–3084 (Crossref); arXiv years moved to year fields; VA special issue as
  note; DLMF title protected. bibtex 0 warnings.
- \raggedbottom added (removes the underfull vboxes).

Items for the author or the referee:
- Page count 80 (target 70–76). The remaining length is mathematics (§§4–6 frame and comparison, Apps. A–D) and the two
  tables; reaching 76 would need cutting Table 10.2 to one row per p, dropping Lemma E.1's 𝔠₀ (unused in the paper),
  or condensing §2.7.
- 𝔠₀ in Lemma E.1 is stated "for completeness" and used nowhere in II (nor, per PAPER_III_OUTLINE, in III).
- LL is still cited as "Research announcement, 1999" without journal data.


## 8. Referee fixes and Theorem 1.4 for every p > 0 (2026-10-15, branch plan-70-paperII)

**Referee fixes (REFEREE_MATH.md), commit 3e6f87d.** M1: Prop 8.4 Step 2 rewritten with the referee's citation-free
paragraph (α > −1/2: (R-at-zero) + Lemma cauchy-arcs(c) on R − I; −1 < α ≤ −1/2: Prop 5.6(vii) + CD Thm 4.4 as in §6);
the local solution X̃ is gone; the sentences claiming that §8 never uses Prop 5.6(vii) are corrected (standing
assumptions, the paragraph before the proof, the Outline). m1: Lemma A.1(iii) extended by the two fixed-n facts; Lemma 8.1
cites (iii). m2: O(n^{−p} + n^{−3}) in the remark after Lemma 8.1 (and E_pgt1 Remark (1), marked). m3: f^{1/2} at δ.
m4: App. F renamed B(s') → 𝖠_z(s'), t → τ'. m5: KMVV (6.19)–(6.21) in §2.5(a), DLMF 10.32.4/10.32.9 in §2.7(c), and the §1
sentence now says the Lommel formulas are quoted at the point of use. m6: the middle M-range of App. F case (b) stated.
m8: a′ → a_* in Lemma 9.3. m7 (Teschl) not done: Teschl not read.

**New material.**
| § | Content | pp. (105-p. build) | Source |
|---|---|---|---|
| 1 | Thm 1.4 restated for every p > 0 (𝗄_p := 2pc(p)ζ(−p)); Rem 1.7 (second order at p = 1); external-results paragraph incl. the WLXZ dependence at p = 1; method, organisation and reading paths | 1–6 | E_plt1 Thm E′.1, E_p1 Thms E1.6, E1.10 |
| 10 | Pure powers 0 < p < 1 (Lemmas 10.1 band factor with zeta moments, 10.2 Szegő of e^{−𝖽x}, 10.3, 10.4 glued parametrix; Props 10.5, 10.8; Lemmas 10.6, 10.7; proof; Rem 10.9) | 59–65 | E_plt1, RH_plt1b §2, REVIEW_Plan67_A/B |
| 11 | Pure powers p = 1 (fold; comparison with Tricomi–Carlitz, Cor 11.7 = −1/24; Lemma 11.8 differences in s; Prop 11.9 first-order analysis in the symmetric variable; Lemmas 11.10–11.11; Prop 11.12; Thm 11.13 chain; proof; Rem 11.14) | 66–73 | E_p1, RH_p1, RH_p1_general, REVIEW_Plan66_A/B |
| 12 | Numerics: Tables 12.3 (n^{−1−p} coefficient, p < 1) and 12.4 (second order at p = 1) added | 74–78 | check_e_plt1_num.out, check_e1_tc.out, check_e1_rate.out |
| 13 | Conjecture 13.1 (alternating constant at p = 1), Conjecture 13.2 (tilt law), open coefficients | 78–79 | E_p1 §8, E_plt1 §10 |
| G | Lemma 10.1(iv)–(v); 𝖽-derivative of the full Airy coefficient | 97–98 | E_plt1 §3, Lemma E′.5 |
| H | First-order analysis at p = 1 (setup, Stirling truncation, Szegő functions, Airy reduction, Fisher–Hartwig parametrix and mismatch, behaviour at 0, identification), two-term models, second-order jumps | 98–105 | RH_p1_general, E_p1 §3 |

**Dependency of p = 1 on Paper III removed.** E_p1 fixes d₁ by UL Cor UL-3.10 (Paper III). Paper II uses instead the new
Lemma 11.8 (for every p > 0: log h_n(s) − log h_n(t) = −(s−t) log n + O(1)), proved from the minimum property, Jensen,
the Christoffel identity h_n(xσ) = u_n h_n(σ), Cor 1.3 and Lemma 3.4 (no tail bound). Existence of the 1/N term (Thm 11.13)
plus Lemma 11.8 at t = 3/2 plus d₁(3/2) = −1/4 (Cor 11.7, elementary) gives d₁ = −(s−1)/2. **Lemma 11.8 is new and has not
had a Rule R review.**

**Other deviations from the reviewed sources (need a second reading).**
- §10: residue combinations stated exactly in 𝖽 (source: first order in λ; re-checked exactly by the drafting agent,
  scratch only); bound (10.5) on the whole discs (source: on the circles); the seam split Ǎ = Ǎ^a + Ǎ^s with the claim that
  the seam boundary values of G have derivatives ≤ Cn^C (one line, not in the sources); Ψ_α bounds near 0 on the moved
  rays; the M1-corrected Step 2 run for p < 1.
- §11/App. H: the identification at the origin rewritten without the local solution X̃ (Lemma cauchy-arcs(c) applied to
  z(𝖷 − I) − 𝖷₁, then the constant removed along arg z = π/8); the log² padding of the amplification bound at α = −1/2
  dropped (orders ±½ are elementary). In App. H the Fisher–Hartwig exponent α + ½ is written a (local to App. H).
- p = 1 relies on WLXZ's analysis (uniform O(e^{−cN}) jumps up to the largest node; uniform Cauchy bound): stated in §1
  after Thm 1.4, in §2.4, and after Prop 11.9.

**Notation.** 𝗄_p (not κ_p, which Papers I/III reserve for 3p/2 + log c(p)); 𝖽_n := 2ζ(−p)n^{−p}; 𝖤_n remainder of the
band function; 𝖬_k moments; 𝔧 seam jump; 𝔎 Cauchy kernel; ϱ^mod; 𝖾_N symmetric chain (as Paper III); 𝖿₀, 𝖿₁ chain
constants at p = 1; 𝖷 error matrix at p = 1; 𝖰_m, 𝒟_h, 𝒟_q, 𝒩, 𝒩_s, 𝖶_N; App. H band jump 𝗃.

**Numbering.** Exported numbers unchanged: Thm 1.2, Cor 1.3, Thm 1.4, Rem 1.6, Thm 3.1, Lemmas 3.2–3.5, Prop 8.6, Def 1.1.
Changed: old §10 (numerics) → §12, Tables 10.1, 10.2 → 12.1, 12.2; old §11 → §13, Conjecture 11.1 (1/n term for p ≤ 1)
removed (now Theorem 1.4), Conjecture 11.2 (tilt) → Conjecture 13.2; new Rem 1.7. **Paper III must update**
papers/paperIII/sec8.tex: [II, Conjecture 11.1] is now [II, Theorem 1.4]; [II, Conjecture 11.2] → [II, Conjecture 13.2];
Paper III's remarks that the pointwise 1/n term for p ≤ 1 is unknown are out of date.

**Open items.** Second reading of §§10–11 and Apps. G–H against the sources (and of Lemma 11.8); m7 (Teschl); the
introduction is now about 5 pages (guide: ≤ 4); length 105 pp.; novelty search for Thm 1.4 (p ≤ 1) and Cor 11.7 not done.
