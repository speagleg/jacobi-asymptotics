# Paper 2 — notes (draft of 2026-10-14)

Files: `main.tex` (shared preamble), `sec_front.tex` (chunk A: title, abstract, §1), `sec_2.tex`–`sec_8.tex`,
`app_*.tex` (chunks B–D), `sec_back.tex` (chunk A: §§9–10), `refs.bib` (chunk A), `checks/`.
Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main`. Author line is a placeholder ("Gordon [surname]
(draft)"). The binding contract is `OUTLINE.md`. This file records departures from it, sources, the citation gate and
the pre-submission checklist. Other chunks should append their own sections below.

---

## 0. Revision log (2026-10-14, after EDIT_REPORT.md and REFEREE_REPORT.md)

Numbering after the revision: **Theorem 1** (main; parts (i) law, (ii) analytic ℓ with rate O(1/n)); the old part (ii)
is now the display **(eq:main-rate)** in a "Quantitative form" paragraph; **Corollary 1.6** (pure powers; label kept as
`thm:pure`, environment `corollary`); **Theorem 2** (Christoffel shift, `thm:shift`); **Theorem 3** (RH engine,
`thm:engine`). All labels thm:main, thm:shift, thm:engine unchanged. `rem:engine-scope` is now a second label on
`rem:main-rate` (merged). New labels: `eq:main-rate`. Removed: `rem:main-unbounded` (merged into `rem:main-finite`),
`sec:p1-routes` is now a second label on `sec:nodes` (§10.3). `def:regular` is a phantom label in §2.3 (the definition
is in §1.2 only). Section order in §1: 1.1 Setting, 1.2 Results, 1.3 Strategy, 1.4 Context, 1.5 Organisation.
Convention: "Section~\ref" for sections, "\S\ref" for subsections. App. D (empty) deleted and its \input removed.

### Front half and back matter (sec_front, sec_2–sec_4, sec_back, main.tex, refs.bib, NOTES; this agent)

| Finding | Action |
|---|---|
| EDIT S9 (Thm 1 on p. 2) | Thm 1 now on p. 2: Defs 1.1 (slow variation), 1.2 (A_ϑ), then Thm 1 (i), (ii). Rate + ρ_ℓ + M₀ moved to "Quantitative form" (Def. 1.3, eq:main-rate). One-sentence answer added to §1.1 ¶1. Averaged law / Tauberian discussion moved after Thm 1 ("Why the pointwise law is subtle"). |
| EDIT S10 (Thm 2 → corollary) | Corollary 1.6 (pure powers), explicit c(1), c(2) values kept; Remarks Lommel, zeta, origin of c(p) attached. All references updated (sec_4 Step 3, §9, §10, Figure 1). |
| EDIT §1 "how by p. 5" | Strategy (§1.3) moved before Context (§1.4); the hard edge paragraph is on p. 5. |
| EDIT S6 (hard-edge story once) | §1.3 "The hard edge": one paragraph (editor's draft). "What is new relative to C–D" merged into the C–D paragraph of §1.4 Context. Sec_7's verbatim repeat is the RH agent's to delete. |
| EDIT Fig. 1 | "Paper 1" box → "Equilibrium measure μ* [Paper1]"; Corollary placed directly under the analytic box; labels Thm 1(ii), Thm 1(i)+(eq:main-rate). |
| EDIT §3.3 "Paper 1" in text | Removed everywhere in my files; footnote in §2.1 now "The companion paper [15] writes …". (sec_5.tex lines 29, 153 still say "Paper~1": RH agent.) |
| EDIT S7 restatements | Removed: slow-variation display in §2.2; smoothing/(A_ϑ) recap in §4.1; Paper-1 indexing in §1.1 (footnote kept); "no uniqueness of Y" in T1(a); Thm 3 restatement in §3 (one sentence); Thm 4 restatement in §4.4; Rem 1.13 merged into Rem 1.5; regular-rate definition kept only in §1.2; Potter remark now cites §2.2; DP quoted once (§1.4). |
| EDIT S12 / referee: Tools | Quotations replaced by precise statements with hypotheses and equation numbers (T1–T3); T3(b) stated exactly in L^r, r′ notation; T4 compressed; opening sentence says §2.5 can be skipped until Section 5. Saving ≈ 0.5 p only: moving the T1(a) proof into Lemma 5.1 and the Mellin items into App. A (editor's other proposals) need the RH agent's files. |
| Referee F4 | One-line remark added to T3(b): C–D (4.14) is printed without v_B^{−1}; agrees when (v_A − v_B)v_B^{−1} = v_A − v_B; we use the consequence of Thm 4.4. |
| Referee F5 | DPQ, DD, DP (§1 + abstract), DY (re-read from the arXiv PDF), VA §3 and DLMF (10.2.2, 10.6.1, 10.16.1, 4.22.3) entries appended to research/G1/RH/CITATIONS.md. |
| EDIT L6 (Lommel hedge) | Mass identification **verified** (resolvent of the Lommel Jacobi matrix = −2ν J_ν(1/x)/J_{ν−1}(1/x) via the ℓ² minimal solution; ν = 3/2 gives masses 3/(πk)² at ±1/(πk) by Euler's partial fractions; image under t ↦ π²t² is (6/π²)σ_{2,2}). Proof sketch now in Remark rem:pure-lommel; checked numerically (mpmath). Hedge removed in §1 and §10.1. |
| EDIT S8 / item 10 | §10.2 (other routes at p = 1) compressed to two sentences + pointer to Remark rem:quotient-p1, merged into §10.3 "Other nodes, other frames, larger Bessel orders". Zeta-zero paragraph of §10.4 dropped entirely (with the "work in preparation" sentence and the coordinator comment). −p/2 convention stated explicitly before Conjecture 10.1 (pairing a_n/(2b_n) vs a_n/(2b_{n+1})). §9 "How computed" split in two paragraphs (L16); Table 2 column heads use ℓ, defined in the caption. |
| EDIT L7, L8 (Rem 3.5, 3.6) | Expansion of ℓ̂_n written out with the n^{−1/2} cancellation (re-derived); converse remark gets the "common image xσ" clause. |
| EDIT L12, L15, L18 | Lemma 4.1(ii) stated in words; Lemma 2.1 "j dyadic steps and one final step"; (A_ϑ) "in words" now says {|t| ≥ e^{−c₀}, |arg t| ≤ ϑ_p}. |
| EDIT §3.2 "Λ satisfies (A_ϑ)" | Def. 1.2 now says "we then also say that Λ satisfies (A_ϑ)". |
| EDIT N-list (my files) | Π (Lemma 4.3 product) → 𝒫; c_p := min(1, p) → ς_p; ω(T), ω*(T) (§4) → Ω_L(T), Ω_L*(T); arcsine law ω_β → arc_β; first-variation direction f → h, coefficients ϖ_j → 𝖼_j, generic ⟨f, g⟩ → ⟨h₁, h₂⟩; g_p(θ) → g_p(y), θ₁ → y₁; Euler's γ → γ_E; T3 integrand H → 𝓔; T3 exponents p, q → r, r′; Christoffel coefficients c_j removed; rough perturbation f(k) → ε_k (§1.4, §10.2); nodes "f(k)" in §10.3 removed; T4 large-argument series named 𝗌_±. |
| Hygiene | All `% src:` comments and repo codenames removed from my files and main.tex; TODO gates: Dai–Yao resolved (re-read), C–D (5.5) resolved (equation recorded in RH/CITATIONS.md (C–D)), Gragg–Harrod: the algorithm is now described ("adds one atom at a time and restores tridiagonal form by plane rotations") without a citation. Hyperref: \texorpdfstring on the §4.3/§4.4 titles; no "Token not allowed" warnings from my files. Overfull boxes in my files: none. refs.bib: titles of DY, DP, Tro, MM and journal data of KMVV, KV, VA, DD (doi) filled from the arXiv API. |
| Prop. 2.5(iii) (EDIT S14) | **Kept**: RH agent should cite it in the proof of Lemma 5.4(iii), or tell the coordinator to delete it. |

### RH half (other agent)

(placeholder: sec_5–sec_8, app_a–app_c and any new appendices)

### Revision 2 — consistency pass (2026-10-15, final copy/consistency editor; 67 pp, was 69)

Build: pdflatex, bibtex, pdflatex ×2 — 0 errors, 0 undefined references, 0 overfull boxes, 0 LaTeX/hyperref warnings.

**Cross-half notation (one symbol, one meaning).**

| Old | New | Where |
|---|---|---|
| ϱ_n (regular-majorant input, Rem. 2.3) | υ_n | sec_2; ϱ_± = e^{∓iπα} kept in §7/App. D |
| ε_n := sup_{m≥n} osc_m(2) | osc*_n | sec_2 (Lemma 2.1, Rem. 2.2) — clashed with ε'_n, ε, ε_Λ |
| N (index in Lemma 2.1(ii)) | m | sec_2 ("no N" rule) |
| Ω_L(T), Ω_L*(T) (local oscillation) | osc_L(T), osc_L*(T) | sec_4 — Ω now only for RH regions Ω_b, Ω^△, Ω_∞ |
| 𝓗_n (head set) | written out as "k < n/M₀" (no symbol) | sec_4 — removes clash with H°_n |
| W := Σ w_k, W^{(τ)}, W_ℓ (§4) | ‖w‖₁, ‖w^{(τ)}‖₁, σ_{p,s,ℓ}(ℝ) | sec_4 — W is the RH residue weight |
| 𝖺_n, 𝗆_n (chain sequence, §3) | 𝗋_n, 𝗀_n | sec_3 — 𝖺, 𝖻 are the extraction functionals of §5 |
| β_τ, arc_β | defined once in §2.4 (μ* = ∫₀¹ arc_{β_τ} dτ); §5.4 now cites Prop. 2.4 instead of restating it | sec_2, sec_5 |
| Θ, Θ₀, Θ₁ (numbers), M (constant) in Lemma 6.3 | 𝔠, 𝔠₀, 𝔠₁, 𝔐 | sec_6, sec_7 — Θ₀, Θ_∞ are matrices, M the KMVV matrix |
| ξ = ⅔ζ^{3/2} in the Airy proof | written out | sec_6 — ξ is the log variable |
| δ (DLMF sector constant in T4) | "uniformly in closed subsectors" | sec_2 — δ is the disc radius |
| τ (Lemma A.3) | τ₀ | app_outer — τ is the path parameter of §4 |
| 𝔥 (density in Prop. 7.6) | 𝓔 (the same object as in T3(b)) | sec_7 — 𝔥_n is the head mass |
| Ω (Cauchy–Pompeiu term, Lemma B.1) | 𝔓 | app (now in App. B) |
| γ_E | defined once (T4); repeat in Lemma 7.1 removed | sec_2, sec_7 |
| ε₀ (rough-weights announcement) | ε_* | sec_front — ε₀ is the soft-edge radius of Lemma 5.5 |

Checked and left as is: κ_n (§3) vs κ_± (§5) vs ϰ_∞ (Lemma 6.4) — distinct glyphs/subscripts, each defined once; 𝗄₀
(Lemma 7.1, used in (7.x) and App. D (B3) as 𝗄); ι_± (Lemma 5.9, restated in (F1)); 𝓘 is the only incomplete-beta
symbol; N_n only in (O5); m_n only spectral weights; Υ defined once (Lemma 6.3(i)); J is the Jacobi matrix in §§2–3 and
the band jump in §§6–7 (separate halves, each defined). A "Notation used throughout" paragraph was added to §2's opening.

**Tools (§2.5).** T1 intro and T1(c) shrunk to an attribution (§6 builds its own Airy parametrix). T4: added DLMF
9.2.8, 9.2.12, 9.7.2, 9.7.5–9.7.6 (statements as in RH/CITATIONS.md "(DLMF-9, Paper 2)", written with relative errors
O(|z|^{−3/2}), the only consequence used); §6 now cites T4 instead of quoting DLMF inline. Removed from T4 as unused:
Mellin items (1.14.32, 1.14.38–40; the parenthetical in App. C that used them was dropped — Minkowski's inequality is
the proof), 10.27.3, and 5.12.1 as a separate item (Beta function now named in §2.4; 5.12.1 kept next to 5.12.3,
which Rem. C.3 cites via T4). T2(a) shortened; T2(c) now explains N, W̃, f̃ (KMVV notation). The DLMF numbers in the
Lommel remark (4.22.3, 10.2.2, 10.6.1, 10.16.1) are cited directly: that remark is not proof input.

**Duplication cut (no mathematics removed).** Intro: "Averaged versus pointwise" merged into "Why the pointwise law is
subtle" (moved directly after Thm 1); "Special cases" shortened; C–D novelty sentence de-duplicated; Lommel 90-digit
check moved to §9. §3: restatement of Thm 2, the Cholesky aside and the iteration paragraph (repeated in §4.4) cut.
§4: "order of the steps" shortened. §5: repeated standing data (ϑ_p, "c reserved"), restatement of μ*, the p-dependence
of g − log z (Table row also dropped; unused) cut. §6: intro shortened; Rem. 6.2 shortened; numerical airy_check
sentence removed from the text (numerics only in §9); Rem. "what depends on the geometry" removed (Table 1 says it);
(F1) now states the band and lip jumps and "v_V with W₀ replaced by ω^{−1}" for the other arcs (checked entry by
entry). §7: intro shortened (repeated hard-edge story), organisation paragraph removed, resolvent proof sketch halved,
Rem. 7.7 shortened and pointed to Rem. 1.5. §8: Rem. "Why c(p)" folded into one paragraph after the proof (corrected:
"constant Jacobi matrix with diagonal 2c, off-diagonal c, spectrum [0, 4c]" instead of "Jacobi matrix of the arcsine law").
§9 rewritten more compactly. Organisation (§1.5) now lists the appendices A–D in their final order.

**Hygiene.** No repo jargon or codename comments (grep clean). "Section~\ref" for sections and "\S\ref" for
subsections throughout (three fixes). RH defined at first use (§1.3). Stale "Corollary 1.4" comments → 1.6.

**Second referee (REFEREE2_REPORT.md), minor findings applied.** G1: (O3)/(O4) now on |z| ≤ 1 / |z| ≥ 1 (η₀ removed).
G2: ε < c·sin ϑ_w added to the parameter list, with the reason (U(4c, 4ε) ⊂ Z_n). G3: Lemma 5.6 — first piece is the
preimage in U(0, 2δ) (δ₁ ≤ r_*/4), corner rounded in {δ < |z| < 2δ} so (a) holds; r_* < δ₀ strictly; arc condition
arcsin(h₀/4c) < ϑ_w. G4: .gitignore now ignores only main.out, so checks/*.out are tracked; airy_check scope recorded
in RH/CITATIONS.md (DLMF-9 entry): it tests jumps, det, MJM⁻¹, band cancellation and O(1/n) matching, but sets φ̃ and ω
structurally, so it does not test Lemma 5.5(iv) or Lemma 6.3(vi)(b). The sentence about it was removed from §6.
G5: Rem. 7.8 now says "in an essential way" and lists the two harmless uses (App. D vertex conditions need |α| < 2;
Δ₃ bound in Prop. 7.6). G6: comments fixed; the "Three facts about Cauchy integrals" subsection moved from App. D to
App. B (§B.1, labels unchanged), so Cor. B.5 now refers backwards. G7: abstract says "extends to a slowly varying
analytic function on a sector". G8: WLXZ Fig. 3 region layout (v1 PDF, text layer) recorded in RH/CITATIONS.md.
Note for readers of REFEREE_REPORT.md: its appendix letters are pre-revision.

**Open after this pass.**
1. Length: 67 pp against the 58–60 target. The remaining length is mathematics (proofs in §§5–7 and the appendices);
   reaching 60 would need cutting or relocating proofs (e.g. Rem. 3.6's converse proof, Prop. 2.4(iii), the Lommel
   derivation) or a tighter layout — author's decision.
2. Observation for the author/referee (not changed): Lemma 5.7 keeps all weight evaluations in |Im ξ| ≤ ϑ_w/p with
   ϑ_w/p < π/2 also for p > 1, so for 1 < p < 2 the hypothesis ϑ_p = π/p seems stronger than the proof needs.
3. Bibliography: printed entries still carrying "to verify" (DLMF release, LL publication data; Van pages are unprinted
   since Van is uncited). refs.bib keeps uncited entries KV, Van, BD, BueMar, BGT, Vuil, Fischer (not printed).
4. Author line, MSC codes, supplementary-material URL (§9).

---

## 1. Front matter (chunk A): claim → source (numbering updated)

| Paper | Statement | Repo source | Repo label |
|---|---|---|---|
| Thm 1 (`thm:main`) | main theorem, statement verbatim from OUTLINE §2 | PROOF.md §3.21 B_all, §3.20 B_{p<1}, §3.23 B_{p=1}^{all} (+§3.19), rate re-ordered (OUTLINE §0 item 5) | PROVED-mod-cite, REVIEWED |
| Cor. 1.6 (`thm:pure`, formerly Thm 2) | pure powers, O(1/n) | THEOREMS.md H2; in the paper Thm 4 at Λ ≡ 0 + Thm 3 | PROVED-mod-cite, REVIEWED |
| Thm 2 (`thm:shift`, formerly Thm 3) | Christoffel shift with rate | PROOF.md §3.21 SH, SH-r; ROUTE2_alpha §§2–4 | PROVED, REVIEWED |
| Thm 3 (`thm:engine`, formerly Thm 4) | RH engine, base window | ROUTE2 §4.4 RII; ROUTE2_xframe1 §4 RII_x1; ROUTE2_plt1 §4.3 RII_{<1} | PROVED-mod-cite, REVIEWED |
| Def. `def:sv`, `def:smoothing`, `def:A` | slow variation (sequence form), ρ_ℓ, (A_ϑ) with ϑ_p | PROOF.md §3.14; ROUTE2 §1; (H_an), (H_an^{x1}), (H_an^{<1}) | — |
| §1.2 "(A_ϑ) ⇒ slowly varying" | one-line mean-value bound | written here | elementary |
| Rem `rem:pure-lommel` | closed form for σ_{2,2}: b_n = π²/((4n+1)√((4n−1)(4n+3))), a_n = 2π²/((4n+1)(4n+5)), n ≥ 1 | derived here from the Lommel recurrence quoted in novelty_G1RH §1.3 (Van Assche math/9510214 §3) by the quadratic transformation; checked in `checks/lommel_check.py` (90+ digits, n ≤ 9) and against Table 2 (p = 2, ℓ ≡ 1: all 4 digits, n ≤ 800) | mass identification now proved in the remark (resolvent/minimal solution + DLMF 4.22.3); numerical check kept; derivation not independently reviewed |
| Rem `rem:shift-credit`, `rem:shift-converse` | credit DD §1, DPQ Prop. 2.1; rate part not found | novelty_lineB_A.md §§1–4 | — |
| §1.3 Context | positioning | novelty_lineB_A/B, novelty_G1RH, RESEARCH_PROGRAM §§1, 6; wording of OUTLINE §6.6 | — |
| §1.3 "log D_n changes by ≤ εn" | from Heine's formula (each term changes by a factor in [e^{−nε}, e^{nε}]) | Paper 1 Lemma 2.1 | elementary |
| §1.3 Paper 3 announcement | as OUTLINE §2 (no constants; not "the same weights") | THEOREMS.md H4 Theorem R, §2.6 Theorem Ra | PROVED-mod-cite, REVIEWED |
| §1.4 strategy | prose | ROUTE2 §2 (last paragraph), §3; OUTLINE §5 §1.4 | — |
| §9 Table (`tab:numerics`) | numerics | `checks/table2.py` → `checks/table2.out` (this chunk) | NUMERICAL |
| §10.1 Conjecture (`conj:tilt`) | 1/n term | ROUTE2 §5; xframe §5; ROUTE2_plt1 §6; RH_px §0 (pure power, translated, see §2 item 1 below) | CONJECTURE + NUMERICAL |
| §10.3 (last ¶) | other routes at p = 1 (two sentences) | ROUTE2_p1; xframe §0; PROOF.md §3.22 (REVIEW_Plan53 F1–F2); RH_px §4.1; RH_plt1b §2; xframe Lemma X2 | — |
| §10.3 | other nodes, α ≥ 1 (zeta-zero paragraph dropped) | PROOF.md §4; ROUTE2 §6; outline_A_nodes.md §1 item 5 (not cited) | — |

## 2. Departures from OUTLINE.md (chunk A) and why

1. **Sign of the 1/n coefficient of a_n/(2b_n).** OUTLINE §2 (remarks after Thm 2), §9 (Table 2, last column) and
   §10.1 say the pure-power coefficient is **+p/2**. That value is for the toolkit pairing a[n]/(2√b2[n]), which in the
   paper's convention (§2: xP_n = P_{n+1} + a_nP_n + b_n²P_{n−1}, b_n² = h_n/h_{n−1}) is **a_n/(2b_{n+1})** (see the
   docstrings of research/G1/RH/route2/checks/check_r2_coeff.py and check_r2p_coeff.py, and `jacobi_asym.jacobi.result`:
   a[i] = diagonal at P_i, b2[i] = h_{i+1}/h_i). In the paper's convention, n(a_n/(2b_n) − 1) → **−p/2** (since
   b_{n+1}/b_n = 1 − p/n + O(n^{−2})). Confirmed: Table 2 (recomputed) and the exact (2, 2) closed form
   (a_n/(2b_n) = 1 − 1/n + O(n^{−2})). §9 and Conjecture 10.1 use −p/2. **Chunks B–D: if any remark quotes the 1/n
   coefficient of a_n/(2b_n), use −p/2.** (Remark 3.7's "shift by −p/2" concerns the b-coefficient −(s − 1)/2 and is
   consistent: −(s + p − 1)/2 = −(s − 1)/2 − p/2.)
2. **Table 2 recomputed** (`checks/table2.py`), all three rows, in the paper's convention, each n separately, with
   both ℓ and ℓ ≡ 1 in both column pairs. The p = 2 row now uses the continuous-tail model too (the repo's
   check_r2_coeff had no tail and was not K-converged at n = 800, REVIEW_Plan48 F8); with the tail all entries are
   stable to 2·10⁻¹¹. Where both exist and are converged, the b-columns agree with check_r2p_coeff.out,
   check_x1_coeff.out ("Psi A") and check_r2_coeff.out to all printed digits (p = 2: to ≤ 10⁻³ at n = 400, where the
   old run was not converged).
3. **Lommel remark** gives an explicit closed form (OUTLINE asked for "quote the explicit formula from a source that has
   been read"). No read source states the formula for σ_{2,2}; it is derived from the read Lommel recurrence (Van Assche
   §3, via novelty_G1RH §1.3) and checked numerically. The text says so and says the mass identification was not
   checked against a source.
4. **Monien's O(n^{−2}) remark dropped.** OUTLINE §2 suggested "the Monien–Zagier expansion implies O(n^{−2})
   numerically". This depends on the indexing of Monien's H_n (Table 2 shows n(nb_n/c − 1) → −½ in our indexing at
   p = 1, s = 2, i.e. b_n ≈ 1/(2n + 1), so the statement is only true after an index shift). Replaced by a neutral
   sentence: Monien reports a full expansion found numerically by Zagier, which goes beyond Thm 2 and is unproved.
5. **Karamata remark dropped** (BGT unread; OUTLINE §2 citation gate).
6. **Freud-type framing omitted** (Lubinsky–Mhaskar–Saff unread). Levin–Lubinsky is cited from the 1999 announcement
   that was opened.
7. **Dai–Yao** is paraphrased, not quoted (OUTLINE: quote only after re-reading); TODO comment in sec_front.tex.
8. **Remark after Thm 1** adds that the Jacobi matrix is compact with eigenvalues k^{−p} (abstract states it).
9. **§10.3** adds the test case f(k) = ε sin log k (an open question; nothing claimed). **§10.4** contains one sentence
   on the zeta-zero measure referring to "work in preparation" (G3prime N″, REVIEWED, unpublished). No claim about RH
   is made. **Coordinator: keep or drop.**
10. **Paper 3** has a provisional title in refs.bib.
11. **Figure 1** drawn per OUTLINE §3.1/§9: tools box feeds §§5–6 and §7; arrows labelled §3 (shift) and §4
    (smoothing and stability); ℓ ≡ 1 branch to Theorem 2.
12. Theorem statements 1–4 are verbatim from OUTLINE §2, except that "Here c(p) = …" is printed inside Thm 1 as in the
    outline, and Thm 3's parenthesis (d(xσ) := x dσ(x)) is upright.

## 3. Cross-chunk labels used by chunk A (must be defined by chunks B–D, or renamed by the coordinator)

Status 2026-10-14 21:57: all chunk B labels below exist in sec_2–sec_4.tex as drafted (checked by grep); chunk B's
\cite keys (Paper1, WLXZ, KMVV, CD, DLMF, DPQ, DD) are all in refs.bib. Chunk C/D labels not yet checked.

| Label | Expected object | Chunk |
|---|---|---|
| sec:prelim | §2 Preliminaries | B |
| sec:shift | §3 Christoffel shift | B |
| sec:smoothing | §4 smoothing reduction | B |
| lem:potter | Lemma 2.1 (chaining and Potter bounds) | B |
| prop:equilibrium | Proposition 2.2 (Paper 1 input) | B |
| lem:smoothing | Lemma 4.1 (Gaussian smoothing) | B |
| lem:saturation | Lemma 4.3 (saturation of the head; defines M₀) | B |
| prop:stability | Proposition 4.5 (stability under ℓ/ℓ₁ → 1) | B |
| rem:base-window | Remark 4.6 (robustness of the base window) | B |
| sec:frame | §5 | C |
| sec:outer | §6 | C |
| rem:quotient-p1 | Remark 6.3 (quotient parametrix fails at p = 1) | C |
| prop:frame | Proposition 6.9 (Frame Proposition) | C |
| app:apriori | Appendix C | C |
| sec:hardedge | §7 | D |
| prop:UR-comparison | Proposition 7.4 (uniform resolvent, comparison problem) | D |
| rem:alpha-ge-1 | Remark 7.8 (α ≥ 1) | D |
| sec:extraction | §8 | D |
| app:L2 | Appendix A | D |
| app:resolvent | Appendix B | D |

Labels defined by chunk A for others: thm:main, thm:pure, thm:shift, thm:engine; def:sv, def:smoothing, def:A,
def:rate is **not** defined (regular rate is defined in running text just before Thm 3; chunk B defines it formally in
§2.3); eq:sigma, eq:jacobi, eq:cp, eq:law, eq:paper1-averaged, eq:osc, eq:smoothing, eq:epsLambda, eq:thetap;
rem:main-finite, rem:main-unbounded, rem:main-rate, rem:main-averaged, rem:pure-lommel, rem:pure-zeta,
rem:pure-constant, rem:shift-credit, rem:shift-converse, rem:engine-scope; sec:intro, sec:setting, sec:results,
sec:context, sec:strategy, sec:organisation, fig:dependency; sec:numerics, tab:numerics, sec:further, sec:tilt,
conj:tilt, sec:p1-routes, sec:rough, sec:nodes. Macros (via \providecommand in chunk A files): `\Ath{θ}` prints
(A_θ); `\ceil`. sec_back.tex defines a `conjecture` environment if none exists.

## 4. Citation gate (every key in refs.bib)

"Read" = read by an agent of this project, with quotes recorded in the repo (as for Paper 1). The chunk A drafting agent
did not re-open any external source; quotations in sec_front.tex are copied from the repo records named below.

| Key | Source | Status | Where recorded | Used by chunk A for |
|---|---|---|---|---|
| Paper1 | companion paper | own | papers/paper1 | throughout |
| Paper3 | companion paper | in preparation | THEOREMS.md H4 | announcement |
| WLXZ | arXiv:1410.3948v1 | READ (§§1–7) | research/G1/RH/CITATIONS.md (WLXZ-v1) | context, frame |
| KMVV | arXiv:math/0111252v2 | READ (§1, §6) | RH/CITATIONS.md (KMVV) | Figure 1 (tools) |
| CD | arXiv:1711.01590v4 | READ (abstract, §§1–5) | RH/CITATIONS.md (C–D) | context (abstract quote), §1.4, (5.5) in §10.1 |
| DLMF | dlmf.nist.gov | READ (sections listed in RH/CITATIONS.md) | RH/CITATIONS.md | not cited by chunk A |
| KV, Van | arXiv:math-ph/0305044, math/0212014 | READ (parts) | RH/CITATIONS.md | not cited by chunk A |
| BKMM | arXiv:math/0212149v1 | READ (abstract, §1) | research/G1/CITATIONS.md | context |
| DY | arXiv:2104.03563v1 | READ (§1, PDF re-fetched 2026-10-14) | RH/CITATIONS.md (DY, Paper 2) | context (verbatim quote) |
| DP | arXiv:2307.09277v2 | OPENED by novelty agent | novelty_lineB_B.md §§1–2 | context (quote "the crucial Theorem 4.7 in [4] requires a different proof") |
| Pio | arXiv:1910.00564v2 | OPENED | novelty_lineB_B.md §1 | context |
| Tro | arXiv:2412.18656v5 | OPENED | novelty_lineB_B.md §1 | context |
| MM | arXiv:0805.1980v1 | OPENED | novelty_lineB_B.md §1 | context |
| DIK | arXiv:0905.0443v3 §6.2 | OPENED | novelty_lineB_B.md §2(a) | context. Title and journal data confirmed by the arXiv API |
| LL | Levin–Lubinsky 1999 announcement | OPENED (PDF, Lubinsky homepage) | novelty_lineB_B.md §1 item 7 | context. Publication data to verify; book (CMS 2001) NOT read |
| VA | arXiv:math/9510214 §3 | OPENED | novelty_G1RH.md §§1.1, 1.3; novelty_lineB_A.md §3 | Lommel and Tricomi–Carlitz remarks |
| Monien | arXiv:0901.1883v1 | READ (Paper 1) | papers/paper1/NOTES.md §3 | Rem. pure-zeta |
| HaynesZudilin | SIGMA 11 (2015) 101 | READ §1 (Paper 1) | papers/paper1/NOTES.md §3 | context |
| DPQ | arXiv:2508.07653v1 Prop. 2.1 | OPENED (statement verbatim; proof read only through a summarising tool) | novelty_lineB_A.md §2 | Rem. shift-credit, shift-converse |
| DD | arXiv:1012.3712v2 §1 | OPENED | novelty_lineB_A.md §1 | Rem. shift-credit |
| BD | arXiv:2107.09824 | OPENED (fetch-tool extraction) | novelty_lineB_A.md §3 | not cited by chunk A |
| BueMar | LAA 384 (2004) | **UNREAD** | — | do not cite |
| BGT | Regular Variation (1987) | **UNREAD** (only via quotations in Eichinger–Winter, Benaim–Friz, Alouin–Bigot) | novelty_lineB_B.md §4 | do not cite |
| Vuil | Trans. AMS 218 (1976) | **ABSTRACT ONLY** | novelty_lineB_B.md §4 | do not cite for content |
| Fischer | Z. Anal. Anwend. 17 (1998) | **UNREAD** (pointer) | RESEARCH_PROGRAM.md §6 | do not cite |

Not cited although relevant (unread): Lubinsky–Mhaskar–Saff (1988); Knopfmacher–Lubinsky–Nevai (1988; needed for the
Paper 3 positioning, not for this paper); Chihara 1978 Ch. III; Wall 1948; Szwarc, Math. Z. 217 (1994);
Geronimo–Van Assche, JAT 62 (1990); Gragg–Harrod (RKPW; §9 names the algorithm without citation, TODO comment);
Galambos–Seneta (1973); the Lommel primary sources (Dickinson 1954, Dickinson–Pollak–Wannier 1956, Goldberg 1965).

Bibliographic fields marked "to verify" in refs.bib: KMVV pages; KV, Van pages; DLMF release; DY authors/title; DP,
Tro, MM titles; DIK title; LL publication data; VA publication data; DD volume/pages; Monien status; Paper 3 title.

## 5. Numerics (chunk A; all NUMERICAL, none certified)

- `checks/table2.py` → `checks/table2.out` (Table 2). Run:
  `/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/.venv/bin/python papers/paper2/checks/table2.py > checks/table2.out`
  (≈ 1 min; the script prepends the main repository's `src/` to `sys.path`, which has the built C kernels). Model: atoms
  k ≤ K plus Gauss–Legendre tail (log panels, ratio 1.02, 8 nodes) to T = 10⁴⁸ (p = ½) or 10¹⁶ (p = 1, 2); RKPW long
  double. Truncation runs: (K, T) = (10⁵, T), (2·10⁵, T), (2·10⁵, T/10⁴). Max spreads: 9.5·10⁻⁸ (p = ½), 1.9·10⁻⁸
  (p = 1), 1.7·10⁻¹¹ (p = 2). The script also prints θ_n/2 = Λ′(log n)/2 for §10.1.
- `checks/lommel_check.py` → `checks/lommel_check.out` (Remark pure-lommel): mpmath, 120 digits, Hankel determinants of
  ζ(2j + 2), n ≤ 9; max relative error 2·10⁻⁹⁵. Run with `-I`.
- No-tail values quoted in §9 (−1.81, −13.3, −105.9) are from research/G1/RH/route2/checks/check_r2p_coeff.out [4]
  (p = ½, s = 1.5, ℓ = exp√log(k+e), atoms k ≤ 2·10⁵, n = 100, 400, 1600).
- The tilt ratios "0.91 to 0.99" in §10.1 are (B(ℓ) − B(1))/(θ_n/2) from table2.out (0.911 … 0.987).

## 6. Open TODOs (front half and back matter, after the revision)

1. Re-verify all quotations character by character against the sources (CD abstract, DP §1, DY §1, DPQ, DD, VA).
   DPQ's proof: re-read from the PDF (only the statement is verbatim).
2. Bibliographic fields still "to verify": Van (J. Approx. Theory 125 pages), DLMF release (pages fetched 2026-10-14
   show "Release date 2026-09-15"), LL publication data, Monien status, Paper 3 title, DD volume/pages (doi given).
3. Supplementary material: URL and commit hash (§9).
4. Author line (placeholder) and MSC codes.
5. Remaining length: §2.5 can lose ≈ 1 more page only if the T1(a) proof moves into Lemma 5.1 and the Mellin items into
   App. A (RH agent's files); Prop. 2.5(iii) to be cited in Lemma 5.4(iii) or deleted.
6. The hedge in the proof of Theorem 3 (sign remark, sec_8.tex, EDIT L5) is in the RH agent's file.

## 7. Pre-submission checklist

- [ ] Author name, affiliation, email, MSC codes (suggest 42C05, 47B36, 30E25, 26A12; to confirm).
- [ ] Remove all `% src:` and `% TODO` comments.
- [ ] Citation gate: every `\cite` key is READ/OPENED in §4 above; no UNREAD key is cited (currently none is).
- [ ] Re-verify every quotation against the source (CD, DP, VA, Monien, HZ, DD, DPQ).
- [ ] Complete the "to verify" bibliographic fields; check journal versions of arXiv-only items.
- [ ] Rerun the novelty search close to submission (arXiv: "slowly varying" + orthogonal polynomials / Riemann–Hilbert;
      "accumulation point" + discrete orthogonal polynomials); the arXiv API was rate-limited during the 2026-10-14
      search (novelty_lineB_B.md).
- [ ] Read before any further positioning claim: Szwarc 1994, Geronimo–Van Assche 1990 (rate in Thm 3);
      BGT §1.8 and Vuilleumier 1976 (Lemma 4.1 credit); Bueno–Marcellán 2004.
- [ ] Re-run `checks/table2.py` and `checks/lommel_check.py` from a clean checkout; confirm the outputs are identical.
- [ ] Expert read of Theorem 4 (Deift, Piorkowski; Kuijlaars, Van Assche; Zhao, Dai) — OUTLINE §7 R1.
- [ ] Tell the reviewer about the re-ordered assembly (OUTLINE §7 R10) and the pure powers via the comparison route
      (R11).
- [ ] Compile from clean (pdflatex, bibtex, pdflatex ×2): no undefined references, no overfull boxes.
