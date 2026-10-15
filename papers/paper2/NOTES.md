# Paper 2 — notes (draft of 2026-10-14)

Files: `main.tex` (shared preamble), `sec_front.tex` (chunk A: title, abstract, §1), `sec_2.tex`–`sec_8.tex`,
`app_*.tex` (chunks B–D), `sec_back.tex` (chunk A: §§9–10), `refs.bib` (chunk A), `checks/`.
Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main`. Author line is a placeholder ("Gordon [surname]
(draft)"). The binding contract is `OUTLINE.md`. This file records departures from it, sources, the citation gate and
the pre-submission checklist. Other chunks should append their own sections below.

---

## 1. Chunk A: claim → source

| Paper | Statement | Repo source | Repo label |
|---|---|---|---|
| Thm 1 (`thm:main`) | main theorem, statement verbatim from OUTLINE §2 | PROOF.md §3.21 B_all, §3.20 B_{p<1}, §3.23 B_{p=1}^{all} (+§3.19), rate re-ordered (OUTLINE §0 item 5) | PROVED-mod-cite, REVIEWED |
| Thm 2 (`thm:pure`) | pure powers, O(1/n) | THEOREMS.md H2; in the paper Thm 4 at Λ ≡ 0 + Thm 3 | PROVED-mod-cite, REVIEWED |
| Thm 3 (`thm:shift`) | Christoffel shift with rate | PROOF.md §3.21 SH, SH-r; ROUTE2_alpha §§2–4 | PROVED, REVIEWED |
| Thm 4 (`thm:engine`) | RH engine, base window | ROUTE2 §4.4 RII; ROUTE2_xframe1 §4 RII_x1; ROUTE2_plt1 §4.3 RII_{<1} | PROVED-mod-cite, REVIEWED |
| Def. `def:sv`, `def:smoothing`, `def:A` | slow variation (sequence form), ρ_ℓ, (A_ϑ) with ϑ_p | PROOF.md §3.14; ROUTE2 §1; (H_an), (H_an^{x1}), (H_an^{<1}) | — |
| §1.2 "(A_ϑ) ⇒ slowly varying" | one-line mean-value bound | written here | elementary |
| Rem `rem:pure-lommel` | closed form for σ_{2,2}: b_n = π²/((4n+1)√((4n−1)(4n+3))), a_n = 2π²/((4n+1)(4n+5)), n ≥ 1 | derived here from the Lommel recurrence quoted in novelty_G1RH §1.3 (Van Assche math/9510214 §3) by the quadratic transformation; checked in `checks/lommel_check.py` (90+ digits, n ≤ 9) and against Table 2 (p = 2, ℓ ≡ 1: all 4 digits, n ≤ 800) | NUMERICAL check; derivation not reviewed; **mass identification not checked against a source** (hedged in the text) |
| Rem `rem:shift-credit`, `rem:shift-converse` | credit DD §1, DPQ Prop. 2.1; rate part not found | novelty_lineB_A.md §§1–4 | — |
| §1.3 Context | positioning | novelty_lineB_A/B, novelty_G1RH, RESEARCH_PROGRAM §§1, 6; wording of OUTLINE §6.6 | — |
| §1.3 "log D_n changes by ≤ εn" | from Heine's formula (each term changes by a factor in [e^{−nε}, e^{nε}]) | Paper 1 Lemma 2.1 | elementary |
| §1.3 Paper 3 announcement | as OUTLINE §2 (no constants; not "the same weights") | THEOREMS.md H4 Theorem R, §2.6 Theorem Ra | PROVED-mod-cite, REVIEWED |
| §1.4 strategy | prose | ROUTE2 §2 (last paragraph), §3; OUTLINE §5 §1.4 | — |
| §9 Table (`tab:numerics`) | numerics | `checks/table2.py` → `checks/table2.out` (this chunk) | NUMERICAL |
| §10.1 Conjecture (`conj:tilt`) | 1/n term | ROUTE2 §5; xframe §5; ROUTE2_plt1 §6; RH_px §0 (pure power, translated, see §2 item 1 below) | CONJECTURE + NUMERICAL |
| §10.2 | other routes at p = 1 | ROUTE2_p1; xframe §0; PROOF.md §3.22 (REVIEW_Plan53 F1–F2); RH_px §4.1; RH_plt1b §2; xframe Lemma X2 | — |
| §10.4 | other nodes, α ≥ 1, zeta zeros | PROOF.md §4; ROUTE2 §6; outline_A_nodes.md §1 item 5 (not cited) | — |

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
| DY | arXiv:2104.03563v1 | OPENED (§1) by novelty agent | novelty_G1RH.md §2 | context (paraphrase; re-read before quoting) |
| DP | arXiv:2307.09277v2 | OPENED by novelty agent | novelty_lineB_B.md §§1–2 | context (quote "the crucial Theorem 4.7 in [4] requires a different proof") |
| Pio | arXiv:1910.00564v2 | OPENED | novelty_lineB_B.md §1 | context |
| Tro | arXiv:2412.18656v5 | OPENED | novelty_lineB_B.md §1 | context |
| MM | arXiv:0805.1980v1 | OPENED | novelty_lineB_B.md §1 | context |
| DIK | arXiv:0905.0443v3 §6.2 | OPENED | novelty_lineB_B.md §2(a) | context. **Title in refs.bib from memory: verify** |
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

## 6. Open TODOs (chunk A)

1. Second pass of §1.4 against the final lemma names and labels of chunks C and D (OUTLINE §8).
2. Re-read Dai–Yao §1 before quoting; re-verify all quotations character by character (CD abstract, DP §1).
3. Confirm the Lommel mass identification from a source (e.g. Dickinson 1954, or Van Assche's survey in full), or keep
   the hedge.
4. Re-check the equation number (5.5) of Conway–Deift cited in §10.1.
5. Fill the "to verify" bibliographic fields.
6. Decide on the zeta-zero sentence in §10.4 (coordinator).
7. Supplementary material: URL and commit hash (§9).

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
