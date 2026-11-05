# Rule R review: JZC Σ, reviewer A: JZC_SIGMA.md (Conjecture Σ via the m-frame)

Reviewer: independent second reader (Rule R), reviewer **A**. Date: 2026-10-22. Branch plan-e2-d2.
- Target: research/G1/RH/spectral/JZC_SIGMA.md (Lemma F (i)–(ii), Prop FI, Theorem Σ, Cor Σ.1, Cor Σ.2, Remark C, §§5–7).
- Context read: AGENTS.md, VERIFICATION_POLICY.md; papers/paper2/app_outer.tex (whole), app_c.tex (whole), sec_5.tex
  (Lemma interp, invariance, §frame-weight, (eq:g), Lemma signs), sec_6.tex (Lemma normalisation), sec_7.tex (§7.1–7.2: (eq:he-Phi-jumps),
  (eq:he-ephi), (eq:he-P0), (eq:he-P0hat), L comparison-parametrix); spectral/JZC_M3a_Hd.md (§0–1), JZC_M3a_H_G12.md (L2.2–P2.4),
  JZC_M3a_H_G1u.md (§0–§2 L1), JZC_M3a_H.md (§1, §3.3, §4), JZC_M4_proof.md (Thm N.6 statement, §5 N.6d, §6), second_order/E3.md
  (Lemma F.1′ and proof).
- I edited no file except this report. Scripts and outputs: scratchpad
  `/tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/` (rr_spot.py, rr_fi.out, rr_z2.out, rr_hi.out,
  exact_cached.out, exact_fresh18.out, num_rerun.out, and the copy rr/ of the checks directory used for the cache-free exact run).
- No statement about RH is made or used; ζ(−jp) enter only as band-factor constants.

## Overall verdict: **ACCEPT WITH FIXES**

I found **no mathematical error** in the chain Lemma F ⇒ (F) ⇒ FI₀ ⇒ Theorem Σ ⇒ Cor Σ.1, Σ.2. I re-derived every algebraic step
(gauge, residues, the two cancellations, the lip phase, band limit, extraction, uniqueness, rationality, FI ⇔ Σ, evenness, the
ζ(−2p)/ζ(−p)² separation) and checked rows 2–5 of the transfer table against the Paper 2 / memo text line by line. One
**MAJOR (scope)** fix: Lemma F (ii) is stated for |γ| < (1−|α|)/2, but its REVIEWED inputs (H-d, G12, G1u, Hc) are stated for
−1 < δ ≤ 0, i.e. γ = −δ ≥ 0; γ < 0 is not covered by any cited statement. The proof of Σ needs only an open set of γ, so the fix is
to restrict to 0 < γ < min(¼, (1−|α|)/2) (S1). The rest are MINOR (missing written steps, wording). With S1–S8 applied,
**Theorem Σ is proved modulo cited results (PROVED-mod-cite)**, with Cor Σ.1 and Cor Σ.2 as stated; the label of the transfer
Lemma F (ii) is exactly as strong as the REVIEWED chain it transfers, and after this review it can carry "+ REVIEWED (reviewer A)".

All re-runs reproduce the stored outputs (§D); my independent numerical checks (new points, general base β ≠ ν, half-integer γ,
the second-order zeta layer 2e₁ that the author did not test, and order 10) all pass with controls failing (§D).

## A. Per-item verdicts

| Item | Verdict |
|---|---|
| Lemma F (i) (frame algebra, §2.2) | **ACCEPT** (fix S2: one missing sentence) |
| Lemma F (ii) (transfer table, §2.3) | **ACCEPT WITH FIXES** (S1 scope γ > 0 — MAJOR; S3 lens computation in row 3; S4 row 2/5 wording) |
| (F) | **ACCEPT WITH FIXES** (range per S1) |
| Prop FI / §3.1 uniqueness | **ACCEPT WITH FIXES** (S1 range; S5 the "for every K" bookkeeping sentence) |
| §3.2 open set → identity | **ACCEPT WITH FIXES** (S6 rationality for all k argued structurally; S7 denominators) |
| FI ⇔ Σ (§1), Theorem Σ | **ACCEPT** |
| Cor Σ.1 | **ACCEPT** |
| Cor Σ.2 | **ACCEPT WITH FIXES** (S8: meromorphy instead of "continuity"; 2e₁ numerics now exist, §D) |
| Remark C, §4 | **ACCEPT** (OBSTRUCTION labels appropriate) |
| Checks §5 | **ACCEPT** (re-run identical; SHI = 18 note below) |

## B. Re-derivations (what I checked, independently of the write-up's conclusions)

**B1. Gauge and residues (§2.1).** U_m := m^{pnσ₃}Y(zm^{−p}) is a constant left-conjugate of a rescaling of Y, so within each
row the residue relation of Y survives: Res_{X_k}(U_m)_{j2} = m^pw_k(U_m)_{j1}(X_k), X_k = (m/k)^p, and
U_mz^{−nσ₃} = m^{pnσ₃}(Yx^{−nσ₃})m^{−pnσ₃} = I + m^p(conj Y₁)/z + …, so 𝖻 = m^{2p}b_n² (Lemma invariance, constant k). With
Ũ = C U_m z^{γσ₃}C^{−1}: Ũ_{j1} = (c_j/c₁)U_{j1}z^γ, Ũ_{j2} = (c_j/c₂)U_{j2}z^{−γ}, so Res Ũ_{j2} = (c₁/c₂)X_k^{−2γ}m^pw_kŨ_{j1}(X_k)
= m^pk^{−(s−2pγ)}Ũ_{j1}(X_k). As analytic functions, w̃(z) = (c₁/c₂)z^{−2γ}w(z) on the slit plane (t_m^{−s̃} = m^{2pγ}z^{−2γ}t_m^{−s}),
hence W̃ = const·z^{−2γ}W and α̃ = (s̃−1)/p − 1 = α − 2γ. t_m(X_k) = k: the zeros of sin θ are exactly the nodes (no phantom node;
t ∈ −ℕ would need |arg z| = πp > π). Ũz^{−mσ₃} = C(U_mz^{−nσ₃})C^{−1} → I. All correct.

**B2. (−∞, 0) (g′).** Ũ₋^{−1}Ũ₊ = z₋^{−γσ₃}z₊^{γσ₃} = e^{2πiγσ₃}; g₊ − g₋ = 2πiμ*(ℝ) = 2πi so φ₊ − φ₋ = −2πi; F has no jump there
(app_outer L binetcut (iv) (O1): "F is analytic and zero-free off [0,∞)"; its proof does not use n ∈ ℤ; t ↦ t_m changes nothing).
V₋^{−1}V₊ = e^{(2πiγ − 2πim)σ₃} = e^{−2πinσ₃} = I. Correct; the integrality used is that of the degree only.

**B3. Lip phase and band limit (§2.2, item (b) of the brief).** Lemma signs (iii) (sec_5, read): φ = ∓iπ − 2f^{1/2} in
U(0,2δ₀) ∩ ℂ_±, f parameter-free; consistent with Im φ₊ = −π on (−∞,0) from ℂ₊ (Im g₊ = πμ*(ℝ)). Hence in ℂ₊
e^{2mφ} = e^{−2πim}e^{−4mf^{1/2}} = e^{−2πiγ}e^{−4ζ^{1/2}} (n ∈ ℤ), ζ = m²f. The Q-frame lip entry is D_{W̃}²·e^{2mφ}/W̃₀ =
ω^{(α̃)}e^{∓2πiγ}e^{−4ζ^{1/2}}. With ω^{(α̃)} → e^{∓iπα̃} (Paper 2 notation ϱ_±; G1u L1 (ii) for any real exponent),
ω♮ → e^{∓iπ(α−2γ+2γ)} = e^{∓iπα} = ϱ_±(α): the lip data of Φ_α ((eq:he-Phi-jumps)). So the comparison parametrix
P̂₀ = A₀(2πm)^{σ₃/2}Φ_α(m²f) ((eq:he-P0hat) with n ↦ m; it contains neither the weight nor (−1)^n) has the lip jumps ϱ_±e^{−4ζ^{1/2}},
and the mismatch with the true lips is G1u L3 with δ = −γ. **The Bessel order stays α.** I also checked G1u L1 (ii) under the
dictionary: ϱ_±ρ♮^{−2} = e^{∓iπα}e^{±iπα̃}ω^{(α̃)} = e^{∓2πiγ}ω^{(α̃)} = ω♮ exactly. The (−1)^n of (eq:he-ephi)/(eq:he-P0) lives only in
the V-frame P̃₀ and is not used in the Q-frame (sec_7: "Φ̂₀ contains neither D_W nor any other trace of the weight"). Sign control:
with e^{±2πiγ} the limit would be e^{∓iπ(α−4γ)}, which the C5-type control excludes (Rule A item 1) — confirmed.

**B4. Normalisation (Lemma normalisation, sec_6, read).** Its proof uses: equal 2πi jumps of g and Log z on (−∞,0); on
(n^p+δ′, ∞) the jump e^{2πinμ*((x,∞))} = e^{2iθ} of e^{n(g−Log z)} equals that of F; (O5) polynomial bound and boundedness on iℝ.
With m: e^{m(g−Log z)} has no jump on (−∞,0) for every real m; m·μ*((x,∞)) = mx^{−1/p} = t_m(x) so the jump is e^{2iθ}; (O5) with
m^p + δ′. In Ω_∞, V_m = C_∞e^{−mγ_pσ₃}(Ũz^{−mσ₃})(z^me^{mφ}F_m)^{σ₃}, z^me^{mφ}F_m = e^{mγ_p}/ϰ_∞: so 𝖻(Q₁) = 𝖻(Ũz^{−mσ₃}) = m^{2p}b_n².
Correct (Rule A item 8).

**B5. Row 2 (outer scalar).** t_m(y) = m|y|^{−1/p}e^{∓iπ/p} = t_n((n/m)^py), so 𝔟_m(y) = 𝔟_n((n/m)^py); substituting
y′ = (n/m)^py in (eq:B) gives B_m(z) = B_n((n/m)^pz)·exp(const) (the subtracted 1/(y−1) becomes 1/(y′−(n/m)^p), a z-independent
change). So F_m, H_m are Paper 2's with t_m; (O1)–(O5) are statements in t (proof of L binetcut uses |t₊| = n|y|^{−1/p} only as a
real scale). Correct.

**B6. Row 3 (a-priori bound).** Off the lens, columns of Q_m = (const diag)·[(U_m)_{·1}e^{mφ}F_mD_{W}·(z^γD_{x^{−2γ}}),
(U_m)_{·2}e^{−mφ}F_m^{−1}D_W^{−1}·(z^γD_{x^{−2γ}})^{−1}], D_{W̃} = D_W·D_{x^{−2γ}}·const, and z^γD_{x^{−2γ}} = z^γ(4cz/Υ)^{−γ} =
(Υ/4c)^γ times a unimodular constant in ℂ_±, bounded above and below near 0 (Υ(0) = −4c) — exactly G12 L2.3 with δ = −γ. **In the lens
the write-up's sentence is incomplete** (it describes only "columns of U_m times z^{±γ}(F_mD_{W̃})^{±1}"): there UM = R e^{mφσ₃}A_±F̃^{σ₃},
and the first column involves R_{·2}/W̃. I checked it: the m-frame lens matrix is built with W̃, and R̃_{j2} = Ũ_{j2} − Ũ_{j1}W̃e^{−2iθ}κ₊
= (c_j/c₂)z^{−γ}[U_{j2} − U_{j1}We^{−2iθ}κ₊] = (c_j/c₂)z^{−γ}R_{j2}, with R the lens transform of U_m with the s-weight W, to which
Paper 2 L lenssector applies (fixed n; its proof uses only Res(U_m)_{j2} = w(X_k)U_{j1}(X_k), the nodes at t_m ∈ ℕ and arcs with
t_m ∈ ℕ + ½). Then the first column is e^{mφ}z^γ(U_{·1} ∓ R_{·2}/W)·F̃_mD_{W̃}·const and the second z^{−γ}R_{·2}e^{−mφ}(F̃_mD_{W̃})^{−1}·const,
i.e. Paper 2's lens columns times (z^γD_{x^{−2γ}})^{±1}. Exponent |α|/2, L² margin (1+|α|)/4 < ½: correct. Fix S3 adds this.

**B7. Row 4 (G1u).** G1u's Q-frame inputs are: band J; lips ω♮e^{−4ζ^{1/2}}; none on (−∞,0); soft-edge data with ω^{(β′)} (no phase);
ρ♮ = ρ^{(α)}/G; F7 (row 3); (O3)–(O4) for the band factor (row 2/5). Under (n, δ, β′) ↦ (m, −γ, α̃) each holds (B3, B5, B6). n enters
G1u's Q-frame only via ζ = n²f, (2πn)^{σ₃/2}, and the n-uniformity statements on the fixed circle |z| = δ_r; all make sense for real m.
The Hurwitz-specific phases on Σ_v/Σ^△/saturated segment (θ_δ) are absent in the m-frame (θ = πt_m matches the nodes), which only
removes terms. **But** every G1u/G12/H-d statement is hypothesised for −1 < δ ≤ 0; for γ < 0 (δ > 0) the citations do not apply as
written (S1). (H-a's reason for excluding δ > 0 — a phantom node at t = δ — does not arise in the m-frame, so I expect γ < 0 to be
fine, but it is unreviewed and unnecessary.)

**B8. Row 5 (Hc / E3 F.1′).** E3 F.1′'s proof (read) uses n only through t₊ = n r^{−1/p}e^{−iπ/p} and Γ-integrals with real
aₙ = 2πin e^{−iπ/p}; valid for real m. Since H_m(z) = h(t_m(z))·const, the moments are μ_{m,k} = 2ζ(−kp)/(km^{kp}), the same
μ̂_k = 2ζ(−kp)/k in both frames. Correct.

**B9. Uniqueness (§3.1, item (c)).** Both expansions are of the same number n^pb_n/c along integers n ≥ n₀(γ) (the m-frame result
times (n/m)^p). In the m-frame, μ_m^β = μ̂^βn^{−|β|_wp}(n/m)^{|β|_wp}, and (n/m)^{(1+J)p}, m^{−k} are convergent series in integer powers
of 1/n: they never move a term between layers J; the remainder O(m^{−E}) = O(n^{−E}) for fixed γ (γ-uniformity is not needed: γ is
fixed, and the identity is extracted coefficientwise for each γ separately). For p ∉ ℚ, k + Jp are distinct, and only β = 0 produces
integer exponents. The comparison of finite sums with o(n^{−E}) remainder is elementary. Correct.

**B10. Open set → identity (§3.2).** R_k(p, α, γ) = Σ_i d_i(p, α−2γ, α)C(−i, k−i)γ^{k−i} − Σ_jC(p, j)γ^jd_{k−j}(p, α, α) — I re-derived
the two coefficient formulas ((n+γ)^{−i} = n^{−i}Σ C(−i, l)(γ/n)^l). It is rational in (p, α, γ) **provided d_k ∈ ℚ(p, β, ν) for every k**,
which the write-up cites from an engine run at KORD ≤ 4 (S6: the structural argument exists and should be written). The step itself
is fine modulo denominators (S7).

**B11. FI ⇔ Σ and Theorem Σ (item (d)).** (⇐): N′ = n + γ + (β−2γ+1)/2 = N. (⇒) and §3.2's construction: with γ = (ν−β)/2,
FI₀ at index n₀ = N − (ν+1)/2 gives B(N − (β+1)/2; β, ν) = ((N−(β+1)/2)/n₀)^pB(n₀; ν, ν); multiplying by (N/(N−(β+1)/2))^p gives
F_p(N; ν) := (N/n₀)^pB(n₀; ν, ν), visibly β-free; all substitutions are between formal series in 1/n₀, 1/m, 1/N that differ by
constant shifts. Infinitesimal form: d/dγ|₀ gives ∂_nB − 2∂_βB = (p/n)B. ν² claim: at fixed β, ν enters d_k only through the DLMF
a_k(ν), b_k(ν) (polynomials in ν²; in the engine Ξ_k uses only these), so F = (N/m)^pB(m; 0, ν) is a function of ν². Correct.

**B12. Cor Σ.1.** Theorem R in formal form is B(n; −β−2, ν) = B(−n; β, ν). With N′ = n − (β+1)/2, Σ gives
(n/N′)^pF(N′) = (n/N′)^pF(−N′) (the factor ((−n)/(−N′))^p = (n/N′)^p as formal series (1 + c/N′)^{±p}). So F is even. Correct.

**B13. Cor Σ.2 (item (e)).** μ̂₁ = 2ζ(−p) ≠ 0 on (1, 2) (no real zeros of ζ in (−2, −1)); μ̂₂ = ζ(−2p), μ̂₁² = 4ζ(−p)²; both weight-2
layers carry c(p)² (JZC_M4_proof §5, c-normalisation), and the remaining factors [X_{e₂}]_k, [X_{2e₁}]_k are rational in p for fixed
(α, γ) (gauge Taylor data rational, N.6d). If [X_{e₂}]_k ≢ 0 then ζ(−2p)/ζ(−p)² is a rational function R(p) on ℂ (identity of
meromorphic functions); it vanishes at every odd p ≥ 1 (ζ(−2p) = 0, ζ(−p) = −B_{p+1}/(p+1) ≠ 0, e.g. ζ(−1) = −1/12, ζ(−3) = 1/120),
so R ≡ 0, contradicting ζ(−2p) ≢ 0. Correct. The extension of the J = 2 relation from (1, 2)∖ℚ to (1, 2) must be by real-analyticity
(rational functions may have poles in (1, 2)), not "continuity" (S8).

## C. Fixes (exact text)

**S1 (MAJOR, scope of Lemma F (ii) and §3.1).** The REVIEWED inputs are stated for −1 < δ ≤ 0 (G1u L1 "Let p > 1, −1 < δ ≤ 0";
G12 P2.4 "Fix n ≥ n₀, p > 1, −1 < δ ≤ 0"; H-d scope), i.e. γ ≥ 0.
- In the table row "Lemma F (ii)" and in §2.1, replace "|γ| < (1 − |α|)/2" by "0 ≤ γ < (1 − |α|)/2 (γ = −δ with −1 < δ ≤ 0, the range
  of the cited H-d/G12/G1u statements; γ < 0 is expected to work — the H-a obstruction (phantom node) does not occur in the m-frame —
  but is not covered by any reviewed statement and is not used)".
- In (F)'s preamble ("Conclusion of Lemma F") replace "|γ| < (1 − |α|)/2" by "0 ≤ γ < (1 − |α|)/2".
- In §3.1 replace "γ ∈ (−¼, ¼)" by "γ ∈ (0, ¼)" and in §3.2 replace "((1, 2)∖ℚ) × (−½, ½) × (−¼, ¼)" by
  "((1, 2)∖ℚ) × (−½, ½) × (0, ¼)" (still an open set in (α, γ)); same in §3.3's last bullet.
- Rule A item 7: replace "|γ| < (1 − |α|)/2 keeps |α̃| < 1 … Only an open set is needed." by "0 ≤ γ < (1 − |α|)/2 keeps |α̃| < 1 and
  δ = −γ ∈ (−1, 0], the range of the cited H-d/G12/G1u statements. Only an open set is needed."
- §5, the sentence "At p = 1.7 and √2 (p > 1, inside Lemma F's range for γ ∈ {0.37, −0.21})": replace "for γ ∈ {0.37, −0.21}" by "for
  γ = 0.37 (γ = −0.21 tests the algebraic identity only)".

**S2 (MINOR, Lemma F (i), (g′)).** After "(F_m has no jump there, (O1))" add: "(app_outer L binetcut (iv), (O1): F = DBK is analytic
and zero-free off [0, ∞); D's jump e^{i𝔟} on (−∞, 0) is cancelled by B, and the proof uses n only as the real scale in t)".

**S3 (MINOR, row 3).** Append to the "transfer" cell: "In the lens, the m-frame lens factor is built with W̃ = const·z^{−2γ}W, and
R̃_{j2} = Ũ_{j2} − Ũ_{j1}W̃e^{−2iθ}κ₊ = (c_j/c₂)z^{−γ}R_{j2}, where R is the lens transform of U_m with W, to which Paper 2 L lenssector
applies at fixed n (nodes at t_m ∈ ℕ, arcs at t_m ∈ ℕ + ½). Hence the lens columns of Q_m are Paper 2's lens columns
(U_{·1} ∓ R_{·2}/W)e^{mφ}F̃_mD_W and R_{·2}e^{−mφ}(F̃_mD_W)^{−1} times (z^γD_{x^{−2γ}})^{±1}, and Prop apriori (i) holds with exponent |α|/2."

**S4 (MINOR, rows 2 and 5).** Row 2: replace "B_m(z) = const·B_n((n/m)^pz)" by "B_m(z) = B_n((n/m)^pz)·exp(c_{n,m}), c_{n,m}
independent of z (substitute y′ = (n/m)^py in (eq:B); 𝔟_m(y) = 𝔟_n((n/m)^py))". Row 5: replace "E3 F.1′'s proof treats n as a real
parameter" by "E3 F.1′'s proof uses n only through t₊ = nr^{−1/p}e^{−iπ/p} and the Γ-integral with a_n = 2πin e^{−iπ/p}, both valid
for real m > 0".

**S5 (MINOR, §3.1).** After "Both remainders are then o(n^{−E})" add: "(for fixed γ; the constants in (F) may depend on γ, which is
harmless since the coefficient identity is extracted separately for each γ)".

**S6 (MINOR, rationality of d_k for all k; §1 and Rule A item 6).** Replace "each d_k a rational function of (p, β, ν) (exact engine
m4_shift_exact.py over ℚ(p, ν, β))" by: "each d_k is a rational function of (p, β, ν), for every k: the residue recursion of N.6b–c and
the extraction are field operations on the Laurent data of the circle jumps; these data are rational in p once c = 1 (JZC_M4_proof N.6d),
polynomial in ν (the DLMF a_k(ν), b_k(ν), polynomials in ν²), and polynomial in β, because β enters only through
ρ² = (w/2 + (1 + w²/4)^{1/2})^{2(β+1)} and its soft-edge analogue, binomial series of 1 + (series with zero constant term) raised to
the power 2(β+1) (m4_rh_exact2 l. 218; m4_shift_exact.py computes the same over ℚ(p, α, β) to order 4)". Same sentence (shortened) in
Rule A item 6.

**S7 (MINOR, §3.2 denominators).** Replace "For fixed p there, R_k(p, ·, ·) is rational and vanishes on an open set, so it is 0; as a
function of p it is then a rational function vanishing on a dense subset of (1, 2), so R_k ≡ 0." by: "Write R_k = N_k/D_k with
N_k, D_k ∈ ℚ[p, α, γ], D_k ≢ 0. For all but finitely many p ∈ (1, 2)∖ℚ, D_k(p, ·, ·) ≢ 0, so N_k(p, ·, ·) vanishes on a non-empty open
subset of (α, γ) and is the zero polynomial; each coefficient of N_k as a polynomial in (α, γ) is then a polynomial in p with infinitely
many zeros, so N_k ≡ 0 and R_k ≡ 0."

**S8 (MINOR, Cor Σ.2).** In the J = 2 bullet replace "hence on (1, 2) by continuity in p (both [X]_k are rational in p after removing
the common factor c(p)²)" by "hence, both sides being real-analytic in p on (1, 2) off the finitely many poles of the rational factors
[X]_k (rational in p after removing the common factor c(p)²), on all of (1, 2) minus those poles". Add to §5: "The 2e₁ layer
(second order in μ₁) is checked numerically by Rule R reviewer A (REVIEW_JZC_SIGMA_A.md §D), not by this note's scripts."

**Label after fixes.** Lemma F (ii): "PROVED-mod-cite by transfer (0 ≤ γ < (1−|α|)/2) + REVIEWED (Rule R reviewer A)"; Prop FI,
Theorem Σ, Cor Σ.1, Cor Σ.2 (β ∈ {e₁, e₂, 2e₁}): PROVED-mod-cite + REVIEWED (reviewer A). Policy note: VERIFICATION_POLICY Rule R
requires "a human or a second independent agent"; if the repo's practice is two readers (A and B) before REVIEWED, as for the H chain,
keep "NOT REVIEWED (B pending)". Novelty stays UNCHECKED (§8; Rule L not done). Propagation (§7 item 4) is for the owners.

## D. Checks re-run and independent checks

Re-runs (python at the scratchpad venv, -B):
- `sigma_frame_exact.py` with the cache (SHI=18, KORD=4): output identical to the stored .out up to the timing line (diff empty).
- `sigma_frame_exact.py` **without** cache (copy of the checks dir under the scratchpad so that the cache path resolves there;
  repo cache untouched): fresh engine run 1526 s on the loaded machine; the d_k file it writes is byte-identical to the repo cache <repo>/tmp/sigma_cache/d_K4_SHI18_c5bf8bb1a9743a07.txt (cmp), all [1]–[5] and C1–C6 lines identical to sigma_frame_exact.out, and [1]–[4], C1–C6 identical to sigma_frame_exact_fresh.out; ALL IDENTITIES HOLD, ALL CONTROLS FAIL.
- `sigma_frame_num.py` (KORD=8, SHI=56): byte-identical to sigma_frame_num.out (diff empty), ALL 176 CHECKS PASSED.
- SHI = 18: the engine guard (assert on "truncation too shallow") passed in the fresh run, and [5] matches the SHI = 30 closed forms
  f₂, f₄ of m4_shift_exact.out; the cap does not affect the exact d₀..d₄.

Independent (rr_spot.py; m4_rh4 imported unchanged; points none of which the author used):
- **General base β ≠ ν** (the author checked this only exactly to order 4): FI B(n+γ; β−2γ, ν) = (1+γ/n)^pB(n; β, ν) at order 8 for
  p ∈ {2.3, e, 1.13}, ν ∈ {0.71, −0.12}, β ∈ {−0.8, 1.6}, γ ∈ {0.13, −0.61, 0.5} (γ = ½: lip phase e^{∓iπ} = −1): 36 points, FI residuals 9·10⁻³⁹–1.2·10⁻³⁴ (relative, dps 40; largest at γ = −0.61, p = e), max |f_odd| (k ≤ 7) ≤ 1.5·10⁻³⁷; controls half shift / no frame factor / Bessel order moved 0.04–32 at every point; ALL OK.
- **Second-order zeta layer 2e₁** (Cor Σ.2; untested by the author): second central differences in μ₁ (h = 10⁻¹⁴, dps 60, KORD 6),
  𝔇_{2e₁}(n+γ; ν−2γ, ν) = (1+γ/n)^{3p}𝔇_{2e₁}(n; ν, ν) at p ∈ {1.37, 2.6}, ν = 0.22, γ ∈ {0.19, −0.33}; control exponent 2p: residuals 1.0·10⁻¹³–3.2·10⁻¹³, at the noise floor of the second difference (the n⁻¹ coefficient of 𝔇_{2e₁}, exactly 0 by E3.7, comes out as 3·10⁻¹³–6·10⁻¹³); control with (1+γ/n)^{2p}: 0.11–0.29; ALL OK. (Two points per p; NUMERICAL, a check of the algebraic identity only.).
- **Order 10** (beyond every stored check, which stop at 8): FI₀ and f_odd = 0 (f₉ new) at (p, ν, γ) = (1.61, 0.27, 0.29),
  (2.9, −0.4, −0.17), KORD = 10, SHI = 72: FI₀ residual 6·10⁻³⁵ and 8·10⁻³³; |f₁|, |f₃|, |f₅|, |f₇|, |f₉| ≤ 1.0·10⁻³⁵ and ≤ 5.3·10⁻³⁴ (dps 40); ALL OK — f₉ = 0 and FI₀ at order 10 are new numerical evidence (Cor Σ.1 predicts both).

What these do and do not show (Rule X). All of them test the algebraic identity FI on the formal model (equivalent to Prop S at
the tested order); none tests Lemma F (ii), which is analysis. A direct lattice computation of b_n would test Theorem N.6 (already
REVIEWED, incl. an Arb lattice check in REVIEW_JZC_M4_proof_B) and FI's algebra, but cannot isolate Lemma F, because (F) at any finite
order is implied by N.6 + FI; I therefore did not repeat it. The evidence for Lemma F is the line-by-line transfer of §B.

## E. Rule A items of the note, reviewed
1 (prove too much) ✓; 2 (cancellation) ✓ (B2); 3 (γ = 1) ✓; 4 (equilibrium) ✓ — μ*, g, f, φ̃ are n-free (sec_5 (eq:g) remark),
the node density in z is m-free; 5 (uniqueness) ✓, p = 3/2 collision n^{−4} vs n^{−1−2p} correctly noted; 6 (rationality) — needs S6;
7 (range) — needs S1; 8 (constants) ✓ (B4); 9 (hidden n ∈ ℤ) — I repeated the search in sec_5–7, app_outer, app_c: the only uses are
jumpsV (g), (eq:he-ephi), (eq:he-P0) and the polynomial nature of U_{j1} (App C, holds: degree n); ✓; 10 (circularity) ✓.
