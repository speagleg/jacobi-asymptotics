# Paper II — notes (draft of 2026-10-15)

Local working notes; not part of the paper. Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main`
(no latexmk). Current build: 81 pp., 0 errors, 0 warnings, 0 overfull boxes (one underfull vbox in §5 and one underfull
hbox in the data statement, both harmless).

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
| 5 | Outer scalar and properties of the frame (Lemma 5.1, Table 5.1, Prop 5.6) | 25–35 | Paper 2 sec_6 |
| 6 | Hard edge: comparison with a Bessel model (Prop 6.6 now states the L² bound) | 35–44 | Paper 2 sec_7 |
| 7 | Proof of Theorems 7.1, 1.2, Corollary 1.3 | 44–46 | Paper 2 sec_8 + sec_4 assembly Steps 1–3 |
| 8 | Pure powers, p > 1: classical hard-edge parametrix (Lemmas 8.1–8.3, Prop 8.4, Rem 8.5, Prop 8.6, Lemmas 8.7–8.8) | 46–55 | NEW: RH_px §§4–5, E_pgt1 Lemma E.2, TAIL.md §§3, 6 |
| 9 | The 1/n term for p > 1 (Lemmas 9.1–9.4, Prop 9.5, Rem 9.6) | 55–61 | NEW: E_pgt1 §§2–7.1 |
| 10 | Numerical illustrations (Tables 10.1, 10.2) | 61–64 | Paper 2 §9 + SECOND §1.1 grid (check_so_grid.out) |
| 11 | Further remarks (Conjectures 11.1, 11.2) | 64–65 | Paper 2 §10 rewritten |
| A | Outer scalar for p ≠ 1 | 65–70 | Paper 2 app_outer |
| B | A priori bound at the hard edge | 70–73 | Paper 2 app_c |
| C | Two L² bounds on a star | 73–75 | Paper 2 app_a |
| D | Uniform invertibility of the comparison problem | 75–79 | Paper 2 app_b |
| E | First corrections and Laurent coefficients | 79–80 | NEW: E_pgt1 §5 |

Numbering versus PAPER_II_OUTLINE.md: everything matches except **Proposition 5.6** (outline: 5.7; the quotient
remark moved to §8 removed one item before it) and Definition 4.10 (the outer-scalar properties, formerly (O1)–(O5)).
Paper III must cite the numbers of the frozen version; exported labels: thm:analytic (1.2), cor:pure (1.3), thm:onen
(1.4), rem:lommel (1.6), thm:shift (3.1), lem:transfer (3.3), lem:chain-limit (3.4), prop:tail (8.6).

## 2. Placeholders

- Author line "Gordon [Surname]"; date line; repository tag "[to be fixed at submission]" in the data statement.
- MSC codes, affiliation, e-mail: not yet present.
- §2.1 footnote on Paper I's indexing (a_{k+1}): delete once the Paper I revision (a_k, arc_β, 𝓑_y) is merged.
- Paper III bibliography entry: title provisional ("Stability and instability of recurrence asymptotics …").

## 3. Open items and items pending review

1. **Prop 8.6 and its lemmas (8.7, 8.8)**: written from TAIL.md, which is now reviewed (REVIEW_Plan69, fixes applied);
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
4. **Conjecture 11.1 (p ≤ 1)**: other agents (E_p1.md for p = 1, E_plt1.md for 0 < p < 1) claim proofs, review in
   progress. Keep as a conjecture until reviewed; then Theorem 1.4 extends and §§8–9 need a p ≤ 1 counterpart.
   The sentence attributing the p = 1 averaged statement to Paper III relies on TAIL.md's telescoping (every s > 1).
5. Human expert reading of §§4–6 and Apps. B, D (REFEREE2 "what a human expert should still check") is still needed.
6. Intro length: §2 starts about 45% down p. 5; the introduction is just under 4 pages after the abstract.
7. Disc notation U(z₀, r) still shares the letter U with the matrix U (EDIT_REPORT N12); not renamed.
8. Length 81 pp (outline estimate 70–76 + 3–4 for Prop 8.6). §8 is about 9 pp (outline 5 + 3–4).

## 4. Sources to verify (citations)

- All 19 printed references are READ/OPENED in the repo's citation records (see papers/paper2/NOTES.md §4 and
  research/G1/RH/CITATIONS.md). No UNREAD key is cited (BGT, Vuil, Fischer, BueMar are uncited and do not print).
- DPQ: only the statement of Prop. 2.1 is recorded verbatim; used for attribution only.
- LL: printed as "Research announcement, 1999"; journal/book data not verified. Monien: arXiv only; publication status
  not verified. DD: volume and pages missing (bibtex warning). DLMF release date from pages fetched 2026-10-14.
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
