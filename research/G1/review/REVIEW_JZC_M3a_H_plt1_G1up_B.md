# Rule R review: Theorem H (i) for 0 < p < 1, the n-uniform part (G1u′ and Hc.5), reviewer B

Reviewer: independent second reader (Rule R), reviewer **B**. Date: 2026-10-22. Branch plan-e2-d2, HEAD c961b47.
- Targets (NOT REVIEWED before this report):
  1. research/G1/RH/spectral/JZC_M3a_H_G1u_plt1.md ("G1up"): Lemmas P1–P5, Prop G1u′ (A), (B), §3a change table, §5–§6;
     checks/m3a_g1up_hardedge.py/.out, checks/m3a_g1up_endtoend.py/.out;
  2. research/G1/RH/spectral/JZC_M3a_H_Hc.md, **Lemma Hc.5 only** (§4), and its consistency with L P5; checks/m3a_hc_gauge.py/.out
     (the p < 1 rows).
- Context read: AGENTS.md, VERIFICATION_POLICY.md; JZC_M3a_H.md (statement, §2, §3.2–3.3, §4); JZC_M3a_H_Hc.md §0, §3 (Hc.3, the
  p > 1 template of Hc.5), §5–7; JZC_M3a_H_G23plt1.md §2 (Lemma M, Lemma F.1_δ, the §2.2 line table); JZC_M3a_H_Ha.md (scope:
  p < 1 covered); JZC_M4_proof.md N.6a–c (incl. the p < 1 bullets); second_order/E3.md Lemma E3.4; second_order/E_plt1.md
  Prop E′.5′ (1)(b); the format example REVIEW_JZC_M3a_H_pgt1_chain_A.md; papers/paper2/sec_6.tex l. 150–200 ((eq:szego),
  (eq:szego-repr) "for every z ∉ [0, 4c] and every number 𝔠", (eq:DW-factor), (eq:omega), Lemma szego (i)), sec_7.tex l. 180–235
  ((eq:he-Phi-jumps), (eq:he-Phi-large), (eq:he-Phi-small), (eq:he-ephi), (eq:he-P0hat), Lemma comparison-parametrix), sec_5.tex
  (eq:thetaw), (eq:angles).
- I edited no file except this report. My own scripts and run outputs are in the session scratchpad
  (`…/scratchpad/rev_g1up/`: indep_P1.py, sens_d2eps.py, run_e2e_fresh.py and the .out files); they are not repo code.
- Environment: the repo `.venv` does not exist in this checkout; every script was run with the session venv
  (`…/scratchpad/venv/bin/python -B`). The machine was shared with other reviewers (load ≈ 15 on 2 cores), so the wall times
  below are not comparable with the memo's.

## Overall verdicts

| Target | Verdict | Findings |
|---|---|---|
| G1up Lemma P1 (seam band factor, Cauchy difference) | **ACCEPT** | P1-1 (MINOR, a constant), P1-2 (INFO) |
| G1up Lemma P2 (ρ♮) | **ACCEPT** | — |
| G1up Lemma P3 (glued parametrix; glue jump; circle expansion) | **ACCEPT WITH FIXES** | P3-1 (MINOR: the R-frame seam jump is not J_g) |
| G1up Lemma P4 (lip mismatch; fixed-n identification) | **ACCEPT** | — |
| G1up Lemma P5 (gauge = H-c, p < 1) | **ACCEPT** | P5-1 (INFO, "independent") |
| G1up Prop G1u′ (A), (B) | **ACCEPT WITH FIXES** | = P3-1 in (B); G-1 (MINOR, stale labels/statuses) |
| G1up §3a change table | **ACCEPT** | (no wrong row found) |
| G1up checks (hard edge, end-to-end) | **ACCEPT WITH FIXES** | N-1 (MINOR, over-conservative control guard), N-2, N-3 (typos in docstrings), N-4 (INFO, circle radius) |
| Hc.5 (p < 1 gauge given F.1_δ) | **ACCEPT WITH FIXES** | Hc5-1 (MINOR, stale "still open" paragraph), Hc5-2 (typo in check docstring) |
| Consistency Hc.5 ↔ L P5 | **consistent** (same μ, same G_μ, same remainder; normalisation 𝒢(1) vs 𝒢(0) cancels) | — |
| JZC_M3a_H.md (status of (i), p < 1) | fixes to bookkeeping only | H-1 (MINOR, stale table rows / garbled sentence) |
| **Theorem H (i), 0 < p < 1** | **no missing mathematical link found** | its unreviewed links are G3 and G23plt1 (see §6) |

**No MAJOR finding.** I re-derived every lemma of G1up and Hc.5 from the write-ups (record in §1–§3). I re-ran
m3a_g1up_hardedge.py, m3a_g1up_endtoend.py (with **re-generated** caches) and m3a_hc_gauge.py; results in §4. I also wrote
two independent checks (a pointwise test of L P1 (b) and an ε₂-sensitivity test of the end-to-end d₂|ε row).

On the four points the coordinator asked about:
- **δ-uniform constant of L P1:** justified. Every estimate uses ℓ_± only through (M2) |ℓ_±| ≤ ℓ and (M3) |ℓ_±′| ≤ ℓ′. The
  geometry constants (θ, τ, R₁, c₁, n₀) depend on p only. Confirmed independently, pointwise in (z, x) (§4.3).
- **"Paper 2's Szegő formula allows choosing the side of the seam":** correct. (eq:szego-repr) is an identity in the free
  number 𝔠 (sec_6.tex l. 170–173), so using the S_out value or either seam boundary value of log h° at z is legitimate. The
  resulting L_h is exactly what ρ♮ needs, sector by sector (§1, L P1 (d) and L P2 (i)). Paper 2's sentence "We use it with
  𝔠 = log q(z), the value of an analytic continuation" is a usage note and not a hypothesis.
- **Polynomial glue amplification in the Q-frame:** correct. X := (2πn)^{σ₃/2}Φ_α(n²f) satisfies |X^{±1}| ≤ Cn^{1/2}|z|^{−1/2} on
  U_0, from (eq:he-Phi-large)/(eq:he-Phi-small); the e^{∓2√ζ} factors are inside Φ_α (Θ₀, Θ_∞). Hence
  |J_g − I| ≤ Cn|z|^{−3/2}q + Cq. The R-frame jump is also polynomially amplified, but it is not J_g (P3-1).
- **Non-asserted controls:** they do not hide a failure. The only genuinely vacuous ones are the [1] n^{−2p} control at
  (0.3, −0.98) (S₁ ≈ 0) and, at (0.75, 0.3, −0.3), the band-factor-dropped control (m₁ small) and the ν = β′ control (|β′| = |α|).
  With the guard "e_mod > 10 e_true" the dropped-factor control is asserted in 2 of 5 sets. With the claim's own exponent window
  it would be asserted, and would fail as required, in **4 of 5** (N-1). The evidence is adequate. It is also backed by [1], which
  tests L P1 (d), the statement that carries the band factor, directly and with discriminating controls.

---

## 1. Lemma P1 (re-derivation): ACCEPT

**(a).** F.1_δ (ii) holds with the sector value at every w ∉ Γ₊ ∪ Γ₋ ∪ {0}. The Liouville step of its proof (G23plt1 §2.2, rows
"K₀ … Morera", "Liouville") makes 𝒢_δ − 𝒢_δ(1) − 𝒥 ≡ 0 globally, not sector by sector. Subtracting at w = z and w = x and using
K(ζ, z) − K(ζ, x) = 1/(ζ − z) − 1/(ζ − x) = (z − x)/((ζ − z)(ζ − x)) gives (a). I checked the identity
K(ζ, w) = 1/(ζ − w) − 1/(ζ − 1) = (w − 1)/((ζ − w)(ζ − 1)) against G23plt1's form. The limit x → 0⁺ is dominated by (B1) and by
ℓ = O(e^{−c₁n}r^m) near 0.

**(b).** I redid each estimate.
- Far-part expansion: 1/((ζ − z)(ζ − x)) = (z − x)^{−1}Σ_{j≥0}(z^j − x^j)ζ^{−j−1} = Σ_{k≥1}q_kζ^{−k−1}. With |q_k| ≤ kR₁^{k−1} and
  r ≥ 2R₁, the tail is ≤ C_Kr^{−K−2}.
- Mellin integral: with u = 2πnr^{−1/p}, I get ∫_0^∞ℓr^{−K−2}dr = p(2πn)^{−(K+1)p}Γ((K+1)p)ζ(1 + (K+1)p), as stated.
- (B2): ℓ ≤ 2q for q ≤ ½ (convexity of −log(1 − q)). ℓ′ = q′/(1 − q) with q′ = qy/(pr), and r^{−m}e^{−y} ≤ y^{mp}e^{−y} with
  (2πn)^{−mp} ≤ 1. Hence the e^{−c₁n} bounds hold, c₁ = π(2R₁)^{−1/p}.
- (B3) is correct. In both cases the inequality is the stated one.
- Case B:
  - (1 − τ)|z| ≤ r* (r* = |z|cos ψ, sin ψ < τ), |z − z*| ≤ τ|z| ≤ r*/4, and 𝒲 ⊂ {|ζ| ≤ 1.8R₁} ⊂ near part.
  - Constant term: the argument of ζ − z changes by < π along a segment not through z, and by exactly π in the boundary-value
    limit. So the bound log 3 + π holds for the boundary values too.
  - Remainder: |ζ − z| ≥ |ζ − z*| by Pythagoras.
  - Off 𝒲 I get |ζ − z| ≥ (|ζ| + r*)/10, slightly better than the memo's /12. The memo's constant is still correct.
  - On Γ₋ the angle between z and Γ₋ lies in [θ, π]. For rays at angle φ ∈ [θ, π], |ae^{iφ} − b| ≥ sin(φ/2)(a + b) ≥ sin(θ/2)(a + b),
    as stated.
  - Two cases cannot hold at once, since 2 arcsin(τ) < 2θ.
- All constants depend on (p, K) only. The only δ-input is (M2)–(M3) (Lemma M, PROVED, re-checked: |1 − w| ≥ 1 − q).
  **The δ-uniformity claim is justified.**

**(c)** is (a)–(b) at x = 0.

**(d).**
- Sector by sector, L_h(z) = (𝓡/π)∫(log h°(x) − log h°(z))dx/(√(x(4c−x))(z − x)) with 𝔠 = log h°(z).
- Then log h°(x) − log h°(z) = 2(𝒢(z) − 𝒢(x)) = 2(z − x)I(z, x) (sector value at z, S_in value at x).
- The arcsine moments (1/π)∫_0^{4c}x^jdx/√(x(4c−x)) = C(2j, j)c^j give (1/π)∫q_k(·)dx/√(·) = Q_k(z).
- So L_h = 𝓡Σμ_kQ_k + (2𝓡/π)∫I_K dx/√(·), μ_k = 2m_k. This matches E3 L E3.4 (i)'s convention q_μ = e^{−P_μ} (E3.md l. 127–128:
  (𝔠(x) − 𝔠(z))/(z − x) = Σμ_k(x^k − z^k)/(x − z), i.e. 𝔠 = −P_μ). Here log h° ≈ −2Σm_kz^k = −P_μ: signs consistent.
- Reality of h°: (F.1_δ) with ℓ₋ = conj ℓ₊ gives 𝒢(z̄) = conj 𝒢(z). I verified the conjugation of the integrand term by term.

Remark P1.4 (single integral; check only): (1/π)∫dx/(√(·)(ζ − x)) = 1/𝓡(ζ) with ζ on the seams (off [0, 4c]); Fubini by (B1).
Correct. The script implements it as stated (w = z/e^{±iθ}, ∫ℓ/(r − w)dr = ∫ℓe^{±iθ}dr/(ζ − z)).

- **P1-1 (MINOR, constant only).** In (b) Case B, "Off 𝒲 on Γ₊: … ≥ |ζ − z*|/2 ≥ (|ζ| + r*)/12" is true. The intermediate step
  "|ζ − z*| ≥ (|ζ| + r*)/6" is not written. *Fix text:* after "≥ |ζ − z*|/2" insert "and, ζ and z* lying on one ray with
  ||ζ| − r*| ≥ r*/2, |ζ − z*| ≥ (|ζ| + r*)/5,".
- **P1-2 (INFO).** The "n-uniform replacement of (O3)–(O4)" (Remark P1.1) is correct and is the reason no derivative bound is
  needed. This is a genuine simplification over Hc.5's route.

## 2. Lemmas P2–P5 and Prop G1u′

**L P2.**
- (i): W̃♮/D_W with (eq:DW-factor) (r_n ≡ 1) gives ρ♮ = ρ♮^{mod}e^{−(𝒢(z)−𝒢(0))}/D_{h°} = ρ♮^{mod}exp(−½(log D_{h°}² − log h°(z))),
  with the sector value at z. Exactly L_h, sector by sector. The bounds follow from L P1 (d) at K = 0 and |1 + β′| < 2.
- (ii): (−z)^{β′} = z^{β′}e^{∓iπβ′} in ℂ_±, so ρ♮² = e^{∓iπβ′}/ω^{(β′)}. Then ϱ_±ρ♮^{−2} = e^{±iπ(β′−α)}ω = e^{±2πiδ}ω = ω♮.
  The lips (≤ (5/4)θ_L = 5θ/8 with 𝗆 = 1; smaller for 𝗆 < 1, Paper 2 (eq:thetaw)) lie in S_in.
- (iii)–(v): verified; |e^{−ℓ_±} − 1| = q exactly.

**L P3.**
- (i): ρ♮^{σ₃} = (ρ^{mod})^{σ₃}e^{−L_hσ₃/2}, so Â♮ = Â^{mod}·f^{−σ₃/4}M^{−1}e^{−L_hσ₃/2}Mf^{σ₃/4}.
  - M^{−1}diag(a, b)M has entries of size |a − b| off the diagonal. The f^{∓1/2} weights give |𝔈| ≤ C|L_h|(1 + |f|^{−1/2}) ≤ Cn^{−p}.
  - det(I + 𝔈) = 1. Y_± likewise.
  - This is the core of the memo, and it is right.
- (ii):
  - P̂_in^{−1}P̂_out = ρ_in^{σ₃}X^{−1}Y_±Xρ_in^{−σ₃}e^{ℓ_±σ₃}: verified.
  - Seams in the central sector: arg f = arg z ∓ π, so |arg ζ| ≈ π − θ < π − θ_L.
  - Bounds on X from (eq:he-Phi-large) (X = (2πn)^{σ₃/2}ζ^{−σ₃/4}Θ_∞, |X| ≤ C|z|^{−1/4}) and (eq:he-Phi-small)
    (|X| ≤ Cn^{1/2}|ζ|^{−|α|/2} ≤ Cn^{1/2}|z|^{−1/2} for |ζ| ≤ 2, |α| < 1).
  - So |J_g − I| ≤ Cn|z|^{−3/2}q + Cq: verified.
- **P3-1 (MINOR).** Prop G1u′ (B), bullet "in U_0: … and on the seam segments (L P3 (ii))", applies J_g's bound to the jump of R.
  - R's seam jump is J_R = P̂_in J_g^{−1}P̂_in^{−1}, as L P4 (b) itself writes, not J_g. Its n-uniform bound does not follow from
    L P3 (ii) by quoting it: conjugating by |P̂^{±1}| ≤ Cn^{1/2}|z|^{−1/2} costs another n|z|^{−1}.
  - The conclusion survives. Directly, J_R = Â♮_inXe^{−ℓ_±σ₃}X^{−1}Y_±^{−1}(Â♮_in)^{−1}, hence
    |J_R − I| ≤ C(n|z|^{−1} + |z|^{−1/2})q ≤ C_Kn^{−K}min(1, |z|^K).
  - *Fix text* for Prop G1u′ (B), second bullet: replace "and on the seam segments (L P3 (ii))" by "and on the seam segments,
    where J_R = P̂₀♮_inJ_g^{−1}P̂₀♮_in^{−1} = Â♮_inXe^{−ℓ_±σ₃}X^{−1}Y_±^{−1}(Â♮_in)^{−1}, so |J_R − I| ≤ C(n|z|^{−1} + |z|^{−1/2})e^{−2πn|z|^{−1/p}}
    by L P3 (i), (ii)". Optionally add this formula to L P3 (ii) as a fifth bullet.
- (iii), (iv): G1u L2's proofs with bounded ρ♮^{±1}, Â♮^{±1}. Verified that only conjugation by ρ♮^{σ₃} enters Δ_k♮.

**L P4.**
- (a): ρ♮^{−2} = (Υ̂/4c)^{−(1+β′)}e^{L_h}, so |ω♮ − ϱ_±| ≤ C|z|^{1/2}: correct.
- (b): |R| ≤ |Q♮||P̂^{−1}| ≤ C_{n,η}|z|^{−|α|−η}. R has no band jump and no jump on (−δ_r, 0). The local jumps are super-small and
  Hölder on finitely many rays. Removability needs |α| + 2η < 1. Correct.

**L P5.**
- ρ♮² = (ρ^μ)²e^{−(L_h − 𝓡M_μ)}. Diagonal factors commute, so Δ_k^{0,μ} = G_μΔ_k^{mod,β′}G_μ^{−1} exactly for every k. I re-did
  the commutation with G_μ := P₀^∞e^{−𝓡M_μσ₃/2}(P₀^∞)^{−1}.
- Soft edge: ω^{(β′)}/ω^μ = e^{L_h − 𝓡M_μ} by (eq:omega) and E3.4 (i).
- L P1 (d) holds on both circles (both lie in |z| ≤ R₁ and off [0, 4c] except at one crossing each, where it holds for both
  boundary values). Correct.
- **P5-1 (INFO).** "The two proofs are independent" is accurate in the sense stated: L P5 needs no derivative bound. Both still rest on
  the representation (F.1_δ) and Lemma M. L P1's Case B is (iv)'s window argument redone. A G23plt1 error in (F.1_δ) (ii) would
  hit both.

**Prop G1u′.**
- (A): Q̃ (A₀, Φ_α at 0) never sees the seams or the glue. Q♮ has no seam jump. Only L P4 (a) and the soft-edge Szegő bound
  (L szego (vi)(b), with 𝔐 n-free from L P1 (c) on U(4c, 2ε₁) ⊂ S_in) enter. Correct.
- (B):
  - The jump list is complete once P3-1 is fixed.
  - ‖𝒞₋‖ is bounded with the extra fixed rays as in E_plt1 Prop E′.5′ (1), REVIEWED at δ = 0.
  - The N.6c residue recursion needs meromorphic circle data. The true Δ_k♮ have a super-small discontinuity at the seam
    crossings of ∂U_0, which L P5 replaces at a cost O(n^{−1−(J+1)p}).
  - The remainder O(n^{−K−1} + n^{−1−(J+1)p}) matches Theorem H (i).
- **G-1 (MINOR, stale statuses).** Several G1up sentences are out of date with HEAD.
  - G1up §0 "Overlap": "That memo (another agent, in progress, read-only here)".
  - The L P5 row of the table: "(being written in parallel)".
  - §2.5 last paragraph: "NOT REVIEWED, in progress by another agent".
  - The L P3 citation "G1u L2 [NOT REVIEWED]" and §4 "G1u L1–L4 (PROVED-mod-cite, NOT REVIEWED)". G1u L1–L4 are REVIEWED for p > 1
    (review A of the p > 1 chain), and their p-free parts are what is used here.
  - §4 "For p > 1, (i) rests on H-c (JZC_M3a_H_Hc.md Cor Hc.4, in progress)": Cor Hc.4 is REVIEWED.
  - *Fix text:* replace each with "JZC_M3a_H_Hc.md Lemma Hc.5 (NOT REVIEWED before Rule R review B)" / "G1u L1–L4 [REVIEWED for
    p > 1, review A; used here only in their p-free parts]" / "Cor Hc.4 (PROVED-mod-cite + REVIEWED)".

**§3a.** Each row checked against RH_plt1b §2, E_plt1 §0/E′.3/E′.5/E′.5′, N.6a–c and G1u L1–L4. I found no wrong row.
- The "verbatim" claims that matter (E′.3 sectors; N.6b parity, β-free) hold.
- The row "E_plt1 Prop E′.5′ (1)(b) … CHANGED (value; bound sharper)" is right. E_plt1's e^{Cn|z|^{1/2}} amplification
  (E_plt1.md l. 319–320) is a valid but weaker bound from the classical frame.

## 3. Hc.5 (re-derivation): ACCEPT WITH FIXES

- Step 1 sector-wise: the split L = 𝓡M_μ + T with E := the sector value of E_n^{(J)} is exact, because P_μ is entire. G_T
  commutes with G_μ, so Δ_k = G_μG_TΔ^{mod,β′}G_T^{−1}G_μ^{−1}.
- Step 2: off U(x₀, η₀), dist(z, [0, 4c]) ≥ d. The sup bound of F.1_δ (iv) (seam boundary values included) suffices there.
  Inside, U(x₀, 2η₀) ⊂ S_in.
  - With η₀ ≤ δ_r sin(πp/2)/4 I get dist(U(x₀, 2η₀), Γ_±) ≥ δ_r sin(πp/2) − 2η₀ ≥ 2η₀. That is better than the memo's
    "≥ η₀ sin(πp/2)", which is true but weaker; only the constant changes.
  - So F.1_δ (iv)'s derivative bound applies with η = η₀ sin(πp/2).
- Step 3 verbatim.
- **Consistency with L P5.**
  - Same μ^δ_{n,j} = 2m_j(δ) and same G_μ. Same conclusion and the same remainder O(n^{−(J+1)p}).
  - Hc.5 normalises h° by 𝒢(1), L P5 by 𝒢(0). The constant cancels in (eq:szego-repr) (𝔠 constant ⇒ L unchanged).
  - Both take log h° sector-wise, which is the same L. **Consistent.**
  - Hc.5 needs F.1_δ (iv) (sup + derivative). L P5 needs only F.1_δ (i)–(iii) + Lemma M plus L P1's own estimates.
  - Either closes H-c for p < 1, given G23plt1.
- **Hc5-1 (MINOR, stale).** Hc.md §4, the paragraph "*Not part of H-c, still open for p < 1 (G1u "p < 1"):* the glued hard-edge
  parametrix rebuilt with W̃♮ … and items 2–3 of JZC_M3a_H §4 (now in G23plt1)". The glued parametrix is now
  JZC_M3a_H_G1u_plt1.md, and the same applies to the table row Hc.5 ("the hard-edge data in the α-frame need the glued W̃♮
  (G1u "p < 1", not part of H-c)") and §7 bullet 2.
  - *Fix text:* "*Not part of H-c (p < 1):* the glued hard-edge parametrix with W̃♮ is JZC_M3a_H_G1u_plt1.md (L P2–P3), which
    also gives an independent proof of Hc.5 (L P5); items 2–3 of JZC_M3a_H §4 are G23plt1."
  - Also: "boundary values at the seams and at (−δ_r, 0) included". For p < 1 there is no cut on (−δ_r, 0); the point −δ_r ∈ S_out
    is an ordinary point. Harmless; delete "and at (−δ_r, 0)".
- **Hc5-2 (typo).** checks/m3a_hc_gauge.py docstring line 1: "Hc.4 (p < 1)" → "Hc.5 (p < 1)".

## 4. Checks re-run (Rule R)

### 4.1 m3a_g1up_hardedge.py
- Re-run in full (no cache involved).
  - Output **byte-identical** to the stored m3a_g1up_hardedge.out (`diff`, after stripping the `time` lines).
  - **ALL 157 CHECKS PASSED**: 34 controls fail as required; 5 controls are printed as "not applicable".
  - Wall time 101 min (user 40 min) on the loaded machine.
- I recounted the assertions from the code: [0a] 1, [0b] 2, [1] 60 + 8 controls, [2] 25, [3] 15, [4] 15, [5] 15 + 2 + 4, [6] 10.
  That makes 157, of which 34 are controls, matching memo §5a.
- What the asserted rows establish, read against the lemmas:
  - [0a]: the Fubini formula (Remark P1.4) equals (eq:szego-repr) at a seam boundary value and in S_out, to 7·10⁻²⁹.
  - [0b]: the representation equals G3's literal glued exponent next to both seams, to 8·10⁻²⁷.
  - [1]: L P1 (c), (d) for K ≤ 2, flat in n and below the δ-free majorant at δ = −0.02, −½, −0.98.
  - [2]–[6]: L P2–P4 and P3 (iii) with the true glued ρ♮, β′ down to −2.2.
- The 5 "not applicable" cases are analysed in N-1.

### 4.2 m3a_g1up_endtoend.py (caches re-generated)
- **Caches re-generated, not reused.** I ran the script through a wrapper (`run_e2e_fresh.py`) that only redirects
  `so_coeffs.CACHE` to an empty scratchpad directory. All six measures (p = 0.6, s = 1.3, δ ∈ {−0.8, −½}, K ∈ {1.6, 3.2}·10⁵;
  p = 0.75, s = 1.375, δ = −0.8, both K) were recomputed from scratch with binary128 RKPW.
  - The six regenerated cache files are **byte-identical** to tmp/plan62_cache/ (`cmp`).
  - The output is **byte-identical** to the stored m3a_g1up_endtoend.out (`diff`, after stripping the `time` lines).
  - **ALL 29 CHECKS PASSED**, 9 of them controls (dev/tol 39.6 … 6·10⁴).
  - Wall time 63 min (user 20 min) on the loaded machine.
- Re-derived: d₁ = −p(β′+1)/2 (0.33, 0.15, 0.4125), as in the script's assertion against m4_rh4.run.

### 4.2a m3a_hc_gauge.py (Hc.5's check, p < 1 rows included)
Re-run: output **byte-identical** to the stored m3a_hc_gauge.out; **ALL 34 CHECKS PASSED**, 9 of them controls.

### 4.3 Independent checks (reviewer's scripts)
- **L P1 (b) pointwise** (`indep_P1.py`, own quadrature: direct mp.quad of the two seam integrals; S_k(δ) by mp.polylog rather than
  the author's residue classes):
  - Setup: p = 0.6; z ∈ {0.05, 0.4, 2} × {θ(1 ∓ 10⁻⁸) on Γ₊ both sides, Γ₋ inner side, 0.8π, π}; x ∈ {0, 0.05, 2c, 4c}; δ ∈ {−0.01, −0.5,
    −0.99}; K = 0, 1; n = 10, 40, 160.
  - The author's [1] tests x = 0 and the x-integrated L_h only. This tests the pointwise statement over the band.
  - Results: sup n^{(K+1)p}|I_K|:

    | δ | K = 0 (n = 10, 40, 160) | K = 1 (n = 10, 40, 160) |
    |---|---|---|
    | −0.01 | 0.187, 0.176, 0.171 | 0.0863, 0.0851, 0.0845 |
    | −0.5 | 0.0715, 0.0645, 0.0616 | 0.0538, 0.0525, 0.0518 |
    | −0.99 | 0.140, 0.127, 0.122 | 0.0961, 0.0934, 0.0922 |

  - Every value is flat in n and below twice the δ-free next-term majorant (0.432 for K = 0, 0.191 for K = 1). The bound is
    δ-uniform up to both ends of (−1, 0).
- **End-to-end d₂|ε sensitivity** (`sens_d2eps.py`, p = 0.6 cases, my regenerated K = 1.6·10⁵ caches). The row d₂|ε subtracts the
  predicted ε₂, which is itself not asserted (not discriminating). Replacing ε₂ by 0, 2ε₂, −ε₂ moves d₂|ε as follows:
  - δ = −0.8: +0.197314 → +0.196433, +0.198342, +0.195545;
  - δ = −½: +0.082111 → +0.084112, +0.080346, +0.085827.

  So the row moves by ≤ 0.004, against its tolerance 0.018 and the H2 control's distance of ≥ 40 tolerances. The row is a genuine
  test of d₂ and is insensitive to ε₂. It is not circular (it is also no test of ε₂).

### 4.4 Findings on the checks
- **N-1 (MINOR; the coordinator's question).** The band-factor-dropped control of [5] is asserted only if e_mod > 10·e_true at
  n = 400 (2 of 5 sets).
  - The guard is stricter than needed. The control's own criterion ("all exponents of the dropped-factor remainder ≥ 1.9") fails,
    as required, at (0.6, −0.6, −0.8) (1.783, 1.751, 1.724) and at (0.75, 0.6, −0.95) (1.917, 1.898, 1.881).
  - It passes vacuously only at (0.75, 0.3, −0.3) (1.991, 2.009, 2.012), where m₁(−0.3) is small.
  - So the [5] claim window [1.9, 2.15] does distinguish the true ρ♮ from ρ^{mod} in 4 of 5 sets. Nothing is hidden.
  - *Fix text* (optional, script and §6 item 9b): replace the guard `if eM[-1] > 10*eT[-1]:` by
    `if not all(mp.mpf('1.9') <= x for x in xM[1:]) or eM[-1] > 10*eT[-1]:`, i.e. assert wherever the control is discriminating
    by the claim's own exponent criterion, and record "asserted in 4 of 5 sets".
  - If the script is left unchanged, amend §6 9b "In the other 3 its effect is 0.9–3.6× … visible but not decisive" to: "In 2 of
    the other 3 the dropped-factor exponents (≤ 1.92 → 1.72–1.88) already fall outside the claim's window [1.9, 2.15]; only at
    (0.75, 0.3, −0.3) is the control non-discriminating."
- **N-2 (typo).** m3a_g1up_hardedge.py docstring:
  - l. 33 "J_g = ceil(1/p) moments" → "J_g = floor(1/p) moments (the smallest J with (J+1)p > 1)", as the code and memo §5a do;
  - l. 15 "at angular distance 1e-8 from both seams" → "at relative angular distance 1e-12 (EPS) from the seams".
- **N-3 (typo).** m3a_g1up_endtoend.py docstring l. 14–15 "each subtracted term is itself tested in its own row, so the conditional
  row is not circular". At p = 0.6, ε₂'s row is not asserted. *Fix text:* "each subtracted term except ε₂ (not discriminating at
  n ≤ 1600) is tested in its own row; the row is insensitive to ε₂ at the scale of its tolerance (Rule R review B, §4.3)". Memo
  §5b already says this correctly.
- **N-4 (INFO).** [5] evaluates the circle expansion at |z| = c/2, while the theorem's circle is |z| = δ_r ≤ c/4 (δ₀ = 2δ_r ≤ c/2).
  The check is still meaningful, because L P1 (d) and L P2 (i) hold on |z| ≤ R₁ and the expansion needs only n²|f| large. One
  sentence in §5a would avoid the mismatch: "(the circle |z| = c/2 is larger than U_0; the algebra is the same)".

## 5. JZC_M3a_H.md (status of (i) for p < 1)

- **H-1 (MINOR, bookkeeping).**
  - (1) §2 table, row H-b′: "p < 1: OPEN (= H-d (iv) for p < 1 …)" contradicts §4 item 2 ("done in JZC_M3a_H_G23plt1.md §1"). *Fix
    text:* "p < 1: G23plt1 P2.6 (PROVED-mod-cite, NOT REVIEWED) (= H-d (iv) for p < 1)".
  - (2) Row H-e: add "for p < 1 the hard-edge circle data are JZC_M3a_H_G1u_plt1.md (L P3, L P5; NOT REVIEWED before review B)".
  - (3) §4 item 1, l. 130–131: "It is uses H-a and item 5 (both done) …" is garbled. *Fix text:* "It uses H-a and item 5 (both
    done) and, for the step to N.6(i), E3.7 for M(β′, α) (§3.3, exact)."
  - (4) Row H-c: add "p < 1 also L P5 of JZC_M3a_H_G1u_plt1.md".

## 6. Theorem H (i) for 0 < p < 1: is any link missing?

Chain:
- H-a: JZC_M3a_H_Ha.md, covers p < 1, REVIEWED.
- H-b: G3 Lemmas 1–3, Prop 4; review A ACCEPT WITH FIXES, checks not re-run, so NOT REVIEWED.
- H-b′ = H-d (iv): G23plt1 P2.6, NOT REVIEWED.
- H-c: Hc.5 given G23plt1 F.1_δ, or L P5 given F.1_δ (i)–(iii) + Lemma M.
- H-d (i)–(iii): G3 Cor 5 + the H-d jump algebra, REVIEWED.
- H-e: G1up L P1–P4, Prop G1u′ + JZC_M4_proof N.6a–c (p < 1 bullets) for M(β′, α).
- E3.7 for M(β′, α): m3a_e37_decoupled, exact in symbolic p, NOT REVIEWED check.
- Extraction: JZC_M4_proof §5–6, Theorem N.6 covers p < 1.

**I found no missing mathematical link.**
- The objects passed between the links match:
  - μ^δ_{n,j} = 2m_j(δ) (Fourier sums);
  - the α-frame with ρ♮ = W̃♮/D_W and Bessel order α;
  - ω♮ = ω^{(β′)}e^{±2πiδ};
  - the seam glue super-small with polynomial amplification;
  - the remainder exponents.
- Once P3-1, G-1, Hc5-1 and H-1 are applied, G1up (L P1–P5, Prop G1u′) and Hc.5 can carry "REVIEWED (review B)" within this
  scope. That is only if the coordinator's convention requires one reviewer who re-derives and re-runs; this review did both.
- Theorem H (i) for p < 1 remains **PROVED-mod-cite, NOT REVIEWED as a whole**. Its unreviewed links are G3 (needs a reader who
  re-runs its checks) and G23plt1 (§1 P2.6, §2 F.1_δ, Lemma M; no Rule R review yet), plus the m3a_e37_decoupled check.
- G1up's and Hc.5's correctness is conditional on G23plt1 F.1_δ (ii) (the representation) and G3 Lemma 3.
  - Numerically the representation equals G3's literal construction near 0 and next to the seams. Check [0b] reproduces this to
    ≤ 8·10⁻²⁷ in my re-run.
  - The review of G23plt1 is therefore the critical remaining step for p < 1.

No RH claim is made or implied here.
