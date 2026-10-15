# Paper III — notes (first full draft, 2026-10-15)

`main.tex` (amsart 11pt, 28 pages) with `sec1.tex` … `sec8.tex`, `refs.bib`. Build (no latexmk):
`pdflatex main; bibtex main; pdflatex main; pdflatex main` — 0 errors, 0 warnings, 0 overfull/underfull boxes,
0 undefined references (last build of this draft). Author line "Gordon [Surname]" is a placeholder.

**Status.** DRAFT. Every statement is taken from a REVIEWED repo source, except the items listed under
"New arguments (need Rule R)" below. Nothing here has had a second reader as a paper.

## 1. Sections and pages

| § | Title | pp | Main content |
|---|---|---|---|
| 1 | Introduction | 1–4 | Def 1.1, Thms 1.2–1.4, Cor 1.5 (all stated by p. 3); context; method; organisation and notation |
| 2 | First variation and localisation | 5–11 | conventions; imports from I and II (§2.2); slow variation; Lemmas 2.13–2.16 (first variation, Toda form, q̇, linear response with ε² remainder); Lemma 2.18 saturation, Cor 2.19 head mass, Lemma 2.20 arcsine localisation, (2.12) + Lemma 2.21 polynomial tail, Lemma 2.22 one power for all M, Lemma 2.23 u_sat < 1 |
| 3 | Every slowly varying factor | 12–14 | Def 3.1 smoothing, Lemma 3.2 Gaussian smoothing, Lemma 3.3 a priori size, Prop 3.4 stability, proof of Thm 1.2 |
| 4 | Rough weights | 14–19 | window constants (4.1), Lemma 4.1, Thm 4.2 (b-law), Lemma 4.3 + Thm 4.4 (a-law), proof of Thm 1.3(iii), Remarks 4.5–4.8 |
| 5 | Christoffel transformation at the Cesàro level | 19–22 | Prop 5.1 converse/point mass (+ Lean sentence), Prop 5.2 product identity, proof of Thm 1.4(i), Prop 5.3 O(1/k), Lemma 5.4 quadratic transformation, Cor 5.5 lattice values, Prop 5.6 conditional transfer |
| 6 | Pure powers as s varies | 22–25 | Prop 6.1, Lemma 6.2 sandwich, Prop 6.3, Lemma 6.4, Thm 6.5, Lemma 6.6 telescoping; proofs of Thm 1.4(ii)–(iii), Cor 1.5 |
| 7 | Numerical illustrations | 25–27 | Tables 1–2, s-law sup deviations, slowly varying factors |
| 8 | Open problems | 27–28 | Conjectures 8.1 (convexity), 8.3 (1/n for p ≤ 1 = [II, Conj 11.1]), 8.4 (tilt = [II, Conj 11.2]); Remark 8.2 (truncations) |

The outline estimated 48–54 pp; the draft is 28 pp. Reasons: Prop 6.7 (o(log n) log moment) omitted (outline III-b),
non-explicit Theorem R omitted (D5), tail-Cesàro a-law omitted (D6), Lemma RL omitted (III-d), and proofs written
compactly. Nothing in the outline's theorem list is missing.

## 2. Claim → source

| Paper III | Source (repo, REVIEWED unless stated) |
|---|---|
| Thm 1.2, Def 3.1, Lemmas 3.2–3.3, Prop 3.4, Rem 3.5 | papers/paper2 sec_4.tex (smoothing, saturation, a priori, stability, Steps 4–5); G1 PROOF.md §3.17 RedA |
| Lemma 2.11 (Potter), Rem 2.12 | papers/paper2 sec_2.tex §prelim-sv |
| Lemma 2.13, 2.14, 2.15 | papers/paper2 lem:first-variation; G1 §3.5 FVa, §3.12 Lemma Toda, §3.8 Lemma TV (q̇ formula) |
| Lemma 2.16 (i)–(iii), Rem 2.17 | G1 §3.11 LR, LR′, LRa (and the two-atom example) |
| Lemma 2.18, Cor 2.19 | papers/paper2 lem:saturation; G1 §3.3 Sat_p⁺ |
| Lemma 2.20 | G1 §3.8 Lemma LP, §3.10 LP-w, §3.12 LP′ (method of moments written out here) |
| Lemma 2.23 | G1 §3.10 Lemma u_s |
| Lemma 2.21, Lemma 2.22 | **new proofs** (see §3); statements correspond to G1 §3.4 Lemma TL and TAIL.md Cor TB-C |
| Thm 1.3(i), Lemma 4.1, Thm 4.2 | G1 §3.10 Lemma R1W, Theorem RW (cases A, B); uses LR′ (2ε²) in place of R2 (8ε²) — conclusion unchanged |
| Thm 1.3(ii), Lemma 4.3, Thm 4.4 | G1 §3.12 Lemma R1a, Theorem Ra; **cross-scale step reworked** (see §3) |
| Thm 1.3(iii) | Paper I Thm 1.1/Cor 1.2 (C = 1) |
| Rem 4.5–4.8 | G1 §3.10 RW-b/RW-d/RW-f, §3.11 Cor LR-law, §3.12 Ra-a/Ra-c |
| Prop 5.1 | papers/paper2 rem:converse; G1 §3.19 CT₁; DPQ Prop 2.1 statement; Lean `christoffel_shift_law_converse` |
| Prop 5.2, Thm 1.4(i) | SECOND.md Prop 3.1, Thm 3.2 |
| Prop 5.3 | SECOND.md Prop 3.5 |
| Lemma 5.4 | SECOND.md Lemma 2.1 (quadratic transformation) |
| Cor 5.5 | SECOND.md Cor 3.6(i), Thm 3.10(a)–(c); TC identification from WLXZ (1.4)–(1.9) (read this session, see §4) |
| Prop 5.6 | SECOND.md Cor 3.3, Thm 3.4 (as one implication, D9) |
| Prop 6.1, Lemma 6.2, Prop 6.3, Lemma 6.4, Thm 6.5 | UL.md Prop 3.7 (SECOND), Lemma V, Thm UF, Lemma W, Thm UF-lim, with the tail input replaced by Lemma 2.22 (as in TAIL.md Thm TS(a)) |
| Lemma 6.6, Thm 1.4(ii) all s₀, s₁ | TAIL.md Lemma TS, Thm TS(b) (Plan 69, REVIEWED on master) |
| Thm 1.4(iii) | UL.md Thm UP (b-part) and TAIL.md Prop UP-w (a-part split at 1 + p) (Plan 69, REVIEWED on master) |
| Cor 1.5 | UL.md Cor UL-3.10 + TAIL.md Thm TS(b) (all s > 1 at p = 1) |
| Conj 8.1, Rem 8.2 | SECOND §3.3 (CVX), UL.md Prop SV, Remark CVX-fin |
| Conj 8.3, 8.4 | PAPER_II_OUTLINE Conj 11.1, 11.2 (Paper 2 conj:tilt); SECOND §1.1 |

## 3. New arguments (Rule R done: REFEREE_PLAN71.md, all six ACCEPT)

1. **Theorem 4.4 (a-law), cross-scale step without Lemma TL.** The repo's Theorem Ra (G1 §3.12) takes windows
   [θn_i, n_i^γ] and controls the other windows along the path u(t) uniformly over the sandwich class, using Lemma TL.
   The draft instead linearises along the direct path ve^{tφ} with Lemma 2.16(iii) (= LRa, remainder evaluated at the
   pure power), takes windows [n_i/M₀, i·n_i] with n_{i+1} ≥ (i+1)²M₀n_i, and bounds all off-window and cross-window
   masses at the pure power by Cor 2.19 and Lemma 2.20 (shifts −1, 0, 1). This is the argument of G1 §3.10 remark RW-c
   transposed to the diagonal. Constants: ε ≤ 𝔦/16 and the conclusion εγ_a/2 are unchanged.
2. **Lemma 2.21 (polynomial tail) with a self-contained proof (decision D5).** Instead of citing the Markov and
   Chebyshev inequalities (no source read), the draft proves the weaker inequalities (2.12) from the Chebyshev
   expansion: max|P′| ≤ 2n³‖P‖ and |P(y)| ≤ 2(n+1)|T_n(y)|‖P‖. Consequences: T′ = ⌈16pn³⌉ (repo: ⌈8pn²⌉), constant
   68²(n+1)² (repo: 1156), and the deep-tail exponent bookkeeping changes.
3. **Lemma 2.22 exponent.** With Lemma 2.21's constants the all-M exponent is ϑ_* = (s−1)/(4 + (2+2/p)s), not TAIL.md's
   (s−1)/(s(1+2/p)+2). Only positivity, ϑ_* < min(p/2, s−1) and monotonicity in s are used. Check the arithmetic.
4. **φ′(0) = log c in Thm 6.5** is computed directly from the arcsine law (mean of log(1 + cos θ), via the mean value
   property of log|1+z| and dominated convergence), not identified through the Christoffel step as in UL.md. This
   avoids enlarging K beyond S_p (TAIL.md's K″ device is then unnecessary).
5. **Thm 1.3(iii) "no limit in [0, ∞]"**: the short Cesàro argument excluding L ∈ {0, ∞} is new (RW only excluded a
   positive limit).
6. **Remark 4.7 last sentence** (saturated indices carry no spectral weight) and Remark 3.6 (ρ_ℓ = O(1/log m) for
   1 + ½(−1)^k/log(k+1)) are one-line observations not in the repo.

## 4. Sources (Rule C) — what was read, and where

- **WLXZ** arXiv:1410.3948v1, §1 read in this session (PDF via pdftotext): (1.4) orthogonality with
  h_n = 2e^α/((n+α)n!); (1.5) jumps (k+α)^{k−1}e^{−k}/k! at ±x_k, x_k = (k+α)^{−1/2}, k ≥ 0; (1.6)
  (n+1)f_{n+1} − (n+α)x f_n + f_{n−1} = 0, f_0 = 1, f_1 = αx; (1.9) γ_n = Π_{k<n}(k+α)/(k+1). Used at α = 1 in
  Cor 5.5(a). (These quotes are recorded here because files outside papers/paperIII were not to be modified; copy them
  into research/G1/RH/CITATIONS.md when integrating.)
- **Fischer**, Z. Anal. Anwend. 17 (1998) 183–205, §4 read in this session (EMS Press PDF, OCR): Lemma 4 ("Let l be some
  positive linear functional on P_{2n−1}, differentiably depending on some parameter t, … The partial derivatives of the
  recursion coefficients with respect to t are" (20), (21)); Lemma 5 (derivatives w.r.t. a single node or weight). Cited
  only for the first-order formulas.
- **Simon** JAT 126 (2004): Thms 3.1, 3.2, Prop 3.3 — read per research/G1/CITATIONS.md (Simon). Cited for the
  path-counting method only.
- **DPQ** Prop 2.1 (statement read, research/G1/RH/CITATIONS.md); **DD** §1 (same file); **VA** §3 only through
  [II, Remark 1.6]; **DLMF** (5.11.1) and §5.11(ii) (same file, "DLMF"); **Monien**, **Haynes–Zudilin** cited for context
  only (as in Papers I and II).
- Bibliographic data for Simon, Fischer, DD (volume/pages) from Crossref (2026-10-15).
- **Not cited (not read):** Bingham–Goldie–Teugels, Vuilleumier (the smoothing lemma is proved in full, with no
  attribution claim), Markov/Chebyshev sources (replaced by (2.12)), Knopfmacher–Lubinsky–Nevai, Rakhmanov-type
  theorems, Teschl.

## 5. Placeholders

- `\tailbound` macro (main.tex) = [II, Proposition 8.6]; Plan 69 (TAIL.md) is now REVIEWED (master), and Paper II's
  numbering is not frozen. Statement imported (Prop 2.10): arcsine-range bound m_{n'}((Mn,∞)) ≤ CM^{−p/2},
  1 ≤ M ≤ c₂n^{2/p}, for 1 < s < 1+2p (all p) or p > 1 (all s). If the review fails for p ≤ 1 (fallback D2(b)):
  set S_p := ∅ for p ≤ 1 in (1.6); then Thm 1.4(ii)–(iii) hold for p > 1 only, Lemma 6.6 needs S_p ⊇ (1, 1+p] and
  becomes p > 1 only, and Cor 1.5 must be replaced by Cor 5.5(a) (s ∈ 3/2 + ℕ₀). The abstract sentences on uniformity
  and on "every s > 1" at p = 1 must then be cut.
- Paper II numbers used: Def 1.1, Thm 1.2, Cor 1.3, Thm 1.4, Rem 1.6, Lemmas 3.2–3.4, Thm 3.1, Section 3, Prop 8.6,
  Conj 11.1, 11.2 (from PAPER_II_OUTLINE.md §§2, 6). Re-check when II is frozen.
- Paper I numbers: Thm 1.1, Cor 1.2, Thm 1.3(i), Cor 1.4 (current papers/paper1). Paper I still writes u_s, ω_β; III
  uses u_sat, arc_β (SERIES §4; D11).
- Titles of Papers I/II in refs.bib; repository tag `v1.0-paper3`; date line.

## 6. Open items

1. Done (REFEREE_PLAN71.md): Rule R on §3 items 1–6 and on §§4–6 as paper text.
2. Done: Plan 69 REVIEWED (ACCEPT WITH FIXES, merged to master); the D2(b) fallback of §5 is not needed.
3. Done (REFEREE_PLAN71.md §C): re-verify the numerical values quoted in §7 and Remark 4.5 against the stored outputs
   (research/G1/checks/check_rw.out [1]–[3], check_ra.out [3]–[4] (via PROOF.md §3.12 Ra-c/Ra-e), check_t3_conv.out,
   check_sv_general.out [1]; research/G1/RH/second_order/checks/check_so_shift.out [A]–[D], check_ul.out [4],
   check_so_validate.out, check_so_convex.out). check_t3_conv was not K-doubled (stated as indicative in §7).
4. Lean sentence in §5: the formal statement is for discrete measures with bounded, strictly decreasing, non-negative
   atoms and a general scale s_n with s_n/s_{n+1} → 1; confirm the wording against lean/JacobiAsym/Christoffel.lean.
5. Novelty: Theorem 1.3 "not found" rests on research/program/novelty_lineB_C.md (one-session search). Lemma 2.16's
   second-order bounds likewise NOT FOUND there; the paper makes no novelty claim for them.
6. Style: run-in paragraph heads use \emph (as in Papers I and II); see STYLE_CHECK.md.
