# JZC M3a, Theorem H gaps 2 and 3 for 0 < p < 1: the a-priori bound in the seam geometry, and E_plt1 Lemma F.1 with the complex seam densities

Status (2026-10-21): NOT REVIEWED (Rule R pending for everything below). Labels per VERIFICATION_POLICY.md. Closes, modulo review,
items 2 and 3 of JZC_M3a_H.md §4 ("What is still open for (i)"). Setting: Hurwitz lattice λ_k = (k + δ)^p, k ≥ 1, **0 < p < 1,
−1 < δ < 0**, a := 1 + δ, 1 < s < 1 + 2p, α := (s − 1 − p)/p ∈ (−1, 1), n ≥ n₀ fixed where stated. Seam objects (χ_±^δ, χ_δ, F_δ,
B_in^δ, B_out^δ, λ_δ, ϖ_δ, H_n^δ) are those of JZC_M3a_H_G3.md §2; everything else (U, R, W, φ, θ_δ, κ_δ, F♮ := F_δ(−z)^{−δ}, Q♮,
D_W, D_W^{(α)}, G) as in JZC_M3a_H_G12.md §2. Everything attributed to Paper 2 is quoted from papers/paper2/{sec_5,sec_6,app_outer,
app_c}.tex as read for this note; E_plt1 is research/G1/RH/second_order/E_plt1.md §3 (REVIEWED for δ = 0).
Checks: `checks/m3a_g23_apriori.py/.out` (gap 2), `checks/m3a_g23_F1.py/.out` (gap 3); counts in §4.

| # | Statement | Label |
|---|---|---|
| L2.1′ | G12 L2.1 (Hurwitz sum bound) holds for 0 < p < 1 verbatim; line-by-line audit: it is p-free (p enters only the constant 1/sin(πp/8)) | PROVED + NUMERICAL |
| L2.2′ | G12 L2.2 (lens sectors) holds for 0 < p < 1; the poles of 𝒦_j in the sector are exactly the Hurwitz nodes; arc constant corrected | PROVED + NUMERICAL |
| L2.3′ | G12 L2.3 (column factorisation, exponent \|α\|/2) holds for 0 < p < 1, in S_in and S_out alike | PROVED-mod-cite (Paper 2 L szego (i)) |
| L2.4 | seam inputs near 0: (O5) near 0 for F_δ, (O3)–(O4) for H_n^δ (ν_p = ½), hence \|D_W^{(α)}\|^{±1} ≤ C_{n,η}\|z\|^{±α/2−η} | PROVED-mod-cite (Paper 2 L seam, L corner, L szego (vi); G3 Lemma 3; G12 L1.2) + NUMERICAL |
| L2.5 | the seam scalar at ∞ uniformly up to the seams: χ_δ bounded on {\|z\| ≥ 1} and χ_δ → 0 uniformly; \|F_δ\|^{±1} ≤ C_n\|z\|^{N_n} next to the seams | PROVED-mod-cite (G3 Lemma 3 (ii); G12 L1.2 (c)) + NUMERICAL |
| P2.6 | Prop apriori for Q♮, p < 1: \|Q♮\| ≤ C_{n,η,δ}\|z\|^{−\|α\|/2−η}; Q♮ → I; Cor L2 (Q♮_± ∈ I + ∂𝒞(L²)) | PROVED-mod-cite (Paper 2 L szego, L normalisation, Cor L2; G3 Lemma 3, Prop 4) |
| L M | majorants of the complex seam densities: ℓ₋ = conj ℓ₊, \|ℓ_±\| ≤ ℓ, \|ℓ_±′\| ≤ ℓ′, \|ℓ_±\| ≤ π + log(1/s_δ) | PROVED + NUMERICAL |
| F.1_δ | E_plt1 Lemma F.1 (i)–(iv) with ℓ_±: (i), (ii), (iv) hold with the listed line changes; (iii) gives the Fourier sum m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ) (not ζ(−kp)/(kn^{kp})); the constants of (iv) are δ-free | PROVED-mod-cite (as E_plt1 F.1 + G3 Lemma 3 + G12 L1.2; DLMF 5.2.1, 25.2.1) + NUMERICAL |
| Rem H | m_k(δ) = ζ(−kp, 1+δ)/(kn^{kp}) | NUMERICAL (Hurwitz's formula NOT QUOTED) |

## 0. What Paper 2 does for p < 1 in App C, and the shape of the answer

Paper 2's App C (Lemma sumbound, Lemma lenssector, Prop apriori, Cor L2) has no separate p < 1 version: its standing
assumptions (sec_5, \subsection{Standing assumptions}: "Throughout Sections [frame]–[extraction] and the appendices we fix p > 0
and 1 < s < 1 + 2p"), and App C uses
p only through (a) the angles (eq:thetaw)/(eq:angles) — for p < 1, ϑ_w⁰ = 3πp/8, ϑ_lip⁰ = πp/4, and "θ_w < πp/2 if p < 1"; (b) (O5)
near 0 for F and (O3)–(O4) for H_n (through Lemma szego (vi)), which for p < 1 are supplied by app_outer §outer-plt1 (Lemma seam
(iv), with ν_p = ½: "Since ν_p = ½, this is (O3)"); (c) Lemma normalisation, which needs (O5) at ∞. RH_plt1b §2 (REVIEWED) records the
same for the KMVV route: "(Y4)_x. The sum bound is p-free. The lens-sector argument needs Im θ < 0 on 0 < arg s < φ₀ … i.e. only
φ₀ < πp."

So the p < 1 Hurwitz a-priori bound is G12 §2 (L2.1–P2.4) with the seam inputs of G3 in place of the Binet-cut inputs of G12 §1. The
audit below confirms that L2.1–L2.3 are p-free and that every p > 1-specific input of P2.4 has a seam replacement. One input was
not covered by any written lemma: the bound on e^{χ_δ} at ∞ *next to the seams* (needed for the polynomial bound in (O5) at ∞, hence
for G3 Lemma 2/Prop 4 and Lemma normalisation). Lemma 2.5 supplies it (window argument of Lemma corner (iii), at ∞). The same
statement is asserted without proof in Paper 2 for δ = 0 (For FIXES, §5).

For gap 3 (E_plt1 Lemma F.1 with the complex densities ℓ_±): every estimate in F.1 uses ℓ only through |ℓ| and |ℓ′|, and the
pointwise majorants |ℓ_±| ≤ ℓ, |ℓ_±′| ≤ ℓ′ (Lemma M) make (ii) and (iv) go through with δ-free constants. What changes is the
algebra: the jump identity in (i) (factor e^{±2πiδ}, two different densities), Tonelli → Fubini in (iii), and the value of the
moments, which is the Fourier sum of JZC_M3a_H.md §3.2, not ζ(−kp)/(kn^{kp}). The full line-by-line table is §2.2.

## 1. Gap 2: the a-priori bound for p < 1 (Paper 2 App C in the seam geometry)

Angles. ℓ₁ ≡ 1 satisfies (A_ϑ) for every ϑ, so 𝗆 = 1 in (eq:thetaw): ϑ_w = 3πp/8, ϑ_lip = πp/4, φ₁ := ½ϑ_lip = πp/8, and
ϑ_lip < (5/4)ϑ_lip < ϑ_w < θ_seam := πp/2. Z_n ⊂ S_in (G3 §1 takes the outer radius e^{pc₀}n^p > X₁ = (n/a)^p).

**Lemma 2.1′ (sum bound, p < 1).** G12 L2.1 holds verbatim for 0 < p < 1: with M_n := max_j max_{[0,X₁]}|U_{j1}|, γ := p − s,
T := n|z|^{−1/p}, for 0 < |z| ≤ 1, φ₁ ≤ |arg z| ≤ π,
  |U_{j2}(z)| ≤ I₁ := (M_n/sin φ₁)[Σ_{τ_k≤T}τ_k^γ + T^pΣ_{τ_k>T}τ_k^{−s}] ≤ I₂ := (M_n/sin φ₁)[a^γ + ∫_a^Tu^γdu + T^γ + T^{1+γ}/(s−1)],
hence |U_{j2}(z)| ≤ C_{n,δ}(1 + |z|^α + 𝟙_{α=0}log(1/|z|)) ≤ C_{n,δ,η}|z|^{−η}(1 + |z|^α).
*Proof (audit of G12's proof, each line with its p-dependence).*
1. |z − X| ≥ sin φ₁·max(|z|, X) for X > 0, φ₁ ≤ |arg z| ≤ π, φ₁ < π/2: plane geometry, p-free.
2. X_k = (n/τ_k)^p ≥ |z| ⟺ τ_k ≤ T: monotonicity of u ↦ u^p, any p > 0.
3. w(X_k)/X_k = n^pτ_k^{−s}(τ_k/n)^p = τ_k^γ and w(X_k)/|z| = T^pτ_k^{−s}: identities. This is I₁.
4. Spacing 1 of τ_k ∈ a + ℕ₀: for decreasing f, Σ_{a≤τ_k≤T}f(τ_k) ≤ f(a) + ∫_a^Tf. For p < 1, γ = p − s < 0 (s > 1 > p), so u^γ is
   decreasing and max(a^γ, T^γ) = a^γ: only one of G12's two monotone cases occurs (the increasing case γ > 0 needs p > s > 1).
5. Σ_{τ_k>T}τ_k^{−s} ≤ T^{−s} + T^{1−s}/(s−1): s > 1.
6. T ≥ n ≥ 1, so T^γ ≤ T^{1+γ}; T^{1+γ} = n^{1+p−s}|z|^{−(1+p−s)/p} = n^{1+p−s}|z|^α ((s−1−p)/p = α, an identity in p);
   1 + γ = −pα, so ∫_a^Tu^γ ≤ T^{1+γ}/(1+γ) (α < 0), ≤ a^{1+γ}/|1+γ| (α > 0), = ln(T/a) (α = 0).
So p enters only the constant 1/sin φ₁ = 1/sin(πp/8) (and n^{1+p−s}); the exponent is α, δ-free. ∎ (PROVED.)
NUMERICAL (§4, [A]): |U_{j2}| ≤ I₁ ≤ I₂ at (p, s) ∈ {(½, 1.25), (½, 1.8), (¾, 1.375), (0.3, 1.15), (0.3, 1.45)}, δ ∈ {0, −½, −0.9},
|z| ∈ {1, 10⁻², 10⁻⁴, 10⁻¹⁶, 10⁻²⁴}, arg z ∈ {φ₁, π/2, π}; fitted exponent = min(α, 0); control α + 2δ fails.

**Lemma 2.2′ (lens sectors, p < 1).** Paper 2's Lemma lenssector holds for R built with κ_δ, with C = C_{n,η,δ}, exactly as in G12 L2.2.
*Proof (audit).* 𝒢 := {r < |s| < δ_s, |arg s| < ϑ_lip} ⊂ Z_n ⊂ S_in (ϑ_lip < ϑ_w), so W = 𝗐_ns^α is analytic on a neighbourhood of
𝒢̄ (Lemma bandweight, r_n ≡ 1). (1) *Poles.* e^{2iθ_δ(s)} = 1 ⟺ t − δ ∈ ℤ, t real. On 𝒢̄, |arg t| = |arg s|/p ≤ π/4, so t > 0 and
t = δ + k with k ≥ 1: exactly the Hurwitz nodes. The other points t = δ − m ≤ δ < 0 have arg t = π, i.e. arg z = ±πp, which lie in
S_out, far from 𝒢. Residues w(X_k)U_{j1}(X_k), since θ_δ′ = θ′. (2) *Ray arg s = ϑ_lip.* (eq:imtheta) needs 0 < arg z < min(π, πp);
ϑ_lip = πp/4 < πp. So |e^{2iθ_δ} − 1|^{−1} ≤ 2exp(−2πn|s|^{−1/p}sin(π/4)) (|e^{±2iθ_δ}| = |e^{±2iθ}|, δ real). This is RH_plt1b's
condition "φ₀ < πp". (3) *Ray arg s = −ϑ_lip:* 𝒦_j = −U_{j1}W + super-small, ∫_0^{δ_s}ρ^α dρ/(ρ + |z|) ≤ C(1 + |z|^α + log(1/|z|))
(α > −1); p-free. (4) *Arcs* |s| = r, δ_s with t ∈ δ + ℕ + ½ and |t| ≥ 1 (δ_s small). Write t − δ = u′ + iv. If |v| < ¼:
|t| − Re t = v²/(|t| + Re t) ≤ 1/16 (Re t > 0 since |arg t| < π/4), so dist(u′, ℤ) ≥ 7/16 and |e^{2πi(t−δ)} − 1| = 2e^{−πv}|sin π(u′ + iv)|
≥ 2e^{−π/4}sin(7π/16). If |v| ≥ ¼: |e^{2πi(t−δ)}| = e^{−2πv} ∉ (e^{−π/2}, e^{π/2}), so |e^{2πi(t−δ)} − 1| ≥ 1 − e^{−π/2}. Hence
|e^{2πi(t−δ)} − 1| ≥ c_arc := min(1 − e^{−π/2}, 2e^{−π/4}sin(7π/16)) = 0.7921 (G12 L2.2 wrote only the |v| < ¼ constant; Paper 2:
"if |v| ≥ ¼ this is clear"). The last sentence of the proof (z ∈ Ω_b with φ₁ ≤ |arg z| < (5/4)ϑ_lip): R_{j2} = U_{j2} −
U_{j1}We^{∓2iθ_δ}κ_δ±, the second term super-small, the first by L2.1′. ∎ (PROVED.)
NUMERICAL (§4, [L]): (a) R_{j2} is continuous across Hurwitz nodes (relative jump ≤ 1.2·10⁻¹¹ at ε = 10⁻¹², while U_{j2} itself jumps by
~10¹¹); with the lattice θ in place of θ_δ the jump stays ~10¹² (control, must fail, fails); (b) in the lens (arg z = φ₁/2) the
exponent of |R_{j2}| is min(α, 0); (c) c_arc on 3 × 3 × 39 × 99 arc samples.

**Lemma 2.3′ (column factorisation, p < 1).** G12 L2.3 holds verbatim: D_W = D_W^{(α)}D_{x^{2δ}}, D_{x^{2δ}} = (4cz/Υ)^δ, |G| = |4c/Υ|^δ,
|G|^{±1} ≤ 2 on |z| < r_G; near 0, Q♮ = (const. diag)·U·M₀·(F♮D_W)^{σ₃} off the lens and ·(F̃♮D_W)^{σ₃} in the lens, with
|F♮D_W| = |F_δD_W^{(α)}|·|G|·const.
*Proof.* Lemma szego (i) concerns the band [0, 4c] only; (eq:VM)/(eq:Q) are pointwise algebra. For p < 1 the region near 0 off the
lens contains parts of S_in and of S_out; F_δ is one analytic function there (no jump across the seams: G3 Lemma 3 (iii) = Paper 2
Lemma seam (iv), "F … extends analytically across Σ^s_±"), so M♮ = M₀F♮^{σ₃} holds in both. ∎ (PROVED-mod-cite: Paper 2 L szego (i).)

**Lemma 2.4 (seam inputs near 0).** Fix n ≥ n₀. (a) |F_δ|^{±1} ≤ C_n on U(0, δ_r) ∖ (Ω̄_b ∪ [0, ∞)) and |F̃_δ|^{±1} ≤ C_n on
Ω_b ∩ U(0, δ_r), F̃_δ := F_δ/κ_δ = D̃_δB_in^δKe^{χ_δ}; in fact F_δ → F₀ := (4c)^{−½}e^{χ_δ(0)} as z → 0 off the lens and F̃_δ → F₀ in
it. (b) (O3)–(O4) hold for H_n^δ = (D̃_δB_in^δe^{χ_δ})^{−2} on Z_n with ν_p = ½. (c) For every η > 0, |D_W^{(α)}(z)|^{±1} ≤
C_{n,η}|z|^{±α/2−η} for 0 < |z| < ¼η_*, z ∉ [0, ∞).
*Proof.* (a) In S_in off the lens, ¾ϑ_lip/p ≤ |arg t| < π/2, so |e^{∓2iθ_δ}| = exp(−2π|t|sin|arg t|) → 0 and κ_δ → 1; D̃_δ → 1 (G12
L1.2(b) with φ = π/2: |j_δ(t)| ≤ C_J/|t|); B_in^δ(z) = (1+z)^{ϖ_δ}(1+z)/(1+λ_δz) → 1. In S_out, B_out^δ → 1. K → (4c)^{−½}. χ_δ is
bounded near 0 uniformly up to the seams and continuous at 0 from every sector: Paper 2 Lemma corner (iii) and (ii) for χ_δ, whose
proofs use only the density bounds of corner (i), supplied for χ_±^δ by G3 Lemma 3 (ii) (|χ_±^δ(ζ)| ≤ C|ζ| on |ζ| ≤ 1, |χ_±^δ′| ≤ C on
|ζ| ≤ 2, χ_±^δ/ζ integrable at ∞). In the lens, F̃_δ omits κ_δ, and the same facts apply. (b) For z ∈ Z_n,
log H_n^δ − log H_n^δ(0⁺) = 2j_δ(t) − 2log B_in^δ(z) − 2(χ_δ(z) − χ_δ(0)). For |z| ≤ 1: |t| ≥ n ≥ 2, |arg t| ≤ 3π/8, so G12 L1.2(b) gives
|j_δ(t)| ≤ C|z|^{1/p}/n and |d j_δ(t)/dz| = |j_δ′(t)||t|/(p|z|) ≤ C|z|^{1/p−1}/n; |log B_in^δ| ≤ C|z| and |(log B_in^δ)′| ≤ C (Re(λ_δz) > 0
on S_in, so |1 + λ_δz| ≥ 1); corner (ii) for χ_δ gives |χ_δ − χ_δ(0)| ≤ C|z|(1 + log(1/|z|)), |χ_δ′| ≤ C(1 + log(1/|z|)). Since 1/p > 1,
the total is ≤ C|z|^{1/2} with derivative ≤ C|z|^{−1/2}: (O3) with ν_p = ½, as in Paper 2. For |z| ≥ 1 in Z_n: j_δ is bounded on
{|t| ≥ e^{−c₀}, |arg t| ≤ 3π/8} (L1.2(b) for |t| ≥ 2, continuity of the analytic j_δ on the compact rest), |log B_in^δ| ≤ C(1 + log|z|),
|χ_δ − χ_δ(0)| ≤ C(1 + log|z|)²: (O4). (c) Paper 2 Lemma szego (vi), last claim, for the weight W₀^{(α)} = 𝗐_nz^α(4c − z)H_n^δ: its
proof uses (O3)–(O4) for H_n and r_n ≡ 1 only. ∎ (PROVED-mod-cite: Paper 2 L corner, L szego (vi); G3 Lemma 3 (ii); G12 L1.2.)
NUMERICAL (§4, [O]): F_δ/F₀ → 1 at |z| = 10⁻⁸ off the lens, in S_out and at angular distance 10⁻⁸ from both seams (both sides);
F̃_δ/F₀ → 1 in the lens.

**Lemma 2.5 (the seam scalar at ∞, uniformly up to the seams).** Fix n ≥ 2, 0 < p < 1, −1 < δ < 0. Then χ_δ is bounded on
{|z| ≥ 1} ∖ (Σ^s_+ ∪ Σ^s_−), uniformly up to the seams (boundary values included), and χ_δ(z) → 0 as z → ∞ uniformly in arg z.
Consequently |F_δ(z)|^{±1} ≤ C_n|z|^{N_n} for |z| ≥ X₁ + δ′, z ∉ ℝ, including next to the seams.
*Proof.* *Density derivative.* On Σ^s_+, t = −i|t|, |t| = n|ζ|^{−1/p}, dt/dζ = −t/(pζ). Write
χ_+^δ = −ρ_δ(t) − (δ+½)Log t − Log(1 − e^{2πiδ}e^{−2π|t|}) + (ϖ_δ+1)Log(1+ζ) − Log(1+λ_δζ) − (½+δ)Log(1 − ζ/2πn), with
ρ_δ(t) := j_δ(t) − (δ+½)Log t. Differentiate in ζ. The terms with a 1/ζ part: −(δ+½)Log t = −(δ+½)ln n + ((δ+½)/p)Log ζ, and the
three elementary logarithms, whose derivatives are (ϖ_δ+1)/ζ − 1/ζ − (½+δ)/ζ + O_n(|ζ|^{−2}) for |ζ| ≥ 4πn. The 1/ζ coefficients sum to
(δ+½)/p + ϖ_δ − ½ − δ = 0 (the identity of G3 Lemma 3 (ii): ϖ_δ = (1 − 1/p)(½ + δ)). For |t| ≤ |δ|/2, G12 L1.2(c) gives
|ρ_δ′(t)| = |j_δ′(t) − (δ+½)/t| ≤ C(1 + |ln|t||), so |dρ_δ/dζ| ≤ C|t|(1 + |ln|t||)/|ζ|. And |1 − e^{2πiδ}q| ≥ s_δ := min_{q∈[0,1]}
|1 − qe^{2πiδ}| > 0 (δ ∉ ℤ), so |d/dζ Log(1 − e^{2πiδ}e^{−2π|t|})| ≤ (2π/s_δ)|dt/dζ| = (2π/(ps_δ))|t|/|ζ|. Hence, with |t| → 0,
  |χ_+^δ′(ζ)| ≤ ε(|ζ|)/|ζ|,  ε(ρ) := C_n(ρ^{−1/p}(1 + log ρ) + ρ^{−1}) → 0  (ρ ≥ ρ₀ := max(4πn, (2n/|δ|)^p)),
and |χ_+^δ′(ζ)| ≤ C_n/|ζ| on 1 ≤ |ζ| ≤ ρ₀ (continuity on a compact set; χ_+^δ is real-analytic on the open ray, G3 Lemma 3 (ii)).
Σ^s_− by conjugation. Also (G3 Lemma 3 (ii)) |χ_±^δ(ζ)| ≤ C|ζ| on |ζ| ≤ 1, χ_±^δ → 0 at ∞, so ‖χ_±^δ/ζ‖_{L¹} =: A < ∞.
*Window argument* (Paper 2 Lemma corner (iii), at ∞). Let τ := ⅕sin θ_seam and |z| ≥ 2. (A) If dist(z, Σ^s_+ ∪ Σ^s_−) ≥ τ|z|, then
|ζ − z| ≥ (τ/3)(|ζ| + |z|) on both seams (as in corner (ii)), so |χ_δ(z)| ≤ (3/(2πτ))∫_0^∞(|χ_+^δ| + |χ_−^δ|)(ρ)dρ/(ρ + |z|) ≤ C·A, and
→ 0 as |z| → ∞ by dominated convergence (majorant |χ_±^δ(ρ)|/ρ). (B) Otherwise z is within τ|z| of one seam, say Σ^s_+, with nearest
point z* = re^{iθ_seam}; then (1 − τ)|z| ≤ r ≤ (1 + τ)|z| and |z − z*| ≤ r/4. Split Σ^s_+ into the window 𝒲 := {|ζ − z*| ≤ r/2} and
the rest. On 𝒲: χ_+^δ(ζ) = χ_+^δ(z*) + (χ_+^δ(ζ) − χ_+^δ(z*)). The constant contributes χ_+^δ(z*)[Log(ζ − z)] between the end points
z* ± (r/2)e^{iθ_seam}, which are at distance in [r/4, 3r/4] from z, and the argument of ζ − z changes by less than π along the segment;
so this is ≤ |χ_+^δ(z*)|(log 3 + π). The remainder: |χ_+^δ(ζ) − χ_+^δ(z*)| ≤ sup_𝒲|χ_+^δ′|·|ζ − z*| and |ζ − z| ≥ |ζ − z*| (z − z* is
orthogonal to the seam), so it contributes ≤ sup_𝒲|χ_+^δ′|·length(𝒲) ≤ 2sup_{ρ≥r/2}ε(ρ) (resp. ≤ 2C_n for r ≤ 2ρ₀). Off 𝒲, |ζ − z| ≥ |ζ − z*|/2 ≥ (|ζ| + r)/12 (|ζ − z*| = ||ζ| − r| > r/2), so
this part is ≤ 12∫|χ_+^δ(ρ)|dρ/(ρ + r) ≤ 12A, → 0 as r → ∞. On Σ^s_−, |ζ − z| ≥ c_p(|ζ| + |z|) (the angle between z and Σ^s_− is at least
2θ_seam − arcsin τ ≥ θ_seam), so the same bound. Every constant is independent of dist(z, Σ^s_+), so the bounds hold for the
boundary values too; and |χ_+^δ(z*)| → 0, sup_{ρ≥r/2}ε(ρ) → 0. *Polynomial bound.* For |z| ≥ X₁ + δ′: in S_out, F_δ = B_out^δKe^{χ_δ}, a product of
powers and a bounded factor. In S_in, |t| ≤ n(X₁ + δ′)^{−1/p} =: a − ε_n < a and |arg t| ≤ π/2; the zeros of 1 − e^{∓2πi(t−δ)} are
t ∈ δ + ℤ, at distance ≥ min(ε_n, |δ|) from this closed half-disc, so |κ_δ|^{±1} ≤ C_n; |j_δ(t)| ≤ |δ + ½|·|ln|t|| + C_n (G12 L1.2 (c)
and continuity) gives |D̃_δ|^{±1} ≤ C_n|t|^{−|δ+½|} = C_n'|z|^{|δ+½|/p}; B_in^δ, K are powers; e^{χ_δ} is bounded above and below. ∎
(PROVED-mod-cite: G3 Lemma 3 (ii) [NOT REVIEWED]; G12 L1.2 (c); Paper 2 Lemma corner (ii)–(iii) for the geometry.)
NUMERICAL (§4, [W]): at angular distance 10⁻⁸ from both seams, max|χ_δ| decreases from |z| = 10⁸ to 10¹² (≤ 10⁻⁵ at 10¹²) and
|F_δ(−z)^{−δ}/(2πn)^{−½−δ} − 1| ≤ 10⁻⁵ at 10¹²; χ_δ bounded next to the seams on |z| ∈ [1, 10⁵]; Plemelj χ_out − χ_in = χ_+^δ at 10³.

*Why Lemma 2.5 is needed.* G3 Prop 4 obtains F_δ ~ (2πn)^{−½−δ}(−z)^δ uniformly from G3 Lemma 2, whose hypothesis is
|F|^{±1} ≤ C|z|^N on all of {|z| > R}; and Paper 2 Lemma normalisation needs |ϰ_∞| ≤ C_n|z|^{N_n} on {|z| > X₁ + δ′} ∖ ℝ. Next to the
seams at ∞ neither Lemma corner (ii) (needs dist ≥ τ₀|z|) nor (iii) (only U(0, 1)) applies. G3 Lemma 3 (iii) quotes "the polynomial
bound at ∞" as verbatim from Paper 2 Lemma seam (iv), where it reads "In S_in ∩ {|z| ≥ n^p+δ′}, |t| < 1 and t stays away from 1, so D,
B_in, K and e^χ are bounded above and below by powers of |z|" with no argument for e^χ near the seams. Lemma 2.5 closes this for δ < 0.

**Proposition 2.6 (a-priori bound, Hurwitz, 0 < p < 1).** Fix n ≥ n₀, 0 < p < 1, −1 < δ < 0. Then det Q♮ ≡ 1, and
(i) for every η > 0, |Q♮(z)| ≤ C_{n,η,δ}|z|^{−|α|/2−η} on U(0, δ_r) ∖ Σ;
(ii) Q♮ is bounded on bounded sets at positive distance from 0, and Q♮ → I at ∞;
(iii) Q♮ has continuous boundary values on Σ minus its vertices (incl. X₁ + δ′ ± ih₀, X₁ + δ′).
The same holds for (Q♮)^{−1}; and Q♮_± ∈ I + ∂𝒞(L²(Σ)) (Cor L2 verbatim: (1 + |α|)/4 < ½).
*Proof.* G12 P2.4's proof, with the following substitutions (nothing else in it depends on p or on the outer-scalar construction).
- det: as in Paper 2 (det U = 1; all other factors have determinant 1).
- (i): L2.3′ reduces to the pair (F_δD_W^{(α)}, its inverse) times |G|^{±1} ≤ 2. Paper 2's proof of Prop apriori (i) then runs with:
  |e^{±nφ}| ≤ C (Lemma signs (iii), lattice φ, p-generic); |F_δ|^{±1} ≤ C off the lens and |F̃_δ|^{±1} ≤ C in it (L2.4 (a), in S_in and
  S_out); |D_W^{(α)}|^{±1} ≤ C_{n,η}|z|^{±α/2−η} (L2.4 (c)); |1/W| = C|z|^{−α}; U_{j1} bounded; L2.1′ off the lens (|arg z| ≥ ¾ϑ_lip > φ₁);
  L2.2′ in the lens. The column bounds are those of Paper 2: ≤ C|z|^{−|α|/2−3η}.
- (ii): near 4c, (F̃♮D_W)² = Wω♮e^{±2πiδ} (H-d §3 (ii); algebra), with ω♮ bounded above and below by Lemma szego (vi)(b) applied to
  q₁ = x^{α+2δ}Ĥ_n^δ; H_n^δ is analytic and positive near 4c because 4c ∈ Z_n ⊂ S_in at positive distance from the seams. At the other
  vertices all factors are analytic and bounded (the seams are not part of Σ, and nothing jumps across them). At ∞: Lemma normalisation
  for F♮ — its hypotheses are (O1) for F♮ (G3 Cor 5), the polynomial bound (L2.5) and the limit F♮ → (2πn)^{−½−δ} (G3 Prop 4, whose
  Lemma-2 hypothesis is now supplied by L2.5); so Q♮ = k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃} → I.
- (iii): H-d Lemma (ii) / G3 Cor 5 (jumps); seams carry no jump.
- Cor L2: Paper 2's proof with η = (1 − |α|)/4: the margin is δ- and p-free. ∎
(PROVED-mod-cite: Paper 2 L szego, L normalisation, L signs, Cor L2; G3 Lemma 3, Prop 4, Cor 5 [NOT REVIEWED]; NOT REVIEWED.)

*What changes vs p > 1 (G12 §2).* Exponents: none (|α|/2; L² margin (1+|α|)/4). Constants: 1/sin(πp/8) in L2.1′; a^{p−s} (γ < 0
always); C_n of L2.4–L2.5 through G3's constants (λ_δ, 1/|sin πδ| in κ_δ near t = 0, s_δ); the factor 2 from |G|. Geometry: lens and
sum-bound regions inside S_in resp. all sectors; poles of 𝒦_j = Hurwitz nodes (the Γ-poles t = δ − m sit on arg z = ±πp ⊂ S_out).
**What would fail:** as for p > 1, using D_W alone (exponent β′ = α + 2δ) gives |z|^{−|β′|/2}, not L² when |β′| ≥ 1 (e.g. p = ½,
s = 1.25: α = −½, δ = −0.9, β′ = −2.3); the cancellation of L2.3′ is essential; checked numerically by the control in [A].

## 2. Gap 3: E_plt1 Lemma F.1 with the complex seam densities

### 2.1 Setting and the majorant lemma
q(r) := e^{−2πnr^{−1/p}} ∈ (0, 1), ℓ(r) := −log(1 − q(r)) (E_plt1), and ℓ_±(r) := −Log(1 − e^{±2πiδ}q(r)) (G3 §2). Put θ := θ_seam = πp/2
and, with log D̃_δ := −j_δ(t),
  𝒢_δ(z) := −j_δ(t(z)) + log B_in^δ(z) + χ_δ(z) (z ∈ S_in),  𝒢_δ(z) := log B_out^δ(z) + χ_δ(z) (z ∈ S_out),
log B_in^δ = (ϖ_δ + 1)Log(1+z) − Log(1+λ_δz), log B_out^δ = (½ + δ)Log(1 − z/2πn); so H_n^δ = e^{−2𝒢_δ} on Z_n ⊂ S_in. At δ = 0 these are
E_plt1's 𝒢 and ℓ (ϖ₀ = ϖ, λ₀ = 1).

**Lemma M (majorants).** For r > 0 and −1 < δ < 0: (M1) ℓ_−(r) = conj ℓ_+(r); (M2) |ℓ_±(r)| ≤ ℓ(r); (M3) |ℓ_±′(r)| ≤ ℓ′(r);
(M4) |ℓ_±(r)| ≤ π + log(1/s_δ), s_δ := min_{q∈[0,1]}|1 − qe^{2πiδ}| > 0; (M5) ℓ_± is real-analytic on (0, ∞).
*Proof.* w := e^{±2πiδ}q has |w| = q < 1, so 1 − w lies in the right half-plane and −Log(1 − w) = Σ_{m≥1}w^m/m (the Taylor series of
the principal branch on the unit disc). (M1): conjugate the series. (M2): |Σw^m/m| ≤ Σq^m/m = ℓ. (M3): ℓ_±′ = e^{±2πiδ}q′/(1 − w),
q′ > 0, and |1 − w| ≥ 1 − q, so |ℓ_±′| ≤ q′/(1 − q) = ℓ′. (M4): s_δ ≤ |1 − w| ≤ 2 and |arg(1 − w)| < π/2; s_δ = |sin 2πδ| if
cos 2πδ ≥ 0, else 1, and sin 2πδ ≠ 0 when cos 2πδ > 0 and δ ∉ ℤ. (M5): composition of analytic maps with 1 − w ≠ 0. ∎ (PROVED.)
NUMERICAL (§4, [M]): (M1)–(M4) on 91 points r ∈ [10⁻³, 10⁶] × n ∈ {4, 40} × p ∈ {0.3, 0.6, 0.75} × δ ∈ {−0.02, −0.25, −0.5, −0.8, −0.98}.

**Lemma F.1_δ.** Let 0 < p < 1, −1 < δ < 0, R₁ := 4c + 2.
(i) 𝒢_δ is analytic in S_in and in S_out, has continuous boundary values on the open seams, is bounded near 0, and
  𝒢_δ,out − 𝒢_δ,in = ℓ_±(|ζ|) on Γ_± (= Σ^s_±).
(ii) For z ∉ Γ₊ ∪ Γ₋ ∪ {0}, with K(ζ, z) := (z − 1)/((ζ − z)(ζ − 1)),
  𝒢_δ(z) − 𝒢_δ(1) = (1/2πi)∫_0^∞[ℓ_+(r)e^{iθ}K(re^{iθ}, z) − ℓ_−(r)e^{−iθ}K(re^{−iθ}, z)]dr.   (F.1_δ)
(iii) For k ≥ 1, m_k(δ) := (1/2πi)∫_0^∞[ℓ_+(r)e^{iθ}(re^{iθ})^{−k−1} − ℓ_−(r)e^{−iθ}(re^{−iθ})^{−k−1}]dr is real and
  m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ),  S_k(δ) := Σ_{m≥1}sin(πkp/2 − 2πmδ)/m^{1+kp};  |m_k(δ)| ≤ (p/π)Γ(kp)ζ(1+kp)(2πn)^{−kp}.
(iv) For every K ≥ 1 there are C = C(p, K) and n₀ = n₀(p, K), **independent of δ**, such that for n ≥ n₀, |z| ≤ R₁ (boundary values on
  the seams included), |𝒢_δ(z) − 𝒢_δ(1) − Σ_{k=1}^K m_k(δ)(z^k − 1)| ≤ Cn^{−(K+1)p}; the derivative of the left side is ≤ Cn^{−(K+1)p}/η
  for |z| ≤ R₁ − η, dist(z, Γ₊ ∪ Γ₋) ≥ η; with E_n^δ(z) := 𝒢_δ(z) − 𝒢_δ(1) − m_1(δ)(z − 1): |E_n^δ| ≤ Cn^{−2p} on |z| ≤ R₁,
  |E_n^δ′(x)| ≤ Cn^{−2p} for real 0 < |x| ≤ R₁/2, E_n^δ extends continuously to 0, and |E_n^δ(x) − E_n^δ(0)| ≤ Cn^{−2p}|x|.
Hence log H_n^δ(z) − log H_n^δ(1) = −2m_1(δ)(z − 1) − 2E_n^δ(z), i.e. H_n^δ ∝ e^{−λ_n^δz}e^{−2E_n^δ}, λ_n^δ := 2m_1(δ).
(PROVED-mod-cite: as E_plt1 Lemma F.1 [Paper 2 Lemmas seam, corner; (eq:binet-bound); DLMF 5.2.1, 25.2.1 as quoted in RH/CITATIONS.md
"(DLMF-zeta, Plan 67)"], with G3 Lemma 3 [NOT REVIEWED] for the seam objects and G12 L1.2 for j_δ; DLMF 25.4.1 is no longer used.)
*Proof.* E_plt1's proof with the changes listed line by line in §2.2; every line not listed there is used verbatim. ∎

**Remark H (NUMERICAL; Hurwitz's formula NOT QUOTED).** m_k(δ) = ζ(−kp, 1+δ)/(kn^{kp}), i.e. λ_n^δ = 2ζ(−p, a)n^{−p}, μ^δ_{n,k} = 2m_k(δ) =
2ζ(−kp, a)/(kn^{kp}). Agreement to ≤ 10⁻²⁴ (relative) for k ≤ 3, p ∈ {0.3, 0.6, 0.75}, δ ∈ {−0.02, −0.25, −0.5, −0.8, −0.98} ([E]); the
controls (density with δ dropped; ζ(−kp, 1−δ)) fail (relative mismatch 0.06–25). This is the p < 1 counterpart of JZC_M3a_H.md Remark 3.3.

### 2.2 Line-by-line record: which lines of E_plt1 Lemma F.1 change

"verbatim" = the line holds as written with (𝒢, ℓ, j, B_in, B_out, χ) ↦ (𝒢_δ, ℓ_±, j_δ, B_in^δ, B_out^δ, χ_δ) and no other change.

| E_plt1 F.1, line | with δ | status |
|---|---|---|
| Setup: 𝒢 := −j + ϖLog(1+z) + χ (S_in), ½Log(1 − z/2πn) + χ (S_out); ℓ(r) := −log(1 − e^{−2πnr^{−1/p}}) > 0 | 𝒢_δ as in §2.1 (extra Möbius factor in B_in^δ, exponent ½ + δ in B_out^δ); two complex densities ℓ_± | **CHANGED** (definitions) |
| (i) analyticity in S_in: "−j(t) analytic (Lemma seam (i)), Log(1+z) analytic off (−∞,−1] ⊂ S_out, χ analytic off the seams" | −j_δ analytic on S_in (G3 Lemma 3 (i): Γ(t−δ)'s poles t = δ − m have arg t = π); Log(1+λ_δz) analytic off (−∞, −1/λ_δ] ⊂ S_out | **CHANGED** (one more factor; same reason) |
| (i) S_out: "1 − z/(2πn) ∉ (−∞, 0]" | same for the power ½ + δ | verbatim |
| (i) boundary values of χ (Lemma seam (iii)) | χ_δ: G3 Lemma 3 (iii) | verbatim |
| (i) jump: "𝒢_out − 𝒢_in = ½Log(1 − ζ/2πn) + χ₊ + j − ϖLog(1+ζ) = −Log(1 − e^{−2πit})" | = log B_out^δ + χ_+^δ + j_δ − log B_in^δ = −Log(1 − e^{−2πi(t−δ)}) (G3's χ_+^δ) | **CHANGED** (phase δ) |
| (i) "t = −i\|t\|, so e^{−2πit} = e^{−2π\|t\|} ∈ (0, 1) and the jump is ℓ(\|ζ\|)" | e^{−2πi(t−δ)} = e^{2πiδ}e^{−2π\|t\|}, modulus in (0, 1); the jump is ℓ_+(\|ζ\|) ∈ ℂ | **CHANGED** |
| (i) "Γ₋ by conjugation (χ₋(ζ̄) = conj χ₊(ζ))" | conjugation gives ℓ_− = conj ℓ_+ (M1): the two seams carry **different** densities | **CHANGED** (two densities) |
| (i) near 0: "j(t) → 0 by (eq. binet-bound); B_in, B_out → 1; χ bounded near 0 (Lemma corner (iii))" | j_δ → 0 by G12 L1.2(b) (φ = π/2); B_in^δ(0) = B_out^δ(0) = 1; χ_δ by corner (iii) with G3 Lemma 3 (ii) | **CHANGED** (citation for j_δ only) |
| (ii) statement (F.1) with ℓ on both seams | (F.1_δ): ℓ_+ on Γ₊, ℓ_− on Γ₋ | **CHANGED** |
| (ii) convergence: "ℓ(r) ≤ 2e^{−2πnr^{−1/p}} whenever … ≤ ½" and "ℓ(r) = O_n(1 + log r)" | \|ℓ_±\| ≤ ℓ (M2), then the same bounds (also \|ℓ_±\| ≤ π + log(1/s_δ), M4: bounded, better than ℓ) | **CHANGED** (via M2) |
| (ii) "the Sokhotski–Plemelj formula gives 𝒥_out − 𝒥_in = ℓ on both seams (density +ℓ on Γ₊, −ℓ on Γ₋…)", "ℓ is real-analytic" | the formula is linear in the density; ℓ_± real-analytic (M5); 𝒥_out − 𝒥_in = ℓ_± on Γ_± | **CHANGED** (complex density; same theorem) |
| (ii) "K₀ := 𝒢 − 𝒢(1) − 𝒥 continuous across, analytic (Morera)" | same | verbatim |
| (ii) "K₀ bounded near 0: 𝒢 is, by (i), and so is 𝒥 (\|ℓ\| ≤ 2e^{−2πnr^{−1/p}} near 0 …)" | \|ℓ_±\| ≤ ℓ (M2) | **CHANGED** (via M2) |
| (ii) growth on \|z\| = ρ ≥ 2: "−j(t), ϖLog(1+z), ½Log(1−z/2πn) are O_n(1 + log ρ) (binet-small for \|t\| < 1)" | −j_δ: G12 L1.2(c) (j_δ = (δ+½)ln t + O(1)) + continuity; log B_in^δ, log B_out^δ: O_n(1 + log ρ) (on S̄_in, Re(λ_δz) ≥ 0, so 1 ≤ \|1 + λ_δz\| ≤ 1 + λ_δρ) | **CHANGED** (j_δ's small-t form) |
| (ii) "χ and 𝒥 are Cauchy integrals of densities bounded by C_n(1 + log\|ζ\|) (Lemma corner (i); and ℓ)" | χ_±^δ: G3 Lemma 3 (ii); ℓ_±: (M2) | **CHANGED** (via M2) |
| (ii) Liouville; "K₀(1) = 0 (𝒥(1) = 0 since K(ζ, 1) = 0)" | same | verbatim |
| (iii) definition of m_k with ℓ | with ℓ_± | **CHANGED** |
| (iii) "on Γ₊, (re^{iθ})^{−k−1}e^{iθ} = r^{−k−1}e^{−ikθ}; on Γ₋ the conjugate. So m_k = −(sin(kθ)/π)∫ℓr^{−k−1}dr" | with (M1) the integrand is 2ir^{−k−1}Im(ℓ_+e^{−ikθ}); m_k(δ) = (1/π)∫_0^∞r^{−k−1}Im(ℓ_+(r)e^{−ikθ})dr — real, but **not** a multiple of sin kθ | **CHANGED** |
| (iii) substitution u = 2πnr^{−1/p} | same | verbatim |
| (iii) "−log(1 − e^{−u}) = Σe^{−mu}/m (non-negative terms, Tonelli)" | −Log(1 − e^{2πiδ}e^{−u}) = Σe^{2πimδ}e^{−mu}/m; terms complex: **Fubini**, with the absolutely convergent majorant Σ_m∫e^{−mu}u^{kp−1}du/m = Γ(kp)ζ(1+kp) < ∞ (the δ = 0 computation) | **CHANGED** (Tonelli → Fubini) |
| (iii) DLMF 5.2.1 (∫e^{−mu}u^{kp−1}du = Γ(kp)m^{−kp}) | same | verbatim |
| (iii) "= Γ(kp)ζ(1+kp) (DLMF 25.2.1); hence m_k = −(sin(πkp/2)/π)pΓ(kp)ζ(1+kp)(2πn)^{−kp}" | Im(e^{2πimδ}e^{−iπkp/2}) = −sin(πkp/2 − 2πmδ): m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ); \|S_k(δ)\| ≤ ζ(1+kp) (DLMF 25.2.1) | **CHANGED** (value) |
| (iii) DLMF 25.4.1 → ζ(−kp)/(kn^{kp}) | not available for δ ≠ 0; the identification with ζ(−kp, a)/(kn^{kp}) is Hurwitz's formula (NOT QUOTED): Remark H, NUMERICAL | **DROPPED** |
| (iv) Taylor expansion of K for \|ζ\| ≥ 2R₁ | same | verbatim |
| (iv) far part: "∫_{2R₁}^∞ℓr^{−K−2} ≤ ∫_0^∞ℓr^{−K−2} = n^{−(K+1)p}p(2π)^{−(K+1)p}Γ((K+1)p)ζ(1+(K+1)p)" | \|ℓ_±\| ≤ ℓ (M2): same bound, δ-free | **CHANGED** (via M2) |
| (iv) near part: "ℓ(r) ≤ 2e^{−2πnr^{−1/p}} …, ℓ′(r) = O(nr^{−1−1/p}e^{−2πnr^{−1/p}})"; near parts of m_k; z away from the seams | (M2), (M3) | **CHANGED** (via M2, M3) |
| (iv) z near/on a seam: "subtract ℓ(\|z*\|) on the window \|ζ − z*\| ≤ \|z*\|/2 and use \|ℓ′\|" | subtract the complex value ℓ_±(\|z*\|); its modulus ≤ ℓ(\|z*\|) (M2), \|ℓ_±′\| ≤ ℓ′ (M3); the window logarithm is the same | **CHANGED** (via M2, M3) |
| (iv) derivative away from the seams (Cauchy's estimate) | same | verbatim |
| (iv) real x: "\|∂_zK(ζ, x)\| ≤ C\|ζ\|^{−2} … times ℓ = O(e^{−2πn\|ζ\|^{−1/p}})" | times \|ℓ_±\| ≤ ℓ | **CHANGED** (via M2) |
| (iv) continuity at 0 ("density vanishing to infinite order at the corner") | (M2) | **CHANGED** (via M2) |
| (iv) E_n := 𝒢 − 𝒢(1) − ζ(−p)(z−1)n^{−p}; "H_n ∝ e^{−λ_nz}e^{−2E_n}, λ_n := 2ζ(−p)n^{−p}" | E_n^δ with m_1(δ); λ_n^δ := 2m_1(δ) | **CHANGED** |
| (iv) constants C(p, K), n₀ | every bound in (iv) uses ℓ_± only through (M2)–(M3), and (F.1_δ) itself: C, n₀ are δ-free | **NEW** observation |
| Remark (1) (zeta-regularised product, HEURISTIC) | formally −Σ_mlog(1 − x(m+δ)^p) ↦ Σ_k(x^k/k)ζ(−kp, 1+δ): consistent with Remark H; HEURISTIC, not used | (heuristic) |
| Remark (2) (checks) | replaced by `m3a_g23_F1.out` | — |
| Remarks (3)–(4) | (3) p ≥ 1 not applicable here; (4) asymptotic, not convergent (\|S_k\| ≤ ζ(1+kp), Γ(kp) growth) | verbatim |

So the G3 memo's "(iv) expected verbatim" is right for the *estimates*, but every line that touches ℓ changes (through M2–M3), and
(iii) changes its value; the moments that the circle jumps of H-e see are the Fourier sums of JZC_M3a_H.md §3.2. For p < 1 that
section's sentence "the seam integrals give the same Fourier sum" is now Lemma F.1_δ (iii) (PROVED-mod-cite, NOT REVIEWED).

## 3. Rule A (adversarial pass) — log

Gap 2.
1. *Is L2.1 really p-free?* Line-by-line (L2.1′). The only p-dependent quantities are 1/sin φ₁ = 1/sin(πp/8) (constant, → ∞ as p → 0)
   and the sign of γ (always < 0 for p < 1: one monotone case). Tested p ∈ {0.3, ½, ¾}: |U_{j2}| ≤ I₁ ≤ I₂ everywhere.
2. *Exponent shift.* Fitted exponent of |U_{j2}(iy)| is min(α, 0), not min(α + 2δ, 0) (control asserted to fail, δ ∈ {−½, −0.9}).
3. *Extra poles of 𝒦_j for p < 1?* The Γ-type points t = δ − m lie on arg z = ±πp ⊂ S_out; the lens sector has |arg z| < πp/4. Checked
   that R_{j2} is continuous across Hurwitz nodes with θ_δ, and that with the lattice θ the pole survives (control).
4. *(eq:imtheta)'s range 0 < arg z < min(π, πp)* is the binding p < 1 condition for the lens ray (ϑ_lip = πp/4 < πp): satisfied.
5. *G12 L2.2's arc constant* covers only |v| < ¼; the |v| ≥ ¼ case gives 1 − e^{−π/2} (Paper 2: "clear"). Corrected (c_arc = 0.7921).
6. *Seams near 0.* F_δ next to the seams (both sides) at |z| = 10⁻⁸: F_δ/F₀ → 1 ([O]). The proof uses corner (iii) for χ_δ.
7. *Seams at ∞.* No written lemma covered e^{χ} next to the seams at ∞ (Paper 2's (O5) paragraph asserts it; G3 quotes it). Lemma 2.5
   proves it for δ < 0 via |χ_+^δ′(ζ)| = o(1/|ζ|), which rests on the exact cancellation of the 1/ζ coefficients (the same identity as
   the decay of χ_±^δ). With Paper 2's lattice B_in, B_out at δ ≠ 0 the coefficient is δ/p ≠ 0 (G3 §0) and χ_+ would grow like log ζ
   — that is why the re-balanced B's are needed here too.
8. *δ → −1:* a^{p−s} in L2.1′, λ_δ → ∞ in G3; fixed δ fine. *δ → 0⁻:* s_δ ~ 2π|δ| and κ_δ's constant ~ 1/|sin πδ| blow up (H-d §3
   crossover); all statements are fixed-n, fixed-δ.
9. *Does Q♮ jump on the seams?* No: F_δ is analytic across (G3 L3 (iii)); U, φ, D_W, P₀^∞ have no seam jumps.
10. *Rule N.* mpmath's zeta(σ, b) avoided at large b (own EM tails, as G12); summation methods A/B cross-validated for p < 1, also at a
    small angle inside the lens ([X]). The near-seam Cauchy integrals use an exact subtraction of the density on [r*/2, 2r*]
    (G3's version only refined the quadrature).

Gap 3.
11. *Tonelli in (iii).* Fails for complex terms; replaced by Fubini with the δ = 0 series as majorant. Numerically the literal
    (iii)_δ integral equals the Fourier sum to ≤ 10⁻²⁰ ([E]).
12. *Are the majorants true?* (M2)–(M3) from the series / |1 − w| ≥ 1 − |w|; checked on grids, max |ℓ_±|/ℓ ≤ 1, max |ℓ_±′|/ℓ′ ≤ 1 ([M]).
13. *ℓ_± does not decay at ∞* (ℓ_±(∞) = −Log(1 − e^{±2πiδ}) ≠ 0; E_plt1's ℓ even grows like log r). The separate Cauchy integrals
    ∫ℓ_±dζ/(ζ − z) diverge logarithmically; only the subtracted kernel K of (F.1) converges — used as in E_plt1.
14. *Plemelj with a complex density* — linear, checked: 𝒥_out − 𝒥_in = ℓ_± across both seams to ≤ 10⁻¹³ (relative) ([P]).
15. *Reality of m_k(δ)* (needed for H_n^δ > 0 and real λ_n^δ): from (M1); numerically Im m_k ≤ 10⁻²⁰|m_k| ([E]).
16. *δ-uniformity of (iv).* Claimed from (M2)–(M3); checked: n^{(K+1)p}|res_K| at δ ∈ {−0.02, −½, −0.98} stays below the δ-free
    majorant 2(p/π)Γ((K+1)p)(2π)^{−(K+1)p}ζ(1+(K+1)p)·max|z^{K+1} − 1| ([R]). (ii) itself (𝒢_δ − 𝒢_δ(1) = 𝒥) has δ-dependent qualitative
    inputs only.
17. *Controls:* the real density (δ dropped) gives S_k(0) ≠ S_k(δ) (relative mismatch 0.06–25); ζ(−kp, 1−δ) in place of ζ(−kp, 1+δ) fails. (A first
    version used ζ(−kp, −δ), which coincides with ζ(−kp, 1+δ) at δ = −½ — a vacuous control; replaced.)
18. *Möbius factor.* B_in^δ's pole −1/λ_δ lies in S_out, where 𝒢_δ uses B_out^δ: no singularity of 𝒢_δ in |z| ≤ R₁. (ii) at points next
    to the seams with the literal 𝒢_δ (χ_δ from G3's densities) equals 𝒥 ([G]).
19. *Rule X:* nothing fitted. The Fourier sums are computed from the Hurwitz *series* at rational δ (residue classes), independently of
    mpmath's analytic continuation ζ(−kp, a), which enters only Remark H.

## 4. Numerical checks (Rule N: NUMERICAL, not certified)

Both scripts use `spec_common.Checks`; every pass/fail value is computed. Precision: dps 40 (summation engine), dps 30 (seam and
F.1 quadratures). n = 4 unless stated.

`checks/m3a_g23_apriori.out` — **ALL 132 CHECKS PASSED** (≈ 35 min wall on 2 cores).
- [X] summation methods A (direct + exact Hurwitz tails) and B (Euler–Maclaurin) agree for p < 1 to ≤ 1.5·10⁻³⁹, including at
  arg z = πp/16 inside the lens.
- [A] L2.1′ at (p, s) ∈ {(½, 1.25), (½, 1.8), (¾, 1.375), (0.3, 1.15), (0.3, 1.45)} × δ ∈ {0, −½, −0.9}, both U_{j1} (= π_n, π_{n−1} of
  σ^δ), |z| ∈ {1, 10⁻², 10⁻⁴, 10⁻¹⁶, 10⁻²⁴} × arg z ∈ {πp/8, π/2, π}: |U_{j2}| ≤ I₁ (max ratio 0.108) and I₁ ≤ I₂ everywhere. Exponent
  of |U_{j2}(iy)| from 10⁻¹⁶ to 10⁻²⁴: −0.5 (α = −½) to 10⁻⁸, and |·| ≤ 3·10⁻⁹ (α > 0), for every δ; the control exponent
  min(α + 2δ, 0) (−1.5, −2.3, −0.4, −1.2, −1.3) is asserted to fail and fails.
- [L](b) inside the lens (arg z = πp/16): same exponents. [L](a) R_{j2} continuous across X_k (k ∈ {5, 40} resp. {3, 12}) at
  (p, s, δ) = (½, 1.25, −½), (¾, 2.125, −0.9), (0.3, 1.15, −¼): relative jump ≤ 1.2·10⁻¹¹ (ε = 10⁻¹²) while the Cauchy sum jumps by
  6·10¹⁰–10¹¹; CONTROL with the lattice θ: jump ≥ 3·10⁹·|R| (fails, as it must). [L](c) c_arc = 0.79212 on all arc samples.
- [O] p ∈ {0.3, 0.6} × δ ∈ {−¼, −0.8}: max|F_δ/F₀ − 1| over 8 off-lens angles (4 of them at angular distance 10⁻⁸ from a seam, both
  sides; S_out incl. arg z = 0.95π) and |F̃_δ/F₀ − 1| at 3 lens angles: ≤ 2.3·10⁻⁵ at |z| = 10⁻⁴, ≤ 2.3·10⁻⁹ at 10⁻⁸ (linear in |z|).
- [W] same (p, δ): next to the seams (angular distance 10⁻⁸, both seams, both sides) max|χ_δ| ≤ 0.75 on |z| ∈ [1, 10⁵], ≤ 6.8·10⁻⁸ at
  10⁸ and ≤ 6.8·10⁻¹² at 10¹² (decay ∝ |z|^{−1}); |F_δ(−z)^{−δ}/(2πn)^{−½−δ} − 1| ≤ 3·10⁻¹² at 10¹²; Plemelj χ_out − χ_in = χ_+^δ at
  |z| = 10³ to ≤ 7·10⁻²³.

`checks/m3a_g23_F1.out` — **ALL 398 CHECKS PASSED** (≈ 20 min).
- [M] (M1)–(M4) on 91 log-spaced r ∈ [10⁻³, 10⁶] × n ∈ {4, 40} × p ∈ {0.3, 0.6, 0.75} × δ ∈ {−0.02, −¼, −½, −0.8, −0.98}:
  max|ℓ_±|/ℓ = 1, max|ℓ_±′|/ℓ′ = 1 (equality as q → 0), ℓ₋ = conj ℓ₊ to 10⁻²⁵.
- [E] (iii)_δ at n = 7, k ≤ 3, same p × δ grid: literal seam integral = Fourier sum (S_k from the Hurwitz series by residue classes) to
  ≤ 4·10⁻²⁶ relative; Im m_k ≤ 10⁻²⁰|m_k|; |S_k(δ)| ≤ ζ(1+kp); Remark H (mpmath ζ(−kp, 1+δ)) to ≤ 4·10⁻²⁶; two controls fail.
- [P] p ∈ {0.3, 0.6} × δ ∈ {−¼, −0.8}: 𝒥_out − 𝒥_in = ℓ_± across both seams at |z| ∈ {½, 3, 40}, relative error ≤ 1.1·10⁻¹³ (floor 10⁻⁶
  where ℓ underflows).
- [R] (iv)_δ, K ∈ {1, 2}, n ∈ {10, 40, 160, 640}, δ ∈ {−0.02, −½, −0.98}; z ∈ {½, −1.3, 2e^{iθ/2}, 1.5e^{0.8πi}, both boundary values at
  2e^{iθ}, 2e^{−iθ} (outer side)} (+ 6e^{0.9πi}, 6e^{iθ/3} at p = 0.6): sup_z n^{(K+1)p}|res_K| stable in n (e.g. p = 0.6, δ = −½, K = 1:
  0.435, 0.555, 0.557, 0.551) and below the δ-free majorant; n^{(K+2)p}|res_K − m_{K+1}(z^{K+1} − 1)| stable or decreasing (next order);
  max|res_K/(m_{K+1}(z^{K+1} − 1)) − 1| decreases with n, to 0.007–0.28 (p = 0.6) and 0.13–0.38 (p = 0.3) at n = 640 — slow at p = 0.3
  because the series is asymptotic in |z|(2πn)^{−p} (Remark (4)).
- [D] p = 0.6, δ ∈ {−½, −0.98}: max_x n^{2p}|E_n^δ(x) − E_n^δ(0)|/|x| over x ∈ {0.01, 0.3, −0.01, −2, 3} = 0.047 resp. 0.083, flat in
  n ∈ {20, 80, 320}.
- [G] (ii)_δ with the literal 𝒢_δ (χ_δ by quadrature of G3's χ_±^δ): |𝒢_δ(z) − 𝒢_δ(1) − 𝒥(z)| ≤ 9·10⁻²⁷ at 6 points, 4 of them at angular
  distance 10⁻⁸ from a seam (both sides), (p, δ) ∈ {(0.6, −½), (0.3, −0.8)}.

*Rule N notes.* A first run of the F.1 script had 42 failing assertions, all numerical artefacts, now fixed: ℓ_± evaluated as
−log((1 − Q) − Q·expm1(−y)) loses all digits when q underflows (amplified by r^{−k−1} in the moment integrals) — replaced by
−log1p(−Qq); the ζ(−kp, −δ) control was vacuous at δ = −½; the ratio tolerance in [R] was too tight at p = 0.6, K = 2 (S₃ is small:
sin(0.9π)), loosened from 0.1 to 0.4 and supplemented by the next-order check. No assertion was removed.

## 5. What remains

- **Rule R** for everything here, and for its inputs G3 Lemma 3, Prop 4, Cor 5 and G12 L1.2 (all NOT REVIEWED).
- Theorem H, item 1 of JZC_M3a_H.md §4 (the n-uniform hard-edge comparison with Szegő exponent β′, in the α-frame of L2.3/L2.3′): not
  touched. Item 4 (H-a written out): not touched. With this note, items 2 and 3 are closed modulo review for 0 < p < 1, −1 < δ < 0.
- Hurwitz's formula remains NOT QUOTED; the band factor is stated with the Fourier sums S_k(δ) (F.1_δ (iii)).
- The constants of L2.4–L2.5 are fixed-n; n-uniform versions are part of item 1.
- **For FIXES (via a human; Rule 1):** Paper 2, Lemma seam (iv), (O5) "near ∞": "In S_in ∩ {|z| ≥ n^p+δ′} … D, B_in, K and e^χ are bounded
  above and below by powers of |z|". For e^χ next to the seams this needs the window argument of Lemma corner (iii) at ∞ (corner (ii)
  needs dist ≥ τ₀|z|, (iii) is stated on U(0, 1)). Lemma 2.5 is that argument for δ < 0; for δ = 0 it needs |χ_±′(ζ)| = o(1/|ζ|), which
  should follow in the same way from (eq:binet-small) (with a derivative bound for its remainder) — not written here. The result is
  unaffected.
- Internal corrections: G12 L2.2's arc constant (§1, L2.2′ (4)); G3 §4 "F.1 (iv) expected verbatim": confirmed for the estimates, with the
  line changes of §2.2, and (iii)'s value is the Fourier sum (as JZC_M3a_H.md §3.2 already states).
- Not covered: δ > 0 (phantom nodes); p = 1 with δ ≠ 0; δ = 0 is Paper 2 / E_plt1.
