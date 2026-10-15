# Cross-paper consistency pass (Plan 73, 2026-10-15)

Scope: `papers/paper1` (I), `papers/paperII` (II), `papers/paperIII` (III). `papers/paper2` (the superseded combined
draft) was not touched. No mathematical statement was changed in content or strength.

## Checked

- Notation against SERIES.md §4: σ, x_k, w_k, p, s, ℓ, a_n, b_n with xP_n = P_{n+1} + a_nP_n + b_n²P_{n−1}, c(p), I(p),
  κ_p = 3p/2 + log c(p) (I and III), 𝗄_p = 2p c(p) ζ(−p) (II), D_n, h_n, pairing a_n/(2b_n). No σ_p, ω_β, u_s,
  a_{k+1} or κ-overloading left.
- Cross-references against the current aux files: III → I (Thm 1.1, Cor 1.2, Thm 1.3(i), Cor 1.4); III → II (Def 1.1,
  Thm 1.2, Cor 1.3, Thm 1.4, Rem 1.6, Thm 3.1, Lemmas 3.2–3.5, Rem 3.6, Prop 8.6, Conj 13.2, §13); II → I (Cor 1.2,
  Thm 1.3, Cor 1.4). Each restatement in III §2.2 compared with the original (hypotheses, constants).
- Bib titles of I, II, III equal the papers' \title. Shared entries (Monien, Haynes–Zudilin, WLXZ, DD, DPQ, VA, DLMF,
  Fischer) identical across the refs.bib files that contain them.
- Abstracts against the main theorems; plain-text length I 1226, II 1881, III 1600 characters (limit 1920).
- Style sweep (banned words, repo vocabulary, bold, em-dashes, lists). "seam" kept in II (user decision pending).
- Builds: 0 overfull/underfull boxes, 0 undefined references, 0 rerun requests, 0 BibTeX warnings (grep -a).
  Pages: I 19, II 105, III 29.

## Changed

- Author "Gordon Speagle" in all three \author lines and the II/III bib entries for the companion papers; \date{October
  2026} in all three; ARXIV.md, NOTES.md, STYLE_CHECK.md updated.
- Data and code availability: tag stated plainly (v1.0-paper1, v1.0-paper2, v1.0-paper3), same sentence pattern in all
  three; acknowledgement sentence in the same one-sentence form in all three (\section* headings throughout).
- III: Theorem 2.6 now restates II Theorem 1.4 in full (p ≥ 1 and 0 < p < 1 with 𝗄_p, and the a_n/(2b_n) consequence).
  Stale sentences saying the pointwise 1/n term is known only for p > 1 (§1.1, §5 before and after Prop 5.6, §8) now
  say that II proves it for every p > 0; the abstract says the p = 1 averaged coefficient is recovered by soft methods.
  §8 used 2p c(p)ζ(−p) where II writes 𝗄_p; now 𝗄_p. §8 said "three conjectures" (there are two). Prop 2.10 uses
  γ_* as in II Prop 8.6. "[II, Section 3]" for the O(n^{-1/2}) chain rate is now "[II, Lemma 3.5 and Remark 3.6]".
  Re/Im typeset as in II. One sentence on the a_n/(2b_n) pairing added to the notation paragraph. The placeholder
  comment on Prop 8.6 numbering removed.
- II: the bare symbol 𝗄 (a constant in App. D, a scalar function in App. F) renamed 𝗊, so 𝗄 means only 𝗄_p.
- Bibliographies: II's Vanlessen entry printed "to verify" for pages; now J. Approx. Theory 125 (2003), no. 2,
  198–237 (Crossref). II's Fischer stub replaced by III's full entry (not cited in II). arXiv versions as recorded
  in the citation notes (Monien v1, DPQ v1, DD v2).

## Not resolved

- None blocking. `papers/paper2/` (superseded draft) still carries "Gordon [surname] (draft)"; it is not submitted.
