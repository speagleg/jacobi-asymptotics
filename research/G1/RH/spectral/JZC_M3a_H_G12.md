# JZC M3a, gaps G1–G2 (p > 1): the Hurwitz outer scalar at ∞, and the a-priori bound at the hard edge

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_M3a_H_G12_A.md); fixes applied 2026-10-21.

Rule R review B: ACCEPT (research/G1/review/REVIEW_JZC_M3a_H_assembly_B.md §A); fixes A-1, A-2 applied 2026-10-22.

Status (2026-10-22): PROVED-mod-cite + **REVIEWED** (Rule R: review A re-derived and spot-checked; review B
(research/G1/review/REVIEW_JZC_M3a_H_assembly_B.md §A) re-derived L1.1, L1.2, C1.5, L2.1, L2.3, P2.4 and re-ran both checks with
identical output) (fixed per Rule R review B, A-2). The table labels below are unchanged; each carries REVIEWED. Labels per
VERIFICATION_POLICY.md. Closes JZC_M3a_Hd.md §7 G1 and G2 for
p > 1, −1 < δ ≤ 0. Checks: `checks/m3a_g12_outer.py/.out`, `checks/m3a_g12_apriori.py/.out` (spec_common.Checks: 58 and 67 assertions, all pass).
Everything attributed to Paper 2 is quoted from papers/paper2/{sec_5,sec_6,app_outer,app_c}.tex as read for this note.

| # | Statement | Label |
|---|---|---|
| L1.1 | j_δ(t) = j(t−δ) + (t−δ−½)Log(1−δ/t) + δ | PROVED |
| L1.2 | bounds for j_δ: |t j_δ| ≤ C_J for |t| ≥ 2; expansion at t → 0 | PROVED-mod-cite (Paper 2 (eq:binet-bound)) |
| L1.3 | binetcut (i)–(iii) for δ: 𝔟_δ, its limit 𝔟_∞(δ), B_δ | PROVED-mod-cite (as L1.2) |
| P1.4 | F_δ := D_δB_δK satisfies (O1_δ), (O2)–(O4), (O5) at 0; F♮ := F_δ(−z)^{−δ} satisfies (O1) and (O5) at ∞ | PROVED-mod-cite (as L1.2) |
| C1.5 | F♮ → C_δ ∈ (0, ∞) uniformly as z → ∞ (H-d Prop 2.1); closed form of log C_δ | PROVED-mod-cite (+ DLMF 5.5.3 via Paper 2) + NUMERICAL |
| L2.1 | sum bound for the Hurwitz U, explicit constants, exponent α (no δ-shift) | PROVED + NUMERICAL |
| L2.2 | lens-sector bound for the Hurwitz R | PROVED (Paper 2 L lenssector, modified) |
| L2.3 | column factorisation: Q♮ sees F♮ only through F♮D_W, and |F♮D_W| = |F_δD_W^{(α)}|·|4c/Υ|^δ | PROVED-mod-cite (Paper 2 L szego (i)) + NUMERICAL |
| P2.4 | Prop apriori for Q♮: |Q♮| ≤ C_{n,η,δ}|z|^{−|α|/2−η}; Cor L2 (Q♮_± ∈ I + ∂𝒞(L²)) | PROVED-mod-cite (Paper 2 L szego, L normalisation) |

## 0. Setting, and what is reused

−1 < δ ≤ 0, a := 1 + δ ∈ (0, 1], p > 1, 1 < s < 1 + 2p, α := (s−1−p)/p ∈ (−1, 1); n ≥ 2 fixed where stated. σ^δ := Σ_{k≥1}τ_k^{−s}δ_{τ_k^{−p}},
τ_k := k + δ; X_k = (n/τ_k)^p, **top node X₁ = (n/a)^p**. t = nz^{−1/p}, θ = πt (lattice), θ_δ := π(t − δ), κ_δ± := 1/(1 − e^{∓2iθ_δ}).
Pure power (ℓ₁ ≡ 1): w(z) = n^pt^{−s}, W = 2iθ′w = 𝗐_nz^α exactly (θ_δ′ = θ′), r_n ≡ 1. Paper 2's contour with n^p + δ′ replaced by
X₁ + δ′ (H-a), and c₀ := 1 + log(1/a) in (eq:Zn), so that the top segment lies in 𝒵_n. Constants C may depend on p, s, δ (and on
n when subscripted); "n-free" means independent of n.

*Reused verbatim* (their proofs use only the listed facts, all unchanged): Lemma interp (any discrete measure; poles X_k, residues
n^pw_kU_{j1}(X_k), Uz^{−nσ₃} = I + O(1/z) for |z| > X₁); Lemma invariance; Lemma bandweight; Lemma gfunction; Lemma signs; Lemma lips
(lattice g, φ, φ̃: JZC_M3_scope §3.1, G1 trivial); Lemma szego (i)–(v) (stated for any exponent / any q); Lemma normalisation (uses only
(O1), (O5) at ∞ and Lemma gfunction); Lemma B-cauchy; Cor L2. *Modified* (proved below): Lemma binetcut (ii), (iv); the proofs of
Lemma sumbound, Lemma lenssector, Prop apriori. External inputs: Paper 2 (eq:binet-bound) ("By T4 (DLMF 5.11.1 with the remainder
bound of §5.11(ii) …), for every φ < π, |j(t)| ≤ sec²(φ/2)/(12|t|), |j′(t)| ≤ C_φ/|t|² (|arg t| ≤ φ, |t| ≥ 1)"; primary quote:
RH/CITATIONS.md (DLMF) §5.11), the branch LnΓ analytic on ℂ∖(−∞,0] and real on (0,∞) (Paper 2 §6), and DLMF 5.5.3 as quoted in
Paper 2's proof of Lemma outer (1/Γ(t) = Γ(1−t)sin(πt)/π; primary quote: RH/CITATIONS.md (DLMF-5.5/5.11, Plan 54)) (fixed per
Rule R review A, F4).
**Not used:** DLMF 5.11.8 and Hurwitz's formula (Rule C: see JZC_M3a_H.md G4) — L1.1 removes the need for 5.11.8 here.

## 1. G1: the outer scalar (H-d Prop 2.1 as a proof)

j(u) := LnΓ(u) − (u−½)ln u + u − ½ln 2π (Paper 2); j_δ(t) := LnΓ(t−δ) − (t−δ−½)ln t + t − ½ln 2π; D̃_δ := e^{−j_δ(t)}, D_δ := κ_δ±D̃_δ in ℂ_±;
𝔟_δ(y) := 2Im(−j_δ(t₊) − Log(1 − e^{−2iθ_δ+})) (y < 0); B_δ := (eq:B) with 𝔟_δ; K := (4c−z)^{−1/2}; F_δ := D_δB_δK; for δ = 0 all is Paper 2.

**Lemma 1.1 (shift identity).** For t ≠ 0, |arg t| < π: t − δ ∉ (−∞, 0] and j_δ(t) = j(t−δ) + (t−δ−½)Log(1−δ/t) + δ.
*Proof.* t − δ = t + |δ| has arg between 0 and arg t, so it avoids (−∞,0] and arg(t−δ) − arg t ∈ (−π, π); hence ln(t−δ) − ln t = Log(1−δ/t).
Insert LnΓ(t−δ) = j(t−δ) + (t−δ−½)ln(t−δ) − (t−δ) + ½ln 2π (definition of j). ∎ (PROVED; checked to 10⁻³⁵, incl. Re t < 0 at p = 1.1.)

**Lemma 1.2 (j_δ).** Let φ ∈ (0, π), Σ_φ := {t ≠ 0: |arg t| ≤ φ}.
(a) j_δ is analytic on ℂ∖(−∞,0], real on (0,∞).
(b) For t ∈ Σ_φ, |t| ≥ 2: |j_δ(t)| ≤ C_J/|t|, C_J := sec²(φ/2)/6 + ⅔ (n-free, δ-uniform); |j_δ′(t)| ≤ (4C_φ + 2)/|t|².
(c) δ < 0, t ∈ Σ_φ, |t| ≤ |δ|/2: j_δ(t) = (δ+½)ln t + LnΓ(−δ) − ½ln 2π + ρ(t), |ρ| ≤ C|t|(1 + |ln|t||), |j_δ′(t) − (δ+½)/t| ≤ C(1 + |ln|t||).
*Proof.* (a) L1.1 and the branch of LnΓ. (b) |t−δ| ≥ |t| − 1 ≥ |t|/2 ≥ 1 and |arg(t−δ)| ≤ φ, so binet-bound gives |j(t−δ)| ≤ sec²(φ/2)/(6|t|),
|j′(t−δ)| ≤ 4C_φ/|t|². With w := δ/t (|w| ≤ ½), Log(1−w) = −w − w²/2 − R, |R| ≤ ⅔|w|³, and expanding,
(t−δ−½)Log(1−w) + δ = δ(1+δ)/(2t) + (δ+½)(w²/2 + R) − tR, whose modulus is ≤ (⅛ + ⅛ + 1/12 + ⅓)/|t| = ⅔/|t| (|δ| < 1, |δ+½| ≤ ½,
|t| ≥ 2). Differentiating L1.1: j_δ′ = j′(t−δ) + [Log(1−w) + w] − δ/(2t(t−δ)), and |Log(1−w)+w| ≤ |w|², |δ/(2t(t−δ))| ≤ 1/|t|².
(c) Re(t−δ) ≥ |δ|/2 > 0, so LnΓ(t−δ) = LnΓ(−δ) + O(|t|) and ψ(t−δ) = O(1) there; j_δ = LnΓ(t−δ) + (δ+½)ln t − t ln t + t − ½ln 2π, and
j_δ′ = ψ(t−δ) + (δ+½)/t − ln t. ∎ (PROVED-mod-cite: binet-bound. NUMERICAL: sup|t j_δ| ≤ 0.112 ≪ C_J on a grid, p ∈ {1.1, 1.5, 3}.)
(The leading term B₂(−δ)/(2t) of H-d (2.1) follows from L1.1 and j(u) ~ 1/(12u) but is never used.)

**Lemma 1.3 (binetcut (i)–(iii) for δ).** Let p > 1, n ≥ 2.
(i) D̃_δ is analytic and zero-free on ℂ∖(−∞,0]; D_δ is analytic and zero-free in ℂ_± with continuous boundary values on
ℝ∖({X_k} ∪ {0}); on (−∞,0), D_δ₋ = conj D_δ₊.
(ii) D_δ₊/D_δ₋ = e^{i𝔟_δ} on (−∞,0); 𝔟_δ is real-analytic; |𝔟_δ(y)| ≤ C min(1, |y|^{1/p}) (C n-free); |𝔟_δ′(y)| ≤ C|y|^{1/p−1}/n for
|y| ≤ (n/2)^p and ≤ C/|y| for |y| ≥ (n/2)^p; **𝔟_δ(y) → 𝔟_∞(δ) := 2[(δ+½)π/p − π/2 − πδ] = (π/p − π) + 2πδ(1/p − 1)** as y → −∞, with
|𝔟_δ − 𝔟_∞| ≤ C|t₊|(1 + ln(1/|t₊|)) for |t₊| ≤ |δ|/2 (δ < 0; δ = 0: Paper 2), hence ∫_{−∞}^{−1}|𝔟_δ − 𝔟_∞||y|^{−1}dy < ∞.
(iii) Paper 2 Lemma binetcut (iii) holds verbatim for B_δ (incl. (eq:B-bounds), C n-free).
*Proof.* (i) L1.1 (Γ(t−δ) has no zeros or poles); |e^{∓2iθ_δ}| = |e^{∓2iθ}| < 1 in ℂ_± by (eq:imtheta) (δ real); j_δ, θ_δ are real-symmetric.
(ii) On y < 0, t₊ = n|y|^{−1/p}e^{−iπ/p}, q := e^{−2iθ_δ+} has |q| = exp(−2π sin(π/p)|t₊|) < 1, so Log(1−q) is continuous, and
D_δ₊/D_δ₋ = e^{2i Im log D_δ₊}. For |t₊| ≥ 2 (⊃ |y| ≤ 1 as n ≥ 2): L1.2(b) with φ = π/p and |Log(1−q)| ≤ C_pe^{−2π sin(π/p)|t₊|} (as in Paper 2) give |𝔟_δ| ≤ C/|t₊|
= C|y|^{1/p}/n, and d/dt[j_δ + Log(1−q)] = O(|t|^{−2}), times |dt₊/dy| = |t₊|/(p|y|), gives the first derivative bound. 𝔟_δ is a function of
|t₊| alone; on |t₊| ≤ |δ|/2, L1.2(c) and q → e^{2πiδ}, 1 − e^{2πiδ} = 2|sin πδ|e^{i(π/2+πδ)} ≠ 0, give the limit (Im(−(δ+½)ln t₊) = (δ+½)π/p,
LnΓ(−δ) real) with the stated rate, and d/dt = O(1/|t|), so |𝔟_δ′| ≤ C/|y|; the compact range |δ|/2 ≤ |t₊| ≤ 2 is covered by continuity
(the constants depend only on |t₊|-ranges, hence are n-free). (iii) Paper 2's proof of (iii) uses only the properties in (ii). ∎

**Proposition 1.4 (binetcut (iv) for δ, and the normalised scalar).** Let p > 1, n ≥ 2, F♮ := F_δ·(−z)^{−δ} (principal power, cut [0,∞)).
(a) (O1_δ): F_δ is analytic and zero-free in ℂ∖[0,∞), has no jump on (−∞,0), continuous boundary values on (0,∞)∖{X_k}, and
F_δ₊ = F_δ₋e^{2iθ_δ} on (4c,∞)∖{X_k}. (O2)–(O4) hold with F̃_δ := F_δ/κ_δ = D̃_δB_δK, H_n^δ := (D̃_δB_δ)^{−2} > 0 on (0,∞),
H_n^δ(0⁺) = B_δ(0)^{−2}, ν_p = min(1/p, ½) ≤ 1/p, so the bound C|z|^{1/p} on |z| ≤ 1 gives (O3) (fixed per Rule R review A, F1),
constants n-free. (O5) near 0 holds verbatim.
(b) (O1) for F♮: analytic and zero-free in ℂ∖[0,∞), no jump on (−∞,0), F♮₊ = F♮₋e^{2iθ} on (4c,∞)∖{X_k} (lattice θ).
(c) (O5) at ∞ for F♮: |F♮(z)|^{±1} ≤ C_n|z|^{N_n} for |z| ≥ X₁ + δ′, z ∉ ℝ; and F♮(iy) → e^{L_δ}, L_δ given in C1.5, as y → ±∞.
*Proof.* (a) Paper 2's proof of binetcut (iv), with L1.2–L1.3 in place of binet-bound/binetcut (ii)–(iii): D_δB_δ extends across (−∞,0)
(iii); D_δ₊/D_δ₋ = (1−e^{2iθ_δ})/(1−e^{−2iθ_δ}) = −e^{2iθ_δ} and K₊/K₋ = −1 on (4c,∞). (O2): F̃_δ₊ = −F̃_δ₋ (from K); D̃_δ → 1 as
z → 0 in 𝒵_n (|t| → ∞, L1.2(b)). (O3): for z ∈ 𝒵_n, |z| ≤ 1, |t| ≥ n ≥ 2 and L1.2(b) give |j_δ(t)| ≤ C|z|^{1/p}/n, |dj_δ/dz| ≤ C|z|^{1/p−1}/n;
with (eq:B-bounds) this is (O3). (O4): for |z| ≥ 1 in 𝒵_n, |t| ≥ e^{−c₀}, and j_δ is bounded on {|t| ≥ e^{−c₀}, |arg t| ≤ ϑ_w/p} (L1.2(b) and
continuity, L1.1); (eq:B-bounds) gives the rest. (O5) near 0: |e^{∓2iθ_δ}| = |e^{∓2iθ}| → 0 off the lens, D̃_δ → 1, and Paper 2's window
argument for log B near 0 uses only L1.3(ii).
(b) (−z)^{−δ} is analytic, zero-free off [0,∞), with ((−z)^{−δ})₊/((−z)^{−δ})₋ = x^{−δ}e^{iπδ}/(x^{−δ}e^{−iπδ}) = e^{2πiδ} on (0,∞);
and e^{2iθ_δ}e^{2πiδ} = e^{2iθ}.
(c) *Polynomial bound.* For |z| ≥ X₁ + δ′: |t| ≤ a − ε_n. The zeros of 1 − e^{∓2πi(t−δ)} are t ∈ δ + ℤ; in {|t| ≤ a − ε_n} ∩ Σ_{π/p} there are
none (t = δ + k, k ≥ 1, has |t| ≥ a; t = δ − k ≤ 0 is outside Σ_{π/p} for δ < 0), and κ_δ± → 1/(1 − e^{±2πiδ}) ≠ 0, ∞ as t → 0; so
|κ_δ|^{±1} ≤ C_n (δ < 0; at δ = 0, κ_± = (±2πit)^{−1}(1 + O(t)) is a power of |z|, as in Paper 2) (fixed per Rule R review A, F2).
By L1.2(c) and continuity, |D̃_δ|^{±1} ≤ C_n|z|^{1/p}. |K|^{±1}, |(−z)^{−δ}|^{±1} are powers. *Window argument for B_δ at ∞*
(Paper 2's (O5) paragraph, made explicit): let |z| ≥ 2, z ∉ ℝ, and write log B_δ(z) = −(1/2π)∫𝔟_δ(y)(z−1)dy/((y−z)(y−1)).
If Re z ≥ −|z|/2, |y − z|² ≥ (y² + |z|²)/2 for y < 0 and the bound C∫_0^∞|z|du/((u+|z|)(u+1)) ≤ C(1 + log|z|) follows from |𝔟_δ| ≤ C.
If x := Re z < −|z|/2, put 𝒲 := [3x/2, x/2] ⊂ (−∞, −½]. Off 𝒲, |y − z| ≥ |y − x| ≥ (|y| + |z|)/16 (|x| ≥ |z|/2): same bound. On 𝒲, the 1/(y−1) term
is O(1); write 𝔟_δ(y) = 𝔟_δ(x) + (𝔟_δ(y) − 𝔟_δ(x)): the constant gives 𝔟_δ(x)[log(y−z)]_{3x/2}^{x/2}, bounded (both end points at distance in
[|x|/2, 3|x|] from z; Im(y − z) has fixed sign); the rest is ≤ sup_𝒲|𝔟_δ′|·∫_𝒲|y−x|/|y−z|dy ≤ (2C_n/|x|)·|x| by L1.3(ii)
(|𝔟_δ′| ≤ C_n/|y| on (−∞, −½]). So |log B_δ(z)| ≤ C_n(1 + log|z|) uniformly up to the cut, and |B_δ|^{±1} ≤ C_n|z|^{C_n}.
*Limit along iy.* Split 𝔟_δ = 𝔟_∞𝟙_{(−∞,−1)} + 𝔯_δ. Since ∫_{−∞}^{−1}[1/(y−z) − 1/(y−1)]dy = Log((1+z)/2), the first part contributes
−(𝔟_∞/2π)Log((1+z)/2) to log B_δ; the second tends to I_r := (1/2π)∫_{−∞}^0𝔯_δ(y)dy/(y−1) as z = iY → ∞ (dominated convergence:
|𝔯_δ(y)/(y−iY)| ≤ |𝔯_δ(y)|min(1, 1/|y|), integrable by L1.3(ii)). With L1.2(c), Log t = ln n − (1/p)Log z, Log(1 − e^{2πiδ}) =
ln(2|sin πδ|) + i(π/2 + πδ), and −½Log(4c − z) = −½Log(−z) + o(1), the coefficient of Log z in log F_δ is (δ+½)/p − 𝔟_∞/(2π) = ½ + δ and
that of Log(−z) is −½ (δ < 0 by L1.2(c); δ = 0 by (eq:binet-small) and κ_+ ∼ 1/(2πit), see C1.5) (fixed per Rule R review A, F2); so log F♮(iY) → L_δ, the imaginary parts cancelling (Log(−z) = Log z − iπ in ℂ₊). y → −∞: F♮(z̄) = conj F♮(z). ∎
(PROVED-mod-cite: binet-bound; DLMF 5.5.3 as quoted in Paper 2 for the form of L_δ.)

**Corollary 1.5 (H-d Prop 2.1, (2.4)).** Under P1.4, ϰ_∞♮ := F♮^{−1}e^{n(g − Log z)} is analytic on {|z| > X₁ + δ′} ∪ {∞}, ϰ_∞♮(∞) ≠ 0, and
F♮(z) → C_δ := 1/ϰ_∞♮(∞) uniformly as z → ∞ (boundary values on ℝ included); i.e. **F_δ(z) = C_δ(−z)^δ(1 + o(1))**. Moreover C_δ = e^{L_δ} > 0,
  L_δ = lnΓ(1+δ) − (δ+½)ln n − ½ln 2π + (𝔟_∞(δ)/2π)ln 2 + I_r(δ),  I_r(δ) = (1/2π)∫_{−∞}^0[𝔟_δ(y) − 𝔟_∞(δ)𝟙_{(−∞,−1)}(y)]dy/(y−1).
*Proof.* Paper 2 Lemma normalisation verbatim with F♮: on (−∞, −X₁−δ′) g and Log z both jump by 2πi, F♮ not at all (b); on (X₁+δ′, ∞)
e^{n(g−Log z)} jumps by e^{2iθ} (Lemma gfunction (i)), as does F♮ (b); (c) gives the polynomial bound and the bounded, non-vanishing limit
along iy, so ∞ is removable with ϰ_∞♮(∞) = e^{−L_δ}; Lemma gfunction (ii) gives e^{n(g−Log z)} → 1 uniformly. L_δ: from (c), using
e^{−LnΓ(−δ)}/(2|sin πδ|) = Γ(1+δ)/(2π) (DLMF 5.5.3 at t = −δ); L_δ is real, so C_δ > 0. At δ = 0 the same formula results from
(eq:binet-small) and κ ~ 1/(2πit) (Paper 2's |F(iy)| ≍ 1). ∎ NUMERICAL (m3a_g12_outer.out, n = 4, c = 1, dps 40): |log F♮(10³⁰e^{iψ}) − L_δ| ≤
1.5·10⁻¹⁹ (p = 3/2) and 1.5·10⁻⁹ (p = 3; the O(|z|^{−1/p}log|z|) tail) on ψ ∈ {10⁻³π, π/4, π/2, 3π/4, π − 10⁻³π}, δ ∈ {0, −0.3, −0.7, −0.95};
L_{−0.3} = −1.4000719248 agrees with m3a_hd_outer.out. Non-uniformity in δ → 0⁻ (H-d §3, "crossover"): the o(1) needs |t| ≪ |δ| (L1.2(c));
L_δ itself is continuous at δ = 0.

## 2. G2: the a-priori bound (Paper 2 App C) for the Hurwitz interpolant

Notation of H-d §3: V♮ := Paper 2 (eq:VM) with κ_δ (in L_±, A^△_±), the lattice φ, and F♮, F̃♮ := F♮/κ_δ = F̃_δ(−z)^{−δ};
W₀^{(β′)} := 𝗐_nz^{α+2δ}(4c − z)H_n^δ (principal), D_W := D_{W₀^{(β′)}}, D_∞ := D_W(∞), Q♮ := D_∞^{−σ₃}V♮D_W^{σ₃}; W₀^{(α)} := 𝗐_nz^α(4c−z)H_n^δ,
D_W^{(α)} := D_{W₀^{(α)}}. φ₁ := ½ϑ_lip. U_{j2}(z) = Σ_k w(X_k)U_{j1}(X_k)/(z − X_k), w(X_k) = n^pτ_k^{−s} ((eq:U-sum), Lemma interp).

**Lemma 2.1 (sum bound, Hurwitz).** Let M_n := max_j max_{[0,X₁]}|U_{j1}|, γ := p − s, T := n|z|^{−1/p}. For 0 < |z| ≤ 1, φ₁ ≤ |arg z| ≤ π:
  |U_{j2}(z)| ≤ I₁ := (M_n/sin φ₁)[Σ_{τ_k≤T}τ_k^{γ} + T^pΣ_{τ_k>T}τ_k^{−s}] ≤ I₂ := (M_n/sin φ₁)[max(a^γ, T^γ) + ∫_a^Tu^γdu + T^γ + T^{1+γ}/(s−1)].
Hence |U_{j2}(z)| ≤ C_{n,δ}(1 + |z|^α + 𝟙_{α=0}log(1/|z|)) ≤ C_{n,δ,η}|z|^{−η}(1 + |z|^α): Paper 2's Lemma sumbound with the same exponent;
δ enters only through M_n and the top-node factors a^γ, a^{1+γ}/|1+γ| (from ∫_a^T u^γ when α > 0) — not through the exponent.
*Proof.* |z − X| ≥ sin φ₁·max(|z|, X) for X > 0. X_k ≥ |z| iff τ_k ≤ T, and then w(X_k)/X_k = τ_k^γ; otherwise w(X_k)/|z| = T^pτ_k^{−s}
(T^p = n^p/|z|). This is I₁. The nodes τ_k ∈ a + ℕ₀ have spacing 1, so for monotone f, Σ_{a≤τ_k≤T}f(τ_k) ≤ max(f(a), f(T)) + ∫_a^Tf, and
Σ_{τ_k>T}τ_k^{−s} ≤ T^{−s} + T^{1−s}/(s−1). Finally T ≥ n ≥ 1, T^γ ≤ T^{1+γ}, T^{1+γ} = n^{1+p−s}|z|^α ((s−1)/p − 1 = α), ∫_a^Tu^γ ≤ T^{1+γ}/(1+γ)
(α < 0), ≤ a^{1+γ}/|1+γ| (α > 0), = ln(T/a) (α = 0). No Potter bound is needed (ℓ₁ ≡ 1). ∎ (PROVED.) NUMERICAL: see §3.

**Lemma 2.2 (lens sectors, Hurwitz).** Paper 2's Lemma lenssector holds for R built with κ_δ, with C = C_{n,η,δ}, after two changes in its
proof: (1) the poles of 𝒦_j(s) := U_{j1}W/(e^{2iθ_δ} − 1) in 𝒢 are where t ∈ δ + ℤ, |arg t| < ϑ_lip/p, i.e. exactly the Hurwitz nodes
(t = δ − m ≤ 0 lies off the sector), with residues w(X_k)U_{j1}(X_k) (θ_δ′ = θ′); (2) δ_s, r are chosen with t(δ_s), t(r) ∈ δ + ℕ + ½, and on
those arcs (|t| ≥ 1), |v| < ¼ gives |t| − u ≤ 1/16, so dist(u − δ, ℤ) ≥ 7/16 and |e^{2πi(t−δ)} − 1| ≥ 2e^{−π/4}sin(7π/16) (t = u + iv).
Steps (2)–(3) of that proof are unchanged since |e^{±2iθ_δ}| = |e^{±2iθ}|, and |W(s)| = |𝗐_n||s|^α (the η only absorbs the α = 0 logarithm).
The final sentence uses Lemma 2.1. ∎ (PROVED.)

**Lemma 2.3 (column factorisation).** Let G(z) := (−z)^{−δ}D_{x^{2δ}}(z), z ∉ [0, ∞). Then
(i) D_W = D_W^{(α)}D_{x^{2δ}}, D_{x^{2δ}} = (4cz/Υ)^δ (principal), and |G(z)| = |4c/Υ(z)|^δ; there is r_G = r_G(c) with |G|^{±1} ≤ 2 on |z| < r_G;
(ii) near 0, Q♮ = (const. diagonal)·U·M₀·(F♮D_W)^{σ₃} off the lens and ·(F̃♮D_W)^{σ₃} in the lens, with M₀ ∈ {e^{nφσ₃}, L_±e^{nφσ₃}A_±}
free of F; and |F♮D_W| = |F_δD_W^{(α)}|·|G|, |F̃♮D_W| = |F̃_δD_W^{(α)}|·|G| (exact: F♮D_W = F_δD_W^{(α)}G; fixed per Rule R
review A, F5(a)).
*Proof.* (i) Multiplicativity of D_q and W₀^{(β′)}(x) = W₀^{(α)}(x)x^{2δ} on (0, 4c); Lemma szego (i) with exponent 2δ and the value
c^δ > 0 at ∞ fix the root of D_{x^{2δ}}² = (4cz/Υ)^{2δ}; |w^δ| = |w|^δ for real δ; Υ(z) = −4c(1 + O(|z|^{1/2})) (Lemma szego (i)).
(ii) (eq:VM), (eq:Q): Q♮ = D_∞^{−σ₃}C♮_∞e^{−nγ_pσ₃}·U·M♮·D_W^{σ₃} and M♮ = M₀F♮^{σ₃} (resp. M₀F̃♮^{σ₃}); diagonal factors commute. ∎
(PROVED-mod-cite: Paper 2 L szego (i). NUMERICAL: D_{x^{2δ}} by quadrature of (eq:szego) = (4cz/Υ)^δ to 10⁻⁵⁰; |G| ∈ [1, 1.11] on |z| ≤ 10⁻², δ ∈ {−0.3, −0.9}, c = 0.7.)

**Proposition 2.4 (a-priori bound, Hurwitz).** Fix n ≥ n₀, p > 1, −1 < δ ≤ 0. Then det Q♮ ≡ 1, and
(i) for every η > 0, |Q♮(z)| ≤ C_{n,η,δ}|z|^{−|α|/2−η} on U(0, δ_r)∖Σ (δ_r: Paper 2's disc radius);
(ii) Q♮ is bounded on bounded sets at positive distance from 0, and Q♮ → I at ∞;
(iii) Q♮ has continuous boundary values on Σ minus its vertices (now incl. X₁ + δ′ ± ih₀, X₁ + δ′).
The same holds for (Q♮)^{−1}; and Q♮_± ∈ I + ∂𝒞(L²(Σ)) (Cor L2, verbatim: (1 + |α|)/4 < ½).
*Proof.* det: as in Paper 2. (i) By L2.3(ii), |Q♮| is bounded by C|G|^{±1} times the entries of U·M₀·diag(F_δD_W^{(α)}, (F_δD_W^{(α)})^{−1})
(F̃_δ in the lens), and |G|^{±1} ≤ 2 on |z| < r_G; so (i) is proved here for |z| < min(δ_s/2, r_G), and the annulus up to δ_r is
covered by (ii) (fixed per Rule R review A, F5(c)). For this pair, Paper 2's proof of (i) runs verbatim with: |e^{±nφ}| ≤ C (lattice φ);
|F_δ|^{±1} ≤ C off the lens and |F̃_δ|^{±1} ≤ C in it (P1.4(a), (O5) at 0); |D_W^{(α)}|^{±1} ≤ C_{n,η}|z|^{±α/2−η} (Lemma szego (vi), last claim:
its proof uses (O3)–(O4) for H_n^δ (P1.4(a)) and r_n ≡ 1); |1/W| = C|z|^{−α}; U_{j1} bounded; Lemma 2.1; Lemma 2.2. Off the lens: first
column ≤ C|z|^{α/2}, second ≤ C|z|^{−η}(1+|z|^α)|z|^{−α/2}; in the lens: first ≤ C(1 + |z|^{−α}|R_{·2}|)|z|^{α/2}, second as before; all
≤ C|z|^{−|α|/2−2η}. (ii) As in Paper 2: near 4c, (F̃♮D_W)² = W·ω♮·e^{±2πiδ} with ω♮ := D_W²/W₀^{(β′)} (W/F̃♮² = W₀^{(β′)}e^{∓2πiδ} in ℂ_±,
H-d §3 (ii)), bounded above and below by Lemma szego (vi)(b) applied to q₁ = x^{α+2δ}H°_n (H°_n := H_n^δ/H_n^δ(0⁺); r_n ≡ 1) (fixed per Rule R review A, F5(b)) (analytic and positive near 4c; (iv) holds for
any exponent); at ∞, Lemma normalisation holds for F♮ (C1.5), so Q♮ = k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃} → I. (iii) H-d Lemma (ii) (jumps). ∎
(PROVED-mod-cite + REVIEWED; status updated 2026-10-22 after Rule R review B, see header.)

*What changes vs Paper 2.* Exponents: none (|α|/2; the L² margin (1+|α|)/4 < ½ is δ-free). Constants: M_n, a^{p−s}, a^{1+p−s}/|1+p−s|, the
L1.2–L1.3 constants C(p,δ) (n-free), C_n of P1.4(c) (through κ_δ near t = 0: ∝ 1/|sin πδ|), the factor 2 from |G|. Geometry: node set
δ + ℕ, arc radii in δ + ℕ + ½, top vertex X₁ + δ′. **What would fail:** Prop apriori applied with D_W alone (exponent β′ = α + 2δ, as
Lemma szego (vi) would give |D_W|^{±1} ≲ |z|^{±β′/2}) yields |z|^{−|β′|/2}, not L² when |β′| ≥ 1 (e.g. α = −½, δ = −0.8); the
cancellation of L2.3 between (−z)^{−δ} in F♮ and D_{x^{2δ}} in D_W is essential.

## 3. Numerical checks (Rule N: NUMERICAL, not certified; finite samples of universally quantified statements)

- `m3a_g12_outer.out` (dps 40, n = 4, c = 1): L1.1 to 10⁻³⁵ (p ∈ {1.1, 1.5, 3}, δ ∈ {0, −0.3, −0.95}); L1.2 sup|tj_δ| ≤ 0.112 vs C_J ≥ 0.89;
  L1.3 𝔟_δ(−10⁸⁰) = 𝔟_∞ to 10⁻²⁰ and |𝔟_δ − 𝔟_∞|/(|t₊|ln(1/|t₊|)) ≤ 3.4 on y ∈ {−10¹⁰, −10²⁰, −10³⁰}; C1.5 as stated; P1.4 (O5) at 0:
  F_δ(10⁻¹²e^{iψ}) = (4c)^{−½}B_δ(0) to 2·10⁻¹¹ for ψ ∈ {π/3, π/2, π − 10⁻³π}.
- `m3a_g12_apriori.out` (dps 50, n = 4): exact moments ζ(s+jp, a); U_{j2} by direct summation + (A) exact Hurwitz-type tails
  (own Euler–Maclaurin: mpmath's zeta(σ, b) has relative error 4·10⁻¹¹ at σ = 20, b = 1200.5) or (B) Euler–Maclaurin with analytic
  derivatives; A and B agree to 4·10⁻⁵⁰ (fixed per Rule R review B, A-1). (mp.zeta(σ, b) is used only for small b, checked against the EM continuation
  to 10⁻⁴⁰; it is also O(b) in time for σ < 1.) L2.1 at (p, s) ∈ {(1.5, 1.75), (1.5, 2.5), (1.5, 3.1), (3, 2.5), (3, 5.5)}, δ ∈ {0, −0.5, −0.9},
  |z| ∈ {1, 10⁻², 10⁻⁴, 10⁻⁸, 10⁻¹⁶, 10⁻²⁴}, arg z ∈ {π/6, π/2, π}: |U_{j2}| ≤ I₁ ≤ I₂ everywhere (max |U_{j2}|/I₁ = 0.16); the exponent of |U_{j2}(iy)| from 10⁻¹⁶
  to 10⁻²⁴ is α = −½ to 10⁻⁸ for every δ (α + 2δ would be −1.5, −2.3), 0 to 10⁻⁷ for α > 0, −0.023 at α = 0 (the logarithm).
  L2.3: (eq:szego) by quadrature = (4cz/Υ)^δ to 2·10⁻⁵⁰ at 7 points incl. |z| = 10⁻⁶ next to both axes; a control (exponent 2δ) must fail.

## 4. Rule A (adversarial pass) — log

1. *Branches in L1.1 when Re t < 0* (p < 2): arg(t−δ) − arg t ∈ (−π, π) always; tested at p = 1.1, |arg t| up to 0.99π/p. No failure.
2. *δ → −1 (a → 0):* C_J is δ-uniform; the sum-bound constant grows like a^{p−s} (top node mass a^{−s} at X₁ = (n/a)^p) — a constant, not an
   exponent; κ_δ near t = 0 is controlled by |sin πδ| > 0. Tested δ = −0.9, −0.95: no exponent change.
3. *δ → 0⁻:* t = δ (zero of 1 − e^{−2πi(t−δ)}) approaches the sector Σ_{π/p} and C_n of P1.4(c) blows up like 1/|sin πδ|; all statements are
   fixed-n, fixed-δ; L_δ is continuous at 0 (the same formula passes the δ = 0 check). Consistent with H-d §3's crossover remark.
4. *Converse of C1.5's use:* with F_δ instead of F♮, ϰ_∞ jumps by e^{2πiδ} on (X₁+δ′, ∞) — not analytic; F♮ is needed (H-d §2).
5. *Does Q♮ contain F♮ without D_W anywhere near 0?* No: M♮ = M₀F♮^{σ₃} with F-free M₀ in Ω_∞ and the lens; the saturated region
   (where κ_δ^{σ₃} enters) is away from 0. Checked against (eq:VM).
6. *Window argument in Paper 2 (O5) at ∞:* Paper 2 writes "on (−∞, −½], where 𝔟′ is bounded"; boundedness alone only gives |log B| ≤ C|z|
   on the window. The needed |𝔟′(y)| ≤ C/|y| is proved in Paper 2's own proof of (ii) ("|𝔟′(y)| ≤ C/|y| otherwise"); P1.4(c) uses it. Wording
   gap in Paper 2, not an error of its result (record for FIXES via a human).
7. *α = 0:* the sum has a logarithm; covered by the η. *α > 0:* U_{j2} → finite limit (exponent 0, checked).
8. *Rule N:* a first version of the L2.3 check passed vacuously (a nan from log(1 − cos φ) was swallowed by max()); fixed, with a
   control that must fail. mpmath's zeta(σ, b) has relative error 4·10⁻¹¹ at σ = 20, b = 1200.5; replaced by own EM tails.
9. *Rule X:* nothing fitted; the checks evaluate the stated closed forms against independent direct evaluation.

## 5. Outcome

*Now proved (REVIEWED, see header):* G1 — H-d Prop 2.1 in full for p > 1, −1 < δ ≤ 0: F_δ = C_δ(−z)^δ(1 + o(1)) uniformly at ∞ with C_δ > 0 explicit
(C1.5), F_δ unchanged at 0 ((O2)–(O5) at 0, P1.4(a)), and (O1)/(O5) at ∞ for F♮, so Lemma normalisation and the extraction hold for the
degree-n Hurwitz U (H-d Lemma (i)). G2 — Prop apriori and Cor L2 for Q♮ with the lattice exponent |α|/2 (P2.4), via the Hurwitz sum
bound (L2.1), lens sectors (L2.2) and the column factorisation (L2.3). DLMF 5.11.8 is no longer needed for p > 1.
*Remains (as of 2026-10-22):* nothing for G1–G2. G3: JZC_M3a_H_G3.md; G4: resolved by the Fourier-sum route (JZC_M3a_H §3.1–3.2); G5:
JZC_M3a_H §3.3; the n-uniform comparison: JZC_M3a_H_G1u.md (p > 1), JZC_M3a_H_G1u_plt1.md (p < 1) — it is run in the α-frame of L2.3, as
anticipated (fixed per Rule R review B, A-2).
*Corrections to JZC_M3a_Hd.md:* (1) (2.1) need not cite DLMF 5.11.8 (L1.1 + Paper 2's binet-bound suffice; only O(1/t) is used).
(2) (2.4)'s "monodromy" step is replaced by Lemma normalisation, which gives the limit uniformly in direction. (3) (O5) at ∞ and the
contour vertices must use X₁ + δ′ = (n/a)^p + δ′, not n^p + δ′ (its §1 quote of (O5); §6 item 6 noted the node). (4) §3 (iv)'s
identity [·] = (4c/Υ)^δe^{±iπδ} holds in ℂ_± with principal branches (arg Υ ∈ (0, π) in ℂ₊); only its modulus |G| = |4c/Υ|^δ is
used (L2.3) (fixed per Rule R review A, F3). (5) Its claims "(F7) with the same
exponent |α|/2" and 𝔟_∞(δ) are confirmed; no claim of the H-d memo was found false.
