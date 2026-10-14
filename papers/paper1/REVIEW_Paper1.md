# Rule R review: Paper 1 draft (branch paper-1-averaged, commit 5118e96)

Reviewer: independent second reader (Rule R), also acting as journal referee. Date: 2026-10-14.
Scope: papers/paper1/main.tex (and the PDF built from it), refs.bib, NOTES.md, checks/. Sources compared against:
research/G2/PROOF.md, research/G2/CITATIONS.md, research/program/novelty_G2.md, and item 11 PROOF.md H1–H7
(math-pursuits, read-only). Rule C: I opened no external source. Every claim below about an external paper is
checked only against the verbatim records in CITATIONS.md and novelty_G2.md.

## Verdicts

- **Lemma 3.3 (Fourier proof that the log energy is positive): CORRECT.** It holds in the stated generality. Unbounded
  support is allowed, and no compact support or log moment is needed beyond the |ν|⊗|ν| hypothesis. That generality
  covers the use in Thm 1.3(iii). The fixes are expository only (F1–F3).
- **Paper overall: ACCEPT WITH FIXES.** No mathematical error was found. I re-derived every step of §§2–6. There is
  one small numerical misstatement (F5). The open items are scholarship and positioning work that NOTES.md already
  lists (F7, F8), plus exposition.

## Checks done

1. **Lemma 3.3, line by line.**
   - *Step 1 constants.*
     - (a): integration by parts gives |∫_A^B cos t dt/t| ≤ 2/A, which is better than the stated 3/A.
     - (b): θ ∈ [0, 1/4].
     - (c): θ′ ∈ [−1, e⁻¹].
     - In the three cases this gives |K| − |log|a|| ≤ 5.25, ≤ 2.25 and ≤ 5 respectively. So (3.3) holds with
       room to spare, and the cases are exhaustive.
   - *Step 2.* The two-endpoint decomposition is right. The limit is k₀ − log|a|. In fact k₀ = 0 (Frullani/Ci–E₁).
     This is verified numerically, and the proof never needs it because ν(ℝ) = 0.
   - *Step 3.*
     - The diagonal is |ν|⊗|ν|-null, because the integrand is +∞ there.
     - The dominating function |log|x−y|| + 6 is |ν|⊗|ν|-integrable, since |ν| is finite.
     - Fubini on [ε,R]×ℝ² holds: the integrand is bounded by 2/ε against a finite measure.
     - ∬cos((x−y)ξ)dνdν = |ν̂(ξ)|², with no stray factor of 2 or 1/2.
     - Monotone convergence on the right gives the identity.
     - The two-parameter limit should be taken along sequences (F2).
   - *Equality.* ν̂ ≡ 0 follows from continuity, conjugate symmetry and ν̂(0) = 0. Gaussian smoothing then gives
     Fourier uniqueness. The signs in G_t*ν and Fubini are correct. The step "∫ψ dν = 0 for all bounded continuous ψ
     ⇒ ν = 0" is standard for finite Borel measures on ℝ.
   - *Generality.* There is no compactness or support assumption, and none is needed: the whole argument runs on
     |ν|⊗|ν|, a finite measure.
2. **Use of Lemma 3.3 in Thm 1.3(iii).** The hypotheses match. ν = μ^x − μ* is a finite signed measure on (0,∞) ⊂ ℝ
   of mass 0. Since |ν| ≤ μ^x + μ*, ∬|log| d|ν|d|ν| is at most the sum of the three absolute energies that the
   bullets establish:
   - |L|(μ^x): the positive part comes from log⁺|x−y| ≤ log(1+x) + log(1+y) and μ^x ≤ σ_p; the negative part is
     finite because J_p(μ) > −∞.
   - |L|(μ*): from (3.1), integrable over (s,t) ∈ (0,1]², then Tonelli on the mixture.
   - |L|(μ^x, μ*): from |t| = 2t⁺ − t and U* ≥ log c + p.

   The bilinear expansion is checked algebraically. The middle-term sign argument is correct: the integrand is 0 on
   (0,4c] and ≥ 0 on (4c,∞), where ν = μ^x − σ_p ≤ 0. Uniqueness follows from L(ν) = 0 ⇒ ν = 0, and g is a bijection.
   The step |ν| ≤ μ^x + μ* is left implicit (F1).
3. **Bound (3.1).** ∫|log|x−y|| dω_β = 2∫log⁺ − U_β(x) ≤ 2 log(1+x+β) − log(β/4). Correct for every x ≥ 0, since U_β
   is finite there. The Fubini steps in Thm 1.3(ii) and (iii) that use it are correct.
4. **Tail bound via Heine (Thm 4.3).**
   - V(T) ≤ (Mn)^{−pm(m−1)}, because there are m(m−1)/2 pairs, each of squared gap < (Mn)^{−2p}.
   - Σ_{|T|=m} w(T) ≤ W^m.
   - The Heine sum factorises over (H,T), and the cross bound is (N!)^{−2pm}.
   - φ_M: I re-derived it term by term. It equals item 11 H7's φ_M, A = 4p + 2|E_p| is correct, and the N = 0 case and
     the uniformity in m are correct.
5. **Translation remark.** Under (H-a), f(ξ) − L = ∫_ξ^∞|f′| ∼ Cξ^{−p}. Lemma 2.2(ii) and the purely difference-based
   Lemma 2.3 make L irrelevant. Correct.
6. **Rest of the paper re-derived.**
   - **§2:**
     - Lemma 2.1, including the permutation/sign step.
     - Lemma 2.2.
     - Lemma 2.3: Cauchy MVT, k_i ≥ i, exponent 2Σ(n−i)η(i).
     - Lemma 2.4: the recurrence coefficient h_k/h_{k−1} and the product count n − j.
     - Lemma 2.5: the integral is (n²/2)log n − (3/4)n² + O(n), and the Euler–Maclaurin error is O(n log n).
   - **§3:**
     - Lemma 3.1: J_p(μ_τ) = τ²(J_p − pm² log τ).
     - Lemma 3.2.
     - Thm 1.3(i): substitutions t = t_x s and v = s^p; B(1/p + ½, ½) = 2I(p); (4c)^{1/p} = π/(2I(p)) ⇒
       dμ*/dσ_p = 𝓑_{min(1,x/4c)}.
     - Thm 1.3(ii).
     - Thm 1.3(iii) value: ∫∫ log min(s,t) = −3/2.
   - **§4, Lemma 4.1:**
     - c₀ = ∫₀¹∫₁² log(y−x) = 2 log 2 − 3/2, recomputed via the triangular density.
     - Δ/D ≤ 1/(l−k−1).
     - The diagonal −3/2.
     - The harmonic count ≤ 1 + log n.
   - **§5, Lemma 5.1 and Theorem 5.2, steps 1–4.** I re-derived every inequality, including the b > ½ case:
     b − a = (r_{i+1} − l_i)/l_j + (l_i/r_j)(r_j − l_j)/l_j ≤ 3/(d_U n l_j).
     - The i = 1 bathtub steps hold.
     - The diagonal sum p((n−1)log n − log(n−1)!) = O(n) holds.
     - The direction of the diagonal correction is right: it is an upper bound on ⟨F⟩_{B_i²}, subtracted.
   - **§6:**
     - f′ < 0 and f bounded.
     - Cor 1.2 algebra: bracket = log(c(p)C)n² + o(n²).
   - **§7:** the reindexing of Cor 1.4; c(1) = ½; c(2) = π²/16; b > −1 and b > −3. The asymptotics of the b = 0
     closed form also check out: 2n(n+1)log(π/2) − [(m²/2)log m − ¾m²] with m = 2n+1 gives 3 + log(π²/16).
7. **Constants against G2.** u_s = (4c)^{−1/p} (G2 B*(i)) equals 2I(p)/π, by (4c)^{1/p} = π/(2I). Checked at p = 1
   (½), p = 2 (2/π = 0.6366) and p = 0.5 (0.375), all matching Table 1. The abstract's c(p) is algebraically the same
   as (1.2). κ₁ = 0.806853 and κ₂ = 2.516871 were recomputed.
8. **Faithfulness to the repo.** Thm 1.1, Cor 1.2, Thm 1.3 and Cor 1.4 have the same hypotheses and conclusions as
   G2 H_all, B*, HZ: (H-a), Σw < ∞, w_k ≥ c₁k^{−s}, 2a + b > 1. The only addition is the closed-form density, which is
   proved in the paper. Nothing is stated more strongly than it is proved.
   - Lemmas 2.1–2.4 match item 11 H1–H4. The paper adds boundedness of f and h and Σw < ∞, both needed for finite
     moments.
   - Thm 4.3 matches H7/A-U, with Heine replacing Hadamard.
   - Thm 5.2 matches A-L.
   - The "Remark (uses of Lemma 3.3)" is accurate: only E_p ≤ κ_p enters Thm 1.1.
9. **Scripts re-run** with jacobi-asymptotics/.venv/bin/python:
   - `checks/bs_check.py`, `checks/monien_check.py`, `checks/positivity_sanity.py`: outputs **byte-identical** to the
     stored .out files.
   - `research/G2/checks/check_energy.py`: **identical** (Table 1).
   - `check_averaged.out` and `check_hz.out`: compared by hand with Table 2 and the §8 text, and they match. I did not
     re-run them (they need the toolkit C kernels).
10. **Independent numerics (scratch, NUMERICAL).**
    - k₀ = 0.0.
    - max(|K_{ε,R}(a)| − |log|a||) = 0.60 on a grid a ∈ [1e−8, 1e9], ε ∈ [1e−9, 0.999], R ∈ [1.001, 1e10], well
      within 6.
    - The Lemma 3.3 identity for an *unbounded-support* ν = Exp(1) − Exp(rate 2): the energy side is (1/3)log 2 =
      0.2310491 (closed form, using E log|X−Y| = −γ − (1/3)log 2). The Fourier side is 0.2310491 by quadrature.
11. **Quotation trace (Rule C).** Every quoted string in main.tex was matched against the repo records:

    | Quotation | Recorded in |
    |---|---|
    | Monien §1 "We do not know…" | CITATIONS (M) |
    | Monien §3 "We seek…" | CITATIONS (M) |
    | Monien Thm 3.1 formula | CITATIONS (M) |
    | HZ "for positive integers a and b…" | CITATIONS (HZ) |
    | HZ "≤ −(a/2)…" (fragment of the recorded sentence) | CITATIONS (HZ) |
    | HZ "In [5] Monien…r = 0" (truncated, correct) | novelty §3 |
    | Lai sentence | novelty §3 |
    | BKMW Lemma 2.1 and (1.12) | CITATIONS (P) |
    | BS Cor 3, Rem 5, (22) | novelty §3 |
    | KVA theorem via CCV Thm 1.3 (paraphrased) | novelty §2(c) |
    | Coons–Sutherland Thm 1.3 (paraphrase is faithful) | novelty §1(c) |

    No quotation lacks a source in the repo. The framework sentences (Rakhmanov, DS, KVA-PLMS) faithfully paraphrase
    abstracts only (see F7).
12. **The NOTES.md §2.7 KVA coefficient swap.** I verified it from the CCV quote in novelty_G2.md. KVA's recurrence is
    zP = P_{n+1} + b P_n + a² P_{n−1}, so b is diagonal and a is off-diagonal, with γ = b − 2a and δ = b + 2a.
    - novelty_G2 §2(c) uses a(t) = 2ct^{−p} and b(t) = ct^{−p}. That gives [γ,δ] = [−3ct^{−p}, 5ct^{−p}], which is
      **wrong**.
    - The paper uses diagonal 2ct^{−p} and off-diagonal ct^{−p}. That gives [0, 4ct^{−p}], which is **right**, and is
      consistent with the paper's own convention a_n ∼ 2b_n (Lemma 2.4: a diagonal, b off-diagonal). It is also
      consistent with G2's remark "b_j = c(p)j^{−p}, a_j = 2b_j" in item 11's convention.
    - **NOTES.md is right, and novelty_G2.md §2(c) still carries the error** (F9).

## Findings

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| F1 | Minor | Thm 1.3(iii) proof, the sentence defining ν (main.tex l. 539–540) | The claim ∬\|log\|x−y\|\| d\|ν\|d\|ν\| < ∞ rests on the three bullets only through \|ν\| ≤ μ^x + μ*. This is not said. | Add "since \|ν\| ≤ μ^x + μ*, this follows from the three bullets." |
| F2 | Minor (exposition) | Lemma 3.3, Steps 1–3 | (a) The bound is 2/A. "3/A" is harmless but invites a check. k₀ = 0 is true (Frullani) and could simply be stated, or k₀ dropped. The joint limit ε → 0, R → ∞ in the dominated-convergence step should be taken along sequences (ε_m, R_m). | Tighten (a) to 2/A or keep it. Say "along any sequences ε_m ↓ 0, R_m ↑ ∞". Optionally note k₀ = 0. |
| F3 | Minor | Rem 3.4 (BKMW), l. 464 | "Lemma 3.3 is a special case of [BKMW, Lemma 2.1]". This needs a sentence. The hypothesis of Lemma 3.3 implies ν^± ∈ M(ℂ): finite energy, and the log moment, which follows from \|ν\|⊗\|ν\|-integrability by fixing a typical y. Also, BKMW states positivity only, not the Fourier identity. | Write "its positivity statement is a special case of …, because ν^± ∈ M(ℂ) under our hypothesis". |
| F4 | Minor (exposition) | Abstract; §1.2 "logarithmic energy problem"; heading of §3.3; Thm 1.3(ii) "logarithmic potential" | The sign convention flips. "Logarithmic energy" means ∬log\|x−y\| (to be maximised) in the abstract and §1, but −∬log\|x−y\| in Lemma 3.3. "Potential" ∫log\|x−y\| is the negative of the standard U^μ (and of BKMW's convention, quoted in Rem 3.4). A potential theorist will trip on this. | Define once, e.g. "I(μ) = ∬log(1/\|x−y\|)" (standard), and say "J_p = −I ∘ g_*, maximised". Or call J_p "the functional" and keep "energy" for the standard sign. |
| F5 | Minor (factual, numeric) | Rem 7.2, l. 873 | "(n/log n) times it stays between −1.2 and −4.9". bs_check.out gives −1.386, −1.257, −1.192, −1.154 (ℓ = 0) and down to −4.890 (ℓ = 2). Two values lie outside the stated range. | Replace with "between −1.1 and −4.9" (or "−1.15 and −4.89"). |
| F6 | Minor | Rem 7.2, last sentence | "for a = 2, b ∈ {−2, 0, 2}, Cor 1.4 also follows from [BS]". The asymptotics are derived in the text only for b = 0. For b = ±2 the paper shows only numerics. | Add one line: the ℓ = 0, 2 closed forms differ from ℓ = 1 by explicit factors (2^{−2n(n+ℓ)}, product range 2n+ℓ−1, and for ℓ = 2 the factor (n+1)(n+3/2)) that do not change the n² log n or n² terms. Or restrict the claim to b = 0. |
| F7 | Moderate (scholarship; pre-submission blocker, already in NOTES §5.5) | §1.2 "The equilibrium problem" | The sentences on Rakhmanov, Dragnev–Saff and KVA-PLMS rest on abstracts (Rakhmanov only via the CDLO abstract). The "TO VERIFY" markers are LaTeX comments and so invisible in the PDF. The no-prior-art sentence "We have not found in the literature the problem sup_𝒜 J_p … or its solution" depends on texts that were not read: DS 1997, KVA PLMS/JAT 1999, Beckermann 2000. The BS quotations were read by the novelty agent, not re-opened at drafting. The closed forms are confirmed independently by bs_check (direct ζ-determinants), but the numbering (Cor 3, Rem 5, (22)) and the H_n^{(ℓ)} indexing convention are second-hand. | Read the full texts before submission (NOTES §6 checklist). Keep the paraphrases tied to the abstract wording. If a full text is not obtainable, hedge in the visible text ("as described in its abstract"). |
| F8 | Moderate (positioning) | §1.2, the Lai/Fauzan paragraph | novelty_G2.md §3 records that Fauzan's Zenodo abstract mentions "a positive moment representation and a logarithmic-energy estimate", and that Romik's formalization README mentions arcsine measures. That is a methodological overlap with Thm 1.3. The paper says only that its results are "logically independent". A referee will ask whether Fauzan's energy estimate solves the same or a related constrained problem. The paper also cites, without qualification, an unrefereed record whose title claims a major result. | Add: "Fauzan's announcement describes a logarithmic-energy estimate for Hankel determinants of a different moment sequence; the full manuscript was not available to us." Cite it as an announcement / Zenodo record. Re-check once the manuscript appears (NOTES §5.7). |
| F9 | Minor (repo hygiene) | research/program/novelty_G2.md §2(c) | The KVA coefficient assignment a(t) = 2ct^{−p}, b(t) = ct^{−p} is wrong in KVA's convention (Check 12). The paper is correct, but the repo record still carries the error. | Add a dated correction note to novelty_G2.md §2(c), in a separate docs: commit (not done here; review-only mandate). |
| F10 | Minor (exposition) | Remark 7.1 and §1.2 ("agrees with Monien's weak asymptotic form") | Read literally, Monien's "∼" carries only the leading term. The n² constant comes from reading −n²(log 2n − 3/2) with an o(n²) error, which Zagier's numerics support (novelty §3). | Say "Monien's form −n²(log 2n − 3/2), read with an o(n²) error (as Zagier's expansion quoted there indicates)". |
| F11 | Minor (exposition) | Table captions and the opening of §8 | They point to repo paths (`research/G2/checks/…`) and an unnamed "accompanying repository". | Replace with a supplementary-material reference or a public repository URL and commit hash. |
| F12 | Minor | §8, Table 2 text | At p = 1.5 the K-doubling change (5.4·10⁻⁴) is about 20% of S₁₆₀₀ = −2.67·10⁻³. The last column for p = 1.5 is only indicative. | State it, or drop the n = 1600 entry for p = 1.5. |
| F13 | Minor (bibliography) | refs.bib | BKMW is cited as arXiv only. It may have a journal version: I recall Constr. Approx. (2013), unverified, so check it. VAVB lacks volume and pages (bibtex warning). Check the publication status of Monien, Coons–Sutherland and Lai. | Complete the entries (NOTES §5.9). |
| F14 | Trivial (exposition) | various | (i) Thm 5.2 Step 2: "u_i ≤ r_{i+1}" needs i ≤ n−1 (that is the only use). (ii) Define the mixture μ* = ∫ω_{β_t}dt as μ*(B) = ∫₀¹ω_{β_t}(B)dt. (iii) The letter c is overloaded: c(p), the weight scaling in Lemma 2.2(iii), c₀, c₁. I(p) clashes with BKMW's I(μ) in Rem 3.4. (iv) In (1.3), the sup condition is implied by the limit plus continuity, so it is harmless but redundant. | Light edits. |
| F15 | Info | papers/paper1/ | The build products main.aux, .bbl, .blg, .log and .out are untracked. | Add them to .gitignore. |

## Notes on what is *not* a problem (checked because it looked risky)

- **Unbounded support and infinite constraint mass in Lemma 3.3.** Not an issue. The lemma's only hypothesis is
  |ν|⊗|ν|-integrability of |log|x−y||, and in Thm 1.3(iii) it is established (F1 aside) from the finite log moments of
  measures ≤ σ_p. μ* and μ^x are probability measures; the constraint σ_p has infinite mass near x = 0, but that never
  enters.
- **Saturation / upper constraint.** It enters only through the sign of ν on (4c,∞), where μ* = σ_p ≥ μ^x. Correct.
- **Finiteness of E_p before it is used in A = 4p + 2|E_p|.** Thm 1.3 precedes §4, so this is not circular.
- **Thm 5.2 diagonal blocks.** Only an upper bound on ⟨F⟩_{B_i²} is needed, and that is what is proved.
- **Lemma 2.3 when some w_k = 0** (upper bound only). The term-by-term comparison holds whether or not the determinants
  are positive.
