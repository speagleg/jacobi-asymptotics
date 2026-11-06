# CG — the Christoffel function of σ_{p,s} at the accumulation point 0 (exact CG/MINRES constant)

Agent CG, branch `g1-constants`, 2026-11-05. Proof note; checks in `checks/`.

**Status summary.**

| Part | Statement | Label |
|---|---|---|
| A | Conjecture CG for every **p ≠ 1** and every **s > 1**, with relative error O(1/m) | **PROVED-mod-cite + REVIEWED** (review/REVIEW_CG_R1.md; Paper II Props. `prop:classical`, `prop:plt1-small`, Lemmas `lem:classical-param`, `lem:plt1-param`, `lem:bandfactor`, `lem:plt1-band`, Prop. `prop:frame`; through them KMVV §6 and DLMF) |
| L | Localisation lemma: λ_m(0; gμ)/λ_m(0; μ) → 1 if g → 1 at 0 (comparable weights, compact Jacobi matrices) | **PROVED + REVIEWED** (elementary, self-contained); novelty PARTIALLY KNOWN: Nevai's comparison principle; the accumulation-point setting not found as a statement (NOVELTY_CG.md §3) |
| B | Conjecture CG at **p = 1, s ∈ {3/2, 5/2}** (relative error o(1)) | **PROVED-mod-cite + REVIEWED** (review/REVIEW_CG_R1.md; Paper II Lemma `lem:pone-tc` ← Carlitz/WLXZ (1.4)–(1.9); DLMF 4.13.1, 4.13.2, 4.13.5, 5.5.1, 5.11.1) |
| C | Conjecture CG at **p = 1 for every s > 1**, relative error O(1/m) (closes GAP-1 of §6) | **PROVED-mod-cite + REVIEWED** (review/REVIEW_CG_R2.md; §9; Paper II Prop. `prop:pone-first`, Lemmas `lem:pone-weight`, `lem:pone-fh`, `lem:pone-mismatch` ← WLXZ, KV §5, Van §4; inherits Paper II's stated dependence on WLXZ (5.8), (6.34) and the Cauchy-operator bound after (6.35)) |
| Cor E2.7 | the exponent E for p > 1 (C unspecified) was already in second_order/E2_pgt1.md Cor E2.7 (REVIEWED) | see §10 (REVIEWED, R2): new here are the explicit C, the O(1/m) rate, p < 1 and p = 1 |
| F7 | λ_m = C·N^{−E}(1 + o(1/m)), N = m + (s−1)/(2p) | **CONJECTURE (NUMERICAL)** (review R1 F7, R2 at p = 1; §10) |
| — | "even in 1/N with rational e₂" | not addressed (NUMERICAL only, `checks/check_lambda_n80.out`) |

Rule R: §§0–5, 7–8 REVIEWED in review/REVIEW_CG_R1.md (no errors, no serious gaps; fixes F1–F7 applied 2026-11-05, see LOG).
§9 (Theorem C) and §10 REVIEWED in review/REVIEW_CG_R2.md (no errors, no gaps; nits N1–N5 applied 2026-11-05).
Novelty (Rule L, 2026-11-06, NOVELTY_CG.md): constant POSSIBLY-NEW pending Hanke, Numer. Algorithms 11 (1996) (unread); the upper bound O(m^{−E}) for every p > 0 follows from Velikanov–Yarotsky Thm 4.10; N-centring NOT FOUND.

---

## 0. Statement

σ = σ_{p,s} = Σ_{k≥1} k^{-s} δ_{k^{-p}}, p > 0, s > 1, monic OPs P_k, h_k = ∫P_k² dσ,
K_m(x,y) := Σ_{k<m} P_k(x)P_k(y)/h_k, λ_m(0) := min{∫P² dσ : deg P < m, P(0) = 1} = 1/K_m(0,0).
c = c(p) = ¼(π/(2I(p)))^p, I(p) = (√π/2)Γ(1/p+½)/Γ(1/p+1); ζ := (s−1)/p, E := (p+2)ζ; Bessel order
α := (s−1−p)/p = ζ − 1 > −1.

**Theorem A.** Let p > 0, p ≠ 1, s > 1. Then, as m → ∞,

  λ_m(0; σ_{p,s}) = (Γ(ζ)Γ(ζ+1)/p) · (c(p)(p+2)²)^ζ · m^{−(p+2)ζ} · (1 + O(1/m)).

Since N = m + (s−1)/(2p) = m(1+O(1/m)), this is Conjecture CG with N in place of m (same statement).

**Theorem B.** The same asymptotics (with 1+o(1)) hold for p = 1 and s ∈ {3/2, 5/2}.

**Theorem C (§9; PROVED-mod-cite + REVIEWED).** The same asymptotics, with 1 + O(1/m), hold for p = 1 and every
s > 1: λ_m(0; σ_{1,s}) = Γ(s−1)Γ(s)·(9/2)^{s−1}·m^{−3(s−1)}(1 + O(1/m)).

**Prior result (exponent only).** For p > 1 the exponent E = (p+2)(s−1)/p, with an unspecified constant C(p,s) > 0 and
error o(1), is second_order/E2_pgt1.md Corollary E2.7 (REVIEWED 2026-10-20); see also its Remarks E2.12 (CG reading) and
E2.13 (first-order route). What is new here: the explicit value of C (all p > 0), the rate O(1/m), and the ranges p < 1 and
p = 1. Comparison and consistency check in §10.

The constant is the hard-edge Bessel constant. Writing the local data of Paper II: the band weight is
W(z) = w_n z^α, w_n = −(2πi/p)n^{1+p−s} (Paper II Lemma `lem:bandweight`), the hard-edge map is f with
f'(0) = −π²C_*², C_* = (4c)^{−1/p−1/2}/(p a_* B(a_*,½)), a_* = 1/p+½ (Paper II Prop. `prop:equilibrium`(iii),
Lemma `lem:signs`(iii)), and the proof gives the exact leading identity

  K_n(0,0) = p |f'(0)|^{α+1} n^{(p+2)(α+1)} / (Γ(α+1)Γ(α+2)) · (1 + O(1/n)),        (★)

together with |f'(0)| = 1/(c(p)(p+2)²) (identity (I1) below). This is precisely the brief's "Laguerre-calibrated"
heuristic λ ≈ W Γ(a+1)Γ(a+2) D^{−2(a+1)} with W = 1/p (the local density of σ: σ ≈ (1/p)x^{ζ−1}dx near 0) and
D² = n^{p+2}|f'(0)|.

## 1. Literature check (Rule L; queries recorded in LOG below)

* **Hanke, Numer. Algorithms 11 (1996) 203–213** ("Asymptotics of orthogonal polynomials and the numerical solution of
  ill-posed problems", DOI 10.1007/BF02142497). Only the abstract/MaRDI record was accessible: it is a review of the
  ν-method and CG for ill-posed problems, uses Tricomi–Carlitz and modified Lommel polynomials as CG prototypes, and
  relates Christoffel-function asymptotics to a saturation result for the ν-method. Full text NOT read; we cite nothing
  from it. Our Part B (Tricomi–Carlitz) is in the same spirit; whether Hanke states the TC Christoffel constant is
  UNCHECKED.
* **Velikanov–Yarotsky, JMLR 25 (2024) no. 81** (arXiv:2202.00992). Abstract read: rates O(n^{−ξ}) with ξ = (2+ν)ζ for
  CG under power-law spectral conditions, with tight lower bounds. These are exponents (our E = (p+2)ζ in their
  notation ν ↔ p), not exact constants. Nothing used.
* **Lubinsky, hard-edge universality for compactly supported measures** (lubinsky.math.gatech.edu,
  "UniverseHardEdge2008"); **Totik / Lubinsky, varying weights**; **Danka–Totik** (power-type weights on arcs,
  JEMS 2018). All concern measures that are absolutely continuous near the edge on a FIXED support (regular in the
  Stahl–Totik sense, with a Jacobi-type weight at the endpoint). σ_{p,s} is purely atomic with support {k^{-p}} ∪ {0}
  of capacity 0 and is not of that class; after the rescaling z = n^p x it is a varying discrete weight with a
  saturated region (Paper II §4). We found no theorem in these sources that contains σ_{p,s}. Answer to the brief's
  question: the Laguerre-calibrated heuristic is a theorem here only through the RH analysis of Paper II (Part A).
* **Internal prior result: second_order/E2_pgt1.md Cor E2.7** (REVIEWED): λ_n(0; σ_{p,s}) = C n^{−(p+2)(s−1)/p}(1+o(1))
  for p > 1, s > 1, C unspecified, via the Hankel ratio λ_n = D_n(σ)/D_{n−1}(x²σ) and third-order recurrence asymptotics
  (Thm E2.1) plus UL Thm UF-lim. It gives the exponent of Theorem A for p > 1 but not C (the global constant from summing
  log h_j(s) − log h_j(s+2p) is not evaluated — this is exactly obstruction O1 in §7). Remarks E2.12–E2.13: §10.
* **Lemma L, novelty (review F6).** Lemma L is a comparison/localisation principle of the Máté–Nevai–Totik type for
  Christoffel functions; we have not checked whether this exact version (point 0 at the edge of an atomic support,
  hypothesis a_k, b_k → 0) is in the literature. Novelty UNCHECKED; the PROVED label is unaffected.
* Kuijlaars–Vanlessen (hard-edge/origin universality via RH) are the template for §3; we use only what Paper II
  already cites (KMVV §6, quoted in research/G1/RH/CITATIONS.md and Paper II §2.4).

## 2. The ingredients from Paper II (all for ℓ ≡ 1)

Notation of Paper II §§4–5, 8, 10 (labels refer to papers/paperII/*.tex). Degree n = m.

(P1) `lem:interp`, `eq:U`: U(z) = n^{pnσ₃} Y(z n^{−p}); Y₁₁ = P_n, Y₂₁ = P_{n−1}/h_{n−1}.
(P2) `eq:VM`, `eq:Q`: in Ω_∞, V = C_∞ e^{−nγ_pσ₃} U e^{nφσ₃} F^{σ₃}, Q = D_∞^{−σ₃} V D_W^{σ₃}, with C_∞, D_∞ constants
     (scalar)^{σ₃}.
(P3) `eq:Pcheck`, `eq:error-matrix`: in U₀ = D(0,δ), 𝖱 = Q P̌₀^{−1}, P̌₀ = Ǎ (2πn)^{σ₃/2} Φ_α(n²f) ρ_n^{−σ₃},
     ρ_n = W̃/D_W, Φ_α = σ₃Ψ_ασ₃ e^{−2ζ^{1/2}σ₃}; W̃ = w_n^{1/2}(−z)^{α/2}(4c−z)^{1/2}e^{−G} (`eq:Wtilde`,
     `eq:plt1-Wtilde`), with G = −j(t) + log B (p>1, `eq:G-def`), G = ½Log(1−z/(2πn)) + χ in S_out (p<1,
     `eq:plt1-G`).
(P4) `lem:outer`, `lem:seam`(iv): F = DBK, D = υ_±D̃, D̃ = e^{−j(t)}, K = (4c−z)^{−1/2} (p>1); F = B_out K e^χ in S_out,
     B_out = (1−z/(2πn))^{1/2} (p<1).
(P5) `lem:classical-param`(i), `lem:plt1-param`(i): det Ǎ = 1, Ǎ = Ǎ^a + Ǎ^s on D(0,δ), Ǎ^a analytic, |Ǎ^{±1}| ≤ C;
     Ǎ^s the Cauchy integral over (−2δ,0) (p>1), resp. the two seam segments (p<1), of a density d with
     |d(w)| ≤ C|w|^{−1}·e^{−c n|w|^{−1/p}} (from the bounds |Ǎ| ≤ C|z|^{−1/2} and `eq:A-jump`, resp. its seam analogue,
     with |𝔢|, 𝔧 ≤ π e^{−c n|w|^{−1/p}}). The crude bound |Ǎ| ≤ C|z|^{−1/2} on D(0,δ) off the cuts: by `eq:Pcheck`,
     Ǎ = P^∞₀ρ_n^{σ₃}Mf^{σ₃/4} with M constant; |P^∞₀| ≤ C|z|^{−1/4} near 0 (`eq:Pinf0-bound`); |ρ_n^{±1}| ≤ C
     (`lem:classical-param`(i) for p>1, `eq:plt1-rho-mod` for p<1, with boundary values); |f| ≍ |z| (f conformal,
     f(0) = 0), so |f^{±1/4}| ≤ C|z|^{−1/4}. Hence |Ǎ| ≤ C|z|^{−1/2} for p<1 as well (review F2).
(P6) `prop:classical`(ii)–(iv), `prop:plt1-small`: 𝖱 = I + 𝒞(𝖱₋(J_𝖱 − I)) off Σ_𝖱; ‖𝖱₋ − I‖_{L²(Σ_𝖱)} ≤ C/n;
     |J_𝖱 − I| ≤ C/n on the circles, ≤ Ce^{−n/C} on the far arcs (total length O(n^p)), and
     |J_𝖱 − I| ≤ C_K n^{−K} min(1,|w|^K) on Σ_𝖱 ∩ U₀ (lips, and (−δ,0) for p>1, seam segments for p<1).
(P7) Geometry: inside D(0,δ) the lips satisfy ¾θ_lip ≤ |arg z| ≤ (5/4)θ_lip with θ_lip = π/3 (p>1) or πp/4 (p<1);
     seams at arg z = ±πp/2 (p<1); f conformal, real, f(0)=0, f'(0) < 0, φ = ∓iπ − 2f^{1/2} in ℂ_± (`lem:signs`(iii)),
     hence e^{nφ} = (−1)^n e^{−2ζ^{1/2}} with ζ = n²f (`eq:he-ephi`).
(P8) Bessel model: in the central sector |arg ζ| < π − θ_lip, Ψ_α e₁ = (I_α(2ζ^{1/2}), 2πiζ^{1/2}I_α'(2ζ^{1/2}))ᵀ
     (KMVV (6.23), quoted in Paper II §2.2(a)); DLMF (10.25.2) series for I_α.

Paper II's own status: these items are proved in Paper II with the external results listed in its §§2.3–2.6 (KMVV §6,
Conway–Deift Thm 4.4 for −1<α≤−½, DLMF). We inherit those labels; we re-prove nothing in Paper II.

## 3. Proof of Theorem A

Fix p ≠ 1, s > 1, n = m ≥ n₀. Put X = n^p x. All points below are X = iy with 0 < y ≤ δ/4.

**S1 (kernel in U-variables).** By Christoffel–Darboux and (P1),
K_n(x,y) = [Y₁₁(x)Y₂₁(y) − Y₂₁(x)Y₁₁(y)]/(x−y) = n^p [U₁₁(X)U₂₁(Y) − U₂₁(X)U₁₁(Y)]/(X−Y), so with
u := (U₁₁, U₂₁)ᵀ (a vector of polynomials)

  K_n(0,0) = n^p det[u'(0), u(0)].                                               (1)

**S2 (first column through Q).** Points iy lie in Ω_∞ (outside the lens: the lips stay in |arg z| ≤ 5θ_lip/4 < π/2),
off all contours, in ℂ_+, and for p<1 in S_out (π/2 > πp/2). By (P2), U = 𝖬 Q D_W^{−σ₃}F^{−σ₃}e^{−nφσ₃} with
𝖬 = e^{nγ_pσ₃}C_∞^{−1}D_∞^{σ₃} constant, diagonal, det 𝖬 = 1. Hence u = 𝖬 Qe₁ /(D_W F e^{nφ}). By (P3), (P7),
Qe₁ = 𝖱Ǎ(2πn)^{σ₃/2}Φ_α(ζ)e₁ ρ_n^{−1} and Φ_α(ζ)e₁ = e^{−2ζ^{1/2}}σ₃Ψ_α(ζ)e₁, e^{−nφ}e^{−2ζ^{1/2}} = (−1)^n, so

  u(X) = (−1)^n 𝖬 𝖱(X)Ǎ(X)(2πn)^{σ₃/2} σ₃Ψ_α(ζ)e₁ / (F(X)W̃(X)).                  (2)

**S3 (the scalar F W̃ is explicit).** p>1, ℂ_+: F W̃ = υ₊e^{−j}B(4c−z)^{−1/2} · w_n^{1/2}(−z)^{α/2}(4c−z)^{1/2}e^{j}B^{−1}
= υ₊ w_n^{1/2}(−z)^{α/2}. p<1, S_out: F W̃ = B_out e^χ(4c−z)^{−1/2} · w_n^{1/2}(−z)^{α/2}(4c−z)^{1/2}B_out^{−1}e^{−χ}
= w_n^{1/2}(−z)^{α/2}. (Exact pointwise cancellation: the n-dependent scalar functions B (Binet-cut factor) and χ (seam factor) cancel
identically in z, and the constants H_n(0⁺), D_∞, k_∞ cancel with them. Check (I4).) Structurally: W̃² = e^{∓iπα}W/F̃² and F = υF̃, so (W̃F)² = υ²w_n(−z)^α.

**S4 (the Bessel column).** By (P8) and DLMF (10.25.2), σ₃Ψ_α(ζ)e₁ = ζ^{α/2} b̂(ζ) with b̂ entire,
β₁(ζ) = Σ_k ζ^k/(k!Γ(α+k+1)), β₂(ζ) = −πi Σ_k (α+2k)ζ^k/(k!Γ(α+k+1)). For X = iy, arg(−X) = −π/2 and
arg ζ = −π/2 + O(y) (f'(0) < 0), so the principal powers combine: (−X)^{−α/2}ζ^{α/2} = (n²F₁(X))^{α/2} with
F₁(X) := f(X)/(−X) analytic near 0, F₁(0) = |f'(0)| > 0. Thus, with c(X) := (2πn)^{σ₃/2}b̂(ζ(X)), N := 𝖱Ǎ,

  u(X) = s(X) 𝖬 N(X) c(X),   s(X) := (−1)^n w_n^{−1/2} (n²F₁(X))^{α/2} υ(X)^{−1}   (υ := 1 for p<1).   (3)

**S5 (determinant).** det 𝖬 = det N = 1, so det[u',u] = s²(det[c',c] + det[Bc,c]) with B := N^{−1}N'. Here
det[c',c] = ζ'(X)(β₁'β₂ − β₂'β₁)(ζ) (the factors (2πn)^{±1/2} cancel), and at ζ = 0
β₁'β₂ − β₂'β₁ = 2πi/(Γ(α+1)Γ(α+2)) (check (I2)). For any matrix B, det[Bc,c] = (B₁₁−B₂₂)c₁c₂ + B₁₂c₂² − B₂₁c₁², and
c₁ = (2πn)^{1/2}β₁, c₂ = (2πn)^{−1/2}β₂, so |det[Bc,c]| ≤ C|B| n uniformly for |ζ| ≤ 1.

**S6 (uniform bounds along iy, the only analytic input).** For 0 < y ≤ δ/4:
 (a) |𝖱(iy) − I| ≤ C/n and |𝖱'(iy)| ≤ C/n, with C independent of n and y.
 Proof: 𝖱(z) − I = (2πi)^{−1}∫_{Σ_𝖱} h(w)dw/(w−z), h = (J−I) + (𝖱₋−I)(J−I) (P6). On the circles and far arcs
 |w − iy| ≥ δ/2, so these parts and their z-derivatives are ≤ C(‖J−I‖_{L¹} + ‖𝖱₋−I‖_{L²}‖J−I‖_{L²}) ≤ C/n. On
 Σ_𝖱 ∩ U₀ every w has |arg w| ≤ 5θ_lip/4, or |arg w| = πp/2 (p<1), or arg w = π (p>1), so the angle between w and iy is
 ≥ min(π/12 [lips, p>1], π/2 − 5πp/16 ≥ 3π/16 [lips, p<1], π(1−p)/2 [seams, p<1], π/2 [(−δ,0), p>1]) and
 |w − iy| ≥ κ|w|, κ > 0. With |J−I| ≤ C_K n^{−K}|w|^K there,
 ∫|h(w)||w−iy|^{−j}|dw| ≤ C_K n^{−K}(∫|w|^{K−j}|dw| + ‖𝖱₋−I‖_{L²}(∫|w|^{2K−2j})^{1/2}) ≤ Cn^{−K} for j = 1,2, K = 3.
 (b) |Ǎ^{±1}(iy)| ≤ C (P5) and |Ǎ'(iy)| ≤ C: Ǎ^a is analytic and bounded on D(0,δ), so |Ǎ^{a\prime}| ≤ C on D(0,δ/2);
 |Ǎ^{s\prime}(iy)| ≤ ∫|d(w)||w − iy|^{−2}|dw| ≤ C∫₀^{2δ} r^{−3}e^{−cnr^{−1/p}}dr ≤ Ce^{−n/C} (|w − iy| ≥ κ|w| again).
 Hence |B(iy)| ≤ |Ǎ^{−1}||𝖱^{−1}||𝖱'||Ǎ| + |Ǎ^{−1}Ǎ'| ≤ C, uniformly in y.

**S7 (limit y → 0).** u, u' are polynomial, so by (1), (3), S5:
K_n(0,0) = n^p lim_{y→0} s(iy)²(det[c',c](iy) + det[Bc,c](iy)). As y → 0: υ(iy)^{−1} = 1 − e^{−2iθ(iy)} → 1
(|e^{−2iθ}| = exp(−2πn y^{−1/p}sin(π/(2p))), p>1), F₁(iy) → |f'(0)|, ζ(iy) → 0, ζ' → n²f'(0); so
s² → w_n^{−1}(n²|f'(0)|)^α, det[c',c] → n²f'(0)·2πi/(Γ(α+1)Γ(α+2)), and limsup|det[Bc,c]| ≤ Cn. Therefore

  K_n(0,0) = n^p w_n^{−1}(n²|f'(0)|)^α [ n²f'(0)·2πi/(Γ(α+1)Γ(α+2)) + O(n) ].

With w_n^{−1}·2πi·f'(0) = p|f'(0)|n^{s−1−p} = p|f'(0)|n^{pα} this is (★).

**S8 (the constant).** B(a_*,½) = √πΓ(1/p+½)/Γ(1/p+1) = 2I(p), so p a_* B(a_*,½) = (p+2)I(p); and
(4c)^{−1/p} = 2I(p)/π. Hence C_* = 1/(π(p+2)√c), |f'(0)| = π²C_*² = 1/(c(p+2)²) (check (I1), also by quadrature of
ψ* independently of the formula for C_*). Inserting into (★) with α+1 = ζ:
λ_n(0) = 1/K_n(0,0) = (Γ(ζ)Γ(ζ+1)/p)(c(p+2)²)^ζ n^{−(p+2)ζ}(1+O(1/n)). ∎

**Remark (by-product, step S7 refined).** The same computation with det[u(X),u(0)] gives the extremal polynomial
profile P*_m(x) = K_m(x,0)/K_m(0,0) → Γ(α+2) w^{−(α+1)/2} J_{α+1}(2√w), w = m^{p+2}|f'(0)| x (bounded w); not used,
but checked numerically (it is an independent test of S4–S7, see §5).

## 4. Localisation lemma and Theorem B (p = 1)

**Lemma L.** Let μ, μ' be finite positive measures on [0, A] with infinite support, μ' = gμ with c₁ ≤ g ≤ c₂ on supp μ
(0 < c₁ ≤ c₂) and g(x) → 1 as x → 0 along supp μ. Assume the recurrence coefficients a_k, b_k of μ and of μ' tend to 0,
and λ_m(0;μ) → 0. Then λ_m(0;μ')/λ_m(0;μ) → 1.

*Proof.* (i) Let ν ∈ {μ, μ'}, p_k its orthonormal polynomials, v_k := p_k(0), S_m := Σ_{k<m}v_k² = 1/λ_m(0;ν);
S_m → ∞ for ν = μ by hypothesis, and for ν = μ' because λ_m(0;μ') ≤ c₂λ_m(0;μ). The minimiser is
P*(x) = Σ_{k<m}v_kp_k(x)/S_m, and ε_m(ν) := ∫xP*²dν/∫P*²dν = vᵀJ_mv/S_m, J_m the m×m Jacobi matrix (since
∫x p_jp_k dν = (J)_{jk}). By 2|v_kv_{k+1}| ≤ v_k² + v_{k+1}², vᵀJ_mv ≤ Σ_{k<m}(a_k + b_k + b_{k+1})v_k², and since
a_k+b_k+b_{k+1} → 0 and S_m → ∞, ε_m(ν) → 0 (Toeplitz: split at k₀ with the sup of the null sequence beyond k₀ ≤ η).
(ii) Given η > 0 pick δ_η with |g − 1| ≤ η on (0, δ_η]∩supp μ; then g ≤ 1 + η + (c₂/δ_η)x and
1/g ≤ (1−η)^{−1} + (1/(c₁δ_η))x on supp μ. Testing the μ-minimiser in the μ'-problem:
λ_m(0;μ') ≤ λ_m(0;μ)(1 + η + (c₂/δ_η)ε_m(μ)); testing the μ'-minimiser in the μ-problem:
λ_m(0;μ) ≤ λ_m(0;μ')((1−η)^{−1} + ε_m(μ')/(c₁δ_η)). Let m → ∞, then η → 0. ∎

(Remark: for compact support accumulating only at 0, a_k, b_k → 0 automatically — the Jacobi operator is then compact —
but we do not use this; in the applications both measures have known coefficients.)

**Theorem B, proof.** Tricomi–Carlitz data (Paper II Lemma `lem:pone-tc`(a),(b), from Carlitz's theorem as quoted in
WLXZ (1.4)–(1.6), (1.9); quotes in research/G1/RH/CITATIONS.md "WLXZ"): σ_TC := Σ_{j≥1}v_jδ_{1/j},
v_j = j^{j−1}e^{−j}/j!, has b_k² = 1/(2k(2k+1)), u_k := −P_{k+1}(0)/P_k(0) = 1/(2k+2); xσ_TC has
b_k² = 1/((2k+1)(2k+2)), u_k = (2k+5)/((2k+2)(2k+3)); a_k, b_k = O(1/k) for both (and for σ_{1,3/2}, σ_{1,5/2} by
Paper II Cor. `cor:tc` / Cor. `cor:pure`).

*Total mass.* DLMF 4.13.1 (W e^W = z, W₀ the increasing solution with W₀ ≥ W₀(−1/e) = −1, 4.13.2) and 4.13.5
(W₀(z) = Σ_{n≥1}(−n)^{n−1}zⁿ/n!, |z| < 1/e) give Σ_n n^{n−1}xⁿ/n! = −W₀(−x) for 0 ≤ x < 1/e. The left side increases to
Σ_n n^{n−1}e^{−n}/n! as x ↑ 1/e (positive terms, monotone convergence), and the right side tends to −W₀(−1/e) = 1
(W₀ is the inverse of the continuous increasing map w ↦ we^w on [−1,0], hence continuous). So h₀(σ_TC) = Σv_j = 1, and
h₀(xσ_TC) = a₀(σ_TC)h₀(σ_TC) = ½.

*Exact kernels.* P_k(0) = (−1)^kΠ_{i<k}u_i, h_k = h₀Π_{i≤k}b_i², so
K_m(0,0;σ_TC) = Σ_{k<m}(2k+1)!/(4^kk!²) = (2m+1)!!/(3·(2m−2)!!) ~ 4m^{3/2}/(3√π),
K_m(0,0;xσ_TC) = Σ_{k<m}(2k+2)(2k+3)²(2k+1)!/(9·4^kk!²) ~ 32 m^{9/2}/(81√π)
(using (2k+1)!/(4^kk!²) = (2k+1)Γ(k+½)/(√πΓ(k+1)) ~ 2√(k/π), DLMF 5.11.1). [Note: an earlier draft of the check script
had the factor 2 instead of (2k+2); corrected and verified, check (T3).]

*Weights.* k^{−3/2} = √(2π)e^{j(k)}v_k (Paper II eq. `eq:pone-weight`, from DLMF 5.5.1, 5.11.1), with Binet's
j(k) ∈ (0, 1/12+1/360] and j(k) → 0. So σ_{1,3/2} = √(2π)·g·σ_TC and σ_{1,5/2} = xσ_{1,3/2} = √(2π)·g·xσ_TC with
g(1/k) = e^{j(k)}, 1 ≤ g ≤ e^{1/12+1/360}, g → 1 at 0. Lemma L (the constant √(2π) factors out exactly) gives
λ_m(0;σ_{1,3/2}) ~ √(2π)·3√π/(4m^{3/2}) = (3π√2/4)m^{−3/2} and λ_m(0;σ_{1,5/2}) ~ √(2π)·81√π/(32m^{9/2}) =
(81π/(16√2))m^{−9/2}. Conjecture CG at p = 1 (c(1) = ½): s = 3/2: Γ(½)Γ(3/2)(9/2)^{1/2} = 3π/(2√2) = 3π√2/4 ✓;
s = 5/2: Γ(3/2)Γ(5/2)(9/2)^{3/2} = (3π/8)(27/(2√2)) = 81π/(16√2) ✓. ∎

(Lemma L also gives, for free, CG with the factor L for any σ_{p,s,ℓ} with ℓ(k) → L > 0, ℓ bounded above and below, as
long as its recurrence coefficients tend to 0 — e.g. analytic ℓ by Paper II Thm `thm:analytic`. Not needed here.)

## 5. Numerical checks (Rule N) — all NUMERICAL, mpmath, precision doubling; none is a proof

| Check | Claim | Script / output | Result |
|---|---|---|---|
| I1 | \|f'(0)\| = π²C_*² = 1/(c(p+2)²) (S8), f'(0) from quadrature of ψ* | `checks/check_identities.py` → `.out` | quadrature: rel. err ~1e−9 (= O(x) at x=1e−8); closed form: 1e−41; p ∈ {.5,.7,1,1.5,2,3} |
| I2 | β₁'β₂−β₂'β₁ = 2πi/(Γ(α+1)Γ(α+2)); series b̂ = ζ^{−α/2}(I_α, −2πiζ^{1/2}I_α') (S4–S5) | same | exact to 1e−41, α ∈ {−.9,−.5,0,.3,1.7,4} |
| I3 | Laguerre calibration λ_n(0) = Γ(a+1)Γ(a+2)Γ(n)/Γ(n+a+1) | same | exact to 1e−41 |
| I4 | F W̃ = υ w_n^{1/2}(−z)^{α/2} (S3, branches) | same | 1e−41 |
| Λ | λ_m m^E/C → 1 for (2,3.5), (3,2.5), (.5,1.3), (.5,2.5), (1.5,4), (.7,1.2), (2,2), and p=1: s=1.5, 2, 2.5, 3.7; m ≤ 81 | `checks/check_lambda.py 80 800` → `check_lambda_n80.out` | raw r_m−1 = O(1/m) (m(r_m−1) stable); Richardson limits −1: 1e−22 (2,3.5), 1e−25 (3,2.5), 1e−29 (2,2), 3e−6 (.5,1.3), 4e−9 (1.5,4), 2e−7 (.7,1.2) [p<1 slower: n^{−1−p} terms]; p=1: 1e−17…1e−27 |
| Λ' | precision doubling (Rule N.3; review F5) | `checks/check_lambda.py 80 800` → `check_lambda_n80.out` (regenerated 2026-11-05: dps 800 vs 1600) and `checks/check_stability.py` → `check_stability.out` | max abs(r_m(800) − r_m(1600)) over m ≤ 81: 2e−61 (3,2.5), 1e−288 (2,3.5), 8e−400 (1.5,4), 4e−292 (2,2), ≤ 5e−508 for all p ≤ 1 pairs — far below the Richardson residuals; the Richardson values are unchanged from the earlier export (which already used dps 800) |
| Pr | profile K_m(x,0)/K_m(0,0) vs Γ(α+2)w^{−(α+1)/2}J_{α+1}(2√w) at w = 2.5 | `check_lambda.py` | difference halves from m=41 to m=81 for every pair (O(1/m)) |
| T1–T4 | Σv_j = 1; TC data re-derived from the moments Σ_j v_j j^{−i}; exact kernels and their leading constants; Lemma L ratio → 1 | `checks/check_tc.py` → `check_tc.out` | Σv_j−1 = −8e−62; b_k², a_k of σ_TC, xσ_TC match the quoted formulas to 5e−62 (k<20); closed forms exact; K_m(ν)m^{−E} at m=20000 vs √(2π)/C: 0.752267 vs 0.752253 (s=3/2), 0.222927 vs 0.222890 (s=5/2), i.e. O(1/m); λ_m(σ_{1,s})/(√(2π)λ_m(ν)) − 1 = 6e−4, 1.5e−4 (m=10,20; s=3/2) and 1.6e−3, 4.4e−4 (s=5/2), ~m^{−2} |
| P1 | WLXZ (2.1): ψ(0) = 1/(3π), f'(0) = 1/3; ∫ψ = 1 (§9 G5) | `checks/check_p1.py` → `check_p1.out` | 3πψ(10⁻⁵) − 1 = 7.5e−12 (= O(x²)); ∫ψ − 1 = −2e−31; f'(0) = 0.33333… to 25 digits |
| P2 | D(ir) = e^{j(N/r²)} from WLXZ (2.6), branch −1/z² = e^{πi}/z² (§9 G4(iv)) | same | 3e−57 (N ∈ {10,101}, r ∈ {.9,.3,.1}) |
| P3 | sector-II column (Van (4.27)) × W^{−1}, W = (−z)^a: lim det[w_r,w] = π(Nf'(0))^{2a+1}2^{−2a}/(Γ(a+½)Γ(a+3/2)) (§9 G4, G6) | same | 1.1e−14 at r = 1e−8 (= O(r²)), a ∈ {−.3,0,.5,1,2.2,3.5}, N ∈ {7,40}, linear and cubic odd f |
| P4 | assembly of E(0), 𝔳₀(0), e^L, κ, σ₃-sign, d/dz = −i d/dr into (C★) (§9 G8) | same | 3e−61 (s ∈ {1.2,1.5,2,2.5,3.7,5}, N ∈ {9,99}) |
| P5 | fold λ_m(σ_{1,s}) = λ_{2m−1}(ν_s) = λ_{2m}(ν_s) (§9 G1) | same | 3e−184, 1e−185 (s = 2.3, 1.2; m = 10; dps 200) |
| P6 | Theorem C: r_m = λ_m(σ_{1,s})(N³/36)^ζ/(Γ(ζ)Γ(ζ+1)), N = 2m−1, → 1 with O(1/m) | same (m ≤ 80, dps 400 vs 800) | Richardson(K=12) limit − 1: 8e−27 (s=1.2), 7e−27 (1.5), −7e−24 (2), −4e−21 (2.5), −1e−16 (3.7), −2e−13 (5); r_m − 1 halves from m = 40 to 80; dps diff ≤ 5e−110 |
| E2 | Theorem A (shifted form) vs E2_pgt1 Cor E2.7's numerical slopes (§10) | `checks/check_e2_consistency.py` → `.out` | residual −1e−5 … +2e−7, ~n^{−2}, at (1.5,2), (2,2), (2,3), (3,2); unshifted −E misses by up to 1.4e−2 |

Data provenance (Rule X): λ_m is computed from the exact moments ζ(s+jp) by the Chebyshev algorithm; the conjectured
constant is not fitted.

## 6. GAP-1 (p = 1, general s) — precise statement and the route

*Status: CLOSED by §9 (Theorem C; not yet reviewed). The text below is kept as written for the review record.*

At p = 1 Paper II has no classical hard-edge parametrix in the x-variable (Remark `rem:quotient-p1`); the analysis is
done in the symmetric variable y = x^{1/2} (Prop. `prop:pone-first`, App. H) with the Fisher–Hartwig parametrix
P₀ = 𝖡_NΨ^{FH}(Nf)W_𝔳^{−σ₃}e^{−Nφ^{KV}σ₃} at the interior point 0 and error matrix 𝖷 = VP₀^{−1}.
λ_m(0;σ_{1,s}) = λ_{2m−1}(0; ν_s) (ν_s symmetric, so the extremal polynomial is even; Lemma `lem:pone-fold`).

*What carries over verbatim.* Step S6: Prop. `prop:pone-first`(iv) gives ‖𝖷₋−I‖_{L²} ≤ C/N and Lemma
`lem:pone-mismatch` gives |J_H − I| ≤ CN^{−6m−3}(N|z|)^{δ_m}, δ_m ≥ 2, near 0, so the weighted Cauchy estimate of S6
yields |𝖷(iy) − I|, |𝖷'(iy)| ≤ C/N uniformly for 0 < y ≤ ε/2 (iℝ is at angle π/4 from the lips at ±π/4, ±3π/4 and
π/2 from the band); 𝖡_N is analytic and bounded (Lemma `lem:pone-fh`(ii)).

*GAP-1 (exact statement).* Prove the analogue of S2–S3 in the WLXZ frame: for z = iy near 0, the first column of the
symmetric-variable matrix U (degree N = 2m−1) equals 𝖬'·σ(z)·𝖷(z)𝖡_N(z)Ψ^{FH}(Nf(z))e₁ with a constant
𝖬' (det 𝖬' = 1) and an explicit scalar σ(z) whose square, combined with det[Ψ^{FH}e₁', Ψ^{FH}e₁] at 0, gives
K_{2m−1}(0,0;ν_s) = 1/λ_m(0;σ_{1,s}) with the value of Conjecture CG at p = 1 — i.e. that the WLXZ scalars (D, D̃, D̂, E, e^L, the
g-function and 𝒩_s) cancel against W_𝔳 exactly as F, B, χ cancel in S3. This needs the transformations
WLXZ (3.1), (3.9)–(3.15), (4.1), (4.12)–(4.24), (5.1) in their explicit form, and Vanlessen's first column
(4.26)–(4.33) at ζ → 0 (orders a ± ½, a = s − 3/2); we did not carry out this bookkeeping. Numerically the conjecture
holds at p = 1, s ∈ {1.5, 2, 2.5, 3.7} to 17–27 digits (check Λ), so no obstruction is expected.

## 7. Routes considered (OBSTRUCTION notes)

* **O1 (Hankel ratio λ_m = D_m(σ_s)/D_{m−1}(σ_{s+2p}) + Conjecture C).** λ_m = h_{m−1}(s)Π_{k<m−1}h_k(s)/h_k(s+2p);
  the product of the ratios h_k(s)/h_k(s+2p) ≈ c^{−2}k^{2p}(1 + O(1/k)) carries an undetermined global constant
  Π(1+O(1/k)), so C (even if proved) does not give CG without second-order information summed over all k.
  OBSTRUCTION (heuristic).
* **O2 (differential identity in s).** d/ds log λ_m = (1/p)∫log x dν_m (envelope theorem, ν_m = P*²σ/λ_m). Needs
  weak convergence of the rescaled ν_m to the Bessel profile measure with uniform log-integrability, i.e. the same
  hard-edge universality, plus an anchor; no gain over Part A. Not pursued.
* **O3 (Paper II §6 comparison route for |α|<1, in particular p = 1).** The Conway–Deift comparison controls only the
  moments at ∞ (`prop:moments`); the comparison mismatch near 0 is O(1/n) in a weighted L¹ sense but is conjugated by
  P̂₀ ~ n^{±1/2}, so it does not give |𝖱 − I| = O(1/n) pointwise at the hard-edge scale. OBSTRUCTION (heuristic) to
  using §6 for the value at 0; this is why GAP-1 goes through the symmetric frame.
* **O4 (Lemma L + exact families at p=1 for general s).** Lemma L cannot change s (the factor x^{Δs/p} vanishes at 0),
  and the only exactly solvable p=1 family available (Tricomi–Carlitz and its Christoffel transforms) has
  s ∈ 3/2 + ℕ₀. s = 7/2 would follow the same way from Lemma `lem:pone-tc`(c) once u_k(x²σ_TC) is computed; not done.

## 8. Adversarial pass (Rule A), by the author — not a substitute for Rule R

1. *Branches in S4.* (−X)^{−α/2}ζ^{α/2} = (ζ/(−X))^{α/2} needs arg ζ − arg(−X) ∈ (−π,π): both are −π/2 + O(y) at X = iy.
   A wrong branch would give a factor e^{±iπα} — excluded numerically (check Λ at α ∉ ℤ, e.g. α = −0.714, −0.4, 0.75)
   and by positivity of K.
2. *Is iy really outside the lens and in Ω_∞ for p<1?* Lips in |arg| ≤ 5πp/16 < πp/2 < π/2; seams at πp/2 < π/2. Yes.
   For p > 1 the negative axis carries 𝖱-jumps but iy is at angle π/2 from it.
3. *Uniformity of S6 as y → 0.* The bound uses only ‖𝖱₋ − I‖_{L²} (uniform) and the factor |w|^K in |J−I|, never a
   pointwise bound on 𝖱₋; the kernel |w − iy|^{−j} ≤ κ^{−j}|w|^{−j} is integrable against |w|^{K} for K = 3. ✓ (A first
   attempt bounded the Cauchy integral by ‖h‖_{L²}dist(z,Σ)^{−1/2}, which degenerates as y → 0; replaced.)
4. *Scale disparity in S5.* c₁ ~ n^{1/2}, c₂ ~ n^{−1/2}: the term B₂₁c₁² is O(n|B|), compared with the main term
   ~ n²|f'(0)|. If 𝖱' were only O(n) (Cauchy estimate on a disc of radius ~n^{−2}), the error would be O(n²), i.e. not
   small — hence S6(a) must give 𝖱' = O(1/n), which it does. ✓
5. *det 𝖬 = 1, det N = 1*: 𝖬 is a product of (scalar)^{σ₃}; det 𝖱 = 1 (det Q = det P̌₀ = 1). ✓
6. *Degenerate α = 0* (s = 1+p): b̂ is entire, the formula is continuous; K_0 never enters (only the first column). p=1,
   s=2 (α=0) numerically fine; p≠1, α=0: (2,3) gives Richardson limit −1 = −9e−17 at n=40, and α = 4/3: (3,8)
   gives −2e−10 (`checks/check_alpha0.py` → `.out`, precision doubling 500/1000 stable). The argument has no
   α-dependent step.
7. *α ≤ −½ (Conway–Deift branch of Paper II's Step 2)*: only affects Paper II's identification (iii), which we use as a
   black box; (2,2) has α = −½ and (.7,1.2) has α ≈ −0.71: both pass numerically.
8. *Lemma L counter-attempt.* Without "g → 1 at 0" the ratio tends to the value of g at 0 only — e.g. g ≡ 2 gives 2
   (consistent). Without a_k, b_k → 0 the lemma fails in general (a measure with an interval [0,1] in its support: the
   extremal measure ν_m does not concentrate at 0; ε_m does not → 0); the hypothesis is used exactly in (i). ✓
9. *p ≠ 1 restriction*: genuinely from Paper II (no classical parametrix at p = 1). The near-1 behaviour of the O(1/m)
   constant is not uniform; not claimed.

## 9. Theorem C: Conjecture CG at p = 1 for every s > 1 (closes GAP-1) — PROVED-mod-cite + REVIEWED (review/REVIEW_CG_R2.md)

Added 2026-11-05 after the Rule R review of §§0–8; the proofs of Theorems A and B and Lemma L are not changed. Notation of Paper II §`sec:pone-first` and
App. H (WLXZ objects at parameter α_W = 1, rescaled variable z = N^{1/2}y): a := s − 3/2 > −½, ζ := s − 1 = a + ½ (the CG exponent; the KV/Van model variable is written ξ := Nf(z) here), N is
the degree of the symmetric problem, and the Stirling truncation order of Paper II (called m there) is written m_S here, so
that m is always the CG index. We take N := 2m − 1 (N = 2m gives the same kernel, see G1). The claim is

  K_N(0,0; ν_s) = (N³/36)^ζ / (Γ(ζ)Γ(ζ+1)) · (1 + O(1/N)),                                          (C★)

hence, with G1 and N = 2m(1 + O(1/m)), λ_m(0; σ_{1,s}) = Γ(ζ)Γ(ζ+1)(36/8)^ζ m^{−3ζ}(1 + O(1/m)) = Γ(ζ)Γ(ζ+1)(c(1)·3²)^ζ
m^{−3ζ}(1 + O(1/m)), which is Conjecture CG at p = 1 (c(1) = ½, E = 3ζ). At s = 3/2 and 5/2 this agrees with Theorem B.

**External statements used (Rule C; all quoted in research/G1/RH/CITATIONS.md, hypotheses checked here).**
WLXZ (arXiv:1410.3948v1; hypothesis "α is a positive parameter", here α_W = 1): (2.1), (2.3), (2.6), (3.1), (3.4), (3.11),
(4.1), (4.12), (4.19), (5.1), and the constant L of the (5.9) context, L = log(√2 iΓ²(α)e^α/√π) — entries "(WLXZ-v1)",
"(WLXZ-v1, additional quotes for RH_px)", "(WLXZ-v1, Plan 53)", "(WLXZ-v1, Plan 66)". KV §5 (5.9), (5.22), (5.26)–(5.30) —
entry "(KV)"; hypotheses: an interior band point with ψ(0) > 0 (here ψ(0) = 1/(3π), G5), band jump |x|^{2a} times an
analytic non-vanishing factor (Paper II Lemma `lem:pone-weight`, factor 𝔳₀𝖶_N), four lips meeting at 0 (App. H).
Van (math/0212014) (4.27), (4.53) — entries "(Van)", "(Van, Plan 66)"; hypothesis λ > −½ (here λ = a = s − 3/2 > −½).
DLMF 10.25.2 (entry "(DLMF-5)"; ν = a ± ½ > −1) and 5.11.1/5.5.1 (entries "(DLMF)", "(DLMF-5.11, Plan 51)"). Paper II
results are internal and inherit Paper II's labels, including its stated dependence on WLXZ (5.8), (6.34) and the Cauchy
bound after (6.35) (Paper II §`sec:pone-first`, paragraph after Prop. `prop:pone-first`).

**G1 (fold; elementary).** For symmetric ν_s the minimiser of ∫P²dν_s over deg P ≤ 2m−2, P(0) = 1 is even (replace P by
½(P(y)+P(−y)): same value at 0, and ∫ of the square does not increase by convexity), and even polynomials of degree ≤ 2m−2
are exactly Q(y²) with deg Q < m, with ∫Q(y²)²dν_s = ∫Q²dσ_{1,s}. So λ_m(0; σ_{1,s}) = λ_{2m−1}(0; ν_s). Since p_{2m−1}
is odd, p_{2m−1}(0) = 0 and also λ_{2m}(0;ν_s) = λ_{2m−1}(0;ν_s). (Paper II Lemma `lem:pone-fold` is the polynomial
version.) Check [P5].

**G2 (kernel and normalisation).** Paper II App. H: the masses ½k^{−s} of ν_s at ±k^{−1/2} equal (√(2π)/(2e))·w_d(y)e^{j(1/y²)}(y²)^a
at the nodes (w_d of WLXZ (2.15), w_d(±k^{−1/2}) = e·v_k). After z = N^{1/2}y the problem used in App. H has weight wF,
F = e^{j(N/z²)}(z²)^a, w(z) = N^{1/2}w_d(N^{−1/2}z) (WLXZ (3.4)). In the y-variable this is the residue problem
(WLXZ (2.14)) of the measure μ_Y := κν_s, κ := 2eN^a/√(2π) (the factor N^a comes from (z²)^a = N^a(y²)^a). With the
residue normalisation, Y₂₁ = P_{N−1}/h_{N−1} (no 2πi; the coefficient of z^{−N} of Y₂₂ = Σw_kY₂₁(y_k)/(z−y_k) must be 1),
so as in S1, K_N(0,0; μ_Y) = det[Y'e₁, Ye₁](0). WLXZ (3.1), U(z) = N^{Nσ₃/2}Y(N^{−1/2}z), gives
det[U'e₁, Ue₁](0) = N^{−1/2}K_N(0,0;μ_Y), and K(ν) scales as 1/(mass), so

  K_N(0,0; ν_s) = κ·N^{1/2}·det[u_z, u](0),   u := Ue₁ (a pair of polynomials).
(κ here is the mass factor; η below is η(r) = ξ(ir)/i, and the lip-angle tolerance is written η₀.)                     (G2)

**G3 (first column through the WLXZ chain on iℝ).** Fix z = ir, 0 < r ≤ ε/2. Near 0 the only contours are the band and
the four lips, which lie in |arg(±z)| ∈ [π/4 − η₀, π/4 + η₀] (η₀ small) (App. H §"The Fisher–Hartwig point"); the saturated
contours Σ^△ lie near |z| ∈ [2, k_n]. So ir ∈ Ω∞, where by WLXZ (3.11), (4.12) and (5.1) R = U, Q = T and
V = N^{(α_W−½)σ₃}Q(ED)^{σ₃}; by (4.1) T = e^{−Nlσ₃/2}Re^{(−Ng+Nl/2)σ₃}. (Lemma `lem:pone-weight`: g, φ, D, E do not depend
on the weight, so these are WLXZ's functions.) Hence

  u = 𝖬₀·Ve₁·e^{Ng−Nl/2}/(E D),   𝖬₀ := e^{Nlσ₃/2}N^{−(α_W−½)σ₃} (constant, diagonal, det 1).

In U(0,ε), App. H sets H := σ₃Vσ₃P₀^{−1} (H = 𝖷 up to conjugation by σ₃, as in `prop:pone-first`), P₀ = 𝖡_NΨ^{FH}(Nf)W_𝔳^{−σ₃}e^{−Nφ^{KV}σ₃}, φ^{KV} = −φ,
φ = l/2 − g (WLXZ (2.3)), W_𝔳 = W𝔳₀^{1/2}, 𝔳₀ = e^L(4 − z²)𝖰_{m_S}. As σ₃e₁ = e₁,
Ve₁ = σ₃HP₀e₁ = σ₃H𝖡_NΨ^{FH}(ξ)e₁·W_𝔳^{−1}e^{N(l/2−g)}, ξ := Nf(z). **The exponentials cancel exactly**:

  u(ir) = 𝖬₀σ₃·𝖦(ir)·c(ir) / (E D 𝔳₀^{1/2})(ir),   𝖦 := H𝖡_N (not Paper II's 𝒩, 𝒩_s),   c := Ψ^{FH}(ξ)e₁·W^{−1}.            (G3)

This is the p = 1 analogue of S2–S3 (there FW̃ was explicit; here the scalar is 1/(ED𝔳₀^{1/2})). det 𝖬₀σ₃ = −1;
det 𝖦 = 1 (det V = det P₀ = 1 (`lem:pone-fh`(i)), det Ψ^{FH} = 1 (Van (4.53)), det W_𝔳^{−σ₃}e^{…σ₃} = 1, hence
det 𝖡_N = 1). P₀ is analytic across iℝ (Ψ^{FH} and W jump there, P₀ does not), so (G3) holds with the boundary
values from the sector to the right of iℝ, f^{−1}(II).

**G4 (the explicit scalar and Bessel column).** (i) f is odd, real on ℝ, f'(0) = πψ(0) (App. H), so ξ(ir) = iη(r), η real
analytic, η(r) = Nf'(0)r(1 + O(r²)) > 0: ξ is on arg ξ = π/2, the boundary of sector II (π/4 < arg ξ < π/2).
(ii) In f^{−1}(II), 0 < |arg f| < π/2, so W = (−z)^a (KV (5.9)); at z = ir, W = r^a e^{−iπa/2}.
(iii) Van (4.27) (sector II, λ = a): first column = e^{−aπi/2}·√πξ^{1/2}(I_{a+½}(ξe^{−πi/2}), −iI_{a−½}(ξe^{−πi/2}))ᵀ, with
ξe^{−πi/2} = η, ξ^{1/2} = e^{iπ/4}η^{1/2}. With DLMF 10.25.2, I_ν(η) = (η/2)^ν β_ν(η²), β_ν entire, β_ν(0) = 1/Γ(ν+1):

  c(ir) = e^{iπ/4}√π (η/r)^a · v(η),   v(η) := (2^{−a−½}η β_{a+½}(η²), −i2^{−a+½}β_{a−½}(η²))ᵀ,

with (η/r)^a real analytic and → (Nf'(0))^a. (The singular powers η^{±a} and r^{∓a} cancel; this is the analogue of S4.)
(iv) Scalars at 0: E(z) = √(2π)(4 − z²)^{−1/2} (WLXZ (4.19), α_W = 1), E(0)² = π/2; D(ir) = e^{j(N/r²)} → 1 (WLXZ (2.6)
at z = ir: −N/z² = N/r² > 0 with the branch e^{±πi}/z², and Γ(1+T)e^TT^{−T−½}/√(2π) = e^{j(T)}, DLMF 5.5.1, 5.11.1; check [P2]);
𝔳₀(0) = 4e^L (𝖰_{m_S}(0) = 1); e^L = √2 i e/√π. So, writing τ := e^{iπ/4}√π(η/r)^a/(E D 𝔳₀^{1/2}),

  τ(ir)² → i(Nf'(0))^{2a}/(2e^L) = (√π/(2√2 e))·(Nf'(0))^{2a}  (r → 0)   — a positive number.

**G5 (ψ(0)).** From WLXZ (2.1), with arctan(x/√(4−x²)) = arcsin(x/2):
ψ(x) = (1/π)(4arcsin(x/2)/x³ − √(4−x²)/x²) = (1/π)(2/x² + 1/12 − 2/x² + 1/4 + O(x²)) = 1/(3π) + O(x²). So f'(0) = 1/3.
Check [P1] (also ∫ψ = 1).

**G6 (determinant).** u = 𝖬₀σ₃·τ·𝖦v. Scalar factors drop out of a Wronskian of a vector with itself, so with d/dz = −i d/dr
on z = ir and B := 𝖦^{−1}∂_r𝖦,

  det[u_z, u](ir) = (−i)(−1)·τ²·(det[v_r, v] + det[Bv, v]).

As r → 0: v → (0, −i2^{−a+½}/Γ(a+½)), v_r → (2^{−a−½}Nf'(0)/Γ(a+3/2), 0), so
det[v_r, v] → −i·2^{−2a}Nf'(0)/(Γ(a+½)Γ(a+3/2)); and |det[Bv, v]| ≤ C|B||v|² ≤ C|B| with v(0) independent of N. Check [P3]
(the limit computed from mpmath's I_ν with the sector-II formula, linear and non-linear odd f, a ∈ {−0.3, 0, …, 3.5}).

**G7 (uniform bound on B along iℝ; from Paper II as in S6).** 𝖡_N is analytic in U(0,ε) with |𝖡_N^{±1}| ≤ C uniformly in
N (`lem:pone-fh`(ii)), so |∂𝖡_N| ≤ C on U(0, ε/2) (Cauchy). For 𝖷 = I + 𝒞(𝖷₋(J_𝖷 − I)) (`prop:pone-first`(iv)) at z = ir:
the circles and the parts of Σ_𝖷 outside U(0,ε) are at distance ≥ ε/2, giving ≤ C(‖J−I‖_{L¹} + ‖𝖷₋−I‖_{L²}‖J−I‖_{L²}) ≤ C/N
for 𝖷 − I and its derivative (by (i)–(iii) of the proposition, ‖J−I‖_{L¹∩L²} ≤ C/N). On Σ_𝖷 ∩ U(0,ε) (band, angle π/2 to iℝ;
lips, angle ≥ π/4 − η₀) we have |w − ir| ≥ κ₀ max(|w|, r), κ₀ := sin(π/4 − η₀), and by `lem:pone-mismatch` |J−I| ≤ CN^{−2m_S−1}
everywhere there and ≤ CN^{−6m_S−3}(N|w|)^{δ}, δ = δ_{m_S} ≥ 2, for N|w| ≤ 1. Then for j ∈ {1, 2}
∫|J−I||w−ir|^{−j}|dw| ≤ C[N^{−6m_S−1}∫_{|w|≤1/N}|w|^{2−j}|dw| + N^{−2m_S−1}∫_{1/N≤|w|≤ε}|w|^{−j}|dw|]
≤ CN^{−2m_S−1}(N^{j−1} + log N) ≤ CN^{−2m_S}log N, and (∫|J−I|²|w−ir|^{−2j}|dw|)^{1/2} ≤ CN^{−2m_S−1}N^{j−½} + (smaller)
≤ CN^{−2m_S+½}; both are ≤ C/N since m_S ≥ 1 (the second is combined with ‖𝖷₋−I‖_{L²} ≤ C/N by Cauchy–Schwarz). Hence |𝖷(ir) − I| + |∂𝖷(ir)| ≤ C/N
uniformly for 0 < r ≤ ε/2. (The uniformity in r comes from the refined bound (N|w|)^{δ} of `lem:pone-mismatch`
together with the L² bound of `prop:pone-first`(iv); the uniform bound CN^{−2m_S−1} of `prop:pone-first`(ii) alone would not
control |w − ir|^{−2} as r → 0.) So |𝖦^{±1}| ≤ C, |∂𝖦| ≤ C and |B(ir)| ≤ C uniformly in r and N.

**G8 (assembly).** u is polynomial, so det[u_z, u](0) = lim_{r→0} det[u_z, u](ir). By G6, G7, G4:

  det[u_z, u](0) = (√π/(2√2e))(Nf'(0))^{2a}·2^{−2a}Nf'(0)/(Γ(a+½)Γ(a+3/2))·(1 + O(1/N)).

(Phases: (−i)(−1) = i from G6, and i·(−i) = 1 with the −i of det[v_r, v]; τ² → (√π/(2√2e))(Nf'(0))^{2a} > 0 since
i/(2e^L) = √π/(2√2e).) Insert into (G2), with κN^{1/2} = (√2e/√π)N^{a+½}:

  K_N(0,0; ν_s) = N^{a+½}(Nf'(0)/2)^{2a+1}/(Γ(a+½)Γ(a+3/2))·(1 + O(1/N)) = (N³(f'(0)/2)²)^ζ/(Γ(ζ)Γ(ζ+1))·(1 + O(1/N)),

and f'(0) = 1/3 gives (C★). The assembly of constants (E(0), 𝔳₀(0), e^L, κ, the σ₃ sign and d/dz = −i d/dr) is
re-done numerically in [P4]. ∎

**Why GAP-1 closed by direct bookkeeping (no calibration against s = 3/2 needed).** In the Ω∞ region the WLXZ chain is
U ↦ (constant)·U·(scalar)^{σ₃} with scalars e^{±Ng}, E, D only (no lens or pole-removal factor), and the KV parametrix
carries the matching e^{−Nφ^{KV}} = e^{N(l/2−g)}; all weight dependence sits in W_𝔳 = (−z)^a𝔳₀^{1/2}, whose power cancels
the Bessel singularity η^a exactly and whose constant 𝔳₀(0) = 4e^L cancels the phase of e^L. 𝖡_N (which contains
𝒩_s, the Szegő factors 𝒟_h, 𝒟_q, and the phase e^{Nφ^{KV}_+(0)σ₃}) only enters through det 𝖡_N = 1 and |∂𝖡_N| ≤ C.
Theorem B is then a consistency check, not an input.

**Rule A (for §9).**
1. *Is ir really in Ω∞ and off the △ regions?* The △ regions belong to the saturated interval (2, k_n) (WLXZ (3.11),
   (4.10)); near 0 only the lens regions Ω_{l,±}, Ω_{r,±} exist, bounded by lips at angle ≈ π/4 from ℝ (App. H). ✓
2. *Sector and branch of W.* P₀ is continuous across iℝ, so the sector to the left must give the same c. There Van (4.28)
   is (4.27) with e^{+½aπiσ₃} (first column × e^{aπi} relative to II, same Bessel arguments), and KV (5.9) gives W = z^a
   (π/2 < |arg f| < π), with z^a = e^{iπa}(−z)^a at z = ir. The two factors e^{iπa} cancel in c = Ψe₁W^{−1}: consistent.
   A mismatched pairing would leave e^{±iπa} in τ² and a non-real K for 2a ∉ ℤ; [P6] at s = 1.2 (a = −0.3) and s = 3.7
   (a = 2.2) confirms the real positive constant.
3. *N vs N ± 1.* G1 shows K_{2m−1} = K_{2m}; the leading term (N³/36)^ζ with N = 2m−1 or 2m differs by 1 + O(1/m). ✓
4. *Scale disparity in G6* (as in §8 item 4): v is N-independent and only v_r ∝ N, so the main term is O(N) and the
   error det[Bv,v] = O(|B|) = O(1) — no derivative of order N enters (unlike S5, where c₁ ~ n^{1/2}). This needs the
   derivative bound in G7 only up to O(1), but G7 gives O(1/N) for 𝖷 anyway.
5. *Dependence.* Through `prop:pone-first`, Theorem C inherits Paper II's stated reliance on WLXZ (5.8), (6.34) and the Cauchy
   bound after (6.35). Rule-C quotes for those are in CITATIONS.md "(WLXZ-v1)"; nothing beyond Paper II's own use is assumed.
6. *Not used:* the second-order analysis of Paper II (`lem:pone-models`, `prop:pone-S1`), and Theorem B.

## 10. Relation to second_order/E2_pgt1.md (Cor E2.7, Remarks E2.12–E2.13) and the index-shift conjecture (F7) — REVIEWED (review/REVIEW_CG_R2.md)

**What was known.** E2_pgt1.md Corollary E2.7 (PROVED-mod-cite + REVIEWED, 2026-10-20): for p > 1, s > 1,
λ_n(0; σ_{p,s}) = C(p,s)·n^{−(p+2)(s−1)/p}(1 + o(1)) with some C > 0 not computed. Its λ_n is the same quantity as ours
(minimum over deg R ≤ n−1, R(0) = 1). So, for p > 1, **the exponent E of Theorem A is Cor E2.7**; the contributions of this
note are (a) the value C = Γ(ζ)Γ(ζ+1)(c(p)(p+2)²)^ζ/p, (b) the rate O(1/m), (c) the range 0 < p < 1 (Theorem A), and
(d) p = 1 (Theorems B, C), where E2_pgt1 is not applicable (E2 Remark E2.10 / E_pgt1 §9).

**Routes compared.** Cor E2.7 uses the Hankel identity λ_n = D_n(σ)/D_{n−1}(x²σ) and sums the third-order expansion of
log h_j(s) − log h_j(s+2p) over j < n; the summed constant K = −2log c comes from UL Thm UF-lim, but the global constant
(C₁ of E_pgt1 Thm E.1 together with Σ_j of the O(j^{1−ν}) remainders) is not evaluated, which is why C is left open (our
obstruction O1, §7). Remark E2.13 (review A I1) replaces this by K_n(0,0) = Σ_{j<n}p_j(0)² with first-order asymptotics of
each p_j(0) (E_pgt1 Cor E.6), giving C n^{−E}(1 + O(n^{−θ})); again C is a sum over all j and is not explicit. Our S1 uses the
reproducing kernel too, but through Christoffel–Darboux: the sum Σ_{j<n}p_j(0)² is replaced by the single Wronskian
n^p det[u'(0), u(0)] of the degree-n RH solution, and the hard-edge parametrix evaluates that Wronskian in closed form (the
Bessel Wronskian 2πi/(Γ(α+1)Γ(α+2)) and |f'(0)|). This is why the constant is accessible, and why the error is O(1/n) (one
RH error matrix, no summation of remainders). The two routes are independent; agreement of the exponents is a cross-check.

**Consistency (NUMERICAL).** (i) Exponent: E2.7's −(p+2)(s−1)/p = −E (identical expression). (ii) E2's own numbers:
`second_order/checks/check_e2_christoffel.out` reports local slopes of log λ_n over [n, 2n], n = 100…800, at (1.5,2), (2,2),
(2,3), (3,2). Theorem A in the shifted form λ ≈ C(n + (s−1)/(2p))^{−E} predicts these slopes (C cancels); the difference is
−1e−5, −2e−6, −4e−7, +2e−7 at (1.5,2), and similarly for the others, decreasing like n^{−2} down to the 6-digit rounding of
the printed slopes, while the unshifted −E misses by 1.4e−2 … 2.5e−4 over the four rows (`checks/check_e2_consistency.py` → `.out`). No statement
of E2_pgt1.md about C conflicts with Theorem A (E2 states only C > 0). (iii) Remark E2.12 identifies λ_n(0; σ_{p,s}) with
the squared A-norm CG error after n − 1 steps, for spectral weights k^{−s} at eigenvalues k^{−p}; with Theorem A this
error is Γ(ζ)Γ(ζ+1)(c(p)(p+2)²)^ζ p^{−1} n^{−(p+2)(s−1)/p}(1 + O(1/n)), the "exact CG constant" of the brief.

**F7 (CONJECTURE, NUMERICAL; review F7).** λ_m(0; σ_{p,s}) = C·N^{−E}(1 + o(1/m)) with N = m + (s−1)/(2p), i.e. the 1/m
coefficient of λ_m m^E/C is −E(s−1)/(2p). Evidence: review (Arb ball arithmetic) −5.75998 vs −5.76 at (2.5, 5) and
−2.92515 vs −2.925 at (0.6, 1.9); the slopes in (ii) above at four (p, s); at p = 1 [P6] gives m(r_m − 1) at m = 80
approaching −3ζ·s/2, the value F7 predicts for r_m normalised with N = 2m − 1 (−1.117 vs −1.125 at s = 1.5, −2.94 vs −3 at s = 2); and review R2 (REVIEW_CG_R2.md) finds the 1/m coefficient −3ζ²/2 at p = 1, s = 1.35 and 4.2,
the value F7 predicts (λ = C(m + ζ/2)^{−3ζ}, ζ = s − 1). Not proved: Theorem A's proof
gives the O(1/m) term only as a bound (det[Bc,c] = O(n) in S7), and identifying its coefficient would need the 1/n term of
𝖱 at 0 (second-order hard-edge data). This is the same index shift n ↦ n + (s−1)/(2p) as in E2 Remark E2.8.

## LOG (literature queries, 2026-11-05)

* WebSearch "Hanke 1996 Numerical Algorithms conjugate gradient asymptotics Tricomi-Carlitz Lommel polynomials" →
  MaRDI Q1911450 abstract (full text not found).
* WebSearch "Christoffel function at hard edge asymptotics varying weights discrete measure eigenvalues k^{-p}
  conjugate gradient power law spectrum Velikanov Yarotsky" → Lubinsky hard-edge / varying weights papers, Danka–Totik
  arXiv 1504.03968; none covers atomic measures accumulating at the edge.
* WebSearch "Velikanov Yarotsky 2024 JMLR ..." → JMLR v25/23-0698, arXiv 2202.00992 (abstract read: rates only).
* WebFetch DLMF §4.13 (quotes in §4).
One search per topic is not a full Rule-L check; novelty stays UNCHECKED.

## LOG (2026-11-05, after Rule R review R1)
* Applied review/REVIEW_CG_R1.md: F1 (DLMF 4.13.1, 4.13.2, 4.13.5 quoted verbatim in research/G1/RH/CITATIONS.md, new entry
  "(DLMF-4.13, constants/CG)", plus "Also used in: constants/CG/CG.md" lines in the KV, KMVV, DLMF §5.11, DLMF-5, Van Plan 66,
  WLXZ Plan 53 and WLXZ Plan 66 entries); F2 (|Ǎ| ≤ C|z|^{−1/2} for p < 1 written out in (P5)); F3 (S3 wording: B, χ are
  functions); F4 (p < 1 lip angle in S6(a)); F5 (check_lambda_n80.out regenerated at dps 800/1600); F6 (Lemma L novelty
  UNCHECKED, §1); F7 (recorded as CONJECTURE, §10). Labels of A, L, B: + REVIEWED.
* Added §0 Theorem C, §9 (GAP-1 closed; NOT REVIEWED), §10 (Cor E2.7 and Remarks E2.12–E2.13, per coordinator); §6 marked
  closed (text unchanged). New checks: checks/check_p1.py → .out, checks/check_e2_consistency.py → .out.
* Applied review/REVIEW_CG_R2.md nits N1–N5 (𝖦 := H𝖡_N; κ₀, η₀; "H = 𝖷 up to σ₃-conjugation"; G7 uniformity source;
  §10(ii) range); Theorem C and §10 relabelled REVIEWED; F7 updated with R2's p = 1 evidence.

