# Paper I: independent referee and editor pass on the Plan 68 revision

Reviewed: branch `plan-68-paper1-style` at 18e815d (base `master`), `papers/paper1/main.tex` and `refs.bib`, against
`research/program/paper_style.md`, `research/program/papers_split/PAPER_I_AUDIT.md`, AGENTS.md and
VERIFICATION_POLICY.md. Date: 2026-10-15.

**Verdict.** No critical or major issues. The mathematics is unchanged. The new product-structure sentence is correct.
The literature paragraph matches CITATIONS.md "Plan 68", and three sources were re-fetched and confirmed. The forward
pointer to the unposted companion papers has been replaced, and the remaining minor and editorial points are applied
(list in §6). Build: 19 pp., 0 warnings, 0 overfull or underfull boxes, 0 undefined references, both in place and
from `main.tex` + `main.bbl` alone.

Severity scale: critical (wrong mathematics or a false claim), major (an unsupported claim or a hypothesis gap that
needs the author), minor (imprecision a referee would query), editorial (wording, notation, layout).

---

## 1. Mathematics unchanged (`git diff master..HEAD -- papers/paper1/main.tex`)

I checked every hunk. No theorem, lemma or corollary statement, hypothesis, constant or proof step changed in substance.
The non-notation changes are layout only: displays split with `align`/`multline`/`gather`, `\qedhere`, the two-case
list in Theorem 5.2(b) turned into two paragraphs, and Lemma 3.3's definition of the Fourier transform moved out of the
display. Also removed or moved without changing any content: the repeated remark on the role of Lemma 3.3, the
"Note that only E_p enters" sentence, the duplicate lower-bound sentence, Monien's formula (from §1.2 into
Remark 3.5), and the floating-point statistic (from Remark 7.2 into §9). The shortened Remark 3.4 (BKMW) is still
accurate. The new proof outlines (Lemma 3.3, Theorems 4.3 and 5.2) and section openers agree with the proofs. Two
wording points in them are fixed in §6 (E3, E4).

Renames, checked by grep for leftovers (`\omega`, `\sigma_p`, `u_s`, `\cB_V`, `a_{k+1}`, `\ell`, `ds`):

| Rename | Status |
|---|---|
| a_{k+1} → a_k in Lemma 2.4 | Consistent. `a_k` appears nowhere else except the heuristic "a_n ∼ 2b_n" in §1.2, which matches the new convention (diagonal a_k paired with P_k) and the KVA-JAT mapping ψ = 2φ. The proof of Lemma 2.4 never uses a_k. |
| σ_p → λ_p | Complete (§3.1, proof of Thm 1.3(i), (iii), §9). |
| u_s → u_sat | Complete (Thm 1.3, proof (i), Remark 3.5, §§8–9, Table 1). |
| ω_β → arc_β | Complete, and there is one subscript form throughout (the old ω_{[0,4ct^{−p}]} is gone). |
| 𝓑_V(α,γ) → 𝓑_y(a′,b′) | Complete, **but y clashed** (editorial, fixed, E1). |
| s → r/v as an integration variable | Complete (Lemma 3.2 proof, Thm 1.3(i), (iii), Remark 3.5). The remaining `s` are the weight exponent only. |
| σ_{2m}(ν), ℓ → R_{2m}(ν), j (Remark 7.2) | Consistent. Matrix indices (i,i′), exponent of π 2Σ(2i+j−1), range 2n+j−1 and b = 2j−2 all agree with the old text. |

## 2. New product-structure sentence (§1.2): μ* is the law of SY

**Correct.** arc_β is the law of βZ with Z ~ arc_1, so arc_{4ct^{−p}} is the law of t^{−p}Y with Y ~ arc_{4c}. Mixing
over t uniform on (0,1), with T independent of Y, gives μ*(B) = ∫_0^1 P(t^{−p}Y ∈ B) dt = P(T^{−p}Y ∈ B). This is
exactly the definition of μ* in Theorem 1.3. The comparison with [KVA-PLMS] is fair: there the extremal measure is
the Mellin convolution b_α * ω_{[A,B]}, i.e. the law of a product of independent scale and arcsine variables. Here
S = T^{−p} has density (1/p)s^{−1−1/p} on [1,∞).
- *Editorial (applied, E2):* the text said "The maximiser has the same structure", but the maximiser is μ*_u and the
  statement is about μ* (the x-variable). Now: "In the variable x our solution has the same product structure as in
  [KVA-PLMS]: μ* is the law of SY …".

## 3. Literature (§1.2)

Each statement was checked against CITATIONS.md "Plan 68". Three sources were re-fetched and checked by me:

| Source | Fetched from | Confirmed |
|---|---|---|
| Rakhmanov 1996 | mathnet.ru sm153, English full text (16 pp.) | Thm 1: discrete Chebyshev T_{n,N}, n/N → c ∈ (0,1), zero distribution f_c dx. Thm 2: weighted L_p-extremal polynomials on N_n separated points with (1/n)Σδ → σ. Thm 3: σ on [−1,1] with continuous potential and \|σ\| > 1, constrained equilibrium characterised by conditions (i)–(vi). The paper's three attributions are accurate. The constrained problem of Thm 3 has no external field, so "Dragnev and Saff added an external field" is fair. |
| Kuijlaars–Van Assche, JAT 1999 | wis.kuleuven.be/analyse/members/walter/varrec.pdf | Thm 1.4 verbatim: x p_{n,N} = a_{n+1,N}p_{n+1,N} + b_{n,N}p_{n,N} + a_{n,N}p_{n−1,N}; continuous a: (0,∞) → [0,∞), b: (0,∞) → ℝ; lim ν(p_{n,N}) = (1/t)∫_0^t ω_{[α(s),β(s)]} ds with α = b − 2a, β = b + 2a. The paper's paraphrase (average over r ∈ (0,t) of the arcsine laws of [ψ − 2φ, ψ + 2φ]) is exact, and φ = cr^{−p}, ψ = 2cr^{−p} gives [0, 4cr^{−p}]. |
| Van Assche–Van Baelen | arXiv:1910.12518v1 | Thm 2.2: lattice {q^k}, lim n^{−2} log w(x^n) = 0 uniformly on closed subintervals of (0,1] ("does not generate an external field"); σ([0,1]) = ∞; zeros scaled as x^{1/n}; radial part of a circularly symmetric constrained problem in the disc. Accurate. §1 of that paper also says constrained problems "were first used by Rakhmanov", which supports "introduced by Rakhmanov". |

Dragnev–Saff (Thms 2.1, 2.6, 3.3), KVA-PLMS (Thms 2.1, 2.2) and Beckermann (Thm 1.3) agree with CITATIONS.md. I did not
re-fetch them: the KVA-PLMS and Beckermann manuscripts are image-only PDFs.

Findings:
- **Minor (applied, M1).** The text said "Beckermann … extended them to complex sets". Per CITATIONS.md, Dragnev–Saff's
  existence theorem already holds on closed E ⊂ ℂ (Beckermann's Thm 1.1 summarises it). What Thm 1.3 extends is the
  zero-distribution theorem (his Thm 1.2). Now: "weakened the separation and growth hypotheses of these
  zero-distribution results and allowed discrete sets in the complex plane."
- **Minor (not applied; author, before submission).** The `note` fields "numbering as in the authors' manuscript"
  (KVA-PLMS, KVA-JAT, Beckermann) will look odd to a referee. Check the theorem numbers against the journal versions
  and delete the notes, or cite the manuscripts. ARXIV.md already lists this as open.
- No overclaim found. "None of the results above covers this case" is justified: Rakhmanov and Dragnev–Saff assume
  finite constraints, KVA-PLMS has no finite accumulation point, and VAVB uses a geometric lattice and circular
  symmetry. KVA-PLMS's weights exp(−γx^αL(x)^α) are simplified to exp(−γx^α), which understates their result and does
  not misstate it.

## 4. Forward pointer (decision: Paper I posted alone first)

**Major as submitted; fixed (F1).** The last sentences of §1.2 credited the unposted [PaperII] with pointwise
asymptotics by Riemann–Hilbert methods. They also said that [PaperIII] "shows that they can fail for weights
k^{−s}e^{ε_k}". Both attribute results to unposted work. Replaced by: "Companion papers in preparation treat the
pointwise asymptotics of b_n and a_n." The `PaperII` and `PaperIII` bib entries are removed (now uncited). ARXIV.md
placeholder 3 and NOTES.md are updated to match.

## 5. Read as a human referee and editor

Structure. The introduction runs from p. 1 to six lines into p. 5, about 3.7 pp. of text after the title block, so it
is within the 4 pp. limit. Theorem 1.1 is stated in full on p. 1, Theorem 1.3 on pp. 2–3 and Corollary 1.4 on p. 3.
Every section has an opener, and the long proofs have outlines. The 10pt amsart default (geometry and booktabs
removed) gives 19 pp. with standard margins. That is acceptable and matches ARXIV.md.

Style §§2–3 grep: no banned words, no "Note that", no "Indeed", no em-dashes, no `\textbf`, no repository vocabulary.
One file/path sentence remains, in the data statement, as the style guide allows. Lists remain only for parallel
items (the parts of Lemma 2.2 and Theorem 1.3, the three absolute-convergence checks, the quantile facts).

Editorial findings (all applied):
- **E1 (notation clash).** 𝓑_y was defined in the same sentence that uses y as the arcsine variable. y = min(1, x/4c)
  in the proof of Theorem 1.3(i) also collides with y in U*(x) = ∫log|x−y|dμ*(y). Renamed the incomplete-beta
  argument to z (definition in §1.1, proof of 1.3(i), Remark 3.5). z was unused.
- **E2.** "The maximiser has the same structure" became "In the variable x our solution has the same product
  structure" (§2 above).
- **E3 (Theorem 4.3 outline).** "a tail atom is closer than a^{−p} to the head atom a^{−p}" was hard to parse. Now:
  "each head atom a^{−p} is at distance less than a^{−p} from every tail atom".
- **E4 (Theorem 5.2 outline).** "place one atom at each 1/n-quantile of θ" did not match Step 2, which takes
  k_i = ⌈nq_i⌉ at the midpoint quantile. Now: "split the support of θ into n blocks of θ-mass 1/n and take one atom
  next to the midpoint quantile of each block".
- **E5 (Lemma 3.3 outline).** The truncated integrals tend to k_0 − log|a|, not to −log|a|. Now: "write −log|a|, up
  to an additive constant, as the limit of the truncated integrals".
- **E6 (Lemma 3.3 statement).** "…≥ 0, where ν̂(ξ) := …, with equality iff ν = 0" attached the equality clause to the
  definition. Now: "with equality if and only if ν = 0; here ν̂(ξ) := …".
- **E7 (heuristic, §1.2).** The zero distribution μ* matches the measures of Theorem 1.1 after scaling by n^p/C, not
  n^p, and only when the accumulation point is 0 (a_n ∼ 2cCn^{−p} → 0 forces L = 0). Now: "after scaling by n^p/C,
  that the measures of Theorem 1.1 with L = 0 would have".
- **E8 (σ overloaded, §1.2).** In the description of Rakhmanov's result, "a constraint σ" reused σ, the paper's
  discrete measure. Now: "a constraint measure of total mass > 1".
- **E9 (§2 opener).** Its first sentence repeated the organisation paragraph almost word for word, and "its
  consequences include" was vague. Now: "Most of this section rests on Heine's formula … From it we derive
  monotonicity in the weights, the effect of translations and dilations (Lemma 2.2), and a comparison lemma …
  (Lemma 2.3)."
- **E10 (layout).** There were two underfull boxes: the arcsine definition in §1.1 (reworded: "denote … which has
  density") and the data statement (reordered and set ragged-right because of the unbreakable `\texttt`
  identifiers). Both are gone.

No other LLM tells were found that need action. The prose reads as a careful human paper. Sentences of the form "X is
used only for Y" now appear once (§1.3).

## 6. Applied changes (summary)

`main.tex`: E1–E10, M1 and F1. `refs.bib`: removed `PaperII` and `PaperIII`. `main.bbl` and `main.pdf` were
regenerated (pdflatex, bibtex, pdflatex ×2). `ARXIV.md` placeholder 3 and `NOTES.md` (bibliography rows, §2.5.7 row)
were updated. The abstract in `main.tex` and in ARXIV.md are identical up to `Ces\`aro`/Cesaro (1225 characters).
MANIFEST.sha256 was regenerated.

## 7. Open for the author (not blocking)

1. Bib `note` fields on manuscript numbering (§3, minor).
2. When II and III are on arXiv, a revised version of I may cite them in the sentence that ends §1.2.
3. Optional: re-fetch Dragnev–Saff, KVA-PLMS and Beckermann against their journal versions (I confirmed them only
   against CITATIONS.md).
