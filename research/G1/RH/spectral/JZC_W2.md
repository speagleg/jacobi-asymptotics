# JZC W2: Conjecture W for λ_k = (k + δ)^p + κ at second order in the poles (pole² and pole×Toda layers)

Status (2026-10-22): **NOT REVIEWED** (no Rule R reader). Labels per VERIFICATION_POLICY.md; NOT REVIEWED applies to every item
of this note. Novelty: UNCHECKED (no Rule L pass). No claim about RH: no measure built from zeta zeros is used. Scope:
JZC_W_kappa §9 item 1 ("second order in the poles: products of branched terms, the O(n^{−2p}) remainder of P K.12's refined form").
Inputs, with their labels: JZC_W_kappa P K.12 and Prop K.12′ (PROVED-mod-cite + REVIEWED; review A, and review B
research/G1/review/REVIEW_JZC_W_WE1_K12p_B.md for K.12′ and the assembly); JZC_W_BT Prop BT.5 (PROVED + REVIEWED); JZC_W_exact
Lemma WE.1 (REVIEWED by review B); m3a_e37_decoupled route 1 and JZC_M4_proof N.6b–c, Theorem N.6 (REVIEWED). No external theorem is
used beyond those quoted in the cited notes (Rule C: nothing new to quote).

Checks (all in `checks/`, Python = the session venv, `-B`; caches in `tmp/w2/`; every `.out` prints the sha256 of its script, of
the modules it uses and of the engine):
- `w2_engine.py`: a copy of m4_rh_exact2.py (sha256 2d18e259…cbc06, **not modified**) with **two** nilpotent band-factor
  parameters e₁, e₂ of independent exponents j, k (symbolic, or fixed rationals), E3's full cosh/sinh gauge of M = e₁Q_j/C(2j,j) +
  e₂Q_k/C(2k,k) through the symbolic Taylor data at 0 and 4 (= A_ρ, M_ρ of WE.1 at j = ρ); changes 1–7 in its docstring. With E2 = 0
  it is m4_rh_exact2's EO = E1 symbolic-j run; NT (change 7) defaults to m4_rh_exact2's 12.
- `w2_exact.py` → `w2_exact_{B,T,M,Q,H}.out` (§2, exact identities).
- `w2_common.py` (times, the formal prediction from cached exact engine runs), `w2_predict.py` → `w2_predict.out`,
  **`w2_predictions.json`** (§4.1, the registration, 2026-10-22 16:56:01 MDT).
- `w2_data.py` (double-double atoms, a binary128 RKPW kernel copy, an exact-κ smooth tail, y in mpmath), `w2_fit.py` →
  `w2_fit_P15.out`, `w2_fit_P25.out` (§4.2).
- `w2_cross.py` → `w2_cross.out` (Rule A: the prediction machinery against the numeric engine m4_rh4 and W's first-order term).

| # | Statement | Label |
|---|---|---|
| **Prop 2.1** | (formal layers of BT_coh to all orders in the times) every n^{−k} coefficient of 𝔅_n^{rec}[BT_coh] is an entire function of the times (μ_j, μ_ρ) whose Taylor coefficients are the exact outputs of the multi-parameter engine at the symbolic exponents continued to j = ρ; in particular the second-order (pole², pole×Toda) part is the engine's bilinear layer, and **there is no second-order lip/companion term** | PROVED-mod-cite (K.12′(a)–(b) [REVIEWED], BT.5 [REVIEWED], WE.1 [REVIEWED]; exact algebra of the engine) |
| **Prop 2.2** | exact layer identities (formal model M(β, ν), symbolic p, ν, β, j, k unless stated): (i) bilinear e₁e₂ layer: natural N⁰ = N⁻¹ = 0, **N⁻² = jkp(pj + pk + p + 1)/4**, i.e. per natural leads ε_x = (px/2)e_x: **ε_jε_k(1 + p + pj + pk)/p**, diagonal half; (ii) third order: e₁³ and e₁²e₂ start at N⁻³ with closed forms; (iii) fourth order (p = 5/2): e₁⁴ starts at N⁻⁴; (iv) the bilinear N⁻³ term is 0 and the N⁻⁴ dressing h(j, k) (p = 3/2) is β-free, symmetric, has simple poles at j = ½ and k = ½ only, and reduces to JZC_M4_proof's h₂ at j = k = 1 | PROVED (exact computer algebra, `w2_exact_{B,T,M,Q,H}.out`, 27 identities incl. 3 controls) |
| Obs 2.3 | the leading terms of all computed orders are the Lagrange–Bürmann coefficients of (n/x)^p, **x = N − (1/p)Σ_a ε_a x^{−p j_a}** (the times act as a shift of the natural index) | exact at orders 2 (all j, k, p), 3 (e³, e²e′; all p), 4 (e⁴, p = 5/2); CONJECTURE beyond |
| **Cor 2.4** | κ-family, leading second-order pole terms: pole q_m × pole q_m′: L_mL_{m′}(p(m + m′ + 1) − 1)/p (½ if m = m′) at (n/N)^pN^{−p(m+m′)}; pole q_m × Toda t_j: **(1 + m + j)L_mε_j** at (n/N)^pN^{−1−p(m+j)}; L_m := pR_{q_m}W(q_m)π cot(πq_m) (W's first-order pole coefficient), ε_j the first-order Toda lead. In particular **q₁²: L₁²(3p − 1)/(2p)·n^{−2p}** and **q₁×t₁: 3L₁ε₁·n^{−1−2p}** | PROVED (Prop 2.2(i) + the times of K.12) |
| **Thm 2.5** | (S), p > 1, p ≠ 2: n^pb_n/c = 𝔅_n[M(α+2δ, α); t] + Σ_m Λ¹_m + Σ_{m≤m′} Λ²_{q_mq_m′} + Σ_{m,j} Λ²_{q_m t_j} + **O(n^{1−3p})** (+ the truncation errors O(n^{−K−1} + n^{−1−(J+1)p}) of P K.12); with Prop 2.2(ii)–(iii) the remainder improves to O(n^{−3p} + n^{2−4p}) | PROVED-mod-cite (P K.12, Prop K.12′, BT.5, WE.1, route 1, N.6b–c, all REVIEWED; Prop 2.1–2.2); NOT REVIEWED |
| §4 | registered predictions (16:56:01) for p = 3/2, 5/2, κ = ±k, k/2: fits of the n^{−2p}, n^{−1−2p} coefficients | NUMERICAL (§4.2) |

**Main outcome.** For the κ-family, W at first order in the poles (JZC_W_kappa P K.12 + K.12′) extends to second order: the
products of pole terms and the pole×Toda cross terms are exactly the formal model's bilinear response to two band-factor times with
symbolic exponents, continued to the pole exponents q_m = m − 1/p, with **no second-order companion or lip term** (coherence makes the
gauge form exact to all orders). The leading coefficients are elementary: q₁² enters at n^{−2p} with L₁²(3p − 1)/(2p), q₁×t₁ at
n^{−1−2p} with 3L₁ε₁, and in general the second-order bracket is (1 + p + pj + pk)/p — the analogue of JZC_M4_proof's (3p + 1)/(2p)
(j = k = 1), and all computed orders are the Lagrange–Bürmann coefficients of a single index shift (Obs 2.3). Analytically:
proved with remainder O(n^{1−3p}) (O(n^{−3p} + n^{2−4p}) with the exact cubic identities). Numerically, the registered
predictions hold at p = 3/2 to 10⁻¹³ (n⁻³) and 10⁻¹⁰ (n⁻⁴), and at p = 5/2 to 4·10⁻¹³ (n⁻⁵) and 4·10⁻¹⁰ (n⁻⁶), while "no second order", "Toda-only bracket",
"naive exponentiation" and "naive square" miss by 10⁶–10⁸ fit half-ranges.

## 0. Setting and notation

As JZC_W_kappa §0 (setting (S)): p > 1, −1 < δ ≤ 0, a := 1 + δ, κ ≠ 0, κ > −a^p, 1 < s < 1 + 2p, α = (s − 1 − p)/p ∈ (−1, 1),
β′ = α + 2δ, N = n + (β′ + 1)/2, q_m = m − 1/p, a_m = −binom(1/p, m)(−κ)^m, τ_m = 2π cot(πq_m)a_m, R_{q_m} = −q_ma_m, c = c(p),
W(q) = (4c)^qΓ(q + ½)/(√πΓ(q + 1)). BT_coh := BT_coh(β′, α; μ^κ_n, (2a_m)_{m≤M}) (JZC_W_kappa §4.1, L K.10).
**Times.** In the n^p frame the band factor of BT_coh is exp(−Σ_aμ_az^{j_a}) with Toda times μ_j = X_jn^{−jp} (X_j = −t_j = 2Z_κ(−j)/j − B_j,
P W-out.5(i), j ∈ ℕ) and pole times μ_{q_m} = −τ_mn^{−pq_m}. The engine works at c = 1 with the normalised tilt e·z′^j/C(2j, j), z′ = z/c:
**e_a = μ_a c^{j_a}C(2j_a, j_a)** (the c-scaling M_ρ^{(c)}(z) = c^{ρ−1}M_ρ^{(1)}(z/c) of z^ρ/R; for integer j this is JZC_M4_proof's
"ε_j carries c^j"). The natural first-order lead of time a is **ε_a := (pj_a/2)e_a** (Prop 2.2(i), first-order part = m3a_e37_decoupled
route 1 with WE.1(i)); for a pole, ε_{q_m} = −(pq_mW(q_m)/2)τ_mn^{−pq_m} = L_mn^{−pq_m}, L_m = pR_{q_m}W(q_m)π cot(πq_m) (P K.12).
**Natural form** of a layer with exponent sum S = p Σ j_a: (N/n)^{(S/p + 1)p}Σ_k e_kn^{−k} re-expanded in 1/N (m4_rh_exact2's gz
convention); for products this is (n/N)^p ε_aε_b… N^{−S}[bracket in 1/N].

## 1. The formal layers of BT_coh to all orders in the times (Prop 2.1)

**Proposition 2.1.** Assume (S) with p ≠ 2 (so no q_m is a half-integer). Fix K. Then 𝔅_n^{rec}[BT_coh] = Σ_{k≤K}n^{−k}b_k(μ_n), where
(i) each b_k is an entire function of the times (μ_j)_{j≤J}, (μ_{q_m})_{m≤M} with n-free Taylor coefficients;
(ii) b_0 ≡ 1, and b_1 is affine in the times (b_1 = d₁ + Σ_a(pj_a/2)e_a);
(iii) the Taylor coefficient of b_k at a monomial Π_ae_a^{β_a} equals the coefficient of the same monomial computed by `w2_engine.py`
  (E3 gauge of M = Σ_ae_aQ_{j_a}/C(2j_a, j_a), Taylor data at 0 and 4 rational in j_a) with the symbolic exponents set to j_a ∈ {j, q_m};
(iv) no other term exists: the second (and every higher) order in the pole data has no lip-mismatch/companion contribution.
*Proof.* (i): JZC_W_kappa Prop K.12′(b) (as re-derived by review B, item (b): "G = cosh h·I + (sinh h/R)·RN, h linear in the times, and
the hard-edge and soft-edge functions A_ρ and M_ρ are analytic on the respective discs. So the Laurent coefficients of Δ_k^{BT} are
entire in the times with n-free coefficients. The residue recursion and the extraction … are polynomial in these, so each b_k(times) is
entire"). This statement is not restricted to first order. (iv) and the gauge form: by coherence, JZC_W_BT Prop BT.5: "the κ-problem's
hard-edge parametrix built with ρ_a is **exact** (no lip mismatch, to all orders in the a_m)" — the mismatch exponent μ tan πq + πσ of
Lemma BT.1(iv) vanishes identically, so Δ_k^{BT_coh} = G_aΔ_k^{mod}G_a^{−1} (K.12′(a)) as an identity of functions, not of first-order
layers; the only jumps are the circle jumps (BT.1(ii)–(iv)), so the residue recursion of N.6c is the whole formal model. (iii): G_a is
E3's gauge of M = Σ_jμ_jQ_j + Σ_mμ_{q_m}(A_{q_m} at 0, M_{q_m} at 4c) (K.12′(a)); by WE.1(i)–(ii) [REVIEWED] the Taylor data of A_ρ at 0 and
M_ρ at 4 are the symbolic-j data at j = ρ (rational in j, with poles only at half-integers). The engine performs the same recursion over
the ring K[i][e₁, e₂]/(e₁^{E1+1}, e₂^{E2+1}); reduction modulo that ideal is a ring homomorphism from power series in the times, it
commutes with products, inverses, principal parts and residues (linear) and with the square root of the extraction (computed by the
binomial series of a unit), so the engine's monomial coefficients are the Taylor coefficients of the b_k. (The Laurent truncations
SHI, NT are guarded by the engine's assertion "principal part not determined" and were varied: NT = 12 → 20 → 28 and SHI = 20 → 24
give identical outputs.) (ii): b_0: Q₁ = P₁ + O(n⁻¹) is time-free at n⁰. b_1: m3a_e37_decoupled route 1 [REVIEWED] ("e(M) − e(0) =
cp·M(4c) identically in M(0), M(4c), M′(4c)"), with M linear in the times. ∎ (PROVED-mod-cite.)

*Consequently* (as review B noted for the mixed first-order terms): every term of order ≥ 2 in the times starts at n⁻² in the
n-expansion, so a monomial Π_a μ_a^{β_a} with |β| ≥ 2 contributes O(n^{−2−pΣβ_aj_a}).

## 2. Exact layer identities (Prop 2.2, Obs 2.3, Cor 2.4)

**Proposition 2.2** (formal model M(β, ν) with ν = α the Bessel order, β the Szegő exponent (decoupled, JZC_M4 §7); exact identities of
rational functions; `w2_exact.py`).
(i) [B; symbolic p, α, β, j, k; KORD 2] the e₁e₂ layer has natural coefficients N⁰ = N⁻¹ = 0 and
  **N⁻²: jkp(pj + pk + p + 1)/4**, identically in (p, α, β, j, k);
  the first-order layers are pj/2 (and pk/2) at N⁻¹. In ε-form: ε_jε_k(1 + p + pj + pk)/p·(n/N)^pN^{−2−pj−pk}; at j = k = 1 the diagonal
  (half) value is JZC_M4_proof N.6(ii)'s (3p + 1)/(2p) ε₁² (asserted).
(ii) [T, M; symbolic p, α, β, j, k; KORD 3] e₁² has N⁻² = j²p(2jp + p + 1)/8 (= (i)/2 on the diagonal) and N⁻³ = 0;
  e₁³: N⁰…N⁻² = 0, **N⁻³ = j³p(3jp + p + 1)(3jp + p + 2)/48**; e₁²e₂: N⁰…N⁻² = 0, **N⁻³ = j²kp(2jp + kp + p + 1)(2jp + kp + p + 2)/16**.
(iii) [Q; p = 5/2, symbolic α, β, j; KORD 4] e₁⁴: N⁰…N⁻³ = 0, N⁻⁴ = 5j⁴(20j + 7)(20j + 9)(20j + 11)/6144.
(iv) [H; p = 3/2, symbolic α, β, j, k; KORD 4] the e₁e₂ layer has N⁻³ = 0 and an N⁻⁴ term h(j, k) (printed in `w2_exact_H.out`) which is
  β-free, symmetric in (j, k), has denominator 512(2j − 1)(2k − 1), and at j = k = 1, β = α equals p²h₂/2 with JZC_M4_proof's
  h₂ = (p+1)(p+2)(3p²+2p+1)/(8p²) + (p+2)(2p³−p²−7p−6)α²/(16p²) (asserted at p = 3/2). In the rational-data runs of §3 the e₁e₂ and e₁²
  layers have zero N⁻³ and N⁻⁵ coefficients at p = 3/2 and 5/2 (KORD 6, 8), i.e. the second-order bracket is even in 1/N there.
*Controls (must fail, fail):* (p j + p k + 1) in (i); (3jp + p + 1)² in (ii); S = p(j + 2k) in the e₁²e₂ formula.
Run times: 22 s, 158 s, 1833 s, 249 s, 1414 s. (PROVED: exact computer algebra; the engine is the REVIEWED m4_rh_exact2 algebra over a
larger nilpotent ring, §1(iii).) A fully symbolic (p, α, β, j, k) KORD-4 run of (iv) did not finish its first order in 30 min and was
stopped; h(j, k) is therefore known at p = 3/2 only (and numerically at the rational data of §3).

**Observation 2.3 (index-shift structure).** Let x solve x = N − (1/p)Σ_aε_ax^{−pj_a} (formal series in the ε's). By Lagrange–Bürmann,
x^{−p} = Σ_m ((−1)^m/m!)∂_N^{m−1}[(−pN^{−p−1})φ(N)^m], φ = (1/p)Σ_aε_aN^{−pj_a}, whose order-m coefficient for a single time is
ε^m(p + 1 + mpj)_{m−1}/(m!p^{m−1})N^{−p−m−mpj}. The leading natural coefficients of Prop 2.2 (i) (all j, k), (ii) (e³, e²e′), (iii) (e⁴,
p = 5/2) are exactly the corresponding coefficients of (n/x)^p (asserted in w2_exact as "Lagrange(m)"). So, to leading order in 1/N at
each order in the times, **n^pb_n/c ≈ (n/x)^p: the band-factor times act as a shift of the natural index** — the first-order layer is
the first-order shift x ≈ N − (1/p)Σε_aN^{−pj_a}, and the products are its iterates. (Exact at the listed orders; CONJECTURE in general;
HEURISTIC as an explanation. It is consistent with N.6(ii)'s "(n/N)^p" normalisation and with E3.7 (no N⁻¹ term beyond first order).)

**Corollary 2.4 (κ-family closed forms).** With pq_m = pm − 1 and ε_{q_m} = L_mn^{−pq_m}, Prop 2.2(i) gives the leading second-order
pole terms of n^pb_n/c:
- pole × pole: L_mL_{m′}·(p(1 + m + m′) − 1)/p·(n/N)^pN^{−p(m+m′)} (factor ½ if m = m′); e.g. **q₁²: L₁²(3p − 1)/(2p)·n^{−2p}(1 + O(n⁻¹))**;
- pole × Toda: (1 + m + j)·L_mε_j·(n/N)^pN^{−1−p(m+j)}, ε_j := (pj/2)X_jc^jC(2j, j) the first-order Toda lead (for the lattice
  ε_j = C(2j, j)pc^jζ(−jp), JZC_M4_proof); e.g. **q₁×t₁: 3L₁ε₁·n^{−1−2p}(1 + O(n⁻¹))**.
Integer coefficients for pole×Toda; for comparison the Toda×Toda bracket is (1 + p + pj + pj′)/p, (3p + 1)/(2p) for t₁².
*Proof.* Insert j_a ∈ {q_m, j} in (i). ∎ (PROVED; `w2_cross.out` (4) asserts both at P15a, P25a against the registered layers.)

*p = 2.* Then q_m = m − ½, τ_m = 0, and the A-data have poles at half-integers: the first-order layers carry the W′ limit (JZC_W_exact §4).
At second order the leading bracket (i) is pole-free, so the leading pole² term vanishes (τ² × finite); but h(j, k) has simple poles at
j = ½ and at k = ½ (iv, p = 3/2), so τ_aτ_bh can have a finite W′-type limit at relative N⁻², i.e. at n^{−2p−2} = n⁻⁶ for p = 2. Not
computed (needs h at p = 2); p = 2 is excluded from Thm 2.5.

## 3. Conjecture W at second order in the poles for σ^{δ,κ} (Theorem 2.5)

**Theorem 2.5.** Assume (S), p > 1, p ≠ 2, and let K, J, M = J + 1 be as in JZC_W_kappa P K.12 (K ≥ 3p). Write
Λ¹_m(n) := Σ_{k≤K}e_{q_m}(n)E^{(1)}_k(q_m)n^{−k} (the continued symbolic-j layer of K.12′'s refined form, e_{q_m} = −τ_mc^{q_m}C(2q_m, q_m)n^{−pq_m}),
Λ²_{ab}(n) := e_a(n)e_b(n)Σ_{k≤K}E^{(2)}_k(j_a, j_b)n^{−k} (a ≠ b; E^{(2)} = the engine's e₁e₂ coefficients) and Λ²_{aa} := e_a²Σ_kE^{(2,0)}_k(j_a)n^{−k}.
Then
  n^pb_n(σ^{δ,κ})/c = 𝔅_n[M(α + 2δ, α); t] + Σ_{m≤M}Λ¹_m + Σ_{m≤m′≤M}Λ²_{q_mq_m′} + Σ_{m≤M, j≤J}Λ²_{q_mt_j}
                        + O(n^{−K−1} + n^{−1−(J+1)p} + n^{1−3p}).
With Prop 2.2(ii) (cubic layers with at most two distinct exponents start at n⁻³) the last remainder improves to O(n^{−3p} + n^{2−4p}).
**Displayed form.** The only second-order terms above O(n^{1−3p}) are the q₁² layer, leading term **L₁²(3p − 1)/(2p)n^{−2p}**, and, for
p > 2, the q₁×t₁ layer, leading term **3L₁ε₁n^{−1−2p}**. With the improved remainder, q₁×t₁ is captured for every p > 3/2 (the q₁q₂ layer
starts at n^{−3p}).
*Proof.* (1) JZC_W_kappa P K.12 [REVIEWED]: n^pb_n/c = 𝔅_n^{rec}[BT_coh] + O(n^{−K−1} + n^{−1−(J+1)p}); its proof (L K.10(b) + N.6c with
the meromorphic BT_coh data, L K.9) does not expand in the times. (2) Prop 2.1: 𝔅^{rec} = Σ_kn^{−k}b_k(μ_n), b_k entire with n-free
coefficients, b_0 ≡ 1, b_1 affine. (3) The times are bounded: |μ_{q_m}| ≤ C|κ|^mn^{−pq_m} ≤ Cn^{1−p}, |μ_j| ≤ Cn^{−jp} (P W-out.5,
L K.10), so by Cauchy's estimate on a fixed polydisc, uniformly in n,
  b_k(μ) = b_k(μ_T, 0) + Σ_a∂_{q_a}b_k(μ_T, 0)μ_{q_a} + ½Σ_{a,b}∂²_{q_aq_b}b_k(0, 0)μ_{q_a}μ_{q_b} + O(|μ_br|²|μ_T| + |μ_br|³),
  ∂_{q_a}b_k(μ_T, 0) = ∂_{q_a}b_k(0, 0) + Σ_j∂_{q_a}∂_{t_j}b_k(0, 0)μ_j + O(|μ_br||μ_T|²),
with μ_br the pole times, μ_T the Toda times. (4) By Prop 2.1(ii) the O-terms (all of order ≥ 3 in the times) vanish for k ≤ 1, so they
contribute Σ_{k≥2}n^{−k}·O(n^{−2(p−1)−p} + n^{−3(p−1)} + n^{−(p−1)−2p}) = O(n^{1−3p}) (the largest is |μ_br|³n⁻² = n^{−2−3(p−1)}). (5) The
terms kept are: b_k(μ_T, 0) = 𝔅_n[M; t] (Theorem N.6 / K.12′(b) at μ_br = 0); ∂_{q_a}b_k(0, 0)μ_{q_a} = Λ¹_a (K.12′ refined); the second
derivatives = Λ² by Prop 2.1(iii). (6) Improvement: by Prop 2.2(ii) the cubic Taylor coefficients of the monomials μ_{q_1}³, μ_{q_1}²μ_x
vanish for k ≤ 2, so they are O(n^{−3−3(p−1)}) = O(n^{−3p}) and O(n^{−1−3p}); cubic monomials with three distinct times are
O(n^{−2−(p−1)−p−(2p−1)}) = O(n^{−4p}) by (4); quartic ones are O(n^{−2−4(p−1)}) = O(n^{2−4p}). ∎
(PROVED-mod-cite: P K.12, K.12′, BT.5, WE.1, route 1, N.6b–c, Theorem N.6, all REVIEWED; Prop 2.1, 2.2 (this note, NOT REVIEWED).)

*What is and is not proved.* Proved: the second-order layer is the engine's bilinear layer (Prop 2.1) and its closed form at leading
order (Cor 2.4); the asymptotic statement with remainder O(n^{1−3p}) (or O(n^{−3p} + n^{2−4p})). Not proved: closed forms in p of the
second-order dressing (only p = 3/2 symbolic in (α, β, j, k), and exact rational values at the registered data); Obs 2.3 beyond the
listed orders; p = 2; the quartic start at N⁻⁴ for general p (exact at p = 5/2 symbolically and at q₁ for the registered data, asserted
in `w2_predict.py`), which would give O(n^{−3p}) for all p > 1.

## 4. Numerical test (pre-registered; NUMERICAL)

### 4.1 Registration (Rule X)

`w2_predict.py` wrote `w2_predictions.json` at **2026-10-22 16:56:01 MDT**, before any Jacobi coefficient of these measures existed
(Rule A item 1: a timing test had generated one data file before registration; it was deleted unread). Cases:
P15{a,b,c}: p = 3/2, δ = −¼, s = 11/5 (α = −⅕, β′ = −7/10), κ = ½, −½, ¼; P25{a,b,c}: p = 5/2, δ = −¼, s = 2 (α = −3/5, β′ = −11/10),
κ = ⅖, −⅖, ⅕. Registered: the predicted coefficient of every n^{−e}, e ≤ 5.5 (p = 3/2) resp. 7.5 (p = 5/2), split by order and monomial,
from exact engine runs at the rational data (KORD 6 resp. 8; all orders in the times up to cubic, quartic asserted out of range); the
targets T₁ = 2p (q₁² leading, κ²) and T₂ = 1 + 2p (q₁×t₁ leading + q₁² dressing); alternatives with the same model, Toda and first-order
layers but the pole monomials of order ≥ 2 replaced by: **A0** nothing (first order in the poles only); **A1** the Toda (μ₁²) bracket
(1 + 3p)/p per ε_aε_b; **A2** naive exponentiation ½(Σε_aN^{−1−pj_a})²(n/N)^p; **A3** naive square (Σε_aN^{−1−pj_a})²(n/N)^p; and the
κ-structure at T₁: coefficient = d_{2p} + κ²C. The fit method and the pass/fail thresholds are fixed in `w2_fit.py`'s docstring (A0–A2
must miss by > 10 tol and A3 by > 3 tol at T₁; tol = max(3 half-ranges, 10⁻⁹(1 + |P|))).

Registered values (coefficient of n^{−e}; "2nd" = the order ≥ 2 pole part):

| case | n^{−2p}: total | 2nd (q₁²) | A0 | A1 | A2 | A3 | n^{−1−2p}: total | 2nd |
|---|---|---|---|---|---|---|---|---|
| P15a | −0.14765335832 | +0.09352711 | −0.24118047 | −0.09420930 | −0.20109742 | −0.16101437 | +0.12542733481 | +0.20728447 |
| P15b | −0.14765335832 | +0.09352711 | −0.24118047 | −0.09420930 | −0.20109742 | −0.16101437 | +0.06501217221 | +0.26769963 |
| P15c | −0.11759107396 | +0.02338178 | −0.14097285 | −0.10423006 | −0.13095209 | −0.12093133 | +0.09003150222 | +0.04426922 |
| P25a | +0.24738604745 | +0.08973208 | +0.15765397 | +0.27499592 | +0.19216631 | +0.22667865 | −0.99120569850 | −0.51820622 |
| P25b | +0.24738604745 | +0.08973208 | +0.15765397 | +0.27499592 | +0.19216631 | +0.22667865 | −1.09679257051 | −0.55340185 |
| P25c | +0.06619627762 | +0.02243302 | +0.04376326 | +0.07309875 | +0.05239134 | +0.06101943 | −0.23136823670 | −0.12515210 |

(n^{−2p} is even in κ: the q₁² layer and the first-order q₂ layer are both ∝ κ²; at n^{−1−2p} the q₁×t₁ layer, 3L₁ε₁, is
−0.552 (P25a) and +0.270 (P15a).)

### 4.2 Data and fits

`w2_data.py`: atoms 1/λ_k, masses λ_k^{−s/p}, k ≤ 2K (K = 100·1200), λ_k = (k + δ)^p + κ, at mpmath dps 40, passed to a binary128 RKPW
kernel (copy of csrc/rkpw.c with double-double input); tail: a C^∞ partition of unity in k on [K, 2K] (atoms weighted by χ, the
complement integrated by Gauss–Legendre on [K, 2K] and by Gauss–Jacobi in x beyond 2K with the exact factor (1 − κx)^{1/p−1}), both
Gauss rules Newton-refined at dps 40; y_n = n^pb_n/c − 1 kept in mpmath. Fit of the coefficient of n^{−T}: residual after subtracting
every other registered coefficient (e ≤ emax), least squares on [lo, 1200] with n^{−T} and the next J − 1 half-integer exponents above
emax, J ∈ {2, …, 5}, lo ∈ {150, 300, 600}; median and half-range (half-ranges are spreads, not error bounds; Rule N).

**Results, p = 3/2 (`w2_fit_P15.out`, ALL 27 CHECKS PASSED, run 3 — see Rule A items 5–7):**

| case | y − P at n = 150 / 1200 (× n⁶) | n⁻³ fit (half-range) | − registered | n⁻⁴ fit (half-range) | − registered |
|---|---|---|---|---|---|
| P15a | −0.905 / −0.890 | −0.1476533583 (1.7·10⁻¹⁰) | +1.2·10⁻¹³ | +0.1254273350 (5.2·10⁻⁸) | +2.1·10⁻¹⁰ |
| P15b | −1.175 / −1.206 | −0.1476533583 (5.7·10⁻¹⁰) | +8·10⁻¹⁶ | +0.0650121722 (1.9·10⁻⁷) | +2.3·10⁻¹² |
| P15c | −0.163 / −0.166 | −0.1175910740 (5.1·10⁻¹¹) | −2·10⁻¹⁶ | +0.0900315022 (1.7·10⁻⁸) | +8·10⁻¹⁴ |

- The second-order part at n⁻³ is +0.0935 (P15a/b) and +0.0234 (P15c), i.e. 8·10⁷, 5·10⁷, 2·10⁷ tol; A0, A1, A2, A3 miss by
  ≥ 8·10⁶, 3·10⁷, 3·10⁷, 3·10⁶ tol at n⁻³ and by ≥ 4·10⁵, 7·10⁴, 3·10⁵, 2·10⁵ tol at n⁻⁴ (all four cases of each).
- After subtracting the full registered prediction the residual is a clean c₆n⁻⁶ (c₆ ≈ −0.90, −1.19, −0.165, flat to 2% from n = 150
  to 1200): nothing unpredicted is left through n^{−5.5}, including the q₁³ layer at n^{−4.5} and the q₁×q₂, q₁²×t₁ layers.
- κ-structure: fit(½) − fit(−½) = 1·10⁻¹³ at n⁻³; κ² coefficient fitted −0.16033218 = registered −0.16033218 (first order (q₂)
  −0.53444061 + second order (q₁²) +0.37410843); the first-order-only value misses by > 10⁷ of the (floor-dominated) tolerance.
- Tail control (K = 100·nmax vs 200·nmax): identical fits at both targets.

**Results, p = 5/2 (`w2_fit_P25.out`, ALL 27 CHECKS PASSED):**

| case | y − P at n = 150 / 1200 (× n⁸) | n⁻⁵ fit (half-range) | − registered | n⁻⁶ fit (half-range) | − registered |
|---|---|---|---|---|---|
| P25a | −3.568 / −3.463 | +0.2473860475 (2.2·10⁻⁹) | +3.9·10⁻¹³ | −0.9912056981 (5.9·10⁻⁷) | +3.9·10⁻¹⁰ |
| P25b | −3.568 / −3.703 | +0.2473860475 (3.0·10⁻⁹) | +7·10⁻¹⁴ | −1.0967925704 (8.3·10⁻⁷) | +1.0·10⁻¹⁰ |
| P25c | −0.838 / −0.815 | +0.0661962776 (4.8·10⁻¹⁰) | +3.6·10⁻¹³ | −0.2313682364 (1.3·10⁻⁷) | +3.1·10⁻¹⁰ |

- The second-order part at n⁻⁵ (+0.0897, +0.0897, +0.0224) is 10⁷ tol; at n⁻⁶ (−0.518, −0.553, −0.125; dominated by q₁×t₁ =
  3L₁ε₁ = −0.552, −0.587, −0.134) it is 2–3·10⁵ tol. A0, A1, A2, A3 miss by ≥ 10⁷, 3·10⁶, 6·10⁶, 2·10⁶ tol at n⁻⁵ and by
  ≥ 2·10⁵, 3·10⁴, 1.5·10⁵, 7·10⁴ tol at n⁻⁶.
- Residual after the full prediction: a clean c₈n⁻⁸ (c₈ ≈ −3.5, −3.6, −0.82), i.e. nothing unpredicted through n^{−7.5} (this includes
  the first-order q₃ layer and the q₁×q₂ and q₁³ layers at n^{−7.5}).
- κ-structure: n⁻⁵ coefficient even in κ to 3·10⁻¹³; κ² coefficient fitted +1.50991475 = registered +1.50991475 (first order (q₂)
  +0.94908927 + second order (q₁²) +0.56082548).
- Tail control: K = 100·nmax and 200·nmax agree to 10⁻¹⁵ (n⁻⁵) and 10⁻¹² (n⁻⁶).

## 5. Rule A (adversarial pass) — log

1. *Rule X.* A timing test of `w2_data.py` (before registration) generated the P15a data file and printed four y_n values (no fit, no
   comparison with any prediction); the file was deleted and regenerated after registration (`w2_fit.py`'s docstring says "deleted unread": no fit or comparison was
   made). `w2_fit.py` asserts that the predictions
   predate the run and that every data file used postdates them.
2. *Is the second-order layer just the first-order formula squared?* No: the bracket (1 + p + pj + pk)/p is not 1 (A3) or ½ (A2), and
   for poles it is not the integer-time (3p + 1)/(2p) (A1); all four are excluded by ≥ 10⁶ half-ranges.
3. *Companion at second order.* For coherent pole data BT.5 makes the gauge form exact (no lip term at any order), so none is
   predicted. Test: after subtracting the registered prediction the residual is c₆n⁻⁶ (p = 3/2) resp. c₈n⁻⁸ (p = 5/2) with ×n^{6,8}
   flat to 2–7% from n = 150 to 1200; a q₁ companion at relative N^{−2q₁−1} (Thm BT's scale for a genuine fractional tilt) would sit at
   non-half-integer exponents (n^{−1.5−5/3} at p = 3/2, n^{−2.5−11/5} at p = 5/2), below emax, and is not seen.
4. *Normalisations (Rule N 5).* The c-scaling and the C(2j, j) normalisation of the times are tested independently in `w2_cross.py`:
   exact d_k vs the numeric engine m4_rh4 at the true c (10⁻²⁰); Toda first and second order vs w_common.model's finite differences
   (10⁻¹²); the first-order q₁ lead vs W's pRWπcot (10⁻²⁵); Cor 2.4's two closed forms vs the registered layers. An error in the scratch
   version of this comparison (α = −2/15 instead of −⅕ typed by hand) produced a spurious mismatch, found and fixed before registration.
5. *Run 1 data defect (tail without κ).* The first data generator copied famK's tail (pure power t^p beyond K, i.e. κ dropped there).
   Its first fit run stopped at an informational print (np.int64 → mpf; fixed: `mpf(int(k))`, no fit rule touched;
   `tmp/w2/w2_fit_P15_run1_partial.out`); the rerun (`tmp/w2/w2_fit_P15_run1_partial2.out`, stopped after P15b) showed a flat ±10⁻¹³
   residual y − P (not ∝ n⁻⁶), n⁻³ half-ranges 7·10⁻³, and A0–A3 missing by only 0.7–5 tol, while the registered prediction passed. No
   prediction or fit rule was changed after this; only the measure generator was corrected (items 6–7).
6. *Run 2 (exact-κ tail, midpoint rule).* y(K = 100·nmax) − y(200·nmax) = 5·10⁻¹⁴ at n = 1200, growing like n^{3.3}: the continuum tail
   still mattered at large n. Diagnosed below; no fit run.
7. *Float64 Gauss rules.* The remaining error was the quadrature: with scipy's float64 Gauss rules (Gauss–Jacobi, n = 1208, β = −0.2,
   and Gauss–Legendre) the smooth-cut tail reproduces the tail moments Σ_{k>K}λ_k^{−s/p−m} (m = 0, 1; reference: mpmath Euler–Maclaurin)
   only to 7·10⁻¹⁵ and 2·10⁻¹³ relative, independently of K (so: rule error, not tail-model error); y(K = 25·nmax) − y(50·nmax) was then
   still 6·10⁻¹⁶ relative at n = 1200. With both rules Newton-refined at dps 40 (`gauss_jacobi_mp`) the same moments agree to 10⁻⁴⁰, and in
   the final runs K = 100·nmax and 200·nmax give the same fits to 10⁻¹⁵ (n^{−2p}) and 10⁻¹² (n^{−1−2p}). **Note for other notes:**
   `w_common.run_measure` (famK and the other families) uses float64 atoms, float64 roots_jacobi tails and float64 y; data built that way
   carry a measure error of this size, which may limit fits at deep orders there (not re-examined here; those files were not modified).
8. *Engine truncation.* m4_rh_exact2's fixed re-expansion depth NT = 12 is too shallow at KORD 8 (assertion fired); NT is now an env
   variable (default 12, unchanged behaviour). P15 predictions were recomputed after the change and agree with the earlier run to all
   printed digits; NT = 20 vs 28 give identical KORD-8 output. `w2_exact_{B,T,M}.out` ran on the engine before this change (sha256
   b5d60698…, printed there); with NT unset the two versions execute the same algebra.
9. *Third and fourth order.* Not assumed: the order-3 layers that reach emax were computed (q₁³ at n^{−4.5} for p = 3/2; q₁²×t₁) and
   their start at n⁻³ asserted; the quartic q₁⁴ layer's start at n⁻⁴ is asserted on the engine at each registered case, so it cannot
   reach emax.
10. *Degenerate parameters.* p = 2 excluded (half-integer q_m, h has poles at ½); integer j ∈ {q_m} impossible for p > 1 (1/p ∉ ℤ);
    κ < 0 tested (P15b, P25b): even-in-κ structure at n^{−2p} confirmed.
11. *pkill.* A `pkill -f` pattern matched its own shell during the session (no data affected); later processes were killed by pid.

## 6. What remains

1. **Rule R** for this note (Prop 2.1's ring-homomorphism argument, Prop 2.2's identities, Thm 2.5's remainder bookkeeping).
2. **Closed forms in p** of the second-order dressing h(j, k) (only p = 3/2 symbolic; the full symbolic run is too slow as written) and
   a proof of Obs 2.3 (the index-shift / Lagrange structure) to all orders — it would give the leading term of every order at once.
3. **p = 2**: the finite W′-type second-order term τ_aτ_bh at q = ½ (needs h at p = 2).
4. The quartic start at N⁻⁴ for general p (exact at p = 5/2 only), which would make the remainder O(n^{−3p}) for 1 < p ≤ 2.
5. Rule L before any novelty claim.
6. The float64 tail floor of `w_common.run_measure` (Rule A item 7) affects earlier numerical notes' precision, not their labels; a
   re-run with `w2_data`'s generator would sharpen JZC_W_outer §8 (not done; those files belong to other notes).
