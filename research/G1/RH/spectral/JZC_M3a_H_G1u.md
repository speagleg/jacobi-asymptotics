# JZC M3a, gap 1 of Theorem H: the n-uniform hard-edge comparison with Szegő exponent β′ = α + 2δ (p > 1)

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_M3a_H_pgt1_chain_A.md); fixes applied 2026-10-21.
Status (2026-10-21): **REVIEWED** for p > 1 (L1–L4, Prop G1u (A), (B); Rule R: independent second reader A re-derived them and re-ran
m3a_g1u_hardedge.py, m3a_g1u_endtoend.py, byte-identical outputs; fixes G1u-1–G1u-3 applied). The "p < 1" paragraph of §3 was not
reviewed. Inputs keep their own labels (G12: NOT REVIEWED; E3.7 for M(β′, α): exact check m3a_e37_decoupled, not yet reviewed).
Labels per VERIFICATION_POLICY.md. Closes, modulo the inputs listed in §4, item 1 of JZC_M3a_H.md §4 ("the n-uniform hard-edge comparison with Szegő exponent β′") for **p > 1, −1 < δ ≤ 0,
1 < s < 1 + 2p** (|α| < 1). Checks: `checks/m3a_g1u_hardedge.py/.out` (110 assertions, 34 of them controls that must fail),
`checks/m3a_g1u_endtoend.py/.out` (29 assertions, 8 controls). Everything attributed to Paper 2 is quoted from papers/paper2/{sec_6,sec_7,app_a,app_b,
app_c}.tex as read for this note (read-only; nothing there was edited). No external theorem is quoted here that is not already
quoted, with hypotheses, in the cited repo notes (Rule C): the Bessel/Airy facts are those of Paper 2 (T2, T4) and of
JZC_M4_proof Lemma N.6a (DLMF 10.17, 10.40, 9.7 as quoted there).

| # | Statement | Label |
|---|---|---|
| §1 | inventory: where Paper 2 §6–7 / App A–C and the N.6 route use the Szegő exponent, and what happens at β′ | (analysis) |
| L1 | ρ♮ := W̃♮/D_W (classical W̃ with exponent β′, Szegő function of x^{β′}) = ρ^{(α)}/G; ρ♮² = e^{∓iπβ′}/ω^{(β′)}; ρ♮₊ρ♮₋ = 1 on the band; \|ρ♮\|^{±1} ≤ C n-free, for every real β′ | PROVED-mod-cite (Paper 2 L szego (i)–(ii); G12 L1.2–L1.3, L2.3) |
| L2 | the Hurwitz hard-edge parametrix P̂₀♮ (Bessel order α): matching factor Â♮ analytic (mod super-small) and bounded n-uniformly; exact lip match; circle jump I + Σ_{k≤K}Δ_k♮n^{−k} + O(n^{−K−1}) uniformly; Bessel-scale size n^{1/2}\|ζ\|^{−\|α\|/2} | PROVED-mod-cite (L1; Paper 2 L bessel-local, (eq:he-Phi-large/small); JZC_M4_proof N.6a / E_pgt1 L E.3 for the expansion) |
| L3 | lip mismatch: \|ω♮ − e^{∓iπα}\| ≤ C\|z\|^{ν_p}log(2/\|z\|) on the lips in U(0, δ_r), C n-free | PROVED-mod-cite (L1; Paper 2 L szego (ii)) |
| L4 | fixed n: R := Q♮P̂₀♮^{−1} satisfies \|R\| ≤ C_{n,η}\|z\|^{−\|α\|−η} near 0, so R is bounded at 0 and R_± ∈ I + ∂𝒞(L²) | PROVED-mod-cite (G12 P2.4; Paper 2 L B-cauchy (c)) |
| **Prop G1u** | (A) Paper 2 §7 (UR-comparison, UR-true, Prop moments) holds verbatim for Q♮, with ε′_n = n^{−2ν_p}log n; (B) the order-K small norm (N.6c) holds for the Hurwitz problem in the α-frame, with remainder O(n^{−K−1} + n^{−1−(J+1)p}) | (A) PROVED-mod-cite; (B) PROVED-mod-cite (H-a: JZC_M3a_H_Ha.md; H-c: JZC_M3a_H_Hc.md Cor Hc.4) (fixed per Rule R review A of the p>1 chain, G1u-2); REVIEWED (p > 1) |
| §5 | numerics: L1–L3 pointwise, circle matching rate O(n^{−2}) after Δ₁♮, \|β′\| ≥ 1 incl. β′ = −2.1, −2.2; end-to-end Hurwitz Jacobi coefficients at β′ = −2.1, −1.5 | NUMERICAL |

## 0. Answer

Gap 1 closes for p > 1 (−1 < δ ≤ 0, |α| < 1), with **no loss in the error exponents**, and in the α-frame exactly as anticipated:
the Szegő exponent β′ never enters a bound alone. It enters only through
- ρ♮ := W̃♮/D_W, where the two singular powers (−z)^{β′/2} and D_{x^{β′}} cancel: ρ♮ = ρ^{(α)}·G^{−1}, G := (−z)^{−δ}D_{x^{2δ}} the
  factor of G12 L2.3; ρ♮ is bounded above and below on the whole disc, uniformly in n, for **every** real β′ (L1);
- ω♮ := ω^{(β′)}e^{±2πiδ} on the lips, whose limit at 0 is e^{∓iπβ′}e^{±2πiδ} = e^{∓iπα}: the Bessel model of order α (L3);
- the a-priori bound F7, which G12 P2.4 already proved with the lattice exponent |α|/2 (used only at fixed n, L4).

Two remarks on the brief.
1. **There is no shrinking disc.** Paper 2 §7 and the N.6 route (RH_px §4.1, E_pgt1 L E.3, JZC_M4_proof N.6a) both use a fixed disc
   U(0, δ_r) ("radii fixed, small", Frame Prop "may be taken as small as we wish (but fixed, independent of n)"). n enters only through
   the Bessel variable ζ = n²f(z). So "uniform in n on the disc boundary" means: on the fixed circle |z| = δ_r, uniformly in n.
2. **G is not analytic at 0.** G = (4c/Υ̂)^δ with Υ̂ := ((−z)^{1/2} + (4c−z)^{1/2})² (§2, proof of L1 (v)); it is analytic in U(0, δ_r)∖[0, δ_r)
   and bounded above and below, but on the band G₊G₋ = 1, G₊ ≠ G₋. It is a ratio of Szegő type, like ρ itself. What the proof needs
   is exactly this (boundedness and the band relation), not analyticity. The matching factor that must be analytic is Â♮ = P₀^∞ρ♮^{σ₃}Mf^{σ₃/4}
   (route B), resp. Paper 2's A₀ = P₀^∞Mf^{σ₃/4} (route A), and both are (L2 (i); Paper 2 L comparison-parametrix (i)).

The two routes, and where β′ would have broken them:
- **Route A (Paper 2 §7, Conway–Deift comparison; O(1/n)).** The comparison problem Q̃ is *literally the lattice-α one* at the hard edge
  (P̂₀ = A₀(2πn)^{σ₃/2}Φ_α(n²f) contains no weight), and at the soft edge it differs only through ω♮ = ω^{(β′)} near 4c, which is bounded
  above and below (no phase there; H-d Lemma (ii)–(iii)). So Prop UR-comparison is unchanged. The true problem differs from Q̃ only
  on the lips (L3, with ε_Λ ≡ 0 since ℓ₁ ≡ 1) and needs Q♮_± ∈ I + ∂𝒞(L²) (G12 P2.4). **Would fail** if F7 were proved with
  |D_W|^{±1} ≲ |z|^{±β′/2} (Paper 2 L szego (vi), last claim, at exponent β′): |z|^{−|β′|/2} is not square integrable for |β′| ≥ 1.
- **Route B (classical KMVV parametrix; order K, as in N.6).** The lip match forces W̃♮ ∝ (−z)^{β′/2} (exponent β′) while the Bessel order
  stays α; the matching factor and the Bessel-scale size of P̂₀♮ are governed by ρ♮, which is bounded (L1–L2). **Would fail** if one
  used W̃ with the exponent α (the "Bessel-α W̃, β′-Szegő" mixture): then ρ_w := W̃^{(α)}/D_W ∼ |z|^{−δ}, the matching factor grows like
  |z|^{−1/2+δ} (not removable for δ < −½), and P̂₀ acquires the exponent |α|/2 + |δ| (checks [2], [3], [6]: controls). It would also fail
  in the identification step (L4) with the naive Q-bound: the product exponent (|β′| + |α|)/2 + η is ≥ 1 for α = −½, δ = −0.8.

## 1. Inventory: which statements use the Szegő exponent

Frame 1 of H-d: V♮, Q♮ := D_∞^{−σ₃}V♮D_W^{σ₃} with D_W the Szegő function of W₀^{(β′)} := 𝗐_nz^{β′}(4c − z)H_n^δ (principal), the
lattice g, φ, f, the outer scalar F♮ = F_δ(−z)^{−δ}. Jumps (H-d Lemma (ii), conjugated by D_W^{σ₃}): J on the band; on the lips
[[1, 0], [ω♮e^{2nφ}, 1]] + E with ω♮ := ω^{(β′)}e^{±2πiδ} in ℂ_±, ω^{(β′)} := D_W²/W₀^{(β′)}; in U(4c, ε) the lattice jumps with
ω^{(β′)} (the lips avoid U(4c, h₀), so no phase there); none on (−∞, 0).

| Paper 2 / N.6 item | where an exponent enters | at β′ (Bessel order α) | status |
|---|---|---|---|
| F1 (jumps, \|v^{±1}\| ≤ C) | ω on the lips: L szego (vi)(a), factor (4cz/Υ)^α/z^α | the factor is (4c/Υ)^{β′}e^{2πikβ′}: bounded for every real exponent; ω♮ = ω^{(β′)}e^{±2πiδ}, \|e^{±2πiδ}\| = 1 | survives |
| F2 (band weight) | x^α, H_n Hölder (O3)–(O4) | x^{β′}; (O3)–(O4) for H_n^δ: G12 P1.4(a) | survives |
| F3, F6 (lips, f, localisation (eq:he-localisation)) | none (built from μ*, lattice g) | unchanged (H-d: lattice g) | survives |
| F4 (super-small E) | \|κ_± − 1\|, e^{−2nφ̃}, ω^{±1} | \|e^{∓2iθ_δ}\| = \|e^{∓2iθ}\|; phases of modulus 1 | survives |
| F5 (P₀^∞; Airy; far arcs) | ω near 4c (L szego (vi)(b) with q₁ = x^αĤ°), (vi)(c) | q₁ = x^{β′}Ĥ° is analytic and positive near 4c, (iv) holds for any exponent; top vertex X₁ + δ′ (H-a) | survives (Ha §4, 'F5 on the moved arcs') (fixed per Rule R review A of the p>1 chain, G1u-1 = C-1) |
| F7 (a priori, Cor L2) | \|D_W\|^{±1} ≤ C\|z\|^{±α/2−η}, exponent \|α\|/2 | **breaks if done with β′** (\|z\|^{−\|β′\|/2} ∉ L² for \|β′\| ≥ 1); G12 P2.4 gives \|α\|/2 via L2.3 | survives (G12) |
| F8 (extraction) | ϰ_∞ at ∞ | G12 C1.5 (F♮ → C_δ) | survives |
| L bessel-local, (eq:he-Phi-large/small) | Bessel order α: \|Ψ_α^{±1}\| ≤ C\|ζ\|^{−\|α\|/2} | order stays α (H-d; H3 excluded by data) | unchanged |
| L comparison-parametrix (i), (iii) | A₀ = P₀^∞Mf^{σ₃/4}: weight-free | unchanged | unchanged |
| L comparison-parametrix (ii) | D_{W,+}D_{W,−} = W₀; lip entry ϱ_±e^{2nφ}/D_W² | D_{W,+}D_{W,−} = W₀^{(β′)}; lip entry vs. true e^{2nφ}e^{±2πiδ}/W₀^{(β′)}: mismatch is L3 | survives |
| L lip-mismatch | factor x^α: D_{x^α}²/z^α = ϱ_±(1 + O(\|z\|^{1/2})) | D_{x^{β′}}²/z^{β′} = e^{∓iπβ′}(1 + O(\|z\|^{1/2})), times e^{±2πiδ}: ϱ_± = e^{∓iπα} | survives (L3) |
| Prop UR-comparison, App B | hard block: β = ±α/2 in L A-power (\|β\| < ½ ⇔ \|α\| < 1); soft block: A_r with (−ω)^{±1/2} | Q̃ at 0 is weight-free and Bessel-α: unchanged; soft block: (−ω♮)^{±1/2} bounded | unchanged |
| Thm UR-true, Prop moments | F7 (membership only), d_n bounds, Q̃ bounds | as above; ε_Λ ≡ 0 | survives |
| Rem alpha-ge-1 (a)–(c) | \|α\| < 1 in (a) F7, (b) L A-power, (c) ∫\|ζ\|^{−\|α\|} | (a) by G12 P2.4 (\|α\|/2); (b), (c) Bessel order α | survives (\|α\| < 1 needed, \|β′\| < 1 not) |
| N.6 route: W̃ (RH_px §4.1, KMVV (6.44)–(6.46)) | W̃² = W₀e^{∓iπα} | must be W̃♮² = W₀^{(β′)}e^{∓iπβ′} (exponent β′) for the lip match (L1 (ii)) | modified (L1) |
| N.6 route: Ẽ / Â analytic, bounded | ρ := W̃/D_W bounded | ρ♮ bounded for every β′ (L1 (iv)) | survives (L2) |
| N.6a: circle jumps to order K | Δ_k^0 = (2f^{1/2})^{−k}P₀^∞ρ^{σ₃}σ₃Ξ_k(α)σ₃ρ^{−σ₃}(P₀^∞)^{−1} | ρ → ρ♮ (model: ρ♮² = (Υ̂/4c)^{1+β′}), Ξ_k(α) | survives (L2 (iii)) |
| RH_px L4.3 (hard-edge mismatch inside U_0) | amplification of super-small entries by P₀^{±1} | polynomial in n, \|z\|^{−1} (L2 (iv)); beaten by e^{−n\|z\|^{−1/p}/C} | survives |
| RH_px §5 identification / Cor L2 | R = QP̂₀^{−1} near 0 | \|R\| ≤ C_n\|z\|^{−\|α\|−η} in the α-frame (L4); with the naive β′ bound it fails | survives (L4) |
| N.6b, N.6c | meromorphy of Δ_k, residue recursion | β-free and k-free (JZC_M3a_H §3.3) | unchanged |
| E3 L E3.4–E3.5, F.1′ (band-factor gauge) | H_n | H_n^δ: input H-c | input |

## 2. The lemmas

Notation. δ_r: Paper 2's hard-edge radius (fixed, small); U_0 := U(0, δ_r); Z(r) as in Paper 2 §6. h_n^δ := H_n^δ = (D̃_δB_δ)^{−2},
analytic off (−∞, 0] (G12 L1.2(a), L1.3), with a super-small jump on (−δ_r, 0) (as RH_px L3.2(v): D̃_δB_δ jumps by κ_δ₋/κ_δ₊ there, and
|e^{∓2iθ_δ}| = |e^{∓2iθ}| = exp(−2π sin(π/p)n|y|^{−1/p})). Principal powers, cut [0, ∞) for (−z)^γ. ϱ_± := e^{∓iπα} (Paper 2's notation).

W̃♮ := (𝗐_nH_n^δ(0⁺))^{1/2}(−z)^{β′/2}(4c − z)^{1/2}(h_n^δ°)^{1/2},  h_n^δ° := h_n^δ/H_n^δ(0⁺);  ρ♮ := W̃♮/D_W;
W̃^{(α)}, ρ^{(α)} := the same with α in place of β′ and D_W^{(α)} := D_{W₀^{(α)}}, W₀^{(α)} := 𝗐_nz^α(4c − z)H_n^δ (the lattice-α objects with the
Hurwitz band factor); G := (−z)^{−δ}D_{x^{2δ}} (G12 L2.3).

**Lemma 1 (ρ♮).** Let p > 1, −1 < δ ≤ 0, β′ = α + 2δ, n ≥ 2. On U_0∖ℝ (boundary values where stated):
(i) ρ♮ = ρ^{(α)}·G^{−1};
(ii) ρ♮² = e^{∓iπβ′}/ω^{(β′)} in ℂ_± ∩ Z(¼η_*), hence ϱ_±ρ♮^{−2} = ω♮ (exactly) there, in particular on the lips in U_0;
(iii) ρ♮₊ρ♮₋ = 1 on (0, δ_r);
(iv) |ρ♮|^{±1} ≤ C on U_0∖ℝ, C = C(p, s, δ, δ_r), independent of n;
(v) model (h_n^δ° ≡ 1): ρ♮ = (Υ̂/4c)^{(1+β′)/2} = ((−z)^{1/2}/(2√c) + (1 − z/4c)^{1/2})^{1+β′}, Υ̂ := ((−z)^{1/2} + (4c−z)^{1/2})²; ρ♮(0) = 1 and
  (1 − √(δ_r/c))^{|1+β′|} ≤ |ρ♮| ≤ (1 + √(δ_r/c))^{|1+β′|} for δ_r ≤ c/4.
*Proof.* (i) Principal powers of the same base with real exponents multiply exactly: (−z)^{β′/2} = (−z)^{α/2}(−z)^δ, so W̃♮ = W̃^{(α)}(−z)^δ;
and D_W = D_W^{(α)}D_{x^{2δ}} (G12 L2.3(i): multiplicativity of D_q). Divide.
(ii) In ℂ_±, arg(−z) = arg z ∓ π, so (−z)^{β′} = e^{∓iπβ′}z^{β′} (principal) and W̃♮² = W₀^{(β′)}e^{∓iπβ′} (h_n^δ is the continuation of H_n^δ
from the band, which is the W₀ of F1). So ρ♮² = e^{∓iπβ′}W₀^{(β′)}/D_W² = e^{∓iπβ′}/ω^{(β′)}, and ϱ_±ρ♮^{−2} = e^{∓iπα}e^{±iπβ′}ω^{(β′)} = e^{±2πiδ}ω^{(β′)} = ω♮.
(iii) On (0, δ_r): (−z)^{β′/2}₊(−z)^{β′/2}₋ = x^{β′/2}e^{−iπβ′/2}·x^{β′/2}e^{iπβ′/2} = x^{β′}; (4c − z)^{1/2}, h_n^δ are analytic across the band; so
W̃♮₊W̃♮₋ = W₀^{(β′)}(x) = D_{W,+}D_{W,−} (Paper 2 §6: D_{q,+}D_{q,−} = q where log q is Hölder; here log H_n^δ is, by (O3)).
(v) Paper 2 L szego (i): D_{x^b}² = (4cz/Υ)^b, D_{4c−x}² = 4c(z − 4c)/Υ. In ℂ_± near 0, z^{1/2} = ±i(−z)^{1/2}, (z − 4c)^{1/2} = ±i(4c − z)^{1/2}, so
Υ = −Υ̂, 4cz/Υ = (−z)(4c/Υ̂), 4c(z−4c)/Υ = (4c − z)(4c/Υ̂) (this is E_pgt1 L E.4(iii)'s computation with α replaced by β′). For δ_r small,
arg(4c/Υ̂) is small, and arg(−z) + arg(4c/Υ̂) stays in (−π, π) (on the band from ℂ₊, arg(−z) = −π and arg(4c/Υ̂) = 2arctan√(x/(4c−x)) > 0),
so the principal powers multiply: D_W = (−z)^{β′/2}(4c − z)^{1/2}(4c/Υ̂)^{(β′+1)/2}·(𝗐_nH_n^δ(0⁺))^{1/2} and ρ♮ = (Υ̂/4c)^{(1+β′)/2}. With
u := (−z)^{1/2}/(2√c), |u| ≤ ½√(δ_r/c), and |(1 − z/4c)^{1/2} − 1| ≤ δ_r/(4c) ≤ ½√(δ_r/c), the bound follows.
(iv) In general ρ♮ = ρ♮^{mod}·(h_n^δ°)^{1/2}/D_{h°}, D_{h°} := D_{H_n^δ°}. On Z(¼η_*): Paper 2 L szego (ii) with q = H_n^δ°, 𝔠₀ = 0, ν = ν_p and 𝔐 = C
from (O3)–(O4) (G12 P1.4(a), n-free) gives |log(D_{h°}²/h°)| ≤ C|z|^{ν_p}log(2/|z|). Off Z(¼η_*) (|arg z| ≥ ¼θ_w, so |x − z| ≥ (x + |z|)/C):
(eq:szego-repr) with 𝔠 = 0 gives |log D_{h°}| ≤ C (as in the proof of L szego (vi), last claim), and |log h_n^δ°| ≤ C on U_0∖(−δ_r, 0] since
|t| = n|z|^{−1/p} ≥ 2 and |arg t| ≤ π/p < π (G12 L1.2(b): |j_δ| ≤ C_J/|t|), and log B_δ is bounded and Hölder near 0 from each side
(G12 L1.3(iii), (eq:B-bounds)). Together with (v). (Alternatively: (i), the lattice bound for ρ^{(α)}, and |G|^{±1} ≤ C on U_0, since
|G| = |4c/Υ|^δ and Υ = −4c(1 + O(|z|^{1/2})).) ∎ (PROVED-mod-cite: Paper 2 L szego (i)–(ii); G12 L1.2–L1.3, P1.4(a), L2.3.)

*NUMERICAL* (check [2], model): |ρ♮| ∈ [0.683, 1] on 10⁻¹² ≤ |z| ≤ c/2 for β′ = −2.1 (p ∈ {0.6, 1.5, 3}), [0.660, 1] for β′ = −2.2,
[0.901, 1] for β′ = −1.3; ρ♮₊ρ♮₋ = 1 to 10⁻²⁰ on the band. Control: ρ_w := W̃^{(α)}/D_W satisfies |ρ_w||z|^δ ∈ [0.94, 1], i.e. |ρ_w| ∼ |z|^{−δ}.

**Lemma 2 (the Hurwitz hard-edge parametrix).** Put, in U_0 off the contour,
  Â♮ := P₀^∞ρ♮^{σ₃}Mf^{σ₃/4},  P̂₀♮ := Â♮(2πn)^{σ₃/2}Φ_α(n²f)ρ♮^{−σ₃}  (Φ_α = σ₃Ψ_ασ₃e^{−2ζ^{1/2}σ₃}, Paper 2 (eq:he-Phi), Bessel order α).
This is D_∞^{−σ₃}P₀♮D_W^{σ₃} for the classical construction P₀♮ = (−1)^nẼσ₃Ψ_α(n²f)σ₃W̃♮^{−σ₃}e^{nφσ₃}, Ẽ = NW̃♮^{σ₃}Mf^{σ₃/4}(2πn)^{σ₃/2},
N = D_∞^{σ₃}P₀^∞D_W^{−σ₃} (RH_px §4.1 with W̃♮; (eq:he-ephi) for (−1)^ne^{nφσ₃} = e^{−2ζ^{1/2}σ₃}). For n ≥ n₀:
(i) Â♮ = Â♮^a + O(e^{−c′n}) on U(0, ½δ_r) with Â♮^a analytic in U(0, ½δ_r), det Â♮ = 1, and |Â♮^{±1}| ≤ C (n-free). For the model weight
  Â♮ is analytic, exactly, and independent of n.
(ii) det P̂₀♮ = 1; P̂₀♮₊ = P̂₀♮₋J on (0, δ_r); on the lips in U_0 ∩ ℂ_±, P̂₀♮₊ = P̂₀♮₋[[1, 0], [ω♮e^{2nφ}, 1]] — exactly the main part of Q♮'s
  lip jump; on (−δ_r, 0) only the super-small jump inherited from h_n^δ.
(iii) Uniformly on the circle |z| = δ_r (off Σ, boundary values included) and for every K:
  P̂₀♮(P₀^∞)^{−1} = I + Σ_{k≤K}Δ_k♮n^{−k} + O(n^{−K−1}),  Δ_k♮ := (2f^{1/2})^{−k}P₀^∞ρ♮^{σ₃}(σ₃Ξ_k(α)σ₃)ρ♮^{−σ₃}(P₀^∞)^{−1},
  Ξ_k(α) = M^{−1}(M∘C_k) as in N.6a (Bessel order α). In particular the circle jump is I + O(1/n) uniformly in n, with
  Δ₁♮ = (1/(16f^{1/2}))P₀^∞ρ♮^{σ₃}Q₀ρ♮^{−σ₃}(P₀^∞)^{−1}, Q₀ = [[−(1+4α²), 2i], [2i, 1+4α²]] (E_pgt1 L E.3).
(iv) With ζ = n²f(z): |P̂₀♮^{±1}| ≤ Cn^{1/2}|ζ|^{−|α|/2} for |ζ| ≤ 2 (Cn^{1/2}(1 + |log|ζ||) if α = 0) and |P̂₀♮^{±1}| ≤ C|z|^{−1/4} for |ζ| ≥ 2, C n-free.
*Proof.* (ii) Â♮ is analytic off the band and (−δ_r, 0) (below), so the jumps of P̂₀♮ are those of Φ_α(n²f) conjugated by ρ♮^{−σ₃}, plus
ρ♮'s own. Band: Φ_α jumps by J ((eq:he-Phi-jumps), with Paper 2 L comparison-parametrix (ii)'s orientation argument), and
ρ♮₋^{σ₃}Jρ♮₊^{−σ₃} = Jρ♮₋^{−σ₃}ρ♮₊^{−σ₃} = J by L1 (iii). Lips: Φ_α jumps by [[1, 0], [ϱ_±e^{−4ζ^{1/2}}, 1]] and e^{−4ζ^{1/2}} = e^{2nφ}
(eq:he-ephi); conjugation by ρ♮^{−σ₃} turns the entry into ϱ_±ρ♮^{−2}e^{2nφ} = ω♮e^{2nφ} by L1 (ii). (−δ_r, 0): Φ_α has no jump there, ρ♮ only
h_n^δ's.
(i) Band: P₀^∞₊ = P₀^∞₋J, ρ♮₊^{σ₃} = ρ♮₋^{−σ₃} (L1 (iii)), f₊^{σ₃/4} = f₋^{σ₃/4}diag(−i, i) (Paper 2 L comparison-parametrix (i), proof), and
JM = M diag(i, −i). So Â♮₊ = P₀^∞₋Jρ♮₋^{−σ₃}M diag(−i, i)f₋^{σ₃/4} = P₀^∞₋ρ♮₋^{σ₃}JM diag(−i, i)f₋^{σ₃/4} = Â♮₋. On (−δ_r, 0) the only jump is h_n^δ's,
super-small, and is removed as in RH_px L4.2(iii) (write Â♮ = Â♮^a + Cauchy integral of the jump over (−δ_r, 0); the density is
O(|y|^{−1/2}e^{−cn|y|^{−1/p}})). At 0: |P₀^∞| ≤ C|z|^{−1/4} (eq:Pinf0-bound), |f^{±1/4}| ≤ C|z|^{±1/4}, |ρ♮^{±1}| ≤ C (L1 (iv)), so |Â♮^a| ≤ C|z|^{−1/2}:
removable (Paper 2 L comparison-parametrix (i), whose argument uses only this growth). det: each factor has determinant 1. Uniform
bound: on |z| = ¾δ_r all factors are bounded n-free (L1 (iv), f conformal and n-free), and the maximum principle applies to Â♮^a and its
adjugate.
(iii) The expansion of Ψ_α at large ζ to order K (DLMF 10.40.1–4 in the central sector, 10.17.5–6, .11–.12 in the thin ones, with the
coefficients a_k(α), b_k(α) of 10.17.1, 10.17.8) is exactly as in JZC_M4_proof L N.6a / E_pgt1 L E.3: it gives
σ₃Ψ_ασ₃ = (2πζ^{1/2})^{−σ₃/2}M[I + Σ_kσ₃Ξ_k(α)σ₃(2ζ^{1/2})^{−k} + O(|ζ|^{−(K+1)/2})]e^{2ζ^{1/2}σ₃} in every sector. Insert into P̂₀♮: the factors
M, f^{±σ₃/4}, (2πn)^{±σ₃/2} cancel as in Paper 2 L comparison-parametrix (iii), leaving P₀^∞ρ♮^{σ₃}[I + Σ_k …]ρ♮^{−σ₃}(P₀^∞)^{−1}. On |z| = δ_r,
|ζ^{1/2}| = n|f|^{1/2} ≍ n, and P₀^∞, (P₀^∞)^{−1}, ρ♮^{±1}, f^{−1/2} are bounded n-free (L1 (iv)); the remainder is O(n^{−K−1}) uniformly.
(Note: (2ζ^{1/2})^{−k} with ζ^{1/2} = nf^{1/2} is n^{−k}(2f^{1/2})^{−k}, so the half-integer powers of ζ give integer powers of n.)
(iv) Paper 2 (eq:he-Phi-large), (eq:he-Phi-small) and L bessel-local (iii) bound (2πn)^{σ₃/2}Φ_α(n²f) as in Paper 2 App B (B2)–(B3); the outer
factors Â♮^{±1}, ρ♮^{±σ₃} are bounded n-free (i), L1 (iv). ∎ (PROVED-mod-cite: L1; Paper 2 L bessel-local, L comparison-parametrix (proofs);
RH_px L4.2(iii) [REVIEWED]; DLMF as quoted in JZC_M4_proof N.6a / CITATIONS.)

*Remark (what depends on β′).* Δ_k♮ depends on β′ only through ρ♮; in the model ρ♮² = (Υ̂/4c)^{1+β′}, which is m4_rh4.py's `rho2` with
al = β′, nu = α — the decoupled model M(β′, α) of JZC_M4 §7. So L2 (iii) is the analytic content of H-d's "M(β′, ν = α)" at the hard edge.

*NUMERICAL* (checks [3], [5], [6], model weight, c = c(p), circle |z| = c/2, central-sector points): |Â♮^{±1}| ≤ 2.4 on
10⁻¹² ≤ |z| ≤ 10⁻² and Â♮₊ = Â♮₋ on the band to 10⁻¹² (all cases); n|J − I| is flat in n = 25…400 (e.g. 1.1270 → 1.1237 at p = 1.5, α = −0.6,
β′ = −2.2) and after subtracting Δ₁♮/n the remainder ratios e(2n)/e(n) are 0.24–0.25 (O(n^{−2})); at α = −½ (Bessel order ½) the Hankel
series terminates and J = I + Δ₁♮/n up to O(e^{−cn}) (remainders 10⁻⁴¹ at n = 400). |P̂₀♮^{±1}||ζ|^{|α|/2}n^{−1/2} ≤ 0.94 for |ζ| ∈ [10⁻⁸, 2],
n ∈ {10, 100, 1000}. Controls (must fail, and do): Δ₁ with ν = β′ in Q₀ leaves an O(1/n) remainder (ratios 0.50); Â_w (with ρ_w) has
|z|^{1/2}|Â_w| growing from 31 to 2.8·10⁹ between |z| = 10⁻² and 10⁻¹² (β′ = −2.1); P̂₀ with ρ_w reaches 10²⁴ in the same normalised size.

**Lemma 3 (Hurwitz lip mismatch).** For z on the lips in U_0 ∩ ℂ_±, |ω♮(z) − ϱ_±| ≤ C|z|^{ν_p}log(2/|z|), ν_p = min(1/p, ½), C n-free.
Consequently Paper 2 L lip-mismatch holds for Q♮ with ε_Λ ≡ 0: sup_lips|d_n| ≤ Cε′_n, ε′_n = n^{−2ν_p}log n, and ‖v − ṽ‖_{L^∞(Σ̂)} ≤ C(ε′_n + n^{−1}).
*Proof.* By L1 (ii), ω♮ − ϱ_± = ϱ_±(ρ♮^{−2} − 1), and ρ♮^{−2} = (Υ̂/4c)^{−(1+β′)}·D_{h°}²/h° = (1 + O(|z|^{1/2}))(1 + O(|z|^{ν_p}log(2/|z|))) by
L1 (v) and the proof of L1 (iv) (|Υ̂/4c − 1| ≤ C|z|^{1/2}). |z|^{1/2} ≤ |z|^{ν_p}. The rest is Paper 2's proof (localisation (eq:he-localisation),
super-small E by F4, circles by L2 (iii) at K = 0, Paper 2 L comparison-parametrix (iii) for route A). ∎ (PROVED-mod-cite.)
Equivalently, in Paper 2's four-factor form: the factor x^{β′} gives D_{x^{β′}}²/z^{β′} = e^{∓iπβ′}(1 + O(|z|^{1/2})) (Paper 2's argument is valid
for every real exponent: it uses only (4cz/Υ)^b = (−z)^b(1 + O(|z|^{1/2}))^b with principal powers that multiply on the lips), and the
lip phase e^{±2πiδ} of H-d Lemma (ii) turns e^{∓iπβ′} into ϱ_± = e^{∓iπα}.
*NUMERICAL* (check [4]): ϱ_±ρ♮^{−2} = ω♮ to 6·10⁻⁴¹ (rays ±π/3, ±π/4, |z| = 10⁻²…10⁻¹²); |ω♮ − ϱ_±|/|z|^{1/2} ∈ [0.36, 1.75] (bounded and
converging). Control: |ω♮ − e^{∓iπβ′}| ≥ 0.28 at |z| = 10⁻¹² (does not → 0).

**Lemma 4 (fixed n: the error matrix near 0).** Fix n ≥ n₀ and 1 < s < 1 + 2p. Let R := Q♮P̂₀♮^{−1} in U_0∖Σ. Then for every η > 0,
|R(z)| ≤ C_{n,η}|z|^{−|α|−η}; R − 𝒞_loc(R₋(J_R − I)) (the Cauchy integral over Σ ∩ U(0, ½δ_r) of R's jumps there) has a removable
singularity at 0; R is bounded near 0 up to a logarithm; and R_± ∈ I + ∂𝒞(L²(Σ_R)).
*Proof.* |Q♮| ≤ C_{n,η}|z|^{−|α|/2−η} (G12 P2.4(i)); |P̂₀♮^{−1}| = |adj P̂₀♮| ≤ C_n|z|^{−|α|/2} for fixed n (L2 (iv), ζ ≍ n²z). Inside U_0 the jumps of
R are J_R = P̂₀♮₋(v_{Q♮}v_{P̂}^{−1})P̂₀♮₋^{−1}: on the band none (equal jumps J), on the lips and on (−δ_r, 0) the super-small parts (F4, h_n^δ's jump),
so |J_R − I| ≤ C_n|z|^{−|α|}e^{−n|z|^{−1/p}/C} and R₋(J_R − I) is bounded and Hölder on Σ ∩ U(0, ½δ_r). Its Cauchy integral is O(1 + |log|z||)
near the vertex 0. The difference has no jump in U(0, ½δ_r)∖{0} and is O(|z|^{−|α|−2η}) with |α| + 2η < 1, hence removable. Square
integrability of R_± − I on Σ_R then follows near 0, and away from 0 from G12 P2.4(ii)–(iii) and the boundedness of P̂^{±1} off 0;
membership in I + ∂𝒞(L²) is Paper 2 L B-cauchy (c) as in Cor L2 (at ∞, R = Q♮(P₀^∞)^{−1} = I + O(1/z)). ∎ (PROVED-mod-cite: G12 P2.4,
Paper 2 L B-cauchy (c).)
*Where |β′| would bite.* With the naive bound |Q| ≤ C|z|^{−|β′|/2−η} the product exponent is (|β′| + |α|)/2 + η, which is ≥ 1 for α = −½,
δ = −0.8 (1.3): neither removability nor L² would follow. In the α-frame the exponent is |α| + η < 1 for every δ.

## 3. The proposition

**Proposition G1u (n-uniform hard-edge comparison for the Hurwitz problem, p > 1).** Let p > 1, −1 < δ ≤ 0, 1 < s < 1 + 2p (so
α ∈ (−1, 1) and β′ = α + 2δ ∈ (−3, 1), with |β′| ≥ 1 allowed), and let Q♮ be the Hurwitz Q-matrix of frame 1 (H-d Lemma; G12 P2.4).
With H-a (JZC_M3a_H_Ha.md) (fixed per Rule R review A of the p>1 chain, G1u-2), there is n₀ = n₀(p, s, δ) such that
for n ≥ n₀:

**(A) (Paper 2 §7 verbatim.)** Prop UR-comparison holds for the comparison problem Q̃ built with A₀, Φ_α at 0 and the Airy parametrix with
ω♮ = ω^{(β′)} at 4c; Thm UR-true holds for Q♮ (‖(1 − 𝒞_{v♮})^{−1}‖ ≤ 2C); and
  (Q♮)₁ = P₁ + Ξ₁♮ + O(n^{−1−2ν_p}log n + n^{−2}),  (Q♮)₂ = P₂ + Ξ₂♮ + ((Q♮)₁ − P₁)P₁ + O(n^{−1−2ν_p}log n + n^{−2}),
where Ξ_k♮ are the circle terms (eq:he-Xi) of Q̃. The hard-edge part of Ξ_k♮ is the lattice-α one (weight-free); the soft-edge part
uses ω^{(β′)}. In particular n^pb_n(σ^δ) = c(p)(1 + O(1/n)) and n^pa_n(σ^δ) = 2c(p)(1 + O(1/n)).

**(B) (order K, the input to H-e.)** Let R := Q♮P̂^{−1} with P̂ = P̂₀♮ (L2) in U_0, Paper 2's P̂_r (with ω♮ = ω^{(β′)}) in U(4c, ε), P₀^∞ elsewhere;
circles clockwise. Then, uniformly in n ≥ n₀:
- on ∂U_0: J_R = I + Σ_{k≤K}Δ_k♮n^{−k} + O(n^{−K−1}) (L2 (iii)); on ∂U(4c, ε): N.6a's soft-edge expansion with (−ω^{(β′)})^{±1/2};
- in U_0: |J_R − I| ≤ C_Kn^{−K}min(1, |z|^K) for every K (super-small entries ≤ Ce^{−n|z|^{−1/p}/C}, amplified by |P̂₀♮^{±1}|² ≤ Cn|z|^{−1}…,
  L2 (iv); as RH_px L4.3);
- elsewhere |J_R − I| ≤ Ce^{−n/C}, resp. Cn^{−pn/4} on the top segment (F5 for Q♮);
- so ‖J_R − I‖_{L¹∩L²∩L^∞(Σ_R)} = O(1/n), ‖𝒞₋‖ ≤ C (F1: contour geometry only), R₋ = (1 − 𝒞_{J_R})^{−1}I (L4 for the identification),
  ‖R₋ − I‖_{L²} = O(1/n),
and the residue recursion of JZC_M4_proof Prop N.6c holds with Δ_k♮ in place of Δ_k:
  R = I + Σ_{k≤K}R^{(k)}n^{−k} + O(n^{−K−1})  uniformly at distance ≥ d from Σ_R, and R₁ = Σ_{k≤K}R₁^{(k)}n^{−k} + O(n^{−K−1}).
With the band-factor input H-c (Δ_k♮ = G_{μ^δ}Δ_k^{mod,β′}G_{μ^δ}^{−1} + O(n^{−(J+1)p}), E3 L E3.4–E3.5 and the Hurwitz analogue of F.1′), this is
Prop N.6c for M(β′, ν = α) with remainder **O(n^{−K−1} + n^{−1−(J+1)p})** — the same exponents as for the lattice. Input for the
step to Theorem N.6(i): E3 Lemma E3.7 for M(β′, α) (the n⁻¹ coefficient is d₁ + cpM_μ(4c), exactly linear in μ; JZC_M3a_H.md §3.3,
exact check checks/m3a_e37_decoupled.out) (fixed per Rule R review A of the p>1 chain, G1u-2 / C-2).

*Proof.* (A) By §1 every item of Paper 2 §7 used in UR-comparison, UR-true and Prop moments holds for Q♮: the comparison problem
is the lattice-α one at 0 and has a bounded (−ω♮)^{±1/2} at 4c (App B "the two instances": "No α is involved" at the soft edge, and at
the hard edge (B2)–(B3) are (eq:he-Phi-large/small) with β = α/2); Q♮_± ∈ I + ∂𝒞(L²) (G12 P2.4, Cor L2); L3 replaces L lip-mismatch,
with ε_Λ ≡ 0 (ℓ₁ ≡ 1: r_n ≡ 1). The proof of Prop moments uses only (eq:he-main-bound), (eq:he-column-bound) — products of 𝔪_n with
bounds on Q̃, which is weight-free near 0 — and these. The extraction is F8 (G12 C1.5). The O(1/n) for b_n, a_n: Q_k = P_k + O(1/n)
and (P₁)₁₂(P₁)₂₁ = c², 𝖺(P₀^∞) = 2c.
(B) The circle expansion is L2 (iii) (and N.6a at 4c with ω^{(β′)}, bounded above and below there: L szego (vi)(b) with q₁ = x^{β′}Ĥ°).
The bound in U_0 is L2 (iv) times F4 (and the h_n^δ jump on (−δ_r, 0)): |P̂₀♮₋|·|P̂₀♮₋^{−1}| ≤ Cn|ζ|^{−|α|} ≤ Cn^{1−2|α|}|z|^{−|α|} for |ζ| ≤ 2
and ≤ C|z|^{−1/2} for |ζ| ≥ 2, against e^{−n|z|^{−1/p}/C}: since sup_{0<r≤δ_r} r^{−m}e^{−nr^{−1/p}/(2C)} ≤ C_mn^{−mp}, every power of n and of
|z| is absorbed, giving C_Kn^{−K}min(1, |z|^K). The far arcs are F5. Identification: L4 (fixed n). The small-norm and induction steps
of N.6c are then verbatim (they use only these jump bounds, ‖𝒞₋‖ ≤ C, and the meromorphy of Δ_k♮ in U_0: the model Δ_k^{mod,β′} is
N.6b's object at β = β′, which is β-free in its proof). ∎ (PROVED-mod-cite; REVIEWED per Rule R review A of the p>1 chain; inputs listed
in §4.)

**p < 1 (what changes).** The local analysis in U_0 (L1–L3, L2's parametrix, the circle expansion) is p-free once f, the lattice φ and
the bounds (O3)–(O4) for H_n^δ are given; G3 Lemma 3 supplies the latter with the seam construction. Check [2]–[6] pass at p = 0.6,
β′ = −2.1. What is *not* available for p < 1:
- the a-priori bound (H-b′ for p < 1, JZC_M3a_H §4 item 2), used in route A (UR-true, Prop moments: Q♮_± ∈ I + ∂𝒞(L²)) and in L4;
- E_plt1 Lemma F.1(iv) with the complex seam densities (item 3), used for the band-factor gauge in route B;
- E_plt1's glued parametrix (L E′.3) must be rebuilt with W̃♮; its glue jumps are super-small and the amplification is L2 (iv)'s, so no new
  exponent issue is expected, but this was not written out.
So for p < 1 Proposition G1u is CONDITIONAL on items 2–3 (and the glue), with the same statement. (Parallel work on items 2–3 appears
in checks/m3a_g23_*.py; not read here.)

**α ≥ 1 (s ≥ 1 + 2p).** Not covered: G12's P2.4 and L4 use |α| < 1. In the N.6 route the lattice identification (RH_px §5) works for every
α > −1 by un-lensing; the α-frame identity F♮W̃♮ = F_δ·(−z)^{α/2}(4c − z)^{1/2}(𝗐_nh_n^δ)^{1/2} (L1 (i)) gives, off the lens, R = O_n(1 + |z|^α)
(Bessel factorisation L bessel-local (i) and the Hurwitz sum bound G12 L2.1, which hold for all α > −1), which suggests the same, but the
in-lens part was not done. OPEN.

## 4. Inputs and labels

Proposition G1u (A) uses: Paper 2 §6–7 and App A–C (as read; labels as in the repo), G12 P1.4, C1.5, L2.1–L2.3, P2.4 (PROVED-mod-cite,
NOT REVIEWED), H-d Lemma (i)–(iii) (PROVED for the jump algebra, REVIEWED: Rule R review A of the p>1 chain), L1–L4 above, H-a
(JZC_M3a_H_Ha.md) (fixed per Rule R review A of the p>1 chain, G1u-2).
(B) additionally uses JZC_M4_proof N.6a–c (PROVED-mod-cite; review A done), RH_px §4.1–§5 [REVIEWED], E_pgt1 L E.3, and the band-factor
input H-c for δ (JZC_M3a_H §2, §3.2: the gauge Δ_k = G_μΔ_k^{mod}G_μ^{−1} + O(n^{−(J+1)p}) with the Hurwitz moments).
Label: **(A), (B) PROVED-mod-cite (inputs H-a, H-c as above)** (fixed per Rule R review A of the p>1 chain, G1u-2); **REVIEWED** (Rule R review A of the p>1
chain, fixes applied 2026-10-21). Novelty: UNCHECKED.

Effect on Theorem H (JZC_M3a_H §4): item 1 is closed for p > 1, 1 < s < 1 + 2p. (i) for p > 1 rests on H-a (JZC_M3a_H_Ha.md), the
band-factor input H-c (JZC_M3a_H_Hc.md) and E3.7 for M(β′, α) (JZC_M3a_H §3.3); for p < 1 on items 2–3 and the glued parametrix
(status updated 2026-10-21 after Rule R review A of the p>1 chain).

## 5. Numerical checks (Rule N: NUMERICAL, not certified)

**m3a_g1u_hardedge.py/.out** (mpmath dps 40; model weight z^{β′}(4c − z); f from μ* as in m4_rh4.py; Ψ_α by mpmath Bessel functions in
the central sector; 110 assertions, ALL PASSED; 34 of them are controls that must fail and do). Parameters (p, α, δ): (1.5, −½, −0.8), (1.5, −0.6, −0.8),
(3, −½, −0.8), (3, −0.3, −0.9), (1.5, 0.3, −0.3), (3, 0.6, −0.95), (0.6, −½, −0.8), (1.5, −½, 0); β′ = −2.1, −2.2, −2.1, −2.1, −0.3, −1.3, −2.1, −0.5.
- [1] the Szegő exponent function by quadrature equals ½log(4cz/Υ) to 2·10⁻⁴¹ (asserted 10⁻²⁵) (so D_{x^b} = (4cz/Υ)^{b/2} for every real b);
- [2] L1 (iv), (iii) and control; [3] L2 (i) and control; [4] L1 (ii), L3 and control; [5] L2 (iii) for n = 25…400 and control; [6] L2 (iv)
  for n ∈ {10, 100, 1000} and control. Values quoted under the lemmas. The [5] control (Δ₁ with ν = β′) is not asserted at β′ = −α, where
  ν = β′ gives the same Bessel data (fixed per Rule R review A of the p>1 chain, G1u-3, INFO).
Limits: model weight only (H_n^δ ≡ const; its effect is the n-free Hölder factor of L1 (iv), checked by G12 for (O3)–(O4)); central-sector
points only on the circle (the sector-independence of (E.3.1) is check_e_num [2] of Plan 65); finite samples.

**m3a_g1u_endtoend.py/.out** (Hurwitz Jacobi coefficients, n ≤ 1600, via second_order/checks/so_coeffs (K atoms + Gauss–Jacobi tail,
binary128 RKPW); fits by spec_common.fit; runtime ≈ 1 min with the cached coefficients, ≈ 15 min to generate them). Results in §5a.

## 5a. End-to-end results (m3a_g1u_endtoend.out: 29 assertions, ALL PASSED; 8 are controls that must fail and do)

α = −½ throughout; fits at K atoms (K → 2K stability asserted at < tol/10 where both were run).

| p, s, δ (β′) | d₁ fit / M(β′, α) | d₂ fit / M(β′, α) | third coefficient fit / prediction | controls (dev/tol) |
|---|---|---|---|---|
| 1.5, 1.75, −0.8 (−2.1) | +0.8250000 / +0.825 | +0.6661447 (hr 3.5·10⁻⁵) / +0.6661458 | ε₁ −0.03666 (hr 1.1·10⁻³) / −0.03665 | lattice d₁ 1.2·10⁵; H2 d₂ 1.7·10⁴ |
| 1.5, 1.75, −0.5 (−1.5) | +0.3750000 / +0.375 | +0.2161454 (hr 3.4·10⁻⁵) / +0.2161458 | ε₁ +0.02798 / +0.02799 | 7.5·10⁴; 8.5·10³ |
| 3, 2.5, −0.8 (−2.1) | +1.6500000 / +1.65 | +1.9920833 (hr 2·10⁻⁸) / +1.9920833 | d₃ +2.1507287 (hr 1.3·10⁻⁵) / +2.1507292 | 2.4·10⁵; 2.6·10⁴ |
| 3, 2.5, −0.5 (−1.5) | +0.7500000 / +0.75 | +0.5520833 (hr 10⁻⁹) / +0.5520833 | d₃ +0.3776042 (hr 9·10⁻⁷) / +0.3776042 | 1.5·10⁵; 1.25·10⁴ |

So in the regime |β′| ≥ 1, down to β′ = −2.1, the Jacobi coefficients of the actual Hurwitz measures follow M(β′ = α + 2δ, ν = α) to the
third coefficient (d₃ at p = 3 is an m4_rh4 output, not a closed form fitted here), and the lattice (δ ignored) and H2 (Bessel order
shifted with β′) are excluded by 10⁴–10⁵ tolerances. This is evidence for the *conclusion* of Prop G1u + N.6 (and of Theorem H(i)) at
|β′| ≥ 1, not for the uniform bounds themselves. ε₁ is β-free (not discriminating); its prediction uses mpmath's ζ(−p, a), i.e. the
identification of Remark 3.3 (NUMERICAL).

## 6. Rule A (adversarial pass) — log

1. *Shrinking disc / analytic mismatch factor (the brief).* Checked against Paper 2 and N.6: both use fixed discs; n enters only via
   ζ = n²f. The factor G = (−z)^{−δ}D_{x^{2δ}} is not analytic at 0 (G₊G₋ = 1 on the band); the proof needs only boundedness and
   the band relation, both proved (L1). Recorded in §0.
2. *Is the Bessel order forced to be α?* Yes: the lip match ϱ_±^{(ν)}ρ♮^{−2} = ω♮ holds iff e^{∓iπν} = e^{∓iπα}·(phase 1), i.e. ν ≡ ±α mod 2;
   a different order leaves a constant lip mismatch and the Neumann series fails. Check [4] control (ν = β′: |ω♮ − e^{∓iπβ′}| ≥ 0.28)
   and [5] control (Δ₁ with ν = β′: O(1/n) remainder). Data: H-d §4 excluded H3.
3. *β′ < −1, even β′ < −2.* D_{x^{β′}} needs only log x ∈ L¹(dx/√(x(4c−x))) (Paper 2 §6's hypothesis on q), not integrability of x^{β′}.
   Nothing in L1–L4 uses |β′| < 1; checks at β′ = −2.1, −2.2. The constants grow like (1 + √(δ_r/c))^{|1+β′|} ≤ (1 + √(δ_r/c))², δ-uniform.
4. *Principal powers on the lips.* L1 (v) and L3 multiply principal powers; the arguments do not wrap for δ_r small (proof of L1 (v)).
   Check [4] confirms ϱ_±ρ♮^{−2} = ω♮ to 6·10⁻⁴¹ on four rays in both half-planes, down to |z| = 10⁻¹².
5. *α = −½ (the brief's example).* Bessel order ½: a_k(½) = 0 (k ≥ 1), b_k(½) = 0 (k ≥ 2), so J = I + Δ₁♮/n + O(e^{−cn}) on the circle. A first
   version of check [5] asserted an O(n^{−2}) remainder ratio there and failed; the statement is stronger, not weaker (assertion changed
   to "exponentially small", and α = −0.6, −0.3 added for the rate test).
6. *δ → 0⁻ and δ → −1.* n-uniform constants (L1–L3) depend on δ through (O3)–(O4) (G12, δ-uniform constants of L1.2(b)) and |1 + β′| ≤ 2;
   the 1/|sin πδ| blow-up of G12 P1.4(c) enters only fixed-n statements (L4, F8). δ = 0 reproduces Paper 2 (ρ♮ = ρ^{(α)}, ω♮ = ω).
7. *Does App B see ω at the hard edge?* No: Q̃ near 0 is A₀(2πn)^{σ₃/2}Φ_α(n²f), weight-free (Paper 2 (eq:he-P0hat): "contains neither D_W
   nor any other trace of the weight"). At 4c, ω♮ = ω^{(β′)} without phase (H-d §6 item 1: the lips avoid U(4c, h₀)).
8. *Converse direction in L4.* Removability needs an isolated singularity: the super-small jumps are removed first by the local Cauchy
   integral, whose density is bounded and Hölder; at the vertex 0 it contributes only a logarithm. Checked that |α| + 2η < 1 is the only
   condition used.
9. *Rule N.* Controls added for every claim that could pass vacuously; [1] initially returned nan (log 0 at the quadrature end point) and
   was fixed (the failure was reported by the assertion, not swallowed).
10. *Rule X.* hardedge: closed forms vs independent evaluation (quadrature, Bessel functions). endtoend: Jacobi coefficients of the actual
    Hurwitz measures; predictions are closed forms / m4_rh4 outputs; nothing is fitted to the predictions.

## 7. What remains

- (Rule R for L1–L4 and Prop G1u: done, review A of the p>1 chain. H-a and H-c: done, JZC_M3a_H_Ha.md, JZC_M3a_H_Hc.md. The three
  former bullets are deleted (fixed per Rule R review A of the p>1 chain, G1u-2).)
- p < 1: items 2–3 of JZC_M3a_H §4 and E_plt1's glued parametrix with W̃♮ (§3).
- α ≥ 1 (s ≥ 1 + 2p): the in-lens part of the identification in the α-frame (§3). OPEN.
- Route B was checked numerically only for the model weight; a direct numerical check of the Hurwitz R near 0 (fixed n) was not done.

## 8. Corrections and notes for other memos (not edited here)

- **JZC_M3a_H.md §4 item 1** should point here; its expectation ("must be run in the α-frame of the column factorisation, as Prop 2.4 was")
  is confirmed, with a precise location: the α-frame matters only in F7 (G12 P2.4) and in the identification L4; the comparison
  problem and the circle jumps are insensitive to β′ (route A: weight-free; route B: through the bounded ρ♮).
- **JZC_M3a_Hd.md §6 item 4** says "Not tested numerically below β′ = −1." The datum spec_shift_hi δ = −½ (p = 1.5, s = 2, α = −⅓) has
  β′ = −4/3 and is reproduced by H1 in m3a_hd_model.out (d₃ = +0.103299 vs fit +0.10330). So one point below −1 was tested;
  m3a_g1u_endtoend adds β′ = −1.5, −2.1. (Applied in JZC_M3a_Hd.md §6 item 4, 2026-10-21, per Hd-2 of Rule R review A of the p>1 chain.)
- **JZC_M3a_H_G12.md L2.3** is correct as stated (|G| = |4c/Υ|^δ); add, if useful: G = (4c/Υ̂)^δ near 0, G₊G₋ = 1 on the band (G is not analytic at 0).
- **For FIXES (Paper 2, via a human):** none found in §7/App B for this purpose. (Paper 2's L lip-mismatch proof is written for the exponent α
  but is valid verbatim for any real exponent; no change needed.)
