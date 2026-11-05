# Rule R review: Theorem H (i) for p > 1, the H-a → H-e chain, reviewer A

Reviewer: independent second reader (Rule R), reviewer **A**. Date: 2026-10-21.
- Targets (all NOT REVIEWED before this report):
  1. research/G1/RH/spectral/JZC_M3a_H_Ha.md (H-a), checks/m3a_ha_interp.py/.out;
  2. research/G1/RH/spectral/JZC_M3a_Hd.md (H-d), checks/m3a_hd_outer.py/.out, checks/m3a_hd_model.py/.out;
  3. research/G1/RH/spectral/JZC_M3a_H_G1u.md (G1u), checks/m3a_g1u_hardedge.py/.out, checks/m3a_g1u_endtoend.py/.out;
  4. research/G1/RH/spectral/JZC_M3a_H_Hc.md (H-c), checks/m3a_hc_pgt1.py/.out, checks/m3a_hc_gauge.py/.out.
- Context read: AGENTS.md, VERIFICATION_POLICY.md; JZC_M3a_H.md (statement, §2 step table, §3.3, §4 status); JZC_M3a_H_G12.md and
  its review REVIEW_JZC_M3a_H_G12_A.md; JZC_M4_proof.md (N.6a–c, proof of Thm N.6); second_order/E_pgt1.md (Lemma E.2),
  second_order/E3.md (Lemmas E3.4, E3.5, E3.7); RH/CITATIONS.md entries "(Plan E3)" (DLMF 5.9.1), "(DLMF-zeta, Plan 67)";
  papers/paper2: sec_2.tex (T1(a) and its proof, T4), sec_5.tex (Lemma interp, Lemma invariance, §frame-contour, Step 1–4,
  (eq:VM), (O1)–(O5), Lemma jumpsV and its proof, Lemma weightdomain), sec_6.tex ((O2)–(O5) for the lattice, (eq:szego),
  (eq:szego-repr), (eq:DW-factor), (eq:omega), Lemma szego, F1–F6 incl. the F5 arc-by-arc bound), sec_7.tex ((eq:he-Phi),
  (eq:he-Phi-jumps), (eq:he-ephi), (eq:he-localisation), (eq:he-P0hat), Lemma comparison-parametrix and proof, (eq:he-vtilde),
  Lemma lip-mismatch and proof, Prop moments), app_b.tex ("The two instances", "No α is involved").
- I edited no file except this report. I did not open or run anything named m3a_g1up_*. My own scripts are in the session
  scratchpad (`…/scratchpad/review/spot.py`, `…/scratchpad/review/lin_check.py`); they are not repo code.
- Environment note: the repo `.venv` does not exist in this checkout and the system python has no mpmath/numpy. I ran every
  script with a throw-away venv in the session scratchpad (numpy 2.5.4, mpmath 1.3.0, sympy 1.14.0, python-flint 0.9.0) and
  `PYTHONPATH=src`. Nothing was installed into the repo.

## Overall verdicts

| Memo | Verdict | Findings |
|---|---|---|
| JZC_M3a_H_Ha.md (H-a) | **ACCEPT WITH FIXES** | Ha-1, Ha-2 (MINOR), Ha-3 (typo) |
| JZC_M3a_Hd.md (H-d) | **ACCEPT WITH FIXES** | Hd-1 (MINOR, a false sentence with no downstream effect), Hd-2 (MINOR, stale status) |
| JZC_M3a_H_G1u.md (G1u) | **ACCEPT WITH FIXES** | G1u-1 (MINOR, unwritten routine step), G1u-2 (MINOR, stale status), G1u-3 (INFO) |
| JZC_M3a_H_Hc.md (H-c) | **ACCEPT WITH FIXES** | Hc-1 (MINOR, Rule C bookkeeping), Hc-2 (INFO) |
| Chain H-a → H-b → H-b′ → H-c → H-d → H-e → (i), p > 1 | **no mathematical gap found; two unwritten links** | C-1 (MINOR) = G1u-1, C-2 (MINOR, needs a line plus an exact check) |

**No MAJOR finding.** I re-derived every lemma and proposition of the four memos (record below). Every Paper 2 quotation I
checked matches the .tex. All seven check scripts were re-run. Each output is byte-identical to the stored .out (§5).

The chain for p > 1 closes, with two additions:
- **C-1.** F5 (the far-arc bound) on the lengthened saturated lips and the moved top segment must be written for the Hurwitz
  contour. I did this below; it is routine, with constants that depend on a.
- **C-2.** E3 Lemma E3.7 (the 1/n coefficient is exactly linear in μ) is used in the proof of Theorem N.6(i) and is needed for the
  decoupled model M(β′, α). JZC_M3a_H.md §3.3 lists only N.6a–c, so this input is not stated anywhere. My numerical check
  confirms it to 10⁻⁴⁰.

None of this changes a statement. Under Rule R the labels can become "PROVED-mod-cite + REVIEWED (reviewer A)" once the fixes
are applied and a second reader re-runs the checks. Per JZC_M3a_H.md §4's own convention, that second reader is still pending.

---

## 1. JZC_M3a_H_Ha.md (H-a): ACCEPT WITH FIXES

### Re-derivations
- **Quotations.** I compared the memo with the .tex:
  - T1(a): sec_2.tex l. 200–216, including the hypothesis "x_k ∈ (0,1]" and the proof sentence "For |z|>2, expanding (z−x)^{−1}".
  - Lemma interp: sec_5.tex l. 79–113, including "X₁ = n^p (the top node)" and "for |z| > n^p".
  - Lemma invariance: l. 115–135. "We never use that Y is the unique solution": l. 137.
  - §frame-contour: l. 355–375.
  - app_c l. 116 ("e^{2iθ}=1 only where t∈ℤ … t∈−ℕ have |arg s| = πp > ϑ_lip").
  - T4 (5.5.3): sec_2 l. 332.

  All verbatim or exact paraphrases. Paper 2's own L5.1 claims the Laurent expansion for |z| > n^p (|ζ| > 1), which is
  slightly stronger than its proof's |ζ| > 2. It is true because x_k ≤ 1. The memo's version, |z| > X₁, is the correct
  generalisation.
- **L Ha.1.** I checked:
  - e^{2iθ_δ} = e^{2πi(t−δ)}. The positive points of δ + ℤ are δ + k, k ≥ 1, since δ ≤ 0 < a.
  - arg t = −arg z/p. For p > 1, |arg t| < π/p < π, so t never reaches (−∞, 0] and there are no non-nodes.
  - For p < 1, t ∈ (−∞, 0) iff arg z = ±πp, at |z| = (n/(m−δ))^p.
  - (iv) Γ-factorisation. D̃_δ = e^{−j_δ} = √(2π)t^{t−δ−½}e^{−t}/Γ(t−δ).

  All correct.
- **L Ha.2.** The only use of x_k ≤ 1 in T1(a)'s proof is the geometric series. Σ_kw_k|P_m(x_k)|x_k^i ≤ x₁^i‖P_m‖_{[0,x₁]}Σw_k
  gives convergence for |z| > x₁. The substitution z = n^pζ sends |ζ| = x₁ to |z| = X₁. The residues come from
  1/(ζ − x_k) = n^p/(z − X_k): Res U_{j2} = n^pw_kU_{j1}(X_k), for both rows (the n^{±pn} factors go into U_{j1}). Correct.
- **L Ha.3.**
  - (Y3) gives deg Y₁₁ = n monic, deg Y₂₁ ≤ n − 1, Y₁₂ = O(z^{−n−1}) and Y₂₂ = O(z^{−n}). Then Liouville applies to E_j.
  - Orthogonality identifies Y₁₁ = P_n and Y₂₁ = P_{n−1}/h_{n−1}.
  - The non-uniqueness example in Rule A 5 is O(z^{−n−1}).

  Correct. See Ha-2 for the logical status of (Y2).
- **L Ha.4.** W/(e^{2iθ_δ} − 1) = we^{−iθ_δ}θ′/sin θ_δ = we^{−iθ_δ}/Π_δ. The residue at X_k is W(X_k)/(2iθ′(X_k)) = w(X_k), since
  θ_δ′ = θ′. Also |e^{∓2iθ_δ}| = |e^{∓2iθ}| because δ is real. Correct.
- **P Ha.5.**
  - In the lens, R_{j2} = U_{j2} − U_{j1}𝒦^δ.
  - In the saturated region the first column is κ_δ±(U_{j1} ∓ U_{j2}/(κ_δ±W)). Here κ_δ± = ±1/(2iθ′(X_k)(z − X_k)) + O(1), so
    U_{j2}/(κ_δ±W) = ±r_{jk}/w(X_k) + O(z − X_k). The second column, U_{j2}/κ_δ±, is regular.
  - Both signs are checked: in ℂ₋, 1 − e^{2iθ_δ} = −2iθ′(z − X_k)(…).

  The "⇔" is correct and is exactly Paper 2's Step 1 (sec_5 l. 455–466) run in both directions with κ_δ.
- **Contour.** e^{pc₀} = e^pa^{−p} with c₀ = 1 + log(1/a). Re ξ = log|t| > −c₀ on 𝒵_n. The top node t = a lies inside. Correct.

### Findings
**Ha-1 (MINOR; §1, paragraph after the proof of L Ha.1).** The memo says: "The only new point is t = δ (m = 0). It lies on the same
rays, at |z| = (n/|δ|)^p > X₁". This holds only for δ > −½: (n/|δ|)^p > (n/a)^p ⇔ |δ| < 1 + δ ⇔ δ > −½. For example, at δ = −0.9
the point is at (n/0.9)^p < X₁ = (10n)^p. The conclusion is unaffected, because the point is on arg z = ±πp, outside every
sector the frame uses. It is in Ω_∞ and far from 0 (|z| ≥ n^p). *Fix:* replace "at |z| = (n/|δ|)^p > X₁, in Ω_∞, where κ_δ is
not used" by "at |z| = (n/|δ|)^p (which is > X₁ only for δ > −½; for δ ≤ −½ it lies between n^p and X₁), on the rays
arg z = ±πp, outside 𝒵_n, the lens and S_in; so it is in Ω_∞, where κ_δ is not used".

**Ha-2 (MINOR; L Ha.3 / P Ha.5 "Consequently").** (Y4) implies (Y2). If Y_{j2} − Σ_kw_kY_{j1}(x_k)/(z − x_k) is entire, the
residue at x_k is w_kY_{j1}(x_k). So in the class (Y1), (Y3), (Y4), the first bullet of the "Consequently" of P Ha.5 always
holds, and the stated equivalence is vacuous. It is not false. The substantive content is the local "for each k" equivalence,
which is correct. Nothing downstream uses uniqueness (the memo says so).
*Fix:* in §3 replace (Y4) by "(Y4′) Y_{j1} extends to an entire function, and there are numbers r_{jk} with Σ_k|r_{jk}| < ∞
such that Y_{j2}(z) − Σ_k r_{jk}/(z − x_k) extends to an entire function (j = 1, 2)". In L Ha.3's proof, insert after
"Uniqueness: let Y solve IP^δ_n." the sentence "By (Y2), r_{jk} = w_kY_{j1}(x_k)." In P Ha.5, replace "(Y1), (Y3), (Y4)" by
"(Y1), (Y3), (Y4′)".

**Ha-3 (typo; header table, row "L Ha.1").** "PROVED-mod-cite (DLMF 5.5.3 via Paper 2 T4)" is right. The proof's closing
parenthesis adds "NUMERICAL: argument-principle counts, §5", which is evidence, not part of the label. *Fix:* in the ∎ line of
L Ha.1, write "(PROVED-mod-cite: DLMF 5.5.3 as quoted in Paper 2 T4. Numerical evidence: argument-principle counts, §5.)"

C-1 below (the F5 bound on the Hurwitz contour) belongs naturally in Ha §4 "Contour bookkeeping". The fix text is given there.

Check: re-run, **ALL 298 CHECKS PASSED**, byte-identical to the stored .out (537 s wall on a loaded 2-core machine).

---

## 2. JZC_M3a_Hd.md (H-d): ACCEPT WITH FIXES

### Re-derivations (the jump algebra, line by line against Paper 2's proof of Lemma jumpsV)
Notation: F♮ = F_δ(−z)^{−δ}, F̃♮ = F♮/κ_δ. In ℂ_±, (−z)^{γ} = z^γe^{∓iπγ} (principal), so ((−z)^{−δ})₊((−z)^{−δ})₋ = x^{−2δ} and
((−z)^{−δ})₊/((−z)^{−δ})₋ = e^{2πiδ} on x > 0. Hence W/F̃♮² = W₀^{(α)}(−z)^{2δ} = W₀^{(β′)}e^{∓2πiδ} in ℂ_±.
- **(a) band.** L₋^{−1}L₊ has (1,2) entry −W(e^{−2iθ_δ}κ_δ+ + e^{2iθ_δ}κ_δ−) = W, for any phase. After A_±, the band matrix is
  (0, W; −1/W, 0). Conjugating by F̃♮₋^{−σ₃}(·)F̃♮₊^{σ₃} gives (0, W/(F̃♮₊F̃♮₋); −F̃♮₊F̃♮₋/W, 0). F̃_δ has no band jump (G12 P1.4(a)),
  so F̃♮₊F̃♮₋ = F̃_δ²x^{−2δ} and the entry is W₀^{(β′)}(x). Correct.
- **(d) saturated.** κ_δ+^{−1} + κ_δ−^{−1} = 2 − 2cos 2θ_δ = κ_δ+^{−1}κ_δ−^{−1} on ℝ. The diagonal is
  e^{n(φ₊−φ₋)}F♮₊/F♮₋ = e^{−2iθ}·e^{2iθ_δ}e^{2πiδ} = e^{−2iθ}e^{2iθ} = 1. The (2,1) entry is e^{2nφ̃}(−F̃♮₊F̃♮₋)/W, and
  −F̃_δ₊F̃_δ₋ = F̃_δ² by (O2)_δ. So it is e^{2nφ̃}/W₀^{(β′)}. Correct.
- **(c) Σ_v.** The (1,2) entry is −(W/F̃♮²)e^{−2nφ}e^{−2iθ_δ} = −W₀^{(β′)}e^{∓2πiδ}·e^{−2nφ̃}e^{±2πiδ} = −W₀^{(β′)}e^{−2nφ̃}. The phases
  cancel. Correct.
- **(b) lips.** (1,2): W₀^{(β′)}e^{−2nφ̃}, phases cancel. (2,1): κ_δ±e^{2nφ}F̃♮²/W = κ_δ±e^{2nφ}e^{±2πiδ}/W₀^{(β′)}, so the phase
  stays. Correct as stated in (ii) bullet 4.
- **(e) Σ^△, (f) top.** The (2,1) entry is ∓F♮²e^{2nφ}/(κ_δ±W) = ∓κ_δ±e^{2nφ}e^{±2πiδ}/W₀^{(β′)}. **The phase stays.** See Hd-1.
- **(g).** (−z)^{−δ} has its cut on [0, ∞), so F♮ has no jump on (−∞, 0). On (X₁ + δ′, ∞) the diagonal is 1 as in (d).
- **(iii).** ω♮ = ω^{(β′)}e^{±2πiδ} on the lips. Its band limits are e^{∓iπβ′}e^{±2πiδ} = e^{∓iπα} = ϱ_±. In U(4c, ε) the arcs
  are the band, the saturated segment and Σ_v (Paper 2 sec_5 l. 371–375), all of them phase-free, and Σ^△ starts at
  4c ± ih₀ with ε < h₀. So the Airy disc sees ω^{(β′)} without phase. Correct.
- **Prop 2.1.**
  - (2.1): B₂(−δ) = δ² + δ + ⅙.
  - (2.2): |D_δ| → Γ(1+δ)(2π)^{−1/2}|t|^{−δ−½}, by Γ(−δ)Γ(1+δ) = π/|sin πδ| and |1 − e^{2πiδ}| = 2|sin πδ|.
  - (2.4): the exponents sum to δ.

  All re-derived. As the memo says, the (2.4) limit is G12 C1.5, which review A of G12 accepted.

### Findings
**Hd-1 (MINOR; Lemma H-d (ii), third bullet).** The bullet reads "Σ_v (c), lip super-small entries, Σ^△, top: the entries carry
e^{−2nφ}e^{∓2iθ_δ} = e^{−2nφ̃}e^{±2πiδ}, and W/F̃♮² = W₀^{(β′)}e^{∓2πiδ} in ℂ_±; the phases cancel". This is true for Σ_v and
for the (1,2) super-small lip entry. It is **false** for Σ^△ (e), the top segment (f), and the (2,1) super-small lip entry. Those
entries carry κ_δ±e^{2nφ} with no e^{−2iθ_δ}, and they equal ∓κ_δ±e^{2nφ}e^{±2πiδ}/W₀^{(β′)} and (κ_δ± − 1)e^{2nφ}e^{±2πiδ}/W₀^{(β′)}.
In the Q-frame they read κ_δ±e^{2nφ}ω♮ and (κ_δ± − 1)e^{2nφ}ω♮, i.e. they come with ω♮, like the main lip entry.

This has no downstream effect:
- these arcs lie outside U(4c, ε), so (iii) is unaffected;
- every later use takes moduli (G1u §1 rows F4, F5: "phases of modulus 1");
- the phase is a unimodular constant.

Rule A item 1's conclusion is right in substance ("only θ-free entries keep it"). The listed arcs are wrong.
*Fix:* replace the third and fourth bullets of (ii) by:
"- Σ_v (c) and the (1,2) entries on the lips: these carry e^{−2nφ}e^{∓2iθ_δ} = e^{−2nφ̃}e^{±2πiδ}, and W/F̃♮² = W₀^{(β′)}e^{∓2πiδ} in ℂ_±, so
  the phases cancel and these are the lattice formulas with W₀^{(β′)};
- lips, (2,1) entries (main and super-small), Σ^△ (e) and the top segment (f): κ_δ±e^{2nφ}F̃♮²/W = κ_δ±e^{2nφ}e^{±2πiδ}/W₀^{(β′)}
  (no e^{2iθ} to absorb the phase). In the Q-frame these entries read with ω♮ := ω^{(β′)}e^{±2πiδ}. Σ^△ and the top lie outside U(4c, ε),
  and only |e^{±2πiδ}| = 1 enters their bounds (F5)."
In §6 item 1, replace "Only the lips (θ-free entries) keep it, and the lips avoid U(4c, h₀)" by "The (2,1) entries on the lips,
Σ^△ and the top segment keep it; none of these arcs meets U(4c, ε)".

**Hd-2 (MINOR; stale status, no mathematical content).** Several statements predate G12, H-a and H-c:
- header table, row Prop 2.1, "PROOF SKETCH" → "PROOF SKETCH, superseded by G12 C1.5 (PROVED-mod-cite; review A: ACCEPT WITH FIXES)";
- §0 and (iii): "Lemma H moments ζ(−kp, a)" and "μ_{n,k} = 2ζ(−kp, a)/(kn^{kp}) (Lemma H, CONDITIONAL on Hurwitz's formula)" →
  "μ^δ_{n,k} = 2m_k(δ), the Fourier sums of JZC_M3a_H.md §3.2 (JZC_M3a_H_Hc.md Lemma Hc.2); = 2ζ(−kp, a)/(kn^{kp}) by Remark 3.3
  (NUMERICAL)";
- §5, "the run m4_shift_exact.out in the tree currently reports orders ≤ 3 only": the stored m4_shift_exact.out reports orders
  1–4 and "ALL IDENTITIES HOLD". Delete the clause;
- §6 item 4, "Not tested numerically below β′ = −1" → "tested at β′ = −4/3 (spec_shift_hi, δ = −½) and, in m3a_g1u_endtoend, at
  β′ = −1.5, −2.1" (as G1u §8 already says);
- §7: append "Status 2026-10-21: G1 = G12 §1; G2 = G12 §2; G4 resolved by the Fourier-sum route (JZC_M3a_H §3.1–3.2); G5 =
  JZC_M3a_H §3.3; G3 = JZC_M3a_H_G3.md (p < 1)."

Checks: m3a_hd_outer, re-run, **ALL 34 CHECKS PASSED** (byte-identical, 276 s). m3a_hd_model re-run, **ALL 42 CHECKS PASSED** (byte-identical, 766 s). Both .py/.out pairs match
MANIFEST.sha256.

---

## 3. JZC_M3a_H_G1u.md (G1u): ACCEPT WITH FIXES

### Re-derivations
- **L1.**
  - (i): principal powers of the same base multiply exactly, and D_q is multiplicative.
  - (ii): in ℂ_±, (−z)^{β′} = e^{∓iπβ′}z^{β′}, so ρ♮² = e^{∓iπβ′}/ω^{(β′)} and ϱ_±ρ♮^{−2} = e^{±iπ(β′−α)}ω^{(β′)} = ω♮.
  - (iii): ((−z)^{β′/2})₊((−z)^{β′/2})₋ = x^{β′}.
  - (v): in ℂ_±, z^{1/2} = ±i(−z)^{1/2} and (z − 4c)^{1/2} = ±i(4c − z)^{1/2}, so Υ = −Υ̂. Then 4cz/Υ = (−z)(4c/Υ̂) and
    ρ♮ = (Υ̂/4c)^{(1+β′)/2}. The bound uses |√(1−w) − 1| ≤ |w|.
  - (iv): Paper 2 L szego (ii) applies with q = H°, by (O3) for H_n^δ (G12 P1.4(a)).

  All correct.

  *Independent check* (my quadrature of (eq:szego), not the repo's): e^{∓iπb}/ω^{(b)} = (Υ̂/4c)^{1+b} to ≤ 1.5·10⁻¹⁸ at 9 points
  (|z| ∈ [0.003, 0.02], both half-planes, b ∈ {−2.1, −1.3, 0.4}). |ρ♮| ∈ [0.97, 1.04] there.
- **L2.**
  - (i): Â♮₊ = Â♮₋ on the band. This uses Jρ^{−σ₃} = ρ^{σ₃}J, ρ₊^{σ₃} = ρ₋^{−σ₃} and JM = M diag(i, −i) (Paper 2 sec_7 l. 251–255).
    The singularity at 0 is removable by the |z|^{−1/2} growth.
  - (ii): the lip jump is ϱ_±ρ♮^{−2}e^{2nφ} = ω♮e^{2nφ}. The orientation is that of (eq:he-Phi-jumps): the upper lip maps to
    arg ζ = −(π − ϑ_lip), with jump e^{−iπα} = ϱ₊.
  - (iii): the factors cancel as in Paper 2 Lemma comparison-parametrix (iii), leaving P₀^∞ρ♮^{σ₃}[I + …]ρ♮^{−σ₃}(P₀^∞)^{−1}.

  Correct.
- **L3.** ω♮ − ϱ_± = ϱ_±(ρ♮^{−2} − 1), and ρ♮^{−2} = (Υ̂/4c)^{−(1+β′)}D_{h°}²/h°. Correct. Paper 2's lip-mismatch proof (sec_7
  l. 333–343) is indeed valid for any real exponent.
- **L4.**
  - The exponent is |α|/2 + η + |α|/2 < 1.
  - R has no band jump (both factors jump by J; the band jump of Q is J because D_{W+}D_{W−} = W₀^{(β′)}).
  - The super-small lip jumps are subtracted by a local Cauchy integral, and the singularity is then removable.

  Correct.
- **Prop G1u.**
  - (A): Prop moments (sec_7 l. 419–427) is quoted correctly, with ε′_n/n = n^{−1−2ν_p}log n.
  - (B): sup_r r^{−m}e^{−nr^{−1/p}/(2C)} ≤ C_mn^{−mp}. The N.6c induction uses only the listed bounds and the meromorphy of the
    model data.
  - N.6b's limit argument (JZC_M4_proof §3) gives single-valuedness of Δ_k^{mod,β′} in U_0∖{0}, because the model expansion
    holds on compacts and the lip jumps are e^{2nφ}-small there. Polynomial growth comes from |ρ♮^{mod}|^{±1} ≤ C, so 0 is a
    pole. β′ enters only through the bounded ρ♮.

  Correct.

### Findings
**G1u-1 (MINOR; §1 table, row F5, "top vertex X₁ + δ′ (H-a) | survives (H-a: input)"; = chain item C-1).** H-a (Ha §4) moves the
contour, but nobody verifies Paper 2's F5 bound on the **lengthened** saturated lips Σ^{△±} (now up to X₁ + δ′), on the lengthened
saturated segment, and on the moved top segment with κ_δ. I checked Paper 2's F5 proof (sec_6 l. 585–598) line by line for the
Hurwitz contour:
- Re φ ≤ γ_p − U*(x) ≤ −½log x for x ≥ x₀ is a statement about the lattice g and is unchanged.
- |Im θ(x ± ih₀)| ≥ h₀nx^{−1−1/p}/C gives |κ_δ±| ≤ Ca^{−p−1}n^p for x ≤ X₁ + δ′ (|κ_δ| depends on |e^{∓2iθ_δ}| = |e^{∓2iθ}|).
- On the top segment t − δ is close to 1, so |1 − e^{∓2iθ_δ}| ≥ a^{p+1}n^{−p}/C (|t − a| ≍ (a/p)δ′/X₁).
- log x ≤ C log n still holds, so |ω♮| = |ω^{(β′)}| ≤ exp(C log²n) by (O4) for H_n^δ (G12 P1.4(a)).
- The Cauchy-operator bound F1 is unchanged (translation invariance).

So F5 holds for Q♮ with constants depending also on a, and the bound on the top segment is even smaller (|e^{2nφ}| ≤ X₁^{−n/2}).
*Fix (in Ha §4, after "This agrees with JZC_M3a_H_G12.md §0 and with the corrected JZC_M3a_Hd.md §1."):* "F5 on the moved arcs.
Paper 2's F5 argument (sec_6, 'Σ^{△±} and the top segment') holds verbatim for x ≤ X₁ + δ′: Re φ ≤ −½log x for x ≥ x₀ (lattice g);
|Im θ(x ± ih₀)| ≥ h₀nx^{−1−1/p}/C gives |κ_δ±| ≤ Ca^{−p−1}n^p (|e^{∓2iθ_δ}| = |e^{∓2iθ}|); on the top segment
|1 − e^{∓2iθ_δ}| ≥ a^{p+1}n^{−p}/C; log x ≤ C log n; the phase e^{±2πiδ} of these entries (H-d (ii)) has modulus 1. Hence |v − I| ≤ C_ae^{−n/C}
there, and ≤ C_an^{−pn/4} on the top segment." In the G1u §1 table, row F5, replace "survives (H-a: input)" by "survives (Ha §4,
'F5 on the moved arcs')".

**G1u-2 (MINOR; stale status).**
- Header table, row Prop G1u: "(B) PROVED-mod-cite, CONDITIONAL on H-a and H-c (§4)" → "(B) PROVED-mod-cite (H-a: JZC_M3a_H_Ha.md;
  H-c: JZC_M3a_H_Hc.md Cor Hc.4); NOT REVIEWED".
- §4: "H-a (routine, not written: OPEN item 4)" → "H-a (JZC_M3a_H_Ha.md)". The Label line: "(A) PROVED-mod-cite, CONDITIONAL on
  H-a; (B) … CONDITIONAL on H-a and H-c" → "(A), (B) PROVED-mod-cite (inputs H-a, H-c as above); NOT REVIEWED".
- §7: delete the bullets "H-a written out" and "H-c: …" (done).
- Prop G1u's text "Assume H-a (…, JZC_M3a_H §4 item 4)" → "With H-a (JZC_M3a_H_Ha.md)".
- In (B), add E3 Lemma E3.7 for M(β′, α) to the inputs of "Prop N.6c for M(β′, ν = α)" (see C-2).

**G1u-3 (INFO; check [5]).** At (p, α, δ) = (1.5, 0.3, −0.3), β′ = −α, and the control "Δ₁ with ν = β′" is the true Δ₁, since
a_k, b_k depend on ν². The script correctly skips the assertion when |β′| = |α| (m3a_g1u_hardedge.py l. 181). The printed control
line for that case shows identical ratios. This is consistent with Rule A item 2 ("ν ≡ ±α"). No change needed. Optionally add
"(not asserted at β′ = −α, where ν = β′ gives the same Bessel data)" to §5.

Checks: m3a_g1u_hardedge re-run, **ALL 110 CHECKS PASSED** (byte-identical, 62 s). m3a_g1u_endtoend re-run, **ALL 29 CHECKS
PASSED** (byte-identical, 21 s).
- endtoend reads Jacobi coefficients from tmp/plan62_cache and does not regenerate them. All 7 needed cache files are present.
  Their provenance is so_coeffs (K atoms + Gauss–Jacobi tail, binary128 RKPW). I did not regenerate them (≈15 min each by the
  memo). The re-run therefore confirms the fits and predictions, not the coefficient generation.
- The quoted §5/§5a numbers match the .out. For example: |ρ♮| ∈ [0.68302, 1]; n|J − I| 1.127 → 1.1237; ratios 0.2385–0.2487;
  lip match 6.16·10⁻⁴¹; d₃ +2.1507287 vs +2.1507292.

---

## 4. JZC_M3a_H_Hc.md (H-c): ACCEPT WITH FIXES

### Re-derivations
- **Hc.1 (a).**
  - Jump: G_δ₊ − G_δ₋ = −2i Im j_δ(t₊) − i𝔟_δ = 2i Im Log(1 − q_δ). This uses Paper 2's sign (log B)₊ − (log B)₋ = −i𝔟, which
    is consistent with (1/2π)∫𝔢/(y − z) having jump +i𝔢.
  - Majorants: |arg(1 − w)| ≤ arcsin|w| ≤ (π/2)|w|; |q′| = 2π|q||t₊|/(p|y|); |t||q|/(1 − |q|) ≤ 1/(2π sin(π/p)). So
    |𝔢_δ′| ≤ 2/(p sin(π/p)|y|), δ-free.
  - The E_pgt1 Lemma E.2 quotations in the §1.1 table match second_order/E_pgt1.md.
- **Hc.1 (b), (c).** I checked the Liouville argument (with the added window step) and that the far/near split depends only on
  the majorants. Correct. E_pgt1's Remark (3) indeed fails for δ ∉ {0, −½} at p = 2: q_δ = e^{2πiδ}e^{−2πn|y|^{−1/2}} is not
  real, and S_k(−½) = 0 at p = 2.
- **Hc.2 (i).** q_δ = e^{2πiδ}exp(−aₙr^{−1/p}) with aₙ = 2πine^{−iπ/p} and Re aₙ = 2πn sin(π/p) > 0. With w = r^{−1/p},
  ∫q^m r^{−k−1}dr = pΓ(kp)(maₙ)^{−kp}, and (aₙ)^{−kp} = (2πn)^{−kp}(−1)^ke^{−iπkp/2}. The y = −r sign (−1)^{k+1} gives
  m_k = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ). At δ = 0, DLMF 25.4.1 gives ζ(−kp)/(kn^{kp}). The DLMF 5.9.1 hypotheses (Re ν = kp > 0,
  μ = 1, Re z > 0, principal power) are those of the CITATIONS entry "(Plan E3)". Correct.

  *Independent check* (my quadrature of 𝔢_δ against my partial Fourier sum, m ≤ 2·10⁴): agreement to 10⁻¹⁰–10⁻³¹ relative (the
  10⁻¹⁰ is the truncation of my Fourier sum at k = 1) for (p, δ) ∈ {(1.5, −0.3), (3, −0.7), (1.25, −0.95)}, k = 1, 2, n = 4. The
  identification ζ(−kp, 1+δ)/(kn^{kp}) (Remark 3.3, NUMERICAL) also agrees at all printed digits.
- **Hc.2 (ii).** E3 F.1′(ii) applies verbatim with the δ-free majorants. Correct.
- **Hc.3.**
  - Step 1: ρ♮ = ρ♮^{mod}h°^{1/2}/D_{h°} = ρ♮^{mod}e^{−L/2} and (−ω)^{1/2} = (−ω^{mod})^{1/2}e^{L/2}, with the same L. L splits
    as 𝓡M_μ + T by (eq:szego-repr) with 𝔠 = log h°(z) and E3.4(i)'s arcsine moments.
  - Diagonal factors commute, so Δ_k♮ = G_μG_TΔ_k^{mod,β′}G_T^{−1}G_μ^{−1} exactly, for every k.
  - Step 2 (window bound for T): the disc U(x₀, 2η₀) has distance ≥ 2η₀ from (−∞, 0] and lies in |w| ≤ R₁ − η, and for
    |x − z| ≥ η₀ the sup bound applies.
  - Step 3: G_μ is entire (E3.4(ii), REVIEWED) and |μ^δ_n| ≤ C.

  Correct. Normalising h° at 1 instead of at 0⁺ is harmless (constants cancel in h°^{1/2}/D_{h°}).
- **Cor Hc.4.** Correct as a statement about G1u (B)'s input. See C-2 for the one N.6 ingredient not covered by "N.6a–c for
  M(β, ν)".

### Findings
**Hc-1 (MINOR; Rule C.2 bookkeeping, as G12 review F4).** Hc.2 uses DLMF 5.9.1, 25.2.1 (and 25.4.1 at δ = 0) through the CITATIONS
entries "(Plan E3)" and "(DLMF-zeta, Plan 67)". Neither entry records the reuse. *Fix:* append to RH/CITATIONS.md "(Plan E3)":
"**Also used in: JZC_M3a_H_Hc** (Lemma Hc.2(i)): 5.9.1 with μ = 1, ν = kp, z = m·aₙ, unchanged by δ (the factor e^{2πimδ} is
outside the integral); hypotheses as above." Append to "(DLMF-zeta, Plan 67)": "**Also used in: JZC_M3a_H_Hc** (Lemma Hc.2(i)):
25.2.1 at s = 1 + kp for the Fubini bound and |S_k(δ)| ≤ ζ(1+kp); 25.4.1 only at δ = 0."

**Hc-2 (INFO; Hc.3 Step 1 at the crossing points).** (eq:szego-repr) is stated in Paper 2 "for every z ∉ [0, 4c]". Each circle
crosses [0, 4c] at x₀, where Δ_k♮ is taken as a boundary value. The identity extends there by continuity: the density
(log h°(x) − log h°(z))/(z − x) is C¹ near x₀ by Hc.2 (ii). Step 2's window bound covers exactly this. Optionally add "(at the
crossing point x₀, by continuity of both sides from ℂ_±)" after "(eq:szego-repr) with 𝔠 = log h°(z)".

Checks: m3a_hc_pgt1 re-run, **ALL 240 CHECKS PASSED**; m3a_hc_gauge re-run, **ALL 34 CHECKS PASSED** (both byte-identical; 981 s, 996 s).

---

## 5. Re-run of the repo checks

All runs used the scratch venv described above, from research/G1/RH/spectral/checks, with outputs written to the scratchpad and
compared with `diff` against the stored .out. The seven scripts ran in parallel on a 2-core machine that another agent was also
loading (load ≈ 6), so the wall times are inflated.

| Script | Result | Stored .out | Wall |
|---|---|---|---|
| m3a_ha_interp.py | ALL 298 CHECKS PASSED | byte-identical | 537 s |
| m3a_hd_outer.py | ALL 34 CHECKS PASSED | byte-identical | 276 s |
| m3a_hd_model.py | ALL 42 CHECKS PASSED | byte-identical | 766 s |
| m3a_g1u_hardedge.py | ALL 110 CHECKS PASSED | byte-identical | 62 s |
| m3a_g1u_endtoend.py | ALL 29 CHECKS PASSED (cached coefficients) | byte-identical | 21 s |
| m3a_hc_pgt1.py | ALL 240 CHECKS PASSED | byte-identical | 981 s |
| m3a_hc_gauge.py | ALL 34 CHECKS PASSED | byte-identical | 996 s |

MANIFEST.sha256 lists m3a_hd_model.py/.out and m3a_hd_outer.py/.out, and their hashes match. The Ha, G1u and Hc check files are not
in MANIFEST.sha256 (INFO: add them when the memos are committed as reviewed).

Rule N: every pass/fail I inspected is computed. Spec_common.Checks asserts |value − pred| ≤ tol, and controls are asserted as
failures. Ha's wrapper takes real parts, but every complex comparison is passed through abs() first. I found no hard-coded flag.

---

## 6. The chain for p > 1: H-a → H-b → H-b′ → H-c → H-d → H-e → (i)

| Link | Supplied by | Inputs it needs | Status after this review |
|---|---|---|---|
| H-a | Ha L Ha.1–P Ha.5, contour | Paper 2 T1(a) (re-proved for x₁ > 1), L5.1–5.2, Step 1 | OK (Ha-1, Ha-2 wording); **C-1** adds F5 on the moved arcs |
| H-b | G12 L1.1–C1.5 (review A: ACCEPT WITH FIXES) | Paper 2 binet-bound, binetcut | not re-reviewed here; used as accepted |
| H-b′ | G12 L2.1–P2.4 | Paper 2 App C | as above |
| H-c | Hc.1–Hc.3, Cor Hc.4 | G12 L1.1–L1.3, P1.4; E3.4 [REVIEWED]; G1u L1–L2 (form of the data only) | OK; no circularity (Hc uses G1u's *definitions*, G1u (B) uses Hc's *estimate*) |
| H-d | Hd Lemma (i)–(iii), (iv) via G12 L2.3 | H-a (Step 1 with κ_δ), H-b (F♮ → C_δ, (O1)–(O5)) | OK (Hd-1 is a false sentence about two far arcs, without effect) |
| H-e | G1u L1–L4, Prop (A), (B); JZC_M4_proof N.6a–c | H-b′ (P2.4) for L4; H-c for (B); F1–F6 for Q♮ | OK given C-1 |
| (i) | Thm N.6(i) for M(β′, α) (JZC_M4_proof §6 + JZC_M3a_H §3.3) | N.6a–c **and E3 Lemma E3.7** | **C-2**: E3.7 for M(β, ν) is used but not stated |

**C-1 (MINOR) = G1u-1.** F5 on the lengthened Σ^{△±}, saturated segment and the moved top segment. Verified above, with the fix text.

**C-2 (MINOR; JZC_M3a_H.md §3.3 and JZC_M4_proof §6 (i)).** The proof of Thm N.6(i) (JZC_M4_proof l. 272–281) gets 𝔇_{β,K} = O(n⁻²)
for |β| ≥ 2, and hence the remainder O(n^{−2−(B+1)p}), from **E3 Lemma E3.7**: the n⁻¹ coefficient is d₁ + cpM_μ(4c), exactly
linear in μ. JZC_M3a_H.md §3.3 asserts "Lemmas N.6a–c hold for M(β, ν) verbatim" but says nothing about E3.7. E3.7's proof is a
sympy identity in which:
- the soft-edge data A_r, B_r enter with the weight exponent as a symbol. In M(β, ν) that symbol is β, and the identity
  i(Δ₂₁ − Δ₁₂)/(2c) = cpM₄ is free of it;
- the hard edge enters only through "G(0) commutes with A₀". In M(β, ν), A₀ is built from ν (Bessel) and from ρ♮, which
  depends on β. The commutation was asserted only for β = ν.

Without E3.7 for M(β′, α), the |β| = B + 1 terms are only O(n^{−1−(B+1)p}), and the stated remainder of Theorem H(i) is not proved.

*My check (NUMERICAL; …/scratchpad/review/lin_check.py, using the repo's m4_rh4.run(p, β′, nu = α, mu = …), dps 40).* At
(p, α, β′) ∈ {(1.5, −½, −2.1), (3, −0.3, −2.1), (1.25, 0.4, −0.2)} I computed d₁(μ) at μ_k ∈ {−0.2, 0, 0.2, 0.4} (k = 1, 2).
- The second and third differences are ≤ 6·10⁻⁴⁰.
- The slopes are exactly cpQ_k(4c) (c = 1): p for μ₁, 6p for μ₂.

So E3.7 holds for M(β′, α) numerically.
*Fix (JZC_M3a_H.md §3.3, first bullet, append):* "E3 Lemma E3.7 (the n⁻¹ coefficient is d₁ + cpM_μ(4c), exactly linear in μ) also
holds for M(β, ν). The soft-edge part of its identity is free of the weight exponent symbol. The hard-edge part needs
[G_μ(0), A₀(β, ν)] = 0. To be asserted exactly by re-running check_e3_gauge.py with β and ν separated. NUMERICAL now:
REVIEW_JZC_M3a_H_pgt1_chain_A C-2 (second differences ≤ 10⁻³⁹ at three (p, α, β′))." Until that exact check exists, the label of
(i)'s remainder term n^{−2−(B+1)p} should read "PROVED-mod-cite, with E3.7 for M(β′, α) NUMERICAL". Everything else in (i) is
unaffected.

**Chain verdict.** For p > 1 (−1 < δ ≤ 0, 1 < s < 1 + 2p) the chain H-a → H-b → H-b′ → H-c → H-d → H-e → (i) has **no mathematical
gap that I could find**. It has two unwritten links:
- C-1 is routine and verified here;
- C-2 is true numerically to 10⁻⁴⁰ and needs one line plus an exact re-run of the E3.7 gauge identity with β ≠ ν.

With the fixes applied, (i) for p > 1 is PROVED-mod-cite modulo C-2's exact check. It is not REVIEWED until a second reader
re-runs the checks (JZC_M3a_H §4's convention). G12 is used here as accepted by its review A; I did not re-review it.

## 7. Rule A (reviewer's adversarial attempts)
1. *δ ≤ −½ and the phantom point*: Ha-1. This is a false sentence, not a counterexample.
2. *Is (Y2) independent of (Y4)?* No (Ha-2).
3. *Do the lip phases leak into the Airy disc?* No. The phase-carrying arcs (lip (2,1) entries, Σ^△, top) all avoid U(4c, ε),
   since ε < h₀ (Hd-1).
4. *β′ = −α (|β′| = |α|)*: then the Bessel data of ν = β′ and ν = α coincide, so the data cannot discriminate there. The theory
   does not need it to (G1u-3).
5. *Decoupled model at |β| ≥ 2 in μ*: E3.7 at β ≠ ν (C-2). Tested numerically and true.
6. *Top region with a → 0*: the F5 constants grow like a^{−p−1} (C-1). This is fixed-δ, so n₀ = n₀(p, s, δ) as stated.
7. *p = 2*: E_pgt1's "H_n constant" fails for δ ∉ {0, −½}. Hc records this and does not use it. Verified.
8. *Circularity Hc ↔ G1u*: none (§6 table).

Novelty: not assessed (outside remit). No RH claim is made or needed.
