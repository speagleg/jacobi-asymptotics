# Rule R review, reviewer A: the κ-family proof chain of Conjecture W (JZC_W_outer, JZC_W_kappa, JZC_W_BT)

Reviewer: independent second reader (Rule R), reviewer **A**, 2026-10-22, branch plan-e2-d2 (HEAD 4f3b3f7).
- **Targets** (all "NOT REVIEWED", research/G1/RH/spectral/):
  - JZC_W_outer.md, with checks w_outer_index, w_outer_scalar, w_outer_e2e;
  - JZC_W_kappa.md, with checks w_kappa_gauge, w_kappa_transfer, w_kappa_apriori, w_kappa_plt1;
  - JZC_W_BT.md, with checks w_bt_engine/core/companion/mellin/symp/predict/poles7.
- **Context read:**
  - JZC_W.md §1 (W(q), the statement) and JZC_W_exact.md §§0–2 (WE.1, WE.2, WE.3);
  - JZC_M4_proof.md §3 (N.6b) and l. 205–215 (N.6c's single use of the jump error);
  - the header and table of JZC_M3a_H.md;
  - m3a_e37_decoupled.py header (route 1/route 2);
  - E3.md Lemma E3.7 and REVIEW_PlanE3_A.md I1;
  - Paper 2 sec_5 (O1)–(O5), sec_6 (Table, Lemma szego, F1–F4), sec_7 l. 70–80, 300–360, 455–490;
  - RH/CITATIONS.md (DLMF-2), (DLMF-zeta, Plan 67), and G1/CITATIONS.md (DLMF-3).
- **Not my target:** JZC_SIGMA.md (reviewed separately).
- **What I did and did not touch:**
  - I edited nothing except this file.
  - All re-runs used a copy of the working tree in the scratchpad, with a fresh tmp/ cache (only tmp/w_exact was copied in, because w_bt_companion reads it).
  - My own scripts are in /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/mine/ (k1.py, we1.py).
- **No claim about RH.** No measure here is built from zeta zeros.

## Overall verdict

**ACCEPT WITH FIXES, all three memos.** I found no mathematical error in any lemma I re-derived. The list is in §1. The checks re-run
identically; the table is in §4. The findings are:
- one structural finding (**F1**), which is positive and changes the overall status;
- one precise answer to the (F-br) question (**F2**);
- eight MINOR fixes.

**F1 (the main point; the two memos do not close a loop that is closable).** JZC_W_kappa P K.12 leaves Conjecture W at first
order in the poles CONDITIONAL on Hypothesis BT_coh. JZC_W_BT Prop BT.5 says the pole terms "no longer" need BT but need "H-b′ and Hc.3
on the circles". Neither memo uses the other:
- W_kappa only cross-references BT.5 (§4.1, "not used in any proof here");
- W_BT does not know that W_kappa has proved the transfer items.

Put together, and adding one REVIEWED input that neither memo cites (m3a_e37_decoupled route 1 = the decoupled E3.7 identity
e(M) − e(0) = cp·M(4c), all orders in the gauge), **BT_coh follows** at the precision P K.12 needs (§2, fix text R1). What is left is:
- the NOT-REVIEWED status of the inputs;
- one written assembly paragraph (R1);
- **not** (F-br).

**F2 ((F-br)).** (F-br) is the analytic frame (Paper 2 F1–F8 plus N.6c with O(n^{−K−1}) remainder) for a *general* branched band
factor, plus ρ ≥ |ν| for the lip-term derivative of Lemma BT.2.
- For the κ-family the band factor is **coherent**. Its frame is exactly what W_kappa proves: P K.5 (H-b′), L K.6–K.7, P K.8(B)
  (order-K small norm), L K.10 (transfer of the circle data), and P K.13 ((O3) replaced by the X-cancellation).
- There is no lip term, so ρ ≥ |ν| is not needed.
- So **W_kappa's transfer lemmas do prove the κ-instance of (F-br)**. They do **not** prove (F-br) for non-coherent tilts, e.g. a
  genuine x^ρ mass tilt, which is σ = 0 with τ ≠ 0. There L K.9 shows the lip-matched data are not meromorphic, and P K.13's
  cancellation (exponent ½ instead of ρ) uses coherence.
- (F-br) for general branched tilts remains a GAP. It is irrelevant to the κ-family.

**Honest status of Conjecture W for σ^{δ,κ}** (λ_k = (k + δ)^p + κ, p > 1, −1 < δ ≤ 0, κ ∉ {0}, κ > −a^p, |α| < 1). This is §3, stated
precisely there.
- *Up to the order n^{−1−p} (exclusive)*, W holds in the following form:
  - the κ-free Szegő shift β′ = α + 2δ;
  - every n^{−k} coefficient with k < p equal to that of M(α + 2δ, α);
  - the single pole term pR_{q₁}W(q₁)π cot(πq₁)n^{−p}, with W's exact coefficient.
  - **Label:** PROVED-mod-cite; NOT yet REVIEWED as a chain. Several inputs are unreviewed: W_outer L W-out.0–5, P W-out.3, P W-out.5;
    W_kappa L K.1–K.10, P K.5, K.8; W_BT BT.1(iii) and BT.5; W_exact WE.1. I re-derived all of them except Paper-2-level steps quoted
    from REVIEWED notes.
  - Once R1 is written and the fixes applied, the chain can be labelled REVIEWED, subject to a reviewer B.
- *At first order in the pole tilts and to all orders of their dressing* (the continued engine series at j = q_m, by BT.5), with
  integer and Toda layers from Theorem N.6, the remainder is O(n^{−2p}). The remainder comes from second order in the branched data.
  These are formal-layer statements made into asymptotics by P K.12. W's "first order in the poles" form therefore holds to O(n^{−2p}).
- *Not covered:*
  - second-order (product) terms;
  - p < 1 (OBSTRUCTION for the lattice-g route, P K.14);
  - p = 1/m;
  - α ∉ (−1, 1).

## 1. Per-memo, per-lemma verdicts

### 1.1 JZC_W_outer.md

| Item | Re-derived | Verdict |
|---|---|---|
| L W-out.0 | Yes: (1.2) continuation; the residue −binom(q_m, m)κ^m/p; binom(−w, m) = (−1)^m w/m + O(w²) gives (−κ)^m at p = 1/m; (c) via the K₀-shift | ACCEPT (PROVED) |
| L W-out.1 | Yes: t∘ζ = (n^p/z − κ)^{1/p}; non-node argument for κ < 0 uses t_∞ < a | ACCEPT |
| L W-out.2 | Yes: θ_κ′/θ′ = (t_κ/t)(ζ/z) = (1 − z/z_*)^{1/p−1} | ACCEPT (PROVED-mod-cite) |
| L W-out.3 | Yes, (a)–(d); |F_κ| ≍ z′^{2δ+1}|z − z_*|^{−δ−½} from −ζ = zz_*/(z − z_*) | ACCEPT |
| Remark 3.6 | Follows from (d) | ACCEPT |
| P W-out.3 | Yes: the jump products e^{2πi(t_κ−δ)}e^{2πiδ}e^{2πi(t−t_κ)} = e^{2πit}; at z_* the log-coefficient ρ(z_*−) − ρ(z_*+) = δ + ½; the κ < 0 limit at ∞ (exponent ½, phase agreement) | ACCEPT |
| L W-out.4 | Yes: band, lip and Σ_v identities, as in Hd | ACCEPT. Its last paragraph about (O3) for 1 < p < 2 is superseded (B4) |
| L W-out.5 | Yes, the scaling argument | ACCEPT |
| P W-out.5 | Yes, all parts (see the note below) | ACCEPT (PROVED-mod-cite; hypotheses of 5.12.1, 5.12.3, 5.5.3 checked) |
| P W-out.7 | Yes: (−pqW/2)(−2π cot(πq)R/q) = pRWπ cot(πq); a₁ = κ/p = −R_{q₁}/q₁ | ACCEPT |
| P W-out.6 | (i) ACCEPT. (ii) and (iii) are **superseded**: by P K.11 for (iii), and by P K.12 + R1 for (ii) | FIX B4 |
| §7 | Sharpened by P K.14 | ACCEPT as OBSTRUCTION (heuristic) |

Note on P W-out.5. I checked:
- the coefficient of z^j through ζ^k = z^kΣbinom(k+l−1, l)(z/z_*)^l and (1/k)binom(j−1, k−1) = (1/j)binom(j, k);
- the κ > 0 finite part via B(s, 1 + r) = 0 at s = −r − j;
- the κ < 0 finite part: the (0, ∞) piece −nz′^sΓ(s)Γ(j)/Γ(−r), the (−∞, −z′) piece (−1)^j nz′^sΓ(j)Γ(1+r)/Γ(1+r+j), and their
  cancellation by 5.5.3 (Γ(−r−j)/Γ(−r) = (−1)^jΓ(1+r)/Γ(1+r+j));
- the sign bookkeeping μ = 2Z/j − 2κ^jζ(0,a)/j (Hurwitz∘ζ) − B_j (density) + 2κ^jζ(0,a)/j (gauge).

### 1.2 JZC_W_kappa.md

| Item | Re-derived | Verdict |
|---|---|---|
| L K.1 | Yes: sin(πq_m) = −(−1)^m sin(π/p); (−z)^{q_m} = (−1)^m z^m(−z)^{−1/p}; Σa_mw^m = 1 − (1 − κw)^{1/p}; Ψ₀ = 𝒞(0) + π cot(π/p)ρ₁ − ζ(0,a)log(1 − z/z_*); exponent 1/p − 1 + 2ζ(0,a) = 1/p − 2a | ACCEPT. **Independently confirmed** (k1.py, no shared code): quadrature of 𝒞[ρ₁] minus the closed form is constant to ≤ 9·10⁻¹⁸ at 4 parameter sets incl. κ < 0 (ρ̃ part); the π cot control fails by 0.16–2.2 |
| Cor K.1′ | Yes: (cot πq ∓ i) = e^{∓iπq}/sin πq | ACCEPT |
| L K.2 | Yes: inclusions {λ ≤ T^p} ⊂ {τ ≤ c₋^{−1/p}T}, {λ > T^p} ⊂ {τ > c₊^{−1/p}T} | ACCEPT |
| L K.3 | Yes, arc bound (i)–(iii): |w|² = (A − κ)² + 2Aκ(1 − cos ψ); c_p = 8/(3π²p) | ACCEPT |
| L K.4 | Yes: X₊X₋ = e^{2Ψ₀}e^{−2Ψ₀} = 1 ⇒ L odd ⇒ L = 𝓡A_X; removability by B/|z|^{½} = o(1/|z|); max principle on a fixed circle | ACCEPT. This is the key new estimate; it is correct |
| P K.5 | Column factorisation F♮_κD_W = (F_κD^♭_α)·G·X checked | ACCEPT (PROVED-mod-cite) |
| L K.6 | Yes: W̃_κ² = e^{∓iπβ′}e^{∓2πiρ₁}W₀^κ; ϱ_±ρ♮_κ^{−2} = e^{±2πi(δ+ρ₁)}ω^{(β′)}; (v) from ρ♮ = ρ^♭/X | ACCEPT |
| L K.7, P K.8 | Logic checked against the cited G1u items | ACCEPT (PROVED-mod-cite) |
| L K.9 | Coherent part: parity argument quoted correctly from N.6b | ACCEPT. Non-coherent part: FIX B6 |
| L K.10 | Yes: log(ρ♮_κ/ρ_BT) = ∓iπ tail_M − ½T via (eq:szego-repr) with 𝔠 = E(z); E = E₁ + E₂ + E₃; M ≥ J + 1 ⇒ p(M+1) − 1 ≥ (J+1)p | ACCEPT |
| P K.11 | Yes: the jump difference Σ_{k≥1}O(n^{1−p})n^{−k} = O(n^{−p}); N.6c uses the jump error once | ACCEPT (PROVED-mod-cite) |
| P K.12 | Reduction ACCEPT. The CONDITIONAL label can be removed after R1 (§2). The phrase "to N.6's orders in the integer and Toda layers" overclaims | FIX B3 |
| P K.13 | Yes; Paper 2 grep re-done | ACCEPT. Precision fix B5 |
| P K.14 | Yes: e(p) = (1 − p)(2 + p)/p from n^{1−p}n^{−2q₁}; sign of log|e^{2πiρ₁}| on both lips | ACCEPT (PROVED given (G); OBSTRUCTION for the route) |
| §6.3 | Not reviewed as mathematics | PROOF SKETCH, correctly labelled |

### 1.3 JZC_W_BT.md

| Item | Re-derived | Verdict |
|---|---|---|
| Lemma BT.1 | Yes: log D_h = −(μ/2)g, g = z^ρ − RM_ρ, g₊ + g₋ = 2x^ρ; RM_ρ = RA_ρ ± i tan(πρ)z^ρ (g = (−z)^ρ/cos πρ − RA_ρ near 0); the mismatch (ω − ω_a)ρ_a² = ϱ_±(e^{±i(μt+πσ)z^ρ} − 1) | ACCEPT. Wording fix B8 ("to first order" in (iii): the identity is exact) |
| Lemma BT.2 | Deformation algebra checked | ACCEPT as a formal-layer formula. Label fix B9 (the analytic statement presupposes the small-norm solvability of the tilted model, i.e. part of (F-br)) |
| Lemma BT.3 | Yes: (i) the ℝ² change of variables gives 2^{−s−1}𝒞(2ν)𝒞(0) and Γ(s); u = e^{2a} gives 2^{s−1}B; (iii) via 5.5.3 three times | ACCEPT (PROVED-mod-cite). Citation gate passed: 10.32.9 in G1/CITATIONS (DLMF-3); 5.2.1 in (DLMF-zeta); 5.5.3, 5.12.1, 5.12.3 in (DLMF-2); hypotheses checked: Re(s ± 2ν) > 0, |ph w| < π/2, non-integer arguments |
| Thm BT | — | ACCEPT as a formal-layer identity (c_0, c_1 symbolic; c_2–c_4 at the listed p only, as stated) |
| Cor BT.4 | — | ACCEPT with the labels given |
| Prop BT.5 | Yes: coherent data give μ tan πq + πσ = −τ tan πq + 2πa = 0, and ρ_BT = ρ_aexp(∓(i/2)(μ tan πρ + πσ)z^ρ) = ρ_a exactly | ACCEPT. Statement fix B7 (q = ½, i.e. p = 2) and B2 (its conditional clause) |
| Cor BT.6 | μ_eff = μ + πσ cot πρ | ACCEPT (first order, layer identity) |
| §5 Rule X | — | ACCEPT. Fixes B1 |

## 2. F1 in detail: BT_coh from BT.5 + WE.1 + decoupled E3.7 (fix text R1, for JZC_W_kappa §4.3)

Proposed insertion after P K.12:

> **Proposition K.12′ (BT_coh at the order P K.12 needs).** For coherent data (β, ν; μ_n, (σ_ρ)_{ρ∈𝓡}) with μ_{n,j} = O(n^{−jp}) and
> bounded σ_ρ,
>   𝔅_n^{rec}[BT_coh] = 𝔅_n[M(β, ν); μ_n] − Σ_{ρ∈𝓡}(pρW(ρ)/2)τ_ρ n^{−1−pρ} + O(n^{−2−p·min𝓡}),
> and more precisely the first-order part in (τ_ρ) is Σ_ρ (engine symbolic-j layer at j = ρ) with μ = −τ_ρn^{−pρ}, to all orders in 1/n.
> The remainder of that refined form is O(n^{−2−2p·min𝓡}), the second-order part.
>
> *Proof.*
> (a) **Gauge form.** By coherence and JZC_W_exact WE.1(iii), ρ_BT = ρ_a := ρ_mod·exp(−½Σ_ρμ_ρRA_ρ)·(Toda gauge), with μ_ρ := −τ_ρn^{−pρ}.
>   This is JZC_W_BT BT.1 with the mismatch exponent μ tan πρ + πσ = 0 (Prop BT.5). Hence Δ_k^{BT} = G_aΔ_k^{mod}G_a^{−1}, with G_a
>   the E3 gauge of the tilt function M = Σ_jμ_jQ_j + Σ_ρμ_ρM_ρ. G_a is exactly E3's G, since P₀^∞e^{hσ₃}(P₀^∞)^{−1} = cosh h + (sinh h/R)·RN
>   with N² = I and RN = T[[0, z−4c], [z, 0]]T^{−1}. Its Taylor data at 0 (A_ρ) and at 4c (M_ρ) are the engine's symbolic-j data at j = ρ (WE.1(i)–(ii)).
> (b) **Entire dependence.** By N.6b (REVIEWED), every Laurent coefficient of Δ_k^{BT} is entire in the times (μ_j, μ_ρ) with n-free
>   coefficients. So each order n^{−k} of 𝔅^{rec} is entire in the times. Its value at μ_ρ = 0 is 𝔅_n[M(β, ν); μ_n] (Theorem N.6).
> (c) **The n⁻¹ order.** By the decoupled E3.7 identity (m3a_e37_decoupled route 1, REVIEWED: e(M) − e(0) = cp·M(4c) identically in
>   M(0), M(4c), M′(4c)), the n⁻¹ coefficient is exactly linear in the times, with no products. Its ρ-part is
>   cp·μ_ρM_ρ(4c) = (pρW(ρ)/2)μ_ρ (WE.1(i) at m = 0, with c-scaling; W(ρ) = c^ρC(2ρ, ρ), JZC_W §1).
> (d) **Orders n^{−k}, k ≥ 2.** By (b) these are O(|μ_ρ|) = O(n^{−p·min𝓡}) for the first-order part, and O(|μ_ρ|²) beyond.
> (e) Finally (n/N)^pN^{−1−pρ} = n^{−1−pρ}(1 + O(1/n)). ∎
>
> **Consequently** Hypothesis BT_coh holds with η = 1. P K.12 (ii) is PROVED-mod-cite, with inputs: L K.10, P K.8, and the
> W_outer inputs (NOT REVIEWED); BT.1(iii), BT.5 (NOT REVIEWED); WE.1 (NOT REVIEWED); m3a_e37_decoupled, N.6b, N.6c (REVIEWED).

Reviewer checks for R1:
- (a) The algebra of BT.5 and the identity ρ_BT = ρ_a, by hand.
- (a) WE.1(ii) at the κ-family's exponents, by an **independent** quadrature (we1.py). I took M_ρ := z^ρ/R − 2C_ρ, with C_ρ the Cauchy
  transform of x^ρ/R₊ (derived from g₊ + g₋ = 2x^ρ, g = O(1)). At ρ ∈ {⅓, 4/3, 0.7} and four points, including both sides of the negative
  axis, M_ρ − tan(πρ)z^{ρ−½}(4−z)^{−½} equals the stated Taylor series of A_ρ to ≤ 6·10⁻¹⁸. That is the quadrature limit at dps 30; my
  script's 10⁻²⁰ threshold was too strict, so it printed FAIL, but the deviations are at the quadrature floor. The control "no branched
  term" misses by 0.9–3.3. ρ = 4/3 = q₂ at p = 3/2 tests the continuation beyond ρ < 1.
- (c) WE.2 route 2 independently confirms (c) at first order (response pj/2 per unit μC(2j, j), symbolic j, zero at orders 2 and 3).
  The re-run w_bt_poles7 asserts g1[1] = pj/2 at p = 3, 3/2.

Caveats (why this is "PROVED-mod-cite", not more):
- WE.1 is NOT REVIEWED (elementary; spot-checked above).
- The proof assumes 𝔅^{rec} is the *finite* recursion at fixed K, as in K.12's definition. Uniformity in n of the n^{−k} coefficients
  holds because, in the n^p frame, the model data are n-free and only the times depend on n.

**p = 2.** Here all q_m are half-integers, so τ_m = 0 and the data are pure lip factors exp(C(−z/n^p)^{q}). R1(a) still holds in the
limiting form, because (−z)^{½} = −R/(4−z)^{½} is of engine form. W's pole terms vanish (cot = 0). The W′ term, n^{−3−p/2} = n^{−4}, lies inside R1's coarse
remainder O(n^{−2−p/2}) = O(n^{−3}), so there is no conflict with W′. In the refined form it is part of the continued first-order
layer (JZC_W_exact: exact limit).

## 3. Overall status of Conjecture W for this node family (precise)

Assume (S) of JZC_W_outer §0 with p > 1. Write t_j = −2Z_κ(−j)/j + B_j and q_m = m − 1/p.

**(W-κ, first order in the poles).** n^pb_n(σ^{δ,κ})/c equals the sum of:
- 𝔅_n[M(α + 2δ, α); t] (Theorem N.6's formal series with Toda times t);
- Σ_m (the continued symbolic-j layer at j = q_m with μ = −τ_mn^{−pq_m}), whose leading term is
  pR_{q_m}W(q_m)π cot(πq_m)(n/N)^pN^{−1−pq_m};
- O(n^{−2p}).

**Label:** PROVED-mod-cite, *conditional only on the Rule R status of the inputs listed in R1*. It is no longer conditional on any
hypothesis (BT, BT₀, BT_coh, (F-br)).

Truncated to W's own displayed form, i.e. the pole term only at leading order (1 + O(N^{−1})), the remainder is O(n^{−1−p}). In that
range:
- the only pole term is m = 1, at n^{−p};
- every integer coefficient n^{−k} with k < 1 + p is that of M(α + 2δ, α), κ-free;
- the first Toda layer (t₁ at n^{−1−p}) needs the refined form.

**Numerical consistency** (W_outer §8, re-run status in §4): d₁ to 10⁻¹⁰ and d₂ to 5·10⁻⁸ at p = 2.5; the n^{−p} pole term to 4·10⁻⁷.

**Not covered:** second-order branched terms (O(n^{−2p})); p < 1 (OBSTRUCTION, route-specific); p = 1/m; α ∉ (−1, 1).

**Novelty:** UNCHECKED. No Rule L pass has been done.

## 4. Re-run of the checks

Setup:
- Copy of the tree; fresh tmp/; python = session venv, -B.
- Two shared cores; the other reviewer's jobs were running concurrently, so wall times are roughly ×2 the recorded ones.
- Outputs were compared with the stored .out after deleting timings and run-start timestamps.

| Script | Result | vs stored .out |
|---|---|---|
| w_outer_index | ALL 104 PASSED | byte-identical |
| w_outer_scalar | ALL 125 PASSED | identical (modulo timings) |
| w_outer_e2e, run 1 (fresh: empty tmp/w_cache, so predictions and all three 120 000-atom measures regenerated, ~70 s each) | ALL 43 PASSED | every fitted value, tolerance and control miss identical. 43 = 44 minus "stored predictions reproduced", which exists only on a second run |
| w_outer_e2e, run 2 (on run 1's caches) | ALL 44 PASSED (incl. "stored predictions reproduced") | identical to the stored .out apart from run and predictions timestamps |
| w_kappa_gauge | ALL 94 PASSED | identical |
| w_kappa_transfer | ALL 43 PASSED | identical |
| w_kappa_apriori | ALL 36 PASSED | identical apart from the "(t …s)" elapsed-time stamps (≈ 55 min wall time) |
| w_kappa_plt1 | ALL 27 PASSED | identical |
| w_bt_companion Q / L / P / B | 6 / 10 / 30 / 3 PASSED | identical. P reads the cached w_exact residues (tmp/w_exact copied in) |
| w_bt_mellin | ALL 11 PASSED | identical |
| w_bt_symp | ALL 5 PASSED | identical |
| w_bt_predict 3/2 3 | completes | identical apart from the w_bt_core hash and time; JSON p-block identical |
| w_bt_poles7 3 (SHI=30, stored predictions) | ALL 11 PASSED (engine 1170 s) | identical |
| w_bt_poles7 3/2 (SHI=30, stored predictions) | ALL 11 PASSED (engine 641 s) | identical |
| reviewer k1.py (L K.1, independent) | spread ≤ 9·10⁻¹⁸; π cot control misses by ≥ 0.16 | — |
| reviewer we1.py (WE.1(ii), independent) | deviation ≤ 6·10⁻¹⁸ (quadrature floor); control misses by ≥ 0.9 | — |

Assertion count for JZC_W_BT's "76 assertions incl. 17 controls (+ 11 numerical)": 6+10+30+3+5+11+11 = 76 exact; w_bt_mellin's 11 are the
numerical ones. Consistent.

**Rule X / pre-registration audit (JZC_W_BT §5):**
- w_bt_predictions.json says "written 11:14:19". Both stored KORD-7 outputs record a run start of 11:51:22, i.e. later. Their file
  mtimes (12:31) are consistent with the recorded 2385 s.
- w_bt_engine.py differs from w_exact_engine.py **only** by the docstring and the two `EXPORT` lines (diff checked).
- w_exact_engine.py differs from m4_rh_exact2.py (sha 2d18e259…) only by the PVAL/SZOFF switches.
- The stored prediction run printed w_bt_core sha 7ef4f425…; the current file is 116335d9…. The memo says the edit only added
  `control=` switches. My re-run of w_bt_predict with the current w_bt_core (in a separate copy, so as not to touch the JSON the KORD-7 runs read)
  reproduces every predicted c_k and residue exactly. The "p" block of the regenerated JSON is identical to the stored one, and the
  .out is identical except for the w_bt_core hash and the timestamp. **The post-registration edit did not change the computation.**
- Both KORD-7 tests were re-run against the **stored** (11:14:19) predictions JSON, with SHI=30, and passed 11/11 each.

## 5. Fixes

**B1 (MINOR, reproducibility; W_BT §5, header l. 18, w_bt_poles7.py).**
- The script sets `os.environ.setdefault("SHI", "24")`. The memo says SHI = 24 aborted and the stored runs used SHI = 30. The .out does
  not print SHI, so the committed script does not reproduce the stored output without an undocumented environment variable.
- Fix: change the default to "30" (or print SHI in the output header). Change header l. 18 "(engine runs started 11:14:33)" to "(the
  runs whose outputs are stored started 11:51:22; an earlier attempt at 11:14:33 aborted, §5)".
- I reproduced both stored outputs with SHI=30 exported (§4).

**B2 (MINOR, label consistency; W_BT Prop BT.5, §0 item 3, §8 item 4).**
- Replace "CONDITIONAL on the transfer items of P W-out.6(ii) (H-b′, Hc.3 on the circles), but no longer on BT" with: "as asymptotics
  of σ^{δ,κ}: PROVED-mod-cite via JZC_W_kappa P K.5, L K.10, P K.12 and Prop K.12′ (R1); the leading coefficient of the analytic layer
  is m3a_e37_decoupled route 1 with WE.1".
- §8's "H-b′ and Hc.3 on the circles" bullet: done (W_kappa).

**B3 (MINOR, overclaim; W_kappa P K.12 statement and §4.3 last paragraph).**
- "to N.6's orders in the integer and Toda layers" holds only up to the second-order branched remainder O(n^{−2p}), and only if the
  first-order pole layer is taken with its continued dressing. With "(1 + O(N^{−1}))" the error is O(n^{−1−p}).
- Replace "+ O(n^{−p−η})" by the two precise forms of §3. Replace "under Hypothesis BT_coh (CONDITIONAL)" by "by Prop K.12′".
- Update the status table row P K.12 and the "Main outcome" paragraph.

**B4 (MINOR, apply the author's own corrections; W_outer).** W_kappa §9 item 5 lists them; I agree with all, but none has been
applied. Apply:
- §4 last paragraph and §10 item 3 (1 < p < 2: no restriction, P K.13);
- §6 rows H-b′ (→ P K.5), H-c (→ L K.10), H-e (→ L K.9, P K.11);
- P W-out.6 (ii) → "PROVED-mod-cite (W_kappa P K.12 + K.12′)", and (iii) → "PROVED-mod-cite (W_kappa P K.11)";
- Hypothesis BT: restrict to coherent tilts for the κ-family, pointing to W_BT for the non-coherent companion;
- §10 item 1 "the *only* gap": now closed by R1.
- Also update the table rows of P W-out.6 and the "(ii) holds at n^{−p}" sentence.

**B5 (MINOR, precision; W_kappa P K.13(b)).**
- (O3) is also invoked in Paper 2 sec_6 l. 182 ("by (O3)–(O4), log H° is bounded on (0, 4c)") and l. 283 (the polynomial bound for
  log W₀ on 𝒵_n).
- Both use only boundedness, which H_n^κ satisfies (|ρ₁| ≤ Cn^{1−p} on [0, 4c]). So the conclusion stands.
- Add these two lines to (b) ("the exponent of (O3) is used only in …; (O3) is also used at sec_6 l. 182, 283 for boundedness only").

**B6 (MINOR, scope; W_kappa L K.9 non-coherent part and §8 item 6).**
- The jump of Δ₁ across (−δ_r, 0) is for the *lip-matched* parametrix.
- With JZC_W_BT's analytic-gauge parametrix (BT.1), non-coherent circle data stay meromorphic and the mismatch moves to a lip term.
- Add: "for the lip-matched parametrix; JZC_W_BT Lemma BT.1 gives a meromorphic alternative with an explicit lip term (Theorem BT)".

**B7 (MINOR, degenerate case; W_BT Prop BT.5).**
- At q = ½ (p = 2 for all m) "πσ = τ tan πq" is 0·∞, since τ = 0 and tan is infinite.
- State BT.5 through the single factor exp(C(−z/n^p)^q), C = 2πa/sin πq. This is in engine form for every q, including
  (−z)^{½} = −R/(4−z)^{½}.
- Note that the pole term vanishes there and the W′ term is the limit (W_exact).

**B8 (MINOR, wording; W_BT BT.1(iii) proof).**
- "to first order, R·P₀^∞σ₃(P₀^∞)^{−1} = T[[0, z−4], [z, 0]]T^{−1}" is an exact identity, and the engine uses the full cosh/sinh gauge.
- Write "exactly", and add the line P₀^∞e^{hσ₃}(P₀^∞)^{−1} = cosh h·I + (sinh h/R)·RN, N² = I. R1(a) relies on exactness.

**B9 (MINOR, label; W_BT Lemma BT.2).**
- The differentiability of μ ↦ R_1(μ) at fixed n via Conway–Deift presupposes that the tilted model's error problem exists with
  R_± ∈ I + ∂𝒞(L²). That is part of (F-br) and is not cited.
- Label BT.2 as "formula PROVED for the formal lip layer; as a derivative of the true R_1: CONDITIONAL (F-br)". Theorem BT's layer
  label is unaffected; nothing in the κ-family uses BT.2.

## 6. Rule A (reviewer's adversarial attempts)

1. *Is BT.5's coherence the same coherence as W_kappa's?* Both reduce to τ = π cot(πρ)σ. BT.5: τ = −μ, πσ = τ tan πq. W_kappa:
   τ_m = π cot(πq_m)σ_m with σ_m = 2a_m. The lip sign convention matches L W-out.4: the (2,1) entries carry e^{±2πiρ₁} = e^{±iπσz^q}.
2. *Could second-order terms reach n⁻¹?* No: route 1 is exact in M at n⁻¹. A naive count would put τ₁² at n^{1−2p}, above n^{−1−p} for
   p < 2; route 1 rules this out.
3. *Is "(O3) fails for 1 < p < 2" a gap?* Every Paper 2 use was re-grepped (B5); the exponent enters only through ω (L K.6(iv)–(v)).
4. *κ ≥ a^p, κ near −a^p, δ = −½ (ζ(0, a) = 0):* the memos handle all three (L W-out.0 K₀ split; t_∞ < a; controls de-asserted at δ = −½).
5. *Independence:* k1.py and we1.py share no code with the repo.

## 7. Items for the authors (summary)

R1 (write Prop K.12′); B1–B9. No RETRACTED item. No stop condition hit.
