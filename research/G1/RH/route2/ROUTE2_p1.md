# ROUTE2_p1: Route II for p = 1 — the pointwise Law P for k^{−r}Ψ, Ψ slowly varying, x_k = 1/k (Plan 50, WP5a)

Status: **Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan50.md), fixes applied — REVIEWED** (F1–F10 applied after merging master, which contains Plan 52, PROOF.md §3.21). Novelty: UNCHECKED (no Rule L search).

*(Plan 55 note, 2026-10-15: the conclusion of Theorem RII₁ and the rate clauses of Corollaries B_{p=1}, B_{p=1}⁺ also hold under (A_ϑ) for any ϑ > 0 instead of (H_an₁), because they are contained in RII_x1 (ROUTE2_xframe1.md, 1 < r < 3), whose hypothesis can be so weakened; the band-centre proof below was not re-examined for thin strips; verified on Paper 2's consolidated write-up (papers/paper2), see ../../PROOF.md §3.24 (Theorem AS, PROVED-mod-cite, proof of record papers/paper2 rev. 3 + §3.24 audit; Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan55.md), fixes applied — REVIEWED). This file is unchanged and proves its results as stated.)*

Source: `research/program/outline_B_sv.md` §5 Route II, work package WP5 (p = 1 part). Templates: `ROUTE2.md` (Plan 48,
REVIEWED; p > 1) and its review `../../review/REVIEW_Plan48.md` (UR′(b′), Conway–Deift comparison); base analysis
`../RH_p1_general.md` (Theorem RH₁(r), REVIEWED) and `../RH_p1.md` (RH₁, REVIEWED); C–D precedent `../zeta/RH_zeta_close.md`
§1 (REVIEWED); PROOF.md §3.16 (QLP; the p = 1 remarks: lips at ±π/4, ±3π/4, small norm only I + O(n^{−1/2}) at off-contour
points, Lemma M amplification). Numerics: `checks/check_r2p1_{lw1,coeff,ct}.py/.out`.

**Labels (per step).**

| Item | Statement (short) | Label |
|---|---|---|
| §1 RedA at p = 1 | ROUTE2 Lemma RedA applies verbatim (it is stated for every p > 0 and every strip) | PROVED (ROUTE2 §1, REVIEWED); the p = 1 check is §1 here |
| §2 set-up | (H_an₁) on the open strip \|Im u\| < π; change table for RH₁(r) | PROVED (bookkeeping), each changed step proved in §§3–4 |
| §3.1 Lemma H1₁ | band-centre comparison parametrix with W̃ := W·D_ϱ (D_ϱ = Szegő function of the whole non-Fisher–Hartwig band factor); Ẽ_n = const·(KV's E_n for the pure \|x\|^{2a}) | PROVED-mod-cite (KV §5 (5.6), (5.9), (5.10), (5.17)–(5.20), (5.25)–(5.30), p. 19; Vanlessen (4.43)–(4.46); RH₁(r) Lemmas B, G) |
| §3.2 Lemma LF₁ | Ψ_a = Ψ̂(ζ)ζ^{aσ₃}S_j, Ψ̂ entire, det Ψ̂ = 1, for \|a\| < ½ | PROVED-mod-cite (Vanlessen (4.27), (4.53); KV (5.17)–(5.20); DLMF 10.25.2, 10.27.4) |
| §3.3 Lemma LW1₁ | lip mismatch \|D_ϱ²/ϱ − 1\| ≤ C(\|z\| + ε₁,n) in U(0, δ), with no decay in \|z\| for the q_n part | PROVED-mod-cite (DLMF 5.11 for the H_n part only); NEW (the even pairing) |
| §4.1 Lemma UR₁ (incl. (b′)) | uniform resolvent of the comparison problem, \|a\| < ½ | PROVED-mod-cite (as RH_ζ_close Lemma UR; Lemma W with exponents ±a) |
| §4.2–4.3 C₁, D₁ | ‖(1 − C_v)^{−1}‖ ≤ 2C; Q₁ − Q̃₁ = O(ε′_n/n) | PROVED-mod-cite (C–D Thm 4.4, arguments of Thm 4.7 / Prop. 4.9) |
| **Theorem RII₁** | p = 1, **1 < r < 2**, (H_an₁): nβ_n = 1 + O(1/n), nb_n = ½(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n) | **PROVED-mod-cite** (WLXZ v1 §§2–6 via RH₁/RH₁(r); KV §5; Vanlessen §4; C–D Thm 4.4 + 4.7/4.9 arguments via RH_ζ_close §1; DLMF 5.11, 10.25.2, 10.27.4, and those of Lemma W); Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan50.md), fixes applied — REVIEWED |
| **Corollary B_{p=1}** | p = 1, 1 < r < 2, Ψ sequence-form slowly varying (incl. D(γ) = ∞): nb_n → ½, na_n → 1, rate O(1/n + ρ(n/M₀)) | PROVED-mod-cite (RII₁ + RedA); Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan50.md), fixes applied — REVIEWED |
| **Lemma CT₁ (Cholesky form)** | (i) J(xμ) = LᵀL if J(μ) = LLᵀ — master's Lemma CT (§3.21, Plan 52) in other coordinates (g_n = l_n², h_n = m_{n−1}²); (ii) "⟹" = master's Lemma CS + Theorem SH; **(ii) "⟸": Law P for xμ ⇒ Law P for μ, for every positive bidiagonal factorization (new relative to §3.21)**; supp μ ⊂ [0, ∞) | (i), "⟹": cited from §3.21 (REVIEWED; the proof here is an alternative); "⟸": PROVED (self-contained); very likely KNOWN in chain-sequence form (Wall; Chihara 1978 Ch. III — not read, pointer only), novelty UNCHECKED |
| Lemma D | parabolic dynamics: (a) x_n > 0, x_{n+1} = A_{n+1} − B_n/x_n ⇒ x_n → 1 (alternative proof of master's CS); (b) 0 < z_n < A_n, z_{n+1} = B_n/(A_n − z_n) ⇒ z_n → 1 (used for "⟸") | PROVED |
| **Corollary B_{p=1}⁺** | p = 1, **every non-integer r > 1**, Ψ sequence-form slowly varying: the law, with rate O(1/n) if Ψ satisfies (H_an₁), and with the regular majorant of 1/n + ρ(⌈n/M₀⌉) in general | PROVED-mod-cite (B_{p=1} + master's Theorem SH-r, §3.21); Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan50.md), fixes applied — REVIEWED |
| (Corollary B_{p>1}⁺ — withdrawn as a separate result) | p > 1, every s > 1 | = master's **Corollary B_all** (Plan 52, §3.21, REVIEWED, with rate); not claimed here |
| GAP-int | *(Plan 54 note, 2026-10-14, Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan54.md), fixes applied — REVIEWED: GAP-int is closed — p = 1, every integer r ≥ 2, by Route II in the unsymmetrized x-frame (Theorem RII_x1, 1 < r < 3) and SH-r; PROOF.md §3.23, `ROUTE2_xframe1.md`.)* p = 1, r ∈ {2, 3, 4, …} with D(γ) = ∞; by CT₁ "⟺" equivalent to the law at the single exponent r = 2 (a = ½, α_x = 0) | GAP (§7) |
| OBSTRUCTION-a | the C–D frame at the band centre needs \|a\| < ½: Q̃ ∉ L²_loc and Lemma W fails at \|a\| ≥ ½ | OBSTRUCTION (scoped to this frame; §7) |
| GAP-rate₁ | the 1/n coefficient (tilt law) | GAP; tilt law CONJECTURE + NUMERICAL (§6) |

Notation (RH_p1_general / RH_p1): WLXZ = Wu–Lin–Xu–Zhao arXiv:1410.3948v1 at α_W = 1; n = degree of the orthogonal polynomials
of the **symmetrized** measure (nodes ±k^{−1/2}, masses halved); z = WLXZ's rescaled variable, t = n/z² the rescaled index
variable, band [−2, 2]; β_n := squared recurrence coefficients of the symmetrized measure, so that a_m = β_{2m−2} + β_{2m−1},
b_m² = β_{2m−1}β_{2m}; H(t) = Γ(t + 1)e^t/(√(2π)t^{t+1/2}), H_n(z) := H(n/z²); the Fisher–Hartwig exponent at the band centre is

  **a := r − 3/2 > −½**  (KV's α; the KV/Vanlessen Bessel model Ψ_a is built from Bessel functions of orders a ± ½),

and the hard-edge (unsymmetrized, x = y²) order is α_x = r − 2 = a − ½. f, φ, P^{(∞)}, W, ω, E, E_n, Ψ_a, Σ₁, …, Σ₈ are those of
KV §5 (with KV's φ = −φ_WLXZ, as in RH₁(r) §5, "Dictionary"). R(z) := (z − 2)^{1/2}(z + 2)^{1/2} (cut [−2, 2], R ~ z at ∞),
Φ(z) := (z + R(z))/2. Principal branches unless said otherwise.

---

## 1. RedA at p = 1 (no change)

ROUTE2 Lemma RedA (PROVED, REVIEWED) is stated for x_k = k^{−p} with **every p > 0** in (iii), and (ii) holds **in every strip
|Im u| ≤ σ₀**. Checked for p = 1:
- (o)–(ii) do not involve p.
- (iii) is T3-conv's proof with base vΨ₁; its p-dependence is only through Sat_p⁺ (PROOF.md §3.3, "all p > 0") and the head
  margin M₀(p). Nothing else changes at p = 1.
- **Strip width needed at p = 1.** The analytic weight is evaluated at t = n/z² with z in WLXZ's regions, so u = log t =
  log n − Log z² and Im u = −arg(z²). Those regions (band, lens, lips, saturated region, Σ^△, the vertical segments up to ±k_n)
  lie in sectors |arg(±z)| ≤ π/2 − θ_W for some θ_W > 0 (RH_p1.md §2, "Stirling with a sectorial bound"), and the lips inside
  U(0, δ) in |arg(±z)| ≤ π/4 + π/24 (PROOF.md §3.16, Lemma Z, geometry). Hence |Im u| ≤ π − 2θ_W everywhere, and
  |Im u| ≤ π/2 + π/12 on the lips: **the open strip |Im u| < π suffices.** This is the p > 1 strip |Im u| ≤ π/p at p = 1, but
  open. It must be open for the model example: L₁(u) = √(log(e^u + e)) (Ψ₁(t) = exp √log(t + e)) has branch points on
  Im u = ±π. The weight is never evaluated near iℝ in the z-plane (§3.1: the comparison parametrix never continues the weight
  across iℝ), which is where a glued construction would need Im u = ±π (§2, last paragraph).
- RedA's L₁ is entire, real on ℝ, bounded on {−c₀ ≤ Re u ≤ 0, |Im u| ≤ π} for every c₀ (L is constant on y ≤ 0), and
  ε₁(T) → 0 uniformly on |Im u| ≤ π by (ii). So it satisfies (H_an₁) below.

---

## 2. Set-up for w₁ = k^{−r}Ψ₁, and what changes in RH₁(r)

**Hypothesis (H_an₁).** For some c₀ > log 2, Ψ₁(t) = exp L₁(log t), where L₁ is analytic on {u : Re u > −c₀, |Im u| < π}, real
on the real axis, and for every θ ∈ (0, π): L₁ is bounded on {−c₀ < Re u ≤ 0, |Im u| ≤ π − θ}, and
  ε₁(T; θ) := sup{|L₁′(u)| : Re u ≥ T, |Im u| ≤ π − θ} → 0  (T → ∞).
(c₀ > log 2 because WLXZ's pieces near ±k_n have t ≥ ½, RH_p1.md §2 step 2.) Consequence (Potter in the sector): for every
η > 0 and θ, |L₁(u)| ≤ A + η Re u on {Re u ≥ 0, |Im u| ≤ π − θ}; so |Ψ₁(t)|^{±1} ≤ C_η|t|^η for |arg t| ≤ π − θ, |t| ≥ 1.

Measure σ_{r,Ψ₁} := Σ_k k^{−r}Ψ₁(k)δ_{1/k}. In RH₁(r) §1 the analytic weight wH_n(z²)^a acquires the factor Ψ₁(n/z²); dividing by
the constant Ψ₁(n) (which does not change β_n),

  q_n(z) := Ψ₁(n/z²)/Ψ₁(n) = exp(L₁(log n − Log z²) − L₁(log n)),

analytic on ℂ ∖ iℝ (where |Im u| < π), **even** (q_n(−z) = q_n(z)), positive on ℝ ∖ {0}. The band weight of V (RH₁(r) §2,
"Weight bookkeeping") becomes

  m_σ(x) = e^L(4 − x²)·H_n(x)²·|x|^{2a}·q_n(x) =: |x|^{2a}ϱ(x),  ϱ := h_W·H_n²·q_n,  h_W(x) := e^L(4 − x²),

and the lens/saturated entries carry the analytic continuation of m_σ (upper-right × F q_n, lower-left × (F q_n)^{−1}).

**Table (RH₁(r) step → change).**

| RH₁(r) step | Uses the weight? | Change for w₁ |
|---|---|---|
| §1 identification | yes | F = H_n(z²)^a ↦ F·q_n; q_n analytic on ℂ ∖ iℝ by (H_an₁) |
| §2 Lemma W1(r): R, T, Q, V, pole removal (3.13)–(3.18) | algebraic in w | unchanged; q_n analytic nonvanishing on the Ω-regions (|arg(±z)| ≤ π/2 − θ_W) and at the nodes |
| §2 saturated pieces 2 − ε ≤ \|z\| ≤ k_n, Σ^△, vertical segments | w^{±1} | extra factor q_n^{±1} with Re u ∈ [−log 2, log n + C], \|Im u\| ≤ π − 2θ_W: \|log q_n\| ≤ 2A + 2η log n + C, so q_n^{±1} = O(n^{2η}), absorbed by e^{−cn} |
| §3 Lemma S (Stirling truncation Q_m), Lemma G, N_r, model mismatch κ_n | yes | **not used**: the global parametrix is the exact Szegő parametrix of m_σ, N_σ := 𝔇_∞^{σ₃}N₀𝔇^{−σ₃}, 𝔇 := D_a·D_ϱ (§3.1); no band mismatch outside the discs |
| §3 extraction value (N₁)₁₂(N₁)₂₁ = 1 | no | unchanged (invariance; 𝔇's 1/z-coefficient is finite for each n, §4.4) |
| §4 Airy discs U(±2, ε) | yes, via A = Ng^{σ₃}N^{−1} | g := ϱ₁^{1/2}/(D_aD_q), ϱ₁ := \|x\|^{2a}q_n (analytic in U(±2, 2ε)); D_H = 1 + O(1/n) factor; matching I + O(1/n) (§3.4) |
| §5 origin: KV/Vanlessen parametrix with W_h = Wh₀^{1/2}, Lemma M (quotient, small norm) | yes | **replaced** by the C–D comparison (§§3–4): W̃ := W·D_ϱ; q_n is never continued across iℝ |
| §6 (Y4)_r, Lemmas O1, X, identification | masses; lens K± | (Y4)_r with a Potter loss \|z\|^{−2η}; O1/X replaced by "Q ∈ I + ∂C(L²)" (§4.2) |
| §7 small norm, extraction | — | small norm only for the comparison problem 𝒵̃; the true problem via Theorem C₁ and Proposition D₁ |

**Why the direct (quotient) construction is not used** (the p = 1 form of ROUTE2's stop condition (i)). RH₁(r)'s origin
parametrix needs the analytic continuation h of the non-FH band factor to all of U(0, δ), since KV's W_h = W·h^{1/2} must have no
jump on Σ₃ ∪ Σ₇ = iℝ (where Ψ_a's jump e^{πiaσ₃} is cancelled by W's cut). For h ∋ q_n the continuation across iℝ evaluates
L₁ at Im u = ±π: (i) for exp √log(t + e) this is the branch line, so q_n has no continuation there at all; (ii) even when L₁ is
analytic there, the jump of q_n^{1/2} across iℝ is exp(½(L₁(T − iπ) − L₁(T + iπ))) = 1 + O(ε₁) with no rate, which conjugated by
Ψ_a (amplification ρ^{−2|a|}, RH₁(r) Lemma M) is unbounded at ζ → 0 for a ≠ 0 and not small at a = 0. Absorbing the tilt
z^{−2ϑ_n} into a drifting exponent a − ϑ_n leaves e^{ρ_n} with the same defect. So the quotient argument fails, as at p > 1,
and the C–D comparison is used instead. At p = 1 it also needs only the open strip.

---

## 3. The band centre by a Conway–Deift comparison

Restriction (needed in §4): **|a| < ½, i.e. 1 < r < 2** (equivalently α_x ∈ (−1, 0)).

### 3.1 The frame and the comparison parametrix (Lemma H1₁)

*Szegő functions.* D_a(z) := (z/Φ(z))^a (RH₁(r) Lemma G: D_{a,+}D_{a,−} = |x|^{2a}, D_a(∞) = 1, |D_a|/|z|^a bounded above and
below near 0). For a weight ϱ > 0 on (−2, 2) with log ϱ ∈ L¹(dx/√(4 − x²)),
  log D_ϱ(z) := (R(z)/2π)∫_{−2}^{2}log ϱ(x)dx/(√(4 − x²)(z − x))   (z ∉ [−2, 2]),
so that D_{ϱ,+}D_{ϱ,−} = ϱ on (−2, 2) (Plemelj, with R₊(x) = i√(4 − x²)), D_ϱ is analytic and zero-free off [−2, 2], and
D_ϱ(∞) is finite. D_ϱ = D_{h_W}·D_H·D_q multiplicatively. Explicitly D_{h_W} = e^{L/2}R/Φ (since R₊R₋ = 4 − x², Φ₊Φ₋ = 1,
R/Φ → 1); D_H = 1 + O(1/n) uniformly (|log H_n(x)²| ≤ Cx²/n on the band, DLMF 5.11 as in RH₁(r) Lemma S); log q_n ∈
L¹(dx/√(4 − x²)) for each n since |log q_n(x)| ≤ A′ + 2η log(2/|x|) (Potter). Put

  𝔇 := D_a·D_ϱ  (the Szegő function of m_σ),  N_σ := 𝔇_∞^{σ₃}N₀𝔇^{−σ₃},

where N₀ is the normalized solution with jump [[0, −1], [1, 0]] on (−2, 2) and |z ∓ 2|^{−1/4} endpoint bounds. N_σ is the global
parametrix with band jump [[0, −m_σ], [1/m_σ, 0]] exactly. (WLXZ's N, band weight h_W, equals D_{h_W,∞}^{σ₃}N₀D_{h_W}^{−σ₃}: both
solve the same normalized problem, and the quotient has an isolated singularity at ±2 of order |z ∓ 2|^{−1/2} by the column
exponents −3/4, 1/4 of WLXZ (5.11) (RH₁(r) §4), hence removable; the quotient is I.)

*Frame.* Work in KV's frame (V ↦ σ₃Vσ₃, RH₁(r) §5 "Dictionary") and put

  Q := 𝔇_∞^{−σ₃}·V·𝔇^{σ₃}.

Its jumps v: band (−2, 2): [[0, 1], [−1, 0]] (since 𝔇₊𝔇₋ = m_σ); lips: lower-triangular with (2,1) entry
𝔇²ω^{−1}ϱ^{−1}e^{−2nφ} (ϱ continued from the band, ω = (z²)^a as in KV (3.6)), plus the (J2) entries of RH₁(r) Lemma M
(diagonal D/D̂ − 1, upper-right) which are O(e^{−cn/|z|²}poly(n, 1/|z|)); saturated pieces etc. as in RH₁(r) Lemma W1(r).
Nothing jumps on iℝ.

**Lemma H1₁ (comparison parametrix).** In U(0, δ) put

  P̃₀ := Ẽ_n(z)·Ψ_a(nf(z))·W̃(z)^{−σ₃}·e^{−nφ(z)σ₃},  W̃ := W·D_ϱ,  Ẽ_n := Ẽ·e^{nφ₊(0)σ₃}e^{−πiσ₃/4}(1/√2)[[1, i], [i, 1]],

with Ẽ := P̃^{(∞)}W̃^{σ₃}e^{±½aπiσ₃} (and the anti-diagonal factor in f^{−1}(V ∪ … ∪ VIII)) exactly as KV (5.27)–(5.30), where
P̃^{(∞)} := σ₃N_σσ₃. Then:
- **(i)** Ẽ = (𝔇_∞/D_{a,∞})^{σ₃}·E^{KV}, where E^{KV} is KV's E (5.27)–(5.30) for the **pure** weight |x|^{2a} on the single
  interval [−2, 2] (P^{(∞)} = σ₃N₀^{(a)}σ₃, N₀^{(a)} := D_{a,∞}^{σ₃}N₀D_a^{−σ₃}). In particular Ẽ_n does not involve ϱ except
  through the constant 𝔇_∞; Ẽ_n is analytic in U(0, δ), det Ẽ_n = 1, and 𝔇_∞^{−σ₃}Ẽ_n and its inverse are bounded on U(0, δ)
  uniformly in n.
- **(ii)** P̃₀ has exactly V's band jump in U(0, δ), no jump on iℝ (Σ₃ ∪ Σ₇), and on the lips the lower-triangular jump with
  (2,1) entry ω^{−1}D_ϱ^{−2}e^{−2nφ} (KV frame).
- **(iii)** 𝔇_∞^{−σ₃}(P̃₀(σ₃N_σσ₃)^{−1} − I)𝔇_∞^{σ₃} = O(1/n) uniformly on ∂U(0, δ).

*Proof.* (i) P̃^{(∞)}W̃^{σ₃} = σ₃𝔇_∞^{σ₃}N₀𝔇^{−σ₃}σ₃W^{σ₃}D_ϱ^{σ₃} = 𝔇_∞^{σ₃}σ₃N₀σ₃(W/D_a)^{σ₃} (diagonal factors commute with
σ₃ and D_ϱ cancels), which is (𝔇_∞/D_{a,∞})^{σ₃} times KV's P^{(∞)}W^{σ₃} for |x|^{2a}. KV p. 19: E is analytic in a full
neighbourhood of U_δ, "Here we need the fact that D(z)/W(z) and W(z)/D(z) remain bounded as z → 0" — here D = D_a, bounded by
RH₁(r) Lemma G(iv). E^{KV} = σ₃N₀^{(a)}σ₃W^{σ₃}e^{±½aπiσ₃}(·) is n-independent: its factors are, and its sectors
f^{−1}(I ∪ II), … are bounded by f^{−1}(ℝ ∪ iℝ) = ℝ ∪ iℝ (f is real on ℝ and odd, so f(iℝ) ⊂ iℝ; RH₁(r) §5, "Parity").
|e^{nφ₊(0)}| = 1 (φ₊(0) ∈ iℝ) and D_{a,∞} = 1; so 𝔇_∞^{−σ₃}Ẽ_n is bounded with bounded inverse uniformly in n. det Ẽ_n = 1:
det N₀ = 1 (explicit) and the remaining factors are diagonal or constant with determinant 1.
(ii) KV, after (5.25): "for every matrix valued function E_n analytic in a neighborhood of U_δ, the matrix valued function P
given by (5.25), satisfies conditions (a), (b) and (d)": with W, the band jump is [[0, W₊W₋], [−1/(W₊W₋), 0]] = [[0, |x|^{2a}],
[−|x|^{−2a}, 0]] and the lip (2,1) entry is ω^{−1}e^{−2nφ} (KV (5.1)–(5.2)); the computation is entrywise in the scalar W
(P₋^{−1}P₊ = e^{nφ₋σ₃}W₋^{σ₃}J_ΨW₊^{−σ₃}e^{−nφ₊σ₃}, φ₊ + φ₋ = 0 on the band). Replacing W by W̃ = WD_ϱ, with D_ϱ analytic in
U(0, δ) ∖ [−δ, δ], multiplies the band (1,2) entry by D_{ϱ,+}D_{ϱ,−} = ϱ (giving m_σ), the lip (2,1) entry by D_ϱ^{−2}, and
leaves the iℝ cancellation (KV (5.9), (5.13)/(5.19)) unchanged.
(iii) P̃₀(σ₃N_σσ₃)^{−1} = (𝔇_∞/D_{a,∞})^{σ₃}·[E_n^{KV}Ψ_a(nf)W^{−σ₃}e^{−nφσ₃}·P^{(∞),−1}]·(𝔇_∞/D_{a,∞})^{−σ₃}, because
W̃^{−σ₃}·(σ₃N_σσ₃)^{−1} = W^{−σ₃}D_a^{σ₃}·σ₃N₀^{−1}σ₃·𝔇_∞^{−σ₃} (D_ϱ cancels between W̃ and 𝔇; diagonal factors commute). The bracket is KV's P·P^{(∞),−1} for the pure power, which is
I + O(1/n) on ∂U_δ by KV (5.3)/(c) via Vanlessen (4.43)–(4.46) (RH₁(r) Lemma B(iv) is this computation). ∎

*Large-ζ form.* For ζ ∈ ℂ± KV (5.6) gives −nφ(z) = ±iζ ∓ nφ₊(0) (ζ := nf(z)). With Vanlessen (4.43)–(4.46),
Ψ_a(ζ) = B(I + O(1/ζ))e^{πiσ₃/4}e^{−iζσ₃}D_j (upper half-plane; D_j diagonal) and = B(I + O(1/ζ))e^{πiσ₃/4}e^{−iζσ₃}D_jJ (lower
half-plane; J = [[0, −1], [1, 0]]), B constant. Since Je^{−iζσ₃} = e^{iζσ₃}J,

  P̃₀𝔇^{σ₃} = Ẽ_n·Φ(ζ)·Θ(z),  Φ(ζ) := Ψ_a(ζ)e^{±iζσ₃},  Θ(z) := e^{∓nφ₊(0)σ₃}(D_a(z)/W(z))^{σ₃}  (ζ ∈ ℂ±),

with Φ(ζ) = B(I + O(1/ζ))e^{πiσ₃/4}·(D_j or D_jJ): **Φ and Φ^{−1} are bounded for |ζ| ≥ 2** (for 2 ≤ |ζ| ≤ R₀ by continuity up to
the rays and det Φ = 1), and Θ, Θ^{−1} are bounded on U(0, δ) uniformly in n. There is **no N^{σ₃/2}-type factor** (unlike the
hard edge): the Bessel scale is |z| ≍ 1/n and conjugation by the parametrix costs O(1) there.

### 3.2 Local form of Ψ_a for |a| < ½ (Lemma LF₁)

Sources: Vanlessen (4.27) (sector II), (4.53) (det Ψ ≡ 1); KV (5.17)–(5.20) (constant jumps); DLMF 10.25.2 (with §10.25(ii),
principal branch) and 10.27.4 (quoted in `../CITATIONS.md` DLMF-4 / DLMF-2, re-verified as DLMF-5). For |a| < ½ the orders
ν = a ± ½ lie in (−1, 1) ∖ {0} and are **never integers**, so 10.27.4 applies and no logarithm appears (contrast ROUTE2 §3.2,
where α = 0 needed Lemma W′).

**Lemma LF₁.** For |a| < ½ there are an entire Ψ̂ with det Ψ̂ ≡ 1 and constant matrices S_j (j = I, …, VIII) such that
Ψ_a(ζ) = Ψ̂(ζ)ζ^{aσ₃}S_j in sector j (ζ^a principal). Consequently, for |ζ| ≤ 3: |Ψ_a^{±1}(ζ)| ≤ C|ζ|^{−|a|} and
|Ψ_a(ζ)Me₂e₁ᵀM′Ψ_a(ζ)^{−1}| ≤ C|ζ|^{−2|a|} for constant M, M′.

*Proof.* In sector II, Vanlessen (4.27) with w := ζe^{−πi/2} reads
  Ψ = [[√πζ^{1/2}I_{a+½}(w), −π^{−1/2}ζ^{1/2}K_{a+½}(w)], [−i√πζ^{1/2}I_{a−½}(w), −iπ^{−1/2}ζ^{1/2}K_{a−½}(w)]]e^{−½aπiσ₃}.
By 10.27.4, K_ν = (π/2)(I_{−ν} − I_ν)/sin νπ, with sin((a + ½)π) = cos aπ and sin((a − ½)π) = −cos aπ. Substituting, the second
column equals κ·(first column) + c₂, κ := 1/(2cos aπ), c₂ := (√π/(2cos aπ))·(−ζ^{1/2}I_{−a−½}(w), iζ^{1/2}I_{−a+½}(w))ᵀ
(both rows give the same κ). By 10.25.2 and §10.25(ii), for arg ζ ∈ (−π/2, π) (which contains sector II),
ζ^{1/2}I_ν(w) = ζ^{ν+1/2}e^{−iπν/2}(½)^ν·Σ_k(−ζ²/4)^k/(k!Γ(ν + k + 1)) = ζ^{ν+1/2}E_ν(ζ), E_ν entire (1/Γ is entire). Hence the
first column is ζ^a·(√πζE_{a+½}, −i√πE_{a−½})ᵀ and c₂ = ζ^{−a}·(√π/(2cos aπ))(−E_{−a−½}, iζE_{−a+½})ᵀ, i.e.
  Ψ = Ψ̂(ζ)ζ^{aσ₃}S_II,  Ψ̂ := [ (√πζE_{a+½}, −i√πE_{a−½})ᵀ | (√π/(2cos aπ))(−E_{−a−½}, iζE_{−a+½})ᵀ ],
  S_II := [[1, κ], [0, 1]]e^{−½aπiσ₃}.
det S_II = 1 and det Ψ ≡ 1 (Vanlessen (4.53) proof: "det Ψλν ≡ 1"), so det Ψ̂ ≡ 1 on sector II, hence everywhere. Other
sectors: Ψ has constant jumps (KV (5.17)–(5.20)), so in each sector Ψ equals the analytic continuation of Ψ̂ζ^{aσ₃}S_II from
sector II times a constant matrix; continuing ζ^a principal through Γ₅ multiplies by e^{2πiaσ₃}, a constant. So
Ψ = Ψ̂ζ^{aσ₃}S_j. The bounds follow from Ψ̂^{±1} bounded on |ζ| ≤ 3 and |ζ^{±aσ₃}| ≤ |ζ|^{−|a|}; for the rank-one conjugate,
ζ^{aσ₃}Xζ^{−aσ₃} has entries X_{ij}ζ^{a(σ_i − σ_j)}, all O(|ζ|^{−2|a|}). ∎
NUMERICAL (`checks/check_r2p1_lw1.out` [4], a ∈ {−0.4, 0, 0.3, 0.45}): det Ψ = 1 and det Ψ̂ = 1 to 6 digits, Ψ̂ converges as
|ζ| = 10⁻¹ → 10⁻⁸, |Ψ||ζ|^{|a|} ∈ [0.55, 1.42] (consistent with KV (5.21)–(5.22)).

### 3.3 Lemma LW1₁ (lip mismatch) — NEW

Let θ_L := π/2 − π/12 and ε₁,n := ε₁(log n − 2 log 2; θ_L) (from (H_an₁)). **On the lips in U(0, δ)** (|arg(±z)| ∈
[π/4 − π/24, π/4 + π/24]),

  |D_ϱ(z)²/ϱ(z) − 1| ≤ C(|z| + ε₁,n),

with C independent of n. The q_n part does **not** decay as z → 0.

*Proof.* Representation: since (R(z)/π)∫_{−2}^{2}dx/(√(4 − x²)(z − x)) = 1 off [−2, 2],
  log D_q(z)² − log q(z) = (R(z)/π)∫_{−2}^{2}(log q(x) − log q(z))dx/(√(4 − x²)(z − x)).
For **even** q (all three factors are even on the band, and q(−z) = q(z) for their continuations), pair x and −x:
  = (R(z)/π)∫_0^2(log q(x) − log q(z))·(2z/(z² − x²))dx/√(4 − x²).   (∗)
On the lips |z² − x²| = |z − x||z + x| ≥ c(x + |z|)² (z is at angle ≥ π/4 − π/24 from both ±x), and |R(z)| ≤ 3 near 0.
- **q = h_W = e^L(4 − x²).** For x ∈ [0, 1], |log h(x) − log h(z)| ≤ C|x² − z²|, so that part of (∗) is ≤ C|z|; for x ∈ [1, 2],
  |log h(x) − log h(z)| ≤ C(1 + |log(4 − x²)|) and |2z/(z² − x²)| ≤ C|z|, integrable against dx/√(4 − x²). So
  |D_h²/h − 1| ≤ C|z|.
- **q = H_n².** |log H_n(x)²| ≤ Cx²/n on the band and |log H_n(z)²| ≤ C|z|²/n on the lips (Stirling in |ph t| ≤ 2π/3, DLMF 5.11.1
  and §5.11(ii), as RH₁(r) Lemma S with m = 0). So (∗) is ≤ (C/n)∫_0^2(x² + |z|²)|z|/((x + |z|)²√(4 − x²))dx ≤ C|z|/n.
- **q = q_n (the new factor).** Take z on an upper-right lip and x ∈ (0, 2]. Join z to x by the arc of radius |z| from arg z to 0,
  then the segment between |z| and x. Along it u = log n − Log ζ′² has Re u ≥ log n − 2 log 2 and |Im u| ≤ 2 arg z ≤ π − θ_L, and
  |du| = 2|dζ′|/|ζ′| integrates to 2 arg z + 2|log(x/|z|)|. Hence
    |log q_n(x) − log q_n(z)| ≤ ε₁,n(π/2 + π/12 + 2|log(x/|z|)|).
  Substituting x = |z|u in (∗) for x ≤ 1 and using |z² − x²| ≥ c|z|²(1 + u)²:
    |(∗)| ≤ Cε₁,n[∫_0^∞(1 + |log u|)(1 + u)^{−2}du + |z|∫_1^2(1 + log(2/|z|))dx/√(4 − x²)] ≤ C′ε₁,n.
  The other lips follow by z ↦ z̄ and z ↦ −z (q_n(−z) = q_n(z); for z at angle 3π/4 the arc runs from arg z to π, where
  Log z² runs from −π/2 to 0, so again |Im u| ≤ π/2 + π/12).
- Multiply: D_ϱ²/ϱ = (D_h²/h)(D_H²/H_n²)(D_q²/q_n). ∎

*Why the pairing matters.* Without (∗), the part x ∈ [1, 2] of the integral contributes ε₁,n·log(1/|z|)·|R(z)|, and here
R(z) → ±2i does not vanish at the band centre (at the hard edge, R ~ z^{1/2} killed it, ROUTE2 §3.3). The pairing replaces
1/(z − x) by 2z/(z² − x²) = O(|z|) for x ≥ 1. It uses that log q_n is even, i.e. the symmetry of the p = 1 problem.

*NUMERICAL* (`checks/check_r2p1_lw1.out`; Ψ₁ = exp √log(t + e), |z| = 10⁻¹⁴ … 0.3, rays arg z = π/4, π/6, π/3, 3π/4):
[1] sup|D_q²/q_n − 1| = 0.539, 0.425, 0.362, 0.304, 0.269 for n = 10², 10⁴, 10⁶, 10⁹, 10¹², against the ε₁-sample η_n = 0.264,
0.179, 0.142, 0.114, 0.098: ratio 2.04, 2.38, 2.55, 2.67, 2.76 — bounded (slowly approaching π, the pure-tilt value, as at
p > 1); at |z| = 10⁻¹⁴ the mismatch is still 0.19 … 0.16 (no decay in |z|); the mirror ray 3π/4 agrees with π/4 to all printed
digits. [2] band identity D₊D₋ = q to 10⁻¹⁰ (x = 0.5), 10⁻⁸ (x = 10⁻³). [3] |D_h²/h − 1|/|z| ∈ [0.90, 1.00];
n|D_H²/H_n² − 1| ≈ |z|/3 (n = 10², 10⁴; consistent with the bound C|z|/n).

### 3.4 The comparison problem

- P̃ := N_σ outside the discs; P̃₀ in U(0, δ); in U(±2, ε), P_± := (𝔇_∞/D_{h_W,∞})^{σ₃}A_±P^{(3/2)}ϱ₁^{−σ₃/2} with ϱ₁ := |x|^{2a}q_n (continued;
  analytic in U(±2, 2ε)), g := ϱ₁^{1/2}/(D_aD_q), A_± := Ng^{σ₃}N^{−1}, and P^{(3/2)} RH₁'s Airy parametrix (WLXZ §6.1 with weight
  wH_n). This is RH₁(r) §4 with q replaced by ϱ₁ and D by D_aD_q: g₊g₋ = 1 on the band, g is bounded with bounded inverse on
  U(±2, ε) (Lemma G(v) for D_a; |log D_q² − log q_n| ≤ Cε₁ near ±2 by the representation with log q_n analytic there), so A_±
  is analytic and bounded uniformly. P_± has V's jumps in U(±2, ε) exactly, and, since N_σ = (𝔇_∞/D_{h_W,∞})^{σ₃}N(D_aD_HD_q)^{−σ₃} (WLXZ's N = D_{h_W,∞}^{σ₃}N₀D_{h_W}^{−σ₃}, D_{h_W,∞} = e^{L/2};
  Rule R F4: the prefactor plays the role of RH₁(r)'s D_{Q,∞}^{σ₃}), P_±N_σ^{−1} = C^{σ₃}A_±(I + O(1/n))·(Nϱ₁^{−σ₃/2}(D_aD_qD_H)^{σ₃}N^{−1})·C^{−σ₃}
  = C^{σ₃}A_±(I + O(1/n))A_±^{−1}(ND_H^{σ₃}N^{−1})C^{−σ₃} = I + O(1/n) in the 𝔇_∞-frame (C := 𝔇_∞/D_{h_W,∞}; in the 𝔇_∞-frame
  the remaining conjugation is by the fixed constant D_{h_W,∞} = e^{L/2}, which is harmless) (D_H = 1 + O(1/n); RH₁ step 4 gives P^{(3/2)}N^{−1} = I + O(1/n)).
- 𝒵̃ solves the small-norm problem with jumps P̃₀N_σ^{−1} on ∂U(0, δ), P_±N_σ^{−1} on ∂U(±2, ε) (both I + O(1/n) in the
  𝔇_∞-frame), and N_σ·(V's jumps)·N_σ^{−1} outside the discs (band: **none**, since N_σ carries m_σ exactly; lips, saturated
  pieces, Σ^△, vertical segments: I + O(e^{−cn}·poly(n)), RH₁(r) Lemma W1(r) with the q_n^{±1} factors of §2). RH₁(r) §7's
  small-norm argument gives 𝒵̃′ := 𝔇_∞^{−σ₃}𝒵̃𝔇_∞^{σ₃} = I + O(1/n) uniformly, with first moment O(1/n). 𝒵̃ has **no jump inside
  U(0, δ)**: unlike RH₁(r)'s quotient construction (whose 𝒵 jumps by J_H = I + O(1/n) on the band and lips down to 0, Lemma M),
  the comparison problem carries no model mismatch at the band centre. This is what makes 𝒵̃ analytic in U(0, δ), as UR₁(b′),
  (d) require.
- Q̃ := 𝔇_∞^{−σ₃}𝒵̃P̃𝔇^{σ₃}. It solves Q̃₊ = Q̃₋ṽ on Σ with **ṽ = v except on the lips inside U(0, δ)**, where ṽ is P̃₀'s lip
  jump in the Q-frame: the (2,1) entry has D_ϱ² in place of ϱ, and the (J2) entries are dropped. Hence

    v − ṽ = δ_n e₂e₁ᵀ + (J2),  δ_n := ṽ₂₁(D_ϱ²/ϱ − 1),  (v − ṽ)ṽ^{−1} = δ_ne₂e₁ᵀ + (J2)ṽ^{−1},

  and ‖v − ṽ‖_{L^∞(Σ)} ≤ C(1/n + ε₁,n) =: Cε′_n → 0, using LW1₁, |ṽ₂₁| = |(D_a²/ω)e^{−2nφ}| ≤ Ce^{−cn|z|} on the lips
  (|D_a²/ω| bounded; Re φ_WLXZ = −Im f < 0 in ℂ₊, RH₁(r) §5), sup_r (r + ε₁,n)e^{−cnr} ≤ C(1/n + ε₁,n), and
  (J2) = O(e^{−cn/|z|²}poly(n, 1/|z|)) entrywise in the Q-frame (𝔇^{±2} costs |z|^{∓2a}·|z|^{−2η}).
- Near 0: Q̃ = A₀(z)·Φ(ζ)·Θ(z) with A₀ := 𝔇_∞^{−σ₃}𝒵̃Ẽ_n analytic in U(0, δ) with A₀^{±1} bounded uniformly in n (H1₁(i),
  𝒵̃′ = I + O(1/n)). (Rule R F10: D_ϱ has disappeared from this local form — Θ involves only D_a/W — so a possible |z|^{±O(ε₁)}
  behaviour of D_q at 0 never enters UR₁; it enters only the true Q, through the 3η margin of §4.2.)

---

## 4. Uniform resolvent and transfer (|a| < ½)

### 4.1 Lemma UR₁ — PROVED-mod-cite (as RH_ζ_close Lemma UR)

**Statement.** There are n₀, C such that for n ≥ n₀, 1 − C_ṽ is invertible on L²(Σ) and ‖(1 − C_ṽ)^{−1}‖ ≤ C.

*Proof.* RH_ζ_close Lemma UR (a)–(e) with these changes. Σ is the contour of RH₁(r) (finite union of C² arcs, long straight
pieces of length ≍ √n, Carleson constant uniform in n — the same fact RH₁(r) §7's small norm uses).
- **(a) area estimate / uniqueness.** |Q̃^{−1}| ≤ C_n|z|^{−|a|} near 0 (§3.4 and LF₁; Q̃^{−1} = adj Q̃), so
  ∬_{ε<|z|<2ε}|mQ̃^{−1}|dA ≤ Cε^{1/2}‖h‖·(∬_{|z|<2ε}|z|^{−2|a|}dA)^{1/2} = O(ε^{3/2−|a|}) = o(ε) **because |a| < ½**; every negative
  Laurent coefficient vanishes. Other vertices: as RH_ζ_close (bounded, or the Airy edge, which is α-free).
- **(b′) m := C(gQ̃₊^{−1})Q̃ ∈ ∂C(L²)** — ROUTE2 UR′(b′) verbatim with (−z)^{ασ₃/2} replaced by z^{aσ₃}: at z₀ = 0 and for fixed n,
  on U(0, r_n) (|nf| ≤ 3) LF₁ gives
    Q̃ = G(z)·z^{aσ₃}·Θ_j(z),  G := A₀(z)Ψ̂(nf(z))(nf(z)/z)^{aσ₃},  Θ_j := S_je^{−nφσ₃}(D_a/W)^{σ₃} (sector j),
  G analytic with analytic inverse (nf(z)/z is analytic and positive near 0: f(0) = 0, f′(0) = πψ(0) > 0; the cut of ζ^a is
  f^{−1}(Γ₅) = the negative band, that of z^a), Θ_j^{±1} bounded (|e^{±nφ}| bounded near 0 for fixed n). Then: the far part
  g₂ = g·1_{Σ∖U(0,r_n)} contributes ≤ C_n‖g‖|z|^{−|a|} (annulus integral O(ε^{2−|a|})); with G(s)^{−1}G(z) = I + (s − z)K_G(s, z),
  the K-term is ≤ C_n‖g‖|z|^{−|a|}(∫|s|^{−2|a|}|ds|)^{1/2} (|a| < ½); the core is T_{±a}(z) = z^{±a}∫h(s)s^{∓a}(s − z)^{−1}ds, and
  ROUTE2's three-range Cauchy–Schwarz bound (needs |±a| < ½) gives |T_{±a}(z)| ≤ C‖h‖dist(z, Σ)^{−1/2}, annulus integral O(ε^{3/2}).
  Total o(ε). No logarithmic case (LF₁ has no log for |a| < ½).
- **(c) partition** as RH_ζ_close: U(0, δ/2), U(±2, ε/2), the rest (Q̃ = 𝒵̃′·σ₃N₀σ₃ bounded with bounded inverse).
- **(d) band-centre piece.** On U(0, δ/2), Q̃ = A₀Φ(ζ)Θ with A₀ analytic and uniformly bounded, Θ a bounded multiplier. Write
  C(gQ̃^{−1})Q̃ = C(gΘ^{−1}Φ^{−1}A₀^{−1})A₀ΦΘ and A₀(s)^{−1}A₀(z) = I + (s − z)K(s, z) with K analytic and bounded uniformly
  (Cauchy estimates on U(0, 3δ/4)). Change variables ζ = nf(z) (conformal, f′ ≍ 1, n-free; the Cauchy kernel changes by a
  bounded smooth term and L² norms scale alike). Insert χ_{≤3}(ζ) + χ_{≥2}(ζ) = 1:
  - *large–large* (|ζ_s|, |ζ_z| ≥ 2): Φ^{±1} bounded (§3.1), so h ↦ C(hΦ^{−1})Φ is bounded by ‖C‖·sup|Φ|·sup|Φ^{−1}|; **no
    commutator and no Lemma W are needed here** (unlike the hard edge, Φ has no ζ^{σ₃/4} growth);
  - *small–small* (|ζ| ≤ 3): Φ = Ψ̂ζ^{aσ₃}S_je^{±iζσ₃}; the Ψ̂-commutator kernel is bounded analytic (n-free HS norm); the core
    h ↦ C(hζ^{−aσ₃})ζ^{aσ₃} is two copies of **RH_ζ_close Lemma W with exponents a and −a, |a| < ½**, on the star Γ₁, Γ₂, Γ₄, Γ₅,
    Γ₆, Γ₈ (Ψ's jump on Γ₃ ∪ Γ₇ is cancelled in Q̃);
  - *separated cross blocks*: Hilbert–Schmidt, ∬_{|ζ_s|≤2,|ζ_z|≥3}|ζ_s|^{−2|a|}|ζ_s − ζ_z|^{−2}|dζ_s||dζ_z| < ∞; the overlap annulus
    has Φ^{±1} bounded;
  - *K-term*: kernel Θ^{−1}Φ^{−1}(ζ_s)K(s, z)Φ(ζ_z)Θ with |Φ^{±1}(ζ)| ≤ C(1 + |ζ|^{−|a|}); HS² ≤ C(∫_0^δ(1 + (nr)^{−2|a|})dr)² ≤
    C(δ + n^{−2|a|}δ^{1−2|a|}/(1 − 2|a|))² = O(1).
  In particular |Q̃^{±1}| ≤ C_n|z|^{−|a|} near 0, which (a) used.
- **(e) soft edges ±2.** As ROUTE2 UR′(e) (= RH_ζ_close (e)): the band weight vanishes linearly at ±2 (h_W = e^L(4 − x²)), as
  in RH_px at b; Q̃ = (𝒵̃′A_±)·[RH₁'s WLXZ-§6.1 Airy parametrix in its 𝔇-frame]·(g^{−1}D_H)^{σ₃}, with the left factor analytic and
  bounded (commutator kernel bounded) and the right factor a bounded multiplier. ∎

### 4.2 Q in I + ∂C(L²)

C–D Theorem 4.4 (p = q = 2) needs Q±, Q̃±^{±1} ∈ I + ∂C(L²(Σ)). Σ is bounded and the jumps are bounded.
- **Q at 0** ((Y4)_r with Potter; fixed n). RH₁(r) §6 (a): masses μ_k ≍ k^{−r}Ψ₁(k) ≤ C_ηk^{−r+η} give Y₁₂, Y₂₂ = O(1 + |z|^{2a−2η}ℓ)
  in δ₀ ≤ |arg(±z)| ≤ π/2. (b) lens sectors: the residue argument with K₋ − K₊ = −2iU₁₁wFq̂θ′ = O(|s|^{2a}|q_n(s)|) =
  O(|s|^{2a−2η}) (Potter in the sector |arg s| < φ₀ < π/2, i.e. |Im u| < 2φ₀ < π). So R₁₂, R₂₂ = O(1 + |z|^{2a−2η}ℓ). The explicit
  factors between R and V are bounded for fixed n; the lens factor I + (e^{2nφ}/m_σ)e₂₁ adds |z|^{−2a−2η}·(col 2) to col 1. With
  |𝔇| ≍ |z|^a·|z|^{O(η)} (|log D_q(z)| ≤ A″ + 2η log(1/|z|) for fixed n), Q = V𝔇^{σ₃}·const has col 1 = O(|z|^{a} + |z|^{−a})·|z|^{−3η}
  and col 2 = O(|z|^{−a} + |z|^{a})|z|^{−3η}, i.e. **Q = O(|z|^{−|a|−3η}) ∈ L²_loc for η < (1 − 2|a|)/6**; det Q = 1 gives the same for
  Q^{−1}. Membership in I + ∂C(L²) then follows by the annulus argument of UR₁(b′) (∬_{annulus}|Q| = O(ε^{2−|a|−3η}) = o(ε)).
- **Q at ±2.** V = O(1)(z² − 4)^{(1/2−α_W)σ₃} = O(1)(z² − 4)^{−σ₃/2} (WLXZ (5.7)/(6.3) at α_W = 1, quoted) and |𝔇| ≍ |z ∓ 2|^{1/2}
  (D_{h_W} = e^{L/2}R/Φ; D_a, D_H, D_q bounded above and below near ±2), so Q = O(1).
- Corners and long pieces: bounded jumps, bounded solution (RH₁(r) Lemma W1(r)).
- **Q̃:** by UR₁(d)–(e) and 𝒵̃′ = I + O(1/n).

### 4.3 Theorem C₁ and Proposition D₁

**Theorem C₁.** For n ≥ n₁, ‖(1 − C_v)^{−1}‖ ≤ 2C. *Proof.* ‖C_v − C_ṽ‖ ≤ ‖C₋‖·‖v − ṽ‖_∞ ≤ C″ε′_n → 0 (§3.4), then C–D Theorem
4.7's Neumann argument (quoted) with UR₁. Only ε′_n → 0 is used: **no rate.** ∎

**Proposition D₁.** Q₁ − Q̃₁ = O(ε′_n/n) (entries, in the 𝔇_∞-frame), ε′_n = 1/n + ε₁,n.

*Proof.* C–D (4.14), via Theorem 4.4 as in RH_ζ_close §1.6: Q₁ − Q̃₁ = −(1/2πi)∫_Σh, h := μ(v − ṽ)ṽ^{−1}μ̃^{−1}, μ = Q₋ =
(1 − C_v)^{−1}I, μ̃ = Q̃₋. Only the lips in U(0, δ) contribute.
- *Main term* ∫δ_nμ̃e₂e₁ᵀμ̃^{−1}. With μ̃ = A₀Φ₋Θ₋ and Θ diagonal, Θe₂e₁ᵀΘ^{−1} = e^{±2nφ₊(0)}(W/D_a)²e₂e₁ᵀ, and
  δ_n·e^{±2nφ₊(0)}(W/D_a)² = c_j(D_ϱ²/ϱ − 1)e^{±2iζ} (c_j = KV's lip constant; −nφ = ±iζ ∓ nφ₊(0)). Since
  Φe₂e₁ᵀΦ^{−1} = e^{∓2iζ}Ψ_ae₂e₁ᵀΨ_a^{−1}, the integrand is c_j(D_ϱ²/ϱ − 1)·A₀Ψ_a e₂e₁ᵀΨ_a^{−1}A₀^{−1} (this is RH₁(r) Lemma M's
  structure with κ_n^{−1} − 1 replaced by D_ϱ²/ϱ − 1). On the lip rays: for |ζ| ≥ 2, |Ψ_ae₂e₁ᵀΨ_a^{−1}| = |e^{±2iζ}||Φe₂e₁ᵀΦ^{−1}| ≤
  Ce^{−√2|ζ|} (|e^{±2iζ}| = e^{−2|Im ζ|}, arg ζ ∈ {±π/4, ±3π/4}; Φ bounded both ways); for |ζ| ≤ 2 it is ≤ C|ζ|^{−2|a|} (LF₁). With
  LW1₁ and |dz| ≍ |dζ|/n:
    |main| ≤ C∫_0^δ(r + ε₁,n)(1 + (nr)^{−2|a|})e^{−cnr}dr ≤ C(n^{−2} + ε₁,n/n)∫_0^∞(1 + ρ^{−2|a|})(1 + ρ)e^{−cρ}dρ = O(ε′_n/n)
  (|a| < ½).
- *Correction term* ≤ ‖μ − μ̃‖₂‖δ_ne₁ᵀμ̃^{−1}‖₂ ≤ 2C‖δ_nμ̃e₂‖₂‖δ_ne₁ᵀμ̃^{−1}‖₂ (Theorem C₁); splitting e^{±2iζ} evenly between the two
  factors, each squared norm is ≤ C∫_0^δ(r + ε₁,n)²(1 + (nr)^{−2|a|})e^{−cnr}dr = O(ε′_n²/n). So the correction is O(ε′_n²/n).
- (J2) parts: |μ̃^{±1}| ≤ C(1 + (n|z|)^{−|a|}) times O(e^{−cn/|z|²}poly(n, 1/|z|)): O(n^{−K}). ∎

(Only Q₁ is needed at p = 1: a_n and b_n come from β_n by the fold, RH_p1.md §3.)

### 4.4 Theorem RII₁

**Theorem RII₁.** Let 1 < r < 2 (a = r − 3/2 ∈ (−½, ½)) and Ψ₁ = exp L₁(log t) with (H_an₁). For σ_{r,Ψ₁} = Σ_kk^{−r}Ψ₁(k)δ_{1/k}:

  nβ_n = 1 + O(1/n),  hence  nb_n = ½(1 + O(1/n)) = c(1)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

What is proved about the non-Fisher–Hartwig part: the lip mismatch moves Q₁ by O(ε′_n/n) relative to the comparison problem
Q̃ (Proposition D₁). Q̃ itself depends on Ψ₁ at order 1/n (through 𝒵̃, e.g. at the Airy discs where ϱ₁ ∋ q_n), so **no claim** is
made that β_n(w₁)/β_n(k^{−r}) − 1 = O(ε₁/n) (GAP-rate₁; tilt law §6).

*Proof.* Extraction (RH_p1.md §3, invariance): (U₁)₁₂(U₁)₂₁ = nβ_n, and the diagonal conjugations between U and Q (including
σ₃ and Y ↦ CYk^{σ₃} with k = 𝔇/𝔇_∞ = 1 + d₁/z + …) leave the product of the off-diagonal 1/z-coefficients unchanged; d₁ is
a linear functional of log ϱ and of log|x|^{2a} (the 1/z-coefficient of the Szegő integral), finite for each n because
log q_n ∈ L¹(dx/√(4 − x²)) (no uniformity in n is needed; cf. REVIEW_Plan48 F6). So nβ_n = (Q₁)₁₂(Q₁)₂₁. Outside the discs Q̃ = 𝒵̃′·σ₃N₀σ₃ (no 𝔇), so (Q̃₁)₁₂(Q̃₁)₂₁ = (N₀,₁)₁₂(N₀,₁)₂₁ + O(1/n) = 1 + O(1/n)
(RH_p1.md §3: (N₁)₁₂(N₁)₂₁ = 1), and Q̃₁ = O(1). Proposition D₁: (Q₁)₁₂(Q₁)₂₁ = (Q̃₁)₁₂(Q̃₁)₂₁ + O(ε′_n/n) = 1 + O(1/n). The fold
a_m = β_{2m−2} + β_{2m−1}, b_m² = β_{2m−1}β_{2m} preserves relative O(1/m) errors. ∎

*Cited (Rule C; quoted in `../CITATIONS.md`):* WLXZ v1 §§2–6 (via RH₁ and RH₁(r), incl. (5.7)/(6.3), (5.11), §6.1); KV §5 ((3.6),
(5.1)–(5.3), (5.6), (5.9), (5.10), (5.13), (5.17)–(5.20), (5.25)–(5.30), p. 19); Vanlessen §4 ((4.27), (4.43)–(4.46), (4.53));
C–D Theorem 4.4 and the arguments of Theorem 4.7, Proposition 4.9 (reproduced in RH_ζ_close §§1.4–1.6); DLMF 5.11.1/§5.11(ii),
10.25.2, 10.27.4, and DLMF 1.14.38–40, 5.5.3, 5.12.1/3 through Lemma W. *New here:* (H_an₁) and the strip analysis; the table
of §2; W̃ := W·D_ϱ with Ẽ_n = const·E^{KV} (H1₁); LF₁; LW1₁ with the even pairing; UR₁ (exponents ±a, large-ζ block
commutator-free); D₁'s Lemma-M-type bookkeeping.

### 4.5 Corollary B_{p=1}

**Corollary B_{p=1}.** Let 1 < r < 2 and Ψ > 0 slowly varying in sequence form (no boundedness, no D(γ) < ∞; e.g.
exp(√log k), exp((log k)^θ) for θ < 1, exp(√log k·sin log log k)). Then nb_n(k^{−r}Ψ) → ½ = c(1) and na_n(k^{−r}Ψ) → 1 = 2c(1)
(x_k = 1/k), with rate O(1/n + ρ(n/M₀)); rate O(1/n) if Ψ satisfies (H_an₁) itself (e.g. exp √log(k + e)).

*Proof.* RedA (§1) gives L₁ with (H_an₁) and the base change (iii) at p = 1; Theorem RII₁ gives the law for k^{−r}Ψ₁. ∎

---

## 5. Christoffel transfer: from 1 < r < 2 to all non-integer r (with rate), and the converse direction

*(Rule R F1, after merging master.)* Master's §3.21 (Plan 52, `ROUTE2_alpha.md`, REVIEWED) contains Lemma CT (the same identity
as CT₁(i) below, in monic coordinates g_n = −P_{n+1}(0)/P_n(0) = l_n², h_n = m_{n−1}²), Lemma CS + Theorem SH (= CT₁(ii) "⟹" with
Lemma D(a), G_n = c·x_n), Theorem SH-r (rates) and Corollary B_all (p > 1, every s > 1, with rate). Those are cited here; the
forward-direction proofs below are kept only as an alternative derivation. The content of this section that is **new relative
to §3.21** is the converse CT₁(ii) "⟸" with Lemma D(b), and its use for GAP-int (§7).

Index convention (0-based, as `jacobi_coeffs`): for a measure μ on [0, ∞) with infinite compact support, J = J(μ) has diagonal
a_n and off-diagonal J_{n,n+1} = b_{n+1} > 0 (n ≥ 0). The Law P with constant c > 0 at scale n^p means n^pa_n → 2c and
n^pb_n → c (an index shift does not matter since (n + 1)^p/n^p → 1).

**Lemma CT₁ (Cholesky form).** Let μ be a positive measure on [0, ∞) with infinite compact support. (i) The finite sections J_N are positive definite; J = LLᵀ with L lower bidiagonal, diagonal l_n > 0,
subdiagonal L_{n+1,n} = m_n > 0, given by l_0² = a_0, m_n = b_{n+1}/l_n, l_{n+1}² = a_{n+1} − m_n²; and **J(xμ) = LᵀL**, i.e.
a_n(xμ) = l_n² + m_n², b_{n+1}(xμ) = l_{n+1}m_n.
(ii) For every p > 0 and c > 0: μ satisfies the Law P (c, p) ⟺ xμ does. J(xμ) does not determine μ (μ + mδ₀ has the same xμ),
and the positive bidiagonal factorization J(xμ) = LᵀL is not unique (free parameter u_0 = l_0²); "⟸" covers every positive
factorization, in particular the Cholesky factor of J(μ).

*Proof.* (i) The eigenvalues of J_N are the zeros of the N-th orthogonal polynomial, which lie in the open convex hull of
supp μ ⊂ [0, ∞), i.e. in (0, max supp μ); so J_N > 0 and its Cholesky factor is the leading N × N block of L (the recursion is causal). Let
P = (p_0, p_1, …)ᵀ be the orthonormal polynomials of μ (positive leading coefficients), xP = JP = LLᵀP. Put q := L^{−1}P (L is
lower triangular with nonzero diagonal, so L^{−1} acts row-finitely and q_n = (p_n − m_{n−1}q_{n−1})/l_n is a polynomial of degree
n with leading coefficient lc(p_n)/l_n > 0). Then xq = L^{−1}xP = LᵀP, i.e. xq_n = l_np_n + m_np_{n+1}. For m ≥ n,
∫q_nq_m x dμ = ∫q_n(l_mp_m + m_mp_{m+1})dμ, which is 0 for m > n (deg q_n = n) and l_n·lc(q_n)/lc(p_n) = 1 for m = n. By symmetry
(q_n) is orthonormal for xμ, and xq = LᵀP = LᵀLq is its three-term recurrence; Jacobi matrices are determined by the
orthonormal polynomials, so J(xμ) = LᵀL.
(ii) "⟹" (= master's Lemma CS + Theorem SH, §3.21, with x_n = G_n/c; an alternative proof). Put x_n := n^pl_n²/c (n ≥ 1). From l_{n+1}² = a_{n+1} − b_{n+1}²/l_n²:
  x_{n+1} = A_{n+1} − B_n/x_n,  A_{n+1} := (n + 1)^pa_{n+1}/c → 2,  B_n := (n + 1)^pn^pb_{n+1}²/c² → 1,
and x_n > 0. Lemma D(a) gives x_n → 1. Then, since m_n² = b_{n+1}²/l_n² = (c/n^p)(n/(n + 1))^pB_n/x_n,
n^pa_n(xμ)/c = x_n + (n/(n + 1))^pB_n/x_n → 2 and n^{2p}b_{n+1}(xμ)²/c² = n^{2p}l_{n+1}²m_n²/c² = (n/(n + 1))^{2p}x_{n+1}B_n/x_n → 1.
"⟸". Given J(xμ) = LᵀL, put u_n := l_n², v_n := m_n² > 0: u_n + v_n = a_n(xμ) =: a′_n, u_{n+1}v_n = b_{n+1}(xμ)² =: b′²_{n+1}. With
z_n := n^pu_n/c: z_{n+1} = B′_n/(A′_n − z_n), A′_n := n^pa′_n/c → 2, B′_n := (n + 1)^pn^pb′²_{n+1}/c² → 1, and 0 < z_n < A′_n
(v_n > 0). Lemma D(b) gives z_n → 1, hence n^pv_n/c = A′_n − z_n → 1. Then a_n(μ) = l_n² + m_{n−1}² = u_n + v_{n−1} gives
n^pa_n(μ)/c = z_n + (n/(n − 1))^p(A′_{n−1} − z_{n−1}) → 2, and b_{n+1}(μ)² = m_n²l_n² = u_nv_n gives n^{2p}b_{n+1}(μ)²/c² =
z_n(A′_n − z_n) → 1. ∎

**Lemma D (parabolic dynamics).** Let A_n → 2 and B_n → 1.
- (a) If x_n > 0 and x_{n+1} = A_{n+1} − B_n/x_n for all n ≥ 1, then x_n → 1.
- (b) If 0 < z_n < A_n and z_{n+1} = B_n/(A_n − z_n) for all n ≥ 1, then z_n → 1.

*Proof.* (a) Fix δ ∈ (0, ⅕] and M with |A_n − 2|, |B_n − 1| ≤ ε := δ³/16 for n ≥ M. Let g(x) := 2 − 1/x; x − g(x) = (x − 1)²/x ≥ 0.
*No dip.* If x_m ≤ 1 − δ for some m ≥ M: x_{m+1} ≤ 2 + ε − (1 − ε)/x_m forces x_m ≥ (1 − ε)/(2 + ε) ≥ ⅓ (else x_{m+1} < 0), so
x_{m+1} ≤ g(x_m) + ε(1 + 1/x_m) ≤ x_m − δ² + 4ε ≤ x_m − δ²/2. Iterating, x decreases by ≥ δ²/2 per step while ≤ 1 − δ, so
eventually x < ⅓: contradiction. Hence x_n > 1 − δ for all n ≥ M. *No excess.* For n ≥ M, x_n ≥ ¾, so
x_{n+1} ≤ g(x_n) + 3ε. If x_n ≥ 1 + δ, then (x_n − 1)²/x_n ≥ δ²/(1 + δ) ≥ δ²/2 (increasing for x ≥ 1), so x_{n+1} ≤ x_n − δ²/4: x falls
below 1 + δ in finitely many steps. If x_n < 1 + δ, then x_{n+1} ≤ g(1 + δ) + 3ε = 1 + δ/(1 + δ) + 3ε < 1 + δ, because
δ − δ/(1 + δ) = δ²/(1 + δ) > 3ε. So 1 − δ < x_n < 1 + δ for all large n.
(b) Same δ, ε, M; h(z) := 1/(2 − z), h(z) − z = (1 − z)²/(2 − z) ≥ 0. For n ≥ M: z_{n+1} = B_n/(A_n − z_n) < A_{n+1} gives
A_n − z_n > B_n/A_{n+1} ≥ (1 − ε)/(2 + ε) ≥ 0.49, hence z_n < 1.52 and 2 − z_n ≥ 0.48 (Rule R F3); then
|z_{n+1} − h(z_n)| ≤ |B_n − 1|/(A_n − z_n) + |A_n − 2|/((A_n − z_n)(2 − z_n)) ≤ 2.1ε + 4.3ε ≤ 13ε ≤ 17ε. *No excess.* If z_m ≥ 1 + δ (m ≥ M): z_{m+1} ≥ z_m + (z_m − 1)²/(2 − z_m) − 17ε ≥ z_m + δ² − 17ε ≥
z_m + δ²/4 (17ε ≤ δ²·17δ/16 ≤ ¾δ² for δ ≤ ⅕), so z increases by ≥ δ²/4 per step and exceeds 1.52: contradiction. So z_n < 1 + δ
for n ≥ M. *No dip.* If z_n ≤ 1 − δ: (1 − z_n)²/(2 − z_n) ≥ δ²/2, so z_{n+1} ≥ z_n + δ²/2 − 17ε ≥ z_n + δ²/4 (δ ≤ 4/17), and z exceeds
1 − δ in finitely many steps; if z_n > 1 − δ: z_{n+1} ≥ h(1 − δ) − 17ε = 1 − δ + δ²/(1 + δ) − 17ε > 1 − δ. So 1 − δ < z_n < 1 + δ for all large n. ∎

*Remarks.*
- CT₁ needs nothing about the weights: Law P is invariant under w_k ↦ x_kw_k. Lemma D itself gives no rate; rates are transferred
  forward by master's Theorem SH-r (regular rates; O(1/n) ⇒ O(1/n)). NUMERICAL: x_n − 1 ≈ −1.05/n (`checks/check_r2p1_ct.out` [2]).
- The parabolic fixed point attracts on one side and repels on the other; positivity of the factor (l_n² > 0, resp. m_n² > 0)
  excludes the repelling side. If (A, B) admits no positive orbit the hypothesis is vacuous; such (A, B) never come from a measure.
  Numerically the reverse recursion (b) is unstable (relative error 10⁻³ by n = 800 at p = 2, [3]), which does not affect the proof.
- **Mass at 0 (Rule R F5).** By "⟸" (and "⟹"), Law P is unchanged by adding a mass mδ₀ (m ≥ 0) to a measure μ on [0, ∞) with
  infinite compact support: x(μ + mδ₀) = xμ. (Reviewer probe: law intact at n = 800 for m = 1, 100.)
- Novelty (Rule R F9): in master's chain-sequence form, "⟸" says that every parameter sequence of a chain sequence tending to ¼
  tends to ½ (not only the minimal one). Very likely KNOWN (Wall 1948; Chihara 1978, Ch. III) — not read, pointer only;
  novelty UNCHECKED. (i) is the classical Christoffel/Darboux ("LU ↦ UL") step; proved, not cited.

**Corollary B_{p=1}⁺ (Rule R F2).** Let r > 1, **r ∉ ℤ**, and Ψ sequence-form slowly varying (x_k = 1/k). Then
nb_n(k^{−r}Ψ) → ½ and na_n(k^{−r}Ψ) → 1, with rate **O(1/n)** if Ψ satisfies (H_an₁), and in general with rate O(r_n), r_n the
regular majorant (§3.21 / ROUTE2_alpha §4) of 1/n + ρ(⌈n/M₀⌉) (ρ is a tail supremum, hence non-increasing, and the sum is ≥ 1/n).
*Proof.* r₀ := r − ⌊r⌋ + 1 ∈ (1, 2); Theorem RII₁ resp. Corollary B_{p=1} gives the law for k^{−r₀}Ψ with that rate; ⌊r⌋ − 1
applications of master's Theorem SH-r (x_k·k^{−r′}Ψ(k) = k^{−r′−1}Ψ(k); each x^jσ is a positive measure on [0, 1] with infinite
support) give it for k^{−r}Ψ with rate O(r_n). ∎

**p > 1.** The statement "p > 1, every s > 1, Ψ sequence-form slowly varying" (called B_{p>1}⁺ in the first version of this
file) is master's **Corollary B_all** (Plan 52, §3.21, REVIEWED, with rate); it is not claimed as a result of Plan 50. The
closing of Plan 48's GAP-α for the law is Plan 52's.

(For p = 1 the base interval (1, 2) has length exactly p = 1 and is open, so integer shifts miss r ∈ {2, 3, …}: GAP-int, §7.)

---

## 6. Numerics (NUMERICAL)

`checks/check_r2p1_coeff.out` (p = 1, w = k^{−s}exp √log(k + e), which satisfies (H_an₁) directly; atoms k ≤ K plus an
Euler–Maclaurin Gauss–Legendre tail to t_end; long double RKPW; five truncations: K = 1, 2, 4·10⁵ with t_end = 10¹⁶, and
K = 2·10⁵ with t_end = 10¹⁴ or with a finer tail quadrature — the last two are independent of K-doubling, cf. REVIEW_RH1r F10):
- **s = 1.5 (a = 0; inside RII₁).** n(nb_n/c − 1) = −0.137, −0.142, −0.147, −0.152, −0.157 (n = 50 … 800), bounded, with
  spread over the five truncations ≤ 6.3·10⁻⁷ (≤ 1.9·10⁻⁶ for the a-column, ≤ 2·10⁻⁵ for the R column; Rule R F7); the pure power gives −0.249 … −0.250 = −(s − 1)/2. n(a_n/(2b_n) − 1) = 0.498 …
  0.500 (pure-power baseline p/2 = ½). Tilt ratio T = n(b_n(w)/b_n(k^{−s}) − 1)/ϑ_n = 0.471, 0.477, 0.480, 0.482, 0.484 (→ ½,
  slowly); drifting-order residual R = n(b_n(w)/b_n(k^{−(s−ϑ_n)}) − 1)/ϑ_n = −0.018 … −0.016: the drifting-exponent model accounts
  for ≈ 97% of the 1/n effect of Ψ.
- **s = 2 (a = ½; GAP-int, not covered).** n(nb_n/c − 1) = −0.382 … −0.407 (bounded; spread ≤ 1.3·10⁻⁸), E = 0.487 … 0.499,
  T = 0.472 … 0.484, R = −0.022 … −0.016: numerically the law holds with an O(1/n) rate at r = 2 too.
- The values of nB match the tilted baseline −(s − 1 − ϑ_n)/2 (−0.131 vs −0.137 at s = 1.5, n = 50; −0.381 vs −0.382 at s = 2):
  the (unproved) tilt law n b_n/c = 1 − (s − 1 − ϑ_n)/(2n) + o(ϑ_n/n), as at p = 2 (ROUTE2 §5). Within Route II this is the
  statement that D₁'s main term equals ϑ_n/(2n)·(…) + o(ϑ_n/n); not attempted (GAP-rate₁).
- `checks/check_r2p1_ct.out`: [1] J(xμ) = LᵀL to 3·10⁻¹⁶ (p = 1, s = 1.5 → 2.5) and 7·10⁻¹⁶ (p = 2, s = 4 → 6); [2] x_n = n^pl_n²/c =
  0.979, 0.989, 0.995, 0.997, 0.999 (n = 50 … 800, both cases); [4] p = 2, s = 6 (α_x = 3/2, outside RII, inside master's B_all):
  n(n²b_n/c − 1) = −2.31 … −2.40, bounded. (Rule R F8: [4] uses the same weights as the shifted measure of [1]/[2] and coincides
  with [2]'s Cholesky image to every printed digit; it checks boundedness, it is not independent evidence.)
- `checks/check_r2p1_lw1.out`: §3.2–3.3 above.

---

## 7. Stop conditions, gaps, Rule A

**Stop condition (i) at p = 1: RESOLVED-mod-cite** for 1 < r < 2. The quotient construction fails (§2, last paragraph; it would
need L₁ on Im u = ±π, the branch line of the model example). The C–D comparison with W̃ := W·D_ϱ never continues the weight
across iℝ, needs only the open strip, has a sup-norm lip mismatch O(|z| + ε₁,n) (LW1₁) without rate, and Proposition D₁ gains
1/n from the Bessel localization (|dz| = |dζ|/n; no conjugation cost at the band centre).

**Stop condition (ii): MOOT** (the exponent is the fixed a; no drifting order is used).

**OBSTRUCTION-a (the band-centre C–D frame at |a| ≥ ½; scoped to this frame).** For a ≥ ½ (r ≥ 2) Q̃ has entries ≍ |z|^{−a} at
the Bessel scale (KV (5.22)), not in L²_loc on a curve; C–D Theorem 4.4 with any (p, q), 1/p + 1/q = 1, would need Q̃ ∈ L^p and
Q̃^{−1} ∈ L^q, i.e. 2a < 1; Lemma W needs |a| < ½ (the power weight |s|^{∓2a} is A₂ on the star iff |a| < ½); and D₁'s integral
∫ρ^{−2a}dρ diverges at a = ½ only logarithmically. The loss relative to p > 1 is the symmetrization: the hard-edge order α_x =
a − ½ ranges over (−1, 0) only, half of ROUTE2's (−1, 1), because L²(|dy|) on the symmetric contour corresponds to
L²(|x|^{−1/2}|dx|) in x = y², not L²(|dx|). A weighted-L² version of C–D's comparison (power weight |z|^β, β ∈ (−1, 1)), or an
unsymmetrized p = 1 hard-edge analysis, might reach a < 1; neither is attempted (HEURISTIC).

**GAP-int.** p = 1, r ∈ {2, 3, 4, …}, Ψ with D(γ) = ∞. *(Plan 54 note, Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan54.md), fixes applied — REVIEWED: closed by Route II in the unsymmetrized x-frame at p = 1, 1 < r < 3 incl. r = 2 (α_x = 0) — `ROUTE2_xframe1.md`, PROOF.md §3.23; the "unsymmetrized p = 1 hard-edge analysis" below turned out to be available: RH_px's frame holds at p = 1 except its quotient hard-edge construction, which Route II does not use.)* (For D(γ) < ∞, T3-log already covers every r > 1.) Numerically the law
holds at r = 2 (§6).
*(Plan 53 note, Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan53.md), fixes applied — REVIEWED: GAP-int is closed by PROOF.md
§3.23 (Plan 54, `ROUTE2_xframe1.md`); an independent second proof by folding this symmetric problem to x = z² is PROOF.md §3.22,
`ROUTE2_bnd.md` (Theorem RII₁ᶠ, 1 < r < 3; Corollary B_{p=1}^{all,ᶠ}). OBSTRUCTION-a above stays as scoped to this frame.)*
- **Reduction (Rule R F6).** By CT₁(ii) "⟸" and "⟹" (or master's SH), for a fixed Ψ the law at one integer r₀ ≥ 2 is equivalent
  to the law at every integer r ≥ 2. So GAP-int is equivalent to **the law for k^{−2}Ψ** (a = ½, α_x = 0). This is the main use
  of the "⟸" direction.
- **Alternatives checked, all fail with the present tools:** the forward shift (CT₁/SH, step 1) preserves r mod 1 and starts
  from the open interval (1, 2); a base at a = ½ is obstructed (OBSTRUCTION-a: logarithmic divergence in UR₁(a), Lemma W, D₁);
  a Geronimus step (÷x) moves r down; a base at r = 1 exists as a finite measure only when ΣΨ(k)/k < ∞ and is a = −½, equally
  obstructed; Christoffel factors x + c do not change r; an unsymmetrized p = 1 hard-edge analysis at α_x = 0 (which ROUTE2
  handles for p > 1 with Lemma W′) is not available in this repo (HEURISTIC). *(Plan 54 note, 2026-10-14: superseded — that analysis is `ROUTE2_xframe1.md` (PROOF.md §3.23; Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan54.md), fixes applied — REVIEWED), which closes GAP-int.)*

**GAP-rate₁.** Only the 1/n coefficient (tilt law; CONJECTURE, NUMERICAL). The O(1/n) rate for non-integer r > 2 follows from
master's Theorem SH-r (Corollary B_{p=1}⁺; Rule R F2), and for s ≥ 1 + 2p (p > 1) it is master's Corollary B_all.

**Rule A (adversarial pass; logged in ../../LOG.md).**
- (a) Ψ₁ ≡ const: ε₁ = 0; LW1₁ reduces to the h_W and H_n parts (O(|z|)); RII₁ is then a second proof of RH₁(r) for 1 < r < 2
  (without Lemma S/Q_m and Lemma M). Consistent.
- (b) Ψ = k^ρ (regularly varying): L₁′ ≡ ρ, ε₁ ↛ 0; D_q²/q_n → e^{∓iπρ}-type constants at 0 (pure tilt), mismatch ≈ |e^{iπρ} − 1|,
  not small; the method correctly does not apply (the true answer is RH₁(r − ρ)).
- (c) a → ±½: Lemma W's constant, (∫(1 + ρ^{−2|a|})e^{−cρ}dρ) and the K-term HS bound blow up; finite for fixed |a| < ½.
- (d) The pairing (∗) is essential: for a non-even band factor the far part of the Szegő integral gives ε₁ log(1/|z|), unbounded.
  The only non-even candidate would be a weight asymmetric under x ↦ −x; the symmetrized measure is even by construction.
- (e) Strip: the example exp √log(t + e) is singular on Im u = ±π; every evaluation of q_n is at |Im u| ≤ π − 2θ_W
  (WLXZ regions) or ≤ π/2 + π/12 (lips, LW1₁ paths). D_ϱ is built from band values only.
- (f) Lemma CT₁: (i) checked to machine precision ([1]); finite-support μ (J finite) — the statement is about infinite J,
  excluded; μ with an atom at 0 — allowed (Rule R F5: the zeros of p_N lie in (0, max supp μ), so J_N > 0 on [0, ∞)); then
  x(μ + mδ₀) = xμ and the law is insensitive to mδ₀ (reviewer probe, m = 1, 100); (ii) the dynamics
  without positivity can converge to the repelling side (e.g. x_n ↦ 2 − 1/x_n from x₀ < 1 reaches negative values): positivity
  is used and is available. A Law P measure whose Christoffel transform fails the law would contradict (ii); none found.
- (g) Does UR₁ need ε₁? No: UR₁ is for the comparison problem; ε₁ enters only through ‖v − ṽ‖_∞ (C₁) and D₁.
- (h) Is 𝒵̃ analytic in U(0, δ)? Yes: ṽ = J_{P̃₀} exactly there (H1₁(ii)), so 𝒵̃ = Q̃-frame P̃-quotient has no jump in U(0, δ).
  This fails for RH₁(r)'s own Q_m/κ_n model (Lemma M jumps), which is why the comparison uses D_ϱ for the whole non-FH factor.
