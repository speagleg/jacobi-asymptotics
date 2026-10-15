# Paper II — style self-check (2026-10-15, updated after the editor pass)

Checked against the local style guide (research/program/paper_style.md, §§1–7) by grep over all `papers/paperII/*.tex`
(printed text and source comments), plus a full build. This is a self-check, not an independent review.

## Build
pdflatex, bibtex, pdflatex ×2: 80 pp., 0 errors, 0 LaTeX/hyperref warnings, 0 undefined or multiply defined
references, 0 overfull and 0 underfull boxes (\raggedbottom added; the URL line no longer underfull). bibtex: 0 warnings
(DD now has volume and pages).

## §1 Repo vocabulary
Zero hits for: Plan, REVIEWED, PROVED, CONDITIONAL, GAP, G1, G2, Law P, Lemma CS/CT/LP/TL/QLP/EP, engine,
"Frame Proposition", x-frame, RH (as abbreviation), RH_, E_pgt1, SECOND, check_, Rule A/C/L/N/R/X, UF-lim, Sat_p,
"Paper 1/2/3" in prose (the only "Paper" strings are the bib keys \cite{Paper1}, \cite{Paper3}). The tail-bound
placeholder was replaced by the proved statement, so no placeholder string remains. Files and scripts are mentioned
only in §10 (one sentence pointing to the data statement) and in the data/code availability statement. No absolute
local paths in any tracked file of the folder.

## §2 Prose, not lists
- No \textbf anywhere in the body; \emph used for defined terms and italic run-in step headings in proofs.
- No list inside any proof. 29 enumerate/itemize environments (the two-item hypothesis list of Prop 8.6 is now inline), all parts of lemma/proposition/definition statements or
  the list of contour arcs in §4. Three exceed five items, all parallel statement parts: Lemma 4.x "Jumps of V"
  (7 parts, one per arc), Lemma 5.x Szegő estimates (6 parts), Proposition 5.6 (8 items, the interface used by §§6–9).
  Left as is; splitting them would make cross-references worse.
- No "Contributions", "In summary", "Key idea", "Roadmap" (the old roadmap label in §4 became prose).

## §3 Words
- Banned words (crucially, importantly, notably, key, leverage, robust, delve, novel, seamless, powerful, elegant,
  remarkably, "it is worth noting", "we now turn to", "the upshot", "in summary", "in other words", clearly, obviously,
  "not only"): 0 hits. ("contributions" occurs once in §9 in the mathematical sense "contributions of 𝖱₁ and 𝖱₂".)
- "note that": 0 occurrences (the two in §6, §9 were rephrased in the editor pass).
- "indeed": 2 occurrences in 80 pp. (App. C, App. D), each introducing a one-line verification.
- Em-dashes (---): 0.
- Hedging: Paper 2's "within the literature we have read" replaced by "to our knowledge" with the Dai–Yao citation.

## §4 Structure
- Introduction: Definition 1.1, Theorem 1.2, Corollary 1.3 and Theorem 1.4 all on p. 2 with hypotheses explicit;
  §1.2 opens with the relation to Papers I and III and a paragraph naming the two difficulties (accumulation of nodes at
  the hard edge; non-analytic r_n), which the prior-work paragraphs then answer; method in one paragraph (§1.3);
  organisation with reading paths for Thm 1.2 alone and Thm 1.4 alone (§1.4). The Lommel derivation left the
  introduction (now in Rem 9.6). §2 starts on p. 5; the introduction is under 4 pages after the title block.
- Every section opens with sentences on what it proves and why (re-read in the editor pass; the openers of §§5, 7, 8,
  9 and Apps. B, D, F were rewritten so that they do not all start "This section proves"). Strategy sentences for long
  proofs were added in the drafting pass (reported for the seam lemma of App. A, Prop B.4, the proof in App. D, the
  Szegő lemma, and §§6, 8, 9); they were not re-verified proof by proof in integration.
- Remarks: 1.5 (scope at order 1/n), 1.6 (the case (2,2)), 2.2, 3.6 (sharpness), 4.8 (angles), 6.7 (where |α| < 1 is
  used), 6.8 (circle terms), 7.2 (base window), 8.5 (p = 1), 9.6 (hard edge at order 1/n; derivation of the (2,2)
  closed form), C.3; each carries information a referee needs. The (2,2) check is stated once (Rem 1.6), derived once
  (Rem 9.6) and cited once in §10.
- Numerics short (§10, ~3 pp. because of two floating tables); conjectures only in §11.

## §5 LaTeX hygiene
- amsart; packages amsmath, amssymb, amsthm, mathtools, booktabs, tikz (one contour figure), geometry, hyperref.
  booktabs/tikz/geometry go slightly beyond the guide's list; kept for the two tables and Figure 4.1.
- All macros in main.tex (20 \newcommand, 6 \DeclareMathOperator), each used; no \providecommand in section files.
- Label scheme type:name throughout; the legacy A-/B- prefixes of Apps. B–D were renamed after their appendices,
  rem:not-proved → rem:circle-terms, thm:UR-true → prop:UR-true (intermediate results are Propositions; Theorems are
  1.2, 1.4, 3.1, 7.1 only). Theorem-environment titles in one style.
- \label/\ref/\eqref throughout; the only hard-coded numbers are external ones inside or next to \cite
  (e.g. \cite[Theorem~4.4]{CD}) and the PDF-string fallbacks of \texorpdfstring titles.
- Equations, tables and figures numbered within sections; one theorem counter per section.
- Bibliography amsplain; 19 entries printed, all cited; arXiv-only entries carry a year field and the arXiv id in the
  note; journal abbreviations consistent.

## §6 Honesty and disclosure
- Theorem 1.2 / 1.4: the external inputs are named in a paragraph right after Theorem 1.4 (WLXZ as pattern, KMVV §6,
  CD Thm 4.4/4.7/Prop 4.6/4.9, DLMF; KMVV (6.42)–(6.53) and DLMF §§9.7, 10.17, 10.40 for Thm 1.4) and the exact
  symbolic computation of the Laurent coefficients is disclosed there and in App. E. Theorem 7.1, Prop 8.4, 8.6, 9.5
  carry their own inputs next to the statements.
- Conjectures 11.1 (1/n term, p ≤ 1) and 11.2 (tilt law) are labelled as such and placed in §11.
- Acknowledgements: one plain sentence as required; author line "Gordon [Surname]".
- Data/code availability: github.com/speagleg/jacobi-asymptotics, tag placeholder; Lean declarations named there only.

## §7 Cross-paper consistency
- "Recurrence coefficients" is the only term for a_n, b_n (was mixed with "Jacobi coefficients"). The disc is
  𝔻(z₀, r) (was U(z₀, r), clashing with the matrix U); C_± defined in §2. Paper I and Paper III are "the first/third
  paper of the series" on first mention, not both "the companion paper". \wn used for 𝗐_n everywhere.
- Notation per SERIES.md §4: σ_{p,s,ℓ}, x_k, w_k, p, s, ℓ, a_n, b_n (xP_n = P_{n+1} + a_nP_n + b_n²P_{n−1}), c(p),
  I(p), D_n, h_n, λ_p, arc_β, 𝓑_y, α = (s−1−p)/p, u_n, l_n, m_n(k). Pairing a_n/(2b_n) with 1/n coefficient −p/2
  stated after Theorem 1.4 and in §2.1 only (the repetitions in §§7, 9, 11 were removed); the other pairing never appears. κ not used.
- Imports from Paper I cited with numbers (Cor 1.2, Thm 1.3(i)–(ii), Cor 1.4, Thm 1.1 for the atom constant),
  checked against papers/paper1/main.tex. Paper III cited as forthcoming for general slowly varying/rough weights and
  for the averaged p = 1 statement. The §2.1 footnote on Paper I's former a_{k+1} indexing is deleted (Paper I now uses
  a_k).

## Update 2026-10-15 (referee fixes; Theorem 1.4 for every p > 0; 105 pp.)
Build: pdflatex, bibtex, pdflatex ×2: 105 pp., 0 errors, 0 LaTeX/hyperref/bibtex warnings, 0 undefined references,
0 overfull/underfull boxes. Grep over the new and changed files (sec1, sec10_plt1, sec11_pone, sec12, sec13, appG, appH):
0 hits for the banned words, "---", \textbf, "Plan", "REVIEW", "Route", "x-frame", "RH", E_p1/E_plt1, κ; "note that" 0,
"indeed" 0 in the new files. κ_p is not used (𝗄_p instead; Papers I/III reserve κ_p). New sections open with purpose
paragraphs (§10: why §§8–9 do not apply verbatim; §11: why neither hard-edge construction gives the 1/n term at p = 1);
the long proofs of §11/App. H open with the plan of the appendix. Lists only in statements. New external inputs are
recorded in §2 (2.4: the parts of WLXZ applied at p = 1; 2.5(d): the Fisher–Hartwig model of KV/Vanlessen; 2.7: DLMF
5.2.1, 25.2.1, 25.4.1, 10.32.4, 10.32.9; KMVV (6.19)–(6.21) in 2.5(a)), and the dependence of Thm 1.4 at p = 1 on the
analysis of WLXZ is stated after Thm 1.4 and after Prop 11.9. Deviation: the introduction is now about 5 pages (guide
≤ 4) because Theorem 1.4 has two parts and Remark 1.7 was added; trimming left to the author.

## Update 2026-10-15 (referee report 2 fixes; editor pass)
Build: pdflatex, bibtex, pdflatex ×2: 105 pp., 0 errors, 0 LaTeX/hyperref/bibtex warnings, 0 undefined references,
0 overfull/underfull boxes. Paper III rebuilt with the amended Conjecture 8.3: 29 pp., same counts.
- Introduction: 3.9 pages from the heading on p. 1 to "2. Preliminaries" on p. 5 (PDF bounding boxes), within the guide's
  ≤ 4. Main statements (Def 1.1, Thm 1.2, Cor 1.3, Thm 1.4) unchanged and on pp. 2–3; context in prose with the two
  difficulties first; method in two paragraphs; organisation in five sentences. The deviation recorded in the previous
  update is removed.
- Voice: section openers of §§10–13 and Apps. G–H re-read against §§3–9 (each opens with what it proves and why; no
  "This section proves" run). The new text (§13 paragraph after Conj 13.2, Lemma 10.4 parenthesis, Prop 11.5 proof
  sentence, §2.5(d) addition, intro rewrite) was grepped: 0 banned words, 0 "---", 0 \textbf, 0 repo vocabulary
  (Plan, Rule, REVIEWED, PROVED-mod-cite, UF-lim, RH_p, x-frame, engine), "note that" 0, "indeed" 2 (App. C, D as
  before). The only "crucial" is inside the verbatim quotation of Deift–Piorkowski.
- Notation: App. H clashes removed (𝖫(z), δ_m, Ω_b, sector index S in X_S, Y_S).
- Open deviation (author's decision): the word "seam(s)" (104 printed occurrences, §§4–5, 8, 10, Apps. A, G) is the
  paper's defined name for the two rays across which the weight is glued (Appendix A). The guide lists "seam" among repo
  vocabulary; it is kept because it is defined in the text and a global rename would touch every proof of §10 and
  App. A. A replacement such as "gluing ray" can be done mechanically if wanted.
- Log check corrected: main.log of Paper II is ISO-8859 (non-UTF-8 bytes), so a plain `grep` treats it as binary and
  prints nothing; the earlier "0 overfull/underfull" counts were false negatives. With `grep -a` the 105-p. build had
  12 overfull boxes (§11: Lemma 11.3, Lemma 11.8 display, Lemma 11.10(a), Prop 11.12 display, its proof, proof of Thm
  11.13; App. H: §H.1 opening (2), proof of Lemma H.2, "Three smooth factors", "The circle at 2"), 1 underfull box
  (caption of Table 12.3) and 1 hyperref warning (PDF string of §12.3 title). All fixed by moving long inline formulas
  into displays or rewording, with no change of content; now `grep -a` finds 0 warnings and 0 overfull/underfull boxes.
  Paper III's log is ASCII and was clean.
