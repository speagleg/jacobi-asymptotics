# Rule R referee report: Paper II, new mathematical writing (§§8–9, App. E, App. F, Prop 6.6, the §1/§3 statements)

Reviewer: independent second reader (Rule R). Worktree <repo path> branch plan-70-paperII,
read at commit 0d3c467 (editor pass 1: the proof of Prop 8.6 and Lemmas 8.7–8.8 moved verbatim to App. F, `appF_tail.tex`;
I diffed the moved block against the previous §8 and it is verbatim apart from `U(·,·)` → `\mathbb D(·,·)` and
`thm:UR-true` → `prop:UR-true`). Report only; no paper file was edited.

Sources compared: research/G1/RH/px/RH_px.md (§§3–5), research/G1/RH/second_order/E_pgt1.md (+ REVIEW_Plan65_A/B),
research/G1/RH/second_order/TAIL.md (+ REVIEW_Plan69), research/G1/PROOF.md §3.16 (Theorem QLP, Lemmas BK, Z, A: the
proof of record of TAIL's Prop TB-P), papers/paper2 (prop:moments, thm:shift, rem:pure-lommel), research/G1/RH/CITATIONS.md
and research/G1/CITATIONS.md (DLMF-3).

## 0. Re-derivations and checks run (Rule N: exact symbolic, NUMERICAL where stated)

- `scratchpad/refR/ref_check2.py` (sympy, written from the paper's own definitions, not from check_e_sym.py):
  (conj-T) and (T-back) as identities; P₁, P₂ of (P1P2); Lemma 9.2(a) (σ₃𝖹_Bσ₃/16 from a₁, b₁) and 9.2(b) (𝖹_Ai from
  u₁, v₁); then, at three rational points (c, p, α) = (1, 3/2, 3/10), (2, 3, −5/7), (3/4, 5/4, 7/3), the full Laurent
  expansions of Δ_r^mod and Δ_0^mod built directly as P₀^∞ Z (P₀^∞)⁻¹ (no use of (conj-T)), with f, φ̃, ω^mod from
  Lemma 9.3: odd powers vanish; 𝔅_r, 𝔄_r (App. E), 𝔄₀, 𝔠₀ (App. E) agree exactly; both combinations (Ar-combinations)
  agree; and the first-order expansions of 𝖻(Q), 𝖺(Q) with Q₁ = P₁ + 𝒜/n, Q₂ = P₂ + 𝒜P₁/n + ℬ/n give exactly
  c² − c²p(1+α)/n and 2c − pc(α+2)/n. All differences are 0.
- `scratchpad/num_local.py` (mpmath, NUMERICAL, 30 digits): f′(0), f₂ (from μ*((0,x]) by quadrature of ψ*) and
  𝗀₃, 𝗀₅ (from π∫_x^{4c}(λ_p − ψ*)) at p = 3/2 and 3 agree with Lemma 9.3 (f′(0) to 10⁻¹⁰ relative; residual of the
  φ̃ expansion is O(v^{7/2}) with a stable coefficient).
- By hand: the extraction algebra of the proof of Thm 1.4 (𝖺 linearised: 2c + 𝒜₁₁ − 𝒜₂₂ + 2i𝒜₁₂ − (i/c)ℬ₁₂), the hand
  computations of 𝔄₀, 𝔅_r and the two residue combinations in the proof of Lemma 9.4, the (Y-airy) and hard-edge Y
  formulas, the meromorphy argument (J𝖹J⁻¹ = −𝖹, ρ²₊ρ²₋ = 1, f^{1/2}₊ = −f^{1/2}₋), the orientation/residue signs of
  Prop 9.5, the Lommel closed forms (β_{2n}² + β_{2n+1}² = 2/((4n+1)(4n+3)(4n+5))·(4n+3), etc.) and their 1/n terms,
  Lemma 8.2(i)–(ii) jump algebra (JM diag(−i, i) = M; ρ^{σ₃}[[1,0],[x,1]]ρ^{−σ₃} = [[1,0],[ρ⁻²x,1]]), the column/row size
  count behind (R-at-zero), and every integral of App. F case (a) (main term, Bessel-scale term, correction term) and
  case (b) (Bessel products, the three M-ranges).

**Item (5) of the brief (constants):** Thm 1.4 is exactly E_pgt1 Thm E.1: n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)),
n^pa_n = 2c(1 − (s−1+p)/(2n) + O(n⁻²)), a_n the diagonal coefficient at P_n in xP_n = P_{n+1} + a_nP_n + b_n²P_{n−1}
(Prop 5.6(viii) / RH_px F7 convention), standard pairing a_n/(2b_n) = 1 − p/(2n) + O(n⁻²); b_n = c(n + (s−1)/(2p))^{−p}(1 + O(n⁻²)).
Verified independently (above). Remark 9.6's (2, 2) check is consistent.

## 1. Verdict per section

| Item | Verdict | Findings |
|---|---|---|
| §8 intro, standing assumptions | ACCEPT | — |
| Lemma 8.1 (band factor) | ACCEPT WITH MINOR FIXES | m1, m2 |
| Lemma 8.2 (classical parametrix), Lemma 8.3 (mismatch) | ACCEPT | — |
| Prop 8.4 (first-order small norm) | ACCEPT WITH FIX | **M1** (Step 2), m5 |
| Rem 8.5 | ACCEPT | — (the p < 1 sentence is no stronger than E_pgt1 §9) |
| Prop 8.6 statement; App. F proof, Lemmas 8.7–8.8 | ACCEPT WITH MINOR FIXES | m4, m6, m7 |
| §9 (Lemmas 9.1–9.4, Prop 9.5, proof of Thm 1.4, Rem 9.6) | ACCEPT WITH MINOR FIXES | m3, m8, m2 (remark) |
| App. E (Lemma E.1) | ACCEPT | constants verified exactly |
| Prop 6.6 statement (eq:he-L2-diff) | ACCEPT | matches the proof and TAIL (P2-e); Plan 69 F7 done |
| Thm 1.2, Cor 1.3, Thm 1.4, Thm 3.1 | ACCEPT | no stronger than sources; hypotheses identical |

Review fixes carried: Plan 65 A1 (Lemma 8.1(iii) third bound, η-version of Cauchy's estimate: present), A2 (R(0): not
needed in Paper II, Cor E.6 not included), A3 (α-independence: §8 standing assumptions use Prop 5.6(i)–(vi), (viii), stated
for all s > 1), A4 (lips at ±π/3 = KMVV's rays: θ_lip = π/3 fixed by 𝗆 = 1), A6/F6 (DLMF sectors for all α > −1: §2.7(d)
"None of these expansions restricts |ν|"); B F1 (α²-cancellation wording: correct in the proof of Thm 1.4 and Rem 9.6),
F2 (remark after Lemma 9.4), F5 (renaming: 𝔞_∞ ↦ a "never indexed"). Plan 69: F3(a) (Ǎ = Ǎ^a + Ǎ^s split, maximum
principle on Ǎ^a: Lemma 8.2(i)), F3(b) (szego(vi)(a) is not needed for ρ_n; Lemma 8.1(iv) + szego(i) used instead), F7
(eq:he-L2-diff promoted). Hypotheses (item 1): Prop 8.6 (a) p > 0, 1 < s < 1 + 2p, 1 ≤ M ≤ γ_*n^{2/p}; (b) p > 1, all
s > 1: arcsine bound for 1 ≤ M ≤ γ_*n^{2/p} and the M^{−τ} bound for all M ≥ 1, τ < min(p/2, s − 1). This is no stronger
than TB-A and QLP(a), (c) (it drops QLP(b) and the endpoint τ = p/2 when s − 1 > p/2). Lemma 8.1 is stated for n ≥ n₀
(source: all n ≥ 1): weaker, fine.

## 2. Findings

### Major

**M1. Prop 8.4, Step 2 (identification) — boundary regularity of the local solution X̃ is used but not justified; the
final application of Lemma 6.x "cauchy-arcs"(c) is to a function that is not continuous up to Γ.**
Location: sec8_classical.tex, proof of Proposition~\ref{prop:classical}, paragraph beginning "Next, let
$\delta_2<\delta_{\mathrm s}/2$" (line ≈333) through "which is~(iii) because …" (line ≈356).

Answer to the flagged question (item 3 of the brief): the fact is true and standard, so this is not a gap in the
mathematics of the result, but as written the step is not proved, in two places.
1. X̃ − I = 𝒞_Γ(𝔥) with 𝔥 ∈ L²(Γ) only, so X̃_± exist only as L² non-tangential limits. "G := RX̃ has no jump on
   Γ∖{0}" and "det X̃ has no jump" then hold only a.e., and "no jump ⇒ analytic" (Morera) needs continuity of the
   boundary values (or an E²/Smirnov-class argument). Neither is given or cited. RH_px §5 (the reviewed source) is even
   terser ("X̃ … H₋ ∈ E²_loc, and L² uniqueness"), so the new text is not weaker than its source. But a referee will ask.
2. "Subtracting the local Cauchy integral near 0 and applying Lemma~\ref{lem:cauchy-arcs}(c) to the rest": the rest,
   R − I − 𝒞_Γ(𝔨) with 𝔨 ∈ L², is not continuous up to Γ ∩ 𝔻(0, δ₂). So the hypothesis "continuous up to Γ" of that
   lemma fails. This is easily repaired. Lemma (c) can be applied to R − I itself: the vertex condition at 0 comes from
   (R-at-zero), since ρ·ρ^{min(0,α)−η} → 0, and the decomposition is needed only to put R_± into L² near 0.

The simplest fix removes X̃ altogether. (R-at-zero) already gives L² boundary values when α > −1/2. In the remaining
range −1 < α ≤ −1/2 we have |α| < 1, so Prop 5.6(vii) and Conway–Deift Thm 4.4 (§2.6(b)) apply exactly as in §6.
Suggested replacement text, for the whole paragraph from "Next, let $\delta_2$…" to the end of Step 2:

> Next we prove~(iii). Away from $0$ the matrix $\mathsf R$ is continuous up to $\Sigma_{\mathsf R}$ off the vertices and
> bounded near them (Proposition~\ref{prop:apriori}(ii)--(iii), whose proof does not involve $\alpha$, and the boundedness
> of the parametrices there), $\mathsf R=I+O(1/z)$ at infinity, and for fixed $n$ the contour $\Sigma_{\mathsf R}$ is bounded
> with $|\Sigma_{\mathsf R}\cap\mathbb D(z,\rho)|\le C_n\rho$.
>
> \emph{Case $\alpha>-\frac12$.} Take $0<\eta<\min(\frac12,\alpha+\frac12)$ in~\eqref{eq:R-at-zero}. Then
> $\mathsf R_\pm-I\in L^2(\Sigma_{\mathsf R})$, and $\rho\sup_{|z|=\rho}|\mathsf R(z)-I|\le C_n\rho^{1+\min(0,\alpha)-\eta}\to0$ at the
> vertex $0$. Lemma~\ref{lem:cauchy-arcs}(c), applied to $\mathsf R-I$ on $\Sigma_{\mathsf R}$, gives
> $\mathsf R=I+\Cauchy(\mathsf R_+-\mathsf R_-)$, which is~(iii) because $\mathsf R_+-\mathsf R_-=\mathsf R_-(J_{\mathsf R}-I)$.
>
> \emph{Case $-1<\alpha\le-\frac12$.} Then $|\alpha|<1$, so $Q_\pm\in I+\dC(L^2(\Sigma))$ and
> $|Q(z)|\le C_{n,\eta}|z|^{-|\alpha|/2-\eta}$ near $0$ (Proposition~\ref{prop:frame}(vii)). Let $\mathsf P$ be the parametrix
> ($\check P_0$ in $U_0$, $\hat P_r$ in $U_r$, $P^\infty_0$ elsewhere), so that $\mathsf R=Q\mathsf P^{-1}$, and let
> $\Sigma':=\Sigma\cup\Sigma_{\mathsf R}$. By the proof of Lemma~\ref{lem:classical-param}(iii),
> $|\mathsf P^{\pm1}(z)|\le C_n|z|^{-|\alpha|/2}$ near $0$, which is square integrable because $|\alpha|<1$. Moreover
> $\mathsf P$ is continuous up to $\Sigma'$ off its vertices and bounded near the other vertices, and $\mathsf P=I+O(1/z)$.
> So Lemma~\ref{lem:cauchy-arcs}(c) gives $\mathsf P_\pm^{\pm1}\in I+\dC(L^2(\Sigma'))$. The jumps of $Q$ and $\mathsf P$ on
> $\Sigma'$ are bounded with bounded inverses. By \S\ref{sec:tool-cd}(b) with $A=Q$, $B=\mathsf P$ and $r=r'=2$,
> $\mathsf R=I+\Cauchy\bigl(Q_-(vv_{\mathsf P}^{-1}-I)\mathsf P_-^{-1}\bigr)=I+\Cauchy(\mathsf R_+-\mathsf R_-)$. Finally,
> $\mathsf R_+-\mathsf R_-=\mathsf R_-(J_{\mathsf R}-I)$ lies in $L^2(\Sigma_{\mathsf R})$, because $|\mathsf R_-|\le C_{n,\eta}|z|^{-|\alpha|-\eta}$
> and $|J_{\mathsf R}-I|\le C_Kn^{-K}|z|^K$ near $0$ (Lemma~\ref{lem:mismatch-classical}). Hence
> $\mathsf R_\pm-I=\Cauchy_\pm(\mathsf R_+-\mathsf R_-)\in L^2(\Sigma_{\mathsf R})$, which is~(iii).

With this fix:
- delete the sentence "It does not use Proposition~\ref{prop:frame}(vii) or Corollary~\ref{cor:L2}." (line ≈287), or
  replace it with "It uses Proposition~\ref{prop:frame}(vii) only for $-1<\alpha\le-\frac12$, where $|\alpha|<1$.";
- adjust the Step 2 sentence of the Outline ("this replaces the a priori bound of Appendix~\ref{app:apriori}, which needs
  $|\alpha|<1$, …") accordingly;
- the X̃ construction, the det X̃ argument and the Laurent-coefficient estimate can go; (R-at-zero) stays.

If the author prefers to keep the X̃ route, two changes are needed instead:
- after "$\tilde X_+=J_{\mathsf R}^{-1}\tilde X_-$ on $\Gamma$", add a justified sentence that X̃ (hence det X̃ and G) has
  continuous boundary values on Γ∖{0}. Since J_R extends analytically to a neighbourhood of each open arc of Γ, this
  follows from the standard regularity of L² solutions with analytic jumps. That needs a citation read under Rule C, or
  a short proof;
- replace "Subtracting the local Cauchy integral near $0$ and applying Lemma~(c) to the rest" with "Applying
  Lemma~\ref{lem:cauchy-arcs}(c) to $\mathsf R-I$ itself (the decomposition shows $\mathsf R_\pm\in L^2$ near $0$, and the vertex
  condition at $0$ follows from~\eqref{eq:R-at-zero})".

The route in the suggested text needs no new citation.

### Minor

**m1. Lemma A.1 (lem:binetcut): promote the two facts used by Lemma 8.1(ii) (flagged item).** Lemma 8.1(ii) uses two
facts that appear only inside the proof of Lemma A.1(iv), in the verification of Definition 4.10(e): "log B is bounded on
U(0,δ)∖(−δ,0] uniformly up to the cut" and "|log B(z)| ≤ C_n(1+log|z|) for |z| ≥ 2 off the cut". Both are proved
there, and they are correct (window argument with (ii)'s bound on 𝔟′). Recommendation: extend the statement. Add at the end
of Lemma A.1(iii), after (eq:B-bounds):
> Moreover, for each fixed $n$, $\log B$ is bounded on $\mathbb D(0,\delta)\setminus(-\delta,0]$, uniformly up to the cut from
> both sides, and $|\log B(z)|\le C_n(1+\log|z|)$ for $|z|\ge2$, $z\notin(-\infty,0]$.

In the proof, label the two sentences as the proof of this clause (they can stay where they are). In Lemma 8.1(ii),
replace "by the proof of Lemma~\ref{lem:binetcut}(iv) (the verification of Definition~\ref{def:outer-admissible}(e))" and
"again by the proof of Lemma~\ref{lem:binetcut}(iv)" with "by Lemma~\ref{lem:binetcut}(iii)".

**m2. Remark after Lemma 8.1 (sec8_classical.tex lines 67–68): wrong error term for p > 3.** j(t) = 1/(12t) − 1/(360t³) + …, so
−j(t(z)) = −z^{1/p}/(12n) + O(n⁻³). Then log B(z) = G(z) + j(t(z)) = (z^{1/p} − 1)/(12n) + O(n^{−p} + n^{−3}), not
+ O(n^{−p}): for p > 3 the n⁻³ term dominates. The remark is not used, and E_pgt1 Remark (1) has the same slip. Fix:
replace "$\log B(z)=(z^{1/p}-1)/(12n)+O(n^{-p})$" with "$\log B(z)=(z^{1/p}-1)/(12n)+O(n^{-p}+n^{-3})$".

**m3. §9, line ≈94: "Let $f^{1/2}$ be the principal root; it is analytic and non-zero on $\partial U_0$."** False at the
point δ = ∂U₀ ∩ (0, δ]. There f < 0, f maps ℂ_± into ℂ_∓, and f^{1/2}₊ = −f^{1/2}₋ (as the proof of Lemma 9.4 itself
uses). Fix: "it is analytic and non-zero on $\partial U_0\setminus\{\delta\}$, with the two boundary values
$f^{1/2}_\pm=\mp i|f|^{1/2}$ at $\delta$". Lemma 9.1's "with boundary values where they cross the contour" then covers
this point.

**m4. App. F, case (a): notation clashes.** "$B(s'):=A_0(s')^{-1}A_0(z)$" (appF_tail.tex line ≈79) clashes with the
Binet-cut scalar B of Lemma A.1, which §8 uses heavily, and with the Beta function B(a′, b′). "$t:=n\varrho^{1/2}$" clashes
with the index function t(z) = nz^{−1/p}. Suggested renaming: $\mathsf A_z(s'):=A_0(s')^{-1}A_0(z)$ and
$\tau':=n\varrho^{1/2}$ (or any unused letter), with the corresponding replacements in the displayed integrals and in
$N:=D_{s'}^{-1}\mathsf A_zD_z$.

**m5. §1 claim that every external result is stated in §§2.4–2.7.** The paragraph after Thm 1.4 says "The proofs use the
following external results, each stated with its hypotheses in §§2.4–2.7". Several are cited directly in the new
sections and are not in §2: KMVV (6.19)–(6.21) (behaviour of Ψ_α at 0; Lemma 8.2(iii), Prop 8.4 Step 2); DLMF (10.32.4),
(10.32.9) (App. F case (b)); and, for Rem 9.6, DLMF (10.2.2), (10.6.1), (10.16.1), (4.22.3). All are recorded as READ:
KMVV (6.19)–(6.21) in RH/CITATIONS "(KMVV, additional quotes for Plan 14)" and "(KMVV-orient, Paper 2)"; 10.32.4 and
10.32.9 in **research/G1/CITATIONS.md "(DLMF-3)"**, not in RH/CITATIONS.md; the Lommel formulas in "(DLMF-Lommel,
Paper 2)". Fix, either:
- add to §2.5(a): "As $\zeta\to0$, $\Psi_\alpha(\zeta)=O(|\zeta|^{\alpha/2},|\zeta|^{-\alpha/2})$ (columns) in $|\arg\zeta|<2\pi/3$ and
  $O(|\zeta|^{-\alpha/2})$ in $2\pi/3<|\arg\zeta|<\pi$ for $\alpha>0$; $O(\log|\zeta|)$ for $\alpha=0$; $O(|\zeta|^{\alpha/2})$ for
  $\alpha<0$ \cite[(6.19)--(6.21)]{KMVV}." Also add to §2.7(c): "(10.32.4) $I_\nu(z)=\frac1\pi\int_0^\pi e^{z\cos\theta}\cos(\nu\theta)\diff\theta
  -\frac{\sin(\nu\pi)}\pi\int_0^\infty e^{-z\cosh t-\nu t}\diff t$ and (10.32.9) $K_\nu(z)=\int_0^\infty e^{-z\cosh t}\cosh(\nu t)\diff t$, both for
  $|\mathrm{ph}\,z|<\frac12\pi$"; or
- soften the §1 sentence to "… stated with its hypotheses in §§2.4–2.7 or at the point of use".

For the citation records: add a "(Paper II reuse)" entry to RH/CITATIONS.md that points to G1/CITATIONS (DLMF-3) for
10.32.4 and 10.32.9. Hypothesis check: in App. F, |ph u| ≤ π/12 + π/48 < π/2. All other §§8–9 and App. E citations
match the records by equation number: KMVV (1.1), (6.16)–(6.18), (6.23)–(6.28), Thm 6.3, (6.42)–(6.53), (6.44)–(6.46),
Prop 6.5 (proof); DLMF 5.12.1, 9.7.2, 9.7.5–6, 10.17.1, .2, .5, .6, .8, .11, .12, 10.25.2, 10.40.1–4.

**m6. App. F, case (b), last paragraph: the all-M bound skips the range γ_*n^{2/p} < M < n^{2/p} in words.** The text
says "the first case gives~\eqref{eq:tail-arcsine} for $M\le Cn^{2/p}$; the second gives it for the remaining
$M\le\gamma_*n^{2/p}$ … and the second gives … for $M\ge n^{2/p}$". The final "all M" claim also needs
γ_*n^{2/p} < M < n^{2/p}. It holds, because in the second case y = n²M^{−p} ≥ 1 there, so the bound is Cn⁻¹ ≤ CM^{−p/2}.
But it is not said. Fix: replace "the second gives it for the remaining $M\le \gamma_*n^{2/p}$, where $y$ is bounded below and
above, so that $n^{-1}\le CM^{-p/2}$" with "the second gives $\sum_{k>Mn}m_n(k)\le Cn^{-1}\le CM^{-p/2}$ for the remaining
$M\le n^{2/p}$, where $1\le y\le C$".

**m7. Lemma 8.8 (row product) attribution.** TAIL records Lemma GS as KNOWN (Teschl, *Jacobi Operators*, (1.99)–(1.100),
(2.122), "not re-read"). The paper proves it, which is fine, but the sentence after the lemma attributes the idea without a
citation. After reading Teschl, consider "(this is the classical expression of the diagonal Green's function through the
two solutions of the recurrence, cf.\ \cite[(1.99)--(1.100)]{Teschl})". INFO; optional.

**m8. Lemma 9.3: letter for 1/p + ½.** The proof uses a′ := 1/p + ½, while Prop 2.3(iii) calls the same number a_*. Use
a_* in Lemma 9.3 (sec9_second.tex line ≈170) to avoid two names.

### Info (no change required)

- **I1 (flagged item: Prop 5.6(vii) under |α| < 1).** The statement is correct and conservative. Prop B.4 (a priori
  bound) holds for every α > −1, and only Cor B.5 (L² membership) needs |α| < 1. App. B's opening already says so.
  Nothing in §§8–9 needs the a priori bound for |α| ≥ 1. Under the M1 fix, (vii) is used exactly in its stated range
  (−1 < α ≤ −½). Recommendation: leave (vii) as stated. Relaxing its first half buys nothing.
- **I2 (flagged item: meromorphy "by no jump plus growth bound").** For Δ₀^mod and Δ_r^mod this is rigorous as written.
  These are explicit functions with continuous boundary values, the jump algebra is checked, and the growth bounds
  |z|⁻¹ and |z − 4c|⁻² hold. The odd-power cancellation was re-verified exactly (§0).
- **I3 (Rem 8.5, p < 1 sentence).** It says only that the available seam bound |log H°| ≤ C|z|(1 + log(1/|z|)) does not
  give o(1/n) flatness. That is true and weaker than E_pgt1 §9. Fine.
- **I4 (Lemma 8.1(iv) replaces RH_px's Hölder lemma for ρ_n near the negative axis, flagged in NOTES).** Checked. The
  szego-repr identity with 𝔠 = log H°(z) holds for every z ∉ [0, 4c], including z near (−2δ, 0) with boundary values. The
  segment argument stays in {|w| ≤ ½r_*}∖(−∞, 0) because ½r_* = 2c + 1 < 4c (c > ½ for p > 1). Near 4c, the condition
  4c − 4ε ≥ 1 needs ε ≤ (4c − 1)/4, which holds for small ε. Sound.
- **I5.** Thm 1.2, Cor 1.3 (the (q, r) zeta-Hankel parametrisation: moments ζ(qj + 2q + r), Hankel det ζ(q(i+j) + r),
  requires 2q + r > 1), Thm 3.1 and Prop 6.6 agree with papers/paper2 (thm:main(ii)/engine + shift, thm:pure,
  rem:pure-zeta, thm:shift, prop:moments and its proof) with identical hypotheses. Rem 1.6 / Rem 9.6 (Lommel) agree
  with paper2 rem:pure-lommel; the derivation now sits in Rem 9.6 and the cross-reference is consistent (working tree,
  uncommitted editor change).

## 3. Bottom line

The new mathematics of §§8–9 and Appendices E–F is a faithful transcription of the REVIEWED sources: RH_px §§3–5, E_pgt1
§§2–7.1, TAIL §§3.1–3.3 and G1 §3.16 for case (b). It carries all their review fixes, and every constant of Theorem 1.4
and App. E re-derives exactly. One step needs a real repair of the written proof: Prop 8.4 Step 2 (M1). Its conclusion is
true, and a citation-free replacement is given above. The minor items are wording, notation and citation bookkeeping.
After M1 and m1–m6, I would sign off §§8–9, App. E, App. F and the listed statements as REVIEWED (labels as in the
sources: PROVED-mod-cite).
