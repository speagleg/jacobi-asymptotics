# Paper 1 — notes (release candidate of 2026-10-15, Plan 63; style revision Plan 68)

`main.tex` (amsart 10pt, 19 pages after Plan 68; 17 pages at 11pt with 1.15in margins before), `refs.bib`, `main.bbl` (tracked, for the arXiv bundle), `checks/`. Build:
`pdflatex main; bibtex main; pdflatex main; pdflatex main`. Author line is a placeholder ("Gordon [Surname]", user
decision: keep). arXiv bundle and placeholders: `ARXIV.md`. Final referee/editor pass: `REFEREE_FINAL.md` (Plan 63). Readability revision: §9 below (Plan 68).

**Status.** DRAFT, Rule R done: `REVIEW_Paper1.md` (2026-10-14) gives **ACCEPT WITH FIXES**, Lemma 3.3 **CORRECT**,
and no mathematical error. Fixes F1–F15 are applied (§7 below). The mathematics is research/G2 (PROVED-mod-cite (P) +
REVIEWED, `research/G2/review/REVIEW_G2.md`) plus the item 11 lemmas it uses, written out in full. The steps that are
new relative to the repo (§2 below) were re-derived by the Rule R reviewer. With Lemma 3.3 accepted, the paper's
proofs use no external theorem: PROVED + REVIEWED, at the level of one second reader. Novelty: the paper says "we have not found … in the literature", never "new".
There is no RH framing anywhere.

---

## 1. Claim → source in the repo

Item 11 = `math-pursuits/items/11-zero-measure-jacobi-asymptotics/work/proof/PROOF.md` (private notebook)
(read-only, §7). G2 = `research/G2/PROOF.md`.

| Paper | Statement | Repo source | Repo label |
|---|---|---|---|
| Thm 1.1 | log D_n asymptotics, every p > 0 | G2 Theorem H_all | PROVED-mod-cite (P) + REVIEWED |
| Cor 1.2 | double-Cesàro b_j form | G2 H_all "Equivalently" + item 11 H2 | as H_all |
| Thm 1.3 | explicit constrained maximiser | G2 Theorem B* (i)–(iii); the closed form dμ*/dσ = I_{min(1,x/4c)} is the reviewer's remark in G2 §1 | B*: PROVED-mod-cite (P) + REVIEWED; value citation-free |
| Cor 1.4 | det ζ(a(i+j)+b), real a > 0, 2a+b > 1 | G2 Corollary HZ | PROVED-mod-cite (P) + REVIEWED |
| Lemma 2.1 | Heine formula | item 11 Lemma H1 (one-line proof there; written out here) | PROVED |
| Lemma 2.2 | monotonicity, scaling, positivity | item 11 Lemma H3 (monotone, scaling). Translation invariance and positivity are added here and follow from Lemma 2.1 | PROVED |
| Lemma 2.3 | regular-spacing comparison | item 11 Lemma H4 (boundedness of f, h added for finite moments) | PROVED |
| Lemma 2.4 | D_n = m_0^n Π b_j^{2(n−j)} | item 11 Lemma H2 (proof sketched there; written out here) | PROVED |
| Lemma 2.5 | 2Σ(n−j) log j = n² log n − (3/2)n² + O(n log n) | used in item 11 §7 and G2 §3; proof written here | — |
| Lemma 3.1 | scaling of J_p | G2 §0 "Scaling" + A-L step 1 (mass-m version) | PROVED |
| Lemma 3.2 | arcsine potential | G2 Lemma B0. The bound (3.1) on ∫\|log\|x−y\|\| dω_β is new here; it replaces G2's "≤ C(1 + \|log x\| + log β_t)" | PROVED (B0); (3.1) NEW, unreviewed |
| Lemma 3.3 | positivity of the log energy of zero-mass signed measures (Fourier proof) | **NEW in the paper.** It replaces the external input (P) | unreviewed |
| Rem 3.4 | (P) quoted | research/G2/CITATIONS.md (P) | READ (2026-10-13) |
| Thm 1.3(iii) optimality | bilinear expansion | G2 B*(iii). Finiteness of the mutual energy is now derived from U* ≥ log c + p (Thm 1.3(ii)) instead of the (P) §1 remark | modified, unreviewed |
| Rem 3.5 | Monien's ρ = ρ* at p = 1 (Rem 3.6 before Plan 68) | G2 B* remark (reviewer's check). **Plan 63: proved in the Remark** (substitution v = sin²φ, two lines); certified check `certified/c04_monien_density.py` (no longer cited in the paper, Plan 68) | PROVED (unreviewed, elementary) + CERTIFIED at 11 points |
| Lemma 4.1 | discretisation | G2 Lemma A1. c₀ = 2 log 2 − 3/2 is evaluated here | PROVED + REVIEWED |
| Cor 4.2 | head bound | G2 Corollary A2 | PROVED |
| Thm 4.3 | upper bound ≤ E_p | G2 Theorem A-U = item 11 Lemma H7 with Cor A2 as the head input. **Change:** the tail factor is bounded directly from Heine (V(T) ≤ (Mn)^{−pm(m−1)}, Σ_T w(T) ≤ W^m) instead of by Hadamard's inequality, so no Hadamard citation is needed. The φ_M algebra is written out, with A = 4p + 2\|E_p\| | PROVED (+ REVIEWED in G2 form) |
| Lemma 5.1 | bathtub inequality | used implicitly in G2 A-L 3(a), 3(d) ("because ν ≤ Lebesgue"); proof written here | — |
| Thm 5.2 | lower bound ≥ κ_p | G2 Theorem A-L (steps 1–4, reviewer's scheme, re-check ACCEPT) | PROVED + REVIEWED, citation-free |
| §6 proof of Thm 1.1 | assembly; f′ < 0 and f bounded | G2 H_all proof | as H_all |
| Rem after Thm 1.1 | the limit L of f is arbitrary (translation invariance) | **NEW observation**, a direct consequence of Lemma 2.2(ii) | unreviewed |
| §7 Rem 7.2 | Baricz–Štampach closed forms, a = 2, b ∈ {−2, 0, 2} | research/program/novelty_G2.md §3 (quotes, arXiv PDF); closed forms CERTIFIED against direct determinants for n ≤ 30 (`certified/c03_zeta_hankel.py`); n = 10²…10⁵ statistic from `checks/bs_check.py`; the O(n log n) asymptotic derivation for b = 0 is new here | quotes: novelty agent; closed forms: CERTIFIED n ≤ 30; asymptotic statistic: NUMERICAL |
| §9 Tables 1–2 | numerics (§8 before Plan 68) | Table 1 columns c(p), u_s, κ_p: `certified/c01_constants.py` (CERTIFIED correctly rounded); Monte Carlo column and Table 2: `research/G2/checks/check_energy.out`, `check_averaged.out`, `check_hz.out`. **Re-run 2026-10-15 (Plan 63); byte-identical**, as are `certified/c01, c03, c04` and `checks/*.py` | Table 1 cols 2–4 CERTIFIED; rest NUMERICAL |

**Which external input each result needs (paper version).** None. Lemma 3.3 replaces (P). If Lemma 3.3 fails review,
fall back to the repo version: Thm 1.3(iii) optimality and uniqueness, and hence the upper bound in Thm 1.1 / Cor 1.4,
become PROVED-mod-cite (P) (BKMW Lemma 2.1). In that case the mutual-energy finiteness in Thm 1.3(iii) should be cited
from (P) §1 again, or kept via U* ≥ const, which is independent of (P). The lower bound (Thm 5.2) is citation-free in
either version.

## 2. Material that is new relative to the repo (Rule R: re-derived and accepted in REVIEW_Paper1.md)

1. **Lemma 3.3** (Fourier proof of energy positivity). The truncated kernel K_{ε,R}(a) = ∫_ε^R (cos aξ − e^{−ξ})/ξ dξ
   gives the bound |K| ≤ |log|a|| + 6 (three cases) and the pointwise limit k₀ − log|a|. Dominated convergence on
   |ν|⊗|ν| and Fubini on [ε,R] then give the identity. Uniqueness: Fourier uniqueness via Gaussian smoothing.
   - Sanity check: `checks/positivity_sanity.py` (ν = ω_[0,1] − Unif[0,1]; energy side log(1/4) + 3/2 = 0.1137056).
     The Fourier side agrees to 1.4e−5, which is quadrature error and not a bound. A truncation at X = 2000 plus the
     asymptotic tail 2/(πX) gave 0.1137172 (scratch).
   - Points to check:
     - the constants in Step 1;
     - that the diagonal is |ν|⊗|ν|-null;
     - the passage from "∫ψ dν = 0 for bounded continuous ψ" to ν = 0.
2. **Bound (3.1)**: ∫|log|x−y|| dω_β ≤ 2 log(1+x+β) + |log(β/4)|, from |t| = 2t⁺ − t and U_β ≥ log(β/4). It is used
   for the Fubini steps in Thm 1.3(ii), (iii).
3. **Mutual-energy finiteness** in Thm 1.3(iii), via U* ≥ log c + p (no (P) §1 needed).
4. **Tail bound without Hadamard** in Thm 4.3.
5. **Translation remark**: f need not tend to 0.
6. **Closed-form asymptotics for a = 2, b = 0** (Rem 7.2): log det ζ(2(i+j)) = −2n² log n + (3 + log(π²/16))n² + O(n log n),
   derived from the BS closed form. The identity 2n(n+1) log(π/2) + Σ_{k=1}^{2n}(k−2n−1) log(k+½) was checked against
   direct determinants (n ≤ 8, ≥ 38 digits).
7. **Correction to novelty_G2.md §2(c).** The novelty report applies the KVA theorem with "a(t) = 2c t^{−p},
   b(t) = c t^{−p}". In KVA's convention (a = off-diagonal, b = diagonal, γ = b − 2a, δ = b + 2a) this gives the
   wrong interval [−3ct^{−p}, 5ct^{−p}]. The correct assignment is a(t) = c t^{−p} (off-diagonal) and
   b(t) = 2c t^{−p} (diagonal), which gives [0, 4ct^{−p}]. The paper (§1.2, "Averaged arcsine laws") uses the
   correct assignment. The remark is heuristic and not used in any proof.

## 3. External citations and read status

"Read" here means read by an agent of this project, with quotes recorded in the repo. The drafting agent did **not**
re-open any external source; all quotations in main.tex are copied from research/G2/CITATIONS.md or
research/program/novelty_G2.md. Plan 63 (2026-10-15) checked every quotation and every \cite in main.tex against
those records (REFEREE_FINAL.md §3) and fetched only bibliographic metadata (arXiv API journal_ref/DOI, Crossref); no
source content was read in Plan 63, and no read status below changed.

| Key | Source | Read status (per repo) | Used for |
|---|---|---|---|
| BKMW | Beckermann–Kalyagin–Matos–Wielonsky, arXiv:1105.3088v2, Lemma 2.1, (1.12) | READ (§1, §2 of the arXiv PDF), CITATIONS.md (P). Lemma 2.1's own proof refers to Saff–Totik Lemma I.1.8 and Cegrell–Kolodziej–Levenberg Thm 2.5, **neither read** | Rem 3.4 only (alternative to Lemma 3.3) |
| Monien | arXiv:0901.1883v1, §1, §3, Thm 3.1 | READ (PDF + ar5iv). "Thm 2.1 = multiple-sum formula" is from novelty_G2 §1(a) | context, Rem 3.6, Rem 7.1 |
| HaynesZudilin | SIGMA 11 (2015) 101, arXiv:1510.01901v3, §1 | READ §1 + bibliography (CITATIONS.md (HZ), novelty_G2) | context |
| CoonsSutherland | arXiv:1404.2699, Thm 1.3 | READ (PDF; novelty_G2) | context |
| BariczStampach | LAA 548 (2018) 259–272, arXiv:1708.07729, Cor 3, Rem 5, (22) | READ (PDF) by the novelty agent. ℓ = 3 (b = 4) formula unverified there and not used. The formulas used are independently confirmed numerically (`checks/bs_check.py`) | Rem 7.2 |
| CCV | Coussement–Coussement–Van Assche, arXiv:math/0606440, Thm 1.3 | READ (PDF; novelty_G2) | **no longer cited** (Plan 68: KVA-JAT read directly) |
| KVA-JAT | Kuijlaars–Van Assche, JAT 99 (1999) 167–197 | **READ** (Plan 68; authors' manuscript, §1, Thm 1.4; CITATIONS.md) | heuristic remark in §1.2 |
| KVA-PLMS | Kuijlaars–Van Assche, PLMS 79 (1999) 191–221 | **READ** (Plan 68; authors' manuscript, §§1–2, Thms 2.1, 2.2) | literature paragraph §1.2 |
| DragnevSaff | J. Anal. Math. 72 (1997) 223–259 | **READ** (Plan 68; journal scan, §§1–3, Def 1.2, Thms 2.1, 2.6, 3.3) | literature paragraph §1.2 |
| Rakhmanov | Sb. Math. 187:8 (1996) 1213–1228 | **READ** (Plan 68; English journal PDF, §§1–4, Thms 1–3) | literature paragraph §1.2 |
| Beckermann | Constr. Approx. 16 (2000) 427–448 | **READ** (Plan 68; author's manuscript of 26 March 1999, §1, Thm 1.3) | one clause in §1.2 |
| CDLO | Coroian–Dragnev–Legg–Orive, arXiv:2608.11987 | ABSTRACT | **no longer cited** (Plan 68) |
| VAVB | Van Assche–Van Baelen, arXiv:1910.12518, Constr. Approx. 54 (2021) 117–144 | **READ** (Plan 68; arXiv v1, §§1–2, Thm 2.2) | literature paragraph §1.2 |
| Lai | arXiv:2610.06838 | READ (HTML; one sentence quoted) | **no longer cited** (Plan 68, audit §2.2) |
| Fauzan | Zenodo 22826419 (2026) | **RECORD PAGE ONLY** | **no longer cited** (Plan 68, audit §2.2, D10) |
| PaperII, PaperIII | companion papers | — | forward pointer at the end of §1.2; "In preparation" placeholders |

Not cited although the repo mentions them: Saff–Totik, Cegrell–Kolodziej–Levenberg (behind BKMW; unread);
Zudilin 2017 (SEEN only); Carlitz / Tricomi–Carlitz and the Lommel family (item 11's p ∈ {1,2}
route, not needed here).

## 4. Numerics (Rule N; certified items marked)

- Table 1: `research/G2/checks/check_energy.py` (re-run, identical).
- Table 2 and the HZ statistic and indexing in §8: `check_averaged.py`, `check_hz.py` (re-run, identical; about 1 min).
- Rem 3.6: the identity is now proved in the Remark; the paper cites the certified check
  `certified/c04_monien_density.py` (≤ 4.5e−74 at 11 points). `papers/paper1/checks/monien_check.py` (mpmath dps 30,
  max difference 8.9e−31, plus the mass check ∫ρ* = 1) is kept but no longer cited.
- Table 1 columns 2–4 and the §7 values 3a/2 + log c(a): `certified/c01_constants.py` (correct rounding, Arb).
- Rem 7.2: closed forms vs direct determinants: `certified/c03_zeta_hankel.py` (n ≤ 30, cited). The asymptotic
  statistic at n = 10²…10⁵: `papers/paper1/checks/bs_check.py` → `.out` (mpmath dps 60/30, ~8 s; cited).
- Lemma 3.3 sanity check: `papers/paper1/checks/positivity_sanity.py` → `.out`.
- Interpreter: `.venv/bin/python` (repo root) (`-I` for the paper's own
  scripts).

## 5. Open items: status after Plan 63 (2026-10-15)

| # | Item | Status |
|---|---|---|
| 1 | Lemma 3.3 needs a human analyst's check | **Left open (needs a human).** Rule R (agent) accepted it; the inequality part is also machine-checked in Lean (`energy_pos`, Gaussian-kernel route), which covers everything Thm 1.1 uses. The Fourier identity and the equality case are not formalised. Fallback via BKMW still needs Saff–Totik / Cegrell–Kolodziej–Levenberg to be read. |
| 2 | Thm 1.3(iii) bilinear expansion on an unbounded set | **Resolved.** Re-derived line by line in REFEREE_FINAL.md (absolute convergence of the three energies, |ν| ≤ μ^x + μ*, sign of the middle term); Lean `Jp_le_kappa` proves the bounded-support case used by Thm 1.1. |
| 3 | Thm 5.2 step 3 transcription (indices, b > ½ case, i = 1 block) not second-read | **Resolved (agent referee, Plan 63).** Every inequality of Steps 1–4 re-derived (REFEREE_FINAL.md §2); Lean `quantile_lower`, `hall_lower` prove the same lower bound independently. Only fix: O_U also depends on c₁, s in Step 4 (stated now). |
| 4 | Error term o(n²) only | **Left as is (deliberate).** The paper states that numerics are consistent with O(n log n) for pure powers (Remark after Cor 1.2). Not posed as a formal question; no claim strengthened. |
| 5 | Positioning: framework papers read only via abstracts; Beckermann 2000 unread | **Resolved (Plan 68).** All five read from open copies (CITATIONS.md); §1.2 rewritten with theorem numbers; hedges removed. Superseded text follows: **Left open (needs library access).** Full texts of Rakhmanov 1996, Dragnev–Saff 1997, KVA PLMS/JAT 1999, Beckermann 2000 are paywalled and were not read. The paper keeps the visible hedge ("For the following works we have consulted only the abstracts…", "this statement is provisional"), which is accurate under Rule C. |
| 6 | Monien later publications | **Partly resolved.** Crossref search (2026-10-15, metadata only) found no journal version of arXiv:0901.1883 and no later Monien paper on this topic; together with the novelty report's OpenAlex check this is recorded, not proved absent. Bib entry now "Preprint, arXiv:0901.1883". |
| 7 | Fauzan manuscript | **Moot (Plan 68): paragraph and citation dropped.** Earlier: **Left open (external).** Unavailable; the paper claims only that no proof uses it and acknowledges possible overlap. Re-check before journal submission. |
| 8 | Mention item 11's p ∈ {1,2} results? | **Decided: not mentioned.** They are unpublished, superseded by Thm 1.1 (except the O(n log n) rate for exact Lommel families, which the paper does not claim), and citing them would need the Lommel/Carlitz material. User may override. |
| 9 | Bibliographic details (VAVB, BKMW journal version, statuses) | **Resolved** from arXiv API journal_ref/DOI and Crossref metadata (2026-10-15): BKMW = Constr. Approx. 37 (2013) 101–134; VAVB = Constr. Approx. 54 (2021) 117–144; CCV = Trans. AMS 360 (2008) 5571–5588; HZ = SIGMA 11 (2015) 101, 5 pp.; BS = LAA 548 (2018) 259–272. Monien, Coons–Sutherland, Lai, CDLO: no journal version found → "Preprint". Theorem numbers for BKMW, CCV, BS are those of the arXiv versions that were read (stated in refs.bib / Rem 7.2). No content was read in this step. |
| 10 | Title | **Kept.** Consistent with what is proved (Thm 1.1 + Cor 1.4). |

## 6. Pre-submission checklist

- [ ] Fill in the author surname (placeholder "Gordon [Surname]"; user decision to keep for now); optionally address/email.
- [x] MSC 2020 and keywords in the front matter (Primary 42C05; Secondary 15B05, 31A15, 11M06, 47B36). 15B52 (random
      matrices) was considered and rejected; 15B05 covers Hankel matrices.
- [x] Independent review (Rule R) of the new material in §2, especially Lemma 3.3 (REVIEW_Paper1.md: CORRECT).
- [x] Final referee + editor + consistency pass (REFEREE_FINAL.md, Plan 63; agent, not a Rule R second reader).
- [ ] Optional: a human analyst's check of Lemma 3.3 (the Rule R reader was an agent).
- [x] Read the full texts of DS 1997, KVA PLMS 1999, KVA JAT 1999 and Rakhmanov 1996 (and Beckermann 2000), then
      revise the framework paragraph and the "provisional" sentence (Plan 68).
- [ ] Re-open BKMW, Monien, Haynes–Zudilin, Coons–Sutherland, Baricz–Štampach, CCV and Lai, and re-verify every
      quotation character by character (still copied from repo notes; not re-opened in Plan 63).
- [x] Complete the bibliographic data (Plan 63, from arXiv/Crossref metadata).
- [ ] Rerun the novelty search (Rule L) close to submission.
- [x] Decide on item 11 (not mentioned) and the error term (remark only) — see §5.
- [x] Supplementary-material sentence: https://github.com/speagleg/jacobi-asymptotics, tag `v1.0-paper1` marked as a
      placeholder (the tag is **not** created; create it at submission and the repo must be public by then).
- [x] Recompile from clean (pdflatex, bibtex, pdflatex ×2): no warnings, no overfull boxes; standalone build from
      main.tex + main.bbl checked.
- [x] `checks/` and the scripts behind the tables are distributed via the public repository (not in the arXiv bundle).

## 7. Rule R fixes applied (REVIEW_Paper1.md, 2026-10-14)

| # | Fix |
|---|---|
| F1 | Thm 1.3(iii): "Since \|ν\| ≤ μ^x + μ*, the three bullets give ∬\|log\| d\|ν\|d\|ν\| < ∞". |
| F2 | Lemma 3.3: (a) is now 2/A; k₀ = 0 is noted as not needed; limits are taken along sequences (ε_m, R_m). |
| F3 | Rem 3.4: only the positivity statement is a special case of BKMW. Added the argument that ν^± ∈ M(ℂ) (equal mass, finite energy, log moment by fixing a typical y). |
| F4 | Sign convention. The abstract now speaks of minimising the standard energy ∬log(1/\|·\|). §1.2 says −J_p is the energy of g_*μ. Thm 1.3(ii) names U* as the negative of the logarithmic potential. |
| F5 | Rem 7.2: the range is now "between −1.15 and −4.89" (matches bs_check.out). |
| F6 | Rem 7.2: one paragraph showing that the ℓ = 0, 2 closed forms differ from ℓ = 1 only by O(n log n), so b = −2, 2 follow too. |
| F7 | §1.2: visible hedge ("We have only consulted the abstracts…"; the no-prior-art sentence is marked "provisional"). Rem 7.2 has a visible hedge on the BS quotation and numbering. The LaTeX "% TO VERIFY" comments are removed. No new sources were fetched or read. |
| F8 | §1.2: Fauzan is described as an unrefereed Zenodo announcement. The record's "positive moment representation and a logarithmic-energy estimate" wording is quoted, and the possible overlap with Thm 1.3 is acknowledged. The paper states that no proof uses Fauzan or Lai. |
| F9 | Dated correction note added to research/program/novelty_G2.md §2(c) (separate commit 90f3be9). |
| F10 | §1.2 and Rem 7.1: Monien's "∼" is read with an o(n²) error, per Zagier's expansion; the literal reading is noted. |
| F11 | §8 and table captions: "supplementary material (repository URL and commit hash: to be supplied)" replaces repo paths. |
| F12 | §8: the p = 1.5, n = 1600 entry is flagged as indicative (K-doubling change ≈ 20%). |
| F13 | refs.bib: unknown fields are marked "to verify" (BKMW journal version; VAVB volume/pages; publication status of Monien, Coons–Sutherland, Lai; Fauzan as an unrefereed announcement). No bibliographic data was invented. |
| F14 | (i) "for i ≤ n−1" in Thm 5.2 step 2; (ii) the mixture μ*(B) = ∫ω(B)dt is defined in Thm 1.3 and §3.4; (iii) the weight scale is now ϑ, c₀ is now ϑ₀, and BKMW's I(μ) is distinguished from I(p); (iv) a remark that the sup in (1.3) is redundant. |
| F15 | papers/paper1/.gitignore covers the LaTeX build products. |

## 8. Visible "to verify" list (pre-submission), after Plan 63

1. Done (Plan 68): all five read; the "provisional" sentence is replaced by "We have not found the problem sup_A J_p
   or its solution in the works cited here." Optional: compare KVA and Beckermann theorem numbers (authors'
   manuscripts) with the journal versions.
2. Baricz–Štampach: the hedge in Rem 7.2 is now "statement numbers refer to the arXiv version" (which is what the
   novelty agent read); the closed forms used are CERTIFIED for n ≤ 30. Optional: compare numbering with the journal.
3. Re-verify the remaining quotations character by character: Monien (§1.2, one quote) and Haynes–Zudilin (§1.2,
   one quote). BKMW, Coons–Sutherland, Baricz–Štampach and Monien §3 are now paraphrased (Plan 68), not quoted.
4. (Dropped, Plan 68: Fauzan no longer cited.)
5. refs.bib: done (no "to verify" fields left).
6. Supplementary material: create tag `v1.0-paper1` at submission and make the repository public (user).

## 9. Plan 68 readability revision (2026-10-15)

Applied `research/program/papers_split/PAPER_I_AUDIT.md` (local, unpublished) against the style guide, and the shared
notation of `SERIES.md` (decision D11). No mathematical statement changed in strength; no proof step changed.

| Audit item | Change |
|---|---|
| §2.1 repo paths/process | All script paths, directory names and "re-run" sentences removed from the body and captions. §9 opens with one sentence on precision ("Columns 2–4 of Table 1 … correctly rounded (ball arithmetic); all other entries are floating-point"). The ball-arithmetic check of the Baricz–Štampach closed forms (n ≤ 30) stays in Rem 7.2 without a path; the Arb check sentence in Rem 3.5 (Monien) is deleted. URL, tag placeholder and Lean theorem names now sit only in the new "Data and code availability" statement. |
| §2.2 hedging / unread sources | Literature read (CITATIONS.md, Plan 68 section): Rakhmanov, Dragnev–Saff, KVA-PLMS, KVA-JAT, Beckermann, VAVB. §1.2 "The equilibrium problem" rewritten with theorem numbers; "abstracts only" and "provisional" sentences removed; novelty sentence now "We have not found … in the works cited here". Fauzan/Lai paragraph dropped. "(closed forms confirmed independently)" and the BS numbering hedge shortened to "(numbering of the arXiv version …)". |
| §2.3 repetition | Role of Lemma 3.3 stated once (§1.3 Method); unlabelled remark after Thm 1.3(iii), "Note that only the value…" (§4) and the closing sentence of §5 deleted. Monien's "∼" discussed only in Rem 7.1. |
| §2.4 notation | a_{k+1} → a_k (Lemma 2.4); σ_p → λ_p; u_s → u_sat (macro \usat); ω_β → arc_β (macro \arc), one subscript form; 𝓑_V(α,γ) → 𝓑_y(a′,b′) with Euler B(a′,b′); integration variable s → r (Thm 1.3(i), (iii), Lemma 3.2 proof) and v (Rem 3.5); Rem 7.2 paraphrases BS with R_{2m}(ν) and index j ∈ {0,1,2}. |
| §2.5.1 intro length | 10pt amsart default layout (geometry removed): intro runs from mid p. 1 to the top of p. 5, about 3.7 pp. Monien's formula moved from §1.2 into Rem 3.5; Coons–Sutherland and Monien §3 paraphrased. |
| §2.5.2 openers | 2–4 sentence openers added to §§2–7. |
| §2.5.3 outlines | Strategy paragraphs open the proofs of Lemma 3.3, Thm 4.3 and Thm 5.2. |
| §2.5.4 Rem 3.4 | Cut to five lines (paraphrase, no quotation). |
| §2.5.5 numerics in Rem 6.1 | The "consistent with O(n log n)" sentence moved to §9 (Rem 6.1 now labelled rem:rate). |
| §2.5.6 lists | The b ≤ ½ / b > ½ case analysis in Thm 5.2(b) is two paragraphs. |
| §2.5.7 forward pointer | End of §1.2 points to [II], [III] ("In preparation" bib placeholders). |
| §2.5.8 / §3.1 | New §8 "Formal verification" (old §1.4); intro keeps one sentence. Acknowledgements (one sentence: AI assistance, Claude/Anthropic; Lean verification; author responsibility) and Data and code availability (URL, tag placeholder, Lean theorem names) before the bibliography. |
| §2.6 LaTeX | booktabs → \hline; geometry and \enlargethispage removed; class option 11pt → default 10pt; abstract without displays (1225 characters plain; ARXIV.md updated). Long displays split (gather/align/multline); 0 overfull boxes. |
| §2.6 bibliography | Dropped CDLO, CCV, Lai, Fauzan; added Beckermann, PaperII, PaperIII; numbering notes for KVA-PLMS, KVA-JAT, Beckermann (authors' manuscripts) and VAVB (arXiv). |
| §3.3 organisation | Organisation paragraph covers §§8–9 and says §3 can be read on its own. |
| D14 | Title unchanged; author placeholder unchanged. |

New in the text (our own remark, elementary, not reviewed): μ* is the law of SY with Y ~ arc_{4c(p)}, S = T^{−p}, T
uniform on (0,1) independent of Y (immediate from μ* = ∫_0^1 arc_{4ct^{−p}} dt since arc_β is the law of βY/(4c)).
Section and remark numbers that moved: Rem 3.6 → 3.5 (Monien); old §1.4 → §8; numerics §8 → §9.

