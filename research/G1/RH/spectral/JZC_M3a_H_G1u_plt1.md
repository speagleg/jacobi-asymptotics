# JZC M3a, Theorem H item 1 for 0 < p < 1: the glued Hurwitz hard-edge parametrix in the α-frame, and the n-uniform comparison

Rule R review B: L P1, P2, P4, P5, §3a ACCEPT; L P3, Prop G1u′ (A), (B) and the checks ACCEPT WITH FIXES
(research/G1/review/REVIEW_JZC_M3a_H_plt1_G1up_B.md); fixes P1-1, P3-1, G-1, N-1 – N-4 applied 2026-10-22.
Status (2026-10-22): L P1–P5 and Prop G1u′ (A), (B) are **REVIEWED** (Rule R: review B re-derived every lemma and re-ran both checks
byte-identically, the end-to-end one with regenerated caches; fixes applied). Their inputs G3 and G23plt1 are REVIEWED (Rule R review
B, REVIEW_JZC_M3a_H_plt1_inputs_B.md); JZC_M4_proof Theorem N.6 / N.6a–c is PROVED-mod-cite with review A done, second reader pending.
Labels per VERIFICATION_POLICY.md. Novelty: UNCHECKED.
This note closes the last open p < 1 part of item 1 of JZC_M3a_H.md §4. That part has two pieces:
- rebuilding E_plt1's glued global parametrix with the α-frame factor W̃♮ (Szegő exponent β′ = α + 2δ, Bessel order α);
- the n-uniform hard-edge comparison and the order-K small-norm expansion for the Hurwitz problem when **0 < p < 1, −1 < δ < 0,
  1 < s < 1 + 2p**.

Inputs. Everything attributed to Paper 2 is quoted from papers/paper2/{sec_6,sec_7,app_b,app_outer}.tex as read for this note
(read-only; nothing there was edited). The p > 1 proof is JZC_M3a_H_G1u.md ("G1u"). The p < 1 objects come from:
- G3: JZC_M3a_H_G3.md;
- G23plt1: JZC_M3a_H_G23plt1.md (P2.6, Lemma M, Lemma F.1_δ);
- E_plt1: second_order/E_plt1.md, and RH_plt1b: plt1/RH_plt1b.md (both REVIEWED for δ = 0).

No external theorem is quoted here that is not already quoted, with its hypotheses, in a cited repo note (Rule C):
- the Bessel/Airy facts are JZC_M4_proof N.6a's (DLMF 10.17, 10.40, 9.7);
- the Mellin/ζ facts are F.1_δ's (DLMF 5.2.1, 25.2.1);
- KMVV's angle freedom is RH_plt1b's.

Checks:
- `checks/m3a_g1up_hardedge.py/.out` (the glued parametrix with the **actual** seam band factor);
- `checks/m3a_g1up_endtoend.py/.out` (fits of the actual Hurwitz Jacobi coefficients at p < 1, β′ ≤ −1).

Counts are in §5.

| # | Statement | Label |
|---|---|---|
| L P1 | n-uniform, δ-uniform bounds on the seam band factor on the whole disc \|z\| ≤ R₁, both sectors, seams (boundary values) included. (a) 𝒢_δ(z) − 𝒢_δ(x) = (z − x)I(z, x). (b) \|I − Σ_{k≤K}m_kq_k\| ≤ C_Kn^{−(K+1)p}. (c) \|𝒢_δ(z) − 𝒢_δ(0) − Σ_{k≤K}m_kz^k\| ≤ C_Kn^{−(K+1)p}\|z\|. (d) L_h := log(D_{h°}²/h°) satisfies \|L_h − 𝓡M_μ\| ≤ 2C_Kn^{−(K+1)p}\|𝓡\| | PROVED-mod-cite (G23plt1 F.1_δ (i)–(iii), Lemma M; Paper 2 (eq:szego), (eq:szego-repr); E3 L E3.4 (arcsine moments)) |
| L P2 | ρ♮ := W̃♮/D_W for the glued W̃♮ = (𝗐_n(−z)^{β′}(4c − z))^{1/2}e^{−𝒢_δ}. (i) ρ♮ = ρ♮^{mod}e^{−L_h/2}, \|log(ρ♮/ρ♮^{mod})\| ≤ Cn^{−p}\|z\|^{1/2}, \|ρ♮\|^{±1} ≤ C (n-free, δ-free). (ii) Exact lip match ϱ_±ρ♮^{−2} = ω♮. (iii) ρ♮₊ρ♮₋ = 1 on the band. (iv) No jump on (−δ₀, 0). (v) Glue ρ♮_out = ρ♮_in·e^{−ℓ_±(\|z\|)} on the seams | PROVED-mod-cite (L P1; G1u L1 (i)–(iii), (v); Paper 2 (eq:DW-factor); G23plt1 F.1_δ (i)) |
| L P3 | the glued Hurwitz parametrix P̂₀♮ = Â♮(2πn)^{σ₃/2}Φ_α(n²f)ρ♮^{−σ₃}. (i) Â♮ = Â^{mod}(I + 𝔈) with Â^{mod} analytic and n-free, \|𝔈\| ≤ Cn^{−p}: \|Â♮^{±1}\| ≤ C n-free, seams included. (ii) Exact band and lip jumps, none on (−δ₀, 0); glue jump on the seams \|J_g − I\| ≤ Cn\|z\|^{−3/2}e^{−2πn\|z\|^{−1/p}}. (iii) Circle expansion I + Σ_{k≤K}Δ_k♮n^{−k} + O(n^{−K−1}) uniformly, seam crossings included. (iv) Bessel-scale size n^{1/2}\|ζ\|^{−\|α\|/2} | PROVED-mod-cite (L P1, L P2; G1u L2 (iii)–(iv) proofs; E_plt1 L E′.3 (sectors); Paper 2 L bessel-local, L comparison-parametrix) |
| L P4 | lip mismatch \|ω♮ − ϱ_±\| ≤ C\|z\|^{1/2} (n-free); fixed-n identification: R := Q♮P̂₀♮^{−1} has \|R\| ≤ C_{n,η}\|z\|^{−\|α\|−η}, is bounded near 0 up to a log, R_± ∈ I + ∂𝒞(L²) | PROVED-mod-cite (L P2, L P3; G23plt1 P2.6; Paper 2 L supersmall, L B-cauchy (c)) |
| L P5 | the band-factor gauge (H-c) for p < 1 in the α-frame: Δ_k♮ = G_{μ^δ_n}Δ_k^{mod,β′}G_{μ^δ_n}^{−1} + O(n^{−(J+1)p}) on both circles, seam crossings included; μ^δ_{n,j} = 2m_j(δ). An independent proof of JZC_M3a_H_Hc.md Lemma Hc.5 (NOT REVIEWED before Rule R review B; fixed per Rule R review B, G-1), via L P1 (d) on the whole disc | PROVED-mod-cite (L P1 (d); E3 L E3.4 [REVIEWED]; JZC_M4_proof N.6a formulas) |
| **Prop G1u′** | p < 1. (A) Paper 2 §7 holds verbatim for Q♮, with L P4 in place of L lip-mismatch. (B) The order-K small norm (N.6c) holds for the Hurwitz problem in the α-frame with the glued P̂₀♮, remainder O(n^{−K−1} + n^{−1−(J+1)p}). This is Theorem N.6's chain for M(β′, ν = α) with gauge μ^δ_n | (A), (B) PROVED-mod-cite + REVIEWED (inputs §4: H-a, G3, G23plt1 REVIEWED; JZC_M4_proof N.6a–c review A done, second reader pending) (updated per Rule R review B, C-11 of REVIEW_JZC_M3a_H_assembly_B.md) |
| §3a | exactly which lines of RH_plt1b §2 / E_plt1 §0, E′.3, E′.5, E′.5′ / JZC_M4_proof N.6a–c (p < 1 parts) / G1u L1–L4 change | (record) |
| §5 | numerics. Hard edge: L P1–P4 with the actual seam band factor, matching rate in n at β′ down to −2.2, gauge, controls. End-to-end: p = 0.6, 0.75, β′ = −2.1, −1.5 | NUMERICAL |

## 0. Answer

Item 1 closes for 0 < p < 1, −1 < δ < 0, 1 < s < 1 + 2p (|α| < 1). There is no loss in the error exponents, and the proof is
shorter than for p > 1. The reason is one identity, **Lemma P1 (a)**. The glued seam exponent 𝒢_δ of G23plt1 §2.1 (H_n^δ = e^{−2𝒢_δ}
on Z_n) has, by G23plt1's Cauchy-integral representation (F.1_δ), the exact difference quotient

  𝒢_δ(z) − 𝒢_δ(x) = (z − x)·I(z, x),  I(z, x) = (1/2πi)∫_0^∞[ℓ_+(r)e^{iθ}/((ζ₊ − z)(ζ₊ − x)) − ℓ_−(r)e^{−iθ}/((ζ₋ − z)(ζ₋ − x))]dr,

with ζ_± = re^{±iθ} on the seams. Moreover |I| ≤ Cn^{−p} uniformly in **both** sectors, on the seams (boundary values), for
|z| ≤ R₁ and x ∈ [0, 4c], with C = C(p) δ-free.

Inserted into Paper 2's Szegő representation (eq:szego-repr), whose constant 𝔠 may be **any** number, so the sector value of log h° at
z is allowed, this gives

  L_h(z) := log(D_{h°}(z)²/h°(z)) = (2𝓡(z)/π)∫_0^{4c}I(z, x)dx/√(x(4c − x)),   so   |L_h(z)| ≤ Cn^{−p}|𝓡(z)| ≤ C′n^{−p}|z|^{1/2},

and to every order the same with the gauge 𝓡M_μ subtracted (L P1 (d)). Hence, on the whole disc and across the seams:
- the glued ρ♮ = W̃♮/D_W equals the n-free model ρ♮^{mod} = (Υ̂/4c)^{(1+β′)/2} times e^{−L_h/2} = 1 + O(n^{−p}|z|^{1/2});
- the matching factor equals Â♮ = Â^{mod}(I + O(n^{−p})), because the |z|^{1/2} in L_h exactly absorbs the |f|^{−1/2} of the
  conjugation by f^{σ₃/4}.

Three consequences:
- **No Cauchy splitting is needed.** RH_px L4.2(iii)'s split Ẽ = E^a + Φ (used by RH_plt1b and E_plt1 for the glue), and G1u
  L2 (i)'s maximum-principle step, are replaced by this factorisation.
- **No derivative bound on E_n is needed.** E_plt1 L E′.3 and E3 L E3.5 used a window argument at the two points where the circles
  meet the band; L P1 (d) bounds the whole disc instead.
- **No (O3)–(O4) n-uniform Hölder bound is needed.** G1u L1 (iv) used G12 P1.4 (a) and Paper 2 L szego (ii); here they are not
  used.

β′ enters only through ρ♮^{mod}, as for p > 1. The glue jump of W̃♮ on the seams is e^{−ℓ_±} = 1 − e^{±2πiδ}e^{−2πn|z|^{−1/p}}. This is
RH_plt1b's 1 − e^{∓2πit} with t ↦ t − δ: complex, but of the same modulus, hence super-small with polynomial amplification.

**What the brief anticipated vs what happened.** G1u §3 expected "no new exponent issue" from the glue. That is confirmed, with a
correction: the amplification of the glue jump in the Q-frame is polynomial, n|z|^{−3/2} (L P3 (ii)). It is not E_plt1's
e^{Cn|z|^{1/2}}, which belongs to the classical frame.

**One structural difference from p > 1.** For p < 1 there is **no** jump on (−δ_r, 0) at all: 𝒢_δ is analytic there in S_out. The
p > 1 construction has the super-small h_n^δ jump there. In exchange, the glue jumps sit on the two seam segments.

**Overlap with JZC_M3a_H_Hc.md.** That memo (JZC_M3a_H_Hc.md Lemma Hc.5 (NOT REVIEWED before Rule R review B); fixed per Rule R
review B, G-1) states Lemma Hc.5, the H-c gauge for p < 1
given F.1_δ (iv). It uses the derivative/window argument at the band-crossing points of the circles. L P5 below is an independent
proof of the same statement from L P1 (d). Either closes H-c for p < 1.

## 1. Setting and notation

Throughout:
- **Parameters.** 0 < p < 1, −1 < δ < 0, a = 1 + δ, 1 < s < 1 + 2p, α = (s − 1 − p)/p ∈ (−1, 1), β′ = α + 2δ ∈ (−3, 1),
  c = c(p), R₁ := 4c + 2.
- **Seams.** θ := πp/2 (the seam angle), Γ_± := {re^{±iθ}: r > 0} oriented outward, S_in := {|arg z| < θ},
  S_out := ℂ ∖ (S̄_in ∪ {0}). Lips at ±θ_L, θ_L = πp/4 (Paper 2 (eq:thetaw), p < 1); KMVV rays at π − θ_L (RH_plt1b §2).
- **Seam densities.** q(r) := e^{−2πnr^{−1/p}}, ℓ(r) := −log(1 − q(r)), ℓ_±(r) := −Log(1 − e^{±2πiδ}q(r)) (G23plt1 §2.1, Lemma M:
  ℓ₋ = conj ℓ₊, |ℓ_±| ≤ ℓ, |ℓ_±′| ≤ ℓ′).
- **Band factor.** 𝒢_δ := −j_δ(t) + log B_in^δ + χ_δ on S_in and log B_out^δ + χ_δ on S_out (G23plt1 §2.1, built on G3 §2), so
  H_n^δ = e^{−2𝒢_δ} on Z_n ⊂ S_in.
  - F.1_δ (i)–(iv) (G23plt1): 𝒢_δ,out − 𝒢_δ,in = ℓ_± on Γ_±.
  - The representation (F.1_δ).
  - The moments m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ) (real).
  - 𝒢_δ is bounded near 0, with one limit 𝒢_δ(0) from every sector; 𝒢_δ(0) = χ_δ(0) is real (G3 Lemma 3 (iii):
    H_n^δ(0⁺) = e^{−2χ_δ(0)}).
- **Gauge.** μ_k = μ^δ_{n,k} := 2m_k(δ), Q_k(z) := Σ_{j<k}z^{k−1−j}C(2j, j)c^j, M_μ := Σ_{k≤K}μ_kQ_k (E3 §3).
  G_μ := P₀^∞e^{−𝓡M_μσ₃/2}(P₀^∞)^{−1} (E3 L E3.4 (ii)). q_k(z, x) := Σ_{j<k}z^{k−1−j}x^j = (z^k − x^k)/(z − x).
- **Frame 1 of H-d** (G3 Cor 5 for p < 1): Q♮ := D_∞^{−σ₃}V♮D_W^{σ₃}.
  - D_W is the Szegő function of W₀^{(β′)} := 𝗐_nx^{β′}(4c − x)H_n^δ.
  - ω^{(β′)} := D_W²/W₀^{(β′)}, ω♮ := ω^{(β′)}e^{±2πiδ} in ℂ_± (on the lips), ϱ_± := e^{∓iπα}.
  - Q♮ has no jump on the seams (F_δ is analytic across them: G23plt1 L2.3′) and none on (−∞, 0).
  - Its lip jump is [[1, 0], [ω♮e^{2nφ}, 1]] + E (H-d Lemma (ii); G3 Cor 5).
  - f, φ, P₀^∞, M, Φ_α, Ψ_α are as in G1u §2 (lattice f from μ*, all p > 0).
- **Discs.** δ_r is Paper 2's hard-edge radius (fixed, small), δ₀ := 2δ_r ≤ min(1, c/2), with f conformal on U(0, δ₀). U_0 := U(0, δ_r).
- **Szegő objects.** h° := H_n^δ/H_n^δ(0⁺) on the band. Its sector-wise continuation is h°(z) := e^{−2(𝒢_δ(z) − 𝒢_δ(0))}, with log h°
  equal to that exponent. L_h(z) := log D_{h°}(z)² − log h°(z) for z ∉ [0, 4c] ∪ Γ_±, where log D_{h°}² is the exponent in Paper 2
  (eq:szego).
- 𝔇 := {0 < |z| ≤ R₁} ∖ (Γ₊ ∪ Γ₋). "Boundary values" means the limits from either side of Γ_±.

## 2. The lemmas

### 2.1 Lemma P1 (the seam band factor, n- and δ-uniformly, on the whole disc)

**Lemma P1.** Fix 0 < p < 1. There are n₀ = n₀(p) and, for each K ≥ 0, C_K = C(p, K), **independent of δ ∈ (−1, 0)**, such that the
following holds for n ≥ n₀, z ∈ 𝔇 (boundary values on Γ_± included) and x ∈ [0, 4c].
(a) 𝒢_δ(z) − 𝒢_δ(x) = (z − x)I(z, x), with I as in §0. At x = 0 this uses the common limit 𝒢_δ(0); the integral converges
  absolutely, and on the seams it is the boundary value.
(b) With I_K := I − Σ_{k=1}^Km_k(δ)q_k(z, x) (I₀ = I): |I_K(z, x)| ≤ C_Kn^{−(K+1)p}.
(c) |𝒢_δ(z) − 𝒢_δ(0) − Σ_{k≤K}m_k(δ)z^k| ≤ C_Kn^{−(K+1)p}|z|. In particular |log h°(z)| ≤ 2C₀n^{−p}|z|.
(d) For z ∈ 𝔇 ∖ [0, 4c]: L_h(z) = 𝓡(z)M_μ(z) + (2𝓡(z)/π)∫_0^{4c}I_K(z, x)dx/√(x(4c − x)). Hence
  |L_h(z) − 𝓡(z)M_μ(z)| ≤ 2C_Kn^{−(K+1)p}|𝓡(z)|. For K = 0: |L_h(z)| ≤ 2C₀n^{−p}|𝓡(z)| ≤ C′n^{−p}|z|^{1/2} for |z| ≤ δ₀.

*Proof.* (a) F.1_δ (ii) gives 𝒢_δ(w) − 𝒢_δ(1) = (1/2πi)∫_0^∞[ℓ_+e^{iθ}K(ζ₊, w) − ℓ_−e^{−iθ}K(ζ₋, w)]dr for w ∉ Γ₊ ∪ Γ₋ ∪ {0}, with
K(ζ, w) = 1/(ζ − w) − 1/(ζ − 1).
- Apply it at w = z and w = x ∈ (0, 4c] (real positive, hence off the seams) and subtract. Since
  K(ζ, z) − K(ζ, x) = (z − x)/((ζ − z)(ζ − x)), this is (a).
- Absolute convergence: (B1) and (B3) below; ℓ = O(1 + log r) at ∞.
- Boundary values: both sides have continuous boundary values on the open seams. For the left side this is F.1_δ (i). For the right
  side it is the Sokhotski–Plemelj formula with the real-analytic density ℓ_±(|ζ|)/(ζ − x), as in F.1_δ (ii).
- x → 0⁺: 𝒢_δ is continuous at 0 from S_in (F.1_δ (iv)), and the integrand converges dominatedly by (B1).

(b) Elementary bounds:
- (B1) For ζ ∈ Γ_± and x ≥ 0, |ζ − x| ≥ |ζ|sin θ. The distance from re^{±iθ} to [0, ∞) is r sin θ, since θ < π/2.
- (B2) Choose n₀ with q(2R₁) ≤ ½. Then on (0, 2R₁]: ℓ ≤ 2q, and ℓ′ = q′/(1 − q) ≤ 2q·y/(pr) with y := 2πnr^{−1/p}. Since
  r^{−m} = (y/(2πn))^{mp} and y^ae^{−y/2} ≤ (2a/e)^a, every r^{−m}ℓ(r) and r^{−m+1}ℓ′(r) on (0, 2R₁] is
  ≤ C_me^{−c₁n}, c₁ := π(2R₁)^{−1/p}.
- (B3) Let τ := ⅕sin θ. If dist(z, Γ₊ ∪ Γ₋) ≥ τ|z|, then |ζ − z| ≥ (τ/3)(|ζ| + |z|) for ζ on either seam. Proof: if |ζ| ≥ 2|z|,
  then |ζ − z| ≥ |ζ|/2 ≥ (|ζ| + |z|)/3; otherwise |ζ − z| ≥ τ|z| ≥ τ(|ζ| + |z|)/3.
- *Far part* (r ≥ 2R₁, where |z|, x ≤ R₁ ≤ r/2).
  - 1/((ζ − z)(ζ − x)) = Σ_{k≥1}ζ^{−k−1}q_k(z, x) converges absolutely, with |q_k| ≤ kR₁^{k−1}. The tail after K terms is
    ≤ Σ_{k>K}kR₁^{k−1}r^{−k−1} ≤ C_Kr^{−K−2}.
  - The same expansion, integrated against ℓ_±e^{±iθ}, gives exactly the far parts of the m_k (definition of m_k in F.1_δ (iii)).
  - So |far part of I_K| ≤ (C_K/π)∫_{2R₁}^∞ℓ(r)r^{−K−2}dr ≤ (C_K/π)p(2πn)^{−(K+1)p}Γ((K+1)p)ζ(1+(K+1)p). This uses Lemma M (M2) and
    the Mellin computation of E_plt1 F.1 (iii)/(iv), far part.
  - For K = 0 there is nothing to subtract: |far part of I| ≤ (4/π)∫ℓr^{−2}dr ≤ C₀n^{−p}, using |ζ − z|, |ζ − x| ≥ r/2.
- *Near part of m_k* (r < 2R₁): |·| ≤ (1/π)∫_0^{2R₁}ℓr^{−k−1}dr ≤ C_ke^{−c₁n} by (B2). It is multiplied by |q_k| ≤ kR₁^{k−1}.
- *Near part of I*, N(z, x) := Σ_±(±1/2πi)∫_{Γ_±∩{|ζ|<2R₁}}g_±(ζ)dζ/(ζ − z), with g_±(ζ) := ℓ_±(|ζ|)/(ζ − x).
  - *Case A*, dist(z, Γ₊ ∪ Γ₋) ≥ τ|z|: by (B1), (B3), |N| ≤ (3/(πτ sin θ))∫_0^{2R₁}ℓ(r)r^{−2}dr ≤ Ce^{−c₁n}.
  - *Case B*, dist(z, Γ₊) < τ|z| (Γ₋ is symmetric). Let z* = r*e^{iθ} be the foot of the perpendicular. Then
    (1 − τ)|z| ≤ r* ≤ (1 + τ)R₁ and |z − z*| ≤ r*/4. Let 𝒲 := {ζ ∈ Γ₊: |ζ − z*| ≤ r*/2} ⊂ {|ζ| ≤ 1.8R₁}.
    - On 𝒲, write g₊(ζ) = g₊(z*) + (g₊(ζ) − g₊(z*)).
    - The constant contributes g₊(z*)[Log(ζ − z)] between the ends. These are at distances in [r*/4, 3r*/4] from z, and the argument
      changes by less than π, so the contribution is ≤ |g₊(z*)|(log 3 + π).
    - The remainder is ≤ r*·sup_𝒲|g₊′|, since |ζ − z| ≥ |ζ − z*| (z − z* ⊥ Γ₊).
    - Here |g₊| ≤ ℓ(ρ)/(ρ sin θ) and |g₊′| ≤ ℓ′(ρ)/(ρ sin θ) + ℓ(ρ)/(ρ sin θ)², with ρ = |ζ| ∈ [r*/2, 3r*/2]. These use (M2), (M3) and
      (B1): d/dζ ℓ₊(|ζ|) = e^{−iθ}ℓ₊′.
    - By (B2) the window is ≤ Ce^{−c₁n}.
    - Off 𝒲 on Γ₊: |ζ − z| ≥ |ζ − z*| − r*/4 ≥ |ζ − z*|/2 and, ζ and z* lying on one ray with ||ζ| − r*| ≥ r*/2,
      |ζ − z*| ≥ (|ζ| + r*)/5, (fixed per Rule R review B, P1-1) ≥ (|ζ| + r*)/12, which gives ≤ Ce^{−c₁n}.
    - On Γ₋: the angle between z and Γ₋ is ≥ 2θ − arcsin τ ≥ θ, so |ζ − z| ≥ sin(θ/2)(|ζ| + |z|), which gives ≤ Ce^{−c₁n}.
  - No constant depends on dist(z, Γ₊), so the bound holds for the boundary values.
- Collecting: |I_K| ≤ C_Kn^{−(K+1)p} + C(1 + Σ_{k≤K}kR₁^{k−1})e^{−c₁n}, which is (b) after enlarging C_K. ℓ_± entered only through
  (M2), (M3), and θ, τ, R₁, c₁ depend only on p, so C_K, n₀ are δ-free.

(c) Take x = 0 in (a), (b); q_k(z, 0) = z^{k−1}.

(d) Paper 2 (eq:szego-repr) is stated "for every z ∉ [0, 4c] and every number 𝔠". Apply it to q := h° on (0, 4c) with
𝔠 := log h°(z), the sector value at z.
- h° is positive on (0, 4c), and log h° = −2(𝒢_δ − 𝒢_δ(0)) is real there: ℓ₋ = conj ℓ₊ and (F.1_δ) give 𝒢_δ(z̄) = conj 𝒢_δ(z). It is
  bounded by (c), so log h° ∈ L¹(dx/√(x(4c − x))) and D_{h°} is Paper 2's (eq:szego).
- So L_h(z) = (𝓡/π)∫_0^{4c}(log h°(x) − log h°(z))dx/(√(x(4c−x))(z − x)).
- By (a), log h°(x) − log h°(z) = 2(𝒢_δ(z) − 𝒢_δ(x)) = 2(z − x)I(z, x). Hence L_h = (2𝓡/π)∫I(z, x)dx/√(x(4c − x)).
- Insert I = Σ_{k≤K}m_kq_k + I_K and the arcsine moments (1/π)∫_0^{4c}x^jdx/√(x(4c − x)) = C(2j, j)c^j (E3 L E3.4 (i), proof). Then
  (1/π)∫q_k(z, x)dx/√(…) = Q_k(z), which gives the formula.
- The bound follows from (1/π)∫_0^{4c}dx/√(x(4c − x)) = 1 and (b). Finally |𝓡(z)| ≤ C|z|^{1/2} near 0. ∎
(PROVED-mod-cite: G23plt1 F.1_δ (i)–(iv), Lemma M [REVIEWED]; E_plt1 F.1 (iii)/(iv) Mellin bound (DLMF 5.2.1, 25.2.1 as quoted
there); Paper 2 (eq:szego), (eq:szego-repr); E3 L E3.4 [REVIEWED].)

*Remarks.*
- (P1.1) For K = 0, (d) is the n-uniform replacement of (O3)–(O4) used through Paper 2 L szego (ii) in G1u L1 (iv), L3. It is
  stronger: it is n^{−p}-small, carries no log(2/|z|), holds in S_out and on the seams too, and needs no derivative bound.
- (P1.2) (d) is E3 L E3.4 (i) (exact for polynomial tilts: L_h = 𝓡M_μ when log h° = −P_μ) plus an explicit remainder, valid on the
  whole disc. It therefore also re-proves the "n-dependence" step of E_plt1 L E′.3 / E3 L E3.5 (there only on the circles, by a
  window argument near the two band crossings).
- (P1.3) Sharpness: (c) with K = 0 is attained up to constants when S₁(δ) ≠ 0, since 𝒢_δ(z) − 𝒢_δ(0) ~ m₁z. Numerically the n^{−2p}
  version fails ([1] controls).
- (P1.4) (Fubini; used only by the check.) For z ∉ [0, 4c] ∪ Γ_±, the double integral in (d) converges absolutely: (B1),
  |ζ − z| ≥ c_z(1 + r), ∫ℓ/(r(1+r)) < ∞. With (1/π)∫_0^{4c}dx/(√(x(4c−x))(ζ − x)) = 1/𝓡(ζ) (Paper 2 §6, Stieltjes transform of the
  arcsine law), L_h(z) = 2𝓡(z)·(1/2πi)Σ_±(±)∫_0^∞ℓ_±(r)e^{±iθ}dr/((ζ_± − z)𝓡(ζ_±)). This is a single integral, which the check
  evaluates. Check [0a] compares it with (eq:szego-repr) by band quadrature.

### 2.2 Lemma P2 (ρ♮ for the glued W̃♮)

Define, on U(0, δ₀) ∖ ([0, δ₀) ∪ Γ₊ ∪ Γ₋) (principal powers, cut [0, ∞) for (−z)^γ),

  W̃♮(z) := 𝗐_n^{1/2}(−z)^{β′/2}(4c − z)^{1/2}e^{−𝒢_δ(z)} = (𝗐_n(−z)^{β′}(4c − z))^{1/2}/G̃_δ,

where G̃_δ := D̃_δB_in^δe^{χ_δ} in S_in and B_out^δe^{χ_δ} in S_out. This is the glued W̃ of RH_plt1b §2 / E_plt1 §0, rebuilt with:
- (j, B_in, B_out, χ) ↦ (j_δ, B_in^δ, B_out^δ, χ_δ) of G3 §2;
- the exponent α ↦ β′.

Put ρ♮ := W̃♮/D_W and ρ♮^{mod} := (−z)^{β′/2}(4c − z)^{1/2}/(D_{x^{β′}}D_{4c−x}) = (Υ̂/4c)^{(1+β′)/2} (G1u L1 (v)).

**Lemma P2.** For n ≥ n₀(p):
(i) ρ♮ = ρ♮^{mod}e^{−L_h/2} on U(0, δ₀) ∖ ([0, δ₀) ∪ Γ_±). Hence |log(ρ♮/ρ♮^{mod})| ≤ C₀′n^{−p}|z|^{1/2}, and
  (1 − √(δ₀/c))^{|1+β′|}e^{−C} ≤ |ρ♮| ≤ (1 + √(δ₀/c))^{|1+β′|}e^{C} there, boundary values on Γ_± included. C does not depend on n or
  on δ (|1 + β′| < 2).
(ii) In U(0, δ₀) ∩ S_in ∩ ℂ_± (in particular on the lips, which lie in ¾θ_L ≤ |arg z| ≤ (5/4)θ_L < θ): ρ♮² = e^{∓iπβ′}/ω^{(β′)}, so
  ϱ_±ρ♮^{−2} = ω♮ exactly.
(iii) ρ♮₊ρ♮₋ = 1 on (0, δ₀).
(iv) ρ♮ is analytic across (−δ₀, 0).
(v) On Γ_± ∩ U(0, δ₀): ρ♮_out = ρ♮_in·e^{−ℓ_±(|z|)}, with e^{−ℓ_±} = 1 − e^{±2πiδ}q(|z|) and |e^{−ℓ_±} − 1| = e^{−2πn|z|^{−1/p}}.
(vi) Sector-wise, ρ♮ = ρ^{(α)}G^{−1}, with ρ^{(α)} the same glued construction with exponent α and D_W^{(α)}, and G = (−z)^{−δ}D_{x^{2δ}}
  (G1u L1 (i), G12 L2.3).

*Proof.* (i) Use Paper 2 (eq:DW-factor) with r_n ≡ 1 and the band weight W₀^{(β′)}:
- D_W = (𝗐_nH_n^δ(0⁺))^{1/2}D_{x^{β′}}D_{4c−x}D_{h°}, and H_n^δ(0⁺) = e^{−2𝒢_δ(0)} with 𝒢_δ(0) real.
- So W̃♮ = (𝗐_nH_n^δ(0⁺))^{1/2}(−z)^{β′/2}(4c − z)^{1/2}e^{−(𝒢_δ(z)−𝒢_δ(0))}, and
  ρ♮ = ρ♮^{mod}·e^{−(𝒢_δ(z)−𝒢_δ(0))}/D_{h°} = ρ♮^{mod}exp(−½(log D_{h°}² − log h°)) = ρ♮^{mod}e^{−L_h/2}.
- The bounds follow from L P1 (d) (K = 0) and G1u L1 (v), whose model computation is p-free.
(ii) On S_in, 𝒢_δ is analytic and equals the band function on (0, δ₀). So e^{−2𝒢_δ} is the analytic continuation of H_n^δ from the band,
and W̃♮² = W₀^{(β′)}e^{∓iπβ′} in ℂ_± (arg(−z) = arg z ∓ π). The rest is G1u L1 (ii) verbatim.
(iii) W̃♮ is analytic across (0, δ₀) ⊂ S_in, and W̃♮₊W̃♮₋ = W₀^{(β′)}. Also D_{W,+}D_{W,−} = W₀^{(β′)}, since log H_n^δ is Lipschitz on the band
by L P1 (a), (b). This is G1u L1 (iii).
(iv) On (−δ₀, 0) ⊂ S_out, 𝒢_δ = log B_out^δ + χ_δ is analytic: B_out^δ's cut is [2πn, ∞), and χ_δ is analytic off the seams. The factors
(−z)^{β′/2}, (4c − z)^{1/2} and D_W are analytic there.
(v) F.1_δ (i) gives 𝒢_δ,out − 𝒢_δ,in = ℓ_±(|z|). Then e^{−ℓ_±} = 1 − e^{±2πiδ}q, and |e^{±2πiδ}q| = q.
(vi) Multiply principal powers of the same base, and use D_W = D_W^{(α)}D_{x^{2δ}} (G12 L2.3 (i)), sector by sector. ∎
(PROVED-mod-cite: L P1; Paper 2 (eq:DW-factor), (eq:szego); G1u L1 (i)–(iii), (v); G23plt1 F.1_δ (i) [REVIEWED].)

### 2.3 Lemma P3 (the glued Hurwitz hard-edge parametrix)

On U(0, δ₀) off (0, δ₀) ∪ lips ∪ Γ_±, put

  Â♮ := P₀^∞ρ♮^{σ₃}Mf^{σ₃/4},  P̂₀♮ := Â♮(2πn)^{σ₃/2}Φ_α(n²f)ρ♮^{−σ₃}  (Bessel order α; Φ_α with the KMVV rays at π − θ_L).

This is D_∞^{−σ₃}P₀♮D_W^{σ₃} for E_plt1's classical glued construction P₀♮ = (−1)^nẼσ₃Ψ_α(n²f)σ₃W̃♮^{−σ₃}e^{nφσ₃},
Ẽ = NW̃♮^{σ₃}Mf^{σ₃/4}(2πn)^{σ₃/2}, as in G1u L2. Let Â^{mod} be Â♮ with ρ♮^{mod} in place of ρ♮.

**Lemma P3.** For n ≥ n₀:
(i) Â^{mod} is analytic in U(0, δ₀) (removable singularity at 0), n-free, det = 1. Moreover
  Â♮ = Â^{mod}(I + 𝔈), 𝔈 := f^{−σ₃/4}M^{−1}(e^{−L_hσ₃/2} − I)Mf^{σ₃/4}, |𝔈| ≤ Cn^{−p}.
  Hence det Â♮ = 1 and |Â♮^{±1}| ≤ C (n-free) on U(0, δ_r) minus the contour, seams included. Â♮ has no jump on (0, δ₀), (−δ₀, 0) or the
  lips. On Γ_±, Â♮_out = Â♮_inY_± with Y_± = f^{−σ₃/4}M^{−1}e^{−ℓ_±σ₃}Mf^{σ₃/4}, |Y_± − I| ≤ C|z|^{−1/2}e^{−2πn|z|^{−1/p}}.
(ii) det P̂₀♮ = 1.
  - Band: P̂₀♮₊ = P̂₀♮₋J on (0, δ_r).
  - Lips in U_0 ∩ ℂ_±: P̂₀♮₊ = P̂₀♮₋[[1, 0], [ω♮e^{2nφ}, 1]] exactly.
  - (−δ_r, 0): no jump.
  - Γ_± ∩ U_0: P̂₀♮_out = P̂₀♮_in·J_g, J_g = ρ♮_in^{σ₃}X^{−1}Y_±Xρ♮_in^{−σ₃}e^{ℓ_±σ₃}, X := (2πn)^{σ₃/2}Φ_α(n²f), and
    |J_g − I| ≤ Cn|z|^{−3/2}e^{−2πn|z|^{−1/p}} ≤ C_Kn^{−K}min(1, |z|^K) for every K.
(iii) Uniformly on |z| = δ_r (both boundary values at the two seam crossings included), for every K:
  P̂₀♮(P₀^∞)^{−1} = I + Σ_{k≤K}Δ_k♮n^{−k} + O(n^{−K−1}), with Δ_k♮ := (2f^{1/2})^{−k}P₀^∞ρ♮^{σ₃}(σ₃Ξ_k(α)σ₃)ρ♮^{−σ₃}(P₀^∞)^{−1}.
(iv) With ζ = n²f(z): |P̂₀♮^{±1}| ≤ Cn^{1/2}|ζ|^{−|α|/2} for |ζ| ≤ 2 (Cn^{1/2}(1 + |log|ζ||) if α = 0), and ≤ C|z|^{−1/4} for |ζ| ≥ 2.
  C is n-free; the seams are included.

*Proof.* (i) Â^{mod}: G1u L2 (i), model case, verbatim.
- Band: P₀^∞₊ = P₀^∞₋J, ρ^{mod}₊ρ^{mod}₋ = 1 (Υ̂₊Υ̂₋ = 16c²), f₊^{σ₃/4} = f₋^{σ₃/4}diag(−i, i), JM = Mdiag(i, −i).
- On (−δ₀, 0): P₀^∞, f^{1/4} and ρ^{mod} are analytic.
- At 0: |Â^{mod}| ≤ C|z|^{−1/2}, so the singularity is removable. Â^{mod} is n-free, so |Â^{mod±1}| ≤ C on Ū(0, δ_r).
- The factorisation: diagonal factors commute, so ρ♮^{σ₃} = (ρ^{mod})^{σ₃}e^{−L_hσ₃/2}, by L P2 (i).
- The off-diagonal entries of M^{−1}(e^{−L_hσ₃/2} − I)M are multiplied by f^{±1/2} under the conjugation. With |f|^{−1/2} ≤ C|z|^{−1/2} and
  |e^{∓L_h/2} − 1| ≤ C|L_h| ≤ Cn^{−p}|z|^{1/2} (L P1 (d)), this gives |𝔈| ≤ Cn^{−p}.
- The jumps follow from L P2 (iii)–(v). Y_±: ρ♮_out^{σ₃} = ρ♮_in^{σ₃}e^{−ℓ_±σ₃}, and |f^{∓1/4}||f^{±1/4}| ≤ C|z|^{−1/2}.
(ii) Band and lips: G1u L2 (ii) verbatim, with L P2 (ii), (iii). The lips lie in S_in, so the S_in branch of ρ♮ applies.
- (−δ_r, 0): Φ_α has no jump there (ζ > 0), and Â♮, ρ♮ have none (L P2 (iv)).
- Seams: Γ_± ∩ U_0 is mapped by ζ = n²f into the central sector, since |arg ζ| ≈ π − θ < π − θ_L. So Φ_α is analytic across Γ_±, and
  P̂₀♮_in^{−1}P̂₀♮_out = ρ♮_in^{σ₃}X^{−1}Y_±Xρ♮_in^{−σ₃}·e^{ℓ_±σ₃} (L P2 (v)).
- Paper 2 (eq:he-Phi-large), (eq:he-Phi-small) and App B (B2)–(B3) (the bounds used for (iv)) give |X^{±1}| ≤ Cn^{1/2}|ζ|^{−|α|/2} for
  |ζ| ≤ 2 and ≤ C|z|^{−1/4} for |ζ| ≥ 2. Since |ζ| ≍ n²|z|, both are ≤ Cn^{1/2}|z|^{−1/2} on U_0. With |ρ♮^{±1}| ≤ C,
  |J_g − I| ≤ Cn|z|^{−1}·|z|^{−1/2}q + Cq.
- Finally sup_{0<r≤δ_r}r^{−m}e^{−πnr^{−1/p}} ≤ C_mn^{−mp}.
- The jump of R := Q♮P̂₀♮^{−1} on the seam segments is not J_g but J_R = P̂₀♮_inJ_g^{−1}P̂₀♮_in^{−1} =
  Â♮_inXe^{−ℓ_±σ₃}X^{−1}Y_±^{−1}(Â♮_in)^{−1}, so |J_R − I| ≤ C(n|z|^{−1} + |z|^{−1/2})e^{−2πn|z|^{−1/p}} by (i) and the bounds on X
  above (added per Rule R review B, P3-1).
(iii) G1u L2 (iii)'s proof verbatim (pointwise algebra in ρ♮).
- The large-ζ expansion of Ψ_α to order K holds in the three sectors of E_plt1 L E′.3 (rays at π − θ_L; DLMF 10.40.1–4 with
  δ = θ_L/2 in the central sector, 10.17.5–6, .11–.12 in the thin ones, at general k as quoted in JZC_M4_proof N.6a).
- On |z| = δ_r, P₀^∞^{±1}, f^{−1/2} and ρ♮^{±1} are bounded n-free (L P2 (i)), boundary values included.
(iv) G1u L2 (iv) verbatim: Paper 2 (eq:he-Phi-large), (eq:he-Phi-small), L bessel-local (iii), with |Â♮^{±1}|, |ρ♮^{±1}| ≤ C from (i) and
L P2 (i). ∎
(PROVED-mod-cite: L P1, L P2; G1u L2 [REVIEWED for p > 1, review A; used here only in their p-free parts] (fixed per Rule R
review B, G-1); E_plt1 L E′.3 (sectors) [REVIEWED]; JZC_M4_proof N.6a (DLMF at general k);
Paper 2 L bessel-local, L comparison-parametrix (i) (band-jump algebra).)

*Remark.* The glue enters P̂₀♮ only through the super-small Y_±, J_g. That is why (i) needs no analytic part: Â♮ itself is
bounded, n-uniformly, up to and across the seams. Compare RH_plt1b §2 / RH_px L4.2 (iii), whose split Ẽ_N = E^a + Φ (Cauchy integral
of the jump, endpoint log moved off ∂U) is not needed here.

### 2.4 Lemma P4 (lip mismatch; fixed-n identification)

**Lemma P4.**
(a) For z on the lips in U_0 ∩ ℂ_±, |ω♮(z) − ϱ_±| ≤ C|z|^{1/2}, with C n-free. Consequently Paper 2 L lip-mismatch holds for Q♮ with
  ε_Λ ≡ 0 and ν_p = ½: sup_lips|d_n| ≤ Cε′_n with ε′_n = n^{−1}log n, and ‖v − ṽ‖_{L^∞} ≤ C(ε′_n + n^{−1}).
(b) Fix n ≥ n₀ and 1 < s < 1 + 2p, and let R := Q♮P̂₀♮^{−1} in U_0 ∖ (Σ ∪ Γ_±). Then |R(z)| ≤ C_{n,η}|z|^{−|α|−η} for every η > 0.
  R − 𝒞_loc(R₋(J_R − I)) has a removable singularity at 0, where 𝒞_loc is the Cauchy integral over (lips ∪ Γ_±) ∩ U(0, ½δ_r). R is
  bounded near 0 up to a logarithm, and R_± ∈ I + ∂𝒞(L²(Σ_R)).

*Proof.* (a) By L P2 (ii), ω♮ − ϱ_± = ϱ_±(ρ♮^{−2} − 1), and ρ♮^{−2} = (Υ̂/4c)^{−(1+β′)}e^{L_h}. Here |Υ̂/4c − 1| ≤ C|z|^{1/2} (G1u L1 (v))
and |L_h| ≤ Cn^{−p}|z|^{1/2} (L P1 (d)). The rest is G1u L3 / Paper 2's proof:
- localisation;
- F4 for Q♮, since |e^{∓2iθ_δ}| = |e^{∓2iθ}| and Paper 2 L supersmall holds for all p;
- circles by L P3 (iii) at K = 0.
(b) G1u L4's proof, with these changes:
- |Q♮| ≤ C_{n,η}|z|^{−|α|/2−η} is G23plt1 P2.6 (i), not G12 P2.4.
- |P̂₀♮^{−1}| = |adj P̂₀♮| ≤ C_n|z|^{−|α|/2} (L P3 (iv)).
- The jumps of R in U(0, ½δ_r) are: none on the band (equal jumps J); none on (−δ_r, 0); super-small on the lips (F4 amplified by
  |P̂₀♮^{±1}|²); and on the seams J_R = P̂₀♮_in J_g^{−1}P̂₀♮_in^{−1} (Q♮ has no seam jump), so |J_R − I| ≤ C_nn|z|^{−|α|−3/2}e^{−2πn|z|^{−1/p}}.
- So R₋(J_R − I) is bounded and Hölder on the local contour, which is a finite union of rays from 0. Its Cauchy integral is
  O(1 + |log|z||).
- The difference is O(|z|^{−|α|−2η}) with |α| + 2η < 1 and has no jump, hence is removable.
- Membership in I + ∂𝒞(L²) is Paper 2 L B-cauchy (c), as in Cor L2 (at ∞, R = Q♮(P₀^∞)^{−1} = I + O(1/z)). ∎
(PROVED-mod-cite: L P1–P3; G23plt1 P2.6 [REVIEWED]; Paper 2 L supersmall, L lip-mismatch (proof), L B-cauchy (c).)

### 2.5 Lemma P5 (the band-factor gauge for p < 1 in the α-frame = H-c, p < 1)

**Lemma P5.** Let K, J ≥ 1 and μ = μ^δ_n := (2m_1(δ), …, 2m_J(δ)) (real). Uniformly on ∂U_0 (including both boundary values at the two
seam crossings) and on ∂U_r = ∂U(4c, ε), for k ≤ K:
- Δ_k♮ = G_μΔ_k^{mod,β′}G_μ^{−1} + O(n^{−(J+1)p});
- the Airy data likewise: Δ_k^r[ω^{(β′)}] = G_μΔ_k^{r,mod,β′}G_μ^{−1} + O(n^{−(J+1)p}).

"mod,β′" means the weight x^{β′}(4c − x) with Bessel order α, i.e. the decoupled model M(β′, α).

*Proof.* Hard edge:
- Δ_k^0 depends on ρ only through ρ^{σ₃}(·)ρ^{−σ₃}, which multiplies the off-diagonal entries by ρ^{±2}. The coefficients
  (2f^{1/2})^{−k}P₀^∞σ₃Ξ_kσ₃(P₀^∞)^{−1} are bounded on |z| = δ_r.
- Put ρ^μ := ρ♮^{mod}e^{−𝓡M_μ/2}. This is E3 L E3.4 (i) for the weight x^{β′}(4c−x)e^{−P_μ}; the proof is weight-exponent-free.
- By L P2 (i), ρ♮² = (ρ^μ)²e^{−(L_h − 𝓡M_μ)}, and L P1 (d) with K := J gives |e^{∓(L_h − 𝓡M_μ)} − 1| ≤ Cn^{−(J+1)p} on |z| = δ_r,
  boundary values included. So Δ_k♮ = Δ_k^{0,μ} + O(n^{−(J+1)p}).
Soft edge:
- (−ω)^{±1/2} enters Δ_k^r only through conjugation by (−ω)^{∓σ₃/2}.
- By Paper 2 (eq:omega) / (eq:DW-factor), ω^{(β′)} = ω^{mod,β′}·D_{h°}²/h° = ω^{mod,β′}e^{L_h}. Paper 2 (eq:omega-4c): ω♮ = ω^{(β′)} near
  4c, with no phase, since the lips avoid U(4c, h₀) (H-d §6 item 1).
- ω^μ = ω^{mod,β′}e^{𝓡M_μ} (E3 L E3.4 (i)), so the ratio is e^{L_h − 𝓡M_μ} = 1 + O(n^{−(J+1)p}) on ∂U(4c, ε) ⊂ {|z| ≤ R₁}.
Finally, E3 L E3.4 (iii) gives Δ_k^{⋄,μ} = G_μΔ_k^{⋄,mod,β′}G_μ^{−1}. Its proof commutes diagonal factors only, so it holds for every k
(JZC_M4_proof N.6a, last bullet) and for exponent β′. ∎
(PROVED-mod-cite: L P1 (d), L P2 (i); E3 L E3.4 [REVIEWED]; Paper 2 (eq:omega), (eq:omega-4c).)

Relation to JZC_M3a_H_Hc.md Lemma Hc.5 (same statement; JZC_M3a_H_Hc.md Lemma Hc.5 (NOT REVIEWED before Rule R review B), REVIEWED
by it; fixed per Rule R review B, G-1): Hc.5 uses F.1_δ (iv)'s sup bound
plus its derivative bound near the band crossings {δ_r, 4c − ε} of the circles. L P5 uses only F.1_δ (i)–(iii) and the moment bound of
(iv)'s far part (through L P1). The two proofs are independent.

## 3. The proposition

**Proposition G1u′ (n-uniform hard-edge comparison for the Hurwitz problem, 0 < p < 1).** Let 0 < p < 1, −1 < δ < 0 and
1 < s < 1 + 2p (so α ∈ (−1, 1) and β′ = α + 2δ ∈ (−3, 1); |β′| ≥ 1 is allowed). Let Q♮ be the Hurwitz Q-matrix of Frame 1 (H-d Lemma via
G3 Cor 5; G23plt1 P2.6), and assume H-a (JZC_M3a_H_Ha.md; it covers p < 1). Then there is n₀ = n₀(p, s, δ) such that for n ≥ n₀:

**(A) (Paper 2 §7 verbatim).**
- Prop UR-comparison holds for the comparison problem Q̃. Q̃ is built with A₀ and Φ_α at 0 (weight-free, Bessel-α: "contains neither D_W
  nor any other trace of the weight") and with the Airy parametrix with ω♮ = ω^{(β′)} at 4c.
- Thm UR-true holds for Q♮.
- (Q♮)₁ = P₁ + Ξ₁♮ + O(n^{−2}log n), and (Q♮)₂ = P₂ + Ξ₂♮ + ((Q♮)₁ − P₁)P₁ + O(n^{−2}log n). (Paper 2's O(n^{−1−2ν_p}log n + n^{−2})
  with ν_p = ½.)
- In particular n^pb_n(σ^δ) = c(p)(1 + O(1/n)) and n^pa_n(σ^δ) = 2c(p)(1 + O(1/n)).

**(B) (order K, the input to H-e).** Let R := Q♮P̂^{−1}, with:
- P̂ = P̂₀♮ (L P3, glued) in U_0;
- Paper 2's P̂_r (with ω^{(β′)}) in U(4c, ε);
- P₀^∞ elsewhere;
- circles clockwise.

The contour Σ_R contains the seam segments Γ_± ∩ U_0. Uniformly in n ≥ n₀:
- on ∂U_0: J_R = I + Σ_{k≤K}Δ_k♮n^{−k} + O(n^{−K−1}) (L P3 (iii)). On ∂U(4c, ε): N.6a's soft-edge expansion with (−ω^{(β′)})^{±1/2};
- in U_0: |J_R − I| ≤ C_Kn^{−K}min(1, |z|^K) on the lips (Paper 2 L supersmall amplified by L P3 (iv); as RH_px L4.3) and on the seam
  segments, where J_R = P̂₀♮_inJ_g^{−1}P̂₀♮_in^{−1} = Â♮_inXe^{−ℓ_±σ₃}X^{−1}Y_±^{−1}(Â♮_in)^{−1}, so |J_R − I| ≤
  C(n|z|^{−1} + |z|^{−1/2})e^{−2πn|z|^{−1/p}} by L P3 (i), (ii) (fixed per Rule R review B, P3-1). There is no contour on (−δ_r, 0);
- elsewhere: |J_R − I| ≤ Ce^{−n/C}, resp. Cn^{−pn/4} on the top segment (Paper 2 F5 for Q♮; H-a top vertex X₁ + δ′; G23plt1 P2.6 (ii));
- so ‖J_R − I‖_{L¹∩L²∩L^∞(Σ_R)} = O(1/n) and ‖𝒞₋‖ ≤ C. This is Paper 2 F1 for the contour, plus finitely many fixed rays from 0
  inside U_0, as in E_plt1 Prop E′.5′ (1). Then R₋ = (1 − 𝒞_{J_R})^{−1}I, by L P4 (b) for the identification, and ‖R₋ − I‖_{L²} = O(1/n).

With L P5, the residue recursion of JZC_M4_proof Prop N.6c holds for M(β′, ν = α) with gauge μ^δ_n:

  R = I + Σ_{k≤K}R^{(k)}(μ^δ_n)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}) (at distance ≥ d from Σ_R),  R₁ = Σ_{k≤K}R₁^{(k)}(μ^δ_n)n^{−k} + O(same).

These are the lattice exponents. With the extraction of JZC_M4_proof §5–6 (Theorem N.6 (i)), this gives **Theorem H (i) for 0 < p < 1**.

*Proof.* (A) G1u Prop (A)'s proof, with these replacements:
- F7, i.e. Q♮_± ∈ I + ∂𝒞(L²), is G23plt1 P2.6 (Cor L2 for p < 1, exponent |α|/2).
- L lip-mismatch is L P4 (a) (ε_Λ ≡ 0).
- The soft edge: ω^{(β′)} is bounded above and below near 4c, by Paper 2 L szego (vi)(b) with q₁ = x^{β′}h°. Its hypothesis (iv),
  |log q₁ − 𝔠₁| ≤ 𝔐 on U(4c, 2ε₁), holds with 𝔐 n-free by L P1 (c); 4c ∈ S_in, at positive distance from the seams.
- Extraction is F8 (G3 Prop 4 / G23plt1 L2.5 at ∞).
Nothing else in Paper 2 §7 / App B sees the weight at the hard edge (App B "the two instances"; Paper 2 (eq:he-P0hat)).
(B) The jump bounds are as listed. The small-norm and induction steps of N.6c are verbatim. They use only:
- these bounds;
- ‖𝒞₋‖ ≤ C;
- L P5, which replaces Δ_k♮ by the meromorphic G_μΔ_k^{mod,β′}G_μ^{−1} up to O(n^{−(J+1)p}) on the circles;
- N.6b's meromorphy of Δ_k^{mod,β′} for p < 1. This is the parity argument, which is β-free: on (0, δ), ρ_{mod}²₊ρ_{mod}²₋ = 1 for every
  exponent (Υ̂₊Υ̂₋ = 16c²); on (−δ, 0), ρ_{mod} is analytic.
The point 0 is reached as in E_plt1 Prop E′.5′: the super-small local jumps, lips and seam glue, vanish to all orders at 0. For z on
(−δ_r, 0) and s on a seam, |s − z| ≥ max(|s|, |z|). ∎ (PROVED-mod-cite + REVIEWED (Rule R review B); inputs §4.)

**α ≥ 1 (s ≥ 1 + 2p).** Not covered, exactly as for p > 1: G23plt1 P2.6 and L P4 (b) use |α| < 1. OPEN (outside the Setting).

## 3a. (record) Exactly which lines of the p < 1 construction change

"verbatim" means the line holds as written with (j, B_in, B_out, χ, ℓ, α in W̃) ↦ (j_δ, B_in^δ, B_out^δ, χ_δ, ℓ_±, β′) and no other change.

| source, line | with the α-frame W̃♮ (Hurwitz) | status |
|---|---|---|
| RH_plt1b §2, "W̃ := (C(−z)^{α_x}(4c − z))^{1/2}/G̃, G̃ := D̃·B_in·e^X in S_in, B_out·e^X in S_out ∩ U(0, δ)" | W̃♮ = (𝗐_n(−z)^{**β′**}(4c − z))^{1/2}/G̃_δ, G̃_δ = D̃_δB_in^δe^{χ_δ} \| B_out^δe^{χ_δ} (= e^{𝒢_δ}). Exponent β′, not α: with α, ρ_w ∼ \|z\|^{−δ} (G1u Route B; check [2], [3], [6] controls) | **CHANGED** |
| RH_plt1b §2, "The lips are reproduced exactly in S_in" | exactly, with the Hurwitz lip entry ω♮ = ω^{(β′)}e^{±2πiδ} and Bessel order α ≠ β′ (L P2 (ii)) | **CHANGED** (phase; order ≠ exponent) |
| RH_plt1b §2, "On the seams, W̃_out/W̃_in = D̃B_ine^{X_in}/(B_oute^{X_out}) = D̃/D = 1 − e^{∓2πit}, \|e^{∓2πit}\| = exp(−2πN\|z\|^{−1/p})" | = e^{−ℓ_±} = 1 − e^{∓2πi(t−δ)} = 1 − e^{±2πiδ}q: complex, same modulus (L P2 (v); F.1_δ (i)) | **CHANGED** (value); estimate verbatim |
| RH_plt1b §2, "handled by RH_px Lemma 4.2(iii)'s split Ẽ_N = E^a + Φ" | not needed: Â♮ = Â^{mod}(I + 𝔈), \|𝔈\| ≤ Cn^{−p} (L P3 (i)) | **REPLACED** |
| RH_plt1b §2, "Removability: D_w/W̃ is bounded above and below near 0 in both sectors" | \|log(ρ♮/ρ♮^{mod})\| ≤ Cn^{−p}\|z\|^{1/2}, n-uniform, seams included (L P2 (i)) | **STRENGTHENED** |
| E_plt1 §0 "Hard edge" (P̂₀ := D_∞^{−σ₃}P₀D_W^{σ₃}; ρ := W̃/D_W) | ρ♮ := W̃♮/D_W with D_W of W₀^{(β′)} | **CHANGED** (as above) |
| E_plt1 L E′.3, "The expansions … none depends on p > 1 … rays at π − θ_L … (E.3.1) holds in all three sectors" | same sectors; Ξ_k(α) (Bessel order α) | verbatim |
| E_plt1 L E′.3, "The glue … changes the analytic prefactor by Φ = O(e^{−c′n})" | the prefactor is Â♮ itself, bounded (L P3 (i)); glue in J_g only | **REPLACED** |
| E_plt1 L E′.3, "The n-dependence: … W₀ = 𝗐′z^α(4c−z)e^{−λz}q₂ … window \|x − Re z\| ≤ η₀ … \|E_n′\| ≤ Cn^{−2p}/η₀" | L P1 (d): \|L_h − 𝓡M_μ\| ≤ Cn^{−(J+1)p}\|𝓡\| on the whole disc, no derivative bound | **REPLACED** (L P5) |
| E_plt1 L E′.3, "ρ^{mod} is explicit and bounded above and below on \|z\| = δ" | ρ♮^{mod} = (Υ̂/4c)^{(1+β′)/2} (G1u L1 (v)) | **CHANGED** (exponent) |
| E_plt1 L E′.5 (meromorphy): on (−δ, 0) "(ρ^λ)²₊/(ρ^λ)²₋ = e^{−2πiα}ω₋/ω₊ = 1 (W₀ ∝ z^α …)" | for the model with exponent β′: ρ_{mod}² is analytic across (−δ, 0); band relation Υ̂₊Υ̂₋ = 16c² | **CHANGED** (exponent), conclusion verbatim |
| E_plt1 Prop E′.5′ (1)(a), lips at ±θ_L, "RH_px Lemma 4.3 with the lip constant 2π sin(θ_L/p)" | F4 for Q♮ (\|e^{∓2iθ_δ}\| = \|e^{∓2iθ}\|), amplification L P3 (iv) | verbatim |
| E_plt1 Prop E′.5′ (1)(b), "P̂₀ carries the glue jump W̃_out/W̃_in = 1 − e^{∓2πit} … after amplification by P̂₀ (\|e^{±nφ}\| ≤ e^{Cn\|z\|^{1/2}} …)" | J_g of L P3 (ii): \|J_g − I\| ≤ Cn\|z\|^{−3/2}e^{−2πn\|z\|^{−1/p}} (Q-frame amplification polynomial) | **CHANGED** (value; bound sharper) |
| E_plt1 Prop E′.5′ (2), "Δ₁ = Δ₁^{mod} + λ_nΔ₁^{lin} + O(n^{−2p})" | Δ_k♮ = G_μΔ_k^{mod,β′}G_μ^{−1} + O(n^{−(J+1)p}) (L P5) | **CHANGED** (all k, all J; β′) |
| E_plt1 Prop E′.5′ (3), meromorphy; "the point 0 is reached …" | N.6b for M(β′, α); point 0 verbatim | verbatim |
| JZC_M4_proof N.6a p < 1 bullet, "RH_plt1b's glue changes the prefactor by O(e^{−c′n}) (E_plt1 Lemma E′.3)" | not needed (L P3 (i)) | **REPLACED** |
| JZC_M4_proof N.6a, "With … E_plt1 Lemma F.1(iv) (p < 1), at order J it gives the stated O(n^{−(J+1)p})" | L P1 (d) with F.1_δ (moments m_k(δ), Fourier sums) | **CHANGED** (δ; route) |
| JZC_M4_proof N.6b p < 1 parity argument | ρ_{mod} with exponent β′; β-free | verbatim |
| JZC_M4_proof N.6c p < 1 bullets (lips ±θ_L, seam glue jumps; point 0) | glue jumps = J_g (L P3 (ii)) | verbatim |
| G1u L1 (i), (ii), (iii), (v) | sector-wise | verbatim |
| G1u L1 (iv) proof (Paper 2 L szego (ii) with q = H_n^δ°, 𝔐 from (O3)–(O4) G12 P1.4(a); "log B_δ bounded and Hölder") | L P1 (d) (K = 0) | **REPLACED** |
| G1u L1: "h_n^δ … with a super-small jump on (−δ_r, 0)" | none: 𝒢_δ is analytic on (−δ₀, 0) ⊂ S_out (L P2 (iv)); new: glue on Γ_± (L P2 (v)) | **CHANGED** |
| G1u L2 (i) proof ("On (−δ_r, 0) the only jump is h_n^δ's … removed as in RH_px L4.2(iii) … maximum principle") | Â♮ = Â^{mod}(I + 𝔈) (L P3 (i)) | **REPLACED** |
| G1u L2 (ii) "(−δ_r, 0): … only the super-small jump inherited from h_n^δ" | no jump there; seams carry J_g | **CHANGED** |
| G1u L2 (iii), (iv) | sectors of E_plt1 E′.3 | verbatim |
| G1u L3, \|ω♮ − ϱ_±\| ≤ C\|z\|^{ν_p}log(2/\|z\|) | ≤ C\|z\|^{1/2}, no log (L P4 (a)) | **CHANGED** (sharper) |
| G1u L4: "\|Q♮\| ≤ … (G12 P2.4(i))"; jumps "on the lips and on (−δ_r, 0)" | G23plt1 P2.6 (i); jumps on lips and seams | **CHANGED** (inputs) |
| G1u Prop (A): F7 "G12 P2.4, Cor L2"; L3; ε′_n = n^{−2ν_p}log n | G23plt1 P2.6; L P4 (a); ν_p = ½ | **CHANGED** (inputs) |
| G1u Prop (B): "With the band-factor input H-c …" (CONDITIONAL) | L P5 (proved here for p < 1; also JZC_M3a_H_Hc.md Hc.5) | **DISCHARGED** for p < 1 |

## 4. Inputs and labels

L P1 uses:
- G23plt1 Lemma F.1_δ (i)–(iii) and Lemma M (PROVED-mod-cite + REVIEWED; built on G3 Lemma 3, REVIEWED; Rule R review B);
- E_plt1 F.1 (iii)/(iv)'s Mellin bound [REVIEWED for δ = 0; via M2 for δ];
- Paper 2 (eq:szego), (eq:szego-repr);
- E3 L E3.4 [REVIEWED].

L P2–P4 use:
- G1u L1–L4 [REVIEWED for p > 1, review A; used here only in their p-free parts] (fixed per Rule R review B, G-1; C-11);
- G23plt1 P2.6;
- G3 Cor 5 (H-d (i)–(iii) for p < 1);
- E_plt1 L E′.3 (sectors) [REVIEWED];
- JZC_M4_proof N.6a–c (PROVED-mod-cite; review A done);
- Paper 2 L supersmall, L bessel-local, L comparison-parametrix, L B-cauchy (c), §7 / App B;
- H-a (JZC_M3a_H_Ha.md, REVIEWED) (fixed per Rule R review B, C-11 of REVIEW_JZC_M3a_H_assembly_B.md).

Labels:
- **L P1–P5 and Prop G1u′ (A), (B): PROVED-mod-cite + REVIEWED** (Rule R review B, research/G1/review/REVIEW_JZC_M3a_H_plt1_G1up_B.md).
- Novelty: UNCHECKED (Rule L not done; the method is the standard Deift–Zhou small-norm argument).

**Effect on Theorem H (JZC_M3a_H.md §4).**
- Item 1 is now closed for p < 1 as well (Rule R review B done).
- Together with items 2–4 (done) and H-c (L P5 here; JZC_M3a_H_Hc.md Hc.5), **(i) for 0 < p < 1 has no remaining CONDITIONAL
  input**. Every piece is PROVED-mod-cite; every memo-level piece is REVIEWED except JZC_M4_proof Theorem N.6 / N.6a–c (review A done,
  second reader pending).
- (ii) is unchanged: exact at the orders of Prop S, Conjecture Σ beyond.
- For p > 1, (i) rests on H-c (JZC_M3a_H_Hc.md Cor Hc.4 (PROVED-mod-cite + REVIEWED)) (fixed per Rule R review B, G-1; C-11).
- Not covered: δ > 0, p = 1 with δ ≠ 0, α ≥ 1.

## 5. Numerical checks (Rule N: NUMERICAL, not certified; finite samples of universally quantified statements)

**m3a_g1up_hardedge.py/.out** (mpmath dps 30). This is G1u's hard-edge check ported to p < 1, **with the actual seam band factor**
through the representation of L P1 / Remark P1.4, not with the model weight. The p > 1 check used the model weight only. Results are in
§5a. Data provenance (Rule X):
- 𝒢_δ comes from F.1_δ's representation. That representation is identified with G3's literal construction near 0, including next to
  the seams, in [0b] (and at |z| ≥ 0.7 in G23plt1 [G]).
- m_k(δ) are the Fourier sums S_k(δ), computed from the Hurwitz series by residue classes (no mpmath ζ(s, a) continuation).
- Nothing is fitted.

**m3a_g1up_endtoend.py/.out** (Jacobi coefficients of the actual Hurwitz measures, n ≤ 1600, K = 1.6·10⁵ and 3.2·10⁵ atoms + Gauss–Jacobi
tail, binary128 RKPW, cache tmp/plan62_cache; generation ≈ 2–4 min per measure, fits ≈ 5 s). Results are in §5b.

### 5a. Hard edge

(m3a_g1up_hardedge.out: **ALL 159 CHECKS PASSED**, 36 of them controls that must fail and do; 3 controls are reported as not applicable (Rule A 9b); runtime ≈ 30 min (51 min in the 2026-10-22 re-run). Re-run after Rule R review B, N-1: the band-factor-dropped control is now asserted in 4 of 5 sets; the output differs from the reviewed one only in those lines and the count, 157/34/5 → 159/36/3.) Parameter sets (p, α, δ; β′):
(0.6, −½, −0.8; −2.1), (0.6, −0.6, −0.8; −2.2), (0.3, −0.3, −0.9; −2.1), (0.75, 0.3, −0.3; −0.3), (0.75, 0.6, −0.95; −1.3).
- [0a] L_h by the single-integral formula (Remark P1.4) = Paper 2 (eq:szego-repr) by 64-node Gauss–Chebyshev band quadrature, to
  7·10⁻²⁹ relative. The 4 points include a seam boundary value and S_out.
- [0b] G0 from the representation = G3's literal glued exponent near 0 (|z| ≤ 0.05; three points at angular distance 10⁻¹²θ from a
  seam, plus the negative axis), to ≤ 8·10⁻²⁷.
- [1] L P1 (c), (d), K = 0, 1, 2, n = 10…640.
  - Grid: |z| ∈ {10⁻³, 0.03, 0.3}, 9 angles (both boundary values on both seams, S_in, S_out, negative axis), plus 3 points near 4c.
  - p = 0.6 at δ ∈ {−0.02, −0.5, −0.98}; p = 0.3 at δ ∈ {−0.5, −0.98}.
  - Example (p = 0.6, δ = −0.5): sup n^p|G0|/|z| = 0.0667, 0.0626, 0.0608, 0.0600, and sup n^p|L_h|/|𝓡| = 0.140 → 0.121. With the gauge,
    n^{2p}|L_h − 𝓡M_μ|/|𝓡| = 0.0847 → 0.0835 (K = 1).
  - Every value is below twice the δ-free next-term majorant, and settled (n = 640 within 25% of n = 160).
  - Controls: the n^{−2p}-scaled sup grows (×5.1 at p = 0.6, δ = −0.02). At (0.3, −0.98) the control is not applicable: S₁ ≈ 0
    (Rule A 9b).
- [2] |ρ♮| ∈ [0.66, 1] for β′ ≤ −1 (1 ≤ |ρ♮| ≤ 1.28 at β′ = −0.3), over 10⁻¹² ≤ |z| ≤ c/2 with seams, n = 10, 100, 1000.
  - n^p|log(ρ♮/ρ♮^{mod})|/|z|^{1/2} ∈ {0.075–0.077, 0.151–0.155, 0.013–0.015, 0.085–0.088} (flat in n).
  - ρ♮₊ρ♮₋ = 1 to 10⁻²².
  - Glue ρ♮_out/ρ♮_in = e^{−ℓ_±} to ≤ 2·10⁻²⁰ relative to |e^{−ℓ} − 1|.
  - Control: ρ_w is unbounded.
- [3] |Â♮^{±1}| ≤ 1.77 (10⁻¹² ≤ |z| ≤ 10⁻², seams both sides); Â♮₊ = Â♮₋ on the band to 10⁻²⁵. Control: |z|^{1/2}|Â_w| grows to
  10⁹–10¹¹.
- [4] Exact lip match to 10⁻³⁰. |ω♮ − ϱ_±|/|z|^{1/2} ∈ [0.44, 1.88] at n = 10 and 1000. Control: |ω♮ − e^{∓iπβ′}| ≥ 0.27.
- [5] Circle |z| = c/2, 8 points, 4 of them seam boundary values (the circle |z| = c/2 is larger than U_0; the algebra is the same)
  (per Rule R review B, N-4).
  - n|J − I| is flat (e.g. 0.8452 … 0.8461).
  - Remainder after Δ₁♮/n: exponents 1.95–2.07 → 2.00 (α ≠ ±½); 10⁻²² … 10⁻³¹, exponentially small, at α = −½.
  - Gauge (J = ⌊1/p⌋): exponents 2.00–2.22, as predicted.
  - Controls (asserted where discriminating, Rule A 9b): band factor dropped, exponents 1.59–1.60 (p = 0.6, α = −½), 1.19–1.30
    (p = 0.3), 1.72–1.88 (p = 0.6, α = −0.6) and 1.88–1.92 (p = 0.75, α = 0.6) (the last two asserted since review B, N-1); ν = β′, exponent 1.00.
- [6] |P̂₀♮^{±1}||ζ|^{|α|/2}n^{−1/2} ≤ 1.32 (|ζ| ∈ [10⁻⁸, 2], n = 10, 100, 1000, seam points incl.). Control: ρ_w gives up to 10²⁷.

### 5b. End-to-end (m3a_g1up_endtoend.out: **ALL 29 CHECKS PASSED**, 9 of them controls that must fail and do)

α = −½ throughout. Tolerance = max(3·half-range, floor). Every asserted row is also asserted stable under K → 2K (difference < tol/10).

| p, s, δ (β′) | d₁ fit / M(β′, α) | ε₁ fit / Fourier sum | d₂\|ε fit / M(β′, α) | controls (dev/tol) |
|---|---|---|---|---|
| 0.6, 1.3, −0.8 (−2.1) | +0.3300001 / +0.33 | +0.028671 (hr 8·10⁻⁴) / +0.028662 | +0.197314 (hr 6·10⁻³) / +0.197283 | lattice d₁ 4.8·10⁴; H2 d₂ 74; lattice ε₁ 48 |
| 0.6, 1.3, −0.5 (−1.5) | +0.1500000 / +0.15 | +0.030620 (hr 7·10⁻⁴) / +0.030614 | +0.082111 (hr 6·10⁻³) / +0.082083 | 3.0·10⁴; 40; 55 |
| 0.75, 1.375, −0.8 (−2.1) | +0.4125000 / +0.4125 | +0.018286 (hr 1.5·10⁻⁴) / +0.018302 | +0.258410 (hr 10⁻⁴) / +0.258412 (free d₂ fit: +0.258627, hr 3·10⁻³, also asserted) | 6.0·10⁴; 4.7·10³; 237 |

Notes on the rows:
- **d₂|ε** is the n⁻² coefficient after subtracting the predicted d₁, ε₁ and ε₂ terms. At p = 0.6 the free fit cannot separate n⁻² from
  n^{−1.6} and n^{−2.2}: half-range 0.17, so that row is printed and **not asserted**. Each subtracted term is tested in its own row,
  except ε₂, which is not discriminating (below).
- **ε₂** (n^{−1−2p}) fits agree with the prediction (dev/tol ≤ 0.003), but the half-ranges are ≈ 0.08 against values ≈ 0.01–0.02.
  These rows are printed and not asserted (Rule N: not discriminating).
- So, in the regime β′ ≤ −1 at p < 1, the actual Hurwitz Jacobi coefficients follow M(β′ = α + 2δ, ν = α) with the Hurwitz band
  factor:
  - d₁ = −p(β′+1)/2 to 10⁻⁷;
  - ε₁ (the Fourier sum, = 2pcζ(−p, a) by Remark 3.3 — asserted in the script to 10⁻²⁵ as a NUMERICAL identity, not used) to 10⁻⁵;
  - d₂ to 3·10⁻⁵.
- The lattice (δ ignored), H2 (Bessel order shifted with β′) and the lattice band factor (S₁(0)) are excluded.
- This is evidence for the *conclusion* of Prop G1u′ + N.6, not for the uniform bounds themselves.

## 6. Rule A (adversarial pass) — log

1. *Does the glued W̃ with exponent β′ really need no Bessel-order change?*
   - The lip match ϱ_±ρ♮^{−2} = ω♮ forces ν ≡ ±α (mod 2), as for p > 1 (G1u Rule A 2).
   - Checks [4], [5]: the control ν = β′ leaves a constant lip mismatch (≥ 1.05) and an O(1/n) circle remainder (exponent 1.00).
2. *Is (eq:szego-repr) really valid with the S_out value of log h° as 𝔠?*
   - Yes: the identity holds "for every number 𝔠" (Paper 2 sec_6 l. 170–173). Its derivation uses only (1/π)∫dx/(√(x(4c−x))(z−x)) = 1/𝓡.
   - It is the device that makes L P1 (d) sector-free. Check [0a] tests it on a seam boundary value and in S_out against an independent
     band quadrature.
3. *Window argument for z near a seam with x on the band.*
   - The density g₊ = ℓ₊/(ζ − x) is smooth on the window, since |ζ − x| ≥ |ζ|sin θ (B1). x never comes near the seam.
   - The only z-dependent geometry is Paper 2 Lemma corner's, as in G23plt1 L2.5.
4. *Is the |z|^{1/2} in L_h really there in S_out and on the seams, not only near the band?*
   - Yes: 𝓡(z) is a factor of the exact formula (d), whatever the sector.
   - Check [1] asserts sup_z n^{(K+1)p}|L_h − 𝓡M_μ|/|𝓡| below twice the δ-free next-term majorant, at points on both seams (both sides),
     in S_out, on the negative axis and near 4c.
   - [2] gives n^p|log(ρ♮/ρ♮^{mod})|/|z|^{1/2} ≈ 0.075–0.077 from |z| = 10⁻¹² to c/2, n = 10…1000.
5. *Could 𝔈 fail to be small near 0 (the f^{±1/2} amplification)?*
   - |f|^{−1/2}|L_h| ≤ C|z|^{−1/2}·n^{−p}|z|^{1/2}: the cancellation is exact in the exponents.
   - Check [3]: |Â♮^{±1}| ≤ 1.8 from 10⁻¹² to 10⁻², seams included, at n = 100.
   - Control: with ρ_w (exponent α) |z|^{1/2}|Â_w| grows from 24 to 2·10⁹.
6. *Glue amplification in the Q-frame.* E_plt1 E′.5′ (1)(b) quotes e^{Cn|z|^{1/2}} from the classical frame.
   - In the Q-frame X^{±1} = O(n^{1/2}|z|^{−1/2}) (L P3 (iv)), so the amplification is polynomial.
   - Either way it is beaten by e^{−2πn|z|^{−1/p}}.
7. *β′ ≤ −2.*
   - ρ♮^{mod} = (Υ̂/4c)^{(1+β′)/2} with |1 + β′| < 2. Checks at β′ = −2.1, −2.2: |ρ♮| ∈ [0.66, 1] with the actual band factor.
8. *δ → 0⁻, δ → −1⁺.*
   - L P1's constants are δ-free (Lemma M). Check [1] covers δ ∈ {−0.02, −0.5, −0.98} at p = 0.6 and δ ∈ {−0.5, −0.98} at p = 0.3.
   - The δ-dependence sits in G23plt1 P2.6 / G3 (fixed n) only.
9. *Flatness proxy in check [1] (Rule N).*
   - The first run asserted "n = 640 value ≤ 1.5 × n = 40 value". At (p, δ, K) = (0.6, −0.02, 2) it failed: 0.00102 → 0.00341 for G0,
     0.0066 → 0.0122 for L_h.
   - Reason: the sup approaches its limit |m₃|n^{3p}max|z|² from below. S₃(−0.02) is small, and the n = 10, 40 values sit below the
     asymptote.
   - That assertion was replaced by two assertions: every n below twice the δ-free next-term majorant (|S_k| ≤ ζ(1+kp)), and n = 640
     within 25% of n = 160.
   - No assertion was dropped without replacement. The failing values are quoted here (that run was stopped; its .out was overwritten).
9b. *Vacuous controls and an offset artefact (second run, Rule N).* The second full run had 5 failures of 163 assertions, none of a claim:
   - [1] n^{−2p} control at (p, δ) = (0.3, −0.98): |S₁(−0.98)|/ζ(1.3) = 0.002, so m₁ ≈ 0 and G0/z is dominated by the m₂ term. The
     n^{−2p}-scaled sup is then flat (0.122 → 0.090) and the control cannot fail. Now asserted only if |S₁(δ)| ≥ 0.05ζ(1+p); at
     (0.3, −0.5) the ratio is 0.085, and the control is asserted and fails as required. The claim rows themselves passed.
   - [5] ν = β′ control at (p, α, δ) = (0.75, 0.3, −0.3): β′ = −0.3 = −α, and Q₀ depends on ν² only. The control is degenerate; this
     is G1u's guard |β′| ≠ |α|, which the port had dropped and now restores.
   - [5] band-factor-dropped control at the same point: m₁(−0.3) is small at p = 0.75, so the n^{−1−p} term is invisible against
     O(n^{−2}) at n ≤ 400 (exponents 1.96–2.01). Now asserted only if the dropped-factor remainder exceeds 10× the true one at n = 400,
     or (since Rule R review B, N-1) if its exponents leave the claim's window [1.9, 2.15].
   - [2] glue identity at (0.75, 0.3, −0.3): relative error 1.8·10⁻⁸ against tolerance 10⁻⁸. The boundary values were taken at angular
     offset 10⁻¹²θ, which produces an O(10⁻¹²) error against |e^{−ℓ} − 1| ≈ 5·10⁻⁵. The offset is now 10⁻²⁴; the tolerance is unchanged.
   - A third run caught that the restored guard compared mpf values exactly (α = 0.3 enters as a float, so |β′| − |α| ≈ 10⁻¹⁷ ≠ 0); it now uses ||β′| − |α|| > 10⁻¹² (fourth run).
   - Net effect (fixed per Rule R review B, N-1; guard widened in the script and re-run): the band-factor-dropped control is asserted in
     4 of 5 sets: (0.6, −½, −0.8) and (0.3, −0.3, −0.9) by the 10× guard, and (0.6, −0.6, −0.8) (exponents 1.78, 1.75, 1.72) and
     (0.75, 0.6, −0.95) (1.92, 1.90, 1.88), whose dropped-factor exponents already fall outside the claim's window [1.9, 2.15]; only at
     (0.75, 0.3, −0.3) (1.99, 2.01, 2.01) is the control non-discriminating.
   No claim assertion was weakened.
10. *Matching rate with the band factor.*
    - With the true ρ♮, the remainder after Δ₁♮/n is O(n⁻²): exponents 2.04 → 2.00 at α = −0.6.
    - It is exponentially small at α = −½, as for p > 1.
    - With the band factor dropped (ρ♮^{mod} in Δ₁) the remainder is O(n^{−1−p}): exponents 1.59–1.60 at α = −½, p = 0.6; the control
      fails as required.
    - With the gauge at J = ⌊1/p⌋ it is O(n^{−1−(J+1)p}) (exponent 2.22 at p = 0.6, α = −½).
    - So the band factor is visible at exactly the predicted order, and the gauge removes it.
11. *Rule X.*
    - The band factor's representation is identified with the literal construction ([0b]; G23plt1 [G]).
    - The moments come from series.
    - The Jacobi coefficients are those of the actual measures, and nothing is fitted to the predictions.
    - ε₁'s prediction is the Fourier sum; its equality with 2pcζ(−p, a) is asserted as a NUMERICAL side identity (Remark 3.3, NOT QUOTED).
12. *Converse used?* No: L P1 is a bound, and nowhere is it used that the bound is attained.

## 7. What remains

- **Rule R:** done for L P1–P5 and Prop G1u′ (review B, REVIEW_JZC_M3a_H_plt1_G1up_B.md) and for their inputs G23plt1 F.1_δ, P2.6
  and G3 Lemma 3, Prop 4, Cor 5 (review B, REVIEW_JZC_M3a_H_plt1_inputs_B.md). Still pending: the second reader of JZC_M4_proof
  Theorem N.6 / N.6a–c.
- **α ≥ 1** (s ≥ 1 + 2p): the in-lens identification, as for p > 1. OPEN.
- **p > 1.** L P1's argument should give H-c for p > 1 as well, with E_pgt1's representation (E.2.1)_δ (a Cauchy integral over
  (−∞, 0) with density 𝔢_δ; JZC_M3a_H_Hc.md Hc.1) in place of F.1_δ. The analogue of (B1) is |y − x| ≥ |y| for y < 0 ≤ x, which
  makes the near-band window unnecessary. Not written: HEURISTIC; JZC_M3a_H_Hc.md does p > 1 by the derivative route.
- **The p > 1 hard-edge check used only the model weight.** A port of [1]–[2] here to p > 1 with the actual Binet-cut band factor
  (G12) was not done.
- The end-to-end ε₂ rows are not discriminating at n ≤ 1600 (§5b).

## 8. Notes for other memos (not edited here)

- **JZC_M3a_H.md §4 item 1**: the p < 1 part ("conditional on … E_plt1's glued parametrix with W̃♮") can point here. The status line
  "(i) … For p < 1 it is also conditional on rebuilding E_plt1's glued parametrix with W̃♮" becomes: for p < 1, (i) is PROVED-mod-cite,
  NOT REVIEWED, with inputs G3, G23plt1, H-a, this note (L P5 for H-c), JZC_M4_proof N.6.
- **JZC_M3a_H_G1u.md §3 "p < 1"**: "its glue jumps are super-small and the amplification is L2 (iv)'s, so no new exponent issue is
  expected" is confirmed (L P3 (ii)). The remark "E_plt1's glued parametrix (L E′.3) must be rebuilt with W̃♮" is done here.
- **E_plt1 Prop E′.5′ (1)(b)** (REVIEWED, δ = 0): the amplification quoted there, "|e^{±nφ}| ≤ e^{Cn|z|^{1/2}}", is that of the classical
  frame. In the Q-frame it is polynomial (L P3 (ii) at δ = 0). No change of result.
- **For FIXES (Paper 2, via a human):** none.
