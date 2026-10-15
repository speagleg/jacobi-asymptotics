# Rule R referee report 2: Paper II, the p ≤ 1 material (§§10–11, Apps. G–H, Thm 1.4, Rem 1.7, §2 additions, Tables 12.3–12.4, §13) and the Step-1 fixes

Reviewer: independent second reader (Rule R). Worktree `ja-plan70`, branch plan-70-paperII, read at HEAD 950746b.
This is a report only: no paper file was edited. Numbering below is that of the current build (main.aux): Lemmas 10.1–10.4,
Prop 10.5, Lemmas 10.6–10.7, Prop 10.8, Rem 10.9; Lemma 11.1 (fold), 11.2 (comparable), 11.3 (Christoffel 1+εx),
11.4 (sandwich), Prop 11.5 (transfer), Lemma 11.6 (TC data), Cor 11.7, **Lemma 11.8 (differences in s)**, Prop 11.9,
Lemmas 11.10–11.11, Prop 11.12, Thm 11.13, Rem 11.14; Lemma G.1; Lemmas H.1–H.7; Conj 13.1 (alternating), 13.2 (tilt).

Sources compared (REVIEWED, master `jacobi-asymptotics`): research/G1/RH/second_order/E_plt1.md (+ REVIEW_Plan67_A/B),
E_p1.md (+ REVIEW_Plan66_A/B), E_pgt1.md, UL.md, SECOND.md Thm 3.2, research/G1/RH/RH_p1_general.md, RH/CITATIONS.md, and
the check outputs check_e_plt1_num.out, check_e1_rate.out, check_e1_tc.out, check_so_grid.out.

## 0. Re-derivations and checks run

Scratch: `scratchpad/refR2/` (venv python, sympy/mpmath; no installs).

- `exact_d.py` (sympy). I rebuilt the soft-edge Laurent computation (the inputs Q₀, X and the Lemma 9.3/E.4 closed forms
  as in check_e_plt1_sym.py) but kept the weight factor **exactly**: −ω ↦ −ω^mod·exp(𝖽𝓡), expanded to all orders in 𝖽
  (the u-series is truncated only at the order the double pole needs). Results:
  - odd powers of u vanish for every 𝖽; 𝔅_{r,𝖽} = 𝔅_r;
  - (𝔄_{r,𝖽})₂₁ − (𝔄_{r,𝖽})₁₂ − ipc(1+α−2c𝖽) = 0 and
    (𝔄_{r,𝖽})₁₁ − (𝔄_{r,𝖽})₂₂ − 2i(𝔄_{r,𝖽})₁₂ − (i/c)(𝔅_{r,𝖽})₁₂ + pc(α+2−2c𝖽) = 0, identically in 𝖽.
  So (10.9) is **exact** in 𝖽, not only first order. Stronger: the full matrix satisfies 𝔄_{r,𝖽} = 𝔄_r|_{α↦α−2c𝖽}
  exactly (it is quadratic in 𝖽 through 12p(α−2c𝖽)²). Its 𝖽-derivative at 0 is Lemma G.1's matrix.
- `tc.py` (sympy). Lemma 11.6(c): the paper's a_n(x²σ_TC) equals E_p1's closed form (4n+7)(2n²+7n+8)/(2(n+1)(n+2)(2n+3)(2n+5)).
  The fold (11.4): mb_m = ½(1 + (𝖿₀+½)/(2m)), ma_m = 1 + (𝖿₀−½)/(2m). Rem 11.14: nu_{n−1} = ½(1 + (1+𝖿₀−𝖿₁)/(2n)).
- By hand: Lemmas 11.1–11.4, Prop 11.5 (all three parts, including the second-order Christoffel expansion), Lemma 11.6(a)–(d)
  (transfer formulas J = LU ↦ UL, every rational function and its expansion), the Stirling identity (11.3) with
  f₀ = 1/(288k²) + O(k⁻³), Cor 11.7 (the constants −1/12, −1/24, 3/32 − 1/24 = 5/96, 19/32 − 1/24 = 53/96, and 𝖿₁ = 0, −3 from
  the explicit chains of σ_TC and xσ_TC), **Lemma 11.8 in full** (§2 below), the p = 1 value argument, Lemma 10.1(iii)
  (Mellin computation and the reflection formula), Lemma 10.2, Lemma 10.3(i) on the whole discs, the extraction of §10.5
  (both 𝗄_p terms), the Ψ_α bounds near 0 on the moved rays, the App. H identification argument, the a = 0 amplification
  bound, the phase φ₊(0) = −πi/2 and i^{Nσ₃}, and the circle-at-2 expansion Δ^{(3/2)}.
- Tables 12.2 (rows p ≤ 1), 12.3, 12.4 compared entry by entry with check_so_grid.out, check_e_plt1_num.out,
  check_e1_tc.out and check_e1_rate.out (§6).

## 1. Verdict per section / lemma

| Item | Verdict | Findings |
|---|---|---|
| Thm 1.4 statement; abstract | ACCEPT WITH MINOR FIX | m1 (abstract wording) |
| Rem 1.7 | ACCEPT | constants = E_p1 Thm E1.6 |
| §1 external-results paragraph (WLXZ reliance) | ACCEPT WITH MINOR FIX | m2, m3 |
| §2.4 (WLXZ list), §2.5(d), §2.7(e) | ACCEPT WITH MINOR FIX | m3, m4 (Rule C bookkeeping) |
| Lemma 10.1, 10.2 | ACCEPT | — |
| Lemma 10.3 (bound (10.5) on whole discs) | ACCEPT | proof checked, correct |
| Lemma 10.4 (glued parametrix) | ACCEPT WITH MINOR FIX | m5 (seam derivative claim: true, under-argued) |
| Ψ_α bounds near 0 on the moved rays (before Lemma 10.4) | ACCEPT | correct, own argument |
| Prop 10.5 (M1-corrected Step 2 for p < 1) | ACCEPT | — |
| Lemmas 10.6, 10.7 ((10.9) exact in 𝖽) | ACCEPT | exactness verified; optional I1 |
| Prop 10.8, proof of Thm 1.4 (0 < p < 1), Rem 10.9 | ACCEPT | — |
| App. G (Lemma 10.1(iv)–(v); Lemma G.1) | ACCEPT | optional I1 |
| Lemmas 11.1–11.4, 11.6, Cor 11.7 | ACCEPT | — |
| Prop 11.5 | ACCEPT WITH MINOR FIX | m6 (hypothesis of (i) vs its use on (xw, xv)) |
| **Lemma 11.8** | **ACCEPT** | correct, needs no tail bound (§2) |
| p = 1 value argument (§11.6) | ACCEPT | no circularity; O(1) suffices (§2) |
| Prop 11.9, Lemmas 11.10–11.11, Prop 11.12, Thm 11.13, Rem 11.14 | ACCEPT (PROVED-mod-cite + the stated WLXZ reliance) | m2 |
| App. H | ACCEPT WITH MINOR FIXES | m7 (notation clashes) |
| Tables 12.2 (p ≤ 1 rows), 12.3, 12.4 and their text | ACCEPT | all numbers match the outputs |
| Conj 13.1 | ACCEPT | honest |
| **Conj 13.2 (tilt)** | **REJECT AS STATED** | **MA1: false for every 0 < p < 1** |
| §13 text | ACCEPT WITH MINOR FIX | m8 |
| Step-1 fixes (commit 3e6f87d): M1, m1–m6, m8 | ACCEPT | all applied correctly (§7) |

No critical finding. One major finding (MA1), in a conjecture; it touches no proof.

## 2. Lemma 11.8 and the p = 1 value argument (flagged item 1)

**Re-derivation.** For s ≥ t, h_n(s) ≤ ∫(P_n^{(t)})²dσ_{p,s} = h_n(t)·E_n^{(t)}[k^{t−s}] by the minimum property (Lemma 11.4
with general nodes). With Y = n^px_k = (n/k)^p one has k^{t−s} = n^{−(s−t)}Y^r, r = (s−t)/p. Hence
F_n(s) − F_n(t) ≤ log E[Y^r] ≤ r log(n^p a_n(t)), by Jensen for the concave y^r (r ∈ [0,1]) and E_n[x] = a_n. For the lower
bound the paper uses the exact identity F_n(t+p) − F_n(t) = log(n^p u_n(t)) (from h_n(xσ) = u_n h_n(σ) and
xσ_{p,t} = σ_{p,t+p}) together with the upper bound from base point s to t+p. This gives

  log(n^p u_n(t)) − r′ log(n^p a_n(s)) ≤ F_n(s) − F_n(t) ≤ r log(n^p a_n(t)).

By Cor 1.3, n^pa_n → 2c at s and t. By Lemma 3.4, n^pu_n(t) → c > 0. So both sides are bounded. Chaining steps of length
≤ p gives all s, t > 1. The second claim follows from h_n = ζ(s)∏b_j². **Correct.**

- *No tail bound.* Confirmed. UL Lemma V(D) bounds F_n(s) − F_n(t) from below by a **negative** moment of Y, which needs
  the hard-edge tail bound QLP(c). Lemma 11.8 avoids it: it takes the lower bound from the exact shift identity at t + p
  and then uses only positive moments. Inputs: Cor 1.3 (proved in §§4–7 by the comparison method, independent of §§10–11)
  and Lemma 3.4. This is a genuine simplification over UL Thm UF.
- *Relation to the reviewed results.* Lemma 11.8 is the pointwise-in-(s, t) O(1) form of UL Thm UF / Cor UL-3.8. UF-lim
  (REVIEWED) gives F_n(s) − F_n(t) → ((s−t)/p) log c(p), uniformly on compacts. That is a limit, with uniformity, so it is
  strictly stronger. At s = t + p, Lemma 11.8 is SECOND Thm 3.2 with O(1) in place of the limit. So Lemma 11.8 is a
  correct, weaker statement, consistent with both.
- *Value argument.* Thm 11.13 gives 𝖿₀(s) for every s > 1, so nb_n(σ_s) = ½(1 + d(s)/n + O(n⁻²)) and
  Σ_{j≤n} log(b_j(s)/b_j(3/2)) = (d(s) − d(3/2)) log n + O(1). The O(n⁻²) terms are summable. Lemma 11.8 makes the left side
  −((s−3/2)/2) log n + O(1). The difference of the two coefficients times log n is then bounded, so the coefficients are
  equal; o(log n) would also suffice. d(3/2) = −¼ comes from Cor 11.7, which is elementary: Prop 11.5 plus the explicit
  data of σ_TC and Stirling, with no RH input and no use of Thm 1.4. **No circularity.** Cor 1.3 at p = 1 is proved through
  Thm 1.2 (comparison), not through §11. Thm 11.13's existence statement does not use the value. Check: 𝖿₀(3/2) = −1 and
  𝖿₀(5/2) = −2 (Cor 11.7) agree with 𝖿₀ = ½ − s.

Recommendation (INFO): the drafter's remark in NOTES that Lemma 11.8 "has not had a Rule R review" can now be closed.

## 3. Findings

### Major

**MA1. Conjecture 13.2 (tilt) is false as stated for every 0 < p < 1, and it now contradicts Theorem 1.4(ii).**
Location: sec13_further.tex lines 44–50 (statement), with the reference in sec1_intro.tex line 154 and the captions of
Table 12.1 (sec12_numerics.tex lines 75, 86).

*Counterexample.* Let 0 < p < 1, 0 < ε < 1, ℓ(k) := 1 − εk^{−p}, so Λ(ξ) = log(1 − εe^{−pξ}). This Λ is analytic of every
angle (Definition 1.1 holds with c₀ small: |εe^{−pξ}| ≤ εe^{pc₀} < 1), and Λ′(log n) = pεn^{−p}(1 + O(n^{−p})). Hence
nΛ′(log n) = pεn^{1−p}(1 + o(1)) → +∞, so the conjecture applies. But σ_{p,s,ℓ} = (1 − εx)σ_{p,s} is an exact polynomial
Christoffel transform.

- The proof of Lemma 11.3 works verbatim with z₀ = 1/ε > 1, outside the support. It gives
  h_n(σ_ℓ)/h_n(σ) = 1 − εa_n − ε²b_n²/(…) ∈ [1 − ε, 1].
- With Theorem 1.4(ii) for σ_{p,s}, it follows that
  log(b_n(σ_ℓ)²/b_n(σ)²) = −ε(a_n − a_{n−1}) + O(n^{−1−2p}) = 2pcε n^{−1−p} + O(n^{−1−2p} + n^{−2−p}).
- Therefore
  n^pb_n(σ_ℓ)/c = 1 − (s−1)/(2n) + (𝗄_p + pcε) n^{−1−p} + o(n^{−1−p}).
- The conjecture predicts 1 − (s−1)/(2n) + (pε/2) n^{−1−p} + o(n^{−1−p}).
- The difference of the n^{−1−p} coefficients is 𝗄_p − pε(½ − c(p)). This is < 0 for every ε, because 𝗄_p < 0 and
  c(p) ≤ ½ for p < 1.

There are two independent reasons for the failure. The pure-power term 𝗄_pn^{−1−p} is not o(Λ′/n) when Λ′ ≍ n^{−p}. And
the response to Λ′ at that scale has the coefficient c(p)·p, not p/2. At p = 1 the two coincide (c(1) = ½), which is
exactly Prop 11.5(i).

*Fix.* Replace the hypothesis by one under which both effects are lower order. In sec13_further.tex line 49 replace

  `\qquad\text{whenever}\quad n\Lambda'(\log n)\to\infty.`

with

  `\qquad\text{whenever}\quad n^{\min(1,p)}\Lambda'(\log n)\to\infty.`

and add after the conjecture:

> For $0<p<1$ the stronger condition is needed. For $\ell(k)=1-\epsilon k^{-p}$ the measure $\sigma_{p,s,\ell}=(1-\epsilon
> x)\sigma_{p,s}$ is a polynomial Christoffel transform, $\Lambda'(\log n)\asymp n^{-p}$, and the argument of
> Lemma~\ref{lem:pone-christoffel} together with Theorem~\ref{thm:onen}(ii) gives the coefficient
> $\mathsf k_p+p\,c(p)\epsilon$ of $n^{-1-p}$, not $\frac12p\epsilon$.

The amended statement is consistent with Table 12.1: at p = ½, Λ′(log n) ≍ (log n)^{−1/2} ≫ n^{−1/2}. NOTES §8 also lists
this conjecture as a cross-reference target for Paper III ([II, Conj 13.2]). Paper III's use of it must be re-read with
the amended hypothesis.

### Minor

**m1. Abstract, sec1_intro.tex line 19: the n^{−1−p} term is ambiguous.** "both carry the further term
$2p\,c(p)\zeta(-p)\,n^{-1-p}$" reads as an absolute term of n^pb_n and n^pa_n. The theorem has 𝗄_pn^{−1−p} **inside** the
brackets, i.e. absolute terms c(p)𝗄_p and 2c(p)𝗄_p. Replace with:
> for $0<p<1$ both brackets carry the further term $\mathsf k_pn^{-1-p}$, $\mathsf k_p:=2p\,c(p)\zeta(-p)$, which cancels in
> $a_n/(2b_n)$.

**m2. §1 reliance sentence (sec1_intro.tex lines 140–142) is narrower than §11.** §11 (after Prop 11.9) and App. H name two
points taken from WLXZ: (a) the O(e^{−cN}) bound on the **lens and** saturated contours, uniformly up to the largest node;
(b) the uniform L²(Σ_𝖷) bound for the Cauchy operator on the growing contour. §1 names only (a), and only the saturated
region. For honesty, replace "it relies on the bounds of \cite{WLXZ} for the jumps on the saturated region, which are
uniform up to the largest node and are justified there only briefly" with:
> it relies on two steps of the analysis of \cite{WLXZ} that we do not prove again: the exponential bounds for the jumps on
> the lens and saturated contours, uniformly up to the largest node, which are justified there only briefly, and the uniform
> boundedness of the Cauchy operator on the final contour used in their small-norm argument

The rest of the sentence and the §11 paragraph are accurate. This is a faithful account of RH_p1.md "Reliance noted" and
RH_p1_general §8. The WLXZ equation ranges (4.14)–(4.20) and (4.22) are all quoted verbatim in RH/CITATIONS.md: (4.14)
via (2.6), (4.15)–(4.20) and (4.22) in "(WLXZ-v1, Plan 53)", (4.16)–(4.17) in "(WLXZ-v1)". The range deliberately excludes
the unquoted (4.21).

**m3. Rule C bookkeeping for WLXZ.**
- WLXZ **(4.24)** is cited in the paper: §2.4 list; App. H Lemma H.1 proof and "The circle at 2", "(2.15), (3.4), (3.7),
  (4.15), (4.24)". The "(Plan 66 reuse)" summary of RH/CITATIONS.md lists it, but no entry quotes it verbatim. Quote it.
- Inside cited ranges, (1.7), (3.8), (3.13)–(3.14) are not quoted. Either quote them or narrow the ranges:
  (1.4)–(1.6), (1.8)–(1.9); (3.6)–(3.7), (3.9)–(3.12), (3.15).
- (5.11) (the explicit 𝒩) is referenced but not transcribed. App. H uses (𝒩₁)₁₂ = −ie^L and (𝒩₁)₂₁ = ie^{−L} from it, so
  transcribe it.

These are record fixes in research/G1/RH/CITATIONS.md, plus at most a range edit in sec2_prelim.tex lines 136–141.

**m4. §2.5(d) does not state all KV facts used later.** Lemma H.7 uses KV (5.4), (5.5) (size of P near 0, inside and
outside the lens) and KV (5.18), (5.20) (the lip jumps are lower triangular). All four are recorded READ in RH/CITATIONS.md
(KV, additional verbatim quotes), but the §1 sentence promises that every external result is stated in §§2.4–2.7. Add to
§2.5(d), after "the behaviour at $0$ of \cite[(5.21)--(5.22)]{KV}":
> ; the jumps on the four lip rays are lower triangular \cite[(5.18), (5.20)]{KV}, and the parametrix is
> $O\bigl(\begin{smallmatrix}1&|z|^{2\alpha+1}\\1&|z|^{2\alpha+1}\end{smallmatrix}\bigr)$ as $z\to0$ if $\alpha<-\frac12$, while for
> $\alpha>-\frac12$ it is $O(1)$ outside the lens and
> $O\bigl(\begin{smallmatrix}|z|^{-2\alpha-1}&1\\|z|^{-2\alpha-1}&1\end{smallmatrix}\bigr)$ inside \cite[(5.4)--(5.5)]{KV}

(KV's α is a = α + ½ here, so KV's |z|^{2α} becomes |z|^{2α+1}.)

**m5. Lemma 10.4(i), sec10_plt1.tex lines 248–251: the seam-derivative claim is correct but one line is thin.** "the
boundary values of $G$ on the seams have derivatives bounded by $Cn^C$ (by (10.3), after an integration by parts)". I
checked it. 𝔎(ζ, z) = 1/(ζ − z) − 1/(ζ − 1), so ∂_z𝔎 = (ζ − z)^{−2} = −∂_ζ(ζ − z)^{−1}. Integrating by parts along each
ray, with no boundary terms because 𝔧(0⁺) = 0 and 𝔧(r)/(re^{±iθ} − z) = O(r^{−1}log r) → 0 at ∞, makes G′ the Cauchy integral
over the two rays of 𝔧′. Here 𝔧′ is real-analytic and |𝔧′(r)| ≤ C/r overall. On the seam segments in 𝔻(0, 2δ),
|𝔧′| + |𝔧″| = O(e^{−n/C}). Away from the disc, |𝔧′| = O(e^{−n/C}) for r ≤ cn^p and ≤ C/r beyond. So the boundary values of
G′ on the seams in 𝔻(0, 2δ) are O(log n). Suggested replacement for the parenthesis:
> (by~\eqref{eq:plt1-repr}, $\partial_z\mathfrak K(\zeta,z)=-\partial_\zeta(\zeta-z)^{-1}$, and an integration by parts writes
> $G'$ as the Cauchy integral over the two seams of $\pm\mathfrak j'$, which is $O(e^{-n/C})$ with its derivative on the seam
> segments in $\mathbb D(0,2\delta)$ and $O(1/r)$ beyond, so the boundary values of $G'$ there are $O(\log n)$)

**m6. Prop 11.5, sec11_pone.tex lines 129–141: the hypothesis of (i) does not match its use on the pair (xw, xv).**
Hypothesis: "a_n and b_n of v and of xv are O(1/n)". The proof of (ii) applies (i) to the pair (xw, xv), and the proof of
the u-part of (iii) applies (i)/(iii) to it. Read literally, that requires bounds for x²v. For Cor 11.7 at s = 5/2,
x²v = x³σ_TC, whose coefficients are not given in closed form (E_p1 Remark (3) notes exactly this at s = 7/2). The proof of
(i) itself uses only the coefficients of v: the Christoffel factor through a_n(v), b_n(v), and the moments of v′ and w
through comparability with v. Fix: in (i) assume only "a_n and b_n of v are O(1/n)", and keep the definition of
"regular" (which includes xv) for (ii)–(iii). Then (i) on (xw, xv) needs only the bounds for xv, which regularity of v
supplies. The second-order moments in (iii) for the pair (xw, xv) need n a_n, n b_n of xw and x v′ to O(1/n). The proof of
(ii) already supplies these through (eq:transfer) relative to xv. Nothing about x²v is needed. Concretely, line 130–131:
"such that $a_n$ and $b_n$ of $v$ and of $xv$ are $O(1/n)$" → "such that $a_n(v)$ and $b_n(v)$ are $O(1/n)$". At the
start of the proof, line 147–148, keep "and $xv'$, $xw$ with $xv$" under the regularity assumption of (ii)–(iii).

**m7. App. H notation clashes** (appH_pone.tex). Not errors, but a reader will stumble:
- line 14: ℓ(z) := 1 + |log|z|| clashes with the slowly varying factor ℓ of the whole paper (and "ℓ ≡ 1" of §11).
  Suggest 𝔩(z) or \mathsf L(z).
- line 187: δ := 4m + 2 − 2|a| clashes with the disc radius δ of §§8–10 and with δ₀ in Lemma H.6. Suggest 𝗊 or δ_m.
- line 239: G := {0 < |z| < b, |arg z| < φ₀} (domain) and, line ≈344, G := D̃²/w̃ of WLXZ (6.12) in the same appendix.
  Suggest 𝒢 or Ω_b for the domain.
- line 356: in e^{jσ₃}… X_j…, j is both Binet's j(N/z²) and the sector index. Write the sector index as q or k (as in
  Lemma 11.10(b), which uses q for the quadrant).
- "a := α + ½" (line 13–14): acceptable, since it is declared local and used only in exponents. With the recurrence
  coefficient a_n and with a_* of §9, consider \mathsf a, though nothing is ambiguous in context. The local notation
  matches E_plt1/RH_p1_general, so no conversion error arises: I checked that every occurrence of a in App. H is α + ½,
  including δ ≥ 2 ⇔ m ≥ |a|/2, which is the m of Prop 11.9.

**m8. §13 line 33: "the expansion of the band factor ... continues with the term ζ(−2p)(z²−1)/(2n^{2p})".** That is the
next term of G − G(1) (Lemma 10.1(iv) with 𝖬₂). The band factor H_n = e^{−2G} has −ζ(−2p)(z²−1)n^{−2p} in its logarithm.
Replace "the expansion of the band factor in Lemma~\ref{lem:plt1-band} continues with the term" with "the expansion of
$G$ in Lemma~\ref{lem:plt1-band}(iv) continues with the term".

### Info (no change required)

- **I1 (flagged item 2a, exactness in 𝖽).** (10.9) is exact; I verified it to all orders (§0). The hand argument in the
  proof of Lemma 10.7 is correct for the following reason. All α- and 𝖽-dependence of 𝔄_{r,𝖽}, 𝔅_{r,𝖽} enters through
  the odd series L_r − ½𝖽𝓡. The residue at the double pole needs that series only through order ε, and its ε-coefficient
  is 1 + α − 2c𝖽. So in fact 𝔄_{r,𝖽} = 𝔄_r|_{α↦α−2c𝖽} for the whole matrix. Optional: say so after Lemma 10.7 ("in fact
  $\mathfrak A_{r,\mathsf d}$ is $\mathfrak A_r$ with $\alpha$ replaced by $\alpha-2c\mathsf d$"). The App. G closing sentence
  ("verified … to first order in 𝖽") is accurate as written; if the editor wants, add "and the two combinations
  \eqref{eq:plt1-combinations} to all orders in $\mathsf d$". The full matrix is quadratic in 𝖽 (not affine), as stated.
- **I2 (flagged 2b, (10.5) on whole discs).** Correct. With x₀ the point of [0, 4c] nearest to Re z, |x − x₀| ≤ |x − z| for
  x ∈ [0, 4c]. 𝖤_n is Cn^{−2p}-Lipschitz on [0, 4c] by Lemma 10.1(v) (derivative bound on 0 < x ≤ ½r_*, continuity at 0,
  4c < ½r_*). (5.x) eq:szego-repr holds with any constant 𝔠. The second term uses the sup bound with sector values.
  Lemma 10.3(i) is what (10.8)'s "|ρ_n^{±1}| ≤ C on the disc" needs, so the strengthening over E_plt1 (circles only) is
  both needed and proved.
- **I3 (flagged 2d, Ψ_α near 0 on the moved rays).** Correct. In the thin sectors the model is KMVV's (Hankel formulas).
  In the central sector the first column is ζ^{α/2}·entire by (10.25.2), hence O(|ζ|^{α/2}) ≤ C|ζ|^{−|α|/2}. The second
  column agrees with KMVV's in every sector, because KMVV's jumps on ±2π/3 are lower triangular and right multiplication
  by [[1,0],[x,1]] fixes the second column. So the column bounds of KMVV (6.19)–(6.21) hold. (Equivalently, the moved first
  column is KMVV's first column plus a constant times the second.)
- **I4 (flagged 2e, Step 2 for p < 1).** Prop 10.5's rerun of the M1-corrected Step 2 is correct.
  - α > −½: R is continuous up to the seams, because Q has no seam jump and P̌₀'s seam boundary values are continuous.
    The vertex condition comes from (R-at-zero), whose inputs hold for the seam scalar (F^{±1} bounded near 0;
    |W̃| ≍ |z|^{α/2} since G is bounded near 0).
  - −1 < α ≤ −½: Prop 5.6(vii) applies (|α| < 1). |P̌₀^{±1}| ≤ C_n|z|^{−|α|/2} holds, and the seam jumps v_s are bounded with
    bounded inverses. So CD Thm 4.4 applies on Σ ∪ Σ_𝖱 as in §8.
- **I5 (flagged 3a, identification without X̃).** Correct and cleaner than RH_p1_general §6. 𝔉 := z(𝖷 − I) − 𝖷₁ is O(1/z),
  continuous up to Σ_𝖷 off the vertices, bounded near the other vertices. Since 1 + min(0, 2a) > 0, 𝔉 → 0 at 0; hence
  𝔉_± ∈ L² and Lemma cauchy-arcs(c) applies. 𝔣 = 𝖷₋(J_𝖷 − I) is bounded (δ ≥ 2). The ray arg z = π/8 stays at distance
  ≍ |z| from Σ_𝖷 (lips at |arg(±z)| ∈ [π/4 − η, π/4 + η]). The Ahlfors bound gives |𝒞𝔣| = O(log 1/|z|) there, so 𝔠 = 0.
- **I6 (flagged 3b, log² padding at a = 0).** Dropping it is correct. At a = 0 the orders are ±½, and
  ζ^{1/2}I_{±1/2}(ζe^{∓πi/2}), ζ^{1/2}K_{1/2} and ζ^{1/2}H^{(1,2)}_{±1/2} are elementary and bounded near 0. RH_p1_general's
  padding was only a precaution, and the numerics there are not used.
- **I7 (Thm 1.4 vs sources).** (i) p > 1 = E_pgt1 Thm E.1, p = 1 = E_p1 Thm E1.10 (both O(n⁻²)). (ii) = E_plt1 Thm E′.1, with
  κ_p renamed 𝗄_p (NOTES explains why). Exact order n^{−1−p} holds since 1 + p < min(2, 1 + 2p) and 𝗄_p < 0
  (reflection formula). 𝗄_{1/2} = ζ(−½)/√6 = −0.0848692. The extraction in §10.5 reproduces both terms, and they cancel in
  a_n/(2b_n) up to O(n⁻²) cross terms. Rem 1.7 and Cor 11.7 (−1/24, 5/96, 53/96; u_n, l_n, a_n ratios; 𝖾_N ratio 1 − 1/(6N²))
  = E_p1 Thm E1.6, re-derived.
- **I8.** Lemma 11.8's upper bound is UL Lemma V(U) specialised with Jensen. A one-clause attribution ("this is the
  minimum-property bound; the lower bound replaces the negative moment by the shift identity") would help a reader who
  knows Paper III, but it is optional.

## 4. §10 in detail (flagged item 2): summary

All five flagged departures are mathematically sound:
- (10.9) exact (I1);
- (10.5) on whole discs (I2);
- seam split (m5: correct, under-argued);
- Ψ_α near 0 (I3);
- Step 2 for p < 1 (I4).

Lemma 10.1(iii) (Mellin + DLMF 5.2.1, 25.2.1, 25.4.1) and Lemma 10.2 re-derive. The 𝖽 sign conventions are consistent
throughout: ω_𝖽 = ω^mod e^{𝖽𝓡}, ϱ_𝖽 = ϱ^mod e^{−𝖽𝓡}, L_r ↦ L_r − ½𝖽𝓡, 𝖽_n = 2ζ(−p)n^{−p} < 0, 𝗄_p = pc𝖽_n n^p. The
lips (3θ_lip/4 to 5θ_lip/4 = 5πp/16) lie inside S_in (θ_seam = πp/2). The seams map into the central Bessel sector since
f′(0) < 0 and θ_seam > θ_lip.

## 5. §11 / App. H in detail: other points checked

- Lemma 11.1, folding: R_N(−t) = (−1)^NR_N(t); u_m = 𝖾_{2m+1} from (11.1) at t = 0.
- Lemma 11.6: Carlitz masses (k+1)^{k−1}e^{−k}/k! at ±(k+1)^{−1/2} fold to 2e·v_j at 1/j. 𝖾_N = 1/(N+1) from (1.6), (1.9).
- (11.3): k^{−3/2} = √(2π)e^{j(k)}v_k, with f₀ = j − log(1 + 1/(12k)) = 1/(288k²) + O(k⁻³) uniformly.
- Prop 11.9(v)/App. H: U₁ = N^{1/2}N^{Nσ₃/2}Y₁N^{−Nσ₃/2}, so (U₁)₁₂(U₁)₂₁ = N𝖾_N; the exterior diagonal factors preserve
  the off-diagonal product; (𝒩_{s,1})₁₂(𝒩_{s,1})₂₁ = 1.
- φ₊(0) = −πi∫_0^∞ψ = −πi/2, and conjugation by i^{Nσ₃} gives (−1)^N on the off-diagonal.
- At ±2 there is no phase, since φ̃(2) = φ̂(−2) = 0.
- Stirling truncation: the bound sec^{2m+2}(½ ph t) with |ph t| ≤ 2π/3 is used only on |arg(±z)| ≤ π/3. ∂U(0, ε) carries no
  e^{j(N/z²)} factor (the FH model uses h₀ = e^L(4 − z²)𝖰_m), so the poles of Γ near iℝ never enter. This is the point of
  the truncation 𝖰_m, and it is handled correctly.
- Lemma H.5: δ = 4m + 2 − 2|a| ≥ 2 ⇔ m ≥ |a|/2, the m of Prop 11.9; the ρ ≤ 1 bound N^{−6m−3}ρ^δ re-derives.
- Lemma H.1: the masses ½k^{−s} = (√(2π)/(2e))·w_d·e^{j(1/y²)}(y²)^a at y = ±k^{−1/2}, from WLXZ (2.15) at parameter 1.
- Δ^{(3/2)} on ∂U(2, ε): expanding e^{jσ₃}𝒩(I + Z/N)e^{−jσ₃}𝒩^{−1} gives exactly the two stated terms. Δ^{(2)} is
  N-independent.

## 6. Numerics (flagged item 5)

- **Table 12.3** = check_e_plt1_num.out, lines "b/a: n^-1-p coef. after subtracting the proved 1/n term" (fitted and
  half-range) and "a/2b: n^-1-p" (last column). All 12 × 5 entries match to the digits shown. Examples:
  - (0.3, 3/2): −0.0633783 (4.9e−4), −0.0633873 (1.1e−3), +0.0004;
  - (0.9, 3): −0.0881520 (5.3e−4), −0.0880830 (1.4e−2), −0.0003.
  The text claims also match: "up to 0.3 at (0.3, 3)" (3.0e−1); 1/n coefficients within 6·10⁻⁷ for p ≥ ½ (max 5.4e−7 at
  (0.5, 3)) and within 6·10⁻⁴ at p = 0.3 (max 5.7e−4). The single OUTSIDE row of the .out (g at p = 0.9, s = 1.5;
  |diff| 5.9e−8) is not in the table.
- **Table 12.4**, upper part = check_e1_tc.out (b and α columns at n = 50, 200, 800, 1499, both tails identical). Lower part
  = check_e1_rate.out, n = 200 and 798 (rb, ra) and rc(2n), rc(2n−1) at n = 798 (N = 1596, 1595); every entry matches.
  Other claims also match:
  - "changes under doubling of K below 5·10⁻⁵" (max 4.9e−5);
  - "values at N = 100 differ by < 7%" (max 6.6% at s = 4.5);
  - class means agree in pairs to 1.6·10⁻⁴ (max 1.6e−4);
  - "reproduces the explicit coefficients to 3·10⁻¹⁰" (3.2e−10).
- **Table 12.2 rows p ≤ 1** = check_so_grid.out (d₁ and e₁ˢ columns with half-ranges).
- check_so_grid.out also gives k₁ at p = 1 for s = 1.5, 2, 3, 4: 0.000000026, −1.500000000, −4.500000000, −7.499999999. This
  is −3(s − 3/2) to 10⁻⁸, so it supports Conj 13.1.

## 7. Step-1 fixes (commit 3e6f87d) against REFEREE_MATH.md

- **M1:** applied verbatim (both cases). The preamble sentence and the Outline are adjusted, and the standing assumptions
  of §8 now say that (vii) is used only for −1 < α ≤ −½. Correct.
- **m1:** Lemma A.1(iii) extended; Lemma 8.1 now cites (iii); the proof points to the verification of (e). Correct.
- **m2:** O(n^{−p} + n^{−3}) in the remark after Lemma 8.1, and E_pgt1 Remark (1) marked as corrected. Correct.
- **m3:** f^{1/2} at δ. Correct.
- **m4:** 𝖠_z, τ′ renamed throughout App. F case (a). Correct.
- **m5:** KMVV (6.19)–(6.21) in §2.5(a), DLMF 10.32.4/10.32.9 in §2.7(c), and the §1 sentence amended. Correct. (A new
  instance of the same issue for KV (5.4), (5.5), (5.18), (5.20) is m4 above.)
- **m6:** the middle M-range is stated. Correct: in the second case 1 ≤ y ≤ C and n⁻¹ ≤ M^{−p/2}.
- **m8:** a_* in Lemma 9.3. Correct.
- **m7:** not done (Teschl not read). Acceptable.

## 8. Bottom line

§§10–11 and Apps. G–H are a faithful and in places improved transcription of the REVIEWED sources (E_plt1, E_p1,
RH_p1_general). Every departure the drafter flagged is mathematically correct:
- (10.9) is exact in 𝖽 (verified to all orders);
- (10.5) holds on the whole discs;
- the seam split is correct (with m5's expansion);
- the Ψ_α bounds on the moved rays are correct;
- Step 2 for p < 1 is correct;
- the App. H identification without X̃ is correct;
- dropping the log² padding at a = 0 is correct.

**Lemma 11.8 is correct and needs no tail bound.** It is a weaker (O(1), non-uniform) form of UL Thm UF / UF-lim and
contains SECOND Thm 3.2 (O(1) form) at s = t + p. With Thm 11.13 and Cor 11.7 it fixes d₁ = −(s−1)/2 at p = 1 without
circularity and without Paper III. Theorem 1.4, Remark 1.7, Corollary 11.7 and Tables 12.2–12.4 agree with the sources and
the check outputs.

The one substantive error is in §13: **Conjecture 13.2 is false for every 0 < p < 1 as stated (MA1)** and must be amended
before submission. Paper III's citation of it must be re-checked.

**Sign-off.** After m2, m5 and m6 (and the cosmetic m1, m3, m4, m7, m8 at the editor's discretion), I sign off §§10–11,
Apps. G–H, Thm 1.4 and Rem 1.7 as REVIEWED (labels as in the sources: PROVED-mod-cite; at p = 1 additionally subject to
the stated WLXZ reliance). §13 is signed off once MA1 is fixed.
