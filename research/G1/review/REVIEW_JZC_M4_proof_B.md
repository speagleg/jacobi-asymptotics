# Rule R review: JZC M4 proof, reviewer B: JZC_M4_proof.md, Theorem N.6 (natural-index double expansion, all p ≠ 1)

Reviewer: independent second reader (Rule R), reviewer **B**. Date: 2026-10-22.
- Target: research/G1/RH/spectral/JZC_M4_proof.md as revised after review A (branch plan-e2-d2): Lemmas N.6a, N.6b,
  Prop N.6c, Lemma N.6d, Theorem N.6 (i)–(iii), the visibility table, §§7–9.
- Scripts and outputs: checks/m4_rh_exact.py (→ m4_rh_exact_k4.out, _k6.out), m4_zeta_exact.py (→ m4_zeta_exact.out),
  m4_rh_exact2.py + m4_zeta_exact2.py (→ m4_zeta_exact2_A.out, _B.out; **new since review A**, not seen by it), and the
  numerical scripts the memo cites (m4_rh4.py, m4_f4_lattice.py, m4_zeta_lattice.py).
- Context read: AGENTS.md, VERIFICATION_POLICY.md; review/REVIEW_JZC_M4_proof_A.md; spectral/JZC_M4.md §§5–6 and its label
  table; spectral/JZC_M3a_H.md §1, §4; second_order/E3.md (whole), E2_pgt1.md (Lemmas E2.3, E2.6, Prop E2.5, Thm E2.1),
  E_pgt1.md §0, E_plt1.md (§0, Lemma F.1, Lemma E′.5, Prop E′.5′); papers/paper2/sec_6.tex (Frame Proposition F1–F8);
  RH/CITATIONS.md entries (KMVV-orient, Paper 2), (DLMF-10.40, Paper 2), (DLMF-9, Paper 2), (DLMF-10.17, Plan 55),
  (DLMF-9.7.2, Plan 65), (Plan 65 reuse), (Plan E2 reuse), (JZC M4 reuse); DLMF §10.17 page (fetched 2026-10-22, for the
  §10.17(ii) sentence only).
- I edited no file except this report. My scripts and outputs are in the session scratchpad
  (`/tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/revB/`: symcheck.py, bn_arb.py,
  bn_modcheb.py, ana_p2.py, ana_zeta.py, a_*.txt, checks/re/*.out, re_m4_*.out).
- No statement about RH (the zeta hypothesis) is made or used; ζ(−jp) enter only as the band-factor constants of E3.

## Overall verdict: **ACCEPT WITH FIXES**

I found **no mathematical error** and no MAJOR issue. I re-derived the key steps (list below), re-ran every exact check
(identical outputs up to timings, sha256 provenance lines matching the current scripts and MANIFEST.sha256) and the cited
numerical checks (byte-identical). Independently of the repo's code, I computed the Jacobi coefficients of the lattice measure
σ_{p,s} in Arb ball arithmetic. Against them, the proved layers of Theorem N.6 hold, including f₂, f₄, f₆ (p = 2), g₁, g₂, ε₂,
ε₃ and the ζ(−p)² coefficient **(3p+1)/(2p)**, recovered to 10⁻¹³ at p = 3/2 (two values of s) and to 10⁻¹⁰ at p = 4/5,
with controls failing by 10⁷–10¹⁴ times the fit error. The fixes are wording, scope and Rule C hygiene (M1–M5); there are
also five INFO items. Review A's fixes F1–F8 and I2 are applied correctly in the memo. Two of them were not propagated to
neighbouring files (M5, I2).

| Item | Verdict | Fixes |
|---|---|---|
| Lemma N.6a (jumps to every order; tie argument; band-factor conjugation) | ACCEPT WITH FIXES (math correct; quotation hygiene) | M3 |
| Lemma N.6b (meromorphy for every k; p > 1 limit argument, p < 1 parity argument) | ACCEPT WITH FIXES (the p > 1 paraphrase ignores the lip jumps; conclusion holds) | M1, I5 |
| Prop N.6c (order-K small norm, residue recursion) | ACCEPT | — |
| Lemma N.6d (exact algebra, incl. the new symbolic-j and μ₁² runs) | ACCEPT WITH FIXES (wording of the orders) | M2, I1, I2, I3 |
| Thm N.6 (i) double expansion | ACCEPT | I4 |
| Thm N.6 (ii) layer identities | ACCEPT WITH FIXES (the j ≤ 5, K = 5 sentence) | M2 |
| Thm N.6 (iii), visibility table, Consequences, §8 | ACCEPT WITH FIXES (coincident exponents; ε_j, j ≥ 4 omitted from Consequences) | M4 |
| Review A fixes F1–F8, I2 | applied correctly in the memo; F1 mirror in JZC_M4.md incomplete; F7 not carried into the new m4_rh_exact2.py | M5, I2 |
| Rule C (citation gate) | ACCEPT WITH FIXES | M3 |

With M1–M5 applied, I see no obstacle to marking Lemmas N.6a–c, Lemma N.6d and Theorem N.6 REVIEWED (labels unchanged:
PROVED-mod-cite / PROVED as in the memo's table). For JZC_M3a_H §4 this means that the last unreviewed link of Theorem H (i)
is then reviewed. The other links remain as that memo lists them; the band-factor constants for δ ≠ 0 stay the Fourier sums
(Remark 3.3 NUMERICAL), which this review does not touch.

## Findings

**M1 (MINOR; Lemma N.6b, p > 1 paragraph; the same wording is in E2 Lemma E2.6(a)).** The memo says "G_n :=
P̂^{mod}(P₀^∞)⁻¹ is analytic in U_e ∖ {e}". This is not literally true. By Paper 2 F5, the Airy parametrix "has exactly the
jumps v" in U(4c, ε), and the same holds for the Bessel parametrix in U(0, δ). These jumps include the lips (F1, F3), where
P₀^∞ has no jump. So G_n jumps across the lips inside U_e, with G_{n,+} = G_{n,−}·P₀^∞v(P₀^∞)⁻¹, and v − I is
exponentially small on compacts away from e (F4, F6 at 0; the sign of Re φ̃ at 4c). The conclusion is unaffected:
- the expansion of Lemma N.6a holds uniformly up to each lip from both sides;
- the two one-sided limits defining Δ_k differ by a quantity that is o(n^{−m}) for every m, so Δ_k is continuous across the
  lips and, by Morera, analytic in U_e ∖ {e}.

(The p < 1 parity argument is also p-free. It uses only P₀^∞₊ = P₀^∞₋J (F5, all p), φ̃₊ = −φ̃₋, f^{1/2}₊ = −f^{1/2}₋,
(−ω)^{1/2}₊(−ω)^{1/2}₋ = 1 and the ρ² relations of E′.5, so it could be cited for p > 1 as well.)

*Fix (§3, first paragraph):* replace "G_n := P̂^{mod}(P₀^∞)⁻¹ is analytic in U_e ∖ {e}, the expansion … holds uniformly on
compacts K ⊂ U_e ∖ {e}, and so Δ_k = lim … is analytic and single-valued in U_e ∖ {e}" by:

"G_n := P̂^{mod}(P₀^∞)⁻¹ is analytic in U_e ∖ ({e} ∪ lips). On the lips its jump is P₀^∞v(P₀^∞)⁻¹ = I + O(e^{−n/C_K}) on every
compact K ⊂ U_e ∖ {e} (Paper 2 F4–F6). The expansion of Lemma N.6a holds uniformly on such K from both sides of each lip, so
the one-sided limits Δ_k = lim n^k(G_n − I − Σ_{i<k}Δ_in^{−i}) agree across the lips. Hence Δ_k is continuous, and by Morera
analytic and single-valued, in U_e ∖ {e}."

The same sentence in E2 Lemma E2.6(a) ("P̂^{mod} and P₀^∞ have the same jumps in U_e ∖ {e}") needs the same textual fix.
E2 is REVIEWED, so this is for its owner (cf. F3); see I5.

**M2 (MINOR; header table row "Lemma N.6d", Thm N.6(ii) "For j ≤ 5 at K = 5 …", §1 bookkeeping wording).** The orders are
stated in two different conventions.
- The header row says "first-order μ_j layer for all j (symbolic j) to N⁻⁴ relative, and for j ≤ 5 to N⁻⁵ relative; the
  second-order μ₁ layer to N⁻⁵ relative". These are the *absolute* offsets k of the last computed coefficient N^{−k−|β|_wp},
  not relative orders.
- In relative terms, from 𝔇_{e_j,K} ∼ n⁻¹ and 𝔇_{2e₁,K} ∼ n⁻²:
  - K = 4 gives the first-order bracket through N⁻³ (error O(N⁻⁴));
  - K = 5 gives it through N⁻⁴ (error O(N⁻⁵));
  - the μ₁² bracket at K = 5 is known through N⁻³ (error O(N⁻⁴)), which is what Thm N.6(ii) correctly states.
- Thm N.6(ii) says "For j ≤ 5 at K = 5, the bracket error is O(N⁻⁵)". That is true only if the bracket includes its N⁻⁴
  coefficient. That coefficient is computed by m4_zeta_exact.py for j = 2, …, 5, but it is neither asserted nor displayed;
  only g₁,₄ is. As displayed, the j ≥ 2 brackets are [1 + g_jN⁻² + O(N⁻⁴)]. This is what the bookkeeping (correctly) uses.

*Fix:*
- Header row: "…the first-order μ_j layer for all j (symbolic j) through N^{−4−jp} (bracket error O(N⁻⁴)), and for j ≤ 5
  through N^{−5−jp} (bracket error O(N⁻⁵); the N⁻⁴ bracket coefficient is displayed only for j = 1, g₁,₄); the second-order μ₁
  layer through N^{−5−2p} (bracket error O(N⁻⁴))".
- Thm N.6(ii): replace "For j ≤ 5 at K = 5, the bracket error is O(N⁻⁵); for j = 1 the N⁻⁴ term is g₁,₄" by "For j = 1 at
  K = 5 the N⁻⁴ bracket term is g₁,₄ and the error is O(N⁻⁵)".
- §1 bookkeeping, first bullet: "the bracket is known to N⁻⁵ relative (K = 5)" → "the bracket is known through N⁻⁴ relative
  (K = 5; error O(N⁻⁵))".

**M3 (MINOR; Rule C.1; Lemma N.6a "Inputs").**
- (a) The line `§10.17(ii): "These results follow by differentiation of the corresponding expansions."` is presented as a quote,
  but:
  - it is truncated without an ellipsis (the DLMF text, fetched 2026-10-22, reads "These results follow by differentiation of
    the corresponding expansions in §10.17(i); compare §2.1(iii).");
  - it is not in RH/CITATIONS.md, although the Inputs paragraph says the quotations are "quoted in CITATIONS".

  It is not needed: 10.17.11–10.17.12 are themselves quoted verbatim in "(DLMF-10.17, Plan 55)".
- (b) The Inputs list quotes 10.17.5–6 but not 10.17.11–12, which the proof uses (tie argument, H⁽¹⁾′, H⁽²⁾′). The memo's
  header table does list ".11–.12".

*Fix:* delete the §10.17(ii) line, or quote it in full and add it to the "(DLMF-10.17, Plan 55)" entry with the fetch date. Add
the bullet "**10.17.11–10.17.12:** H^{(1)′}_ν, H^{(2)′}_ν with b_k(ν) in the sectors of 10.17.5–6 (quoted in "(DLMF-10.17,
Plan 55)")".

**M4 (MINOR; Thm N.6(iii) "Which coefficients … are determined", Consequences).**
- (a) The rule "A term cN^{−e} in (iii) is a coefficient of n^pb_n/c exactly when e < min(7, 2 + 3p)" ignores coincident
  exponents. When two displayed exponents coincide, the determined coefficient is their sum. §8 notes this only at
  p = 1/j₀. Further cases inside the visible range include:
  - p = 3: ε₁N⁻⁴ with f₄N⁻⁴, and ε₁ = 6cζ(−3) ≠ 0;
  - p = 3/2: ε₂N⁻⁴ with f₄N⁻⁴;
  - p = 5/2: ε₂N⁻⁶ with f₆N⁻⁶, and ζ(−5) ≠ 0;
  - in general, any equality among the displayed exponents {2, 4, 6, 1 + jp, 3 + jp, 5 + p, 2 + 2p}.
- (b) The "Consequences" list "f₂, f₄, f₆, ε₁, ε₂, ε₃, …" omits ε_j for j ≥ 4. These are determined for p < 1 by the table's own
  row ((j − 3)p < 1, 1 + jp < 7).

*Fix:*
- After the rule: "(when several displayed terms share the exponent e, the determined coefficient is their sum; e.g.
  f₄ + ε₂ at p = 3/2, f₄ + ε₁ at p = 3, f₆ + ε₂ at p = 5/2, f₂ + ε_{j₀} at p = 1/j₀, §8)".
- In Consequences, "ε₁, ε₂, ε₃" → "ε_j (j ≥ 1, in the range (j − 3)p < 1, 1 + jp < 7)".

**M5 (MINOR; review A F1 mirror; JZC_M4.md label table, row Prop N.3).** The statement column lists "f₁ = f₃ = f₅ = f₇ = 0",
and the label column says "PROVED-mod-cite … (Theorem N.6(ii): μ = 0 layer to N⁻⁶, exact)". f₇ = 0 is outside K = 6, and no
script computes f₇ exactly (m4_rh4.py is mpmath). It is NUMERICAL (m4_rh4.out ≤ 10⁻³⁵; also my p = 2 lattice data below,
residual·N⁷ → 0). *Fix:* in the label column, "f₁ = f₃ = f₅ = 0, f₂, f₄, f₆: PROVED-mod-cite (Thm N.6(ii)); f₇ = 0, f₈ and
beyond: NUMERICAL".

**I1 (INFO; §7 item 7, validity of the symbolic-j identity at every integer j).** The memo argues from "poles only at j = ½".
The relevant property is that specialising the field computation over ℚ(p, α, j) to an integer j₀ is legitimate. That needs
no intermediate division by a quantity vanishing at j₀. I read m4_rh_exact2.py with this in mind:
- G.inv inverts only the ε⁰ part, which is μ-free and j-free;
- powr1 divides by integers k and by the j-free leading coefficient;
- the only j-dependent denominators are 2(2j − 2i − 1) in the Taylor data at 0, nonzero for integers;
- the final ratio divides by pj/2 ≠ 0.

So the specialisation is valid for every j ≥ 1. *Suggested sentence:* "All divisions in the run are by j-free quantities
(ε⁰ parts, integers) except the Taylor-data factors 2(2j − 2i − 1) and the final pj/2, none of which vanishes at an integer
j ≥ 1."

**I2 (INFO; m4_rh_exact2.py docstring).** It reproduces the *pre*-F7 docstring of m4_rh_exact.py (assertions listed only up to
f₄; no c-normalisation line). The new header says that docstring "follows", so this is stale rather than wrong. *Fix:* copy the
current m4_rh_exact.py docstring, or point to it.

**I3 (INFO/typo; §7 item 2).** "the numerical version m4_rh4.py, at truncation depths 14–64". JZC_M4 §5 says 40 → 56 → 64, and
m4_rh4.py defaults to SHI = 40. The depths 14, 18, 22 are those of the *exact* scripts. *Fix:* "at truncation depths 40–64".

**I4 (INFO; Thm N.6, range of s).** N.6 is stated for s > 1, while Paper 2 F1–F8 are stated for 1 < s < 1 + 2p. The extension
is inherited from the E-series: E_pgt1 §7 ("α-independence of the Paper 2 inputs … RH_px §5, valid for all s > 1") and E_plt1 §0
("RH_plt1b (REVIEWED) covers every s > 1"). The memo does not say so. *Suggested sentence* in §1: "s > 1 as in E_pgt1/E_plt1
(Paper 2's s < 1 + 2p is not needed, E_pgt1 §7, E_plt1 §0)." JZC_M3a_H's s ∈ (1, 1 + 2p) is a subset, so nothing downstream
changes.

**I5 (INFO; owner fixes outside this memo).**
- E2 Lemma E2.6(a): the M1 wording.
- E2 Lemma E2.3: the F3 wording (already noted in §9).

Both are textual. The conclusions stand by the arguments now in JZC_M4_proof §§2–3.

## Re-derivations (from the write-up)

1. **Jump matrices and parity (N.6a, N.6b).** By hand, with M = [[1, i], [i, 1]]/√2, M⁻¹ = [[1, −i], [−i, 1]]/√2:
   - for C′ = [[u, −u], [v, −v]] (k odd), M⁻¹(M∘C′) = ½[[u+v, i(v−u)], [i(v−u), −(u+v)]] = ½(u+v)σ₃ + ½(v−u)iσ₁;
   - for k even, X_k = ½(u+v)I − ½(u−v)σ₂ (E2's X₂);
   - for C = [[−a, a], [−b, b]] (k odd), Ξ_k = −½(a+b)σ₃ + ½(a−b)iσ₁, so σ₃Ξ_kσ₃ = −½(a+b)σ₃ − ½(a−b)iσ₁. At k = 1 this
     reproduces E_pgt1's Ξ₁ = [[−(1+4α²), −2i], [−2i, 1+4α²]]/8.

   With J = iσ₂, J commutes with I and σ₂ and anticommutes with σ₃ and σ₁, so JX_kJ⁻¹ = (−1)^kX_k and likewise for σ₃Ξ_kσ₃.
   - On (4c − ε, 4c) the factors (−1)^k from (−1/φ̃)^k and from JX_kJ⁻¹ cancel. Jd^{σ₃}J⁻¹ = d^{−σ₃} together with
     (−ω₊)^{1/2} = (−ω₋)^{−1/2} moves the diagonal factors through.
   - On (0, δ) the same holds with (2f^{1/2})^{−k} and ρ²₊ρ²₋ = 1.
   - On (−δ, 0), Δ_k⁰ depends on ρ only through ρ², with (ρ²)₊ = (ρ²)₋ (E′.5). This is k-free.
   - The growth |Δ_k^r| ≤ C|z − 4c|^{−(3k+1)/2} gives pole order ≤ ⌊(3k+1)/2⌋.

   Tie argument: I checked that the derivative columns carry the same sign pattern as the value columns:
   - DLMF 10.17.11/12: H′ has the i^k, resp. (−i)^k, factor with b_k;
   - 10.40.3/4: I′ has (−1)^kb_k and K′ has b_k;
   - 9.7.6: Ai′ has (−1)^kv_k.

   So C_k and C_k′ are fixed by the k = 0 assignment of e^{±w}, e^{±ξ}, as the memo says. b_k = a_k + (k − ½)a_{k−1} follows from
   d/dz[z^{−1/2−k}e^{−z}] = −z^{−1/2−k}e^{−z}(1 + (k + ½)/z). At k = 1 it gives (4ν² + 3)/8, which is 10.17.8.
2. **Prop N.6c.**
   - Orientation: on clockwise circles the minus side is the inside, so R₋⁽ᵏ⁾ = R_in⁽ᵏ⁾ there.
   - For F meromorphic in the discs, (1/2πi)∮_cw F(s)ds/(s − z) equals the sum of the principal parts outside the discs and that
     sum minus F inside. The moment is −(1/2πi)∮_cw F = Res₀ + Res_{4c}.
   - The induction error: n^{−m} + n^{−1−(J+1)p}. The first term comes from the k + j ≥ m + 1 products and from the claim's
     error times J − I = O(1/n). The second comes from the jump error E, which contains Δ_k − Δ_k^{μ_n} = O(n^{−(J+1)p}) at
     order n^{−k}, worst at k = 1.
   - R⁽ᵏ⁾(μ_n) is uniformly bounded on Σ_R because its coefficients are entire in μ and μ_n → 0.
   - This is the review A F2 form, correctly applied.
3. **Thm N.6(i).**
   - The n⁰ term of Q₁₂Q₂₁ is (P₁)₁₂(P₁)₂₁ = c², and P₁ is μ-free, so √ expands with d_k(μ) polynomial in the R_1⁽ⁱ⁾(μ),
     i ≤ k.
   - E3 Lemma E3.7 gives the n⁻¹ coefficient d₁ + cpM_μ(4c), exactly affine in μ. So the Taylor remainder after order B ≥ 1 is
     O(|μ|^{B+1}n⁻²) on |μ| ≤ 1 (Cauchy estimates).
   - With |μ_n| = O(n^{−p}) this is O(n^{−2−(B+1)p}).
4. **Bookkeeping and visibility.** I rechecked every inequality of the F5 bookkeeping and every row of the table against
   e < min(7, 2 + 3p):
   - f₄: p > 2/3; f₆: p > 4/3;
   - ε_j: (j − 3)p < 1 and 1 + jp < 7;
   - ε₁g₁: ½ < p < 4; ε₂g₂: 1 < p < 2; ε₁g₁,₄: 3/2 < p < 2; ε₁²: p < 5/2;
   - ε_jg_j (j ≥ 3) and ε₁²h₂: never.

   All rows are correct, apart from M4(a).
5. **Symbolic-j data (Lemma N.6d A).**
   - At 0: C(2k−2, k−1)/C(2k, k) = k/(2(2k−1)) gives Π_{i≤m}(j−i)/(2(2j−2i−1)).
   - At 4: [w^m]Q_j = [t^{j−m−1}](1−4t)^{−m−3/2}. With C(2j, j) = 4^j(½)_j/j! and (½)_j = (½)_{m+1}(m+3/2)_{j−m−1} this gives
     j(j−1)⋯(j−m)/(4^{m+1}(½)_{m+1}).
   - Both agree with the memo and the script.
6. **Second-order gauge (Lemma N.6d B; code new since review A).**
   - m4_rh_exact2.py builds G = T[[ch, −(z−4)S], [−zS, ch]]T⁻¹ and G⁻¹ = T[[ch, (z−4)S], [zS, ch]]T⁻¹, with
     ch = Σ_{m≤EO/2}(z(z−4)M²/4)^m/(2m)! and S = (M/2)Σ(·)^m/(2m+1)!.
   - det = ch² − z(z−4)S² = 1 + O(ε⁴), so the inverse is exact over ε³ = 0. The construction matches E3 Lemma E3.4(ii).
   - Δ_k ↦ GΔ_kG⁻¹ is applied to every k.
   - The order-m response is extracted as the ε^m coefficient (the μ^m Taylor coefficient). Its natural form is
     (1 − δx)^{−(mj+1)p}Σ_ke_k^{(m)}(x/(1 − δx))^k, which I re-derived from n^{−mjp} = N^{−mjp}(N/n)^{mjp} and the common
     factor (n/N)^p.
   - Normalisation: μ_{n,1}² = 4ζ(−p)²n^{−2p} = ε₁²n^{−2p}/(pc)² (c = 1), so p(3p+1)/2 per unit μ₁² gives ε₁²(3p+1)/(2p),
     and h₂ = (N^{−4−2p} coefficient)/p².
   - The asserted N^{−1−2p} = 0 is E3.7's prediction and serves as a built-in test of the second-order gauge.
7. **Closed forms (scratchpad symcheck.py, sympy).**
   - From E2's d₁ = −p(α+1)/2 and d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12, the natural-form conversion gives
     f₁ = 0 and f₂ = −(p+2)α²/8 + (p+1)/12 identically.
   - JZC_M4 §5's printed f₄ equals the script's f₄ identically.
   - At the Bessel anchor (2, −½): f₄ = 3/128 and f₆ = 5/1024, the coefficients of (1 − y/4)^{−1/2}.
   - A₁ = (p+1)(p²+3p−2)/(24p) and B₁ = (p+2)(p²+2p+2)/(8p).
   - The partial-fraction form of B_j in JZC_M4 §6 is an identity.
   - g₁(3/2) = 95/288 (α = 0) and 22/9 (α = 1), as in JZC_M4 §6.

## Re-runs (Rule R)

Python: scratchpad venv, `-B`. The exact scripts ran on a copy of checks/ with the env vars of run_all.sh. The m4_rh4 and
lattice scripts ran in a scratch mirror with copies of the repo caches. Every stored provenance line equals the current sha256
of the script, which also equals MANIFEST.sha256.

| check | env | result |
|---|---|---|
| m4_rh_exact.py → k4 | KORD=4 SHI=14 | identical to m4_rh_exact_k4.out (timings excepted); ALL IDENTITIES HOLD, EXIT 0 |
| m4_rh_exact.py → k6 | KORD=6 SHI=22 | identical to m4_rh_exact_k6.out (timings excepted); d₁, d₂, f₁–f₆ True |
| m4_zeta_exact.py | KORD=5 SHI=18 JMAX=5 | identical to m4_zeta_exact.out (timings excepted): j = 1…5 all True incl. g₁,₄; ALL IDENTITIES HOLD, EXIT 0 |
| m4_zeta_exact2.py A | EO=1 KORD=4 SHI=14 | identical to m4_zeta_exact2_A.out (timings excepted): Taylor data j ≤ 8, lead pj/2, N^{−2−jp} = 0, A_j + B_jα², N^{−4−jp} = 0 |
| m4_zeta_exact2.py B | EO=2 KORD=5 SHI=18 | identical to m4_zeta_exact2_B.out (timings excepted): N^{−1−2p} = 0, N^{−2−2p} = p(3p+1)/2, N^{−3−2p} = 0, N^{−4−2p} = p²h₂, N^{−5−2p} = 0; ALL IDENTITIES HOLD, EXIT 0 |
| m4_rh4.py | default | byte-identical to m4_rh4.out (58 checks) |
| m4_f4_lattice.py | default | byte-identical (10 checks; reads the existing Plan 62 cache) |
| m4_zeta_lattice.py | default | byte-identical (8 checks; same cache) |

The machine was heavily loaded (two cores shared by up to four jobs), so wall-clock times were 3–10× the stored ones.

## Independent numerical spot check (NUMERICAL; Rule X: independent of the repo's code and caches)

**Method** (bn_arb.py, python-flint/Arb).
- The Jacobi coefficients b_n of σ_{p,s} = Σ_k k^{−s}δ_{k^{−p}} come from Gautschi's modified Chebyshev algorithm, with monic
  shifted-Legendre modified moments on [0, 1]:
  m_j = Σ_i(−1)^{j+i}C(j, i)C(j+i, i)ζ(s + pi)/C(2j, j), with ζ from Arb.
- The algorithm loses about 2p·n·log₁₀n digits. It is run at 2400–4200 digits, and only n with Arb radius/b_n < 10⁻⁴⁰ are used
  (n ≤ 380 at p = 3/2, n ≤ 340 at p = 4/5, all n ≤ 250 at p = 2).
- Validation: at p = s = 2, all b_n (n ≤ 200) equal the Lommel closed form π²/((4n+1)√((4n−1)(4n+3))) of CITATIONS (VA,
  Paper 2) to the 70 printed digits. An mpmath implementation (bn_modcheb.py) at 2400 and 2900 digits agrees to 10⁻⁵⁰.

**Test 1: integer layer at p = 2** (all ζ(−2k) = 0, so μ_n ≡ 0 and b_n is the pure μ = 0 layer).
- With F := (N/n)^p n^pb_n/c, the residuals (F − 1)N², (F − 1 − f₂N⁻²)N⁴ and (F − 1 − f₂N⁻² − f₄N⁻⁴)N⁶ converge to f₂, f₄, f₆.
  At n = 200 they agree to 6·10⁻⁷, 3·10⁻⁸ and 1·10⁻⁸ (O(1/N²) convergence).
- The next residual times N⁷ tends to 0, so f₇ = 0 is consistent. Times N⁸ it tends to f₈:
  - s = 2 (α = −½): 0.00106812, which is 35/32768, the Bessel-anchor value;
  - s = 7/2 (α = ¼): 0.0016118.

**Test 2: the zeta layers and the ζ(−p)² coefficient.**
- I subtract from F every term proved in Theorem N.6(ii) (to the orders proved) except the target ε₁²·K·N^{−2−2p}. The
  subtracted terms are f₂, f₄, f₆; ε_j(1 + g_jN⁻²) for all j with 1 + jp ≤ 12; g₁,₄; and ε₁²h₂N^{−4−2p}.
- I then fit T(n) := residual·N^{2+2p}/ε₁² = K + Σ_ia_iN^{−r_i}. The r_i run over the exponents (relative to 2 + 2p) of
  every *unproved* layer: μ₁μ₂ and μ₁³ at 2 + 3p, f₇ and f₈, the unproved bracket orders, 2 + 4p, and so on.
- Exact solves on m + 1 points in [n_top/2, n_top], two windows.
- Control: g₁ → g₁ + 0.01.

| p, s (α) | target (3p+1)/(2p) | fitted K (m = 8, two windows) | control g₁ + 0.01 |
|---|---|---|---|
| 3/2, 2 (−1/3) | 11/6 | 11/6 − 5·10⁻¹⁴, 11/6 − 1.7·10⁻¹³ | off by 14.5, 13.0 |
| 3/2, 7/2 (2/3) | 11/6 | 11/6 − 9·10⁻¹⁴, 11/6 − 3·10⁻¹³ | off by 14.5, 13.0 |
| 4/5, 2 (¼) | 17/8 | 17/8 − 1·10⁻¹⁰, 17/8 − 3·10⁻¹⁰ (m = 9) | off by 0.014 |

The fitted K is stable as m increases. At p = 3/2: m = 4 gives 3·10⁻⁹, m = 6 gives 3·10⁻¹¹, m = 8 gives 5·10⁻¹⁴.

**What the fit tests.** A subtracted term is tested only if its exponent is not among the free r_i.
- At p = 3/2 this covers f₄ and ε₂ (N⁻⁴), ε₁g₁ (N^{−4.5}), ε₃ (N^{−5.5}), f₆ and ε₂g₂ (N⁻⁶), and the target ε₁²(3p+1)/(2p)
  (N⁻⁵).
- At p = 4/5 (the p < 1 branch) it covers ε₁g₁, f₄, ε₄, ε₂g₂, ε₅ and ε₁²h₂ (relative exponents 0.2, 0.4, 0.6, 1.0, 1.4, 2.0),
  together with the target.
- g₁,₄ (p = 3/2) and h₂ (p = 3/2) coincide with free exponents and are not tested there.

These results are NUMERICAL and are not a proof. They confirm Theorem N.6(ii)–(iii) on the actual lattice, in both regimes p > 1
and p < 1, through a route that shares no code or cache with the memo's scripts.

## Rule C (citation gate)

- Every DLMF formula used in Lemma N.6a is in RH/CITATIONS.md verbatim and is quoted correctly in the memo:
  - 10.17.1, .5, .6, .8, .11, .12;
  - 10.40.1–4;
  - 9.7.1, 9.7.2, 9.7.5–6.

  The exception is the §10.17(ii) sentence (M3). The memo's paraphrase of 10.40.1 is faithful. 10.17.8 matches the TeX alttext
  in "(DLMF-10.17, Plan 55)". 9.7.2 matches "(DLMF-9.7.2, Plan 65)".
- The hypotheses line in "(JZC M4 reuse)" (review A F8) is present and correct:
  - ν = α > −1 fixed;
  - K + 1 terms;
  - the sectors |ph w| ≤ π/2 − δ (δ = θ_L/2 for p < 1), ph 2(−ζ)^{1/2} in the 10.17 sectors, and |ph Z| ≤ π − δ.

  I checked the p < 1 sectors: with rays at π − θ_L, |arg ζ| ≤ π − θ_L gives |ph w| ≤ π/2 − θ_L/2. In the thin sectors,
  ph 2(−ζ)^{1/2} ∈ (−θ_L/2, θ_L/2).
- The internal inputs carry the labels stated in the memo:
  - E-series: E2 E2.3/E2.5/E2.6, E3 F.1′/E3.4–E3.7, E_plt1 E′.3/E′.5/E′.5′/F.1, all REVIEWED;
  - Paper 2: F1, F4–F6, F8 (quoted above from sec_6.tex);
  - RH_px §5.
- No statement relies on an unquoted external source.

## Review A's fixes (verification)

- **F1:** done. The statement is split into (ii)/(iii), and the visibility table is present and correct apart from M4(a). The
  μ₁² layer is computed exactly, which improves the remainder to n^{−2−3p}. I re-ran it and tested it on the lattice. The
  JZC_M4.md mirror is incomplete (M5).
- **F2:** done (§4, running index m, n^{−1−(J+1)p} carried).
- **F3:** done (tie argument). I re-derived it, including the derivative columns.
- **F4:** done (§3 wording and mutation results).
- **F5:** done (§1 bookkeeping, every inequality rechecked; wording M2).
- **F6:** done. Provenance lines match the scripts and MANIFEST, and the outputs re-run identically.
- **F7:** done in m4_rh_exact.py and §5, but not carried into the m4_rh_exact2.py copy (I2).
- **F8:** done.
- **I2:** done (§6 no longer uses "bounded away from 0").

Novelty: not assessed (outside remit).
