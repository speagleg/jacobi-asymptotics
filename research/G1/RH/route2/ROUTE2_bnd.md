# ROUTE2_bnd: the boundary a = ½ at p = 1 by folding the symmetric problem — a second proof of §3.23's p = 1 result (Plan 53)

Status: **Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan53.md), fixes applied — REVIEWED** (F1–F11 applied after merging master, which contains Plan 54, PROOF.md §3.23). Novelty: UNCHECKED (no Rule
L search).

*(Plan 55 note, 2026-10-15: the conclusions of Theorem RII₁ᶠ and Corollary B_{p=1}^{all,ᶠ} (rate clause) also hold under (A_ϑ) for any ϑ > 0 instead of (H_an₁), because they coincide with those of RII_x1 / B_{p=1}^{all} (ROUTE2_xframe1.md), whose hypothesis can be so weakened; the fold proof below was not re-examined for thin strips; verified on Paper 2's consolidated write-up (papers/paper2), see ../../PROOF.md §3.24 (Theorem AS, PROVED-mod-cite, proof of record papers/paper2 rev. 3 + §3.24 audit; Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan55.md), fixes applied — REVIEWED). This file is unchanged and proves its results as stated.)*

**Framing (Rule R F1).** GAP-int is closed by Plan 54 (PROOF.md §3.23, `ROUTE2_xframe1.md`, REVIEWED: Route II in the
unsymmetrized x-frame). This file is an independent **second proof** of the (a_m, b_m) part of §3.23's Theorem RII_x1 on 1 < r < 3
and of its Corollary B_{p=1}^{all}, through a different global frame (WLXZ's symmetric problem, folded); see §3.8 "Relation to
§3.23" for what is shared.

Source: GAP-int and OBSTRUCTION-a of `ROUTE2_p1.md` §7 (Plan 50, REVIEWED; `../../review/REVIEW_Plan50.md`) and PROOF.md §3.19.
Templates: `ROUTE2.md` §§3–4 (Plan 48, REVIEWED: the x-plane hard-edge Conway–Deift comparison for every α_x ∈ (−1, 1), incl.
Lemma W′ at α_x = 0), `ROUTE2_p1.md` (the symmetric p = 1 frame), `../RH_p1_general.md` (RH₁(r), REVIEWED), `../px/RH_px.md`
(the x-plane interpolation problem, (Y4)_x, extraction), PROOF.md §3.21 (Theorem SH-r). Numerics:
`checks/check_bnd_{coeff,fold}.py/.out`.

**Labels (per step).**

| Item | Statement (short) | Label |
|---|---|---|
| §1.1 Range check (option iii) | RH₁(r) covers a = ½ for pure powers (quotient construction; the mismatch κ_n − 1 decays like \|z\|^{4m+2}); the obstruction is that of the comparison step in the symmetric frame | PROVED (reading of RH₁(r), REVIEWED) |
| §1.2 Weaker targets | r = 2 with Ψ bounded (T3-all) or log-type (T3-log) is already PROVED-mod-cite; GAP-int is exactly D(γ) = ∞ at r = 2 | PROVED (bookkeeping) |
| §1.3 Remark Div | in the symmetric frame the C–D integrand for (Q₁)₂₁ is ≍ δ_n(z)/(πζ) on the lips; absolutely integrable only under a Dini condition on L₁′ | HEURISTIC (+ NUMERICAL, fold [4]) |
| §1.4 Option (i) (L^p / E^p, scalar weights) | in the symmetric frame the two columns need p < 2 and p > 2 at a = ½ | OBSTRUCTION (heuristic: A_p necessity not cited); not pursued |
| §2.1 Lemma F0 | fold(Y_ν^{(2m)}) = [[1, 0], [−2πiγ²_{2m−1}, 1]]·Y_μ^{(m)} (quadratic transformation of the RH matrix) | PROVED (self-contained) + NUMERICAL [1] |
| §2.2 Lemma P | for n even, every matrix of the WLXZ chain (and Plan 50's V, Q) is σ₃-even: X(−z) = σ₃X(z)σ₃ | PROVED-mod-cite (WLXZ v1 (2.1)–(2.3), (2.6), (2.15), (3.1), (3.6)–(3.11), (4.1), (4.12)–(4.15), (4.19), (4.22), (5.1)) + NUMERICAL [2] |
| §2.3 Lemma FS | D_ϱ(z) = D^x_{ϱ_x}(z²); Γ := D^x_{α}(z²)/D_a(z) is even with Γ₊Γ₋ = 1/\|y\| | PROVED |
| §2.4 Lemma FJ | jumps of the folded frame Q^x: band [[0, 1], [−1, 0]]; lips of hard-edge type with weight w_x = x^{α_x}ϱ_x; none on ℝ₋; I + O(e^{−cn}poly(n)) elsewhere | PROVED-mod-cite (Plan 50 §§2–3; RH₁(r) §§2, 5) |
| §2.5 Lemma FN | fold(N₀^{KV})Γ^{σ₃} = [[1, 0], [−i, 1]]·N₀^x (N₀^x the [0, 4] outer solution) | PROVED (uniqueness) + NUMERICAL [3] |
| §2.6 Lemma Fφ | e^{−2nφ_KV} on the folded lips = e^{−4(n²f_K)^{1/2}}, f_K(x) := −f(√x)²/4 conformal, f_K′(0) < 0, band ↦ ζ < 0, ℝ₋ ↦ ζ > 0 | PROVED-mod-cite (KV (5.6)–(5.8) via RH₁(r) §5) |
| §2.7 Lemma FY ((Y4)ᶠ) | fold(R) is RH_px's one-sided x-interpolation problem at p = 1; RH_px's (Y4)_x applies | PROVED-mod-cite (RH_px §5 argument; RH₁(r) §6) |
| §3 H1ᶠ, LW1ᶠ, URᶠ, Q^x ∈ I + ∂C(L²), Cᶠ, Dᶠ | ROUTE2 §§3–4 at the folded hard edge, α_x = r − 2 ∈ (−1, 1); the rest of the contour folded from Plan 50 | PROVED-mod-cite (as ROUTE2, ROUTE2_p1) |
| **Theorem RII₁ᶠ** | p = 1, **1 < r < 3**, (H_an₁): m b_m = ½(1 + O(1/m)), a_m/(2b_m) = 1 + O(1/m) | **PROVED-mod-cite**; Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan53.md), fixes applied — REVIEWED; a second, partly independent proof of the (a_m, b_m) part of §3.23's RII_x1 on 1 < r < 3 |
| **Corollary B_{p=1}^{all,ᶠ}** | p = 1, **every r > 1** (integers included), every sequence-form slowly varying Ψ (incl. D(γ) = ∞): the full pointwise Law P; rate O(1/n) under (H_an₁), regular majorant of 1/n + ρ(⌈n/M₀⌉) in general | **PROVED-mod-cite**; Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan53.md), fixes applied — REVIEWED; second proof of §3.23's B_{p=1}^{all} (not a new closure) |
| GAP-int (Plan 50) | p = 1, r ∈ {2, 3, …}, D(γ) = ∞ | closed by §3.23 (Plan 54); **second proof** here (B_{p=1}^{all,ᶠ}) |
| OBSTRUCTION-a (Plan 50) | \|a\| ≥ ½ in the symmetric band-centre C–D frame | stands as stated (scoped to that frame); it is an obstruction of the frame and of extracting β_n individually, not of the law (§1.3, §4) |
| §5 Lemma IR | interpolation in r: \|log b_n²(k^{−2}Ψ) − log b_n²(k^{−2+δ}Ψ)\| ≤ δ·sup_τ Σ_k\|log(k/n)\|(μ_n^τ + μ_{n−1}^τ)(k) | PROVED (FV⁺); not used (it needs a QL-type localization) |
| GAP-rate₁ | the 1/n coefficient (tilt law) | GAP; CONJECTURE + NUMERICAL (§6) |

Notation (ROUTE2_p1 / RH₁(r)): WLXZ = Wu–Lin–Xu–Zhao arXiv:1410.3948v1 at their α = 1 (written α_W); ν = the symmetrization
of μ := σ_{r,Ψ₁} = Σ_k k^{−r}Ψ₁(k)δ_{1/k} (nodes ±k^{−1/2}, masses ½k^{−r}Ψ₁(k)), so μ = (y ↦ y²)_*ν; n = the degree of the
symmetric problem, **always even, n = 2m**; z = WLXZ's rescaled variable (their (3.1): U(z) = n^{nσ₃/2}Y(n^{−1/2}z)); band
[−2, 2]; a := r − 3/2 (KV's exponent at the band centre), **α := α_x := r − 2 = a − ½** (the hard-edge order of μ). KV frame:
V ↦ σ₃Vσ₃. Plan 50's objects: m_σ = |x|^{2a}ϱ, ϱ = h_W·H_n²·q_n (q_n(z) = Ψ₁(n/z²)/Ψ₁(n)), D_a = (z/Φ)^a, D_ϱ, 𝔇 = D_aD_ϱ,
N₀ (jump [[0, −1], [1, 0]] on (−2, 2)), N_σ = 𝔇_∞^{σ₃}N₀𝔇^{−σ₃}, Q = 𝔇_∞^{−σ₃}V𝔇^{σ₃} (KV frame), f (KV's conformal map, odd,
f′(0) = πψ(0) > 0), φ_KV = −φ_WLXZ, the lips Σ₂, Σ₄, Σ₆, Σ₈ = f^{−1}(arg ζ = π/4, 3π/4, −3π/4, −π/4) in U(0, ε).

---

## 1. Where the boundary obstruction sits

### 1.1 Option (iii): RH₁(r) at a = ½ (pure powers) — no obstruction

RH₁(r) (REVIEWED) is a **quotient** construction: V·P₀^{−1} near 0 with KV/Vanlessen's Bessel parametrix Ψ_a, which exists for
every a > −½ (KV (5.17)–(5.23)). Its band-centre mismatch is Lemma M: |J_H − I| ≤ |κ_n^{±1} − 1|·C(1 + ρ^{−2|a|}(1 + |log ρ|)²),
with κ_n − 1 = O((|z|²/n)^{2m+1}) from the Stirling truncation Q_m (m = ⌈|a|/2⌉ = 1 at a = ½), so |J_H − I| ≤ Cn^{−1}min(1,
(n|z|)^δ), δ = 4m + 2 − 2|a| = 5 > 0. **Nothing in RH₁(r) degenerates at a = ½** (the integer Bessel orders a ± ½ = 1, 0 at most
add logarithms, covered by the (1 + |log ρ|)² padding of Lemma M's bound; RH₁(r)'s numerics [3] include a = 0.5). So for Ψ ≡ 1 the law at r = 2 holds with rate (RH₁(r)), and the
obstruction of Plan 50 is specific to the **comparison** step: a Ψ with D(γ) = ∞ has a band-centre mismatch D_ϱ²/ϱ − 1 that
does not decay as z → 0 (LW1₁), which a quotient cannot absorb (ROUTE2_p1 §2, last paragraph), and the C–D comparison that
absorbs it needs Q̃^{±1} ∈ L²(|dz|), i.e. |a| < ½.

### 1.2 Weaker targets already covered

At r = 2 (p = 1): Ψ bounded slowly varying — Theorem T3-all (§3.8); Ψ log-type (slowly varying with D(γ) < ∞, e.g.
(log k)^β) — Theorem T3-log (§3.9). Both are PROVED-mod-cite and REVIEWED for every p > 0, s > 1. So GAP-int is exactly
"r = 2 (equivalently, by CT₁, any integer r ≥ 2) with D(γ) = ∞", e.g. Ψ = exp √log(k + e).

### 1.3 Remark Div (why the symmetric frame must fail at a = ½; HEURISTIC)

In the symmetric frame, Proposition D₁'s main term is ∫δ_n·μ̃e₂e₁ᵀμ̃^{−1} over the lips, with μ̃e₂e₁ᵀμ̃^{−1} =
A₀Ψ_ae₂e₁ᵀΨ_a^{−1}A₀^{−1}(phases). At a = ½ the rank-one factor is of size ≈ 1/(π|ζ|) (5 digits, numerical) as ζ → 0 on a lip ray
(`check_bnd_fold.out` [4]: |Ψe₂e₁ᵀΨ^{−1}|·|ζ| = 0.31831 ≈ 1/π for |ζ| = 10⁻⁴ … 10⁻¹², Vanlessen (4.27) at λ = ½), and it sits in
the off-diagonal entry that is odd in z. With |dz| ≍ |dζ|/n, the integral ∫_0 δ_n(r)(nr)^{−1}dr converges absolutely only if
δ_n(r) = D_ϱ²/ϱ − 1 is Dini at r = 0. For fixed n, δ_n(r) → 0 as r → 0 only like the local tilt
ε₁(log n + 2 log(1/r)) (the argument of LW1₁ with the far part split off), so absolute convergence needs ∫^∞ε₁(u)du < ∞ —
which forces log Ψ to converge (the T3-conv case). In the symmetric frame this entry feeds (Q₁)₂₁, i.e. the individual β_n,
which encodes hard-edge pointwise data of μ (the Cholesky entries l_m² = −P_{m}(0)/P_{m−1}(0)-type, cf. Plan 52's remark that
an RH argument for xσ would need Y_σ(0)). **The law for μ does not need β_n individually** — only a_m, b_m — and those are read
off a different frame in which the dangerous entry is multiplied by z (§2, §3.6). This is the idea of the fold.

### 1.4 Option (i): L^p / Smirnov E^p or scalar power weights — OBSTRUCTION in the symmetric frame (heuristic)

UR₁(d)'s core operators are, column by column, h ↦ z^{±a}C(h s^{∓a}) on a star of rays (Lemma W with exponents ±a). On L^p
(1 < p < ∞) these are bounded iff |s|^{∓ap} is an A_p weight on the rays, i.e. −1 < ∓ap < p − 1. At a = ½ the two columns
require p < 2 and p > 2 respectively; with a scalar power weight |s|^β on L² they require −1 < β ∓ 1 < 1, i.e. β ∈ (0, 2) and
β ∈ (−2, 0). (A column-dependent weight on the full matrix space is excluded, heuristically, because the band jump
[[0, 1], [−1, 0]] exchanges the columns.) So no
L^p theory and no scalar weight rescues the symmetric frame at a = ½; the Conway–Deift / Deift–Zhou L^p machinery (C–D §4.1:
C_Σ^± bounded on L^p for Carleson Σ) is available but does not help. *Label:* OBSTRUCTION (heuristic): the "only if" of the A_p
characterization (Hunt–Muckenhoupt–Wheeden) was **not read**, so this is recorded as a reason not to pursue option (i), not as
a theorem. The fold of §2 avoids this by **restricting to the subspace of σ₃-even functions and changing variable**: on that
subspace ‖fold X‖_{L²(|dx|)} weights the entries by |z|, |z|^{−1}, |z|³, |z| (a conjugation-type weight, not a column weight on the
full space), and the C–D comparison is then run in L²(|dx|) on Σ_x (§2.4, §3).

Option (ii) (a log-modified local frame at the integer Bessel orders 1, 0) is realized in §2–§3, but **in the folded variable**:
the integer-order model is KMVV's hard-edge Bessel model of order α_x = 0 (logs, Lemma W′), not a modification of KV's Ψ_½ in
the symmetric variable, where the column split |ζ|^{±1/2} (not the logs) is the problem.

---

## 2. The fold

**Definition.** A matrix function X on a set G = −G is **σ₃-even** if X(−z) = σ₃X(z)σ₃, i.e. X₁₁, X₂₂ are even and X₁₂, X₂₁
odd. For such X put

  (fold X)(x) := z^{−σ₃/2}X(z)z^{σ₃/2} = [[X₁₁(z), X₁₂(z)/z], [zX₂₁(z), X₂₂(z)]],  x = z², z ≠ 0.

The entries are even in z, so fold X is a well-defined function of x on G² := {z² : z ∈ G} ∖ {0}, analytic where X is (z ↦ z²
is a local biholomorphism off 0). fold(XY) = fold X·fold Y; fold acts trivially on diagonal and on constant diagonal matrices.
*Jumps.* If X₊ = X₋J on an oriented arc γ ∌ 0 with −γ also in the contour and J(−z) = σ₃J(z)σ₃ (orientation transported by
z ↦ −z), then on γ² (oriented as the image of γ; z ↦ z² is conformal near γ and maps the ±-sides of γ to the ±-sides of γ²)
fold X₊ = fold X₋·fold J, computed with the preimage on γ.

### 2.1 Lemma F0 (fold of the OP Riemann–Hilbert matrix) — PROVED

Let ν be an even positive measure on ℝ with infinite support and all moments finite, μ := (y ↦ y²)_*ν, n = 2m, Y_ν^{(n)} the
Fokas–Its–Kitaev matrix [[π_n, C(π_nν)], [−2πiγ²_{n−1}π_{n−1}, −2πiγ²_{n−1}C(π_{n−1}ν)]] (C(fν)(z) = (2πi)^{−1}∫f dν/(s − z),
γ²_j = 1/‖π_j‖²_ν), and Y_μ^{(m)} the same for μ in the variable x. Then Y_ν^{(n)} is σ₃-even and

  fold Y_ν^{(2m)} = [[1, 0], [−2πiγ²_{2m−1}, 1]]·Y_μ^{(m)}.

*Proof.* Parity: π_{2m}(y) = P_m(y²) and π_{2m−1}(y) = yP̃_{m−1}(y²) (π_j has parity (−1)^j for even ν); here P_m are the monic
OPs of μ (∫P_m(y²)y^{2j}dν = ∫P_mx^jdμ) and P̃_{m−1} those of xμ. Row 1: pairing ±s, 1/(s − z) − 1/(s + z) = 2z/(s² − z²), so
C(π_{2m}ν)(z) = z·(2πi)^{−1}∫P_m(x′)dμ(x′)/(x′ − x) = z·C_x(P_mμ)(x), hence (fold Y)₁· = (P_m, C_x(P_mμ)) = row 1 of Y_μ.
Row 2: zπ_{2m−1}(z) = xP̃_{m−1}(x), and for the odd π_{2m−1}, s[1/(s − z) + 1/(s + z)] = 2s²/(s² − z²), so
C(π_{2m−1}ν)(z) = C_x(x′P̃_{m−1}μ)(x). The monic degree-m polynomial xP̃_{m−1}(x) is μ-orthogonal to all x^j, j ≤ m − 2, hence
equals P_m + cP_{m−1}. So row 2 of fold Y = −2πiγ²_{2m−1}·(row 1 of Y_μ) + c′·(row 2 of Y_μ), and det fold Y = det Y_ν = 1 =
det Y_μ forces c′ = 1. ∎ (Classical in substance — the quadratic transformation of orthogonal polynomials; proved, not cited.)
NUMERICAL (`check_bnd_fold.out` [1]; 30 atoms, r = 2, Ψ = exp √log(k + e), m = 4, 40 digits): relative error ≤ 1.1·10⁻³⁹ at four
points x and for both z = ±√x; a_j(μ) = β_{2j} + β_{2j+1}, b_j(μ)² = β_{2j−1}β_{2j} to 10⁻⁴¹.

### 2.2 Lemma P (parity of the WLXZ chain, n even) — PROVED-mod-cite (WLXZ v1, quoted in `../CITATIONS.md` "(WLXZ-v1, Plan 53)")

Take WLXZ's contour symmetric: Σ_{l,±} := −Σ_{r,∓}, Σ^△_{l,±} := −Σ^△_{r,∓} (admissible: WLXZ's requirements — avoid the zeros of
Π and w (3.9)–(3.10), Re φ < 0 on the lips (4.33), and (5.8)'s Re φ̃ > 0, Re φ̂ > 0 — are invariant under z ↦ −z by (a)–(c)
below and by **φ̂(−z) = φ̃(z)** (from (2.4), (4.28) and g′ odd; Rule R F3); their Figure 3 is symmetric), and inside U(0, ε) Plan 50's lips f^{−1}(arg ζ = ±π/4, ±3π/4), symmetric since f is odd. Then for n even each of
Y (rescaled), U, R, T, WLXZ's Q (here Q_W), V — for TC(α_W = 1) and for the weights w·F (RH₁(r)) and w·F·q_n (Plan 50) — and
Plan 50's Q = 𝔇_∞^{−σ₃}σ₃Vσ₃𝔇^{σ₃} is σ₃-even, except that R and T are σ₃-even **up to the scalar −1 on Ω^△**.

*Proof.* (a) Scalars: w_d (2.15) is a function of 1/z² (analytic off iℝ, the only place where 1/z² ≤ 0), so w is even; F = H_n(z²)^a
and q_n are even; θ = nπ/z² − πα_W (3.7) is even; γ = −2nπ/z³ is odd, so Π = sin θ/γ (3.6) is odd. (b) g (2.2) with ψ even
((2.1)) and ∫ψ = 1 ((4.5)): for z ∈ ℂ±, −(z − s) ∈ ℂ∓ and log(−(z − s)) = log(z − s) ∓ iπ, so g(−z) = g(z) ∓ iπ; hence
e^{−ng(−z)} = e^{−ng(z)} (n even) and, by (2.3), e^{2nφ(−z)} = e^{2nφ(z)}. (c) D (2.6) is a function of t = −n/z² with the
principal log ("−1/z² = e^{±πi}/z² for z ∈ ℂ±, arg z ∈ (−π, π)" is the principal argument of −n/z²), hence even; D̂(z) = D̃(−z)
by (4.15), (4.22); E (4.19) is even. NUMERICAL ([2]): g(−z) − g(z) = −iπ to 10⁻⁹ (quadrature), D(−z) = D(z), D̂(−z) = D̃(z) exactly.
Now: Y_ν is σ₃-even (Lemma F0; WLXZ's Y uses the residue form (2.14), Y₁₂ = Σ wπ/(z − x_k) = −2πi·C(πν), which differs from the
FIK convention of F0 by a constant diagonal conjugation — this changes L but not σ₃-evenness, M's diagonality in §3.6 or the
invariance lemma; Rule R F4); U = n^{nσ₃/2}Y(n^{−1/2}z) too. In (3.11) the regions pair as Ω_{r,±} ↔ −Ω_{r,±} = Ω_{l,∓} with the
same factor (U₋ on Ω_{l,−} ∪ Ω_{r,+}, U₊ on Ω_{l,+} ∪ Ω_{r,−}; likewise U^△±); U± (3.9) has (1,2) entry −(w/Π)e^{±iθ}, odd, so
U± is σ₃-even; U^△± = Π^{−σ₃}[[1, 0], [−e^{±iθ}/(Πw), 1]] satisfies U^△±(−z) = −σ₃U^△±(z)σ₃ (Π^{−σ₃} is odd as a whole,
diag(1/Π, Π)(−z) = −diag(1/Π, Π)(z), and the triangular factor is σ₃-even). So R is σ₃-even with the factor −1 on Ω^△. T (4.1)
multiplies by e^{(−ng+nl/2)σ₃}, even by (b). In (4.12) the pairing is again by mirrored regions; V± (4.13) has (2,1) entry
±e^{2nφ}/(2iγw), odd by (a)–(b), so V± is σ₃-even; V^△± = diag(e^{±iθ}/(2iγ), 2iγe^{∓iθ}) is odd, which cancels R's −1 on Ω^△. So
Q_W is σ₃-even. V (5.1) multiplies by constants, E^{σ₃} (even) and D̂^{σ₃}/D̃^{σ₃}/D^{σ₃} on mirrored regions (c). RH₁(r)'s and
Plan 50's modifications only multiply w by the even factors F, q_n (Lemma W1(r), ROUTE2_p1 §2); σ₃-conjugation and the even
diagonal 𝔇^{σ₃} (D_a(−z) = D_a(z) since z/Φ(z) is even and the log is the branch vanishing at ∞; D_ϱ even since ϱ is) preserve
σ₃-evenness. ∎

(The jumps then satisfy J(−z) = σ₃J(z)σ₃ with the transported orientation, which is all the fold needs.)

### 2.3 Lemma FS (Szegő functions under the fold) — PROVED

For a weight q on [0, 4] with log q ∈ L¹(dx/√(x(4 − x))) let D^x_q be its Szegő function on [0, 4]:
log D^x_q(x) = (R_x(x)/2π)∫_0^4 log q(x′)dx′/(√(x′(4 − x′))(x − x′)), R_x(x) = (x(x − 4))^{1/2} ~ x (ROUTE2 §3.3 with b = 4);
D^x_{x^α} with (D^x_{x^α})² = (4x/Φ_x(x))^α, Φ_x(x) = (x^{1/2} + (x − 4)^{1/2})² (ROUTE2 §3.3). Then:
- (i) for an even weight ϱ on [−2, 2], **D_ϱ(z) = D^x_{ϱ_x}(z²)**, ϱ_x(x) := ϱ(√x). *Proof:* in Plan 50's formula
  log D_ϱ(z) = (R(z)/2π)∫_{−2}^2 log ϱ(y)dy/(√(4 − y²)(z − y)) pair ±y (1/(z − y) + 1/(z + y) = 2z/(z² − y²)) and put x′ = y²:
  log D_ϱ(z) = (zR(z)/2π)∫_0^4 log ϱ_x(x′)dx′/(√(x′(4 − x′))(x − x′)), and zR(z) = R_x(z²) (both ~ z² at ∞). ∎
- (ii) Γ(z) := D^x_{x^α}(z²)/D_a(z), α = a − ½, is even, analytic and zero-free off [−2, 2], Γ(∞) = 1, |Γ(z)| ≍ |z|^{−1/2} near 0, Γ
  smooth and nonvanishing up to the band near ±2, and **Γ₊Γ₋ = 1/|y| on (−2, 2) ∖ {0}**: D^x₊D^x₋ = x^α = |y|^{2a−1} at x = y²
  (for y > 0 the + side of the band maps to the + side of (0, 4), for y < 0 to the − side; the product is the same), and
  D_{a,+}D_{a,−} = |y|^{2a} (RH₁(r) Lemma G). The size at 0: |D^x_{x^α}(x)| ≍ |x|^{α/2} (Φ_x(0) = −4) and |D_a| ≍ |z|^a. ∎
- Hence the **folded Szegő function of the folded band weight** w_x(x) := m_σ(√x)/√x = x^αϱ_x(x) is D^x_w = D^x_{x^α}·D^x_{ϱ_x} =
  Γ·𝔇 (as functions of z), and D^x_{ϱ_x} is **exactly Plan 50's D_ϱ** — no new Szegő function of q_n appears.

### 2.4 The folded frame and Lemma FJ (folded jumps) — PROVED-mod-cite (Plan 50 §§2–3, RH₁(r) §§2, 5)

Put (V_KV := σ₃Vσ₃ the KV frame, Q = 𝔇_∞^{−σ₃}V_KV𝔇^{σ₃} as in ROUTE2_p1 §3.1)

  **Q^x(x) := [[1, 0], [−(Q₁)₂₁, 1]]·fold Q(x)·Γ(z)^{σ₃} = [[1, 0], [−(Q₁)₂₁, 1]]·𝔇_∞^{−σ₃}·fold V_KV(x)·D^x_w(x)^{σ₃}.**

(fold Q·Γ^{σ₃} = I + O(1/x) except for the constant (2,1) entry (Q₁)₂₁ (the (2,1) entry of z·(Q₁/z)); the left factor
normalizes Q^x → I.) Σ_x := {z² : z ∈ Σ} (Σ = Plan 50's contour, symmetric by §2.2). **Jumps of Q^x** (left constants do not
change jumps):
- **(a) band (0, 4):** fold of [[0, m_σ], [−1/m_σ, 0]] at y > 0 is [[0, m_σ/y], [−y/m_σ, 0]] = [[0, w_x], [−1/w_x, 0]]; after
  (D^x_w)^{σ₃} (D^x_{w,+}D^x_{w,−} = w_x, §2.3) it is **[[0, 1], [−1, 0]]**.
- **(b) folded lips** (images of Σ₂, Σ₈; Σ₄, Σ₆ = −Σ₈, −Σ₂ have the same images): V_KV's lip jump [[1, 0],
  [ω^{−1}ϱ^{−1}e^{−2nφ_KV}, 1]] (KV (5.1), ω = (z²)^a as in KV (3.6)) plus Plan 50's (J2) entries. Fold multiplies the (2,1)
  entry by z, and z(z²)^{−a} = x^{½−a} = x^{−α} for Re z > 0 (principal powers), so the folded jump is
  [[1, 0], [e^{−2nφ_KV}/w_x, 1]] with w_x continued from the band (principal x^α); in the Q^x frame
  **[[1, 0], [(D^x_w)²w_x^{−1}e^{−2nφ_KV}, 1]]**, plus the folded (J2) entries, which are O(e^{−cn/|x|}poly(n, 1/|x|))
  (RH₁(r) Lemma M (J2), the fold factors z^{±1} being polynomial).
- **(c) ℝ₋ (the image of iℝ): no jump** — V_KV is analytic across iℝ (Ω∞, ROUTE2_p1 §3.1 "Nothing jumps on iℝ"), fold V_KV is
  single-valued (§2.2), and D^x_w is analytic off [0, 4].
- **(d) the rest of Σ_x** (images of the lips, saturated pieces, Σ^△ and vertical segments outside U(0, ε) ∪ U(±2, ε)): the folds
  of Plan 50's jumps there, which are I + O(e^{−cn}poly(n)) (WLXZ (5.8); RH₁(r) Lemma W1(r) with the q_n^{±1} factors; ROUTE2_p1
  §3.4), also after conjugation by the bounded outer model; folding costs the factors z^{±1}, |z| ≤ k_n ≍ √n, and the bounded
  diagonal Γ^{±σ₃}.
- **(e) U_x(4, ε_x)** (image of U(2, ε); U(−2, ε) has the same image): the folds of V's jumps near 2, used only through the folded
  Airy parametrix (§3.1).

### 2.5 Lemma FN (the folded outer parametrix) — PROVED + NUMERICAL [3]

With N₀^{KV} := σ₃N₀σ₃ (the [−2, 2] solution with jump [[0, 1], [−1, 0]]; it is Plan 50's outer model in the Q frame, since
𝔇_∞^{−σ₃}σ₃N_σσ₃𝔇^{σ₃} = N₀^{KV}) and N₀^x the [0, 4] solution with jump [[0, 1], [−1, 0]] (N₀^x = [[(γ + γ^{−1})/2,
(γ − γ^{−1})/(2i)], [−(γ − γ^{−1})/(2i), (γ + γ^{−1})/2]], γ = ((x − 4)/x)^{1/4}):

  **fold(N₀^{KV})·Γ^{σ₃} = [[1, 0], [−i, 1]]·N₀^x.**

*Proof.* N₀^{KV} is σ₃-even (γ_N(−z) = γ_N(z)^{−1} for γ_N = ((z − 2)/(z + 2))^{1/4}). Both sides are analytic off [0, 4] with the
jump [[0, 1], [−1, 0]] on (0, 4) (left: §2.4(a) with m_σ ≡ 1, i.e. Γ₊Γ₋ = 1/y). Near 0 the left side is O(|x|^{−1/4}): N₀^{KV} is
bounded near z = 0, so (1,2) = (N₀^{KV})₁₂Γ^{−1}/z = O(|z|^{−1/2}), (1,1) = O(|z|^{−1/2}), (2,·) = O(|z|^{1/2}); near 4 both are
O(|x − 4|^{−1/4}) (Γ is smooth and nonzero there). So H := (left)·(N₀^x)^{−1} (det N₀^x = 1) has no jump and isolated singularities
of order ≤ |x|^{−1/2}, |x − 4|^{−1/2} at 0, 4: removable; H is entire, and → [[1, 0], [(N₀^{KV},1)₂₁, 1]] at ∞, so it is that
constant; (N₀^{KV},1)₂₁ = −i from γ_N = 1 − 1/z + O(z^{−2}). ∎ NUMERICAL ([3]): the constant is [[1, 0], [−i, 1]] to 10⁻³⁹ at six
points (incl. x = 10⁻³, x ≈ 3.9, x = −3 + 0.2i) for a = 0.5, 0.8, 0.1.

### 2.6 Lemma Fφ (folded phase and conformal map) — PROVED-mod-cite (KV (5.6)–(5.8) via RH₁(r) §5)

By RH₁(r) §5, f(z) = iφ_KV(z) − iφ_KV,₊(0) in ℂ₊ and −iφ_KV(z) − iφ_KV,₊(0) in ℂ₋; f is odd, real on ℝ, conformal on U(0, ε),
f′(0) = πψ(0) > 0. φ_KV,₊(0) = −φ_WLXZ,₊(0) = iπ/2 (g₊(0) = ∫log|s|ψ + iπ/2, l/2 = ∫log|s|ψ by (4.4) at x = 0). Hence for n
even e^{−2nφ_KV(z)} = e^{±2inf(z)} for z ∈ ℂ± (the constant e^{∓2nφ_KV,₊(0)} = e^{∓iπn} = 1). Put

  **f_K(x) := −f(√x)²/4,  φ^x(x) := −2f_K(x)^{1/2}** (principal root).

f(√x)² is even in √x, so f_K is analytic in U_x(0, ε²), real, f_K(0) = 0, **f_K′(0) = −f′(0)²/4 < 0**; (0, ε²) ↦ ζ < 0, (−ε², 0) ↦
ζ > 0. For x ∈ ℂ± (√x principal lies in the quadrant of ℂ± with Re > 0) one has f_K^{1/2} = ∓(i/2)f(√x) (the sign giving Re > 0),
so **e^{−2nφ_KV(√x)} = e^{2nφ^x(x)} = e^{−4(n²f_K)^{1/2}}** on the folded lips, φ^x₊ = −φ^x₋ on the band, φ^x analytic across ℝ₋,
and |e^{2nφ^x}| ≤ e^{−cn|x|^{1/2}} on the folded lips. The folded lips are f_K^{−1}(arg ζ = ±π/2) (ζ := nf(z) at arg ±π/4 gives
−ζ²/4 at arg ∓π/2): the upper folded lip maps to the lower ray, the ordering reversal of RH_px Lemma 4.1 / KMVV (6.42)–(6.53).
This is the structure of RH_px Lemma 4.1 (f there = (φ ± iπ)²/4), with the KMVV rays at angle π/2 instead of 2π/3 — allowed by
KMVV's angle freedom ("It could be replaced by any angle in (0, π)", quoted in `../CITATIONS.md`).

### 2.7 Lemma FY ((Y4)ᶠ: behaviour of the folded true problem at 0) — PROVED-mod-cite (RH_px §5 (Y4)_x, RH₁(r) §6)

For fixed n and x → 0, fold R₁₂, fold R₂₂ = O(1 + |x|^{α−η}ℓ(x)) uniformly in arg x (band boundary values included), ℓ := 1 +
|log|x||, every η > 0; fold R₁₁, fold R₂₁ are polynomials in x (bounded).

*Proof.* By Lemma F0's pairing, fold U is the **one-sided** x-interpolation problem of RH_px §1 with nodes X_k² (X_k = n^{1/2}x_k,
WLXZ (3.2)) and masses 2w(X_k): fold U₁₂(x) = Σ_k 2w(X_k)U₁₁(X_k)/(x − X_k²) (U₁₁ even), and row 2 likewise with the polynomial
zU₂₁(z). In the lens sectors, fold R₁₂ = fold U₁₂ − 𝒦^x₋ (WLXZ (3.12)) with 𝒦^x± := U₁₁·(w/(zΠ))e^{±iθ} = U₁₁·(2w)θ_x′e^{±iθ}/sin θ,
θ_x(x) := nπ/x − π (so γ/z = −2nπ/z⁴ = 2θ_x′): this is RH_px's 𝒦± at p = 1 with weight 2w. RH_px's (Y4)_x argument applies
verbatim: residues 2w(X_k)U₁₁(X_k); Im θ_x < 0 on ℂ₊, so 𝒦^x₋ = O(e^{−cn|Im(1/x)|}) there; 𝒦^x₋ − 𝒦^x₊ = −2iU₁₁(2w)θ_x′ =
O(|x|^{α−η}) (|wFq_n| ≍ |z|^{3+2a}|q_n| by RH₁(r) §6(b), |q_n| ≤ C_η|z|^{−2η} (Potter), times n|x|^{−2}); the left half-plane is
node-free. Away from the lens the direct sum Σ_k k^{−r}Ψ₁(k)/max(|x|, 1/k) (scaled; fixed n) gives O(1 + |x|^{r−2−η}). ∎

---

## 3. Theorem RII₁ᶠ: ROUTE2's hard-edge comparison in the folded variable

Fix 1 < r < 3, so **α = r − 2 ∈ (−1, 1)** — exactly ROUTE2's range (Plan 48; UR′ incl. (b′) for every |α| < 1, Lemma W′ at
α = 0) — and Ψ₁ with (H_an₁) (ROUTE2_p1 §2). Everything below is in x, on Σ_x, for the normalized folded problem Q^x of §2.4.
The dictionary to ROUTE2 §§3–4 is: (N, f, D_w, w₀, b, φ) ↦ (n, f_K, D^x_w, w_x, 4, φ^x); "D_∞-frame" ↦ the Q^x frame.

### 3.1 The comparison problem (Lemma H1ᶠ = ROUTE2 H1′ with the folded data)

- Outside U_x(0, δ_x) ∪ U_x(4, ε_x): the outer model **N₀^x** (Q^x frame). By Lemma FN this is the fold of Plan 50's outer model,
  up to the constant [[1, 0], [−i, 1]].
- In U_x(0, δ_x): ROUTE2's P̃₀ (KMVV left-endpoint construction (6.42)–(6.53), Bessel order α) with the folded data:
  P̃₀^x := Ẽ^x·σ₃Ψ_α(n²f_K)σ₃·D^x_w{}^{−σ₃}e^{nφ^xσ₃} (V-type frame), Ẽ^x := N^x_V D^x_w{}^{σ₃}M f_K^{σ₃/4}(2πn)^{σ₃/2}, M = [[1, i],
  [i, 1]]/√2, N^x_V := D^x_{w,∞}{}^{σ₃}N₀^x D^x_w{}^{−σ₃}; in the Q^x frame P̃₀^x D^x_w{}^{σ₃}·(const). As in ROUTE2 H1′:
  (i) Ẽ^x = const·N₀^xMf_K^{σ₃/4}(2πn)^{σ₃/2} **does not involve the weight**, is analytic in U_x(0, δ_x) (band: RH_px Lemma 4.2(i)'s
  computation, f_K < 0 on the band so f_{K,+}^{1/4} = −if_{K,−}^{1/4}; at 0 an O(|x|^{−1/2}) singularity, removable by KMVV
  Prop. 6.5's argument; across ℝ₋ there is nothing to check: N₀^x and f_K are analytic there), det Ẽ^x = 1, and
  Ẽ^x(2πn)^{−σ₃/2} is bounded with bounded inverse uniformly in n; (ii) P̃₀^x has exactly the band jump of §2.4(a), no jump on ℝ₋,
  and on the folded lips (2,1) entry **c_±e^{2nφ^x}** in the Q^x frame, c_± = e^{∓iπα} (KMVV (6.16), (6.18), (6.45)); (iii)
  P̃₀^x(N₀^x)^{−1} = I + O(1/n) on ∂U_x(0, δ_x) (KMVV (6.28)).
- In U_x(4, ε_x): the **folded Airy parametrix** P̃₄^x := [[1, 0], [−i, 1]]^{−1}·fold(𝔇_∞^{−σ₃}P₊𝔇^{σ₃})·Γ^{σ₃}, with P₊ Plan 50's
  Airy parametrix at +2 (ROUTE2_p1 §3.4; taken in the KV frame, i.e. σ₃-conjugated if written in WLXZ's) and fold evaluated with
  the principal root √x ∈ U(2, ε) (a local object: no σ₃-evenness is needed, since only the preimage near +2 is used; fold V is
  single-valued, so its jumps near 4 are computed from that preimage). It has the folded true jumps exactly, and P̃₄^x(N₀^x)^{−1} =
  [[1, 0], [−i, 1]]^{−1}·fold(I + O(1/n))·[[1, 0], [−i, 1]] = I + O(1/n) on ∂U_x(4, ε_x) (Lemma FN; |z| ≈ 2, so the fold factors
  are bounded).
- 𝒵̃^x: the small-norm problem with jumps P̃₀^x(N₀^x)^{−1}, P̃₄^x(N₀^x)^{−1} = I + O(1/n) on the two circles and N₀^xv^x(N₀^x)^{−1} =
  I + O(e^{−cn}poly(n)) on Σ_x outside the discs (§2.4(d); none on the band and on ℝ₋). Σ_x is a finite union of arcs with long
  pieces of length ≍ n (images of length ≍ √n), Carleson with a uniform constant; RH₁(r) §7's small-norm argument gives
  **𝒵̃^x = I + O(1/n)** uniformly, with first and second moments O(1/n). Q̃^x := 𝒵̃^x·P̃^x.
- **Jumps:** ṽ^x = v^x except on the folded lips inside U_x(0, δ_x), where ṽ^x has (2,1) entry c_±e^{2nφ^x} and no (J2) entries.

### 3.2 Lemma LW1ᶠ (lip mismatch) — PROVED-mod-cite (LW1₁; ROUTE2 §3.3 for the x^α part)

On the folded lips in U_x(0, δ_x): **|(D^x_w)²/w_x − c_±| ≤ C(|x|^{1/2} + ε₁,n)**, ε₁,n := ε₁(log n − 2 log 2; θ_L) as in LW1₁.
*Proof.* (D^x_w)²/w_x = [(D^x_{x^α})²/x^α]·[D_ϱ²/ϱ] by §2.3 (D^x_{ϱ_x}(x) = D_ϱ(z), ϱ_x(x) = ϱ(z)). The first factor is c_±(1 + O(|x|^{1/2}))
(ROUTE2 §3.3, q = x^α, with b = 4: Φ_x(x) = −4(1 + O(|x|^{1/2}))); the second is 1 + O(|z| + ε₁,n) by **LW1₁** (Plan 50; the lips
here are the same lips, |arg(±z)| ∈ [π/4 − π/24, π/4 + π/24]), and |z| = |x|^{1/2}. ∎ Hence, with |e^{2nφ^x}| ≤ e^{−cn|x|^{1/2}}
and the (J2) bound, **‖v^x − ṽ^x‖_{L^∞(Σ_x)} ≤ C(1/n + ε₁,n) =: Cε′_n → 0**, and v^x − ṽ^x = δ^x_ne₂e₁ᵀ + (J2),
δ^x_n := ((D^x_w)²/w_x − c_±)e^{2nφ^x}.

### 3.3 Lemma URᶠ (uniform resolvent) — PROVED-mod-cite (ROUTE2 UR′; ROUTE2_p1 UR₁(c), (e))

For n ≥ n₀, 1 − C_{ṽ^x} is invertible on L²(Σ_x) with ‖(1 − C_{ṽ^x})^{−1}‖ ≤ C.
*Proof.* RH_ζ_close Lemma UR's scheme, localized as in ROUTE2 UR′ (a)–(e):
- **at 0** — (a) area estimate, (b′) m ∈ ∂C(L²), (d) the hard-edge piece: **ROUTE2 UR′ (a), (b′), (d) verbatim**, since by §3.1 the
  comparison problem near 0 has exactly ROUTE2's form Q̃^x = A₀^x·n^{σ₃/2}σ₃Ψ_α(n²f_K)σ₃·Θ^x with A₀^x analytic and bounded with
  bounded inverse uniformly in n (Ẽ^x and 𝒵̃^x = I + O(1/n)) and Θ^x bounded (e^{±nφ^x} bounded near 0 for fixed n), the local
  form of ROUTE2 §3.2 (Ψ = Ψ̂ζ^{ασ₃/2}S for α ≠ 0; Ψ = Ψ̂[[1, κ log ζ], [0, 1]]S at **α = 0**, i.e. r = 2), Lemma W with ±α/2
  (|α| < 1) and **Lemma W′** at α = 0, and the star Σ_x ∩ U_x(0, ·) = band, ℝ₋ (no jump), two folded lips at angles ±π/2 (the ray angle changes only Lemma W's star constants; precedents: Plan 51's ±πp/4, Plan 54's
  ±π/3; Rule R F11);
- **at 4** — (e): Q̃^x = (𝒵̃^xA₄^x)·[folded Airy model]·(bounded diagonal), the fold of ROUTE2_p1 UR₁(e)'s factorization at +2 (the
  fold is a conformal change of variable near z = 2 with bounded factors z^{±1/2}, so the commutator-kernel and multiplier bounds
  transfer);
- **elsewhere** — (c): Q̃^x = 𝒵̃^xN₀^x bounded with bounded inverse away from 0, 4. ∎

### 3.4 Q^x in I + ∂C(L²(Σ_x)) — PROVED-mod-cite

- *At 0:* by Lemma FY and the bounded explicit factors between R and V (RH₁(r) §6 "Bounds on V and P₀ near 0": diagonal factors
  fold trivially; the lens factors are lower triangular, so the fold multiplies their (2,1) entries by z), fold V_KV has the
  column structure of RH_px's (Y4)_x with α; with |D^x_w| ≍ |x|^{α/2}|q_n|^{1/2} (ROUTE2 §4.3; |q_n|^{±1} ≤ C_η|x|^{−η}), exactly
  ROUTE2 §4.3's computation gives **Q^x = O(|x|^{−|α|/2−2η}ℓ) ∈ L²_loc(|dx|)** for η < (1 − |α|)/4, det Q^x = 1 gives the same for
  (Q^x)^{−1}, and the annulus argument of UR′(b′) gives membership in I + ∂C(L²).
- *At 4:* fold of ROUTE2_p1 §4.2 "Q at ±2: Q = O(1)" (|z| ≈ 2, bounded fold factors, Γ bounded).
- *Elsewhere and at ∞:* bounded; Σ_x is bounded for fixed n, and Q^x = I + O(1/x).
- *Q̃^x:* by URᶠ and 𝒵̃^x = I + O(1/n).

### 3.5 Theorem Cᶠ and Proposition Dᶠ — PROVED-mod-cite (C–D Thm 4.4 and the arguments of Thm 4.7, Prop. 4.9; as ROUTE2 C′, D′)

**Cᶠ.** ‖(1 − C_{v^x})^{−1}‖ ≤ 2C for n ≥ n₁: ‖C_{v^x} − C_{ṽ^x}‖ ≤ ‖C₋‖‖v^x − ṽ^x‖_∞ ≤ C″ε′_n → 0 and C–D Theorem 4.7's
Neumann argument with URᶠ. Only ε′_n → 0 is used.

**Dᶠ.** Q^x₁ − Q̃^x₁ and Q^x₂ − Q̃^x₂ are O(ε′_n/n). *Proof:* ROUTE2 Proposition D′ verbatim with N ↦ n: main term
∫δ^x_nμ̃e₂e₁ᵀμ̃^{−1}; for |ζ| ≥ 2 (KMVV (6.28)) the integrand is ≤ C(|x|^{1/2} + ε₁,n)|x|^{−1/2}e^{−cn|x|^{1/2}}, integral
O(n^{−2} + ε₁,n/n); for |ζ| ≤ 2 (|x| ≲ n^{−2}) it is ≤ Cε′_n·n·|ζ|^{−|α|} (log² at α = 0; ROUTE2 §3.2), integral O(ε′_n/n) since |α| < 1;
correction term O(ε′_n²/n) by Cᶠ; (J2) parts O(n^{−K}); the extra factor x in Q₂ only improves the bounds. ∎
*(Contrast with §1.3, HEURISTIC: were Q̃^x the fold of Plan 50's comparison problem, the folded integrand would be
L·fold(X)·L̃^{−1} with fold(X) = [[X₁₁, X₁₂/z], [zX₂₁, X₂₂]] — the dangerous odd entry X₂₁ ≍ δ_n/(πζ) gets the factor z — integrated
against dx. Q̃^x is built directly in x; what is used is ROUTE2's bound, i.e. the folded rank-one factor is O(log²|ζ_K|) at α = 0:
`check_bnd_fold.out` [4], right column, |·|/(1 + log²|ζ_K|) ≤ 0.126 for |ζ_K| = 10⁻¹ … 10⁻¹².)*

### 3.6 Extraction — PROVED-mod-cite (RH_px §5 invariance lemma; Lemma F0)

For |z| > k_n (in Ω∞, outside all nodes), V = C₁^{σ₃}Y_ν(n^{−1/2}z)·h(z)^{σ₃} with C₁ constant and h := e^{−ng+nl/2}E·D·c scalar
(WLXZ (3.1), (4.1), (5.1)). V and Y_ν are analytic and invertible there, so h is analytic in |z| > k_n (the jumps of e^{−ng} and of
D·E on ℝ ∖ [−k_n, k_n] cancel, WLXZ (4.10), (4.20)); h is even (Lemma P); and V → I, Y_ν(n^{−1/2}z)z^{−nσ₃} → const give
h(z)z^n → const. Hence h(z)z^n is analytic in 1/x at x = ∞ (removable singularity). 𝔇 and Γ are even and analytic off [−2, 2],
→ 𝔇_∞, 1, so also analytic in 1/x at ∞. With fold Y_ν = L_Y·Y_μ^{(m)} (Lemma F0; the rescaling y = n^{−1/2}z only conjugates
by n^{∓σ₃/4}): Q^x = M·Y_μ^{(m)}(x/n)·κ(x)^{σ₃} for |x| large, with M constant lower triangular and κ = κ_∞x^{−m}(1 + κ₁/x + …);
M is diagonal because Q^x → I and Y_μ^{(m)}(x/n)κ^{σ₃} → const diagonal. By RH_px
§5's invariance lemma, (Q^x₁)₁₂(Q^x₁)₂₁ = n²b_m(μ)² and a(Q^x) := (Q^x₂)₁₂/(Q^x₁)₁₂ − (Q^x₁)₂₂ = n·a_m(μ) (Y_μ(x/n) rescales Y₁ by n and
Y₂ by n²; RH_px §5 conventions: b_m² = h_m/h_{m−1}, xP_m = P_{m+1} + a_mP_m + b_m²P_{m−1}). For the comparison problem, outside the
discs Q̃^x = 𝒵̃^xN₀^x, so (Q̃^x₁)₁₂(Q̃^x₁)₂₁ = (N₀,₁^x)₁₂(N₀,₁^x)₂₁ + O(1/n) = 1 + O(1/n) and a(Q̃^x) = a(N₀^x) + O(1/n) = 2 + O(1/n)
(N₀^x: γ = 1 − 1/x − (3/2)x^{−2} + …, (N₀,₁^x)₁₂ = i, (N₀,₁^x)₂₁ = −i, (N₀,₂^x)₁₂ = 2i, (N₀,₁^x)₂₂ = 0: the [0, 4] values (b/4)² = 1,
b/2 = 2), and Q̃^x₁ = O(1) with (Q̃^x₁)₁₂ = i + O(1/n). With Dᶠ:

  n²b_m(μ)² = 1 + O(1/n),  n·a_m(μ) = 2 + O(1/n),  n = 2m.

(No hard-edge pointwise value is needed: both functionals are read off the 1/x and 1/x² coefficients. The individual β_n of the
symmetric problem are not extracted — cf. §1.3.)

### 3.7 Theorem RII₁ᶠ

**Theorem RII₁ᶠ.** Let p = 1, **1 < r < 3**, and Ψ₁ = exp L₁(log t) with (H_an₁) (ROUTE2_p1 §2: L₁ analytic on {Re u > −c₀,
|Im u| < π}, c₀ > log 2, real on ℝ, bounded on {−c₀ < Re u ≤ 0, |Im u| ≤ π − θ} and ε₁(T; θ) → 0 for every θ > 0). For
μ = Σ_k k^{−r}Ψ₁(k)δ_{1/k}:

  **m b_m = ½(1 + O(1/m)) = c(1)(1 + O(1/m)),  m a_m = 1 + O(1/m),  a_m/(2b_m) = 1 + O(1/m).**

*Proof.* §3.6 with n = 2m: b_m = (1/n)(1 + O(1/n)) = (1/(2m))(1 + O(1/m)), a_m = (2/n)(1 + O(1/n)). The inputs: §2 (fold;
Lemma P needs n even, which is the only case used), §3.1–3.5. ∎
What is proved about the non-Fisher–Hartwig part: the lip mismatch moves Q^x₁, Q^x₂ by O(ε′_n/n) relative to Q̃^x; Q̃^x depends on
Ψ₁ at order 1/n (through 𝒵̃^x), so b_m(μ)/b_m(k^{−r}) − 1 = O(ε₁/m) is **not** claimed (GAP-rate₁).
For 1 < r < 2 this is another proof of the (a_n, b_n) part of Theorem RII₁ (Plan 50; nβ_n = 1 + O(1/n) is not obtained here), and
on 1 < r < 3 a second proof of the (a_m, b_m) part of §3.23's RII_x1 (Rule R F6).

*Cited (Rule C; quoted in `../CITATIONS.md`):* WLXZ v1 (via RH₁, RH₁(r), Plan 50, and the parity formulas "(WLXZ-v1, Plan 53)");
KV §5 (3.6), (5.1), (5.6)–(5.8) (through RH₁(r) §5 and Plan 50); KMVV §6 ((6.16)–(6.28), (6.42)–(6.53), Prop. 6.5, angle freedom);
C–D Theorem 4.4 and the arguments of Theorem 4.7, Proposition 4.9 (as reproduced in RH_ζ_close §1); DLMF 1.13.4, 1.14.38–40, 5.5.3,
5.11, 5.12.1/3, 10.25.2, 10.27.3–4, 10.28.2, 10.31.2 (through ROUTE2 §3.2, Lemmas W, W′ and LW1₁). *Internal, REVIEWED:* RH₁(r);
ROUTE2 (H1′, §3.2, LW1′'s x^α part, UR′ incl. (b′), Lemma W′, C′, D′, §4.3); ROUTE2_p1 (§2, LW1₁, §3.4 Airy discs, UR₁(c), (e),
§4.2); RH_px §1, §5 ((Y4)_x, invariance lemma). *New here:* the fold (Lemma F0 in RH form), Lemma P, Lemmas FS, FJ, FN, Fφ, FY,
the dictionary of §3, and the observation that the folded frame is ROUTE2's hard edge with α = r − 2.

### 3.8 Relation to §3.23 (Plan 54) — Rule R F2

Plan 54 (REVIEWED) proves the same statement on 1 < r < 3 (Theorem RII_x1, under (H_an^{x1}): strip |Im u| ≤ π/2; both hypotheses
hold for RedA's entire L₁, so the corollaries coincide) by Route II directly in RH_px's unsymmetrized x-frame at p = 1.
- **Independent here:** the global frame (WLXZ's symmetric chain + Lemma P + the fold, versus RH_px at p = 1 with Lemma X1 and its
  transfer table); the outer model (Lemma FN versus RH_px's p = 1 outer model); the Airy disc (fold of Plan 50 / WLXZ §6.1 at +2,
  versus RH_px's at b); the lip mismatch (LW1₁'s even-pairing Szegő integral × the x^α factor, versus LW1-x1 = LW1′ with ν = ½); the
  equilibrium input (WLXZ's ψ, versus G2 μ*/B* at p = 1). The "no jump on ℝ₋" of FJ(c) is the folded form of Plan 54's Lemma X1;
  nothing is continued across ℝ₋, so Plan 54's Lemma X2 obstruction is not triggered.
- **Shared (a common failure point for both at r = 2):** ROUTE2's α_x = 0 hard-edge comparison — H1′, the log local form §3.2,
  **Lemma W′**, **UR′(a), (b′), (d)**, C′, D′ with the log² bound (Plan 48); KMVV §6 (Bessel model, (6.28), angle freedom); C–D
  Theorem 4.4 and the arguments of 4.7/4.9; RH_px's invariance lemma and (Y4)_x argument; RedA; §3.21 SH-r; WLXZ v1 (which Plan 54
  uses through RH_px §§3–5). A failure of ROUTE2's α_x = 0 comparison would sink both proofs.
- **Numerics:** `check_bnd_coeff.out` and Plan 54's `check_x1_coeff.out` are the same computation and agree in every printed
  digit for n ≤ 800; they validate the law, not either route. So this file independently cross-validates the global frame, not
  the α_x = 0 local comparison on which GAP-int rests.

---

## 4. Corollaries (second proof of §3.23's)

**Corollary B_{p=1}^{bnd,ᶠ}** (second proof of §3.23's B_{p=1}^{x}). p = 1, 1 < r < 3, Ψ > 0 slowly varying in sequence form (no boundedness, no D(γ) < ∞): nb_n(k^{−r}Ψ) → ½
and na_n(k^{−r}Ψ) → 1, with rate O(1/n + ρ(⌈n/M₀⌉)), and O(1/n) if Ψ itself satisfies (H_an₁). *Proof:* RedA (ROUTE2 §1; stated
for every p > 0, s > 1 and every strip, checked at p = 1 in ROUTE2_p1 §1) gives L₁ with (H_an₁) and the base change (iii);
Theorem RII₁ᶠ gives the law for k^{−r}Ψ₁. ∎

**Corollary B_{p=1}^{all,ᶠ}** (second proof of §3.23's B_{p=1}^{all}; GAP-int is closed by §3.23). p = 1, **every r > 1**, Ψ sequence-form slowly varying (incl. D(γ) = ∞, e.g.
exp √log(k + e), exp((log k)^θ), θ < 1): the full pointwise Law P nb_n → ½, na_n → 1, with rate O(1/n) under (H_an₁) and in general
O(r_n), r_n the regular majorant of 1/n + ρ(⌈n/M₀⌉). *Proof:* r₀ := r − j with j ≥ 0 the least integer such that r − j < 3; then
r₀ ∈ (1, 3) (r₀ ≥ 2 if j ≥ 1). B_{p=1}^{bnd,ᶠ} at r₀, then j applications of PROOF.md §3.21's Theorem SH-r (x·σ_{r′} = σ_{r′+1} at
x_k = 1/k). ∎ In particular r = 2, 3, 4, … with D(γ) = ∞ (GAP-int) is covered a second time. (Equivalently: B_{p=1}⁺ for non-integer r,
and r = 2 from RII₁ᶠ plus SH-r for r = 3, 4, …; the converse CT₁ "⟸" is not needed.)

*Remark (β_n)* — PROVED (CT₁(ii) "⟸" + Lemma D(b), REVIEWED; no rate; Rule R F7). The individual symmetric coefficients satisfy
nβ_n → 1 as well: given the law for μ, a_m = β_{2m−2} + β_{2m−1}, b_m² = β_{2m−1}β_{2m} (Plan 50's 1-based convention; 0-based, as
in check_bnd_fold [1]: a_j = β_{2j} + β_{2j+1}, b_j² = β_{2j−1}β_{2j}) with β_j > 0 is the Cholesky system of CT₁(ii) "⟸" (u = β_{odd}, v = β_{even}), and Lemma D(b) applies (no
rate). Not needed for the law.

**Status of OBSTRUCTION-a (Plan 50).** It stands as stated (the symmetric band-centre C–D frame needs |a| < ½), but it is an
obstruction of that frame — of reading the law through β_n — not of the problem: in the folded frame the same comparison works
for |a − ½| < 1.

---

## 5. The hybrid route (interpolation in r) — recorded, not used

**Lemma IR (PROVED, from FV⁺ of PROOF.md §3.14).** For 0 < δ < 1 and w_τ := k^{−2+τ}Ψ (x_k = 1/k):
|log b_n²(w_0) − log b_n²(w_δ)| ≤ δ·sup_{τ∈[0,δ]}Σ_k|log(k/n)|(μ_n^{(τ)} + μ_{n−1}^{(τ)})(k).
*Proof.* FV⁺ with v = w_0, f = δ log k (U_k = k^{−2}Ψ(k)k^δ(1 + δ log k) summable by Potter) gives (d/dt)log b_n² = ⟨f, μ_n − μ_{n−1}⟩;
replace f by δ log(k/n) (μ_n, μ_{n−1} are probability measures). ∎
With B_{p=1}⁺ at r = 2 − δ (non-integer), this reduces the law at r = 2 to limsup_n sup_τ Σ_k|log(k/n)|μ_m^{(τ)}(k) < ∞ for
some δ > 0 — a log-moment localization (QL-type, §3.14) for D(γ) = ∞ weights, uniform as a → ½, where RII₁'s constants blow up
(Lemma W's constant ≍ 1/(1 − 2|a|)). That is as hard as QL (open). A Theorem-L-type Grönwall from a log-type base (T3-log) at
r = 2 meets the same commutator term (Plan 49's CB). HEURISTIC; superseded by §§2–4.

---

## 6. Numerics (NUMERICAL)

`checks/check_bnd_coeff.out` (p = 1, w = k^{−r}exp √log(k + e), which satisfies (H_an₁) directly; atoms k ≤ K plus a Gauss–Legendre
tail to t_end; long-double RKPW; five truncations: K-doubling K = 1, 2, 4·10⁵ with t_end = 10¹⁶, and K = 2·10⁵ with t_end = 10¹⁴ or
with a finer tail quadrature):

| r (α_x) | n = 50 | 100 | 200 | 400 | 800 | 1600 | max spread (5 runs) |
|---|---|---|---|---|---|---|---|
| 2 (0): n(nb_n/c − 1) | −0.382 | −0.389 | −0.396 | −0.402 | −0.407 | −0.411 | 4.7·10⁻⁸ |
| 2: pure power | −0.493 | −0.497 | −0.498 | −0.499 | −0.500 | −0.500 | |
| 2: n(a_n/(2b_n) − 1) | 0.487 | 0.494 | 0.497 | 0.498 | 0.499 | 0.500 | 6.6·10⁻⁸ |
| 2.5 (½): n(nb_n/c − 1) | −0.628 | −0.637 | −0.645 | −0.651 | −0.656 | −0.661 | 5.2·10⁻⁹ |
| 3 (1; via SH-r): n(nb_n/c − 1) | −0.875 | −0.886 | −0.894 | −0.901 | −0.906 | −0.911 | 3.7·10⁻⁹ |

The K-doubling differences are ≤ 6·10⁻¹⁰ (nB) and ≤ 1.1·10⁻⁹ (E). All columns are bounded (rate O(1/n), as Theorem RII₁ᶠ and
B_{p=1}^{all,ᶠ} assert). They coincide with Plan 54's check_x1_coeff (same computation; §3.8). The
values sit on the tilted baseline −(r − 1 − ϑ_n)/2 (r = 2, n = 1600: −0.408 vs −0.411; ϑ_n = L′(log n)); the tilt ratio
T = n(b_n(w)/b_n(k^{−r}) − 1)/ϑ_n = 0.472 → 0.485 (r = 2), 0.475 → 0.485 (r = 2.5), 0.477 → 0.485 (r = 3), rising slowly toward ½
(tilt law, CONJECTURE; GAP-rate₁).

`checks/check_bnd_fold.out`: [1] Lemma F0 to 10⁻³⁹; [2] Lemma P's scalar parities: g(−z) − g(z) = −iπ is a genuine numerical check (4·10⁻¹⁰); the D-even and D̂(−z) = D̃(z) lines are
tautological (both sides evaluate the same expression) — those parities rest on the analytic branch argument of §2.2(c) (Rule R F9);
[3] Lemma FN: constant [[1, 0], [−i, 1]] to 10⁻³⁹ (a = 0.5, 0.8, 0.1); [4] the local amplification of the model factors (KV Ψ_½ vs KMVV Ψ_0; it does not probe the folded problem itself; no end-to-end
probe of the folded frame was run): unfolded (KV, a = ½) |·||ζ| =
→ 1/π (5 digits) as |ζ| → 0 (the non-integrable 1/ζ of §1.3), folded (KMVV, α = 0) |·|/(1 + log²|ζ|) ≤ 0.126; det Ψ = 1 to 10⁻⁴⁰ in both.

---

## 7. Rule A (adversarial pass; logged in ../../LOG.md), gaps

- (a) **Ψ ≡ 1:** RII₁ᶠ reduces to another proof of the (a_n, b_n) part of RH₁(r) for 1 < r < 3 (besides RH₁(r) itself and Plan 54's RII_x1 at
  Ψ ≡ 1); consistent with RH₁(r) and
  with the pure-power column of §6 (−(r − 1)/2).
- (b) **n odd:** Lemma P fails (e^{−ng(−z)} = −e^{−ng(z)}); the fold of Y_ν^{(2m+1)} is the xμ-problem. Only n = 2m is used, which
  gives every m. Not a gap.
- (c) **Sign on Ω^△:** R and T are σ₃-even only up to −1 on Ω^△; checked that WLXZ's V^△± is odd and cancels it (§2.2), so Q_W, V
  are exactly σ₃-even. A missed sign would make fold V two-valued across the images of ∂Ω^△; it does not occur.
- (d) **The fold factors z^{±1} on long pieces** (|z| ≤ k_n ≍ √n) cost poly(n), absorbed by e^{−cn} (as RH₁(r)'s n^{|a|}).
- (e) **Is the folded problem really ROUTE2's?** Checked item by item: band constant jump (FJ(a)); lips with the continued weight and
  phase e^{−4(n²f_K)^{1/2}} (FJ(b), Fφ); no jump on ℝ₋ (FJ(c)); outer model the [0, 4] solution (FN); conformal map with f_K′(0) < 0
  and reversed ordering (Fφ); (Y4)_x (FY). ROUTE2's only RH_px-specific inputs at the hard edge are these, plus the Hölder bound
  RH_px Lemma 3.4 for h_N (here replaced by LW1₁, which bounds the whole non-FH ratio D_ϱ²/ϱ).
- (f) **Does LW1ᶠ need the even pairing?** Yes, through LW1₁ (the symmetric Szegő integral); in x it is the statement that the far
  part of the [0, 4] Szegő integral is damped by R_x(x) ~ x^{1/2}, as in ROUTE2 §3.3 — consistent.
- (g) **α = 0 exactly (r = 2):** ROUTE2's log case (Lemma W′, the K-term log² HS bound, D′'s log²) is used; ROUTE2 proved UR′ for
  α = 0 (and REVIEW_Plan48's F1 extended (b′) to all |α| < 1). No new estimate is needed at α = 0.
- (h) **Does anything need |a| < ½?** Only Plan 50's symmetric-frame steps (UR₁, D₁), which are not used here. Plan 50's non-local
  ingredients used on 1 < r < 3 — W1(r) with the q_n factors, the Airy discs with ϱ₁ = |x|^{2a}q_n, the (J2) bounds, LW1₁ — do not use
  |a| < ½: RH₁(r) holds for every r > 1, LW1₁'s proof involves only h_W, H_n, q_n, and ϱ₁ is analytic near ±2 for every a (Rule R F10).
- (i) **Consistency with Remark Div:** the coefficients extracted in x are (Q^x₁)₁₂ = (Q₁)₁₂ and (Q^x₁)₂₁ = (Q₃)₂₁ − (Q₁)₂₁(Q₂)₁₁
  (from the normalization [[1, 0], [−(Q₁)₂₁, 1]] and Γ = 1 + γ₁/x + …; the γ₁ terms cancel), and (Q^x₂); never (Q₁)₂₁ alone. The
  symmetric-frame C–D representation of (Q₁)₂₁ − (Q̃₁)₂₁, which fails at a = ½ (§1.3; consistent with OBSTRUCTION-a), is not used:
  the folded C–D integrals are absolutely convergent (log² at α = 0).
- (j) **Counter-check by a non-symmetric Ψ:** the symmetrized measure is even by construction for every Ψ; Lemma P does not
  depend on Ψ beyond evenness of q_n. No counterexample.

**Remaining.** GAP-rate₁ (the 1/n coefficient; tilt law CONJECTURE, §6). The O(1/n) rate holds for every r > 1 under (H_an₁). The
symmetric-frame OBSTRUCTION-a stands as scoped. GAP-int itself is closed by §3.23; this file is a second proof.
