# JZC W, κ-family: the a-priori bound, the transfer of the H-chain, 1 < p < 2, and the p < 1 obstruction (JZC_W_outer §10 items 2, 3, 5)

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_W_kappa_chain_A.md); fixes R1 (Prop K.12′, §4.3), B3, B5, B6 applied
here, B4 in JZC_W_outer.md, B1, B2, B7–B9 in JZC_W_BT.md, 2026-10-22.
Status (2026-10-22): **REVIEWED** (Rule R: independent second reader A re-derived the key steps, re-ran all four checks of this note
(identical outputs, §7), plus an independent spot check of L K.1 (k1.py, no shared code) and of JZC_W_exact WE.1(ii) (we1.py); fixes
applied) for **L K.1–K.10, P K.11, P K.12 (reduction), Prop K.12′, P K.13, and the elementary parts (a), (b) of P K.14** (its
OBSTRUCTION stays an OBSTRUCTION for the lattice-g route). Not reviewed as mathematics: §6.3 (PROOF SKETCH). Prop K.12′ is the
reviewer's own fix text R1 (derived and checked in the review, §2), inserted verbatim; review A notes that a reviewer B may re-read
the assembled chain. Labels per VERIFICATION_POLICY.md; REVIEWED is combined with, and does not upgrade, the labels below.
Novelty: UNCHECKED (no Rule L pass). No claim about RH: no measure built from zeta zeros is used. Checks: `checks/w_kappa_gauge.py/.out`,
`checks/w_kappa_transfer.py/.out`, `checks/w_kappa_apriori.py/.out`, `checks/w_kappa_plt1.py/.out` (§7). Everything attributed to Paper 2
is quoted from papers/paper2/{sec_5,sec_6,sec_7,app_c}.tex as read for this note (read-only). Inputs from this repo are cited with their
labels; the inputs from JZC_W_outer.md (L W-out.0–5, P W-out.3, 5, 7) are REVIEWED by the same review A. The one input of this note that
is still **NOT REVIEWED** is JZC_W_exact Lemma WE.1 (used only in Prop K.12′; elementary, and WE.1(ii) independently spot-checked by
review A to the quadrature floor 6·10⁻¹⁸) (fixed per Rule R review A of the W chain, R1).

**Status of Conjecture W for σ^{δ,κ}** (λ_k = (k + δ)^p + κ, p > 1, −1 < δ ≤ 0, κ ≠ 0, κ > −a^p, 1 < s < 1 + 2p, i.e. |α| < 1; review A
§3) (fixed per Rule R review A of the W chain, B3):
- *first order in the poles:* n^pb_n(σ^{δ,κ})/c = 𝔅_n[M(α + 2δ, α); t] + Σ_m(the continued symbolic-j layer at j = q_m with μ = −τ_mn^{−pq_m},
  leading term pR_{q_m}W(q_m)π cot(πq_m)(n/N)^pN^{−1−pq_m}) + **O(n^{−2p})** — **PROVED-mod-cite + REVIEWED** (P K.12 + Prop K.12′), with the
  single unreviewed input WE.1; no hypothesis (BT, BT₀, BT_coh, (F-br)) is used;
- *W's displayed form* (pole term at leading order, (1 + O(N^{−1}))): the same with remainder **O(n^{−1−p})**: κ-free Szegő shift
  β′ = α + 2δ, every n^{−k} coefficient with k < p equal to that of M(α + 2δ, α), and the single pole term at n^{−p} with W's exact
  coefficient;
- *not covered:* second order in the poles (products, O(n^{−2p})); p < 1 (OBSTRUCTION for this route, P K.14); p = 1/m; α ∉ (−1, 1);
  non-coherent branched tilts ((F-br) for general branched band factors stays a GAP; irrelevant to this family). Novelty UNCHECKED.

| # | Statement | Label |
|---|---|---|
| **L K.1** | closed form of the gauge on \|z\| < \|z_*\|: 𝒞[ρ₁](z) = 𝒞(0) − ζ(0, a)log(1 − z/z_*) + (π/sin(π/p))ρ₁⁻(z), ρ₁⁻ := n(−z)^{−1/p}(1 − (1 − z/z_*)^{1/p}); hence Ψ₀ = 𝒞(0) + π cot(π/p)ρ₁ − ζ(0, a)log(1 − z/z_*) and H_n^κ = e^{−2𝒞(0)}H_n^δ(ζ(z))(1 − z/z_*)^{1/p−2a}e^{−2π cot(π/p)ρ₁(z)} exactly | PROVED-mod-cite (W_outer L W-out.5, P W-out.5(ii) [REVIEWED]; DLMF-2 for κ < 0) + NUMERICAL + REVIEWED |
| Cor K.1′ | **coherence**: the band tilt and the lip factor of the κ-problem come from one function: τ_m = π cot(πq_m)σ_m, and the hard-edge factor W̃_κ is analytic across (−δ_r, 0) (mod super-small) | PROVED (algebra from L K.1) + NUMERICAL + REVIEWED |
| L K.2 | sum bound (G12 L2.1) for the κ-nodes, exponent α (no δ- or κ-shift) | PROVED + NUMERICAL + REVIEWED |
| L K.3 | lens sectors (G12 L2.2) for the κ-nodes, arcs chosen in t_κ | PROVED-mod-cite (Paper 2 L lenssector, proof; W_outer L W-out.1(c), W-out.2(b)) + NUMERICAL + REVIEWED |
| **L K.4** | X := E_κD_{e^{−2Ψ₀}}: X₊X₋ = 1 on the band, **log X = 𝓡(z)A_X(z) with A_X analytic at 0, \|A_X\| ≤ Cn^{1−p}**, so \|log X\| ≤ Cn^{1−p}\|z\|^{1/2} on U(0, r_*), C n-free, every p > 1 | PROVED-mod-cite (Paper 2 L szego (ii), (eq:szego-repr); L K.1) + NUMERICAL + REVIEWED |
| **P K.5** | **H-b′**: a-priori bound \|Q♮_κ\| ≤ C_{n,η}\|z\|^{−\|α\|/2−η} near 0, Q♮_κ → I at ∞, boundary values; Cor L2 (Q♮_κ± ∈ I + ∂𝒞(L²)) | PROVED-mod-cite (G12 L2.3, P2.4 [REVIEWED]; Paper 2 App C, L szego; L K.2–K.4; W_outer L W-out.3, P W-out.3 [REVIEWED]) + REVIEWED |
| **L K.6** | the κ hard-edge parametrix in the α-frame: ρ♮_κ := W̃_κ/D_W = ρ^♭/X; **exact** lip match ϱ_±ρ♮_κ^{−2} = ω_κ (lip phase e^{±2πi(δ+ρ₁)} included); ρ♮_κ±ρ♮_κ∓ = 1; \|ρ♮_κ\|^{±1} ≤ C n-free; \|ω_κ − ϱ_±\| ≤ C\|z\|^{ν_p}log(2/\|z\|), C n-free; G1u L2 (i)–(iv) for P̂₀^κ | PROVED-mod-cite (G1u L1–L3 [REVIEWED]; L K.4) + REVIEWED |
| L K.7 | fixed n: R := Q♮_κP̂^{−1} is O_{n,η}(\|z\|^{−\|α\|−η}) near 0, R± ∈ I + ∂𝒞(L²) | PROVED-mod-cite (G1u L4 [REVIEWED]; P K.5) + REVIEWED |
| P K.8 | (A) Paper 2 §7 for the κ-problem: **n^pb_n(σ^{δ,κ}) = c(p)(1 + O(1/n)), n^pa_n = 2c(p)(1 + O(1/n))**, every p > 1; (B) the order-K small norm with circle data Δ_k^κ | PROVED-mod-cite (G1u (A), (B) [REVIEWED]; JZC_M4_proof N.6c [REVIEWED]; L K.6–K.7) + REVIEWED |
| L K.9 | the coherent BT model BT_coh: its circle data are meromorphic in both discs (N.6b holds); for a non-coherent pair (σ_ρ ≠ (τ_ρ/π)tan(πρ)) Δ₁ jumps across (−δ_r, 0) **for the lip-matched parametrix**; JZC_W_BT Lemma BT.1 gives a meromorphic alternative with an explicit lip term (Theorem BT) (fixed per Rule R review A of the W chain, B6) | PROVED-mod-cite (JZC_M4_proof N.6b's parity argument [REVIEWED]); "non-coherent" part PROVED (elementary) + NUMERICAL; both + REVIEWED |
| **L K.10** | **transfer** (Hc.3 + G1u to the composite band factor and the lip factor): uniformly on both circles, Δ_k^κ = Δ_k^{BT_coh} + O(n^{−(J+1)p}) (M ≥ J + 1 branched terms), and Δ_k^κ = Δ_k^{M(β′,α)} + O(n^{1−p}) | PROVED-mod-cite (Hc.2, Hc.3 [REVIEWED]; L K.1; P W-out.5 [REVIEWED]) + NUMERICAL + REVIEWED |
| **P K.11** | **P W-out.6 (iii) without BT₀**: n^pb_n(σ^{δ,κ})/c = 𝔅_n[M(α + 2δ, α)] + O(n^{−p}); the n^{−k} coefficients, k < p, are those of M(α + 2δ, α) (κ-free) | PROVED-mod-cite (P K.8(B), L K.10, N.6b–c [REVIEWED]; W_outer inputs REVIEWED) + REVIEWED |
| **P K.12** | **P W-out.6 (ii)**: n^pb_n/c = 𝔅_n^{rec}[BT_coh] + O(n^{−K−1} + n^{−1−(J+1)p}); with Prop K.12′ this is W at first order in the poles, remainder O(n^{−2p}) (refined form, continued pole dressing), resp. O(n^{−1−p}) in W's displayed form (fixed per Rule R review A of the W chain, B3) | (reduction) PROVED-mod-cite + REVIEWED; (ii) PROVED-mod-cite + REVIEWED via Prop K.12′ (input WE.1 NOT REVIEWED; was CONDITIONAL on BT_coh) |
| **Prop K.12′** | **BT_coh at the order P K.12 needs**: 𝔅_n^{rec}[BT_coh] = 𝔅_n[M(β, ν); μ_n] − Σ_ρ(pρW(ρ)/2)τ_ρn^{−1−pρ} + O(n^{−2−p·min𝓡}); refined: first-order part = Σ_ρ(engine symbolic-j layer at j = ρ, μ = −τ_ρn^{−pρ}) to all orders in 1/n, remainder O(n^{−2−2p·min𝓡}); so Hypothesis BT_coh holds with η = 1 (fixed per Rule R review A of the W chain, R1) | PROVED-mod-cite (JZC_W_BT BT.1(iii), BT.5 [REVIEWED]; JZC_W_exact WE.1 [NOT REVIEWED]; m3a_e37_decoupled route 1, N.6b, N.6c [REVIEWED]) + REVIEWED (reviewer A's own fix text, §2 of the review) |
| P K.13 | 1 < p < 2: (O3) with ν_p **fails** for H_n^κ (exponent q₁ = 1 − 1/p < ½), but every use of ν_p in Paper 2 §6–§7/App C and in G12/G1u/Hc survives, because the lip coefficient carries the gauge only through X (exponent ½, L K.4); no restriction on p > 1 is needed | PROVED-mod-cite + NUMERICAL + REVIEWED |
| **P K.14** | p < 1: the gauge density is forced to be ρ₁ (any frame-compatible gauge); on the Bessel scale \|ρ₁\| ≍ \|κ\|n^{(1−p)(2+p)/p} → ∞; the lip entries are unbounded (κ > 0) or vanish (κ < 0) at the hard edge, H_n^κ(0⁺) does not exist unless cot(π/p) = 0, and 𝒞[ρ₁] does not exist for p ≤ ½ | (a), (b) PROVED (elementary) + NUMERICAL + REVIEWED; failure of the lattice-g route: OBSTRUCTION (for this route) |
| §6.3 | fix: the n-dependent constrained equilibrium g_κ (saturated-region jump 2iθ_κ/n), gauge only beyond z_* | PROOF SKETCH (not a proof) / HEURISTIC |
| §7 | 4 scripts, assertion counts and controls in §7 | NUMERICAL |

**Main outcome.** For p > 1 the reduction of JZC_W_outer P W-out.6 is now: (iii) PROVED-mod-cite (no hypothesis, P K.11), and (ii)
PROVED-mod-cite (P K.12 + Prop K.12′; formerly CONDITIONAL on **BT_coh** (§4.1), BT restricted to the coherent tilts τ_ρ = π cot(πρ)σ_ρ).
In that subfamily the circle data are meromorphic, so the obstacle named in JZC_W §5.1 item 4 ("N.6b's meromorphy argument does not
apply") does not arise; the first-order value of the residue recursion in the branched data that BT_coh asked for is supplied by Prop K.12′
(JZC_W_BT BT.1/BT.5 + JZC_W_exact WE.1 + the decoupled E3.7 identity, m3a_e37_decoupled route 1). Precisely: W holds for σ^{δ,κ} at first
order in the poles with remainder O(n^{−2p}) when the pole layer is taken with its continued dressing, and with remainder O(n^{−1−p}) in W's
displayed form (pole term × (1 + O(N^{−1}))); it does **not** hold "to N.6's orders in the integer and Toda layers" beyond O(n^{−2p}), where
second-order branched terms enter (fixed per Rule R review A of the W chain, B3). 1 < p < 2 needs no restriction. p < 1 is obstructed for the lattice-g route at the Bessel scale, with a precise exponent.

## 0. Setting, notation, and what is reused

**Setting (S)** (as JZC_W_outer §0): p > 1 (p < 1 only in §6); −1 < δ ≤ 0, a := 1 + δ; κ ≠ 0, κ > −a^p; 1 < s < 1 + 2p,
α := (s − 1 − p)/p ∈ (−1, 1), β′ := α + 2δ; σ^{δ,κ} := Σ_kλ_k^{−s/p}δ_{1/λ_k}, λ_k = (k + δ)^p + κ; z_* := n^p/κ, z′ := |z_*|; ζ(z) := z/(1 − z/z_*);
t = nz^{−1/p}, t_κ = t∘ζ; q_m := m − 1/p, q₁ = 1 − 1/p ∈ (0, 1); a_m := −binom(1/p, m)(−κ)^m, so ρ₁(y) = Σ_{m≥1}a_m(y/n^p)^{q_m} = t(y) − t_κ(y)
on (0, z′), and ρ₁(z) := n z^{−1/p}(1 − (1 − z/z_*)^{1/p}) (principal) is its continuation to {|z| < z′}∖(−∞, 0]. c = c(p) is Paper 2's
constant; δ_r, ε, ϑ_lip, ϑ_w, η_* := min(1, 2c), Z(r) := {0 < |z| < r, |arg z| < ϑ_w} as in Paper 2. n ≥ n₀(p, δ, κ, s) throughout; in
particular z′ ≥ 8(4c + 2), so |z/z_*| ≤ ⅛ on |z| ≤ 4c + 2. "n-free" means independent of n.

**From JZC_W_outer (REVIEWED, Rule R review A of the W chain).** L W-out.1 (Möbius index map), L W-out.2 (H-a: W_κ = 𝗐_nz^αr_n, r_n = (1 − z/z_*)^{1/p−1}, residues,
top node X₁ = n^p/(a^p + κ), contour), L W-out.3 (F_κ := Φ_δ∘ζ·K; (b): F_κ/F_δ → 1 at 0 off the lens and (D̃_δB_δ)∘ζ/(D̃_δB_δ) → 1 in it),
P W-out.3 (F♮_κ := F_κG_κ, G_κ = (−z)^{−δ}E_κ, E_κ = exp 𝒞[ρ₁]; (O1) with the lattice phase; regular at z_*, −z′; normalisation),
L W-out.4 (jumps; band weight W₀^κ = 𝗐_nz^{β′}(4c − z)H_n^κ, H_n^κ := r_n(D̃_δB_δ∘ζ)^{−2}e^{−2Ψ₀}, Ψ₀ := 𝒞[ρ₁] ∓ iπρ₁ in ℂ_±; lip (2,1) entries
κ_κ±e^{2nφ}e^{±2πi(δ+ρ₁)}/W₀^κ; in its proof W_κ/F̃♮_κ² = W₀^κe^{∓2πiδ}e^{∓2πiρ₁} in ℂ_±), L W-out.5 (PV lemma), P W-out.5 ((ii): the
finite parts FP_j := FP∫_0^∞ρ₁y^{−j−1}dy (+ the ρ̃ part for κ < 0) equal ζ(0, a)κ^jn^{−jp}/j for every j ≥ 1; (i): the Toda parameters).

**From the H-chain (REVIEWED).** G12 L1.2–L1.3, P1.4, L2.1–L2.3, P2.4; Hc.1–Hc.3; G1u L1–L4, Prop G1u (A), (B); JZC_M4_proof N.6a–c.
**From Paper 2 (quoted as read).**
- (eq:szego): D_q(z) := exp((𝓡(z)/2π)∫_0^{4c}log q(x)dx/(√(x(4c−x))(z−x))), 𝓡(z) := (z(z − 4c))^{1/2} ~ z at ∞; "D_q is analytic and zero-free
  off [0,4c], D_{q₁q₂} = D_{q₁}D_{q₂}, and D_q = q^{1/2} for a constant q. Where log q₀ is Hölder continuous, … D_{q,+}D_{q,−} = q."
- (eq:szego-repr): "for every z ∉ [0,4c] and every number 𝔠, log D_q(z)² − 𝔠 = (𝓡(z)/π)∫_0^{4c}(log q(x) − 𝔠)dx/(√(x(4c−x))(z−x))."
- Lemma szego (ii): "Let ν ∈ (0,1], 𝔐 ≥ 0, 𝔠₀ ∈ ℂ. Suppose log q continues analytically to Z(η_*) and continuously to (0,η_*), with
  |log q(z) − 𝔠₀| ≤ 𝔐|z|^ν and |(log q)′(z)| ≤ 𝔐|z|^{ν−1} there, and |log q(x) − 𝔠₀| ≤ 𝔐(1 + |log(4c−x)|) for ½η_* ≤ x < 4c. Then for
  z ∈ Z(¼η_*)∖(0,∞), |log D_q(z)² − log q(z)| ≤ C𝔐|z|^{min(ν,1/2)}log(2/|z|)." (Constants depend only on c.) Its proof's off-zone bound
  (|x − z| ≥ (x + |z|)/8) is used below verbatim.
- (O3) (sec_5): "For z ∈ 𝒵_n with |z| ≤ 1: |log H_n(z) − log H_n(0⁺)| ≤ C|z|^{ν_p} and |(log H_n)′(z)| ≤ C|z|^{ν_p−1}", ν_p := min(1/p, ½),
  constants n-free. Lemma lip-mismatch (sec_7): "|ω(z) − ϱ_±| ≤ C(|z|^{ν_p}log(2/|z|) + ε_Λ(T_n))", proved with "By (O3)–(O4), Lemma
  szego(ii) applies to q = H°_n with 𝔠₀ = 0, ν = ν_p and 𝔐 = C"; (eq:he-epsprime) ε′_n := n^{−2ν_p}log n + ε_Λ(T_n); Lemma sumbound,
  Lemma lenssector, Prop apriori, Cor L2 (app_c), as quoted in G12 §0 and read again for this note.
- External (Rule C): none beyond those already quoted in the cited notes (DLMF-2 enters only through P W-out.5(ii) for κ < 0).

## 1. The gauge in closed form (Lemma K.1) and coherence

**Lemma K.1.** Assume (S). For |z| < z′, z ∉ [0, z′):
  𝒞[ρ₁](z) = 𝒞(0) − ζ(0, a)log(1 − z/z_*) + (π/sin(π/p))ρ₁⁻(z),   ρ₁⁻(z) := n(−z)^{−1/p}(1 − (1 − z/z_*)^{1/p})   (principal powers),
with 𝒞(0) := lim_{z→0}𝒞[ρ₁](z) ∈ ℝ. Consequently, on 𝒵_n ∩ {|z| < z′}, with ρ₁(z) the continuation above,
  Ψ₀(z) = 𝒞(0) + π cot(π/p)ρ₁(z) − ζ(0, a)log(1 − z/z_*),
  H_n^κ(z) = e^{−2𝒞(0)}H_n^δ(ζ(z))·(1 − z/z_*)^{1/p−2a}·e^{−2π cot(π/p)ρ₁(z)}    (H_n^δ := (D̃_δB_δ)^{−2}, G12 P1.4(a)),
  E_κ(z) = e^{𝒞(0)}(1 − z/z_*)^{−ζ(0,a)}exp((π/sin(π/p))ρ₁⁻(z)).
*Proof.* Fix L < z′ and |z| < L. As in the proof of P W-out.5, split 𝒞[ρ₁] at L; on (0, L), ρ₁ = Σ_ma_mn^{−pq_m}y^{q_m} converges uniformly,
and Lemma W-out.5 (q_m > −1, q_m ∉ ℤ since 1/p ∉ ℤ) applied termwise gives 𝒞[ρ₁](z) = A_L(z) + Σ_ma_mn^{−pq_m}(−π/sin(πq_m))(−z)^{q_m}, where A_L
is analytic on |z| < L (the termwise Taylor series converge absolutely there: |q_m − j| ≥ dist(1/p, ℤ) > 0 and Σ_m|a_m|(L/z′)^m < ∞), and
its Taylor coefficients at 0 are A_L(0) and FP_j (j ≥ 1), independent of L (P W-out.5's proof). By P W-out.5(ii), FP_j = ζ(0, a)(κ/n^p)^j/j for
all j ≥ 1, so A_L(z) = A_L(0) − ζ(0, a)log(1 − z/z_*) on |z| < L (both sides analytic on the disc, equal Taylor series). The branched sum: since
sin(πq_m) = −(−1)^m sin(π/p) and (−z)^{q_m} = (−1)^mz^m(−z)^{−1/p} (principal powers; (−z)^m is an integer power),
  a_mn^{−pq_m}(−π/sin(πq_m))(−z)^{q_m} = (π/sin(π/p))·n(−z)^{−1/p}·a_m(z/n^p)^m,
and Σ_ma_mw^m = 1 − (1 − κw)^{1/p}, which gives (π/sin(π/p))ρ₁⁻(z). ρ₁⁻(z) = O(n^{1−p}|z|^{q₁}) → 0 at 0, so A_L(0) = 𝒞(0); 𝒞(0) is real since
ρ₁ (and ρ̃) are real (𝒞(z̄) = conj 𝒞(z)). Letting L ↑ z′ gives the identity on |z| < z′. In ℂ_±, (−z)^{−1/p} = e^{±iπ/p}z^{−1/p}, so
ρ₁⁻ = e^{±iπ/p}ρ₁(z) and Ψ₀ = 𝒞 ∓ iπρ₁ = 𝒞(0) − ζ(0,a)log(1 − z/z_*) + πρ₁(z)(e^{±iπ/p}/sin(π/p) ∓ i) = 𝒞(0) − ζ(0,a)log(1 − z/z_*) + π cot(π/p)ρ₁(z).
H_n^κ: insert into L W-out.4's definition and use r_n·(1 − z/z_*)^{2ζ(0,a)} = (1 − z/z_*)^{1/p−1+1−2a}. ∎
(PROVED-mod-cite: L W-out.5, P W-out.5(ii) [REVIEWED]. NUMERICAL: w_kappa_gauge [CF], six (p, δ, κ) incl. κ = 2 > a^p and p = 2:
𝒞[ρ₁] by quadrature minus the closed form is constant to ≤ 5·10⁻²⁴ over 7 points (both sides of the band, next to the negative axis,
|z| = 0.6z′); controls: π cot(π/p) in place of π/sin(π/p), and dropping the log term, fail by 10⁻¹–10¹; [PSI] the band identity for Ψ₀.
w_kappa_plt1 [P1g]: the same identity holds numerically at p = 0.75, both signs of κ (not proved here for p < 1).)

So near the band the gauge is elementary: the branched part of log H_n^κ is **exactly** −2π cot(π/p)ρ₁(z) = Σ_mτ_m(z/n^p)^{q_m} with
τ_m = −2π cot(π/p)a_m = 2π cot(πq_m)a_m (P W-out.5(iii)), and the analytic part of the gauge is the single logarithm 2ζ(0, a)log(1 − z/z_*),
whose Taylor coefficients are the gauge shares of the Toda parameters.

**Corollary K.1′ (coherence).** Put σ_m := 2a_m (the lip coefficients of P W-out.6(i)). Then τ_m = π cot(πq_m)σ_m, and in ℂ_±
  ½τ_m(z/n^p)^{q_m} ∓ iπa_m(z/n^p)^{q_m} = (πσ_m/(2 sin(πq_m)))(−z/n^p)^{q_m},  Σ_m(πσ_m/(2 sin(πq_m)))(−z/n^p)^{q_m} = −(π/sin(π/p))ρ₁⁻(z).
So the factor exp(½·band tilt ∓ iπ·lip coefficients) is the single function exp(−(π/sin(π/p))ρ₁⁻), analytic off [0, ∞) in |z| < z′;
its band boundary values multiply to the band tilt e^{−2π cot(π/p)ρ₁(x)}. *Proof.* cot(πq) ∓ i = e^{∓iπq}/sin(πq) and z^qe^{∓iπq} = (−z)^q in
ℂ_±; the sum is the computation in the proof of L K.1. ∎ (PROVED. NUMERICAL: [COH]: jump across (−δ_r, 0) ≤ 4·10⁻²⁶, band product = tilt to
3·10⁻²⁶; control: the non-coherent choice (band tilt, no lip factor) jumps by ≥ 1.04·n^{1−p}|y|^{q₁}.)

## 2. H-b′: the a-priori bound for the κ-problem (fixed n)

Notation of G12 §2 with κ: V♮_κ, Q♮_κ := D_∞^{−σ₃}V♮_κD_W^{σ₃}, D_W := D_{W₀^κ}; U_{j2}(z) = Σ_kw(X_k)U_{j1}(X_k)/(z − X_k), w(X_k) = n^pλ_k^{−s/p}
(L W-out.2); φ₁ := ½ϑ_lip; M_n := max_j max_{[0,X₁]}|U_{j1}|.

**Lemma K.2 (sum bound).** Put c₋ := min(1, 1 + κ/a^p) > 0, c₊ := max(1, 1 + κ/a^p), T := n|z|^{−1/p}. For 0 < |z| ≤ 1, φ₁ ≤ |arg z| ≤ π,
  |U_{j2}(z)| ≤ I₁^κ := (M_n/sin φ₁)[Σ_{λ_k≤T^p}λ_k^{1−s/p} + T^pΣ_{λ_k>T^p}λ_k^{−s/p}] ≤ C_{n,δ,κ}(1 + |z|^α + 𝟙_{α=0}log(1/|z|)).
*Proof.* |z − X| ≥ sin φ₁ max(|z|, X); X_k ≥ |z| ⇔ λ_k ≤ T^p; w(X_k)/X_k = λ_k^{1−s/p}, w(X_k)/|z| = T^pλ_k^{−s/p}: this is I₁^κ (G12 L2.1's first
step verbatim). Since τ_k ≥ a, 1 + κ/τ_k^p lies between 1 and 1 + κ/a^p, so c₋τ_k^p ≤ λ_k ≤ c₊τ_k^p. Hence {λ_k ≤ T^p} ⊂ {τ_k ≤ c₋^{−1/p}T},
{λ_k > T^p} ⊂ {τ_k > c₊^{−1/p}T}, λ_k^{1−s/p} ≤ C(c±)τ_k^{p−s} and λ_k^{−s/p} ≤ c₋^{−s/p}τ_k^{−s}: I₁^κ ≤ C·I₁(Hurwitz, T replaced by c₋^{−1/p}T, resp.
c₊^{−1/p}T), and G12 L2.1's second step (node spacing 1 in τ, T^{1+p−s} = n^{1+p−s}|z|^α) gives the last bound. ∎ (PROVED. NUMERICAL:
w_kappa_apriori [SB].)

**Lemma K.3 (lens sectors).** Paper 2's Lemma lenssector (as modified in G12 L2.2) holds for R built with κ_κ, C = C_{n,η,δ,κ}, with: (1) the
poles of 𝒦_j(s) := U_{j1}(s)W_κ(s)/(e^{2iθ_κ(s)} − 1) in 𝒢 := {r < |s| < δ_s, |arg s| < ϑ_lip} are exactly the X_k ∈ 𝒢 (L W-out.1(c); 𝒢 ∩ Γ_κ = ∅
since z_* > δ_s for κ > 0 and Γ_κ = [−z′, 0] for κ < 0), with residues w(X_k)U_{j1}(X_k) (L W-out.2(b)); (2) δ_s, r chosen with
t_κ(δ_s), t_κ(r) ∈ δ + ℕ + ½ (t_κ(r) is continuous and decreasing in r ∈ (0, z′), → ∞ at 0, so such radii exist arbitrarily close to 0);
(3) on the rays arg s = ±ϑ_lip, |e^{2iθ_κ} − 1|^{−1}·|W_κ(s)| ≤ C exp(−n|s|^{−1/p}/C)|s|^α.
*Proof of the arc bound.* Let s = re^{iψ}, |ψ| ≤ ϑ_lip = π/3, u₀ := t_κ(r) ∈ δ + ℕ + ½, A := n^p/r ≥ n^p ≥ 2|κ|, w := t_κ(s)^p = Ae^{−iψ} − κ.
(i) |w|² = (A − κ)² + 2Aκ(1 − cos ψ) and |w| + |A − κ| ≥ A, so ||w| − u₀^p| ≤ 2A|κ|(1 − cos ψ)/A ≤ |κ|ψ², and
||t_κ(s)| − u₀| ≤ |κ|ψ²/(p(u₀^p/2)^{1−1/p}) (mean value; |w| ≥ u₀^p/2 once u₀^p ≥ 2|κ|π²/9). (ii) |w| ≤ A + |κ| ≤ (3/2)A, so
|sin arg w| = A|sin ψ|/|w| ≥ (2/3)|sin ψ| ≥ (4/(3π))|ψ|; |arg w| < π/2 ≤ pπ/2, so |sin(arg w/p)| ≥ (2/π)|arg w|/p ≥ (2/π)|sin arg w|/p. Hence
v := Im t_κ(s) satisfies |v| ≥ c_p|t_κ(s)||ψ|, c_p := 8/(3π²p). (iii) If |v| ≥ ¼: |e^{2πi(t_κ−δ)} − 1| ≥ 1 − e^{−π/2}. If |v| < ¼: |ψ| ≤ 1/(4c_p|t_κ(s)|)
≤ 1/(2c_pu₀) (by (i), |t_κ(s)| ≥ u₀/2 for u₀ ≥ T₀), so by (i) ||t_κ(s)| − u₀| ≤ 1/32 for u₀ ≥ T₀(p, κ), and |t_κ(s)| − Re t_κ(s) ≤ v²/|t_κ(s)| ≤ 1/32
(u₀ ≥ 4); so dist(Re t_κ(s) − δ, ℤ) ≥ ½ − 1/16 = 7/16 and |e^{2πi(t_κ−δ)} − 1| = 2e^{−πv}|sin π(t_κ − δ)| ≥ 2e^{−π/4}sin(7π/16)
≥ 2e^{−π/4}sin(3π/8) (Paper 2's constant; |sin(x + iy)| ≥ |sin x|). Every arc used has
u₀ ≥ t_κ(δ_s) ≥ T₀ once n ≥ n₀ (t_κ(δ_s) ≥ ½nδ_s^{−1/p}). *Rays.* On arg s = ϑ_lip, (ii) gives Im t_κ(s) ≤ −c_p|t_κ(s)|ϑ_lip, hence |e^{2iθ_κ}| =
e^{−2π Im t_κ} ≥ exp(2πc_pϑ_lip|t_κ(s)|), and |t_κ(s)| ≥ ½n|s|^{−1/p}; mirror for −ϑ_lip. |W_κ(s)| = |𝗐_n||s|^α|r_n(s)| ≤ 2|𝗐_n||s|^α.
The rest of Paper 2's proof (steps (1)–(4), r → 0, the sector Ω_b ∩ U(0, δ_s/2)) is verbatim, with L K.2 in place of Lemma sumbound. ∎
(PROVED-mod-cite: Paper 2 L lenssector (proof), L W-out.1(c), W-out.2(b) [REVIEWED]. NUMERICAL: w_kappa_apriori [AR].)
*Why the arcs must be chosen in t_κ:* with the lattice choice t(r) ∈ δ + ℕ + ½, t_κ(r) = t(r) − ρ₁(r) is off by ρ₁(r) ≍ (κ/p)n^{1−p}r^{q₁}, which is not
small for fixed n and large κ; control [AR] (κ = 60, p = 3, n = 4) fails the bound as required.

**Lemma K.4 (the gauge–Szegő factor).** Assume (S) and let r_* := min(¼η_*, ½δ_r) (so r_* < 4c and r_* < z′/8). Put
  X := E_κ·D_{e^{−2Ψ₀}}   (D of the band function e^{−2Ψ₀(x)} = e^{−2PV𝒞[ρ₁](x)}, x ∈ (0, 4c)).
(i) X is analytic and zero-free in U(0, r_*)∖[0, r_*), has continuous boundary values on (0, r_*), and X₊X₋ = 1 there.
(ii) Let L := log X be the branch with L(z) → 0 as z → 0. Then L = 𝓡(z)A_X(z) with A_X analytic in U(0, r_*).
(iii) |A_X| ≤ Cn^{1−p} on U(0, r_*/2), hence |log X(z)| ≤ Cn^{1−p}|z|^{1/2} there, C = C(p, δ, κ, c) n-free. In particular |X|^{±1} ≤ C n-free and
X = 1 + O(n^{1−p}) uniformly.
*Proof.* Write ℓ(z) := −2(Ψ₀(z) − 𝒞(0)) = −2π cot(π/p)ρ₁(z) + 2ζ(0, a)log(1 − z/z_*) (L K.1), so e^{−2Ψ₀} = e^{−2𝒞(0)}e^{ℓ} and D_{e^{−2Ψ₀}} =
e^{−𝒞(0)}D_{e^ℓ}. *Bounds on ℓ.* On {|z| < z′/2}∖(−∞, 0]: with g(w) := 1 − (1 − w)^{1/p}, |g(w)| ≤ (2/p)|w| and |g′(w)| ≤ 2/p for |w| ≤ ½, so
|ρ₁(z)| = n|z|^{−1/p}|g(z/z_*)| ≤ (2|κ|/p)n^{1−p}|z|^{q₁} and |ρ₁′(z)| ≤ C|κ|n^{1−p}|z|^{q₁−1}; |log(1 − z/z_*)| ≤ 2|κ||z|n^{−p} ≤ 2|κ|n^{1−p}|z|^{q₁}
(|z|^{1/p} ≤ n). So |ℓ(z)| ≤ C n^{1−p}|z|^{q₁}, |ℓ′(z)| ≤ Cn^{1−p}|z|^{q₁−1} (|z| ≤ 1), |ℓ(x)| ≤ Cn^{1−p} on (0, 4c]. Likewise
|𝒞[ρ₁](z) − 𝒞(0)| ≤ Cn^{1−p}|z|^{q₁} (L K.1; |ρ₁⁻(z)| = |ρ₁(z)|).
(i) E_κ is analytic, zero-free off [0, ∞) ∪ (−∞, −z′], with boundary values 𝒞± = PV𝒞 ± iπρ₁ (P W-out.3(a)), so E₊E₋ = e^{2Ψ₀} on (0, r_*).
ℓ is Hölder on [0, 4c] (exponent q₁), so D_{e^ℓ} is analytic, zero-free off [0, 4c] with D₊D₋ = e^ℓ (Paper 2 §6, quoted). Multiply.
(ii) Define L := (𝒞[ρ₁](z) − 𝒞(0)) + ½log D_{e^ℓ}(z)², log D_{e^ℓ}² the exponent in (eq:szego) (analytic off [0, 4c]). L is a logarithm of X.
*Crude bound:* for z ∈ Z(¼η_*)∖(0, ∞), Lemma szego (ii) applies to q = e^ℓ with ν = q₁, 𝔠₀ = 0, 𝔐 = Cn^{1−p} (hypotheses: the bounds on ℓ
above; Z(η_*) ⊂ {|z| < z′/2}), giving |log D_{e^ℓ}² − ℓ(z)| ≤ Cn^{1−p}|z|^{min(q₁,½)}log(2/|z|). For ϑ_w ≤ |arg z| ≤ π, |z| ≤ ¼η_*, (eq:szego-repr) with
𝔠 = 0 and |x − z| ≥ (x + |z|)/8 give |log D_{e^ℓ}²| ≤ C|z|^{1/2}∫_0^{4c}Cn^{1−p}x^{q₁}dx/(√(x(4c−x))(x + |z|)) ≤ Cn^{1−p}|z|^{min(q₁,½)}log(2/|z|)
(the integral of szego (ii)'s proof). So |L(z)| ≤ B(z) := Cn^{1−p}|z|^{min(q₁,½)}log(2/|z|) on U(0, r_*)∖[0, r_*), boundary values included, and
L → 0 at 0. *Jumps:* on (0, r_*), L₊ + L₋ ∈ 2πiℤ by (i), is continuous and → 0, hence ≡ 0; on (−r_*, 0) L is analytic (𝒞[ρ₁] has its
densities on (0, ∞) and (−∞, −z′); D off [0, 4c]). 𝓡 is analytic and zero-free in U(0, r_*)∖[0, r_*), 𝓡₊ = −𝓡₋ on the band, and
|𝓡(z)| ≥ c₀|z|^{1/2}. So A_X := L/𝓡 has continuous boundary values with no jump on (0, r_*) and none on (−r_*, 0): by Morera it is analytic in
U(0, r_*)∖{0}, and |A_X| ≤ B(z)/(c₀|z|^{1/2}) = o(1/|z|) (q₁ − ½ > −1), so 0 is removable.
(iii) On |z| = r_*/2, |A_X| ≤ B/(c₀(r_*/2)^{1/2}) ≤ Cn^{1−p}; maximum principle on U(0, r_*/2); |𝓡(z)| ≤ C|z|^{1/2}. ∎
(PROVED-mod-cite: Paper 2 L szego (ii), (eq:szego), (eq:szego-repr); L K.1; P W-out.3(a) [REVIEWED]. NUMERICAL: w_kappa_gauge [X]:
|log X|/(n^{1−p}|z|^{1/2}) ≤ the values in §7 at n = 4, 16, 64 (n-free), A_X continuous across the band and (−δ_r, 0) to 10⁻¹²; [NU] local
exponent of |log X| on the lip = 0.5 at p = 1.25, 1.5, 3. Control: the rate n^{−p} fails.)

*Remark (why ½ and not q₁).* Each of E_κ and D_{e^{−2Ψ₀}} alone has the exponent q₁ at 0 (E_κ ∋ (π/sin(π/p))ρ₁⁻ ∼ |z|^{q₁}; the band factor
e^{−2Ψ₀} has the Hölder exponent q₁). Their product has no jump-type singularity left: X₊X₋ = 1 makes log X odd across the band, i.e. a
multiple of 𝓡. This is the analytic content of coherence (Cor K.1′): the lip phase e^{±2πiρ₁} cancels the q₁-part of the Szegő remainder.

**Proposition K.5 (H-b′: a-priori bound for the κ-problem).** Fix n ≥ n₀. Then det Q♮_κ ≡ 1 and
(i) for every η > 0, |Q♮_κ(z)| ≤ C_{n,η}|z|^{−|α|/2−η} on U(0, δ_r)∖Σ;
(ii) Q♮_κ is bounded on bounded sets at positive distance from 0, and Q♮_κ → I at ∞;
(iii) Q♮_κ has continuous boundary values on Σ minus its vertices (incl. X₁ + δ′ ± ih₀, X₁ + δ′).
The same holds for (Q♮_κ)^{−1}, and Q♮_κ± ∈ I + ∂𝒞(L²(Σ)) (Cor L2 verbatim: (1 + |α|)/4 < ½).
*Proof.* **Column factorisation.** Write H^♭ := H_n^δ(ζ(z))r_n(z) (Hurwitz∘ζ × density). By L K.1 and L W-out.4,
  W₀^κ = [𝗐_nx^α(4c − x)H^♭]·x^{2δ}·e^{−2Ψ₀},  so  D_W = D^♭_α·D_{x^{2δ}}·D_{e^{−2Ψ₀}}   (multiplicativity),
and F♮_κ = F_κ(−z)^{−δ}E_κ. Hence **F♮_κD_W = (F_κD^♭_α)·G·X**, G := (−z)^{−δ}D_{x^{2δ}} (G12 L2.3) and X of L K.4; in the lens the same with
F̃_κ := F_κ/κ_κ = (D̃_δB_δ)(ζ)K. As in G12 L2.3(ii), near 0 Q♮_κ = (const. diagonal)·U·M₀·(F♮_κD_W)^{σ₃} off the lens and ·(F̃♮_κD_W)^{σ₃} in it,
M₀ ∈ {e^{nφσ₃}, L_±^κe^{nφσ₃}A_±} free of F (lattice φ; A_± contains 1/W_κ).
**Bounds near 0 (n fixed).** |G|^{±1} ≤ 2 on |z| < r_G (G12 L2.3(i)); |X|^{±1} ≤ C (L K.4); |F_κ|^{±1} ≤ C off the lens and |F̃_κ|^{±1} ≤ C in it
(L W-out.3(b) with G12 P1.4(a), (O5) at 0); |D^♭_α|^{±1} ≤ C_{n,η}|z|^{±α/2−η}: Paper 2 L szego (vi), last claim, whose proof uses (i) for D_{x^α},
D_{4c−x} and, for the remaining factor q = H^♭/H^♭(0⁺), Lemma szego (ii) in Z(¼η_*) and (eq:szego-repr) with 𝔠 = 0 off it — the hypotheses
hold since |log H^δ(w) − log H^δ(0⁺)| ≤ C|w|^{1/p} with the derivative bound (G12 P1.4(a), (O3)) at w = ζ(z) (|ζ(z)| ≤ 2|z|, |ζ′| ≤ 2, arg ζ(z) − arg z
= O(|z|n^{−p})), and |log r_n| ≤ C|z|n^{−p}; |1/W_κ| ≤ C|z|^{−α} (|r_n| ≥ ½); U_{j1} bounded; L K.2; L K.3. With these, G12 P2.4(i)'s proof (i.e.
Paper 2's Prop apriori (i) for the pair (F_κ, D^♭_α), times the bounded factor G·X) is verbatim, on |z| < min(δ_s/2, r_G, r_*/2), and the
annulus up to δ_r is covered by (ii).
(ii) Away from 0: U is meromorphic with poles at the X_k, cancelled in R (L W-out.2, P Ha.5); F♮_κ is analytic and bounded above and below
near z_* (κ > 0; z_* > X₁ + δ′ + h₀, outside the contour) and near −z′ (κ < 0) (P W-out.3(c)), and Q♮_κ has no jump on (X₁ + δ′, ∞) or
(−∞, 0) (L W-out.4(g)), so these points are removable for Q♮_κ. Near 4c, the only singular factors occur in F̃♮_κD_W, and
(F̃♮_κD_W)² = W_κ·ω^{(β′)}·e^{±2πi(δ+ρ₁)} (from W_κ/F̃♮_κ² = W₀^κe^{∓2πi(δ+ρ₁)}), ω^{(β′)} := D_W²/W₀^κ, which is bounded above and below on
U(4c, ε) by Lemma szego (vi)(b) applied to q₁ = x^{β′}H_n^κ/H_n^κ(0⁺) (analytic and positive near 4c; |log q₁ − 𝔠₁| ≤ 𝔐 there and
≤ 𝔐(1 + |log x|) on (0, 4c), 𝔐 = C_n; fixed n suffices here), and |e^{±2πiρ₁}| ≤ C. At ∞: P W-out.3(d) (normalisation) gives Q♮_κ =
k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃} → I. (iii) L W-out.4. Cor L2: Paper 2's proof verbatim with (i)–(iii). ∎
(PROVED-mod-cite: G12 L2.3, P2.4 [REVIEWED]; Paper 2 App C, L szego (i), (ii), (vi); L K.2–K.4; L W-out.2–4, P W-out.3 [REVIEWED].)
*What would fail:* the bound with D_W alone (|D_W|^{±1} ≲ |z|^{±β′/2}) gives |z|^{−|β′|/2}, not L² for |β′| ≥ 1 (as in G12 §2); the gauge factor
E_κ alone is bounded but carries |z|^{q₁}-terms — only X = E_κD_{e^{−2Ψ₀}} is used.

## 3. The hard edge in the α-frame (transfer of G1u)

**Lemma K.6.** Assume (S), n ≥ n₀. Put W̃_κ := 𝗐_n^{1/2}(−z)^{α/2}r_n^{1/2}/F̃♮_κ (principal powers; fixed root of 𝗐_n), ρ♮_κ := W̃_κ/D_W,
and W̃^♭, ρ^♭ := G1u's W̃♮, ρ♮ with H_n^δ replaced by H^♭ (Szegő exponent β′, band factor H^♭). On U_0 := U(0, δ_r) (δ_r ≤ r_*/2):
(i) W̃_κ = W̃^♭E_κ^{−1}, ρ♮_κ = ρ^♭/X;
(ii) W̃_κ² = e^{∓iπβ′}e^{∓2πiρ₁(z)}W₀^κ in ℂ_±, hence **ϱ_±ρ♮_κ^{−2} = ω_κ := e^{±2πi(δ+ρ₁(z))}ω^{(β′)}** — exactly the coefficient of e^{2nφ} in the
  main part of Q♮_κ's lip jump (L W-out.4(b) conjugated by D_W^{σ₃});
(iii) ρ♮_κ₊ρ♮_κ₋ = 1 on (0, δ_r); ρ♮_κ has only a super-small jump on (−δ_r, 0);
(iv) |ρ♮_κ|^{±1} ≤ C on U_0∖ℝ, C n-free;
(v) on the lips in U_0 ∩ ℂ_±, |ω_κ − ϱ_±| ≤ C|z|^{ν_p}log(2/|z|), C n-free (Paper 2's (eq:he-mismatch) with ε_Λ ≡ 0);
(vi) P̂₀^κ := Â_κ(2πn)^{σ₃/2}Φ_α(n²f)ρ♮_κ^{−σ₃}, Â_κ := P₀^∞ρ♮_κ^{σ₃}Mf^{σ₃/4}, satisfies G1u L2 (i)–(iv) (Bessel order α), with circle data
  Δ_k^κ := (2f^{1/2})^{−k}P₀^∞ρ♮_κ^{σ₃}(σ₃Ξ_k(α)σ₃)ρ♮_κ^{−σ₃}(P₀^∞)^{−1}: P̂₀^κ(P₀^∞)^{−1} = I + Σ_{k≤K}Δ_k^κn^{−k} + O(n^{−K−1}) uniformly on |z| = δ_r.
*Proof.* (i) F̃♮_κ = (D̃_δB_δ)(ζ)K(−z)^{−δ}E_κ and (D̃_δB_δ)(ζ)^{−1} = H_n^δ(ζ)^{1/2} (the root positive on the band, continued); D_W = D_{W₀^♭}·
D_{e^{−2Ψ₀}} with W₀^♭ := 𝗐_nx^{β′}(4c − x)H^♭. (ii) In ℂ_±, (−z)^α = e^{∓iπα}z^α, so W̃_κ² = e^{∓iπα}W_κ/F̃♮_κ² = e^{∓iπα}e^{∓2πiδ}e^{∓2πiρ₁}W₀^κ
(L W-out.4, proof); then ϱ_±ρ♮_κ^{−2} = e^{∓iπα}D_W²e^{±iπβ′}e^{±2πiρ₁}/W₀^κ. The main lip entry of Q♮_κ is the (2,1) entry of L W-out.4(b) with κ_κ±
replaced by 1 (the rest is E, Paper 2 F1), times D_W². (iii) W̃_κ₊W̃_κ₋ = 𝗐_nx^αr_n/(F̃♮_κ₊F̃♮_κ₋) = W₀^κ (L W-out.4(a)) = D_{W,+}D_{W,−} (log W₀^κ
Hölder: L K.1). On (−δ_r, 0): (−z)^{α/2}, r_n, F♮_κ and D_W are analytic there; F̃♮_κ = F♮_κ/κ_κ and κ_κ±'s ratio is 1 + O(exp(−cn|y|^{−1/p}))
(|e^{∓2iθ_κ}| on the negative axis: arg t_κ = ±π/p + O(|y|n^{−p})). (iv) ρ^♭ is bounded above and below n-free by G1u L1 (iv), whose proof needs
only (O3)–(O4)-type bounds for H^♭ (verified in P K.5's proof, n-free) and |log H^♭°| ≤ C on U_0∖(−δ_r, 0] (G12 L1.2(b), L1.3(iii) at ζ(z));
X by L K.4. (v) ω_κ − ϱ_± = ϱ_±(ρ^{♭−2}X² − 1); |ρ^{♭−2} − 1| ≤ C|z|^{ν_p}log(2/|z|) (G1u L3 for H^♭) and |X² − 1| ≤ Cn^{1−p}|z|^{1/2} (L K.4);
|z|^{1/2} ≤ |z|^{ν_p}. (vi) G1u L2's proof uses exactly (ii)–(iv) (and Paper 2's Bessel facts); the lip match is exact by (ii). ∎
(PROVED-mod-cite: G1u L1–L3 [REVIEWED]; L K.1, K.4; L W-out.4 [REVIEWED].)

**Lemma K.7 (fixed n).** R := Q♮_κ(P̂₀^κ)^{−1} satisfies |R| ≤ C_{n,η}|z|^{−|α|−η} in U_0∖Σ, is bounded near 0 up to a logarithm, and R± ∈ I + ∂𝒞(L²).
*Proof.* G1u L4 verbatim with P K.5(i) and L K.6(vi) (|P̂₀^{κ,−1}| ≤ C_n|z|^{−|α|/2}); inside U_0 the jumps of R are super-small (band: equal jumps;
lips: exact match up to E; (−δ_r, 0): ρ♮_κ's super-small jump). ∎ (PROVED-mod-cite.)

**Proposition K.8.** Assume (S). (A) *(Paper 2 §7, leading order.)* Prop UR-comparison, Thm UR-true and Prop moments hold for Q♮_κ with
ε′_n = n^{−2ν_p}log n; in particular **n^pb_n(σ^{δ,κ}) = c(p)(1 + O(1/n)) and n^pa_n(σ^{δ,κ}) = 2c(p)(1 + O(1/n))**.
(B) *(order K.)* With P̂ := P̂₀^κ in U_0, Paper 2's P̂_r (built with ω^{(β′)}) in U(4c, ε) and P₀^∞ elsewhere, R := Q♮_κP̂^{−1} has: on ∂U_0,
J_R = I + Σ_{k≤K}Δ_k^κn^{−k} + O(n^{−K−1}); on ∂U(4c, ε) N.6a's soft-edge expansion with (−ω^{(β′)})^{±1/2}; in U_0, |J_R − I| ≤ C_Kn^{−K}min(1, |z|^K);
elsewhere |J_R − I| ≤ Ce^{−n/C} (resp. Cn^{−pn/4} on the top segment); ‖J_R − I‖_{L¹∩L²∩L^∞} = O(1/n); R₋ = (1 − 𝒞_{J_R})^{−1}I.
*Proof.* (A) Prop G1u (A)'s proof, item by item (its §1 inventory): F1 (|v^{±1}| ≤ C: |ω_κ|^{±1} ≤ C by L K.6(iv), the phases on Σ^△ and the top
segment bounded, W_outer §4); F4 (super-small entries, multiplied by the bounded e^{±2πi(δ+ρ₁)}); F5 (as in W_outer §4); F7 (P K.5); F8 (P W-out.3(d));
the comparison problem Q̃ is weight-free at 0 and uses ω^{(β′)} at 4c (bounded above and below, P K.5's proof); Lemma lip-mismatch is
replaced by L K.6(v), which is its statement with ε_Λ ≡ 0. Paper 2 §7 uses the Hölder exponent only through that lemma and through
𝔪_n, ε′_n (sec_7 l. 74–77, 337, 460; checked by grep: F2 is not invoked in §7, App B, App C, §8). (B) Prop G1u (B)'s proof with L K.6(vi), K.7,
and P K.5. ∎ (PROVED-mod-cite: Prop G1u (A), (B) [REVIEWED]; L K.6, K.7, P K.5; the W_outer inputs [REVIEWED].)

## 4. The transfer of the gauge to the composite band factor, and the reduction

### 4.1 The coherent BT model

**Definition (BT_coh model).** Let β ∈ ℝ, |ν| < 1, J ≥ 1, μ = (μ_1, …, μ_J) ∈ ℝ^J, 𝓡 = {ρ_1, …, ρ_M} ⊂ (0, ∞)∖ℕ and σ_ρ ∈ ℝ; put
τ_ρ := π cot(πρ)σ_ρ (**coherence**). In the n^p frame, h_BT(z) := exp(−P_μ(z) + Σ_ρτ_ρ(z/n^p)^ρ) (z^ρ principal), W₀^{BT} := 𝗐_nz^β(4c − z)h_BT,
  W̃_BT := 𝗐_n^{1/2}(−z)^{β/2}(4c − z)^{1/2}exp(−½P_μ(z) + Σ_ρ(πσ_ρ/(2 sin πρ))(−z/n^p)^ρ),  ρ_BT := W̃_BT/D_{W₀^{BT}},
(−ω_BT) := (4c/Υ)e^{L₁^{BT}} at 4c (Paper 2 (eq:omega-4c) with q₁ = x^βh_BT), and the circle data Δ_k^{BT} := N.6a's Δ_k^0 with ρ_BT and Bessel
order ν, Δ_k^{r,BT} := N.6a's Δ_k^r with (−ω_BT)^{±1/2}. On the lips the model's lip entry is ϱ_±ρ_BT^{−2} = e^{±iπ(β−ν)}e^{±iπΣσ_ρ(z/n^p)^ρ}D²/W₀^{BT}
(lip (2,1) factor exp(±iπΣσ_ρ(z/n^p)^ρ), as in W_outer's BT). 𝔅_n^{rec}[BT_coh(β, ν; μ, σ)] := c^{−1}·(the value of n^pb_n produced by the
residue recursion of N.6c from these data and the extraction n^{2p}b_n² = (Q₁)₁₂(Q₁)₂₁, Q₁ = P₁ + R₁), as a function of n.

**Lemma K.9 (BT_coh is admissible for N.6c).** For coherent data, every Δ_k^{BT} is meromorphic in U(0, δ_r) with a pole at most at 0, and every
Δ_k^{r,BT} in U(4c, ε) with a pole at most at 4c. For a non-coherent pair (σ_ρ ≠ (τ_ρ/π)tan(πρ) for some ρ, with W̃ fixed by the lip match
W̃² = W₀^{BT}e^{∓iπβ}e^{∓iπΣσ_ρ(z/n^p)^ρ}), Δ₁^{BT} has a jump of size ≍ |τ_ρ − π cot(πρ)σ_ρ|n^{−pρ}|y|^ρ across (−δ_r, 0).
This non-coherent statement is for the lip-matched parametrix; JZC_W_BT Lemma BT.1 gives a meromorphic alternative with an explicit lip
term (Theorem BT): with the analytic-gauge parametrix, non-coherent circle data stay meromorphic and the mismatch moves to a lip term
(fixed per Rule R review A of the W chain, B6).
*Proof.* *Band.* W̃_BT₊W̃_BT₋ = W₀^{BT}(x): (−z)^{β/2}₊(−z)^{β/2}₋ = x^β and (−z)^ρ₊ + (−z)^ρ₋ = 2cos(πρ)x^ρ, so the exponent sums to
−P_μ + Σπ cot(πρ)σ_ρx^ρ = log h_BT − 0 (Cor K.1′'s computation); D_{W,+}D_{W,−} = W₀^{BT} (Hölder log). So ρ_BT₊ρ_BT₋ = 1, and the parity
argument of N.6b (p < 1 bullet: "σ₃Ξ_kσ₃ … commutes or anticommutes with J as (−1)^k. f^{1/2}₊ = −f^{1/2}₋ on (0, δ), and the ρ² relations …
hold, so Δ_k^0 has no jump on (0, δ)") applies verbatim. *Negative axis.* By coherence W̃_BT is analytic off [0, ∞) (no z^ρ with a cut on
(−∞, 0) remains), D_{W₀^{BT}}, P₀^∞, f^{1/2} are analytic there: no jump. *At 0:* |ρ_BT|^{±1} ≤ C near 0 (|W̃_BT| ≍ |z|^{β/2} ≍ |D|), |P₀^∞| ≤ C|z|^{−1/4},
|f^{−k/2}| ≤ C|z|^{−k/2}: polynomial growth, so a pole. *Soft edge:* h_BT is analytic near 4c; N.6b's soft-edge bullet verbatim.
*Non-coherent:* then the W̃ forced by the lip match on both lips is W̃ = W̃_BT·exp(Σ_ρc_ρ(z/n^p)^ρ) in both half-planes, c_ρ := ½(τ_ρ − π cot(πρ)σ_ρ),
z^ρ principal (since ½τz^ρ ∓ ½iπσz^ρ = (πσ/(2 sin πρ))(−z)^ρ + c_ρz^ρ in ℂ_±); its boundary values on (−δ_r, 0) differ by the factor
exp(2iΣ_ρc_ρ sin(πρ)|y|^ρn^{−pρ}) ≠ 1; since
σ₃Ξ₁(α)σ₃ = Q₀/16 has non-zero off-diagonal entries (Q₀ = [[−(1+4α²), 2i], [2i, 1+4α²]], G1u L2 (iii)), conjugation by different ρ^{σ₃} from
the two sides changes Δ₁. ∎ (PROVED-mod-cite: N.6b [REVIEWED]. NUMERICAL: [COH].)

**Hypothesis BT_coh (the coherent case of W_outer's BT; was a HYPOTHESIS, now PROVED-mod-cite with η = 1 by Prop K.12′, §4.3)** (fixed per
Rule R review A of the W chain, R1). For p > 1, |ν| < 1, β ∈ ℝ, μ_{n,j} = O(n^{−jp}), coherent bounded
(σ_ρ)_{ρ∈𝓡}:
  𝔅_n^{rec}[BT_coh(β, ν; μ_n, σ)] = 𝔅_n[M(β, ν); μ_n] − Σ_{ρ∈𝓡}(pρW(ρ)/2)τ_ρ(n/N)^pN^{−1−pρ} + O(n^{−1−p·min𝓡−η})   (some η > 0).
(W_outer's BT allows independent σ_ρ; by L K.9 those models are not meromorphic, and they are not needed for the κ-family.)
*Cross-reference (read 2026-10-22; originally not used in any proof here, now used in Prop K.12′):* JZC_W_BT.md (BT.1, BT.3 (i), (iii), BT.5
REVIEWED by the same review A; written in parallel) states as its Prop BT.5 the same relation in its notation (tilt e^{−μz^ρ}, lip e^{±iπσz^ρ}: no lip mismatch iff μ tan πρ + πσ = 0, i.e. τ = π cot(πρ)σ with τ = −μ) and
treats the non-coherent case by a lip-mismatch "companion". The two derivations are independent; they agree on the coherence condition.

### 4.2 The transfer

**Lemma K.10 (transfer of Hc.3/G1u to the κ-problem).** Assume (S), J ≥ 1, M ≥ J + 1, and let μ^κ_{n,j} := (2Z_κ(−j)/j − B_j)n^{−jp} (P W-out.5(i), with
the Fourier-sum constants m_k(δ) of Hc.2 for ζ(−kp, a)/(kn^{kp})), σ_m := 2a_m (m ≤ M), BT_coh := BT_coh(β′, α; μ^κ_n, (σ_m)_{m≤M}) on 𝓡 = {q_1, …, q_M}.
Uniformly on ∂U_0 = {|z| = δ_r} and ∂U_r = {|z − 4c| = ε} (boundary values included) and in n ≥ n₀, for every fixed k:
(a) ρ♮_κ = ρ_BT·exp(∓iπ tail_M(z) − ½T(z)) in ℂ_±, (−ω^{(β′)})^{1/2} = (−ω_BT)^{1/2}e^{½T(z)}, where tail_M := Σ_{m>M}a_m(z/n^p)^{q_m} and
  T(z) := (𝓡(z)/π)∫_0^{4c}(E(x) − E(z))dx/(√(x(4c−x))(z − x)),  E := log H_n^κ − log h_BT (continued from the band; E(z) the value at z);
(b) |tail_M| ≤ Cn^{1−p(M+1)} and |T| ≤ Cn^{−(J+1)p} on both circles; hence **Δ_k^κ = Δ_k^{BT_coh} + O(n^{−(J+1)p})** and Δ_k^{r,κ} = Δ_k^{r,BT_coh} + O(n^{−(J+1)p});
(c) (comparison with M(β′, α) itself) with BT_coh replaced by the model M(β′, α) (h ≡ const, no lip factor): ρ♮_κ = ρ^{mod,β′}exp(∓iπρ₁(z) − ½T₀(z)),
  T₀ the same transform of E₀ := log H_n^κ, and |ρ₁|, |T₀| ≤ Cn^{1−p} on both circles: **Δ_k^κ = Δ_k^{M(β′,α)} + O(n^{1−p})**.
*Proof.* (a) By L K.1 and L K.6(i), log W̃_κ = ½log 𝗐_n + (β′/2)log(−z) + ½log(4c − z) + ½λ^♭(z) − (𝒞[ρ₁](z) − 𝒞(0)) + const with λ^♭ := log H^♭
(continued; super-small jump on (−δ_r, 0)), and −(𝒞 − 𝒞(0)) = ζ(0, a)log(1 − z/z_*) − (π/sin(π/p))ρ₁⁻(z). By Cor K.1′, −(π/sin(π/p))ρ₁⁻ =
Σ_{m≤M}(πσ_m/(2 sin πq_m))(−z/n^p)^{q_m} + [½Σ_{m>M}τ_m(z/n^p)^{q_m} ∓ iπ tail_M(z)] in ℂ_±. Hence log W̃_κ − log W̃_BT = ½E(z) ∓ iπ tail_M(z) + const,
where on the band E = λ^♭ + 2ζ(0, a)log(1 − x/z_*) + P_{μ^κ}(x) + Σ_{m>M}τ_m(x/n^p)^{q_m} + const = log H_n^κ − log h_BT + const (L K.1). By
multiplicativity D_W/D_{W₀^{BT}} = D_{e^E}, and (eq:szego-repr) with 𝔠 = E(z) gives log D_{e^E}² = E(z) + T(z). Constants cancel (D_c = c^{1/2}). So
log(ρ♮_κ/ρ_BT) = ∓iπ tail_M − ½T. At 4c, L₁ is additive in log q₁ and the lips avoid U(4c, h₀) (no lip factor): L₁^κ − L₁^{BT} = T.
(b) tail_M: |a_m(z/n^p)^{q_m}| = |a_m|(|z|/n^p)^m·n|z|^{−1/p} with |a_m| ≤ |κ|^m, so on |z| ≤ 4c + 1 the sum over m > M is geometric (ratio
≤ |κ|(4c + 1)n^{−p} ≤ ½) and |tail_M| ≤ 2(|κ|(4c + 1))^{M+1}n^{1−p(M+1)}|z|^{−1/p}; on the circles |z| ≥ δ_r: |tail_M| ≤ Cn^{1−p(M+1)}.
T: Hc.3 Step 2 verbatim, given (α) sup_{|z|≤R₁′}|E| ≤ Cn^{−(J+1)p} (R₁′ := 4c + 1, boundary values on (−R₁′, 0) included) and (β) |E′| ≤ Cn^{−(J+1)p}/η on the
convex discs U(x₀, 2η₀), x₀ ∈ {δ_r, 4c − ε}, at distance ≥ η from (−∞, 0]. Write E = E₁ + E₂ + E₃ + const with
- E₁ := −2[G_δ(ζ(z)) − G_δ(ζ(1)) − Σ_{k≤J}m_k(δ)(ζ(z)^k − ζ(1)^k)]: Hc.2 (ii) at w = ζ(z) (|ζ(z)| ≤ R₁ = 4c + 2 for |z| ≤ R₁′; ζ maps ℂ_± into ℂ_± and
  (−R₁′, 0) into (−R₁, 0), so boundary values go to boundary values; ζ(U(x₀, 2η₀)) lies at distance ≥ η/2 from (−∞, 0] and |ζ′| ≤ 2): (α), (β);
- E₂ := −2Σ_{k≤J}m_kζ(z)^k + log r_n + 2ζ(0, a)log(1 − z/z_*) + P_{μ^κ}(z): analytic on |z| < z′/2; by the definition of μ^κ (P W-out.5's proof:
  ζ^k = z^kΣ_lbinom(k+l−1, l)(z/z_*)^l) its Taylor coefficients of order ≤ J vanish, and those of order j > J are ≤ C_J(2 + 2|κ|)^jn^{−jp}
  (|m_k| ≤ M̄_kn^{−kp}, Hc.2 (i)); so |E₂| + |E₂′| ≤ Cn^{−(J+1)p} on |z| ≤ R₁′;
- E₃ := Σ_{m>M}τ_m(z/n^p)^{q_m} = −2π cot(π/p)tail_M: ≤ Cn^{1−p(M+1)} ≤ Cn^{−(J+1)p} (M ≥ J + 1 ⇒ p(M+1) − 1 ≥ (J+1)p + p − 1), analytic on the
  discs with the same derivative bound (Cauchy), boundary values on (−R₁′, 0) bounded by the same sup.
Then Hc.3 Step 3: diagonal factors commute, so pointwise on the circle Δ_k^κ = (2f^{1/2})^{−k}P₀^∞e^{wσ₃}[ρ_BT^{σ₃}Y_kρ_BT^{−σ₃}]e^{−wσ₃}(P₀^∞)^{−1} with
w = ∓iπ tail_M − ½T = O(n^{−(J+1)p}), and P₀^∞, (P₀^∞)^{−1}, f^{−1/2}, ρ_BT^{±1} are bounded n-free on the circles (ρ_BT = ρ♮_κe^{−w}, L K.6(iv)).
(c) The same computation with h ≡ const and no lip factor: log W̃_κ − log W̃^{mod,β′} = ½λ^♭ + ζ(0, a)log(1 − z/z_*) − (π/sin(π/p))ρ₁⁻ + const,
and −(π/sin(π/p))ρ₁⁻ = −π cot(π/p)ρ₁ ∓ iπρ₁ in ℂ_±, so this is ½E₀(z) ∓ iπρ₁(z) + const with E₀ := log H_n^κ (continued; L K.1); with
log D_{e^{E₀}}² = E₀(z) + T₀(z), log(ρ♮_κ/ρ^{mod,β′}) = ∓iπρ₁(z) − ½T₀(z). |E₀| ≤ Cn^{1−p} on |z| ≤ R₁′ (L K.1: |ρ₁| ≤ Cn^{1−p}|z|^{q₁}, Hc.1 (c)
for G_δ∘ζ, |log r_n| ≤ Cn^{−p}) and |E₀′| ≤ Cn^{1−p}/η on the discs; Hc.3 Step 2 gives |T₀| ≤ Cn^{1−p}. ∎
(PROVED-mod-cite: Hc.1 (c), Hc.2, Hc.3 Steps 2–3 [REVIEWED]; L K.1, K.6; P W-out.5 [REVIEWED]. NUMERICAL: w_kappa_transfer: sup|T| decays
with exponent (J+1)p (J = 1, 2; M = J + 1) at 4 parameter sets; the lip tail with exponent p(M+1) − 1; against M(β′, α) with exponent p − 1 ([T0]);
controls: M = 0 (Hc.3 verbatim) exponent p − 1, no gauge share in μ exponent p, Hurwitz moments not re-expanded through ζ exponent 2p.)

### 4.3 The reduction

**Proposition K.11 (P W-out.6 (iii), now without BT₀).** Assume (S). Then
  n^pb_n(σ^{δ,κ})/c = 𝔅_n[M(α + 2δ, α)] + O(n^{−p}),
𝔅_n[M(β′, α)] the formal series of the decoupled model (JZC_M4 §7) at μ = 0, truncated at any order K ≥ p. In particular, for every k < p the
coefficient of n^{−k} in n^pb_n/c equals that of M(α + 2δ, α) and does not depend on κ: d₁ = −p(β′ + 1)/2, and d₂ = d₂(M(α + 2δ, α)) for p > 2.
*Proof.* By P K.8(B), J_R on ∂U_0 is I + Σ_{k≤K}Δ_k^κn^{−k} + O(n^{−K−1}), and by L K.10(c) = I + Σ_{k≤K}Δ_k^{M(β′,α)}n^{−k} + O(n^{−K−1} + n^{−p}) (the
perturbation O(n^{1−p}) multiplies n^{−k}, k ≥ 1); likewise on ∂U(4c, ε) with T₀. All other jump bounds of P K.8(B) hold. JZC_M4_proof N.6c
(with its model data Δ_k^{M(β′,α)}, meromorphic by N.6b, and jump error η_n := n^{−K−1} + n^{−p} on the circles: its proof uses only
‖E‖ = O(η_n), ‖J − I‖ = O(1/n), ‖𝒞₋‖ ≤ C and the meromorphy of the model data) gives R = I + Σ_{k≤K}R^{(k)}[M(β′,α)]n^{−k} + O(η_n), and R₁
likewise. The extraction (Paper 2 F8 via P W-out.3(d); n^{2p}b_n² = (Q₁)₁₂(Q₁)₂₁, Q₁ = P₁ + R₁, as in N.6 (i)) gives the claim with K ≥ p. ∎
(PROVED-mod-cite: P K.8(B), L K.10(c); JZC_M4_proof N.6b, N.6c [REVIEWED]; inputs from W_outer [REVIEWED]. NUMERICAL consistency:
W_outer §8 KO1–KO3: d₁ to 10⁻¹⁰ (p = 2.5, 1.5), d₂ (p = 2.5) to 5·10⁻⁸.)

**Proposition K.12 (P W-out.6 (ii)).** Assume (S), K ≥ 1, J ≥ 1, M = J + 1. Then (PROVED-mod-cite)
  n^pb_n(σ^{δ,κ})/c = 𝔅_n^{rec}[BT_coh(α + 2δ, α; μ^κ_n, (2a_m)_{m≤M})] + O(n^{−K−1} + n^{−1−(J+1)p}),
and, by Prop K.12′ below, Conjecture W holds for σ^{δ,κ} at first order in the poles, in the following two precise forms (review A §3)
(fixed per Rule R review A of the W chain, B3):
- *(refined form; first order in the poles, all orders of their dressing)*
  n^pb_n/c = 𝔅_n[M(α + 2δ, α); t] + Σ_m(the continued symbolic-j layer at j = q_m with μ = −τ_mn^{−pq_m}) + O(n^{−2p}),  t_j = −2Z_κ(−j)/j + B_j,
  the m-th layer having leading term pR_{q_m}W(q_m)π cot(πq_m)(n/N)^pN^{−1−pq_m}; the remainder O(n^{−2p}) is the second order in the
  branched data;
- *(W's displayed form; pole term at leading order only)*
  n^pb_n/c = 𝔅_n[M(α + 2δ, α); t] + pR_{q₁}W(q₁)π cot(πq₁)(n/N)^pN^{−1−pq₁}(1 + O(N^{−1})) + O(n^{−1−p}):
  the only pole term is m = 1, at n^{−p}; apart from that pole term, every integer-power coefficient n^{−k} with k < 1 + p is that of M(α + 2δ, α), κ-free (for integer p the pole term sits on the n^{−p} coefficient); the first Toda layer
  (t₁ at n^{−1−p}) needs the refined form.
*Proof.* As P K.11 with L K.10(b) in place of (c) and the BT_coh data (meromorphic by L K.9) as N.6c's model data; jump error
n^{−K−1} + n^{−1−(J+1)p}. Then Prop K.12′ (in its refined form) with τ_m = π cot(πq_m)·2a_m = −2π cot(πq_m)R_{q_m}/q_m (P W-out.5(iii),
P W-out.7) gives the pole terms. ∎ (by Prop K.12′; fixed per Rule R review A of the W chain, B3)

Relative to JZC_W_outer P W-out.6: its "companion" hypothesis (the transfer G1u/Hc.3 to the composite band factor) is now L K.10 + P K.8
(PROVED-mod-cite); (iii) needs no hypothesis; (ii) needed exactly BT_coh, which Prop K.12′ supplies. BT_coh is a statement about a model
problem whose circle data are meromorphic (L K.9): N.6c's residue recursion is available for it; what it asks is the first-order value of
that recursion in the branched data, i.e. the "E3.7 for branched tilts" computation (JZC_W §5.1 item 4) restricted to coherent tilts.

**Proposition K.12′ (BT_coh at the order P K.12 needs)** (fixed per Rule R review A of the W chain, R1; text of review A §2, verbatim).
For coherent data (β, ν; μ_n, (σ_ρ)_{ρ∈𝓡}) with μ_{n,j} = O(n^{−jp}) and bounded σ_ρ,
  𝔅_n^{rec}[BT_coh] = 𝔅_n[M(β, ν); μ_n] − Σ_{ρ∈𝓡}(pρW(ρ)/2)τ_ρ n^{−1−pρ} + O(n^{−2−p·min𝓡}),
and more precisely the first-order part in (τ_ρ) is Σ_ρ (engine symbolic-j layer at j = ρ) with μ = −τ_ρn^{−pρ}, to all orders in 1/n.
The remainder of that refined form is O(n^{−2−2p·min𝓡}), the second-order part.

*Proof.*
(a) **Gauge form.** By coherence and JZC_W_exact WE.1(iii), ρ_BT = ρ_a := ρ_mod·exp(−½Σ_ρμ_ρRA_ρ)·(Toda gauge), with μ_ρ := −τ_ρn^{−pρ}.
  This is JZC_W_BT BT.1 with the mismatch exponent μ tan πρ + πσ = 0 (Prop BT.5). Hence Δ_k^{BT} = G_aΔ_k^{mod}G_a^{−1}, with G_a
  the E3 gauge of the tilt function M = Σ_jμ_jQ_j + Σ_ρμ_ρM_ρ. G_a is exactly E3's G, since P₀^∞e^{hσ₃}(P₀^∞)^{−1} = cosh h + (sinh h/R)·RN
  with N² = I and RN = T[[0, z−4c], [z, 0]]T^{−1}. Its Taylor data at 0 (A_ρ) and at 4c (M_ρ) are the engine's symbolic-j data at j = ρ (WE.1(i)–(ii)).
(b) **Entire dependence.** By N.6b (REVIEWED), every Laurent coefficient of Δ_k^{BT} is entire in the times (μ_j, μ_ρ) with n-free
  coefficients. So each order n^{−k} of 𝔅^{rec} is entire in the times. Its value at μ_ρ = 0 is 𝔅_n[M(β, ν); μ_n] (Theorem N.6).
(c) **The n⁻¹ order.** By the decoupled E3.7 identity (m3a_e37_decoupled route 1, REVIEWED: e(M) − e(0) = cp·M(4c) identically in
  M(0), M(4c), M′(4c)), the n⁻¹ coefficient is exactly linear in the times, with no products. Its ρ-part is
  cp·μ_ρM_ρ(4c) = (pρW(ρ)/2)μ_ρ (WE.1(i) at m = 0, with c-scaling; W(ρ) = c^ρC(2ρ, ρ), JZC_W §1).
(d) **Orders n^{−k}, k ≥ 2.** By (b) these are O(|μ_ρ|) = O(n^{−p·min𝓡}) for the first-order part, and O(|μ_ρ|²) beyond.
(e) Finally (n/N)^pN^{−1−pρ} = n^{−1−pρ}(1 + O(1/n)). ∎

**Consequently** Hypothesis BT_coh holds with η = 1. P K.12 (ii) is PROVED-mod-cite, with inputs: L K.10, P K.8, and the
W_outer inputs; BT.1(iii), BT.5; WE.1; m3a_e37_decoupled, N.6b, N.6c (REVIEWED). After review A, all of these are REVIEWED except
JZC_W_exact WE.1 (NOT REVIEWED; elementary).
*Checks (review A §2, not repo scripts):* (a) the algebra of BT.5 and ρ_BT = ρ_a by hand; WE.1(ii) at the κ-family's exponents by an
independent quadrature (we1.py; ρ ∈ {⅓, 4/3, 0.7}, four points incl. both sides of the negative axis: deviation ≤ 6·10⁻¹⁸, the quadrature
floor at dps 30; control "no branched term" misses by 0.9–3.3; ρ = 4/3 = q₂ at p = 3/2 tests the continuation beyond ρ < 1); (c) WE.2 route 2
confirms the first order (response pj/2 per unit μC(2j, j), symbolic j, zero at orders 2 and 3), and w_bt_poles7 asserts g1[1] = pj/2 at
p = 3, 3/2. *Caveats:* WE.1 is NOT REVIEWED; 𝔅^{rec} is the finite recursion at fixed K (as in P K.12's definition), and the n^{−k}
coefficients are uniform in n because, in the n^p frame, the model data are n-free and only the times depend on n.
*p = 2.* All q_m are half-integers, so τ_m = 0 and the data are pure lip factors exp(C(−z/n^p)^q). (a) holds in the limiting form, because
(−z)^{½} = −R/(4−z)^{½} is of engine form (JZC_W_BT Prop BT.5, fix B7). W's pole terms vanish (cot = 0); the W′ term, n^{−3−p/2} = n^{−4}, lies
inside the coarse remainder O(n^{−2−p/2}) = O(n^{−3}), and in the refined form it is part of the continued first-order layer (JZC_W_exact:
exact limit).

## 5. 1 < p < 2 (Proposition K.13)

**Proposition K.13.** Let 1 < p < 2, (S).
(a) H_n^κ does **not** satisfy (O3) with ν_p = ½: its gauge part −2π cot(π/p)ρ₁(z) has |·| ≍ (2π|cot(π/p)||κ|/p)n^{1−p}|z|^{q₁} with q₁ = 1 − 1/p < ½
  (L K.1; cot(π/p) ≠ 0 for 1 < p < 2). It satisfies (O3) with ν = q₁ and n-free constants (the bounds in L K.4's proof).
(b) Paper 2 uses the exponent of (O3) only in Lemma szego (vi)(a) (|ω|^{±1} ≤ C on Z(¼η_*), hence F1) and in Lemma lip-mismatch / ε′_n / 𝔪_n (§7);
  App C, App B and §8 do not use it (grep of papers/paper2: (O3) appears in sec_7 only at l. 337; F2 is not invoked in §7, App B, App C,
  §8). G12, Hc, G1u use it only through G1u L1 (iv) (boundedness of ρ) and L3 (the lip mismatch). The exponent of (O3) is used only in
  these places; (O3) is also used at Paper 2 sec_6 l. 182 ("by (O3)–(O4), log H° is bounded on (0, 4c)") and l. 283 (the polynomial bound
  for log W₀ on 𝒵_n), for boundedness only, which H_n^κ satisfies (|ρ₁| ≤ Cn^{1−p} on [0, 4c]) (fixed per Rule R review A of the W chain, B5).
(c) In the κ-problem every one of these uses concerns the lip coefficient ω_κ = e^{±2πi(δ+ρ₁)}ω^{(β′)} = ϱ_±ρ^{♭−2}X², and by L K.4 and L K.6 (iv)–(v)
  it holds with Paper 2's exponent: |ω_κ|^{±1} ≤ C, |ω_κ − ϱ_±| ≤ C|z|^{ν_p}log(2/|z|), C n-free; and the a-priori bound needs only |X|^{±1} ≤ C.
Hence Paper 2's frame tolerates the q₁ < ½ band factor, P K.5–K.12 hold for all p > 1, and no restriction of the statement is needed.
*Proof.* (a) L K.1 and |ρ₁(z)| = (|κ|/p)n^{1−p}|z|^{q₁}(1 + O(|z|n^{−p})). (b) Reading of the cited files (Paper 2 sec_6 Lemma szego (vi)(a): "The third is
bounded by (ii) with q = H°_n, 𝔠₀ = 0, ν = ν_p and 𝔐 = C from (O3)–(O4)"; sec_7 l. 74–77, 310–355, 460–487). (c) L K.6, L K.4. Also directly: had one
used Lemma szego (ii) with ν = q₁ for the band factor and ignored the lip phase, the mismatch would be n^{1−p}|z|^{q₁} and ε′_n would contain
n^{−(p+2)(p−1)/p}, still → 0; the cancellation of L K.4 removes this term (control in [NU]). ∎
(PROVED-mod-cite + NUMERICAL: w_kappa_gauge [NU]: the band factor's gauge part has local exponent q₁ (0.2 at p = 1.25, ⅓ at p = 1.5), the
lip-level factor X has ½; the localised gauge lip mismatch sup_r|X² − 1|e^{−nr^{1/2}} decays like n^{−p}, and the q₁-based rate
n^{−(p+2)(p−1)/p} is excluded.)
*Correction to JZC_W_outer §4 (last paragraph) and §10 item 3:* "for 1 < p < 2 it holds with ν_p replaced by q₁ < ν_p (GAP …); G1u L3's lip
mismatch bound |z|^{ν_p}log(2/|z|) likewise holds for p ≥ 2 only" — the first half is right for H_n^κ alone; the second is not: with the lip
phase included the bound holds for every p > 1 (L K.6(v)).

## 6. p < 1 (Proposition K.14): the obstruction, and a fix

### 6.1 The forced density

Within Paper 2's frame with the lattice g, a normalising gauge G (analytic, zero-free off ℝ near (0, ∞)) must give F♮ := F_κG the jump e^{2iθ} on
(4c, ∞)∖{nodes} ((O1)), i.e. G₊/G₋ = e^{2πi(t − t_κ + δ)} there; and the band weight W₀ = W_κ/(F̃♮₊F̃♮₋) and the lip entries, which contain
(W_κ/F̃♮²)^{−1} in ℂ_±, must continue analytically from the band into 𝒵_n (lips) and into U(4c, 2ε) (F2: "H_n and r_n are analytic on 𝒵_n, which
contains … a neighbourhood of (0, 4c + ε]"; Lemma szego (vi)(b)). Write j(x) := log G₊ − log G₋ − 2πiδ on (0, ∞).
**(G)** j is real-analytic on (0, 4c + ε) (equivalently: log G₊ and log G₋ both continue analytically across the band, which the lip entries in ℂ₊ and
in ℂ₋ require, since W_κ/F̃♮² in ℂ_± is W₀e^{∓j}).

**Proposition K.14.** Let 0 < p < 1, κ ≠ 0, and let G satisfy (O1) and (G).
(a) *(forced density)* j = 2πi(ρ₁ + k) on (0, 4c + ε) for one k ∈ ℤ, ρ₁ = t − t_κ; the lip (2,1) entries carry e^{±2πiρ₁(z)}, and the band factor contains
  e^{−2π cot(π/p)ρ₁} (for the gauge exp 𝒞[ρ₁]; L K.1 holds numerically for ½ < p < 1, [P1g]).
(b) *(size)* ρ₁(y) = (κ/p)n^{1−p}y^{q₁}(1 + O(y/n^p)), q₁ = 1 − 1/p < 0: ρ₁ is unbounded at 0+; at the Bessel scale |z| ≍ n^{−2},
  |ρ₁| ≍ (|κ|/p)n^{e(p)}, **e(p) := (1 − p)(2 + p)/p > 0**; at the soft edge ρ₁(4c) ∼ (κ/p)(4c)^{q₁}n^{1−p} → ∞; for p ≤ ½, ρ₁ ∉ L¹(0, 1).
(c) *(consequences)* (i) on the lips arg z = ±ϑ (0 < ϑ < π), log|e^{±2πiρ₁(re^{±iϑ})}| = 2π(κ/p)n^{1−p}r^{q₁}sin(|q₁|ϑ)(1 + o(1)) → +∞ (κ > 0) or
  −∞ (κ < 0) as r → 0, on both lips: for κ > 0 F1 (|v^{±1}| ≤ C) fails at fixed n; for κ < 0 the lip entries vanish faster than any power while
  ϱ_± ≠ 0, so |ω_κ − ϱ_±| → 1 at 0 and Lemma lip-mismatch fails; in both cases ω_κ is not close to ϱ_± anywhere on the Bessel scale
  (|ρ₁| ≫ 1 there, by (b)), so neither the Bessel parametrix of order α nor of any fixed order matches the lips; (ii) if cot(π/p) ≠ 0,
  log H_n^κ is unbounded at 0+ (H_n(0⁺) does not exist: (O2) fails) and varies by ≍ n^{1−p} across U(4c, ε) (the n-free 𝔐 of Lemma szego (vi)(b)
  fails); if cot(π/p) = 0 (p = 2/(2k + 1), e.g. ⅔), (ii) does not occur but (i) does; (iii) for p ≤ ½, 𝒞[ρ₁] does not exist as a Cauchy
  integral, and E_κ must be defined by L K.1's closed form, which is unbounded at 0 ((O5) at 0 fails for F♮).
*Proof.* (a) ρ₁ + k is real-analytic on (0, z′) (an analytic function of y); j and 2πi(ρ₁ + k) agree on (4c, 4c + ε) by (O1) (k fixed by continuity
between nodes, the nodes being isolated); identity theorem on the interval (0, 4c + ε). The lip factor: W_κ/F̃♮² = W₀e^{∓(j+2πiδ)} in ℂ_±
(L W-out.4's computation with E replaced by G(−z)^δ). Any factor A analytic across (0, ∞) multiplying G changes W₀ by A₊A₋ = A² and not the lip
factor. (b) Expansion of n z^{−1/p}(1 − (1 − κz/n^p)^{1/p}); at |z| = n^{−2}: n^{1−p}·n^{−2q₁} = n^{(2 − p − p²)/p}; ∫_0 y^{q₁}dy = ∞ iff q₁ ≤ −1 iff
p ≤ ½. (c)(i) Im((re^{iϑ})^{q₁}) = r^{q₁}sin(q₁ϑ) < 0 in ℂ₊ (q₁ < 0), and |e^{2πiρ₁}| = e^{−2π Im ρ₁}; mirror in ℂ₋ with e^{−2πiρ₁}. (ii) L K.1's band form
(its algebra holds for any p with 1/p ∉ ℤ once the identity holds) and (b). (iii) (b) and [P1g]. ∎
(PROVED (elementary) given (G); the conclusion "the lattice-g route fails for p < 1" is an **OBSTRUCTION (for this route)**: it shows that no
gauge compatible with Paper 2's frame (O1), (G), F1, (O2)–(O3) exists for the lattice g. NUMERICAL: w_kappa_plt1 [P1a]–[P1g].)

The exponent e(p) unifies both regimes: for p > 1, e(p) = −(p − 1)(p + 2)/p < 0, and n^{e(p)} is exactly the size of the lip phase on the
Bessel scale that L K.4 controls (and that the naive q₁ count would have put into ε′_n, §5); for p < 1 it is a positive power of n.
The case p = 1/m (Z(0) = −½ − δ + (−κ)^m, L W-out.0(b)) is excluded above (1/p ∈ ℕ): then t_κ = (n^p/z − κ)^m is a polynomial in 1/z and
ρ₁ = t − t_κ contains the constant −(−κ)^m, a constant lip phase that shifts the hard-edge exponent (W_outer §7, first bullet); not treated here.

### 6.2 What a fix must do

The index offset must be removed from the phase that the frame matches on the saturated region, not carried by a gauge: replace the lattice
g by g_κ with **g_κ₊ − g_κ₋ = 2iθ_κ/n on the saturated region**, θ_κ := πt_κ (κ-node phase), i.e. the constrained equilibrium problem whose upper
constraint is the κ-node density (1/n)|t_κ′(y)|dy instead of the lattice's (1/n)|t′(y)|dy (JZC_W §5.1 item 3; JZC_M1 Theorem Q is the template).

### 6.3 Sketch (PROOF SKETCH, not a proof; HEURISTIC where marked)

1. *Scalar.* With g_κ, F_κ(−z)^{−δ} already has the jump e^{2πi(t_κ−δ)}·e^{2πiδ} = e^{2πit_κ} = e^{2iθ_κ} on (4c, z_*) (L W-out.3(a)), so on
   (0, z_*) no gauge is needed; only the region beyond z_* (κ > 0: density t − δ − ½ on (z_*, ∞), bounded; κ < 0: ρ̃ on (−∞, −z′), bounded) needs
   the gauge of P W-out.3 restricted to that region, which is analytic near the band and bounded at 0. So (O5) at 0, F1, (O2)–(O3) hold with
   the Hurwitz∘ζ data (for p < 1, the seam construction G3/Hc.5 composed with ζ, which maps the non-node rays to circular arcs through 0 and
   −z_*; W_outer §7, GAP-minor).
2. *Equilibrium.* The constraint changes by the relative amount (1/n)|t_κ′|/((1/n)|t′|) − 1 = O(y/n^p) on the saturated region; the band is
   unconstrained, so the hard-edge density stays ∝ x^{−1/2} and the Bessel model of order α survives. Then g_κ = g + O(n^{−p}) (relative), with
   an endpoint 4c_n = 4c(1 + O(n^{−p})), and n(g_κ − g) = O(n^{1−p}) — unbounded for p < 1, so g_κ cannot be treated as a perturbation of g; the
   sign conditions (Lemma signs, Lemma lips) must be proved for g_κ directly (open: JZC_W §5.1 item 3). On the Bessel scale the effect is
   nφ_κ − nφ = O(n^{1−p}|z|^{1/2}) = O(n^{−p}) — small, in contrast to the gauge's n^{e(p)}.
3. *Where the poles go (HEURISTIC).* For p < 1 the poles q_m = m − 1/p < 0 (m < 1/p) give W's terms at N^{−1−pq_m} = N^{−pm}, i.e. before n^{−1}.
   In this route they must come from the expansion of the endpoint/equilibrium in n^{−p} (g_κ's moments), as SPEC Prop E / JZC_M1 Prop M1.2
   describe for the n-dependent equilibrium. Consistency with W's π cot(πq) form is not checked here.
4. *What would be proved.* Theorem H's α-frame with g_κ and the Hurwitz∘ζ seam scalar: β′ = α + 2δ unchanged (Z(0) = −½ − δ for 1/p ∉ ℕ),
   so W's Szegő shift would again be κ-free; the κ-dependence would sit in c_n and in the n-dependent equilibrium moments.

## 7. Checks (Rule N: NUMERICAL; finite samples of universally quantified statements; nothing fitted)

- **`w_kappa_gauge.py/.out`** (mpmath dps 30; c = c(p)). [CF] L K.1 at (p, δ, κ) ∈ {(1.5, −0.3, ±0.5/−0.3), (3, −0.7, 1), (3, −0.7, −0.02),
  (1.25, −0.5, 2), (2, −0.5, 0.7)}: spread ≤ 5·10⁻²⁴; controls (π cot in place of π/sin; log term dropped where ζ(0, a) ≠ 0) fail by 0.1–11.
  [PSI] the band identity for Ψ₀ (tolerance 10⁻⁹ from the 10⁻¹² offset of the boundary values). [COH] coherence (Cor K.1′), control
  non-coherent. [X] L K.4 at n = 4, 16, 64: X₊X₋ = 1, A_X continuous across the band and (−δ_r, 0), |log X| ≤ C n^{1−p}|z|^{1/2} with C n-free;
  control rate n^{−p}. [NU] P K.13. **ALL 94 CHECKS PASSED** (24 of them controls that must fail and do; runtime ≈ 23 min on 2 shared cores).
  Key numbers: |log X|/(n^{1−p}|z|^{1/2}) ≤ 0.75 (p = 1.5), 0.60 (p = 1.25), 1.76 (p = 3), 1.10 (p = 2), flat in n = 4, 16, 64, while |log X|n^p grows
  ×17 (control); X₊X₋ − 1 and the jump of A_X ≤ 2·10⁻¹⁸; local exponents on the lip (10⁻⁶ → 10⁻⁸): band factor 0.2000, 0.33333, 0.6667 (= q₁),
  lip-entry factor X 0.5 at p = 1.25, 1.5, 3; S(n) decay exponent 1.2483 (p = 1.25) and 1.4975 (p = 1.5) vs p (q₁-based 0.65, 1.17 excluded).
- **`w_kappa_transfer.py/.out`** (dps 24; G_δ by (E.2.1)_δ, m_k(δ) by the Fourier sums; Gauss–Chebyshev N = 48 vs 16). L K.10 at
  (p, δ, κ) ∈ {(1.5, −0.3, 0.5), (1.5, −0.3, −0.3), (3, −0.7, 1), (1.25, −0.5, 0.4)}, n = 8, 16, 32: **ALL 43 CHECKS PASSED** (11 controls).
  Exponents of sup|T| (n = 16 → 32), targets (J + 1)p: J = 1: 3.058, 2.975, 5.985, 2.769 (targets 3, 3, 6, 2.5); J = 2: 4.553, 4.486, 8.986, 3.895
  (4.5, 4.5, 9, 3.75); lip tail (M = 2, 3): 3.5/5.0, 3.5/5.0, 8.0/11.0, 2.751/4.001 (= p(M+1) − 1); [T0] against M(β′, α): 0.5006, 0.4996, 2.0,
  0.2504 (= p − 1); controls: no gauge share in μ 1.52, 1.49, 3.0 (≈ p; degenerate at δ = −½, not asserted); Hurwitz moments not re-expanded
  2.95, 2.97, 6.02, 2.48 (≈ 2p). Quadrature N = 16 vs 48 relative ≤ 2.5·10⁻⁷. Runtime ≈ 15 min.
- **`w_kappa_apriori.py/.out`** (dps 30, n = 4). [SB] L K.2 at 6 (p, s, δ, κ) incl. κ = 2 > a^p and α > 0; [AR] L K.3 arcs. **ALL 36 CHECKS
  PASSED** (13 controls; run 2, see Rule A item 13; ≈ 54 min under load). max |U_{j2}|/I₁^κ ≤ 0.122; exponents of |U_{j2}(iy)|: −0.5052, −0.5034,
  −0.5044, −0.5026, −0.0148, −0.0115 (p = 3/2, |z| 10⁻⁴ → 10⁻⁶; targets −½, −½, 0) and −0.50026, −0.50013, −0.50024, −0.50011, −0.0004, −0.0002
  (p = 3, 10⁻⁶ → 10⁻⁸); the shifted exponent α + 2δ (−1.5, −0.2, −2.3, −0.5) is excluded in every case. Arcs: min over the t_κ-arcs = 1.0 ≥ 0.842
  (Paper 2's constant) in all 5 cases; lattice-t arcs at κ = 60: 0.40 (control fails as required).
- **`w_kappa_plt1.py/.out`** (dps 30). [P1a]–[P1g] of P K.14: **ALL 27 CHECKS PASSED** (1 control: "unbounded" at p = 1.5 fails). Key
  numbers: ρ₁(10⁻¹²) = 8.7·10⁷ (p = 0.6), −5.7·10³ (p = 0.75), 10⁻⁵ (p = 1.5); Bessel-scale exponents 1.73333, 0.916667, −1.16667, −3.33333
  = e(p); log|lip factor| at r = 10⁻¹² = ±1.69·10⁸ on both lips (κ = ±0.3, p = 0.6); band gauge part 3.2·10⁸ at x = 10⁻¹² (p = 0.6), 10⁻²⁴
  (p = ⅔, cot = 0); ρ₁(4c) = 87.6 at n = 10⁶ (p = 0.6); ∫_ε^1ρ₁ grows like ε^{−0.501} (p = 0.4); L K.1 at p = 0.75 to 6·10⁻²⁵, Re 𝒞[ρ₁] = ±949 at
  r = 10⁻⁸.

## 8. Rule A (adversarial pass) — log

1. *The exponent of the gauge at the lip level (the main correction made during this work).* The first draft of L K.4 claimed
   |log X| ≤ Cn^{1−p}|z|^{min(q₁,½)}log(2/|z|) (sharp) and log X ≈ ∓iπρ₁ on the lips — i.e. it accepted W_outer §4's claim that the gauge has
   exponent q₁ < ½ for 1 < p < 2 at the level of ω. The first run of w_kappa_gauge (aborted, nothing kept) gave local exponent 0.5000 at
   p = 1.25 and relative deviation ≈ 3 from ∓iπρ₁. Investigation (scratch test: log X/𝓡 converges as z → 0, n^{p−1}A_X(0) → const) led to the
   𝓡-factorisation proof of L K.4(ii). The upper bound with min(q₁, ½) was true but not sharp, and the "≈ ∓iπρ₁" statement was false. The
   assertions were rewritten to test L K.4 as now stated, with the q₁ exponent as a control that must fail. This changes §5's answer from
   "tolerated with a worse ε′_n" to "tolerated with Paper 2's ε′_n".
2. *Counterexample hunt for L K.1.* Large κ (κ = 2 > a^p at p = 1.25, |z| up to 0.6z′), κ < 0 (the (−∞, −z′) density), p = 2 (cot = 0), points next
   to the negative axis and both sides of the band. No failure. The identity also holds at p = 0.75 (outside its proof's hypotheses; recorded as
   numerical only).
3. *Degenerate controls.* At δ = −½, ζ(0, a) = 0: "drop the log term" ([CF]) and "no gauge share in μ" ([C2] of w_kappa_transfer) are then no
   controls. The first was caught before its run completed; the second made the first full run of w_kappa_transfer report 1 of 40 checks
   failed (the control did not fail, at p = 1.25, δ = −0.5: exponent 2.769 = the J1 value, since the share vanishes). Both are now asserted only
   where ζ(0, a) ≠ 0; the run was repeated (43 checks, adding [T0]).
4. *Tolerance of [PSI].* The first version asserted 10⁻¹⁸ for PV𝒞 computed from boundary values at x ± 10⁻¹²i; the offset alone produces
   O(10⁻¹²) errors. The tolerance 10⁻⁹ is derived from the offset (|𝒞′| ≤ 10² there), not from the observed values (≤ 9·10⁻¹³).
5. *Is the transfer to BT_coh exact or only to first order?* Exact in the sense of L K.10(a): ρ♮_κ/ρ_BT = e^{∓iπ tail_M − T/2} pointwise; the only
   approximation is the size of tail_M and T. Products of tilts ("higher order" in P W-out.6(i)) are not separate data: the BT_coh model has the
   full exponential band factor, so they are inside 𝔅^{rec}[BT_coh].
6. *Non-coherent BT.* W_outer's BT was stated with independent σ. Tested: the non-coherent W̃ jumps across (−δ_r, 0) by ≥ 1.04n^{1−p}|y|^{q₁} ([COH]
   control). So a proof of BT for independent σ would need more than N.6c; BT_coh is what the κ-family needs. This is for the lip-matched
   parametrix; JZC_W_BT Lemma BT.1 gives a meromorphic alternative with an explicit lip term (Theorem BT) (fixed per Rule R review A of the W
   chain, B6).
7. *P K.11 vs W_outer's "(iii) CONDITIONAL on BT₀".* W_outer conjugated by the gauge and observed non-meromorphic branched terms in the circle
   data; here the branched terms are compared, as a perturbation of size O(n^{1−p}) on the circles, with the meromorphic model M(β′, α), and
   N.6c needs meromorphy only of the model data. Checked: N.6c's induction uses the jump error once ("The jump error E … appears once"), so
   E = O(n^{−p}) on the circles gives O(n^{−p}) in R. The W_outer data (d₁ to 10⁻¹⁰, d₂ to 5·10⁻⁸ at p = 2.5; d₁ at p = 1.5) are consistent; the
   n^{−p} term itself is not determined by P K.11 (it is BT_coh's content).
8. *Branches at the circle point −δ_r.* E, tail_M and ρ₁ have cuts on (−∞, 0); only sup bounds are used there (Hc.3 Step 2), with boundary
   values from both sides. ρ_BT and ρ♮_κ are analytic across (−δ_r, 0) (mod super-small), so the identity of L K.10(a) holds from each side.
9. *n-uniformity of the radii.* r_*, δ_r, ε, R₁′ are n-free; z′ = n^p/|κ| ≥ 8(4c + 2) for n ≥ n₀, so all expansions in z/z_* are geometric with
   n-free ratios. The sector Z(η_*) ⊂ {|z| < z′/2}. Constants depend on κ through |κ| and (for K.3) through T₀(p, κ).
10. *Lens arcs.* The lattice choice of arc radii fails for large κ at fixed n (control [AR], κ = 60): the arcs must be chosen in t_κ (L K.3).
11. *p < 1, (G).* Could a non-analytic gauge density on the band avoid (a)? Then W₀ or the lip entries are non-analytic at a band point and the
    lens cannot be opened there (F2 requires analyticity on a neighbourhood of (0, 4c + ε]); and a density on (−∞, 0) does not change the lip
    factor (it is a factor analytic across (0, ∞), absorbed in W₀). So within the frame (G) is forced; the obstruction is for this route only.
12. *Rule X.* The checks compare closed forms with independent quadrature (CF, X, T) or exact sums (SB); nothing is fitted. ζ(−kp, a) is not used
    (Fourier sums, as in Hc), except implicitly in W_outer's e2e predictions cited in P K.11.
13. *Rule N, w_kappa_apriori.* Run 1 measured the exponent of |U_{j2}| at p = 3/2 only between |z| = 10⁻² and 10⁻⁴ and found −0.552, −0.534,
    −0.544, −0.526 (α = −½) and −0.10, −0.08 (α = 0.4, target 0), outside the declared tolerance 0.02 (pre-asymptotic corrections of relative size
    |z|^{min(|α|,½)}); it also contained an inadmissible κ = −0.05 < −a^p at δ = −0.9 (λ₁ < 0; the run crashed there). Run 2 adds |z| = 10⁻⁶ at
    p = 3/2 with the same tolerance and uses κ = −0.0005. U_{j2} was cross-validated with two (M₀, R) choices (all 30 digits agree). The bound
    |U_{j2}| ≤ I₁^κ held in run 1 for all four completed cases (max ratio 0.12).

## 9. What remains

(Updated after Rule R review A of the W chain: items 1, 2 and 5 of the former list are done — BT_coh by Prop K.12′ (R1), Rule R for this
note and its W_outer inputs by review A, the W_outer corrections applied there (B4).)
1. **Second order in the poles**: products of branched terms (the O(n^{−2p}) remainder of P K.12's refined form); not treated.
2. **JZC_W_exact Lemma WE.1**: Rule R (it is the one NOT REVIEWED input of Prop K.12′; elementary, numerically spot-checked by review A);
   optionally a reviewer B for the assembled chain incl. Prop K.12′ (review A's suggestion). Rule L before any novelty claim (UNCHECKED).
3. p < 1: the n-dependent equilibrium g_κ (§6.2–6.3), including its sign conditions (OBSTRUCTION for the lattice-g route, P K.14); the case
   p = 1/m (κ-dependent Z(0)).
4. α ∉ (−1, 1) (s ∉ (1, 1 + 2p)): not covered (as in G12/G1u).
5. Non-coherent branched tilts (e.g. a genuine x^ρ mass tilt, σ = 0, τ ≠ 0): (F-br) for a general branched band factor stays a GAP
   (JZC_W_BT §3.3); irrelevant to the κ-family (review A, F2).
