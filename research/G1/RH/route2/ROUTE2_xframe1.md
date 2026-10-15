# ROUTE2_xframe1: GAP-int closed — Route II in the unsymmetrized x-frame at p = 1 (Plan 54)

Status: **Rule R pending.** Novelty: UNCHECKED (no Rule L search).

Source: GAP-int of `ROUTE2_p1.md` §7 / PROOF.md §3.19 (review `../../review/REVIEW_Plan50.md`). Templates: `../px/RH_px.md`
(Theorem RH_p, p > 1, PROVED-mod-cite, REVIEWED) and `ROUTE2.md` (Theorem RII, p > 1, PROVED-mod-cite, REVIEWED, incl. UR′(b′)
for |α_x| < 1 and Lemma W′ for α_x = 0). Converse transfer: `ROUTE2_p1.md` §5 (Lemma CT₁, REVIEWED) and PROOF.md §3.21 (Theorems
SH, SH-r, REVIEWED). Numerics: `checks/check_x1_{frame,e2e,coeff}.py/.out`.

**Labels (per step).**

| Item | Statement (short) | Label |
|---|---|---|
| §1 Lemma X1 (reflection) | at p = 1, RH_px's D = D̃/(1 − e^{∓2iθ}) equals exp μ(−N/z) on ℂ ∖ [0, ∞): no jump on (−∞, 0), ℓ̂ ≡ 0, B ≡ 1 | PROVED-mod-cite (DLMF 5.5.1, 5.5.3; DLMF 5.11.1 for the bounds) |
| §1 Lemma X2 (why RH_px says p > 1) | the only steps of RH_px that fail at p = 1 are Lemma 1.1's uniformity near arg z = ±π for D̃, Lemma 3.2(v) (the (h2) jump of D̃B on (−δ, 0) is O(1): 1 − e^{−2πN sin(π/p)…} with sin π = 0) and its uses in the quotient hard-edge construction (Lemma 4.2(iii), Lemma 4.3 (h2)) | PROVED (bookkeeping, with the computation); OBSTRUCTION (precise) for the **quotient** construction at p = 1 |
| §2 transfer table | every other step of RH_px and ROUTE2 holds at p = 1 verbatim or with the stated replacement | PROVED (bookkeeping), each changed step proved here |
| §3 Lemma LW1-x1 | lip mismatch \|D_w²/w₀ − c_±\| ≤ C(\|z\|^{1/2}log(2/\|z\|) + ε₁,N) at p = 1 | PROVED (as ROUTE2 LW1′; ν = ½) |
| **Theorem RII_x1** | p = 1, **1 < r < 3** (α_x = r − 2 ∈ (−1, 1), incl. **r = 2**), (H_an^{x1}): nb_n = ½(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n) | **PROVED-mod-cite** (inherits RII's citations: WLXZ v1 §§3–5, §6.1; KMVV §6; C–D Thm 4.4 + arguments of 4.7/4.9; DLMF 1.13.4, 1.14, 5.5.1, 5.5.3, 5.11.1, 5.12, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2; G2 μ*, B*(i)–(ii)); Rule R pending |
| **Corollary B_{p=1}^{x}** | p = 1, 1 < r < 3, Ψ sequence-form slowly varying (incl. D(γ) = ∞) | PROVED-mod-cite (RII_x1 + RedA); Rule R pending |
| **Corollary GAP-int (closed)** | p = 1, **every integer r ≥ 2**, Ψ sequence-form slowly varying: the full pointwise Law P; rate O(1/n) under (H_an^{x1}) | PROVED-mod-cite (B_{p=1}^{x} at r = 2 + §3.21 SH-r); Rule R pending |
| **Corollary B_{p=1}^{all}** | p = 1, **every r > 1** (with B_{p=1}⁺ for non-integers) | PROVED-mod-cite; Rule R pending |
| §6 route (C) | symmetrization, Uvarov, Geronimus, rational factors, interpolation in r | OBSTRUCTION / not needed (scoped) |
| GAP-rate₁ | the 1/n coefficient (tilt law) | GAP (unchanged); CONJECTURE + NUMERICAL |

Notation: RH_px and ROUTE2 at **p = 1**: N the degree, nodes X_k = N/k (top X₁ = N), t(z) = N/z, θ = πt, w(z) = N t^{−r},
W = 2iθ′w, band [0, b], b = 4c(1) = 2 (c(1) = ½), α_x = (r − 1 − p)/p = r − 2, μ(u) := Ln Γ(u) − (u − ½)ln u + u − ½ln(2π)
(Binet's function, principal branches), D̃ = e^{−μ(t)}, D = D̃/(1 − e^{∓2iθ}) in ℂ±, B, K = (b − z)^{−1/2}, F = DBK, F̃ = D̃BK,
φ, φ̃, f, Ψ_α (KMVV (6.23)–(6.25)), D_w (Szegő function of the band weight w₀ on [0, b]), q_N(z) := Ψ₁(N/z)/Ψ₁(N).

---

## 0. Why the x-frame at p = 1 is the natural thing to try

In the symmetrized frame of RH₁(r) (WLXZ variable, nodes ±k^{−1/2}) the hard point is the band centre with Fisher–Hartwig
exponent a = r − 3/2; at r = 2, a = ½ and the C–D comparison fails (OBSTRUCTION-a: Q̃ ∉ L²_loc, the weight |s|^{∓2a} is not A₂).
In the x-frame (x = y²) the same point is a **hard edge** with Bessel order α_x = a − ½ = r − 2, and ROUTE2's comparison works for
|α_x| < 1. The loss is purely a frame effect: L²(|dy|) on the symmetric contour is L²(|x|^{−1/2}|dx|) in x. At r = 2, α_x = 0,
which ROUTE2 handles (KMVV local form with log ζ, Lemma W′). So the question is exactly: **does RH_px hold at p = 1?**

## 1. What in RH_px depends on p > 1, and what happens at p = 1

RH_px states p > 1 in Lemma 1.1: on ℂ ∖ (−∞, 0], arg t = −arg z/p ∈ (−π/p, π/p) ⊂ (−π, π), so Γ(t), Γ(t + 1) and Stirling's
series are pole-free and valid. Grepping RH_px and its review for every occurrence of p (done for this plan), the p-dependence
enters only through:

1. **Lemma 1.1.** At p = 1 the sector is the open |arg t| < π: Γ is still pole-free on the slit plane (its poles t = 0, −1, −2, …
   correspond to z ∈ (−∞, 0) ∪ {∞}, which is the cut), but the bound of DLMF 5.11.1 is uniform only in |ph t| ≤ π − δ, i.e. away
   from the negative z-axis. For p > 1 the whole slit plane maps into |ph t| ≤ π/p, a fixed sub-sector.
2. **D, B, ℓ̂ on (−∞, 0)** (Lemmas 3.1(iii), 3.2, 3.3(iii)): ℓ̂ = O(|x|^{1/p}/N), ℓ̂(−∞) = π/p − π, B ~ Cz^{½ − 1/(2p)}, D's
   monodromy e^{iπ/p}.
3. **Lemma 3.2(v)**: on (−δ, 0) the jump of D̃B is (1 − e^{−2iθ₊})/(1 − e^{2iθ₋}) = 1 + O(exp(−2πN sin(π/p)|x|^{−1/p})).
4. Exponents |z|^{−1/p}, Hölder ν = min(1/p, ½), the top node N^p, the length O(N^p) of the saturated region — all harmless at
   p = 1.
5. G2's μ*, B*(i)–(ii) — proved for **every p > 0** (G2 PROOF.md title and Theorem B*), so valid at p = 1 (c(1) = ½: I(1) = ½B(3/2, ½)
   = π/4, (4c)^{1} = π/(2I) = 2).

**Lemma X1 (reflection at p = 1).** Let p = 1. For z ∈ ℂ± put u := −t = −N/z. Then D(z) = D̃(z)/(1 − e^{∓2iθ}) = exp μ(u).
Consequently D extends analytically to ℂ ∖ [0, ∞) (no jump on (−∞, 0)), is real and positive on (−∞, 0) (so ℓ̂ ≡ 0 and the
Binet-cut scalar of RH_px Lemma 3.2 is B ≡ 1), |D − 1| ≤ C/|u| for |u| ≥ 1 in |ph u| ≤ π − δ, and D(z) ~ (−z/N)^{1/2}/√(2π) as
z → ∞.

*Proof.* Take z ∈ ℂ₊, so ph t ∈ (−π, 0) and t ∉ ℤ. By DLMF 5.5.3 (quoted: "Γ(z)Γ(1−z) = π/sin(πz), z ≠ 0, ±1, …"),
1/Γ(t) = Γ(1 − t)sin(πt)/π, and sin(πt)/(1 − e^{−2πit}) = e^{iπt}/(2i). Hence D = √(2π)t^{t−½}e^{−t}Γ(1 − t)e^{iπt}/(2πi). With
u = −t, ph u = ph t + π ∈ (0, π), so ln u = ln t + iπ (principal branches), and t^{t−½}e^{iπt} = exp((t − ½)ln t + iπt) =
exp((t − ½)(ln u − iπ) + iπt) = e^{iπ/2}u^{t−½} = i·u^{−u−½}. So D = u^{−u−½}e^{u}Γ(1 + u)/√(2π). By DLMF
5.5.1 ("Γ(z+1) = zΓ(z)") and the definition of μ, Γ(1 + u) = uΓ(u) = √(2π)u^{u+½}e^{−u}e^{μ(u)}, so D = e^{μ(u)}. For z ∈ ℂ₋ the
same computation with sin(πt)/(1 − e^{2πit}) = −e^{−iπt}/(2i) and ln u = ln t − iπ gives the same formula. μ is analytic on
ℂ ∖ (−∞, 0] (Γ has no zeros; its poles are at u ∈ −ℕ₀ on the cut), and u ∈ (−∞, 0] ⇔ z ∈ (0, ∞): so e^{μ(u)} is analytic on
ℂ ∖ [0, ∞). On (−∞, 0), u = N/|z| > 0 and μ(u) is real. DLMF 5.11.1 (quoted: "As z→∞ in the sector |ph z|≤π−δ, Ln Γ(z) ∼
(z−½)ln z−z+½ln(2π)+Σ B_{2k}/(2k(2k−1)z^{2k−1})") gives μ(u) = O(1/|u|). As z → ∞, u → 0 and μ(u) = −½ln u − ½ln(2π) + O(u). ∎

NUMERICAL (`check_x1_frame.out` [1]): D (WLXZ form) and exp μ(−N/z) agree to 1.1·10⁻²⁷ at nine points including z = −1.3 ± i10⁻²⁰,
−0.013 + i10⁻²², 25 + i and −10⁴ + i; ℓ̂ = 2 arg D₊ ≤ 10⁻²⁷ on (−∞, 0).

So at p = 1 items 1–2 are *better* than at p > 1 in Ω_∞: D needs no Binet cut, and the uniformity problem of Lemma 1.1 near
ph t = ±π concerns only D̃, which RH_px uses only in the band lens Ω_b, the saturated regions Ω^△, U(b, ε) and the top pieces
— all inside |arg z| ≤ π/3 + o(1) (§2), i.e. |ph t| ≤ π/3 + o(1).

**Lemma X2 (the genuine p = 1 failure, and its scope).** At p = 1, for x ∈ (−δ, 0), θ₊ = θ₋ = πN/x is real, and the jump of D̃B
(B ≡ 1) is (1 − e^{−2iθ})/(1 − e^{2iθ}) = −e^{−2iθ}: unimodular and **not** close to 1 (|J − 1| = 2|cos θ|). Moreover the analytic
continuation of the band factor h_N = const·e^{2μ(N/x)} across (−δ, 0) has double poles (as boundary values) at z = −N/m, m ∈ ℕ,
accumulating at 0 (1/Γ(t)² there). Hence RH_px's **quotient** hard-edge construction — W̃ = continuation of w₀^{1/2} to U(0, δ),
Lemma 3.2(v), Lemma 4.2(iii) (Ẽ_N analytic up to O(e^{−c′N})), Lemma 4.3 (the (h2) mismatch) — fails at p = 1 for the pure power
already. This is the precise structural reason for "p > 1" in RH_px §4.1: the factor sin(π/p) of Lemma 3.2(v) vanishes at p = 1
(the poles of Γ(t) reach the boundary of the slit plane). *Proof.* Direct substitution; the poles: 1/Γ(t) = 0 at t = −m.
NUMERICAL (`check_x1_frame.out` [2]): |J − 1| at x = −0.0123, −0.0517, −0.1043, N = 20: 10⁻⁵¹³ … 10⁻¹⁹¹ (p = 2), 10⁻⁸³⁹ … 10⁻¹²⁰
(p = 1.1), but 2.0, 1.77, 1.43 at p = 1; |e^{2μ(N/z)}| ≈ 10^{19}, 10^{17}, 10^{15} at z = −N/m + i10⁻¹²|z|, m = 40, 400, 4000.

**Scope.** ROUTE2 (Plan 48) never uses this construction: its hard edge is the Conway–Deift comparison with W̃ := D_w, the Szegő
function of the band weight, which is built from band values only and has no jump on (−δ, 0); and V itself has no jump on
(−∞, 0) (§2). ROUTE2 §6(i): "nothing is continued across (−δ, 0), so there is no jump there to control". So Lemma X2 obstructs
the pure-power quotient proof at p = 1, but not Route II. In particular the *pure power* at p = 1 in the x-frame is also
covered (Ψ₁ ≡ 1 in RII_x1; ε₁ = 0), giving an x-frame proof of RH₁(r) for 1 < r < 3 — not needed (RH₁(r) holds), but it confirms
the frame.

## 2. Transfer table: RH_px / ROUTE2 at p = 1

**Hypothesis (H_an^{x1}).** For some c₀ > 0, Ψ₁(t) = exp L₁(log t) with L₁ analytic on Σ_{x1} := {Re u ≥ −c₀, |Im u| ≤ π/2}, real
on ℝ, bounded on {u ∈ Σ_{x1} : Re u ≤ 0}, and ε₁(T) := sup{|L₁′(u)| : u ∈ Σ_{x1}, Re u ≥ T} → 0. (RedA's L₁ is entire and
satisfies it for every c₀ — ROUTE2 Lemma RedA (o)–(ii), stated for every strip; so does L₁(u) = √(log(e^u + e)), whose branch
points lie on Im u = ±π.) Potter: |Ψ₁(t)|^{±1} ≤ C_η|t|^η for |ph t| ≤ π/2, |t| ≥ 1.

Strip needed: u = log t = log N − Log z, Im u = −arg z. The weight (hence q_N) is evaluated only (a) on the band and in the band
lens / on its lips, which near 0 are KMVV's rays mapped by f (f′(0) < 0: ζ-rays at ±2π/3 ↦ z-rays at ±π/3) and elsewhere a thin
neighbourhood of (0, b) (RH_px Lemma 2.2 is a local statement near the band); (b) in Ω^△ and on the Σ^△ lips, a thin
neighbourhood of (b, N); (c) on the top segment N + δ′ + i(0, ±δ) (t ≈ 1, Re u ≥ −c₀); (d) in U(b, ε); (e) in (Y4)_x's lens
sectors |arg s| < φ₀ < π/3; (f) on the paths of LW1-x1 (|Im u| ≤ arg z). Ω_∞ never uses w (ROUTE2 (H_an) note). Choosing the
lips inside |arg z| ≤ π/3 + π/24, all evaluations satisfy |Im u| ≤ π/3 + π/24 < π/2. (For p > 1 ROUTE2 used the whole closed
strip |Im u| ≤ π/p for convenience; at p = 1 the closed strip |Im u| ≤ π would contain the branch points of the model example,
which is why the smaller strip is used.)

| RH_px / ROUTE2 step | At p = 1 |
|---|---|
| §1 rescaling, transformations U → R (WLXZ §3 template) | unchanged; nodes N/k ∈ (0, N]; Π = sin θ/θ′, θ′ = −πN/z² ≠ 0 |
| Lemma 1.1 | holds (open sector |ph t| < π); uniform Stirling for D̃ only where D̃ is used (|arg z| ≤ π/3 + π/24) |
| Lemma 1.2 | |W| = 2πN^{2−r}x^{r−2}, arg W = −π/2; α_x = r − 2 |
| §2 μ*, g, φ, φ̃, Lemmas 2.1–2.2 | unchanged (G2 μ*, B*(i)–(ii) for every p > 0; dμ*/dρ = I_{min(1,x/2)}(3/2, ½); ψ√x analytic at 0 since I_y(3/2, ½) = y^{3/2}·analytic and ρ = x^{−2}). NUMERICAL: Re g = log c + 1 = 0.30685… on the band to 12 digits |
| Lemma 3.1 (D) | replaced by Lemma X1 (stronger: no cut on (−∞, 0)) |
| Lemma 3.2 (B) | B ≡ 1; (i)–(iv) trivial; **(v) fails** (Lemma X2) — used only in RH_px §4.1, which ROUTE2 replaces |
| Lemma 3.3 | (i) trivial; (ii) unchanged; (iii) D ~ (−z/N)^{1/2}/√(2π), K ~ (−z)^{−1/2}: F → F_∞ = 1/√(2πN)·(phase), the monodromy count closes because 1/p = 1 ∈ ℤ (RH_px's own remark) |
| Lemma 3.4 + Consequence | log h_N = const + 2μ(N/x) is C^∞ on [0, η] (μ(N/x) has the asymptotic expansion x/(12N) − …); Hölder-ν with ν = ½ a fortiori |
| Lemma 3.5 | unchanged (g − log z ≍ z^{−1}; κ analytic at ∞). NUMERICAL: F e^{−N(g − log z)} at \|z\| = 10⁹ in two directions agree to 10⁻⁸ (`check_x1_e2e_*.out`, F_inf = 0.126157 = 1/√(20π) at N = 10) |
| band weight, global parametrix | w₀ = C_N x^{r−2}(b − x)h_N(x)q_N(x); N = D_{w,∞}^{σ₃}N₀D_w^{−σ₃} |
| §4.1 quotient Bessel construction | **not used** (fails, Lemma X2); replaced by ROUTE2 §3 (H1′, comparison with W̃ = D_w), which is p-free: Ẽ_N = D_∞^{σ₃}N₀Mf^{σ₃/4}(2πN)^{σ₃/2} does not involve the weight |
| Lemma 4.3 (h1) entries on the lips | D/D̃ − 1 = e^{∓2iθ}/(1 − e^{∓2iθ}), |e^{∓2iθ}| = exp(−2πN sin|arg z|/|z|), and e^{−2Nφ̃}: Re(iπ/z) = π sin(arg z)/|z| > 0 in ℂ₊: O(exp(−cN/|z|)) on the lips (rays at ±π/3) — the p = 1 instance of exp(−cN|z|^{−1/p}) |
| §4.2 Airy at b = 2 | unchanged (t ≈ N/2, D̃ analytic nonvanishing in U(b, ε)) |
| §4.3 top | |D| ≤ CN/δ′ (pole of Γ(1 + u) at u = −1 is the node X₁ = N); |J_V − I| ≤ poly(N)N^{−N} on pieces of length O(N) |
| §5 (Y4)_x | Σ_k k^{−r}Ψ₁(k)/max(|z|, 1/k) = O(1 + |z|^{α_x − η}ℓ(z)); lens sectors: 𝒦₋ = O(e^{−cN/|s|}) in the upper right quadrant (Im θ = −πN Im s/|s|² < 0) |
| ROUTE2 §1 RedA | every p > 0 (stated) |
| ROUTE2 §3 H1′, local form (§3.2, incl. α = 0 with log ζ), LW1′ | p-free except LW1′'s constants: §3 below |
| ROUTE2 §4 UR′ (incl. (b′) for every \|α\| < 1 and α = 0), Lemma W′, Q ∈ I + ∂C(L²), Theorem C′, Proposition D′, extraction | p-free (they use only: α_x ∈ (−1, 1), the local form, LW1′, the (h1) bounds, (Y4)_x, the small norm of 𝒵̃) |

NUMERICAL end-to-end validation of the frame (`check_x1_e2e.py`, adapted from RH_px's Rule R probe with D := e^{μ(−N/z)}, B ≡ 1;
true U from the discrete OPs: atoms k ≤ 4N exact plus an (N + 12)-point Gauss rule from exact Hurwitz-zeta tail moments; nine
points outside the discs incl. the negative axis): max|D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}| × N, for N = 10, 20, 40:

| r (α_x) | z = 1.2 + i | 0.5 + 0.8i | −1 + 0.5i | −1.5 + i0 | 2.5i | 4.5 + 1.5i | 3 − 1.2i | 15 + 8i | −6 − 3i |
|---|---|---|---|---|---|---|---|---|---|
| 1.5 (−½) | 0.216, 0.213, 0.212 | 0.154, 0.154, 0.153 | 0.091 | 0.080 | 0.090 | 0.110, 0.114, 0.116 | 0.211, 0.220, 0.225 | 0.020 | 0.034 |
| 2 (0) | 0.374, 0.376, 0.376 | 0.277, 0.282, 0.284 | 0.225, 0.234, 0.239 | 0.189, 0.197, 0.201 | 0.176, 0.183, 0.186 | 0.189, 0.200, 0.206 | 0.347, 0.369, 0.381 | 0.037, 0.039, 0.040 | 0.069, 0.072, 0.073 |
| 2.5 (½) | 0.572, 0.585, 0.591 | 0.424, 0.435, 0.441 | 0.238, 0.247, 0.251 | 0.207, 0.215, 0.219 | 0.227, 0.237, 0.242 | 0.250, 0.268, 0.278 | 0.468, 0.506, 0.526 | 0.048, 0.051, 0.052 | 0.085, 0.089, 0.091 |

N·error is stable: V = (I + O(1/N))N at p = 1, as at p > 1 (RH_px probe P1: 0.37–1.04 at p = 2). The probe also reproduces
Nb_N/c = 0.9531, 0.9758, 0.9877 (r = 2; = 1 − (r − 1)/(2N) + O(N^{−2})). |det V − 1| ≤ 3·10⁻³¹.
*Numerical note (Rule N):* the RH_px probe evaluates D̃ = √(2π)exp((t − ½)ln t − t − LnΓ(t)) at dps 30; at p = 1 the Szegő
quadrature reaches t ≈ N/x ≳ 10⁶⁰, where this difference cancels catastrophically. The first p = 1 run gave an N-independent O(1)
error, diagnosed as a constant diagonal conjugation (V ≈ CNC^{−1}, κ² ≈ 5.5 from the 1/z coefficients at z = −300 + 200i) caused
by a wrong D_{w,∞}; with μ(t) from the Stirling series for |t| > 10⁴ (`check_x1_e2e.py`, Plan 54 fix) it disappeared. The p > 1
outputs in `../px/checks/` were not re-run here (there t ≈ Nx^{−1/p}, a smaller range; their N·errors were already stable).

## 3. Lemma LW1-x1 (lip mismatch at p = 1)

Let T_N := log N − log b and ε₁,N := ε₁(T_N). On the lips in U(0, δ),

  |D_w(z)²/w₀(z) − c_±| ≤ C(|z|^{1/2}log(2/|z|) + ε₁,N),  c_± = e^{∓iπα_x}.

*Proof.* ROUTE2 LW1′ verbatim with p = 1: (i) the factor x^{α_x}: explicit, (−z)^{α_x}(1 + O(|z|^{1/2})); (ii) (b − x)h_N: log h_N
smooth on [0, η] with N-uniform derivative bounds (|(μ(N/x))′| = |μ′(N/x)|N/x² ≤ C/N), so the Hölder representation gives
C|z|^{1/2}log(2/|z|); (iii) q_N: the path from z to x (arc of radius |z| to the positive axis, then a segment) has Re u ≥ T_N and
|Im u| ≤ arg z ≤ π/3 + π/24 < π/2, so |log q_N(x) − log q_N(z)| ≤ ε₁,N(π + |log(x/|z|)|), and on the lips |z − x| ≥ c(x + |z|),
|R(z)| ≤ C|z|^{1/2} (R = (z(z − b))^{1/2}: the hard-edge square root kills the far part, unlike the band centre of ROUTE2_p1,
where the even pairing was needed); the integral is C′ε₁,N as in ROUTE2. ∎

NUMERICAL (`check_x1_frame.out` [3]–[4]; Ψ₁ = exp √log(t + e); rays π/3, π/6; |z| = 10⁻¹⁴ … 0.3): sup|D_q²/q_N − 1| = 0.510,
0.402, 0.349, 0.298, 0.265 for N = 10², 10⁴, 10⁶, 10⁹, 10¹², against the ε₁-sample η_N = 0.244, 0.171, 0.138, 0.112, 0.096:
ratio 2.09, 2.35, 2.53, 2.67, 2.75 — bounded, slowly approaching π (the pure-tilt value, as at p = 2 and in ROUTE2_p1); no decay
in |z|. h-part: |D_q²/q − 1|/|z|^{1/2} = 1.25 … 1.41 (N = 20, 200; |z| = 10⁻⁸ … 0.1), N-independent (the (b − x) factor).

## 4. Theorem RII_x1

**Theorem RII_x1.** Let p = 1, 1 < r < 3 (α_x = r − 2 ∈ (−1, 1)), and Ψ₁ = exp L₁(log t) with (H_an^{x1}). For
σ = Σ_k k^{−r}Ψ₁(k)δ_{1/k}:

  nb_n = ½(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

*Proof.* ROUTE2 §§3–4 (Theorem RII's proof) at p = 1, with RH_px's frame at p = 1 as in §2: Lemma X1 replaces Lemmas 3.1–3.2
(D = e^{μ(−N/z)}, B ≡ 1, F = DK; V has no jump on (−∞, 0)); the hard edge is H1′'s comparison parametrix of order α_x (no
continuation across (−δ, 0), so Lemma X2 does not enter); LW1-x1 replaces LW1′ (ν = ½, strip |Im u| ≤ π/2); UR′ (all |α_x| < 1;
for r = 2, α_x = 0, the log local form and Lemma W′), Q ∈ I + ∂C(L²) via (Y4)_x with Potter, Theorem C′ (only ε′_N → 0 is
used), Proposition D′ (Q₁ − Q̃₁, Q₂ − Q̃₂ = O(ε′_N/N), ε′_N = N^{−1}log N + ε₁,N), extraction ((Q₁)₁₂(Q₁)₂₁ = N²b_N², a(Q) = Na_N;
Q̃ gives c(1)² = ¼ and 2c(1) = 1 up to O(1/N)). ∎

As in RII, **no claim** that b_n(w₁)/b_n(k^{−r}) − 1 = O(ε₁/n) (GAP-rate₁).

**Corollary B_{p=1}^{x}.** p = 1, 1 < r < 3, Ψ sequence-form slowly varying (no boundedness, no D(γ) < ∞): nb_n → ½, na_n → 1,
rate O(1/n + ρ(n/M₀)); O(1/n) if Ψ satisfies (H_an^{x1}) (e.g. exp √log(k + e)). *Proof.* RedA (ROUTE2 §1; every p > 0, every
strip) + RII_x1. ∎

## 5. GAP-int closed, and p = 1 for every r > 1

**Corollary GAP-int (closed).** p = 1, r ∈ {2, 3, 4, …}, Ψ sequence-form slowly varying: the full pointwise Law P,
nb_n(k^{−r}Ψ) → ½, na_n(k^{−r}Ψ) → 1; rate O(1/n) under (H_an^{x1}), and in general O(r_n) with r_n the regular majorant of
1/n + ρ(⌈n/M₀⌉). *Proof.* r = 2: Corollary B_{p=1}^{x}. r ≥ 3: r − 2 applications of §3.21's Theorem SH-r (x·k^{−r′}Ψ(k)δ_{1/k} =
k^{−r′−1}Ψ(k)δ_{1/k}; each measure is positive on [0, 1] with infinite support). (Alternatively: CT₁ "⟸"/"⟹", ROUTE2_p1 §5 —
GAP-int ⟺ the law at r = 2.) ∎

**Corollary B_{p=1}^{all}.** p = 1, **every r > 1**, Ψ sequence-form slowly varying: the full pointwise Law P (non-integer r:
Corollary B_{p=1}⁺, §3.19; integer r: GAP-int above). With §3.20 (0 < p < 1) and §3.21 (p > 1): **for x_k = k^{−p}, every p > 0,
every s > 1 and every sequence-form slowly varying Ψ (incl. D(γ) = ∞), the full pointwise Law P holds** (PROVED-mod-cite; this
plan's part Rule R pending). Direct RH coverage at p = 1 is now 1 < r < 3 (x-frame); the symmetrized RII₁ (1 < r < 2) is
contained in it.

NUMERICAL (`check_x1_coeff.out`; long double RKPW; five truncations: K = 1, 2, 4·10⁵ with tail to 10¹⁶, K = 2·10⁵ with tail to
10¹⁴ and with a finer tail quadrature):
- Ψ = exp √log(k + e): r = 2: n(nb_n/c − 1) = −0.382, −0.389, −0.396, −0.402, −0.407 (n = 50 … 800; spread ≤ 1.3·10⁻⁸),
  n(a_n/(2b_n) − 1) = 0.487 … 0.499; r = 2.5: −0.628 … −0.656 (spread ≤ 5·10⁻¹⁰); r = 3 (via SH): −0.875 … −0.906; E → ½ in all.
  Bounded, consistent with O(1/n); each value sits ≈ +0.11 … +0.09 above the pure power −(r − 1)/2 (the tilt ϑ_n/2, GAP-rate₁).
- the oscillating Ψ = exp(√log(k + e)(1 + ½ sin log log(k + e))) (D(γ) = ∞; RedA not applied): r = 2: −0.315, −0.340, −0.362,
  −0.382, −0.398 (spread ≤ 4.2·10⁻⁹); r = 2.5: −0.562 … −0.648; r = 3: −0.810 … −0.898; E = 0.488 … 0.500. Bounded (the drift is
  the slowly varying tilt ϑ_n/2 → 0).

## 6. Route (C): other routes considered (scoped; none needed after §4)

- **Symmetrization σ(x) ↔ τ(y) on ±√x (Chihara).** This *is* the RH₁(r) frame: two-sided nodes ±k^{−1/2} (a two-sided p = ½
  problem), hard point at the band centre with a = r − 3/2 = ½ at r = 2. OBSTRUCTION-a (ROUTE2_p1 §7) applies; nothing new. The
  x-frame is the opposite move (desymmetrize), and it is what works.
- **Uvarov (mass at 0).** Law P is unchanged by mδ₀ (CT₁ remark F5) and r is unchanged: cannot move r.
- **Geronimus (÷x).** Moves r to r − 1: from r = 2 to k^{−1}Ψ, a finite measure only if ΣΨ(k)/k < ∞ (false for exp √log k), and
  α_x = −1 there, outside every frame (α_x > −1 is integrability at the hard edge).
- **Rational/polynomial factors** (x + c)/(x + d), c, d > 0: multiply w_k by a factor → c/d, i.e. a slowly varying change; r is
  unchanged. Christoffel by x is the only polynomial factor that moves r (by p = 1), and it preserves r mod 1 — hence GAP-int.
- **Interpolation / monotonicity in r.** Would need RII₁'s constants uniform as a ↑ ½; they blow up (Lemma W's A₂ constant;
  D₁'s ∫ρ^{−2|a|}); no monotonicity of b_n in the exponent is available. OBSTRUCTION (heuristic), moot.
- **Products** k^{−2}Ψ = k^{−3/2}Ψ·k^{−1/2}: x^{1/2} is not a polynomial; the only exact "half-step" is the symmetrization above.

## 7. Rule A (adversarial pass; logged in ../../LOG.md)

- (a) Ψ₁ ≡ 1: RII_x1 gives an x-frame proof of RH₁(r), 1 < r < 3; consistent with RH₁(r) and the e2e probe (N·err stable).
- (b) Is Lemma X1 consistent with RH_px's p > 1 limits? ℓ̂(−∞) = π/p − π → 0, B ~ z^{½ − 1/(2p)} → const, monodromy e^{iπ/p} → −1
  cancelled by K: all continuous at p = 1. Numerically exact to 10⁻²⁷.
- (c) Could D̃ be needed near the negative axis at p = 1? Only in RH_px §4.1 (quotient hard edge), not in ROUTE2; checked step by
  step in §2 (Ω_∞ uses D; the lips' diagonal entries D/D̃ − 1 are evaluated at |arg z| ≈ π/3, where |e^{∓2iθ}| = e^{−√3πN/|z|}).
- (d) Strip: exp √log(t + e) is singular at Im u = ±π (z ∈ (−∞, 0) ⇔ |Im u| = π); all evaluations at |Im u| ≤ π/3 + π/24.
  D_w uses band values only. The model example satisfies (H_an^{x1}) directly.
- (e) α_x = 0 exactly (r = 2): the local form has log ζ (ROUTE2 §3.2), Lemma W′ handles it; UR′(b′)'s α = 0 case; D′ with log².
  These were REVIEWED in Plan 48 for p > 1 and do not involve p.
- (f) Ψ = k^ρ: ε₁ ↛ 0, LW1-x1's mismatch ≈ |e^{iπρ} − 1|; the method correctly does not apply.
- (g) Is the conclusion too strong? It agrees with every numerical test (§5; `check_r2p1_coeff.out` s = 2) and with the
  converse CT₁: if the law failed at r = 2 it would fail at every integer r ≥ 2 (CT₁ ⟸), contradicting nothing proved before.
- (h) Top end: t ≈ 1 there; Re u ∈ [−c₀, C]; L₁ bounded by (H_an^{x1}); q_N^{±1} = poly(N) absorbed by N^{−N}.

**Open:** GAP-rate₁ (tilt law); the RH analysis at α_x ≥ 1 itself (not needed); Rule R for this file.
