# Rule R review: JZC M3a, gaps G1–G2 (p > 1), reviewer A: JZC_M3a_H_G12.md

Reviewer: independent second reader (Rule R), reviewer **A**. Date: 2026-10-21.
- Target: research/G1/RH/spectral/JZC_M3a_H_G12.md (L1.1, L1.2, L1.3, P1.4, C1.5, L2.1, L2.2, L2.3, P2.4, §§3–5);
  checks/m3a_g12_outer.py/.out, checks/m3a_g12_apriori.py/.out.
- Context read: AGENTS.md, VERIFICATION_POLICY.md; spectral/JZC_M3a_H.md, JZC_M3a_Hd.md; papers/paper2/sec_5.tex (§§5.1–5.9,
  Lemmas interp, invariance, gfunction, jumpsV, (O1)–(O5)), sec_6.tex (eq:binet-bound, eq:binet-small, Lemma outer, eq:szego,
  Lemma szego, Lemma normalisation), app_outer.tex (Lemma binetcut and proof), app_c.tex (Lemmas B-cauchy, sumbound,
  lenssector, Prop apriori, Cor L2); RH/CITATIONS.md entries (DLMF), (DLMF-2), (DLMF-5.5/5.11, Plan 54).
- I edited no file except this report. My scripts are in the session scratchpad (`…/scratchpad/review/g12_spot.py`).

## Overall verdict: **ACCEPT WITH FIXES**

I found **no mathematical error** in L1.1–P2.4. I re-derived every identity and inequality. Every quotation of Paper 2 matches
the .tex. All fixes are MINOR or INFO. One of them (F3) concerns the memo's own §5 "correction" to H-d, which is wrong in its
diagnosis but harmless.

| Item | Verdict | Fixes |
|---|---|---|
| L1.1 shift identity | ACCEPT (re-derived; branch argument correct; numerically 4·10⁻³¹ incl. Re t < 0 at p = 1.1) | — |
| L1.2 bounds for j_δ | ACCEPT (constants ⅛ + ⅛ + 1/12 + ⅓ = ⅔ and 4C_φ + 2 re-derived) | F4 |
| L1.3 binetcut (i)–(iii) for δ | ACCEPT (𝔟_∞(δ) re-derived; numerically 9·10⁻²⁵ at y = −10⁴⁰) | I2 |
| P1.4 (O1_δ)–(O5) for F_δ, (O1)/(O5) at ∞ for F♮ | ACCEPT WITH FIXES | F1, F2 |
| C1.5 F♮ → C_δ uniformly; closed form of L_δ | ACCEPT (re-derived; independent quadrature agrees) | F2, F4 |
| L2.1 Hurwitz sum bound | ACCEPT (I₁ and I₂ re-derived; exponent α, δ only in constants) | — |
| L2.2 lens sectors | ACCEPT (residues, the 7/16 arc bound, verbatim steps checked) | — |
| L2.3 column factorisation | ACCEPT WITH FIXES (typo) | F5 |
| P2.4 a-priori bound, Cor L2 | ACCEPT WITH FIXES (radius bookkeeping, undefined symbol) | F5 |
| §5 corrections to H-d | ACCEPT WITH FIXES ((4) is not a branch ambiguity) | F3 |
| Rule C | ACCEPT WITH FIXES (the CITATIONS pointers are missing) | F4 |
| Scope / setting | INFO | F6 |

## Findings

**F1 (MINOR; P1.4(a), "ν_p = 1/p").** Paper 2 §5.9 defines ν_p := min(1/p, ½). This is ½, not 1/p, when 1 < p < 2. The
proof is unaffected, because Paper 2's own argument (proof of binetcut (iv), "(O3)") uses only ν_p ≤ 1/p and |z| ≤ 1.
*Fix:* replace "ν_p = 1/p" by "ν_p = min(1/p, ½) ≤ 1/p, so the bound C|z|^{1/p} on |z| ≤ 1 gives (O3)".

**F2 (MINOR; P1.4(c) and C1.5 at δ = 0).** The polynomial-bound paragraph of P1.4(c) uses "κ_δ± → 1/(1 − e^{±2πiδ}) ≠ 0, ∞ as
t → 0". That holds only for δ < 0. At δ = 0, κ ∼ 1/(±2πit) is a power of |z|, and the bound is Paper 2's. Similarly, the
limit computation along iY uses L1.2(c), which is stated for δ < 0. C1.5 does treat δ = 0 in its last sentence. I checked that
the closed form of L_δ is correct at δ = 0: −½Log t − ½ln 2π − iπ/2 from κD̃ via (eq:binet-small), then the Log z coefficient
1/(2p) − 𝔟_∞(0)/2π = ½, and iπ/2 cancels. But P1.4(c) says nothing about δ = 0.
*Fix:* in P1.4(c), after "so |κ_δ|^{±1} ≤ C_n", insert "(δ < 0; at δ = 0, κ_± = (±2πit)^{−1}(1 + O(t)) is a power of |z|, as
in Paper 2)". In the limit paragraph, insert "(δ < 0 by L1.2(c); δ = 0 by (eq:binet-small) and κ_+ ∼ 1/(2πit), see C1.5)".

**F3 (MINOR; §5 correction (4) to H-d, and H.md §4 "Corrections").** The memo says H-d §3(iv)'s "[(−z)^{−δ}D_{x^{2δ}}] =
(4c/Υ)^δe^{±iπδ}" is branch-ambiguous. **It is not.** With principal branches, the identity holds exactly in ℂ_±:
- In ℂ₊, z^{1/2} and (z − 4c)^{1/2} lie in the open first quadrant. So their sum does too, and Υ = (·)² has arg Υ ∈ (0, π),
  hence arg(4c/Υ) ∈ (−π, 0).
- Then arg z + arg(4c/Υ) ∈ (−π, π) equals the principal arg(4cz/Υ). So (4cz/Υ)^δ = z^δ(4c/Υ)^δ.
- Also (−z)^{−δ} = z^{−δ}e^{iπδ} in ℂ₊. ℂ₋ is the mirror image.
- Numerically, G/((4c/Υ)^δe^{±iπδ}) = 1 to 10⁻²² at 10 points, including points next to (−∞, 0) and next to (0, 4c), for
  δ ∈ {−0.3, −0.9}.

The memo's replacement |G| = |4c/Υ|^δ is also correct, and it is all that L2.3 and P2.4 use, so nothing downstream changes.
*Fix:* replace §5 (4) by "(4) §3 (iv)'s identity [·] = (4c/Υ)^δe^{±iπδ} holds in ℂ_± with principal branches (arg Υ ∈ (0, π)
in ℂ₊); only its modulus |G| = |4c/Υ|^δ is used (L2.3)". Change the matching clause of JZC_M3a_H.md §4 "Corrections" in the
same way.

**F4 (MINOR; Rule C.2 bookkeeping).** Every external input is quoted correctly from Paper 2, which I checked against the .tex.
That covers (eq:binet-bound), the LnΓ branch, and "1/Γ(t) = Γ(1−t)sin(πt)/π" from the proof of Lemma outer. But the memo does
not point to the RH/CITATIONS.md entries that hold the primary quotes, and its hypothesis checks are spread across the proofs.
*Fix:* add an "Also used in: JZC_M3a_H_G12" line to two CITATIONS entries:
- **(DLMF) §5.11:** "5.11.1 + §5.11(ii) with n = 1 (via Paper 2 eq:binet-bound) at u = t − δ: |ph u| ≤ |ph t| ≤ φ < π
  (L1.1) and |u| ≥ |t|/2 ≥ 1 for |t| ≥ 2 (L1.2(b))".
- **(DLMF-5.5/5.11, Plan 54):** "5.5.3 at z = −δ ∈ (0, 1), z ∉ ℤ (C1.5, form of L_δ only)".

In the memo's §0, cite those entries next to "binet-bound".

**F5 (MINOR/typo; L2.3(ii), P2.4).**
- (a) L2.3(ii): "|F♮D_W| = |F_δD_W^{(α)}|·|G|·const". The identity is exact, F♮D_W = F_δD_W^{(α)}G, so delete "·const"
  (twice).
- (b) P2.4(ii): "q₁ = x^{α+2δ}Ĥ" uses an undefined symbol. Replace with "q₁ = x^{α+2δ}H°_n (H°_n := H_n^δ/H_n^δ(0⁺); r_n ≡ 1)".
- (c) P2.4(i) uses |G|^{±1} ≤ 2 only on |z| < r_G. Say so: "for |z| < min(δ_s/2, r_G); the annulus up to δ_r is covered
  by (ii)". This is needed because |G| is not ≤ 2 on all of U(0, δ_r) in general: my quadrature gives |G| = 2.10 at
  z = −0.5 + 10⁻³i, δ = −0.9, c = 0.7.

**F6 (INFO; scope, for JZC_M3a_H.md §1).** G12 §0 correctly assumes 1 < s < 1 + 2p, i.e. α ∈ (−1, 1). Cor L2 needs this:
(1 + |α|)/4 < ½. JZC_M3a_H.md §1 "Setting" says only "s > 1". *Fix (in H.md):* "s ∈ (1, 1 + 2p) (Paper 2's standing assumption;
|α| < 1 is used in Cor L2)".

**I1 (INFO; Paper 2 wording gap, Rule A item 6: confirmed).** app_outer.tex line 115 reads "on (−∞,−½], where 𝔟′ is
bounded". With boundedness only, the window term is ≤ sup|𝔟′|·|x|, i.e. |log B| ≤ C|z|, which is not a polynomial bound on B.
Paper 2's own proof of (ii) gives |𝔟′(y)| ≤ C/|y| for |y| ≥ n^p (line 77), which suffices. P1.4(c)'s explicit window argument is
correct. I re-derived the separation off the window with the better constant 1/10 (the memo's 1/16 is also valid), and the end
points of 𝒲 lie at distances in [|x|/2, 5|x|/2] from z. Record for math-pursuits FIXES via a human, as the memo says.

**I2 (INFO; L1.3(ii) constants).** On (−∞, −½] the bound |𝔟_δ′| ≤ C/|y| is n-free: for |y| ≤ (n/2)^p,
C|y|^{1/p−1}/n ≤ (C/2)/|y|. P1.4(c) writes C_n, which is harmless.

## Re-derivations

- **L1.1.** I derived LnΓ(t−δ) = j(t−δ) + (t−δ−½)ln(t−δ) − (t−δ) + ½ln 2π, so j_δ − j(t−δ) = (t−δ−½)(ln(t−δ) − ln t) + δ.
  For −δ ≥ 0, arg(t + |δ|) lies between 0 and arg t, so the difference of principal logs is Log(1 − δ/t), with no 2π. Correct.
- **L1.2(b).** Expanding gives (t−δ−½)Log(1−w) + δ = δ(1+δ)/(2t) + (δ+½)(w²/2 + R) − tR, with
  |R| ≤ (|w|³/3)/(1 − |w|) ≤ ⅔|w|³. The four bounds are 1/(8|t|), 1/(4|t|²) ≤ 1/(8|t|), (1/3)|t|⁻³ ≤ 1/(12|t|), and
  (2/3)|t|⁻² ≤ 1/(3|t|), which sum to ⅔. The derivative is Log(1−w) + w − δ/(2t(t−δ)), and |Log(1−w) + w| ≤ |w|². Correct.
  - Numerically, sup|t j_δ| = 0.079 on |t| ∈ [2, 100], |arg t| ≤ π/p, p = 1.1, δ ∈ {−0.01, −0.5, −0.99}; C_J = 8.9.
- **L1.2(c), L1.3(ii) limit.** 1 − e^{2πiδ} = −2i sin(πδ)e^{iπδ} = 2|sin πδ|e^{i(π/2+πδ)} for δ < 0, and its real part is
  positive, so the principal Log is continuous along the cut. Im(−(δ+½)Log t₊) = (δ+½)π/p. So
  𝔟_∞ = 2[(δ+½)π/p − π/2 − πδ] = (π/p − π) + 2πδ(1/p − 1). Correct.
- **P1.4(c), C1.5.**
  - The Log z coefficient is (δ+½)/p − 𝔟_∞/2π = ½ + δ, and the Log(−z) coefficient is −½ − δ (including (−z)^{−δ}).
  - In ℂ₊ the imaginary parts (½+δ)π − (π/2 + πδ) cancel.
  - Reflection at z = −δ gives Γ(−δ)Γ(1+δ) = π/|sin πδ|. So −LnΓ(−δ) − ln(2|sin πδ|) = lnΓ(1+δ) − ln 2π, and L_δ is as stated.
  - The ∫_{−∞}^{−1} integral is Log((1+z)/2), principal, since the ratio (z − y)/(1 − y) stays in ℂ₊.
  - Uniformity in direction comes from ϰ_∞♮ being analytic at ∞ (removable singularity). That is correct and stronger than
    H-d's monodromy sketch.
- **L2.1.** I checked:
  - X_k ≥ |z| iff τ_k ≤ T = n|z|^{−1/p};
  - w(X_k)/X_k = τ_k^{p−s};
  - the monotone-sum bounds for spacing-1 nodes starting at a (both the increasing and the decreasing case);
  - Σ_{τ_k>T}τ_k^{−s} ≤ T^{−s} + T^{1−s}/(s−1);
  - T^{1+γ} = n^{1+γ}|z|^α (since α = −(1+γ)/p);
  - the three cases of ∫_a^T u^γ.

  δ enters only through a^γ, a^{1+γ}/|1+γ| and M_n. Correct.
- **L2.2.** I checked:
  - the residue U_{j1}W/(2iθ_δ′) = w(X_k)U_{j1}(X_k), since θ_δ′ = θ′;
  - that the points t ∈ δ − ℕ₀ lie off 𝒢 (and |t| is large on 𝒢 anyway);
  - on |t| ∈ δ + ℕ + ½ with |v| < ¼: |t| − u = v²/(|t| + u) ≤ 1/16, so dist(u − δ, ℤ) ≥ 7/16;
  - (eq:R-contour) re-derived from the residue theorem.

  Correct.
- **L2.3.**
  - Multiplicativity of D_q: x^{2δ} > 0, with the real log.
  - D_{x^{2δ}}(∞) = exp(δ·(1/π)∫ln x dx/√(x(4c−x))) = c^δ, which fixes the root (4cz/Υ)^δ.
  - Numerically: quadrature of (eq:szego) = (4cz/Υ)^δ to ≤ 9·10⁻¹⁴ at dps 30 (8 points, two values of δ), and
    |G| = |4c/Υ|^δ to all printed digits.
- **P2.4.**
  - Column factorisation: Q♮ = (const. diag)·U M₀ (F_δD_W^{(α)})^{σ₃} G^{σ₃}.
  - Near 4c: (F̃♮D_W)² = W ω♮ e^{±2πiδ}, using W/F̃♮² = W₀^{(α)}(−z)^{2δ} = W₀^{(β′)}e^{∓2πiδ} in ℂ_±.
  - Cor L2 with η = (1 − |α|)/4.

  Correct.

## Independent verification (commands and outputs)

`…/scratchpad/venv/bin/python -B …/scratchpad/review/g12_spot.py` (mpmath, dps 30, n = 4, c = 1; my own code, not the repo's):
- L1.1: worst |lhs − rhs| = 4.2·10⁻³¹ over p ∈ {1.1, 1.5, 3}, δ ∈ {−0.3, −0.5, −0.95}, and five z, including z = −3 ± 10⁻³i.
- 𝔟_δ(−10⁴⁰) − 𝔟_∞ = 8.8·10⁻²⁵ (δ = −0.3) and 8.5·10⁻²⁵ (δ = −0.7), p = 1.5.
- C1.5, p = 1.5. I_r and log B_δ come from independent quadratures.

  | δ | L_δ | F♮(i·10⁸) | F♮(i·10¹²) | e^{L_δ} |
  |---|---|---|---|---|
  | −0.3 | −1.40007192484 (= memo) | 0.2465875 | 0.24657925 | 0.24657923 |
  | −0.7 | 0.687189151924 | 1.988186 | 1.98811951 | 1.98811937 |

  The error decreases by a factor of about 470 between the two heights, against (10⁴)^{2/3} ≈ 464. This is the
  O(|z|^{−1/p}log) rate.
- L2.3: see Re-derivations.
- Repo outputs: m3a_g12_outer.out "ALL 58 CHECKS PASSED", m3a_g12_apriori.out "ALL 67 CHECKS PASSED". Both are newer than
  their .py files, and `sha256sum -c` against MANIFEST.sha256 gives OK for all four files. I did not re-run the repo scripts
  (slow); my spot checks are independent.

Novelty: not assessed (outside remit). No RH claim is made or needed.
