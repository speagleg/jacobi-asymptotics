# Paper IV — notes (first full draft, 2026-10-21)

"Jacobi coefficients of measures on reciprocal spectra: a spectral dictionary and the natural index."
`main.tex` (amsart 11pt, house style of Paper III) with `sec1.tex` … `sec8.tex`, `secA.tex`, `refs.bib`.
Build (pdflatex, no latexmk needed): `pdflatex main; bibtex main; pdflatex main; pdflatex main`.
Last build: **26 pages**, 0 errors, 0 overfull boxes, 0 undefined references, 0 BibTeX warnings; 9 underfull boxes
(badness ≤ 10000, cosmetic, mostly the `p{}` columns of the appendix tables). `main.pdf` and `main.bbl` in this
directory are from that build.

**Status: DRAFT, not reviewed as a paper.** The sources are only partly reviewed: JZC_M1 (one reader; two readers and REVIEWED since 2026-10-23, see the last section), JZC_M4_proof
(review A only), JZC_M2, JZC_M4 and SPEC §§3.14–3.18 (NOT REVIEWED). Theorems A–C therefore need Rule R before any
"REVIEWED" claim. No mathematical statement of the sources was strengthened.

## 1. Sections

| § | Title | pp | Content |
|---|---|---|---|
| 1 | Introduction | 1–4 | setting σ_Λ, Z_Λ, W(q), ε_j, N; Theorems A (= 5.7(iii)), B (= 4.2), C (= 3.2 + 3.5); the dictionary in one display; organisation/notation |
| 2 | Setting and prior results | 4–6 | Thm 2.1 = [II, Thm 1.4]; frame of [II §§4, 8, 10]; Lemma 2.2 (band-factor moments), 2.3 (gauge), 2.4 (linear response), Thm 2.5 (d₂, ε_j) |
| 3 | The constrained equilibrium | 6–9 | Thm 3.2, Rem 3.3, Cor 3.4 (a = 4c), Prop 3.5 (soft edge carries poles), Rem 3.6 (drum root), Rem 3.7 (checks). *(2026-10-23: Lemma 3.1 deleted (review B, B1); now Thm 3.1, Rem 3.2, Cor 3.3, Prop 3.4, Rem 3.5, Rem 3.6.)* |
| 4 | The kernel | 9–12 | Lemma 4.1 (K0), §4.2 functional e_n, Thm 4.2 (K for p > 1 and K′ for p < 1), Rem 4.3, Prop 4.4 (perturbed phase), Rem 4.5 |
| 5 | Natural index, expansion of the lattice | 12–17 | Prop 5.1 (N.1), Prop 5.2 (Bessel), Lemmas 5.3, 5.4, Prop 5.5, Lemma 5.6 (N.6a–d), closed forms (5.2)–(5.6), Thm 5.7 (N.6), Table 5.1 (visibility), Rem 5.8 |
| 6 | Examples and numerical evidence | 17–23 | method; Tables 6.1–6.8: natural index, f₄ lattice, Hurwitz, pole law (+ κ shift, Möbius), subleading pole (6.1), drums, q^N oscillators, noise |
| 7 | Conjectures and open problems | 23–25 | Conj 7.1 (natural-index law), Rem 7.2, Conj 7.3 (S1⁗), Conj 7.4 (S1-N′), Problem 7.5 (second-order kernel), §7.3 what a proof needs, Rem 7.6 (S2′), §7.4 further problems |
| 8 | Relation to the literature | 25 | **PLACEHOLDER** (TODO comment: to be filled from research/G1/RH/spectral/NOVELTY_JZC.md) |
| A | Reproducibility | 25–26 | sha256 of the four exact scripts, the five exact runs, script ↔ section table, run_all.sh |

Source lines: sec1 151, sec2 124, sec3 199, sec4 157, sec5 301, sec6 324, sec7 111, sec8 17, secA 78.

## 2. Label mapping (repo statement → paper)

| Repo statement (label) | Paper | Form in the paper |
|---|---|---|
| Paper II Thm 1.4 | Thm 2.1 | imported theorem |
| E3 Lemma F.1′ (PROVED-mod-cite, REVIEWED) + Paper II Lemma 10.1(iii)–(iv) | Lemma 2.2 | lemma, proof sketch (p > 1), cited (p < 1) |
| E3 Lemma E3.4 (PROVED) | Lemma 2.3 | lemma, no proof (TODO) |
| E3 Lemma E3.7 (PROVED, exact algebra) | Lemma 2.4 | lemma, proof sketch |
| E2 Thm E2.1, E3 Thm E3.1, E3.2, Cor E3.3, E3.4 (PROVED-mod-cite, REVIEWED) | Thm 2.5 | theorem, proof outline only (TODO) |
| JZC_M1 Thm Q (PROVED + REVIEWED since 2026-10-23, REVIEW_JZC_M1_B B1: energy positivity is Paper I Lemma 3.3 = G2 Lemma EP; was PROVED-mod-cite, Saff–Totik I.1.8 NOT QUOTED) | Thm 3.1 (was Thm 3.2 + Lemma 3.1) | theorem with full proof; positivity cited as [PaperI, Lemma 3.3], with its integrability hypothesis checked for τ = μ′ − μ; Lemma 3.1 and its TODO deleted |
| JZC_M1 weaker hypothesis (F7) + review B Rule A numerics, edge remark (F3 + B3 qualifier), node-language reading | Rem 3.2 (was 3.3) | remark |
| JZC_M1 Cor Q.1 (PROVED + REVIEWED) | Cor 3.3 (was 3.4) | corollary with proof |
| JZC_M1 Prop M1.2 (PROVED + REVIEWED) | Prop 3.4 (was 3.5) | proposition with proof; remainder O(η²) (B7) |
| SPEC §3.16 β² derivation (exact algebra of the continuum condition) | Rem 3.5 (was 3.6) | remark (computation) |
| m1_theoremQ.out (32 assertions), m1_edge.out (NUMERICAL) | Rem 3.6 (was 3.7) | remark |
| SPEC §3.14 Lemma K0 (PROVED) | Lemma 4.1 | lemma with proof |
| SPEC §3.14 Thm K (p > 1) + JZC_M2 Thm K′ (p < 1) (PROVED-mod-cite; MB for (1+x)^{−3/2} NOT QUOTED) | Thm 4.2 | theorem with proof; MB step written as Mellin inversion of DLMF 5.12.3 (inversion itself not quoted) |
| SPEC §3.14 "What Theorem K adds", "Structural reading" (HEURISTIC parts) | Rem 4.3 | remark |
| spec_kernel.out (K), m2_thmK_plt1.out | text after Rem 4.3 | numerical sentence |
| SPEC Prop 3.14.4 (computation PROVED, conclusion HEURISTIC) | Prop 4.4 + Rem 4.5 | proposition (computation, proof sketch) + remark marked as hypothetical |
| JZC_M2 Prop M2.2 (CONDITIONAL on G2) | Rem 4.5 | remark, "none of this is a statement about b_n" |
| JZC_M4 Identity N.1 (PROVED) | Prop 5.1 | proposition with proof |
| JZC_M4 Prop N.2 (PROVED from the Lommel closed form) | Prop 5.2 | proposition; proof via [VA §3] + quadratic transformation; **masses ∝ j^{−2} for general ν not quoted (TODO)**; Z(0) uses McMahon (not quoted, TODO) |
| JZC_M4_proof Lemma N.6a (PROVED-mod-cite) | Lemma 5.3 | lemma, proof sketch |
| JZC_M4_proof Lemma N.6b (PROVED) | Lemma 5.4 | lemma, proof sketch |
| JZC_M4_proof Prop N.6c (PROVED-mod-cite) | Prop 5.5 | proposition, proof sketch |
| JZC_M4_proof Lemma N.6d (PROVED, exact computer algebra) | Lemma 5.6 | lemma with proof (description of the computation) |
| JZC_M4 §5 closed forms f₄, f₆; §6 A_j, B_j, g₁,₄; JZC_M4_proof §5 h₂ | (5.2)–(5.6), Thm A | formulas (identities asserted in the exact outputs) |
| JZC_M4_proof Thm N.6 (i)–(iii) + visibility table (PROVED-mod-cite) | Thm 5.7 + Table 5.1; Thm A = 5.7(iii) | theorem with proof |
| JZC_M4 Prop N.3 beyond N⁻⁶ (f₈, f₇ = 0: NUMERICAL), denominators, evenness heuristic, 1/(2j−1) remark (HEURISTIC) | Rem 5.8(b)–(d) | remark, labelled numerical / heuristic |
| m4_natural_index.out, m4_f4_lattice.out, m4_zeta_lattice.out (NUMERICAL) | Tables 6.1, 6.2, §6.1 text | tables |
| SPEC §2 Hurwitz table; §3.10 S1′ d₂ rows; §3.11(a) rule H; hur_small (NUMERICAL) | Table 6.3, §6.2 text | table + text |
| SPEC §3.12 pole law + table (NUMERICAL; HEURISTIC derivation) | Conj 7.1(c), Table 6.4 | conjecture + table (identification row marked) |
| SPEC §3.5 κ law, Prop M (PROVED, elementary), Möbius check | §6.3 "A constant shift" | text (Prop M stated in one sentence; identification row and the 60% spread at p = 0.3 marked) |
| SPEC §3.12 Limitation (subleading pole terms) | Rem 7.2 | remark |
| SPEC §3.15 Conjecture S1⁗ (NUMERICAL) | (6.1), Table 6.5, Conj 7.3 | formula, table (identification rows marked), conjecture |
| SPEC §3.16 drums (NUMERICAL) | §6.5, Table 6.6 | text + table (Rule X note on the n^{1/2} prediction in the caption) |
| SPEC §3.17 quartic, q^N, rational (N−1)/(6(N+2)) (NUMERICAL; derivation PROVED-mod-cite given the Dunham term, conditional on the pole law) | §6.6, Table 6.7 | text with the AB identity stated as conditional on the second-order quantisation condition (TODO citation) |
| SPEC §3.18 noise (NUMERICAL; single seeds) + §3.6 ensembles + S4 | §6.7, Table 6.8 | text + table |
| JZC_M4 Conj S1-N (CONJECTURE) + S1 / S1′(II) / S1″ / Principle E | Conj 7.1 | conjecture; instances listed below it |
| JZC_M4 Conj S1-N′ (CONJECTURE; instances PROVED-mod-cite) | Conj 7.4 | conjecture; proved instances listed |
| JZC_M4 §6 remark "second-order edge kernel" (HEURISTIC) | Problem 7.5 | problem |
| SPEC §3.14 Hypothesis G (G1–G3) | §7.3 prose | open problem, not a named hypothesis |
| SPEC §3.2 Thm S2′ (PROVED-mod-cite, REVIEWED) | Rem 7.6 | remark only (not among the requested sources; TODO: include with proof or cite) |
| SPEC §3.13 log resonance (weak test) | one sentence after Conj 7.1 | sentence |

Paper vocabulary: none of PROVED/REVIEWED/Rule/Law P/Plan/RH appears in the text; labels live only in this file. The
only "RH" string in the PDF is the repository path `research/G1/RH/spectral/checks` in Appendix A.

## 3. Placeholders and TODOs in the sources

- `sec8.tex`: whole section (literature) — placeholder with the list of topics; no citations invented.
- `sec2.tex` top: Thm 2.5 and Lemmas 2.2–2.4 rest on E2_pgt1.md / E3.md (REVIEWED, but in no paper).
- ~~`sec3.tex` Lemma 3.1: Saff–Totik Lemma I.1.8 not read/quoted~~ — resolved 2026-10-23 (REVIEW_JZC_M1_B B1): Lemma 3.1 deleted;
  the proof cites [PaperI, Lemma 3.3] (no compact support needed), with the integrability hypothesis checked in (iv).
- `sec5.tex` Prop 5.2: general-ν Lommel masses and McMahon's expansion (DLMF 10.21.19) not quoted.
- `sec6.tex` §6.6: the second-order Bohr–Sommerfeld (Dunham) term not quoted; §6.7: the predicted noise variances come from
  a post-processing step whose output is not stored.
- `sec7.tex` Rem 7.6: Theorem S2′ not in any paper.
- `secA.tex`: six scripts missing from run_all.sh; spec_kernelfft post-processing output to be stored.
- `main.tex`: tag for the data availability statement (v1.0-paper4?) to be fixed.

## 4. Inconsistencies and points noticed in the sources (not fixed there)

1. **Prior results not in a paper.** E2 (d₂ for all p > 1) and E3 (κ_p for 1 < p < 2, d₂ and ε_j for p < 1, Lemma E3.7) are
   REVIEWED repo notes but appear in none of Papers I–III (Paper II §13.1 still lists d₂ as open). Paper IV needs them as an
   appendix or a separate paper.
2. **JZC_M1 Thm Q proof (i)** says "As a → 0: F(a) ≥ ∫_a^Y σ → ∞ (H3)"; the divergence follows from (H2) (σ ≥ y₀σ(y₀)/y), not
   (H3). The paper attributes it to (H2).
3. **Check counts.** JZC_M1 says m1_theoremQ has "20 assertions"; the stored output prints "ALL 28 CHECKS PASSED".
4. **SPEC §3.17 q^N precision** "to 10⁻⁹–5·10⁻⁸": spec_homog.out gives ~10⁻¹⁰ for N = 4, 6, 8, 2.4·10⁻⁹ for N = 10 and
   7.1·10⁻⁸ for N = 12. The paper says "between 10⁻¹⁰ and 7·10⁻⁸".
5. **SPEC §3.18** form-factor predictions (5.67, 8.02, 11.36; 22.5, 31.7, 44.9) are not in spec_kernelfft.out (the script
   only prints the kernel spectrum; the variance integral is a separate, unstored post-processing).
6. **run_all.sh** does not regenerate spec_quartic, spec_qN, spec_corners, spec_edgekernel, spec_noiselin, spec_kernelfft.
7. **Prop N.2 label.** JZC_M4 labels it PROVED "from the Lommel closed form"; SPEC §3.9 says the Lommel computation is
   "NOT yet re-derived in this repo", and CITATIONS quotes VA §3 only for the recurrence and the spectrum (the measure is
   identified there only for ν = 3/2, via Paper II Remark 9.6). The closed form is checked numerically (spec_lommel, 1.6·10⁻¹⁵).
8. **Lemma N.6d / Thm N.6(ii) wording** "for j ≤ 5 at K = 5, the bracket error is O(N⁻⁵)": the N⁻⁴ bracket coefficient has a
   closed form only for j = 1 (g₁,₄); for j = 2…5 it is computed but not displayed. The paper states only the j = 1 case.
9. **SPEC §3.12 κ law**: the out-of-sample p = 1.5 run (L = −0.5662723) is a reviewer's scratch run, not a stored output; the
   paper omits it and uses spec_kappa_fit.out only.
10. **m1_theoremQ log-law density**: one of the four test densities is a logarithmic counting law; it is not described in
    the paper (Remark 3.7 says "a fourth density") to respect AGENTS rule 3.
11. **Bouncer, Robin, Maslov readout** (SPEC §§3.3, 3.4, 3.13; Prop B values known from the literature with a sign conflict
    noted in §3.9) were not placed: outside the requested sources. Remark 7.6 and the dictionary text do not rely on them.

## 5. Bibliography

`refs.bib` has 8 entries, each copied verbatim (checked by script) from an existing bibliography:
PaperI, PaperII, DLMF, VA (paperIII); Paper3, KMVV (paperII); Rakhmanov, DragnevSaff (paper1). All are cited.
No entry from CITATIONS.md beyond these was needed; DLMF formulas used: 5.5.3, 5.9.1, 5.12.1, 5.12.3, 9.7.2, 9.7.5–6,
10.17.1, .5, .6, .8, .11, .12, 10.40.1–4, 25.2.1, 25.4.1 (all quoted in research/G1/RH/CITATIONS.md).


## Session additions (2026-10-21)
- §7 now has Theorem 7.x (reflection, proved), Lemma (self-similar Buyarov–Rakhmanov identity, proved) and Conjecture
  (shift), from research/G1/RH/spectral/JZC_M4.md §7.
- §8 written from research/G1/RH/spectral/NOVELTY_JZC.md. The bib entries BleherIts, BeckermannKuijlaars2002,
  BeckermannKuijlaars2001, StovicekSwiderski, EMP, VanAsscheVanBaelen were relayed second-hand (WebFetch); verify against the
  sources before submission (Rule C). BeckermannKuijlaars2001 Thm 2.1 is decisive for the novelty of Theorem Q.
- Inconsistencies flagged by the drafting agent and fixed in the notes: JZC_M1 step (i) now cites (H2); m1_theoremQ count 28;
  JZC_M4 Prop N.2 relabelled PROVED-mod-cite; run_all.sh lists the scripts it does not run.

## Session additions (2026-10-22): Theorem Σ, Toda, Theorem H, the κ-family, Conjecture W
Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main` → **40 pages**, 0 errors, 0 overfull boxes, 0 undefined references;
12 underfull boxes (cosmetic); 1 BibTeX warning (missing pages in BeckermannKuijlaars2001, pre-existing). Multi-index of the
layers renamed β → **r** (`\br`) in §5 and §9 to free β for the Szegő exponent.

New section order: 1 intro, 2 prior, 3 equilibrium, 4 kernel, 5 natural index, **6 Reflection, shift and the Toda structure
(secS.tex)**, **7 Hurwitz lattices (secH.tex)**, 8 examples (was 6), 9 conjectures (was 7), 10 literature (was 8), A.

| Repo statement (label) | Paper | Form in the paper |
|---|---|---|
| JZC_M4 §7 decoupled model; Theorem R (PROVED, algebra; M4 NOT REVIEWED) | §6.1, Thm 6.1 | moved from §7.4 unchanged |
| JZC_M4 Lemma BR (PROVED) | Lemma 6.2 | moved from §7.4 |
| JZC_SIGMA Theorem Σ + Prop FI (PROVED-mod-cite (Lemma F (ii)) + REVIEWED) | Thm 6.3 (i), (6.2); Thm D in intro | theorem; proof: FI⇔Σ algebra, Lemma 6.5, uniqueness on p∈(1,2)∖ℚ, α∈(−½,½), γ∈(0,¼), identity theorem |
| JZC_SIGMA Cor Σ.1 (PROVED-mod-cite + REVIEWED) | Cor 6.4 | corollary with proof; f_{2k} degree k in ν² stated as observed only |
| JZC_SIGMA Cor Σ.2 (PROVED-mod-cite + REVIEWED; weight ≥ 3 open) | Thm 6.3 (ii) | stated in natural-form version (equivalent to the base-ν statement by the FI⇔Σ algebra) |
| JZC_SIGMA Lemma F (i) (PROVED algebra + REVIEWED), (ii) (PROVED-mod-cite by transfer, 0 ≤ γ < (1−|α|)/2, + REVIEWED) | Lemma 6.5 | lemma, proof sketch; text says the transfer is written in the repo notes and not repeated |
| JZC_SIGMA Remark C (OBSTRUCTION) | §6.3 first paragraph | one sentence |
| JZC_SIGMA §5 checks (exact order 4, numerical order 8, controls) | text after proof of Thm 6.3 | sentence, with Rule X caveat |
| JZC_M4 §8 Theorem T (**PROVED-mod-cite, NOT REVIEWED**) | **Prop 6.6** (not a theorem) | proposition, "proof sketch", text says the a_n-extraction and τ-uniformity are not written out |
| JZC_M4 §8 diagonal layer, a₂ (NUMERICAL, m4_toda (A), m4_diag) | Conj 6.7 | conjecture + numerical evidence |
| JZC_M4 §8 Cor T′ (conditional/heuristic), 1/(2j−1) reading (HEURISTIC) | Rem 6.8 | remark, "we expect … not written out", "heuristic reading" |
| JZC_M3a_H Theorem H (i) (PROVED-mod-cite + REVIEWED for p ≠ 1, every memo link REVIEWED; ζ(−jp,a) form adds Remark 3.3, PROVED-mod-cite via CITATIONS (Hurwitz-DK), not second-read) | Thm 7.1 (i); Thm E in intro | theorem; constants via Hurwitz's formula quoted from Dixit–Kumar Thm 1.1 with hypotheses checked in the text |
| JZC_M3a_H Theorem H (ii) (integer layer all orders, weight ≤ 2 layers: PROVED-mod-cite + REVIEWED via Σ; e_j, j ≥ 3: exact to N⁻² relative dressing; weight ≥ 3 beyond: CONDITIONAL) | Thm 7.1 (ii) + text after it | theorem; weight ≥ 3 stated as open |
| H-a … H-f (JZC_M3a_H §2) | §7.3 (H-a)–(H-f) | proof outline; estimates "written out in the notes of the repository" |
| JZC_M3a_Hd (index transfer, α-frame) | §7.2 | text |
| JZC_W_outer + JZC_W_kappa (P K.11, P K.12 + Prop K.12′) + JZC_W_BT (BT.1, BT.5): κ-family W at first order in the poles, PROVED-mod-cite + REVIEWED; input WE.1 (JZC_W_exact) reviewed by REVIEW_JZC_W_WE1_K12p_B.md (16:04, ACCEPT WITH FIXES W1–W3, K1–K4, A1–A2, all MINOR) — **fixes not yet applied in the memos when this draft was built** | Thm 7.2 (displayed form, remainder O(n^{−1−p}), coefficient −2(2−p)cκ = pR_qW(q)π cot(πq)); refined form in the text after it | theorem + footnote ("re-read independently … minor corrections still being incorporated") + proof outline. Check K1 (mixed Toda × branched terms; harmless for the κ-family) when the fixes land |
| JZC_W_kappa P K.14 / W_outer §7 (p < 1 OBSTRUCTION) | last paragraph of §7.4 | sentence |
| JZC_W Conj W (CONJECTURE, NUMERICAL) | Conj 9.5 + (W1)–(W5) | conjecture |
| JZC_W Prop W.1 (PROVED, elementary) | §9.3 data paragraph ("which is exactly …") | sentence |
| JZC_W Obs W.3 (NUMERICAL) | text after Conj 9.5 | sentence, labelled by precision |
| JZC_W Obs W.4, finding (multiplicities); Z(−j) = 0 for l(l+1) (PROVED) | Rem 9.6 | remark with the elementary proof |
| JZC_W Refinement W′ (CONJECTURE, post hoc, one pre-registered confirmation) | Rem 9.7, Problem 9.9 | remark; K4 of review B: K.12′ does not prove W′ (the paper does not claim it) |
| JZC_W_BT Theorem BT (formal-layer identity PROVED, asymptotics CONDITIONAL (F-br)), Prop BT.5 (REVIEWED) | Rem 9.8 | remark; "not proved for actual measures"; note that for ρ < ½ the companion lies inside W's claimed precision (our reading of the orders) |
| JZC_W §2.3 table (NUMERICAL, pre-registered) | §8.5, Table 8.6 | selection of 16 of 41 rows; protocol and pass criterion stated |
| JZC_M4 §9 large order (NUMERICAL) | §9.2 paragraph | numerical sentences (not requested; added because the old hypergeometric remark would otherwise mislead) |

Bibliography: **DixitKumar** added (arXiv:1912.01199). Statement quoted in research/G1/RH/CITATIONS.md (Hurwitz-DK); title/authors/date
re-read from the arXiv abstract page by WebFetch on 2026-10-22 (v1 only, no journal reference). Rule C flag kept: WebFetch is not a
first-hand reading of the PDF; verify before submission. Titchmarsh (2.17.3), the primary source, is mentioned in §10 as not consulted.
DLMF 5.2.1 is now used (step H-c; quoted in CITATIONS (DLMF-zeta, Plan 67)).

Not included, and why:
- Weight ≥ 3 zeta-layer shift and evenness of the zeta layers beyond N.6(ii): open in the memos (stated as open).
- Lemma F for γ < 0: not covered by a reviewed statement (not used).
- The shift for a_n (JZC_SIGMA §7 item 3): not done; Conj 6.7 states it.
- Theorem BT's c₂, c₄ closed forms, Cor BT.4/BT.6, JZC_W_exact Prop WE.2/WE.3, the refuted P2: below the level of detail of the paper
  (BT.4/BT.6 CONDITIONAL; Thm BT asymptotics CONDITIONAL).
- JZC_W §1.6 (p = 1) and §5 (proof obstacles): reflected only in §9.4 "What a proof needs".

New TODOs: Theorem 7.1's and Lemma 6.5's estimates live only in repo memos (JZC_M3a_H chain, JZC_SIGMA) — same status as E2/E3 (§3
above): they need an appendix or a separate paper before submission. The scripts of §§6, 7, 8.5, 9.2 are not in run_all.sh (secA
says so). Once the review-B fixes are applied to JZC_W_exact/JZC_W_kappa, revise the footnote to Theorem 7.2.

## Session additions (2026-10-23): Rule R review B of JZC_M1 applied to §3 (Theorem C)
Source: research/G1/review/REVIEW_JZC_M1_B.md (ACCEPT WITH FIXES B1–B7). JZC_M1 Thm Q (i)–(iv), Cor Q.1, Prop M1.2 are now
PROVED + REVIEWED (Thm Q with no external input); novelty POSSIBLY-NEW (unchanged; B6 caveats).
Discrepancies D1–D15 of review B §3, as adopted:
- D1/D2 (B1): Lemma `lem:energy`, its TODO and the sentence "The proof of optimality uses one fact that we do not prove." deleted;
  (iv) cites \cite[Lemma~3.3]{PaperI} (PaperI already in refs.bib) with the integrability check for τ; the inversion is gone.
  The intro sentence after Theorem C (sec1.tex) that referred to Lemma `lem:energy` now says no outside input is used.
- D3, D4: paper wording kept; the memo was matched to it.
- D5 (B2): (ii) uses the per-point balayage argument (k_y, ρ_y, Fubini); (H1) says Hölder is used only in (iii).
- D6 (B4): continuity of F added in (i).
- D7 (B3): Remark (b) qualified (Hölder > ½ at a), with C = −h(a)/(π√a) and h(a) written out.
- D10: Remark (a) adds that the hypotheses are not necessary but cannot be dropped (review B §2.5 numerics).
- D8, D9, D11, D13: no action. D12: Remark (checks) now mentions the direct potential and the Φ-vs-U′ comparison (B5).
- D14 (B7): (eq:M12b) remainder O(η²); Theorem C in sec1.tex: O(nη_n²) for nη_n (was O(n²η_n²)).
- D15 (B6): sec8.tex adds "these results assume a finite constraint (Dragnev–Saff) or a compact interval (Rakhmanov) and are not
  used in the proof of Theorem C"; Beckermann–Kuijlaars 2002 is now "according to"; a source comment points to G2/CITATIONS.md
  (R96), (DS97), (VAVB).
- Rem 3.6 (checks): "between 10⁻⁹ and 10⁻⁶" → "between 10⁻⁸ (the printed digits) and 10⁻⁶" (review B INFO).
Theorem numbers in §3 shift by one (Thm 3.1, Rem 3.2, Cor 3.3, Prop 3.4, Rem 3.5, Rem 3.6); all references are by \label.
Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main` → **41 pages**, 0 errors, 0 overfull boxes, 0 undefined
references; 12 underfull boxes (cosmetic); 1 BibTeX warning (missing pages in BeckermannKuijlaars2001, pre-existing).

## Session additions (2026-10-23): Rule R review A of JZC_TODA / JZC_SHIFT applied to §6 (updated 2026-10-23 after JZC_TODA / JZC_SHIFT review)
Source: research/G1/review/REVIEW_JZC_TODA_SHIFT_A.md (ACCEPT WITH FIXES T1–T5, S1–S5; all applied in the memos). §6 now has
§6.4 (Toda structure, now a theorem) and a new §6.5 (index-shift law, diagonal layer). Numbering in §6 after Theorem 6.3/Cor 6.4/
Lemma 6.5: **Lemma 6.6** (new), **Theorem 6.7** (was Prop 6.6), **Theorem 6.8** (new), **Remark 6.9** (new), **Proposition 6.10** (new),
**Conjecture 6.11** (was Conj 6.7), **Remark 6.12** (was Rem 6.8). Label `prop:toda` renamed `thm:toda` (refs in sec1, sec7, sec8 updated).

| Repo statement (label) | Paper | Form in the paper |
|---|---|---|
| JZC_TODA Lemma T.1 (PROVED + REVIEWED; KNOWN, not cited: Van Assche read only via a fetch tool) | Lemma 6.6 | lemma with full (short) proof |
| JZC_TODA Theorem T (i)–(iv), T_H, Cor T.3 (PROVED-mod-cite + REVIEWED, review A; scope: E_pgt1/E_plt1/RH_px/G1u rows checked only for how the weight enters) | **Theorem 6.7** (was Prop 6.6) | theorem; proof outline: (i) Lemma T.A transfer (ℓ analytic of every angle, [II, Def 1.1]; gauge Lemma 2.3; r_n^{1/2} entire), (ii) Lemma T.2 Baire + integrated identity + coefficient extraction, (iii) T_H via Thm 7.1(i) + rationality (normalisation fix T4); "details in the notes of the repository" |
| JZC_TODA §7 checks (toda_measures, toda_layers) | text after Thm 6.7 | sentence. Review A's independent Arb test of the tilted lattice is **not** quoted (its scripts are in a reviewer scratchpad, not in the repo) |
| JZC_SHIFT Thm SH (i)–(ii), Lemmas LB, D, R, H (integer exponents, all p ≠ 1, all (β, ν): PROVED-mod-cite + REVIEWED) | **Theorem 6.8** (index-shift law) | theorem; proof outline: defect grading, conservation form, dispersionless hierarchy, Riemann invariant a = 2b, Hopf equations, characteristics, Lagrange inversion; β ≠ ν via Thm 6.7(iii) |
| JZC_SHIFT Cor SH.2 (continued identities: PROVED-mod-cite + REVIEWED; pole-layer identification via JZC_W2 Prop 2.1 (iii), NOT REVIEWED) | Remark 6.9 | remark; the pole-product reading for σ^{δ,κ} stated as conjectural |
| JZC_SHIFT §1.3, §4 (R1–R7), §5 (E2, E3, E6) | text after Thm 6.8 | sentence (exact agreement; dressed-index-shift ansatz fails) |
| JZC_TODA Prop T.4 (exact computer algebra for the model to order 4; PROVED-mod-cite as coefficients of α_n; + REVIEWED) | **Proposition 6.10** | a₂ and a₄ proved to order M⁻⁴, β-free, no M⁻¹, M⁻³ |
| JZC_M4 §8 diagonal layer beyond order 4 (NUMERICAL, m4_toda (A), m4_diag) | **Conjecture 6.11** (was Conj 6.7) | conjecture restricted to all-order evenness/β-independence |
| JZC_SHIFT §5.2 (E7) | Rem 6.12 | parity: exact to third order in the times for generic even integer layers |

Also: abstract (one clause: Toda flows of the integer layers of b_n and a_n; leading term = implicit index shift), §1.2 paragraph after
Theorem D (Theorem 6.7, 6.8, Prop 6.10), §1.4 organisation, §9 (Conj 9.4 text: c_r(0) from Thm 6.8; Conj 6.11 proved to M⁻⁴), §10
(dispersionless tools; literature not searched for Thm 6.8; Rule L for Thm SH not done), \cA macro in main.tex. The abstract was already
above the 1920-character guideline of Papers I–III (2233 characters of source); it is now 2393: shorten before submission.
Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main` → **44 pages**, 0 errors, 0 overfull boxes, 0 undefined references;
11 underfull boxes (cosmetic); 1 BibTeX warning (missing pages in BeckermannKuijlaars2001, pre-existing).
