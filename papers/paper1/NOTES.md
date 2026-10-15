# Paper 1 — notes (release candidate of 2026-10-15, Plan 63)

`main.tex` (amsart, 17 pages), `refs.bib`, `main.bbl` (tracked, for the arXiv bundle), `checks/`. Build:
`pdflatex main; bibtex main; pdflatex main; pdflatex main`. Author line is a placeholder ("Gordon [Surname]", user
decision: keep). arXiv bundle and placeholders: `ARXIV.md`. Final referee/editor pass: `REFEREE_FINAL.md` (Plan 63).

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
| Rem 3.6 | Monien's ρ = ρ* at p = 1 | G2 B* remark (reviewer's check). **Plan 63: now proved in the Remark** (substitution s = sin²φ, two lines); certified check `certified/c04_monien_density.py` | PROVED (unreviewed, elementary) + CERTIFIED at 11 points |
| Lemma 4.1 | discretisation | G2 Lemma A1. c₀ = 2 log 2 − 3/2 is evaluated here | PROVED + REVIEWED |
| Cor 4.2 | head bound | G2 Corollary A2 | PROVED |
| Thm 4.3 | upper bound ≤ E_p | G2 Theorem A-U = item 11 Lemma H7 with Cor A2 as the head input. **Change:** the tail factor is bounded directly from Heine (V(T) ≤ (Mn)^{−pm(m−1)}, Σ_T w(T) ≤ W^m) instead of by Hadamard's inequality, so no Hadamard citation is needed. The φ_M algebra is written out, with A = 4p + 2\|E_p\| | PROVED (+ REVIEWED in G2 form) |
| Lemma 5.1 | bathtub inequality | used implicitly in G2 A-L 3(a), 3(d) ("because ν ≤ Lebesgue"); proof written here | — |
| Thm 5.2 | lower bound ≥ κ_p | G2 Theorem A-L (steps 1–4, reviewer's scheme, re-check ACCEPT) | PROVED + REVIEWED, citation-free |
| §6 proof of Thm 1.1 | assembly; f′ < 0 and f bounded | G2 H_all proof | as H_all |
| Rem after Thm 1.1 | the limit L of f is arbitrary (translation invariance) | **NEW observation**, a direct consequence of Lemma 2.2(ii) | unreviewed |
| §7 Rem 7.2 | Baricz–Štampach closed forms, a = 2, b ∈ {−2, 0, 2} | research/program/novelty_G2.md §3 (quotes, arXiv PDF); closed forms CERTIFIED against direct determinants for n ≤ 30 (`certified/c03_zeta_hankel.py`); n = 10²…10⁵ statistic from `checks/bs_check.py`; the O(n log n) asymptotic derivation for b = 0 is new here | quotes: novelty agent; closed forms: CERTIFIED n ≤ 30; asymptotic statistic: NUMERICAL |
| §8 Tables 1–2 | numerics | Table 1 columns c(p), u_s, κ_p: `certified/c01_constants.py` (CERTIFIED correctly rounded); Monte Carlo column and Table 2: `research/G2/checks/check_energy.out`, `check_averaged.out`, `check_hz.out`. **Re-run 2026-10-15 (Plan 63); byte-identical**, as are `certified/c01, c03, c04` and `checks/*.py` | Table 1 cols 2–4 CERTIFIED; rest NUMERICAL |

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
| CCV | Coussement–Coussement–Van Assche, arXiv:math/0606440, Thm 1.3 | READ (PDF; novelty_G2) | heuristic remark in §1.2 |
| KVA-JAT | Kuijlaars–Van Assche, JAT 99 (1999) 167–197 | **NOT READ** (statement only via CCV Thm 1.3) | heuristic remark in §1.2 |
| KVA-PLMS | Kuijlaars–Van Assche, PLMS 79 (1999) 191–221 | **ABSTRACT ONLY** | framework sentence §1.2 |
| DragnevSaff | J. Anal. Math. 72 (1997) 223–259 | **ABSTRACT ONLY** (partly garbled on the page) | framework sentence §1.2 |
| Rakhmanov | Sb. Math. 187:8 (1996) 1213–1228 | **NOT READ** (only via the CDLO abstract) | framework sentence §1.2 |
| CDLO | Coroian–Dragnev–Legg–Orive, arXiv:2608.11987 | ABSTRACT | framework summary |
| VAVB | Van Assche–Van Baelen, arXiv:1910.12518, Constr. Approx. 2020 | abstract + intro. Volume/pages not recorded (bibtex warning "missing pages") | framework sentence §1.2 |
| Lai | arXiv:2610.06838 | READ (HTML; one sentence quoted) | context only |
| Fauzan | Zenodo 22826419 (2026) | **RECORD PAGE ONLY**; full manuscript "in preparation" | context only; the paper claims only logical independence |

Not cited although the repo mentions them: Saff–Totik, Cegrell–Kolodziej–Levenberg (behind BKMW; unread);
Beckermann 2000 and Zudilin 2017 (SEEN only); Carlitz / Tricomi–Carlitz and the Lommel family (item 11's p ∈ {1,2}
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
| 5 | Positioning: framework papers read only via abstracts; Beckermann 2000 unread | **Left open (needs library access).** Full texts of Rakhmanov 1996, Dragnev–Saff 1997, KVA PLMS/JAT 1999, Beckermann 2000 are paywalled and were not read. The paper keeps the visible hedge ("For the following works we have consulted only the abstracts…", "this statement is provisional"), which is accurate under Rule C. |
| 6 | Monien later publications | **Partly resolved.** Crossref search (2026-10-15, metadata only) found no journal version of arXiv:0901.1883 and no later Monien paper on this topic; together with the novelty report's OpenAlex check this is recorded, not proved absent. Bib entry now "Preprint, arXiv:0901.1883". |
| 7 | Fauzan manuscript | **Left open (external).** Unavailable; the paper claims only that no proof uses it and acknowledges possible overlap. Re-check before journal submission. |
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
- [ ] Read the full texts of DS 1997, KVA PLMS 1999, KVA JAT 1999 and Rakhmanov 1996 (and Beckermann 2000), then
      revise the framework paragraph and the "provisional" sentence (needs library access).
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

1. Full texts of Rakhmanov 1996, Dragnev–Saff 1997, Kuijlaars–Van Assche PLMS 1999 and JAT 1999, and Beckermann
   2000. Then confirm or retract the "provisional" no-prior-art sentence in §1.2 (the hedge stays visible until then).
2. Baricz–Štampach: the hedge in Rem 7.2 is now "statement numbers refer to the arXiv version" (which is what the
   novelty agent read); the closed forms used are CERTIFIED for n ≤ 30. Optional: compare numbering with the journal.
3. Re-verify every other quotation character by character: BKMW, Monien, Haynes–Zudilin, Coons–Sutherland, CCV,
   Lai and the Fauzan record.
4. Fauzan's full manuscript, when available.
5. refs.bib: done (no "to verify" fields left).
6. Supplementary material: create tag `v1.0-paper1` at submission and make the repository public (user).
