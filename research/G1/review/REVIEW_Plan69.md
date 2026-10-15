# Rule R review: Plan 69 (hard-edge tail bound in Paper 2's frame; telescoping, TAIL.md)

Reviewer: independent second reader (Rule R). Branch `plan-69-tailbound`, HEAD f41114e.
Targets:
- research/G1/RH/second_order/TAIL.md (§§0–6);
- checks/check_tail.py and check_tail.out, and their two MANIFEST.sha256 lines.

Context I re-read against the write-up:
- UL.md (REVIEWED): every use of (QLP-c), in Thm UF, Lemma W, UF-lim, Prop UΛ-L¹ and Prop R;
- G1 PROOF.md: §3.4 Lemma TL (statement, the integer-T tail form, the μ_{n−1} remark); §3.16 Thm QLP with Lemmas ST,
  GS, BK, Z, A and the p ≠ 1 proof; §3.21 header (CT, CS);
- SECOND.md: Prop 3.1 and Thm 3.2 with its proof;
- papers/paper2: §3 (lem:transfer, lem:chain-limit); §5 (standing assumptions, eq:angles, lem:interp/eq:U, lem:lips,
  the contour and regions, eq:VM); §6 (eq:Pinf0, eq:Q, lem:normalisation, lem:szego (vi)); §7 in full (Bessel model,
  lem:bessel-local, eq:he-Phi-large/small, lem:comparison-parametrix, eq:he-Qtilde, lem:lip-mismatch,
  prop:UR-comparison, thm:UR-true, prop:moments **with its proof**, rem:alpha-ge-1); sec_2 T3 (Conway–Deift Thm 4.4 as
  quoted, (a)–(e)); sec_front thm:pure;
- E_pgt1.md §§0, 3, 6 (the Q-frame for p > 1 and Prop E.5′).

TAIL.md reads no new external source. Its external inputs reach it through Paper 2 (T3 = Conway–Deift Thm 4.4, quoted with
hypotheses in sec_2) and through G1 §3.16 (KMVV, DLMF). Lemma GS's Teschl attribution is an attribution only, and the
proof is self-contained. So there is no new Rule C item.

## Overall verdict: **ACCEPT WITH FIXES**

I found no mathematical error in any PROVED or PROVED-mod-cite statement. I re-derived every one independently. All
seven high-risk points hold:
1. The §1 audit is correct.
2. The telescoping (Lemma TS, Thm TS) is correct, with the uniformity scope as stated.
3. The lower Christoffel transfer identity is right, and so is the GAP at s = 1 + p.
4. Lemma GS and Lemma ST are correct.
5. The row-weighted Cauchy–Deift estimate of Prop TB-Q is correct. The L² input really is established in the proof of
   prop:moments under the same hypotheses.
6. The exponent bookkeeping of Cor TB-C is exact.
7. Prop TB-P adds no new mathematics: the statement is G1 §3.16 Thm QLP for p > 1, which is already proved and REVIEWED.

The findings are minor or INFO:
- one overstatement ("only boundedness of ε′_n is used");
- one understatement (Prop UΛ⁻ and uniform *boundedness* of the a-part survive at s = 1 + p);
- two points in TB-P's frame dictionary;
- unlabelled heuristic remarks;
- check hygiene.

The check reproduces byte-for-byte. My own scratch checks agree with Lemma CT's transfer identity, Lemma GS and Lemma ST.

| Statement | Verdict | Label after fixes |
|---|---|---|
| §1 (N) audit | ACCEPT WITH FIXES (F5 wording) | audit |
| Lemma TS (i)–(iii) | ACCEPT | PROVED (elementary) + PROVED-mod-cite (II Cor 1.3; SECOND Thm 3.2) |
| Thm TS (a), (b) | ACCEPT | PROVED-mod-cite |
| Prop UP-w (i), (ii) | ACCEPT | PROVED-mod-cite |
| GAP UP-1+p | ACCEPT WITH FIXES (F2: sharpen; consequences paragraph) | GAP (uniform convergence only; uniform boundedness PROVED-mod-cite, F2) |
| Lemma ST | ACCEPT | PROVED (elementary) |
| Lemma GS | ACCEPT | PROVED; KNOWN attribution not re-read |
| Prop TB-Q | ACCEPT | PROVED-mod-cite (Paper 2 rev. 3 §§5–7, App. A–D; T3(b)) |
| Prop TB-A | ACCEPT | PROVED-mod-cite |
| Cor TB-C | ACCEPT | PROVED-mod-cite (+ TL's D5 caveat, as stated) |
| Prop TB-P | ACCEPT WITH FIXES (F3) | PROVED-mod-cite (= G1 §3.16 Thm QLP, p > 1, REVIEWED); Q-frame dictionary = presentation note |
| GAP TB-opt | ACCEPT WITH FIXES (F6: mechanism sentence HEURISTIC) | GAP |
| §3.6 bullets / Verdicts | ACCEPT WITH FIXES (F1, F6) | — |
| §5 checks | ACCEPT WITH FIXES (F4) | NUMERICAL |
| §6 Integration | ACCEPT WITH FIXES (F2, F7) | — |
| Novelty | present (UNCHECKED) | UNCHECKED |

## 1. Checks performed

**Re-run.** `make -C csrc` had nothing to do. I ran
`PYTHONPATH=src …/jacobi-asymptotics/.venv/bin/python research/G1/RH/second_order/checks/check_tail.py`:
- exit 0, empty stderr, 18 s wall time (1 m 37 s CPU);
- the output is **byte-identical** to the committed check_tail.out;
- the MANIFEST.sha256 lines 194–195 match both files.

**Numbers quoted in TAIL §5 / §4 vs the .out.** All match:
- R_S ∈ [0.6968, 0.8298] ("0.70–0.83");
- R_A ∈ [0.4983, 0.6753] ("0.50–0.68");
- R_C ∈ [0.4833, 0.6211] ("0.48–0.62");
- lumped mass ≤ 6.2·10⁻²;
- (1.25, 3.0) row: 4.361·10⁻², 2.377·10⁻², 1.244·10⁻², 6.374·10⁻³;
- K → 2K change ≤ 1.5·10⁻¹⁰;
- additivity defect 2.4·10⁻⁴⁰ (≤ 3·10⁻⁴⁰ as stated).

Every Γ_n row roughly halves per doubling of n, including the pairs outside the window (p = ½: (2.25, 2.75), (2.5, 3.0)).
That is numerical support for Thm TS(b) away from the window. UL's check_ul [4] already covers p = 1 with
s ∈ [1.5, 4] ⊄ (1, 3), so it is a second, independent corroboration.

**Script logic.**
- [1] S_n is the Stieltjes transform in the X variable with μ_n from Lanczos, which is exactly Lemma GS's S_n.
- R_C is a supremum over M with Mn ≤ K only, as printed.
- The p = ½ runs use n ≤ 8, which TAIL states as a limit. The script is NUMERICAL, as Rule N requires.

**Independent scratch checks (not committed; mpmath, dps 50).**
- Lemma CT / lem:transfer(ii) for σ_s = x·σ_{s−p}, p = ½, s ∈ {1.7, 2.3}, 60 atoms, n ≤ 11: the relative error of
  α_n(s) = g_n(s−p) + b_{n+1}(s−p)²/g_n(s−p) is ≤ 9·10⁻⁵¹. The relative error of h_n(s)/h_n(s−p) = g_n(s−p) is
  ≤ 2·10⁻⁵⁰.
- Lemma GS core identity: |U₁₁U₁₂ + hS_n| = 10⁻⁵⁵ against |hS_n| = 5·10⁻⁹, at a complex z (n = 6, 40 atoms).
- Lemma ST on 2000 random discrete probability measures at θ = 5π/6: max of ν([0, τ])/((8/√3)τ|S|) = 0.41 ≤ 1.

## 2. Statement-by-statement re-derivation

**§1 audit (task 1).** I read UL.md line by line.
- **Thm UF.** It uses (QLP-c) only through B_t = sup_n E_t[(k/n)^{u₀}], via Tonelli. The step u₀ enters in two places:
  r = (s − t)/p ≤ ¼ in Jensen, which needs only u₀ ≤ p/4, and the (D) side, which needs u₀ < the tail exponent at
  every base point. Any exponent ϑ(t) with inf_K ϑ > 0 suffices.
- **Lemma W.** V₋ needs pa′ below the tail exponent. ν_arc integrability needs a′ < ½, which is automatic once the
  exponent is < p/2.
- **UF-lim.** It applies Lemma W with g = y^{±r_u} at the grid points t_i = a + iu. There are countably many base
  points in all, and u ≤ u₀. Any positive exponent bounded below on K suffices. The constant is identified through
  (CS) at a, which is Law P and needs no tail bound.
- **Prop UΛ-L¹ and Prop R.** They use (QLP-c) only through Lemma W (g = log, δ small) and QLP-Λ at a single point,
  where any positive exponent gives Λ_n(a) = O(1).
- **Thm UP, Thm UΛ, Prop UΛ⁻.** They inherit the dependence through UF-lim.
- No (RU) and no s-uniformity of the constants are used anywhere, and m = n − 1 is never used.

The audit is correct. The one wording point is F5.

**Lemma TS.**
- (i) Each of the three terms is additive (telescoping sum, a linear coefficient of log n, the constant), so
  antisymmetry follows.
- (ii) m(s) = ⌈(s − 1)/p⌉ − 1 is the largest m ≥ 0 with s − mp > 1, so r(s) ∈ (1, 1 + p]. This includes the boundary
  case s = 1 + jp, where r = 1 + p and m = j − 1. The displayed decomposition follows from (i).
- (iii) With s₁ − s₀ = p, Γ_n(s, s + p) → 0 is exactly SECOND Thm 3.2. I checked that the normalisations agree with
  Cor UL-3.8. Thm 3.2's proof uses only Prop 3.1 and n^pg_n(s) → c, and the latter follows from Law P at s (Paper 2
  thm:pure, every p > 0, s > 1) and lem:chain-limit (= G1 Lemma CS).

ACCEPT.

**Thm TS (a), the enlarged K″.** For K ⊂ [a, b] ⊂ (1, 1 + 2p), put a″ = min(a, 1 + p/2) and b″ = max(b, a″ + p).
Then b″ < 1 + 2p, because a″ + p ≤ 1 + 3p/2 and b < 1 + 2p, and b″ − a″ ≥ p. So UF-lim's "enlarge K so that b ≥ a + p" is
satisfied inside the window, and the identification φ′(0) = log c via (CS) at a″ uses only Law P.

All tail-bound uses are at grid points of K″ ⊂ window, where Cor TB-C gives exponent ϑ_*(p, t):
- ϑ_* is increasing (d/ds of (s − 1)/(Bs + 2), B = 1 + 2/p, has the sign of B + 2 > 0), so inf_{K″} ϑ_* = ϑ_*(a″).
- u₀ := ½ϑ_*(a″) < p/4 keeps Jensen's r ≤ ¼ and φ's C² range.
- In Lemma W, g = y^{−r_u} needs u < ϑ_*(t_i), which holds for every u ≤ u₀ and every grid point.
- Cor TB-C gives the tail bound *at* the exponent ϑ_*, not just below it, so ϑ₀ = ϑ_*(t) itself can be used in B_t.

The uniformity scope "sup over K × K, K compact in the window" is what UF-lim delivers on K″ ⊃ K. ACCEPT.

**Thm TS (b).** r₀ and r₁ lie in (1, 1 + p] ⊂ window, so (a) applies with K = {r₀, r₁}. There are finitely many chain
terms, each → 0 by Lemma TS(iii). ACCEPT. "What the telescoping does not give" is correct: uniformity of the chain
terms in r is a uniform chain-limit statement, which is not available.

**Prop UP-w.**
- (i) is UL Thm UP's b-part. It uses only UF-lim on K and Law P at s₀ ∈ K. ✓
- (ii), K₁ := K ∩ (1, 1 + p). When 1 + p ∉ K, K₁ = K ∩ (−∞, 1 + p] is compact. Its interval hull together with K₁ + p
  lies in the window, so n^pg_n = exp(F_n(s + p) − F_n(s)) → c uniformly (SECOND Prop 3.1). Then Lemma CT,
  α_n = g_n + b_n²/g_{n−1}, with (i) gives the claim. ✓
- (ii), K₂. I checked the transfer identity against lem:transfer(ii) (ã_n = u_n + l_{n+1}, l_{n+1} = b_{n+1}²/u_n,
  with indices as in Paper 2: a from n ≥ 0, b from n ≥ 1, matching UL's α_n and b_n), for σ = σ_{s−p} and xσ = σ_s.
  This is exact (x_k·k^{−(s−p)} = k^{−s}) and was confirmed numerically to 10⁻⁵⁰ above. Uniformity holds because K₂ − p
  and the interval hull of (K₂ − p) ∪ K₂ lie in the window. ✓

The claimed uniformity is exactly what is proved. ACCEPT.

**GAP UP-1+p.** The obstruction is correctly identified. Route 1 needs F_n near 1 + 2p (the window's edge). Route 2
needs σ_{s−p} with s − p ↓ 1, which is not a compact set of (1, ∞). For the *limit*, a refinement of UF-lim cannot cross
1 + 2p: the per-cell error A₀r_u·r → 0 needs base points dense up to the right end. Base points beyond the window would
need a tail bound there.

The consequences paragraph is too pessimistic, however (F2). The *bounded* form survives at s = 1 + p, and with it
Prop UΛ⁻.

**Lemma ST.** For X ≥ 0 and z = τe^{iθ} with cos θ < 0: Re 1/(X − z) = (X + τ|cos θ|)/|X − z|². For X ≤ τ,
|X − z|² ≤ τ²(2 + 2|cos θ|) ≤ 4τ², so Re 1/(X − z) ≥ |cos θ|/(4τ). At θ = 5π/6 the constant is 8/√3. ACCEPT.

**Lemma GS.** U₁₂(z) = Σ_kω_kπ(X_k)/(z − X_k) holds by the definition eq:Y-solution of Y₁₂ (a Cauchy sum), with
ω_k = n^pw_k (lem:interp residues). Since (π(z) − π(X))/(z − X) has degree n − 1 in X, U₁₁U₁₂ = −hS_n.

For Q = CUk^{σ₃}:
- Q₁₁Q₁₂ = C₁²U₁₁U₁₂.
- Q₁₁ → 1 forces C₁z^nk → 1, so (Q₁)₁₂ = C₁²h.

The hypothesis holds in Paper 2. In Ω_∞, Q = [D_∞^{−σ₃}C_∞e^{−nγ_pσ₃}]·U·(e^{nφ}FD_W)^{σ₃} (eq:VM, eq:Q). This is one
constant diagonal on all of Ω_∞, and Ω_∞ contains a neighbourhood of ∞ (consistent with eq:Q-at-infinity). The ray
arg z = 5π/6 lies in Ω_∞, since the lens lies in |arg z| < θ_w < π/2 (lem:lips(b)) and Ω^△ ⊂ {Re z ≥ 4c}. ACCEPT.

**Prop TB-Q (highest risk; scrutinised in full).**
- *Pointwise formula.* T3(b), as quoted in Paper 2, is the pointwise statement AB^{−1} = I + 𝒞(A₋(v_Av_B^{−1} − I)B₋^{−1}),
  not only the moments consequence. Its hypotheses are exactly those verified at the start of prop:moments' proof, for
  the same A = Q, B = Q̃, Σ̂ and r = r′ = 2. z = τe^{5πi/6} with τ ≤ δ/4 is off Σ̂: the circles have |s| ∈ {δ} or lie
  near 4c.
- *Geometry.* Near 0, Σ̂ consists of the band and the lips, with ¾θ_lip ≤ |arg s| ≤ 5/4·θ_lip < π/2. So the angle at 0
  between s and z is ≥ π/3, and |s − z|² ≥ r² + τ² − rτ ≥ ¼(r + τ)². Everything else is at distance ≥ 3δ/4.
- *Main lip term, |ζ_s| ≥ 2.*
  - I recomputed N = D_s^{−1}BD_z entry by entry, with a_w = (2π)^{−1/2}f(w)^{1/4} (n-free):
    - |N₁₁| ≲ (r/τ)^{1/4} and |N₂₂| ≲ (τ/r)^{1/4};
    - |N₁₂| ≲ (r + τ)(rτ)^{1/4} ≤ C;
    - |N₂₁| ≲ (r + τ)(rτ)^{−1/4} ≤ (τ/r)^{1/4} or (r/τ)^{1/4}, as r ≤ τ or r ≥ τ (using r, τ ≤ 1).
  - |B − I| ≤ C(r + τ) holds on U(0, δ): Lipschitz on U(0, δ/2), trivial for r ≥ δ/2.
  - The integrand is then Cτ^{−1/4}𝔪_ne^{−t/C}[1 + (τ/r)^{1/2}]/(r + τ).
  - Substituting r = t²/n² gives dr/(r + τ) = 2t dt/(t² + y) and (τ/r)^{1/2}dr/(r + τ) = 2√y dt/(t² + y). Both
    kernels are ≤ 1 and ≤ 1/t respectively (y ≥ 1, AM–GM), so the bound is Cε′_nτ^{−1/4}. ✓
- *Main lip term, |ζ_s| ≤ 2.* G = (2πn)^{−σ₃/2}B(2πn)^{σ₃/2}ζ_z^{−σ₃/4} has the four entries stated. The dangerous one is
  2πnB₂₁ζ_z^{−1/4}, which is ≲ nτ|ζ_z|^{−1/4} ≍ |ζ_z|^{1/4}τ^{1/2}. So |G| ≲ |ζ_z|^{1/4} ≍ n^{1/2}τ^{1/4}. With
  |Q̃(s)e₂| ≲ n^{1/2}|ζ_s|^{−|α|/2} (lem:bessel-local(iii), boundary values included), |s − z| ≥ τ/2 (r ≤ Cn^{−2} ≤ Cτ/y₀)
  and ∫_0^{Cn^{−2}}(n²r)^{−|α|}dr ≲ n^{−2}, I get Cε′_nτ^{−3/4}/n = Cε′_nτ^{−1/4}y^{−1/2}. ✓ This is where the
  y^{−1/2} is gained: the right factor A₀(z)D_z replaces the (2,1) amplification n by n·τ·|ζ_z|^{−1/4}. The point
  arg ζ_z ≈ −π/6 lies in the central sector, so Θ_∞ is bounded there (eq:he-Phi-large).
- *Circles and the rest.* Q̃₋ is bounded on both circles (lem:comparison-parametrix(iii), lem:airy(iii)), and
  |Q̃₋Δ₂Q̃₋^{−1}| = |Q̃_inQ̃_out^{−1} − I| = O(1/n). On the lips, Δ₃ = Eṽ^{−1} with |Q̃₋^{±1}| ≤ Cn^{1/2}r^{−1/2} (stated in
  prop:moments' proof), and τ^{−1} ≤ n²/y₀ turns the integral into Cτ^{−1/4}n³e^{−n/C′}. Elsewhere P₀^∞ is bounded
  (eq:Pinf0-bound), and the length is O(n^p). On the band, v = ṽ. Inside U(4c, ε), ṽ = v. ✓
- *Correction term (the L² input).* I checked that ‖Q₋ − Q̃₋‖_{L²(Σ̂)} ≤ C(ε′_nn^{−1/2} + n^{−1}) is derived *inside the
  proof* of prop:moments, under the same hypotheses: n ≥ n₁, the standing assumptions of §5, and ℓ₁ ≡ 1, which
  satisfies (A_ϑ). The derivation is (1 − 𝒞_v)(Q₋ − Q̃₋) = 𝒞₋(Q̃₋(v − ṽ)), with ‖(1 − 𝒞_v)^{−1}‖ ≤ 2C (thm:UR-true)
  and eq:he-L2-columns. I re-derived this identity from Q₋ = I + 𝒞₋(Q₋(v − I)) and the tilde version.
- *Second Cauchy–Schwarz factor.*
  - The Δ₁ part on |ζ_s| ≥ 2: the kernel (2t²/√y + 2√y)/(t² + y)² equals 2/(√y(t² + y)) ≤ 2y^{−3/2}, giving
    ε′_n²n²y^{−3/2} = ε′_n²n^{−1}τ^{−3/2}.
  - The Δ₁ part on |ζ_s| ≤ 2: ε′_nn^{−1/2}τ^{−3/4}.
  - Δ₂: n^{−1}τ^{−1/4}.
  - All four cross products are ≤ Cτ^{−1/4}(ε′_n + n^{−1}) because nτ^{1/2} = √y ≥ √y₀. ✓
- *The comparison frame's lip mismatch.* It enters only via sup|d_n| ≤ Cε′_n and Bessel localisation. No rate is
  needed, and the conclusion |Q(z)| ≤ Cτ^{−1/4} uses only boundedness of ε′_n *given* thm:UR-true. But see F1.
- *Range.* The range y₀n^{−2} ≤ τ ≤ δ/4 is exactly where |ζ_z| ≥ 2 (y₀ = max(2C_f, 1)) and z ∈ U(0, δ/4).

ACCEPT.

**Prop TB-A.**
- |S_n| ≤ |Q|²/|(Q₁)₁₂|.
- (Q₁)₁₂ = (P₁)₁₂ + O(1/n) = ic + O(1/n): expand a = (1 − 4c/z)^{1/4} = 1 − c/z + …, so (a − a^{−1})/(2i) = ic/z.
- ν_n([0, τ]) ≤ Cτ^{1/2} on the range of TB-Q, and trivially for τ > δ/4.
- k > Mn ⟺ X_k < M^{−p}, and τ = M^{−p} ≥ y₀n^{−2} ⟺ M ≤ (n²/y₀)^{1/p}.
- For m = n − 1, Paper 2's construction at degree n − 1 with M′ = Mn/(n − 1) ∈ [M, c₁(n − 1)^{2/p}] when
  M ≤ ½c₁n^{2/p}.

ACCEPT.

**Cor TB-C.**
- A = s(1 + 2/p) + 1, ϑ_* = (s − 1)/(A + 1), and s − 1 − ϑ_* = Aϑ_*.
- γ₁ϑ_* = 1, and γ₁ > 1 + 2/p ⟺ s(1 + 2/p) + 2 > (1 + 2/p)(s − 1), which is true.
- ϑ_* < p(s − 1)/(s(p + 2)) < p/(p + 2) < p/2.

The ranges:
- *Arcsine range:* TB-A.
- *Middle range* [c₁n^{2/p}, n^{γ₁}]: monotonicity and TB-A at the endpoint give Cn^{−1} = C(n^{γ₁})^{−ϑ_*} ≤ CM^{−ϑ_*}.
  This range is non-empty for large n because γ₁ > 2/p.
- *Deep range:* G1 Lemma TL's integer form, μ_n((T, ∞)) ≤ 1156T″^sT^{1−s}/(s − 1) for integer T ≥ T″, with c = C = 1
  for the pure power. TL also states the μ_{n−1} version. Here:
  - T″ ≤ (8p + 2)n^{2+2/p};
  - T = ⌊Mn⌋ ≥ Mn/2, and T ≥ T″ for large n because γ₁ + 1 > 2 + 2/p;
  - the bound is C n^{(2+2/p)s+1−s}M^{1−s} = Cn^AM^{−(s−1)} ≤ CM^{−ϑ_*}, since M^{Aϑ_*} ≥ n^{Aγ₁ϑ_*} = n^A.

The three ranges cover M ≥ 1 with matching endpoints. The moment bound is the Tonelli computation of UL Thm UF.
ACCEPT.

**Prop TB-P.** The statement is word for word G1 §3.16 Thm QLP (a)–(c) for p > 1 (β = min(p, s − 1), the endpoint
ϑ = p/2 when s − 1 > p/2). That theorem is PROVED-mod-cite and REVIEWED for every fixed σ > 1 in RH_px's frame (Lemmas Z,
A, BK, ST, GS). So no new mathematics is needed for the *statement*.

The "re-reading in the Q-frame" is a dictionary for Paper II. I checked it against E_pgt1 §§0, 3, 6:
- 𝒵 ↔ R = QP̂₀^{−1}: matches;
- ‖R₋ − I‖_{L²} = O(1/n) for all s > 1: Prop E.5′'s proof;
- the jump in U₀ is O(n^{−K}min(1, |z|^K)): RH_px Lemma 4.3;
- P̂₀ = A(2πn)^{σ₃/2}σ₃Ψσ₃·(det-1 diagonal): E_pgt1 §3.

Two points of the dictionary are not as stated (F3). They do not affect the label, because the proof of record is
G1 §3.16. ACCEPT WITH FIXES.

**GAP TB-opt, §3.6.** These are correctly labelled GAP and not needed by III. The mechanism sentence and the Christoffel
tail-transfer remark are heuristic (F6). I verified the inequality itself: μ̃_n(k) = w_k(P_{n+1} + u_nP_n)²(x_k)/(x_ku_nh_n)
≤ 2[(b_{n+1}²/(u_nx_k))μ_{n+1}(k) + (u_n/x_k)μ_n(k)], whose coefficients are ≍ (k/n)^p.

**§6 Integration.**
- Prop 8.6 (a)/(b) matches TB-A/TB-P exactly, including the c₁ in the range and m ∈ {n − 1, n}.
- The proof sketch matches TB-Q (y₀ range, row weighting, the L² input to be promoted into the statement).
- III Lemma 6.0 = Cor TB-C, with the right ϑ_*, and Lemma 6.4's hypothesis pa < ϑ_*(p, t).
- Thm 1.4(ii)/(iii) as proposed is exactly what Thm TS and Prop UP-w prove.
- Cor 1.5 for every s > 1 (Thm TS(b) with the anchor 3/2 ∈ (1, 3)) is correct.

One line is too restrictive (F2), and the D5 consequence for TL is correctly flagged.

## 3. Findings

**F1 (minor; overstatement "only boundedness of ε′_n").**
*Issue.* The Verdicts paragraph and §3.6, first bullet, say: "only ε′_n → 0 (indeed only boundedness of ε′_n) is used".
TB-Q's own estimate needs only boundedness. Its inputs do not: thm:UR-true (Neumann series, ‖𝒞_v − 𝒞_ṽ‖ ≤ 1/(2C)), and
through it Q₋ ∈ I + ∂𝒞(L²) and the L² bound (P2-e), need ε′_n + n^{−1} *small*, i.e. ε′_n → 0.
*Fix.* Replace with: "The estimate of Prop TB-Q itself uses only boundedness of ε′_n; its inputs (thm:UR-true, hence
(P2-e)) use ε′_n → 0, without a rate."

**F2 (minor; GAP UP-1+p consequences understated).**
*Issue.* The Thm UF *bounded* form needs base points only at t_0, …, t_{J−1}. The last cell [t_{J−1}, b] needs only
b − t_{J−1} ≤ u₀. So with all base points in the window and u₀ = ½ϑ_*(p, a), Thm UF holds on [a, b] for every
b < 1 + 2p + u₀. Hence, for η < u₀ and s ∈ [1 + p − η, 1 + p + η]:
- F_n(s + p) − F_n(s) is bounded uniformly in n and s, so n^pg_n(s) is bounded above and below uniformly;
- with the uniform b-part (Prop UP-w(i)) and Lemma CT, sup_{n,s}n^pα_n(s) < ∞ on every compact K ⊂ (1, 1 + 2p).

Prop UΛ⁻ uses only this upper bound (UL.md: "sup_{n,K}n^pα_n(s) < ∞"). So **Prop UΛ⁻ holds on every compact of the
window**. Only Thm UΛ (step 1 needs the uniform *limit*) and the a-part *limit* are restricted.
*Fix.*
- In GAP UP-1+p, add: "Uniform boundedness of n^pα_n near 1 + p holds (Thm UF's bounded form with base points in the
  window reaches [a, 1 + 2p + ½ϑ_*(p, a)); PROVED-mod-cite as Thm TS). Only uniform convergence is open."
- In the consequences sentence, change "Thm UΛ (o(log n)) and Prop UΛ⁻ hold … on compacts of (1, 1 + 2p) ∖ {1 + p}
  (UΛ and UΛ⁻ use the uniform a-part)" to "Thm UΛ holds … on compacts avoiding 1 + p (it uses the uniform a-part
  limit); Prop UΛ⁻ holds on every compact of (1, 1 + 2p) (it uses only uniform boundedness)".
- Carry this into §6's III bullets (Prop 6.7 line unchanged; add UΛ⁻).

**F3 (minor; Prop TB-P's frame dictionary).**
*Issue.* (a) Item (A) says the prefactor A = P₀^∞ρ^{σ₃}Mf^{σ₃/4} is bounded "by the maximum principle on |z| = δ". For
p > 1 the classical parametrix uses W̃ with an (h2) jump on (−δ, 0): E_pgt1 §6 has (−δ, 0) in Σ_R, and H_n has a cut on
(−∞, 0) (Lemma E.2). So A is not analytic on U(0, δ). G1 Lemma A handles this with RH_px Lemma 4.2(iii),
Ẽ_N = E^a + Φ, where E^a is analytic and Φ = O(e^{−c′N}), and applies the maximum principle to A^a. The dictionary
drops this step.
(b) E_pgt1 §6 checked α-independence for F1, F5 and Lemma szego (vi)(b), (c), not (vi)(a). TB-P uses (vi)(a) "by the
same check". It is in fact α-free: the first factor's bound (z^α versus (4cz/Υ)^α, a bounded ratio) holds for every
real α. But that check is new and should be recorded.
*Fix.*
- Label: "PROVED-mod-cite (= G1 §3.16 Theorem QLP for p > 1, REVIEWED, proved in RH_px's frame); the Q-frame translation
  below is a presentation note for Paper II §8, checked in outline only".
- In (A), add "A = A^a + O(n^{1/2}e^{−c′n}) with A^a analytic in U(0, δ) (RH_px Lemma 4.2(iii), as in G1 Lemma A); the
  maximum principle is applied to A^a".
- Add one sentence: "Lemma szego (vi)(a) is α-independent (its first factor's bound holds for every real α); this
  extends E_pgt1 §6's check".

**F4 (minor; check hygiene).**
*Issues.*
- The docstring of check_tail.py says "Proposition TB-S", which does not exist (it is TB-Q).
- TAIL §5 says "Runtime ≈ 3 min"; the measured wall time is ≈ 20 s (≈ 1.5 min CPU).
- The additivity line of [2] tests an algebraic identity of the code's own Γ (same arrays). It checks the
  implementation, not the mathematics. TAIL §4 cites it as "checked exactly", which is fine, but it is not evidence.
*Fix.*
- Rename to TB-Q in the docstring.
- State the runtime as "≈ 20 s wall on 8 cores (≈ 1.5 min CPU)".
- In §5 call the additivity line an implementation check.
- Re-run, commit the .out (only if it changes), and update the MANIFEST lines.

**F5 (INFO; §1 (N) "Equivalently").** A tail exponent ϑ gives moments for u < ϑ (Tonelli). Moments for every u < ϑ give
tail exponents ϑ′ < ϑ (Markov), not ϑ itself. *Fix:* "equivalently, up to the endpoint exponent".

**F6 (minor; unlabelled heuristics).**
- *GAP TB-opt.* The sentence "the Bessel part of the main term is ≍ ε′_n√n|ζ_z|^{−3|α|/2} …" is an unproved
  mechanism.
- *§3.6, third bullet.* The Christoffel tail-transfer remark ("loses exactly the arcsine decay") is a correct
  inequality plus a heuristic conclusion.
- *§3.2, "Why the row weighting is needed".* The fallback exponent (s − 1)/(2s(1 + 2/p) + 3) is correct (I re-derived it
  from the range M ≤ cn^{1/p}: γ₁ϑ = ½, then ϑ ≤ (s − 1)/(2A + 1)). It is not used.
*Fix.*
- Mark the TB-opt sentence and the §3.6 remark as HEURISTIC / OBSTRUCTION, scoped to "this route".
- Mark the fallback as "remark, not used".

**F7 (minor; Integration wording).**
*Issue.* (P2-e)'s L² bound is used as an input, but it is stated only inside prop:moments' proof. TAIL flags this in
Rule A (vii) and in Prop 8.6's sketch. It should also go into the "Into Paper II" list as a required edit of II's
Prop 6.6. Without it, Prop 8.6(a) would cite a proof-internal estimate.
*Fix.* Add the bullet "Prop 6.6 (= prop:moments): add ‖Q₋ − Q̃₋‖_{L²(Σ̂)} ≤ C(ε′_nn^{−1/2} + n^{−1}) to the statement
(required by Prop 8.6(a))".

## 4. Required before REVIEWED

Apply F1–F4, F6 and F7. F5 is optional. If check_tail.py changes (F4), re-run it and update MANIFEST.sha256. After that,
TAIL.md's PROVED and PROVED-mod-cite statements can carry REVIEWED with the labels in the table above, and the §6
integration into Papers II/III, UL.md's (QLP-c) input line and THEOREMS.md can proceed. A diff-check of the fixes by a
second reader is sufficient; no re-derivation is needed.
