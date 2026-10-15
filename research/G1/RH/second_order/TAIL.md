# TAIL: the hard-edge tail bound that UL.md needs, proved in Paper 2's frame; the telescoping reduction (Plan 69)

Status (2026-10-15): written by the Plan 69 agent; **not REVIEWED** (Rule R pending). Labels per VERIFICATION_POLICY.md.
"RH" means Riemann–Hilbert throughout. This file serves decision D2 of the three-paper split (planning documents kept
locally under research/program/papers_split/, not published): Paper III's uniform-in-s results (UL.md) use the hard-edge
tail bound Theorem QLP(c) of G1 PROOF.md §3.16, which is proved there only through the older RH analyses (RH_px,
RH₁(r), RH_plt1b). Here we (1) state exactly what UL.md uses, (2) check the telescoping reduction of the Cesàro s-law to
the window 1 < s < 1 + 2p, and (3) prove a sufficient tail bound inside Paper 2's frame (papers/paper2, §§5–7 and
App. A–D, the comparison-parametrix frame), for every p > 0 in the window, and for p > 1 and every s > 1 with the
classical module that Paper II's §8 will contain. Nothing in SECOND.md, UL.md, THEOREMS.md or papers/ is changed.

**Summary of labels.** Setting of UL.md §0: σ_s = σ_{p,s} = Σ_{k≥1}k^{−s}δ_{x_k}, x_k = k^{−p}, p > 0, s > 1; μ_n^{(s)}(k) =
k^{−s}π_n^{(s)}(x_k)²/h_n(s) (Paper III's m_n); c = c(p); α := (s − 1 − p)/p; the *window* is 1 < s < 1 + 2p (|α| < 1).

| # | Statement | Label |
|---|---|---|
| §1 (N) | what UL.md uses: for each base point t that its proofs use, some u > 0 with sup_{n≥n₀}E_{μ_n^{(t)}}[(k/n)^u] < ∞ (equivalently a tail bound μ_n^{(t)}((Mn, ∞)) ≤ CM^{−ϑ} for all M ≥ 1, some ϑ > 0), with ϑ bounded below on compact sets of t; the exponent min(p/2, t − 1) of QLP(c) is never needed | audit (no new claim) |
| Lemma TS | telescoping: Γ_n(s₀, s₁) is additive; Christoffel–Cesàro gives Γ_n(s, s + p) → 0 for every s > 1 | PROVED (elementary) + PROVED-mod-cite (II Cor 1.3, as SECOND Thm 3.2) |
| **Thm TS** | for every p > 0 and all s₀, s₁ > 1, Γ_n(s₀, s₁) → 0 (the Cesàro s-law with constant), using the tail bound only at points of the window; uniform on K × K for compact K ⊂ (1, 1 + 2p) | PROVED-mod-cite (UL.md UF-lim restricted to the window + Cor TB-C; SECOND Thm 3.2) |
| Prop UP-w | uniform law on compact K ⊂ (1, 1 + 2p): the b-part on every such K; the a-part on every compact K ⊂ (1, 1 + 2p) ∖ {1 + p} | PROVED-mod-cite (as Thm TS; Paper 2 lem:transfer) |
| GAP UP-1+p | for p ≤ 1: the a-part of the uniform law on a neighbourhood of s = 1 + p | **GAP** |
| Lemma ST | Stieltjes tail bound (= G1 §3.16 Lemma ST) | PROVED (elementary) |
| Lemma GS | row-product identity for the Stieltjes transform of μ_n (= G1 §3.16 Lemma GS; KNOWN, Teschl (1.99)–(1.100), (2.122), not re-read) | PROVED |
| **Prop TB-Q** | comparison frame, p > 0, 1 < s < 1 + 2p: \|Q(z)\| ≤ C\|z\|^{−1/4} on the ray arg z = 5π/6 for y₀n^{−2} ≤ \|z\| ≤ δ/4 (i.e. down to the Bessel scale) | PROVED-mod-cite (Paper 2 rev. 3 §§5–7, App. A–D, as reviewed in G1 §3.24 (Plan 55); Conway–Deift Thm 4.4 via Paper 2 T3(b)) |
| **Prop TB-A** | p > 0, 1 < s < 1 + 2p: μ_m((Mn, ∞)) ≤ C·M^{−p/2} for 1 ≤ M ≤ c₁n^{2/p}, n ≥ n₀, m ∈ {n − 1, n} (QLP(a) up to the Bessel scale) | PROVED-mod-cite (Prop TB-Q; Lemmas ST, GS; Paper 2 Prop. prop:moments) |
| **Cor TB-C** | p > 0, 1 < s < 1 + 2p: μ_m((Mn, ∞)) ≤ C·M^{−ϑ_*} for **all** M ≥ 1, ϑ_* := (s − 1)/(s(1 + 2/p) + 2) | PROVED-mod-cite (Prop TB-A; G1 §3.4 Lemma TL, whose Markov/Chebyshev inputs are quoted as textbook, not checked against a source — decision D5) |
| Prop TB-P | p > 1, every s > 1: Theorem QLP (a)–(c) of G1 §3.16 in the frame of Paper II's classical module (planned §8 = RH_px §§4–5 in the Q-frame, E_pgt1 §§0, 3, 6) | PROVED-mod-cite (= QLP's proof for p ≠ 1, re-read in that frame: RH_px [REVIEWED]; KMVV (6.23), (6.28); DLMF 10.25.2, 10.32.4, 10.32.9) |
| GAP TB-opt | p ≤ 1, window: QLP(b)–(c) with the exponent min(p/2, s − 1) inside Paper 2's frame (below the Bessel scale). Not needed by III. (Proved in the repo by RH₁(r), RH_plt1b, G1 §3.16.) | GAP (in II's frame only) |

**Verdicts.** Telescoping (task 2): **correct**, written out in §2; it reduces the *pointwise* Cesàro s-law to the
window, but not the uniform statements outside it. p ≤ 1 (task 3): the comparison frame **does** suffice. Its lip mismatch
has no rate, but after conjugation by the comparison solution and Bessel localisation it contributes O(ε′_n) relative to
the main term on the ray, for every point down to the Bessel scale; the deep tail is soft (Lemma TL). The price is a
small, explicit exponent ϑ_* in place of min(p/2, s − 1); UL.md needs only some positive exponent. What III loses relative
to `PAPER_III_OUTLINE.md`: only the a-part of the uniform law (Thm 1.4(iii)) near s = 1 + p when p ≤ 1 (and with it Thm UΛ
/ Prop 6.6 on compacts containing 1 + p). Cor 1.5 survives for **every** s > 1 (not only s ∈ 3/2 + ℕ₀).

Novelty: UNCHECKED (no Rule L search). Checks: `checks/check_tail.py` (.out), NUMERICAL (§5).

## 0. Inputs (all internal or already cited in the repo)

From Paper 2 (papers/paper2, rev. 3; proof of record of G1 §3.24 Theorem AS, PROVED-mod-cite, REVIEWED). Standing
assumptions there: p > 0, 1 < s < 1 + 2p, ℓ₁ analytic of some angle ((A_ϑ); here ℓ₁ ≡ 1). Labels are Paper 2's LaTeX
labels.
- (P2-a) The frame: U(z) = n^{pnσ₃}Y(zn^{−p}) (eq:U), with Y of T1(a) (eq:Y-solution), Y₁₁ = P_n,
  Y₁₂(z) = Σ_kw_kP_n(x_k)/(z − x_k); nodes X_k = (n/k)^p. In Ω_∞ (outside the lens and the saturated region),
  Q = D_∞^{−σ₃}VD_W^{σ₃} and V = C_∞e^{−nγ_pσ₃}U·(e^{nφ}F)^{σ₃} (eq:VM, eq:Q), so **Q = C·U·k^{σ₃}** there, with C a
  constant diagonal matrix and k = e^{nφ}FD_W scalar; Q = I + Q₁/z + O(z^{−2}) at ∞ (lem:normalisation, F8).
- (P2-b) Contour near 0 (F3, eq:he-lipangle): in U(0, δ) only the band (0, δ) and the two lips, with
  ¾θ_lip ≤ |arg z| ≤ 5/4·θ_lip < θ_w < π/2 on the lips (eq:angles).
- (P2-c) Comparison solution (eq:he-Qtilde, eq:he-P0hat): in U(0, δ), Q̃ = A₀(2πn)^{σ₃/2}Φ_α(ζ), ζ = n²f(z), with A₀
  analytic on U(0, δ), det A₀ = 1, |A₀^{±1}| ≤ C (lem:comparison-parametrix(i)); |f(z)| ≍ |z|, f′(0) < 0 (F6);
  Φ_α = ζ^{−σ₃/4}Θ_∞ with |Θ_∞^{±1}| ≤ C for |ζ| ≥ 2 (eq:he-Phi-large); |Φ_α^{±1}| ≤ C|ζ|^{−|α|/2} for |ζ| ≤ 3, with
  1 + |log|ζ|| in place of |ζ|^{−|α|/2} at α = 0 (eq:he-Phi-small, lem:bessel-local(iii)). On the circles,
  |Q̃^{±1}| ≤ C (lem:comparison-parametrix(iii), lem:airy(iii)).
- (P2-d) The mismatch (eq:he-dn, lem:lip-mismatch, eq:he-localisation): v − ṽ = d_ne₂e₁ᵀ + E on the lips in U(0, δ), with
  |d_n(s)| ≤ C𝔪_n(s)e^{−n|s|^{1/2}/C}, 𝔪_n(s) = |s|^{ν_p}log(2/|s|) + ε_Λ(T_n), ν_p = min(1/p, ½); ε′_n := n^{−2ν_p}log n +
  ε_Λ(T_n) → 0 (eq:he-epsprime; ε_Λ ≡ 0 for ℓ₁ ≡ 1); |E| ≤ Ce^{−n|s|^{−1/p}/C} (F4); |v − ṽ| = O(1/n) on the circles Σ_∘;
  |v − ṽ| ≤ Ce^{−n/C} on the rest of Σ, of length O(n^p) (F5); v = ṽ = J on the band.
- (P2-e) Theorem thm:UR-true and Proposition prop:moments with its proof: Q_± ∈ I + ∂𝒞(L²(Σ̂)),
  Q̃_±^{±1} ∈ I + ∂𝒞(L²(Σ̂)) (prop:UR-comparison(i)); Q₁ = P₁ + O(1/n); and (proof of prop:moments, "The correction
  term") **‖Q₋ − Q̃₋‖_{L²(Σ̂)} ≤ C(ε′_nn^{−1/2} + n^{−1})**.
- (P2-f) T3(b) (Conway–Deift Thm 4.4, as quoted in Paper 2 sec_2 with hypotheses): under the hypotheses verified in the
  proof of prop:moments, for z ∉ Σ̂,
  𝓡(z) := Q(z)Q̃(z)^{−1} = I + (1/2πi)∫_{Σ̂}𝓔(s)ds/(s − z), 𝓔 := Q₋(v − ṽ)ṽ^{−1}Q̃₋^{−1}.
- (P2-g) P₀^∞ = I + P₁/z + …, (P₁)₁₂ = ic (expand a = (1 − 4c/z)^{1/4} in eq:Pinf0; E_pgt1 §0 lists P₁).
- (P2-h) lem:transfer: for a measure σ on [0, ∞), u_n := −P_{n+1}(0)/P_n(0) > 0, l_n := b_n²/u_{n−1}; a_n = u_n + l_n; the
  coefficients of xσ are ã_n = u_n + l_{n+1}, b̃_n² = u_nl_n; and h_n(xσ) = u_nh_n(σ) (SECOND Prop 3.1).

Repo inputs: II Cor 1.3 = Paper 2 thm:pure (Law P for σ_{p,s}, every p > 0, s > 1); SECOND Thm 3.2 (Christoffel–Cesàro;
needs only Law P without rate and Lemma CS); G1 §3.4 Lemma TL (PROVED, REVIEWED; standard inputs Markov/Chebyshev "not
checked against a specific source"); UL.md (REVIEWED).

## 1. What UL.md actually needs (task 1)

UL.md cites (QLP-c) in the form "for fixed t and every ϑ < min(p/2, t − 1): μ_m^{(t)}((Mn, ∞)) ≤ C_ϑM^{−ϑ}, all M ≥ 1".
Every use, read line by line:

| Use in UL.md | What is used | M range | s range | exponent |
|---|---|---|---|---|
| Thm UF, B_t | sup_{n≥n₀}E_t[(k/n)^{u₀}] < ∞ at grid points t = t_i ∈ K, via Tonelli: E_t[(k/n)^{u₀}] ≤ 2 + ∫_1^∞u₀M^{u₀−1}μ_n^{(t)}((Mn, ∞))dM | all M ≥ 1 | grid points of K | any ϑ₀ > u₀, and u₀ ≤ p/4 is a free step size: some ϑ₀(t) > 0 bounded below on K suffices (then take u₀ := ½inf_K ϑ₀) |
| Lemma W, V₋ | sup_nE_t[Y^{−a′}] < ∞ (Y = n^px) for some a′ > a | all M | the fixed t | pa′ < ϑ(t), with a ∈ {r_u (→ 0), δ (→ 0)}: any positive exponent |
| Thm UF-lim | Lemma W with g(y) = y^{±r_u}, r_u = u/p, u ≤ u₀; u → 0 at the end | all M | grid points t_i = a + iu of K (countably many in all) | any positive (u is chosen below it) |
| Cor UL-3.8, UL-3.10, Thm UP | through UF-lim | — | K (and [a, b + p] for the g-part of UP) | — |
| Prop UΛ-L¹ | Lemma W with g = log | all M | every s ∈ K | any positive |
| Prop R (reduction for (UΛ-O(1))) | Λ_n(a) = O(1) at one point (QLP-Λ: Λ_n ≤ C_ϑ/ϑ) | all M | one point | any positive |
| Thm UΛ, Prop UΛ⁻ | not used (they use UP and Lemma TL) | — | — | — |

The index m = n − 1 is never used (E_t := E_{μ_n^{(t)}} throughout); no uniformity of the constants in t is used (RU is
not needed), only that the admissible exponent is bounded below on K (for the grid step in Thm UF).

**(N) — the statement UL.md needs.** For each t in the set of base points used (a compact K ⊂ (1, ∞), together with the
enlargement of K in the proof of UF-lim): there are ϑ(t) > 0 with inf_{t∈K}ϑ(t) > 0, and C_t, n₀(t), such that
μ_n^{(t)}((Mn, ∞)) ≤ C_tM^{−ϑ(t)} for all M ≥ 1 and n ≥ n₀(t). Equivalently (Tonelli one way, Markov the other):
sup_{n≥n₀}E_{μ_n^{(t)}}[(k/n)^u] < ∞ for every u < ϑ(t).

Since the deep tail M ≥ n^{γ} (some γ = γ(p, s)) is soft (Lemma TL), (N) reduces to a bound in a polynomial range of M
(Cor TB-C below). The arcsine-range exponent p/2 and the hard-edge exponent s − 1 of QLP play no role in UL.md.

## 2. The telescoping reduction (task 2)

For s₀, s₁ > 1 put

  Γ_n(s₀, s₁) := Σ_{j=1}^n log(b_j(s₁)/b_j(s₀)) + ((s₁ − s₀)/2)·log n − ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)).

Cor UL-3.8 (= III Thm 1.4(ii)) is the statement Γ_n(s₀, s₁) → 0; the equivalent form is
log(h_n(s₁)/h_n(s₀)) = 2Γ_n(s₀, s₁) − (s₁ − s₀)log n + ((s₁ − s₀)/p)log c, from h_n(s) = ζ(s)Π_{j≤n}b_j(s)² (UL Cor UL-3.8
proof), i.e. Γ_n = ½(F_n(s₁) − F_n(s₀) − ((s₁ − s₀)/p)log c) with F_n(s) = log h_n(s) + s log n.

**Lemma TS (PROVED: (i), (ii) elementary; (iii) PROVED-mod-cite: SECOND Thm 3.2, II Cor 1.3).**
- (i) Γ_n(s₀, s₂) = Γ_n(s₀, s₁) + Γ_n(s₁, s₂) and Γ_n(s₁, s₀) = −Γ_n(s₀, s₁), for all s₀, s₁, s₂ > 1 and n ≥ 1.
- (ii) For s > 1 let m(s) := ⌈(s − 1)/p⌉ − 1 ≥ 0 and r(s) := s − m(s)p ∈ (1, 1 + p]. Then
  Γ_n(s₀, s₁) = Γ_n(r₀, r₁) − Σ_{j=0}^{m₀−1}Γ_n(r₀ + jp, r₀ + (j + 1)p) + Σ_{j=0}^{m₁−1}Γ_n(r₁ + jp, r₁ + (j + 1)p),
  r_i := r(s_i), m_i := m(s_i).
- (iii) For every s > 1, Γ_n(s, s + p) → 0.

*Proof.* (i) Each of the three terms of Γ_n is additive along s₀ → s₁ → s₂: the sum telescopes termwise, the coefficient
of log n is linear in s₁ − s₀, and log(c^{(s₂−s₀)/p}ζ(s₀)/ζ(s₂)) = log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) +
log(c^{(s₂−s₁)/p}ζ(s₁)/ζ(s₂)). Antisymmetry is the case s₂ = s₀ (Γ_n(s, s) = 0). (ii) m(s) is the largest integer m ≥ 0 with
s − mp > 1, so r(s) ∈ (1, 1 + p]. Write Γ_n(s₀, s₁) = Γ_n(s₀, r₀) + Γ_n(r₀, r₁) + Γ_n(r₁, s₁) by (i), and
Γ_n(r, r + mp) = Σ_{j<m}Γ_n(r + jp, r + (j + 1)p) by (i) again; Γ_n(s₀, r₀) = −Γ_n(r₀, s₀). (iii) With s₁ − s₀ = p,
Γ_n(s, s + p) = Σ_{j≤n}log(b_j(s + p)/b_j(s)) + (p/2)log n − ½log(cζ(s)/ζ(s + p)), and SECOND Thm 3.2 (III Thm 1.4(i)) says
this tends to 0; its proof uses only n^pg_n(s) → c, which follows from Law P for σ_s (II Cor 1.3, every p > 0, s > 1) by the
chain-limit lemma (Paper 2 lem:chain-limit). ∎

**Theorem TS (PROVED-mod-cite: UL.md Thm UF-lim with its base points restricted to the window, Cor TB-C below for those
base points, Lemma TS).** Let p > 0.
- (a) For every compact K ⊂ (1, 1 + 2p): sup_{s₀,s₁∈K}|Γ_n(s₀, s₁)| → 0.
- (b) For all s₀, s₁ > 1: Γ_n(s₀, s₁) → 0. That is, Cor UL-3.8 (III Thm 1.4(ii)) holds for every p > 0 and every pair
  s₀, s₁ > 1, and the hard-edge tail bound is used only at points of the window.

*Proof.* (a) Let K ⊂ [a, b] ⊂ (1, 1 + 2p). Put a″ := min(a, 1 + p/2) and b″ := max(b, a″ + p). Then
1 < a″ ≤ b″ < 1 + 2p (as a″ + p ≤ 1 + 3p/2) and b″ − a″ ≥ p. Run the proof of UL.md Thm UF-lim on K″ := [a″, b″] as written
("Enlarge K so that b ≥ a + p" is satisfied by K″ itself). Its inputs are (P) and (LP) at every point (II Cor 1.3 and G1
Lemma LP: no window restriction), (CS) at s = a″ (no restriction), and (QLP-c) at the grid points t_i ∈ K″, which UL.md uses
only in the form (N) of §1. Cor TB-C gives (N) at every t ∈ K″ with ϑ(t) = ϑ_*(p, t) = (t − 1)/(t(1 + 2/p) + 2); this is
increasing in t, so inf_{K″}ϑ_* = ϑ_*(p, a″) > 0, and Thm UF's step is taken as u₀ := ½ϑ_*(p, a″) (≤ p/4 since ϑ_* < p/2).
Lemma W holds at each t ∈ K″ with the condition pa < ϑ_*(p, t) in place of pa < min(p/2, t − 1) (its proof uses only the
finiteness of V₋ for some a′ > a, and pa′ < ϑ_* < p/2 keeps the arcsine law's moment finite). So UF-lim holds on K″, which
is (a) by the identity Γ_n = ½(F_n(s₁) − F_n(s₀) − ((s₁ − s₀)/p)log c).
(b) Lemma TS(ii): r₀, r₁ ∈ (1, 1 + p] ⊂ (1, 1 + 2p), so Γ_n(r₀, r₁) → 0 by (a) with K = {r₀, r₁}, and each of the finitely many
chain terms tends to 0 by Lemma TS(iii). ∎

*What the telescoping does not give.* Uniformity of (b) on compacts outside the window. Along Lemma TS(ii) with r ranging
over a compact set, the chain terms Γ_n(r + jp, r + (j + 1)p) → 0 would be needed uniformly in r, i.e. n^pg_n → c uniformly
on compacts of (1 + p, ∞) (as F_n(t + p) − F_n(t) = log(n^pg_n(t))). That is a uniform form of the chain-limit lemma (or a
tail bound at points outside the window), which is not available for p ≤ 1. For p > 1 Prop TB-P gives the tail bound at
every s > 1 and UL.md applies verbatim on every compact K ⊂ (1, ∞).

**Proposition UP-w (uniform law in the window; PROVED-mod-cite: Thm TS(a), Paper 2 lem:transfer, SECOND Prop 3.1, II
Cor 1.3).** Let p > 0 and K ⊂ (1, 1 + 2p) compact.
- (i) sup_{s∈K}|n^pb_n(s) − c| → 0.
- (ii) If moreover 1 + p ∉ K, then sup_{s∈K}|n^pα_n(s) − 2c| → 0 (α_n = a_n, the standard pairing).

*Proof.* (i) is UL.md Thm UP's b-part, which uses only UF-lim on K (log b_n(s)² − log b_n(s₀)² = Δ_n(s) − Δ_{n−1}(s) −
(s − s₀)log(n/(n − 1))); UF-lim holds on K by Thm TS(a). (ii) K ⊂ K₁ ∪ K₂ with K₁ := K ∩ (1, 1 + p) and K₂ := K ∩ (1 + p, 1 + 2p),
both compact. On K₁: K₁ ∪ (K₁ + p) is a compact subset of the window, so n^pg_n(s) = exp(F_n(s + p) − F_n(s)) → c uniformly on
K₁ by Thm TS(a) (here g_n = u_n of lem:transfer, and h_n(s + p)/h_n(s) = g_n(s), SECOND Prop 3.1), and
α_n = g_n + b_n²/g_{n−1} (lem:transfer(i)) with (i) gives the claim. On K₂: σ_s = x·σ_{s−p}, so by lem:transfer(ii)
α_n(s) = g_n(s − p) + b_{n+1}(s − p)²/g_n(s − p); K₂ − p and K₂ are compact subsets of the window, so
n^pg_n(s − p) = exp(F_n(s) − F_n(s − p)) → c and (n + 1)^pb_{n+1}(s − p) → c uniformly for s ∈ K₂ (Thm TS(a), (i)). ∎

**GAP UP-1+p (p ≤ 1).** The a-part of the uniform law on a neighbourhood of s = 1 + p (α = 0). At s = 1 + p both routes in
the proof of (ii) need F_n at a boundary point of the window (s + p = 1 + 2p, i.e. α = 1, or s − p = 1). Pointwise Law P at
s = 1 + p holds (II Cor 1.3). For p > 1 there is no gap (Prop TB-P and UL.md Thm UP on any compact of (1, ∞)). Consequences
for III: Thm 1.4(iii)'s a-part, Thm UΛ (o(log n)) and Prop UΛ⁻ hold, for p ≤ 1, on compacts of (1, 1 + 2p) ∖ {1 + p}
(UΛ and UΛ⁻ use the uniform a-part); the b-part, Thm 1.4(ii) and Cor 1.5 are not affected.

*Check of the outline's claim.* `PAPER_III_OUTLINE.md` (Thm 1.4) says: "(ii) … uniformly for s₀, s₁ in compact subsets of
(1, 1 + 2p) (of (1, ∞) if p > 1)", and the telescoping reduces (ii) for arbitrary s₀, s₁ to the window. Both are correct
(Thm TS; Prop TB-P for p > 1). "(iii) For every compact K ⊂ (1, 1 + 2p) … sup(|n^pb_n − c| + |n^pa_n − 2c|) → 0": correct for
the b-part; for the a-part with p ≤ 1 only on compacts avoiding 1 + p (GAP UP-1+p). For p > 1 (iii) holds on compacts of
(1, ∞).

## 3. The tail bound in Paper 2's frame (task 3)

### 3.1 Two elementary lemmas (restated from G1 PROOF.md §3.16, with proofs)

**Lemma ST (PROVED).** Let ν be a probability measure on [0, ∞), S(z) := ∫dν(X)/(X − z), τ > 0 and z = τe^{iθ},
π/2 < θ ≤ π. Then ν([0, τ]) ≤ (4τ/|cos θ|)|S(z)|. For θ = 5π/6: ν([0, τ]) ≤ (8/√3)τ|S(z)|.
*Proof.* For X ≥ 0, Re 1/(X − z) = (X + τ|cos θ|)/|X − z|² ≥ 0; for 0 ≤ X ≤ τ, |X − z|² = (X + τ|cos θ|)² + τ²sin²θ ≤ 4τ², so
Re 1/(X − z) ≥ |cos θ|/(4τ). Hence ν([0, τ])|cos θ|/(4τ) ≤ Re S ≤ |S|. ∎

**Lemma GS (PROVED; KNOWN, Teschl, *Jacobi Operators*, (1.99)–(1.100), (2.122), not re-read for this file).** Let U be as
in (P2-a), ν_n the image of μ_n under k ↦ X_k = (n/k)^p, and S_n(z) := Σ_kμ_n(k)/(X_k − z). If, at a point z ∉ {X_k} ∪ {0}
and in a neighbourhood of ∞, Q = C·U·k^{σ₃} with C constant diagonal, k scalar, and Q = I + Q₁/z + O(z^{−2}) at ∞, then
S_n(z) = −Q₁₁(z)Q₁₂(z)/(Q₁)₁₂.
*Proof.* U₁₁ = π (monic, π(X) = n^{pn}P_n(Xn^{−p})) and U₁₂(z) = Σ_kω_kπ(X_k)/(z − X_k), ω_k := n^pw_k ((P2-a): residue
n^pw_kU₁₁(X_k), and the sum decays at ∞). Since (π(z) − π(X))/(z − X) is a polynomial of degree n − 1 in X, orthogonality
gives U₁₁(z)U₁₂(z) = Σ_kω_kπ(X_k)²/(z − X_k) = −h·S_n(z), h := Σ_kω_kπ(X_k)². Expanding U₁₂ at ∞, the first non-zero term is
h z^{−n−1}, so (U z^{−nσ₃})₁ has (1,2) entry h. For Q = CUk^{σ₃}: Q₁₁Q₁₂ = C₁²U₁₁U₁₂ (k cancels); Q₁₁ → 1 forces
C₁z^nk(z) → 1, so (Q₁)₁₂ = lim zQ₁₂ = C₁·lim zU₁₂/k = C₁²h. ∎

### 3.2 The key estimate: the comparison solution controls Q on the ray, down to the Bessel scale

Fix the standing assumptions of Paper 2 §5 (p > 0, 1 < s < 1 + 2p, here ℓ₁ ≡ 1), the radii δ, ε and the contour of
Paper 2 §5, and θ_z := 5π/6. For z = τe^{iθ_z} put ζ_z := n²f(z), y := n²τ, and

  D_z := (2πn)^{σ₃/2}ζ_z^{−σ₃/4},  so that  Q̃(z) = A₀(z)D_zΘ_∞(ζ_z) when |ζ_z| ≥ 2  ((P2-c); diagonal factors commute).

Since |f(z)| ≍ |z|, the two entries of D_z have moduli (2π)^{±1/2}|f(z)|^{∓1/4} ≍ τ^{∓1/4}; hence |A₀(z)D_z| ≤ Cτ^{−1/4} for
τ ≤ 1. Let C_f be such that |f(z)| ≥ |z|/C_f on U(0, δ), and y₀ := max(2C_f, 1), so that |ζ_z| ≥ 2 whenever y ≥ y₀.

**Proposition TB-Q (PROVED-mod-cite: Paper 2 (P2-a)–(P2-g)).** There are C, n₀ such that for n ≥ n₀ and
z = τe^{iθ_z} with y₀n^{−2} ≤ τ ≤ δ/4,

  |(𝓡(z) − I)A₀(z)D_z| ≤ C(ε′_n + n^{−1})τ^{−1/4},  and hence  |Q(z)| ≤ Cτ^{−1/4}.

*Proof.* z lies in Ω_∞ ∩ U(0, δ/4) and off Σ̂ ((P2-b): the lips stay in |arg z| < π/2). By (P2-f),
(𝓡(z) − I)A₀(z)D_z = (1/2πi)∫_{Σ̂}𝓔(s)A₀(z)D_z ds/(s − z). Geometry: for s in the band (0, δ) the angle between s and z is
5π/6, and for s on a lip in U(0, δ) it is at least 5π/6 − π/2 = π/3; in both cases |s − z| ≥ ½(|s| + |z|). Every other point of
Σ̂ is at distance ≥ 3δ/4 from z. Write (v − ṽ)ṽ^{−1} = Δ₁ + Δ₂ + Δ₃ as in the proof of prop:moments (Δ₁ = d_ne₂e₁ᵀ on the
lips in U(0, δ), Δ₂ = ṽ^{−1} − I on Σ_∘, Δ₃ the exponentially small rest), and Q₋ = Q̃₋ + (Q₋ − Q̃₋). Put
B(s) := A₀(s)^{−1}A₀(z); since A₀^{±1} are bounded on U(0, δ) and A₀ is Lipschitz on U(0, δ/2) (Cauchy estimates),
|B(s) − I| ≤ C(|s| + |z|) for s ∈ U(0, δ). Write r := |s|, t := n r^{1/2} (so |ζ_s| ≍ t²).

*Main term on the lips, |ζ_s| ≥ 2.* Q̃(s)Δ₁Q̃(s)^{−1}A₀(z)D_z = d_n·(Q̃(s)e₂)(e₁ᵀQ̃(s)^{−1}A₀(z)D_z), a rank-one matrix.
Here |Q̃(s)e₂| = |A₀(s)D_sΘ_∞(ζ_s)e₂| ≤ C(r^{−1/4} + r^{1/4}) ≤ Cr^{−1/4}, and
e₁ᵀQ̃(s)^{−1}A₀(z)D_z = e₁ᵀΘ_∞(ζ_s)^{−1}N, N := D_s^{−1}B D_z = diag(a_s, a_s^{−1})·B·diag(a_z^{−1}, a_z), a_w := (2πn)^{−1/2}ζ_w^{1/4},
|a_w| ≍ |w|^{1/4}. With |B − I| ≤ C(r + τ): |N₁₁| ≤ C(r/τ)^{1/4}, |N₂₂| ≤ C(τ/r)^{1/4}, |N₁₂| ≤ C(r + τ)(rτ)^{1/4} ≤ C,
|N₂₁| ≤ C(r + τ)(rτ)^{−1/4} ≤ C((r/τ)^{1/4} + (τ/r)^{1/4}) (split r ≤ τ, r ≥ τ; r, τ ≤ 1). So |N| ≤ C((r/τ)^{1/4} + (τ/r)^{1/4}),
and with |d_n| ≤ C𝔪_n(s)e^{−t/C} and |ds| ≤ C dr on the lips, this part is at most

  Cτ^{−1/4}∫𝔪_n e^{−t/C}[1 + (τ/r)^{1/2}]dr/(r + τ) = Cτ^{−1/4}∫_{t≳1}𝔪_n e^{−t/C}[2t/(t² + y) + 2√y/(t² + y)]dt
  ≤ Cτ^{−1/4}∫_{t≳1}𝔪_n(t²/n²)e^{−t/C}(1 + 1/t)dt ≤ Cε′_nτ^{−1/4},

using 2t ≤ t² + y (as y ≥ 1) and 2√y ≤ (t² + y)/t (AM–GM), and 𝔪_n(t²/n²) ≤ C(t^{2ν_p}n^{−2ν_p}(log n + |log t| + 1) + ε_Λ(T_n)).

*Main term on the lips, |ζ_s| ≤ 2* (so r ≤ Cn^{−2} ≤ Cτ, and 𝔪_n(s) ≤ Cε′_n). Now |Q̃(s)e₂| ≤ C√n|ζ_s|^{−|α|/2} and
e₁ᵀQ̃(s)^{−1}A₀(z)D_z = e₁ᵀΦ_α(ζ_s)^{−1}G, G := (2πn)^{−σ₃/2}B(2πn)^{σ₃/2}ζ_z^{−σ₃/4}, whose entries are B₁₁ζ_z^{−1/4},
B₁₂ζ_z^{1/4}/(2πn), 2πnB₂₁ζ_z^{−1/4}, B₂₂ζ_z^{1/4}. With |B − I| ≤ Cτ and |ζ_z| ≍ n²τ ≥ 2: n·τ·|ζ_z|^{−1/4} ≍ |ζ_z|^{1/4}τ^{1/2},
so |G| ≤ C|ζ_z|^{1/4} ≤ Cn^{1/2}τ^{1/4}. Hence, with |s − z| ≥ τ/2 and ∫_0^{Cn^{−2}}(n²r)^{−|α|}dr ≤ Cn^{−2} (|α| < 1),
this part is at most Cε′_n√n·n^{1/2}τ^{1/4}·τ^{−1}·n^{−2} = Cε′_nτ^{−1/4}/(nτ^{1/2}) = Cε′_nτ^{−1/4}y^{−1/2}. (At α = 0 replace
|ζ_s|^{−|α|} by (1 + |log|ζ_s||)², still integrable.)

*Main term on the circles and the rest.* On Σ_∘, |Δ₂| ≤ C/n, |Q̃₋^{±1}| ≤ C, |s − z| ≥ 3δ/4: contribution ≤ Cn^{−1}τ^{−1/4}.
Δ₃ on the lips in U(0, δ): |Q̃₋^{±1}| ≤ Cn^{1/2}r^{−1/2} (proof of prop:moments), |E| ≤ Ce^{−nr^{−1/p}/C}, |s − z| ≥ τ/2:
≤ Cτ^{−5/4}∫n r^{−1}e^{−nr^{−1/p}/C}dr ≤ Cτ^{−1/4}n³e^{−n/C′} (τ ≥ y₀n^{−2}). Δ₃ elsewhere: |Q̃^{±1}| ≤ C, |s − z| ≥ c,
length O(n^p): ≤ Cn^pe^{−n/C}τ^{−1/4}.

*Correction term* ∫(Q₋ − Q̃₋)(Δ₁ + Δ₂ + Δ₃)Q̃₋^{−1}A₀(z)D_z ds/(s − z). By Cauchy–Schwarz it is at most
‖Q₋ − Q̃₋‖_{L²(Σ̂)}·‖(v − ṽ)ṽ^{−1}Q̃₋^{−1}A₀(z)D_z/(s − z)‖_{L²(Σ̂)}, and the first factor is ≤ C(ε′_nn^{−1/2} + n^{−1}) (P2-e).
In the second, the Δ₁ part on |ζ_s| ≤ 2 is ≤ Cε′_n·n^{1/2}τ^{1/4}·τ^{−1}·(∫_0^{Cn^{−2}}(n²r)^{−|α|}dr)^{1/2} ≤ Cε′_nn^{−1/2}τ^{−3/4};
on |ζ_s| ≥ 2 its square is ≤ C∫𝔪_n²e^{−2t/C}[(r/τ)^{1/2} + (τ/r)^{1/2}]dr/(r + τ)² = C∫𝔪_n²e^{−2t/C}(2t²/√y + 2√y)n²dt/(t² + y)²
≤ Cε′_n²n²y^{−3/2} = Cε′_n²n^{−1}τ^{−3/2}; the Δ₂ part is ≤ Cn^{−1}τ^{−1/4} and the Δ₃ part is O(n³e^{−n/C}τ^{−1/4}). So the
correction term is ≤ C(ε′_nn^{−1/2} + n^{−1})(ε′_nn^{−1/2}τ^{−3/4} + n^{−1}τ^{−1/4}) ≤ Cτ^{−1/4}(ε′_n + n^{−1}), since nτ^{1/2} = √y ≥ √y₀.

Summing, |(𝓡(z) − I)A₀(z)D_z| ≤ C(ε′_n + n^{−1})τ^{−1/4}. Finally Q(z) = 𝓡(z)Q̃(z) = [A₀D_z + (𝓡 − I)A₀D_z]Θ_∞(ζ_z), and
|A₀(z)D_z| ≤ Cτ^{−1/4}, |Θ_∞| ≤ C. ∎

*Why the row weighting is needed (Rule A).* The plain bound |𝓡(z) − I| is not small at the Bessel scale: the Bessel part of the
main term is ∫ε′_n·n|ζ_s|^{−|α|}|ds|/|s − z| ≍ ε′_n/(nτ) = ε′_nn/y (Paper 2's (eq:he-main-bound) integrated against
1/|s − z| instead of 1), which is small only for τ ≫ ε′_n/n. Right-multiplying by A₀(z)D_z, the scale of the comparison
solution at z, replaces n|ζ_s|^{−|α|} by √n|ζ_s|^{−|α|}·|ζ_z|^{1/4} and gains the factor y^{−1/2}. (With the plain bound,
the argument below still works for τ ≥ K₀/n, i.e. M ≤ c n^{1/p}, and Cor TB-C holds with the smaller exponent
(s − 1)/(2s(1 + 2/p) + 3); this is a fallback if the row computation is not accepted.)

### 3.3 The tail bound in the arcsine range, every p > 0, window

**Proposition TB-A (PROVED-mod-cite: Prop TB-Q; Lemmas ST, GS; Paper 2 prop:moments, (P2-g)).** Let p > 0 and
1 < s < 1 + 2p. There are C, c₁ > 0 and n₀ such that for n ≥ n₀, m ∈ {n − 1, n} and 1 ≤ M ≤ c₁n^{2/p},

  μ_m((Mn, ∞)) ≤ C·M^{−p/2}.

*Proof.* Take m = n first. By (P2-a), Q = C·U·k^{σ₃} in Ω_∞ (which contains z = τe^{5πi/6} for τ ≤ δ/4) and near ∞, so by
Lemma GS, S_n(z) = −Q₁₁(z)Q₁₂(z)/(Q₁)₁₂. By prop:moments and (P2-g), (Q₁)₁₂ = ic + O(1/n), so |(Q₁)₁₂| ≥ c/2 for n ≥ n₀. By
Prop TB-Q, |S_n(z)| ≤ (2/c)|Q(z)|² ≤ Cτ^{−1/2} for y₀n^{−2} ≤ τ ≤ δ/4, and Lemma ST gives ν_n([0, τ]) ≤ (8/√3)τ|S_n(z)| ≤ Cτ^{1/2}.
For δ/4 < τ ≤ 1, ν_n([0, τ]) ≤ 1 ≤ (4/δ)^{1/2}τ^{1/2}. Now μ_n((Mn, ∞)) = ν_n([0, M^{−p})) ≤ ν_n([0, τ]) with τ := M^{−p} ∈ (0, 1],
and τ ≥ y₀n^{−2} ⟺ M ≤ (n²/y₀)^{1/p} =: c₁n^{2/p}. For m = n − 1 apply this at degree n − 1 with M′ := Mn/(n − 1) ≥ M, for
M ≤ ½c₁n^{2/p} (then M′ ≤ c₁(n − 1)^{2/p} for n ≥ n₀): μ_{n−1}((Mn, ∞)) = μ_{n−1}((M′(n − 1), ∞)) ≤ CM′^{−p/2} ≤ CM^{−p/2};
so the statement holds with c₁ replaced by ½c₁. ∎

This is G1 §3.16 Theorem QLP(a) (range 1 ≤ M ≤ n^{2/p} up to a constant), now in Paper 2's frame, for every p > 0 in the
window. The lip mismatch enters only through ε′_n → 0; no rate is used. The same proof applies to σ_{p,s,ℓ₁} for every ℓ₁
satisfying (A_ϑ) (the constants then depend on ℓ₁); III does not need this.

### 3.4 One power for all M (what UL.md needs)

**Corollary TB-C (PROVED-mod-cite: Prop TB-A; G1 §3.4 Lemma TL).** Let p > 0, 1 < s < 1 + 2p, and

  ϑ_* = ϑ_*(p, s) := (s − 1)/(s(1 + 2/p) + 2)  (0 < ϑ_* < p/2; increasing in s).

There are C, n₀ with μ_m((Mn, ∞)) ≤ C·M^{−ϑ_*} for all n ≥ n₀, m ∈ {n − 1, n}, M ≥ 1. Consequently (N) of §1 holds at every
t ∈ (1, 1 + 2p) with ϑ(t) = ϑ_*(p, t), and sup_{n≥n₀}E_{μ_n^{(t)}}[(k/n)^u] ≤ 2 + Cu/(ϑ_* − u) for 0 < u < ϑ_*.

*Proof.* Put A := s(1 + 2/p) + 1, so ϑ_* = (s − 1)/(A + 1), and γ₁ := 1/ϑ_* = (A + 1)/(s − 1); note
s − 1 − ϑ_* = Aϑ_* and γ₁ > 1 + 2/p (as A + 1 > (1 + 2/p)(s − 1)). Also ϑ_* < (s − 1)/(s(1 + 2/p)) ≤ p(s − 1)/(s(p + 2)) < p/2.
Monotonicity: M ↦ μ_n((Mn, ∞)) is non-increasing. Take m = n.
- 1 ≤ M ≤ c₁n^{2/p}: Prop TB-A and M^{−p/2} ≤ M^{−ϑ_*}.
- c₁n^{2/p} ≤ M ≤ n^{γ₁}: μ_n((Mn, ∞)) ≤ μ_n((c₁n^{2/p}n, ∞)) ≤ Cc₁^{−p/2}n^{−1} = Cc₁^{−p/2}(n^{γ₁})^{−ϑ_*} ≤ C′M^{−ϑ_*}.
- M ≥ n^{γ₁}: Lemma TL (pure power, sandwich constants c = C = 1; n ≥ 2): for integer T ≥ T″,
  μ_n((T, ∞)) ≤ 1156·T″^sT^{1−s}/(s − 1), and T″ ≤ (8p + 2)n^{2+2/p} (UL.md §4 step 3). Take T := ⌊Mn⌋; then
  {k > Mn} ⊂ {k > T}, T ≥ Mn/2, and T ≥ T″ for n ≥ n₀ because γ₁ + 1 > 2 + 2/p. So
  μ_n((Mn, ∞)) ≤ C n^{(2+2/p)s}(Mn)^{1−s} = C n^{A}M^{−(s−1)} = C n^{A}M^{−Aϑ_*}M^{−ϑ_*} ≤ CM^{−ϑ_*}, since
  M^{Aϑ_*} ≥ n^{Aγ₁ϑ_*} = n^A.
For m = n − 1 use M′ = Mn/(n − 1) as before. The moment bound is Tonelli as in UL.md Thm UF. ∎

*Exponent values* (for orientation): p = ½: ϑ_* = 0.013, 0.053, 0.078 at s = 1.1, 1.5, 1.9; p = 1: 0.036, 0.125, 0.173 at
s = 1.2, 2, 2.8. Small, but UL.md needs only positivity and a positive lower bound on compacts.

### 3.5 p > 1, every s > 1: the classical module

**Proposition TB-P (PROVED-mod-cite: as G1 §3.16 Theorem QLP for p ≠ 1 — RH_px [REVIEWED] Lemmas 4.1–4.3 and §5 small norm;
KMVV (6.23), (6.28); DLMF 10.25.2, 10.32.4, 10.32.9 via Lemma BK; in the Q-frame of Paper 2 as set up in E_pgt1 §§0, 3, 6
[REVIEWED]).** Let p > 1 and s > 1. Theorem QLP (a)–(c) of G1 §3.16 holds: for n ≥ n₀, m ∈ {n − 1, n}: (a) μ_m((Mn, ∞)) ≤ CM^{−p/2}
for 1 ≤ M ≤ n^{2/p}; (b) ≤ Cn^{−1}(M/n^{2/p})^{−β}(1 + log(M/n^{2/p})) for M ≥ n^{2/p}, β = min(p, s − 1); (c) for every
ϑ < min(p/2, s − 1), ≤ C_ϑM^{−ϑ} for all M ≥ 1 (and ϑ = p/2 if s − 1 > p/2).

*Proof (a re-reading, not new mathematics).* G1 §3.16's proof for p ≠ 1 uses: (Z) the small-norm error matrix 𝒵 of RH_px at
z = τe^{5πi/6} satisfies |𝒵(z) − I| ≤ C/n for 0 < τ ≤ δ₁/2, which follows from ‖𝒵₋ − I‖_{L²} = O(1/n),
‖J_𝒵 − I‖_{L¹∩L²∩L^∞} = O(1/n) and the hard-edge mismatch |J_𝒵 − I| ≤ C_Kn^{−K}min(1, |s|^K) in U(0, δ) (RH_px Lemma 4.3);
(A) the prefactor A := P₀^∞ρ^{σ₃}Mf^{σ₃/4} (ρ := W̃/D_W, in the Q-frame) is bounded with bounded inverse on U(0, δ/2), uniformly
in n (maximum principle on |z| = δ; ρ² = e^{∓iπα}/ω with ω bounded above and below there); (GS), (ST), and Lemma BK for the
Bessel functions I_α, K_α at u = 2ζ^{1/2}, uniformly in the order. In the Q-frame these are: 𝒵 = R := QP̂₀^{−1} in U(0, δ),
the error matrix of E_pgt1 Prop E.5′, whose proof records ‖R₋ − I‖_{L²} = O(1/n), the jump O(n^{−K}min(1, |z|^K)) inside U(0, δ)
(RH_px Lemma 4.3) and the uniform Cauchy bound (Paper 2 F1), valid for every s > 1 (E_pgt1 §6 checks that F1, F5 and Lemma
szego (vi)(b)–(c) do not use α < 1); and P̂₀ = A(2πn)^{σ₃/2}σ₃Ψ_α(n²f)σ₃·(diagonal of determinant 1) (E_pgt1 §3: Ẽ_N
(2πζ^{1/2})^{−σ₃/2} = N W̃^{σ₃}M). The bound on ω on ∂U(0, δ) is Paper 2 Lemma szego (vi)(a), (c), α-independent by the same
check. With these identifications G1 §3.16's proof applies line by line. ∎

In Paper II this is the natural place for the full statement: the classical module (planned §8, from RH_px §§4–5) has a
super-small hard-edge mismatch, so the Stieltjes-point argument gives the optimal exponents.

### 3.6 The p ≤ 1 verdict and the remaining GAPs

- For p ≤ 1 the comparison frame proves (N) at every point of the window (Cor TB-C), which is all that Thm TS, Prop UP-w and
  Cor 1.5 need. The mismatch's lack of a rate is harmless because the estimate needed is O(1) relative to the comparison
  solution, not o(1/n): only ε′_n → 0 (indeed only boundedness of ε′_n) is used.
- **GAP TB-opt.** In Paper 2's frame, QLP(b) and the exponent min(p/2, s − 1) in (c) for p ≤ 1. Below the Bessel scale
  (|ζ_z| ≤ 2) the same row-weighted bound loses a factor |ζ_z|^{−|α|} (the Bessel part of the main term is
  ≍ ε′_n√n|ζ_z|^{−3|α|/2}, against row entries ≍ √n|ζ_z|^{±α/2}), so the row product is not controlled uniformly as ζ_z → 0;
  a finer (column-wise) analysis of the rank-one mismatch might close this, but it is not attempted. Not needed by III.
  (In the repo, QLP(b), (c) for p ≤ 1 are proved through RH₁(r) and RH_plt1b, G1 §3.16, REVIEWED; those frames are not in II.)
- **Outside the window for p ≤ 1** (s ≥ 1 + 2p): no tail bound in II's frame (the comparison frame needs |α| < 1, Paper 2
  rem:alpha-ge-1; the Christoffel step does not transfer tail bounds: μ_n^{xσ}(k) ≤ C(k/n)^p(μ_n^σ + μ_{n+1}^σ)(k) loses
  exactly the arcsine decay). By Thm TS this is not needed for the s-law; it is needed only for uniformity outside the window.
- **GAP UP-1+p** (§2).

## 4. Rule A (adversarial pass) — log

- *Lemma TS / Thm TS.* Boundary cases: s exactly 1 + jp gives r = 1 + p (in the window; m(s) = j − 1); s₀ = s₁ trivial; pairs on
  opposite sides of the window handled by antisymmetry. The constant ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) is additive — checked
  exactly (`check_tail.out` [2]: additivity defect ≤ 3·10⁻⁴⁰ at dps 40). Is UF-lim really confined to K″? Its proof uses (QLP-c)
  only at grid points t_i ∈ K″ and (CS) at a″ (no tail bound); Lemma W at those t_i. Yes. Does the identification φ′(0) = log c
  need a + p ∈ K? Yes in UL's proof; K″ provides it inside the window (b″ − a″ ≥ p). Converse/limits: telescoping does not give
  uniformity outside the window (stated).
- *Prop UP-w.* The transfer formula α_n(s) = g_n(s − p) + b_{n+1}(s − p)²/g_n(s − p) is lem:transfer(ii) (ã_n = u_n + l_{n+1})
  with σ = σ_{s−p}, xσ = σ_s; checked indices: l_{n+1} = b_{n+1}²/u_n. At s = 1 + p neither route closes (GAP), confirmed by
  listing both requirements.
- *Prop TB-Q.* (i) Which points of Σ̂ are near z: only the band (0, δ) and the lips in U(0, δ) (P2-b); the angular separation
  ≥ π/3 uses 5/4·θ_lip < θ_w < π/2 (eq:angles), valid for every p (for p < 1 the lips leave 0 at angle θ_lip ≤ πp/4 and the
  seams, at ±πp/2 < π/2, carry no jump, F1). (ii) Is z in Ω_∞, where (P2-a)'s formula Q = CUk^{σ₃} holds? The lens is {|arg z| < θ_w}-bounded
  near 0, and Ω^△ lies near (4c, n^p): yes. (iii) The right factor D_z is the *comparison* scale at z, not a free choice:
  Q̃(z) = A₀D_zΘ_∞ exactly for |ζ_z| ≥ 2 (eq:he-Phi-large holds in all sectors, including at arg ζ_z ≈ −π/6). (iv) Could
  B(s) = A₀(s)^{−1}A₀(z) spoil the conjugation (the factor n from (2πn)^{±σ₃/2})? This is the (2,1) entry: n|z||ζ_z|^{−1/4}
  ≍ |ζ_z|^{1/4}|z|^{1/2}, subdominant — checked. (v) α → ±1: ∫_0^C u^{−|α|}du blows up; s is fixed in the open window. α = 0:
  logs, integrable. (vi) The O(1/n) circle term: Q̃ bounded on both circles. (vii) The correction term needs the L² bound of
  (P2-e), which is stated inside the proof of prop:moments (not in its statement): the II author should promote it to the
  statement of the corresponding proposition.
- *Prop TB-A.* Sign/normalisation of S_n: Lemma GS is exact; ST is checked numerically (G1 check_qlp.out: ST bound ≥ tail in
  every row). (Q₁)₁₂ ≠ 0: = ic + O(1/n). Translation τ ↔ M: k > Mn ⟺ X_k < M^{−p}.
- *Cor TB-C.* γ₁ϑ_* = 1 exactly (so the middle range costs nothing beyond the constant); T ≥ T″ in the deep range; the exponent
  is strictly below p/2 and positive for s > 1; it is not optimal (the numerics suggest M^{−p/2} up to the Bessel scale and
  −(s − 1) beyond, G1 QLP4).
- *Prop TB-P.* Only a dictionary; the one point to re-check in II is that all Paper 2 inputs used are α-independent (E_pgt1 §6
  did this check for F1, F5, Lemma szego).

## 5. Checks

`checks/check_tail.py` (.out), NUMERICAL (finite checks of proved statements; Rule N: not certified). Runtime ≈ 3 min; needs
`make -C csrc` for part [2].
- [1] Prop TB-Q/TB-A/Cor TB-C conclusions in the window, float64 Lanczos (method of G1 check_qlp.py, K ≥ 8n^{1+2/p}):
  R_S := sup_{2/n² ≤ τ ≤ 1/2}τ^{1/2}|S_n(τe^{5πi/6})| (the proof bounds it by C|Q|² τ^{1/2} ≤ C) = 0.70–0.83 in all 18 runs
  (p = ½: n = 4, 6, 8, s = 1.1, 1.5, 1.9; p = 1: n = 8, 16, 32, s = 1.2, 2.0, 2.8; α from −0.8 to 0.8), flat in n;
  R_A := sup_{M ≤ n^{2/p}/2}μ_n((Mn, ∞))M^{p/2} = 0.50–0.68; R_C := sup_M μ_n((Mn, ∞))M^{ϑ_*} = 0.48–0.62. Limits: small n,
  lumped tail mass up to 6% at p = ½, s = 1.1.
- [2] Thm TS at p = ½ (window (1, 2)), binary128 RKPW + Gauss–Jacobi tail (SECOND's so_coeffs), n = 25, 50, 100, 200:
  Γ_n(s₀, s₁) for a window pair, s₁ outside, both outside, three Christoffel steps, and single steps (s, s + p) inside and
  outside: all decrease like 1/n (e.g. (1.25, 3.0): 4.4·10⁻², 2.4·10⁻², 1.2·10⁻², 6.4·10⁻³); K → 2K changes ≤ 1.5·10⁻¹⁰.
  (UL.md's check_ul [4] covered p ∈ {1, 2} only.)

## 6. Integration for the authors of Papers II and III

**Into Paper II (decision D2(a)).** One proposition, two parts, placed after both frames are available (end of §8 of
`PAPER_II_OUTLINE.md`), with the two elementary lemmas before it:

> **Lemma 8.5′ (a Stieltjes bound).** If ν is a probability measure on [0, ∞), τ > 0 and z = τe^{5πi/6}, then
> ν([0, τ]) ≤ (8/√3)τ|∫dν(X)/(X − z)|.
>
> **Lemma 8.5″ (row product).** With U as in (eq:U) and ν_n the image of μ_n := w_kP_n(x_k)²/h_n under k ↦ (n/k)^p: if
> Q = CUk^{σ₃} near a point z and near ∞, C constant diagonal, k scalar, Q = I + Q₁/z + …, then
> ∫dν_n(X)/(X − z) = −Q₁₁(z)Q₁₂(z)/(Q₁)₁₂. (Cite Teschl, *Jacobi Operators*, (1.99)–(1.100), (2.122), after reading it.)
>
> **Proposition 8.6 (hard-edge localisation of the spectral weights, pure powers).** Let p > 0, s > 1, μ_n(k) :=
> k^{−s}P_n(k^{−p})²/h_n for σ_{p,s}. Assume either (a) 1 < s < 1 + 2p, or (b) p > 1. There are C, c₁ > 0 and n₀ such that for
> n ≥ n₀, m ∈ {n − 1, n} and 1 ≤ M ≤ c₁n^{2/p}: Σ_{k>Mn}μ_m(k) ≤ C·M^{−p/2}. In case (b) moreover, for every
> 0 < ϑ < min(p/2, s − 1), Σ_{k>Mn}μ_m(k) ≤ C_ϑM^{−ϑ} for all M ≥ 1.
>
> *Proof sketch.* Lemma 8.5″ applies at z = τe^{5πi/6} because Q = CUk^{σ₃} in Ω_∞ (eq:VM, eq:Q), and (Q₁)₁₂ = ic + O(1/n)
> (Prop 6.6 in case (a), Prop 8.4 in case (b), and the expansion of P₀^∞). By Lemma 8.5′ it suffices to show |Q(z)| ≤ Cτ^{−1/4} for y₀n^{−2} ≤ τ ≤ δ/4.
> (a) Write Q = 𝓡Q̃ with the comparison solution Q̃ of §6, so that 𝓡 − I = 𝒞(Q₋(v − ṽ)ṽ^{−1}Q̃₋^{−1}) (T3(b)), and
> Q̃(z) = A₀D_zΘ_∞(ζ_z), D_z = (2πn)^{σ₃/2}ζ_z^{−σ₃/4} (Lemma 6.2, (eq:he-Phi-large)). Bound (𝓡(z) − I)A₀(z)D_z by splitting
> the jump difference as in the proof of Prop 6.6: the lip mismatch d_ne₂e₁ᵀ (Lemma 6.3), conjugated by Q̃(s) on the left and
> by Q̃(s)^{−1}A₀(z)D_z on the right, is O(ε′_n)τ^{−1/4} after integration against |ds|/|s − z| (Bessel localisation
> (eq:he-localisation) and |ζ_s|^{−|α|} integrable, |α| < 1); the circle terms are O(n^{−1})τ^{−1/4}; the term with
> Q₋ − Q̃₋ is bounded by Cauchy–Schwarz with ‖Q₋ − Q̃₋‖_{L²} ≤ C(ε′_nn^{−1/2} + n^{−1}) (proof of Prop 6.6 — state it in
> Prop 6.6). (b) In §8's frame the error matrix R = QP̂₀^{−1} has a super-small hard-edge jump (Lemma 8.3) and
> ‖R₋ − I‖_{L²} = O(1/n) (Prop 8.4), so |R(z) − I| ≤ C/n on the ray for all τ ≤ δ/2, and the row of P̂₀(z) is bounded by the
> Bessel functions I_α, K_α at u = 2ζ_z^{1/2} uniformly (DLMF 10.25.2, 10.32.4, 10.32.9); this gives the arcsine range and,
> below the Bessel scale, n^{−1}(M/n^{2/p})^{−min(p, s−1)} up to a logarithm, hence the all-M statement.
> *Source:* research/G1/RH/second_order/TAIL.md (Props TB-Q, TB-A, TB-P); G1 PROOF.md §3.16.

Length: about 2.5 pp (a: 1.5 pp; b: 1 pp, mostly the Bessel bound). Labels after writing: PROVED-mod-cite, inputs as in
the table above; needs Rule R in its II form (new writing).

**Into Paper III.**
- §2.5 imports: [II, Prop 8.6] as above (restate: the arcsine-range bound in the window for all p, all M for p > 1).
- New Lemma 6.0 (one power for all M; = Cor TB-C): from [II, Prop 8.6] and Lemma 2.10 (= G1 Lemma TL): μ_m((Mn, ∞)) ≤
  CM^{−ϑ_*} for all M ≥ 1, ϑ_* = (s − 1)/(s(1 + 2/p) + 2), 1 < s < 1 + 2p; for p > 1 and every s > 1 directly from [II, 8.6(b)].
  Consequence: **Lemma 2.10 (TL) must be kept in III** (it is also used by Prop 6.7 / Thm UΛ). Decision D5 then applies to
  TL's Markov/Chebyshev inputs: cite a source with theorem numbers after reading it.
- Lemma 6.2–6.5: use Lemma 6.0 wherever UL.md says (QLP-c); Lemma 6.4 (= Lemma W) with the hypothesis pa < ϑ_*(p, t); the
  grid step of Prop 6.3 (= Thm UF) is u₀ = ½ϑ_*(p, a).
- Lemma 6.6 (telescoping; new) = Lemma TS + Thm TS(b) of §2, with the window enlargement K″ of Thm TS(a) for the constant.
- Theorem 1.4 as it can be stated:
  (ii) for every p > 0 and all s₀, s₁ > 1, with uniformity on compacts of (1, 1 + 2p), and on compacts of (1, ∞) if p > 1;
  (iii) for p > 1 on every compact K ⊂ (1, ∞); for 0 < p ≤ 1: the b-part on every compact K ⊂ (1, 1 + 2p), the a-part on every
  compact K ⊂ (1, 1 + 2p) ∖ {1 + p} (Prop UP-w). Either state (iii) in this form, or state only the b-part for p ≤ 1 and put
  the a-part near s = 1 + p among the open questions of §8 (GAP UP-1+p).
- Corollary 1.5 (p = 1): holds for **every** s > 1 (anchor s₀ = 3/2 in the window (1, 3); Thm TS(b) for the pair (3/2, s)). The
  fallback "only s ∈ 3/2 + ℕ₀" of D2(b) is not needed.
- Prop 6.7 (o(log n) log-moment, optional): for p ≤ 1 only on compacts avoiding 1 + p (it uses the uniform a-part).
- The abstract sentence "gives the law uniformly on compact sets of s" should say "on compact subsets of (1, 1 + 2p)" (and
  the a-part caveat for p ≤ 1), or be limited to the b-law.

**Not changed by this file:** SECOND.md, UL.md, THEOREMS.md, papers/. If the coordinator integrates: UL.md's (QLP-c) input
line can point to Cor TB-C / Prop TB-P as II-frame proofs; THEOREMS.md §2.10 can add rows for Thm TS (s-law for all pairs
with window-only localisation), Prop UP-w and GAP UP-1+p, and Prop TB-A/TB-C/TB-P (not REVIEWED).
