# Rule R review, reviewer B: JZC_W_exact Lemma WE.1 and JZC_W_kappa Prop K.12′ (the two last links of Conjecture W for the κ-family)

Reviewer: independent second reader (Rule R), reviewer **B**, 2026-10-22, branch plan-e2-d2 (HEAD 31386f6). I did not write any of the
target text, and I am not reviewer A (REVIEW_JZC_W_kappa_chain_A.md, whose fix text R1 is Prop K.12′).
- **Targets** (research/G1/RH/spectral/):
  1. JZC_W_exact.md **Lemma WE.1** (§1), checks `w_exact_gauge.py/.out`, `w_exact_laguerre.py/.out` (p = −1 anchor).
  2. JZC_W_kappa.md **Prop K.12′** (§4.3) and its use in P K.12; the assembled statement of "Conjecture W for λ_k = (k + δ)^p + κ at first
     order in the poles" in the JZC_W_kappa header, P K.12, and JZC_W.md header and §1.5.
- **Context read:** AGENTS.md, VERIFICATION_POLICY.md; JZC_W.md §1.3, §1.5; JZC_W_exact.md (all); JZC_W_kappa.md (all); JZC_W_BT.md §1,
  BT.1, Cor BT.4, BT.5, BT.6; REVIEW_JZC_W_kappa_chain_A.md; m3a_e37_decoupled.py (header, route 1) and its .out; w_exact_engine.py l. 245–275
  (the symbolic-j Taylor data); E3.md table rows E3.4, E3.7; JZC_M4_proof.md status/table (N.6a–c); RH/CITATIONS.md (DLMF-2).
- **Edits:** none, except this file. Re-runs wrote only to the scratchpad. My own scripts (no code shared with the repo or with reviewer A):
  `/tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/mineB/we1_cauchy.py` (+ `.out`) and `.../mineB/k12p_coef.py` (+ `.out`).
- **No claim about RH.** No measure here is built from zeta zeros.

## Overall verdict

| Item | Verdict |
|---|---|
| Lemma WE.1 (i)–(iii) | **ACCEPT WITH FIXES** (W1–W3, all MINOR: proof completeness for ρ ≥ 1 and for the Taylor-coefficient step; Rule C for duplication; stale docstring). No mathematical error. |
| Prop K.12′ (coarse form, refined form, η = 1, p = 2 note) | **ACCEPT WITH FIXES** (K1–K4, all MINOR: one precision fix to the refined remainder in the general statement, soft-edge sentence, half-integer reading of the refined layer, and the p = 2 note must not be read as proving W′). The exact leading coefficient pρW(ρ)/2 and η = 1 are correct. Every input is REVIEWED or is WE.1. |
| Assembly (theorem statement in JZC_W_kappa header/P K.12 and JZC_W header/§1.5) | **ACCEPT WITH FIXES** (A1–A2, MINOR: state the K needed; "p = 1/m" is vacuous for p > 1). No overclaim found. |
| Re-runs | all four scripts reproduce the stored outputs (identical apart from timing lines), §4. |

**Final status of the W theorem** (after W1–W3, K1–K4, A1–A2 are applied): Conjecture W for σ^{δ,κ} (λ_k = (k + δ)^p + κ, p > 1,
−1 < δ ≤ 0, κ ≠ 0, κ > −a^p, 1 < s < 1 + 2p) at first order in the poles, remainder O(n^{−2p}) in the refined form and O(n^{−1−p}) in W's
displayed form, is **PROVED-mod-cite + REVIEWED with every input REVIEWED** (WE.1 now REVIEWED by this review). Novelty stays UNCHECKED.
Not covered (unchanged): second order in the poles; p < 1; α ∉ (−1, 1); W′ (at p = 2 the W′ term lies at the order of the remainder, K4).

## 1. Lemma WE.1 (JZC_W_exact §1)

### 1.1 Re-derivation (from the write-up alone)

*Definition and normalisation.* M_ρ := z^ρ/R − 2C_ρ, R = z^{½}(z−4)^{½} (principal roots; ~ z at ∞; cuts combine to [0, 4]),
C_ρ(z) = (1/2πi)∫_0^4 x^ρ dx/(R₊(x)(x − z)), R₊ = i√(x(4−x)). Then g := z^ρ − RM_ρ = 2RC_ρ is analytic off [0, 4], O(1) at ∞, and
(g/R)₊ − (g/R)₋ = (g₊ + g₋)/R₊ gives g₊ + g₋ = 2x^ρ on the band, as BT.1 uses. For integer j, z^j/R − Q_j is O(1/z), analytic off [0, 4] with the
same jump, so M_j = Q_j (I checked M₀ = 0, M₁ = 1, M₂ = z + 2, M₃ = z² + 2z + 6 numerically, §3.1).

*Stieltjes form.* On (−∞, 0), R is real and continuous (R = −√(y(y+4)) at x = −y), so the jump of M_ρ is that of z^ρ/R:
(z^ρ/R)₊ − (z^ρ/R)₋ = −2i sin(πρ)|x|^{ρ−½}(4 − x)^{−½}. For −½ < ρ < 1, M_ρ → 0 at ∞ and has an integrable singularity at 0, so it is the
Cauchy transform of this jump; with x = −s this is (sin πρ/π)∫_0^∞ s^{ρ−½}(s+4)^{−½}(s+z)^{−1}ds. Correct, including the sign.

*(i).* [w^m]M_ρ(4+w) = (−1)^m(sin πρ/π)∫_0^∞ s^{ρ−½}(s+4)^{−m−3/2}ds = (−1)^m(sin πρ/π)4^{ρ−m−1}B(ρ+½, m+1−ρ) (DLMF 5.12.3, Re > 0 for
−½ < ρ < 1). At m = 0, with 5.5.3: 4^{ρ−1}·2Γ(ρ+½)/(√πΓ(ρ)) = 4^ρΓ(ρ+½)/(2√πΓ(ρ)) = C(2ρ,ρ)ρ/2 (the last step is Legendre duplication).
This is the stated formula at m = 0; the general m follows the same way (the sympy identities [1] check it for m ≤ 8, symbolic ρ).

*(ii).* Jump of z^{ρ−½} on (−4, 0): 2i sin(π(ρ−½))|x|^{ρ−½} = −2i cos(πρ)|x|^{ρ−½}. So F := M_ρ − tan(πρ)z^{ρ−½}(4−z)^{−½} has no jump on (−4, 0),
is analytic in 0 < |z| < 4, and is O(|z|^{ρ−½} + |log z|) = o(1/|z|) at 0 for ρ > −½: the singularity is removable. **This gives (ii)'s
analyticity directly, for every ρ > −½, ρ ∉ ½ + ℤ**, without the Mellin argument of the write-up ("The remainder M_ρ − A_ρ is z^{ρ−½}φ(z)
with φ analytic" is asserted there, not proved; fix W1). m = 0 coefficient: (sin πρ/π)4^{ρ−1}B(ρ−½, 1−ρ) = 4^{ρ−1}Γ(ρ−½)/(√πΓ(ρ)), and
C(2ρ,ρ)ρ/(2(2ρ−1)) = 4^ρΓ(ρ+½)/(√πΓ(ρ))/(4(ρ−½)) is the same. Correct.

*(iii).* In ℂ₊, z − 4 = (4 − z)e^{iπ} with arg(4 − z) ∈ (−π, 0), so (z−4)^{½} = i(4−z)^{½}; in ℂ₋, −i. Hence
R·tan(πρ)z^{ρ−½}(4−z)^{−½} = ±i tan(πρ)z^ρ, sign = sign Im z. Correct.

*Range in ρ.* The write-up proves (i) and the Taylor data in (ii) via the Stieltjes form, valid for −½ < ρ < 1, and says "(continued in ρ
beyond)". The κ-family needs WE.1 at q_m = m − 1/p for m ≤ M = J + 1, i.e. at least at q₂ ∈ (1, 2) (L K.10 needs M ≥ 2). The continuation is
valid: for fixed z, M_ρ(z) (definition above, ρ > −½) and the Taylor coefficients at 4 are analytic in ρ; the RHS of (i) is entire in ρ;
the coefficients of F at 0 are analytic in ρ off ½ + ℤ, and the RHS of (ii) is meromorphic with poles only there. Identity theorem in ρ.
But this is one sentence that the write-up does not contain (fix W1), and the author's numerical checks use only ρ ∈ {0.3, −0.2, 2/3, 0.9}
(all < 1; the Stieltjes quadrature in w_exact_gauge.py cannot go beyond ρ < 1). Reviewer A checked ρ = 4/3; I checked ρ ∈ {1.6, 5/3, 2.3}
(§3.1). With W1 the range is proved and checked.

*Engine identification.* w_exact_engine.py l. 249–263 uses exactly the stated rational data at 0 and at 4 for symbolic j, inside the full
cosh/sinh gauge h = RM/2 (dual numbers to order EO). I verified independently (sympy, §3.1) that for integer j ≤ 8 and m ≤ 9 these
formulas are the Taylor data of Q_j/C(2j, j), and numerically that at non-integer ρ they are the data of A_ρ/C(2ρ,ρ) at 0 and of
M_ρ/C(2ρ,ρ) at 4. So "the engine run with symbolic j and then j = ρ is exactly the gauge built from A_ρ at the hard edge and M_ρ at the soft
edge" holds. The engine needs only Taylor data because cosh h and sinh(h)/R are functions of h² = R²M²/4 and of M, both analytic.

### 1.2 Verdict on WE.1: ACCEPT WITH FIXES

The mathematics is right. The label "PROVED (elementary)" is justified once W1–W2 are applied.

## 2. Prop K.12′ (JZC_W_kappa §4.3)

### 2.1 Re-derivation

*(a) Gauge form.* I recomputed BT_coh's hard-edge factor from its definition, not from BT.5. The coherent W̃_BT carries
exp((πσ/(2 sin πρ))(−z/n^p)^ρ). With πσ = τ tan πρ this is exp(τ(−z)^ρ/(2cos πρ)) (n^p scaling suppressed) = exp((τ/2)z^ρ(1 ∓ i tan πρ)) in ℂ_±.
The band tilt h = e^{τz^ρ} = e^{−μz^ρ} (μ = −τ) has log D_h = −(μ/2)(z^ρ − RM_ρ) = (τ/2)(z^ρ − RM_ρ). So
  log ρ_h = (τ/2)z^ρ(1 ∓ i tan πρ) − (τ/2)(z^ρ − RM_ρ) = (τ/2)(RM_ρ ∓ i tan(πρ)z^ρ) = (τ/2)RA_ρ = −(μ/2)RA_ρ
by WE.1(iii). The signs match: WE.1(iii) has +i in ℂ₊, and the coherent W̃ has −i in ℂ₊. So ρ_BT = ρ_mod·e^{−μRA_ρ/2}·(Toda gauge) exactly.
I also checked the lip convention: W̃_BT² = W₀^{BT}e^{∓iπβ}e^{∓iπσz^ρ}, so ϱ_±ρ_BT^{−2} = e^{±iπ(β−ν)}e^{±iπσz^ρ}D²/W₀^{BT}, as in the BT_coh
definition. Diagonal factors commute, so Δ_k^{BT} = G_aΔ_k^{mod}G_a^{−1} at the hard edge.
- *Soft edge* (not written in (a); fix K2): the lips avoid U(4c, h₀), so only h enters there. h is analytic at 4c and D_h²/h = e^{μRM_ρ}
  globally (BT.1 preamble), so E3 Lemma E3.4's argument gives Δ^{r,BT} = G(M_ρ)Δ^{r,mod}G(M_ρ)^{−1} locally. That is the "Taylor data at 4c
  (M_ρ)" of (a).

*(b) Entire dependence.* G = cosh h·I + (sinh h/R)·RN, h linear in the times, and the hard-edge and soft-edge functions A_ρ and M_ρ are
analytic on the respective discs. So the Laurent coefficients of Δ_k^{BT} are entire in the times with n-free coefficients. The residue
recursion and the extraction (√ of (Q₁)₁₂(Q₁)₂₁, leading term c² time-free) are polynomial in these, so each b_k(times) is entire. N.6b
(REVIEWED) states this for polynomial tilts; the same argument covers A_ρ and M_ρ. Correct.

*(c) The n⁻¹ order.* m3a_e37_decoupled route 1 (REVIEWED; re-run, §4) asserts e(M) − e(0) = cpM(4c) **with M(0), M(4c), M′(4c) independent
symbols** (out: "M4p, M0 drop out"; control "cpM(0)" fails). That independence is what makes it applicable here, where the hard-edge
function is A_ρ and the soft-edge function is M_ρ ≠ A_ρ. Only G(0) (a function of A(0)) and G, G′ at 4c enter Res Δ₁. So the n⁻¹
coefficient is exactly linear in all times, with no products, and the ρ-part is cpμ_ρM_ρ^{(c)}(4c).
*c-scaling:* M_ρ^{(c)}(z) = c^{ρ−1}M_ρ^{(1)}(z/c), and M_ρ^{(1)}(4) = C(2ρ,ρ)ρ/2 (WE.1(i), m = 0). So cpM^{(c)}(4c) = pρc^ρC(2ρ,ρ)/2 = pρW(ρ)/2.
**Duplication is not needed for K.12′:** the Beta value 4^ρΓ(ρ+½)/(2√πΓ(ρ)) gives pρ(4c)^ρΓ(ρ+½)/(2√πΓ(ρ+1)) = pρW(ρ)/2 with W in JZC_W's own
Γ-form. With μ_ρ = −τ_ρn^{−pρ}, the term is −(pρW(ρ)/2)τ_ρn^{−1−pρ}. **The exact leading coefficient is confirmed.**

*(d), (e), η.*
- Orders n^{−k}, k ≥ 2: first order O(n^{−2−pρ}); second order O(n^{−2−2p·min𝓡}).
- At n⁰ the times do not enter, since Δ_k starts at k = 1.
- (n/N)^pN^{−1−pρ} − n^{−1−pρ} = O(n^{−2−pρ}).
- So 𝔅^{rec} = 𝔅[M; μ_n] − Σ(pρW/2)τ_ρ(n/N)^pN^{−1−pρ} + O(n^{−2−p·min𝓡}), i.e. BT_coh with **η = 1**. Correct.

*Refined form, precision (fix K1).* "First-order part in (τ_ρ) = Σ_ρ engine layer at j = ρ" is exact if the layer is taken around
M(β, ν; μ_n), i.e. with the Toda times on. If the layer is the one around μ_n = 0, which is how JZC_W and the theorem use "the continued
symbolic-j layer", then the mixed terms τ_ρμ_{n,j} are missing. Each b_k is entire, so ∂_{μ_ρ}b_k(μ_n) − ∂_{μ_ρ}b_k(0) = O(n^{−p}). These
terms are O(n^{−2−p−pρ}) (zero at n⁻¹ by route 1).
- Against the stated remainder O(n^{−2−2p·min𝓡}), they are smaller iff min𝓡 ≤ 1.
- For the κ-family min𝓡 = q₁ = 1 − 1/p < 1, so the mixed terms are O(n^{−1−2p}) ⊂ O(n^{−2p}), and **the theorem is unaffected**.
- As a general statement, K.12′'s refined remainder needs "+ O(n^{−2−p−p·min𝓡})" or the "around M(β, ν; μ_n)" reading.

*Half-integer ρ (fix K3).* For ρ ∈ ½ + ℤ, τ_ρ = 0 and A_ρ has a pole, so "the layer at j = ρ with μ = −τ_ρn^{−pρ}" is 0·∞. The right reading
is the limit ρ′ → ρ at fixed σ_ρ. This limit is legitimate:
- τ(ρ′)M_{ρ′}(4) → 0, D_h → 1, and −(μ/2)RA_{ρ′} = (πσ/(2 sin πρ′))(−z)^{ρ′} − (τ/2)(z^{ρ′} − RM_{ρ′}) → (πσ/(2 sin πρ))(−z)^ρ, locally
  uniformly in U_0;
- the layer is polynomial in the Taylor data, so it converges.

At ρ = q₁ = ½ (p = 2) route 1 applies directly with soft-edge M = 0 and gives a zero n⁻¹ shift (pole term 0, cot = 0).

*p = 2 note (fix K4).* The note is correct: data exp(C(−z/n^p)^q), engine form, pole terms vanish, W′ at n^{−4} inside the coarse remainder
O(n^{−3}). Its last clause ("in the refined form it is part of the continued first-order layer") is true but proves nothing about W′.
- At p = 2 the refined remainder is O(n^{−2p}) = O(n^{−4}).
- The second-order terms in a₁ enter at n^{−2−2pq₁} = n^{−4}, the same order as W′.
- So W′ is not established at p = 2 (nor at any p: q₁ = ½ only at p = 2).
- JZC_W §1.5 correctly lists W′ as not covered; the K.12′ note should say so too.

### 2.2 Inputs of K.12′ and their status

| Input | Status |
|---|---|
| JZC_W_BT BT.1(iii), BT.5 | REVIEWED (review A; fixes B7, B8 applied: BT.1(iii) exact, BT.5 via exp(C(−z)^q)) |
| JZC_W_exact WE.1 (i)–(iii) | **REVIEWED by this review** (ACCEPT WITH FIXES W1–W3) |
| m3a_e37_decoupled route 1 | REVIEWED (REVIEW_JZC_M3a_H_assembly_B.md); re-run identical |
| JZC_M4_proof N.6b, N.6c, Theorem N.6 | REVIEWED |
| E3 Lemma E3.4 (gauge form; used for the soft edge, K2) | REVIEWED (E3.md, Plan E3 A/B) |
| BT_coh definition, L K.9 (meromorphy), L K.10, P K.8 | REVIEWED (review A) |
| DLMF 5.12.3, 5.5.3 | quoted in RH/CITATIONS.md (DLMF-2); hypotheses Re a, Re b > 0 hold for −½ < ρ < 1 (beyond: by continuation, W1) |
| Legendre duplication (C(2ρ,ρ) = 4^ρΓ(ρ+½)/(√πΓ(ρ+1))) | **not quoted** in any CITATIONS file. Needed only for WE.1's C(2ρ,ρ) normalisation and the identification with the engine's C(2j, j)-normalised data, not for K.12′(c) (see above). Fix W2. |

Nothing NOT REVIEWED remains once WE.1 is accepted.

### 2.3 Verdict on K.12′: ACCEPT WITH FIXES

## 3. Independent spot checks

### 3.1 WE.1 by an independent construction (`mineB/we1_cauchy.py`, dps 30; 46 checks, ALL PASS)

M_ρ is built from its **definition** (Cauchy transform C_ρ by quadrature after x = 4sin²t, with the substitution t = v^{1/(1+2ρ)} for
ρ < 0). Taylor coefficients are taken by trapezoidal **Cauchy integrals** on circles |z| = 1 and |z − 4| = 1, with 96 offset nodes. The
method shares nothing with the author's (Stieltjes form + Beta + tanh-sinh) or reviewer A's (pointwise comparison) checks. ρ values used by
neither: 0.15, 0.45, −0.35, 1.6, 5/3, 2.3 (three of them > 1).

| Check | Result |
|---|---|
| normalisation M_j = Q_j, j = 0…3 | ≤ 1.3·10⁻²⁹ |
| (i) [w^m]M_ρ(4+w), m ≤ 5 | relative ≤ 1.6·10⁻²⁶ |
| (ii) analyticity: c₋₁, c₋₂ of F at 0 | ≤ 3·10⁻³¹ (no jump left, i.e. tan is right) |
| (ii) [z^m]A_ρ, m ≤ 5 | relative ≤ 3.8·10⁻²⁸ |
| (iii) R(M_ρ − A_ρ) = (sign Im z)·i tan(πρ)z^ρ, 6 points incl. both sides of the negative axis and of the band | relative ≤ 1.3·10⁻²⁸ |

Controls, all failing as required:
- (½)_m for (½)_{m+1}: off by 4.5;
- sin for tan: off by 5–173;
- the opposite sign in (iii): off by 2.0.

Rule A note: my first run at ρ = −0.35 gave deviations of about 10⁻¹⁰ from the t^{2ρ} endpoint singularity of the plain quadrature, not
from the lemma. The substitution removed them (≤ 3·10⁻²⁸). Integer-ρ engine data: sympy, for integer j ≤ 8 and m ≤ 9 the engine's
symbolic-j formulas equal the Taylor data of Q_j/C(2j, j): True.

### 3.2 K.12′'s coefficient against the κ-measures (`mineB/k12p_coef.py`)

From K.12′(c) alone:
- coefficient = cp·μ·c^{ρ−1}M_ρ^{(1)}(4) with μ = −τ_m, τ_m = 2π cot(πq_m)a_m, a_m = −binom(1/p, m)(−κ)^m;
- M_ρ^{(1)}(4) taken by quadrature of the definition (mean value on |z − 4| = ½), not from the closed form.

| Measure | term | K.12′ (quadrature) | closed form −(pqW/2)τ | W prediction (w_outer_e2e) | measure fit (w_outer_e2e) |
|---|---|---|---|---|---|
| KO1 p = 2.5, δ = −0.3, κ = 0.3 | n^{−2.5} | 0.197044104833 | 0.197044104833 | 0.1970441048 | 0.197043934 (half-range 1.3·10⁻⁵) |
| KO2 κ = −0.3 | n^{−2.5} | −0.197044104833 | same | −0.1970441048 | −0.197043709 (6.8·10⁻⁶) |
| KO3 p = 1.5, δ = −0.4, κ = 0.4 | n^{−1.5} | −0.22650893724 | same | −0.2265089372 | −0.226508433 (3.3·10⁻⁵) |
| KO3, m = 2 (q₂ = 4/3) | n^{−3} | −0.0855104977495 | same | −0.08551049775 | (at the O(n^{−2p}) remainder order; not separately fitted) |

The natural-index shift −(1 + pq + p)(β′+1)/2 × coefficient reproduces the stored "pole-shift" values: 0.09852205242 for KO1/KO2 and
0.06795268117 for KO3. Measure fits agree with K.12′ to 1.7·10⁻⁷ … 5·10⁻⁷, well inside the fit half-ranges. Sign and normalisation of
K.12′(c) are confirmed on true measures (NUMERICAL).

## 4. Re-runs (session venv, -B, outputs in the scratchpad; diff against the stored .out after removing timing fields)

| Script | Result | vs stored .out |
|---|---|---|
| w_exact_gauge | ALL 14 PASSED | identical (sha lines identical) |
| w_exact_laguerre | ALL 24 PASSED | identical except the engine timing line (144 s vs 287 s) |
| w_kappa_transfer | ALL 43 PASSED | identical |
| m3a_e37_decoupled | ALL 36 PASSED | identical |

The w_exact_laguerre anchor (p = −1): the engine's symbolic-j response at j = ρ equals the analytic part of the exact Laguerre response
through N⁻⁶, and g1[1] = −ρ/2 = pρ/2 at p = −1. This is consistent with K.12′(c)'s coefficient at the one p where an independent classical
computation exists.

## 5. Assembly: does the theorem follow, without overclaim?

Chain:
1. P K.12: n^pb_n/c = 𝔅^{rec}[BT_coh(α+2δ, α; μ^κ_n, (2a_m)_{m≤M})] + O(n^{−K−1} + n^{−1−(J+1)p}).
2. K.12′ (refined), with min𝓡 = q₁ = 1 − 1/p: 𝔅[M(α+2δ, α); μ^κ_n] + Σ_m layer_m + O(n^{−2−2pq₁}) = … + O(n^{−2p}). The mixed Toda×pole terms
   are O(n^{−1−2p}) (K1) and the Toda truncation is O(n^{−1−(J+1)p}) ⊂ O(n^{−1−2p}) (J ≥ 1). This needs K ≥ 2p − 1 (fix A1).
3. Pole coefficients: −(pqW/2)τ_m with τ_m = 2π cot(πq_m)a_m and a_m = −R_{q_m}/q_m (P W-out.7) gives pR_qW(q)π cot(πq). Checked (§3.2).
4. Displayed form: the coarse K.12′ remainder O(n^{−2−pq₁}) = O(n^{−1−p}) exactly. For p > 1, the m = 2 pole term n^{−1−pq₂} = n^{−2p} and the
   Toda layer t₁ at n^{−1−p} lie in that remainder. The integer coefficients n^{−k}, k < 1 + p, are those of M(α + 2δ, α) (P K.11; κ-free
   β′). Requires K ≥ p.
5. W's own registered claim (JZC_W §1.3: "each pole term to relative O(N⁻²)") is stronger than the displayed form proved here
   ((1 + O(N⁻¹))). The refined form contains it to the extent the engine layer has no relative N⁻¹ term, which is not claimed as part of the
   theorem. The theorem states (1 + O(N⁻¹)) and no more: **no overclaim**.

Hypotheses:
- p > 1, −1 < δ ≤ 0 (Theorem H/G12 frame), κ ≠ 0, κ > −a^p (λ₁ > 0), 1 < s < 1 + 2p (|α| < 1, the G12/G1u frame).
- 1/p ∉ ℤ is automatic for p > 1, as L K.1 needs. "p ≠ 1/m" in the "not covered" lists is vacuous under p > 1 (fix A2).
- p = 2 (all q_m half-integer) is included, via BT.5 (B7) and K3.

JZC_W.md header and §1.5 match P K.12. §1.5's "k < p" is weaker than K.12's "k < 1 + p apart from the pole term"; both are correct. Both
list second order, p < 1, α ∉ (−1, 1), non-coherent tilts and W′ as not covered. The only stale text is the "one unreviewed input (WE.1)"
clauses, to be updated when the fixes are applied.

## 6. Fixes

**W1 (MINOR, proof completeness; JZC_W_exact WE.1 proof).** Replace the sentence "The remainder M_ρ − A_ρ is z^{ρ−½}φ(z) with φ analytic; its
jump … so φ = tan(πρ)(4−z)^{−½}" by:
> "Put F := M_ρ − tan(πρ)z^{ρ−½}(4−z)^{−½}. On (−4, 0) the jump of z^ρ/R is −2i sin(πρ)|x|^{ρ−½}(4−x)^{−½} and that of z^{ρ−½} is
> −2i cos(πρ)|x|^{ρ−½}, so F has no jump there; F is analytic in 0 < |z| < 4 and O(|z|^{ρ−½} + |log z|) = o(1/|z|) at 0 (ρ > −½), hence
> analytic at 0. A_ρ := F. Its Taylor coefficients for −½ < ρ < 1: split the Stieltjes integral at s = 1; ∫_1^∞ is analytic in |z| < 1, and
> ∫_0^1 termwise with (s+4)^{−½} = Σh_ks^k gives the singular part tan(πρ)z^{ρ−½}(4−z)^{−½} plus an analytic part. Together the coefficients
> are the Mellin-continued moments (−1)^m(sin πρ/π)4^{ρ−m−1}B(ρ−½−m, m+1−ρ)."

And add after the proof:
> "*Range.* For fixed z, M_ρ(z) (defined for ρ > −½ by z^ρ/R − 2C_ρ) and its Taylor coefficients at 4 and those of F at 0 are analytic in
> ρ, and the right-hand sides of (i), (ii) are meromorphic with poles only at ½ + ℤ (in (ii)). So (i) holds for all ρ > −½, and (ii), (iii)
> for all ρ > −½, ρ ∉ ½ + ℤ (identity theorem in ρ). The κ-family uses ρ = q_m = m − 1/p, m ≤ M, including q₂ ∈ (1, 2)."

Add to "Checks": "ρ > 1: Rule R review B, Cauchy-integral check at ρ ∈ {1.6, 5/3, 2.3} (and 0.15, 0.45, −0.35), relative ≤ 1.6·10⁻²⁶; review
A at 4/3."

**W2 (MINOR, Rule C; WE.1 proof and RH/CITATIONS.md).** Legendre duplication (DLMF 5.5.5) is used to pass from the Beta values to
C(2ρ,ρ) = Γ(2ρ+1)/Γ(ρ+1)², and it is not quoted in any CITATIONS file. Either quote DLMF 5.5.5 with its hypothesis into (DLMF-2) (here
2z = 2ρ+1 ∉ −ℕ₀), or state WE.1 with the prefactor 4^ρΓ(ρ+½)/(√πΓ(ρ+1)) = W(ρ)/c^ρ. Also cite 5.12.3 and 5.5.3 (already in (DLMF-2))
explicitly in WE.1's proof. K.12′(c) is unaffected (§2.1).

**W3 (TRIVIAL, reproducibility; w_exact_gauge.py docstring l. 14).** "mpmath quad, 30 digits" → "40 digits" (the code sets dps 40; the
write-up and .out say 40). Also note there that the quadrature checks use the Stieltjes form and are therefore limited to ρ < 1.

**K1 (MINOR, precision; JZC_W_kappa Prop K.12′ statement, refined form).** After "to all orders in 1/n", insert:
> "(the layer taken around M(β, ν; μ_n); if it is taken around μ_n = 0, as in JZC_W, add the mixed Toda × branched terms
> O(n^{−2−p−p·min𝓡}), which vanish at n⁻¹ by (c) and are O(n^{−1−2p}) ⊂ O(n^{−2p}) for the κ-family, min𝓡 = q₁ < 1)".

**K2 (MINOR, completeness; K.12′ proof (a)).** Add:
> "At the soft edge only the band tilt enters (the lips avoid U(4c, h₀)); h is analytic at 4c and D_h²/h = e^{μRM_ρ}, so E3 Lemma E3.4's
> argument gives Δ^{r,BT} = G(M_ρ)Δ^{r,mod}G(M_ρ)^{−1} there. Route 1 treats M(0) = A_ρ(0) and M(4c) = M_ρ(4c) as independent symbols,
> so A_ρ ≠ M_ρ is harmless."

**K3 (MINOR, definition; K.12′ refined form).** Add:
> "For ρ ∈ ½ + ℤ (τ_ρ = 0) the layer is the limit ρ′ → ρ at fixed σ_ρ. The gauge data −(μ/2)RA_{ρ′} converge to
> (πσ/(2 sin πρ))(−z)^ρ and μM_{ρ′}(4c) → 0, and the layer is polynomial in these data."

**K4 (MINOR, scope; K.12′ p = 2 note).** Replace the last clause by:
> "… lies inside the coarse remainder O(n^{−3}). In the refined form it belongs to the first-order layer (JZC_W_exact: exact limit), but at
> p = 2 the refined remainder is O(n^{−2p}) = O(n^{−4}): second-order terms in a₁ enter at n^{−2−2pq₁} = n^{−4} too. So K.12′ does not
> establish W′ (W′ stays a CONJECTURE)."

**A1 (MINOR, explicitness; JZC_W_kappa P K.12 statement).** Add "with K ≥ 2p − 1 for the refined form and K ≥ p for W's displayed form"
(J ≥ 1, M = J + 1 suffice for both).

**A2 (TRIVIAL; JZC_W_kappa header "not covered", JZC_W §1.5).** "p = 1/m" is vacuous for p > 1. Write "(p = 1/m < 1 belongs to the p < 1
case)", or drop it from the p > 1 list.

Status updates when applying:
- JZC_W_exact header and table row WE.1 → "PROVED + REVIEWED (Rule R reviewer B, research/G1/review/REVIEW_JZC_W_WE1_K12p_B.md)". WE.2–WE.6
  were not reviewed here and keep their labels.
- JZC_W_kappa header, table rows P K.12 and Prop K.12′, §4.3 "Consequently" paragraph, §9 item 2: remove "single unreviewed input WE.1".
- JZC_W.md header and §1.5: likewise.
- JZC_W_BT BT.5 label clause: unchanged (it already cites K.12′).

## 7. Rule A (reviewer's adversarial attempts)

1. *Sign of (iii) vs the coherent lip phase.* Both computed by hand (§2.1). The opposite sign would leave e^{∓iτ tan(πρ)z^ρ}, a non-meromorphic
   remainder; my (iii) control (opposite sign) fails by 2.0.
2. *Does route 1 really allow A_ρ ≠ M_ρ?* Yes: M0, M4, M4p are independent symbols and M0 drops out (stored and re-run .out). If route 1 had
   used a single polynomial M, K.12′(c) would need a new computation.
3. *Second order at n⁻¹?* Excluded by route 1 (all orders). The naive count τ₁² n^{1−2p} would exceed n^{−1−p} for p < 2.
4. *ρ > 1.* Needed (q₂ ∈ (1, 2) enters BT_coh since M ≥ 2). Not covered by the author's Stieltjes-form proof or checks; covered by W1 and
   §3.1.
5. *Half-integers / p = 2.* Limit argument verified (K3). The W′ term is not proved (K4); JZC_W §1.5 already says so.
6. *Mixed Toda × branched terms.* Found the K1 imprecision. Harmless for the κ-family (n^{−1−2p} vs n^{−2p}), and I checked the exponent
   arithmetic at p ∈ (1, 2) and p > 2.
7. *Coefficient on true measures.* K.12′'s formula vs fitted κ-measures at both signs of κ and two p (§3.2): agreement within fit error;
   the stored control "no pole term" misses by 2259–9722 tolerances.
8. *Independence.* we1_cauchy.py and k12p_coef.py use the definition of M_ρ via its Cauchy transform and contour integrals. They use none of
   the Stieltjes form, the Beta closed forms, the engine, or reviewer A's we1.py.

No RETRACTED item. No stop condition hit.
