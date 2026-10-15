# ROUTE2: Route II, stage 1 — the pointwise Law P for k^{−s}Ψ, Ψ slowly varying, p > 1, via an RH analysis that perturbs RH_px (Plan 48)

Status: **Rule R: ACCEPT WITH FIXES (../../review/REVIEW_Plan48.md; RedA ACCEPT, RII and B_{p>1} ACCEPT WITH FIXES), fixes
F1–F10 applied, re-check pending.** Novelty: UNCHECKED (no Rule L search).

Source: `research/program/outline_B_sv.md` §5 "Route II", work package WP4, stage 1. Template: `../px/RH_px.md`
(PROVED-mod-cite, REVIEWED). Closest precedent: `../zeta/RH_zeta_close.md` §1 (non-Fisher–Hartwig hard-edge factor via the
Conway–Deift comparison; REVIEWED). Numerics: `checks/check_r2_*.py/.out`.

**Labels (per step).**

| Item | Statement (short) | Label |
|---|---|---|
| §1 RedA | sequence-form slow variation ⇒ entire L₁ with L₁^{(j)} → 0 in every horizontal strip, Ψ/Ψ₁ → 1, and the law for vΨ ⟺ the law for vΨ₁ | PROVED (internal: L0, FV, FVa, Sat_p⁺; no BGT, no measurability) |
| §2 set-up | which steps of RH_px change for w = k^{−s}Ψ₁ (table) | PROVED (bookkeeping), each changed step proved in §3 |
| §3.3 LW1′ | lip mismatch \|D_w²/w₀ − c_±\| ≤ C(\|z\|^ν log(1/\|z\|) + ε₁(T_N)) | PROVED (given RH_px Lemma 3.4) |
| §3.2 local form | Ψ = Ψ̂ζ^{ασ₃/2}S (α ∉ ℤ), Ψ = Ψ̂[[1, κ log ζ], [0, 1]]S (α = 0) | PROVED-mod-cite (KMVV (6.23)–(6.25); DLMF 1.13.4, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2) |
| §4.2 Lemma W′ | log-commutator on a star of rays is L²-bounded | PROVED (DLMF 1.14.38–40) |
| Stop condition (i) | jump of e^{ρ_N} at the hard edge | **RESOLVED-mod-cite**: never placed on (−δ, 0); absorbed in D_w; the sup-norm mismatch is o(1) without rate and that suffices (C–D comparison) |
| Stop condition (ii) | KMVV Bessel construction uniform in a drifting order α_N | **MOOT (not needed)**: the order is the fixed α_x; uniformity in α_N is not established here and is not used |
| **Theorem RII** | p > 1, 1 < s < 1 + 2p, w₁ = k^{−s}exp(L₁(log k)) with (H_an): n^pb_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n) | **PROVED-mod-cite** (WLXZ v1 §§3–5, §6.1; KMVV §6; C–D Thm 4.4 + the arguments of C–D Thm 4.7 / Prop. 4.9 as reproduced in RH_ζ_close §1; DLMF 1.13.4, 1.14, 5.5.3, 5.12, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2; G2 μ*, B*(i)–(ii)); **Rule R ACCEPT WITH FIXES, fixes applied, re-check pending** (F1 closed for all \|α_x\| < 1 by UR′(b′)) |
| **Corollary B_{p>1}** | p > 1, 1 < s < 1 + 2p, Ψ sequence-form slowly varying (e.g. exp(√log k), D(γ) = ∞): n^pb_n → c(p), n^pa_n → 2c(p) | PROVED-mod-cite (RII + RedA); Rule R ACCEPT WITH FIXES, fixes applied, re-check pending |
| GAP-α | s ≥ 1 + 2p (α_x ≥ 1) | GAP (the L² frame of the comparison fails; §6) |
| GAP-rate | the 1/n coefficient (tilt law / Theorem B-rate) | GAP; CONJECTURE + NUMERICAL (§5) |

Notation: as in RH_px (t(z) = Nz^{−1/p}, θ = πt, W = 2iθ′w, band [0, b] with b := 4c(p), φ, φ̃, D̃, D, B, K, F, F̃, V,
N = D_{w,∞}^{σ₃}N₀D_w^{−σ₃}, f, M = [[1, i], [i, 1]]/√2) and RH_ζ_close §1 (Q-frame, ṽ, Q̃, 𝒵̃, Lemma W, Lemma UR, Theorem C,
Proposition D). α_x := (s − 1 − p)/p. ν := min(1/p, ½) (RH_px Lemma 3.2(ii)). log is principal unless said otherwise.

---

## 1. RedA: the smoothing reduction (PROVED)

Setting: x_k = k^{−p} (p > 0), v = k^{−s} (s > 1), Ψ > 0 on ℕ slowly varying in the sequence form of PROOF.md §3.8/§3.14:
δ_n(λ) → 0 for every λ ≥ 1. Nothing else is assumed (no measurability of an interpolant, no representation theorem;
Bingham–Goldie–Teugels is neither used nor cited). ε_n, A_η are those of Lemma L0 (§3.14).

**Construction.** Let L: ℝ → ℝ be the piecewise-linear interpolant of the points (log k, log Ψ(k)), k ≥ 1, extended by
the constant log Ψ(1) on (−∞, 0]. Let φ(z) := e^{−z²/2}/√(2π) and

  L₁(u) := ∫_ℝ L(y)φ(u − y)dy,  Ψ₁(t) := exp L₁(log t)  (t ∈ ℂ ∖ (−∞, 0]).

**Lemma RedA.**
- (o) |L(y)| ≤ A_η + η(y + log 2) for y ≥ 0 and every η > 0 (with A_η from L0(ii)); L₁ is entire.
- (i) L₁(log k) − log Ψ(k) → 0 (k → ∞); i.e. ψ := Ψ/Ψ₁ → 1 on ℕ.
- (ii) For every σ₀ ≥ 0 and j ≥ 0, sup_{|σ|≤σ₀}|L₁^{(j)}(τ + iσ) − δ_{j0}L₁(τ)| → 0 as τ → +∞ (for j = 0 this is
  L₁(τ + iσ) − L₁(τ) → 0; for j ≥ 1 it is L₁^{(j)} → 0). In particular, for every σ₀,
  ε₁(T) := sup{|L₁′(u)| : Re u ≥ T, |Im u| ≤ σ₀} → 0 (T → ∞), and |L₁(u)| ≤ A′_η + η Re u on {Re u ≥ 0, |Im u| ≤ σ₀}.
- (iii) (base change) For every p > 0 and s > 1: log b_n²(vΨ) − log b_n²(vΨ₁) → 0 and n^p(a_n(vΨ) − a_n(vΨ₁)) → 0.
  More precisely, with ρ(m) := sup_{k≥m}|log ψ(k)| (→ 0 by (i)) and M₀ = M₀(p) the head margin of T3-sv,
  |log b_n²(vΨ) − log b_n²(vΨ₁)| ≤ 2ρ(⌈n/M₀⌉) + O(n^{O(1)}e^{−2(n−1)}) and
  n^p|a_n(vΨ) − a_n(vΨ₁)| ≤ 6M₀^p·2^p ρ(⌈n/M₀⌉) + O(n^{O(1)}e^{−2(n−1)}).
  Hence the pointwise Law P (with any rate r_n) for vΨ₁ gives it for vΨ, with rate r_n + O(ρ(n/M₀)).

*Proof.* (o) For y ∈ [log k, log(k+1)], L(y) is a convex combination of log Ψ(k), log Ψ(k + 1), each bounded by
A_η + η log(k + 1) ≤ A_η + η(y + log 2) (L0(ii)). On y ≤ 0, L is constant. So |L(y)| ≤ A + η|y| + const on ℝ, and
for complex u = τ + iσ, |φ(u − y)| = φ(τ − y)e^{σ²/2}: the integral and all its u-derivatives converge locally uniformly,
so L₁ is entire (differentiation under the integral; dominated convergence).

*Local oscillation.* Put ω(τ) := sup{|L(y) − L(y′)| : y, y′ ∈ [τ − 1, τ + 1]}. For τ ≥ 1 + log 2, every y ∈ [τ − 1, τ + 1]
lies in some [log k, log(k + 1)] with k ∈ [e^{τ−1}/2, e^{τ+1}], so L(y), L(y′) are convex combinations of values
log Ψ(k′) with k′ in [m/λ, λm], m := ⌈e^τ⌉, λ := 2e²; hence ω(τ) ≤ 2δ_m(λ) → 0. Put Ω(τ) := sup_{τ′≥τ}ω(τ′) → 0.
Chaining in unit steps: for y ≥ τ, |L(y) − L(τ)| ≤ Ω(τ)(1 + |y − τ|); for y ∈ [τ/2, τ], |L(y) − L(τ)| ≤
Ω(τ/2)(1 + |y − τ|); for y < τ/2, |L(y) − L(τ)| ≤ 2A + 2η(|τ| + |y|) + const by (o).

(ii) The function c ↦ ∫φ(c − y)dy is entire and equals 1 on ℝ, hence ≡ 1; so ∫φ^{(j)}(c − y)dy = 0 for j ≥ 1 and all
c ∈ ℂ. Therefore L₁^{(j)}(τ + iσ) − δ_{j0}L(τ) = ∫(L(y) − L(τ))φ^{(j)}(τ + iσ − y)dy. With |φ^{(j)}(z + iσ)| ≤
P_j(|z| + σ₀)φ(z)e^{σ₀²/2} (P_j a polynomial), the three ranges of the chaining bound give
  |L₁^{(j)}(τ + iσ) − δ_{j0}L(τ)| ≤ e^{σ₀²/2}[Ω(τ/2)∫P_j(|z| + σ₀)(1 + |z|)φ(z)dz + C(1 + τ)∫_{|z|>τ/2}P_j(|z| + σ₀)(1 + |z|)φ(z)dz] → 0.
For j = 0 apply this at σ and at 0 and subtract. The Potter-type bound follows from (o) and the j = 0 case.

(i) L(log k) = log Ψ(k), so (ii) with j = 0, σ = 0 gives L₁(log k) − log Ψ(k) → 0.

(iii) This is the proof of Theorem T3-conv (§3.3) with base vΨ₁ in place of v, and the a-half of T3a/T3-all.
**Verification of the outline's claim that T3-conv's proof "never uses the base weight"** (done line by line):
T3-conv uses (1) the path w(t) = (base)·ψ^t with ψ bounded above and below — here ψ → 1, ψ > 0, so
G := sup|log ψ| < ∞ and w(t)/w(0) ∈ [e^{−G}, e^{G}]; smoothness in t and FV need only ‖log ψ‖_∞ < ∞ and finite moments
of the base (Σ vΨ₁ < ∞ by Potter); (2) centering — not needed here, since ψ → 1 means log ψ is already small at ∞;
(3) the head bound via Sat_p⁺, which uses **the base only through W(t)/w_k(t)**: T3-conv bounds it by the sandwich
(C/c)ζ(s)k^s; for the base vΨ₁ use instead W(t)/w_k(t) ≤ e^{2G}Σ_j j^{−s}Ψ₁(j)/(k^{−s}Ψ₁(k)) ≤ C_ηk^{s+η} (Potter for
Ψ₁ = Ψ/ψ from L0(ii)); (4) the pure-power law of v — used **only after** the difference bound, to convert it into the law.
So the claim holds, with the one modification in (3) (a polynomial lower bound for the base, which Potter supplies).
Hence, with k_ε replaced by ⌈n/M₀⌉ (so that Sat_p⁺ applies to k < n/M₀, as in B-cond step 2):
|log b_n²(vΨ) − log b_n²(vΨ₁)| ≤ sup_tΣ_k|log ψ(k)|(μ_n + μ_{n−1})^{(t)}(k) ≤ 2ρ(⌈n/M₀⌉) + G·n^{O(1)}e^{−2(n−1)}.
For a_n: FVa with f = log ψ (bounded), and the T3a step-1 bounds a_n^{(t)}, b_n^{(t)} ≤ 2M₀^p(n − 1)^{−p}, which use only
Sat_p⁺ (B-cond step 7), give n^p|ȧ_n| ≤ 3C_pρ(⌈n/M₀⌉) + 2Gn^p·(head mass), C_p := 4M₀^p2^p/2 as in T3-all step 2
(constants generous). ∎

*Remarks.*
- (RedA-1) Only sequence-form slow variation is used. The analyticity is produced by the Gaussian, not assumed.
- (RedA-2) The rate ρ(m) is the smoothing error |L − L * φ| at the nodes; for L ∈ C² with L″ → 0 it is
  ≲ sup_{|y−log m|≲√(log m)}|L″|/2 (Taylor). NUMERICAL (`check_r2_redA.out` [1]): for log Ψ = √log(k + e),
  e_n := max_{k≥n}|log Ψ(k) − L₁(log k)| = 8.3e−3, 2.4e−3, 1.1e−3, 8.6e−4 at n = 10², 10⁶, 10¹⁰, 10¹²; for the oscillating
  √(log k + 1)·sin log(log k + 1), 4.8e−2 → 1.2e−3.
- (RedA-3) NUMERICAL ([2]): ε₁(T) over the strip |Im u| ≤ π/2 (p = 2) equals sup_{τ≥T}|L′| to 3 digits (0.221, 0.159,
  0.112, 0.079 at T = 5, 10, 20, 40 for √log). ([3]) p = s = 2, with L₁ evaluated at every k ≤ K (grid convolution, max
  error vs direct quadrature 4e−9 / 2e−8; Rule R F7 — the first version used a hybrid weight): |β_n(vΨ)/β_n(vΨ₁) − 1| =
  4.8e−6 → 6.7e−7 (n = 100 → 800; √log), 6.8e−5 → 4.2e−6 (oscillating).

---

## 2. RH set-up for w₁ = k^{−s}Ψ₁, p > 1: what changes in RH_px

**Hypothesis (H_an)** (domain corrected per Rule R F4). For some c₀ > 0, Ψ₁(t) = exp L₁(log t), where L₁ is analytic on
Σ_p := {u : Re u ≥ −c₀, |Im u| ≤ π/p}, real on the real axis, bounded on {u ∈ Σ_p : Re u ≤ 0}, and
ε₁(T) := sup{|L₁′(u)| : u ∈ Σ_p, Re u ≥ T} → 0 as T → ∞. (The part Re u ∈ [−c₀, 0] is needed because RH_px's top closing
segment N^p + δ′ + i(0, ±δ) has t = N(N^p + δ′)^{−1/p} < 1, i.e. Re log t < 0; with δ′ fixed, Re log t ≥ −c₀ there. The
region Ω_∞ = {|z| > N^p + δ′}, where Re log t < −c₀ is possible, never uses w: V = C_∞QF^{σ₃} there has no weight in its
jumps.) (RedA's L₁ satisfies (H_an) for every c₀, with σ₀ = π/p: it is entire, and bounded on {−c₀ ≤ Re u ≤ 0,
|Im u| ≤ π/p} by continuity (L is constant on y ≤ 0). So does L₁(u) = √(log(e^u + e)), i.e. Ψ₁(t) = exp √log(t + e), and
L₁(u) = (log(e^u + e))^θ, θ < 1.) Consequences: |L₁(u)| ≤ A + η Re u on Σ_p (any η > 0, A = A(η)), so
|Ψ₁(t)|^{±1} ≤ C_η|t|^{η} for |arg t| ≤ π/p, |t| ≥ 1 (Potter in the sector).

Measure σ₁ := Σ_k k^{−s}Ψ₁(k)δ_{k^{−p}}. In RH_px §1 the only change is w(z) := N^pt(z)^{−s}Ψ₁(t(z)), analytic on
ℂ ∖ (−∞, 0] (|arg t| = |arg z|/p < π/p). Since Ψ₁(N) is a constant, and rescaling the measure does not change (a_n, b_n),
we may divide w by Ψ₁(N). Put

  q_N(z) := Ψ₁(Nz^{−1/p})/Ψ₁(N) = exp(L₁(log N − (log z)/p) − L₁(log N)),  z ∈ ℂ ∖ (−∞, 0].

**Table (RH_px step → change).**

| RH_px step | Uses the weight? | Change for w₁ |
|---|---|---|
| §1 rescaling, Lemma 1.1, transformations U → R | w in the lens factors (analytic continuation from the nodes) | w ↦ w·q_N, analytic on the slit plane by (H_an) (Im log t = −arg z/p ∈ (−π/p, π/p)). No new cut: (−∞, 0] is node-free and V never needs w there |
| Lemma 1.2 band weight | W = 2iθ′w | \|W(x)\| = (2π/p)N^{1+p−s}x^{α_x}q_N(x) (after dividing by Ψ₁(N)); α_x unchanged |
| §2 μ*, g, φ, φ̃, Lemmas 2.1–2.2 | no (μ* depends only on the nodes; the external field (1/N)log w → 0) | none. Validity a posteriori needs \|log w₁\| = o(N) on the contours: \|log q_N\| ≤ C log N by Potter |
| §3 D̃, D, B, K, F, F̃, Lemmas 3.1–3.5, normalization at ∞ (κ, C_∞) | no (Γ/Binet and node data only) | none |
| band jump, global parametrix | w₀ = W(b − x)/(D̃²B²) | **w₀ = C_N x^{α_x}(b − x)h_N(x)·q_N(x)**; D_w = (D_w of RH_px)·D_q, with D_q the Szegő function of q_N on [0, b] (outline step 3; finite since \|log q_N(x)\| ≤ ε₁(T_N)(\|log x\| + C)/p) |
| saturated region, Σ^△ lips, top end (§3, §4.3) | 1/w₀, w through e^{2Nφ̃}/w₀ and FF̃/W | extra factor q_N^{∓1} = poly(N) (Potter; on the top pieces Re log t ∈ [−c₀, C] and L₁ is bounded there by (H_an)), absorbed by e^{−cN} resp. N^{−pN} |
| §4.2 soft edge (WLXZ §6.1 Airy) | w̃ analytic nonvanishing in U(b, ε) | q_N is analytic in U(b, 2ε) with \|log q_N\| ≤ Cε₁(T_N); construction unchanged and uniform |
| §4.1 hard edge (KMVV left endpoint, W̃ = continuation of w₀^{1/2}) | yes | **replaced** (§3): the factor q_N(z) = z^{−ϑ_N/p}·e^{ρ_N(z)} (ϑ_N := L₁′(log N), ρ_N := log q_N + (ϑ_N/p)log z) is not Fisher–Hartwig, and its continuation does not glue with the KMVV W̃ |
| §5 (Y4)_x, identification, small norm, extraction | masses w_k; small norm | (Y4)_x with a Potter loss \|z\|^{−η}; small norm replaced by the C–D comparison (§4) |

**The hard-edge factor and what goes wrong with a direct parametrix (outline steps 4–5).** One has exactly
q_N(z) = exp(L₁(log N − (log z)/p) − L₁(log N)) = z^{−ϑ_N/p}e^{ρ_N(z)}, with |ρ_N′(z)| ≤ |z|^{−1}(ε₁ variation of L₁′)/p.
A KMVV-type parametrix needs W̃ with W̃₊W̃₋ = w₀ and W̃ continued across (−δ, 0) (RH_px Lemma 4.2). Continuing q_N^{1/2} from
the band to the left of 0 produces a jump across (−δ, 0) equal to exp(L₁(T − iπ/p) − L₁(T + iπ/p))-type ratios, i.e.
1 + O(ε₁(T_N)) with **no rate**. Conjugated by the Bessel model at the scale |z| ≍ N^{−2} this becomes O(N·ε₁) (the
mechanism of RH_ζ_close §1 "The problem"), not small. Absorbing z^{−ϑ_N/p} into a drifting Bessel order α_N := α_x − ϑ_N/p
removes the leading part of the jump but leaves e^{ρ_N}, whose jump is again O(ε₁) without rate. So the pre-registered
stop condition (i) is real **for a quotient (small-norm) argument**. §3–§4 avoid it.

---

## 3. The hard edge by a Conway–Deift comparison (resolution of stop condition (i))

The construction is RH_ζ_close §1 with Λ replaced by q_N and the Bessel order −½ replaced by α_x. The idea (C–D): never
continue the weight across (−δ, 0); build the Bessel parametrix with **W̃ := D_w**, the Szegő function of the full band
weight, which has no jump on (−δ, 0) and satisfies D_{w,+}D_{w,−} = w₀ exactly. The price is a lip mismatch which is small
in **sup norm** (Lemma LW1′), and sup-norm smallness without rate is exactly what C–D's resolvent comparison needs.

Restriction (needed in §4): **α_x ∈ (−1, 1)**, i.e. 1 < s < 1 + 2p.

### 3.1 Frame and comparison problem (transfer of RH_ζ_close §1.0, §1.2)

Q := D_∞^{−σ₃}VD_w^{σ₃} (D_∞ := D_w(∞)). Its jumps v are those of RH_ζ_close §1.0 with RH_px's contour (band [0, b]; lens
lips [[1, 0], [(D_w²/w₀)e^{2Nφ}, 1]] + the super-small (h1) entries of RH_px Lemma 4.3; saturated region and Σ^△/top
pieces; nothing on (−∞, 0)). Here w₀ on a lip means the analytic continuation of w₀ from the band into ℂ±, which exists
by (H_an) and RH_px.

**Lemma H1′ (comparison parametrix; RH_ζ_close Lemma H1 with order α_x).** In U(0, δ) put
  P̃₀ := (−1)^N·Ẽ_N·σ₃Ψ_α(N²f)σ₃·D_w^{−σ₃}·e^{Nφσ₃},  Ẽ_N := N·D_w^{σ₃}·M·f^{σ₃/4}(2πN)^{σ₃/2} = D_∞^{σ₃}N₀Mf^{σ₃/4}(2πN)^{σ₃/2},
with Ψ_α the KMVV matrix (6.23)–(6.25) of order α = α_x and f the (N-independent) conformal map of RH_px Lemma 4.1. Then
- (i) Ẽ_N is analytic in U(0, δ), det Ẽ_N = 1, and D_∞^{−σ₃}Ẽ_N(2πN)^{−σ₃/2} = N₀Mf^{σ₃/4} is bounded with bounded inverse,
  uniformly in N. **It does not involve the weight at all** (N·D_w^{σ₃} = D_∞^{σ₃}N₀), so the proof of RH_ζ_close H1(i)
  applies verbatim (band: RH_px Lemma 4.2(i) computation; (−δ, 0): N₀, f analytic; at 0: O(|z|^{−1/2}) singularity,
  removable by KMVV Prop. 6.5's argument).
- (ii) P̃₀ has exactly V's band jump, no jump on (−δ, 0), and on the lips the jump [[1, 0], [c_±e^{2Nφ}/D_w², 1]] with
  c_± := e^{∓iπα_x} (KMVV (6.16), (6.18) and (6.45): W̃² = e^{∓απi}w for KMVV's W̃; with W̃ = D_w the lip entry is
  c_±e^{2Nφ}/D_w²).
- (iii) D_∞^{−σ₃}(P̃₀N^{−1} − I)D_∞^{σ₃} = O(1/N) on ∂U(0, δ) (KMVV (6.28), α fixed).

The comparison solution P̃ (N outside the discs, P̃₀ in U(0, δ), RH_px's Airy P_r with weight w₀ in U(b, ε)), 𝒵̃ (small norm,
RH_px §5 verbatim: all jumps outside the discs are I + O(e^{−cN}poly(N)) or I + O(N^{−pN}poly(N)), with the q_N^{±1}
factors poly(N)), and Q̃ := D_∞^{−σ₃}𝒵̃P̃D_w^{σ₃} are as in RH_ζ_close §1.2. Q̃ has the jumps ṽ = v except on the lips inside
U(0, δ), where ṽ = [[1, 0], [c_±e^{2Nφ}, 1]] (Q-frame) and the (h1) entries are dropped. Geometry at b: as in RH_ζ_close
§1.2 (RH_px's outer lips stay outside U(b, ε)), so v = ṽ there.

### 3.2 Local form of Ψ_α (general α ∈ (−1, 1); extends RH_ζ_close "Local form" from α = −½)

Sources (quoted in `../CITATIONS.md`): KMVV (6.23) Ψ = [[I_α(2ζ^{1/2}), (i/π)K_α(2ζ^{1/2})], [2πiζ^{1/2}I′_α(2ζ^{1/2}),
−2ζ^{1/2}K′_α(2ζ^{1/2})]] in |arg ζ| < 2π/3; DLMF 10.25.2 I_ν(z) = (½z)^νΣ_k(¼z²)^k/(k!Γ(ν + k + 1)) (principal branch);
10.27.3–4; 10.31.2 (K₀); 1.13.4 and 10.28.2 (Wronskian). These are in `../CITATIONS.md` entries DLMF-2 and **DLMF-4**
(the latter renamed from "DLMF-3", which on master denotes Plan 46's entry; Rule R F2).
- **α ∉ ℤ.** By 10.25.2, I_{±α}(2ζ^{1/2}) = ζ^{±α/2}E_±(ζ) with E_± entire, and 2πiζ^{1/2}I′_{±α}(2ζ^{1/2}) = ζ^{±α/2}F_±(ζ)
  with F_± entire (term-by-term: ζ^{1/2}·d/dx[(x/2)^{±α+2k}] at x = 2ζ^{1/2} is (±α/2 + k)ζ^{±α/2+k}·const). By 10.27.4,
  K_α = (π/2)(I_{−α} − I_α)/sin(απ). So the second column of (6.23) is (i/(2 sin απ))·[(I_{−α}, 2πiζ^{1/2}I′_{−α}) −
  (I_α, 2πiζ^{1/2}I′_α)]ᵀ (check: (i/(2 sin απ))·2πi = −π/sin απ, and −2ζ^{1/2}K′_α = −πζ^{1/2}(I′_{−α} − I′_α)/sin απ).
  Hence in |arg ζ| < 2π/3
    **Ψ = Ψ̂(ζ)ζ^{ασ₃/2}S,** Ψ̂ := [[E₊, E₋], [F₊, F₋]] entire, S := [[1, −i/(2 sin απ)], [0, i/(2 sin απ)]],
  and det Ψ̂ = 1/det S = −2i sin απ ≠ 0, since det Ψ ≡ 1: by (6.23), det Ψ = 2ζ^{1/2}(K_αI′_α − K′_αI_α)(2ζ^{1/2}) =
  2ζ^{1/2}·𝒲{K_α, I_α}(2ζ^{1/2}) = 2ζ^{1/2}/(2ζ^{1/2}) = 1 (DLMF 1.13.4, 10.28.2, quoted in DLMF-4; Rule R F5). Only det Ψ̂ ≠ 0
  (Ψ̂^{−1} bounded on |ζ| ≤ 3) is used. In the other two sectors S is multiplied by the
  constant jump matrices (6.16), (6.18) (Ψ̂ζ^{ασ₃/2} is analytic off the cut of ζ^{α/2}, and Ψ's jumps are constant). At α = −½ this is
  RH_ζ_close's Ψ = Ψ̂ζ^{−σ₃/4}S.
- **α = 0.** By 10.31.2, K₀(x) = −(log(x/2) + γ)I₀(x) + (entire, even in x). With x = 2ζ^{1/2}: K₀(2ζ^{1/2}) =
  −½ log ζ·I₀(2ζ^{1/2}) + (entire in ζ) (the series Σ(¼x²)^k… is a power series in ζ). Same for −2ζ^{1/2}K₀′(2ζ^{1/2}).
  Hence **Ψ = Ψ̂(ζ)[[1, κ log ζ], [0, 1]]S** with Ψ̂ entire, κ = −i/(2π), S constant.
- Consequently, for |ζ| ≤ 3: |Ψ^{±1}(ζ)| ≤ C|ζ|^{−|α|/2} (α ≠ 0), ≤ C(1 + |log|ζ||) (α = 0); this agrees with KMVV
  (6.19)–(6.21)-type behaviour. And Ψe₂e₁ᵀΨ^{−1} = Ψ̂·[ζ^{ασ₃/2}(Se₂)(e₁ᵀS^{−1})ζ^{−ασ₃/2}]·Ψ̂^{−1}. With S upper-triangular,
  Se₂ = (s₁₂, s₂₂)ᵀ and e₁ᵀS^{−1} = (1, −s₁₂/s₂₂), so the bracket is the outer product of (s₁₂ζ^{α/2}, s₂₂ζ^{−α/2})ᵀ and
  (ζ^{−α/2}, −(s₁₂/s₂₂)ζ^{α/2}), with entries ∝ 1, ζ^{α}, ζ^{−α}: O(|ζ|^{−|α|}) for |ζ| ≤ 3 (α ≠ 0); O(log²|ζ|) for α = 0.

### 3.3 Lemma LW1′ (lip mismatch) — NEW, PROVED

Let T_N := log N − (1/p)log max(b, δ) and ε₁,N := ε₁(T_N) (from (H_an)). **On the lips in U(0, δ),**

  |D_w(z)²/w₀(z) − c_±| ≤ C(|z|^ν log(2/|z|) + ε₁,N),

with C independent of N. Hence ‖v − ṽ‖_{L^∞(Σ)} ≤ C(N^{−2ν}log N + ε₁,N) =: Cε′_N → 0, and v − ṽ = δ_N(z)e₂e₁ᵀ + (h1),
δ_N := (D_w²/w₀ − c_±)e^{2Nφ}, |e^{2Nφ}| ≤ e^{−cN|z|^{1/2}} on the lips.

*Proof.* w₀ = C_N·x^{α_x}·(b − x)h_N(x)·q_N(x), so D_w = C_N^{1/2}D_{x^α}D_{(b−x)h}D_q and D_w²/w₀ is the product of the
three ratios. Representation (RH_ζ_close LW1): for a positive weight q on [0, b] with log q integrable against
dx/√(x(b − x)), log D_q(z) − ½log q(z) = (R(z)/2π)∫_0^b(log q(x) − log q(z))dx/(√(x(b − x))(z − x)), R(z) = (z(z − b))^{1/2}
(from (R(z)/π)∫_0^bdx/(√(x(b − x))(z − x)) = 1, RH_px Lemma 3.4).
- **q = x^α.** Explicitly D_{x^α}(z)² = (bz/Φ(z))^α, Φ(z) := (z^{1/2} + (z − b)^{1/2})². Indeed Φ is analytic and nonzero
  off [0, b] (on (−∞, 0) both roots jump sign, Φ does not), Φ₊Φ₋ = (x^{1/2} + i(b − x)^{1/2})(x^{1/2} − i(b − x)^{1/2})·… = b²
  on the band, so (bx/Φ₊)(bx/Φ₋) = x²; bz/Φ → b/4 at ∞ and has a single-valued logarithm on ℂ̂ ∖ [0, b]. Near 0,
  Φ(z) = −b(1 + O(|z|^{1/2})), so D² = (−z)^α(1 + O(|z|^{1/2})) and D²/z^α = e^{∓iπα}(1 + O(|z|^{1/2})) = c_±(1 + O(|z|^{1/2}))
  in ℂ±. (NUMERICAL, `check_r2_lw1.out` [2]: |D²/z^α − e^{−iπα}| = 0.637|z|^{1/2} (α = −½), 0.424|z|^{1/2} (α = ⅓) on
  arg z = π/3, |z| = 10⁻⁸ … 10⁻².)
- **q = (b − x)h_N.** log h_N is Hölder-ν on [0, η₀] from each side of the cut, with N-uniform constants (RH_px Lemma 3.4
  "Consequence": (log D̃)′ = O(x^{1/p−1}/N), (log B)′ = O(x^{1/p−1})), and analytic on (0, b + ε); log(b − x) is analytic
  near 0. As in RH_ζ_close LW1 (q = k_N): |log D_q² − log q| ≤ C|z|^{1/2}∫_0^b|x − z|^{ν−1}x^{−1/2}(b − x)^{−1/2}dx + … ≤
  C|z|^ν log(2/|z|).
- **q = q_N (the new factor).** For x ∈ (0, b] and z on an upper lip in U(0, δ), join z to x by the arc of radius |z| from
  arg z to 0 followed by the segment [|z|, x] (or [x, |z|]). Along it u = log N − (log ζ′)/p has Re u ≥ T_N and
  |Im u| ≤ arg z/p < π/p, so u ∈ Σ_p, and |du| integrates to (arg z + |log(x/|z|)|)/p. Hence
    |log q_N(x) − log q_N(z)| ≤ ε₁,N·(π + |log(x/|z|)|)/p.
  On the lips |z − x| ≥ c(x + |z|) (the lips leave 0 at the angles ±π/3, RH_px Lemma 4.3; take δ small) and |R(z)| ≤ C|z|^{1/2}.
  Splitting [0, b/2] ∪ [b/2, b]:
    |log D_q(z)² − log q_N(z)| ≤ Cε₁,N[|z|^{1/2}∫_0^{b/2}(π + |log(x/|z|)|)x^{−1/2}(x + |z|)^{−1}dx + |z|^{1/2}log(2b/|z|)]
      ≤ Cε₁,N[∫_0^∞(π + |log u|)u^{−1/2}(1 + u)^{−1}du + 1] = C′ε₁,N.
  (Substitute x = |z|u. The integral is finite.) The lower lips are the mirror image.
- Multiply the three ratios. The (h1) entries are O(exp(−cN|z|^{−1/p})·|z|^{−C}) (RH_px Lemma 4.3; the q_N factors cost
  |z|^{−η}). Finally sup_{lip}(|z|^ν log(2/|z|) + ε₁,N)e^{−cN|z|^{1/2}} ≤ C(N^{−2ν}log N + ε₁,N). ∎

*NUMERICAL* (`check_r2_lw1.out` [1]; p = 2, Ψ₁ = exp √log(t + e), rays arg z = π/3, π/6, |z| = 10⁻¹⁴ … 0.3): the q_N-ratio
mismatch sup|D_q²/q_N − 1| = 0.285, 0.222, 0.188, 0.158, 0.139 for N = 10², 10⁴, 10⁶, 10⁹, 10¹², against ε₁,N/p-sample
η_N = 0.119, 0.084, 0.068, 0.056, 0.048: ratio 2.40, 2.63, 2.75, 2.84, 2.90 — bounded, slowly approaching π. The limit
π is the pure-tilt value: for q = z^{−ϑ/p}, D_q²/q = e^{±iπϑ/p}(1 + O(|z|^{1/2})), so |·−1| ≈ πϑ/p. That is precisely the
part a drifting Bessel order α_x − ϑ_N/p would remove (§5); it is O(ε₁,N), which is all §4 needs.

---

## 4. Uniform resolvent and transfer (the C–D argument for α_x ∈ (−1, 1))

### 4.1 Lemma UR′ (RH_ζ_close Lemma UR, general α_x ∈ (−1, 1)) — PROVED-mod-cite (as UR)

**Statement.** There are N₀, C such that for N ≥ N₀, 1 − C_ṽ is invertible on L²(Σ) with ‖(1 − C_ṽ)^{−1}‖ ≤ C.

*Proof.* RH_ζ_close's proof (a)–(e), with these changes only:
- (a) area estimate: |Q̃^{−1}| ≤ C_N|z − z₀|^{−|α|/2} (log for α = 0) near 0, so ∬_{ε<|z|<2ε}|mQ̃^{−1}|dA ≤
  Cε^{1/2}·ε^{1−|α|/2} and every negative Laurent coefficient is O(ε^{(1−|α|)/2}) → 0 **because |α| < 1**.
- (c), (e): unchanged (they do not involve α; the q_N-dependence enters only through D_w, which cancels in Q̃ inside
  U(0, δ) and outside the discs — Q̃ = 𝒵̃′N₀ there — and through the bounded multiplier (D_w/W_r)^{±σ₃} at b).
- (b) **does** involve α (Rule R F1): RH_ζ_close's crude bound |C(gQ̃₊^{−1})| ≲ ‖g‖|z|^{−1/4}d^{−1/2}, |Q̃| ≲ |z|^{−1/4} becomes
  |m| ≲ ‖g‖|z|^{−|α|}d^{−1/2} for general α, whose annulus integral ≍ ε^{3/2−|α|} is not o(ε) for |α| > ½. It is replaced by
  (b′) below, valid for every |α| < 1.
- (d) hard-edge piece: Φ(ζ) = σ₃Ψ_α(ζ)σ₃e^{Nφσ₃} with the local form of §3.2. For |ζ| ≥ 2 unchanged (KMVV (6.28)). For
  |ζ| ≤ 3 the core operator is h ↦ C(hζ^{−ασ₃/2})ζ^{ασ₃/2}, i.e. two copies of RH_ζ_close **Lemma W with a = ±α/2,
  |a| < ½ ⇔ |α| < 1**; for α = 0 the core is h ↦ C(hL^{−1})L, L = [[1, κ log ζ], [0, 1]], whose only non-trivial entry is
  the log-commutator g ↦ κC(g(log z − log s))-kernel, bounded by **Lemma W′** (§4.2). The Ψ̂- and A₀-commutator kernels are
  bounded analytic; the K-term Hilbert–Schmidt bounds become ∬|s|^{−|α|}|z|^{−|α|} < ∞ (|α| < 1) and, at |ζ| ≤ 2,
  HS² ≲ N²(N^{−2}∫_{|ζ|≤2}|ζ|^{−|α|})² = O(N^{−2}) (log² for α = 0).
- **(b′) m ∈ ∂C(L²) for every |α| < 1** (Rule R F1; the reviewer's sketch, written out). As in RH_ζ_close (b),
  m := C(gQ̃₊^{−1})Q̃ (g ∈ L²(Σ)) satisfies m₊ − m₋ṽ = g, and ‖m±‖ ≤ C‖g‖ by (c)–(e); what must be shown is m = C(m₊ − m₋).
  The difference F := m − C(m₊ − m₋) has no jump on Σ, is O(1/z) at ∞, and is analytic off the finitely many vertices of Σ.
  At a vertex z₀, if ∬_{ε<|z−z₀|<2ε}|F|dA = o(ε), then choosing r ∈ (ε, 2ε) with ∮_{|z−z₀|=r}|F||dz| ≤ ε^{−1}∬|F|dA gives
  |c_{−k}| ≤ (2π)^{−1}r^{k−1}∮|F||dz| = o(ε^{k−1}) → 0 for every Laurent coefficient c_{−k} (k ≥ 1), so z₀ is removable and
  F ≡ 0 by Liouville. Since C(m₊ − m₋) is the Cauchy transform of an L² function, its annulus integral is O(ε^{3/2})
  (RH_ζ_close (a)). So it suffices to show ∬_{ε<|z−z₀|<2ε}|m|dA = o(ε). Vertices away from 0: as in RH_ζ_close (b) (bounded
  Q̃^{±1}, or the Airy edge, where (e) is α-free). **At z₀ = 0** we work for fixed N (only membership in ∂C(L²) is needed;
  constants C_N may depend on N).
  - *Factorization.* On U(0, r_N) with r_N small (so that |N²f(z)| ≤ 3), Q̃ = G(z)·(−z)^{ασ₃/2}·Θ(z) for α ≠ 0, resp.
    Q̃ = G(z)·Λ(z)·Θ(z) with Λ(z) := [[1, κ log(−z)], [0, 1]] for α = 0. Here, from (d) and §3.2,
    G(z) := A₀(z)N^{σ₃/2}σ₃Ψ̂(N²f(z))·(N²f(z)/(−z))^{ασ₃/2} (resp. with the constant shift κ log(N²f(z)/(−z)) absorbed:
    Λ(ζ-variable) = Λ(z)·[[1, κ log(N²f/(−z))], [0, 1]], the second factor analytic), which is analytic with analytic inverse
    on U(0, r_N): N²f(z)/(−z) is analytic and positive near 0 (f(0) = 0, f′(0) < 0, Lemma 4.1), so its powers/logs are
    analytic, and the cut of ζ^{α/2} (ζ < 0 ⇔ the band z > 0) is that of (−z)^{α/2} (principal). Θ(z) := S_jσ₃e^{Nφσ₃}·
    (constant sign) on each sector j is bounded with bounded inverse (|e^{±Nφ}| bounded near 0, φ(0±) = ∓iπ).
  - *Splitting.* Write g = g₁ + g₂, g₁ := g·1_{U(0,r_N)}. The g₂-part: C(g₂Q̃₊^{−1}) is analytic and bounded on U(0, r_N/2),
    so its contribution to m is ≤ C_N‖g‖|Q̃(z)| ≤ C_N‖g‖|z|^{−|α|/2} (resp. log), with annulus integral O(ε^{2−|α|/2}) = o(ε).
  - For the g₁-part write G(s)^{−1}G(z) = I + (s − z)K_G(s, z), K_G analytic and bounded on U(0, r_N)², and
    h := g₁Θ^{−1} (‖h‖ ≤ C‖g‖). Then (α ≠ 0)
      C(g₁Q̃₊^{−1})(z)Q̃(z) = [C(h(−s)^{−ασ₃/2})(z)(−z)^{ασ₃/2} + (1/2πi)∫h(s)(−s)^{−ασ₃/2}K_G(s, z)ds·(−z)^{ασ₃/2}]Θ(z).
  - *K-term.* |∫h(−s)^{−ασ₃/2}K_G ds| ≤ C_N‖h‖·(∫_{Σ∩U}|s|^{−|α|}|ds|)^{1/2} ≤ C_N‖g‖ (|α| < 1), times |(−z)^{±α/2}| ≤ |z|^{−|α|/2}:
    ≤ C_N‖g‖|z|^{−|α|/2}, annulus integral O(ε^{2−|α|/2}) = o(ε).
  - *Core term.* Column by column it is T_a(z) := (−z)^a∫_{Σ∩U}h(s)(−s)^{−a}(s − z)^{−1}ds with a ∈ {α/2, −α/2}, |a| < ½.
    Put r := |z|, d := dist(z, Σ) ≤ r. By Cauchy–Schwarz |T_a(z)| ≤ C|z|^{Re a}‖h‖·I(z)^{1/2}, I(z) := ∫_Σ|s|^{−2Re a}|s − z|^{−2}|ds|
    (|(−s)^{−a}| ≤ C|s|^{−Re a}; here a is real). On each ray: |s| ≤ r/2 gives ≤ (4/r²)∫_0^{r/2}ρ^{−2a}dρ = C r^{−1−2a} (2a < 1);
    r/2 ≤ |s| ≤ 2r gives ≤ C r^{−2a}∫|s − z|^{−2}|ds| ≤ C r^{−2a}/d; |s| ≥ 2r gives ≤ 4∫_{2r}^∞ρ^{−2a−2}dρ = C r^{−1−2a}. Hence
    I(z) ≤ C r^{−2a}/d (d ≤ r) and **|T_a(z)| ≤ C‖h‖d^{−1/2}** — no power of |z| survives. (The reviewer's form
    ‖h‖_ηd^{−1/2} + C_η|z|^{−|a|} is the same estimate with the far part split off.)
  - *Area integral.* Σ ∩ U(0, r_N) is a finite union of C² arcs through 0 at distinct angles, so
    ∬_{ε<|z|<2ε}d(z)^{−1/2}dA ≤ C∫_ε^{2ε}ρ dρ∫_0^{2π}(ρ|θ − θ_j|)^{−1/2}dθ (sum over arcs) = O(ε^{3/2}). With Θ bounded, the
    core term contributes O(ε^{3/2}) = o(ε).
  - *α = 0.* Λ_s^{−1}Λ_z = I + κ(log(−z) − log(−s))e₁e₂ᵀ, so the core is C(h)(z) plus the column
    κ(2πi)^{−1}∫h_{·1}(s)(log(−z) − log(−s))(s − z)^{−1}ds. The first is ≤ C‖h‖d^{−1/2} (a = 0 above). For the second, the
    same three ranges with |log(−z) − log(−s)| ≤ C(1 + |log(|s|/r)|) give ∫(1 + |log(ρ/r)|)²|s − z|^{−2}|ds| ≤ C/d, so it is
    ≤ C‖h‖d^{−1/2}. The K-term carries Λ_s^{−1} = O(1 + |log|s||) ∈ L² and Λ_z = O(log(1/|z|)): ≤ C_N‖g‖log(1/|z|). The area
    integrals are O(ε^{3/2}) and O(ε²log(1/ε)), both o(ε).
  So ∬_{ε<|z|<2ε}|m|dA = O(ε^{3/2} + ε^{2−|α|/2}) = o(ε) for every |α| < 1 (and α = 0), and m ∈ ∂C(L²). ∎

**Outcome of F1:** UR′, hence Theorem C′, Proposition D′, Theorem RII and Corollary B_{p>1}, hold on the whole range
α_x ∈ (−1, 1), i.e. 1 < s < 1 + 2p. (Fallback not needed: no restriction to |α_x| ≤ ½.)

### 4.2 Lemma W′ (log-commutator on a star; needed only for α_x = 0) — PROVED

Let Σ_* be finitely many C² arcs leaving z₀ at distinct angles. Then the operator with kernel
(log(z − z₀) − log(s − z₀))/(s − z) (any fixed branches on each arc) is bounded on L²(Σ_* ∩ U(z₀, r)).

*Proof.* As Lemma W (RH_ζ_close §1.4): flatten each arc to its tangent ray; the error kernels are Hilbert–Schmidt (detail
below). On rays z = re^{iθ_i}, s = ρe^{iθ_j}, log z − log s = log(r/ρ) + i(θ_i − θ_j + 2πm). The constant part
times the Cauchy kernel is Lemma W with a = 0. The part log(r/ρ)/(ρe^{iθ_j} − re^{iθ_i}) is homogeneous of degree −1:
(Tf)(r) = ∫_0^∞k(ρ/r)f(ρ)dρ/r with k(u) = −log u/(ue^{iθ_j} − e^{iθ_i}). It has **no** singularity at u = 1 even when
i = j (log u/(u − 1) → 1), and |k(u)|u^{−1/2} is integrable on (0, ∞) (|log u|u^{−1/2} at 0, |log u|u^{−3/2} at ∞). So
the Mellin symbol is absolutely convergent and bounded on Re s = ½, and DLMF 1.14.38–40 (quoted) give boundedness on
L²(ℝ₊) with norm ≤ ∫_0^∞|k(u)|u^{−1/2}du. ∎
NUMERICAL (`check_r2_mellin.out`): same ray, M₀ = ∫u^{−1/2}|log u|/|u − 1|du = 9.8696 = π² (the symbol is π²/sin²(πs),
equal to π² at τ = 0; the closed form is not used); rays at angle differences π/3, 2π/3, π: sup_τ|symbol| ≤ 6.58, 3.29,
3.61 below the absolute bounds 8.33, 7.56, 7.33.

*The flattening step, in detail.* On a C² arc γ_j(ρ) = z₀ + ρe^{iθ_j}(1 + O(ρ)), log(γ_j(ρ) − z₀) = log ρ + iθ_j + O(ρ),
and γ_j′(ρ)/(γ_j(ρ) − γ_i(r)) − e^{iθ_j}/(ρe^{iθ_j} − re^{iθ_i}) = O(1) (RH_ζ_close Lemma W's flattening; the arclength factor
γ_j′(ρ)dρ must be included — without it, on a single arc the difference is only O(r/|ρ − r|); Rule R F10). For W′ this is
harmless either way, since the factor log(r/ρ) vanishes at ρ = r and makes the product O(1 + |log(r/ρ)|). The resulting error
kernels are O(1 + |log(r/ρ)|) on U(z₀, r)², which is Hilbert–Schmidt (∬log²(r/ρ)dρdr < ∞ on a bounded set).

### 4.3 Theorem C′ and Proposition D′

**(Q in L².)** RH_ζ_close §1.6's hypotheses for C–D Theorem 4.4 (p = q = 2) hold:
- *Q at 0* ((Y4)_x with Potter). Away from the band, Y₁₂, Y₂₂ = O(Σ_kk^{−s}Ψ₁(k)/max(|z|, k^{−p})) = O(1 + |z|^{α_x−η/p})
  (Ψ₁(k) ≤ C_ηk^{η}; the sum is RH_px's with s ↦ s − η). In the lens sectors, RH_px's 𝒦± argument verbatim: 𝒦₋ − 𝒦₊ =
  −2iU₁₁wθ′ = O(|s|^{α_x}|q_N(s)|) = O(|s|^{α_x−η/p}) (Potter in the sector, (H_an)), and 𝒦₋ is O(e^{−cN|s|^{−1/p}})·poly in
  the upper right quadrant. So Y₁₂, Y₂₂ = O(1 + |z|^{α_x−η/p}), and after the D_w^{σ₃} conjugation
  (|D_w| ≍ |z|^{α_x/2}|q_N|^{1/2}, by §3.3 and RH_px Lemma 3.4) Q = O(|z|^{−|α_x|/2−η}) ∈ L²_loc for η < (1 − |α_x|)/2.
- *Q at b*, corners, top: RH_ζ_close §1.6 / RH_px (bounded).
- *Q̃*: by UR′ (d)–(e) and 𝒵̃ = I + O(1/N).

**Theorem C′.** For N ≥ N₁, ‖(1 − C_v)^{−1}‖ ≤ 2C. *Proof.* ‖C_v − C_ṽ‖ ≤ ‖C₋‖·‖v − ṽ‖_∞ ≤ C″ε′_N → 0 (LW1′), then
C–D Theorem 4.7's Neumann argument (quoted) with UR′. ∎ **This is where "no rate" is harmless: only ε′_N → 0 is used.**

**Proposition D′.** Q₁ − Q̃₁ and Q₂ − Q̃₂ are O(ε′_N/N) in the D_∞-frame, ε′_N = N^{−2ν}log N + ε₁,N.

*Proof.* C–D (4.14)–(4.15) as in RH_ζ_close §1.6, h := μ(v − ṽ)ṽ^{−1}μ̃^{−1}, (v − ṽ)ṽ^{−1} = δ_Ne₂e₁ᵀ + (h1).
- Main term ∫δ_N μ̃e₂e₁ᵀμ̃^{−1}. In U(0, δ/2), μ̃e₂e₁ᵀμ̃^{−1}e^{2Nφ} = A₀N^{σ₃/2}[σ₃Ψe₂e₁ᵀΨ^{−1}σ₃]N^{−σ₃/2}A₀^{−1}.
  For |ζ| ≥ 2 (KMVV (6.28); α-independent): ≤ C(|z|^ν log + ε₁,N)|z|^{−1/2}e^{−cN|z|^{1/2}}, integral
  O(N^{−1−2ν}log N + ε₁,N/N). For |ζ| ≤ 2 (§3.2: entries O(|ζ|^{−|α|}), conjugation costs N): ≤ Cε′_N·N|ζ|^{−|α|} on
  |z| ≲ N^{−2}, integral ≤ Cε′_N·N·N^{−2}∫_0^2u^{−|α|}du = O(ε′_N/N) (|α| < 1; log² for α = 0).
- Correction term ≤ ‖μ − μ̃‖₂‖δ_Ne₁ᵀμ̃^{−1}‖₂ ≤ 2C‖δ_Nμ̃e₂‖₂‖δ_Ne₁ᵀμ̃^{−1}‖₂ = O(ε′_N²/N) by the same two-range bounds.
- (h1) parts and the extra factor z in Q₂ only improve the bounds. ∎

### 4.4 Theorem RII

**Theorem RII.** Let p > 1, 1 < s < 1 + 2p (α_x ∈ (−1, 1)), and Ψ₁ = exp L₁(log t) with (H_an). For
σ₁ = Σ_kk^{−s}Ψ₁(k)δ_{k^{−p}}:

  n^pb_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

What is proved about the non-Fisher–Hartwig part (Rule R F3): the lip mismatch moves Q₁, Q₂ by O(ε′_N/N) relative to the
comparison problem Q̃ (Proposition D′). Q̃ itself depends on Ψ₁ at order 1/N (e.g. through 𝒵̃ at the Airy edge, where w₀ ∋ q_N),
so **no claim** is made that b_n(w₁)/b_n(k^{−s}) − 1 = O(ε₁/n); that is GAP-rate (§5).

*Proof.* Extraction as RH_ζ_close §1.7 / RH_px §5 (invariance lemma): (Q₁)₁₂(Q₁)₂₁ = N^{2p}b_N² and a(Q) = N^pa_N. Here Q = D_∞^{−σ₃}VD_w^{σ₃}, and the invariance lemma applies to Y ↦ CYk^{σ₃} with k = D_w/D_∞ = 1 + d₁/z + …; it only needs d₁
finite for each N, which holds since d₁ is ∫log w₀·(bounded kernel) and |log q_N(x)| ≤ ε₁,N(|log x| + C)/p is integrable
against dx/√(x(b − x)) (Rule R F6: this is where D_w's 1/z-coefficient enters; no uniformity in N is needed). For
Q̃ = (D_∞^{−σ₃}𝒵̃D_∞^{σ₃})N₀ outside the discs (no D_w): (Q̃₁)₁₂(Q̃₁)₂₁ = c(p)²(1 + O(1/N)), a(Q̃) = 2c(p)(1 + O(1/N)), and Q̃₁, Q̃₂
are O(1) in this frame. Proposition D′ gives Q₁ − Q̃₁, Q₂ − Q̃₂ = O(ε′_N/N). ∎

*Cited (Rule C; all quoted in `../CITATIONS.md`):* WLXZ v1 §§3–5, §6.1; KMVV §6 ((6.16)–(6.28), (6.42)–(6.53), Prop. 6.5);
C–D Theorem 4.4 and the arguments of Theorem 4.7, Proposition 4.9 (reproduced in RH_ζ_close §§1.4–1.6); DLMF 1.14.38–40,
5.5.3, 5.12.1/3, 1.13.4, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2; G2 μ*, B*(i)–(ii). *New here:* RedA; the table of §2; Lemma
LW1′ (the q_N-part); the general-α local form; Lemma W′; UR′(b′); the α-bookkeeping in UR′ and D′.

### 4.5 Corollary B_{p>1} (Theorem B for p > 1, 1 < s < 1 + 2p)

**Corollary.** Let p > 1, 1 < s < 1 + 2p, and Ψ > 0 slowly varying in sequence form (no boundedness, no D(γ) < ∞; e.g.
exp(√log k), exp((log k)^θ) for θ < 1, exp(√log k·sin log log k)). Then n^pb_n(k^{−s}Ψ) → c(p) and n^pa_n(k^{−s}Ψ) → 2c(p),
with rate O(1/n + ρ(n/M₀)), ρ the RedA smoothing error. If Ψ itself satisfies (H_an) (e.g. exp √log(k + e)), the rate is
O(1/n).

*Proof.* RedA gives L₁ satisfying (H_an) and (iii); Theorem RII gives the law for vΨ₁ with O(1/n). ∎

This is the first case of Problem B with D(γ) = ∞ (PROOF.md §3.14 "D(γ) = ∞: no case of QL is proved"), for p > 1 and
s < 1 + 2p. It does not pass through QL.

---

## 5. Numerics for the law and the drifting-order (tilt) model (NUMERICAL, p = s = 2, α_x = −½)

`check_r2_coeff.out`, w = k^{−2}exp √log(k + e) (satisfies (H_an) directly), long double RKPW, K = 1.2·10⁵, 2.4·10⁵, 4.8·10⁵
(convergence corrected per Rule R F8):
- n(n^pb_n/c − 1) = −0.3869, −0.3938, −0.4000 (n = 100, 200, 400; K = 4.8·10⁵; K-converged to ~3 digits for n ≤ 200, to
  ~2·10⁻³ at n = 400), close to the tilted baseline −(s − 1 − ϑ_n)/2 = −0.387, −0.393, −0.399. At n = 800 the values
  −0.4285, −0.4111, −0.4065 (K = 1.2, 2.4, 4.8·10⁵) are **not** K-converged (second digit), so no match is claimed there;
  they remain bounded, consistent with O(1/n).
- n(a_n/(2b_n) − 1) = 0.9985, 0.9991, 0.9996 (n = 100, 200, 400; n = 800 not converged: 1.028, 1.007, 1.001) (pairing
  a[n]/(2√b2[n]) of `../../checks/check_fine.py`; pure-power e₁ = p/2 = 1).
- Tilt law: n(b_n(w)/b_n(v) − 1)/ϑ_n = 0.489, 0.491, 0.4925, 0.493 (n = 100 … 800; stable in K to ≤ 1.2·10⁻³) (→ ½).
- **Drifting-order model:** comparing with v_σ = k^{−σ}, σ = s − ϑ_n (hard-edge Bessel order α_x − ϑ_n/p),
  n(b_n(w)/b_n(v_σ) − 1)/ϑ_n = −0.0073, −0.0069, −0.0065, −0.0059: the drifting-order model accounts for ≈ 99% of the
  1/n effect of Ψ (T and R vary by ≤ 4·10⁻⁴ over the three K).
- These are consistent with Theorem RII (bounded n·deviation). The observed size ϑ_n/(2n) of the effect of Ψ relative to
  the pure power is the (unproved) tilt law, not Proposition D′ (which compares Q with Q̃, not with the pure power); they do
  not test the comparison problem Q̃ itself (as in RH_ζ_close §1.7, Rule R F6 there).

**Tilt law (CONJECTURE, unchanged from outline §1 "B-rate").** n^pb_n(w)/c = 1 − (s − 1 − ϑ_n)/(2n) + o(ϑ_n/n). Within
Route II this is the statement that the main term of Proposition D′ equals ϑ_N/(2N)·(…) + o(ϑ_N/N). Computing that main
term (as C–D compute theirs in (5.5)) needs the drifting-order parametrix (outline step 4) or an explicit evaluation of
∫δ_Nμ̃e₂e₁ᵀμ̃^{−1}; it is **not** attempted here (GAP-rate).

---

## 6. Stop-condition outcomes and remaining gaps

**(i) RESOLVED-mod-cite.** The e^{ρ_N} factor (indeed all of q_N) is put into D_w; nothing is continued across (−δ, 0), so
there is no jump there to control. The cost is a lip mismatch O(ε₁,N + N^{−2ν}log N) in sup norm, which by C–D's comparison
(Theorem C′) needs no rate, and whose effect on the coefficients is O(ε′_N/N) (Proposition D′) because the Bessel
localization supplies the factor 1/N. The pre-registered obstruction is real only for a quotient/small-norm argument with a
glued KMVV W̃ (§2, last paragraph).

**(ii) MOOT.** The Bessel order is the fixed α_x; no uniformity in a drifting order is used. (KMVV's construction uniform in
an order α_N varying in a compact subset of (−1, 1) is plausible via DLMF 10.40/10.41-type uniform asymptotics, but it was
not read or checked here; it becomes relevant only for GAP-rate.)

**GAP-α (s ≥ 1 + 2p).** For α_x ≥ 1 the comparison frame fails: Q̃'s second column is ≍ |z|^{−α_x/2} at the Bessel scale,
not in L²_loc, so C–D Theorem 4.4 (with any p, q, 1/p + 1/q = 1) and the area estimate of UR′(a) do not apply; Lemma W
needs |a| = α_x/2 < ½. A partial frame change Q·((z − a)/z)^{mσ₃} would fix the exponents at 0 for α_x ∈ (1, 3) but adds a
pole at a; not attempted. (α_x = 1 exactly is also excluded.) Precise open statement: Theorem RII for s ≥ 1 + 2p.

**Other remaining items.** WP5 (p = 1: RH₁(r); p < 1: RH_plt1b seam) is untouched. GAP-rate (§5). Rule R re-check of the
fixes (F1 in particular). Rule L (novelty) not done.

**Rule A (adversarial pass; logged in ../LOG.md).**
- (a) Ψ₁ ≡ const: ε₁ = 0, LW1′ reduces to the Hölder part, RII reduces to RH_px (consistent).
- (b) Ψ = k^{ρ} (regularly, not slowly, varying): L₁′ ≡ ρ, ε₁ ↛ 0, the mismatch is ≈ |e^{iπρ/p} − 1| (cf. §3.3 numerics),
  not small; the method correctly does not apply (the true answer is RH_px with s ↦ s − ρ). No false claim.
- (c) α_x → ±1: the constants of Lemma W (a → ±½) and of D′ (∫u^{−|α|}) blow up; for fixed s they are finite. Consistent
  with GAP-α.
- (d) log-type Ψ ((log k)^β): covered; RII gives O(1/n) for p > 1, s < 1 + 2p, consistent with `../../checks/check_log_weights.out`
  (deviation ≈ |β|/(n log n)).
- (e) Oscillating L (√τ sin log τ, D(γ) = ∞): (H_an) holds after RedA; RedA numerics [1]–[3] behave.
- (f) Is the strip width right? Lips and band need |Im log t| < π/p only (arg z ∈ (−π, π)); the negative axis is never used
  for the weight.
- (g) Does UR′ need ε₁ at all? No: UR′ is for the comparison problem; ε₁ enters only through ‖v − ṽ‖_∞ (Theorem C′) and D′.
