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
