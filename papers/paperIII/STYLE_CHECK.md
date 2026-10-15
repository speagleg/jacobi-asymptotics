# Paper III — self-check against research/program/paper_style.md (2026-10-15)

Counts are over `main.tex` and `sec1.tex`–`sec8.tex` (case-insensitive for words), after the last edit.

## §1 Repo vocabulary
| Pattern | Count |
|---|---|
| "Law P", "Lemma CS", "QLP", "UF-lim", "Plan", "REVIEWED", "PROVED", "CONDITIONAL", "GAP", "Rule ", "engine", "seam", "x-frame", "G1", "G2" | 0 each |
| "RH" | 0 ("Riemann--Hilbert" written out, 2 occurrences, both in §1.1) |
| Files / scripts / repository | §7 opening (one sentence: "The scripts and their stored outputs are in the repository named in the data availability statement") and the data availability statement; Lean declaration names only in the data statement |

All results carry ordinary numbers (Definition 1.1 … Conjecture 8.4); hypotheses have descriptive names ("slowly varying",
"analytic of angle ϑ", "admissible window", the set S_p of (1.6)).

## §2 Prose, not lists
- No `itemize`; no `\textbf`; no bold in running text.
- `enumerate`: 6 environments (12 matches = begin/end), all for the parts (i)–(iii) of a theorem, lemma or corollary
  statement (Thms 1.3, 1.4, Lemmas 2.7, 2.11, 2.16, 3.2). None nested, none longer than 4 items.
- No "contributions" list, no "In summary", "Key idea", "Roadmap".
- `\emph`: 45 uses. They are definitions (*pointwise law*, *slowly varying*, *spectral weights*, *head margin*, *head*,
  *window*, *admissible*, *analytic of angle ϑ*) and run-in paragraph heads ("Averaged and pointwise laws.",
  "Step 1: …", "Reduction.", …). The run-in heads follow the convention of Papers I and II; the style guide reserves
  \emph for defined terms, so the author may prefer `\textit` via a macro or amsart `\subsubsection*` for these heads.
  **Open (cosmetic).**

## §3 Words and tics
| Word / phrase | Count |
|---|---|
| crucially, importantly, notably, key (adj.), leverage, robust, delve, novel, seamless, powerful, elegant, remarkably | 0 each |
| "it is worth noting", "note that", "we now turn to", "the upshot is", "in other words", "not only … but also" | 0 each |
| "indeed" | 1 (§2.6, before the proof of (2.12)) |
| "clearly", "obviously" | 0 |
| em-dash asides (`---`) | 0 |
| "we have not read" | 0 |

One novelty sentence: "We have not found Theorem 1.3 in the literature" (§1.2), backed by
research/program/novelty_lineB_C.md.

## §4 Structure
- Introduction: pp. 1–4 (≤ 4). Theorems 1.2, 1.3 on p. 2; Theorem 1.4 and Corollary 1.5 on p. 3, with all hypotheses
  explicit. Then context (§1.2, prose), method (§1.3, one paragraph), organisation and notation (§1.4).
- Every section opens with 2–4 sentences on what it proves and why. Proofs longer than about a page open with a
  strategy paragraph: Lemma 3.2 (before the proof), §4 opening (mechanism), Lemma 4.1 (before the proof), §6 opening.
- Remarks carry information for a referee: sharpness (2.17), order of steps (3.5), size of constants (4.5),
  ε²-accuracy (4.6), necessity of admissibility (4.7), scope of the a-construction (4.8), failure of convexity for
  truncations (8.2).
- Notation paragraph at the end of §1 lists the symbols local to III. Checked overloads: c only for c(p) (generic C,
  C′; c₁, c₂, c′ named constants); a, b only for a_n, b_n (window ends are τ₁, τ₂; interval ends in Lemma 2.21 are
  x̲, x̄); κ only κ_p; α not used; s, s′ exponents; n, N indices (N for scales in §4); γ_W, γ_a, γ_m (γ_m local to the
  proof of Lemma 2.16); T_p (arcsine tail) vs T_j (Chebyshev, §2.6 only) vs T′, T″ (Lemma 2.21) — the latter two are
  local; φ (direction) vs Φ_n vs ϕ_N, ϕ (local in Lemma 4.1); ϖ (Stirling ratio, Cor 5.5 only).
- Numerics: §7, two tables, method and precision stated, "illustrations; no proof uses them".

## §5 LaTeX hygiene
- amsart; packages amssymb, amsmath, amsthm, mathtools, booktabs, geometry, hyperref (booktabs and geometry as in
  Papers I and II). Macros: \N, \R, \diff, \usat, \Sp, \cE, \cJ, \Proj, \ia, \osc, \arc, \sgn, \dist, \Var, \tailbound —
  all used.
- No unicode in the .tex sources (grep for non-ASCII: none). \label/\ref/\eqref throughout.
- Build: pdflatex, bibtex, pdflatex ×2: no warnings, no overfull or underfull boxes, no undefined references.
- Bibliography amsplain; 11 entries, all cited.

## §6 Honesty and disclosure
- Imported results are restated with their numbers in §2.2 and named where used ("[II, Corollary 1.3]",
  "\tailbound"); §1 says which parts use which imports.
- Conjectures only in §8, labelled Conjecture.
- Acknowledgement sentence as required; author "Gordon Speagle"; data/code availability with tag v1.0-paper3 (Plan 73).

## §7 Cross-paper consistency
- σ_{p,s,ℓ}, x_k, w_k, p, s, ℓ, a_n, b_n (recurrence xP_n = P_{n+1} + a_nP_n + b_n²P_{n−1}), c(p), I(p), κ_p, D_n, h_n,
  arc_β, u_sat, u_n, l_n, m_n, K_n as in SERIES.md §4. Pairing a_n/(2b_n) throughout.
- Renames from the notebooks applied: μ_n → m_n, g_n/h_n^{ch} → u_n/l_n, F_n → Φ_n, Λ_n → Θ_n, F_p(M) → T_p(M),
  f → φ, I (a-kernel) → 𝔦, η_W → γ_W, c_W → ι_W, H → Υ.
