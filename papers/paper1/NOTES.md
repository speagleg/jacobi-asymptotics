# Paper 1 — notes (draft of 2026-10-14)

`main.tex` (amsart, 16 pages), `refs.bib`, `checks/`. Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main`.
Author line is a placeholder ("Gordon [surname] (draft)").

**Status.** DRAFT. The mathematics is research/G2 (PROVED-mod-cite (P) + REVIEWED, `research/G2/review/REVIEW_G2.md`)
plus the item 11 lemmas it uses, written out in full. Some steps of the paper are **new relative to the repo** (§2
below). They have had no Rule R review. Novelty: the paper says "we have not found … in the literature", never "new".
There is no RH framing anywhere.

---

## 1. Claim → source in the repo

Item 11 = `/mnt/c/Users/gspea/source/repos/math-pursuits/items/11-zero-measure-jacobi-asymptotics/work/proof/PROOF.md`
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
| Rem 3.6 | Monien's ρ = ρ* at p = 1 | G2 B* remark (reviewer's check); recomputed in `checks/monien_check.py` | NUMERICAL |
| Lemma 4.1 | discretisation | G2 Lemma A1. c₀ = 2 log 2 − 3/2 is evaluated here | PROVED + REVIEWED |
| Cor 4.2 | head bound | G2 Corollary A2 | PROVED |
| Thm 4.3 | upper bound ≤ E_p | G2 Theorem A-U = item 11 Lemma H7 with Cor A2 as the head input. **Change:** the tail factor is bounded directly from Heine (V(T) ≤ (Mn)^{−pm(m−1)}, Σ_T w(T) ≤ W^m) instead of by Hadamard's inequality, so no Hadamard citation is needed. The φ_M algebra is written out, with A = 4p + 2\|E_p\| | PROVED (+ REVIEWED in G2 form) |
| Lemma 5.1 | bathtub inequality | used implicitly in G2 A-L 3(a), 3(d) ("because ν ≤ Lebesgue"); proof written here | — |
| Thm 5.2 | lower bound ≥ κ_p | G2 Theorem A-L (steps 1–4, reviewer's scheme, re-check ACCEPT) | PROVED + REVIEWED, citation-free |
| §6 proof of Thm 1.1 | assembly; f′ < 0 and f bounded | G2 H_all proof | as H_all |
| Rem after Thm 1.1 | the limit L of f is arbitrary (translation invariance) | **NEW observation**, a direct consequence of Lemma 2.2(ii) | unreviewed |
| §7 Rem 7.2 | Baricz–Štampach closed forms, a = 2, b ∈ {−2, 0, 2} | research/program/novelty_G2.md §3 (quotes); recomputed in `checks/bs_check.py`; the O(n log n) asymptotic derivation for b = 0 is new here | quotes: novelty agent; numerics: NUMERICAL |
| §8 Tables 1–2 | numerics | `research/G2/checks/check_energy.out`, `check_averaged.out`, `check_hz.out`. **Re-run 2026-10-14; byte-identical** (PYTHONPATH = main repo `src`, which has the built `csrc/build/rkpw_*`; the worktree has no csrc build) | NUMERICAL |

**Which external input each result needs (paper version).** None. Lemma 3.3 replaces (P). If Lemma 3.3 fails review,
fall back to the repo version: Thm 1.3(iii) optimality and uniqueness, and hence the upper bound in Thm 1.1 / Cor 1.4,
become PROVED-mod-cite (P) (BKMW Lemma 2.1). In that case the mutual-energy finiteness in Thm 1.3(iii) should be cited
from (P) §1 again, or kept via U* ≥ const, which is independent of (P). The lower bound (Thm 5.2) is citation-free in
either version.

## 2. Material that is new relative to the repo (needs Rule R / expert check)

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
research/program/novelty_G2.md.

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

## 4. Numerics (Rule N: all NUMERICAL, none certified)

- Table 1: `research/G2/checks/check_energy.py` (re-run, identical).
- Table 2 and the HZ statistic and indexing in §8: `check_averaged.py`, `check_hz.py` (re-run, identical; about 1 min).
- Rem 3.6: `papers/paper1/checks/monien_check.py` → `.out` (mpmath dps 30). The max difference is 8.9e−31 over 11
  points. The mass check ∫ρ* = 1 is also there.
- Rem 7.2: `papers/paper1/checks/bs_check.py` → `.out` (mpmath dps 60/30, ~8 s).
- Lemma 3.3 sanity check: `papers/paper1/checks/positivity_sanity.py` → `.out`.
- Interpreter: `/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/.venv/bin/python` (`-I` for the paper's own
  scripts).

## 5. Open issues / places needing an expert check

1. Lemma 3.3 (new). An analyst should confirm it, or the paper should cite BKMW Lemma 2.1 and, behind it,
   Saff–Totik / Cegrell–Kolodziej–Levenberg, which have to be read first.
2. Thm 1.3(iii): the bilinear expansion with signed measures on an unbounded set. Absolute convergence of all three
   pieces is argued in the text; check it.
3. Thm 5.2 step 3: the case analysis (a)–(d) was re-derived during drafting and agrees with G2 (REVIEWED). The
   tex transcription itself (indices, the b > ½ case, the i = 1 block) has not had a second reader.
4. Error term. The theorem gives only o(n²); the numerics suggest O(n log n) for pure powers. This could be stated as
   a question.
5. Positioning.
   - The framework sentences rest on abstracts (§3 table). Read DS 1997, KVA PLMS 1999 and Rakhmanov 1996 in full and
     confirm that none of them contains the problem sup_𝒜 J_p (Lebesgue constraint on (0,∞), kernel
     log|u^{−p} − v^{−p}|).
   - Beckermann 2000 (Constr. Approx. 16) was not read.
6. Haynes–Zudilin attribute to Monien a rigorous (unpublished) treatment of r = 0. Check for later publications by
   Monien. The novelty search found none via OpenAlex.
7. Fauzan's manuscript. Re-check it once available. The paper currently claims only that its results are logically
   independent of it.
8. Author's own prior unpublished results (item 11 Theorem H: p ∈ {1, 2}, with O(n log n) error for exact pure
   powers). The paper does not mention them. Decide whether to mention them (e.g. as a remark that for p = 2 the
   Lommel family gives O(n log n)); citing them would need item 11's Lommel/Carlitz material.
9. The bibliographic details of VAVB (volume, pages) and the journal version of BKMW (if any) are not recorded.
   Check them.
10. Title is negotiable. The current title is the one requested.

## 6. Pre-submission checklist

- [ ] Fill in the author name, affiliation, email and MSC codes (suggest 15B05, 31A15, 42C05, 11M06; to confirm).
- [ ] Independent review (Rule R) of the new material in §2, especially Lemma 3.3.
- [ ] Read the full texts of DS 1997, KVA PLMS 1999, KVA JAT 1999 and Rakhmanov 1996 (and Beckermann 2000).
      Adjust the framework paragraph.
- [ ] Re-open BKMW, Monien, Haynes–Zudilin, Coons–Sutherland, Baricz–Štampach, CCV and Lai, and re-verify every
      quotation character by character (the drafting agent copied them from repo notes).
- [ ] Complete the bibliographic data (VAVB volume/pages; check whether the arXiv-only items have journal versions).
- [ ] Rerun the novelty search (Rule L) close to submission: arXiv/MathSciNet for "Hankel determinant" + "zeta" and
      for constrained equilibrium with accumulating nodes.
- [ ] Decide on the treatment of item 11 (see §5.8) and of the error term (§5.4).
- [ ] Remove the `% TO VERIFY` comments in main.tex once resolved.
- [ ] Recompile from clean (pdflatex, bibtex, pdflatex ×2) with no warnings except known bib gaps.
- [ ] Decide whether `checks/` is distributed as supplementary material (scripts rely on mpmath only, except the
      §8 tables, which need the repo toolkit and its C kernels).
