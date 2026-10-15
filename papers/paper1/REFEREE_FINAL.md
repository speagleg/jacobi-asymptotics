# Paper 1: final referee, editor and consistency pass (Plan 63, 2026-10-15)

Reader: one agent acting as a hostile journal referee, then as an editor. This pass is **not** a Rule R second reading
(LLM self-review does not count for Rule R). The Rule R review is `REVIEW_Paper1.md` (2026-10-14, ACCEPT WITH FIXES,
F1–F15 applied). Scope: `main.tex` (the version on branch plan-63-paper1-release before this pass, commit 82cd0c1),
`refs.bib`, `checks/`, `certified/c01, c03, c04`, `research/G2/checks/check_{energy,averaged,hz}.out`, and the Lean
statements `paper1_thm11` (`lean/JacobiAsym/GeneralAtoms.lean`), `paper1_cor12`, `paper1_cor14`
(`lean/JacobiAsym/Paper1Corollaries.lean`) together with `lean/README.md`.

**Verdict.** No mathematical error found. One moderate issue: an identity was stated as fact while supported only
numerically (R1, now proved). The other findings are minor or editorial, and all are fixed. The strength of the
mathematical claims did not change, except that Remark 3.6 now proves an identity it previously only checked.

## 1. Findings and fixes

| # | Severity | Location | Finding | Fix |
|---|---|---|---|---|
| R1 | Moderate | §1.2 ("which coincides with the density ρ*") and Remark 3.6 | The paper asserted that Monien's density equals ρ* at p = 1, but supported this only with an mpmath check at 11 points. A referee would ask for a proof or a weaker wording. | Remark 3.6 now contains a two-line proof: B(3/2,1/2) = π/2, s = sin²φ gives (2/π)(φ − sin φ cos φ), with φ = arctan(1/√(2u−1)) and sin φ cos φ = √(2u−1)/(2u). I re-derived it. The numerical check is replaced by the certified Arb check `certified/c04_monien_density.py` (≤ 4.5·10⁻⁷⁴), cited only as a check. The claim is now stronger (proved instead of checked); this is justified by the proof. |
| R2 | Minor | Abstract | "atoms … regularly spaced with x_k ∼ Ck^{−p}" does not match Thm 1.1, which assumes f′(ξ) ∼ −pCξ^{−p−1} and allows any limit L (then x_k − L ∼ Ck^{−p}). Taken literally, x_k ∼ Ck^{−p} forces L = 0 and does not express the derivative condition. | The abstract now states x_k = f(k) with f′(ξ) ∼ −pCξ^{−p−1} (so x_k − lim x_j ∼ Ck^{−p}). It also mentions the Jacobi-coefficient form (Cor 1.2) and the Lean formalisation. No claim is changed. |
| R3 | Minor (numeric) | Remark 7.2 | "(n/log n) times it lies between −1.15 and −4.89". `checks/bs_check.out` has −4.89047 (ℓ = 2, n = 10⁵), which lies just outside that range. | Now "between −4.90 and −1.15". The script is cited. |
| R4 | Minor | Thm 5.2, Step 1 ("Constants C_U … depend on p and U only") | In Step 4, the O_U(n log n) term contains −\|s\| n log(U′n+1) and n log c₁, so it also depends on s and c₁. | "(in Step 4 also on c₁ and s)". |
| R5 | Minor | §8, Table 1 | The section said that all computations were "floating-point (not certified)". However, the columns c(p), u_s, κ_p and the §7 values 3a/2 + log c(a) are certified as correctly rounded by `certified/c01_constants.out`, which I compared entry by entry: all 21 table entries and the 4 values match. | §8 and the caption now say which entries are certified and which are not (the Monte Carlo column and Table 2 are floating-point). |
| R6 | Minor | Remark 7.2 | The visible hedge "remain to be re-checked against the published version" was about the BS numbering. The source that was read (by the novelty agent) is the arXiv PDF, and the closed forms are now certified for n ≤ 30 (c03, relative difference ≤ 3.2·10⁻¹⁵²). | The hedge now reads "Statement numbers refer to the arXiv version". The certified check (n ≤ 30) replaces the mpmath one (n ≤ 8). |
| R7 | Minor | §1.4 Formal verification | The section was accurate but incomplete. It did not name the Lean theorems, the Lean version or the axioms. It omitted that admissibility and saturation of μ*_u are formalised but the incomplete-beta density is not, and that the equality case of Lemma 3.3 is not formalised. It did not mention that Lemma 3.2 is proved by log-sine integrals. | The section has been rewritten and checked against `lean/README.md` and the statements of `paper1_thm11`, `paper1_cor12` and `paper1_cor14` (§4 below). |
| R8 | Minor (bibliography) | refs.bib | "to verify" fields: BKMW journal version; VAVB volume and pages; publication status of Monien, Coons–Sutherland and Lai. | Completed from arXiv API journal_ref/DOI and Crossref metadata (no source content read): BKMW = Constr. Approx. 37 (2013) 101–134; VAVB = 54 (2021) 117–144; CCV = Trans. AMS 360 (2008) 5571–5588. Monien, Coons–Sutherland, Lai and CDLO have no journal version in Crossref, so they are listed as "Preprint". Theorem numbers for BKMW and CCV are those of the arXiv versions read (stated in the notes). |
| R9 | Editorial | §1.2, §8, captions | The §8 sentence "repository URL and commit hash: to be supplied". The captions named scripts without paths. | §8 now cites https://github.com/speagleg/jacobi-asymptotics, tag `v1.0-paper1` as a visible placeholder (the tag is not created). It says that the Lean sources are in `lean/` and the certified checks in `certified/`. Captions and text give repository paths. |
| R10 | Editorial | Remark after Thm 1.3(iii) | "uses only parts (i) and the value" | "only part (i) and the value". |
| R11 | Editorial | Thm 1.3(iii) proof | Hard-coded "Section 3.1". | `\ref{sec:energies}`. |
| R12 | Editorial | Remark 7.1 | The sentence "which is how the expansion … reads it" was garbled. | Rewritten; same content. |
| R13 | Editorial | Front matter | No MSC or keywords; the author and date carried "draft". | Added `\subjclass[2020]{Primary 42C05; Secondary 15B05, 31A15, 11M06, 47B36}` and keywords. 15B52 (random matrices) was rejected as inappropriate. 15B05 (Toeplitz, Hankel …), 42C05 (orthogonal polynomials), 31A15 (potentials, energy problems), 11M06 (ζ) and 47B36 (Jacobi matrices, Cor 1.2) fit. The author is "Gordon [Surname]" (user decision). |
| R14 | Editorial | Layout | After the edits: an overfull line in the abstract (inline energy integral), the URL line, and a texttt path. Also an underfull caption and a 1.5 pt overfull vbox on p. 1. | The integral is displayed, the URL is centred, sentences were reflowed, `\emergencystretch` is set, and `\enlargethispage{4pt}` is used on p. 1. The final log has no Overfull, Underfull, undefined-reference or BibTeX warnings. |

## 2. Mathematical checks (re-derived, all correct)

- **§2.** Lemma 2.1: the multilinear expansion and the permutation sign. Lemma 2.2. Lemma 2.3: Cauchy MVT, ξ > k_i ≥ i,
  E_n = 2Σ(n−i)η(i) = o(n²) by Cesàro. Lemma 2.4: the P_{k−1} coefficient is h_k/h_{k−1}, the count n − j, and the
  1-based diagonal a_{k+1} (consistent with "a_n ∼ 2b_n" in §1.2). Lemma 2.5:
  ∫₁ⁿ(n−x)log x = (n²/2)log n − (3/4)n² + O(n), and the sum–integral error is O(n log n).
- **§3.**
  - Lemma 3.1, scaling: J_p(μ_τ) = τ²(J_p(μ) − pm² log τ).
  - Lemma 3.2: the product formula 2|cos θ − cos φ| = |2 sin((θ+φ)/2)||2 sin((θ−φ)/2)|, the cosine series, the bound
    (3.1) and |x − y| ≤ x + β.
  - Lemma 3.3: the Step 1 constants, the three exhaustive cases, Step 2 endpoints, dominated convergence, Fubini, and
    Gaussian uniqueness. This agrees with REVIEW_Paper1.md.
  - Thm 1.3(i): the substitutions t = t_x s and v = s^p; B(1/p+½, ½) = 2I(p); (4c)^{1/p} = π/(2I(p)); V = min(1, x/4c);
    u_s = 2I/π.
  - Thm 1.3(ii): ∫₀¹ log(c t^{−p}) dt = log c + p.
  - Thm 1.3(iii): ∬ log min(s,t) = ∫₀¹ 2(1−m) log m dm = −3/2. The three absolute energies are finite; the
    integrability of U* against |ν| justifies ∫U* dν = ∫(U* − log c − p)dν; ν ≤ 0 on (4c, ∞).
  - Monien's ρ = ρ* (new proof, R1).
- **§4.**
  - Lemma 4.1: D, Δ and Δ/D ≤ 1/(l−k−1); ϑ₀ = 2 log 2 − 3/2 (triangular density); the adjacent excess
    ≤ (p+1)log 2 − ϑ₀; the diagonal −3/2; |g′(k/n)| ≥ pM^{−p−1}; the harmonic count ≤ 1 + log n.
  - Cor 4.2: the exponent identity.
  - Thm 4.3: the cross bound (N!)^{−2pm}; V(T) ≤ (Mn)^{−pm(m−1)}; the log n coefficient −p(2mN + N² + m²) = −pn²; φ_M
    term by term; −(1−t)log(1−t) ≤ t; A = 4p + 2|E_p|; the N = 0 case; max(At − pt² log M) = A²/(4p log M).
- **§5.**
  - Lemma 5.1 (bathtub): signs.
  - Thm 5.2 Step 1: θ = (μ_U)_{1/m_U}, J_p(θ) = m_U^{−2}J_p(μ_U) + p log m_U, and d_U > 0.
  - Step 2: |B_i| ∈ [1/n, 1/(d_U n)], q-spacing ≥ 1/n, distinct k_i, u_i ≤ r_{i+1} for i ≤ n − 1 (used only for
    i < j), u_j ≤ (j+1)/(d_U n).
  - Step 3: (a) both cases i ≥ 2 and i = 1; (b) b < 1 because l_j = r_{j−1} ≥ r_{i+2}; the b ≤ ½ case including i = 1
    (l₁ = 0); the b > ½ identity b − a = (r_{i+1} − l_i)/l_j + (l_i/r_j)(r_j − l_j)/l_j ≤ 3/(d_U n l_j); the sums
    O(n log n); (c); (d), including p((n−1)log n − log(n−1)!) = O(n).
  - Step 4.
- **§6.** f′ < 0, f bounded, ρ = ξ^{p+1}f′/(−pC); positivity of all determinants; the Cor 1.2 bracket.
- **§7.**
  - Cor 1.4: reindexing and hypotheses; c(1) = ½, c(2) = π²/16; b > −1 and b > −3.
  - Remark 7.2: the b = 0 closed form, including the power of π, 2n(n+1); asymptotics with m = 2n+1; the
    O(n log n) effect of the ℓ = 0, 2 changes; the log(k + ½) versus log k difference, which is O(m log m).
- **Constants.** The abstract's c(p) equals (1.2). I(1) = π/4, c(1) = ½, I(2) = 1, c(2) = π²/16 (also sympy-exact in c01).

## 3. Citations (Rule C)

Every `\cite` in main.tex resolves to a refs.bib entry, and every entry is cited. I matched each quotation and
attributed statement against `research/G2/CITATIONS.md` and the novelty report (research/program/novelty_G2.md, local):

| Item | Record |
|---|---|
| Monien §1 "We do not know…" | (M) |
| Monien §3 "We seek…" | (M) |
| Monien Thm 3.1 formula | (M) |
| Monien Thm 2.1 as the multiple-sum formula | novelty §1(a), OPENED |
| HZ "for positive integers a and b, we expect…" | (HZ) |
| HZ "≤ −(a/2)…" | (HZ) |
| HZ "In [5] Monien…", [5] = personal communication | novelty §3 |
| Coons–Sutherland Thm 1.3 (faithful paraphrase) | novelty §1(c) |
| Lai sentence | novelty §3 |
| Fauzan record wording | novelty §3, record page only, hedged in the text |
| CDLO, DS, KVA-PLMS, VAVB | abstracts, hedged visibly |
| KVA-JAT via CCV Thm 1.3, with the corrected coefficient assignment | novelty §2(c) |
| BKMW Lemma 2.1 and (1.12) | (P) |
| BS Cor 3, Rem 5, (22) | novelty §3 (arXiv PDF) |

No claim relies on an unread source. The framework sentences carry a visible "abstracts only" hedge, and the
no-prior-art sentence is marked provisional. Not done: character-by-character re-verification against the original
PDFs (no source was re-opened in Plan 63). This remains on the NOTES §6 checklist.

## 4. §1.4 against the Lean statements

- `paper1_thm11` has these hypotheses: p > 0; C > 0; `HasDerivWithinAt f (f' ξ) (Ici 1) ξ` for ξ ≥ 1; f′
  continuous on [1,∞); ξ^{p+1}f′ → −pC; ∃ 0 < m ≤ ξ^{p+1}|f′| ≤ M on [1,∞); w ≥ 0, summable; w_k ≥ c₁(k+1)^{−s},
  c₁ > 0, s ∈ ℝ. These are exactly (1.3)–(1.4), 0-based. The conclusion is in terms of `(hankel …).det` with the
  Gamma-form constant 3p/2 + log((π/(2I(p)))^p/4) + log C, which is κ_p + log C.
- `paper1_cor12`: (2/n²)Σ_{j=1}^{n−1}(n−j) log(j^p √(b_j²)) → log(c(p)C).
- `paper1_cor14`: real a > 0, 2a + b > 1, Mathlib `riemannZeta` (real parts). The special cases are
  `paper1_cor14_one` and `_two`.
- Theorem 1.3 coverage:
  - `muStar_Ioc_le` / `_eq` give admissibility and saturation.
  - `starPot_eq` / `_ge` give part (ii).
  - `muStar_energy` gives the value.
  - `energy_pos` gives the inequality only.
  - `Jp_le_kappa` covers bounded support with integrable F_p.
  - Uniqueness, the equality case and the incomplete-beta formula are not formalised.
- Axioms: per lean/README.md, `check.sh` audits that only propext, Quot.sound and Classical.choice are used. I did
  not re-run Lean in this pass, since no Lean file changed.

§1.4 as rewritten states exactly this.

## 5. Numerics re-run (2026-10-15)

Re-run with jacobi-asymptotics/.venv/bin/python, and **byte-identical** to the stored outputs:
- `certified/c01_constants.py`, `c03_zeta_hankel.py`, `c04_monien_density.py`;
- `papers/paper1/checks/bs_check.py`, `monien_check.py`, `positivity_sanity.py`;
- `research/G2/checks/check_energy.py`, `check_averaged.py`, `check_hz.py` (PYTHONPATH = main repo `src`, with the C
  kernels).

Tables 1–2 and all numbers in §§7–8 were compared with these outputs. They match, including the K-doubling
differences 5.4·10⁻⁴, 2.8·10⁻⁵, 1.4·10⁻⁶, 7·10⁻⁸ (stored 7.1·10⁻⁸), and the p = 0.5 change of 1.1·10⁻².

## 6. Consistency pass

- Notation: c(p), I(p), κ_p, u_s, ρ*, μ*, μ*_u, 𝒥_p, 𝓛, E_p, σ_p, A, A_τ, ϑ, ϑ₀ and c₁ are used consistently. BKMW's
  I(μ) is distinguished from I(p) (Remark 3.4).
- All `\ref`/`\eqref` resolve, and there are no undefined references.
- Theorem numbering is unchanged, so the Lean and README cross-references (Thm 1.1, Lemma 3.2, 3.3, Thm 4.3, 5.2, …)
  remain valid.
- Title and abstract claim exactly Thm 1.1, Cor 1.2, Thm 1.3 and Cor 1.4. There is no RH/GRH framing. Novelty is
  phrased as "we have not found".
- Build: pdflatex, bibtex, pdflatex ×2 from clean gives 17 pages with no warnings. A standalone build from
  main.tex + main.bbl alone (scratch directory) gives the same PDF.
