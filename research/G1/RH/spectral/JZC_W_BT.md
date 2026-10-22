# JZC W BT: branched tilts in the decoupled model — the hard-edge companion from the lip mismatch (Hypothesis BT)

Status (2026-10-22): **NOT REVIEWED** (no Rule R reader). Labels per VERIFICATION_POLICY.md; "PROVED" below means written proof +
Rule A log (§7), no second reader. Novelty: UNCHECKED (no Rule L pass). No claim about RH: no measure built from zeta zeros is used.
Inputs keep their labels: JZC_M4_proof (Lemmas N.6a–d, Theorem N.6: REVIEWED), JZC_M3a_H_G1u (L1–L2: REVIEWED), JZC_W_exact (NOT
REVIEWED), JZC_W_outer (NOT REVIEWED). Paper 2 (papers/paper2/sec_2.tex T2–T4, sec_7.tex §7.1–7.2) is quoted as read for this note
(read-only). External facts: only DLMF items already quoted in CITATIONS (§2.3).

Checks (all in `checks/`, Python = the session venv, `-B`; every `.out` prints the sha256 of the scripts it uses):
- `w_bt_engine.py`: a copy of `w_exact_engine.py` (itself the m4_rh_exact2 copy) whose only change is that `run()` also stores its
  hard-edge objects (R_in at 0, R1, conj_hard, f^{1/2}, …) in a dict `EXPORT`; nothing computed or returned is altered (diff in its docstring).
- `w_bt_core.py`: the lip-mismatch computation of §3 (exact, over the engine's field; j plays ρ, alpha plays ν).
- `w_bt_mellin.py` → `w_bt_mellin.out`: numerical checks of the analytic inputs (Lemmas BT.2–BT.3, the Bessel frame).
- `w_bt_companion.py` → `w_bt_companion_{L,P,B,Q}.out`: the derived companion against the exact Laguerre series (L), against H, X and
  the cached engine residues at five p (P), β-independence (B), and the pole-term cancellation (Q).
- `w_bt_symp.py` → `w_bt_symp.out`: c_0, c_1 with symbolic (p, ν, β, ρ).
- `w_bt_predict.py` → `w_bt_predict.out`, `w_bt_predictions.json`: **pre-registration** (11:14:19) of the N⁻⁷ pole residues;
  `w_bt_poles7.py` → `w_bt_poles7_p3_2.out`, `w_bt_poles7_p3.out`: the registered test (engine runs started 11:14:33).

| # | Statement | Label |
|---|---|---|
| Def BT.0 | the branched model: M(β, ν) with band tilt h = e^{−μz^ρ} and lip factors e^{±iπσz^ρ}, as an RH problem | definition |
| Lemma BT.1 | with the engine's (A_ρ-gauge) hard-edge parametrix, the error matrix has the engine's circle jumps and, inside U_0, **only** the lip jump I + ϱ_±(e^{±i(μ tan πρ + πσ)z^ρ} − 1)·C L(ζ) C⁻¹, L = (w/π)M[[iKK′, K²], [K′², −iKK′]]M⁻¹ | PROVED (exact algebra from G1u L1–L2, JZC_W_exact WE.1(iii)); L's closed form NUMERICAL-checked to 10⁻³⁰ |
| Lemma BT.2 | first-order formula: ∂_μR_1 = (engine) + (i tan πρ sin π(ρ−ν)/π)∫_0^δ x^ρ R_in C L C⁻¹ R_in⁻¹(−x)dx + O(e^{−cn}) | PROVED-mod-cite (Paper 2 T3(b) = Conway–Deift Thm 4.4 moments; the derivative at μ = 0 needs ρ ≥ \|ν\|, §2.2); deformation NUMERICAL-checked |
| Lemma BT.3 | ∫_0^∞w^{s−1}K_ν(w)²dw = 2^{s−3}Γ(s/2+ν)Γ(s/2−ν)Γ(s/2)²/Γ(s); the K′², KK′ moments by the Bessel ODE; tan πρ sin π(ρ−ν)𝒦(2ρ+2) = −2^{2ρ}π²Φ_ν(ρ) | PROVED-mod-cite (DLMF 10.32.9, 5.2.1, 5.12.3, 5.12.1, 5.5.3); NUMERICAL to 10⁻¹²…10⁻³⁰ |
| **Thm BT** | first-order response = engine's symbolic-j layer at j = ρ **plus** the companion (p+2)^{2ρ+1}Φ_ν(ρ)(n/N)^{(ρ+1)p}N^{−2ρ−2}Σ_kc_kN^{−k}, every c_k given by a finite exact algorithm; c_0 = (pρ+2ρ+1)/2, c_1 = c_3 = 0, c_2, c_4 explicit | formal-layer identity: PROVED (exact algebra + BT.1–BT.3); as an asymptotic statement for true problems: CONDITIONAL (F-br, §3.3) |
| Cor BT.4 | (a) H(ρ) of JZC_W_exact WE.4 for all p (was CONJECTURE); (b) X(p, ν) of Obs WE.6 (was POST HOC) = c_2(½)/c_0(½); (c) the ρ = ½ log terms; (d) E3.7 at n⁻¹ for branched tilts | (a) PROVED as a layer identity in (p, ν, β, ρ) (`w_bt_symp`); (b) PROVED as layer identities at p ∈ {−1, ½, 3/2, 2, 3, 5} (identities in (ν, ρ), not in p); (c) PROVED-mod (uniformity in ρ); (d) CONDITIONAL (F-br) |
| **Prop BT.5** | pole terms (the κ-problem structure: tilt τ and lip factor with πσ = τ tan πq) have **no** lip mismatch: they are exactly the analytic (A_q-)gauge problem; hence no companion, and W′'s premise holds for M(β, ν) | PROVED (algebra, given P W-out.5(iii) and L W-out.4, NOT REVIEWED) |
| Cor BT.6 | Hypothesis BT (W_outer §6) in first order: the lip coefficients σ_ρ do not enter at N^{−1−pρ}; they enter at relative N^{−2ρ−1}, exactly as μ ↦ μ + πσ cot πρ in the companion | PROVED as layer identity; CONDITIONAL (F-br) as asymptotics |
| Tests | Laguerre (p = −1) through N⁻⁴ identically in (ν, ρ); c_0 symbolic in p; X and cached Res_{½}g1[5] at 5 p; β-free; **pre-registered N⁻⁷ residues at p = 3/2, 3: all hold** | exact identities; 76 assertions incl. 17 controls (+ 11 numerical) |

## 0. Summary

1. **Where the companion comes from.** The E3 gauge of a branched tilt e^{−μz^ρ} has, near 0, a side-dependent remainder
   ±i tan(πρ)z^ρ (JZC_W_exact WE.1(iii)). Build the hard-edge parametrix with the analytic part only (this is exactly what the
   symbolic-j engine computes at j = ρ). Then the remainder does not touch the band, the circle or (−δ, 0): it shows up **only as a
   mismatch of the lip jump**, and the lip jump of the Bessel model is exponentially localised at the Bessel scale |ζ| ≲ 1
   (e^{2nφ} = e^{−4ζ^{1/2}}). Deforming the two lip integrals onto the off-band axis (−δ, 0), where z^ρ jumps, turns the mismatch
   into a Mellin integral of the column-2 Bessel bilinear K_ν(w)², K_νK_ν′, K_ν′² against x^ρ: this produces tan(πρ)sin π(ρ−ν)·Γ-ratio
   = −2^{2ρ}π²Φ_ν(ρ), at the scale x ~ n⁻²(p+2)², i.e. relative order n^{−2ρ−1}. Everything else (R_in, the conformal map, the
   outer conjugation) is the engine's exact hard-edge data, so every coefficient of the companion is a finite exact computation.
2. **Results.** c_0 = (pρ+2ρ+1)/2 identically in (p, ν, β, ρ): this **derives** H(ρ) = ½(pρ+2ρ+1)(p+2)^{2ρ+1}Φ_ν(ρ)/C(2ρ,ρ) (per
   normalised tilt), so JZC_W_exact Finding WE.4 is now a theorem of the formal model. The companion is even in 1/N (c_1 = c_3 = 0),
   β-free in N = n + (β+1)/2 (Σ-structure), and its N⁻² dressing at ρ = ½ is exactly the post hoc X(p, ν) of Obs WE.6. At p = −1
   it reproduces the exact Laguerre branched series through N⁻⁴ identically in (ν, ρ), with no calibration.
3. **Pole terms have no companion.** For the κ-problem (JZC_W_outer P W-out.5) the branched band tilt and the lip phase come from
   the single factor exp(C(−z)^q), analytic across (−δ, 0); in Lemma BT.1 they enter as μ tan πq + πσ = 0. So pole terms are
   *exactly* the analytic-gauge problem — the premise of W′ (JZC_W_exact §4) — and N.6b's meromorphy holds for them.
4. **What is not proved.** The analytic transfer (that the formal layers are asymptotic expansions of the Jacobi coefficients of
   true branched-tilted measures) needs the frame for a branched band factor (F-br, §3.3); the derivative at μ = 0 needs ρ ≥ |ν|
   in L^∞ (for |ν| − ½ < ρ < |ν| only the formal identity); second order in μ is not treated.

## 1. Setting

Notation of JZC_M4_proof §1, JZC_M3a_H_G1u §2, c = 1 (band [0, 4]; c-scaling as in N.6d). M(β, ν): Bessel order ν, Szegő exponent β,
lattice g-function, n^p frame; |ν| < 1. ζ = n²f(z), f = −z/(p+2)² + O(z²) (E2 Lemma E2.4; asserted in m4_rh_exact2), so the band
(0, δ) maps to ζ < 0, (−δ, 0) to ζ > 0, U_0 ∩ ℂ_± to ℂ_∓ (Paper 2 sec_7, quoted: "f maps U(0,δ) ∩ ℂ_± into ℂ_∓, the band (0,δ) into
(−∞,0) and (−δ,0) into (0,∞)"). Bessel model (Paper 2 T2(a), quoted): Ψ_α(ζ) = [[I_α(2ζ^{1/2}), (i/π)K_α(2ζ^{1/2})], [2πiζ^{1/2}I_α′,
−2ζ^{1/2}K_α′]] in |arg ζ| < 2π/3 (angle freedom T2(b): the rays at ±(π − ϑ_lip)), jumps [[1,0],[e^{±απi},1]] on the lip rays, all oriented
towards 0; Φ_α := σ₃Ψ_ασ₃e^{−2ζ^{1/2}σ₃} (Paper 2 (eq:he-Phi)), with Φ_{α,+} = Φ_{α,−}[[1,0],[e^{∓iπα}e^{−4ζ^{1/2}},1]] on arg ζ = ∓(π−ϑ_lip),
rays oriented away from 0 (eq:he-Phi-jumps), and e^{2nφ} = e^{−4ζ^{1/2}} (eq:he-ephi). The G1u parametrix (L2, REVIEWED):
P̂₀ = Â(2πn)^{σ₃/2}Φ_ν(n²f)ρ^{−σ₃}, Â = P₀^∞ρ^{σ₃}Mf^{σ₃/4}, with ρ = W̃/D_W, lip identity ϱ_±ρ^{−2} = ω (L1(ii)), ϱ_± = e^{∓iπν}, and
circle expansion Δ_k = (2f^{1/2})^{−k}P₀^∞ρ^{σ₃}(σ₃Ξ_kσ₃)ρ^{−σ₃}(P₀^∞)^{−1} (L2(iii) = N.6a). Write 𝒞X := P₀^∞ρ_mod^{σ₃}Xρ_mod^{−σ₃}(P₀^∞)^{−1}
(the engine's `conj_hard`). The frame identity behind Δ_k is
  M ζ^{σ₃/4}(2π)^{σ₃/2}Φ_ν(ζ) ∼ Σ_k σ₃Ξ_kσ₃(2ζ^{1/2})^{−k}   (ζ → ∞; checked numerically, w_bt_mellin (4)).

**Definition BT.0 (the branched model).** M(β, ν; μ, σ, ρ) is the RH problem of M(β, ν) (Paper 2 frame, Q-frame jumps: J on the band,
[[1,0],[ωe^{2nφ},1]] on the lips, none on (−δ, 0)) whose band weight carries h = e^{−μz^ρ} (principal z^ρ, cut (−∞, 0]; ρ > 0, ρ ∉ ℤ) and
whose lip (2,1) entries carry the extra factor e^{±iπσz^ρ} in ℂ_±. (BT of JZC_W_outer §6 has τ_ρ = −μn^{pρ}, σ_ρ = σn^{pρ}.) The formal
model's layers are defined by the residue recursion of JZC_M4_proof §1 for the circle jumps plus the lip term of Lemma BT.2.

## 2. The lemmas

### 2.1 Lemma BT.1 (the lip mismatch)

Let D_h be the Szegő function of h on [0, 4]. Then log D_h = −(μ/2)(z^ρ − RM_ρ) (M_ρ := z^ρ/R − 2C_ρ, JZC_W_exact §1: z^ρ − RM_ρ = 2RC_ρ is
analytic off [0, 4], O(1) at ∞, and (2RC_ρ)_+ + (2RC_ρ)_− = 2x^ρ on the band), so the h-part of ρ = W̃/D_W is ρ_h = h^{1/2}/D_h = e^{−μRM_ρ/2}.
By WE.1(iii), RM_ρ = RA_ρ ± i tan(πρ)z^ρ in ℂ_± near 0. Put ρ_a := ρ_mod e^{−μRA_ρ/2}, ρ_x := e^{∓(i/2)μ tan(πρ)z^ρ}, so ρ = ρ_aρ_x.

**Lemma BT.1.** Let P̂₀^a := Â_a(2πn)^{σ₃/2}Φ_ν(n²f)ρ_a^{−σ₃}, Â_a := P₀^∞ρ_a^{σ₃}Mf^{σ₃/4}. Then (i) Â_a is analytic in U_0 (removable at 0);
(ii) P̂₀^a has the band jump J, no jump on (−δ, 0), and the lip jump [[1,0],[ω_ae^{2nφ},1]], ω_a := ϱ_±ρ_a^{−2}; (iii) on the circle,
P̂₀^a(P₀^∞)^{−1} = I + ΣΔ_k^an^{−k} with Δ_k^a = G_aΔ_k^{mod}G_a^{−1}, G_a = P₀^∞(e^{−μRA_ρ/2})^{σ₃}(P₀^∞)^{−1} — the engine's gauge (E3
Lemma E3.4 with the Taylor data of A_ρ, WE.1(ii)); (iv) R := Q(P̂₀^a)^{−1} has, in U_0, only the lip jump
  I + ϱ_±(e^{±i(μ tan πρ + πσ)z^ρ} − 1)·𝒞_a L(ζ)𝒞_a^{−1},  L(ζ) := Mζ^{σ₃/4}(2π)^{σ₃/2}[e^{−4ζ^{1/2}}Φ_νE₂₁Φ_ν^{−1}](2π)^{−σ₃/2}ζ^{−σ₃/4}M^{−1},
  and L(ζ) = (w/π)M[[iK_νK_ν′, K_ν²], [K_ν′², −iK_νK_ν′]]M^{−1}, w = 2ζ^{1/2}, K_ν = K_ν(w), 𝒞_a := conjugation by P₀^∞ρ_a^{σ₃}.
*Proof.* (i)–(ii): ρ_a = ρ_mod·e^{−μRA_ρ/2} with A_ρ analytic in |z| < 4 and R₊ = −R₋ on the band, so ρ_{a,+}ρ_{a,−} = 1 on (0, δ) and
ρ_a has no jump on (−δ, 0); with this, the proofs of G1u L2(i)–(ii) (REVIEWED) apply verbatim (they use only these two properties and
|ρ_a^{±1}| ≤ C). (iii): G1u L2(iii) with ρ_a; P₀^∞ρ_a^{σ₃}(P₀^∞)^{−1} = G_a·P₀^∞ρ_mod^{σ₃}(P₀^∞)^{−1} and, to first order,
R·P₀^∞σ₃(P₀^∞)^{−1} = T[[0, z−4], [z, 0]]T^{−1} (computed: T^{−1}σ₃T = σ₁, A² = ((4−z)/(−z))^{1/2}), which is E3's
G = T[[cosh h, −(z−4)S], [−zS, cosh h]]T^{−1}, h = RM/2. (iv): The true lip entry is ωe^{2nφ}·e^{±iπσz^ρ} with ω = ϱ_±ρ^{−2} (L1(ii)),
= ω_ae^{2nφ}e^{±iμ tan(πρ)z^ρ}e^{±iπσz^ρ}. On the band and on (−δ, 0) Q and P̂₀^a have the same jumps ((ii) and Def BT.0). On the lips
R₊ = R₋P̂₋[[1,0],[(ω − ω_a)e^{2nφ},1]]P̂₋^{−1}; ρ_a^{−σ₃}E₂₁ρ_a^{σ₃} = ρ_a²E₂₁ and (ω − ω_a)ρ_a² = ϱ_±(e^{±i(μt+πσ)z^ρ} − 1), t = tan πρ;
f^{σ₃/4}n^{σ₃/2} = ζ^{σ₃/4}. The closed form: e^{−4ζ^{1/2}}Φ_νE₂₁Φ_ν^{−1} = −σ₃Ψ_νE₂₁Ψ_ν^{−1}σ₃ (the exponentials cancel), and
Ψe₂e₁ᵀΨ^{−1} = (b, d)ᵀ(d, −b) for Ψ = [[a, b], [c, d]], det Ψ = 1; column 2 is continuous across the lip rays (the jumps are lower
triangular), so the central formula b = (i/π)K_ν(w), d = −wK_ν′(w) applies on the lips. Conjugate. ∎ (w_bt_mellin (4): the closed
form against the definition at real and lip-ray ζ, 3·10⁻³¹; control with K², K′² swapped fails.)

*Remark.* For σ = 0 the mismatch is ±iμ tan(πρ)z^ρ: the branched part of the gauge, seen only through the lip. No term of the
circle jumps changes, so N.6b's meromorphy is kept (the obstruction recorded in JZC_W_outer §6, row H-e, is avoided by the choice
of parametrix).

### 2.2 Lemma BT.2 (first-order formula and deformation)

**Lemma BT.2.** Let |ν| < 1, ρ > 0, ρ ≥ |ν|. Then at fixed large n, μ ↦ R_1(μ) is differentiable at 0 and
  ∂_μR_1|_0 = (engine's first-order circle response) + ∂_μR_1^{lip}, where for σ = 0
  ∂_μR_1^{lip} = (i tan(πρ) sin(π(ρ − ν))/π) ∫_0^δ x^ρ F(−x)dx + O(e^{−cn}),  F := R_in 𝒞L(ζ)𝒞^{−1} R_in^{−1},
with R_in the μ = 0 interior error matrix (analytic in U_0; N.6c). A lip factor σ adds the same term with tan πρ replaced by πσ/μ
(i.e. it acts on the lip term only, as μ tan πρ ↦ μ tan πρ + πσ).
*Proof.* (a) *Moments.* Paper 2 T3(b) (Conway–Deift Theorem 4.4, quoted there with hypotheses: A_±, B_± ∈ I + ∂𝒞(L^r), v_A, v_B, v_B^{−1} ∈ L^∞,
B_±^{−1} ∈ I + ∂𝒞(L^{r′})): A₁ − B₁ = −(1/2πi)∫A₋(v_A − v_B)v_B^{−1}B₋^{−1}. Take B = R at μ = 0, A = R at μ. At μ = 0 the lips carry no
jump (v_B = I there), and the circle part is the engine's (N.6c). The lip part of v_A − v_B is O(μ) in L¹ ∩ L^∞ when ρ ≥ |ν|: by Paper 2
Lemma bessel-local (iii) |Ψe₂e₁ᵀΨ^{−1}| ≤ C|ζ|^{−|ν|} for |ζ| ≤ 3, so the lip term is ≤ C|μ|n^{1−2|ν|}|z|^{ρ−|ν|} near 0 and ≤ C|μ||z|^ρe^{−c|ζ|^{1/2}}
beyond. With v_A − v_B = O(μ) in L^∞ ∩ L², the small-norm resolvent is Lipschitz in μ and A₋ = B₋ + O(μ) in L²; so ∂_μR_1 =
−(1/2πi)∫_{lips}R(∂_μv)R^{−1}ds (R has no jump on the lips at μ = 0, R₊ = R₋ = R_in) plus the circle part.
(b) *Deformation.* On the lip in ℂ_±, ∂_μv = ±iϱ_± tan(πρ)z^ρ 𝒞L𝒞^{−1}. F is analytic in U_0 ∖ [0, δ): R_in is analytic; P₀^∞, ρ_mod and
f^{1/4} are analytic across (−δ, 0); K_ν(2ζ^{1/2}) is analytic for |arg ζ| < π (from DLMF 10.32.9, valid for |ph w| < π/2). Between each
lip and (−δ, 0) the factor e^{−2w} gives |F| ≤ Cn^{…}e^{−c n|z|^{1/2}} on the arc |z| = δ, and near 0 |z^ρF| ≤ C|z|^{ρ−|ν|}n^{1−2|ν|} is
integrable. Rotating each lip onto the corresponding side of (−δ, 0) (oriented away from 0), with z = −x: z^ρ_± = x^ρe^{±iπρ},
ϱ_±·(±i)·z^ρ_± summed with the orientation gives −(1/2πi)·(i tan πρ)·(e^{iπ(ρ−ν)} − e^{−iπ(ρ−ν)})·(−1)∫_0^δx^ρF(−x)dx. ∎
(w_bt_mellin (5): direct quadrature of the two lip integrals against 2 sin(π(ρ−ν))∫x^ρF(−x)dx for an entire test prefactor, 2 (ρ, ν),
n = 100: agreement to the stated tolerance; control with cos fails.)

*Range.* For |ν| − ½ < ρ < |ν| the lip term is in L¹ ∩ L² but not L^∞; the formula is then the analytic continuation in ρ of the
proved one (the coefficients below are meromorphic in ρ), and it is used only as such.

### 2.3 Lemma BT.3 (Mellin moments)

**Lemma BT.3.** Let ν ∈ (−1, 1) real and 𝒦(s) := ∫_0^∞w^{s−1}K_ν(w)²dw.
(i) For Re s > 2|ν|: 𝒦(s) = 2^{s−3}Γ(s/2+ν)Γ(s/2−ν)Γ(s/2)²/Γ(s).
(ii) 𝒦(s+2) = q(s)𝒦(s), q(s) = (s² − 4ν²)s/(4(s+1)); ∫w^{s−1}K_νK_ν′ = −((s−1)/2)𝒦(s−1); ∫w^{s−1}K_ν′² = [(s−2)²/2 − ν²]𝒦(s−2) − 𝒦(s)
  (for s > 2 + 2|ν|).
(iii) tan(πρ)sin(π(ρ−ν))𝒦(2ρ+2) = −2^{2ρ}π²Φ_ν(ρ), Φ_ν(ρ) = Γ(−1−2ρ)Γ(ν+ρ+1)/(Γ(−ρ)²Γ(ν−ρ)).
*Inputs* (quoted in research/G1/CITATIONS.md (DLMF-3) and research/G1/RH/CITATIONS.md (DLMF-2), (DLMF-zeta, Plan 67)):
(10.32.9) "K_ν(z) = ∫₀^∞ e^{−z cosh t}cosh(νt)dt, |ph z| < ½π"; (5.2.1) "Γ(z) = ∫₀^∞ e^{−t}t^{z−1}dt", ℜz > 0; (5.12.1) "B(a,b) = Γ(a)Γ(b)/Γ(a+b)",
(5.12.3) "∫₀^∞ t^{a−1}/(1+t)^{a+b} dt = B(a,b)", "it is assumed ℜa > 0 and ℜb > 0"; (5.5.3) "Γ(z)Γ(1−z) = π/sin(πz), z ≠ 0, ±1, …".
*Proof.* (i) Insert 10.32.9 twice (w > 0); all integrands are positive, so Tonelli allows ∫dw first: by 5.2.1 (Re s > 0),
𝒦 = Γ(s)∫_0^∞∫_0^∞cosh νt cosh νu (cosh t + cosh u)^{−s}dt du. Extend to ℝ² (even integrand, factor ¼), put t = a+b, u = a−b (Jacobian 2),
cosh t + cosh u = 2cosh a cosh b, cosh νt cosh νu = ½(cosh 2νa + cosh 2νb): 𝒦 = Γ(s)2^{−s−1}𝒞(2ν, s)𝒞(0, s), 𝒞(λ, s) := ∫_ℝcosh(λa)cosh^{−s}a da.
With u = e^{2a}: ∫_ℝe^{λa}cosh^{−s}a da = 2^{s−1}∫_0^∞u^{(s+λ)/2−1}(1+u)^{−s}du = 2^{s−1}B((s+λ)/2, (s−λ)/2) by 5.12.3 (hypotheses:
Re(s ± λ) > 0, i.e. Re s > 2|ν| for λ = 2ν), and 5.12.1. Multiply. (ii) The ODE w²K″ + wK′ − (w² + ν²)K = 0 follows from 10.32.9 by
differentiating under the integral and integrating by parts twice (w sinh t e^{−w cosh t} = −∂_te^{−w cosh t}; boundary terms vanish).
q(s) from (i). The KK′ moment: w^{s−1}KK′ = ½w^{s−1}(K²)′, integrate by parts. The K′² moment: integrate w^{s−1}K′·K′ by parts and use the
ODE. Boundary terms vanish at ∞ (exponential decay from 10.32.9) and at 0 because K(w) = O(w^{−|ν|}), K′ = O(w^{−|ν|−1}) (bound 10.32.9 by
∫e^{−we^t/2}e^{|ν|t}dt) and s > 2 + 2|ν|. (iii) By 5.5.3 (ρ, 2ρ, ν − ρ ∉ ℤ): Γ(−1−2ρ) = π/(sin(2πρ)Γ(2ρ+2)), Γ(−ρ)^{−2} =
sin²(πρ)Γ(1+ρ)²/π², Γ(ν−ρ)^{−1} = sin(π(ν−ρ))Γ(1−ν+ρ)/π; so Φ_ν(ρ) = tan(πρ)sin(π(ν−ρ))Γ(1+ρ)²Γ(1+ρ+ν)Γ(1+ρ−ν)/(2π²Γ(2ρ+2)) and
𝒦(2ρ+2) = 2^{2ρ−1}Γ(ρ+1+ν)Γ(ρ+1−ν)Γ(ρ+1)²/Γ(2ρ+2). ∎ (w_bt_mellin (1)–(3); (1) is limited to 10⁻¹² by the quadrature at the
endpoint singularity, (2)–(3) to 10⁻³⁰; controls fail.)

Note that (iii) reproduces exactly the Γ-structure of the Laguerre branched coefficient (JZC_W_exact §2.2), which there came from a
connection formula NOT QUOTED; here Φ_ν(ρ) arises from quoted inputs only, and its "Weber–Schafheitlin" reading is not needed.

## 3. Theorem BT

### 3.1 The algorithm

In Lemma BT.2 put z = −v² (v > 0 on (−δ, 0)), v = V(y) the inverse of f^{1/2} (V(y) = (p+2)y(1 + O(y²)), odd), y = w/(2n). Write
L = (w/π)[K²L₁ + K′²L₂ + KK′L₃] (L₁ = ME₁₂M⁻¹, L₂ = ME₂₁M⁻¹, L₃ = M(iσ₃)M⁻¹) and S_i := R_in𝒞L_i𝒞^{−1}R_in^{−1}, a Laurent series in v
(the conjugation 𝒞 has a 1/v; R_in = Σ_kR_in^{(k)}n^{−k}, Taylor in z). Then x^ρF dx = Σ_i(2/π)yV^{2ρ+1}V′S_i(V)𝔣_i(w)dw, 𝔣 ∈ {K², K′², KK′},
and yV^{2ρ+1}V′S_i(V) = (p+2)^{2ρ+1}y^{2ρ+2}Σ_mτ_{i,m}y^m (finitely many m < 0). Termwise integration (the tail beyond the disc is
O(e^{−cn}); the Taylor remainders are integrable against w^{2ρ+2+m}e^{−2w}) and Lemma BT.3 give
  ∂_μR_1^{lip} = −(i/2)(p+2)^{2ρ+1}Φ_ν(ρ)n^{−2ρ−2}Λ(n),  Λ(n) = Σ_{i,m,k}τ_{i,m,k}a_{i,m}(2n)^{−m}n^{−k},
a_{i,m} := 𝔐_i(2ρ+3+m)/𝒦(2ρ+2) (rational in (ρ, ν) when the shift is even). Terms with an odd shift would carry 𝒦(2ρ+3)/𝒦(2ρ+2), which is
not rational; their total is **asserted to vanish** in every run (it does: the parity of S_i in v pairs K² and K′² with odd m and KK′
with even m). The extraction is the engine's: n^pb_n/c = (Q₁₂Q₂₁)^{1/2}, Q₁ = P₁ + R_1, so the companion of n^pb_n/c is
−(i/2)(p+2)^{2ρ+1}Φ n^{−2ρ−2}(Λ₁₂Q₂₁ + Q₁₂Λ₂₁)/(2(Q₁₂Q₂₁)^{1/2}); finally the natural form (N/n)^{(ρ+1)p}(·) is expanded in 1/N,
N = n + (β+1)/2 (the convention of JZC_W_exact §2.2 and of g1). Λ starts at n^{+1} (m = −1); that term cancels in the extraction
(asserted), so the companion starts at n^{−2ρ−2}. To get c_k one needs R_in to order k + 1 (engine KORD = k + 1). `w_bt_core.py`.

### 3.2 Statement

**Theorem BT (first order in μ; layer identity).** For the branched model of Def BT.0 with σ = 0, p > 0 (p ≠ 1; also the formal
p = −1), |ν| < 1, ρ > 0, ρ ∉ ℤ, the first-order μ-layer of n^pb_n/c (per unit μ of e^{−μz^ρ}) is
  (engine's symbolic-j layer at j = ρ)·C(2ρ,ρ)  +  (p+2)^{2ρ+1}Φ_ν(ρ)(n/N)^{(ρ+1)p}N^{−2ρ−2}[c_0 + c_1N^{−1} + c_2N^{−2} + …],
with c_k computed by §3.1, and (exact, `w_bt_companion`, `w_bt_predict`):
- c_0 = (pρ + 2ρ + 1)/2 and c_1 = 0 **identically in (p, ν, β, ρ)** (`w_bt_symp.out`, symbolic p, decoupled β); c_3 = 0 at
  p ∈ {−1, ½, 3/2, 2, 3, 5} identically in (ν, ρ) (a symbolic-p run at KORD = 4 was not completed for CPU time);
- c_k does not depend on β in the natural index (p = 3/2, identically in (ν, β, ρ), k ≤ 3); the raw n-expansion does (control);
- c_2: at p = 2: (192ν²ρ³ + 336ν²ρ² + 36ν² + 128ρ⁵ + 800ρ⁴ + 1504ρ³ + 1180ρ² + 492ρ + 45)/(192(2ρ+3));
  at p = 3/2: (3087ν²ρ³ + 4998ν²ρ² − 378ν²ρ + 756ν² + 2401ρ⁵ + 15092ρ⁴ + 30037ρ³ + 26047ρ² + 11426ρ + 1200)/(4992(2ρ+3));
  at p = 3: 5(225ν²ρ³ + 420ν²ρ² + 18ν²ρ + 27ν² + 125ρ⁵ + 775ρ⁴ + 1325ρ³ + 857ρ² + 334ρ + 24)/(528(2ρ+3));
  at p = 5: (5145ν²ρ³ + 9996ν²ρ² + 504ν²ρ + 315ν² + 2401ρ⁵ + 14749ρ⁴ + 22001ρ³ + 9779ρ² + 3690ρ + 180)/(816(2ρ+3));
  at p = ½ see `w_bt_companion_P.out`; no closed form in p was computed;
- c_4: at p = −1 the Laguerre rat_4; at p = 3/2, 3 in `w_bt_predict.out` (denominator (2ρ+3)(2ρ+5)).
Equivalently, per normalised tilt e^{−μz^ρ/C(2ρ,ρ)}: the companion is H(ρ)N^{−2ρ−2}(1 + X(ρ)N^{−2} + O(N^{−4})), H as in JZC_W_exact WE.4,
X(ρ) := c_2/c_0.
*Proof.* Lemma BT.1 splits the problem into the engine's circle problem (whose first-order layer at symbolic j is, at j = ρ, the
A_ρ-gauge layer: WE.1, Lemma N.6d) and the lip term; Lemma BT.2 gives the lip term's first-order contribution to R_1; §3.1 with Lemma
BT.3 evaluates it to every order; the listed values are the exact outputs. ∎

### 3.3 What "layer identity" means, and (F-br)

As in Theorem N.6(ii), Theorem BT is an identity of formal layers: the engine's circle data are formal series, and the lip term is
computed with R_in from the residue recursion. To read it as an asymptotic expansion of b_n for a **true** measure with a branched
tilt (or for the κ-problem) one needs:
- **(F-br)** the frame (Paper 2 F1–F8, N.6c small norm with remainder O(n^{−K−1})) for the tilted weight, uniformly for |μ| ≤ μ₀ — in
  particular Paper 2 (O3) for the branched band factor, whose Hölder exponent at 0 is ρ (GAP for ρ < ν_p); and ρ ≥ |ν| for Lemma BT.2(a).
Under (F-br), Lemma BT.2's error terms are uniform (R_in's expansion is uniform on U(0, δ/2), N.6c; the Taylor and tail remainders of
§3.1 are explicit), so the first-order response has the stated expansion with remainder O(n^{−2ρ−2−K−1}) in the companion.
Alternative route without (F-br) at μ ≠ 0 (not written): ∂_t log h_n = ⟨x^ρ⟩_n exactly (Toda, JZC_M4 §8), and ⟨x^ρ⟩_n is a functional of
the **untilted** problem's Y; Lemma BT.2's integral is that functional. This would make the first-order statement unconditional for the
lattice and Hurwitz measures (N.6, G1u frames, REVIEWED) but needs the node-sum interpolation of H-a for a branched test function.

## 4. Corollaries

**Cor BT.4.**
(a) *H.* c_0 = (pρ+2ρ+1)/2 gives JZC_W_exact's H(ρ) = ½(pρ+2ρ+1)(p+2)^{2ρ+1}Φ_ν(ρ)/C(2ρ,ρ). P0 (Res_{½}) and P1 (Res_{3/2}) of
  JZC_W_exact §3 are thereby consequences, not observations.
(b) *The dressing X.* c_2(½)/c_0(½) = X(p, ν) = [9p⁴+642p³+4588p²+11000p+7360 + 12(p+2)(5p³+24p²+44p−32)ν²]/(1536(p+4)(3p+2)) at
  p ∈ {½, 3/2, 2, 3, 5} (identity in ν), and at p = −1 (Laguerre). So Obs WE.6 (POST HOC there: rational reconstruction) is **derived**
  at these p; the refuted P2 form fails (control). The cached engine residues Res_{½}g1[5] of w_exact_poles (where present) equal
  −(p+2)²c_2(½)Res(Φ/C) (asserted). The full ρ-dependence of the dressing X(ρ) = c_2/c_0 is a rational function with denominator
  (2ρ+3)(pρ+2ρ+1) at the computed p; at ρ = ½ the derivation is exact, the identity in p of the X formula is still JZC_W_exact's reconstruction.
(c) *ρ = ½.* Engine layer and companion both have simple poles at ρ = ½ with opposite residues (P0, now a consequence of (a) and of the
  finiteness of the left side of Thm BT in ρ: the true layer is analytic in ρ near ½ since the tilt is). Their sum at ρ = ½ is
  2Res_{½}g1[3]·N⁻³log N + 2Res_{½}g1[5]·N⁻⁵log N + … (natural form, per normalised tilt), i.e. Finding WE.5's relative
  −(p+2)²(p+4)(1−4ν²)/(128p)N⁻²log N, with the next log coefficient fixed by c_2(½) = c_0(½)X(p, ν). Label: PROVED-mod (uniformity of the
  layer remainders in ρ near ½, which holds for the formal layers; for true measures under (F-br)).
(d) *E3.7 at n⁻¹ for branched tilts.* The lip term contributes O(|μ|n^{−2ρ−1}) to R_1 (Λ starts at n^{+1}) and O(|μ|n^{−2ρ−2}) to
  n^pb_n/c, so for ρ > 0 the n⁻¹ coefficient is the A_ρ-gauge's, d₁ + pM_ρ(4)μ = d₁ + (pρC(2ρ,ρ)/2)μ, exactly linear (JZC_W_exact WE.2
  route 1/2): first order PROVED as layer identity; all orders in μ CONDITIONAL on (F-br) (the higher lip orders are O(|μ|^kn^{−2ρ−1})
  in R_1 by the same bound).

**Prop BT.5 (pole terms carry no companion).** In the κ-problem (JZC_W_outer L W-out.4, P W-out.5(iii)) the branched band factor and the
lip phase are the two halves of exp(C_m(−z/n^p)^{q_m}), C_m = 2πa_m/sin(πq_m): in ℂ_±, (−z)^q = z^q(cos πq ∓ i sin πq), i.e. a band tilt
τ = C cos πq and a lip factor with πσ = C sin πq = τ tan πq. In Lemma BT.1(iv) (with μ = −τ) the mismatch exponent is
μ tan πq + πσ = 0. Hence the κ-problem's hard-edge parametrix built with ρ_a is **exact** (no lip mismatch, to all orders in the a_m):
the pole layers are exactly the analytic A_q-gauge layers, the engine's continued response at j = q_m with μ = −τ_m n^{−pq_m}. This is
W's pole term pR_qW(q)π cot(πq)(n/N)^pN^{−1−pq} (P W-out.7) **with** the continued dressing [1 + g(q)N⁻² + …] and no companion: the premise
of W′ (JZC_W_exact §4), from which W′'s closed form R_{1/2}W(½)π²(p+2)²(p+4)(1−4ν²)/256·n^{−3−p/2} follows (the exact limit there).
PROVED (algebra; inputs P W-out.5(iii), L W-out.4: NOT REVIEWED) as a statement about the decoupled model; as asymptotics of σ^{δ,κ}
it is CONDITIONAL on the transfer items of P W-out.6(ii) (H-b′, Hc.3 on the circles), but **no longer on BT**: the circle jumps are
G_aΔ^{mod}G_a^{−1} with G_a analytic in U_0, so N.6b applies. (`w_bt_companion_Q.out`: the trigonometric identity and τ tan πq = πσ for
τ_m = 2π cot(πq_m)a_m, σ_m = 2a_m; control σ = 0 fails.)

**Cor BT.6 (Hypothesis BT, first order).** For the band factor exp(Σ_ρτ_ρ(z/n^p)^ρ) with lip factors exp(±iπΣσ_ρ(z/n^p)^ρ) the first-order
layer in (τ_ρ, σ_ρ) is −Σ_ρ(pρW(ρ)/2)τ_ρ(n/N)^pN^{−1−pρ}[1 + g(ρ)N⁻² + …] plus the companions with μ_eff = (−τ_ρ + πσ_ρ cot πρ)n^{−pρ}, at
relative N^{−2ρ−1}. So BT's claim (σ_ρ do not enter at N^{−1−pρ}; error O(n^{−1−p min𝓡−η}), here η = min(2ρ+1, 2, p min𝓡 + …)) holds at
first order as a layer identity. Second order in (τ, σ) (products, BT's remainder) is not treated here.

## 5. The pre-registered test (Rule X)

`w_bt_predict.py` computed c_0…c_4 at p = 3/2 and p = 3 (lattice frame β = ν) and wrote at **11:14:19** the predicted residues of the
engine's N⁻⁷ coefficient g1[7] at j = ½ (from c_4), 3/2 (from c_2), 5/2 (from c_0), plus g1[6] = 0 and "the j-poles of g1[7] are exactly
½, 3/2, 5/2, simple". No KORD = 7 engine output existed before (the w_exact runs stop at KORD = 5, i.e. g1[5]). The test runs
(`w_bt_poles7.py`, KORD = 7, symbolic (ν, j)) started at 11:14:33. Note: `w_bt_core.py` was edited after the prediction run, only to
add the two control switches (`control=`); the prediction run's output prints the earlier sha256 (7ef4f425…), the computation is unchanged.
A first attempt (started 11:14:33) aborted in the engine's truncation guard ("principal part not determined", SHI = 24) before
computing any residue; the runs were restarted with SHI = 30 at 11:51:22 (still after the registration) and their outputs replace the
aborted ones.
**RESULT: all registered predictions hold, at both p, identically in ν** (`w_bt_poles7_p3_2.out`, `w_bt_poles7_p3.out`, 11 + 11
checks; 40 min engine time each): g1[0] = g1[2] = g1[4] = g1[6] = 0; the j-poles of g1[7] are exactly ½, 3/2, 5/2, simple; and
Res_{½}g1[7], Res_{3/2}g1[7], Res_{5/2}g1[7] equal the registered values, e.g. at p = 3/2
  Res_{½}g1[7] = −49(2ν−1)(2ν+1)(4070175984ν⁴ − 117588415000ν² − 145906122825)/330987359698944   (tests c_4, the N⁻⁴ dressing),
  Res_{3/2}g1[7] = 180075(2ν−3)(2ν−1)(2ν+1)(2ν+3)(9324ν² + 116461)/223338299392                 (tests c_2 at ρ = 3/2),
  Res_{5/2}g1[7] = 344123325(2ν−5)(2ν−3)(2ν−1)(2ν+1)(2ν+3)(2ν+5)/34359738368                  (tests H at ρ = 5/2).
Controls (c_4 → 0, c_2 → 0, opposite sign) fail. Unlike JZC_W_exact's P2, nothing here was refuted: the companion's own dressings
c_2(ρ) and c_4(ρ), which were never fitted, predict the engine's N⁻⁷ pole structure exactly.

## 6. Data provenance and independence

- The engine (m4_rh_exact2 copy) supplies R_in, R_1, f, 𝒞 — the μ = 0 hard-edge data of M(β, ν) — and the symbolic-j layer. The lip term
  uses only these and Lemma BT.3. Nothing is fitted; no constant was adjusted after comparison (the sign and normalisation of the lip
  term follow from Lemmas BT.1–BT.2, and the first comparison, with Laguerre, matched at all computed orders).
- Laguerre (p = −1): the comparison series rat_k come from the classical moment sum and a connection formula (JZC_W_exact §2.2,
  NOT QUOTED there, numerically checked to 10⁻⁵⁰); they are an independent computation.
- H and X were found in JZC_W_exact from the engine's pole residues (H pre-registered there, X post hoc); here they are outputs of a
  different computation (lip integral), so their agreement is a test of both.
- The N⁻⁷ residues (§5) are registered predictions.

## 7. Rule A log

1. *Circularity of "engine + companion".* The engine computes the A_ρ-gauge circle problem; the companion uses the same μ = 0 data but a
   different jump (the lips). If the lip term were mis-normalised, Laguerre would fail at c_0; if R_in were not needed, the control
   R_in → I would pass (it fails at c_2); if the K² moments did not matter, the control would pass (it fails at c_0).
2. *Sign of tan πρ, orientation of the lips.* Fixed by WE.1(iii) (R = z^{1/2}(z−4)^{1/2}, (z−4)^{1/2}/(4−z)^{1/2} = ±i) and Paper 2's
   orientation (lips away from 0, + on the left); the deformation identity is checked numerically including the factor 2 sin π(ρ−ν)
   (control 2 cos fails). Not adjusted to data.
3. *"The cross terms vanish."* Two cancellations are asserted, not assumed: the odd-shift Mellin part (𝒦(2ρ+3)) is identically 0, and
   the n^{+1} part of Λ cancels in the extraction. Both at every p computed.
4. *Is the companion really absent for integer ρ?* Φ_ν(j) = 0 (double zero of 1/Γ(−ρ)², simple pole of Γ(−1−2ρ)); tan πj = 0 in Lemma
   BT.1. Consistent with Theorem N.6. At half-integer ρ₀, tan has a pole and A_ρ too (C(2ρ,ρ)/(2ρ−1)); the sum is finite (Cor BT.4(c)).
5. *Degenerate ν.* ν = ±½: Φ_ν(½) has the factor (ν−½)(ν+½); all half-integer residues vanish (consistent with Lommel, Prop N.2). ν = 0:
   Lemma bessel-local (ii) (log case) gives the same bounds with logs; Lemma BT.3 holds at ν = 0.
6. *ρ range.* Lemma BT.2(a) needs ρ ≥ |ν| (L^∞); Lemma BT.3(ii) needs s > 2 + 2|ν| for the K′² moment at s = 2ρ+3+m, m ≥ −1, i.e.
   ρ > |ν| − ½. Below, only continuation (stated).
7. *β.* The decoupled run (p = 3/2) shows the companion depends on β only through N; the Laguerre case is β = ν − 1, the lattice runs β = ν.
8. *p < 1, p = −1.* The algebra is p-free; the analytic inputs for p < 1 (glued parametrix, seams) are those of E_plt1 and are not re-checked
   here for the lip term (the seam jumps are super-small and vanish to all orders at 0; the lip term is localised at |ζ| ≲ 1). p = −1 is
   formal (Laguerre identification of JZC_W_exact §2.1).
9. *Counterexample search for Prop BT.5.* A genuine mass/density tilt x^ρ interpolated by principal z^ρ has σ = 0 and a companion (Laguerre
   proves it is real); a tilt written as (−z)^ρ is not real on the band, so the two cases cannot be confused; the κ-problem's factor is
   E_κ = exp𝒞[ρ₁], analytic off [0, ∞) (P W-out.3), which is exactly the no-mismatch case.

## 8. What remains

- **(F-br)**, or the Toda/moment route of §3.3, to turn Theorem BT into an asymptotic statement for true measures with branched tilts
  (and Cor BT.4(d) beyond first order).
- **Second order** in branched tilts (BT's remainder; JZC_W's products of pole/fractional terms).
- **Closed forms in p** for c_2 (and c_4): only fixed-p values here (six p for c_2, p ∈ {−1, 3/2, 3} for c_4); a symbolic-p run of
  w_bt_core at KORD = 3 is the next step (it is the same code with PVAL unset).
- **The H-chain transfer for the κ-problem** (P W-out.6(ii)): with Prop BT.5 it no longer needs BT, only H-b′ and Hc.3 on the circles.
- Measure tests of the companion at ρ < ½ (JZC_W_exact §6 (a), (b)) and Rule R review of this note.
