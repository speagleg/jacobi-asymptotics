# JZC W, κ-family for 0 < p < 1: the n-dependent constrained equilibrium g_κ, its sign conditions, the frame, and a test

Status (2026-10-22): **NOT REVIEWED** (no Rule R reader; every label below is the author's, pending Rule R). Labels per
VERIFICATION_POLICY.md. Novelty: UNCHECKED (no Rule L pass). No claim about RH: no measure built from zeta zeros is used.
Inputs, with their labels: JZC_M1 Theorem Q (i)–(iii) (PROVED, elementary; Rule R: two readers, REVIEW_JZC_M1_A.md and REVIEW_JZC_M1_B.md, REVIEWED — updated 2026-10-23; **not REVIEWED** —
the brief called it reviewed; only (iv), which is not used here, needs the unquoted Saff–Totik input); JZC_W_kappa L K.1, P K.14 (REVIEWED);
JZC_W_outer L W-out.0, W-out.2, W-out.5 (REVIEWED); JZC_M3a_H_G3 Lemma 3, Prop 4, Cor 5, JZC_M3a_H_G23plt1 (P2.6, F.1_δ), JZC_M3a_H_G1u_plt1
(L P1–P5, Prop G1u′) (all REVIEWED); Paper 2 sec_5 (Lemma g-function, Lemma signs, Lemma lips, (O1)–(O5), Lemma jumpsV) and app_outer
(K = (4c − z)^{−1/2}), read for this note (read-only). External theorems: none beyond those quoted in the cited notes (Rule C).
Checks: `checks/w_plt1_equilibrium.py/.out` (§2–§3), `checks/w_plt1_predict.py/.out` and `checks/w_plt1_test.py/.out` (§5); caches in
`tmp/w_plt1_cache/` (gitignored).

| # | Statement | Label |
|---|---|---|
| Prop 1 | the κ-node constraint σ_ε (ε := κ/n^p) and its soft-edge function in closed form, F(b) = (4c)^{1/p}b^{−1/p}(1 − εb)^{1/p−1/2}; unique edge **a_ε = 4c(1 − εa_ε)^{1−p/2}**, both signs of κ; A(ε) := a_ε/4c = Σ_k((−1)^k/(k+1))binom((k+1)(1−p/2), k)(4cε)^k; its κ¹ term is W's κ-law pole term exactly, its κ^k terms (k ≥ 2) are **not** W's first-order pole terms | PROVED (elementary) + NUMERICAL |
| Prop 2 | the variational / sign conditions of g_κ: (i) 0 < ν_ε < σ_ε on the band, (ii) strict outer inequality on the saturated set, (iii)–(vi) Paper 2 Lemma signs (i)–(iv) for g_κ with ε-analytic local maps f_ε, f_{r,ε}; κ > 0: every n ≥ 1; κ < 0: (i), (ii), (iv) on S₊ every n, (iii), (v), (iv) on the negative axis for n ≥ n₀(p, κ); for κ < 0 positivity of ν_ε fails beyond ε = κn^{−p} = ε_c(p) ≈ −0.70 (p = 0.6), i.e. only possibly at n = 1 | PROVED-mod-cite (JZC_M1 Thm Q (i)–(iii) [one reader]; Paper 2 Lemma g-function, Lemma signs (proofs)) + NUMERICAL |
| Lemma 3 | the branch rule: g_κ := G_w∘ζ + log(1 − εz) (G_w the w-plane log transform of ζ_*μ_ε) has e^{n(g₊−g₋)} = e^{2iθ_κ} on the whole saturated set, = 1 on (−∞, 0)∖supp; the principal-branch potential of the same measure (κ < 0) misses by the constant phase e^{−2πi\|κ\|^{1/p}} on ℝ∖[0, a_ε] | PROVED (elementary) + NUMERICAL |
| Prop 3 | the frame for g_κ: F♮_κ := F♮_δ∘ζ (G3's α-frame scalar, K at a_w := ζ(a_ε)) satisfies (O1) with θ_κ, (O2), is regular at z_* and normalisable at ∞; band weight 𝗐_nz^{α+2δ}(a_ε − z)H^♭_κ with H^♭_κ = const·H_n^δ(ζ(z))(1 − εz)^{1/p−2a} = L K.1's H_n^κ **without** the branched gauge factor; lip entries carry only e^{±2πiδ} (exact α-frame lip match, no ρ₁); Toda times = W's (2Z_κ(−j)/j − B_j)n^{−jp} exactly; hard edge: Bessel order α in n²f_ε, f_ε = f + O(ε) | (i)–(iii) PROVED-mod-cite (G3 Prop 4, Cor 5; L K.1; algebra); (iv) PROOF SKETCH (estimates "verbatim with uniform constants", not written line by line) |
| Sketch 4 | reduction: n^pb_n/c = 𝔅_n[𝔐_ε(α + 2δ, α); μ^κ_n] + o, 𝔐_ε := the decoupled model M(α + 2δ, α) on g_κ; double series Σ_kD_k(ε)n^{−k}, D₀ = A(ε), D_k(0) = M(α + 2δ, α)'s d_k; κ enters through A(ε) (all orders), the Toda times, and ε-dressed parametrix data | PROOF SKETCH (the steps not written: a-priori bound (G23plt1 P2.6 with ζ), N.6a–c uniform in ε, the hard-edge comparison with f_ε); no step found that is as hard as an open problem |
| Conj W_<1 | for 0 < p < 1, 1/p ∉ ℕ: n^pb_n/c = A(κ/n^p) + [𝔅_n[M(α+2δ, α); t] − 1] + (W's natural-index shifts of the pole terms) + O(n^{−1−2p}); in particular the n^{−1} coefficient is κ-free, every pure power n^{−mp} has coefficient [x^m]A·(4cκ)^m, and the n^{−1−p} coefficient is W's | CONJECTURE (NUMERICAL: §5, pre-registered) |
| §5 | 6 measures + 1 truncation control, predictions written before the measures (Rule X) | NUMERICAL |

## 0. Answer

The construction goes through; no sign condition fails asymptotically; the numerical test passes at every pre-registered coefficient.
1. **g_κ** is the equilibrium measure (no external field) with upper constraint the κ-node density σ_ε = (1/n)\|t_κ′\|, ε = κn^{−p}, taken over
   **all** phantom indices t_κ ∈ (0, ∞). Its edge is explicit: **a_ε = 4c(1 − εa_ε)^{1−p/2}** (Prop 1), so c_κ(n) := a_ε/4 = c·A(κn^{−p}) with
   A = 1 − (2 − p)·2cκn^{−p} + O(n^{−2p}) and all Taylor coefficients in closed form (Lagrange inversion). For κ > 0 this is JZC_M1 Theorem Q
   verbatim (its (H1)–(H3) hold for every n); for κ < 0 the saturated set has a second piece (−∞, −n^p/\|κ\|) carrying the phantom indices
   t_κ ∈ (0, \|κ\|^{1/p}) — dropping it (Theorem Q on (0, ∞)) gives the wrong g: a constant phase defect e^{−2πi\|κ\|^{1/p}} (Lemma 3) and a
   κ-dependent n^{−1} term −p\|κ\|^{1/p}, which the data exclude by 123–937 tolerances.
2. **Sign conditions** (Prop 2): 0 < ν_ε < σ_ε on the band, the strict outer inequality on the saturated set, Re φ_ε < 0 off the band,
   ∂_yRe φ̃_ε = π(σ_ε − ν_ε) > 0, and nondegenerate square-root/x^{−1/2} edges with ε-analytic local maps — Paper 2's Lemma signs (i)–(iv) for g_κ.
   κ > 0: all n. κ < 0: n ≥ n₀; positivity of ν_ε genuinely fails for κn^{−p} < ε_c(p) (≈ −0.70 at p = 0.6), which for admissible κ can only
   happen at n = 1.
3. **The frame** (Prop 3): with g_κ, the scalar is the Hurwitz α-frame scalar of G3 composed with the Möbius map ζ (K moved to a_w = ζ(a_ε)); it
   satisfies (O1) with the κ-node phase θ_κ, is regular at z_* and normalisable at ∞; the band weight is 𝗐_nz^{α+2δ}(a_ε − z)H^♭_κ with
   H^♭_κ = L K.1's H_n^κ **minus the branched gauge factor** — the P K.14 obstruction (lip phase e^{±2πiρ₁}, \|ρ₁\| ≍ n^{e(p)}) is gone, the lip
   match is the exact α-frame one, the Bessel order is α, the Szegő exponent β′ = α + 2δ (κ-free), and the Toda times are exactly W's. The
   remaining analytic estimates (a-priori bound, the comparison with n²f_ε, N.6a–c uniformly in ε) are re-runs of REVIEWED proofs with one extra
   analytic parameter ε → 0: written as a PROOF SKETCH (Sketch 4), not as a proof.
4. **How κ enters:** through A(κn^{−p}) **to all orders** (pure powers n^{−mp}), through the Toda times (n^{−1−jp}), and through ε-dressed edge
   data (n^{−k−mp}, k ≥ 1; at first order W's natural-index shift). New relative to W: for p < 1, W's first-order pole coefficient is correct at
   n^{−p} but **incomplete at n^{−2p}, n^{−3p}, …** (where second- and higher-order terms of the same pole land: 2 + 2pq₁ = 2p); A(ε) supplies them.
5. **Numerics** (§5; predictions written 16:12:42, every measure generated after it): p = 0.6, 0.75, δ = −0.3, s = 2, κ ∈ {0, ±0.5}, plus odd/even
   combinations and a K → 2K truncation control: **48/48 checks pass**; the κ-free n^{−1} holds to ≤ 4·10⁻⁵ (tolerances 1.4·10⁻⁴–3.6·10⁻³); the
   second-order coefficient at n^{−2p} agrees to 2·10⁻⁶–8·10⁻⁵ while W's first-order value is excluded by 28–502 tolerances; the n^{−3p}
   coefficient agrees (W first order excluded by 7–15 tol); the n^{−1−p} coefficient (W's natural-index shift + κ-dependent t₁) agrees, with the
   shift necessary (18–329 tol) and the gauge-share/density pieces of t₁ only weakly resolved at p = 0.6 (2–12 tol), strongly at p = 0.75, κ < 0
   (60–72 tol).

## 1. Setting and notation

**Setting (S<).** 0 < p < 1 with 1/p ∉ ℕ; −1 < δ ≤ 0, a := 1 + δ; κ ≠ 0, κ > −a^p; 1 < s < 1 + 2p, α := (s − 1 − p)/p ∈ (−1, 1), β′ := α + 2δ.
λ_k := (k + δ)^p + κ, σ^{δ,κ} := Σ_kλ_k^{−s/p}δ_{1/λ_k}. n^p frame: X_k := n^p/λ_k. c = c(p) (Paper 2), 4c = the lattice edge (JZC_M1 Cor Q.1:
(4c)^{−1/p}·(1/p)B(1/p, ½) = 1).
- ε := κ/n^p; z_* := 1/ε = n^p/κ (JZC_W_kappa's z_*); for κ < 0, z′ := 1/|ε| = −z_*.
- ζ(z) := z/(1 − εz) (JZC_W_kappa's ζ; a real Möbius map with ζ′ = (1 − εz)^{−2} > 0 on ℝ∖{z_*}, so ζ(ℂ_±) = ℂ_±).
- t(w) := nw^{−1/p} (lattice index, principal), t_κ(z) := n(1/z − ε)^{1/p} = t(ζ(z)): t_κ(X_k) = k + δ. θ_κ := πt_κ.
- The **κ-node constraint** (the node counting density at scale n^p, per n nodes):
  σ_ε(y) := (1/n)\|t_κ′(y)\| = (1/p)y^{−2}(1/y − ε)^{1/p−1} on Ŝ_ε := {y ≠ 0 : 1/y > ε},
  i.e. Ŝ_ε = (0, z_*) for κ > 0 and Ŝ_ε = (0, ∞) ∪ (−∞, −z′) for κ < 0. In the index variable, Ŝ_ε is t_κ ∈ (0, ∞): it is the image of the
  lattice's (0, ∞) (t ∈ (0, ∞)) under ζ^{−1}, phantom indices t ∈ (0, a) included exactly as Paper 2 includes them for the lattice. For κ < 0
  the phantom indices t_κ ∈ (0, γ), **γ := \|κ\|^{1/p}**, sit on the negative piece (−∞, −z′) (through z = ∞, where t_κ = γ).
- The w-plane: w := ζ(z) maps Ŝ_ε onto (0, ∞) and σ_ε dy onto the lattice density (1/p)w^{−1/p−1}dw; z = ∞ ↦ w = −z_*.

## 2. The κ-node equilibrium (Prop 1, Prop 2)

### 2.1 The edge in closed form

**Proposition 1.** Assume (S<) (only 0 < p and 1/p ∉ ℕ are used in (i)–(iii)). For b > 0 with εb < 1 put
S_b := Ŝ_ε ∖ [0, b] and F(b) := ∫_{S_b}σ_ε(y)(1 − b/y)^{−1/2}dy (the soft-edge function (Q) of JZC_M1, with the negative piece included
when κ < 0).
(i) F(b) = (4c)^{1/p}b^{−1/p}(1 − εb)^{1/p−1/2}.
(ii) F(a) = 1 has exactly one root a = a_ε in {b > 0 : εb < 1}; it is the unique solution of **a_ε = 4c(1 − εa_ε)^{1−p/2}**.
(iii) A(ε) := a_ε/(4c) is real-analytic at ε = 0 and, with x := 4cε and γ_p := 1 − p/2,
  A = Σ_{k≥0}((−1)^k/(k+1))·binom((k+1)γ_p, k)·x^k = 1 − (1 − p/2)x + ½γ_p(3γ_p − 1)x² − …,
so c_κ(n) := a_ε/4 = c·A(κn^{−p}) = c − (2 − p)·2c²κn^{−p} + O(n^{−2p}).
(iv) The x¹ term equals W's κ-law pole term: (−(1 − p/2)·4cκ)·n^{−p} = pR_{q₁}W(q₁)π cot(πq₁)n^{−1−pq₁}, q₁ = 1 − 1/p,
R_{q₁} = −q₁κ/p (L W-out.0). For k ≥ 2 the coefficient [x^k]A(4cκ)^k of n^{−kp} = n^{−1−pq_k} is **not** W's first-order term
pR_{q_k}W(q_k)π cot(πq_k): the difference is the second- and higher-order part of the soft-edge root (Prop M1.2's O(nη²)); e.g. at
p = 0.6 the κ² coefficient is 1.136086 against W's 0.172134 (`w_plt1_predict.out`).
*Proof.* (i) Put u = 1/y. For y ∈ S_b, u ranges over (ε, 1/b) (for κ < 0: u ∈ (ε, 0) is the negative piece, u ∈ (0, 1/b) the positive
part; u = 0 is the point y = ∞, of measure zero), σ_ε(y)dy = (1/p)(u − ε)^{1/p−1}du and 1 − b/y = 1 − bu. With v = u − ε ∈ (0, 1/b − ε) and
v = ((1 − εb)/b)w:
  F(b) = (1/p)∫_0^{1/b−ε}v^{1/p−1}(1 − εb − bv)^{−1/2}dv = (1/p)((1 − εb)/b)^{1/p}(1 − εb)^{−1/2}B(1/p, ½),
and (1/p)B(1/p, ½) = (4c)^{1/p} (Cor Q.1). (ii) F(a) = 1 ⇔ (a/4c)^{1/p} = (1 − εa)^{1/p−1/2} ⇔ a = 4c(1 − εa)^{1−p/2}. Uniqueness: d log F/d log b =
−1/p − (1/p − ½)εb/(1 − εb). For ε > 0 both terms are negative on (0, 1/ε); for ε < 0, \|ε\|b/(1 + \|ε\|b) < 1, so the derivative is
< −1/p + 1/p − ½ < 0. F → ∞ at b → 0, and F → 0 as b → 1/ε (ε > 0) resp. b → ∞ (ε < 0: F ~ C b^{−1/2}). (iii) B := xA satisfies
B = x(1 − B)^{γ_p}; Lagrange inversion gives B = Σ_{m≥1}(x^m/m)[u^{m−1}](1 − u)^{mγ_p} = Σ_m(x^m/m)(−1)^{m−1}binom(mγ_p, m − 1), and
A = B/x. Analyticity: implicit function theorem at (x, A) = (0, 1) (∂_A(A − (1 − xA)^{γ_p}) = 1 there). (iv) With y := 1/p:
W(q₁)π cot(πq₁) = (4c)^{1−y}Γ(3/2 − y)(−π cot(πy))/(√πΓ(2 − y)); (4c)^{−y} = pΓ(y + ½)/(√πΓ(y)) (Cor Q.1); Γ(2 − y) = q₁Γ(1 − y);
Γ(y)Γ(1 − y) = π/sin(πy); Γ(y + ½)Γ(3/2 − y) = (y − ½)π/sin(π(y − ½)) = −(y − ½)π/cos(πy). Hence
pR_{q₁}W(q₁)π cot(πq₁) = −q₁κ·W(q₁)π cot(πq₁) = −4cκ·pΓ(y + ½)Γ(3/2 − y)cos(πy)/π = −4cκ·p(y − ½) = −(1 − p/2)·4cκ. For k ≥ 2 the
inequality is the computed numbers. ∎
(PROVED (elementary). NUMERICAL: w_plt1_equilibrium [A] (closed form vs the quadrature root of F = 1 in the y-variable, 8 (p, ε) incl. p = 0.4;
control: Theorem Q verbatim on (0, ∞) for κ < 0, see Lemma 3), w_plt1_predict (series vs root; the k = 1 identity to 10⁻²⁵).)

*Remark (w-plane).* The w-plane edge is a_w := ζ(a_ε) = a_ε/(1 − εa_ε) = 4c(1 − εa_ε)^{−p/2} ([H]). In w the κ-problem is the lattice
constraint with the external field log\|1 + εw\| (Möbius: log\|z − z′\| = log\|w − w′\| − log\|1 + εw\| − log\|1 + εw′\|; this is SPEC Prop M's
weight (1 + κy)^{−2(m−1)} at the level of potentials). We work in z, where there is no external field and Theorem Q applies.

### 2.2 The equilibrium measure and its sign conditions

Let a := a_ε, S := S_a (the saturated set: (a, z_*) for κ > 0; (a, ∞) ∪ (−∞, −z′) for κ < 0; write S₊ := S ∩ (0, ∞), S₋ := S ∩ (−∞, 0)),
s(y) := σ_ε(y)(y/(y − a))^{1/2} (> 0 on S), g_σ(y) := y^{1/2}σ_ε(y) (y > 0), and
  T(x) := ∫_S s(y)dy/(y − x),   ν_ε(x) := (1/π)((a − x)/x)^{1/2}T(x)   (0 < x < a),   μ_ε := ν_εdx|_{[0,a]} + σ_εdy|_S.

**Proposition 2.** Assume (S<).
(i) μ_ε has unit mass; its Cauchy transform is G(z) = ((z − a)/z)^{1/2}∫_S s(y)dy/(z − y) (principal branch), so U^*(x) := ∫log\|x − y\|dμ_ε(y)
  is constant (=: ℓ_ε) on [0, a], and ν_ε also equals [1 − ∫_Sσ_εR(y)dy/(y − x)]/(π(x(a − x))^{1/2}), R(y) := sign(y)(y(y − a))^{1/2}.
(ii) **ν_ε < σ_ε on (0, a)**, for every ε (both signs).
(iii) **ν_ε > 0 on (0, a)**: for κ > 0 and every n ≥ 1; for κ < 0 whenever \|ε\| ≤ ε₀(p) (i.e. n ≥ n₀(p, κ)). This is sharp in kind:
  for κ < 0 positivity **fails** beyond a threshold ε_c(p) < 0, where the hard-edge constant C_ε changes sign (the negative piece's pull
  T₋(0) < 0 beats T₊(0)); numerically ε_c = −0.7741, −0.6952, −0.6458 at p = 0.4, 0.6, 0.75 ([I′]). Since \|κ\| < a^p ≤ 1, this can only
  happen for n^p < \|κ\|/\|ε_c\| < 1.6, i.e. at n = 1 (and nowhere for \|κ\| < \|ε_c\|): irrelevant for the asymptotics, but it shows that
  the n ≥ n₀ in (iii) is not an artefact of the proof.
(iv) **Outer inequality**: H(z) := PV∫_S s(y)dy/(z − y) > 0 on S₊, hence U^* is strictly increasing on [a, sup S₊) and U^* > ℓ_ε there; for κ < 0
  also U^* > ℓ_ε on (−∞, 0) (for n ≥ n₀), and on the negative piece itself.
(v) **Re φ_ε < 0 on ℂ∖[0, a]**, φ_ε := ℓ_ε − g with Re g(z) = ∫log\|z − y\|dμ_ε(y) (Paper 2 Lemma signs (i) for g_κ); and
  ∂_y Re φ̃_ε(x + iy)\|_{y=0+} = π(σ_ε − ν_ε)(x) > 0 on (0, a), φ̃_ε := φ_ε ± iθ_κ/n in ℂ_± (Lemma signs (ii)).
(vi) **Edges.** μ_ε((0, x]) = x^{1/2}𝔞_ε(x) with 𝔞_ε analytic near 0, 𝔞_ε(0) = 2C_ε, C_ε := a^{1/2}T(0)/π > 0; f_ε := −(π²/4)z𝔞_ε(z)² is
  analytic and univalent near 0 with f_ε′(0) < 0 (Lemma signs (iii)). Near a: σ_ε − ν_ε = (a − x)^{1/2}𝔟_ε(x) with 𝔟_ε analytic near a and
  𝔟_ε(a) = −h(a)/(πa^{1/2}) > 0, where
  h(a) = ∫_{S₊}(g_σ(y) − g_σ(a))(y − a)^{−3/2}dy − 2g_σ(a)(z_* − a)^{−1/2}·[κ > 0] + ∫_{S₋}s(y)dy/(y − a)   (each term < 0)
  (Lemma signs (iv)). All of 𝔞_ε, 𝔟_ε, a_ε, ℓ_ε depend real-analytically on ε near 0, uniformly on fixed discs.
*Proof.* **κ > 0.** σ_ε satisfies JZC_M1's (H1)–(H3) on (0, Y], Y := z_* < ∞: σ_ε is positive and real-analytic on (0, Y); with u = 1/y,
yσ_ε(y) = (1/p)u(u − ε)^{1/p−1}, and d/du[u(u − ε)^{1/p−1}] = (u − ε)^{1/p−2}(u/p − ε) > 0 for u > ε (as 1/p > 1), so yσ_ε is strictly
decreasing in y ((H2)); (H3) is void (Y < ∞). So Theorem Q (i)–(iii) applies verbatim: its root is our a_ε (Prop 1, (Q) = F(a) = 1), its ν and
balayage form are (i), 0 < ν < σ is (ii)–(iii), and its (iii) (via H > 0, including the finite-Y PV term
(z − a)^{−1/2}log[((Y − a)^{1/2} + (z − a)^{1/2})/((Y − a)^{1/2} − (z − a)^{1/2})] > 0) is (iv). Theorem Q (i)–(iii) uses no external input.
**κ < 0.** The proof of Theorem Q (ii)–(iii) goes through with S₋ added, as follows. (i) G̃(z) := ((z − a)/z)^{1/2}∫_S s/(z − y) has the jumps
−2πiσ_ε on S₊ and on S₋ (on S₋, (z − a)/z > 0, so the root is analytic there and only the Cauchy integral jumps, by −2πis·((y − a)/y)^{1/2} =
−2πiσ_ε), −2πiν_ε on (0, a), none elsewhere; it is o(1/\|z − z₀\|) at z₀ ∈ {0, a, −z′} and G̃ = F(a)/z + O(z^{−2}) = 1/z + O(z^{−2}) at ∞ (both
pieces of S are integrable against s, s = O(y^{−2}) at ±∞). G := ∫dμ_ε/(z − y) has the same jumps and endpoint behaviour; G − G̃ is entire and
→ 0: G = G̃ (Liouville). *[Note 2026-10-23 (REVIEW_JZC_M1_B B2, §5): for Y = ∞ this Liouville step is incomplete as written — "→ 0 at ∞" is not uniform near the unbounded support, and Morera across the support needs Plemelj–Privalov, NOT QUOTED. It is closed by the per-point balayage argument now in JZC_M1 §2 (ii) (k_y, ρ_y and Fubini; k_y is still analytic off [0, a] with S₋ on the negative axis), or by the |Im z|-bound lemma of REVIEW_JZC_M1_B B2. Not yet rewritten here; κ > 0 (Y < ∞) is unaffected.]* So μ_ε has mass 1, Re G = 0 on (0, a) (U^* constant), and the balayage form follows from R(y)σ_ε(y) = s(y)(y − a) on
both pieces (R < 0 on S₋, where y − a < 0) exactly as in Theorem Q (ii). (ii) g_σ(y) = (1/p)u^{3/2}(u − ε)^{1/p−1} (u = 1/y > 0) is increasing in
u, so g_σ is strictly decreasing on (0, ∞) (both signs of ε). On S₋, y − x < 0 and s > 0, so the S₋-part of T is negative, and
  ν_ε(x) < (1/π)((a − x)/x)^{1/2}∫_a^∞g_σ(y)(y − a)^{−1/2}dy/(y − x) < g_σ(a)/x^{1/2} ≤ g_σ(x)/x^{1/2} = σ_ε(x)
(∫_a^∞(y − a)^{−1/2}(y − x)^{−1}dy = π(a − x)^{−1/2}; Theorem Q's argument). (iii) T(x) ≥ T₊(0) − \|T₋\|(x), T₊(0) := ∫_{S₊}s(y)dy/y > 0, and
\|T₋(x)\| ≤ ∫_{S₋}s(y)dy/\|y\| ≤ z′^{−1}∫_{S₋}σ_ε = \|ε\|^{1+1/p} (s ≤ σ_ε on S₋, and ∫_{S₋}σ_ε = (t_κ(−∞) − t_κ(−z′))/n = γ/n = \|ε\|^{1/p}). T₊(0) is continuous in ε at 0 (dominated convergence in
the u-representation T₊(0) = ∫_0^{1/a}(1/p)(u − ε)^{1/p−1}(1 − au)^{−1/2}du, u = 1/y) with T₊(0)\|_{ε=0} = πC₀/(4c)^{1/2} > 0 (Paper 2's
𝔞(0) > 0). So T > 0 on (0, a) for \|ε\| ≤ ε₀(p). (iv) H = H₊ + H₋ with H₊ := PV∫_{S₊}s/(z − y) > 0 on S₊ (Theorem Q (iii)'s argument: g_σ
decreasing, Y = ∞ so the PV term is 0) and H₋(z) := ∫_{S₋}s(y)dy/(z − y) > 0 (z − y > 0). Then φ′ = −((z − a)/z)^{1/2}H < 0 (Theorem Q (iii),
sign convention U^μ = −U^*): U^* increases on (a, ∞). Negative axis: for x ∈ (−z′/2, 0), (U^*)′(x) = −∫_{(0,∞)}dμ_ε(y)/(y − x) + ∫_{S₋}dμ_ε(y)/(x − y) < 0 for n ≥ n₀ (Remark below), so
U^*(x) > U^*(0) = ℓ_ε; for x ≤ −z′/2, U^*(x) ≥ (1 − \|ε\|^{1/p})log(z′/2) − 2 sup_{S₋}σ_ε > ℓ_ε for n ≥ n₀ (log\|x − y\| ≥ log\|x\| for y > 0; ∫_{S₋}σ_εlog\|x − y\|dy ≥ −2 supσ_ε, the
part \|x − y\| < 1 being ∫_{−1}^1 log\|u\|du = −2). (v) Paper 2's proof of Lemma signs (i) verbatim for Re z > 0 (\|z − y\| > \|Re z − y\| for every real
y, so Re g(z) > U^*(Re z) ≥ ℓ_ε by (i), (iv)); for Re z ≤ 0, z ∉ ℝ: \|z − y\| ≥ \|Re z − y\| again, and U^*(Re z) > ℓ_ε by (iv) (κ < 0) resp.
Paper 2's x₀-argument (κ > 0: the support lies in (0, ∞)). Lemma signs (ii): the Cauchy–Riemann computation of Paper 2 with θ_κ/n = π(1/z − ε)^{1/p}:
∂_y Re(iθ_κ/n)\|_{y=0} = −π d/dx (t_κ(x)/n) = πσ_ε(x), and ∂_y Re g(x + i0) = πν_ε(x). (vi) T is analytic near 0 (S at distance ≥ a from 0), so
ν_ε = x^{−1/2}·(analytic), and the rest is Paper 2's proof of Lemma signs (iii) verbatim. At a: write s = g_σ(y)(y − a)^{−1/2} on S₊; for x = a − η,
  ∫_{S₊}g_σ(y)(y − a)^{−1/2}dy/(y − x) = ∫_{S₊}(g_σ(y) − g_σ(x))(y − a)^{−1/2}dy/(y − x) + g_σ(x)·(π/√η − 2(Y − a)^{−1/2} + O(η))
(the last integral in closed form, 2η^{−1/2}arctan(((Y − a)/η)^{1/2}); for Y = ∞ it is exactly π/√η), so πν_ε = πσ_ε + (a − x)^{1/2}x^{−1/2}·(h + O(η))
with h analytic near a (the S₋-part is analytic there) and h(a) as stated; each of its terms is negative (g_σ strictly decreasing; g_σ(a) > 0;
s > 0 and y − a < 0 on S₋). Analyticity in ε: in the u-variables all integrals are integrals of (u − ε)^{1/p−1}(1 − au)^{−1/2}×(rational in u, x)
over (ε, 1/a), which after v = (u − ε)/(1/a − ε) are over a fixed interval with integrands analytic in (ε, a, x). ∎
(PROVED-mod-cite: JZC_M1 Theorem Q (i)–(iii) (REVIEWED, two readers; updated 2026-10-23); Paper 2 Lemma g-function, Lemma signs (proofs read for this note).
NUMERICAL: w_plt1_equilibrium [B]–[I].)

*Remark (the negative axis for κ < 0, clean form).* For x ∈ (−z′/2, 0): ∫_{(0,∞)}dμ_ε(y)/(y − x) ≥ ∫_0^a ν_ε(y)dy/(y + z′/2) ≥ m_b/(a + z′/2)
with m_b := μ_ε([0, a]) (continuous in ε, positive: at ε = 0 the lattice band mass), while ∫_{S₋}dμ_ε/(x − y) ≤ \|ε\|^{1/p}/(z′/2) =
2\|ε\|^{1+1/p}. So (U^*)′ < 0 there once 2\|ε\|^{1+1/p}(a + z′/2) < m_b, i.e. \|ε\|^{1/p}(1 + 2a\|ε\|) < m_b, true for n ≥ n₀. In the frame only \|z\| ≤ R₁ and the
contour matter; the far part of the negative axis enters only through U^* > ℓ_ε (Re φ < 0), proved above.

## 3. The branch rule and the frame

### 3.1 The jumps of g_κ (Lemma 3)

For κ > 0, μ_ε is supported in [0, z_*] ⊂ [0, ∞), and the principal g(z) := ∫log(z − y)dμ_ε(y) (Paper 2's (eq:g)) has g₊ − g₋ = 2πiμ_ε((x, ∞))
on (0, ∞): = 2πit_κ(x)/n on (a, z_*) (since ∫_x^{z_*}σ_ε = (t_κ(x) − t_κ(z_*))/n and t_κ(z_*) = 0), 0 on (z_*, ∞), 2πi on (−∞, 0).
For κ < 0 the support passes through ∞ (S₊ → +∞, S₋ from −∞), and the principal branch is the wrong one:

**Lemma 3.** Let κ < 0. (a) For the principal g: on S₊, n(g₊ − g₋) = 2πi(t_κ(x) − γ); on (−z′, 0), n(g₊ − g₋) = 2πi(n − γ); on S₋,
n(g₊ − g₋) = 2πi(n − γ + t_κ(x)). So e^{ng} carries the constant phase e^{−2πiγ} on ℝ∖[0, a] relative to the κ-node phase e^{2iθ_κ}, and no
elementary factor analytic near [0, a] removes it without changing the exponent at 0 or at a.
(b) Define μ_w := ζ_*μ_ε (a positive measure of mass 1 on (0, ∞) in the w-plane: band ζ([0, a]) = [0, a_w], density there ν_ε∘ζ^{−1}·(ζ^{−1})′,
saturated (a_w, ∞) with the lattice density (1/p)w^{−1/p−1}), G_w(w) := ∫log(w − v)dμ_w(v) (principal; analytic in ℂ∖ℝ, with boundary values), and
  **g_κ(z) := G_w(ζ(z)) + log(1 − εz) + const**   (principal log(1 − εz), cut on (z_*, ∞) resp. (−∞, −z′)).
Then Re g_κ = Re g (= U^* on ℝ), so Prop 2 holds verbatim for g_κ; and n(g_κ₊ − g_κ₋) ∈ 2πit_κ(x) + 2πiℤ on S (both pieces),
∈ 2πiℤ on (−z′, 0), and g_κ = log z + C + o(1) at ∞ with boundary values from ℂ_± that differ by 2πiγ/n near ∞ (exactly matching the jump of
F♮_κ there, Prop 3 (ii)). For κ > 0 the same definition gives the principal g up to an additive constant.
*Proof.* (a) μ_ε((x, ∞)) for x ∈ S₊: ∫_x^∞σ_ε = (t_κ(x) − t_κ(+∞))/n and t_κ(+∞) = n\|ε\|^{1/p} = γ; for x ∈ (−z′, 0):
μ_ε((x, ∞)) = μ_ε((0, ∞)) = 1 − μ_ε(S₋) = 1 − γ/n (μ_ε(S₋) = (t_κ(−∞) − t_κ(−z′))/n = (γ − 0)/n); for x ∈ S₋ add ∫_x^{−z′}σ_ε = t_κ(x)/n. An
elementary factor with the constant jump e^{2πiγ} on ℝ∖[0, a] and none on (0, a) is ((z − a)/z)^{±γ} times a factor analytic across ℝ, which
has exponent ∓γ at 0 (a Szegő shift) and ±γ at a. (b) Möbius identity: z − y = (ζ(z) − ζ(y))(1 − εz)(1 − εy) (with ζ(z)(1 − εz) = z), so
log\|z − y\| = log\|ζ(z) − ζ(y)\| + log\|1 − εz\| + log\|1 − εy\|; integrate against μ_ε: Re g_κ = Re g + const. Jumps: ζ maps (0, ∞) onto
(0, z′) and (−∞, −z′) onto (z′, ∞), orientation preserving (ζ(ℂ_±) = ℂ_±), and (−z′, 0) onto (−∞, 0). G_w₊ − G_w₋ = 2πiμ_w((w, ∞)) on
(0, ∞) and = 2πi on (−∞, 0); on the w-saturated set μ_w((w, ∞)) = ∫_w^∞(1/p)v^{−1/p−1}dv = t(w)/n = t_κ(z)/n. log(1 − εz) jumps by ±2πi
on its cut. At ∞: ζ(z) → z′ ∈ (a_w, ∞) (κ < 0), where G_w is continuous from each side with G_w₊ − G_w₋ = 2πit(z′)/n = 2πiγ/n, and
log(1 − εz) = log z + log\|ε\| + o(1). ∎ (PROVED (elementary). NUMERICAL: w_plt1_equilibrium [H] (the masses); the n⁻¹ test of §5 excludes
the principal-branch/Theorem-Q-on-(0, ∞) alternative.)

*Consequence (the constraint for κ < 0).* Theorem Q applied verbatim to σ_ε on (0, ∞) (dropping S₋) is a legitimate equilibrium problem but
the wrong g for the frame: its edge differs from a_ε by the relative amount −p\|ε\|^{1/p}(1 + O(ε)) = −pγn^{−1}(1 + …) ([A] control), i.e. it
would put a κ-dependent term −pγ into the n^{−1} coefficient, and its g has the phase defect of (a). The correct object is the κ-node constraint
over all phantom indices t_κ ∈ (0, ∞), which for κ < 0 includes S₋.

### 3.2 The scalar, the band weight, the hard edge (Prop 3)

Let F_δ := D_δB_in^δKe^{χ_δ} in S_in, B_out^δKe^{χ_δ} in S_out (G3 §2) but with **K := (a_w − w)^{−1/2}** (Paper 2 app_outer: K = (4c − z)^{−1/2};
only (O1)–(O2) see K, and H_n^δ = (D̃_δB_in^δe^{χ_δ})^{−2} does not contain it), F♮_δ(w) := F_δ(w)(−w)^{−δ} (G3 Cor 5), and
  **F♮_κ(z) := F♮_δ(ζ(z))**,  F̃♮_κ := F♮_κ/κ_±^κ,  κ_±^κ := 1/(1 − e^{∓2iθ_κ}) = κ_±^δ∘ζ.

**Proposition 3.** Assume (S<) and n ≥ n₀.
(i) *(O1) with θ_κ and normalisation.* F♮_κ is analytic and zero-free off (0, z_*] (κ > 0) resp. off (0, ∞) ∪ (−∞, −z′] (κ < 0), F♮_κ₊ = F♮_κ₋e^{2iθ_κ}
  on S₊∖{X_k} beyond a and on S₋, no jump on (−∞, 0)∖S₋ and on (z_*, ∞); F♮_κ is continuous and nonzero at z_* (κ > 0) and at ∞, and
  ϰ_∞ := F♮_κ^{−1}e^{n(g_κ − Log z)} has no jump near ∞ and a nonzero limit there (Paper 2 Lemma normalisation for the pair (F♮_κ, g_κ)).
(ii) *(O2) and the band weight.* F̃♮_κ is analytic and zero-free near [0, X₁ + δ′]∖[a, ∞) with F̃♮_κ₊ = −F̃♮_κ₋ on (a, X₁ + δ′), and with
  H^♭_κ := 1/((a_ε − z)F̃♮_κ(z)²)·(sector phases as in G3 Cor 5),
  W_κ/F̃♮_κ² = 𝗐_nz^{β′}(a_ε − z)H^♭_κ(z)·e^{∓2πiδ}e^{∓iπα}-type lip phases exactly as in the Hurwitz α-frame, and
  **H^♭_κ(z) = (a_w/a_ε)·H_n^δ(ζ(z))·(1 − εz)^{1/p−2a}**,  W_κ = 𝗐_nz^αr_n (L W-out.2), r_n = (1 − εz)^{1/p−1}.
  This is L K.1's H_n^κ with the branched gauge factor e^{−2π cot(π/p)ρ₁} (the obstruction of P K.14) removed; the lip (2,1) entries carry
  e^{±2πiδ} only — no e^{±2πiρ₁}: the α-frame lip match of G1u_plt1 L P2 (ii) holds exactly with ρ♮_κ := W̃_κ/D_{W₀^κ}.
(iii) *Toda times.* The Taylor coefficients at 0 of log H^♭_κ, with log H_n^δ(w) = const − 2Σ_k m_k(δ)w^k + O(n^{−(J+1)p}) (G23plt1 F.1_δ, Rem H:
  m_k = ζ(−kp, a)/(kn^{kp})), are −μ^κ_{n,j} = −(2Z_κ(−j)/j − B_j)n^{−jp}, Z_κ(−j) = Σ_l binom(j, l)κ^{j−l}ζ(−lp, a), B_j = −(1/p − 1)κ^j/j —
  W's Toda times (JZC_W §1.2; the same as P W-out.5 (i) for p > 1).
(iv) *Hard edge (PROOF SKETCH).* Near 0: φ_ε = ∓iπ − 2f_ε^{1/2} (Prop 2 (vi)); the Bessel variable is n²f_ε(z) with f_ε = f + O(ε) analytic,
  univalent, uniformly in \|ε\| ≤ ε₀; the band factor satisfies G1u_plt1 L P1 with ζ: 𝒢_δ(ζ(z)) − 𝒢_δ(ζ(x)) = (ζ(z) − ζ(x))I(ζ(z), ζ(x)) and
  ζ(z) − ζ(x) = (z − x)/((1 − εz)(1 − εx)), so \|log h°_κ(z)\| ≤ Cn^{−p}\|z\| and L_h-type bounds \|log(D²/h°)\| ≤ Cn^{−p}\|z\|^{1/2} hold n-uniformly
  on \|z\| ≤ R₁ (the extra factor (1 − εz)^{1/p−2a} is analytic with log = O(n^{−p}\|z\|)). Hence L P2–P5 and Prop G1u′ transfer with f_ε in place
  of f, Szegő exponent β′ = α + 2δ, Bessel order α, and band [0, a_ε].
*Proof of (i)–(iii).* (i) G3 Prop 4 and Cor 5: F♮_δ is analytic and zero-free off [0, ∞), F♮_δ₊ = F♮_δ₋e^{2πit(w)} on (a_w, ∞)∖{nodes} (the jump
−e^{2iθ_δ} of D_δ, −1 of K beyond a_w, e^{2πiδ} of (−w)^{−δ}), no jump on (−∞, 0), and F♮_δ(w) → (2πn)^{−½−δ} as w → ∞ (Prop 4; with
K = (a_w − w)^{−1/2} in place of (4c − w)^{−1/2} the limit is the same: (a_w − w)/(4c − w) → 1). Compose with ζ: ℂ_± → ℂ_± (orientation
preserved), t∘ζ = t_κ. κ > 0: (0, z_*) → (0, ∞), (z_*, ∞) ∪ (−∞, 0) → (−∞, 0) through w = ∞ ↔ z = z_*; so F♮_κ jumps by e^{2πit_κ} on
(ζ^{−1}(a_w), z_*) = (a_ε, z_*), not at all on (z_*, ∞) ∪ (−∞, 0), and is continuous at z_* with the value (2πn)^{−½−δ} (the o(1) of Prop 4 is
uniform in arg w). At z = ∞, w = −z_* is a regular point of F♮_δ: F♮_κ(∞) = F♮_δ(−z_*) ≠ 0. g_κ = g has the jump 2πit_κ/n on (a, z_*) and none on
(z_*, ∞) (Lemma 3), so ϰ_∞ has no jump on (z_*, ∞) or (−∞, 0) (n ∈ ℤ) and tends to F♮_δ(−z_*)^{−1}e^{nC}. κ < 0: ζ maps (0, ∞) → (0, z′),
(−∞, −z′) → (z′, ∞), (−z′, 0) → (−∞, 0), z = ∞ → w = z′ (an interior point of the w-saturated set); F♮_κ jumps by e^{2πit_κ} on S₊ beyond a and
on S₋, and by Lemma 3 (b) so does e^{ng_κ}; at ∞ both boundary values of F♮_δ(ζ(z)) and of e^{n(g_κ − Log z)} differ by e^{2πiγ}, so ϰ_∞ is
continuous there. (ii) The lens scalar: F̃♮_δ = F♮_δ/κ_±^δ is analytic and zero-free near (0, a_w) with F̃₊ = −F̃₋ beyond a_w (Paper 2 (O2) via K);
compose. Band weight: in w (G3 Cor 5, H-d), 1/F̃♮_δ(w)² = (a_w − w)H_n^δ(w)·(−w)^{2δ}·(lip/band phases); at w = ζ(z),
(a_w − ζ(z)) = (a_w − z(1 + εa_w))/(1 − εz) = (a_w/a_ε)(a_ε − z)/(1 − εz) (since 1 + εa_w = a_w/a_ε), and ζ^{2δ} = z^{2δ}(1 − εz)^{−2δ}. Hence
W_κ/F̃♮_κ² = 𝗐_nz^{α+2δ}(a_ε − z)·(a_w/a_ε)H_n^δ(ζ)(1 − εz)^{1/p−1−1−2δ}·(phases), and 1/p − 2 − 2δ = 1/p − 2a. The phases are those of the
Hurwitz α-frame (the lip factor of (−w)^{−δ} is e^{±2πiδ}; no other branched factor occurs, since the jump of e^{ng_κ} matches e^{2iθ_κ} exactly).
(iii) log H^♭_κ = −2Σ_km_k(δ)ζ(z)^k + (1/p − 2a)log(1 − εz) + const; ζ^k = z^kΣ_l binom(k+l−1, l)(εz)^l. The coefficient of z^j is
−Σ_{k≤j}(2ζ(−kp, a)/k)binom(j−1, k−1)κ^{j−k}n^{−jp} − (1/p − 2a)κ^jn^{−jp}/j. Since (2/j)binom(j, l) = (2/l)binom(j−1, l−1) (l ≥ 1) and the l = 0 term
of −(2/j)Z_κ(−j) is −(2/j)κ^jζ(0, a) = −(1 − 2a)κ^j/j, −(2Z_κ(−j)/j − B_j) has the κ^j/j-coefficient −(1 − 2a) − (1/p − 1) = 2a − 1/p, the same. ∎
(PROVED-mod-cite: G3 Prop 4, Cor 5 [REVIEWED]; G23plt1 F.1_δ, Rem H; Paper 2 app_outer (K), Lemma jumpsV algebra; L K.1 [REVIEWED] for the
comparison. NUMERICAL: w_plt1_equilibrium [J] (the Toda algebra at three parameter sets, to 10⁻¹⁵).)

What (ii) achieves, in the language of P K.14: the lattice-g route had to put the index offset ρ₁ = t − t_κ into a gauge, whose lip phase is
e^{±2πiρ₁} with \|ρ₁\| ≍ \|κ\|n^{e(p)} → ∞ on the Bessel scale. With g_κ the offset is in the equilibrium: n(g_κ − g) is O(n^{1−p}) on the band (not
small), but it is **not** treated as a perturbation of anything — the Bessel variable is n²f_ε itself, and the only n-dependence left in the local
data is through ε = κn^{−p} → 0, analytically (Prop 2 (vi)). On the Bessel scale n(φ_ε − φ₀) = −4n(f_ε^{1/2} − f₀^{1/2}) = O(n·ε·n^{−1}) = O(\|κ\|n^{−p}).

## 4. The reduction (sketch) and the prediction

**Sketch 4 (PROOF SKETCH).** With g_κ, F♮_κ, the band [0, a_ε], the lens and contour of Paper 2 (the lips n-free for n ≥ n₀: every strict
inequality of Lemma signs/lips is uniform in \|ε\| ≤ ε₀ by Prop 2, and ζ ≈ id on compacts, so the seam arcs ζ^{−1}(Γ_±) are within O(n^{−p})
of the rays on \|z\| ≤ R₁; the saturated lips at height h₀ satisfy \|arg ζ(x + ih₀)\| ≤ h₀/x + O(n^{−p}) < πp/2, which settles W_outer §7's GAP-minor
for the contour), the κ-problem becomes the decoupled model 𝔐_ε(β′, α) — M(β′, α) of JZC_M4 §7 with the lattice g replaced by g_κ — with the
band factor exp(−P_{μ^κ_n}) up to O(n^{−(J+1)p}) (Prop 3 (iii); the transfer is L K.10 (b) without its branched part, i.e. Hc.3 Step 2 with ζ).
Running G23plt1 P2.6 (a-priori bound), G1u_plt1 Prop G1u′ (A), (B) (comparison, order-K small norm) and N.6a–c for this model gives
  n^pb_n/c = Σ_{k≤K}D_k(ε; μ^κ_n)n^{−k} + O(n^{−K−1} + n^{−1−(J+1)p}),   D₀ = A(ε) (outer parametrix on [0, a_ε]: (P₁)₁₂(P₁)₂₁ = (a_ε/4)²),
with D_k analytic in ε near 0 and D_k(0; μ) the coefficients of M(β′, α) flowed by μ (Theorem N.6). Steps not written out: (a) P2.6 for F♮_κ
(G23plt1's proof with ζ; the a-priori bound uses only (O1)–(O5)-type facts, Prop 3 (i)–(ii)); (b) N.6a–c with ε-dependent model data
(the circle data are meromorphic, with poles at 0 and a_ε only, analytic in ε; N.6c's recursion is algebraic in the data, so D_k(ε) is
analytic — uniformity of the remainders in ε is the point to check); (c) the comparison of G1u_plt1 with f_ε. None of (a)–(c) looks like an open
problem: each is a re-run of a REVIEWED proof with one more analytic parameter. **No sign condition fails** (Prop 2).

**How κ enters (answer to the brief's item 2).** (1) Through c_κ(n) = c·A(κn^{−p}), **to all orders in κn^{−p}** (Prop 1): for p < 1 these are
the terms n^{−mp} = n^{−1−pq_m} that W calls pole terms, with q_m = m − 1/p < 0 for m < 1/p; W's first-order coefficients are right for m = 1
and incomplete for m ≥ 2. (2) Through the Toda times μ^κ_{n,j} (Prop 3 (iii)), at n^{−1−jp}. (3) Through the ε-dependence of the edge data
(f_ε, f_{r,ε}, the Szegő function on [0, a_ε]): cross terms n^{−k−mp}, k ≥ 1; at first order in κ and k = 1 this is W's natural-index shift
−p(1 + m)(β′ + 1)/2·(pole coefficient). The Szegő shift β′ = α + 2δ is κ-free (1/p ∉ ℕ), so the n^{−1} coefficient is κ-free.

**Conjecture W_<1 (CONJECTURE; NUMERICAL §5).** Under (S<),
  n^pb_n/c = A(κn^{−p}) + (𝔅_n[M(α + 2δ, α); t] − 1) + Σ_{m}(W's natural-index shift of the m-th pole term) + O(n^{−1−2p}),
t_j = −2Z_κ(−j)/j + B_j. Equivalently: W with its pole layer replaced by A(ε) − 1 at every order in ε, through n^{−1−p}, plus the pure layer
n^{−mp} at every m (where it does not collide with another exponent).

## 5. Numerical test (pre-registered; Rule X)

**Protocol.** `w_plt1_predict.py` wrote `tmp/w_plt1_cache/predictions.json` at 16:12:42 (W's terms from w_common.predict, i.e. the m4_rh4 engine
with KORD = 4 and the spectral data of w_spectra.famK; the pure layer from Prop 1 (iii); internal checks: series vs root, the k = 1 identity to
10⁻²⁵; 8/8 pass). `w_plt1_test.py` generated the 7 measures afterwards (16:13–17:08) and asserts their mtimes. Measures: K = 320 000 atoms and
the **exact** κ-tail (Gauss–Jacobi in x = 1/(t^p + κ) with the factor (1 − κx)^{1/p−1}; run_measure's pure-power tail would drop it), binary128
RKPW, n ≤ 1600. Fits as w_test (median and half-range over J = 3..6 nuisance exponents and windows n ≥ 100, 200, 400), with the pool
{i + jp : i, j ≥ 0} (pure powers jp included). Pass: \|fit − EQ\| ≤ max(3 half-ranges, 2·10⁻⁶(1 + \|EQ\|)). Half-ranges are fit spreads, not error
bounds (Rule N). Nothing is fitted to the predictions.

**Results (`w_plt1_test.out`, ALL 48 CHECKS PASSED).** y_n := n^pb_n/c − 1; O := (y(κ) − y(−κ))/2, E := (y(κ) + y(−κ))/2 − y(0), κ = ½.

| case | coefficient | prediction EQ | fit (half-range) | alternatives (misses in tolerances) |
|---|---|---|---|---|
| p = 0.6, κ = 0 | n⁻¹, n^{−1.6} | −0.32, −0.0032717 | −0.3199980 (7.6·10⁻⁴), −0.0031803 (3.8·10⁻⁴) | — |
| p = 0.6, κ = +½ | n^{−0.6} | −0.6012338 | −0.6012200 (5.1·10⁻⁴) | (= W) |
| | n⁻¹ | −0.32 (κ-free) | −0.3200400 (1.2·10⁻³) | |
| | **n^{−1.2}** | **+0.2840216** (A, 2nd order) | **+0.2840145** (5.5·10⁻⁴) | W first order +0.0430: 147 |
| | n^{−1.6} | +0.4158741 | +0.4158715 (7.1·10⁻³) | no shift 18; no density 4; no share 2 |
| | n^{−1.8} | −0.1064499 | −0.1066063 (2.7·10⁻³) | W first order 15 |
| p = 0.6, κ = −½ | n^{−0.6}, n⁻¹ | +0.6012338, −0.32 | +0.6012251, −0.3199565 | naive (Thm Q on (0, ∞)) −0.509: 123 |
| | n^{−1.2} | +0.2840216 | +0.2840304 (1.6·10⁻⁴) | W1: 502 |
| | n^{−1.6} | −0.4224176 | −0.4230474 (2.5·10⁻³) | no shift 52; no density 12; no share 7 |
| | n^{−1.8} | +0.1064499 | +0.1063728 (5.3·10⁻³) | W1: 7 |
| p = 0.6, O | n^{−0.6}, n⁻¹, n^{−1.6}, n^{−1.8} | −0.6012338, 0, +0.4191458, −0.1064499 | −0.6012233, −0.0000116, +0.4190968, −0.1062505 | naive 39; no shift 40; W1 11 |
| p = 0.6, E | n⁻¹, **n^{−1.2}** | 0, **+0.2840216** | −0.0000380, **+0.2840235** (6.1·10⁻⁴) | naive 27; W1 132 |
| p = 0.75, κ = 0 | n⁻¹, n^{−1.75} | −0.275, +0.0060359 | −0.2749991, +0.0060137 | — |
| p = 0.75, κ = +½ | n^{−0.75}, n⁻¹ | −0.5728532, −0.275 | −0.5728504, −0.2749901 | |
| | n^{−1.5} | +0.2297125 | +0.2296348 (3.2·10⁻³) | W1 −0.0438: 28 |
| | n^{−1.75} | +0.3096480 | +0.3096620 (3.8·10⁻³) | no shift 27; no density 5; no share 6 |
| | n^{−2.25} | −0.0601561 | −0.0600869 (1.5·10⁻³) | W1 10 |
| p = 0.75, κ = −½ | n^{−0.75}, n⁻¹ | +0.5728532, −0.275 | +0.5728345, −0.2749999 | naive 778 |
| | n^{−1.5} | +0.2297125 | +0.2297416 (2.8·10⁻⁴) | W1 320 |
| | n^{−1.75} | −0.2975763 | −0.2976519 (3.2·10⁻⁴) | no shift 329; no density 60; no share 72 |
| | n^{−2.25} | +0.0601561 | +0.0601402 (1.4·10⁻³) | W1 10 |
| p = 0.75, O | n^{−0.75}, n⁻¹, n^{−1.75}, n^{−2.25} | −0.5728532, 0, +0.3036122, −0.0601561 | −0.5728444, −0.0000010, +0.3036225, −0.0601104 | naive 687; no shift 51; share 11; density 9; W1 11 |
| p = 0.75, E | n⁻¹, **n^{−1.5}** | 0, **+0.2297125** | −0.0000013, **+0.2297139** (1.3·10⁻³) | naive 937; W1 72 |

Truncation (p = 0.6, κ = +½, K → 2K): the fits move by ≤ 3.5·10⁻⁵ (n^{−1.6}), ≤ 5·10⁻⁸ for n^{−0.6}, n⁻¹, n^{−1.2}; all < tolerance/10.

**What the test shows.** (a) The κ-free Szegő shift at p < 1 (n⁻¹ coefficient = d₁(α + 2δ) for both signs of κ), and that the κ < 0
equilibrium must include the negative piece. (b) The pure layer is A(ε) **beyond first order**: the even part E isolates κ² and matches
A's second-order coefficient to 1.9·10⁻⁶ (p = 0.6) and 1.3·10⁻⁶ (p = 0.75); the cubic is confirmed less sharply (10–15 tol against W1).
(c) The n^{−1−p} cross term is W's (natural-index shift + κ-dependent t₁). Not tested: n^{−1−2p} and beyond (not predicted), p ≤ ½, p = 1/m,
other δ, s; W′-type dressings.

**Equilibrium checks (`w_plt1_equilibrium.out`).** [A] closed-form edge vs the quadrature root of F = 1 to ≤ 7·10⁻²⁶ at 8 (p, ε) incl. p = 0.4;
control: Theorem Q on (0, ∞) for κ < 0 moves the edge by −0.42 % … −9.2 % (≈ −p\|ε\|^{1/p}). [B] mass 1 to 10⁻¹⁵. [C] explicit = balayage
density and 0 < ν < σ at 9 points per case. [D] H > 0 on the saturated set (down to 4·10⁻⁴ next to z′-side ends). [E] direct potentials:
U* constant on the band to 1.4·10⁻¹⁰, U* − ℓ > 0 at saturated, negative-axis (κ < 0) and complex points incl. Re z < 0. [F] the hard-edge
constant C_ε; Theorem Q's density at ε = 0 equals Paper 2's ψ* = λ_pI_{x/4c}(1/p + ½, ½) to 10⁻¹⁸; (C_ε − C₀)/ε = 0.2086 (p = 0.6), 0.2155
(p = 0.75). [G] soft edge: (σ − ν)/(a − x)^{1/2} → −h(a)/(πa^{1/2}) to 10⁻⁸ with h(a) < 0. [H] mass accounting of Lemma 3 and the w-plane edge.
[I] κ > 0 up to ε = 10 (aε = 0.983): signs hold; κ < 0: ν < σ and H > 0 hold down to ε = −0.9, while ν > 0 fails there; [I′] the threshold
ε_c. [J] the Toda algebra of Prop 3 (iii) at (p, δ, κ) = (0.6, −0.3, 0.5), (0.75, −0.3, −0.5), (1.5, −0.7, 0.9). **ALL 316 CHECKS PASSED.**

## 6. Rule A (adversarial pass) — log

1. *Which equilibrium for κ < 0?* First guess: Theorem Q verbatim on (0, ∞). Its edge differs by −p\|ε\|^{1/p} relative, i.e. a κ-dependent
   n⁻¹ term, contradicting W's κ-free Z(0); tracing the jumps (Lemma 3 (a)) showed the constant phase defect e^{−2πi\|κ\|^{1/p}}. The correct
   constraint covers all phantom indices, which for κ < 0 lie on (−∞, −z′); with the Möbius branch the jumps match exactly. The data decide:
   the naive alternative misses by 27–937 tolerances.
2. *Is positivity really automatic for κ < 0?* No: the first run of [I] asserted ν > 0 at ε = −0.9 and failed for p = 0.4, 0.6, 0.75 (C_ε < 0).
   Recorded as a sharpness statement in Prop 2 (iii) with the computed ε_c; the assertion was replaced by the threshold check [I′]. ν < σ and the
   outer inequality do hold for every ε < 0 (proof: the negative piece only helps them).
3. *First order vs all orders.* Before the test, W's first-order pole value at n^{−2p} was the natural default; Prop 1 (iv) shows it differs
   from the equilibrium (1.136κ² vs 0.172κ² at p = 0.6). Both were registered; the even part decides (132–320 tol against W1).
4. *Exponent coincidences.* Pure powers mp vs {k + jp, k ≥ 1}: coincide only for p(m − j) ∈ ℕ, i.e. m − j = 5k/3 (p = 0.6) or 4k/3 (p = 0.75);
   the first is n⁻³ (m = 5, resp. m = 4): beyond the targets. 2p, 3p are isolated.
5. *Tail.* run_measure's pure-power tail would misplace the tail nodes by relative κx (≈ 2·10⁻⁴) on z ≲ 0.04 of the band; the exact κ-tail is used,
   and K → 2K changes the fits by < tolerance/10.
6. *Degenerate parameters.* δ = −0.3 so that ζ(0, a) = −0.2 ≠ 0 (the gauge share of t₁ is visible; at δ = −½ it vanishes, JZC_W_kappa Rule A 3).
   κ = ±0.5 < a^p (0.807, 0.765). p = 0.4 ≤ ½ (where 𝒞[ρ₁] does not even exist, P K.14 (iii)) is fine for g_κ ([A]–[G]) but has no measure test.
7. *Rule X.* The predictions file predates every measure (asserted). The odd/even combinations are fixed linear functionals declared in the
   prediction script. The p = 0.6 fits were also looked at once (17:0x) before the full report; nothing was changed afterwards.
8. *Weak discriminations.* At p = 0.6 the n^{−1−p} alternatives "no share"/"no density" miss by only 2–12 tolerances (fit half-ranges 3–7·10⁻³);
   the gauge share and the density factor of t₁ are therefore established only by the p = 0.75, κ < 0 row (60–72 tol) and the odd part (9–11).
9. *The structural claims are not tested by numerics alone.* Prop 3 (ii)'s exponent 1/p − 2a of (1 − εz) is algebra plus the K-at-a_w choice; an
   off-by-one power would change t₁'s κ-part by ±κ and the n^{−1−p} coefficient by ∓pcκ = ∓0.129 (p = 0.6) — 6–60 tolerances; consistent with
   the derived value only.
10. *p = 1/m.* Excluded: then t_κ(∞) is real and the frame acquires the constant phase of Z(0)'s (−κ)^m (L W-out.0); the same construction
   suggests β = α + 2δ − 2(−κ)^m (W's prediction) — HEURISTIC, not checked.

## 7. What remains

1. **Rule R** for this note (Prop 1–3, Lemma 3) (the second reader for JZC_M1 Theorem Q is done: REVIEW_JZC_M1_B.md, 2026-10-23) — Theorem Q (i)–(iii), on which Prop 2 rests (one reader so far).
2. **Sketch 4 → proof:** (a) the a-priori bound (G23plt1 P2.6) for F♮_κ = F♮_δ∘ζ; (b) N.6a–c with ε-analytic model data on [0, a_ε], with
   remainders uniform in ε; (c) G1u_plt1's comparison with the Bessel variable n²f_ε; (d) the transfer (Hc.3 Step 2 through ζ). No step is
   expected to be hard (no OBSTRUCTION found); none is written.
3. **The ε-dressing beyond first order** (D_k(ε), k ≥ 1, at second order in κ: the n^{−1−2p} coefficients, including the ε × t₁ cross term):
   not predicted. The natural-index form (n/N)^pA(κN^{−p}) is a candidate (it reproduces W at first order); untested.
4. **The same pure-layer statement for p > 1**: A(ε) predicts the κ² coefficient at n^{−2p} there too (W's O(n^{−2p}) remainder); e.g. p = 1.25
   (2p = 2.5 isolated). Not tested.
5. p ≤ ½ measures; p = 1/m (κ-dependent Z(0)); α ∉ (−1, 1); novelty (Rule L) — UNCHECKED.
