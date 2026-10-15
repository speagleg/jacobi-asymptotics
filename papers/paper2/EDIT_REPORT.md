# Paper 2 — developmental and copy-edit report

Draft read: `main.pdf` of 14 October 2026 (70 pp) and all `.tex` sources, against `OUTLINE.md` §4 (notation) and §6 (style).
Mathematical correctness was not checked. Places where two sections state the same thing differently are flagged in §3.4.

Locations are given as `file:line` (source) and `p.N` (PDF page). The page map is: §1 pp. 1–7; §2 pp. 8–13 (Tools
pp. 10–13); §3 pp. 14–17; §4 pp. 18–23; §5 pp. 24–33; §6 pp. 33–44; §7 pp. 45–55; §8 p. 56; §§9–10 pp. 57–59;
App. A pp. 60–61; App. B pp. 62–65; App. C pp. 66–69; references p. 70.

---

## 1. Assessment (one page)

**Does the paper tell one clear story?** Mostly, yes. The arc is good and visible at the large scale: averaged law
(Paper 1) → why the pointwise law is subtle → Theorem 1 → reduction to an analytic engine (Theorem 4) by two elementary
steps (shift, smoothing) → RH frame → hard-edge comparison → extraction. Figure 1 shows the architecture well. §§3–4
are the best-written part of the paper. Each step is motivated, the proofs are sized correctly, and the "order of the
steps" paragraph (p. 23) is the kind of signposting a referee likes. §8 and the Christoffel-shift remarks are also
clean. The prose voice ("we", present tense, short sentences, honest scoping) is mostly consistent across the four
drafters.

**Where it fails.**

1. *The thread is lost in §§5–6 (21 pp, pp. 24–44).* A specialist reaches the actual novelty, the hard-edge
   comparison, only on p. 45. Before that come nine pages of frame and twelve pages of outer-scalar constructions. These
   are needed, but they are presented at the same level of detail as the main argument, and nothing says which parts a
   reader can skim. §6.1–6.3 (three geometry-specific lemmas, about 6 pp of Stirling/Binet/Cauchy-integral estimates)
   sit in the middle of the main line of argument.
2. *Seams between drafters show up as duplication rather than contradiction.* The same object is often defined or
   proved twice, in different notation. Examples: the Frame Proposition (F1)–(F8) is restated almost in full as a
   bulleted list in §7.1 (pp. 45–47). The Szegő function, its representation formula and the explicit
   $D_{x^\alpha}^2$ appear in both §6 (Lemma 6.6) and §7 (Lemma 7.3 Steps 0–1). In §6 the conformal map is called $\Phi$,
   in §7 it is called $\Upsilon$. The extraction-invariance argument appears three times (Lemma 5.1 proof, (F8) proof,
   Lemma 8.1). The statement "$Q$ is the Cauchy integral of its jump" is proved twice, by different arguments, in App. B
   (Lemma B.1(c)) and App. C (Corollary C.4). The motivation for the comparison method is told three times (§1.4,
   §7 opening, Remark 6.3/Frame Remarks), the third time with a sentence repeated verbatim.
3. *Notation is overloaded across chunks.* The worst cases are the same symbol with two meanings: $\mathcal H_n$,
   $L_\pm$, $\Pi$, $\kappa$ (six meanings), $m_n$, $c_p$ and $c_\pm$ (which break the paper's own "never $c$" rule), and
   $F$, $\Phi$, $\omega$, $\Xi$. The OUTLINE §4 promise "one symbol, one meaning" is broken in about 25 places (§3 below).
4. *Leaks from the drafting process.* "Paper 1" appears as a name in the running text (§5, Fig. 1). TODO comments and
   a "Coordinator: keep or drop" comment are still in the source. The author line is a placeholder. There is an empty
   Appendix D input. Two hedging sentences read as drafter self-doubt (the sign remark in the proof of Theorem 4 and the
   unchecked Lommel masses).

**Length.** 70 pp is about 10 pp too long for what is proved. The duplications alone (list in §2, items S2–S8) account
for about 6–7 pp. The quote-heavy Tools subsection (§2.5, 3.5 pp) can lose about 1.5 pp. §10.2 and §10.4 can lose about
1 p. A realistic target is **58–60 pp with no loss of content**. Moving §6.1–6.3 to an appendix (S1) does not shorten
the paper, but it shortens the main line from about 56 to about 50 pp.

**Is the introduction effective?** Partly. The first paragraph poses the question well. However:
- Theorem 1 does not appear until **p. 3**. A reader first has to absorb three definitions (slow variation, the smoothing
  error $\rho_\ell$, hypothesis $(\mathrm A_\vartheta)$) and the head margin $M_0$. Most of this is needed only for
  Theorem 1(ii), which is a technical refinement.
- Theorem 1(iii) and Theorem 2 overlap: Theorem 2 is Theorem 1(iii) with $\ell\equiv1$. Theorems 2 and 4 have the same
  displayed conclusion. A reader sees the same display three times before reaching p. 5.
- The "how" (§1.4) is good but long (2.5 pp). It overlaps §7's opening almost sentence by sentence.

A specialist would know *what* is proved by p. 3 and *why it matters* by p. 4. They would know *how* by p. 7. The
target should be p. 2 for what and why, and p. 5 for how. S9 and S10 below achieve this.

**Verdict.** The mathematics is presented honestly and the elementary half reads well. The RH half is complete but
reads like three careful reports bolted together. The paper needs one consolidation pass, mainly removing duplicates,
unifying notation and moving the geometry-specific constructions out of the main line. It does not need a rewrite.

---

## 2. Structural changes (prioritised)

**S1. Move the three geometry constructions (§6.1–6.3) to a new appendix, and keep their statements in §6.**
*Where:* `sec_6.tex:67–369`, pp. 34–39.
*Proposal:* §6 then has this order: the introductory paragraphs (Binet function $j$, $\tilde D$, $D$, $K$, the cut
problem, which is already well written at lines 29–65), then Table 1 (moved here, see F2), then one short subsection
"The outer scalar in each geometry". That subsection states Lemma 6.1 (iv), Lemma 6.2 and Lemma 6.4 (iv) as one lemma:

> **Lemma 6.1 (outer scalar).** *Let $F:=DBK$ if $p>1$ (with the Binet-cut scalar $B$ of (D.x)), $F:=DK$ if $p=1$, and
> $F:=DB_{\rm in}Ke^{\chi}$ in $S_{\rm in}$, $F:=B_{\rm out}Ke^{\chi}$ in $S_{\rm out}$ if $0<p<1$ (with the seam scalar
> $\chi$ of (D.y)). Then $F$ satisfies (O1)–(O5).* For $p=1$ the reflection formula gives $D=e^{j(-n/z)}$, so $D$ has
> no cut and no correction is needed (two lines). The constructions for $p\ne1$ are in Appendix D.

Remark 6.3 (quotient parametrix at $p=1$) stays in the main text. The new appendix ("Construction of the outer scalar")
takes Lemmas 6.1, 6.4 and 6.5 with their proofs. OUTLINE R14 already anticipated this move. The main line then goes
from frame (§5) to outer scalar (stated) to common steps to the Frame Proposition and the hard edge, and §6 shrinks from
12 pp to about 6 pp.

**S2. Replace §7.1's restatement of (F1)–(F8) by a short pointer.**
*Where:* `sec_7.tex:91–141`, pp. 45–47 (about 1.5 pp).
*Why:* it re-proves nothing, and it introduces a discrepancy: (F4) gains a factor $|z|^{-C}$ that is not in
Proposition 6.9 (see §3.4).
*Draft text:*

> We work in the frame of $Q:=D_\infty^{-\sigma_3}VD_W^{\sigma_3}$ and use only the items (F1)–(F8) of the Frame
> Proposition (Proposition 6.9), for fixed radii $\delta,\varepsilon$ that may be taken as small as we wish. In
> $U(0,\delta)$ the contour consists of the band and two lips, with $v=J$ on $(0,\delta)$ and
> $v=\bigl(\begin{smallmatrix}1&0\\ \omega e^{2n\varphi}&1\end{smallmatrix}\bigr)+E$ on the lips, where
> $\omega=D_W^2/W_0$ (F1); there is no jump on $(-\delta,0)$. Since $f'(0)<0$ and $f$ is real on $(-\delta,\delta)$, …
> [keep lines 142–151 as they stand].

**S3. Make §7.3 (lip mismatch) cite §6's Szegő lemma instead of re-deriving it.**
*Where:* `sec_7.tex:409–494` against `sec_6.tex:375–493`.
*Detail:*
- Step 0 re-defines $D_q$ and re-proves (6.x) (`eq:szego-repr` = `eq:he-repr`).
- Step 1 re-proves $D_{x^\alpha}^2=(4cz/\Phi)^\alpha$ (Lemma 6.6(i)) under the new name $\Upsilon$. It also uses local
  symbols $F$ and $g$ that clash with the outer scalar and the $g$-function.
- Step 2 is Lemma 6.6(ii) with $q=q_2$.
- Step 3 is Lemma 6.6(iii) with $M=C\varepsilon_\Lambda(T_n)$, via Lemma 5.6(iii).

*Proposal:* Lemma 7.3's proof becomes "By (6.x), $D_W^2/W_0$ is the product of three ratios. Lemma 6.6(i) and the
expansion $\Phi(z)=-4c(1+O(|z|^{1/2}))$ give the first; Lemma 6.6(ii) with $\nu=\nu_p$ gives the second; Lemma 6.6(iii)
with $M=C\varepsilon_\Lambda(T_n)$, which is admissible by Lemma 5.6(iii), gives the third." The proof then fits in
about 10 lines and saves about 1 p.

The intro advertises "the key estimate for the slowly varying factor is a scale-invariant path integral of $\Lambda'$
(Section 7)". To keep that pointer accurate, either move Lemma 6.6(ii)–(iii) into §7 as Lemma 7.3's engine, or change
the intro pointer to "(Lemmas 5.6(iii) and 6.6(iii))". The first option tells the better story.

**S4. Move the invariance of the extraction functionals into §5, and shrink §8 to the computation.**
*Where:* `sec_5.tex:63–100` (Lemma 5.1, which already contains the conjugation argument), `sec_6.tex:689–693` ((F8)
proof, which repeats it) and `sec_8.tex` (Lemma 8.1, which proves it a third time and repeats (5.x) as (ii)). The
paragraph after Lemma 8.1 also repeats Lemma 6.7.
*Proposal:* State Lemma 8.1(i) once, as a lemma directly after Lemma 5.1 and the definition of $\mathsf a(X)$ (5.x). Define the
second functional $\Pi(X)$ there as well, renamed (see N3). The proof of (F8) then reads "Lemma 6.7 and that lemma". §8
becomes: the indexing paragraph (keep it), the proof of Theorem 4, and Remark 8.2. Saves about 0.7 p.

**S5. Merge App. C's Corollary C.4 into App. B's Lemma B.1(c).**
*Where:* `app_c.tex:131–155` and `app_b.tex:31–75`. Both prove "analytic off $\Gamma$, $L^2$ boundary values, mild at
the vertices, $O(1/z)$ at $\infty$ ⇒ Cauchy integral of the jump", one by a Laurent-coefficient argument and one by the
Cauchy formula with excised discs.
*Proposal:* Keep Lemma B.1(c) and move it to the start of App. A or into §2.5 as a fifth tool, "T5: a Cauchy-integral
criterion". Corollary C.4's proof then becomes: "Proposition C.3(i) with $\eta=(1-|\alpha|)/4$ gives
$\rho\sup_{|z|=\rho}|Q-I|=O(\rho^{1-(1+|\alpha|)/4})\to0$, and Lemma B.1(c) applies." Saves about 0.7 p. It also
removes App. C's local symbols $f$ and $H$, which clash with the conformal map and $H_n$.

**S6. Tell the comparison-method motivation once.**
*Where:*
- (a) `sec_front.tex:390–412`, p. 6: "The hard edge, and why a local parametrix fails", "The remedy" and "What is new".
- (b) `sec_7.tex:31–67`, pp. 45–46: the same three paragraphs, with the sentence "What we add is a comparison model
  built from the Szegő function of the full weight, a uniform resolvent bound … and the treatment of an arbitrary slowly
  varying factor" repeated verbatim from `sec_front.tex:302–303`.
- (c) The fact "nothing is continued across $(-\delta,0)$" appears in Remark 6.3, Frame Remark (2), §7 opening, the
  proof of Lemma 7.2(ii) and §10.2.

*Proposal:* Keep the detailed version in §7, where the reader needs it. Cut §1.4's three paragraphs to one paragraph of
6–8 lines:

> *The hard edge.* The slowly varying factor enters the band weight through $r_n(z)=\ell_1(nz^{-1/p})/\ell_1(n)$, which
> is not analytic at $0$. Hence the standard Bessel parametrix, which needs the weight continued around $0$, leaves a
> jump of size $O(n\varepsilon_\Lambda)$ at the Bessel scale: a quotient argument fails. Following Conway and Deift
> [CD], we instead build the Bessel parametrix from the Szegő function of the whole band weight. The comparison problem
> is then exactly solvable, and it differs from the true problem only on the lips of the lens, by an amount that is
> $o(1)$ in the supremum norm but has no rate. A Neumann series closes once the comparison resolvent is bounded uniformly
> in $n$ (this is where $|\alpha|<1$ is used), and Bessel localisation turns the $o(1)$ mismatch into an $O(1/n)$
> error in the coefficients (Section 7).

Keep "What is new relative to Conway–Deift" in §1.3 *Context*, where the CD paragraph already is, and delete it from
§7's opening. Delete Frame Remark (2) (`sec_6.tex:698–700`). In §10.2, replace the last two sentences by a reference to
Remark 6.3.

**S7. Remove the remaining restatements.** Each is short, but together they cost about 2 pp and make the reader wonder
whether something has changed. The two theorem restatements are allowed by the style guide, but they are verbatim and
very close to the original statements.

| What | Defined at | Restated at | Action |
|---|---|---|---|
| Slow variation display (1.x) | `sec_front.tex:96–100` | `sec_2.tex:69–73` | Replace by "Let $\ell$ be slowly varying (Definition 1.1)". |
| Smoothing error, $L_\ell$, $G$ | `sec_front.tex:110–118` | `sec_4.tex:46–52` | Cite (1.x); keep only "$G$ extends to an entire function". |
| $(\mathrm A_\vartheta)$ | `sec_front.tex:126–140` | `sec_4.tex:53–56` | Delete the restatement. |
| Regular rate | running text `sec_front.tex:245–246` | Def. 2.3 `sec_2.tex:120–123` | Keep one (the intro sentence, citing Def. 2.3 for facts). |
| Potter ⇒ finite measure | Rem. 1.4 `sec_front.tex:175–179` | `sec_2.tex:112–114` | Keep §2; Rem. 1.4 says "(Section 2.2)". |
| Paper 1 indexing of $a_n$ | `sec_front.tex:57–58` | footnote `sec_2.tex:35–36` | Keep the footnote only. |
| "No uniqueness of $Y$ used" | `sec_2.tex:235` | `sec_5.tex:102–104` | Keep §5. |
| Theorem 3 | p. 4 | restated p. 14 | Keep, but shorten to "We prove Theorem 3; recall the notation …". |
| Theorem 4 | p. 5 | restated p. 22 | Delete; the reader saw it one page earlier in Figure 1. |
| $\nu_p$ | `sec_5.tex:458` | `sec_7.tex:148` | Delete in §7. |
| $Q:=D_\infty^{-\sigma_3}VD_W^{\sigma_3}$ | `sec_6.tex:508` | `sec_6.tex:593`, `sec_7.tex:91` | Define once (line 508). |
| Szegő formula | (6.x) `eq:szego` | (7.x) `eq:he-szego` | Cite. |
| $P^\infty_0$ | (6.x) `eq:Pinf0` | (7.x) `eq:he-Pinf` | Cite (removed by S2). |
| Remark 1.13 (engine scope) | `sec_front.tex:352–359` | Rem. 1.6 and Rem. 7.7 | Merge Rem. 1.13 into Rem. 1.6, keep Rem. 7.7. |
| DP quote | `sec_front.tex:304–307` | Rem. 7.8 `sec_7.tex:693–695` | Quote once (§1.3); Rem. 7.8 cites it. See also §3.4(e). |

**S8. Cut or compress §10.2 and §10.4.**
- §10.2 ("Other routes at $p=1$", `sec_back.tex:131–145`) reads like a lab notebook ("We also carried out the analysis
  in that symmetric frame … we do not include it"). Compress to two sentences: "At $p=1$ one can also work in the
  symmetric variable $y=\pm x^{1/2}$ of [WLXZ], where $0$ is an interior Fisher–Hartwig point; the comparison method
  then covers only $1<s<2$ directly, and $1<s<3$ after folding. We do not pursue this."
- §10.4, last paragraph (zeta zeros, `sec_back.tex:160–168`) is speculative, depends on "work in preparation", and is
  flagged in the source for a coordinator decision. Recommendation: **drop it**, or keep only the first sentence
  ("A natural measure outside our scope is built from the ordinates of the zeta zeros; its gaps act like a rough
  perturbation of the nodes.").

**S9. Get Theorem 1 onto page 2.**
*Where:* `sec_front.tex:91–173`.
*Proposal:* State Theorem 1 with parts (i) and (iii) only; both need only Definition 1.1 and $(\mathrm A_\vartheta)$.
Move part (ii) (the rate $1/n+\rho_\ell(\lceil n/M_0\rceil)$), the definition of $\rho_\ell$ and the sentence fixing
$M_0$ to a short "Quantitative form" paragraph after Theorem 1:

> *Quantitative form.* The proof gives more. Let $\Lambda_\ell$ be the Gaussian smoothing of $\log\ell$ in the
> logarithmic variable and $\rho_\ell(m):=\sup_{k\ge m}|\log\ell(k)-\Lambda_\ell(\log k)|$ (Definition 1.2), which
> tends to $0$. Then $|n^pb_n-c(p)|+|n^pa_n-2c(p)|=O(1/n+\rho_\ell(\lceil n/M_0\rceil))$, where $M_0\ge4$ depends only
> on $p$ (Lemma 4.3).

Also add a one-sentence result to the very first paragraph of §1.1 (`sec_front.tex:42–45`):

> … how do its matrix entries behave? We show that $n^pb_n\to c(p)$ and $n^pa_n\to2c(p)$, with an explicit constant
> $c(p)$, for every $p>0$, $s>1$ and every slowly varying perturbation of the weights, and that the convergence has rate
> $O(1/n)$ when the perturbation is analytic.

**S10. Demote Theorem 2 to a corollary.** Theorem 2 is Theorem 1(iii) with $\ell\equiv1$ (the proof in §4.4 Step 3 says
exactly this). Call it "Corollary 1.4 (pure powers)", state it in one line, and keep Remarks 1.8–1.10 (Lommel, zeta
Hankel determinants, origin of $c(p)$) attached to it. The main theorems are then Theorem 1 (main), Theorem 2 (shift)
and Theorem 3 (RH engine). Figure 1 needs relabelling. If the author prefers to keep the numbering, at least change
Theorem 2's opening to "In particular, for pure powers…" so the reader knows it is not a new statement.

**S11. Add a roadmap at the start of §5 for the RH half.**
*Where:* `sec_5.tex:27–39` (the current opening is good but does not list the chain).
*Draft text*, to insert after the first paragraph:

> *Roadmap of the proof of Theorem 4.* The matrices are
> $$Y\ \xrightarrow{z\mapsto n^pz}\ U\ \xrightarrow{\text{poles}}\ R\ \xrightarrow{g}\ T\ \xrightarrow{\text{lens}}\ S
> \ \xrightarrow{F}\ V\ \xrightarrow{D_W}\ Q .$$
> Sections 5.2–5.7 carry out the first four steps for any outer scalar $F$ with properties (O1)–(O5) (§5.9).
> Section 6 constructs $F$ (the only geometry-dependent step) and collects everything the hard edge needs in the Frame
> Proposition 6.9, items (F1)–(F8). Section 7 compares $Q$ with an explicit model $\tilde Q$ built from the global, Airy
> and Bessel parametrices and shows that their first two moments at infinity agree up to $O(1/n)$. Section 8 reads off
> $a_n$ and $b_n$. A reader who trusts the frame can go from the Frame Proposition directly to Section 7.

**S12. Slim the Tools subsection (§2.5, pp. 10–13).** It reads as a citation audit: long verbatim quotations,
"oriented as in Figure 3", "does not depend on $n$", the standing hypotheses of the sources, and many DLMF formula
numbers. The OUTLINE requires each tool to be stated *precisely*, with hypotheses and equation numbers. It does not
require quotation marks. Proposals:
- **T1(a).** Keep the statement and move the 10-line proof to §5 (Lemma 5.1 already proves $\det Y=1$ there). T1(b)
  can then be one sentence. Keep T1(c) as is.
- **T2.** Drop the quotations in (b) and (c). Keep the equation numbers.
- **T3(a)–(e).** Keep (b) verbatim, since it is the hinge of the paper. Paraphrase the others.
- **T4.** Keep only the items used outside a single proof, and cite DLMF inline at the point of use for the others. The
  Mellin items are used only in the Remark at the end of App. A; move them there.

Expected saving is about 1.5 p. Also add one sentence to the opening of §2.5 telling the reader that it can be skipped
until §5.

**S13. Delete the empty Appendix D input and fix the appendix order.** Remove `\input{app_d}` (`main.tex:47`). Order the
appendices by first use: currently App. C is first used in §6 ((F7)), App. B in §7 and App. A inside App. B. If S1 adds
an appendix for the outer scalar, a natural order is: A = outer scalar (§6), B = a priori bound (§6, (F7)), C = $L^2$
bounds on a star, D = uniform resolvent (§7). Rename App. B's title "Proof of Proposition 7.4" to a descriptive one:
"Uniform invertibility of the comparison problem".

**S14. Unify the Prop. 2.5(iii) / $C_*$ material.** Proposition 2.5(iii) and the constant $C_*$ (`sec_2.tex:163–167`,
177–178) are never cited later: Lemma 5.4(iii) re-derives the hard-edge behaviour from the incomplete-beta expansion.
Either cite 2.5(iii) in the proof of Lemma 5.4(iii) or delete it.

---

## 3. Notation and terminology consistency

### 3.1 One symbol, two (or more) meanings: must fix

Ordered by risk of genuine confusion (same section pair, or both appear in one formula).

| # | Symbol | Meanings and locations | Fix |
|---|---|---|---|
| N1 | $\mathcal H_n$ | head set $\{k<n/M_0\}$ (`sec_4.tex:265`) **and** $H_n/H_n(0^+)$ (`sec_6.tex:393`) | Rename the second $\hat H_n$ or $H_n^\circ$. |
| N2 | $L_\pm$ | lens factors (5.x) `sec_5.tex:360` **and** seam logarithms (6.x) `sec_6.tex:242` (also $L_\ell$, the bidiagonal $L$, operator $L$ in App. A) | Rename the seam logarithms $\lambda_\pm$ or $\Lambda^{\rm s}_\pm$ (OUTLINE §4.4 already says "repo L± → χ_±": use $\chi_\pm$ as the densities). |
| N3 | $\Pi$ | $\sin\theta/\theta'$ (`sec_5.tex:113`) **and** the extraction functional $\Pi(X)$ (`sec_8.tex:20`) **and** the product in Lemma 4.3 (`sec_4.tex:223`) | Call the functional $\mathsf b(X)$ (pairs with $\mathsf a(X)$); call the product in Lemma 4.3 $\mathcal P_k$ or $\Pi_{k,n}$. |
| N4 | $\kappa$ | $((n-1)/n)^p$ §3; $\kappa_\pm=1/(1-e^{\mp2i\theta})$ §5; $\kappa\in(0,1)$ Lemma 6.5; $\kappa_\infty$ Lemma 6.7; $\kappa=-i/2\pi$ Lemma 7.1; $\hat\kappa$ App. B | Keep $\kappa_\pm$ (OUTLINE) and $\kappa_n$ (§3). Use $\varkappa_\infty$ or $\nu_\infty$ for Lemma 6.7, a plain number name ($\tau_0$) for Lemma 6.5, and $\mathsf k_0:=-i/(2\pi)$ for the Bessel log coefficient (used again in (7.x) and App. B (B3)). |
| N5 | $c_p$, $c_\pm$, $c_q$, $c_f$, $c_j$, $c_0$, $c_1$, $c'$, $c$ (generic) | The paper says $c$ is reserved for $c(p)$ (`sec_front.tex:461`, `sec_5.tex:51`), but: $c_p:=\min(1,p)$ (`sec_4.tex:230`, which looks exactly like $c(p)$); $c_\pm=e^{\mp i\pi\alpha}$ (§7, everywhere); $c_q$ (Lemma 6.6); $c_f$ (Lemma 6.8); $c_j$ (`sec_2.tex:54`); generic $c$ in `sec_6.tex:150, 365, 368`, `app_c.tex:76`, `app_a.tex` ($c_1$) | Rename $c_p\to\varsigma_p$ and $c_\pm\to\varrho_\pm$ (note $\epsilon_\pm$ is already used in Lemma 5.7); write generic small constants as $1/C$; rename the coefficients $c_j$ in (2.x) to $\beta_j$. Keep $c_0$ (strip constant) and $c_1$, but list them as the exceptions in the conventions line. |
| N6 | $m_n$ | spectral weights $m_n(k)$ §4 **and** the exponent in (O5) "$|F|^{\pm1}\le C_n|z|^{m_n}$" (`sec_5.tex:477`, `sec_6.tex:155, 526`) | Rename the exponent $N_n$; OUTLINE bans $N$ for the degree only. |
| N7 | $F$ | outer scalar **and** the local function $(4cz/\Upsilon)^{\alpha/2}$ in Lemma 7.3 Step 1 (`sec_7.tex:436`) **and** generic $F$ in Lemma B.1(c), App. C | Removed by S3 and S5; otherwise rename. |
| N8 | $\Phi$ / $\Upsilon$ | $\Phi(z)=2z-4c+2\mathcal R(z)$ (Lemma 6.6) **and** $\Phi_\alpha$ (Bessel model, §7) **and** $\Phi(\zeta):=M_n(z)$ (App. B Step 2); $\Upsilon$ (§7) is the same function as $\Phi$ | Call the conformal map $\Upsilon$ in both places (or $\mathcal J$), and the App. B local $\mathbb M$. |
| N9 | $\omega$ | arcsine law $\omega_\beta$ §2; oscillation $\omega(T)$ §4; Szegő ratio $\omega=D_W^2/W_0$ §§6–7 (heavily used); weight $\omega(\zeta)$ App. B | Keep $\omega$ for $D_W^2/W_0$. Use $\mathrm{osc}^*$ or $\Omega_L(T)$ in §4, $\mathrm{arc}_\beta$ or $\nu_\beta$ for the arcsine law, and $w_\beta(\zeta)$ in App. B. |
| N10 | $\Xi$ | circle terms $\Xi_k$ (7.x) **and** weight $\Xi(z)$ (App. B) | Rename the App. B weight $\varpi(z)$, which is free after N11. |
| N11 | $\varpi$ | coefficients $\varpi_j$ (§4); exponent $\frac12-\frac1{2p}$ (§6.3); scale $\varpi_n$ (App. B) | Use $\mathsf c_j$ in §4 and $\Lambda_n$ or $s_n$ (scale) in App. B. |
| N12 | $U$ | rescaled RH matrix §5; upper bidiagonal $U$ §3; potential $U^*$; discs $U(z_0,r)$; dilation $U_\lambda$ (App. A) | Matrix $U$ vs disc $U(0,\delta)$ co-occur ("$A_0$ analytic in $U(0,\delta)$" next to $U_{j2}$). Write discs as $\mathbb D(z_0,r)$ or $B(z_0,r)$. |
| N13 | $\Gamma$ | Gamma function; seams $\Gamma_\pm$ (§6.3); rays $\Gamma_\alpha$ (§7); star $\Gamma$ (App. A, B) | The seams $\Gamma_\pm$ sit next to $\Gamma(t)$ in §6.3. Rename the seams $\Sigma^{\rm seam}_\pm$. |
| N14 | $\theta$ | $\theta(z)=\pi t(z)$; $\theta=k/n$ in $g_p(\theta)$ (§4, defines $M_0$); exponent in examples; $\theta_0$ (Rem. 3.5); $\theta_j$ (App. A) | $g_p$ is defined with $\theta$, so §4 and §5 use $\theta$ for different things. Write $g_p(y)$, $y=k/n$, in §4. |
| N15 | $\hat\ell$ | jump function in Lemma 6.1 (`sec_6.tex:74`), visually the slowly varying factor $\ell$ | Rename $\beta(y)$ or $\phi_{\rm cut}(y)$. |
| N16 | $\gamma$ | $\gamma_p$; Euler's $\gamma$ (T4, Lemma 7.1(ii)); rays $\gamma_{1,2,3}$ (T2); arcs $\gamma_j$ (App. A) | Write Euler's constant as $\gamma_{\rm E}$. |
| N17 | $f$ | hard-edge conformal map (OUTLINE); first-variation direction $f=\log\psi$ (§4); rough perturbation $f(k)$ (§1.3, §10.3); $f:=Q_+-Q_-$ (App. C); $f_0$, $f_r$ | Use $\phi$ or $h$ in §4, $\mathfrak f$ in App. C (App. B already uses fraktur for data). |
| N18 | $H$ | $H_n$; $H$ in (2.x) `eq:CD-moments` and App. C proof | Rename the T3 integrand $\mathcal E$ or $\Delta$. |
| N19 | $A$, $B$ | $A_\pm$ (lens), $A_0,A_r,\hat A$; $A_\eta$ (Potter); $A(x)$ (Lemma 5.4); Ahlfors constant $A$ and matrices $A,B$ (App. B Step 3, T3(b)); $B$ Binet-cut scalar; $B(a,b)$ Beta; sets $S,B,N$ (App. B) | At minimum rename App. B's constant $A\to C_\Sigma$ and its sets $S,B,N\to\mathcal Z_{\le3},\mathcal Z_{\ge2},\mathcal Z_{23}$. |
| N20 | $E$ | super-small entries $E$; prefactor $E_n$; series $E_\nu$ (Lemma 7.1); constant $E_\infty$ (App. C) | Rename $E_\nu\to\mathcal I_\nu$ (or $e_\nu$) and $E_\infty\to C_Q$. |
| N21 | $C_n$ | Specific constant $-\frac{2\pi i}{p}n^{1+p-s}\ell_1(n)$ (5.x) **and** the convention "constants depend on $n$ only if they carry the subscript $n$" (`sec_5.tex:52`; App. C: $C_{n,\eta}$) | Rename the specific constant $\mathsf w_n$ or $\Omega_n$. |
| N22 | $\mathcal B$ vs $\mathcal I$ | Regularised incomplete beta is $\mathcal I_V(a,b)$ in Prop. 2.5 and $\mathcal B_y(a,\frac12)$ in Lemma 5.4(iii)–(iv) (`sec_5.tex:244–258`) | Use $\mathcal I$ throughout. |
| N23 | $q$ | $q_n(k)$ (§4); generic Szegő argument $q$; $q_2$; Hölder conjugate $q$ in T3(b) | Acceptable, but write T3's exponents as $r,r'$. |
| N24 | $N$ | OUTLINE: "no N anywhere". Used: $N$ (Lemma 2.1 proof), $N_r$ (Airy constant), $N_z$ (Lemma 6.6 proof), $N$ (App. B set) | Low risk; rename $N_r\to\mathsf N_r$ at least. |
| N25 | $p$ | node exponent **and** $L^p$, "$p=q=2$" in T3(b) and Prop. 7.7's proof (`sec_7.tex:592`) | Write $L^r$, $r=r'=2$. |

Lower-risk overloads worth a sweep: $\lambda$ (osc parameter, $\lambda_p$, $\lambda_\pm$, dilation, $\lambda_j$);
$\eta$ ($\eta_n$ rate vs Potter $\eta$ vs $\eta_0,\eta_*$); $\rho$ ($\rho_\ell$, $\bar\rho$, local $\rho$ in Prop. 4.5,
radii); $T$ ($T_0$, $T_n$, matrix $T$, operators $T_\pm$, numerics cut-off $T$); $S$ (strip $S_\vartheta$, matrix $S$,
$\mathsf S$, $S_{\rm in/out}$, $S=\log(n!/k!)$); $M$ ($M_0$, $M_1$, matrix $M$ of (7.x), region factor $M$ of (5.x),
Hölder constant $M$); $K$ ($K_n(k)$, $K(z)=(4c-z)^{-1/2}$, $K_\alpha$, $K=n|z|^{-1/p}$ in App. C, operator $K$ App. A);
$\psi$ vs $\psi^*$; $j$ (Binet) vs index $j$; $b$ (radius, App. C) vs $b_n$; $G$ (Gaussian) vs region $G$ (App. C).

### 3.2 Defined twice, or used before definition

- $\tilde D$, $j$, $DBK$, "Binet-cut", $e^\chi$, $S_{\rm in}$ appear in **Table 1** (end of §5, p. 33) before §6 defines
  them. Fixed by F2 (move the table).
- $T_n$ appears in Table 1's $\nu_p$ row before its definition in (7.x).
- $P_r$ (without hat) is used in (F5) (`sec_6.tex:627`) and `sec_7.tex:131` ("$\hat P_r=D_\infty^{-\sigma_3}P_rD_W^{\sigma_3}$")
  but **never defined**. Only $\hat P_r$ is defined, in (6.x) `eq:airy`. Either define $P_r:=D_\infty^{\sigma_3}\hat P_rD_W^{-\sigma_3}$
  or drop $P_r$.
- $W_r$ in App. B (`app_b.tex:186`, "the bounded factor $(D_W/W_r)^{\sigma_3}$ of T1(c)") is **never defined**.
- $D_n$ (Hankel determinant) appears in §1.3 ("$\log D_n$") and in Lemma 4.2's proof as $D_n(\sigma_\tau)$, without
  definition.
- "Proposition 2.5(iii)" and $C_*$ are defined but unused (S14).
- `(\mathrm A_{\vartheta_p})` is typed by hand in §5, §6 and the Frame Proposition, instead of the `\Ath` macro used
  elsewhere. Same output today, but it will diverge if the macro changes.
- "$\Lambda$ satisfies $(\mathrm A_\vartheta)$" (Lemma 4.1(iii), intro p. 3) applies a hypothesis defined for sequences
  $\ell$ to a function $\Lambda$. Add to Definition 1.3: "we also say that $\Lambda$ satisfies $(\mathrm A_\vartheta)$".
- Circular cross-reference: §7's (F5) says the Airy parametrix "has the two-scale structure (B.x) of Appendix B", while
  App. B (`app_b.tex:179`) says "we use the structure of the Airy parametrix provided by (F5)". Make (F5) the definition
  (it already says "(B2), (B3) of Lemma B.2") and have App. B cite (F5) only.

### 3.3 Repo jargon and drafting artefacts

- "**Paper 1**" as a name in the running text: `sec_5.tex:29` ("the equilibrium measure $\mu^*$ of Paper 1") and
  `sec_5.tex:153`; Figure 1, top box. Use "of [15]" or "the companion paper [15]". The footnote in §2
  (`sec_2.tex:35`) renders as "Paper [15] writes …"; change it to "The companion paper [15] writes …".
- `% src:` comments throughout contain repo codenames (RII, LW1′, UR′, REVIEW_Plan48, REVIEWED, "Rule R", G3prime N″,
  AGENTS.md). They do not print, but they are in the arXiv source. **Strip all comments before submission**, for
  example with `arxiv_latex_cleaner`. In particular `sec_back.tex:169–172` ("Coordinator: keep or drop", "REVIEWED but
  unpublished", "AGENTS.md rule 3") must not ship.
- Open TODOs in the source: `sec_front.tex:294` (Dai–Yao citation gate), `sec_back.tex:80` (Gragg–Harrod RKPW),
  `sec_back.tex:120` (CD equation (5.5) to re-check). Placeholders: author "Gordon [surname] (draft)", "repository URL
  and commit hash: to be supplied" (§9), Paper 3 provisional title in `refs.bib`.
- `app_d.tex` is an empty file whose comment says it is intentionally empty. Remove the `\input`.
- No forbidden vocabulary ("Law P", "novel", "first", "trivially", "obviously") was found in the printed text. Good.

### 3.4 Places where two sections disagree, or state the same result differently

(a) **(F4) differs between §6 and §7.** Proposition 6.9 (F4) gives $|E(z)|\le C\exp(-n|z|^{-1/p}/C)$. The §7.1 restatement
(`sec_7.tex:121`) gives $|E(z)|\le C\exp(-n|z|^{-1/p}/C)\,|z|^{-C}$, and §7 later uses the $|z|^{-C}$ form
(`sec_7.tex:491, 655`). One of them should be the statement. S2 removes the restatement; then check that §7's uses
follow from the §6 form, which is stronger.

(b) **"$|\alpha|<1$ is used in exactly three places"** (`sec_7.tex:62–66`). The list given is: the power-weighted Cauchy
bound, the integrability of $|\zeta|^{-|\alpha|}$, and the square integrability of $\tilde Q$. But App. C also uses it
for the a priori bound on $Q$ ($\eta<(1-|\alpha|)/2$, `app_c.tex:157–158`: "this is the place where $|\alpha|<1$ enters
the a priori bound"). The intro (`sec_front.tex:404`) names only App. B. Replace "exactly three places" by "in the
following places" and list all four, or list them once in Remark 7.8 and cite that remark from §1 and §7.

(c) **$D_{x^\alpha}^2$ is derived twice** (Lemma 6.6(i) as $(4cz/\Phi)^\alpha$, and Lemma 7.3 Step 1 as
$(4cz/\Upsilon)^\alpha$ with $\Upsilon=\Phi$). The formulas agree, but a reader will wonder whether they are different
functions.

(d) **Hölder exponent at 0 for $p>1$.** Table 1 gives $|\log(H_n/H_n(0^+))|\le C|z|^{1/p}$. (O3) and (F2) give
$C|z|^{\nu_p}$ with $\nu_p=\min(1/p,\frac12)$. The table is stronger than what is carried forward, which is consistent,
but say "($\le C|z|^{\nu_p}$ is what is used)" in the caption.

(e) **The Deift–Piorkowski quote is altered.** §1.3 quotes "the crucial Theorem 4.7 in [4] requires a different proof"
and glosses "[4] being [CD]". Remark 7.8 quotes "the crucial Theorem 4.7 in [CD] requires a different proof in this
case: now one needs to control the behaviour of the Cauchy operator acting on spaces with Muckenhoupt weights". Inside
quotation marks, "[4]" has been changed to "[CD]" and the spelling has probably been changed to "behaviour". Quote
verbatim once, with the gloss.

(f) **Lemma 6.6(vi)(a)** proves $|\omega|^{\pm1}\le C$ on the lips with the same three-factor split that Lemma 7.3 refines
to $\omega\to c_\pm$. This is consistent, but it is a seam. S3 resolves it.

(g) **Standing assumptions scope.** §5.1 says the assumptions hold "Throughout §§5–6 and Appendix C". §7 restates them.
§8, App. A and App. B rely on them silently. Say "Throughout §§5–8 and Appendices B–C".

(h) **Section 7 says it "must not re-derive anything from §6"** (OUTLINE §8, chunk D), but it does (S3). Any correction
to Lemma 6.6 would then need to be made twice. This is a maintenance risk as well as a reading problem.

No genuine contradictions between theorem statements were found. Theorems 1–4, (4.x) `eq:forms`, Step 1–5 of §4.4,
Remark 1.13 / 7.7, Conjecture 10.1 and Table 2 are mutually consistent. This includes the sign $-p/2$ of the $1/n$
coefficient of $a_n/(2b_n)$ (Lommel check: $-1$ at $p=2$, as in Table 2).

### 3.5 Spelling and typography

- British spelling is consistent in the paper's own text (normalise, organisation, behaviour, localisation,
  parametrised). The only American spellings are inside quotations ("neighborhood", "normalized"), which is correct.
- "Section~\ref" and "\S\ref" are mixed throughout, even within one paragraph (for example §1.4, §7 opening). Pick one.
  Amsart house style is "Section 5" in prose and "§5.3" for subsections.
- Five overfull boxes, the worst 70 pt in App. C (`app_c.tex:146–152`, the vertex-removability display). The others
  are `sec_5.tex:539–546` (7 pt), `sec_6.tex:396–399` (2.6 pt), `sec_7.tex:306–309` (9.6 pt) and `sec_7.tex:615–619`
  (9.3 pt).
- About 20 hyperref "Token not allowed in a PDF string" warnings come from math in section titles ("The $g$-function",
  "stability under $\ell/\ell_1\to1$", "The case $p>1$", …). Wrap them in `\texorpdfstring`.
- Unnumbered "Remarks on the Frame Proposition" (`sec_6.tex:696`) and the unnamed Remark at the end of App. A. Make
  them numbered remarks so they can be cited.

---

## 4. Line-level clarity

Each item gives the location, the original, and a proposed rewrite.

**L1. Lemma 5.5 statement is a run-on list that repeats itself** (`sec_5.tex:406–411`, p. 30).
> *Original:* "The functions $w$, $W$, $r_n$ and $W_0$ … are evaluated in this paper only at points of $\mathcal Z_n$:
> in the closures of $\Omega_b$ and $\Omega^\triangle$ (minus the point 0), which contain the band, the saturated
> segment, the lips, the vertical segments, $\Sigma^{\triangle\pm}$ and the top segment, and at the points of the lips and
> of the sectors … used in §7 and Appendix C, and on the top segment."

> *Rewrite:* "The functions $w$, $W$, $r_n$ and $W_0$ are evaluated only at points of $\mathcal Z_n$. Specifically, they
> are evaluated (a) in $\overline{\Omega_b\cup\Omega^\triangle}\setminus\{0\}$, which contains every arc of $\Sigma$
> except the parts of the lips outside the lens; (b) on the lips; and (c) in the sectors
> $\{|\arg z|\le\frac54\vartheta_{\rm lip}\}\cap U(0,\delta)$ used in §7 and Appendix C. The region $\Omega_\infty$ never
> uses the weight. Consequently $\xi(z)=\log t(z)$ always lies in $S_{\vartheta_p}$."

**L2. The lips bullet hides an existence argument in a parenthesis** (`sec_5.tex:277–285`, p. 29). Split it.
> *Rewrite:* keep the bullet as a definition ("The lips $\Sigma^\pm_{\rm lip}$ are $C^2$ arcs in $\mathbb C_\pm$ from $0$
> to $4c\pm ih_0$ such that: in $U(0,\delta)$ they are the preimages …; outside $U(0,\delta)$ they lie in
> $\{|\arg z|<\vartheta_{\rm w}\}\cap\{\Re\tilde\varphi>0\}$; they meet $U(4c,h_0)$ only at their endpoint."). After the
> list, add a separate sentence: "Such arcs exist. Near $0$, Lemma 5.4(iii) gives $\Re\tilde\varphi>0$ on
> $\{\delta\le|z|\le\delta_0,\ \frac34\vartheta_{\rm lip}\le|\arg z|\le\vartheta_{\rm w}\}$; along the band, Lemma
> 5.4(ii) applies at small height; near $4c$, Lemma 5.4(iv) applies on $|z-4c|=h_0$."

**L3. The "scalar −1" sentence is cryptic** (`sec_5.tex:398–400`, p. 30).
> *Original:* "The factor in $\Omega^\triangle_\pm$ is the product of the factors $\Pi^{-\sigma_3}(\cdot)$ and
> $V^\triangle_\pm$ of T1(b), moved into one step, except that in $\Omega^\triangle_-$ we have changed it by the scalar
> $-1$. With the literal product a constant jump $-I$ would appear on the saturated segment."

> *Rewrite:* "In [WLXZ] the saturated region is treated in two steps, first by $\Pi^{-\sigma_3}$ and then by
> $V^\triangle_\pm$. Our factor $A^\triangle_\pm\kappa_\pm^{\sigma_3}$ combines them, with one change: in
> $\Omega^\triangle_-$ we multiply by $-1$. Without this sign, $V$ would have the constant jump $-I$ on the saturated
> segment."

**L4. Double colon and run-on in the Airy paragraph** (`sec_6.tex:579–580`, p. 42).
> *Original:* "In the frame of $Q$ the global parametrix is the weight-free $P^\infty_0$, so no constant diagonal
> prefactor appears in $A_r$: the matching holds directly in this frame: on $\partial U(4c,\varepsilon)$, …"

> *Rewrite:* "Because the global parametrix in the frame of $Q$ is the weight-free $P^\infty_0$, no constant diagonal
> prefactor is needed in $A_r$, and the matching can be checked directly. On $\partial U(4c,\varepsilon)$ we have
> $|n^{2/3}f_r|\asymp n^{2/3}$, and …"

**L5. A drafter's hedge in the proof of Theorem 4** (`sec_8.tex`, p. 56).
> *Original:* "(If the off-diagonal entries of $P^\infty_0$ carry the opposite signs, or if $a$ is replaced by $a^{-1}$,
> these two values are unchanged.)"

*Rewrite:* delete it. The signs are fixed by (6.x). If robustness is the point, say it in Remark 8.2: "Only the band
$[0,4c]$ enters: $\mathsf b(P^\infty_0)=c^2$ and $\mathsf a(P^\infty_0)=2c$ do not depend on the sign conventions in
$P^\infty_0$."

**L6. The Lommel remark ends with an admission that undercuts it** (`sec_front.tex:222–224`, p. 4).
> *Original:* "We have confirmed numerically that these values agree … (to 90 digits for $n\le9$); we have not checked
> the identification of the masses against a source."

> *Rewrite (if the masses cannot be checked before submission):* "These values follow from the Lommel recurrence of
> [VA, §3] by the quadratic transformation $y\mapsto\pi^2y^2$; they agree with the coefficients computed from the
> Hankel determinants of the moments $\zeta(2j+2)$ to 90 digits for $n\le9$." Then actually check the masses. For
> $\nu=3/2$ the Lommel measure has masses proportional to $1/j_k^2=1/(\pi k)^2$, which can be verified in a line from
> the Mittag-Leffler expansion of $J_{\nu}/J_{\nu-1}$, and that removes the hedge.

**L7. "A short expansion gives" hides the only non-obvious computation of Remark 3.5** (`sec_3.tex:259`, p. 17).
> *Rewrite:* "Since $l_n=b_n^2/u_{n-1}=c^2n^{-2p}/((n-1)^{-p}(c+\theta_0(n-1)^{-1/2}))$, we get
> $\hat l_n=c\,\kappa_n\,(1-\frac{\theta_0}{c}n^{-1/2}+\frac{\theta_0^2}{c^2}n^{-1}+O(n^{-3/2}))$, hence $\hat b_n=c$ and
> $\hat a_n-2c=(\theta_0^2/c-pc)/n+O(n^{-3/2})$." (Check the $n^{-1/2}$ cancellation against $\hat u_n$ as written.)

**L8. Remark 3.6, "it follows that the pointwise law is insensitive to a point mass at 0"** (`sec_3.tex:270`). The
step needs one more clause: "(the laws for $\sigma$ and $\sigma+m\delta_0$ are both equivalent, by the converse and by
Theorem 2, to the law for their common image $x\sigma$)".

**L9. Long proofs with no plan sentence.** The style guide (§6.2) requires one; add these:
- Lemma 6.1 proof (`sec_6.tex:98`, 1.5 pp): "(i) is the absence of poles of $\Gamma$ in the sector; (ii) estimates the
  jump $\hat\ell$ from Stirling for large $|t|$ and from the reflection-free expansion (6.x) for small $|t|$; (iii) is
  Plemelj plus a splitting of the Cauchy integral at $|y|=|z|$; (iv) checks (O1)–(O5) one by one."
- (O5) part of the same proof (`sec_6.tex:145–160`). The "window argument" is used twice and spelled out once. State it
  once as a sublemma ("If $h$ is Lipschitz with constant $L|y|^{-1}\cdot|h|$ … then
  $\int h(y)/(y-z)\,dy$ is bounded up to the cut") and cite it in Lemma 6.5(iii) as well.
- Lemma 6.6 proof (`sec_6.tex:438`): "All parts use the representation (6.x) and a splitting of $(0,4c)$ into the
  near zone $|x-z|<\frac12|z|$ and the rest."
- Frame Proposition proof (`sec_6.tex:645`): "Items (F1)–(F6) collect the lemmas of §§5–6; the only new arguments are
  the uniform Carleson bound in (F1) and the arc-by-arc bound in (F5)."
- Lemma C.2 (lens sectors, `app_c.tex:56`): "Inside the lens the Cauchy sum has poles that $R$ removes; we move the sum
  onto the boundary of a sector by the residue theorem and bound the boundary integral."
- Proposition 7.6 (`sec_7.tex:590`): the first sentence is a citation. Add "We split $v-\tilde v$ into the lip mismatch,
  the circle terms and an exponentially small rest; the lip mismatch is estimated pointwise and then integrated using
  Bessel localisation."

**L10. Unexplained leap in Lemma 5.4(i)** (`sec_5.tex:234`): "choose $0<\varepsilon\le\min(|z|/2,4c)$; then $|z-y|\ge
y>y-\varepsilon$ …". The reader has to reconstruct why this gives $\Re g(z)>U^*(\varepsilon)$. Add: "so $|z-y|>|\varepsilon-y|$
for every $y>0$, and integrating against $\mu^*$ gives $\Re g(z)>U^*(\varepsilon)$." The local $\varepsilon$ also clashes
with the Airy disc radius $\varepsilon$ of §5.6; use $x_0$.

**L11. §2.5 T2(a): a promise without a pointer** (`sec_2.tex:285–286`).
> *Original:* "When the rays are moved by the angle freedom (b) below, the expansions of T4 (DLMF §10.40) give the same
> formula (6.28) in the enlarged sector; this is checked where it is used."

> *Rewrite:* "… in the enlarged sector (see the paragraph before Lemma 7.1)."

**L12. Lemma 4.1(ii) display** (`sec_4.tex:68–71`). "$\Lambda^{(j)}(\xi)-\delta_{j0}\Lambda(\Re\xi)$" uses the
Kronecker $\delta$ next to Dirac $\delta_{x}$ and disc radius $\delta$. State the two cases in words instead:
"$\Lambda(\xi)-\Lambda(\Re\xi)\to0$ and $\Lambda^{(j)}(\xi)\to0$ for $j\ge1$, uniformly in $|\Im\xi|\le\vartheta$".

**L13. Opening of §6.4 "Szegő functions"** (`sec_6.tex:375–390`) is a dense block of definitions ($\mathcal R$,
$D_q$, $D_q(\infty)$, multiplicativity, Plemelj, (6.x), $\eta_*$, $Z(r)$). Split it into two paragraphs: the definition
and its properties, then "We shall estimate $D_q^2/q$ near the band by means of the identity (6.x) …" followed by
$\eta_*$ and $Z(r)$.

**L14. §7 conventions** (`sec_7.tex:86–87`). "Constants $C$ may depend on … the radii $\delta,\varepsilon$ below". Here
$\varepsilon$ is the Airy radius, while $\varepsilon_\Lambda$ and $\varepsilon'_n$ appear four lines later. Write the
radius as $\varepsilon_r$, or say "the radii $\delta$ (at $0$) and $\varepsilon$ (at $4c$)".

**L15. Lemma 2.1 numbering of steps** (`sec_2.tex:92–95`). "Summing these $j+1$ steps" counts $j$ dyadic steps plus
one final step. Make this explicit: "($j$ dyadic steps and one final step)".

**L16. §9 "How the numbers were computed"** (`sec_back.tex:67–83`) is one 17-line paragraph. Split it after "This is a
property of the truncation, not a counterexample." The "−1.81, −13.3, −105.9" example is valuable; keep it.

**L17. Abstract, sentence 4.** "The proof has three parts. A Riemann–Hilbert analysis … controls the non-analytic factor
by a Conway–Deift comparison with a Bessel model instead of a local parametrix." This puts the hardest part first,
while the paper's order is shift, smoothing, RH. Either order is fine, but match the paper. Suggested: "The proof
reduces, by a Christoffel transformation (which shifts $s$ by $p$ and preserves the law with its rate) and a smoothing
step, to analytic factors and a window $1<s<1+2p$; there a Riemann–Hilbert analysis with nodes accumulating at a hard
edge controls the non-analytic factor by a Conway–Deift comparison with a Bessel model."

**L18. "In words, $(\mathrm A_{\vartheta_p})$ asks that $\ell$ extend … (for large $|t|$, and bounded near $t=1$)"**
(`sec_front.tex:142–143`). The strip is $\Re\xi\ge-c_0$, i.e. $|t|\ge e^{-c_0}$, so "for large $|t|$" is inaccurate.
Write "on $\{|t|\ge e^{-c_0},\ |\arg t|\le\vartheta_p\}$".

---

## 5. Figures and tables

**Figure 1 (dependency diagram, p. 7).** Useful, legible, correctly referenced and correctly captioned.
- Replace "Paper 1:" in the top box by "[15]:" or "Equilibrium measure $\mu^*$ [15]".
- If S10 is adopted, relabel Theorem 2 as Corollary.
- The arrow labelled "$\ell\equiv1$" from the analytic box to Theorem 2 crosses the diagram diagonally. Consider placing
  Theorem 2 directly under "analytic $\ell_1$, every $s>1$".

**Figure 2 (contour, p. 29).** Useful, but has three problems.
1. Labels in `\tiny` and light grey ("no jump", "$S_{\rm in}$", "$\Omega_b^+$", "$\Omega^\triangle_+$") are illegible in
   print. Use at least `\scriptsize` in black.
2. Panel 1 draws the "Bessel rays" as dashed rays at $\pm120°$ **in the $z$-plane**. The Bessel rays live in the
   $\zeta=n^2f(z)$ plane, and their preimages are the lips. Drawing them in the $z$-plane suggests a jump contour that
   does not exist. Either drop the dashed rays, or add a small inset in the $\zeta$-plane showing the three rays
   $\arg\zeta=\pi,\pm(\pi-\vartheta_{\rm lip})$, labelled "image under $\zeta=n^2f$".
3. The OUTLINE planned panels for $p>1$, $p=1$, $p<1$. Merging $p\ge1$ into one panel is fine, but say so in the
   caption. The global panel omits the top segment and the vertical segments $\Sigma_v^\pm$, which are both named in
   the text; label them.

**Table 1 (geometry table, p. 33).** Valuable, and it is the one place a reader can see what depends on $p$. However:
1. It is placed at the end of §5, before §6 defines most of its entries ($\tilde D=e^{-j}$, $DBK$, Binet-cut, $e^\chi$,
   $S_{\rm in}$). It also cites lemmas 6.1–6.4 and the $T_n$ of §7. **Move it to the start of §6**, after the
   introductory paragraphs that define $j$, $\tilde D$, $D$ and $K$. Delete "Table 1 at the end of this section" at
   `sec_5.tex:38`.
2. Row "classical quotient parametrix at 0: works with a seam glue (not used)" for $p<1$ is not explained anywhere in
   the paper. Either add a sentence to Remark 6.3 or drop the entry.
3. Row "$\nu_p$ (in $\varepsilon'_n=\dots$)": write "Hölder exponent $\nu_p$ (§5.9)" and drop the $\varepsilon'_n$
   formula, which is defined only in §7.
4. Row "$|\log\frac{H_n(z)}{H_n(0^+)}|$ near 0": add "(only $\le C|z|^{\nu_p}$ is used)" in the caption (see §3.4(d)).

**Table 2 (numerics, p. 58).** Clear, well captioned and honest about what is observed versus proved. It is referenced
correctly. Minor points:
- The header "$\ell(k)=e^{\sqrt{\log(k+e)}}$" is repeated in two columns. Use $\ell$ and $\ell\equiv1$ in the column
  heads, and define $\ell$ once in the caption.
- "Source: supplementary script `table2`" will need the repository URL that §9 promises.

---

## 6. The ten highest-impact edits, in order

1. **Notation sweep for the hard clashes** (§3.1 N1–N8, N21–N22): $\mathcal H_n$, $L_\pm$, $\Pi$, the six $\kappa$'s,
   $c_p$/$c_\pm$/generic $c$, $m_n$, local $F$/$\Phi$/$\Upsilon$, $C_n$, $\mathcal B$ vs $\mathcal I$. Also define $P_r$ and
   $W_r$, which are currently undefined. This is the single biggest readability gain per hour.
2. **Move the three geometry constructions (§6.1–6.3) to an appendix** and state the outer scalar as one lemma (S1).
   Move Table 1 to the start of §6 (Figures/tables item 1).
3. **Delete the (F1)–(F8) restatement in §7.1** and resolve the (F4) discrepancy (S2, §3.4(a)).
4. **Make Lemma 7.3 cite Lemma 6.6** instead of re-deriving the Szegő estimates under new names (S3, §3.4(c)).
5. **Tell the comparison-method story once.** Shorten §1.4's three hard-edge paragraphs to one, delete the verbatim
   repeat in §7, and keep the remark about not continuing across $(-\delta,0)$ in two places, not five (S6).
6. **Get Theorem 1 onto p. 2** by moving part (ii) and $\rho_\ell$/$M_0$ after the theorem, and demote Theorem 2 to a
   corollary (S9, S10).
7. **Add the RH roadmap paragraph at the start of §5** (S11). Also list the uses of $|\alpha|<1$ once and accurately
   (§3.4(b)).
8. **Consolidate the extraction invariance (S4) and the Cauchy-integral criterion (S5)**, removing two duplicated
   proofs.
9. **Slim the Tools subsection** by turning quotations into statements (S12), and remove the remaining restatements in
   the S7 table.
10. **Pre-submission hygiene.**
    - Strip all `%` comments, including the "Coordinator" note.
    - Resolve the three TODO citation gates.
    - Remove `\input{app_d}`.
    - Fix "Paper 1" in the text and in Figure 1.
    - Fix the 70 pt overfull box and the `\texorpdfstring` warnings.
    - Make Figure 2's labels legible and remove its $z$-plane "Bessel rays".
    - Drop or trim §10.2 and §10.4 (S8).
    - Remove the two hedging sentences (L5, L6).

**Expected outcome:** about 58–60 pp, a main line of about 50 pp, and a reader who sees the result on p. 2, the
strategy by p. 5, and the hard edge by about p. 38 instead of p. 45.
