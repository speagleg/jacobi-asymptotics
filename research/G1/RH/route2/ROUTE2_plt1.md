# ROUTE2_plt1: Route II for 0 < p < 1 — the pointwise Law P for k^{−s}Ψ, Ψ slowly varying, via the seam geometry of RH_plt1b, and a Christoffel step that removes the restriction s < 1 + 2p (Plan 51)

Status: **Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan51.md), fixes F1–F8 applied — REVIEWED.** Novelty: UNCHECKED (no Rule L
search). Lemma CT-Ch (Cholesky/Darboux form; renamed from "Lemma CT" per Rule R F1, since Plan 52's §3.21 has a different "Lemma CT")
is a classical Christoffel (Darboux) transformation at the endpoint 0, equivalent to Plan 52's Lemmas CS/CS-r (§5.1); not claimed as new.

*(Plan 55 note, 2026-10-15: Theorem RII_{<1} and the rate clauses of its corollaries hold with (H_an^{<1}) (strip π/2) weakened to (A_ϑ) for any ϑ > 0: the lips may leave 0 at any small ϑ_lip and the weight is then needed only in |arg z| < ϑ_w ≤ pϑ (< πp/2, inside S_in; the seams are unchanged); verified on Paper 2's consolidated write-up (papers/paper2), see ../../PROOF.md §3.24 (Theorem AS, PROVED-mod-cite, proof of record papers/paper2 rev. 3 + §3.24 audit; Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan55.md), fixes applied — REVIEWED). This file is unchanged and proves its results as stated.)*

Source: `research/program/outline_B_sv.md` §5 Route II, work package WP5b (p < 1, seams). Base: `ROUTE2.md` (Plan 48, REVIEWED;
review `../../review/REVIEW_Plan48.md`), `../plt1/RH_plt1b.md` (seam construction, REVIEWED), `../plt1/RH_plt1.md` (amendments
table), `../zeta/RH_zeta_close.md` §1 (Conway–Deift comparison, REVIEWED). Numerics: `checks/check_r2p_{coeff,lw1}.py/.out`.

**Labels (per step).**

| Item | Statement (short) | Label |
|---|---|---|
| §1 strip | for 0 < p < 1 the weight is evaluated only in S_in = {\|arg z\| < πp/2}, so the strip \|Im u\| ≤ π/2 suffices; π/p is **not** needed; RedA's L₁ satisfies the hypothesis in every strip | PROVED (bookkeeping on RH_plt1b §2) |
| §2 change table | RH_plt1b ↔ ROUTE2 §2: what changes for w₁ = k^{−s}Ψ₁ | PROVED (bookkeeping), changed steps proved in §3–§4 |
| §2 seams | Ψ₁ does not enter the seam scalar F (L±, X are node data); V and Q have no seam jump; with W̃ := D_w the comparison parametrix has none either | PROVED |
| §3.2 Lemma X0 | N-uniform bound \|X(z) − X(0)\| ≤ C\|z\|(1 + log(1/\|z\|)), \|X′(z)\| ≤ C(1 + log(1/\|z\|)) off the seams | PROVED-mod-cite (DLMF 5.5.1, 5.11.1 + §5.11(ii); RH_plt1b Lemma S) |
| §3.3 LW1′_{<1} | \|D_w²/w₀ − c_±\| ≤ C(\|z\|^{1/2}log(2/\|z\|) + ε₁(T_N)) on the lips at ±πp/4 | PROVED (given X0, RH_plt1b, ROUTE2 §3.3) |
| §4.1 UR′_{<1} (incl. (b′)) | uniform resolvent for the comparison problem, \|α_x\| < 1, star of three arcs at angles 0, ±πp/4 | PROVED-mod-cite (as UR′; KMVV angle freedom) |
| §4.2 C′_{<1}, D′_{<1} | ‖(1 − C_v)^{−1}‖ ≤ 2C; Q₁ − Q̃₁, Q₂ − Q̃₂ = O(ε′_N/N), ε′_N = N^{−1}log N + ε₁(T_N) | PROVED-mod-cite |
| **Theorem RII_{<1}** | 0 < p < 1, 1 < s < 1 + 2p, (H_an^{<1}): n^pb_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n) | **PROVED-mod-cite** (WLXZ v1 §§3–5, §6.1; KMVV §6 incl. angle freedom; C–D Thm 4.4 + arguments of 4.7/4.9 via RH_ζ_close §1; DLMF 1.13.4, 1.14.38–40, 5.5.1, 5.5.3, 5.11.1, 5.12, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2; G2 μ*, B*(i)–(ii)); Rule R ACCEPT WITH FIXES — REVIEWED |
| **Lemma CT-Ch** | σ on [0, ∞), infinite support, J = LLᵀ (Cholesky) ⇒ LᵀL is the Jacobi matrix of xσ; if a_n/b_n → 2 and b_{n−1}/b_n → 1 then the same holds for xσ, with b̃_n/b_n → 1; with O(1/n) inputs, O(1/n) outputs | PROVED (self-contained, classical; novelty not claimed; equivalent to Plan 52 CS/CS-r with g_j = l_j², h_j = m_{j−1}²; independent second proof) |
| **Corollary RII⁺_{<1}** | as RII_{<1} for **every s > 1** | PROVED-mod-cite (RII_{<1} + CT-Ch); Rule R ACCEPT WITH FIXES — REVIEWED |
| **Corollary B_{p<1}** | 0 < p < 1, **every s > 1**, Ψ sequence-form slowly varying (incl. D(γ) = ∞): n^pb_n → c(p), n^pa_n → 2c(p), rate O(1/n + ρ(n/M₀)) | PROVED-mod-cite (RedA + RII⁺_{<1}); Rule R ACCEPT WITH FIXES — REVIEWED |
| Remark CT-px | cross-reference: Lemma CT-Ch applied to Plan 48's RII gives an independent **second proof** of Plan 52's Corollary B_all (p > 1, every s > 1; PROOF.md §3.21, REVIEWED) | no new label (cross-reference) |
| GAP-rate | the 1/n coefficient (tilt law) | GAP; CONJECTURE + NUMERICAL (§6) |
| GAP-p1 | p = 1 | not treated here (WP5a; see Plan 50, PROOF.md §3.19) |

Notation: as in ROUTE2 (t(z) = Nz^{−1/p}, u = log t = log N − (log z)/p, q_N, ϑ_N, w₀, D_w, Q-frame, ṽ, Q̃, α_x := (s − 1 − p)/p,
c_± = e^{∓iπα_x}) and RH_plt1b (θ_L := πp/4 the lip angle, θ_s := πp/2 the seam angle, S_in := {|arg z| < θ_s}, S_out, Γ± the seam
rays, L±, X, B_in = (1 + z)^c, B_out = (1 − z/(2πN))^{1/2}, c := ½ − 1/(2p), F, F̃). ν := ½ (= min(1/p, ½) for p < 1).

---

## 1. The strip: where the weight is evaluated for p < 1

ROUTE2's hypothesis (H_an) asks for L₁ analytic on |Im u| ≤ π/p, because for p > 1 the lips, lenses and saturated lips use
|arg z| up to (but below) π, and |Im u| = |arg z|/p. For p < 1, π/p > π, and the requirement would be **wider**. It is not
needed:

**Lemma S_w (where w is used, p < 1).** In the RH analysis of RH_plt1b, the weight w(z) = N^pt^{−s}Ψ₁(t) (equivalently q_N) is
evaluated only
- on the nodes and the band (real z > 0),
- in the band lens and Ω^△ (the regions between the real axis and the lens/Σ^△ lips), which lie in S_in (RH_plt1b §2
  "Containment": heights below δ tan(θ_s)/2 at Re z ≥ δ; the lips leave 0 at ±θ_L),
- on the hard-edge lips, at arg z = ±θ_L (KMVV rays at angle π − θ_L, RH_plt1b §2, KMVV angle freedom),
- in the (Y4)_x lens sector {0 < |arg s| < φ₀} with φ₀ ≤ θ_L (RH_plt1b §2: only φ₀ < πp is needed; RH_px §5),
- on the top closing segment N^p + δ′ ± i(0, δ) (arg ≈ δ/N^p, Re u ∈ [−c₀, 0]).

Ω_∞ = {|z| > N^p + δ′} never uses w (V = C_∞QF^{σ₃}); S_out ∩ U(0, δ) never uses w in Route II, because the hard-edge parametrix
uses W̃ := D_w (§3), not a continuation of w₀^{1/2} (RH_plt1b's glued W̃ did continue the *pure* power into S_out, which is
harmless for a power but would need |Im u| up to π/p for q_N). All these sets lie in {|arg z| ≤ θ_w} for some θ_w < θ_s, so
|Im u| ≤ θ_w/p < π/2. ∎

**Hypothesis (H_an^{<1}).** For some c₀ > 0, Ψ₁(t) = exp L₁(log t) with L₁ analytic on Σ_{1/2} := {Re u ≥ −c₀, |Im u| ≤ π/2},
real on ℝ, bounded on {u ∈ Σ_{1/2} : Re u ≤ 0}, and ε₁(T) := sup{|L₁′(u)| : u ∈ Σ_{1/2}, Re u ≥ T} → 0.

As in ROUTE2 §2: |L₁(u)| ≤ A_η + η Re u on Σ_{1/2}, hence |q_N(z)|^{±1} ≤ C_η(N^{η} + |z|^{−η/p}) on the weight-carrying
contours (Potter in the sector).

**RedA on the wider strip.** RedA(ii) holds for **every** σ₀ ≥ 0 (ROUTE2 §1; REVIEW_Plan48 check 1: |φ(τ + iσ − y)| =
φ(τ − y)e^{σ²/2}), so RedA's L₁ satisfies (H_an^{<1}), and would satisfy the π/p version as well; the strip enters only the
constant e^{σ₀²/2} in the rate of ε₁ (≈ 3.4 for σ₀ = π/2, versus e^{2π²} ≈ 3.7·10⁸ for σ₀ = π/p at p = ½). RedA(i), (iii)
hold for every p > 0 and s > 1 (ROUTE2 §1). So the derivative bounds needed on the strip hold.

**Why the narrow strip matters for explicit weights.** L₁(u) = √log(e^u + e) (Ψ₁(t) = exp √log(t + e)) has branch points where
e^u + e ∈ {0, 1}, i.e. at Im u = ±π (and odd multiples). It satisfies (H_an^{<1}) but **not** the π/p strip for p ≤ 1 (π/p ≥ π).
With Lemma S_w it can be used directly (rate O(1/n), no smoothing loss); this is the weight of the numerics (§6).

---

## 2. Set-up: what changes in RH_plt1b for w₁ = k^{−s}Ψ₁ (change table)

Measure σ₁ := Σ_k k^{−s}Ψ₁(k)δ_{k^{−p}}, 0 < p < 1. The weight becomes w ↦ w·q_N (after dividing by the constant Ψ₁(N)).

| RH_plt1b step | ROUTE2 §2 analogue (p > 1) | Change for w₁, p < 1 |
|---|---|---|
| §1 the seam scalar F (D in S_in, B_in, B_out, K, e^X; L±, Lemma S) | §1/§3 of RH_px: D̃, D, B, K, F (Binet-cut B) | **none**: L± and X are built from μ(t), e^{∓2πit}, B_in, B_out only (node data); Ψ₁ never enters F. Lemma S, X, the Liouville identity of RH_plt1b §4 unchanged |
| transformations U → R, band lens, Ω^△ | lens factors with w | w ↦ w·q_N, analytic in S_in by (H_an^{<1}) (|Im u| < π/2; §1). No new cut |
| band weight w₀ = W(4c − x)/(D̃B_ine^X)² | w₀ = W(b − x)/(D̃²B²) | **w₀ = C_N x^{α_x}(b − x)h_N(x)q_N(x)**, h_N := (D̃B_ine^X)^{−2}; D_w = D_{x^α}D_{(b−x)h_N}D_q (b := 4c(p)). Constants (e.g. e^{−2X(0)} = poly(N)) cancel in D_w²/w₀ |
| μ*, g, φ, φ̃, Lemmas 2.1–2.2 | unchanged | unchanged (p-free, G2 μ* for all p > 0; |log w₁| = O(log N) on the contours) |
| saturated region, Σ^△, top end (poly(N) ≪ N^{pN}) | q_N^{∓1} = poly(N) | the same: q_N^{±1} = poly(N) (Potter; Re u ∈ [−c₀, C] on the top pieces, L₁ bounded there) |
| Airy edge at b | q_N analytic in U(b, 2ε) | unchanged (|log q_N − log q_N(b)| ≤ Cε₁ in U(b, 2ε)) |
| hard edge: glued W̃ := (C(−z)^{α_x}(4c − z))^{1/2}/G̃ with a super-small seam jump 1 − e^{∓2πit} | replaced by the C–D comparison with W̃ := D_w | **replaced** as in ROUTE2 §3 with W̃ := D_w: D_w is analytic off [0, b], so the comparison parametrix has **no jump on the seams** (and none on (−δ, 0)); the split Ẽ_N = E^a + Φ of RH_plt1b §2 is not needed. Lips at ±θ_L, Bessel rays at π − θ_L |
| (Y4)_x (sum bound p-free; lens sector φ₀ < πp) | with Potter loss \|z\|^{−η} | the same with φ₀ ≤ θ_L |
| identification, small norm, extraction | small norm → C–D comparison | as ROUTE2 §4 |

**Do the seams and their jumps see Ψ₁?** No.
- F (hence V outside the lenses) is continuous, hence analytic, across Γ± (RH_plt1b §1), and is weight-free. So the true
  problem V, and Q := D_∞^{−σ₃}VD_w^{σ₃}, have **no jump on the seams**.
- The only seam jump in RH_plt1b came from the glued hard-edge W̃ (W̃_out/W̃_in = 1 − e^{∓2πit}). Route II replaces W̃ by
  D_w, which has no seam jump. So the seams disappear from the hard-edge analysis.
- What the seams still contribute is the factor e^{−2X} in h_N (through w₀). LW1′ needs an N-uniform modulus of continuity of X
  at 0 inside S_in; that is Lemma X0 (§3.2), which uses only the seam density L±, again weight-free.

---

## 3. The hard edge (comparison parametrix in the seam geometry)

### 3.1 Frame, comparison problem, local form

Exactly ROUTE2 §3.1–§3.2 with the RH_plt1b contour near 0: Σ ∩ U(0, δ) = band (0, δ) ∪ two lips leaving 0 at ±θ_L (plus the
super-small (h1) entries on the lips, now D/D̃ − 1 = O(exp(−2π sin(θ_L/p)|t|)) = O(exp(−√2πN|z|^{−1/p})), RH_plt1b §2). Lemma H1′
(P̃₀ := (−1)^NẼ_Nσ₃Ψ_α(N²f)σ₃D_w^{−σ₃}e^{Nφσ₃}, Ẽ_N weight-free and analytic, P̃₀ with V's band jump and the lip jump
[[1, 0], [c_±e^{2Nφ}/D_w², 1]], P̃₀N^{−1} = I + O(1/N) on ∂U(0, δ)) holds verbatim with KMVV's Ψ_α built on the angle π − θ_L
(KMVV angle freedom, quoted in `../CITATIONS.md`; as in RH_plt1b §2). The local form of ROUTE2 §3.2 (Ψ = Ψ̂ζ^{ασ₃/2}S, α ∉ ℤ;
Ψ = Ψ̂[[1, κ log ζ], [0, 1]]S, α = 0) holds on the sector |arg ζ| < π − θ_L where (6.23) is used: 2ζ^{1/2} has |arg| < π/2 there,
inside the principal-branch domain of DLMF §10.25(ii); in the other two sectors S is multiplied by the constant jump matrices.
Hence |Ψ^{±1}| ≤ C|ζ|^{−|α|/2} (log for α = 0) and Ψe₂e₁ᵀΨ^{−1} = O(|ζ|^{−|α|}) for |ζ| ≤ 3, as in ROUTE2. On the lips
|e^{2Nφ}| = |e^{−2ζ^{1/2}}·…| ≤ e^{−cN|z|^{1/2}} with c ≍ sin(θ_L/2) > 0 (arg ζ = ±(π − θ_L) on the lips, Re ζ^{1/2} =
|ζ|^{1/2}sin(θ_L/2)).

### 3.2 Lemma X0 (N-uniform modulus of the seam scalar at 0) — NEW, PROVED-mod-cite

Let 0 < p < 1, κ ∈ (0, 1), and Z_κ := {z ≠ 0 : dist(z, Γ₊ ∪ Γ₋) ≥ κ|z|}. There are C = C(p, κ) and N₀ such that for N ≥ N₀:
- (i) |L±(ζ)| ≤ C|ζ| for ζ ∈ Γ±, |ζ| ≤ 1, and |L±(ζ)| ≤ C(1 + log|ζ|) for |ζ| ≥ 1;
- (ii) |X(z) − X(0)| ≤ C|z|(1 + log⁺(1/|z|)) and |X′(z)| ≤ C(1 + log⁺(1/|z|)) for z ∈ Z_κ, |z| ≤ 1; |X(z) − X(0)| ≤ C(1 + log|z|)² for
  z ∈ Z_κ, |z| ≥ 1 (Rule R F3: squared log; only boundedness on [η₀, b] is used).

The band (arg 0) and the lips (arg ±θ_L) lie in Z_κ with κ = sin(θ_s − θ_L) = sin(πp/4).

*Sign convention (Rule R F2).* L± = log(D·B_in/B_out). With **Binet's function** μ (RH_px §1: D̃ = exp(−μ(t))), L± =
−μ(t) − Log(1 − e^{∓2πit}) + c·Log(1 + z) − ½Log(1 − z/(2πN)), exactly as RH_plt1b §1 writes it (its t → 0 expansion "−μ = ½log 2π +
½Log t + …" is also correct for Binet's μ). The only slip in RH_plt1b §1 is the sign of its **displayed definition** μ(t) := ½log 2π +
(t − ½)Log t − t − LogΓ(t), which is −μ_Binet. To avoid a clash with RH_px's μ, we write λ(t) := log D̃(t) = ½log 2π + (t − ½)Log t −
t − LogΓ(t) = −μ(t) (D̃ = √(2π)t^{t−½}e^{−t}/Γ(t), RH_plt1 §1); then L± = λ(t) − Log(1 − e^{∓2πit}) + …, which is what
`check_plt1_seam_winding.py` and `check_r2p_lw1.py` compute. No statement is affected (only |λ| = |μ| enters below). RH_plt1b.md
is not edited.

*Proof.* (i) On Γ₊, arg t = −π/2, t = −i|t|, |t| = N|ζ|^{−1/p}; e^{−2πit} = e^{−2π|t|} ∈ (0, 1).
- |ζ| ≤ 1 (|t| ≥ N): by DLMF 5.11.1 with the §5.11(ii) bound (quoted in `../CITATIONS.md` "(DLMF)", re-verified in "(DLMF-5.11,
  Plan 51)"), at |ph t| = π/2 the remainder after the k = 0 truncation is ≤ sec²(π/4)·(1/12)/|t|, so |λ(t)| ≤ 1/(6|t|) =
  |ζ|^{1/p}/(6N) ≤ |ζ|. |Log(1 − e^{−2π|t|})| ≤ 2e^{−2π|t|} ≤ 2e^{−2πN|ζ|^{−1/p}} ≤ C|ζ|. |c Log(1 + ζ)| ≤ C|ζ|.
  |½Log(1 − ζ/(2πN))| ≤ C|ζ|/N. So |L₊(ζ)| ≤ C|ζ| with C independent of N.
- |ζ| ≥ 1. If |t| ≥ 1: |λ(t)| ≤ 1/6. If |t| < 1: LogΓ(t) = LogΓ(1 + t) − Log t on Re t ≥ 0 (DLMF 5.5.1; both sides continuous on
  the closed right half-plane minus 0 and equal on (0, ∞)), and LogΓ(1 + t) is bounded on {|t| ≤ 1, Re t ≥ 0}; with |Log t| ≤
  |log|t|| + π/2 and |log|t|| = (1/p)log|ζ| − log N ≤ (1/p)log|ζ| (since |t| < 1), |λ(t)| ≤ C(1 + log|ζ|). Next
  |Log(1 − e^{−2π|t|})| ≤ C(1 + |log|t||) ≤ C(1 + log|ζ|) (for y := 2π|t| ∈ (0, 2π], 1 − e^{−y} ≥ (1 − e^{−2π})y/(2π); for
  |t| ≥ 1 it is ≤ 2e^{−2π}). |c Log(1 + ζ)| ≤ |c|(log(1 + |ζ|) + π). Finally ζ/(2πN) lies on the ray at angle
  θ_s ∈ (0, π/2), so |1 − ζ/(2πN)| ≥ sin θ_s and ≤ 1 + |ζ|: |Log(1 − ζ/(2πN))| ≤ C(1 + log(1 + |ζ|)). Γ₋ by conjugation.
(ii) X(z) − X(0) = (z/2πi)Σ±(±)∫_{Γ±}L±(ζ)dζ/(ζ(ζ − z)) and X′(z) = (1/2πi)Σ±(±)∫_{Γ±}L±(ζ)dζ/(ζ − z)² (differentiation under
the integral, z ∉ Γ). For z ∈ Z_κ and ζ ∈ Γ±: |ζ − z| ≥ κ|z|, and |ζ − z| ≥ |ζ|/2 if |ζ| ≥ 2|z|; hence |ζ − z| ≥ (κ/3)(|ζ| + |z|).
With (i), for |z| ≤ 1:
  |X(z) − X(0)| ≤ C|z|[∫_0^1 dρ/(ρ + |z|) + ∫_1^∞(1 + log ρ)ρ^{−2}dρ] ≤ C|z|(1 + log(1/|z|)),
  |X′(z)| ≤ C[∫_0^1 ρ dρ/(ρ + |z|)² + ∫_1^∞(1 + log ρ)ρ^{−2}dρ] ≤ C(1 + log(1/|z|)).
For |z| ≥ 1 the same splitting gives ∫_0^1 dρ/(ρ + |z|) ≤ 1/|z| and ∫_1^∞(1 + log ρ)ρ^{−1}(ρ + |z|)^{−1}dρ ≤ C(1 + log|z|)²/|z|. ∎

This makes quantitative the "N-uniform" statements of RH_plt1b §1 (F3) at the corner 0, which Route II needs because the
comparison mismatch (unlike RH_plt1b's exact glued W̃) sees log h_N on the lips. NUMERICAL (`check_r2p_lw1.out` [2]):
the implementation reproduces RH_plt1b's probe X(0) at p = 0.4, and at p = ½ the ratio |X(z) − X(0)|/(|z|(1 + log(1/|z|))) is
bounded uniformly in N = 10², 10⁴, 10⁶ (§6).

### 3.3 Lemma LW1′_{<1} (lip mismatch in the seam geometry) — PROVED

Let T_N := log N − (1/p)log max(b, δ), ε₁,N := ε₁(T_N) from (H_an^{<1}). On the lips in U(0, δ),

  |D_w(z)²/w₀(z) − c_±| ≤ C(|z|^{1/2}log(2/|z|) + ε₁,N),

C independent of N. Hence ‖v − ṽ‖_{L^∞(Σ)} ≤ Cε′_N, ε′_N := N^{−1}log N + ε₁,N → 0, and v − ṽ = δ_N e₂e₁ᵀ + (h1) with
δ_N := (D_w²/w₀ − c_±)e^{2Nφ}.

*Proof.* D_w²/w₀ is the product of the three ratios for q ∈ {x^{α_x}, (b − x)h_N, q_N}; constants cancel (D_{const}² = const),
so h_N may be replaced by h_N/h_N(0) = exp(−2(log D̃ + log B_in + X − X(0))) (log D̃(0⁺) = 0, B_in(0) = 1). Representation
(ROUTE2 §3.3): log D_q(z)² − log q(z) = (R(z)/π)∫_0^b(log q(x) − log q(z))dx/(√(x(b − x))(z − x)), |R(z)| ≤ C|z|^{1/2}, and on the
lips |z − x| ≥ c_p(x + |z|) (the lips leave 0 at ±θ_L; c_p ≍ sin θ_L).
- **x^{α_x}:** D² = (bz/Φ)^α, D²/z^α = c_±(1 + O(|z|^{1/2})): p-free (ROUTE2 §3.3).
- **(b − x)h_N:** log(b − x) is analytic near 0. For log h_N: on the closed sector {|arg z| ≤ θ_L, |z| ≤ η₀} (inside Z_κ and S_in),
  |log D̃(z)| = |λ(t)| ≤ C|z|^{1/p}/N (DLMF 5.11.1 + §5.11(ii); |arg t| ≤ θ_L/p = π/4), |log B_in(z)| ≤ C|z|, and |X(z) − X(0)| ≤
  C|z|(1 + log(1/|z|)) (Lemma X0). So |log h_N(z) − log h_N(0)| ≤ C|z|(1 + log(1/|z|)) ≤ C′|z|^{1/2}, N-uniformly, on the
  lips and on [0, η₀]; on [η₀, b] it is bounded N-uniformly (Lemma X0(ii), D̃ = 1 + O(1/N), B_in bounded), and h_N is analytic
  on a neighbourhood of (0, b] (no seam meets it). Then, with x = |z|u on [0, b/2],
    |log D_{h}(z)² − log h(z)| ≤ C|z|^{1/2}∫_0^{b/2}(x^{1/2} + |z|^{1/2})x^{−1/2}(x + |z|)^{−1}dx + C|z|^{1/2} ≤ C|z|^{1/2}log(2b/|z|),
  i.e. the Hölder exponent ν = ½, N-uniformly. (In ROUTE2 the same step used RH_px Lemma 3.4's (log D̃)′, (log B)′; here
  B_in is analytic and the seam scalar is controlled by Lemma X0.)
- **q_N:** as ROUTE2 §3.3, path = arc of radius |z| from arg z = ±θ_L to 0, then the segment to x: along it Re u ≥ T_N and
  |Im u| ≤ θ_L/p = π/4, so u ∈ Σ_{1/2}, and |log q_N(x) − log q_N(z)| ≤ ε₁,N(π/4 + |log(x/|z|)|/p) (Rule R F5). The scale-invariant integral
  ∫_0^∞(π/4 + |log u|/p)u^{−1/2}(1 + u)^{−1}du < ∞ gives |log D_q(z)² − log q_N(z)| ≤ C′ε₁,N.
- (h1) entries: super-small times |z|^{−η} (q_N factors). Finally sup_{lip}(|z|^{1/2}log(2/|z|) + ε₁,N)e^{−cN|z|^{1/2}} ≤
  C(N^{−1}log N + ε₁,N). ∎

NUMERICAL (`check_r2p_lw1.out` [1]; p = ½, lips at π/8 and π/16): sup|D_q²/q_N − 1|/η_N bounded, slowly increasing toward the
pure-tilt value π (§6).

---

## 4. Uniform resolvent, comparison, Theorem RII_{<1}

### 4.1 Lemma UR′_{<1} — PROVED-mod-cite

**Statement.** For α_x ∈ (−1, 1) there are N₀, C with ‖(1 − C_ṽ)^{−1}‖_{L²(Σ)} ≤ C for N ≥ N₀.

*Proof.* ROUTE2 §4.1 (UR′ (a), (b′), (c), (d), (e), Lemma W, Lemma W′) applies verbatim; the only inputs that depend on the
geometry are listed here.
- **Vertex 0** is a star of three C² arcs at the distinct angles 0, ±θ_L (no arc on (−δ, 0), no seam: §2). Lemma W (|a| = |α|/2 <
  ½) and Lemma W′ (α = 0) need only distinct angles and C² arcs; their norms depend on θ_L, i.e. on p, not on N.
- **(a)** area estimate: |Q̃^{−1}| ≤ C_N|z|^{−|α|/2} (local form, §3.1) ⇒ negative Laurent coefficients O(ε^{(1−|α|)/2}) → 0.
- **(b′)** factorization Q̃ = G(z)(−z)^{ασ₃/2}Θ(z) (resp. GΛΘ for α = 0) on U(0, r_N): G analytic with analytic inverse (N²f(z)/(−z)
  analytic positive near 0, f′(0) < 0 — RH_px Lemma 4.1, p-free per RH_plt1 amendments), Θ = S_jσ₃e^{Nφσ₃} constant per
  sector, the sectors now being delimited by the lips at ±θ_L and the band. The core bound |T_a(z)| ≤ C‖h‖d^{−1/2} (three ranges of
  |s|), the K-term C_N‖g‖|z|^{−|α|/2} and ∬_{ε<|z|<2ε}d^{−1/2}dA = O(ε^{3/2}) are angle-independent up to constants. So m ∈ ∂C(L²)
  for every |α| < 1.
- **(c)** partition: outside U(0, δ/2) ∪ U(b, ε/2), Q̃ = (D_∞^{−σ₃}𝒵̃D_∞^{σ₃})N₀ is bounded with bounded inverse (D_w cancels; no
  seam factor). The contour (band, lens/Σ^△ lips, saturated region, top pieces of length O(N^p)) is a finite union of C² arcs
  with long pieces straight: Carleson constant uniform in N, as in RH_ζ_close (c).
- **(d)** hard-edge piece: |ζ| ≥ 2 via KMVV (6.28) on the sectors with angle π − θ_L (uniform Bessel/Hankel asymptotics there,
  RH_plt1b §2); |ζ| ≤ 3 via the local form; K-term Hilbert–Schmidt ∬|s|^{−|α|}|z|^{−|α|} < ∞ and O(N^{−2}) at |ζ| ≤ 2.
- **(e)** Airy edge: unchanged (α-free; (D_w/W_r)^{±σ₃} bounded since q_N, h_N are analytic near b). ∎

### 4.2 (Q in L²), Theorem C′_{<1}, Proposition D′_{<1}

- *(Q in L²) at 0.* (Y4)_x of RH_plt1b §2 with the Potter loss: away from the band Σ_kk^{−s}Ψ₁(k)/max(|z|, k^{−p}) =
  O(1 + |z|^{α_x−η/p}) (p-free sum); in the lens sector 0 < arg s < φ₀ ≤ θ_L, 𝒦₋ − 𝒦₊ = −2iU₁₁wθ′ = O(|s|^{α_x−η/p}) (Potter in
  S_in) and Im θ < 0 there (φ₀ < πp). After the D_w^{σ₃} conjugation (|D_w| ≍ |z|^{α_x/2}|q_N|^{1/2} near 0 for fixed N, D_{h_N}
  bounded above and below by Lemma X0) Q = O(|z|^{−|α_x|/2−η}) ∈ L²_loc for η < (1 − |α_x|)/2. Other vertices: RH_plt1b
  (bounded). Q̃: UR′_{<1}(d)–(e).
- **Theorem C′_{<1}.** ‖(1 − C_v)^{−1}‖ ≤ 2C for N ≥ N₁: ‖C_v − C_ṽ‖ ≤ ‖C₋‖Cε′_N → 0 (LW1′_{<1}), then C–D Theorem 4.7's Neumann
  argument (quoted in `../CITATIONS.md`) with UR′_{<1}. Only ε′_N → 0 is used.
- **Proposition D′_{<1}.** Q₁ − Q̃₁, Q₂ − Q̃₂ = O(ε′_N/N). Proof of ROUTE2 D′ verbatim: |ζ| ≥ 2: ∫(|z|^{1/2}log + ε₁,N)|z|^{−1/2}
  e^{−cN|z|^{1/2}}|dz| = O(N^{−2}log N + ε₁,N/N); |ζ| ≤ 2: ε′_N·N·N^{−2}∫_0^2u^{−|α|}du = O(ε′_N/N); correction term O(ε′_N²/N);
  the constant c ≍ sin(θ_L/2) depends on p only.

### 4.3 Theorem RII_{<1}

**Theorem RII_{<1}.** Let 0 < p < 1, 1 < s < 1 + 2p (α_x ∈ (−1, 1)), and Ψ₁ = exp L₁(log t) with (H_an^{<1}) (strip |Im u| ≤ π/2).
For σ₁ = Σ_kk^{−s}Ψ₁(k)δ_{k^{−p}}:

  n^pb_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

As in ROUTE2 (Rule R F3 there), what is proved about the non-Fisher–Hartwig part is that the lip mismatch moves Q₁, Q₂ by
O(ε′_N/N) relative to the comparison problem Q̃; **no claim** that b_n(w₁)/b_n(k^{−s}) − 1 = O(ε₁/n) (GAP-rate).

*Proof.* Extraction as RH_plt1b §3 / ROUTE2 §4.4: (Q₁)₁₂(Q₁)₂₁ = N^{2p}b_N², a(Q) = N^pa_N via the invariance lemma (d₁ of
k = D_w/D_∞ finite for each N: log q_N, log h_N are integrable against dx/√(x(b − x))). For Q̃ = (D_∞^{−σ₃}𝒵̃D_∞^{σ₃})N₀ outside
the discs: (Q̃₁)₁₂(Q̃₁)₂₁ = c(p)²(1 + O(1/N)), a(Q̃) = 2c(p)(1 + O(1/N)) (RH_plt1b's small norm with the q_N^{±1} = poly(N) factors).
Proposition D′_{<1} gives Q₁ − Q̃₁, Q₂ − Q̃₂ = O(ε′_N/N). ∎

*Cited (Rule C; quoted in `../CITATIONS.md`):* WLXZ v1 §§3–5, §6.1; KMVV §6 ((6.16)–(6.28), (6.45), Prop. 6.5, angle freedom);
C–D Theorem 4.4 and the arguments of Theorem 4.7 / Proposition 4.9 (as in RH_ζ_close §1); DLMF 1.13.4, 1.14.38–40, 5.5.1 (new
quote, "(DLMF-5.11, Plan 51)"), 5.5.3, 5.11.1 + §5.11(ii), 5.12.1/3, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2; G2 μ*, B*(i)–(ii).
*New here:* Lemma S_w and (H_an^{<1}); the change table; the seam remark; Lemma X0; the h_N-part of LW1′_{<1}; the θ_L geometry
in UR′/D′.

---

## 5. Lemma CT-Ch (the Christoffel step) and the full range s > 1

### 5.1 Lemma CT-Ch — PROVED (self-contained)

Let σ be a positive measure on [0, ∞) with infinite support and finite moments, with orthonormal polynomials P = (P₀, P₁, …)
(positive leading coefficients) and Jacobi matrix J: xP_j = b_jP_{j+1} + a_jP_j + b_{j−1}P_{j−1} (j ≥ 0, b_{−1} := 0, b_j > 0).
(Indexing in this lemma: a_j = J_{jj}, b_j = J_{j+1,j}, j ≥ 0.)

**(o) Cholesky.** Every finite section J_n = (∫xP_iP_jdσ)_{i,j<n} is positive definite: vᵀJ_nv = ∫x|Σv_jP_j|²dσ > 0 for v ≠ 0,
since x ≥ 0 on supp σ and the polynomial Σv_jP_j ≠ 0 cannot vanish on the infinitely many points of supp σ ∩ (0, ∞). Its
Cholesky factor is lower bidiagonal (J_n tridiagonal) with positive diagonal, and by uniqueness the factor of J_n is the leading
block of that of J_{n+1}. So J = LLᵀ with L lower bidiagonal, L_{jj} = l_j > 0, L_{j+1,j} = m_j:

  a_j = l_j² + m_{j−1}² (m_{−1} := 0),  b_j = l_jm_j  (so m_j > 0).

**(i) Identity.** J̃ := LᵀL (tridiagonal: J̃_{jj} = ã_j := l_j² + m_j², J̃_{j+1,j} = b̃_j := m_jl_{j+1} > 0) is the Jacobi matrix of
xσ = x dσ(x), and R := L^{−1}P are its orthonormal polynomials.

*Proof.* L^{−1} is lower triangular, so R_j = Σ_{k≤j}(L^{−1})_{jk}P_k is a polynomial of degree j with leading coefficient
lc(P_j)/l_j > 0; all products below are finite sums, so associativity holds. From xP = JP = L(LᵀP): xR = L^{−1}(xP) = LᵀP, and
then LᵀLR = Lᵀ(LL^{−1}P) = LᵀP = xR. Orthonormality: ∫RRᵀx dσ = ∫(xR)Rᵀdσ = ∫(LᵀP)(L^{−1}P)ᵀdσ = Lᵀ(∫PPᵀdσ)L^{−ᵀ} = I.
A family of orthonormal polynomials with positive leading coefficients satisfying xR = J̃R with J̃ tridiagonal, b̃_j > 0, is the
orthonormal family of xσ and J̃ is its Jacobi matrix. ∎

**(ii) Limits.** Put r_j := l_j/m_j > 0, A_j := a_j/b_j, B_j := b_{j−1}/b_j. Then l_j² = b_jr_j, m_j² = b_j/r_j, and

  r_j = A_j − B_j/r_{j−1}  (j ≥ 1),  ã_j = b_j(r_j + 1/r_j),  b̃_j = (b_jb_{j+1})^{1/2}(r_{j+1}/r_j)^{1/2}.

If A_j → 2 and B_j → 1, then r_j → 1; hence ã_j/b_j → 2, b̃_j/b_j → 1, so ã_j/(2b̃_j) → 1 and b̃_{j−1}/b̃_j → 1.

*Proof.* Fix ε ∈ (0, ½] and δ := ε²/8; take j₀ with |A_j − 2|, |B_j − 1| ≤ δ for j ≥ j₀. Then r_j < A_j ≤ 2 + δ (j ≥ j₀), and with
T_j(r) := A_j − B_j/r:
  T_j(r) − r ≤ [2 + δ − (1 − δ)/r − r] = [−(1 − r)² + δ(1 + r)]/r.
- *Below.* If r_{j−1} ∈ (0, 1 − ε] for some j − 1 ≥ j₀, then r_j − r_{j−1} ≤ (−ε² + 2δ)/r_{j−1} ≤ −ε²/2, and r_j ≤ 1 − ε again;
  inductively r becomes ≤ 0 after finitely many steps, contradicting r > 0. So r_j > 1 − ε for all j ≥ j₀.
- *Above.* For r ∈ [1 + ε, 2 + δ]: (r − 1)²/r ≥ ε²/(1 + ε) and δ(1 + r)/r ≤ 2δ, so T_j(r) − r ≤ −ε²/(1 + ε) + 2δ ≤ −ε²/4. For
  r ∈ (1 − ε, 1 + ε): T_j(r) ≤ 2 + δ − (1 − δ)/(1 + ε) = 1 + ε/(1 + ε) + δ(1 + 1/(1 + ε)) < 1 + 2ε; for r ∈ [1 + ε, 1 + 2ε],
  T_j(r) ≤ r − ε²/4 < 1 + 2ε. So r_j decreases by ≥ ε²/4 while above 1 + ε, and once in (1 − ε, 1 + 2ε) it stays there.
Hence 1 − ε < r_j < 1 + 2ε for all large j; ε is arbitrary. The formulas give the rest. ∎

**(iii) Rate.** If |A_j − 2| + |B_j − 1| ≤ C/j (j ≥ 1), then r_j − 1 = O(j^{−1/2}), r_{j+1} − r_j = O(1/j), and
ã_j/(2b̃_j) − 1 = O(1/j), b̃_j/b_j − 1 = O(1/j).

*Proof.* By (ii), r_j ∈ [½, 2] for j ≥ j₁, so e_j := r_j − 1 satisfies e_j = e_{j−1}/(1 + e_{j−1}) + η_j with |η_j| ≤ |A_j − 2| +
2|B_j − 1| ≤ 2C/j. Let K² := 24C (so K² ≥ 12C) and j ≥ j₂ large.
- *Negative side.* If g := −e_j ≥ Kj^{−1/2}, then g_{j+1} = g/(1 − g) − η_{j+1} ≥ g + g² − 2C/j ≥ g + g²/2 (g² ≥ K²/j ≥ 4C/j) ≥
  K(j + 1)^{−1/2}; inductively g increases by ≥ g_j²/2 per step and exceeds 1 (r ≤ 0) in finitely many steps: impossible. So
  e_j > −Kj^{−1/2}.
- *Positive side.* If e_j ≥ Kj^{−1/2} (and e_j ≤ 1): e_{j+1} ≤ e_j − e_j²/2 + 2C/j ≤ e_j − e_j²/4 (e_j²/4 ≥ K²/(4j) ≥ 3C/j). If
  e_j ≤ Kj^{−1/2}: e_{j+1} ≤ e_j + 2C/j ≤ 2K(j + 1)^{−1/2} for large j. If e_j ∈ [Kj^{−1/2}, 2Kj^{−1/2}]: e_{j+1} ≤ 2Kj^{−1/2} −
  K²/(4j) ≤ 2K(j + 1)^{−1/2} once 2K(j^{−1/2} − (j + 1)^{−1/2}) ≤ Kj^{−3/2} ≤ K²/(4j), i.e. j ≥ 16/K². So the set
  {e_j ≤ 2Kj^{−1/2}} is invariant for large j, and it is entered: while e_j > 2Kj^{−1/2} ≥ Kj^{−1/2}, e_{j+1} ≤ e_j − e_j²/4, so
  1/e_{j+m} ≥ 1/e_j + m/4 (from 1/(e − e²/4) ≥ 1/e + 1/4), i.e. e_{j+m} ≤ 4/m, which is < 2K(j + m)^{−1/2} for m large.
So |e_j| ≤ 2Kj^{−1/2} for large j. Then r_{j+1} − r_j = e_{j+1} − e_j = −e_j²/(1 + e_j) + η_{j+1} = O(1/j), and
ã_j/(2b̃_j) = [(r_j + 1/r_j)/2]·(b_j/b_{j+1})^{1/2}(r_j/r_{j+1})^{1/2} = (1 + O(e_j²))(1 + O(1/j))(1 + O(1/j)) = 1 + O(1/j),
b̃_j/b_j = (b_{j+1}/b_j)^{1/2}(r_{j+1}/r_j)^{1/2} = 1 + O(1/j). ∎

*Relation to Plan 52 (Rule R F1).* Plan 52 (PROOF.md §3.21, ROUTE2_alpha.md, REVIEWED) proves the same transfer in LU/chain-sequence
variables g_j, h_j (its Lemmas CT, CS, CS-r; Theorems SH, SH-r). The dictionary is g_j = l_j², h_j = m_{j−1}², β_j = g_{j−1}h_j = b_{j−1}²,
r_j² = g_j/h_{j+1}: CT-Ch(i) is Plan 52's Christoffel identity, and CT-Ch(ii)/(iii) are CS/CS-r in ratio form, with ratio-only
hypotheses (A_j → 2, B_j → 1; no n^p normalization). The proof above is an independent second proof (classical; label PROVED).
Both CT-Ch(iii) and SH-r can be cited for the corollaries below. The O(j^{−1/2}) bound for r_j − 1 is sharp for the recursion
(reviewer: η_j = 0.5/j gives e_j√j → 0.7071); only increments enter the output rate.

*Use.* For σ_{s,Ψ} := Σ_kk^{−s}Ψ(k)δ_{k^{−p}}: xσ_{s,Ψ} = σ_{s+p,Ψ} exactly (x_k = k^{−p}); Ψ is unchanged. The pointwise Law P
for σ (n^pb_n → c(p), n^pa_n → 2c(p)) gives A_j → 2, B_j → 1, hence the law for xσ with the same c(p); with rate O(1/n) in, rate
O(1/n) out. (Index shifts between conventions cost O(1/n) only, since b_{j+1}/b_j = 1 + O(1/j).)

*Rule A for CT-Ch.* (a) Laguerre: J(x^αe^{−x}) ↦ J(x^{α+1}e^{−x}) exactly (check [2]). (b) A truncated measure (support [ε₀, 1], ε₀ > 0) violates the hypothesis: its
coefficients tend to a = (1 + ε₀)/2, b = (1 − ε₀)/4, so A_j → 2(1 + ε₀)/(1 − ε₀) > 2, and r_j tends to a root of r² − Ar + 1 = 0,
which is ≠ 1 — consistent (seen numerically: p = ½ atoms without a tail give r_j − 1 growing in j). (c) The converse (xσ ⇒ σ, Geronimus) is not claimed and
not used. (d) Positivity r_j > 0 is what excludes the second branch of the parabolic recursion; it holds because supp σ ⊂ [0, ∞).

### 5.2 Corollary RII⁺_{<1} and Corollary B_{p<1}

**Corollary RII⁺_{<1}.** Let 0 < p < 1, **s > 1**, and Ψ₁ with (H_an^{<1}). Then n^pb_n(k^{−s}Ψ₁) = c(p)(1 + O(1/n)) and
a_n/(2b_n) = 1 + O(1/n).

*Proof.* If s < 1 + 2p this is RII_{<1}. Otherwise let m := ⌈(s − 1)/p⌉ − 1 ≥ 1, s₀ := s − mp ∈ (1, 1 + p] ⊂ (1, 1 + 2p).
RII_{<1} for (s₀, Ψ₁), then Lemma CT-Ch(i)+(iii) m times (σ_{s₀} ↦ σ_{s₀+p} ↦ … ↦ σ_s). ∎

**Corollary B_{p<1}.** Let 0 < p < 1, s > 1, and Ψ > 0 slowly varying in sequence form (no boundedness, no D(γ) < ∞; e.g.
exp(√log k), exp((log k)^θ) (θ < 1), exp(√log k·sin log log k)). Then n^pb_n(k^{−s}Ψ) → c(p) and n^pa_n(k^{−s}Ψ) → 2c(p), with rate
O(1/n + ρ(n/M₀)) (ρ the RedA smoothing error); rate O(1/n) if Ψ itself satisfies (H_an^{<1}) (e.g. exp √log(k + e)).

*Proof.* RedA gives L₁ with (H_an^{<1}) (any strip) and (iii) (all p > 0, s > 1); RII⁺_{<1} gives the law for k^{−s}Ψ₁ with O(1/n);
RedA(iii) transfers it with the extra O(ρ(⌈n/M₀⌉)). ∎

With RH₁(r)/T3-log for p = 1 untouched, this gives the law for every sequence-form slowly varying Ψ (including D(γ) = ∞) for all
p ∈ (0, 1) ∪ (1, ∞) and all s > 1 (with Plan 52's B_all for p > 1, §5.3). It does not go through QL.

### 5.3 Remark CT-px (cross-reference to Plan 52's Corollary B_all)

Lemma CT-Ch applies verbatim for p > 1: Theorem RII (ROUTE2 §4.4; 1 < s < 1 + 2p) plus m CT-Ch steps give RII for every s > 1 with
O(1/n), and with RedA Corollary B_{p>1} for every s > 1. This is Plan 52's **Corollary B_all** (PROOF.md §3.21, ROUTE2_alpha.md,
REVIEWED), which closed ROUTE2's GAP-α for the law first; the present remark is an independent **second proof** via the Cholesky
form, not a new result (Rule R F1). The comparison frame itself still fails at α_x ≥ 1 (ROUTE2 §6); it is not needed there.

---

## 6. Numerics (NUMERICAL; p = ½, Ψ = exp √log(k + e), which satisfies (H_an^{<1}) directly)

Model measure (`checks/check_r2p_coeff.py`; Rule R F7: all coefficient numerics are for this **model measure**, one p, one Ψ; K-doubling
tests the atom/tail seam, not the tail-quadrature parameters): atoms k ≤ K plus a log-panel Gauss–Legendre quadrature tail of ∫_{K+½}^{10⁴⁸}t^{−s}Ψ(t)
δ_{t^{−p}}dt (the model of `../../checks/check_ql_numerics.py`, Plan 45). For p = ½ the hard-edge scale of degree n is k ~ n⁵
(10¹⁶ at n = 1600), so a tail is indispensable ([4]: atoms-only values are wrong in the first digit). RKPW long double;
K-doubling and a quad-precision check. Columns n = 100, 200, 400, 800, 1600.

**[1] Law P** (K = 10⁵ and 2·10⁵ agree to ≤ 10⁻⁷ in every entry; quad vs long double ≤ 5·10⁻¹⁴ [3]).
nB := n(n^pb_n/c(p) − 1), E := n(a_n/(2b_n) − 1) (pairing of `check_r2_coeff.py`; pure power: nB → −(s − 1)/2, E → p/2 = ¼):

| s (α_x) | covered by | nB for w = k^{−s}Ψ (n = 100 … 1600) | E for w | nB for v = k^{−s} |
|---|---|---|---|---|
| 1.5 (0) | RII_{<1} | −0.1542, −0.1570, −0.1602, −0.1633, −0.1663 | 0.2463 … 0.2498 | −0.2567 … −0.2520 |
| 1.75 (½) | RII_{<1} | −0.2785, −0.2817, −0.2850, −0.2882, −0.2913 | 0.2460 … 0.2498 | −0.3812 … −0.3770 |
| **2 (1)** | RII_{<1} at s₀ = 1.5 + one CT-Ch step | −0.4039, −0.4069, −0.4101, −0.4133, −0.4163 | 0.2494 … 0.2500 | −0.5069 … −0.5020 |
| 2.5 (2) | s₀ = 1.5 + two CT-Ch steps | −0.6575, −0.6588, −0.6611, −0.6638, −0.6665 | 0.2670 … 0.2512 | −0.7612 … −0.7523 |

All n·deviations are bounded (consistent with O(1/n)). The slow drift of nB for w is the tilt: n(b_n(w)/b_n(v) − 1)/ϑ_n ≈
(nB(w) − nB(v))/ϑ_n = 0.455 → 0.467 (s = 2, n = 100 → 1600), the p = ½ value of Plan 45 (§3.15: 0.44–0.47, rising toward ½);
the tilt law (GAP-rate) is not tested beyond that. The α_x = 1 and α_x = 2 rows behave exactly like the α_x ∈ (−1, 1) rows: the
comparison-frame restriction is a feature of the proof, not of the asymptotics.

**[2] Lemma CT-Ch.** LᵀL from the Cholesky factor of J(σ_s) equals the directly computed J(σ_{s+p}) to 8·10⁻¹⁷ (relative, all
j < 1601; s = 1.5 → 2 and 2 → 2.5, same quadrature nodes); Laguerre α ↦ α + 1 to 10⁻¹⁴. r_n − 1 = 4.9·10⁻³ … 3.4·10⁻⁴
(n(r_n − 1) = 0.49 … 0.55, s = 1.5) and 1.7·10⁻² … 1.1·10⁻³ (n(r_n − 1) = 1.70 … 1.78, s = 2): r_n − 1 = O(1/n) here, better than
the O(n^{−1/2}) that CT-Ch(iii) proves (the proof only uses the hypothesis, not the hard-edge structure).

**[4] Tail.** Atoms only (k ≤ 2·10⁵): nB = −1.8, −4.8, …, −106 at s = 1.5: the truncated measure has a soft edge at
x = K^{−1/2}, the law fails, and r_n − 1 grows (CT-Ch Rule A (b)).

**LW1′_{<1}** (`check_r2p_lw1.out` [1]; p = ½, rays π/8, π/16, |z| = 10⁻¹⁴ … 0.3, η_N sampled on |Im u| ≤ π/2):
sup|D_q²/q_N − 1| = 0.830, 0.687, 0.611, 0.538, 0.486 for N = 10², 10⁴, 10⁶, 10⁹, 10¹², ratio to η_N = 1.65, 1.97, 2.19, 2.39,
2.51 — bounded, increasing slowly toward the pure-tilt value π (as for p = 2 in ROUTE2 §3.3).

**Lemma X0** (`check_r2p_lw1.out` [2]): the implementation reproduces RH_plt1b's probe X(0) = −1.242, −1.933, −3.314, −4.695 at p = 0.4,
N = 10, 10², 10⁴, 10⁶ (probe: −1.24, −1.93, −3.31, −4.70; truncation tail ≤ 3·10⁻³). At p = ½,
sup_z|X(z) − X(0)|/(|z|(1 + log(1/|z|))) over the band and the lip ray π/8, |z| = 10⁻⁸ … 0.5, equals 0.230, 0.241, 0.242 for
N = 10², 10⁴, 10⁶ (flat in N; attained at |z| = 0.5); restricted to |z| ≤ 10⁻² it is 0.085, 0.088, 0.089 (flat in N; the
reviewer's per-radius values decrease as |z| → 0, consistent with X0 and even with O(|z|); Rule R F7(b)), while X(0) = −1.61, −2.76, −3.91 grows like log N (a constant, which cancels).

---

## 7. Gaps, stop conditions, Rule A

- **GAP-rate.** The 1/n coefficient: n^pb_n/c = 1 − (s − 1 − ϑ_n)/(2n) + o(ϑ_n/n) (tilt law) remains CONJECTURE; §6 is
  consistent with it at p = ½ (convergence in n is slow, ϑ_n ~ 1/(2√log n)).
- **The comparison frame at α_x ≥ 1** still fails (ROUTE2 GAP-α); Lemma CT-Ch (equivalently Plan 52's SH/SH-r) makes it unnecessary for the law (s ≥ 1 + 2p).
- **p = 1**: not treated (WP5a). Lemma CT-Ch would extend any Route II range for p = 1 of length > 1 in s to all s > 1.
- **Stop conditions** (outline §7): (i) as ROUTE2: RESOLVED-mod-cite (no continuation of w across (−δ, 0) or into S_out); (ii)
  MOOT (fixed order α_x). No new stop condition was hit.
- **Rule A (adversarial pass; logged in ../../LOG.md).**
  - (a) Ψ₁ ≡ const: ε₁ = 0, LW1′_{<1} reduces to the h_N/x^α parts, RII_{<1} to RH_plt1b (consistent).
  - (b) Ψ = k^ρ: ε₁ ↛ 0; the method correctly does not apply (the answer is RH_plt1b with s ↦ s − ρ).
  - (c) Strip: a weight with L₁ singular at |Im u| = π/2 exactly (e.g. L₁(u) = √log(e^{2u} + e)) is outside (H_an^{<1}) as stated,
    but the needed strip is only θ_w/p < π/2, and RedA smoothing covers any Ψ anyway. Is anything evaluated at |arg z| ≥ θ_s?
    Checked item by item in Lemma S_w; the only candidate (RH_plt1b's glued W̃ in S_out) is not used.
  - (d) X near 0: is the N-uniformity of Lemma X0 real? |L±| ≤ C|ζ| near 0 uses |t| ≥ N there (super-small e^{−2π|t|}); the
    log N growth of X is only in X(0) (a constant, cancels). Numerics [2b] flat in N.
  - (e) α_x → ±1 in RII_{<1}: constants of Lemma W and D′ blow up. The choice s₀ ∈ (1, 1 + p] avoids α_x → +1 but gives
    α_x(s₀) ∈ (−1, 0], arbitrarily close to −1 (harmless: RII_{<1} covers every |α_x| < 1 for fixed s). Remark (Rule R F6): for
    s > 1 + p/2 one may choose s₀ ∈ (1 + p/2, 1 + 3p/2], i.e. |α_x(s₀)| ≤ ½, so RII⁺_{<1} there needs only the |α_x| ≤ ½ part of
    UR′ (plus Lemma W′ at α_x = 0), as Plan 52 F2 noted for p > 1.
  - (f) CT-Ch: see §5.1 Rule A; the identity is checked to 10⁻¹⁷ on the p = ½ model and exactly on Laguerre.
  - (g) Does s₀ ∈ (1, 1 + p] ⊂ (1, 1 + 2p) always exist? m = ⌈(s − 1)/p⌉ − 1 gives s − mp ∈ (1, 1 + p] for s > 1 + p; for s ≤ 1 + p
    take m = 0. Yes.
